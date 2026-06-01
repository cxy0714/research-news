from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from typing import Any


@dataclass
class Paper:
    source: str            # "arxiv" | "semantic_scholar" | ...
    paper_id: str          # arXiv id, S2 paper id, DOI, etc.
    title: str
    authors: list[str]
    abstract: str
    url: str
    # Best-effort arXiv preprint link for journal papers (publisher URL stays in
    # `url`). Filled by the crossref scraper's arxiv title search; None when no
    # confident preprint match is found (or for arxiv-native papers).
    arxiv_url: str | None = None
    categories: list[str] = field(default_factory=list)
    published: str | None = None   # ISO date string
    venue: str | None = None
    # Author affiliation strings, when available (crossref / arXiv / OpenAlex).
    affiliations: list[str] = field(default_factory=list)
    # Set when an author is at a whitelisted (US News top-50) institution: the
    # matched institution name. Such papers are deep-read regardless of score.
    green_light_institution: str | None = None
    # Filled in by the LLM step:
    score: float | None = None
    score_reason: str | None = None
    summary_zh: str | None = None
    why_relevant: str | None = None
    topic: str | None = None              # one of llm.prompts.TOPICS
    key_techniques: list[str] = field(default_factory=list)
    novelty_flag: str | None = None       # new_theory|new_method|sharper_rate|...
    # Set True when the LLM summary could not be parsed cleanly (truncated or
    # garbled JSON). Used to flag a paper for re-running the summary step.
    summary_incomplete: bool = False
    # Journal issue metadata (set by crossref scraper):
    volume: str | None = None
    issue: str | None = None
    # Set when we download the PDF for high-relevance papers:
    pdf_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Event:
    source: str        # which conference/seminar page
    title: str
    date: str | None = None    # ISO date or freeform if unparseable
    location: str | None = None
    speaker: str | None = None
    url: str | None = None
    note: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
