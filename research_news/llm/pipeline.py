"""LLM pipeline: score papers, summarize top ones, extract events from conference pages."""
from __future__ import annotations

import json
import logging
import re
from typing import Iterable

from ..models import Event, Paper
from .sjtu_client import SJTUClient

log = logging.getLogger(__name__)


SCORE_SYSTEM = """You score academic papers for a statistics researcher.
You will receive (1) the researcher's interests and (2) a batch of papers.
Return a JSON array; each element is {"id": <paper_id>, "score": <0-10 integer>, "reason": "<one short sentence>"}.
Score 0-10 per the rubric in the interests file. Be strict: most papers in
unrelated subfields should get 0-3."""

SUMMARY_SYSTEM = """You write personalized Chinese summaries of papers for a
statistics researcher. Follow the summary_style guidance in the interests
file. Return JSON: {"summary_zh": "...", "why_relevant": "..."}."""

EVENT_SYSTEM = """You extract academic events (conference dates, deadlines,
seminar talks) from a web page's plain text. Return a JSON array; each
element is {"title": "...", "date": "YYYY-MM-DD or freeform", "speaker":
"... or null", "location": "... or null", "url": "... or null", "note": "...
or null"}. Only include events; ignore navigation, footers, and prose."""


def _extract_json(text: str):
    """Tolerant JSON extraction — strips code fences if present."""
    text = text.strip()
    m = re.search(r"```(?:json)?\s*(.+?)```", text, flags=re.DOTALL)
    if m:
        text = m.group(1).strip()
    return json.loads(text)


def score_papers(
    client: SJTUClient,
    papers: list[Paper],
    interests_yaml: str,
    *,
    batch_size: int = 15,
) -> dict[str, tuple[float, str]]:
    """Returns {paper_id: (score, reason)}."""
    out: dict[str, tuple[float, str]] = {}
    for i in range(0, len(papers), batch_size):
        batch = papers[i : i + batch_size]
        payload = [
            {
                "id": p.paper_id,
                "title": p.title,
                "abstract": p.abstract[:1200],
                "categories": p.categories,
            }
            for p in batch
        ]
        user = (
            "## Researcher interests\n"
            + interests_yaml
            + "\n\n## Papers to score\n"
            + json.dumps(payload, ensure_ascii=False)
        )
        try:
            raw = client.chat(
                [
                    {"role": "system", "content": SCORE_SYSTEM},
                    {"role": "user", "content": user},
                ],
                response_format={"type": "json_object"},
            )
            # Some providers wrap arrays in {"data": [...]} when forced to JSON object.
            try:
                parsed = _extract_json(raw)
            except json.JSONDecodeError:
                parsed = []
            if isinstance(parsed, dict):
                # Try common wrapper keys
                for k in ("results", "data", "papers", "scores"):
                    if k in parsed and isinstance(parsed[k], list):
                        parsed = parsed[k]
                        break
            if not isinstance(parsed, list):
                log.warning("score batch returned unexpected shape: %r", parsed)
                continue
            for item in parsed:
                pid = str(item.get("id"))
                score = float(item.get("score", 0))
                reason = str(item.get("reason", ""))
                out[pid] = (score, reason)
        except Exception as e:
            log.warning("score batch failed: %s", e)
    return out


def summarize_paper(
    client: SJTUClient,
    paper: Paper,
    interests_yaml: str,
    *,
    deep: bool = False,
) -> tuple[str, str]:
    user = (
        "## Researcher interests\n"
        + interests_yaml
        + f"\n\n## Paper\nTitle: {paper.title}\nAuthors: {', '.join(paper.authors)}\n"
        f"Categories: {', '.join(paper.categories)}\n"
        f"Abstract: {paper.abstract}\n"
    )
    raw = client.chat(
        [
            {"role": "system", "content": SUMMARY_SYSTEM},
            {"role": "user", "content": user},
        ],
        deep=deep,
        response_format={"type": "json_object"},
    )
    try:
        parsed = _extract_json(raw)
        return parsed.get("summary_zh", "").strip(), parsed.get("why_relevant", "").strip()
    except Exception as e:
        log.warning("summary parse failed for %s: %s", paper.paper_id, e)
        return raw.strip(), ""


def extract_events(client: SJTUClient, source_name: str, text: str) -> list[Event]:
    user = f"## Source: {source_name}\n\n## Page text\n{text}"
    try:
        raw = client.chat(
            [
                {"role": "system", "content": EVENT_SYSTEM},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
        )
        parsed = _extract_json(raw)
        if isinstance(parsed, dict):
            for k in ("events", "data", "results"):
                if k in parsed and isinstance(parsed[k], list):
                    parsed = parsed[k]
                    break
        if not isinstance(parsed, list):
            return []
        return [
            Event(
                source=source_name,
                title=str(e.get("title", "")),
                date=e.get("date"),
                speaker=e.get("speaker"),
                location=e.get("location"),
                url=e.get("url"),
                note=e.get("note"),
            )
            for e in parsed
            if e.get("title")
        ]
    except Exception as e:
        log.warning("event extraction failed for %s: %s", source_name, e)
        return []
