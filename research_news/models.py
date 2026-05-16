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
    categories: list[str] = field(default_factory=list)
    published: str | None = None   # ISO date string
    venue: str | None = None
    # Filled in by the LLM step:
    score: float | None = None
    score_reason: str | None = None
    summary_zh: str | None = None
    why_relevant: str | None = None
    topic: str | None = None              # one of llm.prompts.TOPICS
    key_techniques: list[str] = field(default_factory=list)
    novelty_flag: str | None = None       # new_theory|new_method|sharper_rate|...
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
