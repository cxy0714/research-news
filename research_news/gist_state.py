"""Read the personal state gist that the browser client writes.

The interactive site stores per-user state — read/favorite/queue maps — in a
single *private* GitHub Gist on the owner's account (file
``research-news-state.json``). A few server-side jobs need to read that gist:

  - ``publish_favorites`` builds the public favorites snapshot from it;
  - ``manual_requests`` reads the deep-read *queue* the owner fills in on the
    web (paste an arXiv link → it lands here) and deep-reads each new paper.

This module centralises locating + reading that gist so both jobs stay in sync
with the browser client's filename / description conventions.

Env:
  GIST_TOKEN   GitHub token with ``gist`` scope (required to read a private gist).
  RN_GIST_ID   Optional gist id; if unset, the gist is discovered by its
               description / state filename, mirroring the browser client.
"""
from __future__ import annotations

import json
import os

import httpx

GH_API = "https://api.github.com"
# Must match docs/javascripts/extras.js (STATE_FILE / GIST_DESC) so all three
# clients — browser, publish_favorites, manual_requests — find the same gist.
STATE_FILE = "research-news-state.json"
GIST_DESC = "research-news · 已读与收藏状态（请勿删除）"


def headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def find_gist_id(client: httpx.Client, token: str) -> str | None:
    """Discover the state gist on the token's account by description / filename."""
    r = client.get(f"{GH_API}/gists", headers=headers(token), params={"per_page": 100})
    r.raise_for_status()
    for g in r.json():
        files = g.get("files") or {}
        if g.get("description") == GIST_DESC or STATE_FILE in files:
            return g["id"]
    return None


def load_state(client: httpx.Client, token: str, gist_id: str) -> dict:
    """Return the parsed state object from the gist (``{}`` if the file is empty)."""
    r = client.get(f"{GH_API}/gists/{gist_id}", headers=headers(token))
    r.raise_for_status()
    g = r.json()
    f = (g.get("files") or {}).get(STATE_FILE)
    if not f:
        return {}
    # Files >1 MB come back truncated; fetch the raw blob in that case.
    if f.get("truncated") and f.get("raw_url"):
        raw = client.get(f["raw_url"], headers=headers(token))
        raw.raise_for_status()
        return json.loads(raw.text or "{}")
    return json.loads(f.get("content") or "{}")


def fetch_state(
    token: str | None = None,
    gist_id: str | None = None,
    *,
    timeout: float = 30,
) -> tuple[dict, str | None]:
    """High-level read: return ``(state, gist_id)``.

    ``token`` / ``gist_id`` default to the GIST_TOKEN / RN_GIST_ID env vars.
    Returns ``({}, None)`` when no token is available or no gist is found, so
    callers can fail open (skip quietly) on machines without a token.
    """
    token = (token or os.environ.get("GIST_TOKEN", "")).strip()
    if not token:
        return {}, None
    gist_id = (gist_id or os.environ.get("RN_GIST_ID", "")).strip()
    with httpx.Client(timeout=timeout) as client:
        if not gist_id:
            gist_id = find_gist_id(client, token)
        if not gist_id:
            return {}, None
        return load_state(client, token, gist_id), gist_id
