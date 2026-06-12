#!/usr/bin/env python
"""Re-run deep-read for stub/incomplete deep-read files for a given date."""
import json
import logging
import sys
from datetime import date
from dotenv import load_dotenv
from pathlib import Path

from research_news.deep_read import (
    deep_read_paper, generate_deep_read_report, select_deep_read_papers,
    DEEP_READS_DIR, DEEP_READS_INDEX_PATH,
)
from research_news.llm.sjtu_client import SJTUClient
from research_news.models import Paper
from research_news.score_log import load_scored_for_date

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("rerun_deep_reads")


def main():
    load_dotenv()
    report_date = date(2026, 6, 12)
    interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")
    client = SJTUClient()

    # Find stub files (very small, likely incomplete)
    stub_ids = []
    for f in DEEP_READS_DIR.glob(f"{report_date.isoformat()}-*.md"):
        size = f.stat().st_size
        if size < 1000:  # less than 1KB = stub
            pid = f.stem.split("-", 2)[-1]  # e.g. 2606.11587
            stub_ids.append(pid)
            log.info("found stub: %s (%d bytes)", pid, size)

    if not stub_ids:
        log.info("no stubs found, nothing to do")
        return

    # Load all scored papers for today and find the stub ones
    all_scored = load_scored_for_date(report_date)
    stub_papers = [p for p in all_scored if p.paper_id in stub_ids]
    log.info("re-running deep-read for %d stub papers", len(stub_papers))

    for p in stub_papers:
        log.info("deep reading %s ...", p.paper_id)
        body = deep_read_paper(client, p, interests_text, model="deepseek-reasoner")
        if body:
            out_path = DEEP_READS_DIR / f"{report_date.isoformat()}-{p.paper_id}.md"
            out_path.write_text(body, encoding="utf-8")
            log.info("deep read succeeded for %s (%d chars)", p.paper_id, len(body))
        else:
            log.warning("deep read FAILED for %s", p.paper_id)

    # Update index
    generate_deep_read_report(stub_papers, client, interests_text, report_date, "daily", model="deepseek-reasoner")

    log.info("done")


if __name__ == "__main__":
    main()