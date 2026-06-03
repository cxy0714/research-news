"""Tests for the citation-edge store (no network)."""
from __future__ import annotations

import json

from research_news import citations as cit


def test_edge_from_row_extracts_ids_and_signals():
    row = {
        "isInfluential": True,
        "intents": ["methodology"],
        "citedPaper": {
            "paperId": "s2abc",
            "title": "A Foundational Result",
            "year": 2019,
            "citationCount": 321,
            "externalIds": {"ArXiv": "1901.01234", "DOI": "10.1/xyz"},
        },
    }
    e = cit.edge_from_row(row)
    assert e["arxiv"] == "1901.01234"
    assert e["doi"] == "10.1/xyz"
    assert e["s2"] == "s2abc"
    assert e["is_influential"] is True
    assert e["intents"] == ["methodology"]
    assert e["citation_count"] == 321
    assert e["year"] == 2019


def test_edge_from_row_keeps_rows_without_abstract():
    # No abstract, but it still has identifiers — must be kept (the whole point).
    row = {"citedPaper": {"paperId": "x", "externalIds": {"DOI": "10.2/aaa"}}}
    assert cit.edge_from_row(row) is not None


def test_edge_from_row_drops_unidentifiable():
    row = {"citedPaper": {"title": "Mystery paper", "externalIds": {}}}
    assert cit.edge_from_row(row) is None


def test_build_record_counts_total_vs_identified():
    rows = [
        {"citedPaper": {"externalIds": {"ArXiv": "2001.00001"}}},
        {"citedPaper": {"externalIds": {}}},            # unidentifiable -> dropped
        {"citedPaper": {"paperId": "s2only"}},          # s2 id only -> kept
    ]
    rec = cit.build_record("2605.28341", "2605.28341", rows, fetched="2026-06-03")
    assert rec["n_references_total"] == 3
    assert rec["n_references_identified"] == 2
    assert rec["paper_id"] == "2605.28341"


def test_save_record_upserts_by_paper_id(tmp_path):
    path = tmp_path / "citations.json"
    cit.save_record(cit.build_record("p1", "p1", [
        {"citedPaper": {"externalIds": {"ArXiv": "1"}}}], fetched="2026-06-01"), path)
    # Re-run of the same paper replaces, doesn't duplicate.
    cit.save_record(cit.build_record("p1", "p1", [
        {"citedPaper": {"externalIds": {"ArXiv": "1"}}},
        {"citedPaper": {"externalIds": {"ArXiv": "2"}}}], fetched="2026-06-03"), path)
    cit.save_record(cit.build_record("p2", "p2", [], fetched="2026-06-02"), path)

    data = json.loads(path.read_text(encoding="utf-8"))
    by_id = {e["paper_id"]: e for e in data}
    assert len(data) == 2                       # p1 upserted, not duplicated
    assert by_id["p1"]["n_references_total"] == 2
    assert data[0]["paper_id"] == "p1"          # sorted by fetched desc
