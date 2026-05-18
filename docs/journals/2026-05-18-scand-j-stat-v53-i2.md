# Scand. J. Stat. — Vol 53  Issue 2  ·  2026-05-18

- 共 14 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.70055](https://doi.org/10.1111/sjos.70055) — Interval identification of natural effects in the presence of outcome‐related unmeasured confounding
- **作者**: Marco Doretti, Elena Stanghellini
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 712-734
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在二值处理、二值中介与二值结局的因果中介设定下，本文研究存在与结局相关的未测量混杂时自然效应的识别问题。放松了关于结局的混杂假设，仅要求无未测量的暴露-中介混杂，并引入部分常数跨世界依赖（PC-CWD）和Logit恒常（LC）条件以约束反事实概率。基于对中介和结局的半参数Logistic回归（允许解释变量具有任意函数形式），推导出自然效应与总效应的区间识别界。利用Delta方法为识别界构建了考虑抽样变异性的不确定性区间，模拟与西班牙前瞻性队列研究（吸烟-肺气肿-肺癌）验证了方法表现。该工作为存在结局相关未测量混杂的中介分析提供了新的部分识别框架，直接契合您对因果推断（中介与敏感性分析）及流行病学应用的研究兴趣。
- **关键技术**: `causal mediation analysis`, `partial identification`, `natural effects`, `unmeasured confounding`, `semi-parametric logistic model`, `delta method`
- **为什么对您有用**: 直接契合您在因果推断中对中介分析和敏感性/部分识别的兴趣，展示了在放松结局混杂假设下如何推导识别界，且包含流行病学队列数据的应用。

### 2. [10.1111/sjos.70060](https://doi.org/10.1111/sjos.70060) — Sensitivity analysis for generalized estimating equation with non‐ignorable missing data
- **作者**: Hui Gong, Kin Wai Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 735-762
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在非随机缺失（MNAR）设定下，针对广义估计方程（GEE）的参数估计问题，提出多重敏感性模型（MSMs）框架以放松不可验证的随机缺失（MAR）假设。给定用户指定的敏感性参数，通过求解 MSM 辅助 GEE 的根界获得一系列估计量。进一步推导出估计量的分解表示，以量化不同缺失模式对估计的具体影响。提出渐近有效的百分位 Bootstrap 置信域（CR）进行区间估计，并给出相应的渐近理论保证。理论与模拟验证了该敏感性分析框架的实用性。对您可能有用：该文将敏感性分析从传统的因果推断延伸至纵向数据的 MNAR 缺失机制，其估计量分解技巧和 Bootstrap 置信域构造可直接迁移至您关注的 longitudinal causal inference 与敏感性分析子方向。
- **关键技术**: `sensitivity analysis`, `missing not at random (MNAR)`, `generalized estimating equation (GEE)`, `multiple sensitivity models (MSMs)`, `estimator decomposition`, `bootstrap confidence region`
- **为什么对您有用**: 直接关联您 primary interest 中的 sensitivity analysis 与 longitudinal 数据分析（GEE）；其处理不可验证假设的敏感性参数设定与估计量分解技巧，对放松因果推断中的 MAR/IGN 假设具有方法迁移价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.70071](https://doi.org/10.1111/sjos.70071) — High‐Dimensional Inference for Single‐Index Models With Latent Factors
- **作者**: Yanmei Shi, Meiling Hao, Yanlin Tang, Heng Lian, Xu Guo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 1001-1027
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维因子增强单指标模型设定下，研究潜在因子增强项的必要性检验及系数的估计与推断问题。提出一种 score-type 检验统计量判断增强成分是否必要，该统计量无需估计高维回归系数或精度矩阵，计算更简便。通过 Gaussian multiplier bootstrap 确定检验临界值，并在温和正则条件下证明了其理论有效性。在估计方面，基于带估计因子的惩罚估计量建立误差界，并利用 debiased estimator 构造单个系数的置信区间。值得注意的是，该方法不要求误差分布的矩条件，在重尾或异常值污染下仍保持良好表现。该文结合了高维推断、假设检验与半参数模型，对您在 high-dimensional inference (debiased ML) 与 hypothesis testing 的交叉研究有直接参考价值。
- **关键技术**: `factor-augmented single-index model`, `score-type test`, `Gaussian multiplier bootstrap`, `debiased estimator`, `heavy-tailed robustness`
- **为什么对您有用**: 直接涉及您的高维统计推断与假设检验核心兴趣，其无需估计精度矩阵的 score test 与针对重尾误差的 debiased 推断，可为高维半参数模型的 debiased ML 提供新思路。

### 2. [10.1111/sjos.70066](https://doi.org/10.1111/sjos.70066) — Lasso‐type estimator and classification algorithm for high‐dimensional multivariate Hawkes processes
- **作者**: Christophe Denis, Charlotte Dion‐Blanc, Romain E. Lacoste, Laure Sansonnet
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 919-968
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维多元Hawkes过程(MHP)设定下，目标是在固定短时间区间内重复独立观测的稀疏邻接矩阵上进行支持恢复与分类，假设网络维度相对于观测数较大且邻接矩阵稀疏、不同类别由外生强度向量与邻接矩阵区分。作者提出Lasso-type estimator用于恢复各类别下邻接矩阵的支持集，并在适当假设下证明了估计支持集的相合性；随后基于估计支持集构建经验误差最小化分类器，并给出分类器的收敛速率。数值实验在合成与真实数据上验证了支持恢复与分类的理论结果。该文的高维稀疏Lasso支持恢复相合性与分类收敛速率分析对您的高维统计方向有方法论参考价值，但核心设定(Hawkes过程/事件网络数据)与RMT距离较远，更多是高维稀疏M-估计的应用拓展。
- **关键技术**: `Lasso-type estimator`, `support recovery consistency`, `multivariate Hawkes process`, `empirical error minimization classifier`, `sparse adjacency matrix`, `high-dimensional M-estimation`
- **为什么对您有用**: 与您的高维统计兴趣相邻：Lasso支持恢复的相合性证明与收敛速率分析属于高维稀疏M-估计理论，可迁移至其他高维图结构估计问题；但不含RMT工具，Hawkes过程设定与您核心关注(RMT/效率界/半参数)距离较远。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1111/sjos.70053](https://doi.org/10.1111/sjos.70053) — Extended generalized Marshall–Olkin model for dependent censoring
- **作者**: Salima Helali
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 648-683
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在依赖竞争风险与删失设定下，研究扩展 Marshall-Olkin 模型，目标是边际分布与联合生存概率的估计。作者首先推导了该模型对应生存 copula 的概率性质，随后提出基于 Bernstein 多项式（sieve 估计）的策略来逼近边际与联合生存函数。在适当的正则条件下，证明了所提估计量具有渐近正态性（n^{-1/2}-CAN）。模拟与实际数据验证了该方法在有限样本下的表现。对您而言，该文将 Bernstein 多项式 sieve 应用于依赖删失结构的方法，可为半参数/非参数理论及流行病学应用中的依赖删失问题提供估计思路。
- **关键技术**: `Extended Marshall-Olkin model`, `survival copula`, `Bernstein polynomial sieve`, `dependent censoring`, `asymptotic normality`
- **为什么对您有用**: 涉及半参数/非参数 sieve 估计（Bernstein 多项式）与渐近正态性理论，且依赖删失/竞争风险是流行病学因果推断与生存分析中的常见难题，方法可迁移。

### 2. [10.1111/sjos.70069](https://doi.org/10.1111/sjos.70069) — Smooth and Rough Sample Paths in Mean Derivative Estimation for Functional Data
- **作者**: Max Berger, Hajo Holzmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 969-983
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 在多元函数数据固定同步设计下，本文研究 Hölder 光滑类中均值函数偏导数的估计，导出了极小化极大意义下的近最优收敛速率。与均值估计不同，导数估计的收敛速率严重依赖于样本路径的光滑性：当样本路径粗糙（光滑阶低于导数阶）时，得到比参数速率更慢的新型最优速率；当样本路径足够光滑且设计密集时，仍可达到参数 n^{-1/2} 速率。理论分析在上确界范数下进行，并证明了连续函数空间中的中心极限定理，为构建一致置信带提供基础。对您有用：该文对样本路径粗糙度如何改变非参数极小化极大速率的精细分析，直接契合您在非参数理论方面的兴趣，且其上确界范数下的 CLT 对假设检验与置信带构造具有方法学参考价值。
- **关键技术**: `minimax convergence rates`, `Hölder smoothness classes`, `functional data derivative estimation`, `sup-norm central limit theorem`, `local polynomial estimator`, `sample path smoothness`
- **为什么对您有用**: 直接契合您在非参数理论方面的兴趣，特别是样本路径粗糙度如何改变极小化极大收敛速率的精细刻画，以及上确界范数下的一致置信带构造（CLT）对假设检验的参考价值。

### 3. [10.1111/sjos.70070](https://doi.org/10.1111/sjos.70070) — Nonparametric Cure Models Through Extreme‐Value Tail Estimation
- **作者**: Jan Beirlant, Martin Bladt, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 984-1000
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在生存分析的治愈模型设定下，当随访不足（删失分布支撑集小于目标分布）时，非参数估计治愈率十分困难。本文假设易感人群分布属于 Gumbel 或 Fréchet 最大吸引域，利用极值理论提出联合估计治愈率与极值指数的新方法。核心机制采用概率作图法提取次序统计量顶部信息，并在 Gumbel 域下引入 Peaks-over-Threshold (POT) 方法。进一步将框架推广至 Pareto、对数正态和 Weibull 尾部模型，并在正则化条件下严格建立了估计量的渐近性质。模拟显示该方法在治愈率估计上优于传统模型，并在挪威出生登记流行病学数据中进行了实证。该文将极值理论与非参数尾部估计结合的渐近分析，可为您在非参数理论及流行病学数据应用中提供方法迁移参考。
- **关键技术**: `extreme value theory`, `Peaks-over-Threshold`, `max-domain of attraction`, `probability plotting`, `order statistics`
- **为什么对您有用**: 结合了非参数理论（极值尾部估计与渐近性质推导）与流行病学数据应用，契合您在非参数理论及流行病学队列数据上的双重兴趣，提供处理删失支撑集不足的新思路。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.70065](https://doi.org/10.1111/sjos.70065) — Robust estimation of change points in linear spline models with missing data
- **作者**: Xiang Xiao, Guangyu Yang, Min Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 883-918
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在线性样条模型下研究变点估计问题，设定中存在可能缺失的结果变量，目标是获得变点的一致且渐近正态估计。针对缺失结果导致的变点估计偏差，本文提出逆概率加权（IPW）、双重稳健增广逆概率加权（DR-AIPW）及结果回归（OR）三种估计器，并给出两步法算法实现。理论上证明了这些估计器的一致性与渐近正态性；特别地，DR-AIPW 估计器具有双重稳健性，且通过半参数理论验证了其最优性（达到半参数有效界）。模拟与实际数据表明，不当处理缺失数据会导致变点估计偏差，而所提方法有效纠正了该偏差。该文将因果推断中经典的 IPW/AIPW 缺失数据框架与半参数效率理论结合应用于变点模型，对您在效率理论（半参数有效界验证）及缺失/因果推断方法迁移方面的研究有直接参考价值。
- **关键技术**: `inverse probability weighting (IPW)`, `doubly robust augmented inverse probability weighting (DR-AIPW)`, `semiparametric efficiency bound`, `linear spline models`, `change point estimation`, `two-step estimation`
- **为什么对您有用**: 将因果推断/缺失数据中经典的 IPW/AIPW 框架与半参数效率理论应用于变点估计，对您在效率理论（半参数有效界验证）及缺失数据/因果推断方法向其他模型迁移的研究有直接参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.70063](https://doi.org/10.1111/sjos.70063) — Testing independence between high‐dimensional random vectors using rank‐based max‐sum tests
- **作者**: Hongfei Wang, Binghui Liu, Long Feng
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 821-847
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究两个高维随机向量之间的独立性检验问题，在无特定分布假设的非参数设定下构建检验统计量。提出基于秩相关的 max-sum 检验，整合了 Spearman's ρ、Kendall's τ、Hoeffding's D 及 Bergsma-Dassios-Yanagimoto's τ* 等经典非参数秩度量。通过 max 形式捕捉稀疏备择假设下的强信号，sum 形式捕捉稠密备择假设下的弱信号累积，从而在两种高维备择假设下均保持稳健功效。由于采用秩统计量，检验过程具有分布自由性且能有效捕捉非线性相依结构。理论与大量数值结果表明该检验在稀疏和稠密备择假设下均表现稳健，并在 RNA 微阵列数据中得到了实证验证。该工作直接结合了您关注的高维统计与假设检验方向，其基于非参数秩方法处理非线性相依及稀疏/稠密备择假设的思路，可为高维推断提供分布自由的检验工具。
- **关键技术**: `rank-based correlations`, `max-sum test statistic`, `high-dimensional independence testing`, `nonlinear dependence`, `sparse and dense alternatives`
- **为什么对您有用**: 直接结合您关注的高维统计与假设检验方向，其基于非参数秩方法处理非线性相依及稀疏/稠密备择假设的思路，可为高维推断提供分布自由的检验工具。

### 2. [10.1111/sjos.70064](https://doi.org/10.1111/sjos.70064) — Powerful kernel‐based association tests for multivariate responses
- **作者**: Mingya Long, Yuke Shi, Liuquan Sun, Qizhai Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 848-882
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在多变量响应与协变量的依赖性检验设定下，本文基于再生核希尔伯特空间（RKHS）框架提出了一系列核独立性检验方法。构造了最大核独立性检验（MKIT）与极大极小有效稳健检验（MERT），并给出了检验统计量的显式样本表达式。理论上证明了在特定正则条件下，MKIT与MERT的渐近零分布分别收敛至极值I型Gumbel分布与正态分布，并分析了二者的检验势性质。模拟与遗传/影像数据应用显示其优于现有方法；对您有用之处在于，该文将极值理论与RKHS结合推导多变量假设检验的渐近分布，为您在非参数检验与假设检验方向提供了新的构造与理论分析思路。
- **关键技术**: `RKHS`, `kernel-based independence test`, `extreme-value type I-Gumbel distribution`, `maximin efficient robust test`, `asymptotic null distribution`
- **为什么对您有用**: 直接关联您在数学统计中的假设检验与非参数理论兴趣；MKIT的极值渐近分布推导与MERT的极大极小效度分析，为多变量非参数检验提供了可迁移的理论工具与构造思路。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.70062](https://doi.org/10.1111/sjos.70062) — Online differentially private inference for linear regression model
- **作者**: Senlin Yuan, Fang Liu, Xuerong Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 798-820
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究流数据下线性回归模型的差分隐私在线估计与推断问题，目标是在 ε-差分隐私约束下对回归系数进行在线更新与置信区间构造。提出了一种计算高效的在线更新算法，通过引入 Gaussian 噪声机制并修正其对协方差的影响，推导出参数的差分隐私估计量及其协方差矩阵的显式表达。基于修正后的协方差估计，构建了回归系数的差分隐私置信区间，并提供了估计量的渐近正态性与区间覆盖率的严格理论保证。数值实验表明该方法在有限隐私预算下仍保持较好的覆盖率与估计精度。对您可能有用：该文将在线算法与隐私保护下的渐近推断结合，其在线更新机制和协方差修正思路可为统计计算（在线算法）和假设检验（置信区间构造）提供方法学参考。
- **关键技术**: `differential privacy`, `online updating algorithm`, `asymptotic normality`, `confidence interval construction`, `streaming data inference`
- **为什么对您有用**: 涉及统计计算（在线更新算法）与假设检验（置信区间构造），其流数据下的在线推断与协方差修正思路可为在线算法设计与推断理论提供参考。

### 2. [10.1111/sjos.70061](https://doi.org/10.1111/sjos.70061) — Dimension reduction for optimal design problems with Kronecker product structure
- **作者**: Taras Bodnar, Maryna Prus
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 763-797
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文针对多环境作物品种测试中的试验最优分配问题，研究信息矩阵具有Kronecker乘积结构的设计准则优化。作者推导了两个Kronecker乘积之和的逆矩阵的一般公式，借此将Kronecker-Bayesian线性准则（即两Kronecker乘积之和的逆的迹）重写为复合贝叶斯风险准则。基于该准则的凸性与可微性，建立了近似设计的最优性条件，并提出一种降维方法以高效逼近最优设计。该降维方法允许预先设定独立于真实最优设计的效率损失上界，且支持在成本等线性约束下求解。文中推导的Kronecker乘积求逆公式及降维算法对您在统计计算（矩阵数值方法）方向的兴趣有直接参考价值，该代数结果也可迁移至多元时间序列或控制理论中的矩阵计算。
- **关键技术**: `Kronecker product inverse`, `optimal design`, `dimension reduction`, `Bayesian linear criterion`, `compound Bayes risk`
- **为什么对您有用**: 推导了两个Kronecker乘积之和的显式逆矩阵公式，直接契合您在统计计算（矩阵数值方法）方向的兴趣，且该代数结果可迁移至高维统计或时间序列中的协方差矩阵计算。

## 其他  *(other, 2 篇)*

### 1. [10.1111/sjos.70054](https://doi.org/10.1111/sjos.70054) — Spatial depth for data in metric spaces
- **作者**: Joni Virta
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 684-711
- 相关性 2/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "本文针对任意度量空间中的数据，提出了一种新的统计深度度量——metric spatial depth，目标是量化点相对于数据分布主体的中心性/离群性。该深度在欧氏空间下退化为经典的 spatial depth，其核心构造依赖于度量空间中的距离函数来定义"方向"与"中心"的类比。作者证明了该深度具有可解释的公理性质（如仿射不变性在欧氏情形的恢复、最大深度点与中位数的联系），并在多个具体度量空间（如 Wasserstein 空间、图空间等）中显式计算了深度值以建立直觉。实证部分展示了该方法在异常检测、非凸深度区域估计和分类中的实用性。对您而言，这属于非参数统计深度方法的度量空间推广，虽不直接涉及效率界或因果推断，但其度量空间框架下的深度构造思路可迁移至您关注的非参数/半参数理论中处理复杂数据对象的场景。",
  "key_techniques": [
    "spatial depth",
    "metric space generalization",
    "depth region estimation",
    "outlier detection via depth",
    "object data analysis"
  ],
  "why_relevant"

### 2. [10.1111/sjos.70047](https://doi.org/10.1111/sjos.70047) — Spectral characteristics of Harmonizable VARMA processes
- **作者**: Dominique Dehay, Anna E. Dudek, Jean‐Marc Freyermuth
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 613-647
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文在非平稳谐和过程框架下，提出了参数化的谐和向量自回归滑动平均模型（HVARMA），将其定义为基于谐和噪声的差分方程的唯一解。作者推导了该模型的谱特征，并在基础情形下研究了最小二乘（LS）参数估计的渐近性质；特别地，在爆炸区间的特定情形下，推导出了非标准的渐近分布。通过引入周期平稳VARMA过程来建模谐和噪声的二阶平稳依赖，定义了HVARMA-模型，并刻画了其谱性质。此外，文中还提供了生成此类非平稳过程样本路径的有效算法，并通过模拟展示了其捕捉多种非平稳行为的能力。对您而言，其爆炸区间下LS估计的非标准渐近律推导对数学统计渐近理论有参考价值，而样本生成算法对统计计算中的数值模拟方法有直接借鉴意义。
- **关键技术**: `Harmonizable processes`, `VARMA models`, `spectral distribution`, `least-squares estimation`, `explosive regime asymptotics`, `periodic stationary process`
- **为什么对您有用**: 本文涉及参数估计的非标准渐近分布与样本生成算法，与您在数学统计（渐近理论）和统计计算（数值模拟生成）方面的兴趣有边缘交集，可提供特定时间序列模型下的渐近性质参考。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

