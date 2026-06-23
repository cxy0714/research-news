# Statistica Sinica  ·  2026-06-23

- 共 84 篇 · Statistica Sinica

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文主要围绕**高维统计推断**、**假设检验**与**非参数/半参数方法**三条主线展开，同时涉及因果推断、计算方法及实验设计等应用方向。高维统计方面，聚焦于随机矩阵谱理论、协方差/精度矩阵估计、因子模型及高维时间序列，代表性工作包括 Spearman 秩相关矩阵的 CLT、多元纵向数据的精度矩阵估计、以及网络辅助因子模型等。假设检验方面，涵盖高维位置参数检验、图模型拟合优度检验、多重检验及变点检测，多篇论文涉及 Bootstrap、极值理论及非参数秩方法。非参数与半参数方向，重点关注函数型数据的降维与回归、分位数回归及生存分析中的效率理论。因果推断虽篇数不多，但涉及匹配估计、MNAR 识别及中介分析等核心议题。

**高维统计推断**主线在本期占据显著篇幅，核心推进在于复杂依赖结构与重尾数据下的理论突破。在随机矩阵领域，*Large Dimensional Spearman's Rank Correlation Matrices* 将经典样本协方差矩阵的 CLT 扩展至 Spearman 秩相关及 3 阶 U 统计量情形，为高维独立检验提供了新工具；*Concentration Inequalities for High-Dimensional Linear Processes* 则在 mixingale 依赖下建立了 $l_\infty$ 范数集中不等式，推进了高维时间序列的非渐近理论。在协方差与图模型估计方面，*Adaptive Block Banding Precision Matrix Estimation* 与 *Estimating Covariance Matrices at Different Levels in Repeated Measurements* 分别利用 Kronecker 结构和层次结构解决精度矩阵与协方差矩阵的稀疏估计问题。此外，*Network Assisted Approximate Factor Model Estimation* 和 *Grouped Heterogeneous Gaussian Graphical Models* 引入网络信息与异质性结构，拓展了因子模型与图模型的估计效率。

**假设检验**主线呈现出与高维数据、重尾分布及复杂依赖深度结合的趋势。针对高维位置参数，*Spatial-Sign Based Maxsum Test* 与 *Statistical Inference For Ultrahigh Dimensional Location Parameter* 分别提出了针对稀疏备择假设的 max-sum 组合检验和基于空间中位数的 Bahadur 表示，兼顾了稳健性与高维适应性。在图模型与网络检验方面，*Universally Consistent Tests for the Graph of a Gaussian Graphical Model* 利用极值理论构造了全局拟合优度检验，而 *Weighted Conditional Network Testing* 解决了多组高维精度矩阵的条件等同性检验问题。针对依赖结构与多重检验，*Multiple Testing of One-Sided Hypotheses under Unknown Dependence* 利用因子模型近似解决未知依赖下的 FDR 控制，*An Automatic MDDM-Based Test for Martingale Difference Hypothesis* 则提出了数据驱动的滞后阶选择以检验鞅差序列。非参数检验方面，*Center-Outward Ranks and Signs for Testing Conditional Quantile Independence* 结合中心向外秩与分位数鞅差散度，实现了分布自由的条件独立性检验。

**非参数与半参数方法**主线侧重于函数型数据的降维、稳健估计及效率理论。函数型数据分析中，*On the Optimality of Functional Sliced Inverse Regression* 首次证明了 FSIR 在一般设定下的 minimax 最优性；*Functional Tensor Regression* 与 *Asymmetric Estimation for Varying-Coefficient Additive Model* 分别在张量回归和异方差变系数模型中引入了低秩分解与 RKHS 方法。在稳健与效率推断方面，*Empirical Risk Minimization for Losses without Variance* 在仅有 $(1+\epsilon)$ 阶矩的条件下探讨了经验风险最小化，*Identification and Efficient Estimation in Regression Analysis with Response Missing Not At Random* 利用 shadow variable 实现了 MNAR 机制下的半参数有效估计。因果推断方向，*Rematching Estimators For Average Treatment Effects* 通过双向匹配改进了 ATE 估计的效率，*Semi-supervised Regression Analysis with Model Misspecification and High-dimensional Data* 则在协变量偏移下利用 AIPW 框架实现了稳健推断。

对于关注**因果推断**与**半参数效率**的研究者，建议优先阅读 *Rematching Estimators For Average Treatment Effects*（匹配估计量的效率改进）、*Identification and Efficient Estimation in Regression Analysis with Response Missing Not At Random*（MNAR 下的有效识别与估计）以及 *Semi-supervised Regression Analysis with Model Misspecification and High-dimensional Data*（高维模型误设下的 AIPW 推断）。关注**高维随机矩阵与假设检验**的读者，可重点参阅 *Large Dimensional Spearman's Rank Correlation Matrices*（秩相关矩阵的谱理论）、*Concentration Inequalities for High-Dimensional Linear Processes*（高维时间序列集中不等式）及 *Universally Consistent Tests for the Graph of a Gaussian Graphical Model*（图模型的一致检验）。

## 因果推断  *(causal_inference, 8 篇)*

### 1. [10.5705/ss.202024.0306](https://doi.org/10.5705/ss.202024.0306) — Rematching Estimators For Average Treatment Effects
- **作者**: Lam Lam Hui, Kin Wai Chan
- **期刊/来源**: Statistica Sinica
- **机构**: Chinese University of Hong Kong
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在因果推断中，匹配估计量因其直观性而被广泛应用，但固定匹配数（M0）的简单匹配估计量通常效率低下。本文提出一种可变匹配数的rematching estimators，核心思想是通过从相反方向重新匹配已处理单位，从而利用未匹配的对照单位，在不增加偏差的前提下提升效率。该方法适用于平均处理效应（ATE）及其对受处理总体的效应（ATT）。理论证明所提估计量渐近有效，且一致优于相同M0的简单匹配估计量。模拟研究证实，在有限样本下rematching estimators显著改善了简单匹配估计量的表现。实证部分将该方法应用于National Supported Work数据。对您而言，本文是因果推断中匹配方法的重要效率改进，可直接关联您对ATE估计理论的兴趣，并可能启发更高效的估计策略。
- **关键技术**: `Matching estimators`, `Rematching`, `Variable number of matches`, `Average treatment effect (ATE)`, `Asymptotic efficiency`
- **为什么对您有用**: 本文直接连接您在因果推断中对ATE估计方法的兴趣，特别是匹配估计量的效率改进。从您的技术武库看，您对'estimation theory in causal inference'非常熟悉，因此可以立即复现其理论分析或验证其渐近结论。此外，该方法的识别条件检验可作为'moderately_familiar'中'identification theory'的练习。判断：立即可做——您熟悉的非参统计和因果推断估计工具足以支撑深入阅读和潜在扩展。

### 2. [10.5705/ss.202024.0204](https://doi.org/10.5705/ss.202024.0204) — Identification and Efficient Estimation in Regression Analysis with Response Missing Not At Random
- **作者**: Qinglong Tian, Donglin Zeng, Jiwei Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对回归分析中响应变量缺失非随机（MNAR）的问题，提出一种同时实现半参数效率与模型鲁棒性的估计方法。传统MNAR方法要么强加参数假设以获得效率但牺牲鲁棒性，要么放松假设但导致效率损失；而非参数MNAR机制通常带来模型不可识别问题。作者引入shadow variable解决了识别问题，进而采用sieve方法对MNAR机制进行非参数建模，无需对缺失机制施加严格参数形式。该方法所构造的估计量达到了感兴趣参数（回归系数等）的半参数效率界，即渐近方差最小。论文详细给出了识别条件，构造了半参数似然函数，并严格证明了估计量的半参数有效性。数值模拟和实际数据应用展示了所提方法相比传统方法的优势。该工作与您对因果推断中缺失数据和半参数效率理论的研究高度相关，其shadow variable思路和处理MNAR的非参数识别策略可直接应用于因果推断中的类似问题（如中介分析中的缺失数据或纵向数据中的选择性缺失）。
- **关键技术**: `shadow variable`, `sieve estimation`, `semiparametric efficiency bound`, `EM algorithm`
- **为什么对您有用**: 该论文直接对应您的primary interests中的因果推断（缺失数据识别）和效率理论（半参数效率界）。您可以使用武器库中'very_familiar'的非参数统计和因果推断估计理论来理解其sieve估计与识别论证，并可尝试将shadow variable方法推广到您的proximal causal inference或IV设定下的缺失数据问题。**中期可做**：需先在'moderately_familiar'的半参数理论（如EIF推导）上加强，以验证该文效率界推导是否适用于更复杂的因果参数。

### 3. [10.5705/ss.202024.0188](https://doi.org/10.5705/ss.202024.0188) — Conditional Generative Adversarial Network for Individualized Causal Mediation Analysis with Survival Outcome
- **作者**: Cheng Huan, Xinyuan Song, Hongwei Yuan
- **期刊/来源**: Statistica Sinica
- **机构**: Chinese University of Hong Kong · University of Macau
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在生存结局的因果中介分析框架下，目标是估计个体化的直接效应（NDE）和间接效应（NIE），设定为 right-censored survival time 且假设 sequential ignorability。本文提出 CGAN-ICMA-SO 方法，利用条件生成对抗网络（CGAN）学习潜在结局的条件分布，从而避免对生存模型的具体参数假设。理论部分证明了在 mild regularity 条件下，条件生成器的估计分布收敛到真实条件分布，但未给出收敛速率或 semiparametric efficiency bound。数值实验显示方法优于五种 baseline，应用于 ADNI 数据集揭示了 APOE-4 等位基因对 AD 发病时间的个体化直接和中介效应。对您在 mediation 和 efficiency theory 方向的兴趣有连接，但理论深度有限。
- **关键技术**: `conditional generative adversarial network (CGAN)`, `causal mediation analysis`, `individualized treatment effect`, `survival outcome with censoring`, `distributional convergence`
- **为什么对您有用**: 本文属于因果中介分析（您的 primary interest 中 mediation 子方向），但技术路线是深度生成模型而非 semiparametric efficiency 或 influence function 理论。您武器库中的 semiparametric theory 和 minimax bounds 可用于审视其理论贡献——本文仅给出分布收敛性，未触及 rate-optimality 或 efficiency bound，这是一个可攻的口子。follow-up 判定：**中期可做**——若想深入，需先在深度学习估计的理论分析（如 neural network convergence rate）上长肌肉，目前武器库不直接覆盖。

### 4. [10.5705/ss.202024.0013](https://doi.org/10.5705/ss.202024.0013) · [arXiv](https://arxiv.org/abs/2401.04265) — Estimation of Subsidiary Performance Metrics under Optimal Policies
- **作者**: Zhaoqi Li, Houssam Nassif, Alex Luedtke
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究在政策学习中，当主性能指标的最优策略已确定时，如何估计附属性能指标。首先提出基于一种新的边际条件的Wald型推断方法，在该条件及正则性假设下，证明一阶校正估计量是半参数有效的。然而边际条件对邻近最优策略的附属指标行为施加了较强限制，可能不成立。为此进一步提出不依赖边际条件的两阶段策略：第一阶段构建候选策略集，第二阶段构建该集合上的均匀置信区间。通过数值模拟评估了不同场景下方法的有限样本表现。该工作为因果推断中策略评估的效率理论提供了新视角，且其推断框架可与研究者熟悉的非参估计技术直接对接。
- **关键技术**: `policy learning`, `margin condition`, `one-step corrected estimator`, `Wald-type inference`, `uniform confidence interval`, `semi-parametric efficiency`
- **为什么对您有用**: 该论文直接关联因果推断中的策略学习与效率理论，属于研究者的主要兴趣。一阶校正估计量的半参效率分析可以借助研究者非常熟悉的非参统计与minimax界工具进行验证或延伸，属于立即可做的方向；两阶段均匀置信区间构建涉及非参集估计，研究者也可基于因果推断估计理论进行后续改进探索。

### 5. [10.5705/ss.202024.0261](https://doi.org/10.5705/ss.202024.0261) · [arXiv](https://arxiv.org/abs/2406.13906) — Semi-supervised Regression Analysis with Model Misspecification and High-dimensional Data
- **作者**: Ye Tian, Peng Wu, Zhiqiang Tan
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在半监督学习与协变量偏移迁移学习的框架下，研究条件均值模型的回归系数推断问题，允许模型误设。核心方法是增广逆概率加权（AIPW），并使用正则化校准估计倾向得分和结果回归模型，两者存在顺序依赖。理论证明：当倾向得分模型正确指定时，即使结果回归模型误设且数据维度很高，所提估计量仍能保持一致性、渐近正态性和有效的置信区间。此外，本文展示了一个统一视角，将先前多种方法纳入该AIPW框架。模拟和真实数据应用验证了理论结果。本文与因果推断中的AIPW方法直接相关，其中的高维稳健推断技术可迁移到您的因果效应估计问题中。
- **关键技术**: `Augmented Inverse Probability Weighting (AIPW)`, `Regularized Calibration`, `Propensity Score Estimation`, `High-dimensional Regression Inference`, `Model Misspecification Robustness`, `Semi-supervised Learning`
- **为什么对您有用**: 本文的核心方法 AIPW 是因果推断中估计平均处理效应的标准工具，且重点处理高维协变量下的模型误设——这与您的因果推断（identification/estimation sensitivity analysis）及高维统计兴趣高度吻合。您非常熟悉的“高维渐近”和“因果推断估计理论”可以直接用于理解本文的理论框架，并可能进一步推广到 Proximal CI 或 IV 设定中的稳健推断。该工作立即可做——您现有的高维统计与 AIPW 工具足以复现、扩展或对比其实验设计。

### 6. [10.5705/ss.202023.0317](https://doi.org/10.5705/ss.202023.0317) · [arXiv](https://arxiv.org/abs/2103.00209) — Statistical Inference for Local Granger Causality
- **作者**: Yan Liu, Masanobu Taniguchi, Hernando Ombao
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 该文将Granger因果关系从平稳时间序列推广到局部平稳多元过程，提出了局部Granger因果的定义和统计推断方法。目标是从时变谱密度矩阵中刻画随时间演化的因果关系，并在频域进行识别。方法基于局部Whittle似然对时变自回归模型进行参数化估计，得到谱密度矩阵的估计量。在正则条件下，估计量渐近服从多元正态分布；进一步，局部Granger因果的检验统计量收敛到多元正态分布的二次型。模拟研究证实了有限样本性能，并应用于脑电信号发现了新的功能连接关系，以及识别金融数据的结构变化。对您有用：直接连接时间序列因果推断（Granger因果）和假设检验的渐近理论，同时其应用场景（神经科学和金融）与您的二级兴趣吻合。
- **关键技术**: `Local Granger causality`, `Locally stationary processes`, `Local Whittle likelihood`, `Time-varying spectral density`, `Quadratic form test`, `Multivariate autoregressive models`
- **为什么对您有用**: 直接关联您的主要兴趣中的因果推断（时间序列Granger因果）和假设检验（检验统计量的渐近分布）。您的武器库中的'high-dimensional asymptotics'和'M-estimation theory'可用来理解其估计与检验机制；此外，该文的检验问题可视为一个参数化假设检验，您的'nonparametric statistics'背景也能对比分析正则条件的影响。立即可做——基于M-estimation和渐近工具即可复现其推导或扩展至高维设定。

### 7. [10.5705/ss.202024.0227](https://doi.org/10.5705/ss.202024.0227) · [arXiv](https://arxiv.org/abs/2407.05400) — Collaborative Analysis for Paired A/B Testing Experiments
- **作者**: Qiong Zhang, Lulu Kang, Xinwei Deng
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该论文研究多个A/B测试共享同一组实验对象时的协同分析问题，目标是在个体效应相关的条件下提高各实验处理效应的估计精度。方法基于线性混合效应模型，将同一个体的不同实验响应通过随机截距建模相关性，利用广义最小二乘（GLS）得到估计量，证明了在正态性假设下该估计量是渐近最优线性无偏估计（BLUE）。推导了估计量的渐近分布，并给出了协方差矩阵的替换估计以保证实现简便。计算上只需一次协方差矩阵分解，对连续和离散响应均适用。模拟和某在线平台真实案例表明，协同分析相比逐实验单独分析能显著降低方差。对您而言，该工作为实验因果推断中利用个体相关性提高效率提供了具体方法，可与您熟悉的因果推断估计理论（如方差减少技术、交叉设计）直接对接。
- **关键技术**: `collaborative analysis`, `paired A/B tests`, `best linear unbiased estimator`, `asymptotic normality`, `random effects model`, `generalized least squares`
- **为什么对您有用**: 该论文属于实验因果推断中的估计效率改进，直接关联您 primary interest 中的因果推断子方向（实验设计与方差减少）。您的技术武器库中“estimation theory in causal inference”可立即用于评估该方法在非参数或协变量调整下的扩展性，以及验证其BLUE最优性对模型误设的稳健性。立即可做：基于线性模型和渐近理论，您能快速复现并尝试将框架推广至更一般的因果估计量（如ATE的双稳健估计）的协同分析。

### 8. [10.5705/ss.202023.0202](https://doi.org/10.5705/ss.202023.0202) — Addressing Label Noise in Causation Classification via Kernel Embeddings
- **作者**: Pingbo Hu, Grace Y. Yi
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文考虑因果方向分类问题：给定成对向量序列，判断二者间是否存在因果关系，形式化为二分类问题。核心设定是标签存在误标（mislabeling），这在因果发现数据中普遍存在。作者采用核均值嵌入（kernel mean embedding）将经验分布映射到再生核希尔伯特空间（RKHS），在特征空间中训练分类器。针对误标问题，文章量化了误标对分类器的影响，发展了校正误标效应的学习方法，并给出了理论保证。主要贡献在于将噪声标签学习（learning with noisy labels）框架引入因果分类，建立了 RKHS 下分类器一致性的理论结果。对您在因果推断中的 identification 理论和半参数/非参数方法有直接参考价值。
- **关键技术**: `kernel mean embedding`, `RKHS classification`, `learning with noisy labels`, `mislabeling effect quantification`, `causal direction classification`
- **为什么对您有用**: 本文连接因果推断中的因果发现问题与非参数核方法，属于您 primary interest 中因果推断与半参数/非参数理论的交叉。技术层面使用核均值嵌入和 RKHS 分类，与您熟悉的 nonparametric statistics 直接相关；但核心机器是噪声标签学习框架，这在您武器库中未明确列出。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 基础上补充噪声标签学习的理论工具（如 loss correction、robust risk minimization），才能深入分析该方法在更复杂因果设定下的性质。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 12 篇)*

### 1. [10.5705/ss.202024.0395](https://doi.org/10.5705/ss.202024.0395) · [arXiv](https://arxiv.org/abs/2411.15861) — Large Dimensional Spearman's Rank Correlation Matrices: The Central Limit Theorem and Its Applications
- **作者**: Hantao Chen, Cheng Wang
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本文在高维渐近框架下（p,n同阶增长至无穷），研究Spearman秩相关矩阵的线性谱统计量的中心极限定理。该结果将经典样本协方差矩阵的谱统计量CLT（Ann.Statist.2015）扩展至秩相关矩阵情形。进一步，作者考虑了改进的Spearman相关矩阵（即3阶U统计量），并建立了其对应的CLT。作为应用，提出了三种新的高维独立检验统计量，并证明了其渐近正态性。数值模拟验证了所提方法在有限样本下的良好表现。对您而言，本篇论文直接结合了您核心的高维随机矩阵理论和高阶U统计量两个兴趣方向，特别是3阶U统计量在相关矩阵谱分析中的使用值得关注。
- **关键技术**: `Linear spectral statistics`, `Central limit theorem for random matrices`, `Spearman's rank correlation`, `U-statistic of order 3`, `High-dimensional independence test`
- **为什么对您有用**: 本文同时对接您对高维统计（随机矩阵理论）和高阶U统计量的兴趣。核心工具是线性谱统计量的CLT，这与您非常熟悉的高维渐近工具（Stieltjes变换、Marchenko-Pastur定律）直接相通。此外，改进Spearman矩阵是3阶U统计量，您可立即利用武器库中非常熟悉的『高阶U统计量计算（树宽/张量收缩）』视角来分析其计算成本（例如，将该U统计量表示为张量收缩并评估其计算复杂度）。因此，本文值得深入阅读，并且您已有的工具足以支撑对本文方法的理论理解和扩展探索——立即可做。

### 2. [10.5705/ss.202024.0199](https://doi.org/10.5705/ss.202024.0199) — Efficient Learning of DAG Structures in Heavy-tailed Data
- **作者**: Wei Zhou, Xueqian Kang, Wei Zhong, Junhui Wang
- **期刊/来源**: Statistica Sinica
- **机构**: Chinese University of Hong Kong · Southwestern University of Finance and Economics
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究线性 DAG 结构在重尾误差分布下的学习问题，目标是在误差分布属于 Pareto、Cauchy、log-normal 等重尾族时实现 DAG 结构的一致估计。提出两步算法 TopHEAT：首先基于新的拓扑层重建准则，以 top-down 方式逐层确定节点顺序，无需传统的 faithfulness 假设；其次通过针对重尾分布修正的条件独立性检验恢复有向边。理论证明在适当正则条件下算法可达到 exact DAG structure consistency，Monte Carlo 模拟显示在有限样本下优于现有方法。实证分析 17 国汇率数据，揭示金融传染的源头与路径。对您有用之处：DAG 结构学习是因果推断中结构发现的核心问题，本文处理重尾数据的思路可补充您对高维因果推断中稳健性问题的理解。
- **关键技术**: `topological layer reconstruction`, `heavy-tailed error distributions`, `conditional independence testing`, `DAG structure consistency`, `linear structural equation models`
- **为什么对您有用**: 本文属于因果推断的结构学习方向，与您 primary interest 中的因果推断（identification、estimation）直接相关。技术层面主要依赖高维回归与条件独立性检验的修正，属于您 very_familiar 的高维渐近与估计理论范畴。follow-up 判断：立即可做——用您熟悉的高维估计理论可以审视其 consistency 条件是否可进一步放松或 sharpen rate。

### 3. [10.5705/ss.202023.0364](https://doi.org/10.5705/ss.202023.0364) · [arXiv](https://arxiv.org/abs/2307.12395) — Concentration Inequalities for High-Dimensional Linear Processes with Dependent Innovations
- **作者**: Eduardo Fonseca Mendes, Fellipe Lopes Lima Leite
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维线性过程，创新项具有 sub-Weibull 尾部且允许 mixingale 依赖结构，目标是建立向量过程 l∞ 范数的指数型集中不等式。主要技术工具包括 Bernstein 型不等式和混合条件下的矩不等式，得到了自协方差矩阵最大元素范数的非渐近集中界，该界不要求创新独立性，仅依赖 mixingale 系数衰减。利用该不等式，进一步推导了大维 VAR(p) 系统 Lasso 估计的统计推断性质（如 ℓ∞ 收敛率）以及 HAC 协方差矩阵估计的收敛性。理论结果表明，在弱依赖弱尾条件下，集中速率可与独立情形相匹敌。该不等式对您的高维时间序列推断问题（如工具变量估计中的弱识别诊断）有直接工具价值，尤其适合结合您的 high-dimensional asymptotics 背景来构造联合置信区间。
- **关键技术**: `Concentration inequalities for linf norm`, `Sub-Weibull tail conditions`, `Mixingale dependence`, `Autocovariance matrix concentration`, `Sparse estimation for VAR(p)`, `HAC covariance estimation`
- **为什么对您有用**: 直接服务于高维时间序列的统计推断——您的 primary interest 中 high-dimensional statistics 和 hypothesis testing 都依赖类似集中工具。您 very_familiar 的 high-dimensional asymptotics 可快速验证该界在 VAR 稀疏估计中的最优性（与 minimax bounds 对比）。立即可做：将本文不等式应用于高维因果推断中的时间序列数据（例如带有滞后因变量的 IV 模型），构造 l∞ 联合置信区间或进行弱识别检验。

### 4. [10.5705/ss.202024.0307](https://doi.org/10.5705/ss.202024.0307) · [arXiv](https://arxiv.org/abs/2312.16769) — Estimation and Inference for High-dimensional Multi-response Growth Curve Model
- **作者**: Xin Zhou, Yin Xia, Lexin Li
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维多响应变量增长曲线模型（GCM）的估计与推断问题，目标参数为时间-响应系数矩阵，核心假设包括 Kronecker 乘积结构的协方差分解。方法上提出多步估计程序：首先利用 Kronecker 结构将高维协方差矩阵分解为时间相关阵与响应相关阵，通过 pooling correlated samples 提高估计精度；其次分别估计各协方差分量，采用 l2-regularized estimator 处理高维情形。推断方面，构造全局效应检验（Wald-type test）与个体效应检验，建立检验的 size、power 性质及 FDR 控制；理论分析涉及高维渐近下的 concentration inequality 与随机矩阵理论。主要贡献在于将传统低维 GCM 推广至 p >> n 情形，Kronecker 协方差结构的设计对您的高维随机矩阵研究有参考价值。
- **关键技术**: `Kronecker product covariance decomposition`, `multi-step regularized estimation`, `high-dimensional hypothesis testing`, `false discovery rate control`, `longitudinal neuroimaging analysis`
- **为什么对您有用**: 连接到您 primary interest 中的高维统计与随机矩阵理论——Kronecker 结构下的协方差估计涉及随机矩阵的谱分析，这是 RMT 在高维协方差估计中的典型应用场景。您武器库中的 high-dimensional asymptotics 与 minimax bounds 可用于审视其估计量的 rate optimality。follow-up 判断：**立即可做**——用您熟悉的 minimax bound 技术可验证其估计量是否达到最优收敛速率，或探讨更弱假设下的估计。

### 5. [10.5705/ss.202024.0310](https://doi.org/10.5705/ss.202024.0310) · [arXiv](https://arxiv.org/abs/2501.03463) — Auxiliary Learning and its Statistical Understanding
- **作者**: Hanchao Yan, Feifei Wang, Chuanxin Xia, Hansheng Wang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维小样本情形下，如何利用多个共享相同协变量的辅助任务提升主任务参数估计的统计效率。设定为线性回归及广义线性模型框架，目标参数为主任务回归系数，核心假设是各任务共享协变量分布但响应变量不同。提出一种加权估计量，将主任务的OLS估计量与各辅助任务的OLS估计量做线性组合，并解析推导出使估计量方差最小化的最优权重。理论分析给出了加权估计量的渐近正态性及方差缩减的显式表达，证明了在辅助任务与主任务相关性足够强时可实现效率提升。数值实验和智能售货机深度学习实例验证了方法的有效性。对您研究高维估计效率理论有参考价值。
- **关键技术**: `auxiliary learning`, `weighted OLS estimator`, `optimal weight derivation`, `asymptotic normality`, `variance reduction`, `generalized linear models`
- **为什么对您有用**: 连接到 primary interest 中的高维统计与效率理论。本文的核心技术工具（加权组合估计量的最优权重解析推导、渐近正态性证明）属于您 very_familiar 的估计理论与高维渐近范畴。follow-up 判定：立即可做——可用您熟悉的 minimax bound 工具分析该加权估计量在更一般的高维设定（如 p/n → γ ∈ (0,1)）下的最优性，或探索与 semiparametric efficiency bound 的联系。

### 6. [10.5705/ss.202023.0131](https://doi.org/10.5705/ss.202023.0131) — Adaptive Block Banding Precision Matrix Estimation For Multivariate Longitudinal Data
- **作者**: Chunhui Liang, Wenqing Ma, Yanyuan Ma
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对多元纵向数据提出一种精度矩阵估计方法，假设真实精度矩阵具有带状Kronecker稀疏结构（BKS），即分解为自适应带状矩阵与稀疏矩阵的Kronecker积，两因子均正定。该方法通过设计特殊惩罚函数实现自适应带状化，并用Lasso惩罚强制稀疏性；优化上采用交替凸搜索（ACS）算法交替更新两个因子矩阵，并证明了算法的收敛性与估计量的渐近收敛速率。模拟研究表明BKS在有限样本下显著优于现有方法，并应用于EEG和ADHD数据集，在捕获带状稀疏特征方面表现更优。这篇论文将高维精度矩阵估计与结构化Kronecker分解结合，与您的高维统计兴趣直接相关；其ACS算法及收敛性分析也贴近统计计算方向。
- **关键技术**: `Banded Kronecker Sparse forms (BKS)`, `Adaptive banding penalty`, `Lasso penalization`, `Alternative Convex Search (ACS) algorithm`, `Precision matrix estimation`
- **为什么对您有用**: 该论文属于高维精度矩阵估计，直接对应您的高维统计兴趣；其结构化分解（Kronecker积+自适应带状）为处理多元纵向数据的协方差结构提供了新视角。您在very_familiar武器库中的高维渐近分析可用于验证其理论最优性，软件开发能力可用于复现或扩展其算法。整体为立即可做的follow-up：可用熟悉的高维工具评估其minimax rate是否紧，或模拟其ACS算法与其他优化方法的计算权衡。

### 7. [10.5705/ss.202024.0170](https://doi.org/10.5705/ss.202024.0170) — Network Assisted Approximate Factor Model Estimation
- **作者**: Yuzhou Zhao, Xinyan Fan, Bo Zhang
- **期刊/来源**: Statistica Sinica
- **机构**: Renmin University of China
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对经典近似因子模型在小样本下估计精度不足的问题，引入辅助网络信息，提出联合拟最大似然估计（JQMLE）方法。该方法能灵活利用网络结构并允许网络异质性，通过联合优化因子载荷和网络参数实现信息共享。理论分析建立了估计量的一致性和渐近正态性，并证明当样本量较小时，新方法的收敛速度优于传统最大似然估计。数值模拟验证了有限样本性能。该工作为高维统计中的因子模型提供了利用辅助数据的实用框架。
- **关键技术**: `approximate factor model`, `network information`, `quasi-maximum likelihood estimation`, `convergence rate improvement`, `heterogeneous network modeling`
- **为什么对您有用**: 本文直接关联您的高维统计兴趣，特别是因子模型估计问题。您熟练掌握的高维渐近理论可直接用于检验文中收敛率界的紧性，并可进一步探索网络信息对因子数选择的影响。目前您的武器库中缺乏网络随机图模型的系统知识，属于中期可做：需先熟悉网络模型（如随机图、网络异质性）的渐近理论，再结合 high-dimensional asymptotics 工具进行拓展。

### 8. [10.5705/ss.202024.0258](https://doi.org/10.5705/ss.202024.0258) — Grouped Heterogeneous Gaussian Graphical Models for High-Dimensional Clustered Data
- **作者**: Xin Zeng, Shuangge Ma, Qingzhao Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维聚类数据，提出分组异质性高斯图模型（Grouped-HGGM），核心目标是在网络分析中同时刻画变量间依赖和组件异质性。模型假设簇可分入若干组，异质性通过组级混合概率捕获，并通过融合技术自动确定组件数目并实现稀疏估计。与传统需预设组件数的方法不同，融合惩罚同时实现组结构选择和边集稀疏化，理论部分证明了参数估计的一致性。方法结合了高斯图模型的似然框架与组正则化，属于高维图模型中的异质性建模前沿。该工作为聚类数据网络分析提供了一种无需预指定组件数的自动化方案，对您的兴趣中高维统计的图模型推断有直接参考价值；其融合稀疏估计的思路也可迁移到其他高维分组结构问题中。
- **关键技术**: `fusion penalty`, `grouped heterogeneous Gaussian graphical models`, `automatic determination of number of components`, `high-dimensional clustering`, `consistency in graphical models`
- **为什么对您有用**: 本文属于高维图模型方向，与您的高维统计兴趣（尤其是 high-dimensional asymptotics）直接重叠。您武器库中非常熟悉的 high-dimensional asymptotics 和 nonparametric statistics 可直接用于理解论文的 consistency 证明框架；其融合惩罚的统计性质也可借助 minimax bounds 进行理论对比。**中期可做**：若要跟踪或拓展该方向（如向非高斯图或因果结构扩展），需先补充 moderately_familiar 中的 semiparametric theory 或 identification theory 以处理模型异质性的识别问题。

### 9. [10.5705/ss.202024.0194](https://doi.org/10.5705/ss.202024.0194) — Convoluted Support Matrix Machine in High Dimensions
- **作者**: Bingzhen Chen, Canyi Chen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维矩阵输入的分类问题，扩展传统向量SVM到结构化矩阵输入场景。由于hinge损失非光滑，作者提出一种凸平滑过程（convoluted hinge loss）来替代原始损失函数，同时引入弹性网型惩罚以处理高维矩阵的稀疏性和结构。该方法在理论上达到了最优的统计收敛率（minimax rate），并且由于损失函数的凸性和光滑性，设计了具有线性收敛速率的优化算法，实现简单。数值模拟和一例脑电图（EEG）应用验证了该方法在分类准确率和计算效率上的优势。对您而言，该工作属于高维统计中带结构化输入的判别问题，使用了SVM框架和弹性网正则化，与您的高维渐近和优化算法兴趣有交集。
- **关键技术**: `convex smoothing of hinge loss`, `elastic-net penalty for matrix inputs`, `optimal statistical convergence rate`, `fast linear convergence algorithm`, `electroencephalography (EEG) classification`
- **为什么对您有用**: （1）该论文处理高维矩阵输入的分类问题，属于您'高维统计'兴趣中一类特殊数据结构的判决问题，与高维协方差或矩阵回归有相近之处；（2）您武器库中的'最小最大界'（very_familiar）可以直接用来检查其声明的最优收敛率是否紧，或者能否在其他损失下获得更锐的界；（3）该文的理论和算法框架可以成为您'统计计算'工具箱中一个现成的基准方法，**立即可做**的是用现成的凸分析和高维渐近知识复现并扩展其理论证明，无需额外工具。

### 10. [10.5705/ss.202024.0279](https://doi.org/10.5705/ss.202024.0279) — Estimating Covariance Matrices at Different Levels in Repeated Measurements
- **作者**: Sunpeng Duan, Guo Yu, Juntao Duan, Yuedong Wang
- **期刊/来源**: Statistica Sinica
- **机构**: University of California, Santa Barbara
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 重复测量数据在多个领域常见，其层次结构导致组间和组内协方差不同，但现有稀疏协方差估计方法大多假设独立样本。本文区分了组间协方差矩阵和组内协方差矩阵，为两者同时提出稀疏正定估计。估计器通过凸优化求解，可高效计算。作者推导了估计误差率（Frobenius范数下），理论上证明该方法在高维情形下一致。模拟研究表明估计器在有限样本下优于忽略层次结构的备选方法。实证部分用于构建临床变量的组间与组内协方差图。该工作对您的高维统计兴趣直接相关，尤其涉及协方差矩阵估计的稀疏性和正定性约束。
- **关键技术**: `sparse covariance estimation`, `convex optimization`, `between-subject/within-subject covariance`, `estimation error rates`, `repeated measurements`, `positive-definite constraint`
- **为什么对您有用**: 该文直接连接您的高维统计（协方差矩阵估计）与统计计算（凸优化）兴趣。您武器库中的 high-dimensional asymptotics 可直攻其误差率证明的紧性，且稀疏估计方法可迁移至其他因果推断中的协方差结构调整。立即可做：用您熟悉的 high-dimensional asymptotics 验证其理论界是否最优。

### 11. [10.5705/ss.202024.0021](https://doi.org/10.5705/ss.202024.0021) · [arXiv](https://arxiv.org/abs/2401.13379) — An Ising Similarity Regression Model for Modeling Multivariate Binary Data
- **作者**: Zhi Yang Tho, Francis K. C. Hui, Tao Zou
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对多元二元数据的依赖结构建模，提出Ising相似性回归模型，将Ising模型中成对交互系数表示为相似性度量的线性组合。模型通过伪似然函数结合自适应lasso惩罚进行变量选择，并建立当相似性度量个数和响应维数趋于无穷时估计量与选择的一致性理论。仿真结果表明，在估计交互系数矩阵方面，该方法优于多种现有Ising模型估计器。实际应用于美国参议员投票记录，量化了党派、职业和社交网络相似性对投票一致性的驱动作用。本文方法扩展了经典Ising模型至协变量驱动的回归框架，在高维正则化与相合性方面为图模型选择提供了新视角。
- **关键技术**: `Ising model`, `similarity regression`, `pseudo-likelihood`, `adaptive lasso`, `high-dimensional consistency`, `variable selection`
- **为什么对您有用**: 本文的高维正则化选择方法与您在高维统计（非随机矩阵）方面的兴趣直接对应，其相合性证明使用了您非常熟悉的高维渐近工具；正则化思想可迁移至因果推断中的协变量选择问题（如IV或mediation的筛选）。当前您可立即使用熟悉的高维渐近理论复现并理解其理论证明，并尝试将相似性回归框架移植到因果模型的设定中。

### 12. [10.5705/ss.202023.0287](https://doi.org/10.5705/ss.202023.0287) · [arXiv](https://arxiv.org/abs/2406.14772) — Consistent Community Detection in Multi-Layer Networks with Heterogeneous Differential Privacy
- **作者**: Yaoming Zhen, Shirong Xu, Junhui Wang
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 在多层网络社区检测问题中，目标是研究在异质性差分隐私（节点级个性化隐私偏好）扰动下，社区结构的一致估计问题。设定为多层 degree-corrected stochastic block model (DC-SBM)，隐私机制为个性化边翻转，不同节点可有不同隐私预算。核心方法是先对扰动后的邻接矩阵进行去偏校正，再基于校正后的统计量进行谱聚类或似然型社区估计；理论证明在适当的隐私预算条件下，社区估计具有一致性，并刻画了隐私-效用权衡的定量界。关键技术工具包括 DC-SBM 的矩阵期望计算、谱聚类的一致性分析、以及隐私噪声对特征值/特征向量扰动的影响控制。主要理论结果给出了社区检测一致成立的隐私参数范围与样本量/层数条件，对您理解高维网络模型中的统计-计算-隐私权衡有参考价值。
- **关键技术**: `degree-corrected stochastic block model`, `heterogeneous differential privacy`, `spectral clustering consistency`, `privacy-utility tradeoff`, `matrix debiasing`, `multi-layer network analysis`
- **为什么对您有用**: 本文连接到您的高维统计与随机矩阵理论兴趣：DC-SBM 下的谱聚类一致性分析涉及邻接矩阵特征值/特征向量扰动理论，与 RMT 的 Marchenko-Pastur 型结果有技术相似性。您可以用 very_familiar 的 minimax bounds 和 high-dimensional asymptotics 工具审视本文声称的 privacy-utility 界是否紧，或推广到更一般的噪声机制。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上补充一些 M-estimation 在网络模型中的变体，才能切入更精细的效率界分析。

## 非参数 / 半参数  *(nonparam_semipara, 20 篇)*

### 1. [10.5705/ss.202023.0396](https://doi.org/10.5705/ss.202023.0396) · [arXiv](https://arxiv.org/abs/2307.02777) — On the Optimality of Functional Sliced Inverse Regression
- **作者**: Rui Chen, Songtao Tian, Dongming Huang, Qian Lin, Jun S. Liu
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究函数型切片逆回归（FSIR）在函数型充分降维问题中估计中心空间的 minimax 最优性。设定为多指标模型 Y = g(β^T X, ε)，目标是估计由 β 张成的中心空间，关键正则性假设涉及协方差算子的谱衰减速率。作者首先建立了条件均值协方差 FSIR 估计量的 concentration inequality，据此证明了该估计量像空间的 root-n 相合性。其次，采用截断方案估计协方差算子的逆，精确识别出使 FSIR 达到中心空间估计 minimax 最优收敛速率的截断参数选择。这是首篇严格证明 FSIR 在一般 Y（不必离散）设定下 minimax 最优性的工作，对您在非参数理论方向的 minimax bound 工具箱有直接参考价值。
- **关键技术**: `functional sliced inverse regression`, `minimax optimal rate`, `concentration inequality`, `covariance operator inversion`, `sufficient dimension reduction`, `spectral truncation`
- **为什么对您有用**: 直接连接到您 primary interest 中的非参数理论（minimax bounds）和半参数效率理论。您 very_familiar 的 minimax bounds for estimation problems 可以直接用来审视本文的速率下界证明是否紧；moderately_familiar 的 semiparametric theory 可帮助理解中心空间估计的效率问题。**立即可做**：用您熟悉的 minimax bound 技术验证本文声称的最优性，或尝试将 FSIR 框架推广到您熟悉的因果推断 setting（如 treatment effect heterogeneity 的降维）。

### 2. [10.5705/ss.202024.0104](https://doi.org/10.5705/ss.202024.0104) — A Semiparametric Quantile Single-Index Model for Zero-Inflated and Overdispersed Outcomes
- **作者**: Zirui Wang, Tianying Wang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对微生物组研究中零膨胀和过度离散的计数数据（如微生物丰度），提出了一种半参数分位数单指标模型（SQSI），以灵活建模丰度与协变量（如BMI）之间的关系。该模型通过单指标结构降低维数，并利用分位数回归的稳健性，避免了对参数分布（如零膨胀泊松或负二项）的强假设，能适应不同零膨胀比例。作者建立了指标系数估计和分位数曲线估计的渐近性质，包括相合性和渐近正态性，推导基于经验过程和M估计理论。模拟研究表明，该方法在模型拟合和预测方面优于传统参数模型，且计算效率可接受。本文与您的半参数和非参数理论方向直接相关，其渐近分析技巧（如经验过程、单指数模型的识别条件）值得参考，同时零膨胀数据的建模思路也可迁移到您的因果推断中处理结构零值问题。
- **关键技术**: `semiparametric single-index model`, `quantile regression`, `zero-inflated data`, `asymptotic properties`, `M-estimation`, `empirical process`
- **为什么对您有用**: 本文聚焦半参数单指数分位数回归与零膨胀数据，属于您的非参数/半参数理论兴趣；其渐近分析使用经验过程和M估计理论，您的nonparametric statistics背景（very_familiar）可直接理解核心论证，但要进一步扩展至类似模型（如高维协变量或异质性处理效应），需要先强化semiparametric theory（moderately_familiar）的识别和效率计算；因此属于中期可做：在现有的非参数基础上，补强半参数效率界和影响函数知识后，可以尝试推广至因果推断中的零膨胀结局变量问题。

### 3. [10.5705/ss.202024.0180](https://doi.org/10.5705/ss.202024.0180) — Semiparametric Inference for Functional Survival Models
- **作者**: Hongyi Zhou, Wenqing Su, Qixian Zhong, Ying Yang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对右删失生存数据中的函数型协变量建模问题，提出了一种基于常微分方程（ODE）的半参函数生存模型，以规避Cox模型比例风险假设难以验证的限制。模型同时包含标量系数和函数型参数，通过ODE框架将生存数据与函数型协变量联系起来。对于标量系数，建立了估计量的渐近正态性和半参有效性，从而实现了有效的统计推断。对于函数型参数，推导了渐近同时置信带。模拟研究评估了有限样本下的方法性能。该工作将半参效率理论拓展至函数型生存数据领域，为研究者熟悉的效率理论（semiparametric efficiency bounds）提供了新的应用场景。
- **关键技术**: `functional covariates`, `right-censored survival data`, `ordinary differential equation model`, `semiparametric efficiency`, `asymptotic simultaneous confidence band`
- **为什么对您有用**: 本文直接关联研究者的primary interest中的半参效率理论（semiparametric efficiency bounds），在函数型生存数据中证明了标量系数估计的半参有效性。研究者可利用其非常熟悉的非参统计工具（very_familiar中的nonparametric statistics）理解函数型参数部分，但需在moderately_familiar的semiparametric theory上进一步投入才能完全掌握证明细节。因此，该论文适合中期深入阅读，作为半参理论拓展至函数型数据的桥梁。

### 4. [10.5705/ss.202024.0342](https://doi.org/10.5705/ss.202024.0342) · [arXiv](https://arxiv.org/abs/2506.09358) — Functional Tensor Regression
- **作者**: Tongyu Li, Fang Yao, Anru R. Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究函数型张量回归问题，设定为响应变量对具有光滑变化结构的张量协变量的回归，回归系数同时具有高维张量结构和函数型光滑性。方法上采用低 Tucker 秩分解降维，并对函数型维度施加光滑正则化，提出 functional Riemannian Gauss--Newton 算法进行估计。理论上证明了算法具有二次收敛速率，并给出了依赖于张量协变量维度的估计误差界。模拟实验和神经影像数据分析验证了有限样本表现。对您而言，这是张量方法与函数型/非参数理论的结合，涉及您熟悉的非参数统计和高维渐近理论。
- **关键技术**: `Tucker rank decomposition`, `functional data analysis`, `Riemannian optimization`, `smoothness regularization`, `non-asymptotic error bound`
- **为什么对您有用**: 本文连接到您 primary interest 中的非参数/半参数理论和高维统计，属于张量回归与函数型数据分析的交叉。您武器库中的 very_familiar 项（非参数统计、高维渐近理论）可直接用于审视其 minimax optimality 和误差界紧性。follow-up 判断：**立即可做**——可用 minimax bound 工具验证其声称的收敛率是否达到理论下界，或探索更高阶 U-statistic 视角下的推断问题。

### 5. [10.5705/ss.202022.0206](https://doi.org/10.5705/ss.202022.0206) — Asymmetric Estimation for Varying-Coefficient Additive Model with Functional Response in Reproducing Kernel Hilbert Space
- **作者**: Yi Liu, Wei Tu, Yanchun Bao, Bei Jiang, Linglong Kong
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该论文研究函数型响应（functional response）的变系数可加模型，重点解决异方差性建模问题，提出期望分位数回归（expectile regression）作为均值回归的自然扩展。在再生核希尔伯特空间（RKHS）框架下，构建了不对称损失下的估计量，并在随机设计和固定设计两种设定下推导了极小极大最优收敛速率（minimax optimal rates）。理论贡献在于将expectile回归的理论保证从标量响应推广至函数型响应场景，填补了该方向的理论空白。模拟实验验证了方法在不同设置下的稳健性，并应用于乳腺癌临床试验的生活质量纵向数据，展示了实际效用。对您而言，该文提供了非参数回归中极小极大率分析的经典范例，可直接迁移至您熟悉的minimax bound工具箱；其中异方差建模思路对因果推断中的条件方差估计或敏感度分析也有潜在借鉴价值。
- **关键技术**: `RKHS`, `minimax convergence rate`, `expectile regression`, `function-on-scalar regression`, `varying-coefficient additive model`
- **为什么对您有用**: 连接非参数/半参数理论子方向，文中极小极大收敛速率分析可直接运用您熟悉的minimax bounds工具复现或扩展；异方差建模技巧可迁移至因果推断中的条件方差估计或敏感度分析，属于立即可做的技术迁移。

### 6. [10.5705/ss.202023.0329](https://doi.org/10.5705/ss.202023.0329) · [arXiv](https://arxiv.org/abs/2309.03818) — Empirical Risk Minimization for Losses without Variance
- **作者**: Guanhua Fang, Ping Li, Gennady Samorodnitsky
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究在重尾设定下的经验风险最小化问题，假设数据仅有 (1+ε)-阶矩而无有限方差，目标是估计风险最小化器。作者提出直接最小化经 Catoni 稳健估计的风险值，而非对数据进行截断后估计。核心工具是 Catoni 型影响函数结合 generalized generic chaining 方法建立 excess risk 上界，并分析了 robust gradient descent 和 empirical risk-based 两类优化算法的计算性质。理论结果表明在无方差条件下仍可获得有意义的收敛率，数值实验显示基于 Catoni 风险估计的方法优于截断数据方法。对您研究 semiparametric efficiency 和 influence function 理论有参考价值。
- **关键技术**: `Catoni's M-estimator`, `generalized generic chaining`, `robust gradient descent`, `excess risk bound`, `heavy-tailed empirical process`, `influence function`
- **为什么对您有用**: 连接到 semiparametric & nonparametric theory 中的 influence function 设计，以及 efficiency theory 中稳健估计的效率问题。您熟悉的 minimax bounds 和 nonparametric statistics 可直接用于分析其 excess risk 界是否紧。立即可做：用 very_familiar 的 minimax theory 检验其声称的 rate 是否达到下界，或用 moderately_familiar 的 M-estimation theory 探索更优的影响函数构造。

### 7. [10.5705/ss.202024.0063](https://doi.org/10.5705/ss.202024.0063) · [arXiv](https://arxiv.org/abs/2308.05883) — Empirical Bayes Estimation with Side Information: A Nonparametric Integrative Tweedie Approach
- **作者**: Jiajun Luo, Trambak Banerjee, Gourab Mukherjee, Wenguang Sun
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该论文研究带辅助信息（侧信息）的正态均值复合估计问题，在经验贝叶斯框架下提出非参数综合Tweedie（NIT）方法。核心思路是利用凸优化直接估计对数密度的梯度，从而将结构约束（如线性、稀疏或单调性）纳入估计过程，避免对先验分布做参数化假设。理论上，论文建立了NIT渐近风险的收敛速率，并精确刻画了辅助数据维度增加时风险改善与收敛速率退化之间的权衡。数值模拟和真实数据分析表明，在多种侧信息结构下，NIT优于现有经验贝叶斯方法（如参数Tweedie、非参数局部线性回归）。对您而言，该方法的风险-速率分析与高维统计中的minimax理论直接对话，可用您熟悉的minimax下界工具检验其速率是否最优，也可用非参数统计视角理解其结构约束的收益。
- **关键技术**: `Empirical Bayes`, `Tweedie formula`, `Nonparametric density gradient estimation`, `Convex optimization with structural constraints`, `Compound estimation risk analysis`
- **为什么对您有用**: 该论文涉及非参数估计理论与高维渐近分析，直接连接到您primary interests中的非参数统计和高维统计方向。您武器库中'minimax bounds for estimation problems'（非常熟悉）可用于验证其声称的收敛速率是否紧，而'high-dimensional asymptotics'（非常熟悉）可用于理解辅助数据维度带来的收益与代价。这是立即可做的follow-up问题：用minimax下界检验NIT的逼近速率，或在高维侧信息下推导更精细的风险刻画。

### 8. [10.5705/ss.202024.0159](https://doi.org/10.5705/ss.202024.0159) — Dimension Reduction for Extreme Regression via Contour Projection
- **作者**: Liujun Chen, Jing Zeng
- **期刊/来源**: Statistica Sinica
- **机构**: University of Science and Technology of China
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在极端回归（extreme regression）设定下，目标是推断给定预测变量时响应变量的极端值，核心挑战是预测变量的高维性和重尾分布。本文提出 central extreme subspace (CES) 的概念，证明其在温和正则条件下存在且唯一，通过将数据投影到 CES 实现降维同时保留推断条件极端值所需的全部信息。提出的 COPES 方法利用 contour projection 估计 CES，关键创新在于对重尾预测变量具有稳健性。理论贡献包括建立 CES 估计的 consistency，但未涉及收敛速率或 minimax 最优性。实证部分通过模拟和中国股市数据验证方法有效性。对您而言，这是非参数降维与重尾推断的交叉点，但理论深度较浅。
- **关键技术**: `sufficient dimension reduction`, `contour projection`, `central extreme subspace`, `heavy-tailed robustness`, `consistency theory`
- **为什么对您有用**: 本文属于非参数降维范畴，与您 primary interest 中的 semiparametric/nonparametric theory 相关，但理论贡献仅停留在 consistency 层面，未触及收敛速率、minimax bound 或 efficiency theory。您武器库中的 minimax bounds for estimation problems 可用于分析 CES 估计的最优速率问题——本文未解决的 theoretical gap。follow-up 判定：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上补充 sufficient dimension reduction 的效率界理论，才能切入 sharper rate 或 efficiency bound 的研究。

### 9. [10.5705/ss.202023.0143](https://doi.org/10.5705/ss.202023.0143) · [arXiv](https://arxiv.org/abs/1812.03775) — Sufficient Dimension Reduction for Classification
- **作者**: Xin Chen, Jingjing Wu, Zhigang Yao, Jia Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究高维分类问题中的充分降维，目标是估计中心降维子空间的方向向量，在模型自由设定下避免估计 link function。核心提出 maximal mean variance (MMV) 方法，基于 mean variance index 构造依赖度量，通过 sliced inverse regression 类似的谱分解估计降维方向。理论证明：在固定维度和发散维度两种情形下估计量的一致性，固定维度时建立渐近正态性，且允许类别数随样本量发散。方法在 n < p 情形表现良好，模拟和实例展示分类效率提升。对您在 semiparametric theory 和 minimax bounds 方面的兴趣有参考价值。
- **关键技术**: `sufficient dimension reduction`, `mean variance index`, `spectral decomposition`, `model-free estimation`, `diverging dimension asymptotics`, `central subspace`
- **为什么对您有用**: 连接到 semiparametric theory 的 model-free 降维方向，涉及 diverging dimension 下的渐近理论。您熟悉的 minimax bounds for estimation problems 可用于分析 MMV estimator 在高维情形的 rate optimality；nonparametric statistics 的工具可审视其正则性假设是否可弱化。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上加强，特别是 central subspace 的 efficiency bound 文献。

### 10. [10.5705/ss.202023.0288](https://doi.org/10.5705/ss.202023.0288) — Kernel Mode-Based Regression under Random Truncation
- **作者**: Tao Wang, Weixin Yao
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文考虑因变量受随机左截断的回归问题，提出基于核众数的参数回归模型，目标为估计条件众数而非条件均值。构造核平滑目标函数，并设计修正的众数期望最大化（EM）算法进行参数估计。在温和正则性条件下，证明了估计量的渐近正态性。进一步，开发基于众数的经验似然方法构造置信区间，经验对数似然比渐近服从卡方分布。结合SCAD惩罚，实现变量选择并证明其Oracle性质。模拟和房地产数据实例展示了方法的有限样本表现。该工作为截断数据下稳健回归提供了一套完整的估计、推断和变量选择框架。
- **关键技术**: `kernel mode regression`, `EM algorithm`, `empirical likelihood`, `SCAD penalty`, `oracle property`, `left truncation`
- **为什么对您有用**: 该文属于非参数/半参数回归在截断数据下的延伸，与研究者熟悉的非参数统计和M估计理论直接相关。研究者可以利用对核方法、经验似然和惩罚估计（SCAD）的深入理解，迅速评判该方法的收敛速率、渐近效率及算法收敛性。由于非参数统计和M估计均在武器库'非常熟悉'之列，该论文的估计和推断框架立即可用于比较或扩展研究。

### 11. [10.5705/ss.202024.0211](https://doi.org/10.5705/ss.202024.0211) — Sufficient Dimension Reduction for the Conditional Quantiles of Functional Data
- **作者**: Eliana Christou, Eftychia Solea, Shanshan Wang, Jun Song
- **期刊/来源**: Statistica Sinica
- **机构**: Queen Mary University of London · Bridge University
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究函数型预测变量下条件分位数的充分降维问题，目标是在保持非参数模型灵活性的同时，用有限维投影替代无限维函数型预测变量而不损失关于条件分位数的信息。作者提出基于 sliced inverse regression 和相关技术的降维估计方法，在非参数设定下推导了估计量的收敛速率，并通过模拟和 fMRI 实际数据验证有限样本表现。理论贡献在于建立了函数型分位数回归降维估计的收敛速率界，方法学 novelty 属于将现有降维技术扩展到函数型分位数场景。对您在 semiparametric theory 和 nonparametric statistics 方面的兴趣有直接参考价值。
- **关键技术**: `sufficient dimension reduction`, `functional data analysis`, `conditional quantile regression`, `convergence rate analysis`, `nonparametric estimation`
- **为什么对您有用**: 本文属于 semiparametric/nonparametric theory 方向，涉及函数型数据的降维与收敛速率分析，与您 primary interest 中的 nonparametric statistics 和 minimax bounds 直接相关。您武器库中 very_familiar 的 nonparametric statistics 和 minimax bounds for estimation problems 可直接用于审视本文的收敛速率是否紧、是否可改进。follow-up 判定：**立即可做**——用您熟悉的 minimax 理论框架检验本文速率的最优性，或探索更高阶估计量能否获得更快速率。

### 12. [10.5705/ss.202024.0339](https://doi.org/10.5705/ss.202024.0339) — Nonparametric Spatial Modeling towards the Mode
- **作者**: Tao Wang, Weixin Yao
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对空间数据提出一种非参数条件众数回归模型，假设响应变量Y在给定协变量X下的条件众数服从非参数回归结构，空间相关性通过协方差结构刻画。该方法旨在捕捉'最可能'效应，在数据分布不对称时能揭示均值或分位回归可能遗漏的结构。采用高斯核函数构造的模态期望最大化（MEM）算法进行数值估计，并推导了合适带宽下估计量的渐近分布。进一步将模型推广至可加形式以处理高维数据集，但本文侧重低维非参数设定。对于您的非参数理论兴趣，该工作展示了如何将经典核平滑与空间相关结构结合，其带宽选择与渐近论证可直接迁移到您的武器库中的非参数统计工具。
- **关键技术**: `modal regression`, `nonparametric regression`, `kernel smoothing`, `expectation-maximization (EM) algorithm`, `asymptotic distribution`, `spatial correlation`
- **为什么对您有用**: 直接关联您的主要兴趣——非参数理论（primary），特别是核方法在空间相关数据下的渐近理论；您的武器库中'nonparametric statistics'和'minimax bounds for estimation problems'可立即用于分析该估计量的最优性和带宽的有限样本行为；立即可做，因为非参数核平滑与EM算法都是您非常熟悉的工具，可进一步考察其minimax收敛率或推广到更高阶结构。

### 13. [10.5705/ss.202024.0369](https://doi.org/10.5705/ss.202024.0369) · [arXiv](https://arxiv.org/abs/2503.00716) — Quantile Residual Lifetime Regression for Multivariate Failure Time Data
- **作者**: Tonghui Yu, Liming Xiang, Jong-Hyeon Jeong
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究多元失效时间数据（multivariate failure time data）的分位数剩余寿命（QRL）回归问题，目标是估计协变量对剩余寿命分位数的效应。设定为边际半参数回归模型，同一受试者的多个失效时间存在相关性，采用 working independence 假设下的无偏估计方程方法。核心估计量通过求解估计方程得到，证明了其一致性与渐近正态性（n^{-1/2}-CAN），方差估计采用 resampling 技术与 sandwich estimator。主要贡献在于将单变量 QRL 回归推广到多元相关失效时间情形，提供了完整的推断框架（Wald-type test）。对您在纵向/多元失效时间数据的 semiparametric theory 方面有参考价值。
- **关键技术**: `quantile residual lifetime regression`, `marginal semiparametric model`, `unbiased estimating equations`, `working independence assumption`, `sandwich variance estimator`, `resampling techniques`
- **为什么对您有用**: 本文属于 semiparametric theory 在生存分析/纵向数据的应用，连接到您 primary interest 中的 semiparametric efficiency 与 estimation theory。技术上使用的是经典的 estimating equations + sandwich variance，属于您 very_familiar 的武器库范畴。follow-up 判断：**立即可做**——若想深入，可用 semiparametric efficiency theory 分析该估计量是否达到效率界，或探索是否存在效率改进空间（如引入 optimal weighting）。

### 14. [10.5705/ss.202023.0418](https://doi.org/10.5705/ss.202023.0418) · [arXiv](https://arxiv.org/abs/2505.00860) — Residual-based Alternative Partial Least Squares for Generalized Functional Linear Models
- **作者**: Yue Wang, Xiao Wang, Joseph G. Ibrahim, Hongtu Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在广义函数线性模型框架下，目标是基于高维医学影像数据预测临床结局，同时估计未知斜率函数和标量参数。作者提出 residual-based alternative partial least squares (RAPLS) 方法，将 APLS 算法迭代扩展以容纳标量协变量和非连续结局。理论上，文章建立了 RAPLS 斜率函数估计量的收敛速率，并通过额外的校准步骤证明了校准后 RAPLS 估计量的渐近正态性和效率。模拟研究和 ADNI 阿尔茨海默病数据应用展示了方法的有效性。对您而言，这是函数型数据回归与半参数效率理论结合的具体案例。
- **关键技术**: `functional linear models`, `partial least squares`, `convergence rate`, `semiparametric efficiency`, `asymptotic normality`, `scalar parameter calibration`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric efficiency theory——具体展示了在函数型数据回归设定下，如何通过校准步骤获得标量参数的 semiparametric efficiency bound。您可以用 very_familiar 的 minimax bounds 工具审视其斜率函数收敛速率是否紧，或用 moderately_familiar 的 semiparametric theory 深入理解其校准步骤的 influence function 构造。**中期可做**：若想深入函数型数据的效率理论，需先在 moderately_familiar 的 semiparametric theory 上积累函数型参数的效率界相关知识。

### 15. [10.5705/ss.202023.0366](https://doi.org/10.5705/ss.202023.0366) · [arXiv](https://arxiv.org/abs/2207.08373) — Functional Varying-Coefficient Model Under Heteroskedasticity with Application to DTI Data
- **作者**: Pratim Guha Niyogi, Ping-Shou Zhong, Xiaohong Joe Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究函数型变系数模型在异方差条件下的估计问题，目标是在空间相关误差设定下估计变系数函数 β(t)。提出多步估计程序：首先用局部线性 GMM 基于连续矩条件获得初始估计，然后将矩条件投影到特征函数上并以特征值加权组合，避免直接求逆协方差算子的困难。构造最优工具变量，在所有局部线性 GMM 估计类中最小化渐近方差函数，理论证明估计量达到 n^{-1/2}-CAN 且在异方差下优于忽略空间依赖的方法。模拟和 DTI 实数据验证了有限样本表现。对您在 semiparametric theory 和 efficiency theory 方面的兴趣有直接参考价值。
- **关键技术**: `local-linear GMM`, `optimal instrument variable`, `eigen-function projection`, `functional varying-coefficient model`, `spatial dependence`, `asymptotic efficiency`
- **为什么对您有用**: 直接连接到 semiparametric theory 和 efficiency theory 子方向——本文的核心贡献是在函数型数据设定下构造最优工具变量并证明其渐近有效性，这正是 semiparametric efficiency 的经典问题。您熟悉的 minimax bounds 和 M-estimation theory 可以用来审视其声称的 optimality 是否真正达到效率下界。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是函数型数据的效率界计算），才能判断该估计量是否真正 efficient 或是否有改进空间。

### 16. [10.5705/ss.202024.0118](https://doi.org/10.5705/ss.202024.0118) — Semi-nonparametric Varying Coefficients Models
- **作者**: Ting Li, Yang Yu, Xiao Wang, J.S. Marron, Hongtu Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在 imaging genetics 背景下，本文提出 semi-nonparametric varying coefficients model，目标是估计和推断随协变量变化的系数函数。采用 kernel machine 方法估计未知变系数函数，并给出 representer theorem；理论贡献包括收敛速率、Bahadur 表示、逐点极限分布和置信区间。在 linear mixed effects model 框架下提出检验统计量，用于检验变系数的显著性并处理 within-subject dependence。核心工具是 RKHS 与 kernel ridge regression 的变体，估计量达到非参数回归的最优 minimax 收敛率。对您有用：这是 semiparametric theory 在纵向/相关数据设定下的具体实例，Bahadur representation 的推导方式可借鉴到您熟悉的 HOIF 理论。
- **关键技术**: `kernel machine method`, `RKHS representer theorem`, `Bahadur representation`, `varying coefficient model`, `linear mixed effects model`, `minimax convergence rate`
- **为什么对您有用**: 直接连接到 semiparametric and nonparametric theory 这一 primary interest，具体是 varying coefficient model 的估计与推断理论。您 very_familiar 的 nonparametric statistics 和 moderately_familiar 的 semiparametric theory 足以攻这篇 paper 的核心证明——特别是 Bahadur representation 和极限分布的推导。follow-up 判定：立即可做，可用 HOIF 视角审视其 higher-order 修正项是否有进一步改进空间。

### 17. [10.5705/ss.202024.0318](https://doi.org/10.5705/ss.202024.0318) · [arXiv](https://arxiv.org/abs/2304.03809) — Estimating Shapley Effects in Big-Data Emulation and Regression Settings using Bayesian Additive Regression Trees
- **作者**: Akira Horiguchi, Matthew T. Pratola
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究非参数回归设定下 Shapley sensitivity indices 的估计问题，目标是在输入维度 p 达数百量级时实现计算可行。核心方法是两阶段策略：先用 Bayesian Additive Regression Trees (BART) 拟合 metamodel，再基于拟合模型计算 Shapley effects，绕过了传统 Monte Carlo 方法在高维时的组合爆炸。理论贡献是证明了该估计量在较大函数类上的 posterior consistency。模拟显示方法在 p=500 维度下仍可计算，四个测试函数表现稳定。对您而言，这是高维非参数估计与计算可行性的一个具体案例，展示了 tree-based method 如何突破维度诅咒。
- **关键技术**: `Shapley effects`, `Bayesian Additive Regression Trees`, `posterior consistency`, `global sensitivity analysis`, `metamodel-based estimation`
- **为什么对您有用**: 本文连接到非参数理论方向，展示了 BART 作为 sieve/series estimator 替代品在高维设定下的理论可证性。您可以用 very_familiar 的 minimax bound 视角审视其 posterior consistency rate 是否紧，或用 moderately_familiar 的 M-estimation 理论分析其估计效率。理论深度有限（仅 consistency，无 rate-optimal 或 efficiency 结果），属于方法导向论文。**中期可做**：若想深入，需先在 moderately_familiar 的 semiparametric theory 上补充 BART 的收敛速率理论。

### 18. [10.5705/ss.202023.0017](https://doi.org/10.5705/ss.202023.0017) · [arXiv](https://arxiv.org/abs/2412.10920) — Multiscale Autoregression on Adaptively Detected Timescales
- **作者**: Rafal Baranowski, Yining Chen, Piotr Fryzlewicz
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出 Adaptive Multiscale AutoRegression (AMAR) 模型，在自回归框架下引入多时间尺度的局部平均作为回归特征，时间尺度的数量和跨度通过变点检测技术从数据中自适应估计。核心估计量是线性回归形式，但设计矩阵由自适应检测的变点决定，形成对高阶 AR 模型的正则化。理论贡献在于允许最长的时间尺度随样本量增长，并建立了估计一致性。实证部分通过模拟和英美失业率的 AMVAR 应用展示方法效果，附带 R 包实现。对您可能有用的是，这是一个将变点检测嵌入估计问题的有趣案例，展示了非参数方法如何通过自适应分段获得可解释性。
- **关键技术**: `change-point detection`, `multiscale local averaging`, `adaptive regularization`, `linear autoregression`, `vector autoregression`
- **为什么对您有用**: 本文连接到 semiparametric theory 方向，展示了如何用数据驱动的分段结构实现自适应正则化。从 technical_arsenal 角度，您可以用 minimax bounds 的工具分析 AMAR 在不同信号强度下的收敛率是否达到最优，或用 M-estimation theory 分析变点估计不确定性如何传播到回归系数。follow-up 判定：中期可做——需先在 moderately_familiar 的 M-estimation theory 上补充 model selection 不确定性传播的理论工具。

### 19. [10.5705/ss.202023.0152](https://doi.org/10.5705/ss.202023.0152) — Functional Joint Models for Imaging Genetic Data
- **作者**: Qingzhi Zhong, Xinyuan Song, Hongtu Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在影像遗传学设定下，目标是建立影像表型响应变量与遗传标记及临床协变量之间的关联模型。作者提出 Functional Joint Modeling (FJM) 框架，包含非线性多元函数型主成分分析 (NMFPCA) 和函数型多指标变系数模型 (FMVCM) 两个模块：前者用未知 link function 提取遗传标记的函数型主成分得分，后者用于识别遗传-影像关联的结构。方法涉及 functional PCA、varying coefficient model、sieve estimation 等非参数/半参数工具，理论性质需看全文确认收敛率与推断结果。对您在 semiparametric theory 和 nonparametric estimation 方向的技术积累有直接对接价值。
- **关键技术**: `functional principal component analysis`, `varying coefficient model`, `multiple-index model`, `sieve estimation`, `nonlinear dimension reduction`
- **为什么对您有用**: 本文属于 semiparametric and nonparametric theory 方向，涉及 functional data 与 varying coefficient model 的估计理论，与您 very_familiar 的 nonparametric statistics 直接相关。技术层面，NMFPCA 中未知 link function 的估计涉及 M-estimation theory（您 moderately_familiar），FMVCM 的收敛率分析可用您熟悉的 minimax bound 工具审视其是否达到最优。follow-up 判定：中期可做——若要深入理论细节（如 FPC scores 的 semiparametric efficiency bound），需先在 semiparametric theory 上进一步巩固。

### 20. [10.5705/ss.202023.0312](https://doi.org/10.5705/ss.202023.0312) · [arXiv](https://arxiv.org/abs/2411.18012) — Bayesian Inference of Spatially Varying Correlations via the Thresholded Correlation Gaussian Process
- **作者**: Moyan Li, Lexin Li, Jian Kang
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 该文提出一种基于阈值相关高斯过程（TCGP）的贝叶斯非参数空间变化相关模型，用于多模态神经影像分析中识别关联显著脑区。TCGP通过高斯过程先验结合阈值函数，确保空间相关函数具有分段平滑、稀疏性和跳跃不连续性，特别适用于受试者数少或信噪比低的场景。理论上证明了模型可识别性、大支撑性质、后验一致性与选择一致性。计算上开发了高效Gibbs采样器及其变体。模拟和人类连接组计划fMRI数据验证了方法有效性。对您而言，该文是nonparametric theory方向的后验一致性证明实例，非常熟悉的nonparametric statistics工具可帮助理解其理论证明。
- **关键技术**: `Gaussian process`, `thresholded correlation`, `Gibbs sampler`, `posterior consistency`, `spatially varying correlation`, `Bayesian nonparametrics`
- **为什么对您有用**: 论文直接涉及非参数贝叶斯理论的后验一致性证明和模型可识别性，属于您primary interest中的nonparametric theory子方向。您非常熟悉的nonparametric statistics工具（如经验过程、覆盖数）可以用于验证其后验一致性的技术细节，立即可做。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.5705/ss.202024.0105](https://doi.org/10.5705/ss.202024.0105) — Efficient Estimation of the Accelerated Failure Time Model with Auxiliary Aggregate Information
- **作者**: Huijuan Ma, Manli Cheng, Yukun Liu, Donglin Zeng, Yong Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究加速失效时间（AFT）模型中整合辅助聚合信息以提高估计效率的问题。假设个体水平数据来自AFT模型，同时可获得公共领域中的总体水平辅助信息（如总体分位数、均值等）。为了突破极大化完全似然函数的计算瓶颈，作者提出一种一步估计量（one-step estimator）：以不利用辅助信息的条件极大似然估计作为初始估计，再通过一步Newton-Raphson校正得到最终估计。理论证明该一步估计量具有相合性与渐近正态性，且渐近方差小于初始估计量，即利用聚合信息带来了效率增益。渐近方差具有闭式表达，可采用plug-in方法简便估计。模拟研究和结肠癌化疗数据分析均验证了该方法的有限样本性能。该工作与半参有效率理论中的debiased/one-step框架一脉相承，对您的效率理论兴趣有直接参考价值。
- **关键技术**: `one-step estimation`, `maximum likelihood with aggregate data`, `accelerated failure time model`, `conditional likelihood`, `plug-in variance estimation`
- **为什么对您有用**: 本文直接连接您的效率理论兴趣（semiparametric efficiency bounds, debiased ML），其一步估计框架与EIF/DML思想类似，可用您非常熟悉的semiparametric theory工具（如efficient influence function）来理解其效率增益的机制。同时，将辅助聚合信息整合到个体水平模型中的思路，在因果推断中的数据融合场景（如外部对照、calibration）也有迁移潜力。**中期可做**：若要深入推广到因果estimand（如ATE在生存结局下的整合），需先在moderately_familiar的identification theory中强化对阴性对照和非参数识别的理解。

## 数理统计 / 假设检验  *(hypothesis_testing, 27 篇)*

### 1. [10.5705/ss.202024.0266](https://doi.org/10.5705/ss.202024.0266) — Center-Outward Ranks and Signs for Testing Conditional Quantile Independence
- **作者**: Kai Xu, Huijun Shi, Daojiang He
- **期刊/来源**: Statistica Sinica
- **机构**: Anhui Normal University
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对多维条件分位数独立性检验问题，提出了基于中心向外秩和符号的非参数渐近分布自由检验方法。该方法将分位数鞅差散度与近年发展的多变量中心向外秩和符号相结合，构造检验统计量。作者利用分位数鞅差散度的退化V型和U型结构，以及中心向外秩的Glivenko-Cantelli强一致性和分布自由性质，推导了零假设下统计量的渐近分布表示，无需bootstrap校准。理论结果表明该检验对所有固定备择假设一致，且在根n邻域内具有非平凡局部功效。此外，检验计算可行且无需矩假设。通过模拟和基因表达数据分析展示了方法的优势。该工作连接了您对假设检验和非参数U型统计量的兴趣，其中心向外秩工具可能拓展到因果推断中的敏感性分析或高维独立性检验。
- **关键技术**: `center-outward ranks and signs`, `quantile martingale difference divergence`, `degenerate V-type and U-type structures`, `distribution-free test`, `Glivenko-Cantelli consistency`
- **为什么对您有用**: （1）直接连接到您的primary interest中的hypothesis testing和非参数理论，且涉及U型统计量的渐近性质，属于您非常熟悉的领域。（2）武器库中very_familiar的nonparametric statistics和high-dimensional asymptotics可以直接用于理解其退化U型结构证明和分布自由性质，并可尝试将中心向外秩方法推广到您关注的proximal CI或IV检验问题中。（3）立即可做：无需先学习新工具，即可评估其理论紧性并探索应用。

### 2. [10.5705/ss.202023.0242](https://doi.org/10.5705/ss.202023.0242) · [arXiv](https://arxiv.org/abs/2301.03126) — Statistical Inference For Ultrahigh Dimensional Location Parameter Based On Spatial Median
- **作者**: Guanghui Cheng, Liuhua Peng, Changliang Zou
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 本研究聚焦于超高位下（维度可随样本量指数增长）基于样本空间位数的位置参数统计推断问题，包括同时置信区间构建、全局检验以及多重检验中的错误发现率控制。核心贡献是推导了样本空间位数的一个新的Bahadur表示，给出了余项在最大范数下的界，并在此表示基础上建立了在高维超矩形类上的高斯近似。提出了一种乘子自助法来近似样本空间位数的分布，且证明该方法在维度指数发散时仍然有效。通过模拟和基因表达微阵列数据分析验证了所提方法的有限样本表现。该论文直接推进了您在高维统计和假设检验方面的兴趣，您熟悉的高维渐近理论可帮助审视其技术细节并考虑扩展。
- **关键技术**: `spatial median`, `Bahadur representation`, `Gaussian approximation over hyperrectangles`, `multiplier bootstrap`, `ultrahigh dimensional inference`
- **为什么对您有用**: (1) 直接对接高维统计和假设检验子方向，处理超高位下基于空间位数的推断问题，是数学统计兴趣的核心应用场景。(2) 您武器库中非常熟悉的高维渐近理论可用于检验其Bahadur表示最大范数界的严格性，并评估高斯近似与自助法的适用条件。(3) 立即可做：该方法的理论基础清晰，可基于现有工具（高维渐近、M估计）进行复现与改进，甚至推广到更一般的M估计量。

### 3. [10.5705/ss.202024.0051](https://doi.org/10.5705/ss.202024.0051) · [arXiv](https://arxiv.org/abs/2402.01381) — Spatial-Sign Based Maxsum Test for High Dimensional Location Parameters
- **作者**: Jixuan Liu, Long Feng, Ping Zhao, Zhaojun Wang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维位置参数检验问题中，目标是检验 H₀: μ = 0，针对重尾分布或存在异常值的情形提出 robust 方法。核心贡献是构造 spatial-sign based max-type 检验统计量，适用于 sparse alternatives，并证明其与 spatial-sign based sum-type 统计量渐近独立。基于此独立性结果，提出 max-sum 组合检验程序，自适应于信号稀疏程度，理论上给出检验统计量的渐近分布。模拟研究表明该方法在重尾分布和不同稀疏度设定下优于传统方法。对您的高维假设检验与 minimax 理论研究有直接参考价值。
- **关键技术**: `spatial-sign transformation`, `max-type test statistic`, `asymptotic independence`, `sparse alternatives`, `high-dimensional hypothesis testing`, `robust testing`
- **为什么对您有用**: 直接连接到您 primary interest 中的 hypothesis testing 与 high-dimensional statistics。您熟悉的 minimax bounds 可以用来分析该 max-sum 检验在不同稀疏度下的最优性；moderately_familiar 的 M-estimation theory 可用于理解 spatial-sign 的 robust 性质。立即可做：用 very_familiar 的 minimax bound 工具验证该方法的 rate 是否 sharp，或推广到更一般的 loss function。

### 4. [10.5705/ss.202023.0385](https://doi.org/10.5705/ss.202023.0385) — Universally Consistent Tests for the Graph of a Gaussian Graphical Model
- **作者**: Thien-Minh Le, Ping-Shou Zhong, Chenlei Leng
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维高斯图模型（GGM）提出全局拟合优度检验，目标是检验预设的图结构是否正确。首先构造直接插件检验统计量，其零分布收敛于Gumbel分布，但该检验对包含真图但不等价的替代假设缺乏辨别力（非一致）。进一步开发了一致性增强检验，通过放大估计中的噪声，使得对所有固定替代假设的检验功效趋于1，即达到普遍一致性。理论部分利用极值渐近推导了检验的零分布与势函数，并在高维稀疏设定下证明了一致性。模拟实验表明两种检验在零假设下均有正确尺寸，且增强检验在替代假设下具有高功效。最后应用于COVID-19数据，展示了该检验在选择图结构以提升估计效率中的实际价值。对您有用：直接连接高维假设检验与极值理论，可与您熟悉的 high-dimensional asymptotics 工具结合，拓展至因果图或多变量非高斯图的全局检验。
- **关键技术**: `Gumbel distribution`, `global goodness-of-fit test`, `noise amplification`, `universal consistency`, `plug-in test statistic`, `Gaussian graphical model`
- **为什么对您有用**: 1. 连接感兴趣的子方向：高维统计中的假设检验（图结构的全局检验），属于数学统计与 hypothesis testing 的前沿问题。2. 您非常熟悉的「high-dimensional asymptotics」可直接用于推导检验统计量的极值渐近分布，而「minimax bounds」可用于分析检验的最优可检测阈值。3. 中期可做：当前武器库中极值理论（Gumbel 吸引域、高维极值）并非非常熟悉，需在该方向上加强（可借助经典极值教材补充）；但您已有的高维渐近基础可快速入门，且可将该方法推广到因果图（DAG）的全局检验，与您的因果推断兴趣直接衔接。

### 5. [10.5705/ss.202024.0022](https://doi.org/10.5705/ss.202024.0022) — Multiple Testing of One-Sided Hypotheses under Unknown Dependence
- **作者**: Seonghun Cho, Youngrae Kim, Johan Lim, Hyungwon Choi, DoHwan Park, Woncheol Jang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 针对未知依赖结构下多重单边假设检验的检验功效损失问题，提出DAB-PFA程序。利用主因子近似（PFA）刻画测试统计量的依赖结构，通过自适应丢弃大或小p值以更准确地估计假发现比例（FDP）。推导了FDP估计量的收敛速率，并在数值模拟中将该程序与Benjamini-Hochberg、Efron（2004）以及Wang-Fan（2017）等方法对比。结果表明在控制FDR的同时显著提升了真正阳性率（TPR）。在卵巢癌蛋白质磷酸化数据的实际分析中进一步验证了方法的实用性。该工作将多重检验与高维因子模型有机结合，与您的假设检验及高维统计（特别是随机矩阵理论在因子模型中的应用）兴趣直接关联。
- **关键技术**: `principal factor approximation`, `multiple testing with unknown dependence`, `adaptive p-value discarding`, `false discovery proportion estimation`, `convergence rate analysis`
- **为什么对您有用**: 本文直接关联到您的主要兴趣之一——假设检验，特别是多重比较中处理未知依赖结构这一核心难题。所使用的PFA方法本质上依赖因子模型与随机矩阵理论（如Marchenko-Pastur谱分布），恰好与您在高维统计和随机矩阵理论方面的very_familiar工具匹配。中期来看，您可以进一步探索该收敛速率是否达到（或可改进至）minimax最优，并将其思想推广至半参数设定下的多重检验问题。

### 6. [10.5705/ss.202024.0037](https://doi.org/10.5705/ss.202024.0037) — Testing High-dimensional White Noise Based On Modified Portmanteau Tests
- **作者**: Zeren Zhou, Min Chen
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 针对高维时间序列的白噪声检验问题，提出一种修正的portmanteau检验，不要求数据独立同分布。该方法通过乘子bootstrap近似检验统计量的临界值，避免了对高维协方差结构的具体假设。提供了原假设下的渐近性质，保证了检验的尺寸控制。模拟和实例表明，该方法对密集备择（dense alternatives）具有较好的检验功效。对于研究者而言，该文直接将高维假设检验与乘子bootstrap结合，在时间序列背景下拓展了传统portmanteau检验的适用性。
- **关键技术**: `modified portmanteau test`, `multiplier bootstrap`, `high-dimensional white noise testing`, `dense alternatives`, `asymptotic null distribution`
- **为什么对您有用**: 本文直接对应研究者「hypothesis testing」和「high-dimensional statistics」的主要兴趣，特别是高维场景下的检验问题。研究者熟悉的「high-dimensional asymptotics」工具可以立即用于分析该检验的minimax最优性或扩展至相关设定（如弱信号检测）。立即可做：研究者可用自身的高维渐近知识复现并优化其临界值近似策略。

### 7. [10.5705/ss.202024.0330](https://doi.org/10.5705/ss.202024.0330) — Weighted Conditional Network Testing for Multiple High-Dimensional Correlated Data Sets
- **作者**: Takwon Kim, Inyoung Kim, Ki-Ahm Lee
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该论文研究高维高斯图模型（GGM）中多个精度矩阵的等同性检验问题，特别考虑给定其他网络条件时的条件差异检验。现有方法无法处理条件性给定且不同的网络结构，因此作者提出了加权条件网络测试（Weighted Conditional Network Testing）方法，利用其他精度矩阵的信息构建检验统计量，并推导了理论性质。通过模拟研究和遗传通路分析，验证了新方法相比现有方法在检测条件差异方面的优势。该工作填补了高维精度矩阵假设检验中的一个空白，提供了明确的统计检验工具。对您而言，这篇论文直接联系到您在高维统计假设检验（特别是协方差/精度矩阵检验）方面的兴趣。
- **关键技术**: `Gaussian graphical models`, `precision matrix estimation`, `hypothesis testing for equality`, `weighted conditional testing`, `high-dimensional inference`
- **为什么对您有用**: 直接连接您对高维统计中假设检验的兴趣（检验精度矩阵等价性），且您在高维渐近和极小极大界方面的功底可立即用于分析该检验的渐近势或拓展至更一般的非参数设定。立即可做：基于您熟悉的high-dimensional asymptotics工具，可推导该检验的minimax最优性。

### 8. [10.5705/ss.202024.0255](https://doi.org/10.5705/ss.202024.0255) — Testing for Treatment Effect in Multitreatment Case
- **作者**: Pier Luigi Conti, Livia De Giovanni, Ayoub Mounim
- **期刊/来源**: Statistica Sinica
- **机构**: Libera Università Internazionale degli Studi Sociali Guido Carli
- 相关性 7/10 · novelty: `minor`
- **摘要**: 本文考虑多处理水平（multi-level treatment）情形下检验处理效应是否存在的问题，目标是在潜在结果框架或纯分布假设下检验各处理组的分布是否相同。作者提出一类基于秩的检验统计量，构造思路类似于经典 Kruskal-Wallis 检验，但推广至更一般的 stochastic dominance 检验场景。理论方面，文章在独立样本、连续分布假设下推导了检验统计量在零假设下的渐近分布（渐近 χ² 型），并讨论了局部备择假设下的功效性质。模拟研究比较了所提方法与 ANOVA、Kruskal-Wallis 等常用方法的第一类错误和功效表现，展示了在非正态、异方差设定下的稳健性。对您而言，这是数学统计中假设检验的经典问题设定，可作为 rank-based test 在因果推断处理效应检验中的方法参考。
- **关键技术**: `rank-based test`, `Kruskal-Wallis extension`, `stochastic dominance testing`, `asymptotic χ² distribution`, `local power analysis`
- **为什么对您有用**: 本文属于假设检验方向，与您 primary interest 中的 mathematical statistics (hypothesis testing) 直接相关，但技术层面是经典秩检验的推广，不涉及高维、半参数效率或因果识别等您更核心的关注点。技术武器库中的 very_familiar 工具（nonparametric statistics）完全覆盖本文内容。follow-up 判断：**立即可做**——如果您需要为多处理水平的因果效应检验构造 rank-based 方法，本文提供了现成的渐近理论框架，但 novelty 有限，属于 minor 级别的方法推广。

### 9. [10.5705/ss.202024.0002](https://doi.org/10.5705/ss.202024.0002) · [arXiv](https://arxiv.org/abs/2203.11461) — A Locally Adaptive Algorithm for Multiple Testing with Network Structure
- **作者**: Ziyi Liang, T. Tony Cai, Wenguang Sun, Yin Xia
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对多重假设检验中如何利用网络结构等复杂辅助信息的问题，提出了一个局部自适应结构学习算法（LASLA）。该方法采用p值加权的策略，通过结构学习从辅助数据中导出数据驱动的权重，以调整不同假设的重要性。在独立性或弱依赖性假设下，理论证明了LASLA能渐近控制错误发现率（FDR），并在辅助信息有效时比传统方法有更高的检验功效。算法核心是通过局部邻域估计和自适应阈值实现信息融合，不依赖辅助数据与主数据的维度或结构匹配。模拟研究验证了方法的稳健性，两个实际数据应用展示了其在网络、空间等多类型辅助信息场景中的有效性。该工作直接关联您对假设检验与多重比较的兴趣，尤其是结合结构化辅助信息进行FDR控制的现代方法。
- **关键技术**: `p-value weighting`, `false discovery rate (FDR) control`, `locally adaptive algorithm`, `structure learning`, `network-structured auxiliary information`, `weak dependence`
- **为什么对您有用**: 本文直接对应您primary interest中的hypothesis testing，特别是多重检验中利用辅助信息（网络/空间）提升功效，这正是您熟悉的high-dimensional asymptotics和nonparametric statistics可处理的问题。使用您武器库中very_familiar的'minimax bounds for estimation problems'和'high-dimensional asymptotics'即可分析其FDR控制的理论紧性，属于立即可做的跟进方向。

### 10. [10.5705/ss.202024.0268](https://doi.org/10.5705/ss.202024.0268) · [arXiv](https://arxiv.org/abs/2004.02328) — Asymptotic Normality of Robust Risk Minimizers
- **作者**: Stanislav Minsker
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究一类稳健风险最小化算法的渐近性质，该类算法用中位数均值估计等稳健均值代理替换经典经验风险中的样本均值。在参数族设定下，作者证明稳健风险最小化器与经典经验风险最小化器具有相同的收敛速率（通常为n^{-1/2}）和渐近方差，从而保持渐近效率。核心机制是采用min-max类型的稳健代理（如中位数均值估计）替代经验平均，使得在仅需要矩条件而非子高斯假设等宽松条件下仍能取得最优收敛。技术工具包括M-估计理论、中位数均值估计的集中不等式以及渐近正态性的标准论证。此外，文中显示基于min-max稳健程序的算法在渐近意义下往往优于直接风险最小化。这些结果对您在假设检验和估计理论中的兴趣有直接意义，尤其是稳健推断的渐近分布理论可供您在高维或非标准设定中构建检验统计量时借鉴。
- **关键技术**: `robust risk minimization`, `median-of-means estimator`, `asymptotic normality`, `M-estimation`, `asymptotic efficiency`, `min-max robust proxy`
- **为什么对您有用**: 本文直接关联您primary interests中的“mathematical statistics & hypothesis testing”，提供了稳健M-估计的渐近正态性理论，可为您在非标准或高维环境下的假设检验设计提供理论基础。您对非参数统计和高维渐近的深厚熟悉（very_familiar）足以迅速消化本文的参数族论证，并思考其向半参数模型的推广。跟进判断：立即可做——无需先补充新工具即可开始阅读和评估细节。

### 11. [10.5705/ss.202025.0157](https://doi.org/10.5705/ss.202025.0157) — Robust Control Experiments for Multivariate Tests with Covariates and Network Information
- **作者**: Shaohua Xu, Yongdao Zhou
- **期刊/来源**: Statistica Sinica
- **机构**: Nankai University
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究 multivariate testing 中的 robust experimental design 问题，目标是在 treatment effects 被 covariates 混杂且 subjects 通过 network 相互连接的设定下，找到最优处理分配方案。作者首次引入 mixed effect model 同时刻画 covariate uncertainty 和 network structure，并基于此提出衡量协方差结构误设导致效率损失的 regret criterion。核心方法是推导 minimax robust experimental schemes，通过最优匹配设计与 robust covariance structure 来抵抗模型误设。理论结果表明所提方案对多种 optimality criteria 具有 resilience，且在模型误设下保持效率。实证部分通过模拟和案例研究验证了方法优于现有 A/B testing 设计。对您在 hypothesis testing 和 minimax theory 方面的兴趣有直接参考价值。
- **关键技术**: `minimax robust design`, `mixed effect model`, `optimal experimental design`, `network-dependent observations`, `covariance misspecification`
- **为什么对您有用**: 连接到 hypothesis testing 中的 experimental design 问题，以及您 very_familiar 的 minimax bounds for estimation problems——本文的 minimax robust scheme 推导可直接用您的 minimax 技术审视其 regret criterion 是否紧。follow-up 判断：立即可做，用 minimax theory 验证其声称的 robustness bound 是否可达最优。

### 12. [10.5705/ss.202024.0391](https://doi.org/10.5705/ss.202024.0391) — Robust Score Tests for Censored Outcomes and Incomplete Covariates Leveraging High-Dimensional Auxiliary Variables
- **作者**: Jiahui Feng, Kin Yau Wong
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对右删失生存结局与部分缺失的感兴趣协变量之间的关联检验问题，在半参数变换模型框架下提出了一种稳健得分检验。利用高维辅助变量对缺失协变量进行插补，并结合多个生存模型的结果以提高检验功效，同时保证对结果模型与协变量模型错误设定的稳健性。在理论上建立了检验在模型错误设定下的渐近有效性，并给出了自适应选择插补模型后的检验性质。通过大量模拟和癌症基因组学数据验证了方法相较于现有方法的优越性。该工作与您对高维统计假设检验和缺失数据下稳健推断的兴趣直接相关，其多模型组合与自适应选择的思路可迁移至因果推断中工具变量或阴性对照的敏感性分析场景。
- **关键技术**: `semiparametric transformation models`, `robust score test`, `multiple imputation with high-dimensional auxiliaries`, `model misspecification robustness`, `adaptive model selection for covariates`
- **为什么对您有用**: 本文核心是高维辅助变量缺失场景下的稳健假设检验，直接对应您Primary Interest中的“hypothesis testing”和“high-dimensional statistics”。您熟悉的“high-dimensional asymptotics”和“estimation theory in causal inference”可用于理解其得分检验的渐近行为；而“M-estimation theory”（moderately_familiar）正是该检验推导的基础工具。这是中期可做的工作：需先在“semiparametric theory”上加强以深入分析变换模型下的得分函数，但现有武器库已覆盖大部分技术环节。

### 13. [10.5705/ss.202024.0344](https://doi.org/10.5705/ss.202024.0344) — Statistical Inference for Functional Data over Multi Dimensional Domain
- **作者**: Qirui Hu, Lijian Yang
- **期刊/来源**: Statistica Sinica
- **机构**: Institute of Statistical Science, Academia Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究多维域函数型数据均值函数的统计推断问题，目标是为均值构建同时置信区域（SCR）并进行假设检验。方法上，作者基于张量积样条对每个个体的轨迹进行非参数估计，得到两步均值估计量，并证明了该估计量是oracally efficient的，即与使用真实不可观测轨迹的不可行估计量渐近不可区分。进一步，利用高斯极值分布及其分位数的精确比较结果，实现了协方差函数的一致估计以及极限最大偏差的精确分位数，从而构造出渐近覆盖概率准确且宽度均匀自适应的同时置信区域。文章还提出了单侧SCR，可用于检验均值函数是否恒高于或低于给定边界。蒙特卡洛模拟验证了理论性质，并在Copernicus海洋卫星数据集上展示了SCR的实用价值。该工作对您有用：它提供了非参数假设检验（同时置信带）的严谨理论框架，您可以用very_familiar的非参数统计和渐近理论知识快速理解，并思考如何将这种高效推断方法迁移到因果推断中的敏感性分析或中介效应检验问题。
- **关键技术**: `tensor product spline`, `oracle efficiency`, `simultaneous confidence regions`, `Gaussian extreme distribution quantile`
- **为什么对您有用**: 这篇论文直接连接到您的primary interest中的hypothesis testing和nonparametric statistics：它开发了多维函数型数据均值函数的推断方法（同时置信带），属于非参数假设检验的经典问题。您的technical arsenal中非常熟悉的nonparametric statistics和high-dimensional asymptotics可以直接用于理解论文的渐近理论；同时，论文中使用的张量积样条与您moderately_familiar的HOIF（高阶影响函数）在利用低维结构处理高维对象方面有类似思想，可作为中期迁移的潜在方向。整体上，论文方法值得您的关注，且目前可立即可读（无需额外工具）。

### 14. [10.5705/ss.202024.0153](https://doi.org/10.5705/ss.202024.0153) — Tests on Dynamic Ranking
- **作者**: Nan Lu, Jian Shi, Xin-Yu Tian, Kai Song
- **期刊/来源**: Statistica Sinica
- **机构**: University of Chinese Academy of Sciences
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究动态Bradley-Terry模型下的统计推断问题，目标包括检验得分函数随时间的变化、检验配对间相似性，以及构建动态排名的置信带。作者首先提出了基于极大似然得分的检验统计量，推导了其在原假设下的渐近分布并证明了检验的相合性。为克服通常supremum形式统计量的保守性，创新性地引入基于符号得分差（signed score difference）的检验框架，使临界值更紧且更易计算。同时，针对动态排名的整体性质，构造了具有统一置信水平的置信带，并以理论保证其覆盖性质。数值模拟验证了有限样本下方法的有效性，并应用到真实数据集上得到了有意义的结论。这篇论文对假设检验的理论框架（尤其是检验统计量的构造与渐近性质）有直接贡献，与您对数学统计中假设检验的兴趣高度吻合，可深入理解其方法设计。
- **关键技术**: `Bradley-Terry model`, `score function variation test`, `pairwise similarity test`, `signed score difference statistics`, `supremum-type statistics`, `confidence band for dynamic ranking`
- **为什么对您有用**: 该论文聚焦您主要兴趣中的假设检验子方向，尤其关注动态模型下检验统计量的渐近理论与有限样本特性。您非常熟悉的非参数统计（经验过程理论）可直接用于剖析其supremum统计量的收敛行为，例如检验Donsker性是否成立。中期可做：若想将该检验框架扩展到高维参数或含协变量的情形，您moderately_familiar的M-estimation理论（需先熟练工具）可支撑推广。整体上，这是一篇立即可读的理论工作，适合作为假设检验新问题的案头参考。

### 15. [10.5705/ss.202024.0035](https://doi.org/10.5705/ss.202024.0035) — An Automatic MDDM-Based Test for Martingale Difference Hypothesis
- **作者**: Chenglong Zhong, Guochang Wang
- **期刊/来源**: Statistica Sinica
- **机构**: Jinan University
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多元时间序列参数条件均值模型下，目标是检验误差项是否为鞅差序列（MDS），关键正则性假设涉及残差的平稳性与高阶矩条件。本文提出一种基于 MDDM（martingale difference divergence matrix）的数据驱动检验，通过自动选择滞后阶数避免了传统 MDDM 检验需预先指定滞后阶数的问题。核心机制是构造一个自适应检验统计量，在原假设下自动收敛到滞后阶数为 1 的情形，同时保持对高阶相依性的检验功效。理论上证明了检验统计量的渐近分布与一致性，方法在有限样本下通过模拟和实证分析验证了有效性。对您在 hypothesis testing 与高维渐近理论方面的兴趣有直接参考价值。
- **关键技术**: `martingale difference divergence matrix (MDDM)`, `data-driven lag order selection`, `asymptotic distribution theory`, `multivariate time series residual testing`, `model adequacy diagnostics`
- **为什么对您有用**: 直接连接到您 primary interest 中的 hypothesis testing 方向，涉及多元时间序列残差的渐近检验理论。您 very_familiar 中的 minimax bounds 和 high-dimensional asymptotics 可用于分析该检验在更高维设定下的理论性质（当前论文聚焦固定维数）。follow-up 判断：**立即可做**——用您熟悉的 nonparametric statistics 和 minimax theory 工具可探索高维 MDDM 检验的 rate-optimal 性质或 power 分析。

### 16. [10.5705/ss.202023.0099](https://doi.org/10.5705/ss.202023.0099) — Reproducible Learning in Large-Scale Multiple Graphical Models
- **作者**: Jia Zhou, Guangming Pan, Zeming Zheng, Changchun Tan
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维异质性数据设定下，本文研究如何从多个网络数据中可复现地恢复总体稀疏连接结构，目标是对图模型边集进行 FDR 控制下的多假设检验。提出 multiple graphical knockoff filter 方法，将 knockoff 框架从单样本推广到多组异质样本情形，通过构造 knockoff 变量并利用 swap 统计量进行变量选择。理论贡献包括证明渐近 FDR 控制以及首次给出 graphical knockoffs 的 power 分析，建立了检测功效与信号强度、样本量、稀疏度之间的显式关系。数值模拟验证了方法在异质性设定下的优势。对您的高维假设检验与多图模型研究有直接参考价值。
- **关键技术**: `knockoff filter`, `false discovery rate control`, `multiple graphical models`, `power analysis`, `high-dimensional variable selection`, `data heterogeneity`
- **为什么对您有用**: 连接到您 primary interest 中的 hypothesis testing 与 high-dimensional statistics，特别是高维多假设检验的 FDR 控制问题。您熟悉的 minimax bounds for estimation 与 high-dimensional asymptotics 可用于审视其 power bound 是否紧、FDR 控制的 rate 是否可达最优。follow-up 判定：立即可做——用您 very_familiar 的高维渐近工具可验证其理论 rate 的 sharpness，或探索更精细的 minimax power bound。

### 17. [10.5705/ss.202024.0249](https://doi.org/10.5705/ss.202024.0249) — Catoni-type Confidence Sequences under Infinite Variance
- **作者**: Guanhua Fang, Sujay Bhatt, Ping Li, Gennady Samorodnitsky
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对数据生成分布的方差不存在或无穷的情境，扩展了Catoni型置信序列方法。主要关注分布仅具有有界p阶矩（p∈(1,2)）的情形，利用Ville不等式推导了Catoni型置信序列，并改进了已有上界结果，显示出比vanilla Dubins-Savage不等式更紧的界。进一步建立了p∈(1,2]时Catoni型置信序列宽度的下界，揭示了单纯依赖Ville不等式技术的统计局限性。为弥合上下界之间的差距，作者采用拼接（stitching）方法构造了更紧的置信序列。新方法可便捷应用于风险控制和参数估计问题。对您而言，该工作直接涉及序列假设检验和重尾分布下的统计推断，与您对数学统计（假设检验）的兴趣高度契合，其中的Catoni估计器与拼接技巧也可用于高维稳健推断。
- **关键技术**: `Catoni-style robust estimator`, `Ville's inequality`, `Dubins-Savage inequality`, `stitching method`, `confidence sequences`, `heavy-tailed distributions`
- **为什么对您有用**: 该论文直接服务于您对假设检验（尤其是序列检验和重尾分布）的兴趣，提供了一种在方差无穷时仍有效的置信序列构造框架。您的武器库中非参数统计和高维渐近理论（very_familiar）可直接用于分析Catoni型估计的重尾行为，拼接方法也可结合您熟悉的M估计理论（moderately_familiar）进行推广。中期可做：若想将这篇方法扩展到更一般的U统计量或高阶影响函数，需先加强moderately_familiar中的HOIF和U统计量理论，但当前论文本身即可作为重尾推理的入门应用。

### 18. [10.5705/ss.202024.0092](https://doi.org/10.5705/ss.202024.0092) — The Method of Limits and Its Application to The Analysis of Count Data in Genome-wide Association Studies
- **作者**: Jiming Jiang, Leqi Xu, Yiliang Zhang, Hongyu Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的统计推断框架——极限法（Method of Limits, MoL），可视为矩法的扩展，专门用于解决全基因组关联研究（GWAS）中计数数据的统计推断问题，克服现有方法（如PQLseq）面临的计算瓶颈。MoL的核心机制是构造一组基于期望的方程，通过解方程得到参数估计，并利用渐近理论建立估计量的相合性和渐近正态性，从而支持假设检验和置信区间构建。具体而言，作者推导了GWAS数据中遗传力（heritability）估计的MoL估计量的渐近分布，并给出了因果SNP比例的一致估计。模拟实验采用平均统计效率（ASE）指标，显示MoL在统计效率和计算效率上均优于PQLseq。实际应用中，作者将MoL应用于英国生物银行（UK Biobank）的计数数据，推断每周香槟和红酒消费的遗传力。该方法的提出丰富了矩估计的变体，并为高维、大规模基因组数据分析提供了一种可行的计算和推断工具。对于您对假设检验和数学统计的兴趣，本文提供了一种新的推断框架，可与您熟悉的高维渐近理论结合，用于评估其在高维基因组设定下的表现。
- **关键技术**: `Method of Limits (MoL)`, `Generalized Method of Moments`, `Asymptotic Normality`, `Heritability Estimation`, `Count Data Analysis`, `Average Statistical Efficiency (ASE)`
- **为什么对您有用**: 本文的方法学贡献直接关联您的主要兴趣——假设检验和数学统计中的新推断框架。MoL推广了矩法，其渐近理论（相合性、正态性）正是您非常熟悉的高维渐近分析可以直接切入的切入点：您可以利用您在高维渐近方面的武器，推导MoL在高维基因组设定下的最小最大效率界或检验功效，或将其与U-统计量结合以处理更复杂的遗传力结构。当前该方法的理论验证主要依赖经典渐近，您的中期可做方向是：先熟悉MoL的方程构造和识别条件（需投入一定阅读），然后利用您的minimax界工具和高维渐近知识，给出高维基因组中MoL的统计与计算权衡分析。

### 19. [10.5705/ss.202025.0427](https://doi.org/10.5705/ss.202025.0427) · [arXiv](https://arxiv.org/abs/2512.09430) — Model-robust Inference for Seamless Ii/iii Trials with Covariate Adaptive Randomization
- **作者**: Kun Yi, Lucy Xia
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究无缝 II/III 期临床试验在协变量自适应随机化（CAR）下的模型稳健推断问题，目标参数为 GLM 框架下的处理效应。核心方法是 Z-estimation，作者推导了估计量的渐近性质，显式刻画了方差如何依赖于具体的随机化方案（如 stratified permuted block、minimization 等）。基于此，提出了调整的 Wald 检验，结合 Dunnett 多重比较和 inverse-χ² 组合方法，保证了整体 I 类错误控制。模拟和实例显示该方法相比传统方法有更好的功效和稳健性。对您在假设检验理论方面的兴趣有直接参考价值。
- **关键技术**: `Z-estimation`, `covariate-adaptive randomization`, `GLM`, `adjusted Wald test`, `Dunnett's procedure`, `inverse-χ² combination`
- **为什么对您有用**: 本文属于临床试验设计中的假设检验问题，涉及有限样本推断和渐近理论，与您 primary interest 中的 mathematical statistics (hypothesis testing) 直接相关。技术层面主要使用 Z-estimation 和经典渐近理论，属于您 very_familiar 的武器库范围。**立即可做**：若想深入，可用 minimax 或 higher-order U-stat 视角审视其方差估计的效率性质，或探索更复杂的 CAR 方案下的理论性质。

### 20. [10.5705/ss.202024.0182](https://doi.org/10.5705/ss.202024.0182) · [arXiv](https://arxiv.org/abs/2412.09794) — Sequential Change Point Detection in High-dimensional Vector Auto-regressive Models
- **作者**: Yuhan Tian, Abolfazl Safikhani
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究在线（顺序）变化点检测问题，针对高维向量自回归模型（VAR）中转移矩阵的突变。利用训练数据通过正则化估计（如Lasso）得到转移矩阵和误差方差的估计，再对新数据批次计算检验统计量。在无变化点条件下，证明了该统计量的渐近正态性，并据此将报警阈值设为标准正态分位数。进一步证明当变化幅度增大时，检验势趋近于1。数值模拟验证了方法的有效性，并应用于S&P 500指数波动分析和脑电图（EEG）癫痫发作检测。本文与您的高维假设检验兴趣直接相关，其中使用的正则化估计和渐近正态性工具与您熟悉的高维渐近理论高度吻合。
- **关键技术**: `high-dimensional VAR`, `regularized estimation`, `sequential change point detection`, `asymptotic normality`, `test statistic for transition matrices`
- **为什么对您有用**: 本文涉及高维时间序列的在线变化点检测，属于假设检验与高维统计的交叉方向。您弹药库中“high-dimensional asymptotics”可直接用于评估其检验统计量收敛性及功率推导；同时，change-point检测思想可与因果推断中的结构稳定性检验结合。从follow-up看，本文核心方法立即可用您的very_familiar工具（高维渐近理论）进行理解和扩展，无需新工具储备。

### 21. [10.5705/ss.202025.0108](https://doi.org/10.5705/ss.202025.0108) · [arXiv](https://arxiv.org/abs/2404.03837) — Inference for Non-stationary Time Series Quantile Regression with Inequality Constraints
- **作者**: Yan Cui, Yuan Sun, Zhou Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究非平稳时间序列线性分位数回归的参数推断问题，其中回归系数受不等式约束。作者证明约束分位数估计量渐近等价于无约束估计量在约束参数空间上的度量投影。利用投影操作的几何不变性，提出了三种推断方法——Wald型、似然比型和基于秩的检验，这些方法在真实参数位于约束边界内部或边界上时均保持一致。模拟研究和电力需求数据集的应用展示了考虑不等式约束的优势。该工作将分位数回归与约束推断相结合，扩展了假设检验在非平稳时间序列中的应用场景。
- **关键技术**: `quantile regression`, `inequality constraints`, `metric projection`, `Wald-type test`, `likelihood ratio test`, `rank-based inference`
- **为什么对您有用**: 本文直接关联到您的 hypothesis testing 兴趣子方向，特别是约束参数空间下的推断问题。您的 nonparametric statistics 和 high-dimensional asymptotics 背景能够用于理解此处渐近等价性的理论证明。该工作提出的几何不变性方法可立即可用您的武器库进行理解和扩展，例如将类似投影技巧应用于因果推断中的约束检验。

### 22. [10.5705/ss.202024.0316](https://doi.org/10.5705/ss.202024.0316) — Bootstrapping Portmanteau Tests for Functional White Noise under Unknown Dependence
- **作者**: Yu Miao, Muyi Li, Wai Keung Li, Xingbai Xu
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一类用于函数型时间序列白噪声检验的portmanteau检验方法，该检验基于平方和形式的经验自相关函数。在Hilbert空间框架下，推导了零假设（序列不相关但不要求独立）下的极限分布性质，但该分布非枢轴，依赖于未知的序列内依赖结构。为解决该问题，作者采用块随机加权bootstrap（blockwise random weighting bootstrap）来近似临界值，并严格证明了其有效性。该方法进一步被推广至函数型自回归模型的残差诊断。通过大量蒙特卡洛模拟和真实数据应用验证了方法的优良有限样本性能，并提供了R包以方便实践。尽管函数型数据并非您的核心方向，但本文所发展的用于处理未知依赖的bootstrap策略，对您在高维或U统计量中处理相关数据的假设检验问题具有方法学参考价值。
- **关键技术**: `blockwise random weighting bootstrap`, `Hilbert space approach`, `portmanteau test`, `functional time series`, `functional autoregressive model`
- **为什么对您有用**: 本文研究函数型时间序列的白噪声检验，属于假设检验领域，与您对hypothesis testing的兴趣直接相关。块随机加权bootstrap处理未知依赖的技术，可考虑迁移至您熟悉的高维U统计量推断中，用于处理相关样本的临界值近似（如聚类数据）。暂不可做：函数型数据理论（如Hilbert空间经验过程）不在您当前武器库中，若欲深入需先补充该领域知识。

### 23. [10.5705/ss.202024.0355](https://doi.org/10.5705/ss.202024.0355) — Change-Point Detection with Local Trend Adjustment
- **作者**: Shengji Jia, Chunming Zhang, Yiming Tang
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 研究问题是在序列存在局部趋势（local trend）时，传统分段常数模型会损害变点检测的准确性，目标是识别多个变点的位置。作者首先提出adaptive Neyman test检验局部趋势是否存在，随后基于部分线性模型（partially linear model）将局部趋势纳入变点检测框架，发展出新的估计与检验方法。方法进一步扩展到多维array data情形，用于识别共同变点。理论性质通过模拟和SNP基因分型数据验证，但论文未给出非参数成分收敛率或检验统计量的极限分布的详细理论分析。对您在假设检验和非参数理论方面的兴趣有直接参考价值。
- **关键技术**: `adaptive Neyman test`, `partially linear model`, `change-point detection`, `local trend adjustment`, `wild binary segmentation`, `SNP genotyping analysis`
- **为什么对您有用**: 直接连接到您primary interest中的假设检验与非参数理论——adaptive Neyman test是经典非参数检验工具，部分线性模型是semiparametric theory的标准设定之一。您very_familiar的nonparametric statistics和minimax bounds可以用来审视该方法的理论性质：检验统计量的power function是否有最优性质、非参数成分的收敛率是否达到minimax rate。follow-up判断：**中期可做**——需要先在moderately_familiar的semiparametric theory上长肌肉，特别是部分线性模型中非参数成分的有效估计理论，才能评估该方法的效率性质并提出改进。

### 24. [10.5705/ss.202022.0397](https://doi.org/10.5705/ss.202022.0397) — Localizing Multivariate CAViaR
- **作者**: Xiu Xu, Yegor Klochkov, Li Chen, Wolfgang Karl Härdle
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究多变量 CAViaR 模型中参数时变性的检测与自适应估计问题，目标是识别风险传染结构的时间变化点。核心方法包括：(1) 构造参数齐性检验统计量，采用数据驱动的临界值确定方法，理论上证明了临界值能达到预设置信水平；(2) 基于检验结果提出自适应估计程序，可自动调整以应对参数的潜在时变性。技术工具涉及分位数回归、局部估计、自助法临界值等。模拟研究表明该方法能有效检测多变量 CAViaR 中的结构变化。实证分析美德金融市场数据，发现美国市场在风险传染中占主导地位，尤其在市场波动期。对您而言，本文的参数齐性检验构造和临界值理论可能为因果推断中的结构变化检测提供方法学参考。
- **关键技术**: `parameter homogeneity test`, `data-driven critical values`, `multivariate CAViaR`, `quantile regression`, `local estimation`, `bootstrap inference`
- **为什么对您有用**: (1) 连接到 hypothesis testing 方向——参数齐性检验的构造与临界值理论属于经典数理统计检验问题；(2) 您的 very_familiar 武器库中 minimax bounds 和 nonparametric statistics 可用于分析该检验的势函数性质和临界值的最优性；(3) **中期可做**：需先在 moderately_familiar 的 M-estimation theory 上补充分位数回归的 M-估计理论，才能深入分析估计量的渐近性质。

### 25. [10.5705/ss.202025.0213](https://doi.org/10.5705/ss.202025.0213) — Explicit Form of the Asymptotic Covariance Matrix of the Normalized Within-Stratum Imbalances Following Minimization with Independent Factors with Application to the Log-Rank Test
- **作者**: Olga M Kuznetsova, Victoria P Johnson, Michael Gekhtman
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 在Pocock和Simon的协变量自适应随机化（最小化）框架下，本文研究了不等层患病率且协变量独立时，按层内不平衡的渐近协方差矩阵的显式形式，此矩阵对后续未分层对数秩检验和稳健得分检验的推断性质至关重要。此前仅已知等患病率情形下的表达式，本文基于大量模拟的实证观察，给出了不等患病率情形下的显式形式。方法上，发现该渐近协方差矩阵正比于一个更简单的直觉概率模型导出的协方差矩阵，比例系数V依赖于最小化中使用的偏置硬币的偏度。理论证明当V≤1时，该协方差矩阵的最大特征值不超过1，从而保证在模型误设定下未分层对数秩检验和稳健得分检验是有效或保守的。通过一个按区域（5个水平）和风险组（4个水平）两个因子使用最小化平衡治疗组的临床试验模拟验证了结果。对您有用：本文揭示了自适应随机化下检验的渐近性质，与您对假设检验和因果推断中治疗分配机制的关注直接相关，尤其是协方差结构对敏感性的分析可能迁移至proximal CI中的负对照设定。
- **关键技术**: `Covariate-adaptive randomization`, `Pocock and Simon's minimization`, `Asymptotic covariance matrix`, `Log-rank test`, `Robust score test`, `Biased coin design`
- **为什么对您有用**: 本文直接关联您primary interest中的“mathematical statistics (hypothesis testing)”，具体涉及自适应随机化后检验的渐近有效性。您very_familiar中的“high-dimensional asymptotics”虽不直接匹配，但可用于理解多分类因子下协方差矩阵的谱行为；而moderately_familiar的“identification theory in causal inference”有助于将该协方差结构与proximal CI中的负对照分析联动。Follow-up粗判：暂不可做——本文使用的偏置硬币设计及最小化概率分析不在当前武器库中（缺少对coin bias参数渐近分析的工具），但作为hypothesis testing与随机化设计的入门阅读很有价值。

### 26. [10.5705/ss.202024.0106](https://doi.org/10.5705/ss.202024.0106) — On Runs Tests for Directional Data and Their Local and Asymptotic Optimality Properties
- **作者**: Maxime Boucher, Christian Francq, Yuichi Goto, Thomas Verdebout
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究方向数据的序列相关性检验问题，目标是在球形数据（如太阳黑子位置）设定下构建具有局部渐近最优性的 runs 检验。作者定义了适用于方向数据的 runs 概念，并基于此构造检验统计量，证明其在局部替代假设下具有局部渐近最优性。理论分析采用 Le Cam 的局部渐近正态性（LAN）框架，推导检验的局部渐近势函数。Monte Carlo 模拟显示有限样本表现良好，太阳黑子数据的实证分析展示了方法的应用价值。对您而言，这是数学统计假设检验框架在非标准数据类型上的具体应用案例。
- **关键技术**: `runs test`, `directional data`, `local asymptotic optimality`, `LAN theory`, `serial correlation test`
- **为什么对您有用**: 本文连接到您 primary interest 中的数学统计假设检验方向，具体是 LAN 框架下的局部渐近最优性理论——这是您 very_familiar 的 minimax bounds 和 nonparametric statistics 工具可直接迁移的领域。方向数据（球面数据）的检验问题在 astrostatistics 中常见，本文也可作为该 secondary interest 的入门阅读。follow-up 判定：**立即可做**——用您熟悉的 LAN 理论和 minimax 框架可以分析该检验的势函数性质或考虑高维方向数据的推广。

### 27. [10.5705/ss.202023.0408](https://doi.org/10.5705/ss.202023.0408) · [arXiv](https://arxiv.org/abs/2307.12325) — A Robust Framework for Graph-Based Two-Sample Tests Using Weights
- **作者**: Yichuan Bai, Lynna Chu
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文关注高维数据下的非参数两样本检验问题，基于图（如K-MST）的检验统计量因对图结构敏感（如hub）导致效能不稳定。作者提出新的鲁棒检验框架，采用边加权策略，利用图的固有特征（如边的度数或结构重要性）构造加权统计量，计算简便且不增加复杂度。推导了该鲁棒统计量的渐近零分布，并验证了有限样本下的准确性。通过模拟实验和芝加哥出租车旅行数据的应用，展示了新方法在多种设定下相比传统图检验的效能提升。本文与您的假设检验兴趣直接相关，尤其在高维非参数检验的稳健性改进上提供了新思路，可用于您熟悉的高维渐近理论分析。
- **关键技术**: `graph-based two-sample tests`, `edge-weighting strategy`, `K-minimum spanning tree (K-MST)`, `asymptotic null distribution`, `nonparametric testing`, `high-dimensional data`
- **为什么对您有用**: 本文针对高维数据下的假设检验问题，属于您primary interest中的hypothesis testing和高维统计。您非常熟悉的nonparametric statistics和high-dimensional asymptotics可直接用于分析本文加权策略的渐近性质，例如检验的minimax最优性或更紧的收敛率。这是立即可做的工作，您目前的技术武器足以对本文方法进行深化或扩展。

## 统计计算 / 算法  *(stat_computing, 6 篇)*

### 1. [10.5705/ss.202024.0281](https://doi.org/10.5705/ss.202024.0281) — Generalized Tensor Regression with Internal Variation Regularization
- **作者**: Yang Bai, Ting Li, Yang Sui
- **期刊/来源**: Statistica Sinica
- **机构**: Shanghai University of Finance and Economics
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维成像数据（如CT）的分段常数空间结构，提出广义张量回归框架，引入内部变异（Internal Variation, IV）正则化。IV正则化显式利用张量数据的分段光滑性，通过惩罚相邻体元间的差异增强估计的平滑性。算法上，开发了高效的IV正则化优化程序，交替更新标量系数和低秩张量系数。理论上，推导了正则化张量系数估计的误差界，证明了估计的一致性。数值模拟表明，该方法在预测精度和变量选择上优于LASSO、Tensor回归等现有方法。应用于慢性鼻窦炎CT数据，识别出上颌窦中最活跃的与诊断相关的子区域。对您（研究者）而言，张量回归中的计算策略（如交替优化）与您非常熟悉的einsum/张量收缩技术直接对应，可探索用张量网络视角加速该优化过程。
- **关键技术**: `Generalized tensor regression`, `Internal variation regularization`, `Piecewise constant imaging`, `Alternating optimization for tensor coefficients`, `Error bounds for regularized estimates`
- **为什么对您有用**: 本文属于高维统计与统计计算交叉，具体连接到您对高维成像数据统计方法及张量计算工具的兴趣。您武器库中非常熟悉的‘computation of higher-order U-statistics (treewidth / tensor contraction / einsum)’可直接用于分析该IV正则化算法的计算复杂度（如张量收缩路径选择或梯度计算成本），据此有望提出更快速的优化变体。**立即可做**：您可立即用einsum库重写其核心张量运算，评估计算效率提升潜力。

### 2. [10.5705/ss.202023.0332](https://doi.org/10.5705/ss.202023.0332) — Likelihood-free Gibbs Sequential Monte Carlo Sampling
- **作者**: Weixuan Zhu, Wei Li, Weining Shen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对似然函数不可处理模型（ABC）在高维参数下遭受维数灾难的问题，提出一种Gibbs顺序蒙特卡洛（Gibbs SMC）方法。该方法在SMC框架内利用Gibbs核逐步更新每个参数，并通过回归调整策略（如局部线性回归）逼近参数的条件分布，从而缓解维度诅咒。理论部分建立了Gibbs核的收敛性质，确保条件分布逼近的误差可控。模拟实验与细胞迁移数据应用表明，与现有ABC-SMC及MCMC方法相比，Gibbs SMC在参数个数增加时仍保持稳定采样效率且精度更高。该方法无需设计复杂的似然近似，仅依赖条件分布的回归调整，显著降低了高维ABC的实现门槛。对于您熟悉统计计算与软件开发的优势，可迅速复现该算法并拓展至因果推断中的模拟推断场景，属于立即可做的方向。
- **关键技术**: `Approximate Bayesian Computation`, `Gibbs Sequential Monte Carlo`, `Gibbs kernel`, `Regression adjustment`, `Conditional distribution approximation`
- **为什么对您有用**: 该论文直接属于您的统计计算（数值方法与算法）兴趣子方向，提出了缓解ABC高维灾难的实用算法并给出理论保证。您非常熟悉的软件开发能力可立刻用于实现该Gibbs SMC框架，并验证其在您关注的因果推断或高维问题中的模拟推断效果。该工作在方法上的新颖性（Gibbs核+SMC）使其值得投入时间阅读全文。

### 3. [10.5705/ss.202024.0222](https://doi.org/10.5705/ss.202024.0222) — Distributed Inference for Tail Risks
- **作者**: Liujun Chen, Deyuan Li, Chen Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究在数据分布式存储（如多台机器）场景下进行尾风险（tail risk）推断的统计方法。极值分析通常用于从稀缺极端事件中外推尾部分布，但大规模数据若分散存储则难以直接分析。作者建立了一套分布式尾经验过程（tail empirical process）和分位数过程（quantile process）的渐近理论工具，利用这些工具可以统一证明大多数极值统计分布式估计量的oracle性质（即与集中式数据下渐近等价）。文中给出多个实例（如分布尾指数、高分位数的分布式估计）展示该工具集的实用性和理论价值。该工作连接了分布式计算与极值统计，为大规模非标准数据的统计推断提供了理论支撑。对您而言，本文涉及的分布式推断理论与您的统计计算（numerical methods, algorithm）兴趣直接相关，且工具可推广至其他分布式多元问题。
- **关键技术**: `Distributed inference`, `Extreme value theory`, `Tail empirical process`, `Quantile process`, `Oracle property`, `Blockwise estimation`
- **为什么对您有用**: 本文直接对接您 primary interest 中的统计计算（分布式算法与渐近理论）方向。技术上，可采用 very_familiar 中的高维渐近和非参数统计工具来理解分布式尾估计量的收敛速率，但极值理论的具体结果（如极值指数、二阶条件）目前不在您的技术武器库中，因此属于中期可做——需先补充极值理论的核心概念和常用渐近方法，然后即可将本文的分布式工具应用到您熟悉的因果推断或高维问题中。

### 4. [10.5705/ss.202024.0145](https://doi.org/10.5705/ss.202024.0145) — Construction of Maximin Distance Latin Hypercube Designs via Good Lattice Point Sets
- **作者**: Xueru Zhang, Dennis K.J. Lin, Wei Zheng
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一种混合方法构建空间填充拉丁超立方体设计，解决传统代数方法仅适用于有限运行次数和因子数、算法搜索在大设计下计算困难的问题。代数部分基于好格点集合和水平置换技术，适用于任意运行次数和灵活的因子数；算法部分进一步扩展至代数方法无法覆盖的因子数。理论分析给出了代数设计的最优性条件，数值研究显示所构设计在Lp距离、列正交性和投影均匀性方面均表现优异。该方法在计算机实验设计中提供了灵活且统计高效的构造工具，对您关注的统计计算算法开发有直接参考价值。
- **关键技术**: `good lattice point sets`, `level permutation`, `space-filling Latin hypercube design`, `maximin distance`, `Lp-distance`, `column orthogonality`
- **为什么对您有用**: 本文属于统计计算中的实验设计方法，直接对应您对统计计算（数值方法与算法）的兴趣。混合代数-搜索策略在构造效率与灵活性上做出了实质改进，其理论最优性分析可与您熟悉的minimax bound思路形成对照。中期可做：将代数构造与高阶U-统计量中的张量收缩成本建模结合（需先在computation of higher-order U-statistics上深化），以评估设计复杂度对仿真分析的影响。

### 5. [10.5705/ss.202024.0029](https://doi.org/10.5705/ss.202024.0029) — Grouped Orthogonal Arrays And Their Construction Methods
- **作者**: Guanzhou Chen, Yuanzhen He, Devon Lin, Fasheng Sun
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在计算机实验设计设定下，研究当因子可划分为若干不相交组且组间无交互作用（即响应函数具有可加结构）时的最优设计问题。作者提出 grouped orthogonal arrays (GOA)，在组内保持正交阵列性质的同时，允许组间更灵活的 run size 配置。核心构造方法基于有限域上的线性组合与差分方案，可生成任意素数幂水平数的 GOA，并给出具体的算法步骤和大量表格化设计供实践使用。理论结果表明，GOA 相比现有方法在组内投影性质上更优，且能覆盖更多 run size 组合。对您可能有用：若涉及高维因果推断或非参估计中的设计问题，GOA 提供了一种在已知可加结构下降低实验成本的工具。
- **关键技术**: `orthogonal arrays`, `space-filling design`, `finite field construction`, `additive model structure`, `projection properties`
- **为什么对您有用**: 本文属于实验设计/统计计算方向，与您 primary interest 中的 semiparametric theory 存在间接联系：当模型具有可加结构时，GOA 可用于构造更高效的实验设计，从而改善非参/半参估计的收敛性质。技术层面，本文的构造方法基于有限域和组合设计，不涉及您熟悉的 minimax theory 或 efficiency bound 工具，属于相对独立的 combinatorial design 领域。follow-up 判断：**暂不可做**——核心组合设计工具不在武器库中，且与您当前主攻方向（因果推断效率理论、高维统计、U-statistics）距离较远，除非未来有具体的实验设计需求。

### 6. [10.5705/ss.202024.0191](https://doi.org/10.5705/ss.202024.0191) — Characterizing and Comparing Order-of-Addition Orthogonal Arrays
- **作者**: Shin-Fu Tsai
- **期刊/来源**: Statistica Sinica
- **机构**: National Taiwan University
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本研究针对 order-of-addition（OofA）实验设计中正交数组的比较与选择问题，提出了一组数值指标 centralized generalized wordlength pattern (CGWP)。首先，在考虑 pairwise order 矩阵的传递性后，论证了 J-characteristics 在 OofA 设计中的适用性。随后基于容量-全设计下 pairwise order 矩阵的归一化 J-characteristics 的平方差之和定义了 CGWP，可视为两水平正交数组 generalized wordlength pattern 的自然推广。进一步推导了函数关系的简化形式，大幅降低了计算成本，使得在资源约束下从候选设计中选取最优 OofA 正交数组成为可行。从现有目录中识别出若干经济样本量下的最优 OofA 正交数组，为实际实验设计提供了指导。该工作对统计计算（算法简化）兴趣有直接帮助：其计算简化策略可以借助兵器库中的 software development 技能快速实现，中期需补强实验设计理论即可开展应用。
- **关键技术**: `order-of-addition orthogonal arrays`, `centralized generalized wordlength pattern`, `J-characteristics`, `pairwise order matrix`, `computational simplification`
- **为什么对您有用**: 本文提出的 CGWP 及其计算简化策略针对统计计算子方向（算法简化）有直接联系，利用兵器库中的 software development 擅长项可快速实现该指标。中期可做：需先熟悉正交数组理论（目前不在武器库中），但可借助 nonparametric statistics 基础理解其设计框架；暂不可做部分：缺乏实验设计领域的深入知识，需针对性补课。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.5705/ss.202024.0099](https://doi.org/10.5705/ss.202024.0099) — Probit Time-to-Event Regression for Misclassified Group Testing Data
- **作者**: Lijun Fang, Tao Hu, Shuwei Li, Lianming Wang, Christopher S. McMahan, Joshua M. Tebbs
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对分组检测数据中的时间事件结局提出了一种新的回归分析方法。在分组检测（group testing）中，多个个体的标本混合后检测一次，得到的是当前状态数据（current status data），即只知道截至检测时刻是否感染，但不知精确时间。作者采用半参数probit模型替代比例风险模型，对潜在感染时间进行建模。通过对数单调样条近似非参数 nuisance 函数，并采用 sieve 极大似然估计和 EM 算法进行参数估计。该方法能够处理检测错误分类（misclassification）问题，即在分组检测中可能存在的假阳性/假阴性。模拟和实例分析表明该方法在有限样本下表现良好。对您而言，这是一篇流行病学中分组检测数据分析的应用类论文，展示了半参数建模和计算技巧在处理复杂数据结构时的实际应用，可为您在流行病学数据建模方面提供参考。
- **关键技术**: `sieve maximum likelihood estimation`, `logarithmic monotone splines`, `EM algorithm`, `probit model`, `current status data`, `group testing`
- **为什么对您有用**: 本文属于流行病学应用论文（secondary interest），面向分组检测数据这一实际公共卫生场景。研究者若对流行病学中的统计建模感兴趣，本文展示了半参数sieve方法与EM算法在非标准数据结构（当前状态数据）中的应用，可视为入门读物。武器库中`非参数统计`和`M估计理论`可直接用于理解其理论框架；若要跟进，可考虑将类似方法扩展到因果推断中的mediation分析（当前状态数据的因果估计），但需先熟悉`识别理论`（moderately_familiar）。中期可做：先熟悉`半参数理论`中的sieve方法。

## 其他  *(other, 9 篇)*

### 1. [10.5705/ss.202025.0022](https://doi.org/10.5705/ss.202025.0022) — Simple Inferential Analyses of Big Gwas Data
- **作者**: Jiming Jiang, Leqi Xu, Jiangshan Zhang, Hongyu Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该论文针对大规模GWAS数据（如生物银行规模）中的方差分量估计与推断问题，提出了简单闭式估计量，避免了BOLT-REML等迭代算法的计算负担。作者推导了遗传力与环境误差方差的显式表达式，并建立了估计量的相合性和渐近正态性。基于渐近分布，进一步构建了方差分量的置信区间和假设检验方法。与BOLT-REML相比，新方法可进行推断分析且计算显著更快；与另一种矩匹配方法mmhe相比，统计性能相当且计算优势明显。理论结果主要基于SNP独立的假设，但模拟和实际数据验证表明方法在该假设偏离时仍稳健。该工作为遗传学中方差分量的统计推断提供了一套计算高效、理论完备的工具。
- **关键技术**: `closed-form estimator`, `variance components`, `heritability estimation`, `asymptotic normality`, `confidence interval`, `hypothesis testing`
- **为什么对您有用**: 该论文直接针对假设检验和统计推断这一主要兴趣，提供了方差分量的渐近推断方法，且计算简单（避免迭代），与研究者对统计计算的兴趣（计算优势）相关。研究者可凭借对高维渐近理论（very_familiar）的熟悉轻松理解其理论框架，并进一步探究独立SNP假设放松下的稳健性（立即可做）。

### 2. [10.5705/ss.202024.0195](https://doi.org/10.5705/ss.202024.0195) — Maximizing Area Under the Receiver Operating Characteristic Curve for Biomarker Combination
- **作者**: Yuxuan Chen, Yijian Huang
- **期刊/来源**: Statistica Sinica
- **机构**: Emory University
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多生物标志物组合用于疾病诊断的背景下，目标是最优化线性组合的接收者操作特征曲线下面积（AUC）。现有方法面临两个挑战：AUC 对组合系数的尺度不变性导致计算和渐近研究困难，且经验 AUC 是分段常数，标准梯度方法不适用。本文提出一种新的经验 AUC 直接最大化方法，避免使用核平滑从而消除带宽敏感问题。给出了点估计和方差估计的计算高效算法，利用组合系数的归一化处理解决尺度不变性。模拟和实际数据分析表明方法在统计性能和计算速度上的优势。由于 AUC 本质上是一个两样本 U-statistic，本文对 U-statistic 优化的处理对高阶 U-statistic 的计算和优化问题有参考价值。
- **关键技术**: `empirical AUC maximization`, `scale-invariant optimization`, `piecewise-constant objective`, `U-statistic optimization`, `variance estimation`
- **为什么对您有用**: 本文连接 researcher 在 higher-order U-statistics 方向的兴趣：AUC 作为两样本 U-statistic，其优化面临目标函数分段常数的计算障碍，恰好是 researcher 熟悉的 U-statistic 计算问题（如 treewidth 视角）可以分析的场景。可以使用非常熟悉项 'computation of higher-order U-statistics (treewidth / tensor contraction / einsum)' 中的图论代价模型分析该算法或提出更一般的 U-statistic 优化框架。立即可做：无需预先学习新工具，可直接利用对 U-statistic 投影和计算的理解来评估该方法或扩展至更高阶 U-statistic。

### 3. [10.5705/ss.202024.0109](https://doi.org/10.5705/ss.202024.0109) · [arXiv](https://arxiv.org/abs/2402.12803) — Joint Mean and Correlation Regression Models for Multivariate Data
- **作者**: Zhi Yang Tho, Francis K. C. Hui, Tao Zou
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种联合均值和相关性回归模型，用于多元离散和（半）连续响应数据。该模型同时将每个响应的均值对协变量回归，并将响应间的相关性对相似性或距离度量回归。通过构建一组联合估计方程来估计均值回归系数和相关性回归参数。在响应数量可趋于无穷的一般高维设定下，证明了联合估计量的一致性和渐近正态性，且均值回归系数的收敛速率因异质性而不同。开发了迭代估计算法以确保参数估计落在约束参数空间内。模拟研究展示了方法在点估计和推断上的良好有限样本性能，并应用于苏格兰38种步甲甲虫的计数数据。该工作对于研究者的高维渐近和M估计理论提供了可借鉴的建模思路。
- **关键技术**: `estimating equations`, `joint regression model`, `high-dimensional asymptotics`, `iterative estimation`, `constrained parameter space`
- **为什么对您有用**: 本文在高维响应（p → ∞）设定下基于估计方程构造联合均值-相关模型，直接关联研究者对高维统计和M估计理论的兴趣。研究者可用 moderately_familiar 的 M 估计理论切入，分析该估计方程的渐近效率与正则条件。目前该工具尚需加强，属于中期可做的拓展方向。

### 4. [10.5705/ss.202024.0224](https://doi.org/10.5705/ss.202024.0224) — General Sliced Factorial Designs for Online Experiments
- **作者**: Zijian Han, Dongying Wang, Fasheng Sun, Peter Chien
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究在线实验中的切片因子设计，目标是在多个平台（如不同设备或操作系统）上高效设计因子实验。作者提供了一般化的切片因子设计理论，并提出切片广义字长模式（sliced generalized wordlength pattern）用于构造任意数量平台下的最优设计。方法基于平行平面设计（parallel flat design）的特性，将切片设计扩展到一般情形。论文在补充材料中给出了若干构造好的设计表，便于实际应用。虽然实验设计是因果推断中随机化实验的基础，但本文侧重因子结构的代数构造而非因果识别或估计问题。对您而言，可作为背景了解，但核心方法与您的主要兴趣（因果推断、高维统计、高效理论等）关联较弱。
- **关键技术**: `sliced factorial designs`, `parallel flat designs`, `generalized wordlength pattern`, `optimal design construction`
- **为什么对您有用**: 本文属于实验设计分支，与您对因果推断中在线实验的随机化设计有间接关联，但焦点是因子结构的构造而非因果识别或效率理论。您的技术武器库中非常熟悉的非参数统计、高维渐近等工具难以直接应用于此问题；核心机器（组合设计）不在武器库中，属于暂不可做类型。若需深入在线实验的因果推断，建议转向该领域的识别与估计方法文献，而非本设计构造论文。

### 5. [10.5705/ss.202024.0100](https://doi.org/10.5705/ss.202024.0100) — The Population and Personalized Areas Under the Receiving Operating Characteristic Curve
- **作者**: Haben Michael, Lu Tian
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在聚类数据背景下，将经典的受试者工作特征曲线下面积（AUC）推广为两种形式：总体AUC（Population AUC）和个体化AUC（Personalized AUC）。首先通过具体模型和可视化阐释两种AUC在何种情形下趋同或发散，并用定量结果刻画其差异。文章进一步提出联合估计与统计推断程序，包括基于广义估计方程（GEE）和bootstrap的方法，并在模拟中评估了有限样本表现。最后将所提方法应用于城市警务行为数据集，展示了实际分析流程。对您而言，这篇论文提供了处理聚类、纵向或重复测量数据中判别性能度量的框架，其推断思路可直接迁移到您在流行病学数据集（如诊断试验或风险预测模型验证）中的评估任务。
- **关键技术**: `Clustered ROC curve`, `Area under the ROC curve (AUC)`, `Generalized estimating equations (GEE)`, `Nonparametric estimation`, `Joint inference`
- **为什么对您有用**: 本文直接面向您secondary interest中的流行病学应用，特别是在聚类或纵向数据下的判别性能评估。您非常熟悉的非参数统计和M-estimation理论（very_familiar中的非参数统计与M-estimation theory）正好可以用来审视其GEE推断的渐近性质，并进一步扩展到更复杂的因果推断设定（如处理聚类时估计条件AUC）。该论文的方法和模拟已经成熟，您可立即动手将其对比或复现于您手头的流行病学数据集，属于立即可做的follow-up方向。

### 6. [10.5705/ss.202023.0401](https://doi.org/10.5705/ss.202023.0401) — Two-level Isomorphic Foldovers Designs
- **作者**: Chunyan Wang, Dennis K. J. Lin
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的非正则两水平正交阵列设计——同构折叠设计（IFD），它由初始设计的若干折叠重复构成。研究目标是为IFD建立一般理论，并给出在G-aberration（或G2-aberration）准则下构造最优IFD的算法。与传统的单一平展设计相比，IFD结构能以更高效的方式找到优良设计，特别当初始设计为非正则时优势更明显。同时，IFD具有并行平展结构，在理解与分析上比许多其他非正则设计更简便。文章还证明了一些已有设计可视为IFD的特殊情形。对实验设计领域而言，IFD提供了一个兼具灵活性与解析简洁性的新工具。对您而言，本文属于经典实验设计方法，与您的因果推断中的随机实验（如因子设计）有间接联系，但核心问题与您的武器库交集较小，适合作为备选参考。
- **关键技术**: `orthogonal arrays`, `foldover designs`, `G-aberration criterion`, `isomorphic designs`, `parallel flats structure`
- **为什么对您有用**: 本文与因果推断中的实验设计（如随机化析因实验）有背景联系，但方法本身侧重组合构造而非因果识别。您的武器库中非参数统计和高维渐近难以直接切入，当前暂不可深入，除非后续需要涉及复杂实验方案的结构优化。

### 7. [10.5705/ss.202024.0418](https://doi.org/10.5705/ss.202024.0418) · [arXiv](https://arxiv.org/abs/2412.09872) — Tail Risk Equivalent Level Transition And Its Application for Estimating Extreme Lp-Quantiles
- **作者**: Qingzhao Zhong, Yanxi Hou
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出了一种新的尾部风险度量方法——Tail Risk Equivalent Level Transition (TRELT)，用于刻画在两个不同Lp分位数之间转换时尾部风险的变化。TRELT受Li and Wang (2023)的PELVE启发，但专门针对尾部风险设计，具有存在性、唯一性和渐近性质的理论保证。作者进一步基于TRELT开发了极端Lp分位数的推断方法，这本质上是极值理论中的一种新外推技术。模拟和真实数据分析展示了方法在风险管理中的有效性和实用性。Lp分位数作为VaR和expectile的推广，在金融风控中已有广泛关注，而本文聚焦于尾部风险的动态转换，属于极值推断的一个细化方向。对于您而言，该文的方法学核心是渐近推断和假设检验在极值设定下的应用，但技术工具箱（极值理论）并非您的核心擅长领域，需要先补一些极值渐近基础才能直接跟进。
- **关键技术**: `Lp-quantiles`, `Tail risk transition`, `Extreme value theory`, `Asymptotic inference`, `Risk measurement`
- **为什么对您有用**: 本文属于极值统计与假设检验的交叉应用，与您的“数学统计与假设检验”兴趣有一定重叠。您的技术武器库中“非参数统计”和“高维渐近”不能直接套用极值外推框架，但渐近推断的通用工具（如似然比检验、正态近似）仍有参考价值。中期可做：若想在此方向工作，需先熟悉极值理论中的二项式点过程模型与极值指数估计（目前武器库不具备），因此暂不可直接动手。

### 8. [10.5705/ss.202023.0426](https://doi.org/10.5705/ss.202023.0426) · [arXiv](https://arxiv.org/abs/2309.06428) — Tail Gini Functional Under Asymptotic Independence
- **作者**: Zhaowen Wang, Liujun Chen, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究渐近独立条件下尾部Gini泛函的估计问题，用于测度系统性风险的尾部变异性。首先在中间水平（intermediate level）估计尾部Gini，然后利用极值理论外推至极端尾部。建立了中间估计量和极端估计量的渐近正态性。模拟显示该方法在偏差和方差方面均表现良好。应用于港交所个股周损失数据，给出有意义的尾部风险度量结果。本文方法虽非您直接研究方向，但其极值估计框架和渐近理论可启发因果推断中极端处理效应或经济金融数据集的应用。
- **关键技术**: `Extreme value theory`, `Tail Gini functional`, `Asymptotic independence`, `Extrapolation`, `Asymptotic normality`
- **为什么对您有用**: 本文属于金融风险管理中的极端统计方法，与您次要兴趣中经济理论（金融数据集应用）弱相关。您武器库中高维渐近理论和极值工具可理解其渐近结果，但本文未涉及因果推断或U统计量，立即可做程度低，属于暂不可做（缺少极值外推的领域知识）。

### 9. [10.5705/ss.202025.0061](https://doi.org/10.5705/ss.202025.0061) — Minimum Aberration Fractional Factorial Designs under Baseline Parameterization
- **作者**: Xinxin Xia, Fasheng Sun, Chunyan Wang
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究了基线参数化下s水平部分因子设计的一般理论（s≥3），将此前仅适用于两水平设计的结论推广至多水平情形。在基线参数化下，作者证明了正交阵列在所有设计中保持D-和G-最优性，同时在平衡设计中达到A-最优性。建立了正交参数化下的词长模式与基线参数化下K-值序列之间的关联。进一步提出了构造最小混杂基线设计的一般方法，通过理论推导和实例验证了方法的有效性。该工作为多水平因子设计的筛选实验提供了系统性的最优性理论。对您的统计计算或算法兴趣而言，设计构造中的组合优化算法可能有一定参考意义，但整体偏离您的主要研究方向。
- **关键技术**: `minimum aberration baseline designs`, `orthogonal arrays`, `wordlength pattern`, `K-value sequence`, `D-optimality`, `G-optimality`
- **为什么对您有用**: 本文属于实验设计领域，与您的主要兴趣（因果推断、高维统计、U-统计等）无直接重叠。您的统计计算武器库中不包含实验设计的组合优化方法，因此当前暂不可做。若未来考虑涉及试验设计的研究方向，可作为入门阅读，但短期内无需深读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

