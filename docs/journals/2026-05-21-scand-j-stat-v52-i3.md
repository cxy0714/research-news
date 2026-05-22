# Scand. J. Stat. — Vol 52  Issue 3  ·  2026-05-21

- 共 11 篇 · Scandinavian Journal of Statistics

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12785](https://doi.org/10.1111/sjos.12785) — Mode‐adaptive factor models
- **作者**: Tao Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1206-1238
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维面板数据的因子模型设定下，传统 PCA/约束最小二乘估计在重尾、偏态误差下失效，本文提出 mode-adaptive factor model (MAFM)，用众数回归替代均值回归以捕获中心趋势。核心估计量通过迭代众数回归算法求解，融合 EM 思想保证收敛至驻点；理论贡献在于不对特质误差施加矩条件即可建立估计量相合性，并提出 mode information criterion 实现因子数的一致选择，同时给出数据驱动的带宽选取程序。模拟与宏观预测实证均显示 MAFM 在重尾/偏态设定下优于传统方法。对您有用之处在于：高维因子模型的鲁棒估计放松了矩假设，与非参数/半参数理论及高维统计兴趣相关，宏观预测应用也对接经济理论方向。
- **关键技术**: `mode regression`, `iterative EM algorithm`, `factor number information criterion`, `high-dimensional factor model`, `kernel bandwidth selection`, `moment-free consistency`
- **为什么对您有用**: 高维因子模型放松矩假设的鲁棒估计直接关联您的高维统计与半参数/非参数理论兴趣；宏观预测实证部分对接经济理论应用方向，算法设计也涉及统计计算。

## 非参数 / 半参数  *(nonparam_semipara, 4 篇)*

### 1. [10.1111/sjos.12789](https://doi.org/10.1111/sjos.12789) — Semiparametric regression with localized Bregman divergence
- **作者**: Hiroki Kosugi, Kanta Naito, Spiridon Penev
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1330-1375
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究基于局部化 Bregman 散度最小化的半参数回归，设定为多协变量广义线性模型框架下的局部参数模型，目标是在局部化条件下估计参数向量并导出诱导回归估计量。核心方法是将 Bregman 散度局部化以构造局部似然型目标函数，在 localization 下估计参数，并利用 Faa di Bruno 定理处理多元多项式预测子的一般化情形中复合函数的高阶导数。理论上给出了局部参数估计量与回归估计量的渐近性质（一致性、渐近正态性），并通过散度风险度量（divergence risk measure）对不同估计量进行理论比较。模拟与实际数据表明所提估计量表现良好，但未涉及半参数效率界或 cross-fitting 等现代 debiased 技术。对您有用之处在于：Bregman 散度局部化框架为半参数回归提供了一条不同于 sieve / kernel 的估计路径，Faa di Bruno 定理的多元推广技巧可能在您关注的半参数理论推导中有工具价值。
- **关键技术**: `localized Bregman divergence`, `semiparametric regression`, `local parametric model`, `Faa di Bruno theorem`, `divergence risk measure`, `asymptotic normality`
- **为什么对您有用**: 直接落入您 primary interest 的半参数理论方向；Bregman 散度局部化估计框架与您熟悉的 sieve/kernel 路径形成互补，Faa di Bruno 多元复合导数技巧可迁移至其他半参数渐近理论推导。

### 2. [10.1111/sjos.12791](https://doi.org/10.1111/sjos.12791) — Sparse Fréchet sufficient dimension reduction with graphical structure among predictors
- **作者**: Jiaying Weng, Kai Tan, Cheng Wang, Zhou Yu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1422-1443
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在响应变量为度量空间非欧对象（如概率分布、球面数据）的 Fréchet 回归设定下，研究高维预测变量的充分降维（SDR）问题。核心方法是提出一种利用预测变量间图结构信息的凸优化目标，从而避免高维协方差矩阵求逆。该优化结合图结构惩罚实现中心降维子空间估计与变量选择，并采用交替方向乘子法（ADMM）进行求解。理论上，在合适正则条件下证明了方法的子空间估计与变量选择一致性。对您有用：该文将图结构引入非欧数据的 Fréchet 降维，其 ADMM 算法设计与子空间一致性证明对您在半参数降维及统计计算方面的研究有参考价值。
- **关键技术**: `Fréchet regression`, `sufficient dimension reduction`, `graphical structure`, `ADMM algorithm`, `variable selection consistency`, `convex optimization`
- **为什么对您有用**: 将高维图结构惩罚引入非欧数据的 Fréchet 充分降维，其 ADMM 算法设计与子空间一致性理论对您在半参数降维及统计计算（数值优化）方面的兴趣有直接参考价值。

### 3. [10.1111/sjos.12792](https://doi.org/10.1111/sjos.12792) — Dimension reduction for the estimation of the conditional tail index
- **作者**: Laurent Gardes, Alexandre Podgorny
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1444-1476
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在高维协变量下估计重尾条件分布的条件尾部指数，假设存在低维线性子空间使得条件尾部指数仅依赖于协变量在该子空间上的投影（充分降维设定）。提出估计该降维子空间的方法并建立其一致性；在此基础上构建利用降维结构的条件尾部指数估计量，并证明其一致性。核心机制在于将高维非参数极值估计问题转化为低维子空间上的估计，从而克服维数灾难。理论结果保证了降维子空间与尾部指数估计的相合性，模拟与实证展示了降维对估计精度的提升。对您有用：该工作属于高维非参数估计中的充分降维路径，与您关注的非参数/半参数理论及高维统计（降维方向）直接相关，可提供极值统计中降维估计的理论框架参考。
- **关键技术**: `conditional tail index`, `sufficient dimension reduction`, `heavy-tailed distribution`, `nonparametric consistency`, `linear subspace estimation`
- **为什么对您有用**: 涉及高维协变量下的非参数估计与充分降维理论，与您关注的非参数/半参数理论及高维统计（降维方向）直接相关，可提供极值统计中降维估计的理论框架参考。

### 4. [10.1111/sjos.12782](https://doi.org/10.1111/sjos.12782) — Bandwidth selection for kernel intensity estimators for spatial point processes
- **作者**: Bethany J. Macdonald, Tilman M. Davies, Martin L. Hazelton
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1111-1137
- 相关性 4/10 · novelty: `minor`
- **摘要**: 在空间点过程的非参数核强度估计中，核心问题是如何选择最优带宽以平衡偏差与方差。现有带宽选择方法（及软件默认值）在不同强度模式下表现极不稳定，导致估计特征丢失或引入伪影。本文将多元密度估计中经典的 plug-in 和 cross-validation (CV) 技术适配至空间点过程框架，提出了新的带宽选择器。理论分析与实证（模拟及真实数据）表明，新方法在多种强度模式下表现更稳定一致，并讨论了观测窗口受限下的边缘效应（edge effects）对选择器的影响。虽然聚焦空间点过程，但其对非参数核估计中 plug-in 与 CV 带宽选择的理论与计算对比，对您在非参数理论及统计计算方面的兴趣有参考价值。
- **关键技术**: `kernel intensity estimation`, `bandwidth selection`, `plug-in selector`, `cross-validation`, `spatial point processes`, `edge correction`
- **为什么对您有用**: 属于非参数理论范畴，虽然应用场景（空间点过程）与您的核心方向不同，但其对核估计带宽选择（plug-in vs CV）的稳定性分析与计算实现，对您在非参数理论与统计计算方面的兴趣有边缘参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.12787](https://doi.org/10.1111/sjos.12787) — A minimum Wasserstein distance approach to Fisher's combination of independent, discrete <i>p</i>‐values
- **作者**: Gonzalo Contador, Zheyang Wu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1281-1300
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究独立离散 p 值的 Fisher 组合检验问题，目标是解决离散检验统计量逼近连续零分布时固有的保守性。提出通过最小化 Wasserstein 距离对离散检验统计量进行调整，使其逼近零假设下的连续分布，并在该框架下证明了 Lancaster 的 mid-p 和均值卡方统计量为其特例。为克服 Lancaster 方法的保守性，进一步在特定分布族内最小化 Wasserstein 距离，提出以最优 gamma 分布替代传统的卡方分布作为 Fisher 组合的零分布近似。该方法构造的检验具有渐近一致性，在严格控制第一类错误的同时显著提升了统计功效。对您有用：该工作将 Wasserstein 距离引入离散 p 值组合，为假设检验中的保守性问题提供了新的理论视角和计算方案，直接契合您在 mathematical statistics 与 hypothesis testing 方向的兴趣。
- **关键技术**: `Wasserstein distance minimization`, `Fisher's combination test`, `discrete p-value combination`, `Lancaster's mid-p statistic`, `optimal gamma approximation`
- **为什么对您有用**: 直接契合您在 mathematical statistics 与 hypothesis testing 方向的兴趣；通过 Wasserstein 距离优化离散检验统计量的零分布近似，为解决离散数据检验的保守性问题提供了新理论与计算方案。

### 2. [10.1111/sjos.12783](https://doi.org/10.1111/sjos.12783) — Combining stochastic tendency and distribution overlap towards improved nonparametric effect measures and inference
- **作者**: Jonas Beck, Patrick B. Langthaler, Arne C. Bathke
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1138-1175
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在非参数两样本设定下，本文旨在同时捕捉位置（随机趋势）与尺度差异，目标泛函为 Mann-Whitney 泛函与基于分位过程的分布重叠指数（DOI）。作者推导了这两个泛函估计量的联合渐近分布，并基于此构建了置信域。在此基础上，将 Wilcoxon-Mann-Whitney 检验扩展为基于联合泛函的新检验，该检验在仅存在位置差异时与秩和检验功效相当，而在存在尺度或更一般差异时，模拟功效显著优于经典 omnibus 检验。核心技术工具涉及 U-统计量渐近理论、经验过程与分位过程。新方法提供了具有直观解释性的效应度量，且一致性区域更广。对您有用：本文直接推进了非参数假设检验与 U-统计量渐近理论，其联合泛函推断框架对您在非参数理论及假设检验方向的研究有直接参考价值。
- **关键技术**: `Mann-Whitney functional`, `distribution overlap index`, `quantile process`, `joint asymptotic distribution`, `U-statistic asymptotics`, `nonparametric hypothesis testing`
- **为什么对您有用**: 直接推进了非参数假设检验与 U-统计量渐近理论，其联合泛函推断框架对您在非参数理论及假设检验方向的研究有直接参考价值。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12790](https://doi.org/10.1111/sjos.12790) — Statistical disaggregation—A Monte Carlo approach for imputation under constraints
- **作者**: Shenggang Hu, Hongsheng Dai, Fanlin Meng, Louis Aslett, Murray Pollock, Gareth O. Roberts
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1376-1421
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 研究在等式约束下的统计分解（disaggregation）问题，即从低分辨率观测推断高分辨率变量，约束导致联合分布不可解析且约束集概率测度为零。提出一种基于 Langevin 扩散与拒绝抽样的新型 Monte Carlo 采样算法，克服了传统拒绝抽样在零测度约束下失效的缺陷。针对线性约束，该方法具有精确性；对于任意非线性约束，能自然处理多峰分布。在电力消费数据集上的实证表明，相较于朴素或无约束方法，该算法在数据插补与不确定性估计上更准确。对您有用：直接契合您在统计计算与数值算法方面的兴趣，提供了处理零测度等式约束下 MCMC 采样的新思路，算法可迁移至其他带约束的潜变量推断问题。
- **关键技术**: `Langevin diffusion`, `rejection sampling`, `equality-constrained models`, `statistical disaggregation`, `constrained MCMC`
- **为什么对您有用**: 直接契合您在统计计算（数值方法与算法）方面的核心兴趣，提供了处理零测度等式约束下 MCMC 采样的新思路，算法可迁移至其他带约束的潜变量推断问题。

### 2. [10.1111/sjos.12786](https://doi.org/10.1111/sjos.12786) — Enhanced branching Latin hypercube design and its application in automatic algorithm configuration
- **作者**: Bing Wen, Sumin Wang, Fasheng Sun
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1239-1280
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究具有分支与嵌套因子的计算机实验设计问题，目标是构建在共享与嵌套因子上均具良好分层性质的增强型分支拉丁超方设计（EBLHD）。核心构造方法结合正交阵列（OA）与切片拉丁超方设计（SLHD），所得设计具备低维分层性质与低列相关性，且样本量可根据实验预算与估计精度灵活调整。仿真表明该设计在设计度量和估计精度上具优势，并应用于自动算法配置的初始化。对您而言，若涉及高维调参或计算机实验的统计计算问题，该设计的构造思路有一定参考价值，但与您核心的因果推断或高维渐近理论关联较弱。
- **关键技术**: `Latin hypercube design`, `orthogonal arrays`, `sliced Latin hypercube designs`, `branching and nested factors`, `low-dimensional stratification`
- **为什么对您有用**: 本文属于实验设计领域，与您关注的统计计算（算法配置）有微弱联系，但核心不涉及高维推断、半参数效率或因果识别，阅读收益主要限于了解计算机实验设计的最新构造技巧。

## 其他  *(other, 2 篇)*

### 1. [10.1111/sjos.12788](https://doi.org/10.1111/sjos.12788) — Testing relevant hypotheses in functional variance function via self‐normalization
- **作者**: Qirui Hu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1301-1329
- 相关性 7/10
- **摘要**: ```json
{
  "topic": "hypothesis_testing",
  "summary_zh": "在 contaminated functional data 的方差函数设定下，本文提出检验"无相关偏差"（relevant hypothesis）而非传统精确等价的零假设，覆盖单样本、两样本及变点检验三类问题。方法核心为 spline-backfitted kernel smoothing 估计方差函数，再以 self-normalization 构建检验统计量，避免了 long-run variance 的显式估计。理论证明所提检验具有 oracle efficiency，即渐近等价于已知真实轨迹的 oracle 检验程序，收敛性质不受轨迹估计误差影响。模拟与 EEG 数据验证了有限样本表现。对您有用：relevant hypothesis 将传统点假设替换为有实际意义的区间假设，与您 hypothesis testing 和 nonparametric theory 的兴趣直接相关；self-normalization 避免 nuisance parameter 估计的思路可迁移至其他泛函推断问题。",
  "key_techniques": [
    "spline-backfitted kernel smoothing",
    "self-norm

### 2. [10.1111/sjos.12784](https://doi.org/10.1111/sjos.12784) — A unifying class of compound Poisson integer‐valued ARMA and GARCH models
- **作者**: Johannes Bracher, Barbora Němcová
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1176-1205
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对计数时间序列建模，提出了统一 compound Poisson INAR 与 INGARCH 过程的广义整数 ARMA (GINARMA) 模型类，并在平稳性与几何遍历性等正则条件下研究其随机性质。核心机制包括将 INAR(p) 推广为平行于 INGARCH(p,q) 的结构，并在推断上采用极大似然、高斯拟似然与矩估计，辅以似然比检验区分模型实例。实证部分将模型作为随机流行病过程，应用于德国巴伐利亚州的麻疹与流行性腮腺炎周计数数据。对您而言，该文提供了流行病学计数数据的真实数据集与参数建模思路，但方法学以参数时间序列为主，对半参数/效率/因果推断的直接借鉴有限。
- **关键技术**: `compound Poisson process`, `integer-valued ARMA/GARCH`, `geometric ergodicity`, `Gaussian quasi-likelihood`, `likelihood ratio test`
- **为什么对您有用**: 提供了流行病学（麻疹/腮腺炎）计数时间序列的真实数据集与随机过程建模视角，但缺乏因果推断或半参数效率理论的新贡献，对您的主要兴趣直接帮助较小。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

