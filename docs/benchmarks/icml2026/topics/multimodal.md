# ICML 2026 · 多模态评测

> 本页 2 篇（该主题共 2 篇），按相关性排序。 [返回总览](../index.md)

### 1. Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling
- **链接**: [论文页](https://proceedings.mlr.press/v306/park26c.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/park26c/park26c.pdf) · [OpenReview](https://openreview.net/forum?id=tbqxbGMFUV)
- **作者**: Seojeong Park, Jiho Choi, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `evaluation_method`
- **测什么**: 多模态评测模型在视觉与文本冲突时对感知正确性的判断能力及排序一致性。
- **摘要**: 该论文针对多模态大模型作为评测者时，在视觉证据与文本线索冲突时倾向于奖励看似合理叙述而非感知正确回答的“感知判断偏差”问题。作者通过受控视觉扰动系统分析了这一现象，并构建了感知扰动判断数据集，包含最小编辑的反事实响应以隔离感知错误并提供可验证监督。基于该数据集，他们提出统一训练框架，结合结构化GRPO奖励与批量排序目标，无需显式成对标签即可实现全局一致排序。实验在多个多模态评测基准上显示，该方法显著提升了感知保真度、排序一致性与人类评估对齐度。该工作为训练感知接地、可解释且对视觉-推理冲突鲁棒的多模态评测者提供了可扩展路径。
- **为什么值得看**: 该论文为LLM-as-judge的验证提供了具体方法学贡献：通过受控扰动构造反事实样本，量化并缓解评测者的感知偏差，并展示了如何用可验证监督训练更可靠的评测模型，对评测方法学中的judge验证与偏差控制有直接参考价值。
- **关键技术**: `counterfactual perturbation`, `LLM-as-judge`, `reward modeling`, `GRPO`, `batch ranking`

### 2. MMBench-Live: A Continuously Evolving Benchmark for Multimodal Models
- **链接**: [论文页](https://proceedings.mlr.press/v306/liu26gk.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26gk/liu26gk.pdf) · [OpenReview](https://openreview.net/forum?id=qvjszj58jT)
- **作者**: Yuanzhi Liu, Shousheng Zhao, Bo Zhou, Kongming Liang, Zhanyu Ma
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `benchmark`
- **测什么**: 多模态模型在持续演化数据上的视觉-语言理解能力及抗污染鲁棒性
- **摘要**: MMBench-Live 提出一个由多智能体驱动的自动化流水线，用于构建持续演化的多模态评测基准，以解决静态基准的时效性、污染和维护成本问题。它从 MMBench 实例化，生成 5.9K 个新评测实例，每次更新成本约 30 美元、耗时 1-2 小时。方法包括结构化基准规范、反馈控制的实时数据采集、可验证的 QA 生成（含可执行推理），以及分布一致的更新策略，从原基准提取任务相关视觉模式以指导数据收集和过滤。实验表明，MMBench-Live 保持稳定的模型排名、与原基准语义对齐，并表现出更弱的污染相关记忆信号。该工作为可持续的多模态基准演化提供了实用且可扩展的范式。
- **为什么值得看**: 该论文直接回应了基准污染和静态基准饱和问题，提出了一种可复用的自动化更新流程，并验证了跨版本可比性（排名稳定性、语义对齐），对评测方法学有具体贡献。
- **关键技术**: `multi-agent pipeline`, `distribution-consistent update`, `contamination audit`, `ranking stability analysis`, `semantic alignment`
