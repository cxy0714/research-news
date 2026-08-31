"""Publish a public, read-only snapshot of the personal favorites collection.

The interactive site stores favorites (and read state, and per-paper comments)
in a *private* GitHub Gist that only the signed-in owner can see. This script
is meant to run on a schedule (GitHub Actions): it reads that gist with a token,
joins each favorite against the repo's existing ``data/highlights.json`` to pull
in the Chinese summary / score / key techniques (so the gist itself stays tiny),
and writes ``docs/data/favorites_public.json``. The favorites page then renders
that snapshot for visitors who are not signed in.

Only favorites are published — read state and the deep-read queue are never
exposed. Per the owner's choice, comments ARE included in the public snapshot.

Env:
  GIST_TOKEN   GitHub token with ``gist`` scope (required).
  RN_GIST_ID   Optional gist id; if unset, the gist is discovered by its
               description / state filename, mirroring the browser client.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from . import gist_state

HIGHLIGHTS_PATH = Path("data/highlights.json")
OUT_PATH = Path("docs/data/favorites_public.json")

# Fields copied from the highlights manifest into each published entry.
ENRICH_FIELDS = ("summary_zh", "score", "key_techniques", "why_relevant",
                 "venue", "authors")


def _load_highlights() -> dict[str, dict]:
    if not HIGHLIGHTS_PATH.exists():
        return {}
    try:
        rows = json.loads(HIGHLIGHTS_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    by_id: dict[str, dict] = {}
    for row in rows:
        pid = row.get("paper_id")
        if pid and pid not in by_id:
            by_id[pid] = row
    return by_id


def build_public(state: dict, highlights: dict[str, dict]) -> list[dict]:
    favorites = (state or {}).get("favorites") or {}
    out: list[dict] = []
    for pid, fav in favorites.items():
        entry = {
            "paper_id": fav.get("paper_id") or pid,
            "title": fav.get("title") or pid,
            "url": fav.get("url") or "",
            "deep_read_url": fav.get("deep_read_url") or "",
            "category": fav.get("category") or "未分类",
            "date": fav.get("date") or "",
            "week": fav.get("week") or "",
            "note": fav.get("note") or "",
        }
        hi = highlights.get(entry["paper_id"])
        if hi:
            entry["summary"] = hi.get("summary_zh") or ""
            if hi.get("score") is not None:
                entry["score"] = hi["score"]
            if hi.get("key_techniques"):
                entry["key_techniques"] = hi["key_techniques"]
            if hi.get("venue"):
                entry["venue"] = hi["venue"]
        out.append(entry)
    # Stable order: newest date first (the page regroups anyway).
    out.sort(key=lambda e: (e.get("date") or "", e.get("paper_id") or ""),
             reverse=True)
    return out


def _write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def main() -> int:
    if not os.environ.get("GIST_TOKEN", "").strip():
        print("GIST_TOKEN not set — nothing to publish.", file=sys.stderr)
        return 1

    try:
        state, gist_id = gist_state.fetch_state()
    except gist_state.GistAuthError as e:
        # The recurring failure mode: the classic PAT expired. Say so plainly so
        # the Actions failure email points straight at the fix.
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    if not gist_id:
        print("No state gist found on this account.", file=sys.stderr)
        return 1

    health = gist_state.token_health()
    if health["ok"] and health["days_left"] is not None \
            and health["days_left"] <= gist_state.WARN_WITHIN_DAYS:
        print(f"::warning::GIST_TOKEN 将在 {health['days_left']} 天后"
              f"（{health['expires'][:10]}）过期，请尽快重签。")

    public = build_public(state, _load_highlights())
    _write_atomic(OUT_PATH, json.dumps(public, ensure_ascii=False, indent=2))
    print(f"Wrote {len(public)} favorites → {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
