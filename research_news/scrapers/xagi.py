"""Import the XAGI (交叉智能大会) schedule into the conference pipeline.

The conference site (https://www.x-agi.cc/schedule/) publishes one page with
every session and talk: session number/title/time/room, the chair(s), and for
each talk the speaker, affiliation, official abstract and speaker bio. Unlike
OCIS season pages (Google Sites, JS-heavy) this page is regular, semantic HTML,
so the import is a **deterministic** BeautifulSoup parse — no LLM, no API key.

Output: ``data/conferences/xagi2026/sessions.json`` (one row per session, one
row per talk) plus the raw saved HTML, so a later re-parse works offline.
Downstream, ``research_news.xagi`` matches each talk to its paper(s) and
deep-reads it.
"""
from __future__ import annotations

import json
import logging
import re
from datetime import date, datetime
from pathlib import Path

from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

SCHEDULE_URL = "https://www.x-agi.cc/schedule/"
CONF_DIR = Path("data/conferences/xagi2026")
SESSIONS_PATH = CONF_DIR / "sessions.json"
HTML_PATH = CONF_DIR / "schedule.html"

CONFERENCE = {
    "name": "XAGI 2026 交叉智能大会",
    "short": "XAGI 2026",
    "url": SCHEDULE_URL,
    "year": 2026,
    "dates": "2026.10.16-18",
    "venue": "北京 · 友谊宾馆（友谊宫二层）",
}

_WS_RE = re.compile(r"[\s\u200b\xa0]+")
_DATE_RE = re.compile(r"(?:(\d{4})\s*年\s*)?(\d{1,2})\s*月\s*(\d{1,2})\s*日")
_WEEKDAY_RE = re.compile(r"周[一二三四五六日天]")


def _text(el) -> str:
    """Whitespace-normalized text of a soup element ('' for None)."""
    if el is None:
        return ""
    return _WS_RE.sub(" ", el.get_text(" ", strip=True)).strip()


def _section_text(details, kind: str) -> tuple[str, str]:
    """(affiliation, body) from a ``section[data-profile-section=<kind>]``.

    The section holds an ``<h4>`` label, an optional affiliation paragraph
    (``.schedule-person-profile__affiliation``) and the actual text paragraphs.
    """
    sec = details.select_one(f'section[data-profile-section="{kind}"]')
    if sec is None:
        return "", ""
    aff = _text(sec.select_one(".schedule-person-profile__affiliation"))
    body = " ".join(_text(p) for p in sec.find_all("p")
                    if "schedule-person-profile__affiliation" not in (p.get("class") or []))
    return aff, _WS_RE.sub(" ", body).strip()


def _person(details) -> dict:
    if details is None:
        return {"name": "", "org": "", "affiliation": "", "bio": ""}
    aff, bio = _section_text(details, "bio")
    return {
        "name": _text(details.select_one(".schedule-person-identity strong")),
        "org": _text(details.select_one(".schedule-person-identity__affiliation-text")),
        "affiliation": aff,
        "bio": bio,
    }


def _parse_period_heading(heading: str, default_year: int) -> tuple[str | None, str]:
    """'10 月 17 日 · 周六 · 上午' → ('2026-10-17', '上午')."""
    m = _DATE_RE.search(heading or "")
    if not m:
        return None, ""
    year = int(m.group(1) or default_year)
    try:
        d = date(year, int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None, ""
    period = "上午" if "上午" in heading else "下午" if "下午" in heading else ""
    return d.isoformat(), period


def _weekday_cn(d: date) -> str:
    return "周" + "一二三四五六日"[d.weekday()]


def parse_schedule(html: str) -> dict:
    """Parse the saved schedule page into the catalog dict (no network, no LLM).

    Returns ``{conference, source, fetched_at, sessions: [...]}`` where each
    session is ``{no, id, date, weekday, period, title, time, room, chairs,
    talks: [{no, id, title, time, speaker, org, affiliation, abstract, bio}]}``.
    """
    soup = BeautifulSoup(html or "", "lxml")
    year = CONFERENCE["year"]
    title_el = soup.find("title")
    m = re.search(r"(\d{4})", _text(title_el))
    if m:
        year = int(m.group(1))

    sessions: list[dict] = []
    for card in soup.select("article.schedule-topic-card"):
        no_txt = _text(card.select_one(".schedule-topic-card__number"))
        m = re.search(r"(\d+)", no_txt)
        no = int(m.group(1)) if m else len(sessions) + 1

        grp = card.find_parent("section", class_="schedule-period-group")
        heading = _text(grp.select_one("header h3")) if grp else ""
        iso, period = _parse_period_heading(heading, year)
        if iso and "上午" in heading:
            period = "上午"
        elif iso and "下午" in heading:
            period = "下午"

        venue = _text(card.select_one("[data-session-venue]"))
        detail = _text(card.select_one("[data-session-venue-detail]"))
        room = _WS_RE.sub("", venue + detail) if detail else venue

        chairs = [_person(d) for d in
                  card.select("section.session-chair details.schedule-person-profile")]

        talks: list[dict] = []
        body = card.select_one(".card-body")
        for item in (body.select(".session-list > .session-item") if body else []):
            if "session-item--speaker" not in (item.get("class") or []):
                continue
            n = len(talks) + 1
            title_el = item.select_one(".session-speaker__talk-title span")
            speaker = _person(item.select_one("details.schedule-person-profile"))
            _, abstract = _section_text(item.select_one("details.schedule-person-profile"),
                                        "abstract")
            talks.append({
                "no": n,
                "id": f"sess{no:02d}-t{n}",
                "title": _text(title_el),
                "time": _text(item.select_one(".schedule-inline-time")),
                "speaker": speaker["name"],
                "org": speaker["org"],
                "affiliation": speaker["affiliation"],
                "abstract": abstract,
                "bio": speaker["bio"],
            })

        sess_date = date.fromisoformat(iso) if iso else None
        sessions.append({
            "no": no,
            "id": f"sess{no:02d}",
            "date": iso,
            "weekday": _weekday_cn(sess_date) if sess_date else "",
            "period": period,
            "title": _text(card.select_one(".schedule-topic-card__title")),
            "time": _text(card.select_one(".schedule-topic-card__time")),
            "room": room,
            "chairs": chairs,
            "talks": talks,
        })

    # Chairs are plain names/affiliations in the catalog; bios are context only.
    for s in sessions:
        for c in s["chairs"]:
            c.pop("affiliation", None)
    return {
        "conference": CONFERENCE,
        "source": SCHEDULE_URL,
        "fetched_at": datetime.now().isoformat(timespec="seconds"),
        "sessions": sessions,
    }


def fetch_html(url: str = SCHEDULE_URL, *, timeout: float = 40) -> str:
    """GET the schedule page with a browser UA (the site is Cloudflare-ish)."""
    import httpx

    ua = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
    with httpx.Client(timeout=timeout, headers={"User-Agent": ua},
                      follow_redirects=True) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text


def load_sessions(path: Path = SESSIONS_PATH) -> dict:
    """The saved catalog (empty skeleton when it doesn't exist yet)."""
    if not path.exists():
        return {"conference": CONFERENCE, "source": SCHEDULE_URL,
                "sessions": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        log.warning("cannot read %s: %s", path, e)
        return {"conference": CONFERENCE, "source": SCHEDULE_URL,
                "sessions": []}
    if isinstance(data, list):  # tolerate a bare session list
        return {"conference": CONFERENCE, "source": SCHEDULE_URL,
                "sessions": data}
    return data


def save_sessions(data: dict, path: Path = SESSIONS_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def merge_sessions(old: dict, new: dict) -> dict:
    """Keep per-talk match/read state when re-importing an updated page.

    Session metadata comes from the fresh parse; a talk's ``paper`` (match
    result) is carried over by talk id, since the deep read is expensive and
    the schedule text rarely changes. New talks start with no state; talks
    that disappeared are dropped.
    """
    prev = {t.get("id"): t for s in (old.get("sessions") or [])
            for t in (s.get("talks") or []) if t.get("id")}
    for s in new.get("sessions") or []:
        for t in s.get("talks") or []:
            p = prev.get(t.get("id")) or {}
            for key in ("paper", "read", "skip"):
                if p.get(key) is not None:
                    t[key] = p[key]
    return new


def import_schedule(*, html: str | None = None, save_html: bool = True,
                    dry_run: bool = False) -> dict:
    """Fetch (or accept saved HTML), parse, and write the catalog. Returns it."""
    raw = html
    if raw is None:
        raw = fetch_html()
        log.info("fetched %s (%d chars)", SCHEDULE_URL, len(raw))
    data = parse_schedule(raw)
    old = load_sessions()
    data = merge_sessions(old, data)
    sessions = data["sessions"]
    n_talks = sum(len(s["talks"]) for s in sessions)
    log.info("XAGI: %d session(s), %d talk(s), %d with an abstract",
             len(sessions), n_talks,
             sum(1 for s in sessions for t in s["talks"] if t.get("abstract")))
    if dry_run:
        return data
    if save_html:
        HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
        HTML_PATH.write_text(raw, encoding="utf-8")
    save_sessions(data)
    return data


def talk_by_id(data: dict, cell: str) -> tuple[dict | None, dict | None]:
    """('sess02-t1') → (session, talk) or (None, None)."""
    for s in data.get("sessions") or []:
        for t in s.get("talks") or []:
            if t.get("id") == cell:
                return s, t
    return None, None


def iter_talks(data: dict):
    """Yield (session, talk) in schedule order."""
    for s in data.get("sessions") or []:
        for t in s.get("talks") or []:
            yield s, t
