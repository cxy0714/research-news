"""Tests for the 'show all papers' daily feature: the shared low-relevance
renderer and the retroactive backfill (no LLM, no network)."""
from __future__ import annotations

import json
from datetime import date

from research_news import backfill_low_relevance as blr
from research_news import rerun
from research_news.models import Paper
from research_news.render import markdown as md


def _write_scores(path, rows):
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


# ── shared renderer ───────────────────────────────────────────────────────────

def test_count_line_shows_low_only_when_nonzero():
    assert md.format_daily_count_line(2, 3, 0, 0) == \
        "- 高相关论文 2 篇 · 中相关 3 篇 · 会议/Seminar 事件 0 条"
    assert md.format_daily_count_line(2, 3, 5, 1) == \
        "- 高相关论文 2 篇 · 中相关 3 篇 · 其他 5 篇 · 会议/Seminar 事件 1 条"


def test_render_low_section_empty():
    assert md.render_low_section([]) == []


def test_render_low_section_orders_and_shows_score_and_reason():
    p_lo = Paper(source="arxiv", paper_id="2606.0002", title="Low",
                 authors=["A", "B"], abstract="", url="https://arxiv.org/abs/2606.0002",
                 categories=["stat.AP"], score=1.0, score_reason="tangential work")
    p_hi = Paper(source="arxiv", paper_id="2606.0003", title="Higher",
                 authors=["C"], abstract="", url="https://arxiv.org/abs/2606.0003",
                 categories=["math.ST"], score=3.0, score_reason="some overlap")
    text = "\n".join(md.render_low_section([p_lo, p_hi]))

    assert md.LOW_SECTION_HEADING in text
    # Highest score first → 2606.0003 numbered 1, the score 1 paper numbered 2.
    assert text.index("2606.0003") < text.index("2606.0002")
    assert "### 1. [2606.0003]" in text
    assert "### 2. [2606.0002]" in text
    # Score + the stored reason are surfaced (no Chinese summary for these).
    assert "相关性 1/10" in text
    assert "**评分理由**: tangential work" in text
    assert "**摘要**" not in text


# ── score-log row selection ───────────────────────────────────────────────────

def test_rows_for_date_filters_date_source_and_dedups(tmp_path, monkeypatch):
    rows = [
        {"run_date": "2026-06-12", "paper_id": "a", "source": "arxiv", "score": 2.0},
        {"run_date": "2026-06-12", "paper_id": "a", "source": "arxiv", "score": 5.0},
        {"run_date": "2026-06-11", "paper_id": "b", "source": "arxiv", "score": 9.0},
        {"run_date": "2026-06-12", "paper_id": "j", "source": "jmlr", "score": 7.0},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)

    best = blr.rows_for_date(rerun.load_score_index(), "2026-06-12")
    assert set(best) == {"a"}          # wrong-date 'b' + journal 'j' excluded
    assert best["a"]["score"] == 5.0   # dedup keeps the highest score


# ── end-to-end backfill on a real rendered page ───────────────────────────────

def _make_page(tmp_path):
    """A real daily page with one summarised digest paper 'a'."""
    a = Paper(source="arxiv", paper_id="2606.0001", title="Digest paper",
              authors=["X"], abstract="", url="https://arxiv.org/abs/2606.0001",
              categories=["stat.ME"], score=7.0, topic="causal_inference",
              summary_zh="这是已生成的中文摘要。")
    return md.render_daily([], [a], [], [], when=date(2026, 6, 12),
                           output_dir=tmp_path)


def test_backfill_adds_low_section_and_is_idempotent(tmp_path, monkeypatch):
    page = _make_page(tmp_path)

    rows = [
        # 'a' is the digest paper already on the page → must NOT be duplicated.
        {"run_date": "2026-06-12", "paper_id": "2606.0001", "source": "arxiv",
         "title": "Digest paper", "abstract": "", "score": 7.0,
         "score_reason": "directly relevant", "categories": ["stat.ME"],
         "authors": ["X"], "url": "https://arxiv.org/abs/2606.0001"},
        # 'b' was dropped (below threshold) → recovered into the 🗂 section.
        {"run_date": "2026-06-12", "paper_id": "2606.0002", "source": "arxiv",
         "title": "Dropped paper", "abstract": "", "score": 2.0,
         "score_reason": "tangential to interests", "categories": ["stat.AP"],
         "authors": ["Y", "Z"], "url": "https://arxiv.org/abs/2606.0002"},
        # journal-pipeline row on the same date → excluded (source filter).
        {"run_date": "2026-06-12", "paper_id": "J1", "source": "jmlr",
         "title": "Journal", "abstract": "", "score": 2.0, "score_reason": "n/a"},
    ]
    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, rows)
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)

    n = blr.run(date_str="2026-06-12", daily_dir=tmp_path)
    assert n == 1

    text = page.read_text(encoding="utf-8")
    assert md.LOW_SECTION_HEADING in text
    assert "2606.0002" in text and "tangential to interests" in text
    assert "J1" not in text                      # journal row excluded
    # The summarised digest paper must not be re-listed in the 🗂 section.
    low_part = text.split(md.LOW_SECTION_HEADING, 1)[1]
    assert "2606.0001" not in low_part
    assert "2606.0002" in low_part
    assert "· 其他 1 篇" in text                 # count line refreshed
    assert "这是已生成的中文摘要。" in text       # existing summary preserved

    # Re-running writes nothing new (idempotent) and keeps a single footer.
    before = text
    blr.run(date_str="2026-06-12", daily_dir=tmp_path)
    after = page.read_text(encoding="utf-8")
    assert after == before
    assert after.count("\n---\n") == 1
    assert after.count(md.LOW_SECTION_HEADING) == 1


def test_backfill_no_rows_leaves_page_untouched(tmp_path, monkeypatch):
    page = _make_page(tmp_path)
    original = page.read_text(encoding="utf-8")

    score_file = tmp_path / "llm_scores.jsonl"
    _write_scores(score_file, [
        {"run_date": "2026-06-11", "paper_id": "x", "source": "arxiv", "score": 1.0},
    ])
    monkeypatch.setattr(rerun, "SCORE_LOG_FILE", score_file)

    # No arXiv rows for 2026-06-12 → page is skipped, bytes unchanged.
    blr.run(date_str="2026-06-12", daily_dir=tmp_path)
    assert page.read_text(encoding="utf-8") == original
