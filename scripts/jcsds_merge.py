# -*- coding: utf-8 -*-
"""Merge per-talk research files (sess<idx>_t<no>.json) into per-session
files (sess<idx>.json), for whichever sessions have per-talk files.
Per-talk files are tiny (one object) so subagent writes never truncate."""
import json, glob, re, os
from collections import defaultdict

RDIR = 'data/conferences/jcsds2026/research'
S = json.load(open('data/conferences/jcsds2026/sessions.json', encoding='utf-8'))

per_talk = defaultdict(list)
for f in glob.glob(f'{RDIR}/sess*_t*.json'):
    m = re.search(r'sess(\d+)_t(\d+)\.json$', os.path.basename(f))
    if not m:
        continue
    idx = int(m.group(1))
    try:
        obj = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        print(f"  SKIP bad json {f}: {e}")
        continue
    per_talk[idx].append(obj)

merged = 0
for idx, talks in per_talk.items():
    talks.sort(key=lambda t: int(t.get('no', 0)))
    out = {"session_idx": idx, "talks": talks}
    json.dump(out, open(f'{RDIR}/sess{idx}.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    n_expected = len(S[idx]['talks'])
    flag = '' if len(talks) == n_expected else f'  ⚠ expected {n_expected}'
    print(f"  sess{idx}: {len(talks)} talks, found {sum(1 for t in talks if t.get('found'))}{flag}")
    merged += 1
print(f"merged {merged} sessions")
