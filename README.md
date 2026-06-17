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

### 恢复精读失败的页面（stub）

深度阅读偶尔会失败（LLM 超时 / 报错），这时精读页只剩一行 `*（精读失败，请查看
日志）*` 占位（其余 header 还在）。这些 stub 页可以一键全部重生成——从
`data/llm_scores.jsonl` 还原论文（摘要 / 作者），按 `data/deep_reads_index.json` 的
元数据补回 header，重跑深度阅读、就地覆盖：

```bash
# 把所有日期里失败的精读页全部重生成
python -m research_news.backfill_deep_reads --retry-stubs

# 只补某天 / 某段区间（跑完当天 daily 后只补当天）
python -m research_news.backfill_deep_reads --retry-stubs --date 2026-06-17
python -m research_news.backfill_deep_reads --retry-stubs --since 2026-06-08 --until 2026-06-17

# 先空跑看会补哪些（不调 LLM、不下 PDF、不写盘）
python -m research_news.backfill_deep_reads --retry-stubs --dry-run
```

- **找谁**：扫 `docs/deep_reads/*.md` 里带失败占位符的页；优先按文件名对上索引拿到真实
  paper_id（arXiv 与 DOI 都行），索引里没有的退回从文件名解析（arXiv id 即文件名 slug）。
- **幂等**：只重生成仍是 stub 的页，成功的精读不动；可放进每日 cron 反复跑。
- 取代了早期一次性脚本 `rerun_stubs.py` / `rerun_deep_reads.py`（硬编码日期、且后者已失效）。

### 自动化：每天跑完顺手恢复（cron + 锁）

`run_daily.sh` 已是「日跑 → 修乱码摘要 → **恢复当天失败的精读** → `git add -A` 提交推送」
一条龙，并在最前面加了互斥锁（`flock`）：

```bash
python -m research_news.daily
python -m research_news.rerun --date "$(date -I)"
python -m research_news.backfill_deep_reads --retry-stubs --date "$(date -I)"   # ← 恢复 stub
git add -A && git commit -m "daily report $(date -I)" && git push
```

部署建议（尤其是 OpenClaw / agent 这类托管环境）：

- **只留一个执行者**。最稳是系统 crontab 直接跑脚本；agent 那边的 cron 改成「跑完后检查
  结果并汇报」，不要也去 `exec` 跑一遍。锁能兜住「同一分钟两个触发」并行的情况（第二个检测到
  锁直接退出），但单一触发更干净。
- 锁用 `flock`（锁文件 `${TMPDIR:-/tmp}/research-news-daily.lock`）：内核在进程退出时
  自动释放，`kill -9` / 断电都不会留下死锁，无需手动清理。
- `git add -A` 会把报告（`docs/`）、数据（`data/`）和当天日志（`logs/`）一起提交——
  敏感 / 大文件（`.env`、`data/highlights/` 等）已在 `.gitignore` 里，不会误传。

**服务器入口 `run_rn.sh`**：cron 直接指它即可。它负责机器相关的环节——cd 进仓库、激活
venv、`git pull --rebase --autostash`（先同步网页 / agent 合进来的改动，省得收尾 `git push`
被拒），再 `exec ./run_daily.sh`（真正的管道 + 锁都在那）。逻辑集中在 `run_daily.sh`（进版本
控制），`run_rn.sh` 这层基本不用动。

```cron
# 工作日 09:10，只留这一个执行者
10 9 * * 1-5 /root/research-news/run_rn.sh >> /root/rn.log 2>&1
```

放仓库外（如 `/root/run_rn.sh`）就设 `RN_REPO=/root/research-news`；放仓库里则自动定位。

### 显示全部论文（含低相关）+ 补全历史

每日报告现在**展示当天打过分的所有论文**，不再只留阈值以上的。够格的（score ≥
`score_threshold_show`）照旧按主题分组、生成中文摘要——**不设单日篇数上限，过阈值的全部
展开**。其余的（低于阈值）汇到页尾 **🗂 其他论文** 一节，按评分由高到低排列，**只列
LLM 评分 + 一句简评（score_reason），不再生成摘要**——这些数据每篇打分时就存进了
`data/llm_scores.jsonl`，所以是零额外 LLM 调用。

> 历史说明：早期版本对单日摘要设过 25 篇上限，所以**部分历史页**里有当时超限、没展开的
> 高分论文落在 🗂 里（评分仍标着，且高分的多半已有精读）。上限现已取消，新报告不再有这种
> 情况；历史页可用下面的 `backfill_summaries` 一次性补齐。

**补回低相关列表（纯离线、无需 API）**——过去的报告当时只渲染了阈值以上的，下面的命令把
被遗漏的论文从打分日志**就地补回**对应日期页的 🗂 一节：

```bash
# 给所有历史每日页补全 🗂 其他论文 一节
python -m research_news.backfill_low_relevance

# 只补某天 / 某段区间，或先空跑看会补哪些
python -m research_news.backfill_low_relevance --date 2026-06-12
python -m research_news.backfill_low_relevance --since 2026-06-01 --until 2026-06-13
python -m research_news.backfill_low_relevance --dry-run
```

幂等：已有的 🗂 一节会被整体替换而非追加，重复运行安全。已渲染（摘要区的）论文不会重复
进 🗂；期刊管道写进同一日志的非 arXiv 行按 source 过滤掉。

**把历史 🗂 里的高分论文补成摘要并提上去（需 API key）**——上限取消前堆在 🗂 里的过阈值
论文，可以读打分日志里的摘要、补生成中文摘要，再把整页重渲染、让它们归位到 📌/⭐ 主题分组：

```bash
# 给所有历史页补：🗂 里 score ≥ score_threshold_show 的论文生成摘要并提上去
python -m research_news.backfill_summaries

# 只补某天 / 某段区间
python -m research_news.backfill_summaries --date 2026-06-12

# 先看每天会提哪几篇（不调 LLM、不写盘）
python -m research_news.backfill_summaries --dry-run

# 安全自检：不提升、只把每页重渲染一遍，报告哪页不能逐字还原（无需 API key）
python -m research_news.backfill_summaries --self-check
```

已有的摘要原样保留（只对 🗂 里没摘要的补），故只对那几篇花 token。`--self-check` 会逐字
比对重渲染前后，确认解析器不会动到既有内容——先跑它确认全绿再正式补。

输出：
- `docs/daily/<日期>.md` — 当日速览报告，按主题分组（因果推断 / 高维 RMT / 非参 / 效率理论 / ...）；页尾 **🗂 其他论文** 列出当天其余打分论文（评分 + 简评）
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

### 回补历史卷期（节奏化、agent 驱动）

把期刊的历史卷期一点点补齐——每天 daily 跑完后补一个单元（一本刊的若干期），顺序进行、
绝不并行，攒一两周补完积压。去重（`data/seen_papers.json`）让它天然可续跑：跑更大的
`--n-issues` 只处理新冒出来的更老的期，重跑已覆盖的单元不产生任何提交。

```bash
# 一个单元（脚本自动 pull → 抢锁（与 daily 同一把）→ 跑 → 提交推送）
./run_journal_backfill.sh --only AoS --n-issues 12
./run_journal_backfill.sh --only JMLR --jmlr-n 3
./run_journal_backfill.sh --only-group prob_stats --n-issues 8

# 先估量（不调 LLM、不写盘、不抢锁）——大刊务必先看篇数再决定 N
python -m research_news.journals --only TIT --n-issues 2 --dry-run
```

完整的待办清单 + agent 操作流程在 **[`ops/journal-backfill.md`](ops/journal-backfill.md)**：
按价值排序的队列（先补完全没有的 prob_stats / astro / epi，再加深 core / econ / applied /
ieee），状态用清单里的勾选记在 git 里。OpenClaw / 定时 agent 读它、每天补一项、打勾提交即可。
**唯一硬约束是不并行**——`run_journal_backfill.sh` 和 `run_daily.sh` 共用同一把 `flock` 锁。



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

**页头「目录核对」徽标**：每期页头（`共 N 篇` 那行下面）会自动加一行核对状态——拿本期抓到的
文章对照权威目录（默认 OpenAlex，快且通用），直接告诉你是否齐全：

```text
# AoS — Vol 54  Issue 2  ·  2026-05-26

- 共 22 篇 · Annals of Statistics
- 目录核对 ✅ 22 篇全部抓到（对照 OpenAlex 22 篇）
```

漏了就显示 `⚠️ 疑似漏 N 篇（…）：<DOI>…`，源暂时连不上显示 `⏭️ 未核对`，最新一期 OpenAlex
还没完全收录时显示 `✅ 未见遗漏（…可能尚未完全收录）`（不误报）。正常跑和 `--rerun` 都默认开，
`--no-completeness-check` 可关。想要出版方权威的详单仍用上面的 `completeness --euclid`。

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

## 讲座精读管道

把会议 / seminar 录像（YouTube 上很多，如 **OCIS** Online Causal Inference Seminar 的历史
录像、**INI** workshop 录像）读成 deep-read 风格的结构化中文笔记——论文精读的「口头报告」版。
讲座是**手挑**的（写进 `config/talks.yaml`），所以没有评分 / 门槛，选了就读。

两步走，**转写本地跑、精读哪都能跑**（转写要访问 YouTube + ffmpeg + 最好有 GPU，所以不进 CI）：

```bash
pip install -e ".[asr]"     # yt-dlp + faster-whisper（另需 ffmpeg 在 PATH）

# 看有哪些讲座、各自转写 / 精读到哪一步了
python -m research_news.talks list

# ① 转写：下音频 → faster-whisper → data/talks/<id>.txt（带 asr_prompt 偏置领域词/人名）
python -m research_news.talks ingest --id robins-cambridge-keynote-2026
python -m research_news.talks ingest --all                 # 所有还没转写的
python -m research_news.talks ingest --id <id> --prefer-subs   # 视频已有字幕就直接用，跳过 ASR

# ② 精读：转写 → 讲座专用 prompt → docs/talks/<date>-<id>.md（+ 存档 + 首页入口）
python -m research_news.talks read --id robins-cambridge-keynote-2026
python -m research_news.talks read --all                   # 所有有转写、还没出页面的
python -m research_news.talks read --id <id> --read-papers  # 顺带精读它点名的 arXiv 论文
```

- **转写模型不麻烦**：`pip install -e ".[asr]"` 装好 `faster-whisper`，模型**首次运行自动下载**，
  不用手动找文件。默认 `large-v3`（约 5GB 显存）。
- **小显存 GPU（如 GTX 1650 / 4GB）**：`large-v3` 放不下，用 `distil-large-v3`（英文质量接近、更快）
  或 `small`，配 int8：
  ```bash
  # 一次设好，之后所有 ingest 都用它
  set WHISPER_MODEL=distil-large-v3        # Windows；或 export ...（Linux/macOS）
  set WHISPER_COMPUTE_TYPE=int8
  # GPU 跑 faster-whisper 需要 CUDA/cuDNN 库；最省事是装进 venv：
  pip install nvidia-cublas-cu12 nvidia-cudnn-cu12
  python -m research_news.talks ingest --id <id>   # --model-size 也可临时覆盖
  ```
  实在配不动 CUDA 就 `set WHISPER_DEVICE=cpu`（int8）纯 CPU 跑，慢但能用。
- **不想跑 ASR？两条更省事的路**：① `--prefer-subs` 直接下 YouTube 已有的（自动）字幕，**完全
  不用 GPU**——OCIS 多数讲座年头够久、早有自动字幕，批量转写这条最快；② `--subs-file foo.srt`
  喂入你用**任何工具**（whisper.cpp 等你本地那个轻量的）生成的 `.srt`/`.vtt`，我只做清洗入库。
- **全量转写（194 场）**：`ingest --all` 一条命令搞定，**可断点续传**（已转写的自动跳过、单场
  失败不影响其它），适合挂后台跑几天。1650 上 `distil-large-v3` 大致 3–8× 实时，194h 音频 ≈
  一两天 GPU 时间。
  ```bash
  python -m research_news.talks ingest --all                 # ASR 全转（断了重跑即续）
  python -m research_news.talks ingest --all --prefer-subs   # 或先用 YouTube 字幕快速铺一遍
  ```
  > ⚠️ **转写 vs 精读的成本不对称**：转写只花本地 GPU 时间（不花钱）；但 `read --all` 是 194 次
  > LLM 长调用（deepseek-reasoner，每篇上万 token 输出），**很费 token**。建议转写可以全转，
  > **精读挑着来**（先把 Robins / Rotnitzky / Tchetgen / 半参数效率那条线读了）。
- **质量坑**（和论文精读一致的原则）：自动转写对人名 / 术语 / 公式 / 具体的率与界**容易听错**，
  讲座 prompt 已被要求把这些当线索、并对拿不准的地方标注「待核对」；每页页头也有这条提醒。
  `asr_prompt`（config 里按讲座写，叠加全局 `asr_prompt_default`）喂领域词能明显改善识别。
- **对应论文**：每个讲座可在 config 里写 `papers: [arXiv id / DOI]`。出页面时这些论文会**交叉
  链接**到它们的精读页（已精读的直接挂链接）；`read --read-papers` 会把还没精读的 arXiv 论文
  **自动拉进现有论文精读队列**再链接回来。
- **多讲者视频**：一个 1.5h 录像常是好几个 talk 连着。在 config 里给 `segments`（每段
  `start` 时间点 + 可选 `speaker` / `title`，从节目单 / YouTube chapters 抄）就能按时间戳切成
  **每讲者一篇**笔记；不填则整段读成一篇。

输出：
- `docs/talks/<date>-<id>.md` — 每场（或每讲者）一页，结构同精读：工作线背景 → 最小内核 →
  报告主体（带 `[时间点]` 方便回看）→ 对应论文与开放问题。
- `docs/all_talks.md` — 讲座存档（站点导航「讲座精读」），按来源（OCIS / INI / …）分组。
- `data/talks_index.json` — 讲座元数据索引（首页「今日讲座」与存档页用）。
- `data/talks/<id>.txt` — 清洗后的转写稿（带时间戳，纳入 git，CI 可据此重生成笔记）；
  音频落 `data/talks/audio/`，已 `.gitignore`、不上传。

### 批量导入 OCIS 历史讲座目录

**OCIS**（[Online Causal Inference Seminar](https://sites.google.com/view/ocis/past-talks)）
的历史讲座按季分页，每期基本都带 **video + arXiv + slides**——是个高质量、对口的因果推断
讲座库。`import-ocis` 把这些页面解析成讲座目录，**自动写进 `config/talks.ocis.yaml`**
（与手工的 `talks.yaml` 并列、管道一起读；同 id 以手工文件为准），arXiv 链接落到每场的
`papers:` 上、出页面时自动交叉链接到论文精读。**仓库里已内置导入好的全量目录**（~194 场、
2020 至今，含 arXiv 交叉链接），可直接 `talks list` 挑着转写。

```bash
# 单季 / 多季 / 全部（Google Sites 屏蔽服务器抓取，需本地网络能开它的页面）
python -m research_news.talks import-ocis --season spring-2024
python -m research_news.talks import-ocis --season spring-2024 --season fall-2023
python -m research_news.talks import-ocis --all-seasons          # 2020 至今，404 的季自动跳过

# 离线：浏览器里把某季页面另存为 HTML，直接解析（默认确定性解析，连网和 API key 都不用）
python -m research_news.talks import-ocis --html spring-2024.html

# 先干跑：只抓页面、数出每页有多少 video/arxiv/slides 链接，不写盘
python -m research_news.talks import-ocis --season spring-2024 --dry-run

# 导完照常挑着转写 + 精读
python -m research_news.talks list
python -m research_news.talks ingest --id ocis-2026-06-02-suhas-vijaykumar
python -m research_news.talks read   --id ocis-2026-06-02-suhas-vijaykumar
```

解析 **DOM 无关、默认确定性、纯离线**：直接在页面字节里正则抓 youtube / arxiv / slides 链接
（并自动解开 Google 的 `url?q=` 跳转包装），再按页面固定的「`Tuesday, 日期:` / `Speaker:` /
`Title:` / `[Paper][Slides][Video]`」结构把每场对上——不需要 LLM、不需要 API key。跨 2020–2026
几种历史排版都覆盖。产出 `data/ocis_catalog.json`（完整目录，含 slides）+
`config/talks.ocis.yaml`（有 video 的可转写条目）。个别老页排版怪异时，`--llm` 可改用模型做
关联兜底。链接抓取是确定性的，建议核对一下少量老条目的讲者 / 题目。

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
| `config/talks.yaml` | 讲座精读：要转写 + 精读的会议 / seminar 录像（URL + 讲者 + 对应论文 + ASR 偏置词） |
| `config/talks.ocis.yaml` | `import-ocis` 自动生成的 OCIS 讲座条目，和 `talks.yaml` 一起被读（同 id 手工优先）；勿手改 |
| `.env` | `SJTU_API_KEY` + 可选 model 覆盖；已 .gitignore |

## 定时（Windows 11 · 任务计划程序，纯 cron 式，无需 agent）

daily 全流程交给 Windows 任务计划程序跑 `run_daily.ps1` 即可，**不需要 OpenClaw / agent**
（agent 只是个会自己烧 token 的外壳）。`run_daily.ps1` 已对齐 Linux 版：命名 **Mutex 单实例锁**
→ `git pull --rebase` 同步 → daily → 修乱码摘要 → **恢复当天失败的精读** → `git add -A` 提交并
带重试地 push。

**一条命令注册任务**（仓库根目录、PowerShell 里跑一次；提示权限不足就用管理员 PowerShell）：

```powershell
.\scripts\register-task.ps1                 # 工作日 09:10 的 daily + 登录时的 catch-up
.\scripts\register-task.ps1 -Time "08:30"   # 换时间
.\scripts\register-task.ps1 -NoCatchUp      # 只注册 daily，不要 catch-up
Start-ScheduledTask -TaskName research-news-daily   # 立刻测一次
```

它注册**两个**任务，都勾好关键项（**错过自动补跑** `-StartWhenAvailable`、**绝不并行**
`-MultipleInstances IgnoreNew`、电池不挡）：

- `research-news-daily`：工作日 09:10 跑 `run_daily.ps1`。
- `research-news-catchup`：**登录时**（+10 分钟）跑 `scripts\catch-up.ps1`——台式机不会 24 小时开，
  开机后它会看最后一份日报是哪天，把**关机错过的工作日**用 `python -m research_news.daily --date <X>`
  一次性补齐（跳过周末，今天留给 09:10 那个任务）。它和 daily **共用同一把锁**，所以会排队、不并行；
  靠重跑保护，已存在的报告不会被覆盖。默认最多往前补 14 天（`-MaxDays` 调），手动跑：
  `.\scripts\catch-up.ps1`。

> 手动建任务的话：创建任务 → 触发器 周一至周五 09:10 → 操作
> `powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\research-news\run_daily.ps1"`
> 起始于仓库目录 → 设置里勾「错过尽快运行」、「已在运行则不启动新实例」。

落地前提：

- 机器在 09:10 前后**开着、联网**；睡眠中错过没关系（开机后 daily 补跑当天、catch-up 补齐之前
  错过的工作日）。
- 仓库目录里有 `.env`（`SJTU_API_KEY`）和 `.venv`。
- **先手动 `git push` 一次**，让 Git Credential Manager（或 SSH key）缓存凭证——计划任务是
  无人值守跑的，push 不能弹窗。
- **只留一个执行者**：要从云服务器搬到台式机，就把云上的 cron 关掉，别两台都跑（会各自
  commit/push 打架；锁只防同机并行）。

期刊回补按 `ops/journal-backfill.md` 手动 / 半自动跑即可，不用进每日任务。

**日志会自动传 GitHub（按机器分开）**：每次跑会写两份到 `logs\`——`logs\<日期>-<机器名>.log`
（管道详细日志：抓取 / 打分 / 摘要 / 精读 / 报错）和 `logs\run-<日期>-<机器名>.log`（整次运行的
完整 transcript：含 git、锁、PowerShell 层输出）。文件名带**机器名**（`host_tag()` / `COMPUTERNAME`），
所以云服务器和台式机即使同一天跑也各写各的、**不会互相覆盖或混在一起**，回看时不会误判是哪台
跑的。`run_daily.ps1` 收尾 `git add -A` 会把 `logs\` 一并提交推送，无人值守也有据可查（比如某步
429 限流）。

## 部署到 GitHub Pages

仓库 Settings → Pages → Source 选 `GitHub Actions`，已有 `.github/workflows/deploy-pages.yml` 自动构建 + 部署。

## 目录

```
research_news/
  daily.py            # arxiv 每日管道入口
  journals.py         # 期刊管道入口（含 --rerun 整期重跑）
  talks.py            # 讲座精读管道：ingest（转写）+ read（LLM 精读）+ 独立页面 / 存档
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
    conferences.py    # 会议 / seminar 页面（事件预告，默认禁用）
    transcribe.py     # 讲座转写工具：yt-dlp 下音频 + faster-whisper ASR + VTT/转写清洗（[asr] extra）
    ocis.py           # OCIS 历史讲座目录导入：抓 video/arxiv/slides 链接 + LLM 关联 → talks.ocis.yaml
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
  talks/              # 讲座精读页，每场（或每讲者）一页（自动生成）
  shootout/           # 模型对比页（手动/脚本生成）
  index.md            # 首页（自动生成）
  all_daily.md        # 每日存档（自动生成）
  all_journals.md     # 期刊存档（自动生成）
  all_deep_reads.md   # 精读存档（自动生成）
  all_talks.md        # 讲座精读存档（自动生成）
  all_shootout.md     # 测评存档（自动生成）
data/
  highlights/         # 高相关论文 PDF（本地，.gitignore）
  highlights.json     # 高相关论文 manifest
  deep_reads_index.json  # 精读元数据索引
  talks/              # 讲座转写稿 <id>.txt（纳入 git）；audio/ 子目录为音频（.gitignore）
  talks_index.json    # 讲座元数据索引
  ocis_catalog.json   # OCIS 导入的完整讲座目录（含 slides；import-ocis 生成）
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
