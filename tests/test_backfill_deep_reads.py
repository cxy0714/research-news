"""Tests for the deep-read backfill selection logic (no LLM, no network)."""
from __future__ import annotations

import json

from research_news import backfill_deep_reads as bf


def _write_scores(path, rows):
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


def test_qualifying_papers_filters_threshold_date_and_existing(tmp_path, monkeypatch):
    rows = [
        # qualifies: right date, score >= 6, not yet deep-read
        {"run_date": "2026-05-29", "paper_id": "a", "source": "arxiv",
         "title": "A", "abstract": "x", "score": 7.0, "topic": "causal_inference"},
        # below threshold → excluded
        {"run_date": "2026-05-29", "paper_id": "b", "source": "arxiv",
         "title": "B", "abstract": "x", "score": 5.0},
        # wrong date → excluded
        {"run_date": "2026-05-28", "paper_id": "c", "source": "arxiv",
         "title": "C", "abstract": "x", "score": 9.0},
        # already deep-read on this date → excluded
        {"run_date": "2026-05-29", "paper_id": "d", "source": "arxiv",
         "title": "D", "abstract": "x", "score": 8.0},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)

    # Point the real score-log loader at our temp file, and stub the deep-read index.
    from research_news import rerun
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)
    monkeypatch.setattr(bf, "load_score_index", rerun.load_score_index)
    monkeypatch.setattr(bf, "load_index",
                        lambda: [{"paper_id": "d", "date": "2026-05-29"}])

    papers = bf.qualifying_papers("2026-05-29", 6.0)
    ids = [p.paper_id for p in papers]
    assert ids == ["a"]  # only 'a' survives all four filters
    assert papers[0].score == 7.0


def test_qualifying_papers_dedup_keeps_highest_score(tmp_path, monkeypatch):
    rows = [
        {"run_date": "2026-05-29", "paper_id": "a", "source": "arxiv",
         "title": "A", "abstract": "x", "score": 6.0},
        {"run_date": "2026-05-29", "paper_id": "a", "source": "arxiv",
         "title": "A", "abstract": "x", "score": 9.0},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    from research_news import rerun
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)
    monkeypatch.setattr(bf, "load_score_index", rerun.load_score_index)
    monkeypatch.setattr(bf, "load_index", lambda: [])

    papers = bf.qualifying_papers("2026-05-29", 6.0)
    assert len(papers) == 1
    assert papers[0].score == 9.0


def test_qualifying_papers_source_filter(tmp_path, monkeypatch):
    rows = [
        {"run_date": "2026-05-29", "paper_id": "a", "source": "arxiv",
         "title": "A", "abstract": "x", "score": 7.0},
        {"run_date": "2026-05-29", "paper_id": "j", "source": "jmlr",
         "title": "J", "abstract": "x", "score": 7.0},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    from research_news import rerun
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)
    monkeypatch.setattr(bf, "load_score_index", rerun.load_score_index)
    monkeypatch.setattr(bf, "load_index", lambda: [])

    papers = bf.qualifying_papers("2026-05-29", 6.0, sources={"arxiv"})
    assert [p.paper_id for p in papers] == ["a"]
