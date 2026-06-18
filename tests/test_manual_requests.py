"""Offline tests for the manual deep-read queue (no network / LLM).

Covers: arXiv id normalization + id_list fetch (parsing a canned Atom feed),
reading the gist queue, and the idempotent injection of the '✍️ 手动录入' section
into a day's report.
"""
from __future__ import annotations

from research_news import manual_requests as mr
from research_news.models import Paper
from research_news.render.markdown import MANUAL_SECTION_HEADING, render_manual_section
from research_news.scrapers import arxiv as arxiv_scraper


# ── arXiv id normalization ────────────────────────────────────────────────────

def test_normalize_arxiv_id():
    n = arxiv_scraper.normalize_arxiv_id
    assert n("https://arxiv.org/pdf/2405.08525") == "2405.08525"
    assert n("https://arxiv.org/abs/2405.08525v2") == "2405.08525"
    assert n("2405.08525") == "2405.08525"
    assert n("arXiv:1912.12345") == "1912.12345"
    assert n("math.ST/0123456") == "math.ST/0123456"
    assert n("nothing here") == ""
    assert n("") == ""


_ATOM_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2405.08525v1</id>
    <title>A Manually Requested Paper</title>
    <summary>The abstract of the requested paper.</summary>
    <published>2024-05-14T00:00:00Z</published>
    <author><name>Jane Doe</name></author>
    <author><name>John Roe</name></author>
    <arxiv:primary_category term="math.ST"/>
  </entry>
</feed>
"""


def test_fetch_by_ids_parses_and_dedupes(monkeypatch):
    calls = {"n": 0}

    def fake_fetch_api(params):
        calls["n"] += 1
        return _ATOM_FEED

    monkeypatch.setattr(arxiv_scraper, "_fetch_api", fake_fetch_api)
    monkeypatch.setattr(arxiv_scraper.time, "sleep", lambda *a, **k: None)

    # URL + a versioned dup of the same id collapse to one request, one paper.
    papers = arxiv_scraper.fetch_by_ids(
        ["https://arxiv.org/pdf/2405.08525", "2405.08525v2"]
    )
    assert calls["n"] == 1
    assert len(papers) == 1
    p = papers[0]
    assert p.paper_id == "2405.08525"
    assert p.source == "arxiv"
    assert p.url == "https://arxiv.org/abs/2405.08525"
    assert p.title == "A Manually Requested Paper"
    assert p.authors == ["Jane Doe", "John Roe"]


def test_fetch_by_ids_skips_unparseable(monkeypatch):
    def boom(params):  # must never be called: no valid id to query
        raise AssertionError("arXiv API hit for an input with no valid id")

    monkeypatch.setattr(arxiv_scraper, "_fetch_api", boom)
    assert arxiv_scraper.fetch_by_ids(["not-an-id", ""]) == []


# ── reading the gist queue ────────────────────────────────────────────────────

def test_queued_ids_normalizes_orders_dedupes():
    state = {
        "queue": {
            "2405.08525": {"paper_id": "2405.08525",
                           "url": "https://arxiv.org/abs/2405.08525"},
            "k2": {"url": "https://arxiv.org/pdf/2401.00001v2"},
            "dup": {"paper_id": "2405.08525"},      # same id → dropped
            "bad": {"paper_id": "", "url": "no id"},  # unparseable → dropped
        }
    }
    assert mr.queued_ids(state) == ["2405.08525", "2401.00001"]


def test_queued_ids_empty():
    assert mr.queued_ids({}) == []
    assert mr.queued_ids({"queue": {}}) == []


# ── section rendering + injection ─────────────────────────────────────────────

def _paper(pid="2405.08525", topic="causal_inference", score=7.0):
    return Paper(
        source="arxiv", paper_id=pid, title="A Requested Paper",
        authors=["Jane Doe"], abstract="", url=f"https://arxiv.org/abs/{pid}",
        topic=topic, score=score, summary_zh="中文摘要。",
    )


def test_render_manual_section():
    assert render_manual_section([]) == []
    lines = render_manual_section([_paper()])
    text = "\n".join(lines)
    assert MANUAL_SECTION_HEADING in text
    assert "2405.08525" in text
    assert "中文摘要" in text


_DAILY = """# 2026-06-18 每日 arXiv 资讯

- 高相关论文 1 篇 · 中相关 0 篇 · 会议/Seminar 事件 0 条

## ⭐ 高相关论文（按主题分组）

### 因果推断  *(causal_inference, 1 篇)*

#### 1. [2606.00001](https://arxiv.org/abs/2606.00001) — Existing Paper
- **作者**: Someone

---

Maintained by 陈星宇
"""


def test_inject_section_places_above_digest_and_is_idempotent():
    section = render_manual_section([_paper()])
    once = mr.inject_section(_DAILY, section)

    # Section sits below the count line but above the ⭐ digest.
    assert once.count(MANUAL_SECTION_HEADING) == 1
    assert once.index(MANUAL_SECTION_HEADING) < once.index("## ⭐ 高相关论文")
    assert once.index("高相关论文 1 篇") < once.index(MANUAL_SECTION_HEADING)
    # Original content is preserved.
    assert "2606.00001" in once and "Maintained by" in once

    # Re-injecting replaces (not appends) → still exactly one section, stable.
    twice = mr.inject_section(once, section)
    assert twice.count(MANUAL_SECTION_HEADING) == 1
    assert twice == once


def test_strip_section_removes_it():
    section = render_manual_section([_paper()])
    injected = mr.inject_section(_DAILY, section)
    stripped = mr._strip_existing_section(injected)
    assert MANUAL_SECTION_HEADING not in stripped
    assert "2606.00001" in stripped  # untouched


# ── update_daily_page (file IO via tmp dir) ───────────────────────────────────

def test_update_daily_page_injects_and_is_idempotent(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "manual_papers_for_date", lambda d: [_paper()])
    page = tmp_path / "2026-06-18.md"
    page.write_text(_DAILY, encoding="utf-8")

    assert mr.update_daily_page("2026-06-18", daily_dir=tmp_path) is True
    body = page.read_text(encoding="utf-8")
    assert MANUAL_SECTION_HEADING in body
    # Second run is a no-op (already up to date).
    assert mr.update_daily_page("2026-06-18", daily_dir=tmp_path) is False


def test_update_daily_page_creates_page_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "manual_papers_for_date", lambda d: [_paper()])
    assert mr.update_daily_page("2026-06-18", daily_dir=tmp_path) is True
    page = tmp_path / "2026-06-18.md"
    assert page.exists()
    body = page.read_text(encoding="utf-8")
    assert MANUAL_SECTION_HEADING in body
    assert "每日 arXiv 资讯" in body
    assert "Maintained by" in body


def test_update_daily_page_no_papers_no_page(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "manual_papers_for_date", lambda d: [])
    assert mr.update_daily_page("2026-06-18", daily_dir=tmp_path) is False
    assert not (tmp_path / "2026-06-18.md").exists()


def test_update_daily_page_no_papers_leaves_clean_page_untouched(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "manual_papers_for_date", lambda d: [])
    page = tmp_path / "2026-06-18.md"
    page.write_text(_DAILY, encoding="utf-8")
    assert mr.update_daily_page("2026-06-18", daily_dir=tmp_path) is False
    assert page.read_text(encoding="utf-8") == _DAILY  # byte-for-byte untouched


def test_update_daily_page_removes_stale_section_when_queue_cleared(tmp_path, monkeypatch):
    # Page has a manual section, but there are no manual papers anymore.
    monkeypatch.setattr(mr, "manual_papers_for_date", lambda d: [_paper()])
    page = tmp_path / "2026-06-18.md"
    page.write_text(_DAILY, encoding="utf-8")
    mr.update_daily_page("2026-06-18", daily_dir=tmp_path)
    assert MANUAL_SECTION_HEADING in page.read_text(encoding="utf-8")

    monkeypatch.setattr(mr, "manual_papers_for_date", lambda d: [])
    assert mr.update_daily_page("2026-06-18", daily_dir=tmp_path) is True
    body = page.read_text(encoding="utf-8")
    assert MANUAL_SECTION_HEADING not in body
    assert "2606.00001" in body and "Maintained by" in body
