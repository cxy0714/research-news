# Scand. J. Stat. — Vol 51  Issue 4  ·  2026-05-21

- 共 16 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1111/sjos.12721](https://doi.org/10.1111/sjos.12721) — Mahalanobis balancing: A multivariate perspective on approximate covariate balancing
- **作者**: Yimin Dai, Ying Yan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1450-1471
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在因果推断的协变量平衡加权框架下，本文针对 exact balancing 在重叠差或高维时不可行、而 approximate balancing 的阈值参数难选且矩约束难以全面刻画分布差异的问题，提出 Mahalanobis balancing 方法。核心机制是用二次约束（Mahalanobis 距离）控制整体协变量不平衡度，仅需单一阈值参数且可通过简单程序选取；其对偶问题为范数正则化回归，并由此建立了与倾向得分模型的显式联系。理论上推导了所提估计量的渐近性质，讨论了高维情形下的扩展，并通过大量模拟与现有平衡方法做了对比。对您有用之处在于：该工作将平衡加权与 PS 模型通过 duality 统一，为高维因果推断中的协变量平衡提供了新的正则化视角，且高维讨论部分与您的高维统计兴趣直接交汇。
- **关键技术**: `approximate covariate balancing`, `Mahalanobis distance quadratic constraint`, `dual norm-regularized regression`, `propensity score duality`, `high-dimensional balancing weights`
- **为什么对您有用**: 直接推进因果推断中协变量平衡加权的方法论，其对偶性与 PS 模型的理论连接以及高维扩展与您在因果推断（平衡加权/倾向得分）和高维统计两个 primary interest 均有交叉，可借鉴其正则化对偶思路。

### 2. [10.1111/sjos.12714](https://doi.org/10.1111/sjos.12714) — Asymptotic properties of resampling‐based processes for the average treatment effect in observational studies with competing risks
- **作者**: Jasmin Rühl, Sarah Friedrich
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1506-1532
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在观察性研究的竞争风险时间-事件设定下，目标是基于 g-formula 估计的平均处理效应（ATE）随机过程的渐近性质，关键假设包括无未测量混杂与竞争风险的因果结构。由于 g-formula 对应随机过程的渐近分布复杂、无法直接用于构造置信带，本文研究了三种重抽样方法（非参数 bootstrap 及另两种替代方案）的大样本性质，并严格证明了其在竞争风险设定下的渐近有效性。理论证明依托经验过程理论与计数过程的鞅方法，建立了重抽样过程与原估计量影响函数驱动过程的一致渐近等价性。实证分析展示了体力活动对膝关节置换风险的影响。对您有用：该工作将 g-formula 与竞争风险结合，其重抽样渐近理论对您在纵向因果推断中处理复杂事件结构时的推断方法有直接参考价值。
- **关键技术**: `g-formula`, `nonparametric bootstrap`, `competing risks`, `stochastic process`, `time-simultaneous confidence bands`, `empirical process theory`
- **为什么对您有用**: 连接您 primary interest 中的因果推断（纵向/时间-事件设定下 ATE 估计）与数学统计（渐近分布理论），提供了竞争风险下 g-formula 重抽样推断的严格渐近保证，可迁移到更一般的纵向因果推断场景。

### 3. [10.1111/sjos.12753](https://doi.org/10.1111/sjos.12753) — Some approximations to the path formula for some nonlinear models
- **作者**: Christiana Kartsonaki
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1433-1449
- 相关性 7/10 · novelty: `minor`
- **摘要**: 本文研究在存在中间变量的情形下，将暴露对结局的总效应分解为直接与间接两部分的路径公式（path formula），在线性最小二乘回归中该分解有精确形式，作者进而探讨 logistic 回归与比例风险（Cox PH）模型下的近似分解。设定为经典中介分析框架，关键假设为模型的参数化正确指定及无未测混杂。核心机制是利用线性模型中路径系数的乘积分解思想，在非线性链接函数下推导近似表达式，比较不同近似策略的偏差来源与量级。主要结果表明，logistic 与 Cox 模型下路径公式不再精确成立，近似误差依赖于基线风险、暴露与中介的效应大小及事件概率。对您而言，该文提供了非线性模型中介效应分解的经典近似视角，但方法学 novelty 有限，可作为 mediation 在生存/二值结局场景下的入门参考。
- **关键技术**: `path analysis decomposition`, `mediation effect decomposition`, `logistic regression approximation`, `Cox proportional hazards approximation`, `indirect effect via intermediate variable`
- **为什么对您有用**: 与您 primary interest 中的 causal inference (mediation) 直接相关，但该文仅讨论参数模型下的近似分解，未涉及 semiparametric efficiency 或 sensitivity analysis，收益主要是了解非线性模型中介分解的经典近似思路与局限。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12747](https://doi.org/10.1111/sjos.12747) — Structure learning for continuous time Bayesian networks via penalized likelihood
- **作者**: Tomasz Ca̧kała, Błażej Miasojedow, Wojciech Rejchel, Maryia Shpak
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1707-1729
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究连续时间贝叶斯网络（CTBN）的结构学习问题，目标是在图依赖结构未知时，通过惩罚似然方法恢复真实的网络拓扑。作者提出基于惩罚似然的估计算法，并在温和的正则条件下证明了该算法能以高概率（with high probability）正确识别图的依赖结构，即实现了模型选择一致性。数值研究验证了所提程序在有限样本下的表现。对您有用：该文将高维惩罚似然与模型选择一致性理论应用于连续时间随机过程，对您在**高维统计**中的结构学习/变量选择理论，以及**因果推断**中连续时间因果发现有直接参考价值。
- **关键技术**: `continuous time Bayesian networks`, `penalized likelihood`, `structure learning`, `model selection consistency`, `graph recovery`
- **为什么对您有用**: 将高维惩罚似然与模型选择一致性理论应用于连续时间随机过程，对您在**高维统计**中的结构学习/变量选择理论，以及**因果推断**中连续时间因果发现有直接参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1111/sjos.12756](https://doi.org/10.1111/sjos.12756) — Asymptotically faster estimation of high‐dimensional additive models using subspace learning
- **作者**: Kejun He, Shiyuan He, Jianhua Z. Huang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1587-1618
- 相关性 9/10 · novelty: `sharper_rate`
- **摘要**: 在高维可加模型设定下，目标是通过学习各可加成分函数共享的自适应子空间来减少待估函数数量，从而克服维数灾难。作者为前期提出的 reduced additive model 补充了渐近理论，证明在子空间近似误差足够小的条件下，即使模型仅为近似，基于子空间学习的估计量也能获得比传统无子空间学习估计更快的收敛速率。同时证明了该方法能一致识别相关预测变量（variable selection consistency）。该理论结果解释了前期数值实验中的优越表现，为高维非参数估计中的降维策略提供了严格的收敛速率保证。对您有用：直接推进了高维非参数理论中的收敛速率研究，子空间近似误差与收敛速率的权衡分析对您在 semiparametric/nonparametric efficiency 和 high-dimensional statistics 方面的工作有直接参考价值。
- **关键技术**: `high-dimensional additive model`, `subspace learning`, `convergence rate`, `variable selection consistency`, `approximation error bound`
- **为什么对您有用**: 直接推进了高维非参数理论中的收敛速率研究，子空间近似误差与收敛速率的权衡分析对您在 semiparametric/nonparametric efficiency 和 high-dimensional statistics 方面的工作有直接参考价值。

### 2. [10.1111/sjos.12730](https://doi.org/10.1111/sjos.12730) — Confidence intervals in monotone regression
- **作者**: Piet Groeneboom, Geurt Jongbloed
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1749-1781
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在单调回归（isotonic regression）设定下，目标是构造回归函数的逐点置信区间；关键正则假设为回归函数单调且满足一定光滑条件。已知基于非参数 LSE 的普通 bootstrap 不一致，本文证明对 LSE 做核光滑得到的 SLSE（Smoothed Least Squares Estimator）可支撑 n^{-1/2}-一致的 smoothed bootstrap，并推导了 SLSE 的逐点渐近分布。文中比较了 smoothed bootstrap 置信区间与基于 Nadaraya-Watson 估计量的区间，研究了 Studentization 的效果，并给出了自动带宽选择方法（修正了 Sen & Xu 2015）。最后将类似方法推广到 current status 模型，改进了 Groeneboom & Hendrickx 2018 的结果。对您有用：这是 shape-constrained nonparametric inference 的经典推进，SLSE + smoothed bootstrap 的技术路线可直接迁移到您关注的 nonparametric/semiparametric 理论中 shape constraint 下的 inference 问题。
- **关键技术**: `Smoothed Least Squares Estimator (SLSE)`, `smoothed bootstrap consistency`, `isotonic regression`, `Studentization`, `current status model`, `automatic bandwidth selection`
- **为什么对您有用**: 直接推进您 primary interest 中的 nonparametric theory：解决了单调约束下 bootstrap 不一致这一经典难题，SLSE + smoothed bootstrap 的理论框架可迁移到其他 shape-constrained semiparametric 模型的 inference；current status 模型的讨论也与流行病学（secondary）中的区间删失数据因果推断有关联。

### 3. [10.1111/sjos.12724](https://doi.org/10.1111/sjos.12724) — Gradient‐based approach to sufficient dimension reduction with functional or longitudinal covariates
- **作者**: Ming‐Yueh Huang, Kwun Chuen Gary Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1567-1586
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究实值响应与函数型或纵向协变量回归中的充分降维（SDR）问题，目标是在仅依赖平滑性条件下估计充分降维子空间。传统逆回归类方法依赖线性条件假设，本文提出基于条件分布函数梯度的估计量，避开了该线性假设。实际计算中，该估计量可通过标准的函数型主成分分析（FPCA）算法实现。理论证明其有效性仅需总体参数的平滑性条件，属于半参数/非参数降维框架。模拟与实证分析验证了方法的有效性。对您而言，该文在纵向协变量降维中放松了线性假设，其基于梯度的非参数技巧与 FPCA 计算方案可为纵向因果推断中的高维协变量处理提供方法迁移。
- **关键技术**: `sufficient dimension reduction`, `gradient of conditional distribution function`, `functional principal component analysis`, `inverse regression avoidance`, `longitudinal covariates`
- **为什么对您有用**: 本文处理纵向/函数型协变量的降维并放松了传统逆回归的线性条件，与您关注的纵向因果推断及半参数理论直接相关；其基于梯度的非参数降维思路和 FPCA 计算算法可为高维纵向数据的因果推断提供协变量处理上的方法迁移。

### 4. [10.1111/sjos.12739](https://doi.org/10.1111/sjos.12739) — Bayesian mixture models (in)consistency for the number of clusters
- **作者**: Louise Alamichel, Daria Bystrova, Julyan Arbel, Guillaume Kon Kam King
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1619-1660
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 在有限混合模型设定下，本文研究贝叶斯非参数先验对聚类数目的后验不一致性问题，关键正则假设为真实分量数有限且先验为 Gibbs-type processes 及其有限维表示。已知 Dirichlet process 与 Pitman-Yor process 混合模型在真实聚类数有限时后验不一致，作者将此结果推广至更广泛的 Gibbs-type 先验类（含 Dirichlet multinomial、Pitman-Yor multinomial、normalized generalized gamma multinomial processes），证明它们同样无法恢复真实聚类数。核心证明利用了 Gibbs-type 先验下后验聚类数目的渐近行为分析。作者进一步表明，针对 Dirichlet process 提出的 postprocessing 算法可推广至一般 Gibbs-type 模型，并恢复聚类数的一致估计。对您而言，此文在非参数理论方面提供了贝叶斯非参数模型后验一致性的系统刻画，虽与半参数效率方向不同，但模型选择一致性的理论框架可作参考。
- **关键技术**: `Gibbs-type processes`, `posterior inconsistency`, `Dirichlet process mixture`, `Pitman-Yor process`, `postprocessing algorithm`, `finite-dimensional representation`
- **为什么对您有用**: 与您 primary interest 中的非参数理论相关——本文系统刻画了贝叶斯非参数混合模型聚类数后验不一致的统一框架并提供修正方法；若您关注非参数模型选择的理论性质，此文提供了贝叶斯视角的补充，但与您核心的半参数效率/因果推断方向距离较远。

### 5. [10.1111/sjos.12731](https://doi.org/10.1111/sjos.12731) — Estimation of the conditional tail moment for Weibull‐type distributions
- **作者**: Yuri Goegebeur, Armelle Guillou, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1782-1815
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究 Weibull 型分布在极端水平下的条件尾部矩估计问题，假设分布尾部满足二阶正规变换条件。提出一种两步估计法：首先在中间水平构造条件尾部矩的估计量，随后利用 Weibull 尾部参数进行外推至极端分位数。在合适的正规条件下，严格推导了中间水平估计量与外推估计量的渐近正态性与收敛速率。核心工具依赖于极值理论中的尾部外推技术与二阶条件。仿真实验验证了有限样本表现，并应用于风速与空气污染真实数据。对您而言，本文展示了非参数极值理论中渐近分析的严谨推导，但与您关注的半参数效率界或因果推断距离较远。
- **关键技术**: `extreme value theory`, `Weibull-type distribution`, `conditional tail moment`, `tail extrapolation`, `second-order regular variation`
- **为什么对您有用**: 本文属于非参数极值理论，与您 primary interest 中的非参数理论有微弱交集（渐近性质推导），但核心是尾部外推而非半参数效率或因果推断；空气污染数据的应用也仅是描述性展示，缺乏因果或深度流行病学建模。

### 6. [10.1111/sjos.12746](https://doi.org/10.1111/sjos.12746) — Conditional quasi‐likelihood inference for mean residual life regression with clustered failure time data
- **作者**: Rui Huang, Liuquan Sun, Liming Xiang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1685-1706
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 在聚类失效时间数据下，本文提出 frailty 比例均值剩余寿命（MRL）回归模型，目标参数为回归系数，关键假设是 MRL 与协变量成比例且簇内相关由 frailty 刻画但分布无需指定。方法核心是条件拟似然推断：用随机过程与 IPCW 构建估计方程，通过惩罚拟似然处理簇内相关从而避免指定 frailty 分布，并在 IPCW 中采用 Buckley–James 估计量以允许依赖删失。建立了估计量的渐近性质（一致性、渐近正态），模拟显示有限样本表现良好，并应用于多中心乳腺癌数据。对您而言，该文在 semiparametric 设定下通过惩罚拟似然回避 frailty 分布指定的思路，与您关注的 semiparametric theory 中弱化分布假设的方向一致，但未涉及效率界或 influence function 推导，方法学新颖度有限。
- **关键技术**: `penalized quasi-likelihood`, `inverse probability of censoring weighting (IPCW)`, `Buckley-James estimator`, `mean residual life regression`, `frailty model`, `conditional quasi-likelihood inference`
- **为什么对您有用**: 与您 primary interest 中的 semiparametric theory 相关——通过惩罚拟似然回避 frailty 分布指定是一种弱化假设的策略；乳腺癌流行病学应用属 secondary interest 的 epidemiology 范畴，但因果推断成分较弱，主要收益在于了解 MRL 回归这一较少使用的生存分析参数化角度。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12723](https://doi.org/10.1111/sjos.12723) — Double debiased transfer learning for adaptive Huber regression
- **作者**: Ziyuan Wang, Lei Wang, Heng Lian
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1472-1505
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维线性回归的迁移学习设定下，针对重尾/非对称误差，目标是利用源数据改善目标数据的估计并进行有效统计推断。方法上采用自适应 Huber 回归（AHR）平衡偏差与鲁棒性，提出两步 L1 惩罚迁移 AHR 估计量并建立误差界。为纠正 Lasso 带来的偏差，基于 decorrelated score 方程构建统一的去偏框架，证明了去偏 Lasso 迁移 AHR 估计量的渐近正态性，从而支持高维分量的置信区间与假设检验。当可迁移源未知时，进一步提出具有理论保证的数据驱动源检测算法。该文将 decorrelated score 去偏与鲁棒 M 估计结合，直接推进了您在 debiased ML 与高维假设检验方向的工作，且迁移学习框架下的源检测机制对高维因果推断的异质性数据整合有借鉴意义。
- **关键技术**: `adaptive Huber regression`, `debiased Lasso`, `decorrelated score equations`, `transfer learning`, `high-dimensional inference`
- **为什么对您有用**: 直接涉及您 primary interest 中的 debiased ML（decorrelated score 去偏框架）与高维假设检验，且自适应 Huber 回归的鲁棒性处理对重尾数据下的半参数/高维推断有方法迁移价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1111/sjos.12736](https://doi.org/10.1111/sjos.12736) — Validation of point process predictions with proper scoring rules
- **作者**: Claudio Heinrich‐Mertsching, Thordis L. Thorarinsdottir, Peter Guttorp, Max Schneider
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1533-1566
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在空间点过程预测评估的设定下，提出一类基于汇总统计量（summary statistics）的 proper scoring rules，用于模型校准与选择。核心机制是：对 scoring rule 中的期望项做 Monte Carlo 近似，从而只需模型可模拟即可计算得分，避免了 logarithmic score 等需要显式似然的限制。不同 scoring rule 可针对点过程的不同特征（空间分布、聚类倾向）进行校准检验，等价于对模型特定方面的 goodness-of-fit 检验。模拟实验比较了所提 scoring rules 与 logarithmic score 对不同偏离类型的敏感度；两个应用（北加州地震、太平洋银杉空间分布）展示了科学模型选择中的实用性。对您而言，proper scoring rule 作为预测模型验证的决策理论工具，与 hypothesis testing / model assessment 有概念联系，Monte Carlo 近似策略也可迁移至其他 simulation-based inference 场景，但与您核心的因果推断或效率理论方向距离较远。
- **关键技术**: `proper scoring rules`, `Monte Carlo approximation`, `summary statistics`, `point process calibration`, `logarithmic score comparison`
- **为什么对您有用**: 与您 statistical computing 中的 Monte Carlo 方法及 mathematical statistics 中的模型评估/检验有边缘重叠，Monte Carlo 近似 scoring rule 的思路可迁移至 simulation-based inference，但整体与核心方向（因果、效率、高维）关联较弱。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12742](https://doi.org/10.1111/sjos.12742) — Regression‐based network‐flow and inner‐matrix reconstruction
- **作者**: Michael Lebacher, Göran Kauermann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1730-1748
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在已知矩阵行和与列和（边际信息）的设定下，研究目标是重构矩阵内部元素（网络流/矩阵重构）。本文证明迭代比例拟合过程（IPFP）或最大熵（ME）的解等价于基于增广拉格朗日优化的受限极大似然估计（RMLE）。基于此等价性，作者将网络重构扩展至回归框架，允许在模型中引入外生协变量。回归模型的均值被约束以匹配观测到的行列边际，并采用 Bootstrap 方法进行不确定性量化。模拟研究与国际清算银行（BIS）银行间借贷数据的实证表明，引入外生信息显著降低了重构误差。对您可能有用：增广拉格朗日优化与受限 MLE 的等价推导为统计计算（约束优化数值方法）提供了新视角，且 BIS 数据集对经济理论应用有参考价值。
- **关键技术**: `iterative proportional fitting`, `maximum entropy`, `augmented Lagrangian optimization`, `restricted maximum likelihood`, `bootstrap uncertainty quantification`
- **为什么对您有用**: 增广拉格朗日求解受限 MLE 的等价证明对统计计算（约束优化数值方法）有方法论启发；BIS 银行间借贷数据集对经济理论中的网络重构应用具有数据集价值。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.12754](https://doi.org/10.1111/sjos.12754) — Model‐based clustering in simple hypergraphs through a stochastic blockmodel
- **作者**: Luca Brusa, Catherine Matias
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1661-1684
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究简单超图（simple hypergraph）中的节点聚类问题，提出将图上的随机块模型（stochastic blockmodel, SBM）推广至超图设定，假设潜在节点分组下超边条件独立。作者首先证明了模型参数的 generic identifiability，随后开发了变分近似 EM（VEM）算法进行参数推断与节点聚类，并导出模型选择准则。配套 R 包 HyperSBM 在合成数据、线聚类实验及合著数据集上与其他聚类方法进行了对比。该工作的 identifiability 证明与 VEM 算法设计属于数理统计与统计计算范畴，但核心主题（超图/网络聚类）与您的主要兴趣方向重叠有限。
- **关键技术**: `stochastic blockmodel`, `variational EM`, `generic identifiability`, `hypergraph clustering`, `model selection criterion`
- **为什么对您有用**: 参数 identifiability 证明和 VEM 算法实现与数理统计和统计计算有弱关联，但超图聚类本身不在您的主要兴趣内，收益有限。

### 2. [10.1111/sjos.12752](https://doi.org/10.1111/sjos.12752) — On some publications of Sir David Cox
- **作者**: Nancy Reid
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1425-1432
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是对 Sir David Cox 在《Scandinavian Journal of Statistics》及《Scandinavian Actuarial Journal》上发表的六篇论文的回顾与总结。文章梳理了这些文献的核心贡献，主要涉及生存分析、计数过程及似然推断等领域的奠基性工作。作为纪念性综述，本文不包含新的理论或方法，而是从当代视角审视这些经典结果的学术影响。Cox 的这些工作（如 partial likelihood、残差分析等）构成了现代半参数理论的基石。对您而言，阅读此文有助于加深对半参数效率理论及似然推断历史起源的理解，但方法学新颖度有限。
- **关键技术**: `partial likelihood`, `survival analysis`, `counting processes`, `likelihood inference`
- **为什么对您有用**: 作为统计史综述，本文回顾了 Cox 的经典工作（如 partial likelihood），对您理解半参数效率理论及似然推断的历史脉络有参考价值，但无新理论或新方法。

### 3. [10.1111/sjos.12749](https://doi.org/10.1111/sjos.12749) — Looking back: Selected contributions by C. R. Rao to multivariate analysis
- **作者**: Dianna Smith
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1393-1424
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是 C. R. Rao 在多元分析领域贡献的回顾性综述，涵盖其近 80 年职业生涯中的多项经典成果。重点讨论的主题包括：Rao 的 U 统计量（将单样本 Hotelling T² 推广至多组多元均值检验的框架）、Wilks 统计量的渐近展开（涉及高阶项的 Edgeworth 型修正）、Rao 的 perimeter test（一种基于凸包的非参数多元检验）、以及 functional PCA、canonical coordinates、correspondence analysis 等方法的历史脉络与后续发展。文章强调跨学科合作与真实数据集在 Rao 几乎所有重要贡献中的关键作用。作为综述，本文无新理论或新方法，但对理解 Rao U 统计量与高阶渐近展开的历史动机和数学结构有参考价值。对您有用：若您研究 higher-order U-statistics 的投影与渐近理论，Rao U 统计量的原始构造与 Wilks 统计量高阶展开的思路可作为经典参照。
- **关键技术**: `Rao's U statistic`, `asymptotic expansion of Wilks' statistic`, `perimeter test`, `functional principal component analysis`, `canonical coordinates`
- **为什么对您有用**: 直接关联您 primary interest 中的 higher-order U-statistics（Rao U 统计量是经典多组多元 U 检验框架）与 hypothesis testing（Wilks 统计量高阶展开、perimeter test），可作为理解这些方法原始动机与数学结构的入门文献。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

