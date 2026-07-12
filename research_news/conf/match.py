"""Match a conference talk (title + speaker) to its paper.

Queries BOTH OpenAlex (published works, with abstracts + authors, sometimes an
arXiv id) and the arXiv API (preprints), scores every candidate by title
similarity + speaker last-name overlap, and accepts the best only if it clears
a confidence bar. Never fabricates a match — below the bar => found=False, and
the reader falls back to an inference from the title.
"""
from __future__ import annotations

import logging
import os
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher

from ..scrapers import arxiv, openalex

log = logging.getLogger(__name__)

ACCEPT_THRESHOLD = float(os.environ.get("CONF_MATCH_THRESHOLD", "0.60"))

_STOP = {
    "a", "an", "the", "of", "for", "and", "or", "to", "in", "on", "with",
    "via", "under", "using", "based", "from", "by", "at", "is", "are",
}


def _norm_tokens(text: str) -> set[str]:
    text = re.sub(r"[^\w\s]", " ", (text or "").lower())
    return {w for w in text.split() if w and w not in _STOP and len(w) > 1}


def _last_name(name: str) -> str:
    parts = re.sub(r"[^\w\s]", " ", (name or "")).split()
    return parts[-1].lower() if parts else ""


def title_similarity(a: str, b: str) -> float:
    ta, tb = _norm_tokens(a), _norm_tokens(b)
    if not ta or not tb:
        return 0.0
    jac = len(ta & tb) / len(ta | tb)
    seq = SequenceMatcher(None, (a or "").lower(), (b or "").lower()).ratio()
    return 0.6 * jac + 0.4 * seq


def _author_overlap(speaker: str, authors: list[str]) -> float:
    ln = _last_name(speaker)
    if not ln:
        return 0.0
    return 1.0 if any(ln == _last_name(a) for a in authors) else 0.0


@dataclass
class Candidate:
    title: str
    authors: list[str]
    abstract: str
    arxiv_id: str | None
    doi: str | None
    url: str
    source: str  # "openalex" | "arxiv"


@dataclass
class MatchResult:
    found: bool
    candidate: Candidate | None
    score: float
    reason: str
    # kept for backward-compat with earlier read.py (paper.* access)
    paper: object = field(default=None)


def _gather_candidates(title: str) -> list[Candidate]:
    out: list[Candidate] = []
    for w in openalex.search_works_by_title(title, per_page=8):
        out.append(Candidate(
            title=w["title"], authors=w["authors"], abstract=w["abstract"],
            arxiv_id=w["arxiv_id"], doi=w["doi"], url=w["url"], source="openalex",
        ))
    for p in arxiv.search_by_title(title, max_results=6):
        out.append(Candidate(
            title=p.title, authors=p.authors, abstract=p.abstract,
            arxiv_id=p.paper_id, doi=None, url=p.url, source="arxiv",
        ))
    return out


def match_talk(title: str, speaker: str) -> MatchResult:
    cands = _gather_candidates(title)
    if not cands:
        return MatchResult(False, None, 0.0, "no candidates from any source")

    best: Candidate | None = None
    best_score = 0.0
    best_tsim = 0.0
    for c in cands:
        tsim = title_similarity(title, c.title)
        aov = _author_overlap(speaker, c.authors)
        blended = tsim + 0.18 * aov
        # Prefer a candidate that carries an arXiv id (PDF-readable) on ties.
        blended += 0.02 if c.arxiv_id else 0.0
        if blended > best_score:
            best_score, best, best_tsim = blended, c, tsim

    if best is not None and best_score >= ACCEPT_THRESHOLD:
        return MatchResult(True, best, best_score,
                           f"src={best.source} title_sim={best_tsim:.2f} "
                           f"blended={best_score:.2f}")
    return MatchResult(False, best, best_score,
                       f"below threshold (title_sim={best_tsim:.2f} "
                       f"blended={best_score:.2f} < {ACCEPT_THRESHOLD})")
