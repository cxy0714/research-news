# research-news

陈星宇个人定制的研究资讯系统。两条独立管道：

- **每日 arXiv**: 抓 stat.ME / stat.TH / math.ST / econ.EM / astro-ph.IM 新提交，按个人兴趣评分，对高相关论文按主题分组生成中文摘要 + 下载 PDF
- **季度期刊**: 拉 JMLR / AoS / JASA / JRSSB / Biometrika 最新一期（或近 N 期），同样的评分 + 摘要 + 主题分组

都用 SJTU LLM API（默认 GLM-5.1），渲染成 MkDocs Material 站点。

## 快速开始（Windows 11 / PowerShell）

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[docs]"

copy .env.example .env
# 编辑 .env 填入 SJTU_API_KEY

python -m research_news.smoke_test    # 验 API 通
```

兴趣配置：编辑 `config/interests.yaml`（自然语言写就行，LLM 直接读）。

### 依赖

`pip install -e ".[docs]"` 会按 `pyproject.toml` 装全。明细：

| 依赖 | 用途 |
|---|---|
| `httpx` | 全部 HTTP（arxiv / JMLR / Crossref / S2 / OpenAlex / publisher 落地页） |
| `feedparser` | arxiv RSS 解析 |
| `beautifulsoup4` + `lxml` | HTML 解析（JMLR 卷索引页 + arxiv HTML 深读 + 落地页 abstract） |
| `openai` | SJTU API（OpenAI-compatible 协议） |
| `pyyaml` | 读 `config/*.yaml` |
| `python-dotenv` | 加载 `.env` |
| `tenacity` | HTTP / LLM 调用重试 |
| `pypdf` | 高相关论文 PDF 文本抽取（shootout 深读） |
| `jinja2`, `python-dateutil` | 模板 + 日期工具 |
| `mkdocs`, `mkdocs-material` | 文档站点（仅 `.[docs]` extras） |

Linux/macOS 上 `feedparser` 可能装不上 `sgmllib3k`（Python 3.10+ 移除了 sgmllib）。如果碰到，单独装 feedparser==6.0.10 或 6.0.11 一般能绕开，或 `pip install --no-build-isolation` 重试。

## 每日 arXiv 管道

```powershell
# 干跑（只抓不调 LLM）
python -m research_news.daily --dry-run

# 完整跑
python -m research_news.daily

# 指定历史日期（用 arXiv API 拉过去某天的）
python -m research_news.daily --date 2026-05-14
python -m research_news.daily --lookback-days 3   # 周一补周五的

# 临时换模型
$env:DAILY_MODEL="deepseek-chat"; python -m research_news.daily
```

输出：
- `docs/daily/<日期>.md` — 当日报告，按主题分组（因果推断 / 高维 RMT / 非参 / 效率理论 / ...）
- `data/highlights/<topic>/<arxiv_id>.pdf` — 高相关论文（score ≥ 8）的 PDF
- `data/highlights.json` — 高相关论文 manifest（含 score / topic / 摘要 / 关键技术 / DOI 等）
- `logs/<日期>.log` — 详细日志

## 期刊管道

```powershell
# 最新一期（默认）
python -m research_news.journals

# 子集
python -m research_news.journals --only JMLR,AoS

# 近 N 期（quarterly 期刊：4=一年，8=两年；JMLR 默认拉整卷 ~50 篇，--jmlr-n N 限制）
python -m research_news.journals --n-issues 4

# 干跑
python -m research_news.journals --dry-run
```

### 拆开抓取和 LLM 评分

抓取慢（多期可能 15+ 分钟）、LLM 评分慢且贵。拆开后可以抓一次、反复迭代：

```powershell
# 一次性抓取，存盘（每抓完一个期刊就重写 JSON，^C / 崩了不丢之前的）
python -m research_news.journals --n-issues 4 `
    --save-papers data/corpus-2026Q2-4i.json --dry-run

# 从盘上载入跑 LLM（快，可反复）
python -m research_news.journals --load-papers data/corpus-2026Q2-4i.json

# 改 prompt / 换模型再来一遍，用 --label 区分输出文件
$env:JOURNALS_MODEL="deepseek-chat"
python -m research_news.journals --load-papers data/corpus-2026Q2-4i.json --label deepseek
```

`--save-papers` 出的 JSON 就是 `Paper` 字段列表，原子写入（写 `.tmp` 后 rename），可以手动编辑（删 paper、加 abstract、改 title）再 load。

### Abstract backfill 链路

期刊 paper 的 abstract 不总是齐的，按这个顺序回填：

| 层 | 来源 | 备注 |
|---|---|---|
| T1 | Crossref JATS abstract | JMLR / Biometrika 通常一次就齐 |
| T2 | Semantic Scholar by DOI | 中等覆盖 |
| T3 | OpenAlex by DOI | Cloudflare-免疫，对统计期刊高覆盖 |
| T4 | arxiv 标题搜索 | 找预印本（quoted 短语 → unquoted AND-of-words 兜底） |

Discussion / reply / rejoinder / correction 类条目（如 JRSSB discussion issue）在 backfill 之前就过滤掉，省时间又干净。

### 输出

- `docs/journals/<日期>-<年>Q<n>[-Nissues].md` — 按 venue 分组 → topic 子分组
- 高相关论文（score ≥ 8）的 PDF 也落 `data/highlights/<topic>/`（arxiv / JMLR PDF；付费期刊只记 manifest）

## Shootout（评估工具）

调 prompt / 换模型时用。把同一批 paper 跑多个 variant 出对照页：

```powershell
# 多 variant 对照（A baseline / B rich prompt / C-fast deep content / C-deep reasoner）
python -m research_news.shootout 2408.06103 2508.12627 --add-defaults

# 模型横向对比（固定 prompt，每模型一列）
python -m research_news.shootout --source jmlr --n 10 `
    --models deepseek-chat,glm-5.1
```

输出在 `docs/shootout/<日期>.md`。

## 配置文件

| 文件 | 作用 |
|---|---|
| `config/interests.yaml` | 你的研究兴趣 + score 阈值 + 摘要风格。LLM 直接读 |
| `config/sources.yaml` | arxiv 抓哪些 category，是否启用会议 / authors 抓取 |
| `config/authors.yaml` | 关注的作者列表（默认未启用） |
| `.env` | `SJTU_API_KEY` + 可选 model 覆盖；已 .gitignore |

## 定时（Windows 任务计划程序）

1. 任务计划程序 → 创建任务
2. 触发器：每天 07:30
3. 操作：`powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\research-news\run_daily.ps1"`，起始于 `C:\path\to\research-news`
4. 勾选"如果错过计划开始时间，尽快启动任务"

期刊按季度跑，手动触发即可（每季度一次的事不值得设计排程）。

## 部署到 GitHub Pages

仓库 Settings → Pages → Source 选 `GitHub Actions`，已有 `.github/workflows/deploy-pages.yml` 自动构建 + 部署。

## 目录

```
research_news/
  daily.py            # arxiv 每日管道入口
  journals.py         # 期刊管道入口
  shootout.py         # prompt / 模型对照评估
  highlights.py       # 高相关论文 PDF 下载 + manifest
  models.py           # Paper / Event dataclass
  dedup.py            # 跨日 dedup
  scrapers/
    arxiv.py          # arxiv RSS + API
    jmlr.py           # JMLR 卷索引页
    crossref.py       # 通用 ISSN → 期刊（含 T1-T4 abstract backfill）
    authors.py        # Semantic Scholar by author
    conferences.py    # 会议 / seminar 页面（默认禁用）
  llm/
    prompts.py        # SCORE / RICH_SUMMARY / TOPICS 共享
    pipeline.py       # score_papers / summarize_paper
    sjtu_client.py    # SJTU OpenAI-compatible client
  render/markdown.py  # MkDocs 页面渲染
config/               # interests / sources / authors
docs/                 # MkDocs 源（daily/ + journals/ 自动生成）
data/                 # 运行时持久化（highlights/ + manifest + token_usage）
logs/                 # 每日 log
```

## 安全

- API key 走 `.env`，已 `.gitignore`
- 仓库公开但无凭证

## TODO

- [ ] arxiv 高相关论文也做 intro/section/conclusion 深读后再摘要
- [ ] 期刊 PDF 兜底（Oxford / T&F 学校 IP 时下载？）
- [ ] 加更多期刊：Bernoulli、EJS、Statistica Sinica、Statistical Science
- [ ] 会议抓取改用结构化源（RSS / iCal / 会议官方 API）
- [ ] 邮件推送（可选）
