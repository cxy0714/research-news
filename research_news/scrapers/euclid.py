"""Project Euclid issue-TOC scraper — authoritative article list for the
completeness checker.

Project Euclid hosts most of the theory journals we track (Annals of Statistics,
Annals of Probability, Annals of Applied Statistics, EJS, Bernoulli, Statistical
Science) and — unlike Oxford / T&F — serves plain HTML without a Cloudflare
challenge, so a simple GET + parse works.

Issue URL shape:
    https://projecteuclid.org/journals/<slug>/volume-<vol>/issue-<iss>

Each article on the page links to its landing page; the DOI is embedded in that
href (``.../10.1214/25-AOS2569/full``). We pull (title, DOI) per article. The
DOM class names drift over time, so parsing is deliberately structure-light
(DOI-in-href first, visible-text DOIs as a fallback); if Euclid changes layout,
widen the selectors here.
"""
from __future__ import annotations

import logging
import re

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

log = logging.getLogger(__name__)

BASE = "https://projecteuclid.org"
UA = {"User-Agent": "Mozilla/5.0 (research-news/0.1; mailto:noreply@example.com)"}

# ISSN → Project Euclid journal slug. Only journals actually hosted on Euclid.
ISSN_TO_SLUG: dict[str, str] = {
    "0090-5364": "annals-of-statistics",
    "0091-1798": "annals-of-probability",
    "1932-6157": "annals-of-applied-statistics",
    "1935-7524": "electronic-journal-of-statistics",
    "1350-7265": "bernoulli",
    "0883-4237": "statistical-science",
}

_DOI_IN_HREF_RE = re.compile(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+?)(?:/full|/abstract)?/?$", re.I)
_DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.I)


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=15))
def _get_html(url: str, timeout: float = 30) -> str:
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def issue_url(slug: str, vol: int, iss: int | None) -> str:
    if iss is None:
        return f"{BASE}/journals/{slug}/volume-{vol}"
    return f"{BASE}/journals/{slug}/volume-{vol}/issue-{iss}"


def _norm_doi(d: str) -> str:
    return d.strip().lower().rstrip(" .,;)")


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def parse_issue_html(html: str) -> list[tuple[str, str]]:
    """Return [(title, doi), ...] from a Project Euclid issue page.

    Returns plain tuples (the completeness module wraps them in its TocEntry);
    keeping this dependency-free makes it unit-testable on a saved HTML fixture.
    """
    soup = BeautifulSoup(html, "lxml")
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        m = _DOI_IN_HREF_RE.search(href) or _DOI_RE.search(href)
        if not m:
            continue
        doi = _norm_doi(m.group(1) if m.re is _DOI_IN_HREF_RE else m.group(0))
        title = _clean(a.get_text(" "))
        # Article-title anchors carry real titles; skip "PDF"/"Full"/citation links.
        if len(title) < 15 or title.lower() in {"full", "pdf", "abstract", "full text"}:
            continue
        if doi in seen:
            continue
        seen.add(doi)
        out.append((title, doi))
    return out


def fetch_issue_toc(issn: str, journal_name: str, vol: int, iss: int | None = None):
    """Authoritative TOC for a Euclid-hosted issue, as completeness.TocEntry list.
    Empty list (with a warning) if the journal isn't on Euclid or parsing fails."""
    from ..completeness import TocEntry

    slug = ISSN_TO_SLUG.get(issn)
    if not slug:
        log.warning("%s (ISSN %s) is not a Project Euclid journal — "
                    "use --toc-pdf instead", journal_name, issn)
        return []
    url = issue_url(slug, vol, iss)
    log.info("Euclid TOC: %s", url)
    try:
        html = _get_html(url)
    except Exception as e:  # noqa: BLE001
        log.error("Euclid fetch failed for %s: %s", url, e)
        return []
    pairs = parse_issue_html(html)
    log.info("  parsed %d article(s) from Euclid TOC", len(pairs))
    return [TocEntry(title, doi, f"https://doi.org/{doi}") for title, doi in pairs]
