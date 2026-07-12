# -*- coding: utf-8 -*-
"""Generate a JCSDS 2026 topic (deep-read) page.

Reads:
  data/conferences/jcsds2026/sessions.json
  data/conferences/jcsds2026/topic_groups.json
  data/conferences/jcsds2026/research/sess<idx>.json  (one file per session, written
      by a research subagent:
      {session_idx, talks:[{no,title,speaker,paper_title,arxiv_id,url,abstract,found,deep_read}]})
Writes:
  docs/conferences/jcsds2026/<group>.md

Usage: python scripts/jcsds_gen_topic.py <group-key>
"""
import json, sys, os

ROOT = 'data/conferences/jcsds2026'
S = json.load(open(f'{ROOT}/sessions.json', encoding='utf-8'))
GROUPS = json.load(open(f'{ROOT}/topic_groups.json', encoding='utf-8'))

DATE_LABEL = {
    '2026-07-11 星期六': '7 月 11 日（周六）',
    '2026-07-12 星期日': '7 月 12 日（周日）',
    '2026-07-13 星期一': '7 月 13 日（周一）',
}

def person_str(persons):
    parts = []
    for role, lab in [('Organizing Society','主办'),('Organizer','组织'),('Chair','主持')]:
        if role in persons:
            names = '、'.join(p['name'] + (f"（{p['org']}）" if p['org'] else '') for p in persons[role])
            parts.append(f"{lab} {names}")
    return ' · '.join(parts)

def gen(group_key):
    g = GROUPS[group_key]
    research = {}
    for i in g['session_idx']:
        rpath = f'{ROOT}/research/sess{i}.json'
        if os.path.exists(rpath):
            rdata = json.load(open(rpath, encoding='utf-8'))
            research[i] = {str(t['no']): t for t in rdata['talks']}

    L = []; w = L.append
    w(f"# {g['label']}")
    w("")
    w(f"> JCSDS 2026 · {g['en']} · [返回会议总览](index.md)")
    w("")
    sess_objs = [S[i] for i in g['session_idx']]
    n_talks = sum(len(s['talks']) for s in sess_objs)
    n_found = sum(1 for i in g['session_idx'] for t in S[i]['talks']
                  if research.get(i, {}).get(t['no'], {}).get('found'))
    w(f"- 含 **{len(sess_objs)} 个分会场 · {n_talks} 场报告**"
      + (f"（已检索到对应论文 {n_found} 场）" if research else "") )
    w("")
    if g.get('blurb'):
        w("## 本专题导览")
        w("")
        w("> 自动生成：归纳本专题主线与建议先看的几场，**不打分、不排名**。")
        w("")
        w(g['blurb'])
        w("")
    w("---")
    w("")

    for i in g['session_idx']:
        s = S[i]
        w(f"## {s['title']}")
        w("")
        meta = f"{DATE_LABEL.get(s['date'], s['date'])} · {s['time']} · {s['room']}"
        w(f"*{meta}*  ")
        ps = person_str(s['persons'])
        if ps:
            w(f"*{ps}*")
        w("")
        for t in s['talks']:
            r = research.get(i, {}).get(t['no'], {})
            w(f"### {t['no']}. {t['title']}")
            w("")
            w(f"**讲者**：{t['speaker']}（{t['org']}）")
            w("")
            if r.get('found') and r.get('url'):
                pt = r.get('paper_title') or t['title']
                links = []
                if r.get('arxiv_id'):
                    links.append(f"[arXiv:{r['arxiv_id']}]({r['url']})")
                else:
                    links.append(f"[论文/主页]({r['url']})")
                if r.get('long_read'):
                    links.append(f"📖 [长篇精读](../../{r['long_read']})")
                w(f"**对应论文**：{pt} · " + " · ".join(links))
                w("")
            elif r and not r.get('found'):
                w("**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）")
                w("")
            if r.get('abstract'):
                w("<details><summary>摘要（原文）</summary>")
                w("")
                w(r['abstract'])
                w("")
                w("</details>")
                w("")
            if r.get('deep_read'):
                w(r['deep_read'])
                w("")
            w("")

    w("---")
    w("")
    w("Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)")
    out = f'docs/conferences/jcsds2026/{group_key}.md'
    open(out, 'w', encoding='utf-8').write('\n'.join(L))
    print(f"wrote {out}, {len(L)} lines, {n_found}/{n_talks} found")

if __name__ == '__main__':
    gen(sys.argv[1])
