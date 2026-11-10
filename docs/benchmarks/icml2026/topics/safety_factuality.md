# ICML 2026 · 安全 / 事实性

> 本页 1 篇（该主题共 1 篇），按相关性排序。 [返回总览](../index.md)

### 1. A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness
- **链接**: [论文页](https://proceedings.mlr.press/v306/schwinn26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/schwinn26a/schwinn26a.pdf) · [OpenReview](https://openreview.net/forum?id=RgnoWsmYBM)
- **作者**: Leo Schwinn, Moritz Ladenburger, Tim Beyer, Mehrnaz Mofakhami, Gauthier Gidel, Stephan Günnemann
- **会议/来源**: ICML 2026 · Main
- 相关性 9/10 · `meta_evaluation`
- **测什么**: LLM-as-judge在红队攻击下评估有害性的可靠性（与人类标签的一致性）。
- **摘要**: 本文系统审计了LLM-as-judge在红队安全评测中的可靠性，发现现有验证协议未考虑红队场景固有的分布偏移：不同受害模型的生成风格、攻击对输出模式的扭曲、以及越狱场景的语义模糊性，导致judge性能在6642个人工验证标签上常降至接近随机水平，与先前报告的高人类一致性形成鲜明对比。作者进一步指出，许多攻击通过利用judge的缺陷而非真正诱导有害内容来虚增成功率。为此，他们提出ReliableBench（一组更稳定可判的行为基准）和JudgeStressTest（暴露judge失败的数据集），以支持更可靠的评测。
- **为什么值得看**: 该研究揭示了LLM-as-judge在分布偏移下信度崩塌的问题，并提供了可复用的压力测试数据集和基准，对评测方法学中judge验证与污染控制具有直接价值。
- **关键技术**: `LLM-as-judge`, `human-verified labels`, `distribution shift audit`, `adversarial robustness`, `benchmark construction`
