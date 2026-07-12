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
import re

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


def _abstract_from_inverted_index(inv: dict | None) -> str:
    """Reconstruct plain-text abstract from OpenAlex's inverted-index format."""
    if not inv:
        return ""
    positions: list[tuple[int, str]] = []
    for word, idxs in inv.items():
        for i in idxs:
            positions.append((i, word))
    positions.sort()
    return " ".join(w for _, w in positions)


def _arxiv_id_from_work(w: dict) -> str | None:
    """Pull an arXiv id from any location in an OpenAlex work, if present."""
    locs = list(w.get("locations") or [])
    if w.get("primary_location"):
        locs.append(w["primary_location"])
    for loc in locs:
        src = (loc or {}).get("source") or {}
        pdf = (loc or {}).get("pdf_url") or ""
        landing = (loc or {}).get("landing_page_url") or ""
        for field in (src.get("display_name") or "", pdf, landing):
            m = re.search(r"(\d{4}\.\d{4,6})", field or "")
            if m and ("arxiv" in (field or "").lower() or "arxiv" in (src.get("display_name") or "").lower()):
                return m.group(1)
    return None


def search_works_by_title(title: str, *, per_page: int = 8) -> list[dict]:
    """Search OpenAlex for a title. Returns list of dicts:
    {title, authors[list], abstract, doi, arxiv_id, url}. Fails open ([])."""
    try:
        data = _get_json(
            f"{OPENALEX_BASE}/works",
            {"search": title, "per-page": per_page,
             "select": "id,doi,title,display_name,authorships,"
                       "abstract_inverted_index,primary_location,locations"},
        )
    except Exception as e:  # noqa: BLE001
        log.warning("OpenAlex title search failed for %r: %s", title[:60], e)
        return []
    out: list[dict] = []
    for w in data.get("results", []):
        t = (w.get("title") or w.get("display_name") or "").strip()
        if not t:
            continue
        authors = [
            (a.get("author") or {}).get("display_name", "")
            for a in (w.get("authorships") or [])
        ]
        doi = _norm_doi(w.get("doi"))
        arxiv_id = _arxiv_id_from_work(w)
        url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else (
            f"https://doi.org/{doi}" if doi else w.get("id", ""))
        out.append({
            "title": t,
            "authors": [a for a in authors if a],
            "abstract": _abstract_from_inverted_index(w.get("abstract_inverted_index")),
            "doi": doi or None,
            "arxiv_id": arxiv_id,
            "url": url,
        })
    return out


def fetch_issue_works(issn: str, vol: int, iss: int | None = None,
                      *, max_pages: int = 6) -> list[tuple[str, str | None]]:
    """All works in a journal issue, as (title, doi) pairs, via cursor paging."""
    filt = f"primary_location.source.issn:{issn},biblio.volume:{vol}"
    if iss is not None:
        filt += f",biblio.issue:{iss}"
    # Drop front/back-matter & TOC entries at the source so they don't show up as
    # "missing" articles (real content is article/review/letter/editorial/…).
    filt += ",type:!paratext"
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
