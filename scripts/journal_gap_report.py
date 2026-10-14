"""Journal coverage gap report: which issues exist on Crossref but were never
rendered by us?

Coverage ground truth (union of two independent sources):

1. ``docs/journals/*.md`` page names -- ``<date>-<slug(short)>[-v<vol>][-i<iss>]``
   is exactly what we rendered, so it is the authoritative record. Combined
   issue labels survive unchanged (e.g. ``statmed-v45-i20-22``).
2. every run log's ``taking issues: [(vol, iss), ...]`` line -- an issue that was
   taken is either processed or already in ``data/seen_papers.json`` (dedup), so
   the union of all runs is "covered".

Then Crossref ``/journals/<issn>/works`` gives the issues that actually exist in
the window; ``exists - covered`` is the gap to enqueue in
``ops/journal-backfill.md`` -- together with the smallest ``--n-issues`` that
reaches back past the oldest hole.

Usage (from the repo root)::

    python scripts/journal_gap_report.py                     # since 2026-04-01
    python scripts/journal_gap_report.py --since 2025-01-01
    python scripts/journal_gap_report.py --until 2026-10-15   # ignore newer issues

Prints a per-journal table (ASCII) and writes ``logs/journal-gap-report.md``.
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from research_news import netenv  # noqa: E402

netenv.setup_proxy()

import yaml  # noqa: E402

from research_news.render.markdown import _slug  # noqa: E402
from research_news.scrapers.crossref import CROSSREF_BASE, _get_json  # noqa: E402

RE_FETCH = re.compile(r"fetching latest (\d+) issues of (.+?) \(ISSN ([\w-]+)\)")
RE_TAKING = re.compile(r"taking issues: \[(.*?)\]")
RE_STR_PAIR = re.compile(r"\((\d+),\s*'?([\w-]+)'?\)")
RE_PAGE = re.compile(
    r"^\d{4}-\d\d-\d\d-(?P<slug>[a-z0-9-]+?)(?:-v(?P<vol>[\w.]+))?(?:-i(?P<iss>[\w-]+))?\.md$"
)


def covered_from_logs() -> dict[str, set[tuple[str, str]]]:
    covered: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for path in sorted(glob.glob(str(REPO / "logs" / "*.log"))):
        try:
            lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        # A --dry-run logs "taking issues" too but renders nothing, so it must not
        # count as coverage (that would hide a real gap).
        if any("dry-run:" in ln for ln in lines):
            continue
        pending = None
        for line in lines:
            m = RE_FETCH.search(line)
            if m:
                pending = (m.group(3), m.group(2).strip())
                continue
            if pending is None:
                continue
            m2 = RE_TAKING.search(line)
            if m2:
                issn, _ = pending
                for vol, lab in RE_STR_PAIR.findall(m2.group(1)):
                    covered[issn].add((vol, lab.strip()))
                pending = None
    return covered


def expand(vol: str, label: str) -> set[str]:
    """``('45','20-22')`` -> ``{'45-20','45-21','45-22'}``; ``'S2'`` stays as is."""
    m = re.fullmatch(r"(\d+)-(\d+)", label)
    if m:
        return {f"{vol}-{i}" for i in range(int(m.group(1)), int(m.group(2)) + 1)}
    return {f"{vol}-{label}"}


def load_journals() -> list[tuple[str, str, str]]:
    cfg = yaml.safe_load((REPO / "config" / "journals.yaml").read_text(encoding="utf-8"))
    out: list[tuple[str, str, str]] = []
    for gkey, gcfg in cfg["groups"].items():
        for j in gcfg["journals"]:
            if str(j.get("issn", "")).lower() == "jmlr":  # scraped, no issue numbers
                continue
            out.append((gkey, j["short"], j["issn"]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--since", default="2026-04-01", help="ignore issues before this day")
    ap.add_argument("--until", default=None,
                    help="ignore issues after this day (default: today). Set it to the day of "
                         "your last run so brand-new issues are not reported as gaps.")
    ap.add_argument("--rows", type=int, default=100, help="Crossref works per journal")
    args = ap.parse_args()

    since = date.fromisoformat(args.since)
    until = date.fromisoformat(args.until) if args.until else date.today()

    covered = covered_from_logs()
    pages_by_slug: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for p in (REPO / "docs" / "journals").glob("*.md"):
        m = RE_PAGE.match(p.name)
        if m and m.group("vol"):
            pages_by_slug[m.group("slug")].append((m.group("vol"), m.group("iss") or ""))

    journals = load_journals()
    slug_to_issn = {_slug(short): issn for _g, short, issn in journals}
    for slug, items in pages_by_slug.items():
        issn = slug_to_issn.get(slug)
        if issn:
            for vol, iss in items:
                covered[issn].add((vol, iss))

    print(f"window: {since.isoformat()} .. {until.isoformat()}")
    report = [f"# Journal gap report ({since.isoformat()} .. {until.isoformat()})", ""]
    gaps = 0
    for gkey, short, issn in journals:
        got: set[str] = set()
        for vol, lab in covered.get(issn, set()):
            got |= expand(vol, lab)
        try:
            items = _get_json(
                f"{CROSSREF_BASE}/journals/{issn}/works",
                params={"filter": "type:journal-article", "sort": "published",
                        "order": "desc", "rows": args.rows},
            )["message"]["items"]
        except Exception as e:  # noqa: BLE001
            print(f"!!   {gkey:10} {short:24} crossref failed: {type(e).__name__}")
            continue

        exists: dict[tuple[str, str], int] = {}
        order: list[tuple[str, str]] = []
        for it in items:
            vol, iss = it.get("volume"), it.get("issue")
            if vol is None or iss is None:
                continue
            dp = (it.get("published") or it.get("published-online") or it.get("issued") or {}).get(
                "date-parts", [[None]])[0]
            try:
                pub = date(int(dp[0]), int(dp[1]) if len(dp) > 1 else 1,
                           int(dp[2]) if len(dp) > 2 else 1)
            except (TypeError, ValueError):
                continue
            if pub < since or pub > until:
                continue
            key = (str(vol), str(iss))
            if key not in exists:
                exists[key] = 0
                order.append(key)
            exists[key] += 1

        missing = [k for k in order if not (expand(*k) & got)]
        if not missing:
            print(f"ok   {gkey:10} {short:24} covered")
            continue
        gaps += 1
        n_issues = max(order.index(k) for k in missing) + 1
        est = sum(exists[k] for k in missing)
        labels = ", ".join(f"v{v}-i{i}" for v, i in missing)
        print(f"GAP  {gkey:10} {short:24} need --n-issues {n_issues:2}  ~{est:3} new papers  missing: {labels}")
        report.append(f"- **{short}** ({gkey}): `--n-issues {n_issues}`"
                      f" (est. ~{est} new papers; missing {labels})")

    out = REPO / "logs" / "journal-gap-report.md"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"\njournals with gaps: {gaps} / {len(journals)}")
    print(f"report -> {out}")


if __name__ == "__main__":
    main()
