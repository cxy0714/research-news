# Scand. J. Stat. — Vol 51  Issue 1  ·  2026-06-23

- 共 17 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 17 篇全部抓到（对照 OpenAlex 17 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期文章主要围绕**半参数与非参数建模**、**假设检验与统计推断基础**以及**高维图模型与变量选择**三条主线展开，同时涉及因果推断中的缺失机制检验、分布式计算与计数数据模型等议题。半参数方法贯穿于缺失数据、纵向数据及测量误差等多种数据场景；假设检验方向则既有针对特定模型的设定检验，也有对 P 值概念与置信区间构建的理论反思；高维统计方面重点关注图模型结构恢复中的尺度不变性与正性假设放宽。

在**半参数与非参数建模**主线中，本期论文展示了该方法处理复杂数据结构的灵活性。针对缺失数据与测量误差问题，*Nested semiparametric method* 利用半参数充分维数约简处理病例对照研究中的状态缺失，*Extrapolation estimation* 则通过改进的 SIMEX 外推算法解决非参数回归中的测量误差，两者均追求稳健的估计效率。在模型结构上，*Marginal additive models* 与 *Sparse additive models* 分别从纵向数据总体平均推断和高维小波展开角度推进了加性模型的建模能力，前者关注聚类变异的稳健推断，后者通过分位数通用阈值解决高维惩罚参数选择难题。此外，*Locally adaptive Bayesian isotonic regression* 引入半收缩先验以适应单调函数的局部突变。

**假设检验与推断基础**方向集中探讨模型设定检验与推断工具的改进。*Testing the missing at random assumption* 利用工具变量构造 Hausman 型检验，解决了广义线性模型中 MAR 与 MNAR 机制的识别难题，直接关联因果推断中的敏感性分析。*Flexible specification testing* 通过基函数展开提出了分位数回归的非参数设定检验。值得注意的是，本期包含两篇对经典推断工具的反思文章：*Divergence vs. decision P-values* 从理论上厘清了两种 P 值概念的混淆，*Locally correct confidence intervals* 则提出了二项比例置信区间的新准则以精确控制覆盖概率。*Nearly unstable integer‐valued ARCH process* 将单位根检验拓展至计数时间序列，填补了整数值过程的检验空白。

**高维图模型与变量选择**主线聚焦于现有方法假设的放宽与改进。*Partial correlation graphical LASSO* 针对高斯图模型提出基于偏相关的惩罚族，解决了传统图形 LASSO 因数据标准化导致的推断偏差问题。*Structure recovery for discrete Markov random fields* 则在无需正性分布假设的条件下，实现了部分观测离散马尔可夫随机场的结构恢复，扩展了高维图模型的应用边界。

总体来看，关注**因果推断与缺失数据**的读者可优先阅读 *Testing the missing at random assumption*；对**半参数效率与高维推断**感兴趣者，建议重点参阅 *Communication‐efficient low‐dimensional parameter estimation* 与 *Nested semiparametric method*；研究**高维图模型**的读者可关注 *Partial correlation graphical LASSO* 一文。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12685](https://doi.org/10.1111/sjos.12685) — Testing the missing at random assumption in generalized linear models in the presence of instrumental variables
- **作者**: Rui Duan, C. Jason Liang, Pamela A. Shaw, Cheng Yong Tang, Yong Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Harvard University · National Institute of Allergy and Infectious Diseases · Kaiser Permanente Washington Health Research Institute · University of Pennsylvania · Temple University
- **分类**: vol 51 · issue 1 · pp 334-354
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对广义线性模型（GLM）中缺失数据机制（MAR vs MNAR）的检验问题，提出一种基于工具变量（IV）的假设检验方法。其核心思路是构造两个在MAR下渐近等价的估计量（一个依赖IV，另一个不依赖），而当MNAR成立时两者的概率极限不同。通过度量两个估计量之间的偏差（如Hausman型差异），构造检验统计量，并推导其在原假设下的渐近分布。方法不依赖于缺失模型的完全指定，仅需存在有效IV，具有较强的实用性。模拟和实际数据分析验证了该检验的有限样本表现。该工作直接连接因果推断中缺失数据的敏感性分析问题，且为IV在缺失机制检验中的创新应用。对您而言，可利用您非常熟悉的估计理论和假设检验工具，立即将该检验框架推广到更复杂的因果参数（如ATE或ATT）的MAR假设检验中，属于立即可做的方向。
- **关键技术**: `Hausman-type discrepancy test`, `instrumental variables (IV) for missing data`, `generalized linear models (GLM)`, `MAR vs MNAR hypothesis testing`, `asymptotic null distribution`
- **为什么对您有用**: 直接连接因果推断中缺失数据的机制检验与工具变量方法，属于您主要兴趣中的causal inference（IV、敏感性分析）。您非常熟悉估计理论（very_familiar: estimation theory in causal inference）和假设检验，可立即可用该检验框架在其他因果参数（如ATE、ATT）上验证MAR假设的合理性，属于立即可做的迁移方向。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.12675](https://doi.org/10.1111/sjos.12675) · [arXiv](https://arxiv.org/abs/2104.10099) — Partial correlation graphical LASSO
- **作者**: Jack Storror Carter, David Rossell, Jim Q. Smith
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 32-63
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高斯图模型中的变量尺度变换问题，提出基于偏相关的惩罚族，以替代传统的精度矩阵正则化方法。传统图形LASSO或贝叶斯方法需对数据标准化，但标准化会扭曲推断结果。作者证明偏相关惩罚族（包括最大似然和对数惩罚）具有天然的尺度不变性。具体提出偏相关图LASSO（pc-gLASSO），对偏相关系数施加L1惩罚，优化问题虽非全局凸但条件凸，可通过坐标下降求解。模拟和两个真实数据集表明，pc-gLASSO在恢复图结构上不仅消除了标准化偏差，还通常优于标准图形LASSO。该方法为高维协方差选择提供了一种更稳健的替代方案，直接关联高维统计中的正则化图模型方法，研究者可用其在高维渐近方面的专长分析该方法的模型选择一致性。
- **关键技术**: `partial correlation`, `graphical LASSO`, `scale invariance`, `conditional convex optimization`, `penalized likelihood`
- **为什么对您有用**: 本文聚焦高维图模型中的尺度不变性问题，属于高维统计中正则化方法的重要改进。研究者对高维渐近（very_familiar）可直接用于分析pc-gLASSO的模型选择相变阈值；其软件开发经验也便于实现和扩展该算法。立即可做：利用高维渐近工具推导pc-gLASSO的模型选择一致性条件或误差界。

### 2. [10.1111/sjos.12674](https://doi.org/10.1111/sjos.12674) · [arXiv](https://arxiv.org/abs/1911.12198) — Structure recovery for partially observed discrete Markov random fields on graphs under not necessarily positive distributions
- **作者**: Florencia Leonardi, Rodrigo Carvalho, Iara Frondana
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 64-88
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究部分观测离散马尔可夫随机场（MRF）的图结构恢复问题，允许节点集有限或可数无穷，且分布不必满足通常的正性条件。方法提出惩罚条件似然准则来估计每个节点的邻域，通过最小化带L1惩罚的负条件对数似然实现邻域选择。在有限节点情形下，可概率1恢复整个图；在可数无穷节点情形下，通过允许候选邻域随样本量增长，可概率1恢复任意有限子图。收敛性证明基于条件似然函数的分析，不依赖正性假设，从而适用于更广泛的分布。模拟和真实数据（国际股票指数市场）验证了方法的有效性。对您有用：本文涉及高维图模型的结构恢复，与您的高维统计兴趣直接相关，且不要求正性的想法可借鉴到因果推断中的图学习（如处理缺失数据下的马尔可夫等价类推断）。
- **关键技术**: `Penalized conditional likelihood`, `Neighborhood selection`, `Not-necessarily-positive distribution`, `Graph recovery consistency`, `Infinite countable vertex set`
- **为什么对您有用**: 本文直接关联您 high-dimensional statistics 兴趣中的图模型恢复方向，且方法不要求正性条件，可启发因果推断中部分观测图的学习。您 very_familiar 中的高维渐近理论与非参数统计可直接用于分析该惩罚估计量的收敛速率或提出更高效的估计。立即可做：您熟悉的高维渐近和非参数工具足以理解并评估本文的理论结果，并可考虑将方法扩展到部分观测的高维因果图。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.12673](https://doi.org/10.1111/sjos.12673) — A nested semiparametric method for case‐control study with missingness
- **作者**: Ge Zhao, Yanyuan Ma, Jill Schnall Hasler, Scott Damrauer, Michael Levin, Jinbo Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Portland State University · Pennsylvania State University · University of Pennsylvania
- **分类**: vol 51 · issue 1 · pp 201-219
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 case-control 研究中，部分个体的真实 case status 缺失，目标是估计 genuine case 与 control 的 odds ratio 参数。作者引入 noncase 概念，通过 semiparametric sufficient dimension reduction 方法预测个体为 genuine case 的概率，从而实现缺失值的 imputation。估计量被证明具有 root-n 渐近正态性，且由于使用了 efficient semiparametric SDR estimator，估计稳定。该方法在维度约减框架下统一并推广了现有方法，模拟和扩张型心肌病数据实证展示了有限样本性能。对您在 semiparametric theory 和 efficiency theory 方面的兴趣有直接参考价值。
- **关键技术**: `semiparametric sufficient dimension reduction`, `odds ratio estimation`, `missing data imputation`, `root-n asymptotic normality`, `case-control study design`
- **为什么对您有用**: 本文直接涉及您 primary interest 中的 semiparametric theory 和 efficiency theory——特别是 semiparametric SDR estimator 的效率性质和 root-n CAN 证明。您可以用 very_familiar 的 minimax bounds 和 estimation theory 工具审视其效率声称是否达到 semiparametric efficiency bound，或用 moderately_familiar 的 semiparametric theory 框架分析 influence function 构造。**立即可做**：用您熟悉的 semiparametric efficiency 理论验证其估计量是否 efficient，或探索是否可用 HOIF 进一步改进高维协变量情形下的估计效率。

### 2. [10.1111/sjos.12681](https://doi.org/10.1111/sjos.12681) — Marginal additive models for population‐averaged inference in longitudinal and cluster‐correlated data
- **作者**: Glen McGee, Alex Stringer
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Waterloo
- **分类**: vol 51 · issue 1 · pp 384-401
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在纵向与集群相关数据设定下，本文提出 marginal additive model (MAM)，目标是估计 population-averaged mean function 的非线性关联，同时量化 cluster-level 变异性。估计方法基于 penalized spline M-estimation，结合 marginal quasi-likelihood 与 working correlation structure；作者设计了迭代算法以校正 penalty 参数估计对方差估计的影响，并给出 sandwich-type robust standard error。理论部分建立了估计量的渐近正态性与一致性，但未给出显式的 semiparametric efficiency bound 或收敛率。实证分析包括 beaver 觅食行为的纵向研究与西非 Loa loa 感染的空间数据。对您在纵向因果推断中的 semiparametric efficiency 理论有参考价值，但本文未涉及 influence function 或 debiasing 技术。
- **关键技术**: `penalized spline M-estimation`, `marginal quasi-likelihood`, `working correlation structure`, `sandwich variance estimator`, `cluster-robust inference`, `population-averaged model`
- **为什么对您有用**: (1) 连接到 longitudinal causal推断中的 population-averaged estimand 设定，以及 semiparametric theory 中 marginal model 的效率问题。(2) 您的 M-estimation theory (moderately_familiar) 可以用来审视本文的 variance estimator 是否达到 semiparametric efficiency bound——本文未给出此分析，这是一个可切入的理论口子。(3) **中期可做**：需先在 semiparametric efficiency theory 上长肌肉，推导 MAM 设定下的 efficient influence function 并验证作者的标准误是否 efficient。

### 3. [10.1111/sjos.12680](https://doi.org/10.1111/sjos.12680) · [arXiv](https://arxiv.org/abs/2207.04083) — Sparse additive models in high dimensions with wavelets
- **作者**: Sylvain Sardy, Xiaoyu Ma
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 89-108
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维稀疏加性模型，其中协变量数量可远大于样本量，假设仅有少量协变量对响应有预测信息。作者利用小波基展开将非参数加性分量的估计转化为稀疏表示问题，并提出一种不依赖交叉验证的凸优化求解方案。关键贡献在于提出了分位数通用阈值（quantile universal threshold）来直接设定惩罚参数，无需繁琐调参；同时提出了基于Stein无偏风险估计（SURE）的预测导向规则。模拟和真实数据实验表明，该方法在控制假发现率（FDR）、真阳性率（TPR）和均方误差方面表现良好，尤其在高维场景下具有计算效率和良好的FDR-TPR权衡。该工作将小波变换的快速算法与稀疏模型选择相结合，为高维非参数建模提供了实用工具。您对nonparametric statistics和高维统计的兴趣与此直接相关，可借鉴其阈值规则思想用于其他非参数模型选择问题。
- **关键技术**: `wavelet transforms`, `quantile universal threshold`, `Stein unbiased risk estimation`, `convex optimization`, `sparse additive models`, `model selection`
- **为什么对您有用**: 本文直接涉及高维非参数加性模型的模型选择，与您的nonparametric statistics和高维统计兴趣紧密相连。您掌握的nonparametric statistics理论（如minimax rate、光滑性条件）可用于分析文中阈值规则在稀疏场景下的最优性，检验其提出的分位数通用阈值是否达到自适应收敛速度。立即可做：运用您熟悉的nonparametric minimax bound方法，对文中方法在特定光滑性类（如Sobolev、Besov）下的表现进行理论界定，或比较其与现有方法的效率。

### 4. [10.1111/sjos.12670](https://doi.org/10.1111/sjos.12670) · [arXiv](https://arxiv.org/abs/2107.12586) — Extrapolation estimation for nonparametric regression with measurement error
- **作者**: Weixing Song, Kanwal Ayub, Jianhong Shi
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 1-31
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究带有正态测量误差的非参数回归模型中回归函数的估计问题，目标是在经典误差-in-variables设定下恢复潜在回归函数。作者提出了一种外推算法，通过对局部线性逼近与观测响应之间偏差的核加权最小二乘直接应用条件期望，成功绕过了经典SIMEX方法中的模拟步骤，显著降低了计算时间。该方法提供了外推函数的精确形式，但当带宽小于测量误差标准差时，不能简单地将外推变量设为-1来获得估计。文章建立了所提估计量的大样本性质，包括收敛速率和渐近分布，并通过模拟研究和实际数据分析验证了方法的有效性。对您而言，这是非参数理论在测量误差问题中的经典应用，涉及核估计和inverse problem的正则化处理。
- **关键技术**: `SIMEX extrapolation`, `local linear kernel estimation`, `measurement error correction`, `deconvolution methods`, `kernel-weighted least squares`
- **为什么对您有用**: 本文连接到您primary interest中的非参数理论，具体涉及核估计在测量误差（inverse problem）设定下的正则化处理。您武器库中'very_familiar'的inverse problems with random noise和非参数统计可以直接用来分析该方法的minimax最优性、验证其收敛速率是否达到deconvolution问题的信息论下界。**立即可做**：用您熟悉的minimax bound工具分析该外推估计量在更一般误差分布下的最优性，或探索与HOIF结合以改善边界效应。

### 5. [10.1111/sjos.12676](https://doi.org/10.1111/sjos.12676) · [arXiv](https://arxiv.org/abs/2208.05121) — Locally adaptive Bayesian isotonic regression using half shrinkage priors
- **作者**: Ryo Okano, Yasuyuki Hamura, Kaoru Irie, Shonosuke Sugasawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 109-141
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对等渗回归（单调函数估计）问题，提出了一种新的贝叶斯方法。核心思想是将全局-局部收缩先验引入一阶差分，具体设计为半收缩先验（half shrinkage priors）用于正随机变量，从而实现对目标函数局部突变的自适应处理。方法利用Gibbs采样实现快速后验推断。理论上证明了后验均值估计对大幅跳跃具有稳健性，且未变化点处的渐近风险可得到改进。模拟和真实数据实验验证了方法效果。该工作将收缩先验的思想从高维回归拓展到单调性约束问题，属于非参数贝叶斯领域一个有价值的增量贡献。对于您感兴趣的非参数理论方向，该方法提供了一种处理形状约束的自适应先验构造思路，但贝叶斯计算框架与您的常规工具差距较大。
- **关键技术**: `half shrinkage priors`, `global-local shrinkage priors`, `isotonic regression`, `Gibbs sampling`, `Bayesian nonparametrics`, `posterior consistency`
- **为什么对您有用**: 与您的「半参数与非参数理论」兴趣直接相关，等渗回归是非参数估计的经典问题，本文的全局-局部收缩先验在局部自适应性和理论风险分析上有新进展。但该工作完全基于贝叶斯框架，而您的技术库中对贝叶斯方法不熟悉（moderately_familiar中无贝叶斯模型项），且计算方面Gibbs采样并非您擅长的统计计算权衡方向。因此，目前属于「暂不可做」：核心贝叶斯计算和后验一致性工具不在武器库中，建议先通过阅读了解思想，但直接复现或扩展难度较大。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12683](https://doi.org/10.1111/sjos.12683) — Communication‐efficient low‐dimensional parameter estimation and inference for high‐dimensional Lp$$ {L}^p $$‐quantile regression
- **作者**: Junzhuo Gao, Lei Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Nankai University
- **分类**: vol 51 · issue 1 · pp 302-333
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在分布式数据环境下，研究高维 L^p-quantile 回归中低维目标参数的估计与推断问题，目标参数为预先指定的低维系数，高维协变量作为 nuisance 参数。核心方法是两阶段估计：首先用 regularized projection score 处理高维 nuisance 参数的影响，然后提出两种 communication-efficient surrogate projection score estimator 以减少分布式计算中的通信成本。理论贡献包括建立估计量的渐近正态性、收敛速率，以及在适当正则条件下达到 semiparametric efficiency bound。模拟和 Communities and Crime 数据集验证了有限样本表现。对您在 efficiency theory 和 debiased ML 方向的研究有直接参考价值，特别是分布式设定下的 orthogonal score 构造。
- **关键技术**: `regularized projection score`, `communication-efficient estimation`, `distributed inference`, `orthogonal score`, `debiased estimation`, `L^p-quantile regression`
- **为什么对您有用**: 直接连接到 primary interest 中的 efficiency theory (semiparametric efficiency bounds) 和 debiased ML——本文的 projection score 方法本质上是一种 orthogonalization/debiasing 技术。您熟悉的 minimax bounds 和 semiparametric theory（moderately_familiar）可以用来审视其效率声称是否紧。立即可做：用 very_familiar 的高维渐近理论验证其正则条件是否可以放宽，或用 moderately_familiar 的 semiparametric theory 推导更一般的 efficiency bound。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1111/sjos.12671](https://doi.org/10.1111/sjos.12671) · [arXiv](https://arxiv.org/abs/2105.09003) — Flexible specification testing in quantile regression models
- **作者**: Tim Kutzker, Nadja Klein, Dominik Wied
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 355-383
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对分位数回归模型提出三种新颖的、一致的设定检验，允许协变量效应随分位数变化且具有非线性形式，突破了经典检验对线性或参数形式的限制。通过基函数展开（如样条）参数化条件分位数函数，构造Cramér-von Mises型检验统计量，并推导其极限分布，同时提出残差bootstrap方法实现有限样本推断。进一步，修改检验统计量以提高局部备择下的功效，并对理论性质进行系统分析。蒙特卡洛模拟验证了检验在有限样本下的尺寸和功效表现，两个实际数据应用（德国条件收入分布、澳大利亚电力市场价格）展示了方法的实用性。总体而言，该方法为分位数回归的非参数设定检验提供了灵活且一致的推断框架。对您而言，直接连接到假设检验中的非参数设定检验方向，您熟悉的非参数统计和bootstrap技术可立即用于评估该方法的理论细节，并考虑将其拓展至因果推断中的分位数处理效应设定检验。
- **关键技术**: `Cramér-von Mises test`, `quantile regression specification test`, `bootstrap approximation`, `basis function expansion (splines)`, `local power analysis`, `empirical process theory`
- **为什么对您有用**: 本文属于假设检验中非参数设定检验的重要进展，直接关联您的primary interest“数学统计与假设检验”。您非常熟悉的非参数统计工具（特别是经验过程和bootstrap）可立即用于评估其理论框架、收敛速率及功效性质，并检验论文中推导的极限分布是否严格。立即可做：基于您对非参数统计的深入理解，可以快速掌握论文核心，并考虑将该检验框架应用于您关注的因果推断中的分位数处理效应设定检验（如连续处理变量下的分位数效应）。

### 2. [10.1111/sjos.12687](https://doi.org/10.1111/sjos.12687) — Greenland, S. (2023). Divergence vs. decision P‐values: A distinction worth making in theory and keeping in practice. <i>Scandinavian Journal of Statistics</i> , 50, 1–35, https://onlinelibrary.wiley.com/doi/10.1111/sjos.12625
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 425-425
- 相关性 6/10 · novelty: `survey`
- **摘要**: 这篇论文深入区分了两种P值概念：divergence P-value（基于证据强度，如似然比检验中的P值）和 decision P-value（基于Neyman-Pearson决策框架，如UMPU检验中的P值）。作者指出，两者在定义、解释和实践中常被混淆，而这种混淆可能导致统计推断的误导。论文系统回顾了两种P值的数学基础和适用场景，强调 divergence P-value 更适合作为连续证据度量，而 decision P-value 则与预先设定的决策规则绑定。作者还讨论了两种P值在置信区间、多重检验等问题中的不同表现。最后，论文呼吁理论统计界和实践者在教学和发表中明确区分这两种P值。这篇论文对您假设检验的理论兴趣有直接启发，尤其有助于厘清基础概念，强化对统计推断本质的理解。
- **关键技术**: `divergence P-value`, `decision P-value`, `likelihood ratio test`, `Neyman-Pearson testing`, `UMPU test`
- **为什么对您有用**: 本文直接针对 hypothesis testing 的基础概念，与您主要兴趣中的数学统计与假设检验高度契合。您现有对假设检验的非常熟悉（very_familiar）程度足以充分消化本文论点，属于立即可做（可直接阅读全文）。该文虽非方法创新，但作为一篇系统性的概念澄清，有助于您后续在研究或教学中更精确地使用P值，避免常见误解。

### 3. [10.1111/sjos.12672](https://doi.org/10.1111/sjos.12672) · [arXiv](https://arxiv.org/abs/2106.15521) — Locally correct confidence intervals for a binomial proportion: A new criteria for an interval estimator
- **作者**: Paul H. Garthwaite, Maha W. Moustafa, Fadlalla G. Elfadaly
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 220-244
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对二项比例置信区间提出了一种新准则——'局部正确置信区间'，要求单侧区间的覆盖概率在边界点恰好等于名义置信水平，从而纠正常用方法（如Wilson、Agresti-Coull）覆盖不足的问题。作者证明了满足该准则的区间必然存在，并构造了一种显式方法，其在所有满足准则的方法中平均区间长度最短。与Clopper-Pearson（金标准）相比，新方法在保持覆盖正确性的前提下将区间长度显著缩短；Mid-p方法也满足该准则，但区间略宽。证明利用了二项分布的单峰性和序贯属性，并给出了有限样本下的最优性论证。该工作对您在假设检验与置信区间理论的研究中提供了精确控制覆盖概率与区间长度的新工具，可拓展至其他离散分布或非参数置信区间的类似优化问题。
- **关键技术**: `locally correct confidence intervals`, `Clopper–Pearson method`, `mid-p method`, `optimal expected length`, `binomial proportion inference`, `exact coverage control`
- **为什么对您有用**: 直接连接您对'假设检验与置信区间理论'的兴趣，特别是精确覆盖概率的区间构造。您'非常熟悉'的工具箱中的'非参数统计'和'minimax界'可用于评估该准则能否推广到Poisson或Negative Binomial等分布，且证明中最优性论证的'序贯属性'思路可能启发高维稀疏比例推断的新方法。立即可做：用当前武器即可复现并评估该准则对实际数据（如流行病学中的小样本比例）的收益。

### 4. [10.1111/sjos.12689](https://doi.org/10.1111/sjos.12689) · [arXiv](https://arxiv.org/abs/2107.07963) — Nearly unstable integer‐valued ARCH process and unit root testing
- **作者**: Wagner Barreto‐Souza, Ngai Hang Chan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 402-424
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对计数时间序列数据提出近乎不稳定整数自回归条件异方差（NU-INARCH）过程，研究其单位根检验问题。证明该过程经适当标准化后弱收敛到Cox-Ingersoll-Ross扩散，条件最小二乘估计量的渐近分布由随机积分泛函给出。蒙特卡洛仿真验证了有限样本下渐进性质的有效性，且表明近乎不稳定方法在非近不稳定设定下也优于平稳假设。提出基于该过程的单位根检验，并模拟了其第一类错误和功效。最后应用于英国每日COVID-19死亡人数数据。该工作将经典单位根检验拓展到整数值时序过程，与您主要兴趣中的假设检验子领域直接相关，且计数时间序列在流行病学应用中常见，可为因果推断中纵向计数结果的检验提供参照。
- **关键技术**: `weak convergence to diffusion`, `conditional least squares estimator`, `unit root test`, `INARCH process`, `Cox-Ingersoll-Ross diffusion`, `Monte Carlo simulation`
- **为什么对您有用**: 该文属于假设检验中的单位根检验问题，直接对应您主要兴趣“数学统计与假设检验”的具体子方向。您的武器库中非参统计和逆问题工具可用于分析其弱收敛条件，但该文依赖扩散极限和随机积分泛函，属于您目前 moderately_familiar 未覆盖的内容，因此短期内难以直接上手贡献；不过可作为打开时间序列单位根领域的学习材料，为今后处理纵向计数数据中的平稳性检验提供基础。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12679](https://doi.org/10.1111/sjos.12679) · [arXiv](https://arxiv.org/abs/2207.11303) — Estimating absorption time distributions of general Markov jump processes
- **作者**: Jamaal Ahmad, Martin Bladt, Mogens Bladt
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 1 · pp 171-200
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 该论文研究一般马尔可夫跳跃过程吸收时间分布的估计问题，特别针对时间非齐次情形。传统方法要求可交换子强度矩阵，本文放宽了这一假设。采用极大似然估计和期望最大化（EM）算法进行参数估计，并提出了分段常数强度矩阵函数以简化表示，通过参数线性模型连接不同区间的强度函数。理论部分建立了估计量的渐近性质，实证部分使用人工分布和真实数据验证方法有效性。对您作为统计学计算和算法研究者而言，这篇论文提供了一个经典问题在现代算法框架下的完整解决方案，重点展示了EM算法与矩阵解析方法的结合使用。
- **关键技术**: `Expectation-Maximization (EM) algorithm`, `Maximum likelihood estimation`, `Piecewise constant intensity matrix`, `Matrix analytic methods`, `Parametric linear model`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您「statistical computing (numerical methods, algorithm)」兴趣。文中EM算法与矩阵解析方法的结合实践，可启发您在自己的软件开发和因果推断工具中实现类似参数化建模策略。**立即可做**：您现有的软件工程和算法开发经验足以理解和复现其计算流程，无需额外工具。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.12682](https://doi.org/10.1111/sjos.12682) — On the perimeter estimation of pixelated excursion sets of two‐dimensional anisotropic random fields
- **作者**: Ryan Cotsakis, Elena Di Bernardino, Thomas Opitz
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Université Côte d'Azur · Laboratoire Jean-Alexandre Dieudonné · Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement · Biostatistique et processus spatiaux
- **分类**: vol 51 · issue 1 · pp 268-301
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究二维各向异性随机场excursion set的周长估计问题。目标是从规则正方形网格上的二进制数字图像中估计excursion边界的长度。提出了一种基于分段线性近似的估计量，直接作用于像素化图像。不需要高斯性或各向同性假设，仅要求像素尺寸趋于零即可证明估计量的一致性。在强混合条件下，当考虑多个水平同时估计时，建立了多元中心极限定理。数值实验验证了有限样本下的统计性质。该工作属于空间统计与几何特征估计领域，与您的核心研究兴趣（因果推断、高维统计、U统计量等）无直接重叠。
- **关键技术**: `piecewise linear approximation`, `excursion set`, `pixelated binary image`, `strong mixing condition`, `central limit theorem`, `multivariate CLT`
- **为什么对您有用**: 本文内容与您的primary interests（因果推断、高维、U统计量等）无直接关联，亦不属于您gateway reading范畴（astrostatistics等）。技术库中缺乏空间统计与几何估计相关工具（如strong mixing条件下的渐近理论），短期内难以迁移。不建议投入时间阅读全文。

### 2. [10.1111/sjos.12677](https://doi.org/10.1111/sjos.12677) — Some mechanisms leading to underdispersion: Old and new proposals
- **作者**: Pedro Puig, Jordi Valero, Amanda Fernández‐Fontelo
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Universitat Autònoma de Barcelona · Centre de Recerca Matemàtica · Universitat Politècnica de Catalunya · Humboldt-Universität zu Berlin
- **分类**: vol 51 · issue 1 · pp 245-267
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文系统回顾并拓展了计数数据中欠分散（underdispersion）的生成机制。首先从到达过程的新视角重新审视了更新过程、纯生过程等经典机制，并引入了基于生灭过程稳态分布的新机制（如状态依赖服务率的队列模型）。其次将加权泊松分布等已知的欠分散分布与生灭过程建立了联系。此外，讨论了经典和可变二项稀疏操作如何生成带负相关的二元欠分散计数分布。最后通过一个生物剂量测定实例展示了所提机制的应用。对您而言，若未来涉及流行病学或生物学中计数数据的建模（如发病率或计数反应），本文的机制分类可提供先验分布选择的指导。
- **关键技术**: `underdispersed count distributions`, `renewal and birth-death processes`, `weighted Poisson distribution`, `binomial thinning`, `state-dependent service rates`
- **为什么对您有用**: 本文主题属于计数数据建模，不直接匹配您的主要兴趣方向（因果推断、高维统计等）。但若未来您涉及流行病学或经济学中的计数结果（如发病率、交易次数）的因果推断或描述性建模，欠分散机制的理解有助于选择正确的分布假设。您的武器库（非参数统计、M估计）可用来研究这些机制在模型误设下的稳健性，但当前这篇仅是综述性机制分类，缺乏可直接攻克的数学口子，属于暂不可做——核心工具不在常用武器库中（缺计数数据特定概率模型经验）。

### 3. [10.1111/sjos.12678](https://doi.org/10.1111/sjos.12678) — Design for order‐of‐addition experiments with two‐level components
- **作者**: Hengzhen Huang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Guangxi Normal University
- **分类**: vol 51 · issue 1 · pp 142-170
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究两水平组分的序贯添加实验（order-of-addition, OofA）的统计设计问题。传统OofA仅关注组件顺序对响应的影响，而本文同时考虑组件本身的两水平因子效应（如改变浓度或类型）。作者提出一种系统构造方法，将顺序设计和因子设计结合，得到平衡且运行次数经济的设计。在经验模型下，所构造的设计具有D-、A-、E-最优性等良好性质。该方法还可推广至过程变量数与组件数不同的情形以及多水平组分。本文属于经典实验设计领域，未涉及因果识别或现代高维统计工具。
- **关键技术**: `order-of-addition design`, `two-level factorial design`, `D-optimality`, `balanced design`, `run size economy`
- **为什么对您有用**: 本文与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接关联。您的武器库中的非参数统计和极小极大界工具可用来评估该设计方法在更灵活模型下的效率，但这不是文章重点。目前属于暂不可做方向，因为您未涉猎实验设计最优性理论。可作为交叉领域参考，但无需深入阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

