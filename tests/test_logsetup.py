"""host_tag() must yield a short, filesystem-safe, non-empty hostname so logs
from different machines don't collide under logs/."""
from __future__ import annotations

import re

from research_news import logsetup


def test_host_tag_is_filesystem_safe_and_nonempty(monkeypatch):
    monkeypatch.setattr(logsetup.socket, "gethostname", lambda: "Cloud Server #1 (prod)!")
    tag = logsetup.host_tag()
    assert tag and re.fullmatch(r"[a-z0-9._-]+", tag)   # safe chars only, lowercase
    assert " " not in tag and "/" not in tag


def test_host_tag_falls_back_when_blank(monkeypatch):
    monkeypatch.setattr(logsetup.socket, "gethostname", lambda: "")
    assert logsetup.host_tag() == "host"


def test_host_tag_survives_lookup_error(monkeypatch):
    def _boom():
        raise OSError("no hostname")
    monkeypatch.setattr(logsetup.socket, "gethostname", _boom)
    assert logsetup.host_tag() == "host"


def test_two_hosts_give_distinct_log_names(monkeypatch):
    from datetime import date
    names = []
    for h in ("cloud-prod", "DESKTOP-ABC"):
        monkeypatch.setattr(logsetup.socket, "gethostname", lambda h=h: h)
        names.append(f"{date(2026, 6, 17).isoformat()}-{logsetup.host_tag()}.log")
    assert names[0] != names[1]
    assert names == ["2026-06-17-cloud-prod.log", "2026-06-17-desktop-abc.log"]
