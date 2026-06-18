"""Offline tests for the journal 导览 parse/insert logic and the render hook."""
from __future__ import annotations

from research_news import journal_overview as jo
from research_news.render.markdown import JOURNAL_OVERVIEW_HEADING, render_journal_page
from research_news.models import Paper


_PAGE = (
    "# AoS — Vol 53  Issue 5  ·  2026-05-26\n\n"
    "- 共 2 篇 · Annals of Statistics\n"
    "- 目录核对 ✅ 2 篇全部抓到（对照 OpenAlex 2 篇）\n\n"
    "## 因果推断  *(causal_inference, 1 篇)*\n\n"
    "### 1. [10.1214/x](https://doi.org/10.1214/x) — Robust policy evaluation\n"
    "- **作者**: A B\n"
    "- **摘要**: 在 MDP 下研究鲁棒策略价值估计，提出 robust TD。\n\n"
    "## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*\n\n"
    "### 2. [10.1214/y](https://doi.org/10.1214/y) — Spectral methods\n"
    "- **摘要**: 高维协方差的谱方法。\n\n"
    "---\n\nMaintained by 陈星宇\n"
)


def test_parse_page_papers():
    items = jo.parse_page_papers(_PAGE)
    assert [it["title"] for it in items] == ["Robust policy evaluation", "Spectral methods"]
    assert [it["topic"] for it in items] == ["causal_inference", "high_dim_rmt"]
    assert items[0]["summary"].startswith("在 MDP 下")


def test_build_input_groups_by_topic():
    msg = jo.build_input(jo.parse_page_papers(_PAGE), "AoS Vol 53 Issue 5")
    assert "【causal_inference】" in msg and "【high_dim_rmt】" in msg
    assert "Robust policy evaluation" in msg and "AoS Vol 53 Issue 5" in msg


def test_insert_and_strip_overview_roundtrip():
    assert not jo.has_overview(_PAGE)
    inserted = jo.insert_overview(_PAGE, "本期围绕鲁棒策略评估与谱方法。")
    assert jo.has_overview(inserted)
    # 导览 sits before the first topic group, after the count/completeness lines.
    assert inserted.index(JOURNAL_OVERVIEW_HEADING) < inserted.index("## 因果推断")
    assert inserted.index("- 目录核对") < inserted.index(JOURNAL_OVERVIEW_HEADING)
    assert "本期围绕鲁棒策略评估与谱方法。" in inserted
    # stripping returns to a body with no 导览 (and topic groups intact)
    stripped = jo.strip_overview(inserted)
    assert not jo.has_overview(stripped)
    assert "## 因果推断" in stripped and "Spectral methods" in stripped


def test_insert_is_idempotent_via_skip(tmp_path):
    p = tmp_path / "2026-05-26-aos-v53-i5.md"
    p.write_text(_PAGE, encoding="utf-8")
    # has_overview gate means backfill skips an already-done page (force=False).
    assert jo.backfill_page(p, None, force=False, dry_run=True) == 1   # not yet present
    p.write_text(jo.insert_overview(_PAGE, "x"), encoding="utf-8")
    assert jo.backfill_page(p, None, force=False, dry_run=True) == 0   # present → skip


def test_render_journal_page_includes_overview(tmp_path):
    papers = [Paper(source="crossref", paper_id="10.1/x", title="T", authors=["A"],
                    abstract="", url="https://doi.org/10.1/x", topic="causal_inference",
                    score=7.0, summary_zh="摘要")]
    out = render_journal_page(papers, "AoS", "Annals of Statistics", vol="53", iss="5",
                              output_dir=tmp_path, overview="本期聚焦因果效率。")
    body = out.read_text(encoding="utf-8")
    assert JOURNAL_OVERVIEW_HEADING in body
    assert "本期聚焦因果效率。" in body
    assert body.index(JOURNAL_OVERVIEW_HEADING) < body.index("## 因果推断")
