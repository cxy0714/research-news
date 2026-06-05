"""Offline tests for retroactive institution backfill (no network)."""
from __future__ import annotations

from research_news import backfill_institutions as bi


def test_doi_from_heading_arxiv():
    line = "#### 1. [2606.06441](https://arxiv.org/abs/2606.06441) — Some Title"
    assert bi._doi_from_heading(line) == "10.48550/arXiv.2606.06441"


def test_doi_from_heading_journal_doi():
    line = "## 1. [10.1214/23-AOS2345](https://doi.org/10.1214/23-AOS2345) — Title"
    assert bi._doi_from_heading(line) == "10.1214/23-AOS2345"


def test_insert_after_venue():
    block = [
        "- **作者**: A, B",
        "- **期刊/来源**: AOS",
        "- **分类**: stat.ME",
    ]
    out = bi._insert_institution_line(block, "- **机构**: MIT")
    assert out == [
        "- **作者**: A, B",
        "- **期刊/来源**: AOS",
        "- **机构**: MIT",
        "- **分类**: stat.ME",
    ]


def test_insert_after_author_when_no_venue():
    block = ["- **作者**: A, B", "- **分类**: stat.ME"]
    out = bi._insert_institution_line(block, "- **机构**: MIT")
    assert out == ["- **作者**: A, B", "- **机构**: MIT", "- **分类**: stat.ME"]


def test_backfill_page_injects_and_is_idempotent(tmp_path, monkeypatch):
    page = tmp_path / "2026-06-05.md"
    page.write_text(
        "# 2026-06-05 每日 arXiv 资讯\n\n"
        "## ⭐ 高相关论文\n\n"
        "### 因果推断  *(causal_inference, 1 篇)*\n\n"
        "#### 1. [2606.06441](https://arxiv.org/abs/2606.06441) — A Paper\n"
        "- **作者**: A, B\n"
        "- **分类**: stat.ME\n"
        "- **摘要**: blah\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        bi.affil, "_fetch_affiliations_and_institutions",
        lambda doi: (["MIT"], ["MIT"]),
    )

    assert bi.backfill_page(page) is True
    text = page.read_text(encoding="utf-8")
    assert "- **机构**: MIT" in text
    # 机构 sits between 作者 and 分类.
    assert text.index("**作者**") < text.index("**机构**") < text.index("**分类**")

    # Running again is a no-op (already has the line) and must not double-insert.
    assert bi.backfill_page(page) is False
    assert page.read_text(encoding="utf-8").count("**机构**") == 1


def test_backfill_page_skips_when_not_indexed(tmp_path, monkeypatch):
    page = tmp_path / "2026-06-05.md"
    original = (
        "#### 1. [2606.06441](https://arxiv.org/abs/2606.06441) — A Paper\n"
        "- **作者**: A, B\n"
        "- **分类**: stat.ME\n"
    )
    page.write_text(original, encoding="utf-8")
    # OpenAlex still doesn't know the paper → empty institutions.
    monkeypatch.setattr(
        bi.affil, "_fetch_affiliations_and_institutions",
        lambda doi: ([], []),
    )
    assert bi.backfill_page(page) is False
    assert page.read_text(encoding="utf-8") == original
