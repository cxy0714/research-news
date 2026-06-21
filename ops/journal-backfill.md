# 期刊回补 Runbook（OpenClaw / agent 用）

把期刊的**历史卷期**一点点补齐——每天 daily 跑完之后，补**一个单元**（通常是一本期刊
的若干期），顺序进行、绝不并行，攒一两周把积压补完。Token 充足，唯一硬约束是 **不并行**。

> 这份文档就是给驱动它的 agent（OpenClaw）读的。状态用 **本文件里的清单**（git 里）记录：
> 做完一项就把 `- [ ]` 改成 `- [x]` 并写上日期，提交。git 即状态存储。

## 背景（够用就行）

- 期刊管道：`python -m research_news.journals --only "<短名>" --n-issues N`（JMLR 特殊，用
  `--jmlr-n N`；整组用 `--only-group <组>`）。`--n-issues N` 抓**最近 N 期**。
- **去重让回补天然可续跑**：`data/seen_papers.json` 会在渲染后记下已处理的论文，下次跑
  **更大的 N** 只会处理**新冒出来的更老的期**，已做过的期不会重复渲染、不耗 token。所以
  「逐步加大 N」「重跑同一单元」都安全 —— 重跑已覆盖的单元**不会产生任何提交**。
- 页面名带卷期（`<日期>-<刊>-vNN-iMM.md`），按刊+卷期归档，跟用哪天跑无关。

## 每次触发要做的事（daily 跑完之后）

1. **确认今天的 daily 已经跑完并推送**（看 `docs/daily/<今天>.md` 在、`git log` 有当天
   提交）。**daily 没结束前不要开始回补**。
2. `git pull --rebase` 把本文件清单更新到最新（别人/你昨天可能改过）。
3. 从下面 **Queue** 里挑**第一个未打勾**的项。
4. **先 dry-run 估量**（不调 LLM、不写盘、不抢锁）：
   ```bash
   python -m research_news.journals <那一项的参数> --dry-run
   ```
   看日志里的 `dry-run: N papers`。**若 N 偏大（≳150 篇）就调小 `--n-issues`**（高频刊
   见下方 ⚠），免得一个单元跑太久、压到第二天 daily。
5. **正式跑该单元**（脚本会自动 拉取→抢锁→跑→提交推送）：
   ```bash
   ./run_journal_backfill.sh <那一项的参数>
   ```
6. **核对结果**：退出码 0；`docs/journals/` 新增了对应卷期页；已提交并推送。
7. **打勾**：把该项 `- [ ]` 改成 `- [x] (YYYY-MM-DD, +M 篇)`，`git commit -am "backfill: mark <刊> done"` 并 push。
8. **一天最多做几项**就停（顺序、不并行），留足时间到第二天 09:10 daily 之前。汇报今天补了什么、还剩多少。

## 安全规则（重要）

- **绝不并行**：脚本和 `run_daily.sh` 共用同一把 `flock` 锁——daily 在跑时回补会直接退出，
  反之亦然。但你也别在 daily 即将触发前才开一个大单元。
- **一次一个单元，等它跑完**（脚本是阻塞的，跑完才返回）。
- ⚠ **高频 / 大刊**（每期论文很多）：先 dry-run、用**小 N**。包括：天文 `MNRAS` / `ApJS`、
  流行病 `StatMed`、IEEE `TIT`/`TPAMI`/`TSP`、`J. Econometrics`、`EJS`。这些建议从 `--n-issues 2`
  起步、看量再加。
- 多词短名要**加引号**：`--only "Statistica Sinica"`、`--only "Scand. J. Stat."`、
  `--only "J. Econometrics"`、`--only "Quant. Econ."`、`--only "JRSS-C"`。
- 失败处理：**抓取失败**（个别刊 ISSN/网络问题）就记一笔、跳过下一项；**精读失败的 stub**
  不用管这里——第二天 daily 的 `--retry-stubs` 会兜。
- 出现拿不准的情况（某刊抓回来量异常大 / 反复失败 / 影响到 daily），**停下来问人**，别硬冲。

## Queue（按价值排序：先补完全没有的组，再加深已有的）

> 默认 `--n-issues 8`（季刊≈2 年）。高频刊按 ⚠ 用更小 N。做完打勾即可；想更快可改成
> 整组 `--only-group <组> --n-issues N` 一把跑（更省事但单元更大，先 dry-run）。

### 阶段一 · 零覆盖的组（最高优先）

概率统计 prob_stats：
- [x] (2026-06-18) `--only AoP --n-issues 8`
- [x] (2026-06-18) `--only Bernoulli --n-issues 8`
- [x] (2026-06-19) `--only EJS --n-issues 4`   ⚠ 电子刊、文章多，先 dry-run
- [x] (2026-06-19) `--only "Statistica Sinica" --n-issues 8`
- [x] (2026-06-19) `--only "Scand. J. Stat." --n-issues 8`

流行病 epi：
- [x] (2026-06-19) `--only StatMed --n-issues 2`   ⚠ 双周刊、量大
- [x] (2026-06-19) `--only SMMR --n-issues 6`
- [x] (2026-06-19) `--only AJE --n-issues 4`   ⚠ 月刊
- [x] (2026-06-19) `--only Epidemiology --n-issues 6`

天文 astro：
- [x] (2026-06-19) `--only MNRAS --n-issues 1`   ⚠⚠ 体量巨大，务必先 dry-run，必要时只 1 期
- [x] (2026-06-19) `--only ApJS --n-issues 2`   ⚠ 大刊，先 dry-run

### 阶段二 · 加深已有的组（目前只到最近 ~2–4 期）

应用 / 生物统计 applied（目前只 ~2 期，优先加深）：
- [x] (2026-06-19) `--only AoAS --n-issues 8`
- [x] (2026-06-20) `--only Biometrics --n-issues 8`
- [x] (2026-06-20) `--only Biostatistics --n-issues 8`
- [x] (2026-06-20) `--only "JRSS-C" --n-issues 8`

理论核心 core：
- [x] (2026-06-20) `--only AoS --n-issues 12`
- [x] (2026-06-20) `--only JASA --n-issues 12`
- [x] (2026-06-20) `--only JRSSB --n-issues 12`
- [x] (2026-06-21) `--only Biometrika --n-issues 12`
- [x] (2026-06-21) `--only JMLR --jmlr-n 3`   （JMLR 用 --jmlr-n，不是 --n-issues）

经济 / 计量 econ：
- [x] (2026-06-21) `--only Econometrica --n-issues 12`
- [x] (2026-06-21) `--only "J. Econometrics" --n-issues 4`   ⚠ 出刊密、量大
- [x] (2026-06-21) `--only "Quant. Econ." --n-issues 8`
- [x] (2026-06-21) `--only JBES --n-issues 8`

IEEE 系列 ieee（月刊、每期很大，全部先 dry-run、用小 N）：
- [x] (2026-06-21) `--only TIT --n-issues 2`   ⚠
- [x] (2026-06-21) `--only TPAMI --n-issues 2`   ⚠
- [x] (2026-06-21) `--only TSP --n-issues 2`   ⚠
- [x] (2026-06-21) `--only JSAIT --n-issues 4`

## 补得更深（之后想再往前翻）

清单全打勾后，想继续往更早的年份补：把对应项的 `--n-issues` 调更大重跑即可（去重只会处理
更老的新期）。例如 `--only AoS --n-issues 24`。建议另起一轮、重置勾选，或在行尾追记 `(→24)`。
