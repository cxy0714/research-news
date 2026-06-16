"""Tests for the summary-promotion backfill: the page parser must round-trip
existing content byte-for-byte, and promotion must move a 🗂 paper up while
shrinking the 🗂 section. The LLM summariser is stubbed (no API, no network)."""
from __future__ import annotations

import json
from datetime import date

from research_news import backfill_summaries as bs
from research_news import rerun
from research_news.models import Paper
from research_news.render import markdown as md


def _write_scores(path, rows):
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


# ── parser round-trips (the safety guarantee for existing content) ────────────

def test_rerender_unchanged_is_byte_identical_on_tricky_fields(tmp_path):
    """A digest paper with the awkward cases — >6 authors, commas inside an
    affiliation, >8 institutions, and a CR + newline inside the summary — must
    re-render to exactly the same bytes."""
    p = Paper(
        source="arxiv", paper_id="2606.0001",
        title="A tricky paper — with dash",
        authors=["M. Griggio (Inst, City, US)", "B B", "C C", "D D", "E E", "F F", "G G"],
        abstract="", url="https://arxiv.org/abs/2606.0001",
        categories=["stat.ME", "math.ST"],
        institutions=[f"Institute {i}" for i in range(10)],  # >8 → '… 等'
        score=7.0, novelty_flag="new_method",
        summary_zh="核心 estimand 为 $\rho(X,Y)$（含 CR）\n第二行补充说明。",  # CR + LF
        key_techniques=["cross-fitting", "orthogonal score"],
        why_relevant="连接 efficiency theory。",
    )
    page = md.render_daily([p], [], [], [], when=date(2026, 6, 12), output_dir=tmp_path)

    text = bs._read_raw(page)
    out = bs._rerender_unchanged(text, {}, "2026-06-12")
    assert out == text


def test_rerender_unchanged_preserves_low_section(tmp_path, monkeypatch):
    """Existing digest + 🗂 papers both survive a no-promote re-render."""
    digest = Paper(source="arxiv", paper_id="2606.0001", title="Digest", authors=["X"],
                   abstract="", url="https://arxiv.org/abs/2606.0001",
                   categories=["stat.ME"], score=7.0, topic="causal_inference",
                   summary_zh="摘要。")
    low = Paper(source="arxiv", paper_id="2606.0002", title="Low", authors=["Y"],
                abstract="", url="https://arxiv.org/abs/2606.0002",
                categories=["stat.AP"], score=2.0, score_reason="tangential")
    page = md.render_daily([], [digest], [low], [], when=date(2026, 6, 12), output_dir=tmp_path)

    rows = [
        {"run_date": "2026-06-12", "paper_id": "2606.0002", "source": "arxiv",
         "title": "Low", "abstract": "", "score": 2.0, "score_reason": "tangential",
         "categories": ["stat.AP"], "authors": ["Y"],
         "url": "https://arxiv.org/abs/2606.0002"},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)

    text = bs._read_raw(page)
    best = bs.rows_for_date(rerun.load_score_index(), "2026-06-12")
    assert bs._rerender_unchanged(text, best, "2026-06-12") == text


# ── promotion ─────────────────────────────────────────────────────────────────

def _fake_summarize(client, paper, interests, *, model=None, **kw):
    paper.summary_zh = "新生成的中文摘要。"
    paper.topic = "causal_inference"
    paper.why_relevant = "因为相关。"
    paper.key_techniques = ["technique"]
    paper.novelty_flag = "new_method"
    return {}


def test_promote_moves_paper_up_and_shrinks_low(tmp_path, monkeypatch):
    # Page: one mid digest paper, plus a 🗂 holding an above-threshold paper
    # ('HI', score 6 — stuck by the old cap) and a below-threshold one ('LO').
    digest = Paper(source="arxiv", paper_id="2606.0001", title="Digest", authors=["X"],
                   abstract="", url="https://arxiv.org/abs/2606.0001",
                   categories=["stat.ME"], score=5.0, topic="causal_inference",
                   summary_zh="已有摘要。")
    hi = Paper(source="arxiv", paper_id="2606.00HI", title="Stuck high scorer",
               authors=["A"], abstract="", url="https://arxiv.org/abs/2606.00HI",
               categories=["stat.ME"], score=6.0, score_reason="relevant enough")
    lo = Paper(source="arxiv", paper_id="2606.00LO", title="Genuinely low",
               authors=["B"], abstract="", url="https://arxiv.org/abs/2606.00LO",
               categories=["stat.AP"], score=2.0, score_reason="tangential")
    page = md.render_daily([], [digest], [hi, lo], [], when=date(2026, 6, 12),
                           output_dir=tmp_path)

    rows = [
        {"run_date": "2026-06-12", "paper_id": "2606.00HI", "source": "arxiv",
         "title": "Stuck high scorer", "abstract": "real abstract here", "score": 6.0,
         "score_reason": "relevant enough", "categories": ["stat.ME"], "authors": ["A"],
         "url": "https://arxiv.org/abs/2606.00HI"},
        {"run_date": "2026-06-12", "paper_id": "2606.00LO", "source": "arxiv",
         "title": "Genuinely low", "abstract": "x", "score": 2.0,
         "score_reason": "tangential", "categories": ["stat.AP"], "authors": ["B"],
         "url": "https://arxiv.org/abs/2606.00LO"},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)
    monkeypatch.setattr("research_news.llm.pipeline.summarize_paper", _fake_summarize)
    monkeypatch.setattr(
        "research_news.scrapers.affiliations.backfill_affiliations", lambda papers: None
    )

    score_index = rerun.load_score_index()
    n = bs.backfill_page(page, score_index, client=object(), interests_text="",
                         model="x", dry_run=False, self_check=False)
    assert n == 1

    text = bs._read_raw(page)
    # HI got summarised and moved into a topic-grouped section (📌/⭐), not 🗂.
    assert "新生成的中文摘要。" in text
    low_part = text.split(md.LOW_SECTION_HEADING, 1)[1]
    assert "2606.00LO" in low_part        # genuinely-low stays
    assert "2606.00HI" not in low_part    # promoted out of 🗂
    # The existing digest paper's summary is untouched.
    assert "已有摘要。" in text


def test_dry_run_promotes_nothing(tmp_path, monkeypatch):
    digest = Paper(source="arxiv", paper_id="2606.0001", title="Digest", authors=["X"],
                   abstract="", url="https://arxiv.org/abs/2606.0001",
                   categories=["stat.ME"], score=5.0, topic="causal_inference",
                   summary_zh="已有摘要。")
    hi = Paper(source="arxiv", paper_id="2606.00HI", title="Stuck", authors=["A"],
               abstract="", url="https://arxiv.org/abs/2606.00HI",
               categories=["stat.ME"], score=6.0, score_reason="r")
    page = md.render_daily([], [digest], [hi], [], when=date(2026, 6, 12),
                           output_dir=tmp_path)
    before = bs._read_raw(page)

    rows = [{"run_date": "2026-06-12", "paper_id": "2606.00HI", "source": "arxiv",
             "title": "Stuck", "abstract": "a", "score": 6.0, "score_reason": "r",
             "categories": ["stat.ME"], "authors": ["A"],
             "url": "https://arxiv.org/abs/2606.00HI"}]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)

    n = bs.backfill_page(page, rerun.load_score_index(), client=None,
                         interests_text="", model="x", dry_run=True, self_check=False)
    assert n == 1                          # reports it would promote 1
    assert bs._read_raw(page) == before    # but writes nothing
