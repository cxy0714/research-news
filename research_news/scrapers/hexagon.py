"""Hexagon (hexagonmath.org) scraper — arXiv's AI-era counterpart.

Hexagon is a moderated, non-peer-reviewed repository for research-level works in
the mathematical sciences and theoretical computer science, including
AI-generated and human+AI mixed texts. Its identifiers deliberately mirror
arXiv's (`2610.00165`, `hexagon:2610.00165v1`) and it ships an arXiv-compatible
public API, so this module keeps the shape of :mod:`research_news.scrapers.arxiv`
— a fast "today" path plus a query-API fallback:

- Daily path: the JSON list ``/api/v1/works`` (newest first, cursor-paginated).
  Richest projection: authors *with affiliations*, primary subject + cross-lists,
  the tools behind the text, the AI-authorship flags, and the record/PDF links.

- Fallback path: the arXiv-compatible Atom query ``/api/query``
  (``sortBy=submittedDate``, offset paging), used when the JSON list is
  unreachable or empty. Same authors / affiliations / subjects / PDF link (under
  Hexagon's ``mathlake:`` Atom extensions), minus the human-understanding flag.

What lands on :class:`Paper`: ``categories`` = subject + cross-lists
(arXiv-style); ``affiliations`` / ``institutions`` straight from the deposit, so
the top-institution green-light works without waiting for OpenAlex (most
deposits have no DOI or arXiv id to look up); and ``venue`` =
``"Hexagon · 人机混合 · 人类理解：全部 · 工具: Lean 4.34.1 / Claude Opus 5.5"``,
since "who — or what — wrote this, and how much did a human understand" is the
decision-relevant metadata for this repository, and ``venue`` is exactly what the
scoring and deep-read prompts already receive.

Unlike arXiv, Hexagon publishes continuously (weekends included), so the fetch
window reaches back ``lookback_days`` (config/sources.yaml, default 3) instead of
being a single announcement day: a work published after one run's cut-off is
still picked up by the next run, and the global seen-set
(``data/seen_papers.json``) keeps it from being scored twice.
"""
from __future__ import annotations

import logging
import os
import re
import threading
import time
from datetime import date, datetime, timedelta, timezone
from xml.etree import ElementTree as ET

import httpx

from ..models import Paper

log = logging.getLogger(__name__)

SITE = "https://hexagonmath.org"
LIST_URL = f"{SITE}/api/v1/works"
QUERY_URL = f"{SITE}/api/query"

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"
# Hexagon's own Atom extensions (the JSON API carries the same fields flat).
MATHLAKE_NS = "{https://mathlake.org/schemas/atom}"

# Both APIs cap one request at 100 items; `limit` above that is a 400.
PAGE_MAX = 100

# Hexagon is friendlier to identified clients; env override mirrors ARXIV_USER_AGENT.
_DEFAULT_UA = "research-news/1.0 (+https://github.com/cxy0714/research-news)"

# New- and (defensively) old-style arXiv-shaped ids: 2610.00165 / math.ST/0123456.
_HEX_ID_RE = re.compile(r"\b(\d{4}\.\d{5})(?:v[1-9]\d*)?\b")
_OLD_ID_RE = re.compile(r"\b([a-z\-]+(?:\.[A-Z]{2})?/\d{7})(?:v[1-9]\d*)?\b")

# Request spacing between paged calls, so a multi-page catch-up stays polite.
_PAGE_SLEEP = 1.0
_last_request = [0.0]
_throttle_lock = threading.Lock()


# ── HTTP ──────────────────────────────────────────────────────────────────────

def _headers() -> dict:
    return {"User-Agent": os.environ.get("HEXAGON_USER_AGENT", _DEFAULT_UA)}


def _pause() -> None:
    """Space paged requests by at least :data:`_PAGE_SLEEP` seconds."""
    with _throttle_lock:
        wait = _PAGE_SLEEP - (time.monotonic() - _last_request[0])
        if wait > 0:
            time.sleep(wait)
        _last_request[0] = time.monotonic()


def _retry_after_seconds(resp: httpx.Response, attempt: int) -> float:
    ra = (resp.headers.get("Retry-After") or "").strip()
    if ra.isdigit():
        return min(float(ra), 120)
    return min(10.0 * (attempt + 1), 90.0)


def _get(url: str, params: dict | None = None, *, timeout: float = 40,
         attempts: int = 3) -> httpx.Response:
    """GET with retries on 429/5xx/timeout; raises when every attempt fails.

    Other 4xx raise immediately — a bad query won't get better by retrying.
    """
    last: Exception | None = None
    for attempt in range(attempts):
        _pause()
        try:
            with httpx.Client(timeout=timeout, follow_redirects=True,
                              headers=_headers()) as c:
                r = c.get(url, params=params)
        except httpx.TimeoutException as e:
            last = e
            time.sleep(min(5.0 * (attempt + 1), 30))
            continue
        if r.status_code in (429, 500, 502, 503, 504):
            delay = _retry_after_seconds(r, attempt)
            log.info("Hexagon %d; waiting %.0fs then retry (%d/%d)",
                     r.status_code, delay, attempt + 1, attempts)
            last = httpx.HTTPStatusError(
                f"{r.status_code} from Hexagon", request=r.request, response=r)
            time.sleep(delay)
            continue
        r.raise_for_status()
        return r
    if last:
        raise last
    raise RuntimeError("Hexagon fetch failed with no exception captured")


def _get_json(url: str, params: dict | None = None) -> dict:
    return _get(url, params).json()


def _get_text(url: str, params: dict | None = None) -> str:
    return _get(url, params).text


# ── shared helpers ────────────────────────────────────────────────────────────

def normalize_hexagon_id(text: str | None) -> str:
    """Bare Hexagon id (``2610.00165``) from an id or URL, version stripped.

    Accepts ``2610.00165v2``, ``hexagon:2610.00165v2``, ``/abs/2610.00165v2``,
    ``/pdf/2610.00165`` and the API's ``links.*`` URLs. Returns ``""`` when
    nothing matches.
    """
    s = (text or "").strip()
    m = _HEX_ID_RE.search(s) or _OLD_ID_RE.search(s)
    return m.group(1) if m else ""


def _paper_id(identifier: str) -> str:
    """Namespaced ``paper_id`` mirroring Hexagon's own ``hexagon:2610.00165v1``.

    Hexagon numbers works exactly like arXiv (YYMM.NNNNN), so the prefix is what
    keeps a Hexagon work from colliding with a *different* arXiv paper in the
    id-keyed stores (``data/highlights.json``, ``deep_reads_index.json``). Same
    convention as ``jmlr:v27/...`` / ``oa:<host>-<slug>``.
    """
    bare = normalize_hexagon_id(identifier) or identifier.strip()
    return f"hexagon:{bare}"


def _as_date(value: str | None) -> date | None:
    """UTC date from a Hexagon timestamp.

    Handles both shapes the API emits: ``publishedAt`` (``2026-10-09T14:54:51.638Z``)
    and ``createdAt`` (``2026-10-08 21:37:01``, no zone → assumed UTC).
    """
    if not value:
        return None
    s = value.strip().replace("Z", "+00:00")
    if "T" not in s and " " in s:
        s = s.replace(" ", "T", 1)
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).date()


def _date_window(for_date: date | None, lookback_days: int) -> tuple[date, date]:
    """Inclusive ``(start, end)`` of publication dates to accept."""
    end = for_date or date.today()
    return end - timedelta(days=max(0, lookback_days)), end


def _categories(subject: str | None, cross: list[str] | None) -> list[str]:
    out: list[str] = []
    for c in [subject] + list(cross or []):
        c = (c or "").strip()
        if c and c not in out:
            out.append(c)
    return out


def _split_affiliations(affiliations: list[str]) -> list[str]:
    """Split free-text affiliation strings into display names.

    Hexagon records affiliations as free text (``"Harvard University and a16z
    crypto"``), so there is no clean institution list to read: we split on
    " and " / " & " / ";" — keeping comma-joined names intact (``"University of
    California, Los Angeles"``) — and fall back to the raw string.
    """
    out: list[str] = []
    for raw in affiliations:
        for part in re.split(r"\s+&\s+|\s*;\s*|\s+and\s+", raw or "", flags=re.I):
            s = " ".join(part.split())
            if s and s not in out:
                out.append(s)
    return out


_AUTHORSHIP_ZH = {
    "human": "主要人工撰写",
    "mixed": "人机混合",
    "no-human-author-claimed": "无人类作者署名",
    "primarily-ai": "主要 AI 生成",
}
_UNDERSTANDING_ZH = {
    "all": "人类理解：全部",
    "some": "人类理解：部分",
    "none": "人类理解：无",
}


def _tool_labels(tools: list | None, limit: int = 4) -> list[str]:
    """Deduped ``"Claude Opus 5.5"``-style labels for the tools behind a text."""
    out: list[str] = []
    for t in tools or []:
        if not isinstance(t, dict):
            continue
        name = (t.get("name") or "").strip()
        if not name:
            continue
        label = " ".join(f"{name} {t.get('version') or ''}".split())
        if label not in out:
            out.append(label)
        if len(out) >= limit:
            break
    return out


def _venue(authorship_mode: str | None, human_understanding: str | None,
           tools: list | None) -> str:
    """``"Hexagon · 人机混合 · 人类理解：全部 · 工具: Lean 4.34.1 / ChatGPT 6.1"``.

    The provenance rides on ``venue`` because that is exactly what the scoring and
    deep-read prompts already hand the model (``Venue: ...``) and what the daily /
    deep-read pages render as 期刊/来源. For a repository whose whole point is
    hosting AI-generated mathematics, "who (or what) wrote it, and to what extent
    a human understood it" is the most decision-relevant metadata on the record.
    """
    bits: list[str] = []
    mode = _AUTHORSHIP_ZH.get((authorship_mode or "").strip())
    if mode:
        bits.append(mode)
    und = _UNDERSTANDING_ZH.get((human_understanding or "").strip())
    if und:
        bits.append(und)
    labels = _tool_labels(tools)
    if labels:
        bits.append("工具: " + " / ".join(labels))
    return "Hexagon" + (" · " + " · ".join(bits) if bits else "")


def _subject_match(primary: str | None, cross: list[str] | None,
                   subjects: set[str], include_cross_listed: bool) -> bool:
    """Is this work in the configured subject scope?

    An empty ``subjects`` set means "no whitelist" → every subject passes.
    """
    if not subjects:
        return True
    if (primary or "").strip() in subjects:
        return True
    return include_cross_listed and any(
        (c or "").strip() in subjects for c in cross or []
    )


# ── JSON list path (daily) ────────────────────────────────────────────────────

def _work_date(w: dict) -> date | None:
    """Publication date of a list record (falls back to version/record creation)."""
    return _as_date(
        w.get("publishedAt") or w.get("versionCreatedAt") or w.get("createdAt")
    )


def _work_to_paper(w: dict) -> Paper | None:
    """Map one ``/api/v1/works`` record onto :class:`Paper`."""
    ident = normalize_hexagon_id(w.get("identifier") or w.get("id") or "")
    if not ident:
        return None
    links = w.get("links") or {}
    authors: list[str] = []
    affiliations: list[str] = []
    for a in w.get("authors") or []:
        if not isinstance(a, dict):
            continue
        if a.get("name"):
            authors.append(str(a["name"]).strip())
        if a.get("affiliation"):
            affiliations.append(str(a["affiliation"]).strip())
    published = _work_date(w)
    arxiv_id = normalize_hexagon_id(w.get("arxivId") or "")
    return Paper(
        source="hexagon",
        paper_id=_paper_id(ident),
        title=" ".join((w.get("title") or "").split()),
        authors=authors,
        abstract=" ".join((w.get("abstract") or "").split()),
        url=links.get("record") or f"{SITE}/abs/{ident}",
        arxiv_url=f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None,
        categories=_categories(w.get("subject"), w.get("crossListSubjects")),
        published=published.isoformat() if published else None,
        venue=_venue(w.get("authorshipMode"), w.get("humanUnderstanding"),
                     w.get("tools")),
        affiliations=affiliations,
        # Hexagon's own affiliations are usually the only institution signal
        # available (few deposits carry a DOI or an arXiv id for OpenAlex), so
        # the free-text strings are also what the 机构 line shows.
        institutions=_split_affiliations(affiliations),
        pdf_url=links.get("pdf") or f"{SITE}/pdf/{ident}",
    )


def _fetch_list(start: date, end: date, *, subjects: set[str],
                include_cross_listed: bool, max_works: int) -> tuple[list[Paper], bool]:
    """Works published in ``[start, end]`` from the JSON list, newest page first.

    Returns ``(papers, ok)`` where ``ok`` is False when the very first request
    failed — the caller then falls back to the Atom query. Pages are walked until
    the window start is passed, the cursor runs out, or ``max_works`` is reached.
    """
    papers: list[Paper] = []
    seen: set[str] = set()
    cursor: str | None = None
    ok = False
    while True:
        params: dict[str, object] = {"limit": PAGE_MAX}
        if cursor:
            params["cursor"] = cursor
        try:
            data = _get_json(LIST_URL, params)
        except Exception as e:  # noqa: BLE001 — fail open, caller falls back
            log.warning("Hexagon list fetch failed: %s", e)
            break
        ok = True
        works = data.get("works") or []
        if not works:
            break
        oldest: date | None = None
        for w in works:
            if not isinstance(w, dict):
                continue
            d = _work_date(w)
            if d and (oldest is None or d < oldest):
                oldest = d
            if (w.get("status") or "published") != "published":
                continue
            if d is None or not (start <= d <= end):
                continue
            if not _subject_match(w.get("subject"), w.get("crossListSubjects"),
                                  subjects, include_cross_listed):
                continue
            p = _work_to_paper(w)
            if p and p.paper_id not in seen:
                seen.add(p.paper_id)
                papers.append(p)
                if len(papers) >= max_works:
                    break
        if len(papers) >= max_works:
            break
        page = data.get("page") or {}
        cursor = page.get("next_cursor")
        if not page.get("has_more") or not cursor:
            break
        # The list is newest-first: a page that already reaches past the window
        # means every later page is older still.
        if oldest is not None and oldest < start:
            break
        _pause()
    log.info("hexagon list %s..%s: %d works", start, end, len(papers))
    return papers, ok


# ── Atom query path (fallback) ────────────────────────────────────────────────

def _atom_entry_to_paper(entry: ET.Element) -> Paper | None:
    """Map one Atom ``<entry>`` from ``/api/query`` onto :class:`Paper`."""
    ident = normalize_hexagon_id(
        entry.findtext(f"{MATHLAKE_NS}identifier")
        or entry.findtext(f"{ATOM}id")
        or ""
    )
    if not ident:
        return None
    authors: list[str] = []
    affiliations: list[str] = []
    for a in entry.findall(f"{ATOM}author"):
        name = (a.findtext(f"{ATOM}name") or "").strip()
        if name:
            authors.append(name)
        aff = (a.findtext(f"{ARXIV_NS}affiliation") or "").strip()
        if aff:
            affiliations.append(aff)
    cats = _categories(
        (entry.find(f"{ARXIV_NS}primary_category") or ET.Element("x")).get("term"),
        [c.get("term") or "" for c in entry.findall(f"{ATOM}category")],
    )
    record = (entry.findtext(f"{ATOM}id") or "").strip()
    pdf = ""
    for link in entry.findall(f"{ATOM}link"):
        if (link.get("title") or "") == "pdf" or \
                (link.get("type") or "") == "application/pdf":
            pdf = link.get("href") or ""
            break
    tools = [
        {"name": t.get("name"), "version": t.get("version")}
        for t in entry.findall(f"{MATHLAKE_NS}tool")
    ]
    published = _as_date(entry.findtext(f"{ATOM}published"))
    return Paper(
        source="hexagon",
        paper_id=_paper_id(ident),
        title=" ".join((entry.findtext(f"{ATOM}title") or "").split()),
        authors=authors,
        abstract=" ".join((entry.findtext(f"{ATOM}summary") or "").split()),
        url=record or f"{SITE}/abs/{ident}",
        categories=cats,
        published=published.isoformat() if published else None,
        venue=_venue(entry.findtext(f"{MATHLAKE_NS}authorshipMode"), None, tools),
        affiliations=affiliations,
        institutions=_split_affiliations(affiliations),
        pdf_url=pdf or f"{SITE}/pdf/{ident}",
    )


def _fetch_atom(start: date, end: date, *, subjects: set[str],
                include_cross_listed: bool, max_works: int) -> list[Paper]:
    """Fallback fetch: page the arXiv-compatible Atom query newest-first.

    The query API has no date filter, so results are walked in submittedDate
    order and filtered client-side against the window.
    """
    papers: list[Paper] = []
    seen: set[str] = set()
    step = min(PAGE_MAX, max_works)
    offset = 0
    while offset < max_works:
        params = {
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": offset,
            "max_results": step,
        }
        try:
            root = ET.fromstring(_get_text(QUERY_URL, params))
        except Exception as e:  # noqa: BLE001 — fail open
            log.warning("Hexagon Atom query failed at offset %d: %s", offset, e)
            break
        entries = root.findall(f"{ATOM}entry")
        if not entries:
            break
        oldest: date | None = None
        for entry in entries:
            d = _as_date(entry.findtext(f"{ATOM}published"))
            if d and (oldest is None or d < oldest):
                oldest = d
            p = _atom_entry_to_paper(entry)
            if not p or p.paper_id in seen:
                continue
            if not p.published or not (start.isoformat() <= p.published <= end.isoformat()):
                continue
            if not _subject_match(p.categories[0] if p.categories else "",
                                  p.categories[1:], subjects, include_cross_listed):
                continue
            seen.add(p.paper_id)
            papers.append(p)
            if len(papers) >= max_works:
                break
        offset += len(entries)
        if len(entries) < step or (oldest is not None and oldest < start):
            break
        _pause()
    log.info("hexagon atom %s..%s: %d works", start, end, len(papers))
    return papers


# ── public interface ──────────────────────────────────────────────────────────

def fetch_all(cfg: dict, for_date: date | None = None) -> list[Paper]:
    """Fetch every Hexagon work published in the configured window.

    Config keys (``config/sources.yaml`` → ``hexagon``): ``subjects`` (empty =
    everything), ``include_cross_listed``, ``lookback_days``, ``max_works``.
    """
    subjects = {s.strip() for s in (cfg.get("subjects") or []) if s and s.strip()}
    include_cross = bool(cfg.get("include_cross_listed", True))
    try:
        max_works = max(1, int(cfg.get("max_works", 300)))
    except (TypeError, ValueError):
        max_works = 300
    try:
        lookback = max(0, int(cfg.get("lookback_days", 3)))
    except (TypeError, ValueError):
        lookback = 3
    start, end = _date_window(for_date, lookback)
    log.info("hexagon: fetching works published %s..%s (subjects=%s)",
             start, end, ", ".join(sorted(subjects)) or "all")

    papers, ok = _fetch_list(start, end, subjects=subjects,
                             include_cross_listed=include_cross,
                             max_works=max_works)
    if not papers:
        # Same idea as the arXiv RSS → API fallback: the list endpoint is the
        # fast path, the query API the reliable one — and an empty list is also
        # worth double-checking on the other path, since at ~10 works/day one
        # extra request costs nothing.
        log.warning("Hexagon list yielded 0 works for %s..%s%s — trying the Atom query",
                    start, end, " (request failed)" if not ok else "")
        papers = _fetch_atom(start, end, subjects=subjects,
                             include_cross_listed=include_cross,
                             max_works=max_works)
    log.info("hexagon: %d works in %s..%s", len(papers), start, end)
    return papers
