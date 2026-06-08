"""Tests for the journal issue-rerun targeting / assembly / backup / dry-run.

Offline only: no Crossref, no LLM. The rerun() integration test uses a snapshot
source and --dry-run so nothing is fetched or written."""
from __future__ import annotations

import json
from pathlib import Path

from research_news import journals as j
from research_news.models import Paper


def _write_page(d: Path, name: str, dois: list[str]) -> Path:
    lines = [f"# {name}\n", "## 因果推断  *(causal_inference, N 篇)*\n"]
    for i, doi in enumerate(dois, 1):
        lines.append(f"### {i}. [{doi}](https://doi.org/{doi}) — Paper {i}")
        lines.append("- **作者**: A")
    p = d / name
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


# ── issue-spec parsing ─────────────────────────────────────────────────────────

def test_parse_issue_arg():
    assert j._parse_issue_arg("v54-i1") == (54, 1)
    assert j._parse_issue_arg("54-1") == (54, 1)
    assert j._parse_issue_arg("54/2") == (54, 2)
    assert j._parse_issue_arg("v54") == (54, None)


# ── target resolution (uses a temp journals dir + the real journals.yaml) ───────

def test_resolve_targets_recent_n(tmp_path, monkeypatch):
    monkeypatch.setattr("research_news.render.markdown.JOURNALS_DIR", tmp_path)
    for v, i in [(54, 1), (54, 2), (53, 5), (53, 6)]:
        _write_page(tmp_path, f"2026-05-26-aos-v{v}-i{i}.md", ["10.1214/x"])
    _write_page(tmp_path, "2026-05-26-biometrika-v113-i2.md", ["10.1093/y"])

    targets = j._resolve_rerun_targets(only=["AoS"], only_group=None,
                                       recent=2, issue=None)
    assert [(t.vol, t.iss) for t in targets] == [(54, 2), (54, 1)]  # 2 most recent
    assert all(t.short == "AoS" and t.issn == "0090-5364" for t in targets)


def test_resolve_targets_by_group_and_issue(tmp_path, monkeypatch):
    monkeypatch.setattr("research_news.render.markdown.JOURNALS_DIR", tmp_path)
    _write_page(tmp_path, "2026-05-26-aos-v54-i1.md", ["10.1214/x"])
    _write_page(tmp_path, "2026-05-26-biometrika-v113-i2.md", ["10.1093/y"])
    _write_page(tmp_path, "2026-06-07-econometrica-v94-i1.md", ["10.3982/z"])

    # whole core group
    core = j._resolve_rerun_targets(only=None, only_group=["core"],
                                    recent=None, issue=None)
    shorts = {t.short for t in core}
    assert "AoS" in shorts and "Biometrika" in shorts
    assert "Econometrica" not in shorts  # econ group, excluded

    # one specific issue
    one = j._resolve_rerun_targets(only=["AoS"], only_group=None,
                                   recent=None, issue="v54-i1")
    assert len(one) == 1 and (one[0].vol, one[0].iss) == (54, 1)


def test_resolve_targets_skips_unversioned_and_orphan_pages(tmp_path, monkeypatch):
    monkeypatch.setattr("research_news.render.markdown.JOURNALS_DIR", tmp_path)
    _write_page(tmp_path, "2026-05-26-jasa.md", ["10.1080/x"])       # no vol → skip
    _write_page(tmp_path, "2026-05-26-notajournal-v1-i1.md", ["10.0/z"])  # orphan
    _write_page(tmp_path, "2026-05-26-aos-v54-i1.md", ["10.1214/x"])
    targets = j._resolve_rerun_targets(only=None, only_group=None,
                                       recent=None, issue=None)
    assert [t.short for t in targets] == ["AoS"]


# ── page DOIs + issue membership ────────────────────────────────────────────────

def test_page_dois(tmp_path):
    p = _write_page(tmp_path, "2026-05-26-aos-v54-i1.md",
                    ["10.1214/a", "10.1214/b"])
    assert j._page_dois(p) == ["10.1214/a", "10.1214/b"]


def test_paper_in_issue_matches_on_categories_when_fields_none():
    # Old snapshots leave volume/issue None but always carry the categories.
    p = Paper(source="crossref", paper_id="10.1214/x", title="T", authors=[],
              abstract="a", url="u", categories=["vol 54", "issue 1"],
              venue="Annals of Statistics", volume=None, issue=None)
    assert j._paper_in_issue(p, 54, 1)
    assert j._paper_in_issue(p, 54, None)
    assert not j._paper_in_issue(p, 54, 2)
    assert not j._paper_in_issue(p, 53, 1)


def test_paper_in_issue_matches_on_fields_when_present():
    p = Paper(source="crossref", paper_id="10.1214/x", title="T", authors=[],
              abstract="a", url="u", categories=[], venue="X",
              volume="54", issue="2")
    assert j._paper_in_issue(p, 54, 2)
    assert not j._paper_in_issue(p, 54, 1)


# ── snapshot assembly ───────────────────────────────────────────────────────────

def _snapshot(tmp_path) -> Path:
    papers = [
        Paper(source="crossref", paper_id="10.1214/a", title="In issue one",
              authors=[], abstract="x", url="u", categories=["vol 54", "issue 1"],
              venue="Annals of Statistics"),
        Paper(source="crossref", paper_id="10.1214/b", title="Other issue",
              authors=[], abstract="x", url="u", categories=["vol 54", "issue 2"],
              venue="Annals of Statistics"),
        Paper(source="crossref", paper_id="10.1093/c", title="Other venue",
              authors=[], abstract="x", url="u", categories=["vol 54", "issue 1"],
              venue="Biometrika"),
        Paper(source="crossref", paper_id="10.1214/d", title="No abstract dropped",
              authors=[], abstract="", url="u", categories=["vol 54", "issue 1"],
              venue="Annals of Statistics"),
    ]
    snap = tmp_path / "corpus.json"
    snap.write_text(json.dumps([p.to_dict() for p in papers]), encoding="utf-8")
    return snap


def test_assemble_from_snapshot_filters_issue_venue_and_abstract(tmp_path):
    snap = _snapshot(tmp_path)
    t = j._Target(path=tmp_path / "p.md", short="AoS",
                  full="Annals of Statistics", issn="0090-5364",
                  vol=54, iss=1, when=__import__("datetime").date(2026, 5, 26))
    papers = j._assemble_issue_papers(t, snap)
    # Only the AoS v54-i1 paper with an abstract survives.
    assert [p.paper_id for p in papers] == ["10.1214/a"]


# ── backup ──────────────────────────────────────────────────────────────────────

def test_backup_issue_copies_page_and_deep_reads(tmp_path, monkeypatch):
    journals_dir = tmp_path / "journals"
    deep_dir = tmp_path / "deep_reads"
    backup_root = tmp_path / "backups"
    journals_dir.mkdir(); deep_dir.mkdir()
    monkeypatch.setattr("research_news.render.markdown.DEEP_READS_DIR", deep_dir)
    monkeypatch.setattr(j, "BACKUP_ROOT", backup_root)

    from research_news.deep_read import _slug as dr_slug
    import datetime
    when = datetime.date(2026, 5, 26)
    doi = "10.1214/25-aos2569"
    page = _write_page(journals_dir, "2026-05-26-aos-v54-i1.md", [doi])
    dr_page = deep_dir / f"{when.isoformat()}-{dr_slug(doi)}.md"
    dr_page.write_text("# deep read\n", encoding="utf-8")

    t = j._Target(path=page, short="AoS", full="Annals of Statistics",
                  issn="0090-5364", vol=54, iss=1, when=when)
    j._backup_issue(t, "20260607-120000")

    bdir = backup_root / "20260607-120000"
    assert (bdir / "journals" / page.name).exists()
    assert (bdir / "deep_reads" / dr_page.name).exists()


# ── dry-run integration (snapshot source, nothing fetched or written) ───────────

def test_rerun_dry_run_writes_nothing(tmp_path, monkeypatch):
    journals_dir = tmp_path / "journals"
    journals_dir.mkdir()
    monkeypatch.setattr("research_news.render.markdown.JOURNALS_DIR", journals_dir)
    # Page lists only paper "a"; the snapshot also has "a" for this issue.
    page = _write_page(journals_dir, "2026-05-26-aos-v54-i1.md", ["10.1214/a"])
    before = page.read_text(encoding="utf-8")
    snap = _snapshot(tmp_path)

    out = j.rerun(only=["AoS"], issue="v54-i1", from_snapshot=snap, dry_run=True)
    assert out == []                                   # dry-run returns no paths
    assert page.read_text(encoding="utf-8") == before  # page untouched


# ── completeness badge in the rendered header ───────────────────────────────────

def test_completeness_note_skipped_when_not_applicable():
    papers = [Paper(source="crossref", paper_id="10.1/a", title="T", authors=[],
                    abstract="x", url="u")]
    # disabled
    assert j._completeness_note("AoS", "Annals of Statistics", "0090-5364", "54",
                                "1", papers, enabled=False, source="openalex") is None
    # JMLR (no real ISSN / no issues)
    assert j._completeness_note("JMLR", "JMLR", "jmlr", None, None, papers,
                                enabled=True, source="openalex") is None
    # no volume
    assert j._completeness_note("AoS", "Annals of Statistics", "0090-5364", None,
                                None, papers, enabled=True, source="openalex") is None


def test_completeness_note_emitted(monkeypatch):
    from research_news import completeness as cmp
    papers = [Paper(source="crossref", paper_id="10.1214/a", title="Alpha",
                    authors=[], abstract="x", url="u")]
    monkeypatch.setattr(cmp, "resolve_authoritative",
                        lambda *a, **k: ([cmp.TocEntry("Alpha", "10.1214/a")], "openalex"))
    note = j._completeness_note("AoS", "Annals of Statistics", "0090-5364", "54",
                                "1", papers, enabled=True, source="openalex")
    assert note is not None and "目录核对 ✅" in note


def test_render_journal_page_includes_completeness_note(tmp_path):
    from research_news.render.markdown import render_journal_page
    papers = [Paper(source="crossref", paper_id="10.1214/a", title="Alpha",
                    authors=[], abstract="x", url="u", topic="causal_inference",
                    score=7.0)]
    out = render_journal_page(papers, "AoS", "Annals of Statistics", vol="54",
                              iss="1", output_dir=tmp_path,
                              completeness_note="目录核对 ✅ 1 篇全部抓到（对照 OpenAlex 1 篇）")
    text = out.read_text(encoding="utf-8")
    assert "- 共 1 篇 · Annals of Statistics" in text
    assert "- 目录核对 ✅ 1 篇全部抓到" in text
