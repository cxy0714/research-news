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
OPENALEX_BASE = "https://api.openalex.org"
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


def _reconstruct_inverted_index(idx: dict | None) -> str:
    """OpenAlex stores abstracts as {word: [positions...]}. Reconstruct."""
    if not idx:
        return ""
    try:
        n = max(p for positions in idx.values() for p in positions) + 1
    except ValueError:
        return ""
    words = [""] * n
    for w, positions in idx.items():
        for p in positions:
            if 0 <= p < n:
                words[p] = w
    return " ".join(w for w in words if w).strip()


@retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=2, min=1, max=8))
def _openalex_abstract(doi: str) -> str:
    """Look up a work in OpenAlex by DOI and reconstruct its abstract.

    OpenAlex covers most journal articles broadly, is free with no key, and
    returns 200 even for publishers that 403 us (Oxford / T&F Cloudflare),
    so it's the right Tier-3 fallback when S2 misses.
    """
    data = _get_json(
        f"{OPENALEX_BASE}/works/doi:{doi}",
        params={"select": "abstract_inverted_index"},
        timeout=20,
    )
    return _reconstruct_inverted_index(data.get("abstract_inverted_index"))


# ── T4: arxiv title search ────────────────────────────────────────────────────
# Stats methodology papers almost always have an arxiv preprint with the same
# or near-identical title. When the publisher / OpenAlex don't have an
# abstract (e.g. very recent JRSSB issue not yet indexed), look up the
# preprint on arxiv and use its summary.

_ARXIV_ATOM_NS = "{http://www.w3.org/2005/Atom}"


def _normalize_title(s: str) -> str:
    s = re.sub(r"[^\w\s]+", " ", (s or "").lower())
    return re.sub(r"\s+", " ", s).strip()


def _title_match(a: str, b: str, *, min_overlap: float = 0.82) -> bool:
    """True if a and b refer to the same paper. Cheap heuristic: token-set
    Jaccard >= min_overlap, after normalization."""
    ta = set(_normalize_title(a).split())
    tb = set(_normalize_title(b).split())
    if not ta or not tb:
        return False
    inter = len(ta & tb)
    smaller = min(len(ta), len(tb))
    return inter / smaller >= min_overlap


@retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=2, min=1, max=6))
def _arxiv_search_abstract(title: str) -> str:
    """Search arxiv for a paper by title; return its abstract if a high-
    confidence match is found."""
    from xml.etree import ElementTree as ET

    norm = _normalize_title(title)
    if len(norm) < 20:   # too short to disambiguate; skip
        return ""
    # arxiv `ti:` filter accepts quoted phrases; remove punctuation that
    # confuses the query.
    query = f'ti:"{norm}"'
    with httpx.Client(timeout=25, follow_redirects=True, headers=UA) as c:
        r = c.get("https://export.arxiv.org/api/query",
                  params={"search_query": query,
                          "max_results": 3,
                          "sortBy": "relevance"})
        r.raise_for_status()
        xml = r.text
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return ""
    for entry in root.findall(f"{_ARXIV_ATOM_NS}entry"):
        cand_title = " ".join(
            (entry.findtext(f"{_ARXIV_ATOM_NS}title") or "").split()
        )
        if _title_match(title, cand_title):
            summary = " ".join(
                (entry.findtext(f"{_ARXIV_ATOM_NS}summary") or "").split()
            )
            return summary.strip()
    return ""


_META_NAMES_ABSTRACT = (
    "citation_abstract",
    "DC.Description",
    "dc.Description",
    "DC.description",
    "dc.description",
    "description",
)
_META_PROPS_ABSTRACT = ("og:description",)

# Selectors used by the major scholarly publishers, in roughly preference
# order. Class matching is partial (contains) where the underlying value
# combines multiple class names like "abstractSection abstractInFull".
_ABSTRACT_SELECTORS: list[tuple[str, dict]] = [
    # Oxford Academic (JRSSB, Biometrika)
    ("section", {"class": re.compile(r"\babstract\b", re.I)}),
    ("div",     {"class": re.compile(r"abstract-content|article-abstract", re.I)}),
    # Taylor & Francis (JASA, JCGS)
    ("div",     {"class": re.compile(r"abstractSection|hlFld-Abstract", re.I)}),
    # Project Euclid (AoS, Statistical Science, EJS)
    ("div",     {"class": re.compile(r"article-abstract|publication-abstract", re.I)}),
    ("div",     {"id": "abstract"}),
    # Wiley / generic
    ("div",     {"class": re.compile(r"^abstract$|article-section__content", re.I)}),
    ("p",       {"class": re.compile(r"\babstract\b", re.I)}),
]


def _extract_abstract_from_html(html: str) -> tuple[str, list[str]]:
    """Returns (best_abstract, diagnostic_notes).

    Notes record which selectors hit and their lengths, so we can see what's
    wrong when nothing comes back.
    """
    notes: list[str] = []
    if not html:
        return "", ["empty html"]
    soup = BeautifulSoup(html, "lxml")

    candidates: list[str] = []
    for name in _META_NAMES_ABSTRACT:
        for tag in soup.find_all("meta", attrs={"name": name}):
            v = (tag.get("content") or "").strip()
            if v:
                candidates.append(v)
                notes.append(f"meta[name={name}] len={len(v)}")
    for prop in _META_PROPS_ABSTRACT:
        for tag in soup.find_all("meta", attrs={"property": prop}):
            v = (tag.get("content") or "").strip()
            if v:
                candidates.append(v)
                notes.append(f"meta[property={prop}] len={len(v)}")

    for tag_name, attrs in _ABSTRACT_SELECTORS:
        for el in soup.find_all(tag_name, attrs=attrs):
            t = re.sub(r"\s+", " ", el.get_text(" ")).strip()
            t = re.sub(r"^abstract[:\s]*", "", t, flags=re.I).strip()
            if t:
                candidates.append(t)
                notes.append(f"{tag_name}{attrs} len={len(t)}")

    # Last-resort heuristic: any element with id/class containing "abstract"
    if not candidates:
        for el in soup.find_all(attrs={"class": re.compile(r"abstract", re.I)}):
            t = re.sub(r"\s+", " ", el.get_text(" ")).strip()
            if 100 < len(t) < 5000:
                candidates.append(t)
                notes.append(f"heuristic class~=abstract len={len(t)}")

    if not candidates:
        return "", notes or ["no candidates found"]

    good = [c for c in candidates if len(c) >= 200]
    pick = max(good, key=len) if good else max(candidates, key=len)
    return pick, notes


@retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=2, min=1, max=8))
def _get_html(url: str, timeout: float = 25) -> str:
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def _landing_page_abstract(doi: str) -> tuple[str, str]:
    """Returns (abstract, diagnostic) — the diagnostic explains what happened
    when the abstract is empty."""
    try:
        html = _get_html(f"https://doi.org/{doi}")
    except Exception as e:
        return "", f"HTTP failed: {type(e).__name__}: {str(e)[:120]}"
    if not html:
        return "", "HTTP ok but empty body"
    abs_text, notes = _extract_abstract_from_html(html)
    if abs_text:
        return abs_text, f"ok via {notes[0] if notes else 'unknown'}"
    return "", f"HTTP ok ({len(html)} chars), no selector hit. tried: {notes[:3]}"


def _fill_missing_abstracts(papers: list[Paper], sleep_s: float = 1.2) -> None:
    """Four-tier abstract backfill:
      T1: Crossref's own JATS abstract (already used in _item_to_paper)
      T2: Semantic Scholar by DOI
      T3: OpenAlex by DOI (works for publishers that 403 us — Oxford / T&F)
      T4: publisher landing page (last resort, only works for non-Cloudflare sites)
    """
    missing = [p for p in papers if not p.abstract]
    if not missing:
        return

    # Tier 2: Semantic Scholar
    log.info("backfill T2 (S2): %d papers", len(missing))
    n_s2 = 0
    for p in missing:
        try:
            abs_text = _s2_abstract(p.paper_id)
            if abs_text:
                p.abstract = abs_text
                n_s2 += 1
        except Exception as e:
            log.debug("S2 miss for %s: %s", p.paper_id, e)
        time.sleep(sleep_s)
    log.info("  T2 filled %d/%d", n_s2, len(missing))

    # Tier 3: OpenAlex
    still_missing = [p for p in papers if not p.abstract]
    if still_missing:
        log.info("backfill T3 (OpenAlex): %d papers", len(still_missing))
        n_oa = 0
        for p in still_missing:
            try:
                abs_text = _openalex_abstract(p.paper_id)
                if abs_text and len(abs_text) >= 150:
                    p.abstract = abs_text
                    n_oa += 1
            except Exception as e:
                log.debug("OpenAlex miss for %s: %s", p.paper_id, e)
            time.sleep(sleep_s)
        log.info("  T3 filled %d/%d", n_oa, len(still_missing))

    # Tier 4: arxiv title search. Stats methodology papers almost always have
    # an arxiv preprint with the same/near-identical title; we look that up
    # and use its summary. Covers brand-new JRSSB / JASA issues that OpenAlex
    # hasn't indexed yet. Publisher landing pages (the previous T4) are
    # uniformly Cloudflare-blocked for Oxford / T&F so we don't bother.
    still_missing = [p for p in papers if not p.abstract]
    if still_missing:
        log.info("backfill T4 (arxiv title search): %d papers", len(still_missing))
        n_ax = 0
        for p in still_missing:
            try:
                abs_text = _arxiv_search_abstract(p.title)
                if abs_text and len(abs_text) >= 150:
                    p.abstract = abs_text
                    n_ax += 1
            except Exception as e:
                log.debug("arxiv search miss for %s: %s", p.paper_id, e)
            time.sleep(3.5)   # arxiv API politeness: 3s minimum
        log.info("  T4 filled %d/%d", n_ax, len(still_missing))

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


# ── diagnostic CLI ────────────────────────────────────────────────────────────
# Run: python -m research_news.scrapers.crossref <DOI> [<DOI> ...]
# Prints: final URL after DOI redirect, HTML size, which selectors matched
# and how long the matched abstract was. Use this when T3 misses an entire
# publisher — paste the output back so we know which selector to add.

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    if len(sys.argv) < 2:
        print("usage: python -m research_news.scrapers.crossref <DOI> [<DOI> ...]")
        sys.exit(2)
    for doi in sys.argv[1:]:
        print(f"\n=== {doi} ===")
        # First get the title via Crossref for arxiv search
        title = ""
        try:
            data = _get_json(f"{CROSSREF_BASE}/works/{doi}")
            title_list = data.get("message", {}).get("title") or []
            title = title_list[0] if title_list else ""
            if title:
                print(f"title: {title[:100]}")
        except Exception as e:
            print(f"Crossref title fetch: ERROR {type(e).__name__}: {e}")

        # T2: Semantic Scholar
        try:
            s2 = _s2_abstract(doi)
            print(f"T2 S2: {len(s2)} chars" + (f"  | {s2[:140]}..." if s2 else " (empty)"))
        except Exception as e:
            print(f"T2 S2: ERROR {type(e).__name__}: {e}")

        # T3: OpenAlex
        try:
            oa = _openalex_abstract(doi)
            print(f"T3 OpenAlex: {len(oa)} chars" + (f"  | {oa[:140]}..." if oa else " (empty)"))
        except Exception as e:
            print(f"T3 OpenAlex: ERROR {type(e).__name__}: {e}")

        # T4: arxiv title search
        if title:
            try:
                ax = _arxiv_search_abstract(title)
                print(f"T4 arxiv: {len(ax)} chars" + (f"  | {ax[:140]}..." if ax else " (no match)"))
            except Exception as e:
                print(f"T4 arxiv: ERROR {type(e).__name__}: {e}")
