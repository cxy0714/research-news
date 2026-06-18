# Scand. J. Stat. — Vol 52  Issue 1  ·  2026-06-19

- 共 18 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 18 篇全部抓到（对照 OpenAlex 18 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Scand. J. Stat. 本期 18 篇论文可归为四条主线：**假设检验的多样化新方法**（高维协方差 U‐检验、二阶随机占优 Lorenz P–P 检验、网络拟合优度图泛函检验、发表偏倚筛选效应、ANCOVA 顺序检验、多维变异系数非参数检验、流行病传播同质性检验、自回归马氏链 cutoff），**因果推断中的实验设计与识别**（阶梯楔形聚类随机实验的模型辅助 ANCOVA 估计量、序列对称分析设计的数学性质），**非参数与半参数估计的最优性理论**（SDE 平稳密度 minimax 率、函数主成分 minimax 估计、Lancaster 相关系数的新依赖度量），以及**统计计算与时间序列建模**（地统计似然最大化、分数 SDE 漂移的可计算 Skorokhod 估计、Tobit 计数时间序列）。

因果推断主线尤为突出：阶梯楔形实验的四类 ANCOVA 估计量在潜在结果框架下明确定义 estimands，且模型辅助性质允许工作模型错误，仍获得点估计一致性，并给出有限总体 CLT；SSA 设计重新推导粗序列比在处方时间趋势与未测量时不变混杂下的性质，揭示其可解释为目标药物与结局药物时间间隔趋于零的风险比，且能隐式调整时不变混杂——两者均着力厘清 estimand 与模型假设的匹配关系。非参数效率主线同样密集：SDE 平稳密度在各向异性 Hölder 类上的 minimax 率呈现相变，核估计量可达最优率；函数主成分从噪声离散化数据中的双渐近 minimax 率表明网格密度与样本量的角色差异；Lancaster 相关系数在可计算性与最大相关精度之间取得平衡，渐近分布简单。假设检验方向则覆盖了从高维椭圆分布协方差到 ER 图拟合优度的多种数据形态，其中多篇采用了参数自助法或 bootstrap 改善有限样本表现。

与因果推断方向最贴的论文是阶梯楔形 ANCOVA 和 SSA 设计；与半参数效率相关的是 SDE 平稳密度 minimax 率与函数主成分 minimax 估计；高维假设检验方面的代表是高维协方差 U‐检验（直接关联随机矩阵理论与椭圆分布），网络拟合优度检验则对图模型诊断有参考价值。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.12755](https://doi.org/10.1111/sjos.12755) · [arXiv](https://arxiv.org/abs/2306.11267) — Model‐assisted analysis of covariance estimators for stepped wedge cluster randomized experiments
- **作者**: Xinyuan Chen, Fan Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 416-446
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 针对阶梯楔形聚类随机实验（SW-CREs），本文在潜在结果框架下明确定义了一类 estimands，并突出了三种可解释的典型 estimands。为进行协变量调整，提出了四种分析协方差（ANCOVA）工作模型，每个估计量都是模型辅助的：即使工作模型错误设定，点估计仍然一致。在阶梯楔形随机化方案下，推导了有限总体中心极限定理，为估计量的渐近正态性提供了理论基础。通过模拟研究评估了有限样本性质，并应用于华盛顿州快速伴侣治疗研究的数据分析。本文为聚类随机实验中的 estimands 定义和稳健推断提供了统一框架，对纵向因果推断中的协变量调整方法具有直接指导意义。
- **关键技术**: `Stepped wedge design`, `Model-assisted ANCOVA`, `Finite population CLT`, `Potential outcomes framework`, `Cluster randomized experiments`
- **为什么对您有用**: 本文直接涉及阶梯楔形设计中的因果效应估计，属于因果推断中纵向簇群随机实验的重要子领域。研究者可利用“estimation theory in causal inference”中的知识来理解其模型辅助估计量的构造和有限总体渐近理论。该工作立即可用于改进自身在纵向因果推断中的估计器设计，或作为实际数据应用的基准方法。

### 2. [10.1111/sjos.12759](https://doi.org/10.1111/sjos.12759) — Revisiting the sequence symmetry analysis design
- **作者**: Jeppe Ekstrand Halkjær Madsen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Copenhagen · Leo Pharma (Denmark)
- **分类**: vol 52 · issue 1 · pp 469-479
- 相关性 6/10 · novelty: `minor`
- **摘要**: 本文重新审视序列对称分析（SSA）设计在药物流行病学中的数学性质，该设计通过比较处方顺序来评估药物不良反应。作者严格推导了粗序列比（crude SR）、零效应序列比和调整序列比在存在处方时间趋势与未测量时不变混杂下的性质。核心结论是：粗SR可解释为目标药物与结局药物时间间隔趋于0时的风险比（HR），且可通过logistic回归灵活估计协变量依赖的HR。粗SR能隐式调整未测量的时不变混杂，而调整序列比在治疗与结局不独立时无意义，应放弃使用。模拟研究支持理论推导。对您有用：本文为流行病学因果推断中的一种经典设计提供了清晰的数学框架，可直接应用于药物安全性监测中的数据集分析。
- **关键技术**: `sequence symmetry analysis`, `crude sequence ratio`, `hazard ratio estimation via logistic regression`, `prescription time-trend adjustment`, `unmeasured time-invariant confounding`
- **为什么对您有用**: (1) 直接关联流行病学（secondary interest）中的具体因果推断方法——序列对称分析设计，这是药物安全性监测的常用工具。 (2) 您对因果推断识别理论（moderately_familiar）和估计理论（very_familiar）的掌握足以理解并评估本文的假设与结论。 (3) 立即可做：阅读本文后，您可将该框架应用于流行病学数据集进行敏感性分析，或比较其与IV、proximal方法在同一设定下的表现。

## 非参数 / 半参数  *(nonparam_semipara, 4 篇)*

### 1. [10.1111/sjos.12735](https://doi.org/10.1111/sjos.12735) · [arXiv](https://arxiv.org/abs/2110.02774) — Minimax rate of estimation for invariant densities associated to continuous stochastic differential equations over anisotropic Hölder classes
- **作者**: Chiara Amorino, Arnaud Gloter
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 185-248
- 相关性 8/10 · novelty: `sharper_rate`
- **摘要**: 在连续观测轨道且时间跨度 T→∞ 的设定下，研究 d 维随机微分方程平稳分布密度 π 的非参数估计问题，目标 estimand 为各向异性 Hölder 类（光滑度 β₁≤…≤β_d）上的 π(x)。核心发现是逐点 L₂-risk 的 minimax rate 出现相变：若 β₁+β₂≥β_d，最优率为 T^{-2β̄/(2β̄+1)}（β̄ 为剔除最小两方向后的调和均值）；若 β₁+β₂<β_d，最优率为 T^{-2β̄/(2β̄+d)}，指数显式依赖于 d 与 β̄。作者证明核密度估计量可达此 minimax rate，并提出自适应程序同时覆盖逐点与积分风险；二维情形下自适应核估计可达 minimax optimal rate T^{-2β̄/(2β̄+1)}。对您有用：此各向异性 minimax 相变结果直接补充了您 very_familiar 的 minimax bounds 工具箱，为高维非参数密度估计的 rate 临界现象提供精确刻画。
- **关键技术**: `anisotropic Hölder class`, `minimax rate`, `phase transition in smoothness`, `kernel density estimator`, `stationary distribution of SDE`, `adaptive estimation`
- **为什么对您有用**: 直接连接您 primary interest 中的非参数理论及 minimax bounds 设定，各向异性光滑度条件下的相变现象是 minimax estimation 的经典深化方向。您可用 very_familiar 的 minimax bounds 工具验证其下界构造是否可推广至离散观测或更一般的 Markov 过程设定。立即可做：用现有 minimax 工具复现并拓展其下界论证至离散采样路径。

### 2. [10.1111/sjos.12733](https://doi.org/10.1111/sjos.12733) · [arXiv](https://arxiv.org/abs/2303.17872) — Lancaster correlation: A new dependence measure linked to maximum correlation
- **作者**: Hajo Holzmann, Bernhard Klar
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 145-169
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在非参数独立性检验与依赖度量设定下，本文提出基于 Lancaster 分布的新型相关系数（Lancaster correlation），目标是在一类双变量 Lancaster 分布下等于最大相关（maximum correlation），而在更广分布下仅略小于最大相关。与最大相关（需求解无穷维优化）不同，本文度量允许基于秩与矩的简单估计量，且具有 tractable 的渐近分布（n^{-1/2}-CAN）。基于渐近近似与 covariance bootstrap 的置信区间在有限样本下覆盖良好；独立性检验的 power 在模拟中优于 distance correlation 及秩函数依赖系数等竞争方法。对双变量正态分布，该度量恰好等于 Pearson 相关系数的绝对值，具备实践吸引力。对您可能有用：该度量的渐近理论涉及 U-statistic / 矩估计的投影与收敛分析，可直接连接您对 higher-order U-statistics 与非参数检验的兴趣。
- **关键技术**: `Lancaster correlation`, `maximum correlation (Hirschfeld-Gebelein-Rényi)`, `rank-based estimator`, `moment-based estimator`, `covariance bootstrap`, `asymptotic distribution of dependence measure`
- **为什么对您有用**: 本文连接到非参数独立性检验与依赖度量这一子方向，其估计量的渐近分析涉及 U-statistic 投影与经验过程工具，与您 very_familiar 的 higher-order U-statistics 计算与理论直接对口。您可用 treewidth / einsum 视角审视其矩估计量在高阶情形的计算复杂度，或用 minimax bound 验证其检验在局部替代下的 power 是否达到最优率。**立即可做**：用 very_familiar 的 U-statistic 工具即可展开对其估计量高阶投影与计算成本的延伸分析。

### 3. [10.1111/sjos.12719](https://doi.org/10.1111/sjos.12719) · [arXiv](https://arxiv.org/abs/2110.12739) — Minimax estimation of functional principal components from noisy discretized functional data
- **作者**: Ryad Belhakem, Franck Picard, Vincent Rivoirard, Angelina Roche
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 38-80
- 相关性 6/10 · novelty: `sharper_rate`
- **摘要**: 在噪声离散化函数数据设定下，研究函数主成分（FPC）估计的 minimax 收敛速率；关键 regularity 假设涉及协方差算子的谱衰减与离散网格大小。引入双渐近框架：样本量 n 与网格点数 J 同时增长，以刻画离散化与噪声对估计的联合影响。核心方法为将观测曲线投影到直方图（histogram）基上再进行 FPC 估计，证明了该投影估计在 minimax 意义下达到最优速率。理论结果揭示了网格密度与样本量在控制估计误差上的不同角色，并在模拟与基因组数据可视化中验证了方法。对您可能有用：该双渐近框架与 minimax 速率分析可直接迁移到高维统计中随机矩阵谱估计的离散化误差分析。
- **关键技术**: `minimax convergence rate`, `double asymptotic framework`, `histogram projection estimator`, `functional principal component analysis`, `covariance operator spectral decay`
- **为什么对您有用**: 直接连接到 nonparametric statistics 与 minimax bounds for estimation problems 这两个 primary interest 子方向。您武器库中 very_familiar 的 minimax bounds 工具可直接用来审视其声称的最优速率是否紧，以及双渐近框架的 lower bound 构造是否可推广到高维 RMT 的谱估计设定。follow-up 粗判：立即可做——用 minimax lower bound 技术验证其速率紧性，并尝试将双渐近框架移植到高维协方差矩阵的离散观测情形。

### 4. [10.1111/sjos.12758](https://doi.org/10.1111/sjos.12758) — Data‐driven estimation for multithreshold accelerated failure time model
- **作者**: Chuang Wan, Hao Zeng, Wenyang Zhang, Wei Zhong, Changliang Zou
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Jinan University · Southern University of Science and Technology · University of Macau · Xiamen University · Nankai University
- **分类**: vol 52 · issue 1 · pp 447-468
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在多阈值加速失效时间（AFT）模型设定下，目标是在不同子区间具有分段线性形式的回归系数及阈值参数的估计与推断，关键假设包括误差分布与协变量独立性及 mild regularity 条件。方法核心包含两步：先用修正 BIC 证明选择一致性，但因其依赖惩罚量且对模型配置敏感，进一步提出基于 order-preserved sample-splitting 的 cross-validation 准则，实现完全 data-driven 的阈值数量估计。参数估计的渐近性质（收敛率与分布）被严格建立；同时提出 score-type 检验统计量判断阈值效应是否存在，该统计量无需估计潜在阈值参数，天然适配多阈值场景。理论结果证明了选择一致性与检验的渐近性质，模拟验证了有限样本表现。对您可能有用：score-type 检验免估阈值的思想可迁移至因果推断中处理效应异质性的多阈值检验设定。
- **关键技术**: `multithreshold AFT model`, `modified BIC selection consistency`, `order-preserved sample-splitting`, `cross-validation criterion`, `score-type test`, `asymptotic distribution of threshold estimates`
- **为什么对您有用**: 本文连接到 hypothesis testing 与 semiparametric theory 子方向：score-type 检验绕过 nuisance parameter（阈值位置与数量）直接做存在性检验，与您熟悉的 M-estimation theory 中 nuisance-free test 思路相通。用 very_familiar 的 minimax bounds 与 M-estimation 理论可以审视其参数估计收敛率是否可达最优；moderately_familiar 的 semiparametric theory 可评估该 score-type 检验是否触及 efficiency bound。Follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以将 nuisance-free score 检验推广至因果推断中带 IV / proximal 设定的多阈值场景。

## 数理统计 / 假设检验  *(hypothesis_testing, 8 篇)*

### 1. [10.1111/sjos.12738](https://doi.org/10.1111/sjos.12738) — Adjusted location‐invariant U‐tests for the covariance matrix with elliptically high‐dimensional data
- **作者**: Kai Xu, Yeqing Zhou, Liping Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Anhui Normal University · Tongji University · Renmin University of China
- **分类**: vol 52 · issue 1 · pp 249-269
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在椭圆分布高维数据下研究协方差矩阵的U-检验，目标是对经典的John-Nagao和Ledoit-Wolf检验进行修正，使其在椭圆总体下仍保持有效的大小。研究发现原始检验在椭圆分布下表现不佳，原因在于椭圆分布坐标间存在高阶相关性。为此，作者提出必要的校正项，修正检验统计量以消除这种相关性带来的偏差，并推导了修正后检验统计量的通用渐近零分布，适用于椭圆分布及更广的分布族。为提高计算效率，论文还给出了新统计量的等价简化形式。理论部分证明了所提检验的渐近性质，并通过模拟和实证研究验证了其准确性。该工作直接关联到高维假设检验和随机矩阵理论，特别是对椭圆分布的高维协方差结构提供了实用的推断工具。
- **关键技术**: `U-tests for covariance matrix`, `John-Nagao test`, `Ledoit-Wolf test`, `elliptical distribution correction`, `high-dimensional asymptotics`, `universal null distribution`
- **为什么对您有用**: 本文直接针对高维协方差矩阵的假设检验问题，属于您primary interests中的‘hypothesis testing’和‘high-dimensional statistics (random matrix theory)’交叉方向。您掌握的‘high-dimensional asymptotics’（very_familiar）可以立即用于审视文中渐近零分布的推导是否严谨，并评估其universal性质。此外，若想将校正思想推广到其他U-检验（如高阶U-统计量），需先熟悉椭圆分布的高阶相关性结构，这属于‘theory of higher-order U-statistics’（moderately_familiar）的范畴，因此中期可做：先巩固U-统计量理论，再尝试推广。

### 2. [10.1111/sjos.12761](https://doi.org/10.1111/sjos.12761) · [arXiv](https://arxiv.org/abs/2308.00317) — A new class of nonparametric tests for second‐order stochastic dominance based on the Lorenz P–P plot
- **作者**: Tommaso Lando, Sirio Legramanti
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 480-512
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对两个非负随机变量样本，提出了一类新的非参数检验，用于原假设：一个随机变量在二阶随机占优意义上支配另一个。检验统计量基于 Lorenz P–P 图——即一个分布的非缩放 Lorenz 逆函数与另一个分布的非缩放 Lorenz 函数的复合——与恒等函数的差异的泛函。作者在原假设下确定了这些统计量的上界，并推导了其极限分布，该极限分布可通过 bootstrap 程序近似。在较温和的正则条件下，证明了检验的渐近有效性；模拟研究表明该方法在有限样本下表现良好，能够克服传统基于累积分布函数积分的方法（要求有界支撑且在部分偏离情形下检验力不足）的局限。该方法还可扩展到分数阶随机占优族，其中一阶占优作为极限情况包含在内。对您而言，该工作直接关联假设检验与非参数方法的交叉领域，其中涉及的非参数极限理论和 bootstrap 技术可以借助您熟悉的非参数统计工具（如经验过程、U-统计量投影）加以深入分析。
- **关键技术**: `Lorenz P–P plot`, `second-order stochastic dominance`, `bootstrap approximation`, `functional of difference`, `fractional-degree stochastic orders`
- **为什么对您有用**: (1) 直接对应 primary interest 中的 hypothesis testing 和 nonparametric theory 子方向，具体是二阶随机占优的非参数检验。 (2) 您技术武器库中 very_familiar 的 nonparametric statistics 项可以用于分析检验的渐近性质（如收敛速度、最优化），甚至可能用您熟悉的 minimax bounds 来评估该检验是否达到最优判别率。 (3) follow-up 粗判：立即可做，因为您对非参数极限理论和 bootstrap 方法非常熟悉，可快速评估方法的理论保证并考虑扩展（如高维或相依数据）。

### 3. [10.1111/sjos.12729](https://doi.org/10.1111/sjos.12729) — Tests under simple order in one‐way ANCOVA
- **作者**: Anjana Mondal, Somesh Kumar
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Indian Institute of Technology Kharagpur
- **分类**: vol 52 · issue 1 · pp 104-144
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 针对单因素协方差分析模型中处理效应在简单顺序备择下的同质性检验问题，在误差方差异质的设定下开展研究。提出了似然比检验（LRT）以及基于并交原理的两个近似检验统计量，并推导了它们的渐近分布。采用参数自举技术实现LRT，严格证明了其渐近有效性，同时给出了同时置信区间的构造方法。所有检验程序被进一步推广至多个协变量的情形，并考察了模型偏离正态假定时的稳健性。大规模模拟实验表明，所提方法在名义水平控制和检验功效方面均表现良好。该工作属于参数假设检验在ANCOVA中的扩展，与您主要兴趣中的数学统计与假设检验方向直接相关。
- **关键技术**: `likelihood ratio test`, `union-intersection principle`, `parametric bootstrap`, `simultaneous confidence intervals`, `heterogeneous error variances`, `ordered alternatives`
- **为什么对您有用**: 本文直接对应您primary interest中的‘假设检验’子方向，处理的是ANCOVA中顺序备择的检验这一经典但尚未完全解决的问题。技术层面，参数自举的渐近有效性证明可调用您‘very_familiar’中的非参数统计或渐近理论武器来评估其理论框架的严谨性；同时其对多协变量的推广思路对您关注的因果推断中协变量调整问题也有启发。**立即可做**：检验程序的R代码实现及模拟复现可直接调用您的软件开发和统计计算能力。

### 4. [10.1111/sjos.12743](https://doi.org/10.1111/sjos.12743) — A classical hypothesis test for assessing the homogeneity of disease transmission in stochastic epidemic models
- **作者**: Georgios Aristotelous, Theodore Kypraios, Philip D. O'Neill
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Nicosia · University of Nottingham
- **分类**: vol 52 · issue 1 · pp 295-313
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在群体被划分为社会子群的随机流行病模型中，本文研究已完成疫情（completed epidemic）的疾病传播同质性检验问题，目标 estimand 是是否存在显著的组内传播效应。核心方法基于感染个体的时间有序组标签向量：在零假设（同质性/无组内传播）下，该离散随机向量具有不依赖任何模型参数的已知抽样分布，从而构造出参数自由的精确检验。作者进一步建立了该统计量的中心极限定理，提供大样本近似。模拟与两个真实流行病学数据集显示检验性能优良，且计算代价极低、实现简单。对您有用：该检验的参数自由性质与 CLT 可直接连接到您 hypothesis testing 与 epidemiology 的交叉兴趣，其有序标签向量的组合结构也可能用 higher-order U-statistic 视角重新审视。
- **关键技术**: `parameter-free exact test`, `time-ordered group labels`, `central limit theorem for discrete random vectors`, `stochastic epidemic model`, `homogeneity hypothesis testing`
- **为什么对您有用**: 本文连接到您 hypothesis testing 与 epidemiology（应用因果/流行病学数据集）两个子方向：零假设下标签向量分布不依赖参数这一性质，使得检验完全避开了流行病模型中常见的参数估计难题。从您 very_familiar 的 higher-order U-statistics（treewidth / tensor contraction）出发，有序标签向量的组合抽样分布本质上是一个高阶多项式统计量，其计算复杂度与投影可用您的 einsum/tensor-contraction 工具箱分析——这是**立即可做**的 follow-up：用 U-statistic 投影理论重写该检验的 influence function 并验证 CLT 的收敛速率是否可达 n^{-1/2}-CAN。

### 5. [10.1111/sjos.12750](https://doi.org/10.1111/sjos.12750) · [arXiv](https://arxiv.org/abs/2305.10380) — Goodness‐of‐fit testing based on graph functionals for homogeneous Erdös–Rényi graphs
- **作者**: Barbara Brune, Jonathan Flossdorf, Carsten Jentsch
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 332-380
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文针对齐次Erdös–Rényi (ER) 模型的拟合优度检验问题，提出了一类基于图泛函 (graph functionals) 的检验方法。允许网络既可以是稠密的也可以是稀疏的，且备择假设允许非恒定边概率。作者以统一的方式推导了这类图泛函的极限分布，并构造了渐近检验。为避免渐近检验中常有的方差估计难题，还提出了参数自助法 (parametric bootstrap) 并证明了其相合性。进一步，在固定和局部备择下，对子图计数等常用检验统计量进行了功效分析。该工作为网络数据的模型诊断提供了系统性的假设检验框架。对您而言，该论文直接连接您对假设检验 (hypothesis testing) 的兴趣，且图泛函（如子图计数）本质上与高阶U统计量相关，可以借助您熟悉的U统计量理论来进一步加以分析和推广。
- **关键技术**: `graph functionals`, `limit theorems for network statistics`, `parametric bootstrap`, `power analysis under local alternatives`, `homogeneous Erdős–Rényi models`
- **为什么对您有用**: 本文连接您的数学统计（假设检验）兴趣，子图计数实质上是高阶U统计量，您可以利用您非常熟悉的高阶U统计量投影理论分析其渐近分布性质，或利用最小最大界研究其功效最优性。由于您对非参统计和高维渐近已很熟悉，该论文的核心结果可立即可读并可能推广到更一般的网络模型或用于网络因果推断中的模型诊断。

### 6. [10.1111/sjos.12762](https://doi.org/10.1111/sjos.12762) — The effect of screening for publication bias on the outcomes of meta‐analyses
- **作者**: Haben Michael
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Massachusetts Amherst
- **分类**: vol 52 · issue 1 · pp 513-531
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在 meta-analysis 设定下，研究初步发表偏倚检验（preliminary test）对后续主分析（main stage）估计量的 post-selection inference 效应。关键假设是两阶段检验-估计流程，主分析仅在初步检验不拒绝零假设时执行。核心机制是分析 conditional inference 下估计量的 bias 与 MSE，对比 always-estimate、never-estimate 与 conditional-on-non-rejection 三种策略的理论表现。主要理论结果表明，在许多常见情形下，条件执行主分析产生的偏差很小或为零，即 post-selection 偏倚在此特定两阶段流程中并不严重。对您可能有用：该文将 post-selection inference 问题具体化为两阶段检验-估计流程，与您在 hypothesis testing 及 M-estimation theory 中的兴趣直接相关。
- **关键技术**: `post-selection inference`, `conditional bias analysis`, `preliminary test estimation`, `meta-analysis selection bias`, `MSE comparison of estimation strategies`
- **为什么对您有用**: 直接连接到 hypothesis testing 子方向，具体探讨两阶段检验-估计流程的 post-selection inference 效应。用您 very_familiar 的 M-estimation theory（moderately_familiar）可以分析此类 conditional estimator 的渐近偏差与效率损失，甚至推导更一般的 minimax 策略。立即可做：用 M-estimation 与 minimax 工具即可动手分析该两阶段流程的更紧理论界。

### 7. [10.1111/sjos.12740](https://doi.org/10.1111/sjos.12740) · [arXiv](https://arxiv.org/abs/2301.12009) — Inference for all variants of the multivariate coefficient of variation in factorial designs
- **作者**: Marc Ditzhaus, Łukasz Smaga
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 270-294
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在一般因子设计下，研究多元变异系数（MCV）多种变体的非参数推断问题，目标参数为不同 MCV 变体定义的散度效应量。本文将已有仅针对单一 MCV 变体的 permutation 检验推广至其他合理变体，并在拒绝全局零假设后提出 max-type 检验用于 post hoc 对比分析。为改善 max-type 检验的小样本表现，作者提出一种新型 bootstrap 策略并证明其渐近有效性（asymptotic validity）。模拟与真实数据（R 包 GFDmcv）验证了方法性能。对您有用：本文属于假设检验与非参数推断的交叉，其 max-type 多重比较与 bootstrap 渐近理论可为您在因果推断中处理多假设/多 mediator 的 post hoc 分析提供参考。
- **关键技术**: `multivariate coefficient of variation`, `nonparametric permutation test`, `max-type test`, `bootstrap asymptotic validity`, `post hoc multiple comparisons`, `factorial design`
- **为什么对您有用**: 本文连接到 hypothesis testing 与 nonparametric theory 子方向，具体处理因子设计下多参数变体的全局与 post hoc 检验。您武器库中 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 M-estimation theory 可直接攻破其 bootstrap 渐近有效性证明与 permutation 检验的 exchangeability 条件分析。follow-up 粗判：立即可做——用 very_familiar 的非参数检验工具即可复现并拓展其 max-type 检验到因果 mediator/IV 的多重对比场景。

### 8. [10.1111/sjos.12748](https://doi.org/10.1111/sjos.12748) · [arXiv](https://arxiv.org/abs/2209.01474) — Cutoff for a class of auto‐regressive models with vanishing additive noise
- **作者**: Balázs Gerencsér, Andrea Ottolini
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 314-331
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在 $d$ 维欧氏空间上的一类参数化自回归 Markov 链中，每步随机选取一个坐标并用其他坐标的带噪衰减加权平均替换，目标是研究当参数 $n$ 增大（对应加性噪声趋于零）时链的收敛速率。核心机制是证明该 Markov 链在 $n\to\infty$ 时呈现 cutoff 现象——即总变差距离在临界时间窗口 $O(1)$ 内从接近 1 急剧降至接近 0，而非通常的逐步衰减。技术工具依赖于特征值间隙的精确估计与谱分析，以确定 cutoff 窗口与临界时间 $t_n$ 的显式表达。该模型源于 de Finetti 对部分可交换数据的贝叶斯分析方案，理论结果给出了噪声消退极限下收敛的相变刻画。对您研究 Markov 铴收敛与假设检验中的相变/临界阈值分析有直接参考价值。
- **关键技术**: `cutoff phenomenon`, `total variation distance`, `spectral gap analysis`, `Markov chain convergence`, `de Finetti exchangeability`
- **为什么对您有用**: 本文精确刻画了 Markov 链在噪声消退时的 cutoff 相变，直接连接到您对 hypothesis testing 中临界阈值与收敛速率的兴趣；用您 very_familiar 中的 minimax bounds / high-dimensional asymptotics 工具可以验证其谱间隙估计是否可推广到更一般的高维自回归设定。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以将此 cutoff 框架迁移到 M-estimator 迭代算法的收敛相变分析。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12722](https://doi.org/10.1111/sjos.12722) — On maximizing the likelihood function of general geostatistical models
- **作者**: Tingjin Chu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: The University of Melbourne
- **分类**: vol 52 · issue 1 · pp 81-103
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文研究一般地统计模型（geostatistical models）的似然函数最大化问题。首先，证明了对数似然函数存在唯一全局最大值的充分条件，并探讨了其凸性。其次，分析了两步估计（two-step estimation）的理论性质，且结果适用于非二次可微的协方差函数。模拟部分评估了三种优化算法在最大化对数似然函数时的表现。这些结果对空间统计中基于似然的推断提供了理论保障和算法指导。对统计计算（数值优化算法）兴趣有直接参考价值。
- **关键技术**: `likelihood-based geostatistical models`, `unique global maximizer conditions`, `convexity of log-likelihood`, `two-step estimation consistency`, `non-twice differentiable covariance functions`, `optimization algorithm comparison`
- **为什么对您有用**: 本文深入分析地统计模型似然函数的最大化问题，与您的统计计算（数值算法）兴趣直接相关。您非常熟悉的高维渐近理论和逆问题中的随机噪声处理可用于理解非二次可微协方差函数对似然面的影响。立即可做：您可以用现有的优化工具（如Nelder-Mead、L-BFGS）复现并扩展模拟比较，或研究其两步估计的渐近效率。

### 2. [10.1111/sjos.12711](https://doi.org/10.1111/sjos.12711) · [arXiv](https://arxiv.org/abs/2301.05341) — On a computable Skorokhod's integral‐based estimator of the drift parameter in fractional SDE
- **作者**: Nicolas Marie
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 1-37
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在分数布朗运动（fBm）驱动的随机微分方程（SDE）框架下，研究漂移参数θ的估计问题，基于多个（可能相关）样本路径副本。由于fBm不满足经典Itô积分所需的正则性，需使用Skorokhod积分构造最小二乘（LS）型估计量。当Hurst指数H<1/2时，该估计量可计算且具有一致性；当H≥1/2时，Skorokhod积分无法从数据中直接计算，作者提出了一种可计算的近似替代方案，并证明了其收敛性。理论结果覆盖了Hurst指数全范围（0<H<1），尤其填补了H≥1/2时计算可行性的空白。论文涉及收敛速率和渐近性质，但未明确给出半参数效率界。本文与您对统计计算中数值方法（特别是可计算近似理论）的兴趣直接相关。
- **关键技术**: `Skorokhod integral LS estimator`, `fractional Brownian motion`, `drift parameter estimation`, `computable approximation`, `convergence rates`, `Hurst index`
- **为什么对您有用**: (1) 本文聚焦于统计计算中的数值近似方法（可计算估计量的构造），直接连接到您对统计计算（数值方法）的 primary interest。 (2) 论文中的 LS 型估计量本质上是 M-估计，可借助您 moderately_familiar 中的 M-estimation theory 理解其渐近性质，例如分析收敛条件与正则性。 (3) 暂不可做——核心工具（分数布朗运动、Skorokhod积分与Malliavin calculus）不在您的武器库中，需先补随机分析基础才能在该方向开展工作。

## 其他  *(other, 2 篇)*

### 1. [10.1111/sjos.12734](https://doi.org/10.1111/sjos.12734) — Estimation of win, loss probabilities, and win ratio based on right‐censored event data
- **作者**: Erik T. Parner, Morten Overgaard
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Aarhus University
- **分类**: vol 52 · issue 1 · pp 170-184
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文在独立右删失设定下，研究优先多事件数据中胜率（win ratio）及胜/负概率的估计问题，目标参数为胜率与时间依赖的胜/负概率函数。作者提出无需比例胜负概率假设的胜率估计量，并在独立右删失下推导其渐近正态分布与方差公式。核心方法基于计数过程与Aalen-Johansen型估计，避免了以往文献中删失调整不足或强比例假设的缺陷。模拟显示方差公式在小样本下仍准确，并附两个心血管数据集的应用。对您而言，本文属于生存分析/临床统计的应用方法论文，理论贡献为渐近分布推导，方法学novelty有限。
- **关键技术**: `win ratio estimation`, `right-censored survival data`, `Aalen-Johansen estimator`, `asymptotic normality`, `independent censoring assumption`
- **为什么对您有用**: 本文与您的主要兴趣（因果推断、高维/效率理论、半参数理论）无直接交集，属于临床统计的生存分析应用。若您未来涉足流行病学队列的因果生存分析（如竞争风险下的ATE估计），本文的删失调整与渐近推导可作为背景阅读，但无需用您武器库中的半参数效率/HOIF工具攻破。**暂不可做**：本文核心是计数过程生存分析，不在您当前研究轨道上，不建议展开精读。

### 2. [10.1111/sjos.12751](https://doi.org/10.1111/sjos.12751) · [arXiv](https://arxiv.org/abs/2403.00224) — Tobit models for count time series
- **作者**: Christian H. Weiß, Fukang Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 381-415
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对计数时间序列中INARMA与INGARCH模型难以获得负自相关系数的问题，提出一种名为Tobit方法的通用建模框架。该方法通过引入Tobit映射（带有下界截断的潜变量机制）将线性AR结构转化为近线性的条件期望，相比现有softplus方法更灵活地适用于有限计数和INARMA族。具体以Skellam–Tobit INGARCH模型为例，推导了模型的平稳性条件、近似矩计算公式，并给出了极大似然估计和截断最小绝对偏差（LAD）估计的渐近理论。模拟研究和三个真实数据集表明，该模型能够捕捉负自相关且预测表现良好。尽管本文不直接涉及因果推断或高维问题，但其中使用的截断LAD估计属于M估计范畴，与您的中等熟悉武器'M-estimation theory'可直接对接——您可以分析其识别性及有限样本性质，为将类似框架推广至纵向因果推断中的计数结果建模提供参考。
- **关键技术**: `Tobit model`, `INGARCH`, `Skellam distribution`, `Censored LAD estimation`, `Maximum likelihood`, `Stationarity conditions`
- **为什么对您有用**: 连接您数理统计中M估计理论这一子方向；您可用moderately_familiar的M估计理论分析其估计量的渐近正态性与一致性，检验该方法在纵向设定下的推广潜力。**暂不可做**：核心时间序列的遍历性理论和似然推断工具不在您当前武器库中，需要额外学习。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

