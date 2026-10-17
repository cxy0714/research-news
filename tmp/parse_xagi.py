# -*- coding: utf-8 -*-
"""Scratch: inspect the XAGI 2026 schedule HTML structure."""
import json
import re
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup

html = Path("tmp/xagi_schedule.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "lxml")

print("== period groups ==")
for grp in soup.select("section.schedule-period-group"):
    h = grp.select_one("header h3")
    print(grp.get("id"), "|", h.get_text(" ", strip=True) if h else None)

print("\n== session cards ==")
cards = soup.select("article.schedule-topic-card")
print("n cards:", len(cards))
for card in cards:
    num = card.select_one(".schedule-topic-card__number")
    title = card.select_one(".schedule-topic-card__title")
    tm = card.select_one(".schedule-topic-card__time")
    venue = card.select_one("[data-session-venue]")
    detail = card.select_one("[data-session-venue-detail]")
    print("\n---", card.get("id"), "|", num.get_text(strip=True) if num else None,
          "|", title.get_text(" ", strip=True) if title else None,
          "|", tm.get_text(strip=True) if tm else None,
          "|", venue.get_text(strip=True) if venue else None,
          detail.get_text(strip=True) if detail else None)
    # chair
    for d in card.select("section.session-chair details.schedule-person-profile"):
        nm = d.select_one(".schedule-person-identity strong")
        af = d.select_one(".schedule-person-identity__affiliation-text")
        print("   CHAIR:", nm.get_text(strip=True) if nm else None, "|", af.get_text(strip=True) if af else None)
    body = card.select_one(".card-body")
    if not body:
        print("   (no card-body)")
        continue
    items = body.select(".session-list > .session-item")
    print("   items:", len(items), Counter(" ".join(i.get("class", [])) for i in items))
    for it in items:
        classes = [c for c in it.get("class", []) if c != "session-item"]
        if "session-item--speaker" in it.get("class", []):
            tt = it.select_one(".session-speaker__talk-title")
            title_span = tt.find("span") if tt else None
            time_span = it.select_one(".schedule-inline-time")
            nm = it.select_one(".schedule-person-identity strong")
            af = it.select_one(".schedule-person-identity__affiliation-text")
            abs_sec = it.select_one('section[data-profile-section="abstract"]')
            bio_sec = it.select_one('section[data-profile-section="bio"]')
            print("   TALK:", repr(title_span.get_text(" ", strip=True) if title_span else None),
                  "|", time_span.get_text(strip=True) if time_span else None,
                  "|", nm.get_text(strip=True) if nm else None,
                  "|", af.get_text(strip=True) if af else None,
                  "| abs:", len(abs_sec.get_text(" ", strip=True)) if abs_sec else 0,
                  "| bio:", len(bio_sec.get_text(" ", strip=True)) if bio_sec else 0)
        else:
            print("   OTHER", classes, ":", it.get_text(" ", strip=True)[:120])

print("\n== any panel/discussion-ish classes ==")
all_classes = Counter()
for tag in soup.find_all(True):
    for c in tag.get("class", []):
        if "session" in c or "schedule" in c:
            all_classes[c] += 1
for k, v in sorted(all_classes.items()):
    if "item" in k or "panel" in k or "discuss" in k or "interlude" in k:
        print(f"  {k}: {v}")
