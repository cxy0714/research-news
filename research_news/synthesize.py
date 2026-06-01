"""Stage 2 of the problem-finding engine: cross-paper synthesis.

Aggregates a topic slice of the journal deep-read corpus and surfaces, per
sub-direction, the signals that only appear *across* papers: recurring open
problems (flagged by >=2 independent papers), tensions, and arsenal-shaped
transfer gaps. The LLM mines and groups — it never scores or ranks; every
finding cites the papers it came from so recurrence is auditable.

Run: python -m research_news.synthesize [--topic causal_inference] [--since 2026-01-01]

Reuses the deep-read notes (docs/deep_reads/) and the structured extractions
from extract_problems.py (data/open_problems.jsonl). Self-contained: does not
touch the daily / journal pipelines.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

from . import extract_problems as ep
from .llm.prompts import SYNTHESIS_SYSTEM, TOPIC_LABELS_ZH

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger("research_news")


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_") or "unknown"

DEEP_READS_INDEX = Path("data/deep_reads_index.json")
DOCS_DIR = Path("docs")
SYNTHESIS_DIR = DOCS_DIR / "synthesis"
SYNTHESIS_INDEX = Path("data/synthesis_index.json")
DEFAULT_MODEL = os.environ.get("SYNTHESIS_MODEL", os.environ.get("DAILY_MODEL", "glm-5.1"))
MIN_PAPERS = 3

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"
JOURNALS_CONFIG = Path("config/journals.yaml")


def _norm_venue(s: str | None) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def load_journal_groups() -> dict:
    """Return the `groups` mapping from config/journals.yaml ({} if missing)."""
    if not JOURNALS_CONFIG.exists():
        return {}
    import yaml
    cfg = yaml.safe_load(JOURNALS_CONFIG.read_text(encoding="utf-8")) or {}
    return cfg.get("groups", {}) or {}


def resolve_venue_filter(
    journals: list[str] | None, groups: list[str] | None
) -> tuple[set[str] | None, str, str]:
    """Resolve --journal / --group into (allowed_venues, scope_label, scope_slug).

    allowed_venues is a set of normalized full venue names, or None for "no
    filter / all journals". journals match by short name or full name (or
    substring); groups match group keys in config/journals.yaml.
    """
    groups_cfg = load_journal_groups()
    # Map any normalized name (short OR full) → both its forms, since the corpus
    # stores venue inconsistently (e.g. "JMLR" short, "Annals of Statistics" full).
    name_to_forms: dict[str, set[str]] = {}
    for g in groups_cfg.values():
        for j in g.get("journals", []):
            forms = {_norm_venue(j["short"]), _norm_venue(j["full"])}
            for f in forms:
                name_to_forms[f] = forms

    allowed: set[str] = set()
    labels: list[str] = []
    for gname in groups or []:
        key = gname.strip().lower()
        g = groups_cfg.get(key)
        if not g:
            log.warning("unknown journal group %r (have: %s)", gname, ", ".join(groups_cfg))
            continue
        for j in g.get("journals", []):
            allowed.add(_norm_venue(j["short"]))
            allowed.add(_norm_venue(j["full"]))
        labels.append(key)
    for jn in journals or []:
        k = _norm_venue(jn)
        forms = name_to_forms.get(k)
        if forms:
            allowed.update(forms); labels.append(jn)
        else:  # substring fallback against known names
            hits = {f for f in name_to_forms if k and len(k) > 4 and (k in f or f in k)}
            if hits:
                for h in hits:
                    allowed.update(name_to_forms[h])
                labels.append(jn)
            else:
                log.warning("unknown journal %r", jn)

    if not allowed:
        return None, "全部期刊", "all"
    return allowed, " + ".join(labels), (_slug("-".join(labels)) or "scope")


def _venue_allowed(venue: str | None, allowed: set[str] | None) -> bool:
    if allowed is None:
        return True
    vn = _norm_venue(venue)
    # Exact match on any form (short codes), or substring match for long full names.
    return any(a == vn or (len(a) > 8 and (a in vn or vn in a)) for a in allowed)


def load_deep_reads(run_type: str | None = "journals") -> list[dict]:
    """Load deep-read index entries (optionally filtered by run_type) with bodies."""
    if not DEEP_READS_INDEX.exists():
        log.warning("no deep-read index at %s", DEEP_READS_INDEX)
        return []
    entries = json.loads(DEEP_READS_INDEX.read_text(encoding="utf-8"))
    out: list[dict] = []
    for e in entries:
        if run_type and e.get("run_type") != run_type:
            continue
        body_path = DOCS_DIR / e.get("doc_path", "")
        if not body_path.exists():
            continue
        e = dict(e)
        e["body"] = body_path.read_text(encoding="utf-8")
        out.append(e)
    return out


def survey_excerpt(body: str, max_chars: int = 1500) -> str:
    """Pull the '一、领域脉络/核心问题' section from a deep-read note."""
    # Body starts at "### 一、..."; grab up to the next "### 二".
    m = re.search(r"###\s*一[、,].*?(?=\n###\s*二[、,])", body, re.DOTALL)
    chunk = m.group(0) if m else body
    chunk = re.sub(r"\s+", " ", chunk).strip()
    return chunk[:max_chars]


def _fw_items(future_work: list) -> list[str]:
    """Substantive future-work items only (drop boilerplate)."""
    out = []
    for fw in future_work or []:
        if isinstance(fw, dict):
            if not fw.get("boilerplate"):
                out.append(str(fw.get("item", "")).strip())
        elif fw:
            out.append(str(fw).strip())
    return [x for x in out if x]


def _paper_block(k: int, entry: dict, row: dict) -> str:
    """Render one numbered paper block for the synthesis prompt."""
    venue = entry.get("venue") or ""
    vol = f" {entry['volume']}" if entry.get("volume") else ""
    iss = f"({entry['issue']})" if entry.get("issue") else ""
    head = f"[{k}] {entry.get('title','')} — {venue}{vol}{iss} {entry.get('date','')}".strip()
    lines = [head]
    if row.get("direction"):
        lines.append(f"  方向: {row['direction']}")

    def _join(label: str, key: str):
        vals = [str(x).strip() for x in (row.get(key) or []) if str(x).strip()]
        if vals:
            lines.append(f"  {label}: " + "；".join(vals))

    _join("开放问题", "open_questions")
    _join("作者承认的局限", "stated_limitations")
    fw = _fw_items(row.get("future_work"))
    if fw:
        lines.append("  future work(实打实): " + "；".join(fw))
    _join("结论偏窄", "narrow_conclusions")
    _join("被引张力", "cited_tensions")
    _join("迁移线索", "transfer_hints")
    excerpt = survey_excerpt(entry.get("body", ""))
    if excerpt:
        lines.append(f"  综述摘录: {excerpt}")
    return "\n".join(lines)


def build_user_message(topic: str, entries: list[dict], rows: dict[str, dict]) -> str:
    label = TOPIC_LABELS_ZH.get(topic, topic)
    blocks = [
        _paper_block(k, e, rows.get(e["paper_id"], {}))
        for k, e in enumerate(entries, 1)
    ]
    return (
        f"子方向: {label}（{topic}）\n"
        f"共 {len(entries)} 篇期刊论文。\n\n"
        + "\n\n".join(blocks)
    )


def synthesize_topic(
    client: "SJTUClient",
    topic: str,
    entries: list[dict],
    rows: dict[str, dict],
    *,
    model: str | None = None,
) -> str:
    user = build_user_message(topic, entries, rows)
    return client.chat(
        [
            {"role": "system", "content": SYNTHESIS_SYSTEM},
            {"role": "user", "content": user},
        ],
        model=model,
        max_tokens=10000,
    )


def _render_page(
    topic: str, entries: list[dict], content: str, run_date: date,
    *, scope_label: str = "全部期刊", scope_slug: str = "all",
) -> Path:
    SYNTHESIS_DIR.mkdir(parents=True, exist_ok=True)
    label = TOPIC_LABELS_ZH.get(topic, topic)
    out = SYNTHESIS_DIR / f"{run_date.isoformat()}-{scope_slug}-{_slug(topic)}.md"
    src_lines = [
        f"- [{k}] {e.get('title','')} — {e.get('venue') or ''} ({e.get('date','')})"
        for k, e in enumerate(entries, 1)
    ]
    lines = [
        f"# 跨篇综合 · {label}\n",
        f"**子方向**: {label}  ",
        f"**期刊范围**: {scope_label}  ",
        f"**聚合期刊论文数**: {len(entries)}  ",
        f"**生成日期**: {run_date.isoformat()}  ",
        "\n> 本页由跨篇综合自动生成：从近期期刊精读里归纳反复出现的开放问题、张力与迁移空位。"
        "**不打分、不排名**，每条点名来源论文 [k]，供你自己判断。\n",
        "---\n",
        content if content else "*（综合失败，请查看日志）*",
        "\n---\n\n### 本页聚合的论文\n",
        "\n".join(src_lines),
        f"\n\n---\n\nMaintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · [Source]({REPO_URL})\n",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def _update_index(new_entries: list[dict]) -> None:
    existing = []
    if SYNTHESIS_INDEX.exists():
        try:
            existing = json.loads(SYNTHESIS_INDEX.read_text(encoding="utf-8"))
        except Exception:
            existing = []
    # De-dup by (date, scope, topic): newest run wins.
    def _key(e: dict) -> tuple:
        return (e["date"], e.get("scope", "all"), e["topic"])
    by_key = {_key(e): e for e in existing}
    for e in new_entries:
        by_key[_key(e)] = e
    merged = sorted(by_key.values(), key=_key, reverse=True)
    SYNTHESIS_INDEX.parent.mkdir(parents=True, exist_ok=True)
    SYNTHESIS_INDEX.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    _write_archive(merged)


def _write_archive(entries: list[dict]) -> None:
    """Refresh docs/all_synthesis.md (linked from the site nav)."""
    lines = [
        "# 选题综合\n",
        "跨篇综合：把同一子方向近期的期刊精读放一起，归纳**反复出现的开放问题、"
        "张力与迁移空位**。不打分、不排名，每条点名来源论文，供你自己判断选题。\n",
    ]
    cur_date = None
    for e in entries:
        if e["date"] != cur_date:
            cur_date = e["date"]
            lines.append(f"\n## {cur_date}\n")
        doc_path = e.get("doc_path")
        if not doc_path:
            continue
        stem = Path(doc_path).stem
        scope = e.get("scope_label", "")
        scope_tag = f" · {scope}" if scope and scope != "全部期刊" else ""
        lines.append(
            f"- [{e.get('topic_label', e['topic'])}（{e.get('n_papers','?')} 篇）{scope_tag}]"
            f"(synthesis/{stem}.md)"
        )
    (DOCS_DIR / "all_synthesis.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(
    *,
    topic_filter: str | None = None,
    since: str | None = None,
    min_papers: int = MIN_PAPERS,
    model: str | None = None,
    journals: list[str] | None = None,
    groups: list[str] | None = None,
    dry_run: bool = False,
) -> list[Path]:
    model = model or DEFAULT_MODEL
    run_date = date.today()

    allowed, scope_label, scope_slug = resolve_venue_filter(journals, groups)

    entries = load_deep_reads(run_type="journals")
    if since:
        entries = [e for e in entries if (e.get("date") or "") >= since]
    if allowed is not None:
        entries = [e for e in entries if _venue_allowed(e.get("venue"), allowed)]
    log.info("loaded %d journal deep-reads (期刊范围: %s)", len(entries), scope_label)

    # Group by topic.
    by_topic: dict[str, list[dict]] = {}
    for e in entries:
        by_topic.setdefault(e.get("topic") or "other", []).append(e)

    topics = [topic_filter] if topic_filter else sorted(
        by_topic, key=lambda t: len(by_topic[t]), reverse=True
    )

    if dry_run:
        for t in topics:
            log.info("  %s: %d papers%s", t, len(by_topic.get(t, [])),
                     "" if len(by_topic.get(t, [])) >= min_papers else "  (below min, skip)")
        return []

    from dotenv import load_dotenv
    from .llm.sjtu_client import SJTUClient
    load_dotenv()
    client = SJTUClient()

    # Stage 1: make sure every paper we will aggregate has a structured extraction.
    to_extract = [e for t in topics for e in by_topic.get(t, [])]
    rows = ep.backfill(client, to_extract, model=model, run_date=run_date)

    # Stage 2: synthesize each topic with enough papers.
    written: list[Path] = []
    index_entries: list[dict] = []
    for t in topics:
        group = by_topic.get(t, [])
        if len(group) < min_papers:
            log.info("skip %s: only %d papers (< %d)", t, len(group), min_papers)
            continue
        group = sorted(group, key=lambda e: e.get("date") or "", reverse=True)
        log.info("synthesizing %s over %d papers ...", t, len(group))
        try:
            content = synthesize_topic(client, t, group, rows, model=model)
        except Exception as e:  # noqa: BLE001
            log.warning("synthesis failed for %s: %s", t, e)
            continue
        page = _render_page(t, group, content, run_date,
                            scope_label=scope_label, scope_slug=scope_slug)
        written.append(page)
        index_entries.append({
            "date": run_date.isoformat(),
            "topic": t,
            "topic_label": TOPIC_LABELS_ZH.get(t, t),
            "scope": scope_slug,
            "scope_label": scope_label,
            "n_papers": len(group),
            "doc_path": f"synthesis/{page.name}",
        })
        log.info("wrote %s", page)

    if index_entries:
        _update_index(index_entries)
    return written


def _split(values: list[str] | None) -> list[str]:
    """Flatten repeated + comma-separated CLI values: --journal AoS,JASA --journal JRSSB."""
    out: list[str] = []
    for v in values or []:
        out.extend(part.strip() for part in v.split(",") if part.strip())
    return out


def _print_journals() -> None:
    groups = load_journal_groups()
    if not groups:
        print("no config/journals.yaml found")
        return
    print("可用期刊组 (--group) 与期刊 (--journal，用 short 名)：\n")
    for key, g in groups.items():
        print(f"  --group {key}    # {g.get('label', key)}")
        shorts = ", ".join(j["short"] for j in g.get("journals", []))
        print(f"      journals: {shorts}\n")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ap = argparse.ArgumentParser(
        description="Cross-paper synthesis over journal deep-reads (problem-finding engine).")
    ap.add_argument("--topic", help="only this topic (e.g. causal_inference)")
    ap.add_argument("--journal", action="append", default=[],
                    help="scope to these journals (short or full name; comma-separated "
                         "or repeat the flag). E.g. --journal AoS,JASA")
    ap.add_argument("--group", action="append", default=[],
                    help="scope to these journal groups from config/journals.yaml "
                         "(e.g. --group core). Comma-separated or repeat the flag.")
    ap.add_argument("--since", help="only deep-reads on/after this ISO date")
    ap.add_argument("--min-papers", type=int, default=MIN_PAPERS)
    ap.add_argument("--model", default=None)
    ap.add_argument("--list-journals", action="store_true",
                    help="print available journal groups + journals, then exit")
    ap.add_argument("--dry-run", action="store_true", help="show topic counts, no LLM")
    args = ap.parse_args()

    if args.list_journals:
        _print_journals()
        return

    paths = run(
        topic_filter=args.topic, since=args.since, min_papers=args.min_papers,
        model=args.model, journals=_split(args.journal), groups=_split(args.group),
        dry_run=args.dry_run,
    )
    print(f"wrote {len(paths)} synthesis page(s)")


if __name__ == "__main__":
    main()
