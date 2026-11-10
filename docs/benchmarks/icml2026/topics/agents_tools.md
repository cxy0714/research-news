# ICML 2026 · Agent / 工具使用

> 本页 4 篇（该主题共 4 篇），按相关性排序。 [返回总览](../index.md)

### 1. AgentSuite: Toward More Reliable Agent Evaluation with a Component-Based Benchmark Auditing Pipeline
- **链接**: [论文页](https://proceedings.mlr.press/v306/suh26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/suh26a/suh26a.pdf) · [OpenReview](https://openreview.net/forum?id=2Exmr1eIKZ)
- **作者**: Hyewon Suh, Binfei Ji, Seojune Lee, Rishi Khare, Basit Khan, Hyunjun Kim, Tianyi Zhang, Venkat Krishna Srinivasan et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: agent 基准中由指令、环境、工具、轨迹和评估协议交互产生的有效性问题（缺陷）
- **摘要**: AgentSuite 提出 COBA，一个组件化的基准审计流水线，用于诊断和过滤 LLM agent 基准中的有效性问题。COBA 将 agent 任务分解为用户、环境、真实轨迹和评估四个标准化组件，并利用混合规则检测器和分类学引导的 LLM 评估来操作化组件级问题分类。在六个广泛使用的 agent 基准上，COBA 与专家判断的 F1 分数在 0.791 到 0.874 之间，表现出强一致性。分析表明基准缺陷普遍存在且显著影响评估结果，COBA 还能以最小适配泛化到未见过的基准。作者发布了 AgentSuite 平台，包含 COBA 流水线和审计后的基准变体。
- **为什么值得看**: 该论文提供了一种可复用的基准审计流程，将任务分解为组件并系统化检测缺陷，直接回应了评测方法学中的效度问题，有助于识别基准伪影与模型错误的混淆。
- **关键技术**: `component-based decomposition`, `rule-based detectors`, `LLM-as-judge`, `taxonomy-guided evaluation`, `benchmark auditing`

### 2. Benchmarking World-Model Learning with Environment-Level Queries
- **链接**: [论文页](https://proceedings.mlr.press/v306/warrier26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/warrier26a/warrier26a.pdf) · [OpenReview](https://openreview.net/forum?id=Ny6UYZ8ysN)
- **作者**: Archana Warrier, Dat Nguyen, Michelangelo Naim, Moksh Jain, Yichao Liang, Karen Schroeder, Cambridge Yang, Joshua B. Tenenbaum et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 衡量智能体是否学习到支持多种环境级查询（如可达性、干预效果）的通用世界模型。
- **摘要**: WorldTest 提出一种评测协议，用于检验智能体是否学到支持多种环境级查询的世界模型，而非仅能预测下一帧或优化任务回报。它包含 43 个交互式网格世界环境和 129 个任务，覆盖三个查询族（如可达性、干预效果），这些查询的答案依赖于全局环境结构，无法由单一轨迹分布确定。AutumnBench 作为其实例，同时收集了 517 名人类参与者和五个前沿模型的表现，结果显示人类显著优于模型，差距归因于探索和信念更新方式的差异。该工作强调评测应超越可观测交互属性，关注模型对环境的通用理解能力。
- **为什么值得看**: 该论文提出了一个评测协议，明确区分了从观测轨迹可推断的属性与需要全局环境理解才能回答的查询，为评测世界模型的构念效度提供了新视角；同时通过人类基线和多查询族设计，展示了如何系统评估模型泛化能力，对评测方法学有直接贡献。
- **关键技术**: `benchmark construction`, `human baseline`, `query family design`, `environment-level evaluation`, `exploration analysis`

### 3. DEER: A Benchmark for Evaluating Deep Research Agents on Expert Report Generation
- **链接**: [论文页](https://proceedings.mlr.press/v306/han26m.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/han26m/han26m.pdf) · [OpenReview](https://openreview.net/forum?id=ILRx5neJk6)
- **作者**: Janghoon Han, Heegyu Kim, Changho Lee, Dahm Lee, Min Hyung Park, Hosung Song, Stanley Jungkyu Choi, Moontae Lee et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 深度研究智能体生成报告的多维质量（如逻辑完整性、证据质量）及声明准确性。
- **摘要**: DEER 是一个用于评估深度研究智能体生成专家级报告质量的基准。它通过专家开发的分类体系（7 个维度、25 个子维度）操作化为 101 个细粒度评分项，并提供了任务特定的专家评估指南以支持 LLM 作为评判者。除了基于评分项的评估，DEER 还提出了一种声明验证架构，用于验证引用和未引用的声明，并量化证据质量。实验表明，当前系统能生成结构合理、引用证据的报告，但在满足专家级用户需求和逻辑完整性方面仍有不足。DEER 不仅比较性能，还使系统优缺点可解释，并提供改进的诊断信号。
- **为什么值得看**: 该基准系统化了深度研究报告的评估标准，并提供了 LLM-as-judge 的专家指南，同时引入了声明验证架构，对评测方法学有具体贡献，特别是多维评分项的构建和证据质量量化。
- **关键技术**: `expert-developed taxonomy`, `rubric-based assessment`, `LLM-as-judge`, `claim verification architecture`, `evidence quality quantification`

### 4. DSGym: A Holistic Framework for Evaluating and Training Data Science Agents
- **链接**: [论文页](https://proceedings.mlr.press/v306/nie26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/nie26b/nie26b.pdf) · [OpenReview](https://openreview.net/forum?id=2WrNPRW9Km)
- **作者**: Fan Nie, Junlin Wang, Harper Hua, Federico Bianchi, Yongchan Kwon, Zhenting Qi, Owen Queen, Shang Zhu et al.
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 数据科学智能体在端到端数据分析任务中的规划、执行和验证能力，以及避免捷径解的能力。
- **摘要**: DSGym 是一个用于评估和训练数据科学智能体的标准化框架，提供自包含的执行环境。作者首先指出现有数据科学基准存在碎片化接口、任务覆盖窄和缺乏数据接地的问题，并证明当前基准中相当一部分任务可以在不使用实际数据的情况下解决（即捷径可解）。DSGym 通过模块化架构支持添加任务、智能体脚手架和工具，作为可扩展的活测试平台。他们构建了 DSGym-Tasks，整合并精炼现有基准，通过质量和捷径可解性过滤；并新增 DSBio（专家衍生的生物信息学任务）和 DSPredict（跨视觉、分子预测、单细胞扰动等领域的预测任务）。此外，DSGym 支持通过执行验证的数据合成流水线进行智能体训练，案例研究用 2000 个示例训练集显著提升了 4B 模型在标准化分析基准上的表现。该框架旨在严格端到端测量智能体在现实科学情境中规划、实施和验证数据分析的能力。
- **为什么值得看**: 该论文对评测方法学的价值在于：系统性地揭示了现有数据科学基准中的捷径可解性问题，并提出了可复用的过滤流程（质量与捷径可解性过滤）；同时，其模块化框架和任务套件为跨基准比较和持续扩展提供了标准化接口，有助于提高评测的构念效度和可比性。
- **关键技术**: `benchmark construction`, `shortcut solvability filtering`, `execution-verified data synthesis`, `modular framework`, `human-expert task derivation`
