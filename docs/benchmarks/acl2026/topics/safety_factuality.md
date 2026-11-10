# ACL 2026 · 安全 / 事实性

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking
- **链接**: [论文页](https://aclanthology.org/2026.acl-long.1948/) · [PDF](https://aclanthology.org/2026.acl-long.1948.pdf)
- **作者**: Mark Rothermel, Marcus Kornmann, Marcus Rohrbach, Anna Rohrbach
- **会议/来源**: ACL 2026 · Long
- 相关性 9/10 · `benchmark`
- **测什么**: 多模态声明的事实核查准确性，包括跨语言和跨模态的裁决一致性。
- **摘要**: VeriTaS 是首个面向多模态自动事实核查（AFC）的动态基准，旨在抵御大模型预训练导致的数据泄漏。它包含来自 104 家专业事实核查机构、覆盖 54 种语言的 25,000 条真实声明，涵盖文本和音视频内容。基准通过全自动七阶段流水线每季度更新，该流水线标准化声明表述、检索原始媒体，并将专家裁决映射到一种新颖的、标准化的、解耦的评分方案，附有文本理由。人工评估表明自动标注与人类判断高度一致。该基准通过持续更新来保持抗泄漏性，为 AFC 评测提供了更可靠的测量工具。
- **为什么值得看**: 该论文直接回应了静态基准的污染问题，提出了一个可复用的动态更新流程，并验证了自动标注与人类判断的一致性，对评测方法学中的泄漏控制和标注可靠性具有参考价值。
- **关键技术**: `dynamic benchmark`, `contamination audit`, `human evaluation`, `automated annotation pipeline`, `multi-modal fact-checking`
