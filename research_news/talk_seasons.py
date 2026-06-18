"""Per-series, per-season overview pages for the talk catalog.

Group every talk — the OCIS catalog (data/ocis_catalog.json) *and* the
hand-curated config/talks.yaml (INI, etc.) — by **series** (conference) then
**season** into docs/talks/seasons/<series>-<season>.md. Each page is an LLM
导览 (themes + what to read first) + every talk in that (series, season): linked
to its deep-read when one exists, listed metadata-only ("暂无精读") otherwise.
docs/all_talks.md becomes the index, grouped by series.

Refresh with `python -m research_news.talks seasons`. Series come from each
talk's `series` (or are derived from the venue: OCIS / INI / …); the OCIS season
comes from its source page (date-derived fallback).
"""
from __future__ import annotations

import json
import logging
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

from .llm.prompts import TALK_SEASON_OVERVIEW_SYSTEM
from .scrapers.ocis import CATALOG_PATH, make_talk_id, normalize_date

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger("research_news")

DOCS = Path("docs")
SEASONS_DIR = DOCS / "talks" / "seasons"
SEASONS_INDEX = Path("data/talk_seasons_index.json")
TALKS_INDEX = Path("data/talks_index.json")
TALKS_CONFIG = Path("config/talks.yaml")
DEFAULT_MODEL = os.environ.get("TALK_OVERVIEW_MODEL", os.environ.get("DAILY_MODEL", "glm-5.1"))

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"

_SEASON_ORDER = {"winter": 0, "spring": 1, "summer": 2, "fall": 3}


# ── season / series helpers (pure) ────────────────────────────────────────────

def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-") or "x"


def _date_season(date_str: str | None) -> str | None:
    m = re.match(r"(\d{4})-(\d{2})", date_str or "")
    if not m:
        return None
    year, month = int(m.group(1)), int(m.group(2))
    s = "spring" if 1 <= month <= 5 else "summer" if 6 <= month <= 8 else "fall"
    return f"{s}-{year}"


def season_of(row: dict) -> str:
    """The season a talk belongs to: its tagged season, else date-derived."""
    return (row.get("season") or "").strip().lower() or _date_season(row.get("date")) or "unknown"


def series_of(row: dict) -> str:
    """The series (conference) a talk belongs to: its `series`, else derived from
    the venue (OCIS / INI), else the venue string."""
    s = (row.get("series") or "").strip()
    if s:
        return s
    v = (row.get("venue") or "").lower()
    if "ocis" in v:
        return "OCIS"
    if "ini" in v or "isaac newton" in v:
        return "INI"
    return (row.get("venue") or "其他").strip()


def season_sort_key(slug: str) -> tuple[int, int]:
    m = re.match(r"(winter|spring|summer|fall)-(\d{4})", slug)
    return (int(m.group(2)), _SEASON_ORDER[m.group(1)]) if m else (0, 0)


def season_label(slug: str) -> str:
    m = re.match(r"([a-z]+)-(\d{4})", slug)
    return f"{m.group(1).capitalize()} {m.group(2)}" if m else slug


def page_slug(series: str, season: str) -> str:
    return f"{_slug(series)}-{season}"


def _first_sentence(text: str, limit: int = 100) -> str:
    """A clean one-line blurb: drop markdown emphasis, take the first sentence,
    else cut at a clean boundary + '…' (never mid-`**bold**`)."""
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


# ── data loading ──────────────────────────────────────────────────────────────

def _load_catalog() -> list[dict]:
    if not CATALOG_PATH.exists():
        return []
    try:
        data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def _handcurated_rows(path: Path = TALKS_CONFIG) -> list[dict]:
    """Rows for the hand-curated talks (talks.yaml: INI etc.) — NOT the OCIS yaml.
    id is the explicit talk id; the arXiv link is the first arXiv paper."""
    if not path.exists():
        return []
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows: list[dict] = []
    for t in cfg.get("talks", []) or []:
        if not t.get("id"):
            continue
        papers = [str(p) for p in (t.get("papers") or [])]
        arxiv = next((f"https://arxiv.org/abs/{p}" for p in papers if re.match(r"^\d{4}\.\d", p)), None)
        rows.append({
            "id": t["id"], "series": series_of(t), "season": t.get("season"),
            "date": str(t["date"]) if t.get("date") is not None else None,
            "title": t.get("title"), "speaker": t.get("speaker"),
            "discussant": t.get("discussant"), "abstract": t.get("abstract"),
            "video": t.get("url"), "slides": t.get("slides"), "arxiv": arxiv,
        })
    return rows


def load_rows() -> list[dict]:
    """Unified talk rows from the OCIS catalog + hand-curated talks.yaml, each
    tagged with `id` + `series`, deduped by id."""
    rows: list[dict] = []
    for r in _load_catalog():
        rows.append({**r, "id": make_talk_id(r), "series": r.get("series") or "OCIS"})
    rows.extend(_handcurated_rows())
    seen: set[str] = set()
    out: list[dict] = []
    for r in rows:
        if r["id"] in seen:
            continue
        seen.add(r["id"])
        out.append(r)
    return out


def _load_read_index() -> dict[str, dict]:
    if not TALKS_INDEX.exists():
        return {}
    try:
        data = json.loads(TALKS_INDEX.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {e["talk_id"]: e for e in data if isinstance(e, dict) and e.get("talk_id")}


def _read_excerpt(doc_path: str | None, max_chars: int = 600) -> str:
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
    tid = row.get("id") or make_talk_id(row)
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
    return f"{label}，共 {len(entries)} 场：\n\n" + "\n\n".join(blocks)


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


def _existing_overview(*slugs: str) -> str:
    """The 导览 already on a season page (trying each slug, e.g. the new
    series-prefixed one then a legacy bare-season one), so a re-run reuses it."""
    for slug in slugs:
        if not slug:
            continue
        p = SEASONS_DIR / f"{slug}.md"
        if not p.exists():
            continue
        m = re.search(r"##\s*本季导览\s*\n+>[^\n]*\n+(.*?)\n+##\s*报告列表",
                      p.read_text(encoding="utf-8"), re.DOTALL)
        if m:
            return m.group(1).strip()
    return ""


# ── render ────────────────────────────────────────────────────────────────────

def render_season_page(slug: str, title: str, entries: list[dict], overview: str) -> Path:
    SEASONS_DIR.mkdir(parents=True, exist_ok=True)
    out = SEASONS_DIR / f"{slug}.md"
    n_read = sum(1 for e in entries if e["doc_path"])
    lines = [
        f"# {title}\n",
        f"- 共 {len(entries)} 场 · {n_read} 篇精读\n",
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
    by_slug = {e["slug"]: e for e in existing if e.get("slug")}
    for e in new_entries:
        by_slug[e["slug"]] = e
    merged = sorted(by_slug.values(),
                    key=lambda e: (e.get("series", ""), season_sort_key(e["season"])), reverse=True)
    SEASONS_INDEX.parent.mkdir(parents=True, exist_ok=True)
    SEASONS_INDEX.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    return merged


def _series_order(series: str) -> tuple[int, str]:
    # OCIS first, then alphabetical.
    return (0 if series == "OCIS" else 1, series)


def write_archive(index_entries: list[dict]) -> None:
    """Rewrite docs/all_talks.md as the index, grouped by series then season."""
    lines = [
        "# 讲座精读\n",
        "会议 / seminar 录像（OCIS、INI…）按**会议**与**季**分组。每季一页：**导览** + 全部报告"
        "（每场链到精读；网页有元数据但未精读的也列出，标「暂无精读」）。\n",
    ]
    by_series: dict[str, list[dict]] = defaultdict(list)
    for e in index_entries:
        by_series[e.get("series", "其他")].append(e)
    for series in sorted(by_series, key=_series_order):
        lines.append(f"## {series}\n")
        for e in sorted(by_series[series], key=lambda e: season_sort_key(e["season"]), reverse=True):
            blurb = f" — {e['blurb']}" if e.get("blurb") else ""
            lines.append(
                f"- [{e['label']}]({e['doc_path']}) · {e['n']} 场（{e['n_read']} 精读）{blurb}"
            )
        lines.append("")
    lines.append(f"\n---\n\nMaintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · [Source]({REPO_URL})\n")
    (DOCS / "all_talks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── run ───────────────────────────────────────────────────────────────────────

def group_by_series_season(rows: list[dict]) -> dict[tuple[str, str], list[dict]]:
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        groups[(series_of(r), season_of(r))].append(r)
    return groups


def run(
    *,
    seasons: list[str] | None = None,
    model: str | None = None,
    overview: bool = True,
    force: bool = False,
    dry_run: bool = False,
) -> list[Path]:
    rows = load_rows()
    if not rows:
        log.warning("no talks found — run `talks import-ocis` and/or fill config/talks.yaml")
        return []
    read_idx = _load_read_index()
    groups = group_by_series_season(rows)
    keys = sorted(groups, key=lambda k: (_series_order(k[0]), season_sort_key(k[1])), reverse=True)
    if seasons:
        want = {s.strip().lower() for s in seasons}
        keys = [k for k in keys if k[1] in want or page_slug(*k) in want]

    if dry_run:
        for series, season in keys:
            es = groups[(series, season)]
            log.info("  %s · %s: %d talks (%d read)", series, season, len(es),
                     sum(1 for r in es if (r.get("id") or make_talk_id(r)) in read_idx))
        return []

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
    for series, season in keys:
        slug = page_slug(series, season)
        # Dedupe talks by id within the group.
        seen: set[str] = set()
        entries: list[dict] = []
        for r in groups[(series, season)]:
            e = _entry(r, read_idx)
            if e["id"] not in seen:
                seen.add(e["id"])
                entries.append(e)
        title = f"{series} · {season_label(season)}"
        ov = ""
        if overview:
            if not force:
                # reuse: new series-prefixed slug, then the legacy bare-season slug
                ov = _existing_overview(slug, season if series == "OCIS" else "")
            if not ov:
                try:
                    ov = generate_overview(_get_client(), entries, title, model=model)
                except Exception as e:  # noqa: BLE001
                    log.warning("overview failed for %s: %s", slug, e)
        page = render_season_page(slug, title, entries, ov)
        written.append(page)
        index_entries.append({
            "slug": slug, "series": series, "season": season,
            "label": season_label(season), "n": len(entries),
            "n_read": sum(1 for e in entries if e["doc_path"]),
            "doc_path": f"talks/seasons/{page.name}", "blurb": _first_sentence(ov),
        })
        log.info("wrote %s (%d talks, %d read)", page, len(entries), index_entries[-1]["n_read"])

    # On a full refresh, drop stale season pages (e.g. legacy bare-season names).
    if seasons is None:
        keep = {p.name for p in written}
        for f in SEASONS_DIR.glob("*.md"):
            if f.name not in keep:
                f.unlink()
                log.info("removed stale season page %s", f.name)

    if index_entries:
        merged = _write_index(index_entries)
        write_archive(merged)
    return written
