"""Offline tests for the talk pipeline's pure logic (no ASR, no LLM, no network)."""
from __future__ import annotations

import json

from research_news import talks
from research_news.scrapers import transcribe as tr


# ── transcribe: timestamps + tag stripping ────────────────────────────────────

def test_parse_and_format_timestamp():
    assert tr.parse_timestamp("0:01:30") == 90.0
    assert tr.parse_timestamp("01:30") == 90.0
    assert tr.parse_timestamp("00:01:30.500") == 90.5
    assert tr.parse_timestamp("00:01:30,500") == 90.5  # SRT comma
    assert tr.parse_timestamp(42) == 42.0
    assert tr.format_ts(90) == "0:01:30"
    assert tr.format_ts(3661) == "1:01:01"


def test_strip_inline_tags():
    assert tr.strip_inline_tags("hello <00:00:01.200>world") == "hello world"
    assert tr.strip_inline_tags("<c>foo</c> bar") == "foo bar"


# ── transcribe: VTT parsing ───────────────────────────────────────────────────

def test_parse_vtt_basic():
    vtt = (
        "WEBVTT\n\n"
        "Kind: captions\n"
        "00:00:01.000 --> 00:00:03.000\n"
        "Welcome to the talk\n\n"
        "00:00:03.000 --> 00:00:05.000\n"
        "<c>today</c> we discuss <00:00:04.000>causality\n"
    )
    segs = tr.parse_vtt(vtt)
    assert [s["start"] for s in segs] == [1.0, 3.0]
    assert segs[0]["text"] == "Welcome to the talk"
    assert segs[1]["text"] == "today we discuss causality"


def test_segments_to_text_with_timestamps():
    segs = [{"start": 1, "text": "a"}, {"start": 65, "text": "b"}]
    assert tr.segments_to_text(segs) == "[0:00:01] a\n[0:01:05] b"
    assert tr.segments_to_text(segs, with_timestamps=False) == "a\nb"


# ── transcribe: cleaning ──────────────────────────────────────────────────────

def test_clean_transcript_drops_exact_repeats():
    text = "[0:00:01] hello\n[0:00:02] hello\n[0:00:03] world"
    assert tr.clean_transcript(text) == "[0:00:01] hello\n[0:00:03] world"


def test_clean_transcript_collapses_rolling_captions():
    # The classic YouTube auto-sub pattern: each line extends the previous.
    text = "[0:00:01] we\n[0:00:02] we study\n[0:00:03] we study causality"
    assert tr.clean_transcript(text) == "[0:00:03] we study causality"


def test_clean_transcript_collapses_rolling_overlap():
    # YouTube's other pattern: each cue's head repeats the previous cue's tail.
    text = (
        "[0:00:13] seminar. Uh today we have Dylan from the\n"
        "[0:00:15] Uh today we have Dylan from the University present\n"
        "[0:00:17] University present testing a causal hypothesis"
    )
    assert tr.clean_transcript(text) == (
        "[0:00:13] seminar. Uh today we have Dylan from the\n"
        "[0:00:15] University present\n"
        "[0:00:17] testing a causal hypothesis"
    )


def test_strip_inline_tags_decodes_entities():
    assert tr.strip_inline_tags("Q&amp;A and 5 &lt; 6") == "Q&A and 5 < 6"


def test_clean_transcript_strips_blank_and_tags():
    text = "[0:00:01] foo <00:00:01.500>bar\n\n   \n[0:00:02] baz"
    assert tr.clean_transcript(text) == "[0:00:01] foo bar\n[0:00:02] baz"


# ── transcribe: segment splitting ─────────────────────────────────────────────

def test_split_by_segments_single_when_empty():
    text = "[0:00:01] a\n[0:00:02] b"
    chunks = tr.split_by_segments(text, [])
    assert len(chunks) == 1
    assert chunks[0]["text"] == text


def test_split_by_segments_splits_at_boundaries():
    text = "\n".join([
        "[0:00:05] intro one",
        "[0:00:20] intro two",
        "[0:10:00] second talk starts",
        "[0:10:30] second talk more",
    ])
    segs = [
        {"start": "0:00:00", "speaker": "A", "title": "Talk A"},
        {"start": "0:10:00", "speaker": "B", "title": "Talk B"},
    ]
    chunks = tr.split_by_segments(text, segs)
    assert len(chunks) == 2
    assert chunks[0]["speaker"] == "A" and "intro one" in chunks[0]["text"]
    assert "second talk" not in chunks[0]["text"]
    assert chunks[1]["title"] == "Talk B" and "second talk starts" in chunks[1]["text"]


def test_split_by_segments_untimed_leadin_goes_to_first():
    text = "no timestamp preamble\n[0:00:05] timed line"
    chunks = tr.split_by_segments(text, [{"start": "0:00:00"}, {"start": "0:10:00"}])
    assert "no timestamp preamble" in chunks[0]["text"]


# ── talks: small helpers ──────────────────────────────────────────────────────

def test_is_arxiv_id_and_paper_url():
    assert talks._is_arxiv_id("2606.11421")
    assert talks._is_arxiv_id("2606.11421v2")
    assert not talks._is_arxiv_id("10.1214/aos")
    assert talks._paper_url("2606.11421") == "https://arxiv.org/abs/2606.11421"
    assert talks._paper_url("10.1214/aos") == "https://doi.org/10.1214/aos"


def test_asr_prompt_combines_default_and_talk():
    t = talks.Talk(id="x", url="u", asr_prompt="Robins, HOIF")
    assert talks._asr_prompt(t, "double robustness") == "double robustness, Robins, HOIF"
    assert talks._asr_prompt(talks.Talk(id="x", url="u"), "") is None


def test_talk_date_parsing():
    from datetime import date
    assert talks.talk_date(talks.Talk(id="x", url="u", date="2026-06-15")) == date(2026, 6, 15)
    assert talks.talk_date(talks.Talk(id="x", url="u", date="2026-06")) == date(2026, 6, 1)
    # Freeform / unparseable → today (just assert it doesn't raise and is a date).
    assert isinstance(talks.talk_date(talks.Talk(id="x", url="u", date="spring")), date)


# ── talks: config loading ─────────────────────────────────────────────────────

def test_load_talks_normalizes(tmp_path, monkeypatch):
    cfg = tmp_path / "talks.yaml"
    cfg.write_text(
        "asr_prompt_default: base terms\n"
        "talks:\n"
        "  - id: t1\n"
        "    url: https://example.com/v\n"
        "    title: First\n"
        "    topic: causal_inference\n"
        "    papers: [2606.11421]\n"
        "  - id: t2\n"
        "    url: https://example.com/w\n"
        "    topic: bogus_topic\n"
        "  - {url: https://example.com/no-id}\n",  # dropped: no id
        encoding="utf-8",
    )
    monkeypatch.setattr(talks, "TALKS_CONFIG", cfg)
    monkeypatch.setattr(talks, "OCIS_TALKS_CONFIG", tmp_path / "absent.yaml")
    default, ts = talks.load_talks()
    assert default == "base terms"
    assert [t.id for t in ts] == ["t1", "t2"]
    assert ts[0].topic == "causal_inference" and ts[0].papers == ["2606.11421"]
    assert ts[1].topic == "other"  # unknown topic normalized


# ── talks: cross-linking to deep reads ────────────────────────────────────────

def test_resolve_paper_links(tmp_path, monkeypatch):
    idx = tmp_path / "deep_reads_index.json"
    idx.write_text(json.dumps([
        {"paper_id": "2606.11421", "title": "Known Paper",
         "doc_path": "deep_reads/2026-06-12-2606.11421.md"},
    ]), encoding="utf-8")
    monkeypatch.setattr(talks, "DEEP_READS_INDEX", idx)
    t = talks.Talk(id="x", url="u", papers=["2606.11421", "2606.99999"])
    links = talks.resolve_paper_links(t)
    assert links[0]["title"] == "Known Paper"
    assert links[0]["doc_path"].endswith("2606.11421.md")
    assert links[1]["title"] is None and links[1]["doc_path"] is None

    md = "\n".join(talks._paper_links_md(links))
    assert "(../deep_reads/2026-06-12-2606.11421.md)" in md  # resolved → relative link
    assert "尚未精读" in md                                    # unresolved → hint


# ── talks: render + index + archive ───────────────────────────────────────────

def test_render_talk_page_has_metadata(tmp_path, monkeypatch):
    monkeypatch.setattr(talks, "TALKS_DIR", tmp_path / "talks")
    from datetime import date
    t = talks.Talk(id="robins-keynote", url="https://youtu.be/abc",
                   title="Keynote", speaker="James Robins", venue="Cambridge",
                   date="2026-06", topic="causal_inference")
    links = [{"id": "2606.11421", "title": "P", "doc_path": "deep_reads/x.md",
              "url": "https://arxiv.org/abs/2606.11421"}]
    page = talks._render_talk_page(
        t, "### 一、这场报告在讲哪条工作线\n内容", date(2026, 6, 1),
        file_id="robins-keynote", paper_links=links,
    )
    body = page.read_text(encoding="utf-8")
    assert page.name == "2026-06-01-robins-keynote.md"
    assert "# Keynote" in body
    assert "**讲者**: James Robins" in body
    assert "因果推断" in body                 # topic label
    assert "自动转写" in body                 # ASR caveat
    assert "../deep_reads/x.md" in body       # cross-link rewritten for docs/talks/
    assert "这场报告在讲哪条工作线" in body


def test_update_index_dedups_and_writes_archive(tmp_path, monkeypatch):
    idx = tmp_path / "talks_index.json"
    monkeypatch.setattr(talks, "TALKS_INDEX", idx)
    monkeypatch.setattr(talks, "DOCS_DIR", tmp_path)  # keep all_talks.md out of real docs/
    e1 = {"id": "a", "talk_id": "a", "date": "2026-06-01", "title": "Old",
          "venue": "OCIS", "topic": "causal_inference", "doc_path": "talks/a.md"}
    talks._update_index([e1])
    # Re-run with the same id overwrites; a new id is added.
    talks._update_index([{**e1, "title": "New"}])
    talks._update_index([{"id": "b", "talk_id": "b", "date": "2026-06-10",
                          "title": "Second", "venue": "INI", "topic": "other",
                          "doc_path": "talks/b.md"}])
    data = json.loads(idx.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert [e["id"] for e in data] == ["b", "a"]                  # newest date first
    assert [e for e in data if e["id"] == "a"][0]["title"] == "New"
    archive = (tmp_path / "all_talks.md").read_text(encoding="utf-8")
    assert "## OCIS" in archive and "## INI" in archive
    assert "(talks/a.md)" in archive


def test_ingest_from_subs_file(tmp_path, monkeypatch):
    # Offline path: feed an existing .srt (any tool's output) → cleaned transcript,
    # no download, no ASR.
    monkeypatch.setattr(talks, "TRANSCRIPTS_DIR", tmp_path)
    srt = tmp_path / "x.srt"
    srt.write_text(
        "1\n00:00:01,000 --> 00:00:03,000\nwe study causal inference\n\n"
        "2\n00:00:03,000 --> 00:00:05,000\nwe study causal inference\n\n"   # dup → collapsed
        "3\n00:00:05,000 --> 00:00:07,000\nand double robustness\n",
        encoding="utf-8",
    )
    t = talks.Talk(id="demo", url="https://youtu.be/x")
    out = talks.ingest(t, subs_file=str(srt))
    assert out == tmp_path / "demo.txt"
    body = out.read_text(encoding="utf-8")
    assert "[0:00:01] we study causal inference" in body
    assert "[0:00:05] and double robustness" in body
    assert body.count("we study causal inference") == 1   # consecutive dup collapsed


def test_prefer_subs_skips_instead_of_asr(tmp_path, monkeypatch):
    # In a bulk --prefer-subs run, a caption miss/429 must SKIP the talk, never
    # fall back to ASR (which would download audio + load a model).
    monkeypatch.setattr(talks, "TRANSCRIPTS_DIR", tmp_path)
    monkeypatch.setattr(talks.tr, "fetch_subtitles", lambda *a, **k: None)  # no captions

    def _boom(*a, **k):
        raise AssertionError("ASR must not run under --prefer-subs")
    monkeypatch.setattr(talks.tr, "download_audio", _boom)
    monkeypatch.setattr(talks.tr, "transcribe_audio", _boom)

    t = talks.Talk(id="nocaps", url="https://youtu.be/x")
    assert talks.ingest(t, prefer_subs=True) is None
    assert not (tmp_path / "nocaps.txt").exists()


def test_drive_pdf_url():
    assert talks._drive_pdf_url("https://drive.google.com/file/d/ABC123/view?usp=sharing") == \
        "https://drive.google.com/uc?export=download&id=ABC123"
    assert talks._drive_pdf_url("https://example.com/deck.pdf") == "https://example.com/deck.pdf"


def test_slides_candidates_by_host():
    # Google Drive file → confirm-bypass first
    d = talks._slides_candidates("https://drive.google.com/file/d/ABC/view")
    assert d[0].startswith("https://drive.usercontent.google.com/download?id=ABC")
    # Google Slides presentation → export/pdf
    p = talks._slides_candidates("https://docs.google.com/presentation/d/XYZ/edit?usp=sharing")
    assert p == ["https://docs.google.com/presentation/d/XYZ/export/pdf"]
    # Dropbox → force dl=1
    db = talks._slides_candidates("https://www.dropbox.com/s/abc/deck.pdf?dl=0")
    assert db == ["https://www.dropbox.com/s/abc/deck.pdf?dl=1"]
    # plain PDF → as-is
    assert talks._slides_candidates("https://x.edu/talk.pdf") == ["https://x.edu/talk.pdf"]


def test_ground_truth_context_includes_abstract():
    # No papers → no network call; just the OCIS abstract block.
    t = talks.Talk(id="x", url="u", abstract="The talk is about proximal causal inference.")
    ctx = talks.ground_truth_context(t)
    assert "proximal causal inference" in ctx and "权威" in ctx


def test_build_user_message_includes_context_and_discussant():
    t = talks.Talk(id="x", url="u", title="T", discussant="Dr. D")
    msg = talks.build_user_message(t, "transcript body", "interests",
                                   context="## 报告摘要\nGROUND TRUTH ABSTRACT")
    assert "GROUND TRUTH ABSTRACT" in msg
    assert "Discussant: Dr. D" in msg


def test_build_user_message_caps_and_includes(monkeypatch):
    monkeypatch.setattr(talks, "MAX_TRANSCRIPT_CHARS", 20)
    t = talks.Talk(id="x", url="u", title="T", papers=["2606.11421"])
    msg = talks.build_user_message(t, "y" * 100, "my interests")
    assert "my interests" in msg
    assert "2606.11421" in msg                 # candidate papers surfaced
    assert "y" * 20 in msg and "y" * 21 not in msg  # transcript capped
