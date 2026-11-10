# AAAI 2026 · RAG / 长上下文

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. Inference Scaling Law for Retrieval Augmented Generation
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/38692) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/38692/42654)
- **作者**: Shu Zhou, Yuxuan Ao, Yunyang Xuan, Xin Wang, Tao Fan, Hao Wang
- **会议/来源**: AAAI 2026 · Track 19
- 相关性 8/10 · `analysis`
- **测什么**: RAG推理性能随检索器规模、生成器规模、文档数和上下文长度的缩放规律
- **摘要**: 本文系统研究检索增强生成（RAG）在推理阶段的缩放规律，考察检索器规模、生成器规模、检索文档数和上下文窗口长度四个因素对性能的影响。基于多个基准数据集的大量实验，作者发现性能与这些因素间存在幂律和S型关系，并构建了带理论依据的联合推理缩放定律。该定律可用于预测不同计算资源下RAG模型的性能趋势，为高效部署提供指导。方法学贡献在于将缩放定律从训练阶段拓展到推理阶段，并给出了可验证的定量关系。
- **为什么值得看**: 为RAG评测提供了预测性框架，可帮助研究者理解资源投入与性能增益的边际效应，对评测中的资源分配和实验设计有方法学参考价值。
- **关键技术**: `scaling law`, `power-law fitting`, `sigmoid fitting`, `joint scaling model`
