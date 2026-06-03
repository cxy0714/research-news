"""Persist the citation edges of deep-read papers.

For every deep read we already fetch the paper's references from Semantic
Scholar (for the survey block). Even when a cited work has no abstract — so it
never makes it into the prompt — S2 still gives us its identifiers (ArXiv id /
DOI / S2 id) and objective signals (influential? citation intent? how many
times it's been cited). We store those edges here so that, as the archive
grows, we accumulate a real citation graph over the papers we care about. That
graph can later surface hubs, bridges and recurring open problems that no
single deep read reveals.

Storage: data/citations.json — a list of per-paper records, upserted by
paper_id (re-running a deep read refreshes that paper's edges). Fail-open:
persisting is best-effort and never blocks the deep read.
"""
from __future__ import annotations

import json
import logging
from datetime import date
from pathlib import Path

log = logging.getLogger(__name__)

CITATIONS_FILE = Path("data/citations.json")


def edge_from_row(row: dict) -> dict | None:
    """Turn one raw S2 references row into a compact, objective edge record.

    Returns None when the cited work carries no usable identifier at all (we
    can't place it in a graph, so there's nothing worth storing).
    """
    cited = row.get("citedPaper") or {}
    ext = cited.get("externalIds") or {}
    arxiv = ext.get("ArXiv")
    doi = ext.get("DOI")
    s2 = cited.get("paperId")
    if not (arxiv or doi or s2):
        return None
    return {
        "arxiv": arxiv,
        "doi": doi,
        "s2": s2,
        "title": cited.get("title"),
        "year": cited.get("year"),
        "is_influential": bool(row.get("isInfluential")),
        "intents": list(row.get("intents") or []),
        "citation_count": cited.get("citationCount"),
    }


def build_record(paper_id: str, arxiv_id: str | None, rows: list[dict],
                 *, fetched: str | None = None) -> dict:
    """Build one citation record (the deep-read paper and its outgoing edges)."""
    edges = [e for e in (edge_from_row(r) for r in rows) if e]
    return {
        "paper_id": paper_id,
        "arxiv_id": arxiv_id,
        "fetched": fetched or date.today().isoformat(),
        "n_references_total": len(rows),
        "n_references_identified": len(edges),
        "references": edges,
    }


def _load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:  # noqa: BLE001
        return []


def save_record(record: dict, path: Path = CITATIONS_FILE) -> None:
    """Upsert one paper's citation record (keyed by paper_id). Fail-open."""
    try:
        existing = _load(path)
        by_id = {e.get("paper_id"): e for e in existing if isinstance(e, dict)}
        by_id[record["paper_id"]] = record
        merged = sorted(by_id.values(), key=lambda e: e.get("fetched") or "", reverse=True)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as e:  # noqa: BLE001 — never block the deep read
        log.warning("could not persist citation edges for %s: %s",
                    record.get("paper_id"), e)


def record_citations(paper_id: str, arxiv_id: str | None, rows: list[dict],
                     *, path: Path = CITATIONS_FILE) -> int:
    """Build + persist the citation record for one deep-read paper.

    Returns the number of identifiable edges stored.
    """
    record = build_record(paper_id, arxiv_id, rows)
    save_record(record, path)
    log.info("citation graph: stored %d/%d identifiable edge(s) for %s",
             record["n_references_identified"], record["n_references_total"], paper_id)
    return record["n_references_identified"]
