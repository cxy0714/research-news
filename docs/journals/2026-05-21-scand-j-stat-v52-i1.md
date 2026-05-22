# Scand. J. Stat. — Vol 52  Issue 1  ·  2026-05-21

- 共 18 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.12759](https://doi.org/10.1111/sjos.12759) — Revisiting the sequence symmetry analysis design
- **作者**: Jeppe Ekstrand Halkjær Madsen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 469-479
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文在数学框架下重新审视流行病学中的序列对称性分析（SSA）设计，分析 crude SR、null-effects SR 和 adjusted SR 在处方时间趋势与未测量时间不变混杂下的性质。核心发现：当治疗与结局药物之间的允许时间窗口足够小时，crude SR 可解释为 hazard ratio 的估计量，且隐式地调整了未测量时间不变混杂；而 null-effects SR 及 adjusted SR 除非治疗与结局严格独立，否则缺乏合理解释，作者建议废弃 adjusted SR。此外，crude SR 可通过 logistic regression 灵活估计协变量依赖的 HR 并检验 HR 是否随协变量变化。对您有用：该文将流行病学中常用的 self-controlled 设计形式化为因果识别问题，与您在 causal inference 中对 unmeasured confounding 下 identification 及 epidemiology 应用的兴趣直接相关，且数学处理方式可迁移至其他 self-controlled 设计的理论分析。
- **关键技术**: `sequence symmetry analysis`, `self-controlled design`, `unmeasured time-invariant confounding`, `hazard ratio identification`, `logistic regression for covariate-dependent effects`
- **为什么对您有用**: 将流行病学 SSA 设计形式化为因果识别问题，展示了 crude SR 在未测量时间不变混杂下的隐式调整性质，直接连接您在 causal inference（identification under unmeasured confounding）和 epidemiology 应用方面的兴趣，数学框架可迁移至其他 self-controlled 设计的理论分析。

### 2. [10.1111/sjos.12755](https://doi.org/10.1111/sjos.12755) — Model‐assisted analysis of covariance estimators for stepped wedge cluster randomized experiments
- **作者**: Xinyuan Chen, Fan Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 416-446
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在阶梯楔形集群随机实验(SW-CREs)的潜在结果框架下，本文定义了一类显式刻画多层次数据结构的因果 estimand，并重点讨论了三种可解释的典型成员。针对这些 estimand，作者提出了四种带有协变量调整的 ANCOVA 工作模型估计量。这些估计量属于 model-assisted 类型，即在工作模型误判时点估计仍保持一致，具备类似半参数的稳健性。在阶梯楔形随机化机制下，文章为每个估计量建立了有限总体中心极限定理。模拟与华盛顿州加速伴侣治疗流行病学数据的应用验证了其有限样本表现。对您而言，该文将有限总体推断与因果 estimand 对齐的思路，对纵向/集群因果推断及流行病学应用有直接参考价值，且 model-assisted 的稳健性设计与半参数效率理论的精神相通。
- **关键技术**: `stepped wedge cluster randomized experiments`, `potential outcomes framework`, `model-assisted ANCOVA estimator`, `covariate adjustment`, `finite population Central Limit Theorem`
- **为什么对您有用**: 直接关联您 primary interest 中的纵向因果推断与 secondary interest 中的流行病学应用；model-assisted 估计量在模型误判下的一致性对理解半参数稳健性有启发，真实流行病学数据集也可作为方法迁移的测试床。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.12735](https://doi.org/10.1111/sjos.12735) — Minimax rate of estimation for invariant densities associated to continuous stochastic differential equations over anisotropic Hölder classes
- **作者**: Chiara Amorino, Arnaud Gloter
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 185-248
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在连续观测 d 维随机微分方程 (SDE) 轨道 [0,T] 的设定下，目标是估计其平稳分布的不变密度 π，属于各向异性 Hölder 类 Σ(β₁,…,β_d)。对 d≥3，将光滑度排序 β₁≤⋯≤β_d 后，发现 minimax rate 存在相变：当 β₁>2β₂ 时速率为 T^{-2β̄/(2β̄+1)}（β̄ 为调和均值），当 β₁≤2β₂ 时速率为 T^{-2α/(2α+1)}（α 依赖于 d 及去掉最小两个光滑度后的调和均值），核心工具为核密度估计与各向异性 Hölder 类上的下界构造。对 d=2 情形，证明核估计达到 minimax 最优速率 T^{-2β̄/(2β̄+1)}，并提出对积分风险与逐点风险的自适应程序。数值实验验证了理论结论。对您有用：这是非参数理论中 minimax rate 的精细刻画，各向异性光滑度导致的相变现象与您关注的 semiparametric/nonparametric efficiency 理论直接相关，自适应程序的设计思路也可迁移。
- **关键技术**: `minimax rate estimation`, `anisotropic Hölder class`, `kernel density estimation`, `invariant density of SDE`, `L^2 pointwise risk`, `adaptive bandwidth selection`
- **为什么对您有用**: 直接推进非参数理论中 minimax rate 的精细刻画，各向异性光滑度导致的相变现象与您 primary interest 中的 semiparametric/nonparametric efficiency theory 紧密相关；自适应程序对逐点/积分风险的选择可迁移至其他非参数推断问题。

### 2. [10.1111/sjos.12758](https://doi.org/10.1111/sjos.12758) — Data‐driven estimation for multithreshold accelerated failure time model
- **作者**: Chuang Wan, Hao Zeng, Wenyang Zhang, Wei Zhong, Changliang Zou
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 447-468
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究多阈值加速失效时间（AFT）模型的估计问题，模型在不同子域上具有不同的线性形式，关键正则条件包括阈值处连续性及误差项的矩条件。核心方法分三部分：(1) 证明 modified BIC 在温和条件下对阈值数量的选择一致性，但指出其对惩罚参数的敏感性；(2) 提出 order-preserved sample-splitting 配合 cross-validation 的数据驱动准则，无需额外调参即可一致估计阈值数量及位置，并建立参数估计量的 n^{-1/2}-CAN 渐近性质；(3) 构造 score-type 检验统计量检验阈值效应是否存在，该统计量无需估计潜在阈值参数，天然适用于多阈值场景。对您而言，score-type 检验的构造思路（避免 nuisance parameter 估计）可迁移至其他 semiparametric 假设检验问题，且 order-preserved splitting 对 longitudinal/变化点设定下的 sample-splitting 有方法论借鉴价值。
- **关键技术**: `modified BIC selection consistency`, `order-preserved sample-splitting`, `cross-validation threshold selection`, `score-type test for threshold existence`, `accelerated failure time model`, `change-point asymptotic theory`
- **为什么对您有用**: 与您 primary interest 中的 hypothesis testing 直接相关——score-type 检验免于估计 nuisance threshold 参数的思路可迁移；同时 semiparametric 渐近理论的建立与您 efficiency theory / semiparametric 方向的方法论品味一致，order-preserved splitting 技巧对 longitudinal 变化点问题有参考价值。

### 3. [10.1111/sjos.12719](https://doi.org/10.1111/sjos.12719) — Minimax estimation of functional principal components from noisy discretized functional data
- **作者**: Ryad Belhakem, Franck Picard, Vincent Rivoirard, Angelina Roche
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 38-80
- 相关性 6/10 · novelty: `sharper_rate`
- **摘要**: 在函数型主成分分析（FPCA）中，针对含噪且仅在有限离散网格上观测的曲线数据，本文研究其特征函数估计量的收敛速率，设定为样本量 n 与网格点数 m 同时趋于无穷的双渐近框架。传统做法通常先平滑数据再计算 FPCA，但去噪步骤对统计性能的理论影响鲜有严格量化；本文直接基于直方图投影构造 FPCA 估计量，避免了预平滑带来的偏差。作者推导了该估计量在双渐近设定下的收敛速率，并证明了其在极小化极大意义下达到最优。核心技术工具涉及特征值与特征函数的扰动理论以及非参数下界构造。理论结果揭示了网格密度与样本量对估计精度的联合影响，并在模拟与基因组数据中验证了方法的有效性。对您有用之处在于，其双渐近框架与极小化极大最优速率的推导思路，可直接迁移至您关注的非参数理论中处理离散化与噪声交织的估计问题。
- **关键技术**: `functional principal component analysis`, `minimax convergence rates`, `double asymptotic framework`, `histogram projection`, `eigenvalue perturbation`
- **为什么对您有用**: 直接关联您 primary interest 中的非参数理论；其双渐近框架（n, m 趋于无穷）与极小化极大最优速率的严格推导，为处理离散化与噪声交织的估计问题提供了可迁移的理论工具。

### 4. [10.1111/sjos.12733](https://doi.org/10.1111/sjos.12733) — Lancaster correlation: A new dependence measure linked to maximum correlation
- **作者**: Hajo Holzmann, Bernhard Klar
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 145-169
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的依赖度量——Lancaster 相关，在双变量 Lancaster 分布下等于最大相关，在更广泛的分布下也仅略小于最大相关。与难以计算的最大相关不同，该指标允许基于秩和矩的简单估计量，且具有易于处理的渐近分布。基于渐近近似和协方差 Bootstrap 构建的置信区间展现出良好的有限样本覆盖律。在独立性检验中，基于该指标的渐近检验和置换检验的功效优于距离相关等竞争方法。特别地，在双变量正态下该指标等于 Pearson 相关绝对值，弥补了其他非参数度量的不足。对您有用：该文将非参数依赖度量与经典矩/秩估计结合，提供了清晰的渐近理论，对您在非参数理论及假设检验方面的兴趣有直接参考价值。
- **关键技术**: `Lancaster distributions`, `maximum correlation`, `rank-based estimator`, `moment-based estimator`, `covariance bootstrap`, `independence testing`
- **为什么对您有用**: 直接关联您在非参数理论与假设检验方面的兴趣；新指标在保留非参数最大相关性质的同时给出了易于计算的秩/矩估计量及清晰的渐近分布，为独立性检验提供了兼具理论可解释性与计算便利性的新工具。

### 5. [10.1111/sjos.12734](https://doi.org/10.1111/sjos.12734) — Estimation of win, loss probabilities, and win ratio based on right‐censored event data
- **作者**: Erik T. Parner, Morten Overgaard
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 170-184
- 相关性 2/10 · novelty: `weaker_assumption`
- **摘要**: 在独立右删失设定下，本文研究胜率及胜负概率的估计问题，目标估计量为胜率，关键正则条件为独立删失且无需传统的胜负概率成比例假设。作者提出了基于右删失数据的胜率与胜负概率的非参数估计量，并推导了其渐近分布与方差公式。核心机制依赖于对删失机制的适当调整，避免了以往方法中成比例假设不满足时的估计偏差。理论结果表明估计量具有渐近正态性，且模拟研究证实小样本下方差公式依然准确。实证分析使用了心血管队列数据。对您有用：该文放松了比例假设并给出渐近分布，对您在纵向/生存数据的半参数理论与流行病学队列应用中的估计量构造有参考价值。
- **关键技术**: `win ratio estimation`, `right-censored data`, `asymptotic distribution`, `nonparametric survival analysis`, `independent censoring`
- **为什么对您有用**: 放松了比例假设并推导了渐近分布，属于生存/纵向数据的数学统计与半参数估计范畴，对您在流行病学队列数据中的非参数推断方法有直接参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 6 篇)*

### 1. [10.1111/sjos.12761](https://doi.org/10.1111/sjos.12761) — A new class of nonparametric tests for second‐order stochastic dominance based on the Lorenz P–P plot
- **作者**: Tommaso Lando, Sirio Legramanti
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 480-512
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在两个非负随机变量的设定下，本文提出一类基于 Lorenz P–P plot 的二阶随机占优（SOSD）零假设非参数检验。检验统计量定义为恒等函数与 Lorenz P–P plot 之差的泛函，其中 Lorenz P–P plot 由一个分布的逆未标度 Lorenz 曲线与另一个的未标度 Lorenz 曲线复合而成。作者推导了零假设下检验统计量的上界及极限分布，并通过 bootstrap 方法近似临界值。在较温和的正则条件下证明了检验的渐近有效性，且无需经典基于 CDF 积分方法所要求的有界支撑假设，从而在部分情形下提升了检验功效。该方法可推广至分数阶随机占优族，一阶占优为其极限情形。对您有用：该工作直接推进了非参数假设检验中排序约束的 inference 理论，放松有界支撑假设的 Lorenz P–P plot 路线可迁移至您关注的 nonparametric theory 与 hypothesis testing 交叉问题。
- **关键技术**: `Lorenz P-P plot`, `second-order stochastic dominance`, `bootstrap approximation`, `unscaled Lorenz curve`, `fractional-degree stochastic order`, `nonparametric test`
- **为什么对您有用**: 直接关联您 primary interest 中的 hypothesis testing 与 nonparametric theory；放松有界支撑假设的 Lorenz P–P plot 方法为排序约束下的非参数检验提供了新工具，思路可迁移至因果推断中 treatment effect 分布比较等场景。

### 2. [10.1111/sjos.12750](https://doi.org/10.1111/sjos.12750) — Goodness‐of‐fit testing based on graph functionals for homogeneous Erdös–Rényi graphs
- **作者**: Barbara Brune, Jonathan Flossdorf, Carsten Jentsch
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 332-380
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文针对齐次 Erdős–Rényi (ER) 随机图模型，提出了基于图泛函的拟合优度检验，以检测边概率非恒定的异质替代假设，设定涵盖渐近稠密与稀疏网络。检验统计量基于图泛函（包含各类子图计数，本质为网络上的 U-统计量），作者在统一框架下推导了其极限分布，并将现有若干检验作为特例纳入。为避免渐近检验中繁琐的方差估计，提出了参数 Bootstrap 并证明其一致性。此外，针对子图计数统计量，在固定与局部替代假设下进行了功效分析。理论结果表明该检验类在局部替代下具有非平凡功效，且 Bootstrap 方法在小样本下提升了经验表现。对您有用：本文将子图计数作为 U-统计量处理的极限理论推导，以及对局部替代假设的功效分析，直接契合您在假设检验与高阶 U-统计量方面的兴趣。
- **关键技术**: `goodness-of-fit testing`, `graph functionals`, `subgraph counts`, `U-statistics`, `parametric bootstrap`, `local alternatives`
- **为什么对您有用**: 本文核心是随机图上的假设检验与子图计数（高阶 U-统计量）的极限理论，直接契合您在假设检验与高阶 U-统计量方面的 primary interests；其参数 Bootstrap 的计算方法也对统计计算方向有参考价值。

### 3. [10.1111/sjos.12743](https://doi.org/10.1111/sjos.12743) — A classical hypothesis test for assessing the homogeneity of disease transmission in stochastic epidemic models
- **作者**: Georgios Aristotelous, Theodore Kypraios, Philip D. O'Neill
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 295-313
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在将人群划分为社会群体的随机流行病模型设定下，研究疾病传播过程同质性的假设检验问题，目标是检验暴发期间是否存在显著的组内传播。检验统计量基于感染者时间排序的组别标签构建；在原假设（个体间传播同质，即无额外组内传播）下，该离散随机向量的抽样分布已知且不依赖任何模型参数。作者发展了相应的渐近理论，包括中心极限定理（CLT），使得检验实施无需进行参数估计。模拟和两个真实流行病数据集表明该检验表现优异，且计算成本低、易于实现。对您而言，该文提供了一个在随机过程模型下构建分布无关（distribution-free）假设检验的具体案例，可作流行病学应用与经典假设检验结合的参考。
- **关键技术**: `stochastic epidemic model`, `classical hypothesis testing`, `distribution-free test`, `central limit theorem`, `time-ordered group labels`
- **为什么对您有用**: 连接到您 primary interest 中的 hypothesis testing 与 secondary interest 中的 epidemiology：该文在随机流行病模型下构建了原假设下参数无关的假设检验并推导了 CLT，为您在流行病学数据中应用经典假设检验提供了具体案例与真实数据集参考。

### 4. [10.1111/sjos.12762](https://doi.org/10.1111/sjos.12762) — The effect of screening for publication bias on the outcomes of meta‐analyses
- **作者**: Haben Michael
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 513-531
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 本文研究元分析中因初步筛选发表偏倚而引发的 post-selection inference 问题，目标 estimand 为综合效应量。作者将“先进行发表偏倚检验，若不显著则执行元分析”的两步程序严格建模为条件推断问题。核心机制在于分析主阶段估计量在初步检验接受原假设条件下的条件分布与偏差。理论结果表明，在许多常见设定下，这种基于初步检验阴性结果的条件推断对主阶段估计量造成的偏差极小或可忽略。该文量化了选择性筛选步骤对最终推断的影响，对您在假设检验与选择性推断方面的数学统计兴趣有直接参考价值。
- **关键技术**: `post-selection inference`, `conditional inference`, `publication bias testing`, `selective inference`, `meta-analysis`
- **为什么对您有用**: 直接关联您的数学统计与假设检验兴趣：文章严格分析了“先检验后估计”这一经典 post-selection inference 设定下的条件偏差，为理解选择性推断的渐近性质提供了理论参考。

### 5. [10.1111/sjos.12740](https://doi.org/10.1111/sjos.12740) — Inference for all variants of the multivariate coefficient of variation in factorial designs
- **作者**: Marc Ditzhaus, Łukasz Smaga
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 270-294
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究多变量变异系数（MCV）在因子设计下的推断问题，目标是在非参数设定下对多种 MCV 变体进行全局检验及事后对比分析。作者将非参数置换检验推广至其他 MCV 变体，并针对全局原假设被拒绝后的事后分析提出了 max-type 检验。为改善该 max-type 检验的小样本表现，文章提出了一种新的 bootstrap 策略并严格证明了其渐近有效性。大量模拟与实际数据分析验证了所提方法的有限样本性质，所有方法均已在 R 包 GFDmcv 中实现。对您可能有用：该文在因子设计下非参数假设检验的 bootstrap 渐近理论处理，可为小样本推断的算法设计提供计算与理论参考。
- **关键技术**: `nonparametric permutation test`, `max-type test`, `bootstrap asymptotic validity`, `multivariate coefficient of variation`, `post hoc analysis`
- **为什么对您有用**: 涉及假设检验与非参数渐近理论，其针对小样本的 bootstrap 修正策略及 R 包实现，对您在数学统计假设检验与统计计算方面的兴趣有直接参考价值。

### 6. [10.1111/sjos.12729](https://doi.org/10.1111/sjos.12729) — Tests under simple order in one‐way ANCOVA
- **作者**: Anjana Mondal, Somesh Kumar
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 104-144
- 相关性 3/10 · novelty: `minor`
- **摘要**: 在固定效应单因素 ANCOVA 模型下，研究误差方差异质时处理效应齐性对 simple order 有序替代的检验问题。提出似然比检验（LRT）及两种基于 union-intersection 型统计量渐近分布的近似检验，并用参数 bootstrap 实现 LRT 且证明其渐近有效性。进一步给出同时置信区间构造方法，将所有检验推广至多协变量情形，并在非正态偏离下研究稳健性。模拟显示所提方法在名义水平控制和功效方面表现良好。对您而言，该文属于经典假设检验框架下有序替代检验的扩展，与您 hypothesis testing 兴趣有一定关联，但理论新颖性有限，更多是方法在 ANCOVA 异方差设定下的系统整理。
- **关键技术**: `likelihood ratio test`, `union-intersection principle`, `parametric bootstrap`, `ordered alternatives (simple order)`, `simultaneous confidence intervals`, `heteroscedastic ANCOVA`
- **为什么对您有用**: 与您 hypothesis testing 方向相关，展示了有序替代下 LRT 与 union-intersection 方法的渐近处理及 bootstrap 实现；但理论贡献偏经典设定扩展，无 sharper rate 或新效率理论，阅读收益主要在于了解有序替代检验在异方差 ANCOVA 中的系统处理方式。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12722](https://doi.org/10.1111/sjos.12722) — On maximizing the likelihood function of general geostatistical models
- **作者**: Tingjin Chu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 81-103
- 相关性 3/10 · novelty: `weaker_assumption`
- **摘要**: 在一般地统计模型（general geostatistical models）框架下，本文研究基于似然函数的两步估计的理论与计算问题，关键正则假设允许协方差函数非二次可微。核心贡献包括：(1) 证明对数似然函数全局极大值的唯一性；(2) 分析对数似然函数的凸性条件；(3) 建立两步估计的渐近理论性质，且不要求协方差函数二次可微——这放松了经典结果的光滑性假设。模拟部分比较了三种优化算法在最大化对数似然函数上的数值表现。对您而言，非二次可微协方差函数下的似然理论分析以及优化算法评估，与您在统计计算（数值优化方法）和非参数理论（弱正则条件下的估计理论）方面的兴趣有直接关联。
- **关键技术**: `two-step likelihood estimation`, `log-likelihood convexity analysis`, `non-twice differentiable covariance`, `global maximizer uniqueness`, `optimization algorithm comparison`
- **为什么对您有用**: 非二次可微协方差函数下似然理论及优化算法评估，直接关联您在统计计算（数值优化）和非参数理论（弱正则条件）方面的兴趣，可借鉴其弱假设下证明唯一性与凸性的技术路线。

## 其他  *(other, 4 篇)*

### 1. [10.1111/sjos.12738](https://doi.org/10.1111/sjos.12738) — Adjusted location‐invariant U‐tests for the covariance matrix with elliptically high‐dimensional data
- **作者**: Kai Xu, Yeqing Zhou, Liping Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 249-269
- 相关性 10/10 · novelty: `new_theory`
- **摘要**: 在高维椭圆分布设定下，本文研究协方差矩阵的位置不变 U-检验（基于经典 John-Nagao 和 Ledoit-Wolf 检验的修正），目标是检验协方差矩阵结构（如球性）。作者发现经典 U-检验在一般椭圆总体下因坐标间高阶相关性（如峰度偏移）而导致 size 严重失真。为此，通过引入对高阶依赖性的修正项，提出调整后的位置不变 U-检验，并给出计算高效的等价统计量形式。在维度与样本量以任意方式趋于无穷时，推导了新检验在椭圆分布及更广泛模型下的通用渐近零分布，并分析了其 power 性质。对您有用：直接推进了您关注的“高维假设检验”与“高阶 U-统计量”交叉方向，提供了椭圆分布下协方差检验的 size 校正与渐近理论。
- **关键技术**: `high-dimensional covariance testing`, `U-statistics`, `elliptical distribution`, `location-invariant test`, `asymptotic null distribution`, `John-Nagao test`
- **为什么对您有用**: 论文核心是高维椭圆分布下的 U-检验修正，完美契合您在“高维统计假设检验”与“高阶 U-统计量”两个 primary interests 的交叉点；其处理高阶相关性的修正技巧和通用渐近分布推导对您自己的理论研究有直接参考价值。

### 2. [10.1111/sjos.12711](https://doi.org/10.1111/sjos.12711) — On a computable Skorokhod's integral‐based estimator of the drift parameter in fractional SDE
- **作者**: Nicolas Marie
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 1-37
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在由 Hurst 指数为 H 的分数布朗运动驱动的随机微分方程 (SDE) 设定下，基于多组（可能相依）解轨道的观测，研究漂移参数的 Skorokhod 积分型最小二乘 (LS) 估计量。当 H > 1/2 时，作者直接建立了该 LS 估计量的收敛性结果。当 H ≤ 1/2 时，由于 Skorokhod 积分无法直接从离散数据计算，作者提出了一种可计算的近似估计量，并严格证明了该近似估计量的收敛性质。核心方法利用了分数微积分工具与对不可直接观测泛函的数值逼近策略。主要理论贡献是为分数 SDE 的漂移参数估计提供了具备收敛保证的可计算方案。对您可能有用之处在于：其处理“不可计算泛函（Skorokhod 积分）的数值逼近”思路，可为统计计算中类似不可观测泛函的算法设计提供参考。
- **关键技术**: `Skorokhod integral`, `fractional Brownian motion`, `least squares estimation`, `stochastic differential equations`, `computable approximation`
- **为什么对您有用**: 虽然核心是 SDE 参数估计，但其处理“不可直接计算统计量（Skorokhod 积分）的数值逼近”思路，对您在统计计算（数值方法与算法）方向处理类似不可观测泛函的近似计算有一定借鉴价值。

### 3. [10.1111/sjos.12751](https://doi.org/10.1111/sjos.12751) — Tobit models for count time series
- **作者**: Christian H. Weiß, Fukang Zhu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 381-415
- 相关性 0/10
- **摘要**: {
  "topic": "other",
  "summary_zh": "本文针对计数时间序列（如 INARMA 和 INGARCH）提出"Tobit 方法"，旨在实现近似条件线性的同时允许负自相关函数（ACF），克服了现有 softplus 链接仅适用于无界计数 INGARCH 的局限。核心研究了 Skellam-Tobit INGARCH 模型，推导了其平稳性条件及矩的近似计算公式。参数估计方面，提出了最大似然估计（MLE）与删失最小绝对偏差（censored LAD）估计，并进行了相应的模拟验证。该方法可进一步扩展至其他离散分布、INAR 模型及有界计数情形。对您而言，本文的删失 LAD 数值计算及离散时间序列的平稳性推导可为统计计算与数理统计兴趣提供边际参考，但整体偏参数化建模，与半参数效率或高维理论的核心方向距离较远。",
  "key_techniques": [
    "Tobit approach",
    "INGARCH models",
    "censored least absolute deviations",
    "Skellam distribution",
    "maximum likelihood estimation"
  ],
  "why_relevant": "本文主要属于参数化计数时间序列建模，与您核心的半参数/高维/

### 4. [10.1111/sjos.12748](https://doi.org/10.1111/sjos.12748) — Cutoff for a class of auto‐regressive models with vanishing additive noise
- **作者**: Balázs Gerencsér, Andrea Ottolini
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 1 · pp 314-331
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究欧氏空间上一类带消失加性噪声的自回归马尔可夫链的收敛速率，模型设定为每步随机选取一个坐标并用其他坐标的带噪衰减加权平均替换。核心机制利用了该模型与 de Finetti 部分可交换数据贝叶斯推断方案的联系，通过分析转移矩阵的谱隙与特征结构来精确刻画混合时间。主要理论贡献是证明了当参数 n 趋于无穷（对应噪声趋于零）时，马尔可夫链的收敛呈现 cutoff 现象，即混合时间在临界点发生急剧相变。该结果给出了此类自回归过程收敛的精确渐近阶，明确了噪声消失速度与收敛相变点之间的定量关系。对您而言，虽然本文侧重概率论，但其对马尔可夫链混合时间的精确刻画和谱分析方法，可为 MCMC 采样收敛性或贝叶斯序贯更新算法的理论分析提供数学工具借鉴。
- **关键技术**: `cutoff phenomenon`, `Markov chain mixing time`, `spectral gap analysis`, `auto-regressive process`, `de Finetti exchangeability`
- **为什么对您有用**: 本文属于数学统计与概率论交叉，虽然不直接涉及因果推断或半参数效率，但其对马尔可夫链混合时间 cutoff 现象的精确刻画，可为研究 MCMC 采样收敛或贝叶斯推断算法的理论性质提供谱分析与收敛速率的数学工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

