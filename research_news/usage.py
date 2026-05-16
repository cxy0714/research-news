"""Token usage logging — shared by daily.py and journals.py.

Per-run log goes to data/token_usage.json (append-only list). Also logs
to stdout/file. Used to monitor against the SJTU weekly quota of 1e9 tokens.
"""
from __future__ import annotations

import json
import logging
from datetime import date, timedelta
from pathlib import Path

from .llm.sjtu_client import SJTUClient

log = logging.getLogger(__name__)

USAGE_FILE = Path("data/token_usage.json")
WEEKLY_QUOTA = 1_000_000_000   # SJTU quota: 1e9 tokens/week


def report(client: SJTUClient, pipeline: str, run_date: date | None = None,
           path: Path = USAGE_FILE) -> None:
    """Log per-run token usage to stdout AND append to data/token_usage.json.

    `pipeline` is a short string identifying which pipeline ran (e.g. "daily",
    "journals", "shootout"). `run_date` defaults to today.
    """
    if not client.usage:
        return

    run_date = run_date or date.today()
    total_all = sum(m["total_tokens"] for m in client.usage.values())
    log.info(
        "[%s] token usage: %d calls, %d tokens total across %d model(s)",
        pipeline, client.calls, total_all, len(client.usage),
    )
    for model, u in client.usage.items():
        log.info(
            "  %s: %d prompt + %d completion = %d total",
            model, u["prompt_tokens"], u["completion_tokens"], u["total_tokens"],
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    history: list = []
    if path.exists():
        try:
            history = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(history, list):
                history = []
        except json.JSONDecodeError:
            history = []
    history.append({
        "run_at": date.today().isoformat(),
        "report_date": run_date.isoformat(),
        "pipeline": pipeline,
        "calls": client.calls,
        "by_model": client.usage,
        "total_tokens": total_all,
    })
    path.write_text(json.dumps(history, ensure_ascii=False, indent=2),
                    encoding="utf-8")

    # Rolling 7-day total against the SJTU weekly quota.
    cutoff = (date.today() - timedelta(days=7)).isoformat()
    week_total = sum(h["total_tokens"] for h in history if h["run_at"] >= cutoff)
    log.info(
        "rolling 7-day total: %d / %d tokens (%.2f%% of weekly quota)",
        week_total, WEEKLY_QUOTA, 100 * week_total / WEEKLY_QUOTA,
    )
