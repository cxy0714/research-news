"""Tests for the AI auto-research radar track."""
from __future__ import annotations

from datetime import date

from research_news import autoresearch as ar
from research_news.models import Paper

FILTER = ar.load_config()["filter"]


def test_prefilter_title_abstract_deny():
    # title signal
    assert ar._matches(
        "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery",
        "", FILTER,
    )
    assert ar._matches("Agent Laboratory: Using LLM Agents as Research Assistants", "", FILTER)
    # abstract-only signal is allowed on this track (unlike the benchmark radar),
    # because research-agent papers often only announce themselves in the abstract
    assert ar._matches(
        "SciAgent: A Multi-Agent System",
        "We present a research pipeline that runs experiments end to end.",
        FILTER,
    )
    # deny wins
    assert not ar._matches("Automated Machine Learning Tool for Tabular Data", "", FILTER)
    # unrelated paper must stay out
    assert not ar._matches(
        "Scaling Laws for Speech Models",
        "We evaluate on three benchmarks and report WER.",
        FILTER,
    )


def test_card_shows_autonomy_and_links():
    p = Paper(
        source="arxiv", paper_id="2611.00001", title="AutoResearcher", authors=["A", "B"],
        abstract="a", url="https://arxiv.org/abs/2611.00001",
        pdf_url="https://arxiv.org/pdf/2611.00001", venue="arXiv",
        venue_track="cs.CL", track="ai-auto-research", score=9,
        bench_type="semi_autonomous", what_it_measures="自动化选题到实验，人只审最终稿",
        summary_zh="摘要。", why_relevant="值得看。", key_techniques=["code execution sandbox"],
        arxiv_id="2611.00001",
    )
    text = "\n".join(ar.card(p, 1))
    assert "### 1. AutoResearcher" in text
    assert "[论文页](https://arxiv.org/abs/2611.00001)" in text
    assert "[arXiv](https://arxiv.org/abs/2611.00001)" in text
    assert "相关性 9/10" in text
    assert "自动化程度 `semi_autonomous`" in text
    assert "自动化选题到实验，人只审最终稿" in text


def test_if_missing_short_circuits_without_fetch(tmp_path, monkeypatch):
    page = tmp_path / "2026-11-10.md"
    page.write_text("# already rendered\n", encoding="utf-8")
    monkeypatch.setattr(ar, "DAILY_DIR", tmp_path)

    def _boom(*args, **kwargs):
        raise AssertionError("fetch must not run when the page already exists")

    monkeypatch.setattr(ar, "fetch_arxiv", _boom)
    assert ar.daily(date(2026, 11, 10), skip_existing=True) == page
