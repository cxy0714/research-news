# Stat. Comput. — Vol 36  Issue 3  ·  2026-07-14

- 共 30 篇 · Statistics and Computing
- 目录核对 ⚠️ 疑似漏 12 篇（对照 OpenAlex 45 篇）：10.1007/s11222-026-10891-z、10.1007/s11222-026-10861-5、10.1007/s11222-026-10848-2、10.1007/s11222-026-10853-5、10.1007/s11222-026-10860-6 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Stat. Comput.》第36卷第3期的30篇论文，整体上呈现两条清晰的主线：**统计计算中的高效推断与算法设计**，以及**高维/结构化数据的建模与正则化**。前者覆盖了变分贝叶斯、在线学习、路径优化、MCMC加速、伪边际方法等计算策略，后者则聚焦于矩阵/张量分解、混合模型、稀疏回归、主题模型等结构化设定。此外，还有少量论文涉及假设检验（如变点后选择推断）和机器学习公平性（距离协方差框架），但数量较少，不构成主线。

在统计计算主线中，多篇论文致力于解决特定模型的计算瓶颈。例如，“Optimal estimation and uncertainty quantification for Stochastic inverse problems via variational Bayesian methods”将变分贝叶斯与最优控制结合，避免了MCMC的高成本；“Online survival analysis with quantile regression”针对流式删失数据，通过二阶近似和MM算法实现低存储在线更新；“Pathwise optimization for bridge-type estimators and its applications”为非凸桥型正则化提供了路径优化方案；“A Gibbs sampler for the LKJ Prior on correlation matrices”通过解析条件后验提升了相关矩阵采样的效率；“Approximating evidence via bounded harmonic means”用椭球覆盖解决了调和均值估计器的方差问题。这些工作共同展示了如何通过算法创新（如近似、分解、条件推断）将复杂模型的计算变得可行。

另一条主线是高维/结构化数据的建模，尤其关注矩阵、张量和混合模型。例如，“High-dimensional regularized additive matrix autoregressive model”用低秩加稀疏分解处理矩阵时间序列；“Shift-aware sparse kronecker tensor classification”将移位感知嵌入张量回归以应对空间未对齐；“Non-negative matrix factorization algorithms generally improve topic model fits”建立了主题模型与NMF的等价性，并引入加速优化；“Parsimonious Gaussian mixture models with piecewise-constant eigenvalue profiles”通过分段常数特征值谱实现高维GMM的简约化；“Matrix-variate cluster-weighted bilinear factor analyzers”在矩阵聚类中引入双线性因子分析。这些论文的共同策略是利用结构假设（低秩、稀疏、因子分解）来降低参数维度，同时保持模型的可解释性和计算效率。

对于因果推断方向的研究者，本期最直接相关的论文是“Post-selection inference for quantifying uncertainty in changes in variance”，它将后选择推断框架从均值变点推广到方差变点，其条件推断思路可迁移至因果效应估计中的变点或断点问题。半参数效率方向虽无直接论文，但“High-dimensional regularized additive matrix autoregressive model”中的低秩加稀疏分解思路，以及“Shift-aware sparse kronecker tensor classification”中的张量回归框架，对高维因果结构学习有参考价值。高维统计方向则可优先关注“Non-negative matrix factorization algorithms generally improve topic model fits”（展示矩阵分解与统计模型的等价性）和“Parsimonious Gaussian mixture models with piecewise-constant eigenvalue profiles”（特征值谱结构在高维混合模型中的应用）。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1007/s11222-026-10881-1](https://doi.org/10.1007/s11222-026-10881-1) · [arXiv](https://arxiv.org/abs/2405.15670) — Post-selection inference for quantifying uncertainty in changes in variance
- **作者**: Rachel Carrington, Paul Fearnhead
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究变点检测中方差变化的不确定性量化问题。核心挑战在于数据被重复使用：先用数据检测变点，再用同一数据检验变点，导致 naive 检验的 p 值偏小、拒绝率膨胀。作者将 post-selection inference 框架从均值变点推广到方差变点，通过条件推断（condition on the selection event）构造出在无变化原假设下服从均匀分布的 valid p 值。方法上提出两种构造策略，分别对应不同的变点检测算法（如 CUSUM-type 或 likelihood-based），但统一采用 selection event 的几何刻画（polytope / affine constraints）来推导条件分布。理论结果包括 p 值的 exact finite-sample validity 和 power 分析。对您而言，本文是 post-selection inference 在方差参数上的首次系统推广，与您 hypothesis testing 和 high-dimensional statistics 的兴趣直接相关——变点检测在时间序列和高维协方差结构变化中都有广泛应用，且 post-selection 的几何条件推断技术（polytope conditioning）与您熟悉的 M-estimation 和 U-statistic 的投影方法有潜在交叉。
- **关键技术**: `post-selection inference`, `changepoint detection`, `conditional hypothesis testing`, `polyhedral conditioning`, `selective inference`
- **为什么对您有用**: 直接连接 hypothesis testing 兴趣：post-selection inference 是当前假设检验的前沿方向，本文首次处理方差变点而非均值变点，填补了选择性推断在方差参数上的空白。技术武器库中 very_familiar 的 nonparametric statistics 和 high-dimensional asymptotics 可用于理解其条件推断的渐近性质；moderately_familiar 的 M-estimation theory 可用于将 selection event 的几何刻画推广到更一般的估计方程框架。中期可做：若先熟悉 polytope conditioning 的几何推导（moderately_familiar 的 semiparametric theory 可辅助），可将本文方法扩展到高维协方差矩阵的变点检测。

## 统计计算 / 算法  *(stat_computing, 26 篇)*

### 1. [10.1007/s11222-026-10847-3](https://doi.org/10.1007/s11222-026-10847-3) · [arXiv](https://arxiv.org/abs/2503.10199) — Optimal estimation and uncertainty quantification for Stochastic inverse problems via variational Bayesian methods
- **作者**: Ruibiao Song, Liying Zhang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对随机逆问题（如SPDE解）中贝叶斯MAP估计不稳定且MCMC计算昂贵的问题，提出一种基于最优控制理论和变分贝叶斯的两阶段优化方法。第一阶段引入新的加权公式以保证MAP估计的稳定性；第二阶段将该加权公式与变分推断结合，推导出高效不确定性量化的必要条件。作者建立了误差估计定理，刻画了最优估计解与真实解在不同观测数据量下的关系。数值实验验证了该方法在点估计和不确定性量化上的效率。该方法的核心技术是变分贝叶斯与最优控制理论的结合，避免了MCMC的高计算成本。对您而言，本文属于统计计算方向，展示了变分推断在逆问题中的实用框架，可作为您软件开发和数值方法兴趣的参考案例。
- **关键技术**: `variational Bayesian inference`, `optimal control theory`, `maximum a posteriori (MAP) estimation`, `uncertainty quantification`, `stochastic inverse problems`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的'statistical computing (numerical methods, algorithm)'直接相关。您武器库中'very_familiar'的'inverse problems with random noise'和'software development'可直接用于理解其变分推断框架，并评估其数值稳定性。中期可做：若您想将类似变分方法扩展到因果推断中的逆概率加权问题，需先在'moderately_familiar'的'identification theory in causal inference'上加强。

### 2. [10.1007/s11222-026-10858-0](https://doi.org/10.1007/s11222-026-10858-0) · [arXiv](https://arxiv.org/abs/2506.01403) — High-dimensional regularized additive matrix autoregressive model
- **作者**: Debika Ghosh, Samrat Roy, Nilanjana Chakraborty
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种高维正则化加性矩阵自回归模型（RAMAR），用于分析矩阵时间序列。与现有基于双线性或Tucker分解的模型不同，该模型假设行向和列向的时间依赖以加性方式交互，从而避免了非凸优化问题，提高了可解释性。模型将转移矩阵分解为低秩加稀疏结构，并通过交替块最小化算法进行凸优化求解。作者证明了模型参数的可识别性，并给出了高维尺度下的有限样本误差界。在合成数据和真实数据上的实验验证了模型的有效性。该工作对您可能有用：其凸优化框架和低秩加稀疏分解思路可迁移至高维因果推断中的结构学习问题，且交替块最小化算法与您熟悉的软件开发和数值方法有直接关联。
- **关键技术**: `alternating block minimization`, `low-rank plus sparse decomposition`, `additive matrix autoregression`, `convex optimization`, `finite-sample error bound`
- **为什么对您有用**: 本文属于统计计算方向，与您的主要兴趣“统计计算（数值方法、算法）”直接相关。其交替块最小化算法和低秩加稀疏分解是您“very_familiar”中的“软件开发和数值方法”可以立即实现的工具——您可以用einsum库高效实现矩阵运算，并测试其在高维因果推断（如IV估计中的结构矩阵分解）中的迁移性。**立即可做**：基于您对非参数统计和高维渐近的熟悉，可以复现其有限样本误差界并扩展到更一般的损失函数。

### 3. [10.1007/s11222-026-10849-1](https://doi.org/10.1007/s11222-026-10849-1) — Computationally efficient likelihood-based estimation and variable selection for the Cox model with incomplete covariates
- **作者**: Ngok Sang Kwok, Kin Yau Wong
- **期刊/来源**: Statistics and Computing
- **机构**: Hong Kong Polytechnic University · Shenzhen Polytechnic University
- **分类**: vol 36 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对 Cox 比例风险模型中协变量缺失（MAR 假设）且缺失模式任意、缺失变量数量大的场景，提出一种计算可行的非参数最大似然估计方法。核心创新在于 E-step 中通过变换技巧将高维积分降为一维积分，使得 EM 算法在缺失变量多时仍保持计算可处理性。进一步，将 Lasso 惩罚项融入似然，实现变量选择。通过大规模模拟和癌症基因组数据应用验证了方法的可行性与优势。该方法对您而言，可作为处理高维缺失数据时计算策略的参考，尤其其降维技巧可能启发您在高阶 U-统计量或张量计算中处理类似积分问题。
- **关键技术**: `EM algorithm`, `nonparametric maximum likelihood`, `Cox model`, `missing at random`, `Lasso penalty`, `one-dimensional integration`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中“statistical computing (numerical methods, algorithm)”直接相关。其核心技巧——将高维积分降为一维——可视为一种计算复杂度削减策略，您可以用 very_familiar 的“software development”和“high-dimensional asymptotics”工具来评估该技巧的通用性，并思考是否可迁移到您熟悉的“higher-order U-statistics (treewidth / tensor contraction / einsum)”场景中，例如处理缺失数据下 U-统计量的计算。中期可做：需先在 moderately_familiar 的“M-estimation theory”上巩固，以理解 EM 与惩罚似然的结合。

### 4. [10.1007/s11222-026-10870-4](https://doi.org/10.1007/s11222-026-10870-4) · [arXiv](https://arxiv.org/abs/2507.15696) — Online survival analysis with quantile regression
- **作者**: Yi Deng, Shuwei Li, Liuquan Sun, Baoxue Zhang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对流式数据（streaming data）场景下的删失分位数回归（censored quantile regression）提出在线推断方法。核心策略是将基于鞅的非光滑目标函数通过二阶展开近似为二次损失函数，从而构造仅依赖当前数据批次和历史数据汇总统计量的在线凸函数，实现低存储空间的在线更新。为估计回归参数，设计了一种新的majorize-minimize（MM）算法，通过合理构造二次代理目标函数得到参数更新的闭式解，显著降低计算负担。理论上，与一次性分析全部原始数据的oracle估计量相比，本文对分位数网格大小（quantile grid size）的假设更弱，并证明在线估计量能保持相同的收敛速度和统计效率。模拟研究和实际应用验证了所提方法的良好经验性能。对您而言，该工作展示了如何将经典统计方法（分位数回归）适配到计算资源受限的流式数据场景，其MM算法和在线更新框架对您感兴趣的统计计算方向有直接参考价值。
- **关键技术**: `online convex optimization`, `majorize-minimize (MM) algorithm`, `censored quantile regression`, `martingale-based objective function`, `quadratic surrogate loss`, `streaming data inference`
- **为什么对您有用**: 本文直接关联您的primary interest中的统计计算方向，特别是流式数据下的高效算法设计。您武器库中'软件开发和M-estimation理论'可直接用于复现或扩展其MM算法框架，例如将二次代理目标函数的思想推广到其他非光滑M估计问题。中期可做：若想将在线更新框架与您熟悉的higher-order U-statistics结合（如在线U-statistic估计），需先在moderately_familiar的HOIF理论上提升，因为U-statistic的在线化涉及更复杂的依赖结构。

### 5. [10.1007/s11222-026-10856-2](https://doi.org/10.1007/s11222-026-10856-2) · [arXiv](https://arxiv.org/abs/2412.04047) — Pathwise optimization for bridge-type estimators and its applications
- **作者**: Alessandro De Gregorio, Francesco Iafrate
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究桥型正则化估计（bridge-type estimators）的路径优化（pathwise optimization）问题，目标是在损失函数（如负对数似然或残差平方和）加上 ℓ^q 范数惩罚（q∈(0,1]）的框架下，高效计算整个正则化路径。由于目标函数非凸且不可微，直接优化困难。作者应用非凸优化理论中的两种通用算法——加速近端梯度下降（accelerated proximal gradient descent）和分块交替优化（blockwise alternating optimization）——来高效求解自适应桥估计器的路径解。路径方案不仅支持基于网格的快速调参验证，还能帮助避免非凸优化中的虚假局部极小值。文章讨论了算法的收敛性和路径一致性，并将方法应用于离散时间观测的扩散过程的惩罚估计，这是时间依赖数据统计中的一个新兴课题。对您而言，本文属于统计计算方向，展示了非凸优化算法在正则化路径求解中的具体实现，与您的 statistical computing 兴趣直接相关，但方法学新颖性有限，主要是现有算法的应用组合。
- **关键技术**: `bridge-type regularization`, `ℓ^q norm penalty`, `accelerated proximal gradient descent`, `blockwise alternating optimization`, `pathwise optimization`, `non-convex optimization`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。核心算法（加速近端梯度下降、分块交替优化）是您 very_familiar 的优化工具，可以立即复现或扩展。但方法学 novelty 较低（novelty_flag: application），主要是将现有非凸优化算法应用于桥型正则化路径求解，没有提出新的理论界或算法创新。中期可做：若想深入，需在 moderately_familiar 的 M-estimation 理论上加强，以分析路径一致性条件。

### 6. [10.1007/s11222-026-10850-8](https://doi.org/10.1007/s11222-026-10850-8) · [arXiv](https://arxiv.org/abs/2504.11279) — Simulation-based inference for stochastic nonlinear mixed-effects models with applications in systems biology
- **作者**: Henrik Häggström, Sebastian Persson, Marija Cvijovic, Umberto Picchini
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对随机非线性混合效应模型（如混合效应随机微分方程）提出了一种可扩展的贝叶斯推断方法。核心思路是先构建似然和后验的摊销近似（amortized approximation），再针对每个个体数据集快速精调，从而高效地逼近多个个体的参数后验。该方法使用混合专家模型（mixture of experts）而非神经网络，使得代理模型既简洁又具有表达力，且易于训练。作者在系统生物学驱动的随机模型上验证了有效性，并应用于mRNA转染的真实数据案例。与精确的伪边际贝叶斯推断相比，该方法在统计精度相当的前提下大幅提升了计算速度。本文属于统计计算方向，对您而言可作为gateway reading：它展示了在复杂分层模型（如混合效应SDE）中如何用非神经网络的摊销推断实现计算-精度权衡，而您的武器库中“软件开发和M估计理论”可直接用于评估其计算成本与收敛性，但核心的摊销推断机制（如混合专家训练）不在您当前熟悉范围内，属于暂不可做方向。
- **关键技术**: `amortized Bayesian inference`, `mixture of experts`, `pseudo-marginal MCMC`, `stochastic differential equations`, `mixed-effects models`
- **为什么对您有用**: 本文属于统计计算方向，可作为gateway reading：它展示了在复杂分层模型（如混合效应SDE）中如何用非神经网络的摊销推断实现计算-精度权衡。您的武器库中“软件开发和M估计理论”可直接用于评估其计算成本与收敛性，但核心的摊销推断机制（如混合专家训练）不在您当前熟悉范围内，属于暂不可做方向。

### 7. [10.1007/s11222-026-10892-y](https://doi.org/10.1007/s11222-026-10892-y) — Shift-aware sparse kronecker tensor classification
- **作者**: Hsin-Hsiung Huang, Yuh-Haur Chen, Teng Zhang
- **期刊/来源**: Statistics and Computing
- **机构**: University of Central Florida
- **分类**: vol 36 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对神经影像分类中空间未对齐的挑战，提出循环移位稀疏Kronecker乘积分解（CS-SKPD）模型，将移位感知机制嵌入低秩张量回归框架。模型通过生成自适应对齐的输入视图，提升对解剖变异的鲁棒性，同时利用稀疏空间分解保持可解释性。理论分析在适应logistic损失的受限强凸性条件下建立了渐近一致性。模拟实验表明在噪声和未对齐下能准确恢复信号，并在分辨率与效率间取得良好权衡。在OASIS-1和ADNI-1 MRI数据上，模型取得有竞争力的分类性能，识别出海马体和小脑等临床相关区域。对您而言，本文的张量分解与移位对齐机制可视为统计计算中处理结构化高维数据的一个具体案例，其低秩分解思路与您熟悉的张量收缩/树宽计算有潜在联系，但核心方法（循环移位、Kronecker分解）不在您的武器库中，属于中期可读的gateway材料。
- **关键技术**: `Kronecker product decomposition`, `low-rank tensor regression`, `cyclic shift alignment`, `restricted strong convexity`, `sparse spatial factorization`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的统计计算（数值方法、算法）直接相关。其低秩张量分解与移位对齐机制，可尝试用您very_familiar的树宽/张量收缩复杂度视角来分析其计算成本（如Kronecker分解的收缩顺序优化）。但核心的循环移位对齐和logistic损失下的受限强凸性分析并非您的武器库核心，属于中期可做：需先在moderately_familiar的M估计理论中熟悉受限强凸性条件，才能评估其理论紧性。

### 8. [10.1007/s11222-026-10871-3](https://doi.org/10.1007/s11222-026-10871-3) · [arXiv](https://arxiv.org/abs/2507.09206) — A deep learning approach to multi-marginal optimal transport via Hilbert space embeddings of probability measures
- **作者**: Yumiharu Nakano, Takafumi Saito
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种求解多边际 Monge 问题的数值方法，该问题将经典 Monge 最优传输推广到多个目标分布。方法基于概率测度的 Hilbert 空间嵌入（核均值嵌入），利用最大均值差异（MMD）作为惩罚项来强制边际约束，从而将原问题转化为一个可微的优化目标。该方法设计为可 GPU 加速，适合大规模计算。数值实验在合成数据上验证了有效性。对您而言，本文属于统计计算方向的新算法，其核嵌入+惩罚的思路可迁移到您熟悉的因果推断中高维协变量平衡或分布匹配问题，但方法学 novelty 一般，主要是工程实现上的贡献。
- **关键技术**: `kernel mean embedding`, `maximum mean discrepancy (MMD)`, `multi-marginal optimal transport`, `penalized optimization`, `GPU-based implementation`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关。您武器库中的 nonparametric statistics（核方法）和 software development（GPU 实现）可直接用于复现或扩展该方法。中期可做：将 MMD 惩罚用于因果推断中的分布平衡（如 IV 或 mediation 中的协变量匹配），但需先在 moderately_familiar 的 identification theory 上熟悉具体设定。

### 9. [10.1007/s11222-026-10865-1](https://doi.org/10.1007/s11222-026-10865-1) · [arXiv](https://arxiv.org/abs/2505.06935) — Accelerated inference for stochastic compartmental models with over-dispersed partial observations
- **作者**: Michael Whitehouse
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对一类部分观测的随机房室模型（stochastic compartmental models），在允许观测过分散（over-dispersion）的设定下，推导了一种假设密度近似似然（assumed density approximate likelihood）。核心创新是将时变报告概率（time-varying reporting probabilities）视为潜变量，利用Laplace近似在Poisson近似似然（LawPAL）框架内将其积分掉，从而得到边际似然和滤波分布的快速确定性近似。作者证明了大群体极限下该滤波近似是渐近精确的，能恢复潜在疾病状态和报告概率。模拟表明：1）在大群体和大时间跨度下，最大近似似然估计器能良好恢复真实参数；2）相比基于序贯蒙特卡洛（SMC）的似然方法，计算速度提升一个数量级，同时清晰刻画了近似引入的统计折衷。最后，该方法被嵌入概率编程语言Stan中，用于瑞士Covid-19疫情数据的自动化贝叶斯推断。本文对您作为统计计算方向的研究者特别有用：它展示了如何用确定性近似（Laplace + 解析积分）替代SMC，在保持统计精度的同时实现数量级加速，其思路可迁移到您熟悉的逆问题或高维渐近分析中。
- **关键技术**: `Laplace approximation`, `Poisson Approximate Likelihood (LawPAL)`, `assumed density filtering`, `sequential Monte Carlo (SMC) comparison`, `probabilistic programming (Stan)`
- **为什么对您有用**: 本文直接命中您的primary interest中的统计计算（numerical methods, algorithm），提供了一个用确定性近似替代SMC的清晰案例，计算加速显著且统计折衷被明确刻画。您的武器库中'非参数统计'和'逆问题'的功底可用于分析该近似在大群体极限下的误差界，而'软件开发'经验可直接用于将类似思路嵌入Stan或其他概率编程框架。中期可做：若想将此类确定性近似推广到更一般的潜变量模型（如您熟悉的因果推断中的测量误差问题），需先在moderately_familiar的M估计理论或半参数理论上长肌肉，以处理近似带来的偏差-方差权衡。

### 10. [10.1007/s11222-026-10855-3](https://doi.org/10.1007/s11222-026-10855-3) · [arXiv](https://arxiv.org/abs/2508.12288) — An optimal experimental design approach to sensor placement in continuous stochastic filtering
- **作者**: Sahani Pathiraja, Claudia Schillings, Philipp Wacker
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究连续时间随机滤波中传感器放置的最优实验设计（OED）问题。将传感器放置问题推广为关于一般概率测度ξ的积分，从而将离散时间传感器放置（Dirac混合特例）提升到无限维但数学上更良定的框架。针对由Zakai方程控制的连续时间滤波设定，推导了OED效用泛函的Fréchet导数，其关键在于一个伴随（时间反向）微分方程。这一结果为利用基于梯度的优化方法替代传统的（半）离散优化方法（如贪心插入/删除）提供了理论依据，有望大幅提升计算效率。文章在数值上展示了所提方法在传感器数量较多时的优势。对您而言，本文展示了统计计算中OED与随机滤波的交叉，其伴随方法思想可迁移至您熟悉的逆问题与高维统计设定，属于中期可做的方向——需先在moderately_familiar的M-estimation理论中熟悉伴随方程构造。
- **关键技术**: `Optimal Experimental Design (OED)`, `Zakai equation`, `Fréchet derivative`, `adjoint (backwards) differential equation`, `gradient-based optimization`, `continuous-time stochastic filtering`
- **为什么对您有用**: 本文直接关联您的primary interest中的统计计算（numerical methods, algorithm）以及逆问题（inverse problems with random noise）。其核心贡献——通过伴随方程计算OED泛函的Fréchet导数——为传感器放置问题提供了可微优化框架，这与您very_familiar的逆问题工具（如随机噪声下的反问题）高度契合。您可以用minimax bound视角分析该梯度方法的收敛率，或用higher-order U-statistics的树宽视角评估其计算复杂度。**中期可做**：需先在moderately_familiar的M-estimation理论中熟悉伴随方程构造，然后可尝试将本文的连续时间框架推广到您的因果推断设定（如纵向数据中的最优观测时间点设计）。

### 11. [10.1007/s11222-026-10893-x](https://doi.org/10.1007/s11222-026-10893-x) — Bootstrap aggregation for regression problems via generalized least squares
- **作者**: Chih-Yu Chang, Ming-Chung Chang
- **期刊/来源**: Statistics and Computing
- **机构**: Imperial College London · Institute of Statistical Science, Academia Sinica
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对回归问题中的 Bootstrap 聚合（bagging）方法，提出基于广义最小二乘（GLS）的聚合策略，以更有效地处理基模型间的相关性。传统 bagging 通过随机特征选择（如随机森林）降低相关性，但缺乏最优加权机制。作者将基模型预测视为带相关误差的观测，用 GLS 估计最优聚合权重，理论上证明了无偏性和最优性。为平衡计算精度与复杂度，进一步提出两阶段方法：先用简单加权估计协方差结构，再代入 GLS 得到最终聚合。实验在多个回归数据集上验证了该方法在保持低计算成本的同时提升了预测精度。该工作属于统计计算中 ensemble 方法的算法改进，对您作为统计计算方向（特别是软件开发和算法设计）的参考价值在于：其 GLS 聚合框架可推广到更一般的模型集成场景，且两阶段策略为计算-精度 tradeoff 提供了可操作的模板。
- **关键技术**: `bootstrap aggregation`, `generalized least squares`, `two-stage estimation`, `ensemble learning`, `covariance estimation`
- **为什么对您有用**: 本文直接关联您的 primary interest 中的 statistical computing（算法设计）方向，其 GLS 聚合框架可视为 ensemble 方法中一个计算上可操作的改进。您武器库中 very_familiar 的 minimax bounds 和 high-dimensional asymptotics 可用于分析该两阶段估计量的收敛速率和最优性条件，属于**立即可做**的 follow-up：例如推导 GLS 权重估计的 minimax 风险，或在高维基模型场景下分析协方差估计的精度对聚合效果的影响。

### 12. [10.1007/s11222-026-10866-0](https://doi.org/10.1007/s11222-026-10866-0) · [arXiv](https://arxiv.org/abs/2105.13440) — Non-negative matrix factorization algorithms generally improve topic model fits
- **作者**: Peter Carbonetto, Abhishek Sarkar, Zihao Wang, Matthew Stephens
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文重新审视了主题模型中的最大似然估计问题，并正式建立了其与非负矩阵分解（NMF）优化问题之间的等价关系。作者证明，主题模型的EM算法本质上等价于NMF的经典乘法更新规则。基于这一理论联系，文章将近年来NMF优化方法的进展（如加速梯度法、坐标下降法）直接应用于主题模型的拟合，显著提升了计算效率。在多个真实和模拟数据集上，新方法不仅收敛更快，而且通常能得到比现有主题模型算法（如变分EM、吉布斯采样）更高的似然值。所有方法已实现为R包“fastTopics”。本文对您的主要价值在于：它展示了如何将一个统计计算问题（主题模型MLE）重新表述为矩阵分解优化问题，从而利用数值线性代数的成熟工具——这与您对统计计算（数值方法、算法）的兴趣直接相关，且您熟悉的软件开发和矩阵计算技能可立即用于复现或扩展其方法。
- **关键技术**: `non-negative matrix factorization (NMF)`, `multiplicative updates`, `coordinate descent`, `accelerated gradient methods`, `expectation maximization (EM) algorithm`
- **为什么对您有用**: 本文直接对应您的primary interest“statistical computing (numerical methods, algorithm)”，且属于gateway-reading范畴：它清晰展示了如何将统计模型（主题模型）的MLE问题转化为NMF优化问题，并利用数值线性代数工具加速求解。您武器库中“software development”和“high-dimensional asymptotics”可立即用于：1) 复现并测试其算法在大规模文本数据上的扩展性；2) 从优化收敛率角度分析其加速机制。**立即可做**：用您熟悉的软件开发和矩阵计算技能，即可复现其核心算法并应用于自己的数据。

### 13. [10.1007/s11222-026-10879-9](https://doi.org/10.1007/s11222-026-10879-9) — A Gibbs sampler for the LKJ Prior on correlation matrices
- **作者**: Steven Andrew Culpepper, Trevor Park
- **期刊/来源**: Statistics and Computing
- **机构**: University of Illinois Urbana-Champaign
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对层次回归模型中随机效应相关矩阵的贝叶斯推断，提出了一种基于 LKJ 先验（Lewandowski et al., 2009）的新型 Gibbs 采样算法。核心贡献在于将相关矩阵的采样分解为一系列条件分布，利用 Hamura et al. (2024) 的多元广义逆高斯分布采样器实现高效的逐元素更新。在计算时间和有效样本量方面，该 Gibbs 采样器与基于 Stan 的 brms R 包（Bürkner, 2017）具有竞争力，且在稀疏或小样本数据集中表现更优、更稳定。方法本质上是一种针对特定先验结构设计的 MCMC 算法，其效率提升来源于对条件后验分布的解析推导和专用采样器的使用。对您而言，本文属于统计计算中算法设计的案例，其将复杂后验分解为可采样条件分布的思想，可迁移到您熟悉的因果推断或高维统计中涉及相关矩阵或协方差矩阵后验采样的场景。
- **关键技术**: `Gibbs sampling`, `LKJ prior`, `multivariate generalized inverse Gaussian distribution`, `Bayesian mixed models`, `random-effect correlation matrix`
- **为什么对您有用**: 本文属于统计计算（MCMC 算法设计）方向，直接对应您的 primary interest 中的 statistical computing。虽然方法本身不涉及因果推断或高维理论，但其对 LKJ 先验下相关矩阵的高效采样策略，是您 moderately_familiar 的 M-estimation 和 semiparametric theory 中处理随机效应模型时可能用到的计算工具。您可以用 very_familiar 的软件开发和算法实现能力，快速复现或扩展该 Gibbs 采样器到其他先验结构（如分离协方差矩阵）。中期可做：将本文的采样思想与您 moderately_familiar 的 HOIF 结合，用于贝叶斯半参数效率界计算中的后验采样。

### 14. [10.1007/s11222-026-10883-z](https://doi.org/10.1007/s11222-026-10883-z) — Matrix-variate cluster-weighted bilinear factor analyzers
- **作者**: Salvatore D. Tomarchio
- **期刊/来源**: Statistics and Computing
- **机构**: University of Catania
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对矩阵型数据（matrix-variate data），在 Cluster-Weighted Model (CWM) 框架下引入双线性因子分析（bilinear factor-analytic）结构，构建了两个包含 64 种简约配置的模型族。参数估计采用 AECM 算法，并提供了 R 包 MatFacReg 的实现。通过模拟研究评估了信息准则在恢复正确模型结构、成分数和潜在因子数方面的能力，以及估计精度和计算效率。在农业食品部门温室气体排放的实证分析中，所提模型相比无因子分析约束的标准矩阵 CWM 拟合更优，揭示了四个主要由能源使用和人口规模区分的国家群体。本文的方法贡献在于为高维矩阵数据提供了一种结构化降维与聚类联合建模的途径。对您而言，该工作展示了统计计算中算法实现（AECM）与软件包开发的完整流程，属于您 primary interest 中“statistical computing”的直接应用，但方法学新颖性有限。
- **关键技术**: `AECM algorithm`, `bilinear factor analysis`, `Cluster-Weighted Model`, `matrix-variate data`, `information criteria`
- **为什么对您有用**: 本文属于统计计算与软件实现方向，直接对应您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。您可以用 very_familiar 的“软件开发”经验快速评估其 R 包 MatFacReg 的代码质量与扩展性；但核心方法（CWM + 因子分析）是经典技术的组合，不涉及您武器库中的 minimax bound、U-statistic 或因果推断工具，属于“暂不可做”的 follow-up——除非您有意在矩阵聚类方向积累，否则不值得深读。

### 15. [10.1007/s11222-026-10878-w](https://doi.org/10.1007/s11222-026-10878-w) · [arXiv](https://arxiv.org/abs/2510.06787) — Likelihood-based inference for the Gompertz model with Poisson errors
- **作者**: Paolo Onorati, Sofia Ruiz-Suarez, Radu V. Craiu
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对 Gompertz 种群动态模型在 Poisson 观测误差下的统计推断问题，提出了一套基于完整似然的计算工具。传统方法因忽略采样误差或依赖近似似然而导致估计偏差，而完整似然的计算在状态空间模型框架下通常计算量巨大。作者通过设计高效的数值算法（如结合序贯重要性采样与粒子滤波的似然计算），使得在贝叶斯和频率学派框架下均可进行参数推断。模拟和实际数据分析表明，该方法在偏差和覆盖概率上优于忽略采样误差的近似方法。对您而言，本文展示了在复杂状态空间模型中如何通过计算技巧实现完整似然推断，其数值策略（如粒子滤波与 MCMC 的结合）对您在高维统计计算或因果推断中处理隐变量模型具有参考价值。
- **关键技术**: `particle filter`, `sequential Monte Carlo`, `state-space model`, `full likelihood inference`, `Bayesian MCMC`, `population dynamics`
- **为什么对您有用**: 本文属于统计计算方向，直接对接您对数值方法和算法的兴趣。文中使用的粒子滤波与 MCMC 结合策略，可迁移至您熟悉的因果推断中处理纵向数据或隐变量（如未测量混杂）的似然计算。您武器库中的非参数统计和软件开发经验足以支撑理解其算法实现，属于**立即可做**的阅读材料。

### 16. [10.1007/s11222-026-10867-z](https://doi.org/10.1007/s11222-026-10867-z) · [arXiv](https://arxiv.org/abs/2502.06605) — Quantile forecast matching with a bayesian quantile gaussian process model
- **作者**: Spencer Wadsworth, Jarad Niemi
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于高斯过程的贝叶斯方法（分位数高斯过程，QGP），用于从一组估计的分位数重建完整的连续概率分布。核心设定是：给定多个概率水平及其对应的样本分位数，目标是推断出背后的连续分布函数，并量化分位数估计本身的不确定性。方法利用样本分位数的渐近联合正态性，将分位数建模为高斯过程，从而在分位数之间进行平滑插值并传播不确定性。对于未知分布形式的情形，作者进一步引入截断狄利克雷过程混合模型（truncated DPM）作为非参数先验，以灵活估计底层密度。模拟和2023-24美国CDC流感预报协作项目的真实数据表明，QGP在参数推断、分布近似和不确定性量化上优于现有方法（如线性插值、核密度估计等）。对您而言，本文展示了如何将经典渐近理论（分位数联合正态性）与贝叶斯非参数工具（GP + DPM）结合，解决一个实际的计算统计问题，其建模思路可迁移到您感兴趣的因果推断中预测分布的校准或敏感性分析。
- **关键技术**: `quantile Gaussian process`, `truncated Dirichlet process mixture`, `asymptotic normality of sample quantiles`, `Bayesian nonparametrics`, `probabilistic forecasting`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其核心贡献是用高斯过程对分位数进行建模，这属于您非常熟悉的非参数统计工具（very_familiar），因此您可以立即评估该方法在您自己的预测或因果推断任务中的适用性（立即可做）。此外，文中使用的截断DPM混合模型属于贝叶斯非参数方法，与您moderately_familiar的M-estimation理论有交叉，可作为扩展阅读。

### 17. [10.1007/s11222-026-10868-y](https://doi.org/10.1007/s11222-026-10868-y) · [arXiv](https://arxiv.org/abs/2408.04419) — Analysing symbolic data by pseudo-marginal methods
- **作者**: Yu Yang, Matias Quiroz, Boris Beranger, Robert Kohn, Scott A. Sisson
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对符号数据分析（SDA）中似然函数含大指数积分、计算不可行且参数估计有偏的问题，提出贝叶斯框架下的伪边际MCMC方法。核心机制是：将原始大数据集压缩为随机矩形/直方图等分布性摘要，然后基于摘要进行推断以大幅降低计算成本。方法上，作者开发了两种策略——基于路径采样和Poisson估计量的精确（但计算昂贵）版本，以及基于泰勒展开的快速近似版本。理论贡献在于解决了SDA中积分难处理性和估计偏差这两个关键障碍，并通过模拟和真实数据展示了相比全数据分析的巨大计算时间缩减（信息损失很小）。对您而言，本文展示了在计算受限场景下如何用近似贝叶斯方法替代精确推断，其伪边际MCMC与泰勒近似的组合策略可迁移到您的高维U统计量或因果推断中涉及复杂积分的问题。
- **关键技术**: `pseudo-marginal MCMC`, `path sampling`, `Poisson estimator`, `Taylor expansion`, `symbolic data analysis`, `Bayesian inference`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您的primary interest中的'statistical computing'。技术层面，伪边际MCMC和泰勒近似是处理不可解积分的通用工具，您可以用very_familiar的'软件开发和数值方法'能力快速复现并测试其在高维U统计量积分问题上的表现。中期可做：若想将本文的路径采样+Poisson估计量推广到更复杂的因果推断模型（如proximal CI中的积分），需先在moderately_familiar的'identification theory'上补足对模型结构的理解。

### 18. [10.1007/s11222-026-10869-x](https://doi.org/10.1007/s11222-026-10869-x) · [arXiv](https://arxiv.org/abs/2505.16919) — Hilbert space methods for approximating multi-output latent variable Gaussian processes
- **作者**: Soham Mukherjee, Manfred Claassen, Paul-Christian Bürkner
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文针对高斯过程（GP）在大数据下计算复杂度高的问题，将Hilbert空间近似方法从单输出、显式输入推广到多输出和潜变量输入设定。核心机制是利用Hilbert空间特征函数展开将GP的协方差核近似为有限基函数的线性组合，从而将计算复杂度从O(n^3)降至O(n m^2)（m为基函数数量）。在多输出场景中，作者通过线性模型核（linear model of coregionalization）结构保持输出间的相关性；在潜变量场景中，则通过变分推断联合估计潜变量和GP超参数。模拟实验表明，该方法在计算速度上显著优于精确GP，且在不确定性校准和潜变量估计精度上持平或更优；与其他近似GP（如稀疏GP）相比，虽不一定更快，但校准和估计精度更好。最后在单细胞生物学真实数据上展示了实用性。对您而言，本文属于统计计算中近似方法的推广，与您的统计计算兴趣直接相关，但方法学新颖性有限（主要是已有技术的扩展）。
- **关键技术**: `Hilbert space Gaussian process approximation`, `multi-output Gaussian process`, `latent variable Gaussian process`, `linear model of coregionalization`, `variational inference`
- **为什么对您有用**: 本文属于统计计算中近似方法的推广，直接对应您的primary interest中的统计计算（numerical methods, algorithm）。您的武器库中'软件开发和'非参数统计'可用于复现和扩展其近似框架，但核心的Hilbert空间特征函数展开与您的现有工具交集不大，属于'暂不可做'——缺少谱方法或RKHS近似方面的专门知识。不过作为统计计算方向的入门级阅读，值得花时间了解其思路。

### 19. [10.1007/s11222-026-10859-z](https://doi.org/10.1007/s11222-026-10859-z) · [arXiv](https://arxiv.org/abs/2506.09850) — Lower-dimensional posterior density and cluster summaries for overparameterized Bayesian models
- **作者**: Henrique Bolfarine, Hedibert F. Lopes, Carlos M. Carvalho
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对贝叶斯非参数或过参数化模型（如DP混合模型）在密度估计与聚类中可解释性差的问题，提出一种投影总结方法。核心思路分三步：先用灵活模型拟合数据；再通过决策论框架将原始模型的后验预测分布投影到一系列低维参数化代理（如有限混合模型）上，选出最优维度的点估计；最后将原始后验分布投影到该代理上，为总结提供不确定性量化。该方法在合成与真实数据上展示了密度与聚类总结的有效性，平衡了灵活性与可解释性。对您而言，本文的投影思想与您熟悉的非参数统计和逆问题方法有潜在联系，但核心是贝叶斯计算与模型总结，属于统计计算方向。
- **关键技术**: `posterior projection`, `decision-theoretic summary`, `overparameterized Bayesian models`, `nonparametric density estimation`, `cluster summaries`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的'statistical computing'直接相关。您的武器库中'nonparametric statistics'和'minimax bounds'可用于分析投影估计的收敛性质，但核心的贝叶斯后验投影框架与您的very_familiar工具集（如逆问题、高维渐近）有距离，属于中期可做——需先在贝叶斯非参数（moderately_familiar之外）上补课。

### 20. [10.1007/s11222-026-10854-4](https://doi.org/10.1007/s11222-026-10854-4) · [arXiv](https://arxiv.org/abs/2503.18381) — Efficient inference in first passage time models
- **作者**: Sicheng Liu, Alexander Fengler, Michael J. Frank, Matthew T. Harrison
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究一类广泛使用的首达时间模型（first passage time models）的似然计算效率问题，具体针对广义漂移扩散模型（GDDMs）。GDDMs 通过一维随机微分方程（SDE）的首达时间描述选择与反应时间的联合分布，在计算认知神经科学中用于提取与决策过程相关的潜在心理参数。当前方法在漂移率随外生协变量（如脑区活动）动态变化时计算困难。作者提出一种快速灵活的算法，将每个试验划分为离散阶段，利用满足 Cherkasov 条件的 SDE 的解析结果计算阶段密度，再积分得到整体似然。数值实验表明，该方法在保持似然计算精度的同时，速度显著优于现有方法。对您而言，本文展示了统计计算中数值方法与解析技巧的结合，与您对统计计算（numerical methods, algorithm）的兴趣直接相关。
- **关键技术**: `Cherkasov condition`, `stage-wise density integration`, `first passage time likelihood`, `generalized drift diffusion model`, `numerical likelihood computation`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，是您 primary interest 中的 gateway reading。它展示了如何利用解析结果（Cherkasov 条件）加速数值似然计算，与您武器库中 'software development' 和 'inverse problems with random noise' 有直接接口——您可以用熟悉的数值方法（如自适应积分）进一步优化其 stage-wise 积分步骤。中期可做：若您想将类似的分阶段解析-数值混合策略推广到其他 SDE 模型，需先在 moderately_familiar 的 'M-estimation theory' 上建立对 SDE 参数估计的渐近理论理解。

### 21. [10.1007/s11222-026-10832-w](https://doi.org/10.1007/s11222-026-10832-w) · [arXiv](https://arxiv.org/abs/2507.01542) — Parsimonious Gaussian mixture models with piecewise-constant eigenvalue profiles
- **作者**: Tom Szwagier, Pierre-Alexandre Mattei, Charles Bouveyron, Xavier Pennec
- **期刊/来源**: Statistics and Computing
- **机构**: Université Côte d'Azur · Institut de Biologie Valrose
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对高维高斯混合模型（GMM）协方差矩阵过度参数化的问题，提出了一类新的简约GMM族，其核心思想是让协方差矩阵的特征值谱具有分段常数结构（即特征值按块取相同值）。该模型统一并推广了混合概率主成分分析（MPPCA）等低秩模型，允许任意指定的特征值重数序列，从而在完全GMM和球面GMM之间提供了灵活的中间地带。当特征值重数预先指定时，作者自然导出了期望最大化（EM）算法来学习混合参数；当重数未知时，他们提出了一个分量惩罚的EM算法，并证明了其单调性。实验部分在密度拟合、聚类和单图像去噪等无监督任务上展示了该模型在似然与简约性之间的优越权衡。对您而言，本文属于统计计算方向，其核心贡献在于提出了一种新的参数化策略并配以可证明单调的EM算法，这与您对统计计算（数值方法、算法）的兴趣直接相关。
- **关键技术**: `Expectation-Maximization (EM) algorithm`, `penalized EM`, `piecewise-constant eigenvalue profiles`, `mixtures of probabilistic principal component analyzers (MPPCA)`, `parsimonious covariance models`
- **为什么对您有用**: 本文属于统计计算（stat_computing）方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其核心贡献——提出新的参数化策略并配以可证明单调的EM算法——是您非常熟悉的算法设计问题。您可以用'软件开发和M-estimation理论'中的经验来评估该EM算法的收敛性和计算复杂度，甚至考虑将其推广到其他混合模型或张量分解场景。这是一个中期可做的方向：需要先在'moderately_familiar'的M-estimation理论上再熟悉一些，以严格分析该惩罚EM的统计性质（如一致性、收敛速率）。

### 22. [10.1007/s11222-026-10839-3](https://doi.org/10.1007/s11222-026-10839-3) · [arXiv](https://arxiv.org/abs/2306.15908) — Generalized Bayesian multidimensional scaling and model comparison
- **作者**: Jiarui Zhang, Jiguo Cao, Liangliang Wang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出广义贝叶斯多维缩放（GBMDS）框架，将经典MDS从欧氏距离和高斯噪声推广到灵活的非相似性度量与稳健的非高斯误差结构（如t分布），以提升模型灵活性和对异常值的鲁棒性。核心贡献在于设计了一种自适应退火序贯蒙特卡洛（ASMC）算法，该算法利用已有的MCMC提议分布，通过退火路径逐步逼近目标后验，能高效处理大规模数据，并提供边际似然的近似无偏估计，从而支持基于贝叶斯因子的模型比较。ASMC算法在计算上缓解了传统贝叶斯MDS的扩展性瓶颈，同时保留了不确定性量化的优势。模拟和真实数据实验表明，GBMDS在文本挖掘等领域的拟合精度和模型选择上优于现有方法。对您而言，本文的ASMC算法和贝叶斯模型比较框架是统计计算方向的具体技术贡献，您可借鉴其退火SMC设计思路来改进您在高维或因果推断中的后验采样或模型选择问题。
- **关键技术**: `adaptive annealed Sequential Monte Carlo`, `Bayesian model comparison via Bayes factors`, `non-Euclidean dissimilarity metrics`, `robust non-Gaussian error structures`, `marginal likelihood estimation`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其ASMC算法是您武器库中'very_familiar'的'软件发展'和'高维渐近'可攻的具体口子——您可尝试将退火SMC与您熟悉的einsum/tensor-contraction结合，加速高维后验计算。中期可做：需先在'moderately_familiar'的M估计理论中熟悉SMC的收敛性分析。

### 23. [10.1007/s11222-026-10875-z](https://doi.org/10.1007/s11222-026-10875-z) · [arXiv](https://arxiv.org/abs/2510.20617) — Approximating evidence via bounded harmonic means
- **作者**: Dana Naderi, Christian P Robert, Kaniav Kamary, Darren Wraith
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文针对贝叶斯模型选择中边际似然（模型证据）的计算难题，提出了一种新的调和均值估计器变体。标准调和均值估计器（HME）因可能具有无限方差而不可靠；作者基于Gelfand-Dey的标准化表示和Robert-Wraith的高后验密度（HPD）指示函数思路，用非重叠椭球体覆盖HPD区域，构造了椭球覆盖边际似然估计器（ECMLE）。ECMLE通过精确体积计算消除了无限方差问题，并能处理多峰后验分布。在多个数值例子中，ECMLE在方差控制和估计稳定性上优于THAMES及其改进版等近期方法。该方法本质上是数值积分技巧，不依赖特定模型结构，计算成本可控。对您而言，这是一篇统计计算方向的实用方法论文，其椭球覆盖策略可视为一种确定性数值积分方案，与您熟悉的软件开发和数值方法兴趣直接相关，但方法学新颖性有限，属于增量改进。
- **关键技术**: `harmonic mean estimator`, `Gelfand-Dey standardization`, `high posterior density region`, `ellipsoidal covering`, `marginal likelihood estimation`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。ECMLE的椭球覆盖策略是一种确定性数值积分方案，与您'very_familiar'的'软件开发和数值方法'武器库中的数值积分经验可对接——您可以用已有的数值优化和体积计算知识快速复现并评估其性能。**中期可做**：若想将此类覆盖思想推广到更高维或更复杂后验形状（如非凸HPD区域），需先在'moderately_familiar'的M估计理论中补足对后验几何的理解，但当前论文本身作为入门读物价值有限，仅适合快速浏览方法细节。

### 24. [10.1007/s11222-026-10835-7](https://doi.org/10.1007/s11222-026-10835-7) · [arXiv](https://arxiv.org/abs/2407.19236) — Approximate learning of parsimonious Bayesian context trees
- **作者**: Daniyar Ghani, Nicholas A. Heard, Francesco Sanna Passino
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对分类序列建模中常见的可交换性或一阶马尔可夫假设过于简化、无法捕捉长程复杂依赖的问题，提出了一种贝叶斯框架——Parsimonious Bayesian Context Trees (PBCT)。该模型属于变阶马尔可夫模型，通过丢弃冗余依赖并对序列上下文进行聚类，显著减少了参数数量，同时保持记忆效率，适用于数据流的实时处理。模型采用共轭先验分布，并通过一种计算高效的基于模型的凝聚聚类算法进行近似推断，避免了精确后验推断的高计算成本。在合成数据和真实数据（蛋白质序列、蜜罐计算机终端会话）上的实验表明，PBCT 在预测性能上优于现有的序列模型。本文的方法论核心在于将模型选择与聚类相结合，实现了稀疏性与表达力的平衡。对于您而言，该工作展示了如何将贝叶斯非参数思想与计算约束相结合，解决高维分类序列的在线学习问题，其凝聚聚类推断策略可能启发您在统计计算中设计更高效的算法。
- **关键技术**: `variable-order Markov model`, `agglomerative clustering`, `conjugate prior`, `Bayesian model averaging`, `online learning`
- **为什么对您有用**: 本文属于统计计算方向，直接关联您的 primary interest 中的 statistical computing。其核心贡献在于提出了一种计算高效的近似推断方法（凝聚聚类），用于处理高维分类序列的贝叶斯变阶马尔可夫模型。从您的技术武器库看，您对非参数统计和软件开发的熟悉程度（very_familiar）足以理解并复现其算法框架，但若要深入分析其聚类算法的理论性质（如收敛速度、一致性），则需要动用 moderately_familiar 的 M-estimation 理论。总体而言，这是一篇**中期可做**的论文：您可以先将其视为 gateway reading，了解变阶马尔可夫模型与凝聚聚类在序列建模中的结合方式，然后考虑是否将类似思路迁移到您熟悉的因果推断或高维统计问题中。

### 25. [10.1007/s11222-026-10885-x](https://doi.org/10.1007/s11222-026-10885-x) — Age-of-information in distributed systems caused by asynchronous computing modeled as parallel renewal processes
- **作者**: Adrian Redder
- **期刊/来源**: Statistics and Computing
- **机构**: Paderborn University
- **分类**: vol 36 · issue 3
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究分布式计算系统中异步参数更新导致的“信息年龄”（Age-of-Information, AoI）问题。将各处理器的计算时间建模为平行更新过程（parallel renewal processes），推导了离散AoI的分布和矩界，以及渐近均值的精确表达式和渐近方差的sharp界。核心贡献在于为异步算法的性能预测和误差控制提供了概率论基础。对您而言，该工作属于统计计算方向，其建模思路（平行更新过程）和渐近分析工具（更新理论、矩界）与您在高维统计和U-统计量中使用的概率工具相通，可作为gateway reading了解分布式系统中的统计建模问题。
- **关键技术**: `parallel renewal processes`, `age-of-information (AoI)`, `moment bounds`, `asymptotic variance`, `renewal theory`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其核心建模工具（平行更新过程）和渐近分析（矩界、方差界）与您very_familiar中的'high-dimensional asymptotics'和'inverse problems with random noise'有技术交集，但问题设定（分布式系统异步计算）对您是新的。作为gateway reading，本文清晰阐述了模型和结果，但未涉及您最擅长的U-统计量或因果推断。**暂不可做**：核心机器（更新理论、排队论）不在您的武器库中，需先补充renewal process和queueing theory的基础。

### 26. [10.1007/s11222-026-10833-9](https://doi.org/10.1007/s11222-026-10833-9) — Differential evolution variants for searching D- and A-optimal designs for nonlinear models in the bioscience
- **作者**: Lyuyang Tong, Weng Kee Wong
- **期刊/来源**: Statistics and Computing
- **机构**: Wuhan University · University of California, Los Angeles
- **分类**: vol 36 · issue 3
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究差分进化（DE）及其变体（JADE、CoDE、SHADE、LSHADE）在非线性模型最优设计问题中的表现，目标是为生物统计中常用的非线性模型寻找 D- 和 A-最优设计。核心机制是：DE 通过变异、交叉和选择操作在连续参数空间中搜索设计点，各变体在自适应参数控制（如 JADE 的存档机制）、组合策略（CoDE）或种群缩减（LSHADE）上有所改进。与统计领域的最优设计专用算法 REX 相比，LSHADE 在多数仿真场景下表现更优，收敛更快且设计效率更高。仿真使用了生物统计中常见的非线性模型（如 Emax、四参数 logistic 模型）。对您而言，本文属于统计计算中元启发式算法的应用比较，虽不直接涉及您核心兴趣中的理论方法，但可作为了解 DE 变体在统计优化中实用性的入门读物，且其算法实现思路对您开发统计软件中的优化模块有参考价值。
- **关键技术**: `Differential Evolution`, `JADE`, `SHADE`, `LSHADE`, `D-optimal design`, `A-optimal design`
- **为什么对您有用**: 本文属于统计计算方向，是您的 secondary interest 之一。作为 gateway reading，它清晰介绍了 DE 及其变体的基本机制，并对比了统计专用算法 REX，适合作为进入元启发式优化领域的入门材料。您的武器库中 'software development' 和 'nonparametric statistics' 足以理解其仿真框架，但核心的算法自适应机制（如参数存档、种群缩减）属于您 moderately_familiar 之外的领域，因此暂不可直接迁移到您的高阶 U-统计量计算问题中。值得花时间读全文以了解 DE 变体的实用表现，但无需深入理论细节。

## 其他  *(other, 3 篇)*

### 1. [10.1007/s11222-026-10874-0](https://doi.org/10.1007/s11222-026-10874-0) · [arXiv](https://arxiv.org/abs/2412.00720) — Fairness via independence: a (conditional) distance covariance framework
- **作者**: Ruifan Huang, Haixia Liu
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 3
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文从统计独立性角度研究算法公平性，利用（条件）距离协方差作为预测与敏感属性之间独立性的度量。方法是在模型训练中加入基于距离协方差的惩罚项以促进公平性。为提升计算效率，给出了经验（条件）距离协方差的矩阵形式以实现并行计算。理论上证明了经验（条件）距离协方差向总体版本的收敛性，为批量计算提供了保证。在多个真实数据集上的实验表明该方法能有效缩小公平性差距。对您而言，本文涉及高维统计中的距离协方差工具，但核心是机器学习公平性应用，与您的主要兴趣方向（因果推断、高维统计、U统计量）关联较弱。
- **关键技术**: `distance covariance`, `conditional distance covariance`, `fairness regularization`, `parallel computation`
- **为什么对您有用**: 本文属于机器学习公平性应用，与您的主要兴趣方向（因果推断、高维统计、U统计量）关联较弱。距离协方差虽与U统计量有技术联系，但本文未深入理论层面，且不涉及因果推断或效率理论。作为gateway reading价值有限，暂不可做。

### 2. [10.1007/s11222-026-10888-8](https://doi.org/10.1007/s11222-026-10888-8) — A clustered and sparse ising regression model for multivariate binary data
- **作者**: Francis K. C. Hui, Ding Ding
- **期刊/来源**: Statistics and Computing
- **机构**: Australian National University
- **分类**: vol 36 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对多元二值响应数据，提出了一种带聚类与稀疏约束的 Ising 回归模型。模型将每个二值响应的主效应参数化为协变量的线性函数，并通过 pairwise 交互项刻画响应间的条件依赖结构。为同时实现系数聚类（同一协变量对不同响应的影响相似）和变量选择（协变量与交互项稀疏），作者在损失函数中引入 adaptive fused lasso 与 adaptive lasso 惩罚。通过重参数化技巧，将带结构惩罚的估计问题转化为一个标准的 adaptive lasso 逻辑回归，从而可高效求解。模拟与鱼类调查数据应用表明，该方法在系数聚类与稀疏性上优于现有 Ising 回归模型，并得到可解释的物种-环境关系。本文方法学贡献在于将聚类与稀疏惩罚结合到 Ising 模型，但整体属于应用导向的统计建模，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术交集。
- **关键技术**: `Ising regression model`, `adaptive fused lasso`, `adaptive lasso`, `logistic regression reparametrization`, `multivariate binary data`
- **为什么对您有用**: 本文属于统计计算与建模方向，但核心方法（Ising 模型+结构化惩罚）与您的主要兴趣（因果推断、高维统计、U-统计量）无直接技术连接。您武器库中的 minimax bounds 或高维渐近工具难以直接攻入该文的估计问题；若想进入生态/心理测量领域的多元二值数据分析，本文可作为入门读物，但需额外补充 Ising 模型与伪似然估计的背景。暂不可做：核心机器（Ising 模型的结构化惩罚估计）不在武器库中。

### 3. [10.1007/s11222-026-10877-x](https://doi.org/10.1007/s11222-026-10877-x) — A model-based feature selection approach for type 2 Diabetes Mellitus diagnosis using Heart Rate and Systolic Arterial Pressure series measures
- **作者**: Javier Roca-Pardiñas, María J. Lado, Leandro Rodríguez-Liñares
- **期刊/来源**: Statistics and Computing
- **机构**: Universidade de Vigo
- **分类**: vol 36 · issue 3
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出一种基于 logistic 广义可加模型（GAM）的特征选择方法，用于高维分类问题。方法以 BIC 和 AUC 为模型评价准则，通过搜索最优协变量子集来提升分类性能。将该方法应用于一项临床研究，利用静息和主动站立两种条件下的心率（HP）、收缩压（SAP）时间序列特征以及压力反射敏感性（BRS）指标，区分 2 型糖尿病（T2DM）患者与健康对照。最优模型仅选择 3-5 个协变量，前 20 个模型的 AUC 介于 0.918 至 0.931 之间，最佳三变量模型的灵敏度为 0.816、假阳性率为 0.184。该方法在变量选择上具有可解释性，但未涉及因果推断或高维统计的深层理论。对您而言，本文属于应用型工作，方法学新颖性有限，与您的主要兴趣方向（因果推断、高维统计、U-统计量等）无直接关联。
- **关键技术**: `Generalized Additive Models (GAM)`, `Bayesian Information Criterion (BIC)`, `Area Under the ROC Curve (AUC)`, `feature selection`
- **为什么对您有用**: 本文属于统计计算与医学应用交叉，但方法学贡献较浅（基于 GAM 的变量选择），未涉及您核心兴趣中的因果识别、高维渐近或效率理论。武器库中 '非参数统计' 和 '软件工程' 可复现其分析流程，但无实质理论挑战。暂不可做：核心问题（变量选择的因果解释或高维一致性）不在本文框架内。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

