# Technometrics — Vol 67  Issue 2  ·  2026-07-13

- 共 16 篇 · Technometrics
- 目录核对 ⚠️ 疑似漏 4 篇（对照 OpenAlex 20 篇）：10.1080/00401706.2025.2485656、10.1080/00401706.2025.2485657、10.1080/00401706.2025.2485655、10.1080/00401706.2025.2485661

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期 Technometrics 共 16 篇论文，整体上可归纳为四条主线：**因果推断与敏感性分析**（1 篇）、**非参数/半参数回归与降维**（3 篇）、**统计计算与算法等价性**（3 篇）、以及**假设检验与区间估计**（2 篇）。其余 7 篇分散在空间数据、极值分析、交通应用、书评等方向，与核心统计方法关联较弱。值得注意的是，本期在非参数/半参数方向集中出现了两篇关于单指标 Fréchet 回归的工作，分别处理分布响应建模和异常点检测，形成一个小型专题。

在**非参数/半参数回归**主线中，两篇单指标 Fréchet 回归论文值得关注：一篇提出分布-标量单指标分位数回归模型，通过分位数函数将分布响应映射到希尔伯特空间并引入单指标降维，系统建立了渐近性质；另一篇则将 Cook 距离推广到度量值回归，为单指标 Fréchet 回归提供影响诊断工具，但理论深度有限。此外，关于全局敏感性分析的论文利用 Shapley 效应与 Sobol 指数的线性变换关系，结合 Delta 方法和 Möbius 反演，为所有阶交互效应提供了同时推断框架，与因果推断中的 mediation 分析有潜在联系。

在**统计计算**主线中，分布式主支持向量机（PSVM）的论文展示了如何通过朴素或精炼分布式估计在保持 n^{-1/2} 收敛率的同时处理大规模数据，其统计效率保持的分析框架可迁移至高维或因果推断中的分布式估计。另一篇短文严格证明了正交化 EM 算法等价于近端梯度下降，揭示了其收敛性可直接借用成熟理论，适合关注算法等价性的读者。分层抽样设计论文则从方差缩减角度提出最优分层策略，与因果推断中的子群分析或自适应采样有交集。

对于因果推断方向的研究者，优先看《An Inference Method for Global Sensitivity Analysis》（交互效应推断与 mediation 的潜在联系）和《Distribution-on-Scalar Single-Index Quantile Regression Model》（单指标降维在高维协变量处理中的可迁移性）。对于半参数/非参数方向，两篇单指标 Fréchet 回归论文提供了分布响应建模和诊断工具的新视角。对于高维统计方向，《Profile Monitoring via Eigenvector Perturbation》展示了特征向量扰动在序列假设检验中的创新应用，而《Distributed Estimation of Principal Support Vector Machines》则涉及高维降维的分布式计算。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1080/00401706.2024.2431113](https://doi.org/10.1080/00401706.2024.2431113) — An Inference Method for Global Sensitivity Analysis
- **作者**: Gildas Mazo, Laurent Tournier
- **期刊/来源**: Technometrics
- **机构**: Université Paris-Saclay · Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement
- **分类**: vol 67 · issue 2 · pp 270-282
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对全局敏感性分析中交互效应（所有阶）的推断问题，提出了一种基于 Monte Carlo 样本的简单推断方法。核心思路是利用 Shapley 效应和 Sobol 指数均为总效应的线性变换这一事实，从而标准渐近理论（如 Delta 方法）即可用于构造置信区间和进行统计检验。数值计算上采用 Möbius 反演公式并关联快速 Möbius 变换算法，提高了计算效率。方法在涉及 12 个输入变量的布尔网络和 10 个输入变量的常微分方程系统两个生命科学实例上得到展示。该方法为敏感性分析提供了同时推断所有交互效应的实用工具，且理论简洁。对您而言，该文将敏感性分析与因果推断中的 mediation 和 interaction 概念联系起来，其线性变换和渐近推断思路可迁移至您熟悉的因果推断设定。
- **关键技术**: `Shapley effects`, `Sobol indices`, `Möbius inversion`, `fast Möbius transform`, `Delta method`, `Monte Carlo sampling`
- **为什么对您有用**: 本文连接至您 primary interest 中的因果推断（mediation/interaction）和 hypothesis testing 子方向。您武器库中 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 可直接用于理解其渐近推断框架，而 moderately_familiar 的 identification theory 可帮助评估其线性变换假设在因果设定下的适用性。**中期可做**：若想将本文方法推广至因果 mediation 中的交互效应推断，需先在 moderately_familiar 的 semiparametric theory 上加强，以处理更复杂的识别条件。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1080/00401706.2024.2441686](https://doi.org/10.1080/00401706.2024.2441686) — Distribution-on-Scalar Single-Index Quantile Regression Model for Handling Tumor Heterogeneity
- **作者**: Xingcai Zhou, Shengxian Ding, Jiangyan Wang, Rongjie Liu, Linglong Kong, Chao Huang
- **期刊/来源**: Technometrics
- **机构**: Nanjing Audit University · Yale University · University of Georgia · University of Alberta
- **分类**: vol 67 · issue 2 · pp 323-332
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对肿瘤影像异质性，提出分布-标量单指标分位数回归模型。目标是建模分布型响应（如肿瘤影像特征分布）与标量协变量的关系，同时处理分布响应位于非线性子空间、关联结构未知及缺乏统计推断等挑战。方法核心是：通过分位数函数将分布响应映射到希尔伯特空间，再引入单指标结构降维，未知连接函数和指标向量通过轮廓最小二乘估计。渐近性质（估计量的相合性、收敛速率、推断的渐近正态性）被系统建立。模拟和脑癌影像数据（TCIA-GBM）验证了有限样本性能。对您而言，该工作展示了非参数/半参数方法在复杂数据（分布响应）中的应用，与您的非参数统计和半参数理论兴趣直接相关，且其单指标降维思路可迁移至因果推断中的高维协变量处理。
- **关键技术**: `single-index model`, `quantile regression`, `distributional data analysis`, `profile least squares`, `Hilbert space embedding`
- **为什么对您有用**: 本文属于非参数/半参数理论方向，直接对应您的 primary interest。其分布响应的建模思路（通过分位数函数嵌入希尔伯特空间）是您 very_familiar 的非参数统计工具可以攻克的——您可以用 minimax 下界技术检验其估计量的最优性。中期可做：若您想将类似方法推广至因果推断（如分布型处理效应），需先在 moderately_familiar 的半参数理论上长肌肉（特别是影响函数推导）。

### 2. [10.1080/00401706.2024.2441683](https://doi.org/10.1080/00401706.2024.2441683) · [arXiv](https://arxiv.org/abs/2311.17246) — Detecting Influential Observations in Single-Index Fréchet Regression
- **作者**: Abdul-Nasah Soale
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 311-322
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对单指标 Fréchet 回归（响应变量为度量空间中的随机对象，协变量为欧氏向量）提出了一种度量 Cook 距离，用于检测异常观测点。该方法将经典 Cook 距离推广到非欧几里得响应空间，通过度量空间中的距离和 Fréchet 函数定义影响度量。在四种不同响应空间（如分布、网络）的模拟实验中验证了其有效性，并在两个真实数据应用（德克萨斯州 COVID-19 传播分布分析和脑结构连接网络分析）中展示了实用性。核心贡献在于为度量值回归提供了首个系统性的影响诊断工具，但方法本身是经典统计诊断的直白推广，缺乏新的理论深度（如影响函数的渐近分布或阈值选择准则）。对您而言，该文属于非参数回归的稳健性诊断方向，但 novelty 较低，且未涉及您核心兴趣中的因果推断或高维理论。
- **关键技术**: `Fréchet regression`, `Cook's distance`, `metric space response`, `single-index model`, `influence diagnostics`
- **为什么对您有用**: 该文属于非参数回归的稳健性诊断，与您的非参数统计兴趣有弱关联，但方法学贡献有限（经典 Cook 距离的度量推广），且未涉及因果推断、高维或效率理论。武器库中的非参数统计知识可理解其框架，但无直接可攻的问题。暂不可做——核心机器（如影响函数渐近理论、阈值选择）不在武器库中，且该方向本身非您主要兴趣。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1080/00401706.2024.2431119](https://doi.org/10.1080/00401706.2024.2431119) · [arXiv](https://arxiv.org/abs/2205.15422) — Profile Monitoring via Eigenvector Perturbation
- **作者**: Takayuki Iguchi, Andrés F. Barrientos, Eric Chicken, Debajyoti Sinha
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 283-292
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对统计过程控制（SPC）中的轮廓监控问题，提出了一种基于特征向量扰动理论的新型控制图（EPCC）。目标是同时实现极低的虚警率（FAR）和极短的检测延迟（ARL1），这在采样率高且ARL0≥200的实际场景中是一个经典挑战。方法的核心机制是利用特征向量对协方差矩阵扰动的敏感性来构造非参数监控统计量，无需分布假设。通过模拟研究，EPCC在多种常见过程偏移下均优于现有方法（如T²、MEWMA等），实现了ARL1≈1且ARL0>10⁶的极端性能。理论部分基于随机矩阵理论中的特征向量扰动界，给出了统计量的渐近性质。对您而言，本文展示了特征向量扰动这一高维统计工具在序列假设检验中的创新应用，与您的高维统计和假设检验兴趣直接相关。
- **关键技术**: `eigenvector perturbation`, `control chart`, `nonparametric profile monitoring`, `random matrix theory`, `average run length`
- **为什么对您有用**: 本文直接连接您的假设检验和高维统计兴趣，特别是特征向量扰动理论在序列监控中的应用。您的技术武器库中'高维渐近理论'和'随机矩阵理论'可以用于分析其统计量的渐近分布和最优性，属于**立即可做**的范畴。此外，本文的ARL0>10⁶极端性能为假设检验中的多重比较校正提供了新视角。

### 2. [10.1080/00401706.2024.2407324](https://doi.org/10.1080/00401706.2024.2407324) — Tolerance Intervals Under a Class of Unbalanced Linear Mixed Models
- **作者**: Cristian Oliva-Aviles, Paloma Hauser
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 193-202
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对一类非平衡线性混合模型（unbalanced linear mixed models）提出了一种计算 (β,γ)-容忍区间（tolerance intervals）的通用方法。现有文献主要处理单因素随机效应模型，本文将其推广到更一般的模型类，包括含多个随机效应和协变量的情形。方法基于广义枢轴量（generalized pivotal quantities）的概念，推导了该类模型下枢轴量的独立性，并利用蒙特卡洛采样获得容忍区间的实现。模拟研究表明，所提区间覆盖概率接近名义水平。通过药品稳定性数据估计货架期的实际案例，展示了方法在药物开发中的应用。对您而言，该文涉及混合模型下的区间估计与假设检验，与您对数学统计和假设检验的兴趣直接相关；其基于广义枢轴量的构造思路可迁移至因果推断中的敏感性分析或工具变量模型的置信区间构建。
- **关键技术**: `generalized pivotal quantities`, `Monte Carlo sampling`, `tolerance intervals`, `linear mixed models`, `unbalanced data`
- **为什么对您有用**: 该文直接关联您对假设检验和数学统计的兴趣，特别是混合模型下的区间估计问题。您武器库中'非参数统计'和'高维渐近理论'可用于分析其蒙特卡洛方法的收敛性，或将其广义枢轴量思路推广至更复杂的因果推断设定（如工具变量模型）。中期可做：若先熟悉'半参数理论'中的影响函数概念，可尝试将容忍区间方法扩展到半参数混合模型。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1080/00401706.2024.2422942](https://doi.org/10.1080/00401706.2024.2422942) · [arXiv](https://arxiv.org/abs/1911.12732) — Distributed Estimation of Principal Support Vector Machines for Sufficient Dimension Reduction
- **作者**: Jun Jin, Chao Ying, Zhou Yu
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 254-266
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对大规模数据下主支持向量机（PSVM）进行充分降维的计算瓶颈，提出了朴素分布式估计和精炼分布式估计两种算法。在分布式框架下，每个机器仅处理数据子集，通过平均或迭代合并局部解来逼近全局解。理论证明两种分布式估计量均能达到与全数据合并相同的统计效率（即 n^{-1/2} 收敛率），其中精炼方法在更小的批样本量下仍保持该性质，适合内存受限的分布式环境。方法进一步推广至二分类的主加权支持向量机（PWSVM）。模拟和真实数据（60万+样本）验证了统计精度与计算效率的权衡。对您而言，本文展示了如何将经典降维方法适配分布式计算，其“统计效率保持”的分析框架可迁移至您熟悉的因果推断或高维统计中的分布式估计问题（如分布式 DML），且精炼算法的通信策略对您开发统计软件有直接参考价值。
- **关键技术**: `distributed estimation`, `principal support vector machines`, `sufficient dimension reduction`, `divide-and-conquer`, `statistical efficiency preservation`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。您武器库中“software development”和“high-dimensional asymptotics”两项 very_familiar 工具可直接用于分析其分布式估计的收敛性（如检查其 n^{-1/2} 率是否紧，或推广至更一般的 M-估计框架）。中期可做：若想将类似分布式策略用于您 moderately_familiar 的“semiparametric theory”中的 DML 估计，需先熟悉“分布式推断中的通信效率与统计效率权衡”这一子领域（当前武器库缺此专项知识）。

### 2. [10.1080/00401706.2024.2416411](https://doi.org/10.1080/00401706.2024.2416411) — Strata Design for Variance Reduction in Stochastic Simulation
- **作者**: Jaeshin Park, Eunshin Byon, Young Myoung Ko, Sara Shashaani
- **期刊/来源**: Technometrics
- **机构**: University of Michigan · Pohang University of Science and Technology · North Carolina State University
- **分类**: vol 67 · issue 2 · pp 203-214
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究随机模拟中分层抽样（stratified sampling）的方差缩减问题，核心目标是设计最优的 strata 划分方案以最小化估计方差。在单变量情形下，作者解析推导了最优分层结构，给出了方差最小化的显式条件。针对高维输入空间，作者将最优分层思想与决策树（decision tree）算法结合，提出了一种鲁棒的多维分层构造方法，有效缓解了维数灾难和数据稀疏问题。数值实验和风电机组案例表明，该方法在方差缩减、计算效率和可扩展性上均优于现有方法。对您而言，本文的分层设计思路可迁移至因果推断中的子群分析或高维统计中的自适应采样策略，尤其适合需要平衡计算预算与估计精度的场景。
- **关键技术**: `stratified sampling`, `variance reduction`, `decision tree partitioning`, `optimal stratification`, `stochastic simulation`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，直接对应您 primary interest 中的 'statistical computing (numerical methods, algorithm)'。您武器库中的 'nonparametric statistics' 和 'minimax bounds' 可用于分析其分层策略的 minimax 最优性，而 'software development' 经验可帮助复现或扩展其算法。中期可做：若将分层思想与您 moderately_familiar 的 'identification theory in causal inference' 结合，可探索在 IV 或 mediation 设定下如何自适应分配样本以降低估计方差。

### 3. [10.1080/00401706.2024.2430204](https://doi.org/10.1080/00401706.2024.2430204) — Note on the Equivalence of Orthogonalizing EM and Proximal Gradient Descent
- **作者**: James Yang, Trevor Hastie
- **期刊/来源**: Technometrics
- **机构**: Stanford University
- **分类**: vol 67 · issue 2 · pp 267-269
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文指出 Xiong 等人提出的正交化 EM (OEM) 算法，本质上就是近端梯度下降 (proximal gradient descent) 的一个特例。OEM 最初被设计用于处理高瘦数据（tall data）的惩罚回归问题，其核心步骤是交替进行一个正交化变换和一个软阈值操作。作者通过代数推导，严格证明了 OEM 的迭代格式与近端梯度下降在特定步长和近端算子下的形式完全等价。这一等价性揭示：OEM 的收敛性分析可以直接借用近端梯度下降的成熟理论（如 O(1/k) 的次线性收敛率），无需重新建立。此外，该视角也自然解释了 OEM 为何能处理非光滑惩罚项（如 Lasso）。对于您而言，这篇短文提供了一个简洁的算法等价性案例，有助于在统计计算工具箱中建立不同优化算法之间的联系，尤其当您需要为高维统计问题设计或理解新算法时，这种视角迁移是有价值的。
- **关键技术**: `proximal gradient descent`, `orthogonalizing EM`, `penalized regression`, `tall data`, `convex optimization equivalence`
- **为什么对您有用**: 本文直接关联到您的 primary interest 中的 statistical computing 子方向，具体是算法等价性分析。您武器库中 very_familiar 的 high-dimensional asymptotics 和 software development 可以立即用于验证或扩展这种等价性：例如，在您熟悉的惩罚回归设定下，用数值实验检验 OEM 与近端梯度下降的实际收敛行为是否完全一致。这是一个立即可做的 follow-up：写一个简单的 R/Python 脚本，在 tall data 场景下对比两种实现的迭代路径和计算时间。

## 其他  *(other, 8 篇)*

### 1. [10.1080/00401706.2024.2447282](https://doi.org/10.1080/00401706.2024.2447282) · [arXiv](https://arxiv.org/abs/1906.08843) — On Statistical Properties of a Veracity Scoring Method for Spatial Data
- **作者**: Arnab Chakraborty, Soumendra N. Lahiri
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 344-355
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对空间数据（geostatistical data）中部分观测可能被噪声污染的场景，提出了一种基于“局部”汇总统计量的真实性评分（veracity scoring, VS）方法，用于衡量每个观测的可靠性。在非平稳噪声结构和一般性空间过程假设下，作者将VS作为权重引入空间回归模型，构建了回归参数的VS加权估计量。理论部分证明了该估计量的一致性，并通过渐近均方误差（asymptotic MSE）分析，从理论和数值两方面展示了VS估计量相比普通最小二乘（OLS）估计量的优势。模拟和真实数据实验表明，VS方法在抗污染数据方面优于现有的稳健空间统计方法。本文的方法学贡献在于为缺乏高质量参考数据的空间数据提供了一种可操作的可靠性评估与稳健估计框架。对您而言，本文属于统计计算与空间统计的交叉应用，但核心问题（数据可靠性评估与稳健估计）与您的主要兴趣（因果推断中的测量误差/敏感性分析、非参数估计）有一定间接关联，可作为方法学参考，但并非直接相关领域的前沿进展。
- **关键技术**: `veracity scoring`, `local summary statistics`, `spatial regression`, `asymptotic mean squared error`, `robust estimation`
- **为什么对您有用**: 本文属于空间统计的应用方法论文，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集。其核心方法（基于局部汇总的加权估计）在理论上较为常规，未涉及您武器库中的高阶工具（如树宽/张量收缩、半参数效率界）。作为gateway reading，本文对空间数据稳健估计的入门有一定价值，但方法学新颖性有限，暂不构成可迁移的技术问题。

### 2. [10.1080/00401706.2024.2444310](https://doi.org/10.1080/00401706.2024.2444310) · [arXiv](https://arxiv.org/abs/2110.10604) — Bayesian Model Calibration and Sensitivity Analysis for Oscillating Biological Experiments
- **作者**: Youngdeok Hwang, Hang J. Kim, Won Chang, Christian Hong, Steven N. MacEachern
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 333-343
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对振荡型生物实验中的计算机模型校准问题，提出了一套贝叶斯框架。核心挑战在于振荡过程的参数可识别性差、数值不稳定以及高维带来的病态行为。作者构建了贝叶斯模型，并利用先进的马尔可夫链蒙特卡洛（MCMC）技术高效推断匹配模拟与观测振荡过程的参数。此外，提出了一种基于干预后验的敏感性分析方法，利用MCMC样本衡量单个参数对目标过程的影响。该方法在粗糙脉孢菌（Neurospora crassa）的昼夜节律振荡数据上进行了验证。本文主要贡献在于将贝叶斯校准与敏感性分析系统性地应用于振荡生物模型，但方法学上未引入新的统计理论或推断框架。对您而言，本文属于应用导向的统计计算工作，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术交集，但可作为了解贝叶斯MCMC在生物系统建模中应用的入门读物。
- **关键技术**: `Bayesian calibration`, `Markov chain Monte Carlo (MCMC)`, `intervention posterior`, `sensitivity analysis`, `oscillating biological models`
- **为什么对您有用**: 本文属于应用统计计算工作，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术交集。作为gateway-reading，本文对统计学家友好，清晰阐述了振荡模型校准的数据与模型结构，但方法学新颖性有限，未涉及您武器库中的核心工具（如非参、minimax界、高阶U-统计量）。暂不可做：核心机器（贝叶斯MCMC与振荡模型）不在您的武器库中，且与您当前研究方向距离较远，不值得花时间精读全文。

### 3. [10.1080/00401706.2024.2441679](https://doi.org/10.1080/00401706.2024.2441679) — Spatiotemporal Interactive Modeling of Event-Based Dynamic Networks
- **作者**: Di Wang, Xiaochen Xian, Haidong Li
- **期刊/来源**: Technometrics
- **机构**: Shanghai Jiao Tong University · Georgia Institute of Technology · National Academy of Governance · University of Chinese Academy of Sciences
- **分类**: vol 67 · issue 2 · pp 293-310
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对事件型动态网络（如交通、社交网络中的交互事件序列）提出了一种时空交互霍克斯过程（SIHP）模型。该模型显式刻画了任意节点对之间交互事件的发生率，并利用历史事件信息以及地理和语义邻近节点的信息来建模事件间的触发与影响模式。模型将空间结构先验知识作为图正则化项纳入，并通过交替方向乘子法（ADMM）框架进行参数估计。数值实验和纽约黄色出租车数据的案例分析验证了方法的有效性。该工作属于应用统计建模，方法学创新集中在时空点过程与图正则化的结合，而非因果推断或高维统计的核心理论。
- **关键技术**: `Hawkes process`, `graph regularization`, `alternating direction method of multipliers (ADMM)`, `spatiotemporal modeling`, `event-based dynamic networks`
- **为什么对您有用**: 本文属于应用统计建模，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集。方法学上未涉及您武器库中的核心工具（如非参极小极大界、高阶U-统计量、半参效率理论）。作为gateway reading，本文对统计计算（ADMM框架）有一定参考价值，但整体相关性较低，暂不可做。

### 4. [10.1080/00401706.2024.2421744](https://doi.org/10.1080/00401706.2024.2421744) · [arXiv](https://arxiv.org/abs/2310.17999) — Automated Threshold Selection and Associated Inference Uncertainty for Univariate Extremes
- **作者**: Conor Murphy, Jonathan A. Tawn, Zak Varty
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 2 · pp 215-224
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对单变量极值分析中的阈值选择问题，提出了一种自动化方法。核心思想是直接处理偏差-方差权衡：阈值过低导致极值模型拟合有偏，过高则增加参数估计的不确定性。方法通过优化一个目标函数来自动选择阈值，并进一步开发了将阈值估计的不确定性传播到高分位数推断的技术。模拟研究表明，该方法在阈值选择和极端分位数估计上优于现有主流方法，且对调参不敏感。文章还应用于经典的River Nidd数据集进行演示。该方法本质上是极值统计中的实用工具开发，与您的主要研究兴趣（因果推断、高维统计、U统计量等）无直接交集。
- **关键技术**: `threshold selection`, `bias-variance tradeoff`, `extreme value analysis`, `uncertainty propagation`, `high quantile inference`
- **为什么对您有用**: 本文属于极值统计的应用方法，与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接关联。作为gateway reading，它并非您当前武器库（非参数统计、U统计量计算、因果推断等）能直接攻克的领域，且极值统计的核心工具（如广义帕累托分布、点过程模型）不在您的技术栈中。因此，本文暂不可做，不值得花时间深入阅读。

### 5. [10.1080/00401706.2024.2421752](https://doi.org/10.1080/00401706.2024.2421752) — Modeling Crash Risk on Roadway Networks Using Bayesian Regression Trees
- **作者**: Benjamin K. Dahl, Matthew J. Heaton, Richard L. Warr, Jared D. Fisher, Grant G. Schultz
- **期刊/来源**: Technometrics
- **机构**: Brigham Young University
- **分类**: vol 67 · issue 2 · pp 225-237
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种在非规则道路网络上建模车辆碰撞风险的方法。将道路网络上的碰撞事件视为泊松点过程，其强度函数为分段线性曲面。结合贝叶斯加性回归树（BART）与空间数据分析，估计强度曲面并推断道路特征（如限速、车道数）对碰撞风险的影响。方法在犹他州州际公路碰撞数据集上进行了实证分析。主要贡献在于将BART扩展到不规则网络空间点过程，提供了一种灵活的非参数建模工具。对您而言，本文属于应用统计方法在交通领域的案例，与您的主要研究方向（因果推断、高维统计等）关联较弱，但可作为了解BART在空间点过程应用的入门读物。
- **关键技术**: `Bayesian additive regression trees`, `Poisson point process`, `piecewise linear intensity`, `spatial data analysis`
- **为什么对您有用**: 本文属于应用统计方法在交通领域的实证研究，与您的主要兴趣（因果推断、高维统计、半参理论等）无直接关联。作为gateway-reading，本文对BART在空间点过程的应用有清晰阐述，但问题本身（碰撞风险建模）对统计方法论的挑战性一般。武器库中'非参数统计'和'软件'可支撑理解，但缺乏与您核心工具（如U统计量、效率理论）的接口。暂不可做：核心问题不匹配。

### 6. [10.1080/00401706.2024.2421763](https://doi.org/10.1080/00401706.2024.2421763) — Remaining Useful Life Prediction Based on Forward Intensity
- **作者**: Peihong Xiao, Yudong Wang, Wenting Liu, Zhi-Sheng Ye
- **期刊/来源**: Technometrics
- **机构**: National University of Singapore · Singapore University of Social Sciences
- **分类**: vol 67 · issue 2 · pp 238-253
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对无固定失效阈值场景下的剩余寿命预测问题，提出基于前向强度（forward intensity）的新方法。该方法将历史退化信号视为时变协变量，通过平滑样条估计前向强度函数中的时变回归参数，替代了传统的最大伪似然估计。预测区间也一并给出。蒙特卡洛模拟和三个真实数据案例表明，所提方法在预测精度上优于现有方法。本文的核心贡献在于将计量经济学中的前向强度工具引入可靠性工程，并解决了阈值缺失的难题。对您而言，本文属于应用统计方法在工程领域的拓展，与您的主要研究方向（因果推断、高维统计等）关联较弱，但可作为统计计算与算法应用的参考。
- **关键技术**: `forward intensity`, `smoothing splines`, `maximum pseudolikelihood`, `prediction interval`
- **为什么对您有用**: 本文属于工程可靠性领域的应用统计方法，与您的主要兴趣（因果推断、高维统计、半参理论等）直接关联较弱。武器库中的非参数统计和软件工程经验可帮助理解平滑样条的实现，但核心问题（无阈值RUL预测）并非您当前研究重点。暂不可做——缺乏该领域特定的退化模型和可靠性工程背景。

### 7. [10.1080/00401706.2025.2485660](https://doi.org/10.1080/00401706.2025.2485660) — Machine Learning For Transportation Research and Application
- **作者**: Johanes Robert Kera, Agri Satrio Adi Nugroho
- **期刊/来源**: Technometrics
- **机构**: Universitas Gadjah Mada · ADA University
- **分类**: vol 67 · issue 2 · pp 362-363
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是对《Machine Learning for Transportation Research and Applications》一书的书评，发表于 Technometrics。书评概述了该书的结构，涵盖从基础机器学习方法到交通领域特定应用（如交通流预测、需求预测、车辆轨迹分析等）的内容。书评指出该书适合作为交通领域从业者的入门教材，强调其将 ML 方法与实际交通问题结合的特点。但书评本身并未提出新的方法论或理论贡献，也未深入讨论任何统计或计算技术细节。对于您而言，这是一篇应用领域的书评，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接技术关联。
- **为什么对您有用**: 本文属于应用领域的书评，与您的主要研究兴趣（因果推断、高维统计、半参数理论、计算统计等）无直接技术关联。它不涉及新的方法、理论或数据，也不提供可迁移的技术工具。作为 gateway reading 也不合适，因为书评本身没有详细阐述交通数据或模型的结构。因此，不值得花时间阅读全文。

### 8. [10.1080/00401706.2025.2485658](https://doi.org/10.1080/00401706.2025.2485658) — Robust and Multivariate Statistical Methods: Festschrift in Honor of David E. Tyler
- **作者**: Cacu Cacu, Dadan Hermawan
- **期刊/来源**: Technometrics
- **机构**: Universitas Gadjah Mada · Jenderal Soedirman University
- **分类**: vol 67 · issue 2 · pp 360-362
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是对一本名为《Machine Learning for Transportation Research and Applications》的书的分析性书评，发表在Technometrics上。书评详细介绍了该书的章节结构、覆盖范围（包括交通领域的机器学习应用）以及写作风格。书评指出该书适合作为交通领域研究生的入门教材或从业者的参考书，但并未提出任何新的统计方法或理论。书评本身不包含原创的方法论贡献或实证分析，仅是对现有出版物的评价。对于您而言，这是一篇书评，与您的主要研究兴趣（因果推断、高维统计、U-统计量等）没有直接的方法学关联。
- **为什么对您有用**: 本文是一篇书评，不涉及新的统计方法或理论，与您的主要研究兴趣（因果推断、高维统计、U-统计量、半参数理论等）无直接关联。它属于应用领域的综述性读物，但并未提供可供迁移的方法学工具或可分析的公开数据集。因此，暂不可做，不值得投入时间阅读全文。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

