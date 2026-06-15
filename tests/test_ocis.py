"""Offline tests for the OCIS importer's pure logic (no network, no LLM)."""
from __future__ import annotations

from research_news import talks
from research_news.scrapers import ocis


# ── redirect unwrapping + classification ──────────────────────────────────────

def test_unwrap_google_redirect():
    wrapped = "https://www.google.com/url?q=https%3A%2F%2Farxiv.org%2Fabs%2F2401.12345&sa=D&ust=1"
    assert ocis.unwrap_redirect(wrapped) == "https://arxiv.org/abs/2401.12345"
    # Non-redirect URLs pass through.
    assert ocis.unwrap_redirect("https://youtu.be/abc") == "https://youtu.be/abc"
    assert ocis.unwrap_redirect("") == ""


def test_classify_link():
    assert ocis.classify_link("https://www.youtube.com/watch?v=abc") == "video"
    assert ocis.classify_link("https://youtu.be/abc") == "video"
    assert ocis.classify_link("https://arxiv.org/abs/2401.12345") == "arxiv"
    assert ocis.classify_link("https://doi.org/10.1214/aos") == "doi"
    assert ocis.classify_link("https://docs.google.com/presentation/d/xyz") == "slides"
    assert ocis.classify_link("https://drive.google.com/file/d/xyz") == "slides"
    assert ocis.classify_link("https://example.com/talk.pdf") == "slides"
    assert ocis.classify_link("https://twitter.com/ocis") == "other"


def test_extract_links_handles_wrapped_and_direct():
    html = """
    <a href="https://www.google.com/url?q=https%3A%2F%2Farxiv.org%2Fabs%2F2401.12345&sa=D">paper</a>
    <a href="https://youtu.be/dQw4w9WgXcQ">video</a>
    <a href="https://docs.google.com/presentation/d/abc/edit">slides</a>
    <link href="https://fonts.googleapis.com/css">
    <a href="https://youtu.be/dQw4w9WgXcQ">dup video</a>
    """
    links = ocis.extract_links(html)
    kinds = {lk["kind"]: lk["url"] for lk in links}
    assert kinds["arxiv"] == "https://arxiv.org/abs/2401.12345"
    assert kinds["video"] == "https://youtu.be/dQw4w9WgXcQ"
    assert kinds["slides"].startswith("https://docs.google.com/presentation/")
    assert len(links) == 3  # font CDN dropped, duplicate video collapsed


def test_arxiv_id_from_url():
    assert ocis.arxiv_id_from_url("https://arxiv.org/abs/2401.12345") == "2401.12345"
    assert ocis.arxiv_id_from_url("https://arxiv.org/pdf/2401.12345v2") == "2401.12345"
    assert ocis.arxiv_id_from_url("https://example.com") is None


# ── dates + ids + season urls ─────────────────────────────────────────────────

def test_normalize_date():
    assert ocis.normalize_date("2024-04-16") == "2024-04-16"
    assert ocis.normalize_date("April 16, 2024") == "2024-04-16"
    assert ocis.normalize_date("sometime in spring") == "sometime in spring"
    assert ocis.normalize_date("") is None


def test_make_talk_id_stable():
    row = {"date": "April 16, 2024", "speaker": "James M. Robins", "title": "X"}
    assert ocis.make_talk_id(row) == "ocis-2024-04-16-james-m-robins"
    # No date → falls back to speaker only.
    assert ocis.make_talk_id({"speaker": "Jane Doe"}) == "ocis-jane-doe"


def test_season_urls():
    assert ocis.season_url("spring-2024") == \
        "https://sites.google.com/view/ocis/past-talks/spring-2024-talks"
    assert ocis.season_url("summer-2020-talks").endswith("summer-2020-talks")
    urls = ocis.default_season_urls(2020, 2021)
    assert len(urls) == 8  # 2 years × 4 seasons
    assert any("fall-2021-talks" in u for u in urls)


# ── row → entry + dedupe ──────────────────────────────────────────────────────

def test_row_to_talk_entry_with_arxiv():
    row = {"date": "April 16, 2024", "speaker": "J. Robins", "title": "HOIF",
           "video": "https://youtu.be/abc", "arxiv": "https://arxiv.org/abs/2401.12345",
           "slides": "https://docs.google.com/presentation/d/x"}
    e = ocis.row_to_talk_entry(row)
    assert e["url"] == "https://youtu.be/abc"
    assert e["venue"] == ocis.VENUE and e["topic"] == "causal_inference"
    assert e["papers"] == ["2401.12345"]
    assert e["date"] == "2024-04-16"


def test_row_to_talk_entry_requires_video():
    assert ocis.row_to_talk_entry({"speaker": "X", "arxiv": "https://arxiv.org/abs/1"}) is None
    assert ocis.row_to_talk_entry({"video": "https://example.com/not-youtube"}) is None


def test_dedupe_entries():
    entries = [
        {"id": "a", "url": "u1"},
        {"id": "a", "url": "u2"},   # dup id dropped
        {"id": "b", "url": "u3"},
        {"id": "c"},                # no url dropped
    ]
    out = ocis.dedupe_entries(entries)
    assert [e["id"] for e in out] == ["a", "b"]


def test_clean_text_with_links_inlines_and_unwraps():
    html = ('<div>Talk by <a href="https://www.google.com/url?q='
            'https%3A%2F%2Fyoutu.be%2Fabc123&sa=D">Watch</a></div>')
    text = ocis.clean_text_with_links(html)
    assert "Watch <https://youtu.be/abc123>" in text


# ── writer + config merge ─────────────────────────────────────────────────────

def test_write_talks_yaml_and_load_merge(tmp_path, monkeypatch):
    main = tmp_path / "talks.yaml"
    main.write_text(
        "asr_prompt_default: base\n"
        "talks:\n"
        "  - {id: hand-1, url: https://youtu.be/h1, topic: causal_inference}\n"
        "  - {id: shared, url: https://youtu.be/HAND, title: Hand}\n",
        encoding="utf-8",
    )
    ocis_path = tmp_path / "talks.ocis.yaml"
    ocis.write_talks_yaml([
        {"id": "ocis-1", "url": "https://youtu.be/o1", "venue": ocis.VENUE,
         "topic": "causal_inference"},
        {"id": "shared", "url": "https://youtu.be/OCIS", "title": "Ocis"},  # collides
    ], path=ocis_path)
    monkeypatch.setattr(talks, "TALKS_CONFIG", main)
    monkeypatch.setattr(talks, "OCIS_TALKS_CONFIG", ocis_path)

    default, ts = talks.load_talks()
    assert default == "base"                       # from the hand-curated file
    by_id = {t.id: t for t in ts}
    assert set(by_id) == {"hand-1", "shared", "ocis-1"}
    assert by_id["shared"].title == "Hand"         # hand-curated wins the collision
    assert by_id["ocis-1"].venue == ocis.VENUE
