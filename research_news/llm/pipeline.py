"""LLM pipeline: score papers, summarize top ones, extract events from conference pages."""
from __future__ import annotations

import json
import logging
import re

from ..models import Event, Paper
from .sjtu_client import SJTUClient

log = logging.getLogger(__name__)


SCORE_SYSTEM = """You score academic papers for a statistics researcher.
You will receive (1) the researcher's interests and (2) a batch of papers.

Respond with ONLY a valid JSON object of the form:
{"results": [{"id": "<paper_id>", "score": <0-10 integer>, "reason": "<one short sentence>"}, ...]}

No prose, no markdown fences, no commentary — just the JSON object.
Score 0-10 per the rubric in the interests file. Be strict: most papers in
unrelated subfields should get 0-3."""

SUMMARY_SYSTEM = """You write personalized Chinese summaries of papers for a
statistics researcher. Follow the summary_style guidance in the interests file.

Respond with ONLY a valid JSON object of the form:
{"summary_zh": "...", "why_relevant": "..."}

No prose, no markdown fences, no commentary — just the JSON object."""

EVENT_SYSTEM = """You extract academic events (conference dates, deadlines,
seminar talks) from a web page's plain text.

Respond with ONLY a valid JSON object of the form:
{"events": [{"title": "...", "date": "YYYY-MM-DD or freeform or null", "speaker": "... or null", "location": "... or null", "url": "... or null", "note": "... or null"}, ...]}

No prose, no markdown fences, no commentary — just the JSON object.
Only include real events; ignore navigation, footers, and generic prose. If
the page contains no events, return {"events": []}."""


def _extract_json(text: str):
    """Tolerant JSON extraction — strips code fences, finds first {...} or [...] block."""
    text = (text or "").strip()
    m = re.search(r"```(?:json)?\s*(.+?)```", text, flags=re.DOTALL)
    if m:
        text = m.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    for opener, closer in (("{", "}"), ("[", "]")):
        start = text.find(opener)
        if start == -1:
            continue
        depth = 0
        for i in range(start, len(text)):
            if text[i] == opener:
                depth += 1
            elif text[i] == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start : i + 1])
                    except json.JSONDecodeError:
                        break
    raise json.JSONDecodeError("no parseable JSON found", text, 0)


def score_papers(
    client: SJTUClient,
    papers: list[Paper],
    interests_yaml: str,
    *,
    batch_size: int = 8,   # smaller batches → shorter output → less risk of truncation
) -> dict[str, tuple[float, str]]:
    """Returns {paper_id: (score, reason)}."""
    out: dict[str, tuple[float, str]] = {}
    n_batches = (len(papers) + batch_size - 1) // batch_size
    for bi, i in enumerate(range(0, len(papers), batch_size)):
        batch = papers[i : i + batch_size]
        payload = [
            {
                "id": p.paper_id,
                "title": p.title,
                "abstract": p.abstract[:600],   # shorter → fewer tokens
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
        log.info("scoring batch %d/%d (%d papers) ...", bi + 1, n_batches, len(batch))
        try:
            raw = client.chat(
                [
                    {"role": "system", "content": SCORE_SYSTEM},
                    {"role": "user", "content": user},
                ],
                max_tokens=2000,
            )
            log.debug("score batch %d raw response: %s", bi + 1, raw[:500])
        except Exception as e:
            log.warning("score batch %d: LLM call failed: %s", bi + 1, e)
            continue

        try:
            parsed = _extract_json(raw)
        except json.JSONDecodeError:
            log.warning(
                "score batch %d: JSON parse failed. Raw response (first 400 chars):\n%s",
                bi + 1,
                raw[:400],
            )
            continue

        # Unwrap common wrapper keys
        if isinstance(parsed, dict):
            for k in ("results", "data", "papers", "scores"):
                if k in parsed and isinstance(parsed[k], list):
                    parsed = parsed[k]
                    break

        if not isinstance(parsed, list):
            log.warning(
                "score batch %d: unexpected shape %s. Raw:\n%s",
                bi + 1,
                type(parsed).__name__,
                raw[:400],
            )
            continue

        n_ok = 0
        for item in parsed:
            if not isinstance(item, dict):
                continue
            pid = str(item.get("id", "")).strip()
            if not pid:
                continue
            try:
                score = float(item.get("score", 0))
            except (TypeError, ValueError):
                score = 0.0
            reason = str(item.get("reason", ""))
            out[pid] = (score, reason)
            n_ok += 1
        log.info("score batch %d: parsed %d scores", bi + 1, n_ok)

    # Log score distribution so we can see what happened
    if out:
        scores_only = [v[0] for v in out.values()]
        log.info(
            "score distribution: min=%.1f max=%.1f mean=%.1f  (matched %d/%d papers)",
            min(scores_only),
            max(scores_only),
            sum(scores_only) / len(scores_only),
            len(out),
            len(papers),
        )
    else:
        log.warning("score_papers returned 0 results — all papers will be dropped")

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
        max_tokens=1500,
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
            max_tokens=2500,
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
