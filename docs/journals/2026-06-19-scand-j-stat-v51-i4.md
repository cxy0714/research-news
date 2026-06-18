# Scand. J. Stat. — Vol 51  Issue 4  ·  2026-06-19

- 共 16 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 16 篇全部抓到（对照 OpenAlex 18 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

第一段：本期主攻四条主线——因果推断中的平衡与效应估计（Mahalanobis balancing、竞争风险重抽样、非线性路径公式、连续时间贝叶斯网络结构学习）、非参数与半参数估计效率（高维加性模型子空间学习、单调回归置信区间、梯度充分降维、条件拟似然推断、贝叶斯混合模型不一致性）、高维稳健推断（双去偏迁移学习中的自适应Huber回归）、以及结构学习与网络建模（连续时间贝叶斯网络、超图随机块模型、矩阵重构）。另有极值条件尾矩估计与两篇历史综述（C.R.Rao、Cox），作为补充方向。

第二段：因果推断方向聚焦于不同技术路径。Mahalanobis balancing 用二次约束整体控制协变量不平衡，对偶性揭示其与正则化回归的联系，并给出阈值选择程序与渐近正态性。竞争风险重抽样证明三种bootstrap对g‑formula弱收敛过程的渐近有效性，填补理论空白。非线性路径公式针对logistic与Cox模型构造直接/间接效应的近似分解，给出误差界。连续时间贝叶斯网络结构学习以惩罚似然实现有向图发现，在稀疏性条件下证明高概率恢复，直接服务于因果图推断。四篇覆盖平衡、生存因果、中介分解、图结构学习，形成互补。

第三段：非参数/半参数主线的五个工作各有侧重。高维加性模型利用子空间学习降低加性函数维数，在子空间近似误差可控时获得快于经典加性模型的收敛速度，并实现变量选择一致性。单调回归的SLSE bootstrap相比于bootstrap非参数LSE取得n^{-1/2}一致性与逐点渐近分布，还比较了Studentization与自动带宽。梯度充分降维用条件分布梯度估计中心降维子空间，仅需平滑性条件，通过FPCA实现弱化了线性假设。条件拟似然在聚类失效时间下构建frailty比例平均剩余寿命模型，用PQL+IPCW估计方程而无须指定frailty分布，具n^{-1/2}‑CAN性。贝叶斯混合模型论证了Gibbs型过程先验下聚类数后验不一致性，延续对先验敏感性的理论讨论。

第四段（可选）：与因果推断、半参数效率、高维方向最贴的优先阅读：因果推断四篇（Mahalanobis balancing、竞争风险重抽样、非线性路径公式、连续时间贝叶斯网络结构学习）；非参数/半参数中的高维加性模型子空间学习与单调回归置信区间；高维稳健推断中的双去偏迁移学习（自适应Huber回归的去偏推断）。此外，梯度充分降维和条件拟似然也适合关注纵向/生存因果推断的读者。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1111/sjos.12721](https://doi.org/10.1111/sjos.12721) · [arXiv](https://arxiv.org/abs/2204.13439) — Mahalanobis balancing: A multivariate perspective on approximate covariate balancing
- **作者**: Yimin Dai, Ying Yan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1450-1471
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该文针对因果推断中协变量平衡问题，提出了一种名为 Mahalanobis balancing 的近似平衡方法。传统精确平衡法在处理协变量重叠差或高维情况时可能不可行，而近似平衡虽用不等式矩约束缓解这一问题，但阈值选择困难且无法充分捕捉分布差异。本文从多元视角出发，使用二次约束（Mahalanobis 距离）来整体控制不平衡，仅需单个阈值参数，并给出了简单的选择程序。作者证明了对偶问题等价于一个基于范数的正则化回归，这建立了与倾向得分模型的深层联系。文章推导了估计量的渐近性质（如 n^{-1/2} 一致性和正态性），并讨论了高维情形下的理论保证。数值模拟和真实数据分析表明，该方法在平衡性能和后续因果估计精度上优于多种现有平衡方法。该工作对您的因果推断研究有直接参考价值，特别是其高维推广与您熟悉的高维渐近理论相契合，且所涉及的优化求解思路可与您的统计计算经验结合。
- **关键技术**: `Mahalanobis balancing`, `approximate covariate balancing`, `quadratic constraint`, `dual problem`, `regularized regression`, `propensity score model`
- **为什么对您有用**: 本文直接涉足您的首要兴趣——因果推断中的协变量平衡估计，是近似平衡方法的新进展。您非常熟悉的 estimation theory in causal inference 和高维渐近理论可用来验证其理论声称的率是否最优，例如用 minimax lower bound 检验其收敛速度的紧致性。方法本身涉及正则化优化，与您的统计计算背景契合，属于立即可做的延伸方向：可通过撰写讨论或小型模拟来评估其在复杂高维数据下的鲁棒性，并考虑引入更高效的优化算法。

### 2. [10.1111/sjos.12714](https://doi.org/10.1111/sjos.12714) · [arXiv](https://arxiv.org/abs/2306.02970) — Asymptotic properties of resampling‐based processes for the average treatment effect in observational studies with competing risks
- **作者**: Jasmin Rühl, Sarah Friedrich
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Augsburg
- **分类**: vol 51 · issue 4 · pp 1506-1532
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 针对具有竞争风险的观察性时间-事件数据，本文研究用g-formula估计平均治疗效应时，其随机过程的渐近分布复杂，难以直接构造置信区间或时间同步置信带。作者考察了三种重抽样方法（包括非参数bootstrap）在此设定下的大样本性质，并证明了它们在处理竞争风险时的渐近有效性。理论证明依赖于对g-formula估计量作为随机过程的弱收敛性分析，以及重抽样过程的相合性。通过模拟和实际数据分析（身体活动对膝骨关节炎患者膝关节置换风险的影响）展示了方法的应用。该工作填补了竞争风险框架下重抽样方法渐近理论的空白，为实践提供了理论保障。对于您从事因果推断（尤其是纵向数据和生存分析中的因果效应估计）的研究，该文的渐近论证可直接借鉴，且您熟悉的非参数统计和因果推断估计理论（如g-formula）能帮助深入理解其收敛性证明。此问题属于您“立即可做”的范畴。
- **关键技术**: `g-formula`, `nonparametric bootstrap`, `perturbation resampling`, `competing risks`, `time-simultaneous confidence bands`, `weak convergence of stochastic processes`
- **为什么对您有用**: 本文直接针对您primary interest中因果推断的纵向数据子方向（时间-事件 + 竞争风险），提供了三种重抽样方法的渐近理论证明。您武器库中的“非参数统计”和“因果推断估计理论”正好可用来评估其收敛性论证的严谨性，甚至考虑能否将类似重抽样策略推广到您更感兴趣的proximal causal inference或mediation setting。这篇论文属于立即可做的理论消化，无硬性知识缺口。

### 3. [10.1111/sjos.12753](https://doi.org/10.1111/sjos.12753) — Some approximations to the path formula for some nonlinear models
- **作者**: Christiana Kartsonaki
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Oxford
- **分类**: vol 51 · issue 4 · pp 1433-1449
- 相关性 7/10 · novelty: `minor`
- **摘要**: 在线性最小二乘回归中，暴露对结局的总效应可通过中间变量分解为直接与间接效应（路径公式/path formula）。本文旨在将此经典线性效应分解推广至非线性模型，重点考察 logistic 回归与 Cox 比例风险模型下的类似分解。核心方法是利用非线性模型中参数的近似关系，构造直接与间接效应的近似分解公式，而非依赖精确的乘性/加性分解。理论贡献在于给出了这些近似在特定参数设定下的误差界或渐近行为，但未涉及 semiparametric efficiency bound 或 influence function。对您可能有用：若研究 mediation 在非线性/生存模型中的 identification 与 estimation，本文的近似分解提供了一个对比基准，但方法学深度较浅。
- **关键技术**: `path analysis decomposition`, `mediation decomposition in nonlinear models`, `logistic regression effect decomposition`, `proportional hazards mediation approximation`
- **为什么对您有用**: 本文连接到 causal inference 的 mediation 子方向，但仅停留在参数模型的近似分解，未触及 semiparametric identification 或 efficient estimation。用您 very_familiar 的 minimax bounds 与 moderately_familiar 的 semiparametric theory / HOIF，可以审视其近似分解的误差是否可被更严格的 influence-function-based estimator 替代或改进。**中期可做**：需先在 moderately_familiar 的 semiparametric mediation identification 上长肌肉，才能将此参数近似提升到 semiparametric 效率框架下。

### 4. [10.1111/sjos.12747](https://doi.org/10.1111/sjos.12747) — Structure learning for continuous time Bayesian networks via penalized likelihood
- **作者**: Tomasz Ca̧kała, Błażej Miasojedow, Wojciech Rejchel, Maryia Shpak
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Warsaw · Nicolaus Copernicus University · Maria Curie-Skłodowska University
- **分类**: vol 51 · issue 4 · pp 1707-1729
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 连续时间贝叶斯网络（CTBN）是一类用于建模连续时间动态系统依赖结构的随机过程模型，广泛应用于生物学、社会科学和医学等领域。现有研究通常假设依赖结构已知，仅估计条件转移强度参数；本文则研究更具挑战性的结构学习问题，即从观测数据中推断有向图结构。作者提出基于惩罚似然的算法，通过在似然函数中添加L1正则化项实现边的选择与稀疏化。在温和正则条件（如稀疏图、可识别性）下，他们证明了该算法能以高概率正确恢复真实图结构，提供了统计一致性保证。数值模拟和实际数据分析进一步展示了方法的有限样本性能。对您而言，本文的结构学习思想是因果推断中因果图发现的关键步骤，尤其适用于纵向数据或连续时间因果模型，与您关注的因果推断（特别是动态系统识别）高度相关。
- **关键技术**: `penalized likelihood`, `L1 regularization`, `continuous time Bayesian networks`, `structure learning`, `graph recovery consistency`
- **为什么对您有用**: 本文直接针对CTBN的结构学习问题，属于因果推断中图发现方法的前沿，与您感兴趣的纵向因果模型和动态系统识别紧密相连。您可以利用熟悉的 high-dimensional asymptotics 和 estimation theory in causal inference 来分析惩罚似然估计的收敛性与一致性，评估其在弱假设下的最优性。后续研究为中期可做：虽然CTBN模型本身不在您的武器库中，但惩罚似然的工具（L1正则化、高维一致性）已具备，只需补充CTBN基础知识和连续时间马尔可夫过程的优化算法即可动手。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1111/sjos.12756](https://doi.org/10.1111/sjos.12756) — Asymptotically faster estimation of high‐dimensional additive models using subspace learning
- **作者**: Kejun He, Shiyuan He, Jianhua Z. Huang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Renmin University of China · Beijing Technology and Business University · Chinese University of Hong Kong, Shenzhen
- **分类**: vol 51 · issue 4 · pp 1587-1618
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 研究针对高维加性模型，利用自适应子空间学习（adaptive subspace learning）降低待估函数维数，提出简化加性模型的估计方法，并填补其渐近理论空白。该方法通过迭代算法同时学习共享子空间与加性成分函数，核心思想是假设加性函数共享一个低维子空间以减少未知参数。理论分析表明，即使简化模型仅为近似，只要子空间近似误差足够小，估计量的收敛速度仍快于传统加性模型（不进行子空间学习）。此外，方法能一致识别相关预测变量（变量选择一致性）。技术工具涉及非参数收敛速度、高维渐近、子空间辨识与偏差-方差权衡。该成果直接连接您的非参数统计和高维渐近兴趣，尤其为加性模型估计的收敛率改进提供了可推广的理论框架。
- **关键技术**: `adaptive subspace learning`, `reduced additive model`, `nonparametric convergence rate`, `variable selection consistency`, `high-dimensional additive models`
- **为什么对您有用**: 本文直接对应您的非参数统计与高维渐近兴趣，特别是通过子空间学习提升加性模型收敛速度这一新思路。您武器库中的“高维渐近”和“非参数统计”可直接用于评估该收敛率是否最优，并探索将子空间学习推广至其他非参数结构（如多元加法模型）。**立即可做**：利用您熟悉的高维渐近工具，可以立即复现或扩展其理论结果，例如用minimax下界检验其速度的紧性。

### 2. [10.1111/sjos.12730](https://doi.org/10.1111/sjos.12730) · [arXiv](https://arxiv.org/abs/2303.17988) — Confidence intervals in monotone regression
- **作者**: Piet Groeneboom, Geurt Jongbloed
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1749-1781
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在单调回归设定下，目标是构造单调回归函数的置信区间；经典非参数 bootstrap 基于非参数 LSE 已被证明不一致。本文提出基于 SLSE（Smoothed Least Squares Estimator）的 bootstrap 方法，证明了其 n^{-1/2}-一致性，并推导了 SLSE 的逐点渐近分布。通过与 Nadaraya-Watson 估计器的置信区间对比，研究了 Studentization 的效果；同时给出了自动带宽选择方法，修正了 Sen and Xu (2015) 的结果。类似方法也应用于 current status 模型的置信区间构造，改进了 Groeneboom and Hendrickx (2018) 的工作。对您有用：本文处理的是形状约束非参数估计中的 bootstrap 一致性与逐点推断问题，直接关联非参数统计与 M-estimation 理论。
- **关键技术**: `smoothed least squares estimator`, `bootstrap consistency`, `monotone regression`, `current status model`, `Studentization`, `kernel bandwidth selection`
- **为什么对您有用**: 本文直接关联非参数统计与 M-estimation 理论子方向，解决形状约束下经典 bootstrap 失效的问题，属于该领域的经典推进。您武器库中 very_familiar 的非参数统计与 moderately_familiar 的 M-estimation 理论足以分析其 SLSE 的渐近性质与带宽选择机制。Follow-up 判断：立即可做——可用 minimax bound 视角验证其逐点收敛率是否紧，或用 M-estimation 理论审视其 Studentization 的 influence function 结构。

### 3. [10.1111/sjos.12724](https://doi.org/10.1111/sjos.12724) — Gradient‐based approach to sufficient dimension reduction with functional or longitudinal covariates
- **作者**: Ming‐Yueh Huang, Kwun Chuen Gary Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Institute of Statistical Science, Academia Sinica · University of Washington
- **分类**: vol 51 · issue 4 · pp 1567-1586
- 相关性 5/10 · novelty: `weaker_assumption`
- **摘要**: 在回归分析中研究实值响应与函数/纵向协变量的充分降维（SDR）问题，目标是估计中心降维子空间。现有逆回归类方法依赖线性条件，本文提出基于条件分布函数梯度的新估计方法，其有效性仅需人口参数的平滑性条件，显著弱化了分布假设。实际计算中，估计量可通过函数主成分分析（FPCA）的标准算法获得，避免了复杂的数值优化。理论上，在平滑性条件下证明了估计量的收敛性；模拟与两个实证例子验证了方法实用性。对您可能有用：该工作在纵向协变量设定下弱化SDR的线性假设，与您semiparametric/nonparametric理论及纵向因果推断的兴趣交汇。
- **关键技术**: `sufficient dimension reduction`, `conditional distribution gradient`, `functional principal component analysis`, `central subspace estimation`, `linearity condition relaxation`
- **为什么对您有用**: 直接连接到您semiparametric/nonparametric理论及纵向因果推断的子方向：在纵向协变量下弱化SDR的线性条件，用平滑性替代，属于weaker_assumption类推进。您武器库中very_familiar的nonparametric statistics与moderately_familiar的semiparametric theory足以审视其收敛率是否可达semiparametric efficiency bound，或能否嵌入纵向因果的estimation pipeline。**立即可做**：用nonparametric minimax bound工具检查其声称的rate是否紧，或尝试将gradient-based SDR与HOIF结合做更高阶校正。

### 4. [10.1111/sjos.12746](https://doi.org/10.1111/sjos.12746) — Conditional quasi‐likelihood inference for mean residual life regression with clustered failure time data
- **作者**: Rui Huang, Liuquan Sun, Liming Xiang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Nanyang Technological University · Chinese Academy of Sciences · Academy of Mathematics and Systems Science
- **分类**: vol 51 · issue 4 · pp 1685-1706
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在聚类失效时间数据设定下，本文提出 frailty proportional mean residual life 回归模型，目标为回归参数的估计与推断，无需指定 frailty 的具体分布。核心机制是构建条件 quasi-likelihood 推断程序：利用惩罚 quasi-likelihood (PQL) 处理簇内相关性，结合逆概率 censoring 权重 (IPCW) 与 Buckley–James 估计量形成估计方程，从而允许依赖性 censoring。建立了估计量的渐近性质（n^{-1/2}-CAN），并通过模拟与多中心乳腺癌数据验证了有限样本表现。对您可能有用：本文的 PQL + IPCW 组合策略为处理聚类生存数据中的分布假设放松提供了半参数思路，可对比您熟悉的 semiparametric efficiency bound 在此模型下是否可达。
- **关键技术**: `penalized quasi-likelihood`, `inverse probability of censoring weighting`, `Buckley-James estimator`, `mean residual life regression`, `frailty model`, `asymptotic normality`
- **为什么对您有用**: 本文连接到 semiparametric theory 子方向：在聚类生存分析中用 PQL 避免指定 frailty 分布，属于半参数 M-estimation 的一个具体实例。可用您 moderately_familiar 的 M-estimation theory 分析其估计方程的 influence function，进而检验该 PQL 估计量是否达到 semiparametric efficiency bound（目前论文未讨论效率，这是一个可攻的口子）。follow-up 粗判：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是推导该模型下的 efficient influence function 以判断 PQL 估计量的效率损失。

### 5. [10.1111/sjos.12739](https://doi.org/10.1111/sjos.12739) · [arXiv](https://arxiv.org/abs/2210.14201) — Bayesian mixture models (in)consistency for the number of clusters
- **作者**: Louise Alamichel, Daria Bystrova, Julyan Arbel, Guillaume Kon Kam King
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Mathématiques et Informatique Appliquées du Génome à l'Environnement
- **分类**: vol 51 · issue 4 · pp 1619-1660
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在 Bayesian nonparametric mixture model 设定下，目标是估计真实有限聚类数 K_0，研究 Gibbs-type processes 及其有限维表示（Dirichlet multinomial / Pitman-Yor multinomial / normalized generalized gamma multinomial）作为先验时聚类数的 posterior consistency。核心结论是：这些先验下的聚类数后验分布均不一致（posterior inconsistency），即后验无法收敛到真实的有限 K_0，延续了 Dirichlet / Pitman-Yor process mixture 的已知负面结果。作者进一步将 Dirichlet process 下提出的 postprocessing 算法推广至更一般的 Gibbs-type 框架，证明该修正方法可恢复聚类数估计的 consistency。对您可能有用：该文揭示了 BNP 先验在离散结构推断中的根本局限，为 semiparametric theory 中涉及 latent component / mixture 的 identification 与 efficiency 问题提供了警示。
- **关键技术**: `Bayesian nonparametric mixture model`, `Gibbs-type process prior`, `posterior inconsistency`, `Dirichlet multinomial process`, `postprocessing algorithm for cluster number`, `finite-dimensional representation of BNP prior`
- **为什么对您有用**: 本文直接触及 semiparametric theory 中 mixture / latent component 的 identification 与 estimation 问题——BNP 先验虽在 density estimation 上表现良好，但在离散参数（聚类数）上存在 posterior inconsistency，这对您做 semiparametric efficiency bound 时涉及 latent structure 的模型设定有重要参考价值。用您 very_familiar 的 minimax bounds 视角，可以审视该 postprocessing 算法恢复 consistency 后的收敛率是否达到 minimax optimal，或用 moderately_familiar 的 M-estimation theory 分析其 frequentist 性质。Follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以将 BNP posterior inconsistency 的结论与 semiparametric efficiency / HOIF 框架中的 latent variable identification 建立更精确的数学桥梁。

### 6. [10.1111/sjos.12736](https://doi.org/10.1111/sjos.12736) · [arXiv](https://arxiv.org/abs/2110.11803) — Validation of point process predictions with proper scoring rules
- **作者**: Claudio Heinrich‐Mertsching, Thordis L. Thorarinsdottir, Peter Guttorp, Max Schneider
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 4 · pp 1533-1566
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在空间点过程预测评估设定下，基于汇总统计量构造了一类新的 proper scoring rule，以衡量模型对特定特征（如空间分布、聚类倾向）的校准程度。核心机制是对期望进行 Monte Carlo 近似，使得只要模型可模拟即可计算得分，从而绕过了 logarithmic score 等需要精确似然的限制。模拟研究分析了不同 scoring rule 对点过程各特征的敏感性，并与 logarithmic score 做了对比。两个实证应用（北加州地震与太平洋银杉空间分布）展示了该方法在科学模型选择中的实用性。对您可能有用：该文虽属点过程模型评估，但其 proper scoring rule 的构造与 Monte Carlo 近似误差分析，与 semiparametric efficiency 及数值计算中的近似推断有方法论上的对照价值。
- **关键技术**: `proper scoring rule`, `Monte Carlo approximation`, `spatial point process`, `summary statistics`, `logarithmic score`, `model calibration`
- **为什么对您有用**: 本文主要连接 semiparametric / nonparametric theory 中的模型评估与 scoring rule 理论，以及 stat_computing 中的 Monte Carlo 近似计算。用您 very_familiar 的 minimax bounds 与 inverse problems with random noise 视角，可以审视其 Monte Carlo 近似误差的收敛阶是否达到最优，这是一个潜在的 sharper_rate 改进口子。Follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立 proper scoring rule 在 semiparametric 模型类下的效率界与近似误差的严格理论。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.12723](https://doi.org/10.1111/sjos.12723) — Double debiased transfer learning for adaptive Huber regression
- **作者**: Ziyuan Wang, Lei Wang, Heng Lian
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Nankai University · City University of Hong Kong
- **分类**: vol 51 · issue 4 · pp 1472-1505
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维线性回归在误差重尾或非对称时的迁移学习问题，采用自适应Huber回归平衡偏差与稳健性，提出一种新的稳健迁移学习算法。当可迁移源域已知时，先构造两阶段L1惩罚的自适应Huber迁移估计量，并建立收敛速度界；再基于去相关得分方程构建统一的去偏框架，得到去偏Lasso迁移估计量的渐近正态性，从而可构造每个系数的置信区间和假设检验。当可迁移源域未知时，给出带理论保证的数据驱动源检测算法。数值实验和GTEx组织基因表达数据分析验证了方法的有效性。对您而言，本文的高维稳健推断技术可迁移到因果推断中处理重尾协变量或结果变量的场景，尤其适合在敏感性分析或IV估计中构造稳健置信区间。
- **关键技术**: `adaptive Huber regression`, `debiased lasso`, `transfer learning`, `decorrelated score equations`, `high-dimensional inference`, `robust estimation`
- **为什么对您有用**: 本文与您对高维统计推断和假设检验的兴趣直接相关，特别是去偏Lasso的渐近正态性为构造置信区间提供了理论基础。从您的技术武库看，您对high-dimensional asymptotics和nonparametric statistics非常熟悉，可以快速理解本文的收敛速率和去偏机制，并考虑将类似Huber损失的去偏方法应用于您在因果推断中处理重尾数据的问题（例如Proximal CI中的稳健估计）。立即可做：您可用very_familiar的高维渐近工具直接复现并推广其假设检验程序至您的因果推断设定。

### 2. [10.1111/sjos.12749](https://doi.org/10.1111/sjos.12749) — Looking back: Selected contributions by C. R. Rao to multivariate analysis
- **作者**: Dianna Smith
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Statistics Finland · University of Helsinki
- **分类**: vol 51 · issue 4 · pp 1393-1424
- 相关性 6/10 · novelty: `survey`
- **摘要**: 本文是一篇回顾C. R. Rao在多变量分析领域主要贡献的综述文章。文章系统梳理了Rao从早期到晚期的工作，包括线性判别分析的扩展、Rao's perimeter test、Rao's U统计量、Wilks统计量的渐近展开、典范因子分析、函数主成分分析、冗余分析、典范坐标和对应分析等主题。文章强调这些贡献至今仍在被使用和扩展，并指出跨学科合作与真实数据集的应用是Rao产生深远影响的关键。对于关注高阶U统计量历史的读者，本文提供了Rao's U统计量的原始动机和后续发展脉络。这是一篇方法论历史综述，不包含新理论或新方法，适合作为了解多元分析发展史的入门读物。
- **关键技术**: `Rao's U statistic`, `Rao's perimeter test`, `canonical factor analysis`, `functional principal component analysis`, `redundancy analysis`, `correspondence analysis`
- **为什么对您有用**: 本文直接关联您的更高阶U统计量兴趣，Rao's U统计量是该方向的早期形式，可帮助理解历史动机。同时Rao的检验方法（如perimeter test）属于假设检验范畴。但本文是历史综述，无新方法，武器库中非常熟悉的higher-order U-statistics知识已足够覆盖；考虑到无实质技术问题可跟进，属于暂不可做的范畴。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12742](https://doi.org/10.1111/sjos.12742) — Regression‐based network‐flow and inner‐matrix reconstruction
- **作者**: Michael Lebacher, Göran Kauermann
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Siemens (Germany) · Ludwig-Maximilians-Universität München
- **分类**: vol 51 · issue 4 · pp 1730-1748
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究在给定行和与列和的条件下重构矩阵（网络）的问题。传统方法如迭代比例拟合（IPFP）或最大熵（ME）只能产生唯一解，但无法融入协变量信息或提供不确定性量化。作者证明IPFP/ME估计等价于约束极大似然估计，并采用增广拉格朗日优化实现。在此基础上，将重构框架扩展为回归模型，允许引入外生协变量，并通过bootstrap进行不确定性量化。在模拟和国际清算银行（BIS）的银行间借贷真实网络数据上，展示了包含协变量可显著降低预测误差（MSE和MAE）。该方法本质上是将离散优化问题转化为平滑优化，兼具计算效率与统计推断能力。对您而言，本文的矩阵重构思路可自然推广到高阶张量重构，与您在高阶U统计量中的张量收缩计算（einsum复杂度）直接相连，可利用现有的树宽/张量网络工具分析推广后的计算成本。
- **关键技术**: `iterative proportional fitting (IPFP)`, `maximum entropy`, `restricted maximum likelihood`, `augmented Lagrangian optimization`, `bootstrap uncertainty quantification`, `network reconstruction`
- **为什么对您有用**: 本文方法属于统计计算与反问题范畴，直接对应您 primary interest 中的 'statistical computing (numerical methods, algorithm)'。核心技术（增广拉格朗日优化与bootstrap推断）与您的 very_familiar 武器库 'inverse problems with random noise' 相通。更重要的是，矩阵重构可视为张量重构的特例——您在高阶U统计量中奠定的 'treewidth/tensor contraction/einsum' 计算模型可直接用于分析更高阶重构问题的计算复杂度与最优收缩顺序。目前该扩展方向尚未被系统研究，是一个中期可做的路线：您需先在 moderately_familiar 的 'theory of higher-order U-statistics' 中巩固张量层面的identifiability理论，然后用现有的einsum工具实现算法原型。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.12754](https://doi.org/10.1111/sjos.12754) · [arXiv](https://arxiv.org/abs/2210.05983) — Model‐based clustering in simple hypergraphs through a stochastic blockmodel
- **作者**: Luca Brusa, Catherine Matias
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Milano-Bicocca · Université Paris Cité · Sorbonne Université · Sorbonne Paris Cité · Laboratoire de Probabilités et Modèles Aléatoires
- **分类**: vol 51 · issue 4 · pp 1661-1684
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究简单超图（simple hypergraph）中的节点聚类问题，设定为不允许同一节点在同一超边中重复出现的结构（如合著网络），采用随机块模型（hypergraph stochastic blockmodel, HyperSBM）作为生成模型，假设节点有潜在分组且超边在给定分组下条件独立。首先证明了模型参数的一般可辨识性（generic identifiability）。随后开发变分近似 EM（variational EM）算法进行参数推断与节点聚类，并导出模型选择准则。通过 R 包 HyperSBM 在合成数据、线聚类实验与合著数据集上与现有方法对比验证性能。对您可能有用：超边结构可视为高阶交互，其似然展开与 higher-order U-statistics 的组合结构有形式上的联系。
- **关键技术**: `hypergraph stochastic blockmodel`, `generic identifiability`, `variational EM algorithm`, `model selection criterion`, `simple hypergraph`
- **为什么对您有用**: （1）连接到 higher-order U-statistics 子方向：超边是 d-阶交互，模型似然中的组合结构与高阶 U-statistic 的核展开形式相似，可作为理解高阶交互统计量的入门场景。（2）武器库中 very_familiar 的 higher-order U-statistics computation（treewidth / einsum）可直接切入：变分 EM 中超边似然的求和/边际化本质上是一类 tensor contraction，可用 einsum 复杂度视角分析其计算瓶颈并优化。（3）中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格分析变分 EM 估计量的收敛性与相合性。

### 2. [10.1111/sjos.12731](https://doi.org/10.1111/sjos.12731) — Estimation of the conditional tail moment for Weibull‐type distributions
- **作者**: Yuri Goegebeur, Armelle Guillou, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Southern Denmark · Centre National de la Recherche Scientifique · Institut de Recherche Mathématique Avancée · Université de Strasbourg
- **分类**: vol 51 · issue 4 · pp 1782-1815
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 该论文针对Weibull型分布的极端条件尾矩（conditional tail moment）提出一种两步估计法。第一步在中间水平上估计条件尾矩，第二步利用极值外推技术将其推广到极端水平。在适当的正则条件下，论文建立了两个步骤估计量的渐近性质（一致性、渐近正态性）。通过蒙特卡洛模拟验证了有限样本表现，并应用于海上风电场风速数据和空气污染数据。方法基于极值理论中的块极大值或超越阈值技术，但参数形式限定为Weibull类。对您而言，本文属极值统计专门方向，未直接涉及因果推断、半参效率或高维随机矩阵等核心兴趣领域，但两步估计框架与非参数估计有一定技术关联。
- **关键技术**: `conditional tail moment`, `Weibull-type distribution`, `two-step estimation`, `extreme value extrapolation`, `asymptotic normality`
- **为什么对您有用**: 本文属于极值统计方法论文，与您的首要兴趣（因果推断、高维、半参理论）无直接重叠。武器库中虽涉及非参数估计和高维渐近，但本文化指Weibull尾行为的参数假设限制了方法通用性。立即可做性判定：暂不可做——核心极值理论工具（如极值索引估计、超阈值模型）不在您的技术武器库中。若后续希望进入环境或能源统计应用方向，此文献可作入门参考；但目前对您的研究主线帮助有限。

### 3. [10.1111/sjos.12752](https://doi.org/10.1111/sjos.12752) — On some publications of Sir David Cox
- **作者**: Nancy Reid
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Toronto
- **分类**: vol 51 · issue 4 · pp 1425-1432
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是Nancy Reid对Sir David Cox在Scandinavian Journal of Statistics和Scandinavian Actuarial Journal上发表的四篇论文的简要回顾。Cox是20世纪最杰出的统计学家之一，他对生存分析、似然推断、模型选择等领域的贡献影响深远。文章对这些论文的核心内容进行了总结，包括Cox比例风险模型、部分似然、广义线性模型等关键思想。虽然这是回顾性文章，不包含新的方法学结果，但它为理解Cox的统计哲学和贡献提供了清晰的脉络。对于统计学家而言，阅读此文有助于把握现代统计方法的思想根源，特别是因果推断中常用的部分似然和模型选择概念。
- **关键技术**: `Cox proportional hazards model`, `partial likelihood`, `generalized linear models`, `survival analysis`, `likelihood inference`
- **为什么对您有用**: 本文是关于David Cox工作的历史回顾，虽不直接推进研究者primary interest中的方法论，但Cox在统计推断和半参数建模方面的思想深刻影响了因果推断中的倾向评分、工具变量等概念。研究者若对统计思想史感兴趣，可作为入门读物；但若追求方法论进步，则无需深读。武器库中的'nonparametric statistics'和'identification theory in causal inference'与Cox的工作有渊源，但本文不提供新的技术细节。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

