# 因果推断 · 专题 B：半参数、策略优化与机器学习

> JCSDS 2026 · Causal Inference B — Semiparametrics, Policy Optimization & ML · [返回会议总览](index.md)

- 含 **4 个分会场 · 17 场报告**（已检索到对应论文 10 场）

---

## Statistical Perspectives on Causal Inference and Modern Machine Learning

*7 月 11 日（周六） · 15:30-17:10 · Hongfeng Meeting Room*  
*主办 Bernoulli Society for Mathematical Statistics and Probability · 组织 Xingqiu Zhao（The Hong Kong Polytechnic University） · 主持 Xingqiu Zhao（The Hong Kong Polytechnic University）*

### 1. A Bayesian Nonparametric Framework for Private, Fair, and Balanced Tabular Data Synthesis

**讲者**：Linglong Kong（University of Alberta）

**对应论文**：A Bayesian Nonparametric Framework for Private, Fair, and Balanced Tabular Data Synthesis · [论文/主页](https://openreview.net/forum?id=j0czDrEnFc)

<details><summary>摘要（原文）</summary>

A fundamental challenge in data synthesis is protecting the fairness and privacy of the individual, particularly in data-scarce environments where underrepresented groups are at risk of further marginalization by reproducing the biases inherent in the data modeling process. We introduce a privacy- and fairness-aware for a class of generative models, which fuses the conditional generator within the framework of Bayesian nonparametric learning (BNPL). This conditional structure imposes fairness constraints in our generative model by minimizing the mutual information between generated outcomes and protected attributes. Unlike existing methods that primarily focus on sensitive binary-valued attributes, our framework extends seamlessly to non-binary attributes. Moreover, our method provides a systematic solution to class imbalance, ensuring adequate representation of underrepresented protected groups. Our proposed approach offers a scalable, privacy-preserving framework for ethical and equitable data generation, which we demonstrate by theoretical guarantees and extensive experiments on sensitive empirical examples.

</details>

## 问题
表格数据合成需同时满足**隐私保护**、**群体公平**与**类别均衡**，且保持数据效用，这在数据稀缺、弱势群体样本不足时尤其困难——朴素生成模型会复制并放大数据中的偏见。

## 核心方法
作者（Fazeli-Asl、Zhang、Kong、Jiang，ICLR 2026）提出把**条件生成器**（如 VAECGAN 的 generator/decoder 结构）嵌入**贝叶斯非参数学习（BNPL）**框架，形成 Private-Fair-Balanced 三位一体方案：
- **公平性**：以 BNP 为基础构造互信息正则项，最小化生成结果与受保护属性间的互信息 $I(\hat{Y};A)$，且可处理**非二值**敏感属性；
- **隐私**：分全局与局部两层，全局用 **Dirichlet 过程机制**注入随机性，局部用 **copula 型基测度**针对连续/类别特征定制隐私预算并保留特征依赖；
- **均衡**：用基于 Dirichlet 过程的 KL 估计量系统纠正类别不平衡。

## 与已有工作关系
现有方法多用 GAN/VAE，易 mode collapse，且通常只处理二值敏感属性、难以在单一框架统一公平与隐私。本文以 BNPL 贝叶斯非参数视角统一三目标，并把公平扩展到非二值属性，是对差分隐私表格合成与公平生成模型的推进。

## 贡献
提供可扩展、带理论保证的隐私-公平-均衡合成框架，Dirichlet 过程浓度参数刻画隐私-效用权衡，实验在 Adult 等敏感数据集上验证了公平与鲁棒性提升。


### 2. Identification and Inference with Many Weak Interaction Moments

**讲者**：Zhonghua Liu（Columbia University）

**对应论文**：Constructive Instrumental Variable Identification and Inference with Many Weak Interaction Moments · [arXiv:2504.13565](https://arxiv.org/abs/2504.13565)

<details><summary>摘要（原文）</summary>

Instrumental variable methods are widely used for causal inference, but identification becomes especially challenging when instruments are weak and potentially invalid. These challenges are particularly pronounced in Mendelian randomization, where genetic variants serve as instruments and violations of exclusion restriction or independence assumptions are common. We propose MAGIC, a constructive and assumption-lean framework that achieves identification even when all candidate instruments may be invalid. The method exploits pairwise and higher-order interactions among mutually independent instruments to construct moment conditions orthogonal to both unmeasured confounding and direct effects under a linear structural model. The resulting estimation problem involves many potentially weak interaction moments with unknown nuisance parameters. We develop a semiparametric generalized method of moments estimator and introduce a global Neyman orthogonality condition to ensure robustness of both the moment function and its derivative to nuisance estimation under many weak moment asymptotics. We establish consistency and asymptotic normality when the number of moments diverges with sample size and characterize the semiparametric efficiency bound under fixed dimension. Simulations and an application to UK Biobank data illustrate the method.

</details>

## 问题
工具变量（IV）因果推断在工具**弱**且**可能无效**时识别极为困难。孟德尔随机化（MR）尤为典型：以基因变异为工具，排他性约束与独立性假设常被违反（水平多效性）。当**所有**候选工具都可能无效时，如何仍能识别因果效应？

## 核心方法
作者（Zhang、Yao、Liu、Sun）提出 **MAGIC** 框架，构造性、assumption-lean：在线性结构模型下，利用互相独立工具间的**成对及高阶交互**构造与未测混杂、直接效应都正交的矩条件。由此得到含**大量潜在弱交互矩**、带未知冗余参数的估计问题。方法上：
- 构建**半参数 GMM** 估计量；
- 引入**全局 Neyman 正交性**，保证矩函数及其导数在 many-weak-moment 渐近下对冗余参数估计具鲁棒性；
- 在矩数量随样本量发散时证明相合性与渐近正态，并刻画固定维度下的半参数效率界。

## 与已有工作关系
相较于要求多数/部分工具有效的稳健 MR 方法（如众数、中位数、sisVIVE），MAGIC 允许**全部**工具无效；相较传统 many-weak-moment 的 GMM 理论，本文的创新在于用交互矩构造正交条件并引入全局 Neyman 正交性处理冗余参数。

## 贡献
给出全工具无效下的构造性识别、半参数效率界与稳健推断，并在 UK Biobank 实证与模拟中验证。


### 3. Double Machine Learning of Continuous Treatment Effects with General Instrumental Variables

**讲者**：Yifan Cui（Zhejiang University）

**对应论文**：Double Machine Learning of Continuous Treatment Effects with General Instrumental Variables · [arXiv:2601.01471](https://arxiv.org/abs/2601.01471)

<details><summary>摘要（原文）</summary>

Estimating causal effects of continuous treatments is a common problem in practice, for example, in studying average dose-response functions. Classical analyses typically assume that all confounders are fully observed, whereas in real-world applications, unmeasured confounding often persists. In this article, we propose a novel framework for the identification of average dose-response functions using instrumental variables, thereby mitigating bias induced by unobserved confounders. We introduce the concept of a uniform regular weighting function and consider covering the treatment space with a finite collection of open sets. On each of these sets, such a weighting function exists, allowing us to identify the average dose-response function locally within the corresponding region. For estimation, we propose an augmented inverse probability weighted score for continuous treatments with instrumental variables under a debiased machine learning framework, and provide practical guidance to adaptively establish regular weighting functions from the data. We further establish the asymptotic properties when the average dose-response function is estimated via kernel regression or empirical risk minimization. Finally, we conduct both simulation and empirical studies to assess the finite-sample performance of the proposed methods.

</details>

## 问题
估计**连续处理**的因果效应（平均剂量-反应函数 ADRF）是常见需求，但经典方法假定混杂全部可观测；现实中**未测混杂**普遍存在，导致偏倚。如何在连续处理下用工具变量（IV）克服未测混杂，识别并推断 ADRF？

## 核心方法
作者（Chen、Zhang、Cui）提出基于**一般工具变量**的连续处理 ADRF 识别-估计框架：
- 引入**一致正则加权函数（uniform regular weighting function）**概念，用有限个开集**覆盖**处理空间，在每个开集上存在这样的加权函数，从而在对应局部区域识别 ADRF；
- 估计上提出连续处理下带 IV 的**增广逆概率加权（AIPW）得分**，纳入**去偏机器学习（DML）**框架，并给出从数据**自适应**构造正则加权函数的实践指导；
- 当 ADRF 用**核回归**或**经验风险最小化**估计时建立渐近性质。

## 与已有工作关系
延续 Chernozhukov 等 DML/去偏思想与连续处理 AIPW（如 Kennedy 的剂量-反应），但突破点在于**引入 IV 处理未测混杂**并给出连续处理下的局部覆盖识别策略——相比二值处理 IV（LATE）与需全混杂可观测的连续处理法更一般。

## 贡献
提出连续处理+一般 IV 的识别理论（正则加权函数与开集覆盖）、DML 下的 AIPW 估计量与渐近理论，并以模拟和实证验证有限样本表现。


### 4. A General Framework for Fair and Robust Regression

**讲者**：Wen Su（City University of Hong Kong）

**对应论文**：A General Framework for Fair and Robust Regression · [论文/主页](https://icml.cc/virtual/2026/poster/64084)

<details><summary>摘要（原文）</summary>

Fair regression methods typically rely on squared error loss, making them fragile under heavy tailed noise. We propose a general framework for robust regression under demographic parity (DP) that applies to a wide class of M-estimators, including Cauchy, Huber, least absolute deviation, quantile, and Tukey losses. We propose an optimal fair transformation that guarantees DP while achieving the minimum population risk among all rank preserving fair predictors. We also establish convergence rates for the resulting estimators. To balance fairness and predictive accuracy, we develop an interpolation scheme whose risk decreases while unfairness grows linearly with the interpolation parameter. The proposed framework can be further extended to conditional DP to account for legitimate covariates. Extensive simulation studies and real data applications show clear improvements over existing fair regression approaches in both robustness and predictive performance.

</details>

## 问题
现有公平回归多以**平方误差损失**为基础，在**重尾噪声**下脆弱。如何构造既满足**人口均等（demographic parity, DP）**又对异常值/重尾**稳健**的回归框架？

## 核心方法
作者（Wenhai Cui、Xiaoting Ji、Wen Su、Xingqiu Zhao，ICML 2026）提出适用于一大类 **M-估计**（Cauchy、Huber、最小绝对偏差 LAD、分位数、Tukey 等损失）的稳健公平回归通用框架：
- 提出**最优公平变换（optimal fair transformation）**，在保证 DP 的同时，于所有**保序（rank-preserving）**公平预测器中达到**最小总体风险**；
- 建立所得估计量的**收敛速率**；
- 为权衡公平与预测精度，设计**插值方案**：随插值参数变化，风险下降而不公平度**线性**增长，给出可解释的权衡曲线；
- 进一步扩展到**条件 DP**，以容纳合法协变量（legitimate covariates）。

## 与已有工作关系
相较基于平方损失的公平回归（如 Chzhen 等最优传输/Wasserstein 重心公平预测），本文把公平变换推广到通用 M-估计损失族，兼顾**稳健性**；保序最优变换思想与最优传输公平表示一脉相承，但强调重尾稳健与显式风险-公平权衡。

## 贡献
给出稳健公平回归的统一框架、最优公平变换、收敛速率、风险-不公平插值权衡及条件 DP 扩展，模拟与实证均优于现有公平回归方法。


## Statistical Methods in Causal Inference and Policy Optimization

*7 月 13 日（周一） · 08:30-10:10 · Libo Room*  
*主办 Chinese Association for Applied Statistics · 组织 Liuquan Sun（Chinese Academy of Sciences） · 主持 Liuquan Sun（Chinese Academy of Sciences）*

### 1. Deconfounding Sequential Treatment Effects through Overlapping Treatment Histories

**讲者**：Hui Huang（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到确证的公开论文（arXiv/期刊），以下基于题目与讲者（人大统计学院、生物统计与纵向数据方向）方向合理推断。

**问题**：在纵向观测数据中估计时变处理的序贯因果效应时，核心障碍是**时变混杂**——既往协变量既受前期处理影响、又影响后续处理与结局。标准边际结构模型（MSM）依赖“序贯可忽略性/无未测混杂”假设，一旦存在未观测混杂即产生偏倚。

**核心方法**：本报告提出利用**重叠的处理历史（overlapping treatment histories）**来去混杂。直觉是：不同个体虽处理路径各异，但在若干时点上共享相同的处理历史片段，这些“重叠”提供了可比子群，可在给定历史下识别处理分配的局部变异，从而分离未观测混杂的影响。方法上很可能构造基于历史匹配/分层的加权或估计方程，形式上估计如 $E[Y(\bar a)]$ 或对比 $E[Y(\bar a)]-E[Y(\bar a')]$ 的序贯效应，并借重叠结构放松单纯的序贯可忽略性。

**与已有工作关系**：延续 Robins 的 g-formula、MSM 与结构嵌套模型传统，与近年“序贯去混杂/时变去混杂器（temporal deconfounder）”文献相呼应，但强调用观测到的重叠历史而非潜变量代理来处理混杂。

**贡献（推断）**：给出重叠历史下的识别条件、构造相合且渐近正态的估计量并给出方差估计，通过模拟与真实纵向数据验证对未测/残余混杂的稳健性。


### 2. Optimal Treatment Allocations Accounting for Population Differences

**讲者**：Wei Zhang（Chinese Academy of Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到确证的公开论文（arXiv/期刊，检索受网络限制无法核验），以下基于题目与讲者（中科院数学与系统科学研究院，因果推断/最优处理规则方向）合理推断。

**问题**：从源人群（如随机试验或某观测研究）学到的最优个体化处理规则/分配方案，直接迁移到结构不同的目标人群时并非最优——因为协变量分布、处理效应的条件结构在两个人群间存在差异（covariate shift 与效应异质性）。报告聚焦在**存在人群差异**下如何构造对目标人群最优的处理分配。

**核心方法**：很可能在潜在结果框架下，将目标定为最大化目标人群的期望结局 $E_{\text{target}}[Y(d(X))]$，其中 $d(\cdot)$ 为处理分配规则。方法上预期结合密度比/重要性加权做人群间迁移（transportability），以及双稳健/半参数高效估计（AIPW 型估计方程）来构造价值函数估计并求解最优规则，可能进一步纳入资源/预算约束下的分配。给出规则的相合性、价值函数的渐近分布与效率界。

**与已有工作关系**：融合 individualized treatment rule/policy learning（Qian-Murphy、Zhao 等）与因果可迁移性（transportability, Bareinboim-Pearl；Dahabreh 等）两条线，强调跨人群泛化而非仅在训练人群内最优。

**贡献（推断）**：在人群差异下建立最优分配的识别与高效估计理论，给出双稳健估计与推断，并以模拟及真实数据展示相较“直接迁移”规则的价值提升。


### 3. A Nonparametric Potential Outcomes Framework for Bidirectional Causal Inference

**讲者**：Guoyu Zhang（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到确证的公开论文（arXiv/期刊，检索受网络限制无法核验），以下基于题目与讲者（北京大学，因果推断方向）合理推断。

**问题**：传统潜在结果框架预设单向的“因→果”（$A\to Y$），但许多系统中两个变量互为因果、存在反馈（如供需、生理指标间的相互调节）。报告旨在为**双向因果（bidirectional causality）**建立一个**非参数的潜在结果框架**，刻画“$A$ 对 $Y$”与“$Y$ 对 $A$”两个方向的因果效应并加以识别。

**核心方法**：预期为每个方向定义各自的潜在结果（如 $Y(a)$ 与 $A(y)$），在均衡/反馈机制下给出结构性假设，用以在不设定参数形式的前提下识别双向效应。方法上可能借助工具型变量、外生冲击或对称性/不动点（均衡）条件来打破双向内生性，并给出非参数识别的充分条件与相应的（半参数高效）估计量。区别于线性联立方程/结构方程模型，本框架强调分布层面的非参数识别与潜在结果语义。

**与已有工作关系**：连接联立方程内生性、Mendelian randomization 中的双向 MR，以及近年双向近端因果推断（bidirectional proximal causal inference）文献，但主张在 Neyman-Rubin 潜在结果语言下给出更一般的非参数处理。

**贡献（推断）**：形式化双向因果的潜在结果定义、给出非参数识别条件与估计/推断方法，并以模拟与实证说明区分两个因果方向的可行性。


### 4. General Sieve Learning-Based Specification Analysis with Missing Survey Data

**讲者**：Puying Zhao（Yunnan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到确证的公开论文（arXiv/期刊，检索受网络限制无法核验），以下基于题目与讲者（云南大学，缺失数据/估计方程/复杂抽样方向，曾著“Augmented two-step estimating equations with nuisance functionals and complex survey data”等）合理推断。

**问题**：在含**缺失（尤其可能不可忽略/MNAR）的调查数据**中做模型设定检验（specification analysis）——即检验工作模型（回归函数、缺失机制或倾向得分模型）是否正确设定——既受缺失偏倚影响，又受复杂抽样设计（分层、聚类、不等概率）干扰，标准拟合优度/设定检验不再有效。

**核心方法**：提出**一般化筛法（general sieve）学习**框架：用筛（如样条、级数、神经网络等基展开）非参数逼近未知的冗余函数（nuisance functionals，如条件均值、缺失倾向），在此基础上构造对模型设定的检验统计量。方法很可能结合估计方程/矩条件与筛估计，给出在缺失与抽样权重下相合的设定检验，并推导其（近似 $\chi^2$ 或基于经验过程的）渐近分布及重抽样校准。

**与已有工作关系**：延续作者关于带冗余泛函的增广两步估计方程与复杂抽样、非可忽略缺失下的经验似然/估计方程工作，将筛法半/非参数逼近引入设定检验，弥补参数化设定检验对模型误设敏感的不足。

**贡献（推断）**：建立缺失调查数据下基于一般筛学习的设定检验理论（相合性、渐近分布、功效），给出实现与重抽样方案，并以模拟与真实调查数据验证其对模型误设的检出能力与对复杂设计的稳健性。


## Some Recent Topics in Causal Inference

*7 月 13 日（周一） · 10:30-12:10 · Baihua Meeting Room*  
*组织 Rajarshi Mukherjee（Harvard T.H. Chan School of Public Health） · 主持 Rajarshi Mukherjee（Harvard T.H. Chan School of Public Health）*

### 1. Data-Automated Policy Learning for Nonlinear Welfare

**讲者**：Zheng Zhang（Renmin University of China）

**对应论文**：Data-Automated Policy Learning for Nonlinear Welfare · [arXiv:2606.01659](https://arxiv.org/abs/2606.01659)

<details><summary>摘要（原文）</summary>

This paper explores policy learning from observational data, focusing on a nonlinear welfare criterion in a binary treatment setting. The nonlinear criterion is inspired by scenarios where policymakers prioritize specific population segments. We model this criterion using a utility function that encompasses potential outcomes and intermediate parameters, with the latter capturing higher moments of the outcome distributions. When formulated in the context of observational data, both the intermediate parameters and the welfare criterion depend on the propensity score, which we estimate using machine-learning techniques. To address bias in machine learning estimates, we introduce a novel reweighting-based debiasing approach that offers a promising alternative to traditional orthogonality-based methods. To tackle the complexities of infinite-dimensional policy spaces, we employ sieve approximations and $K$-fold cross-validation for model selection, thereby fully automating the policy-learning process. Despite these complexities, we demonstrate that both the welfare regret and the average welfare regret of our proposed policy learning method satisfy an oracle inequality, thereby providing theoretical guarantees on the performance of the estimated policy relative to the best possible policy. This finding extends the existing results from linear to nonlinear welfare criteria, from finite-dimensional to infinite-dimensional policy spaces, and from a known propensity score to a machine-learned one.

</details>

**问题**：传统政策学习（treatment allocation）多以线性福利准则（如平均处理效应加权和）为目标，但现实中决策者常关心特定人群分层、公平性或对结果分布高阶矩的偏好，这需要**非线性福利准则**。本文（Ai、Wu、Zhang）研究在二值处理、观测数据下，如何学习最大化非线性福利的个体化处理规则。

**核心方法**：以效用函数刻画福利，涉及潜在结果与捕捉结果分布高阶矩的**中间参数（intermediate parameters）**。由于观测数据中间参数与福利准则均依赖倾向得分，作者用机器学习估计倾向得分，并提出一种新颖的**基于重加权（reweighting-based）的去偏方法**，作为传统正交化（Neyman orthogonality）路径的替代。针对无穷维策略空间，采用 sieve 逼近与 $K$ 折交叉验证做模型选择，实现策略学习的**全自动化（data-automated）**。

**与已有工作关系**：延续 Kitagawa-Tetenov、Athey-Wager 的经验福利最大化（EWM）传统，但把结果从三方面推广——由线性福利推广到非线性福利；由有限维策略类推广到无穷维；由已知倾向得分推广到机器学习估计的倾向得分。

**贡献**：证明所提方法的福利遗憾（welfare regret）与平均福利遗憾均满足 oracle 不等式，给出相对最优策略的理论保证；重加权去偏为处理非线性/复杂泛函提供了新的技术工具。


### 2. Optimal Nuisance Function Tuning for Estimating a Doubly Robust Functional under Proportional Asymptotics

**讲者**：Zixiao Wang（Harvard University）

**对应论文**：Optimal Nuisance Function Tuning for Estimating a Doubly Robust Functional under Proportional Asymptotics · [arXiv:2509.25536](https://arxiv.org/abs/2509.25536)

<details><summary>摘要（原文）</summary>

In this paper, we explore the asymptotically optimal tuning parameter choice in ridge regression for estimating nuisance functions of a statistical functional that has recently gained prominence in conditional independence testing and causal inference. Given a sample of size $n$, we study estimators of the Expected Conditional Covariance (ECC) between variables $Y$ and $A$ given a high-dimensional covariate $X \in \mathbb{R}^p$. Under linear regression models for $Y$ and $A$ on $X$ and the proportional asymptotic regime $p/n \to c \in (0, \infty)$, we evaluate three existing ECC estimators and two sample splitting strategies for estimating the required nuisance functions. Since no consistent estimator of the nuisance functions exists in the proportional asymptotic regime without imposing further structure on the problem, we first derive debiased versions of the ECC estimators that utilize the ridge regression nuisance function estimators. We show that our bias correction strategy yields $\sqrt{n}$-consistent estimators of the ECC across different sample splitting strategies and estimator choices. We then derive the asymptotic variances of these debiased estimators to illustrate the nuanced interplay between the sample splitting strategy, estimator choice, and tuning parameters of the nuisance function estimators for optimally estimating the ECC. Our analysis reveals that prediction-optimal tuning parameters (i.e., those that optimally estimate the nuisance functions) may not lead to the lowest asymptotic variance of the ECC estimator -- thereby demonstrating the need to be careful in selecting tuning parameters based on the final goal of inference. Finally, we verify our theoretical results through extensive numerical experiments.

</details>

**问题**：在因果推断与条件独立性检验中，期望条件协方差（Expected Conditional Covariance, ECC）$\mathbb{E}[\mathrm{Cov}(Y,A\mid X)]$ 是一个典型的**双稳健泛函**，其估计依赖两个 nuisance 函数（$Y$ 与 $A$ 关于高维 $X$ 的回归）。本文（McGrath、D. Mukherjee、R. Mukherjee、Wang）关注一个被以往半参数理论忽视的现实设定：**比例渐近（proportional asymptotics）** $p/n\to c\in(0,\infty)$，此时 nuisance 函数根本无法一致估计，经典的 $\sqrt{n}$ 半参数效率理论失效。

**核心方法**：在 $Y,A$ 关于 $X$ 均为线性模型的假设下，以**岭回归（ridge）**估计 nuisance 函数，考察三种 ECC 估计量与两种样本分割策略。作者先推导各估计量的**去偏（debiased）版本**做偏差校正，证明在不同组合下均可得到 $\sqrt{n}$-一致估计；进而给出去偏估计量的渐近方差，刻画样本分割策略、估计量选择与岭调参三者之间的微妙互动。

**与已有工作关系**：延续 Robins 等双稳健/high-order influence function 及 undersmoothing、sample splitting（如 2212.14857）的路线，但把分析放到 $p\propto n$ 的比例渐近框架，与 2408.06103（GLM 的矩方法推断）互补。

**贡献**：核心发现是**预测最优（prediction-optimal）的调参未必给出 ECC 估计的最小渐近方差**——即最优估计 nuisance 与最优推断目标泛函所需调参不一致，提醒实践者应按最终推断目标而非预测精度选择调参，并以数值实验验证。


### 3. Where Best to Intervene?

**讲者**：Caleb Miles（Columbia University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**（未检索到对应公开论文/arXiv 预印本，以下基于题目与讲者 Caleb Miles 在 Columbia 生物统计系的研究方向推断。）**

**问题**：题目「Where Best to Intervene?」直指公共卫生与因果推断中的核心决策问题——当存在**多个可干预的变量或路径**（如多个中间变量、风险因素、暴露层级）时，把有限资源投向何处能最大程度改善结果？这不同于「是否干预」，而是**干预靶点的比较与排序**。

**核心方法（推断）**：结合 Miles 一贯的半参数因果推断风格，估计量很可能建立在**随机/可修改干预（stochastic / modified treatment policies）与路径特异效应（path-specific effects）**之上。思路应是为每个候选干预定义一个反事实分布或干预后福利（如把某风险因素分布右移/设限后的期望结果），比较各靶点对应的干预效应大小，并给出识别条件、影响函数与双稳健、$\sqrt{n}$-一致的高效估计量，允许用机器学习估计 nuisance 函数。可能涉及在互相依赖的多中介结构下对靶点效应的可识别性与分解，以及对「最优靶点」这一被选参数的推断（选择后推断/optimizer 问题）。

**与已有工作关系（推断）**：延续 VanderWeele、Díaz、Miles 本人关于中介分析、interventional (in)direct effects（如其 2203.00245）与健康公平因果分解（decomposition to identify intervention targets）的脉络，把「分解归因」推进为「面向决策的靶点比较」。

**贡献（推断）**：为「在何处干预最有效」提供统一的因果估计目标与稳健推断框架，服务于干预设计与卫生资源配置。具体方法与结论以现场报告及后续论文为准。


## Advances in Causal Inference and Machine Learning for Complex Data

*7 月 12 日（周日） · 15:30-17:10 · Qingyan Boardroom*  
*主持 Yuqian Zhang（Renmin University of China）*

### 1. Design and Analysis for Valid Causal Inference with Network-Dependent Data

**讲者**：Zhejia Dong（Brown University）

**对应论文**：Disentangling network dependence among multiple variables · [arXiv:2506.20974](https://arxiv.org/abs/2506.20974)

<details><summary>摘要（原文）</summary>

When two variables depend on the same or similar underlying network, their shared network dependence structure can lead to spurious associations. While statistical associations between two variables sampled from interconnected subjects are a common inferential goal across various fields, little research has focused on how to disentangle shared dependence for valid statistical inference. We revisit two different approaches from distinct fields that may address shared network dependence: the pre-whitening approach, commonly used in time series analysis to remove the shared temporal dependence, and the network autocorrelation model, widely used in network analysis often to examine or account for autocorrelation of the outcome variable. We demonstrate how each approach implicitly entails assumptions about how a variable of interest propagates among nodes via network ties given the network structure. We further propose adaptations of existing pre-whitening methods to the network setting by explicitly reflecting underlying assumptions about level of interaction that induce network dependence, while accounting for its unique complexities. Simulation studies demonstrate the effectiveness of the two approaches in reducing spurious associations due to shared network dependence when their respective assumptions hold, but also show sensitivity to assumption violations.

</details>

该报告与 Dong、Zigler、Lee 的 arXiv:2506.20974 属同一研究脉络（报告标题更宽泛，聚焦网络依赖数据下的有效因果推断，论文侧重其中的核心难点：共享网络依赖）。**问题**：当研究单元通过同一张（或相似）网络相连时，两变量各自的网络依赖会诱发虚假关联，破坏经典独立同分布假设下推断的有效性。如何在设计与分析阶段剥离这种「共享依赖」以获得有效的 $p$ 值与区间是核心挑战。**核心方法**：作者比较并改造两条来自不同领域的思路——时间序列中的预白化（pre-whitening），通过对残差去相关消除共享结构；以及网络分析中的网络自相关模型 $y=\rho W y+X\beta+\varepsilon$，用邻接权重 $W$ 刻画结点间传播。文章揭示二者都隐含了「变量如何沿网络边传播」的假设，并按「交互层级」显式建模，将预白化推广到网络场景。**与已有工作关系**：区别于 Hudgens–Halloran 干扰框架与 Ogburn 等网络因果工作对单一结果依赖的处理，本文强调多变量共享依赖的识别与去除。**贡献**：给出两类方法的假设几何与适用边界，模拟显示假设成立时能显著降低虚假关联，但对误设敏感，凸显正确指定依赖结构的重要性。


### 2. Efficient Inference of Regional Treatment Effects in Multi-Regional Clinical Trials

**讲者**：Kunhai Qing（East China Normal University）

**对应论文**：Consistency Assessment of Regional Treatment Effect for Multi-Regional Clinical Trials in the Presence of Covariate Shift · [arXiv:2602.07468](https://arxiv.org/abs/2602.07468)

<details><summary>摘要（原文）</summary>

Multi-Regional Clinical Trials (MRCTs) play a central role in the development of new therapies by enabling the simultaneous evaluation of drug efficacy and safety across diverse global populations. Assessing the consistency of treatment effects across regions is a fundamental aspect of MRCTs. Existing methods typically focus on region-specific marginal treatment effects. However, when treatment effect heterogeneity arises due to effect-modifying baseline covariates, distributional differences in these covariates can lead to erroneous conclusions. In this paper, we explicitly account for this phenomenon in the consistency assessment by considering the conditional average treatment effect. We propose a two-step assessment strategy that complements existing methods and mitigates the impact of treatment effect heterogeneity. Results from numerical studies demonstrate the effectiveness of the proposed approach.

</details>

报告与 Kunhai Qing（ECNU，合作者含 Jin Xu、Menggang Yu）的 MRCT 系列工作一脉相承，最贴近的公开论文为 arXiv:2602.07468（报告题「Efficient Inference of Regional Treatment Effects」框架更强调估计与推断效率，可能为该系列的较新稿件）。**问题**：多区域临床试验（MRCT）需同时在全球多地评估药效并判断各区域疗效是否与整体一致。传统方法只比较区域「边际」治疗效应，但当疗效受基线协变量调节、而各区域协变量分布不同（covariate shift）时，边际比较会得出误导性结论。**核心方法**：转而以「条件平均治疗效应」$\tau(x)=E[Y(1)-Y(0)\mid X=x]$ 为标的，提出两步式一致性评估：先在共同协变量分布上标准化各区域效应以剥离分布差异，再进行区域一致性判定；配合半参数高效估计与样本量计算。**与已有工作关系**：相较 MHLW(2007)、Japan 桥接指南及固定/随机效应一致性准则只处理边际效应，本文显式纳入协变量偏移与效应异质性，属于将 CATE 与迁移/泛化思想引入 MRCT 监管评估。**贡献**：给出对异质性稳健的评估策略、数值验证其有效性，为区域效应的有效推断提供了可操作框架。


### 3. Quadruply Robust Methods for Causal Mediation Analysis

**讲者**：Zhen Qi（Renmin University of China）

**对应论文**：Quadruply robust methods for causal mediation analysis · [arXiv:2601.22592](https://arxiv.org/abs/2601.22592)

<details><summary>摘要（原文）</summary>

Estimating natural effects is a core task in causal mediation analysis. Existing triply robust (TR) frameworks (Tchetgen Tchetgen & Shpitser 2012) and their extensions have been developed to estimate the natural effects. In this work, we introduce a new quadruply robust (QR) framework that enlarges the model class for unbiased identification. We study two modeling strategies. The first is a nonparametric modeling approach, under which we propose a general QR estimator that supports the use of machine learning methods for nuisance estimation. We also study high-dimensional settings, where the dimensions of covariates and mediators may both be large. In these settings, we adopt a parametric modeling strategy and develop a model quadruply robust (MQR) estimator to limit the impact of model misspecification. Simulation studies and a real data application demonstrate the finite-sample performance of the proposed methods.

</details>

**问题**：因果中介分析的核心是估计自然（直接/间接）效应 $E[Y(a,M(a'))]$。经典识别依赖对结果、中介密度、处理机制等多个讨厌参数（nuisance）建模，一旦模型误设即产生偏差。Tchetgen Tchetgen & Shpitser (2012) 提出的三重稳健（TR）估计仅需三组模型之一正确即可一致，但其可容许的模型组合仍受限。**核心方法**：本文提出「四重稳健」（QR）框架，扩大了可保证无偏识别的模型类。给出两条路线：(1) 非参数建模下的通用 QR 估计量，允许用机器学习估计讨厌参数并借助交叉拟合保持 $\sqrt{n}$ 推断；(2) 面向协变量与中介同时高维的情形，采用参数化策略构造「模型四重稳健」（MQR）估计量，降低误设影响。**与已有工作关系**：直接推广 TR 中介框架及其 EIF/多重稳健文献，把稳健性从三重提升到四重，并接入现代 ML 与高维正则化。**贡献**：更宽的模型稳健性、支持 ML 讨厌参数、覆盖高维中介，模拟与实证验证有限样本表现。作者 Zhen Qi 与 Yuqian Zhang（均属人民大学统计方向）合作，与本会场 t6 同源团队。


### 4. Stabilized Debiased Machine Learning

**讲者**：Ruicong Yao（Ghent University, Belgium）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与本报告完全对应的公开论文（arXiv 上 Ruicong Yao 名下多为随机森林/模型树等题目，同名混淆；同题演讲见于剑桥 talks.cam.ac.uk，讲者为根特大学 Ruicong Yao，与 Stijn Vansteelandt 组相关），以下基于题目与该组研究方向推断。**问题**：Debiased/Double Machine Learning（DML, Chernozhukov 等 2018）用 Neyman 正交得分 + 交叉拟合，使目标参数（如 ATE）估计对讨厌参数的机器学习误差一阶不敏感。但当倾向得分接近 0/1（弱重叠）或讨厌估计不稳定时，逆概率权重方差爆炸、有限样本偏差与波动大，正态近似失效。**核心方法（推断）**：'Stabilized' DML 应对该不稳定性，思路可能包括：对权重做稳定化/截断或等渗校准（isotonic calibration），构造对讨厌函数扰动更稳健的稳定影响函数；或采用免样本分裂的稳定估计量（借鉴 stable estimators 无需 cross-fitting 的结果），在保持正交性的同时降低方差、改进覆盖率。**与已有工作关系**：延续 DML、目标最小损失估计（TMLE）、重叠权重与稳定 IPW 校准文献，聚焦「稳定性」这一有限样本痛点。**贡献（推断）**：给出在弱重叠/高维讨厌下更稳健的 DML 估计与推断，理论上保持 $\sqrt{n}$ 正态性，经验上改善区间覆盖。


### 5. Sparse Deep Integrative Latent Factor Regression for Supervised Multi-Modal Data Analysis

**讲者**：Jing Yu（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（讲者 Jing Yu 为常见姓名，arXiv/学术库中未定位到上海财经大学此人对应稿件），以下基于题目与多模态统计学习方向推断。**问题**：多模态数据（如影像、组学、文本/表格）从不同视角刻画同一批样本，各模态既有共享的潜在结构又有模态特异信息；在有监督（supervised）目标下，如何同时整合多模态、提取低维潜因子并保持可解释的稀疏性，是核心难点。**核心方法（推断）**：'Sparse Deep Integrative Latent Factor Regression' 很可能构建一个联合潜因子模型：设各模态 $X_m\approx f_m(Z)$，用共享潜因子 $Z$（含共享+模态特异分量）驱动，$f_m$ 由深度网络实现非线性载荷，并对载荷/因子施加稀疏正则（如 $\ell_1$、group-lasso）以选变量、提升可解释性；同时以 $Y=g(Z)+\varepsilon$ 的监督头引导因子朝预测目标对齐（supervised factor / 类偏最小二乘）。训练上联合优化重构损失与监督损失。**与已有工作关系**：融合 JIVE、DIABLO/多组学整合、（深度）CCA、监督自编码器与稀疏因子回归等线索，将线性整合因子模型深度化并加入稀疏与监督。**贡献（推断）**：给出可解释、可做变量选择的深度多模态监督降维框架，兼顾整合与预测，适用于生物医学等多模态场景。


### 6. Balancing Utility and Cost in Dynamic Treatment Regimes

**讲者**：Yuqian Zhang（Renmin University of China）

**对应论文**：Balancing utility and cost in dynamic treatment regimes · [arXiv:2507.17360](https://arxiv.org/abs/2507.17360)

<details><summary>摘要（原文）</summary>

Dynamic treatment regimes (DTRs) are personalized, adaptive strategies designed to guide the sequential allocation of treatments based on individual characteristics over time. Before each treatment assignment, covariate information is collected to refine treatment decisions and enhance their effectiveness. The more information we gather, the more precise our decisions can be. However, this also leads to higher costs during the data collection phase. In this work, we propose a balanced Q-learning method that strikes a balance between the utility of the DTR and the costs associated with both treatment assignment and covariate assessment. The performance of the proposed method is demonstrated through extensive numerical studies, including simulations and a real-data application to the MIMIC-III database.

</details>

**问题**：动态治疗方案（DTR）根据个体随时间变化的特征序贯分配治疗。每次决策前采集协变量能提升决策精度，但采集本身有成本（检验、检查、时间），治疗分配也有成本。既往 DTR 研究多只最大化临床效用（utility），忽视了「为获取信息而付出的成本」，导致方案在实践中过度检测、不经济。**核心方法**：提出「平衡 Q-learning」，将效用与两类成本——治疗分配成本、协变量评估成本——同时纳入目标，学习在收益与代价间权衡的最优策略。等价于在标准 Q 函数上引入成本惩罚项，序贯地决定「是否采集某协变量」与「采取何种治疗」，从而内生地实现信息价值与采集开销的取舍。**与已有工作关系**：延续 Murphy 的 DTR/Q-learning 与成本效益 DTR（如 cost-effective Q-learning）文献，但把成本从单纯治疗成本扩展到「信息采集成本」，接近带测量成本的序贯决策/主动特征获取。**贡献**：给出兼顾效用与成本的平衡 Q-learning 估计与算法，经模拟及 MIMIC-III 真实重症监护数据验证，能在小幅牺牲效用下显著降低成本。作者 Kai Chen、Yuqian Zhang（人民大学），与本会场 t3 同源团队。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)