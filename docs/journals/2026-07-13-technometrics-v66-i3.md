# Technometrics — Vol 66  Issue 3  ·  2026-07-13

- 共 20 篇 · Technometrics
- 目录核对 ✅ 20 篇全部抓到（对照 OpenAlex 20 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Technometrics Vol 66 Issue 3 的 20 篇论文可归纳为三条主线：**假设检验与变点检测**（Moving Sum Procedure、两篇书评涉及核分布函数与大样本检验）、**高维与迁移学习**（Transfer Learning with Quantile Regression）、以及**统计计算与代理模型**（Gaussian Process Emulation、Mesh-Clustered GP、Bayesian Optimization via Exact Penalty、Adaptive Sampling）。此外，还有若干应用导向的方法开发（Partial Tail-Correlation Coefficient、Deep Latent Factor Model、Covariate-Dependent Clustering）和书评。整体上，本期在非参数推断、高维迁移学习和计算效率方面有实质性推进。

在假设检验与变点检测主线中，**Moving Sum Procedure under Piecewise Linearity** 将经典 MOSUM 方法从分段常数推广至分段线性信号，同时检测跳跃和斜率变化，在控制 FWER 下达到 minimax 最优率，且算法复杂度为 O(n)，允许序列相关和重尾分布。该工作填补了该设定下同时控制错误率和最优收敛速率的空白。**Transfer Learning with Large-Scale Quantile Regression** 则在高维分位数回归框架下，通过样本分裂检测信息源并构建迁移学习估计量，理论误差率由样本量、信噪比和模型相似度共同决定，在飞行安全数据上验证了有效性。这两篇分别从变点检测和高维迁移角度推进了统计推断的实用边界。

统计计算主线中，**Gaussian Process Emulation for High-Dimensional Coupled Systems** 提出并行部分链接 GP 代理模型（PPLE），通过共享相关结构捕捉子模型输出依赖，在保持计算效率的同时提升预测精度。**Mesh-Clustered Gaussian Process Emulator** 针对 PDE 边界值问题，用 Dirichlet 过程对网格节点聚类并拟合共享超参数的 GP，降低了计算负担并提供不确定性量化。**Bayesian Optimization via Exact Penalty** 将贝叶斯优化嵌入精确罚函数框架，用 GP 加权和建模复合罚函数，具有闭式采集函数和对初始设计鲁棒的特性。这三篇共同展示了 GP 代理模型在复杂系统仿真中的高效扩展。

与因果推断方向最贴的论文是 **Transfer Learning with Large-Scale Quantile Regression**（高维分位数回归的迁移学习框架，可类比因果迁移学习中的分布偏移问题）；与半参数效率方向相关的有 **Moving Sum Procedure under Piecewise Linearity**（其 minimax 率分析涉及非参数收敛速度）；与高维方向相关的还有 **Partial Tail-Correlation Coefficient**（极值依赖度量，可借助高维 graphical Lasso 学习网络结构）。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1080/00401706.2024.2315952](https://doi.org/10.1080/00401706.2024.2315952) · [arXiv](https://arxiv.org/abs/2212.06693) — Transfer Learning with Large-Scale Quantile Regression
- **作者**: Jun Jin, Jun Yan, Robert H. Aseltine, Kun Chen
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 381-393
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究高维分位数回归的迁移学习问题。目标是在目标人群数据有限时，利用多个可能相关的源人群数据来提升条件分位数的估计和推断。方法的核心是两步法：首先基于样本分裂检测与目标模型相似的“信息源”，然后利用这些信息源构建迁移学习估计量。检测步骤通过比较源与目标模型在稀疏假设下的参数差异实现一致性。理论分析表明，在合理的信号噪声比和源-目标相似度条件下，迁移学习估计量的误差率远低于仅使用目标数据的朴素估计量，且误差率由样本量、信噪比和模型相似度共同决定。模拟实验和飞行安全数据（波音737、空客A320、A380）的应用验证了方法的有效性。对您而言，本文的高维分位数回归迁移学习框架与您在高维统计和因果推断中的迁移学习兴趣直接相关，其基于样本分裂的源检测策略和误差率分析思路可迁移至因果推断中的异质性处理效应迁移问题。
- **关键技术**: `transfer learning`, `high-dimensional quantile regression`, `sample splitting for source detection`, `informative source detection`, `error rate analysis under similarity measures`
- **为什么对您有用**: 本文直接连接到您的高维统计兴趣子方向——高维分位数回归的迁移学习。您武器库中`high-dimensional asymptotics`和`minimax bounds for estimation problems`两项非常熟悉的技术可直接用于验证本文误差率上界的紧性，并探索更优的源检测阈值。中期可做：若将本文的源检测策略迁移至因果推断中的异质性处理效应迁移，需先在`identification theory in causal inference`上长肌肉（当前为moderately_familiar），以处理处理效应识别中的未观测混杂。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1080/00401706.2024.2374184](https://doi.org/10.1080/00401706.2024.2374184) — Statistical Inference Based on Kernel Distribution Function EstimatorsStatistical Inference Based on Kernel Distribution Function Estimators, Rizky Reza Fauzi and Yoshihiko Maesono, Singapore: Springer Nature Singapore Pte Ltd, 2023, 103 pp., $39.99, ISBN 9789819918621.
- **作者**: Sukardi, Puji Lestari
- **期刊/来源**: Technometrics
- **机构**: Bandung Institute of Technology
- **分类**: vol 66 · issue 3 · pp 485-487
- 相关性 7/10 · novelty: `survey`
- **摘要**: 本文是对《基于核分布函数估计的统计推断》一书的书评。该书系统介绍了核分布函数估计（KDFE）的理论与方法，涵盖了一维与多维设定下的分布估计、光滑分位数估计以及基于KDFE的拟合优度检验。核心内容包括核估计的偏差-方差权衡、带宽选择（如交叉验证、plug-in方法）以及渐近正态性等理论性质。在假设检验方面，书中讨论了基于KDFE的Kolmogorov-Smirnov型检验和Cramér-von Mises型检验，并给出了检验统计量的渐近分布。书评指出该书适合作为研究生教材或参考书，但缺乏实际应用案例和软件实现。对于您而言，该书评本身是二手信息，但原书涉及的核分布估计与拟合优度检验是您非参数统计和假设检验兴趣的基础工具，不过其内容较为经典，方法学新颖性有限。
- **关键技术**: `kernel distribution function estimator`, `bandwidth selection`, `goodness-of-fit test`, `Kolmogorov-Smirnov test`, `Cramér-von Mises test`, `smooth quantile estimation`
- **为什么对您有用**: 本文是书评，非原创研究。原书主题与您的非参数统计和假设检验兴趣直接相关，但内容属于经典教科书级别，不涉及前沿方法。您的武器库中的非参数统计和minimax界知识已远超该书范围，因此不值得花时间读全文。

### 2. [10.1080/00401706.2024.2374182](https://doi.org/10.1080/00401706.2024.2374182) — A Course in the Large Sample Theory of Statistical InferenceA Course in the Large Sample Theory of Statistical Inference, W. J. Hall and D. Oakes, Boca Raton, FL: Chapman and Hall, CRC Press, 2024, x + 310 pp., $115.00, ISBN 978-0429160080.
- **作者**: David J. Olive
- **期刊/来源**: Technometrics
- **机构**: Southern Illinois University Carbondale
- **分类**: vol 66 · issue 3 · pp 483-484
- 相关性 6/10 · novelty: `survey`
- **摘要**: 本文是对 Hall 与 Oakes 所著《大样本统计推断理论》一书的书评。该书覆盖了 Serfling (1980) 水平的大样本理论，包括随机变量、随机向量、极限分布、Delta 方法、U-统计量、M-估计、似然比检验等经典主题。书评指出该书适合作为研究生教材，内容组织清晰，习题丰富。对于您而言，这是一本经典大样本理论的教材，可作为教学参考或复习大样本基础的工具，尤其与您对数学统计与假设检验的兴趣直接相关。
- **关键技术**: `large sample theory`, `U-statistics`, `M-estimation`, `likelihood ratio tests`, `Delta method`
- **为什么对您有用**: 本文是教材书评，直接关联您对数学统计与假设检验的兴趣。该书覆盖的大样本理论是您非常熟悉的领域，可作为教学或快速查阅的参考。属于 gateway-reading 范畴，值得花时间浏览全书目录和关键章节。

### 3. [10.1080/00401706.2024.2308202](https://doi.org/10.1080/00401706.2024.2308202) · [arXiv](https://arxiv.org/abs/2208.04900) — Moving Sum Procedure for Change Point Detection under Piecewise Linearity
- **作者**: Joonpyo Kim, Hee-Seok Oh, Haeran Cho
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 358-367
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对分段线性信号下的多变点检测问题，提出了一种基于移动和（MOSUM）的统计推断方法。该方法能够同时检测信号中的不连续跳跃和斜率变化，并在控制族系错误率（FWER）的同时实现变点个数和位置的一致性估计。在信号为分段线性且连续的情形下，估计量达到了极小化最优收敛速率。方法仅需 O(n) 计算复杂度，且允许序列相关和重尾分布等弱假设，显著优于现有基于惩罚或贝叶斯的方法。模拟实验验证了其有限样本性能，并在滚动轴承退化预测的真实数据上展示了应用价值。该工作将经典 MOSUM 从分段常数推广至分段线性，填补了该设定下同时控制 FWER 和达到 minimax 率的空白。对您而言，其 O(n) 算法和弱假设下的理论保证可直接迁移至您在高维时间序列或因果推断中纵向数据的变点检测问题。
- **关键技术**: `MOSUM (moving sum) procedure`, `multiple change point detection`, `piecewise linear signal`, `family-wise error rate control`, `minimax optimal estimation rate`, `O(n) computational complexity`
- **为什么对您有用**: 本文属于假设检验与变点检测方向，直接连接您的 primary interest 中的 hypothesis testing 和 longitudinal causal inference。其 MOSUM 方法在弱假设下达到 minimax 率且计算复杂度为 O(n)，您可以用 very_familiar 的高维渐近理论验证其 rate 的紧性，并考虑将其推广至因果推断中的结构变点检测（如 treatment effect 的时变）。中期可做：若需处理更复杂的依赖结构（如长期记忆），需先在 moderately_familiar 的 M-estimation 理论上加强。

## 统计计算 / 算法  *(stat_computing, 5 篇)*

### 1. [10.1080/00401706.2024.2322645](https://doi.org/10.1080/00401706.2024.2322645) — An Adaptive Sampling Strategy for Real-Time Anomaly Detection with Unmanned Sensing Vehicles
- **作者**: Yue Jiang, Ana María Estrada Gómez
- **期刊/来源**: Technometrics
- **机构**: Purdue University West Lafayette
- **分类**: vol 66 · issue 3 · pp 438-454
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对无人传感车辆（USV）实时异常检测中的自适应采样问题，提出了一种结合时空张量分解与采样策略的框架。目标是在监测空间中动态决定USV的部署位置，以最大化变化检测能力并控制部署成本。方法核心包括：首先，提出一种新的时空序贯张量分解算法，将高维数据分解为空间、时间和稀疏（异常）三个分量；稀疏分量用于定位可疑变化区域。然后，利用空间和时间分量进行一步预测，指导自适应采样策略。采样策略通过设计采样分布函数来平衡探索与利用，并利用Voronoi图控制USV的运动轨迹。仿真与案例研究验证了框架的有效性。对您而言，本文的张量分解与序贯决策框架可视为统计计算中“算法与数值方法”的一个应用实例，但其方法学新颖性有限，主要贡献在于工程应用层面的系统集成。
- **关键技术**: `tensor decomposition`, `spatio-temporal modeling`, `adaptive sampling`, `Voronoi tessellation`, `sequential decision`
- **为什么对您有用**: 本文属于统计计算的应用方向，与您的primary interest中的“statistical computing (numerical methods, algorithm)”有直接关联。但方法学上，张量分解和自适应采样是成熟技术，本文的创新在于工程集成而非理论突破。从武器库角度看，您对“software development”和“high-dimensional asymptotics”的熟悉程度足以理解本文的算法流程，但核心的序贯决策与探索-利用平衡问题并不在您的核心武器库中（如bandit理论、强化学习），因此属于**暂不可做**的范畴——除非您有意向将统计计算拓展到序贯决策领域。作为gateway reading，本文适合快速浏览以了解USV异常检测的应用场景，但不必深入研读。

### 2. [10.1080/00401706.2024.2322651](https://doi.org/10.1080/00401706.2024.2322651) — Gaussian Process Emulation for High-Dimensional Coupled Systems
- **作者**: Tamara Dolski, Elaine T. Spiller, Susan E. Minkoff
- **期刊/来源**: Technometrics
- **机构**: The University of Texas at Dallas · Marquette University
- **分类**: vol 66 · issue 3 · pp 455-469
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对复杂耦合多物理场仿真中计算成本高昂的问题，提出了一种新的高斯过程（GP）代理模型——并行部分链接GP代理模型（PPLE）。PPLE结合了共享相关结构（parallel partial emulator）的高效性与链接代理模型（linked emulator）对耦合物理过程的准确性，用于近似具有向量值输出的复合函数。方法的核心机制是：对每个物理子模型分别构建GP代理，并通过一个共享的相关结构来捕捉子模型输出之间的依赖关系，从而在保持计算效率的同时提高整体预测精度。与直接对复合函数输出进行GP代理建模相比，PPLE在两个数值实验中均表现出更小的平均预测误差和预测方差。该工作为高维耦合系统的不确定性量化提供了一种实用的统计计算工具。对您而言，本文属于统计计算（statistical computing）方向的应用型工作，展示了GP代理模型在复杂仿真中的设计思路，可作为您软件开发和数值方法兴趣的参考案例。
- **关键技术**: `Gaussian process emulator`, `parallel partial emulator`, `linked emulation`, `vector-valued output`, `uncertainty quantification`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。您武器库中的'software development'技能可直接用于复现或扩展PPLE方法。本文是gateway-reading范畴：它清晰介绍了GP代理模型在耦合系统中的应用，适合作为入门读物；但方法本身不涉及您核心的因果推断或高维统计理论，属于中期可做——若想深入，需先在moderately_familiar的'M-estimation theory'上加强以理解GP的估计性质。

### 3. [10.1080/00401706.2024.2320211](https://doi.org/10.1080/00401706.2024.2320211) · [arXiv](https://arxiv.org/abs/2301.10387) — Mesh-Clustered Gaussian Process Emulator for Partial Differential Equation Boundary Value Problems
- **作者**: Chih-Li Sung, Wenjia Wang, Liang Ding, Xingjian Wang
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 406-421
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对偏微分方程（PDE）边界值问题，提出一种基于网格聚类的高斯过程（GP）仿真器，用于高效预测整个空间域上的解。传统数值求解PDE（如有限元法）计算成本高，限制了参数探索；本文创新地将网格节点坐标纳入统计模型，通过Dirichlet过程先验将网格节点分割为多个聚类，并在每个聚类内拟合共享超参数的GP模型。该方法不仅降低了计算负担，还提供了不确定性量化的理论保证。通过揭示聚类结构，可识别具有物理意义的网格节点分组（如满足边界条件的节点），为后续分析提供定性洞察。在真实案例中，该方法在预测误差上优于主要竞争对手，且计算时间具有竞争力。文中还提供了开源的R包。对您而言，本文展示了统计计算中仿真器设计与不确定性量化的实用范例，与您的统计计算（数值方法、算法）兴趣直接相关，可作为入门级阅读材料。
- **关键技术**: `Gaussian process emulator`, `Dirichlet process clustering`, `finite element method`, `uncertainty quantification`, `mesh-based PDE solver`
- **为什么对您有用**: 本文属于统计计算（仿真器设计）的应用型工作，与您的primary interest“statistical computing”直接相关。您的武器库中“nonparametric statistics”和“software development”可轻松理解其GP建模与R包实现；但核心的网格聚类与PDE数值求解并非您的熟悉领域，属于“暂不可做”——缺少有限元方法和物理仿真背景。不过，作为gateway reading，本文清晰展示了统计模型如何与计算科学结合，值得花时间读全文以拓宽视野。

### 4. [10.1080/00401706.2024.2315937](https://doi.org/10.1080/00401706.2024.2315937) — Bayesian Optimization via Exact Penalty
- **作者**: Jiangyan Zhao, Jin Xu
- **期刊/来源**: Technometrics
- **机构**: East China Normal University
- **分类**: vol 66 · issue 3 · pp 368-380
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对目标函数和约束均为非凸且评估代价高昂的黑箱仿真问题，提出了一种混合优化方法——精确罚贝叶斯优化（EPBO）。该方法将贝叶斯优化嵌入精确罚函数框架，用高斯过程的加权和建模复合罚函数，并通过预测均值平滑约束违反的定性分量。EPBO 具有闭式采集函数、对初始设计鲁棒、可从不可行点启动以及有效处理等式约束等特性。在基准合成测试问题和两个实际工程设计问题上的实验表明，EPBO 优于当前最先进的竞争方法。对您而言，本文展示了统计代理模型（高斯过程）与数值优化（精确罚函数）的巧妙结合，其闭式采集函数的设计思路可迁移至您熟悉的因果推断或高维统计中的计算问题，例如在 proximal causal inference 中优化复杂目标函数。
- **关键技术**: `Bayesian optimization`, `Gaussian process surrogate`, `exact penalty function`, `closed-form acquisition function`, `constrained black-box optimization`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 'statistical computing (numerical methods, algorithm)'。您武器库中 'software development' 和 'nonparametric statistics' 的功底可帮助您快速理解并复现其高斯过程建模与采集函数优化流程。中期可做：若您希望将此类贝叶斯优化方法应用于因果推断中的超参数调优或实验设计，需先在 'M-estimation theory' 上加强，以理解优化目标的理论性质。

### 5. [10.1080/00401706.2024.2374183](https://doi.org/10.1080/00401706.2024.2374183) — Applied Machine Learning Using mlr3 in RApplied Machine Learning Using mlr3 in R, Edited by Bernd Bischl, Raphael Sonabend, Lars Kotthoff, and Michel Lang, Boca Raton, FL: CRC Press, Taylor &amp; Francis Group, Chapman and Hall, 2024, xvii + 339 pp., $ 79.95 (pbk), ISBN 978-1-032-50754-5.
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 484-485
- 相关性 2/10 · novelty: `survey`
- **摘要**: 这是一本关于 mlr3 框架在 R 中实现机器学习工作流的书籍的书评。mlr3 是 mlr 包的下一代版本，提供了统一的接口和模块化设计，支持数据预处理、模型训练、超参数调优、重采样和基准测试等完整流程。该书评指出，mlr3 的设计强调可扩展性和可重复性，适合从初学者到专家的不同用户群体。书中涵盖了监督学习、无监督学习、特征工程、模型解释等主题，并提供了大量代码示例。书评认为该书是 R 用户进行机器学习实践的实用指南，尤其适合需要系统化工作流的统计学家和数据科学家。对于您而言，这本书是了解 mlr3 生态系统的入门读物，但作为一本应用导向的书籍，其方法学新颖性有限。
- **关键技术**: `mlr3 framework`, `R package ecosystem`, `machine learning pipeline`, `hyperparameter tuning`, `resampling`, `benchmarking`
- **为什么对您有用**: 本文属于统计计算（stat_computing）范畴，是 mlr3 框架的入门读物。您对统计计算和软件开发有兴趣，mlr3 的模块化设计和工作流管理理念可迁移到您自己的软件项目（如因果推断或 U-统计量的 R 包开发）。不过，本文是书评而非技术论文，方法学深度有限，属于 gateway-reading 性质——值得花时间浏览以了解 mlr3 的架构，但无需深入精读。

## 其他  *(other, 11 篇)*

### 1. [10.1080/00401706.2024.2304334](https://doi.org/10.1080/00401706.2024.2304334) · [arXiv](https://arxiv.org/abs/2210.07351) — Partial Tail-Correlation Coefficient Applied to Extremal-Network Learning
- **作者**: Yan Gong, Peng Zhong, Thomas Opitz, Raphaël Huser
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 331-346
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的极值依赖度量——偏尾相关系数（PTCC），其构造基于多元正则变差框架和变换线性代数运算，类似于经典多元分析中的偏相关系数。PTCC 能在给定其他变量的条件下识别出具有部分不相关尾部的变量对，且所需建模假设极少，适用于极值图模型的探索性结构学习。与传统极值条件独立性框架不同，PTCC 可借助高维数据的经典推断方法（如带拉普拉斯谱约束的 graphical Lasso）高效学习极值网络结构。作者将 PTCC 应用于极端河流流量和全球历史货币汇率两个数据集，提取出具有领域特定解释意义的极端风险网络结构。本文方法学贡献在于将偏相关思想推广到极值领域，但整体属于应用导向的方法开发，理论深度有限。
- **关键技术**: `partial tail-correlation coefficient`, `multivariate regular variation`, `graphical Lasso`, `extremal graphical models`, `transformed-linear algebra`
- **为什么对您有用**: 本文属于极值统计与网络学习的交叉，与您的 primary interests 无直接重叠。但作为 astrostatistics 的 gateway reading 候选，它清晰展示了如何将经典统计概念（偏相关）推广到非标准设定（极值尾部），并提供了完整的数据分析流程（从度量定义到网络学习再到实际数据应用），适合作为了解极值图模型方法的入门读物。您的武器库中 nonparametric statistics 和 high-dimensional asymptotics 足以支撑理解本文核心方法，但极值理论（regular variation 框架）并非您熟悉领域，需额外投入时间学习，因此暂不可做。

### 2. [10.1080/00401706.2024.2322661](https://doi.org/10.1080/00401706.2024.2322661) — Deep Latent Factor Model for Spatio-Temporal Forecasting
- **作者**: Wonmo Koo, Eun-Yeol Ma, Heeyoung Kim
- **期刊/来源**: Technometrics
- **机构**: Korea Advanced Institute of Science and Technology
- **分类**: vol 66 · issue 3 · pp 470-482
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种深度潜因子模型用于时空预测。模型将观测数据分解为潜因子与因子载荷的乘积，其中潜因子通过循环神经网络（RNN）建模时间依赖，因子载荷通过基于距离的高斯过程（GP）建模空间依赖。与经典潜因子模型假设线性向量自回归不同，该模型利用深度神经网络的表达能力捕捉复杂的非线性时空依赖。模型通过 beta-Bernoulli 过程自动推断潜因子数量，避免了手动选择。推导了随机变分推断算法以实现可扩展推断。在模拟和真实数据上验证了预测性能。对您而言，本文属于应用导向的方法学工作，与您的主要兴趣（因果推断、高维统计）无直接交集，但时空建模中的潜因子结构可能与您熟悉的张量分解或高阶 U-统计量有间接联系。
- **关键技术**: `deep latent factor model`, `recurrent neural network`, `Gaussian process`, `beta-Bernoulli process`, `stochastic variational inference`
- **为什么对您有用**: 本文属于统计计算与时空建模的应用方法，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。武器库中 'nonparametric statistics' 和 'high-dimensional asymptotics' 可帮助理解其 GP 与变分推断的理论性质，但核心问题（时空预测）并非您的研究方向。暂不可做——缺乏时空因果推断或张量分解的直接连接点。

### 3. [10.1080/00401706.2024.2321930](https://doi.org/10.1080/00401706.2024.2321930) — Covariate-Dependent Clustering of Undirected Networks with Brain-Imaging Data
- **作者**: Sharmistha Guha, Rajarshi Guhaniyogi
- **期刊/来源**: Technometrics
- **机构**: Texas A&M University
- **分类**: vol 66 · issue 3 · pp 422-437
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对无向网络响应变量与标量协变量之间的聚类问题，提出一种非参数贝叶斯混合模型框架。模型假设不同子群中网络与协变量的关系存在差异，并旨在识别每个子群内与协变量显著相关的网络节点。方法采用对称矩阵系数建模，并引入低秩结构与组稀疏性，以增强模型简洁性与计算效率，同时支持节点层面的推断。作为贝叶斯方法，模型可自动确定聚类数，提供聚类不确定性度量（共聚类矩阵），并刻画节点显著性的不确定性。模拟实验表明该方法在推断性能上优于现有竞争者；在真实脑连接组数据中，识别出与创造性成就显著相关的脑区。补充材料提供了后验预测密度的收敛率证明及MCMC算法细节。
- **关键技术**: `nonparametric Bayesian mixture model`, `low-rank matrix decomposition`, `group sparsity`, `Markov chain Monte Carlo (MCMC)`, `co-clustering matrix`
- **为什么对您有用**: 本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计等）无直接交集。其核心方法（贝叶斯混合模型、低秩分解）不在您的技术武器库中，且问题设定（网络聚类）与您的方向距离较远。作为gateway reading价值有限，因为需要大量背景知识且不涉及您熟悉的统计推断框架。建议仅作泛读，不投入深度阅读。

### 4. [10.1080/00401706.2024.2319138](https://doi.org/10.1080/00401706.2024.2319138) · [arXiv](https://arxiv.org/abs/2109.02726) — Screening the Discrepancy Function of a Computer Model
- **作者**: Pierre Barbillon, Anabel Forte, Rui Paulo
- **期刊/来源**: Technometrics
- **机构**: AgroParisTech · Universitat de València · University of Lisbon
- **分类**: vol 66 · issue 3 · pp 394-405
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对计算机模型与现场观测数据之间的 discrepancy 函数（模型偏差）进行变量筛选，而非传统意义上的计算机模型输入筛选。目标是在贝叶斯框架下识别哪些输入变量在 discrepancy 函数中是活跃的，从而告知建模者模型可能错误处理了哪些输入方向，以及哪些方向不适合用于预测。方法受贝叶斯变量选择中连续 spike-and-slab 先验启发，提出 PIPS（后验包含概率筛选）方法。核心创新在于：只需从完整模型进行一次 MCMC 采样，即可计算所有竞争模型的后验概率，计算效率远高于传统方法。后验包含概率作为筛选活跃输入的可解释指标。该方法在模拟和实际案例中展示了良好的筛选性能。对您而言，本文属于统计计算与贝叶斯方法在计算机实验设计中的应用，与您的主要兴趣（因果推断、高维统计）无直接交集，但 MCMC 计算策略和变量筛选思路在您的统计计算兴趣中可能有参考价值。
- **关键技术**: `Bayesian variable selection`, `spike-and-slab prior`, `MCMC`, `posterior inclusion probability`, `computer model calibration`, `discrepancy function`
- **为什么对您有用**: 本文属于计算机实验与贝叶斯筛选的应用，与您的主要兴趣方向（因果推断、高维统计、效率理论）无直接交集。作为 gateway reading 来看，它并非 astrostatistics / econ / epi 领域的入门读物，而是统计计算在工程建模中的应用。您的武器库中 very_familiar 的软件开发和 moderately_familiar 的 M-estimation 理论无法直接攻入本文核心（贝叶斯 MCMC 与 spike-and-slab 先验设计）。暂不可做——缺少贝叶斯计算与计算机模型校准的领域知识。

### 5. [10.1080/00401706.2024.2304341](https://doi.org/10.1080/00401706.2024.2304341) — Discrepancy Measures for Global Sensitivity Analysis
- **作者**: Arnald Puy, Pamphile T. Roy, Andrea Saltelli
- **期刊/来源**: Technometrics
- **机构**: University of Birmingham · Universitat Pompeu Fabra · Barcelona School of Economics
- **分类**: vol 66 · issue 3 · pp 347-357
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出基于 discrepancy 的全局敏感性分析方法，目标是降低敏感性分析的技术门槛，使其像散点图目视检查一样直观。核心思想是用 discrepancy 度量（如 L2-discrepancy、star discrepancy）衡量输入参数对输出分布的影响，替代传统的基于方差的 Sobol' 总效应指数。作者比较了多种 discrepancy 算法，发现某些度量（如 L2-discrepancy）在排序参数重要性方面与总效应指数几乎同样准确。进一步，他们引入了一种“替代 discrepancy”（ersatz-discrepancy），其性能与最佳 discrepancy 算法相当，但实现更简单、解释更直观，且计算速度快数个数量级。该方法适用于任何可生成输入-输出样本的模型，无需假设模型结构或分布形式。实证部分通过多个数值算例验证了其排序准确性和计算效率。对您而言，本文属于统计计算与敏感性分析的交叉，但方法学新颖性有限（主要是工程简化），且与您的主要兴趣（因果推断、高维统计、U-统计量）无直接技术连接，仅可作为敏感性分析领域的入门参考。
- **关键技术**: `discrepancy measures`, `L2-discrepancy`, `star discrepancy`, `Sobol' total sensitivity index`, `ersatz-discrepancy`
- **为什么对您有用**: 本文属于敏感性分析的应用方法，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接技术连接。武器库中无直接对口工具，且方法学新颖性有限（主要是工程简化）。暂不可做——核心机器不在武器库里（缺乏敏感性分析领域的专门工具）。

### 6. [10.1080/00401706.2024.2374187](https://doi.org/10.1080/00401706.2024.2374187) — Computational and Analytic Methods in Biological Sciences, 1st ed. <b>Computational and Analytic Methods in Biological Sciences, 1st ed.</b> , Edited by Akshara Makrariya, Brajesh Kumar Jha, Rabia Musheer, Anant Kant Shukla, Amrita Jha, Parvaiz Ahmad Naik, Denmark, FL: River Publishers Series in Biomedical Engineering, 2023, 324 pp., £99.99, ISBN: 9788770226950.
- **作者**: Manap Trianto
- **期刊/来源**: Technometrics
- **机构**: Universitas Gadjah Mada
- **分类**: vol 66 · issue 3 · pp 489-490
- 相关性 2/10 · novelty: `survey`
- **摘要**: 这是一篇书评，评述了《Computational and Analytic Methods in Biological Sciences》一书。该书涵盖生物医学工程、生物物理学、生物信息学等主题，并探讨了用于癌症分类与预测的概率计算学习模型。书评本身并未提出新的统计方法或理论结果。该书内容广泛但深度有限，适合作为入门参考。对您而言，该书评不涉及您核心研究方向的具体技术细节，仅作为跨领域信息参考。
- **为什么对您有用**: 本文为书评，不涉及具体统计方法或理论。与您的主要研究方向（因果推断、高维统计、U统计量等）无直接关联。不推荐深入阅读。

### 7. [10.1080/00401706.2024.2374186](https://doi.org/10.1080/00401706.2024.2374186) — Statistical Modeling of Occupant Behavior <b>Statistical Modeling of Occupant Behavior</b> , JanKloppenborg Møller, Marcel Schweiker, Rune Korsholm Andersen, Burak Gunay, Selin Yilmaz, Verena MarieBarthelmes, and Henrik Madsen, Boca Raton, FL: CRC Press, Taylor &amp; Francis Group, Chapman and Hall, 2024, xv + 366 pp., 35 b/w illustrations, $ 160.00 (hbk), ISBN 978-1-032-33460-8.
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 487-488
- 相关性 2/10 · novelty: `survey`
- **摘要**: 本文是对《Statistical Modeling of Occupant Behavior》一书的书评，该书由多位国际学者合著，专注于室内环境、能源使用及与舒适度相关的 occupant behavior 的统计建模。书评概述了全书结构，包括基础统计方法、数据收集、模型选择、验证及实际应用等章节。该书旨在为建筑科学、能源工程等领域的研究者和从业者提供统计建模的实用指南。书评指出，该书内容全面，涵盖了从经典回归到机器学习等多种建模技术。对于统计学家而言，该书提供了一个将统计方法应用于建筑环境与人类行为交叉领域的应用案例。然而，该书评本身并未提出新的统计理论或方法，主要价值在于介绍该领域的一本综合性参考书。
- **关键技术**: `statistical modeling`, `occupant behavior`, `building science`, `energy efficiency`
- **为什么对您有用**: 本文是一篇书评，属于应用领域的介绍性材料，而非原创研究。它连接了 secondary interest 中的 epidemiology（人类行为与健康环境）和 econ_theory（能源经济）的应用场景，但缺乏具体的方法学细节。对于研究者而言，若对建筑环境中的统计建模感兴趣，可作为入门读物，但武器库中的工具（如非参数统计、因果推断）在此书评中无直接应用点。暂不可做：核心内容为领域综述，不涉及可攻击的具体技术问题。

### 8. [10.1080/00401706.2024.2374188](https://doi.org/10.1080/00401706.2024.2374188) — Molecular Networking Statistical Mechanics in the Age of AI and Machine Learning <b>Molecular Networking Statistical Mechanics in the Age of AI and Machine Learning</b> , Edited by Caroline Desgranges and Jerome Delhommelle, Boca Raton, CRC Press, 2024, 248 pp., £ 110.00, ISBN 9780367438937.
- **作者**: Zulfaidil, La Ode Muhamad Iqbal, Riani Utami, Sri Redjeki Pudjaprasetya, Warsoma Djohan
- **期刊/来源**: Technometrics
- **机构**: Bandung Institute of Technology · Universitas Gadjah Mada
- **分类**: vol 66 · issue 3 · pp 490-491
- 相关性 2/10 · novelty: `survey`
- **摘要**: 本文是对《Molecular Networking Statistical Mechanics in the Age of AI and Machine Learning》一书的书评，该书旨在为统计力学提供现代视角，整合AI和机器学习方法。书评指出，该书涵盖了分子模拟、网络理论和机器学习在统计力学中的应用，但内容较为宽泛。核心贡献是作为入门读物，介绍了AI/ML如何加速分子动力学模拟和材料性质预测。然而，书评本身并未提出新的统计方法或理论。对您而言，该书评与您的主要研究方向（因果推断、高维统计、U统计量等）无直接关联，且缺乏具体的技术细节和可迁移的方法论。
- **关键技术**: `molecular dynamics simulation`, `machine learning`, `network theory`
- **为什么对您有用**: 本文是书评，属于gateway-reading范畴，但主题为分子统计力学，与您的primary interests（因果推断、高维统计、U统计量等）无直接连接。武器库中的工具（如非参数统计、高维渐近）无法直接应用于该领域。因此，本文不值得花时间阅读全文。

### 9. [10.1080/00401706.2023.2296465](https://doi.org/10.1080/00401706.2023.2296465) — Assessing Measurement System Agreement in the Presence of Reproducibility and Repeatability
- **作者**: Adel Ahmadi Nadi, Stefan H. Steiner, Nathaniel T. Stevens
- **期刊/来源**: Technometrics
- **机构**: University of Waterloo
- **分类**: vol 66 · issue 3 · pp 319-330
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文在测量系统一致性评估中，将概率一致性（PoA）指标从仅考虑重复性（repeatability）扩展到同时包含再现性（reproducibility）和相对偏倚。设定为两个测量系统（旧系统与新系统）在多个操作者下的比较，操作者效应可视为固定或随机，且允许各系统/操作者下的重复测量数不平衡。方法核心是使用极大似然估计（MLE）估计PoA，并给出其标准误和置信区间。技术工具包括正态混合模型、Fisher信息矩阵和delta方法。通过两个案例（工业质检和呼吸率测量）展示方法的应用。本文属于应用统计方法论文，方法学创新有限（主要是现有PoA框架的扩展），但提供了完整的估计和推断程序。对您而言，本文与您的主要兴趣方向（因果推断、高维统计等）无直接关联，但若您未来涉及测量误差或仪器校准问题，PoA框架可作为评估工具参考。
- **关键技术**: `Probability of Agreement (PoA)`, `Maximum Likelihood Estimation`, `Repeatability and Reproducibility`, `Mixed Effects Models`, `Delta Method`
- **为什么对您有用**: 本文属于应用统计方法，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术连接。它扩展了测量系统一致性评估的PoA指标，但方法学深度有限（主要是MLE和delta方法）。作为gateway reading，它不涉及您武器库中的任何具体工具（如minimax界、U-统计量、半参理论）。暂不可做：核心问题（测量系统一致性）不在您当前研究议程中，且方法学新颖性不足以驱动新问题。

### 10. [10.1080/00401706.2024.2374190](https://doi.org/10.1080/00401706.2024.2374190) — Data Science and Machine Learning for Non-Programmers Using SAS Enterprise Miner, 1st ed. <b>Data Science and Machine Learning for Non-Programmers Using SAS Enterprise Miner, 1st ed.</b> , Dothang Truong, CRC Press Taylor &amp; Francis Group, 2024. IX + 565 pages, £59,99 (hbk) ISBN: 978-0-367-75538-6 (hbk). Boca Raton and Abingdon. Scope: Textbook. Level: Students, lecturers, researchers, and industry professionals from various backgrounds.
- **作者**: Egi Rahmansyah, Nur Hidayah, Megawati Zein Waliulu, Hawinda Restu Putri
- **期刊/来源**: Technometrics
- **机构**: Universitas Gadjah Mada · IPB University · Bandung Institute of Technology
- **分类**: vol 66 · issue 3 · pp 493-494
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是对《Data Science and Machine Learning for Non-Programmers Using SAS Enterprise Miner》一书的书评。该书面向非编程背景的学生、研究人员和行业从业者，旨在通过SAS Enterprise Miner这一图形化界面工具，教授数据科学和机器学习的基本概念与流程。书评指出，该书覆盖了从数据理解、准备、建模到评估的完整CRISP-DM流程，并介绍了决策树、神经网络、回归、聚类等常用算法。书评认为该书适合作为入门教材，但缺乏对算法背后统计理论的深入讨论。对于您而言，这是一本面向初学者的应用导向教材，与您的研究兴趣（因果推断、高维统计、半参理论等）在方法论深度上不匹配，且不涉及您武器库中的任何具体技术工具。
- **关键技术**: `SAS Enterprise Miner`, `CRISP-DM framework`, `decision trees`, `neural networks`, `clustering`
- **为什么对您有用**: 这是一本面向非编程者的SAS Enterprise Miner入门教材书评，与您的主要研究兴趣（因果推断、高维统计、半参理论等）无直接关联。该书不涉及您武器库中的任何具体技术（如U-statistics、minimax bound、efficient influence function等），且作为书评本身不提供新的方法论或数据应用。因此，本文不值得花时间阅读全文。

### 11. [10.1080/00401706.2024.2374189](https://doi.org/10.1080/00401706.2024.2374189) — The Planetary Atom: A Fictional Account of George Adolphus Schott, the Forgotten Physicist <b>The Planetary Atom: A Fictional Account of George Adolphus Schott, the Forgotten Physicist</b> , Jean-Patrick Connerade, alias Chaunes. Singapore: World Scientific, 2022, xviii + 227 pp., $ 28.00 (pbk), ISBN 978-1-80061-014-9.
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 66 · issue 3 · pp 491-493
- 相关性 0/10 · novelty: `minor`
- **摘要**: 这是一篇书评，介绍了一部以小说形式讲述物理学家乔治·阿道夫斯·肖特生平及早期原子物理学史的作品。书评本身并未提出任何统计方法或理论。它属于文学与科学史交叉领域的读物，与统计学研究无关。
- **为什么对您有用**: 本文是一篇书评，内容为原子物理学史的小说，与您列出的任何研究方向（因果推断、高维统计、非参数理论等）均无直接或间接关联。不涉及任何统计方法、数据或模型，因此不值得阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

