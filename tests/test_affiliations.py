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


def test_parse_authorships_dedupes_institutions():
    work = {
        "authorships": [
            {
                "institutions": [{"display_name": "Stanford University"}],
                "raw_affiliation_strings": ["Dept. of Statistics, Stanford University, CA"],
            },
            {
                "institutions": [{"display_name": "Stanford University"}],
                "raw_affiliation_strings": ["Stanford University"],
            },
            {
                "institutions": [{"display_name": "MIT"}],
                "raw_affiliation_strings": [],
            },
        ]
    }
    affils, institutions = affil._parse_authorships(work)
    # Institutions are deduped, order preserved.
    assert institutions == ["Stanford University", "MIT"]
    # Affiliation strings keep both display names and raw strings for matching.
    assert "Stanford University" in affils
    assert "Dept. of Statistics, Stanford University, CA" in affils


def test_backfill_affiliations_populates_institutions(monkeypatch):
    p = Paper(source="arxiv", paper_id="2401.00003", title="t", authors=["A"],
              abstract="", url="")
    monkeypatch.setattr(
        affil, "_fetch_affiliations_and_institutions",
        lambda doi: (["Princeton University"], ["Princeton University"]),
    )
    n = affil.backfill_affiliations([p])
    assert n == 1
    assert p.institutions == ["Princeton University"]
    assert p.affiliations == ["Princeton University"]


def test_backfill_skips_already_populated(monkeypatch):
    p = Paper(source="arxiv", paper_id="2401.00004", title="t", authors=["A"],
              abstract="", url="", institutions=["MIT"], affiliations=["MIT"])

    def _boom(doi):  # must not be called
        raise AssertionError("should not fetch when already populated")

    monkeypatch.setattr(affil, "_fetch_affiliations_and_institutions", _boom)
    assert affil.backfill_affiliations([p]) == 0
    assert p.institutions == ["MIT"]


def test_doi_for_arxiv_and_journal():
    p = Paper(source="arxiv", paper_id="2401.01234v2", title="t", authors=[], abstract="", url="")
    assert affil._doi_for(p) == "10.48550/arXiv.2401.01234"
    j = Paper(source="crossref", paper_id="10.1214/23-AOS2345", title="t", authors=[],
              abstract="", url="https://doi.org/10.1214/23-AOS2345")
    assert affil._doi_for(j) == "10.1214/23-AOS2345"
