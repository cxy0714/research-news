"""arXiv daily-new scraper using official RSS feeds.

RSS endpoint: https://rss.arxiv.org/rss/<category>
Each feed contains the papers *announced* today (submitted the prior business
day). On weekends and holidays arXiv does not announce papers, so the feed is
empty — that is expected behaviour.
"""
from __future__ import annotations

import logging
from email.utils import parsedate_to_datetime

import feedparser
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import Paper

log = logging.getLogger(__name__)

RSS_BASE = "https://rss.arxiv.org/rss"


@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=2, min=2, max=16))
def _fetch_rss(url: str) -> str:
    with httpx.Client(timeout=30, follow_redirects=True) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def _arxiv_id(entry) -> str:
    """Extract bare arXiv ID from entry id/link fields."""
    raw = entry.get("id") or entry.get("link") or ""
    # typical: http://arxiv.org/abs/2505.12345v1
    return raw.rstrip("/").rsplit("/", 1)[-1].split("v")[0]


def _is_cross_listed(entry) -> bool:
    """RSS entries have a <arxiv:announce_type> tag for new / cross / rep."""
    announce = entry.get("arxiv_announce_type", "new")
    return announce != "new"


def fetch_category(
    category: str,
    *,
    include_cross_listed: bool = False,
    max_results: int = 80,
) -> list[Paper]:
    url = f"{RSS_BASE}/{category}"
    try:
        xml = _fetch_rss(url)
    except Exception as e:
        log.warning("arXiv RSS fetch failed for %s: %s", category, e)
        return []

    feed = feedparser.parse(xml)
    out: list[Paper] = []
    for entry in feed.entries:
        if not include_cross_listed and _is_cross_listed(entry):
            continue

        arxiv_id = _arxiv_id(entry)
        title = " ".join((entry.get("title") or "").split())
        abstract = " ".join((entry.get("summary") or "").split())
        link = entry.get("link") or f"https://arxiv.org/abs/{arxiv_id}"

        authors: list[str] = []
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

        out.append(
            Paper(
                source="arxiv",
                paper_id=arxiv_id,
                title=title,
                authors=authors,
                abstract=abstract,
                url=link,
                categories=cats,
                published=published,
            )
        )
        if len(out) >= max_results:
            break

    log.info("arxiv %s: %d new papers", category, len(out))
    return out


def fetch_all(cfg: dict) -> list[Paper]:
    papers: list[Paper] = []
    for cat in cfg.get("categories", []):
        papers.extend(
            fetch_category(
                cat,
                include_cross_listed=cfg.get("include_cross_listed", False),
                max_results=cfg.get("max_per_category", 80),
            )
        )
    return papers
