#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

# ── Mutual-exclusion: bail if another instance is still running ──
LOCKDIR=/tmp/research-news-daily.lock
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  echo "[$(date -Iseconds)] Another instance is running (lockdir=$LOCKDIR). Exiting." >&2
  exit 1
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT

# Activate venv if you use one:
# source .venv/bin/activate

python -m research_news.daily

# Re-run any summaries that came out garbled / truncated. Uses the LLM for
# blocks whose prose was cut off, and salvages clean prose for the rest.
python -m research_news.rerun --date "$(date -I)"

# Commit and push all changes.
git add -A
if [[ -n "$(git status --porcelain)" ]]; then
  git commit -m "daily report $(date -I)"
  git push
fi

# Crontab example (run every weekday at 07:30):
#   30 7 * * 1-5 /path/to/research-news/run_daily.sh >> /tmp/research-news.log 2>&1
