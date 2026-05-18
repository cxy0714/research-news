# Scand. J. Stat. — Vol 53  Issue 1  ·  2026-05-18

- 共 20 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.70035](https://doi.org/10.1111/sjos.70035) — Causal discovery in heavy‐tailed linear structural equation models via scalings
- **作者**: Mario Krali
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 291-334
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究重尾噪声下的线性结构方程模型（SEM）的极端因果依赖结构，在正则变差（regular variation）框架下，目标是基于极端观测识别因果图。提出一种基于极端角测度（extremal angular measure）缩放参数的因果发现方法，将因果方向识别转化为缩放参数的排序问题。算法层面引入了基于稳定性概念的超参数选择程序，并在理论上证明了该因果发现算法的相合性（consistency）。模拟与河流流量数据的实证表明，该方法相较于现有极端因果方法具有竞争力。对您有用：该文将正则变差与线性SEM结合的因果发现思路，为您在重尾数据下的因果识别（identification）及半非参数理论应用提供了新视角。
- **关键技术**: `linear structural equation model`, `regular variation`, `extremal angular measure`, `causal discovery`, `consistency`, `scaling parameter`
- **为什么对您有用**: 结合了因果推断（因果发现/识别）与半非参数理论（正则变差），为您在重尾或极端值设定下的因果识别提供了新视角和相合性理论保证。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.70025](https://doi.org/10.1111/sjos.70025) — Data integration with nonprobability sample: Semiparametric model‐assisted approach
- **作者**: Danhyang Lee, Sixia Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 33-53
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在概率与非概率样本数据融合设定下，本文旨在估计有限总体参数并处理非概率样本中可能存在的不可忽略选择偏差。为放宽传统的随机缺失（MAR）假设，作者提出灵活的半参数倾向得分模型，并采用伪剖面似然法进行估计。随后基于概率样本构建差分估计器，利用非概率样本及估计的倾向得分生成代理值以修正偏差。理论部分给出了所提估计量的渐近性质与方差估计公式，模拟与实证显示其优于现有方法。对您有用：半参数倾向得分与伪剖面似然的结合为处理不可忽略选择偏差提供了新思路，可直接迁移至因果推断中的敏感性分析或流行病学数据融合场景。
- **关键技术**: `semiparametric propensity score`, `pseudo-profile-likelihood`, `difference estimator`, `nonignorable selection bias`, `data integration`
- **为什么对您有用**: 半参数倾向得分模型与伪剖面似然估计直接契合您在半参数理论与因果推断（选择偏差/倾向得分）上的兴趣；放宽MAR假设的思路对流行病学或经济学中的非随机缺失数据处理有迁移价值。

### 2. [10.1111/sjos.70032](https://doi.org/10.1111/sjos.70032) — Variable selection via thresholding
- **作者**: Ka Long Keith Ho, Hien Duy Nguyen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 207-237
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在回归设定下，针对无法将无关信号精确收缩至零的估计量，本文研究基于阈值化的变量选择，目标是在温和正则条件下一致估计相关变量集合。作者形式化分析了一种阈值截断程序，提出一种简单的阈值方法以实现变量选择一致性。在此基础上，构造了一个稀疏、n^{-1/2}-相合且渐近正态的估计量，其非零元素不带有收缩偏差，避免了 Lasso 等正则化方法的系数偏移。理论证明表明，阈值截断能在保证选择一致性的同时恢复非零系数的渐近正态性，数值模拟和真实数据进一步验证了其表现。该工作对您在效率理论中构造无偏/渐近正态估计量（如 debiased ML 消除收缩偏差的思路）有直接参考价值。
- **关键技术**: `thresholding variable selection`, `sqrt(n)-consistent estimation`, `asymptotic normality`, `shrinkage bias correction`, `oracle property`
- **为什么对您有用**: 涉及高维/半参数估计中的收缩偏差与渐近正态性恢复，与您关注的 efficiency theory (debiased ML 消除正则化偏差) 和高维统计中构造有效推断的思路直接相通。

### 3. [10.1111/sjos.70051](https://doi.org/10.1111/sjos.70051) — Shape‐restricted statistical inference for non‐ignorable missing data under a general additive model
- **作者**: Junjun Lang, Yukun Liu, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 554-574
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在非可忽略缺失数据设定下，目标为总体结果均值，假设缺失概率服从带一般可加协变量效应的logistic模型，并利用工具变量(IV)实现identification。提出一种基于形状约束（如单调、凸/凹）且无需调参的半参数估计量，通过IV分离非可忽略缺失的混淆，避免了参数模型的误设风险。系统建立了该估计量的相合性、收敛速率与渐近正态性，核心工具涉及形状约束下的经验过程与半参数理论。数值结果表明，当参数模型正确时该估计量与参数方法表现相当，而在模型误设时显著优于后者。该文将IV识别与半参数形状约束结合，为处理非可忽略缺失/选择偏差提供了无需调参的渐近正态推断路径，直接契合您在IV因果推断与半参数理论方面的兴趣。
- **关键技术**: `shape-restricted estimation`, `non-ignorable missing data`, `instrumental variable`, `additive model`, `asymptotic normality`, `tuning-parameter-free`
- **为什么对您有用**: 将IV识别策略与半参数形状约束结合，为非可忽略缺失/选择偏差提供无需调参的渐近正态推断，直接契合您在IV因果推断与半参数理论方面的兴趣。

### 4. [10.1111/sjos.70027](https://doi.org/10.1111/sjos.70027) — Semiparametric regression for circular response with application in ecology
- **作者**: Jose Ameijeiras‐Alonso, Irène Gijbels
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 54-101
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究圆形响应变量依赖于线性或圆形预测变量的半参数回归问题，设定条件密度属于允许不对称与变峰度的参数族，而模态方向与集中度非参数地依赖于协变量。核心估计方法采用带核权重的局部多项式拟合来建模条件模态方向与集中度。理论上，建立了模态方向与集中度估计量的渐近正态性。基于该渐近结果，推导了最优平滑参数的表达式并提出了数据驱动的带宽选择器。实证部分将该模型应用于迁徙鸟类方位对高度与风向的回归。尽管本文聚焦于方向统计学的圆形数据，其局部多项式核估计的渐近正态性推导对您的半参数/非参数理论兴趣有基础方法论的参考价值。
- **关键技术**: `semiparametric regression`, `local polynomial kernel smoothing`, `circular data modeling`, `asymptotic normality`, `optimal bandwidth selection`
- **为什么对您有用**: 本文涉及您的半参数与非参数理论兴趣（局部多项式核估计与渐近正态性推导），虽然应用场景为生态学中的圆形数据，但其对非参数成分的渐近分析思路可为您的半参数理论研究提供基础方法论的参考。

### 5. [10.1111/sjos.70048](https://doi.org/10.1111/sjos.70048) — Nonparametric simulation of multivariate extreme events via spectral bootstrap
- **作者**: Nisrine Madhar, Juliette Legrand, Maud Thomas
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 482-497
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多元极值理论（EVT）设定下，针对极端观测稀少导致推断困难的问题，目标是基于多元广义 Pareto 分布的谱表示对联合尾部行为进行非参数模拟。本文提出多元极端事件谱自助法（spectral bootstrap），与传统自助法不同，该方法通过保留数据的联合尾部结构来生成合成极端数据，从而改善推断的可靠性。核心技术依赖于广义 Pareto 随机向量的谱表示与非参数重抽样机制。模拟与实证结果表明，该方法在估计尾部风险指标时有效提升了可靠性。对您可能有用：虽然聚焦 EVT，但其非参数谱自助与重抽样机制对您在非参数理论及统计计算（数值模拟算法）方面的兴趣有方法论借鉴意义。
- **关键技术**: `spectral bootstrap`, `multivariate generalized Pareto distribution`, `nonparametric simulation`, `joint tail behavior`, `tail risk metrics`
- **为什么对您有用**: 虽然应用领域为极值理论，但其非参数谱自助法的设计思路对您在非参数理论及统计计算（数值模拟与重抽样算法）方面的兴趣有方法论上的迁移价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.70043](https://doi.org/10.1111/sjos.70043) — Efficient multiple‐robust estimation for nonresponse data under informative sampling
- **作者**: Kosuke Morikawa, Kenji Beppu, Wataru Aida
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 395-412
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在信息性抽样与无响应导致的联合偏差设定下，本文研究目标参数的半参数有效估计，将抽样权重显式建模为随机变量并假设缺失机制可由观测协变量解释。首先推导了该缺失数据结构下的半参数有效界（semiparametric efficiency bound），并构造了具有双稳健（double robustness）性质的有效估计量。为缓解对工作模型正确设定的依赖，作者提出一种两步经验似然（two-step empirical likelihood）方法，将双稳健扩展至多重稳健（multiple robustness），使得在多个候选模型中仅有一个正确时仍可消除偏差。理论证明了所提估计量的有效性与稳健性，模拟与 NHANES 流行病学数据应用验证了其在有限样本下整合外部汇总统计量并校正选择偏差的能力。对您有用：该文推导的半参数有效界与多重稳健构造直接契合您在效率理论与因果推断（选择偏差/缺失数据）上的兴趣，且 NHANES 数据应用对流行病学方向有参考价值。
- **关键技术**: `semiparametric efficiency bound`, `multiple robustness`, `empirical likelihood`, `informative sampling`, `data integration`, `double robustness`
- **为什么对您有用**: 推导了信息性抽样缺失数据下的半参数有效界，并通过经验似然实现多重稳健，直接契合您在效率理论与因果推断（选择偏差校正）的核心兴趣；同时 NHANES 数据应用对流行病学方向有数据集参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1111/sjos.70050](https://doi.org/10.1111/sjos.70050) — ATM: An aggregation test of moments approach for assessing high‐dimensional normality
- **作者**: Hengjian Cui, Lingyue Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 532-553
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维数据正态性检验问题，在维数 p 可大于样本量 n 的设定下，目标是构造不依赖协方差矩阵逆的仿射不变检验。传统基于逆协方差阵的检验在高维下失效，作者引入共三阶矩（co-third moment）与共四阶矩（co-fourth moment）新指标来刻画分布形状相对高维高斯族的偏离。基于此构造了两个渐近正态的检验统计量，有效规避了高维求逆的数值与理论困难。进一步通过聚合这两个检验并结合 power enhancement technique，发展出对局部偏离更敏感的 ATM 检验。理论上在较弱正则条件下证明了检验的渐近性质，模拟与实证显示其水平控制良好且功效优越。这对您的高维假设检验兴趣有直接参考价值，其避免矩阵求逆与功效增强的技巧可迁移至其他高维推断问题。
- **关键技术**: `high-dimensional normality test`, `co-third moment`, `co-fourth moment`, `power enhancement technique`, `affine invariant test`, `asymptotic properties`
- **为什么对您有用**: 直接契合您的高维统计与假设检验兴趣；其通过高阶矩聚合避免协方差矩阵求逆的思路，对高维统计计算和构造新检验统计量具有可迁移的方法论价值。

### 2. [10.1111/sjos.70046](https://doi.org/10.1111/sjos.70046) — Fixed effects Bayesian testing in high‐dimensional linear mixed models
- **作者**: Jiamin Liu, Xingwei Liu, Heng Lian, Wangli Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 442-481
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维线性混合模型（p>n）设定下，本文研究固定效应的分组显著性检验问题。针对传统频率派方法失效的问题，提出了一种受贝叶斯启发的检验统计量，其构造为独立非同分布随机变量的两个二次型之比。通过二次型的正态近似推导了检验统计量的零分布。为实现快速统计计算，引入了一种创新的一步迭代法来确定检验临界值。在温和正则条件下，推导了局部替代假设下的功效函数。数值实验表明该方法在功效上优于现有方法。该文将高维假设检验与二次型近似结合，且涉及临界值计算的迭代算法，直接契合您在假设检验、高维统计及统计计算方面的核心兴趣。
- **关键技术**: `high-dimensional linear mixed model`, `Bayesian-motivated test`, `quadratic form ratio`, `normality approximation`, `one-step iteration`, `local alternative power`
- **为什么对您有用**: 直接契合您在假设检验和高维统计方面的核心兴趣；其基于二次型比值的检验构造与临界值一步迭代算法，对高维推断的计算实现有直接参考价值。

### 3. [10.1111/sjos.70049](https://doi.org/10.1111/sjos.70049) — Kernel‐based marginal testing for covariate effects in high‐dimensional settings
- **作者**: Hong Yin, Yijun Wang, Ancha Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 498-531
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在高维设定下研究协变量对响应变量的效应，针对协变量间复杂的依赖与异质性，提出基于核条件均值依赖的无模型边际检验程序。检验统计量被构造为高维二次型，通过渐近近似该二次型，分别在原假设和局部替代假设下建立了统计量的极限正态分布。进一步，在线性模型框架和完全非参数设定下，详细推导并比较了所提检验相对于现有前沿方法的渐近相对效率（ARE）。理论结果表明，该方法在放松模型假设的同时保持了优良的检验功效与效率。对您可能有用之处在于，该文将高维二次型近似与核非参数检验结合，直接推进了您关注的高维假设检验与非参数理论交叉方向。
- **关键技术**: `kernel-based conditional mean dependence`, `quadratic form approximation`, `asymptotic relative efficiency`, `marginal testing`, `local alternatives`
- **为什么对您有用**: 直接推进您关注的“高维假设检验”与“非参数理论”交叉方向；通过高维二次型近似推导极限分布和渐近相对效率的分析框架，对您研究高维检验的 power 与效率有直接参考价值。

### 4. [10.1111/sjos.70034](https://doi.org/10.1111/sjos.70034) — Assessing estimation uncertainty under model misspecification
- **作者**: Rong Li, Yichen Qin, Yang Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 268-290
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在广义线性模型(GLM)可能误设的设定下，研究目标是准确评估估计量的不确定性。传统 bootstrap 和渐近推断在误设下常失效，本文提出 local residual bootstrap，通过从邻近观测重抽样代理残差(surrogate residuals)来近似统计量的抽样分布。该方法绕过得分方程，直接重构响应变量，从而支持标准误估计、置信区间构建与假设检验。理论上证明了该方法的 bootstrap validity；在模型正确时表现与传统方法相当，在误设下提供更准确的不确定性评估。对您可能有用：为数学统计中的假设检验与统计计算提供了一种在放松模型假设下仍保持有效的重抽样推断工具。
- **关键技术**: `local residual bootstrap`, `surrogate residuals`, `model misspecification`, `generalized linear models`, `bootstrap validity`
- **为什么对您有用**: 涉及数学统计中的假设检验与统计计算，提供在模型误设下稳健的 bootstrap 推断方法，对关注模型假设放松下的推断理论有参考价值。

### 5. [10.1111/sjos.70029](https://doi.org/10.1111/sjos.70029) — On goodness‐of‐fit testing for self‐exciting point processes
- **作者**: José Carlos Fontanesi Kling, Mathias Vetter
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 102-139
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对自激点过程（如Hawkes过程）参数模型缺乏可靠拟合优度检验的问题，本文提出一种基于bootstrap的检验方法。该方法通过bootstrap构造检验统计量的零分布，以规避自激过程复杂依赖结构下解析分布难以推导的困难。在infill-asymptotic设定下，作者证明了该检验的渐近一致性，但理论保证目前仅限于底层过程为非齐次Poisson过程的特例。模拟显示该方法对一般自激点过程均具有经验有效性。对您研究hypothesis testing与statistical computing（bootstrap数值算法）有直接参考价值，且点过程模型在astrostats与econ theory中应用广泛。
- **关键技术**: `goodness-of-fit test`, `self-exciting point process`, `bootstrap test`, `infill asymptotics`, `inhomogeneous Poisson process`
- **为什么对您有用**: 直接关联您primary interest中的hypothesis testing与statistical computing（bootstrap方法）；同时点过程模型是astrostats（如天文事件流）和econ theory（如金融交易数据）的常用工具，该方法填补了该领域拟合优度检验的空白。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1111/sjos.70052](https://doi.org/10.1111/sjos.70052) — Optimal subsampling for estimation of dimension reduction directions
- **作者**: Xinru Jia, Weixuan Yuan, Xingqiu Zhao, Xuehu Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 575-611
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在大规模数据充分维度降维（SDR）设定下，针对基于条件密度的 rdOPG 与 dMAVE 方法迭代计算代价高的问题，研究目标为在逆概率加权（IPW）框架下最小化估计量的渐近方差-协方差矩阵迹。作者提出了最优子抽样策略，推导出显式的最优抽样概率公式，实现了计算效率与统计精度的有效权衡。理论上证明了基于最优子抽样估计量的一致性与渐近正态性，并给出了具体的渐近协方差结构。模拟与实证表明，相比均匀子抽样，该方法在大幅降低计算负担的同时提升了估计精度。该工作将 A-最优准则与 IPW 框架结合优化渐近方差的思路，对您在统计计算（大规模算法）与效率理论（渐近方差最优性）交叉方向的研究有直接参考价值。
- **关键技术**: `sufficient dimension reduction`, `optimal subsampling`, `inverse probability weighting`, `A-optimality criterion`, `dMAVE`, `asymptotic normality`
- **为什么对您有用**: 最优子抽样与 IPW 框架结合最小化渐近方差的思路，直接关联您的统计计算（大规模算法）与效率理论（渐近方差最优性）兴趣，提供了半参数降维方法在计算与效率间权衡的具体方案。

### 2. [10.1111/sjos.70006](https://doi.org/10.1111/sjos.70006) — On optimal linear prediction
- **作者**: Inge S. Helland
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 16-32
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文在线性预测设定下，研究基于模型降维的近最优预测方法，目标是最小化期望均方预测误差（EMSPE）。作者证明了在特定假设下，最优模型降维对应于偏最小二乘（PLS）回归的统计模型，并在特定条件下严格证明了PLS型预测量相较于其他预测量的优良性。进一步地，文章将两种不同模型降维的情形统一嵌入量子力学框架，实现了数理统计、化学计量学算法与量子基础的综合。对您而言，虽然量子视角较偏，但其中关于高维线性预测中模型降维与最优性的数理证明，可为高维统计与统计计算中的算法设计提供理论参考。
- **关键技术**: `linear prediction`, `model reduction`, `partial least squares (PLS)`, `expected mean squared prediction error`, `quantum mechanical setting`
- **为什么对您有用**: 文章探讨了高维线性预测中PLS算法的最优性与模型降维，其对预测误差最优性的数理统计证明可为您的统计计算与高维算法设计提供不同视角的理论参考。

### 3. [10.1111/sjos.70031](https://doi.org/10.1111/sjos.70031) — Recursive Bayesian prediction of remaining useful life for gamma degradation process under conjugate priors
- **作者**: Ancha Xu, Weiwei Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 175-206
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文针对齐次 Gamma 退化过程的单调退化数据，研究其在复杂似然结构下的贝叶斯推断与剩余寿命预测（RUL）问题。作者推导了该过程的共轭先验分布，并设计了 Gibbs 采样、离散网格采样和重要性重采样（SIR）三种算法进行后验抽样。进一步将共轭先验扩展至含异质效应的 Gamma 过程，在等间距观测下实现了参数后验分布的递归更新。基于此，提出了一种在线算法用于多系统 RUL 的实时预测。模拟与实证表明该算法在高频监测下计算效率与估计精度俱佳。对您而言，其递归贝叶斯更新与在线推断机制可为统计计算（数值方法与算法）方向提供特定结构下的算法设计参考，但与您核心的高维/因果/效率理论关联较弱。
- **关键技术**: `conjugate prior`, `Gibbs sampling`, `sampling importance resampling`, `recursive Bayesian updating`, `online prediction algorithm`, `Gamma degradation process`
- **为什么对您有用**: 递归贝叶斯更新与在线推断算法属于统计计算（数值方法与算法）范畴，可为特定结构模型的计算加速提供参考，但与您核心的高维、因果或效率理论关联较弱。

### 4. [10.1111/sjos.70045](https://doi.org/10.1111/sjos.70045) — Adaptive blind image deblurring and denoising
- **作者**: Yicheng Kang, Anik Roy, Partha Sarathi Mukherjee
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 413-441
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在空间变化模糊设定下，本文研究盲图像去模糊与去噪问题，目标是在未知且随像素位置变化的模糊机制下恢复原始图像。提出一种自适应方法，通过优化检测功效（detection power）的自适应邻域大小来识别模糊像素，并利用周围清晰像素进行去模糊与去噪。理论上，证明了随着图像分辨率提升，图像估计量具有一致性，弥补了多数现有去模糊方法缺乏渐近性质的不足。数值实验与实际数据应用表明该方法优于现有前沿方法。对您而言，其优化检测功效的思路与假设检验兴趣有微弱交叉，但整体图像处理背景与核心因果/高维/效率理论距离较远。
- **关键技术**: `adaptive neighborhood selection`, `detection power optimization`, `spatially varying blur`, `asymptotic consistency`, `nonparametric image smoothing`
- **为什么对您有用**: 优化检测功效（detection power）的机制与您在假设检验方向的兴趣有微弱方法论交叉，渐近一致性证明也涉及非参数理论；但应用背景（图像处理）与您的核心因果推断、高维统计或天文/经济/流行病学应用距离较远，方法可迁移性有限。

## 其他  *(other, 4 篇)*

### 1. [10.1111/sjos.70036](https://doi.org/10.1111/sjos.70036) — Estimating Monte Carlo variance from multiple Markov chains
- **作者**: Kushagra Gupta, Dootika Vats
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 335-363
- 相关性 5/10
- **摘要**: {
  "topic": "stat_computing",
  "summary_zh": "在多链并行 MCMC 设定下，目标是估计 Monte Carlo 平均的协方差矩阵（即方差估计），关键假设为 Markov 链满足弱混合条件。本文指出对多链 batch means (BM) 协方差估计简单取平均会在小样本下严重低估方差，尤其对慢混合链。作者扩展 Argon & Andradóttir (2006) 的工作，提出 multivariate replicated batch means (RBM) 估计量，利用并行链间信息修正低估问题；在弱混合条件下证明 RBM 强一致，且大样本偏差与方差与 BM 估计量相当。进一步证明在 MCMC 正相关存在时，RBM 估计量的负偏差严格小于平均 BM 估计量，因此小样本下 RBM 可显著优于 BM。对您而言，这为并行 MCMC 计算中的方差估计提供了有理论保证的数值方法，直接关联 statistical computing 中 MCMC 诊断与算法实现。
  "key_techniques": ["replicated batch means", "multivariate covariance estimation", "strong consistency under weak mixing", "bias comparison u

### 2. [10.1111/sjos.70042](https://doi.org/10.1111/sjos.70042) — A standardization procedure to incorporate variance partitioning‐based priors in latent Gaussian models
- **作者**: Luisa Ferrari, Massimo Ventrucci
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 364-394
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在贝叶斯潜高斯模型（LGM）设定下，研究目标是解决方差参数先验设定的解释性困难，通过方差分割（VP）重新参数化模型以赋予直观先验。传统 VP 先验多将固定效应与随机效应分开处理，本文提出一种新的标准化程序（standardization procedure），将 VP 先验扩展至同时包含两类效应的更广泛 LGM 类别。该方法的核心机制是对模型设计矩阵进行标准化，使得先验可直接施加于反映各效应相对方差贡献的参数上。该标准化程序保证了先验设定的直观解释性，并通过模拟与真实生存分析数据验证了其计算可行性。对您而言，若在统计计算或贝叶斯半参数推断中涉及 LGM 的先验选择与 MCMC/INLA 计算，此标准化技巧可提供更稳健的方差参数设定方案。
- **关键技术**: `Latent Gaussian models`, `Variance partitioning`, `Prior elicitation`, `Bayesian hierarchical models`, `Standardization procedure`
- **为什么对您有用**: 虽然核心是贝叶斯先验设定，但其对潜高斯模型方差参数的标准化处理技巧，对您在统计计算或贝叶斯半参数建模中的先验选择与算法实现有一定参考价值。

### 3. [10.1111/sjos.70030](https://doi.org/10.1111/sjos.70030) — Multivariate representations of univariate marked Hawkes processes
- **作者**: Louis Davis, Conor Kresin, Boris Baeumer, Ting Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 140-174
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究单变量标记 Hawkes 过程与多变量无标记 Hawkes 过程之间的基本联系，在标记空间离散化设定下，目标是将一维标记过程表示为多维无标记过程以简化推断。核心方法是将标记空间划分为若干区域，每个区域对应多变量表示的一个维度，从而用多变量无标记条件强度参数化原始标记过程；证明了该多变量表示在细分下渐近逼近一大类标记 Hawkes 过程，在原过程平稳时保持平稳性，且条件强度参数可识别、可解释。模拟研究给出了多变量表示因参数空间增大而引入误差的启发式界，并将方法应用于南加州地震目录数据。该文属于点过程表示理论，与您的主要兴趣方向（因果推断、效率理论、高维统计）直接关联较弱，但 Hawkes 过程在经济高频数据（order book）和流行病学（传染扩散）中有广泛应用，多变量表示的参数可识别性结果对您关注的经济理论或流行病学应用中的点过程建模或可提供参考。
- **关键技术**: `marked Hawkes process`, `multivariate Hawkes representation`, `conditional intensity identifiability`, `asymptotic approximation via mark discretization`, `stationarity preservation`
- **为什么对您有用**: 与您的主要兴趣方向关联较弱；Hawkes 过程在经济高频交易和流行病传播建模中常见，多变量表示的参数可识别性与渐近逼近界对这两个 secondary interest 场景下的点过程推断有一定参考价值。

### 4. [10.1111/sjos.70033](https://doi.org/10.1111/sjos.70033) — Estimation of generalized tail distortion risk measures with applications in reinsurance
- **作者**: Roba Bairakdar, Frédéric Godin, Mélina Mailhot, Fan Yang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 1 · pp 238-267
- 相关性 1/10 · novelty: `minor`
- **摘要**: 在极值风险设定下，本文研究广义尾部失真（GTD）风险度量的估计问题，目标 estimand 为 GTD 风险度量。作者基于该风险度量的一阶渐近展开（first-order asymptotic expansion）构建了新的估计量，该方法计算简便，且模拟实验表明其表现与现有方法相当或更优。此外，文章提出了基于 GTD 的再保险保费原则，并在车险索赔数据上进行了实证检验，通过在定价中嵌入安全附加来抵御统计不确定性。主要理论贡献在于给出了 GTD 的一阶渐近展开并据此构造估计量；对您而言，本文主要面向精算应用，与您核心的因果推断或高维效率理论关联较弱，仅渐近展开技巧对非参数理论有微弱参考。
- **关键技术**: `first-order asymptotic expansion`, `generalized tail distortion risk measure`, `reinsurance premium principle`, `extreme value estimation`
- **为什么对您有用**: 本文属于精算与风险度量领域，与您核心的因果推断、高维统计或半参数效率理论关联较弱；仅在一阶渐近展开的数学处理上与您的非参数/半参数理论兴趣有微弱交集，收益有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

