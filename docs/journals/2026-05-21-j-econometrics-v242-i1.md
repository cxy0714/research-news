# J. Econometrics — Vol 242  Issue 1  ·  2026-05-21

- 共 7 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105793](https://doi.org/10.1016/j.jeconom.2024.105793) — On the performance of the Neyman Allocation with small pilots
- **作者**: Yong Cai, Ahnaf Rafi
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105793
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在实验设计框架下，研究当先导实验样本量固定而主实验样本量趋于无穷时，Neyman Allocation 对 ATE 估计的渐近性质。本文采用固定先导样本量的渐近框架，证明了在此设定下基于先导方差的 Neyman Allocation 可能导致 ATE 估计的渐近方差高于非自适应的平衡随机化。具体而言，当结果变量相对于处理状态近似同方差或具有高峰度时，这种效率损失尤为显著。理论分析揭示了小先导样本导致的方差估计误差如何传导至分配机制并恶化渐近效率。多个实证例子表明同方差和重尾情形在实践中常见，模拟实验探讨了改进有限样本表现的方法。对您有用：该文为小先导实验下的 ATE 估计效率提供了严谨的渐近方差分析，直接关联您对因果推断中效率理论与实验设计的兴趣。
- **关键技术**: `Neyman allocation`, `fixed-pilot asymptotics`, `asymptotic variance comparison`, `balanced randomization`, `ATE estimation`
- **为什么对您有用**: 该文聚焦小先导实验下 ATE 估计的渐近方差比较，直接关联您在因果推断（实验设计）与效率理论（渐近方差/效率损失）方面的核心兴趣，提醒在异方差/重尾设定下需谨慎使用自适应分配。

### 2. [10.1016/j.jeconom.2024.105785](https://doi.org/10.1016/j.jeconom.2024.105785) — 2SLS with multiple treatments
- **作者**: Manudeep Bhuller, Henrik Sigstad
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105785
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在处理效应异质性下，多处理（multiple treatments）模型的 2SLS 识别问题，核心 estimand 为各处理的个体特定效应。证明了“平均条件单调性”与“无交叉效应”是 2SLS 识别各处理效应正加权平均的充要条件。设定允许任意数量的处理、连续或离散工具变量及协变量。进一步给出了上述识别条件的可检验含义，并刻画了隐含的选择行为。主要理论贡献在于澄清了多处理 IV 设定下 2SLS 的因果解释边界，对您在因果推断（IV 方法）与经济理论（因果应用）交叉领域的研究有直接参考价值，特别是多处理 IV 的识别逻辑与可检验约束。
- **关键技术**: `2SLS identification`, `multiple treatments`, `treatment effect heterogeneity`, `average conditional monotonicity`, `no cross effects`, `testable implications`
- **为什么对您有用**: 直接关联您的 primary interest 中的因果推断（IV）与 secondary interest 中的经济理论（因果应用），为多处理 IV 设定下的识别逻辑和可检验约束提供了严格的理论刻画，有助于理解异质性下 2SLS 的因果解释边界。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105788](https://doi.org/10.1016/j.jeconom.2024.105788) — A simple specification test for models with many conditional moment inequalities
- **作者**: Mathieu Marcoux, Thomas M. Russell, Yuanyuan Wan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105788
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对具有大量（可能不可数）条件矩不等式的部分识别模型，提出一种设定检验方法，关键正则条件允许弱识别与非可微矩条件。为降低临界值计算中昂贵组件的运算负担，该统计量复用了部分计算结果以实现计算简化。针对弱假设引入的新理论问题，作者提出一种非传统的样本分割程序，对同一原假设执行多次检验。理论结果表明，该检验在广泛的分布类上控制均匀尺寸（uniform size），对固定替代假设势趋于1，并刻画了局部替代假设下的检验势。该工作在弱假设下兼顾了计算可行性与渐近优良性。对您有用：直接推进了您在假设检验方向对高维/无限维矩不等式检验的理论认知，且该方法在部分识别的因果推断（如弱IV下的ATE界）和经济理论应用中具有直接迁移价值。
- **关键技术**: `conditional moment inequalities`, `specification test`, `unconventional sample splitting`, `uniform size control`, `partially identified models`, `local power analysis`
- **为什么对您有用**: 直接契合您在数学统计（假设检验）方向的兴趣，处理了高维/无限维矩不等式下的均匀检验问题；同时，部分识别与条件矩不等式在因果推断（如弱IV、部分识别的ATE界）和经济理论中应用广泛，该方法提供了弱假设下的新检验工具。

### 2. [10.1016/j.jeconom.2024.105794](https://doi.org/10.1016/j.jeconom.2024.105794) — Prewhitened long-run variance estimation robust to nonstationarity
- **作者**: Alessandro Casini, Pierre Perron
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105794
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 在时间序列线性回归的假设检验设定下，目标是构造对自相关和异方差稳健的长期方差（LRV）估计量，但传统 HAC 和 fixed-b 方法在非平稳性下或理论失效或导致检验不一致。本文提出一种非参数非线性 VAR 预白化 LRV 估计量，显式处理非平稳性，克服了以往预白化程序在非平稳下的不可靠性。技术上，该方法通过非线性 VAR 预白化提取非平稳动态，并建立了比现有文献更锐利的 LRV 估计 MSE 界，以此指导数据驱动的带宽选择。理论证明该估计量在非平稳原假设下有效，且在非平稳备择假设下检验具有一致性和单调功效，有限样本下第一类错误率准确。对您有用：该文在非参数 HAC 估计中推导了更锐利的 MSE 界，并解决了非平稳下假设检验的稳健推断问题，直接契合您在假设检验和半/非参数理论方面的 primary interest。
- **关键技术**: `nonlinear VAR prewhitening`, `long-run variance estimation`, `HAC estimation`, `sharper MSE bounds`, `data-dependent bandwidth`, `nonstationarity robust inference`
- **为什么对您有用**: 本文在非参数 LRV 估计中获得了更锐利的 MSE 界，并解决了非平稳下假设检验的稳健推断问题，直接契合您在假设检验和半/非参数理论方面的 primary interest，同时属于经济计量学中的核心推断问题。

## 经济理论 / 应用  *(econ_theory, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105790](https://doi.org/10.1016/j.jeconom.2024.105790) — Maximum likelihood estimation of a spatial autoregressive model for origin–destination flow variables
- **作者**: Hanbat Jeong, Lung-fei Lee
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105790
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文针对起点-终点（Origin-Destination, OD）流量数据（如贸易、人口流动），构建了空间自回归（SAR）模型，并在空间依赖性假设下研究其最大似然估计（MLE）。OD 流量数据的矩阵结构导致空间权重矩阵维度高达 N^2 × N^2，使得似然函数中的 Jacobian 项（对数行列式）与二次型计算面临维数灾难。作者推导了该 MLE 的一致性与渐近正态性，并利用权重矩阵的特定结构（如分块或稀疏性）来处理高维矩阵运算的理论性质。理论结果给出了估计量的渐近分布，模拟与实证表明该方法在流量网络数据中的有效性。对您而言，该文处理 N^2 × N^2 维矩阵似然与渐近性质的框架，与您关注的高维统计计算及随机矩阵理论（RMT）有潜在交集，同时提供了经济理论中空间溢出与网络因果的典型模型设定。
- **关键技术**: `spatial autoregressive model`, `maximum likelihood estimation`, `origin-destination flow matrix`, `Jacobian log-determinant`, `large-N asymptotics`, `spatial weight matrix`
- **为什么对您有用**: 本文属于经济理论中的空间计量模型，其处理 N^2 × N^2 维权重矩阵的似然计算与渐近理论，对您关注的高维统计计算及随机矩阵理论（RMT）在网络/空间数据中的拓展有启发，同时提供了经济理论中空间因果溢出的典型模型框架。

### 2. [10.1016/j.jeconom.2024.105751](https://doi.org/10.1016/j.jeconom.2024.105751) — Modeling long cycles
- **作者**: Da Natasha Kang, Vadim Marmer
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105751
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究经济与金融时间序列中高度持久且跨越样本大部分的“长随机周期”建模问题，目标是在周期长度可能随样本量增长的设定下对周期长度进行有效推断。作者指出传统推断程序在长周期存在时会产生误导性结果，并提出了一种新的计量经济学推断程序。该程序的核心在于构造了无论周期长度如何均渐近有效的检验与估计量，克服了传统方法在强持久性下的失准问题。实证应用于美国宏观与金融变量发现，商业周期、信贷和房价中存在长随机周期，且金融周期长度约为商业周期的两倍，而资产市场数据不存在此类周期。对您有用：该文在时间序列假设检验与渐近有效性方面提供了新视角，且其宏观金融数据集与分析范式对经济理论（应用宏观模型）的实证研究具有直接参考价值。
- **关键技术**: `long stochastic cycles`, `asymptotically valid inference`, `cycle length estimation`, `time series hypothesis testing`, `macroeconomic modeling`
- **为什么对您有用**: 属于经济理论（模型与数据集）方向，提出了对长周期参数的渐近有效推断程序（与数学统计假设检验/渐近理论相关），并提供了美国宏观金融数据集的实证分析，对研究经济时间序列的结构模型有参考价值。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105787](https://doi.org/10.1016/j.jeconom.2024.105787) — Bridging the Covid-19 data and the epidemiological model using the time-varying parameter SIRD model
- **作者**: Cem Çakmaklı, Yasin Şimşek
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 242 · issue 1 · pp 105787
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在经典 SIRD 传染病模型框架下引入时变参数，旨在利用每日计数数据对 Covid-19 疫情轨迹进行实时测量与预测，核心假设是传播率等参数随时间动态演变。方法上，采用广义自回归得分（GAS）结构捕捉参数的时变性，该结构专为疫情相关的每日计数数据设计，兼具灵活性与稀疏性且计算成本低。进一步，模型通过混频设定扩展以处理未报告病例的潜在影响，实证表明未报告病例对参数估计具有显著效应。全样本结果显示该框架能准确捕捉疫情的连续波次，实时预测练习也表明其能提供及时精确的疫情态势信息及对确诊和死亡病例的准确预测。对您而言，这篇论文展示了如何将计量经济学中的 GAS 模型与流行病学结构模型结合，为流行病学动态结构模型的参数估计与混频数据处理提供了可迁移的建模思路。
- **关键技术**: `time-varying parameter SIRD model`, `Generalized Autoregressive Score (GAS) model`, `mixed-frequency data`, `count data time series`, `state-space filtering`
- **为什么对您有用**: 属于您 secondary interest 中的流行病学与经济理论交叉应用；展示了计量时间序列方法（GAS）在流行病学结构模型中的实际应用与混频数据处理，对您在流行病学应用因果/结构模型工作有建模思路借鉴价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

