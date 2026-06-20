# J. Econometrics  ·  2026-06-21

- 共 1 篇 · Journal of Econometrics

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期仅含一篇论文，整体主线聚焦于**因果识别与政策评估中的不对称效应**，具体通过分位数回归与结构性向量自回归（VAR）的贝叶斯融合来展开。

在因果识别与不对称效应这条主线上，本期推进的是对政策冲击异质性影响的刻画，核心工具是Bayesian structural quantile VAR。传统均值回归或对称脉冲响应难以捕捉宏观结果分布的偏度变化，该文通过分位数脉冲响应函数，将结构性识别嵌入贝叶斯框架，从而在显式损失函数下评估政策干预的收益-成本权衡，定义了下行风险与上行潜力的不对称度量。

对因果推断与半参数效率方向的研究者而言，这篇“Bayesian structural quantile VAR”将分位数回归的结构性识别用于不对称因果效应分析，提供了有别于均值框架的分布异质性视角，适合优先阅读。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106230](https://doi.org/10.1016/j.jeconom.2026.106230) — Macro-prudential policy under asymmetric risks: A Bayesian structural quantile VAR approach
- **作者**: Sulkhan Chavleishvili, Robert F. Engle, Stephan Fahr, Manfred Kremer, Frederik Lund-Thomsen, Simone Manganelli et al.
- **期刊/来源**: Journal of Econometrics
- **机构**: Aarhus University · European Central Bank · Danmarks Nationalbank
- **分类**: pp 106230
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在宏观审慎政策设定下，研究目标是定义下行风险与上行潜力的不对称度量，并在显式损失函数下评估政策干预的收益-成本权衡。核心方法是提出 Bayesian structural quantile VAR 模型，通过分位数脉冲响应函数刻画政策冲击对预测分布不同分位数的异质影响，从而捕捉宏观结果分布的不对称性与偏度变化。模型在贝叶斯框架下对分位数 VAR 施加结构性识别，提供灵活且可能不对称的预测分布。实证表明宏观审慎政策可降低增长波动与负偏度，并刻画了政策干预有利的经济状态条件。对您可能有用：本文将分位数回归与结构性 VAR 结合用于政策评估，为经济理论中的不对称因果效应分析提供了新视角。
- **关键技术**: `Bayesian structural quantile VAR`, `quantile impulse response function`, `asymmetric predictive distribution`, `macro-prudential loss function`, `downside risk and upside potential measures`
- **为什么对您有用**: 本文连接到经济理论中的因果推断与政策评估子方向，用分位数 VAR 做结构性冲击识别，实质是在分布的不同分位数上做异质性因果效应估计。您武器库中的 semiparametric theory 与 M-estimation theory 可以攻这篇 paper 的口子：它对分位数 VAR 的贝叶斯推断缺乏效率理论分析，用 semiparametric efficiency bound 视角可以审视其估计是否达到最优率，或用 M-estimation 理论严格推导其渐近性质。Follow-up 粗判：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立分位数结构性 VAR 的严格渐近与效率理论。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

