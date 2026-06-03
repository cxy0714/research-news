"""Tests for the OpenAlex references fallback (pure logic; no network)."""
from __future__ import annotations

from research_news.scrapers import references as r


def test_reconstruct_abstract_orders_by_position():
    inv = {"Causal": [0], "inference": [1], "is": [2], "hard": [3]}
    assert r._reconstruct_abstract(inv) == "Causal inference is hard"
    assert r._reconstruct_abstract(None) == ""
    assert r._reconstruct_abstract({}) == ""


def test_bare_doi_strips_url_prefix():
    assert r._bare_doi("https://doi.org/10.1/abc") == "10.1/abc"
    assert r._bare_doi("10.1/abc") == "10.1/abc"
    assert r._bare_doi(None) is None


def test_openalex_work_to_cited_shape_and_arxiv_recovery():
    work = {
        "id": "https://openalex.org/W42",
        "ids": {"openalex": "https://openalex.org/W42"},
        "doi": "https://doi.org/10.48550/arXiv.2401.01234",
        "title": "A Cited Work",
        "publication_year": 2024,
        "cited_by_count": 88,
        "abstract_inverted_index": {"hello": [0], "world": [1]},
        "authorships": [{"author": {"display_name": "Jane Roe"}}],
        "primary_location": {"source": {"display_name": "Annals"}},
    }
    c = r._openalex_work_to_cited(work)
    assert c["paperId"] == "W42"
    assert c["externalIds"]["DOI"] == "10.48550/arXiv.2401.01234"
    assert c["externalIds"]["ArXiv"] == "2401.01234"   # recovered from the DOI
    assert c["abstract"] == "hello world"
    assert c["citationCount"] == 88
    assert c["authors"] == [{"name": "Jane Roe"}]
    assert c["venue"] == "Annals"
    # this normalized row must be usable by the S2-shaped selection helper
    row = {"isInfluential": False, "intents": [], "contexts": [], "citedPaper": c}
    assert r.select_key_references([row]) == [row]   # has an abstract -> usable


def test_fetch_references_best_prefers_s2_then_openalex(monkeypatch):
    s2_usable = [{"citedPaper": {"abstract": "a"}, "isInfluential": True, "intents": []}]
    oa_usable = [{"citedPaper": {"abstract": "b"}, "isInfluential": False, "intents": []}]

    # 1) S2 has usable refs -> use S2, don't even call OpenAlex
    called = {"oa": False}
    monkeypatch.setattr(r, "fetch_references", lambda a, **k: s2_usable)
    monkeypatch.setattr(r, "fetch_references_openalex",
                        lambda a, **k: called.__setitem__("oa", True) or oa_usable)
    rows, src = r.fetch_references_best("2401.00001")
    assert src == "s2" and rows is s2_usable and called["oa"] is False

    # 2) S2 empty -> fall back to OpenAlex
    monkeypatch.setattr(r, "fetch_references", lambda a, **k: [])
    monkeypatch.setattr(r, "fetch_references_openalex", lambda a, **k: oa_usable)
    rows, src = r.fetch_references_best("2401.00001")
    assert src == "openalex" and rows is oa_usable

    # 3) both empty -> "none"
    monkeypatch.setattr(r, "fetch_references", lambda a, **k: [])
    monkeypatch.setattr(r, "fetch_references_openalex", lambda a, **k: [])
    rows, src = r.fetch_references_best("2401.00001")
    assert src == "none" and rows == []

    # 4) S2 has rows but no abstracts (edges only), OpenAlex none -> keep S2 for graph
    s2_no_abs = [{"citedPaper": {"externalIds": {"DOI": "10.1/x"}}, "intents": []}]
    monkeypatch.setattr(r, "fetch_references", lambda a, **k: s2_no_abs)
    monkeypatch.setattr(r, "fetch_references_openalex", lambda a, **k: [])
    rows, src = r.fetch_references_best("2401.00001")
    assert src == "s2" and rows is s2_no_abs
