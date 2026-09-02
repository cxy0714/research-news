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

### Added

- **选题提案引擎 `research_news/proposals.py`**：把攒下来的精读语料 + 收藏变成**可上手的提案**
  ——能投出去的标题、点名数学对象的 claim、先打哪个最简特例、哪几篇论文**独立**点名了这个 gap
  （附原话）、接武器库的哪一件、什么会杀死它、第一周做什么。候选池是「每篇取最新一次精读，
  `score >= 8` **或**已收藏」（收藏不受分数门槛限制：手挑比任何 LLM 分数都更能说明想做什么，
  且科普 / 天文 rubric 本来就压低分）。四段式：①**战线划定**（LLM，每 topic 桶一次，只让收藏
  或 `score >= 9` 的种子论文参与）产出中文标签 + 范围 + 英文关键词，落 `config/fronts.yaml`
  ——**生成后可手改**，改 `keywords` 即调整成员、删一条即弃用，重跑 `--build-fronts` 覆盖；
  ②**论文归属**（纯确定性、无 LLM）按关键词 / 技术标签子串匹配，允许一篇进多条战线；
  ③**去重 + 择优**，论文集合 Jaccard ≥ 0.5 丢一条，再按「主兴趣 → 武器库覆盖面分档 → 收藏数」
  取前 N（`--max-fronts` 默认 14）；④**提案生成 + 渲染**（LLM，每战线一次，最多 30 篇、收藏优先）。
  站点页 `选题提案`（`docs/all_synthesis.md`）+ `docs/proposals/<战线>.md` + `data/proposals.json`。
  不接定时流水线（语料增长慢，手动 / 按周跑即可）。**LLM 只生成，不打分不排名**，排序键全是
  可审计的计数。
- **手动录入支持免费 / 开放获取期刊**：粘一条期刊文章链接或 DOI，次日精读就直接读**期刊自己的
  全文 PDF**，不再要求存在 arXiv 预印本。新模块 `research_news/oa_pdf.py` 三层解析：落地页的
  `citation_*` 元标签（绝大多数出版社都发，所以「很多免费刊」不需要逐个登记）→ 少量 host 规则
  （落地页被反爬 / 是 JS 应用的站点）→ OpenAlex 的 OA 位置（`work_oa_info`）。每个候选都要**下回来
  验 `%PDF` 魔数**，付费墙页 / 反爬页永远不会被当成 PDF 存下来。

### Changed

- **不再「先用 LLM 把每篇抽成 JSON」**：精读笔记里的开放问题本来就带扎根引文（`扎根点：Remark 5`），
  所以改成按表头**前缀**（不是精确标题——格式漂移过四个月，`四、开放问题` 有 4 个变体）确定性切出
  五段（方向瓶颈 / 作者 framing / 被引张力 / 结论比证明窄 / 开放问题）。600 篇抽样实测：只留
  **17% 字符**、开放问题覆盖 **83%**、引文原样保留。旧路子要 1300+ 次 LLM 调用，还把引文丢了。
- **战线扫到 >10% 池子就自动收紧**到「命中 ≥2 个关键词」：`influence function` 单个词就能命中
  7.7% 的池子，那种战线是 topic 桶不是战线。择优用「覆盖面分档」而非原始命中数——战线范围是中文、
  关键词是英文，同一领域有多个近义写法，按命中数排等于奖励话多的那条。
- **精读笔记里的旁注不得当证据**：55% 的 gap 切片含「您 / 研究者 / 武器库」字样，那是上一次精读时
  LLM 自己写的建议，不是论文内容。引用它会变成循环论证（LLM 拿 LLM 的建议证明 gap 是真的）。
  现在切片时给这些行打标记、prompt 里明令禁止引用，并有 `n_commentary_leak` 自动审计写进日志。
- 旧的**跨篇综合** `synthesize` 仍可跑、`docs/synthesis/*.md` 全部保留（从提案总览页底部可达），
  但存档页 `docs/all_synthesis.md` 现归提案引擎所有——跑 `synthesize` 会把它覆盖回旧版索引，
  重跑一次 `proposals` 即恢复。
- 取全文时**代理与直连都试**：arXiv / OpenAlex 一类要走本机代理（GFW），而认校园 IP 的出版社
  经代理会被弹反爬页（Project MUSE 就是），所以先按环境代理试、失败再直连。反爬页本身是
  `text/html`，因此判据是「这页有没有 citation 元数据」，不是「有没有拿到 HTML」。
- 期刊论文（DOI）过去一律没有 PDF、精读只喂摘要；`highlights.download_pdf` 现在会回落到 OA
  解析器，免费刊因此拿到真全文。`OA_PDF=0` 可关掉这层回落。

### Fixed

- **JMLR 精读一直只读到摘要**：`highlights._pdf_url` 拼的是 `/papers/v27/<stem>.pdf`（404），
  真实路径是 `/papers/volume27/<stem>/<stem>.pdf`。
- `oa_pdf.fetch_pdf` 只重试传输错误，不重试「响应不是 PDF」（重试也不会变成 PDF）。
- **`data/open_problems.jsonl` 被一次 merge 塞进冲突标记，静默腐蚀了三个月**：两个 loader 都
  「跳过解析失败的行」，于是冲突标记 + 被拼接的记录直接变成「语料少了一半」，而且不报任何错。
  `extract_problems` 现在读文件时检测 `<<<<<<<` / `=======` / `>>>>>>>` 并打 ERROR，要求按
  `paper_id` union 解决后再用。

---

## [0.11] — 2026-08-31

一届会议的全量深读、站内搜索换引擎、综合刊走科普通道，以及两个「无声失败」的根治
（Nature 只抓到 9 篇、GIST_TOKEN 到期打挂两条流水线）。

### Added
- **JCSDS 2026 全量会议深读流水线**：把第四届统计与数据科学联合会议（163 分会场 / 703 场报告）
  做成结构化清单 + 可浏览专题页 + 逐场深读。新模块 `research_news/conf/`：`match.py` 给
  （题目, 讲者）同时查 OpenAlex 与 arXiv，按标题相似度（token Jaccard 0.6 + SequenceMatcher 0.4）
  加讲者姓氏重合打分，过 `CONF_MATCH_THRESHOLD`（0.60）才算命中——**没查到就诚实标注「未检索到
  公开论文」，绝不编造**；`read.py` 有 arXiv 全文就喂全文、否则喂摘要；`run.py` 编排
  （`--group` / `--sessions` / `--all` / `--skip-done` / `--no-pdf`）。一轮跑完 647 场 / 158 分会场，
  `scripts/jcsds_*.py` 生成链输出 43 个专题页 + 总览 + 刷新 nav。各专题命中率 20–45%（中文本土 /
  环境统计题目多无预印本，属正常）。
- **会议报告的长篇精读**：对「命中且有 arXiv id」的 189 篇唯一论文改走日常管道
  `deep_read_paper()`——全文 24 万字、抓参考文献、四段结构，比内联短精读丰富得多，输出
  `docs/deep_reads/jcsds2026-<arxiv>.md` 并回填专题页的「📖 长篇精读」链接。**关键坑**：SJTU 端
  100k tokens/min 硬限、单篇 prompt ≈96k token，并发必触发 429，所以脚本内建 `TokenGate`
  （60s 滚动窗口每分钟只放行一篇），跑时须 `SJTU_TIMEOUT=600`。按「非 stub 页已存在」断点续跑。
- **通用科学期刊走科普通道**：新增 `general`（Nature / Science / PNAS / Nature Methods）与
  `broad`（Nature Machine Intelligence / Science Advances / Nature Communications）两组，打
  `gateway_popsci: true` 标志。这些综合刊绝大多数文章在统计学之外，要的是「开阔眼界式科普为主、
  联系统计为辅」，不做牵强的方法迁移。落点全是 config-driven（加新科普刊只改 yaml）：
  `interests.yaml` 加 `general science` gateway rubric、新 `DEEP_READ_GENERAL_SYSTEM` prompt、
  打分 payload 加 `venue`。**按 venue 而非 topic 切换**——一篇 Nature 的因果文也走科普 prompt。
- 期刊新增 **compute 组**（JCGS / Technometrics / Stat. Comput. / CSDA）+ 第四阶段回补队列。
- `run_daily.ps1 -Force`：把 `--force` 透传给 `daily.py`，用于「今天只跑出一部分类目（arXiv 429）
  必须整页重跑」的情况。会**覆盖**当天页面。
- **GIST_TOKEN 到期预警**：`gist_state.token_health()` / `warn_if_expiring()` 读 GitHub 返回的
  过期日期，剩 ≤14 天就告警；CI 里到期前开 / 更新一个提醒 issue。

### Changed
- **站内搜索换 Pagefind**：内置 Material/lunr 会把全站正文打包成一个索引下载到浏览器再现场建索引，
  语料涨到 4700+ 页（102MB，其中精读 80MB）后「初始化搜索引擎」要卡好几秒。Pagefind 改为构建后
  扫 `site/` 生成切片索引，浏览器按查询只取几十 KB 分片、入口约 174B。Extended 版自带 CJK 分词，
  顺带改善中文搜索。新增独立搜索页 `docs/search.md`，`data-pagefind-body` 把索引限定到正文
  （排除导航 / 侧栏 / TOC 噪音）；构建链加 Node 20 + pagefind 步骤。
- **代理开关集中进 `research_news/netenv.py`**：arXiv / OpenAlex / Crossref 在校园网直连会
  `SSL: UNEXPECTED_EOF_WHILE_READING` / TLS 握手超时，现在按标准代理环境变量统一导出（httpx 与
  urllib 都自动遵守，**调用处一行不改**），国内 LLM 网关与 `*.cn` 留在 `NO_PROXY` 走直连。
  `PROXY_URL=` 置空即整体关掉，`NO_PROXY_EXTRA` 可追加直连 host。

### Fixed
- **Nature 只抓到 9 篇论文（无声丢掉大半个期刊）**：`crossref.fetch_latest_issue` 只要存在带期号的
  期，就把所有没有 volume+issue 的文章全部丢掉。可综合刊大多数文章先以 online-first 发布、要几周后
  才编进期号，于是主体内容被静默丢弃。现在带期号的分支也保留最新的 online-first 条目，按 `n_issues`
  比例设上限；传统期刊（全带期号、无 online-first）行为不变。Nature 在 `n_issues=2` 下从 12 篇涨到 42 篇。
- **GIST_TOKEN 过期（周期性故障）打挂两条流水线且症状完全误导**：classic PAT 默认 90 天到期，
  一死就同时带走夜间收藏快照 workflow 与本机手动录入队列——而且 workflow 是**在 checkout 阶段**失败
  （用同一个 PAT），报错跟 token 毫无关系。现在 401/403 单独抛 `GistAuthError` 并带上「去哪重签、
  勾哪些 scope、要同时改仓库 secret 和本机 `.env`」；`publish_favorites` 直接以此退出，
  `manual_requests` 打 ERROR 但不中断当天提交；workflow 把「Verify GIST_TOKEN」放在 checkout **之前**，
  失败邮件因此直指病根。配 `tests/test_gist_token.py` 覆盖。
- 收藏快照 CI 装不齐依赖：`research_news/__init__.py` 现在会 import python-dotenv，而 workflow 只装了
  httpx，于是夜间任务 `ModuleNotFoundError: No module named 'dotenv'`。改成 `pip install -e .`。
- 收藏快照 CI 又被代理默认值坑：runner 上没有本机 Clash，`netenv` 的 `127.0.0.1:7897` 连不通，
  显式设 `PROXY_URL=""` 关掉这层。

---

## [0.10] — 2026-07-02

模型配置一处集中、一键全局切换，并修好一个「改了 `.env` 却不生效」的加载顺序 bug。

### Fixed
- **`.env` 里的模型配置从未生效，一律回落硬编码的 `glm-5.1`（加载顺序 bug）**：各模块在
  **import 时**就把模型名读进模块级常量（`DAILY_MODEL = os.environ.get("DAILY_MODEL", "glm-5.1")`），
  而 `load_dotenv()` 却在各自的入口函数里才调用——等它跑时常量早已绑定，`.env` 的值根本没被
  读到，于是所有跑批（daily / journals / synthesize / talks / manual / backfill / rerun）都在用
  硬编码默认值 `glm-5.1`。这就是「glm-5.1 挂了、改了 `.env` 也切不掉」的根因。修法：在包
  `research_news/__init__.py` 里提前 `load_dotenv()`——`python -m research_news.X` 必先导入包，
  故 `.env` 在任何子模块读常量之前就已加载，一处修复覆盖所有模块。子模块入口里原有的
  `load_dotenv()` 保留无害（幂等）。

### Changed
- **模型配置集中进 `.env`，一处改全局生效**：把散落各模块的模型环境变量整理成一块，注释写清
  级联关系。真正的**总开关只有两个**——`DAILY_MODEL`（轻量任务：打分 / 摘要 / 概览）与
  `DEEP_READ_MODEL`（长文精读）；`JOURNALS_MODEL` / `SYNTHESIS_MODEL` / `TALK_OVERVIEW_MODEL`
  默认级联自 `DAILY_MODEL`，`TALK_MODEL` 级联自 `DEEP_READ_MODEL`（留空即跟随，只想给某类任务
  单独钉模型时才填）。`SJTU_MODEL_FAST` / `SJTU_MODEL_DEEP` 是 client 底层默认（调用方不显式传
  model 时才用，多数调用会显式传）。`glm-5.1` 用不了时只改 `DAILY_MODEL` 一行，期刊 / 综述 /
  talk 概览自动跟着换。`.env.example` 同步。

### Docs
- **README 增补模型切换与 Windows 定时任务的常用命令**：模型一节讲清「改 `.env` 的两个总开关
  即全局切换」；新增查看 / 手动触发 / 启停三个计划任务（`research-news-daily` /
  `research-news-catchup` / `research-news-journals`）的 PowerShell 命令。

---

## [0.9] — 2026-06-25

网页手动录入 + 收藏即补读，期刊往期全自动回补，Windows 开机补齐缺天。

### Added
- **网页手动录入论文 → 次日定时精读（与 Gist 联动）**：收藏页顶部新增「✍️ 手动录入论文」框，
  登录后粘贴 arXiv 链接 / 编号（可多条）即可。论文 **默认加入收藏**，并写进同一个私密 Gist 的
  新字段 `queue`（与收藏一样跨设备同步）。`run_daily.*` 新增一步 `research_news.manual_requests`：
  用 `GIST_TOKEN` 读队列，对**尚未精读**的链接按 id 抓元数据（新增 `arxiv.fetch_by_ids`）→ 打分 +
  首过摘要 → 下 PDF → **精读**（`run_type="manual"`），并把结果幂等地注入当天日报的
  **「✍️ 手动录入的论文」** 章节（计数行下方、digest 之前），同时进精读存档。去重靠
  「`paper_id` 已在精读索引中则跳过」，无需把状态写回 Gist；精读完成后前端从
  `deep_reads_index.json` 回填收藏 / 录入列表的 **🔍 精读** 链接。无 `GIST_TOKEN` 时该步安静跳过，
  绝不影响日跑。新增共享模块 `research_news.gist_state`（`publish_favorites` 同步改用）。
- **收藏即补读：收藏未精读的论文，次日自动补精读**：在日报里点 ☆ 收藏一篇没精读的 arXiv 论文，
  下次 `manual_requests` 会把它当成隐式队列（`favorite_deepread_ids`，按收藏时间新→旧）自动补一份
  精读，无需再去录入框。每次限量 `MANUAL_FAV_LIMIT`(默认 10) 篇，剩余后续几天补完（日志记录余量）；
  `AUTO_DEEPREAD_FAVORITES=0` 可整体关闭。已带精读链接的收藏、非 arXiv 书签会跳过。
- **手动录入支持非 arXiv 论文（按标题找预印本）**：录入框现在也接受**标题 / 整条引用 / DOI**，
  不必是 arXiv。这类 `kind:"lookup"` 请求由 `manual_requests` 处理：LLM 抽出干净标题 → 复用
  `crossref._arxiv_search_match` 按标题去 arXiv 找预印本——找到就解析 id、照常精读；找不到就只作
  书签收藏。结果写进**提交进仓库**的 `docs/data/manual_resolved.json`（只读回传给浏览器 + 去重 +
  每 7 天复查"未找到"项）；前端据此显示状态（排队中 / 已精读 / 未找到预印本）并把找到的书签链到精读页。
- **期刊往期回补全自动 `journal_backfill` + Windows 连续循环任务**：`python -m research_news.journal_backfill`
  读 `ops/journal-backfill.md` 的待办清单，跑**下一个未打勾**的单元（一本刊的若干期）、成功后
  自动打勾、队列空时退出码非 0，无需 agent。`--max N` / `--dry-run`。`run_journal_backfill.ps1`
  是一个**连续循环**：一格接一格补到队列空、单元间释放锁、pull→跑→提交推送（按机器名记日志）。
  `register-task.ps1` 加第三个任务 `research-news-journals`（**登录自启循环** + 每日 10:30 重启兜底，
  `-JournalMax`/`-JournalTime`/`-NoJournals` 可调）。机器常开约 1-2 天补完整个清单——token 不是
  瓶颈（周配额 10 亿，单元才 0.2-0.5M），限制是开机时长。
- **期刊循环给 daily 让路 + daily 改为等锁**：期刊循环在 daily 时段（默认 9:00–11:00、当天报告
  还没出来时）不抢锁、主动让路；`run_daily.ps1` 的锁从「占用即跳过」改为「**等锁**最多 3h」。
  两者配合保证 daily 永远不会因为期刊正在跑而被跳过（一格未跑完就到 9:10 的话，daily 排在其后）。
- **期刊每期导览 `journal_overview`**：期刊每期页顶部加一段 LLM **导览**（归纳本期主线 /
  主题，**不打分、不排名**），和 OCIS 季页共用同一套「导览」模式。新跑的期自动带
  （`journals` → `render_journal_page(overview=…)`）；历史页用
  `python -m research_news.journal_overview` 回填——**从页面自身解析**每篇的题目 + 主题 +
  中文摘要（不重抓、不重打分、不依赖快照），生成导览插到计数行下方、首个主题分组之前。幂等
  （已有导览的页跳过，`--force` 重生成），范围 `--only AoS,JASA` / `--date` /
  `--since..--until` / `--dry-run`（只数页、不调 LLM）。
- **OCIS 讲座按季成页 + 导览 `talks seasons`**：把讲座目录按季（对齐 OCIS 官方分季，
  `import-ocis` 现给每场打 `season` 标签，缺失则按日期派生）成页 `docs/talks/seasons/<季>.md`。
  每页一段 **LLM 导览**（归纳本季主线、反复出现的方法、值得先看的几场，不打分不排名）+ 全部
  报告：每场链到精读，**网页有元数据但未精读的也列出**（标「暂无精读」+ 视频/幻灯片/论文链接）。
  `docs/all_talks.md` 改为**按季的索引**（年份分组、每季一行带场数与一句话导览），由
  `talk_seasons` 接管（读流程不再重写它）。季页从全量 catalog 生成（含无视频/未精读的场次），
  精读链接据 `data/talks_index.json` 解析。`--season` / `--no-overview`（离线）/ `--dry-run`。
  **按会议（series）分组**：页面与索引先按会议（OCIS / INI…）再按季分，页名
  `docs/talks/seasons/<series>-<季>.md`；series 取自每场 `series`（缺则按 venue 派生）。
  并**纳入手工 `config/talks.yaml`** 的非 OCIS 讲座（如 INI 的 Robins keynote），不再只看
  OCIS catalog——之前手工讲座虽已精读却不在任何季页里。`--force` 重写导览，否则复用既有
  （含旧无前缀页名兜底），全量刷新会清掉过期季页。
- **Windows 开机补齐缺天 `scripts\catch-up.ps1`**：台式机不会 24 小时开，关机会错过当天的
  定时跑。catch-up 找到最新的 `docs\daily\<日期>.md`，把从那以后到**昨天**缺的**工作日**用
  `daily --date <X>` 一次性补齐（跳过周末，今天留给 09:10 的 daily 任务）。靠 daily 的重跑
  保护，已存在的报告不覆盖；与 daily **共用同一把锁**，排队不并行（等运行中的 daily 跑完
  再补）；默认最多往前 14 天（`-MaxDays`）。`register-task.ps1` 现在同时注册 `research-news-daily`
  （工作日 09:10）与 `research-news-catchup`（登录 +3 分钟），`-NoCatchUp` 可只装前者。
- **期刊历史卷期回补 `run_journal_backfill.sh` + `ops/journal-backfill.md`**：把期刊积压的
  历史卷期节奏化补齐——每天 daily 后补一个单元（一本刊若干期），顺序、绝不并行。去重让
  「逐步加大 `--n-issues`」天然可续跑、重跑已覆盖单元零提交。脚本自动 pull → 抢锁（与 daily
  同一把 `flock`）→ 跑 `research_news.journals` → 提交推送；`ops/journal-backfill.md` 是给
  OpenClaw / 定时 agent 读的 runbook：按价值排序的待办队列（先补零覆盖的 prob_stats / astro /
  epi，再加深 core / econ / applied / ieee）、操作流程与安全规则，状态用清单勾选记在 git 里。
- **部署脚本统一 `run_rn.sh` + `run_daily.sh`**：`run_rn.sh` 作服务器入口（cd 仓库 → 激活
  venv → `git pull --rebase --autostash` 先同步免得收尾 push 被拒 → `exec run_daily.sh`）；
  `run_daily.sh` 持管道与锁（daily → 修摘要 → 恢复当天 stub → `git add -A` 提交推送）。逻辑
  集中、进版本控制，cron 指 `run_rn.sh` 即可。互斥锁用 `flock`（进程退出内核自动释放，
  `kill -9` / 断电不留死锁），daily 与期刊回补共用同一把、保证不并行。Windows 侧 `run_daily.ps1`
  同步对齐（命名 Mutex 单实例锁 → `git pull` → daily → 修摘要 → 恢复当天 stub → `git add -A`
  带重试 push），新增 `scripts/register-task.ps1` 一条命令注册任务计划程序任务（错过自动补跑、
  不并行）；`run_daily.bat` 改为转发到 ps1。**daily 用纯 cron / 任务计划即可，无需 agent。**
- **恢复失败的精读页 `backfill_deep_reads --retry-stubs`**：深度阅读偶尔失败（LLM 超时 /
  报错），精读页只剩 `*（精读失败，请查看日志）*` 占位。新增 `--retry-stubs` 扫
  `docs/deep_reads/*.md` 找这些 stub，从 `data/llm_scores.jsonl` 还原论文、按
  `data/deep_reads_index.json` 补回 header，重跑深度阅读就地覆盖。按文件名对索引拿真实
  paper_id（arXiv / DOI 都行），索引缺失则从文件名解析（arXiv id 即 slug）；幂等（只重生
  成仍是 stub 的），可放进每日 cron。取代硬编码的一次性脚本 `rerun_stubs.py` /
  `rerun_deep_reads.py`。`run_daily.sh` 已接入（日跑后补当天 stub），并加了 `flock` 互斥锁
  防止两个触发并行、`git add -A` 一并提交 `docs/` + `data/` + `logs/`。
- **每日报告展示全部论文 + 历史补全 `backfill_low_relevance`**：每日页不再只留阈值以上
  的论文。够格的（score ≥ `score_threshold_show`）照旧分组 + 生成中文摘要；其余的（低于
  阈值）汇到页尾 **🗂 其他论文** 一节，按评分由高到低排列，**只列 LLM 评分 + 一句简评，
  不再生成摘要**——这些字段每篇打分时就存进 `data/llm_scores.jsonl`，所以零额外 LLM
  调用。新增 `python -m research_news.backfill_low_relevance` 把过去报告里被遗漏的论文从
  打分日志**就地补回**对应日期页（纯离线、幂等、按 source 过滤掉期刊管道写进同一日志的
  非 arXiv 行）。

- **历史摘要补全 `backfill_summaries`**：把上限取消前堆在历史页 🗂 里的过阈值论文，读
  `data/llm_scores.jsonl` 里的摘要、补生成中文摘要，再整页重渲染、让它们归位到 📌/⭐ 主题
  分组（需 API key）。既有摘要原样保留（只补没摘要的），只对那几篇花 token。带
  `--self-check`：不提升、只把每页重渲染一遍逐字比对，确认页面解析器不会动到既有内容
  （无需 API key，可先跑确认全绿）；解析对作者/机构等"列表拼接"字段整段保留、对摘要里的
  杂散 CR / 换行也能逐字还原。

### Changed
- **取消单日摘要 25 篇上限**：过阈值的论文当天全部展开生成摘要，不再受篇数上限截断而漏到
  🗂 区。（上限取消前的历史页仍有超限未展开的高分论文落在 🗂 里，评分仍标着；用上面的
  `backfill_summaries` 可一次性补齐。）
- **`render_daily` 新增 `papers_low` 参数**：渲染页尾 🗂 其他论文 一节；计数行加上
  「· 其他 N 篇」。`format_daily_count_line` / `render_low_section` 抽出共享，供日跑与历史
  补全复用，保证两条路径渲染一致。

### Fixed
- **周一（及任何 RSS 延迟的早晨）daily 抓到 0 篇 / 空报告**：`rss.arxiv.org` feed 周一早上
  9:10 还没刷出当天批次（周日 20:00 美东公告，到点还没传到 RSS），五个分类全返回 0、当天报告
  整空。三处修复：① RSS 抓到 0 篇时**自动回退 search API**（按 submittedDate 查、更可靠）；
  ② API 时间窗从回溯 2 天放宽到 **4 天**，让周一也覆盖到周末（周五下午提交、周一才公告的论文）；
  ③ 重跑保护对**空报告**放行——空报告（抓 0 篇那种）不再被 guard 锁住，之后重跑能就地恢复。
- **收尾 `git push` 被远程超前拒绝时会先 rebase 再重试**：之前 push 失败只是原样重试（带退避），
  对 non-fast-forward（远程在本次运行期间被另一台机器 / 网页合并推进）无效，于是放弃、要手动
  `git pull` 再推。现在 `run_daily.ps1` / `catch-up.ps1` / `run_daily.sh` / `run_journal_backfill.sh`
  在 push 失败后都会 `git pull --rebase --autostash` 再推一次。
- **多机日志文件名带机器名，避免跨机覆盖 / 混淆**：多台机器（云服务器 + 台式机）对同一仓库跑
  时，都写 `logs/<日期>.log` 会撞名、两边运行互相覆盖 / 交错，回看时分不清哪台跑的。新增
  `logsetup.host_tag()`，日志改名为 `logs/<日期>-<机器名>.log`（期刊 `journals-...`、Windows
  transcript `run-<日期>-<机器名>.log` 同理），各机各写各的。
- **重复运行 daily 会把当天报告覆盖成近乎空白（数据丢失）**：`seen_papers.json` 是跨天全局
  去重，对同一天再跑一次 daily 时 `filter_new` 会把当天**已处理**的论文全过滤掉，
  `render_daily` 随即用只剩零星几篇的页**覆盖**掉完整报告（2026-06-17 实际从 66KB 被覆盖成
  6.5KB）。新增**重跑保护**：目标日期报告已存在且未加 `--force` 时直接跳过渲染、绝不覆盖；
  `--force` 重生成时跳过 seen 去重以产出完整页。这样 `run_daily.sh` 一天内被重复触发也安全
  （daily 步骤跳过、`--retry-stubs` 照常补当天失败的精读）。被覆盖的 06-17 报告已从 git
  历史恢复。
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

---

## [0.8] — 2026-06-13

跨篇综合 / 选题引擎，讲座（OCIS / seminar 录像）精读管道，每日报告展示全部论文。

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

---

## [0.7] — 2026-06-01

精读方向重构：从「这篇讲了啥」转向「先把方向综述透、再谈值不值得做」；机构绿灯、核心被引文献、账户 + 收藏。

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
