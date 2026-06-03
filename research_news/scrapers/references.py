"""Fetch the key cited works of a paper from Semantic Scholar.

Used by the deep-read step: feeding the abstracts of the papers an
introduction actually leans on lets the model build a small *survey* of the
direction (history, sub-threads, tensions) instead of guessing from titles.

Free without a key (heavily rate-limited); set SEMANTIC_SCHOLAR_API_KEY for
higher limits. Fail-open everywhere: any network/parse error returns nothing
and the deep read proceeds on the PDF alone.
"""
from __future__ import annotations

import logging
import os
import re

import httpx
from tenacity import Retrying, retry_if_exception, stop_after_attempt, wait_random_exponential

log = logging.getLogger(__name__)

S2_BASE = "https://api.semanticscholar.org/graph/v1"


def should_retry_http(exc: BaseException) -> bool:
    """Retry only *transient* failures: 429 (rate limit), 5xx, network/timeout.

    A 404 (paper not yet indexed — common for same-day arXiv posts) or any
    other 4xx is permanent, so we don't waste two more round-trips on it.
    Shared with the OpenAlex scraper so both report the real cause.
    """
    if isinstance(exc, httpx.HTTPStatusError):
        code = exc.response.status_code
        return code == 429 or code >= 500
    return isinstance(exc, (httpx.TransportError, httpx.TimeoutException))

# Fields we ask S2 for on each cited paper. `isInfluential` + `intents` let us
# rank "core" citations (methodological / background) above passing mentions.
_REF_FIELDS = "title,abstract,year,authors,externalIds,venue,citationCount"


def _headers() -> dict:
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    return {"x-api-key": key} if key else {}


def extract_arxiv_id(*candidates: str | None) -> str | None:
    """Pull a bare arXiv id (e.g. 2401.01234) from a url or id string."""
    for c in candidates:
        if not c:
            continue
        # New-style id, optionally with version, possibly embedded in a URL.
        m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", c)
        if m:
            return m.group(1)
        # Old-style id like math.ST/0123456 or hep-th/9901001.
        m = re.search(r"([a-z\-]+(?:\.[A-Z]{2})?/\d{7})", c)
        if m:
            return m.group(1)
    return None


def _env_int(name: str, default: int) -> int:
    try:
        return max(1, int(os.environ.get(name, str(default))))
    except ValueError:
        return default


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, str(default)))
    except ValueError:
        return default


def _do_get(path: str, params: dict) -> dict:
    with httpx.Client(timeout=30, headers=_headers()) as c:
        r = c.get(f"{S2_BASE}{path}", params=params)
        r.raise_for_status()
        return r.json()


def _get(path: str, params: dict) -> dict:
    """GET with patient, jittered retry on 429/5xx/network.

    Semantic Scholar refused our API-key request, so we live on the shared
    unauthenticated pool where 429s are frequent. The lever we have left is to
    retry more patiently: more attempts + longer, *jittered* backoff (so we
    don't hammer the shared pool in lockstep with everyone else). Tunable via
    S2_FETCH_ATTEMPTS / S2_MAX_BACKOFF; read at call time so .env takes effect.
    """
    retryer = Retrying(
        retry=retry_if_exception(should_retry_http),
        stop=stop_after_attempt(_env_int("S2_FETCH_ATTEMPTS", 6)),
        wait=wait_random_exponential(multiplier=1.5, max=_env_float("S2_MAX_BACKOFF", 30.0)),
        reraise=True,  # surface the real HTTPStatusError, not an opaque RetryError
    )
    return retryer(_do_get, path, params)


def fetch_references(arxiv_id: str, *, fetch_limit: int = 100) -> list[dict]:
    """Return cited-paper records (raw S2 `references` payload rows).

    Each row has `isInfluential`, `intents`, `contexts`, and `citedPaper`.
    Returns [] on any failure.
    """
    try:
        data = _get(
            f"/paper/arXiv:{arxiv_id}/references",
            {"fields": f"isInfluential,intents,contexts,{_REF_FIELDS}", "limit": fetch_limit},
        )
        return data.get("data", []) or []
    except httpx.HTTPStatusError as e:  # fail open, deep read still works
        code = e.response.status_code
        hint = " (paper not indexed yet?)" if code == 404 else (" (rate limited)" if code == 429 else "")
        log.info("reference fetch failed for arXiv:%s: HTTP %s%s", arxiv_id, code, hint)
        return []
    except Exception as e:  # noqa: BLE001 — network/parse error, also fail open
        log.info("reference fetch failed for arXiv:%s: %s", arxiv_id, e)
        return []


def _ref_rank_key(row: dict) -> tuple:
    """Sort key: influential first, then by how the intro uses it, then cites."""
    cited = row.get("citedPaper") or {}
    intents = set(row.get("intents") or [])
    # background / methodology citations matter most for a survey; result-only
    # comparisons matter less.
    intent_weight = (
        2 if {"methodology", "background"} & intents else (1 if intents else 0)
    )
    return (
        1 if row.get("isInfluential") else 0,
        intent_weight,
        cited.get("citationCount") or 0,
    )


def select_key_references(rows: list[dict], *, top_n: int = 25) -> list[dict]:
    """Keep the most survey-relevant cited papers that have an abstract."""
    usable = [r for r in rows if (r.get("citedPaper") or {}).get("abstract")]
    usable.sort(key=_ref_rank_key, reverse=True)
    return usable[:top_n]


def format_references_block(rows: list[dict], *, top_n: int = 25, max_chars: int = 60_000) -> str:
    """Render selected references as a Markdown block for the deep-read prompt.

    Returns "" when there is nothing usable, so callers can append unconditionally.
    """
    selected = select_key_references(rows, top_n=top_n)
    if not selected:
        return ""
    lines = [
        "## 主要被引论文（已检索，按重要性排序）",
        "（以下是本文 introduction / 参考文献里较核心的被引工作及其摘要，"
        "用来帮助你梳理这个方向的发展脉络；isInfluential 表示 Semantic Scholar "
        "判断为高影响引用。）",
        "",
    ]
    for i, row in enumerate(selected, 1):
        cited = row.get("citedPaper") or {}
        authors = ", ".join(a.get("name", "") for a in (cited.get("authors") or [])[:4])
        if len(cited.get("authors") or []) > 4:
            authors += " et al."
        year = cited.get("year") or "?"
        title = cited.get("title") or "(untitled)"
        flags = []
        if row.get("isInfluential"):
            flags.append("influential")
        if row.get("intents"):
            flags.append("/".join(row["intents"]))
        flag_str = f" [{'; '.join(flags)}]" if flags else ""
        lines.append(f"### [{i}] {title} ({authors}, {year}){flag_str}")
        # How *this* paper cites it — the author's own read of the work.
        contexts = [c for c in (row.get("contexts") or []) if c.strip()]
        if contexts:
            lines.append(f"- 本文引用语境：{contexts[0].strip()[:400]}")
        abstract = (cited.get("abstract") or "").strip()
        if abstract:
            lines.append(f"- 摘要：{abstract[:1200]}")
        lines.append("")
        if sum(len(x) for x in lines) > max_chars:
            lines.append("（其余被引文献从略。）")
            break
    return "\n".join(lines).rstrip() + "\n"


# ── OpenAlex fallback ───────────────────────────────────────────────────────
# Semantic Scholar declined our API key, so on heavy-throttle days S2 may fail
# or return references with no abstracts. OpenAlex (free, no key, polite pool
# with OPENALEX_MAILTO) is a second source. It has no per-citation signals
# (isInfluential / intents / contexts), so those come back empty and the
# ranking falls back to citation count — but the abstracts let the survey
# section still get built, and the edges still feed the citation graph.

OPENALEX_BASE = "https://api.openalex.org"

# Fields we pull per cited work. abstract_inverted_index is OpenAlex's abstract
# representation; we reconstruct plain text from it.
_OA_SELECT = (
    "id,ids,doi,title,display_name,publication_year,cited_by_count,"
    "abstract_inverted_index,authorships,primary_location"
)


def _openalex_params(extra: dict) -> dict:
    params = dict(extra)
    mailto = os.environ.get("OPENALEX_MAILTO")
    if mailto:
        params["mailto"] = mailto
    return params


def _do_openalex_get(path: str, params: dict) -> dict:
    with httpx.Client(timeout=30) as c:
        r = c.get(f"{OPENALEX_BASE}{path}", params=_openalex_params(params))
        r.raise_for_status()
        return r.json()


def _openalex_get(path: str, params: dict) -> dict:
    retryer = Retrying(
        retry=retry_if_exception(should_retry_http),
        stop=stop_after_attempt(_env_int("OPENALEX_FETCH_ATTEMPTS", 4)),
        wait=wait_random_exponential(multiplier=1.5, max=_env_float("OPENALEX_MAX_BACKOFF", 20.0)),
        reraise=True,
    )
    return retryer(_do_openalex_get, path, params)


def _reconstruct_abstract(inv_index: dict | None) -> str:
    """Rebuild plain-text abstract from OpenAlex's word -> [positions] index."""
    if not inv_index:
        return ""
    pairs = [(pos, word) for word, positions in inv_index.items() for pos in positions]
    pairs.sort()
    return " ".join(word for _, word in pairs)


def _bare_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    doi = doi.strip()
    for pre in ("https://doi.org/", "http://doi.org/", "doi.org/"):
        if doi.lower().startswith(pre):
            return doi[len(pre):] or None
    return doi or None


def _openalex_work_to_cited(work: dict) -> dict:
    """Normalize an OpenAlex work into the same `citedPaper` shape S2 returns,
    so downstream ranking / formatting / edge extraction work unchanged."""
    doi = _bare_doi(work.get("doi"))
    ext: dict = {}
    if doi:
        ext["DOI"] = doi
        # arXiv works carry the 10.48550/arXiv.<id> DOI — recover the bare id.
        m = re.match(r"10\.48550/arxiv\.(.+)$", doi, re.IGNORECASE)
        if m:
            ext["ArXiv"] = m.group(1)
    oa_id = ((work.get("ids") or {}).get("openalex") or work.get("id") or "")
    authors = [
        {"name": (a.get("author") or {}).get("display_name")}
        for a in (work.get("authorships") or [])
        if (a.get("author") or {}).get("display_name")
    ]
    venue = ((work.get("primary_location") or {}).get("source") or {}).get("display_name")
    return {
        "paperId": oa_id.rsplit("/", 1)[-1] or None,
        "title": work.get("title") or work.get("display_name"),
        "abstract": _reconstruct_abstract(work.get("abstract_inverted_index")),
        "year": work.get("publication_year"),
        "authors": authors,
        "externalIds": ext,
        "citationCount": work.get("cited_by_count"),
        "venue": venue,
    }


def fetch_references_openalex(arxiv_id: str, *, fetch_limit: int = 100) -> list[dict]:
    """Return cited-work rows from OpenAlex, in the same shape as S2 rows.

    Two steps: the paper's `referenced_works` (OpenAlex ids), then a batched
    metadata fetch (≤50 ids per request — OpenAlex's pipe-OR limit). [] on any
    failure.
    """
    doi = f"10.48550/arXiv.{arxiv_id}"
    try:
        head = _openalex_get(f"/works/doi:{doi}", {"select": "referenced_works"})
    except httpx.HTTPStatusError as e:
        code = e.response.status_code
        hint = " (not indexed yet?)" if code == 404 else ""
        log.info("OpenAlex refs: lookup failed for arXiv:%s: HTTP %s%s", arxiv_id, code, hint)
        return []
    except Exception as e:  # noqa: BLE001 — fail open
        log.info("OpenAlex refs: lookup failed for arXiv:%s: %s", arxiv_id, e)
        return []

    ref_ids = [u.rsplit("/", 1)[-1] for u in (head.get("referenced_works") or [])]
    ref_ids = [r for r in ref_ids if r][:fetch_limit]
    if not ref_ids:
        return []

    rows: list[dict] = []
    for i in range(0, len(ref_ids), 50):
        chunk = ref_ids[i:i + 50]
        try:
            data = _openalex_get(
                "/works",
                {"filter": "ids.openalex:" + "|".join(chunk),
                 "per-page": 50, "select": _OA_SELECT},
            )
        except Exception as e:  # noqa: BLE001 — keep whatever we already have
            log.info("OpenAlex refs: batch fetch failed for arXiv:%s: %s", arxiv_id, e)
            continue
        for w in data.get("results", []) or []:
            rows.append({
                "isInfluential": False,  # OpenAlex has no such signal
                "intents": [],
                "contexts": [],
                "citedPaper": _openalex_work_to_cited(w),
            })
    return rows


def fetch_references_best(arxiv_id: str, *, fetch_limit: int = 100) -> tuple[list[dict], str]:
    """Best available references: prefer S2 (richer signals); fall back to
    OpenAlex when S2 yields no abstract-bearing references.

    Returns (rows, source) where source is "s2" / "openalex" / "none".
    """
    s2 = fetch_references(arxiv_id, fetch_limit=fetch_limit)
    if select_key_references(s2):
        return s2, "s2"
    oa = fetch_references_openalex(arxiv_id, fetch_limit=fetch_limit)
    if select_key_references(oa):
        return oa, "openalex"
    # Neither yields usable abstracts; still return edges for the graph,
    # preferring S2's richer rows when present.
    if s2:
        return s2, "s2"
    if oa:
        return oa, "openalex"
    return [], "none"
