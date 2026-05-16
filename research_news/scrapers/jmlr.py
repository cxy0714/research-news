"""JMLR scraper.

JMLR (Journal of Machine Learning Research) publishes papers continuously
within a single yearly volume. The volume index page

    https://www.jmlr.org/papers/v<N>/

lists every accepted paper in that volume in reverse-chronological order
(most recent first). Each entry is a <dl><dt>Title</dt><dd>...</dd></dl>
block linking to an abstract page like

    https://www.jmlr.org/papers/v<N>/<paper-id>.html

We:
  1. Resolve the latest volume (defaults to current_year - 1999; can override).
  2. Parse the first `n` <dt>/<dd> entries.
  3. For each, fetch the abstract page and extract <h3>Abstract</h3>'s paragraph.

JMLR HTML is hand-crafted and varies slightly across years — if the abstract
selector misses, we fall back to "biggest paragraph on the page".
"""
from __future__ import annotations

import logging
import re
import time
from datetime import date

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import Paper

log = logging.getLogger(__name__)

BASE = "https://www.jmlr.org"
UA = {"User-Agent": "research-news-jmlr/0.1"}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=10))
def _get(url: str) -> str:
    with httpx.Client(timeout=30, follow_redirects=True, headers=UA) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def _current_volume() -> int:
    """JMLR vol 1 = 2000, vol 2 = 2001, ..., vol N = 1999 + N."""
    return date.today().year - 1999


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def _parse_index(html: str, volume: int) -> list[Paper]:
    """Pull (title, authors, abs_url) from a JMLR volume index page."""
    soup = BeautifulSoup(html, "lxml")
    out: list[Paper] = []
    seen: set[str] = set()
    for dl in soup.find_all("dl"):
        dt = dl.find("dt")
        dd = dl.find("dd")
        if not dt or not dd:
            continue
        title = _clean(dt.get_text())
        if not title:
            continue
        # abs link (preferred) — otherwise first paper link
        abs_link = None
        for a in dd.find_all("a", href=True):
            href = a["href"]
            txt = (a.get_text() or "").strip().lower()
            if txt == "abs" or href.endswith(".html"):
                abs_link = href
                break
        if not abs_link:
            continue
        if abs_link.startswith("/"):
            abs_url = BASE + abs_link
        elif abs_link.startswith("http"):
            abs_url = abs_link
        else:
            abs_url = f"{BASE}/papers/v{volume}/{abs_link}"
        # paper id = filename stem
        m = re.search(r"/([^/]+?)\.html?$", abs_url)
        paper_id = m.group(1) if m else abs_url
        paper_id = f"jmlr:v{volume}/{paper_id}"
        if paper_id in seen:
            continue
        seen.add(paper_id)
        # authors: first text node of <dd> before any <a>
        # heuristic: take the first comma-list before a semicolon or "[" or first <a>
        dd_text = _clean(dd.get_text(" "))
        authors_part = re.split(r";|\[", dd_text, maxsplit=1)[0]
        authors = [a.strip() for a in authors_part.split(",") if a.strip()]
        out.append(
            Paper(
                source="jmlr",
                paper_id=paper_id,
                title=title,
                authors=authors,
                abstract="",   # filled by _enrich_abstract
                url=abs_url,
                categories=[f"JMLR v{volume}"],
                published=None,
                venue="JMLR",
            )
        )
    return out


def _extract_abstract(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    # 1) <h3>Abstract</h3> → next <p>
    for tag in soup.find_all(["h2", "h3", "h4"]):
        if _clean(tag.get_text()).lower().startswith("abstract"):
            p = tag.find_next("p")
            if p:
                return _clean(p.get_text(" "))
    # 2) "Abstract" plain text → next <p>
    for el in soup.find_all(string=re.compile(r"^\s*Abstract\s*$", re.I)):
        nxt = el.find_next("p") if hasattr(el, "find_next") else None
        if nxt:
            return _clean(nxt.get_text(" "))
    # 3) biggest <p> on the page (last resort)
    paras = [(_clean(p.get_text(" ")), p) for p in soup.find_all("p")]
    paras = [t for t, _ in paras if len(t) > 100]
    if paras:
        return max(paras, key=len)
    return ""


def _enrich_abstract(paper: Paper) -> None:
    try:
        html = _get(paper.url)
    except Exception as e:
        log.warning("abstract fetch failed for %s: %s", paper.paper_id, e)
        return
    abs_text = _extract_abstract(html)
    if abs_text:
        paper.abstract = abs_text
    else:
        log.warning("no abstract found on %s", paper.url)


def fetch_latest(n: int = 10, volume: int | None = None,
                 *, sleep_s: float = 1.0) -> list[Paper]:
    """Return the `n` most recent JMLR papers from the given volume.

    `volume=None` auto-resolves to the current year's volume.
    """
    vol = volume or _current_volume()
    url = f"{BASE}/papers/v{vol}/"
    log.info("fetching JMLR volume index: %s", url)
    try:
        html = _get(url)
    except Exception as e:
        log.error("JMLR volume %d not reachable (%s); trying volume %d", vol, e, vol - 1)
        vol -= 1
        html = _get(f"{BASE}/papers/v{vol}/")
    papers = _parse_index(html, vol)
    log.info("JMLR v%d index: %d papers found, taking top %d", vol, len(papers), n)
    papers = papers[:n]
    for p in papers:
        _enrich_abstract(p)
        if sleep_s:
            time.sleep(sleep_s)
    log.info("JMLR fetch complete: %d papers with abstracts (%d non-empty)",
             len(papers), sum(1 for p in papers if p.abstract))
    return papers
