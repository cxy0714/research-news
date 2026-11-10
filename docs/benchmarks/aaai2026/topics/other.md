# AAAI 2026 · 其他

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. Measuring What Matters: Scenario-Driven Evaluation for Trajectory Predictors in Autonomous Driving
- **链接**: [论文页](https://ojs.aaai.org/index.php/AAAI/article/view/36978) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/36978/40940)
- **作者**: Longchao Da, David Isele, Hua Wei, Manish Saroya
- **会议/来源**: AAAI 2026 · Track 1
- 相关性 8/10 · `evaluation_method`
- **测什么**: 轨迹预测器在关键场景下的精度与多样性综合表现，及其对自车驾驶性能的贡献
- **摘要**: 本文针对自动驾驶轨迹预测器的评测提出场景驱动（scenario-driven）的评估流程，主张传统误差指标（ADE/FDE）仅反映事后精度，忽略预测器对自车（SDV）决策的实际影响，尤其在复杂交互场景中，预测器应同时捕捉邻车所有可能运动方向以支持谨慎决策。作者基于场景关键性（criticality）动态组合精度与多样性两个维度，生成最终评分；在真实世界数据集的闭环基准上实验，显示该流程比传统指标更能反映预测器评估与自车驾驶性能的相关性。方法学贡献在于将评测从单一误差转向多维度、场景自适应的综合评分，并验证了其与下游驾驶性能的关联。
- **为什么值得看**: 该论文提出了一种新的评测维度组合方式（精度+多样性，按场景关键性动态加权），并验证了评测分数与下游任务性能的相关性，对评测效度（construct validity）有直接贡献，可作为任务特定评测方法学的参考。
- **关键技术**: `scenario-driven evaluation`, `adaptive weighting`, `closed-loop benchmark`, `accuracy-diversity tradeoff`, `construct validity`
