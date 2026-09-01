"""Tests for the 选题提案 engine (research_news/proposals.py)."""
from __future__ import annotations

import json
from datetime import date

from research_news import proposals as pr


# --------------------------------------------------------------- gap slicing

def test_gap_slice_keeps_all_five_sections():
    body = """# T

### 一、领域脉络与小综述

#### 这个方向是什么
铺垫，不该进切片。

#### 这个方向在追问的核心问题
瓶颈在于信息算子不可逆。

#### ⚠️ 作者的 framing
作者把缺口 frame 成单一分解。

#### 张力
未见明显对立引用。

### 三、这篇论文做了什么

#### 主要结果
定理内容，不该进切片。

#### 🔎 结论是否比证明窄
Proposition 3 只给了子空间。

### 四、开放问题

1. 多个约束下的完整刻画。**扎根点**：Remark 5。

---

Maintained by 陈星宇 · [Homepage](https://x) · [Source](https://y)
"""
    out = pr.gap_slice(body)
    assert "瓶颈在于信息算子不可逆" in out
    assert "frame 成单一分解" in out
    assert "未见明显对立引用" in out
    assert "只给了子空间" in out
    assert "扎根点" in out and "Remark 5" in out
    # Bulk sections and the footer stay out.
    assert "铺垫" not in out
    assert "定理内容" not in out
    assert "Maintained by" not in out


def test_gap_slice_tolerates_historical_header_variants():
    """The note format drifted for four months; the slicer matches on prefix."""
    variants = [
        "### 四、开放问题（点到为止，扎根具体语句）\n扎根在 Remark 5。\n",
        "### 四、开放问题（扎根具体语句）\n扎根在 Remark 5。\n",
        "#### ⚠️ 作者的framing\n作者淡化了竞争路线。\n",
        "#### ⚠️ 作者的 framing（必须明确标注成“这是作者的说法”）\n作者淡化了竞争路线。\n",
        "#### 核心问题与瓶颈\n卡在收敛率上。\n",
    ]
    for body in variants:
        assert pr.gap_slice(body).strip(), f"slicer missed: {body[:40]}"


def test_gap_slice_respects_max_chars():
    body = "### 四、开放问题\n" + ("很长的开放问题。" * 500)
    assert len(pr.gap_slice(body, max_chars=200)) <= 200


def test_gap_slice_empty_for_note_without_gap_sections():
    body = "### 一、这篇论文属于什么学科\n科普向内容。\n\n### 四、数据问题\n数据结构。\n"
    assert pr.gap_slice(body) == ""


def test_gap_slice_marks_note_commentary_not_paper_content():
    """Advice addressed to the researcher must not read as paper evidence."""
    body = (
        "### 四、开放问题\n"
        "1. 信息算子可逆性。**扎根点**：Remark 5。\n"
        "2. 对于您在高阶U统计量计算方面的专长，这是一个直接的连接点。\n"
    )
    out = pr.gap_slice(body)
    assert "（笔记作者的旁注，非论文内容）" in out
    # The genuine paper-grounded line stays clean.
    grounded = [ln for ln in out.split("\n") if "Remark 5" in ln][0]
    assert "旁注" not in grounded


def test_count_evidence_flags_commentary_leak():
    leaked = "### 提案 1：A\n- **证据**：\n  - [7] 指出您的武器库正好能接上这个洞\n"
    clean = "### 提案 1：A\n- **证据**：\n  - [7] Remark 4 引用 Chen et al. (2025)\n"
    assert pr.count_evidence(leaked)["n_commentary_leak"] == 1
    assert pr.count_evidence(clean)["n_commentary_leak"] == 0


def test_commentary_audit_ignores_arsenal_talk_outside_evidence():
    """武器匹配 / 为什么现在 are *required* to name the arsenal — not leaks."""
    md = (
        "### 提案 1：A\n"
        "- **证据**：\n  - [7] Remark 4 引用 Chen et al. (2025)\n"
        "- **为什么现在**：研究者武器库里的 einsum 使这件事可算\n"
        "- **武器匹配**：用 very_familiar 里的高阶 U 统计量计算\n"
    )
    assert pr.count_evidence(md)["n_commentary_leak"] == 0


# ------------------------------------------------------------- candidate pool

def _write_corpus(tmp_path, monkeypatch, *, deep_reads, highlights, favorites):
    docs = tmp_path / "docs"
    (docs / "data").mkdir(parents=True)
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "deep_reads_index.json").write_text(
        json.dumps(deep_reads), encoding="utf-8")
    (tmp_path / "data" / "highlights.json").write_text(
        json.dumps(highlights), encoding="utf-8")
    (docs / "data" / "favorites_public.json").write_text(
        json.dumps(favorites), encoding="utf-8")
    monkeypatch.setattr(pr, "DOCS_DIR", docs)
    monkeypatch.setattr(pr, "DEEP_READS_INDEX", tmp_path / "data/deep_reads_index.json")
    monkeypatch.setattr(pr, "HIGHLIGHTS", tmp_path / "data/highlights.json")
    monkeypatch.setattr(pr, "FAVORITES", docs / "data/favorites_public.json")
    return docs


def test_pool_gate_and_favorite_bypass(tmp_path, monkeypatch):
    """Favorites enter the pool even below the score gate; low-score others don't."""
    _write_corpus(
        tmp_path, monkeypatch,
        deep_reads=[
            {"paper_id": "hi", "date": "2026-08-01", "topic": "causal_inference",
             "doc_path": "deep_reads/hi.md"},
            {"paper_id": "fav_low", "date": "2026-08-02", "topic": "astrostats",
             "doc_path": "deep_reads/fav_low.md"},
            {"paper_id": "lo", "date": "2026-08-03", "topic": "other",
             "doc_path": "deep_reads/lo.md"},
        ],
        highlights=[
            {"paper_id": "hi", "title": "High", "score": 9.0, "key_techniques": ["eif"]},
            {"paper_id": "fav_low", "title": "Fav low", "score": 4.0, "key_techniques": []},
            {"paper_id": "lo", "title": "Low", "score": 5.0, "key_techniques": []},
        ],
        favorites=[{"paper_id": "fav_low", "note": "读这个"}],
    )
    ids = {p["paper_id"]: p for p in pr.build_pool()}
    assert set(ids) == {"hi", "fav_low"}
    assert ids["fav_low"]["favorite"] is True
    assert ids["fav_low"]["note"] == "读这个"
    assert ids["hi"]["favorite"] is False


def test_pool_keeps_newest_deep_read_per_paper(tmp_path, monkeypatch):
    _write_corpus(
        tmp_path, monkeypatch,
        deep_reads=[
            {"paper_id": "p", "date": "2026-06-01", "topic": "other",
             "doc_path": "deep_reads/old.md"},
            {"paper_id": "p", "date": "2026-09-01", "topic": "causal_inference",
             "doc_path": "deep_reads/new.md"},
        ],
        highlights=[{"paper_id": "p", "title": "P", "score": 9.0}],
        favorites=[],
    )
    pool = pr.build_pool()
    assert len(pool) == 1
    assert pool[0]["doc_path"] == "deep_reads/new.md"
    assert pool[0]["topic"] == "causal_inference"


def test_pool_since_filter(tmp_path, monkeypatch):
    _write_corpus(
        tmp_path, monkeypatch,
        deep_reads=[
            {"paper_id": "a", "date": "2026-05-01", "topic": "other", "doc_path": "d/a.md"},
            {"paper_id": "b", "date": "2026-08-01", "topic": "other", "doc_path": "d/b.md"},
        ],
        highlights=[{"paper_id": "a", "title": "A", "score": 9.0},
                    {"paper_id": "b", "title": "B", "score": 9.0}],
        favorites=[],
    )
    assert {p["paper_id"] for p in pr.build_pool(since="2026-07-01")} == {"b"}


# ----------------------------------------------------------- front assignment

def _paper(pid, title, techs=(), fav=False, score=8.0, date_="2026-08-01"):
    return {"paper_id": pid, "title": title, "venue": "AoS", "date": date_,
            "published": "", "url": "", "topic": "causal_inference", "score": score,
            "techniques": list(techs), "favorite": fav, "note": "",
            "doc_path": f"deep_reads/{pid}.md"}


def test_assign_matches_title_and_techniques_and_allows_overlap():
    pool = [
        _paper("a", "Two-Sample IV: Efficient Two-Step Estimation"),
        _paper("b", "Debiased inference", techs=["proximal causal inference"]),
        _paper("c", "Unrelated spectral paper", techs=["marchenko-pastur law"]),
    ]
    fronts = [
        {"key": "fusion", "label": "融合", "scope": "", "topic": "",
         "keywords": ["two-sample iv"], "techniques": []},
        {"key": "prox", "label": "近端", "scope": "", "topic": "",
         "keywords": ["proximal causal"], "techniques": []},
        {"key": "wide", "label": "宽", "scope": "", "topic": "",
         "keywords": ["iv", "proximal causal"], "techniques": []},
    ]
    buckets = pr.assign_papers(pool, fronts)
    assert [p["paper_id"] for p in buckets["fusion"]] == ["a"]
    assert [p["paper_id"] for p in buckets["prox"]] == ["b"]
    # Overlap is intentional: a paper may support several fronts.
    assert {p["paper_id"] for p in buckets["wide"]} == {"a", "b"}
    assert buckets["fusion"] and "c" not in {p["paper_id"] for p in buckets["fusion"]}


def test_assign_ignores_front_with_empty_keywords():
    pool = [_paper("a", "Anything at all")]
    fronts = [{"key": "dead", "label": "x", "scope": "", "topic": "",
               "keywords": [], "techniques": []}]
    assert pr.assign_papers(pool, fronts)["dead"] == []


def test_select_for_prompt_puts_favorites_first_then_score():
    papers = [
        _paper("s7", "s7", score=7.0),
        _paper("s10", "s10", score=10.0),
        _paper("f5", "f5", score=5.0, fav=True),
    ]
    picked = pr.select_for_prompt(papers, limit=2)
    assert [p["paper_id"] for p in picked] == ["f5", "s10"]


def _front(key, keywords, label="x", scope="", topic="causal_inference"):
    return {"key": key, "label": label, "scope": scope, "topic": topic,
            "keywords": list(keywords), "techniques": []}


def test_broad_front_is_tightened_to_two_keyword_hits():
    """A front sweeping most of the pool is a topic bucket, not a front."""
    pool = [_paper(f"p{i}", "influence function paper") for i in range(20)]
    pool += [_paper(f"q{i}", "influence function and data fusion paper") for i in range(8)]
    front = _front("broad", ["influence function", "data fusion"])
    buckets = pr.assign_papers(pool, [front], broad_fraction=0.10)
    # 28 matched > 10% of 28; only the 8 double-hit papers survive.
    assert len(buckets["broad"]) == 8
    assert all(p["paper_id"].startswith("q") for p in buckets["broad"])


def test_broad_front_not_tightened_below_min_papers():
    """Tightening that would starve the front is skipped, not applied."""
    pool = [_paper(f"p{i}", "influence function paper") for i in range(20)]
    pool += [_paper("q0", "influence function and data fusion paper")]
    front = _front("broad", ["influence function", "data fusion"])
    buckets = pr.assign_papers(pool, [front], broad_fraction=0.10)
    assert len(buckets["broad"]) == 21   # kept loose: 1 < FRONT_MIN_PAPERS


def test_dedupe_drops_near_duplicate_front_keeping_more_favorites():
    shared = [_paper(f"s{i}", "shared", fav=(i < 3)) for i in range(9)]
    a, b = _front("keep", ["x"]), _front("dup", ["y"])
    buckets = {"keep": shared, "dup": shared[:8]}     # Jaccard 8/9 = 0.89
    kept = pr.dedupe_fronts([a, b], buckets, max_jaccard=0.5)
    assert [f["key"] for f in kept] == ["keep"]


def test_dedupe_keeps_fronts_that_merely_overlap():
    a_papers = [_paper(f"a{i}", "a") for i in range(10)]
    b_papers = a_papers[:2] + [_paper(f"b{i}", "b") for i in range(8)]
    a, b = _front("a", ["x"]), _front("b", ["y"])
    kept = pr.dedupe_fronts([a, b], {"a": a_papers, "b": b_papers}, max_jaccard=0.5)
    assert {f["key"] for f in kept} == {"a", "b"}


def test_affinity_counts_distinct_areas_not_synonyms():
    """Listing five synonyms for one area must not beat touching two areas."""
    one_area = _front("one", [
        "u-statistic", "u-process", "hoeffding decomposition", "v-statistic",
        "higher-order u-statistic",
    ])
    two_areas = _front("two", ["u-statistic", "minimax lower bound"])
    assert pr.front_affinity(one_area) == 1
    assert pr.front_affinity(two_areas) == 2


def test_affinity_matches_chinese_scope_text():
    """Front scopes come back in Chinese; anchors must cover both languages."""
    front = _front("zh", [], label="双稳健估计与半参效率理论",
                   scope="推导半参数效率界，应用于处理效应与剂量反应函数的推断。")
    areas = pr.front_affinity(front)
    assert areas >= 2, f"Chinese scope matched only {areas} areas"


def test_affinity_band_groups_near_equal_fronts():
    assert pr.affinity_band(6) == pr.affinity_band(4)      # both top band
    assert pr.affinity_band(3) < pr.affinity_band(2)       # bands are ordered
    assert pr.affinity_band(0) == len(pr.AFFINITY_BANDS)   # floor band


# ------------------------------------------------------ prompt + evidence math

def test_paper_block_marks_favorites_and_inlines_gap_slice(tmp_path, monkeypatch):
    docs = tmp_path / "docs"
    (docs / "deep_reads").mkdir(parents=True)
    (docs / "deep_reads" / "a.md").write_text(
        "### 四、开放问题\n完整刻画仍开放。**扎根点**：Remark 5。\n", encoding="utf-8")
    monkeypatch.setattr(pr, "DOCS_DIR", docs)
    paper = _paper("a", "Nested Markov Efficiency", fav=True)
    paper["note"] = "跟 HOIF 有联系"
    block = pr.paper_block(1, paper)
    assert block.startswith("[1] ★收藏 Nested Markov Efficiency")
    assert "你的笔记: 跟 HOIF 有联系" in block
    assert "扎根点" in block and "Remark 5" in block


def test_paper_block_survives_missing_note_file(tmp_path, monkeypatch):
    monkeypatch.setattr(pr, "DOCS_DIR", tmp_path / "docs")
    block = pr.paper_block(3, _paper("gone", "No Note On Disk"))
    assert "[3] No Note On Disk" in block


def test_count_evidence_counts_cards_citations_and_warnings():
    md = """### 提案 1：A
- **证据**：[1] 说 X；[2] 说 Y
### 提案 2：B
- **证据**：⚠️ 单点证据 只有 [2] 提到
"""
    ev = pr.count_evidence(md)
    assert ev["n_proposals"] == 2
    assert ev["n_cited_papers"] == 2      # distinct [k], not occurrences
    assert ev["n_single_source"] == 1


def test_extract_titles_handles_both_colon_forms():
    md = "### 提案 1：中文冒号标题\n\n### 提案 2: ASCII colon title\n"
    assert pr.extract_titles(md) == ["中文冒号标题", "ASCII colon title"]


def test_split_cards_returns_title_and_body():
    md = "### 提案 1：T1\n- **claim（一句话）**：C1\n\n### 提案 2：T2\n- body2\n"
    cards = pr.split_cards(md)
    assert [t for t, _ in cards] == ["T1", "T2"]
    assert "C1" in cards[0][1]


def test_find_recurring_themes_needs_two_fronts(tmp_path, monkeypatch):
    docs = tmp_path / "docs"
    (docs / "proposals").mkdir(parents=True)
    monkeypatch.setattr(pr, "DOCS_DIR", docs)
    hoif = ("### 提案 1：Higher-Order Influence Functions for X\n"
            "- **claim（一句话）**：当 nuisance 收敛率慢于 n^{-1/4} 时仍 √n 一致\n")
    (docs / "proposals" / "a.md").write_text(hoif, encoding="utf-8")
    (docs / "proposals" / "b.md").write_text(hoif, encoding="utf-8")
    (docs / "proposals" / "c.md").write_text(
        "### 提案 1：Something About Subspace\n- **claim（一句话）**：无关\n",
        encoding="utf-8")
    entries = [{"key": k, "label": k.upper(), "doc_path": f"proposals/{k}.md"}
               for k in ("a", "b", "c")]
    themes = pr.find_recurring_themes(entries)
    names = [t["theme"] for t in themes]
    assert "HOIF 放松 n^{-1/4} 速率条件" in names
    hoif_theme = next(t for t in themes if t["theme"].startswith("HOIF"))
    assert hoif_theme["n_fronts"] == 2 and hoif_theme["n_proposals"] == 2
    # A theme appearing in only one front is not reported.
    assert not any(t["theme"] == "子空间估计的 minimax 率" for t in themes)


# ------------------------------------------------------------------- rendering

def test_render_front_page_and_overview(tmp_path, monkeypatch):
    docs = tmp_path / "docs"
    docs.mkdir()
    monkeypatch.setattr(pr, "DOCS_DIR", docs)
    monkeypatch.setattr(pr, "PROPOSALS_DIR", docs / "proposals")
    monkeypatch.setattr(pr, "OVERVIEW_PAGE", docs / "all_synthesis.md")

    front = {"key": "prox", "label": "近端因果", "scope": "代理变量下的识别与效率",
             "topic": "causal_inference", "keywords": ["proximal causal"], "techniques": []}
    papers = [_paper("a", "Paper A", fav=True), _paper("b", "Paper B")]
    md = "### 提案 1：某个可投的标题\n- **证据**：[1] 与 [2] 都点名了。\n"
    ev = pr.count_evidence(md)
    page = pr.render_front_page(front, papers, md, date(2026, 9, 1), evidence=ev)
    text = page.read_text(encoding="utf-8")
    assert "# 选题提案 · 近端因果" in text
    assert "代理变量下的识别与效率" in text
    assert "不打分、不排名" in text
    assert "[1] ★ [Paper A](/research-news/deep_reads/a/)" in text
    assert "某个可投的标题" in text

    entry = pr.front_stats(front, papers)
    entry.update({"date": "2026-09-01", "doc_path": f"proposals/{page.name}",
                  "evidence": ev, "titles": pr.extract_titles(md)})
    ov = pr.render_overview([entry], date(2026, 9, 1), 1441)
    otext = ov.read_text(encoding="utf-8")
    assert "# 选题提案" in otext
    assert "[近端因果](proposals/prox.md)" in otext
    assert "候选池 1441 篇" in otext
    assert "证据 2 篇 · 含收藏 1 篇" in otext
    assert "某个可投的标题" in otext
    # No old synthesis pages in this tmp tree, so no archive section.
    assert "旧版跨篇综合" not in otext


def test_overview_links_archive_only_when_old_pages_exist(tmp_path, monkeypatch):
    docs = tmp_path / "docs"
    (docs / "synthesis").mkdir(parents=True)
    (docs / "synthesis" / "2026-06-02-core-other.md").write_text("x", encoding="utf-8")
    monkeypatch.setattr(pr, "DOCS_DIR", docs)
    monkeypatch.setattr(pr, "OVERVIEW_PAGE", docs / "all_synthesis.md")
    entry = {"key": "k", "label": "L", "scope": "", "n_papers": 6, "n_favorites": 1,
             "date": "2026-09-01", "doc_path": "proposals/k.md",
             "evidence": {"n_proposals": 2, "n_cited_papers": 4,
                          "n_single_source": 0, "n_commentary_leak": 0},
             "titles": ["T"]}
    text = pr.render_overview([entry], date(2026, 9, 1), 10).read_text(encoding="utf-8")
    assert "1 个旧页面全部保留" in text
    assert "[跨篇综合存档](synthesis/index.md)" in text
