"""Retroactively add the '🗂 其他论文' (low-relevance / un-summarised) section to
*past* daily reports, recovered from ``data/llm_scores.jsonl``.

Daily reports used to show only papers above the show-threshold
(``score_threshold_show``); everything below was scored and then dropped from
the page. But every scored paper — including the dropped ones — is recorded in
``data/llm_scores.jsonl`` with its score and the LLM's one-line reason, so we can
list the dropped papers under each past report **without re-scraping, re-scoring,
or any LLM call**.

For each daily page ``docs/daily/<date>.md``:

  1. read the arXiv rows scored on ``<date>`` from the score log;
  2. parse the paper_ids already rendered on the page (the summarised digest);
  3. the remaining scored papers are the "low" set → render the 🗂 section
     (score + reason, highest first) with the shared renderer;
  4. insert it just above the footer and refresh the count line's '其他 N 篇'.

Idempotent: an existing 🗂 section is replaced (not appended), so re-running is
safe — handy after another daily run adds new rows to the log.

Usage::

    python -m research_news.backfill_low_relevance                 # every daily page
    python -m research_news.backfill_low_relevance --date 2026-06-12
    python -m research_news.backfill_low_relevance --since 2026-06-01 --until 2026-06-13
    python -m research_news.backfill_low_relevance --dry-run
"""
from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path

from .render.markdown import (
    DOCS_DIR,
    LOW_SECTION_HEADING,
    _footer,
    format_daily_count_line,
    render_low_section,
)
from .rerun import _paper_from_row, load_score_index

log = logging.getLogger("research_news.backfill_low")

# A rendered paper-block heading: "#### 3. [2606.14544](url) — Title"
# (3-6 hashes, em-dash or hyphen). Group 1 is the paper_id.
_HEADING_RE = re.compile(r"^#{3,6} \d+\. \[([^\]]+)\]\([^)]+\) (?:—|-) ")
# The tally line under the title. High / mid / (optional 其他) / events counts.
_COUNT_LINE_RE = re.compile(
    r"^- 高相关论文 (\d+) 篇 · 中相关 (\d+) 篇(?: · 其他 \d+ 篇)?"
    r"(?: · 会议/Seminar 事件 (\d+) 条)?.*$",
    re.M,
)
_DATE_STEM_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_FOOTER_SEP_RE = re.compile(r"\n---\n")


def rows_for_date(
    score_index: dict[str, list[dict]],
    run_date: str,
    *,
    source: str = "arxiv",
) -> dict[str, dict]:
    """Score-log rows scored on ``run_date`` for ``source``, deduped by paper_id
    (highest score wins). The journal pipeline logs to the same file, so the
    ``source`` filter keeps the daily backfill to arXiv papers only."""
    best: dict[str, dict] = {}
    for pid, rows in score_index.items():
        for row in rows:
            if row.get("run_date") != run_date:
                continue
            if (row.get("source") or "arxiv") != source:
                continue
            cur = best.get(pid)
            if cur is None or (row.get("score") or 0) > (cur.get("score") or 0):
                best[pid] = row
    return best


def _rendered_ids(body: str) -> set[str]:
    """paper_ids already rendered as blocks in the page body (the digest)."""
    return {m.group(1) for ln in body.splitlines() if (m := _HEADING_RE.match(ln))}


def _strip_footer_and_low(text: str) -> str:
    """Return the page body — title, count line, high/mid/events — with any
    existing 🗂 section and the footer removed (both get re-rendered)."""
    cut = len(text)
    i_low = text.find(LOW_SECTION_HEADING)
    if i_low != -1:
        cut = min(cut, i_low)
    m_foot = _FOOTER_SEP_RE.search(text)
    if m_foot:
        cut = min(cut, m_foot.start())
    return text[:cut].rstrip("\n")


def backfill_page(
    path: Path, score_index: dict[str, list[dict]], *, dry_run: bool
) -> int:
    """Add/refresh the 🗂 section on one daily page.

    Returns the number of low papers written, or ``-1`` when the page is skipped
    (filename isn't a date, or no arXiv rows were logged for that date)."""
    if not _DATE_STEM_RE.match(path.stem):
        return -1
    run_date = path.stem

    best = rows_for_date(score_index, run_date)
    if not best:
        log.info("%s: no arXiv scores in log — skip", run_date)
        return -1

    text = path.read_text(encoding="utf-8")
    body = _strip_footer_and_low(text)
    had_low = LOW_SECTION_HEADING in text
    rendered = _rendered_ids(body)

    low_papers = [
        _paper_from_row(row) for pid, row in best.items() if pid not in rendered
    ]
    low_papers.sort(key=lambda p: p.score or 0, reverse=True)

    # Refresh the count line's '其他 N 篇' (preserving the high/mid/event counts).
    def _count_repl(m: re.Match) -> str:
        n_high, n_mid = int(m.group(1)), int(m.group(2))
        n_events = int(m.group(3)) if m.group(3) else 0
        return format_daily_count_line(n_high, n_mid, len(low_papers), n_events)

    body, _ = _COUNT_LINE_RE.subn(_count_repl, body, count=1)

    parts = [body]
    low_lines = render_low_section(low_papers)
    if low_lines:
        parts.append("")
        parts.extend(low_lines)
    parts.append(_footer())
    new_text = "\n".join(parts) + "\n"

    if new_text == text:
        log.info("%s: already up to date (%d low)", run_date, len(low_papers))
        return len(low_papers)

    action = "would write" if dry_run else "wrote"
    extra = " (replacing existing section)" if had_low else ""
    log.info("%s: %s %d low paper(s)%s", run_date, action, len(low_papers), extra)
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return len(low_papers)


def run(
    *,
    date_str: str | None = None,
    since: str | None = None,
    until: str | None = None,
    dry_run: bool = False,
    daily_dir: Path = DOCS_DIR,
) -> int:
    """Backfill the 🗂 section across daily pages. Returns total low papers."""
    score_index = load_score_index()
    pages = sorted(daily_dir.glob("*.md")) if daily_dir.exists() else []
    if date_str:
        pages = [p for p in pages if p.stem == date_str]
    elif since and until:
        pages = [p for p in pages if since <= p.stem <= until]

    if not pages:
        log.warning("no daily pages matched")
        return 0

    n_pages = total_low = 0
    for path in pages:
        n = backfill_page(path, score_index, dry_run=dry_run)
        if n >= 0:
            n_pages += 1
            total_low += n

    log.info(
        "%s %d page(s); %d low paper(s) total",
        "would update" if dry_run else "updated",
        n_pages,
        total_low,
    )
    return total_low


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ap = argparse.ArgumentParser(
        description="Recover scored-but-dropped arXiv papers into past daily "
        "reports' '🗂 其他论文' section, from data/llm_scores.jsonl (no LLM)."
    )
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--date", metavar="YYYY-MM-DD", help="only this daily page")
    g.add_argument("--since", metavar="YYYY-MM-DD",
                   help="start of a date range (requires --until)")
    ap.add_argument("--until", metavar="YYYY-MM-DD", help="end of a date range")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change without writing")
    args = ap.parse_args()

    if args.since and not args.until:
        ap.error("--since requires --until")

    run(date_str=args.date, since=args.since, until=args.until, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
