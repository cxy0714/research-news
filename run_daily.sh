#!/usr/bin/env bash
# Example wrapper for cron. Adjust paths to match your environment.
set -euo pipefail

cd "$(dirname "$0")"

# Activate venv if you use one:
# source .venv/bin/activate

python -m research_news.daily

# Commit and push the new daily report.
if [[ -n "$(git status --porcelain docs/)" ]]; then
  git add docs/ data/
  git commit -m "daily report $(date -I)"
  git push
fi

# Crontab example (run every weekday at 07:30):
#   30 7 * * 1-5 /path/to/research-news/run_daily.sh >> /tmp/research-news.log 2>&1
