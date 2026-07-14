# Stat. Comput. — Vol 35  Issue 6  ·  2026-07-14

- 共 15 篇 · Statistics and Computing
- 目录核对 ⚠️ 疑似漏 38 篇（对照 OpenAlex 53 篇）：10.1007/s11222-025-10721-8、10.1007/s11222-025-10708-5、10.1007/s11222-025-10706-7、10.1007/s11222-025-10689-5、10.1007/s11222-025-10683-x 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Stat. Comput. 第 35 卷第 6 期的 15 篇论文可归纳为三条主线：**统计计算与算法加速**（并行 MCMC、自适应分层、随机化谱聚类、选逆方法）、**高维计数数据建模**（零膨胀泊松对数正态、混合因子分析、迁移学习推断）、以及**非参数与函数型方法**（自适应 P 样条、核密度有效自由度、协变量依赖集成）。此外，时空突变点检测、网络边数据多尺度分解、ABC 随机森林、分类一致性显著性检验等主题分散于各主线。

在统计计算主线中，多篇论文聚焦于并行与自适应策略的误差控制。Parallel Selected Inversion for Space-Time GMRF 用区域分解混合 Krylov 与直接法加速稀疏精度矩阵求逆；A non-asymptotic error analysis for parallel Monte Carlo estimation from many short Markov chains 给出多短链估计量的非渐近误差界；Adaptive stratified Monte Carlo using decision trees 通过决策树自适应划分区域实现方差缩减，在高维积分中达到超标准 MC 的收敛速率。Randomized Spectral Clustering for Large-Scale Multi-Layer Networks 将随机采样与投影结合，在百万节点多层网络上保持社区检测精度。Bayesian parameter estimation for partially observed McKean-Vlasov diffusions using multilevel MCMC 则用多层蒙特卡洛将计算成本降低一个数量级。

高维计数数据建模主线以泊松-对数正态（PLN）族为核心。Zero-inflation in the multivariate Poisson lognormal family 引入伯努利潜变量处理零膨胀，用变分推断在 90% 零占比下仍有效；Finite mixtures of multivariate Poisson-log normal factor analyzers for clustering count data 通过因子分析降维，构建八种协方差结构的混合模型用于 RNA-seq 聚类。Post-transfer learning statistical inference in high-dimensional regression 则从迁移学习角度，用分割-条件推断在目标域样本有限时提供精确 p 值，控制假阳性率。

与因果推断 / 半参数效率方向最贴的论文包括：Post-transfer learning statistical inference in high-dimensional regression（迁移学习下的高维推断，条件检验框架）、The effective number of parameters in kernel density estimation（非参数有效自由度，可关联 AIC 带宽选择）、Adaptive Generalized P-Splines for Functional Data（自适应节点选择，条件数感知）。此外，Ensemble Prediction via Covariate-dependent Stacking 的 Oracle 不等式分析对集成学习理论有参考价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1007/s11222-025-10738-z](https://doi.org/10.1007/s11222-025-10738-z) · [arXiv](https://arxiv.org/abs/2504.18212) — Post-transfer learning statistical inference in high-dimensional regression
- **作者**: Nguyen Vu Khai Tam, Cao Huyen My, Vo Nguyen Le Duy
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究迁移学习（TL）下高维回归（HDR）的统计推断问题。目标是在目标域样本量有限、借助源域数据做特征选择后，对所选特征与响应变量的关系提供有效的p值，控制假阳性率（FPR）。核心贡献PTL-SI框架基于分割-条件推断（split-and-conditional inference）思路：先用源域数据筛选候选特征集，再在目标域保留样本上构造条件检验，得到精确有限样本p值。该方法不依赖渐近正态近似，而是利用截断高斯分布的条件分布性质进行精确推断。为提升统计功效，论文引入分治策略（divide-and-conquer），将目标域数据多次随机分割后合并检验结果。实验在合成数据和真实高维数据集上验证了FPR控制和功效。对您而言，该工作将高维回归的post-selection inference推广到迁移学习场景，其条件推断框架可与您熟悉的非参数统计和因果推断中的sensitivity analysis思路对接，中期可做的是将类似条件检验思想引入proximal causal inference的变量选择后推断。
- **关键技术**: `post-selection inference`, `conditional inference`, `truncated Gaussian distribution`, `split-and-conquer`, `transfer learning`, `high-dimensional regression`
- **为什么对您有用**: 直接连接您的高维统计与假设检验兴趣：post-selection inference是高维回归后推断的核心问题，本文将其拓展到迁移学习设定。技术武器库中'非参数统计'和'高维渐近理论'可直接用于理解其条件推断框架的有限样本性质。中期可做：将类似的条件检验思路引入您熟悉的因果推断中的变量选择后推断（如proximal CI中的negative control筛选后检验），这需要先在'moderately_familiar'的identification theory上巩固。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1007/s11222-025-10744-1](https://doi.org/10.1007/s11222-025-10744-1) · [arXiv](https://arxiv.org/abs/2406.14453) — The effective number of parameters in kernel density estimation
- **作者**: Sofia Guglielmini, Igor Volobouev, A. Alexandre Trindade
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对核密度估计（KDE）中的有效自由度（EDoF）提出新公式。从经验密度与 oracle 密度之比的正交多项式序列（OPS）展开出发，证明核卷积导出一个新的 OPS，KDE 可在此新基下表达。两个 OPS 系统的展开系数通过核敏感度矩阵关联，从而通过迹算子给出 oracle EDoF 的自然定义。通过影响函数推导了经验 plug-in EDoF 的渐近性质，并与其它经验 EDoF 建立联系。还研究了最小化 KL 散度作为带宽选择准则，给出新的正态尺度规则。该方法不限于卷积核，并暗示了基于 AIC 的信息准则带宽选择的可能性。对您而言，本文的非参数统计视角与您熟悉的 minimax 界和渐近理论直接相关，且其 OPS 框架可能为高维或半参数问题中的复杂度度量提供新思路。
- **关键技术**: `orthogonal polynomial sequence (OPS) expansion`, `kernel sensitivity matrix`, `influence function`, `effective degrees of freedom (EDoF)`, `Kullback-Leibler divergence bandwidth selection`
- **为什么对您有用**: 本文直接连接您的 primary interest 中的非参数统计与渐近理论，具体涉及 KDE 的模型复杂度度量。您的 very_familiar 武器库中的非参数统计和 minimax 界可用于验证其 EDoF 公式的紧性，或扩展至高维设定。中期可做：需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以处理其影响函数推导的泛化。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1007/s11222-025-10728-1](https://doi.org/10.1007/s11222-025-10728-1) · [arXiv](https://arxiv.org/abs/2504.15325) — Significativity Indices for Agreement Values
- **作者**: Alberto Casagrande, Francesco Fabris, Rossano Girometti, Roberto Pagliarini
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出了一种评估分类器间一致性指标（如Cohen's kappa、组内相关系数）显著性的通用框架。核心创新在于定义“显著性指数”（significativity index），即从同一数据集上随机生成混淆矩阵并得到更低一致性值的概率，以此替代传统主观划分的质量等级。作者分别针对有限数据集和分类概率分布两种情况设计了两种显著性指数，并给出了高效的计算算法。该方法不替代原有的一致性度量，而是为其提供统计显著性参考，避免了现有质量量表边界任意的问题。理论部分证明了指数在随机混淆矩阵下的概率性质，计算部分则利用组合优化和动态规划降低枚举复杂度。模拟和真实医学影像数据实验表明，该指数能有效区分不同分类器的一致性水平，且对样本量变化稳健。对您而言，该工作将假设检验思想引入一致性评估，其概率框架和计算策略可迁移至因果推断中敏感性分析或高维U统计量的显著性检验问题。
- **关键技术**: `significativity index`, `confusion matrix permutation`, `Cohen's kappa`, `intraclass correlation`, `combinatorial optimization`, `dynamic programming`
- **为什么对您有用**: 本文直接关联您对假设检验的兴趣，其核心思想——通过随机化构造零分布来评估观测值的显著性——是经典统计推断的变体。技术层面，您武器库中的“higher-order U-statistics (treewidth / tensor contraction / einsum)”可用来分析其计算复杂度：显著性指数的计算本质上是对混淆矩阵空间上的枚举或采样，其树宽结构可能决定精确计算的可行性，这与您熟悉的U统计量计算问题同构。中期可做：若想将类似框架推广到连续型一致性度量（如ICC），需先在moderately_familiar的“semiparametric theory”上提升，以处理非参数零分布构造。

## 统计计算 / 算法  *(stat_computing, 12 篇)*

### 1. [10.1007/s11222-025-10729-0](https://doi.org/10.1007/s11222-025-10729-0) · [arXiv](https://arxiv.org/abs/2405.14711) — Zero-inflation in the multivariate poisson lognormal family
- **作者**: Bastien Batardière, Julien Chiquet, François Gindraud, Mahendra Mariadassou
- **期刊/来源**: Statistics and Computing
- **机构**: Département mathématiques, informatique, sciences de la donnée et technologies du numérique · Mathématiques et Informatique Appliquées · Laboratoire de Biométrie et Biologie Evolutive · Mathématiques et Informatique Appliquées du Génome à l'Environnement
- **分类**: vol 35 · issue 6
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维计数数据中常见的零膨胀现象，在多元泊松-对数正态（PLN）模型基础上引入零膨胀成分，提出ZIPLN模型。该模型通过一个额外的伯努利潜变量刻画零膨胀机制，允许零膨胀概率为固定、位点特异、特征特异或依赖于协变量。参数估计采用变分推断，比较了两种近似策略：独立高斯与伯努利变分分布，以及以伯努利为条件的高斯变分分布。模拟实验表明，即使在零膨胀比例高达90%时，ZIPLN仍能有效恢复参数。在牛微生物组数据集（零占比90.6%）上的应用显示，考虑零膨胀显著提升了对数似然并降低了潜空间离散度，从而改善了组别判别。本文的方法论贡献在于为高维计数数据提供了一种可扩展的、保留可解释性的统计建模框架，对您在高维统计计算和软件实现方面的兴趣有直接参考价值。
- **关键技术**: `variational inference`, `Poisson-Log-Normal model`, `zero-inflated model`, `latent Gaussian model`, `high-dimensional count data`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您对统计计算（数值方法、算法）的兴趣。其变分推断框架和可扩展性分析可为您在软件开发和算法实现方面提供参考。武器库中'软件发展'和'高维渐近'两项可直接用于评估其计算效率与理论性质，属于'立即可做'的范畴。

### 2. [10.1007/s11222-025-10720-9](https://doi.org/10.1007/s11222-025-10720-9) · [arXiv](https://arxiv.org/abs/2311.07762) — Finite mixtures of multivariate Poisson-log normal factor analyzers for clustering count data
- **作者**: Andrea Payne, Anjali Silva, Steven J Rothstein, Paul D. McNicholas, Sanjeena Subedi
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对高维离散计数数据的聚类问题，提出了一类有限混合的多元泊松-对数正态因子分析模型（MPLNFA）。通过在协方差矩阵上施加因子分析结构约束，将模型参数化到低维潜因子空间，从而在保持灵活性的同时实现降维。参数估计采用变分高斯近似（VGA）来逼近难以处理的后验，模型选择则依赖信息准则（如BIC）。作者构建了包含八种不同协方差结构的简约混合模型族，并重点应用于RNA测序（RNA-seq）数据的聚类分析。模拟和真实数据实验表明，所提模型在聚类准确性和可解释性上优于传统方法（如K-means、高斯混合模型）。配套的R包mixMPLNFA已开源发布，便于复现和扩展。对您而言，本文的变分推断框架和因子分析约束策略可迁移至您熟悉的高维统计与软件工具开发方向，尤其适合作为处理离散数据聚类问题的入门参考。
- **关键技术**: `variational Gaussian approximation`, `factor analysis covariance constraints`, `mixture of factor analyzers`, `Poisson-log normal distribution`, `information criteria model selection`
- **为什么对您有用**: 本文属于统计计算与软件工具方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'和'software development'。您武器库中'very_familiar'的'high-dimensional asymptotics'和'software development'可直接用于评估其变分近似的收敛性及R包的可扩展性；'moderately_familiar'的'M-estimation theory'可用于分析其EM/变分估计的渐近性质。这是一篇方法学应用论文，novelty程度中等，但作为gateway reading，它清晰地展示了变分推断在复杂混合模型中的应用流程，值得花时间读全文以获取离散数据建模的实用技巧。

### 3. [10.1007/s11222-025-10734-3](https://doi.org/10.1007/s11222-025-10734-3) — Adaptive Generalized P-Splines for Functional Data: A Statistical Framework via Blockwise GSVD
- **作者**: Anna De Magistris, Elvira Romano, Rosanna Campagna
- **期刊/来源**: Statistics and Computing
- **机构**: University of Campania "Luigi Vanvitelli"
- **分类**: vol 35 · issue 6
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对函数型数据提出一种自适应广义P样条方法，核心创新在于将条件数感知策略融入节点位置、数量及正则化参数的联合选择。通过重新表述Tikhonov正则化问题，作者设计了一个计算高效的准则，在控制模型复杂度的同时保证数值稳定性。该方法无需均匀或预置节点，而是根据数据局部曲率自适应放置节点，从而在全函数域上提升拟合精度。数值实验表明，该方法在近似误差和矩阵条件数上显著优于传统自由节点样条和光滑样条。对您而言，本文展示了一种将数值线性代数中的条件数分析直接嵌入模型选择流程的实用范式，这与您统计计算方向中关注算法数值稳定性的兴趣高度契合。
- **关键技术**: `generalized P-splines`, `Tikhonov regularization`, `blockwise GSVD`, `conditioning-aware knot selection`, `adaptive knot placement`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。其核心贡献是将条件数（数值稳定性指标）作为模型选择准则的一部分，这与您武器库中 'inverse problems with random noise' 和 'software development' 两项非常熟悉工具直接相关——您可以用已有的逆问题正则化理解来快速评估其条件数准则的通用性，并考虑将其移植到您熟悉的样条或核方法软件中。中期可做：若想将类似条件数感知策略推广到高维或因果推断中的非参数回归，需先在 moderately_familiar 的 M-estimation theory 上补足对惩罚似然框架的理解。

### 4. [10.1007/s11222-025-10731-6](https://doi.org/10.1007/s11222-025-10731-6) · [arXiv](https://arxiv.org/abs/2501.04842) — Adaptive stratified Monte Carlo using decision trees
- **作者**: Nicolas Chopin, Hejin Wang, Mathieu Gerber
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维超立方体 [0,1]^s 上积分的高效蒙特卡洛估计问题，提出一种基于决策树的自适应分层策略。传统分层方法（如 Haber 方法）需要 O(k^s) 个评估点，在 s 较大时不可行。作者利用初步样本拟合决策树来划分区域，使得每个子区域内的被积函数方差较小，从而在后续采样中实现分层。理论分析表明，对于某些函数类（如分段光滑或具有低维结构），该自适应分层估计器可达到 O(N^{-1/2 - r}) 的收敛速率，r>0，优于标准蒙特卡洛的 O(N^{-1/2})。数值实验在 s 高达 20 时仍显示改进效果。该工作属于统计计算中方差缩减技术的范畴，对您作为统计计算方向（特别是数值方法与算法）的入门读物很有价值，因为其核心思想（用决策树自适应捕捉函数结构）与您熟悉的非参数统计和软件工具链有直接联系。
- **关键技术**: `adaptive stratification`, `decision trees`, `variance reduction`, `Monte Carlo integration`, `convergence rate improvement`
- **为什么对您有用**: 本文属于统计计算（stat_computing）中的方差缩减方法，是您 secondary interest 中 'statistical computing (numerical methods, algorithm)' 的 gateway reading。您武器库中 'nonparametric statistics' 和 'software development' 两项 very_familiar 工具可直接用于理解其决策树自适应分层的核心机制，并评估其在实际计算中的实现成本。中期可做：若您想将类似自适应分层思想推广到更复杂的积分问题（如高维 U-统计量的期望计算），需先在 'theory of higher-order U-statistics' 上长肌肉，以分析分层对 U-统计量方差的影响。本文值得花时间读全文，作为进入统计计算方差缩减领域的入门。

### 5. [10.1007/s11222-025-10741-4](https://doi.org/10.1007/s11222-025-10741-4) · [arXiv](https://arxiv.org/abs/2401.17963) — A non-asymptotic error analysis for parallel Monte Carlo estimation from many short Markov chains
- **作者**: Austin Brown
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种多短链蒙特卡洛（MSC）估计量，通过平均多条独立短马尔可夫链的求和来估计期望，从而利用并行计算优势。与单长链MCMC相比，MSC需要精心设计的初始分布（基于重要性采样），但每条链长度有保证，可独立并行运行。作者在几何遍历和乘法漂移条件下给出了MSC估计量的非渐近误差分析，适用于高度不规则和无界函数的估计。数值实验在自回归过程和贝叶斯逻辑回归的Pólya-Gamma Gibbs采样器上验证了性能。该工作为并行MCMC提供了理论保证，对您作为统计计算方向的研究者具有直接参考价值。
- **关键技术**: `many-short-chains Monte Carlo`, `importance sampling initial distribution`, `non-asymptotic error bounds`, `geometric ergodicity`, `multiplicative drift condition`
- **为什么对您有用**: 本文直接关联您的统计计算兴趣，特别是并行MCMC的误差理论。您熟悉的非参数统计和minimax界工具可用于分析其非渐近界的紧性，而软件开发经验可帮助实现MSC估计量。中期可做：需先在MCMC收敛理论（moderately_familiar）上加强，以深入理解几何遍历条件。

### 6. [10.1007/s11222-025-10739-y](https://doi.org/10.1007/s11222-025-10739-y) · [arXiv](https://arxiv.org/abs/2408.09755) — Ensemble Prediction via Covariate-dependent Stacking
- **作者**: Tomoya Wakayama, Shonosuke Sugasawa
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出了一种名为“协变量依赖堆叠”（CDST）的集成预测新方法。与传统的堆叠和模型平均方法不同，CDST 允许模型权重作为协变量的函数灵活变化，从而在复杂场景下提升预测性能。作者通过基函数的组合来参数化协变量依赖的权重，并通过优化交叉验证来估计这些权重。在理论方面，文章建立了关于估计模型权重时最小化期望损失的 Oracle 不等式。通过全面的模拟研究和大规模地价预测应用，CDST 在基模型未能捕捉潜在复杂性的数据集上持续优于传统模型平均方法。该方法特别适用于（但不限于）时空预测问题，为数据科学实践者提供了一个强大的工具。
- **关键技术**: `covariate-dependent stacking`, `model averaging`, `basis function expansion`, `oracle inequality`, `cross-validation optimization`
- **为什么对您有用**: 本文属于统计计算与算法方向，直接关联您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。您武器库中“nonparametric statistics”和“software development”两项非常熟悉，可以立即动手复现其算法并测试其在您关注的因果推断预测任务中的表现。这是一篇方法学论文，值得花时间阅读全文以评估其与您工作的结合点。

### 7. [10.1007/s11222-025-10733-4](https://doi.org/10.1007/s11222-025-10733-4) · [arXiv](https://arxiv.org/abs/2410.13693) — A multiscale method for data collected from network edges via the line graph
- **作者**: Dingjia Cao, Marina I. Knight, Guy P. Nason
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对网络边上的数据（如河流流量）提出了一种多尺度分解方法。传统图信号处理通常假设函数定义在节点上，而本文通过线图（line graph）构造将边数据映射到节点域，从而允许使用已有的节点提升方案。作者开发了 LG-LOCAAT 变换，这是一种第二代小波提升方案，能够沿网络边进行数据分解和去噪。算法性质（如消失矩、预测与更新步骤）被详细分析，并与现有方法（如基于节点的小波、图傅里叶变换）在模拟和真实数据上进行了比较。应用案例是英格兰河流网络的水质指数去噪，展示了方法在真实水文网络上的实用性。对您而言，本文是统计计算与图信号处理的交叉，其线图构造和提升方案的设计思路可能启发您在高阶 U-统计量的张量网络计算中处理边/路径上的聚合问题。
- **关键技术**: `lifting scheme`, `second-generation wavelets`, `line graph`, `LOCAAT`, `network signal processing`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。其线图构造和提升方案的设计思路，可能启发您在高阶 U-统计量的张量网络计算中处理边/路径上的聚合问题（very_familiar 中的 treewidth / tensor contraction / einsum 可尝试建模该算法的计算成本）。中期可做：需先在 moderately_familiar 的 HOIF 上长肌肉，以理解该提升方案是否可视为某种影响函数分解。

### 8. [10.1007/s11222-025-10723-6](https://doi.org/10.1007/s11222-025-10723-6) · [arXiv](https://arxiv.org/abs/2501.05326) — Randomized Spectral Clustering for Large-Scale Multi-Layer Networks
- **作者**: Wenqing Su, Xiao Guo, Xiangyu Chang, Ying Yang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对大规模多层网络的社区检测问题，提出了一种随机化谱聚类算法。算法首先对每层的邻接矩阵进行随机采样（sparsify），然后对所有层稀疏化后的邻接矩阵平方和进行随机投影（random projection）以加速特征分解，最后对特征向量做k-means聚类。理论部分在多层随机块模型（multi-layer SBM）下分析了误分类错误率，证明随机化在特定条件下不恶化误差界。算法的时间复杂度和存储空间均显著降低，数值实验在百万节点规模的多层网络上展示了高效性。作者还开发了R包MLRclust。对您而言，本文属于统计计算方向，其随机化加速思路（采样+投影）可迁移到您熟悉的high-dimensional asymptotics和software development领域，但核心问题（谱聚类加速）与您的主要兴趣（因果推断、U统计量）距离较远。作为gateway reading，本文对统计计算tradeoff的讨论较浅，未涉及信息-计算间隙或低度多项式障碍等深层理论，因此暂不可做——缺少计算复杂性理论工具。
- **关键技术**: `randomized spectral clustering`, `random sampling sparsification`, `random projection`, `multi-layer stochastic block model`, `misclassification error rate`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的statistical computing直接相关。其随机化加速策略（采样+投影）可视为一种计算-精度tradeoff的实例，但本文未深入讨论信息-计算间隙或低度多项式障碍，因此作为gateway reading价值有限。您的武器库中high-dimensional asymptotics可用于验证其误差界的紧性，但核心计算复杂性理论工具（如低度多项式方法）不在您的武器库中，因此暂不可做。

### 9. [10.1007/s11222-025-10748-x](https://doi.org/10.1007/s11222-025-10748-x) · [arXiv](https://arxiv.org/abs/2406.15865) — Approximate Bayesian computation sequential Monte Carlo via random forests
- **作者**: Khanh N. Dinh, Cécile Liu, Zijin Xiang, Zhihan Liu, Simon Tavaré
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在近似贝叶斯计算（ABC）框架下，针对似然函数难以计算的问题，提出了两种基于随机森林（RF）的新方法。第一种方法利用分布随机森林直接推断参数的联合后验分布，避免了传统ABC中手动选择汇总统计量、距离函数和容差阈值的繁琐步骤。第二种方法将随机森林与序贯蒙特卡洛（SMC）结合，通过迭代更新先验分布，将计算资源集中在参数空间的高概率区域，从而提升采样效率。两种方法均无需预先指定汇总统计量，且对先验分布的选择不敏感。作者在多个确定性和随机模型（包括群体遗传学、传染病动力学等）上进行了数值实验，结果表明新方法在精度和计算效率上优于传统ABC-RF和标准ABC-SMC。对您而言，本文属于统计计算方向，展示了如何将机器学习（RF）嵌入模拟推断框架，其核心思想（用非参数回归替代手工特征工程）可迁移至您熟悉的因果推断或高维统计中的计算密集型问题。
- **关键技术**: `Approximate Bayesian Computation`, `random forests`, `sequential Monte Carlo`, `distributional random forests`, `likelihood-free inference`
- **为什么对您有用**: 本文属于统计计算方向，是您secondary interest中的gateway reading。它不要求天文学或经济学背景，而是聚焦于似然不可得时的通用推断框架，适合作为您进入模拟推断领域的入门读物。您的武器库中'非参数统计'和'软件工具开发'两项very_familiar技能可直接用于理解其核心机制（RF作为非参数回归器），而'高维渐近'知识有助于评估其在高维参数空间下的表现。中期可做：若您想在此方向深入，需在'moderately_familiar'的M估计理论上补强，因为ABC-SMC的收敛性分析本质上依赖于重要性采样的方差控制。

### 10. [10.1007/s11222-025-10745-0](https://doi.org/10.1007/s11222-025-10745-0) — Efficient Likelihood-Based Temporal Changepoint Detection in Spatio-Temporal Processes
- **作者**: Gaurav Agarwal, Idris A. Eckley, Paul Fearnhead
- **期刊/来源**: Statistics and Computing
- **机构**: Lancaster University
- **分类**: vol 35 · issue 6
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对时空过程的时间突变点检测问题，提出一种基于似然的方法。传统时间序列方法难以处理时空相关性，而现有方法常假设数据在突变点间独立，这在实际中不成立。作者采用一种近期提出的协方差模型，允许时间上的非平稳性，并通过马尔可夫近似来降低似然计算的计算负担。该方法的核心在于利用马尔可夫近似将原本复杂的时空似然分解为可高效计算的形式，从而在保持统计效率的同时实现可扩展性。应用于爱尔兰多个气象站两年间的日风速数据，成功检测出2021年7月24日的一个显著突变点，与天气模式重大变化吻合。本文的方法学贡献在于为时空数据提供了一种计算上可行的似然推断框架，对您而言，其计算策略（马尔可夫近似加速似然）与您统计计算兴趣中的数值方法直接相关，可作为处理大规模时空模型计算瓶颈的参考。
- **关键技术**: `Markov approximation`, `likelihood-based changepoint detection`, `nonstationary covariance model`, `spatio-temporal process`, `scalable likelihood computation`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您 primary interest 中的 statistical computing。其核心计算技巧——利用马尔可夫近似分解时空似然——是您 very_familiar 中非参数统计和软件开发的典型应用场景。立即可做：您可以用树宽/张量收缩的视角分析该马尔可夫近似的计算复杂度，或将其与您熟悉的 einsum 库结合实现更高效的似然计算。

### 11. [10.1007/s11222-025-10747-y](https://doi.org/10.1007/s11222-025-10747-y) · [arXiv](https://arxiv.org/abs/2309.05435) — Parallel Selected Inversion for Space-Time Gaussian Markov Random Fields
- **作者**: Abylay Zhumekenov, Elias T. Krainski, Håvard Rue
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对大规模时空高斯马尔可夫随机场（GMRF）的贝叶斯推断，提出一种并行选逆（selected inversion）方法，用于高效计算稀疏精度矩阵的逆元素（边际方差）及超参数估计所需的导数。传统直接矩阵分解在分布式集群上扩展性差，而Krylov子空间方法虽可处理选逆但收敛慢。作者提出基于区域分解（domain decomposition）的混合策略：全局用Krylov子空间方法，子域用直接分解作为基求解器，结合Rao-Blackwellized Monte Carlo估计器实现分布式精度矩阵的选逆。通过引入子域重叠（subdomain overlaps）可在不增加通信开销下提升精度。在模拟数据和美国日温度数据上展示了加速效果和超参数推断效率。该方法对您统计计算兴趣中的数值方法与算法子方向有直接参考价值，尤其是并行化稀疏矩阵计算的策略。
- **关键技术**: `selected inversion`, `Krylov subspace methods`, `domain decomposition`, `Rao-Blackwellized Monte Carlo`, `sparse precision matrix`, `distributed computing`
- **为什么对您有用**: 本文属于统计计算（stat_computing）的数值方法，直接对应您primary interest中的'statistical computing (numerical methods, algorithm)'。您武器库中'软件开发和逆问题'的very_familiar技能可用来评估其并行化策略的通用性，特别是子域重叠的精度-计算权衡。中期可做：若想将类似区域分解思路迁移到您熟悉的higher-order U-statistics的分布式计算中，需先在moderately_familiar的M-estimation理论中熟悉分布式推断的收敛性分析。

### 12. [10.1007/s11222-025-10749-w](https://doi.org/10.1007/s11222-025-10749-w) · [arXiv](https://arxiv.org/abs/2504.15588) — Bayesian parameter estimation for partially observed McKean-Vlasov diffusions using multilevel Markov chain Monte Carlo
- **作者**: AJAY JASRA, AMIN WU
- **期刊/来源**: Statistics and Computing
- **分类**: vol 35 · issue 6
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对部分观测的 McKean-Vlasov 扩散过程，在固定时间区间内离散时间观测下，研究静态参数的贝叶斯估计问题。该问题的难点在于：即使已知转移概率，连续时间下的后验密度在数值上也是不可处理的；即使采用时间离散化，标准 MCMC 方法也无法直接用于后验采样。作者提出了一种新的 MCMC 算法来解决上述问题，并将其扩展为基于多层蒙特卡罗（MLMC）的 MCMC 算法。理论部分证明了参数估计量的收敛界，并表明与普通 MCMC 相比，MLMC-MCMC 算法将达到给定均方误差所需的计算成本降低了一个数量级。最后通过两个数值模型验证了结果。
- **关键技术**: `Multilevel Monte Carlo (MLMC)`, `Markov chain Monte Carlo (MCMC)`, `McKean-Vlasov diffusion`, `Bayesian parameter estimation`, `time-discretization`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，是您 secondary interest 中 'statistical computing (numerical methods, algorithm)' 的典型应用。您武器库中的 'software development' 和 'high-dimensional asymptotics' 可用于理解其 MLMC 的收敛性分析，但核心的 MCMC 与扩散过程耦合并非您的主要工具。本文作为 gateway reading 价值中等：它清晰展示了 MLMC 在复杂模型（McKean-Vlasov）中的计算增益，但需要读者熟悉扩散过程和贝叶斯计算，入门门槛不低。**暂不可做**：核心机器（扩散过程的 MCMC 采样、MLMC 的方差分解）不在您武器库中，需先补充随机过程与贝叶斯计算基础。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

