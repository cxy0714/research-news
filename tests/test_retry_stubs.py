"""Tests for failed-deep-read (stub) recovery selection — no LLM, no network."""
from __future__ import annotations

from research_news import backfill_deep_reads as bf
from research_news.deep_read import DEEP_READ_FAILED_MARKER


def _stub_page(path):
    path.write_text(f"# Title\n\n**作者**: X  \n\n---\n\n{DEEP_READ_FAILED_MARKER}\n",
                    encoding="utf-8")


def _good_page(path):
    path.write_text("# Title\n\n## 一、综述\n\nreal deep-read content\n", encoding="utf-8")


def test_find_stub_entries_indexed_filename_fallback_and_excludes_good(tmp_path, monkeypatch):
    dr = tmp_path / "deep_reads"
    dr.mkdir()
    _stub_page(dr / "2026-06-17-2606.0001.md")   # stub, in index
    _stub_page(dr / "2026-06-17-2606.0002.md")   # stub, NOT in index → filename fallback
    _good_page(dr / "2026-06-17-2606.0003.md")   # not a stub → excluded
    index = [{"paper_id": "2606.0001", "date": "2026-06-17",
              "doc_path": "deep_reads/2026-06-17-2606.0001.md",
              "topic": "causal_inference", "score": 8}]
    monkeypatch.setattr(bf, "DEEP_READS_DIR", dr)
    monkeypatch.setattr(bf, "load_index", lambda: index)

    entries = bf.find_stub_entries()
    by_id = {e["paper_id"]: e for e in entries}
    assert sorted(by_id) == ["2606.0001", "2606.0002"]      # good page excluded
    assert by_id["2606.0001"]["topic"] == "causal_inference"  # indexed metadata kept
    assert by_id["2606.0002"]["date"] == "2026-06-17"         # recovered from filename
    assert by_id["2606.0002"]["topic"] is None


def test_find_stub_entries_date_scope(tmp_path, monkeypatch):
    dr = tmp_path / "deep_reads"
    dr.mkdir()
    _stub_page(dr / "2026-06-16-2606.0001.md")
    _stub_page(dr / "2026-06-17-2606.0002.md")
    monkeypatch.setattr(bf, "DEEP_READS_DIR", dr)
    monkeypatch.setattr(bf, "load_index", lambda: [])

    assert {e["paper_id"] for e in bf.find_stub_entries(dates={"2026-06-17"})} == {"2606.0002"}
    assert len(bf.find_stub_entries()) == 2  # no filter → both


def test_stub_papers_reconstructs_from_log_and_patches_metadata():
    entries = [
        # indexed: score/topic/title come from the index entry
        {"paper_id": "2606.0001", "date": "2026-06-17",
         "topic": "causal_inference", "score": 8, "title": "Index Title"},
        # filename-fallback: score/topic/title come from the score-log row
        {"paper_id": "2606.0002", "date": "2026-06-17",
         "topic": None, "score": None, "title": None},
    ]
    score_index = {
        "2606.0001": [{"run_date": "2026-06-17", "paper_id": "2606.0001",
                       "title": "Log Title", "abstract": "abs1", "authors": ["A"],
                       "score": 8.0, "topic": "causal_inference"}],
        "2606.0002": [{"run_date": "2026-06-17", "paper_id": "2606.0002",
                       "title": "Log T2", "abstract": "abs2", "authors": ["B"],
                       "score": 7.0, "topic": "hypothesis_testing"}],
    }
    papers = {p.paper_id: p for p in bf.stub_papers(entries, score_index, "2026-06-17")}
    assert len(papers) == 2
    assert papers["2606.0001"].abstract == "abs1"        # rebuilt from the log
    assert papers["2606.0001"].score == 8.0
    assert papers["2606.0002"].topic == "hypothesis_testing"  # from log row
    assert papers["2606.0002"].score == 7.0


def test_stub_papers_skips_papers_missing_from_log():
    entries = [{"paper_id": "missing", "date": "2026-06-17",
                "topic": None, "score": None, "title": None}]
    assert bf.stub_papers(entries, {}, "2026-06-17") == []
