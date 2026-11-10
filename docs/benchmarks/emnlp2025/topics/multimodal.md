# EMNLP 2025 · 多模态评测

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. ClimateViz: A Benchmark for Statistical Reasoning and Fact Verification on Scientific Charts
- **链接**: [论文页](https://aclanthology.org/2025.emnlp-main.1196/) · [PDF](https://aclanthology.org/2025.emnlp-main.1196.pdf)
- **作者**: Ruiran Su, Jiasheng Si, Zhijiang Guo, Janet B. Pierrehumbert
- **会议/来源**: EMNLP 2025 · Main
- 相关性 8/10 · `benchmark`
- **测什么**: 多模态模型在科学图表上进行统计推理和事实核查的能力（支持/反驳/信息不足）。
- **摘要**: ClimateViz 是首个面向科学图表的事实核查基准，包含 49,862 条声明与 2,896 张可视化图表，每条标注为支持、反驳或信息不足，并附带结构化知识图谱解释，涵盖统计模式、时间趋势、空间比较和因果关系。该基准基于真实世界、专家策展的科学图表，旨在评估多模态大模型在图表上的统计推理与事实核查能力。作者对多种专有和开源多模态模型进行了零样本和少样本评估，结果显示当前模型表现远低于人类水平（最佳模型如 Gemini 2.5 和 InternVL 2.5 的准确率仅 76.2–77.8%，而人类为 89.3–92.7%）。少样本提示提升有限，但解释增强输出显著提升了部分闭源模型（如 o3 和 Gemini 2.5）的性能。该基准提供了可复用的标注流程和知识图谱解释，为图表事实核查评测提供了新范式。
- **为什么值得看**: 该基准引入了结构化知识图谱解释作为可解释的验证依据，并提供了人类基线（89.3–92.7%）与模型性能的对比，揭示了多模态模型在统计推理上的显著差距，为评测图表理解能力提供了新的构念覆盖和难度校准参考。
- **关键技术**: `benchmark construction`, `knowledge graph explanations`, `human baseline`, `zero-shot and few-shot evaluation`, `explanation-augmented prompting`
