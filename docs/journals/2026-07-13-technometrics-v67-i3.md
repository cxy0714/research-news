# Technometrics — Vol 67  Issue 3  ·  2026-07-13

- 共 16 篇 · Technometrics
- 目录核对 ✅ 16 篇全部抓到（对照 OpenAlex 19 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Technometrics》第67卷第3号共收录16篇论文，整体上呈现两条主线：**统计计算与大规模模型加速**，以及**空间/时空数据建模与监控**。前者聚焦于高斯过程、张量分解、Lasso诊断等经典方法的计算效率提升，后者则覆盖空间聚类、非参数监控、竞争风险建模等应用导向的方法。此外，还有少量论文涉及假设检验（周期检测）、实验设计（逆映射、退化试验）和预测校准，但数量较少，未形成独立主线。

在**统计计算与大规模模型加速**主线上，Block Vecchia Approximation 针对高斯过程似然计算，通过块分组和GPU并行化显著提升Vecchia近似的效率，本质是计算技巧而非模型创新。Personalized Tucker Decomposition 提出“共享+个性化”的张量分解框架，并给出收敛性保证，适用于异质性张量数据的异常检测。Bivariate DeepKriging 用深度神经网络替代传统协克里金进行双变量空间插值，并建立与线性区域化模型的理论联系。Assessment of Case Influence in the Lasso 则通过case-weight路径方法高效计算Lasso的Cook距离，避免了重拟合，并引入可视化工具。Robust Covariance Estimation for Matrix-Valued Data 提出MMCD方法，直接利用矩阵结构进行鲁棒协方差估计，避免了向量化带来的维数灾难，并证明了矩阵仿射等变性和高breakdown point。

在**空间/时空数据建模与监控**主线上，Clustering Spatial Data with a Mixture of Skewed Regression Models 使用偏态分布混合回归模型处理空间聚类，避免因数据偏态或重尾导致的过拟合。Partially Observable Online Nonparametric Monitoring 针对部分可观测的时空数据流，结合随机投影、去相关秩统计量和数据增广实现实时异常检测，并给出理论保证。A Spatially Correlated Competing Risks Model 在贝叶斯框架下分析超级计算机GPU故障的空间模式，展示了复杂数据结构下的建模流程。此外，Derivative Based Global Sensitivity Analysis 提出基于导数的条件熵上界作为熵基敏感性指标的代理，适用于偏态或重尾分布下的变量筛选。

与因果推断、半参数效率或高维统计最直接相关的论文是：**Noise Resistant Control Charts for Detecting Periodicity**（假设检验框架与有限样本理论，噪声鲁棒特征设计可启发因果推断中的测量误差处理）、**Robust Covariance Estimation for Matrix-Valued Data**（矩阵结构下的鲁棒估计与breakdown point分析）、**Assessment of Case Influence in the Lasso**（高维回归中的影响诊断与路径算法）。此外，**Block Vecchia Approximation** 和 **Personalized Tucker Decomposition** 在计算效率与算法收敛性方面对大规模统计计算有参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1080/00401706.2025.2460584](https://doi.org/10.1080/00401706.2025.2460584) — Noise Resistant Control Charts for Detecting Periodicity from Correlation
- **作者**: Yongxiang Li, Yunji Zhang, Qian Xiao, Jianguo Wu
- **期刊/来源**: Technometrics
- **机构**: Shanghai Jiao Tong University · Peking University
- **分类**: vol 67 · issue 3 · pp 451-463
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对高噪声环境下控制图检测周期性的问题，提出了一种基于时域的新型噪声鲁棒特征。传统谱控制图依赖周期图等谱特征，在强噪声下性能下降，且容易将相关但不具周期性的信号误判为周期信号，导致高假阳性率。作者基于该特征构造了两个稳健检验统计量，并建立了噪声鲁棒控制图。理论部分证明了所提特征具有吸引人的有限样本和渐近性质，并给出了高效的计算方法。模拟和案例研究表明，该方法在检测周期性和控制假阳性方面优于现有方法。对您而言，本文的假设检验框架和有限样本理论分析，与您在高维统计和假设检验方面的兴趣直接相关，其噪声鲁棒特征的设计思路也可能启发您在因果推断敏感性分析中处理测量误差问题。
- **关键技术**: `robust test statistics`, `finite-sample properties`, `asymptotic properties`, `time-domain feature`, `control charts`
- **为什么对您有用**: 本文属于假设检验方向，直接对应您的primary interest。其核心是设计噪声鲁棒的检验统计量并建立有限样本理论，这与您熟悉的非参数统计和minimax界技术高度契合。**中期可做**：若想将此类噪声鲁棒特征迁移到因果推断的敏感性分析中，需先在moderately_familiar的M-estimation理论上加强，以处理更复杂的识别函数。

## 统计计算 / 算法  *(stat_computing, 5 篇)*

### 1. [10.1080/00401706.2025.2475784](https://doi.org/10.1080/00401706.2025.2475784) · [arXiv](https://arxiv.org/abs/2410.04477) — Block Vecchia Approximation for Scalable and Efficient Gaussian Process Computations
- **作者**: Qilong Pan, Sameh Abdulah, Marc G. Genton, Ying Sun
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 546-558
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对大规模高斯过程（GP）计算中Vecchia近似效率低的问题，提出Block Vecchia方法。传统Vecchia将似然分解为一系列单变量条件分布，导致冗余计算和内存负担；Block Vecchia将观测分组为块，利用K-means聚类形成块，并基于GPU的变批量线性代数运算并行计算每个块的多变量条件分布，显著减少似然评估次数。在邻居选择准则上，发现随机排序在块数较大时能有效提升近似质量。数值实验和模拟验证了该方法相比精确GP的可扩展性和效率，并在百万点的高分辨率三维风速数据集上展示了实际效用。该方法本质上是计算加速技巧，未改变GP模型本身或引入新的统计推断理论。对您而言，这是一篇统计计算方向的实用方法论文，展示了如何将GPU并行和块化策略应用于经典空间统计模型，可作为您软件开发和算法优化兴趣的参考案例。
- **关键技术**: `Vecchia approximation`, `block conditional likelihood`, `K-means clustering`, `GPU batched linear algebra`, `random ordering for neighbor selection`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。方法本身是计算加速技巧，不涉及因果推断或高维理论，但您武器库中的'software development'和'high-dimensional asymptotics'可用于评估其计算复杂度与近似精度之间的权衡。**暂不可做**：核心机器不在武器库里——您缺少GPU编程和空间统计中Vecchia近似的领域知识，需先补充这些才能动手改进或复现。

### 2. [10.1080/00401706.2025.2475781](https://doi.org/10.1080/00401706.2025.2475781) · [arXiv](https://arxiv.org/abs/2403.03975) — Robust Covariance Estimation and Explainable Outlier Detection for Matrix-Valued Data
- **作者**: Marcus Mayrhofer, Una Radojičić, Peter Filzmoser
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 516-530
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对矩阵型数据（matrix-valued data）提出鲁棒协方差估计方法 MMCD（Matrix Minimum Covariance Determinant），目标是在矩阵变量椭圆分布类中一致估计均值矩阵以及行/列协方差矩阵。与将矩阵向量化后应用传统多元鲁棒估计（如 MCD）不同，MMCD 直接利用矩阵结构，避免了高维带来的维数灾难。方法的核心是寻找一个子集，其样本协方差矩阵的行列式最小，并基于该子集估计行/列协方差矩阵。作者证明了 MMCD 估计量具有矩阵仿射等变性（matrix affine equivariant），且其 breakdown point 高于向量化后任何仿射等变估计量的最大可达值。算法方面，提出了带收敛保证的迭代算法，并基于 MMCD 的稳健马氏距离进行异常值检测。进一步，将 Shapley 值分解扩展到矩阵设定，将平方马氏距离分解为行、列或单个单元格的贡献，实现可解释的异常值归因。模拟和真实数据表明，MMCD 在计算效率和鲁棒性上均优于基于向量化的方法。对您而言，该工作直接关联统计计算中的鲁棒估计与算法设计，其矩阵结构保持的思路可迁移到您熟悉的张量/高阶 U-统计量计算场景中，例如在 tensor contraction 中考虑鲁棒性。
- **关键技术**: `Minimum Covariance Determinant (MCD)`, `matrix affine equivariance`, `breakdown point`, `robust Mahalanobis distance`, `Shapley value decomposition`, `matrix-variate elliptical distribution`
- **为什么对您有用**: 本文属于统计计算方向，直接关联您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。其核心贡献——保持矩阵结构的鲁棒估计——与您 very_familiar 的“computation of higher-order U-statistics (treewidth / tensor contraction / einsum)”有潜在交叉：您可以用 tensor contraction 的视角分析 MMCD 算法的计算复杂度，或将其鲁棒性思想推广到高阶 U-统计量的计算中。中期可做：需先在 moderately_familiar 的“theory of higher-order U-statistics”上进一步熟悉，以将 MMCD 的 breakdown point 分析推广到张量设定。

### 3. [10.1080/00401706.2025.2477641](https://doi.org/10.1080/00401706.2025.2477641) · [arXiv](https://arxiv.org/abs/2406.00493) — Assessment of Case Influence in the Lasso with a Case-Weight Adjusted Solution Path
- **作者**: Zhenbang Jiao, Yoonkyung Lee
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 559-572
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究 Lasso 回归中单个观测删除对拟合值的影响，即 Cook's distance 的推广。由于 l1 惩罚导致 Lasso 系数无闭式解，直接计算 case-deleted 解需要重拟合模型，计算成本高。作者提出一种基于 case-weight 调整的路径方法：引入一个从 1 到 0 的权重参数，从全数据解出发生成一条解路径，并证明该路径在权重参数的简单函数下是分段线性的。当权重为 0 时，该路径对应的 Cook's distance 即为经典定义。进一步，作者引入 case influence graph 可视化每个数据点在不同惩罚参数下的影响变化，发现欠拟合与过拟合阶段的影响图呈现不同模式，可为模型选择提供额外信息。该方法避免了重拟合，显著降低了计算开销。对您而言，本文的 piecewise linear path 思路与您熟悉的 high-dimensional asymptotics 和软件工程背景高度契合，可直接用于开发 Lasso 诊断的 R 包或扩展至其他带惩罚的回归模型。
- **关键技术**: `case-weight adjusted solution path`, `piecewise linear path`, `Cook's distance for Lasso`, `case influence graph`, `model selection via influence patterns`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您的 primary interest 中的 statistical computing（数值方法与算法）。您非常熟悉的 high-dimensional asymptotics 和软件工程能力可直接用于复现或扩展该方法（如推广至 elastic net 或 group Lasso），属于**立即可做**的 follow-up。此外，case influence graph 的可视化思路对您开发诊断工具包有直接参考价值。

### 4. [10.1080/00401706.2025.2453206](https://doi.org/10.1080/00401706.2025.2453206) · [arXiv](https://arxiv.org/abs/2309.03439) — Personalized Tucker Decomposition: Modeling Commonality and Peculiarity on Tensor Data
- **作者**: Jiuyun Hu, Naichen Shi, Raed Al Kontar, Hao Yan
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 409-425
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出个性化 Tucker 分解（perTucker），旨在解决传统张量分解方法无法捕捉跨数据集异质性的问题。perTucker 将张量数据分解为共享的全局成分和个性化的局部成分，并引入模正交性假设以增强可识别性。算法方面，开发了带近端梯度的正则化块坐标下降法，并证明其收敛到稳定点。通过模拟研究和两个案例（太阳耀斑检测、吨位信号分类）展示了 perTucker 在异常检测、客户分类和聚类中的有效性。对您而言，该工作直接关联统计计算中的张量分解算法，且其“共享+个性化”的分解思路可迁移至高阶 U 统计量的计算成本建模（如用树宽刻画张量收缩复杂度）。
- **关键技术**: `Tucker decomposition`, `proximal gradient`, `block coordinate descent`, `mode orthogonality`, `personalized tensor decomposition`
- **为什么对您有用**: 本文属于统计计算（张量分解算法）方向，是您 primary interest 中的明确子领域。您武器库中 very_familiar 的“高阶 U 统计量的树宽/张量收缩计算”可直接用于分析 perTucker 的收缩成本（如评估全局与局部成分的树宽对算法复杂度的影响），属于**立即可做**的 follow-up。

### 5. [10.1080/00401706.2025.2453197](https://doi.org/10.1080/00401706.2025.2453197) · [arXiv](https://arxiv.org/abs/2307.08038) — Bivariate DeepKriging for Large-Scale Spatial Interpolation of Wind Fields
- **作者**: Pratik Nag, Ying Sun, Brian J Reich
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 397-408
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对双变量风场（二维速度分量）的大尺度空间插值问题，提出了一种名为 Bivariate DeepKriging 的新方法。该方法利用空间径向基函数构造嵌入层，构建空间依赖的深度神经网络（DNN），以替代传统协克里金（cokriging）方法。传统协克里金在处理非高斯、高空间变异性和异质性数据时表现不佳，且计算复杂度高，难以应用于大规模数据集。Bivariate DeepKriging 通过 DNN 实现了分布自由的预测，并基于自助法和集成 DNN 提供了不确定性量化。理论上，作者将所提方法与线性区域化模型（LMC）建立联系，奠定了理论基础。实验表明，该方法在预测性能上优于使用 LMC 和简约双变量 Matérn 协方差函数的传统协克里金，且计算速度提升约 20 倍。最后，作者将方法应用于中东地区 506,771 个位置的风场数据，展示了其卓越的预测性能和计算可扩展性。对于您而言，本文展示了如何将深度学习与空间统计结合，解决大规模、非高斯数据的计算瓶颈，其计算加速和不确定性量化思路对您在高维统计计算和软件开发方面的兴趣有直接参考价值。
- **关键技术**: `DeepKriging`, `spatial radial basis functions`, `bootstrap ensemble DNN`, `Linear Model of Coregionalization`, `distribution-free uncertainty quantification`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您对大规模空间插值计算方法的兴趣。您武器库中 'software development' 和 'high-dimensional asymptotics' 可用于复现或扩展其 DNN 架构与计算效率分析；'nonparametric statistics' 可用于评估其分布自由预测的理论性质。本文是统计计算与空间统计交叉的实用工作，值得作为入门阅读，但核心方法（DNN 嵌入层）不在您武器库的核心区，属于中期可做——需先在 'semiparametric theory' 上理解其与 LMC 的理论联系。

## 其他  *(other, 10 篇)*

### 1. [10.1080/00401706.2025.2467920](https://doi.org/10.1080/00401706.2025.2467920) — Clustering Spatial Data with a Mixture of Skewed Regression Models
- **作者**: Junho Lee, Michael P. B. Gallaugher, Amanda S. Hering
- **期刊/来源**: Technometrics
- **机构**: Louisiana State University · Baylor University
- **分类**: vol 67 · issue 3 · pp 505-515
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对大尺度空间域中单一回归模型不适用的问题，提出了一种基于偏态分布（skew-t 或正态逆高斯分布）的马尔可夫随机场混合回归模型。该模型通过有限混合回归对数据进行聚类，并为每个同质组分配一个回归模型，同时利用马尔可夫随机场捕捉空间依赖性。核心创新在于使用偏态分布处理误差项，从而避免因数据偏态或重尾导致过拟合（即选择过多的组分）。模型估计采用 EM 算法，并通过模拟研究和两个案例验证了估计量和模型选择的性能。该方法主要面向空间统计应用，而非因果推断或高维统计理论。
- **关键技术**: `Finite mixture of regressions`, `Markov random field`, `Skew-t distribution`, `Normal inverse Gaussian distribution`, `EM algorithm`
- **为什么对您有用**: 本文属于空间统计应用，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接方法学关联。武器库中的非参数统计或M估计理论可能用于分析其EM算法的收敛性，但核心问题（空间聚类与偏态建模）并非您当前的研究方向。暂不可做——缺乏空间统计和混合模型的专业知识。

### 2. [10.1080/00401706.2025.2460633](https://doi.org/10.1080/00401706.2025.2460633) — Partially Observable Online Nonparametric Monitoring of Spatiotemporally Correlated Data Streams
- **作者**: Di Wang, Andi Wang, Xiaochen Xian, Yongxiang Li
- **期刊/来源**: Technometrics
- **机构**: Shanghai Jiao Tong University · University of Wisconsin–Madison · Georgia Institute of Technology
- **分类**: vol 67 · issue 3 · pp 464-480
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究物联网传感器网络中部分可观测、时空相关数据流的在线非参数监控问题。目标是在传感器资源受限（每次仅采集部分数据）且时空相关结构复杂、难以用参数模型刻画时，实现实时异常检测。方法核心是：先用集成随机投影将高维原始数据降维为多个子数据流，再对每个子数据流构造去相关的秩统计量（decorrelated rank-based statistics），并结合数据增广策略处理部分观测。监控与采样决策基于所有子数据流的聚合局部统计量。理论分析证明了所提去相关秩统计量与采样策略的有效性。数值实验与案例（粮仓储粮温度监控、太阳耀斑检测）验证了方法在多种场景下的稳健性能。本文主要贡献在工程监控领域，与您的主要研究方向（因果推断、高维统计、半参理论等）直接交集有限。
- **关键技术**: `decorrelated rank-based statistics`, `ensemble random projections`, `data augmentation`, `online monitoring`, `distribution-free method`
- **为什么对您有用**: 本文属于统计过程监控（SPC）的应用方向，与您的主要兴趣（因果推断、高维RMT、半参效率理论等）无直接交集。方法上使用的去相关秩统计量、随机投影降维等工具不在您的技术武器库核心范围内。作为gateway reading价值不高，因为问题设定（在线监控、部分观测、时空相关）与您的统计推断框架差异较大。暂不可做——核心机器（在线监控的序贯决策理论、秩统计量的渐近理论）不在武器库里。

### 3. [10.1080/00401706.2025.2455143](https://doi.org/10.1080/00401706.2025.2455143) · [arXiv](https://arxiv.org/abs/2310.00551) — Derivative Based Global Sensitivity Analysis and Its Entropic Link
- **作者**: Jiannan Yang
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 440-450
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文在全局敏感性分析（GSA）框架下，针对方差基Sobol'指标在高度偏态或重尾分布下刻画不足的问题，提出一种基于导数的条件熵上界，作为熵基总效应指标的代理。核心方法利用导数信息构造上界，避免直接估计条件熵的困难，并通过对总效应熵取指数解决微分熵可能为负的问题。数值实验表明，该上界对单调函数紧致，在1000个随机函数测试中约四分之三情形下与熵基指标给出相同的输入变量排序。在具有八种不同分布输入的河流洪水物理模型中，新熵代理与方差基代理表现相似，且在输入为高斯、函数为线性时两者等价。本文主要贡献在于提供一种计算高效的熵基敏感性代理，扩展了导数基GSA的变量筛选能力，适用于更广泛的分布类型。对您而言，本文属于统计计算与不确定性量化方向，与您的主要兴趣（统计计算、非参数理论）有间接关联，但方法学新颖性有限，属于应用导向的改进。
- **关键技术**: `derivative-based global sensitivity analysis`, `Sobol' indices`, `conditional entropy upper bound`, `entropy-based total effect index`, `Monte Carlo estimation`
- **为什么对您有用**: 本文属于统计计算与不确定性量化领域，与您的主要兴趣（统计计算、非参数理论）有间接关联，但方法学核心是敏感性分析而非因果推断或高维统计。武器库中'非参数统计'和'软件工具'可用于复现或扩展其数值实验，但无直接可攻问题。作为gateway阅读，本文清晰阐述了GSA的问题设定和熵基方法的计算挑战，但方法学新颖性有限，属于应用导向的改进。建议作为背景了解，不优先深入。

### 4. [10.1080/00401706.2025.2475783](https://doi.org/10.1080/00401706.2025.2475783) · [arXiv](https://arxiv.org/abs/2303.16369) — A Spatially Correlated Competing Risks Time-to-Event Model for Supercomputer GPU Failure Data
- **作者**: Jie Min, Yili Hong, William Q. Meeker, George Ostrouchov
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 3 · pp 531-545
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对超级计算机 GPU 故障时间数据，建立了一个空间相关的竞争风险时间-事件模型。研究目标是分析 GPU 在机柜内的连接位置对两种主要故障类型的影响，同时考虑协变量和空间相关随机效应。模型将机柜的连接位置视为空间相关随机效应，将 GPU 在机柜内的位置作为协变量，采用贝叶斯框架进行统计推断。此外，还比较了通过期望最大化算法实现的极大似然估计方法。数据来自 Cray XK7 Titan 超级计算机中超过 30,000 个 GPU 的故障记录。结果揭示了 GPU 故障在 HPC 系统中的空间模式。对您而言，本文属于应用统计工作，展示了复杂数据结构（空间相关、竞争风险）下的建模与推断流程，但方法学新颖性有限，与您的主要研究方向（因果推断、高维统计、U-统计量等）无直接技术连接。
- **关键技术**: `spatially correlated random effects`, `competing risks model`, `Bayesian inference`, `expectation-maximization algorithm`, `Weibull distribution`
- **为什么对您有用**: 本文属于应用统计，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术连接。作为 gateway reading 价值有限：虽然数据规模大且结构复杂，但方法学上未涉及您武器库中的核心工具（如非参数统计、minimax 界、高阶 U-统计量）。暂不可做：核心机器（空间生存模型、贝叶斯推断）不在您的武器库中，且问题本身不指向您感兴趣的方法学前沿。

### 5. [10.1080/00401706.2025.2464004](https://doi.org/10.1080/00401706.2025.2464004) — Regression Recalibration by Learning PIT Map Values
- **作者**: Christopher Qian, Daniel Ries, Feng Liang, Jason Adams
- **期刊/来源**: Technometrics
- **机构**: University of Illinois Urbana-Champaign · Sandia National Laboratories
- **分类**: vol 67 · issue 3 · pp 481-492
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究回归模型中概率预测的校准问题，目标是在给定一个初始预测模型后，找到一个映射函数以提升其概率预测的校准性。作者基于概率积分变换（PIT）值，提出了一类广义的重新校准函数族，其中分位数重新校准是特例。在该函数族下，推导了最优映射的解析解，并提出了一个新颖的重新校准方法，在经验研究中在校准性和锐度两方面均优于分位数重新校准。方法通过一个案例研究得到验证：使用卷积神经网络预测皮纳图博火山喷发后的全球平流层温度，展示了该方法如何调整模型对喷发后气候的预测。本文属于方法学贡献，但更偏向预测校准这一统计学习子领域，与您的主要兴趣（因果推断、高维统计等）无直接技术交集。
- **关键技术**: `probability integral transform (PIT)`, `quantile recalibration`, `optimal mapping`, `calibration and sharpness`
- **为什么对您有用**: 本文属于统计预测校准的方法学工作，与您的主要兴趣方向（因果推断、高维统计、半参理论等）无直接技术关联。您的武器库中非参数统计和M估计理论可用于分析其最优映射的收敛性，但核心问题（校准而非因果识别）与您的研究主线距离较远。暂不可做——核心机器（预测校准理论）不在武器库中，且无明确连接点。

### 6. [10.1080/00401706.2025.2453207](https://doi.org/10.1080/00401706.2025.2453207) — Likelihood Inference for Possibly Nonstationary Processes via Adaptive Overdifferencing
- **作者**: Maryclare Griffin, Gennady Samorodnitsky, David S. Matteson
- **期刊/来源**: Technometrics
- **机构**: University of Massachusetts Amherst · Cornell University
- **分类**: vol 67 · issue 3 · pp 426-439
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对 ARFIMA 模型在非平稳情形下的似然推断问题，提出一种基于自适应过差分的精确似然方法。核心观察是：估计单个非平稳 ARFIMA 模型的参数等价于估计一系列平稳 ARFIMA 模型的参数，从而可以利用已有的平稳过程似然近似工具。该方法避免了传统方法在记忆参数 d 接近参数空间边界时表现不佳的问题，并允许上界 d̄ 超过 0.5。作者进一步引入自适应选择 d̄ 的程序，通过模拟展示当真实 d 高达 2.5 时，该方法仍能良好估计记忆参数。本文属于时间序列分析的方法学贡献，但未涉及因果推断、高维统计或半参效率等您的主要兴趣方向。
- **关键技术**: `ARFIMA model`, `exact likelihood inference`, `adaptive overdifferencing`, `nonstationary processes`, `memory parameter estimation`
- **为什么对您有用**: 本文与您的主要兴趣（因果推断、高维统计、半参理论等）无直接关联，属于时间序列分析领域的方法学工作。您的技术武器库（如非参统计、高维渐近、U-统计量）在此问题上的直接应用空间有限。作为 gateway-reading 价值较低，因为时间序列并非您的 secondary interest 方向。建议仅作泛读，无需深入。

### 7. [10.1080/00401706.2024.2413077](https://doi.org/10.1080/00401706.2024.2413077) — Experimental Design and Modeling for Forward-Inverse Maps
- **作者**: Russell R. Barton, Max D. Morris
- **期刊/来源**: Technometrics
- **机构**: Pennsylvania State University · Iowa State University
- **分类**: vol 67 · issue 3 · pp 367-381
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文提出在工程系统设计中，直接构建逆元模型（inverse metamodel）替代传统的正向模拟加优化迭代策略。核心设定是：给定性能目标，需要反推设计参数值；传统方法通过计算机模拟（正向模型）拟合回归或神经网络等近似元模型，再运行优化搜索。作者论证直接构建逆元模型可省去优化步骤，并设计同时拟合正向与逆元模型的实验方案。文章讨论了该策略与校准问题（calibration）的联系，以及实际应用需解决的关键问题（如模型可逆性、实验设计效率）。主要贡献是概念框架与问题阐述，而非具体的新方法或理论结果。对您而言，本文属于统计计算与实验设计的交叉领域，但方法学新颖性有限，且与您的主要兴趣（因果推断、高维统计、U-统计量）无直接技术连接。
- **关键技术**: `inverse metamodel`, `computer simulation experiments`, `design of experiments`, `calibration`
- **为什么对您有用**: 本文属于统计计算与实验设计的一般性讨论，与您的主要兴趣方向（因果推断、高维统计、U-统计量）无直接技术连接。武器库中的非参数统计或逆问题工具可泛泛理解其思路，但缺乏具体可攻口子。暂不可做——核心机器（实验设计优化、计算机模型校准）不在武器库中，且本文为概念性综述，不提供可迁移的数学框架。

### 8. [10.1080/00401706.2025.2467900](https://doi.org/10.1080/00401706.2025.2467900) — Optimal Planning of Destructive Degradation Tests
- **作者**: Jiaxiang Cai, William Q. Meeker, Zhi-Sheng Ye
- **期刊/来源**: Technometrics
- **机构**: National University of Singapore · Iowa State University
- **分类**: vol 67 · issue 3 · pp 493-504
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究破坏性退化试验的最优设计问题。在一般路径模型框架下，目标是最小化估计寿命分位数的渐近方差。作者推导了最优试验设计的闭式解，并明确了加速应力是否必要的条件——关键参数是寿命分位数和链接函数中加速变量的系数。通过胶粘剂和密封件两个实际案例验证了结果，并探讨了折中方案以增强稳健性。该工作属于可靠性工程的经典最优设计问题，方法上依赖渐近方差分析和闭式优化，不涉及因果推断、高维统计或半参效率理论等核心兴趣方向。对于您而言，本文与主要兴趣方向无直接关联，但可作为统计计算中优化设计的一个应用案例参考。
- **关键技术**: `optimal design`, `asymptotic variance`, `closed-form solution`, `general path model`, `destructive degradation test`
- **为什么对您有用**: 本文属于可靠性工程中的最优试验设计，与您的主要兴趣方向（因果推断、高维统计、半参理论等）无直接连接。技术武器库中的非参数统计或M估计理论可勉强用于理解其渐近方差推导，但核心问题设定和方法论差异较大。暂不可做——缺乏对退化过程建模和加速试验设计的背景知识。

### 9. [10.1080/00401706.2025.2491366](https://doi.org/10.1080/00401706.2025.2491366) — Thoughts on Forward-Inverse Maps
- **作者**: David M. Steinberg
- **期刊/来源**: Technometrics
- **机构**: Tel Aviv University
- **分类**: vol 67 · issue 3 · pp 382-383
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是Steinberg对Barton和Morris关于正向-逆向映射（Forward-Inverse Maps）论文的讨论稿，发表在Technometrics上。文章主要表达了对Barton和Morris工作的赞赏，认为其分析透彻、呈现清晰，具有启发性。作者预测该工作将在许多应用中证明其价值，并激发更多建设性研究。全文为简短的评论性质，未提出新的方法论或理论贡献。该文属于学术讨论范畴，不涉及具体统计方法或实证分析。对您而言，本文缺乏技术细节和实质性贡献，与您的主要研究兴趣（因果推断、高维统计、U统计量等）无直接关联。
- **为什么对您有用**: 本文为学术评论，无实质方法学内容，与您的主要研究兴趣（因果推断、高维统计、U统计量等）无直接关联，也不属于任何secondary interest领域。无需进一步阅读。

### 10. [10.1080/00401706.2025.2459106](https://doi.org/10.1080/00401706.2025.2459106) — Comment: A Model-Free Method for Input-Output Space-Filling Design
- **作者**: Shangkun Wang, V. Roshan Joseph
- **期刊/来源**: Technometrics
- **机构**: Georgia Institute of Technology
- **分类**: vol 67 · issue 3 · pp 384-387
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是对 Barton 和 Morris 关于逆设计（inverse design）实验设计框架的讨论性评论。评论提出了一种无模型（model-free）的输入-输出空间填充设计方法，旨在直接填充输入空间和输出空间，而不依赖于代理模型。该方法的核心思想是使用拉丁超立方体设计生成候选点，然后通过优化准则选择同时覆盖输入和输出空间的子集。评论通过一个简单示例展示了该方法与基于模型的方法的对比。本文属于讨论性短文，未提出新的统计理论或方法学突破。对您而言，本文与您的主要研究方向（因果推断、高维统计等）无直接关联，但如果您对实验设计或空间填充设计感兴趣，可作为入门了解。
- **关键技术**: `space-filling design`, `Latin hypercube design`, `inverse design`, `model-free design`
- **为什么对您有用**: 本文属于实验设计领域的讨论性评论，与您的主要兴趣（因果推断、高维统计、半参理论等）无直接关联。您的技术武器库中无直接可攻此文的工具。本文可作为实验设计方向的入门阅读，但非必要。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

