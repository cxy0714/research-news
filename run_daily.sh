#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

# ── single-run lock ───────────────────────────────────────────────────────────
# Guard against two triggers firing at once (e.g. a system crontab AND an
# OpenClaw/agent cron starting this around the same minute). flock holds the lock
# for the lifetime of this process; the kernel releases it automatically on exit
# — even on kill -9 — so there's no stale lock to clean up by hand.
exec 9>"${TMPDIR:-/tmp}/research-news-daily.lock"
if ! flock -n 9; then
  echo "[$(date -Iseconds)] another run is already in progress — exiting" >&2
  exit 0
fi

# Activate venv if you use one:
# source .venv/bin/activate

python -m research_news.daily

# Re-run any summaries that came out garbled / truncated. Uses the LLM for
# blocks whose prose was cut off, and salvages clean prose for the rest.
python -m research_news.rerun --date "$(date -I)"

# Regenerate any deep reads whose LLM call failed today (the '精读失败' stubs).
# Idempotent: only pages still showing the failure marker are retried.
python -m research_news.backfill_deep_reads --retry-stubs --date "$(date -I)"

# Commit and push all changes (report under docs/, its data/, and the run logs/).
git add -A
if [[ -n "$(git status --porcelain)" ]]; then
  git commit -m "daily report $(date -I)"
  # If the push is rejected (remote moved on), rebase onto it and retry once.
  git push || { git pull --rebase --autostash && git push; }
fi

# Crontab example (run every weekday at 09:10) — use ONE executor only, either
# the system crontab below OR an agent cron, not both (the lock makes a double
# fire safe, but a single trigger is cleaner):
#   10 9 * * 1-5 /path/to/research-news/run_daily.sh >> /tmp/research-news.log 2>&1
