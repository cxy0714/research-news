# Stat. Comput. — Vol 36  Issue 2  ·  2026-07-14

- 共 22 篇 · Statistics and Computing
- 目录核对 ⚠️ 疑似漏 13 篇（对照 OpenAlex 38 篇）：10.1007/s11222-026-10845-5、10.1007/s11222-025-10809-1、10.1007/s11222-025-10817-1、10.1007/s11222-026-10821-z、10.1007/s11222-026-10827-7 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Stat. Comput.》第36卷第2期的22篇论文，整体上围绕**统计计算与算法加速**、**非参数/半参数方法与密度估计**、**贝叶斯推断与模型选择**、以及**高维变量选择与检验**四条主线展开。其中，统计计算与算法加速是数量最多的主题，涵盖子抽样、优化加速、MCMC改进、变分推断等；非参数/半参数方向则聚焦于密度估计的方差-偏差权衡和带宽选择；贝叶斯方向涉及后验诊断、模型选择稳健性、以及近似采样；高维方向则包括变量筛选规则和全局检验。

在**统计计算与算法加速**这条主线上，多篇论文致力于降低经典方法的计算成本或提升可扩展性。例如，“D-Optimal Subsampling Design”利用最优设计理论推导出子抽样规则，适用于海量线性回归；“Safe Feature Identification Rule for Fused Lasso”通过引入额外对偶变量，首次为fused Lasso提供了安全筛选规则以加速求解；“Fast estimation of the composite link model”将估计重新表述为广义线性数组模型（GLAM），利用数组运算大幅降低高维分组计数数据的计算时间；“A unified and efficient proximal gradient descent algorithm”通过卷积平滑hinge损失，使惩罚SVM可用近端梯度下降高效求解。此外，“Combining Adaptive MCMC and Nested Sampling”和“Sampling from density power divergence-based generalized posterior”分别从MCMC与优化结合、以及随机梯度近似角度，处理贝叶斯推断中的计算瓶颈。

**非参数/半参数方法与密度估计**主线中，“Reducing variance and improving bandwidth selection in density estimation”是核心贡献，它通过半参数变换和局部线性平滑，在保持偏差缩减的同时更有效地降低方差，并开发了MISE最优的plug-in带宽选择器，其收敛速度优于标准非参数方法。“Non-parametric estimation techniques of factor copula model”则用核密度估计灵活捕捉因子copula中的依赖结构，并证明了相合性。“Score-driven time-varying parameter models with spline-based densities”用样条构造灵活密度，使时变参数更新对异常值更稳健，属于应用导向的改进。

**贝叶斯推断与模型选择**方向中，“Posterior SBC”提出条件于观测数据的后验自洽性检验，能发现特定数据下的推断失败；“Variational Markov chain mixtures”用变分EM自动确定混合马尔可夫链的组件数，并给出了分类误差的理论下界；“Bayesian stability selection”将先验信息融入稳定性选择，提供贝叶斯可信区间以量化变量选择的不确定性；“Bayesian analysis of Cox-type regression model”用RJMCMC自适应估计部分线性Cox模型中的非线性效应，避免了交叉验证。

**高维变量选择与检验**方面，“Global test for covariate significance in quantile regression”同时检验所有分位数的协变量显著性，提出多种置换策略并证明渐近精确性；“Safe Feature Identification Rule for Fused Lasso”直接服务于高维fused Lasso的加速；“Bayesian stability selection”也涉及高维设定下的变量选择不确定性量化。

对于因果推断方向的研究者，可优先关注“Reducing variance and improving bandwidth selection in density estimation”（半参数变换与方差-偏差权衡）和“Global test for covariate significance in quantile regression”（分位数回归的全局检验，其置换检验框架可迁移至因果效应的分布检验）。对于半参数效率方向，“Reducing variance”中的带宽选择器收敛速度分析直接相关。对于高维方向，“Safe Feature Identification Rule”和“Bayesian stability selection”提供了变量筛选与不确定性量化的新工具。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1007/s11222-026-10841-9](https://doi.org/10.1007/s11222-026-10841-9) — Reducing variance and improving bandwidth selection in density estimation via semiparametric transformations and local linear smoothing
- **作者**: Dimitrios Bagkavos, Prakash N. Patil, Thekke V. Ramanathan
- **期刊/来源**: Statistics and Computing
- **机构**: University of Ioannina · Mississippi State University · Punjabi University
- **分类**: vol 36 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的密度估计方法，结合初始参数近似与基于半参数数据变换的边界感知校正因子。主要贡献包括：在实现与现有半参数方法相当的偏差缩减的同时，更有效地降低估计方差；以及基于初始参数密度估计量开发MISE最优的plug-in带宽选择器。文章从解析上证明了所提数据驱动带宽的渐近分布及其向“理想”带宽的收敛速度优于标准非参数方法。通过模拟和真实数据分析，展示了该方法在复杂密度特征（如多模态）场景下有限样本估计性能的提升。该工作对您可能有用：它直接关联到您的非参数统计与半参数理论兴趣，特别是通过半参数变换改进非参数估计的方差-偏差权衡，其带宽选择器的收敛速度分析也与您熟悉的高维渐近理论有技术交集。
- **关键技术**: `semiparametric data transformation`, `local linear smoothing`, `plug-in bandwidth selector`, `MISE-optimal bandwidth`, `bias-variance tradeoff`
- **为什么对您有用**: 本文直接关联到您的非参数统计与半参数理论兴趣，特别是通过半参数变换改进非参数估计的方差-偏差权衡。其带宽选择器的收敛速度分析可与您熟悉的高维渐近理论（如minimax界）进行对比验证。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上进一步熟悉半参数变换的识别条件，才能评估该方法在您关注的因果推断（如密度比加权）中的可迁移性。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1007/s11222-025-10774-9](https://doi.org/10.1007/s11222-025-10774-9) — Global test for covariate significance in quantile regression
- **作者**: Tomáš Mrkvička, Konstantinos Konstantinou, Mikko Kuronen, Mari Myllymäki
- **期刊/来源**: Statistics and Computing
- **机构**: Sewanee: The University of the South · University of South Bohemia in České Budějovice · Chalmers University of Technology · Natural Resources Institute Finland
- **分类**: vol 36 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该文研究分位数回归中协变量对整体分布（所有分位数）的全局显著性检验问题。传统方法通常只检验某个特定分位数，而本文同时考虑所有分位数，将问题视为线性回归或Kolmogorov-Smirnov检验的推广。方法基于逐点系数估计、置换检验和全局包络检验（global envelope test），后者作为多重检验调整程序控制族系错误率，并自动给出导致拒绝的分位数或分类协变量水平的图形解释。针对Freedman-Lane置换策略在极端分位数下表现偏liberal的问题，作者提出了四种替代置换策略，其中一种适用于一般情形，其余适用于特定条件。理论部分证明了所提置换过程的渐近精确性，模拟研究比较了各策略的表现，并在两个实际数据中进行了应用。该文对您可能有用：它直接关联您对假设检验的兴趣，且其全局包络检验与多重比较调整的思路可迁移至您熟悉的高维或非参数检验设定。
- **关键技术**: `global envelope test`, `permutation test`, `quantile regression`, `family-wise error rate control`, `Freedman-Lane permutation`
- **为什么对您有用**: 直接连接到您primary interest中的hypothesis testing子方向，特别是全局检验与多重比较问题。您武器库中very_familiar的nonparametric statistics和high-dimensional asymptotics可以用于分析该方法的渐近性质或扩展到高维协变量场景。中期可做：若想将全局包络检验与您moderately_familiar的higher-order U-statistics结合（例如检验U-statistic型统计量的全局显著性），需先在多重比较调整的几何方法上长肌肉。

### 2. [10.1007/s11222-025-10820-6](https://doi.org/10.1007/s11222-025-10820-6) · [arXiv](https://arxiv.org/abs/2410.21914) — Bayesian stability selection and inference on selection probabilities
- **作者**: Mahdi Nouraie, Connor Smith, Samuel Muller
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在高维变量选择框架下，将贝叶斯分析融入稳定性选择（stability selection）方法，旨在改进选择概率的推断。传统稳定性选择依赖选择频率进行决策，忽略了领域先验知识。作者提出两阶段专家交互流程，允许统计学家基于专家知识构建先验分布，并让专家控制先验权重。利用后验分布，提供贝叶斯可信区间以量化变量选择的不确定性，并证明引入先验知识可降低选择概率的方差、提升选择稳定性，同时控制每族错误率（per-family error rate）。该方法保留了稳定性选择的通用性，适用于多种结构估计问题。对您而言，本文虽未直接涉及因果推断或高维U统计，但其在高维设定下结合先验信息进行推断的思路，可迁移至您熟悉的非参数统计或因果推断中的敏感性分析（如利用先验约束工具变量或负对照的强度）。
- **关键技术**: `stability selection`, `Bayesian inference`, `prior elicitation`, `posterior credible intervals`, `per-family error rate`
- **为什么对您有用**: 本文连接您对高维统计和假设检验的兴趣，具体在变量选择的不确定性量化上。您的技术武库中'非参数统计'和'高维渐近'可直接用于评估其贝叶斯可信区间的覆盖性质（如是否渐近精确）。中期可做：若想将类似贝叶斯先验融入因果推断的敏感性分析，需先在'moderately_familiar'的识别理论中熟悉工具变量或负对照的先验建模。

## 统计计算 / 算法  *(stat_computing, 17 篇)*

### 1. [10.1007/s11222-026-10852-6](https://doi.org/10.1007/s11222-026-10852-6) — Robust distances and multivariate outlier detection under heavy tails
- **作者**: Lucio Barabesi, Andrea Cerioli, Luis Angel García-Escudero, Agustín Mayo-Iscar, Domenico Perrotta, Francesca Torti
- **期刊/来源**: Statistics and Computing
- **机构**: University of Siena · University of Parma · Universidad de Valladolid · Joint Research Centre
- **分类**: vol 36 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对重尾分布（如多元 t 分布）下的稳健距离与异常值检测问题，提出统一框架。传统观点认为 t 分布本身具有稳健性，但实际数据中仍可能存在非高斯污染。作者利用广义半径过程理论，在高污染率下实现位置、散度和尾部参数的稳健估计。首先推导了与稳健马氏距离相关的主要统计泛函的影响函数，然后提出新的统计量来评估数据对多元 t 分布的符合程度，并自动推断自由度和污染率。计算上，通过蒙特卡洛估计半径过程分位数，并提供了可复现的算法实现。模拟实验验证了方法的准确性。对您而言，本文在统计计算（稳健估计、蒙特卡洛方法）和异常值检测方面有直接参考价值，且其广义半径过程框架可能为高维或因果推断中的稳健性分析提供新工具。
- **关键技术**: `generalized radius processes`, `influence function`, `high-breakdown estimation`, `Mahalanobis distances`, `Monte Carlo quantile estimation`, `multivariate Student-t distribution`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。其广义半径过程框架和影响函数推导，可迁移至您 very_familiar 的稳健估计与高维渐近分析。中期可做：将本文的稳健距离思想与您 moderately_familiar 的 semiparametric theory 结合，用于因果推断中的离群值敏感度分析。

### 2. [10.1007/s11222-026-10834-8](https://doi.org/10.1007/s11222-026-10834-8) — D-Optimal Subsampling Design for Multiple Linear Regression on Massive Data
- **作者**: Torsten Glemser, Rainer Schwabe
- **期刊/来源**: Statistics and Computing
- **机构**: Otto-von-Guericke-Universität Magdeburg
- **分类**: vol 36 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究海量数据下多元线性回归的 D-最优子抽样设计问题。目标是在观测数极大但协变量较少时，从全数据中选取固定比例的子样本，使得基于子样本的最小二乘估计的 D-最优性（即广义方差最小化）成立。作者利用最优设计理论和约束凸优化的等价性定理，推导出子抽样接受/拒绝的简单规则，并给出了易于实现的算法。此外，还提出了一种计算复杂度更低的简化子抽样方法，该方法偏离了严格的 D-最优设计。模拟研究将两种方案与 IBOSS 方法在固定子样本量下进行了比较。本文对您作为统计计算方向的研究者可能有用：它提供了一个从经典最优设计理论出发、可算法化实现的子抽样框架，与您武器库中的“软件开发”和“高维渐近”工具直接对接，且其设计思路可迁移至因果推断中大规模数据的处理。
- **关键技术**: `D-optimal design`, `subsampling`, `constrained convex optimization`, `equivalence theorem`, `IBOSS method`
- **为什么对您有用**: 本文属于统计计算（subsampling）方向，直接对应您的 primary interest 中的“statistical computing (numerical methods, algorithm)”。您武器库中“软件开发”和“高维渐近”两项 very_familiar 工具可直接用于实现和验证其算法在大规模数据下的表现。**中期可做**：若想将 D-optimal 子抽样推广到因果推断中的 ATE 估计或高维 U-统计量，需先在 moderately_familiar 的“identification theory in causal inference”或“theory of higher-order U-statistics”上长肌肉，以处理非 i.i.d. 或非线性目标函数下的子抽样设计。

### 3. [10.1007/s11222-026-10830-y](https://doi.org/10.1007/s11222-026-10830-y) · [arXiv](https://arxiv.org/abs/2510.18241) — Non-parametric estimation techniques of factor copula model using proxies
- **作者**: Bahareh Ghanbari, Pavel Krupskii, Laleh Tafakori, Yan Wang
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对因子 copula 模型中连接 copula 的估计问题，提出了一种基于非参数核估计的新方法。传统参数方法在高维或复杂依赖结构下估计困难，而本文利用核密度估计的灵活性来捕捉潜在依赖关系。作者证明了所提估计量在温和条件下具有相合性，并通过大量模拟研究验证了其有效性。该方法特别适用于连接 copula 结构未知或复杂的情形，为多元依赖建模提供了稳健且高效的估计途径。对您而言，本文的非参数核估计技术与您熟悉的非参数统计和估计理论直接相关，其相合性证明和模拟设计可作为您在高维因果推断或 U-统计量研究中借鉴的案例。
- **关键技术**: `kernel density estimation`, `factor copula model`, `non-parametric estimation`, `consistency proof`
- **为什么对您有用**: 本文属于统计计算与算法方向，与您的 primary interest 中的非参数统计和估计理论高度契合。您可以用 very_familiar 中的非参数统计和 minimax 界工具来评估该核估计量的收敛速率是否最优，或将其与您熟悉的 U-统计量方法结合以处理更复杂的依赖结构。立即可做：基于现有武器库即可复现并扩展其模拟设计。

### 4. [10.1007/s11222-026-10828-6](https://doi.org/10.1007/s11222-026-10828-6) · [arXiv](https://arxiv.org/abs/2404.10262) — Safe Feature Identification Rule for Fused Lasso by An Extra Dual Variable
- **作者**: Pan Shang, Huangyue Chen, Lingchen Kong
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对高维数据中 fused Lasso 计算耗时的问题，提出了一种安全特征识别规则（Safe Feature Identification Rule）。该规则通过引入一个额外的对偶变量，能够在低计算成本下预先剔除系数为零的非活跃特征，并识别系数相同的相邻特征，从而加速 fused Lasso 的求解。这是首个能够应用于 fused Lasso 的筛选规则，填补了现有 screening rules 在该模型上的空白。数值实验（模拟和真实数据）验证了该规则在减少计算时间方面的有效性。该规则可以嵌入任何高效的 fused Lasso 算法中，具有较好的通用性。对您而言，本文属于统计计算中算法加速的实用方法，与您对 statistical computing 的兴趣直接相关。
- **关键技术**: `safe feature screening`, `dual variable`, `fused Lasso`, `screening rule`, `high-dimensional regression`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 statistical computing。该规则通过引入额外对偶变量实现特征筛选，思路清晰且可嵌入现有算法，属于实用型方法贡献。您的武器库中 'software development' 和 'high-dimensional asymptotics' 可以支撑您理解其理论保证并评估其计算效率。该论文适合作为 gateway reading 了解 fused Lasso 的加速技巧，但方法学 novelty 有限（属于应用型改进），**中期可做**：若想深入，需先在 moderately_familiar 的 'M-estimation theory' 上熟悉 fused Lasso 的优化理论。

### 5. [10.1007/s11222-025-10801-9](https://doi.org/10.1007/s11222-025-10801-9) · [arXiv](https://arxiv.org/abs/2411.17400) — A Generalized Unified Skew-Normal Process with Neural Bayes Inference
- **作者**: Kesen Wang, Marc G. Genton
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对空间数据中常见的非高斯特征（偏斜、厚尾），提出广义统一偏斜正态（GSUN）空间过程，作为高斯过程的灵活替代。GSUN 过程基于统一偏斜正态（SUN）分布的一种更简洁、可解释的重参数化，并证明了其在大距离上相关性消失，从而保证了空间过程的合法性。在推断方面，作者开发了基于神经贝叶斯估计器的框架，采用深度图注意力网络（GAT）和编码器变换器架构，替代传统的 CNN 架构，在模拟研究中展示了更高的稳定性和准确性。通过 Pb 污染土壤数据的应用，GSUN 过程相比文献中其他偏斜模型表现出更强的灵活性。此外，通过概率积分变换（PIT）验证了 GSUN 过程与高斯过程及 Tukey g-and-h 过程的本质区别。该工作对您作为统计计算方向的研究者具有参考价值，因为它展示了如何将深度图网络（GAT）与贝叶斯推断结合，解决高维空间过程的参数估计问题，且方法可迁移至其他复杂统计模型的推断。
- **关键技术**: `neural Bayes estimators`, `graph attention networks (GATs)`, `encoder transformer`, `unified skew-normal (SUN) distribution`, `spatial process`, `probability integral transform (PIT)`
- **为什么对您有用**: 本文属于统计计算方向，直接连接您的 primary interest 中的 statistical computing。文中使用的神经贝叶斯估计器与深度图注意力网络（GAT）是您武器库中 moderately_familiar 的软件开发和 high-dimensional asymptotics 的延伸，但核心推断框架（神经网络替代 MCMC）对您而言是中期可做的：需先在 moderately_familiar 的 M-estimation theory 上加强，以理解其理论性质（如收敛性、效率）。本文作为 gateway reading，清晰展示了非高斯空间过程的建模与计算流程，值得花时间读全文以获取方法迁移的灵感。

### 6. [10.1007/s11222-026-10840-w](https://doi.org/10.1007/s11222-026-10840-w) — Score-driven time-varying parameter models with spline-based densities
- **作者**: Janneke van Brummelen, Paolo Gorgi, Siem Jan Koopman
- **期刊/来源**: Statistics and Computing
- **机构**: Tinbergen Institute · Vrije Universiteit Amsterdam
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种基于样条密度的得分驱动时变参数模型，无需指定参数化误差分布。核心方法是用自然三次样条构造灵活密度，其得分函数自然为样条形式，高斯分布是特例，且能刻画非对称、厚尾分布，从而产生对异常值稳健的时变参数更新函数。以位置模型和log-尺度模型为例，静态参数通过极大似然估计，并建立了部分渐近性质。实证部分用位置模型滤波美国CPI月度通胀序列，用尺度模型对S&P 500日度股票收益面板做波动率滤波，结果显示与现有竞争模型相比性能有竞争力。对您而言，本文是统计计算与时间序列建模的交叉，其样条密度构造和得分驱动框架可作为您软件开发和数值方法兴趣的参考案例，但方法学新颖性有限，属于应用导向的改进。
- **关键技术**: `score-driven models`, `natural cubic spline density`, `time-varying parameter models`, `maximum likelihood estimation`, `outlier-robust filtering`
- **为什么对您有用**: 本文属于统计计算与时间序列建模的交叉，与您的primary interest中'statistical computing (numerical methods, algorithm)'直接相关，可作为软件开发和数值方法兴趣的参考案例。武器库中'very_familiar'的'nonparametric statistics'和'software development'可直接用于理解其样条密度构造和实现，但方法学新颖性有限，属于应用导向的改进，暂不可做直接follow-up。

### 7. [10.1007/s11222-026-10826-8](https://doi.org/10.1007/s11222-026-10826-8) · [arXiv](https://arxiv.org/abs/2601.05586) — Poisson Hyperplane processes with rectified linear units
- **作者**: Shufei Ge, Shijia Wang, Lloyd Elliott
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文建立了 Poisson 超平面过程 (PHP) 与两层 ReLU 神经网络之间的概率联系，证明带高斯先验的 PHP 是两层 ReLU 网络的一种替代概率表示。通过分解命题，展示了基于 PHP 构建的两层神经网络可扩展到大规模问题。提出了一种退火序贯蒙特卡洛 (SMC) 算法用于贝叶斯推断，数值实验表明该方法优于经典的两层 ReLU 网络。代码已开源。对您而言，本文属于统计计算方向，展示了如何将几何概率模型（PHP）与神经网络结构结合，并开发了可扩展的贝叶斯推断算法，这与您对统计计算（数值方法、算法）的兴趣直接相关。
- **关键技术**: `Poisson hyperplane processes`, `ReLU neural networks`, `annealed sequential Monte Carlo`, `Bayesian inference`, `probabilistic representation`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的 primary interest 中的 'statistical computing (numerical methods, algorithm)'。文章将几何概率模型与神经网络结合，并开发了可扩展的贝叶斯推断算法，属于方法学贡献。您的武器库中 'software development' 和 'nonparametric statistics' 可用于理解其概率表示和实现，但核心的 SMC 算法和 PHP 几何并非您非常熟悉的领域，因此属于**中期可做**：需先在 'M-estimation theory' 或 'semiparametric theory' 上进一步熟悉贝叶斯推断的渐近性质，才能深入评估该方法的理论保证。

### 8. [10.1007/s11222-026-10825-9](https://doi.org/10.1007/s11222-026-10825-9) · [arXiv](https://arxiv.org/abs/2502.03279) — Posterior SBC: simulation-based calibration checking conditional on data
- **作者**: Teemu Säilynoja, Marvin Schmitt, Paul-Christian Bürkner, Aki Vehtari
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出后验 SBC（Posterior SBC）方法，用于在给定观测数据条件下验证贝叶斯推断算法和模型实现的正确性。传统 SBC 从先验采样参数并生成模拟数据，检验推断在参数先验支持下的整体自洽性；后验 SBC 则从观测数据的后验分布采样参数，再生成模拟数据，从而检验推断是否在特定观测数据下有效。方法核心是构造一个条件化的自洽性检验统计量，并利用秩统计量进行可视化诊断。通过三个案例（多层模型、微分方程模型、基于神经网络的摊销贝叶斯推断的联合神经科学模型）展示了后验 SBC 在发现条件性推断失败方面的实用性。对您而言，该方法为贝叶斯计算中的模型诊断提供了新工具，可应用于您感兴趣的因果推断和流行病学中的复杂模型验证。
- **关键技术**: `Simulation-based calibration (SBC)`, `posterior SBC`, `rank-based diagnostics`, `amortized Bayesian inference`, `neural network inference`
- **为什么对您有用**: 本文属于统计计算（贝叶斯推断验证）方向，与您的 primary interest 中的统计计算和软件工具开发直接相关。您的 technical arsenal 中的非参数统计和软件工具开发经验可用于实现和扩展后验 SBC 方法，例如将其应用于因果推断中的复杂模型（如 IV、mediation）的验证。中期可做：需先熟悉贝叶斯计算和 SBC 框架（moderately_familiar 中的 M-estimation 理论可辅助理解），但核心思想简单，可快速上手。

### 9. [10.1007/s11222-025-10808-2](https://doi.org/10.1007/s11222-025-10808-2) · [arXiv](https://arxiv.org/abs/2206.02340) — Unifying Summary Statistic Selection for Approximate Bayesian Computation
- **作者**: Till Hoffmann, Jukka-Pekka Onnela
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在近似贝叶斯计算（ABC）框架下，系统研究了低维汇总统计量的选择问题。作者将现有汇总统计量分为三类，并指出正确区分这三类对于理解降维算法的行为至关重要。核心贡献是证明最小化期望后验熵（EPE）是一个统一原则，许多现有方法（如基于互信息、后验均值等的方法）均可视为其特例或极限情形。方法上，作者利用条件密度估计（如神经网络）来自动学习高保真汇总统计量，避免了手工构造。在多个基准问题（包括多峰后验、群体遗传学模型和动态网络模型）上，该方法与专用似然方法竞争，甚至在某些情况下更优。对您而言，本文属于统计计算中的算法设计，其利用条件密度估计自动学习汇总统计量的思路，与您熟悉的非参数统计和软件工具有直接联系，可作为进入ABC领域的入门读物。
- **关键技术**: `Approximate Bayesian Computation`, `expected posterior entropy`, `conditional density estimation`, `summary statistics`, `likelihood-free inference`
- **为什么对您有用**: 本文属于统计计算（stat_computing）领域的gateway reading，适合作为ABC方法的入门。您的武器库中'非参数统计'和'软件工具'足以支撑理解其核心方法（条件密度估计），但ABC的模拟推断范式与您熟悉的频率学派方法差异较大，属于'暂不可做'——核心缺失是ABC的MCMC/SMC采样器和模拟校准机制。不过，本文对汇总统计量选择的理论统一视角（EPE最小化）值得一读，可启发您在高维统计或因果推断中如何设计低维充分统计量。

### 10. [10.1007/s11222-025-10807-3](https://doi.org/10.1007/s11222-025-10807-3) · [arXiv](https://arxiv.org/abs/2501.07790) — Sampling from density power divergence-based generalized posterior distribution via stochastic optimization
- **作者**: Naruki Sonobe, Tomotaka Momozaki, Tomoyuki Nakagawa
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对密度幂散度（DPD）贝叶斯后验的采样问题，提出一种结合损失-似然自助法（loss-likelihood bootstrap）与随机梯度下降（SGD）的近似采样方法。DPD后验在理论上具有稳健性，但包含难以处理的积分项，传统数值积分在高维下计算昂贵。作者将DPD估计转化为一个可微优化问题，利用SGD迭代更新参数，避免了MCMC中每次迭代的积分计算。方法适用于一般参数模型，并扩展至广义线性模型。模拟表明，该方法在高维下计算可扩展性显著优于传统MCMC，且能处理含不可积积分项的复杂模型。对您而言，本文展示了统计计算中优化与贝叶斯推断结合的新思路，属于统计计算方向，但方法本身与您的主要兴趣（因果推断、高维统计）无直接交叉，可作为计算技巧的参考。
- **关键技术**: `loss-likelihood bootstrap`, `stochastic gradient descent`, `density power divergence`, `robust Bayesian inference`, `generalized linear models`
- **为什么对您有用**: 本文属于统计计算方向，与您的主要兴趣（因果推断、高维统计）无直接交叉。作为计算技巧的参考，可了解SGD在稳健贝叶斯推断中的应用，但武器库中已有软件开发和M-estimation经验，无需额外工具即可理解。暂不可做：核心问题（DPD后验采样）与您的因果推断或高维统计问题距离较远，不构成直接follow-up。

### 11. [10.1007/s11222-025-10818-0](https://doi.org/10.1007/s11222-025-10818-0) — Bayesian analysis of Cox-type regression model with partly linear covariate effects via reversible jump Markov chain Monte Carlo
- **作者**: Hengtao Zhang, Yuanke Qu, Kin Yau Wong, Chun Yin Lee
- **期刊/来源**: Statistics and Computing
- **机构**: Guangdong Ocean University · Hong Kong Polytechnic University · Hang Seng University of Hong Kong · University of Hong Kong
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对部分线性Cox型回归模型，提出一种贝叶斯估计方法。该模型允许连续协变量对删失结局存在非线性效应，传统频率学派方法需手动选择带宽或样条基函数数量。作者采用可逆跳跃马尔可夫链蒙特卡洛（RJMCMC）算法，在后验推断过程中自适应地估计未知函数中节点的数量和位置，无需额外调参。通过模拟研究评估了有限样本性能，并在两个医学数据集上展示了方法的有效性。代码已公开。该方法的核心贡献在于将模型选择与估计统一在贝叶斯框架下，避免了交叉验证等计算开销。对于您而言，本文展示了RJMCMC在复杂半参数模型中的实际应用，可作为统计计算（MCMC算法实现与调优）的参考案例，但方法学新颖性有限。
- **关键技术**: `reversible jump MCMC`, `partly linear Cox model`, `adaptive knot selection`, `Bayesian survival analysis`, `spline basis functions`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。您对MCMC算法和软件实现有经验（very_familiar中的software development），可以快速理解其RJMCMC实现细节。但本文的方法学贡献主要是将现有技术（RJMCMC + 样条）应用于特定模型，缺乏新的理论或计算效率突破，属于'暂不可做'的范畴——核心机器（RJMCMC的收敛性分析、节点选择的先验敏感性）不在您的武器库中，且与您更核心的因果推断/高维统计兴趣无直接关联。

### 12. [10.1007/s11222-025-10815-3](https://doi.org/10.1007/s11222-025-10815-3) · [arXiv](https://arxiv.org/abs/2208.04669) — Boosting with copula-based components
- **作者**: Simon Boge Brant, Ingrid Hobæk Haff Author
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种新的加法提升模型，其基学习器为基于copula的回归模型（Noh et al. 2013），旨在捕捉复杂的交互效应。模型无需对连续协变量进行离散化，因此特别适用于包含大量连续协变量的回归问题。作者设计了高效的模型选择与组件评估算法，该算法也可推广至其他类型的copula回归模型。提供了R包copulaboost实现。模拟与实证研究表明，该方法的预测性能优于或至少不逊于同类方法。对您而言，本文属于统计计算与算法设计方向，其模型选择与拟合算法中的计算效率策略（如避免离散化、组件评估）可能对您开发或优化统计软件中的数值方法有参考价值。
- **关键技术**: `copula-based regression`, `additive boosting`, `model selection`, `R package implementation`
- **为什么对您有用**: 本文属于统计计算方向，与您的primary interest中的'statistical computing (numerical methods, algorithm)'直接相关。您武器库中'very_familiar'的'software development'可直接用于评估其R包copulaboost的代码质量与可扩展性；'moderately_familiar'的'M-estimation theory'可用于分析其boosting算法的收敛性。本文是gateway-reading级别的计算论文，不涉及复杂理论，适合快速阅读以获取算法设计灵感，值得花时间读全文。

### 13. [10.1007/s11222-026-10842-8](https://doi.org/10.1007/s11222-026-10842-8) · [arXiv](https://arxiv.org/abs/2406.04653) — Variational Markov chain mixtures with automatic component selection
- **作者**: Christopher E. Miles, Robert J. Webber
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出用变分期望最大化（variational EM）自动确定混合马尔可夫链的组件数，避免传统模型比较或后验采样。核心贡献是证明了分类误差的理论下界，并展示变分EM能达到与最优误差缩放一致的性能。实验涵盖音乐收听、超长跑和基因表达三个真实数据集，验证了方法能识别有意义的异质性。对您而言，本文的变分EM框架和自动组件选择思路可迁移到您熟悉的因果推断或高维统计中的混合模型问题，尤其是当您需要处理纵向数据或潜在异质性时。
- **关键技术**: `variational expectation-maximization`, `Markov chain mixture`, `automatic component selection`, `classification error lower bound`
- **为什么对您有用**: 本文属于统计计算方向，直接对接您的primary interest中的统计计算。变分EM的自动组件选择机制可迁移到因果推断中的潜在类别模型（如混合效应IV或纵向数据），您熟悉的非参数统计和M估计理论可用于分析其收敛性。中期可做：需先在moderately_familiar的M估计理论上巩固，以严格推导变分EM的渐近性质。

### 14. [10.1007/s11222-026-10843-7](https://doi.org/10.1007/s11222-026-10843-7) — Combining Adaptive MCMC and Nested Sampling for Robust Bayesian Model Selection with reduced prior sensitivity
- **作者**: José Carlos García-Merino, Miracle Amadi, Heikki Haario, Carmen Calvo-Jurado, Enrique García-Macías
- **期刊/来源**: Statistics and Computing
- **机构**: Universidad Nacional de Educación a Distancia · Lappeenranta-Lahti University of Technology · Universidad de Extremadura · Universidad de Granada
- **分类**: vol 36 · issue 2
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文针对贝叶斯模型选择中贝叶斯因子对先验假设敏感的问题，提出了一种结合自适应MCMC与嵌套采样的新方法DRAM-NS。该方法在标准嵌套采样算法前增加一个基于数据子集的初步MCMC步骤，从而自然地整合无信息或 improper 先验，降低模型比较对先验的敏感性。DRAM-NS的核心机制是利用自适应MCMC（DRAM算法）从数据中学习后验分布，以此构建一个更稳健的“数据驱动”先验，再用于嵌套采样计算边际似然。数值实验表明，在先验知识不确定的场景下，DRAM-NS相比标准NS提供了更可靠的模型选择框架。该方法主要贡献在于缓解了贝叶斯证据计算中长期存在的先验敏感性难题，而无需依赖复杂的先验设计。对您而言，本文属于统计计算方向的实用算法改进，其自适应MCMC与嵌套采样的结合思路可迁移至您在高维或因果推断中遇到的复杂后验计算问题，但方法学新颖性有限，属于增量改进。
- **关键技术**: `Nested Sampling`, `Adaptive MCMC (DRAM)`, `Bayesian evidence`, `Prior sensitivity`, `Model selection`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。您武器库中'very_familiar'的'软件发展'和'高维渐近'可用于评估其算法效率或扩展至高维设定。这是一篇方法学增量改进的论文，可作为统计计算领域的入门级阅读，但核心机器（嵌套采样、自适应MCMC）不在您当前武器库的核心区，属于'暂不可做'——需先熟悉MCMC诊断与嵌套采样实现。

### 15. [10.1007/s11222-026-10844-6](https://doi.org/10.1007/s11222-026-10844-6) · [arXiv](https://arxiv.org/abs/2504.14164) — Learning over von Mises–Fisher distributions via a Wasserstein-like geometry
- **作者**: Kisung You, Dennis Shung, Mauro Giuffrè
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对单位超球面上的 von Mises–Fisher (vMF) 分布族，提出了一种基于最优传输理论的新型几何距离度量。由于 vMF 分布的归一化常数难以处理且缺乏合适的几何度量，现有比较工具十分有限。作者在高浓度区域利用高斯近似，推导出一个可分解为均值方向测地距离和浓度参数方差项的闭式 Wasserstein-like 距离。该距离保留了球面几何结构，并诱导出非退化 vMF 分布空间上的潜在几何结构。作为主要应用，作者开发了高效的 vMF 混合约简算法，能在高维设置下实现保结构的混合模型压缩。在合成数据及真实高维嵌入（如生物医学句子表示和深度视觉特征）上的实验验证了该距离在分布区分和可解释推断中的有效性。对您而言，本文属于统计计算方向，其核心贡献在于为球面数据提供了一种可计算且几何感知的距离工具，与您对统计计算（数值方法与算法）的兴趣直接相关。
- **关键技术**: `Wasserstein-like distance`, `von Mises–Fisher distribution`, `Gaussian approximation`, `optimal transport`, `mixture reduction`, `spherical geometry`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您 primary interest 中的 'statistical computing (numerical methods, algorithm)'。其核心贡献——为 vMF 分布设计可计算的距离度量并用于混合模型压缩——是一个典型的算法设计问题，您可以用 very_familiar 中的 'software development' 和 'high-dimensional asymptotics' 来复现或扩展其算法（例如，验证高斯近似的精度界）。中期可做：若想将此类几何距离推广到其他指数族分布，需先在 moderately_familiar 的 'M-estimation theory' 上加强。

### 16. [10.1007/s11222-025-10816-2](https://doi.org/10.1007/s11222-025-10816-2) · [arXiv](https://arxiv.org/abs/2412.04956) — Fast estimation of the composite link model for multidimensional grouped counts
- **作者**: Carlo G. Camarda, María Durbán
- **期刊/来源**: Statistics and Computing
- **分类**: vol 36 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对分组计数数据的复合链接模型（Composite Link Model），在惩罚似然框架下提出了一种加速估计算法。核心创新是将迭代估计过程重新表述为广义线性数组模型（GLAM），利用数组运算替代传统矩阵运算，从而在高维、大尺度设定下大幅降低计算时间和内存消耗。通过模拟和真实高维死亡率数据集验证，新方法在保持估计精度的同时，计算速度提升显著，存储效率也得到改善。该方法适用于流行病学、人口学等需要处理分组汇总计数数据的领域。对您而言，本文的数组运算技巧（GLAM）与您熟悉的einsum/tensor-contraction思路高度契合，可直接迁移到高维U-statistics或因果推断中涉及分组数据的计算优化问题，属于立即可做的方向。
- **关键技术**: `Generalized Linear Array Models (GLAM)`, `penalized likelihood`, `composite link model`, `array operations`, `computational efficiency`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。其核心技巧——将模型估计转化为数组运算（GLAM）——与您very_familiar的'computation of higher-order U-statistics (treewidth / tensor contraction / einsum)'在思想上一脉相承，您可以直接用einsum库复现或扩展其算法。立即可做：用您熟悉的tensor-contraction视角分析其计算复杂度，或将其数组化思路迁移到您自己的U-statistics计算框架中。

### 17. [10.1007/s11222-026-10823-x](https://doi.org/10.1007/s11222-026-10823-x) — A unified and efficient proximal gradient descent algorithm for penalized convoluted support vector machines
- **作者**: Bingzhen Chen, Canyi Chen
- **期刊/来源**: Statistics and Computing
- **机构**: Hangzhou Dianzi University · University of Michigan
- **分类**: vol 36 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对高维分类中惩罚支持向量机（SVM）的 hinge 损失非光滑性导致优化困难的问题，提出了一种基于卷积平滑的统一框架。通过将 hinge 损失与光滑核函数卷积，得到一族光滑且仍保持凸性的替代损失函数，从而允许使用近端梯度下降（proximal gradient descent）算法高效求解。算法在每次迭代中只需计算光滑梯度与近端算子，避免了子问题求解或坐标下降的复杂内循环。作者在模拟和真实高维数据上进行了系统数值实验，与 ADMM、坐标下降等现有算法对比，展示了所提方法在收敛速度和分类精度上的优势。对您而言，本文的卷积平滑技巧可迁移至其他非光滑统计估计问题（如分位数回归、稳健 M-估计），且其算法实现思路对您熟悉的软件开发和数值方法方向有直接参考价值。
- **关键技术**: `convolution smoothing`, `proximal gradient descent`, `hinge loss approximation`, `convex optimization`, `high-dimensional classification`
- **为什么对您有用**: 本文属于统计计算方向，直接对接您 primary interest 中的 statistical computing（数值方法与算法）。卷积平滑技巧是处理非光滑损失的一般性工具，您可以用 very_familiar 的 minimax 理论分析其光滑偏差与方差之间的 tradeoff，或将其与您熟悉的 inverse problems 中的正则化方法结合。中期可做：若想将此类平滑方法推广到更复杂的非光滑目标（如双稀疏惩罚），需先在 moderately_familiar 的 M-estimation 理论上补足光滑损失下的渐近理论。

## 其他  *(other, 2 篇)*

### 1. [10.1007/s11222-025-10796-3](https://doi.org/10.1007/s11222-025-10796-3) — A Support vector machine-based mixture cure model for mixed case interval censored data
- **作者**: Suvra Pal, Wisdom Aselisewine
- **期刊/来源**: Statistics and Computing
- **机构**: The University of Texas at Arlington
- **分类**: vol 36 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对混合病例区间删失（MCIC）数据提出一个半参数两分量治愈模型。第一分量用支持向量机（SVM）替代传统广义线性模型来建模治愈概率，以捕捉复杂协变量效应；第二分量用Cox比例风险结构建模未治愈者的生存分布，保持协变量效应的可解释性。这是首个将机器学习算法用于MCIC数据治愈模型的工作。估计采用EM算法，模拟研究显示SVM基模型优于传统方法。最后用NASA的减压病数据做实证分析。该文方法学贡献在于将SVM嵌入治愈模型框架，但核心统计工具（EM、Cox）均为经典，对您的主攻方向（因果推断、高维统计、U统计量）无直接方法学连接。
- **关键技术**: `support vector machine`, `mixture cure model`, `mixed case interval censored data`, `EM algorithm`, `Cox proportional hazards`
- **为什么对您有用**: 该文属于统计计算与生存分析的应用，与您的主攻方向（因果推断、高维统计、U统计量）无直接方法学连接。武器库中的非参数统计、M估计理论可理解其框架，但无具体可攻口子。暂不可做——核心机器（SVM嵌入治愈模型）不在武器库中，且该方向非您兴趣核心。

### 2. [10.1007/s11222-026-10829-5](https://doi.org/10.1007/s11222-026-10829-5) — A New Look at the Flexible Generalized Skew-Normal Family: A Trimodal Extension and Numerical Insights
- **作者**: Michele Bufalo, Andrea Nigri
- **期刊/来源**: Statistics and Computing
- **机构**: University of Bari Aldo Moro · University of Foggia
- **分类**: vol 36 · issue 2
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文提出一类新的广义偏态正态分布族，通过在FGSN密度（Ma & Genton 2004）的奇数多项式项中引入五次项，使密度函数在参数约束下最多可呈现三个模态。核心方法是利用正态累积分布函数内的奇数多项式调控偏度、峰度和多模态性，并给出模态数量的理论界。数值实验系统评估了似然估计和参数估计的数值稳定性，证明该方法在实际应用中具有鲁棒性。实证部分使用人类死亡率数据库（HMD）的人口统计数据验证模型拟合优度，并与多个基准模型对比。该工作属于分布族扩展与数值计算的应用研究，方法学创新在于多项式阶数的提升和模态数刻画，但未涉及因果推断、高维统计或半参效率理论等您的主要兴趣方向。
- **关键技术**: `generalized skew-normal distribution`, `odd polynomial expansion`, `multimodal density estimation`, `maximum likelihood estimation`, `numerical stability analysis`
- **为什么对您有用**: 本文属于统计分布建模与数值计算的应用研究，与您的主要兴趣（因果推断、高维统计、半参理论）无直接关联。虽然涉及数值稳定性分析，但方法学深度有限，且未提供可迁移至您武器库（如U统计量、半参效率界）的新工具。作为gateway reading价值低，不推荐深入阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

