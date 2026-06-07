"""OpenAlex issue-listing — the universal automatic authoritative source for the
completeness checker.

OpenAlex (api.openalex.org) is free, key-less, not Cloudflare-blocked, and — the
key property here — lets us list *every* work in a given journal issue by
filtering on ISSN + volume + issue. It aggregates from Crossref, MAG, PubMed,
repositories and publisher feeds, so its per-issue list is an independent
cross-check against our Crossref scrape (which only pulled a publication-date
window and can drop the tail of an issue).

Works for any journal by ISSN, so this is the default authoritative source for
all venues; Project Euclid (scrapers/euclid.py) is layered on top as the
publisher-canonical source for the journals it hosts.
"""
from __future__ import annotations

import logging

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

log = logging.getLogger(__name__)

OPENALEX_BASE = "https://api.openalex.org"
UA = {"User-Agent": "research-news/0.1 (mailto:noreply@example.com)"}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=15))
def _get_json(url: str, params: dict, timeout: float = 30) -> dict:
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA) as c:
        r = c.get(url, params=params)
        r.raise_for_status()
        return r.json()


def _norm_doi(d: str | None) -> str:
    d = (d or "").strip().lower()
    if d.startswith("http"):
        d = d.split("doi.org/", 1)[-1]
    return d.rstrip(" .,;)")


def parse_works_json(data: dict) -> list[tuple[str, str | None]]:
    """[(title, doi), ...] from one OpenAlex /works response page. Dependency-free
    so it's unit-testable on a saved JSON sample."""
    out: list[tuple[str, str | None]] = []
    for w in data.get("results", []):
        title = (w.get("title") or w.get("display_name") or "").strip()
        if not title:
            continue
        doi = _norm_doi(w.get("doi"))
        out.append((title, doi or None))
    return out


def fetch_issue_works(issn: str, vol: int, iss: int | None = None,
                      *, max_pages: int = 6) -> list[tuple[str, str | None]]:
    """All works in a journal issue, as (title, doi) pairs, via cursor paging."""
    filt = f"primary_location.source.issn:{issn},biblio.volume:{vol}"
    if iss is not None:
        filt += f",biblio.issue:{iss}"
    out: list[tuple[str, str | None]] = []
    cursor = "*"
    for _ in range(max_pages):
        if not cursor:
            break
        data = _get_json(
            f"{OPENALEX_BASE}/works",
            {"filter": filt, "per-page": 200, "cursor": cursor,
             "select": "id,doi,title,display_name,biblio,type"},
        )
        out.extend(parse_works_json(data))
        cursor = (data.get("meta") or {}).get("next_cursor")
    return out


def fetch_issue_toc(issn: str, journal_name: str, vol: int, iss: int | None = None):
    """Authoritative TOC for an issue as completeness.TocEntry list (empty +
    warning on failure)."""
    from ..completeness import TocEntry

    log.info("OpenAlex issue listing: ISSN %s vol %s issue %s",
             issn, vol, iss if iss is not None else "*")
    try:
        pairs = fetch_issue_works(issn, vol, iss)
    except Exception as e:  # noqa: BLE001
        log.error("OpenAlex issue fetch failed (ISSN %s v%s i%s): %s",
                  issn, vol, iss, e)
        return []
    log.info("  OpenAlex returned %d work(s)", len(pairs))
    return [TocEntry(title, doi, f"https://doi.org/{doi}" if doi else None)
            for title, doi in pairs]
