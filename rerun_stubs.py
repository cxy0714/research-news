#!/usr/bin/env python
"""Re-run deep-read for stub files for 2026-06-12."""
import json
import logging
import os
import sys
from datetime import date
from dotenv import load_dotenv
from pathlib import Path

from research_news.deep_read import deep_read_paper, DEEP_READS_DIR, DEEP_READS_INDEX_PATH
from research_news.llm.sjtu_client import SJTUClient
from research_news.models import Paper

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("rerun_stubs")

load_dotenv()

STUB_IDS = ["2606.11746", "2606.12184", "2606.11587", "2606.12324"]
report_date = date(2026, 6, 12)
interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")

# Build Paper objects from the deep_reads_index metadata + PDFs
idx = json.loads(DEEP_READS_INDEX_PATH.read_text())
stub_entries = [e for e in idx if e.get("paper_id") in STUB_IDS]

client = SJTUClient()

for entry in stub_entries:
    pid = entry["paper_id"]
    # Find the PDF
    pdf_path = None
    for p in Path("data/highlights").rglob(f"{pid}.pdf"):
        pdf_path = str(p)
        break

    paper = Paper(
        paper_id=pid,
        title=entry.get("title", ""),
        authors=entry.get("authors", "").split(", ") if entry.get("authors") else [],
        abstract=entry.get("abstract", ""),
        score=float(entry.get("score", 0)),
        source="arxiv",
        url=f"https://arxiv.org/abs/{pid}",
        pdf_path=pdf_path,
        topic=entry.get("topic", ""),
    )
    
    log.info("deep reading %s (score=%.1f) ...", pid, paper.score)
    body = deep_read_paper(client, paper, interests_text, model="deepseek-reasoner")
    
    if body:
        out_path = DEEP_READS_DIR / f"{report_date.isoformat()}-{pid}.md"
        out_path.write_text(body, encoding="utf-8")
        log.info("deep read succeeded for %s (%d chars)", pid, len(body))
    else:
        log.warning("deep read FAILED for %s", pid)

log.info("all stubs processed")