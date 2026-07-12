# -*- coding: utf-8 -*-
"""Generate the browsable JCSDS 2026 overview page from sessions.json."""
import json, sys
sys.path.insert(0, 'scripts')
from jcsds_themes import classify, THEME_ORDER, THEME_LABEL
from collections import defaultdict, OrderedDict

S = json.load(open('data/conferences/jcsds2026/sessions.json', encoding='utf-8'))
content = [s for s in S if s['talks']]

# theme -> sessions
tgroups = defaultdict(list)
for s in content:
    k = 'plenary' if s['title'] == 'Plenary Talk' else classify(s['title'])[0]
    s['_theme'] = k
    tgroups[k].append(s)

n_sess = len(content)
n_talks = sum(len(s['talks']) for s in content)
speakers = set(t['speaker'] for s in content for t in s['talks'] if t['speaker'])
orgs = set(t['org'] for s in content for t in s['talks'] if t['org'])

DATE_LABEL = OrderedDict([
    ('2026-07-11 星期六', '7 月 11 日（周六）'),
    ('2026-07-12 星期日', '7 月 12 日（周日）'),
    ('2026-07-13 星期一', '7 月 13 日（周一）'),
])

L = []
w = L.append
w("# 第四届统计与数据科学联合会议（JCSDS 2026）")
w("")
w("> 2026 年 7 月 11–13 日 · 贵州 · [官方日程](https://jcsds2026.scimeeting.cn/cn/web/program/31392)")
w("")
w(f"本页是全会日程的**结构化存档与深读入口**。全会共 **6 场大会报告 + {n_talks-6} 场分会报告**，"
  f"分布在 **{n_sess} 个分会场**、21 个会场、3 个会期；涉及讲者约 **{len(speakers)}** 位、单位约 **{len(orgs)}** 家。")
w("")
w("- **主题导航**：按研究方向聚合分会场，每个专题页含摘要检索与逐场精读。")
w("- **完整日程**：页面底部按日期/会场列出全部报告，包含题目、讲者、单位——"
  "即使某场报告暂未检索到对应论文，也能看到「谁在讲、讲什么主题」。")
w("")
w("---")
w("")
w("## 主题导航")
w("")
w("> 精读进度分批推进；「专题页」列为空表示尚未生成，可先在下方完整日程中浏览。")
w("")
w("| 主题 | 分会场 | 报告数 | 专题页 |")
w("|------|:---:|:---:|------|")
# map theme key -> list of (group_key, label) for generated topic pages that exist
import os as _os
_GROUPS = {}
_gpath = f'{ROOT}/topic_groups.json' if False else 'data/conferences/jcsds2026/topic_groups.json'
if _os.path.exists(_gpath):
    _GROUPS = json.load(open(_gpath, encoding='utf-8'))
topic_links = defaultdict(list)
for gk, gv in _GROUPS.items():
    theme_key = gk.split('-')[0]  # 'causal-a' -> 'causal'
    if _os.path.exists(f'docs/conferences/jcsds2026/{gk}.md'):
        # short tag = last segment uppercased
        tag = gk.split('-')[-1].upper()
        topic_links[theme_key].append((gk, tag))

for k in THEME_ORDER:
    if k not in tgroups:
        continue
    sess = tgroups[k]
    nt = sum(len(s['talks']) for s in sess)
    links = topic_links.get(k, [])
    link = "、".join(f"[{tag}]({gk}.md)" for gk, tag in links) if links else "—"
    w(f"| {THEME_LABEL[k]} | {len(sess)} | {nt} | {link} |")
w("")
w("---")
w("")
w("## 完整日程")
w("")

# group by date then room, preserving original order
by_date = OrderedDict()
for s in content:
    by_date.setdefault(s['date'], []).append(s)

def person_str(persons):
    parts = []
    for role in ['Organizing Society', 'Organizer', 'Chair']:
        if role in persons:
            names = '、'.join(p['name'] + (f"（{p['org']}）" if p['org'] else '') for p in persons[role])
            label = {'Organizer': '组织', 'Chair': '主持', 'Organizing Society': '主办'}[role]
            parts.append(f"{label}：{names}")
    return ' · '.join(parts)

for date, sess_list in by_date.items():
    w(f"### {DATE_LABEL.get(date, date)}")
    w("")
    # order rooms by first appearance
    for s in sess_list:
        title = s['title']
        theme = THEME_LABEL.get(s['_theme'], '')
        w(f"<details><summary><b>{s['time']}</b> · {s['room']} · <b>{title}</b>"
          f"（{len(s['talks'])} 场）</summary>")
        w("")
        ps = person_str(s['persons'])
        if ps:
            w(f"*{ps}*")
            w("")
        w("| # | 时间 | 题目 | 讲者 | 单位 |")
        w("|:--:|:--:|------|------|------|")
        for t in s['talks']:
            tt = t['title'].replace('|', '\|')
            w(f"| {t['no']} | {t['time']} | {tt} | {t['speaker']} | {t['org']} |")
        w("")
        w("</details>")
        w("")
    w("")

w("---")
w("")
w("Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)")

open('docs/conferences/jcsds2026/index.md', 'w', encoding='utf-8').write('\n'.join(L))
print("wrote index.md,", len(L), "lines")
