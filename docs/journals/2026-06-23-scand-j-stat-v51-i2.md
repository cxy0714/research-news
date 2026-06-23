# Scand. J. Stat. — Vol 51  Issue 2  ·  2026-06-23

- 共 16 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 16 篇全部抓到（对照 OpenAlex 17 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期《Scandinavian Journal of Statistics》第51卷第2期共收录16篇论文，主题覆盖假设检验、非参数/半参数方法、高维随机矩阵、效率估计及若干分散方向。假设检验主线包括三篇：高维条件均值检验（极端型统计量处理混合依赖）、偏差高阶近似用于聚焦模型选择、协变量自适应随机化下层内不平衡的Bootstrap协方差估计。非参数与半参数主线最为密集：七篇涉及高维半参数特征聚合（基于距离的U统计量与有效影响函数）、函数型数据的核均值嵌入与MMD检验、球面密度估计与测量误差下的反卷积、纵向数据二次推断函数（QIF）的工作相关矩阵影响、函数型协方差算子的Wasserstein软聚类、多元极值分布的马尔可夫树近似、以及Pitman-Yor过程的截断Poisson-Dirichlet近似。此外，高维随机矩阵方向有一篇Wishart/逆Wishart矩阵等变函数期望的递推计算；效率方向有约束多元回归的包络（Envelope）估计量改进；其余四篇分别涉及偏斜布朗运动MLE的非标准收敛速率、极端风险度量调整标准差位点、马尔可夫链混合时间的实例依赖估计、以及极值分布辅助函数表征。

假设检验主线中，**Nonparametric conditional mean testing via an extreme-type statistic**将极值理论与非参数平滑结合，在高维混合依赖数据下实现了渐近尺寸控制的检验，并衍生出特征筛选方法；**Accurate bias estimation with applications to focused model selection**通过泰勒展开给出估计量偏差与平方偏差的高阶近似，使聚焦信息准则（FIC）能正确反映O(n⁻¹)量级方差；**Consistent covariances estimation for stratum imbalances under minimization method**则利用Le Cam第三引理证明Bootstrap估计量一致性，并将其用于调整治疗效应检验的size膨胀问题——后者直接关联因果推断中随机化设计的后验推断。非参数/半参主线中的**A new paradigm for high-dimensional data: Distance-based semiparametric feature aggregation framework via between-subject attributes**构建了U统计量基估计方程（UGEE）与有效影响函数，在数十万维特征下实现根n一致且分布稳健的半参数估计，其半参数效率思想贯穿全文；**Kernel mean embedding of probability measures and its applications to functional data analysis**将概率测度嵌入RKHS并构造pseudo-likelihood，基于MMD给出了Function-on-Scalar回归、one-way ANOVA等检验；**The effect of the working correlation on fitting models to longitudinal data**通过影响函数展开揭示QIF估计量的无界性与效率得失，为纵向数据边际模型的工作相关选择提供理论指引。

与因果推断、半参数效率、高维方向最贴合的论文包括：**Consistent covariances estimation for stratum imbalances under minimization method**（协变量自适应随机化下的推断工具，直接服务于因果效应检验）；**A new paradigm for high-dimensional data: Distance-based semiparametric feature aggregation framework via between-subject attributes**（半参数效率与U统计理论的结合，可迁移至因果效应估计）；**Envelopes for multivariate linear regression with linearly constrained coefficients**（约束模型下的envelope效率提升，类比半参数效率界方法）；**Nonparametric conditional mean testing via an extreme-type statistic**（高维非参数假设检验的极限理论）；**On the expectations of equivariant matrix-valued functions of Wishart and inverse Wishart matrices**（高维随机矩阵矩计算的递推公式，适合作为高维协方差推断的工具）。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12707](https://doi.org/10.1111/sjos.12707) — On the expectations of equivariant matrix‐valued functions of Wishart and inverse Wishart matrices
- **作者**: Grant Hillier, Raymond M. Kan
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Southampton · University of Toronto
- **分类**: vol 51 · issue 2 · pp 697-723
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究Wishart矩阵和逆Wishart矩阵的矩阵值函数的期望计算问题，这类函数在正交群共轭作用下具有齐次性和等变性。作者利用对称函数理论（幂和对称函数）将这类期望空间基函数展开，并推导出递推关系和分析表达式。核心方法依赖于矩阵变量的齐次度参数和划分的索引结构，避免了直接数值积分或蒙特卡洛模拟。所得结果大幅降低了计算此类矩的计算复杂度，尤其适用于高维协方差矩阵的矩计算场景。对您而言，该工作直接对应高维随机矩阵理论中的矩计算问题，且其递推公式便于软件实现（如einsum库中的张量收缩优化），属于立即可做的工具改进方向。
- **关键技术**: `Wishart distribution`, `equivariant functions under orthogonal group`, `power-sum symmetric functions`, `recurrence relations for moments`, `matrix-valued function expectations`
- **为什么对您有用**: 本文直接连接到您的高维随机矩阵理论和统计计算兴趣，具体涉及Wishart矩阵期望的解析计算。技术武器库中'高维渐近理论'和'软件开发'两项即可支撑您实现并推广这些递推公式，属于立即可做的方向。

## 非参数 / 半参数  *(nonparam_semipara, 7 篇)*

### 1. [10.1111/sjos.12695](https://doi.org/10.1111/sjos.12695) — A new paradigm for high‐dimensional data: Distance‐based semiparametric feature aggregation framework via between‐subject attributes
- **作者**: Jinyuan Liu, Xinlian Zhang, Tuo Lin, Ruohui Chen, Yuan Zhong, Tian Chen et al.
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Vanderbilt University · UC San Diego Health System · University of Michigan · Takeda (United States) · Vanderbilt Health · University of California San Diego · VA San Diego Healthcare System · MicroBio Engineering (United States) 等
- **分类**: vol 51 · issue 2 · pp 672-696
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出一种面向高维数据的基于距离的半参数特征聚合框架，目标是在不依赖稀疏性假设或置换推断的情况下实现有效推断。方法利用成对个体间属性构造距离结果，从而在保留所有特征信息的同时实现降维。通过U统计量基估计方程（UGEE）处理成对结果之间的复杂相关性，并借助有效影响函数（EIF）得到半参数估计量。该估计量具有根n一致性和渐近最优性，对分布误设稳健。模拟实验和人与人微生物组、可穿戴设备数据应用显示，该方法在数十万维特征下仍保持计算可行性和可解释性。对研究者而言，本工作直接连接其高维统计与U统计量方法论，同时在半参数效率理论方面提供实际案例。
- **关键技术**: `distance-based feature aggregation`, `U-statistics-based estimating equations (UGEE)`, `efficient influence function (EIF)`, `semiparametric regression`, `between-subject attributes`, `high-dimensional pairwise outcomes`
- **为什么对您有用**: 本文直接连接您的高维统计兴趣（特征聚合不依赖稀疏性）和U统计量兴趣（UGEE方法），并展示了半参数效率理论在高维场景中的应用。您非常熟悉的U统计量计算（树宽/张量收缩）可以用来分析该框架的计算复杂度，而 moderately familiar 的半参数理论推动您深入理解EIF推导。总体而言，是**立即可做**的阅读：核心武器（U统计量理论、非参数方法）已到位，只需在EIF细节上稍加补充即可进入讨论。

### 2. [10.1111/sjos.12691](https://doi.org/10.1111/sjos.12691) · [arXiv](https://arxiv.org/abs/2011.02315) — Kernel mean embedding of probability measures and its applications to functional data analysis
- **作者**: Saeed Hayati, Kenji Fukumizu, Afshin Parvardeh
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 447-484
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在无穷维可分 Hilbert 空间上建立概率测度的核均值嵌入（kernel mean embedding），用于 functional response 统计模型的推断。核心构造是将分布嵌入到再生核 Hilbert 空间（RKHS），该嵌入函数在开邻域内刻画概率测度的集中程度，从而诱导一个 pseudo-likelihood 用于统计推断。基于 Maximum Mean Discrepancy（MMD），作者提出了针对 Function-on-Scalar 回归、functional one-way ANOVA、以及协方差算子相等性检验的假设检验方法。理论部分证明了嵌入的识别性，但未给出检验统计量的精确极限分布或功效的 minimax 最优性分析。实证模拟显示新方法在三类 functional data 问题上优于传统 competitors。对您而言，这是 RKHS 方法在 functional data 假设检验中的系统应用，与 nonparametric theory 和 hypothesis testing 方向直接相关。
- **关键技术**: `kernel mean embedding`, `Maximum Mean Discrepancy (MMD)`, `reproducing kernel Hilbert space (RKHS)`, `functional data analysis`, `pseudo-likelihood construction`, `permutation-based hypothesis testing`
- **为什么对您有用**: 本文连接到您 primary interests 中的 nonparametric theory 与 hypothesis testing：在无穷维 Hilbert 空间上用 RKHS 嵌入做分布比较与检验，是经典的 nonparametric 方法拓展。您武器库中的 nonparametric statistics 与 minimax bounds 理论可以用来审视本文方法的局限——作者未给出检验功效的 minimax rate 或 asymptotic power analysis，这正是您熟悉的 minimax lower bound 技术可以切入的地方。follow-up 判断：**立即可做**——用 very_familiar 的 minimax bounds 工具分析 MMD-based test 在 functional data 设定下的检验功效最优性，或研究 pseudo-likelihood 的效率性质。

### 3. [10.1111/sjos.12684](https://doi.org/10.1111/sjos.12684) — Density estimation and regression analysis on hyperspheres in the presence of measurement error
- **作者**: Jeong Min Jeon, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: KU Leuven
- **分类**: vol 51 · issue 2 · pp 513-556
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文研究单位超球面上的密度估计与回归问题，假设观测数据被测量误差污染，目标是非参数估计密度函数与回归函数及其渐近性质。作者提出基于 deconvolution 的核类估计量，利用球谐函数展开处理球面几何结构，在测量误差分布已知的条件下建立收敛速度与渐近正态性。理论贡献包括推导估计量的最优收敛速率（受测量误差平滑度影响）以及构造两类渐近置信区间：基于渐近正态的 Wald 型区间与基于经验似然的区间。模拟与实数据分析验证了有限样本表现。对您而言，这是非参数理论在非欧数据上的扩展，测量误差设定与 deconvolution 技术可迁移至您熟悉的 inverse problems with random noise。
- **关键技术**: `deconvolution kernel estimation`, `spherical harmonics`, `asymptotic normality`, `empirical likelihood`, `minimax convergence rates`, `measurement error models`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric & nonparametric theory，具体是球面非参数估计与测量误差（inverse problems with random noise）的交叉。您武器库中的 nonparametric statistics 和 inverse problems with random noise（very_familiar）可直接用于审视其收敛速率是否达到 minimax optimal、经验似然区间是否有效率损失。**立即可做**：用您熟悉的 minimax bound 工具验证其声称的收敛速率在测量误差平滑度假设下是否紧；或尝试将 HOIF 思路引入以改善置信区间的 higher-order 性质。

### 4. [10.1111/sjos.12704](https://doi.org/10.1111/sjos.12704) — The effect of the working correlation on fitting models to longitudinal data
- **作者**: Samuel Muller, Suojin Wang, A. H. Welsh
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Macquarie University · Texas A&M University · Australian National University
- **分类**: vol 51 · issue 2 · pp 891-912
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究纵向数据边际线性回归模型中二次推断函数（QIF）估计量的理论性质，核心关注 working correlation 矩阵的选择对估计量存在性、稳健性和渐近相对效率的影响。作者证明 QIF 估计量并非总是存在，并提出处理非存在情形的方法；进一步证明 QIF 估计量具有无界影响函数，其渐近效率相对于广义估计方程（GEE）估计量可高可低，取决于真实相关结构与 working correlation 的偏离程度。理论分析基于影响函数展开和渐近相对效率比较，辅以模拟验证。对您而言，这是纵向数据边际模型中 GEE 与 QIF 方法的理论比较研究，涉及影响函数有界性、效率权衡等 semiparametric 理论核心议题。
- **关键技术**: `quadratic inference function`, `generalized estimating equations`, `influence function`, `asymptotic relative efficiency`, `working correlation structure`, `robustness analysis`
- **为什么对您有用**: 本文直接涉及纵向数据因果推断中的边际模型估计方法，属于 primary interest 中 longitudinal / semiparametric theory 的交叉点。文中对影响函数有界性的分析、QIF 与 GEE 的渐近效率比较，与您熟悉的 semiparametric efficiency theory 和 influence function 方法高度相关。follow-up 判断：立即可做——用 very_familiar 的非参数统计和 minimax 理论工具，可以深入分析 QIF 在 misspecified working correlation 下的效率损失界，或探索有界影响函数的改进估计量。

### 5. [10.1111/sjos.12692](https://doi.org/10.1111/sjos.12692) · [arXiv](https://arxiv.org/abs/2212.13287) — Covariance‐based soft clustering of functional data based on the Wasserstein–Procrustes metric
- **作者**: Valentina Masarotto, Guido Masarotto
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 485-512
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究函数型数据（functional data）基于协方差结构的软聚类问题，目标是在协方差算子空间中对曲线进行分组，允许个体以概率属于多个簇。核心方法是将协方差算子视为概率测度，使用 Wasserstein–Procrustes 距离度量协方差之间的差异，并通过熵正则化（entropy regularization）实现软聚类，类似于 fuzzy c-means 在无穷维协方差算子空间的推广。作者还提出了估计簇数的方法以及检验是否存在聚类结构的假设检验程序，理论部分涉及协方差算子的几何与 Wasserstein 空间的度量性质。实证分析包括模拟研究和真实数据示例，展示了方法在协方差分离不清晰时的优势。对您而言，本文提供了协方差算子非参数推断的一个具体应用场景，可作为 semiparametric theory 在函数型数据领域的延伸阅读。
- **关键技术**: `Wasserstein-Procrustes metric`, `covariance operator clustering`, `entropy regularization`, `soft clustering`, `functional data analysis`, `hypothesis testing for cluster structure`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric and nonparametric theory——具体是协方差算子的非参数推断。从 technical_arsenal 角度，您 very_familiar 的 nonparametric statistics 和 minimax bounds 可以用来审视本文的聚类一致性率和检验的功效性质；moderately_familiar 的 M-estimation theory 可用于分析熵正则化估计量的渐近行为。follow-up 判断：**中期可做**——若想深入，需在 moderately_familiar 的 M-estimation theory 上加强，特别是无穷维参数空间上的 M-估计收敛速率和正则化理论。

### 6. [10.1111/sjos.12698](https://doi.org/10.1111/sjos.12698) · [arXiv](https://arxiv.org/abs/2208.02627) — Modeling multivariate extreme value distributions via Markov trees
- **作者**: Shuang Hu, Zuoxiang Peng, Johan Segers
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 760-800
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在高维多元极值分布建模问题中，目标是构建既灵活又稀疏的 max-stable 分布，传统方法在高维时面临参数爆炸和计算困难。作者提出 Markov tree 方法：将二元 max-stable 分布沿树结构组合成 Markov 随机场，虽然其本身一般不是 max-stable，但被一个多元 max-stable 分布吸引，从而提供树结构近似。估计方面，用 Prim 算法学习树结构，边权重为估计的 pairwise upper tail dependence coefficients，连接变量对的边缘分布可用多种方法拟合。理论贡献在于建立了 Markov tree 与 max-stable 分布的吸引关系，实证分析展示了在 Danube 河流流量数据上对稀有事件概率的推断。对您的 semiparametric theory 兴趣而言，这是一个将图结构约束与半参数估计结合的有趣案例。
- **关键技术**: `max-stable distribution`, `Markov random field on trees`, `upper tail dependence coefficient`, `Prim's algorithm for tree learning`, `multivariate extreme value theory`
- **为什么对您有用**: 连接到 semiparametric theory 的图结构约束估计问题，展示了如何用树结构实现高维稀疏建模。从 technical_arsenal 角度，您熟悉的 nonparametric statistics 和 minimax bounds 可用于分析该估计量的收敛性质——目前文献中树结构学习的理论保证可能不够紧。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上补充 extreme value distribution 的特定结构知识，才能深入分析估计效率。

### 7. [10.1111/sjos.12688](https://doi.org/10.1111/sjos.12688) — Truncated two‐parameter Poisson–Dirichlet approximation for Pitman–Yor process hierarchical models
- **作者**: Junyi Zhang, Angelos Dassios
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Hong Kong Polytechnic University · London School of Economics and Political Science
- **分类**: vol 51 · issue 2 · pp 590-611
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究 Pitman-Yor 过程的近似问题，目标是在保持分布性质的同时降低计算复杂度。作者基于 two-parameter Poisson-Dirichlet 表示构造截断近似，核心思想是保留按降序排列的前 L 个随机权重，相比 truncated stick-breaking 近似具有更低的 L1 误差界。开发了精确采样算法和针对困难参数区域的替代 MCMC 算法，并给出了近似误差的理论分析。将近似过程嵌入 Pitman-Yor 过程混合模型，设计了 blocked Gibbs sampler 进行后验推断。该工作属于 Bayesian nonparametrics 的计算方法贡献，对您 primary interest 中的 semiparametric theory 和 statistical computing 有一定参考价值。
- **关键技术**: `Pitman-Yor process`, `Poisson-Dirichlet distribution`, `truncated stick-breaking`, `blocked Gibbs sampler`, `Bayesian nonparametric mixture`
- **为什么对您有用**: 本文涉及 Bayesian nonparametrics 的计算方法，与您 primary interest 中的 semiparametric theory 和 statistical computing 有交叉。然而，该论文的核心工具（Dirichlet process、stick-breaking construction、MCMC）不在您的 technical_arsenal 中，且与您熟悉的 minimax bounds、U-statistics、influence function 等理论工具距离较远。**暂不可做**：若要进入 Bayesian nonparametrics 领域，需要先补充 Dirichlet process 理论和 MCMC 方法论的基础知识。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12690](https://doi.org/10.1111/sjos.12690) · [arXiv](https://arxiv.org/abs/2101.00514) — Envelopes for multivariate linear regression with linearly constrained coefficients
- **作者**: R. Dennis Cook, Liliana Forzani, Lan Liu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 429-446
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文考虑有线性约束系数的多元线性回归模型，如生长曲线和纵向数据中常见的情形，目标是通过envelope方法提升参数估计效率。首先对比了标准envelope估计量与约束模型下经典估计量在偏差和效率上的差异。接着提出了一种新的基于约束模型的envelope估计器，通过利用系数矩阵列空间的已知子空间约束来进一步降低估计变异。理论分析表明，新估计量在均方误差意义上优于标准方法。模拟研究验证了效率提升。最后通过益生菌减少沙门氏菌感染的实例展示了方法的应用。该论文将envelope思想推广到约束线性模型，为多元回归的效率改进提供了新的工具，与您的效率理论（半参数效率界）兴趣直接相关。
- **关键技术**: `Envelope method`, `Multivariate linear regression`, `Linearly constrained coefficients`, `Subspace estimation`, `Efficiency improvement`
- **为什么对您有用**: 该论文直接涉及您的效率理论兴趣，尤其是通过子空间降维提高多元回归估计效率的envelope方法。您对非参数统计和估计理论非常熟悉，可以迅速理解其核心思想，并可能将envelope方法与您的半参数效率界限工作结合，拓展到纵向数据或因果推断场景。目前立即可做：您的武器库中的非参统计和高维渐近知识足以支撑您深入这一方向。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12697](https://doi.org/10.1111/sjos.12697) — Nonparametric conditional mean testing via an extreme‐type statistic in high dimension
- **作者**: Yiming Liu, Guangming Pan, Guangren Yang, Wang Zhou
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Jinan University · Nanyang Technological University · National University of Singapore
- **分类**: vol 51 · issue 2 · pp 801-831
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对高维场景下响应变量与协变量之间的条件均值依赖性检验问题，提出了一种基于非参数方法的极端型（extreme-type）统计量。在温和的混合条件下，推导了该统计量的渐近零分布，并给出了检验的渐近尺寸控制。为增强对一般依赖结构的检验功效，进一步构造了一个更一般的极端型统计量，并建立了其渐近性质与局部功效分析。此外，基于所提检验提出了一种新的特征筛选方法，通过模拟和真实数据验证了其有限样本性能。本文的技术核心在于将极值理论与非参数回归平滑结合起来处理高维协变量的条件均值检验，同时允许数据具有时间或空间混合依赖性。对您而言，这是一个直接对应“假设检验”兴趣子方向的工作，尤其在高维非参数检验的理论分析上，可以运用您熟悉的高维渐近与非参数统计工具（如极值分布、混合条件）来理解其方法，并进一步探索在因果推断中条件独立性检验的应用场景——属于立即可做的阅读。
- **关键技术**: `extreme-type statistic`, `nonparametric conditional mean testing`, `mixing condition`, `asymptotic null distribution`, `power analysis`, `feature screening via hypothesis test`
- **为什么对您有用**: 本文直接属于您 primary interest 中的“hypothesis testing”子方向，具体是高维条件下非参数条件均值检验。您 very_familiar 中的“nonparametric statistics”和“high-dimensional asymptotics”可以直接攻入——例如用极值分布理论评估其渐近零分布的紧性，或用 minimax 框架审视其功效是否达到最优。立即可做：仅需已有武器即可深度理解并可能提出改进（如引入稳健的方差估计或调整统计量的阈值选择）。

### 2. [10.1111/sjos.12696](https://doi.org/10.1111/sjos.12696) — Accurate bias estimation with applications to focused model selection
- **作者**: Ingrid Dæhlen, Nils Lid Hjort, Ingrid Hobæk Haff
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: OsloMet – Oslo Metropolitan University · University of Oslo
- **分类**: vol 51 · issue 2 · pp 724-759
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究估计量的偏差与平方偏差的高阶近似，误差阶分别达到 O(n^{-3/2}) 和 O(n^{-2})，并应用于均方误差（MSE）估计与聚焦模型选择。设定覆盖分位数、无偏估计量的变换、可能错误指定模型下的极大似然估计及其函数等一大类估计量。核心方法基于泰勒展开和渐近展开技术，得到偏差与平方偏差的显式近似公式，进而构造 MSE 估计量，其精度足以正确反映 O(n^{-1}) 量级的方差信息。利用这些近似，作者提出新的聚焦信息准则（FIC），用于目标参数导向的模型选择。实证部分以国际战争死亡数据为例，展示了不同偏差估计精度对模型选择结果的显著影响。对您而言，该工作直接对应数学统计与假设检验方向，提供了估计量偏差校正的高阶框架，可迁移至因果推断中各类估计量的 MSE 评估与模型选择问题。
- **关键技术**: `bias approximation to order n^{-3/2}`, `MSE estimation correct to order n^{-2}`, `focused information criterion (FIC)`, `maximum likelihood under misspecification`, `Taylor series expansion`
- **为什么对您有用**: 该文直接关联您的数学统计与假设检验兴趣，提供的偏差高阶近似框架可应用于任何参数/半参数估计量的 MSE 评估，您熟悉的渐近理论和非参数统计能立即用于理解其精度增益。FIC 方法在模型选择中的使用可与因果推断中的 DML 或 IV 模型选择形成连接，属于中期可做的拓展方向（需在 semiparametric theory 上稍加熟悉）。

### 3. [10.1111/sjos.12703](https://doi.org/10.1111/sjos.12703) · [arXiv](https://arxiv.org/abs/2209.13117) — Consistent covariances estimation for stratum imbalances under minimization method for covariate‐adaptive randomization
- **作者**: Zixuan Zhao, Yanglei Song, Wenyu Jiang, Dongsheng Tu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 861-890
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究在Pocock-Simon最小化法（一种协变量自适应随机化）下，层内不平衡的极限协方差矩阵的估计问题。该方法自1975年提出以来，极限协方差的存在性直到近年才被证明，而其显式形式难以计算。作者提出基于bootstrap的估计量，并利用Le Cam第三引理证明该估计量的一致性。作为应用，将该估计量用于调整生存数据中治疗效应的稳健检验统计量。模拟研究表明，调整后的检验其size接近名义水平，而未调整的检验在最小化法下存在渐进size膨胀的问题。本文为协变量自适应随机化下的统计推断提供了实用工具，与您的假设检验和因果推断中的随机化设计分析紧密相关。
- **关键技术**: `bootstrap estimator`, `Le Cam's third lemma`, `covariate-adaptive randomization`, `minimization method`, `robust tests for survival data`
- **为什么对您有用**: 本文直接关联您‘hypothesis testing’兴趣中的自适应随机化检验调整问题。您对‘非参数统计’和‘bootstrap’非常熟悉，可立即复现其理论并扩展到其他随机化方案（如分层置换检验）。此外，其一致性证明依赖Le Cam第三引理，技术细节对您的高维渐近功底是可攻克的。立即可做：利用已有bootstrap和假设检验知识验证并推广该估计量到更一般的协变量结构。

## 其他  *(other, 4 篇)*

### 1. [10.1111/sjos.12694](https://doi.org/10.1111/sjos.12694) · [arXiv](https://arxiv.org/abs/2302.02954) — Maximum likelihood estimator for skew Brownian motion: The convergence rate
- **作者**: Antoine Lejay, Sara Mazzonetto
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 612-642
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究偏斜布朗运动（SBM）中偏斜参数θ的最大似然估计（MLE）的渐近性质。利用局部时过程的中心极限定理最新结果，证明MLE的收敛速率为n^{-1/4}，且极限分布为混合正态分布，从而证实了一个长期未解决的猜想。进一步给出了MLE的级数展开，并系统分析了得分函数及其导数随参数变化的渐近行为。特别地，当θ=0（即真实过程为标准布朗运动）时，极限分布与混合正态分布不同，呈现出奇异行为；当θ接近±1时，展开系数发生爆炸。论文为非正则扩散过程估计理论提供了完整刻画，对理解非标准收敛速率的统计推断有方法论价值。对您而言，虽不直接覆盖因果推断或高维统计，但其渐近分布分析技术可迁移至其他非标准速率问题（如部分高维U统计量的极限分布）。
- **关键技术**: `Maximum likelihood estimation`, `Skew Brownian motion`, `Local time`, `Mixed normal distribution`, `n^{-1/4} convergence rate`, `Series expansion of MLE`
- **为什么对您有用**: 该论文属于扩散过程估计理论，与您对假设检验（渐近分布理论）的兴趣有间接关联——MLE的极限分布可用于构造检验统计量。然而，其核心工具（局部时CLT、偏斜扩散）不在您当前的`technical_arsenal`（very_familiar无随机过程，moderately_familiar也为空缺）内，属于**暂不可做**的跟进方向。若未来需要对非标准速率（如n^{-1/4}）的估计量构建检验或置信区间，可参考本文的分析框架，但需要先补齐随机过程局部时的理论基础。

### 2. [10.1111/sjos.12693](https://doi.org/10.1111/sjos.12693) · [arXiv](https://arxiv.org/abs/2411.07203) — Estimation of the adjusted standard‐deviatile for extreme risks
- **作者**: Haoyu Chen, Tiantian Mao, Fan Yang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 643-671
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的极端风险度量——调整标准差位点（adjusted standard-deviantile），它是对 expectile 的修改以更灵敏地捕捉尾部风险。首先推导了该度量的一阶渐近展开式；然后基于该展开，针对中间水平和极高水平分别设计了两种估计方法。利用极值理论技巧，在 i.i.d. 和 α-mixing 时间序列两种设定下证明了估计量的渐近正态性。模拟和真实数据（如金融收益率）验证了估计量的有限样本表现。该工作聚焦于风险度量的统计推断，是极值理论在现代风险管理中的一个完整应用案例。
- **关键技术**: `extreme value theory`, `expectile`, `risk measure estimation`, `asymptotic expansion`, `α-mixing time series`
- **为什么对您有用**: 本文并非研究者核心兴趣方向的论文，但可作为极值理论在金融风险度量中的应用范例。研究者具备非参数统计和高维渐近的基础，但缺少极值指数估计和二阶极值理论的专门训练，因此当前不适合直接在该方向上展开工作。然而，本文的渐近展开技巧和估计量构造思路对研究者熟悉的非参数估计（如 M-估计）有一定拓展价值，可作为扩展统计应用视野的泛读材料。

### 3. [10.1111/sjos.12686](https://doi.org/10.1111/sjos.12686) · [arXiv](https://arxiv.org/abs/1912.06845) — Empirical and instance‐dependent estimation of Markov chain and mixing time
- **作者**: Geoffrey Wolfer
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 557-589
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究从单条轨迹观测数据中估计马尔可夫链混合时间的问题。与以往利用谱间隙的方法不同，本文采用基于全变差收缩的Dobrushin型收缩系数，该系数可控制混合时间且适用于不可逆链。作者改进了该收缩系数的完全数据依赖置信区间，使其比谱方法更易计算且更窄。此外，引入实例依赖的分析框架，利用转移矩阵的额外信息推导出诱导一致范数下估计的实例依赖速率，从而超越最坏情况分析。理论结果包括非渐近置信区间和收敛速率的刻画。本文对统计推断中依赖于混合时间的链估计问题提供了新的视角。
- **关键技术**: `contraction coefficient`, `Dobrushin's coefficient`, `total variation`, `mixing time estimation`, `instance-dependent rates`, `data-dependent confidence interval`
- **为什么对您有用**: 本文属于统计推断与随机过程交叉领域，直接连接到研究者的“mathematical statistics & hypothesis testing”兴趣，特别是非渐近置信区间构造。技术层面，本文的实例依赖收敛速率分析可用研究者熟悉的“minimax bounds”工具评判其最优性，也可用“高维渐近”中的浓度不等式方法扩展。对于研究者，此方向可作为“统计计算权衡”中算法复杂度的补充理解：混合时间控制MCMC采样效率，与统计计算中的信息-计算间隙问题有潜在关联。目前核心武器库中缺少马尔可夫链混合时间的精确理论，属暂不可做方向，但可作为methodological阅读拓宽视野。

### 4. [10.1111/sjos.12701](https://doi.org/10.1111/sjos.12701) · [arXiv](https://arxiv.org/abs/2311.15355) — Characterization of valid auxiliary functions for representations of extreme value distributions and their max‐domains of attraction
- **作者**: Miriam Isabel Seifert
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 51 · issue 2 · pp 832-860
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究极值分布及其最大吸引域（MDA）的两种重要表示：von Mises表示（vMR）和变差表示（VR）。两种表示依赖于所谓的辅助函数，但此前对有效辅助函数集合的表征并不完整，未能区分适用于vMR和VR的辅助函数。作者引入“通用”辅助函数概念，其同时适用于整个MDA分布族下的vMR和VR。进一步精确刻画了vMR和VR各自有效辅助函数的集合，给出了完全分离的条件。此外提出寻找结构简单（解析简洁）的辅助函数的方法，并为若干重要极值分布给出了具体辅助函数。该工作属于极值统计的基础理论推进，有助于深化对极值分布表示的理解，但与你当前的主要研究方向（因果推断、高维统计、U统计等）无直接重叠。可作为极值理论入门参考，但短期内难以整合到既有工作流程中。
- **关键技术**: `von Mises representation`, `variation representation`, `auxiliary function`, `max-domains of attraction`, `extreme value distributions`
- **为什么对您有用**: 本文属于极值统计的理论工作，与你的primary interests（因果推断、高维统计、U-统计、半参等）缺乏直接的方法论关联。武器库中非常熟悉的nonparametric statistics或minimax bounds难以直接应用于极值分布的辅助函数表征问题；该领域更依赖极值指数估计、点过程等工具，不在你的technical arsenal内。因此目前暂不可做深入跟进，但可作为扩展统计学视野的参考资料。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

