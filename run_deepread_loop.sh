#!/usr/bin/env bash
# Resident deep-read loop (Linux/macOS counterpart of run_deepread_loop.ps1) —
# one paper per lock hold, back to back, until nothing is pending. Priority inside
# `backfill_deep_reads --pending`: data/highlights.json backlog (papers daily
# selected but never deep-read — incl. green-lit / popsci ones) -> failed stubs
# past their cooldown -> score-threshold leftovers.
#
# daily defers its deep reads here (DAILY_DEFER_DEEP_READS=1), so a 50+ paper day
# no longer stretches the daily run for hours. It takes the same flock as
# run_daily.sh, so the loop and daily never overlap; it exits on its own when the
# queue is empty (unit exits 7). Run it from cron/systemd at logon/boot, e.g.:
#
#   @reboot  cd /root/research-news && ./run_deepread_loop.sh >> /root/rn-deepread.log 2>&1
#
#   ./run_deepread_loop.sh            # grind until nothing is pending
set -uo pipefail
cd "$(dirname "$0")"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

git pull --rebase --autostash \
  || echo "[$(date -Iseconds)] WARN: git pull failed; push may need manual sync" >&2

commit_and_push() {
  [[ -z "$(git status --porcelain)" ]] && return 0
  git add -A
  git commit -m "deep reads $(date -I)" || return 0
  git push || { git pull --rebase --autostash && git push; }
}

echo "[$(date -Iseconds)] deep-read loop start"
done_units=0
while true; do
  # One unit = one paper. flock -w waits up to 60 min behind a running daily.
  flock -w 3600 "${TMPDIR:-/tmp}/research-news-daily.lock" \
    python -m research_news.backfill_deep_reads --pending --limit 1
  code=$?
  if [[ $code -eq 7 ]]; then
    echo "[$(date -Iseconds)] nothing pending - stopping"
    break
  fi
  if [[ $code -ne 0 ]]; then
    echo "[$(date -Iseconds)] unit failed (exit $code) - stopping"
    break
  fi
  done_units=$((done_units + 1))
  if (( done_units % 5 == 0 )); then
    commit_and_push
  fi
  sleep 10
done
(( done_units % 5 != 0 )) && commit_and_push
echo "[$(date -Iseconds)] deep-read loop done ($done_units unit(s) this run)"
