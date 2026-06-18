"""Per-issue 导览 for journal pages — an LLM overview of the issue's main themes.

New journal runs get it inline (journals.py passes ``overview=`` to
``render_journal_page``). Past pages are backfilled here, **from the page itself**
(no re-scrape / re-score): parse each issue's papers (title + topic + 中文摘要),
generate the 导览, and insert it just under the count line.

    python -m research_news.journal_overview                 # every journal page
    python -m research_news.journal_overview --only AoS,JASA  # by journal short name
    python -m research_news.journal_overview --date 2026-05-26
    python -m research_news.journal_overview --dry-run        # count, no LLM, no write
    python -m research_news.journal_overview --force          # regenerate existing ones

Idempotent: a page that already has a 导览 is skipped unless ``--force``.
"""
from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING

from .llm.prompts import JOURNAL_OVERVIEW_SYSTEM
from .render.markdown import (
    JOURNALS_DIR,
    JOURNAL_OVERVIEW_HEADING,
    _journal_short_from_stem,
    render_journal_overview,
)

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger("research_news.journal_overview")

# Topic group heading: "## 因果推断  *(causal_inference, 1 篇)*" → label, topic key.
_TOPIC_HEAD_RE = re.compile(r"^##\s+(.+?)\s+\*\(([a-z_]+),\s*\d+\s*篇\)\*")
# Paper heading: "### 1. [<id>](<url>) — Title"  (### under ## topics).
_PAPER_HEAD_RE = re.compile(r"^#{3,4}\s+\d+\.\s+\[[^\]]+\]\([^)]+\)\s+(?:—|-)\s+(.+)$")
_SUMMARY_RE = re.compile(r"^- \*\*摘要\*\*:\s*(.+)$")


# ── parse an existing page ────────────────────────────────────────────────────

def parse_page_papers(body: str) -> list[dict]:
    """Pull [{title, topic, summary}] from a rendered journal page."""
    items: list[dict] = []
    topic: str | None = None
    cur: dict | None = None
    for ln in body.splitlines():
        mt = _TOPIC_HEAD_RE.match(ln)
        if mt:
            topic = mt.group(2)
            continue
        mp = _PAPER_HEAD_RE.match(ln)
        if mp:
            cur = {"title": mp.group(1).strip(), "topic": topic, "summary": ""}
            items.append(cur)
            continue
        ms = _SUMMARY_RE.match(ln)
        if ms and cur is not None:
            cur["summary"] = ms.group(1).strip()
    return items


def has_overview(text: str) -> bool:
    return JOURNAL_OVERVIEW_HEADING in text


def strip_overview(text: str) -> str:
    """Remove an existing 导览 section (heading → next topic heading)."""
    i = text.find(JOURNAL_OVERVIEW_HEADING)
    if i == -1:
        return text
    nxt = text.find("\n## ", i + len(JOURNAL_OVERVIEW_HEADING))
    end = nxt + 1 if nxt != -1 else len(text)
    return text[:i].rstrip("\n") + "\n\n" + text[end:].lstrip("\n")


def insert_overview(text: str, overview: str) -> str:
    """Insert the 导览 section just before the first topic group heading."""
    section = "\n".join(render_journal_overview(overview))
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and ln != JOURNAL_OVERVIEW_HEADING and _TOPIC_HEAD_RE.match(ln):
            return "\n".join(lines[:i] + [section, ""] + lines[i:])
    return text  # no topic groups (e.g. empty issue) → leave unchanged


# ── generate ──────────────────────────────────────────────────────────────────

def build_input(items: list[dict], label: str) -> str:
    by_topic: dict[str, list[dict]] = {}
    for it in items:
        by_topic.setdefault(it.get("topic") or "other", []).append(it)
    blocks: list[str] = []
    for topic, group in by_topic.items():
        blocks.append(f"【{topic}】")
        for it in group:
            line = f"- {it['title']}"
            if it.get("summary"):
                line += "：" + re.sub(r"\s+", " ", it["summary"])[:300]
            blocks.append(line)
    return f"{label}，共 {len(items)} 篇：\n\n" + "\n".join(blocks)


def generate(client: "SJTUClient", items: list[dict], label: str,
             *, model: str | None = None) -> str:
    return client.chat(
        [
            {"role": "system", "content": JOURNAL_OVERVIEW_SYSTEM},
            {"role": "user", "content": build_input(items, label)},
        ],
        model=model,
        max_tokens=2200,
    )


# ── backfill ──────────────────────────────────────────────────────────────────

def _issue_label_from_page(body: str) -> str:
    m = re.match(r"^#\s+(.+)", body)
    return m.group(1).strip() if m else "this issue"


def backfill_page(path: Path, client: "SJTUClient | None", *, force: bool, dry_run: bool) -> int:
    """Add a 导览 to one journal page. Returns 1 if (it would be) written, 0 if
    skipped (already has one, or no parseable papers)."""
    text = path.read_text(encoding="utf-8")
    if has_overview(text) and not force:
        log.info("%s: already has 导览 — skip", path.name)
        return 0
    items = parse_page_papers(text)
    if not items:
        log.info("%s: no papers parsed — skip", path.name)
        return 0
    if dry_run:
        log.info("%s: would generate 导览 over %d paper(s)", path.name, len(items))
        return 1
    base = strip_overview(text) if has_overview(text) else text
    try:
        overview = generate(client, items, _issue_label_from_page(base), model=None)
    except Exception as e:  # noqa: BLE001
        log.warning("%s: overview generation failed: %s", path.name, e)
        return 0
    new_text = insert_overview(base, overview)
    if new_text == text:
        return 0
    path.write_text(new_text if new_text.endswith("\n") else new_text + "\n", encoding="utf-8")
    log.info("%s: wrote 导览 (%d paper(s))", path.name, len(items))
    return 1


def run(
    *,
    only: list[str] | None = None,
    date_str: str | None = None,
    since: str | None = None,
    until: str | None = None,
    force: bool = False,
    dry_run: bool = False,
    journals_dir: Path = JOURNALS_DIR,
) -> int:
    pages = sorted(journals_dir.glob("*.md")) if journals_dir.exists() else []
    if date_str:
        pages = [p for p in pages if p.stem.startswith(date_str)]
    elif since and until:
        pages = [p for p in pages if since <= p.stem[:10] <= until]
    if only:
        want = {s.strip().lower() for s in only}
        pages = [p for p in pages if _journal_short_from_stem(p.stem).lower() in want]
    if not pages:
        log.warning("no journal pages matched")
        return 0

    client = None
    if not dry_run:
        from dotenv import load_dotenv

        from .llm.sjtu_client import SJTUClient
        load_dotenv()
        client = SJTUClient()

    n = 0
    for path in pages:
        n += backfill_page(path, client, force=force, dry_run=dry_run)
    log.info("%s 导览 on %d/%d page(s)", "would write" if dry_run else "wrote", n, len(pages))
    return n


def _split(values: list[str] | None) -> list[str]:
    out: list[str] = []
    for v in values or []:
        out.extend(part.strip() for part in v.split(",") if part.strip())
    return out


def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    ap = argparse.ArgumentParser(
        description="Add a per-issue 导览 (LLM overview) to journal pages, parsed "
                    "from the page itself.")
    ap.add_argument("--only", action="append", default=[],
                    help="journal short names (comma-separated / repeatable), e.g. --only AoS,JASA")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--date", metavar="YYYY-MM-DD", help="only pages with this date prefix")
    g.add_argument("--since", metavar="YYYY-MM-DD", help="start of a date range (needs --until)")
    ap.add_argument("--until", metavar="YYYY-MM-DD", help="end of a date range")
    ap.add_argument("--force", action="store_true", help="regenerate even if a 导览 exists")
    ap.add_argument("--dry-run", action="store_true", help="count pages, no LLM, no write")
    args = ap.parse_args()
    if args.since and not args.until:
        ap.error("--since requires --until")
    run(only=_split(args.only), date_str=args.date, since=args.since, until=args.until,
        force=args.force, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
