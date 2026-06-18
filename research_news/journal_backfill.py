"""Drive the journal back-catalog backfill one unit at a time, unattended.

Reads the queue in ``ops/journal-backfill.md`` (the markdown checklist), runs the
next unchecked ``- [ ]`` unit through ``research_news.journals`` in a fresh
subprocess, and ticks it off on success. Dedup makes each unit resumable, and
the weekly token quota dwarfs a unit, so the throttle is simply "N units per
scheduled run" (default 1) plus the shared run lock (held by the wrapper script)
so it never overlaps the daily run.

    python -m research_news.journal_backfill            # do the next 1 unit
    python -m research_news.journal_backfill --max 3    # up to 3 units this run
    python -m research_news.journal_backfill --dry-run  # show what's next, run nothing
"""
from __future__ import annotations

import argparse
import logging
import re
import shlex
import subprocess
import sys
from datetime import date
from pathlib import Path

log = logging.getLogger("research_news.journal_backfill")

QUEUE_PATH = Path("ops/journal-backfill.md")
# A queue line: "- [ ] `--only AoP --n-issues 8`   ⚠ optional note"
_ITEM_RE = re.compile(r"^(\s*-\s*)\[ \](\s*)`([^`]+)`(.*)$")


def pending_units(lines: list[str]) -> list[tuple[int, str]]:
    """(line_index, args_string) for each unchecked ``- [ ] `…` `` item, in order."""
    out: list[tuple[int, str]] = []
    for i, ln in enumerate(lines):
        m = _ITEM_RE.match(ln)
        if m:
            out.append((i, m.group(3).strip()))
    return out


def mark_done(line: str, when: date) -> str:
    """``- [ ] `cmd` …`` → ``- [x] (date) `cmd` …`` (other lines unchanged)."""
    m = _ITEM_RE.match(line)
    if not m:
        return line
    prefix, gap, cmd, tail = m.groups()
    return f"{prefix}[x] ({when.isoformat()}){gap}`{cmd}`{tail}"


def run(*, max_units: int = 1, dry_run: bool = False,
        queue_path: Path = QUEUE_PATH) -> int:
    """Do up to ``max_units`` queue units. Returns the number done."""
    if not queue_path.exists():
        log.error("journal backfill queue not found: %s", queue_path)
        return 0
    lines = queue_path.read_text(encoding="utf-8").split("\n")
    pending = pending_units(lines)
    if not pending:
        log.info("journal backfill queue is empty — all units done")
        return 0
    log.info("%d unit(s) left in the queue; doing up to %d this run",
             len(pending), max_units)

    done = 0
    for idx, args in pending[:max_units]:
        log.info("next unit: research_news.journals %s", args)
        if dry_run:
            done += 1
            continue
        try:
            argv = shlex.split(args)
        except ValueError as e:
            log.error("unit %r: cannot parse args (%s) — leaving unchecked", args, e)
            continue
        # Fresh subprocess per unit: clean logging/state, and one unit failing
        # can't take down the others.
        proc = subprocess.run([sys.executable, "-m", "research_news.journals", *argv])
        if proc.returncode != 0:
            log.error("unit %r exited %d — leaving unchecked", args, proc.returncode)
            continue
        lines[idx] = mark_done(lines[idx], date.today())
        queue_path.write_text("\n".join(lines), encoding="utf-8")
        done += 1
        log.info("ticked off: %s", args)

    log.info("%s %d unit(s)", "would do" if dry_run else "did", done)
    return done


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ap = argparse.ArgumentParser(
        description="Run the next journal back-catalog backfill unit(s) from "
        "ops/journal-backfill.md and tick them off."
    )
    ap.add_argument("--max", type=int, default=1, dest="max_units",
                    help="how many queue units to do this run (default 1)")
    ap.add_argument("--dry-run", action="store_true",
                    help="show the next unit(s) without running journals")
    args = ap.parse_args()
    run(max_units=args.max_units, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
