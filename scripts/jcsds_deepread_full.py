# -*- coding: utf-8 -*-
"""Long-form deep-reads for JCSDS 2026 talks that have a matched arXiv paper.

The conf pipeline (research_news/conf/read.py) writes a *short* 300-500 word
inline deep_read into each sess<idx>_t<no>.json. This script reuses the *daily*
long-form deep-read (research_news.deep_read.deep_read_paper: full PDF, 240k
chars, 24k tokens, reference-enriched survey) to produce a standalone page per
paper under docs/deep_reads/jcsds2026-<arxiv>.md, and records the page path back
into each per-talk JSON as `long_read` so the topic-page generator can link it.

Scope: every talk with found=True and an arxiv_id (deduped by arxiv_id). PDFs
already in data/conferences/jcsds2026/pdfs/ are used as-is; missing ones are
downloaded (best effort). Idempotent: an existing non-stub page is skipped, so
the run is resumable.

Usage:
  python scripts/jcsds_deepread_full.py            # all, skip done, 4 workers
  python scripts/jcsds_deepread_full.py --limit 1  # smoke test: 1 paper
  python scripts/jcsds_deepread_full.py --workers 6
  python scripts/jcsds_deepread_full.py --force    # regenerate even if page exists
"""
from __future__ import annotations

import argparse
import glob
import json
import logging
import os
import re
import sys
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research_news.conf.read import _download_pdf, PDF_DIR
from research_news.deep_read import (
    deep_read_paper,
    DEEP_READ_FAILED_MARKER,
    extract_pdf_text,
)
from research_news.llm.sjtu_client import SJTUClient
from research_news.models import Paper

log = logging.getLogger("jcsds_deepread_full")

ROOT = Path("data/conferences/jcsds2026")
RDIR = ROOT / "research"
DEEP_READS_DIR = Path("docs/deep_reads")
MODEL = os.environ.get("TALK_MODEL") or os.environ.get("DEEP_READ_MODEL") \
    or os.environ.get("SJTU_MODEL_DEEP")
HOMEPAGE_URL = "https://cxy0714.github.io/"
REPO_URL = "https://github.com/cxy0714/research-news"

SESSIONS = json.load(open(ROOT / "sessions.json", encoding="utf-8"))

# The SJTU endpoint enforces a hard tokens-per-minute cap (observed 100k). A
# single full-PDF deep-read prompt is ~90-95k tokens, so at most one call may
# *enter* per rolling 60s window. This gate serializes the moment each worker
# fires its LLM call (not the whole 6-min generation), letting several reads
# overlap in flight while never bursting two prompts into the same minute.
_TPM_LIMIT = int(os.environ.get("JCSDS_TPM", "100000"))
_EST_TOKENS_PER_CALL = int(os.environ.get("JCSDS_EST_TOKENS", "96000"))


class TokenGate:
    """Block until admitting `cost` tokens keeps the rolling-60s spend under
    the limit. Records spend at admission time (prompt tokens dominate)."""

    def __init__(self, limit: int):
        self.limit = limit
        self.events: deque[tuple[float, int]] = deque()
        self.lock = threading.Lock()

    def acquire(self, cost: int) -> None:
        while True:
            with self.lock:
                now = time.monotonic()
                while self.events and now - self.events[0][0] > 60:
                    self.events.popleft()
                spent = sum(c for _, c in self.events)
                if spent + cost <= self.limit or not self.events:
                    self.events.append((now, cost))
                    return
                wait_for = 60 - (now - self.events[0][0]) + 0.5
            time.sleep(max(wait_for, 1.0))


_GATE = TokenGate(_TPM_LIMIT)


def _slug(arxiv_id: str) -> str:
    return arxiv_id.replace("/", "_")


def page_path_for(arxiv_id: str) -> Path:
    return DEEP_READS_DIR / f"jcsds2026-{_slug(arxiv_id)}.md"


def _is_real_page(p: Path) -> bool:
    """True if the page exists and is not a failure stub."""
    if not (p.exists() and p.stat().st_size > 512):
        return False
    return DEEP_READ_FAILED_MARKER not in p.read_text(encoding="utf-8")


def collect_talks() -> dict[str, dict]:
    """arxiv_id -> {arxiv_id, title, paper_title, url, abstract, speaker,
    session_idx, session_title, files:[per-talk json paths]}. Deduped by id."""
    by_id: dict[str, dict] = {}
    for f in glob.glob(str(RDIR / "sess*_t*.json")):
        m = re.search(r"sess(\d+)_t(\d+)\.json$", os.path.basename(f))
        if not m:
            continue
        idx = int(m.group(1))
        d = json.load(open(f, encoding="utf-8"))
        aid = d.get("arxiv_id")
        if not (d.get("found") and aid):
            continue
        aid = str(aid)
        rec = by_id.get(aid)
        if rec is None:
            rec = {
                "arxiv_id": aid,
                "title": d.get("title") or "",
                "paper_title": d.get("paper_title") or d.get("title") or "",
                "url": d.get("url") or f"https://arxiv.org/abs/{aid}",
                "abstract": d.get("abstract") or "",
                "speaker": d.get("speaker") or "",
                "session_idx": idx,
                "session_title": SESSIONS[idx]["title"] if idx < len(SESSIONS) else "",
                "files": [],
            }
            by_id[aid] = rec
        rec["files"].append(f)
    return by_id


def build_paper(rec: dict) -> Paper | None:
    """Build a Paper for deep_read_paper. Ensures a PDF is present (downloads
    on miss); falls back to the stored abstract if the PDF can't be had."""
    aid = rec["arxiv_id"]
    pdf = PDF_DIR / f"{_slug(aid)}.pdf"
    if not (pdf.exists() and pdf.stat().st_size > 1024):
        txt = _download_pdf(aid)  # writes into PDF_DIR as a side effect
        if not txt and not rec.get("abstract"):
            log.warning("no PDF and no abstract for %s — skipping", aid)
            return None
    pdf_path = str(pdf) if (pdf.exists() and pdf.stat().st_size > 1024) else None
    return Paper(
        source="arxiv",
        paper_id=aid,
        title=rec["paper_title"] or rec["title"],
        authors=[rec["speaker"]] if rec.get("speaker") else [],
        abstract=rec.get("abstract") or "",
        url=rec["url"],
        arxiv_url=f"https://arxiv.org/abs/{aid}",
        topic="conference",
        pdf_path=pdf_path,
    )


def render_page(rec: dict, content: str) -> Path:
    """Write docs/deep_reads/jcsds2026-<arxiv>.md. Conference-flavored header
    (session context instead of the daily relevance score)."""
    DEEP_READS_DIR.mkdir(parents=True, exist_ok=True)
    aid = rec["arxiv_id"]
    lines = [
        f"# {rec['paper_title'] or rec['title']}\n",
        f"**讲者**: {rec['speaker']}  ",
        f"**会场**: {rec['session_title']}  ",
        f"**报告题目**: {rec['title']}  ",
        f"**链接**: [arXiv]({rec['url']})  ",
        f"**来源**: JCSDS 2026 · [返回会议总览](../conferences/jcsds2026/index.md)\n",
        "---\n",
        content if content else DEEP_READ_FAILED_MARKER,
        f"\n---\n\nMaintained by 陈星宇 · "
        f"[Homepage]({HOMEPAGE_URL}) · [Source on GitHub]({REPO_URL})\n",
    ]
    out = page_path_for(aid)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def annotate_talk_files(rec: dict, doc_rel: str) -> None:
    """Write `long_read` (path relative to docs/) into each per-talk JSON."""
    for f in rec["files"]:
        d = json.load(open(f, encoding="utf-8"))
        d["long_read"] = doc_rel
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False)


def process_one(client: SJTUClient, interests: str, rec: dict, force: bool) -> str:
    aid = rec["arxiv_id"]
    doc_rel = f"deep_reads/{page_path_for(aid).name}"
    if not force and _is_real_page(page_path_for(aid)):
        annotate_talk_files(rec, doc_rel)  # ensure link recorded even on resume
        return f"skip {aid} (page exists)"
    paper = build_paper(rec)
    if paper is None:
        return f"SKIP {aid} (no source)"
    _GATE.acquire(_EST_TOKENS_PER_CALL)  # throttle to stay under tokens/min cap
    content = deep_read_paper(client, paper, interests, model=MODEL)
    render_page(rec, content)
    if content and DEEP_READ_FAILED_MARKER not in content:
        annotate_talk_files(rec, doc_rel)
        return f"ok {aid} ({len(content)} chars)"
    return f"FAIL {aid} (empty/failed content)"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="process at most N papers")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--force", action="store_true", help="regenerate existing pages")
    ap.add_argument("--only", help="comma-separated arxiv ids (smoke test)")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    interests = Path("config/interests.yaml").read_text(encoding="utf-8")
    by_id = collect_talks()
    recs = list(by_id.values())
    if args.only:
        want = {s.strip() for s in args.only.split(",")}
        recs = [r for r in recs if r["arxiv_id"] in want]
    if args.limit:
        recs = recs[: args.limit]
    log.info("MODEL=%s | %d unique papers to consider (workers=%d, force=%s)",
             MODEL, len(recs), args.workers, args.force)

    client = SJTUClient()
    done = ok = fail = skip = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process_one, client, interests, r, args.force): r
                for r in recs}
        for fut in as_completed(futs):
            done += 1
            try:
                msg = fut.result()
            except Exception as e:  # noqa: BLE001
                r = futs[fut]
                msg = f"EXC {r['arxiv_id']}: {e}"
            if msg.startswith("ok"):
                ok += 1
            elif msg.startswith("skip"):
                skip += 1
            else:
                fail += 1
            log.info("[%d/%d] %s", done, len(recs), msg)
    log.info("ALL DONE: ok=%d skip=%d fail=%d (of %d)", ok, skip, fail, len(recs))


if __name__ == "__main__":
    main()
