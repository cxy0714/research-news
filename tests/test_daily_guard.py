"""The daily re-run guard: an existing report must not be clobbered by a re-run
(the seen-set would strip the day's papers and re-render a near-empty page).
No network / LLM — _collect_papers is stubbed to explode if the guard lets the
run proceed."""
from __future__ import annotations

import sys
from datetime import date

import pytest

from research_news import daily


def _stub_config(monkeypatch):
    monkeypatch.setattr(daily, "_load_config", lambda: ({}, "interests text"))
    monkeypatch.setattr(daily, "_parse_thresholds", lambda t: (4.0, 8.0, 6.0))

    def _boom(*a, **k):
        raise AssertionError("daily proceeded past the re-run guard")

    monkeypatch.setattr(daily, "_collect_papers", _boom)


# A real report contains at least one scored paper ("相关性 N/10"); the guard
# uses that to tell a real report from an empty one.
_REAL = "# 2026-06-17\n\n#### 1. [x](u) — t\n- 相关性 8/10\n"


def test_existing_report_is_not_clobbered(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    page = tmp_path / "2026-06-17.md"
    page.write_text(_REAL, encoding="utf-8")
    _stub_config(monkeypatch)

    out = daily.run(for_date=date(2026, 6, 17))          # not forced
    assert out == page
    assert page.read_text(encoding="utf-8") == _REAL     # left untouched


def test_empty_report_is_regenerated(tmp_path, monkeypatch):
    # An empty report (no papers — e.g. arXiv RSS was lagging) must NOT block a
    # re-run: the guard lets it through to re-fetch (our boom fires).
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    (tmp_path / "2026-06-17.md").write_text(
        "# 2026-06-17 每日 arXiv 资讯\n\n- 高相关论文 0 篇 · 中相关 0 篇 · 会议/Seminar 事件 0 条\n",
        encoding="utf-8",
    )
    _stub_config(monkeypatch)

    with pytest.raises(AssertionError, match="past the re-run guard"):
        daily.run(for_date=date(2026, 6, 17))


def test_force_bypasses_the_guard(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    (tmp_path / "2026-06-17.md").write_text(_REAL, encoding="utf-8")
    _stub_config(monkeypatch)

    # --force must NOT short-circuit → it proceeds to fetch (our boom fires).
    with pytest.raises(AssertionError, match="past the re-run guard"):
        daily.run(for_date=date(2026, 6, 17), force=True)


def test_replace_bypasses_the_guard(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    (tmp_path / "2026-06-17.md").write_text(_REAL, encoding="utf-8")
    _stub_config(monkeypatch)

    with pytest.raises(AssertionError, match="past the re-run guard"):
        daily.run(for_date=date(2026, 6, 17), replace=True)


def test_missing_report_proceeds(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)     # empty dir → no report
    _stub_config(monkeypatch)

    with pytest.raises(AssertionError, match="past the re-run guard"):
        daily.run(for_date=date(2026, 6, 17))


# ── outage guard ─────────────────────────────────────────────────────────────
# A zero-paper run must not be published when the sources were unreachable
# (dead proxy → WinError 10061 on every scraper); it has to abort instead so the
# day stays re-runnable. A genuinely quiet day (arXiv answers, nothing new)
# still renders, and --allow-empty overrides the abort.

def _stub_empty_collection(monkeypatch, *, reachable: bool):
    monkeypatch.setattr(daily, "_load_config", lambda: ({}, "interests text"))
    monkeypatch.setattr(daily, "_parse_thresholds", lambda t: (4.0, 8.0, 6.0))
    monkeypatch.setattr(daily, "_collect_papers", lambda *a, **k: [])
    monkeypatch.setattr(daily, "_probe_arxiv", lambda: reachable)


def test_outage_refuses_to_render(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    _stub_empty_collection(monkeypatch, reachable=False)

    with pytest.raises(daily.SourceOutage):
        daily.run(for_date=date(2026, 6, 17))
    assert not (tmp_path / "2026-06-17.md").exists()   # nothing written


def test_quiet_day_still_renders(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    _stub_empty_collection(monkeypatch, reachable=True)
    # Reaching the LLM client proves the guard let the quiet day through.
    monkeypatch.setattr(
        daily, "SJTUClient",
        lambda: (_ for _ in ()).throw(AssertionError("proceeded past outage guard")),
    )

    with pytest.raises(AssertionError, match="proceeded past outage guard"):
        daily.run(for_date=date(2026, 6, 17))


def test_allow_empty_overrides_outage(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    _stub_empty_collection(monkeypatch, reachable=False)
    monkeypatch.setattr(
        daily, "SJTUClient",
        lambda: (_ for _ in ()).throw(AssertionError("proceeded past outage guard")),
    )

    with pytest.raises(AssertionError, match="proceeded past outage guard"):
        daily.run(for_date=date(2026, 6, 17), allow_empty=True)


def test_cli_exits_2_on_outage(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    _stub_empty_collection(monkeypatch, reachable=False)
    monkeypatch.setattr(daily, "_setup_logging", lambda: None)
    monkeypatch.setattr(sys, "argv", ["daily", "--date", "2026-06-17"])

    with pytest.raises(SystemExit) as exc:
        daily.main()
    assert exc.value.code == 2
