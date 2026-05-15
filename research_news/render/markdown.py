"""Render the daily report as a Markdown page consumed by MkDocs."""
from __future__ import annotations

from datetime import date
from pathlib import Path

from ..models import Event, Paper

DOCS_DIR = Path("docs/daily")


def _paper_block(p: Paper, n: int) -> str:
    authors = ", ".join(p.authors[:6]) + (" et al." if len(p.authors) > 6 else "")
    cats = " · ".join(p.categories) if p.categories else ""
    head = f"### {n}. [{p.paper_id}]({p.url}) — {p.title}"
    body = []
    body.append(f"- **作者**: {authors}")
    if cats:
        body.append(f"- **分类**: {cats}")
    if p.score is not None:
        body.append(f"- **相关性**: {p.score:.0f}/10")
    if p.summary_zh:
        body.append(f"- **摘要**: {p.summary_zh}")
    if p.why_relevant:
        body.append(f"- **为什么对您有用**: {p.why_relevant}")
    return head + "\n" + "\n".join(body) + "\n"


def render_daily(
    papers_high: list[Paper],
    papers_mid: list[Paper],
    events: list[Event],
    when: date | None = None,
    output_dir: Path = DOCS_DIR,
) -> Path:
    when = when or date.today()
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{when.isoformat()}.md"

    lines: list[str] = []
    lines.append(f"# {when.isoformat()} 每日研究资讯\n")
    lines.append(
        f"- 高相关论文 {len(papers_high)} 篇 · 中相关 {len(papers_mid)} 篇 · "
        f"会议/Seminar 事件 {len(events)} 条\n"
    )

    if papers_high:
        lines.append("## ⭐ 高相关论文")
        for i, p in enumerate(papers_high, 1):
            lines.append(_paper_block(p, i))

    if papers_mid:
        lines.append("## 📌 中相关论文")
        for i, p in enumerate(papers_mid, 1):
            lines.append(_paper_block(p, i))

    if events:
        lines.append("## 📅 会议 / Seminar")
        by_source: dict[str, list[Event]] = {}
        for e in events:
            by_source.setdefault(e.source, []).append(e)
        for src, evs in by_source.items():
            lines.append(f"### {src}")
            for e in evs:
                line = f"- **{e.title}**"
                if e.date:
                    line += f" — {e.date}"
                if e.speaker:
                    line += f" · {e.speaker}"
                if e.location:
                    line += f" · {e.location}"
                if e.url:
                    line += f" · [link]({e.url})"
                if e.note:
                    line += f"  \n  {e.note}"
                lines.append(line)
            lines.append("")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def update_index(output_dir: Path = DOCS_DIR) -> None:
    """Regenerate docs/index.md with a chronological list of dailies."""
    docs = Path("docs")
    docs.mkdir(parents=True, exist_ok=True)
    dailies = sorted(output_dir.glob("*.md"), reverse=True)
    lines = ["# Research News\n", "每日统计学与因果推断研究资讯。\n", "## 历史报告\n"]
    for d in dailies:
        lines.append(f"- [{d.stem}](daily/{d.name})")
    (docs / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
