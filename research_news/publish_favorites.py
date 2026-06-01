"""Publish a public, read-only snapshot of the personal favorites collection.

The interactive site stores favorites (and read state, and per-paper comments)
in a *private* GitHub Gist that only the signed-in owner can see. This script
is meant to run on a schedule (GitHub Actions): it reads that gist with a token,
joins each favorite against the repo's existing ``data/highlights.json`` to pull
in the Chinese summary / score / key techniques (so the gist itself stays tiny),
and writes ``docs/data/favorites_public.json``. The favorites page then renders
that snapshot for visitors who are not signed in.

Only favorites are published — read state is never exposed. Per the owner's
choice, comments ARE included in the public snapshot.

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

import httpx

GH_API = "https://api.github.com"
STATE_FILE = "research-news-state.json"
GIST_DESC = "research-news · 已读与收藏状态（请勿删除）"

HIGHLIGHTS_PATH = Path("data/highlights.json")
OUT_PATH = Path("docs/data/favorites_public.json")

# Fields copied from the highlights manifest into each published entry.
ENRICH_FIELDS = ("summary_zh", "score", "key_techniques", "why_relevant",
                 "venue", "authors")


def _headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _find_gist_id(client: httpx.Client, token: str) -> str | None:
    r = client.get(f"{GH_API}/gists", headers=_headers(token),
                   params={"per_page": 100})
    r.raise_for_status()
    for g in r.json():
        files = g.get("files") or {}
        if g.get("description") == GIST_DESC or STATE_FILE in files:
            return g["id"]
    return None


def _load_state(client: httpx.Client, token: str, gist_id: str) -> dict:
    r = client.get(f"{GH_API}/gists/{gist_id}", headers=_headers(token))
    r.raise_for_status()
    g = r.json()
    f = (g.get("files") or {}).get(STATE_FILE)
    if not f:
        return {}
    # Files >1 MB come back truncated; fetch the raw blob in that case.
    if f.get("truncated") and f.get("raw_url"):
        raw = client.get(f["raw_url"], headers=_headers(token))
        raw.raise_for_status()
        return json.loads(raw.text or "{}")
    return json.loads(f.get("content") or "{}")


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
    token = os.environ.get("GIST_TOKEN", "").strip()
    if not token:
        print("GIST_TOKEN not set — nothing to publish.", file=sys.stderr)
        return 1

    with httpx.Client(timeout=30) as client:
        gist_id = os.environ.get("RN_GIST_ID", "").strip() or \
            _find_gist_id(client, token)
        if not gist_id:
            print("No state gist found on this account.", file=sys.stderr)
            return 1
        state = _load_state(client, token, gist_id)

    public = build_public(state, _load_highlights())
    _write_atomic(OUT_PATH, json.dumps(public, ensure_ascii=False, indent=2))
    print(f"Wrote {len(public)} favorites → {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
