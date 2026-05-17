"""Render daily / journal / deep-read reports and maintain the site index."""
from __future__ import annotations

import re
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

from ..llm.prompts import TOPIC_LABELS_ZH, TOPICS
from ..models import Event, Paper

DOCS_DIR = Path("docs/daily")
JOURNALS_DIR = Path("docs/journals")
DEEP_READS_DIR = Path("docs/deep_reads")

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"


# ── per-paper block ───────────────────────────────────────────────────────────

def _paper_block(p: Paper, n: int, heading_prefix: str = "####") -> str:
    authors = ", ".join(p.authors[:6]) + (" et al." if len(p.authors) > 6 else "")
    cats = " · ".join(p.categories) if p.categories else ""
    head = f"{heading_prefix} {n}. [{p.paper_id}]({p.url}) — {p.title}"
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
    if not papers:
        return []
    groups = _group_by_topic(papers)
    out: list[str] = []
    ordered = [t for t in TOPICS if t in groups] + \
              [t for t in groups if t not in TOPICS]
    paper_prefix = heading_prefix + "#"
    for topic in ordered:
        ps = groups[topic]
        ps.sort(key=lambda p: p.score or 0, reverse=True)
        label = TOPIC_LABELS_ZH.get(topic, topic)
        out.append(f"{heading_prefix} {label}  *({topic}, {len(ps)} 篇)*\n")
        for i, p in enumerate(ps, 1):
            out.append(_paper_block(p, i, heading_prefix=paper_prefix))
    return out


def _footer() -> str:
    return (
        "\n---\n\n"
        f"Maintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · "
        f"[Source on GitHub]({REPO_URL})\n"
    )


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


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


# ── journals (one page per journal) ──────────────────────────────────────────

def _venue_issue_label(papers: list[Paper]) -> str:
    """Build a 'Vol X, Issue Y' label from papers' categories field."""
    pairs: set[tuple[int, int]] = set()
    jmlr_vols: set[int] = set()
    for p in papers:
        vol, iss = None, None
        for c in p.categories or []:
            m_vol = re.match(r"vol\s+(\d+)", c, re.I)
            m_iss = re.match(r"issue\s+(\d+)", c, re.I)
            m_jmlr = re.match(r"JMLR\s+v(\d+)", c)
            if m_vol:
                vol = int(m_vol.group(1))
            elif m_iss:
                iss = int(m_iss.group(1))
            elif m_jmlr:
                jmlr_vols.add(int(m_jmlr.group(1)))
        if vol is not None and iss is not None:
            pairs.add((vol, iss))
    if jmlr_vols and not pairs:
        if len(jmlr_vols) == 1:
            return f"Vol {next(iter(jmlr_vols))}"
        return f"Vols {min(jmlr_vols)}-{max(jmlr_vols)}"
    if not pairs:
        return ""
    if len(pairs) == 1:
        v, i = next(iter(pairs))
        return f"Vol {v} Issue {i}"
    sorted_p = sorted(pairs, reverse=True)
    if len(sorted_p) <= 4:
        return ", ".join(f"{v}({i})" for v, i in sorted_p)
    return f"{sorted_p[0][0]}({sorted_p[0][1]}) - {sorted_p[-1][0]}({sorted_p[-1][1]})"


def render_journal_page(
    papers: list[Paper],
    short: str,
    full: str,
    when: date | None = None,
    output_dir: Path = JOURNALS_DIR,
) -> Path:
    """Write one Markdown page for a single journal. Returns the path."""
    when = when or date.today()
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{when.isoformat()}-{_slug(short)}.md"

    papers_sorted = sorted(papers, key=lambda p: p.score or 0, reverse=True)
    issue_lbl = _venue_issue_label(papers_sorted)

    heading = f"# {short}"
    if issue_lbl:
        heading += f" — {issue_lbl}"
    heading += f"  ·  {when.isoformat()}\n"

    lines: list[str] = [
        heading,
        f"- 共 {len(papers_sorted)} 篇 · {full}\n",
    ]
    lines.extend(_render_topic_groups(papers_sorted, heading_prefix="##"))
    lines.append(_footer())
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


# ── homepage + archive pages ─────────────────────────────────────────────────

def _parse_date_from_stem(stem: str) -> str | None:
    """Extract YYYY-MM-DD from a filename stem, or None."""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", stem)
    return m.group(1) if m else None


def _journal_short_from_stem(stem: str) -> str:
    """'2026-05-17-jmlr' → 'JMLR', '2026-05-17-j-econometrics' → best guess."""
    # Strip leading date
    name = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)
    # Un-slug: hyphen → space, capitalise
    return name.replace("-", " ").upper()


def update_index(
    daily_dir: Path = DOCS_DIR,
    journals_dir: Path = JOURNALS_DIR,
    deep_reads_dir: Path = DEEP_READS_DIR,
) -> None:
    """Regenerate docs/index.md and the three archive pages."""
    from ..deep_read import load_index as _load_dr_index

    docs = Path("docs")
    docs.mkdir(parents=True, exist_ok=True)

    dailies = sorted(daily_dir.glob("*.md"), reverse=True) if daily_dir.exists() else []
    journal_pages = sorted(journals_dir.glob("*.md"), reverse=True) if journals_dir.exists() else []
    dr_entries = _load_dr_index()  # newest first from deep_reads_index.json

    today_str = dailies[0].stem if dailies else ""
    week_cutoff = (date.fromisoformat(today_str) - timedelta(days=7)).isoformat() \
        if today_str else ""

    lines: list[str] = [
        "# Research News\n",
        "每日 arXiv + 季度期刊的个性化统计学 / 因果推断研究资讯。\n",
    ]

    # ── 今日 ────────────────────────────────────────────────────────────────
    if today_str:
        lines.append(f"## 今日 · {today_str}\n")
        lines.append(f"### 每日 arXiv 速览\n")
        lines.append(f"[→ 查看完整报告](daily/{dailies[0].name})\n")

        today_dr = [e for e in dr_entries if e.get("date") == today_str]
        if today_dr:
            today_dr_sorted = sorted(today_dr, key=lambda e: e.get("score") or 0, reverse=True)
            lines.append(f"### 精读论文（{len(today_dr_sorted)} 篇）\n")
            for e in today_dr_sorted:
                topic_label = TOPIC_LABELS_ZH.get(e.get("topic", "other"), e.get("topic", "other"))
                lines.append(
                    f"- [{e['title']}]({e['doc_path']})  \n"
                    f"  `{topic_label}` · 相关性 {e.get('score', 0):.0f}/10"
                )
            lines.append("")

        # Today's journal pages
        today_journals = [j for j in journal_pages
                          if _parse_date_from_stem(j.stem) == today_str]
        if today_journals:
            lines.append("### 期刊更新\n")
            for j in today_journals:
                short = _journal_short_from_stem(j.stem)
                lines.append(f"- [{short}](journals/{j.name})")
            lines.append("")

    # ── 本周 ────────────────────────────────────────────────────────────────
    week_dailies = [d for d in dailies
                    if d.stem != today_str and d.stem >= week_cutoff]
    week_journals = [j for j in journal_pages
                     if (_parse_date_from_stem(j.stem) or "") < today_str
                     and (_parse_date_from_stem(j.stem) or "") >= week_cutoff]

    if week_dailies or week_journals:
        lines.append("## 本周\n")
        if week_dailies:
            lines.append("### 每日报告\n")
            for d in week_dailies:
                lines.append(f"- [{d.stem}](daily/{d.name})")
            lines.append("")
        if week_journals:
            lines.append("### 期刊\n")
            for j in week_journals:
                short = _journal_short_from_stem(j.stem)
                date_str = _parse_date_from_stem(j.stem) or j.stem
                lines.append(f"- [{short} · {date_str}](journals/{j.name})")
            lines.append("")

    # ── 存档入口 ─────────────────────────────────────────────────────────────
    lines.append("## 存档\n")
    lines.append("- [→ 所有每日报告](all_daily.md)")
    lines.append("- [→ 所有期刊](all_journals.md)")
    lines.append("- [→ 所有精读报告](all_deep_reads.md)")
    lines.append("")

    lines.append(_footer())
    (docs / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Also regenerate the three archive pages
    _update_all_daily_page(dailies, docs)
    _update_all_journals_page(journal_pages, docs)
    _update_all_deep_reads_page(dr_entries, docs)


def _update_all_daily_page(dailies: list[Path], docs: Path) -> None:
    lines = ["# 每日 arXiv 存档\n"]
    if not dailies:
        lines.append("*（暂无记录）*\n")
        (docs / "all_daily.md").write_text("\n".join(lines), encoding="utf-8")
        return
    by_month: dict[str, list[Path]] = defaultdict(list)
    for d in dailies:
        month = d.stem[:7]  # YYYY-MM
        by_month[month].append(d)
    for month in sorted(by_month.keys(), reverse=True):
        lines.append(f"## {month}\n")
        for d in sorted(by_month[month], reverse=True):
            lines.append(f"- [{d.stem}](daily/{d.name})")
        lines.append("")
    lines.append(_footer())
    (docs / "all_daily.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _update_all_journals_page(journal_pages: list[Path], docs: Path) -> None:
    lines = ["# 期刊存档\n"]
    if not journal_pages:
        lines.append("*（暂无记录）*\n")
        (docs / "all_journals.md").write_text("\n".join(lines), encoding="utf-8")
        return
    # Group by journal short name
    by_journal: dict[str, list[Path]] = defaultdict(list)
    for j in journal_pages:
        short = _journal_short_from_stem(j.stem)
        by_journal[short].append(j)
    for short in sorted(by_journal.keys()):
        lines.append(f"## {short}\n")
        for j in sorted(by_journal[short], reverse=True):
            date_str = _parse_date_from_stem(j.stem) or j.stem
            lines.append(f"- [{date_str}](journals/{j.name})")
        lines.append("")
    lines.append(_footer())
    (docs / "all_journals.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _update_all_deep_reads_page(entries: list[dict], docs: Path) -> None:
    lines = ["# 精读报告存档\n"]
    if not entries:
        lines.append("*（暂无记录）*\n")
        (docs / "all_deep_reads.md").write_text("\n".join(lines), encoding="utf-8")
        return
    by_date: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_date[e.get("date", "unknown")].append(e)
    for d in sorted(by_date.keys(), reverse=True):
        lines.append(f"## {d}\n")
        day_entries = sorted(by_date[d], key=lambda e: e.get("score") or 0, reverse=True)
        for e in day_entries:
            topic_label = TOPIC_LABELS_ZH.get(e.get("topic", "other"), e.get("topic", "other"))
            run_type = e.get("run_type", "")
            tag = f"[{run_type}]" if run_type else ""
            lines.append(
                f"- [{e['title']}]({e['doc_path']})  \n"
                f"  `{topic_label}` · {e.get('score', 0):.0f}/10 {tag}"
            )
        lines.append("")
    lines.append(_footer())
    (docs / "all_deep_reads.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
