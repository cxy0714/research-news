"""Offline tests for the synthesis engine's pure logic (no LLM, no network)."""
from __future__ import annotations

import json

from research_news import extract_problems as ep
from research_news import synthesize as syn


# ── extraction parsing ────────────────────────────────────────────────────────

def test_parse_extraction_plain_and_fenced():
    payload = {
        "direction": "proximal causal inference",
        "open_questions": ["identification under weak proxies"],
        "stated_limitations": ["requires completeness"],
        "future_work": [{"item": "extend to longitudinal", "boilerplate": False}],
        "narrow_conclusions": [],
        "cited_tensions": [],
        "transfer_hints": ["minimax rate for the proxy regression"],
    }
    raw = json.dumps(payload, ensure_ascii=False)
    assert ep.parse_extraction(raw)["direction"] == "proximal causal inference"
    fenced = "```json\n" + raw + "\n```"
    assert ep.parse_extraction(fenced)["open_questions"] == ["identification under weak proxies"]
    # Trailing prose after the object is tolerated.
    assert ep.parse_extraction(raw + "\n\n好的就这些") is not None


def test_parse_extraction_garbage_returns_none():
    assert ep.parse_extraction("not json at all") is None


def test_parse_extraction_normalizes_missing_fields():
    out = ep.parse_extraction('{"direction": "x"}')
    assert out["direction"] == "x"
    assert out["future_work"] == [] and out["transfer_hints"] == []


def test_load_append_roundtrip(tmp_path):
    p = tmp_path / "open_problems.jsonl"
    ep._append_row({"paper_id": "a", "topic": "t", "open_questions": ["q1"]}, path=p)
    ep._append_row({"paper_id": "b", "topic": "t"}, path=p)
    assert ep.load_done_ids(p) == {"a", "b"}
    rows = ep.load_rows(p)
    assert rows["a"]["open_questions"] == ["q1"]


# ── synthesis helpers ─────────────────────────────────────────────────────────

def test_fw_items_drops_boilerplate():
    fw = [
        {"item": "real extension", "boilerplate": False},
        {"item": "left for future work", "boilerplate": True},
        "bare string item",
    ]
    assert syn._fw_items(fw) == ["real extension", "bare string item"]


def test_survey_excerpt_extracts_section_one():
    body = (
        "# Title\n\n### 一、领域脉络与小综述\n这是综述内容，讲方向 history。\n\n"
        "### 二、这篇论文做了什么\n不该出现的细节。\n"
    )
    ex = syn.survey_excerpt(body)
    assert "综述内容" in ex
    assert "不该出现" not in ex


def test_build_user_message_numbers_and_cites():
    entries = [
        {"paper_id": "p1", "title": "Paper One", "venue": "AoS", "date": "2026-01-01",
         "body": "### 一、领域脉络\nfoo\n\n### 二、x\nbar"},
        {"paper_id": "p2", "title": "Paper Two", "venue": "JASA", "date": "2026-02-01",
         "body": ""},
    ]
    rows = {
        "p1": {"direction": "dir1", "open_questions": ["oq1"],
               "future_work": [{"item": "fw1", "boilerplate": False}]},
        "p2": {"stated_limitations": ["lim2"]},
    }
    msg = syn.build_user_message("causal_inference", entries, rows)
    assert "[1] Paper One" in msg and "[2] Paper Two" in msg
    assert "因果推断" in msg          # topic label
    assert "dir1" in msg and "fw1" in msg and "lim2" in msg


def test_update_index_dedups_by_date_topic(tmp_path, monkeypatch):
    idx = tmp_path / "synthesis_index.json"
    monkeypatch.setattr(syn, "SYNTHESIS_INDEX", idx)
    monkeypatch.setattr(syn, "DOCS_DIR", tmp_path)  # keep the archive out of real docs/
    syn._update_index([{"date": "2026-06-01", "topic": "x", "n_papers": 3}])
    syn._update_index([{"date": "2026-06-01", "topic": "x", "n_papers": 5}])  # overwrite
    syn._update_index([{"date": "2026-06-01", "topic": "y", "n_papers": 4}])
    data = json.loads(idx.read_text())
    assert len(data) == 2
    x = [e for e in data if e["topic"] == "x"][0]
    assert x["n_papers"] == 5
