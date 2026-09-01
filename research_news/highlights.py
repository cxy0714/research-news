"""Persist high-relevance papers: download their PDFs into per-topic folders
and maintain a JSON manifest at data/highlights.json.

Layout on disk:
    data/highlights/
      causal_inference/
        2605.14692.pdf
        10.1214_24-aos2401.pdf      # journal DOIs slugified
      high_dim_rmt/
        ...
    data/highlights.json            # list of entries (see _to_manifest_entry)
"""
from __future__ import annotations

import json
import logging
import os
import re
from datetime import date
from pathlib import Path

from . import oa_pdf
from .models import Paper

log = logging.getLogger(__name__)

HIGHLIGHTS_DIR = Path("data/highlights")
MANIFEST_PATH = Path("data/highlights.json")


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_") or "unknown"


def _pdf_url(paper: Paper) -> str | None:
    """Best-guess PDF URL by source (None when this source has no derivable one)."""
    if paper.pdf_url:
        return paper.pdf_url            # explicitly resolved (see oa_pdf.resolve)
    if paper.source == "arxiv":
        return f"https://arxiv.org/pdf/{paper.paper_id}"
    if paper.source == "jmlr":
        # paper_id is "jmlr:v27/<stem>"; the PDF lives at
        # /papers/volume27/<stem>/<stem>.pdf (NOT /papers/v27/<stem>.pdf — that
        # path 404s, which is why JMLR deep reads used to see only the abstract).
        m = re.match(r"jmlr:v(\d+)/(.+)$", paper.paper_id)
        if m:
            vol, stem = m.group(1), m.group(2)
            return f"https://www.jmlr.org/papers/volume{vol}/{stem}/{stem}.pdf"
    return None


# Try the open-access resolver (oa_pdf) for papers whose source gives no PDF URL
# — journal DOIs, mostly. Set OA_PDF=0 to skip it (saves a landing-page fetch per
# paper). Fails open either way: no PDF just means the deep read reads the abstract.
_OA_FALLBACK = os.environ.get("OA_PDF", "1").strip().lower() not in ("0", "false", "no")


def download_pdf(paper: Paper, base_dir: Path = HIGHLIGHTS_DIR) -> Path | None:
    """Download the paper's PDF into base_dir/<topic>/<slug>.pdf.

    Resolution order: an already-downloaded local file → the per-source URL guess
    (:func:`_pdf_url`) → the open-access resolver (landing-page meta tags / host
    rules / OpenAlex OA locations), which is what lets free journals be read in
    full rather than from their abstract alone.

    Returns the local path (freshly downloaded or already present), or None when
    no candidate yields a real PDF.
    """
    topic = paper.topic or "other"
    folder = base_dir / _slug(topic)
    dest = folder / f"{_slug(paper.paper_id)}.pdf"

    # Already on disk — either from an earlier run or fetched by the caller.
    for cached in (Path(paper.pdf_path) if paper.pdf_path else None, dest):
        if cached and cached.exists() and cached.stat().st_size > 1024:
            log.info("PDF already present: %s", cached)
            paper.pdf_path = str(cached)
            return cached

    folder.mkdir(parents=True, exist_ok=True)
    url = _pdf_url(paper)
    if url:
        log.info("downloading PDF for %s → %s", paper.paper_id, dest)
        if oa_pdf.fetch_pdf(url, dest):
            paper.pdf_path = str(dest)
            return dest
        log.warning("PDF download failed for %s (%s)", paper.paper_id, url)

    if not _OA_FALLBACK or not paper.url:
        if not url:
            log.info("no PDF source for %s (source=%s) — skipping",
                     paper.paper_id, paper.source)
        return None

    # Open-access fallback: resolve the landing page / DOI to a real PDF.
    doi = paper.paper_id if paper.paper_id.startswith("10.") else ""
    try:
        src = oa_pdf.resolve(paper.arxiv_url or paper.url, doi=doi)
    except Exception as e:  # noqa: BLE001 — never break the pipeline
        log.warning("OA resolve failed for %s: %s", paper.paper_id, e)
        return None
    if not src:
        log.info("no open PDF for %s (%s)", paper.paper_id, paper.url)
        return None
    got = oa_pdf.download(src, dest)
    if got:
        paper.pdf_url = src.pdf_url
        paper.pdf_path = str(got)
    return got


def _to_manifest_entry(paper: Paper, run_date: date) -> dict:
    return {
        "paper_id": paper.paper_id,
        "source": paper.source,
        "title": paper.title,
        "authors": paper.authors,
        "url": paper.url,
        "venue": paper.venue,
        "published": paper.published,
        "categories": paper.categories,
        "score": paper.score,
        "topic": paper.topic,
        "key_techniques": paper.key_techniques,
        "novelty_flag": paper.novelty_flag,
        "summary_zh": paper.summary_zh,
        "why_relevant": paper.why_relevant,
        "pdf_path": paper.pdf_path,
        "first_seen": run_date.isoformat(),
    }


def update_manifest(papers: list[Paper], run_date: date | None = None,
                    path: Path = MANIFEST_PATH) -> int:
    """Upsert each paper into the manifest (keyed by paper_id). Returns the
    number of NEW entries added (i.e. not previously in the manifest)."""
    run_date = run_date or date.today()
    path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(existing, list):
                existing = []
        except json.JSONDecodeError:
            log.warning("highlights manifest at %s was malformed; starting fresh", path)
            existing = []
    by_id = {e.get("paper_id"): e for e in existing if isinstance(e, dict)}
    n_new = 0
    for p in papers:
        entry = _to_manifest_entry(p, run_date)
        if p.paper_id in by_id:
            # Preserve original first_seen but refresh everything else
            entry["first_seen"] = by_id[p.paper_id].get("first_seen", entry["first_seen"])
        else:
            n_new += 1
        by_id[p.paper_id] = entry
    # Sort by first_seen desc, then score desc
    merged = sorted(
        by_id.values(),
        key=lambda e: (e.get("first_seen", ""), e.get("score") or 0),
        reverse=True,
    )
    path.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info("highlights manifest: %d total entries (%d new)", len(merged), n_new)
    return n_new


def save_highlights(papers: list[Paper], run_date: date | None = None,
                    base_dir: Path = HIGHLIGHTS_DIR,
                    manifest_path: Path = MANIFEST_PATH) -> None:
    """Download PDFs + update manifest in one call."""
    for p in papers:
        download_pdf(p, base_dir=base_dir)
    update_manifest(papers, run_date=run_date, path=manifest_path)
