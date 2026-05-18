# J. Econometrics — Vol 256  ·  2026-05-18

- 共 2 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106254](https://doi.org/10.1016/j.jeconom.2026.106254) — Bounding treatment effects by pooling limited information across observations
- **作者**: Sokbae Lee, Martin Weidner
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106254
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在无混淆假设下，针对高维协变量或重叠性被破坏的困难情境，本文提出了对受处理者平均处理效应（ATT）的新型稳健边界识别与估计方法。核心机制是通过跨观测值的“有限信息池化”实现稳健性：将边界构造为观测结果的样本平均，且每个结果的贡献仅依赖于有限数量观测的处理状态。无池化退化为 Manski 边界，无限池化退化为标准逆概率加权（IPW），本文探索了两者之间的中间连续谱。作者针对该部分识别框架提供了相应的推断方法。模拟与两项实证应用表明该边界兼具稳健性与信息量。对您有用：该工作为处理倾向得分重叠性破坏下的因果识别提供了新视角，其有限池化思想与半参数效率理论中 IPW 的极端性质形成对比，对您在因果推断识别与敏感性分析方向的研究有直接启发。
- **关键技术**: `partial identification`, `overlap violation`, `inverse propensity score weighting`, `Manski bounds`, `limited information pooling`, `inference for bounds`
- **为什么对您有用**: 直接关联因果推断中的识别与估计问题，特别是处理倾向得分重叠性破坏（overlap violation）这一常见痛点；有限池化的思想为 IPW 和 Manski 边界提供了连续谱视角，对研究半参数效率与敏感性分析有理论启发。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106264](https://doi.org/10.1016/j.jeconom.2026.106264) — A kernelization-based approach to nonparametric binary choice models
- **作者**: Guo Yan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106264
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在非参数二元选择模型设定下，目标是估计未知的协变量系统函数与误差分布，传统 sieve 方法在中等维协变量下会引发高维优化计算瓶颈。本文提出一种基于核化的估计器，将再生核希尔伯特空间（RKHS）视为特殊 sieve 空间，并耦合谱截断正则化（spectral cut-off）实现降维，从而在协变量维度增加时保持计算可扩展性。理论上，本文证明了该 RKHS sieve 估计器的相合性，以及加权平均偏导数（weighted average partial derivatives）plug-in 估计器的渐近正态性。模拟表明该方法在模型误设下有效改善有限样本表现，且正确设定时效率损失轻微；实证重新检验了美国庇护法庭裁决中室外温度对法官“情绪”及判决的效应。对您有用：该文将 RKHS sieve 与谱截断结合解决计算瓶颈，并推导了功能参数的渐近正态性，直接契合您在半/非参数理论与统计计算方面的兴趣，且实证部分涉及经济因果应用。
- **关键技术**: `RKHS sieve estimation`, `spectral cut-off regularization`, `asymptotic normality of plug-in estimator`, `weighted average partial derivatives`, `nonparametric binary choice`
- **为什么对您有用**: 该文将 RKHS 视为 sieve 空间并引入谱截断正则化以解决计算可扩展性，直接契合您在半/非参数理论与统计计算方面的核心兴趣；同时，其对加权平均偏导数 plug-in 估计的渐近正态性推导与效率理论相关，且实证部分涉及经济理论中的因果推断应用。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

