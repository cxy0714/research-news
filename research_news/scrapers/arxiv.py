"""arXiv scraper supporting two modes:

- RSS (default, today):  https://rss.arxiv.org/rss/<category>
  Contains papers announced today. Empty on weekends/holidays.

- API (historical):  https://export.arxiv.org/api/query
  Used when --date or --lookback-days > 1 is specified.
  Queries by submittedDate range so any past date works.
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

import feedparser
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import Paper

log = logging.getLogger(__name__)

RSS_BASE = "https://rss.arxiv.org/rss"
API_BASE = "https://export.arxiv.org/api/query"

_ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,6})(?:v\d+)?\b")
_OLD_ARXIV_ID_RE = re.compile(r"\b([a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?\b")
ATOM = "{http://www.w3.org/2005/Atom}"


# ── shared helpers ────────────────────────────────────────────────────────────

def _extract_arxiv_id(text: str) -> str:
    m = _ARXIV_ID_RE.search(text)
    if m:
        return m.group(1)
    m = _OLD_ARXIV_ID_RE.search(text)
    return m.group(1) if m else ""


# ── RSS path (today) ──────────────────────────────────────────────────────────

@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=2, min=2, max=16))
def _fetch_rss(url: str) -> str:
    with httpx.Client(timeout=30, follow_redirects=True) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def _is_cross_listed(entry) -> bool:
    return entry.get("arxiv_announce_type", "new") != "new"


def _rss_entry_to_paper(entry) -> Paper | None:
    arxiv_id = _extract_arxiv_id(entry.get("id") or entry.get("link") or "")
    if not arxiv_id:
        return None
    authors = []
    for a in entry.get("authors", []):
        name = a.get("name") if isinstance(a, dict) else str(a)
        if name:
            authors.append(name)
    cats = [t.get("term", "") for t in entry.get("tags", [])]
    published = ""
    if entry.get("published"):
        try:
            published = parsedate_to_datetime(entry["published"]).date().isoformat()
        except Exception:
            published = entry["published"]
    return Paper(
        source="arxiv",
        paper_id=arxiv_id,
        title=" ".join((entry.get("title") or "").split()),
        authors=authors,
        abstract=" ".join((entry.get("summary") or "").split()),
        url=f"https://arxiv.org/abs/{arxiv_id}",
        categories=cats,
        published=published,
    )


def fetch_rss(category: str, *, include_cross_listed: bool = False, max_results: int = 80) -> list[Paper]:
    try:
        xml = _fetch_rss(f"{RSS_BASE}/{category}")
    except Exception as e:
        log.warning("arXiv RSS failed for %s: %s", category, e)
        return []
    out: list[Paper] = []
    for entry in feedparser.parse(xml).entries:
        if not include_cross_listed and _is_cross_listed(entry):
            continue
        p = _rss_entry_to_paper(entry)
        if p:
            out.append(p)
        if len(out) >= max_results:
            break
    log.info("arxiv RSS %s: %d papers", category, len(out))
    return out


# ── API path (historical) ─────────────────────────────────────────────────────

@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=2, min=2, max=16))
def _fetch_api(params: dict) -> str:
    with httpx.Client(timeout=40, follow_redirects=True) as c:
        r = c.get(API_BASE, params=params)
        r.raise_for_status()
        return r.text


def _date_window(for_date: date) -> tuple[str, str]:
    """Return the submittedDate window for papers announced on `for_date`.

    arXiv announces papers submitted the previous business day. We use a
    ±1 day window around for_date to be tolerant of timezone drift, then
    rely on arXiv's own primary-category filtering.
    """
    start = datetime(for_date.year, for_date.month, for_date.day, 0, 0, tzinfo=timezone.utc) - timedelta(days=2)
    end   = datetime(for_date.year, for_date.month, for_date.day, 23, 59, tzinfo=timezone.utc)
    fmt = "%Y%m%d%H%M"
    return start.strftime(fmt), end.strftime(fmt)


def _api_entry_to_paper(entry: ET.Element) -> Paper | None:
    arxiv_url = (entry.findtext(f"{ATOM}id") or "").strip()
    arxiv_id = _extract_arxiv_id(arxiv_url)
    if not arxiv_id:
        return None
    title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
    abstract = " ".join((entry.findtext(f"{ATOM}summary") or "").split())
    published = (entry.findtext(f"{ATOM}published") or "")[:10]
    authors = [
        (a.findtext(f"{ATOM}name") or "").strip()
        for a in entry.findall(f"{ATOM}author")
    ]
    cats = [c.attrib.get("term", "") for c in entry.findall("{http://arxiv.org/schemas/atom}category")]
    primary_el = entry.find("{http://arxiv.org/schemas/atom}primary_category")
    primary = primary_el.attrib.get("term", "") if primary_el is not None else ""
    return Paper(
        source="arxiv",
        paper_id=arxiv_id,
        title=title,
        authors=authors,
        abstract=abstract,
        url=f"https://arxiv.org/abs/{arxiv_id}",
        categories=cats,
        published=published,
    ), primary


def fetch_api(
    category: str,
    for_date: date,
    *,
    include_cross_listed: bool = False,
    max_results: int = 80,
) -> list[Paper]:
    start, end = _date_window(for_date)
    query = f"cat:{category} AND submittedDate:[{start} TO {end}]"
    all_papers: list[Paper] = []
    step = 50
    for offset in range(0, max_results, step):
        params = {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": offset,
            "max_results": min(step, max_results - offset),
        }
        try:
            xml = _fetch_api(params)
        except Exception as e:
            log.warning("arXiv API failed for %s offset %d: %s", category, offset, e)
            break
        root = ET.fromstring(xml)
        entries = root.findall(f"{ATOM}entry")
        if not entries:
            break
        for entry in entries:
            result = _api_entry_to_paper(entry)
            if result is None:
                continue
            paper, primary = result
            if not include_cross_listed and primary != category:
                continue
            all_papers.append(paper)
        if len(entries) < step:
            break
        time.sleep(3)   # arXiv API rate limit: 3 req/sec max
    log.info("arxiv API %s for %s: %d papers", category, for_date, len(all_papers))
    return all_papers


# ── public interface ──────────────────────────────────────────────────────────

def fetch_all(cfg: dict, for_date: date | None = None) -> list[Paper]:
    """Fetch all configured categories.

    If for_date is None or today, use RSS (fast, designed for daily use).
    If for_date is a past date, use the search API.
    """
    today = date.today()
    use_api = for_date is not None and for_date != today

    if use_api:
        log.info("using arXiv API for historical date %s", for_date)
    else:
        log.info("using arXiv RSS for today's announcements")

    papers: list[Paper] = []
    for cat in cfg.get("categories", []):
        if use_api:
            papers.extend(
                fetch_api(
                    cat,
                    for_date,
                    include_cross_listed=cfg.get("include_cross_listed", False),
                    max_results=cfg.get("max_per_category", 80),
                )
            )
        else:
            papers.extend(
                fetch_rss(
                    cat,
                    include_cross_listed=cfg.get("include_cross_listed", False),
                    max_results=cfg.get("max_per_category", 80),
                )
            )
    return papers
