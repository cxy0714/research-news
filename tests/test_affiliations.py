"""Offline tests for institution green-light matching (no network)."""
from __future__ import annotations

from research_news.scrapers import affiliations as affil
from research_news.models import Paper


def test_normalize_dashes_and_punct():
    assert affil._normalize("University of Wisconsin–Madison") == "university of wisconsin madison"
    assert affil._normalize("Dept. of Statistics, Stanford University, CA") == \
        "dept of statistics stanford university ca"


def test_match_full_official_name():
    assert affil.match_affiliation(
        ["Department of Statistics, Stanford University, Stanford, CA"]
    ) == "Stanford University"
    assert affil.match_affiliation(
        ["University of California, Berkeley"]
    ) == "University of California, Berkeley"


def test_match_alias_token_boundary():
    # "MIT" alias matches as a whole token (returns the alias label), not inside
    # a longer word like "Schummit".
    assert affil.match_affiliation(["MIT, Cambridge"]) == "MIT"
    assert affil.match_affiliation(["Schummit Institute"]) is None
    # The full official name still resolves to the canonical form.
    assert affil.match_affiliation(["Massachusetts Institute of Technology"]) == \
        "Massachusetts Institute of Technology"


def test_no_cross_match_between_similar_names():
    # Washington University in St. Louis must NOT match "University of Washington".
    got = affil.match_affiliation(["Washington University in St. Louis"])
    assert got == "Washington University in St. Louis"
    # A non-whitelisted school stays None.
    assert affil.match_affiliation(["Some Local College"]) is None


def test_green_light_uses_existing_affiliations_without_network(monkeypatch):
    # Force no backfill so the test never touches the network.
    p = Paper(source="arxiv", paper_id="2401.00001", title="t", authors=["A"],
              abstract="", url="", affiliations=["Princeton University"])
    assert affil.green_light(p, backfill=False) == "Princeton University"

    p2 = Paper(source="arxiv", paper_id="2401.00002", title="t", authors=["A"],
               abstract="", url="", affiliations=["Nowhere State"])
    assert affil.green_light(p2, backfill=False) is None


def test_doi_for_arxiv_and_journal():
    p = Paper(source="arxiv", paper_id="2401.01234v2", title="t", authors=[], abstract="", url="")
    assert affil._doi_for(p) == "10.48550/arXiv.2401.01234"
    j = Paper(source="crossref", paper_id="10.1214/23-AOS2345", title="t", authors=[],
              abstract="", url="https://doi.org/10.1214/23-AOS2345")
    assert affil._doi_for(j) == "10.1214/23-AOS2345"
