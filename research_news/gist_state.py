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


class GistAuthError(RuntimeError):
    """GIST_TOKEN is missing, expired, or lacks the ``gist`` scope.

    Split out from generic network errors because it is a *recurring* failure:
    a classic PAT expires (90 days by default) and both the nightly
    publish-favorites workflow and the local manual-queue step go silent at the
    same time. See README「GIST_TOKEN 过期（周期性故障）」.
    """


_AUTH_HINT = (
    "GIST_TOKEN 无效 / 已过期 / 缺少 `gist` scope（GitHub 返回 {code}）。"
    "去 https://github.com/settings/tokens 重新签发 classic PAT"
    "（勾选 gist + public_repo，有效期建议 No expiration），然后同时更新"
    "仓库 secret GIST_TOKEN 和本机 .env。"
)


def _check(r: httpx.Response) -> httpx.Response:
    """Raise :class:`GistAuthError` on an auth failure, else the usual HTTP error."""
    if r.status_code in (401, 403):
        raise GistAuthError(_AUTH_HINT.format(code=f"{r.status_code} {r.reason_phrase}"))
    r.raise_for_status()
    return r


def headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def find_gist_id(client: httpx.Client, token: str) -> str | None:
    """Discover the state gist on the token's account by description / filename."""
    r = client.get(f"{GH_API}/gists", headers=headers(token), params={"per_page": 100})
    _check(r)
    for g in r.json():
        files = g.get("files") or {}
        if g.get("description") == GIST_DESC or STATE_FILE in files:
            return g["id"]
    return None


def load_state(client: httpx.Client, token: str, gist_id: str) -> dict:
    """Return the parsed state object from the gist (``{}`` if the file is empty)."""
    r = client.get(f"{GH_API}/gists/{gist_id}", headers=headers(token))
    _check(r)
    g = r.json()
    f = (g.get("files") or {}).get(STATE_FILE)
    if not f:
        return {}
    # Files >1 MB come back truncated; fetch the raw blob in that case.
    if f.get("truncated") and f.get("raw_url"):
        raw = client.get(f["raw_url"], headers=headers(token))
        _check(raw)
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


# ── token health (expiry pre-warning) ─────────────────────────────────────────
# A classic PAT defaults to a 90-day life, and when it dies EVERYTHING that
# reads the gist dies with it — silently, because both callers fail open. So we
# surface the expiry date GitHub reports and warn while there's still time to
# rotate.

WARN_WITHIN_DAYS = 14


def token_health(token: str | None = None, *, timeout: float = 30) -> dict:
    """Probe ``GIST_TOKEN`` against ``/user``.

    Returns ``{"ok": bool, "login": str, "scopes": str, "expires": str|None,
    "days_left": int|None, "detail": str}``. Never raises: a dead token is a
    result (``ok=False``), not an exception, so callers can warn and move on.
    """
    token = (token or os.environ.get("GIST_TOKEN", "")).strip()
    if not token:
        return {"ok": False, "login": "", "scopes": "", "expires": None,
                "days_left": None, "detail": "GIST_TOKEN 未配置"}
    try:
        with httpx.Client(timeout=timeout) as client:
            r = client.get(f"{GH_API}/user", headers=headers(token))
    except Exception as e:  # noqa: BLE001 — network trouble is not a dead token
        return {"ok": False, "login": "", "scopes": "", "expires": None,
                "days_left": None, "detail": f"无法连接 GitHub API：{e}"}

    if r.status_code in (401, 403):
        return {"ok": False, "login": "", "scopes": "", "expires": None,
                "days_left": None,
                "detail": _AUTH_HINT.format(code=f"{r.status_code} {r.reason_phrase}")}
    if r.status_code >= 400:
        return {"ok": False, "login": "", "scopes": "", "expires": None,
                "days_left": None, "detail": f"GitHub API {r.status_code}"}

    # Classic PATs with an expiry date report it in this header (absent for
    # "No expiration" tokens and for fine-grained PATs on some endpoints).
    expires = r.headers.get("github-authentication-token-expiration") or None
    days_left = None
    if expires:
        try:
            from datetime import date as _date
            days_left = (_date.fromisoformat(expires[:10]) - _date.today()).days
        except Exception:  # noqa: BLE001 — unparseable header, just report raw
            days_left = None

    scopes = r.headers.get("x-oauth-scopes", "")
    detail = f"token 有效（{r.json().get('login', '?')}）"
    if expires:
        detail += f"，{expires[:10]} 过期"
        if days_left is not None:
            detail += f"（还剩 {days_left} 天）"
    else:
        detail += "，无过期时间"
    return {"ok": True, "login": r.json().get("login", ""), "scopes": scopes,
            "expires": expires, "days_left": days_left, "detail": detail}


def warn_if_expiring(log, token: str | None = None) -> dict:
    """Log a WARNING when the token is dead or expires within
    :data:`WARN_WITHIN_DAYS` days. Returns the :func:`token_health` dict."""
    h = token_health(token)
    if not h["ok"]:
        log.warning("GIST_TOKEN 健康检查失败：%s", h["detail"])
    elif h["days_left"] is not None and h["days_left"] <= WARN_WITHIN_DAYS:
        log.warning(
            "GIST_TOKEN 将在 %d 天后（%s）过期 —— 请尽快重签，否则公开收藏快照与"
            "手动录入队列会一起静默失效。", h["days_left"], h["expires"][:10])
    if h["ok"] and "gist" not in (h["scopes"] or ""):
        # Empty scopes header = fine-grained PAT (scopes aren't reported); only
        # warn when the header lists scopes but `gist` isn't among them.
        if h["scopes"]:
            log.warning("GIST_TOKEN 缺少 `gist` scope（当前：%s）", h["scopes"])
    return h


def main() -> int:
    """``python -m research_news.gist_state`` — print token health, exit 1 if dead."""
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    from dotenv import load_dotenv
    load_dotenv()
    h = warn_if_expiring(logging.getLogger("gist_state"))
    print(h["detail"])
    if h["ok"]:
        print(f"scopes: {h['scopes'] or '(fine-grained PAT / 未报告)'}")
    return 0 if h["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
