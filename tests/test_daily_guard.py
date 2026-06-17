"""The daily re-run guard: an existing report must not be clobbered by a re-run
(the seen-set would strip the day's papers and re-render a near-empty page).
No network / LLM — _collect_papers is stubbed to explode if the guard lets the
run proceed."""
from __future__ import annotations

from datetime import date

import pytest

from research_news import daily


def _stub_config(monkeypatch):
    monkeypatch.setattr(daily, "_load_config", lambda: ({}, "interests text"))
    monkeypatch.setattr(daily, "_parse_thresholds", lambda t: (4.0, 8.0, 6.0))

    def _boom(*a, **k):
        raise AssertionError("daily proceeded past the re-run guard")

    monkeypatch.setattr(daily, "_collect_papers", _boom)


def test_existing_report_is_not_clobbered(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    page = tmp_path / "2026-06-17.md"
    page.write_text("FULL REPORT", encoding="utf-8")
    _stub_config(monkeypatch)

    out = daily.run(for_date=date(2026, 6, 17))          # not forced
    assert out == page
    assert page.read_text(encoding="utf-8") == "FULL REPORT"  # left untouched


def test_force_bypasses_the_guard(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)
    (tmp_path / "2026-06-17.md").write_text("FULL REPORT", encoding="utf-8")
    _stub_config(monkeypatch)

    # --force must NOT short-circuit → it proceeds to fetch (our boom fires).
    with pytest.raises(AssertionError, match="past the re-run guard"):
        daily.run(for_date=date(2026, 6, 17), force=True)


def test_missing_report_proceeds(tmp_path, monkeypatch):
    monkeypatch.setattr(daily, "DOCS_DIR", tmp_path)     # empty dir → no report
    _stub_config(monkeypatch)

    with pytest.raises(AssertionError, match="past the re-run guard"):
        daily.run(for_date=date(2026, 6, 17))
