# ACL 2026 · 领域基准

> 本页 2 篇（该主题共 2 篇），按相关性排序。 [返回总览](../index.md)

### 1. Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.150/) · [PDF](https://aclanthology.org/2026.acl-long.150.pdf)
- **作者**: Jinu Lee, Kyoung-Woon On, Sophia Simeng Han, Arman Cohan, Julia Hockenmaier
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: LLM 法律推理轨迹的议题覆盖度和正确性
- **摘要**: 本文提出 LEGIT（LEGal Issue Trees），一个大规模（24K 实例）专家级法律推理数据集，专门用于评估 LLM 生成的推理轨迹质量。作者将法院判决转换为层级树结构，包含对立双方的论点及法院结论，作为评估推理轨迹议题覆盖度和正确性的评分标准（rubrics）。通过人类专家标注和与粗略、信息量较少的评分标准对比，验证了该评分标准的可靠性。实验表明，LLM 的法律推理能力受议题覆盖度和正确性显著影响；RAG 和基于评分标准的 RL 带来互补收益：RAG 提升整体推理能力，而 RL 提升正确性但降低覆盖度。
- **为什么值得看**: 该论文提供了一种将领域知识结构化为层级评分标准（rubrics）的评测方法，并验证了其与人类专家标注的一致性，为复杂推理轨迹的评测提供了可复用的方法论，尤其适用于专家领域。
- **关键技术**: `rubric-based evaluation`, `hierarchical tree structure`, `human expert annotation`, `inter-annotator agreement`, `retrieval-augmented generation`

### 2. MedEinst: Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1847/) · [PDF](https://aclanthology.org/2026.acl-long.1847.pdf)
- **作者**: Wenting Chen, Guolin Huang, Wenxuan Wang, Zhongrui Zhu
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 医疗大模型在反事实诊断中对统计捷径的依赖程度（定势效应）
- **摘要**: MedEinst 是一个针对医疗大模型‘定势效应’（Einstellung Effect）的反事实基准，包含 5,383 对临床病例，覆盖 49 种疾病。每对由对照病例和陷阱病例组成，陷阱病例通过改变关键鉴别证据使诊断翻转，用于检测模型是否依赖统计捷径而非患者特异性证据。作者提出 Bias Trap Rate 指标，即正确诊断对照但误诊陷阱的概率，以量化定势易感性。评测发现前沿模型在常规基准上准确率高，但 Bias Trap Rate 严重，表明该失败模式普遍存在。论文还提出 ECR-Agent 方法，通过动态因果推理和批评驱动的图记忆进化来缓解该问题，但基准本身的方法学贡献是核心。
- **为什么值得看**: 该基准针对现有医疗评测的构念覆盖缺口，提供了可复用的反事实病例构造流程和 Bias Trap Rate 指标，能揭示模型在典型病例上的高分可能掩盖对非典型病例的脆弱性，对评测效度分析有直接价值。
- **关键技术**: `counterfactual benchmark construction`, `bias trap rate`, `paired case design`, `evidence audit`, `dynamic causal inference`
