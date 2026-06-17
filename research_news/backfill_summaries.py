"""Promote above-threshold papers that past daily reports left un-summarised.

When the old 25-paper summary cap was in effect, papers that scored at/above
``score_threshold_show`` but past the cap were dropped to the page's
"🗂 其他论文" section with only a score + reason. This tool gives them the
first-pass Chinese summary they should have had and re-renders the page so they
move up into the topic-grouped 📌/⭐ sections.

For each daily page:

  1. parse the page — existing summarised papers (kept faithfully, their prose
     lives only on the page, not in the score log) and the 🗂 papers;
  2. for 🗂 papers scoring >= ``score_threshold_show``: pull the abstract from
     ``data/llm_scores.jsonl`` and run the summariser (LLM);
  3. re-render with ``render_daily`` — promoted papers join the topic groups,
     the 🗂 section shrinks to genuinely below-threshold papers.

Needs ``SJTU_API_KEY`` (it summarises). ``--dry-run`` lists what would be
promoted without any LLM call or write. ``--self-check`` re-renders every page
*without* promoting and reports any that don't round-trip byte-for-byte — a
safety net for the page parser, runnable with no API key.

Usage::

    python -m research_news.backfill_summaries --dry-run
    python -m research_news.backfill_summaries --date 2026-06-12
    python -m research_news.backfill_summaries --since 2026-06-01 --until 2026-06-13
    python -m research_news.backfill_summaries --self-check
"""
from __future__ import annotations

import argparse
import logging
import os
import re
from datetime import date
from pathlib import Path

import yaml
from dotenv import load_dotenv

from .models import Paper
from .render.markdown import (
    DOCS_DIR,
    RERUN_MARKER,
    render_daily,
)
from .backfill_low_relevance import rows_for_date
from .rerun import _paper_from_row, load_score_index

log = logging.getLogger("research_news.backfill_summaries")

DAILY_MODEL = os.environ.get("DAILY_MODEL", "glm-5.1")

# Section markers + the paper/group headings render_daily emits.
_SEC_HIGH, _SEC_MID, _SEC_LOW, _SEC_EVENTS = "## ⭐", "## 📌", "## 🗂", "## 📅"
_GROUP_RE = re.compile(r"^### .*\*\((\w+), \d+ 篇\)\*\s*$")
_PAPER_HEAD_RE = re.compile(r"^#{3,4} \d+\. \[([^\]]+)\]\(([^)]+)\) (?:—|-) (.*)$")


def _thresholds() -> tuple[float, float]:
    """(score_threshold_show, score_threshold_highlight) from interests.yaml."""
    path = Path("config/interests.yaml")
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    cfg = cfg or {}
    return (
        float(cfg.get("score_threshold_show", 4)),
        float(cfg.get("score_threshold_highlight", 8)),
    )


def _interests_text() -> str:
    path = Path("config/interests.yaml")
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _read_raw(path: Path) -> str:
    """Read a page preserving its exact bytes (newline='' → no universal-newline
    translation), so stray CRs inside summaries survive the round-trip."""
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def _write_raw(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


# ── page parsing ──────────────────────────────────────────────────────────────

def _grab(body: str, pat: str) -> str | None:
    m = re.search(pat, body, re.M)
    return m.group(1).strip() if m else None


def _grab_field(body: str, label: str) -> str | None:
    """A field value that may span several lines (摘要 / 为什么对您有用 can carry
    embedded newlines from the model). Runs from after the label to the next
    '- ' bullet or the block end."""
    m = re.search(rf"- \*\*{re.escape(label)}\*\*: (.*?)(?=\n- |\Z)", body, re.S)
    return m.group(1).strip() if m else None


def _paper_from_block(
    pid: str, url: str, title: str, body: str, topic: str | None
) -> Paper:
    """Reconstruct a Paper from one rendered block, capturing exactly the fields
    shown so a re-render reproduces the block. ``authors`` here is the displayed
    (truncated) list — callers patch the full list from the score log so the
    'et al.' suffix round-trips."""
    p = Paper(source="arxiv", paper_id=pid, title=title, authors=[], abstract="", url=url)

    # 作者 / 机构 / 分类 are rendered by joining a list. We store each whole
    # displayed string as a single pre-formatted element so the render-time join
    # is a no-op and the line round-trips verbatim — robust to commas inside
    # author/affiliation names and the 'et al.' / '… 等' truncation suffixes
    # (and avoids depending on the score log's inconsistent author formatting).
    authors_s = _grab(body, r"^- \*\*作者\*\*: (.+)$")
    if authors_s is not None:
        p.authors = [authors_s]
    inst_s = _grab(body, r"^- \*\*机构\*\*: (.+)$")
    if inst_s is not None:
        p.institutions = [inst_s]
    cats_s = _grab(body, r"^- \*\*分类\*\*: (.+)$")
    if cats_s is not None:
        p.categories = [cats_s]

    p.venue = _grab(body, r"^- \*\*期刊/来源\*\*: (.+)$")

    rel = _grab(body, r"^- 相关性 (\d+)/10")
    if rel is not None:
        p.score = float(rel)
    p.novelty_flag = _grab(body, r"novelty: `([^`]+)`")
    p.summary_zh = _grab_field(body, "摘要")

    kt_s = _grab(body, r"^- \*\*关键技术\*\*: (.+)$")
    if kt_s:
        p.key_techniques = re.findall(r"`([^`]+)`", kt_s)
    p.why_relevant = _grab_field(body, "为什么对您有用")
    p.pdf_path = _grab(body, r"^- \*\*本地 PDF\*\*: `(.+)`$")
    p.summary_incomplete = RERUN_MARKER in body
    p.topic = topic
    return p


def _parse_page(text: str) -> tuple[list[Paper], list[Paper], bool]:
    """Parse a daily page into (digest_papers, low_papers, has_events).

    digest_papers carry section info via a temporary ``_section`` attribute
    ('high'/'mid'); low_papers carry their score (for the threshold split)."""
    lines = text.split("\n")
    boundaries = sorted(
        {i for i, ln in enumerate(lines) if ln.startswith("#") or ln.strip() == "---"}
        | {len(lines)}
    )

    digest: list[Paper] = []
    low: list[Paper] = []
    section: str | None = None
    topic: str | None = None
    has_events = False

    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            if ln.startswith(_SEC_HIGH):
                section = "high"
            elif ln.startswith(_SEC_MID):
                section = "mid"
            elif ln.startswith(_SEC_LOW):
                section = "low"
            elif ln.startswith(_SEC_EVENTS):
                section, has_events = "events", True
            else:
                section = "other"
            topic = None
            continue
        if section in ("high", "mid"):
            mg = _GROUP_RE.match(ln)
            if mg:
                topic = mg.group(1)
                continue
        mh = _PAPER_HEAD_RE.match(ln)
        if mh and section in ("high", "mid", "low"):
            pid, url, title = mh.group(1), mh.group(2), mh.group(3)
            end = next(b for b in boundaries if b > i)
            body = "\n".join(lines[i + 1 : end])
            p = _paper_from_block(pid, url, title, body, topic if section != "low" else None)
            if section == "low":
                low.append(p)
            else:
                p._section = section  # type: ignore[attr-defined]
                digest.append(p)
    return digest, low, has_events


# ── re-render ─────────────────────────────────────────────────────────────────

def _rerender_unchanged(text: str, best: dict[str, dict], when: str) -> str:
    """Re-render a page WITHOUT promoting anything (self-check). Existing digest
    papers come from the page; 🗂 papers are rebuilt from the log exactly as the
    low-relevance backfill wrote them. Output should equal the input."""
    digest, low_page, _ = _parse_page(text)
    _, th_high = _thresholds()
    low = [_paper_from_row(best[p.paper_id]) for p in low_page if p.paper_id in best]
    return _render_to_string(digest, low, th_high, when)


def _render_to_string(
    digest: list[Paper], low: list[Paper], th_high: float, when: str
) -> str:
    high, mid = [], []
    for p in digest:
        sec = getattr(p, "_section", None)
        if sec == "high" or (sec is None and (p.score or 0) >= th_high):
            high.append(p)
        else:
            mid.append(p)
    import tempfile
    tmp = Path(tempfile.mkdtemp())
    render_daily(high, mid, low, [], when=date.fromisoformat(when), output_dir=tmp)
    return _read_raw(tmp / f"{when}.md")


# ── per-page driver ───────────────────────────────────────────────────────────

def backfill_page(
    path: Path,
    score_index: dict[str, list[dict]],
    *,
    client,
    interests_text: str,
    model: str,
    dry_run: bool,
    self_check: bool,
) -> int:
    """Promote a page's above-threshold 🗂 papers. Returns the number promoted
    (or, in self-check, 0 and logs whether the page round-trips)."""
    when = path.stem
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", when):
        return 0
    best = rows_for_date(score_index, when)
    # newline="" keeps the file's bytes verbatim — some summaries carry a stray
    # CR (an unescaped LaTeX \r…), and universal-newline mode would split it.
    text = _read_raw(path)
    th_show, th_high = _thresholds()
    digest, low_page, has_events = _parse_page(text)
    promote = [p for p in low_page if (p.score or 0) >= th_show]

    if self_check:
        if not promote:
            return 0  # never rewritten → nothing to verify
        try:
            rendered = _rerender_unchanged(text, best, when)
        except Exception as e:  # noqa: BLE001
            log.error("%s: self-check FAILED to render (%s)", when, e)
            return 0
        if rendered == text:
            log.info("%s: round-trips ✓ (%d promote candidate(s))", when, len(promote))
        else:
            log.error("%s: round-trip MISMATCH — parser would alter this page", when)
        return 0

    keep_low_ids = {p.paper_id for p in low_page if (p.score or 0) < th_show}

    if not promote:
        log.info("%s: nothing above %.0f in 🗂 — skip", when, th_show)
        return 0
    if has_events:
        log.warning("%s: page has an events section — skipping to avoid dropping it", when)
        return 0

    log.info("%s: %d paper(s) to promote (score >= %.0f):", when, len(promote), th_show)
    for p in sorted(promote, key=lambda x: x.score or 0, reverse=True):
        log.info("  %s  score=%.0f  %s", p.paper_id, p.score or 0, p.title[:64])
    if dry_run:
        return len(promote)

    # Build the promoted papers from the log (abstract!) + summarise them.
    promoted: list[Paper] = []
    for rec in promote:
        row = best.get(rec.paper_id)
        if not row or not (row.get("abstract")):
            log.warning("  %s: no abstract in score log — leaving in 🗂", rec.paper_id)
            keep_low_ids.add(rec.paper_id)
            continue
        p = _paper_from_row(row)
        try:
            from .llm.pipeline import summarize_paper
            summarize_paper(client, p, interests_text, model=model)
        except Exception as e:  # noqa: BLE001
            log.warning("  %s: summary failed (%s) — leaving in 🗂", rec.paper_id, e)
            keep_low_ids.add(rec.paper_id)
            continue
        promoted.append(p)

    if not promoted:
        log.info("%s: no papers summarised — page unchanged", when)
        return 0

    # Best-effort institution lookup so promoted papers match the others.
    try:
        from .scrapers import affiliations as affil
        affil.backfill_affiliations(promoted)
    except Exception as e:  # noqa: BLE001
        log.warning("%s: affiliation lookup skipped (%s)", when, e)

    digest_all = digest + promoted
    low = [_paper_from_row(best[pid]) for pid in keep_low_ids if pid in best]

    rendered = _render_to_string(digest_all, low, th_high, when)
    _write_raw(path, rendered)
    log.info("%s: promoted %d paper(s); 🗂 now %d", when, len(promoted), len(low))
    return len(promoted)


def run(
    *,
    date_str: str | None = None,
    since: str | None = None,
    until: str | None = None,
    model: str | None = None,
    dry_run: bool = False,
    self_check: bool = False,
    daily_dir: Path = DOCS_DIR,
) -> int:
    load_dotenv()
    score_index = load_score_index()
    interests_text = _interests_text()

    pages = sorted(daily_dir.glob("*.md")) if daily_dir.exists() else []
    if date_str:
        pages = [p for p in pages if p.stem == date_str]
    elif since and until:
        pages = [p for p in pages if since <= p.stem <= until]
    if not pages:
        log.warning("no daily pages matched")
        return 0

    client = None
    if not (dry_run or self_check):
        from .llm.sjtu_client import SJTUClient
        client = SJTUClient()

    total = 0
    for path in pages:
        total += backfill_page(
            path, score_index,
            client=client, interests_text=interests_text,
            model=model or DAILY_MODEL, dry_run=dry_run, self_check=self_check,
        )
    if self_check:
        log.info("self-check done over %d page(s)", len(pages))
    else:
        log.info("%s %d paper(s) across %d page(s)",
                 "would promote" if dry_run else "promoted", total, len(pages))
    return total


def _setup_logging(log_dir: str = "logs") -> None:
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
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(formatter)
    root.addHandler(fh)
    httpx_log = logging.getLogger("httpx")
    httpx_log.setLevel(logging.WARNING)


def main() -> None:
    _setup_logging()
    ap = argparse.ArgumentParser(
        description="Promote above-threshold papers stuck in past dailies' 🗂 "
        "section by summarising them and re-rendering the page."
    )
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--date", metavar="YYYY-MM-DD", help="only this daily page")
    g.add_argument("--since", metavar="YYYY-MM-DD",
                   help="start of a date range (requires --until)")
    ap.add_argument("--until", metavar="YYYY-MM-DD", help="end of a date range")
    ap.add_argument("--model", help=f"summary model (default: {DAILY_MODEL})")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be promoted; no LLM, no write")
    ap.add_argument("--self-check", action="store_true",
                    help="re-render each page WITHOUT promoting and report any "
                         "that don't round-trip byte-for-byte (no API key needed)")
    args = ap.parse_args()
    if args.since and not args.until:
        ap.error("--since requires --until")

    run(date_str=args.date, since=args.since, until=args.until, model=args.model,
        dry_run=args.dry_run, self_check=args.self_check)


if __name__ == "__main__":
    main()
