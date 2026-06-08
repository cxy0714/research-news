"""Tests for the issue completeness checker. Offline only — no network, no LLM."""
from __future__ import annotations

from pathlib import Path

from research_news import completeness as cmp
from research_news.completeness import TocEntry
from research_news.scrapers import euclid, openalex


# ── content-PDF TOC text parsing ───────────────────────────────────────────────

def test_parse_toc_text_with_dois_strips_page_numbers():
    toc = (
        "TABLE OF CONTENTS\n"
        "Berry-Esseen bounds for design-based causal inference  10.1214/25-aos2569  1\n"
        "Confounder selection via iterative graph expansion  10.1214/25-aos2577  20\n"
        "A brand new paper on minimax rates  10.1214/25-aos2599  45\n"
    )
    entries = cmp.parse_toc_text(toc)
    assert [e.doi for e in entries] == [
        "10.1214/25-aos2569", "10.1214/25-aos2577", "10.1214/25-aos2599"
    ]
    # Page numbers and the header line are gone.
    assert entries[2].title == "A brand new paper on minimax rates"
    assert all(not t.title.lower().startswith("table of contents") for t in entries)


def test_parse_toc_text_doi_on_its_own_line_looks_back_for_title():
    toc = (
        "Optimality of approximate message passing for spiked matrix models\n"
        "    10.1214/25-aos2575\n"
    )
    entries = cmp.parse_toc_text(toc)
    assert len(entries) == 1
    assert entries[0].doi == "10.1214/25-aos2575"
    assert "approximate message passing" in entries[0].title


def test_parse_toc_text_title_only_when_no_dois():
    toc = (
        "CONTENTS\n"
        "Volume 54, Number 1\n"
        "Semiparametric Bernstein-von Mises in Wicksell's problem . . . 71\n"
        "On the structural dimension of sliced inverse regression . . . 95\n"
        "12\n"   # pure page-number row — not a title
    )
    entries = cmp.parse_toc_text(toc)
    titles = [e.title for e in entries]
    assert "Semiparametric Bernstein-von Mises in Wicksell's problem" in titles
    assert "On the structural dimension of sliced inverse regression" in titles
    assert all(e.doi is None for e in entries)
    # Headers / page-number rows excluded.
    assert not any(t.lower().startswith(("contents", "volume")) for t in titles)
    assert "12" not in titles


# ── diff ────────────────────────────────────────────────────────────────────────

def _scraped(*pairs):
    return [TocEntry(t, d, "u") for t, d in pairs]


def test_diff_by_doi_finds_the_one_we_missed():
    auth = cmp.parse_toc_text(
        "A  10.1214/25-aos1  1\nB  10.1214/25-aos2  2\nC  10.1214/25-aos3  3\n"
    )
    scraped = _scraped(("A", "10.1214/25-aos1"), ("B", "10.1214/25-aos2"))
    missing = cmp.diff(auth, scraped)
    assert [m.doi for m in missing] == ["10.1214/25-aos3"]


def test_diff_doi_match_is_case_insensitive():
    auth = [TocEntry("Some paper", "10.1214/25-AOS2569", "u")]
    scraped = _scraped(("Some paper", "10.1214/25-aos2569"))
    assert cmp.diff(auth, scraped) == []


def test_diff_title_fallback_when_no_doi():
    # Authoritative entry has no DOI; matches a scraped title → not missing.
    auth = [TocEntry("Confounder selection via iterative graph expansion")]
    scraped = _scraped(
        ("Confounder selection via iterative graph expansion", "10.1214/25-aos2577")
    )
    assert cmp.diff(auth, scraped) == []
    # A genuinely different title → missing.
    auth2 = [TocEntry("An entirely unrelated title about random matrices")]
    assert len(cmp.diff(auth2, scraped)) == 1


def test_diff_excludes_discussion_items():
    # Comments / rejoinders are intentionally not scraped — never report them.
    auth = [
        TocEntry("Comments on: A new approach to inference", "10.1214/25-aos9001"),
        TocEntry("Rejoinder", "10.1214/25-aos9002"),
        TocEntry("A real research article", "10.1214/25-aos9003"),
    ]
    missing = cmp.diff(auth, scraped=[])
    assert [m.doi for m in missing] == ["10.1214/25-aos9003"]


# ── scraped side: rendered page ─────────────────────────────────────────────────

def test_page_entries_handles_arxiv_link_headings(tmp_path: Path):
    md = (
        "# AoS — Vol 54 Issue 1\n\n"
        "## 因果推断  *(causal_inference, 2 篇)*\n\n"
        "### 1. [10.1214/25-aos2569](https://doi.org/10.1214/25-aos2569) — Berry-Esseen bounds\n"
        "- **作者**: X\n"
        "### 2. [10.1214/25-aos2577](https://doi.org/10.1214/25-aos2577) · "
        "[arXiv](https://arxiv.org/abs/2501.1) — Confounder selection\n"
        "- **作者**: Y\n"
    )
    p = tmp_path / "2026-05-26-aos-v54-i1.md"
    p.write_text(md, encoding="utf-8")
    entries = cmp.page_entries(p)
    assert [e.doi for e in entries] == ["10.1214/25-aos2569", "10.1214/25-aos2577"]
    assert entries[1].title == "Confounder selection"


def test_norm_doi():
    assert cmp._norm_doi("https://doi.org/10.1214/25-AOS2569") == "10.1214/25-aos2569"
    assert cmp._norm_doi("10.1214/25-aos2569.") == "10.1214/25-aos2569"


# ── Project Euclid HTML parsing ────────────────────────────────────────────────

def test_euclid_parse_issue_html_extracts_doi_from_href():
    html = """
    <html><body>
      <div class="issue">
        <a href="/journals/annals-of-statistics/volume-54/issue-1/Berry-Esseen-bounds/10.1214/25-AOS2569/full">
          Berry-Esseen bounds for design-based causal inference</a>
        <a href="/journals/annals-of-statistics/volume-54/issue-1/Confounder/10.1214/25-AOS2577/full">
          Confounder selection via iterative graph expansion</a>
        <a href="/journals/annals-of-statistics/volume-54/issue-1/x/10.1214/25-AOS2577/full">PDF</a>
      </div>
    </body></html>
    """
    pairs = euclid.parse_issue_html(html)
    dois = {d for _, d in pairs}
    assert dois == {"10.1214/25-aos2569", "10.1214/25-aos2577"}
    # The "PDF" anchor (duplicate DOI, short text) is not double-counted.
    assert len(pairs) == 2
    titles = {t for t, _ in pairs}
    assert "Berry-Esseen bounds for design-based causal inference" in titles


# ── OpenAlex issue listing parsing ─────────────────────────────────────────────

def test_openalex_parse_works_json():
    data = {
        "meta": {"next_cursor": None},
        "results": [
            {"title": "Berry-Esseen bounds",
             "doi": "https://doi.org/10.1214/25-AOS2569",
             "biblio": {"volume": "54", "issue": "1"}},
            {"display_name": "Confounder selection", "doi": None,
             "biblio": {"volume": "54", "issue": "1"}},
            {"title": "", "doi": "https://doi.org/10.1214/25-aos9999"},  # no title → dropped
        ],
    }
    pairs = openalex.parse_works_json(data)
    assert pairs == [
        ("Berry-Esseen bounds", "10.1214/25-aos2569"),
        ("Confounder selection", None),
    ]


# ── automatic authoritative-source resolution ──────────────────────────────────

def test_resolve_authoritative_auto_prefers_euclid(monkeypatch):
    monkeypatch.setattr(euclid, "fetch_issue_toc",
                        lambda *a, **k: [TocEntry("From Euclid", "10.1/e")])
    called = {"openalex": False}
    def _oa(*a, **k):
        called["openalex"] = True
        return [TocEntry("From OpenAlex", "10.1/o")]
    monkeypatch.setattr(openalex, "fetch_issue_toc", _oa)

    entries, used = cmp.resolve_authoritative("0090-5364", "AoS", 54, 1)
    assert used == "euclid" and entries[0].doi == "10.1/e"
    assert called["openalex"] is False  # not consulted when Euclid has data


def test_resolve_authoritative_auto_falls_back_to_openalex(monkeypatch):
    monkeypatch.setattr(euclid, "fetch_issue_toc", lambda *a, **k: [])  # Euclid empty
    monkeypatch.setattr(openalex, "fetch_issue_toc",
                        lambda *a, **k: [TocEntry("From OpenAlex", "10.1/o")])
    entries, used = cmp.resolve_authoritative("1234-5678", "JASA", 121, 1)
    assert used == "openalex" and entries[0].doi == "10.1/o"


def test_resolve_authoritative_pdf_override(monkeypatch, tmp_path):
    monkeypatch.setattr(cmp, "extract_toc_from_pdf",
                        lambda p, **k: [TocEntry("From PDF", "10.1/p")])
    entries, used = cmp.resolve_authoritative(
        "0090-5364", "AoS", 54, 1, toc_pdf=tmp_path / "c.pdf")
    assert used == "pdf" and entries[0].doi == "10.1/p"


# ── inline completeness badge ──────────────────────────────────────────────────

def test_diff_excludes_paratext():
    auth = [
        TocEntry("Front Matter", "10.1214/25-aos0001"),
        TocEntry("Editorial Board", None),
        TocEntry("A real research article", "10.1214/25-aos0003"),
    ]
    missing = cmp.diff(auth, scraped=[])
    assert [m.doi for m in missing] == ["10.1214/25-aos0003"]


def test_paper_doi_and_entries():
    from research_news.models import Paper
    crossref = Paper(source="crossref", paper_id="10.1214/25-AOS2601", title="T1",
                     authors=[], abstract="a", url="u")
    jmlr = Paper(source="jmlr", paper_id="jmlr:v27/foo", title="T2",
                 authors=[], abstract="a", url="u")
    assert cmp._paper_doi(crossref) == "10.1214/25-aos2601"
    assert cmp._paper_doi(jmlr) is None
    entries = cmp.papers_to_entries([crossref, jmlr])
    assert [e.doi for e in entries] == ["10.1214/25-aos2601", None]


def test_check_issue_and_status_line(monkeypatch):
    from research_news.models import Paper
    papers = [
        Paper(source="crossref", paper_id="10.1214/a", title="Alpha", authors=[],
              abstract="x", url="u"),
        Paper(source="crossref", paper_id="10.1214/b", title="Beta", authors=[],
              abstract="x", url="u"),
    ]
    # Authoritative has a third article we didn't scrape.
    monkeypatch.setattr(cmp, "resolve_authoritative", lambda *a, **k: (
        [TocEntry("Alpha", "10.1214/a"), TocEntry("Beta", "10.1214/b"),
         TocEntry("Gamma", "10.1214/c")], "openalex"))
    res = cmp.check_issue("0090-5364", "AoS", 54, 2, cmp.papers_to_entries(papers))
    assert res.n_authoritative == 3 and res.n_scraped == 2
    assert [m.doi for m in res.missing] == ["10.1214/c"]
    line = cmp.format_status_line(res)
    assert "疑似漏 1 篇" in line and "10.1214/c" in line


def test_status_line_all_present_and_unavailable():
    ok = cmp.CompletenessResult(22, 22, [], "openalex")
    assert "✅" in cmp.format_status_line(ok) and "22 篇全部抓到" in cmp.format_status_line(ok)
    none = cmp.CompletenessResult(0, 22, [], "none")
    assert "未核对" in cmp.format_status_line(none)
    # OpenAlex lagging (fewer than scraped) but nothing missing → no false alarm.
    lag = cmp.CompletenessResult(3, 22, [], "openalex")
    assert "未见遗漏" in cmp.format_status_line(lag)
