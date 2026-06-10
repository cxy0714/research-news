"""Deep-read high-relevance papers via LLM using their downloaded PDFs.

Each paper gets its own page at docs/deep_reads/<date>-<paper_id_slug>.md.
Metadata for all deep reads is persisted at data/deep_reads_index.json so
the homepage can show today's deep reads with titles and scores.
"""
from __future__ import annotations

import json
import logging
import os
import re
from datetime import date
from pathlib import Path

from pypdf import PdfReader

from . import citations
from .llm.prompts import DEEP_READ_ASTRO_SYSTEM, DEEP_READ_SYSTEM, TOPIC_LABELS_ZH
from .llm.sjtu_client import SJTUClient
from .models import Paper
from .scrapers import affiliations as affil
from .scrapers import references as refs

log = logging.getLogger(__name__)

DEEP_READS_DIR = Path("docs/deep_reads")
DEEP_READS_INDEX_PATH = Path("data/deep_reads_index.json")
# ~240 k chars ≈ 60 k tokens. The deep-read model has a 128k context window;
# feed (almost) the whole paper — intro + body + full bibliography — so the
# survey section can be built from what the paper actually cites. The bulk of
# the budget is intentionally left for the long structured output.
MAX_PDF_CHARS = 240_000
# How much room the structured 4-section deep read needs.
DEEP_READ_MAX_TOKENS = 24_000

# Fetch the abstracts of the paper's key cited works (Semantic Scholar) and feed
# them in so the deep read can survey the direction, not just this one paper.
# On by default; set DEEP_READ_FETCH_REFS=0 to disable. Fails open (no refs).
FETCH_REFS = os.environ.get("DEEP_READ_FETCH_REFS", "1").strip().lower() not in ("0", "false", "no", "")

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_") or "unknown"


def _clean_text(text: str) -> str:
    """Strip control characters and garbled binary that pypdf sometimes emits."""
    # Remove null bytes and non-printable control chars (keep \n \t)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]", "", text)
    # Drop tokens >120 chars (binary blobs disguised as text)
    text = re.sub(r"\S{120,}", "[…]", text)
    return text


def extract_pdf_text(pdf_path: str | Path, max_chars: int = MAX_PDF_CHARS) -> str:
    """Return up to max_chars of cleaned text from a PDF file."""
    try:
        reader = PdfReader(str(pdf_path))
        parts: list[str] = []
        total = 0
        for page in reader.pages:
            chunk = _clean_text(page.extract_text() or "")
            parts.append(chunk)
            total += len(chunk)
            if total >= max_chars:
                break
        return "\n".join(parts)[:max_chars]
    except Exception as e:
        log.warning("PDF text extraction failed for %s: %s", pdf_path, e)
        return ""


def deep_read_paper(
    client: SJTUClient,
    paper: Paper,
    interests_yaml: str,
    *,
    model: str | None = None,
) -> str:
    """Return a Markdown deep-read body for one paper (empty string on failure)."""
    pdf_text = ""
    if paper.pdf_path and Path(paper.pdf_path).exists():
        pdf_text = extract_pdf_text(paper.pdf_path)

    if not pdf_text:
        log.info("no PDF text for %s — falling back to abstract", paper.paper_id)
        pdf_text = f"Abstract:\n{paper.abstract}"

    # Include first-pass LLM output as context so the deep read can build on it.
    meta_lines = [
        f"Title: {paper.title}",
        f"Authors: {', '.join(paper.authors)}",
        f"Venue: {paper.venue or paper.source}",
        f"Relevance score: {paper.score}/10",
        f"Topic: {paper.topic}",
        f"Novelty flag: {paper.novelty_flag or 'unknown'}",
    ]
    if paper.key_techniques:
        meta_lines.append(f"Key techniques (first-pass): {', '.join(paper.key_techniques)}")
    if paper.summary_zh:
        meta_lines.append(f"First-pass summary (Chinese): {paper.summary_zh}")
    if paper.why_relevant:
        meta_lines.append(f"Why relevant (first-pass): {paper.why_relevant}")

    # Optionally pull the key cited works so the survey section can be built
    # from the actual references, not just how this paper paraphrases them.
    refs_block = ""
    if FETCH_REFS:
        arxiv_id = refs.extract_arxiv_id(paper.paper_id, paper.arxiv_url, paper.url)
        if arxiv_id:
            rows = refs.fetch_references(arxiv_id)
            # Persist the citation edges first — we want them even when the
            # cited works have no abstracts (so no prompt block), since the
            # identifiers alone build the citation graph over time.
            if rows:
                citations.record_citations(paper.paper_id, arxiv_id, rows)
            refs_block = refs.format_references_block(rows)
            if refs_block:
                # Count what actually made it into the block (each cited work is
                # rendered as a "### [i] …" heading); persist it as tuning data.
                paper.n_references = refs_block.count("### [")
                log.info("deep read %s: attached %d refs (%d chars)",
                         paper.paper_id, paper.n_references, len(refs_block))

    user = (
        f"## Researcher interests\n{interests_yaml}\n\n"
        f"## Paper metadata\n" + "\n".join(meta_lines) + "\n\n"
        + (f"{refs_block}\n" if refs_block else "")
        + f"## Full text\n{pdf_text}\n"
    )
    # Astrostat papers need a different deep-read style: the researcher lacks
    # astronomy background, so the notes must teach the physical concepts
    # before getting into the methodology.
    system_prompt = (
        DEEP_READ_ASTRO_SYSTEM if paper.topic == "astrostats" else DEEP_READ_SYSTEM
    )
    try:
        result = client.chat(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user},
            ],
            model=model,
            max_tokens=DEEP_READ_MAX_TOKENS,
        )
        log.info("deep read LLM call succeeded for %s (%d chars)",
                 paper.paper_id, len(result))
        return result
    except Exception as e:
        log.error("deep read FAILED for %s (all retries exhausted): %s", paper.paper_id, e)
        return ""


def select_deep_read_papers(
    all_scored: list[Paper],
    digest_papers: list[Paper],
    th_deepread: float,
    *,
    client: SJTUClient,
    interests_yaml: str,
    model: str | None = None,
) -> list[Paper]:
    """Choose which papers get a deep read.

    Union of two rules:
      1. score >= th_deepread, for ALL topics (the gate is loose on purpose —
         scoring only sees the abstract);
      2. an author at a whitelisted institution (config/institutions.yaml,
         US News top-50) — green-lit regardless of score.

    Green-lit papers that never got a first-pass summary (they were below the
    digest threshold) are summarized here so the deep read has topic + context.
    """
    from .llm.pipeline import summarize_paper  # local import avoids import cycle

    selected: list[Paper] = []
    seen: set[str] = set()

    def _add(p: Paper) -> None:
        if p.paper_id not in seen:
            seen.add(p.paper_id)
            selected.append(p)

    for p in digest_papers:
        if (p.score or 0) >= th_deepread:
            _add(p)

    if affil.greenlight_enabled():
        n_green = 0
        for p in all_scored:
            inst = affil.green_light(p)
            if inst:
                p.green_light_institution = inst
                if p.paper_id not in seen:
                    n_green += 1
                _add(p)
        if n_green:
            log.info("institution green-light promoted %d extra paper(s)", n_green)

    for p in selected:
        if not p.summary_zh:
            try:
                summarize_paper(client, p, interests_yaml, model=model)
            except Exception as e:  # noqa: BLE001
                log.warning("first-pass summary failed for %s: %s", p.paper_id, e)

    return selected


def _render_deep_read_page(
    paper: Paper,
    content: str,
    run_date: date,
    output_dir: Path = DEEP_READS_DIR,
) -> Path:
    """Write a single paper's deep-read page. Returns the path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{run_date.isoformat()}-{_slug(paper.paper_id)}.md"
    out = output_dir / fname
    topic_label = TOPIC_LABELS_ZH.get(paper.topic or "other", paper.topic or "other")
    authors_str = ", ".join(paper.authors[:5]) + (" et al." if len(paper.authors) > 5 else "")
    lines = [
        f"# {paper.title}\n",
        f"**作者**: {authors_str}  ",
    ]
    if paper.venue:
        lines.append(f"**来源**: {paper.venue}  ")
    lines += [
        f"**主题**: {topic_label}  ",
        f"**相关性**: {paper.score:.0f}/10  ",
    ]
    if paper.green_light_institution:
        lines.append(f"**机构绿灯**: {paper.green_light_institution}（US News 前 50，免分进入精读）  ")
    if paper.arxiv_url:
        lines.append(f"**链接**: [期刊页]({paper.url}) · [arXiv]({paper.arxiv_url})\n")
    else:
        lines.append(f"**链接**: <{paper.url}>\n")
    lines += [
        "---\n",
        content if content else "*（精读失败，请查看日志）*",
        f"\n---\n\nMaintained by 陈星宇 · "
        f"[Homepage]({HOMEPAGE_URL}) · [Source on GitHub]({REPO_URL})\n",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def _load_index(path: Path = DEEP_READS_INDEX_PATH) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _save_index(entries: list[dict], path: Path = DEEP_READS_INDEX_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")


def generate_deep_read_report(
    papers: list[Paper],
    client: SJTUClient,
    interests_yaml: str,
    run_date: date,
    run_type: str = "daily",
    *,
    model: str | None = None,
    output_dir: Path = DEEP_READS_DIR,
) -> list[Path]:
    """Generate one deep-read page per paper and update the index.

    Returns list of written page paths.
    """
    if not papers:
        log.info("deep_read: no papers — skipping")
        return []

    existing = _load_index()
    existing_by_key = {(e["paper_id"], e["date"]): e for e in existing}

    written: list[Path] = []
    new_entries: list[dict] = []
    updated = 0

    for i, paper in enumerate(papers, 1):
        log.info("deep reading %d/%d: %s", i, len(papers), paper.paper_id)
        content = deep_read_paper(client, paper, interests_yaml, model=model)
        page_path = _render_deep_read_page(paper, content, run_date, output_dir)
        written.append(page_path)

        key = (paper.paper_id, run_date.isoformat())
        prev = existing_by_key.get(key)
        if prev is not None:
            # Re-run of an indexed paper: refresh the cited-works count so the
            # tuning data reflects this run (these mutate `existing` in place).
            if paper.n_references is not None and prev.get("n_references") != paper.n_references:
                prev["n_references"] = paper.n_references
                updated += 1
            continue

        entry = {
            "date": run_date.isoformat(),
            "run_type": run_type,
            "paper_id": paper.paper_id,
            "title": paper.title,
            "topic": paper.topic or "other",
            "score": paper.score or 0.0,
            # Path relative to docs/ for use in markdown links
            "doc_path": f"deep_reads/{page_path.name}",
        }
        # Cited-works count attached to the deep read (tuning data); omitted when
        # references couldn't be fetched so the field stays meaningful.
        if paper.n_references is not None:
            entry["n_references"] = paper.n_references
        # Journal issue metadata, populated by the crossref scraper.
        # Optional so daily (arxiv) entries don't carry empty fields.
        if paper.venue:
            entry["venue"] = paper.venue
        if paper.volume:
            entry["volume"] = paper.volume
        if paper.issue:
            entry["issue"] = paper.issue
        new_entries.append(entry)
        existing_by_key[key] = entry

    if new_entries or updated:
        merged = new_entries + existing
        merged.sort(key=lambda e: (e["date"], e.get("score") or 0), reverse=True)
        _save_index(merged)
        log.info("deep reads index: %d new entries, %d ref-count update(s)",
                 len(new_entries), updated)

    return written


def load_index(path: Path = DEEP_READS_INDEX_PATH) -> list[dict]:
    """Public accessor for the deep reads index (used by update_index)."""
    return _load_index(path)
