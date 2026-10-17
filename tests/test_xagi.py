"""Offline tests for the XAGI 2026 conference pipeline (no network, no LLM).

Covers the deterministic halves: parsing the saved schedule page, preserving
match state when re-importing, the paper-match scoring, and the one-cell-at-a-
time queue driver.
"""
from __future__ import annotations

from datetime import date

import pytest

from research_news import xagi
from research_news.scrapers import xagi as scrape

SESSION_HTML = """
<section class="schedule-period-group" id="schedule-1017-am">
  <header class="schedule-period-heading"><h3>10 月 17 日 · 周六 · 上午</h3></header>
  <div class="schedule-period-cards">
    <article class="info-card schedule-card schedule-topic-card" id="schedule-session-01">
      <div class="card-header">
        <span class="schedule-topic-card__heading">
          <span class="schedule-topic-card__number">Session 01</span>
          <span class="schedule-topic-card__title">Keynote</span>
          <span class="schedule-topic-card__time">08:45-12:00</span>
          <span class="schedule-topic-card__location">
            <span data-session-venue>聚英厅</span>
            <span data-session-venue-detail>（友谊宫二层）</span>
          </span>
        </span>
      </div>
      <section class="session-chair" aria-label="Chair">
        <details class="schedule-person-profile schedule-person-profile--chair">
          <summary><span class="schedule-person-profile__summary-copy schedule-person-identity">
            <strong>王健桥</strong>
            <span class="schedule-person-identity__affiliation">
              <span class="schedule-person-identity__affiliation-text">清华大学</span>
            </span>
          </span></summary>
          <div class="schedule-person-profile__details">
            <div class="schedule-person-profile__copy">
              <section data-profile-section="bio">
                <h4>Chair 简介</h4>
                <p class="schedule-person-profile__affiliation">清华大学 · 统计与数据科学系</p>
                <p>王健桥，助理教授。</p>
              </section>
            </div>
          </div>
        </details>
      </section>
      <div class="card-body">
        <div class="session-list">
          <div class="session-item session-item--speaker">
            <div class="session-speaker">
              <p class="session-speaker__talk-title">
                <span>人工智能随想录</span>
                <span class="schedule-inline-time">09:10-10:00</span>
              </p>
              <details class="schedule-person-profile schedule-person-profile--speaker">
                <summary><span class="schedule-person-profile__summary-copy schedule-person-identity">
                  <strong>孙茂松</strong>
                  <span class="schedule-person-identity__affiliation">
                    <span class="schedule-person-identity__affiliation-text">清华大学</span>
                  </span>
                </span></summary>
                <div class="schedule-person-profile__details">
                  <div class="schedule-person-profile__copy">
                    <section data-profile-section="abstract">
                      <h4>演讲摘要</h4>
                      <p>本报告讨论生成式人工智能的基本问题。</p>
                    </section>
                    <section data-profile-section="bio">
                      <h4>嘉宾介绍</h4>
                      <p class="schedule-person-profile__affiliation">清华大学 · 计算机科学与技术系</p>
                      <p>孙茂松，清华大学教授。</p>
                    </section>
                  </div>
                </div>
              </details>
            </div>
          </div>
          <div class="session-item session-item--interlude">
            <span>茶歇</span><span class="schedule-inline-time">10:50-11:10</span>
          </div>
          <div class="session-item session-item--speaker">
            <div class="session-speaker">
              <p class="session-speaker__talk-title">
                <span>Neuroscience Where AI = Science</span>
                <span class="schedule-inline-time">10:00-10:50</span>
              </p>
              <details class="schedule-person-profile schedule-person-profile--speaker">
                <summary><span class="schedule-person-profile__summary-copy schedule-person-identity">
                  <strong>冯建峰</strong>
                  <span class="schedule-person-identity__affiliation">
                    <span class="schedule-person-identity__affiliation-text">复旦大学</span>
                  </span>
                </span></summary>
                <div class="schedule-person-profile__details">
                  <div class="schedule-person-profile__copy">
                    <section data-profile-section="abstract">
                      <h4>演讲摘要</h4>
                      <p>We present the Digital Twin Brain.</p>
                    </section>
                    <section data-profile-section="bio">
                      <h4>嘉宾介绍</h4>
                      <p class="schedule-person-profile__affiliation">复旦大学 · 类脑研究院</p>
                      <p>冯建峰，复旦大学教授。</p>
                    </section>
                  </div>
                </div>
              </details>
            </div>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
"""


@pytest.fixture()
def catalog() -> dict:
    return scrape.parse_schedule(SESSION_HTML)


# ── schedule parsing ─────────────────────────────────────────────────────────

def test_parse_sessions_and_talks(catalog):
    assert len(catalog["sessions"]) == 1
    s = catalog["sessions"][0]
    assert s["no"] == 1
    assert s["id"] == "sess01"
    assert s["date"] == "2026-10-17"
    assert s["weekday"] == "周六"
    assert s["period"] == "上午"
    assert s["title"] == "Keynote"
    assert s["time"] == "08:45-12:00"
    assert s["room"] == "聚英厅（友谊宫二层）"
    assert [c["name"] for c in s["chairs"]] == ["王健桥"]
    assert s["chairs"][0]["org"] == "清华大学"


def test_parse_talks_skips_interludes_and_strips_headers(catalog):
    talks = catalog["sessions"][0]["talks"]
    assert [t["id"] for t in talks] == ["sess01-t1", "sess01-t2"]
    assert [t["title"] for t in talks] == ["人工智能随想录", "Neuroscience Where AI = Science"]
    assert talks[0]["speaker"] == "孙茂松"
    assert talks[0]["org"] == "清华大学"
    assert talks[0]["affiliation"] == "清华大学 · 计算机科学与技术系"
    # The section's <h4> label is not part of the abstract / bio text.
    assert talks[0]["abstract"] == "本报告讨论生成式人工智能的基本问题。"
    assert "演讲摘要" not in talks[0]["abstract"]
    assert "嘉宾介绍" not in talks[0]["bio"]
    assert talks[0]["time"] == "09:10-10:00"


def test_parse_schedule_is_stable_on_reimport(catalog):
    again = scrape.parse_schedule(SESSION_HTML)
    assert again["sessions"] == catalog["sessions"]


def test_merge_sessions_keeps_paper_state(catalog):
    old = {"sessions": [{
        "id": "sess01", "talks": [
            {"id": "sess01-t1", "paper": {"found": True, "arxiv_id": "2601.00001"}},
        ],
    }]}
    merged = scrape.merge_sessions(old, catalog)
    talk = merged["sessions"][0]["talks"][0]
    assert talk["paper"]["arxiv_id"] == "2601.00001"
    # A talk that was not in the old catalog has no state.
    assert "paper" not in merged["sessions"][0]["talks"][1]


def test_talk_by_id(catalog):
    s, t = scrape.talk_by_id(catalog, "sess01-t2")
    assert s["id"] == "sess01" and t["speaker"] == "冯建峰"
    assert scrape.talk_by_id(catalog, "sess09-t9") == (None, None)


# ── paper matching score ─────────────────────────────────────────────────────

def test_keyword_coverage():
    q = "outlier-driven rescaling attention sinks residual"
    assert xagi.keyword_coverage(q, "A Unified View of Attention and Residual Sinks: "
                                    "Outlier-Driven Rescaling is Essential") == 1.0
    assert xagi.keyword_coverage(q, "Functional flood frequency analysis and outlier detection") < 0.4
    assert xagi.keyword_coverage("", "anything") == 0.0


def test_score_accepts_author_plus_keywords_with_different_title():
    talk = {"title": "大模型中离群值的功能性分析", "speaker": "邱子涵"}
    cand = {
        "title": "A Unified View of Attention and Residual Sinks: Outlier-Driven Rescaling",
        "authors": ["Zihan Qiu", "Zeyu Huang"],
        "abstract": "We study attention sinks and residual sinks in large language models.",
        "arxiv_id": "2601.22966",
    }
    score, sim, kw = xagi.score_candidate(
        talk, cand, alt_title="Functional Analysis of Outliers in Large Models",
        query="outlier-driven rescaling attention sinks residual sinks",
        hint_authors=["Zihan Qiu"])
    assert score >= xagi.MATCH_THRESHOLD
    assert kw > 0.6


def test_score_rejects_keyword_match_without_author():
    talk = {"title": "数学自然语言的形式化与结构化", "speaker": "罗涛"}
    cand = {
        "title": "Fyan: A Human-AI Harness for Mathematical Natural Language",
        "authors": ["Someone Else"],
        "abstract": "structured representation for formalization",
        "arxiv_id": None,
    }
    score, _sim, _kw = xagi.score_candidate(
        talk, cand, alt_title="Formalization and Structuring of Mathematical Natural Language",
        query="mathematical natural language formalization structured representation",
        hint_authors=["Tao Luo"])
    assert score < xagi.MATCH_THRESHOLD  # speaker is not an author → no keyword path


def test_score_title_match(catalog):
    talk = catalog["sessions"][0]["talks"][1]
    cand = {"title": "Neuroscience Where AI = Science", "authors": ["Jianfeng Feng"],
            "arxiv_id": "2602.00001"}
    score, sim, _kw = xagi.score_candidate(talk, cand, query="", hint_authors=["Jianfeng Feng"])
    assert sim == 1.0 and score >= xagi.MATCH_THRESHOLD


# ── queue ────────────────────────────────────────────────────────────────────

def _queue_text(done_cell: str = "", cell: str = "sess01-t1") -> str:
    check = "x (2026-10-17)" if done_cell else ""
    return (xagi.QUEUE_HEADER + "\n### Session 01 · Keynote\n"
            f"- [{check or ' '}] {done_cell or ''} `{cell}` 报告一 — 讲者（单位）\n"
            "- [ ] `sess01-t2` 报告二 — 讲者（单位）\n")


def test_pending_cells_and_mark_done(tmp_path):
    q = tmp_path / "q.md"
    q.write_text(_queue_text(done_cell="sess01-t1"), encoding="utf-8")
    pend = xagi.pending_cells(q)
    assert [c for _, c in pend] == ["sess01-t2"]

    line = "- [ ] `sess01-t2` 报告二 — 讲者（单位）"
    assert xagi.mark_done(line, date(2026, 10, 18)) == \
        "- [x] (2026-10-18) `sess01-t2` 报告二 — 讲者（单位）"


def test_render_queue_preserves_ticks(tmp_path, catalog):
    q = tmp_path / "q.md"
    q.write_text(_queue_text(done_cell="sess01-t1"), encoding="utf-8")
    body = xagi.render_queue(catalog, path=q)
    assert "- [x]" in body and "sess01-t1" in body
    assert "- [ ] `sess01-t2`" in body
    assert "### Session 01 · Keynote" in body


def test_backfill_ticks_next_cell(tmp_path, monkeypatch):
    q = tmp_path / "q.md"
    q.write_text(_queue_text(), encoding="utf-8")
    calls = []

    class _Proc:
        returncode = 0

    def _fake_run(argv, *a, **k):
        calls.append(argv)
        return _Proc()

    monkeypatch.setattr(xagi.subprocess, "run", _fake_run)
    monkeypatch.setattr(xagi, "render", lambda *a, **k: None)

    assert xagi.backfill(max_units=1, queue_path=q) == 1
    assert "sess01-t1" in calls[0]
    txt = q.read_text(encoding="utf-8")
    assert "- [x] (" in txt and "sess01-t1" in txt
    assert "- [ ] `sess01-t2`" in txt


def test_backfill_leaves_cell_unchecked_on_failure(tmp_path, monkeypatch):
    q = tmp_path / "q.md"
    q.write_text(_queue_text(), encoding="utf-8")

    class _Proc:
        returncode = 3

    monkeypatch.setattr(xagi.subprocess, "run", lambda *a, **k: _Proc())
    monkeypatch.setattr(xagi, "render", lambda *a, **k: None)

    assert xagi.backfill(max_units=1, queue_path=q) == 0
    assert q.read_text(encoding="utf-8") == _queue_text()


def test_backfill_dry_run_changes_nothing(tmp_path):
    q = tmp_path / "q.md"
    q.write_text(_queue_text(), encoding="utf-8")
    assert xagi.backfill(max_units=2, dry_run=True, queue_path=q) == 2
    assert q.read_text(encoding="utf-8") == _queue_text()
