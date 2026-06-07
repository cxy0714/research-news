"""Issue completeness check: diff what we scraped against an authoritative TOC.

Background: the Crossref issue scrape (``crossref.fetch_latest_issue``) pulls a
``rows``-capped, publication-date-sorted window and keeps works matching the
target (vol, issue). Occasionally an article is dropped — it falls outside the
window, or Crossref lacks its vol/issue metadata so it isn't bucketed into the
issue. This tool catches those by comparing against an *authoritative* table of
contents.

Authoritative sources are resolved automatically — you don't supply anything but
the journal + issue. In order:
  1. Project Euclid issue TOC (publisher-canonical) for the journals it hosts
     (AoS, AoP, AoAS, EJS, Bernoulli, Statistical Science);
  2. OpenAlex issue listing (universal — works for any journal by ISSN, and is an
     independent database from the Crossref scrape that did the missing).
Force one with ``--euclid`` / ``--openalex``, or override with a local content
PDF via ``--toc-pdf PATH`` (offline fallback).

The "scraped" side is the already-published journal page under
``docs/journals/`` (default) or a corpus snapshot (``--snapshot``). The diff is
by DOI, falling back to a normalized-title match (reusing the same helpers the
scraper uses for arxiv matching). Discussion / comment / correction items are
filtered from the authoritative set first, so intentionally-excluded entries are
never reported as missing.

Output: a "missing articles" report (title + DOI + link). With ``--refetch`` the
missing DOIs are pulled from Crossref one-by-one (a direct ``/works/{DOI}``
lookup succeeds even when the issue listing omitted them); add ``--rerun`` to
regenerate the issue page so the recovered articles are scored, summarized,
deep-read and rendered in.

Usage::

    python -m research_news.completeness --journal AoS --issue v54-i1
    python -m research_news.completeness --journal AoS --issue v54-i1 --euclid
    python -m research_news.completeness --journal AoS --issue v54-i1 --refetch --rerun
    python -m research_news.completeness --journal AoS --issue v54-i1 --toc-pdf contents.pdf
"""
from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path
from typing import NamedTuple

from .models import Paper
from .scrapers.crossref import _is_discussion_content, _title_match, fetch_work

log = logging.getLogger("research_news.completeness")

# A DOI as it appears in text. Kept permissive on the suffix; trailing
# punctuation is trimmed by _norm_doi.
_DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.I)

# Paper heading on a rendered journal page:
#   "### N. [DOI](url) — Title"  or  "### N. [DOI](url) · [arXiv](au) — Title"
_PAGE_ENTRY_RE = re.compile(
    r"^#{2,6}\s+\d+\.\s+\[([^\]]+)\]\(([^)]+)\).*?\s[—-]\s(.+)$"
)

# Header / boilerplate lines that are never article titles.
_NON_TITLE_RE = re.compile(
    r"^\s*(contents|table of contents|volume|vol\.?|issue|number|no\.?|"
    r"part|index|errata|in this issue|annals|biometrika|journal|issn|"
    r"copyright|©|institute of|page)\b",
    re.I,
)


class TocEntry(NamedTuple):
    title: str
    doi: str | None = None
    url: str | None = None


# ── normalization helpers ──────────────────────────────────────────────────────

def _norm_doi(d: str | None) -> str:
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d.rstrip(" .,;)")


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def _strip_pageno(s: str) -> str:
    """Drop dotted leaders and a trailing page number ('Some title .... 2569')."""
    s = re.sub(r"[.…\s]{2,}\d+\s*$", "", s)   # "title .... 2569"
    s = re.sub(r"\s{2,}\d+\s*$", "", s)             # "title    2569"
    return s.strip()


def _looks_like_title(s: str) -> bool:
    s = _clean(s)
    if len(s) < 15 or " " not in s:
        return False
    if _NON_TITLE_RE.match(s):
        return False
    if not re.search(r"[a-z]", s):    # all-caps banners aren't titles
        return False
    if re.fullmatch(r"[\d\s.…–-]+", s):  # pure page-number rows
        return False
    return True


# ── authoritative TOC: content PDF ──────────────────────────────────────────────

def parse_toc_text(text: str) -> list[TocEntry]:
    """Parse a journal 'Contents' page's plain text into article entries.

    Separated from PDF extraction so it can be unit-tested on strings. Two
    strategies: when the text carries DOIs, one entry per DOI (title = the text
    around it, looking back a line if the DOI sits alone); otherwise title-like
    lines become title-only entries (the diff still matches them by title).
    """
    raw_lines = [ln.rstrip() for ln in text.splitlines()]
    lines = [ln for ln in raw_lines if ln.strip()]

    entries: list[TocEntry] = []
    if any(_DOI_RE.search(ln) for ln in lines):
        for i, ln in enumerate(lines):
            m = _DOI_RE.search(ln)
            if not m:
                continue
            doi = _norm_doi(m.group(0))
            # The title is almost always the text *before* the DOI; the text
            # after it is the page number. Strip page numbers before collapsing
            # whitespace so dotted/spaced leaders are still recognizable.
            before = _clean(_strip_pageno(ln[: m.start()]))
            after = _clean(_strip_pageno(ln[m.end():]))
            if _looks_like_title(before):
                title = before
            else:
                # DOI alone (or with only a page no.) → look back a line or two.
                title = _clean((before + " " + after).strip())
                look = i - 1
                # Absorb only preceding *continuation* lines (wrapped titles).
                # A previous line that has its own DOI is a different article —
                # stop there so we never merge two entries.
                while (not _looks_like_title(title)) and look >= 0 and (i - look) <= 2:
                    if _DOI_RE.search(lines[look]):
                        break
                    title = _clean(_strip_pageno(lines[look]) + " " + title)
                    look -= 1
            entries.append(TocEntry(_clean(title), doi, f"https://doi.org/{doi}"))
    else:
        for ln in lines:
            t = _strip_pageno(ln)
            if _looks_like_title(t):
                entries.append(TocEntry(_clean(t)))

    # Dedup by DOI, then by normalized title.
    out: list[TocEntry] = []
    seen_doi: set[str] = set()
    seen_title: set[str] = set()
    for e in entries:
        if e.doi:
            if e.doi in seen_doi:
                continue
            seen_doi.add(e.doi)
        tnorm = re.sub(r"[^\w\s]+", " ", e.title.lower()).strip()
        if not e.doi:
            if tnorm in seen_title or not tnorm:
                continue
        seen_title.add(tnorm)
        out.append(e)
    return out


def extract_toc_from_pdf(path: str | Path, *, max_pages: int = 6) -> list[TocEntry]:
    """Pull article entries from the front-matter 'Contents' page(s) of a PDF."""
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    texts = []
    for page in reader.pages[:max_pages]:
        texts.append(page.extract_text() or "")
    full = "\n".join(texts)
    # Narrow to the Contents region if a clear marker exists; otherwise parse all
    # the front pages (a content PDF is mostly the TOC anyway).
    m = re.search(r"(table of contents|contents)\b", full, re.I)
    region = full[m.start():] if m else full
    entries = parse_toc_text(region)
    log.info("PDF TOC %s: %d article entr%s parsed",
             Path(path).name, len(entries), "y" if len(entries) == 1 else "ies")
    return entries


# ── scraped side: published page / snapshot ─────────────────────────────────────

def page_entries(path: Path) -> list[TocEntry]:
    """(doi, url, title) for each paper on a rendered journal page."""
    if not path.exists():
        return []
    out: list[TocEntry] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _PAGE_ENTRY_RE.match(line)
        if m:
            out.append(TocEntry(_clean(m.group(3)), _norm_doi(m.group(1)), m.group(2)))
    return out


def snapshot_entries(snapshot: Path, full_venue: str, vol: int, iss: int | None) -> list[TocEntry]:
    from .journals import _load_papers, _paper_in_issue
    out: list[TocEntry] = []
    for p in _load_papers(snapshot):
        if p.venue == full_venue and _paper_in_issue(p, vol, iss):
            out.append(TocEntry(_clean(p.title), _norm_doi(p.paper_id), p.url))
    return out


# ── diff ────────────────────────────────────────────────────────────────────────

def diff(authoritative: list[TocEntry], scraped: list[TocEntry]) -> list[TocEntry]:
    """Authoritative entries absent from the scraped set. Match by DOI first,
    then normalized title; discussion/comment items are dropped from the
    authoritative set so they're never reported as missing."""
    scraped_dois = {e.doi for e in scraped if e.doi}
    scraped_titles = [e.title for e in scraped if e.title]
    missing: list[TocEntry] = []
    for a in authoritative:
        if _is_discussion_content(a.title):
            continue
        if a.doi and a.doi in scraped_dois:
            continue
        if a.title and any(_title_match(a.title, t) for t in scraped_titles):
            continue
        missing.append(a)
    return missing


def format_report(missing: list[TocEntry], *, journal: str, vol: int,
                  iss: int | None, n_auth: int, n_scraped: int) -> str:
    iss_label = f"i{iss}" if iss is not None else "(whole volume)"
    head = (f"# Completeness: {journal} v{vol} {iss_label}\n\n"
            f"- authoritative TOC: {n_auth} article(s)\n"
            f"- scraped/published: {n_scraped} article(s)\n"
            f"- **missing: {len(missing)}**\n")
    if not missing:
        return head + "\n✅ no missing articles.\n"
    lines = [head, "\n## Missing articles\n"]
    for i, e in enumerate(missing, 1):
        doi = e.doi or "—"
        link = e.url or (f"https://doi.org/{e.doi}" if e.doi else "—")
        lines.append(f"{i}. {e.title}\n   - DOI: `{doi}`\n   - link: {link}")
    return "\n".join(lines) + "\n"


# ── refetch ─────────────────────────────────────────────────────────────────────

def resolve_authoritative(issn: str, full_venue: str, vol: int, iss: int | None,
                          *, source: str = "auto",
                          toc_pdf: Path | None = None) -> tuple[list[TocEntry], str]:
    """Obtain the issue's authoritative article list automatically.

    ``source``: 'auto' (Euclid → OpenAlex), 'euclid', 'openalex', or 'pdf'.
    Returns (entries, source_used). A local ``toc_pdf`` always wins when given.
    """
    if toc_pdf or source == "pdf":
        if not toc_pdf:
            log.error("source 'pdf' needs --toc-pdf PATH")
            return [], "pdf"
        return extract_toc_from_pdf(toc_pdf), "pdf"

    if source in ("auto", "euclid"):
        from .scrapers.euclid import fetch_issue_toc as euclid_toc
        entries = euclid_toc(issn, full_venue, vol, iss)
        if entries:
            return entries, "euclid"
        if source == "euclid":
            return [], "euclid"
        log.info("Euclid empty/unavailable — falling back to OpenAlex")

    if source in ("auto", "openalex"):
        from .scrapers.openalex import fetch_issue_toc as openalex_toc
        return openalex_toc(issn, full_venue, vol, iss), "openalex"

    return [], source


def refetch_missing(missing: list[TocEntry], full_venue: str) -> list[Paper]:
    """Pull each missing article from Crossref by DOI. No-DOI entries can't be
    auto-refetched (reported only)."""
    papers: list[Paper] = []
    for e in missing:
        if not e.doi:
            log.warning("can't auto-refetch (no DOI): %s", e.title[:80])
            continue
        p = fetch_work(e.doi, full_venue)
        if p is None:
            log.warning("refetch failed for %s (%s)", e.doi, e.title[:60])
            continue
        if not p.abstract:
            log.warning("refetched %s but no abstract found (kept anyway)", e.doi)
        papers.append(p)
        log.info("refetched %s — %s", e.doi, p.title[:70])
    return papers


# ── driver ──────────────────────────────────────────────────────────────────────

def run(*, journal: str, issue: str, source: str = "auto",
        toc_pdf: Path | None = None, page: Path | None = None,
        snapshot: Path | None = None, refetch: bool = False,
        rerun: bool = False, dry_run: bool = False) -> list[TocEntry]:
    """Returns the list of missing entries."""
    from .journals import (_journal_catalog, _parse_issue_arg,
                           _resolve_rerun_targets)
    from .render.markdown import _slug

    catalog = _journal_catalog()
    meta = catalog.get(_slug(journal))
    if meta is None:
        log.error("unknown journal %r — see config/journals.yaml", journal)
        return []
    vol, iss = _parse_issue_arg(issue)
    full, issn = meta["full"], meta["issn"]

    # ── authoritative set (resolved automatically) ──────────────────────────
    authoritative, used = resolve_authoritative(
        issn, full, vol, iss, source=source, toc_pdf=toc_pdf)
    if not authoritative:
        log.error("authoritative TOC is empty (source=%s) — nothing to diff "
                  "against. Try --euclid / --openalex / --toc-pdf, or check "
                  "network access.", used)
        return []
    log.info("authoritative TOC: %d article(s) via %s", len(authoritative), used)

    # ── scraped set ─────────────────────────────────────────────────────────
    if snapshot:
        scraped = snapshot_entries(snapshot, full, vol, iss)
    else:
        page_path = page
        if page_path is None:
            targets = _resolve_rerun_targets(only=[journal], only_group=None,
                                             recent=None, issue=issue)
            if not targets:
                log.error("no published page for %s %s — pass --page or --snapshot",
                          journal, issue)
                return []
            page_path = targets[0].path
        scraped = page_entries(page_path)
        log.info("scraped side: %s (%d entries)", page_path.name, len(scraped))

    # ── diff + report ─────────────────────────────────────────────────────────
    missing = diff(authoritative, scraped)
    report = format_report(missing, journal=meta["short"], vol=vol, iss=iss,
                           n_auth=len(authoritative), n_scraped=len(scraped))
    print("\n" + report)

    if not missing:
        return missing

    if not refetch:
        log.info("re-run with --refetch to pull the missing articles "
                 "(add --rerun to regenerate the page)")
        return missing

    if dry_run:
        log.info("dry-run: would refetch %d DOI'd article(s)%s",
                 sum(1 for e in missing if e.doi),
                 " and rerun the issue" if rerun else "")
        return missing

    recovered = refetch_missing(missing, full)
    log.info("refetched %d/%d missing article(s)", len(recovered), len(missing))

    if rerun and recovered:
        from .journals import rerun as journal_rerun
        log.info("regenerating %s %s with %d recovered article(s) ...",
                 journal, issue, len(recovered))
        journal_rerun(only=[journal], issue=issue, extra_papers=recovered)

    return missing


def _setup_logging() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    logging.getLogger("httpx").setLevel(logging.WARNING)


def main(argv: list[str] | None = None) -> int:
    _setup_logging()
    ap = argparse.ArgumentParser(description="Check a journal issue for missing "
                                             "articles against an authoritative TOC.")
    ap.add_argument("--journal", required=True,
                    help="journal short name (e.g. AoS) — see config/journals.yaml")
    ap.add_argument("--issue", required=True, metavar="vNN-iMM",
                    help="issue spec, e.g. v54-i1 (or v54 for a whole volume)")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--euclid", action="store_true",
                     help="force authoritative source: Project Euclid issue TOC")
    src.add_argument("--openalex", action="store_true",
                     help="force authoritative source: OpenAlex issue listing")
    src.add_argument("--toc-pdf", type=Path, metavar="PATH",
                     help="authoritative source: a local content/Contents PDF "
                          "(offline fallback; default is to fetch automatically)")
    scr = ap.add_mutually_exclusive_group()
    scr.add_argument("--page", type=Path, metavar="PATH",
                     help="scraped side: a specific docs/journals/*.md page "
                          "(default: the published page for this issue)")
    scr.add_argument("--snapshot", type=Path, metavar="PATH",
                     help="scraped side: a corpus JSON snapshot instead of the page")
    ap.add_argument("--refetch", action="store_true",
                    help="pull the missing articles from Crossref by DOI")
    ap.add_argument("--rerun", action="store_true",
                    help="with --refetch: regenerate the issue page including them")
    ap.add_argument("--dry-run", action="store_true",
                    help="with --refetch: report what would be fetched, do nothing")
    args = ap.parse_args(argv)

    if args.rerun and not args.refetch:
        ap.error("--rerun requires --refetch")

    source = ("pdf" if args.toc_pdf else "euclid" if args.euclid
              else "openalex" if args.openalex else "auto")
    run(journal=args.journal, issue=args.issue, source=source, toc_pdf=args.toc_pdf,
        page=args.page, snapshot=args.snapshot,
        refetch=args.refetch, rerun=args.rerun, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
