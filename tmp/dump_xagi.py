# -*- coding: utf-8 -*-
"""Scratch: dump the parsed XAGI schedule to JSON for inspection."""
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

html = Path("tmp/xagi_schedule.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "lxml")


def txt(el, sep=" "):
    return re.sub(r"\s+", " ", el.get_text(sep, strip=True)).strip() if el else ""


DATE_RE = re.compile(r"(?:(\d{4})\s*年\s*)?(\d{1,2})\s*月\s*(\d{1,2})\s*日")

sessions = []
for card in soup.select("article.schedule-topic-card"):
    grp = card.find_parent("section", class_="schedule-period-group")
    heading = txt(grp.select_one("header h3")) if grp else ""
    m = DATE_RE.search(heading)
    date = (f"{m.group(1) or 2026}-{int(m.group(2)):02d}-{int(m.group(3)):02d}" if m else None)
    period = "上午" if "上午" in heading else "下午" if "下午" in heading else ""
    room = txt(card.select_one("[data-session-venue]"))
    detail = txt(card.select_one("[data-session-venue-detail]"))
    chairs = []
    for d in card.select("section.session-chair details.schedule-person-profile"):
        chairs.append({
            "name": txt(d.select_one(".schedule-person-identity strong")),
            "org": txt(d.select_one(".schedule-person-identity__affiliation-text")),
            "bio": txt(d.select_one('section[data-profile-section="bio"]')),
        })
    num = txt(card.select_one(".schedule-topic-card__number")).replace("Session", "").strip()
    talks = []
    body = card.select_one(".card-body")
    n = 0
    for it in (body.select(".session-list > .session-item") if body else []):
        if "session-item--speaker" not in (it.get("class") or []):
            continue
        n += 1
        tt = it.select_one(".session-speaker__talk-title")
        title = txt(tt.find("span")) if tt else ""
        tm = txt(it.select_one(".schedule-inline-time"))
        abs_sec = it.select_one('section[data-profile-section="abstract"]')
        talks.append({
            "no": n,
            "title": title,
            "time": tm,
            "speaker": txt(it.select_one(".schedule-person-identity strong")),
            "org": txt(it.select_one(".schedule-person-identity__affiliation-text")),
            "abstract": txt(abs_sec),
            "bio": txt(it.select_one('section[data-profile-section="bio"]')),
        })
    sessions.append({
        "no": int(num) if num.isdigit() else None,
        "date": date,
        "period": period,
        "title": txt(card.select_one(".schedule-topic-card__title")),
        "time": txt(card.select_one(".schedule-topic-card__time")),
        "room": (room + (detail if detail else "")).strip() or room,
        "chairs": chairs,
        "talks": talks,
    })

Path("tmp/xagi_parsed.json").write_text(
    json.dumps(sessions, ensure_ascii=False, indent=1), encoding="utf-8")
print("sessions:", len(sessions), "talks:", sum(len(s["talks"]) for s in sessions))
for s in sessions:
    print(s["no"], s["date"], s["period"], s["title"], "|", s["room"], "|",
          len(s["talks"]), "talks |", ", ".join(c["name"] for c in s["chairs"]))

