"""Orchestrate the JCSDS conference deep-read pipeline (match -> fetch -> read).

Usage:
  python -m research_news.conf.run --sessions 4,17,29      # specific sessions
  python -m research_news.conf.run --group network-a       # one topic group
  python -m research_news.conf.run --all                   # every content session
  python -m research_news.conf.run --all --skip-done       # only missing talks

Writes one small JSON per talk to data/conferences/jcsds2026/research/
sess<IDX>_t<no>.json — the same schema the topic-page generator consumes.
"""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

from dotenv import load_dotenv

from ..llm.sjtu_client import SJTUClient
from .match import match_talk
from .read import read_talk

log = logging.getLogger(__name__)

ROOT = Path("data/conferences/jcsds2026")
RDIR = ROOT / "research"


def _load_sessions() -> list[dict]:
    return json.loads((ROOT / "sessions.json").read_text(encoding="utf-8"))


def _load_groups() -> dict:
    return json.loads((ROOT / "topic_groups.json").read_text(encoding="utf-8"))


def _talk_path(idx: int, no) -> Path:
    return RDIR / f"sess{idx}_t{no}.json"


def _resolve_indices(args, sessions: list[dict], groups: dict) -> list[int]:
    if args.sessions:
        return [int(x) for x in args.sessions.split(",") if x.strip()]
    if args.group:
        return list(groups[args.group]["session_idx"])
    if args.all:
        return [i for i, s in enumerate(sessions) if s.get("talks")]
    raise SystemExit("specify --sessions, --group, or --all")


def process_session(client: SJTUClient, idx: int, session: dict, *,
                    skip_done: bool, download: bool) -> int:
    talks = session.get("talks", [])
    written = 0
    for t in talks:
        no = t["no"]
        out_path = _talk_path(idx, no)
        if skip_done and out_path.exists():
            log.info("skip sess%s t%s (already done)", idx, no)
            continue
        title, speaker = t["title"], t.get("speaker", "")
        m = match_talk(title, speaker)
        log.info("sess%s t%s: found=%s (%s) | %s",
                 idx, no, m.found, m.reason, title[:55])
        rec = read_talk(client, no, title, speaker, m, download=download)
        RDIR.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8")
        written += 1
    return written


def main() -> None:
    load_dotenv()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--sessions", help="comma-separated session indices")
    g.add_argument("--group", help="topic-group key, e.g. network-a")
    g.add_argument("--all", action="store_true", help="all content sessions")
    ap.add_argument("--skip-done", action="store_true",
                    help="skip talks whose JSON already exists")
    ap.add_argument("--no-pdf", action="store_true",
                    help="skip PDF download; deep-read from abstract only")
    args = ap.parse_args()

    sessions = _load_sessions()
    groups = _load_groups()
    indices = _resolve_indices(args, sessions, groups)

    client = SJTUClient()
    total = 0
    for idx in indices:
        session = sessions[idx]
        n = process_session(client, idx, session,
                            skip_done=args.skip_done, download=not args.no_pdf)
        total += n
        log.info("sess%s done: %d talks written", idx, n)
    log.info("ALL DONE: %d talks written across %d sessions; LLM calls=%d",
             total, len(indices), client.calls)


if __name__ == "__main__":
    main()
