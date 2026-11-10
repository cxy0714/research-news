"""Tests for the AI evaluation / benchmark track."""
from __future__ import annotations

from research_news import benchmarks as b
from research_news.models import Paper
from research_news.scrapers import proceedings as proc

FILTER = {
    "title_patterns": [r"\bbenchmark", r"\bevaluat", r"\bmetric", r"\bjudge"],
    "deny_title_patterns": [r"\bmetric learning"],
}


def _acl_fixture() -> str:
    return """
    <html><body>
      <div class="d-sm-flex align-items-stretch mb-3">
        <div class="d-block me-2 list-button-row">
          <a href="https://aclanthology.org/2026.acl-long.1.pdf">pdf</a>
        </div>
        <span class="d-block">
          <strong><a href="/2026.acl-long.1/">Octo<span class="acl-fixed-case">T</span>ools: A Benchmark for <span class="acl-fixed-case">LLM</span>s</a></strong>
          <br/><a href="/people/pan-lu/">Pan Lu</a> | <a href="/people/bowen-chen/">Bowen Chen</a>
        </span>
      </div>
      <div class="collapse" id="abstract-2026--acl-long--1">
        We introduce OctoTools, a benchmark of 100 tasks.
      </div>
    </body></html>
    """


def test_matches_title_only():
    assert b._matches("A New Benchmark for LLM Agents", "", FILTER)
    assert b._matches("Evaluating Factuality in Long Documents", "", FILTER)
    # deny wins over allow
    assert not b._matches("Deep Metric Learning for Faces", "", FILTER)
    # abstract-only mention must NOT pull a paper in (the 62%-of-EMNLP failure mode)
    assert not b._matches("Scaling Laws for Speech Models", "We evaluate on three benchmarks.", FILTER)


def test_acl_volume_parses_inline_abstract(monkeypatch):
    monkeypatch.setattr(proc, "fetch", lambda url, **kw: _acl_fixture())
    papers = proc.acl_volume("2026.acl-long", venue_id="acl2026", label="ACL 2026")
    assert len(papers) == 1
    p = papers[0]
    assert p.source == "acl2026"
    assert p.paper_id == "acl2026:2026.acl-long.1"
    assert p.title == "OctoTools: A Benchmark for LLMs"   # no lost space around spans
    assert p.authors == ["Pan Lu", "Bowen Chen"]
    assert p.abstract.startswith("We introduce OctoTools")
    assert p.pdf_url.endswith("2026.acl-long.1.pdf")
    assert p.track == "ai"
    assert p.venue_track == "acl-long"


def test_paper_new_fields_roundtrip():
    p = Paper(
        source="icml2026", paper_id="icml2026:abc", title="T", authors=[],
        abstract="A", url="u", track="ai", venue_id="icml2026",
        venue_track="Main", bench_type="benchmark", what_it_measures="x",
        openreview_id="or1", arxiv_id="2501.00001",
    )
    d = p.to_dict()
    restored = Paper(**{k: v for k, v in d.items() if k in b._PAPER_FIELDS})
    assert restored.track == "ai"
    assert restored.venue_track == "Main"
    assert restored.bench_type == "benchmark"
    assert restored.openreview_id == "or1"


def test_paged_names():
    items = [Paper(source="s", paper_id=str(i), title=f"t{i}", authors=[], abstract="a", url="u")
             for i in range(5)]
    pages = b._paged("methodology", items, 2)
    assert [name for name, _ in pages] == [
        "methodology.md", "methodology-2.md", "methodology-3.md"
    ]
    assert [len(chunk) for _, chunk in pages] == [2, 2, 1]
    assert b._paged("x", [], 10) == []


def test_card_has_links_and_measure():
    p = Paper(
        source="emnlp2025", paper_id="emnlp2025:1", title="Benchmark X", authors=["A", "B"],
        abstract="a", url="https://example.org/p", pdf_url="https://example.org/p.pdf",
        venue="EMNLP 2025", venue_track="Main", track="ai", score=8,
        bench_type="benchmark", what_it_measures="多步工具调用的规划鲁棒性",
        summary_zh="摘要。", why_relevant="值得看。", key_techniques=["contamination audit"],
    )
    text = "\n".join(b.card(p, 1))
    assert "### 1. Benchmark X" in text
    assert "[论文页](https://example.org/p)" in text
    assert "[PDF](https://example.org/p.pdf)" in text
    assert "相关性 8/10" in text
    assert "多步工具调用的规划鲁棒性" in text
    assert "`contamination audit`" in text
