"""LLM pipeline: score papers, summarize top ones, extract events from conference pages."""
from __future__ import annotations

import json
import logging
import re

from ..models import Event, Paper
from .sjtu_client import SJTUClient

log = logging.getLogger(__name__)


from .prompts import (
    EVENT_SYSTEM,
    RICH_SUMMARY_SYSTEM,
    SCORE_SYSTEM,
    TOPICS,
)


def _strip_code_fence(text: str) -> str:
    """Drop a ```json … ``` fence (or a dangling ```json opener from truncated
    output) so the bare JSON body can be repaired / parsed."""
    text = (text or "").strip()
    m = re.search(r"```(?:json)?\s*(.+?)```", text, flags=re.DOTALL)
    if m:
        return m.group(1).strip()
    # Truncated output keeps the opening fence but never reaches the closer.
    m = re.match(r"```(?:json)?\s*", text)
    if m:
        return text[m.end():].strip()
    return text


def _extract_json(text: str):
    """Tolerant JSON extraction — strips code fences, finds first {...} or [...] block."""
    text = _strip_code_fence(text)
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
    model: str | None = None,
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
                model=model,
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


def _try_repair_truncated_json(text: str) -> str:
    """If `text` looks like JSON that got cut off mid-string/list/dict, close
    the open brackets so it parses. Returns the (possibly modified) text."""
    text = (text or "").strip()
    # Tolerate a leading ```json fence stripped earlier
    if not text or text[0] not in "{[":
        return text

    # Walk to track string state + bracket stack. Find last "safe" position
    # where we could cut cleanly (after a `}`, `]`, or string-close quote that
    # is itself followed by punctuation).
    stack: list[str] = []
    in_str = False
    esc = False
    safe_cut: int | None = None
    for i, ch in enumerate(text):
        if esc:
            esc = False
            continue
        if in_str:
            if ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{[":
            stack.append(ch)
        elif ch in "}]":
            if stack:
                stack.pop()
            if not stack:
                safe_cut = i + 1   # complete JSON ends here
        elif ch == "," and stack:
            # cutting just before a comma drops the next (partial) element
            safe_cut = i

    # Truncate at the last comma-or-end-of-object boundary so the partial last
    # element is dropped, then close any remaining open brackets / strings.
    if safe_cut is not None:
        text = text[:safe_cut]
        # Re-walk to get the actual stack at safe_cut
        stack, in_str, esc = [], False, False
        for ch in text:
            if esc:
                esc = False
                continue
            if in_str:
                if ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch in "{[":
                stack.append(ch)
            elif ch in "}]" and stack:
                stack.pop()

    if in_str:
        text += '"'
    for opener in reversed(stack):
        text += "}" if opener == "{" else "]"
    return text


# Field names the rich-summary prompt emits, used as anchors when salvaging
# prose from JSON the model failed to escape / finish properly.
_SUMMARY_KEYS = ("topic", "summary_zh", "key_techniques", "why_relevant", "novelty_flag")


def summary_looks_garbled(text: str | None) -> bool:
    """True when `text` is a raw JSON blob that leaked into a summary field
    instead of clean prose — i.e. the parse fell back to dumping the model
    output. Used both to flag papers at summarize time and to find blocks worth
    re-running in already-rendered reports."""
    t = (text or "").strip()
    if not t:
        return False
    if t.startswith("```") or '```json' in t:
        return True
    # A bare JSON object whose first key is one of the schema fields.
    if t.startswith("{") and re.search(r'"(?:%s)"\s*:' % "|".join(_SUMMARY_KEYS), t):
        return True
    return False


def salvage_summary_fields(raw: str) -> dict:
    """Best-effort recovery of summary fields from malformed/truncated JSON.

    The model frequently emits unescaped inner quotes (e.g. a Chinese phrase in
    "smart quotes") or gets cut off mid-array, so strict json.loads fails. We
    anchor on the known field names instead: a value runs until the closing
    quote that precedes the next field name (or the end of the object). Only
    fully-formed values are returned — a half-written summary_zh is dropped so
    callers can decide to re-run rather than render a fragment."""
    body = _strip_code_fence(raw)
    out: dict = {}

    # topic / novelty_flag: simple quoted scalars.
    for key in ("topic", "novelty_flag"):
        m = re.search(rf'"{key}"\s*:\s*"([^"]*)"', body)
        if m:
            out[key] = m.group(1).strip()

    # summary_zh / why_relevant: prose that may contain stray quotes. Capture up
    # to the closing `",` (or `"}`) that is immediately followed by a known key
    # or the end of the object, so embedded quotes don't end the match early.
    next_key = r'(?:%s)' % "|".join(_SUMMARY_KEYS)
    for key in ("summary_zh", "why_relevant"):
        m = re.search(
            rf'"{key}"\s*:\s*"(.*?)"\s*,\s*"{next_key}"\s*:', body, flags=re.DOTALL
        )
        if not m:
            m = re.search(rf'"{key}"\s*:\s*"(.*?)"\s*\}}', body, flags=re.DOTALL)
        if m:
            out[key] = m.group(1).strip()

    # key_techniques: pull every complete quoted item, even if the array was cut
    # off before its closing bracket.
    m = re.search(r'"key_techniques"\s*:\s*\[(.*)', body, flags=re.DOTALL)
    if m:
        arr = m.group(1)
        end = arr.find("]")
        if end != -1:
            arr = arr[:end]
        items = re.findall(r'"([^"]*)"', arr)
        if items:
            out["key_techniques"] = [s.strip() for s in items]

    return out


def summarize_paper(
    client: SJTUClient,
    paper: Paper,
    interests_yaml: str,
    *,
    deep: bool = False,
    model: str | None = None,
    extra_body: str | None = None,
) -> dict:
    """Mutates `paper` with summary_zh / why_relevant / topic / key_techniques /
    novelty_flag, and returns the parsed dict (for callers who want it raw)."""
    body = f"Abstract: {paper.abstract}"
    if extra_body:
        body += "\n\n" + extra_body
    user = (
        "## Researcher interests\n" + interests_yaml +
        f"\n\n## Paper\nTitle: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Venue: {paper.venue or paper.source}\n"
        f"Categories: {', '.join(paper.categories)}\n\n{body}\n"
    )

    def _call(max_tokens: int) -> str:
        return client.chat(
            [
                {"role": "system", "content": RICH_SUMMARY_SYSTEM},
                {"role": "user", "content": user},
            ],
            deep=deep,
            model=model,
            max_tokens=max_tokens,
        )

    def _parse(text: str) -> dict | None:
        """Strict parse, then truncation-repair (fence stripped first), as a dict."""
        try:
            p = _extract_json(text)
            return p if isinstance(p, dict) else None
        except Exception:
            pass
        try:
            p = _extract_json(_try_repair_truncated_json(_strip_code_fence(text)))
            if isinstance(p, dict):
                log.info("summary recovered via JSON repair for %s", paper.paper_id)
                return p
        except Exception:
            pass
        return None

    # First attempt: generous budget. Rich prompt typically outputs ~1500-2500
    # tokens. 1500 was truncating the JSON mid-array for ~half of AoS papers.
    raw = _call(max_tokens=3000)
    parsed = _parse(raw)
    if parsed is None:
        # Retry once with a larger budget — the usual failure is the JSON array
        # getting cut off by max_tokens.
        log.warning("summary parse failed for %s, retrying LLM call", paper.paper_id)
        try:
            raw = _call(max_tokens=3500)
            parsed = _parse(raw)
        except Exception as e:
            log.warning("summary retry also failed for %s: %s", paper.paper_id, e)

    paper.summary_incomplete = False
    if parsed is None:
        # Last resort: salvage whatever clean fields we can from the raw blob
        # (handles unescaped inner quotes the repair can't). Flag the paper as
        # incomplete so it can be picked up by `python -m research_news.rerun`.
        parsed = salvage_summary_fields(raw)
        paper.summary_incomplete = True
        if parsed.get("summary_zh"):
            log.warning("summary salvaged (incomplete) for %s — flagged for rerun",
                        paper.paper_id)
        else:
            log.warning("summary unrecoverable for %s — flagged for rerun",
                        paper.paper_id)

    paper.summary_zh = (parsed.get("summary_zh") or "").strip()
    paper.why_relevant = (parsed.get("why_relevant") or "").strip()
    topic = (parsed.get("topic") or "").strip().lower()
    paper.topic = topic if topic in TOPICS else "other"
    kt = parsed.get("key_techniques")
    paper.key_techniques = [str(x).strip() for x in kt] if isinstance(kt, list) else []
    paper.novelty_flag = (parsed.get("novelty_flag") or "").strip() or None
    return parsed


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
