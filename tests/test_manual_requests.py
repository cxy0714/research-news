"""Offline tests for the manual deep-read queue (no network / LLM).

Covers: arXiv id normalization + id_list fetch (parsing a canned Atom feed),
reading the gist queue (arXiv + non-arXiv lookups), resolving a lookup to an
open-access publisher PDF or to a preprint by title, and the idempotent injection
of the '✍️ 手动录入' section.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from research_news import manual_requests as mr
from research_news.models import Paper
from research_news.render.markdown import MANUAL_SECTION_HEADING, render_manual_section
from research_news.scrapers import arxiv as arxiv_scraper
from research_news.scrapers import crossref


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


def test_queue_entries_classifies_arxiv_and_lookup():
    state = {"queue": {
        "2405.08525": {"paper_id": "2405.08525", "url": "https://arxiv.org/abs/2405.08525"},
        "q:foo": {"kind": "lookup", "query": "Some non arxiv paper title here",
                  "doi": "10.1/x", "url": "https://doi.org/10.1/x"},
        "bad": {},   # no id, no query → dropped
    }}
    es = mr.queue_entries(state)
    assert len(es) == 2
    arxiv = [e for e in es if e["kind"] == "arxiv"]
    lookup = [e for e in es if e["kind"] == "lookup"]
    assert arxiv[0]["arxiv_id"] == "2405.08525"
    assert lookup[0]["query"] == "Some non arxiv paper title here"
    assert lookup[0]["doi"] == "10.1/x"


# ── lookup resolution (non-arXiv → preprint by title) ─────────────────────────

class _EchoClient:
    """Stand-in SJTU client: echoes the citation back as the parsed title."""
    def chat(self, messages, **kw):
        import json as _j
        return _j.dumps({"title": messages[-1]["content"], "doi": ""})


def test_resolve_lookups_finds_preprint_or_bookmarks(monkeypatch):
    monkeypatch.setattr(mr.time, "sleep", lambda *a, **k: None)

    def fake_match(title):
        if "polynomial chaos" in title.lower():
            return ("https://arxiv.org/abs/1506.00343", "abstract")
        return None
    monkeypatch.setattr(crossref, "_arxiv_search_match", fake_match)

    lookups = [
        {"key": "q:a", "kind": "lookup", "doi": "", "url": "",
         "query": "Peng Hampton Doostan. On polynomial chaos expansion via gradient l1"},
        {"key": "q:b", "kind": "lookup", "doi": "", "url": "",
         "query": "Roderick Anitescu Fischer. Polynomial regression derivative info"},
    ]
    resolved = {}
    to_read = mr._resolve_lookups(lookups, resolved, client=_EchoClient(),
                                  run_date="2026-06-19", model="m")
    assert to_read == {"1506.00343"}
    assert resolved["q:a"]["status"] == "resolved"
    assert resolved["q:a"]["arxiv_id"] == "1506.00343"
    assert resolved["q:b"]["status"] == "no_preprint"

    # Re-run: 'resolved' is re-confirmed, recent 'no_preprint' is NOT re-searched.
    def boom(title):
        raise AssertionError("re-searched a recently-checked lookup")
    monkeypatch.setattr(crossref, "_arxiv_search_match", boom)
    to_read2 = mr._resolve_lookups(lookups, resolved, client=_EchoClient(),
                                   run_date="2026-06-19", model="m")
    assert to_read2 == {"1506.00343"}   # q:a re-added from cache; q:b skipped


# ── open-access resolution (journal link / DOI → publisher PDF) ───────────────

def test_queue_entries_recovers_url_and_doi_from_query():
    # An older entry that stored the pasted link only as query text still becomes
    # an open-access candidate.
    state = {"queue": {"q:muse": {
        "kind": "lookup",
        "query": "https://muse.jhu.edu/pub/56/article/999750/pdf",
    }}}
    e = mr.queue_entries(state)[0]
    assert e["url"] == "https://muse.jhu.edu/pub/56/article/999750/pdf"
    assert e["doi"] == ""

    state2 = {"queue": {"q:doi": {"kind": "lookup",
                                  "query": "see doi:10.1214/25-AOS2537 for details"}}}
    assert mr.queue_entries(state2)[0]["doi"] == "10.1214/25-AOS2537"


def _fake_src(**kw):
    from research_news.oa_pdf import PdfSource
    base = dict(landing_url="https://muse.jhu.edu/article/999750",
                pdf_candidates=["https://muse.jhu.edu/article/999750/pdf"],
                doi="", title="Beyond No Unmeasured Confounding",
                authors=["Gary C. N. Hettinger"], venue="Observational Studies",
                published="2026-08-27", volume="12", issue="2",
                abstract="An abstract long enough to be useful for scoring.")
    base.update(kw)
    return PdfSource(**base)


def test_resolve_oa_builds_paper_and_records_status(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "OA_CACHE_DIR", tmp_path)
    monkeypatch.setattr(mr.oa_pdf, "resolve", lambda t, doi="": _fake_src())

    def fake_download(src, dest):
        dest.write_bytes(b"%PDF-1.7\n" + b"x" * 4000)
        return dest
    monkeypatch.setattr(mr.oa_pdf, "download", fake_download)

    lookups = [{"key": "q:muse", "kind": "lookup", "query": "https://muse.jhu.edu/article/999750",
                "url": "https://muse.jhu.edu/article/999750", "doi": ""}]
    resolved = {}
    papers = mr._resolve_oa(lookups, resolved, run_date="2026-09-01")

    assert len(papers) == 1
    p = papers[0]
    assert p.source == "oa"
    assert p.paper_id == "oa:muse.jhu.edu-article-999750"
    assert p.title == "Beyond No Unmeasured Confounding"
    assert p.venue == "Observational Studies"
    assert (p.volume, p.issue) == ("12", "2")
    assert p.pdf_url == "https://muse.jhu.edu/article/999750/pdf"
    assert p.pdf_path and Path(p.pdf_path).exists()
    assert resolved["q:muse"]["status"] == "oa_pdf"
    assert resolved["q:muse"]["paper_id"] == p.paper_id


def test_resolve_oa_uses_doi_as_paper_id(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "OA_CACHE_DIR", tmp_path)
    monkeypatch.setattr(mr.oa_pdf, "resolve",
                        lambda t, doi="": _fake_src(doi="10.1353/OBS.2026.A999750"))
    monkeypatch.setattr(mr.oa_pdf, "download",
                        lambda src, dest: (dest.write_bytes(b"%PDF-1.7" + b"x" * 4000), dest)[1])
    resolved = {}
    papers = mr._resolve_oa(
        [{"key": "q:a", "kind": "lookup", "query": "x", "url": "https://x/a", "doi": ""}],
        resolved, run_date="2026-09-01")
    assert papers[0].paper_id == "10.1353/obs.2026.a999750"


def test_resolve_oa_marks_no_pdf_and_respects_retry_window(tmp_path, monkeypatch):
    monkeypatch.setattr(mr, "OA_CACHE_DIR", tmp_path)
    monkeypatch.setattr(mr.oa_pdf, "resolve", lambda t, doi="": _fake_src())
    monkeypatch.setattr(mr.oa_pdf, "download", lambda src, dest: None)  # paywalled

    lookups = [{"key": "q:a", "kind": "lookup", "query": "x",
                "url": "https://paywalled.example/a", "doi": ""}]
    resolved = {}
    assert mr._resolve_oa(lookups, resolved, run_date=date.today().isoformat()) == []
    assert resolved["q:a"]["status"] == "no_pdf"

    # Re-run the same day: not re-fetched (the retry window hasn't elapsed).
    def boom(*a, **k):
        raise AssertionError("re-resolved a recently-checked lookup")
    monkeypatch.setattr(mr.oa_pdf, "resolve", boom)
    assert mr._resolve_oa(lookups, resolved, run_date=date.today().isoformat()) == []


def test_resolve_oa_skips_entries_without_link():
    def boom(*a, **k):
        raise AssertionError("tried to resolve a bare title")
    resolved = {}
    # No url / doi → the arXiv title search owns this one.
    assert mr._resolve_oa(
        [{"key": "q:t", "kind": "lookup", "query": "A bare paper title", "url": "", "doi": ""}],
        resolved, run_date="2026-09-01") == []
    assert resolved == {}


def test_finalize_resolved_links_oa_paper_by_paper_id(monkeypatch):
    monkeypatch.setattr(mr, "load_index", lambda: [
        {"paper_id": "oa:muse.jhu.edu-article-999750", "date": "2026-09-01",
         "doc_path": "deep_reads/2026-09-01-oa_muse.jhu.edu-article-999750.md",
         "title": "Beyond No Unmeasured Confounding"},
    ])
    resolved = {"q:muse": {"status": "oa_pdf",
                           "paper_id": "oa:muse.jhu.edu-article-999750",
                           "title": "raw pasted text"},
                "q:none": {"status": "no_pdf", "title": "nothing found"}}
    mr._finalize_resolved(resolved)
    assert resolved["q:muse"]["status"] == "deep_read"
    assert resolved["q:muse"]["deep_read"].startswith("deep_reads/2026-09-01-oa_")
    assert resolved["q:muse"]["title"] == "Beyond No Unmeasured Confounding"
    assert resolved["q:none"]["status"] == "no_pdf"    # untouched


def test_finalize_resolved_marks_deep_read(monkeypatch):
    monkeypatch.setattr(mr, "load_index", lambda: [
        {"paper_id": "1506.00343", "date": "2026-06-19",
         "doc_path": "deep_reads/2026-06-19-1506.00343.md", "title": "Real Title"},
    ])
    resolved = {
        "q:a": {"status": "resolved", "arxiv_id": "1506.00343", "title": "echoed"},
        "q:b": {"status": "no_preprint", "title": "no preprint paper"},
    }
    mr._finalize_resolved(resolved)
    assert resolved["q:a"]["status"] == "deep_read"
    assert resolved["q:a"]["deep_read"] == "deep_reads/2026-06-19-1506.00343.md"
    assert resolved["q:a"]["title"] == "Real Title"
    assert resolved["q:b"]["status"] == "no_preprint"   # untouched


def test_stale():
    assert mr._stale(None) is True
    assert mr._stale("2000-01-01") is True
    assert mr._stale(date.today().isoformat()) is False


def test_favorite_deepread_ids_selects_un_deep_read_arxiv_newest_first():
    state = {"favorites": {
        "2405.08525": {"paper_id": "2405.08525",
                       "url": "https://arxiv.org/abs/2405.08525",
                       "added": "2026-06-18T00:00:00Z"},
        "2401.00001": {"paper_id": "2401.00001",
                       "url": "https://arxiv.org/abs/2401.00001",
                       "added": "2026-06-19T00:00:00Z"},
        "2399.55555": {"paper_id": "2399.55555", "added": "2026-06-17",
                       "deep_read_url": "/deep_reads/x/"},        # already read → skip
        "q:foo": {"paper_id": "q:foo", "manual_lookup": True,
                  "added": "2026-06-19"},                          # bookmark → skip
        "doi-x": {"paper_id": "10.1/x", "url": "https://doi.org/10.1/x",
                  "added": "2026-06-19"},                          # no arXiv id → skip
        "2300.00002": {"paper_id": "2300.00002", "added": "2026-06-10"},  # excluded
    }}
    ids = mr.favorite_deepread_ids(state, exclude={"2300.00002"})
    assert ids == ["2401.00001", "2405.08525"]   # newest favorited first


def test_favorite_deepread_ids_empty():
    assert mr.favorite_deepread_ids({}, exclude=set()) == []
    assert mr.favorite_deepread_ids({"favorites": {}}, exclude=set()) == []


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
