"""Backfill deep-read reports for *past* daily runs.

The deep-read threshold was lowered over time (papers used to need a very high
score to be deep-read; now anything at ``score_threshold_deepread`` — currently
6 — qualifies). So earlier dailies contain papers that *would* be deep-read
under today's rules but never were. Every scored paper is recorded in
``data/llm_scores.jsonl`` (including its abstract), so we can replay the
deep-read step for those papers without re-scraping or re-scoring.

For each qualifying paper that isn't already in the deep-reads index:

  1. reconstruct the :class:`Paper` from the score-log row (carries the
     abstract, title, score, topic …);
  2. fill the first-pass Chinese summary if missing (deep read uses it as
     context — the score log doesn't store it, so we regenerate from the
     abstract);
  3. download the PDF (the deep read is best on full text; it falls back to
     the abstract when no PDF is available);
  4. deep-read it and update ``data/deep_reads_index.json`` + the per-paper
     page under ``docs/deep_reads/``.

The page for a backfilled paper lands under its *original* report date, exactly
where a same-day deep read would have put it. Already-deep-read papers are
skipped, so re-running is safe and cheap.

Usage::

    python -m research_news.backfill_deep_reads --date 2026-05-29
    python -m research_news.backfill_deep_reads --date 2026-05-29 --threshold 7
    python -m research_news.backfill_deep_reads --since 2026-05-27 --until 2026-06-02
    python -m research_news.backfill_deep_reads --date 2026-05-29 --dry-run
    python -m research_news.backfill_deep_reads --date 2026-05-29 --limit 5
"""
from __future__ import annotations

import argparse
import logging
import os
from datetime import date
from pathlib import Path

import yaml
from dotenv import load_dotenv

from .deep_read import generate_deep_read_report, load_index
from .highlights import save_highlights
from .models import Paper
from .render.markdown import update_index
from .rerun import _paper_from_row, load_score_index

log = logging.getLogger("research_news.backfill")

DAILY_MODEL = os.environ.get("DAILY_MODEL", "glm-5.1")


def _default_threshold() -> float:
    """Read score_threshold_deepread from config/interests.yaml (default 6)."""
    path = Path("config/interests.yaml")
    if not path.exists():
        return 6.0
    try:
        cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return float(cfg.get("score_threshold_deepread", 6))
    except Exception:  # noqa: BLE001
        return 6.0


def _interests_text() -> str:
    path = Path("config/interests.yaml")
    return path.read_text(encoding="utf-8") if path.exists() else ""


def qualifying_papers(
    run_date: str,
    threshold: float,
    *,
    sources: set[str] | None = None,
    force: bool = False,
) -> list[Paper]:
    """Papers scored on ``run_date`` at/above ``threshold``, not yet deep-read.

    Sourced from data/llm_scores.jsonl. Deduped by paper_id (a paper can have
    several rows); the highest-scoring row for that date wins.

    By default papers already in the deep-reads index for this date are excluded
    (incremental backfill). With ``force=True`` nothing is excluded and the set
    is *every* paper that is either at/above threshold OR already deep-read that
    day — i.e. regenerate the whole day's deep reads, picking up newly-qualifying
    papers too. A previously deep-read paper below the threshold (e.g. an
    institution green-light) is still re-run under force so the day isn't shrunk.
    """
    score_index = load_score_index()  # paper_id -> list[row]
    already = {pid for pid, d in
               ((e["paper_id"], e["date"]) for e in load_index()) if d == run_date}

    best_row: dict[str, dict] = {}
    for pid, rows in score_index.items():
        for row in rows:
            if row.get("run_date") != run_date:
                continue
            meets = (row.get("score") or 0) >= threshold
            if not meets and not (force and pid in already):
                continue
            if sources and (row.get("source") or "arxiv") not in sources:
                continue
            cur = best_row.get(pid)
            if cur is None or (row.get("score") or 0) > (cur.get("score") or 0):
                best_row[pid] = row

    papers: list[Paper] = []
    for pid, row in best_row.items():
        if pid in already and not force:
            continue
        papers.append(_paper_from_row(row))
    # Highest score first — the most relevant papers get deep-read even under a
    # --limit cap.
    papers.sort(key=lambda p: p.score or 0, reverse=True)
    return papers


def backfill_date(
    run_date: str,
    *,
    threshold: float,
    client,
    interests_text: str,
    model: str | None,
    limit: int | None,
    dry_run: bool,
    sources: set[str] | None,
    force: bool,
) -> int:
    """Backfill deep reads for one date. Returns the number deep-read."""
    papers = qualifying_papers(run_date, threshold, sources=sources, force=force)
    if limit is not None:
        papers = papers[:limit]

    if not papers:
        log.info("%s: nothing to backfill (no new papers >= %.0f)", run_date, threshold)
        return 0

    verb = "re-run" if force else "backfill"
    log.info("%s: %d paper(s) to %s (score >= %.0f%s):",
             run_date, len(papers), verb, threshold,
             ", incl. already-deep-read" if force else "")
    for p in papers:
        log.info("  %s  score=%.0f  topic=%s  %s",
                 p.paper_id, p.score or 0, p.topic or "?", p.title[:70])

    if dry_run:
        log.info("%s: dry run — wrote nothing", run_date)
        return 0

    from .llm.pipeline import summarize_paper  # local import avoids import cycle

    # First-pass summary (the score log doesn't store summary_zh / why_relevant,
    # and the deep read leans on them for context). Skip papers that already
    # somehow carry one.
    for p in papers:
        if not p.summary_zh and p.abstract:
            try:
                summarize_paper(client, p, interests_text, model=model)
            except Exception as e:  # noqa: BLE001 — deep read can proceed without it
                log.warning("first-pass summary failed for %s: %s", p.paper_id, e)

    # Download PDFs so the deep read uses full text (falls back to abstract).
    log.info("%s: downloading %d PDF(s) ...", run_date, len(papers))
    save_highlights(papers, run_date=date.fromisoformat(run_date))

    log.info("%s: generating %d deep read(s) ...", run_date, len(papers))
    generate_deep_read_report(
        papers, client, interests_text, date.fromisoformat(run_date),
        "daily", model=model,
    )
    return len(papers)


def _dates_in_range(since: str, until: str) -> list[str]:
    """Every run_date in the score log between since and until (inclusive)."""
    index = load_score_index()
    dates = {row.get("run_date") for rows in index.values() for row in rows}
    return sorted(d for d in dates if d and since <= d <= until)


def run(
    *,
    date_str: str | None = None,
    since: str | None = None,
    until: str | None = None,
    threshold: float | None = None,
    model: str | None = None,
    limit: int | None = None,
    dry_run: bool = False,
    sources: set[str] | None = None,
    force: bool = False,
) -> int:
    """Backfill deep reads for one date or a date range. Returns total deep-read."""
    load_dotenv()
    threshold = threshold if threshold is not None else _default_threshold()
    interests_text = _interests_text()

    if date_str:
        target_dates = [date_str]
    elif since and until:
        target_dates = _dates_in_range(since, until)
        if not target_dates:
            log.error("no scored dates between %s and %s", since, until)
            return 0
        log.info("backfilling %d date(s): %s", len(target_dates), ", ".join(target_dates))
    else:
        log.error("specify --date, or both --since and --until")
        return 0

    client = None
    if not dry_run:
        from .llm.sjtu_client import SJTUClient
        client = SJTUClient()

    total = 0
    for d in target_dates:
        total += backfill_date(
            d,
            threshold=threshold,
            client=client,
            interests_text=interests_text,
            model=model or DAILY_MODEL,
            limit=limit,
            dry_run=dry_run,
            sources=sources,
            force=force,
        )

    if total and not dry_run:
        update_index()  # refresh homepage + archive pages with the new deep reads
        log.info("backfill done: %d new deep read(s); index refreshed", total)
    return total


def _setup_logging(log_dir: str = "logs") -> None:
    """Log to console *and* logs/<today>.log, mirroring the daily pipeline, so
    backfill runs (incl. the real reference-fetch HTTP status codes) are
    persisted for diagnosis rather than lost to the console."""
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    Path(log_dir).mkdir(exist_ok=True)
    log_file = Path(log_dir) / f"{date.today().isoformat()}.log"

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt, datefmt=datefmt)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    root.addHandler(ch)
    fh = logging.FileHandler(log_file, encoding="utf-8")  # append
    fh.setFormatter(formatter)
    root.addHandler(fh)
    # httpx request lines stay in the file but off the console.
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
        description="Backfill deep-read reports for past dailies under today's "
                    "(lower) score threshold, using data/llm_scores.jsonl."
    )
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", metavar="YYYY-MM-DD", help="backfill a single run date")
    g.add_argument("--since", metavar="YYYY-MM-DD",
                   help="start of a date range (requires --until)")
    ap.add_argument("--until", metavar="YYYY-MM-DD", help="end of a date range")
    ap.add_argument("--threshold", type=float,
                    help="score cutoff (default: score_threshold_deepread from "
                         "config/interests.yaml)")
    ap.add_argument("--model", help="override the deep-read model "
                                    f"(default: {DAILY_MODEL})")
    ap.add_argument("--limit", type=int,
                    help="cap papers per date (highest score first) — useful for "
                         "a trial run before committing tokens")
    ap.add_argument("--source", action="append", dest="sources",
                    help="only papers from this source (e.g. arxiv); repeatable")
    ap.add_argument("--force", action="store_true",
                    help="re-run the WHOLE day: don't skip already-deep-read papers, "
                         "and re-generate them too (use when the deep-read recipe "
                         "changed and you want the day refreshed end-to-end)")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be backfilled without calling the LLM "
                         "or downloading anything")
    args = ap.parse_args()

    if args.since and not args.until:
        ap.error("--since requires --until")

    run(
        date_str=args.date,
        since=args.since,
        until=args.until,
        threshold=args.threshold,
        model=args.model,
        limit=args.limit,
        dry_run=args.dry_run,
        sources=set(args.sources) if args.sources else None,
        force=args.force,
    )


if __name__ == "__main__":
    main()
