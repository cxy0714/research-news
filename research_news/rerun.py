"""Re-run the summary step for daily-report papers that came out garbled.

The daily pipeline occasionally renders a raw or cut-off JSON blob into a
paper's 摘要 — this happens when the model emits unescaped inner quotes or hits
``max_tokens`` mid-output, so the JSON can't be parsed and the fallback leaks
the raw text into the page (see ``docs/daily/*.md`` blocks containing
``\`\`\`json``). This tool finds those blocks and regenerates them in place:

  1. **LLM re-run** (best quality; needs ``SJTU_API_KEY``): paper metadata is
     reconstructed from ``data/llm_scores.jsonl`` and the summary is generated
     again with a fresh, larger-budget call.
  2. **Salvage** (offline, no API call): when the LLM is unavailable or also
     fails, the clean prose already present in the blob is recovered. This works
     because the model almost always finishes ``summary_zh`` before the array
     that gets truncated.

Only blocks that can actually be improved are rewritten; a block whose
``summary_zh`` itself was cut off mid-sentence is left untouched (and reported)
when no working LLM is available.

Usage::

    python -m research_news.rerun                  # scan every daily report
    python -m research_news.rerun --date 2026-06-01
    python -m research_news.rerun --offline         # salvage only, no API calls
    python -m research_news.rerun --dry-run         # report findings, write nothing
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
from pathlib import Path

from dotenv import load_dotenv

from .llm.pipeline import salvage_summary_fields, summary_looks_garbled, summarize_paper
from .llm.prompts import TOPICS
from .models import Paper
from .render.markdown import DOCS_DIR, RERUN_MARKER, _paper_block
from .score_log import SCORE_LOG_FILE

log = logging.getLogger("research_news.rerun")

_HEADING_RE = re.compile(
    r"^(#{4,6}) (\d+)\. \[([^\]]+)\]\(([^)]+)\) (?:—|-) (.*)$"
)
_BOUNDARY_RE = re.compile(r"^(#|---\s*$)")
_LEAKED_JSON_RE = re.compile(
    r'^\s*"(?:topic|summary_zh|key_techniques|why_relevant|novelty_flag)"\s*:',
    re.M,
)


# ── score-log lookup ──────────────────────────────────────────────────────────

def load_score_index() -> dict[str, list[dict]]:
    """Index every scored-paper row by paper_id (a paper may appear on several
    run dates). Rows carry the abstract needed to re-run the summary."""
    index: dict[str, list[dict]] = {}
    if not SCORE_LOG_FILE.exists():
        return index
    with SCORE_LOG_FILE.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            pid = row.get("paper_id")
            if pid:
                index.setdefault(pid, []).append(row)
    return index


def _pick_row(rows: list[dict], report_date: str) -> dict:
    """Prefer the row scored on the report's own date; else the most recent."""
    same_day = [r for r in rows if r.get("run_date") == report_date]
    pool = same_day or rows
    return max(pool, key=lambda r: r.get("run_date") or "")


def _paper_from_row(row: dict) -> Paper:
    p = Paper(
        source=row.get("source") or "arxiv",
        paper_id=row["paper_id"],
        title=row.get("title") or "",
        authors=list(row.get("authors") or []),
        abstract=row.get("abstract") or "",
        url=row.get("url") or "",
        categories=list(row.get("categories") or []),
        published=row.get("published"),
    )
    if row.get("score") is not None:
        p.score = float(row["score"])
    p.score_reason = row.get("score_reason")
    p.topic = row.get("topic")
    p.novelty_flag = row.get("novelty_flag")
    p.key_techniques = list(row.get("key_techniques") or [])
    return p


# ── markdown block parsing ────────────────────────────────────────────────────

def _block_is_garbled(block_text: str) -> bool:
    return (
        "```json" in block_text
        or RERUN_MARKER in block_text
        or bool(_LEAKED_JSON_RE.search(block_text))
    )


def _summary_blob(block_text: str) -> str:
    """The text after ``- **摘要**:`` to the end of the block — the raw JSON we
    try to salvage clean prose from."""
    parts = block_text.split("- **摘要**: ", 1)
    return parts[1] if len(parts) == 2 else ""


def _carry_over_from_block(paper: Paper, block_text: str) -> None:
    """Preserve rendered fields the score log doesn't store (venue, local PDF),
    and fall back to block-parsed score / categories when no log row was found."""
    m = re.search(r"- \*\*期刊/来源\*\*: (.+)", block_text)
    if m:
        paper.venue = m.group(1).strip()
    m = re.search(r"- \*\*本地 PDF\*\*: `(.+?)`", block_text)
    if m:
        paper.pdf_path = m.group(1).strip()
    if paper.score is None:
        m = re.search(r"相关性 (\d+)/10", block_text)
        if m:
            paper.score = float(m.group(1))
    if not paper.novelty_flag:
        m = re.search(r"novelty: `([^`]+)`", block_text)
        if m:
            paper.novelty_flag = m.group(1).strip()
    if not paper.categories:
        m = re.search(r"- \*\*分类\*\*: (.+)", block_text)
        if m:
            paper.categories = [c.strip() for c in m.group(1).split("·") if c.strip()]


def _paper_from_block(heading: re.Match, block_text: str) -> Paper:
    """Minimal Paper reconstructed from the rendered block alone, for the
    salvage path when the paper isn't in the score log (no abstract needed)."""
    paper = Paper(
        source="arxiv",
        paper_id=heading.group(3),
        title=heading.group(5).strip(),
        authors=[],
        abstract="",
        url=heading.group(4),
    )
    m = re.search(r"- \*\*作者\*\*: (.+)", block_text)
    if m:
        authors = m.group(1).replace(" et al.", "")
        paper.authors = [a.strip() for a in authors.split(",") if a.strip()]
    _carry_over_from_block(paper, block_text)
    return paper


def _apply_salvage(paper: Paper, salvaged: dict) -> None:
    paper.summary_zh = salvaged["summary_zh"].strip()
    if salvaged.get("why_relevant"):
        paper.why_relevant = salvaged["why_relevant"].strip()
    topic = (salvaged.get("topic") or paper.topic or "").strip().lower()
    paper.topic = topic if topic in TOPICS else (paper.topic or "other")
    if salvaged.get("key_techniques"):
        paper.key_techniques = salvaged["key_techniques"]
    if salvaged.get("novelty_flag"):
        paper.novelty_flag = salvaged["novelty_flag"].strip()
    # The visible prose is now clean; clear the marker.
    paper.summary_incomplete = False


def _regenerate_block(
    heading: re.Match,
    block_text: str,
    *,
    report_date: str,
    offline: bool,
    client,
    score_index: dict[str, list[dict]],
    interests_text: str,
    model: str | None,
) -> str | None:
    """Return a freshly rendered block, or None if it can't be improved."""
    prefix, n, pid = heading.group(1), int(heading.group(2)), heading.group(3)

    rows = score_index.get(pid)
    paper = _paper_from_row(_pick_row(rows, report_date)) if rows else None

    # 1) LLM re-run — needs the abstract from the score log.
    if not offline and client is not None and paper is not None and paper.abstract:
        try:
            _carry_over_from_block(paper, block_text)
            summarize_paper(client, paper, interests_text, model=model)
            if paper.summary_zh and not summary_looks_garbled(paper.summary_zh):
                how = "incomplete-but-recovered" if paper.summary_incomplete else "ok"
                log.info("re-ran %s via LLM (%s)", pid, how)
                return _paper_block(paper, n, heading_prefix=prefix)
            log.warning("LLM re-run for %s still unusable, falling back to salvage", pid)
        except Exception as e:  # noqa: BLE001 — keep going to salvage
            log.warning("LLM re-run failed for %s: %s — falling back to salvage", pid, e)

    # 2) Salvage the clean prose already present in the rendered blob.
    if paper is None:
        paper = _paper_from_block(heading, block_text)
    else:
        _carry_over_from_block(paper, block_text)
    salvaged = salvage_summary_fields(_summary_blob(block_text))
    if not salvaged.get("summary_zh"):
        log.warning(
            "cannot salvage %s (summary_zh truncated); needs an LLM re-run", pid
        )
        return None
    _apply_salvage(paper, salvaged)
    log.info("salvaged %s from rendered blob (no LLM)", pid)
    return _paper_block(paper, n, heading_prefix=prefix)


# ── per-file driver ───────────────────────────────────────────────────────────

def rerun_file(
    path: Path,
    *,
    offline: bool,
    client,
    score_index: dict[str, list[dict]],
    interests_text: str,
    model: str | None,
    dry_run: bool,
) -> tuple[int, int]:
    """Repair garbled blocks in one daily report.

    Returns (n_garbled_found, n_fixed)."""
    report_date = path.stem
    lines = path.read_text(encoding="utf-8").split("\n")

    # A dry run must never spend API calls, so it only considers the offline
    # (salvage) path; blocks that would need an LLM are reported as such.
    offline = offline or dry_run

    boundaries = sorted(
        {i for i, ln in enumerate(lines) if _BOUNDARY_RE.match(ln)} | {len(lines)}
    )

    # Collect (start, end, new_block_lines) for garbled paper blocks.
    edits: list[tuple[int, int, list[str]]] = []
    found = 0
    for i, ln in enumerate(lines):
        heading = _HEADING_RE.match(ln)
        if not heading:
            continue
        end = next(b for b in boundaries if b > i)
        block_text = "\n".join(lines[i:end])
        if not _block_is_garbled(block_text):
            continue
        found += 1
        new_block = _regenerate_block(
            heading,
            block_text,
            report_date=report_date,
            offline=offline,
            client=client,
            score_index=score_index,
            interests_text=interests_text,
            model=model,
        )
        if new_block is not None:
            new_lines = new_block.rstrip("\n").split("\n") + [""]
            edits.append((i, end, new_lines))

    if not edits:
        return found, 0

    if not dry_run:
        for start, end, new_lines in reversed(edits):  # back-to-front: indices stable
            lines[start:end] = new_lines
        path.write_text("\n".join(lines), encoding="utf-8")

    return found, len(edits)


def _make_client():
    """Best-effort SJTU client; returns None if the key isn't configured."""
    try:
        from .llm.sjtu_client import SJTUClient

        return SJTUClient()
    except Exception as e:  # noqa: BLE001
        log.warning("LLM client unavailable (%s) — running salvage-only", e)
        return None


def run(
    *,
    date_str: str | None = None,
    offline: bool = False,
    dry_run: bool = False,
    model: str | None = None,
) -> int:
    """Repair garbled summaries across daily reports. Returns the number fixed."""
    load_dotenv()

    if date_str:
        targets = [DOCS_DIR / f"{date_str}.md"]
        if not targets[0].exists():
            log.error("no daily report at %s", targets[0])
            return 0
    else:
        targets = sorted(DOCS_DIR.glob("*.md"))

    interests_path = Path("config/interests.yaml")
    interests_text = interests_path.read_text(encoding="utf-8") if interests_path.exists() else ""

    score_index = load_score_index()
    client = None if offline else _make_client()
    if model is None:
        # Same default the daily pipeline uses (kept in sync without importing
        # the heavy daily module / its PDF deps).
        model = os.environ.get("DAILY_MODEL", "glm-5.1")

    total_found = total_fixed = 0
    for path in targets:
        found, fixed = rerun_file(
            path,
            offline=offline,
            client=client,
            score_index=score_index,
            interests_text=interests_text,
            model=model,
            dry_run=dry_run,
        )
        if found:
            log.info("%s: %d garbled, %d %s", path.name, found, fixed,
                     "fixable" if dry_run else "fixed")
        total_found += found
        total_fixed += fixed

    log.info(
        "done: %d garbled block(s) across %d report(s); %d %s",
        total_found, len(targets), total_fixed,
        "would be fixed (dry run)" if dry_run else "fixed",
    )
    # Archive/index pages only list report links (no summaries), so they don't
    # need regenerating here.
    return total_fixed


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ap = argparse.ArgumentParser(
        description="Re-run garbled / truncated daily-report summaries."
    )
    ap.add_argument("--date", metavar="YYYY-MM-DD",
                    help="only this report (default: every docs/daily/*.md)")
    ap.add_argument("--offline", action="store_true",
                    help="salvage clean prose from the page; never call the LLM")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change without writing")
    ap.add_argument("--model", help="override the summary model")
    args = ap.parse_args()

    run(date_str=args.date, offline=args.offline, dry_run=args.dry_run, model=args.model)


if __name__ == "__main__":
    main()
