"""Quarterly journal pull: fetch the latest issue of each configured journal,
score + summarize all papers (no dropout threshold — these are pre-curated),
download high-relevance PDFs, render a Markdown page.

Sources:
  - JMLR: HTML scrape of the volume index page (rolling publication; we
    take the N most recent papers).
  - AoS / JASA / JRSSB / Biometrika: Crossref API for issue TOC + Semantic
    Scholar for abstract backfill when Crossref doesn't expose it.

Usage:
    python -m research_news.journals                       # all journals
    python -m research_news.journals --only AoS,JRSSB      # subset
    python -m research_news.journals --jmlr-n 15
    python -m research_news.journals --dry-run             # no LLM
"""
from __future__ import annotations

import argparse
import logging
import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

from .highlights import save_highlights
from .llm.pipeline import score_papers, summarize_paper
from .llm.sjtu_client import SJTUClient
from .models import Paper
from .render.markdown import render_journals, update_index
from .scrapers.crossref import KNOWN_JOURNALS, fetch_latest_issue
from .scrapers.jmlr import fetch_latest as jmlr_fetch_latest

log = logging.getLogger("research_news.journals")

JOURNALS_MODEL = os.environ.get("JOURNALS_MODEL",
                                os.environ.get("DAILY_MODEL", "glm-5.1"))

# Journals enabled by default. "JMLR" is special (own scraper); the rest go
# through Crossref via KNOWN_JOURNALS.
DEFAULT_JOURNALS = ["JMLR", "AoS", "JASA", "JRSSB", "Biometrika"]

CROSSREF_BY_SHORT = {short: (name, issn)
                     for name, (issn, short) in KNOWN_JOURNALS.items()}


def _fetch_journal(short: str, *, jmlr_n: int = 10,
                   jmlr_vol: int | None = None,
                   n_issues: int = 1) -> list[Paper]:
    if short == "JMLR":
        return jmlr_fetch_latest(n=jmlr_n, volume=jmlr_vol)
    if short in CROSSREF_BY_SHORT:
        full_name, issn = CROSSREF_BY_SHORT[short]
        return fetch_latest_issue(issn, full_name, n_issues=n_issues)
    log.warning("unknown journal short name: %r — skipping", short)
    return []


def run(only: list[str] | None = None, dry_run: bool = False,
        jmlr_n: int = 10, jmlr_vol: int | None = None,
        n_issues: int = 1, label: str | None = None,
        skip_pdf: bool = False) -> Path | None:
    load_dotenv()
    interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")

    targets = only or DEFAULT_JOURNALS
    log.info("journals run: %s", targets)

    papers: list[Paper] = []
    for short in targets:
        try:
            ps = _fetch_journal(short, jmlr_n=jmlr_n, jmlr_vol=jmlr_vol,
                                n_issues=n_issues)
        except Exception as e:
            log.error("fetch failed for %s: %s", short, e)
            continue
        log.info("  %s → %d papers", short, len(ps))
        papers.extend(ps)

    # Drop any without an abstract — can't score them meaningfully.
    n_before = len(papers)
    papers = [p for p in papers if p.abstract]
    if len(papers) < n_before:
        log.info("dropped %d papers with no abstract (Crossref + S2 both empty)",
                 n_before - len(papers))

    if not papers:
        log.error("no papers fetched — bailing")
        return None

    if dry_run:
        log.info("dry-run: %d papers across %d venues",
                 len(papers),
                 len({p.venue for p in papers}))
        for p in papers[:10]:
            log.info("  [%s] %s — abstract chars=%d", p.venue, p.title[:80], len(p.abstract))
        return None

    client = SJTUClient()

    log.info("scoring %d papers (model=%s) ...", len(papers), JOURNALS_MODEL)
    scores = score_papers(client, papers, interests_text, model=JOURNALS_MODEL)
    for p in papers:
        sr = scores.get(p.paper_id)
        if sr:
            p.score, p.score_reason = sr
        else:
            p.score = 0.0

    # No drop threshold: journals are pre-curated, the researcher wants to see
    # the whole issue. Sort by score so the most relevant float to the top
    # within each venue's section in the rendered output.
    papers.sort(key=lambda p: p.score or 0, reverse=True)

    log.info("summarizing %d papers (model=%s) ...", len(papers), JOURNALS_MODEL)
    for p in papers:
        try:
            summarize_paper(client, p, interests_text, model=JOURNALS_MODEL)
        except Exception as e:
            log.warning("summary failed for %s: %s", p.paper_id, e)

    # Highlight = score >= threshold from interests.yaml
    import yaml as _yaml
    th_highlight = float(
        _yaml.safe_load(interests_text).get("score_threshold_highlight", 8)
    )
    high = [p for p in papers if (p.score or 0) >= th_highlight]

    # Stamp the file with the year + quarter for easy quarterly recognition,
    # unless an explicit label is given (e.g. for multi-issue backfills).
    today = date.today()
    if label is None:
        quarter = (today.month - 1) // 3 + 1
        label = f"{today.year}Q{quarter}"
        if n_issues > 1:
            label = f"{label}-{n_issues}issues"
    out_path = render_journals(papers, when=today, label=label)
    update_index()

    if high and not skip_pdf:
        log.info("saving %d journal highlights (PDF + manifest)", len(high))
        save_highlights(high, run_date=today)
    elif skip_pdf:
        log.info("skip_pdf set; not downloading journal highlight PDFs")

    log.info("wrote %s  (total LLM calls: %d)", out_path, client.calls)
    log.info("token usage: %s", client.usage)
    return out_path


def _setup_logging() -> None:
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=fmt, datefmt="%Y-%m-%d %H:%M:%S")
    logging.getLogger("httpx").setLevel(logging.WARNING)


def main(argv: list[str] | None = None) -> int:
    _setup_logging()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", default=None,
                    help="Comma-separated subset of journals to fetch. "
                         f"Available: {','.join(DEFAULT_JOURNALS)}")
    ap.add_argument("--jmlr-n", type=int, default=10,
                    help="How many recent JMLR papers to pull (default 10).")
    ap.add_argument("--jmlr-vol", type=int, default=None,
                    help="Override JMLR volume (default: current year - 1999).")
    ap.add_argument("--n-issues", type=int, default=1,
                    help="How many recent issues to pull from each quarterly "
                         "journal (AoS/JASA/JRSSB/Biometrika). "
                         "Default 1 (latest only). Use 4 for a full year, 8 for two.")
    ap.add_argument("--label", default=None,
                    help="Override the output filename suffix "
                         "(default: '<year>Q<n>' or '<year>Q<n>-Nissues').")
    ap.add_argument("--skip-pdf", action="store_true",
                    help="Don't download PDFs for high-relevance papers.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Fetch metadata + abstracts only; skip LLM and rendering.")
    args = ap.parse_args(argv)

    only = [s.strip() for s in args.only.split(",")] if args.only else None
    run(only=only, dry_run=args.dry_run, jmlr_n=args.jmlr_n,
        jmlr_vol=args.jmlr_vol, n_issues=args.n_issues, label=args.label,
        skip_pdf=args.skip_pdf)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
