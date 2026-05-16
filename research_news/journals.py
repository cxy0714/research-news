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
from .render.markdown import render_journals_by_group, update_index
from .scrapers.crossref import fetch_latest_issue
from .scrapers.jmlr import fetch_latest as jmlr_fetch_latest
from .usage import report as report_token_usage

log = logging.getLogger("research_news.journals")

JOURNALS_MODEL = os.environ.get("JOURNALS_MODEL",
                                os.environ.get("DAILY_MODEL", "glm-5.1"))

JOURNALS_CONFIG_PATH = Path("config/journals.yaml")


def _load_groups() -> dict:
    """Returns {group_key: {label, journals: [{short, full, issn}]}}."""
    import yaml as _yaml
    cfg = _yaml.safe_load(JOURNALS_CONFIG_PATH.read_text(encoding="utf-8"))
    return cfg.get("groups", {})


def _fetch_journal(jcfg: dict, *, jmlr_n: int | None = None,
                   jmlr_vol: int | None = None,
                   n_issues: int = 1) -> list[Paper]:
    issn = jcfg["issn"]
    full = jcfg["full"]
    short = jcfg.get("short", full)
    if issn == "jmlr":
        return jmlr_fetch_latest(n=jmlr_n, volume=jmlr_vol)
    try:
        return fetch_latest_issue(issn, full, n_issues=n_issues)
    except Exception as e:
        log.warning("fetch failed for %s (ISSN %s): %s", short, issn, e)
        return []


def _save_papers(papers: list[Paper], path: Path) -> None:
    """Atomic write: serialize to <path>.tmp, then os.replace into place. So a
    crash mid-write can't corrupt the file."""
    import json, os
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps([p.to_dict() for p in papers], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    os.replace(tmp, path)
    log.info("saved %d papers to %s", len(papers), path)


def _load_papers(path: Path) -> list[Paper]:
    import json
    raw = json.loads(path.read_text(encoding="utf-8"))
    papers = [Paper(**d) for d in raw]
    log.info("loaded %d papers from %s", len(papers), path)
    return papers


def _summary_is_broken(p: Paper) -> bool:
    """Heuristics for a paper whose LLM summary needs a retry.

    Catches both LLM call failures (no summary at all) and parse failures
    (raw JSON spill-over where summary_zh starts with '{')."""
    s = (p.summary_zh or "").strip()
    if not s:
        return True
    if s.startswith("{") or s.startswith("```"):
        return True
    if len(s) < 80:
        return True
    # A successful rich-prompt run always fills these; their absence is a
    # strong signal that summarize_paper bailed out.
    if not p.topic or not p.key_techniques or not p.why_relevant:
        return True
    return False


def run(only: list[str] | None = None, dry_run: bool = False,
        jmlr_n: int | None = None, jmlr_vol: int | None = None,
        n_issues: int = 1, label: str | None = None,
        skip_pdf: bool = False,
        save_papers: Path | None = None,
        load_papers: Path | None = None,
        retry_broken: bool = False,
        only_group: list[str] | None = None) -> list[Path] | None:
    load_dotenv()
    interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")
    groups = _load_groups()

    if load_papers:
        log.info("skipping fetch; loading papers from %s", load_papers)
        papers = _load_papers(load_papers)
    else:
        if only_group:
            groups_to_run = {k: groups[k] for k in only_group if k in groups}
            unknown = [k for k in only_group if k not in groups]
            if unknown:
                log.warning("unknown groups (skipped): %s — available: %s",
                            unknown, list(groups.keys()))
        else:
            groups_to_run = groups

        only_shorts = set(s.strip() for s in (only or []) if s.strip())
        log.info("journals run: groups=%s, only=%s",
                 list(groups_to_run.keys()),
                 sorted(only_shorts) if only_shorts else "all")

        papers = []
        for gkey, gcfg in groups_to_run.items():
            for jcfg in gcfg["journals"]:
                if only_shorts and jcfg["short"] not in only_shorts:
                    continue
                ps = _fetch_journal(jcfg, jmlr_n=jmlr_n,
                                    jmlr_vol=jmlr_vol, n_issues=n_issues)
                log.info("  [%s] %s → %d papers", gkey, jcfg["short"], len(ps))
                papers.extend(ps)
                # Incremental save: ^C / crash leaves earlier journals on disk.
                if save_papers:
                    _save_papers([p for p in papers if p.abstract], save_papers)

        # Drop any without an abstract — can't score them meaningfully.
        n_before = len(papers)
        papers = [p for p in papers if p.abstract]
        if len(papers) < n_before:
            log.info("dropped %d papers with no abstract (Crossref + S2 both empty)",
                     n_before - len(papers))

        if save_papers:
            _save_papers(papers, save_papers)

    if not papers:
        log.error("no papers — bailing")
        return None

    if dry_run:
        log.info("dry-run: %d papers across %d venues",
                 len(papers),
                 len({p.venue for p in papers}))
        for p in papers[:10]:
            log.info("  [%s] %s — abstract chars=%d", p.venue, p.title[:80], len(p.abstract))
        return None

    client = SJTUClient()

    # Skip scoring on --retry-broken with loaded papers: existing scores
    # are still valid (rich-prompt summary failure doesn't invalidate the
    # cheaper batch score).
    if retry_broken and load_papers and all(p.score is not None for p in papers):
        log.info("retry-broken: keeping cached scores from %s", load_papers)
    else:
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

    # If we loaded saved papers with --retry-broken, skip already-good
    # summaries and only re-call LLM on the ones that broke last time.
    if retry_broken and load_papers:
        to_summarize = [p for p in papers if _summary_is_broken(p)]
        log.info("retry-broken: %d/%d papers need re-summarize (model=%s)",
                 len(to_summarize), len(papers), JOURNALS_MODEL)
    else:
        to_summarize = papers
        log.info("summarizing %d papers (model=%s) ...",
                 len(to_summarize), JOURNALS_MODEL)

    for p in to_summarize:
        try:
            summarize_paper(client, p, interests_text, model=JOURNALS_MODEL)
        except Exception as e:
            log.warning("summary failed for %s: %s", p.paper_id, e)

    # Persist the LLM enrichment back to the source JSON so a future
    # --load-papers picks up the fixed summaries.
    if load_papers:
        _save_papers(papers, load_papers)

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
    out_paths = render_journals_by_group(papers, groups, when=today, label=label)
    update_index()

    if high and not skip_pdf:
        log.info("saving %d journal highlights (PDF + manifest)", len(high))
        save_highlights(high, run_date=today)
    elif skip_pdf:
        log.info("skip_pdf set; not downloading journal highlight PDFs")

    for p in out_paths:
        log.info("wrote %s", p)
    report_token_usage(client, "journals", today)
    return out_paths


def _setup_logging() -> None:
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=fmt, datefmt="%Y-%m-%d %H:%M:%S")
    logging.getLogger("httpx").setLevel(logging.WARNING)


def main(argv: list[str] | None = None) -> int:
    _setup_logging()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", default=None,
                    help="Comma-separated subset of journal short names to fetch "
                         "(e.g. JMLR,AoS). See config/journals.yaml for the list.")
    ap.add_argument("--only-group", default=None,
                    help="Comma-separated subset of group keys to fetch "
                         "(e.g. core,applied). Skips all journals outside these "
                         "groups. See config/journals.yaml for the group list.")
    ap.add_argument("--jmlr-n", type=int, default=None,
                    help="Cap how many recent JMLR papers to pull. "
                         "Default: no cap (take entire current volume, ~50).")
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
    ap.add_argument("--save-papers", type=Path, default=None, metavar="PATH",
                    help="After fetching (before LLM), dump papers to PATH as JSON. "
                         "Combine with --dry-run for a pure 'fetch only' step.")
    ap.add_argument("--load-papers", type=Path, default=None, metavar="PATH",
                    help="Skip fetching and load papers from PATH. Lets you "
                         "iterate on prompts / models without re-scraping.")
    ap.add_argument("--retry-broken", action="store_true",
                    help="With --load-papers: only re-summarize papers whose "
                         "previous LLM output was broken (empty / truncated JSON / "
                         "missing topic+key_techniques). Keeps existing scores. "
                         "Saves the fixed summaries back to the JSON.")
    args = ap.parse_args(argv)

    if args.load_papers and args.save_papers:
        ap.error("--load-papers and --save-papers are mutually exclusive")
    if args.retry_broken and not args.load_papers:
        ap.error("--retry-broken requires --load-papers")

    only = [s.strip() for s in args.only.split(",")] if args.only else None
    only_group = [s.strip() for s in args.only_group.split(",")] \
        if args.only_group else None
    run(only=only, only_group=only_group,
        dry_run=args.dry_run, jmlr_n=args.jmlr_n,
        jmlr_vol=args.jmlr_vol, n_issues=args.n_issues, label=args.label,
        skip_pdf=args.skip_pdf,
        save_papers=args.save_papers, load_papers=args.load_papers,
        retry_broken=args.retry_broken)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
