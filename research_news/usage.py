"""Token usage logging — shared by daily.py and journals.py.

Per-run log goes to data/token_usage.json (append-only list). Also logs
to stdout/file. Used to monitor against the SJTU weekly quota of 1e9 tokens.
"""
from __future__ import annotations

import json
import logging
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger(__name__)

USAGE_FILE = Path("data/token_usage.json")
USAGE_PAGE = Path("docs/token_usage.md")
WEEKLY_QUOTA = 1_000_000_000   # SJTU quota: 1e9 tokens/week


def _week_start(today: date | None = None) -> date:
    """Return the most recent Monday (today if today is Monday)."""
    today = today or date.today()
    return today - timedelta(days=today.weekday())


def _fmt(n: int) -> str:
    return f"{n:,}"


def render_usage_page(
    history: list[dict],
    *,
    page_path: Path = USAGE_PAGE,
    today: date | None = None,
) -> None:
    """Write a human-readable Token 消耗 page based on `history`."""
    today = today or date.today()
    week_start = _week_start(today)

    total_all = sum(h.get("total_tokens", 0) for h in history)
    total_calls = sum(h.get("calls", 0) for h in history)

    this_week = [h for h in history if h.get("run_at", "") >= week_start.isoformat()]
    week_total = sum(h.get("total_tokens", 0) for h in this_week)
    week_calls = sum(h.get("calls", 0) for h in this_week)

    by_model_week: dict[str, dict[str, int]] = defaultdict(
        lambda: {"prompt": 0, "completion": 0, "total": 0, "calls": 0}
    )
    for h in this_week:
        for model, u in (h.get("by_model") or {}).items():
            by_model_week[model]["prompt"] += u.get("prompt_tokens", 0)
            by_model_week[model]["completion"] += u.get("completion_tokens", 0)
            by_model_week[model]["total"] += u.get("total_tokens", 0)
        # calls are reported per-run, not per-model; split proportionally is
        # noisy — just sum at the run level, shown in pipeline breakdown.

    by_pipeline_week: dict[str, dict[str, int]] = defaultdict(
        lambda: {"calls": 0, "total": 0, "runs": 0}
    )
    for h in this_week:
        p = h.get("pipeline") or "?"
        by_pipeline_week[p]["calls"] += h.get("calls", 0)
        by_pipeline_week[p]["total"] += h.get("total_tokens", 0)
        by_pipeline_week[p]["runs"] += 1

    pct_quota = 100 * week_total / WEEKLY_QUOTA if WEEKLY_QUOTA else 0

    lines: list[str] = [
        "# Token 消耗\n",
        "本页由 `research_news.usage.render_usage_page()` 自动生成。",
        f"统计口径：`data/token_usage.json` 累积日志；本周自 **{week_start.isoformat()}（周一）00:00 UTC** 起。\n",
        "## 总览\n",
        f"- **历史总消耗**：{_fmt(total_all)} tokens，共 {_fmt(total_calls)} 次 LLM 调用",
        f"- **本周累计**：{_fmt(week_total)} tokens，{_fmt(week_calls)} 次调用",
        f"- **配额占用**：{_fmt(week_total)} / {_fmt(WEEKLY_QUOTA)} = **{pct_quota:.2f}%** "
        f"（上海交大 GLM 周配额 {_fmt(WEEKLY_QUOTA)}/周）\n",
    ]

    lines.append("## 本周按模型分\n")
    if by_model_week:
        lines.append("| 模型 | prompt | completion | total |")
        lines.append("|---|---:|---:|---:|")
        for model in sorted(by_model_week, key=lambda m: by_model_week[m]["total"], reverse=True):
            u = by_model_week[model]
            lines.append(
                f"| `{model}` | {_fmt(u['prompt'])} | {_fmt(u['completion'])} | {_fmt(u['total'])} |"
            )
        lines.append("")
    else:
        lines.append("*（本周暂无运行）*\n")

    lines.append("## 本周按 pipeline 分\n")
    if by_pipeline_week:
        lines.append("| pipeline | 运行次数 | LLM 调用 | total tokens |")
        lines.append("|---|---:|---:|---:|")
        for pipe in sorted(by_pipeline_week, key=lambda p: by_pipeline_week[p]["total"], reverse=True):
            u = by_pipeline_week[pipe]
            lines.append(
                f"| `{pipe}` | {u['runs']} | {_fmt(u['calls'])} | {_fmt(u['total'])} |"
            )
        lines.append("")
    else:
        lines.append("*（本周暂无运行）*\n")

    lines.append("## 最近 30 次运行\n")
    if history:
        lines.append("| 运行日期 | 报告日期 | pipeline | 调用 | total tokens |")
        lines.append("|---|---|---|---:|---:|")
        for h in list(reversed(history))[:30]:
            lines.append(
                f"| {h.get('run_at','?')} | {h.get('report_date','-')} | "
                f"`{h.get('pipeline') or '?'}` | {_fmt(h.get('calls',0))} | "
                f"{_fmt(h.get('total_tokens',0))} |"
            )
        lines.append("")
    else:
        lines.append("*（暂无记录）*\n")

    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def report(client: "SJTUClient", pipeline: str, run_date: date | None = None,
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

    # Refresh the published docs/token_usage.md page so the site reflects
    # latest consumption right after every run.
    try:
        render_usage_page(history)
    except Exception as e:
        log.warning("failed to render token_usage.md: %s", e)
