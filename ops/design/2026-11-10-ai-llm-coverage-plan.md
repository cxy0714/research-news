# AI / 大模型内容覆盖方案

> 状态：设计稿（待拍板，未实施）
> 日期：2026-11-10
> 适用范围：research-news 现有「每日 arXiv+Hexagon / 期刊 / 讲座 / 会议专题」之外的第四条内容线
> 结论一句话：**会议论文基本全公开，但不要把 AI 论文直接塞进现有日报**；建议做成「AI 雷达（轻量、每日/每周）+ 会议专题（按届、队列式）」双轨，复用现有 Paper / 打分 / 精读 / 渲染 / 去重设施。

---

## 0. TL;DR

1. **会议论文公开性**：ML 主流会议（NeurIPS、ICML、ICLR、ACL 家族、CVPR/ICCV、AAAI、IJCAI、COLT/AISTATS/UAI、TMLR）**官方 proceedings 全部免费公开**（摘要 + PDF）。真正的付费墙只剩 ACM DL 系（KDD/WWW/SIGIR/CHI）——但这些论文几乎都有 arXiv 版，用「DOI/DBLP 元数据 + arXiv 全文」组合即可绕过。
2. **"公开"不等于"能批量下"**：arXiv 明确要求 ≥3 秒/请求，ACM 禁止批量抓取；本方案只批量抓**元数据与摘要**，PDF 按需、单篇、限速，且不入 git（沿用 `data/highlights/` 的 `.gitignore` 约定）。
3. **不要扩 `config/sources.yaml` 的 `arxiv.categories`**：cs.CL + cs.LG + cs.AI + cs.CV 每天新增约 1,500–2,500 篇，是现在 5 个统计分类（约 100–200 篇/天）的 10 倍以上，会把统计日报的信号彻底稀释。AI 内容走**独立兴趣档 + 独立阈值 + 独立页面**。
4. **会议 proceedings 不是"追新"工具**：proceedings 通常比 arXiv 晚 1–3 个月上线；它的价值是**补全、权威元数据、评审信号、以及"这篇后来中了哪"**。追新用 arXiv / OpenReview 录用列表，补全用 proceedings。
5. **成本不是瓶颈**：SJTU 配额是 1e9 tokens/周，跑完 3 个大会议（约 15,000 篇打分 + 1,200 篇摘要 + 90 篇精读）≈ 1% 周配额；真正的瓶颈是 LLM 端点 **9 请求/分钟** 的限速和抓取礼仪。所以设计重点是**限速下的排队与断点续跑**，不是省钱。
6. **推荐落地节奏**：P0（AI 雷达，0.5–1 天）→ P1（PMLR + NeurIPS 两个稳定适配器，2–3 天）→ P2（ACL + OpenReview + CVF + arXiv 合并，2–3 天）→ P3（博客/周报/榜单，1–2 天）。

---

## 1. 现有系统给了什么、卡在哪

| 设施 | 位置 | 对 AI 线的复用方式 |
|---|---|---|
| `Paper` 数据模型 | `research_news/models.py` | 扩字段（venue_id / doi / uid / track…），不新建模型 |
| 打分 / 摘要 | `llm/pipeline.py`（`score_papers` / `summarize_paper`） | 直接复用，换 `interests.ai.yaml` 与 `TOPICS_AI` |
| 精读 | `deep_read.py` + `highlights.py` | 复用；AI 精读页 slug 加 `ai-` 前缀，避免与 arXiv 版重复 |
| 卷/期式批量 | `journals.py` + `config/journals.yaml` | 会议「届/卷」= 期刊「期」，最贴近的模板 |
| 队列 + 共享锁 | `xagi.py`、`ops/xagi2026-backfill.md`、`run_xagi_backfill.ps1` | 会议回补直接照抄：一次一格、git 即状态、`Global\research-news-daily` 互斥量 |
| 渲染 | `render/markdown.py` | 建议新增 `render/ai.py`，不往 33KB 的单文件里再塞 |
| 去重 | `dedup.py`（`source:paper_id`） | 需要升级为**规范 id**（DOI/arXiv/标题哈希），否则 arXiv 版与 proceedings 版会各精读一遍 |
| 导航 | `mkdocs.yml` 的 `*-NAV-START/END` 标记 | 每个会议一个自动生成的 nav 段；AI 雷达只进 index + archive 两个入口 |
| Token 记账 | `usage.py`（周配额 1e9） | 新增 `pipeline="ai-daily"` / `"proceedings:<venue>"` 两类即可 |

**两条硬约束（决定了架构）**：

- `SJTUClient` 的 `RateLimiter(max_per_minute=9)`：所有 LLM 调用串行排队。5,000 篇按 8 篇/批 = 625 次调用 ≈ **70 分钟**；30 篇精读（每次 60–180 秒）≈ **1–1.5 小时**。所以批量工作必须**分夜、可续跑**，不能塞进 09:10 的日报。
- `run_daily.ps1` 的命名互斥量：日报、期刊回补、XAGI 共用一把锁。AI 线要么排在其后（10:30 独立任务），要么复用同一把锁做「一格一跑」。

---

## 2. 会议论文到底公开吗？

### 2.1 三档公开性

| 档位 | 含义 | 代表 |
|---|---|---|
| **A. 官方全开放** | 官方站点免费给摘要 + PDF，无登录 | NeurIPS、ICML（PMLR）、ACL 家族（Anthology）、CVPR/ICCV（CVF）、AAAI（OJS）、IJCAI、COLT/AISTATS/UAI（PMLR）、TMLR |
| **B. 评审也公开** | 除论文外还能拿到评审意见、打分、作者回复、decision | ICLR、NeurIPS（OpenReview 评审）、TMLR、COLM、大量 workshop |
| **C. 正式版付费** | 出版商版本在 ACM DL / IEEE Xplore 后面；但同内容的开放版或 arXiv 版通常存在 | KDD、WWW、SIGIR、CHI（ACM）；CVPR/ICCV 的 IEEE 正式版（CVF 有开放版） |

> 实践结论：**A 档足够覆盖 90% 的 AI 论文**；C 档不抓 PDF，只取 Crossref/DBLP 元数据，再用标题匹配 arXiv 全文。

### 2.2 逐会清单（2026-11-10 实测/核对）

| 会议 | 官方站点 | 能拿到 | 元数据特点 | 规模 | 上线时滞 | 抓法 |
|---|---|---|---|---|---|---|
| **NeurIPS** | `proceedings.neurips.cc` | 摘要页 + PDF | Main / Datasets&Benchmarks 分轨、作者、BibTeX | 2024 届 **4,493 篇**（页面实测） | 会后 2–3 月 | 届列表 → 逐篇摘要页（约 1 请求/篇） |
| **ICML** | `proceedings.mlr.press` | 卷页 + 逐篇摘要/PDF/BibTeX | PMLR 卷号（2026 = v306，2025 = v267）；有 RSS | 数千 | 会后 1–3 月 | 卷页 → 逐篇；或直接解析其 GitHub 源仓库 |
| **ICLR** | `openreview.net` | 摘要 + PDF + **评审/decision** | API v2 字段最全（keywords、venue、pdf） | 数千投稿 | 录用即公开 | API 批量 notes（1000/页，最省请求） |
| **ACL / EMNLP / NAACL / EACL** | `aclanthology.org` | **卷页内联摘要** + PDF + DOI | 每卷 BibTeX / MODS XML；DOI 覆盖率极高 | 2024 ACL-long **864 篇**（实测） | 会后 1–2 月 | **一个卷页一次抓完**（最省请求） |
| **CVPR / ICCV** | `openaccess.thecvf.com` | 逐篇 HTML + PDF | 按天分组；开放版与正式版内容一致 | 2,000–3,000 | 会后 ~1 月 | 总列表（`?day=all`）→ 逐篇 |
| **ECCV** | `ecva.net` | PDF | 与 CVF 类似 | 1,000–2,000 | 会后 | 同 CVF |
| **AAAI** | `ojs.aaai.org` | PDF | OJS issue 结构，一年一 issue | 2,000–3,500/年 | 会后 | issue 目录 → 文章页 |
| **IJCAI** | `ijcai.org/proceedings` | PDF | 年份索引 | ~800 | 会后 | 年索引 |
| **COLT / AISTATS / UAI / ALT / CLeaR** | PMLR | 同 ICML | 卷号 | 数百–千 | 会后 | 同 PMLR；**与统计兴趣重叠最大，可同时进两条轨道** |
| **TMLR** | OpenReview | 摘要 + PDF + 评审 | 滚动发表（期刊式） | 每月数十 | 即时 | 同 OpenReview |
| **KDD / WWW / SIGIR / CHI** | ACM DL | 摘要免费、PDF 订阅 | DOI / DBLP | 数千 | — | 只取元数据 + arXiv 匹配，**不抓 PDF** |

### 2.3 三个容易踩的坑

1. **时滞**：proceedings 上线晚 1–3 个月，且"届"与日历年不一定对应（NeurIPS 2025 在 2025-12 开、proceedings 2026 年才全）。所以会议页要按**届**建，不要按"今天"建。
2. **轨/卷混杂**：NeurIPS 有 Main 与 D&B；ACL 有 Long / Short / Findings；ICML 有 oral/spotlight/poster（虚拟站）；CVPR 有 main / workshop。**必须把 track 抓下来**，否则"顶会主会"和"workshop 摘要"会混在一个池子里。
3. **"开放获取"≠"可批量下载"**：CVF 页面明确说版权归作者；arXiv 要求 3 秒间隔；OpenReview API 也有速率限制。**元数据 + 摘要可以批量，PDF 必须按需**（精读时才下，且缓存本地）。

---

## 3. 还有哪些平台（按"能拿到什么"分类）

| 类别 | 平台 | 拿得到什么 | 抓法 / 限制 | 建议优先级 |
|---|---|---|---|---|
| **预印本** | arXiv `cs.CL / cs.LG / cs.AI / cs.CV` | 每日新投稿、摘要、PDF | 现成 `arxiv.py`（RSS + API，3s 间隔）；日增 1.5–2.5k | **P0** |
| | Hexagon | 数学/TCS 预印本 | 已有 | 已有 |
| **会议 proceedings** | 见 §2.2 | 权威版元数据 + 摘要 + PDF | 逐站适配器 | **P0–P2** |
| **评审/讨论** | OpenReview（ICLR/NeurIPS/TMLR/COLM） | 摘要、PDF、评审、打分、decision、作者回复 | API v2；**唯一能拿到"争议度/复现问题"的源** | **P1** |
| **录用名单（早于 proceedings）** | 会议虚拟站（NeurIPS/ICML virtual）、OpenReview decision | 录用列表、oral/spotlight/poster 标记、日程 | HTML；比 proceedings 早 1–3 个月，适合"追新" | P1（可选） |
| **索引/元数据** | **DBLP** | 会议/作者/年份的完整论文清单、DOI、链接 | `dblp.org/search/publ/api?format=json`；会议页更新快 | **P1**（做完整性校验） |
| | OpenAlex | 跨库作品、摘要（倒排索引）、引用数、机构 | `api.openalex.org/works?filter=...&per_page=200`；礼貌池加 `mailto` | **P1**（补引用/机构） |
| | Semantic Scholar | 引用图、tldr、venue 归一 | 无 key 时共享池 **429 频繁**（实测） | P2（有 key 再上） |
| | Crossref | DOI、期刊/会议名 | 摘要覆盖差 | P2 |
| **发现/社区** | HF Daily Papers | 每日精选 + upvote 排序 | `huggingface.co/api/daily_papers`；**本机 DNS 不可达**（实测），需镜像 | P2（可选） |
| | Papers with Code | 论文-代码-榜单 | 已重定向到 Hugging Face（实测），**事实下线** | 跳过 |
| | AlphaXiv / arXiv Sanity / Connected Papers | 讨论、相似论文 | 无公开批量 API | 跳过（人工用） |
| **工业界一手** | OpenAI / Anthropic / Google DeepMind / Meta AI / Mistral / Qwen / DeepSeek / Moonshot / Zhipu / MiniMax / xAI 博客 | 模型发布、技术报告、系统卡 | RSS / HTML；量小、信号高 | **P3** |
| | GitHub Releases（vLLM、SGLang、transformers…） | 工程进展 | GitHub API | P3 |
| **榜单/评测** | LMSYS Arena、Artificial Analysis、HELM、LiveBench、SWE-bench | 模型能力对比 | HTML/API；更新频繁、易变 | P3（可做"模型动态"一页） |
| **二次加工** | The Batch、Import AI、Interconnects、Ahead of AI、Latent Space、Simon Willison | 人肉筛选过的趋势 | RSS / 邮件 | P3 |
| **中文** | 机器之心、量子位、新智元、PaperWeekly | 中文解读 | 微信生态，抓取不合规且易碎 | 不做（人工看） |

> 这张表的取舍逻辑：**一手论文（arXiv + proceedings）做深度，索引（DBLP/OpenAlex）做补全与校验，评审（OpenReview）做差异化信号，博客/榜单只做周报里的"一句话动态"**。不要试图把 20 个源都做成日更。

---

## 4. 推荐架构

### 4.1 总体：两条轨道 + 一个共享层

```
[来源层]
  A1  arXiv cs.CL / cs.LG / cs.AI / cs.CV（RSS，日更）
  A2  OpenReview 录用列表（ICLR / NeurIPS / TMLR / COLM）
  B1  PMLR（ICML / AISTATS / COLT / UAI）、NeurIPS proceedings
  B2  ACL Anthology、CVF、AAAI、IJCAI
        ↓
[轨道 A] AI 雷达：    预过滤 → 打分 → 摘要 → 少量精读 ──→ docs/ai/
[轨道 B] 会议专题：    import → 打分 → 摘要 → 精读 → render ──→ docs/conferences/<venue>/
        ↓  两条轨道共用规范 uid：同一篇只打分/精读一次，页面互链
[共享层] Paper/uid · LLM 打分 · deep_read · Markdown 渲染 · seen 集合 · token 记账
```

**为什么分轨而不是合并**：统计日报的阈值（show=4 / highlight=8 / deepread=6）是按"每天 100–200 篇、命中十几篇"调的；AI 论文每天 1,500+ 篇、术语密度高、LLM 容易一律打 7–8 分。混在一起会让统计侧的高相关页面被 AI 灌水，也会让 AI 侧被统计阈值误杀。分轨后各自有独立的 interests、阈值、页面、日配额，互不干扰，但共享底层设施。

### 4.2 轨道 A：AI 雷达

**目标**：每天 10–20 篇值得扫一眼的 AI 论文 + 每周一篇 800–1,200 字综述。不是"全量追踪"，是"高质量抽样"。

**流程**：

```
arXiv 4 类 RSS（约 1,500–2,500 篇）
  → Stage 0 规则预过滤（零 LLM）：保留命中 AI 关键词的、或作者单位在实验室白名单的
  → Stage 1 LLM 打分（约 150–300 篇，8 篇/批，约 20–40 次调用）
  → Stage 2 摘要（score ≥ show，约 15–20 篇）
  → Stage 3 精读（score ≥ deepread 且 每日 ≤2 篇；或你手动收藏）
  → 渲染 docs/ai/YYYY-MM-DD.md
```

**预过滤规则（草案，放在 `config/sources.ai.yaml`）**：

```yaml
prefilter:
  # 标题/摘要命中任一 → 进入打分
  require_any:
    - LLM
    - language model
    - transformer
    - agent
    - reasoning
    - RLHF
    - DPO
    - alignment
    - scaling law
    - pretraining
    - post-training
    - inference
    - RAG
    - retrieval-augmented
    - benchmark
    - evaluation
    - interpretability
    - jailbreak
    - multimodal
  # 命中任一 → 直接丢弃（省 token；误杀靠白名单兜底）
  deny_any:
    - medical image
    - remote sensing
    - autonomous driving
    - speech enhancement
    - recommendation system
    - wireless
  # 这些机构的论文永远进打分（不被 deny 误杀）
  lab_whitelist:
    - DeepSeek
    - Qwen
    - Alibaba
    - ByteDance
    - Moonshot
    - Zhipu
    - MiniMax
    - OpenAI
    - Anthropic
    - Google DeepMind
    - Meta
    - Microsoft Research
    - Tsinghua
    - Peking University
    - Shanghai Jiao Tong University
limits:
  max_scored_per_day: 200
  max_shown: 20
  max_deep_reads_per_day: 2
```

> 预过滤是"省时间"不是"省 token"（配额用不完）。真正要防的是**打分把 9 请求/分钟占满、把日报挤到中午**。所以宁可预过滤严一点，靠"实验室白名单 + 你手动收藏"兜底。

**页面**：
- `docs/ai/index.md`：最近 7 天 top（按 score），加"本周趋势"三句话。
- `docs/ai/YYYY-MM-DD.md`：当日卡片（标题/作者/机构/score/中文摘要/为什么相关/链接/精读链接）。
- `docs/ai/weekly/YYYY-Www.md`：周报（top 20 + 综述）。
- `docs/all_ai.md`：存档索引。
- nav 只放"AI 雷达"一个入口 + 存档，避免每天新增 nav 项。

### 4.3 轨道 B：会议专题

**模型**：一届会议 = 期刊管道里的"一期"。复用 `journals.py` 的"抓取快照 → 打分 → 摘要 → 渲染"骨架，复用 `xagi.py` 的"队列 + 共享锁 + nav 标记"。

**五阶段**：

| 阶段 | 命令 | 产出 | LLM | 可续跑 |
|---|---|---|---|---|
| 1. import | `proceedings import --venue icml2026` | `data/proceedings/<venue>/papers.json`（规范化 Paper + uid） | 否 | 是（按页偏移） |
| 2. score | `proceedings score --venue icml2026 --max 600` | `scores.jsonl` + `papers.json` 回填 | 是 | 是（跳过已有 uid） |
| 3. summarize | `proceedings summarize --venue icml2026 --top 300` | `cards.json`（中文摘要 + topic + 为什么相关） | 是 | 是 |
| 4. read | `proceedings read --venue icml2026 --max 2` | `reads/<uid>.json` + `docs/deep_reads/ai-<uid>.md` | 是 | 是（一次一篇） |
| 5. render | `proceedings render --venue icml2026` | `docs/conferences/<venue>/index.md` + `topics/*.md` + nav | 否 | 幂等 |

**适配器接口（最小面）**：

```python
# research_news/proceedings/base.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Protocol

@dataclass
class RawPaper:
    venue_id: str
    title: str
    authors: list[str]
    abstract: str = ""
    url: str = ""              # 详情页
    pdf_url: str = ""
    track: str = ""            # Main / D&B / Findings / Long ...
    session: str = ""
    doi: str = ""
    arxiv_id: str = ""
    openreview_id: str = ""

class ProceedingsSource(Protocol):
    id: str                                  # "pmlr" | "neurips" | "acl" | "openreview" | "cvf"
    def volumes(self, cfg: dict) -> list[dict]: ...
    def papers(self, cfg: dict, volume: dict) -> Iterable[RawPaper]: ...
    def detail(self, raw: RawPaper) -> RawPaper: ...   # 可选：卷页没摘要时逐篇补
```

**注册表（`config/proceedings.yaml`）**：

```yaml
venues:
  - id: neurips2025
    label: NeurIPS 2025
    adapter: neurips
    year: 2025
    track: ai
    caps: { score: 6000, summarize: 400, deep_read: 30 }
    enabled: false          # 抓完一届再开下一届，避免队列打架
  - id: icml2026
    label: ICML 2026
    adapter: pmlr
    volume: 306
    track: ai
    caps: { score: 4000, summarize: 300, deep_read: 25 }
  - id: iclr2026
    label: ICLR 2026
    adapter: openreview
    venue_id: ICLR.cc/2026/Conference
    track: ai
    caps: { score: 5000, summarize: 400, deep_read: 30 }
  - id: acl2026
    label: ACL 2026
    adapter: acl
    volumes: ["2026.acl-long", "2026.acl-short", "2026.findings-acl"]
    track: ai
    caps: { score: 2000, summarize: 200, deep_read: 20 }
```

**为什么先做 PMLR + NeurIPS**：两者都是**纯静态 HTML、无需 key、无重定向、结构十年没变**，最容易写出稳定适配器；且 PMLR 覆盖 ICML/AISTATS/COLT/UAI——正好和你的统计兴趣重叠最大，一举两得。

### 4.4 数据模型扩展（`models.py`）

```python
@dataclass
class Paper:
    ...                                   # 现有字段不动
    uid: str = ""                         # 规范 id，见 §4.5
    arxiv_id: str = ""                    # 显式 arXiv id（proceedings 记录补全用）
    track: str = "stats"                  # "stats" | "ai"
    venue_id: str = ""                    # "neurips2025" / "icml2026"
    venue_track: str = ""                 # "Main" / "D&B" / "Findings" / "Long"
    session: str = ""                     # 分会场（有则填）
    doi: str = ""
    openreview_id: str = ""
    proceedings_url: str = ""
    code_url: str = ""
    citation_count: int | None = None
    also_in: list[str] = field(default_factory=list)   # 同一篇的其它出处
    tldr_en: str = ""                     # 英文一句话（AI 线可选）
```

> `track` 让所有既有渲染/索引函数多一个维度而不破坏调用方（默认 `"stats"`）。

### 4.5 去重与 arXiv 对齐（这是全案最容易做错的地方）

**问题**：同一篇论文会以三种身份出现——arXiv 预印本（`arxiv:2501.12345`）、OpenReview 投稿（`openreview:abc123`）、proceedings 正式版（`doi:10.xxxx` / 会议页 hash）。如果按 `source:paper_id` 去重，会在三条管道里各精读一遍。

**规范 id（uid）优先级**：

```python
def canonical_uid(p: Paper) -> str:
    if p.doi:            return "doi:" + p.doi.lower()
    if p.arxiv_id:       return "arxiv:" + p.arxiv_id.split("v")[0]
    if p.openreview_id:  return "openreview:" + p.openreview_id
    return "title:" + sha1(normalize_title(p.title))[:12]
```

**对齐流程**（import 阶段执行，零 LLM）：

1. 先查**本地**：`data/llm_scores.jsonl`、`data/highlights.json`、`data/deep_reads_index.json`、`data/conferences/*/papers.json`（标题归一化后精确/近似匹配）。命中 → 写 `also_in`，复用已有摘要与精读，**不再调用 LLM**。
2. 未命中且有标题 → arXiv `ti:"..."` 搜索（最多 5 条），用 `conf.match.title_similarity`（已有）+ 作者姓氏重叠 ≥1 判定；阈值建议 **0.88**（比 XAGI 的 0.58 严，因为这里是"同一篇"而不是"相关"）。
3. 仍无 → 独立记录，`url` 指向 proceedings 页；精读时直接下 proceedings PDF。
4. 合并方向：**以 arXiv 记录为主**（早、有 HTML 全文、已有精读），proceedings 记录只补 `venue_id/venue_track/doi/proceedings_url` 和 `also_in`。

**去重集合**：`data/seen_papers.json` 继续存 `uid`（升级时做一次迁移：把旧的 `arxiv:xxxx` 保持不变，新增 `doi:` / `title:` 键）。分轨不分子集——同一篇在两条轨道只出现一次，但可以在两个页面互链。

### 4.6 打分口径（`config/interests.ai.yaml` 草案）

关键不是"AI 兴趣列表"，而是**明确"什么不值得读"**。建议把定位写成两句话，再给硬规则：

```yaml
researcher: "陈星宇 (Chen Xingyu)"

positioning: |
  AI / 大模型对本人的定位是「二级兴趣 + 方法论交叉」：
  - 广度：作为统计学者理解当代 AI 的主线（预训练 / 后训练 / 推理 / 评测 / 安全），
    不追 SOTA 榜单，读得懂、能形成判断即可；
  - 深度：只在「与统计、因果、高维、计算理论真正接壤」的地方精读，例如
    scaling law 的统计表述、RLHF/偏好学习的统计模型、LLM 评测的测量误差与选择偏差、
    推理的采样/搜索理论、注意力与状态空间模型的近似理论、
    U-statistics / 张量方法在 LLM 分析中的应用。

primary_interests:      # 理论接口：够得着、值得精读
  - learning theory, generalization, optimization for LLMs
  - statistical foundations of RLHF / preference learning / evaluation
  - scaling laws and compute-optimal training (as statistical estimation)
  - inference-time reasoning: sampling, search, verification
  - uncertainty, calibration, probabilistic methods for LLM analysis

secondary_interests:    # 广度：读摘要即可
  - LLM agents, tool use, RAG, memory
  - post-training (SFT / DPO / RLVR), data curation
  - efficient inference (KV cache, quantization, MoE, long context)
  - evaluation and benchmarks (with a measurement angle)
  - interpretability and safety (mechanistic, jailbreak, alignment)
  - multimodal / AI4Science (only when methodologically legible)

out_of_scope:
  - pure systems / infra engineering without a testable claim
  - benchmark-only SOTA chasing
  - medical imaging / remote sensing / autonomous driving applications
```

**打分 rubric（写进 prompt，不是只写在 yaml 里）**：

| 分 | 含义 |
|---|---|
| 9–10 | 提出可检验的理论/统计问题，假设与结果清楚，统计学者能读懂并复用工具；或设计干净、规模足够大、会改变研究判断的实证 |
| 7–8 | 方法或结论有持久价值，讲清了"为什么 work"（有消融/理论解释），与统计工具箱有明确接口 |
| 4–6 | 工程/应用有价值但主要是组合创新；或理论但离统计太远 |
| 1–3 | 纯榜单提升、不可复现、与兴趣无关 |
| 0 | 无关 |

**硬规则**（防 LLM 被术语带跑）：
- 不因出现 "LLM / scaling / emergent" 加分；
- 纯 benchmark / 纯 SOTA 论文**最高 6 分**，除非它同时给出评测方法学（测量误差、选择偏差、污染分析）；
- 有代码 + 数据 + 可复现细节 → 同级内优先；
- 机构/热度不加分（机构只用于预过滤白名单）。

**阈值与配额**（AI 档独立）：

```yaml
score_threshold_show: 5
score_threshold_highlight: 8
score_threshold_deepread: 7
max_deep_reads_per_venue: 30
max_deep_reads_per_day: 2
```

**主题词表（`TOPICS_AI`）**：`llm_pretraining`、`post_training`、`reasoning_test_time`、`agents_tools`、`retrieval_rag`、`evaluation`、`efficiency_inference`、`interpretability_safety`、`multimodal`、`theory_ml`、`ai4science`、`other`。其中 `theory_ml` 与统计轨道交叉，允许同一篇在两个页面出现（用 uid 保证只精读一次）。

### 4.7 渲染与导航

| 页面 | 路径 | 内容 |
|---|---|---|
| 会议总览 | `docs/conferences/<venue>/index.md` | 一句话定位、篇数、主题分布、Top 20、完整论文表（可折叠） |
| 主题页 | `docs/conferences/<venue>/topics/<topic>.md` | 该主题全部卡片（按 score 排） |
| 逐篇精读 | `docs/deep_reads/ai-<uid>.md` | 复用现有精读模板；顶部加"会议 / arXiv 版"徽标 |
| AI 日报 | `docs/ai/YYYY-MM-DD.md` | 当日 top |
| AI 周报 | `docs/ai/weekly/YYYY-Www.md` | 本周 top 20 + 综述 |
| 存档 | `docs/all_ai.md`、`docs/all_journals.md` 式 | 索引 |

**nav 策略（重要）**：**只把每个会议的 `index.md` 放进 nav**，主题页从总览里链出去。否则 10 个会议 × 12 个主题 = 120 个 nav 项，侧边栏会废掉。AI 雷达同理，只放一个入口 + 存档。仍用 `# <VENUE>-NAV-START/END` 标记自动生成，避免手改 `mkdocs.yml`。

### 4.8 调度、限速与并发

```
工作日 09:10  run_daily.ps1        （统计日报，不动）
工作日 10:30  run_ai.ps1           （AI 雷达；拿同一把锁，30 分钟内跑完）
每晚 23:30    run_proceedings.ps1  （会议队列；一次 1 个单元：400 篇打分 或 2 篇精读）
周日 20:00    run_ai_weekly.ps1    （周报）
```

- **限速**：LLM 9 次/分钟是全局共享的。AI 雷达与会议回补不能同时跑（否则互相拖慢）——所以共用一个互斥量，按时间片排队。
- **并发**：目前 `score_papers` 是串行 for 循环。建议在**不改客户端**的前提下加一个 `ThreadPoolExecutor(max_workers=3)` 只包住"批次调度"，`RateLimiter` 本身是线程安全的（有锁），能把 5,000 篇的打分墙钟从 ~70 分钟压到 ~25 分钟；精读仍串行（单篇 60–180 秒，且长输出更容易超时）。
- **断点续跑**：所有阶段写 append-only JSONL（`scores.jsonl` / `cards.jsonl`），启动时按 uid 跳过已完成项。中断、换机、重跑都安全——这正是期刊回补和 XAGI 队列已经验证过的模式。

---

## 5. 成本与时间（以"一届 5,000 篇"为单位）

| 项目 | 数量 | 说明 |
|---|---|---|
| 抓取请求 | ~5,000 次（1.2 请求/秒） | 约 **70 分钟**；有卷页内联摘要的源（ACL）可降到 3–10 次请求 |
| 打分调用 | 625 次（8 篇/批） | 约 **70 分钟**（串行）/ **25 分钟**（3 并发） |
| 摘要调用 | ~400 次（top 8%） | 约 **45 分钟** |
| 精读调用 | 30 次 | 约 **45–90 分钟**（串行） |
| Token | ≈ 1.5M（打分）+ 0.6M（摘要）+ 1.5M（精读）≈ **3.6M** | 占 1e9 周配额 **0.36%** |
| 一次性墙钟 | 约 **4 小时** | 拆成 3–4 个夜间单元即可 |

> 结论：**钱和配额都不是问题，时间是**。三个大会议的首轮全量 ≈ 1% 周配额、12 小时机器时间；之后每年只增量处理新一届。

---

## 6. 分阶段落地

| 阶段 | 工期 | 做什么 | 验收标准 |
|---|---|---|---|
| **P0 AI 雷达** | 0.5–1 天 | `config/interests.ai.yaml`、`config/sources.ai.yaml`、`research_news/ai_daily.py`、`render/ai.py`、`docs/ai/*`、nav + 存档、fixture 测试 | 连跑 3 天：每天打分 ≤200、展示 ≤20、日报不被拖到 10:30 之后；统计日报零变化 |
| **P1 会议框架 + 两个适配器** | 2–3 天 | `proceedings/`（base/registry/CLI）、`adapters/pmlr.py`、`adapters/neurips.py`、队列脚本、venue 页渲染 | ICML 2026 与 NeurIPS 2025 各出一页；30 篇精读；重跑幂等；中断后可续 |
| **P2 扩大覆盖 + 合并** | 2–3 天 | `adapters/acl.py`、`adapters/openreview.py`、`adapters/cvf.py`、DBLP 完整性校验、arXiv 标题合并 | ICLR 2026 / ACL 2025 各一页；arXiv 重复项 ≥60% 被正确合并；无重复精读 |
| **P3 周边信号** | 1–2 天 | 实验室博客 RSS、周报综述、榜单页（可选）、按 track 的 token 记账 | 周报自动生成；token 页能分 `ai-daily` / `proceedings:*` 看 |

每个阶段结束都跑一次 `pytest`（现有 300+ 个测试）+ 一次 `mkdocs build --strict`，避免破坏站点。

---

## 7. 风险与对策

| 风险 | 表现 | 对策 |
|---|---|---|
| **信号稀释** | AI 论文把统计日报的"高相关"挤没 | 双轨 + 独立阈值 + 独立页面；统计侧代码零改动 |
| **评分漂移** | LLM 看到 "LLM/scaling" 就 7–8 分 | 硬规则写进 prompt；用 20 篇人工标注做校准集；每季度复核一次分布 |
| **抓取失礼/封禁** | arXiv 429、CVF/ACL 反爬、ACM 警告 | 1–2 rps、明确 UA、缓存原始页、只抓元数据；PDF 单篇按需；遵守 robots |
| **版权** | PDF 进 git、公开站分发 | PDF 只落本地 `data/`（已在 `.gitignore`），站点只放链接与摘要 |
| **页面膨胀** | 5,000 篇 × 卡片 = 巨型 HTML，Pagefind 变慢 | 页面只渲染 top N + 主题页；全量只进 `papers.json`；分页/折叠 |
| **适配器腐烂** | 站点改版，抓取静默返回 0 篇 | 每站 fixture + "篇数对不上 DBLP/官网"告警（复用 `completeness.py` 思路） |
| **重复精读** | arXiv 版与 proceedings 版各读一遍 | 规范 uid + 本地优先匹配 + `also_in`；精读前查 `deep_reads_index.json` |
| **时滞误判** | 把"去年中的会"当"今天的新论文" | 会议页按届建，卡片显示 `venue + year`，不混入日报时间线 |
| **网络可达性** | HF 在本机不可达（实测）；OpenReview API 域名会 302 | HF 走镜像或跳过；OpenReview 落地时用 `openreview-py` 或带浏览器 UA 复测，失败则回落到 proceedings 页 |

---

## 8. 需要你拍板的 5 个问题

1. **定位**：AI 论文是"广度阅读"（像 astrostats 那样的 gateway），还是"潜在选题"（theory / stat-ML 交叉要深读）？——这决定 rubric 里 `primary` 与 `secondary` 的权重。
2. **子领域取舍**：全都要，还是只留「推理/后训练/理论/评测」四条主线，暂时砍掉 agent、多模态、AI4Science？
3. **每日体量**：AI 雷达每天 5 / 10 / 20 篇？周报要不要？
4. **会议范围**：只顶会主会，还是也收 Findings / workshop / D&B？（后者数量翻倍、噪声大）
5. **非论文内容**：实验室博客、榜单、播客要不要进站？还是只在周报里提一句？

> 我的默认建议：**2（四条主线）+ 3（每天 10 篇、要周报）+ 4（只主会，D&B 单独标记）+ 5（P3 只做博客 RSS，不做榜单）**。你确认后我按 P0 直接开工。

---

## 附录 A：目录 / 配置 / 命令一览

```
config/
  interests.ai.yaml        # AI 档兴趣 + rubric + 阈值
  sources.ai.yaml          # arXiv 分类、预过滤、日配额
  proceedings.yaml         # 会议注册表（adapter / 卷号 / caps）
research_news/
  ai_daily.py              # 轨道 A 入口
  proceedings/
    __init__.py            # CLI: import/score/summarize/read/render/status/backfill
    base.py                # RawPaper / Protocol / canonical_uid / to_paper
    registry.py            # 读 proceedings.yaml，实例化 adapter
    adapters/
      pmlr.py  neurips.py  acl.py  openreview.py  cvf.py
  render/ai.py             # AI 日报 / 周报 / 会议页
  scrapers/openreview.py   # 共享 API 客户端（分页 / 限速 / 重试）
data/
  proceedings/<venue>/
    papers.json  scores.jsonl  cards.jsonl  reads/<uid>.json
  ai/seen.json             # 可选：与全局 seen 合并
ops/
  proceedings-<venue>.md   # 队列（git 即状态）
  design/2026-11-10-ai-llm-coverage-plan.md
docs/
  ai/{index.md, YYYY-MM-DD.md, weekly/YYYY-Www.md}
  conferences/<venue>/{index.md, topics/<topic>.md}
```

```bash
# 轨道 A
python -m research_news.ai_daily --date 2026-11-10
python -m research_news.ai_daily --dry-run          # 只抓 + 预过滤，不调 LLM

# 轨道 B
python -m research_news.proceedings import    --venue icml2026
python -m research_news.proceedings score     --venue icml2026 --max 400
python -m research_news.proceedings summarize --venue icml2026 --top 300
python -m research_news.proceedings read      --venue icml2026 --max 2
python -m research_news.proceedings render    --venue icml2026
python -m research_news.proceedings status
python -m research_news.proceedings backfill   # 队列驱动，一次一个单元
```

## 附录 B：适配器骨架（PMLR 为例）

```python
# research_news/proceedings/adapters/pmlr.py
from __future__ import annotations
import httpx
from bs4 import BeautifulSoup
from ..base import RawPaper

BASE = "https://proceedings.mlr.press"
UA = "research-news/1.0 (+https://github.com/cxy0714/research-news)"

class PMLR:
    id = "pmlr"

    def volumes(self, cfg: dict) -> list[dict]:
        # 卷号直接写死在 config/proceedings.yaml 里更稳；
        # 需要发现新卷时再抓首页 + RSS。
        return [{"volume": cfg["volume"], "url": f"{BASE}/v{cfg['volume']}/"}]

    def papers(self, cfg: dict, volume: dict) -> list[RawPaper]:
        html = httpx.get(volume["url"], headers={"User-Agent": UA}, timeout=40).text
        soup = BeautifulSoup(html, "lxml")
        out = []
        # 选择器按 PMLR 实际页面校准（div.paper 内 title 链接）；先跑 --dry-run 核对条数
        for a in soup.select("div.paper a[href$='.html']"):
            href = a["href"]
            out.append(RawPaper(
                venue_id=cfg["id"],
                title=" ".join(a.get_text(" ", strip=True).split()),
                authors=[],
                url=f"{BASE}/{href.lstrip('/')}",
            ))
        return out

    def detail(self, raw: RawPaper) -> RawPaper:
        soup = BeautifulSoup(
            httpx.get(raw.url, headers={"User-Agent": UA}, timeout=40).text, "lxml"
        )
        raw.abstract = (soup.select_one("#abstract") or soup).get_text(" ", strip=True)
        raw.authors = [s.get_text(strip=True) for s in soup.select("span.authors span")]
        pdf = soup.select_one("a[href$='.pdf']")
        raw.pdf_url = pdf["href"] if pdf else ""
        return raw
```

## 附录 C：2026-11-10 实测/核对记录

| 事实 | 来源 | 状态 |
|---|---|---|
| NeurIPS 2024 主会 + D&B 共 4,493 篇 | `proceedings.neurips.cc/paper_files/paper/2024` | ✅ 实测 |
| ACL 2024 Long 卷 864 篇、摘要内联、DOI 全覆盖 | `aclanthology.org/volumes/2024.acl-long/` | ✅ 实测 |
| PMLR 卷号：ICML 2026=v306、ICML 2025=v267、AISTATS 2026=v300、COLT 2026=v336、UAI 2026=v337 | `proceedings.mlr.press/` | ✅ 实测 |
| CVF ICCV 2025 开放获取（逐篇 HTML + PDF） | `openaccess.thecvf.com/ICCV2025` | ✅ 实测 |
| Papers with Code 已 302 到 Hugging Face | `paperswithcode.com/api/v1/papers/` | ✅ 实测 |
| Hugging Face 在本机 DNS 不可达 | `huggingface.co/api/daily_papers` | ✅ 实测（网络限制，非站点下线） |
| Semantic Scholar 无 key 直接 429 | `api.semanticscholar.org/graph/v1/...` | ✅ 实测 |
| OpenReview API 域名在本机 302 到站点 | `api2.openreview.net/notes` | ⚠️ 本机网络现象，落地时复测 |
| arXiv 4 个 AI 分类的日增量 1,500–2,500 | 估计（按 2026 年投稿量） | ⚠️ 待用 RSS 实数校准 |