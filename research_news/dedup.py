"""Track which papers we've already reported so we don't repeat ourselves."""
from __future__ import annotations

import json
from pathlib import Path

from .models import Paper

SEEN_FILE = Path("data/seen_papers.json")


def load_seen() -> set[str]:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text()))
    return set()


def save_seen(ids: set[str]) -> None:
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps(sorted(ids), ensure_ascii=False, indent=2))


def filter_new(papers: list[Paper], seen: set[str]) -> list[Paper]:
    out = []
    for p in papers:
        key = f"{p.source}:{p.paper_id}"
        if key in seen:
            continue
        out.append(p)
    return out


def mark_seen(papers: list[Paper], seen: set[str]) -> set[str]:
    for p in papers:
        seen.add(f"{p.source}:{p.paper_id}")
    return seen
