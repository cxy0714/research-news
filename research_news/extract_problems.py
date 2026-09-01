"""Stage 1 of the problem-finding engine: extract grounded problem-seeds.

For each deep-read note we pull out, in structured form, what the *authors*
stated (limitations, future work, narrow conclusions) plus the direction's open
questions and arsenal-shaped transfer hints. Extraction hallucinates far less
than generation, and the structured rows are what the cross-paper synthesis
(synthesize.py) aggregates over to find recurring problems.

Rows accumulate in data/open_problems.jsonl, keyed by paper_id.
"""
from __future__ import annotations

import json
import logging
import re
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

from .llm.prompts import PROBLEM_EXTRACT_SYSTEM

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger(__name__)

OPEN_PROBLEMS_FILE = Path("data/open_problems.jsonl")
# Fields we expect back; used to normalize partial/again-malformed output.
_LIST_FIELDS = (
    "open_questions", "stated_limitations", "future_work",
    "narrow_conclusions", "cited_tensions", "transfer_hints",
)


def _strip_fence(s: str) -> str:
    s = s.strip()
    if s.startswith("```"):
        s = re.sub(r"^```[a-zA-Z]*\n?", "", s)
        s = re.sub(r"\n?```$", "", s)
    return s.strip()


def parse_extraction(raw: str) -> dict | None:
    """Best-effort parse of the extraction JSON. Returns None if unusable."""
    text = _strip_fence(raw)
    try:
        obj = json.loads(text)
    except Exception:
        # Grab the outermost {...} block and retry.
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if not m:
            return None
        try:
            obj = json.loads(m.group(0))
        except Exception:
            return None
    if not isinstance(obj, dict):
        return None
    norm: dict = {"direction": obj.get("direction") or ""}
    for f in _LIST_FIELDS:
        v = obj.get(f) or []
        norm[f] = v if isinstance(v, list) else [v]
    return norm


_CONFLICT_PREFIXES = ("<<<<<<<", "=======", ">>>>>>>")


def _warn_if_conflicted(path: Path, text: str) -> None:
    """Shout if a merge left conflict markers in the JSONL.

    Both loaders skip unparseable lines, so a conflicted file degrades
    silently into "half the corpus is missing" — which is exactly how this
    file sat broken for three months. Make it loud instead.
    """
    if any(line.startswith(_CONFLICT_PREFIXES) for line in text.splitlines()):
        log.error(
            "%s contains git conflict markers — rows are being silently "
            "dropped. Resolve the conflict (union by paper_id) before relying "
            "on this file.", path,
        )


def load_done_ids(path: Path = OPEN_PROBLEMS_FILE) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    _warn_if_conflicted(path, text)
    ids: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ids.add(json.loads(line)["paper_id"])
        except Exception:
            continue
    return ids


def load_rows(path: Path = OPEN_PROBLEMS_FILE) -> dict[str, dict]:
    """Return {paper_id: row} for all extracted rows (last one wins)."""
    out: dict[str, dict] = {}
    if not path.exists():
        return out
    text = path.read_text(encoding="utf-8")
    _warn_if_conflicted(path, text)
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
            out[row["paper_id"]] = row
        except Exception:
            continue
    return out


def _append_row(row: dict, path: Path = OPEN_PROBLEMS_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def extract_one(
    client: "SJTUClient",
    *,
    paper_id: str,
    title: str,
    topic: str,
    body: str,
    model: str | None = None,
) -> dict | None:
    """Run the extraction LLM call on one deep-read note. Returns the parsed dict."""
    user = f"标题: {title}\n主题: {topic}\n\n## 精读笔记\n{body}"
    try:
        raw = client.chat(
            [
                {"role": "system", "content": PROBLEM_EXTRACT_SYSTEM},
                {"role": "user", "content": user},
            ],
            model=model,
            max_tokens=2500,
        )
    except Exception as e:  # noqa: BLE001
        log.warning("problem extraction failed for %s: %s", paper_id, e)
        return None
    return parse_extraction(raw)


def backfill(
    client: "SJTUClient",
    entries: list[dict],
    *,
    model: str | None = None,
    run_date: date | None = None,
) -> dict[str, dict]:
    """Ensure every entry has an extraction row; extract the missing ones.

    `entries` are deep-read index dicts that also carry a "body" key. Returns
    {paper_id: extraction_row} for all entries that now have a row.
    """
    existing = load_rows()
    done = set(existing)
    run_date = run_date or date.today()
    n_new = 0
    for e in entries:
        pid = e["paper_id"]
        if pid in done:
            continue
        body = e.get("body") or ""
        if not body.strip():
            continue
        parsed = extract_one(
            client, paper_id=pid, title=e.get("title", ""),
            topic=e.get("topic", "other"), body=body, model=model,
        )
        if parsed is None:
            continue
        row = {
            "paper_id": pid,
            "date": e.get("date"),
            "run_type": e.get("run_type"),
            "topic": e.get("topic", "other"),
            "title": e.get("title", ""),
            "venue": e.get("venue"),
            "extracted_on": run_date.isoformat(),
            **parsed,
        }
        _append_row(row)
        existing[pid] = row
        done.add(pid)
        n_new += 1
        log.info("extracted problems %d: %s", n_new, pid)
    if n_new:
        log.info("problem extraction: %d new rows → %s", n_new, OPEN_PROBLEMS_FILE)
    return existing
