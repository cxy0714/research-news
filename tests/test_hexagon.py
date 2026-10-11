"""Hexagon scraper: id/date mapping, provenance, window paging, Atom fallback."""
from datetime import date
from xml.etree import ElementTree as ET

import pytest

from research_news.scrapers import hexagon


@pytest.fixture(autouse=True)
def _no_page_sleep(monkeypatch):
    monkeypatch.setattr(hexagon, "_PAGE_SLEEP", 0)


# ── ids + dates ───────────────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected", [
    ("2610.00165", "2610.00165"),
    ("2610.00165v2", "2610.00165"),
    ("hexagon:2610.00165v1", "2610.00165"),
    ("https://hexagonmath.org/abs/2610.00165v1", "2610.00165"),
    ("https://hexagonmath.org/pdf/2610.00165", "2610.00165"),
    ("", ""),
    ("no id here", ""),
])
def test_normalize_hexagon_id(raw, expected):
    assert hexagon.normalize_hexagon_id(raw) == expected


def test_paper_id_is_namespaced_and_version_stripped():
    # Hexagon numbers works exactly like arXiv, so the namespace is what keeps a
    # Hexagon work from colliding with a real arXiv id in the id-keyed stores.
    assert hexagon._paper_id("2610.00165v1") == "hexagon:2610.00165"


def test_date_window_lookback():
    assert hexagon._date_window(date(2026, 10, 9), 3) == (
        date(2026, 10, 6), date(2026, 10, 9)
    )
    assert hexagon._date_window(date(2026, 10, 9), 0) == (
        date(2026, 10, 9), date(2026, 10, 9)
    )


@pytest.mark.parametrize("raw,expected", [
    ("2026-10-09T14:54:51.638Z", date(2026, 10, 9)),
    ("2026-10-08 21:37:01", date(2026, 10, 8)),        # naive createdAt → UTC
    ("2026-10-09T00:30:00+02:00", date(2026, 10, 8)),  # normalised to UTC
    ("", None),
    ("not a date", None),
])
def test_as_date(raw, expected):
    assert hexagon._as_date(raw) == expected


# ── subject scope ─────────────────────────────────────────────────────────────

def test_empty_subject_whitelist_means_everything():
    assert hexagon._subject_match("math.AG", ["math.NT"], set(), False)


def test_primary_subject_matches_whitelist():
    assert hexagon._subject_match("math.ST", [], {"math.ST"}, False)


def test_cross_list_needs_include_cross_listed():
    # Hexagon marks stat.ME / astro-ph.IM / … cross-list-only, so a whitelist
    # entry for those is inert unless cross-lists are included.
    assert not hexagon._subject_match("math.PR", ["stat.ME"], {"stat.ME"}, False)
    assert hexagon._subject_match("math.PR", ["stat.ME"], {"stat.ME"}, True)


# ── JSON list records ─────────────────────────────────────────────────────────

_WORK = {
    "identifier": "2610.00165",
    "title": "Multi-coverings by lattice translates of convex bodies",
    "abstract": "We show  that for every convex body $K$ ...",
    "subject": "math.MG",
    "crossListSubjects": ["math.CO", "math.NT"],
    "authorshipMode": "mixed",
    "humanUnderstanding": "all",
    "status": "published",
    "publishedAt": "2026-10-09T14:54:51.638Z",
    "createdAt": "2026-10-08 21:37:01",
    "arxivId": None,
    "doi": None,
    "tags": ["convex bodies"],
    "mscCodes": ["52C17"],
    "authors": [
        {"name": "Scott Kominers", "affiliation": "Harvard University and a16z crypto"},
        {"name": "A. B.", "affiliation": None},
    ],
    "tools": [
        {"provider": "OpenAI", "name": "GPT", "version": "6 Astra"},
        {"provider": "Lean", "name": "Lean", "version": "4.34.1"},
    ],
    "links": {
        "record": "https://hexagonmath.org/abs/2610.00165v1",
        "pdf": "https://hexagonmath.org/pdf/2610.00165v1",
    },
}


def test_work_to_paper_maps_everything_the_pipeline_needs():
    p = hexagon._work_to_paper(_WORK)
    assert (p.source, p.paper_id) == ("hexagon", "hexagon:2610.00165")
    assert p.title == "Multi-coverings by lattice translates of convex bodies"
    assert "".join(p.abstract.split()) == "Weshowthatforeveryconvexbody$K$..."
    assert p.url == "https://hexagonmath.org/abs/2610.00165v1"
    assert p.pdf_url == "https://hexagonmath.org/pdf/2610.00165v1"
    assert p.categories == ["math.MG", "math.CO", "math.NT"]
    assert p.published == "2026-10-09"
    assert p.authors == ["Scott Kominers", "A. B."]
    # Affiliations feed both the OpenAlex-free green-light match and the 机构 line.
    assert p.affiliations == ["Harvard University and a16z crypto"]
    assert p.institutions == ["Harvard University", "a16z crypto"]
    assert p.venue == "Hexagon · 人机混合 · 人类理解：全部 · 工具: GPT 6 Astra / Lean 4.34.1"
    assert p.arxiv_url is None


def test_work_to_paper_links_a_declared_arxiv_cross_post():
    w = dict(_WORK, arxivId="2610.03612")
    p = hexagon._work_to_paper(w)
    assert p.arxiv_url == "https://arxiv.org/abs/2610.03612"
    # The Hexagon deposit stays the primary link / PDF.
    assert p.url.endswith("/abs/2610.00165v1")
    assert p.pdf_url.endswith("/pdf/2610.00165v1")


def test_work_to_paper_without_identifier_is_skipped():
    assert hexagon._work_to_paper({"title": "x"}) is None


@pytest.mark.parametrize("raw,expected", [
    (["Yale University"], ["Yale University"]),
    (["Harvard University and a16z crypto"], ["Harvard University", "a16z crypto"]),
    (["University of California, Los Angeles"], ["University of California, Los Angeles"]),
    (["A; B & C"], ["A", "B", "C"]),
    (["", "  Yale University  ", "Yale University"], ["Yale University"]),
])
def test_split_affiliations(raw, expected):
    assert hexagon._split_affiliations(raw) == expected


# ── list paging ───────────────────────────────────────────────────────────────

def _page(works, *, has_more, cursor=None):
    return {"works": works, "page": {"has_more": has_more, "next_cursor": cursor}}


def test_fetch_list_walks_pages_until_window_start(monkeypatch):
    calls = []

    pages = [
        _page([_WORK], has_more=True, cursor="c1"),
        # Oldest work on page 2 already predates the window → stop after it.
        _page([dict(_WORK, identifier="2610.00001",
                    publishedAt="2026-09-01T00:00:00Z")], has_more=True, cursor="c2"),
    ]

    def fake(url, params=None):
        calls.append(params)
        return pages[len(calls) - 1]

    monkeypatch.setattr(hexagon, "_get_json", fake)
    papers, ok = hexagon._fetch_list(
        date(2026, 10, 6), date(2026, 10, 9), subjects=set(),
        include_cross_listed=True, max_works=300,
    )
    assert ok and [p.paper_id for p in papers] == ["hexagon:2610.00165"]
    assert len(calls) == 2              # page 2 fetched, page 3 never needed
    assert "cursor" not in calls[0] and calls[1]["cursor"] == "c1"


def test_fetch_list_filters_status_subject_and_window(monkeypatch):
    works = [
        _WORK,
        dict(_WORK, identifier="2610.00166", status="draft"),
        dict(_WORK, identifier="2610.00167", publishedAt="2026-09-20T00:00:00Z"),
        dict(_WORK, identifier="2610.00168", subject="math.AG",
             crossListSubjects=[]),
        dict(_WORK, identifier="2610.00169", subject="math.ST",
             crossListSubjects=[]),
    ]
    monkeypatch.setattr(hexagon, "_get_json",
                        lambda url, params=None: _page(works, has_more=False))
    papers, ok = hexagon._fetch_list(
        date(2026, 10, 6), date(2026, 10, 9), subjects={"math.ST"},
        include_cross_listed=False, max_works=300,
    )
    assert ok
    assert [p.paper_id for p in papers] == ["hexagon:2610.00169"]


def test_fetch_list_respects_max_works(monkeypatch):
    works = [dict(_WORK, identifier=f"2610.0016{i}") for i in range(5)]
    monkeypatch.setattr(hexagon, "_get_json",
                        lambda url, params=None: _page(works, has_more=False))
    papers, _ = hexagon._fetch_list(
        date(2026, 10, 6), date(2026, 10, 9), subjects=set(),
        include_cross_listed=True, max_works=2,
    )
    assert len(papers) == 2


def test_fetch_list_reports_failure_for_the_fallback(monkeypatch):
    def boom(url, params=None):
        raise RuntimeError("503")

    monkeypatch.setattr(hexagon, "_get_json", boom)
    papers, ok = hexagon._fetch_list(
        date(2026, 10, 6), date(2026, 10, 9), subjects=set(),
        include_cross_listed=True, max_works=300,
    )
    assert papers == [] and ok is False


# ── Atom fallback ─────────────────────────────────────────────────────────────

_ATOM = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom"
      xmlns:mathlake="https://mathlake.org/schemas/atom">
  <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">1</opensearch:totalResults>
  <entry>
    <title>Nearly Minimax Variance Estimation Under Rough Random Design</title>
    <id>https://hexagonmath.org/abs/2610.00162v1</id>
    <published>2026-10-08T17:16:30.000Z</published>
    <summary>We determine, up to a power of $\\log n$, the minimax risk ...</summary>
    <author><name>P. M. Aronow</name><arxiv:affiliation>Yale University</arxiv:affiliation></author>
    <author><name>Patrick Lopatto</name><arxiv:affiliation>University of North Carolina at Chapel Hill</arxiv:affiliation></author>
    <link href="https://hexagonmath.org/abs/2610.00162v1" rel="alternate" type="text/html" />
    <link href="https://hexagonmath.org/pdf/2610.00162v1" rel="related" type="application/pdf" title="pdf" />
    <arxiv:primary_category term="math.ST" />
    <category term="math.ST" scheme="http://arxiv.org/schemas/atom" />
    <category term="stat.TH" scheme="http://arxiv.org/schemas/atom" />
    <mathlake:identifier>hexagon:2610.00162v1</mathlake:identifier>
    <mathlake:authorshipMode>no-human-author-claimed</mathlake:authorshipMode>
    <mathlake:tool provider="Lean" name="Lean" version="4.34.1" />
  </entry>
</feed>"""


def test_atom_entry_maps_to_paper():
    entry = ET.fromstring(_ATOM).find(hexagon.ATOM + "entry")
    p = hexagon._atom_entry_to_paper(entry)
    assert (p.source, p.paper_id) == ("hexagon", "hexagon:2610.00162")
    assert p.categories == ["math.ST", "stat.TH"]
    assert p.published == "2026-10-08"
    assert p.authors == ["P. M. Aronow", "Patrick Lopatto"]
    assert p.institutions == ["Yale University", "University of North Carolina at Chapel Hill"]
    assert p.url == "https://hexagonmath.org/abs/2610.00162v1"
    assert p.pdf_url == "https://hexagonmath.org/pdf/2610.00162v1"
    # The Atom projection has no human-understanding flag; authorship + tools still ride along.
    assert p.venue == "Hexagon · 无人类作者署名 · 工具: Lean 4.34.1"


def test_fetch_all_falls_back_to_atom_when_the_list_is_down(monkeypatch):
    def boom(url, params=None):
        raise RuntimeError("503")

    monkeypatch.setattr(hexagon, "_get_json", boom)
    monkeypatch.setattr(hexagon, "_get_text", lambda url, params=None: _ATOM)
    papers = hexagon.fetch_all(
        {"subjects": [], "lookback_days": 1}, for_date=date(2026, 10, 8)
    )
    assert [p.paper_id for p in papers] == ["hexagon:2610.00162"]


def test_fetch_all_uses_the_list_when_it_works(monkeypatch):
    monkeypatch.setattr(hexagon, "_get_json",
                        lambda url, params=None: _page([_WORK], has_more=False))
    monkeypatch.setattr(hexagon, "_get_text",
                        lambda url, params=None: pytest.fail("Atom path not expected"))
    papers = hexagon.fetch_all({"lookback_days": 1}, for_date=date(2026, 10, 9))
    assert [p.paper_id for p in papers] == ["hexagon:2610.00165"]


# ── Hexagon ids must not be mistaken for arXiv ids ────────────────────────────

class _FakeClient:
    def chat(self, *args, **kwargs):
        return "deep-read notes"


def _deep_read(monkeypatch, paper):
    """Run deep_read_paper with the citation lookup recorded instead of fetched."""
    from research_news import deep_read

    looked_up = []
    monkeypatch.setattr(deep_read, "FETCH_REFS", True)
    monkeypatch.setattr(deep_read.refs, "fetch_references",
                        lambda aid, **kw: looked_up.append(aid) or [])
    deep_read.deep_read_paper(_FakeClient(), paper, "interests")
    return looked_up


def test_deep_read_does_not_resolve_hexagon_ids_on_arxiv(monkeypatch):
    paper = hexagon._work_to_paper(_WORK)
    # "2610.00165" has a valid arXiv-id shape, but this work is not that paper —
    # resolving it would attach an unrelated paper's citations to this read.
    assert _deep_read(monkeypatch, paper) == []


def test_deep_read_still_resolves_arxiv_papers(monkeypatch):
    from research_news.models import Paper

    paper = Paper(source="arxiv", paper_id="2610.00165", title="T", authors=[],
                  abstract="A", url="https://arxiv.org/abs/2610.00165")
    assert _deep_read(monkeypatch, paper) == ["2610.00165"]
