"""Institution green-light: promote papers from top institutions into deep read.

A paper whose author is at a whitelisted institution (config/institutions.yaml,
default US News top-50) is worth a deep read regardless of its relevance score.

Affiliations are sparse in arXiv/Crossref metadata, so we back-fill them from
OpenAlex (free, no key) by arXiv id / DOI at run time. Everything fails open:
if OpenAlex is unreachable or the config is missing, green-light simply finds
nothing and the normal score-based selection still runs.

Disable entirely with AFFIL_GREENLIGHT=0.
"""
from __future__ import annotations

import functools
import logging
import os
import re
import unicodedata
from pathlib import Path

import httpx
import yaml
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from ..models import Paper
from .references import extract_arxiv_id, should_retry_http

log = logging.getLogger(__name__)

CONFIG_PATH = Path("config/institutions.yaml")
OPENALEX_BASE = "https://api.openalex.org"


def greenlight_enabled() -> bool:
    return os.environ.get("AFFIL_GREENLIGHT", "1").strip().lower() not in ("0", "false", "no", "")


def _normalize(s: str) -> str:
    """Lowercase, fold accents, unify dashes, drop punctuation, collapse spaces."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[‐-―\-]", " ", s)   # any hyphen/dash → space
    s = re.sub(r"[^a-z0-9 ]+", " ", s)          # drop commas, periods, etc.
    return re.sub(r"\s+", " ", s).strip()


@functools.lru_cache(maxsize=1)
def _whitelist_patterns(path: str = str(CONFIG_PATH)) -> list[tuple[str, str]]:
    """Return [(normalized_pattern, canonical_display_name), ...]."""
    p = Path(path)
    if not p.exists():
        log.warning("institutions whitelist missing: %s", p)
        return []
    try:
        cfg = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as e:  # noqa: BLE001
        log.warning("could not parse %s: %s", p, e)
        return []
    out: list[tuple[str, str]] = []
    for name in (cfg.get("institutions") or []):
        out.append((_normalize(name), name))
    for alias in (cfg.get("aliases") or []):
        out.append((_normalize(alias), alias))
    # Longest patterns first so the most specific match wins.
    out.sort(key=lambda t: len(t[0]), reverse=True)
    return out


def match_affiliation(affiliations: list[str]) -> str | None:
    """Return the canonical institution name if any affiliation is whitelisted."""
    patterns = _whitelist_patterns()
    if not patterns:
        return None
    for raw in affiliations:
        if not raw:
            continue
        norm = _normalize(raw)
        if not norm:
            continue
        # Pad so an alias like "mit" matches as a whole token, not inside a word.
        padded = f" {norm} "
        for pat, canonical in patterns:
            needle = f" {pat} " if len(pat) <= 5 else pat
            if needle in padded:
                return canonical
    return None


def _doi_for(paper: Paper) -> str | None:
    """Best-effort DOI for an OpenAlex lookup (arXiv papers get a 10.48550 DOI)."""
    arxiv_id = extract_arxiv_id(paper.paper_id if paper.source == "arxiv" else None,
                                paper.arxiv_url)
    if arxiv_id:
        return f"10.48550/arXiv.{arxiv_id}"
    # Journal papers: paper_id or url often carries the DOI.
    for cand in (paper.paper_id, paper.url):
        if cand and "10." in cand:
            m = re.search(r"10\.\d{4,9}/\S+", cand)
            if m:
                return m.group(0)
    return None


@retry(
    retry=retry_if_exception(should_retry_http),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    reraise=True,  # surface the real HTTPStatusError, not an opaque RetryError
)
def _openalex_work(doi: str) -> dict:
    params = {"select": "authorships"}
    mailto = os.environ.get("OPENALEX_MAILTO")
    if mailto:
        params["mailto"] = mailto
    with httpx.Client(timeout=30) as c:
        r = c.get(f"{OPENALEX_BASE}/works/doi:{doi}", params=params)
        r.raise_for_status()
        return r.json()


def _parse_authorships(work: dict) -> tuple[list[str], list[str]]:
    """Split an OpenAlex work into (affiliation_strings, institution_names).

    The first list (institution display names + raw affiliation strings) feeds
    green-light matching; the second is a deduplicated list of clean institution
    display names for showing on the daily / journal pages.
    """
    affils: list[str] = []
    institutions: list[str] = []
    for a in work.get("authorships") or []:
        for inst in a.get("institutions") or []:
            name = inst.get("display_name")
            if name:
                affils.append(name)
                institutions.append(name)
        affils.extend(a.get("raw_affiliation_strings") or [])
    seen: set[str] = set()
    deduped = [n for n in institutions if not (n in seen or seen.add(n))]
    return affils, deduped


def _fetch_affiliations_and_institutions(doi: str) -> tuple[list[str], list[str]]:
    """(affiliation_strings, institution_names) for a work, ([], []) on failure."""
    try:
        work = _openalex_work(doi)
    except httpx.HTTPStatusError as e:  # fail open — green-light just finds nothing
        code = e.response.status_code
        hint = " (work not indexed yet?)" if code == 404 else (" (rate limited)" if code == 429 else "")
        log.info("OpenAlex affiliation lookup failed for %s: HTTP %s%s", doi, code, hint)
        return [], []
    except Exception as e:  # noqa: BLE001 — network/parse error, also fail open
        log.info("OpenAlex affiliation lookup failed for %s: %s", doi, e)
        return [], []
    return _parse_authorships(work)


def fetch_openalex_affiliations(doi: str) -> list[str]:
    """Return affiliation strings for a work, or [] on any failure."""
    return _fetch_affiliations_and_institutions(doi)[0]


def backfill_affiliations(papers: list[Paper]) -> int:
    """Populate `affiliations` + `institutions` from OpenAlex for the given papers.

    Used to fill in institution names for the daily / journal pages before they
    are rendered. Best-effort and fails open: papers OpenAlex doesn't know about
    (or when the feature is disabled / unreachable) simply keep empty lists.
    Results are cached on each Paper so the later green-light step reuses them
    instead of fetching twice. Returns the number of papers that got at least
    one institution.
    """
    if not greenlight_enabled():
        return 0
    n = 0
    for p in papers:
        if p.affiliations or p.institutions:
            continue  # already populated (e.g. a prior run on the same object)
        doi = _doi_for(p)
        if not doi:
            continue
        affils, institutions = _fetch_affiliations_and_institutions(doi)
        if affils:
            p.affiliations = affils
        if institutions:
            p.institutions = institutions
            n += 1
    return n


def green_light(paper: Paper, *, backfill: bool = True) -> str | None:
    """Return the matched institution name if this paper should be green-lit."""
    if not greenlight_enabled():
        return None
    # 1) Anything the scrapers (or a prior backfill_affiliations) already captured.
    hit = match_affiliation(paper.affiliations)
    if hit:
        return hit
    # 2) Back-fill from OpenAlex — skip when affiliations are already cached, since
    #    they come from the same source and re-fetching yields the same data.
    if backfill and not paper.affiliations:
        doi = _doi_for(paper)
        if doi:
            affils, institutions = _fetch_affiliations_and_institutions(doi)
            if affils:
                paper.affiliations = affils  # cache on the paper for reuse
                paper.institutions = institutions
                return match_affiliation(affils)
    return None
