# Technometrics — Vol 67  Issue 4  ·  2026-07-13

- 共 18 篇 · Technometrics
- 目录核对 ✅ 18 篇全部抓到（对照 OpenAlex 18 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Technometrics》第67卷第4期的18篇论文可归纳为三条主线：**因果推断与实验设计**（网络A/B测试的rerandomization、响应曲面设计、顺序-因子析因设计）、**统计计算与优化**（分数交叉验证、黑箱模拟器的贝叶斯优化、时序网络影响力最大化的贝叶斯优化）、以及**高维/结构化数据建模与监控**（张量图LASSO的在线监控、多元函数控制图、空间方向数据回归、单元级离群值检测、贝叶斯变点检测）。此外，还有若干书评和奖项公告，不涉及方法论贡献。

在**因果推断与实验设计**主线上，最突出的是《Rerandomization Algorithms for Optimal Designs of Network A/B Tests》，它针对网络干扰下的处理效应估计，通过rerandomization框架逼近最优设计，推导了随机化设计向量的渐近分布，为网络实验设计提供了可操作的算法工具。同属实验设计方向的《Optimal Response Surface Designs for Detection and Minimization of Model Contamination》和《Optimal Designs for Order-of-Addition Two-Level Factorial Experiments》分别从模型误设定下的偏差-方差权衡和顺序-因子联合优化角度推进了经典设计理论，前者引入了多组分最优性准则，后者提出了强双正交阵列。

**统计计算与优化**主线中，《Fractional Cross-Validation for Optimizing Hyperparameters of Supervised Learning Algorithms》利用层次高斯过程模型捕捉跨折和跨超参数的相关结构，仅需单折误差即可高效定位最优超参数，显著降低K折CV的计算成本。《Targeted Variance Reduction: Effective Bayesian Optimization of Black-Box Simulators with Noise Parameters》针对控制-噪声交互的随机优化问题，提出了联合采集函数直接缩减目标函数方差，并给出了闭式解和归一化流扩展。《BOPIM: Bayesian Optimization for Influence Maximization on Temporal Networks》则将贝叶斯优化应用于组合空间上的影响力最大化，设计了海明距离和Jaccard系数两种高斯过程核，在速度上大幅超越贪心算法。

**高维/结构化数据建模与监控**主线中，《Real-Time Monitoring of Dynamic Tensor Data with Longitudinal Patterns: A Tensor Graphical LASSO Approach》将张量图LASSO与Cholesky分解、EWMA控制图结合，实现了对动态张量序列的在线异常检测。《An Adaptive Multivariate Functional Control Chart》通过组合不同参数下Hotelling T²型检验的p值，自适应地适应未知的失控分布，提升了多元函数型过程监控的检测能力。《Spatial von-Mises Fisher Regression for Directional Data》和《Cellwise Outlier Detection in Heterogeneous Populations》分别处理了空间方向数据的回归和异质性总体中的单元级离群值检测，前者采用vMF分布与空间自回归，后者在高斯混合模型框架下将污染元素视为缺失值进行插补。

与**因果推断**方向最贴的是《Rerandomization Algorithms for Optimal Designs of Network A/B Tests》；与**半参数/非参数效率**方向相关的是《Factor Importance Ranking and Selection Using Total Indices》，它建立了内在重要性与总Sobol指数的等价性，给出了无需模型假设的一致估计量；与**高维统计**方向相关的是《Real-Time Monitoring of Dynamic Tensor Data with Longitudinal Patterns: A Tensor Graphical LASSO Approach》和《Cellwise Outlier Detection in Heterogeneous Populations》。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1080/00401706.2025.2505438](https://doi.org/10.1080/00401706.2025.2505438) — Rerandomization Algorithms for Optimal Designs of Network A/B Tests
- **作者**: Qiong Zhang
- **期刊/来源**: Technometrics
- **机构**: Clemson University
- **分类**: vol 67 · issue 4 · pp 655-668
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究网络A/B测试中的最优设计问题，目标是在用户存在社交网络连接且响应可能受邻居影响（网络相关结果或网络干扰）的设定下，最小化处理效应估计量的方差。作者基于常用的结果模型（如线性模型含网络效应）推导出最优设计准则，该准则依赖于随机设计向量的几个关键统计量（如处理分配在特征向量上的投影）。核心贡献是提出一个rerandomization框架：通过算法生成满足这些统计量特定条件的随机化设计，并推导了这些统计量的渐近分布以指导算法参数设定。方法上，rerandomization通过拒绝不满足条件的分配方案来逼近最优设计，而非直接求解组合优化问题。仿真和真实网络数据验证了算法有效性。对您而言，本文属于因果推断中网络干扰（network interference）这一子方向，与您的primary interest直接相关；您可以用非参数统计和M估计理论来审视其设计准则的稳健性，或将其rerandomization思路与您熟悉的higher-order U-statistics计算框架结合，分析更复杂网络结构下的最优分配。
- **关键技术**: `rerandomization`, `network A/B testing`, `network interference`, `optimal experimental design`, `asymptotic distribution of design statistics`
- **为什么对您有用**: 本文直接切入因果推断中的网络干扰问题，是您primary interest的子方向。您武器库中的非参数统计和M估计理论可用于检验其设计准则在模型误设下的稳健性；而rerandomization算法的计算成本（如拒绝率与网络规模的关系）恰好可以用您熟悉的higher-order U-statistics的treewidth/einsum复杂度视角来分析——这是一个中期可做的方向，需先在moderately_familiar的identification theory上补足网络干扰的识别假设。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1080/00401706.2025.2483531](https://doi.org/10.1080/00401706.2025.2483531) · [arXiv](https://arxiv.org/abs/2401.00800) — Factor Importance Ranking and Selection Using Total Indices
- **作者**: Chaofan Huang, V. Roshan Joseph
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 573-589
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究因子重要性度量问题，聚焦于 Williamson 等人提出的内在重要性（intrinsic importance），即移除某因子后预测潜力的损失。作者发现预测潜力与全局敏感性分析中的总 Sobol 指数等价，从而绕过了现有估计器所需的建模步骤。基于此等价性，提出一种无需模型假设、可直接从含噪数据中计算的一致估计量。将该估计量与前向选择和后向消除结合，得到 FIRST（Factor Importance Ranking and Selection using Total indices）方法。大量模拟实验表明，FIRST 在回归和二分类问题上优于现有方法。本文对您可能有用：它连接了非参数统计中的敏感性分析与因果推断中的变量重要性度量，且其模型-free 估计量思路可迁移至您熟悉的非参数统计和估计理论。
- **关键技术**: `total Sobol' indices`, `predictiveness potential`, `model-free consistent estimator`, `forward selection`, `backward elimination`
- **为什么对您有用**: 本文直接连接您的非参数统计兴趣，特别是全局敏感性分析与变量重要性度量的交叉点。技术武器库中'非参数统计'和'估计理论'可直接用于分析其估计量的一致性和收敛速率，属于立即可做的范畴。此外，其模型-free 思路对因果推断中的变量选择问题有启发，可中期探索与您 moderately_familiar 的识别理论的结合。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1080/00401706.2025.2491362](https://doi.org/10.1080/00401706.2025.2491362) — Real-Time Monitoring of Dynamic Tensor Data with Longitudinal Patterns: A Tensor Graphical LASSO Approach
- **作者**: Wendong Li, Yifan Li, Fugee Tsung, Chunjie Wu
- **期刊/来源**: Technometrics
- **机构**: East China Normal University · Nanjing Audit University · Shanghai University of Finance and Economics · Hong Kong University of Science and Technology · University of Hong Kong
- **分类**: vol 67 · issue 4 · pp 590-602
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对动态张量数据的实时监控问题，提出了一种基于张量图LASSO的在线监控方法。研究设定为：每个个体过程产生一个张量观测序列，时间作为张量的一个模式，目标是检测纵向行为中的异常。方法的核心机制分为两步：Phase I中，利用张量图LASSO估计in-control参数，同时处理稀疏性和高维挑战；Phase II中，通过Cholesky分解对张量过程进行去趋势和去时间相关，然后基于EWMA控制图进行实时监控。技术工具包括张量图LASSO、Cholesky分解、EWMA控制图。模拟和香港地铁客流数据验证了方法的有效性。对您而言，本文展示了张量结构在统计过程监控中的实际应用，其张量图LASSO估计与您熟悉的张量计算（einsum/treewidth）有潜在联系，可作为统计计算与高维张量方法交叉的入门阅读。
- **关键技术**: `tensor graphical LASSO`, `Cholesky decomposition`, `EWMA control chart`, `dynamic tensor`, `sparsity regularization`
- **为什么对您有用**: 本文属于统计计算与高维张量方法的交叉应用，连接您的stat_computing兴趣。您的very_familiar武器库中的'computation of higher-order U-statistics (treewidth/tensor contraction/einsum)'可直接用于分析张量图LASSO的估计计算复杂度，例如通过einsum视角优化其迭代算法。作为gateway reading，本文对张量监控问题有清晰的数据和模型描述，适合作为进入张量统计计算方向的入门读物，值得花时间读全文。

### 2. [10.1080/00401706.2025.2515926](https://doi.org/10.1080/00401706.2025.2515926) — Fractional Cross-Validation for Optimizing Hyperparameters of Supervised Learning Algorithms
- **作者**: Suraj Yerramilli, Daniel W. Apley
- **期刊/来源**: Technometrics
- **机构**: Northwestern University
- **分类**: vol 67 · issue 4 · pp 683-692
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对监督学习超参数优化中 K 折交叉验证计算成本过高的问题，提出了一种高效的贝叶斯优化算法。核心创新在于利用不同超参数配置下单折验证误差之间的成对相关性，引入层次高斯过程模型来捕捉跨折和跨超参数空间的固有相关结构。该算法仅需对多数超参数配置评估单折误差（称为“分数交叉验证”），即可高效定位最优超参数，大幅减少完整 K 折 CV 所需的计算量。方法在多个模型和真实数据集上验证了有效性。对您而言，本文属于统计计算方向，其利用相关结构降低计算成本的思路，与您对统计计算（数值方法、算法）的兴趣直接相关。
- **关键技术**: `Bayesian optimization`, `hierarchical Gaussian process`, `K-fold cross-validation`, `fractional cross-validation`, `hyperparameter tuning`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。您武器库中“software development”和“high-dimensional asymptotics”可用于理解其高斯过程建模和相关性结构，但核心的贝叶斯优化框架属于您 moderately_familiar 之外的领域。**中期可做**：需先在 moderately_familiar 中“M-estimation theory”上长肌肉，以理解其优化收敛性分析。

### 3. [10.1080/00401706.2025.2495298](https://doi.org/10.1080/00401706.2025.2495298) — Targeted Variance Reduction: Effective Bayesian Optimization of Black-Box Simulators with Noise Parameters
- **作者**: John J. Miller, Simon Mak
- **期刊/来源**: Technometrics
- **机构**: Duke University · United States Department of Energy
- **分类**: vol 67 · issue 4 · pp 617-631
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究黑箱模拟器在控制参数 x 和噪声参数 θ 下的随机优化问题，目标是最小化 E[f(x,Θ)]，其中 Θ 服从已知分布 P。现有贝叶斯优化方法通常采用两阶段策略，分别用不同采集函数选择 x 和 θ，未能充分利用控制-噪声交互。作者提出 Targeted Variance Reduction (TVR) 方法，其核心是联合采集函数，直接针对目标函数在期望改进区域内的方差进行缩减。在平方指数核高斯过程代理模型下，TVR 采集函数具有闭式解，并揭示了探索-利用-精度三者的权衡。TVR 通过归一化流处理非高斯分布 P，扩展了适用性。数值实验和汽车刹车盘稳健设计案例表明 TVR 优于现有方法。对您而言，本文的联合采集函数设计和方差缩减思路可迁移到因果推断中处理不确定协变量或工具变量的优化问题，属于统计计算与算法设计方向。
- **关键技术**: `Bayesian optimization`, `Gaussian process surrogate`, `acquisition function`, `variance reduction`, `normalizing flows`, `robust design`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。TVR 方法中的联合采集函数设计思路可启发您在因果推断中处理带有不确定性的协变量或工具变量时的优化策略。武器库中 'software development' 和 'nonparametric statistics' 足以支撑理解其 GP 代理和归一化流实现，属于**立即可做**的阅读范畴。

## 其他  *(other, 13 篇)*

### 1. [10.1080/00401706.2025.2497822](https://doi.org/10.1080/00401706.2025.2497822) · [arXiv](https://arxiv.org/abs/2409.07881) — Cellwise Outlier Detection in Heterogeneous Populations
- **作者**: Giorgia Zaccaria, Luis A. García-Escudero, Francesca Greselin, Agustín Mayo-Íscar
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 643-654
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对异质性总体中的单元级离群值检测问题，提出了一种基于高斯混合模型的单元级离群值检测方法。传统方法通常将包含离群值的整个观测单元（行）剔除，但可能丢失其他特征中的有效信息。本文遵循单元级污染范式，在EM算法中增加一个步骤来标记数据矩阵中被污染的元素，并将其视为缺失值进行插补而非直接丢弃。该方法通过EM算法同时进行聚类、离群值检测和缺失值插补。模拟研究在不同场景下与现有方法进行了比较，并在三个真实数据集上展示了其在聚类、离群值检测和插补方面的潜力。该方法可应用于社会经济研究、环境分析和医疗健康等领域。
- **关键技术**: `Gaussian mixture model`, `Expectation-Maximization (EM) algorithm`, `cellwise contamination`, `missing data imputation`, `robust clustering`
- **为什么对您有用**: 本文属于统计计算与稳健方法领域，与您的主要兴趣（统计计算、高维统计）有间接关联，但核心问题（单元级离群值检测）与您的因果推断、半参理论等主要研究方向交集有限。武器库中的非参数统计和M估计理论可用于分析其稳健性，但整体上属于方法学应用，而非理论突破。暂不可做：核心机器（单元级污染模型、EM插补）不在武器库中，且与您的主要研究方向距离较远。

### 2. [10.1080/00401706.2025.2519303](https://doi.org/10.1080/00401706.2025.2519303) · [arXiv](https://arxiv.org/abs/2207.08321) — Spatial von-Mises Fisher Regression for Directional Data
- **作者**: Zhou Lan, Arkaprava Roy, For The Alzheimer’s Disease Neuroimaging Initiative
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 706-715
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对空间方向数据（如脑纤维方向）提出一种新的广义线性模型，假设响应变量服从 von Mises-Fisher (vMF) 分布，并通过 Cartesian 与球坐标之间的变换构造链接函数，将方向数据回归到外部协变量上。模型引入自回归结构刻画空间依赖性，兼顾计算效率与灵活性。作者开发了一套完整的贝叶斯推断工具，包括先验设定、后验采样和模型比较。在 ADNI 脑纤维数据上的应用揭示了认知障碍与纤维方向之间的新关联，模拟实验验证了方法的经验有效性。该方法填补了协变量依赖的方向数据分析的空白，但对您而言，其统计框架（vMF 回归 + 空间自回归）与您的主要兴趣方向（因果推断、高维、U-统计量）无直接交集，且方法学 novelty 主要体现在应用建模而非理论突破。
- **关键技术**: `von Mises-Fisher distribution`, `spatial autoregressive model`, `Bayesian inference`, `link function via coordinate transformation`
- **为什么对您有用**: 本文属于方向数据建模的应用工作，与您的主要兴趣（因果推断、高维统计、U-统计量、效率理论）无直接关联。作为流行病学应用，它使用了 ADNI 数据，但方法学核心（vMF 回归 + 空间自回归）并非您武器库中的工具，且未涉及 identification、semiparametric efficiency 或高维推断。暂不可做——核心机器（方向数据建模、空间贝叶斯）不在您的武器库中，且无明显的统计-计算权衡或高阶 U-统计量连接。

### 3. [10.1080/00401706.2025.2515928](https://doi.org/10.1080/00401706.2025.2515928) · [arXiv](https://arxiv.org/abs/2401.02917) — Bayesian Changepoint Detection via Logistic Regression and the Topological Analysis of Image Series
- **作者**: Andrew M. Thomas, Michael Jauch, David S. Matteson
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 693-705
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种贝叶斯多元变点检测方法 BCLR，将变点位置与区分变点前后数据的逻辑回归系数联合建模，适用于混合类型数据且不要求数据分布或变化形式的严格假设。模型通过 Pólya-gamma 数据增广实现简单的 Gibbs 采样后验推断，并给出了变点恢复的相合性条件。方法结合拓扑特征嵌入（如持久同调）用于图像序列的拓扑变化检测，在模拟和真实图像数据上表现良好，也在传统变点任务中有效。BCLR 的 Python 包已开源。对您而言，本文属于统计计算与贝叶斯方法的交叉应用，与您的主要兴趣（因果推断、高维统计）无直接重叠，但变点检测在纵向因果推断中可能作为预处理步骤（如识别干预时间点），且 Gibbs 采样与 Pólya-gamma 增广是统计计算中可借鉴的技术。
- **关键技术**: `Bayesian changepoint detection`, `Pólya-gamma data augmentation`, `Gibbs sampling`, `logistic regression`, `topological data analysis`, `persistent homology`
- **为什么对您有用**: 本文属于统计方法应用，与您的主要兴趣（因果推断、高维统计）无直接重叠，但变点检测在纵向因果推断中可作为预处理步骤（如识别干预时间点）。您的武器库中 'nonparametric statistics' 和 'software development' 可用于复现或扩展其方法，但核心贝叶斯推断与拓扑数据分析不在您的 very_familiar 列表中，因此暂不可做——需先熟悉 Pólya-gamma 增广和持久同调工具。

### 4. [10.1080/00401706.2025.2495302](https://doi.org/10.1080/00401706.2025.2495302) — Optimal Response Surface Designs for Detection and Minimization of Model Contamination
- **作者**: Olga Egorova, Steven G. Gilmour
- **期刊/来源**: Technometrics
- **机构**: King's College London
- **分类**: vol 67 · issue 4 · pp 632-642
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在响应曲面设计框架下，针对模型误设定（如遗漏高阶多项式项）的风险，提出了一个多组分最优性准则。该准则同时优化三个目标：(i) 基于置信区间的推断质量；(ii) 检测模型拟合不足（lack-of-fit）的能力，通过引入新开发的检验分量实现；(iii) 最小化因模型误设定导致的参数估计的方差与偏差。后两个分量采用与模型无关的“纯误差”方法进行误差估计，并扩展至区组实验设计。通过点交换算法搜索近似最优设计，并结合真实与模拟案例展示了各目标间的权衡关系。对您而言，本文属于实验设计领域的方法学工作，与您的主要兴趣（因果推断、高维统计等）无直接交集，但其中关于模型误设定下偏差-方差权衡的量化思路，对敏感性分析中的模型稳健性评估有一定启发。
- **关键技术**: `response surface design`, `multiple-component optimality criterion`, `lack-of-fit test`, `pure error estimation`, `point-exchange algorithm`
- **为什么对您有用**: 本文属于实验设计领域，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接连接。其核心贡献在于响应曲面设计中的多目标优化，而非您关注的统计推断或计算理论。作为应用统计方法论文，它不涉及您武器库中的具体工具（如非参极小极大界、高阶U-统计量树宽等），因此暂不可做。

### 5. [10.1080/00401706.2025.2520849](https://doi.org/10.1080/00401706.2025.2520849) — Optimal Designs for Order-of-Addition Two-Level Factorial Experiments
- **作者**: Qiang Zhao, Qian Xiao, Abhyuday Mandal, Fasheng Sun
- **期刊/来源**: Technometrics
- **机构**: Northeast Normal University · Shanghai Jiao Tong University · University of Georgia
- **分类**: vol 67 · issue 4 · pp 716-724
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究一类新型实验设计——顺序-因子两水平析因实验，旨在同时优化药物成分的添加顺序和剂量水平。在复合模型下，现有最优设计为双正交阵列（DOA），但其构造灵活度有限。作者提出一种理论引导的搜索方法，可高效构造任意可行规模的DOA，并给出一种代数构造法直接生成特定DOA。针对DOA忽略交互效应的潜在问题，进一步提出强双正交阵列（SDOA），在扩展复合模型下达到最优，并提供两种代数构造方法。理论结果证明了DOA和SDOA的最优性，数值实验展示了所提设计的优越性。该工作属于实验设计领域，与您的主要兴趣（因果推断、高维统计等）无直接方法学交叉，但若您未来涉及多因素序贯干预的因果实验设计，其正交阵列思想可能提供参考。
- **关键技术**: `dual-orthogonal arrays`, `strong dual-orthogonal arrays`, `compound model`, `theory-guided search`, `algebraic construction`
- **为什么对您有用**: 本文属于实验设计（design of experiments）领域，与您的主要兴趣（因果推断、高维统计、半参理论）无直接方法学重叠。但若您未来研究涉及序贯多因素干预的因果实验（如药物组合的时序优化），其正交阵列构造思想可能提供设计层面的启发。目前武器库中无直接可攻工具，暂不可做。

### 6. [10.1080/00401706.2025.2505483](https://doi.org/10.1080/00401706.2025.2505483) · [arXiv](https://arxiv.org/abs/2308.04700) — BOPIM: Bayesian Optimization for Influence Maximization on Temporal Networks
- **作者**: Eric Yanchenko
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 669-682
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究时序网络上的影响力最大化（IM）问题，目标是在给定预算下选择种子节点集合以最大化影响力传播。作者提出 BOPIM，一种基于贝叶斯优化（BO）的算法，将 IM 视为黑箱昂贵函数优化问题。核心挑战在于输入空间是基数约束的非欧几里得组合空间。为此，作者设计了两种高斯过程核函数：基于海明距离的核和基于 Jaccard 系数的核；并使用期望改进（EI）作为采集函数，通过贪心算法处理基数约束。在真实网络上的数值实验表明，BOPIM 在影响力传播上与黄金标准贪心算法相当，但速度提升可达 10 倍；海明核在多数设定下优于 Jaccard 核。此外，该方法首次量化了最优种子集的不确定性。本文属于应用导向的方法论文，方法学新颖性有限（novelty_flag: application），但为统计计算中的组合优化问题提供了 BO 框架的实例。
- **关键技术**: `Bayesian optimization`, `Gaussian process regression`, `Hamming kernel`, `Jaccard kernel`, `expected improvement`, `greedy algorithm`
- **为什么对您有用**: 本文属于统计计算中的算法设计，但核心问题（组合空间上的 BO）与您的主要兴趣（统计计算、算法）仅有弱关联。您的武器库中非常熟悉的非参数统计和软件工程可用于复现或扩展其 BO 框架，但 IM 问题本身与您的因果推断、高维统计等核心方向无直接交集。作为 gateway reading，本文对统计计算方向的新手友好，但方法学深度一般，暂不可做——核心缺失在于组合空间上的 BO 理论（如核函数设计对收敛性的影响）不在您的武器库中。

### 7. [10.1080/00401706.2025.2491369](https://doi.org/10.1080/00401706.2025.2491369) · [arXiv](https://arxiv.org/abs/2504.09684) — An Adaptive Multivariate Functional Control Chart
- **作者**: Fabio Centofanti, Antonio Lepore, Biagio Palumbo
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 603-616
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出自适应多元函数控制图（AMFCC），用于监控多元函数型质量特性的过程稳定性。传统方法在参数选择上依赖已知的失控（OC）分布信息，而AMFCC通过组合不同参数组合下Hotelling T²型部分检验的p值，自适应地适应未知的OC分布。通过蒙特卡洛模拟，与现有方法比较，AMFCC在检测能力上表现更优。案例研究应用于汽车工业的电阻点焊过程监控。该方法已实现为R包funcharts。对您而言，本文属于统计过程控制的应用领域，与您的主要兴趣方向（因果推断、高维统计等）关联较弱，但函数型数据分析方法可能对您处理纵向数据或高维曲线数据有间接启发。
- **关键技术**: `functional data analysis`, `Hotelling T² statistic`, `p-value combination`, `adaptive monitoring`, `multivariate control chart`
- **为什么对您有用**: 本文属于统计过程控制的应用，与您的主要兴趣（因果推断、高维统计、半参理论）关联较弱。武器库中的非参数统计和软件工程经验可辅助理解函数型数据方法，但核心问题（过程监控）与您的方向差异较大。暂不可做：缺乏函数型数据分析和统计过程控制的专门工具。

### 8. [10.1080/00401706.2025.2565978](https://doi.org/10.1080/00401706.2025.2565978) — Just Enough Data Science and Machine Learning
- **作者**: Fahmi Nugraha Heryanto, Zulfaidil Zulfaidil
- **期刊/来源**: Technometrics
- **机构**: Australian Regenerative Medicine Institute · Monash University · Bandung Institute of Technology
- **分类**: vol 67 · issue 4 · pp 731-733
- 相关性 0/10 · novelty: `survey`
- **摘要**: 这是一篇书评，评论一本名为《Just Enough Data Science and Machine Learning》的教材。该书旨在为初学者提供数据科学和机器学习的入门知识，涵盖基本概念、方法和工具。书评指出，该书内容全面但深度有限，适合作为非技术背景读者的快速入门读物。书评本身没有提出新的统计方法或理论贡献。对于您这样专注于因果推断、高维统计和效率理论的研究者，这篇书评没有直接的技术价值。
- **为什么对您有用**: 这是一篇书评，不涉及具体统计方法或理论。与您的任何研究方向（因果推断、高维统计、U统计量、半参数理论等）均无直接关联。不推荐阅读。

### 9. [10.1080/00401706.2025.2561534](https://doi.org/10.1080/00401706.2025.2561534) — The 2024 <i>Technometrics</i> Prizes
- **作者**: 
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 734-737
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是《Technometrics》期刊2024年奖项公告，公布了Jack Youden奖（最佳阐述性论文）和Frank Wilcoxon奖（最佳应用性论文）的获奖者及入围名单。获奖论文涉及统计过程控制、数据融合、计算机实验设计等应用统计领域。文章仅列出获奖者姓名、论文标题及简短引用，不包含任何方法学贡献或理论结果。对您而言，这是一则期刊新闻，不涉及因果推断、高维统计、半参数理论或计算统计等您的主要研究方向，无需深入阅读。
- **为什么对您有用**: 本文为期刊奖项公告，不涉及具体统计方法或理论，与您的主要研究兴趣（因果推断、高维统计、半参数理论等）无直接关联。无需投入时间阅读。

### 10. [10.1080/00401706.2025.2565977](https://doi.org/10.1080/00401706.2025.2565977) — The Polls Weren’t Wrong
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 730-731
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是一篇书评，讨论如何正确解读民意调查结果。作者强调民意调查是抽样统计工具，旨在提供有意义的总体估计，而非精确预测。书中可能涉及抽样误差、非抽样误差、加权调整等经典调查统计方法。文章指出公众常误解民调的不确定性，将置信区间误读为预测失败。本书适合作为调查统计学的入门读物，帮助非专业人士理解抽样推断的基本逻辑。对您而言，这是一篇非技术性书评，与您的主要研究方向（因果推断、高维统计等）无直接关联。
- **关键技术**: `survey sampling`, `confidence intervals`, `non-sampling error`
- **为什么对您有用**: 本文属于书评，不涉及您核心兴趣中的任何具体子方向（如proximal CI、RMT、higher-order U-statistics等）。武器库中的工具无法直接应用于本文内容。建议跳过，无需阅读全文。

### 11. [10.1080/00401706.2025.2565974](https://doi.org/10.1080/00401706.2025.2565974) — Bayesian Inference: Theory, Methods, and Computations
- **作者**: Kazuhiko Kakamu, Shuangzhe Liu
- **期刊/来源**: Technometrics
- **机构**: Nagoya City University · University of Canberra
- **分类**: vol 67 · issue 4 · pp 728-729
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是一篇书评，介绍Silvelyn Zwanzig和Rauf Ahmad所著的《Bayesian Inference: Theory, Methods, and Computations》教科书。该书评概述了教材内容，包括贝叶斯推断的理论基础、计算方法（如MCMC）以及实际应用。书评指出该书适合作为研究生教材，兼顾严谨性与可读性。对于研究者而言，这是一篇信息性书评，而非原创方法论贡献。
- **关键技术**: `Bayesian inference`, `MCMC`
- **为什么对您有用**: 本文为书评，不涉及原创方法或理论。与您的主要研究兴趣（因果推断、高维统计、U统计量等）无直接关联。若您对贝叶斯方法入门感兴趣，可作为参考读物，但无需深入阅读。

### 12. [10.1080/00401706.2025.2565973](https://doi.org/10.1080/00401706.2025.2565973) — Natural Language Processing in the Real World: Text Processing, Analytics, and Classification
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 726-728
- 相关性 0/10 · novelty: `survey`
- **摘要**: 这是一篇书评，评述了《Natural Language Processing in the Real World: Text Processing, Analytics, and Classification》一书。该书属于数据科学系列，主要介绍自然语言处理（NLP）在数据科学和机器学习中的现代方法，涵盖文本处理、分析和分类。书评概述了书籍的内容结构和覆盖范围，但未提供具体的技术细节或方法论贡献。作为一篇书评，它没有提出新的理论、方法或实证结果。对于您的研究兴趣（因果推断、高维统计、半参数理论等），NLP 并非直接相关领域，且书评本身缺乏可迁移的技术深度。因此，本文仅作为一般性信息参考，不涉及您核心或次要兴趣中的具体子方向。
- **为什么对您有用**: 本文是一篇书评，不涉及具体方法论或实证研究，与您的主要兴趣（因果推断、高维统计、半参数理论等）和次要兴趣（天体统计、经济理论、流行病学）均无直接关联。武器库中的工具无法应用于本文。暂不可做。

### 13. [10.1080/00401706.2025.2565972](https://doi.org/10.1080/00401706.2025.2565972) — Soccer Analytics: An Introduction Using R
- **作者**: Stan Lipovetsky
- **期刊/来源**: Technometrics
- **分类**: vol 67 · issue 4 · pp 725-726
- 相关性 0/10 · novelty: `survey`
- **摘要**: 这是一篇书评，介绍《Soccer Analytics: An Introduction Using R》一书。该书属于数据科学系列，用现代统计方法描述足球比赛（欧洲足球）。全书共11章，涵盖数据来源、探索性分析、模型构建等。书评指出该书适合对体育分析感兴趣的读者，但未深入讨论具体统计方法或理论贡献。对您而言，这是一本入门级应用书籍，与您的主要研究方向（因果推断、高维统计、半参理论等）无直接关联。
- **为什么对您有用**: 本文是书评，非原创研究。与您的主要兴趣（因果推断、高维统计、半参理论等）无直接关联。作为应用领域（体育分析）的入门读物，但未提供新的统计方法或理论。武器库中的工具无法直接应用于此。暂不可做。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

