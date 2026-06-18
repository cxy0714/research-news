"""Offline tests for the OCIS season-page generator's pure logic (no LLM)."""
from __future__ import annotations

from research_news import talk_seasons as ts


def test_season_of_prefers_tag_then_date():
    assert ts.season_of({"season": "Spring-2024", "date": "2024-03-01"}) == "spring-2024"
    assert ts.season_of({"date": "2024-03-01"}) == "spring-2024"   # Jan–May → spring
    assert ts.season_of({"date": "2024-07-01"}) == "summer-2024"   # Jun–Aug → summer
    assert ts.season_of({"date": "2024-10-01"}) == "fall-2024"     # Sep–Dec → fall
    assert ts.season_of({}) == "unknown"


def test_season_sort_and_label():
    slugs = ["spring-2024", "fall-2023", "summer-2024", "spring-2023"]
    ordered = sorted(slugs, key=ts.season_sort_key, reverse=True)
    assert ordered == ["summer-2024", "spring-2024", "fall-2023", "spring-2023"]
    assert ts.season_label("spring-2024") == "Spring 2024"


def test_group_by_season():
    rows = [
        {"date": "2024-03-01", "speaker": "A"},
        {"date": "2024-04-01", "speaker": "B"},
        {"season": "fall-2023", "date": "2023-10-01", "speaker": "C"},
    ]
    groups = ts.group_by_season(rows)
    assert {len(v) for v in groups.values()} == {2, 1}
    assert set(groups) == {"spring-2024", "fall-2023"}


def test_render_season_page_lists_read_and_unread(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "SEASONS_DIR", tmp_path / "seasons")
    read_idx = {"ocis-2024-03-01-jane-doe": {"doc_path": "talks/2024-03-01-jane.md"}}
    rows = [
        {"date": "2024-03-01", "speaker": "Jane Doe", "title": "Read Talk",
         "video": "https://youtu.be/v", "slides": "https://drive/x", "arxiv": "https://arxiv.org/abs/1"},
        {"date": "2024-04-01", "speaker": "No Read", "title": "Unread Talk",
         "discussant": "Bob"},
    ]
    entries = [ts._entry(r, read_idx) for r in rows]
    page = ts.render_season_page("spring-2024", entries, "本季围绕 proximal 与半参数效率。")
    body = page.read_text(encoding="utf-8")
    assert page.name == "spring-2024.md"
    assert "# OCIS · Spring 2024" in body
    assert "本季导览" in body and "proximal" in body
    assert "[Read Talk](../2024-03-01-jane.md)" in body        # links to the deep-read
    assert "Unread Talk　*（暂无精读）*" in body                 # metadata-only, flagged
    assert "[视频](https://youtu.be/v)" in body and "[arXiv]" in body
    assert "**讨论人**: Bob" in body


def test_first_sentence():
    assert ts._first_sentence("这一季关注 proximal 因果推断。还有别的。") == "这一季关注 proximal 因果推断。"
    assert ts._first_sentence("") == ""


def test_first_sentence_strips_bold_and_cuts_clean():
    # A long first "sentence" with no period within the limit must not end inside
    # a **bold** span (which would break the markdown).
    long = "这一季围绕**未观测混杂**（A、B、C）、**半参数效率与去偏**（D、E、F）、" + "讨论" * 60
    s = ts._first_sentence(long)
    assert "**" not in s and s.endswith("…")


def test_existing_overview_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "SEASONS_DIR", tmp_path)
    entries = [ts._entry({"date": "2024-03-01", "speaker": "A", "title": "T"}, {})]
    ts.render_season_page("spring-2024", entries, "本季围绕 proximal 展开。\n\n第二段。")
    assert ts._existing_overview("spring-2024") == "本季围绕 proximal 展开。\n\n第二段。"
    assert ts._existing_overview("fall-1999") == ""        # no page → empty


def test_write_archive_groups_by_year(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "DOCS", tmp_path)
    ts.write_archive([
        {"season": "spring-2024", "label": "Spring 2024", "n": 10, "n_read": 8,
         "doc_path": "talks/seasons/spring-2024.md", "blurb": "半参数效率与 DML。"},
        {"season": "fall-2023", "label": "Fall 2023", "n": 11, "n_read": 11,
         "doc_path": "talks/seasons/fall-2023.md", "blurb": ""},
    ])
    md = (tmp_path / "all_talks.md").read_text(encoding="utf-8")
    assert "## 2024" in md and "## 2023" in md
    assert "[Spring 2024](talks/seasons/spring-2024.md)" in md
    assert "10 场（8 精读）" in md and "半参数效率与 DML。" in md
