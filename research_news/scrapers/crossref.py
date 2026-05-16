"""Generic journal scraper using Crossref for issue TOCs and Semantic Scholar
for abstracts when Crossref doesn't provide one.

This works for any DOI-registered journal (AoS, JASA, JRSSB, Biometrika, ...)
without writing a per-publisher HTML parser. Quarterly journals will have
one "issue" per quarter; we fetch the most recent issue by default.

Output: list[Paper] with source="crossref", paper_id=DOI.
"""
from __future__ import annotations

import logging
import re
import time
from collections import defaultdict

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import Paper

log = logging.getLogger(__name__)

CROSSREF_BASE = "https://api.crossref.org"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
UA = {"User-Agent": "Mozilla/5.0 (research-news/0.1; mailto:noreply@example.com)"}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=15))
def _get_json(url: str, params: dict | None = None,
              timeout: float = 30) -> dict:
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA) as c:
        r = c.get(url, params=params)
        r.raise_for_status()
        return r.json()


def _strip_jats(s: str) -> str:
    """Crossref abstracts are wrapped in JATS XML, e.g.
    "<jats:p>...</jats:p>". Strip tags, keep text."""
    if not s:
        return ""
    # Drop common JATS tags
    s = re.sub(r"</?jats:[^>]+>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _item_to_paper(item: dict, journal_name: str) -> Paper | None:
    doi = item.get("DOI")
    if not doi:
        return None
    title_list = item.get("title") or []
    title = re.sub(r"\s+", " ", (title_list[0] if title_list else "").strip())
    if not title:
        return None
    authors_raw = item.get("author") or []
    authors = []
    for a in authors_raw:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        name = " ".join(x for x in [given, family] if x) or a.get("name", "")
        if name:
            authors.append(name)
    issued = item.get("issued", {}).get("date-parts", [[]])
    if issued and issued[0]:
        date_parts = issued[0]
        published = "-".join(f"{p:02d}" if isinstance(p, int) and i > 0 else str(p)
                             for i, p in enumerate(date_parts))
    else:
        published = None
    volume = item.get("volume")
    issue = item.get("issue") or item.get("journal-issue", {}).get("issue")
    page = item.get("page")
    cats = []
    if volume:
        cats.append(f"vol {volume}")
    if issue:
        cats.append(f"issue {issue}")
    if page:
        cats.append(f"pp {page}")
    abstract = _strip_jats(item.get("abstract") or "")
    return Paper(
        source="crossref",
        paper_id=doi,
        title=title,
        authors=authors,
        abstract=abstract,
        url=f"https://doi.org/{doi}",
        categories=cats,
        published=published,
        venue=journal_name,
    )


def _latest_issue_key(items: list[dict]) -> tuple | None:
    """Pick the most recent (volume, issue) tuple from a list of works.

    Numeric where possible. Returns None if no items have both volume + issue.
    """
    def key_for(it: dict):
        vol = it.get("volume")
        iss = it.get("issue") or it.get("journal-issue", {}).get("issue")
        try:
            vol_n = int(re.sub(r"[^0-9]", "", vol)) if vol else None
            iss_n = int(re.sub(r"[^0-9]", "", iss)) if iss else None
        except ValueError:
            return None
        if vol_n is None or iss_n is None:
            return None
        return (vol_n, iss_n)

    keys = [k for k in (key_for(it) for it in items) if k is not None]
    if not keys:
        return None
    return max(keys)


def fetch_latest_issue(issn: str, journal_name: str, *,
                       rows: int = 60,
                       fill_abstract: bool = True) -> list[Paper]:
    """Fetch the most recent issue's worth of articles for a journal.

    We pull the latest 60 works for the ISSN, identify the most-recent
    (volume, issue) tuple, then return only papers in that issue.
    For journals that don't expose issue numbers (rolling pub like JMLR
    via Crossref), we fall back to the most recent `rows` items capped at 15.
    """
    log.info("Crossref: fetching latest works for %s (ISSN %s)", journal_name, issn)
    data = _get_json(
        f"{CROSSREF_BASE}/journals/{issn}/works",
        params={
            "filter": "type:journal-article",
            "sort": "published",
            "order": "desc",
            "rows": rows,
        },
    )
    items = data.get("message", {}).get("items", [])
    log.info("  got %d works", len(items))
    if not items:
        return []

    target = _latest_issue_key(items)
    if target is not None:
        vol_n, iss_n = target
        log.info("  latest issue key: vol %d issue %d", vol_n, iss_n)
        keep = []
        for it in items:
            v = it.get("volume")
            i = it.get("issue") or it.get("journal-issue", {}).get("issue")
            try:
                if v and i and int(re.sub(r"[^0-9]", "", v)) == vol_n \
                   and int(re.sub(r"[^0-9]", "", i)) == iss_n:
                    keep.append(it)
            except ValueError:
                continue
    else:
        log.info("  no (vol, issue) keys found, taking 15 most recent")
        keep = items[:15]

    papers: list[Paper] = []
    for it in keep:
        p = _item_to_paper(it, journal_name)
        if p:
            papers.append(p)
    log.info("  %d papers in latest issue", len(papers))

    if fill_abstract:
        _fill_missing_abstracts(papers)
    return papers


@retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=2, min=1, max=8))
def _s2_abstract(doi: str) -> str:
    data = _get_json(
        f"{S2_BASE}/paper/DOI:{doi}",
        params={"fields": "abstract"},
        timeout=20,
    )
    return (data.get("abstract") or "").strip()


# Meta tags that publishers commonly use to expose abstracts on landing pages.
# Order = preference; longer / more structured wins.
_META_NAMES_ABSTRACT = (
    "citation_abstract",
    "DC.Description",
    "dc.Description",
    "DC.description",
    "dc.description",
    "description",
)
_META_PROPS_ABSTRACT = ("og:description",)


def _extract_abstract_from_html(html: str) -> str:
    """Try meta tags first, then common abstract block selectors.

    Works for Oxford Academic (JRSSB, Biometrika), Taylor & Francis (JASA),
    Project Euclid (AoS), and most publishers that follow scholarly meta
    conventions. Returns "" if nothing usable found."""
    if not html:
        return ""
    soup = BeautifulSoup(html, "lxml")

    candidates: list[str] = []
    for name in _META_NAMES_ABSTRACT:
        for tag in soup.find_all("meta", attrs={"name": name}):
            v = (tag.get("content") or "").strip()
            if v:
                candidates.append(v)
    for prop in _META_PROPS_ABSTRACT:
        for tag in soup.find_all("meta", attrs={"property": prop}):
            v = (tag.get("content") or "").strip()
            if v:
                candidates.append(v)

    # Structural selectors used by the big publishers.
    for sel in [
        {"name": "section", "attrs": {"class_": "abstract"}},
        {"name": "div", "attrs": {"class_": "abstractSection"}},   # T&F
        {"name": "div", "attrs": {"class_": "abstract"}},
        {"name": "div", "attrs": {"id": "abstract"}},
        {"name": "div", "attrs": {"class_": "hlFld-Abstract"}},    # T&F variant
        {"name": "p",   "attrs": {"class_": "abstract"}},
    ]:
        for el in soup.find_all(sel["name"], **sel["attrs"]):
            t = re.sub(r"\s+", " ", el.get_text(" ")).strip()
            # Strip a leading "Abstract" label
            t = re.sub(r"^abstract[:\s]*", "", t, flags=re.I).strip()
            if t:
                candidates.append(t)

    # Keep candidates that look like real abstracts: long enough, and not
    # site-wide marketing copy ("description" sometimes returns a site tagline).
    good = [c for c in candidates if len(c) >= 200]
    if good:
        return max(good, key=len)
    # Last resort: longest candidate regardless of length floor.
    return max(candidates, key=len) if candidates else ""


@retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=2, min=1, max=8))
def _get_html(url: str, timeout: float = 25) -> str:
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def _landing_page_abstract(doi: str) -> str:
    """Follow the DOI to the publisher landing page and parse its abstract."""
    try:
        html = _get_html(f"https://doi.org/{doi}")
    except Exception as e:
        log.debug("landing-page fetch failed for %s: %s", doi, e)
        return ""
    return _extract_abstract_from_html(html)


def _fill_missing_abstracts(papers: list[Paper], sleep_s: float = 1.2) -> None:
    """Three-tier abstract backfill: Semantic Scholar → publisher landing page.

    (Crossref's own abstract was already used in _item_to_paper.)
    """
    missing = [p for p in papers if not p.abstract]
    if not missing:
        return

    # Tier 2: Semantic Scholar by DOI
    log.info("backfill T2: Semantic Scholar for %d papers", len(missing))
    n_s2 = 0
    for p in missing:
        try:
            abs_text = _s2_abstract(p.paper_id)
            if abs_text:
                p.abstract = abs_text
                n_s2 += 1
        except Exception as e:
            log.debug("S2 abstract miss for %s: %s", p.paper_id, e)
        time.sleep(sleep_s)
    log.info("  T2 filled %d/%d", n_s2, len(missing))

    # Tier 3: publisher landing page (DOI redirect). Require >=150 chars to
    # filter out site-wide descriptions / cookie-wall copy that look like
    # abstracts but are not.
    still_missing = [p for p in papers if not p.abstract]
    if still_missing:
        log.info("backfill T3: publisher landing pages for %d papers",
                 len(still_missing))
        n_lp = 0
        for p in still_missing:
            abs_text = _landing_page_abstract(p.paper_id)
            if abs_text and len(abs_text) >= 150:
                p.abstract = abs_text
                n_lp += 1
            time.sleep(sleep_s)
        log.info("  T3 filled %d/%d", n_lp, len(still_missing))

    final_missing = sum(1 for p in papers if not p.abstract)
    log.info("after all backfills: %d/%d still missing abstract",
             final_missing, len(papers))


# Built-in ISSN registry for the journals we usually want. Override via
# config/journals.yaml.
KNOWN_JOURNALS: dict[str, tuple[str, str]] = {
    # name: (issn, short_label)
    "Annals of Statistics":         ("0090-5364", "AoS"),
    "Journal of the American Statistical Association": ("0162-1459", "JASA"),
    "Journal of the Royal Statistical Society Series B": ("1369-7412", "JRSSB"),
    "Biometrika":                   ("0006-3444", "Biometrika"),
}
