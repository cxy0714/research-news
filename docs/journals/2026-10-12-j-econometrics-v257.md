# J. Econometrics — Vol 257  ·  2026-10-12

- 共 4 篇 · Journal of Econometrics
- 目录核对 ⚠️ 疑似漏 20 篇（对照 OpenAlex 24 篇）：10.1016/j.jeconom.2024.105926、10.1016/j.jeconom.2026.106301、10.1016/j.jeconom.2026.106298、10.1016/j.jeconom.2023.105558、10.1016/j.jeconom.2024.105731 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期共四篇论文，主线清晰：两篇聚焦因果推断中的识别与估计（LATE 的高维稳健推断、百分比点 ATE 的异质性偏差修正），两篇分别落在假设检验的空间推广与功效敏感性分析。整体上，方法工具以半参数框架、去偏机器学习、局部最优不变检验和去卷积估计为主，且均强调有限样本性质与实证可操作性。

因果推断主线最突出。Identification-robust inference for the LATE with high-dimensional covariates 处理高维协变量下弱识别与 LATE 推断的冲突，通过 DML 估计 nuisance 参数，构造均匀尺寸正确的检验统计量，并在模拟中展示对传统方法的优势；其应用部分报告置信区间缩短 49%–92%，直接回应了高维因果推断中识别稳健性与效率的权衡。另一篇 Estimation and inference on average treatment effect in percentage points under heterogeneity 则从半对数回归的 Jensen 偏差切入，提出加权子组 estimand 作为百分比点 ATE 的下界，在异质性处理效应下给出可解释的替代度量，并建立半参数大样本理论。两篇互补：前者关注推断的稳健性，后者关注 estimand 的定义与偏差修正，均与半参数效率理论紧密相关。

假设检验主线包含两篇。Testing coefficient stability in spatial regression 将 Nyblom 时间序列系数稳定性检验推广至空间回归，基于局部最优不变检验的近似构造统计量，允许回归元与误差空间相关，覆盖多种持久性系数变化模式；其技术核心是渐近分布推导与功效优化，适合空间计量背景的检验问题。Testing for underpowered literatures 则转向功效的元分析视角，提出去卷积估计量以反事实评估样本量增大对显著结果数量的影响，调整发表偏倚且不假设效应分布形状，应用于经济学 RCT 后发现样本量加倍仅提升功效 7.2 个百分点，结论指向实验设计而非单纯扩容。两篇虽主题不同，但均以检验统计量的构造与渐近性质为核心，前者侧重空间结构，后者侧重发表偏倚下的功效校准。

若按主题优先阅读：因果推断方向建议先看 LATE 高维稳健推断与百分比点 ATE 两篇，前者涉及高维与弱识别下的推断理论，后者连接半参数估计与异质性处理效应；假设检验方向可关注空间系数稳定性检验（检验理论的空间推广）与功效去卷积（发表偏倚下的功效分析），后者对实证研究设计有直接参考价值。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1016/j.jeconom.2026.106302](https://doi.org/10.1016/j.jeconom.2026.106302) · [arXiv](https://arxiv.org/abs/2302.09756) — Identification-robust inference for the LATE with high-dimensional covariates
- **作者**: Yukun Ma
- **期刊/来源**: Journal of Econometrics
- **机构**: University of Rochester
- **分类**: vol 257 · pp 106302
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究高维协变量下局部平均处理效应（LATE）的识别稳健推断，不依赖识别强度假设。作者提出一种新的检验统计量，并证明其在均匀意义下具有正确的渐近尺寸。通过双重/去偏机器学习（DML）估计 nuisance 参数，开发了易于实现的推断和置信区间算法。模拟表明，该方法在弱识别和高维情形下均能控制尺寸并保持功效，优于传统检验。应用于铁路与人口数据，估计的铁路效应系数更小，置信区间比传统结果缩短 49% 至 92%。
- **关键技术**: `double/debiased machine learning`, `uniform inference`, `weak identification`, `high-dimensional covariates`, `LATE`
- **为什么对您有用**: 直接关联因果推断中的工具变量与弱识别问题，且结合了高维统计与 DML 方法。可用您非常熟悉的估计理论（如 semiparametric efficiency）来审视其均匀尺寸性质，中期可做：需在 moderately_familiar 的 semiparametric theory 上巩固以深入理解其正交性条件。

### 2. [10.1016/j.jeconom.2026.106303](https://doi.org/10.1016/j.jeconom.2026.106303) · [arXiv](https://arxiv.org/abs/2408.06624) — Estimation and inference on average treatment effect in percentage points under heterogeneity
- **作者**: Ying Zeng
- **期刊/来源**: Journal of Econometrics
- **机构**: Xiamen University
- **分类**: vol 257 · pp 106303
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文关注半对数回归中处理效应系数作为百分比点平均处理效应（ATE）近似时的偏差问题，指出在异质性处理效应下，由于 Jensen 不等式，该近似存在系统性偏差，尤其在 log 结果变量的双重差分和交错采用设计中更为突出。作者提出一个新的 estimand，通过对可观测子组进行加权，在组内同质性假设下等于百分比点 ATE，否则为其下界，从而改进传统度量。估计方法基于半参数框架，建立大样本性质（一致性、渐近正态性），并通过蒙特卡洛实验展示异质性较大时传统与提议度量的显著差异。两个实证应用进一步说明方法的实用性。对您而言，该文连接了因果推断中 ATE 估计与半参数效率理论，其下界估计量的构造思路可借鉴到您的 proximal CI 或纵向设定中的敏感性分析。
- **关键技术**: `semi-logarithmic regression`, `difference-in-differences`, `Jensen's inequality`, `semiparametric estimation`, `asymptotic normality`, `Monte Carlo simulation`
- **为什么对您有用**: 该文直接关联您的因果推断兴趣，特别是处理效应异质性下的 ATE 识别与估计，以及半参数方法。您可以用 very_familiar 的非参数统计和 minimax 工具分析其下界估计量的最优性，或用 moderately_familiar 的半参数理论检验其效率界。中期可做：若想扩展至更复杂异质性结构，需在 identification theory 上加强。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1016/j.jeconom.2026.106309](https://doi.org/10.1016/j.jeconom.2026.106309) — Testing coefficient stability in spatial regression
- **作者**: Ulrich K. Müller, Mark W. Watson
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 257 · pp 106309
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在空间回归框架下提出检验系数稳定性的新方法，目标是检测回归系数随空间位置变化的备择假设。该方法基于局部最优不变检验（locally best invariant test）的近似，适用于高斯回归模型且系数变化具有鞅结构的情形，是 Nyblom (1989) 时间序列系数稳定性检验的空间推广。检验对多种持久性系数变化模式具有良好功效，并允许回归元和误差存在空间相关，适用于广泛的空间设计。技术核心在于构造检验统计量并推导其渐近分布，通过近似局部最优不变检验实现功效优化。模拟和实证研究表明该方法在有限样本下表现良好。对您而言，该检验的构造思路与您熟悉的假设检验理论直接相关，且其空间推广框架可能启发您在高维或非参数设定下设计类似检验。
- **关键技术**: `locally best invariant test`, `spatial regression`, `coefficient stability test`, `martingale approximation`, `Gaussian likelihood`
- **为什么对您有用**: 本文属于假设检验方向，直接对应您的主要兴趣之一。其局部最优不变检验的构造与您熟悉的效率理论（如 semiparametric efficiency bounds）有相通之处，您可以用 very_familiar 的 minimax 和渐近理论工具来审视其最优性。中期可做：若想推广到非参数或高维空间设定，需在 moderately_familiar 的 semiparametric theory 上进一步打磨。

### 2. [10.1016/j.jeconom.2026.106312](https://doi.org/10.1016/j.jeconom.2026.106312) · [arXiv](https://arxiv.org/abs/2406.13122) — Testing for underpowered literatures
- **作者**: Stefan Faridani
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 257 · pp 106312
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究如何估计一组实验在样本量反事实增大时，其统计显著结果数量的期望变化，即检验功效的敏感性分析。作者提出一种去卷积估计量，该估计量渐近正态，并调整了发表偏倚，且不要求对真实处理效应的分布作任何假设，允许存在点质量。模拟显示即使t分数仅近似正态，覆盖也良好。应用于经济学期刊发表的随机对照试验（RCTs），发现样本量加倍平均使t检验功效提高7.2个百分点，且该效应小于非RCTs，与实验室心理学的系统复制相当。结论是RCTs对样本量增加相对不敏感，资助者应更多考虑提高测量质量和实验设计而非单纯扩大样本。对您而言，该去卷积方法为功效分析提供了新视角，与您对假设检验和因果推断中功效问题的兴趣相关。
- **关键技术**: `deconvolution estimator`, `publication bias adjustment`, `asymptotic normality`, `power analysis`, `counterfactual sample size`
- **为什么对您有用**: 本文属于假设检验领域，直接关联您对功效和检验行为的兴趣。其去卷积估计方法可迁移到因果推断中的敏感性分析，例如评估未观测混杂对结论稳健性的影响。您可运用非常熟悉的非参数统计和M估计理论来审视该估计量的渐近性质，中期可探索将其扩展到更复杂的因果设定（如工具变量或纵向数据）中的功效分析。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

