# J. Econometrics — Vol 255  ·  2026-05-18

- 共 11 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106250](https://doi.org/10.1016/j.jeconom.2026.106250) — Transfer estimates for causal effects across heterogeneous sites
- **作者**: Konrad Menzel
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106250
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在多站点异质性总体设定下，研究如何将实验站点的因果效应外推至仅有基线数据的“目标”站点，目标参数为条件平均处理效应（CATE）。方法将基线视为函数数据，以捕捉未观测站点混杂与观测属性的交互作用，并在有限维特征空间中求解预测问题。采用基于设计的视角，评估给定有限站点选择下预测器的表现。理论上构造了最优预测基底，并给出了估计的 CATE 相对于约束最优总体预测器的非参数收敛速率。实证部分利用五个多站点 RCT 的条件现金转移支付（CCT）数据量化了外推收益。该文将函数数据视角引入因果外推，其非参数收敛率分析与最优特征选择对您关注的因果推断（transportability）与半参数/非参数理论交叉研究有直接参考价值，且附带经济学多站点 RCT 数据集。
- **关键技术**: `treatment effect transportability`, `functional data perspective`, `optimal basis construction`, `nonparametric convergence rates`, `design-based inference`, `multi-site RCT`
- **为什么对您有用**: 直击因果推断中的外部有效性/跨站点外推问题，结合了非参数收敛率分析（primary: nonparametric theory）与多站点 RCT 经济数据集（secondary: economic theory），对研究异质性总体下的因果识别与估计极具启发。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106247](https://doi.org/10.1016/j.jeconom.2026.106247) — Reduced rank multivariate spatial autoregressive model for large-scale networks
- **作者**: Tianyi Zhu, Dan Pu, Yingying Ma, Danyang Huang, Wei Lan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106247
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在多变量空间自回归（MSAR）模型设定下，当响应维度发散时，空间影响矩阵的未知参数量以 O(p^2) 速率增长，导致估计困难。本文对该矩阵施加低秩结构，提出降秩 MSAR 模型以实现维度缩减与可解释性提升。为克服拟极大似然估计（QMLE）的高计算成本，提出计算更高效的最小二乘估计量（LSE）。在网络规模与响应维度同时发散的设定下，严格建立了 LSE 的渐近性质，并提出信息准则实现秩选择的一致性。该文的高维渐近理论与计算优化策略对您在 high-dimensional statistics 与 statistical computing 方向的研究有直接参考价值，同时其网络计量模型与支付平台数据集也契合 econ_theory 兴趣。
- **关键技术**: `reduced-rank structure`, `multivariate spatial autoregressive model`, `least squares estimator`, `diverging dimension asymptotics`, `rank selection consistency`
- **为什么对您有用**: 涉及高维发散维度下的渐近理论推导与计算优化（LSE 替代 QMLE），直接契合您在 high-dimensional statistics 和 statistical computing 的兴趣；同时网络计量模型与实证数据集也符合 econ_theory 子方向。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106241](https://doi.org/10.1016/j.jeconom.2026.106241) — Using spatial modeling to address covariate measurement error
- **作者**: Susanne M. Schennach, Vincent Starck
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106241
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在空间数据设定下，本文提出利用邻近观测作为重复测量来解决协变量测量误差的识别与估计问题，允许非经典误差且无需先验分布假设。核心机制是通过控制观测间的随机距离，利用算子对角化方法建立非线性模型的可识别性。估计量的实现结合了筛半参数极大似然、第一步核估计与模拟方法。该方法突破了传统测量误差校正对经典误差或强参数假设的依赖。实证部分应用于评估非洲前殖民政治结构对当前经济发展的影响。对您有用：该文将算子对角化与筛半参数极大似然结合的思路，对您在半参数理论及因果推断中处理测量误差与不可观测混淆具有直接的方法论借鉴价值。
- **关键技术**: `sieve semiparametric maximum likelihood`, `operator diagonalization`, `nonclassical measurement error`, `kernel estimation`, `spatial repeated measurements`
- **为什么对您有用**: 该文将算子对角化与筛半参数极大似然结合的思路，对您在半参数理论及因果推断中处理测量误差与不可观测混淆具有直接的方法论借鉴价值；同时其经济史应用数据集对经济理论兴趣有参考意义。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1016/j.jeconom.2026.106249](https://doi.org/10.1016/j.jeconom.2026.106249) — Latent factor analysis in short panels
- **作者**: Alain-Philippe Fortin, Patrick Gagliardini, Olivier Scaillet
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106249
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在短面板 (n→∞, T 固定) 的潜在因子模型中，本文研究在误差协方差矩阵为对角阵（不要求球面性或高斯性）的半参数设定下，因子个数检验及参数估计的渐近理论。采用伪极大似然方法推导了潜在因子与误差协方差矩阵估计量的渐近分布。基于似然比统计量，构造了检验因子个数的渐近一致最优势不变（AUMPI）检验。该检验的推导核心依赖于正态变量正定二次型确保单调似然比性质的不等式。实证部分利用美股月度收益面板数据，在短期的牛熊市区间中分离了系统性与特质性风险。该文对因子个数的 AUMPI 检验推导及短面板下的半参数伪似然理论，直接契合您在假设检验与半参数理论方面的研究兴趣。
- **关键技术**: `pseudo maximum likelihood`, `asymptotically uniformly most powerful invariant (AUMPI) test`, `monotone likelihood ratio property`, `positive definite quadratic forms`, `short panel factor model`, `latent factor analysis`
- **为什么对您有用**: 本文推导的因子个数 AUMPI 检验及短面板半参数伪似然理论，直接契合您在假设检验与半参数理论方面的 primary interest；同时其实证应用也符合您在经济理论（资产定价因子模型）方面的 secondary interest。

### 2. [10.1016/j.jeconom.2026.106234](https://doi.org/10.1016/j.jeconom.2026.106234) — The information matrix test for Gaussian mixtures
- **作者**: Dante Amengual, Gabriele Fiorentini, Enrique Sentana
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106234
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在有限高斯混合模型设定下，本文研究信息矩阵（IM）检验在不可完全观测数据下的渐近性质与有限样本表现。利用EM原理，证明不完全数据下的IM检验矩等价于完全数据对应矩的条件期望，并导出经参数估计抽样变异性调整的渐近协方差矩阵解析式。采用参数Bootstrap克服IM检验常见的有限样本过度拒绝问题，模拟显示其具有可靠水平和良好功效。实证表明3成分高斯混合能准确拟合Penn World Tables跨国人均收入分布。对您有用：该文将经典设定检验拓展至隐变量模型，其渐近协方差推导思路对您在hypothesis testing与efficiency theory方面的研究有理论借鉴，且Penn World Tables数据对economic theory应用有参考价值。
- **关键技术**: `Information Matrix test`, `EM principle`, `Gaussian mixture models`, `asymptotic covariance adjustment`, `parametric bootstrap`
- **为什么对您有用**: 直接关联您primary interest中的hypothesis testing（信息矩阵检验的渐近协方差推导），同时涉及您secondary interest中economic theory的Penn World Tables数据集，对隐变量模型设定检验的数理推导和经济实证均有参考价值。

### 3. [10.1016/j.jeconom.2026.106240](https://doi.org/10.1016/j.jeconom.2026.106240) — LASSO inference for high dimensional predictive regressions
- **作者**: Zhan Gao, Ji Hyung Lee, Ziwei Mei, Zhentao Shi
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106240
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维预测回归设定下，目标是对局部单位根非平稳回归变量的系数进行假设检验，需同时克服 LASSO 收缩偏差与 Stambaugh 偏差。本文提出 IVX-desparsified LASSO (XDlasso) 估计量，结合去稀疏化与工具变量投影（IVX）机制，同步消除上述两种偏差。该方法无需预先区分非平稳与平稳回归变量，理论上证明了 XDlasso 的渐近正态性，从而恢复了基于 t 统计量的标准推断程序。蒙特卡洛模拟验证了有限样本性质，基于 FRED-MD 数据库的实证分析了美股收益与通胀的可预测性。该文将高维去偏推断拓展至非平稳时间序列，对您的高维统计推断与假设检验（primary）研究有直接参考价值，同时提供了经济预测模型与数据集（secondary）的应用范例。
- **关键技术**: `desparsified LASSO`, `IVX instrumentation`, `Stambaugh bias correction`, `high-dimensional inference`, `local unit root`
- **为什么对您有用**: 直接连接到您的高维统计推断与假设检验（primary）兴趣，展示了如何在非平稳时间序列中恢复去偏 LASSO 的渐近正态性；同时提供了经济预测模型与 FRED-MD 数据集（secondary）的应用范例。

## 经济理论 / 应用  *(econ_theory, 5 篇)*

### 1. [10.1016/j.jeconom.2026.106218](https://doi.org/10.1016/j.jeconom.2026.106218) — Consistency, distributional convergence, and optimality of time-varying parameters in score-driven models
- **作者**: Eric Beutner, Yicong Lin, Andre Lucas
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106218
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在观测驱动的 score-driven 时间序列模型设定下，研究模型存在严重误设时滤波时变参数路径的渐近性质。采用 in-fill 渐近框架，证明即使在误设下，滤波路径仍依概率收敛至 Kullback-Leibler (KL) 最优时变参数路径。进一步推导了滤波误差的分布收敛结果，并给出了最小化渐近滤波误差方差的最优滤波器形式，该最优滤波器仍具备 score-driven 特征。理论结果推广了已有发现，并被应用于时变尾部形状模型、动态 Copula 和时变回归模型。基于渐近理论，文章构建了量化滤波路径不确定性的逐点区间，并应用于 Pfizer 日内对数收益率的波动率路径。对您有用：该文在误设下推导 KL 最优收敛与分布收敛的框架，为经济理论中的时变参数推断提供了严谨的数学统计基础，其处理模型误设的渐近逻辑可借鉴至半参数效率理论或因果推断中关于稳健估计的思考。
- **关键技术**: `score-driven models`, `in-fill asymptotics`, `Kullback-Leibler optimality`, `distributional convergence`, `misspecification robust`, `time-varying parameters`
- **为什么对您有用**: 该文属于经济理论方向，其严谨的 in-fill 渐近与误设下分布收敛推导契合您对数学统计与渐近效率的兴趣；处理模型误设下 KL 最优路径的逻辑，可为半参数推断或因果推断中稳健估计的假设放松提供方法论借鉴。

### 2. [10.1016/j.jeconom.2026.106245](https://doi.org/10.1016/j.jeconom.2026.106245) — Mixture matrix-valued autoregressive model
- **作者**: Fei Wu, Kung-Sik Chan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106245
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 针对矩阵值时间序列数据中线性MAR模型无法捕捉非线性体制转换（如经济衰退与扩张）的问题，提出混合矩阵自回归（MMAR）模型。模型通过混合分布刻画不同体制下的动态关系，并采用EM算法进行极大似然估计（MLE）。理论上证明了估计量的一致性与渐近正态性。模拟与实证（经济/金融数据）验证了方法在识别体制转换和参数估计上的有效性。对您有用：该文将矩阵代数与EM算法结合，其渐近理论推导和矩阵计算方法可直接迁移至您关注的统计计算（矩阵算法）与经济理论（体制转换模型）交叉研究。
- **关键技术**: `matrix autoregressive model`, `EM algorithm`, `maximum likelihood estimation`, `regime switching`, `asymptotic normality`
- **为什么对您有用**: 匹配您在统计计算（矩阵算法、EM迭代）和经济理论（经济模型、应用）方面的兴趣；其矩阵值数据的渐近理论推导对高维矩阵序列研究有参考价值。

### 3. [10.1016/j.jeconom.2026.106251](https://doi.org/10.1016/j.jeconom.2026.106251) — Implicit score-driven filters for time-varying parameter models
- **作者**: Rutger-Jan Lange, Bram van Os, Dick van Dijk
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106251
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在时变参数模型的观测驱动框架下，本文提出隐式得分驱动（ISD）更新机制，目标是在对数观测密度极大化中加入加权 L2 惩罚以实现参数动态更新。核心机制将 ISD 表述为隐式随机梯度下降，并证明经典的显式得分驱动（ESD）模型仅是其在对数似然线性近似下的特例。通过保留完整的对数密度信息，ISD 将 ESD 的局部优良性质扩展至全局。在对数凹密度（无论是否正确设定）下，ISD 滤波器对所有学习率均稳定，且每一步更新在均方误差（MSE）意义下对（伪）真实参数具有收缩性。模拟与金融、宏观经济实证展示了方法的有效性。对您而言，该文将隐式优化与时间序列参数更新结合，其全局稳定与 MSE 收缩性的严格证明对统计计算（隐式更新算法）与经济理论（时变参数模型）的交叉研究有直接参考价值。
- **关键技术**: `implicit stochastic-gradient update`, `score-driven models (GAS)`, `L2-penalized log-density`, `log-concave density`, `MSE contractivity`, `observation-driven filter`
- **为什么对您有用**: 属于经济理论（时变参数模型）与统计计算（隐式随机梯度算法）的交叉；其全局稳定性和 MSE 收缩性的严格证明，对您在动态模型中的数值算法设计有借鉴意义。

### 4. [10.1016/j.jeconom.2026.106244](https://doi.org/10.1016/j.jeconom.2026.106244) — Integrated variance estimation for assets traded in multiple venues
- **作者**: Gustavo Fruet Dias, Karsten Schweikert
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106244
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多交易场所同时交易同一资产的高频数据设定下，研究乘性市场微观结构噪声（fragmentation noise）下的积分方差估计问题。指出传统已实现方差及现有噪声稳健估计量在此噪声下不一致。提出两步估计法：第一步利用漂移项估计消除 fragmentation noise，第二步根据是否含跳跃或加性噪声，应用已实现方差、双幂变差或预平均估计量。推导了不同设定下两步估计量的渐近分布，仿真与 DJIA 实证表明其优于传统单变量估计量。对您可能有用：该文属于经济理论中的金融计量模型与应用，其两步去噪与渐近分布推导思路可为处理复杂噪声结构的半参数估计提供参考。
- **关键技术**: `integrated variance estimation`, `multiplicative microstructure noise`, `two-step estimation`, `pre-averaging estimator`, `bipower variation`, `asymptotic distribution`
- **为什么对您有用**: 契合您在 econ_theory 上的次级兴趣（模型与应用），其两步去噪与渐近理论推导对处理复杂噪声结构的半参数/非参数估计有方法学参考价值。

### 5. [10.1016/j.jeconom.2026.106235](https://doi.org/10.1016/j.jeconom.2026.106235) — Robust econometrics for growth-at-risk
- **作者**: Tobias Adrian, Yuya Sasaki, Yulong Wang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 255 · pp 106235
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究 Growth-at-Risk (GaR) 框架下的尾部估计问题，目标是在放松现有方法中常数 Pareto 指数假设的条件下估计条件分布的尾部。作者提出了一种基于极值理论的稳健计量方法，允许 Pareto 指数随协变量变化，构建了相应的尾部分位数估计量，并严格证明了其渐近性质与有效性。模拟结果显示该估计量在预测精度上持续优于现有方法；长期 GaR 实证分析也表明其能更精准地捕捉金融异常。对您而言，该文不仅提供了经济理论 (GaR) 的应用与数据集，其放松常数尾部指数的非参数极值估计思路也可迁移至其他半/非参数理论场景。
- **关键技术**: `extreme value theory`, `varying Pareto exponent`, `tail index estimation`, `quantile regression`, `Growth-at-Risk`
- **为什么对您有用**: 契合您的 secondary interest 'economic theory (application, model)'，同时其放松常数尾部指数假设的非参数极值估计思路对您关注的 nonparametric theory 有方法学借鉴意义。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

