"""Offline tests for the Semantic Scholar references helper.

No network is touched — we feed fake S2 payloads to the pure functions.
"""
from __future__ import annotations

from research_news.scrapers import references as refs


def test_extract_arxiv_id():
    assert refs.extract_arxiv_id("https://arxiv.org/abs/2401.01234") == "2401.01234"
    assert refs.extract_arxiv_id("2401.01234v3") == "2401.01234"
    assert refs.extract_arxiv_id("arXiv:1912.12345") == "1912.12345"
    assert refs.extract_arxiv_id(None, "", "math.ST/0123456") == "math.ST/0123456"
    assert refs.extract_arxiv_id(None, "not-an-id") is None


def _row(title, *, infl=False, intents=None, cites=0, abstract="abc"):
    return {
        "isInfluential": infl,
        "intents": intents or [],
        "contexts": [f"we build on {title}"],
        "citedPaper": {
            "title": title,
            "abstract": abstract,
            "year": 2020,
            "citationCount": cites,
            "authors": [{"name": "A. Author"}],
        },
    }


def test_select_ranks_influential_and_drops_abstractless():
    rows = [
        _row("low", infl=False, intents=[], cites=1),
        _row("infl", infl=True, intents=["background"], cites=5),
        _row("noabs", infl=True, abstract=None),  # dropped: no abstract
        _row("method", infl=False, intents=["methodology"], cites=2),
    ]
    sel = refs.select_key_references(rows, top_n=10)
    titles = [r["citedPaper"]["title"] for r in sel]
    assert "noabs" not in titles            # abstractless dropped
    assert titles[0] == "infl"              # influential first
    assert titles.index("method") < titles.index("low")  # intent beats bare cite


def test_format_block_empty_when_nothing_usable():
    assert refs.format_references_block([]) == ""
    assert refs.format_references_block([_row("x", abstract=None)]) == ""


def test_format_block_renders_markdown():
    block = refs.format_references_block([_row("Key Paper", infl=True, intents=["background"])])
    assert "主要被引论文" in block
    assert "Key Paper" in block
    assert "influential" in block
    assert "摘要：" in block
