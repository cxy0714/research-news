"""arXiv daily-new scraper using the official API.

Strategy: query each category for entries submitted in the last 24h window
(UTC), filter to "new" submissions only (no cross-list, no replacements).
arXiv's RSS lumps new+cross+replacements together; the API gives us cleaner
control via submittedDate range and primary-category filtering.
"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import Paper

log = logging.getLogger(__name__)

ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"


@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=2, min=2, max=16))
def _fetch(params: dict) -> str:
    with httpx.Client(timeout=30, follow_redirects=True) as c:
        r = c.get(ARXIV_API, params=params)
        r.raise_for_status()
        return r.text


def _window_utc(days: int = 1) -> tuple[str, str]:
    end = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - timedelta(days=days)
    fmt = "%Y%m%d%H%M"
    return start.strftime(fmt), end.strftime(fmt)


def fetch_category(
    category: str,
    *,
    lookback_days: int = 1,
    max_results: int = 80,
    include_cross_listed: bool = False,
) -> list[Paper]:
    start, end = _window_utc(lookback_days)
    query = f"cat:{category} AND submittedDate:[{start} TO {end}]"
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": 0,
        "max_results": max_results,
    }
    xml = _fetch(params)
    root = ET.fromstring(xml)
    out: list[Paper] = []
    for entry in root.findall(f"{ATOM}entry"):
        arxiv_url = (entry.findtext(f"{ATOM}id") or "").strip()
        arxiv_id = arxiv_url.rsplit("/", 1)[-1]
        title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
        abstract = " ".join((entry.findtext(f"{ATOM}summary") or "").split())
        published = (entry.findtext(f"{ATOM}published") or "").strip()
        authors = [
            (a.findtext(f"{ATOM}name") or "").strip()
            for a in entry.findall(f"{ATOM}author")
        ]
        cats = [
            c.attrib.get("term", "")
            for c in entry.findall("{http://arxiv.org/schemas/atom}category")
        ]
        primary_el = entry.find("{http://arxiv.org/schemas/atom}primary_category")
        primary = primary_el.attrib.get("term") if primary_el is not None else ""

        if not include_cross_listed and primary != category:
            continue

        out.append(
            Paper(
                source="arxiv",
                paper_id=arxiv_id,
                title=title,
                authors=authors,
                abstract=abstract,
                url=arxiv_url.replace("http://", "https://"),
                categories=cats,
                published=published,
            )
        )
    log.info("arxiv %s: %d new papers", category, len(out))
    return out


def fetch_all(cfg: dict) -> list[Paper]:
    papers: list[Paper] = []
    for cat in cfg.get("categories", []):
        try:
            papers.extend(
                fetch_category(
                    cat,
                    max_results=cfg.get("max_per_category", 80),
                    include_cross_listed=cfg.get("include_cross_listed", False),
                )
            )
        except Exception as e:
            log.warning("arxiv fetch failed for %s: %s", cat, e)
    return papers
