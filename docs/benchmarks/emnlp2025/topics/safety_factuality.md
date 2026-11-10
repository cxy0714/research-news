# EMNLP 2025 · 安全 / 事实性

> 本页 2 篇（该主题共 2 篇），按相关性排序。 [返回总览](../index.md)

### 1. The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1761/) · [PDF](https://aclanthology.org/2025.emnlp-main.1761.pdf)
- **作者**: Denis Janiak, Jakub Binkowski, Albert Sawczyn, Bogdan Gabrys, Ravid Shwartz-Ziv, Tomasz Jan Kajdanowicz
- **会议/来源**: EMNLP 2025 · Main
- 相关性 9/10 · `meta_evaluation`
- **测什么**: 幻觉检测方法在人类对齐指标下的真实性能，以及评测指标（ROUGE）的效度。
- **摘要**: 该论文重新评估了LLM幻觉检测方法的评测方式，指出广泛使用的ROUGE指标基于词法重叠，与人类判断不一致。通过人类研究，作者发现ROUGE虽然召回率高，但精确度极低，导致对检测方法性能的高估；改用LLM-as-Judge等语义对齐指标后，若干既有检测方法的性能下降高达45.9%。此外，基于响应长度的简单启发式方法竟能与复杂检测技术匹敌，暴露了当前评测实践的根本缺陷。论文主张采用语义感知且稳健的评测框架，以准确衡量幻觉检测的真实性能。
- **为什么值得看**: 该研究提供了对评测指标（ROUGE）效度的系统性验证，通过人类基线对比揭示了指标偏差，并量化了LLM-as-Judge与人类判断的一致性，对评测方法学有直接贡献。
- **关键技术**: `human study`, `LLM-as-judge`, `metric validation`, `baseline comparison`

### 2. A Fully Probabilistic Perspective on Large Language Model Unlearning: Evaluation and Optimization
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.452/) · [PDF](https://aclanthology.org/2025.emnlp-main.452.pdf)
- **作者**: Anda Cheng, Wei Huang, Yinggui Wang
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `evaluation_method`
- **测什么**: 大模型遗忘后对语义相似输入的信息泄露风险（概率化度量）
- **摘要**: 本文提出一个全概率评估框架（FPE）用于大模型遗忘（LLMU），针对现有确定性评估过于乐观的问题。FPE 通过输入分布采样（IDS）生成语义相似但多样的输入，并对每个输入进行多次采样，从而获得概率化的信息泄露风险度量。作者还提出对比嵌入损失（CEL）改进遗忘效果，通过对比学习拉远遗忘样本与对比样本的表示，同时对齐随机向量。实验在 Llama-2-7B 上显示 FPE 能发现更多泄露风险，CEL 将遗忘效果提升至少 50.1%，鲁棒性提升至少 37.2%，同时保持模型效用。该工作为遗忘评估提供了概率化视角，但未涉及人类基线或污染检查。
- **为什么值得看**: 该工作挑战了确定性评估的乐观偏差，提出概率化评估框架，为测量信息泄露风险提供了更严格的方法，对评测方法学有直接贡献。
- **关键技术**: `probabilistic evaluation`, `input distribution sampling`, `contrastive learning`, `unlearning robustness`
