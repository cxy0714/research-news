# Changelog

本项目所有值得记录的改动会写在这里。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号按里程碑递增（暂未做正式发布），日期为 PR 合并日期（UTC）。
分类约定：

- **Added** — 新增功能
- **Changed** — 已有功能的行为变化
- **Fixed** — Bug 修复
- **Docs** — 仅文档调整

每条改动末尾的 `#N` 是对应的 PR 编号，可在
<https://github.com/cxy0714/research-news/pull/N> 查看。

---

## [Unreleased]

### Fixed
- **被引检索 / 机构查询失败显示真实状态码，404 不再重试**：`references.py`（Semantic
  Scholar）与 `affiliations.py`（OpenAlex）原先把异常被 `RetryError[HTTPStatusError]`
  吞掉，看不出是 404（论文尚未被收录）还是 429（限速）——而两者解法完全不同。新增
  `should_retry_http`：只对 **429 / 5xx / 网络超时**重试，**404 等 4xx 直接放过**（不再
  白重试），并 `reraise=True` 让真实异常冒泡、日志打印真实状态码与提示。
- **`backfill_deep_reads` 日志落盘**：原先用 `logging.basicConfig` 只输出到控制台，重跑
  时的真实 HTTP 状态码没被保存。改为同时写入 `logs/<当天>.log`（对齐 daily 的日志设置）。
- **arXiv 抓取 403 / 429 / RetryError**：`export.arxiv.org` 与 `rss.arxiv.org` 请求改为带
  描述性 User-Agent（arXiv 会拦截 httpx 默认 UA，表现为反复 403），失败时日志直接显示真实
  状态码而非被 `RetryError` 吞掉。并重写抓取重试：**请求间最小间隔 3 秒**（`ARXIV_MIN_INTERVAL`）、
  遇 **429/503 时honor `Retry-After`**（无则 10/20/30…s 退避，封顶 120s）、超时单独退避。
  这能避免突发请求触发 429、并从限流中自动恢复。可用 `ARXIV_USER_AGENT` / `ARXIV_MIN_INTERVAL`
  / `ARXIV_FETCH_ATTEMPTS` 调。

### Added
- **OCIS 目录批量导入 `talks import-ocis`**：把
  [Online Causal Inference Seminar](https://sites.google.com/view/ocis/past-talks)
  的历史讲座（按季分页，每期多带 video + arXiv + slides）解析成讲座目录，自动写进
  `config/talks.ocis.yaml`（与手工 `talks.yaml` 并列、管道一起读，同 id 手工优先），arXiv
  落到每场 `papers:` 上、出页面时交叉链接到论文精读。解析 **DOM 无关 + 默认确定性 + 纯离线**：
  正则抓页面里的 youtube / arxiv / slides 链接、自动解开 Google `url?q=` 跳转包装，再按页面
  固定的「`Tuesday, 日期:` / `Speaker:` / `Title:` / `[Paper][Slides][Video]`」结构把每场对上
  ——不需要 LLM / API key，跨 2020–2026 几种历史排版都覆盖；`--llm` 可改用模型做兜底。
  `--season` / `--all-seasons`（2020 至今，404 跳过）/ `--html`（离线解析另存页面）/ `--dry-run`
  / `--catalog-only`。产出 `data/ocis_catalog.json` 全目录。**已内置全量导入结果**（~194 场）。
  Google Sites 屏蔽服务器抓取，需本地网络，转写步骤亦同。
- **讲座精读管道 `talks`**：把会议 / seminar 录像（如 OCIS、INI workshop）读成
  deep-read 风格的结构化中文笔记，是论文精读的「口头报告」版。手挑视频、不打分不过滤。
  两步：① `talks ingest`（本地：yt-dlp 下音频 → faster-whisper 转写 →
  `data/talks/<id>.txt`，带 `asr_prompt` 注入领域词偏置识别）。转写来源三选一：默认 ASR、
  `--prefer-subs`（下 YouTube 已有字幕、免 GPU）、`--subs-file foo.srt`（喂入 whisper.cpp 等任意
  工具的字幕、纯离线）。小显存 GPU 用 `--model-size distil-large-v3`/`small` 或 `$WHISPER_MODEL`；
  `ingest --all` 可断点续传，适合全量批跑。② `talks read`（转写 → 讲座专用 prompt `TALK_READ_SYSTEM` →
  `docs/talks/<date>-<id>.md`）。讲座可声明它对应的 arXiv/DOI 论文，自动**交叉链接**到这些
  论文的精读页；`read --read-papers` 还会把尚未精读的 arXiv 论文**自动拉进现有论文精读
  队列**。多讲者视频可在 config 里给 `segments`（时间点边界）切成「每讲者一篇」。新栏目
  `docs/all_talks.md` + 首页「讲座精读」入口；转写需 `pip install -e ".[asr]"` + ffmpeg，
  仅本地跑（YouTube / GPU），不进 CI。配置见 `config/talks.yaml`。
- **补做历史精读 `backfill_deep_reads`**：精读门槛放宽到 6 后，过去的每日里有些当时没
  精读、但按现在标准够格的论文。`data/llm_scores.jsonl` 记了每篇打过分论文（含摘要），
  据此补做精读，无需重抓重打分：`--date` / `--since..--until` / `--threshold` / `--limit`
  / `--source` / `--dry-run`。精读页落到论文**原报告日期**下；默认增量（跳过已精读），
  **`--force` 整天重跑**（含已精读的、连绿灯低分的也重跑，不缩小当天集合）。
- **引用网络存储 `data/citations.json`**：精读时已从 Semantic Scholar 抓到 references；
  即便被引works没摘要（不进 prompt），也带 `externalIds`。把这些**引用边**存下来——每条
  边含 arXiv / DOI / S2 id + 标题 + 年份 + 是否高影响 + 引用意图 + 被引数（都是客观信号），
  按 paper_id upsert（重跑刷新）。攒多了可只凭引用关系构论文引用网络，辅助发掘问题。
- **记录每篇精读附带的被引篇数 `n_references`**：写进日志（`attached N refs (X chars)`）
  与 `data/deep_reads_index.json`，作为日后调 prompt 的参考数据；重跑已存在的论文时就地刷新。
- **跨篇综合 / 选题引擎**：新增 `python -m research_news.synthesize`，把同一子方向近期的
  **期刊**精读聚合起来，归纳只在跨篇层面才看得见的信号——**反复出现的开放问题**（被 ≥2 篇
  独立论文点名，recurrence 即证据）、论文间的**张力**、以及接武器库的**迁移空位**。两段式：
  先用 `extract_problems.py` 把每篇精读抽成结构化「问题种子」（limitation / future work /
  窄结论 / 张力 / 迁移线索）存进 `data/open_problems.jsonl`（缺的才抽、可累积），再按 topic
  综合。贯彻一条原则——**LLM 只挖掘与归纳、不打分不排名**，每条点名来源论文供研究者自判。
  输出 `docs/synthesis/<date>-<范围>-<topic>.md` + 存档页 `docs/all_synthesis.md`（导航
  「选题综合」）。自包含，不触动 daily / journal 管道。
  - **可按期刊 / 期刊组聚合**：`--journal AoS,JASA`（short 或全名）、`--group core,applied`
    （`config/journals.yaml` 的组键），支持逗号分隔或重复传、可混搭、可再叠 `--topic`；
    `--list-journals` 列出所有组与期刊。不同范围各自独立成页、不互相覆盖（页名带范围 slug，
    索引按 date+scope+topic 去重）。期刊名匹配同时认 short（如 `JMLR`）和全名。
  - 全部参数：`--topic` / `--journal` / `--group` / `--since` / `--min-papers` / `--model`
    / `--list-journals` / `--dry-run`。

### Changed
- **精读 prompt 调整章节顺序：最简例子提到综述之后**。把原第四节「最核心、最简单的例子 /
  数学问题」上移为**第二节**（紧接领域综述），并要求展开例子前**先把所有符号、模型、可观测
  数据交代清楚**；原「这篇论文做了什么」「开放问题」顺延为第三、四节。意图：读者先在最小内核
  + 干净记号上建立直觉，再读第三节的完整技术展开。`DEEP_READ_SYSTEM` 篇幅预算相应改为
  一 ≥25% / 二 ≥15% / 三 ≥45% / 四 ≈10%。`survey_excerpt`（按 `### 一`→`### 二` 边界切片）
  仍只取领域综述节、不受影响。
- **精读 prompt 再迭代：重心转向「综述 + 把论文讲透」，砍掉按武器库找问题**。实践发现
  LLM 按研究者技能判断「能不能做」很不可靠、且常高估其能力，故大幅删减。`DEEP_READ_SYSTEM`：
  第二节升为重心（≥45%），新增**「证明路线与技术技巧」**（整体路线 / 关键跳跃点 / 技巧点名）
  与**「真实例子与应用（有就必须讲）」**；第三节从「武器库 A/B/C 找问题 + 迁移视角」精简为
  **「开放问题点到为止」**（最多 3-4 条、扎根具体语句、不判可行性、不匹配技能）；第四节由
  「阅读路线 + 检测题」改为**「最核心、最简单的例子 / 数学问题」**（剥掉一般性假设，讲清
  支撑整篇证明的最简特例 / 最小命题）。
- **天文精读 prompt 用上被引文献**：`DEEP_READ_ASTRO_SYSTEM` 原先抓了被引却不用（astro
  论文加被引后质量无变化）。把被引织进已有节——第三节「主流方法与局限」落到具体被引工作
  （作者-年份），第六节「下一步读什么」从**真实**被引文献里挑确切标题（禁止编造）。
- **Semantic Scholar 无 API key，被引检索改为更耐心的重试**：S2 拒了 key 申请，只能用
  免认证共享池（429 频繁）。已确认 S2 有这些论文、失败纯是限速、重试能救回，故重试预算
  3 次 → **6 次**（`S2_FETCH_ATTEMPTS`），退避改 `wait_random_exponential`（**带抖动**，
  避免与共享池其他人锁步重试，上限 30s / `S2_MAX_BACKOFF`），用 `Retrying` 在调用时读 env
  让 `.env` 生效。（曾尝试 OpenAlex 作被引兜底，但实测 OpenAlex 对近期 arXiv 预印本
  **无参考文献**——其引用数据来自 Crossref deposit，预印本没有；S2 是唯一解析 PDF 抽被引的
  来源——故已回退。）
- **精读重构为「先综述方向、再谈值不值得做」**：重写 `DEEP_READ_SYSTEM`，把重心从
  "这篇论文讲了啥 + 我能做什么" 改成 **先用 introduction + bibliography 把这个方向的
  发展脉络（history）综述清楚**（奠基→进展→frontier→本文位置、子线索聚类、核心问题与
  瓶颈、**明确标注"作者的 framing"与被引工作之间的张力**），**之后**才谈值不值得做、
  能做什么。问题种子要求 grounded（扎根在本文的 limitation / future work / 窄结论上），
  并新增「迁移视角」一节。落实一条原则：**LLM 负责挖掘与生成、不替研究者做质量评判**
  （不给论文打分），把判断材料交回研究者。
- **放宽精读上下文预算**：`MAX_PDF_CHARS` 60k → 240k（≈60k tokens，喂进几乎整篇含完整
  参考文献），精读输出 `max_tokens` 16k → 24k，以用满 128k 上下文窗口。
- **精读门槛对所有领域统一放宽到 6**：评分只看摘要，故 deep-read 门槛从"primary 需 ≥8、
  少数 topic ≥6"统一改为**所有 topic ≥ `score_threshold_deepread`（默认 6）**；并放宽
  `SCORE_SYSTEM` 的打分标准（拿不准就往 6-7 靠，避免漏掉相关论文）。原先按 topic 分桶的
  deep-read 选择逻辑（`DEEP_READ_LOWER_THRESHOLD_TOPICS`、application≥7）由统一阈值取代。

### Added
- **机构绿灯：top 学者免分进入精读**：新增 `config/institutions.yaml`（US News 2024
  全美大学前 50 + 一批策划的国际统计/数学强校：Oxbridge、ETH、EPFL、Toronto、Tsinghua、
  NUS、HKUST 等）+ `research_news/scrapers/affiliations.py`。任一作者属于名单内机构的论文，
  **无视相关性分数**直接进入深度阅读（仍会先生成首遍摘要），精读页标注「机构绿灯」。作者机构
  在 arXiv/Crossref 元数据里很稀疏，故运行时按 arXiv id / DOI 从 **OpenAlex** 回填机构信息。
  默认开启、失败即降级，`AFFIL_GREENLIGHT=0` 关闭，`OPENALEX_MAILTO` 走 OpenAlex 礼貌池。
- **精读检索核心被引文献（现默认开启）**：`research_news/scrapers/references.py` 通过
  Semantic Scholar 拉取本文 introduction 真正依赖的核心被引论文的标题 + 摘要 + 引用语境，
  作为「## 主要被引论文（已检索）」喂进精读，让综述基于实际引用而非标题猜测。失败即降级
  （仅用 PDF），`DEEP_READ_FETCH_REFS=0` 关闭。
- **重跑乱码 / 没跑完的摘要**：新增 `python -m research_news.rerun`，扫描
  `docs/daily/*.md` **和 `docs/journals/*.md`** 里因模型输出未转义引号或
  `max_tokens` 截断而渲染成生 JSON（含 ```` ```json ````）的「摘要」块并就地修复——
  优先用 LLM 重新生成（论文元数据从 `data/llm_scores.jsonl` 还原，沿用当初打分用的
  模型），正文未被截断时也能离线从残留 JSON 抢救出干净中文摘要。支持
  `--scope daily|journals|all` / `--date` / `--offline` / `--dry-run`，并已接入
  `run_daily.*` 的日跑收尾步骤。同时修复了 `summarize_paper` 的 JSON 修复在带
  ```` ```json ```` 围栏时失效、以及解析失败时把生 JSON 直接灌进摘要的问题
  （改为抢救干净正文并标记待重跑）。一次性清理了既有报告中 40 处乱码块。 #52
- **账户 + 半自动收藏**：站点新增右下角「👤 登录」。用一个带 `gist` 权限的 GitHub
  Personal Access Token 登录后，已读 / 未读状态与「收藏」会存进你账号下的一个私密
  Gist，多设备同步。需登录才显示徽标与收藏按钮（不再有 `?me=1` 本地模式）。
- 每日 / 期刊 / 精读页每篇论文旁新增 **☆ 收藏** 按钮，点一下即把论文加入收藏，
  并自动记录其类别 / 日期。
- 新增动态「收藏」页 `docs/favorites.md`（替代原「每周周报」菜单），两种视图：
  **总收藏**（按论文类别分大类、类内按日期降序）与 **按周**（按 ISO 周号，周内再按
  类别 / 日期）。每篇收藏可直接在网页写评论 / 笔记，并随状态同步；支持逐条移除与
  一键「复制为 Markdown」。旧的手工周报仍存档在 `all_weekly.md` 并从页面底部链接。
- 管道新增 `docs/data/topic_labels.json`（主题分类表）供收藏页按类别分组 / 排序；
  `docs/data/deep_reads_index.json` 增加 `topic` 字段，供精读页收藏时归类。
- 精读页大标题旁也加了「○ 未读 / ✓ 已读」开关，与日报 / 期刊页共用同一份已读状态。
- **公开收藏快照**：新增每晚定时 Action `publish-favorites.yml` + 脚本
  `research_news/publish_favorites.py`，读私密 Gist 并拼上 `highlights.json` 的摘要 /
  评分，写出 `docs/data/favorites_public.json`。未登录访客在收藏页看到这份只读快照
  （带摘要与评论）。摘要在发布时从仓库数据拼接、不入 Gist，故 Gist 不膨胀。
  需配置仓库 secret `GIST_TOKEN`（`gist` + `public_repo`）。

### Changed
- 精读存档页面每个主题下再拆 `Daily` / `期刊` 两个子段：daily 按日期降序平铺
  （同日按评分降序），期刊按日期分子段（最新在前），便于追上新增的精读。
- `data/deep_reads_index.json` 增加可选的 `venue` / `volume` / `issue` 字段
  （由 crossref 抓取的 journal 论文写入）；精读存档页面的期刊子段优先按
  `(venue, volume, issue)` 分组（如 `TIT Vol 72 Issue 3`），未填字段的老条目
  回退到 `run_date` 分组，向后兼容。

---

## [0.6] — 2026-05-25

### Changed
- 精读存档页面 (`all_deep_reads.md`) 改为按主题分组而非按日期，主题内部按评分降序、
  同分按日期降序排列，方便从主题视角直接浏览精读论文。 (#40)

### Added
- 新增 `CHANGELOG.md` 与站点导航中的「更新日志」入口；通过
  `docs/changelog.md → ../CHANGELOG.md` 符号链接复用单一源。 (#41)

---

## [0.5] — 2026-05-19 → 2026-05-20

围绕站点体验和长期数据沉淀。

### Added
- 全站 LaTeX 数学渲染：`pymdownx.arithmatex` + MathJax。 (#33)
- 手动维护的「每周周报」版块，统一存放维护者挑选的当周备忘。 (#34)
- Giscus 评论系统（GitHub Discussions 后端），并填好 `repo_id` / `category_id`。 (#35, #36)
- 把「统计-计算权衡 (statistical-computational tradeoff)」作为低门槛精读主题：与
  二级兴趣同样以分数 ≥6 进入精读，prompt 中明确为「outsider gateway reading」。 (#32)
- 全量打分日志 `data/llm_scores.jsonl`：在 daily / journals 流水线的 summarize 后追加
  写入所有 LLM 打分（含低分），保留摘要、topic、novelty_flag、key_techniques 等字段，
  作为日后做排序 / 推荐的训练数据。 (#39)

### Changed
- 精简首页，自动管理 weekly 存档列表。 (#35)

### Fixed
- 列举每周周报时跳过模板文件。 (#37)
- 周报报告中链接 / 评论 bullet 在带编号列表下的缩进。 (#38)

---

## [0.4] — 2026-05-18

阅读体验 + 天文统计专用流水线。

### Added
- 期刊存档按 config group 分组展示；每篇论文显示已读 / 未读徽章（`?me=1`
  个人模式下可见）。 (#24, #25)
- 天文统计 (astrostats) 独立的打分与精读 prompt，定位为「gateway reading」而非
  方法论迁移源。 (#28, #29)
- 期刊运行日志输出到 `logs/journals-*.log`，方便追溯失败。 (#26, #27)

### Changed
- `all_journals.md` 按 `config/sources.yaml` 中的 group 顺序排列，组内按刊名字母序；
  重新生成以包含 astro 组 (MNRAS, ApJS)。 (#30, #31)

---

## [0.3] — 2026-05-17

精读 (deep-read) 子系统上线。

### Added
- 高相关度论文的精读 LLM 分析：解析 PDF 主体并生成长文报告，单独存档于
  `docs/deep_reads/`，每日 / 期刊页面顶部插入精读链接。 (#16, #17, #18, #20)
- 顶栏导航 (`navigation.tabs`)，让各 archive 一级可达。 (#19)
- 二级兴趣主题 (astrostats / econ_theory / epidemiology) 评分 ≥6 也进入精读候选，
  扩展低分但高价值论文的覆盖。 (#23)

### Changed
- 精读改进合订：排序逻辑修正、PDF 解析乱码处理、更深的 prompt、更大的 LLM 上下文。 (#22)

### Docs
- README 更新以匹配新管道输出与站点结构。 (#21)

---

## [0.2] — 2026-05-16（下午）

journals 抓取链路加固。

### Added
- 出版社 landing-page 作为缺失摘要的 fallback。 (#5)
- OpenAlex 作为 T3 摘要源，绕开 Cloudflare 拦截。 (#7)
- arxiv title search 作为 T4 fallback，弃用易被 Cloudflare 拦的 landing page。 (#8)
- `journals` CLI：`--n-issues N` / `--save-papers` / `--load-papers`，把抓取与
  打分/总结解耦，便于反复实验。 (#11)
- JMLR 不再设抓取上限；新增增量保存与 token 用量统计；README 补全依赖。 (#13)
- 精读管道 (deep-read) 的雏形与首版整合。 (#16)

### Fixed
- T3 landing-page fallback 缺失原因的诊断与修复。 (#6)
- crossref：更宽的 arxiv title fallback + 更长的礼貌等待，避免 429。 (#9)
- crossref：在 backfill 前过滤 discussion / reply 类条目（JRSSB 问题排查）。 (#10)
- 修复损坏的 LLM summary 并新增 `--retry-broken` CLI。 (#14)
- 合并后恢复 group-based fetch + render。 (#15)

### Docs
- README 文档化 daily / journals / shootout 三条工作流。 (#12)

---

## [0.1] — 2026-05-16（上午）

最初的多管道骨架。

### Added
- prompt / depth shootout：用于评估总结质量的模型横评工具。 (#1)
- shootout 加载 `.env`；arxiv HTML 404 时回退到 PDF。 (#2)
- shootout 接入 JMLR 数据源，并支持跨模型批量 sweep。 (#3)
- 拆分 daily 与 journals 两条独立流水线；新增 Crossref scraper；渲染按主题分组。 (#4)

---

## 写作约定

把新的改动累加到 `[Unreleased]` 区段。等到一组改动构成一个可发布的里程碑时，
把 `[Unreleased]` 改名为 `[0.x] — YYYY-MM-DD` 并在上面再开一个新的
`[Unreleased]`。

合并 PR 后，从 PR 标题里提炼 1 句「为什么」放进对应分类，附 `(#N)`。
不必每个 PR 一条 —— 同一时间段的多个 PR 合成一条更易读。
