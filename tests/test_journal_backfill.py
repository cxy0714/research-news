"""Queue-driven journal backfill: pick the next unchecked unit, tick it off on
success, leave it on failure. The journals subprocess is stubbed (no LLM)."""
from __future__ import annotations

from datetime import date

from research_news import journal_backfill as jb

QUEUE = """# Journal backfill queue

- [ ] `--only AoP --n-issues 8`
- [x] (2026-06-01) `--only AoS --n-issues 12`   already done
- [ ] `--only "Statistica Sinica" --n-issues 8`   ⚠ note
- [ ] `--only JMLR --jmlr-n 3`
some prose, not a unit
"""


def test_pending_units_finds_only_unchecked():
    args = [a for _, a in jb.pending_units(QUEUE.split("\n"))]
    assert args == [
        "--only AoP --n-issues 8",
        '--only "Statistica Sinica" --n-issues 8',
        "--only JMLR --jmlr-n 3",
    ]


def test_mark_done_preserves_command_and_trailing_note():
    line = "- [ ] `--only AoP --n-issues 8`   ⚠ note"
    assert jb.mark_done(line, date(2026, 6, 18)) == \
        "- [x] (2026-06-18) `--only AoP --n-issues 8`   ⚠ note"


def test_dry_run_changes_nothing(tmp_path):
    q = tmp_path / "q.md"
    q.write_text(QUEUE, encoding="utf-8")
    assert jb.run(max_units=2, dry_run=True, queue_path=q) == 2
    assert q.read_text(encoding="utf-8") == QUEUE


def test_run_ticks_off_first_unit_on_success(tmp_path, monkeypatch):
    q = tmp_path / "q.md"
    q.write_text(QUEUE, encoding="utf-8")
    calls = []

    class _Proc:
        returncode = 0

    def _fake_run(argv, *a, **k):
        calls.append(argv)
        return _Proc()

    monkeypatch.setattr(jb.subprocess, "run", _fake_run)
    assert jb.run(max_units=1, queue_path=q) == 1

    assert "--only" in calls[0] and "AoP" in calls[0]      # ran the AoP unit
    txt = q.read_text(encoding="utf-8")
    assert "- [ ] `--only AoP" not in txt                  # AoP now checked
    assert "- [x] (" in txt and "AoP" in txt
    assert '- [ ] `--only "Statistica Sinica"' in txt      # next unit still pending


def test_run_leaves_unit_unchecked_on_failure(tmp_path, monkeypatch):
    q = tmp_path / "q.md"
    q.write_text(QUEUE, encoding="utf-8")

    class _Proc:
        returncode = 2

    monkeypatch.setattr(jb.subprocess, "run", lambda *a, **k: _Proc())
    assert jb.run(max_units=1, queue_path=q) == 0
    assert q.read_text(encoding="utf-8") == QUEUE           # unchanged → still pending
