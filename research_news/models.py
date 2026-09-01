from __future__ import annotations

from dataclasses import dataclass, field, asdict
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
    # Holds both institution names and raw affiliation strings; used for the
    # green-light match below.
    affiliations: list[str] = field(default_factory=list)
    # Clean, deduplicated institution display names (from OpenAlex) shown on the
    # daily / journal pages. We don't track which author belongs to which
    # institution — just the set present on the paper.
    institutions: list[str] = field(default_factory=list)
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
    # Explicit full-text PDF URL, when the source-based guess in
    # `highlights._pdf_url` can't derive one — e.g. an open-access journal paper
    # resolved from a pasted link by `oa_pdf.resolve`. Takes priority over the
    # per-source guess.
    pdf_url: str | None = None
    # Number of cited works (with abstracts) attached to the deep-read prompt.
    # Recorded per deep read as reference data for tuning the prompt later.
    n_references: int | None = None

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


@dataclass
class Talk:
    """A hand-curated conference talk / lecture (e.g. a YouTube recording).

    Unlike papers, talks are NOT scored or filtered — you pick the video and it
    always gets read. The transcript (produced locally by
    ``scrapers.transcribe``) is the "full text" the LLM reads, in place of a
    paper's PDF. Talks ride the deep-read style but live in their own
    docs/talks/ section + data/talks_index.json.
    """
    id: str                    # stable slug: transcript filename + dedup key
    url: str                   # video / recording URL
    title: str | None = None
    speaker: str | None = None
    venue: str | None = None   # seminar / conference (e.g. "OCIS", "INI CIFW04")
    date: str | None = None    # talk date: YYYY-MM-DD, YYYY-MM, or freeform
    # arXiv ids / DOIs the talk is about → cross-linked to their deep-read pages
    # (and optionally auto-queued into the paper deep-read pipeline).
    papers: list[str] = field(default_factory=list)
    # The talk's own abstract + discussant, when the source page carries them
    # (OCIS season pages do). The abstract is authoritative, ASR-error-free
    # ground truth fed into the read; the discussant is shown for context.
    abstract: str | None = None
    discussant: str | None = None
    # Slide deck URL (e.g. Google Drive PDF). Its extracted text is fed into the
    # read as another authoritative source alongside transcript + abstract + paper.
    slides: str | None = None
    # Source season slug ('spring-2024') from the OCIS season page, used to group
    # talks into per-season overview pages. Falls back to a date-derived season.
    season: str | None = None
    # Conference / series the talk belongs to (e.g. "OCIS", "INI"). Season pages
    # group by series; derived from the venue when unset.
    series: str | None = None
    # One of llm.prompts.TOPICS — used to slot the talk into the archive's topic
    # grouping. Defaults to "other" when unset.
    topic: str | None = None
    # Domain terms (names, jargon) fed to Whisper as initial_prompt to bias ASR.
    asr_prompt: str | None = None
    # ASR language hint ("en", "zh", ...); None = auto-detect.
    language: str | None = None
    # Per-talk boundaries for a multi-talk recording. Each segment is a dict with
    # `start` (HH:MM:SS or seconds) + optional `speaker` / `title`. Empty = the
    # whole video is a single talk.
    segments: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
