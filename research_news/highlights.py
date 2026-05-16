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
import re
from datetime import date
from pathlib import Path

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from .models import Paper

log = logging.getLogger(__name__)

HIGHLIGHTS_DIR = Path("data/highlights")
MANIFEST_PATH = Path("data/highlights.json")


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s).strip("_") or "unknown"


def _pdf_url(paper: Paper) -> str | None:
    """Best-guess PDF URL by source."""
    if paper.source == "arxiv":
        return f"https://arxiv.org/pdf/{paper.paper_id}"
    if paper.source == "jmlr":
        # paper_id looks like "jmlr:v27/<stem>"; the PDF is at the same v27/<stem>.pdf
        m = re.match(r"jmlr:(v\d+)/(.+)$", paper.paper_id)
        if m:
            return f"https://www.jmlr.org/papers/{m.group(1)}/{m.group(2)}.pdf"
    if paper.source == "crossref" or (paper.url and "doi.org" in paper.url):
        # No reliable open PDF for paywalled DOIs; skip rather than fail noisily.
        return None
    return None


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=15))
def _download(url: str, dest: Path) -> None:
    with httpx.Client(timeout=120, follow_redirects=True,
                      headers={"User-Agent": "research-news/0.1"}) as c:
        with c.stream("GET", url) as r:
            r.raise_for_status()
            with dest.open("wb") as f:
                for chunk in r.iter_bytes(chunk_size=64 * 1024):
                    f.write(chunk)


def download_pdf(paper: Paper, base_dir: Path = HIGHLIGHTS_DIR) -> Path | None:
    """Download the paper's PDF into base_dir/<topic>/<slug>.pdf.

    Returns the local path (whether freshly downloaded or already present),
    or None if no PDF URL is available for this source.
    """
    url = _pdf_url(paper)
    if not url:
        log.info("no PDF source for %s (source=%s) — skipping", paper.paper_id, paper.source)
        return None
    topic = paper.topic or "other"
    folder = base_dir / _slug(topic)
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / f"{_slug(paper.paper_id)}.pdf"
    if dest.exists() and dest.stat().st_size > 1024:
        log.info("PDF already present: %s", dest)
        paper.pdf_path = str(dest)
        return dest
    try:
        log.info("downloading PDF for %s → %s", paper.paper_id, dest)
        _download(url, dest)
        paper.pdf_path = str(dest)
        return dest
    except Exception as e:
        log.warning("PDF download failed for %s (%s): %s", paper.paper_id, url, e)
        if dest.exists():
            try:
                dest.unlink()
            except OSError:
                pass
        return None


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
