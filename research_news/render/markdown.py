"""Render the daily / journals report as a Markdown page consumed by MkDocs."""
from __future__ import annotations

import re
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
    """Render papers grouped by topic, ordered by TOPICS, with stable numbering
    restarting at 1 inside each topic. Paper blocks nest one level deeper than
    the topic-group heading."""
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

def _venue_issue_label(papers: list[Paper]) -> str:
    """For papers in one venue, build a 'Vol X, Issue Y' (or multi-issue range)
    label from their categories field (which holds 'vol N', 'issue M', 'pp ...').
    JMLR papers have 'JMLR vN' in categories — handle that variant too."""
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
    # Multi-issue: list sorted descending, capped
    sorted_p = sorted(pairs, reverse=True)
    if len(sorted_p) <= 4:
        return ", ".join(f"{v}({i})" for v, i in sorted_p)
    return f"{sorted_p[0][0]}({sorted_p[0][1]}) - {sorted_p[-1][0]}({sorted_p[-1][1]})"


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def render_journals_by_group(
    papers: list[Paper],
    groups: dict,
    when: date | None = None,
    output_dir: Path = JOURNALS_DIR,
    label: str | None = None,
) -> list[Path]:
    """Write one Markdown page per group. Each page has venue → topic sections.

    `groups` is the parsed config/journals.yaml dict (see journals._load_groups).
    Pages are named `<date>-<group_key>[-<label>].md`. Empty groups (no papers
    in them after fetch + filter) are skipped silently.
    """
    when = when or date.today()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build venue → group_key reverse map, and gather papers per group.
    venue_to_group: dict[str, str] = {}
    venue_to_short: dict[str, str] = {}
    for gkey, gcfg in groups.items():
        for jcfg in gcfg["journals"]:
            venue_to_group[jcfg["full"]] = gkey
            venue_to_short[jcfg["full"]] = jcfg.get("short", jcfg["full"])

    by_group: dict[str, list[Paper]] = defaultdict(list)
    for p in papers:
        venue = p.venue or ""
        gkey = venue_to_group.get(venue, "other")
        by_group[gkey].append(p)

    out_paths: list[Path] = []
    suffix = f"-{label}" if label else ""
    for gkey, gcfg in groups.items():
        ps = by_group.get(gkey, [])
        if not ps:
            continue
        out = output_dir / f"{when.isoformat()}-{gkey}{suffix}.md"
        out_paths.append(out)

        # Group papers by venue inside this group
        by_venue: dict[str, list[Paper]] = defaultdict(list)
        for p in ps:
            by_venue[p.venue or "Unknown"].append(p)
        n_venues = len(by_venue)

        lines: list[str] = []
        lines.append(f"# {gcfg.get('label', gkey)} — {when.isoformat()}\n")
        lines.append(f"- 共 {len(ps)} 篇 · 来自 {n_venues} 个期刊"
                     f" · 分组 `{gkey}`\n")

        # Venue order: follow the YAML order so the user's mental list matches
        venue_order = [j["full"] for j in gcfg["journals"]]
        venue_order_set = set(venue_order)
        ordered_venues = [v for v in venue_order if v in by_venue] + \
                         [v for v in by_venue if v not in venue_order_set]

        for venue in ordered_venues:
            vps = by_venue[venue]
            vps.sort(key=lambda p: p.score or 0, reverse=True)
            short = venue_to_short.get(venue, venue)
            issue_lbl = _venue_issue_label(vps)
            heading = f"## {short} — {issue_lbl}" if issue_lbl else f"## {short}"
            heading += f"  *({len(vps)} 篇)*\n"
            lines.append(heading)
            lines.extend(_render_topic_groups(vps, heading_prefix="###"))

        # Also show any "other" papers (venue not in this group's YAML list)
        # We skip them — they should never end up here unless venue strings drift.

        lines.append(_footer())
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # "other" bucket: papers whose venue isn't in any group (e.g. loaded from
    # an old JSON before the group was added). Write to a dedicated page.
    other = by_group.get("other", [])
    if other:
        out = output_dir / f"{when.isoformat()}-other{suffix}.md"
        out_paths.append(out)
        by_venue: dict[str, list[Paper]] = defaultdict(list)
        for p in other:
            by_venue[p.venue or "Unknown"].append(p)
        lines = [f"# 其他期刊 — {when.isoformat()}\n",
                 f"- 共 {len(other)} 篇 · 来自 {len(by_venue)} 个未分组期刊\n"]
        for venue, vps in by_venue.items():
            vps.sort(key=lambda p: p.score or 0, reverse=True)
            issue_lbl = _venue_issue_label(vps)
            heading = f"## {venue} — {issue_lbl}" if issue_lbl else f"## {venue}"
            heading += f"  *({len(vps)} 篇)*\n"
            lines.append(heading)
            lines.extend(_render_topic_groups(vps, heading_prefix="###"))
        lines.append(_footer())
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return out_paths


# ── index ─────────────────────────────────────────────────────────────────────

def update_index(daily_dir: Path = DOCS_DIR,
                 journals_dir: Path = JOURNALS_DIR) -> None:
    """Regenerate docs/index.md with chronological lists of daily + journal pages.

    Journal pages are grouped by group key (parsed out of the filename:
    `<date>-<group>[-<label>].md`).
    """
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
        # Group journal pages by the inferred group key.
        # File pattern: YYYY-MM-DD-<group>[-<label>].md
        by_group: dict[str, list[Path]] = defaultdict(list)
        for j in journals:
            m = re.match(r"\d{4}-\d{2}-\d{2}-([a-z_]+)", j.stem)
            gkey = m.group(1) if m else "other"
            by_group[gkey].append(j)

        # Stable display order: core first, then alphabetical
        preferred = ["core", "prob_stats", "applied", "econ"]
        ordered = [k for k in preferred if k in by_group] + \
                  sorted(k for k in by_group if k not in preferred)

        lines.append("## 期刊\n")
        for gkey in ordered:
            lines.append(f"### `{gkey}`\n")
            for j in by_group[gkey]:
                lines.append(f"- [{j.stem}](journals/{j.name})")
            lines.append("")

    lines.append(_footer())
    (docs / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
