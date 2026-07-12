# -*- coding: utf-8 -*-
"""Rewrite the JCSDS nav block in mkdocs.yml between the marker comments,
listing every generated topic page (docs/conferences/jcsds2026/<key>.md)."""
import json, os, re

GROUPS = json.load(open('data/conferences/jcsds2026/topic_groups.json', encoding='utf-8'))
lines = []
for gk, gv in GROUPS.items():
    if gk == 'causal-a':
        continue  # already listed statically above the markers
    if os.path.exists(f'docs/conferences/jcsds2026/{gk}.md'):
        label = gv['label']
        lines.append(f"    - {label}: conferences/jcsds2026/{gk}.md")

block = "\n".join(lines)
yml = open('mkdocs.yml', encoding='utf-8').read()
new = re.sub(
    r"(# JCSDS-NAV-START[^\n]*\n)(.*?)([ \t]*# JCSDS-NAV-END)",
    lambda m: m.group(1) + (block + "\n" if block else "") + m.group(3),
    yml, flags=re.S)
open('mkdocs.yml', 'w', encoding='utf-8').write(new)
print(f"nav: wrote {len(lines)} topic-page entries")
