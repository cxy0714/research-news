"""Import the Online Causal Inference Seminar (OCIS) catalog into the talk pipeline.

OCIS lists its past talks on Google Sites, one sub-page per season, each talk
carrying (usually) a YouTube video + an arXiv link + slides:
    https://sites.google.com/view/ocis/past-talks/<season>-<year>-talks

Google Sites is JS-ish and bot-hostile (server-side fetchers get 403), so this is
meant to run **locally**, like ingest. Two robust halves:

- **Pure helpers** (regex link extraction, Google `url?q=` redirect unwrapping,
  host classification, row → talks.yaml entry): DOM-agnostic — they scan the raw
  HTML string for the URL patterns, so they don't depend on Google's markup. Unit
  tested, run anywhere, and work on a saved page (`--html`).
- **Heavy** (`fetch_html`, `extract_talks` LLM call): fetch over the network +
  associate links to talks with the LLM. Local + API key.

Output: a catalog at data/ocis_catalog.json (every talk, incl. arxiv/slides) and
an auto-generated config/talks.ocis.yaml that the talk pipeline reads alongside
the hand-curated config/talks.yaml.
"""
from __future__ import annotations

import json
import logging
import re
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

PAST_TALKS = "https://sites.google.com/view/ocis/past-talks"
SEASONS = ("winter", "spring", "summer", "fall")
VENUE = "OCIS (Online Causal Inference Seminar)"

CATALOG_PATH = Path("data/ocis_catalog.json")
OCIS_TALKS_YAML = Path("config/talks.ocis.yaml")

_URL_RE = re.compile(r"https?://[^\s\"'<>\\)]+")
_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,6})(?:v\d+)?")


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-") or "x"


# ── pure helpers ──────────────────────────────────────────────────────────────

def unwrap_redirect(url: str) -> str:
    """Google Sites wraps external links as https://www.google.com/url?q=<real>&…
    Decode that back to the real URL; pass anything else through unchanged."""
    if not url:
        return ""
    try:
        p = urlparse(url)
    except ValueError:
        return url
    if p.netloc.endswith("google.com") and p.path == "/url":
        q = parse_qs(p.query).get("q")
        if q:
            return q[0]
    return url


def classify_link(url: str) -> str:
    """One of video | arxiv | doi | slides | other."""
    u = (url or "").lower()
    if "youtube.com/watch" in u or "youtu.be/" in u:
        return "video"
    if "arxiv.org/abs/" in u or "arxiv.org/pdf/" in u:
        return "arxiv"
    if "doi.org/" in u:
        return "doi"
    # Real slide decks only — not Google Sites' own Drive viewer chrome
    # (bare drive.google.com / drive.google.com/viewer show up on every page).
    if "docs.google.com/presentation" in u:
        return "slides"
    if "drive.google.com/file/" in u or "drive.google.com/open" in u or "drive.google.com/uc" in u:
        return "slides"
    if u.split("?")[0].endswith(".pdf"):
        return "slides"
    return "other"


def extract_links(html: str) -> list[dict]:
    """Scan raw HTML for every URL, unwrap Google redirects, classify by host.

    DOM-agnostic on purpose: the talk links live somewhere in the page bytes
    regardless of how Google nests them, so we match the URL strings directly.
    Returns [{'url', 'kind'}] for video/arxiv/doi/slides links (dedup, in order).
    """
    out: list[dict] = []
    seen: set[str] = set()
    for raw in _URL_RE.findall(html or ""):
        url = unwrap_redirect(raw.rstrip(".,;)"))
        kind = classify_link(url)
        if kind == "other" or url in seen:
            continue
        seen.add(url)
        out.append({"url": url, "kind": kind})
    return out


def clean_text_with_links(html: str, max_chars: int = 40000) -> str:
    """Visible page text with each anchor inlined as 'text <unwrapped-href>', so
    the LLM can see which link sits next to which talk."""
    soup = BeautifulSoup(html or "", "lxml")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    for a in soup.find_all("a"):
        href = unwrap_redirect(a.get("href") or "")
        label = a.get_text(" ", strip=True)
        a.replace_with(f"{label} <{href}>" if href.startswith("http") else label)
    text = soup.get_text("\n", strip=True)
    lines = [ln for ln in (s.strip() for s in text.splitlines()) if ln]
    cleaned = "\n".join(lines)
    return cleaned[:max_chars] + ("\n...[truncated]" if len(cleaned) > max_chars else "")


# Each talk block on an OCIS season page starts with a weekday-date header and
# carries `- Speaker:` / `- Title:` markers and a trailing
# `[Paper <url>][Slides <url>][Video <url>]` row. We parse that structure
# directly — more reliable than LLM association and works fully offline.
_HEADER_RE = re.compile(
    r"^(?:Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day,\s+"
    r"([A-Z][a-z]{2,8}\.?\s+\d{1,2},\s+\d{4})\s*:"
)
_MARKER_RE = re.compile(r"^-\s*([A-Za-z][A-Za-z /]*?):\s*(.*)$")
# Bare labels (no leading dash) used on older pages. Allowlisted so a normal
# title containing a colon ("So Many Choices: ...") isn't mistaken for a marker.
_BARE_MARKER_RE = re.compile(
    r"^(Speaker|Title|Abstract|Discussants?|Panelists?|Details|Time)\s*:\s*(.*)$", re.I
)
_INLINE_URL_RE = re.compile(r"\s*<(https?://[^>]+)>")
_WEBINAR_NOISE = re.compile(r"OCIS\+|joint webinar|INI\b", re.I)
_QUOTED_RE = re.compile(r'["“”](.+?)["“”]', re.DOTALL)
_CONNECTOR_RE = re.compile(r"^(and|&|,|with)+$", re.I)


def _norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\xa0", " ").replace("​", "")).strip()


def _clean_inline(s: str) -> str:
    """Drop inlined `<url>` tokens and normalize whitespace (keeps parentheses)."""
    return _norm_ws(_INLINE_URL_RE.sub("", s))


def _clean_speaker(s: str) -> str:
    """Speaker name(s): drop inlined urls + `(affiliation)`, keep `&` for joints."""
    s = _INLINE_URL_RE.sub("", s)
    s = re.sub(r"\([^)]*\)", "", s)
    return _norm_ws(s).strip(" ;,&")


def parse_talks_structured(text: str) -> list[dict]:
    """Deterministically parse an OCIS page (the inlined-link text from
    ``clean_text_with_links``) into talk rows. No LLM, no network.

    Handles the layouts OCIS has used over the years: `- Speaker:` / `- Title:`
    markers (current season pages), speaker inline on the date header, and
    quoted titles in an unmarked preamble (older pages). Links (video / arxiv /
    slides) are scanned across the whole block, so they're captured regardless of
    layout. Non-talk blocks (panels with no speaker/title/links) are skipped.
    """
    lines = text.splitlines()
    heads = [i for i, ln in enumerate(lines) if _HEADER_RE.match(ln)]
    rows: list[dict] = []
    for k, i in enumerate(heads):
        j = heads[k + 1] if k + 1 < len(heads) else len(lines)
        block = lines[i:j]
        date_str = _HEADER_RE.match(block[0]).group(1)
        # Older pages put the speaker after the date colon on the header line.
        after = block[0].split(":", 1)[1] if ":" in block[0] else ""
        header_speaker = _clean_speaker(_WEBINAR_NOISE.sub("", after))

        fields: dict[str, list[str]] = {}
        preamble: list[str] = []      # unmarked lines before any marker/links
        cur: str | None = None
        links_started = False
        for ln in block[1:]:
            s = ln.lstrip()
            # Everything from the trailing `[Paper <url>][Slides <url>]...` row on
            # is links + page footer — stop absorbing text (links are scanned
            # separately over the whole block).
            if links_started:
                continue
            if s.startswith(("[", "]")):
                links_started = True
                cur = None
                continue
            m = _MARKER_RE.match(ln) or _BARE_MARKER_RE.match(ln)
            if m:
                label = m.group(1).strip().lower()
                if label.startswith("panel"):
                    cur = "_skip"      # drop panel lines (not a single-speaker talk)
                else:
                    cur = label        # speaker / title / abstract / discussant / ...
                    fields[cur] = [m.group(2)] if m.group(2).strip() else []
                continue
            if cur is None:
                preamble.append(ln)
            elif cur != "_skip":
                fields[cur].append(ln)

        sp_field = fields.get("speaker", [])
        ti_field = fields.get("title", [])
        has_title = bool(ti_field)
        # Preamble minus pure "(affiliation)" lines and bare connectors ("and"),
        # url-stripped.
        pre = [p for p in (_clean_inline(x) for x in preamble
                           if not x.lstrip().startswith("(")) if p and not _CONNECTOR_RE.match(p)]

        # Speaker: a `Speaker:` marker's first line (later lines are an overflow
        # title), else the date-header remainder, else the preamble — all of it
        # when the title lives elsewhere, otherwise just the first (name) line.
        title_extra: list[str] = []
        if sp_field:
            speaker = _clean_speaker(sp_field[0])
            title_extra = sp_field[1:]
        elif header_speaker:
            speaker = header_speaker
        elif pre and (has_title or len(pre) == 1):
            speaker = _clean_speaker(", ".join(pre))
        elif pre:
            speaker = _clean_speaker(pre[0])
        else:
            speaker = ""

        # Title: a `Title:` marker, else a quoted string, else the leftover text
        # (speaker-field overflow, or the preamble lines that aren't the speaker —
        # all of it when the speaker came from a marker/header, else pre[1:]).
        title = _clean_inline(" ".join(ti_field))
        if not title:
            quoted = _QUOTED_RE.search(" ".join(preamble) + " " + " ".join(title_extra))
            if quoted:
                title = _clean_inline(quoted.group(1))
            else:
                cands = list(title_extra) + (pre if (sp_field or header_speaker) else pre[1:])
                cands = [c for c in (_clean_inline(x) for x in cands)
                         if c and not _CONNECTOR_RE.match(c)]
                title = " ".join(cands)
        title = title.strip(" \"“”'")

        abstract = _clean_inline(" ".join(fields.get("abstract", [])))
        discussant = _clean_speaker(" ".join(fields.get("discussant", [])))

        kinds: dict[str, str] = {}
        for u in _INLINE_URL_RE.findall("\n".join(block)):
            kind = classify_link(u)
            if kind in ("video", "arxiv", "doi", "slides") and kind not in kinds:
                kinds[kind] = u

        row = {
            "date": normalize_date(date_str),
            "speaker": speaker or None,
            "title": title or None,
            "abstract": abstract or None,
            "discussant": discussant or None,
            "video": kinds.get("video"),
            "arxiv": kinds.get("arxiv") or kinds.get("doi"),
            "slides": kinds.get("slides"),
        }
        # Keep only blocks that are actually a talk (have a link or a title).
        if row["video"] or row["arxiv"] or row["title"]:
            rows.append(row)
    return rows


def arxiv_id_from_url(url: str) -> str | None:
    m = _ARXIV_ID_RE.search(url or "")
    return m.group(1) if m else None


def normalize_date(value) -> str | None:
    """Best-effort ISO date. Returns YYYY-MM-DD when parseable, else the original
    trimmed string, else None."""
    s = str(value or "").strip()
    if not s:
        return None
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s
    for fmt in ("%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%m/%d/%Y", "%Y/%m/%d", "%B %Y"):
        try:
            from datetime import datetime
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    return s


def make_talk_id(row: dict) -> str:
    """Stable id for a talk row: ocis-<date>-<speaker> (falls back to title)."""
    d = normalize_date(row.get("date")) or ""
    d = d if re.match(r"^\d{4}-\d{2}-\d{2}$", d) else (d[:10] if d else "")
    who = _slug(row.get("speaker") or row.get("title") or "talk")[:40]
    return "-".join(p for p in ("ocis", d, who) if p)


def season_url(slug: str) -> str:
    """'spring-2024' → the season sub-page URL ('-talks' suffix added if absent)."""
    slug = slug.strip().lower()
    if not slug.endswith("-talks"):
        slug += "-talks"
    return f"{PAST_TALKS}/{slug}"


def default_season_urls(start_year: int = 2020, end_year: int | None = None) -> list[str]:
    end_year = end_year or date.today().year
    return [
        f"{PAST_TALKS}/{season}-{year}-talks"
        for year in range(start_year, end_year + 1)
        for season in SEASONS
    ]


def row_to_talk_entry(row: dict) -> dict | None:
    """Convert an extracted talk row into a config/talks.yaml entry. Requires a
    video (no video → nothing to transcribe); returns None otherwise."""
    video = (row.get("video") or "").strip()
    if not video or classify_link(video) != "video":
        return None
    entry: dict = {
        "id": make_talk_id(row),
        "url": video,
        "title": (row.get("title") or "").strip() or None,
        "speaker": (row.get("speaker") or "").strip() or None,
        "venue": VENUE,
        "date": normalize_date(row.get("date")),
        "topic": "causal_inference",
        "language": "en",
        "discussant": (row.get("discussant") or "").strip() or None,
        "abstract": (row.get("abstract") or "").strip() or None,
    }
    aid = arxiv_id_from_url(row.get("arxiv") or "")
    if aid:
        entry["papers"] = [aid]
    elif (row.get("arxiv") or "").lower().startswith(("10.", "http")) and "doi.org" in (row.get("arxiv") or "").lower():
        entry["papers"] = [row["arxiv"].split("doi.org/")[-1]]
    return {k: v for k, v in entry.items() if v is not None}


def dedupe_entries(entries: list[dict]) -> list[dict]:
    """Drop entries with a duplicate id (first wins) or no video URL."""
    out: list[dict] = []
    seen: set[str] = set()
    for e in entries:
        eid = e.get("id")
        if not eid or eid in seen or not e.get("url"):
            continue
        seen.add(eid)
        out.append(e)
    return out


# ── writers ───────────────────────────────────────────────────────────────────

def write_catalog(rows: list[dict], path: Path = CATALOG_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")


def merge_talk_entries(new_entries: list[dict], path: Path = OCIS_TALKS_YAML) -> list[dict]:
    """Merge freshly-parsed entries into the existing talks.ocis.yaml by id.

    Existing entries are kept (in order); a matching id gets the new non-empty
    fields filled in / refreshed (season pages are richer than the index, so they
    add abstract / discussant without dropping anything); new ids are appended.
    """
    existing: list[dict] = []
    if path.exists():
        cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        existing = cfg.get("talks", []) or []
    by_id: dict[str, dict] = {e["id"]: dict(e) for e in existing if e.get("id")}
    order: list[str] = [e["id"] for e in existing if e.get("id")]
    for ne in new_entries:
        eid = ne.get("id")
        if not eid:
            continue
        if eid in by_id:
            for k, v in ne.items():
                if v not in (None, "", []):
                    by_id[eid][k] = v
        else:
            by_id[eid] = ne
            order.append(eid)
    return [by_id[i] for i in order]


def write_talks_yaml(entries: list[dict], path: Path = OCIS_TALKS_YAML) -> None:
    """Write the auto-generated talks file the pipeline reads next to talks.yaml."""
    path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# AUTO-GENERATED by `python -m research_news.talks import-ocis`.\n"
        "# Do not hand-edit — re-run the importer to refresh. Hand-curated talks\n"
        "# (and asr_prompt_default) live in talks.yaml; the pipeline reads both.\n\n"
    )
    body = yaml.safe_dump({"talks": entries}, allow_unicode=True, sort_keys=False)
    path.write_text(header + body, encoding="utf-8")


# ── heavy: fetch + LLM ────────────────────────────────────────────────────────

def fetch_html(url: str, *, timeout: float = 30) -> str:
    """GET raw HTML with a browser UA (Google Sites blocks library UAs)."""
    import httpx
    ua = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
    with httpx.Client(timeout=timeout, headers={"User-Agent": ua}, follow_redirects=True) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def extract_talks(client, source: str, html: str, *, model: str | None = None) -> list[dict]:
    """LLM-associate the page's links into talk rows."""
    from ..llm.pipeline import _extract_json
    from ..llm.prompts import OCIS_EXTRACT_SYSTEM

    links = extract_links(html)
    text = clean_text_with_links(html)
    links_block = "\n".join(f"- [{lk['kind']}] {lk['url']}" for lk in links)
    user = (
        f"## Source: {source}\n\n"
        f"## Candidate URLs (pre-classified)\n{links_block}\n\n"
        f"## Page text (links inlined as `text <URL>`)\n{text}"
    )
    try:
        raw = client.chat(
            [
                {"role": "system", "content": OCIS_EXTRACT_SYSTEM},
                {"role": "user", "content": user},
            ],
            model=model,
            max_tokens=8000,
        )
        parsed = _extract_json(raw)
        if isinstance(parsed, dict):
            parsed = parsed.get("talks", parsed.get("data", []))
        return [r for r in parsed if isinstance(r, dict)] if isinstance(parsed, list) else []
    except Exception as e:  # noqa: BLE001
        log.warning("OCIS extraction failed for %s: %s", source, e)
        return []


def import_pages(
    *,
    urls: list[str] | None = None,
    html_files: list[str] | None = None,
    model: str | None = None,
    catalog_only: bool = False,
    limit: int | None = None,
    dry_run: bool = False,
    use_llm: bool = False,
) -> list[dict]:
    """Fetch / read the given OCIS pages, extract talk rows, write the catalog +
    talks.ocis.yaml. Returns the talk rows.

    Default extraction is the deterministic structured parser (no LLM, no API
    key) — OCIS season pages are regular. `use_llm=True` falls back to LLM
    association for irregular pages. `html_files` parses pages saved from a
    browser, so the whole import can run offline. Network/LLM only when used.
    """
    sources: list[tuple[str, str]] = []  # (label, html)
    for path in html_files or []:
        try:
            sources.append((path, Path(path).read_text(encoding="utf-8", errors="ignore")))
        except OSError as e:
            log.warning("cannot read %s: %s", path, e)
    for url in urls or []:
        try:
            sources.append((url, fetch_html(url)))
            log.info("fetched %s", url)
        except Exception as e:  # noqa: BLE001
            log.info("skip %s (%s)", url, e)  # 404 season pages are expected

    if not sources:
        log.warning("no OCIS pages fetched/read")
        return []

    if dry_run:
        for label, html in sources:
            links = extract_links(html)
            log.info("  %s: %d candidate link(s) (%d video, %d arxiv, %d slides)",
                     label, len(links),
                     sum(lk["kind"] == "video" for lk in links),
                     sum(lk["kind"] == "arxiv" for lk in links),
                     sum(lk["kind"] == "slides" for lk in links))
        return []

    client = None
    if use_llm:
        from dotenv import load_dotenv

        from ..llm.sjtu_client import SJTUClient
        load_dotenv()
        client = SJTUClient()

    rows: list[dict] = []
    for label, html in sources:
        if use_llm:
            page_rows = extract_talks(client, label, html, model=model)
        else:
            page_rows = parse_talks_structured(clean_text_with_links(html, max_chars=2_000_000))
            if not page_rows:
                log.warning("%s: structured parse found 0 talks — try --llm", label)
        log.info("  %s: %d talk(s)", label, len(page_rows))
        rows.extend(page_rows)

    if not rows:
        return rows
    if limit:
        rows = rows[:limit]
    write_catalog(rows)
    entries = dedupe_entries([e for r in rows if (e := row_to_talk_entry(r))])
    n_abstracts = sum(1 for e in entries if e.get("abstract"))
    log.info("OCIS import: %d talk(s), %d with video, %d with abstract → %s",
             len(rows), len(entries), n_abstracts, OCIS_TALKS_YAML)
    if not catalog_only:
        write_talks_yaml(merge_talk_entries(entries))
    return rows
