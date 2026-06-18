"""OCIS per-season overview pages.

Group the OCIS talk catalog (data/ocis_catalog.json) by season into
docs/talks/seasons/<slug>.md — each page an LLM 导览 (the season's themes +
what to read first) followed by every talk in that season, linking to its
deep-read when one exists and listing metadata-only (with a 「暂无精读」 tag)
otherwise. docs/all_talks.md becomes the season index.

Self-contained; refresh with `python -m research_news.talks seasons`. The season
label comes from the OCIS source page (Talk.season, via import-ocis), falling
back to a date-derived season.
"""
from __future__ import annotations

import json
import logging
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING

from .llm.prompts import TALK_SEASON_OVERVIEW_SYSTEM
from .scrapers.ocis import CATALOG_PATH, make_talk_id, normalize_date

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger("research_news")

DOCS = Path("docs")
SEASONS_DIR = DOCS / "talks" / "seasons"
SEASONS_INDEX = Path("data/talk_seasons_index.json")
TALKS_INDEX = Path("data/talks_index.json")
DEFAULT_MODEL = os.environ.get("TALK_OVERVIEW_MODEL", os.environ.get("DAILY_MODEL", "glm-5.1"))

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"

_SEASON_ORDER = {"winter": 0, "spring": 1, "summer": 2, "fall": 3}


# ── season helpers (pure) ─────────────────────────────────────────────────────

def _date_season(date_str: str | None) -> str | None:
    m = re.match(r"(\d{4})-(\d{2})", date_str or "")
    if not m:
        return None
    year, month = int(m.group(1)), int(m.group(2))
    s = "spring" if 1 <= month <= 5 else "summer" if 6 <= month <= 8 else "fall"
    return f"{s}-{year}"


def season_of(row: dict) -> str:
    """The season a talk belongs to: its OCIS source season, else date-derived."""
    return (row.get("season") or "").strip().lower() or _date_season(row.get("date")) or "unknown"


def season_sort_key(slug: str) -> tuple[int, int]:
    m = re.match(r"(winter|spring|summer|fall)-(\d{4})", slug)
    return (int(m.group(2)), _SEASON_ORDER[m.group(1)]) if m else (0, 0)


def season_label(slug: str) -> str:
    m = re.match(r"([a-z]+)-(\d{4})", slug)
    return f"{m.group(1).capitalize()} {m.group(2)}" if m else slug


def _first_sentence(text: str, limit: int = 100) -> str:
    """A clean one-line blurb for the index: drop markdown emphasis, take the
    first sentence, else cut at a clean boundary + '…' (never mid-`**bold**`)."""
    t = re.sub(r"\*\*|`|#", "", (text or "").strip())
    t = re.sub(r"\s+", " ", t).strip()
    if not t:
        return ""
    m = re.match(r"(.{0,%d}?[。！？.!?])" % limit, t)
    if m:
        return m.group(1).strip()
    head = t[:limit]
    cut = max(head.rfind("、"), head.rfind("，"), head.rfind("（"), head.rfind("："))
    if cut >= limit // 2:
        head = head[:cut]
    return head.strip(" 、，（：") + "…"


def _existing_overview(slug: str) -> str:
    """The 导览 already written into a season page, so a re-run can reuse it
    instead of paying for the LLM again."""
    p = SEASONS_DIR / f"{slug}.md"
    if not p.exists():
        return ""
    body = p.read_text(encoding="utf-8")
    m = re.search(r"##\s*本季导览\s*\n+>[^\n]*\n+(.*?)\n+##\s*报告列表", body, re.DOTALL)
    return m.group(1).strip() if m else ""


# ── data loading ──────────────────────────────────────────────────────────────

def _load_catalog() -> list[dict]:
    if not CATALOG_PATH.exists():
        return []
    try:
        data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _load_read_index() -> dict[str, dict]:
    """talk_id → talks_index entry (the talks that have a deep-read page)."""
    if not TALKS_INDEX.exists():
        return {}
    try:
        data = json.loads(TALKS_INDEX.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {e["talk_id"]: e for e in data if isinstance(e, dict) and e.get("talk_id")}


def _read_excerpt(doc_path: str | None, max_chars: int = 600) -> str:
    """Pull the '一、…' section of a deep-read note for the overview prompt."""
    if not doc_path:
        return ""
    p = DOCS / doc_path
    if not p.exists():
        return ""
    body = p.read_text(encoding="utf-8")
    m = re.search(r"###\s*一[、,].*?(?=\n###\s*二[、,])", body, re.DOTALL)
    chunk = m.group(0) if m else body
    return re.sub(r"\s+", " ", chunk).strip()[:max_chars]


def _entry(row: dict, read_idx: dict[str, dict]) -> dict:
    tid = make_talk_id(row)
    e = read_idx.get(tid)
    return {
        "id": tid,
        "date": normalize_date(row.get("date")) or (row.get("date") or ""),
        "title": (row.get("title") or "").strip() or tid,
        "speaker": (row.get("speaker") or "").strip() or None,
        "discussant": (row.get("discussant") or "").strip() or None,
        "abstract": (row.get("abstract") or "").strip() or None,
        "video": (row.get("video") or "").strip() or None,
        "slides": (row.get("slides") or "").strip() or None,
        "arxiv": (row.get("arxiv") or "").strip() or None,
        "doc_path": e.get("doc_path") if e else None,
    }


# ── overview (LLM) ────────────────────────────────────────────────────────────

def build_overview_input(entries: list[dict], label: str) -> str:
    blocks: list[str] = []
    for e in entries:
        lines = [f"- 讲者: {e['speaker'] or '?'}｜题目: {e['title']}"]
        if e["abstract"]:
            lines.append("  摘要: " + re.sub(r"\s+", " ", e["abstract"])[:400])
        excerpt = _read_excerpt(e["doc_path"])
        if excerpt:
            lines.append("  精读摘录: " + excerpt)
        blocks.append("\n".join(lines))
    return f"OCIS {label}，共 {len(entries)} 场：\n\n" + "\n\n".join(blocks)


def generate_overview(client: "SJTUClient", entries: list[dict], label: str,
                      *, model: str | None = None) -> str:
    return client.chat(
        [
            {"role": "system", "content": TALK_SEASON_OVERVIEW_SYSTEM},
            {"role": "user", "content": build_overview_input(entries, label)},
        ],
        model=model,
        max_tokens=2500,
    )


# ── render ────────────────────────────────────────────────────────────────────

def render_season_page(slug: str, entries: list[dict], overview: str) -> Path:
    SEASONS_DIR.mkdir(parents=True, exist_ok=True)
    out = SEASONS_DIR / f"{slug}.md"
    label = season_label(slug)
    n_read = sum(1 for e in entries if e["doc_path"])
    lines = [
        f"# OCIS · {label}\n",
        f"- 共 {len(entries)} 场 · {n_read} 篇精读 · Online Causal Inference Seminar\n",
    ]
    if overview:
        lines += [
            "## 本季导览\n",
            "> 自动生成：归纳本季主线与值得先看的几场，**不打分、不排名**。\n",
            overview.strip() + "\n",
        ]
    lines.append("## 报告列表\n")
    for e in sorted(entries, key=lambda e: e["date"], reverse=True):
        if e["doc_path"]:
            lines.append(f"### [{e['title']}](../{Path(e['doc_path']).name})")
        else:
            lines.append(f"### {e['title']}　*（暂无精读）*")
        meta = []
        if e["speaker"]:
            meta.append(f"**讲者**: {e['speaker']}")
        if e["discussant"]:
            meta.append(f"**讨论人**: {e['discussant']}")
        if e["date"]:
            meta.append(e["date"])
        if meta:
            lines.append(" · ".join(meta) + "  ")
        links = []
        if e["video"]:
            links.append(f"[视频]({e['video']})")
        if e["slides"]:
            links.append(f"[幻灯片]({e['slides']})")
        if e["arxiv"]:
            links.append(f"[arXiv]({e['arxiv']})")
        if links:
            lines.append("链接：" + " · ".join(links))
        if e["abstract"]:
            ab = e["abstract"]
            ab = ab[:500] + "…" if len(ab) > 500 else ab
            lines.append(f"<details><summary>摘要</summary>\n\n{ab}\n\n</details>")
        lines.append("")
    lines.append(f"\n---\n\nMaintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · [Source]({REPO_URL})\n")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def _write_index(new_entries: list[dict]) -> list[dict]:
    existing: list[dict] = []
    if SEASONS_INDEX.exists():
        try:
            existing = json.loads(SEASONS_INDEX.read_text(encoding="utf-8"))
        except Exception:
            existing = []
    by_season = {e["season"]: e for e in existing if e.get("season")}
    for e in new_entries:
        by_season[e["season"]] = e
    merged = sorted(by_season.values(), key=lambda e: season_sort_key(e["season"]), reverse=True)
    SEASONS_INDEX.parent.mkdir(parents=True, exist_ok=True)
    SEASONS_INDEX.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    return merged


def write_archive(index_entries: list[dict]) -> None:
    """Rewrite docs/all_talks.md as the season index (site nav target)."""
    lines = [
        "# 讲座精读（OCIS）\n",
        "Online Causal Inference Seminar 历史讲座，按季分组。每季一页：**导览** + 全部报告"
        "（每场链到精读；网页有元数据但未精读的也列出，标「暂无精读」）。\n",
    ]
    by_year: dict[str, list[dict]] = defaultdict(list)
    for e in sorted(index_entries, key=lambda e: season_sort_key(e["season"]), reverse=True):
        by_year[e["season"].split("-")[-1]].append(e)
    for year in sorted(by_year, reverse=True):
        lines.append(f"## {year}\n")
        for e in by_year[year]:
            blurb = f" — {e['blurb']}" if e.get("blurb") else ""
            lines.append(
                f"- [{e['label']}]({e['doc_path']}) · {e['n']} 场（{e['n_read']} 精读）{blurb}"
            )
        lines.append("")
    lines.append(f"\n---\n\nMaintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · [Source]({REPO_URL})\n")
    (DOCS / "all_talks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── run ───────────────────────────────────────────────────────────────────────

def group_by_season(rows: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        groups[season_of(r)].append(r)
    return groups


def run(
    *,
    seasons: list[str] | None = None,
    model: str | None = None,
    overview: bool = True,
    force: bool = False,
    dry_run: bool = False,
) -> list[Path]:
    rows = _load_catalog()
    if not rows:
        log.warning("no OCIS catalog at %s — run `talks import-ocis` first", CATALOG_PATH)
        return []
    read_idx = _load_read_index()
    groups = group_by_season(rows)
    slugs = sorted(groups, key=season_sort_key, reverse=True)
    if seasons:
        want = {s.strip().lower() for s in seasons}
        slugs = [s for s in slugs if s in want]

    if dry_run:
        for s in slugs:
            es = groups[s]
            log.info("  %s: %d talks (%d read)", s, len(es),
                     sum(1 for r in es if make_talk_id(r) in read_idx))
        return []

    # Reuse the 导览 already on each page unless --force; only spin up the LLM
    # client (and need an API key) when something actually has to be generated.
    client: "SJTUClient | None" = None

    def _get_client() -> "SJTUClient":
        nonlocal client
        if client is None:
            from dotenv import load_dotenv

            from .llm.sjtu_client import SJTUClient
            load_dotenv()
            client = SJTUClient()
        return client

    written: list[Path] = []
    index_entries: list[dict] = []
    for slug in slugs:
        # Dedupe talks by id (the catalog can carry the same talk twice).
        seen: set[str] = set()
        entries: list[dict] = []
        for r in groups[slug]:
            e = _entry(r, read_idx)
            if e["id"] not in seen:
                seen.add(e["id"])
                entries.append(e)
        ov = ""
        if overview:
            if not force:
                ov = _existing_overview(slug)
            if not ov:
                try:
                    ov = generate_overview(_get_client(), entries, season_label(slug), model=model)
                except Exception as e:  # noqa: BLE001
                    log.warning("overview failed for %s: %s", slug, e)
        page = render_season_page(slug, entries, ov)
        written.append(page)
        index_entries.append({
            "season": slug,
            "label": season_label(slug),
            "n": len(entries),
            "n_read": sum(1 for e in entries if e["doc_path"]),
            "doc_path": f"talks/seasons/{page.name}",
            "blurb": _first_sentence(ov),
        })
        log.info("wrote %s (%d talks, %d read)", page, len(entries), index_entries[-1]["n_read"])

    if index_entries:
        merged = _write_index(index_entries)
        write_archive(merged)
    return written
