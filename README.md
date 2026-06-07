# research-news

个人定制的研究资讯系统。两条独立管道：

- **每日 arXiv**: 抓 stat.ME / stat.TH / math.ST / econ.EM / astro-ph.IM 新提交，按个人兴趣评分，对高相关论文按主题分组生成中文摘要 + 下载 PDF + LLM 全文精读
- **季度期刊**: 拉 JMLR / AoS / JASA / JRSSB / Biometrika 等最新一期（或近 N 期），同样的评分 + 摘要 + 主题分组 + 精读

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
| `pypdf` | 高相关论文 PDF 文本抽取（精读管道） |
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

### 重跑乱码 / 没跑完的摘要

LLM 偶尔会输出未转义的引号或在 `max_tokens` 处截断，导致某篇论文的「摘要」里
渲染出一段生 JSON（页面上能看到 ```` ```json ````）。**每日和期刊页都可能出现**，
这类「没跑完」的块可以事后重跑修复，无需重跑整个管道：

```powershell
# 扫描所有 docs/daily/*.md + docs/journals/*.md，修复乱码块
python -m research_news.rerun

# 只扫期刊页（或 --scope daily 只扫每日）
python -m research_news.rerun --scope journals

# 只处理某个日期（每日文件 + 该日期的期刊页都算）
python -m research_news.rerun --date 2026-05-26

# 离线模式：不调 LLM，只从页面里已有的残缺 JSON 抢救出干净正文
python -m research_news.rerun --offline

# 只看会改哪些、不落盘（不会调用 LLM）
python -m research_news.rerun --dry-run
```

修复优先用 LLM 重新生成（论文元数据从 `data/llm_scores.jsonl` 还原，并沿用当初给
该篇打分的模型）；当正文本身没被截断时，也能直接从页面残留的 JSON 里抢救出完整中文
摘要（无需 API）。正文被拦腰截断、又没有可用 LLM 的块会被原样保留并在日志里标出，
等有 `SJTU_API_KEY` 时再重跑。`run_daily.*` 已在每次日跑后自动执行一次每日页的重跑。

> 期刊管道另有 `--retry-broken`（配合 `--load-papers`）可在抓取快照仍在时只重跑坏掉
> 的摘要；`rerun` 则不依赖快照，直接在已发布的页面上修复，二者互补。

### 补做历史精读（阈值放宽后）

精读阈值放宽后（`score_threshold_deepread`，现为 6），过去的每日里有些当时没精读、
但按现在的标准够格的论文。每篇打过分的论文都记在 `data/llm_scores.jsonl`（含摘要），
所以可以直接拿这份记录补做精读，无需重抓重打分：

```bash
# 补做某天够格但当时没精读的论文（阈值默认读 config/interests.yaml）
python -m research_news.backfill_deep_reads --date 2026-05-29

# 先空跑看会补哪些、补几篇（不调 LLM、不下 PDF）
python -m research_news.backfill_deep_reads --date 2026-05-29 --dry-run

# 自定义阈值 / 先试补分数最高的 5 篇
python -m research_news.backfill_deep_reads --date 2026-05-29 --threshold 7 --limit 5

# 补一段日期区间
python -m research_news.backfill_deep_reads --since 2026-05-27 --until 2026-06-02

# 整天重跑：不跳过已精读的，把当天够格的全部重新精读一遍（含之前已精读的）
python -m research_news.backfill_deep_reads --date 2026-05-29 --force
```

补做的精读页会落到论文**原本的报告日期**下（和当天精读位置一致）。

- **默认（增量）**：只补当天够格、但当时没精读的论文，已精读的自动跳过 —— 重复运行
  安全、不浪费 token。
- **`--force`（整天重跑）**：当天 score≥阈值的论文（含已精读的）全部重新精读，连之前
  绿灯进来的（分数低于阈值）也一并重跑，不会缩小当天集合。适合精读配方变了、想把整天
  刷新一遍。附带好处：几天前的论文这时多半已被 Semantic Scholar 收录，被引文献块更可能
  抓成功。

两种模式补完都会自动刷新首页与存档页。

输出：
- `docs/daily/<日期>.md` — 当日速览报告，按主题分组（因果推断 / 高维 RMT / 非参 / 效率理论 / ...）
- `docs/deep_reads/<日期>-<paper_id>.md` — 每篇高相关论文（score ≥ `score_threshold_deepread`，现为 6）的独立精读页
- `docs/index.md` / `docs/all_daily.md` / `docs/all_deep_reads.md` — 自动更新的首页和存档页
- `data/highlights/<topic>/<arxiv_id>.pdf` — 高相关论文 PDF（本地存储，不上传 GitHub）
- `data/highlights.json` — 高相关论文 manifest（含 score / topic / 摘要 / 关键技术等）
- `data/deep_reads_index.json` — 精读元数据索引（首页展示用；含每篇 `n_references` 被引篇数）
- `data/citations.json` — 精读论文的引用边（被引文献的 arXiv/DOI/S2 id + 是否高影响 / 引用意图 / 被引数）。即使当时没抓到摘要也存，攒成引用网络供日后挖掘问题
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

# 改 prompt / 换模型再来一遍
$env:JOURNALS_MODEL="deepseek-chat"
python -m research_news.journals --load-papers data/corpus-2026Q2-4i.json
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

### arXiv 预印本链接

期刊文章的官方链接（DOI 落地页）常要看权限才能打开，arXiv 预印本免费、一点就开。所以抓取后会对每篇期刊文章（含 JMLR）按标题在 arXiv 上找一遍预印本：找到高置信匹配就把 arXiv 链接记到 `Paper.arxiv_url`，**期刊页和深度阅读页都同时挂「官方链接 + arXiv」两个链接**（没找到的只挂官方链接）。链接随 `--save-papers` 落盘，`--load-papers` 直接复用、不重查。

### 重跑整期（换了 prompt / 模型后覆盖重生成）

改了「深度阅读 + 打分」prompt 或换了模型后，想把**已发布的某些期**按新配方重新生成、
**就地覆盖**对应 markdown，用 `--rerun`（挂在 `journals` 上；和 `python -m
research_news.rerun` 不是一回事——后者只修页面里的乱码摘要块）：

```powershell
# core 组每刊最近 4 期，全部重跑
python -m research_news.journals --rerun --only-group core --rerun-recent 4

# 指定单期（最好配 --only 锁单刊）
python -m research_news.journals --rerun --only AoS --issue v54-i1

# 先干跑：列出会重生成哪些页、每期会拉到多少篇（对比页上现有，提示 +N 篇新增 / -N 篇消失），不调 LLM、不写盘
python -m research_news.journals --rerun --only-group core --rerun-recent 4 --dry-run

# 不重抓、直接复用快照里的这期论文（快、省钱，纯迭代 prompt；但不会带上原来漏抓的）
python -m research_news.journals --rerun --only AoS --issue v54-i1 \
    --from-snapshot data/corpus-2026Q2-4i.json
```

- 目标期次从 `docs/journals/*.md` 文件名解析（`--only` 刊 / `--only-group` 组 /
  `--rerun-recent N` 每刊最近 N 期 / `--issue vNN-iMM` 单期，可叠加）。
- **就地覆盖**：把 `run_date` 钉成原页面文件名里的日期，重渲染就盖回**同一个文件**
  （期刊页 + 该期对应的精读页都覆盖），不会另起新日期页。prompt 现取，自动用最新版。
- **默认重抓 Crossref**（能顺带带上原来漏抓的文章、元数据最新）；`--from-snapshot PATH`
  改为从 corpus JSON 取，快但不自愈。
- **默认先备份**：旧的期刊页 + 精读页拷到 `backups/<时间戳>/`（已 `.gitignore`），
  `--no-backup` 关掉。
- 仅适用于**带期号的页**（`-vN-iM` / `-vN`）。JMLR（滚动出版、单卷一页）与个别无期号的
  单页（如旧的 `2026-05-26-jasa.md`）暂不在 issue-rerun 范围内——JMLR 直接用普通
  `--only JMLR` 重抓即可。

### 抓取完整性检查 + 报缺

期刊抓取偶尔会漏文章（Crossref 的 issue 列表按发表日排序 + `rows` 窗口截断，或个别文章
缺 vol/issue 元数据没归进该期）。**权威目录脚本自己抓**，你只给期号就行：

```powershell
# 自动取权威目录（Euclid → OpenAlex），对比已发布的 AoS v54-i1 页，报缺
python -m research_news.completeness --journal AoS --issue v54-i1

# 查到缺失后：按 DOI 从 Crossref 单篇补抓，并重跑该期把补回来的文章一起重渲染
python -m research_news.completeness --journal AoS --issue v54-i1 --refetch --rerun

# 强制指定权威源（默认 auto），或离线用本地 content PDF 兜底
python -m research_news.completeness --journal AoS --issue v54-i1 --euclid
python -m research_news.completeness --journal AoS --issue v54-i1 --openalex
python -m research_news.completeness --journal AoS --issue v54-i1 --toc-pdf contents.pdf
```

- **权威集**（真相，自动获取）：① Project Euclid issue TOC（出版方权威，覆盖
  AoS/AoP/AoAS/EJS/Bernoulli/Stat Sci）；② OpenAlex 按 ISSN+卷+期列全期文章（**通用**，
  任何刊都行，且和 Crossref 是不同库——正好交叉验证当初漏抓的那次）。默认 `auto`
  先 Euclid 后 OpenAlex；`--euclid`/`--openalex` 强制其一，`--toc-pdf` 离线兜底。
- **已抓集**（现状）：默认解析已发布的期刊页（`--page` 指定，或 `--snapshot` 用 corpus）。
- **diff** 先按 DOI、无 DOI 再按标准化标题（复用抓取器里的标题匹配）；discussion /
  comment / correction 类会**先从权威集滤掉**，不会误报成漏抓。
- 输出「缺失文章」报告（标题 + DOI + 链接）。`--refetch` 按 DOI 单篇补抓
  （`/works/{DOI}` 直查，即使 issue 列表漏了也能拿到）；再加 `--rerun` 就把补回来的文章
  喂给上面的整期重跑，重新打分 / 摘要 / 精读 / 渲染进去。`--dry-run` 只报会补哪些、不动。

### 输出

- `docs/journals/<日期>-<期刊>.md` — 每个期刊独立一页（如 `2026-05-17-jmlr.md`、`2026-05-17-aos.md`），按主题分组
- `docs/deep_reads/<日期>-<paper_id>.md` — 高相关论文（score ≥ 8）每篇独立精读页
- `docs/all_journals.md` / `docs/all_deep_reads.md` — 自动更新的期刊和精读存档页
- 高相关论文 PDF 落 `data/highlights/<topic>/`（arxiv / JMLR 可下；付费期刊只记 manifest）

## 跨篇综合 / 选题引擎

把同一子方向近期的**期刊**精读放在一起，归纳只在跨篇层面才看得见的信号：反复出现的开放
问题（被 ≥2 篇独立论文点名）、论文之间的张力、以及能接上武器库的迁移空位。**LLM 只做
挖掘与归纳，不打分不排名**，每条都点名来源论文，供你自己判断选题。

```powershell
# 先看各 topic 的论文数（不调 LLM）
python -m research_news.synthesize --dry-run

# 对所有 ≥3 篇的子方向各生成一份综合（默认聚合全部期刊）
python -m research_news.synthesize

# 只做某个子方向 / 只看某日期之后的期刊精读
python -m research_news.synthesize --topic causal_inference --since 2026-01-01
```

**按期刊 / 期刊组聚合**（范围都在 `config/journals.yaml`，用 `--list-journals` 列出）：

```powershell
python -m research_news.synthesize --list-journals          # 看有哪些期刊组和期刊

python -m research_news.synthesize --journal AoS            # 单个期刊（short 名）
python -m research_news.synthesize --journal AoS,JASA       # 多个期刊（逗号分隔）
python -m research_news.synthesize --group core            # 一个期刊组（core/prob_stats/applied/econ/...）
python -m research_news.synthesize --group core,applied    # 多个期刊组
python -m research_news.synthesize --group core --journal Bernoulli   # 组 + 散刊混搭
python -m research_news.synthesize --group core --topic causal_inference  # 再叠 topic 过滤
```

`--journal` 接 short 名（如 `AoS` `JASA` `JRSSB` `Biometrika` `JMLR`）或全名，`--group` 接组
键名（`core` `prob_stats` `applied` `econ` `astro` `epi` `ieee`）；两者都支持逗号分隔或重复传，
也可同时用。不带范围参数 = 全部期刊。

全部参数：`--topic` `--journal` `--group` `--since` `--min-papers`（默认 3）`--model`
`--list-journals` `--dry-run`。

两段式：先把每篇精读抽成结构化的「问题种子」（limitation / future work / 张力 / 迁移线索）
存进 `data/open_problems.jsonl`（缺的才抽，可累积），再按 topic 综合。输出
`docs/synthesis/<日期>-<范围>-<topic>.md`，并刷新存档页 `docs/all_synthesis.md`（站点导航
「选题综合」）。不同范围（如 `all` / `core` / `AoS-JASA`）各自独立成页、不互相覆盖。

## 账户与收藏（网页端）

站点是纯静态的（GitHub Pages，无后端），但通过把状态存进你 GitHub 账号下的一个
**私密 Gist**，实现了"登录账户 + 跨设备已读/未读 + 半自动收藏"。全部逻辑在
`docs/javascripts/extras.js`，无需任何服务器或第三方服务。需登录才会出现徽标与收藏按钮。

**登录**：点页面右下角「👤 登录」，粘贴一个带 `gist` 权限的 GitHub Personal Access
Token（classic）。Token 只存在你本机浏览器的 localStorage，首次登录会自动在你账号下
创建一个私密 Gist（`research-news-state.json`）存放状态；其它设备用同一个 token 登录即
同步。点 [创建 Token](https://github.com/settings/tokens/new?scopes=gist&description=research-news)
（勾选 `gist`，其它都不用）。

**已读 / 未读**：登录后每篇论文标题旁出现 `○ 未读` / `✓ 已读` 徽标，点击切换，跨设备同步。

**收藏**：每篇论文旁还有 **☆ 收藏** 按钮（精读页在大标题旁），点一下即把论文加入
「收藏」页（`docs/favorites.md`），自动汇总——不用再手动维护周报。收藏页有两种视图：

- **总收藏**（默认）：按论文类别（沿用 `interests` 主题分类）分大类，类内按日期降序。
- **按周**：按 ISO 周号分组，周内再按类别 / 日期。

每篇收藏都能直接在网页上写 **评论 / 笔记**（点「✎ 评论」），随状态一起同步；
还能一键「复制为 Markdown」。类别分组所需的主题分类表由管道写入
`docs/data/topic_labels.json`。

### 公开收藏快照（让访客也能看）

私密 Gist 只有你登录后看得到。要让没登录的访客也能浏览你的收藏，有一个**每晚定时**的
GitHub Action（`.github/workflows/publish-favorites.yml`）：读私密 Gist →
按 `paper_id` 拼上 `data/highlights.json` 里的中文摘要 / 评分（**摘要不存进 Gist，
所以 Gist 始终很小**）→ 写出 `docs/data/favorites_public.json` → 有变化才提交，
触发 Pages 部署。收藏页对未登录访客就渲染这份**只读快照**（带摘要与你的评论）。

`research_news/publish_favorites.py` 是导出脚本，也可本地手动跑
（`GIST_TOKEN=... python -m research_news.publish_favorites`）。

**一次性配置**：仓库 Settings → Secrets and variables → Actions → 新建
secret `GIST_TOKEN`，填一个 classic PAT（勾 `gist` + `public_repo`；用 PAT 推送
快照才能触发部署 workflow）。可选 variable `RN_GIST_ID` 固定 gist id，
不填则按描述 / 文件名自动发现。

## Shootout（评估工具）

调 prompt / 换模型时用。把同一批 paper 跑多个 variant 出对照页：

```powershell
# 多 variant 对照（A baseline / B rich prompt / C-fast deep content / C-deep reasoner）
python -m research_news.shootout 2408.06103 2508.12627 --add-defaults

# 模型横向对比（固定 prompt，每模型一列）
python -m research_news.shootout --source jmlr --n 10 `
    --models deepseek-chat,glm-5.1
```

输出在 `docs/shootout/<日期>.md`，`docs/all_shootout.md` 存档页自动更新。

## 配置文件

| 文件 | 作用 |
|---|---|
| `config/interests.yaml` | 你的研究兴趣 + score 阈值 + 摘要风格。LLM 直接读 |
| `config/sources.yaml` | arxiv 抓哪些 category，是否启用会议 / authors 抓取 |
| `config/authors.yaml` | 关注的作者列表（默认未启用） |
| `config/journals.yaml` | 期刊列表 + ISSN |
| `.env` | `SJTU_API_KEY` + 可选 model 覆盖；已 .gitignore |

## 定时（Windows 任务计划程序）

1. 任务计划程序 → 创建任务
2. 触发器：每天 07:30
3. 操作：`powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\research-news\run_daily.ps1"`，起始于 `C:\path\to\research-news`
4. 勾选"如果错过计划开始时间，尽快启动任务"

期刊按季度跑，手动触发即可。

## 部署到 GitHub Pages

仓库 Settings → Pages → Source 选 `GitHub Actions`，已有 `.github/workflows/deploy-pages.yml` 自动构建 + 部署。

## 目录

```
research_news/
  daily.py            # arxiv 每日管道入口
  journals.py         # 期刊管道入口（含 --rerun 整期重跑）
  completeness.py     # 抓取完整性检查：权威 TOC ↔ 已抓 diff + 报缺 + 补抓
  deep_read.py        # PDF 精读：文本抽取 + LLM 精读 + 独立页面生成
  shootout.py         # prompt / 模型对照评估
  highlights.py       # 高相关论文 PDF 下载 + manifest
  models.py           # Paper / Event dataclass
  dedup.py            # 跨日 dedup
  scrapers/
    arxiv.py          # arxiv RSS + API
    jmlr.py           # JMLR 卷索引页
    crossref.py       # 通用 ISSN → 期刊（含 T1-T4 abstract backfill、按期/按 DOI 单抓）
    euclid.py         # Project Euclid issue TOC（完整性检查权威源：出版方）
    openalex.py       # OpenAlex 按期列文章（完整性检查权威源：通用、跨库交叉验证）
    authors.py        # Semantic Scholar by author
    conferences.py    # 会议 / seminar 页面（默认禁用）
  llm/
    prompts.py        # SCORE / RICH_SUMMARY / DEEP_READ / TOPICS 共享
    pipeline.py       # score_papers / summarize_paper
    sjtu_client.py    # SJTU OpenAI-compatible client
  render/markdown.py  # MkDocs 页面渲染（daily / journal / deep_read / index）
config/               # interests / sources / authors / journals
docs/
  daily/              # 每日速览（自动生成）
  journals/           # 期刊页，每期刊一页（自动生成）
  deep_reads/         # 精读页，每篇论文一页（自动生成）
  shootout/           # 模型对比页（手动/脚本生成）
  index.md            # 首页（自动生成）
  all_daily.md        # 每日存档（自动生成）
  all_journals.md     # 期刊存档（自动生成）
  all_deep_reads.md   # 精读存档（自动生成）
  all_shootout.md     # 测评存档（自动生成）
data/
  highlights/         # 高相关论文 PDF（本地，.gitignore）
  highlights.json     # 高相关论文 manifest
  deep_reads_index.json  # 精读元数据索引
  token_usage.json    # API token 用量记录
logs/                 # 每日日志（.gitignore）
```

## 安全

- API key 走 `.env`，已 `.gitignore`
- `data/highlights/`（PDF 文件）已 `.gitignore`，不上传 GitHub
- 仓库公开但无凭证

## TODO

- [ ] 期刊 PDF 兜底（Oxford / T&F 学校 IP 时下载？）
- [ ] 加更多期刊：Bernoulli、EJS、Statistica Sinica、Statistical Science
- [ ] 会议抓取改用结构化源（RSS / iCal / 会议官方 API）
- [ ] 邮件推送（可选）
