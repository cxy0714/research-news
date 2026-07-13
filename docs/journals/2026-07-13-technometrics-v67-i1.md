# Technometrics — Vol 67  Issue 1  ·  2026-07-13

- 共 22 篇 · Technometrics
- 目录核对 ✅ 22 篇全部抓到（对照 OpenAlex 23 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期 Technometrics 的 22 篇论文整体上呈现出三条主线：**因果推断与有限总体推断**、**计算机实验设计与贝叶斯优化**、以及**时间序列与空间统计建模**。此外，还有少量工作涉及**假设检验**（如频域序列比较）和**实验设计**（如 OofA 与混合因子筛选）。因果推断方向仅有一篇，但方法学上自成一体；计算机实验设计方向论文数量最多，覆盖了主动学习、多保真度建模、多智能体协作等子主题；时间序列与空间统计方向则聚焦于非平稳性、突变检测和极值依赖。

在**因果推断与有限总体推断**这条主线上，唯一一篇论文《Active Sampling: A Machine-Learning-Assisted Framework for Finite Population Inference with Optimal Subsamples》提出了一个主动采样框架，将机器学习预测（随机森林）与重要性采样（泊松/条件泊松）结合，用于在给定协变量信息但结果未知时自适应选择子样本，以最小化 Horvitz-Thompson 估计量的方差。该方法本质上是在有限总体框架下用主动学习优化因果估计的效率，与您关注的因果识别与效率问题直接相关。另一条主线是**计算机实验设计与贝叶斯优化**，包含多篇论文：例如《Bayesian Sequential Design of Computer Experiments for Quantile Set Inversion》用高斯过程与 SUR 原则解决鲁棒优化中的集合反演问题；《Active Learning for a Recursive Non-Additive Emulator for Multi-Fidelity Computer Experiments》提出递归非可加高斯过程模型，并设计了四种主动学习策略来平衡多保真度仿真的精度与成本；《Multi-Agent Collaborative Bayesian Optimization via Constrained Gaussian Processes》则引入约束高斯过程，使多个智能体在不交换原始数据的前提下协作优化异质黑箱函数。这些工作共同推进了计算机实验中的序贯设计、多保真度建模和分布式优化，与您对统计计算与主动学习的兴趣有交集。

在**时间序列与空间统计**方向，多篇论文处理非平稳性和突变问题：《Drift versus Shift: Decoupling Trends and Changepoint Analysis》用贝叶斯动态线性模型与收缩先验解耦趋势与变点；《Locally Adaptive Shrinkage Priors for Trends and Breaks in Count Time Series》针对计数数据提出负二项贝叶斯趋势滤波器；《Flexible Modeling of Nonstationary Extremal Dependence using Spatially Fused LASSO and Ridge Penalties》用空间融合惩罚处理极值依赖的非平稳性。此外，《Scalable Methods for Multiple Time Series Comparison in Second Order Dynamics》属于假设检验方向，提出了可扩展的频域成对比较方法，并推导了渐近联合分布。如果您关注因果推断，建议优先看《Active Sampling》；若关注半参数效率或高维统计，可留意《Scalable Methods》中的多重比较渐近理论；若关注统计计算，则《Active Learning for a Recursive Non-Additive Emulator》和《Multi-Agent Collaborative Bayesian Optimization》值得一读。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1080/00401706.2024.2374554](https://doi.org/10.1080/00401706.2024.2374554) · [arXiv](https://arxiv.org/abs/2212.10024) — Active Sampling: A Machine-Learning-Assisted Framework for Finite Population Inference with Optimal Subsamples
- **作者**: Henrik Imberg, Xiaomi Yang, Carol Flannagan, Jonas Bärgman
- **期刊/来源**: Technometrics
- **机构**: Chalmers University of Technology · University of Gothenburg · Michigan Department of Transportation · University of Michigan
- **分类**: vol 67 · issue 1 · pp 46-57
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种主动采样框架，用于有限总体推断中基于最优子样本的估计。目标是在给定总体协变量信息但结果变量未知的场景下，通过自适应地选择子样本以最小化估计量的方差。方法核心是迭代过程：利用已有子样本拟合机器学习模型（如随机森林）预测未采样单元的结果，然后基于预测值构造重要性权重，采用泊松采样或条件泊松采样选择下一批子样本，使得估计量的渐近方差最小。该框架与Horvitz-Thompson估计量结合，并证明了在适当条件下估计量的相合性和渐近正态性。模拟和实际案例（虚拟仿真安全评估）显示，相比简单随机抽样或固定比例分层抽样，主动采样在相同样本量下显著降低均方误差。对您而言，本文的主动学习+重要性采样思路可迁移至因果推断中的自适应数据收集设计（如IV或纵向研究中的样本选择），且其方差最小化框架与您熟悉的非参数估计和M估计理论有直接接口。
- **关键技术**: `adaptive importance sampling`, `Horvitz-Thompson estimator`, `conditional Poisson sampling`, `active learning`, `finite population inference`
- **为什么对您有用**: 本文连接因果推断中的自适应数据收集问题（如IV或纵向研究中的样本选择偏差校正），其核心方差最小化框架可直接用您熟悉的非参数估计和M估计理论分析。武器库中'minimax bounds for estimation problems'可用于验证其声称的方差缩减是否最优。中期可做：需先在'moderately_familiar'的HOIF上长肌肉，以处理更复杂的因果估计量（如DR估计）的自适应采样。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1080/00401706.2024.2388547](https://doi.org/10.1080/00401706.2024.2388547) — Scalable Methods for Multiple Time Series Comparison in Second Order Dynamics
- **作者**: Lei Jin, Bo Li
- **期刊/来源**: Technometrics
- **机构**: Texas A&M University – Corpus Christi · University of Illinois Urbana-Champaign
- **分类**: vol 67 · issue 1 · pp 82-96
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对多个时间序列在频域（二阶动态）上的统计比较问题，提出可扩展的检验方法。现有方法仅适用于少量独立序列或两两比较，本文基于一种新算法高效计算 M 个时间序列的所有成对谱特征差异，从而突破规模限制。在 M 个序列相互独立时，推导了成对特征差异的联合渐近分布，并利用其渐近依赖结构构造检验；对于相依序列，通过部分校正依赖结构将检验推广。此外还引入全局检验以增强整体推断能力。模拟表明新方法在独立和相依情形下均能处理大量序列且具有竞争性功效。应用实例为多个机械振动时间序列的比较。对您而言，本文的成对比较与多重检验的渐近联合分布推导，以及处理相依序列的校正策略，与您在高维统计和假设检验方面的兴趣直接相关。
- **关键技术**: `spectral density estimation`, `pairwise feature differences`, `joint asymptotic distribution`, `multiple testing`, `dependent time series`
- **为什么对您有用**: 本文属于假设检验方向，具体处理多个时间序列的频域比较，与您 primary interest 中的 hypothesis testing 和 high-dimensional statistics 直接相关。技术武器库中 very_familiar 的 high-dimensional asymptotics 可用于分析其成对比较的联合分布推导是否最优，而 moderately_familiar 的 M-estimation theory 可用于评估其相依序列校正策略的稳健性。中期可做：若想将本文的成对比较框架推广到更高阶的谱特征（如双谱），需先在 moderately_familiar 的 higher-order U-statistics 上提升，因为高阶谱估计涉及 U-statistic 结构。

### 2. [10.1080/00401706.2024.2407315](https://doi.org/10.1080/00401706.2024.2407315) — Practical and Optimal Likelihood Intervals and Regions for Weibull and Gumbel Distributions
- **作者**: Eloísa Díaz-Francés
- **期刊/来源**: Technometrics
- **机构**: Mathematics Research Center
- **分类**: vol 67 · issue 1 · pp 147-156
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对 Weibull 和 Gumbel 分布（广泛用于可靠性和环境科学）的参数及分位数，提出了具有良好覆盖概率且计算简便的 profile likelihood 区间估计方法。核心创新在于利用 Gumbel 分布属于位置-尺度族这一性质，以及似然对称化参数化技巧，将问题转化为更简单的推断形式。对于形状参数、尺度参数和分位数，分别给出了显式的 profile likelihood 区间公式，并提供了 R 代码实现（样本量 n≥10）。同时，还给出了两个参数的联合似然置信域。这些区间首次实现了对 Weibull 分布参数的高质量似然-置信推断，且计算成本极低。数值例子表明，所提区间在覆盖率和区间长度上优于传统渐近方法。该方法对您可能有用：它展示了如何利用分布族的结构性质（位置-尺度族）简化 profile likelihood 的计算，这一思路可迁移到您 moderately_familiar 的 semiparametric theory 中，用于构造更高效的 profile likelihood 推断。
- **关键技术**: `profile likelihood`, `likelihood-confidence interval`, `location-scale family`, `likelihood symmetrizing parameterization`, `Weibull distribution`, `Gumbel distribution`
- **为什么对您有用**: 本文属于 hypothesis_testing 方向，直接连接到您 primary interest 中的数学统计推断。其核心技巧——利用分布族的结构性质简化 profile likelihood 计算——与您 moderately_familiar 的 semiparametric theory 中的 profile likelihood 方法相通，可启发您在高维或半参数设定下构造更易计算的 profile likelihood 区间。从 follow-up 角度看，**中期可做**：您需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体是 profile likelihood 在 nuisance parameter 存在时的渐近理论），才能将本文的对称化参数化思路推广到更一般的半参数模型。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1080/00401706.2024.2407310](https://doi.org/10.1080/00401706.2024.2407310) — A Subsampling Strategy for AIC-based Model Averaging with Generalized Linear Models
- **作者**: Jun Yu, HaiYing Wang, Mingyao Ai
- **期刊/来源**: Technometrics
- **机构**: Beijing Institute of Technology · University of Connecticut · King University · Peking University
- **分类**: vol 67 · issue 1 · pp 122-132
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对大规模数据下广义线性模型的模型平均问题，提出了一种基于子抽样的AIC计算方法。现有子抽样方法通常忽略模型不确定性，本文通过校正子样本最大化目标函数的渐近偏差，推导出基于子样本的AIC形式，从而将子抽样技术扩展到平滑AIC模型平均框架。方法核心是构造一个渐近无偏的AIC估计量，使得在子样本上也能进行有效的模型选择与加权平均。作者给出了子抽样AIC模型平均估计量的损失和估计量的渐近性质，并开发了实际可实现的算法。数值实验在模拟和真实数据集上验证了方法的计算效率与统计性能。对您而言，本文展示了如何将计算约束（子抽样）与统计推断（模型平均）结合，属于统计计算与模型选择交叉的实用工作，但方法学新颖性有限，主要是应用层面的扩展。
- **关键技术**: `subsampling`, `Akaike information criterion (AIC)`, `smoothed AIC model averaging`, `generalized linear models (GLM)`, `asymptotic bias correction`
- **为什么对您有用**: 本文连接您的统计计算兴趣，特别是大规模数据下的计算效率问题。您武器库中的非参数统计与高维渐近工具可用于分析其子抽样AIC的渐近性质，但核心方法（AIC校正与模型平均）并非您最擅长的因果推断或U统计方向。属于中期可做：若想深入，需先在M估计理论（moderately_familiar）上加强，以理解其目标函数的渐近行为。

### 2. [10.1080/00401706.2024.2407314](https://doi.org/10.1080/00401706.2024.2407314) · [arXiv](https://arxiv.org/abs/2311.18146) — Co-Active Subspace Methods for the Joint Analysis of Adjacent Computer Models
- **作者**: Kellin N. Rumsey, Zachary K. Hardy, Cory Ahrens, Scott Vander Wiel
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 133-146
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出 Co-Active Subspace (Co-AS) 方法，用于联合分析两个相邻计算机模型（如物理模拟器）的输入-输出关系。传统 active subspace 方法仅针对单一模型，Co-AS 通过定义 co-active directions、co-sensitivity indices 以及标量 concordance 度量（及其互补的 discordance 伪度量），量化两个模型梯度空间的对齐程度。估计方法基于梯度矩阵的奇异值分解，计算高效，并提供了 R 包 concordance。在 PBX 9501 高爆炸药的模拟 rate stick 实验中，Co-AS 揭示了模型间的复杂动力学差异，补充了传统 AS 分析。对您而言，本文属于统计计算与降维方法的交叉，其核心思想（子空间对齐度量）可迁移至您熟悉的因果推断中敏感性分析或 IV 设定下两个代理变量的联合结构探索，且 R 包可直接用于原型验证。
- **关键技术**: `active subspace`, `co-active subspace`, `singular value decomposition`, `concordance metric`, `gradient space alignment`, `R package concordance`
- **为什么对您有用**: 本文属于统计计算与降维方法，直接对应您 primary interest 中的 'statistical computing (numerical methods, algorithm)'。其核心思想——用奇异值分解量化两个梯度子空间的对齐——可迁移至您 very_familiar 的 'inverse problems with random noise' 或 'estimation theory in causal inference' 中，例如在 IV 设定下比较两个工具变量的有效子空间。**中期可做**：需先在 moderately_familiar 的 'identification theory in causal inference' 上长肌肉，以将子空间对齐概念转化为因果识别条件。

### 3. [10.1080/00401706.2024.2376173](https://doi.org/10.1080/00401706.2024.2376173) · [arXiv](https://arxiv.org/abs/2309.11772) — Active Learning for a Recursive Non-Additive Emulator for Multi-Fidelity Computer Experiments
- **作者**: Junoh Heo, Chih-Li Sung
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 58-72
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对多保真度计算机实验的代理模型问题，提出了一种递归非可加（RNA）高斯过程模型。传统方法（如 Kennedy-O'Hagan 自回归模型）假设低保真度与高保真度输出之间为线性可加关系，而 RNA 模型通过递归高斯过程先验捕捉非线性非可加依赖，无需加性假设，从而适应更复杂的数据模式。作者推导了后验预测均值和方差的闭式表达式，避免了 MCMC 或数值积分，显著提升了计算效率。在此基础上，设计了四种主动学习策略，用于在给定预算下选择下一轮仿真的保真度层级和输入位置，以平衡精度与成本。数值实验和实际案例（如翼型阻力预测）验证了方法的有效性，并提供了 R 包 RNAmf。对您而言，本文的主动学习框架和闭式后验计算思路可迁移至您熟悉的因果推断或高维统计中的实验设计问题（如 IV 或敏感性分析中的仿真预算分配），但核心高斯过程建模与您的武器库（非参数统计、M 估计）有重叠，属于中期可做方向——需先熟悉高斯过程回归的主动学习文献。
- **关键技术**: `Gaussian process prior`, `recursive non-additive model`, `closed-form posterior`, `active learning strategies`, `multi-fidelity emulation`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关。您的武器库中 very_familiar 的软件开发和 nonparametric statistics 可支撑您快速理解并复现其闭式后验推导和主动学习策略；但高斯过程主动学习的理论（如 acquisition function 的 regret bound）属于 moderately_familiar 的 M-estimation 范畴，需先补课。中期可做：将 RNA 模型与您熟悉的 higher-order U-statistics 的 tensor-contraction 视角结合，分析多保真度数据下的计算-精度 tradeoff。

### 4. [10.1080/00401706.2024.2365732](https://doi.org/10.1080/00401706.2024.2365732) — Multi-Agent Collaborative Bayesian Optimization via Constrained Gaussian Processes
- **作者**: Qiyuan Chen, Liangkui Jiang, Hantang Qin, Raed Al Kontar
- **期刊/来源**: Technometrics
- **机构**: University of Michigan · University of Wisconsin–Madison
- **分类**: vol 67 · issue 1 · pp 32-45
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种多智能体协同贝叶斯优化框架，目标是在不交换原始数据的前提下，让多个智能体协作优化各自的异质黑箱函数。核心创新是引入一类约束高斯过程（constrained GP）作为替代模型，每个智能体通过约束条件从表现优异的协作者那里借用信息，从而加速自身优化。该方法与任意GP核函数和大多数已知采集函数兼容，具有通用性。理论方面，作者证明了该框架的收敛性保证，并分析了协作带来的信息增益。实验部分通过仿真和一个增材制造真实案例，展示了该方法在智能体函数异质时显著优于现有协同BO方法。对您而言，本文的约束GP机制和协作优化思路可迁移到您熟悉的因果推断或高维统计中的分布式/联邦学习场景，尤其是当各数据源存在异质性时，如何借用信息提升估计效率。
- **关键技术**: `constrained Gaussian process`, `collaborative Bayesian optimization`, `acquisition function`, `heterogeneous black-box functions`, `federated learning`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的统计计算（数值方法、算法）直接相关。您武器库中very_familiar的软件开发和high-dimensional asymptotics可用于复现和扩展其理论分析，例如验证收敛速率是否紧。中期可做：若您想将协作BO思想用于因果推断中的多站点异质性处理效应估计，需先在moderately_familiar的identification theory上补足多源数据识别条件。

## 其他  *(other, 15 篇)*

### 1. [10.1080/00401706.2024.2407316](https://doi.org/10.1080/00401706.2024.2407316) · [arXiv](https://arxiv.org/abs/2309.00080) — Locally Adaptive Shrinkage Priors for Trends and Breaks in Count Time Series
- **作者**: Toryn L. J. Schafer, David S. Matteson
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 157-167
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对非平稳计数时间序列（如具有突变和波动趋势的序列）提出了一种负二项贝叶斯趋势滤波器（NB-BTF）。该模型采用层次贝叶斯框架，结合动态全局-局部收缩先验，能够自适应地捕捉多尺度特征，同时保持对整数值推断的有效性。核心机制是通过全局-局部先验实现局部正则化，并利用时间依赖性诱导局部平滑趋势。模拟实验表明，NB-BTF在趋势滤波性能上优于多种现有方法。实证部分应用于马萨诸塞州乡镇的每周停电频率数据，展示了在低水平趋势伴随偶发尖峰场景下的平滑非平稳趋势估计与不确定性量化。该方法对您的主要兴趣（如非参数统计、高维收缩先验）有一定技术关联，但更偏向贝叶斯时间序列建模，与您的核心方向（因果推断、高维随机矩阵、U-统计量）直接交集有限。
- **关键技术**: `global-local shrinkage prior`, `negative binomial likelihood`, `Bayesian trend filtering`, `dynamic shrinkage process`, `state-space model`
- **为什么对您有用**: 本文属于贝叶斯时间序列方法，与您的主要兴趣（因果推断、高维统计、U-统计量）直接交集有限。技术武器库中的非参数统计和M-估计理论可部分用于理解其收缩先验的渐近性质，但核心贝叶斯框架与您的工具集（如minimax界、高阶U-统计量）匹配度低。作为gateway阅读，本文对计数时间序列的建模思路（如全局-局部先验处理突变）可能对您未来处理纵向因果推断中的计数结局有启发，但暂不可做——缺乏贝叶斯计算和状态空间模型的直接工具。

### 2. [10.1080/00401706.2024.2365729](https://doi.org/10.1080/00401706.2024.2365729) — Convolutional Non-Homogeneous Poisson Process and its Application to Wildfire Ignition Risk Quantification for Power Delivery Networks
- **作者**: Guanzhou Wei, Feng Qiu, Xiao Liu
- **期刊/来源**: Technometrics
- **机构**: Georgia Institute of Technology · Argonne National Laboratory
- **分类**: vol 67 · issue 1 · pp 11-22
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出卷积非齐次泊松过程（cNHPP），用于量化电力传输网络上的野火点燃风险。模型将野火点燃视为时空点过程，其强度函数同时包含环境协变量的瞬时效应和累积历史效应，并通过卷积结构刻画电力网络不同区段之间的时空依赖性。强度函数的计算和解释性被详细讨论。应用部分使用加州主要输电线路的历史火灾数据、气象和植被数据（来自NOAA和NASA）进行实证分析，并与多种基准方法比较，展示了模型的预测能力和实用性。该工作属于应用统计建模，方法学创新在于将卷积机制引入非齐次泊松过程以处理时空依赖，但整体框架是经典点过程模型的扩展。对您而言，本文属于应用领域（流行病学/环境风险）的实证工作，若您关注点过程在因果推断或流行病学中的应用，可作为入门参考。
- **关键技术**: `Non-homogeneous Poisson process`, `spatio-temporal point process`, `convolutional intensity function`, `environmental covariates`
- **为什么对您有用**: 本文属于应用统计建模，与您的主要兴趣（因果推断、高维统计等）无直接技术交集。作为流行病学/环境风险领域的应用工作，它展示了点过程模型在真实数据上的使用流程，但方法学深度有限。武器库中的非参数统计和估计理论可用于评估其强度函数估计的收敛性，但这不是本文重点。暂不可做——核心机器（时空点过程的渐近理论、卷积核选择）不在武器库中，且本文不涉及因果识别或效率理论。

### 3. [10.1080/00401706.2024.2365730](https://doi.org/10.1080/00401706.2024.2365730) — Drift versus Shift: Decoupling Trends and Changepoint Analysis
- **作者**: Haoxuan Wu, Toryn L. J. Schafer, Sean Ryan, David S. Matteson
- **期刊/来源**: Technometrics
- **机构**: Cornell University · Texas A&M University
- **分类**: vol 67 · issue 1 · pp 23-31
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种将趋势（drift）与变点（shift）解耦的时间序列分析方法。首先使用过参数化的贝叶斯动态线性模型（DLM）结合收缩先验（如 horseshoe 或 LASSO 型先验）对平滑趋势进行估计，该步骤擅长处理复杂噪声但无法实现精确的变点检测。随后利用加权惩罚似然估计（如 fused LASSO 或 adaptive LASSO）基于 DLM 后验分布识别变点位置，利用其硬阈值特性实现精确检测。该方法对异常值稳健，可检测均值或斜率变化，并易于扩展至时变参数模型。模拟和实证表明，该方法在复杂噪声环境下优于纯贝叶斯或纯惩罚方法。对您而言，本文属于时间序列分析的应用方法，与您的主要兴趣（因果推断、高维统计等）无直接交集，但变点检测与纵向因果推断中的结构变化问题有一定概念联系。
- **关键技术**: `Bayesian dynamic linear model`, `shrinkage priors`, `penalized likelihood estimation`, `fused LASSO`, `changepoint detection`
- **为什么对您有用**: 本文属于时间序列方法论文，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。变点检测与纵向因果推断中的结构变化问题有概念联系，但方法本身（贝叶斯 DLM + 惩罚似然）并非您武器库中的核心工具。暂不可做——核心机器（贝叶斯时间序列、变点检测理论）不在武器库中，且无直接可迁移的技术口子。

### 4. [10.1080/00401706.2025.2455298](https://doi.org/10.1080/00401706.2025.2455298) — Models for Multi-State Survival Data Rates, Risks, and Pseudo-Values, 1st ed.
- **作者**: Siti Mutiah, Indra Rivaldi Siregar
- **期刊/来源**: Technometrics
- **机构**: IPB University
- **分类**: vol 67 · issue 1 · pp 182-184
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文是对《Models for Multi-State Survival Data: Rates, Risks, and Pseudo-Values》一书的书评，发表于 Technometrics。该书系统介绍了多状态生存数据的统计框架，涵盖率、风险以及伪值方法。书评指出，该书适合作为应用统计工作者的参考书，但并未提出新的统计方法或理论。对于您而言，该书评属于书评类文章，不涉及具体的方法学创新或技术细节，与您的主要研究方向（因果推断、高维统计、半参数理论等）无直接关联。
- **关键技术**: `multi-state models`, `pseudo-values`, `survival analysis`
- **为什么对您有用**: 本文是书评，不涉及新的统计方法或理论，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接关联。作为书评，它可能提供多状态生存数据的入门概述，但缺乏技术深度，不值得投入时间阅读全文。

### 5. [10.1080/00401706.2024.2388549](https://doi.org/10.1080/00401706.2024.2388549) · [arXiv](https://arxiv.org/abs/2210.05792) — Flexible Modeling of Nonstationary Extremal Dependence using Spatially Fused LASSO and Ridge Penalties
- **作者**: Xuanjie Shao, Arnab Hazra, Jordan Richards, Raphaël Huser
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 97-111
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对非平稳空间极值依赖结构的建模问题，提出一种全局非平稳但局部平稳的 max-stable 过程（MSP）构造。将空间域划分为细网格子区域，每个子区域有自己的依赖参数，并采用 LASSO（L1）或 ridge（L2）惩罚来获得空间平滑的参数估计。进一步开发了一种数据驱动的算法，将同质相邻子区域合并，以提高模型简洁性和可解释性。为适应高维数据，使用 pairwise 似然进行推断，并讨论了其计算与统计效率。方法应用于尼泊尔及喜马拉雅地区 1400 多个站点的月最高温度数据，相比平稳模型显著改善了拟合效果。合并后的分区在地理上具有可解释性，并通过减少参数数量提升了模型诊断能力。本文主要贡献在空间极值统计的应用与方法，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接技术重叠。
- **关键技术**: `max-stable process`, `pairwise likelihood`, `LASSO penalty`, `ridge penalty`, `spatial clustering`
- **为什么对您有用**: 本文属于空间统计与极值理论的交叉应用，与您的主要兴趣方向（因果推断、高维统计、U-统计量、半参效率理论等）无直接技术连接。武器库中无空间极值建模的核心工具（如 max-stable 过程、pairwise 似然），且方法学 novelty 有限（主要是 LASSO/ridge 惩罚在空间极值上的应用）。作为 gateway reading 也不合适，因为需要极值统计背景。建议跳过。

### 6. [10.1080/00401706.2024.2394475](https://doi.org/10.1080/00401706.2024.2394475) · [arXiv](https://arxiv.org/abs/2211.01008) — Bayesian Sequential Design of Computer Experiments for Quantile Set Inversion
- **作者**: Romain Ait Abdelmalek-Lomenech, Julien Bect, Vincent Chabridon, Emmanuel Vazquez
- **期刊/来源**: Technometrics
- **机构**: Laboratoire des signaux et systèmes · Universitas Quality · EDF Energy (United Kingdom) · Laboratoire Pluridisciplinaire de Recherche en Ingénierie des Systèmes, Mécanique et Energétique
- **分类**: vol 67 · issue 1 · pp 112-121
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究 Quantile Set Inversion (QSI) 问题：给定一个未知多变量函数（如复杂数值模拟器），其输入包含确定性参数和随机参数，目标是估计所有确定性输入构成的集合，使得在这些输入下输出值落入给定集合的概率（关于随机参数分布）低于某个阈值。该问题出现在鲁棒优化（基于可靠性的优化）中，即寻找以足够大概率满足约束的解集。作者提出一种基于高斯过程建模和逐步不确定性缩减 (SUR) 原则的贝叶斯序贯设计策略，用于高效选择函数评估点以逼近目标集合。通过多个数值实验展示了所提 SUR 策略的性能和优势。该方法属于计算机实验设计与贝叶斯优化的交叉领域，与统计计算中的序贯设计相关。
- **关键技术**: `Gaussian process modeling`, `Stepwise Uncertainty Reduction (SUR)`, `Bayesian sequential design`, `Quantile set inversion`, `Computer experiments`
- **为什么对您有用**: 本文属于统计计算中的序贯实验设计，与您的 secondary interest 中的统计计算（numerical methods, algorithm）有弱连接。但该文的方法论核心（高斯过程 + SUR）不在您的技术武器库中，且与您的主要研究方向（因果推断、高维统计、U-统计量）无直接交集。作为 gateway reading 价值有限，因为问题设定（计算机模拟器的鲁棒优化）与您的兴趣领域距离较远，且未涉及您熟悉的 minimax 理论或高维渐近分析。暂不可做。

### 7. [10.1080/00401706.2024.2379850](https://doi.org/10.1080/00401706.2024.2379850) · [arXiv](https://arxiv.org/abs/2310.12460) — Linear Source Apportionment Using Generalized Least Squares
- **作者**: Jordan G. Bryan, Peter D. Hoff, Christopher L. Osburn
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 73-81
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对水质监测中的荧光光谱数据，提出了一种线性源解析模型，用于估计溶解有机物（DOM）的高维剖面中各来源的贡献比例。方法核心是将源解析问题转化为广义最小二乘（GLS）估计框架，并给出了参数估计的显式表达式及其与普通最小二乘（OLS）的关系。作者进一步分析了估计量的变异性，并提出了DOM剖面中缺失元素的预测方法。在北卡罗来纳州纽斯河的荧光光谱数据集上展示了方法的实际效用。该工作属于应用统计方法在环境科学中的具体落地，方法学贡献在于将经典GLS框架适配到源解析问题，但未涉及因果推断、高维统计或半参理论等您的主要兴趣方向。
- **关键技术**: `generalized least squares`, `source apportionment`, `fluorescence spectroscopy`, `missing data prediction`
- **为什么对您有用**: 本文属于环境统计应用，与您的次要兴趣（流行病学/应用因果）有一定距离，但可作为了解荧光光谱数据结构和源解析问题的入门读物。武器库中的非参数统计和逆问题工具可处理其线性假设的推广，但核心方法（GLS）过于经典，缺乏您感兴趣的方法学深度。暂不可做——缺少与您主要兴趣（因果推断、高维U统计、计算-统计权衡）的直接连接点。

### 8. [10.1080/00401706.2024.2407317](https://doi.org/10.1080/00401706.2024.2407317) · [arXiv](https://arxiv.org/abs/2506.07096) — Robust Design for Order-of-Addition Experiments
- **作者**: Yiran Huang, Jian-Feng Yang
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 168-176
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究 order-of-addition (OofA) 实验的设计问题，目标是在 m 个组分的全排列 (m! 种) 不可行时找到高效且稳健的设计。现有设计（如 component orthogonal array, COA）在特定模型下最优，但在其他模型下可能奇异。作者提出一种新设计——maximin distance component orthogonal array (MDCOA)，它在保持 COA 任意两列平衡性的同时最大化最小成对距离，从而获得优良的空间填充性质。采用遗传算法搜索 MDCOA。理论证明 MDCOA 在 component-position 模型下是 D-最优的，并在其他模型下表现良好。案例研究和应用表明，MDCOA 在多种场景下优于现有两类设计。该论文属于实验设计领域，与您的主要兴趣（因果推断、高维统计等）无直接交集，但如果您对稳健实验设计或空间填充设计感兴趣，可作参考。
- **关键技术**: `maximin distance design`, `component orthogonal array`, `genetic algorithm`, `D-optimality`, `space-filling design`
- **为什么对您有用**: 本文属于实验设计（design of experiments）领域，与您的主要兴趣方向（因果推断、高维统计、半参理论等）无直接交集。您的技术武器库（非参统计、U-统计量、因果推断等）难以直接应用于 OofA 实验设计问题。因此，本文暂不可做，核心缺失在于实验设计（特别是序贯实验设计）的专业知识。

### 9. [10.1080/00401706.2024.2362149](https://doi.org/10.1080/00401706.2024.2362149) — Screening Designs for Continuous and Categorical Factors
- **作者**: Bradley Jones, Ryan Lekivetz, Dibyen Majumdar, Christopher Nachtsheim
- **期刊/来源**: Technometrics
- **机构**: Statistical Research (United States) · University of Illinois Chicago · Department of Physics, Mathematics and Informatics · University of Minnesota
- **分类**: vol 67 · issue 1 · pp 1-10
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的饱和筛选实验设计，用于同时包含连续因子（三水平）和分类因子（两水平）的场景。设计运行次数为 n=2m，其中 m≥4，且 n 为偶数时均可构造，突破了传统设计对运行次数的限制。当 n 是 8 的倍数时，设计正交；当 n 是 4 的倍数而非 8 的倍数时，三水平因子间及与两水平因子间正交，两水平因子间近似正交；当 n 仅为 2 的倍数时，组内近似正交、组间正交。模拟表明，在效应稀疏假设下，该设计能识别至多三个活跃的二次效应，且信噪比大于 1.5 时，识别 m 个主效应的功效接近 1。该工作属于实验设计领域的方法学贡献，与您的统计计算兴趣（设计构造）有微弱关联，但整体与您的主要研究方向（因果推断、高维统计、U-统计量等）距离较远。
- **关键技术**: `saturated designs`, `screening experiments`, `orthogonal and near-orthogonal arrays`, `effect sparsity`
- **为什么对您有用**: 本文属于实验设计（DOE）领域，与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。作为 gateway reading 价值有限，因为实验设计的方法学框架（正交阵列、效应稀疏）与您的技术武器库（非参、minimax、U-统计量）缺乏直接连接。暂不可做——核心机器（实验设计理论）不在武器库中。

### 10. [10.1080/00401706.2025.2455294](https://doi.org/10.1080/00401706.2025.2455294) · [arXiv](https://arxiv.org/abs/1811.09130) — Advanced Statistical Methods
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 178-179
- 相关性 1/10 · novelty: `survey`
- **摘要**: 这是一篇书评，介绍了一本涵盖经济学、管理学等应用领域基本统计方法的教科书。该书分为四章，每章包含多个小节，内容涉及基础统计方法及案例研究。书评简要概述了教材的结构和覆盖范围，但未深入讨论任何具体的方法论创新或理论贡献。作为一篇书评，本文缺乏对统计方法本身的实质性讨论或新见解。对于您的研究方向，这篇书评没有提供新的方法论、理论或应用案例，因此参考价值有限。
- **为什么对您有用**: 本文是一篇书评，不包含新的统计方法、理论或应用分析，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接关联。它既不是入门读物，也未提供可迁移的技术工具或值得关注的数据分析模式。因此，不值得花时间阅读全文。

### 11. [10.1080/00401706.2025.2455296](https://doi.org/10.1080/00401706.2025.2455296) — Statistics Today: Everyday Applications, Research Questions, Insights, and Challenges
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 179-181
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是Technometrics期刊上的一篇书评，评述了《Statistics Today: Everyday Applications, Research Questions, Insights, and Challenges》一书。该书属于“社会、环境与统计”系列，收录了来自德国大学和研究中心的41位作者的论文。书评概述了该书的章节安排和主题范围，涵盖了统计在日常生活中的各种应用、研究问题、见解和挑战。书评本身并未提出新的统计方法或理论，而是对现有著作的介绍和评价。对于研究者而言，这篇书评的价值在于提供了一个快速了解该领域近期出版物概貌的入口，但缺乏深入的方法论细节。
- **为什么对您有用**: 这是一篇书评，不涉及具体统计方法或理论，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接关联。它属于信息性阅读，但无法提供可迁移的技术工具或可攻击的问题。作为gateway reading的价值也有限，因为它只是对一本论文集的概述，而非对某个子领域的系统入门。因此，不值得花费时间阅读全文。

### 12. [10.1080/00401706.2025.2455292](https://doi.org/10.1080/00401706.2025.2455292) — Correlation in Engineering and the Applied Sciences: Applications in R
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 177-178
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是一本书评，介绍《Correlation in Engineering and the Applied Sciences: Applications in R》一书。该书属于《Synthesis Lectures on Mathematics and Statistics》系列，主要讨论相关系数这一统计工具在工程与应用科学中的使用。书中内容涵盖相关系数的定义、性质、推断方法以及R语言实现。书评简要总结了各章内容，并评价了其作为教材或参考书的实用性。对于您而言，这是一篇书评而非原创研究，不涉及您主要兴趣中的任何具体方法论或理论进展。
- **关键技术**: `correlation coefficient`, `R programming`
- **为什么对您有用**: 本文为书评，不涉及具体方法学贡献或数据应用，与您的主要兴趣（因果推断、高维统计、半参数理论等）无直接关联。作为gateway reading，它也不属于您感兴趣的astrostatistics、经济理论或流行病学领域。因此不值得花时间阅读全文。

### 13. [10.1080/00401706.2025.2455297](https://doi.org/10.1080/00401706.2025.2455297) — Intelligent Fatigue Statistics
- **作者**: Zulfaidil, Shelma Maharani Pelu
- **期刊/来源**: Technometrics
- **机构**: Bandung Institute of Technology
- **分类**: vol 67 · issue 1 · pp 181-182
- 相关性 1/10 · novelty: `survey`
- **摘要**: 本文是一篇书评，评述了《Intelligent Fatigue Statistics》一书。该书将统计方法（如加速寿命试验、贝叶斯推断、机器学习）应用于材料疲劳分析，旨在预测材料在循环载荷下的失效概率。核心内容涵盖疲劳寿命分布的参数与非参数建模、小样本下的推断策略，以及如何将物理模型与数据驱动方法结合。书中强调了统计思维在工程可靠性中的关键作用，但并未提出新的统计理论或方法。对您而言，本文属于应用导向的综述性读物，与您的主要研究方向（因果推断、高维统计、半参理论等）无直接技术交集。
- **关键技术**: `accelerated life testing`, `Bayesian inference`, `machine learning for reliability`
- **为什么对您有用**: 本文属于书评，不涉及新的统计方法论或理论贡献。它与您的主要兴趣（因果推断、高维统计、半参理论等）无直接关联，也不属于您指定的次级兴趣领域（如天体统计、经济理论、流行病学）中的实证应用。因此，不值得投入时间阅读全文。

### 14. [10.1080/00401706.2024.2374956](https://doi.org/10.1080/00401706.2024.2374956) — OMARS Letter for Technometrics
- **作者**: James M. Lucas
- **期刊/来源**: Technometrics
- **机构**: Lucas Research
- **分类**: vol 67 · issue 1 · pp 186-188
- 相关性 1/10 · novelty: `minor`
- **摘要**: 本文是一封致Technometrics编辑的信，讨论Nunez Ares和Goos (2020)提出的OMARS（正交最小混杂响应曲面）设计的实用性。作者从实际应用角度出发，对OMARS设计在某些场景下的有效性提出质疑，并给出了自己的观点。该信主要基于作者在工业实验设计领域的长期经验，对设计的选择标准进行了评述。文中没有提出新的统计方法或理论，也没有提供新的数据集或实证分析。对于专注于因果推断、高维统计、半参数理论等核心方向的您而言，这封信属于实验设计领域的应用讨论，与您的主要研究兴趣无直接关联。
- **关键技术**: `response surface methodology`, `orthogonal designs`, `minimal aliasing`
- **为什么对您有用**: 本文属于实验设计领域的应用讨论，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接关联。它既不是您主要兴趣方向的方法论进展，也不属于您次要兴趣（如天体统计、经济理论、流行病学）中具有方法论深度的应用工作。因此，该文不值得花费时间阅读全文。

### 15. [10.1080/00401706.2025.2455299](https://doi.org/10.1080/00401706.2025.2455299) · [arXiv](https://arxiv.org/abs/2510.01267) — Statistical Prediction and Machine Learning
- **作者**: Fransiskus Serfian Jogo
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 1 · pp 184-185
- 相关性 1/10 · novelty: `survey`
- **摘要**: 这是一篇书评，对一本关于统计预测与机器学习的教材进行概述。文章简要介绍了该教材的内容结构，涵盖从经典统计方法到现代机器学习算法的广泛主题。书评指出该书适合作为数据科学入门课程的参考读物，强调其理论与实践的结合。然而，本文并未提出任何新的统计方法、理论结果或实证分析。对于专注于因果推断、高维统计、半参数理论等前沿方法学的研究者而言，这篇书评缺乏技术深度和新颖性。它更像是一篇面向教学或初学者的推荐，而非研究贡献。
- **为什么对您有用**: 本文是一篇书评，属于教学或科普性质，不涉及任何具体的研究方法或理论进展。它与研究者的主要兴趣（因果推断、高维统计、半参数理论等）和次要兴趣（天体统计、经济理论、流行病学）均无直接关联。研究者无需阅读全文，因为其中不包含可迁移的技术工具或值得深入分析的数据集。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

