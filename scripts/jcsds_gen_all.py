# -*- coding: utf-8 -*-
"""Merge per-talk files, then regenerate every topic page that has research,
then regenerate the index. One command to refresh the whole conference site."""
import json, subprocess, sys, os
sys.path.insert(0, 'scripts')

# 1. merge per-talk -> per-session
subprocess.run([sys.executable, 'scripts/jcsds_merge.py'], check=True)

# 2. for each group, generate if any of its sessions has a research file
GROUPS = json.load(open('data/conferences/jcsds2026/topic_groups.json', encoding='utf-8'))
import jcsds_gen_topic as T
done = []
for gk, gv in GROUPS.items():
    has = any(os.path.exists(f'data/conferences/jcsds2026/research/sess{i}.json')
              for i in gv['session_idx'])
    if has:
        T.gen(gk)
        done.append(gk)
print(f"generated {len(done)} topic pages")

# 3. regenerate index (picks up topic-page links)
subprocess.run([sys.executable, 'scripts/jcsds_gen_index.py'], check=True)

# 4. refresh nav block in mkdocs.yml
subprocess.run([sys.executable, 'scripts/jcsds_gen_nav.py'], check=True)
