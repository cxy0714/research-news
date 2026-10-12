# Stat. Comput. — Vol 36  Issue 6  ·  2026-10-13

- 共 6 篇 · Statistics and Computing
- 目录核对 ✅ 6 篇全部抓到（对照 OpenAlex 6 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Statistics and Computing》整体上呈现出两条主线：一是围绕估计与推断的**算子化与几何化**框架，二是针对**复杂数据结构（删失、缺失、稀疏）的算法设计与计算可行性**。前者以首篇统计交换子论文为代表，将效率下界与正则化调参统一到传输算子的交换子语言中；后者则覆盖了左截断区间删失生存数据的NPMLE、协方差矩阵补全、稀疏列联表精确检验的SAT采样，以及Tsallis熵估计与拟合优度检验。此外，贝叶斯非参数Hawkes过程模型独立成线，聚焦极端事件聚类的分层建模。

最值得展开的是统计交换子一文。它构造了得分-传输算子Λ_θ，并证明其与估计量乘法算子的交换子精确等于参数导数项，从而将经典Cramér–Rao下界重新解释为L²(P_θ)中的角度几何问题。这一框架不仅统一了有偏估计与参数依赖支撑的情形，还直接导出了基于交换子的非重采样正则化调参方法——对理解估计效率的几何本质和设计新调参准则都有直接参考价值。另一条突出主线是**稀疏与缺失结构下的计算策略**：协方差补全（AuxCov）将缺失相关性估计转化为回归问题，用辅助变量预测并正则化观测值；SAT采样则绕开Markov基的连通性要求，用布尔电路编码纤维并混合局部移动保证平稳分布，两者分别回应了高维协方差估计和稀疏列联表精确检验中的计算瓶颈。生存数据NPMLE一文通过乘积限重参数化解析处理左截断与右删失，仅对区间删失迭代，显著减少EM迭代次数，属于同一计算效率主题下的具体推进。

与因果推断最贴近的是统计交换子框架——其传输算子与得分协方差几何可直接迁移到半参数效率理论中；半参数效率方向还可关注Tsallis熵估计中基于分位数函数的相合估计量及其在拟合优度检验中的应用；高维方向则优先看AuxCov的协方差补全思路，以及SAT采样对稀疏表结构零问题的处理。贝叶斯非参数Hawkes过程虽主题独立，但其分层GPD标记模型对极端事件幅度的部分合并估计，对处理簇内小样本的层次模型设计有借鉴意义。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1007/s11222-026-10989-4](https://doi.org/10.1007/s11222-026-10989-4) · [arXiv](https://arxiv.org/abs/2602.01228) — Estimation of Tsallis entropy and its applications to goodness-of-fit tests
- **作者**: Siddhartha Chakraborty, Asok K. Nanda, Narayanaswamy Balakrishnan
- **期刊/来源**: Statistics and Computing
- **机构**: University of Kalyani · Indian Institute of Science Education and Research Kolkata · Atilim University · McMaster University
- **分类**: vol 36 · issue 6
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究 Tsallis 熵的估计问题，提出了基于高阶样本间距的四种估计量，并扩展到渐进 II 型删失数据。通过 Monte-Carlo 模拟比较了完整和删失样本下各估计量的偏差和均方误差，并考察了其对正态和指数模型离群值的稳健性。此外，基于分位数函数提出另一种 Tsallis 熵估计量，证明了其相合性和渐近正态性，并通过模拟与前述估计量比较。文章还引入基于间距的 Tsallis 散度估计量，并据此构建正态和指数分布的拟合优度检验，模拟显示所提检验性能良好。最后，提出了渐进 II 型删失下的指数性检验，并与现有基于熵的检验比较，同时用真实数据进行了说明。
- **关键技术**: `higher-order sample spacings`, `Tsallis entropy`, `Tsallis divergence`, `goodness-of-fit tests`, `progressive type-II censoring`, `quantile-based estimation`
- **为什么对您有用**: 本文属于假设检验与熵估计的交叉方向，与您的 hypothesis testing 兴趣直接相关；其基于高阶间距的估计思路可联系到您熟悉的 higher-order U-statistics 技术，例如用 U-statistic 投影分析估计量的渐近性质。从武器库看，您可用 very_familiar 的非参数统计和 U-statistic 工具立即评估其理论性质，属于立即可做的范畴。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1007/s11222-026-10991-w](https://doi.org/10.1007/s11222-026-10991-w) — Statistical commutators with applications to estimation, inference, and regularization tuning
- **作者**: Ivo D. Dinov, Eric Tatt Wei Ho, S. Ejaz Ahmed
- **期刊/来源**: Statistics and Computing
- **机构**: University of Michigan · Universiti Teknologi Petronas · Brock University
- **分类**: vol 36 · issue 6
- 相关性 7/10 · novelty: `minor`
- **摘要**: 本文提出一个经典算子框架——统计交换子，用于研究估计与正则化中的非交换性。在受控参数模型下，定义得分-传输算子 Λ_θ g = ∂_θ g + g S_θ，其与估计量乘法算子的交换子满足 [Λ_θ, M_T]g = (∂_θ T)g，从而精确刻画了交换子项所捕获的内容：对于无显式 θ 依赖的标准估计量，传输交换子为零，效率/方差下界来自得分-协方差几何而非非零交换子。由此得到几何 Cramér–Rao 不等式和 L^2(P_θ) 中效率的角度解释，并给出传输恒等式成立的条件，涵盖有偏和参数依赖支撑的情形，使经典无偏界 Var_θ(T)I(θ)≥1 成为特例。主要应用贡献是基于交换子的非重采样准则，用于选择二次模型和广义线性模型中的正则化强度；由于朴素交换子退化，作者引入两个非平凡交换子族 [A, H_λ^{-1}P] 和 [P, H_λ^{-1}A]，并用有效自由度加权的钟形平衡因子避免边界最优。模拟研究表明，该交换子得分在某些 GLM 设置下可与交叉验证竞争，但在线性模型结构化惩罚下具有场景和顺序依赖性；作者还识别了 Type II 构造的块算子不对称性并讨论稳定化策略。对您而言，该文将统计估计的几何与算子代数结合，可能为您的统计计算兴趣提供新的正则化选择视角，但方法新颖性有限，更多是概念框架而非突破性理论。
- **关键技术**: `statistical commutator`, `score-transport operator`, `Cramér–Rao inequality`, `regularization tuning`, `effective degrees of freedom`, `GLM`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关，可作为该方向的入门或拓展阅读。您的武器库（如非参数统计、M-估计理论）足以理解其核心框架，但该文的方法论贡献偏向概念整合而非新理论，因此 follow-up 价值有限。若您对正则化选择或算子方法感兴趣，可中期探索其与您 moderately_familiar 的 semiparametric theory 的结合，但当前暂不建议深入。

### 2. [10.1007/s11222-026-10984-9](https://doi.org/10.1007/s11222-026-10984-9) — A fast and stable algorithm for non-parametric maximum likelihood estimation of survival functions for left-truncated and interval-censored data
- **作者**: Zachary Waller, Adele H. Marshall, Frank Kee, Felicity Lamrock
- **期刊/来源**: Statistics and Computing
- **机构**: Queen's University Belfast · Ontario Tech University
- **分类**: vol 36 · issue 6
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对左截断且区间删失（LTIC）数据，提出一种快速且稳定的非参数极大似然估计（NPMLE）算法。通过将生存函数估计量重新参数化为乘积限（product-limit）形式，左截断和右删失可以解析地处理，而区间删失仍通过算法迭代处理，从而显著减少EM算法的迭代次数。结合改进的迭代凸最小化（ICM）步骤（Pan 1999），该算法能够处理更大规模、更复杂的LTIC数据。通过模拟研究评估了算法性能，并应用于马萨诸塞州健康护理小组研究数据，展示了相对于其他算法的有效性。该工作属于统计计算方向，对您而言，其乘积限重参数化与EM/ICM结合的思路，可借鉴到您熟悉的软件开发和数值方法中，用于处理复杂删失数据的计算效率问题。
- **关键技术**: `product-limit reparameterization`, `EM algorithm`, `iterative convex minorant (ICM)`, `non-parametric maximum likelihood estimation`, `left-truncated and interval-censored data`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的主要兴趣之一。其核心贡献在于算法设计（乘积限重参数化+EM/ICM），而非新统计理论，但计算效率的提升对实际应用（如流行病学队列研究中的生存分析）有直接价值。您可以用 very_familiar 的软件开发和数值方法技能，快速复现并测试该算法，甚至将其扩展到更复杂的删失模式。因此，这是一个立即可做的入门级计算论文，值得阅读全文以获取算法细节和实现技巧。

### 3. [10.1007/s11222-026-10963-0](https://doi.org/10.1007/s11222-026-10963-0) · [arXiv](https://arxiv.org/abs/2402.05767) — Covariance matrix completion via auxiliary information
- **作者**: Joseph R. Steneman, Giuseppe Vinci
- **期刊/来源**: Statistics and Computing
- **机构**: University of Notre Dame
- **分类**: vol 36 · issue 6
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出 AuxCov 方法，用于在结构缺失数据下估计完整协方差矩阵，即某些变量对没有联合观测时，传统样本协方差矩阵无法定义。核心思想是利用辅助变量（如神经元间距离）与相关性的关系，通过回归预测缺失的相关性估计，并正则化已观测的相关性。实现上支持参数与非参数回归，并给出调参和不确定性量化流程。模拟和神经科学大规模数据实验表明，AuxCov 能有效恢复完整协方差矩阵并提升估计精度。该方法将协方差补全问题转化为回归问题，为统计计算与高维协方差估计提供了新工具。
- **关键技术**: `covariance matrix completion`, `auxiliary variables`, `nonparametric regression`, `regularization`, `uncertainty quantification`
- **为什么对您有用**: 本文属于统计计算方向，与您对统计计算（数值方法、算法）的兴趣直接相关；同时协方差估计是高维统计的核心问题，可作为您在高维协方差估计中处理缺失数据的参考。您可用 very_familiar 的软件开发和 minimax 界工具来评估其回归估计的收敛率，或将其与您熟悉的协方差估计理论对比，中期可做。

### 4. [10.1007/s11222-026-10985-8](https://doi.org/10.1007/s11222-026-10985-8) · [arXiv](https://arxiv.org/abs/2511.05709) — SAT-sampling for statistical significance testing in sparse contingency tables
- **作者**: Patrick Scharpfenecker, Tobias Windisch
- **期刊/来源**: Statistics and Computing
- **机构**: Kempten University of Applied Sciences
- **分类**: vol 36 · issue 6
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对稀疏列联表中精确条件检验的抽样问题，提出基于 SAT 求解器的替代方案。传统 Markov basis MCMC 方法需要计算连接所有纤维的完整基，在稀疏或存在结构零时计算不可行且链收敛慢。作者将纤维编码为布尔电路，利用现代 SAT 采样器随机生成表格，并分析了 SAT 采样可能引入的抽样偏差，提供诊断方法和缓解措施。进一步提出混合 MCMC 方案，将 SAT 提议与局部移动结合，确保正确的平稳分布，且不要求局部移动连通，特别适用于结构零场景。在多个基准（包括小规模及含大量结构零的复杂表格）上，该方法能提供可靠的条件 p 值，且常优于依赖预计算 Markov 基的采样器。对您而言，本文属于统计计算方向，其 SAT 编码与混合 MCMC 思路可迁移至您在高维或因果推断中遇到的离散约束抽样问题。
- **关键技术**: `SAT sampling`, `Boolean circuit encoding`, `Markov basis MCMC`, `hybrid MCMC`, `conditional exact tests`, `structural zeros`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中 statistical computing 直接相关。您可用 very_familiar 的软件开发和算法实现能力快速复现其 SAT 编码与混合 MCMC 流程，评估其在您关注的稀疏列联表或因果推断中离散数据场景的适用性。中期可做：若需深入分析 SAT 采样的偏差界，可结合您 moderately_familiar 的 M-estimation 理论进行理论刻画。暂不可做：若涉及大规模 SAT 求解的复杂度分析，则需补充计算复杂性理论工具。

## 其他  *(other, 1 篇)*

### 1. [10.1007/s11222-026-10981-y](https://doi.org/10.1007/s11222-026-10981-y) — Bayesian modelling of clustered extreme events using a nonparametric Hawkes process
- **作者**: Gordon J. Ross, Dean Markwick
- **期刊/来源**: Statistics and Computing
- **机构**: University of Edinburgh · University College London
- **分类**: vol 36 · issue 6
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一个贝叶斯点过程模型，用于建模极端事件的时间聚类及其幅度局部变化。模型用自激 Hawkes 过程刻画极端事件的发生率，用 Dirichlet 过程非参数地学习时间激发模式，并用广义帕累托分布（GPD）建模极端事件的幅度，其中分层标记模型允许幅度在不同 Hawkes 簇间变化。分层规范实现部分合并，即使在簇内观测数很少时也能更准确地估计 GPD。作者开发了 MCMC 算法对分层模型进行采样，模拟研究证实两个灵活组件在数据生成机制包含相应特征时能提升预测，四个真实数据集上非参数 Hawkes 模型加分层 GPD 标记在留出预测性能上优于其他变体。对您而言，该文属于统计计算与贝叶斯非参数方法的交叉应用，与您的主要兴趣（统计计算、非参数理论）有间接关联，但并非核心方向。
- **关键技术**: `Hawkes process`, `Dirichlet process`, `generalized Pareto distribution`, `hierarchical Bayesian model`, `MCMC`
- **为什么对您有用**: 本文属于统计计算与贝叶斯非参数方法的交叉应用，与您的主要兴趣（统计计算、非参数理论）有间接关联，但并非核心方向。作为统计计算方向的入门读物，它展示了 MCMC 在复杂分层模型中的应用，但方法学新颖性有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

