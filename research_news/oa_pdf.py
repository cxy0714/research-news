"""Resolve a pasted paper link / DOI to a downloadable full-text PDF.

Motivation: the manual deep-read queue (``research_news.manual_requests``) used
to be arXiv-only — a non-arXiv paste was searched for an arXiv preprint by title
and, failing that, kept as a bookmark with no deep read. But a large share of the
journals worth reading serve their PDFs for free (Observational Studies on
Project MUSE, JMLR, PMLR, PLOS, eLife, Nature Communications, bioRxiv, PMC, …),
so "no preprint" is a bad reason to skip the read. This module finds that PDF.

Three layers, cheapest and most general first:

  1. **Google-Scholar meta tags** on the landing page (``citation_pdf_url``,
     ``citation_title``, ``citation_author``, …). Nearly every publisher emits
     them — this is what makes "many free journals" work *without* a per-journal
     table. It also hands us clean metadata (title / authors / venue / date /
     DOI), so a bare URL is enough to build a ``Paper``.
  2. **Host rules** (:data:`_HOST_RULES`) for the handful of sites whose landing
     page is unusable — behind a bot wall (Project Euclid / Incapsula), or a JS
     app — but whose PDF path is mechanical. Unknown hosts need no entry.
  3. **OpenAlex OA locations** (``best_oa_location.pdf_url`` + every
     ``locations[].pdf_url``) when a DOI is known: catches repository / PMC /
     publisher copies the landing page didn't advertise.

Every candidate is verified by *downloading* it and checking the ``%PDF`` magic
bytes, so a Cloudflare challenge or a paywall interstitial can never be stored as
a "PDF" and silently feed garbage to the deep read.

Fails open everywhere: any network / parse error yields ``None`` (the caller then
keeps the paper as a bookmark), never an exception.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, urlsplit

import httpx

log = logging.getLogger(__name__)

# Browser-ish UA: MUSE / PMLR / eLife / Wiley answer 403 to an obvious bot.
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
}

PDF_MAGIC = b"%PDF"
MIN_PDF_BYTES = 2048          # smaller than this is a stub / error page
MAX_PDF_BYTES = 120 * 1024 * 1024

_DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.I)
_URL_RE = re.compile(r"https?://[^\s<>\"')\]]+", re.I)


def extract_doi(text: str) -> str:
    """First DOI in ``text`` (trailing punctuation stripped), or ""."""
    m = _DOI_RE.search(text or "")
    return m.group(0).rstrip(".,;)]}'\"") if m else ""


def extract_url(text: str) -> str:
    """First http(s) URL in ``text`` (trailing punctuation stripped), or ""."""
    m = _URL_RE.search(text or "")
    return m.group(0).rstrip(".,;)]}'\"") if m else ""


def _host(url: str) -> str:
    return (urlsplit(url or "").hostname or "").lower().removeprefix("www.")


def landing_url(url: str) -> str:
    """Strip a trailing PDF marker so we can read the *landing* page's meta tags.

    ``…/article/999750/pdf`` → ``…/article/999750``;  ``…/23-0535.pdf`` is left
    alone (its landing page isn't derivable by chopping the extension)."""
    u = (url or "").split("#", 1)[0]
    u = re.sub(r"/pdf/?$", "", u, flags=re.I)
    u = re.sub(r"\.full\.pdf$", ".full", u, flags=re.I)
    return u


# ── layer 2: host rules ───────────────────────────────────────────────────────
# (host suffix, URL regex, replacement) — applied to the whole URL when the host
# matches. These exist ONLY for sites where layer 1 (meta tags) can't work: a bot
# wall (Project Euclid), a JS-rendered page, or no citation_pdf_url at all. Any
# journal not listed here still works via its landing page's meta tags, so this
# table stays short on purpose. Candidates are verified by magic bytes, so a rule
# that has gone stale costs a wasted request, never a corrupt "PDF".
_HOST_RULES: list[tuple[str, str, str]] = [
    ("arxiv.org",              r"/(?:abs|pdf)/([^/?#]+)$",        r"https://arxiv.org/pdf/\1"),
    ("jmlr.org",               r"/papers/v(\d+)/([^/]+?)\.html?$",
     r"https://www.jmlr.org/papers/volume\1/\2/\2.pdf"),
    ("proceedings.mlr.press",  r"/(v\d+)/([^/]+?)\.html?$",       r"https://proceedings.mlr.press/\1/\2/\2.pdf"),
    ("openreview.net",         r"/forum\?id=([^&#]+).*$",         r"https://openreview.net/pdf?id=\1"),
    # Keep the /pub/<n>/ prefix when present — both forms serve the article.
    ("muse.jhu.edu",           r"^(https://muse\.jhu\.edu/(?:pub/\d+/)?article/\d+)$", r"\1/pdf"),
    ("projecteuclid.org",      r"/(10\.\d{4,9}/[^/?#]+)\.full$",  r"https://projecteuclid.org/journalArticle/Download?urlId=\1"),
    ("biorxiv.org",            r"(/content/10\.\d{4,9}/[^?#]+?)(?:\.full)?$", r"https://www.biorxiv.org\1.full.pdf"),
    ("medrxiv.org",            r"(/content/10\.\d{4,9}/[^?#]+?)(?:\.full)?$", r"https://www.medrxiv.org\1.full.pdf"),
    ("nature.com",             r"(/articles/[^/?#]+)$",           r"https://www.nature.com\1.pdf"),
    ("link.springer.com",      r"/(?:article|chapter)/(10\.\d{4,9}/[^?#]+)$",
     r"https://link.springer.com/content/pdf/\1.pdf"),
    ("elifesciences.org",      r"(/articles/\d+)$",               r"https://elifesciences.org\1.pdf"),
    ("scipost.org",            r"^(https://scipost\.org/[A-Za-z0-9.]+)$", r"\1/pdf"),
    ("science.org",            r"/doi/(?:abs/|full/)?(10\.[^?#]+)$", r"https://www.science.org/doi/pdf/\1"),
    ("onlinelibrary.wiley.com", r"/doi/(?:abs/|full/|epdf/)?(10\.[^?#]+)$",
     r"https://onlinelibrary.wiley.com/doi/pdfdirect/\1"),
    ("tandfonline.com",        r"/doi/(?:abs/|full/)?(10\.[^?#]+)$", r"https://www.tandfonline.com/doi/pdf/\1"),
    ("dl.acm.org",             r"/doi/(?:abs/|full/)?(10\.[^?#]+)$", r"https://dl.acm.org/doi/pdf/\1"),
    ("mdpi.com",               r"^(https://www\.mdpi\.com/[\d-]+/\d+/\d+/\d+)$", r"\1/pdf"),
    ("journals.plos.org",      r"^(https://journals\.plos\.org/[^/]+)/article\?id=([^&#]+)$",
     r"\1/article/file?id=\2&type=printable"),
]


def host_rule_pdf(url: str) -> str | None:
    """PDF URL for ``url`` from the host-rule table, or None.

    Table patterns are written against the *path* for readability; they are
    anchored to the whole URL here (the replacements are absolute, so a partial
    match would otherwise leave the original scheme+host glued in front)."""
    host = _host(url)
    for suffix, pattern, repl in _HOST_RULES:
        if host == suffix or host.endswith("." + suffix):
            full = pattern if pattern.startswith("^") else "^.*?" + pattern
            new = re.sub(full, repl, url, count=1, flags=re.I)
            if new != url:
                return new
    return None


# ── layer 1: Google-Scholar / Dublin-Core meta tags ───────────────────────────

@dataclass
class PdfSource:
    """A paper resolved from a pasted link: where its PDF is + what it is."""
    landing_url: str
    pdf_candidates: list[str] = field(default_factory=list)
    doi: str = ""
    title: str = ""
    authors: list[str] = field(default_factory=list)
    venue: str = ""
    published: str | None = None
    volume: str | None = None
    issue: str | None = None
    abstract: str = ""
    arxiv_id: str = ""

    @property
    def pdf_url(self) -> str:
        return self.pdf_candidates[0] if self.pdf_candidates else ""


def parse_meta(html: str) -> dict:
    """Citation metadata from a landing page's ``<meta>`` tags.

    Reads the Google-Scholar ``citation_*`` set (what publishers emit for
    indexing) and falls back to Dublin Core / OpenGraph. Returns a dict with
    ``pdf_url, title, authors, venue, published, doi, volume, issue, abstract``;
    missing keys are absent. Dependency-light + pure so it is unit-testable on a
    saved page."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html or "", "lxml")
    bag: dict[str, list[str]] = {}
    for tag in soup.find_all("meta"):
        name = (tag.get("name") or tag.get("property") or "").strip().lower()
        content = (tag.get("content") or "").strip()
        if name and content:
            bag.setdefault(name, []).append(content)

    def first(*names: str) -> str:
        for n in names:
            if bag.get(n):
                return re.sub(r"\s+", " ", bag[n][0]).strip()
        return ""

    out: dict = {}
    pdf = first("citation_pdf_url", "eprints.document_url", "bepress_citation_pdf_url")
    if pdf:
        out["pdf_url"] = pdf
    title = first("citation_title", "dc.title", "dcterms.title", "og:title")
    if title:
        out["title"] = title
    authors = [re.sub(r"\s+", " ", a).strip()
               for a in (bag.get("citation_author") or bag.get("dc.creator") or [])]
    if authors:
        out["authors"] = _flip_names([a for a in authors if a])
    venue = first("citation_journal_title", "citation_conference_title",
                  "citation_inbook_title", "dc.source", "og:site_name")
    if venue:
        out["venue"] = venue
    date = first("citation_publication_date", "citation_online_date",
                 "citation_date", "dc.date", "citation_year")
    if date:
        out["published"] = _norm_date(date)
    doi = first("citation_doi", "dc.identifier.doi", "dc.identifier")
    doi = extract_doi(doi)
    if doi:
        out["doi"] = doi
    for key, names in (("volume", ("citation_volume",)), ("issue", ("citation_issue",))):
        v = first(*names)
        if v:
            out[key] = v
    abstract = first("citation_abstract", "dc.description", "og:description",
                     "description")
    if abstract and len(abstract) > 80:
        out["abstract"] = abstract
    return out


def _norm_date(raw: str) -> str:
    """Publisher dates come as ``2026/08/27``, ``2026-08-27``, ``Dec 13, 2023``
    or just ``2026``. Normalize to ISO where possible; pass the rest through
    (``Paper.published`` is a display string, so a year alone is fine)."""
    s = raw.strip().replace("/", "-")
    if re.fullmatch(r"\d{4}(-\d{1,2}){0,2}", s):
        parts = s.split("-")
        return "-".join([parts[0]] + [f"{int(p):02d}" for p in parts[1:]])
    try:
        from dateutil import parser as dateparser
        return dateparser.parse(s).date().isoformat()
    except Exception:  # noqa: BLE001 — unparseable, keep the raw text
        return s


def _flip_names(authors: list[str]) -> list[str]:
    """``"Doe, Jane"`` → ``"Jane Doe"`` (citation_author uses both forms)."""
    out = []
    for a in authors:
        if a.count(",") == 1:
            family, given = (p.strip() for p in a.split(","))
            a = f"{given} {family}" if given and family else a
        out.append(a)
    return out


# ── HTTP ──────────────────────────────────────────────────────────────────────

def _proxy_modes() -> list[bool]:
    """``trust_env`` values to try, in order.

    Publisher access cuts both ways and no single setting serves both:
    arXiv / OpenAlex / Crossref need the local proxy (GFW), while a publisher that
    licenses *this machine's* IP — or just dislikes a foreign proxy exit — answers
    a bot-verification page through it and the real PDF direct (Project MUSE does
    exactly this). So: ambient proxy first, then a direct retry. When no proxy is
    configured there's only one mode to try."""
    import os
    proxied = any(os.environ.get(k) for k in
                  ("HTTPS_PROXY", "HTTP_PROXY", "ALL_PROXY",
                   "https_proxy", "http_proxy", "all_proxy"))
    return [True, False] if proxied else [True]


def _get_html(url: str, timeout: float = 30, *, trust_env: bool = True) -> tuple[str, str]:
    """(html, final_url) for one fetch of a landing page; ("", url) on failure."""
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA,
                          trust_env=trust_env) as c:
            r = c.get(url)
            r.raise_for_status()
            ctype = (r.headers.get("content-type") or "").lower()
            if "html" in ctype or "xml" in ctype:
                return r.text, str(r.url)
            log.info("landing page is not HTML (%s): %s",
                     ctype.split(";")[0] or "?", url)
    except Exception as e:  # noqa: BLE001 — fail open
        log.info("landing page fetch failed (%s, proxy=%s): %s", url, trust_env, e)
    return "", url


def _fetch_meta(url: str) -> tuple[dict, str]:
    """(citation metadata, final landing URL) for ``url``, trying each connection
    mode until one returns a page that actually carries metadata.

    A bot-verification page is still ``text/html``, so "got HTML" is not good
    enough to stop at: MUSE serves a ``/verify?url=…`` interstitial through a
    proxy and the real article direct. A page with neither a title nor a PDF link
    is treated as unusable, and the *requested* URL is kept as the landing URL so
    an interstitial never ends up recorded as the paper's page."""
    best: tuple[dict, str] = ({}, url)
    for trust_env in _proxy_modes():
        html, final = _get_html(url, trust_env=trust_env)
        if not html:
            continue
        meta = parse_meta(html)
        if meta.get("title") or meta.get("pdf_url"):
            return meta, final
        log.info("landing page carried no citation metadata (proxy=%s): %s",
                 trust_env, url)
    return best


class _NotAPdf(Exception):
    """Internal: the response body isn't a usable PDF (don't retry — it won't
    become one)."""


def _stream_pdf(url: str, tmp: Path, timeout: float, trust_env: bool = True) -> int:
    """Stream ``url`` into ``tmp``; return the byte count. Raises ``_NotAPdf``
    when the body isn't a PDF, or the transport error for the retry wrapper."""
    with httpx.Client(timeout=timeout, follow_redirects=True, headers=UA,
                      trust_env=trust_env) as c:
        with c.stream("GET", url) as r:
            r.raise_for_status()
            first = True
            size = 0
            with tmp.open("wb") as f:
                for chunk in r.iter_bytes(chunk_size=64 * 1024):
                    if first and chunk:
                        first = False
                        if not chunk[:8].startswith(PDF_MAGIC):
                            ctype = (r.headers.get("content-type") or "?").split(";")[0]
                            log.info("not a PDF (%s) at %s", ctype, url)
                            raise _NotAPdf
                    size += len(chunk)
                    if size > MAX_PDF_BYTES:
                        log.info("PDF too large (>%d MB): %s",
                                 MAX_PDF_BYTES // (1024 * 1024), url)
                        raise _NotAPdf
                    f.write(chunk)
    if size < MIN_PDF_BYTES:
        log.info("PDF suspiciously small (%d bytes): %s", size, url)
        raise _NotAPdf
    return size


def fetch_pdf(url: str, dest: Path, *, timeout: float = 120,
              attempts: int = 3) -> Path | None:
    """Download ``url`` to ``dest`` **only if it really is a PDF**.

    Streams to a temp file, checks the ``%PDF`` magic bytes and a plausible size,
    then moves it into place. Returns the path, or None (nothing written) when the
    response is HTML — a paywall page, a bot challenge, a 404 — or on any error.
    Transport failures are retried; a non-PDF body is not (it won't change).
    """
    from tenacity import (retry, retry_if_not_exception_type, stop_after_attempt,
                          wait_exponential)

    tmp = dest.with_suffix(dest.suffix + ".part")
    runner = retry(stop=stop_after_attempt(attempts),
                   wait=wait_exponential(multiplier=2, min=2, max=15),
                   retry=retry_if_not_exception_type(_NotAPdf),
                   reraise=True)(_stream_pdf)
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        for trust_env in _proxy_modes():
            try:
                size = runner(url, tmp, timeout, trust_env)
            except _NotAPdf:
                continue     # bot wall / paywall on this route — try the other
            except Exception as e:  # noqa: BLE001 — fail open, try the other route
                log.info("PDF download failed (%s, proxy=%s): %s", url, trust_env, e)
                continue
            tmp.replace(dest)
            log.info("downloaded PDF (%d KB, proxy=%s): %s", size // 1024,
                     trust_env, url)
            return dest
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
    return None


# ── top level ─────────────────────────────────────────────────────────────────

def _looks_like_pdf_url(url: str) -> bool:
    return bool(re.search(r"(\.pdf($|[?#])|/pdf($|[?#/])|type=printable)", url or "", re.I))


def resolve(text: str, *, doi: str = "", use_openalex: bool = True) -> PdfSource | None:
    """Resolve a pasted link / DOI / citation to a :class:`PdfSource`.

    ``text`` may be a bare URL, a DOI, or a citation string containing either.
    Returns None when no URL or DOI can be found in it (a pure title — the caller
    should fall back to searching arXiv by title). A returned source has at least
    one PDF *candidate*; whether a candidate really yields a PDF is only known
    after :func:`download`, which verifies the bytes.
    """
    from urllib.parse import urljoin

    url = extract_url(text)
    doi = doi or extract_doi(url) or extract_doi(text)
    if not url and doi:
        url = "https://doi.org/" + quote(doi, safe="/:")
    if not url:
        return None

    landing = landing_url(url)
    meta, final_url = _fetch_meta(landing)

    cands: list[str] = []

    def _add(c: str | None) -> None:
        if c and c not in cands:
            cands.append(c)

    # A pasted PDF link is the cheapest, most authoritative candidate.
    if _looks_like_pdf_url(url):
        _add(url)
    if meta.get("pdf_url"):
        _add(urljoin(final_url or landing, meta["pdf_url"]))
    _add(host_rule_pdf(final_url or landing))
    if (final_url or landing) != landing:
        _add(host_rule_pdf(landing))

    doi = doi or meta.get("doi", "")
    src = PdfSource(
        landing_url=final_url or landing,
        doi=doi,
        title=meta.get("title", ""),
        authors=list(meta.get("authors") or []),
        venue=meta.get("venue", ""),
        published=meta.get("published"),
        volume=meta.get("volume"),
        issue=meta.get("issue"),
        abstract=meta.get("abstract", ""),
    )
    if _host(src.landing_url) == "arxiv.org":
        m = re.search(r"/(?:abs|pdf)/([^/?#v]+)", src.landing_url)
        src.arxiv_id = m.group(1) if m else ""

    # Repository / PMC / publisher copies the landing page didn't advertise.
    if use_openalex and doi:
        from .scrapers.openalex import work_oa_info
        info = work_oa_info(doi)
        for c in info.get("pdf_urls") or []:
            _add(c)
        for key in ("title", "venue", "abstract"):
            if not getattr(src, key) and info.get(key):
                setattr(src, key, info[key])
        if not src.authors and info.get("authors"):
            src.authors = list(info["authors"])
        if not src.published and info.get("published"):
            src.published = info["published"]
        if not src.arxiv_id and info.get("arxiv_id"):
            src.arxiv_id = info["arxiv_id"]

    src.pdf_candidates = cands
    if not cands:
        log.info("no PDF candidate for %s (doi=%s)", url, doi or "—")
        return None
    log.info("resolved %s → %d PDF candidate(s); title=%r",
             url, len(cands), (src.title or "")[:60])
    return src


def download(src: PdfSource, dest: Path) -> Path | None:
    """Try each candidate in order; return the path of the first real PDF."""
    for cand in src.pdf_candidates:
        got = fetch_pdf(cand, dest)
        if got:
            return got
    log.info("all %d PDF candidate(s) failed for %s",
             len(src.pdf_candidates), src.landing_url)
    return None
