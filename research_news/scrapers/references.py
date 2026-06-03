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
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

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


@retry(
    retry=retry_if_exception(should_retry_http),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=10),
    reraise=True,  # surface the real HTTPStatusError, not an opaque RetryError
)
def _get(path: str, params: dict) -> dict:
    with httpx.Client(timeout=30, headers=_headers()) as c:
        r = c.get(f"{S2_BASE}{path}", params=params)
        r.raise_for_status()
        return r.json()


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
