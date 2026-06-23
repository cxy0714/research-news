# Scand. J. Stat. — Vol 50  Issue 1  ·  2026-06-23

- 共 16 篇 · Scandinavian Journal of Statistics
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 17 篇）：10.1111/sjos.12631

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期文章主要沿因果推断与稳健估计、假设检验与选择推断、非参数与生存分析、以及贝叶斯与统计计算四条主线展开。因果推断与稳健估计方向集中了讨论多重稳健匹配估计的 *Multiply robust matching estimators* 与处理公开调查数据加权的 *Unconditional empirical likelihood approach*；假设检验主线涵盖功能性协方差分析、P值理论辨析、后选择置信分布及变点估计四篇；非参数与生存分析关注依赖截断下的生存函数界限；其余则散见于贝叶斯聚类、惩罚回归计算及流行病学设计。

因果推断与稳健估计主线在本期推进了对模型误设与数据结构的双重适应性。*Multiply robust matching estimators* 针对倾向得分匹配（PSM）依赖正确模型设定的痛点，引入双评分匹配（DSM）及多候选模型策略，实现了只要倾向得分或预后得分任一模型正确估计量即一致的“多重稳健性”，并利用鞅表示理论解决了方差估计问题。*Unconditional empirical likelihood approach* 则聚焦于公开调查数据（如 NHANES）因设计变量缺失无法直接建模的困境，提出无需传统抽样假设的无条件经验似然方法，为因果推断中的加权估计提供了直接可用的工具。两者分别从方法论的稳健性架构和实际数据的可及性角度丰富了观察性研究的推断工具。

假设检验与推断主线呈现了从非参数检验到选择性偏差修正的理论纵深。*Minimax powerful functional analysis of covariance tests* 针对纵向稀疏功能数据，通过核平滑与非参数协方差估计构建了具有极小化极大最优功效的检验；*Exact uniformly most powerful postselection confidence distributions* 则直面模型选择后的推断难题，利用选择事件的条件概率构造了有限样本下精确且均匀最优的置信分布，有效避免了选择性偏差。此外，*Divergence versus decision P-values* 从统计哲学层面严格区分了度量证据的分歧P值与控制错误的决策P值，澄清了P值使用的概念混淆。

对于关注因果推断与半参数效率的研究者，*Multiply robust matching estimators* 提供了最新的多重稳健匹配理论与效率分析，*Unconditional empirical likelihood approach* 解决了复杂抽样数据下的加权推断难题，二者均属必读；对高维与选择推断感兴趣者，*Exact uniformly most powerful postselection confidence distributions* 提供了后选择推断的精确解法，值得重点关注。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.12585](https://doi.org/10.1111/sjos.12585) · [arXiv](https://arxiv.org/abs/2001.06049) — Multiply robust matching estimators of average and quantile treatment effects
- **作者**: Shu Yang, Yunshu Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 1 · pp 235-265
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文在因果推断中关注平均处理效应（ATE）和分位数处理效应（QTE）的估计，采用倾向得分匹配（PSM）但传统方法依赖正确模型设定。作者提出双评分匹配（DSM），同时利用倾向得分和预后得分，并引入多个候选模型以实现多重稳健性：只要任意一个评分模型正确，debiasing DSM估计量即一致。核心机制是通过匹配的鞅表示和局部正态实验理论推导渐近分布，并给出两阶段复制法用于方差估计。方法进一步扩展到分位数处理效应估计。模拟表明，在极端倾向得分场景下DSM明显优于单评分匹配和现有多重稳健加权估计。该工作与您主要兴趣中的因果推断（稳健估计与匹配方法）直接相关，为实际数据分析提供了更强的模型误设保护。
- **关键技术**: `propensity score matching`, `prognostic score`, `double score matching`, `multiply robust estimation`, `martingale representation`, `quantile treatment effects`
- **为什么对您有用**: 本文属于因果推断中的匹配估计方向，与您主要兴趣中的causal inference（identification, estimation）紧密相关。您very_familiar中的'estimation theory in causal inference'可直接用于评估其debiasing DSM估计量的构造和多重稳健性证明，且moderately_familiar中的'semiparametric theory'可进一步检验其效率性质。立即可做：您能迅速将其中多重稳健性与匹配思想融入到自己的因果推断研究中，并考虑结合higher-order influence functions（HOIF）扩展其高阶性质。

### 2. [10.1111/sjos.12590](https://doi.org/10.1111/sjos.12590) — Unconditional empirical likelihood approach for analytic use of public survey data
- **作者**: Yves G. Berger
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Southampton
- **分类**: vol 50 · issue 1 · pp 383-410
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对公开调查数据中设计变量缺失导致无法直接建模的问题，提出一种无条件经验似然方法。只需校准权重、分层变量和初级抽样单元标识即可获得一致点估计和用于检验置信区间的 pivotal 统计量。方法无需有放回抽样、单阶段、可忽略抽样分数或非信息性抽样假设，允许多阶段设计和不等概率抽取 PSU。非响应可通过包含非响应调整的校准权重轻松处理。该方法将变量和样本均视为随机变量，适用于信息性抽样设计。对您可能有用：该方法可直接用于流行病学公开调查数据（如 NHANES）的因果推断中的加权估计，与您的因果推断和流行病学应用兴趣高度吻合。
- **关键技术**: `empirical likelihood`, `calibrated weights`, `pivotal statistics`, `complex survey design`, `informative sampling`
- **为什么对您有用**: 该方法针对公开调查数据（流行病学常用数据源）提供一种稳健的推断框架，直接服务于您 secondary interest 中的流行病学应用。您非常熟悉的 estimation theory in causal inference 中的加权估计（如 IPW）是该方法的自然类比，可帮助快速理解其估计和检验原理。立即可做：利用您的非参数统计和估计理论背景即可消化该方法，并将其应用于您熟悉的公开调查数据因果分析中。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1111/sjos.12582](https://doi.org/10.1111/sjos.12582) — Nonparametric bounds for the survivor function under general dependent truncation
- **作者**: Jing Qian, Rebecca A. Betensky
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Massachusetts Amherst · New York University
- **分类**: vol 50 · issue 1 · pp 327-357
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究在一般依赖截断（general dependent truncation）和删失并存下，如何对生存函数进行非参数推断。主要目标是估计边际生存函数在整个支撑集上的真实值，而非仅局限于可观测区域。作者首先推导了完全非参数的可识别界限（nonparametric bounds），该界限扩展了已有文献中仅限于无截断情形的结果。进一步，通过定义一个危险比函数（hazard ratio function）来链接不可观测区域与可观测区域，当该函数可被有界且截断概率近似已知时，可得到比纯非参数界限更窄的识别区间。方法不依赖参数模型，仅利用观测数据中的截断和删失结构。模拟和临床实例展示了所提界限的有效性和实用性。本文对非参数统计中复杂抽样下的生存函数估计问题提供了新的非参数界工具，可直接与因果推断中缺失数据机制下的敏感性分析思路相联系。
- **关键技术**: `nonparametric bounds`, `dependent truncation`, `survivor function`, `hazard ratio function`, `identifiability bounds`, `censoring`
- **为什么对您有用**: 本文紧扣非参数统计的理论兴趣，特别是依赖截断下生存函数的非参数可识别性问题，为后续用minimax界检验边界紧度提供了具体案例。武器库中非参数统计和逆问题工具可直接用于理解其界的最优性（立即可做）。此外，其有界危险比函数的思路可推广至因果推断中的选择偏倚敏感性分析，属于中期可做（需巩固识别理论）。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1111/sjos.12583](https://doi.org/10.1111/sjos.12583) — Minimax powerful functional analysis of covariance tests with application to longitudinal genome‐wide association studies
- **作者**: Weicheng Zhu, Sheng Xu, Catherine C. Liu, Yehua Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Amazon (United States) · BeiGene (China) · Hong Kong Polytechnic University · University of California, Riverside
- **分类**: vol 50 · issue 1 · pp 266-295
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对纵向全基因组关联研究中在不规则时间点上观测的稀疏功能数据，提出非参数函数协方差分析检验，用于检测功能性基因型效应，同时控制环境协变量的混杂。方法基于看似无关的核平滑器，通过引入一致的非参数协方差函数估计量来刻画受试者内时间相关性，从而提升检验功效。理论证明，所提检验具有Wilks现象，且是极小化极大最有效的检验，即在所有满足一定条件的检验中达到最优化功效。在ADNI数据库的阿尔茨海默病数据应用中，该方法识别出若干可能与疾病相关的新基因。对您而言，该工作将非参数假设检验与纵向数据结合，提供了检验在复杂依赖结构下的最优性理论，可启发因果推断中纵向设定下的敏感性分析或检验问题。
- **关键技术**: `functional analysis of covariance`, `kernel smoothing`, `minimax most powerful test`, `Wilks phenomenon`, `nonparametric covariance estimation`, `longitudinal GWAS`
- **为什么对您有用**: 本文直接关联您对假设检验与非参数理论的主要兴趣，特别是其在纵向设定下的最优化理论。您very_familiar中的非参数统计与minimax bound工具箱可快速评估其理论紧致性和可推广性，且该文对时间相关性的处理方式对您causal inference中纵向数据的检验问题具有参考价值。立即可做：利用现有非参数武器可复现或改进其检验构造。

### 2. [10.1111/sjos.12625](https://doi.org/10.1111/sjos.12625) — Divergence versus decision<i>P</i>‐values: A distinction worth making in theory and keeping in practice: Or, how divergence<i>P</i>‐values measure evidence even when decision<i>P</i>‐values do not
- **作者**: Sander Greenland
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of California, Los Angeles
- **分类**: vol 50 · issue 1 · pp 54-88
- 相关性 7/10 · novelty: `minor`
- **摘要**: 这篇论文严格区分了P值的两种定义：分歧P值（divergence P-value）和决策P值（decision P-value）。分歧P值起源于将观测数据与模型预期之间的偏离程度（如平方和或偏差统计量）映射到一个参考分布上，得到一个无量纲的相容性指标。决策P值则被定义为单位区间上的随机变量，其实现值与预先设定的阈值α比较以构造决策规则，从而在模型和特定备择假设下控制错误率。论文指出，尽管通常认为决策P值总是对应于分歧P值，但实际情况并非如此：决策P值可能违反直观的单一样本相干性准则，而分歧P值则不会。因此，作者主张在教学和实践中应仔细区分这两种P值，且当分析目标是总结证据而非实施决策规则时，分歧P值是更合适的选择。该论文对假设检验的基础概念进行了澄清，对于研究者日常使用的P值解释具有直接的指导意义。
- **关键技术**: `divergence P-value`, `decision P-value`, `compatibility index`, `coherence criterion`, `test statistic divergence`
- **为什么对您有用**: 此文直接对应研究者的primary interest“mathematical statistics & hypothesis testing”，尤其对假设检验中P值的本质理解至关重要。研究者“very_familiar”中的“nonparametric statistics”框架已经包含假设检验（如基于偏差统计量的检验），因此可以立即吸收本文观点，将其应用于因果推断的敏感性分析或高维检验中的P值解释。后续可进一步探讨在U-statistics框架下分歧P值与决策P值的具体表现，属于可直接动手的入门级理论澄清。

### 3. [10.1111/sjos.12581](https://doi.org/10.1111/sjos.12581) — Exact uniformly most powerful postselection confidence distributions
- **作者**: Andrea C. Garcia‐Angulo, Gerda Claeskens
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Escuela Superior Politecnica del Litoral · Statistics Belgium · KU Leuven
- **分类**: vol 50 · issue 1 · pp 358-382
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 这篇论文研究模型选择后的推断问题，具体设定为从一组可能错误设定的正态线性回归模型中选出某一个后，对选定模型中的焦点参数进行推断。作者基于选择事件的条件概率，构造了条件置信分布（conditional confidence distributions），这些分布在有限样本下是精确的，且在所有置信水平下都是均匀最优的（uniformly most powerful）。该方法利用条件推断避免了选择性偏差，并同时提供了最优的置信区间和假设检验。核心机制是将模型选择视为一个可测事件，通过证明条件密度族的凸性，推导出似然比检验的最优性。最终，作者展示了该条件置信分布可以高效地构造后选择推断，包括双侧和单侧检验，且不需要渐近近似。这一结果对您在假设检验方向的研究有直接借鉴意义，尤其是后选择推断的理论框架和最优性保证。
- **关键技术**: `conditional confidence distributions`, `postselection inference`, `uniformly most powerful tests`, `finite sample exact inference`, `conditioning on selection event`, `likelihood ratio optimality`
- **为什么对您有用**: 该论文直接关联您主要兴趣中的假设检验（hypothesis testing）方向，特别是模型选择后的有效推断问题。您熟悉的非参数统计和最小最大界技术可用于评估该方法在非参数设定下的扩展性，或验证其最优性是否依赖正态假设。从武器库来看，您对假设检验理论的熟悉程度足以深入理解其技术细节，并考虑将其与因果推断中的模型选择后推断（如IV选择）结合，属于立即可做的方向。

### 4. [10.1111/sjos.12567](https://doi.org/10.1111/sjos.12567) · [arXiv](https://arxiv.org/abs/2102.06871) — Estimation for change point of discretely observed ergodic diffusion processes
- **作者**: Yozo Tonaki, Yusuke Kaino, Masayuki Uchida
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 1 · pp 142-183
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文考虑离散观测遍历扩散过程的变点估计问题。设定为两种情形：扩散参数存在变点，以及漂移参数存在变点而扩散参数无变点。估计方法基于对比函数（contrast function）最小化，其中扩散参数变点估计使用拟似然对比函数，漂移参数变点估计则在扩散参数已知或估计后构造对比函数。论文给出了变点估计量的收敛速度，证明其在某些正则条件下以 n^{-1/2} 速率收敛，并建立了极限分布（如复合泊松过程或两段布朗桥）。数值模拟验证了有限样本表现。对您有用的连接：变点估计是假设检验的自然延伸，属于数学统计中经典的非标准推断问题；您熟悉的 M-estimation 理论和渐近工具可直接用于理解对比函数估计量的性质。
- **关键技术**: `change point estimation via contrast minimization`, `discretely observed ergodic diffusion`, `diffusion parameter change`, `drift parameter change`, `convergence rate and limit distribution`, `quasi-likelihood contrast`
- **为什么对您有用**: 与您 primary interest 中的 'mathematical statistics (hypothesis testing)' 直接相关——变点估计是假设检验后最自然的后续问题。本文的对比函数估计量本质上是 M-estimation 框架在遍历扩散过程中的应用，您 moderately_familiar 中的 M-estimation theory 可用来分析估计量的一致性和收敛速度（需要补充扩散过程均匀遍历性等额外条件）。整体而言，**立即可做**：您已有的统计渐近理论和 M-estimation 背景足以理解本文主要论证，无需新武器。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12574](https://doi.org/10.1111/sjos.12574) · [arXiv](https://arxiv.org/abs/2001.09834) — Penalized angular regression for personalized predictions
- **作者**: Kristoffer H. Hellton
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 1 · pp 184-212
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种名为个性化角度（PAN）回归的惩罚回归方法，旨在针对预测任务实现模型个性化。该方法通过惩罚给定协变量向量的归一化预测来构造系数，使回归系数随预测对象变化，从而将个性化直接嵌入模型。PAN方法使用超球面参数化，将惩罚施加于归一化回归系数的角度，形成一类新的角度惩罚。在正交设计矩阵下，PAN估计退化为低维特征向量问题，并基于超球面参数化设计了高效算法。调参采用参数化bootstrap程序，模拟显示PAN在预测误差上优于OLS、岭回归等常见方法。最后通过实际数据应用演示了方法效果。对您而言，本文提供了一种新的统计计算算法，可结合您熟悉的软件开发和高维渐近工具进行实现与理论分析。
- **关键技术**: `penalized angle regression`, `hyperspherical parametrization`, `normalized prediction penalty`, `parametric bootstrap`, `eigenvector equation`
- **为什么对您有用**: 本文属于统计计算方法论，直接对应您的主要兴趣中的统计计算（numerical methods, algorithm）。您熟悉的high-dimensional asymptotics可用于分析PAN在高维下的性质，software development技能可快速实现其算法。立即可做：您可以用已知的simulation框架复现并扩展其模拟比较，或者从渐近角度推导PAN的Oracle性质。

### 2. [10.1111/sjos.12577](https://doi.org/10.1111/sjos.12577) · [arXiv](https://arxiv.org/abs/2201.10993) — Approximate reference priors for Gaussian random fields
- **作者**: Victor De Oliveira, Zifei Han
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 1 · pp 296-326
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 该论文研究高斯随机场模型参数的参考先验计算问题。由于精确参考先验计算困难，作者基于频谱近似提出了一类新的近似参考先验。该方法通过频谱近似计算协方差参数的积分似然，仅需在辅助规则网格的频谱点处评估谱密度和均值函数。相比精确参考先验，近似先验计算更稳定且计算负担大幅降低。此外对于相关参数，边际近似参考先验总是正常的，该性质对协方差模型选择具有重要价值。文章通过加利西亚铅污染数据集展示了默认贝叶斯分析的应用。对统计计算方向而言，该工作提供了一种实用的先验近似计算方法，可推广至其他空间或时间序列模型。
- **关键技术**: `Reference priors`, `Spectral approximation`, `Integrated likelihood`, `Gaussian random fields`, `Default priors`
- **为什么对您有用**: 该论文直接关联您的统计计算兴趣：提出了一种计算更简便、更稳定的先验近似方法，解决高斯随机场中参考先验的计算瓶颈。您的“软件开发”技能可用于复现或扩展该方法。不过要深入理解频谱近似推导或改进，可能需要先熟悉频谱分析与贝叶斯先验理论，属于中期可做的工作（需在频谱近似方法上积累经验）。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1111/sjos.12624](https://doi.org/10.1111/sjos.12624) — Use of multiple imputation in supersampled nested case‐control and case‐cohort studies
- **作者**: Ørnulf Borgan, Ruth H. Keogh, Aleksander Njøs
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Oslo · London School of Hygiene & Tropical Medicine
- **分类**: vol 50 · issue 1 · pp 13-37
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文研究嵌套病例-对照和病例-队列设计中，当昂贵协变量仅部分收集时如何有效利用廉价协变量信息。标准分析忽略全队列数据，而多重插补虽能利用全队列信息但计算成本高。作者提出对超采样数据（即在病例-对照样本外额外补充廉价协变量观测的对照）使用多重插补进行分析。通过模拟研究，展示了该方法相对于传统分析可提升效率，且与使用全队列数据的多重插补相比效率损失不大。该方法基于标准多重插补技术，无需复杂计算框架，适用于大规模队列研究。结果为流行病学研究中成本约束下的数据利用提供了实用方案。对您而言，此文可作为流行病学队列研究统计方法的入门案例，但由于方法学创新有限，且与您的核心兴趣（因果推断、高维统计等）关联较弱，可能仅作泛读。
- **关键技术**: `multiple imputation`, `nested case-control study`, `case-cohort study`, `supersampling`, `survival analysis`
- **为什么对您有用**: 本文属于流行病学应用方向的统计方法工作，直接对应您的 secondary interest 中的 epidemiology。方法本身是经典多重插补，但结合了超采样设计，武器库中的 nonparametric statistics 和 estimation theory 可轻松理解其渐近性质。但由于方法学贡献较浅（模拟为主），且不涉及因果推断或效率理论，属于中期可读但不需深究的文献。

## 其他  *(other, 6 篇)*

### 1. [10.1111/sjos.12633](https://doi.org/10.1111/sjos.12633) — Remove unwanted variation retrieves unknown experimental designs
- **作者**: Ingrid M. Lönnstedt, Terence P. Speed
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Walter and Eliza Hall Institute of Medical Research · SDS Life Science (Sweden)
- **分类**: vol 50 · issue 1 · pp 89-101
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文在去除不想要的变异（RUV）框架下，研究了RUV-inverse方法中权重矩阵的估计问题。RUV方法利用负对照测量（假设在实验条件下不变的基因表达值）估计多变量数据集的潜在相关结构。作者推导了RUV-inverse中纳入广义最小二乘估计的权重矩阵，并证明该权重矩阵实际上是负对照测量平均协方差矩阵的估计。通过将RUV-inverse与平衡不完全区组设计（BIBD）的经典分析联系起来，作者展示了RUV-inverse能够恢复内块和块间参数估计，并以加权和的形式组合，类似于最佳线性无偏估计（BLUE）。关键区别在于RUV-inverse的权重是从负对照测量全局估计的，而非像经典BIBD-BLUE那样针对每个测量单独优化。本文提供了一种理解RUV方法的新理论视角，但研究内容与方法论并不直接匹配您的主要兴趣（因果推断、高维统计等），可视为统计学方法论的一般性参考。
- **关键技术**: `Remove Unwanted Variation (RUV)`, `generalized least squares`, `balanced incomplete block design (BIBD)`, `best linear unbiased estimator (BLUE)`, `negative control measurements`, `weight matrix estimation`
- **为什么对您有用**: 本文主要涉及基因表达数据的归一化方法，与您的核心兴趣（因果推断、高维统计、半参数理论等）关联较弱。您的技术武器库中的'高维渐近'或许可用于理解RUV在高维协方差估计中的表现，但本文并未提供渐近理论。目前难以直接转化为可攻的问题，属于'暂不可做'——核心机器不在武器库中（缺少基因表达数据分析的领域知识和方法上下文）。除非您有意拓展生物信息学方向，否则阅读优先级较低。

### 2. [10.1111/sjos.12609](https://doi.org/10.1111/sjos.12609) — Approximate exchangeability and de Finetti priors in 2022
- **作者**: Persi Diaconis
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Stanford University
- **分类**: vol 50 · issue 1 · pp 38-53
- 相关性 5/10 · novelty: `survey`
- **摘要**: 这是一篇针对近似可交换性和 de Finetti 先验研究的综述文章。文章从 de Finetti 关于部分可交换性的经典工作出发，梳理了其在非标准情形下赋予信息先验的策略。随后介绍了最近在 MCMC 推断上的进展，特别是 Gerencsér 和 Ottolini 给出的收敛速率严格界（honest bounds）。最后，作者展望了将经典渐近理论（如边缘似然、贝叶斯信息准则）与蒙特卡洛方法相结合的思路，认为这一方向有可能显著加速计算并促进理论与计算的互动。本文主要整理已有结论，未提出新方法或新理论。对您而言，该综述有助于了解贝叶斯非参数推断的基础框架，但您的技术武器库以频率学派和高维理论为主，短期内难以直接利用该方向的结果。
- **关键技术**: `de Finetti representation theorem`, `partial exchangeability`, `Markov chain Monte Carlo (MCMC)`, `honest bounds for mixing rates`, `classical asymptotics + Monte Carlo`
- **为什么对您有用**: 本文属于综述性质，回顾了近似可交换性的理论进展与 MCMC 收敛界的近期结果。虽然不直接涉及您主要关注的因果推断、高维统计或效率理论，但其中关于“经典渐近+蒙特卡洛”加速计算的思路与您“统计计算”的次要兴趣有所关联。技术武器库中“非参数统计”和“最小最大界”可用于理解其收敛率的表述，但您缺乏贝叶斯和非参数贝叶斯的具体经验，因此后续利用该文成果暂不可行。建议将其作为拓宽统计计算视野的入门读物。

### 3. [10.1111/sjos.12575](https://doi.org/10.1111/sjos.12575) — Learning the two parameters of the Poisson–Dirichlet distribution with a forensic application
- **作者**: Giulia Cereda, Fabio Corradi, Cecilia Viscardi
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Florence
- **分类**: vol 50 · issue 1 · pp 120-141
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对法医学中的稀有类型匹配问题，即嫌疑人与犯罪现场的匹配特征在参考数据库中不存在时，如何评估似然比。现有解决方案假设有序总体概率服从两参数 Poisson–Dirichlet 分布，并用参数的极大似然估计代替后验，但存在系统性偏差。作者提出使用完全贝叶斯推理，通过马尔可夫链蒙特卡洛（MCMC）和近似贝叶斯计算（ABC）两种方法学习参数的后验分布，并比较了二者在精度和效率上的表现。基于 Y 染色体单倍型数据库，他们展示了全贝叶斯方法得到的似然比优于插件法。本文属于法医学应用，与流行病学中稀有事件匹配、基因数据库分析等方法有类比价值。对您而言，本文的贝叶斯计算方法和似然比评估思路可能为统计计算（软件开发和 MCMC 实现）提供实践案例。
- **关键技术**: `Markov Chain Monte Carlo`, `Approximate Bayesian Computation`, `Poisson-Dirichlet distribution`, `likelihood ratio`, `full Bayesian inference`
- **为什么对您有用**: 本文属于法医学应用，与次要兴趣流行病学中的稀有事件似然比评估有相通之处。虽然您的主要兴趣不在贝叶斯非参数，但 MCMC 和 ABC 是统计计算中的核心工具，您对统计软件开发很熟悉，可以借鉴其计算实现和性能比较方法。由于您的武器库缺少贝叶斯非参数和 ABC 的核心知识，如需深入此方向需先补足相关理论，因此属于暂不可做。

### 4. [10.1111/sjos.12578](https://doi.org/10.1111/sjos.12578) · [arXiv](https://arxiv.org/abs/2201.06994) — Flexible clustering via hidden hierarchical Dirichlet priors
- **作者**: Antonio Lijoi, Igor Prünster, Giovanni Rebaudo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 1 · pp 213-234
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 该文提出一种基于隐藏层次狄利克雷先验的灵活贝叶斯非参数聚类模型。与传统嵌套狄利克雷过程不同，该方法允许不同样本的分布部分共享而非强制归为单一聚类。作者导出了随机划分分布的闭式表达，从而深入理解模型的聚类行为，并支撑MCMC推断。针对多群体场景下原有算法的局限性，设计了更高效的采样方案，并能同时检验群体同质性。通过模拟和真实数据与嵌套狄利克雷过程进行对比，展示了方法的灵活性和有效性。
- **关键技术**: `nested Dirichlet process`, `Bayesian nonparametrics`, `random partition distribution`, `MCMC sampling`, `hidden hierarchical Dirichlet prior`
- **为什么对您有用**: 本文属于贝叶斯非参数聚类，与您的主要兴趣（因果推断、高维统计等）无直接关联。但论文中的MCMC算法设计和计算效率改进对统计计算有一定参考价值，不过并非您武器库中的核心工具。作为gateway阅读，本文不属于您当前关注的方向，建议暂不深入。

### 5. [10.1111/sjos.12571](https://doi.org/10.1111/sjos.12571) — Spectral analysis of Markov switching GARCH models with statistical inference
- **作者**: Maddalena Cavicchioli
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Modena and Reggio Emilia
- **分类**: vol 50 · issue 1 · pp 102-119
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究马尔可夫转换GARCH（MS-GARCH）模型的谱分析，推导了自协方差函数和谱密度的闭式矩阵表达式，利用Riesz-Fischer定理将谱表示表示为自协方差函数的傅里叶变换。在适当假设下，证明了谱密度样本估计量的相合性和渐近正态性。进一步讨论了阶别识别和参数估计等统计推断应用。仿真研究验证了渐近性质的有效性，并通过实际金融时间序列示例展示了频率域分析的适用性。该工作属于时间序列计量经济学中的模型推断范畴，与研究者主要关注的因果推断、高维统计和U统计量方向无直接交叉。
- **关键技术**: `Markov switching GARCH`, `spectral density estimation`, `Riesz–Fischer theorem`, `autocovariance function`, `asymptotic normality`, `parametric time series inference`
- **为什么对您有用**: 本文属于时间序列计量经济学，与研究者主要兴趣（因果推断、高维统计、U统计量）关联度较低。但其谱分析方法可作为处理时间序列数据时频率域工具的一般性参考，对流行病学或经济理论中的长期数据可能具有间接启发意义。研究者无需深入此方向，保留文档备查即可。

### 6. [10.1111/sjos.12612](https://doi.org/10.1111/sjos.12612) — A conversation with Elja Arjas (Helsinki, November 2021 and March 2022)
- **作者**: Jukka Corander
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Statistics Finland · University of Helsinki · University of Oslo · Wellcome Sanger Institute
- **分类**: vol 50 · issue 1 · pp 3-12
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文是Scandinavian Journal of Statistics发表的一篇访谈录，对象是芬兰赫尔辛基大学退休教授Elja Arjas，采访时间为2021年11月至2022年3月。访谈主要回顾了Arjas在芬兰统计学科建立与发展中的核心作用，以及芬兰统计学在过去半个多世纪从无到有、逐步成长的历史。对话涉及芬兰统计学会的成立、早期研究方向的确定、国际学术网络的建立等关键事件，并穿插了对Arjas个人学术生涯的回忆。文章还尝试对统计学在芬兰的未来发展提出一些展望。整篇以口语化形式呈现，没有方法论贡献，但对理解北欧统计学派的发展脉络具有参考价值。对于主要关注因果推断和高维统计理论的研究者而言，本文不直接涉及技术问题，短期内无实际可用的方法学迁移。
- **关键技术**: `historical narrative`, `oral history`, `academic biography`
- **为什么对您有用**: 本文不属于研究者所列的任何主要或次要兴趣方向（因果推断、高维统计、半参理论等），因此不提供直接的方法学借鉴。作为统计学科发展史的参考读物，研究者可从中了解芬兰统计学界的传统与变迁，但目前无法与自身技术武器库中的任何工具产生具体结合（缺少统计史研究方法）。暂不可做后续工作，除非研究者有意涉足科学史或学科社会学方向。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

