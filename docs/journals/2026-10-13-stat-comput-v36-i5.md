# Stat. Comput. — Vol 36  Issue 5  ·  2026-10-13

- 共 16 篇 · Statistics and Computing
- 目录核对 ⚠️ 疑似漏 8 篇（对照 OpenAlex 23 篇）：10.1007/s11222-026-10955-0、10.1007/s11222-026-10962-1、10.1007/s11222-026-10964-z、10.1007/s11222-026-10967-w、10.1007/s11222-026-10966-x 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《统计计算》第36卷第5期的16篇论文，主线大致可归为四类：**统计计算与采样算法**（约7篇，涵盖MCMC、ABC、HMC、约束采样等）、**高维与稀疏建模**（约4篇，涉及双聚类、列联表、可加模型、分位数回归）、**假设检验与预测推断**（2篇，核两样本检验与共形预测）、以及**因果与缺失数据**（1篇，半参数模型平均）。此外还有少量应用导向的工作（如小域估计、函数型数据分析、传染病建模）。

最突出的一条主线是**采样与MCMC方法的效率改进**，占据了近半篇幅。`Rare event ABC-SMC²` 将rare event SMC嵌入SMC²框架，规避了标准ABC在高维下的指数缩放；`Faster Hamiltonian Monte Carlo by learning leapfrog scale` 通过离线经验分布校准HMC的步长与步数，避免在线自适应；`Piecewise deterministic sampling for constrained distributions` 引入mirror map构造满足凸约束的PDMP；`Kinetic interacting particle Langevin Monte Carlo` 则提出相互作用欠阻尼Langevin算法，在潜变量模型上给出非渐近收敛速率。这四篇从不同角度切入采样效率问题，但工具差异明显（SMC、HMC、PDMP、Langevin），值得对照阅读。另一条值得注意的线索是**U-统计量与核方法的计算复杂度**：`On computing and the complexity of computing higher-order U-statistics, exactly` 建立了U-统计量分解与Einstein求和、treewidth的联系，而`A fast and effective kernel two-sample test` 则利用核嵌入聚合统计量降低两样本检验的计算负担——两篇虽主题不同，但都触及核方法的计算瓶颈。

第二主线是**高维稀疏与稳健估计**。`Sparse convex biclustering` 在凸双聚类中加入group-sparsity惩罚，同时估计行/列划分与特征选择；`Loglinear modelling of huge contingency tables` 针对极端稀疏高维列联表提出空单元格子采样方案，处理6.6×10³⁸规模的表；`Fast robust additive models using gamma-divergence` 用gamma散度对REML准则加权，在异常值下拟合可加模型；`Semiparametric model averaging for high-dimensional quantile regression with nonignorable nonresponse` 则结合半参数倾向得分与模型平均处理缺失数据。这四篇共享「高维+稳健/稀疏」的框架，但各自应对的挑战不同（双聚类结构、单元格爆炸、异常值、缺失机制），其中最后一篇与因果推断直接相关。

若按主题优先阅读：因果推断方向看 `Semiparametric model averaging...`（缺失机制与模型平均）；半参数/非参方向看 `Fast robust additive models...`（gamma散度加权）与 `Analyzing functional data...`（混合协方差结构）；高维方向看 `Sparse convex biclustering` 与 `Loglinear modelling...`；计算复杂度方向看 `On computing...U-statistics` 与 `A fast and effective kernel two-sample test`。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1007/s11222-026-10953-2](https://doi.org/10.1007/s11222-026-10953-2) · [arXiv](https://arxiv.org/abs/2509.00464) — Semiparametric model averaging for high-dimensional quantile regression with nonignorable nonresponse
- **作者**: Wei Xiong, Dianliang Deng, Dehui Wang
- **期刊/来源**: Statistics and Computing
- **机构**: Liaoning University · University of Regina
- **分类**: vol 36 · issue 5
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对高维分位数回归中响应变量存在不可忽略缺失（nonignorable nonresponse）的问题，提出一种半参数模型平均（SMA）方法。目标是在候选模型集合中自动选择或加权组合，使得估计量渐近等价于最优的正确模型。方法采用两阶段方案：第一阶段用半参数似然估计缺失机制（倾向得分），第二阶段用半参数加权（如逆概率加权）组合候选模型，从而放松对响应者条件分布的参数假设。理论上证明了在复杂缺失机制下，SMA估计量具有渐近最优性（即能集中到渐近最优正确模型）。模拟和实证研究表明该方法在有限样本下有效。对您而言，该方法将缺失数据处理与模型平均结合，属于因果推断中处理缺失协变量/结果的估计问题，且其半参数加权思路与您的semiparametric theory和efficiency theory兴趣点相关。
- **关键技术**: `semiparametric model averaging`, `quantile regression`, `nonignorable missingness`, `inverse probability weighting`, `semiparametric likelihood`
- **为什么对您有用**: 本文属于因果推断中缺失数据处理的估计问题，与您的primary interest中的causal inference（特别是缺失机制和加权估计）直接相关。您可以用very_familiar中的semiparametric theory和M-estimation理论来审视其渐近最优性证明，或考虑将其与您的higher-order U-statistics工具结合，分析其估计量的高阶性质。中期可做：需先熟悉quantile regression的特定技术细节。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1007/s11222-026-10960-3](https://doi.org/10.1007/s11222-026-10960-3) — Fast robust additive models using gamma-divergence
- **作者**: Francis K. C. Hui, Ding Ding, Shonosuke Sugasawa
- **期刊/来源**: Statistics and Computing
- **机构**: Australian National University · Keio University
- **分类**: vol 36 · issue 5
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于 gamma-divergence 的稳健可加模型（GDAM），用于在存在异常值时拟合连续响应与多个预测变量的非线性关系。方法将惩罚样条系数视为随机效应，对可加模型的 REML 准则应用 gamma-divergence，从而自适应地通过归一化幂密度权重降低异常点的影响。估计采用 minorization-maximization (MM) 算法，计算高效且可扩展，并同时提供不确定性量化。模拟和联邦拨款数据应用表明，GDAM 在多种污染程度下与现有稳健/非稳健方法性能相当或更优，且计算更快。对您而言，该方法将稳健统计与半参数可加模型结合，其 MM 算法和权重机制可能对您在高维或纵向因果推断中的稳健估计有借鉴意义。
- **关键技术**: `gamma-divergence`, `penalized splines`, `restricted maximum likelihood`, `minorization-maximization algorithm`, `robust additive models`
- **为什么对您有用**: 本文属于半参数/非参数回归的稳健估计方法，与您的非参数与半参数理论兴趣直接相关。您可以用 very_familiar 的非参数统计和 M-estimation 理论来审视其 gamma-divergence 估计的影响函数和稳健性性质，并考虑将其扩展到因果推断中的稳健 nuisance 估计。中期可做：结合您 moderately_familiar 的 semiparametric theory，推导 GDAM 在部分线性模型中的半参数效率界。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1007/s11222-026-10969-8](https://doi.org/10.1007/s11222-026-10969-8) · [arXiv](https://arxiv.org/abs/2110.03118) — A fast and effective kernel two-sample test for large-scale data
- **作者**: Hoseung Song, Hao Chen
- **期刊/来源**: Statistics and Computing
- **机构**: Korea Advanced Institute of Science and Technology · University of California, Davis
- **分类**: vol 36 · issue 5
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对大规模高维数据提出一种快速有效的核两样本检验。现有方法如MMD及其大规模变体在计算上昂贵或对某些常见备择假设功效不足。新检验基于核嵌入的某种聚合统计量，无需通过数据分裂优化核带宽等参数，对高维更稳健。数值实验表明其在合成和真实数据上均表现良好。该方法可能利用U-统计量或V-统计量的分解来降低计算复杂度，并可能涉及随机特征近似或分块策略。对您而言，该检验的构造与理论分析（如功效和计算复杂度）与您在高阶U-统计量和假设检验方面的兴趣直接相关。
- **关键技术**: `kernel two-sample test`, `maximum mean discrepancy`, `U-statistics`, `high-dimensional robustness`, `bandwidth-free test`
- **为什么对您有用**: 本文属于假设检验方向，直接关联您的主要兴趣。其方法可能基于U-统计量，您可用高阶U-统计量的树宽/张量收缩视角分析其计算效率，并验证其在高维下的功效界是否最优。该文为中期可做：需先熟悉核方法在假设检验中的应用（moderately_familiar中的semiparametric理论可辅助）。

### 2. [10.1007/s11222-026-10936-3](https://doi.org/10.1007/s11222-026-10936-3) — Generative conformal prediction under multiple covariate shifts
- **作者**: Meifang Lan, Tong Wang, Siming Zheng, Yuanyuan Lin
- **期刊/来源**: Statistics and Computing
- **机构**: Chinese University of Hong Kong · Southeast University
- **分类**: vol 36 · issue 5
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究在多个目标数据集面临不同协变量偏移时的预测推断问题，这在经济和生物医学应用中很常见。作者提出一种两步生成式共形预测（GCP）方法，能有效处理类别不平衡数据。他们建立了所提方法覆盖有效性的通用结果，阐明了条件生成学习过程对覆盖有效性的影响。此外，他们证明了GCP区间的稳健性，并提供了理论证据表明其优于基于密度比的方法。数值研究（包括模拟和真实数据）将所提方法与现有基于密度比的方法进行比较，实证说明了其有效性。
- **关键技术**: `generative conformal prediction`, `covariate shift`, `coverage validity`, `density ratio`, `conditional generative learning`
- **为什么对您有用**: 本文属于预测推断与分布偏移的交叉领域，与您的主要兴趣（假设检验、非参数/半参数理论）相关，特别是共形预测的覆盖有效性证明涉及非参数推断。您可以用非常熟悉的非参数统计工具（如经验过程理论）来审视其覆盖保证的有限样本性质，或探索其与更高阶U统计量的联系。中期可做：若想深入生成式模型的理论性质，需在中等熟悉的半参数理论上加强。

## 统计计算 / 算法  *(stat_computing, 8 篇)*

### 1. [10.1007/s11222-026-10977-8](https://doi.org/10.1007/s11222-026-10977-8) · [arXiv](https://arxiv.org/abs/2601.01757) — Sparse convex biclustering
- **作者**: Jiakun Jiang, Dewei Xiang, Binhuan Wang, Wei Liu, Chenliang Gu
- **期刊/来源**: Statistics and Computing
- **机构**: Beijing Normal University · Beijing Normal University, Zhuhai · AbbVie (United States) · Sichuan University
- **分类**: vol 36 · issue 5
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出 Sparse Convex Biclustering (SpaCoBi)，在凸双聚类准则中加入特征向量的 group-sparsity 惩罚，从而同时估计行/列划分并选择一组共同的信息特征。该方法通过无标签的稳定性调参过程评估棋盘状划分和特征集的复现性，避免了传统调参对标签的依赖。数值实验涵盖模拟、小鼠嗅球和 TCGA 泛癌基因表达数据，验证了其在棋盘结构恢复和全局特征选择上的有效性。但作者指出，当前稠密的 Sylvester 更新限制了其在两个维度都很大时的可扩展性。
- **关键技术**: `convex biclustering`, `group-sparsity penalty`, `stability-based tuning`, `Sylvester equation`, `feature selection`
- **为什么对您有用**: 本文属于统计计算方向，涉及凸优化和矩阵更新，与您的统计计算兴趣相关；但方法本身是聚类而非因果推断，且可扩展性受限。作为入门读物，它清晰展示了双聚类问题的建模和计算挑战，但武器库中的工具（如高阶 U 统计、张量收缩）难以直接用于改进其稠密 Sylvester 更新，因此暂不可做。

### 2. [10.1007/s11222-026-10965-y](https://doi.org/10.1007/s11222-026-10965-y) · [arXiv](https://arxiv.org/abs/2508.18037) — Enhancing differentially private linear regression via public second-moment
- **作者**: Zilong Cao, Hai Zhang
- **期刊/来源**: Statistics and Computing
- **机构**: Northwest University
- **分类**: vol 36 · issue 5
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究在差分隐私（DP）约束下，利用公开数据的二阶矩信息来提升线性回归中普通最小二乘估计（OLSE）的效用。传统基于充分统计量扰动（SSP）的DP方法仅依赖私有数据添加噪声，导致效用显著下降。作者提出先利用公开二阶矩矩阵对私有数据进行变换和裁剪，再计算变换后的SSP-OLSE，从而改善数据矩阵的条件数，提高估计精度和鲁棒性。理论上，作者推导了所提方法与标准SSP-OLSE相对于非DP OLSE的误差界，证明了其改进的鲁棒性和准确性。实验在合成和真实数据集上验证了方法的效用和有效性。该工作属于统计计算与隐私保护交叉领域，对您而言，其利用公开数据改善病态问题的思路与您在高维统计和数值方法上的兴趣相关，但方法本身并非您核心研究方向的直接延伸。
- **关键技术**: `sufficient statistics perturbation`, `second-moment matrix`, `condition number`, `differential privacy`, `linear regression`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 相关，但更偏向隐私保护应用。作为 gateway reading，它展示了如何利用公开数据改善病态线性回归问题，但方法学深度一般。您的武器库（如高维渐近、数值方法）足以理解其理论，但该问题并非您核心研究领域，可能不值得深入展开。

### 3. [10.1007/s11222-026-10959-w](https://doi.org/10.1007/s11222-026-10959-w) · [arXiv](https://arxiv.org/abs/2603.07288) — Loglinear modelling of huge contingency tables
- **作者**: Veronica Vinciotti, Ernst C. Wit
- **期刊/来源**: Statistics and Computing
- **机构**: University of Trento · Università della Svizzera italiana
- **分类**: vol 36 · issue 5
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维列联表（变量数多导致单元格数指数爆炸、绝大多数为空）中的高阶对数线性模型推断问题，提出两种基于空单元格子采样的高效估计方法。首先在零膨胀泊松抽样方案下推导似然，并通过迭代加权最小二乘（IRLS）最大化，得到一致且接近有效的估计量，适用于中等规模表。为应对维度增长带来的计算不稳定，作者进一步提出嵌套病例对照多项抽样结合退化逻辑回归的方法，牺牲部分效率换取可扩展性，可处理任意大的列联表。方法在 General Social Survey 数据上验证，该数据含 15014 个观测、69 维列联表、总单元格数达 6.6×10^38。对您而言，本文展示了在极端稀疏高维离散数据下通过巧妙抽样设计实现可计算推断的思路，与您在高维统计和统计计算方面的兴趣相关，但方法本身并非您核心武器库中的工具。
- **关键技术**: `zero-deflated Poisson sampling`, `iteratively re-weighted least squares (IRLS)`, `nested case-control multinomial sampling`, `degenerate logistic regression`, `subsampling empty cells`
- **为什么对您有用**: 本文属于统计计算方向，涉及高维稀疏数据的计算策略，与您的 primary interest 中的 statistical computing 和 high-dimensional statistics 相关。但方法核心是抽样设计而非您熟悉的 U-statistics 或 RMT 工具，因此作为 gateway reading 了解计算 tradeoff 尚可，但直接可迁移性有限。

### 4. [10.1007/s11222-026-10979-6](https://doi.org/10.1007/s11222-026-10979-6) · [arXiv](https://arxiv.org/abs/2211.02172) — Rare event ABC-SMC$$^{2}$$
- **作者**: Ivis Kerama, Thomas Thorne, Richard G. Everitt
- **期刊/来源**: Statistics and Computing
- **机构**: University of Exeter · University of Surrey · University of Warwick
- **分类**: vol 36 · issue 5
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的 ABC-SMC 方法（ABC-SMC²），用于在高维数据下进行近似贝叶斯推断。标准 ABC 方法的 Monte Carlo 点数随数据维度指数增长，而 Prangle et al. (2018) 提出的 rare event SMC 方法可避免这一指数缩放，但基于 MCMC 框架。本文将 rare event SMC 嵌入 SMC 框架，类似于 SMC² (Chopin et al. 2013)，从而减少调参负担。方法在 toy example 和 duplication-divergence 随机图模型（用于蛋白质相互作用网络）上进行了演示，并与现有 ABC-SMC 方法比较。核心贡献在于将 rare event SMC 的维度优势与 SMC 的自动调参特性结合，为高维隐式模型推断提供更实用的工具。对您而言，该方法涉及 sequential Monte Carlo 和计算效率的权衡，与您统计计算兴趣中的算法设计相关，但并非您核心理论方向。
- **关键技术**: `Approximate Bayesian computation`, `Sequential Monte Carlo`, `Rare event simulation`, `SMC^2`, `Implicit models`
- **为什么对您有用**: 本文属于统计计算方向，涉及 SMC 算法设计和计算效率，与您的 primary interest 中 statistical computing 相关。但作为 gateway reading，本文对您作为数学统计学家而言，入门性一般，因为需要熟悉 ABC 和 SMC 背景。您的武器库（如软件开发和数值方法）足以理解算法实现，但缺乏 SMC 理论深度，可能难以快速评估其理论贡献。建议作为了解 ABC 高维推断进展的补充阅读，但不必深入。

### 5. [10.1007/s11222-026-10972-z](https://doi.org/10.1007/s11222-026-10972-z) · [arXiv](https://arxiv.org/abs/1810.04449) — Faster Hamiltonian Monte Carlo by learning leapfrog scale: an offline randomized solution
- **作者**: Changye Wu, Pierre Pudlo, Christian P. Robert, Julien Stoehr
- **期刊/来源**: Statistics and Computing
- **机构**: Centre National de la Recherche Scientifique · Centre de Recherche en Mathématiques de la Décision · Université Paris Sciences et Lettres · Université Paris Dauphine-PSL · Aix-Marseille Université · Institut de Mathématiques de Marseille · University of Warwick · Centre de Recherche en Économie et Statistique 等
- **分类**: vol 36 · issue 5
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于离线经验校准的哈密顿蒙特卡洛（HMC）方法 eHMC，目标是在无需在线自适应和手动 burn-in 诊断的情况下提高采样效率。方法核心是：在预热阶段，通过重要性采样构造离散化参数（leapfrog 步长与步数）的经验分布，该分布由带 tempering 的 Population Monte Carlo 方案结合 flexible 参数变分族（如 normalizing flows）得到。校准完成后，算法通过固定混合分布的 HMC 核混合定义齐次马尔可夫链，从而严格保持目标分布不变。数值实验表明，在离线分布能有效概括有用积分时间的情况下，eHMC 的采样效率（按 leapfrog 步数归一化）可与 NUTS 相当或更优。该方法将随机化 leapfrog 参数与离线学习相结合，避免了在线调参的方差与诊断负担。对您而言，本文属于统计计算方向，其离线校准与重要性采样思想可能对您在高维或复杂模型中的 MCMC 应用有参考价值。
- **关键技术**: `Hamiltonian Monte Carlo`, `importance sampling`, `Population Monte Carlo`, `normalizing flows`, `randomized leapfrog parameters`, `No-U-Turn Sampler`
- **为什么对您有用**: 本文属于统计计算（statistical computing）方向，是您的 primary interest 之一。虽然不直接涉及因果推断或高维理论，但其离线校准与重要性采样框架可能启发您在高维后验采样中的计算策略。您可用 very_familiar 的软件开发和数值方法技能快速复现其算法，评估在您关心的模型中的表现，属于立即可做的探索。

### 6. [10.1007/s11222-026-10976-9](https://doi.org/10.1007/s11222-026-10976-9) · [arXiv](https://arxiv.org/abs/2508.05462) — Piecewise deterministic sampling for constrained distributions
- **作者**: Joël Tatang Demano, Paul Dobson, Konstantinos Zygalakis
- **期刊/来源**: Statistics and Computing
- **机构**: Heriot-Watt University · Maxwell Institute for Mathematical Sciences · University of Edinburgh
- **分类**: vol 36 · issue 5
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一类新的分段确定性马尔可夫过程（PDMP），用于从凸集 M 上的目标分布 π 中采样。该方法将凸优化中的 mirror map 概念引入采样，构造满足约束的 PDMP，从而产生无偏样本并支持精确子采样。算法在多个约束采样问题上优于基于随机微分方程（SDE）的现有方法，如 bouncy particle sampler 和 zig-zag sampler。理论部分给出了算法的收敛性和无偏性保证，并通过数值实验验证了其优势。对您而言，该工作属于统计计算方向，其 mirror map 与约束处理的思路可能对您在高维或结构化问题中的计算工具有启发。
- **关键技术**: `Piecewise Deterministic Markov Processes`, `mirror map`, `constrained sampling`, `exact subsampling`, `unbiased estimation`
- **为什么对您有用**: 本文属于统计计算（statistical computing）方向，与您的 primary interest 中的统计计算直接相关。您可以用 very_familiar 的软件开发和数值方法知识快速理解并复现其算法，评估其在实际问题中的表现。中期可做：若想深入分析其收敛速率，需在 moderately_familiar 的 M-estimation 理论上稍作延伸。总体而言，这是一篇值得一读的方法论论文，但 novelty 属于新方法而非新理论。

### 7. [10.1007/s11222-026-10980-z](https://doi.org/10.1007/s11222-026-10980-z) · [arXiv](https://arxiv.org/abs/2407.05790) — Kinetic interacting particle Langevin Monte Carlo
- **作者**: Paul Valsecchi Oliva, O. Deniz Akyildiz
- **期刊/来源**: Statistics and Computing
- **机构**: Imperial College London
- **分类**: vol 36 · issue 5
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出并分析了一类用于潜变量模型统计推断的相互作用欠阻尼 Langevin 算法（KIPLMC）。作者构造了一个在参数与潜变量联合空间上演化的扩散过程，并证明其平稳分布集中于参数的边际极大似然估计附近。随后给出该扩散的两种显式离散化作为实用算法，并在联合对数似然关于潜变量和参数强凹的假设下，建立了 Wasserstein-2 距离下的非渐近收敛速率。所得加速收敛速率在维度依赖上明显优于现有结果。数值实验展示了所提扩散在无监督学习、统计推断和反问题等应用中的有效性。对您而言，该文属于统计计算方向，其非渐近收敛分析框架与您熟悉的 M-估计理论有交集，但核心工具（Langevin 扩散、Wasserstein 收敛）不在您当前武器库中，可作为了解该方向的入门阅读。
- **关键技术**: `underdamped Langevin dynamics`, `interacting particle systems`, `Wasserstein-2 convergence`, `nonasymptotic rates`, `latent variable models`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关；其非渐近收敛分析可视为 M-估计理论在采样算法中的延伸，但核心机器（Langevin 扩散、Wasserstein 度量）不在您的武器库中，属于暂不可做的方向；作为 gateway reading，本文对统计学家友好，值得一读以了解该领域。

### 8. [10.1007/s11222-026-10961-2](https://doi.org/10.1007/s11222-026-10961-2) — Fuzzy clustering with three-way semi-perimeter distance
- **作者**: Pierpaolo D’Urso, Lorenzo Federico
- **期刊/来源**: Statistics and Computing
- **机构**: Sapienza University of Rome · Libera Università Internazionale degli Studi Sociali Guido Carli
- **分类**: vol 36 · issue 5
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于三向距离的模糊聚类方法，具体定义了基于半周长三向距离的模糊 c-medoid 算法。该三向距离可由任意经典（两向）距离导出，算法最小化一个目标函数，该函数是簇内成员对与簇中心之间的三向距离的线性组合，并加入熵正则项。作者在模拟数据和意大利人口普查数据上验证了方法的有效性，表明其优于标准模糊 c-medoids 算法。该工作属于统计计算与算法设计范畴，方法新颖性中等，主要贡献在于将三向距离引入模糊聚类框架并给出可操作的算法。
- **关键技术**: `fuzzy c-medoids`, `three-way distance`, `semi-perimeter distance`, `entropic regularization`, `clustering objective minimization`
- **为什么对您有用**: 本文属于统计计算方向，与您的 statistical computing 兴趣直接相关，可作为算法设计的新思路。您可以用 very_familiar 的软件开发和数值方法技能快速复现其算法，并评估其计算复杂度；中期可做的是将其与您 moderately_familiar 的 M-estimation 理论结合，分析该目标函数的统计性质。

## 其他  *(other, 4 篇)*

### 1. [10.1007/s11222-026-10974-x](https://doi.org/10.1007/s11222-026-10974-x) · [arXiv](https://arxiv.org/abs/2508.12627) — On computing and the complexity of computing higher-order U-statistics, exactly
- **作者**: Xingyu Chen, Lin Liu, Ruiqi Zhang
- **期刊/来源**: Statistics and Computing
- **机构**: Shanghai Jiao Tong University
- **分类**: vol 36 · issue 5
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 本文系统研究了高阶 U-统计量的精确计算复杂度问题，填补了该领域缺乏全面复杂度分析的空白。作者首先推导出将 m 阶 U-统计量分解为阶数不超过 m 的 V-统计量线性组合的分解式，后者通常更易计算。其次，建立了精确计算 V-统计量与 Einstein 求和（张量缩并）之间的联系，利用计算数学和量子计算中的加速工具。第三，基于与 U-统计量核相关的特定图的 treewidth，给出了精确计算 U-统计量时间复杂度的乐观估计。这些结果催生了一个新的、对具有乘法可分解结构的核更高效的精确算法，并提供了更简洁的复杂度刻画。作者开发了开源 R/Python 包 u-stats（CRAN 可获取），并通过三个统计学实例展示了其相对于现有基准的显著运行时优势。本文对您直接相关：它正是您 higher-order U-statistics 与 tensor-network/einsum 复杂度研究的核心延伸，且提供了可立即使用的软件工具。
- **关键技术**: `U-statistic decomposition into V-statistics`, `Einstein summation / tensor contraction`, `treewidth-based complexity analysis`, `multiplicative-decomposable kernels`, `open-source R/Python package`
- **为什么对您有用**: 这篇论文正是您 higher-order U-statistics 与 tensor-network/einsum 复杂度研究的核心延伸，且提供了可立即使用的软件工具。您可以用 very_familiar 的 treewidth/einsum 视角直接审视其复杂度刻画是否最优，或扩展其分解算法到更一般的核结构——立即可做。

### 2. [10.1007/s11222-026-10970-1](https://doi.org/10.1007/s11222-026-10970-1) · [arXiv](https://arxiv.org/abs/2406.04256) — Gradient boosting for hierarchical data in small area estimation
- **作者**: Paul Messer, Timo Schmid
- **期刊/来源**: Statistics and Computing
- **机构**: University of Bamberg
- **分类**: vol 36 · issue 5
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对小域估计（SAE）中线性混合模型（LMM）对正态性和线性假设的依赖问题，提出混合效应梯度提升（MEGB）方法。MEGB将梯度提升机的灵活性与混合模型的层次结构处理能力结合，通过引入随机效应捕捉域间未观测异质性，同时以非参数框架建模非线性和交互作用。该方法支持从单元级数据推导区域均值，并采用非参数bootstrap估计均方误差（MSE）。通过基于模型的模拟研究，将MEGB与既有估计器比较，并在真实数据上验证，结果表明MEGB在多种场景下能提供有竞争力的区域均值估计，甚至优于现有SAE方法。
- **关键技术**: `gradient boosting machines`, `mixed effects models`, `nonparametric bootstrap`, `small area estimation`, `mean squared error estimation`
- **为什么对您有用**: 本文属于统计计算与机器学习方法在应用统计中的结合，与您的主要兴趣（统计计算）有部分重叠，但并非核心方向。作为入门读物，它展示了如何将非参数机器学习工具融入层次数据建模，对您了解梯度提升与混合模型的结合有一定参考价值。您的武器库（如软件开发和M估计理论）足以支撑理解其方法，但该文方法学新颖性一般，属于应用型改进，可能不值得深入阅读全文。

### 3. [10.1007/s11222-026-10954-1](https://doi.org/10.1007/s11222-026-10954-1) · [arXiv](https://arxiv.org/abs/2504.01313) — Analyzing functional data with a mixture of covariance structures using a curve-based sampling scheme
- **作者**: Yian Yu, Bo Wang, Jian Qing Shi
- **期刊/来源**: Statistics and Computing
- **机构**: Southern University of Science and Technology · University of Leicester · Beijing Normal-Hong Kong Baptist University
- **分类**: vol 36 · issue 5
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对自由生活步态数据中不同行走模式对应的协方差结构异质性，提出一种基于曲线的采样方案，用于混合协方差结构的函数型数据分析。传统方法难以刻画数据子集间协方差模式的差异，作者构建了一个统一贝叶斯框架，将非线性回归函数与连续时间隐马尔可夫模型结合，以识别并利用变化的协方差结构。核心贡献是开发了计算高效的曲线式采样方案用于隐状态估计，解决了高维条件相依数据的采样复杂性。文中详述了贝叶斯推断过程，并考察了模型结构一致性的渐近性质，通过模拟和真实数据验证了方法的有效性。
- **关键技术**: `curve-based sampling scheme`, `continuous-time hidden Markov model`, `Bayesian inference`, `functional data analysis`, `mixture covariance structures`
- **为什么对您有用**: 本文属于统计计算与函数型数据分析的交叉，与您的统计计算兴趣相关，但并非核心方向。作为入门读物，其曲线式采样方案对高维条件相依数据的处理思路可能对您有启发，但武器库中的工具（如 U-统计量、张量网络）在此问题上的直接应用有限，暂不建议深入阅读。

### 4. [10.1007/s11222-026-10956-z](https://doi.org/10.1007/s11222-026-10956-z) · [arXiv](https://arxiv.org/abs/2504.11836) — Non-centering for discrete-valued state transition models: an application to ESBL-producing E. coli transmission in Malawi
- **作者**: James Neill, Rebecca Lester, Winnie Bakali, Gareth Roberts, Nicholas Feasey, Lloyd A. C. Chapman et al.
- **期刊/来源**: Statistics and Computing
- **机构**: Lancaster University · University College London · Malawi-Liverpool-Wellcome Trust Clinical Research Programme · Kamuzu University of Health Sciences · University of Warwick · University of St Andrews
- **分类**: vol 36 · issue 5
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对离散值状态转移的传染病传播模型，提出了一种新的数据增广MCMC方法——Rippler算法。该算法在Metropolis-Hastings的提议步骤中使用传播模型本身，而非在接受-拒绝步骤中，从而提高了部分观测数据下贝叶斯推断的效率。作者在模拟数据上验证了算法，并将其应用于马拉维布兰太尔产ESBL大肠杆菌传播数据。与两种常用的部分观测流行病数据贝叶斯推断方法相比，Rippler算法在混合速度与计算复杂度之间取得了良好平衡。该方法属于统计计算领域，对您而言，其计算策略（如提议分布设计）可能对您熟悉的统计计算或算法设计有启发，但主题与您的主要研究方向关联较弱。
- **关键技术**: `data augmentation MCMC`, `Metropolis-Hastings`, `individual-based epidemic models`, `discrete-time state transition`
- **为什么对您有用**: 本文属于统计计算方向，与您的统计计算兴趣有交集，但并非您主要研究领域。作为入门读物，它展示了针对复杂似然的MCMC设计思路，但武器库中的工具（如高阶U统计、张量网络）难以直接迁移。建议仅作泛读，不值得深入展开。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

