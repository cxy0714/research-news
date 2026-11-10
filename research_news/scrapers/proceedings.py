"""Proceedings scrapers for the AI evaluation / benchmark track.

Every venue is an isolated, deterministic HTML parser (no LLM): the benchmark
pipeline only needs title / authors / abstract / links, then does its own
keyword prefilter and LLM scoring.

Sources implemented (all open access, no API key):

- PMLR      (ICML, AISTATS, COLT, UAI, ...)  proceedings.mlr.press
- ACL       (ACL/EMNLP/NAACL volumes)        aclanthology.org
- CVF       (CVPR / ICCV)                    openaccess.thecvf.com
- AAAI      (AAAI-YY technical tracks)       ojs.aaai.org
- NeurIPS   (proceedings.neurips.cc)         optional, per-year listing

Design notes:
- Volume/listing pages are large (PMLR v306 ≈ 7 MB, ACL 2026 long ≈ 7 MB,
  CVPR ?day=all ≈ 12 MB); they are fetched once per run and cached under
  ``tmp/bench_cache/`` (never committed).
- Per-paper abstract pages are fetched **only for candidates** that passed the
  title filter — that keeps a 6,000-paper venue to a few hundred requests.
- Throttled at ~1.2 s/request with a descriptive UA, per the sites' terms.
"""
from __future__ import annotations

import hashlib
import logging
import re
import threading
import time
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

from ..models import Paper

log = logging.getLogger(__name__)

UA = "research-news/1.0 (+https://github.com/cxy0714/research-news; mailto:cxy0714@sjtu.edu.cn)"
CACHE_DIR = Path("tmp/bench_cache")
MIN_INTERVAL = 1.2

_last = [0.0]
_lock = threading.Lock()


def _throttle() -> None:
    with _lock:
        wait = MIN_INTERVAL - (time.monotonic() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.monotonic()


def _cache_path(url: str) -> Path:
    return CACHE_DIR / (hashlib.sha1(url.encode("utf-8")).hexdigest() + ".html")


def fetch(url: str, *, use_cache: bool = True, timeout: float = 120) -> str:
    """GET with throttle + on-disk cache. Raises after 3 attempts."""
    path = _cache_path(url)
    if use_cache and path.exists() and path.stat().st_size > 0:
        return path.read_text(encoding="utf-8", errors="replace")
    last_exc: Exception | None = None
    for attempt in range(3):
        _throttle()
        try:
            with httpx.Client(
                timeout=timeout, follow_redirects=True, headers={"User-Agent": UA}
            ) as c:
                r = c.get(url)
            if r.status_code in (429, 503):
                time.sleep(10 * (attempt + 1))
                continue
            r.raise_for_status()
            text = r.text
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            return text
        except Exception as e:  # noqa: BLE001
            last_exc = e
            time.sleep(3 * (attempt + 1))
    assert last_exc is not None
    raise last_exc


def _soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "lxml")


def _clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


def _authors_from_text(s: str) -> list[str]:
    s = s.split(";")[0]
    s = re.sub(r"\s+", " ", s).strip(" ,")
    return [a.strip() for a in s.split(",") if a.strip()]


def _paper(
    *,
    venue_id: str,
    label: str,
    pid: str,
    title: str,
    authors: list[str] | None = None,
    abstract: str = "",
    url: str = "",
    pdf_url: str = "",
    track: str = "",
    openreview_id: str = "",
    arxiv_id: str = "",
) -> Paper:
    return Paper(
        source=venue_id,
        paper_id=f"{venue_id}:{pid}",
        title=_clean(title),
        authors=authors or [],
        abstract=_clean(abstract),
        url=url,
        pdf_url=pdf_url,
        venue=label,
        categories=[track] if track else [],
        track="ai",
        venue_id=venue_id,
        venue_track=track,
        proceedings_url=url,
        openreview_id=openreview_id,
        arxiv_id=arxiv_id,
    )


# ── PMLR (ICML / AISTATS / COLT / UAI / ...) ─────────────────────────────────

def pmlr_volume(volume: str, *, venue_id: str, label: str, track: str = "Main") -> list[Paper]:
    url = f"https://proceedings.mlr.press/v{volume}/"
    soup = _soup(fetch(url))
    out: list[Paper] = []
    for div in soup.select("div.paper"):
        t = div.select_one("p.title")
        if not t:
            continue
        authors_node = div.select_one("span.authors")
        links = {a.get_text(strip=True).lower(): a.get("href", "") for a in div.select("p.links a")}
        page_url = links.get("abs", "")
        pdf_url = links.get("download pdf", "")
        or_id = ""
        m = re.search(r"[?&]id=([A-Za-z0-9_-]+)", links.get("openreview", ""))
        if m:
            or_id = m.group(1)
        pid = page_url.rsplit("/", 1)[-1].removesuffix(".html") or hashlib.sha1(
            _clean(t.get_text()).encode()
        ).hexdigest()[:12]
        out.append(
            _paper(
                venue_id=venue_id,
                label=label,
                pid=pid,
                title=t.get_text(" ", strip=True),
                authors=_authors_from_text(
                    authors_node.get_text(" ", strip=True) if authors_node else ""
                ),
                url=page_url,
                pdf_url=pdf_url,
                track=track,
                openreview_id=or_id,
            )
        )
    log.info("[%s] PMLR v%s: %d papers", venue_id, volume, len(out))
    return out


def pmlr_detail(p: Paper) -> Paper:
    """Fill abstract from a PMLR per-paper page."""
    if p.abstract or not p.url:
        return p
    soup = _soup(fetch(p.url))
    node = soup.select_one("#abstract")
    if node:
        p.abstract = _clean(node.get_text(" ", strip=True))
    return p


# ── ACL Anthology (ACL / EMNLP / NAACL / ...) ────────────────────────────────

def acl_volume(volume: str, *, venue_id: str, label: str, track: str = "") -> list[Paper]:
    """ACL volume pages carry every abstract inline — one request per volume."""
    if not track:
        track = volume.split(".", 1)[-1]
    url = f"https://aclanthology.org/volumes/{volume}/"
    soup = _soup(fetch(url))

    abstracts: dict[str, str] = {}
    for d in soup.select("div[id^=abstract-]"):
        pid = d["id"].removeprefix("abstract-").replace("--", ".")
        abstracts[pid] = _clean(d.get_text(" ", strip=True))

    out: list[Paper] = []
    seen: set[str] = set()
    for entry in soup.select("div.d-sm-flex.align-items-stretch"):
        a = entry.select_one("strong a[href]")
        if not a or not a["href"].startswith(f"/{volume}."):
            continue
        href = a["href"].strip("/")
        pid = href.split("/")[0]
        if pid in seen:
            continue
        seen.add(pid)
        authors = [
            _clean(x.get_text())
            for x in entry.select("a[href^='/people/']")
        ]
        pdf = entry.select_one("a[href$='.pdf']")
        # Join text nodes without inserting separators: ACL wraps fixed-case
        # letters in <span class="acl-fixed-case">, and get_text(" ", ...) would
        # turn "of LLMs" into "of LLM s", while strip=True would turn it into
        # "ofLLMs". Concatenating the raw strings preserves the source spacing.
        title = _clean("".join(str(x) for x in a.find_all(string=True)))
        out.append(
            _paper(
                venue_id=venue_id,
                label=label,
                pid=pid,
                title=title,
                authors=authors,
                abstract=abstracts.get(pid, ""),
                url=f"https://aclanthology.org/{pid}/",
                pdf_url=pdf["href"] if pdf else "",
                track=track,
            )
        )
    log.info("[%s] ACL %s: %d papers (%d with abstracts)",
             venue_id, volume, len(out), sum(1 for p in out if p.abstract))
    return out


# ── CVF (CVPR / ICCV) ────────────────────────────────────────────────────────

def cvf_conference(conf: str, year: int, *, venue_id: str, label: str) -> list[Paper]:
    base = f"https://openaccess.thecvf.com/{conf}{year}"
    soup = _soup(fetch(f"{base}?day=all"))
    out: list[Paper] = []
    seen: set[str] = set()
    for a in soup.select("a[href*='/html/']"):
        href = a.get("href", "")
        if not href or href in seen:
            continue
        seen.add(href)
        pid = href.rsplit("/", 1)[-1].removesuffix(".html")
        out.append(
            _paper(
                venue_id=venue_id,
                label=label,
                pid=pid,
                title=a.get_text(" ", strip=True),
                url="https://openaccess.thecvf.com" + href,
                track="Main",
            )
        )
    log.info("[%s] %s %d: %d papers", venue_id, conf, year, len(out))
    return out


def cvf_detail(p: Paper) -> Paper:
    if p.abstract or not p.url:
        return p
    soup = _soup(fetch(p.url))
    if node := soup.select_one("div#abstract"):
        p.abstract = _clean(node.get_text(" ", strip=True))
    if not p.authors and (node := soup.select_one("div#authors")):
        p.authors = _authors_from_text(node.get_text(" ", strip=True))
    if not p.pdf_url and (a := soup.select_one("a[href$='.pdf']")):
        p.pdf_url = "https://openaccess.thecvf.com" + a["href"] if a["href"].startswith("/") else a["href"]
    return p


# ── AAAI (OJS technical tracks) ──────────────────────────────────────────────

def aaai_year(year: int, *, venue_id: str, label: str) -> list[Paper]:
    """Collect all AAAI-YY technical-track issues, titles only (detail is lazy)."""
    archive = _soup(fetch("https://ojs.aaai.org/index.php/AAAI/issue/archive"))
    tag = f"AAAI-{str(year)[-2:]}"
    issue_urls: list[str] = []
    for a in archive.select("a[href*='/issue/view/']"):
        if tag in a.get_text(" ", strip=True):
            issue_urls.append(a["href"])
    log.info("[%s] %d issue pages for %s", venue_id, len(issue_urls), tag)
    out: list[Paper] = []
    seen: set[str] = set()
    for iurl in issue_urls:
        soup = _soup(fetch(iurl))
        track = ""
        if h := soup.select_one("h1"):
            text = _clean(h.get_text())
            m = re.search(r"Tracks?\s*(\d+)", text)
            track = f"Track {m.group(1)}" if m else text
        for a in soup.select("a[href*='/article/view/']"):
            href = a["href"]
            if href in seen:
                continue
            seen.add(href)
            pid = href.rstrip("/").rsplit("/", 1)[-1]
            out.append(
                _paper(
                    venue_id=venue_id,
                    label=label,
                    pid=pid,
                    title=a.get_text(" ", strip=True),
                    url=href,
                    track=track,
                )
            )
    log.info("[%s] AAAI %d: %d papers", venue_id, year, len(out))
    return out


def aaai_detail(p: Paper) -> Paper:
    if p.abstract or not p.url:
        return p
    soup = _soup(fetch(p.url))
    if node := soup.select_one("section.item.abstract"):
        # drop the "Abstract" heading
        for h in node.select("h2"):
            h.decompose()
        p.abstract = _clean(node.get_text(" ", strip=True))
    if node := soup.select_one("h1.page_title"):
        title = _clean(node.get_text(" ", strip=True))
        if title:
            p.title = title
    if not p.authors:
        names = [
            _clean(n.get_text())
            for n in soup.select("section.item.authors span.name")
        ]
        if names:
            p.authors = names
    if not p.pdf_url and (a := soup.select_one("a.obj_galley_link.pdf")):
        p.pdf_url = a["href"]
    return p


# ── NeurIPS (per-year listing; used for D&B / main tracks) ───────────────────

def neurips_year(year: int, *, venue_id: str, label: str,
                 href_must_contain: str | None = None) -> list[Paper]:
    base = f"https://proceedings.neurips.cc/paper_files/paper/{year}"
    soup = _soup(fetch(base))
    out: list[Paper] = []
    for a in soup.select("a[href*='-Abstract-']"):
        href = a["href"]
        if href_must_contain and href_must_contain not in href:
            continue
        track = "Datasets & Benchmarks" if "Datasets_and_Benchmarks" in href else "Main"
        pid = href.rsplit("/", 1)[-1].removesuffix(".html")
        out.append(
            _paper(
                venue_id=venue_id,
                label=label,
                pid=pid,
                title=a.get_text(" ", strip=True),
                url="https://proceedings.neurips.cc" + href,
                track=track,
            )
        )
    log.info("[%s] NeurIPS %d: %d papers", venue_id, year, len(out))
    return out


def neurips_detail(p: Paper) -> Paper:
    if p.abstract or not p.url:
        return p
    soup = _soup(fetch(p.url))
    # abstract page: <h4>Authors</h4> ... <p>abstract text</p>, PDF link
    if node := soup.select_one("div.container p"):
        p.abstract = _clean(node.get_text(" ", strip=True))
    if not p.authors:
        h4 = soup.find("h4")
        if h4:
            p.authors = _authors_from_text(h4.get_text(" ", strip=True))
    if not p.pdf_url and (a := soup.select_one("a[href$='.pdf']")):
        p.pdf_url = a["href"] if a["href"].startswith("http") else "https://proceedings.neurips.cc" + a["href"]
    return p


# ── abstract enrichment (candidates only) ────────────────────────────────────

def enrich_abstracts(papers: list[Paper], *, adapter: str, workers: int = 1) -> int:
    """Fetch abstracts for papers that don't have one. Returns the count filled."""
    fn = {
        "pmlr": pmlr_detail,
        "cvf": cvf_detail,
        "aaai": aaai_detail,
        "neurips": neurips_detail,
    }.get(adapter)
    if fn is None:
        return 0
    filled = 0
    for i, p in enumerate(papers, 1):
        if p.abstract:
            continue
        try:
            fn(p)
            if p.abstract:
                filled += 1
        except Exception as e:  # noqa: BLE001
            log.warning("abstract fetch failed for %s: %s", p.paper_id, e)
        if i % 25 == 0:
            log.info("  fetched %d/%d abstracts", i, len(papers))
    return filled
