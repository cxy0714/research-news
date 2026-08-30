#!/usr/bin/env bash
# One-off backfill for 2026-08-24 .. 2026-08-28.
#
# Three independent failures were hit and worked around:
#  1. daily cron fired while Clash/VPN was down -> arXiv/OpenAlex (routed through
#     127.0.0.1:7897 by netenv.py) got WinError 10061. Fix: bypass the dead proxy
#     (PROXY_URL empty + NO_PROXY=*) and go direct.
#  2. deep reads (reasoner, up to 24k tokens) timed out on a congested SJTU
#     gateway. Fix: raise per-call timeout to 10 min, cap attempts at 2.
#  3. repeated --force runs tripped arXiv's 429 rate limit. Fix: 08-24 is already
#     rendered (168KB) so we DON'T re-scrape it (only backfill its deep reads);
#     re-scrape only 08-25..28 with a gentler 5s request interval, after a cooldown.
set -uo pipefail
cd "$(dirname "$0")/.."

export PROXY_URL=              # disable Clash proxy: setup_proxy() no-ops
export NO_PROXY='*'           # bypass Windows registry proxy too
export no_proxy='*'
export SJTU_TIMEOUT=600       # 10 min/deep-read call (default 300)
export SJTU_MAX_ATTEMPTS=2    # cap wasted time on stuck deep-read calls
export ARXIV_MIN_INTERVAL=5   # gentler arXiv spacing (default 3) to avoid 429

echo "=== cooldown 20 min for arXiv 429 to clear $(date -Iseconds) ==="
sleep 1200

# 08-24: report already complete; only retry its failed deep reads (no re-scrape).
echo "=================== 2026-08-24 deep-read backfill $(date -Iseconds) ==================="
python -m research_news.backfill_deep_reads --retry-stubs --date 2026-08-24

# 08-25..28: full generate (currently empty 255B placeholders, safe to (re)render).
for d in 2026-08-25 2026-08-26 2026-08-27 2026-08-28; do
  echo "=================== $d START $(date -Iseconds) ==================="
  python -m research_news.daily --date "$d" --force
  python -m research_news.rerun --date "$d"
  python -m research_news.backfill_deep_reads --retry-stubs --date "$d"
  echo "=================== $d DONE ($(wc -c < docs/daily/$d.md) bytes) $(date -Iseconds) ==================="
done
echo "ALL BACKFILL COMPLETE $(date -Iseconds)"
