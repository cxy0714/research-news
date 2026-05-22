# Scand. J. Stat. — Vol 53  Issue 2  ·  2026-05-21

- 共 14 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.70055](https://doi.org/10.1111/sjos.70055) — Interval identification of natural effects in the presence of outcome‐related unmeasured confounding
- **作者**: Marco Doretti, Elena Stanghellini
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 712-734
- 相关性 10/10 · novelty: `weaker_assumption`
- **摘要**: 在二值处理、中介与结局设定下，本文研究存在与结局相关的未测量混杂时自然效应的区间识别问题，仅假设无未测暴露-中介混杂及 PC-CWD 和 LC 条件。该方法放松了传统中介分析中强不可检验的跨世界独立性假设，允许总效应不再被点识别而是区间识别。核心机制是为中介和结局指定半参数逻辑模型（解释变量的函数形式任意），据此推导自然效应的识别界。推断方面，利用 delta 方法近似标准误以构建不确定性区间。模拟与西班牙前瞻性队列（吸烟-肺气肿-肺癌）应用验证了方法实用性。对您有用：直接推进了因果推断中 mediation 的 partial identification 理论，且半参数界估计与 delta 方法的框架对您在流行病学数据上的应用因果分析有迁移价值。
- **关键技术**: `partial identification`, `natural direct/indirect effects`, `cross-world independence relaxation`, `semiparametric logistic model`, `delta method`
- **为什么对您有用**: 直接推进了因果推断中 mediation 的 partial identification 理论，放松了强不可检验的跨世界独立性假设；同时半参数界估计与 delta 方法的框架，对您在流行病学队列数据上的应用因果推断工作有直接迁移价值。

### 2. [10.1111/sjos.70060](https://doi.org/10.1111/sjos.70060) — Sensitivity analysis for generalized estimating equation with non‐ignorable missing data
- **作者**: Hui Gong, Kin Wai Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 735-762
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在纵向/聚类数据的广义估计方程（GEE）框架下，针对非随机缺失（MNAR）问题提出了一种新的多重敏感性模型（MSM）分析框架。给定用户指定的敏感性参数，通过求解 MSM 辅助 GEE 的根界获得一系列估计量；进一步推导出估计量的分解表示，将其拆解为若干更简单的子估计量，从而量化不同缺失模式对参数估计的具体影响。理论上，文章提出了渐近有效的百分位 Bootstrap 置信域构建方法并给出了严格证明。实证结果验证了该敏感性分析框架的实用性。该方法将 MNAR 敏感性分析系统嵌入 GEE 框架，对您在纵向因果推断中的敏感性分析（primary interest）及半参数边际模型推断具有直接的参考价值。
- **关键技术**: `generalized estimating equation`, `missing not at random`, `sensitivity analysis`, `multiple sensitivity models`, `bootstrap confidence region`
- **为什么对您有用**: 直接关联您在因果推断中的敏感性分析（primary interest）和纵向数据设定，提供了一种在 GEE 框架下处理 MNAR 的可计算敏感性参数化方法，对放松 MAR 假设的推断有借鉴意义。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.70071](https://doi.org/10.1111/sjos.70071) — High‐Dimensional Inference for Single‐Index Models With Latent Factors
- **作者**: Yanmei Shi, Meiling Hao, Yanlin Tang, Heng Lian, Xu Guo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 1001-1027
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维因子增强单指标模型（factor-augmented single-index model）下，研究潜在因子的必要性检验与回归系数的惩罚估计及推断问题。作者提出一种 score-type 检验统计量判断是否需要引入因子增强成分，该检验无需估计高维回归系数或精度矩阵，计算更简便稳定；临界值通过 Gaussian multiplier bootstrap 确定，并在温和正则条件下建立其理论有效性。惩罚估计部分，在潜在因子被估计的条件下给出了估计量的误差界；进一步基于 debiased 估计量构造单个系数的置信区间。值得注意的是，方法不要求误差项的矩条件，对重尾或含异常值的误差仍适用。该文将高维因子模型从线性推广至半参数单指标结构，对您在高维推断（debiased inference）与半参数效率理论交叉方向的工作有直接参考价值。
- **关键技术**: `factor-augmented single-index model`, `score-type test`, `Gaussian multiplier bootstrap`, `debiased estimation`, `penalized M-estimation with estimated factors`, `heavy-tailed robust inference`
- **为什么对您有用**: 直接连接您的高维统计与半参数理论两个 primary interest：score test 绕过精度矩阵估计的思路可迁移至其他高维检验场景，debiased estimator 在因子被估计条件下的推断框架对高维 semiparametric efficiency bound 研究有借鉴意义。

### 2. [10.1111/sjos.70066](https://doi.org/10.1111/sjos.70066) — Lasso‐type estimator and classification algorithm for high‐dimensional multivariate Hawkes processes
- **作者**: Christophe Denis, Charlotte Dion‐Blanc, Romain E. Lacoste, Laure Sansonnet
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 919-968
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维多元Hawkes过程(MHP)在短时间区间重复观测下的交互网络恢复与监督分类问题，假设网络维度相对于观测数较大且邻接矩阵稀疏。针对每一类数据，作者提出Lasso-type估计量以恢复邻接矩阵的支持集，并在适当的正则性假设下证明了支持集估计的相合性。基于估计的支持集，进一步构建了由分类准则引导的重拟合步骤。随后，利用经验误差最小化提出监督分类算法，并严格给出了分类器的收敛速率。合成与真实数据的数值实验支持了理论发现。对您有用：该文将高维Lasso支持集恢复理论拓展至事件型点过程，其高维稀疏估计与收敛速率分析对您关注的高维统计方向具有参考价值。
- **关键技术**: `Lasso-type estimator`, `support recovery consistency`, `high-dimensional Hawkes process`, `sparse adjacency matrix`, `empirical error minimization`, `convergence rates`
- **为什么对您有用**: 将高维稀疏估计（Lasso）与支持集恢复理论应用于事件型点过程，其高维邻接矩阵的估计与收敛速率分析直接契合您对高维统计方向的兴趣。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.70053](https://doi.org/10.1111/sjos.70053) — Extended generalized Marshall–Olkin model for dependent censoring
- **作者**: Salima Helali
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 648-683
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在依赖竞争风险与删失设定下，研究扩展 Marshall-Olkin (EMO) 模型的估计问题，目标 estimand 为边际生存分布与联合生存概率。作者首先刻画了 EMO 模型对应生存 Copula 的概率性质，并基于此构建估计框架。核心估计策略采用 Bernstein 多项式（sieve 方法）对边际分布与联合生存概率进行非参数逼近。在标准正则条件下，证明了该 sieve 估计量具有渐近正态性（n^{-1/2}-CAN）。仿真与真实数据验证了方法的有限样本表现。对您而言，该文将 Bernstein 多项式 sieve 估计应用于依赖删失 Copula 的技巧，可为 semiparametric/nonparametric theory 中的 sieve 估计渐近性质研究，以及 epidemiology 队列生存分析中的依赖删失问题提供方法借鉴。
- **关键技术**: `dependent censoring`, `Marshall-Olkin copula`, `Bernstein polynomial sieve`, `asymptotic normality`, `competing risks`
- **为什么对您有用**: 论文涉及依赖删失下的非参数 sieve 估计与渐近正态理论，与您的 semiparametric/nonparametric theory 兴趣直接相关；同时依赖删失是流行病学队列研究中常见的因果识别/估计挑战，方法可迁移至 epidemiology 应用。

### 2. [10.1111/sjos.70054](https://doi.org/10.1111/sjos.70054) — Spatial depth for data in metric spaces
- **作者**: Joni Virta
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 684-711
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在一般度量空间设定下提出新的统计深度度量——metric spatial depth，用于量化数据点的中心性与离群性。该度量在欧氏空间下退化为经典 spatial depth，但在任意度量空间中仍保持高度可解释性，适用于传统描述统计失效的 object data analysis。作者在多种具体度量空间中显式计算了该深度，并证明了其理论性质。实证部分展示了其在异常值检测、非凸深度区域估计和分类任务中的实用性。对您而言，若研究涉及非参数理论中的深度概念或复杂空间下的统计计算，此度量空间推广思路可作参考，但与您核心关注的效率理论或因果推断距离较远。
- **关键技术**: `metric spatial depth`, `statistical depth`, `object data analysis`, `outlier detection`, `non-convex depth region`
- **为什么对您有用**: 涉及非参数理论中的统计深度概念与复杂空间下的统计计算，若您在非参数设定下需要度量中心性或处理 object data，该度量空间推广思路可作参考，但与核心的效率/因果推断距离较远。

### 3. [10.1111/sjos.70069](https://doi.org/10.1111/sjos.70069) — Smooth and Rough Sample Paths in Mean Derivative Estimation for Functional Data
- **作者**: Max Berger, Hajo Holzmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 969-983
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在多元函数数据的固定同步设计下，研究 Hölder 光滑类中均值函数偏导数估计的 minimax 最优收敛速率。与均值估计不同，导数估计的收敛性质关键取决于样本路径的光滑度：当样本路径粗糙（光滑阶数低于待估导数阶数）时，文章给出了比参数速率更慢的新颖最优收敛速率；当样本路径足够光滑且设计稠密时，仍可达到参数 n^{-1/2} 速率。理论分析在 sup-norm 下进行，并推导了连续函数空间（装备 sup-norm）的中心极限定理，为构建均匀置信带奠定基础。方法上实现了多元局部多项式导数估计量，并提出通过比较协方差核偏导数的受限估计来判断样本路径光滑度。对您有用：该文的 minimax 速率分析与 sup-norm CLT 直接契合您的非参数理论兴趣，且函数数据导数推断对纵向因果推断中的动态机制评估有方法迁移价值。
- **关键技术**: `minimax convergence rate`, `Hölder smoothness class`, `local polynomial estimation`, `supremum norm CLT`, `uniform confidence band`, `functional data derivative estimation`
- **为什么对您有用**: 直击您在非参数理论方面的 primary interest，其 sup-norm 下的 minimax 速率与 CLT 结果对函数/纵向数据的推断（如动态因果机制）有直接迁移价值。

### 4. [10.1111/sjos.70070](https://doi.org/10.1111/sjos.70070) — Nonparametric Cure Models Through Extreme‐Value Tail Estimation
- **作者**: Jan Beirlant, Martin Bladt, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 984-1000
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随访不充分（删失支撑集小于目标分布支撑集）的生存分析设定下，目标是估计永远不会发生事件的治愈率，假设易感人群分布属于 Fréchet 或 Gumbel 最大吸引域。本文提出基于极值技术的概率作图法，利用最高次序统计量的全部信息，联合估计治愈率与极值指数；在 Gumbel 最大域假设下构建了 Peaks-over-Threshold (POT) 估计量，并将其推广至 Pareto、对数正态和 Weibull 尾部模型以捕捉尾部特征。在正则化条件下建立了估计量的渐近性质，模拟显示其表现优于现有模型，并应用于挪威出生登记数据。对您而言，该文展示了非参数理论中极值方法与删失数据的结合，其渐近正则化技术对处理支撑集不重合的半参数/非参数识别问题有参考价值。
- **关键技术**: `extreme value theory`, `Peaks-over-Threshold`, `order statistics`, `cure rate estimation`, `asymptotic regularization`, `Gumbel max-domain of attraction`
- **为什么对您有用**: 涉及非参数理论中的渐近正则化与极值估计，且应用了流行病学出生登记数据；对处理支撑集不重合的半参数识别问题及流行病学队列数据分析有方法论参考价值。

### 5. [10.1111/sjos.70065](https://doi.org/10.1111/sjos.70065) — Robust estimation of change points in linear spline models with missing data
- **作者**: Xiang Xiao, Guangyu Yang, Min Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 883-918
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在线性样条模型下研究变点估计，设定中结果变量存在缺失，关键假设为缺失机制满足 MAR 且倾向得分或结果回归模型至少一个正确。提出了逆概率加权（IPW）、插补法结果回归（OR）以及双重稳健的增广逆概率加权（DR-AIPW）三种估计量，并构建了两步法算法实现。理论上证明了这些估计量的一致性与渐近正态性，其中 DR-AIPW 估计量具有双重稳健性，且通过半参数理论验证了其达到半参数有效界。模拟与实际数据表明，不当处理缺失会导致变点估计有偏，而 DR-AIPW 在模型误设下仍保持稳健且有效。对您有用：该文将 DR-AIPW 与半参数有效界应用于变点估计，直接契合您在 efficiency theory (semiparametric efficiency bounds) 及 causal inference (IPW/AIPW) 方面的兴趣，展示了缺失数据下变点估计的效率理论推导范式。
- **关键技术**: `inverse probability weighting (IPW)`, `doubly robust AIPW`, `semiparametric efficiency bound`, `change point estimation`, `linear spline model`, `missing at random (MAR)`
- **为什么对您有用**: 直接契合您在 efficiency theory (semiparametric efficiency bounds) 方向的 primary interest，展示了如何在变点估计中推导并验证 DR-AIPW 估计量的半参数有效性；同时 IPW/AIPW 框架与您 causal inference 中的缺失数据/可忽略性假设处理高度同源，方法可迁移。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.70063](https://doi.org/10.1111/sjos.70063) — Testing independence between high‐dimensional random vectors using rank‐based max‐sum tests
- **作者**: Hongfei Wang, Binghui Liu, Long Feng
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 821-847
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究两个高维随机向量之间的独立性检验问题，在无分布假设的设定下提出基于秩相关的 max-sum 检验统计量。方法聚合了三类经典秩相关系数（涵盖 Spearman's ρ、Kendall's τ、Hoeffding's D、BKR's R 与 BDY's τ*），通过 max-sum 形式同时捕获稀疏与稠密备择假设下的非线性相依结构。这些秩度量本质上是（高阶退化）U-统计量，其高维极限行为依赖于相应的投影与经验过程分析。理论结果表明所提检验具有分布自由性，且数值模拟与 RNA 微阵列数据应用证实其在多种备择假设下保持稳健的势。对您有用：该工作将高阶 U-统计量与高维假设检验的 max-sum 聚合框架结合，直接关联您对高维统计与假设检验的兴趣，并为高维非线性相依度量的推断提供了分布自由的思路。
- **关键技术**: `max-sum test aggregation`, `rank-based correlation`, `high-dimensional independence testing`, `degenerate U-statistics`, `distribution-free test`
- **为什么对您有用**: 直接关联您的高维统计与假设检验兴趣；文中使用的 Hoeffding's D 等秩相关本质上是高阶退化 U-统计量，其高维极限理论对您研究 higher-order U-statistics 在高维检验中的应用有直接参考价值。

### 2. [10.1111/sjos.70064](https://doi.org/10.1111/sjos.70064) — Powerful kernel‐based association tests for multivariate responses
- **作者**: Mingya Long, Yuke Shi, Liuquan Sun, Qizhai Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 848-882
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在 RKHS 框架下提出一系列核独立性检验，用于检测协变量与多元响应之间的依赖关系，目标是在正则条件下获得检验统计量的显式样本表达式与渐近零分布。核心方法包括两类具体检验：MKIT（极大核独立性检验）取多个核函数对应统计量的最大值，渐近服从极值 I 型 Gumbel 分布；MERT（极大极小有效稳健检验）通过线性组合核函数实现 maximin 功效，渐近服从正态分布。理论上给出了两种检验的渐近分布证明与功效分析，MKIT 的 Gumbel 极值分布推导涉及核矩阵最大特征值的极端值理论。模拟与小鼠基因数据、人类连接组项目数据的应用表明 MKIT 和 MERT 在多种场景下优于现有核检验方法。对您有用：该工作将 RKHS 核检验与极值渐近理论结合，直接关联您在假设检验与非参数理论方面的兴趣，MKIT 的 Gumbel 渐近分布推导技术可迁移至其他高维检验问题。
- **关键技术**: `RKHS kernel independence test`, `extreme-value type I Gumbel distribution`, `maximin efficient robust test (MERT)`, `kernel matrix eigenvalue extreme-value theory`, `U-statistic representation of kernel tests`
- **为什么对您有用**: 直接关联您在假设检验与非参数理论的 primary interest；MKIT 的 Gumbel 极值渐近分布推导为高维核检验提供了新的理论工具，MERT 的 maximin 功效思路可迁移至其他稳健检验场景。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.70062](https://doi.org/10.1111/sjos.70062) — Online differentially private inference for linear regression model
- **作者**: Senlin Yuan, Fang Liu, Xuerong Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 798-820
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在差分隐私（differential privacy）框架下，针对流式数据（streaming data）提出线性回归参数的在线更新与推断方法。核心估计量基于在线梯度下降或递推更新，注入适当校准的噪声以满足 ε-差分隐私；同时推导了参数的协方差估计，据此构建隐私保护的置信区间。理论上给出了估计量的收敛性保证与隐私-效用权衡分析，数值实验验证了有限样本下置信区间的覆盖性质。该方法填补了流式数据下差分隐私统计推断的空白，计算效率高且无需存储全部历史数据。对您而言，在线递推算法的设计思路可迁移至统计计算方向，但差分隐私本身与您核心兴趣（效率理论、半参数推断）的直接关联有限。
- **关键技术**: `differential privacy mechanism`, `online streaming update`, `linear regression inference`, `privacy-preserving confidence interval`, `noise calibration for privacy-utility tradeoff`
- **为什么对您有用**: 在线递推算法的设计与统计计算兴趣相关，置信区间构建触及假设检验方向，但差分隐私框架本身与您核心的效率理论/半参数推断方向距离较远，收益主要在计算方法层面。

### 2. [10.1111/sjos.70061](https://doi.org/10.1111/sjos.70061) — Dimension reduction for optimal design problems with Kronecker product structure
- **作者**: Taras Bodnar, Maryna Prus
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 763-797
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 在多环境作物品种测试的最优试验分配问题中，目标是优化信息矩阵具有 Kronecker 乘积结构的设计准则。本文考虑 Kronecker-Bayesian 线性准则（即两个 Kronecker 乘积之和的逆的迹），推导了此类矩阵求逆的新一般公式。基于该公式，将原准则重写为复合 Bayes 风险准则，并利用凸性与可微性建立了近似设计的最优性条件。提出了一种降维方法，允许预先设定独立于真实最优设计的效率损失上界，从而在成本等线性约束下高效求解。该矩阵求逆公式也可推广至控制论和多变量时间序列分析。对您可能有用：推导的 Kronecker 乘积之和求逆公式直接丰富了您在统计计算（矩阵代数）方向的工具箱，且降维思路对高维信息矩阵的快速计算有参考价值。
- **关键技术**: `Kronecker product structure`, `matrix inversion formula`, `optimal experimental design`, `Bayesian linear criterion`, `dimension reduction`
- **为什么对您有用**: 推导的两个 Kronecker 乘积之和的矩阵求逆公式直接契合您在统计计算（矩阵、张量数值方法）方向的兴趣，且该代数技巧在多变量时间序列等高维协方差矩阵计算中具有迁移价值。

## 其他  *(other, 1 篇)*

### 1. [10.1111/sjos.70047](https://doi.org/10.1111/sjos.70047) — Spectral characteristics of Harmonizable VARMA processes
- **作者**: Dominique Dehay, Anna E. Dudek, Jean‐Marc Freyermuth
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 2 · pp 613-647
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在非平稳谐和过程框架下，本文引入谐和向量自回归滑动平均（HVARMA）模型，将其定义为基于谐和噪声的差分方程的唯一解。作者推导了该模型的谱分布特征，并在基础情形下研究了最小二乘参数估计的渐近性质，特别在爆炸区（explosive regime）下获得了非标准的渐近分布。文中还提出了一种有效的过程模拟生成方法，通过周期平稳VARMA过程刻画谐和噪声，衍生出HVARMA-模型并分析其谱性质。对您而言，本文在爆炸区估计的非常规渐近律对数学统计渐近理论有一定参考，但整体属于参数时间序列范畴，与您核心的高维/半参数/因果推断方向距离较远。
- **关键技术**: `Harmonizable processes`, `VARMA models`, `spectral distribution`, `least-squares estimation`, `explosive regime asymptotics`, `periodic stationary process`
- **为什么对您有用**: 本文涉及参数时间序列的渐近理论（特别是爆炸区的非常规渐近分布），对数学统计与假设检验的渐近理论有边际参考价值，但核心设定与您的高维/半参数/因果推断主方向距离较远。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

