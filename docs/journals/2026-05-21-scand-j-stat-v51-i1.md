# Scand. J. Stat. — Vol 51  Issue 1  ·  2026-05-21

- 共 17 篇 · Scandinavian Journal of Statistics

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12675](https://doi.org/10.1111/sjos.12675) — Partial correlation graphical LASSO
- **作者**: Jack Storror Carter, David Rossell, Jim Q. Smith
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 32-63
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维 Gaussian 图模型设定下，传统 graphical LASSO 惩罚精度矩阵非对角元，但缺乏尺度不变性，而预先标准化样本方差会显著干扰推断。本文提出基于偏相关的新惩罚族，证明了其与最大似然及对数惩罚均具备尺度不变性。作者重点发展了 partial correlation graphical LASSO (pc-glasso)，直接对偏相关系数施加 L1 惩罚。相应的优化问题虽非全局凸，但具有条件凸性，可通过交替优化策略求解。模拟与实际数据表明，pc-glasso 在保证尺度不变的同时，在图结构恢复推断上有显著增益。对您有用：该工作为高维精度矩阵估计提供了更稳健的惩罚机制，其条件凸优化算法设计对您在高维统计与统计计算方向的研究有直接参考价值。
- **关键技术**: `graphical LASSO`, `partial correlation`, `scale invariance`, `conditionally convex optimization`, `precision matrix estimation`, `penalized likelihood`
- **为什么对您有用**: 直接关联您的高维统计与统计计算兴趣：提出了高维精度矩阵估计中替代传统 glasso 的尺度不变惩罚方法，其条件凸优化求解策略对算法设计有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1111/sjos.12681](https://doi.org/10.1111/sjos.12681) — Marginal additive models for population‐averaged inference in longitudinal and cluster‐correlated data
- **作者**: Glen McGee, Alex Stringer
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 384-401
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向与聚类相关数据中，本文提出边际可加模型（MAM），目标是在 population-averaged 设定下对非线性边际均值进行估计与推断，同时兼顾聚类间变异与聚类特异性预测。MAM 结合了 GEE 式的边际均值结构与可加惩罚样条，通过拟似然方法进行估计。作者提出了一种新的拟合算法，能够高效计算标准误，并对惩罚项的估计偏差进行了修正，从而保证了不确定性量化的有效性。模拟与实证（海狸觅食行为纵向数据与西非罗阿罗阿丝虫病空间数据）表明，该方法在聚类相关结构下提供了可靠的边际推断与聚类特异性预测。对您有用：MAM 为纵向数据的半参数边际建模提供了新方法，其惩罚项修正与标准误计算算法可直接迁移至纵向因果推断中的 GEE/TMLE 计算框架，且流行病学空间数据集具有应用参考价值。
- **关键技术**: `marginal additive model`, `penalized splines`, `population-averaged inference`, `sandwich variance estimation`, `cluster-correlated data`
- **为什么对您有用**: 与您关注的纵向因果推断及半参数理论直接相关：MAM 提供了聚类相关数据下半参数边际均值的有效推断与计算方案，其惩罚项修正算法可迁移至纵向 GEE/TMLE 的标准误计算；同时包含流行病学空间数据集。

### 2. [10.1111/sjos.12680](https://doi.org/10.1111/sjos.12680) — Sparse additive models in high dimensions with wavelets
- **作者**: Sylvain Sardy, Xiaoyu Ma
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 89-108
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维回归设定下（n 与 p 均可很大），本文研究稀疏可加模型（Sparse Additive Models）的变量选择与估计问题，假设真实模型仅依赖少数协变量的非参数可加函数。方法利用快速小波变换将非参数成分展开，通过求解带有 quantile universal threshold (QUT) 的凸优化问题实现变量选择，从而避免了交叉验证。针对预测目标，作者进一步提出了基于 Stein's Unbiased Risk Estimate (SURE) 的惩罚参数选择规则。模拟与实证表明，该方法在高维设定下计算高效，且在 FDR-TPR 权衡及 MSE 上优于传统方法。对您有用：该文将小波基与高维稀疏非参数模型结合，其 QUT 阈值构造与 SURE 规则对您在“高维统计”与“半/非参数理论”方向的研究具有方法与计算上的迁移价值。
- **关键技术**: `sparse additive models`, `wavelet transforms`, `quantile universal threshold`, `Stein's Unbiased Risk Estimate`, `convex optimization`, `variable selection`
- **为什么对您有用**: 该文结合高维变量选择与非参数可加模型，其无需交叉验证的 QUT 阈值构造与 SURE 规则对您在“高维统计”与“半/非参数理论”方向的研究具有方法与计算上的迁移价值。

### 3. [10.1111/sjos.12673](https://doi.org/10.1111/sjos.12673) — A nested semiparametric method for case‐control study with missingness
- **作者**: Ge Zhao, Yanyuan Ma, Jill Schnall Hasler, Scott Damrauer, Michael Levin, Jinbo Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 201-219
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在病例对照研究中部分真实患病状态缺失的设定下，目标是估计真实病例相对于对照的 odds ratio 参数。引入“非病例”概念以半参数方式对缺失的真实病例概率进行插补，并利用充分降维（SDR）技术实现灵活的维度缩减。方法核心在于构建高效的半参数充分降维估计量，以保证插补程序的稳定性和对高维协变量的适应性。理论上证明了该 odds ratio 参数估计量具有 n^{-1/2}-相合渐近正态性（root-n CAN）。实证部分通过模拟和扩张型心肌病数据验证了方法的有效性。对您有用：该文将半参数效率理论与充分降维结合处理缺失数据的思路，以及推导 n^{-1/2}-CAN 的技术，可直接迁移至您关注的半参数效率界与因果推断中缺失/选择偏差的处理。
- **关键技术**: `semiparametric sufficient dimension reduction`, `efficient semiparametric estimator`, `missing data imputation`, `root-n asymptotic normality`, `case-control odds ratio`
- **为什么对您有用**: 论文核心是半参数效率理论与充分降维的结合，并在流行病学病例对照缺失数据下证明了 n^{-1/2}-CAN，直接契合您对半参数效率界的关注，其处理缺失/选择偏差的半参数方法可迁移至因果推断设定。

### 4. [10.1111/sjos.12670](https://doi.org/10.1111/sjos.12670) — Extrapolation estimation for nonparametric regression with measurement error
- **作者**: Weixing Song, Kanwal Ayub, Jianhong Shi
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 1-31
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在协变量受正态测量误差污染的非参数回归模型中，本文提出一种外推估计算法来估计回归函数。核心方法是对局部线性逼近与观测响应之间的偏差施加核加权最小二乘，再对其取条件期望，从而绕过经典 SIMEX 中的模拟步骤，显著降低计算时间。该算法给出了外推函数的精确形式，但指出当带宽小于测量误差标准差时，不能简单地将外推变量设为 -1 来获得外推估计。文中讨论了所提估计量的大样本性质（一致性、收敛速度），并通过模拟与实例验证。对您有用之处在于：这是非参数测量误差校正的新计算方案，连接了您关注的非参数理论与统计计算（数值算法效率），且外推函数精确形式的理论推导可为类似 deconvolution 问题的效率分析提供参考。
- **关键技术**: `SIMEX extrapolation`, `local linear kernel estimation`, `kernel-weighted least squares`, `measurement error deconvolution`, `conditional expectation extrapolation`
- **为什么对您有用**: 直接关联您 primary interest 中的非参数/半参数理论与统计计算：新算法绕过 SIMEX 模拟步骤提升了计算效率，且外推函数精确形式的理论分析对非参数测量误差框架下的估计效率研究有迁移价值。

### 5. [10.1111/sjos.12674](https://doi.org/10.1111/sjos.12674) — Structure recovery for partially observed discrete Markov random fields on graphs under not necessarily positive distributions
- **作者**: Florencia Leonardi, Rodrigo Carvalho, Iara Frondana
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 64-88
- 相关性 4/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究部分观测离散 Markov 随机场（MRF）的图结构恢复问题，目标是在不要求分布满足通常正性条件的设定下估计节点邻域。作者提出了一种惩罚条件似然准则，并在有限及可数无限节点图上证明了邻域估计量的相合性。在有限节点情形下，底层图结构可以概率 1 完美恢复；在可数无限节点情形下，通过让候选邻域大小随样本量增长，亦能以概率 1 恢复任意有限子图。该方法的核心突破在于摒弃了传统 MRF 结构学习中严格的分布正性假设，仅需极弱的分布条件。对您而言，该工作在可数无限维设定下的模型选择一致性及放松正性假设的思路，可为高维图模型或因果发现中的弱假设理论提供参考，且其股票市场应用契合您的经济理论兴趣。
- **关键技术**: `penalized conditional likelihood`, `Markov random fields`, `graph structure recovery`, `model selection consistency`, `positivity assumption relaxation`
- **为什么对您有用**: 放松正性假设的图结构恢复理论与高维统计中的模型选择一致性相关；同时，股票市场数据的实证分析契合您在经济理论（应用图模型/因果发现）方面的次级兴趣。

### 6. [10.1111/sjos.12682](https://doi.org/10.1111/sjos.12682) — On the perimeter estimation of pixelated excursion sets of two‐dimensional anisotropic random fields
- **作者**: Ryan Cotsakis, Elena Di Bernardino, Thomas Opitz
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 268-301
- 相关性 1/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究在正方形网格（像素化）观测下，二维各向异性随机场的偏移集（excursion sets）周长估计问题，无需高斯性或各向同性假设。提出一种基于二值数字图像的逐段线性逼近估计量，计算偏移集边界的长度。证明了当像素尺寸递减时该估计量具有相合性，且无需归一化常数；在域扩张时，估计误差的阶低于域边长。对于仿射强混合随机场，在同时考虑多个水平时，证明了该估计量的多元中心极限定理（CLT）。有限样本数值模拟验证了估计量的统计性质。对您而言，本文在非参数随机场几何泛函的渐近理论（特别是放松了各向同性与高斯性假设）方面具有参考价值，其逐段线性逼近算法也可作为统计计算中网格数据处理的一个案例。
- **关键技术**: `excursion set perimeter`, `piecewise linear approximation`, `strongly mixing random fields`, `multivariate CLT`, `anisotropic random fields`
- **为什么对您有用**: 涉及非参数随机场几何泛函的渐近理论，放松了传统的各向同性与高斯性假设，对您在非参数理论及统计计算（网格数据逼近算法）方面的兴趣有参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12683](https://doi.org/10.1111/sjos.12683) — Communication‐efficient low‐dimensional parameter estimation and inference for high‐dimensional Lp$$ {L}^p $$‐quantile regression
- **作者**: Junzhuo Gao, Lei Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 302-333
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在分布式数据设定下，研究高维 $L^p$-分位数回归中低维目标参数的估计与推断，目标是在冗余参数高维且数据分块的条件下实现 $n^{-1/2}$-CAN 推断。为处理高维冗余参数，文章首先提出正则化投影得分方法，通过 profile/debiasing 机制消除高维惩罚带来的收缩偏差。针对分布式场景，进一步构造两种通信高效的代理投影得分估计器，仅需局部与中心节点间一轮通信即可逼近全局估计的渐近性质。理论上证明了代理估计器的渐近正态性，并给出通信轮数与统计效率的权衡。该工作将高维推断中的 debiased 思想与分布式计算结合，对您在效率理论（高维冗余下的低维参数 semiparametric efficiency）与统计计算（通信高效算法）交叉方向的研究有直接借鉴价值。
- **关键技术**: `regularized projection score`, `communication-efficient estimation`, `distributed inference`, `high-dimensional nuisance parameter`, `$L^p$-quantile regression`
- **为什么对您有用**: 直接关联您的高维统计（高维冗余参数下的低维推断/debiased思想）与统计计算（分布式通信高效算法）两个主要兴趣；同时 $L^p$-分位数回归在计量经济学中应用广泛，方法可迁移至经济数据应用。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12685](https://doi.org/10.1111/sjos.12685) — Testing the missing at random assumption in generalized linear models in the presence of instrumental variables
- **作者**: Rui Duan, C. Jason Liang, Pamela A. Shaw, Cheng Yong Tang, Yong Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 334-354
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在广义线性模型(GLM)下，本文研究如何利用工具变量(IV)检验缺失机制是缺失完全随机(MAR)还是非随机缺失(MNAR)。核心机制是构造仅在MAR下一致与在MNAR下也一致的两类估计量，并建立它们之间的差异度量(discrepancy measure)。在MAR原假设下，该差异度量的概率极限为零；而在MNAR备择假设下，由于IV的引入，差异度量将偏离零。基于该差异度量的渐近正态性，构建了检验MAR的统计量，实现了数据驱动的缺失机制选择。理论分析了检验的水平和功效，模拟与流行病学真实数据验证了方法有效性。该文将IV与缺失机制的假设检验结合，为您在因果推断中处理不可观测缺失/混淆时的敏感性分析及假设检验提供了直接的方法论参考。
- **关键技术**: `instrumental variable`, `missing at random test`, `discrepancy measure`, `generalized linear models`, `asymptotic normality`
- **为什么对您有用**: 直接结合了您primary interest中的因果推断(IV)与假设检验，且缺失数据问题在流行病学(secondary interest)中极为常见，阅读此文可获知如何利用IV对MAR假设进行严格的统计检验。

### 2. [10.1111/sjos.12671](https://doi.org/10.1111/sjos.12671) — Flexible specification testing in quantile regression models
- **作者**: Tim Kutzker, Nadja Klein, Dominik Wied
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 355-383
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在分位数回归框架下提出三种一致的设定检验，目标是在协变量效应允许依赖于分位数且非线性的设定下检验条件分布函数的函数形式。方法上，作者通过适当的基函数（如sieve）对条件分位数函数进行参数化，而非局限于纯参数形式，从而将线性效应作为特例包含。检验统计量采用 Cramér-von Mises (CvM) 类型，作者推导了其理论极限分布并提出相应的 bootstrap 推断方法。此外，文章推导了修正的检验统计量以提升检验功效。蒙特卡洛模拟和两个实证（德国条件收入分布与澳大利亚电力市场）验证了方法的有效性。对您而言，该文将基函数参数化引入分位数回归设定检验并推导极限分布，直接契合您在假设检验与半/非参数理论方面的兴趣，且德国收入分布的实证对经济理论应用有参考价值。
- **关键技术**: `specification testing`, `quantile regression`, `Cramer-von Mises statistic`, `basis function parameterization`, `bootstrap inference`, `asymptotic distribution`
- **为什么对您有用**: 直接契合您在假设检验与半/非参数理论方面的核心兴趣，展示了如何将基函数参数化引入 CvM 型检验并推导极限分布；同时德国收入分布的实证分析对经济理论应用有数据集与分析范式的参考价值。

### 3. [10.1111/sjos.12689](https://doi.org/10.1111/sjos.12689) — Nearly unstable integer‐valued ARCH process and unit root testing
- **作者**: Wagner Barreto‐Souza, Ngai Hang Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 402-424
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文针对计数时间序列，引入了近不稳定整数自回归条件异方差（NU-INARCH）过程，研究其在接近单位根边界时的渐近性质。理论上，证明了经正则化的 NU-INARCH 过程在 Skorohod 拓扑下弱收敛至 Cox-Ingersoll-Ross (CIR) 扩散过程。基于此，推导了相关参数的条件最小二乘（CLS）估计量的渐近分布，其表现为特定随机积分的泛函。利用上述非标准渐近结果，本文构建了单位根检验并考察了其有限样本下的 Type-I 误差与功效。模拟显示近不稳定方法优于基于平稳性假设的方法，实证分析将其应用于英国 COVID-19 日死亡人数数据。对您而言，本文在非标准渐近下的假设检验推导及流行病学计数数据应用具有参考价值。
- **关键技术**: `weak convergence to CIR diffusion`, `conditional least squares estimation`, `unit root test`, `Skorohod topology`, `stochastic integrals`, `INARCH process`
- **为什么对您有用**: 本文属于数学统计假设检验方向，推导了非标准渐近（近单位根）下的检验统计量极限分布，同时包含流行病学（COVID-19）计数数据应用，对您在假设检验理论及流行病学数据分析方面的兴趣有直接参考价值。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12679](https://doi.org/10.1111/sjos.12679) — Estimating absorption time distributions of general Markov jump processes
- **作者**: Jamaal Ahmad, Martin Bladt, Mogens Bladt
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 171-200
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在非时齐 Markov 跳跃过程 (MJP) 框架下，目标是估计吸收时间分布，突破了以往要求子强度矩阵可交换 (commuting) 的正则性假设。本文提出基于最大似然估计 (MLE) 的一般理论，并构造期望最大化 (EM) 算法求解含潜在状态的似然函数。为实现参数的简约表示，将强度矩阵函数降维为分段常数形式，并引入参数线性模型绑定不同区间的强度参数。算法实现与理论推导高度依赖矩阵解析方法 (matrix analytic methods)，特别是对矩阵指数与条件期望的数值计算。实证表明该方法能拟合计算需求极高的理论分布与真实数据。对您可能有用：若关注统计计算中的矩阵算法与 EM 数值实现，其处理分段常数强度矩阵的矩阵解析技巧可作参考，但与您的高维/半参数/因果主线距离较远。
- **关键技术**: `Markov jump processes`, `EM algorithm`, `matrix analytic methods`, `maximum likelihood estimation`, `piecewise constant intensity matrix`
- **为什么对您有用**: 本文核心是连续时间马尔可夫过程的 MLE 与 EM 算法实现，属于统计计算与参数模型推断；对您在统计计算（矩阵算法、数值优化）方面的兴趣有一定参考价值，但与高维、半参数或因果推断的主线关联较弱。

## 其他  *(other, 5 篇)*

### 1. [10.1111/sjos.12687](https://doi.org/10.1111/sjos.12687) — Greenland, S. (2023). Divergence vs. decision P‐values: A distinction worth making in theory and keeping in practice. <i>Scandinavian Journal of Statistics</i> , 50, 1–35, https://onlinelibrary.wiley.com/doi/10.1111/sjos.12625
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 425-425
- 相关性 7/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "本文是 Greenland (2023) 关于 divergence P-value 与 decision P-value 区别的论文的勘误。原论文在假设检验理论框架下，区分了基于统计散度的 P-value（衡量数据与假设的偏离程度）和基于决策的 P-value（如 Hodges & Lehmann 1954 的 UMPU decision P-value p_HL），二者在区间假设下行为不同。勘误指出：第 70 页公式仅对参数 μ 在开区间 (m_L, m_U) 外部给出 p_HL，此时 p_HL 是区间端点处 divergence P-value 的均值；而 p_M 在区间外则是端点 divergence P-value 的最大值。第 71 页将条件"α ≥ .16"更正为"α < .16"。该勘误本身无新理论贡献，但原论文对 P-value 两种解释的梳理对假设检验基础理论有参考价值。",
  "key_techniques": [
    "divergence P-value",
    "UMPU decision P-value",
    "Hodges-Lehmann test",
    "interval hypothesis testing"
  ],

### 2. [10.1111/sjos.12676](https://doi.org/10.1111/sjos.12676) — Locally adaptive Bayesian isotonic regression using half shrinkage priors
- **作者**: Ryo Okano, Yasuyuki Hamura, Kaoru Irie, Shonosuke Sugasawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 109-141
- 相关性 4/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "在单调约束下的非参数函数估计（isotonic regression）设定中，本文提出基于 global-local shrinkage prior 的贝叶斯方法来估计单调函数值。核心创新是引入"half shrinkage prior"——将传统 shrinkage prior 限制在正半轴——并赋予函数值的一阶差分，从而在保持单调性的同时对局部跳变（jumps）具有自适应性。作者提供了简单快速的 Gibbs sampling 算法进行全后验推断。理论上证明了后验均值估计量对大差值具有鲁棒性，且在函数未变化点处的渐近风险可得到改善。该工作对您在非参数理论方面的兴趣有参考价值，尤其是 shrinkage prior 在 shape-constrained 非参数估计中的风险自适应性质，但与您关注的 semiparametric efficiency bound 方向距离较远。",
  "key_techniques": [
    "half shrinkage prior",
    "global-local shrinkage",
    "isotonic regression",
    "Gibbs sampling",
    "posterior risk adap

### 3. [10.1111/sjos.12672](https://doi.org/10.1111/sjos.12672) — Locally correct confidence intervals for a binomial proportion: A new criteria for an interval estimator
- **作者**: Paul H. Garthwaite, Maha W. Moustafa, Fadlalla G. Elfadaly
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 220-244
- 相关性 4/10
- **摘要**: {
  "topic": "hypothesis_testing",
  "summary_zh": "本文针对二项分布比例的置信区间构造提出新准则"局部正确置信区间"(locally correct CI)：要求在任意参数值θ处，区间覆盖率关于θ的导数在θ等于真实参数时非负，从而避免常见方法（Wilson、Agresti-Coull等）覆盖率低于名义水平的问题。作者提出一种满足该准则的方法，并证明在所有满足准则的方法中其区间平均长度最短；与Clopper-Pearson（严格满足CI定义但区间过宽）相比，平均长度显著缩短。对实际常用置信水平，mid-p方法也满足新准则且具有自身最优性，其区间仅略宽于新方法。对您有用：该工作为二项比例区间估计提供了严格的覆盖率准则与最优性理论，属于数学统计中区间估计/假设检验的基础性贡献，其"局部正确性"思路可启发其他离散分布或高维参数推断中的覆盖率控制问题。",
  "key_techniques": [
    "locally correct confidence interval criterion",
    "coverage probability monotonicity",
    "Clopper-Pearson interval",
    "mid-p method",
    "average length optimal

### 4. [10.1111/sjos.12678](https://doi.org/10.1111/sjos.12678) — Design for order‐of‐addition experiments with two‐level components
- **作者**: Hengzhen Huang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 142-170
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究两水平成分的序加实验（order-of-addition, OofA）设计问题，目标是在同时考虑序列效应与因子效应的设定下，构造平衡且经济运行次数的 OofA 设计。传统 OofA 仅关注成分排列顺序对响应的影响，本文引入各成分两水平因子效应，提出系统化方法联合构造序列设计与因子设计。通过适当选择两部分设计，证明其组合可达到平衡设计且运行次数经济，并在若干经验模型下建立 D-、A-、E-最优性。方法可推广至过程变量数不等于成分数、多水平成分等情形。该文属于实验设计领域，与您关注的 semiparametric efficiency / 高维推断 / 因果推断方向无直接交集，D-/A-/E-最优性是设计准则而非估计效率界，阅读收益有限。
- **关键技术**: `order-of-addition design`, `D-/A-/E-optimality`, `balanced design construction`, `factorial design`, `sequence effect modeling`
- **为什么对您有用**: 与您 primary interests 的 semiparametric efficiency bounds / 高维推断 / 因果推断无直接关联；D-/A-/E-最优性属实验设计准则，非估计效率理论，方法可迁移性低。

### 5. [10.1111/sjos.12677](https://doi.org/10.1111/sjos.12677) — Some mechanisms leading to underdispersion: Old and new proposals
- **作者**: Pedro Puig, Jordi Valero, Amanda Fernández‐Fontelo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 245-267
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究计数数据欠离散(underdispersion)的生成机制，在更新过程、纯生过程及生灭过程等随机过程设定下探讨其分布性质。作者重新审视了基于到达过程（如状态依赖服务率的排队模型）和加权泊松分布的欠离散机制，并证明加权泊松等已知分布可与生灭过程建立直接联系。文章引入了经典及变体二项稀疏化(variable binomial thinning)机制，该机制不仅能生成单变量欠离散分布，还可构造具有负相关的双变量计数分布。最后通过生物剂量测定等实例展示了所提机制的应用。对您而言，此文主要提供离散分布的概率生成视角，但与您关注的半参数效率、因果推断或高维渐近理论关联较弱，仅作背景参考。
- **关键技术**: `underdispersed count distributions`, `birth-death processes`, `weighted Poisson distributions`, `variable binomial thinning`, `renewal processes`
- **为什么对您有用**: 本文属于纯概率分布与随机过程机制研究，与您核心关注的半参数效率界、因果推断或高维渐近理论无直接交集，仅当您需要处理欠离散计数数据的参数模型时可能作为背景参考。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

