"""Append-only log of every LLM-scored paper.

Captures both above- and below-threshold papers as training data for
future ranking/recommendation work. One JSON object per line.

We log after the summarize step so above-threshold papers carry their
topic/novelty_flag/key_techniques too; below-threshold papers only have
score and reason (the summarizer is not run on them)."""
from __future__ import annotations

import hashlib
import json
import logging
from datetime import date
from pathlib import Path

from .models import Paper

log = logging.getLogger(__name__)

SCORE_LOG_FILE = Path("data/llm_scores.jsonl")


def interests_hash(interests_text: str) -> str:
    return hashlib.sha256(interests_text.encode("utf-8")).hexdigest()[:12]


def _paper_row(p: Paper, *, run_date: date, model: str, interests_hash: str) -> dict:
    return {
        "run_date": run_date.isoformat(),
        "model": model,
        "interests_hash": interests_hash,
        "source": p.source,
        "paper_id": p.paper_id,
        "title": p.title,
        "authors": p.authors,
        "abstract": p.abstract,
        "categories": p.categories,
        "published": p.published,
        "url": p.url,
        "score": p.score,
        "score_reason": p.score_reason,
        "topic": p.topic,
        "novelty_flag": p.novelty_flag,
        "key_techniques": p.key_techniques,
    }


def append_scored(
    papers: list[Paper],
    *,
    run_date: date,
    model: str,
    interests_text: str,
) -> None:
    if not papers:
        return
    SCORE_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    h = interests_hash(interests_text)
    with SCORE_LOG_FILE.open("a", encoding="utf-8") as f:
        for p in papers:
            row = _paper_row(p, run_date=run_date, model=model, interests_hash=h)
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    log.info("appended %d scored papers to %s", len(papers), SCORE_LOG_FILE)
