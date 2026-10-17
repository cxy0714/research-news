# XAGI 2026 精读队列（Runbook · agent 用）

XAGI 2026 交叉智能大会（2026.10.16-18，北京友谊宾馆）的**逐场精读**队列。
**一格 = 一场报告**，从第一个未打勾的格子开始，顺序执行、绝不并行。

- 驱动：`python -m research_news.xagi backfill --max 1`（Windows 计划任务走 `run_xagi_backfill.ps1`）。
- **共享锁**：与 daily、期刊回补共用 `Global\research-news-daily` 互斥量，同一时刻只允许一个任务。
- **可续跑**：每格把结果写到 `data/conferences/xagi2026/research/<cell>.json`；已生成的格子
  重跑会跳过（`--force` 才重做），所以中断 / 重跑都安全。
- **产物**：`docs/conferences/xagi2026/session-XX.md`（逐场精读页，随进度刷新）、
  `docs/deep_reads/xagi2026-<arXiv>.md`（对应论文的长篇精读）。
- 打勾由驱动自动完成（`- [ ]` → `- [x] (日期)`）；要重做某格，就把它改回 `- [ ]` 再跑。

## Queue

### Session 01 · Keynote · 2026-10-17 08:45-12:00 · 聚英厅（友谊宫二层）
- [x] (2026-10-17) `sess01-t1` 主办方致辞 — 刘军（清华大学）
- [x] (2026-10-17) `sess01-t2` 人工智能随想录 — 孙茂松（清华大学）
- [x] (2026-10-17) `sess01-t3` Neuroscience Where AI = Science — 冯建峰（复旦大学）
- [x] (2026-10-17) `sess01-t4` 大模型中离群值的功能性分析 — 邱子涵（Qwen）

### Session 02 · AI4Math & Theory · 2026-10-17 14:00-16:00 · 9会（友谊宫二层9号会议室）
- [x] (2026-10-17) `sess02-t1` 深度学习理论的技术科学道路 — 刘方辉（上海交通大学）
- [x] (2026-10-17) `sess02-t2` LLM for ML Theory at Scale: The VALG Agent and OpenTheoryBench — 邹荻凡（香港大学）
- [x] (2026-10-17) `sess02-t3` 数学自然语言的形式化与结构化 — 罗涛（上海交通大学）
- [x] (2026-10-17) `sess02-t4` MechGeo: Autoformalizing and Proving Euclidean Geometry in Lean 4 — 沈皓（中国科学院数学与系统科学研究院）

### Session 03 · LLM评测 & Benchmark · 2026-10-17 14:00-16:00 · 7会（友谊宫二层7号会议室）
- [x] (2026-10-17) `sess03-t1` 大模型数据归因：从行为溯源到精准干预 — 潘亮铭（北京大学）
- [x] (2026-10-17) `sess03-t2` 科学大模型的数据自动化：数据整理、推理合成与定制评测 — 刘泽群（中关村学院）
- [x] (2026-10-17) `sess03-t3` 大语言模型评测的两种视角 — 姚金戈（至知研究院）
- [x] (2026-10-17) `sess03-t4` 大语言模型持续优化能力评测 — 张辉帅（北京大学）

### Session 04 · 预训练算法的新进展 · 2026-10-17 14:00-16:00 · 5会（友谊宫二层5号会议室）
- [x] (2026-10-17) `sess04-t1` On Optimal Hyperparameter Scaling for LLM Pretraining — 张华清（清华大学）
- [x] (2026-10-17) `sess04-t2` Controlled LLM Training on Spectral Sphere — 胡译文（中国人民大学）
- [x] (2026-10-17) `sess04-t3` Pretraining Loss相同，模型能力则相同么？ — 陈焕然（清华大学）

### Session 05 · AI Infra · 2026-10-17 14:00-16:00 · 3会（友谊宫二层3号会议室）
- [x] (2026-10-17) `sess05-t1` 基于FlagOS的高性价比混合云Token工厂 — 张先轶（澎峰科技）
- [ ] `sess05-t2` 跨集群异构PD分离：挑战、设计与工程实践 — 李秀红（无问芯穹）
- [ ] `sess05-t3` 基于昇腾的AgenticRL训练技术与企业级Agent落地实践 — 吴晨玮（华为）

### Session 06 · AI + Finance · 2026-10-17 14:00-16:00 · 4会（友谊宫二层4号会议室）
- [ ] `sess06-t1` From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models — 韩佳乐（深圳河套学院）
- [ ] `sess06-t2` Who Verifies Decentralized Information? Economic Incentives, Accountability, and Trustworthy AI Across Oracle Protocols — Luyao Zhang（Duke Kunshan University）
- [ ] `sess06-t3` Large and Deep Factor Models — Yuan Zhang（上海财经大学）
- [ ] `sess06-t4` Incorporating Return Prediction in High-Dimensional Mean-Variance Portfolio Optimization — 黄睿钊（香港科技大学）

### Session 07 · 扩散模型的理论基础以及推理测算法 · 2026-10-17 14:00-16:00 · 8会（友谊宫二层8号会议室）
- [ ] `sess07-t1` Weighted Laplacian Flow: A Deterministic Particle Flow with Provable Convergence — 史作强（清华大学）
- [ ] `sess07-t2` Simulation-Free Dynamic Unbalanced Optimal Transport and One-step Inference — 周沛劼（北京大学）
- [ ] `sess07-t3` 基于Bellman缺陷校正的科学机器学习与生成式人工智能的推理算法 — 陆一平（北京大学）
- [ ] `sess07-t4` Offline Deep Q* Estimation with Diffusion Models — 焦雨领（武汉大学）

### Session 08 · AI + 教育 · 2026-10-18 10:00-12:00 · 4会（友谊宫二层4号会议室）
- [ ] `sess08-t1` 从灵感到实现：AI赋能教育中的创造力支持 — 陈晴（同济大学）
- [ ] `sess08-t2` CogEvol：面向教育普惠的课件生成模型 — 涂尚卿（清华大学）
- [ ] `sess08-t3` 面向高等教育的AGI落地：未来学习中心建设的实践与思考 — 黄沛（华栖云教育）

### Session 09 · AI4Science · 2026-10-18 10:00-12:00 · 8会（友谊宫二层8号会议室）
- [ ] `sess09-t1` Memory Mechanisms in Genomic Foundation Models — 许慧楠（中国科学院大学）
- [ ] `sess09-t2` AI赋能聚变等离子体仿真、控制和诊断 — 吴泰霖（西湖大学）
- [ ] `sess09-t3` 跨发育阶段精神共病的层级神经认知模型 — 谢超（清华大学）
- [ ] `sess09-t4` 基因组大模型Carbon — 李秋熠（中关村学院）

### Session 10 · 机器学习理论 · 2026-10-18 10:00-12:00 · 3会（友谊宫二层3号会议室）
- [ ] `sess10-t1` 步长加速梯度下降的收敛下界 — 马鉴昊（清华大学）
- [ ] `sess10-t2` 在线学习与大模型高效推理 — 赵鹏（南京大学）
- [ ] `sess10-t3` Learning to Build Agents: Adaptive Planning, Memory, and Harness Evolution — 常恒（Unity China）

### Session 11 · Physics of Deep Learning · 2026-10-18 10:00-12:00 · 5会（友谊宫二层5号会议室）
- [ ] `sess11-t1` 从AI的物理学到AI自进化 — 刘子鸣（清华大学）
- [ ] `sess11-t2` Towards the Foundation of Deep Learning — 张耀宇（上海交通大学）
- [ ] `sess11-t3` 物理第一性 AI：从物理到智能 — 罗迪（清华大学）

### Session 12 · 扩散语言模型 · 2026-10-18 10:00-12:00 · 7会（友谊宫二层7号会议室）
- [ ] `sess12-t1` Parallel Generation, Iterative Refinement: The Evolution of LLaDA 2.x in Practice — 刘华斌（蚂蚁集团）
- [ ] `sess12-t2` 扩散式语言建模探索：从掩码扩散到连续扩散 — 胡天阳（香港中文大学（深圳））
- [ ] `sess12-t3` ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings — 李根（香港中文大学）

### Session 13 · AI的数理和计算基础 · 2026-10-18 14:00-16:00 · 4会（友谊宫二层4号会议室）
- [ ] `sess13-t1` Spiked Matrix Models with Rotationally Invariant Noise: AMP Algorithms and Optimality — 马俊杰（中国科学院数学与系统科学研究院）
- [ ] `sess13-t2` An Improved SE(3)-Transformer Driven by Hamiltonian Flow — 许洪腾（中国人民大学）
- [ ] `sess13-t3` 高效大模型 — 周峰（中国人民大学）

### Session 14 · Agent技术及应用 · 2026-10-18 14:00-16:00 · 3会（友谊宫二层3号会议室）
- [ ] `sess14-t1` 情境学习与协作发现：人工智能赋能教育教学新范式 — 王宏宁（清华大学）
- [ ] `sess14-t2` 自然语言驱动的数学研究智能体 - AIM系统的探索与实践 — 李鹏（清华大学）
- [ ] `sess14-t3` PilotDeck - 面向生产力的智能体操作系统尝试 — 闫宇坤（启元）
- [ ] `sess14-t4` Benchmarking Language Models for Statistical Problem Formulation — 从鑫（清华大学）
