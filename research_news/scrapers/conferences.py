"""Conference / seminar page fetcher.

We don't write a parser per site. We fetch the page, strip to readable text,
and hand it to the LLM with instructions to extract structured events.
This is robust against site redesigns and easy to add new sources to.
"""
from __future__ import annotations

import logging

import httpx
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

log = logging.getLogger(__name__)

UA = "research-news/0.1 (+https://github.com/cxy0714/research-news)"


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=10))
def _get(url: str) -> str:
    with httpx.Client(timeout=30, headers={"User-Agent": UA}, follow_redirects=True) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def fetch_clean_text(url: str, max_chars: int = 20000) -> str:
    html = _get(url)
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    text = soup.get_text("\n", strip=True)
    # collapse blank lines
    lines = [ln for ln in (l.strip() for l in text.splitlines()) if ln]
    cleaned = "\n".join(lines)
    if len(cleaned) > max_chars:
        cleaned = cleaned[:max_chars] + "\n...[truncated]"
    return cleaned


def fetch_all(cfg: dict) -> list[dict]:
    """Returns a list of {name, url, kind, text} dicts; LLM extracts events later."""
    out = []
    for src in cfg.get("sources", []):
        try:
            text = fetch_clean_text(src["url"])
            out.append({**src, "text": text})
            log.info("fetched %s (%d chars)", src["name"], len(text))
        except Exception as e:
            log.warning("conference fetch failed for %s: %s", src["name"], e)
    return out
