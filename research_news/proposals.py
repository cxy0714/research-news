"""选题提案引擎 — turn the accumulated deep-read corpus into actionable proposals.

Replaces the old cross-paper synthesis at /research-news/all_synthesis/. Three
things changed relative to synthesize.py:

1. **Candidate pool includes taste.** The pool is "score >= 8 OR favorited",
   over *all* run types (journals + daily + manual), not journals-only. The 196
   hand-picked favorites are the strongest signal of what the researcher
   actually wants to work on, and the old engine ignored them entirely.

2. **No LLM extraction stage.** The deep-read notes already state open problems
   as grounded prose ("扎根点：Remark 5"). A deterministic header-prefix slicer
   keeps the five gap-bearing sections — measured over 600 notes: 17% of the
   characters, 83% coverage of 开放问题, grounding quotes preserved verbatim.
   The old stage-1 LLM->JSON extraction cost one call per paper (1374 pending)
   and threw the quotes away.

3. **Output is a proposal, not a diagnosis.** Each card carries a submittable
   title, a claim naming a mathematical object, the minimal kernel to attack
   first, >=2 independent papers grounding the gap, arsenal match, risks, and
   concrete first-week actions.

Ordering is by *auditable evidence count* (how many independent papers name the
gap), never by an LLM quality score — same principle as the deep-read prompts.

Run:
  python -m research_news.proposals --dry-run       # pool + front sizes, no LLM
  python -m research_news.proposals --build-fronts  # (re)build config/fronts.yaml
  python -m research_news.proposals                 # generate + render
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

if TYPE_CHECKING:
    from .llm.sjtu_client import SJTUClient

log = logging.getLogger("research_news")

DOCS_DIR = Path("docs")
DEEP_READS_INDEX = Path("data/deep_reads_index.json")
HIGHLIGHTS = Path("data/highlights.json")
FAVORITES = DOCS_DIR / "data/favorites_public.json"
FRONTS_CONFIG = Path("config/fronts.yaml")
INTERESTS_CONFIG = Path("config/interests.yaml")
PROPOSALS_DATA = Path("data/proposals.json")
PROPOSALS_DIR = DOCS_DIR / "proposals"
OVERVIEW_PAGE = DOCS_DIR / "all_synthesis.md"

HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"

DEFAULT_MODEL = os.environ.get(
    "PROPOSALS_MODEL", os.environ.get("DEEP_READ_MODEL", "deepseek-reasoner")
)

# Pool gates.
POOL_MIN_SCORE = 8.0
SEED_MIN_SCORE = 9.0      # papers that get to *define* fronts
FRONT_MIN_PAPERS = 6      # fronts thinner than this are dropped
FRONT_MAX_PAPERS = 30     # papers fed to the proposal call, favorites first
MAX_FRONTS = 14           # keep the reading load survivable (~2-3 proposals each)


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_").lower() or "unknown"


# ---------------------------------------------------------------- gap slicing

# The deep-read format drifted over four months, so match on header *prefix*,
# not exact title. Measured header variants in the corpus include
# "四、开放问题", "四、开放问题（点到为止）", "四、开放问题（扎根具体语句）",
# "⚠️ 作者的 framing" / "作者的framing" / "作者的Framing".
GAP_SECTIONS: tuple[tuple[str, str], ...] = (
    ("core", r"核心问题|在追问的核心问题|瓶颈"),
    ("framing", r"作者的\s*framing"),
    ("tension", r"^张力"),
    ("narrow", r"结论是否比证明窄"),
    ("open", r"开放问题"),
)

GAP_LABELS = {
    "core": "方向的核心问题与瓶颈",
    "framing": "作者的 framing / 该被引却没被引",
    "tension": "被引工作之间的张力",
    "narrow": "结论比证明窄的地方",
    "open": "作者留下的开放问题",
}


# Sentences in a deep-read note that address the researcher directly, or reason
# about his arsenal, are the *note author's* commentary — not something the
# paper says. 55% of gap slices contain such text. Left unmarked, the proposal
# call quotes it back as if it were paper evidence, which makes the evidence
# circular (an LLM citing an earlier LLM's suggestion as proof the gap is real).
_COMMENTARY_RE = re.compile(
    r"您|研究者|武器库|专长|very_familiar|moderately_familiar|技术武器"
)


def _mark_commentary(text: str) -> str:
    """Tag lines that are note-commentary rather than paper content."""
    out = []
    for line in text.split("\n"):
        if line.strip() and _COMMENTARY_RE.search(line):
            out.append("（笔记作者的旁注，非论文内容）" + line)
        else:
            out.append(line)
    return "\n".join(out)


def gap_slice(body: str, *, max_chars: int = 4000) -> str:
    """Pull the gap-bearing sections out of a deep-read note.

    Returns a labelled concatenation of the five sections that carry
    problem-finding signal, dropping the survey / minimal-kernel / what-the-
    paper-did bulk. Grounding quotes inside those sections survive verbatim —
    that is the whole point, since they are what makes a proposal auditable.

    Lines that talk *to* the researcher get tagged as commentary so the
    proposal call cannot mistake them for what the paper itself claims.
    """
    chunks: list[str] = []
    for match in re.finditer(r"^(#{3,4})\s*(.+)$", body, re.M):
        level, title = len(match.group(1)), match.group(2)
        for key, pattern in GAP_SECTIONS:
            if not re.search(pattern, title):
                continue
            start = match.end()
            nxt = re.search(r"^#{1,%d}\s" % level, body[start:], re.M)
            end = start + (nxt.start() if nxt else len(body) - start)
            text = body[start:end].strip()
            # Strip the page footer if the section ran to end-of-file.
            text = re.split(r"\n---\s*\n\s*Maintained by", text)[0].strip()
            if text:
                chunks.append(f"[{GAP_LABELS[key]}] {_mark_commentary(text)}")
            break
    out = "\n".join(chunks)
    return out[:max_chars]


# ------------------------------------------------------------- candidate pool


def _load_json(path: Path, default):
    if not path.exists():
        log.warning("missing %s", path)
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        log.warning("could not parse %s: %s", path, exc)
        return default


def load_favorites() -> dict[str, dict]:
    """{paper_id: favorite entry} from the public favorites snapshot."""
    rows = _load_json(FAVORITES, [])
    return {r["paper_id"]: r for r in rows if r.get("paper_id")}


def load_highlights() -> dict[str, dict]:
    rows = _load_json(HIGHLIGHTS, [])
    return {r["paper_id"]: r for r in rows if r.get("paper_id")}


def load_latest_deep_reads() -> dict[str, dict]:
    """{paper_id: newest deep-read index entry}, all run types."""
    best: dict[str, dict] = {}
    for entry in _load_json(DEEP_READS_INDEX, []):
        pid = entry.get("paper_id")
        if not pid:
            continue
        prev = best.get(pid)
        if prev is None or (entry.get("date") or "") > (prev.get("date") or ""):
            best[pid] = entry
    return best


def build_pool(*, min_score: float = POOL_MIN_SCORE, since: str | None = None) -> list[dict]:
    """Papers eligible to support a proposal: high-scoring OR favorited.

    Favorites bypass the score gate on purpose — a hand-picked paper is a
    stronger statement of research intent than any LLM score, and several
    favorites sit at score 4-7 (the gateway-reading rubrics score low by
    design).
    """
    deep_reads = load_latest_deep_reads()
    highlights = load_highlights()
    favorites = load_favorites()

    pool: list[dict] = []
    for pid, entry in deep_reads.items():
        hl = highlights.get(pid, {})
        score = hl.get("score")
        score = float(score) if isinstance(score, (int, float)) else 0.0
        is_fav = pid in favorites
        if not is_fav and score < min_score:
            continue
        if since and (entry.get("date") or "") < since:
            continue
        pool.append({
            "paper_id": pid,
            "title": hl.get("title") or entry.get("title") or pid,
            "venue": hl.get("venue") or entry.get("venue") or "",
            "date": entry.get("date") or "",
            "published": hl.get("published") or "",
            "url": hl.get("url") or "",
            "topic": entry.get("topic") or hl.get("topic") or "other",
            "score": score,
            "techniques": [str(t) for t in (hl.get("key_techniques") or [])],
            "favorite": is_fav,
            "note": (favorites.get(pid, {}).get("note") or "").strip(),
            "doc_path": entry.get("doc_path") or "",
        })
    pool.sort(key=lambda p: (not p["favorite"], -p["score"], p["title"]))
    return pool


def match_text(paper: dict) -> str:
    """Lowercased haystack used for deterministic front assignment."""
    return (paper["title"] + " | " + " ".join(paper["techniques"])).lower()


# ------------------------------------------------------------------- fronts


def load_fronts(path: Path = FRONTS_CONFIG) -> list[dict]:
    """Read the front definitions (hand-editable YAML written by --build-fronts)."""
    if not path.exists():
        return []
    import yaml
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    fronts = cfg.get("fronts") or []
    out = []
    for f in fronts:
        if not f.get("key") or not f.get("label"):
            continue
        out.append({
            "key": str(f["key"]),
            "label": str(f["label"]),
            "scope": str(f.get("scope") or ""),
            "topic": str(f.get("topic") or ""),
            "keywords": [str(k).lower() for k in (f.get("keywords") or [])],
            "techniques": [str(k).lower() for k in (f.get("techniques") or [])],
        })
    return out


def keyword_hits(paper: dict, front: dict) -> int:
    """How many of the front's needles this paper matches."""
    hay = match_text(paper)
    needles = front["keywords"] + front["techniques"]
    return sum(1 for n in needles if n and n in hay)


def assign_papers(
    pool: list[dict], fronts: list[dict], *, broad_fraction: float = 0.10,
) -> dict[str, list[dict]]:
    """Attach pool papers to fronts by keyword / technique substring match.

    A paper may land in several fronts — research fronts genuinely overlap
    (a two-sample-IV paper is both data fusion and IV), and forcing a single
    assignment would hide exactly the cross-front papers that make the best
    proposals. Deterministic and auditable: no LLM, no embeddings.

    Fronts that sweep up more than ``broad_fraction`` of the pool get tightened
    to papers matching >=2 needles. Some keywords are unavoidably generic
    ("influence function" alone hits 7.7% of the pool), and a front matching a
    sixth of the corpus is a topic bucket, not a research front — it produces
    exactly the vague synthesis this engine exists to replace.
    """
    threshold = max(1, int(len(pool) * broad_fraction))
    buckets: dict[str, list[dict]] = {}
    for front in fronts:
        hits = [(p, keyword_hits(p, front)) for p in pool]
        matched = [(p, n) for p, n in hits if n > 0]
        if len(matched) > threshold:
            tightened = [(p, n) for p, n in matched if n >= 2]
            if len(tightened) >= FRONT_MIN_PAPERS:
                log.info(
                    "front %s matched %d papers (>%d); tightened to %d "
                    "by requiring >=2 keyword hits",
                    front["key"], len(matched), threshold, len(tightened),
                )
                matched = tightened
        buckets[front["key"]] = [p for p, _ in matched]
    return buckets


def dedupe_fronts(
    fronts: list[dict], buckets: dict[str, list[dict]], *, max_jaccard: float = 0.5,
) -> list[dict]:
    """Drop fronts that are near-duplicates of a front we already keep.

    Clustering runs once per topic bucket, so the same front gets rediscovered
    from several angles ("doubly robust efficiency" from causal_inference and
    "semiparametric efficiency / influence function" from nonparam_semipara
    shared 73% of their papers). Generating proposals for both burns calls and
    hands back the same ideas twice.

    Keep-order: more favorites first (that is the researcher's own signal),
    then more papers, then key for stability. No LLM judgement involved.
    """
    ranked = sorted(
        fronts,
        key=lambda f: (
            -sum(1 for p in buckets.get(f["key"], []) if p["favorite"]),
            -len(buckets.get(f["key"], [])),
            f["key"],
        ),
    )
    kept: list[dict] = []
    kept_sets: list[set[str]] = []
    for front in ranked:
        ids = {p["paper_id"] for p in buckets.get(front["key"], [])}
        if not ids:
            continue
        dup_of = None
        for other, other_ids in zip(kept, kept_sets):
            union = ids | other_ids
            if union and len(ids & other_ids) / len(union) >= max_jaccard:
                dup_of = other["key"]
                break
        if dup_of:
            log.info("drop front %s: >=%.0f%% overlap with %s",
                     front["key"], max_jaccard * 100, dup_of)
            continue
        kept.append(front)
        kept_sets.append(ids)
    return kept


# Topics that config/interests.yaml lists under primary_interests. The three
# secondary ones (astrostats / econ_theory / epidemiology) are read as gateway
# material, and their rubrics deliberately score on accessibility rather than
# transferability — so they should not outrank a primary front when we cap.
PRIMARY_TOPICS = frozenset({
    "causal_inference", "hypothesis_testing", "high_dim_rmt",
    "nonparam_semipara", "efficiency_dml", "stat_computing", "other",
})

# Interest areas from config/interests.yaml (primary_interests +
# technical_arsenal), each with the phrasings that show up in front keywords.
# Fronts are ranked by how many *distinct areas* they touch, not by raw anchor
# hits: front scopes are Chinese and keywords are English, so one area often
# has several near-synonyms ("computational phase transition" vs
# "computational-statistical tradeoff") and counting them would just reward
# whichever front the clustering call happened to describe more verbosely.
#
# Why not favorite count alone: the statistical-computational rubric in
# interests.yaml explicitly calls the researcher an OUTSIDER there, so those
# fronts carry few favorites by construction — not by lack of interest.
ARSENAL_AREAS: dict[str, tuple[str, ...]] = {
    "higher_order": (
        "higher-order influence", "higher order influence", "hoif",
        "higher-order u-statistic", "higher-order efficien",
        "second-order efficien", "higher-order debiased", "higher-order cumulant",
        "u-statistic", "u-process", "hoeffding decomposition", "v-statistic",
        "高阶影响函数", "高阶u", "u统计量", "高阶去偏",
    ),
    "tensor_compute": (
        "tensor contraction", "einsum", "treewidth", "cumulant tensor",
        "tensor decomposition", "gram matrix",
        "张量", "累积量", "gram 矩阵",
    ),
    "minimax": (
        "minimax", "lower bound", "phase transition", "optimal rate",
        "convergence rate", "le cam", "fano",
        "极小极大", "下界", "相变", "收敛率", "最优率",
    ),
    "semipara_efficiency": (
        "semiparametric efficiency", "efficient influence function",
        "influence function", "debiased", "cross-fitting", "neyman orthogonal",
        "structure-agnostic", "double robust", "doubly robust", "riesz",
        "tangent space", "targeted minimum loss",
        "半参数效率", "影响函数", "去偏", "双稳健", "多重稳健", "切空间", "效率界",
    ),
    "stat_comp_tradeoff": (
        "low-degree", "low coordinate degree", "computational threshold",
        "statistical-computational", "computational-statistical",
        "computational phase transition", "information-computation",
        "sq lower bound", "planted", "average-case hardness",
        "polynomial-time",
        "低度多项式", "计算-统计", "统计-计算", "计算阈值", "多项式时间",
    ),
    "high_dim_rmt": (
        "random matrix", "marchenko-pastur", "high-dimensional asymptotic",
        "spiked", "stieltjes", "eigenvalue", "eigenvector", "spectral",
        "universality",
        "随机矩阵", "高维渐近", "尖峰", "特征值", "特征向量", "谱",
    ),
    "nonparametric": (
        "nonparametric", "sieve", "rkhs", "kernel", "smoothing", "manifold",
        "非参数", "核", "光滑", "流形",
    ),
    "causal_identification": (
        "identification", "proximal causal", "negative control",
        "instrumental variable", "mediation", "interference", "transportability",
        "partial identification", "sensitivity analysis",
        "识别", "近端因果", "负对照", "工具变量", "中介", "干扰", "可迁移",
        "部分识别", "敏感性分析", "因果参数", "处理效应",
    ),
    "inverse_m_est": (
        "inverse problem", "m-estimation", "empirical process",
        "反问题", "m估计", "m-估计", "经验过程",
    ),
}

# Fronts are bucketed into affinity bands, then ordered by favorites *inside*
# each band. Strict affinity ordering would let a 2-favorite front outrank a
# 23-favorite one on a one-area difference; bands keep the arsenal signal
# dominant without letting it erase the researcher's own picks.
AFFINITY_BANDS: tuple[int, ...] = (4, 3, 2)


def affinity_band(affinity: int) -> int:
    for i, floor in enumerate(AFFINITY_BANDS):
        if affinity >= floor:
            return i
    return len(AFFINITY_BANDS)


def front_affinity(front: dict) -> int:
    """How many distinct arsenal *areas* this front touches (0-9)."""
    hay = (front["label"] + " " + front["scope"] + " " +
           " ".join(front["keywords"] + front["techniques"])).lower()
    return sum(
        1 for terms in ARSENAL_AREAS.values() if any(t in hay for t in terms)
    )


def front_stats(front: dict, papers: list[dict]) -> dict:
    return {
        "key": front["key"],
        "label": front["label"],
        "scope": front["scope"],
        "n_papers": len(papers),
        "n_favorites": sum(1 for p in papers if p["favorite"]),
    }


def select_for_prompt(papers: list[dict], *, limit: int = FRONT_MAX_PAPERS) -> list[dict]:
    """Favorites first, then highest score, then most recent — capped."""
    ranked = sorted(
        papers,
        key=lambda p: (not p["favorite"], -p["score"], p["date"]),
        reverse=False,
    )
    return ranked[:limit]


# --------------------------------------------------- stage B: build the fronts


def _parse_json_object(raw: str) -> dict | None:
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text).strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if not m:
            return None
        try:
            return json.loads(m.group(0))
        except Exception:
            return None


def build_fronts(
    client: "SJTUClient", pool: list[dict], *, model: str | None = None,
    seed_min_score: float = SEED_MIN_SCORE,
) -> list[dict]:
    """Cluster the pool into fine-grained research fronts, one LLM call per topic.

    Only *seed* papers (favorited or score >= 9) get to define fronts — the
    full pool is too big for one context and the marginal score-8 paper does
    not tell us where the research fronts are. Assignment of the whole pool
    happens deterministically afterwards, from the keywords the LLM emits.
    """
    from .llm.prompts import FRONT_CLUSTER_SYSTEM, TOPIC_LABELS_ZH

    seeds: dict[str, list[dict]] = {}
    for paper in pool:
        if paper["favorite"] or paper["score"] >= seed_min_score:
            seeds.setdefault(paper["topic"], []).append(paper)

    fronts: list[dict] = []
    for topic, papers in sorted(seeds.items(), key=lambda kv: -len(kv[1])):
        if len(papers) < FRONT_MIN_PAPERS:
            log.info("skip topic %s: only %d seed papers", topic, len(papers))
            continue
        label = TOPIC_LABELS_ZH.get(topic, topic)
        lines = [
            f"{'★' if p['favorite'] else ' '} {p['title']} | "
            + ", ".join(p["techniques"][:6])
            for p in papers
        ]
        user = (
            f"粗方向：{label}（{topic}）\n"
            f"共 {len(papers)} 篇，其中 ★ 收藏 "
            f"{sum(1 for p in papers if p['favorite'])} 篇。\n\n"
            + "\n".join(lines)
        )
        log.info("clustering %s over %d seed papers ...", topic, len(papers))
        try:
            raw = client.chat(
                [{"role": "system", "content": FRONT_CLUSTER_SYSTEM},
                 {"role": "user", "content": user}],
                model=model, max_tokens=4000,
            )
        except Exception as exc:  # noqa: BLE001
            log.warning("front clustering failed for %s: %s", topic, exc)
            continue
        obj = _parse_json_object(raw) or {}
        for f in obj.get("fronts") or []:
            key, lab = f.get("key"), f.get("label")
            kws = [str(k).lower().strip() for k in (f.get("keywords") or []) if str(k).strip()]
            if not key or not lab or not kws:
                continue
            fronts.append({
                "key": _slug(f"{topic}_{key}"),
                "label": str(lab),
                "scope": str(f.get("scope") or ""),
                "topic": topic,
                "keywords": kws,
                "techniques": [],
            })
    return fronts


def write_fronts_config(fronts: list[dict], path: Path = FRONTS_CONFIG) -> None:
    """Persist front definitions as hand-editable YAML.

    Written once and then reused: the clustering call is non-deterministic, so
    freezing the result keeps proposal runs comparable across dates and lets
    the owner correct a bad front by editing keywords instead of re-rolling.
    """
    import yaml
    path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# 研究战线定义 — 提案的分组单位。\n"
        "# 由 `python -m research_news.proposals --build-fronts` 生成，"
        "之后可手改：\n"
        "#   - keywords 决定哪些论文进这条战线（对标题 + key_techniques 做小写子串匹配）\n"
        "#   - 想砍掉一条战线，直接删掉它，或把 keywords 清空\n"
        "#   - 想新开一条，照抄格式手写一条即可（key 必须唯一）\n"
        "# 重新生成会覆盖手改，改完记得提交。\n\n"
    )
    body = yaml.safe_dump(
        {"fronts": fronts}, allow_unicode=True, sort_keys=False, width=100
    )
    path.write_text(header + body, encoding="utf-8")
    log.info("wrote %s (%d fronts)", path, len(fronts))


# ---------------------------------------------- stage D: generate the proposals


def paper_block(k: int, paper: dict, *, gap_max_chars: int = 4000) -> str:
    """One numbered paper block for the proposal prompt: metadata + gap slice."""
    star = "★收藏 " if paper["favorite"] else ""
    head = f"[{k}] {star}{paper['title']}"
    meta = " · ".join(x for x in (paper["venue"], paper["date"]) if x)
    lines = [head + (f"\n    ({meta})" if meta else "")]
    if paper["note"]:
        lines.append(f"    你的笔记: {paper['note']}")
    body_path = DOCS_DIR / paper["doc_path"] if paper["doc_path"] else None
    if body_path and body_path.exists():
        gap = gap_slice(body_path.read_text(encoding="utf-8"), max_chars=gap_max_chars)
        if gap:
            lines.append("    " + gap.replace("\n", "\n    "))
    return "\n".join(lines)


def build_proposal_message(front: dict, papers: list[dict]) -> str:
    blocks = [paper_block(k, p) for k, p in enumerate(papers, 1)]
    n_fav = sum(1 for p in papers if p["favorite"])
    return (
        f"研究战线：{front['label']}\n"
        f"战线范围：{front['scope']}\n"
        f"本战线论文 {len(papers)} 篇，其中 ★ 收藏 {n_fav} 篇。\n\n"
        + "\n\n".join(blocks)
    )


def generate_proposals(
    client: "SJTUClient", front: dict, papers: list[dict], *, model: str | None = None,
) -> str:
    from .llm.prompts import PROPOSAL_SYSTEM
    user = build_proposal_message(front, papers)
    return client.chat(
        [{"role": "system", "content": PROPOSAL_SYSTEM},
         {"role": "user", "content": user}],
        model=model, max_tokens=12000,
    )


def count_evidence(markdown: str) -> dict:
    """Count auditable evidence in generated proposals — never a quality score.

    Returns the number of proposal cards, how many distinct papers [k] are
    cited across them, and how many cards carry the single-source warning.
    Ordering fronts by distinct-citation count keeps the "no LLM ranking"
    principle intact: the number is a fact about the evidence, not a verdict.
    """
    cards = re.findall(r"^###\s*提案\s*\d+", markdown, re.M)
    cited = {int(m) for m in re.findall(r"\[(\d+)\]", markdown)}
    single = len(re.findall(r"⚠️\s*单点证据", markdown))
    # Provenance audit: an *evidence* bullet that quotes the note's advice-to-
    # the-researcher instead of the paper is circular reasoning. Scope this to
    # the 证据 block only — 武器匹配 and 为什么现在 are *supposed* to name the
    # arsenal, so scanning every bullet would flag correct output as a leak.
    leaked = 0
    for block in re.finditer(
        r"^\s*[-*]\s*\*\*证据.*?\*\*[:：]?(.*?)(?=^\s*[-*]\s*\*\*|\Z)",
        markdown, re.M | re.S,
    ):
        leaked += sum(
            1 for line in block.group(1).split("\n")
            if line.strip() and _COMMENTARY_RE.search(line)
        )
    return {
        "n_proposals": len(cards),
        "n_cited_papers": len(cited),
        "n_single_source": single,
        "n_commentary_leak": leaked,
    }


# ------------------------------------------------------------ stage E: render

FOOTER = (
    f"\n---\n\nMaintained by 陈星宇 · [Homepage]({HOMEPAGE_URL}) · [Source]({REPO_URL})\n"
)


def _deep_read_link(paper: dict) -> str:
    """Site-relative link into the deep-read note, or the arXiv url as fallback."""
    doc = paper.get("doc_path") or ""
    if doc.endswith(".md"):
        return "/research-news/" + doc[:-3] + "/"
    return paper.get("url") or ""


def render_front_page(
    front: dict, papers: list[dict], content: str, run_date: date,
    *, evidence: dict,
) -> Path:
    PROPOSALS_DIR.mkdir(parents=True, exist_ok=True)
    out = PROPOSALS_DIR / f"{front['key']}.md"
    src = []
    for k, paper in enumerate(papers, 1):
        star = "★ " if paper["favorite"] else ""
        link = _deep_read_link(paper)
        title = f"[{paper['title']}]({link})" if link else paper["title"]
        meta = " · ".join(x for x in (paper["venue"], paper["date"]) if x)
        src.append(f"- [{k}] {star}{title}" + (f" — {meta}" if meta else ""))

    lines = [
        f"# 选题提案 · {front['label']}\n",
        f"**战线范围**: {front['scope']}  " if front["scope"] else "",
        f"**证据论文**: {len(papers)} 篇（★ 收藏 "
        f"{sum(1 for p in papers if p['favorite'])} 篇）  ",
        f"**提案条数**: {evidence['n_proposals']}  ",
        f"**生成日期**: {run_date.isoformat()}  ",
        "\n> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——"
        "「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，"
        "自己掂量。\n",
        "---\n",
        content.strip() if content.strip() else "*（生成失败，请查看日志）*",
        "\n---\n\n### 本页的证据论文\n",
        "\n".join(src),
        FOOTER,
    ]
    out.write_text("\n".join(x for x in lines if x != "") + "\n", encoding="utf-8")
    return out


def render_overview(entries: list[dict], run_date: date, pool_size: int) -> Path:
    """Rewrite docs/all_synthesis.md as the proposal index."""
    total = sum(e["evidence"]["n_proposals"] for e in entries)
    lines = [
        "# 选题提案\n",
        "从你的精读语料 + 收藏里提炼**可上手的选题**。每条提案给：可投的标题、"
        "点名数学对象的 claim、先打哪个最简特例、哪几篇论文独立点名了这个 gap（附原话）、"
        "接你武器库的哪一件、什么会杀死它、以及第一周的具体动作。\n",
        "> **怎么读**：战线按**你收藏了几篇**排（同数再看证据论文数）——都是**可数的事实**，"
        "不是质量分。系统不打分、不排名、不替你判断值不值得做，每条证据都点到论文原话，"
        "你自己核验。战线本身是先按「主兴趣 → 覆盖了你武器库的几个领域 → 收藏数」筛出来的，"
        "所以 `低度多项式` 这种收藏少但正中主兴趣的战线也在。\n",
        f"**本次生成**: {run_date.isoformat()} · "
        f"{len(entries)} 条战线 · {total} 条提案 · "
        f"候选池 {pool_size} 篇（score ≥ {POOL_MIN_SCORE:.0f} 或已收藏的精读）\n",
        "---\n",
        "## 战线一览\n",
        "| 战线 | 证据论文 | ★ 收藏 | 提案 |",
        "|---|---:|---:|---:|",
    ]
    for e in entries:
        lines.append(
            f"| [{e['label']}](proposals/{e['key']}.md) | {e['n_papers']} | "
            f"{e['n_favorites']} | {e['evidence']['n_proposals']} |"
        )
    themes = find_recurring_themes(entries)
    if themes:
        lines += [
            "\n---\n",
            "## 跨战线反复出现的主题\n",
            "每条战线生成提案时**看不到其他战线**，所以同一个想法从多条战线独立冒出来时，"
            "这个「反复」本身就是证据——跟提案内部要求「≥2 篇独立论文点名」是同一个标准。"
            "这里只报事实，不替你合并：想法相近但 estimand 常常不同，值得你自己对一遍。\n",
        ]
        for t in themes:
            lines.append(
                f"**{t['theme']}** — {t['n_proposals']} 条提案，横跨 "
                f"{t['n_fronts']} 条战线\n"
            )
            for key, label, title in t["hits"]:
                lines.append(f"- [{label}](proposals/{key}.md) · {title}")
            lines.append("")

    lines.append("\n---\n")
    for e in entries:
        lines.append(f"## [{e['label']}](proposals/{e['key']}.md)\n")
        if e["scope"]:
            lines.append(f"{e['scope']}\n")
        badge = (
            f"证据 {e['n_papers']} 篇 · 含收藏 {e['n_favorites']} 篇 · "
            f"提案 {e['evidence']['n_proposals']} 条"
        )
        if e["evidence"]["n_single_source"]:
            badge += f" · ⚠️ 单点证据 {e['evidence']['n_single_source']} 条"
        lines.append(f"*{badge}*\n")
        for title in e.get("titles", []):
            lines.append(f"- {title}")
        lines.append("")
    synthesis_dir = DOCS_DIR / "synthesis"
    n_old = len(list(synthesis_dir.glob("*.md"))) if synthesis_dir.exists() else 0
    if n_old:
        lines += [
            "---\n",
            "## 旧版跨篇综合（存档）\n",
            "本页此前是按 10 个粗 topic 做的跨篇综合，产物停在「反复出现的开放问题 / 张力 / "
            f"迁移空位」，没有到可上手的提案。{n_old} 个旧页面全部保留："
            "[跨篇综合存档](synthesis/index.md)。\n",
        ]
    lines.append(FOOTER)
    OVERVIEW_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return OVERVIEW_PAGE


def merge_index(new_entries: list[dict]) -> list[dict]:
    """Merge freshly generated fronts into the stored index, newest wins per key.

    Without this, `--front X` (the natural way to retry one timed-out front)
    would rewrite the overview with a single row and drop the other fifteen
    pages from the index while leaving their files on disk.

    Entries whose page no longer exists are pruned, so deleting a front's file
    is enough to retire it.
    """
    stored: list[dict] = []
    if PROPOSALS_DATA.exists():
        try:
            stored = (json.loads(PROPOSALS_DATA.read_text(encoding="utf-8"))
                      .get("fronts") or [])
        except Exception as exc:  # noqa: BLE001
            log.warning("could not read %s, starting a fresh index: %s",
                        PROPOSALS_DATA, exc)
    by_key = {e["key"]: e for e in stored if e.get("key")}
    by_key.update({e["key"]: e for e in new_entries})
    alive = [e for e in by_key.values()
             if (DOCS_DIR / e.get("doc_path", "")).exists()]
    # Same ordering as selection: most favorites first, then most evidence.
    alive.sort(key=lambda e: (-e.get("n_favorites", 0), -e.get("n_papers", 0)))
    return alive


# Recurring methodological themes. Each front generates proposals blind to the
# other fronts, so the same idea legitimately surfaces several times — e.g.
# "HOIF to relax the n^{-1/4} rate condition" arrived independently from four
# fronts. That recurrence is *signal* (independent convergence is the same
# evidence standard the proposals themselves must meet), so the overview reports
# it as a fact instead of silently deduplicating. Marker pairs are (title/claim
# pattern, required second pattern or None).
RECURRING_THEMES: dict[str, tuple[str, str | None]] = {
    "HOIF 放松 n^{-1/4} 速率条件": (
        r"higher-order (influence|debiased)",
        r"slow nuisance|n\^\{-1/4\}|收敛率慢|慢于",
    ),
    "近端因果的桥函数估计": (r"proximal|bridge function", r"bridge|桥函数"),
    "低度多项式 / 计算-统计 gap": (
        r"low-degree|statistical.computational|computational (barrier|transition)",
        None,
    ),
    "退化核 U 统计量的极限分布": (r"degenerate", r"u-statistic"),
    "子空间估计的 minimax 率": (r"subspace", r"minimax|optimal"),
    "张量估计的相变 / 优化": (r"tensor", r"phase transition|riemannian|gap"),
}


def split_cards(markdown: str) -> list[tuple[str, str]]:
    """Split generated markdown into (title, body) per proposal card."""
    out = []
    for chunk in re.split(r"^###\s*提案\s*\d+\s*[：:]\s*", markdown, flags=re.M)[1:]:
        lines = chunk.split("\n", 1)
        out.append((lines[0].strip(), lines[1] if len(lines) > 1 else ""))
    return out


def find_recurring_themes(entries: list[dict]) -> list[dict]:
    """Which themes showed up in >=2 fronts, and where."""
    found: dict[str, list[tuple[str, str, str]]] = {}
    for entry in entries:
        page = DOCS_DIR / entry.get("doc_path", "")
        if not page.exists():
            continue
        text = page.read_text(encoding="utf-8")
        for title, body in split_cards(text):
            claim = re.search(r"\*\*claim.*?\*\*\s*[：:]\s*(.+)", body)
            hay = (title + " " + (claim.group(1) if claim else "")).lower()
            for name, (pat, extra) in RECURRING_THEMES.items():
                if re.search(pat, hay) and (extra is None or re.search(extra, hay)):
                    found.setdefault(name, []).append(
                        (entry["key"], entry["label"], title)
                    )
    out = []
    for name, hits in found.items():
        fronts = {k for k, _, _ in hits}
        if len(fronts) >= 2:
            out.append({"theme": name, "n_proposals": len(hits),
                        "n_fronts": len(fronts), "hits": hits})
    out.sort(key=lambda t: (-t["n_fronts"], -t["n_proposals"]))
    return out


def extract_titles(markdown: str) -> list[str]:
    """Pull proposal titles out of generated markdown for the overview page."""
    out = []
    for m in re.finditer(r"^###\s*提案\s*\d+\s*[：:]\s*(.+?)\s*$", markdown, re.M):
        out.append(m.group(1).strip())
    return out


# ------------------------------------------------------------------ orchestrate


def _client():
    from dotenv import load_dotenv
    from .llm.sjtu_client import SJTUClient
    load_dotenv()
    return SJTUClient()


def run(
    *,
    front_filter: str | None = None,
    min_score: float = POOL_MIN_SCORE,
    since: str | None = None,
    min_papers: int = FRONT_MIN_PAPERS,
    max_papers: int = FRONT_MAX_PAPERS,
    max_fronts: int = MAX_FRONTS,
    model: str | None = None,
    rebuild_fronts: bool = False,
    dry_run: bool = False,
) -> list[Path]:
    model = model or DEFAULT_MODEL
    run_date = date.today()

    pool = build_pool(min_score=min_score, since=since)
    log.info(
        "candidate pool: %d papers (%d favorited)",
        len(pool), sum(1 for p in pool if p["favorite"]),
    )
    if not pool:
        log.error("empty candidate pool — nothing to do")
        return []

    if rebuild_fronts:
        if dry_run:
            log.info("--dry-run with --build-fronts: skipping the clustering calls")
        else:
            fronts = build_fronts(_client(), pool, model=model)
            if not fronts:
                log.error("front clustering produced nothing; keeping existing config")
            else:
                write_fronts_config(fronts)

    fronts = load_fronts()
    if not fronts:
        log.error(
            "no fronts defined — run with --build-fronts first (writes %s)", FRONTS_CONFIG
        )
        return []

    buckets = assign_papers(pool, fronts)
    fronts = [f for f in fronts if len(buckets.get(f["key"], [])) >= min_papers]
    fronts = dedupe_fronts(fronts, buckets)

    kept: list[tuple[dict, list[dict]]] = []
    for front in fronts:
        if front_filter and front["key"] != front_filter:
            continue
        kept.append((front, buckets[front["key"]]))

    # Selection order — every key a deterministic count, no quality judgement:
    #   1. primary interest before secondary (secondary topics are gateway reading)
    #   2. arsenal affinity *band*: how many of his own tool areas the front names
    #   3. favorite count inside the band: papers he hand-picked
    def _order(fp: tuple[dict, list[dict]]) -> tuple:
        front, papers = fp
        return (
            0 if front["topic"] in PRIMARY_TOPICS else 1,
            affinity_band(front_affinity(front)),
            -sum(1 for p in papers if p["favorite"]),
            -len(papers),
        )

    kept.sort(key=_order)
    if max_fronts and len(kept) > max_fronts:
        log.info(
            "capping %d fronts to %d (primary interest → arsenal affinity → favorites)",
            len(kept), max_fronts,
        )
        for front, papers in kept[max_fronts:]:
            log.info("  cut %s (affinity=%d, favorites=%d)", front["key"],
                     front_affinity(front), sum(1 for p in papers if p["favorite"]))
        kept = kept[:max_fronts]

    if dry_run:
        log.info("would generate proposals for %d fronts:", len(kept))
        for front, papers in kept:
            log.info(
                "  %-42s papers=%3d  favorites=%2d  prompt=%d papers",
                front["key"], len(papers),
                sum(1 for p in papers if p["favorite"]),
                min(len(papers), max_papers),
            )
        return []

    client = _client()
    written: list[Path] = []
    index_entries: list[dict] = []
    for front, papers in kept:
        selected = select_for_prompt(papers, limit=max_papers)
        log.info(
            "generating proposals for %s (%d papers, %d in prompt) ...",
            front["key"], len(papers), len(selected),
        )
        try:
            content = generate_proposals(client, front, selected, model=model)
        except Exception as exc:  # noqa: BLE001
            log.warning("proposal generation failed for %s: %s", front["key"], exc)
            continue
        evidence = count_evidence(content)
        if not evidence["n_proposals"]:
            log.warning("no proposal cards parsed for %s — skipping page", front["key"])
            continue
        if evidence["n_commentary_leak"]:
            log.warning(
                "%s: %d line(s) may cite note-commentary instead of paper content "
                "— spot-check the 证据 bullets on that page",
                front["key"], evidence["n_commentary_leak"],
            )
        page = render_front_page(front, selected, content, run_date, evidence=evidence)
        written.append(page)
        entry = front_stats(front, papers)
        entry.update({
            "date": run_date.isoformat(),
            "doc_path": f"proposals/{page.name}",
            "evidence": evidence,
            "titles": extract_titles(content),
        })
        index_entries.append(entry)
        log.info("wrote %s (%d proposals)", page, evidence["n_proposals"])

    if index_entries:
        merged = merge_index(index_entries)
        render_overview(merged, run_date, len(pool))
        PROPOSALS_DATA.parent.mkdir(parents=True, exist_ok=True)
        PROPOSALS_DATA.write_text(
            json.dumps(
                {"date": run_date.isoformat(), "pool_size": len(pool),
                 "fronts": merged},
                ensure_ascii=False, indent=2,
            ),
            encoding="utf-8",
        )
        written.append(OVERVIEW_PAGE)
    return written


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ap = argparse.ArgumentParser(
        description="选题提案引擎：把精读语料 + 收藏变成可上手的选题提案。")
    ap.add_argument("--build-fronts", action="store_true",
                    help=f"(re)cluster the pool into research fronts, writing {FRONTS_CONFIG}")
    ap.add_argument("--front", help="only this front key")
    ap.add_argument("--min-score", type=float, default=POOL_MIN_SCORE,
                    help="score gate for the pool (favorites always bypass it)")
    ap.add_argument("--since", help="only deep-reads on/after this ISO date")
    ap.add_argument("--min-papers", type=int, default=FRONT_MIN_PAPERS,
                    help="drop fronts with fewer evidence papers than this")
    ap.add_argument("--max-papers", type=int, default=FRONT_MAX_PAPERS,
                    help="cap papers fed to one proposal call (favorites first)")
    ap.add_argument("--max-fronts", type=int, default=MAX_FRONTS,
                    help="keep only the N fronts with most favorited papers (0 = no cap)")
    ap.add_argument("--model", default=None)
    ap.add_argument("--dry-run", action="store_true",
                    help="show pool + front sizes, make no LLM calls")
    args = ap.parse_args()

    paths = run(
        front_filter=args.front, min_score=args.min_score, since=args.since,
        min_papers=args.min_papers, max_papers=args.max_papers,
        max_fronts=args.max_fronts, model=args.model,
        rebuild_fronts=args.build_fronts, dry_run=args.dry_run,
    )
    print(f"wrote {len(paths)} page(s)")


if __name__ == "__main__":
    main()
