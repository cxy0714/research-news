# -*- coding: utf-8 -*-
"""Auto-assign all content sessions to topic pages (~4 sessions each) by theme.
Preserves manually-defined causal-a/b/c. Writes topic_groups.json (merged)."""
import json, sys
sys.path.insert(0, 'scripts')
from jcsds_themes import classify, THEME_ORDER, THEME_LABEL
from collections import defaultdict, OrderedDict

S = json.load(open('data/conferences/jcsds2026/sessions.json', encoding='utf-8'))
existing = json.load(open('data/conferences/jcsds2026/topic_groups.json', encoding='utf-8'))

# sessions already claimed by manual groups
claimed = set()
for g in existing.values():
    claimed.update(g['session_idx'])

# group remaining content sessions by theme
theme_sess = defaultdict(list)
for i, s in enumerate(S):
    if not s['talks']:
        continue
    if i in claimed:
        continue
    k = 'plenary' if s['title'] == 'Plenary Talk' else classify(s['title'])[0]
    theme_sess[k].append(i)

CHUNK = 4
groups = OrderedDict(existing)  # keep manual first

# plenary: all 6 in one page
if theme_sess.get('plenary'):
    groups['plenary'] = {
        "label": "大会报告 Plenary Lectures",
        "en": "Plenary Lectures",
        "session_idx": theme_sess['plenary'],
        "blurb": ""
    }
    del theme_sess['plenary']

# chunk the rest
suffix = [chr(c) for c in range(ord('a'), ord('z')+1)]
for k in THEME_ORDER:
    if k not in theme_sess:
        continue
    idxs = theme_sess[k]
    # chunk into ~4; if last chunk is size 1, merge into previous
    chunks = [idxs[i:i+CHUNK] for i in range(0, len(idxs), CHUNK)]
    if len(chunks) >= 2 and len(chunks[-1]) == 1:
        chunks[-2] += chunks[-1]
        chunks.pop()
    multi = len(chunks) > 1
    for ci, ch in enumerate(chunks):
        key = f"{k}-{suffix[ci]}" if multi else k
        # skip if collides with manual (e.g. causal-a); manual causal already removed via claimed
        label = THEME_LABEL[k]
        if multi:
            label = f"{label} · {ci+1}"
        groups[key] = {
            "label": label,
            "en": "",
            "session_idx": ch,
            "blurb": ""
        }

json.dump(groups, open('data/conferences/jcsds2026/topic_groups.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print(f"total groups: {len(groups)}")
for gk, gv in groups.items():
    nt = sum(len(S[i]['talks']) for i in gv['session_idx'])
    print(f"  {gk:16s} | {len(gv['session_idx'])} sess | {nt:2d} talks | {gv['label']}")
