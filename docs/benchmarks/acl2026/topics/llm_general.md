# ACL 2026 · 通用能力评测

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. AdvancedIF: Rubric-Based Benchmarking and Reinforcement Learning for Advancing LLM Instruction Following
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.820/) · [PDF](https://aclanthology.org/2026.acl-long.820.pdf)
- **作者**: Yun He, Wenzhe Li, Hejia Zhang, Songlin Li, Karishma Mandyam, Sopan Khosla, Yuanhao Xiong, Nanshu Wang et al.
- **会议/来源**: ACL 2026 · Long
- 相关性 8/10 · `benchmark`
- **测什么**: 复杂、多轮及系统级指令遵循能力
- **摘要**: AdvancedIF 是一个针对复杂、多轮及系统级指令遵循能力的评测基准，包含 1,600 余条提示词，并配有专家撰写的评分细则（rubrics）。该基准旨在弥补现有指令遵循评测在复杂场景下的不足，并开源了评测脚本。论文还提出 RIFL 后训练流程，利用 rubric 生成、微调的 rubric 验证器和奖励塑形来强化学习，在 AdvancedIF 上取得 6.7% 的绝对提升，并在公开基准上表现优异。消融实验验证了各组件有效性。该工作将 rubric 作为训练与评测的统一工具，为高级指令遵循提供了可解释的奖励信号。
- **为什么值得看**: 该工作将评分细则（rubric）作为评测的核心构件，提供了可解释、可验证的评测信号，并公开了评测脚本，有助于提升评测的透明度和可复现性；同时，其验证器与人类标注的一致性分析对 LLM-as-judge 方法有参考价值。
- **关键技术**: `rubric-based evaluation`, `expert-annotated rubrics`, `rubric verifier`, `reward shaping`, `reinforcement learning`
