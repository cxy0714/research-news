#!/usr/bin/env bash
# Paced journal back-catalog backfill — ONE unit at a time, never in parallel
# with the daily run or another backfill (it takes the same flock as
# run_daily.sh). Pass the journals.py args for a single unit, e.g.:
#
#   ./run_journal_backfill.sh --only AoS --n-issues 12
#   ./run_journal_backfill.sh --only JMLR --jmlr-n 3
#   ./run_journal_backfill.sh --only-group prob_stats --n-issues 8
#
# Dedup (data/seen_papers.json) means already-processed issues are skipped, so a
# unit is naturally resumable and re-running a finished unit produces no commit.
# See ops/journal-backfill.md for the queue + the procedure an agent should follow.
set -euo pipefail
cd "$(dirname "$0")"

if [[ $# -eq 0 ]]; then
  echo "usage: $0 <journals.py args>   e.g. --only AoS --n-issues 12" >&2
  exit 2
fi

# Activate the virtualenv so `python` sees the package (same probe as run_rn.sh).
if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

# Sync first so the commit/push at the end fast-forwards (changes may have been
# merged via the web/agent). Best-effort.
git pull --rebase --autostash \
  || echo "[$(date -Iseconds)] WARN: git pull failed; push may need manual sync" >&2

# Same lock as run_daily.sh → daily and backfill (and two backfills) never overlap.
# If something else holds it, bail cleanly; the caller can retry later.
exec 9>"${TMPDIR:-/tmp}/research-news-daily.lock"
if ! flock -n 9; then
  echo "[$(date -Iseconds)] daily or another backfill is already running — try later" >&2
  exit 0
fi

echo "[$(date -Iseconds)] journal backfill start: research_news.journals $*"
python -m research_news.journals "$@"
echo "[$(date -Iseconds)] journal backfill done: $*"

# Commit + push. Nothing changed (e.g. a unit already fully covered) → no commit.
if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "journal backfill: $* ($(date -I))"
  # If the push is rejected (remote moved on), rebase onto it and retry once.
  git push || { git pull --rebase --autostash && git push; }
else
  echo "[$(date -Iseconds)] no new pages — unit already covered, nothing to commit"
fi
