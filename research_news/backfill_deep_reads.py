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
import json
import logging
import os
import re
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import yaml
from dotenv import load_dotenv

from .deep_read import (
    DEEP_READ_FAILED_MARKER,
    DEEP_READS_DIR,
    generate_deep_read_report,
    load_index,
)
from .highlights import save_highlights
from .models import Paper
from .render.markdown import update_index
from .rerun import _paper_from_row, _pick_row, load_score_index

log = logging.getLogger("research_news.backfill")

DAILY_MODEL = os.environ.get("DAILY_MODEL", "deepseek-chat")


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


def _deep_read_papers(
    papers: list[Paper],
    run_date: str,
    *,
    client,
    interests_text: str,
    model: str | None,
    dry_run: bool,
    verb: str,
) -> int:
    """Shared tail: first-pass summary → download PDFs → deep read + index.
    Returns the number deep-read (0 on empty / dry-run)."""
    if not papers:
        log.info("%s: nothing to %s", run_date, verb)
        return 0

    log.info("%s: %d paper(s) to %s:", run_date, len(papers), verb)
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

    verb = (f"re-run (score >= {threshold:.0f}, incl. already-deep-read)"
            if force else f"backfill (score >= {threshold:.0f})")
    return _deep_read_papers(
        papers, run_date, client=client, interests_text=interests_text,
        model=model, dry_run=dry_run, verb=verb,
    )


# ── failed-deep-read (stub) recovery ──────────────────────────────────────────

def find_stub_entries(dates: set[str] | None = None) -> list[dict]:
    """Deep-reads index entries whose page is a failure stub (the LLM call failed
    and left ``DEEP_READ_FAILED_MARKER``). Matched by filename so both arxiv ids
    and slugified DOIs resolve to their real paper_id. Restricted to ``dates``
    (run dates) when given."""
    index_by_name = {
        Path(e["doc_path"]).name: e for e in load_index() if e.get("doc_path")
    }
    out: list[dict] = []
    if not DEEP_READS_DIR.exists():
        return out
    for f in sorted(DEEP_READS_DIR.glob("*.md")):
        try:
            if DEEP_READ_FAILED_MARKER not in f.read_text(encoding="utf-8"):
                continue
        except OSError:
            continue
        entry = index_by_name.get(f.name)
        if entry is None:
            # Stub page with no index entry (e.g. an older / partial run). Recover
            # date + id from the filename: for arxiv ids the slug == paper_id
            # (DOIs are lossy, but those are virtually always indexed).
            m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", f.stem)
            if not m:
                log.warning("stub %s: can't parse date/id from name — skipping", f.name)
                continue
            entry = {"paper_id": m.group(2), "date": m.group(1),
                     "doc_path": f"deep_reads/{f.name}",
                     "topic": None, "score": None, "title": None}
        if dates and entry.get("date") not in dates:
            continue
        out.append(entry)
    return out


def stub_papers(
    entries: list[dict], score_index: dict[str, list[dict]], run_date: str
) -> list[Paper]:
    """Rebuild Paper objects for stub ``entries`` from the score log (abstract /
    authors), patched with the index metadata (topic / score / title) so the
    regenerated page keeps its header."""
    papers: list[Paper] = []
    # Manually queued papers are not scored into llm_scores.jsonl, so their
    # failed pages cannot be reconstructed from the score log.  The highlights
    # manifest is the durable source for those papers (it also points at the
    # downloaded PDF); use it as a fallback, and enrich arXiv entries with the
    # abstract when available.
    highlights: dict[str, dict] = {}
    manifest = Path("data/highlights.json")
    if manifest.exists():
        try:
            rows = json.loads(manifest.read_text(encoding="utf-8"))
            highlights = {r.get("paper_id"): r for r in rows
                          if isinstance(r, dict) and r.get("paper_id")}
        except (OSError, json.JSONDecodeError):
            pass
    for e in entries:
        rows = score_index.get(e["paper_id"])
        if rows:
            p = _paper_from_row(_pick_row(rows, run_date))
        else:
            h = highlights.get(e["paper_id"])
            if not h:
                log.warning("stub %s (%s): not in score/highlights log — skipping",
                            e["paper_id"], run_date)
                continue
            p = Paper(
                source=h.get("source") or "arxiv",
                paper_id=e["paper_id"],
                title=h.get("title") or e.get("title") or "",
                authors=list(h.get("authors") or []),
                abstract="",
                url=h.get("url") or "",
                categories=list(h.get("categories") or []),
                published=h.get("published"),
            )
            p.summary_zh = h.get("summary_zh")
            p.why_relevant = h.get("why_relevant")
            p.key_techniques = list(h.get("key_techniques") or [])
            p.novelty_flag = h.get("novelty_flag")
            p.pdf_path = h.get("pdf_path")
        p.topic = p.topic or e.get("topic")
        if e.get("score") is not None:
            p.score = float(e["score"])
        if not p.title:
            p.title = e.get("title") or ""
        papers.append(p)
    return papers


def retry_stubs(
    *,
    dates: set[str] | None,
    client,
    interests_text: str,
    model: str | None,
    dry_run: bool,
) -> int:
    """Regenerate every failed (stub) deep-read page, optionally limited to
    ``dates``. Returns the number regenerated."""
    entries = find_stub_entries(dates=dates)
    if not entries:
        log.info("no stub deep reads found%s", " in scope" if dates else "")
        return 0

    by_date: dict[str, list[dict]] = {}
    for e in entries:
        by_date.setdefault(e["date"], []).append(e)
    log.info("found %d stub deep read(s) across %d date(s): %s",
             len(entries), len(by_date), ", ".join(sorted(by_date)))

    score_index = load_score_index()
    total = 0
    for d in sorted(by_date):
        papers = stub_papers(by_date[d], score_index, d)
        total += _deep_read_papers(
            papers, d, client=client, interests_text=interests_text,
            model=model, dry_run=dry_run, verb="retry failed deep-read",
        )
    return total


def _dates_in_range(since: str, until: str) -> list[str]:
    """Every run_date in the score log between since and until (inclusive)."""
    index = load_score_index()
    dates = {row.get("run_date") for rows in index.values() for row in rows}
    return sorted(d for d in dates if d and since <= d <= until)


# ── resident loop: one unit of pending work ───────────────────────────────────
#
# `--pending` is what run_deepread_loop.ps1 calls in a loop. One invocation does
# ONE unit (default: one paper) and exits, so the loop can release the daily lock
# and commit between units. Exit code 0 = did work, 7 = nothing pending (stop).

# How long a failed page must sit untouched before the loop retries it: a failed
# retry rewrites the stub (refreshing its mtime), so one bad paper can't spin the
# loop forever — it gets picked up again on a later pass.
STUB_COOLDOWN_MINUTES = int(os.environ.get("DEEPREAD_STUB_COOLDOWN_MIN", "120"))


def _manifest_rows() -> list[dict]:
    """Rows of data/highlights.json — the durable "selected for deep read" queue.

    save_highlights() is called by daily for every paper it selects, *before* the
    slow LLM step, so a manifest row without a deep-read page is a deep read that
    was selected but never finished (shutdown, crash, timeout). That is the true
    backlog — it also covers green-lit / popsci papers below the score gate.
    """
    path = Path("data/highlights.json")
    if not path.exists():
        return []
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return [r for r in rows if isinstance(r, dict) and r.get("paper_id")]


def _paper_from_highlight(row: dict) -> Paper:
    """Rebuild a Paper from a highlights-manifest row (no score-log row needed)."""
    p = Paper(
        source=row.get("source") or "arxiv",
        paper_id=row["paper_id"],
        title=row.get("title") or "",
        authors=list(row.get("authors") or []),
        abstract="",
        url=row.get("url") or "",
        categories=list(row.get("categories") or []),
        published=row.get("published"),
        venue=row.get("venue"),
    )
    p.summary_zh = row.get("summary_zh")
    p.why_relevant = row.get("why_relevant")
    p.key_techniques = list(row.get("key_techniques") or [])
    p.novelty_flag = row.get("novelty_flag")
    p.pdf_path = row.get("pdf_path")
    p.topic = row.get("topic")
    if row.get("score") is not None:
        p.score = float(row["score"])
    return p


def _window_dates(window_days: int) -> list[str]:
    """Scored run dates within the window (0 = all history), ascending."""
    dates = sorted({row.get("run_date")
                    for rows in load_score_index().values() for row in rows
                    if row.get("run_date")})
    if window_days and window_days > 0:
        cutoff = (date.today() - timedelta(days=window_days)).isoformat()
        dates = [d for d in dates if d >= cutoff]
    return dates


def manifest_pending(window_days: int = 0) -> list[tuple[str, dict]]:
    """(run_date, manifest row) for highlights never deep-read, oldest first."""
    indexed = {e.get("paper_id") for e in load_index()}
    cutoff = ((date.today() - timedelta(days=window_days)).isoformat()
              if window_days and window_days > 0 else None)
    out: list[tuple[str, dict]] = []
    for row in _manifest_rows():
        if row["paper_id"] in indexed:
            continue
        d = (row.get("first_seen") or "")[:10]
        if not d:
            continue
        if cutoff and d < cutoff:
            continue
        out.append((d, row))
    # Oldest date first; within a date, highest score first.
    out.sort(key=lambda dr: (dr[0], -(dr[1].get("score") or 0)))
    return out


def _stub_attempted_recently(entry: dict) -> bool:
    page = DEEP_READS_DIR / Path(entry.get("doc_path") or "").name
    try:
        return (page.exists()
                and (time.time() - page.stat().st_mtime) < STUB_COOLDOWN_MINUTES * 60)
    except OSError:
        return False


def pending_unit(
    *,
    limit: int = 1,
    threshold: float | None = None,
    window_days: int = 0,
    sources: set[str] | None = None,
) -> tuple[str, list[Paper]] | None:
    """One unit of pending deep-read work — (run_date, papers) — or None.

    Priority: (1) highlights manifest rows never deep-read (the real backlog,
    incl. green-lit / popsci selections), (2) failed stubs past their cooldown,
    (3) score-threshold backfill (catches papers scored >= threshold that never
    entered the manifest).
    """
    threshold = threshold if threshold is not None else _default_threshold()

    backlog = manifest_pending(window_days)
    if backlog:
        d = backlog[0][0]
        return d, [_paper_from_highlight(r)
                   for dd, r in backlog if dd == d][:limit]

    stub_entries = [e for e in find_stub_entries() if not _stub_attempted_recently(e)]
    if stub_entries:
        stub_entries.sort(key=lambda e: e.get("date") or "")
        d = stub_entries[0]["date"]
        papers = stub_papers([e for e in stub_entries if e["date"] == d],
                             load_score_index(), d)
        if papers:
            return d, papers[:limit]

    for d in _window_dates(window_days):
        papers = qualifying_papers(d, threshold, sources=sources)
        if papers:
            return d, papers[:limit]
    return None


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
    retry_stubs_mode: bool = False,
    pending_mode: bool = False,
    window_days: int = 0,
) -> int:
    """Backfill deep reads for one date, a date range, stubs, or one pending unit.

    Returns the number of papers deep-read (0 = nothing was pending)."""
    load_dotenv()
    threshold = threshold if threshold is not None else _default_threshold()
    interests_text = _interests_text()

    # Resident-loop mode: exactly one unit of work, then return.
    if pending_mode:
        unit = pending_unit(limit=limit or 1, threshold=threshold,
                            window_days=window_days, sources=sources)
        if unit is None:
            log.info("pending: nothing left to deep-read")
            return 0
        unit_date, papers = unit
        log.info("pending: %s -> %d paper(s)", unit_date, len(papers))
        if dry_run:
            for p in papers:
                log.info("  would deep-read %s (score=%.0f)", p.paper_id, p.score or 0)
            return 0
        from .llm.sjtu_client import SJTUClient
        client = SJTUClient()
        total = _deep_read_papers(
            papers, unit_date, client=client, interests_text=interests_text,
            model=model or DAILY_MODEL, dry_run=False, verb="loop deep-read",
        )
        if total:
            update_index()  # homepage / archive pages pick up the new pages
            log.info("loop unit done: %d paper(s) deep-read; index refreshed", total)
        return total

    # Stub recovery has its own paper selection (scan pages, not score threshold)
    # and date scope (all stub dates by default), so it branches early.
    if retry_stubs_mode:
        if date_str:
            dates: set[str] | None = {date_str}
        elif since and until:
            dates = {d for d in {e["date"] for e in find_stub_entries()}
                     if since <= d <= until}
        else:
            dates = None  # all stub dates
        client = None
        if not dry_run:
            from .llm.sjtu_client import SJTUClient
            client = SJTUClient()
        total = retry_stubs(dates=dates, client=client, interests_text=interests_text,
                            model=model or DAILY_MODEL, dry_run=dry_run)
        if total and not dry_run:
            update_index()
            log.info("retry-stubs done: %d deep read(s) regenerated; index refreshed", total)
        return total

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
    from .logsetup import host_tag
    log_file = Path(log_dir) / f"{date.today().isoformat()}-{host_tag()}.log"

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
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--date", metavar="YYYY-MM-DD", help="backfill a single run date")
    g.add_argument("--since", metavar="YYYY-MM-DD",
                   help="start of a date range (requires --until)")
    ap.add_argument("--until", metavar="YYYY-MM-DD", help="end of a date range")
    ap.add_argument("--retry-stubs", action="store_true",
                    help="instead of threshold backfill, regenerate every FAILED "
                         "deep-read page (the '精读失败' stubs) from the score log; "
                         "scope to --date / --since..--until or default to all dates")
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
    ap.add_argument("--pending", action="store_true",
                    help="resident-loop mode: deep-read ONE unit of pending work "
                         "(highlights backlog -> failed stubs -> score-threshold) "
                         "and exit. Exit code 7 means nothing is pending, so a "
                         "loop (run_deepread_loop.ps1) can stop. Unit size = "
                         "--limit (default 1).")
    ap.add_argument("--window-days", type=int, default=0, metavar="N",
                    help="--pending: only look N days back (0 = all history)")
    args = ap.parse_args()

    if args.since and not args.until:
        ap.error("--since requires --until")
    if not (args.retry_stubs or args.pending or args.date or args.since):
        ap.error("specify --date, --since/--until, --retry-stubs, or --pending")

    total = run(
        date_str=args.date,
        since=args.since,
        until=args.until,
        threshold=args.threshold,
        model=args.model,
        limit=args.limit,
        dry_run=args.dry_run,
        sources=set(args.sources) if args.sources else None,
        force=args.force,
        retry_stubs_mode=args.retry_stubs,
        pending_mode=args.pending,
        window_days=args.window_days,
    )

    if args.pending and not args.dry_run:
        # 0 = did a unit, 7 = queue empty (the loop stops on 7).
        sys.exit(0 if total else 7)


if __name__ == "__main__":
    main()
