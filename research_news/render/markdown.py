"""Render the daily / journals report as a Markdown page consumed by MkDocs."""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from pathlib import Path

from ..llm.prompts import TOPIC_LABELS_ZH, TOPICS
from ..models import Event, Paper

DOCS_DIR = Path("docs/daily")
JOURNALS_DIR = Path("docs/journals")

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"


# ── per-paper block ───────────────────────────────────────────────────────────

def _paper_block(p: Paper, n: int) -> str:
    authors = ", ".join(p.authors[:6]) + (" et al." if len(p.authors) > 6 else "")
    cats = " · ".join(p.categories) if p.categories else ""
    head = f"### {n}. [{p.paper_id}]({p.url}) — {p.title}"
    body = []
    body.append(f"- **作者**: {authors}")
    if p.venue:
        body.append(f"- **期刊/来源**: {p.venue}")
    if cats:
        body.append(f"- **分类**: {cats}")
    bits = []
    if p.score is not None:
        bits.append(f"相关性 {p.score:.0f}/10")
    if p.novelty_flag:
        bits.append(f"novelty: `{p.novelty_flag}`")
    if bits:
        body.append("- " + " · ".join(bits))
    if p.summary_zh:
        body.append(f"- **摘要**: {p.summary_zh}")
    if p.key_techniques:
        body.append("- **关键技术**: " + ", ".join(f"`{k}`" for k in p.key_techniques))
    if p.why_relevant:
        body.append(f"- **为什么对您有用**: {p.why_relevant}")
    if p.pdf_path:
        body.append(f"- **本地 PDF**: `{p.pdf_path}`")
    return head + "\n" + "\n".join(body) + "\n"


def _group_by_topic(papers: list[Paper]) -> dict[str, list[Paper]]:
    groups: dict[str, list[Paper]] = defaultdict(list)
    for p in papers:
        groups[p.topic or "other"].append(p)
    return groups


def _render_topic_groups(papers: list[Paper], heading_prefix: str) -> list[str]:
    """Render papers grouped by topic, ordered by TOPICS, with stable numbering
    restarting at 1 inside each topic."""
    if not papers:
        return []
    groups = _group_by_topic(papers)
    out: list[str] = []
    # Ordered by TOPICS, plus any unexpected topics appended at the end.
    ordered = [t for t in TOPICS if t in groups] + \
              [t for t in groups if t not in TOPICS]
    for topic in ordered:
        ps = groups[topic]
        ps.sort(key=lambda p: p.score or 0, reverse=True)
        label = TOPIC_LABELS_ZH.get(topic, topic)
        out.append(f"{heading_prefix} {label}  *({topic}, {len(ps)} 篇)*\n")
        for i, p in enumerate(ps, 1):
            out.append(_paper_block(p, i))
    return out


# ── footer ────────────────────────────────────────────────────────────────────

def _footer() -> str:
    return (
        "\n---\n\n"
        f"Maintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · "
        f"[Source on GitHub]({REPO_URL})\n"
    )


# ── daily ─────────────────────────────────────────────────────────────────────

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
    lines.append(f"# {when.isoformat()} 每日 arXiv 资讯\n")
    lines.append(
        f"- 高相关论文 {len(papers_high)} 篇 · 中相关 {len(papers_mid)} 篇 · "
        f"会议/Seminar 事件 {len(events)} 条\n"
    )

    if papers_high:
        lines.append("## ⭐ 高相关论文（按主题分组）\n")
        lines.extend(_render_topic_groups(papers_high, heading_prefix="###"))

    if papers_mid:
        lines.append("## 📌 中相关论文（按主题分组）\n")
        lines.extend(_render_topic_groups(papers_mid, heading_prefix="###"))

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

    lines.append(_footer())
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


# ── journals ──────────────────────────────────────────────────────────────────

def render_journals(
    papers: list[Paper],
    when: date | None = None,
    output_dir: Path = JOURNALS_DIR,
    label: str | None = None,
) -> Path:
    """Render journal-issue pull. Grouped by venue (journal), then by topic
    inside each venue."""
    when = when or date.today()
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"-{label}" if label else ""
    out = output_dir / f"{when.isoformat()}{suffix}.md"

    by_venue: dict[str, list[Paper]] = defaultdict(list)
    for p in papers:
        by_venue[p.venue or "Unknown"].append(p)

    lines: list[str] = []
    lines.append(f"# {when.isoformat()} 期刊最新一期\n")
    lines.append(f"- 共 {len(papers)} 篇 · 来自 {len(by_venue)} 个期刊\n")
    for venue, ps in by_venue.items():
        ps.sort(key=lambda p: p.score or 0, reverse=True)
        lines.append(f"## {venue}  *({len(ps)} 篇)*\n")
        lines.extend(_render_topic_groups(ps, heading_prefix="###"))

    lines.append(_footer())
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


# ── index ─────────────────────────────────────────────────────────────────────

def update_index(daily_dir: Path = DOCS_DIR,
                 journals_dir: Path = JOURNALS_DIR) -> None:
    """Regenerate docs/index.md with chronological lists of daily + journal pages."""
    docs = Path("docs")
    docs.mkdir(parents=True, exist_ok=True)
    dailies = sorted(daily_dir.glob("*.md"), reverse=True)
    journals = sorted(journals_dir.glob("*.md"), reverse=True) \
        if journals_dir.exists() else []

    lines = [
        "# Research News\n",
        "每日 arXiv + 季度期刊的个性化统计学 / 因果推断研究资讯。\n",
    ]
    if dailies:
        lines.append("## 每日 arXiv\n")
        for d in dailies:
            lines.append(f"- [{d.stem}](daily/{d.name})")
        lines.append("")
    if journals:
        lines.append("## 期刊最新一期\n")
        for j in journals:
            lines.append(f"- [{j.stem}](journals/{j.name})")
        lines.append("")
    lines.append(_footer())
    (docs / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
