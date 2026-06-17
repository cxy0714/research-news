#!/usr/bin/env bash
# Server entry point for the daily cron (point cron at this, or symlink it from
# /root/run_rn.sh). It sets up the environment, syncs with the remote, then
# delegates to run_daily.sh — which holds the actual pipeline, the run lock, and
# the commit/push. Keeping the real logic in run_daily.sh (version-controlled)
# means this thin wrapper rarely has to change.
#
#   Crontab (weekday 09:10) — use ONE executor only:
#     10 9 * * 1-5 /root/research-news/run_rn.sh >> /root/rn.log 2>&1
set -euo pipefail

# Path to the cloned repo. Defaults to this script's own directory (keep
# run_rn.sh inside the repo); override with RN_REPO=/path if you put it elsewhere
# (e.g. a copy at /root/run_rn.sh → set RN_REPO=/root/research-news).
REPO="${RN_REPO:-$(cd "$(dirname "$0")" && pwd)}"
cd "$REPO"

# Activate the virtualenv so `python` sees the installed package + deps.
# Adjust to your setup (venv / conda / system python); comment out if unused.
if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

# Pull anything merged via the web / agent since the last run, so the commit +
# push at the end of run_daily.sh fast-forwards cleanly instead of being
# rejected. Best-effort: warn and carry on (the report still gets generated;
# you can reconcile the push by hand if needed). --autostash tolerates a stray
# uncommitted file (e.g. a half-written log) without aborting.
git pull --rebase --autostash \
  || echo "[$(date -Iseconds)] WARN: git pull failed; end-of-run push may need manual sync" >&2

# SJTU_API_KEY etc. live in .env and are loaded by the Python code (python-dotenv).
# Export any extra per-run overrides here if you want, e.g.:
# export DEEP_READ_MODEL=deepseek-reasoner

# Hand off to the pipeline wrapper (daily → rerun → retry failed deep reads →
# commit/push), which takes the single-run lock.
exec ./run_daily.sh
