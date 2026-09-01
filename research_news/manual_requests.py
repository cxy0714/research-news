"""Deep-read papers the owner manually queued on the website.

The browser client lets the signed-in owner paste a paper link to *request* a
deep read (see ``docs/javascripts/extras.js``). Each request is stored in the
private state gist under a ``queue`` map (and the paper is added to favorites by
default). This module — run as a step of the daily pipeline — reads that queue,
deep-reads everything that hasn't been deep-read yet, and slots the results into
the day's report under a dedicated '✍️ 手动录入的论文' section.

Three kinds of request, all ending in the same deep read:

  * **arXiv link / id** → metadata from the arXiv API, PDF from arxiv.org;
  * **journal link / DOI** → :mod:`research_news.oa_pdf` resolves it to a
    downloadable PDF (landing-page citation meta tags → host rules → OpenAlex OA
    locations) and reads the publisher's own full text. This is what lets free
    journals — Observational Studies, JMLR, PMLR, PLOS, eLife, bioRxiv, … — be
    read without an arXiv preprint existing at all;
  * **bare title / citation** → LLM extracts a clean title, then an arXiv title
    search looks for a preprint; found → read it, not found → bookmark only.

Flow (mirrors the daily deep-read tail, but driven by the gist queue instead of
the score threshold):

  1. read the ``queue`` from the state gist (``gist_state.fetch_state``);
  2. drop ids already in ``data/deep_reads_index.json`` (already deep-read) — so
     re-running is cheap and a paper is never deep-read twice;
  3. resolve each request to metadata + a PDF (the three paths above);
  4. score + first-pass summary (for topic / relevance), then deep-read
     (run_type="manual") → per-paper page + index entry;
  5. (re)render the '✍️ 手动录入的论文' section on the day's report from *all* of
     that day's manual deep reads, so the section is idempotent.

Fails open: with no GIST_TOKEN (e.g. a machine without the secret) or on any
gist/network error it logs and exits 0, so it never breaks the daily commit.

Usage::

    python -m research_news.manual_requests                 # today
    python -m research_news.manual_requests --date 2026-06-18
    python -m research_news.manual_requests --dry-run
    # read one link right now, no gist involved:
    python -m research_news.manual_requests --url https://muse.jhu.edu/article/999750
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import time
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from dotenv import load_dotenv

from . import gist_state, oa_pdf
from .deep_read import generate_deep_read_report, load_index
from .highlights import HIGHLIGHTS_DIR, MANIFEST_PATH, save_highlights
from .models import Paper
from .render.markdown import (
    DOCS_DIR,
    MANUAL_SECTION_HEADING,
    _footer,
    render_manual_section,
)
from .scrapers import arxiv as arxiv_scraper

log = logging.getLogger("research_news.manual")

DAILY_MODEL = os.environ.get("DAILY_MODEL", "glm-5.1")
DEEP_READ_MODEL = os.environ.get("DEEP_READ_MODEL", "deepseek-reasoner")

# Published map (committed, like favorites_public.json) that reports the fate of
# non-arXiv "lookup" requests back to the read-only browser client: which got an
# open-access PDF, which got a preprint, which got neither (bookmark only). Also
# dedupes server-side so a link isn't re-resolved every single day. Statuses:
#   oa_pdf     — resolved to a downloadable PDF, deep read queued this run
#   resolved   — an arXiv preprint was found by title
#   deep_read  — the read exists; `deep_read` holds its doc_path
#   no_pdf     — a link/DOI, but nothing downloadable (bookmark only)
#   no_preprint— no link, and no arXiv preprint found by title (bookmark only)
RESOLVED_PATH = Path("docs/data/manual_resolved.json")
# Re-check a settled "nothing found" lookup at most this often (an OA copy or a
# preprint may appear later). Keeps the daily retry cheap for hopeless papers.
NO_PREPRINT_RETRY_DAYS = 7

_COUNT_LINE_RE = re.compile(r"^- 高相关论文 .*$", re.M)
_H1_RE = re.compile(r"^# .*$", re.M)
_FOOTER_SEP_RE = re.compile(r"\n---\n")


def _interests_text() -> str:
    path = Path("config/interests.yaml")
    return path.read_text(encoding="utf-8") if path.exists() else ""


# ── reading the queue ─────────────────────────────────────────────────────────

def queue_entries(state: dict) -> list[dict]:
    """Structured view of the gist ``queue``, in input order.

    Each item is either::

        {"key": <gist key>, "kind": "arxiv",  "arxiv_id": "2405.08525"}
        {"key": <gist key>, "kind": "lookup", "query": "<title/citation>",
         "doi": "...", "url": "..."}

    An arXiv id is recovered from paper_id / url / key (so a pasted PDF or abs
    link still resolves). Anything without an arXiv id but with query text is a
    *lookup*: resolved to a publisher PDF when it carries a link / DOI
    (:func:`_resolve_oa`), otherwise searched on arXiv by title
    (:func:`_resolve_lookups`). arXiv ids are deduped.
    """
    queue = (state or {}).get("queue") or {}
    out: list[dict] = []
    seen_arxiv: set[str] = set()
    for key, entry in queue.items():
        entry = entry or {}
        aid = (
            arxiv_scraper.normalize_arxiv_id(entry.get("paper_id") or "")
            or arxiv_scraper.normalize_arxiv_id(entry.get("url") or "")
            or arxiv_scraper.normalize_arxiv_id(key)
        )
        if aid:
            if aid in seen_arxiv:
                continue
            seen_arxiv.add(aid)
            out.append({"key": key, "kind": "arxiv", "arxiv_id": aid})
            continue
        query = (entry.get("query") or entry.get("title") or "").strip()
        if not query:
            continue
        # Recover a URL / DOI from the pasted text when the client didn't send
        # one — that's what turns an old "just a journal link" entry into an
        # open-access candidate instead of a hopeless title search.
        out.append({
            "key": key, "kind": "lookup", "query": query,
            "doi": (entry.get("doi") or "").strip() or oa_pdf.extract_doi(query),
            "url": (entry.get("url") or "").strip() or oa_pdf.extract_url(query),
        })
    return out


def queued_ids(state: dict) -> list[str]:
    """Normalized arXiv ids requested in the gist ``queue`` (input order, deduped).
    Lookup (non-arXiv) entries are not included — see :func:`queue_entries`."""
    return [e["arxiv_id"] for e in queue_entries(state) if e["kind"] == "arxiv"]


def _already_deep_read() -> set[str]:
    """paper_ids that already have a deep-read page (any date / run type)."""
    return {e.get("paper_id") for e in load_index() if e.get("paper_id")}


def favorite_deepread_ids(state: dict, *, exclude: set[str]) -> list[str]:
    """arXiv ids of *favorites that have no deep read yet* — an implicit backfill
    queue. Use case: you star a paper in a daily report that wasn't deep-read; the
    next run should deep-read it. Newest-favorited first; ``exclude`` drops ones
    already handled (already deep-read / in the explicit queue). Non-arXiv
    bookmarks (``manual_lookup`` / no arXiv id) and favorites that already link a
    deep read are skipped."""
    favs = (state or {}).get("favorites") or {}
    cands: list[tuple[str, str]] = []
    for fav in favs.values():
        fav = fav or {}
        if fav.get("manual_lookup") or fav.get("deep_read_url"):
            continue
        aid = (arxiv_scraper.normalize_arxiv_id(fav.get("paper_id") or "")
               or arxiv_scraper.normalize_arxiv_id(fav.get("url") or ""))
        if aid and aid not in exclude:
            cands.append((fav.get("added") or "", aid))
    cands.sort(key=lambda t: t[0], reverse=True)   # newest favorited first
    out: list[str] = []
    seen: set[str] = set()
    for _, aid in cands:
        if aid not in seen:
            seen.add(aid)
            out.append(aid)
    return out


# ── resolving non-arXiv "lookup" requests to an arXiv preprint ─────────────────

def _load_resolved() -> dict:
    if not RESOLVED_PATH.exists():
        return {}
    try:
        d = json.loads(RESOLVED_PATH.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def _save_resolved(m: dict) -> None:
    RESOLVED_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESOLVED_PATH.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")


def _stale(checked: str | None, days: int = NO_PREPRINT_RETRY_DAYS) -> bool:
    """True if a 'no_preprint' result is old enough to re-check on arXiv."""
    if not checked:
        return True
    try:
        return (date.today() - date.fromisoformat(checked[:10])).days >= days
    except Exception:  # noqa: BLE001
        return True


def _oa_paper_id(src: oa_pdf.PdfSource) -> str:
    """Stable id for an open-access paper: its DOI when known, else a slug built
    from the landing URL (``oa:muse.jhu.edu-999750``). Used as the deep-read /
    manifest key, so it must be filename-safe and identical across runs."""
    if src.doi:
        return src.doi.lower()
    host = (urlsplit(src.landing_url).hostname or "oa").lower().removeprefix("www.")
    tail = [p for p in urlsplit(src.landing_url).path.split("/") if p][-2:]
    return "oa:" + re.sub(r"[^A-Za-z0-9_.-]+", "-", f"{host}-{'-'.join(tail)}").strip("-")


def _paper_from_source(src: oa_pdf.PdfSource, pdf_path: Path) -> Paper:
    """Build a Paper from a resolved open-access source + its downloaded PDF."""
    title = src.title or _title_from_pdf(pdf_path) or src.landing_url
    p = Paper(
        source="oa",
        paper_id=_oa_paper_id(src),
        title=title,
        authors=list(src.authors),
        abstract=src.abstract,
        url=src.landing_url,
        categories=[c for c in (f"vol {src.volume}" if src.volume else "",
                                f"issue {src.issue}" if src.issue else "") if c],
        published=src.published,
        venue=src.venue or None,
        volume=src.volume,
        issue=src.issue,
    )
    p.pdf_url = src.pdf_url
    p.pdf_path = str(pdf_path)
    if src.arxiv_id:
        p.arxiv_url = f"https://arxiv.org/abs/{src.arxiv_id}"
    if not p.abstract:
        p.abstract = _abstract_from_pdf(pdf_path)
    return p


def _title_from_pdf(pdf_path: Path) -> str:
    """Longest of the first few lines of page 1 — a rough title for the rare page
    that carries no metadata at all. Empty string when nothing usable."""
    from .deep_read import extract_pdf_text
    head = extract_pdf_text(pdf_path, max_chars=1500)
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in head.splitlines()]
    cands = [ln for ln in lines[:12] if 20 <= len(ln) <= 200]
    return max(cands, key=len) if cands else ""


def _abstract_from_pdf(pdf_path: Path, limit: int = 2500) -> str:
    """First page-ish of text, used as the 'abstract' when the source page had
    none, so scoring / first-pass summary still have something to work with."""
    from .deep_read import extract_pdf_text
    return extract_pdf_text(pdf_path, max_chars=limit).strip()


def _extract_title(client, query: str, model: str | None) -> tuple[str, str]:
    """Use the LLM to pull a clean paper title (+DOI) out of a pasted citation,
    so the arXiv title search isn't diluted by author names / venue / year.
    Fails open: returns the raw text as the title if parsing is unavailable."""
    from .llm.pipeline import _extract_json
    system = (
        "You extract bibliographic fields from a single citation string. "
        'Return ONLY JSON: {"title": "<the paper title, no authors/venue/year>", '
        '"doi": "<DOI if present, else empty>"}.'
    )
    try:
        raw = client.chat(
            [{"role": "system", "content": system},
             {"role": "user", "content": query}],
            model=model, max_tokens=300,
        )
        obj = _extract_json(raw)
        if isinstance(obj, dict) and (obj.get("title") or "").strip():
            return obj["title"].strip(), (obj.get("doi") or "").strip()
    except Exception as e:  # noqa: BLE001 — fall back to the raw text
        log.warning("citation title parse failed (%s); using raw text", e)
    return query.strip(), ""


# Where a resolved open-access PDF is parked before its topic is known (the
# topic decides the final data/highlights/<topic>/ folder). Under the
# gitignored highlights dir, so PDFs are never committed.
OA_CACHE_DIR = HIGHLIGHTS_DIR / "_oa"


def _resolve_oa(lookups: list[dict], resolved: dict, *,
                run_date: str) -> list[Paper]:
    """Resolve every lookup that carries a **link or DOI** to a downloadable PDF.

    This is the open-access path: a pasted journal URL is enough — the landing
    page's citation meta tags give title / authors / venue / DOI and usually the
    PDF link itself (see :mod:`research_news.oa_pdf`). Papers that resolve here
    are deep-read from the publisher's own full text, so a free journal no longer
    needs an arXiv preprint to be readable.

    Updates ``resolved`` in place (status ``oa_pdf`` on success, ``no_pdf`` when
    nothing downloadable was found) and returns the Papers to deep-read. Entries
    left at ``no_pdf`` fall through to the arXiv title search afterwards.
    """
    out: list[Paper] = []
    for e in lookups:
        key = e["key"]
        prev = resolved.get(key) or {}
        status = prev.get("status")
        if status in ("deep_read", "oa_pdf", "resolved"):
            continue                       # settled by an earlier run
        if status in ("no_pdf", "no_preprint") and not _stale(prev.get("checked")):
            continue                       # checked recently, don't re-fetch yet
        if not (e.get("url") or e.get("doi")):
            continue                       # pure title → arXiv search handles it

        target = e.get("url") or e["doi"]
        try:
            src = oa_pdf.resolve(target, doi=e.get("doi") or "")
        except Exception as ex:  # noqa: BLE001 — fail open, try the arXiv path
            log.warning("OA resolve failed for %s: %s", target, ex)
            src = None
        pdf = None
        if src:
            pid = _oa_paper_id(src)
            pdf = oa_pdf.download(src, OA_CACHE_DIR / f"{_slug(pid)}.pdf")
        if not (src and pdf):
            resolved[key] = {"status": "no_pdf", "title": prev.get("title") or "",
                             "doi": e.get("doi") or "", "url": e.get("url") or "",
                             "query": e["query"], "checked": run_date}
            log.info("manual lookup %s → no open PDF", target)
            continue

        paper = _paper_from_source(src, pdf)
        resolved[key] = {"status": "oa_pdf", "paper_id": paper.paper_id,
                         "title": paper.title, "doi": src.doi,
                         "url": paper.url, "pdf_url": paper.pdf_url,
                         "venue": paper.venue or "", "query": e["query"],
                         "checked": run_date}
        log.info("manual lookup %s → OA PDF (%s, %s)", target, paper.paper_id,
                 paper.venue or "venue unknown")
        out.append(paper)
    return out


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_") or "unknown"


def _resolve_lookups(lookups: list[dict], resolved: dict, *, client,
                     run_date: str, model: str | None) -> set[str]:
    """Resolve each non-arXiv lookup to an arXiv preprint by title, updating the
    ``resolved`` map in place. Returns the set of arXiv ids that should be
    deep-read (newly resolved this run, plus prior 'resolved' not yet read)."""
    from .scrapers import crossref

    to_read: set[str] = set()
    for e in lookups:
        key = e["key"]
        prev = resolved.get(key) or {}
        status = prev.get("status")
        if status == "deep_read":
            continue                      # already found + read
        if status == "resolved" and prev.get("arxiv_id"):
            to_read.add(prev["arxiv_id"])  # found before, (re)confirm the read
            continue
        if status == "no_preprint" and not _stale(prev.get("checked")):
            continue                      # checked recently, don't re-search yet

        title, doi = e["query"], e.get("doi") or ""
        if client is not None:
            title, doi2 = _extract_title(client, e["query"], model)
            doi = doi or doi2

        match = None
        try:
            match = crossref._arxiv_search_match(title)
        except Exception as ex:  # noqa: BLE001 — fail open, treat as no preprint
            log.warning("arXiv title search failed for %r: %s", title[:60], ex)

        if match:
            arxiv_id = arxiv_scraper.normalize_arxiv_id(match[0])
            if arxiv_id:
                resolved[key] = {"status": "resolved", "arxiv_id": arxiv_id,
                                 "title": title, "doi": doi, "query": e["query"],
                                 "checked": run_date}
                to_read.add(arxiv_id)
                log.info("manual lookup %r → arXiv:%s", title[:60], arxiv_id)
                time.sleep(3)            # arXiv API courtesy between searches
                continue
        resolved[key] = {"status": "no_preprint", "title": title, "doi": doi,
                         "query": e["query"], "checked": run_date}
        log.info("manual lookup %r → no arXiv preprint found", title[:60])
        time.sleep(3)
    return to_read


def _finalize_resolved(resolved: dict) -> None:
    """After deep-reading, mark resolved lookups whose paper now has a deep-read
    page as ``deep_read`` (+ its doc_path) so the browser can link it. Matches on
    ``paper_id`` — an arXiv id for the preprint path, a DOI / ``oa:`` slug for the
    open-access path."""
    idx: dict[str, dict] = {}
    for e in load_index():            # newest first
        pid = e.get("paper_id")
        if pid and pid not in idx:
            idx[pid] = e
    for info in resolved.values():
        if info.get("status") in ("no_preprint", "no_pdf"):
            continue
        pid = info.get("paper_id") or info.get("arxiv_id")
        if pid and pid in idx:
            info["status"] = "deep_read"
            info["deep_read"] = idx[pid].get("doc_path")
            info["title"] = idx[pid].get("title") or info.get("title")


# ── reconstructing papers for the report section ──────────────────────────────

def _load_manifest_by_id() -> dict[str, dict]:
    if not MANIFEST_PATH.exists():
        return {}
    try:
        rows = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}
    by_id: dict[str, dict] = {}
    for row in rows or []:
        pid = row.get("paper_id")
        if pid and pid not in by_id:
            by_id[pid] = row
    return by_id


def _paper_from_manifest(row: dict) -> Paper:
    """Rebuild a Paper from a highlights-manifest entry (for re-rendering the
    section). Carries everything the per-paper block needs."""
    p = Paper(
        source=row.get("source") or "arxiv",
        paper_id=row["paper_id"],
        title=row.get("title") or row["paper_id"],
        authors=list(row.get("authors") or []),
        abstract="",
        url=row.get("url") or f"https://arxiv.org/abs/{row['paper_id']}",
        categories=list(row.get("categories") or []),
        published=row.get("published"),
        venue=row.get("venue"),
    )
    if row.get("score") is not None:
        p.score = float(row["score"])
    p.topic = row.get("topic")
    p.key_techniques = list(row.get("key_techniques") or [])
    p.novelty_flag = row.get("novelty_flag")
    p.summary_zh = row.get("summary_zh")
    p.why_relevant = row.get("why_relevant")
    return p


def manual_papers_for_date(run_date: str) -> list[Paper]:
    """Every manually-requested paper deep-read on ``run_date``, rebuilt from the
    highlights manifest, for (re)rendering the day's '✍️ 手动录入' section."""
    ids = [
        e["paper_id"]
        for e in load_index()
        if e.get("run_type") == "manual" and e.get("date") == run_date and e.get("paper_id")
    ]
    by_id = _load_manifest_by_id()
    papers = [_paper_from_manifest(by_id[pid]) for pid in ids if pid in by_id]
    papers.sort(key=lambda p: p.score or 0, reverse=True)
    return papers


# ── injecting the section into the day's report ───────────────────────────────

def _strip_existing_section(text: str) -> str:
    """Remove an existing '✍️ 手动录入' section (heading → next '## ' / footer / EOF)."""
    pattern = re.compile(
        re.escape(MANUAL_SECTION_HEADING) + r".*?(?=\n## |\n---\n|\Z)",
        re.DOTALL,
    )
    return pattern.sub("", text)


def _new_daily_page(run_date: str, section_lines: list[str]) -> str:
    """A minimal daily page carrying only the manual section (used when the day
    has no report yet — e.g. a weekend with no arXiv announcements)."""
    lines = [
        f"# {run_date} 每日 arXiv 资讯\n",
        "- 高相关论文 0 篇 · 中相关 0 篇 · 会议/Seminar 事件 0 条\n",
        "\n".join(section_lines).rstrip(),
        _footer(),
    ]
    return "\n".join(lines) + "\n"


def inject_section(text: str, section_lines: list[str]) -> str:
    """Insert the manual section just under the count line (top of the report),
    replacing any existing one. Idempotent."""
    text = _strip_existing_section(text)
    block = "\n".join(section_lines).rstrip()

    m = _COUNT_LINE_RE.search(text) or _H1_RE.search(text)
    if m:
        insert_at = m.end()
        text = text[:insert_at] + "\n\n" + block + text[insert_at:]
    else:
        text = block + "\n\n" + text
    # Collapse any 3+ blank-line runs the splice/strip may have left.
    return re.sub(r"\n{3,}", "\n\n", text)


def update_daily_page(run_date: str, *, daily_dir: Path = DOCS_DIR,
                      dry_run: bool = False) -> bool:
    """(Re)render the manual section on ``run_date``'s report. Returns True if the
    page changed (or would, under --dry-run)."""
    papers = manual_papers_for_date(run_date)
    section_lines = render_manual_section(papers)
    page = daily_dir / f"{run_date}.md"

    if not page.exists():
        if not section_lines:
            return False
        new_text = _new_daily_page(run_date, section_lines)
    else:
        text = page.read_text(encoding="utf-8")
        if not section_lines:
            # No manual papers today: only touch the page if it carries a stale
            # section to remove (otherwise leave it byte-for-byte untouched).
            if MANUAL_SECTION_HEADING not in text:
                return False
            new_text = re.sub(r"\n{3,}", "\n\n", _strip_existing_section(text))
        else:
            new_text = inject_section(text, section_lines)
        if new_text == text:
            log.info("%s: manual section already up to date (%d paper(s))",
                     run_date, len(papers))
            return False

    log.info("%s: %s manual section with %d paper(s)",
             run_date, "would write" if dry_run else "writing", len(papers))
    if not dry_run:
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(new_text, encoding="utf-8")
    return True


# ── orchestration ─────────────────────────────────────────────────────────────

def _deep_read_new(papers: list[Paper], run_date: str, *, client,
                   interests_text: str, model: str, deep_model: str) -> int:
    """Score + summary → PDF → deep-read (run_type=manual). Returns count done."""
    from .llm.pipeline import score_papers, summarize_paper

    # Open-access journal papers: look for an arXiv preprint of the same paper.
    # Not for the full text (we already have the publisher PDF) but because the
    # deep read fetches the paper's cited works *by arXiv id* — with the link, an
    # OA paper gets the same reference-grounded survey section as an arXiv one.
    oa = [p for p in papers if p.source != "arxiv" and not p.arxiv_url
          and (p.title or "").strip()]
    if oa:
        from .scrapers import crossref
        try:
            crossref.fill_arxiv_links(oa)
        except Exception as e:  # noqa: BLE001 — enrichment only, never fatal
            log.warning("arXiv link enrichment failed: %s", e)

    # Score so the deep-read page header / index carry a relevance number (the
    # renderer needs a non-None score). The user explicitly asked for these, so
    # the score is informational only — it never gates a manual paper.
    try:
        scores = score_papers(client, papers, interests_text, model=model)
    except Exception as e:  # noqa: BLE001 — proceed without scores
        log.warning("scoring manual papers failed: %s", e)
        scores = {}
    for p in papers:
        sr = scores.get(p.paper_id)
        p.score = sr[0] if sr else 0.0
        if sr:
            p.score_reason = sr[1]

    # First-pass summary for topic + context the deep read leans on.
    for p in papers:
        try:
            summarize_paper(client, p, interests_text, model=model)
        except Exception as e:  # noqa: BLE001 — deep read can proceed without it
            log.warning("first-pass summary failed for %s: %s", p.paper_id, e)

    log.info("downloading %d PDF(s) for manual deep read ...", len(papers))
    save_highlights(papers, run_date=date.fromisoformat(run_date))

    log.info("deep-reading %d manually-requested paper(s) ...", len(papers))
    generate_deep_read_report(
        papers, client, interests_text, date.fromisoformat(run_date),
        "manual", model=deep_model,
    )
    return len(papers)


def run_adhoc(inputs: list[str], run_date: str, *, client, interests_text: str,
              model: str, deep_model: str) -> int:
    """Deep-read links / DOIs / arXiv ids passed straight on the command line.

    Same resolution as the gist queue, minus the gist: arXiv ids take the arXiv
    path, everything else goes through the open-access resolver. Nothing is
    written to ``manual_resolved.json`` (there's no queue entry to report back
    on) — the deep-read page, the index and the day's section are the output.
    Use it to try a link now, or to verify the path without a GIST_TOKEN."""
    already = _already_deep_read()
    arxiv_ids, lookups = [], []
    for i, raw in enumerate(inputs):
        aid = arxiv_scraper.normalize_arxiv_id(raw)
        if aid:
            arxiv_ids.append(aid)
        else:
            lookups.append({"key": f"adhoc:{i}", "kind": "lookup", "query": raw,
                            "url": oa_pdf.extract_url(raw),
                            "doi": oa_pdf.extract_doi(raw)})

    papers = [p for p in _resolve_oa(lookups, {}, run_date=run_date)
              if p.paper_id not in already]
    new_arxiv = [a for a in dict.fromkeys(arxiv_ids) if a not in already]
    if new_arxiv:
        papers = arxiv_scraper.fetch_by_ids(new_arxiv) + papers
    skipped = (len(arxiv_ids) - len(new_arxiv))
    if skipped:
        log.info("%d input(s) already deep-read — skipped", skipped)
    if not papers:
        log.info("ad-hoc: nothing new to deep-read.")
        return 0

    n = _deep_read_new(papers, run_date, client=client,
                       interests_text=interests_text, model=model,
                       deep_model=deep_model)
    if update_daily_page(run_date) or n:
        from .render.markdown import update_index
        update_index()
    log.info("ad-hoc done: %d deep read(s)", n)
    return n


def run(*, date_str: str | None = None, dry_run: bool = False,
        model: str | None = None, deep_model: str | None = None,
        urls: list[str] | None = None) -> int:
    """Process the deep-read queue for ``date_str`` (default today).

    Returns the number of papers newly deep-read. Fails open (returns 0) when no
    GIST_TOKEN is configured or the gist can't be read. With ``urls``, the gist is
    bypassed entirely (see :func:`run_adhoc`)."""
    load_dotenv()
    run_date = date_str or date.today().isoformat()

    if urls:
        from .llm.sjtu_client import SJTUClient
        if dry_run:
            log.info("dry run: would deep-read %d ad-hoc input(s): %s",
                     len(urls), ", ".join(urls))
            return 0
        return run_adhoc(urls, run_date, client=SJTUClient(),
                         interests_text=_interests_text(),
                         model=model or DAILY_MODEL,
                         deep_model=deep_model or DEEP_READ_MODEL)

    if not os.environ.get("GIST_TOKEN", "").strip():
        log.info("GIST_TOKEN not set — skipping manual deep-read queue.")
        return 0

    try:
        state, gist_id = gist_state.fetch_state()
    except gist_state.GistAuthError as e:
        # Loud: an expired PAT silently kills the manual queue for weeks. Not a
        # crash though — the daily commit must still go through.
        log.error("跳过手动录入队列：%s", e)
        return 0
    except Exception as e:  # noqa: BLE001 — never break the daily pipeline
        log.warning("could not read state gist: %s", e)
        return 0
    if not gist_id:
        log.info("no state gist found — skipping manual deep-read queue.")
        return 0

    # Pre-warn while there's still time to rotate: a classic PAT dies at 90 days
    # and takes both this step and publish-favorites with it.
    gist_state.warn_if_expiring(log)

    # Auto-deep-read favorites that have no deep read yet (capped per run so a
    # large backlog drains over several days instead of one giant run). Toggle /
    # cap via env; read here so a .env value applies.
    auto_fav = os.environ.get("AUTO_DEEPREAD_FAVORITES", "1").strip().lower() \
        not in ("0", "false", "no", "")
    try:
        fav_limit = max(0, int(os.environ.get("MANUAL_FAV_LIMIT", "10")))
    except ValueError:
        fav_limit = 10

    entries = queue_entries(state)
    arxiv_direct = [e["arxiv_id"] for e in entries if e["kind"] == "arxiv"]
    lookups = [e for e in entries if e["kind"] == "lookup"]
    already = _already_deep_read()
    fav_pending = (favorite_deepread_ids(state, exclude=already | set(arxiv_direct))
                   if auto_fav else [])

    if not entries and not fav_pending:
        log.info("manual queue + favorites: nothing to deep-read.")
        return 0
    log.info("manual queue: %d arXiv link(s), %d non-arXiv lookup(s); "
             "%d favorite(s) awaiting deep read",
             len(arxiv_direct), len(lookups), len(fav_pending))

    if dry_run:
        new_direct = [a for a in arxiv_direct if a not in already]
        linked = [e for e in lookups if e.get("url") or e.get("doi")]
        log.info("dry run: %d new arXiv to deep-read (%s); %d lookup(s) to resolve "
                 "(%d with a link/DOI → open-access first); "
                 "%d favorite(s) to backfill (cap %d)",
                 len(new_direct), ", ".join(new_direct) or "—", len(lookups),
                 len(linked), min(len(fav_pending), fav_limit), fav_limit)
        update_daily_page(run_date, dry_run=True)
        return 0

    from .llm.sjtu_client import SJTUClient
    client = SJTUClient()
    model = model or DAILY_MODEL
    deep_model = deep_model or DEEP_READ_MODEL
    interests = _interests_text()

    resolved = _load_resolved()

    # 1a) Open access first, for every lookup carrying a link or a DOI: resolve it
    #     to the publisher's own PDF and read that. Free journals (Observational
    #     Studies, JMLR, PMLR, PLOS, eLife, …) need no preprint this way.
    oa_papers = [p for p in _resolve_oa(lookups, resolved, run_date=run_date)
                 if p.paper_id not in already]

    # 1b) Everything left — pure titles, and links with nothing downloadable —
    #     falls back to searching arXiv for a preprint by title.
    remaining = [e for e in lookups
                 if (resolved.get(e["key"]) or {}).get("status") != "oa_pdf"]
    resolved_ids = _resolve_lookups(remaining, resolved, client=client,
                                    run_date=run_date, model=model)

    # 2) Build the read set: explicit requests (pasted links + resolved preprints)
    #    are always read; favorites are an implicit backfill, capped per run.
    explicit = [a for a in dict.fromkeys(arxiv_direct + sorted(resolved_ids))
                if a not in already]
    fav_all = (favorite_deepread_ids(
        state, exclude=already | set(arxiv_direct) | set(resolved_ids))
        if auto_fav else [])
    fav_take = fav_all[:fav_limit]
    if len(fav_all) > len(fav_take):
        log.info("favorites backfill: %d this run, %d more pending (cap=%d)",
                 len(fav_take), len(fav_all) - len(fav_take), fav_limit)
    to_read = list(dict.fromkeys(explicit + fav_take))

    n_done = 0
    papers: list[Paper] = []
    if to_read:
        papers = arxiv_scraper.fetch_by_ids(to_read)
        missing = set(to_read) - {p.paper_id for p in papers}
        if missing:
            log.warning("arXiv metadata not found for: %s", ", ".join(sorted(missing)))
    papers += oa_papers
    if papers:
        n_done = _deep_read_new(
            papers, run_date, client=client, interests_text=interests,
            model=model, deep_model=deep_model,
        )

    # 3) Mark resolved lookups whose preprint now has a deep-read page, and
    #    publish the map so the browser can show status + link the read.
    _finalize_resolved(resolved)
    if resolved:
        _save_resolved(resolved)

    # 4) (Re)render the day's manual section, then refresh homepage / archives.
    changed = update_daily_page(run_date)
    if n_done or changed:
        from .render.markdown import update_index
        update_index()
    def _n(*statuses: str) -> int:
        return sum(1 for v in resolved.values() if v.get("status") in statuses)

    log.info("manual queue done: %d deep read(s) (%d from open-access PDFs); "
             "lookups: %d resolved/read, %d with no full text",
             n_done, len(oa_papers), _n("resolved", "oa_pdf", "deep_read"),
             _n("no_preprint", "no_pdf"))
    return n_done


def _setup_logging(log_dir: str = "logs") -> None:
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    Path(log_dir).mkdir(exist_ok=True)
    from .logsetup import host_tag
    log_file = Path(log_dir) / f"{date.today().isoformat()}-{host_tag()}.log"

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt, datefmt=datefmt)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root.addHandler(ch)
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(formatter)
    root.addHandler(fh)
    httpx_log = logging.getLogger("httpx")
    httpx_log.setLevel(logging.WARNING)
    fh_httpx = logging.FileHandler(log_file, encoding="utf-8")
    fh_httpx.setFormatter(formatter)
    fh_httpx.setLevel(logging.INFO)
    httpx_log.addHandler(fh_httpx)
    httpx_log.propagate = False


def main() -> None:
    _setup_logging()
    ap = argparse.ArgumentParser(
        description="Deep-read papers the owner queued on the website (the gist "
                    "'queue'), and slot them into the day's report."
    )
    ap.add_argument("--date", metavar="YYYY-MM-DD",
                    help="process for this report date instead of today")
    ap.add_argument("--model", help=f"override the score/summary model "
                                    f"(default: {DAILY_MODEL})")
    ap.add_argument("--deep-model", help=f"override the deep-read model "
                                         f"(default: {DEEP_READ_MODEL})")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be deep-read without LLM calls or writes")
    ap.add_argument("--url", metavar="LINK", action="append", dest="urls",
                    help="deep-read this link / DOI / arXiv id now, without going "
                         "through the gist queue (repeatable)")
    args = ap.parse_args()

    try:
        run(date_str=args.date, dry_run=args.dry_run,
            model=args.model, deep_model=args.deep_model, urls=args.urls)
    except Exception as e:  # noqa: BLE001 — fail open: never break the daily commit
        log.error("manual deep-read step failed (continuing): %s", e, exc_info=True)


if __name__ == "__main__":
    main()
