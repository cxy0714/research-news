"""Track which papers we've already reported so we don't repeat ourselves."""
from __future__ import annotations

import json
from pathlib import Path

from .models import Paper

SEEN_FILE = Path("data/seen_papers.json")


def load_seen() -> set[str]:
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text(encoding="utf-8")))
    return set()


def save_seen(ids: set[str]) -> None:
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(
        json.dumps(sorted(ids), ensure_ascii=False, indent=2), encoding="utf-8"
    )


def filter_new(papers: list[Paper], seen: set[str]) -> list[Paper]:
    out = []
    known = set(seen)
    for p in papers:
        key = f"{p.source}:{p.paper_id}"
        if key in known:
            continue
        out.append(p)
        # A paper can be returned by multiple configured arXiv categories in
        # the same fetch. Treat the first occurrence as queued so it is scored
        # and rendered only once even before the persistent seen-set is saved.
        known.add(key)
    return out


def mark_seen(papers: list[Paper], seen: set[str]) -> set[str]:
    for p in papers:
        seen.add(f"{p.source}:{p.paper_id}")
    return seen
