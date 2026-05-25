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
