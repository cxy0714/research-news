# J. Econometrics — Vol 240  Issue 1  ·  2026-05-21

- 共 6 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105680](https://doi.org/10.1016/j.jeconom.2024.105680) — A computational approach to identification of treatment effects for policy evaluation
- **作者**: Sukjin Han, Shenshen Yang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 240 · issue 1 · pp 105680
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在仅有二元工具变量（IV）的设定下，本文研究如何将局部平均处理效应（LATE）外推至不同反事实政策环境，以解决其外部有效性不足的问题。作者提出一种计算框架，系统性地求解以边际处理效应（MTE）加权平均定义的各类政策相关处理参数的 sharp nonparametric bounds。该框架突破了既有文献对 MTE 的形状约束，能够灵活纳入 IV 的统计独立性（而非仅均值独立性）及其他多种识别假设。核心机制是将非参数识别问题转化为可计算的约束优化问题，从而推导出识别域。理论上获得了比以往更紧的识别界，实证分析应用于医疗保险对医疗服务利用的影响。对您有用：本文将因果识别问题转化为计算优化的思路，以及利用统计独立性放松假设的切入点，对您在 IV 外推与因果识别边界（primary: causal inference/identification）的研究具有直接参考价值。
- **关键技术**: `sharp nonparametric bounds`, `marginal treatment effect (MTE)`, `instrumental variable extrapolation`, `statistical independence`, `computational identification`
- **为什么对您有用**: 直接对应您 primary interest 中的因果推断（IV、identification），本文将识别问题转化为计算约束优化的思路，以及利用统计独立性放松假设的方法，对处理 IV 外推和敏感性分析有直接启发；同时应用部分契合您 secondary interest 中的经济理论与流行病学因果应用。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1016/j.jeconom.2023.105647](https://doi.org/10.1016/j.jeconom.2023.105647) — Locally robust inference for non-Gaussian linear simultaneous equations models
- **作者**: Adam Lee, Geert Mesters
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 240 · issue 1 · pp 105647
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在线性联立方程模型（SEM）中，若结构冲击独立且至多一个为高斯分布，则所有参数可识别，但现有方法在真实分布接近高斯时（弱非高斯性）存在严重的水平扭曲问题。本文提出一种局部稳健（locally robust）的半参数推断方法，通过构建对冲击分布 nuisance 参数正交的得分函数，有效缓解了弱非高斯性导致的识别弱化问题。该方法在实现 n^{-1/2}-CAN 推断的同时，保证了在分布接近高斯边界时的覆盖率，且计算简便。大量模拟和学校教育回报率的实证表明该方法在修正水平扭曲的同时保持了良好的功效。对您有用：该文将 Neyman 正交性/局部稳健技术应用于非高斯 SEM 的弱识别问题，直接契合您在半参数效率理论与因果推断（IV/SEM）交叉领域的兴趣，为处理弱识别下的半参数假设检验提供了可迁移的框架。
- **关键技术**: `locally robust inference`, `Neyman orthogonal score`, `semi-parametric efficiency`, `independent component analysis`, `weak identification`
- **为什么对您有用**: 将 Neyman 正交性/局部稳健得分应用于非高斯 SEM 的弱识别推断，直接契合您在半参数效率理论、因果推断（IV/SEM）与假设检验的交叉兴趣，为弱识别下的稳健推断提供了可迁移的理论框架。

### 2. [10.1016/j.jeconom.2024.105689](https://doi.org/10.1016/j.jeconom.2024.105689) — Non-representative sampled networks: Estimation of network structural properties by weighting
- **作者**: Chih-Sheng Hsieh, Yu-Chin Hsu, Stanley I.M. Ko, Jaromír Kovářík, Trevon D. Logan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 240 · issue 1 · pp 105689
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在网络数据存在非代表性抽样（节点缺失概率依子群而异）的设定下，本文研究网络结构特征（如度分布等）的估计问题，指出非随机缺失会导致非经典测量误差与系统性偏差。作者提出一种基于加权（类似 Horvitz-Thompson/IPW）的估计方法，以恢复网络级统计量并修正偏差。该方法的核心优势在于无需假设特定的网络生成模型（半参数设定），且易于实现。理论上，证明了所提加权估计量具有一致性与渐近正态性（CAN），并在有限样本下表现良好。该工作将因果推断中处理选择偏差的加权思想应用于网络缺失数据；对您在因果推断中处理非代表性抽样/缺失数据，以及半参数 CAN 估计量的推导有直接的方法迁移价值。
- **关键技术**: `inverse probability weighting (IPW)`, `non-representative sampling`, `asymptotic normality (CAN)`, `network structural estimation`, `missing data correction`
- **为什么对您有用**: 将因果推断中处理选择偏差的 IPW 加权思想拓展至网络结构估计，对您在因果推断（特别是缺失数据/选择偏差）及半参数 CAN 估计理论方面的研究有直接的方法迁移价值。

## 经济理论 / 应用  *(econ_theory, 3 篇)*

### 1. [10.1016/j.jeconom.2023.105636](https://doi.org/10.1016/j.jeconom.2023.105636) — Likelihood approach to dynamic panel models with interactive effects
- **作者**: Jushan Bai
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 240 · issue 1 · pp 105636
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究带交互效应（因子误差结构）的动态面板模型，在误差项与回归变量相关且个体效应可为固定常数的设定下，同时考虑短面板（T固定）与长面板（T增大）。作者将动态面板视为联立方程组，利用均值与协方差矩阵之间的约束提出 quasi-FIML（准完全信息极大似然）方法。该方法无需估计个体效应，从而规避了横截面维度的 incidental parameters problem（伴随参数问题）。因子过程被视作参数且允许任意动态结构，理论证明在固定或大 T 下估计量无伴随参数偏差，且以 (NT)^{1/2} 的快速收敛率中心化为零。文章进一步分析了 quasi-FIML 估计量的渐近效率，并开发了一个可行且快速的数值计算算法。对您有用：该文在处理高维固定效应/因子结构时规避 incidental parameters problem 的技巧、对 FIML 效率的讨论以及快速计算算法，直接关联您的 efficiency theory、high-dimensional statistics 与 statistical computing 兴趣，且是经济理论中动态面板因果推断的经典设定。
- **关键技术**: `quasi-FIML`, `interactive effects`, `incidental parameters problem`, `simultaneous-equation system`, `asymptotic efficiency`, `dynamic panel data`
- **为什么对您有用**: 直接关联您的 efficiency theory（quasi-FIML 渐近效率）与 high-dimensional statistics（规避 incidental parameters problem），同时其针对交互效应的快速计算算法契合您的 statistical computing 兴趣，且属于经济理论中动态面板因果推断的经典模型。

### 2. [10.1016/j.jeconom.2024.105685](https://doi.org/10.1016/j.jeconom.2024.105685) — Panel data models with time-varying latent group structures
- **作者**: Yiren Wang, Peter C.B. Phillips, Liangjun Su
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 240 · issue 1 · pp 105685
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究带交互固定效应的线性面板模型，设定个体与时间异质性分别由潜在分组结构与未知结构突变刻画，且允许突变前后组数及组员身份不同。估计策略分三步：先通过核范数正则化初步估计再做行列线性回归；基于二分分割思想估计突变点；利用序贯检验K-means算法同时估计潜在分组结构与组数。理论证明突变点、组数和组员身份均能以概率趋于1被正确估计，并建立了斜率系数估计量的渐近分布。蒙特卡洛模拟显示有限样本表现良好，实证分析了美国377个MSA的房价数据。对您有用：核范数正则化在面板交互固定效应中的降维应用，以及序贯检验确定分组数的算法，对高维统计与半参数理论中的潜在结构估计有直接借鉴意义。
- **关键技术**: `nuclear-norm regularization`, `interactive fixed effects`, `binary segmentation`, `sequential testing K-means`, `latent group structure`, `asymptotic distribution`
- **为什么对您有用**: 面板数据中的交互固定效应与潜在分组结构估计，结合了核范数正则化（高维统计）与序贯检验（半参数理论），对您在经济理论应用和高维/半参数方法交叉领域的研究有直接参考价值。

### 3. [10.1016/j.jeconom.2023.105648](https://doi.org/10.1016/j.jeconom.2023.105648) — Cross-section bootstrap for CCE regressions
- **作者**: Ignace De Vos, Ovidijus Stauskas
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 240 · issue 1 · pp 105648
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在因子增强面板数据模型中，当时间序列长度 T 与截面维度 N 可比（TN^{-1}→τ<∞）时，混合 CCE 估计量存在渐近偏差，导致常规推断失效。本文为截面 Bootstrap (CS bootstrap) 在大 N 大 T 设定下的 CCE 估计建立了严格的理论基础。作者证明该重抽样方案不仅能估计标准误，还能有效消除 T/N→τ 引起的偏差，从而实现渐近有效的推断。理论推导进一步涵盖了因子非共同存在以及斜率异质性的情形，使得研究者无需对这些设定做先验强假设。模拟实验验证了上述渐近性质在有限样本下的良好表现。对您有用：该文提出的 Bootstrap 偏差修正机制对您在经济学理论（面板因果推断）和统计计算（重抽样算法）方向的研究有直接借鉴价值。
- **关键技术**: `cross-section bootstrap`, `Common Correlated Effects (CCE)`, `panel data inference`, `bias correction`, `factor-augmented models`, `heterogeneous slopes`
- **为什么对您有用**: 解决了宏观面板 T≈N 下的 CCE 估计偏差与推断问题，属于经济学理论（面板因果/因子模型）与统计计算（Bootstrap 偏差修正）的交叉，对您在经济学应用中的因果推断和重抽样算法设计有直接参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

