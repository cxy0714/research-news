"""Retroactively fill the '机构' (institution) line on already-rendered pages.

OpenAlex doesn't index brand-new arXiv preprints for several days, so the daily
run can't show institutions for papers that came out the same day (the lookup
404s). This module re-scans recently rendered daily / journal pages, looks up
any paper still missing its 机构 line in OpenAlex, and injects the line once the
work is indexed. It's idempotent — papers that already have a 机构 line (or that
OpenAlex still doesn't know) are left untouched — so it's cheap to run every day.

Run standalone with: ``python -m research_news.backfill_institutions``
"""
from __future__ import annotations

import argparse
import logging
import re
from datetime import date, timedelta
from pathlib import Path

from .render.markdown import format_institutions_line, DOCS_DIR, JOURNALS_DIR
from .scrapers import affiliations as affil

log = logging.getLogger(__name__)

# A paper heading like "#### 1. [2606.06441](https://arxiv.org/abs/2606.06441) — Title".
_HEADING_RE = re.compile(r"^#{2,6}\s+\d+\.\s+\[")
_ARXIV_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,6})")
_ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,6})(?:v\d+)?\b")
_DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s)\]]+)")


def _doi_from_heading(line: str) -> str | None:
    """Best-effort DOI for an OpenAlex lookup, parsed from a paper heading line."""
    m = _ARXIV_URL_RE.search(line)
    if m:
        return f"10.48550/arXiv.{m.group(1)}"
    m = _DOI_RE.search(line)
    if m:
        return m.group(1)
    m = _ARXIV_ID_RE.search(line)
    if m:
        return f"10.48550/arXiv.{m.group(1)}"
    return None


def _insert_institution_line(block: list[str], inst_line: str) -> list[str]:
    """Insert inst_line after the 期刊/来源 line, else after 作者 (matching the
    renderer's order). Returns the block unchanged if neither anchor is found."""
    anchor = None
    for j, b in enumerate(block):
        if b.startswith("- **作者**"):
            anchor = j
        elif b.startswith("- **期刊/来源**"):
            anchor = j  # prefer the venue line when present (it comes later)
            break
    if anchor is None:
        return block
    return block[: anchor + 1] + [inst_line] + block[anchor + 1 :]


def backfill_page(path: Path, *, budget: list[int] | None = None) -> bool:
    """Fill missing 机构 lines on one rendered page. Returns True if it changed.

    ``budget`` is an optional single-element list acting as a shared mutable
    counter capping the number of OpenAlex lookups across pages in one run.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    changed = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if not _HEADING_RE.match(line):
            out.append(line)
            i += 1
            continue
        # Collect this paper's block: everything up to the next heading of any
        # level (next paper or next topic/section).
        out.append(line)
        i += 1
        block: list[str] = []
        while i < len(lines) and not lines[i].startswith("#"):
            block.append(lines[i])
            i += 1

        if not any("**机构**" in b for b in block):
            if budget is not None and budget[0] <= 0:
                out.extend(block)
                continue
            doi = _doi_from_heading(line)
            if doi:
                if budget is not None:
                    budget[0] -= 1
                _, institutions = affil._fetch_affiliations_and_institutions(doi)
                if institutions:
                    block = _insert_institution_line(
                        block, format_institutions_line(institutions)
                    )
                    changed = True
        out.extend(block)

    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def _recent_pages(directory: Path, days: int) -> list[Path]:
    """Pages whose YYYY-MM-DD filename prefix is within the last `days` days."""
    if not directory.exists():
        return []
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    out = []
    for p in directory.glob("*.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", p.stem)
        if m and m.group(1) >= cutoff:
            out.append(p)
    return sorted(out, reverse=True)


def backfill_recent(days: int = 14, max_lookups: int = 400) -> int:
    """Backfill recent daily + journal pages. Returns the number of pages changed.

    Fails open: when the affiliation feature is disabled (AFFIL_GREENLIGHT=0) or
    OpenAlex is unreachable, nothing changes.
    """
    if not affil.greenlight_enabled():
        log.info("institution backfill skipped (AFFIL_GREENLIGHT disabled)")
        return 0
    pages = _recent_pages(DOCS_DIR, days) + _recent_pages(JOURNALS_DIR, days)
    if not pages:
        return 0
    budget = [max_lookups]
    n_changed = 0
    for p in pages:
        try:
            if backfill_page(p, budget=budget):
                n_changed += 1
                log.info("filled institutions in %s", p)
        except Exception as e:  # noqa: BLE001 — never let backfill break a run
            log.warning("institution backfill failed for %s: %s", p, e)
        if budget[0] <= 0:
            log.info("institution backfill hit lookup budget (%d)", max_lookups)
            break
    if n_changed:
        log.info("institution backfill updated %d page(s)", n_changed)
    return n_changed


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    ap = argparse.ArgumentParser(
        description="Retroactively fill author institutions on rendered pages."
    )
    ap.add_argument("--days", type=int, default=14,
                    help="How many days back to scan (default 14).")
    ap.add_argument("--max-lookups", type=int, default=400,
                    help="Cap on OpenAlex lookups in one run (default 400).")
    args = ap.parse_args()
    from dotenv import load_dotenv
    load_dotenv()
    changed = backfill_recent(days=args.days, max_lookups=args.max_lookups)
    print(f"updated {changed} page(s)")


if __name__ == "__main__":
    main()
