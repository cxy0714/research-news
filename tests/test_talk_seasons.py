"""Offline tests for the series/season talk-page generator's pure logic (no LLM)."""
from __future__ import annotations

from research_news import talk_seasons as ts


def test_season_of_prefers_tag_then_date():
    assert ts.season_of({"season": "Spring-2024", "date": "2024-03-01"}) == "spring-2024"
    assert ts.season_of({"date": "2024-03-01"}) == "spring-2024"   # Jan–May → spring
    assert ts.season_of({"date": "2024-07-01"}) == "summer-2024"   # Jun–Aug → summer
    assert ts.season_of({"date": "2024-10-01"}) == "fall-2024"     # Sep–Dec → fall
    assert ts.season_of({}) == "unknown"


def test_series_of():
    assert ts.series_of({"series": "INI"}) == "INI"
    assert ts.series_of({"venue": "OCIS (Online Causal Inference Seminar)"}) == "OCIS"
    assert ts.series_of({"venue": "INI CIFW04 (Isaac Newton Institute)"}) == "INI"
    assert ts.series_of({"venue": "University of Cambridge (INI)"}) == "INI"
    assert ts.series_of({"venue": "Some Workshop"}) == "Some Workshop"
    assert ts.series_of({}) == "其他"


def test_season_sort_label_and_page_slug():
    slugs = ["spring-2024", "fall-2023", "summer-2024", "spring-2023"]
    assert sorted(slugs, key=ts.season_sort_key, reverse=True) == [
        "summer-2024", "spring-2024", "fall-2023", "spring-2023"]
    assert ts.season_label("spring-2024") == "Spring 2024"
    assert ts.page_slug("OCIS", "spring-2024") == "ocis-spring-2024"
    assert ts.page_slug("INI", "summer-2026") == "ini-summer-2026"


def test_group_by_series_season():
    rows = [
        {"id": "a", "series": "OCIS", "date": "2024-03-01"},
        {"id": "b", "series": "OCIS", "date": "2024-04-01"},
        {"id": "c", "series": "INI", "date": "2026-06-01"},
    ]
    g = ts.group_by_series_season(rows)
    assert set(g) == {("OCIS", "spring-2024"), ("INI", "summer-2026")}
    assert len(g[("OCIS", "spring-2024")]) == 2


def test_handcurated_rows_includes_series_and_arxiv(tmp_path):
    p = tmp_path / "talks.yaml"
    p.write_text(
        "talks:\n"
        "  - id: robins\n    url: https://youtu.be/x\n    series: INI\n"
        "    date: '2026-06'\n    title: Keynote\n    speaker: Robins\n    papers: ['2002.05670']\n",
        encoding="utf-8",
    )
    rows = ts._handcurated_rows(p)
    assert rows[0]["id"] == "robins" and rows[0]["series"] == "INI"
    assert rows[0]["video"] == "https://youtu.be/x"
    assert rows[0]["arxiv"] == "https://arxiv.org/abs/2002.05670"


def test_render_season_page_lists_read_and_unread(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "SEASONS_DIR", tmp_path / "seasons")
    read_idx = {"ocis-2024-03-01-jane-doe": {"doc_path": "talks/2024-03-01-jane.md"}}
    rows = [
        {"date": "2024-03-01", "speaker": "Jane Doe", "title": "Read Talk",
         "video": "https://youtu.be/v", "slides": "https://drive/x", "arxiv": "https://arxiv.org/abs/1"},
        {"date": "2024-04-01", "speaker": "No Read", "title": "Unread Talk", "discussant": "Bob"},
    ]
    entries = [ts._entry(r, read_idx) for r in rows]
    page = ts.render_season_page("ocis-spring-2024", "OCIS · Spring 2024", entries,
                                 "本季围绕 proximal 与半参数效率。")
    body = page.read_text(encoding="utf-8")
    assert page.name == "ocis-spring-2024.md"
    assert "# OCIS · Spring 2024" in body
    assert "本季导览" in body and "proximal" in body
    assert "[Read Talk](../2024-03-01-jane.md)" in body        # links to the deep-read
    assert "Unread Talk　*（暂无精读）*" in body                 # metadata-only, flagged
    assert "[视频](https://youtu.be/v)" in body and "[arXiv]" in body
    assert "**讨论人**: Bob" in body


def test_first_sentence_strips_bold_and_cuts_clean():
    assert ts._first_sentence("这一季关注 proximal 因果推断。还有别的。") == "这一季关注 proximal 因果推断。"
    assert ts._first_sentence("") == ""
    long = "这一季围绕**未观测混杂**（A、B、C）、**半参数效率与去偏**（D、E、F）、" + "讨论" * 60
    s = ts._first_sentence(long)
    assert "**" not in s and s.endswith("…")


def test_existing_overview_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "SEASONS_DIR", tmp_path)
    entries = [ts._entry({"date": "2024-03-01", "speaker": "A", "title": "T"}, {})]
    ts.render_season_page("ocis-spring-2024", "OCIS · Spring 2024", entries,
                          "本季围绕 proximal 展开。\n\n第二段。")
    assert ts._existing_overview("ocis-spring-2024") == "本季围绕 proximal 展开。\n\n第二段。"
    # legacy fallback: a bare-season page name is found too
    ts.render_season_page("spring-2099", "OCIS · Spring 2099", entries, "旧版导览。")
    assert ts._existing_overview("ocis-spring-2099", "spring-2099") == "旧版导览。"
    assert ts._existing_overview("nope-1999") == ""


def test_write_archive_groups_by_series(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "DOCS", tmp_path)
    ts.write_archive([
        {"slug": "ocis-spring-2024", "series": "OCIS", "season": "spring-2024",
         "label": "Spring 2024", "n": 10, "n_read": 8,
         "doc_path": "talks/seasons/ocis-spring-2024.md", "blurb": "半参数效率与 DML。"},
        {"slug": "ini-summer-2026", "series": "INI", "season": "summer-2026",
         "label": "Summer 2026", "n": 1, "n_read": 1,
         "doc_path": "talks/seasons/ini-summer-2026.md", "blurb": "Robins 的 HOIF。"},
    ])
    md = (tmp_path / "all_talks.md").read_text(encoding="utf-8")
    assert "## OCIS" in md and "## INI" in md
    assert md.index("## OCIS") < md.index("## INI")               # OCIS first
    assert "[Spring 2024](talks/seasons/ocis-spring-2024.md)" in md
    assert "[Summer 2026](talks/seasons/ini-summer-2026.md)" in md
