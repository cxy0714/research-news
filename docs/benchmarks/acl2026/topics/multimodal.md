# ACL 2026 · 多模态评测

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. Macaron: Controlled, Human-Written Benchmark for Multilingual and Multicultural Reasoning via Template-Filling
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.2211/) · [PDF](https://aclanthology.org/2026.acl-long.2211.pdf)
- **作者**: Alaa Elsetohy, Sama Hadhoud, Haryo Akbarianto Wibowo, Chenxi Whitehouse, Genta Indra Winata, Fajri Koto, Alham Fikri Aji
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 多语言多文化背景下不同推理类型（如数学、计数）的推理能力，以及语言间性能差距。
- **摘要**: Macaron 是一个模板优先的多语言多文化推理基准，通过 100 个语言无关模板分解推理类型（7 种）和文化方面（22 种），由母语标注者生成英文和本地语言的选择题及系统推导的真假题。数据集包含 11,862 个实例，覆盖 20 个国家/文化背景、10 种文字和 20 种语言（含阿姆哈拉语、约鲁巴语、祖鲁语、吉尔吉斯语等低资源语言）。零样本评估 21 个多语言 LLM，推理模式模型表现最佳（总体 80.8%），英文与本地语言差距小（ΔMC = -1.3%），而开放权重模型在本地语言上显著下降（ΔMC = -6.8%），且在真假题上常接近随机。文化相关的数学和计数模板最难。该基准通过模板填充控制推理类型和文化方面，避免了翻译数据集的英语中心偏差，并提供了系统化的真假题生成方法。
- **为什么值得看**: 该论文展示了如何通过模板填充实现推理类型和文化方面的因子化设计，从而控制构念覆盖并减少语言偏差，为多语言评测提供了可复用的构造方法；同时报告了模型在本地语言上的性能退化，揭示了现有基准可能高估多语言能力。
- **关键技术**: `template-based construction`, `factorized design`, `native annotators`, `multilingual evaluation`, `zero-shot evaluation`
