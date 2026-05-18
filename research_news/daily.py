"""Main entry point: run the daily pipeline."""
from __future__ import annotations

import argparse
import logging
from datetime import date, timedelta
from pathlib import Path

import yaml
from dotenv import load_dotenv

from .dedup import filter_new, load_seen, mark_seen, save_seen
from .deep_read import generate_deep_read_report
from .highlights import save_highlights
from .llm.pipeline import extract_events, score_papers, summarize_paper
from .llm.prompts import SECONDARY_TOPICS
from .llm.sjtu_client import SJTUClient
from .models import Event, Paper
from .render.markdown import render_daily, update_index
from .scrapers import arxiv as arxiv_scraper
from .scrapers import authors as authors_scraper
from .scrapers import conferences as conf_scraper
from .usage import report as report_token_usage

log = logging.getLogger("research_news")

# Model used by the daily pipeline (overridable via env). GLM-5.1 won the
# in-house shootout vs DeepSeek V3.2 — see docs/shootout/.
import os
DAILY_MODEL = os.environ.get("DAILY_MODEL", "glm-5.1")


def _load_config() -> tuple[dict, str]:
    sources = yaml.safe_load(Path("config/sources.yaml").read_text(encoding="utf-8"))
    interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")
    return sources, interests_text


def _collect_papers(sources_cfg: dict, for_date: date | None = None) -> list[Paper]:
    papers: list[Paper] = []
    if sources_cfg.get("arxiv", {}).get("enabled"):
        papers.extend(arxiv_scraper.fetch_all(sources_cfg["arxiv"], for_date=for_date))
    if sources_cfg.get("authors", {}).get("enabled"):
        authors_cfg = yaml.safe_load(Path("config/authors.yaml").read_text(encoding="utf-8"))
        papers.extend(
            authors_scraper.fetch_all(
                authors_cfg, lookback_days=sources_cfg["authors"].get("lookback_days", 14)
            )
        )
    return papers


def _collect_events(client: SJTUClient, sources_cfg: dict) -> list[Event]:
    if not sources_cfg.get("conferences", {}).get("enabled"):
        return []
    pages = conf_scraper.fetch_all(sources_cfg["conferences"])
    events: list[Event] = []
    for p in pages:
        events.extend(extract_events(client, p["name"], p["text"]))
    return events


def _parse_thresholds(interests_text: str) -> tuple[float, float]:
    cfg = yaml.safe_load(interests_text)
    return (
        float(cfg.get("score_threshold_show", 4)),
        float(cfg.get("score_threshold_highlight", 8)),
    )


def run(dry_run: bool = False, for_date: date | None = None) -> Path:
    load_dotenv()
    sources_cfg, interests_text = _load_config()
    th_show, th_highlight = _parse_thresholds(interests_text)

    report_date = for_date or date.today()
    log.info("collecting papers for %s ...", report_date)
    papers = _collect_papers(sources_cfg, for_date=for_date)
    log.info("collected %d papers before dedup", len(papers))

    seen = load_seen()
    papers = filter_new(papers, seen)
    log.info("%d papers after dedup", len(papers))

    if dry_run:
        log.info("dry run: skipping LLM")
        return Path("/dev/null")

    client = SJTUClient()

    if papers:
        log.info("scoring papers (model=%s) ...", DAILY_MODEL)
        scores = score_papers(client, papers, interests_text, model=DAILY_MODEL)

        for p in papers[:3]:
            log.info("ID sample: %r  matched=%s", p.paper_id, p.paper_id in scores)

        for p in papers:
            sr = scores.get(p.paper_id)
            if sr:
                p.score, p.score_reason = sr
            else:
                p.score = 0.0

        papers = [p for p in papers if (p.score or 0) >= th_show]
        papers.sort(key=lambda p: p.score or 0, reverse=True)
        log.info("%d papers above threshold %.0f", len(papers), th_show)

        # Cap to keep the daily digest readable.
        papers = papers[:25]

        log.info("summarizing %d papers (model=%s) ...", len(papers), DAILY_MODEL)
        for p in papers:
            try:
                summarize_paper(client, p, interests_text, model=DAILY_MODEL)
            except Exception as e:
                log.warning("summary failed for %s: %s", p.paper_id, e)

    log.info("collecting events ...")
    events = _collect_events(client, sources_cfg)

    high = [p for p in papers if (p.score or 0) >= th_highlight]
    mid = [p for p in papers if (p.score or 0) < th_highlight]

    out_path = render_daily(high, mid, events, when=report_date)

    # Deep-read candidates: primary-interest papers above th_highlight (8),
    # plus two secondary buckets from below the threshold:
    #   - secondary-interest topics (astrostats/econ_theory/epidemiology) at score >= 6
    #   - real-data application papers at score >= 7 (their analysis pipelines
    #     and datasets are themselves worth a deep read)
    deep_read_papers = list(high) + [
        p for p in mid
        if ((p.topic or "other") in SECONDARY_TOPICS and (p.score or 0) >= 6)
        or (p.novelty_flag == "application" and (p.score or 0) >= 7)
    ]

    # Persist high-relevance papers: download PDFs, deep-read, then update index.
    # update_index() is called last so the homepage includes today's deep reads.
    if deep_read_papers:
        log.info("saving %d highlights (PDF + manifest)", len(deep_read_papers))
        save_highlights(deep_read_papers, run_date=report_date)
        log.info("generating deep-read report for %d papers ...", len(deep_read_papers))
        generate_deep_read_report(
            deep_read_papers, client, interests_text, report_date, "daily", model=DAILY_MODEL
        )

    update_index()
    mark_seen(papers, seen)
    save_seen(seen)

    report_token_usage(client, "daily", report_date)
    log.info("wrote %s", out_path)
    return out_path


def _setup_logging(log_dir: str = "logs") -> None:
    from datetime import date
    from pathlib import Path

    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    Path(log_dir).mkdir(exist_ok=True)
    log_file = Path(log_dir) / f"{date.today().isoformat()}.log"

    root = logging.getLogger()
    root.setLevel(logging.INFO)

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(ch)

    # File handler — append so reruns on the same day accumulate
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(fh)

    # httpx HTTP request lines are noisy on console; keep them in file only
    console_httpx = logging.getLogger("httpx")
    console_httpx.setLevel(logging.WARNING)
    # But also add a file-only handler at INFO to capture them in the log file
    fh_httpx = logging.FileHandler(log_file, encoding="utf-8")
    fh_httpx.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    fh_httpx.setLevel(logging.INFO)
    console_httpx.addHandler(fh_httpx)
    console_httpx.propagate = False


def main() -> None:
    _setup_logging()
    ap = argparse.ArgumentParser(description="Fetch and summarise daily research papers.")
    ap.add_argument("--dry-run", action="store_true", help="Fetch only; skip LLM and rendering")
    ap.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        help="Fetch papers for this date instead of today (uses arXiv API)",
    )
    ap.add_argument(
        "--lookback-days",
        type=int,
        default=0,
        metavar="N",
        help="Fetch papers from N days ago (e.g. 3 on Monday to get Friday's papers)",
    )
    args = ap.parse_args()

    for_date: date | None = None
    if args.date:
        for_date = date.fromisoformat(args.date)
    elif args.lookback_days > 0:
        for_date = date.today() - timedelta(days=args.lookback_days)

    run(dry_run=args.dry_run, for_date=for_date)


if __name__ == "__main__":
    main()
