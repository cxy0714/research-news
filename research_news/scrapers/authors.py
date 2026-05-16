"""Author tracking via Semantic Scholar.

Resolves author names → S2 author IDs (cached), then pulls recent papers.
Free, no key required for low volume; add SEMANTIC_SCHOLAR_API_KEY for higher rate limits.
"""
from __future__ import annotations

import json
import logging
import os
import time
from datetime import date, timedelta
from pathlib import Path

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models import Paper

log = logging.getLogger(__name__)

S2_BASE = "https://api.semanticscholar.org/graph/v1"
CACHE_FILE = Path("data/authors_resolved.json")


def _headers() -> dict:
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    return {"x-api-key": key} if key else {}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=10))
def _get(path: str, params: dict | None = None) -> dict:
    with httpx.Client(timeout=30, headers=_headers()) as c:
        r = c.get(f"{S2_BASE}{path}", params=params)
        r.raise_for_status()
        return r.json()


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    return {}


def _save_cache(d: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(
        json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def resolve_author(name: str, affiliation_hint: str | None = None) -> str | None:
    cache = _load_cache()
    if name in cache:
        return cache[name]
    try:
        data = _get(
            "/author/search",
            {"query": name, "limit": 5, "fields": "name,affiliations,paperCount"},
        )
        candidates = data.get("data", [])
        if not candidates:
            return None
        # Prefer the candidate whose affiliation matches the hint.
        if affiliation_hint:
            for c in candidates:
                affs = " ".join(c.get("affiliations") or [])
                if affiliation_hint.lower() in affs.lower():
                    cache[name] = c["authorId"]
                    _save_cache(cache)
                    return c["authorId"]
        # Otherwise pick the one with the most papers.
        best = max(candidates, key=lambda c: c.get("paperCount", 0))
        cache[name] = best["authorId"]
        _save_cache(cache)
        return best["authorId"]
    except Exception as e:
        log.warning("author resolution failed for %s: %s", name, e)
        return None


def recent_papers(author_id: str, lookback_days: int = 14) -> list[Paper]:
    cutoff = date.today() - timedelta(days=lookback_days)
    fields = "title,abstract,authors,year,publicationDate,venue,externalIds,url"
    data = _get(
        f"/author/{author_id}/papers",
        {"limit": 20, "fields": fields, "sort": "publicationDate:desc"},
    )
    out: list[Paper] = []
    for p in data.get("data", []):
        pub = p.get("publicationDate")
        if pub:
            try:
                if date.fromisoformat(pub) < cutoff:
                    continue
            except ValueError:
                pass
        out.append(
            Paper(
                source="semantic_scholar",
                paper_id=p.get("paperId") or p.get("externalIds", {}).get("DOI", ""),
                title=p.get("title") or "",
                authors=[a.get("name", "") for a in (p.get("authors") or [])],
                abstract=p.get("abstract") or "",
                url=p.get("url") or "",
                categories=[],
                published=pub,
                venue=p.get("venue"),
            )
        )
    return out


def fetch_all(authors_cfg: dict, lookback_days: int = 14) -> list[Paper]:
    out: list[Paper] = []
    for entry in authors_cfg.get("authors", []):
        name = entry["name"]
        aid = entry.get("semantic_scholar_id") or resolve_author(
            name, entry.get("affiliation_hint")
        )
        if not aid:
            log.warning("could not resolve author %s", name)
            continue
        try:
            out.extend(recent_papers(aid, lookback_days=lookback_days))
        except Exception as e:
            log.warning("recent_papers failed for %s (%s): %s", name, aid, e)
        time.sleep(1.0)   # be polite to the free tier
    return out
