"""Quarterly journal pull: fetch the latest issue of each configured journal,
score + summarize all papers (no dropout threshold — these are pre-curated),
download high-relevance PDFs, render a Markdown page.

Sources:
  - JMLR: HTML scrape of the volume index page (rolling publication; we
    take the N most recent papers).
  - AoS / JASA / JRSSB / Biometrika: Crossref API for issue TOC + Semantic
    Scholar for abstract backfill when Crossref doesn't expose it.

Usage:
    python -m research_news.journals                       # all journals
    python -m research_news.journals --only AoS,JRSSB      # subset
    python -m research_news.journals --jmlr-n 15
    python -m research_news.journals --dry-run             # no LLM
"""
from __future__ import annotations

import argparse
import logging
import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

from .dedup import filter_new, load_seen, mark_seen, save_seen
from .deep_read import generate_deep_read_report, select_deep_read_papers
from .highlights import save_highlights
from .llm.pipeline import score_papers, summarize_paper
from .llm.sjtu_client import SJTUClient
from .models import Paper
from .render.markdown import render_journal_page, update_index
from .score_log import append_scored as append_score_log
from .scrapers import affiliations as affil
from .scrapers.crossref import fetch_issue, fetch_latest_issue, fill_arxiv_links
from .scrapers.jmlr import fetch_latest as jmlr_fetch_latest
from .usage import report as report_token_usage

log = logging.getLogger("research_news.journals")

JOURNALS_MODEL = os.environ.get("JOURNALS_MODEL",
                                os.environ.get("DAILY_MODEL", "glm-5.1"))

JOURNALS_CONFIG_PATH = Path("config/journals.yaml")


def _load_groups() -> dict:
    """Returns {group_key: {label, journals: [{short, full, issn}]}}."""
    import yaml as _yaml
    cfg = _yaml.safe_load(JOURNALS_CONFIG_PATH.read_text(encoding="utf-8"))
    return cfg.get("groups", {})


def _fetch_journal(jcfg: dict, *, jmlr_n: int | None = None,
                   jmlr_vol: int | None = None,
                   n_issues: int = 1) -> list[Paper]:
    issn = jcfg["issn"]
    full = jcfg["full"]
    short = jcfg.get("short", full)
    if issn == "jmlr":
        return jmlr_fetch_latest(n=jmlr_n, volume=jmlr_vol)
    try:
        return fetch_latest_issue(issn, full, n_issues=n_issues)
    except Exception as e:
        log.warning("fetch failed for %s (ISSN %s): %s", short, issn, e)
        return []


def _save_papers(papers: list[Paper], path: Path) -> None:
    """Atomic write: serialize to <path>.tmp, then os.replace into place. So a
    crash mid-write can't corrupt the file."""
    import json, os
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps([p.to_dict() for p in papers], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    os.replace(tmp, path)
    log.info("saved %d papers to %s", len(papers), path)


def _load_papers(path: Path) -> list[Paper]:
    import json
    raw = json.loads(path.read_text(encoding="utf-8"))
    papers = [Paper(**d) for d in raw]
    log.info("loaded %d papers from %s", len(papers), path)
    return papers


def _summary_is_broken(p: Paper) -> bool:
    """Heuristics for a paper whose LLM summary needs a retry.

    Catches both LLM call failures (no summary at all) and parse failures
    (raw JSON spill-over where summary_zh starts with '{')."""
    s = (p.summary_zh or "").strip()
    if not s:
        return True
    if s.startswith("{") or s.startswith("```"):
        return True
    if len(s) < 80:
        return True
    # A successful rich-prompt run always fills these; their absence is a
    # strong signal that summarize_paper bailed out.
    if not p.topic or not p.key_techniques or not p.why_relevant:
        return True
    return False


def _completeness_note(short: str, venue: str, issn: str | None,
                       vol: str | None, iss: str | None,
                       issue_papers: list[Paper], *,
                       enabled: bool, source: str) -> str | None:
    """The '目录核对' badge for a journal page: diff the rendered papers against
    the issue's authoritative TOC. Returns None (no line) when disabled or not
    applicable (no real ISSN — e.g. JMLR — or no volume). Never raises."""
    if not enabled or not issn or issn == "jmlr" or not vol:
        return None
    try:
        from .completeness import check_issue, format_status_line, papers_to_entries
        res = check_issue(issn, venue, int(vol), int(iss) if iss else None,
                          papers_to_entries(issue_papers), source=source)
        note = format_status_line(res)
        log.info("[%s v%s i%s] %s", short, vol, iss, note)
        return note
    except Exception as e:  # noqa: BLE001 — a failed check must not block rendering
        log.warning("completeness check failed for %s v%s i%s: %s", short, vol, iss, e)
        return None


def _process_issue(
    issue_papers: list[Paper],
    short: str,
    venue: str,
    vol: str | None,
    iss: str | None,
    *,
    when: date,
    client: SJTUClient,
    interests_text: str,
    model: str,
    th_deepread: float,
    skip_pdf: bool = False,
    retry_broken: bool = False,
    is_loaded: bool = False,
    issn: str | None = None,
    check_completeness: bool = True,
    completeness_source: str = "openalex",
) -> Path:
    """Score → summarize → render → deep-read one issue's papers, then return the
    rendered journal page path.

    Shared by the normal run (``when`` = today) and the issue-rerun path
    (``when`` = the original page's date, so the regenerated page overwrites it).
    Prompts are imported fresh from ``llm.prompts`` by the callees, so a rerun
    automatically picks up any prompt edits.
    """
    # ── score ──────────────────────────────────────────────────────────────
    # On --retry-broken with loaded papers the cached batch scores are still
    # valid (only the rich summary broke), so we keep them.
    if retry_broken and is_loaded and all(p.score is not None for p in issue_papers):
        log.info("[%s v%s i%s] retry-broken: keeping cached scores", short, vol, iss)
    else:
        log.info("[%s v%s i%s] scoring %d papers (model=%s) ...",
                 short, vol, iss, len(issue_papers), model)
        scores = score_papers(client, issue_papers, interests_text, model=model)
        for p in issue_papers:
            sr = scores.get(p.paper_id)
            p.score, p.score_reason = sr if sr else (0.0, p.score_reason)

    # No drop threshold: journals are pre-curated. Sort so the most relevant
    # float to the top within each topic section.
    issue_papers.sort(key=lambda p: p.score or 0, reverse=True)

    # ── summarize ──────────────────────────────────────────────────────────
    if retry_broken and is_loaded:
        to_summarize = [p for p in issue_papers if _summary_is_broken(p)]
        log.info("[%s v%s i%s] retry-broken: %d/%d need re-summarize",
                 short, vol, iss, len(to_summarize), len(issue_papers))
    else:
        to_summarize = issue_papers
        log.info("[%s v%s i%s] summarizing %d papers (model=%s) ...",
                 short, vol, iss, len(to_summarize), model)
    for p in to_summarize:
        try:
            summarize_paper(client, p, interests_text, model=model)
        except Exception as e:  # noqa: BLE001
            log.warning("summary failed for %s: %s", p.paper_id, e)

    append_score_log(issue_papers, run_date=when, model=model,
                     interests_text=interests_text)

    # ── completeness badge (diff this issue against an authoritative TOC) ─────
    note = _completeness_note(short, venue, issn, vol, iss, issue_papers,
                              enabled=check_completeness, source=completeness_source)

    # ── institutions + render ───────────────────────────────────────────────
    log.info("[%s v%s i%s] looking up institutions for %d papers ...",
             short, vol, iss, len(issue_papers))
    affil.backfill_affiliations(issue_papers)
    out = render_journal_page(issue_papers, short, venue, vol=vol, iss=iss,
                              when=when, completeness_note=note)

    # ── deep read (score >= th_deepread, plus institution green-lights) ──────
    deep_read_papers = select_deep_read_papers(
        issue_papers, issue_papers, th_deepread,
        client=client, interests_yaml=interests_text, model=model,
    )
    if deep_read_papers and not skip_pdf:
        log.info("[%s v%s i%s] %d deep-read papers (PDF + report)",
                 short, vol, iss, len(deep_read_papers))
        save_highlights(deep_read_papers, run_date=when)
        generate_deep_read_report(
            deep_read_papers, client, interests_text, when, "journals", model=model
        )
    elif skip_pdf:
        log.info("[%s v%s i%s] skip_pdf set; no PDF / deep read", short, vol, iss)

    return out


def run(only: list[str] | None = None, dry_run: bool = False,
        jmlr_n: int | None = None, jmlr_vol: int | None = None,
        n_issues: int = 1, label: str | None = None,
        skip_pdf: bool = False,
        save_papers: Path | None = None,
        load_papers: Path | None = None,
        retry_broken: bool = False,
        only_group: list[str] | None = None,
        dedup: bool = True,
        check_completeness: bool = True) -> list[Path] | None:
    load_dotenv()
    interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")
    groups = _load_groups()

    if load_papers:
        log.info("skipping fetch; loading papers from %s", load_papers)
        papers = _load_papers(load_papers)
    else:
        if only_group:
            groups_to_run = {k: groups[k] for k in only_group if k in groups}
            unknown = [k for k in only_group if k not in groups]
            if unknown:
                log.warning("unknown groups (skipped): %s — available: %s",
                            unknown, list(groups.keys()))
        else:
            groups_to_run = groups

        only_shorts = set(s.strip() for s in (only or []) if s.strip())
        log.info("journals run: groups=%s, only=%s",
                 list(groups_to_run.keys()),
                 sorted(only_shorts) if only_shorts else "all")

        papers = []
        for gkey, gcfg in groups_to_run.items():
            for jcfg in gcfg["journals"]:
                if only_shorts and jcfg["short"] not in only_shorts:
                    continue
                ps = _fetch_journal(jcfg, jmlr_n=jmlr_n,
                                    jmlr_vol=jmlr_vol, n_issues=n_issues)
                log.info("  [%s] %s → %d papers", gkey, jcfg["short"], len(ps))
                papers.extend(ps)
                # Incremental save: ^C / crash leaves earlier journals on disk.
                if save_papers:
                    _save_papers([p for p in papers if p.abstract], save_papers)

        # Drop any without an abstract — can't score them meaningfully.
        n_before = len(papers)
        papers = [p for p in papers if p.abstract]
        if len(papers) < n_before:
            log.info("dropped %d papers with no abstract (Crossref + S2 both empty)",
                     n_before - len(papers))

        if dedup:
            seen = load_seen()
            n_before = len(papers)
            papers = filter_new(papers, seen)
            if len(papers) < n_before:
                log.info("dropped %d papers already in seen_papers.json",
                         n_before - len(papers))

    if not papers:
        log.error("no papers — bailing")
        return None

    # Resolve arxiv preprint links so the rendered journal + deep-read pages can
    # show both the publisher link and the (paywall-free) arxiv link. Runs on
    # both fetch and --load-papers paths; papers that already have a link
    # (e.g. arxiv-native, or picked up during abstract backfill) are skipped.
    fill_arxiv_links(papers)

    # Persist the enrichment so a later --load-papers run reuses the links
    # without re-querying arxiv.
    if save_papers:
        _save_papers(papers, save_papers)
    elif load_papers:
        _save_papers(papers, load_papers)

    if dry_run:
        log.info("dry-run: %d papers across %d venues",
                 len(papers),
                 len({p.venue for p in papers}))
        for p in papers[:10]:
            log.info("  [%s] %s — abstract chars=%d", p.venue, p.title[:80], len(p.abstract))
        return None

    client = SJTUClient()

    import yaml as _yaml
    _icfg = _yaml.safe_load(interests_text)
    th_deepread = float(_icfg.get("score_threshold_deepread", 6))

    today = date.today()

    # Build full_name → (short, issn) mapping from the groups config.
    full_to_short: dict[str, str] = {}
    full_to_issn: dict[str, str] = {}
    for gcfg in groups.values():
        for jcfg in gcfg["journals"]:
            full_to_short[jcfg["full"]] = jcfg["short"]
            full_to_issn[jcfg["full"]] = jcfg["issn"]

    # Group papers by (venue, volume, issue) → process + render one page per issue.
    by_issue: dict[tuple, list[Paper]] = {}
    for p in papers:
        key = (p.venue or "Unknown", p.volume, p.issue)
        by_issue.setdefault(key, []).append(p)

    out_paths = []
    for (venue, vol, iss), vps in by_issue.items():
        short = full_to_short.get(venue, venue)
        out = _process_issue(
            vps, short, venue, vol, iss, when=today,
            client=client, interests_text=interests_text, model=JOURNALS_MODEL,
            th_deepread=th_deepread, skip_pdf=skip_pdf,
            retry_broken=retry_broken, is_loaded=bool(load_papers),
            issn=full_to_issn.get(venue), check_completeness=check_completeness,
        )
        out_paths.append(out)

    # Persist the LLM enrichment back to the source JSON so a future
    # --load-papers picks up the fixed summaries.
    if load_papers:
        _save_papers(papers, load_papers)

    update_index()

    # Record the papers we just published so future runs skip them.
    # Done after rendering: a crash mid-render shouldn't poison seen_papers.json.
    if dedup and not load_papers:
        seen = load_seen()
        mark_seen(papers, seen)
        save_seen(seen)

    for p in out_paths:
        log.info("wrote %s", p)
    report_token_usage(client, "journals", today)
    return out_paths


# ── issue rerun ────────────────────────────────────────────────────────────────
# Re-generate already-published journal issue pages in place, using the *current*
# deep-read + scoring prompts. Distinct from research_news.rerun (which repairs
# garbled summary blocks); this re-runs the whole LLM stack for a chosen issue
# and overwrites its markdown (backing up the old page + deep reads first).

import re as _re
import shutil as _shutil
from typing import NamedTuple

BACKUP_ROOT = Path("backups")

# First [id](url) on a rendered paper heading: "### N. [DOI](url) [· [arXiv](..)] — Title".
_PAGE_HEADING_RE = _re.compile(r"^#{2,6}\s+\d+\.\s+\[([^\]]+)\]\(([^)]+)\)")


class _Target(NamedTuple):
    path: Path          # existing docs/journals/*.md page
    short: str          # config short name (e.g. "AoS")
    full: str           # config full name / venue label
    issn: str
    vol: int
    iss: int | None
    when: date          # original page date — regen overwrites this exact file


def _journal_catalog() -> dict[str, dict]:
    """slug -> {short, full, issn, group} for every configured journal."""
    from .render.markdown import _slug
    out: dict[str, dict] = {}
    for gkey, gcfg in _load_groups().items():
        for j in gcfg["journals"]:
            out[_slug(j["short"])] = {
                "short": j["short"], "full": j["full"],
                "issn": j["issn"], "group": gkey,
            }
    return out


def _parse_issue_arg(s: str) -> tuple[int, int | None]:
    """'v54-i1' / '54-1' / '54/1' / '54' → (54, 1) or (54, None)."""
    m = _re.search(r"v?(\d+)(?:[-/ ]i?(\d+))?", s.strip(), _re.I)
    if not m:
        raise ValueError(f"can't parse issue spec {s!r} (try e.g. v54-i1)")
    return int(m.group(1)), (int(m.group(2)) if m.group(2) else None)


def _resolve_rerun_targets(*, only: list[str] | None, only_group: list[str] | None,
                           recent: int | None, issue: str | None) -> list[_Target]:
    """Find the docs/journals/*.md pages to re-generate, from journal/group/issue
    filters and an optional 'most recent N issues per journal' cap."""
    from collections import defaultdict
    from .render.markdown import (
        JOURNALS_DIR, _slug, _journal_slug_from_stem,
        _journal_vol_iss_from_stem, _parse_date_from_stem,
    )
    catalog = _journal_catalog()
    only_slugs = {_slug(s) for s in only} if only else None
    only_groups = set(only_group) if only_group else None

    candidates: list[_Target] = []
    for p in sorted(JOURNALS_DIR.glob("*.md")):
        slug = _journal_slug_from_stem(p.stem)
        meta = catalog.get(slug)
        if meta is None:
            continue  # orphan page (journal not in config) — no ISSN to refetch
        if only_slugs is not None and slug not in only_slugs:
            continue
        if only_groups is not None and meta["group"] not in only_groups:
            continue
        vol, iss = _journal_vol_iss_from_stem(p.stem)
        if vol is None:
            continue  # can't target an issue without a volume in the filename
        dstr = _parse_date_from_stem(p.stem)
        when = date.fromisoformat(dstr) if dstr else date.today()
        candidates.append(
            _Target(p, meta["short"], meta["full"], meta["issn"], vol, iss, when)
        )

    if issue is not None:
        tv, ti = _parse_issue_arg(issue)
        candidates = [c for c in candidates
                      if c.vol == tv and (ti is None or c.iss == ti)]

    if recent:
        by_slug: dict[str, list[_Target]] = defaultdict(list)
        for c in candidates:
            by_slug[_slug(c.short)].append(c)
        picked: list[_Target] = []
        for cs in by_slug.values():
            cs.sort(key=lambda c: (c.vol, c.iss or 0), reverse=True)
            picked.extend(cs[:recent])
        candidates = picked

    candidates.sort(key=lambda c: (c.short.lower(), -c.vol, -(c.iss or 0)))
    return candidates


def _page_dois(path: Path) -> list[str]:
    """The paper ids (DOIs) listed on a rendered journal page, in order."""
    if not path.exists():
        return []
    out: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _PAGE_HEADING_RE.match(line)
        if m:
            out.append(m.group(1))
    return out


def _paper_in_issue(p: Paper, vol: int, iss: int | None) -> bool:
    """Whether a snapshot paper belongs to (vol, iss). Matches on the volume/issue
    fields when present, else on the 'vol N' / 'issue M' category strings — older
    snapshots leave volume/issue None but always carry the categories."""
    cats = " ".join(p.categories or []).lower()
    vol_ok = (p.volume is not None and str(p.volume) == str(vol)) or f"vol {vol}" in cats
    if not vol_ok:
        return False
    if iss is None:
        return True
    return (p.issue is not None and str(p.issue) == str(iss)) or f"issue {iss}" in cats


def _assemble_issue_papers(t: _Target, from_snapshot: Path | None, *,
                           fill_abstract: bool = True) -> list[Paper]:
    """The paper set for one issue: re-fetched from Crossref/JMLR (default,
    self-healing — picks up articles the original scrape missed) or loaded from a
    snapshot (corpus JSON) for fast prompt iteration."""
    if from_snapshot:
        papers = [p for p in _load_papers(from_snapshot)
                  if p.venue == t.full and _paper_in_issue(p, t.vol, t.iss)]
        log.info("snapshot: %d papers for %s v%s i%s", len(papers),
                 t.short, t.vol, t.iss if t.iss is not None else "*")
        return [p for p in papers if p.abstract]
    if t.issn == "jmlr":
        papers = jmlr_fetch_latest(volume=t.vol)  # JMLR has no issues — whole volume
    else:
        papers = fetch_issue(t.issn, t.full, t.vol, t.iss, fill_abstract=fill_abstract)
    if fill_abstract:
        papers = [p for p in papers if p.abstract]
        fill_arxiv_links(papers)
    return papers


def _backup_issue(t: _Target, stamp: str) -> None:
    """Copy the issue page and its deep-read pages to backups/<stamp>/ before
    they're overwritten."""
    from .render.markdown import DEEP_READS_DIR
    from .deep_read import _slug as _dr_slug
    dest = BACKUP_ROOT / stamp
    (dest / "journals").mkdir(parents=True, exist_ok=True)
    if t.path.exists():
        _shutil.copy2(t.path, dest / "journals" / t.path.name)
    dr_n = 0
    for doi in _page_dois(t.path):
        cand = DEEP_READS_DIR / f"{t.when.isoformat()}-{_dr_slug(doi)}.md"
        if cand.exists():
            (dest / "deep_reads").mkdir(parents=True, exist_ok=True)
            _shutil.copy2(cand, dest / "deep_reads" / cand.name)
            dr_n += 1
    log.info("backed up %s + %d deep-read page(s) → %s", t.path.name, dr_n, dest)


def rerun(*, only: list[str] | None = None, only_group: list[str] | None = None,
          recent: int | None = None, issue: str | None = None,
          from_snapshot: Path | None = None, backup: bool = True,
          dry_run: bool = False, skip_pdf: bool = False,
          model: str | None = None,
          extra_papers: list[Paper] | None = None,
          check_completeness: bool = True) -> list[Path]:
    """Re-generate published journal issue pages in place with current prompts.

    Overwrites each targeted ``docs/journals/<date>-<short>-vN-iM.md`` (and the
    matching deep-read pages) by re-running score → summarize → render → deep read
    for that issue, pinned to the page's original date. Old pages are backed up
    (timestamped) first unless ``backup=False``.

    ``extra_papers`` (used by the completeness checker's --refetch --rerun) are
    merged into whichever targeted issue they belong to, deduped by paper_id —
    so articles the issue scrape missed get added back on regeneration.
    """
    load_dotenv()
    interests_text = Path("config/interests.yaml").read_text(encoding="utf-8")
    import yaml as _yaml
    th_deepread = float((_yaml.safe_load(interests_text) or {}).get(
        "score_threshold_deepread", 6))

    targets = _resolve_rerun_targets(only=only, only_group=only_group,
                                     recent=recent, issue=issue)
    if not targets:
        log.error("rerun: no journal issue pages match the given filters")
        return []

    log.info("rerun: %d issue page(s) targeted:", len(targets))
    for t in targets:
        log.info("  %s  (%s vol %s issue %s · %s)", t.path.name, t.short, t.vol,
                 t.iss if t.iss is not None else "*", t.when)

    if dry_run:
        for t in targets:
            try:
                assembled = _assemble_issue_papers(t, from_snapshot, fill_abstract=False)
            except Exception as e:  # noqa: BLE001
                log.warning("  [dry-run] %s: assemble failed: %s", t.path.name, e)
                continue
            old = set(_page_dois(t.path))
            new_ids = {p.paper_id for p in assembled}
            log.info("  [dry-run] %s: page=%d source=%d (+%d new, -%d gone)%s",
                     t.path.name, len(old), len(assembled),
                     len(new_ids - old), len(old - new_ids),
                     "; would back up page + deep reads" if backup else "")
        log.info("rerun dry-run: wrote nothing, called no LLM")
        return []

    model = model or JOURNALS_MODEL
    client = SJTUClient()
    from datetime import datetime
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    out_paths: list[Path] = []
    for t in targets:
        try:
            papers = _assemble_issue_papers(t, from_snapshot)
        except Exception as e:  # noqa: BLE001
            log.warning("rerun: assemble failed for %s — skipping: %s", t.path.name, e)
            continue
        if extra_papers:
            have = {p.paper_id for p in papers}
            added = [p for p in extra_papers
                     if _paper_in_issue(p, t.vol, t.iss) and p.paper_id not in have]
            if added:
                log.info("rerun: merging %d extra (recovered) paper(s) into %s",
                         len(added), t.path.name)
                papers.extend(added)
        if not papers:
            log.warning("rerun: no papers for %s — skipping", t.path.name)
            continue
        if backup:
            _backup_issue(t, stamp)
        out = _process_issue(
            papers, t.short, t.full, str(t.vol),
            str(t.iss) if t.iss is not None else None,
            when=t.when, client=client, interests_text=interests_text,
            model=model, th_deepread=th_deepread, skip_pdf=skip_pdf,
            issn=t.issn, check_completeness=check_completeness,
        )
        if out.resolve() != t.path.resolve():
            log.warning("rerun: wrote %s but target was %s (slug mismatch?)",
                        out.name, t.path.name)
        out_paths.append(out)
        log.info("rerun: regenerated %s (%d papers)", out, len(papers))

    if out_paths:
        update_index()
    report_token_usage(client, "journals", date.today())
    return out_paths


def _setup_logging(log_dir: str = "logs") -> None:
    from datetime import date
    from pathlib import Path

    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    Path(log_dir).mkdir(exist_ok=True)
    from .logsetup import host_tag
    log_file = Path(log_dir) / f"journals-{date.today().isoformat()}-{host_tag()}.log"

    root = logging.getLogger()
    root.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(ch)

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    root.addHandler(fh)

    # httpx request lines are noisy on console; keep them in the file only
    console_httpx = logging.getLogger("httpx")
    console_httpx.setLevel(logging.WARNING)
    fh_httpx = logging.FileHandler(log_file, encoding="utf-8")
    fh_httpx.setFormatter(logging.Formatter(fmt, datefmt=datefmt))
    fh_httpx.setLevel(logging.INFO)
    console_httpx.addHandler(fh_httpx)
    console_httpx.propagate = False


def main(argv: list[str] | None = None) -> int:
    _setup_logging()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", default=None,
                    help="Comma-separated subset of journal short names to fetch "
                         "(e.g. JMLR,AoS). See config/journals.yaml for the list.")
    ap.add_argument("--only-group", default=None,
                    help="Comma-separated subset of group keys to fetch "
                         "(e.g. core,applied). Skips all journals outside these "
                         "groups. See config/journals.yaml for the group list.")
    ap.add_argument("--jmlr-n", type=int, default=None,
                    help="Cap how many recent JMLR papers to pull. "
                         "Default: no cap (take entire current volume, ~50).")
    ap.add_argument("--jmlr-vol", type=int, default=None,
                    help="Override JMLR volume (default: current year - 1999).")
    ap.add_argument("--n-issues", type=int, default=1,
                    help="How many recent issues to pull from each quarterly "
                         "journal (AoS/JASA/JRSSB/Biometrika). "
                         "Default 1 (latest only). Use 4 for a full year, 8 for two.")
    ap.add_argument("--label", default=None,
                    help="Override the output filename suffix "
                         "(default: '<year>Q<n>' or '<year>Q<n>-Nissues').")
    ap.add_argument("--skip-pdf", action="store_true",
                    help="Don't download PDFs for high-relevance papers.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Fetch metadata + abstracts only; skip LLM and rendering.")
    ap.add_argument("--save-papers", type=Path, default=None, metavar="PATH",
                    help="After fetching (before LLM), dump papers to PATH as JSON. "
                         "Combine with --dry-run for a pure 'fetch only' step.")
    ap.add_argument("--load-papers", type=Path, default=None, metavar="PATH",
                    help="Skip fetching and load papers from PATH. Lets you "
                         "iterate on prompts / models without re-scraping.")
    ap.add_argument("--retry-broken", action="store_true",
                    help="With --load-papers: only re-summarize papers whose "
                         "previous LLM output was broken (empty / truncated JSON / "
                         "missing topic+key_techniques). Keeps existing scores. "
                         "Saves the fixed summaries back to the JSON.")
    ap.add_argument("--no-dedup", action="store_true",
                    help="Don't filter against data/seen_papers.json and don't "
                         "update it. Use this to re-render an issue you've "
                         "already published.")
    ap.add_argument("--no-completeness-check", action="store_true",
                    help="Skip the per-issue '目录核对' badge (which diffs the "
                         "scraped articles against the issue's authoritative TOC "
                         "via OpenAlex). On by default for both normal runs and "
                         "--rerun.")

    # ── rerun mode: re-generate already-published issue pages in place ───────
    g = ap.add_argument_group(
        "rerun (re-generate published issue pages with the current prompts)")
    g.add_argument("--rerun", action="store_true",
                   help="Rerun mode: overwrite existing docs/journals/*.md pages "
                        "(scoped by --only / --only-group / --rerun-recent / "
                        "--issue) by re-running the LLM stack and pinning each "
                        "page to its original date. Backs up the old page + deep "
                        "reads first. NOT the same as `python -m research_news."
                        "rerun` (which only repairs garbled summary blocks).")
    g.add_argument("--rerun-recent", type=int, default=None, metavar="N",
                   help="Rerun the N most recent issues per targeted journal.")
    g.add_argument("--issue", default=None, metavar="vNN-iMM",
                   help="Rerun one specific issue (e.g. v54-i1); best with --only.")
    g.add_argument("--from-snapshot", type=Path, default=None, metavar="PATH",
                   help="Rerun source: load papers from a corpus JSON instead of "
                        "re-fetching Crossref (fast prompt iteration; won't pick "
                        "up articles the original scrape missed).")
    g.add_argument("--no-backup", action="store_true",
                   help="With --rerun: don't back up the pages being overwritten.")
    args = ap.parse_args(argv)

    if args.load_papers and args.save_papers:
        ap.error("--load-papers and --save-papers are mutually exclusive")
    if args.retry_broken and not args.load_papers:
        ap.error("--retry-broken requires --load-papers")
    rerun_only = ("--rerun-recent", "--issue", "--from-snapshot", "--no-backup")
    if not args.rerun and (args.rerun_recent is not None or args.issue
                           or args.from_snapshot or args.no_backup):
        ap.error(f"{', '.join(rerun_only)} require --rerun")

    only = [s.strip() for s in args.only.split(",")] if args.only else None
    only_group = [s.strip() for s in args.only_group.split(",")] \
        if args.only_group else None

    if args.rerun:
        rerun(only=only, only_group=only_group, recent=args.rerun_recent,
              issue=args.issue, from_snapshot=args.from_snapshot,
              backup=not args.no_backup, dry_run=args.dry_run,
              skip_pdf=args.skip_pdf,
              check_completeness=not args.no_completeness_check)
        return 0

    run(only=only, only_group=only_group,
        dry_run=args.dry_run, jmlr_n=args.jmlr_n,
        jmlr_vol=args.jmlr_vol, n_issues=args.n_issues, label=args.label,
        skip_pdf=args.skip_pdf,
        save_papers=args.save_papers, load_papers=args.load_papers,
        retry_broken=args.retry_broken,
        dedup=not args.no_dedup,
        check_completeness=not args.no_completeness_check)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
