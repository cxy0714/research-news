"""Offline tests for GIST_TOKEN health / auth-error handling (no network).

The recurring failure this covers: the classic PAT behind GIST_TOKEN expires
(90 days by default) and both consumers — the nightly publish-favorites
workflow and the daily manual_requests step — go silent at the same time. These
tests pin the behaviour that makes that loud: a dedicated GistAuthError instead
of a generic network warning, and an expiry pre-warning.
"""
from __future__ import annotations

import logging

import httpx
import pytest

from research_news import gist_state


def _client(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


# ── auth failures are their own error class ────────────────────────────────────

@pytest.mark.parametrize("code", [401, 403])
def test_find_gist_id_raises_auth_error(code):
    with _client(lambda r: httpx.Response(code, json={"message": "Bad credentials"})) as c:
        with pytest.raises(gist_state.GistAuthError) as ei:
            gist_state.find_gist_id(c, "dead-token")
    assert str(code) in str(ei.value)
    assert "settings/tokens" in str(ei.value)   # message carries the fix


def test_load_state_raises_auth_error():
    with _client(lambda r: httpx.Response(401, json={"message": "Bad credentials"})) as c:
        with pytest.raises(gist_state.GistAuthError):
            gist_state.load_state(c, "dead-token", "abc123")


def test_non_auth_http_error_is_not_auth_error():
    """A 500 must stay a plain HTTP error, so real outages aren't misreported
    as an expired token."""
    with _client(lambda r: httpx.Response(500, text="boom")) as c:
        with pytest.raises(httpx.HTTPStatusError):
            gist_state.find_gist_id(c, "tok")


def test_success_path_still_works():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/gists":
            return httpx.Response(200, json=[
                {"id": "g1", "description": "unrelated", "files": {}},
                {"id": "g2", "description": gist_state.GIST_DESC, "files": {}},
            ])
        return httpx.Response(200, json={
            "files": {gist_state.STATE_FILE: {"content": '{"favorites": {"x": {}}}'}}
        })

    with _client(handler) as c:
        assert gist_state.find_gist_id(c, "tok") == "g2"
        assert gist_state.load_state(c, "tok", "g2") == {"favorites": {"x": {}}}


# ── token_health ──────────────────────────────────────────────────────────────

def _patch_client(monkeypatch, handler):
    """Make gist_state's httpx.Client use a mock transport."""
    real = httpx.Client

    def factory(*a, **kw):
        kw.pop("timeout", None)
        return real(transport=httpx.MockTransport(handler))

    monkeypatch.setattr(gist_state.httpx, "Client", factory)


def test_token_health_no_token(monkeypatch):
    monkeypatch.delenv("GIST_TOKEN", raising=False)
    h = gist_state.token_health()
    assert h["ok"] is False
    assert "未配置" in h["detail"]


def test_token_health_expired(monkeypatch):
    _patch_client(monkeypatch, lambda r: httpx.Response(401, json={"message": "Bad credentials"}))
    h = gist_state.token_health("dead")
    assert h["ok"] is False
    assert "401" in h["detail"]


def test_token_health_reports_days_left(monkeypatch):
    from datetime import date, timedelta
    exp = (date.today() + timedelta(days=9)).isoformat()
    _patch_client(monkeypatch, lambda r: httpx.Response(
        200, json={"login": "cxy0714"},
        headers={"github-authentication-token-expiration": f"{exp} 12:00:00 UTC",
                 "x-oauth-scopes": "gist, public_repo"}))
    h = gist_state.token_health("live")
    assert h["ok"] is True
    assert h["days_left"] == 9
    assert h["expires"].startswith(exp)
    assert h["scopes"] == "gist, public_repo"


def test_token_health_no_expiry_header(monkeypatch):
    _patch_client(monkeypatch, lambda r: httpx.Response(
        200, json={"login": "cxy0714"}, headers={"x-oauth-scopes": "gist"}))
    h = gist_state.token_health("live")
    assert h["ok"] is True
    assert h["expires"] is None
    assert h["days_left"] is None
    assert "无过期时间" in h["detail"]


def test_token_health_network_error_is_not_a_dead_token(monkeypatch):
    def boom(request):
        raise httpx.ConnectError("refused")

    _patch_client(monkeypatch, boom)
    h = gist_state.token_health("live")
    assert h["ok"] is False
    assert "无法连接" in h["detail"]     # distinct from the expiry message


# ── warn_if_expiring ──────────────────────────────────────────────────────────

class _Rec(logging.Handler):
    def __init__(self):
        super().__init__()
        self.msgs: list[str] = []

    def emit(self, record):
        self.msgs.append(record.getMessage())


def _logger_with_recorder(name):
    log = logging.getLogger(name)
    log.handlers.clear()
    rec = _Rec()
    log.addHandler(rec)
    log.setLevel(logging.INFO)
    log.propagate = False
    return log, rec


def test_warn_if_expiring_warns_inside_window(monkeypatch):
    from datetime import date, timedelta
    exp = (date.today() + timedelta(days=3)).isoformat()
    _patch_client(monkeypatch, lambda r: httpx.Response(
        200, json={"login": "u"},
        headers={"github-authentication-token-expiration": f"{exp} 00:00:00 UTC",
                 "x-oauth-scopes": "gist"}))
    log, rec = _logger_with_recorder("t.warn.inside")
    gist_state.warn_if_expiring(log, "live")
    assert any("3 天后" in m for m in rec.msgs)


def test_warn_if_expiring_quiet_when_healthy(monkeypatch):
    from datetime import date, timedelta
    exp = (date.today() + timedelta(days=200)).isoformat()
    _patch_client(monkeypatch, lambda r: httpx.Response(
        200, json={"login": "u"},
        headers={"github-authentication-token-expiration": f"{exp} 00:00:00 UTC",
                 "x-oauth-scopes": "gist, public_repo"}))
    log, rec = _logger_with_recorder("t.warn.quiet")
    gist_state.warn_if_expiring(log, "live")
    assert rec.msgs == []


def test_warn_if_expiring_flags_missing_scope(monkeypatch):
    _patch_client(monkeypatch, lambda r: httpx.Response(
        200, json={"login": "u"}, headers={"x-oauth-scopes": "public_repo"}))
    log, rec = _logger_with_recorder("t.warn.scope")
    gist_state.warn_if_expiring(log, "live")
    assert any("gist` scope" in m for m in rec.msgs)


def test_warn_if_expiring_silent_on_empty_scopes(monkeypatch):
    """Fine-grained PATs don't report scopes — don't cry wolf."""
    _patch_client(monkeypatch, lambda r: httpx.Response(200, json={"login": "u"}))
    log, rec = _logger_with_recorder("t.warn.fg")
    gist_state.warn_if_expiring(log, "live")
    assert rec.msgs == []


# ── callers surface the auth error ────────────────────────────────────────────

def test_manual_requests_fails_open_but_logs_error(monkeypatch, caplog):
    from research_news import manual_requests as mr

    monkeypatch.setenv("GIST_TOKEN", "dead")
    monkeypatch.setattr(mr.gist_state, "fetch_state",
                        lambda: (_ for _ in ()).throw(gist_state.GistAuthError("过期了")))
    with caplog.at_level(logging.ERROR, logger="research_news.manual"):
        assert mr.run(dry_run=True) == 0        # never breaks the daily commit
    assert any(r.levelno == logging.ERROR and "过期了" in r.getMessage()
               for r in caplog.records)


def test_publish_favorites_exits_nonzero_on_auth_error(monkeypatch, capsys):
    from research_news import publish_favorites as pf

    monkeypatch.setenv("GIST_TOKEN", "dead")
    monkeypatch.setattr(pf.gist_state, "fetch_state",
                        lambda: (_ for _ in ()).throw(gist_state.GistAuthError("过期了")))
    assert pf.main() == 1                       # CI must go red
    assert "过期了" in capsys.readouterr().err
