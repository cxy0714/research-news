"""Tests for the issue completeness checker. Offline only — no network, no LLM."""
from __future__ import annotations

from pathlib import Path

from research_news import completeness as cmp
from research_news.completeness import TocEntry
from research_news.scrapers import euclid


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
