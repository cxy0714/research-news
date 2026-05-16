"""Prompt / depth shootout for evaluating summary quality.

Runs each paper through 4 variants and renders a side-by-side comparison
page so the researcher can pick the best (prompt, depth, model) combo.

Variants
--------
A         baseline: current SUMMARY_SYSTEM prompt + abstract (truncated)
B         richer prompt + abstract (full)
C-fast    richer prompt + intro / per-section first paragraph / conclusion,
          run on the fast chat model
C-deep    same content as C-fast, run on the reasoning model

Usage
-----
    python -m research_news.shootout 2408.06103 2508.12627 ...

Output: docs/shootout/<YYYY-MM-DD>.md
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

import httpx
import yaml
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

from .llm.pipeline import _extract_json
from .llm.prompts import (
    RICH_SUMMARY_SYSTEM,
    SUMMARY_SYSTEM as BASELINE_SUMMARY_SYSTEM,
)
from .llm.sjtu_client import SJTUClient
from .models import Paper

log = logging.getLogger(__name__)

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"

OUTPUT_DIR = Path("docs/shootout")


# ── arxiv metadata ────────────────────────────────────────────────────────────

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=10))
def _get(url: str, params: dict | None = None) -> str:
    with httpx.Client(timeout=40, follow_redirects=True,
                      headers={"User-Agent": "research-news-shootout/0.1"}) as c:
        r = c.get(url, params=params)
        r.raise_for_status()
        return r.text


def fetch_metadata(arxiv_id: str) -> Paper:
    xml = _get("https://export.arxiv.org/api/query",
               params={"id_list": arxiv_id})
    root = ET.fromstring(xml)
    entry = root.find(f"{ATOM}entry")
    if entry is None:
        raise RuntimeError(f"no entry for {arxiv_id}")
    title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
    abstract = " ".join((entry.findtext(f"{ATOM}summary") or "").split())
    authors = [(a.findtext(f"{ATOM}name") or "").strip()
               for a in entry.findall(f"{ATOM}author")]
    cats = [c.attrib.get("term", "")
            for c in entry.findall(f"{ARXIV_NS}category")]
    published = (entry.findtext(f"{ATOM}published") or "")[:10]
    return Paper(
        source="arxiv",
        paper_id=arxiv_id,
        title=title,
        authors=authors,
        abstract=abstract,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        categories=cats,
        published=published,
    )


# ── arxiv HTML extraction (intro + per-section first para + conclusion) ───────

INTRO_RE = re.compile(
    r"^\s*(?:\d+(?:\.\d+)?[\.\)]?[\s ]+)?introduction\b.*$", re.I,
)
CONCL_RE = re.compile(
    r"^\s*(?:\d+(?:\.\d+)?[\.\)]?[\s ]+)?"
    r"(?:conclusion[s]?|concluding remarks|discussion|summary|final remarks)\b.*$",
    re.I,
)
SECTION_NUM_RE = re.compile(r"^\s*\d+(?:\.\d+)?[\.\)]?\s+\S")


@dataclass
class DeepContent:
    intro: str
    section_leads: list[tuple[str, str]]   # (section_title, first_paragraph)
    conclusion: str
    char_count: int
    source: str   # "html" | "pdf" | "fallback-abstract"


def _clean(text: str) -> str:
    # Normalize NBSP + other unicode whitespace before collapsing
    text = text.replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def _extract_from_html(html: str) -> tuple[str, list[tuple[str, str]], str]:
    soup = BeautifulSoup(html, "lxml")
    sections = soup.find_all("section")
    if not sections:
        sections = soup.find_all("div", class_="ltx_section")

    intro = ""
    conclusion = ""
    section_leads: list[tuple[str, str]] = []

    for sec in sections:
        h = sec.find(["h1", "h2", "h3"])
        title = _clean(h.get_text()) if h else ""
        para = ""
        for p in sec.find_all("p"):
            t = _clean(p.get_text())
            if len(t) > 80:
                para = t
                break
        if not para:
            continue
        para_short = para[:1200]
        if INTRO_RE.match(title) and not intro:
            intro = para_short
        elif CONCL_RE.match(title):
            conclusion = para_short
        elif title and len(section_leads) < 8:
            section_leads.append((title, para_short))

    return intro, section_leads, conclusion


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=10))
def _get_bytes(url: str) -> bytes:
    with httpx.Client(timeout=60, follow_redirects=True,
                      headers={"User-Agent": "research-news-shootout/0.1"}) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.content


# Heuristic heading regex for plain-text PDF content. Allows numbered
# (e.g. "1 Introduction", "1. Introduction", "2.3 Methods") or unnumbered.
_PDF_HEADING_RE = re.compile(
    r"^\s*(?:(?P<num>\d+(?:\.\d+)?)[\.\)]?\s+)?(?P<title>[A-Z][A-Za-z][\w \-/&'’()]{1,80})\s*$"
)


def _extract_from_pdf_text(text: str) -> tuple[str, list[tuple[str, str]], str]:
    """Heuristic: walk lines, find heading-like lines, group paragraphs between them.

    PDF text extraction is noisy — lines wrap mid-sentence, headers/footers
    intrude. We do the simplest thing that mostly works: split by blank lines
    into paragraph blocks, treat short Title-Case blocks as candidate
    headings, and emit (heading, next-substantive-paragraph) pairs.
    """
    # Normalize whitespace per-line but keep line breaks for heading detection
    raw_lines = [l.strip() for l in text.splitlines()]
    # Group into blocks separated by blank lines; join wrapped lines inside a block
    blocks: list[str] = []
    cur: list[str] = []
    for ln in raw_lines:
        if ln:
            cur.append(ln)
        elif cur:
            blocks.append(_clean(" ".join(cur)))
            cur = []
    if cur:
        blocks.append(_clean(" ".join(cur)))

    intro = ""
    conclusion = ""
    section_leads: list[tuple[str, str]] = []
    pending_heading: str | None = None

    def is_heading(b: str) -> bool:
        if len(b) > 100 or len(b) < 3:
            return False
        return bool(_PDF_HEADING_RE.match(b))

    for b in blocks:
        if is_heading(b):
            pending_heading = b
            continue
        if pending_heading is None:
            continue
        if len(b) < 80:
            # too short to be a real paragraph; skip but keep heading
            continue
        para_short = b[:1200]
        title = pending_heading
        pending_heading = None
        if INTRO_RE.match(title) and not intro:
            intro = para_short
        elif CONCL_RE.match(title):
            conclusion = para_short   # keep latest
        elif len(section_leads) < 8:
            section_leads.append((title, para_short))

    return intro, section_leads, conclusion


def _pdf_to_text(arxiv_id: str) -> str | None:
    try:
        from pypdf import PdfReader   # lazy import; optional dep
    except ImportError:
        log.warning("pypdf not installed; cannot read PDF for %s "
                    "(pip install pypdf)", arxiv_id)
        return None
    try:
        pdf_bytes = _get_bytes(f"https://arxiv.org/pdf/{arxiv_id}")
    except Exception as e:
        log.warning("PDF download failed for %s: %s", arxiv_id, e)
        return None
    import io
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
        # Cap at first 25 pages — methods/intro/conclusion almost always fit;
        # avoids huge appendix dumps.
        max_pages = min(len(reader.pages), 25)
        chunks = []
        for i in range(max_pages):
            try:
                chunks.append(reader.pages[i].extract_text() or "")
            except Exception as e:
                log.debug("pdf page %d extract failed for %s: %s", i, arxiv_id, e)
        return "\n\n".join(chunks)
    except Exception as e:
        log.warning("pypdf parse failed for %s: %s", arxiv_id, e)
        return None


def fetch_deep_content(arxiv_id: str, abstract_fallback: str) -> DeepContent:
    """Try arxiv HTML first, fall back to PDF, then to abstract-only."""
    # 1) HTML
    try:
        html = _get(f"https://arxiv.org/html/{arxiv_id}")
        intro, leads, conclusion = _extract_from_html(html)
        chars = len(intro) + sum(len(t) + len(p) for t, p in leads) + len(conclusion)
        if chars >= 400:
            return DeepContent(intro, leads, conclusion, chars, "html")
        log.info("HTML for %s too thin (%d chars), trying PDF", arxiv_id, chars)
    except Exception as e:
        log.info("arxiv HTML unavailable for %s (%s), trying PDF", arxiv_id, e)

    # 2) PDF
    text = _pdf_to_text(arxiv_id)
    if text:
        intro, leads, conclusion = _extract_from_pdf_text(text)
        chars = len(intro) + sum(len(t) + len(p) for t, p in leads) + len(conclusion)
        if chars >= 400:
            return DeepContent(intro, leads, conclusion, chars, "pdf")
        log.warning("PDF extraction for %s also thin (%d chars), using abstract",
                    arxiv_id, chars)

    # 3) fallback
    return DeepContent("", [], "", len(abstract_fallback), "fallback-abstract")


def deep_content_to_text(d: DeepContent, paper: Paper) -> str:
    parts = [f"Abstract: {paper.abstract}"]
    if d.intro:
        parts.append(f"\n## Introduction\n{d.intro}")
    for title, para in d.section_leads:
        parts.append(f"\n## {title}\n{para}")
    if d.conclusion:
        parts.append(f"\n## Conclusion\n{d.conclusion}")
    return "\n".join(parts)


# ── variant runners ───────────────────────────────────────────────────────────

@dataclass
class VariantResult:
    name: str
    model: str
    raw: str
    parsed: dict
    prompt_tokens: int
    completion_tokens: int
    seconds: float
    content_source: str   # "abstract-600" | "abstract-full" | "html" | "fallback-abstract"
    error: str | None = None


def _run_chat(client: SJTUClient, system: str, user: str, *,
              deep: bool = False, model: str | None = None,
              max_tokens: int = 2000) -> tuple[str, int, int, float]:
    if model is None:
        model = client.model_deep if deep else client.model_fast
    before_usage = dict(client.usage.get(model, {}))
    t0 = time.monotonic()
    raw = client.chat(
        [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        model=model,
        max_tokens=max_tokens,
    )
    dt = time.monotonic() - t0
    after = client.usage.get(model, {})
    pt = after.get("prompt_tokens", 0) - before_usage.get("prompt_tokens", 0)
    ct = after.get("completion_tokens", 0) - before_usage.get("completion_tokens", 0)
    return raw, pt, ct, dt


# ── model-sweep mode (one column per model, fixed rich prompt + best content) ─

def run_model_variant(
    client: SJTUClient, paper: Paper, interests_yaml: str,
    deep_content: DeepContent, model: str,
) -> VariantResult:
    """Rich prompt + best available content (html/pdf if any, else full abstract),
    run on a specific model."""
    if deep_content.source in ("html", "pdf"):
        body = deep_content_to_text(deep_content, paper)
        content_src = deep_content.source
    else:
        body = f"Abstract: {paper.abstract}"
        content_src = "abstract-full"
    user = (
        "## Researcher interests\n" + interests_yaml +
        f"\n\n## Paper\nTitle: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Venue: {paper.venue or paper.source}\n"
        f"Categories: {', '.join(paper.categories)}\n\n"
        f"{body}\n"
    )
    try:
        raw, pt, ct, dt = _run_chat(client, RICH_SUMMARY_SYSTEM, user, model=model)
        parsed = _extract_json(raw) if raw else {}
        return VariantResult(model, model, raw,
                             parsed if isinstance(parsed, dict) else {},
                             pt, ct, dt, content_src)
    except Exception as e:
        return VariantResult(model, model, "", {}, 0, 0, 0, content_src, str(e))


def render_model_sweep(
    results: list[tuple[Paper, DeepContent, list[VariantResult]]],
    models: list[str],
    when: date,
    out_dir: Path = OUTPUT_DIR,
    label: str = "model-sweep",
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{when.isoformat()}-{label}.md"

    lines: list[str] = []
    lines.append(f"# Model Sweep — {when.isoformat()} ({label})\n")
    lines.append(
        f"固定 rich prompt + 最佳可用内容（HTML/PDF > full abstract），"
        f"沿 model 维度横向对比：{', '.join('`'+m+'`' for m in models)}.\n"
    )
    # Per-model token totals
    tot: dict[str, list[int]] = {m: [0, 0] for m in models}
    for _, _, vs in results:
        for v in vs:
            if v.model in tot:
                tot[v.model][0] += v.prompt_tokens
                tot[v.model][1] += v.completion_tokens
    lines.append("**Token 总览**（in / out per model）:")
    for m in models:
        lines.append(f"- `{m}`: {tot[m][0]} / {tot[m][1]}")
    lines.append("")

    for paper, deep, vs in results:
        lines.append(f"## [{paper.paper_id}]({paper.url}) — {paper.title}\n")
        if paper.authors:
            lines.append(f"- **作者**: {', '.join(paper.authors[:6])}"
                         f"{' et al.' if len(paper.authors) > 6 else ''}")
        if paper.venue:
            lines.append(f"- **来源**: {paper.venue}")
        if paper.categories:
            lines.append(f"- **分类**: {' · '.join(paper.categories)}")
        lines.append(f"- **内容抓取**: source=`{deep.source}`, "
                     f"intro={len(deep.intro)} chars, sections={len(deep.section_leads)}, "
                     f"conclusion={len(deep.conclusion)} chars\n")

        # One row per model
        lines.append("| model | output |")
        lines.append("|---|---|")
        for v in vs:
            cell = _render_cell(v).replace(chr(10), "<br>")
            lines.append(f"| `{v.model}` | {cell} |")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def run_variant_a(client: SJTUClient, paper: Paper, interests_yaml: str) -> VariantResult:
    """Baseline: current prompt + abstract truncated to 600 chars."""
    user = (
        "## Researcher interests\n" + interests_yaml +
        f"\n\n## Paper\nTitle: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Categories: {', '.join(paper.categories)}\n"
        f"Abstract: {paper.abstract[:600]}\n"
    )
    try:
        raw, pt, ct, dt = _run_chat(client, BASELINE_SUMMARY_SYSTEM, user, deep=False)
        parsed = _extract_json(raw) if raw else {}
        return VariantResult("A (baseline)", client.model_fast, raw,
                             parsed if isinstance(parsed, dict) else {},
                             pt, ct, dt, "abstract-600")
    except Exception as e:
        return VariantResult("A (baseline)", client.model_fast, "", {}, 0, 0, 0,
                             "abstract-600", str(e))


def run_variant_b(client: SJTUClient, paper: Paper, interests_yaml: str) -> VariantResult:
    """Richer prompt + full abstract."""
    user = (
        "## Researcher interests\n" + interests_yaml +
        f"\n\n## Paper\nTitle: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Categories: {', '.join(paper.categories)}\n"
        f"Abstract: {paper.abstract}\n"
    )
    try:
        raw, pt, ct, dt = _run_chat(client, RICH_SUMMARY_SYSTEM, user, deep=False)
        parsed = _extract_json(raw) if raw else {}
        return VariantResult("B (rich+abs)", client.model_fast, raw,
                             parsed if isinstance(parsed, dict) else {},
                             pt, ct, dt, "abstract-full")
    except Exception as e:
        return VariantResult("B (rich+abs)", client.model_fast, "", {}, 0, 0, 0,
                             "abstract-full", str(e))


def run_variant_c(
    client: SJTUClient, paper: Paper, interests_yaml: str,
    deep_content: DeepContent, *, use_deep_model: bool,
) -> VariantResult:
    """Richer prompt + intro/sections/conclusion."""
    body = deep_content_to_text(deep_content, paper)
    user = (
        "## Researcher interests\n" + interests_yaml +
        f"\n\n## Paper\nTitle: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Categories: {', '.join(paper.categories)}\n\n"
        f"{body}\n"
    )
    label = "C-deep (rich+html, reasoner)" if use_deep_model else "C-fast (rich+html, chat)"
    model = client.model_deep if use_deep_model else client.model_fast
    try:
        raw, pt, ct, dt = _run_chat(client, RICH_SUMMARY_SYSTEM, user, deep=use_deep_model)
        parsed = _extract_json(raw) if raw else {}
        return VariantResult(label, model, raw,
                             parsed if isinstance(parsed, dict) else {},
                             pt, ct, dt, deep_content.source)
    except Exception as e:
        return VariantResult(label, model, "", {}, 0, 0, 0,
                             deep_content.source, str(e))


# ── rendering ─────────────────────────────────────────────────────────────────

def _render_cell(v: VariantResult) -> str:
    if v.error:
        return f"_(error: {v.error})_"
    p = v.parsed or {}
    lines = []
    if "topic" in p:
        lines.append(f"**topic**: `{p.get('topic', '')}`")
    if p.get("summary_zh"):
        lines.append(f"**摘要**: {p['summary_zh']}")
    if p.get("key_techniques"):
        kt = p["key_techniques"]
        if isinstance(kt, list):
            lines.append("**key_techniques**: " + ", ".join(f"`{k}`" for k in kt))
    if p.get("why_relevant"):
        lines.append(f"**为什么相关**: {p['why_relevant']}")
    if not lines and v.raw:
        # Couldn't parse; show raw (truncated)
        lines.append(f"_(raw, parse failed)_\n\n```\n{v.raw[:600]}\n```")
    lines.append(
        f"\n<sub>model=`{v.model}` · source=`{v.content_source}` · "
        f"tokens in/out = {v.prompt_tokens}/{v.completion_tokens} · {v.seconds:.1f}s</sub>"
    )
    return "\n\n".join(lines)


def render_shootout(
    results: list[tuple[Paper, DeepContent, list[VariantResult]]],
    when: date,
    out_dir: Path = OUTPUT_DIR,
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{when.isoformat()}.md"

    lines: list[str] = []
    lines.append(f"# Prompt/Depth Shootout — {when.isoformat()}\n")
    lines.append(
        "对照 4 种 variant：A=baseline prompt+短摘要，B=新 prompt+完整摘要，"
        "C-fast=新 prompt+arxiv HTML 抽取（intro/各 section 首段/conclusion，chat 模型），"
        "C-deep=同样内容但 reasoner 模型。\n"
    )
    # Token totals
    tot = {"A": [0, 0], "B": [0, 0], "Cf": [0, 0], "Cd": [0, 0]}
    for _, _, vs in results:
        for v, key in zip(vs, ["A", "B", "Cf", "Cd"]):
            tot[key][0] += v.prompt_tokens
            tot[key][1] += v.completion_tokens
    lines.append("**Token 总览**（in / out）:")
    lines.append(
        f"- A: {tot['A'][0]} / {tot['A'][1]}  · "
        f"B: {tot['B'][0]} / {tot['B'][1]}  · "
        f"C-fast: {tot['Cf'][0]} / {tot['Cf'][1]}  · "
        f"C-deep: {tot['Cd'][0]} / {tot['Cd'][1]}\n"
    )

    for paper, deep, vs in results:
        lines.append(f"## [{paper.paper_id}]({paper.url}) — {paper.title}\n")
        cats = " · ".join(paper.categories) if paper.categories else ""
        lines.append(f"- **作者**: {', '.join(paper.authors[:6])}"
                     f"{' et al.' if len(paper.authors) > 6 else ''}")
        if cats:
            lines.append(f"- **arxiv 分类**: {cats}")
        lines.append(f"- **深读抓取**: source=`{deep.source}`, "
                     f"intro={len(deep.intro)} chars, sections={len(deep.section_leads)}, "
                     f"conclusion={len(deep.conclusion)} chars\n")

        # 2x2 table for compact comparison
        lines.append("| | fast chat (`deepseek-chat`) |")
        lines.append("|---|---|")
        lines.append(f"| **A** baseline + abstract-600 | {_render_cell(vs[0]).replace(chr(10), '<br>')} |")
        lines.append(f"| **B** rich prompt + full abstract | {_render_cell(vs[1]).replace(chr(10), '<br>')} |")
        lines.append(f"| **C-fast** rich prompt + html | {_render_cell(vs[2]).replace(chr(10), '<br>')} |")
        lines.append(f"| **C-deep** rich prompt + html (reasoner=`deepseek-reasoner`) | {_render_cell(vs[3]).replace(chr(10), '<br>')} |")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


# ── CLI ───────────────────────────────────────────────────────────────────────

DEFAULT_EXTRA = [
    "2605.14692",   # Anytime-valid U-statistics — higher_order_U
    "2605.13983",   # SBI for kilonovae — astrostats
    "2605.11806",   # Adaptive kernel ridge, minimax — nonparam_semipara
]


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    load_dotenv()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ids", nargs="*",
                    help="arXiv IDs (e.g. 2408.06103). URLs accepted; the ID is extracted. "
                         "Ignored when --source jmlr is used.")
    ap.add_argument("--source", choices=["arxiv", "jmlr"], default="arxiv",
                    help="Where to pull papers from.")
    ap.add_argument("--n", type=int, default=10,
                    help="Number of papers to take when --source jmlr.")
    ap.add_argument("--jmlr-vol", type=int, default=None,
                    help="Override JMLR volume number (default: current year - 1999).")
    ap.add_argument("--models", default=None,
                    help="Comma-separated list of model names. When set, runs the "
                         "model-sweep mode (rich prompt + best content, one column "
                         "per model) instead of the A/B/C/D variant mode. "
                         "Example: --models deepseek-chat,glm-5.1")
    ap.add_argument("--add-defaults", action="store_true",
                    help="Also include the built-in extra coverage papers "
                         "(U-stat, astro, kernel-ridge). Arxiv only.")
    ap.add_argument("--skip-deep-model", action="store_true",
                    help="(variant mode) Skip the C-deep (reasoner) variant.")
    ap.add_argument("--interests", default="config/interests.yaml")
    ap.add_argument("--dry-run", action="store_true",
                    help="Only fetch metadata + content; print plan; don't call LLM.")
    args = ap.parse_args(argv)

    interests_yaml = Path(args.interests).read_text(encoding="utf-8")

    # ── Phase 1: gather papers + deep content (no LLM) ────────────────────────
    fetched: list[tuple[Paper, DeepContent]] = []

    if args.source == "jmlr":
        from .scrapers.jmlr import fetch_latest as jmlr_fetch_latest
        papers = jmlr_fetch_latest(n=args.n, volume=args.jmlr_vol)
        # JMLR has no arxiv HTML; use abstract as the only content.
        for paper in papers:
            deep = DeepContent("", [], "", len(paper.abstract or ""), "fallback-abstract")
            fetched.append((paper, deep))
    else:
        id_re = re.compile(r"(\d{4}\.\d{4,6})")
        ids: list[str] = []
        for raw in args.ids:
            m = id_re.search(raw)
            if m:
                ids.append(m.group(1))
            else:
                log.warning("could not parse arxiv id from %r — skipping", raw)
        if args.add_defaults:
            for d in DEFAULT_EXTRA:
                if d not in ids:
                    ids.append(d)
        if not ids:
            ap.error("provide at least one arxiv id (or pass --add-defaults), "
                     "or use --source jmlr")

        log.info("shootout on %d arxiv papers: %s", len(ids), ids)
        for pid in ids:
            log.info("fetching metadata for %s", pid)
            try:
                paper = fetch_metadata(pid)
            except Exception as e:
                log.error("metadata fetch failed for %s: %s — skipping", pid, e)
                continue
            log.info("  title: %s", paper.title[:90])
            log.info("fetching deep content for %s", pid)
            deep = fetch_deep_content(pid, paper.abstract)
            log.info("  deep: source=%s intro=%d sections=%d conclusion=%d",
                     deep.source, len(deep.intro), len(deep.section_leads),
                     len(deep.conclusion))
            fetched.append((paper, deep))
            time.sleep(3)   # arxiv API rate limit

    if not fetched:
        log.error("no papers fetched; bailing")
        return 1

    if args.dry_run:
        print(json.dumps([
            {"id": p.paper_id, "title": p.title, "venue": p.venue,
             "abstract_chars": len(p.abstract),
             "deep_source": d.source, "intro_chars": len(d.intro),
             "n_sections": len(d.section_leads),
             "conclusion_chars": len(d.conclusion)}
            for p, d in fetched
        ], indent=2, ensure_ascii=False))
        return 0

    # ── Phase 2: LLM ──────────────────────────────────────────────────────────
    client = SJTUClient()

    if args.models:
        models = [m.strip() for m in args.models.split(",") if m.strip()]
        log.info("model-sweep mode: %d papers × %d models = %d calls",
                 len(fetched), len(models), len(fetched) * len(models))
        results: list[tuple[Paper, DeepContent, list[VariantResult]]] = []
        for paper, deep in fetched:
            log.info("running model sweep for %s", paper.paper_id)
            vs = [run_model_variant(client, paper, interests_yaml, deep, m)
                  for m in models]
            results.append((paper, deep, vs))
        out = render_model_sweep(results, models, date.today(), label=args.source)
    else:
        # Variant mode: A / B / C-fast / C-deep on the fixed default models
        results = []
        for paper, deep in fetched:
            log.info("running variants for %s", paper.paper_id)
            a = run_variant_a(client, paper, interests_yaml)
            b = run_variant_b(client, paper, interests_yaml)
            cf = run_variant_c(client, paper, interests_yaml, deep, use_deep_model=False)
            if args.skip_deep_model:
                cd = VariantResult("C-deep (skipped)", client.model_deep, "", {}, 0, 0, 0,
                                   deep.source, "skipped")
            else:
                cd = run_variant_c(client, paper, interests_yaml, deep, use_deep_model=True)
            results.append((paper, deep, [a, b, cf, cd]))
        out = render_shootout(results, date.today())

    log.info("wrote %s", out)
    log.info("total LLM calls: %d", client.calls)
    log.info("usage by model: %s", json.dumps(client.usage, indent=2))
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
