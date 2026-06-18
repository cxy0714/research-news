# Statistica Sinica  ·  2026-06-19

- 共 101 篇 · Statistica Sinica

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Statistica Sinica 这一期体量庞大（101篇），覆盖领域广泛，但主线清晰。按主题可大致聚为四条路线：**因果识别与推断**（约10篇，涉及群随机试验共形推断、无效工具变量、代理变量、双重稳健最优治疗方案、主分层、协变量平衡等）、**半参数/非参数建模与效率**（约15篇，聚焦核岭回归泛函、条件密度、分位数回归效率界、缺失数据稳健推断、函数型数据等）、**高维统计与随机矩阵**（约15篇，包括相关矩阵结构检验、重尾max统计量、因子数确定、迁移学习、稀疏回归等）、**假设检验与变点检测**（约10篇，涵盖序贯多重检验、变化平面子组检验、协方差变点、条件尾部独立检验等）。此外，还有若干计算方法、实验设计及经济应用类论文。

因果推断主线贯穿多类设定。**Efficient Estimation of ATE with Proxies** 将bridge function与ATE联合估计，通过递增矩条件达到半参效率界，直接回应了proximal inference中两步估计的效率损失。**Semiparametric Causal Discovery with Invalid Instruments** 在部分线性结构方程下构建替代有效IV，同时处理因果发现与效应估计，放宽了传统IV线性与有效性假设。**Doubly Robust Optimal ITR in Semi-supervised Framework** 利用单指标核平滑插补无标签数据，获得立方根收敛的DR估计量，并给出非标准渐近分布。**Conformal Causal Inference for CRT** 提供有限样本预测区间，不依赖渐近近似，为群水平效应提供了model-robust工具。**Semiparametric Principal Stratification Beyond Monotonicity** 以无边际条件优势比为敏感性参数，导出双稳健与去偏ML估计，放松了单调性假设。这几篇共同推进了因果推断中识别假设的松弛与效率的改进。

半参数/非参数方向中，效率理论是一条突出线索。**Semiparametric Efficient Quantile Regression** 推导了分位数回归的半参数有效得分与效率界，并给出具体构造方法。**Kernel-Profile Efficient Estimation in Generalized PLM with Missing Outcomes** 在纵向缺失数据下证明其双稳健参数估计可达半参效率界。**Assumption-Lean Quantile Regression** 通过非参数主效应映射将参数解释与模型误设解耦，所得估计量具有一致渐近正态性，可联合机器学习与变量选择。**Efficient Estimation of ATE with Proxies** 同样以半参效率界为靶心，通过联合估计绕过两步偏差。这些工作为半参数效率理论提供了新的估计器与可操作框架，尤其适合关注efficiency bound与debiased推断的读者。

高维统计与假设检验板块中，**Structural Testing of High-dimensional Correlation Matrices** 基于Marchenko-Pastur谱分析构造quadratic与sup-norm检验，适配dense/sparse备择。**Robust Max Statistics for High-dimensional Inference** 在重尾下用L^4-L^2矩条件达到与维度无关的bootstrap近似速率。**Detecting Structural Breaks in High-dimensional Functional Time Series Factor Models** 以WBS结合泛函主成分给出变点定位收敛速率。**Transfer Learning for Ridge Regression with Random Coefficients** 在p/n→常数下用RMT导出最优组合权重闭式极限，是迁移学习中精确渐近的示范。此外，**High-Dimensional Log Contrast Models with Measurement Errors** 的Eric Lasso在组成数据误差下实现变量选择一致性，适合处理微生物组等特殊结构。

对于因果推断与半参数效率方向的研究者，建议优先浏览：**Efficient Estimation of ATE with Proxies**（联合估计达成效率界）、**Semiparametric Causal Discovery with Invalid Instruments**（松弛IV假设）、**Semiparametric Efficient Quantile Regression**（完整效率界推导）、**Kernel-Profile Efficient Estimation**（纵向缺失下双稳健达到效率界）、**Doubly Robust ITR**（半监督DR估计与非标准渐近）。高维方向可关注**Robust Max Statistics**（重尾推断速率无维度依赖）、**Structural Testing of Correlation Matrices**（RMT谱工具）及**Transfer Learning for Ridge**（RMT精确渐近）。

## 因果推断  *(causal_inference, 11 篇)*

### 1. [10.5705/ss.202025.0476](https://doi.org/10.5705/ss.202025.0476) · [arXiv](https://arxiv.org/abs/2401.01977) — Conformal Causal Inference for Cluster Randomized Trials: Model-robust Inference Without Asymptotic Approximations
- **作者**: Bingkai Wang, Fan Li, Mengxin Yu
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文提出在群随机试验（CRT）中使用共形推断进行因果推断，目标是在有限样本下为反事实结果的差异提供预测区间，无需依赖渐近近似。该方法兼容任意工作结果模型，包括数据自适应的机器学习方法，并证明对模型错误设定具有稳健性。研究者开发了高效的算法来构建群水平和个体水平的处理效应预测区间，并进一步扩展至协变量子组。与传统聚焦于平均处理效应估计不同，共形因果推断提供了一种新的决策工具。模拟和实际数据（慢性疼痛CRT）验证了方法性能。该框架将共形推断引入经典因果推断设定，拓展了有限样本有效推断的适用范围，对您在因果推断（特别是CRT设计）中的方法论研究具有直接参考价值。
- **关键技术**: `Conformal inference`, `Cluster randomized trials`, `Prediction intervals for treatment effects`, `Model-robust inference`, `Data-adaptive machine learning`, `Finite-sample valid inference`
- **为什么对您有用**: 本文直接连接您对因果推断（尤其是群随机试验和有限样本推断）的兴趣。您非常熟悉的非参数统计工具（如交换性、排列检验）可以立即用于理解和扩展该共形框架的稳健性边界，属于立即可做的 follow-up。此外，文中算法的实现细节也可与您的软件开发经验结合，便于复现或改进。

### 2. [10.5705/ss.202025.0331](https://doi.org/10.5705/ss.202025.0331) · [arXiv](https://arxiv.org/abs/2504.12085) — Semiparametric Causal Discovery and Inference with Invalid Instruments
- **作者**: Jing Zou, Wei Li, Wei Lin
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对存在未观测混杂变量的因果发现与推断问题，允许工具变量（IV）可能无效且关系非线性。通过引入部分线性结构方程模型（PLSEM），在无需所有IV有效或线性假设的条件下，构建替代有效IV以恢复识别。方法上，提出有限样本程序同时估计因果结构与效应，并控制错误发现率。理论证明了因果结构学习的一致性、估计量的渐近正态性以及FDR控制的有效性。模拟和阿尔茨海默症基因调控网络的应用展示了方法优于现有竞争方法。对您而言，该工作直接拓展了IV在因果推断中的应用场景，与您对IV、半参数估计以及因果识别理论的兴趣高度吻合。
- **关键技术**: `instrumental variables`, `partially linear structural equation model`, `surrogate valid IV`, `false discovery rate control`, `semiparametric estimation`, `causal discovery`
- **为什么对您有用**: 本文处理的是因果推断中IV方向的一个核心难点——IV可能无效且关系非线性，这与您对IV、半参数非参数理论的兴趣直接对应。技术武器库中的非参数统计和因果推断估计理论（非常熟悉）可以直接用于理解该文估计步骤的渐近性质；半参数识别理论（中等熟悉）可帮助您进一步审视其识别条件的充分必要性。总体上，该文属于立即可做的工作：您已有的IV估计和半参数理论储备足以支撑对本文方法的复现、改进或应用到其他数据场景。

### 3. [10.5705/ss.202025.0104](https://doi.org/10.5705/ss.202025.0104) · [arXiv](https://arxiv.org/abs/2501.02214) — Efficient Estimation of Average Treatment Effects with Unmeasured Confounding and Proxies
- **作者**: Chunrong Ai, Jiawei Shan
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在 proximal causal inference 框架下，目标是利用 outcome 和 treatment proxies 在未测量混杂下识别并估计 ATE，核心假设是 bridge function 的存在性。传统方法先参数化估计 bridge function（由积分方程定义）再代入 ATE 估计，存在两步效率损失：积分方程估计难达有效，且未考虑两步估计的相关性。本文提出用递增矩条件（increasing moment restrictions）逼近积分方程，并将 bridge function 与 ATE 联合估计。理论证明在适当条件下该估计量达到 semiparametric efficiency bound，并给出了选择矩条件个数（tuning parameter）的数据驱动方法。模拟与右心导管化（RHC）数据应用验证了有限样本表现。对您有用：本文的递增矩条件逼近与联合估计策略直接关联 proximal CI 的效率理论，且与您熟悉的 HOIF 逼近思路高度同构。
- **关键技术**: `proximal causal inference`, `bridge function`, `increasing moment restrictions`, `joint GMM estimation`, `semiparametric efficiency bound`, `integral equation approximation`
- **为什么对您有用**: 本文直接推进 proximal CI 的效率理论，属于您 primary interest 中 proximal CI 与 efficiency theory 的交叉。您 very_familiar 的 HOIF（Higher-Order Influence Functions）正是用递增矩/投影阶数逼近无穷维 nuisance 的同类技术，可直接用来审视本文的 moment restriction 逼近是否等价于 HOIF 的投影层级，以及其声称的 efficiency 是否在更弱假设下仍成立。**立即可做**：用您 very_familiar 的 HOIF 框架重写本文的逼近机制，验证其效率界与联合估计的 orthogonal score 结构。

### 4. [10.5705/ss.202024.0380](https://doi.org/10.5705/ss.202024.0380) — Kernel-Profile Efficient Estimation in Generalized Partially Linear Models with Missing Outcomes in Longitudinal Studies
- **作者**: Zhongzhe Ouyang, Chang Wang, Lu Wang
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究纵向研究中结果变量存在缺失时的广义部分线性模型。提出纵向增广逆概率加权核-剖面估计方程方法，其中非参数部分采用核估计方程，参数部分采用剖面估计方程，并引入辅助变量对缺失机制和条件均值分别建模。所得参数与非参数估计量均具有双稳健性质。进一步推导了半参数效率界，并在多元正态假设下证明参数估计量达到该效率界。通过模拟和CD4计数数据应用验证了方法的有限样本表现。该工作与您关注的纵向数据因果推断及半参数效率理论直接相关，为缺失数据下的有效估计提供了可操作框架。
- **关键技术**: `kernel estimating equations`, `profile estimating equations`, `augmented inverse probability weighting`, `double robustness`, `semiparametric efficiency bound`, `generalized partially linear models`
- **为什么对您有用**: 本文聚焦纵向缺失数据下的半参数有效估计，直接关联您primary interest中的纵向因果推断与半参数效率理论。您very_familiar中的非参数统计和因果推断估计理论可快速理解其核估计与双稳健机制，moderately_familiar中的半参数理论则可用于评估效率界推导的适用条件与推广潜力。基于现有工具，您能立即可做：将该双稳健框架融入纵向因果推断的敏感性分析或IV方法中，处理类IVEGO或Mediation中的缺失问题。

### 5. [10.5705/ss.202025.0168](https://doi.org/10.5705/ss.202025.0168) — Doubly Robust Estimation of Optimal Individual Treatment Regime in A Semi-supervised Framework
- **作者**: Xintong Li, Mengjiao Peng, Yong Zhou
- **期刊/来源**: Statistica Sinica
- **机构**: East China Normal University
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在半监督框架下（大量无标签数据与少量有标签数据并存），目标是估计最优个体化治疗方案（ITR）的价值函数。作者提出基于单指标核平滑的灵活插补技术以利用无标签数据，随后通过直接优化插补价值函数确定最优 ITR。在倾向得分未知的观察性研究中，进一步基于单调指标模型类构建了双重稳健（DR）半监督估计量。理论证明估计量具有立方根收敛速率（cube root n），且非标准渐近分布表现为带二次漂移的中心化高斯过程的最大值点。模拟与 ACTG 175 实际数据验证了方法相对于纯监督方法的效率提升与稳健性。对您有用：本文将半监督效率增益与 ITR 的 DR 估计结合，且立方根收敛与非标准分布的理论细节直接触及您在因果推断估计理论与半参数效率方面的兴趣。
- **关键技术**: `doubly robust estimation`, `semi-supervised learning`, `single-index kernel smoothing`, `cube root convergence rate`, `maximizer of Gaussian process with quadratic drift`, `monotonic index model`
- **为什么对您有用**: 本文直接连接因果推断中的 ITR 估计与半监督效率增益，属于您 primary interest 中因果推断估计理论与效率理论的交叉。您武器库中 very_familiar 的 M-estimation theory 与 moderately_familiar 的 semiparametric theory 可以直接攻入其立方根收敛与非标准分布的证明细节，验证其 DR 结构下的半监督效率界是否紧。follow-up 判断：**立即可做**——用您熟悉的 M-estimation 与 minimax bound 工具即可动手分析其收敛速率与效率界。

### 6. [10.5705/ss.202025.0267](https://doi.org/10.5705/ss.202025.0267) — Semi-Parametric Estimation of Potential Outcome Distributions and General Causal Estimands by Borrowing Information from Both Treatments and Controls
- **作者**: Manli Cheng, Yukun Liu
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在潜在结果框架下，本文针对潜在结果分布的估计问题，提出半参数比例似然比模型（SPLRM），通过共享基线分布联合建模处理组和对照组的条件分布，以利用两组间的相似性。核心估计方法为最大经验似然估计（MELE），并开发了迭代经验似然算法求解参数；同时提出简单似然比检验（LRT）判断分布型处理效应，其零假设下渐近服从中心卡方分布。理论证明各类因果 estimand 的估计量具有渐近正态性，相比传统分组独立估计方法提升了效率与鲁棒性。对您有用：本文的 SPLRM 假设为潜在结果分布间的信息借用提供了新的半参数 identification 路径，其经验似然框架下的效率提升可直接与您熟悉的 semiparametric efficiency bound 理论进行对比验证。
- **关键技术**: `semi-parametric proportional likelihood ratio model`, `maximum empirical likelihood estimation`, `iterative empirical likelihood algorithm`, `likelihood ratio test for distributional treatment effect`, `asymptotic normality of causal estimands`, `information borrowing across treatment groups`
- **为什么对您有用**: 本文直接连接因果推断的 estimation theory 子方向，通过半参数比例似然比模型实现跨组信息借用以提升效率。您可用 very_familiar 中的 semiparametric theory 和 minimax bounds 工具，严格推导该模型下各类 estimand 的 semiparametric efficiency bound，验证其声称的效率提升是否真正达到 bound。follow-up 判断：立即可做——用您熟悉的 semiparametric efficiency 理论即可动手分析其效率声称的紧性。

### 7. [10.5705/ss.202025.0315](https://doi.org/10.5705/ss.202025.0315) · [arXiv](https://arxiv.org/abs/2602.07390) — Balancing Covariates in Survey Experiments
- **作者**: Pengfei Tian, Jiyang Ren, Yingying Ma
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究调查实验中的协变量平衡问题，目标是在有限样本中改善协变量不平衡导致的估计效率损失。提出一种结合分层拒绝抽样与再随机化的实验设计，通过拒绝不平衡的样本并重新随机化处理分配，在采样和分配两个阶段同时增强协变量平衡。针对该设计下的分层差分估计量，建立了基于设计的渐近理论，证明其极限分布是正态分布与两个截断正态分布的卷积，比传统实验设计的极限分布更集中在真实平均处理效应附近。进一步提出分析阶段的协变量调整方法，利用分层信息和协变量进一步提升估计效率。数值研究验证了所提方法在有限样本下的有效性。该工作与因果推断中的实验设计、基于设计的推断有直接关联，对您熟悉的处理效应估计和随机化理论有参考价值。
- **关键技术**: `stratified rejective sampling`, `rerandomization`, `design-based inference`, `difference-in-means estimator`, `truncated normal distribution`, `covariate adjustment`
- **为什么对您有用**: 本文属于因果推断中的实验设计方向，直接关联您的主要兴趣之一causal inference中的estimation theory。您熟悉的nonparametric statistics和estimation theory in causal inference中的渐近工具可直接用于理解其极限分布推导和设计效率分析。立即可做：基于该设计的渐近分布结果，可进一步考虑在更复杂因果参数（如ATE with noncompliance或mediation）下的推广与推断。

### 8. [10.5705/ss.202025.0066](https://doi.org/10.5705/ss.202025.0066) · [arXiv](https://arxiv.org/abs/2501.17514) — Semiparametric Principal Stratification Analysis Beyond Monotonicity
- **作者**: Jiaqi Tong, Brennan Kahan, Michael O. Harhay, Fan Li
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究主分层分析（principal stratification）中放宽单调性假设的问题。在临床对照试验和观察研究中，中间事件常影响结局的存在或解释，主分层通过定义亚组内局部平均处理效应来解决，但通常依赖单调性等限制性假设。作者提出一个半参数框架，利用无边际条件优势比（odds ratio）作为敏感性参数，在principal ignorability假设下导出非参数识别公式。方法包括条件双稳健参数估计器和基于数据自适应学习的去偏机器学习估计器，实现有效推断。模拟表明错误假设单调性常导致偏倚推断，而错误假设非单调性时近似推断仍有效。在关键护理试验数据中演示了方法。本文对您将因果推断中的敏感性分析扩展到主分层框架有直接参考价值。
- **关键技术**: `principal stratification`, `odds ratio sensitivity parameter`, `principal ignorability`, `doubly robust estimation`, `debiased machine learning`, `nonparametric identification`
- **为什么对您有用**: 本文直接连接您primary interest中的因果推断子方向，特别是主分层分析与敏感性分析的交叉。您可以使用very_familiar中的nonparametric statistics和estimation theory来评估其识别策略与估计量，并利用moderately_familiar的identification theory探讨在proximal CI框架下的推广。立即可做：您已有的因果推断工具即可复现其模拟或检验其鲁棒性。

### 9. [10.5705/ss.202025.0236](https://doi.org/10.5705/ss.202025.0236) · [arXiv](https://arxiv.org/abs/2311.04696) — Quantification and Inference of Asymmetric Relations Under Generative Exposure Mappings
- **作者**: Soumik Purkayastha, Peter Xuekun Song
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 generative exposure mapping (GEM) 框架下，目标是量化噪声扰动模型 Y=g(X)+ε 中 X→Y 与 Y→X 的方向性不对称，无需先验排序假设。作者提出基于 Shannon 熵的 asymmetry coefficient，通过 FFT-based 密度估计避免调参，并利用 data-splitting 与 cross-fitting 获得该系数的 n^{-1/2}-CAN 性质与渐近正态性，从而实现不确定性量化的统计推断。该方法允许生成函数 g 属于宽泛的非参数类，并容忍结局变量的测量污染。模拟显示其优于现有 bivariate causal discovery 方法；在 DNA 甲基化与血压的流行病学数据中，揭示了 FGF5/HSD11B2 的致病通路。对您有用：本文将非参数密度估计与 cross-fitting 结合用于因果方向推断，为 bivariate causal discovery 的 identification 与 inference 提供了新视角。
- **关键技术**: `generative exposure mapping`, `Shannon entropy-based asymmetry coefficient`, `FFT-based density estimation`, `cross-fitting`, `asymptotic normality`, `bivariate causal discovery`
- **为什么对您有用**: 本文连接到 causal inference 的 bivariate causal discovery / identification 子方向，用 cross-fitting 与非参数密度估计构造可做推断的 asymmetry coefficient。研究者 very_familiar 的 minimax bounds 与 nonparametric statistics 可直接用来审视该 estimator 在不同 g 类下的 rate 是否紧，moderately_familiar 的 semiparametric theory 可分析其 influence function 结构。Follow-up 粗判：立即可做——用 very_familiar 的非参数 minimax 理论验证其 FFT 密度估计步骤的收敛率是否达到最优。

### 10. [10.5705/ss.202025.0156](https://doi.org/10.5705/ss.202025.0156) — Conformal Prediction Under Nonignorable Missingness
- **作者**: Menghan Yi, Yingying Zhang, Yanlin Tang, Huixia Judy Wang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非可忽略缺失（nonignorable missingness）设定下，目标是为新个体构建条件密度预测集，面临非识别性与数据不可交换性两大核心挑战。作者提出基于 conformal prediction 的框架：对结局回归保持 model-free，但依赖一致估计的倾向得分（propensity score）来纠正选择偏差。核心机制是利用目标点附近的局部子集构建最高条件密度预测集，并通过倾向得分加权修正偏差。框架内开发了一种偏差调整的半参数条件密度估计器：对观测数据拟合分位数过程，再用倾向得分权重纠偏。该方法不仅保证边际覆盖，还保证局部与渐近条件覆盖，且区间长度渐近最优；仿真与 HIV-CD4 数据验证了有效性。对您可能有用：该文将倾向得分纠偏与 conformal prediction 结合，为缺失数据下的预测推断提供了新视角，直接连接因果推断中的选择偏差/倾向得分建模与半参数效率理论。
- **关键技术**: `conformal prediction`, `nonignorable missingness`, `propensity score weighting`, `semiparametric conditional density estimation`, `quantile process fitting`, `local highest conditional density set`
- **为什么对您有用**: 本文直接连接因果推断中的非可忽略缺失/选择偏差处理与倾向得分建模，属于 primary interest 中因果推断的缺失数据设定。技术武器库中 very_familiar 的倾向得分与 moderately_familiar 的半参数理论可直接攻入其偏差调整半参数估计器的效率分析（如是否达到半参数效率界）。Follow-up 判断：**立即可做**——用您熟悉的半参数效率界工具验证其条件密度估计器的渐近最优性是否真正达到效率下界，或探讨 propensity score 估计误差对 coverage 的更高阶影响。

### 11. [10.5705/ss.202025.0034](https://doi.org/10.5705/ss.202025.0034) · [arXiv](https://arxiv.org/abs/2404.10495) — Assumption-Lean Quantile Regression
- **作者**: Georgi Baklicharov, Christophe Ley, Vanessa Gorasso, Brecht Devleesschauwer, Stijn Vansteelandt
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对分位数回归中模型误设和变量选择导致的估计偏差与过度不确定性，提出了一种假设松弛（assumption-lean）的部分线性分位数回归方法。该模型将感兴趣的暴露协变量关联参数化，但不限制其他协变量的函数形式，从而使目标参数即使在分位数模型误设下仍具有明确的因果/关联解释。作者将感兴趣参数映射为一个非参数主效应估计量，并推导其在非参数模型下的有效影响函数，进而构建了一致且渐近正态的估计量。该估计量可自然融入数据自适应过程（如机器学习、变量选择），无需假设参数模型正确也能保证推断的有效性。通过模拟和比利时年度医疗费用与超重关联的实际数据分析，展示了方法的稳健性和实用性。本文对因果推断中部分线性模型的稳健估计以及半参数效率理论的应用具有直接启发。
- **关键技术**: `partially linear quantile regression`, `efficient influence function`, `assumption-lean estimation`, `data-adaptive estimation`, `nonparametric main effect estimand`
- **为什么对您有用**: 本文属于因果推断中关联参数稳健估计的方法论贡献，直接对应您的主要兴趣——因果推断的估计理论与半参数效率理论。您的技术武库中'因果推断的估计理论'（非常熟悉）与'半参数理论'（中等熟悉）足以立刻理解其核心机制，并可将其中的假设松弛思路迁移到您关注的 Proximal CI 或 IV 设定中，例如在负对照假设下构建类似的双稳健分位数估计。**立即可做**：您无需额外学习新工具即可复现或拓展该方法。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 17 篇)*

### 1. [10.5705/ss.202025.0223](https://doi.org/10.5705/ss.202025.0223) · [arXiv](https://arxiv.org/abs/2407.15084) — High-Dimensional Log Contrast Models with Measurement Errors
- **作者**: Wenxi Tan, Lingzhou Xue, Songshan Yang, Xiang Zhan
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 针对高维组成数据（compositional data）的回归分析，协变量测量误差因成分间依赖而尤为棘手。本文提出 Eric Lasso 方法，在保持 log-contrast 模型“成分和为1”约束的同时，引入乘法测量误差结构。理论部分推导了 Eric Lasso 的估计误差界（在高维稀疏设定下），并证明其具有渐进符号一致的变量选择性质。方法通过 L1 正则化联合处理稀疏性与测量误差，与标准 Compositional Lasso 相比在误差存在下显著提升变量选择精度。模拟实验显示有限样本性能优越，并在真实微生物组数据上验证实用性。对您而言，该论文是 high-dimensional statistics 中一个带有特殊约束的变量选择问题，可直接用您熟悉的 minimax 框架检验其误差界的紧性。
- **关键技术**: `Error-in-composition (Eric) Lasso`, `log-contrast model`, `multiplicative measurement error`, `high-dimensional variable selection`, `sign-consistent selection`, `sparsity regularization`
- **为什么对您有用**: 直接对应您 primary interest 中的 high-dimensional statistics 子方向，特别是高维线性模型的变量选择与测量误差处理。您武器库中的 minimax bounds 和 high-dimensional asymptotics 可直接用于检验本文估计误差界的最优性，属于立即可做的工作。此外，组成数据在流行病学（微生物组）中常见，也连接 secondary interest。

### 2. [10.5705/ss.202025.0014](https://doi.org/10.5705/ss.202025.0014) — Detecting Structural Breaks in High-dimensional Functional Time Series Factor Models
- **作者**: Caixia Xu, Huacheng Su, Xu Liu, Jinhong You
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维函数时间序列因子模型设定下，研究因子载荷随时间发生未知次数结构变点的检测与定位问题，estimand 为变点位置与个数。方法分三步：逐时刻估计因子载荷并计算相邻时刻载荷差异序列；对差异序列采用 wild binary segmentation (WBS) 估计变点个数与位置；基于估计变点重新估计函数因子模型。理论给出了变点估计的一致性及定位误差的收敛速率，依赖于高维泛函主成分估计与 WBS 的 empirical process 分析。对您可能有用：该文将高维因子模型变点检测与 WBS 结合，其载荷差异序列的收敛分析涉及随机矩阵谱分离与泛函估计，可连接到您的高维渐近理论与 RMT primary interest。
- **关键技术**: `functional factor model`, `wild binary segmentation`, `change point detection`, `high-dimensional functional PCA`, `spectral separation`, `time-varying factor loadings`
- **为什么对您有用**: 直接连接到您的高维统计与 RMT 子方向：高维因子模型载荷估计的谱分离条件与随机矩阵理论紧密相关，变点检测的 WBS 机制依赖 empirical process 工具。您武器库中 very_familiar 的「高维渐近理论」可直接切入该文载荷差异序列的谱收敛分析，评估其定位误差 rate 是否可达 minimax；moderately_familiar 的 M-estimation 理论可用于审视其泛函主成分估计的渐近性质。判断：**立即可做**——用 very_familiar 的高维渐近与 minimax bound 工具即可验证其收敛速率的紧性，并探索 RMT Marchenko-Pastur 型工具是否可替代其谱分离假设给出更弱条件。

### 3. [10.5705/ss.202025.0087](https://doi.org/10.5705/ss.202025.0087) — Distributed Algorithms for High-Dimensional Statistical Inference and Structure Learning with Heterogeneous Data
- **作者**: Hongru Zhao, Xiaotong Shen
- **期刊/来源**: Statistica Sinica
- **机构**: Twin Cities Orthopedics
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在分布式高维异质数据设定下，目标是同时估计全局效应与站点特异效应，同时满足隐私约束下仅共享汇总统计的限制。作者提出异质模型整合全局与局部参数，通过非凸 ℓ0 约束的 difference-of-convex (DC) 算法实现变量选择一致性。尽管底层优化 worst-case NP-hard，但在合理条件下该方法以高概率在多项式时间内收敛至全局最优。关键推断策略是对 nuisance 参数施加 ℓ0 惩罚而对假设检验参数不加惩罚，从而保证 debiased-type 的有效统计推断。对您可能有用：该文在分布式高维推断中的 ℓ0-DC 框架与多项式时间可达性，直接触及 stat-computing tradeoff 中的 polynomial-time achievability 问题。
- **关键技术**: `difference-of-convex programming`, `ℓ0 nonconvex penalization`, `distributed heterogeneous model`, `selection consistency`, `polynomial-time convergence`, `debiased inference for unpenalized parameters`
- **为什么对您有用**: 本文直接连接 stat-computational tradeoff 中的 polynomial-time achievability：在 worst-case NP-hard 的 ℓ0 优化问题上，给出了高概率多项式时间收敛至全局最优的条件，属于典型的 average-case tractability 结果。用您 very_familiar 的高维渐近理论可以审视其收敛条件与 minimax 视角的差距；用 moderately_familiar 的 M-estimation 理论可检查其 nuisance 参数 ℓ0 惩罚下推断的有效性证明。**中期可做**：需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以严格审视其 debiased 推断的 influence function 展开与异质模型下的 semiparametric efficiency bound。

### 4. [10.5705/ss.202024.0248](https://doi.org/10.5705/ss.202024.0248) — Hybrid Denoising-screening for High-dimensional Contaminated Data
- **作者**: Liming Wang, Peng Lai, Chen Xu, Xingxiang Li
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维污染数据（同时含噪声观测与无关特征）设定下，目标是同时筛选出干净样本与有效特征，保证sure screening性质。本文提出hybrid denoising-screening（HDS）方法，核心是基于dual sample-feature L0拟合程序，精确控制保留的观测数与特征数。理论部分证明了在常规regularity条件下HDS的sure screening一致性及特征/样本选择的误差率界，数值实验显示其优于仅做特征筛选的传统方法。对您有用：此文的dual L0拟合与高维筛选框架可视为高维稳健估计的一个入口，与您的高维统计与M-estimation理论兴趣直接相关。
- **关键技术**: `feature screening`, `L0 penalized fitting`, `sure screening property`, `dual sample-feature selection`, `high-dimensional contaminated data`
- **为什么对您有用**: 直接连接您的高维统计与M-estimation理论兴趣：dual L0拟合的样本-特征联合选择是一个非标准的高维M-estimation问题，可用您very_familiar的minimax bounds工具审视其理论界是否紧，或用moderately_familiar的M-estimation理论分析其收敛条件。中期可做：需先在moderately_familiar的M-estimation理论上补强高维penalized拟合的oracle性质推导，再可切入对其理论界的sharpening或扩展。

### 5. [10.5705/ss.202025.0132](https://doi.org/10.5705/ss.202025.0132) — Random Weighting Approximation of M-estimators with Increasing Dimensions of Parameter
- **作者**: Ruixing Ming, Chengyao Yu, Min Xiao, Zhanfeng Wang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文研究参数维度随样本量增长时，M-估计量的随机加权（RW）逼近性质。传统RW理论主要针对固定维度参数，本文将其推广到高维情形，证明了RW估计量与原始M-估计量具有相同的渐近分布，从而无需估计渐近方差中的冗余参数即可进行统计推断。文章建立了RW估计量的Bahadur表示、收敛速度等关键统计性质，为高维M-估计的推断提供了理论保障。该工作与高维统计推断和M-估计理论直接相关，对您在高维假设检验和因果推断中的参数估计问题有参考价值。
- **关键技术**: `Random weighting`, `M-estimator`, `Bahadur representation`, `high-dimensional inference`, `increasing dimension asymptotics`
- **为什么对您有用**: 该论文直接切入您primary interest中的高维统计理论，特别是M-估计在高维设定下的推断问题。您武器库中的high-dimensional asymptotics和M-estimation theory可以直接用于理解其理论机制，并可尝试将其扩展至因果推断中的高维M-估计（如高维IV估计）或semiparametric M-estimation场景。follow-up判断：中期可做——需在moderately_familiar的M-estimation theory上进一步熟悉，即可结合您的causal inference工作。

### 6. [10.5705/ss.202025.0212](https://doi.org/10.5705/ss.202025.0212) · [arXiv](https://arxiv.org/abs/2501.13614) — Determining the Number of Factors in Two-way Factor Model of High-dimensional Matrix-variate Time Series: a White-noise Based Method for Serial Correlation Models
- **作者**: Qiang Xia, W.K. Li, Rubing Liang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该文针对高维矩阵时间序列的双向因子模型，提出基于白噪声分量的两类比率估计量以确定行、列因子空间的维数。具体地，作者利用样本自协方差矩阵的元素最大范数和Frobenius范数构造归一化统计量，并通过比率方法选择转折点。为削弱行间和列间因子强度异质性的影响，原始模型被重参数化为仅含行载荷或仅含列载荷的简约形式，再运用改进的比率准则。在正则条件下，证明了估计量的相合性。蒙特卡洛模拟和真实数据（如宏观经济指标）验证了有限样本性能，并与现有方法进行了对比。对您来说，该方法为高维时间序列的因子数选择提供了直观且可操作的途径，可应用于宏观金融等需处理矩阵型面板数据的因果推断场景。
- **关键技术**: `white-noise-based ratio estimators`, `element-wise maximum norm`, `Frobenius norm`, `sample autocovariance matrix`, `matrix factor model`, `reparameterization`
- **为什么对您有用**: (1) 连接到高维统计和随机矩阵理论中的因子模型鉴定问题，这是您primary interests中高维统计的子方向；(2) 您very familiar的“高维渐近”工具可直接用于分析比率估计量的极限行为，但需补充时间序列依赖下的自协方差矩阵收敛性质，属于中期可做的缺口——因为白噪声检验的依赖结构分析尚不在武器库内；(3) 论文方法对矩阵数据的因子数选择具有应用前景，值得跟进验证其在实际数据上的表现。

### 7. [10.5705/ss.202025.0292](https://doi.org/10.5705/ss.202025.0292) — A Two-Way Factor Model for High-dimensional Matrices with Cross-section and Time-Series Effects
- **作者**: Qiang Xia, Zhigen Gao, Gaorong Li, Rubing Liang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `sharper_rate`
- **摘要**: 在高维面板时间序列设定下，本文提出一种新型双向因子模型，假定低维隐因子受行、列效应的可分离影响，目标是对因子载荷及参数进行 likelihood inference。核心机制基于矩阵分解技术构建似然，利用传统 delta method（依赖 score function 与 Hessian）推导 MLE 的渐近分布，并设计基于 diagonal block matrix 的快速参数估计算法。在 regularity 条件下，证明了估计量的 consistency 与 asymptotic normality，关键理论结果为达到 √T-consistency，显著优于先前文献的收敛速率。仿真与实证分析验证了方法有效性。对您可能有用：该矩阵分解+似然推断框架为高维矩阵数据的因子建模提供了更优收敛率，与您的高维渐近理论及统计计算（矩阵算法）兴趣直接相连。
- **关键技术**: `two-way factor model`, `matrix decomposition likelihood`, `delta method for MLE`, `diagonal block matrix algorithm`, `√T-consistency`, `asymptotic normality`
- **为什么对您有用**: 本文直接连接您的高维统计与随机矩阵理论兴趣，其矩阵分解与似然推断框架属于高维渐近理论范畴；您 very_familiar 的高维渐近理论可直接审视其声称的 √T-consistency 是否紧、以及 delta method 在此矩阵因子设定下的渐近展开是否完备。此外，其 diagonal block matrix 快速算法与您 statistical computing / matrix 兴趣契合。Follow-up 粗判：**立即可做**——用您熟悉的高维渐近与 M-estimation 理论工具即可检验其收敛率与渐近正态性证明的严谨度，并评估其矩阵算法的计算复杂度。

### 8. [10.5705/ss.202025.0303](https://doi.org/10.5705/ss.202025.0303) · [arXiv](https://arxiv.org/abs/2412.19963) — Linear Shrinkage Convexification of Penalized Linear Regression with Missing Data
- **作者**: Seongoh Park, Seongjin Lee, Nguyen Thi Hai Yen, Nguyen Phuoc Long, Johan Lim
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在含缺失数据的高维惩罚线性回归设定下，目标是修正因缺失导致的协方差矩阵非正定问题，恢复凸性并保证稀疏估计的一致性。作者提出 linear shrinkage positive definite (LPD) 修正，通过线性收缩估计将样本协方差矩阵强制正定，使 L1-penalized 回归的损失函数重回凸域。LPD 修正具有解析表达式，计算代价极低。理论上，作者证明了 LPD-Lasso 的 selection consistency，并给出 ℓ2-error 收敛率为 √(log p / n) × s0^{3/2}（s0 为真实非零系数数），该率因缺失与收缩修正引入了 s0^{3/2} 因子，相比无缺失标准 Lasso 的 s0^{1/2} 略粗。实证部分在 GDSC 癌症药物敏感性数据上验证了方法。对您可能有用：LPD 的线性收缩修正思路与高维协方差矩阵估计的 RMT 收缩法直接相通，可作为缺失数据下凸化手段的入门参考。
- **关键技术**: `linear shrinkage covariance estimator`, `convexification of non-convex loss`, `L1-penalized regression with missing data`, `selection consistency`, `ℓ2-error convergence rate`
- **为什么对您有用**: 本文直接连接到高维统计与协方差矩阵估计（RMT shrinkage 方法）的交叉点：缺失数据下用线性收缩强制正定以恢复凸性。您武器库中 high-dimensional asymptotics 与 minimax bounds 可直接用来审视其声称的 s0^{3/2} 收敛率是否紧，或能否用更精细的 RMT 收缩（如 Ledoit-Wolf / Marchenko-Pastur 最优收缩）替代其线性收缩以改善 rate。Follow-up 判断：**立即可做**——用 very_familiar 的高维 minimax 理论验证其 rate 的紧性，并尝试将 LPD 替换为 RMT-optimal shrinkage 看是否可消除 s0^{3/2} 因子。

### 9. [10.5705/ss.202024.0341](https://doi.org/10.5705/ss.202024.0341) · [arXiv](https://arxiv.org/abs/2410.11320) — Regularized Estimation of High-Dimensional Matrix-Variate Autoregressive Models
- **作者**: Hangjin Jiang, Baining Shen, Yuzhou Li, Zhaoxing Gao
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究高维矩阵时间序列的估计问题，采用双线性矩阵自回归（Bilinear MAR）模型，该模型通过行-列交互降低复杂度。针对大维情形下传统迭代最小二乘估计参数过多、难以解释的困境，提出两种正则化方法：第一种假设系数矩阵为带状结构，采用带限迭代最小二乘估计，并利用BIC选择带宽；第二种假设稀疏结构，引入LASSO进行变量选择。理论上，在维度发散（p,q→∞）且样本量T→∞的渐近框架下，推导了带状估计和LASSO估计的相合性与渐近分布。模拟和实际数据（如经济指标）表明，两种方法在预测性能上优于普通自回归模型，且能实现有效降维。该工作对您在高维统计（矩阵型数据建模与正则化理论）和统计计算（迭代算法与稀疏优化）两个方向有直接参考价值。
- **关键技术**: `bilinear matrix-variate autoregressive model`, `banded iterated least squares`, `LASSO regularization`, `Bayesian Information Criterion (BIC) for bandwidth selection`, `high-dimensional asymptotics with diverging dimensions`
- **为什么对您有用**: 本文直接对接您在高维统计中“矩阵型数据建模”这一子方向，特别是高维矩阵自回归的结构化正则化（带状、稀疏）为处理类似的时间序列数据（如经济学、流行病学中的面板数据结构）提供了可复用的估计框架。您熟悉的high-dimensional asymptotics工具（very_familiar）足以理解其理论证明和收敛速率，并可立即检验其是否达到minimax最优。因此，立即可做——只需花时间消化模型设定和正则化参数的选择细节。

### 10. [10.5705/ss.202024.0423](https://doi.org/10.5705/ss.202024.0423) · [arXiv](https://arxiv.org/abs/2306.04182) — Simultaneous Estimation and Dataset Selection for Transfer Learning in High Dimensions by a Non-convex Penalty
- **作者**: Zeyu Li, Dong Liu, Yong He, Xinsheng Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维迁移学习问题，提出一个非凸惩罚方法，同时实现模型参数估计和信息源数据集选择，区别于现有分开进行数据集筛选与迁移学习的两阶段流程。具体处理稀疏线性回归和一般化低秩迹回归两种模型，采用差值凸规划（DC）与交替方向乘子法（ADMM）求解非凸目标函数。从统计角度证明了估计量的一致性和选择一致性；从计算角度证明了算法的收敛性。大量数值模拟验证了理论结果，并提供了R包MHDTL供实际使用。该方法在高维情景下将数据集识别与估计统一为一个优化问题，避免了信息泄露与两阶段误差累积。对您而言，高维统计的理论框架与R包开发直接对应您非常熟悉的技术，而DC/ADMM的算法分析可借助M估计理论进一步深化，为后续在因果迁移学习等方向提供工具基础。
- **关键技术**: `non-convex penalty`, `difference of convex (DC) programming`, `alternating direction method of multipliers (ADMM)`, `sparse linear regression`, `low-rank trace regression`, `transfer learning`
- **为什么对您有用**: (1) 本文直接涉及高维统计中的迁移学习与变量/数据选择，是您高维统计兴趣的具体子方向。 (2) 技术武器库中“高维渐近理论”可用于分析估计量的统计性质，“软件发展”可直接利用R包进行复现与拓展。 (3) 中期可做：在非凸优化与DC/ADMM的算法分析上，需先加强M估计理论（moderately_familiar），再结合您已有的高维渐近工具，可进一步推导有限样本误差界或开发更高效的求解器。

### 11. [10.5705/ss.202025.0283](https://doi.org/10.5705/ss.202025.0283) · [arXiv](https://arxiv.org/abs/2502.12621) — A Primal Dual Active Set with Continuation Algorithm for ℓ0-penalized High-dimensional Accelerated Failure Time Model
- **作者**: Peili Li, Ruoying Hu, Yanyun Ding, Yunhai Xiao
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维右删失数据下的加速失效时间(AFT)模型, 提出基于ℓ0-惩罚的加权最小二乘估计方法, 以同时实现变量选择与系数估计. 核心算法采用原始-对偶积极集(primal-dual active set)求解非凸优化问题, 并引入连续化(continuation)策略自动选取正则化参数, 避免了网格搜索. 理论上, 在协变量矩阵满足互不相关性(mutual incoherence)与限制等距性(RIP)的条件下, 证明了迭代过程中活跃集的单调性以及算法在有限步内终止于oracle解. 通过模拟与真实乳腺癌数据集, 与LASSO、SCAD等方法对比, 展示了该方法在预测精度和变量选择一致性上的优势. 本文为高维删失数据提供了一套有理论保证的计算框架, 其算法分析与高维渐近理论(您非常熟悉)及M-估计理论(中度熟悉)强相关, 可直接借鉴于因果推断中删失数据或高维工具变量的处理.
- **关键技术**: `ℓ0-penalized regression`, `accelerated failure time model`, `primal-dual active set algorithm`, `continuation strategy`, `mutual incoherence property`, `restricted isometry property`
- **为什么对您有用**: 本文直接面向高维删失数据下的变量选择, 拓宽了您在高维统计方向的应用场景. 算法证明依赖互不相关性与限制等距性, 与您武器库中高维渐近理论(very_familiar)和M-估计理论(moderately_familiar)高度契合, 可立即可做地将其推广至因果推断中的删失协变量或纵向数据情况. 该算法框架值得全文研读以借鉴其有限步收敛分析思路.

### 12. [10.5705/ss.202025.0232](https://doi.org/10.5705/ss.202025.0232) · [arXiv](https://arxiv.org/abs/2306.15915) — Transfer Learning for Ridge Regression with Random Coefficients
- **作者**: Hongzhe Zhang, Hongzhe Li
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在高维随机系数 ridge regression 框架下，研究如何利用来自相关源模型的样本进行迁移学习；目标 estimand 为目标模型系数的估计与预测风险，关键假设为源-目标系数相关性刻画源信息量。提出两个加权估计器（分别最小化估计风险与预测风险），本质是目标与源 ridge 估计的最优凸组合。在高维渐近 regime p/n → 常数下，利用随机矩阵理论（Marchenko-Pastur 型 Silverstein 方程）推导出最优权重与对应风险的闭式极限。模拟与脂质性状/结直肠癌微生物组预测应用显示该方法一致优于仅用目标或混合数据的 ridge。对您可能有用：本文将 RMT 的精确渐近分析引入迁移学习，为高维因果/半参数估计中的多源数据融合提供了新的风险刻画视角。
- **关键技术**: `random-coefficient ridge regression`, `transfer learning optimal weighting`, `random matrix theory high-dimensional asymptotics`, `Silverstein equation`, `estimation and prediction risk limits`
- **为什么对您有用**: 本文直接连接到 primary interest 中的高维统计与 RMT，利用 RMT 给出迁移学习权重的精确渐近闭式解，而非泛泛的 consistency。用您 very_familiar 的 high-dimensional asymptotics 与 minimax bounds 工具，可以审视其声称的“最优”权重在更一般协方差结构或 misspecified 源相关性下的鲁棒性，并尝试推导 minimax lower bound 验证其风险极限是否紧。此方向立即可做：您现有的 RMT 与高维渐近工具足以展开对其理论框架的扩展分析。

### 13. [10.5705/ss.202025.0205](https://doi.org/10.5705/ss.202025.0205) · [arXiv](https://arxiv.org/abs/2501.02244) — Sparsity Learning via Structured Functional Factor Augmentation
- **作者**: Hanteng Ma, Ziliang Shen, Xingdong Feng, Xin Liu
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维函数线性回归设定下，研究存在相关性时函数协变量的变量选择与推断问题，目标 estimand 为回归系数函数及稀疏选择集。本文提出函数因子增广结构（fFAS）对多元函数序列提取公共因子以消除协变量间相关性，并在此基础上构建函数因子增广选择模型（fFASM）实现稀疏学习。理论部分证明了 fFAS 的因子提取有效性，并建立了 fFASM 的估计一致性与选择一致性（selection consistency）。数值模拟显示 fFASM 在估计精度与选择一致性上优于忽略相关性的传统方法。对您可能有用：该文在高维函数数据中用因子增广解耦相关性的思路，与高维统计中因子模型/随机矩阵谱分解的技术路线相通，可作为理解高维函数协变量推断的入口。
- **关键技术**: `functional linear regression`, `factor augmentation structure`, `sparse variable selection`, `selection consistency`, `high-dimensional functional data`
- **为什么对您有用**: 本文连接到高维统计（因子增广解耦）与半参数/非参数理论（函数协变量回归）的交叉方向。您武器库中 high-dimensional asymptotics 与 minimax bounds 可直接用来审视其声称的 selection consistency 条件是否过强、收敛率是否可达 minimax 下界。判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，才能将函数系数推断推进到 semiparametric efficiency bound 与 debiased 框架。

### 14. [10.5705/ss.202025.0071](https://doi.org/10.5705/ss.202025.0071) · [arXiv](https://arxiv.org/abs/2411.15713) — Bayesian High-Dimensional Grouped-Regression Using Sparse Projection-posterior
- **作者**: Samhita Pal, Subhashis Ghosal
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的贝叶斯高维分组回归方法——稀疏投影后验（Sparse Projection Posterior），通过构造稀疏诱导映射将稠密后验投影到低维稀疏参数空间，从而实现组级变量选择和估计。具体设计了三种投影映射：Group LASSO 投影后验、Group SCAD 投影后验以及 Adaptive Group LASSO 投影后验，分别对应不同的惩罚函数。理论方面，推导了估计和预测的最优后验收缩率，并证明方法具有模型选择一致性。此外，还提出去偏 Group LASSO 投影映射（Debiased Group LASSO Projection Map），使得所得可信集达到精确覆盖频率。该方法可自然应用于非参数可加模型，通过 B 样条展开刻画协变量与响应之间的复杂关系。大量模拟验证了理论结论，并应用于 ADNI 脑 MRI 数据，识别与阿尔茨海默症进展相关的关键脑区。该方法将贝叶斯推断与高维分组回归结合，为高维统计中的结构稀疏性问题提供了一种新途径。
- **关键技术**: `Sparse projection posterior`, `Group LASSO penalty`, `Posterior contraction rate`, `Model selection consistency`, `Debiased Group LASSO`, `B-spline expansions`
- **为什么对您有用**: 该论文直接对应您在高维统计（high-dimensional statistics）方向的核心兴趣，特别是分组变量选择和收缩率分析。您技术库中“high-dimensional asymptotics”和“minimax bounds for estimation problems”两项非常熟悉的工具可用于检验其声称的后验收缩率是否最优（对比已知 minimax rate），甚至可进一步探索投影映射的构造是否能在其他稀疏结构（如树结构组）下得到类似的理论保证。综上，这篇论文立即可做：用现成的渐近分析技术即可深入评估其理论紧致性并考虑扩展方向。

### 15. [10.5705/ss.202024.0294](https://doi.org/10.5705/ss.202024.0294) — Uncertainty Quantification for Large-Scale Deep Neural Networks via Post-StoNet Modeling
- **作者**: Yan Sun, Faming Liang
- **期刊/来源**: Statistica Sinica
- **机构**: University of Pennsylvania
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 该论文针对大规模深度神经网络预测不确定性量化这一未解决问题，提出一种后处理（post-processing）方法。该方法利用预训练大模型最后一个隐藏层的输出，将其输入到一个随机神经网络（StoNet）中，并在验证集上施加稀疏惩罚（如L1正则化）进行训练，从而构建未来观测的预测区间。理论部分证明了稀疏StoNet参数估计的一致性，这是该方法有效性的关键；同时表明StoNet框架为将线性模型的稀疏学习理论推广到深度神经网络提供了平台。实验结果显示，该方法能构建出区间长度更短且校准效果优于共形预测及其他事后校准技术的置信区间。对您而言，该工作将高维稀疏估计与深度学习不确定性量化结合，其一致性分析可借助您熟悉的高维渐近工具进行理解或推广。
- **关键技术**: `stochastic neural network`, `sparse regularization`, `post-hoc calibration`, `prediction interval construction`, `parameter estimation consistency`, `post-processing for DNNs`
- **为什么对您有用**: 该论文直接关联到您在高维统计（尤其是稀疏高维估计）方向的兴趣，其理论部分（参数估计一致性）可调用您非常熟悉的高维渐近工具进行审读或改进。由于您对高维渐近已十分熟练，且稀疏惩罚的M估计框架属您中度熟悉的领域，本文可作为中期可做方向：先通过M估计理论熟悉StoNet的训练机制，进而探索能否将高阶U统计量或半参效率思想引入其不确定性量化框架。

### 16. [10.5705/ss.202024.0329](https://doi.org/10.5705/ss.202024.0329) — Efficient Decoding from Heterogeneous 1-Bit Compressive Measurements over Networks
- **作者**: Canyi Chen, Zhengtian Zhu, Liping Zhu
- **期刊/来源**: Statistica Sinica
- **机构**: Tongji University · Renmin University of China
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在去中心化网络设定下，研究从异质 1-bit 压缩感知测量中恢复高维信号的估计问题，estimand 为稀疏信号向量，关键假设为仅允许邻居间局部通信且测量面临 sign flip 与异质性。本文将 1-bit CS 重构为 penalized least squares 问题，据此开发广义 ADMM 算法以实现去中心化优化。理论上证明算法具有线性收敛速率，且在有限次通信后即可达到 near-oracle 统计收敛速率，并在温和条件下可靠恢复信号支撑集。数值实验验证了方法有效性。对您可能有用：该文将 1-bit 降维与去中心化优化结合，其 near-oracle rate 与 minimax 理论可直接对接您的高维统计与 efficiency 理论兴趣。
- **关键技术**: `1-bit compressive sensing`, `generalized ADMM`, `penalized least squares`, `near-oracle convergence rate`, `decentralized optimization`, `support recovery`
- **为什么对您有用**: 本文连接到高维统计与 efficiency 理论子方向，其 near-oracle rate 的声称可用 minimax bound 验证是否紧。用您 very_familiar 的高维渐近理论与 minimax 估计界可直接审视其统计收敛率的 sharpness。**立即可做**：用 minimax 下界工具检验该 near-oracle rate 是否达到高维 1-bit CS 的最优速率。

### 17. [10.5705/ss.202024.0435](https://doi.org/10.5705/ss.202024.0435) — Mixed Membership Network with the Autoregressive Structure
- **作者**: Tianyi Sun, Bo Zhang, Baisuo Jin, Yuehua Wu
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在动态随机块网络设定下，本文提出带一阶自回归结构的混合隶属度网络模型（Mixed Membership AR-1 Network），目标是估计隶属度矩阵与社区检测。核心方法为 AR-1 混合谱聚类算法，结合经验特征值阈值估计器确定社区数 K，利用随机矩阵理论中谱方法对混合隶属度矩阵进行估计。理论贡献在于给出隶属度矩阵估计的显式误差率，并在不同设定下证明该误差率不劣于既有方法；实证与模拟显示其在混合隶属度与纯块结构场景下泛化性更强。对您可能有用：该文的谱聚类与经验特征值阈值直接依赖随机矩阵理论（RMT）的尖峰模型分析，可作为 RMT 在网络动态模型中应用的参考。
- **关键技术**: `mixed membership stochastic blockmodel`, `AR-1 autoregressive network`, `spectral clustering`, `empirical eigenvalue threshold`, `spiked random matrix model`, `community detection`
- **为什么对您有用**: 本文直接连接到 primary interest 中的高维统计与随机矩阵理论（RMT）子方向——经验特征值阈值估计器本质是 RMT 尖峰模型中信号特征值与噪声特征值的分离准则。用您 very_familiar 的高维渐近理论可以审视其谱聚类误差率是否达到 minimax 下界，或用 moderately_familiar 的 M-estimation 理论分析自回归参数与隶属度矩阵联合估计的效率。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以推导联合估计的 semiparametric efficiency bound；若仅关注 RMT 部分的尖峰阈值分析，则立即可做。

## 非参数 / 半参数  *(nonparam_semipara, 37 篇)*

### 1. [10.5705/ss.202024.0256](https://doi.org/10.5705/ss.202024.0256) · [arXiv](https://arxiv.org/abs/2403.04248) — Asymptotic Theory for Linear Functionals of Kernel Ridge Regression
- **作者**: Rui Tuo, Lu Zou
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在 Sobolev 等价 RKHS 设定下，本文研究核岭回归 (KRR) 预测函数的线性泛函（如点评估、导数、L2 内积）的估计理论，关键正则性假设为核与 Sobolev 空间的等价性及光滑度 m。核心发现是：为平衡方差与 worst-case bias，泛函估计的普适最优平滑参数阶为 λ∼n^{-1}，而非已知最小化 KRR L2 误差的 λ∼n^{-2m/(2m+d)}；在此最优 λ 下，作者建立了估计的上下界及渐近正态性，并推得 KRR 的最优 L∞ 误差在 λ∼n^{-1}log n 下可达。对您可能有用：该结果为 RKHS/Sobolev 框架下非参数泛函的 inference 提供了精确的渐近分布与最优 tuning 理论，直接连接到您 primary interest 中的非参数/半参数理论及 efficiency bound 计算。
- **关键技术**: `kernel ridge regression`, `RKHS-Sobolev equivalence`, `linear functional estimation`, `asymptotic normality`, `worst-case bias-variance tradeoff`, `optimal smoothing parameter`
- **为什么对您有用**: 本文直接连接到您 primary interest 的非参数/半参数理论子方向，为 Sobolev-RKHS 框架下的线性泛函 inference 给出了精确的渐近分布与最优 λ 理论。您武器库中 very_familiar 的 nonparametric statistics 与 minimax bounds 完全可用来验证其上下界是否紧，甚至可尝试用 moderately_familiar 的 HOIF 视角审视该泛函估计的 higher-order bias 校正潜力。Follow-up 判断：**立即可做**——用 very_familiar 的 minimax bound 工具即可动手检验其声称的 rate sharpness，或延伸到半参数效率界对比。

### 2. [10.5705/ss.202024.0378](https://doi.org/10.5705/ss.202024.0378) · [arXiv](https://arxiv.org/abs/1705.09599) — Semiparametric Efficient Estimation of Quantile Regression
- **作者**: Zhanfeng Wang, Kani Chen, Yuanyuan Lin, Zhiliang Ying
- **期刊/来源**: Statistica Sinica
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在半参数分位数回归模型下（假设响应变量的分位数与解释变量线性相关，其余分布成分无限维），目标是估计回归分位数系数并推导其半参数效率界。本文首先推导了该模型的半参数有效得分函数及对应的效率下界，明确了传统分位数回归估计量在何种偏离条件下存在效率损失。进而提出了一种具体的半参数有效估计量构造方法，通过估计 nuisance function（条件密度与残差分布）来实现效率提升。模拟实验表明，该方法相比标准分位数回归估计可获得显著的效率增益。对您可能有用：本文为分位数回归设定下的 semiparametric efficiency bound 提供了完整推导，直接补充了您 efficiency theory 与 semiparametric theory 方向的理论储备。
- **关键技术**: `semiparametric efficiency bound`, `efficient score function`, `quantile regression`, `nuisance function estimation`, `conditional density estimation`
- **为什么对您有用**: 直接连接到您 primary interest 中的 efficiency theory（semiparametric efficiency bounds）与 semiparametric theory 子方向，给出了分位数回归这一经典模型的效率界与有效得分函数的显式推导。您武器库中 moderately_familiar 的 semiparametric theory 完全可以攻这篇 paper 的核心口子——验证其 nuisance function 估计路径是否唯一、是否可拓展到高维设定下的 debiased ML 框架。属于**立即可做**：用 very_familiar 的 minimax bounds 与 moderately_familiar 的 semiparametric theory 即可动手探索其高维/无穷维 nuisance 下的效率界是否仍紧。

### 3. [10.5705/ss.202024.0298](https://doi.org/10.5705/ss.202024.0298) · [arXiv](https://arxiv.org/abs/2410.09402) — Minimax Rates of Convergence for Nonparametric Regression Under Adversarial Attacks
- **作者**: Jingfu Peng, Yuhong Yang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在非参数回归设定下，研究输入遭受对抗性攻击（adversarial sup-norm perturbation）时估计的 minimax 收敛速率。目标 estimand 为回归函数，关键假设为输入扰动在 sup-norm 约束下由对手选择。核心发现是：对抗设定下的 minimax rate 等于两项之和——标准无攻击设定下的 minimax rate，加上目标函数类在输入扰动下的最大函数值偏差。作者证明此最优速率可通过“对抗性 plug-in 程序”实现，即直接取标准设定下的 minimax optimal estimator 并做对抗修正，无需新构造。文中给出两个具体函数类（如 Holder 类）的实例以阐明速率表达式。对您有用：本文将 minimax bound 与对抗鲁棒性结合，直接对接您 primary interest 中的 nonparametric minimax theory，且其 plug-in 构造思路可类比 semiparametric efficiency 中的 one-step correction。
- **关键技术**: `minimax convergence rate`, `adversarial sup-norm perturbation`, `nonparametric regression`, `plug-in estimator`, `Holder class`
- **为什么对您有用**: 本文直接对接您 primary interest 中的 nonparametric minimax bounds，将经典 minimax rate 分解为“标准速率+扰动偏差”的形式，与您 very_familiar 的 minimax estimation theory 完全契合。您可用 very_familiar 的 minimax bound 工具验证其速率在更复杂函数类（如 RKHS / Besov）下是否紧，或用 moderately_familiar 的 M-estimation theory 探究对抗设定下 M-estimator 的 influence function 形式。Follow-up 判断：立即可做——用现有 minimax 武器即可推广或验证。

### 4. [10.5705/ss.202025.0144](https://doi.org/10.5705/ss.202025.0144) — Conditional Density Estimation with Deep Neural Networks
- **作者**: Chenxuan He, Yuan Gao, Liping Zhu, Jian Huang
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `sharper_rate`
- **摘要**: 本文研究基于深度神经网络的条件密度估计问题，目标是在非参数设定下估计条件密度函数 f(y|x)，不施加强参数假设。作者将条件密度估计转化为非参数最小二乘问题，利用深度神经网络的逼近能力来求解。理论上证明了该方法在一般非参数设定下达到 minimax 最优收敛速率；进一步，在数据满足低维流形假设时，收敛速率可随维度自适应改善（克服传统非参数方法的维度灾难）。数值实验（模拟与真实数据）表明该方法在精度与鲁棒性上优于多种经典方法。对您而言，本文提供了深度非参数估计的 minimax 理论框架，直接连接到您 primary interest 中的非参数理论与 minimax bound 研究。
- **关键技术**: `nonparametric least squares`, `deep neural network approximation`, `minimax optimal convergence rate`, `manifold adaptive rate`, `conditional density estimation`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的非参数理论与 minimax bound：它给出了深度非参数估计器的 minimax 最优速率证明，且流形自适应速率是高维非参数的经典前沿。用您 very_familiar 的 minimax bounds for estimation problems 武器，可以立刻检验其速率紧性，甚至考虑将此 least-squares 框架与您 moderately_familiar 的 HOIF / semiparametric theory 结合，探索条件密度估计的 semiparametric efficiency bound 或更高阶修正。follow-up 判断：立即可做——用 minimax 与 semipara 理论基础即可展开理论延伸。

### 5. [10.5705/ss.202025.0151](https://doi.org/10.5705/ss.202025.0151) · [arXiv](https://arxiv.org/abs/2310.14419) — Variable Selection and Minimax Prediction in High-dimensional Functional Linear Models
- **作者**: Xingche Guo, Yehua Li, Tailen Hsing
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在超高维函数线性回归设定下（p个函数型协变量，系数函数属于RKHS），目标是变量选择与minimax最优预测。作者提出group elastic-net型惩罚对RKHS范数做正则化，证明损失函数的Gateaux次可微性及估计量在乘积RKHS中的唯一存在性。在稀疏假设与函数型不可表示条件下，导出变量选择一致性的非渐近尾界；允许真实信号维度q随n发散，证明post-selection精炼估计量可达oracle minimax最优预测收敛率。模拟与Human Connectome Project数据验证了方法。对您有用：本文将RKHS正则化与minimax rate结合，直接对接您在nonparametric minimax bounds与semiparametric theory上的核心武器。
- **关键技术**: `RKHS regularization`, `group elastic-net penalty`, `functional irrepresentable condition`, `non-asymptotic tail bound`, `oracle minimax prediction rate`, `Gateaux sub-differentiability`
- **为什么对您有用**: 本文直接连接您primary interest中的nonparametric minimax bounds与semiparametric theory：在函数型RKHS设定下给出了oracle minimax prediction rate的显式刻画。您very_familiar的nonparametric statistics与minimax bounds武器可以直接用来审视其rate的紧性，以及irrepresentable条件是否可进一步弱化。立即可做：用您熟悉的minimax lower bound工具验证其声称的oracle rate是否紧，并探索用HOIF视角改善post-selection估计量的高阶偏差。

### 6. [10.5705/ss.202025.0115](https://doi.org/10.5705/ss.202025.0115) · [arXiv](https://arxiv.org/abs/2602.13538) — Empirical Bayes Data Integration for Multi-Response Regression
- **作者**: Antik Chakraborty, Fei Xue
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多响应回归（multi-response regression）设定下，目标是整合来自不同数据源的向量型结局，estimand 为回归系数矩阵，关键假设为经验 Bayes 先验下的线性收缩结构。核心方法提出对数据矩阵奇异值进行线性收缩的估计器，并将其与特定损失下的协方差矩阵估计问题建立理论联系；进一步扩展为局部线性收缩估计器以提升灵活性。该方法无需稀疏或低秩假设即可工作，突破了传统 sparse / reduced-rank 估计器的设定限制；计算上比全 Bayes 方法更具可扩展性。理论贡献包括在特定损失下给出渐近最优的协方差估计器。对您可能有用：该文的奇异值收缩与协方差估计理论可直接对接您的高维渐近与随机矩阵理论兴趣，局部线性收缩的渐近最优性也可用 minimax bound 视角验证其率是否紧。
- **关键技术**: `empirical Bayes linear shrinkage`, `singular value shrinkage`, `asymptotically optimal covariance estimation`, `local linear shrinkage`, `multi-response regression`
- **为什么对您有用**: 本文直接连接您的高维统计与随机矩阵理论子方向——奇异值收缩是 RMT Marchenko-Pastur 定律的经典应用场景，而渐近最优协方差估计与 minimax rate 紧密相关。您可用 very_familiar 的高维渐近与 minimax bound 武器验证其声称的渐近最优性是否紧，或用 moderately_familiar 的 M-estimation 理论分析局部线性收缩的收敛性质。Follow-up 判断：立即可做——用您已有的高维渐近工具即可展开对其理论率的验证与潜在改进。

### 7. [10.5705/ss.202025.0076](https://doi.org/10.5705/ss.202025.0076) — Nonparametric Inference on Treatment-biomarker Interaction Based on Probability Index
- **作者**: Zehui Wang, Yanglei Song, Wenyu Jiang, Dongsheng Tu
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在精准医学设定下，目标是通过二分 biomarker 的 cutpoint 划分亚组，用概率指数（probabilistic index）定义非参数 treatment-biomarker interaction estimand，检验不同亚组间处理效应差异。当 cutpoint 预先指定时，采用 Wilcoxon-type 统计量检验无交互零假设；当 cutpoint 未指定时，取该统计量在 cutpoint 区间上的 supremum 构造检验，p 值由 bootstrap 计算，两种情形下检验 size 均收敛至名义水平。若未指定 cutpoint 下拒绝零假设，提出 profile estimator 估计使处理效应差异最大化的 cutpoint，证明其收敛速率为 n^{-1/3}（cubic-rate）且渐近服从 scaled Chernoff distribution。进一步引入 m-out-of-n bootstrap 估计渐近分布中的未知 scaling factor。对您可能有用：cutpoint 估计的 cubic-rate 与 Chernoff distribution 是非参数 M-estimation 的经典极值结果，可作为非参数极值点估计理论的参考案例。
- **关键技术**: `probabilistic index model`, `Wilcoxon-type statistic`, `supremum test over cutpoint`, `cubic-rate convergence`, `Chernoff distribution`, `m-out-of-n bootstrap`
- **为什么对您有用**: 本文连接到非参数理论子方向，特别是非参数极值点估计（cubic-rate / Chernoff distribution）与 supremum-type 检验的渐近理论。用您 very_familiar 的 minimax bounds 可以验证其 cubic-rate 是否在该模型下达到 minimax 下界；用 moderately_familiar 的 M-estimation theory 可以审视其 profile estimator 的渐近展开与 m-out-of-n bootstrap 的 validity 论证。follow-up 粗判：**立即可做**——用 minimax 理论与 M-estimation 工具即可审视其收敛速率与 bootstrap 理论的紧性。

### 8. [10.5705/ss.202024.0167](https://doi.org/10.5705/ss.202024.0167) — On Efficient Estimation for Value-at-Risk via Location-Scale Time Series Models
- **作者**: Chaoxu Lei, Qianqian Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 location-scale 时间序列模型框架下研究 Value-at-Risk (VaR) 的高效估计，目标参数为高条件分位数；关键假设为创新项分布半参数或参数化且具有显式分位数函数。提出半参数与参数化 composite quantile regression (CQR) 两种估计器：半参数 CQR 融合多分位数水平信息，无需创新项分布假设即可提升相对于单点 quantile regression 的效率；参数化 CQR 利用分位数函数的参数结构，在数据稀缺的高条件分位数估计中进一步提效。建立两类 CQR 估计器在 ARMA-GARCH、双自回归及 NAR-GARCH 等模型下的渐近性质，推导其渐近方差并与 Gaussian/exponential QMLE 进行效率比较。对您可能有用：本文的半参数 CQR 多分位数融合提效机制与 semiparametric efficiency bound 的视角直接相关，为条件分位数估计的效率理论提供了具体案例。
- **关键技术**: `composite quantile regression`, `location-scale time series`, `semiparametric efficiency`, `asymptotic variance comparison`, `ARMA-GARCH`, `conditional quantile estimation`
- **为什么对您有用**: 本文直接连接到 primary interest 中的 semiparametric & nonparametric theory 和 efficiency theory 子方向，具体讨论了半参数模型下多分位数融合估计的效率提升及其与 QMLE 的渐近方差比较。用 technical_arsenal 中 moderately_familiar 的 semiparametric theory 可以直接攻本文的效率界推导口子，验证其半参数 CQR 是否达到 semiparametric efficiency bound。follow-up 粗判：立即可做——用 very_familiar 的 minimax bounds 工具审视其效率声称是否紧，或用 moderately_familiar 的 M-estimation theory 推导其 influence function。

### 9. [10.5705/ss.202025.0318](https://doi.org/10.5705/ss.202025.0318) · [arXiv](https://arxiv.org/abs/2603.29333) — Semiparametric Analysis for Paired Comparisons with Covariates
- **作者**: Haoyue Song, Lianqiang Qu, Ting Yan, Yuguo Chen
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对配对比较数据（如Bradley-Terry模型及其变体）提出一个半参数分析框架，引入具有未知分布的潜变量来建模项目的优劣和协变量效应（如主场优势），从而放松参数模型对分布形式的假设。当配对比较中项目数量趋于无穷时，参数数量也随之增加，使得半参数推断极具挑战。作者采用基于核的最小二乘估计方法同时估计所有未知参数，并在每对项目比较次数固定、项目数增大时，证明了估计量的一致性并推导出其渐近正态分布。据作者所知，这是首项在高维配对比较设置下进行半参数分析的工作。模拟实验验证了方法的有限样本性能，并通过NBA数据集展示了其实际应用价值。本文对半参数理论与高维渐近分析有直接贡献，尤其适合关注非参数与半参数推断的研究者。
- **关键技术**: `kernel-based least squares`, `semiparametric paired comparison`, `increasing dimension asymptotics`, `latent random variables`, `Bradley-Terry model`, `asymptotic normality`
- **为什么对您有用**: 本文连接了您对半参数理论的兴趣，提出在高维配对比较中利用核方法进行半参数估计。您非常熟悉的非参数统计和核估计技术可以直接用于理解其估计机制，并可进一步评估其minimax最优性。此工作的方法可迁移至其他高维比较模型，属于立即可读并可参与讨论的范畴。

### 10. [10.5705/ss.202025.0389](https://doi.org/10.5705/ss.202025.0389) · [arXiv](https://arxiv.org/abs/2510.18149) — Conformal Inference for Missing Data Under Multiple Robust Learning
- **作者**: Wenlu Tang, Hongni Wang, Xingcai Zhou, Bei Jiang, Linglong Kong
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 Missing at Random (MAR) 设定下，本文研究缺失数据的 conformal prediction 问题，目标是构建边际与条件覆盖均有效的预测区间。核心方法 CM-MRL 将 split conformal calibration 与 multiple robust empirical-likelihood (EL) 重加权结合，对 complete-case scores 进行双重校准，使其分布匹配 MAR 下全样本的校准分布。该方法在多个 working model 部分误设时仍保持分布一致性（multiple robustness），并通过 empirical process theory 证明估计量的渐近性质与预测区间的可靠覆盖，进一步给出区间长度占优结果。数值实验验证了方法在缺失数据下的有效性。对您可能有用：本文将 semiparametric multiple robustness 思想引入 conformal inference，为缺失数据下的分布自由预测提供新路径。
- **关键技术**: `split conformal prediction`, `empirical likelihood reweighting`, `multiple robustness`, `Missing at Random`, `empirical process theory`, `double calibration`
- **为什么对您有用**: 本文连接到 semiparametric efficiency 与 causal inference 中的 multiple robustness 设定，将 EL 重加权与 conformal calibration 结合，是 semiparametric 理论在分布自由预测中的新应用。您武器库中的 M-estimation theory 与 semiparametric theory（moderately_familiar）可直接切入分析其 EL 重加权估计量的渐近性质与 influence function；empirical process theory 的收敛率分析也是您 very_familiar 的高维渐近工具可覆盖的范围。Follow-up 判断：**立即可做**——用 very_familiar 的高维渐近与 moderately_familiar 的 semiparametric theory 即可展开对其 multiple robustness 条件与区间长度占优率的深入验证。

### 11. [10.5705/ss.202025.0478](https://doi.org/10.5705/ss.202025.0478) — Non-parametric Testing for Survival Data with Time-dependent Covariates
- **作者**: Ying Cui, HuiChuan Lai, Limin Peng
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在带时变协变量的生存分析设定下，目标是检验时变协变量（如时变处理或暴露）对生存结局的非参数效应，避免对协变量-生存关系施加参数或半参数模型假设。作者采用 landmark 视角并引入广义区间分位相关指数（generalized interval quantile correlation index），构造了无需指定回归模型形式的非参数检验框架，可灵活容纳协变量效应的动态变化。理论部分证明了检验统计量的渐近性质与检验的一致性。实证方面，将该方法应用于囊性纤维化幼儿前 3 年的时变喂养模式（母乳/配方奶）对关键肺部结局的效应检验。对您可能有用：本文提供了一个在时变协变量生存设定下绕过半参数建模的非参数检验方案，与您在 nonparametric statistics 和 causal inference 中时变处理/暴露的 identification 与 estimation 问题直接相关。
- **关键技术**: `landmark analysis`, `generalized interval quantile correlation index`, `nonparametric hypothesis testing`, `time-dependent covariate`, `survival analysis`, `asymptotic distribution of test statistic`
- **为什么对您有用**: 本文连接到 causal inference 中时变处理/暴露的效应评估以及 nonparametric statistics 中的检验问题。您武器库中 very_familiar 的 nonparametric statistics 和 moderately_familiar 的 identification theory in causal inference 可以直接攻本文的口子：审视其广义区间分位相关指数在时变混杂下的 identification 能力，以及检验统计量的渐近分布推导是否可借用您熟悉的 minimax bounds 或 higher-order U-statistics 投影技术来获得更紧的 power 分析。Follow-up 粗判：立即可做——用 very_familiar 的非参数检验与 minimax 理论即可审视其检验的 optimality 与时变因果 identification 的局限。

### 12. [10.5705/ss.202025.0305](https://doi.org/10.5705/ss.202025.0305) — Semiparametric Regression Analysis of Clustered Interval-censored Failure Time Data with Random Change Points and Application to Breast Cancer Study
- **作者**: Yichen Lou, Mingyue Du, Jianguo Sun
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对聚类区间删失失效时间数据，在存在随机变更点的情况下提出半参数回归方法。研究背景是国际乳腺癌研究中疾病风险可能因生物标志物阈值而突变。方法采用筛极大似然估计（sieve MLE）同时处理聚类结构、区间删失和随机变更点三个特征。估计使用EM算法实施，并建立了估计量的相合性和渐近正态性。大量模拟表明方法在有限样本下表现良好，并应用于乳腺癌研究实例。本文为半参数筛估计在复杂数据结构中的应用提供了理论保证和计算框架。对于您的半参数理论兴趣，该文展示了筛M估计在非标准设定下的渐近分析，对您moderately_familiar的M估计理论和半参数理论有参考价值。
- **关键技术**: `sieve maximum likelihood estimation`, `EM algorithm`, `interval-censored failure time data`, `random change points`, `clustered data`, `semiparametric regression`
- **为什么对您有用**: 本文属于半参数理论中筛估计在生存数据上的方法扩展，直接关联您的semiparametric & nonparametric theory兴趣。您当前武器库中的M-estimation theory（moderately_familiar）可用于理解其筛MLE的渐近论证，并评估该方法在更广设定下的效率损失。中期可做：需先在moderately_familiar的M-estimation理论（尤其是筛估计的收敛速率）上加深，方可复现或改进其理论分析。

### 13. [10.5705/ss.202025.0295](https://doi.org/10.5705/ss.202025.0295) — Inference on Two-Sample Covariance Difference for Large-Scale Functional Data
- **作者**: Kaijie Xue, Lan Xue, Riquan Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在两样本大规模函数数据设定下，目标是推断协方差差异矩阵，不施加结构约束或严格分布假设。核心方法是基于 multiplier bootstrap 构建协方差差异的置信域，而非仅做检验，从而同时获得更优的检验功效与一致的估计功效函数。该方法具有 eigenvalue-decay-free 与 square-integrable-free 特性，避免了传统函数数据推断对谱衰减率或平方可积性的依赖。理论上证明了置信域的覆盖概率收敛与功效函数在广泛备择假设下的一致性。实证通过模拟与真实数据验证了数值表现。对您可能有用：此文的 bootstrap 置信域构造与高维/函数数据下的弱假设推断，直接连接到您的高维渐近理论与非参数检验方向。
- **关键技术**: `multiplier bootstrap`, `functional data covariance inference`, `confidence region construction`, `eigenvalue-decay-free condition`, `estimated power function consistency`
- **为什么对您有用**: 本文直接连接到您的高维渐近理论与非参数统计方向，特别是函数数据协方差推断中放宽谱衰减假设的设定。您武器库中的 very_familiar 项（高维渐近理论与 minimax bounds）可直接用来审视本文声称的 eigenvalue-decay-free 条件是否真正达到了 minimax sharp rate，或是否存在更紧的下界。follow-up 判断：立即可做——用 minimax bound 与高维渐近工具即可验证其收敛率是否紧，并探索该 multiplier bootstrap 在更一般高维协方差差异设定下的扩展。

### 14. [10.5705/ss.202024.0402](https://doi.org/10.5705/ss.202024.0402) — Robust Mean Signal Estimation and Inference for Imaging Data
- **作者**: Yang Long, Guanqun Cao, David Kepplinger, Lily Wang
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究被污染的成像数据（视为 contaminated functional data）在非规则区域上的均值信号估计与推断问题，目标是均值函数及其显著性区域的 detection/localization。作者提出基于三角剖分上 bivariate penalized splines 的 robust and smoothed M-estimator，以同时应对数据污染、空间依赖与不规则区域。在 regularity 条件下证明了该 M-estimator 的 L2 收敛性与渐近正态性，并据此构造了均值信号的 simultaneous confidence corridor (SCC)。模拟与脑成像实证表明该方法在污染设定下优于传统非稳健方法。对您有用：本文在非参数 M-estimation 理论与 SCC 构造上的框架，可直接迁移至您关注的 inverse problems with random noise 与非参数推断场景。
- **关键技术**: `bivariate penalized splines over triangulation`, `robust smoothed M-estimation`, `L2 convergence rate`, `asymptotic normality`, `simultaneous confidence corridor`, `contaminated functional data`
- **为什么对您有用**: 直接连接非参数理论（primary interest）与脑成像实证（epidemiology secondary interest）中的 inverse problems with random noise 设定。您武器库中 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 M-estimation theory 完全覆盖本文的理论工具，可直接审视其 L2 rate 与渐近正态性证明的紧致性。follow-up 判断：立即可做——可用 minimax bounds 验证其收敛率是否达到最优，或用 higher-order U-statistics / HOIF 视角探索其 SCC 构造在更高阶下的 sharper rate 可能。

### 15. [10.5705/ss.202025.0221](https://doi.org/10.5705/ss.202025.0221) — Nonparametric Shrinkage Estimation in High Dimensional Glms via Polya Trees
- **作者**: Asaf Weinstein, Jonas Wallin, Daniel Yekutieli, Malgorzata Bogdan
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在高维广义线性模型（GLM）中提出了一种非参数收缩估计方法，目标是对固定效应系数向量进行正则化。首先定义了一个理想的oracle贝叶斯估计量，其先验对系数向量的所有排列赋予相同权重，只依赖于系数的经验分布函数，并证明了该oracle估计量在频率和贝叶斯框架下的某些最优性。为了逼近这个oracle，作者采用分层贝叶斯模型：假定各系数独立同分布于一个共同分布，并对该共同分布赋予Polya树先验以表达不确定性。后验均值能够非参数地自适应于真实系数的经验分布，从而模仿oracle估计量。数值实验表明，该方法在估计和预测精度上优于多种参数和非参数替代方法，包括Lp正则化、现代惩罚似然以及贝叶斯高维回归方法。本文与您的高维统计兴趣直接相关，提供了一种非参数贝叶斯正则化思路，可用您熟悉的minimax理论考察其最优性是否紧。
- **关键技术**: `Polya tree prior`, `hierarchical Bayes`, `permutation-invariant prior`, `shrinkage estimation`, `high-dimensional GLM`
- **为什么对您有用**: 本文涉及高维统计中的收缩估计问题，与您的非参数理论和高维渐近兴趣直接相连。您可以用熟悉的minimax bounds工具分析该方法的理论最优性（例如确认其自适应速率是否达到最优），而非参数贝叶斯方法（Polya tree）当前不在您的武器库中，属于**中期可做**——需要先在贝叶斯非参数（尤其是Polya tree和Dirichlet过程混合）上提升熟悉度，才能深入评估或改进其理论保证。

### 16. [10.5705/ss.202025.0057](https://doi.org/10.5705/ss.202025.0057) — Robust Jackknife Model Averaging
- **作者**: Kang You, Miaomiao Wang, Guohua Zou
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在大数据含异常值的设定下，传统基于最小二乘或极大似然的模型平均方法会严重退化，本文提出鲁棒 Jackknife 模型平均（RJMA）方法，通过最小化 leave-one-out 交叉验证准则选择权重，候选模型维度可随样本量增长。核心理论结果包括：RJMA 权重估计量的渐近最优性（最小化 out-of-sample final prediction error）与对理论最优权重向量的一致性；当候选集包含正确模型时，RJMA 将全部权重分配给正确模型，实现模型平均估计的一致性。此外，本文推导了 RJMA 估计量的 influence function，并引入 empirical prediction influence function 以量化其鲁棒性。对您可能有用：influence function 的推导与鲁棒性量化直接对接 semiparametric efficiency / influence function 理论，而 leave-one-out CV 权重选择机制与 higher-order U-statistic 的投影分析有潜在联系。
- **关键技术**: `jackknife model averaging`, `leave-one-out cross-validation`, `influence function`, `asymptotic optimality`, `robust M-estimation`
- **为什么对您有用**: 本文直接对接 semiparametric theory 中的 influence function 工具，将其用于量化模型平均估计量的鲁棒性，这是您 moderately_familiar 中 semiparametric theory 的直接应用场景。RJMA 的 leave-one-out CV 准则本质上是 U-statistic 结构，您 very_familiar 的 higher-order U-statistic / treewidth 视角可用来分析该准则的计算复杂度与高阶投影性质。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格处理鲁棒损失函数下的 M-estimator 渐近理论，随后可用 U-statistic 工具深化其计算与理论分析。

### 17. [10.5705/ss.202025.0398](https://doi.org/10.5705/ss.202025.0398) · [arXiv](https://arxiv.org/abs/2510.20541) — Bootstrap Consistency for Empirical Likelihood in Density Ratio Models
- **作者**: Weiwei Zhuang, Weiqi Yang, Jiahua Chen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在密度比模型（DRM）框架下，本文研究经验似然（EL）估计量的 bootstrap 一致性问题，目标是证明 bootstrap 最大 EL 估计量与总体对应估计量具有相同的极限分布。核心机制在于将已有的逐点收敛理论拓展至过程的弱收敛（weak convergence of processes），从而为分布泛函、分位数及优势指数（dominance indices）的 bootstrap 推断提供严格的理论保证。技术路径依赖经验过程理论与 EL 的非参数推断性质，填补了 DRM 下 resampling 推断的理论空白。模拟实验验证了所提 bootstrap 置信区间与假设检验的精度。对您可能有用：本文的过程弱收敛结果与 EL 推断框架，可直接服务于 semiparametric efficiency 与 M-estimation 理论下的 bootstrap 推断需求。
- **关键技术**: `empirical likelihood`, `density ratio model`, `bootstrap consistency`, `weak convergence of empirical processes`, `distribution functional inference`
- **为什么对您有用**: 本文直接连接到 semiparametric theory 与 M-estimation 理论子方向，为密度比模型下的 EL 推断补上了 resampling 理论缺口。用 technical_arsenal 中 very_familiar 的 M-estimation theory 与 moderately_familiar 的 semiparametric theory 即可审视其过程弱收敛证明的细节与边界条件。属于**立即可做**：可用现有武器评估其 bootstrap 一致性条件是否可进一步放松或拓展至高维/缺失数据设定。

### 18. [10.5705/ss.202025.0207](https://doi.org/10.5705/ss.202025.0207) — A Model-free Correlation Coefficient for Censored Data
- **作者**: Linlin Dai, Tengfei Li, Kani Chen
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据设定下，本文提出一种无模型依赖的依赖性度量及其估计量 CRC（censored rank-based correlation coefficient），目标 estimand 取值于 [0,1]，当且仅当变量独立或存在可测函数关系时取 0 或 1。CRC 基于 rank 构造，不依赖变量分布，计算复杂度为 O(n log n)，能检测非线性与非单调关联。理论方面，CRC 在重删失下仍具有强相合性与渐近正态性；独立性检验的 p 值通过 power-consistent 的 permutation 方法获得。模拟与 ADNI 实际数据表明，CRC 在检测非线性关联上优于 Cox 模型及其他方法。对您可能有用：CRC 的渐近正态性证明与 permutation 检验的 power 分析涉及非参数统计与假设检验理论，可作为删失数据下无模型相关性检验的参考方法。
- **关键技术**: `rank-based correlation coefficient`, `right-censored data dependence measure`, `permutation test for independence`, `asymptotic normality under censoring`, `model-free association measure`
- **为什么对您有用**: 本文连接到非参数统计与假设检验子方向：CRC 的渐近正态性与 permutation 检验 power-consistency 的严格证明，可用您 very_familiar 的非参数统计与 minimax bound 工具审视其收敛率是否可达最优。follow-up 判断：**立即可做**——用 minimax 理论验证该 dependence measure 在特定删失机制下的 estimation lower bound，并考察 permutation 检验在局部替代假设下的 power 行为。

### 19. [10.5705/ss.202025.0120](https://doi.org/10.5705/ss.202025.0120) · [arXiv](https://arxiv.org/abs/2503.16007) — Estimation of Piecewise Continuous Regression Function in Finite Dimension using Oblique-axis Regression Tree with Applications in Image Denoising
- **作者**: Subhasish Basak, Anik Roy, Partha Sarathi Mukherjee
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在固定设计的有限维回归设定下，目标是估计具有分段连续结构（含跳跃位置曲线 JLC）的回归函数，传统决策树仅适用于连续或分段常数函数，无法保留 JLC 的复杂形状。本文提出 Oblique-axis Regression Tree (ORT)，通过递归树分区对局部像素强度聚类，并在叶节点仅做局部平均来估计给定像素的回归值。理论分析采用与经典回归树文献不同的假设体系与证明框架，以适应分段连续函数的结构。数值实验（尤其是图像去噪）表明该方法在有效去噪的同时能保留复杂的边缘结构。对您可能有用：本文的非参数树估计与跳跃曲线保留机制，可为非参数统计中分段结构估计的 minimax rate 分析提供新的模型设定参考。
- **关键技术**: `oblique-axis regression tree`, `piecewise continuous regression`, `jump location curve preservation`, `recursive tree partitioning`, `local leaf-only averaging`, `fixed design regression`
- **为什么对您有用**: 本文连接到非参数统计与估计理论子方向，其分段连续函数与 JLC 的估计设定是经典非参数 minimax 理论较少覆盖的模型。您可用 very_familiar 的 minimax bounds for estimation problems 工具审视其声称的估计精度是否达到该函数类的最优收敛率，或用 moderately_familiar 的 M-estimation theory 检视其树分区与局部平均的 M-估计收敛证明。Follow-up 粗判：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立该 ORT 估计量的严格渐近理论并推导 minimax 下界。

### 20. [10.5705/ss.202025.0069](https://doi.org/10.5705/ss.202025.0069) · [arXiv](https://arxiv.org/abs/2111.03223) — Quantile Index Regression
- **作者**: Yingying Zhang, Qianqian Zhu, Yuefeng Si, Guodong Li
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对尾部高阶分位数估计中数据稀疏的难题，提出了一种灵活的尾部参数结构——分位数指数回归模型。该模型通过分位数指数将不同分位水平上的系数联系起来，使得可以利用中部丰富观测数据估计参数，再外推至极端分位数。估计采用复合分位数回归方法，确保不同分位数曲线不交叉。理论部分建立了低维协变量下估计量的渐近正态性，以及高维协变量下的非渐近误差界。模拟和实证表明该模型能有效改善尾部估计的稳定性。对您而言，该工作直接涉及高维统计和非参数回归，其中高维误差界的结果可用您熟知的minimax界工具检验是否紧致，而复合分位数方法与U-统计量的联系值得深挖。
- **关键技术**: `composite quantile regression`, `non-crossing quantile estimators`, `asymptotic normality`, `non-asymptotic error bounds`, `high-dimensional covariates`, `tail extrapolation`
- **为什么对您有用**: 直接关联您的高维统计学兴趣，特别是高维协变量下的非渐近误差界——您可以用minimax下界工具检验其最优性。分位数指数回归的估计问题也可转入半参数视角，用您中等熟悉的半参理论分析其效率。结合您对非参统计的熟悉，本文的尾部参数结构是否过于刚性值得考察，属于**中期可做**：需先在高维分位数回归的局部一致收敛理论上补充火力。

### 21. [10.5705/ss.202024.0358](https://doi.org/10.5705/ss.202024.0358) — Estimation and Model Selection Procedures in Generalized Functional Partially Additive Hybrid Model with Diverging Number of Covariates
- **作者**: Yanxia Liu, Zhihao Wang, Yu Zhen, Wolfgang K. Härdle, Maozai Tian
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究广义函数部分可加混合模型(GFPAHM)，其中解释变量包含带测量误差的无限维函数型预测变量和高维标量协变量，后者对响应的影响是非线性的。目标是同时估计系数并选择重要的可加成分，而现有工作多限于函数型线性模型。作者提出非凸惩罚似然估计方法，在协变量维数随样本量发散的情况下进行变量选择和估计。理论方面，建立了收缩估计量的渐近性质，包括变量选择一致性和估计收敛速率。通过蒙特卡洛模拟验证了方法在中等样本量下的有效性，并应用于饼干面团数据集。该工作将半参数非参数理论拓展至函数型数据与高维协变量结合的场景，对您在半参数理论和高维统计的兴趣具有直接参考价值。
- **关键技术**: `nonconvex penalized likelihood`, `functional data analysis`, `generalized partially additive model`, `variable selection`, `asymptotic theory`
- **为什么对您有用**: 本文直接切入您在半参数非参数理论和高维统计方面的兴趣，尤其是函数型数据与高维协变量联合建模这一子方向。您武器库中 nonparametric statistics 和 high-dimensional asymptotics 这两项 very_familiar 工具可直接用于检验其估计量的 minimax 最优性——这是立即可做的工作。

### 22. [10.5705/ss.202025.0044](https://doi.org/10.5705/ss.202025.0044) · [arXiv](https://arxiv.org/abs/2411.13822) — High-dimensional Extreme Quantile Regression
- **作者**: Yiwei Tang, Huixia Judy Wang, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维协变量（维度随样本量增长）下的极端条件分位数估计问题，提出了一套结合极值理论外推策略与正则化回归的新方法。现有方法在固定协变量数场景下有效，但在高维场景下失效。作者构造了基于分位数回归与极值尾部模型的估计量，利用稀疏性假设控制维度增长，并给出了估计量的渐近性质（收敛速度、极限分布）。通过模拟实验，显示新方法在维度较高时显著优于传统极值分位数回归。最后应用于汽车保险理赔数据，说明方法在极端损失预测与变量选择中的实用性。本文对您可能有用：其高维渐近理论可以直接衔接您武器库中的“high-dimensional asymptotics”工具，非参数极值建模部分也与“semiparametric theory”领域相关。
- **关键技术**: `extreme value theory`, `high-dimensional quantile regression`, `regularized estimation`, `extrapolation strategy`, `high-dimensional asymptotic analysis`, `variable selection`
- **为什么对您有用**: 本文归属于高维统计中的极值分位数回归子方向，与您对 high-dimensional statistics 和 semiparametric & nonparametric theory 的兴趣直接相关。您武器库中的“high-dimensional asymptotics”完全可以用来检验其渐近结论的严谨性，同时“minimax bounds for estimation problems”可用来评判其收敛速率是否最优。关于follow-up粗判：**立即可做**——本文的渐近框架基于经典高维正则化理论，利用您已熟悉的渐近分析工具即可深入理解其理论贡献并评估改进空间。

### 23. [10.5705/ss.202024.0234](https://doi.org/10.5705/ss.202024.0234) · [arXiv](https://arxiv.org/abs/2405.05459) — Estimation and Inference of Change Points in Functional Regression Time Series
- **作者**: Shivam Kumar, Haotian Xu, Haeran Cho, Daren Wang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究函数线性回归模型中斜率函数发生变化的变点估计与推断问题。假设函数型协变量和误差项均允许时间依赖和重尾分布，目标是在未知位置分段常数斜率函数下进行变点检测。提出一种基于再生核希尔伯特空间（RKHS）的函数回归二元分割（FRBS）算法，利用分段常数函数线性回归的预测能力，实现多个变点的计算高效且一致的检测。进一步设计精炼步骤改善初始估计的定位率，并在两种不同变化幅度机制下推导精炼估计量的渐近分布。基于极限分布构造置信区间，同时提出一致性的块状长期方差估计量。模拟实验和S&P 500指数数据分析验证了方法的有效性。该工作连接至半参数非参数理论和高维推断，并且其变点推断框架为您的统计假设检验兴趣提供了具体应用场景。
- **关键技术**: `Functional Regression Binary Segmentation`, `Reproducing Kernel Hilbert Space`, `piecewise constant functional linear regression`, `block-type long-run variance estimator`, `asymptotic distribution of change point estimators`
- **为什么对您有用**: 本文属于非参数半参数理论的变点推断问题，直接连接您的 semiparametric & nonparametric theory 和 hypothesis testing 兴趣。您的 very_familiar 非参数统计学和高维渐近工具能立即理解其变点定位率的理论推导和分块方差估计的收敛性，属于立即可做的范畴。此外，其基于 RKHS 的分段常数回归思想可为后期在因果推断（如结构变点）中拓展提供切入点。

### 24. [10.5705/ss.202024.0414](https://doi.org/10.5705/ss.202024.0414) · [arXiv](https://arxiv.org/abs/2402.15442) — GROS: A General Robust Aggregation Strategy
- **作者**: Alejandro Cholaquidis, Emilien Joly, Leonardo Moreno
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在一般度量空间设定下，本文提出了一种名为 GROS 的鲁棒聚合策略，目标是对任意度量空间中的估计量进行鲁棒组合，核心假设是分组估计量满足次高斯尾。方法借鉴 median-of-means：将样本分为 K 组并在各组计算估计量，随后在度量空间中通过最小化某种距离进行鲁棒聚合；作者证明该估计量具有次高斯性并给出了 Donoho 意义下的 breakdown point。关键理论结果：将最小化域从整个度量空间限制到样本点集上，所得估计量的次高斯常数仅相差一个常数因子，从而使 GROS 在计算上可行。模拟涵盖 k-means 分类、多臂老虎机、回归、噪声下的集合估计及鲁棒持久图。对您可能有用：GROS 在集合估计与持久图上的应用为非参数拓扑数据分析提供了鲁棒估计路径，其 breakdown point 与次高斯界分析可连接到 minimax bound 与 M-estimation 理论。
- **关键技术**: `median-of-means`, `sub-Gaussian concentration`, `Donoho breakdown point`, `metric space minimization`, `robust persistent diagram`, `set estimation under noise`
- **为什么对您有用**: 本文直接连接到非参数统计与 minimax bounds 子方向：GROS 在一般度量空间中给出次高斯收敛与 breakdown point，属于鲁棒 M-estimation 的泛化框架。用您 very_familiar 的 minimax bounds 工具可以验证其声称的次高斯常数是否紧，或探究 K 分组策略下的 minimax lower bound；用 moderately_familiar 的 M-estimation 理论可分析其限制到样本集最小化的渐近性质。Follow-up 判断：立即可做——用 minimax 与 M-estimation 武器即可展开理论验证与界紧性分析。

### 25. [10.5705/ss.202025.0060](https://doi.org/10.5705/ss.202025.0060) — Distributed Focused Information Criterion and Focused Frequentist Model Averaging for Massive Data
- **作者**: Yifan Zhang, Xiaolin Chen, Yuzhan Xing
- **期刊/来源**: Statistica Sinica
- **机构**: Qufu Normal University
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在局部渐近框架下，本文研究线性回归模型中针对聚焦参数的分布式 FIC 与聚焦频率模型平均估计，设定为大规模分块数据且候选模型集固定。核心机制是三种 divide-and-conquer 系数估计（one-shot 与两种迭代），据此构造分布式 FIC 与数据驱动权重的模型平均估计器。理论结果给出了各候选模型下分布式估计器及模型平均估计器的渐近分布，并严格推导了 MSE 上界；权重选择基于最小化聚焦参数的局部渐近 MSE。对您可能有用：分布式模型平均的 MSE 上界推导涉及 M-estimation 渐近理论与 semiparametric 局部渐近框架，与您在 semiparametric efficiency 与 M-estimation 方向的积累直接相关。
- **关键技术**: `local asymptotic framework`, `focused information criterion (FIC)`, `frequentist model averaging`, `divide-and-conquer estimation`, `MSE upper bound derivation`, `data-driven weighting`
- **为什么对您有用**: 本文连接到 semiparametric / M-estimation 子方向：局部渐近框架下的模型平均权重优化本质是 semiparametric 局部渐近效率问题，MSE 上界推导直接调用 M-estimation 渐近理论。您武器库中 moderately_familiar 的 M-estimation theory 可直接攻本文渐近分布与 MSE 界的推导口子，验证其上界是否紧。Follow-up 判断：**立即可做**——用 very_familiar 的高维渐近与 minimax bound 工具检查其分布式 MSE 上界在高维设定下是否仍紧，并探索是否可用 HOIF 改进局部渐近 MSE 界。

### 26. [10.5705/ss.202025.0294](https://doi.org/10.5705/ss.202025.0294) — Estimation of Conditional Extremiles in Reproducing Kernel Hilbert Spaces with Application to Large Commercial Banks Data
- **作者**: Fang Chen, Caixing Wang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在多协变量非参数设定下，本文研究条件 extremile（一种对极端尾部敏感的谱风险度量）的估计问题，目标 estimand 为给定协变量下的条件 extremile 函数。核心方法将 RKHS 与分位数回归过程近似结合：先在 RKHS 中建模条件分位数，再通过分位数-extremile 转换映射到条件 extremile，利用 RKHS 的正则化实现重尾分布下的可靠外推。理论贡献为建立估计误差的非渐近误差界（non-asymptotic error bound），在重尾假设下给出显式收敛率。实证部分应用于大型商业银行数据，展示尾部风险预测效果。对您有用：本文在非参数理论框架下处理重尾条件 extremile，其 RKHS 正则化与非渐近界的技术路线与您熟悉的 minimax bound 及非参数统计工具直接对接。
- **关键技术**: `conditional extremile estimation`, `reproducing kernel Hilbert spaces (RKHS)`, `quantile regression process approximation`, `non-asymptotic error bound`, `heavy-tailed extrapolation`, `spectral risk measure`
- **为什么对您有用**: 本文直接连接非参数理论（primary interest），具体在 RKHS 框架下做条件 extremile 估计并给出非渐近界，与您 very_familiar 的 minimax bounds 与非参数统计高度契合。您可用 minimax 理论审视其非渐近界是否达到极小极大最优率，或用 moderately_familiar 的 semiparametric theory 探究该估计的效率性质（如是否可构造 efficient influence function）。Follow-up 判断：立即可做——用 minimax lower bound 验证其收敛率紧性，并尝试构造 one-step / debiased 版本提升效率。

### 27. [10.5705/ss.202024.0181](https://doi.org/10.5705/ss.202024.0181) · [arXiv](https://arxiv.org/abs/2504.12496) — Mean Independent Component Analysis for Multivariate Time Series
- **作者**: Chung Eun Lee, Zeda Li
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文在多元时间序列设定下提出 mean independent component analysis (mean ICA)，目标是寻找同期线性变换以提取一维均值独立成分，使各成分可独立建模，从而降低参数空间；核心假设是不依赖特定参数模型或分布假设。估计方法基于 martingale difference divergence (MDD) 最小化跨成分与跨时间的均值依赖，适用于固定维度与发散维度两种情形，并扩展至 group mean ICA 以利用分组结构。理论贡献包括固定与发散维度下估计量的一致性证明，以及未知分组结构的可识别性方法。实证通过模拟与社区流动真实数据展示方法有效性。对您可能有用：MDD 作为非参数均值依赖度量，与您熟悉的非参数统计及高维渐近理论直接对接，且发散维度下的渐近分析可视为 semiparametric M-estimation 的一个实例。
- **关键技术**: `mean independent component analysis`, `martingale difference divergence`, `diverging dimension asymptotics`, `group structure identification`, `nonparametric dependence measure`
- **为什么对您有用**: 本文连接到非参数统计与高维渐近理论子方向：MDD 是纯非参数的均值依赖度量，无需分布假设，其发散维度下的 consistency 分析涉及您 very_familiar 的高维渐近与 minimax 界工具。用您 very_familiar 的 minimax bounds 工具可验证发散维度下估计量的收敛率是否达到极小极大最优；用 moderately_familiar 的 M-estimation theory 可审视其一致性证明的 regularity 条件是否可进一步放松。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以推导发散维度下更精细的渐近分布与 semiparametric efficiency bound。

### 28. [10.5705/ss.202024.0003](https://doi.org/10.5705/ss.202024.0003) — Rank-Based Inference for the Accelerated Failure Time Model with Partially Interval-Censored Data
- **作者**: Taehwa Choi, Sangbum Choi, Dipankar Bandyopadhyay
- **期刊/来源**: Statistica Sinica
- **机构**: Sungshin Women's University · Virginia Commonwealth University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对部分区间删失数据下的加速失效时间（AFT）模型，提出了一套统一的基于秩的推断方法。通过构造Gehan型单调估计方程（与加权log-rank检验等价），将估计转化为线性规划问题，从而获得回归系数估计，避免了传统似然方法中对残差分布进行复杂的非参数估计。借助标准经验过程理论，证明了估计量的一致性和渐近正态性，并给出了显式的方差估计程序。此外，该方法还被扩展到多元聚类部分区间删失数据，适用于相依失效时间情境。仿真实验和结直肠癌数据实例验证了方法的有限样本表现。该方法属于半参数模型中的秩估计，其渐近理论依赖于经验过程，与您对非参数统计和假设检验的兴趣直接相关。
- **关键技术**: `Rank-based estimation`, `Gehan-type estimating function`, `Empirical process theory`, `Linear programming optimization`, `Extension to clustered data`
- **为什么对您有用**: 本文的核心方法基于非参数秩检验思想，直接联系您对假设检验和非参数理论的兴趣（primary interests）。您非常熟悉的经验过程理论（nonparametric statistics 中的核心工具）可直接用于验证和扩展该方法的渐近性质，而您在 semiparametric theory 方面的积累可用于考察该秩估计量是否达到半参效率界。立即可做：利用已有的经验过程和非参数统计工具可复现并扩展该估计程序至其他删失类型。

### 29. [10.5705/ss.202025.0266](https://doi.org/10.5705/ss.202025.0266) · [arXiv](https://arxiv.org/abs/2505.22289) — Network Model Averaging Prediction for Latent Space Models by K-fold Edge Cross-Validation
- **作者**: Yan Zhang, Jun Liao, Xinyan Fan, Kuangnan Fang, Yuhong Yang
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在网络数据（单层/多层）的 latent space model 框架下，当网络规模较小而真实潜空间维度较大时，参数估计不稳定，目标是提升 link prediction 的精度。本文提出 NetMA（Network Model Averaging）方法，对不同维度的 latent space candidate models 进行 K-fold edge cross-validation 权重分配。理论证明：在最小化 prediction loss 意义下，NetMA 达到 asymptotic optimality；当 candidate models 包含正确模型时，权重全分配给正确模型（即 achieving model selection consistency）；且 NetMA 权重估计量一致收敛至最优权重向量。模拟与实证（合作网络/虚拟事件网络）显示，NetMA 优于简单平均与模型选择，在潜空间维度较大时甚至超越 oracle。对您可能有用：model averaging 的 asymptotic optimality 与 weight consistency 理论与您熟悉的 minimax bounds 及 M-estimation 理论直接相通。
- **关键技术**: `latent space model`, `K-fold edge cross-validation`, `model averaging`, `asymptotic optimality`, `weight consistency`, `link prediction`
- **为什么对您有用**: 本文核心落在 model averaging 的理论性质（asymptotic optimality 与 weight consistency），与您 primary interest 中的 semiparametric / nonparametric theory 及 minimax estimation 理论直接对话。用您 very_familiar 的 minimax bounds 视角可以审视其 asymptotic optimality 界是否紧；用 moderately_familiar 的 M-estimation 理论可以分析其 weight estimator 的收敛条件是否可进一步放松。**中期可做**：需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以将现有 weight consistency 结果推广至更一般的 semiparametric candidate models 场景。

### 30. [10.5705/ss.202025.0466](https://doi.org/10.5705/ss.202025.0466) — Out-of-cluster Prediction for Model Selection in Regression with Unsupervised Clustering
- **作者**: Masao Ueki
- **期刊/来源**: Statistica Sinica
- **机构**: RIKEN Center for Advanced Intelligence Project
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在无监督聚类回归（如 K-means + 分组回归）设定下，目标是选择聚类数 K 及排除冗余模型，核心假设是不同簇的回归系数存在差异。本文提出利用簇间预测（out-of-cluster prediction）精度低于簇内预测的特性，构建模型排除程序，在 AIC/BIC 选择前剔除冗余模型。针对 Cox 回归中标准 partial log-likelihood 在跨簇预测时发散的问题，提出 normalized partial log-likelihood 替代。理论证明 AIC 结合该排除程序可实现模型选择一致性（selection consistency），仿真覆盖线性、logistic 及 Cox 回归。对您可能有用：该排除程序的 consistency 证明涉及 M-estimation 与似然理论，可作为 semiparametric M-estimation consistency 的具体案例阅读。
- **关键技术**: `unsupervised clustering regression`, `out-of-cluster prediction`, `model exclusion procedure`, `normalized partial log-likelihood`, `model selection consistency`, `AIC/BIC for cluster number`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 中的 M-estimation consistency 子方向，以及 causal inference 中 latent subgroup / mixture regression 的模型选择问题。用 very_familiar 中的 M-estimation theory 可以直接审视其 consistency 证明的 regularity 条件是否过强，或用 moderately_familiar 的 semiparametric theory 检查 normalized partial log-likelihood 的效率性质。follow-up 判断：**立即可做**——用 M-estimation 理论工具即可分析其排除程序的渐近性质。

### 31. [10.5705/ss.202025.0196](https://doi.org/10.5705/ss.202025.0196) · [arXiv](https://arxiv.org/abs/2505.09043) — Exploratory Hierarchical Factor Analysis with an Application to Psychological Measurement
- **作者**: Jiawei Qiao, Yunxiao Chen, Zhiliang Ying
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 在 hierarchical factor model（含 bifactor 为特例）设定下，目标是从数据中可学习地恢复 factor loading matrix 上的层级零约束结构，当前默认的 Schmid-Leiman transformation 被指出有缺陷且易失败。本文首先建立一般 hierarchical factor model 的 identifiability 理论，证明在 mild regularity 条件下层级结构可被学习。其次提出 divide-and-conquer 的计算方法来恢复该结构，计算效率高。最后建立渐近理论，证明所提方法随样本量趋于无穷时可一致恢复真实的层级因子结构。模拟与人格测试真实数据验证了方法表现。对您可能有用：其 identifiability 理论与 consistent structure recovery 的渐近分析为 semiparametric M-estimation 中的结构学习提供了新视角。
- **关键技术**: `hierarchical factor model identifiability`, `divide-and-conquer structure learning`, `bifactor model`, `Schmid-Leiman transformation`, `consistent structure recovery`
- **为什么对您有用**: 本文连接到 semiparametric / nonparametric theory 中的结构识别与估计问题，其 identifiability 理论与 consistent recovery 渐近分析可被您 very_familiar 的 minimax bounds 与 moderately_familiar 的 M-estimation theory 工具审视——例如用 M-estimation 理论验证其 divide-and-conquer 步骤的局部渐近性质是否可整合为全局效率界。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以审视其分步估计的渐近效率是否达到 semiparametric efficiency bound。

### 32. [10.5705/ss.202024.0371](https://doi.org/10.5705/ss.202024.0371) — On a Flexible Generalized Model Averaging Forecasting of Nonlinear Time Series
- **作者**: Rong Peng, Zudi Lu, Fangsheng Ge
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 针对非线性时间序列预测中的维数灾难与非高斯特征，提出了半参数广义边际预测模型平均（GMAFMA）框架，在条件指数族分布下统一处理连续/离散响应。方法通过半参数条件似然估计各边际预测模型的组合权重，并建立渐近正态性（mild时间序列依赖条件下）。进一步引入自适应惩罚版（PGMAFMA）筛选重要边际模型，提升可解释性与预测精度。核心机制是将多个单变量非参数预测视为候选，用似然加权融合，避免高维非参数回归。模拟与实证（如经济数据）验证了方法的有效性。对您而言，该工作直接与半参数建模与模型平均的效率理论相关，且模型平均的权重估计思路可迁移至因果推断中的离策略评估（DR estimator stacking）。
- **关键技术**: `Semiparametric conditional likelihood`, `Generalized MArginal Forecast Model Averaging (GMAFMA)`, `Penalized marginal forecast model averaging (PGMAFMA)`, `Asymptotic normality`, `Exponential family distribution`, `Nonlinear time series forecasting`
- **为什么对您有用**: 连接半参数理论中的模型平均子方向：如何用半参数方法融合多个非参数预测器，并导出渐近正态加权估计。武器库中最熟悉的非参数统计可用来检验其预测误差的 minmax 最优性（例如对照对应非参数回归的收敛下界），这是立即可做的后续分析——只需将论文的收敛速率与已知的非参数 minmax 界对比，即可判断其是否紧。同时，模型平均的似然加权机制与因果推断中基于非参/半参估计量的 stacking（如 DML 里的超学习器）有深层类比，为进一步交叉提供了入口。

### 33. [10.5705/ss.202024.0349](https://doi.org/10.5705/ss.202024.0349) — Intrinsic Functional Sliced Inverse Regression on Riemannian Manifolds and Wasserstein Spaces
- **作者**: Xinyu Li, Jianjun Xu
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在 Riemannian 或 Wasserstein 空间上的函数型预测变量与标量响应设定下，本文定义了沿 Fréchet 均值曲线的对数函数中心子空间（logarithmic functional central subspace），目标是实现非欧几里得函数数据的 sufficient dimension reduction。核心方法为 intrinsic functional sliced inverse regression（FSIR），利用内蕴几何的对数映射将流形数据拉回切空间进行切片逆回归，并采用截断估计程序估计该子空间。在温和条件下，证明了截断估计量的渐近性质；特别地，利用 Wasserstein 空间的平坦性，方法可识别最优截断数，从而在估计对数函数中心子空间时达到 minimax optimal convergence rate。对您可能有用：本文将 minimax rate 与流形上的 SDR 结合，其内蕴几何+截断估计的框架可为 semiparametric efficiency 在非欧空间的研究提供参照。
- **关键技术**: `functional sliced inverse regression`, `logarithmic central subspace`, `Riemannian manifold intrinsic geometry`, `Wasserstein space flatness`, `minimax optimal convergence rate`, `Fréchet mean curve`
- **为什么对您有用**: 本文直接连接到 semiparametric & nonparametric theory 子方向，在 Wasserstein 空间上给出了 minimax optimal rate，与您熟悉的 minimax bounds 工具高度契合。您可用 very_familiar 的 minimax bounds for estimation problems 验证其声称的最优率是否紧，或用 moderately_familiar 的 semiparametric theory 探究该对数函数中心子空间估计的 semiparametric efficiency bound 是否可达。**立即可做**：用 minimax 理论审视其收敛率下界证明的紧性。

### 34. [10.5705/ss.202024.0213](https://doi.org/10.5705/ss.202024.0213) · [arXiv](https://arxiv.org/abs/2406.15170) — Inference for Delay Differential Equations Using Manifold-Constrained Gaussian Processes
- **作者**: Yuxuan Zhao, Samuel W.K. Wong
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在含时滞反馈的动态系统设定下，目标是从稀疏噪声观测中推断 DDE（delay differential equation）的未知参数（含时滞参数）。本文将 manifold-constrained Gaussian processes（MCGP）扩展至 DDE 推断，在 Bayesian 框架下对系统轨迹施加 GP 先验，并以满足 DDE 的 manifold constraint 作为条件。针对时滞项导致现有 bypass-ODE-solver 方法失效的困难，提出线性插值近似时滞输出，并给出近似导数的理论误差界。模拟（Hutchinson 方程与 lac operon）和 Ontario COVID-19 实际数据验证了方法有效性。对您可能有用：MCGP 的 manifold-constraint 思想与 semiparametric theory 中的 sieve / RKHS 估计有深层联系，且时滞参数的 identification 与推断直接触及 causal inference 中 longitudinal/mediation 设定的时间尺度问题。
- **关键技术**: `manifold-constrained Gaussian process`, `delay differential equation`, `Bayesian parameter inference`, `linear interpolation for time delay`, `derivative approximation error bound`, `gradient-matching bypass solver`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向（MCGP 本质是 RKHS 上的 constrained nonparametric Bayes），以及 causal inference 的 longitudinal 设定（时滞参数 identification 与 mediation 的时间尺度推断同构）。用 very_familiar 的 nonparametric statistics 与 minimax bounds 工具，可以分析该线性插值近似在何种 smoothness 假设下达到最优收敛率，验证其声称的误差界是否紧——这是一个**立即可做**的 follow-up。

### 35. [10.5705/ss.202024.0345](https://doi.org/10.5705/ss.202024.0345) · [arXiv](https://arxiv.org/abs/2309.15855) — Temporally-Evolving Generalised Networks and Their Reproducing Kernels
- **作者**: Tobia Filosi, Claudio Agostinelli, Emilio Porcu
- **期刊/来源**: Statistica Sinica
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究时变广义网络上的随机过程，设定为边具有非线性结构、顶点与边上连续索引随机过程、且拓扑随时间动态演化（节点/边可消失、边形状可变）的图结构。作者基于 Euclidean-edge graph 概念，为线性与循环（周期）时间两种情形分别构建了严格的数学框架，并比较了两种设定的优劣。核心机制是通过拓扑演化构造时变半距离（semi-distance），使广义网络成为半距离空间，进而利用半距离的复合构造定义时变核函数。最终结果是在该时变半距离拓扑上，通过核函数定义了合法的随机场，为网络上的非参数建模提供了 RKHS 基础。对您可能有用：本文的时变半距离与核构造为 longitudinal/动态设定下的非参数协方差建模提供了新思路。
- **关键技术**: `Euclidean-edge graphs`, `semi-distance spaces`, `reproducing kernel Hilbert spaces`, `time-evolving topology`, `circular/linear time indexing`, `kernel composition with semi-distances`
- **为什么对您有用**: 本文连接到非参数理论中的 RKHS 与协方差核构造子方向，特别是动态/纵向设定下的半距离空间建模。您武器库中的 nonparametric statistics 与 minimax bounds 可用于分析此类时变核估计的收敛率，但本文纯数学框架缺乏估计理论，需先在 moderately_familiar 的 M-estimation theory 上长肌肉才能推进估计与推断问题。中期可做。

### 36. [10.5705/ss.202024.0276](https://doi.org/10.5705/ss.202024.0276) · [arXiv](https://arxiv.org/abs/2408.09418) — Grade of Membership Analysis for Multi-Layer Ordinal Categorical Data
- **作者**: Huan Qing
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多层有序分类数据（如个体在不同时间点重复参与同一心理测试）的设定下，目标是估计个体跨层共享的混合成员度（grade of membership），模型假设每个个体以不同权重隶属于多个潜在类别。本文将传统单层 GoM 模型扩展至多层 GoM 模型，并提出基于去偏 Gram 矩阵之和（debiased sum of Gram matrices, DSoG）的估计方法 GoM-DSoG。理论部分建立了 GoM-DSoG 在多层 GoM 模型下的逐个体收敛速率，证明了无响应减少、个体数、项目数及层数的增加均有利于 GoM 分析的精度；同时提出了潜在类别数的选取方法。实验验证了理论发现并展示了 GoM-DSoG 相对于竞争方法的优越性。对您可能有用：DSoG 估计器的去偏 Gram 矩阵构造与逐个体收敛率分析，可直接连接到高维统计中的随机矩阵理论以及去偏估计（debiased estimation）的效率理论视角。
- **关键技术**: `grade of membership model`, `debiased sum of Gram matrices`, `per-subject convergence rate`, `multi-layer ordinal categorical data`, `latent class number selection`
- **为什么对您有用**: 本文的核心估计器基于去偏 Gram 矩阵之和，其逐个体收敛率分析直接触及您 primary interest 中的高维统计与随机矩阵理论（Gram 矩阵谱性质）以及效率理论（去偏估计）的交叉点。您武器库中 very_familiar 的高维渐近理论与 minimax bound 可用于审视其声称的收敛速率是否紧致，moderately_familiar 的 M-estimation 理论可用于分析 DSoG 去偏项的构造逻辑。Follow-up 粗判：**中期可做**——需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以严格推导 DSoG 的 influence function 并判定其是否达到 semiparametric efficiency bound。

### 37. [10.5705/ss.202024.0253](https://doi.org/10.5705/ss.202024.0253) · [arXiv](https://arxiv.org/abs/2109.02236) — Predictive Distributions and the Transition from Sparse to Dense Functional Data
- **作者**: Álvaro Gajardo, Xiongtao Dai, Hans-Georg Müller
- **期刊/来源**: Statistica Sinica
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在稀疏纵向数据向密集函数数据过渡的设定下，目标是研究基于噪声纵向观测的函数主成分（FPC）预测分布的收敛性。核心机制是将每个个体的稀疏观测映射为多元高斯预测分布，并在高斯假设下证明整个预测分布向真实 FPC 的点测度收缩；进一步将截断水平 K=K(n) 随样本量发散时的函数 K-截断预测分布的收缩行为进行了刻画。针对点预测不一致的问题，在函数线性模型中为稀疏纵向预测变量构造了预测分布，并推导了真实与估计预测分布之间 2-Wasserstein 距离的渐近收敛速率。实证部分使用了 Baltimore Longitudinal Study of Aging 数据。对您可能有用：本文的 Wasserstein 收敛速率分析为稀疏纵向/函数数据的分布推断提供了新的非参数理论视角。
- **关键技术**: `functional principal component analysis`, `predictive distribution`, `2-Wasserstein metric`, `shrinkage towards point mass`, `functional linear model`, `sparse-to-dense transition`
- **为什么对您有用**: 本文直接连接到非参数理论（functional data 的分布推断与收敛速率），属于您 primary interest 中 semiparametric & nonparametric theory 的范畴。您武器库中 very_familiar 的 minimax bounds for estimation problems 可直接用来检验本文声称的 Wasserstein 收敛速率是否紧，或进一步推导 minimax lower bound。follow-up 粗判：立即可做——用 minimax rate 工具验证或改进其收敛速率。

## 效率理论 / Debiased ML  *(efficiency_dml, 3 篇)*

### 1. [10.5705/ss.202025.0211](https://doi.org/10.5705/ss.202025.0211) — Inference for High-dimensional Model Averaging Estimators
- **作者**: Lise Léonard, Eugen Pircalabelu, Rainer von Sacks
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在高维线性回归（p>n）设定下，本文提出一种基于 debiased Lasso 的 model averaging 估计器，目标是在进行模型平均的同时实现有效推断。估计器通过 debiased Lasso 构造以消除 Lasso 的正则化偏置，权重选取以最小化预测风险为准。作者在高维框架下推导了该估计器的渐近正态分布，并提供了所选权重下预测风险的极小化保证。与现有仅做平均或仅做选择的方法不同，该方法同时兼顾了预测风险的优化与基于渐近正态性的推断能力。实证与模拟表明其预测风险低于竞争对手。对您可能有用：将 debiased / one-step 思路从单一模型拓展到 model averaging 组合，为高维因果推断中多模型稳健推断提供了新路径。
- **关键技术**: `debiased Lasso`, `model averaging`, `high-dimensional asymptotic normality`, `prediction risk minimization`, `one-step correction`
- **为什么对您有用**: 直接连接 efficiency_dml（debiased ML / one-step correction）与 high_dim_rmt 的高维推断设定；用您 very_familiar 的高维渐近与 minimax bound 工具可以审视其预测风险保证是否紧，以及权重选取的 optimality。**立即可做**：用 minimax bound 验证其声称的预测风险界，并思考该 model averaging + debiased 框架能否迁移到高维因果推断（如 debiased IV / debiased mediation）的 robust inference。

### 2. [10.5705/ss.202024.0359](https://doi.org/10.5705/ss.202024.0359) · [arXiv](https://arxiv.org/abs/2312.10596) — A Maximin Optimal Approach for Sampling Designs in Two-phase Studies
- **作者**: Ruoyu Wang, Qihua Wang, Wang Miao
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在两阶段抽样研究中，第一阶段对全部个体收集廉价变量，第二阶段依据预设抽样规则对子样本收集昂贵变量，目标是基于 semiparametric efficiency bound 寻找最优抽样规则以提升估计效率。现有文献多局限于特定参数模型或单参数估计，本文提出 maximin 准则，在模型未知（model-free）的半参数框架下设计最优抽样规则。当参数为标量时，该规则可直接最小化 semiparametric efficiency bound；当参数为多维时，该规则能改善每个分量对应的 efficiency bound。模拟与实证表明，所提设计在多种设定下有效降低了估计量方差。对您可能有用：本文将 semiparametric efficiency bound 从估计问题拓展到抽样设计问题，为两阶段因果推断（如 proximal CI 的 negative-control 子抽样）提供了效率最优的实验设计视角。
- **关键技术**: `semiparametric efficiency bound`, `maximin optimal design`, `two-phase sampling`, `model-free estimation`, `influence function`
- **为什么对您有用**: 本文直接连接到 efficiency theory 子方向，将 semiparametric efficiency bound 用于两阶段抽样设计的最优化，而非传统的估计最优化；您可以用 very_familiar 中的 minimax bounds 工具审视其 maximin 准则的紧性，并用 moderately_familiar 的 semiparametric theory 推导具体因果 estimand（如 ATE）在该抽样规则下的 influence function。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以将本文的 model-free 抽样规则具体化到 proximal CI 或 longitudinal causal setting 中。

### 3. [10.5705/ss.202025.0083](https://doi.org/10.5705/ss.202025.0083) — Estimation and Inference for Density-convoluted Support Vector Machine with Streaming Data
- **作者**: Haochen Rao, Xu Guo, Heng Lian, Haobo Qi
- **期刊/来源**: Statistica Sinica
- **机构**: City University of Hong Kong · Beijing Normal University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维流式数据设定下研究 SVM 系数的估计与推断，目标 estimand 为分类边界系数，关键假设为稀疏性与流式数据独立到达。为处理 hinge loss 的非光滑性，采用密度卷积（density convolution）技术构造光滑替代损失；进而提出在线 Lasso 估计器，利用可更新的二次型近似历史信息，仅需新数据与有限历史摘要即可在线更新，并给出其非渐近误差界。为消除 Lasso 的固有偏差，进一步提出在线去偏 Lasso 估计器并构造推断程序，证明了去偏估计器的渐近正态性（n^{-1/2}-CAN）。数值计算采用 proximal gradient descent，适用于高维且计算高效。对您可能有用：本文将 density convolution 与在线去偏推断结合，为流式数据下的高维非光滑损失推断提供了完整框架。
- **关键技术**: `density convolution`, `online lasso`, `debiased lasso`, `streaming data quadratic approximation`, `proximal gradient descent`, `asymptotic normality`
- **为什么对您有用**: 直接连接到 efficiency theory 中的 debiased ML / 高维推断子方向，以及 stat_computing 中的在线算法设计。您武器库中的 high-dimensional asymptotics 与 M-estimation theory（moderately_familiar）可直接攻入本文的误差界与去偏渐近正态性证明；density convolution 对 hinge loss 的光滑化处理是一个值得借鉴的技术点。follow-up 粗判：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉（特别是非光滑损失的 M-estimator 渐近理论），即可尝试将此在线去偏框架迁移到其他非光滑损失（如 quantile regression）的流式推断。

## 数理统计 / 假设检验  *(hypothesis_testing, 17 篇)*

### 1. [10.5705/ss.202024.0078](https://doi.org/10.5705/ss.202024.0078) — Structural Testing of High-dimensional Correlation Matrices
- **作者**: Tingting Zou, Guangren Yang, Ruitao Lin, Guoliang Tian, Shurong Zheng
- **期刊/来源**: Statistica Sinica
- **机构**: Northeast Normal University
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在高维设定下检验相关矩阵的一般线性结构（含 banded 与 compound symmetry 等特例），目标参数为结构中的未知系数。首先基于 quadratic loss 构造参数估计程序，随后分别以 quadratic 与 sup-norm 构造检验统计量，以适配 dense 与 sparse alternatives。在 null 与 alternative 下推导了检验统计量的极限分布，核心工具为高维随机矩阵的 Marchenko-Pastur 型谱分析及大维中心极限定理。模拟与实数据验证了有限样本表现。对您可能有用：本文将 RMT 谱工具直接用于高维假设检验，与您的高维统计与 hypothesis testing 两个 primary interest 交叉。
- **关键技术**: `high-dimensional correlation matrix testing`, `quadratic loss estimation`, `sup-norm test statistic`, `Marchenko-Pastur law`, `large-dimensional central limit theorem`, `banded / compound symmetry structure`
- **为什么对您有用**: 直接连接您的高维统计（RMT）与 hypothesis testing 两个 primary interest：本文用 RMT 谱极限推导高维相关矩阵结构检验的极限分布，是典型的 RMT-inference 交叉工作。您 very_familiar 的高维渐近理论可直接审视其极限分布推导的 technical 细节（如 CLT 中的 variance 估计是否紧），moderately_familiar 的 M-estimation theory 可切入其 quadratic loss 参数估计的收敛性分析。**立即可做**：用 very_familiar 的高维渐近与 minimax bound 工具验证其声称的检验功效在 sparse alternative 下是否达到 minimax rate。

### 2. [10.5705/ss.202025.0036](https://doi.org/10.5705/ss.202025.0036) · [arXiv](https://arxiv.org/abs/2409.16683) — Robust Max Statistics for High-dimensional Inference
- **作者**: Mingshuo Liu, Miles Lopes
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `weaker_assumption`
- **摘要**: 在高维重尾数据设定下研究 max statistic 的 bootstrap 近似问题，目标 estimand 是 max statistic 的分布函数，关键 regularity 假设为扩展的 L^4-L^2 moment equivalence 条件与弱方差衰减条件。作者提出基于 robust max statistic 的推断方法，证明在 Kolmogorov 距离下 bootstrap 近似可达到近参数速率（near-parametric rate），且该速率与数据维度无关。核心机制利用 moment equivalence 控制重尾下的 tail probability，结合方差衰减条件保证 bootstrap 一致性，适用于 Euclidean 与 functional 数据。主要理论结果将高维 max statistic bootstrap 的适用范围从轻尾拓展至重尾，对您有用之处在于为高维假设检验中重尾场景提供了 sharper rate 的理论保证。
- **关键技术**: `robust max statistic`, `bootstrap approximation`, `L^4-L^2 moment equivalence`, `weak variance decay`, `near-parametric rate`, `Kolmogorov metric`
- **为什么对您有用**: 直接连接高维假设检验与 RMT 相关的 moment condition 设定，L^4-L^2 moment equivalence 是高维统计与 RMT 中控制谱分布与 tail behavior 的核心工具。用您 very_familiar 的高维渐近理论可以直接审视其 near-parametric rate 在重尾设定下是否紧，或与 minimax bound 对比验证 optimality。立即可做：用 very_familiar 的 minimax bounds 工具检验该速率的下界是否可达，或探索该 moment equivalence 条件在您熟悉的 random matrix 谱分布中的等价形式。

### 3. [10.5705/ss.202025.0042](https://doi.org/10.5705/ss.202025.0042) — Sequential Multiple Testing of Multiple Composite Hypotheses: an Asymptotic Optimality Theory with General Information Functions
- **作者**: Yiming Xing
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究多个独立数据流的序贯多重检验问题，每个数据流对应多个复合假设以及一个无差异区（indifference zone）。作者提出了一种新的全局错误度量，同时控制不同误分类个数（即错误分类数量）的概率低于指定水平，该度量将经典误分类概率和广义误分类概率作为特例。针对该度量，设计了一个新的序贯检验程序，并证明在所有水平趋于零的渐近意义下，该程序在所有可能分布下达到最小期望样本量，且渐近最优性允许时间依赖和一般信息函数（不限于线性信息函数）。理论通过若干例子加以说明，数值研究展示了渐近性质和有限样本表现。本文对假设检验理论有重要贡献，尤其适合对多重比较和序贯分析感兴趣的统计学者。
- **关键技术**: `sequential multiple testing`, `composite hypotheses`, `indifference zone`, `global error metric`, `asymptotic optimality`, `general information functions`
- **为什么对您有用**: 本文属于假设检验理论的前沿工作，与您对数学统计和假设检验的兴趣高度吻合。其中提出的渐近最优性框架可借助您非常熟悉的minimax下界技术来验证其效率边界是否紧致。但由于序贯分析的核心工具（序贯概率比检验、最优停止理论）不在您当前的技术库中，直接推进相关拓展工作暂不可行，建议先了解序贯检验的基本理论以填补该缺口。

### 4. [10.5705/ss.202025.0155](https://doi.org/10.5705/ss.202025.0155) — Subgroup Testing in Change-Plane Models and Its Applications to Medical Data
- **作者**: Xu Liu, Jian Huang, Yong Zhou, Feipeng Zhang, Panpan Ren
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对变化平面模型（change-plane model）中的子组参数是否存在差异提出假设检验问题，该问题在零假设下部分参数不可识别。经典的指数平均检验（exponential average test）在实际中功效不足；为克服此缺陷，作者构造了一个加权平均平方得分检验统计量（WAST），通过在分组参数空间上取加权平方得分统计量的平均，并选择适当权重使其具有封闭形式。WAST显著提升了有限样本下的检验功效，并给出了零假设和备择假设下的渐近分布。作者进一步研究了基于自助法（bootstrap）的临界值逼近，并提供了理论保证；同时将方法扩展到广义估计方程（GEE）框架和多个变化平面的场景。在模拟实验和三个医疗数据集上的应用验证了该方法的有效性。对您而言，该工作直接关联您对假设检验的兴趣，并提供了处理非标准（non-identifiable）参数检验问题的新思路；其中自助法的理论分析可借助您熟悉的非参数统计工具进行深入评估，而医疗数据应用也可能与流行病学中的异质性因果效应检验产生联系。
- **关键技术**: `change-plane models`, `weighted average of squared score test`, `bootstrap`, `generalized estimating equations`, `non-identifiable parameters under null`
- **为什么对您有用**: 本文直接命中您primary interest中的假设检验方向，尤其聚焦于零假设下参数不可识别这一困难设定，提出了一个具有封闭形式的检验统计量并给出了渐近理论。您可以利用您对nonparametric statistics的熟悉（如bootstrap理论）来理解其理论保障，并可能将这种加权得分思想推广至其他因果推断中的子组异质性检验场景。此外，医疗数据的应用为流行病学中的个性化治疗提供了可复用的分析框架。综合判断：立即可做，因为假设检验和bootstrap均在您非常熟悉的武器库中。

### 5. [10.5705/ss.202025.0183](https://doi.org/10.5705/ss.202025.0183) — A Conditionally Studentized Test for High-dimensional Parametric Regression via Sample Splitting
- **作者**: Feng Liang, Chuhan Wang, Jiaqi Huang, Lixing Zhu
- **期刊/来源**: Statistica Sinica
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维参数回归模型的模型检验问题，提出了一种条件学生化检验（COST）。该方法基于两个不相交的样本划分，通过一个权重矩阵连接，并对其中一个子样本进行条件学生化处理。COST不需要降维或稀疏性假设，当原假设成立时，无论初始检验统计量是全局还是局部平滑型，以及预测变量维度、样本量和参数个数之间的关系如何（固定或发散，在一定的速率限制下），都能实现渐近正态性。在回归函数满足一定条件时，渐近正态性甚至可以在预测变量维度超过样本量时成立，从而具有分析高维问题的潜力。此外，COST对局部备择假设具有快速的检测速率。论文讨论了样本划分策略，并通过数值研究展示了COST在有限样本下的表现，包括预测变量维度等于样本量的情形。这项工作为高维回归模型检验提供了一种不依赖稀疏性的新工具，对您在高维假设检验方面的兴趣有直接价值。
- **关键技术**: `sample splitting`, `conditional studentization`, `weight matrix`, `asymptotic normality`, `global/local smoothing-based test`
- **为什么对您有用**: 本文直接连接您的首要兴趣——高维统计下的假设检验，针对的是参数回归模型的模型检验，不依赖于稀疏性或降维假设。您的技术武器库中“high-dimensional asymptotics”非常熟悉，可直接用于分析和拓展该检验的渐近性质，例如推导更紧的速率或适应更一般的设定。该方法的样本分割策略与条件学生化思路清晰，属于**立即可做**的范畴：您可以快速复现核心结论并考虑将其推广到其他检验问题（如非参数模型或因果推断中的假设检验）。

### 6. [10.5705/ss.202025.0327](https://doi.org/10.5705/ss.202025.0327) — A Data-Adaptive Integrated Approach to Covariance Change Point Detection in High-dimensional Settings
- **作者**: Canhuang Xu, Lei Shu, Yu Chen, Qing Yang
- **期刊/来源**: Statistica Sinica
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究高维随机向量序列中协方差矩阵的变点检测问题，目标是在维数远大于样本量的设定下识别协方差结构的变化点。提出了一种基于重加权累积和（CUSUM）的统计量，并引入数据自适应的参数选择方法以优化权重确定。围绕该统计量构建了变点检测的完整框架，包括假设检验程序以检验变点是否存在。理论方面证明了参数选择的有效性和变点估计的相合性，并在一定正则条件下建立了检验的渐近有效性。通过大量仿真和真实数据分析验证了方法的实用性和统计可靠性。对您有用：本文的高维假设检验框架和高维渐近理论可以直接与您非常熟悉的高维渐近性工具对接，可进一步分析该方法的 minimax 最优性。
- **关键技术**: `CUSUM statistic`, `data-adaptive weight selection`, `high-dimensional covariance estimation`, `change point detection`, `hypothesis testing procedure`, `consistency`
- **为什么对您有用**: (1) 直接连接到您主要兴趣中的高维假设检验，特别是高维协方差结构的变点检测这一具体子方向。 (2) 您非常熟悉的高维渐近性工具可以直接用于分析该CUSUM统计量的收敛速度和检验功效，无需额外学习新工具。 (3) 立即可做：方法核心是经典CUSUM在高维的推广，理论验证复杂度不高，可直接用您已有知识复现或扩展。

### 7. [10.5705/ss.202025.0113](https://doi.org/10.5705/ss.202025.0113) · [arXiv](https://arxiv.org/abs/2308.04368) — Multiple Testing of Local Extrema for Detection of Structural Breaks in Piecewise Linear Models
- **作者**: Zhibing He, Dan Cheng, Yunpeng Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在分段线性模型（stationary Gaussian noise）设定下，目标是检测结构断点（连续斜率变化 Type I 与跳跃 Type II）的数量与位置。方法将断点检测转化为对数据序列核平滑后局部极值的识别，利用光滑 Gauss 过程的 peak height 分布为所有局部极值计算 p-value，再通过 BH 程序筛选显著极值作为断点。理论证明在序列长度、斜率变化量或跳跃量增大时，方法保证 FDR 的渐近控制与 power consistency；计算复杂度仅为 O(n)，优于传统递归分割算法。数值研究与 R 包 dSTEM 显示在非渐近（信号较弱）情形下 FDR 与 power 仍表现稳健。对您有用：该文将 multiple testing（BH）与 Gauss 过程极值分布结合解决断点检测，为 hypothesis testing 与 nonparametric kernel smoothing 的交叉提供了一个具体可操作的框架。
- **关键技术**: `kernel smoothing and differentiation`, `peak height distribution of smooth Gaussian processes`, `Benjamini-Hochberg procedure`, `FDR control for local extrema`, `piecewise linear change point detection`, `computational complexity O(n)`
- **为什么对您有用**: 本文直接连接 hypothesis testing 子方向：将断点检测重构为基于 Gauss 过程极值分布的多重检验问题，FDR 渐近控制与 power consistency 的理论证明是核心贡献。用您 very_familiar 的 nonparametric statistics（核平滑）与 minimax bounds 视角，可以审视其 peak height 分布逼近的 rate 是否紧、弱信号下 FDR bound 的非渐近精度是否可进一步 sharpen。Follow-up 判断：**立即可做**——用 minimax bound 工具验证其声称的渐近 rate 在最坏情形下是否紧，或用 higher-order U-statistic / HOIF 视角探索极值分布高阶逼近的改进空间。

### 8. [10.5705/ss.202024.0320](https://doi.org/10.5705/ss.202024.0320) — Model-free Multivariate Change Point Detection and Localization with Statistical Guarantee
- **作者**: Xin Xing, Zuofeng Shang, Hongyu Miao, Pang Du
- **期刊/来源**: Statistica Sinica
- **机构**: Florida Institute of Technology · Virginia Tech
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究多元变点检测问题，目标是在无模型假设下识别数据分布的变化并精确定位变点位置。方法基于RKHS框架下的非参数密度估计，构造CUSUM似然比检验统计量，避免了以往非参数检验依赖于无穷级数的局限性。作者建立了完整的非渐近理论框架，证明该统计量能渐近控制第一类错误，且变点定位达到最优收敛速率。理论结果覆盖了多元情形，且不依赖参数模型假设，具有较好的适用性。本文对您的研究方向有直接联系：它属于假设检验和非参数统计的交汇点，同时其非渐近分析技术可借鉴到其他统计推断问题中。
- **关键技术**: `CUSUM likelihood ratio`, `RKHS density estimation`, `non-asymptotic analysis`, `change point localization`
- **为什么对您有用**: 本文直接关联假设检验和非参数理论两个核心兴趣方向。研究者可以用其非常熟悉的非参数统计和极小极大下界工具来评估该方法的定位速率是否达到最优。由于方法基于RKHS，研究者也能利用对高维渐近的理解，检验其在多元情形下的实际表现。follow-up粗判：立即可做——研究者已熟练掌握非参数统计和渐近理论，可直接理解本文技术细节，并可尝试扩展至依赖结构（如sparsity）的变点检测。

### 9. [10.5705/ss.202025.0225](https://doi.org/10.5705/ss.202025.0225) — Integrating External Summary Information via James-Stein Shrinkage
- **作者**: Peisong Han, Haoyue Li, Jeremy M. G. Taylor
- **期刊/来源**: Statistica Sinica
- **机构**: Cancer Research And Biostatistics
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该论文研究在拟合一般参数回归模型（如广义线性模型）时，如何利用外部研究的汇总信息（如参数估计）来改进内部模型的参数估计。传统方法分为两类：一类旨在减少方差但不引入偏差，另一类允许以偏差换取方差的大幅缩减。作者采用后一种思路，开发了James-Stein收缩估计量，以整合外部信息。该估计量能够保证渐近期望风险不劣于不使用外部信息的情况，无论内外群体异质性程度如何；这一性质被称为“安全通道”，现有方法极少能提供这种保证。论文给出了渐近风险分析，并通过模拟和前列腺癌数据集验证了数值表现。对您而言，本文是James-Stein收缩在信息整合中的新应用，连接了经典统计推断与实证研究中的外部数据利用问题。
- **关键技术**: `James-Stein shrinkage`, `asymptotic risk`, `bias-variance trade-off`, `external summary information`, `parametric regression model`, `risk improvement guarantee`
- **为什么对您有用**: 本文属于数学统计与假设检验方向，直接对应您的主要兴趣之一。您熟悉的minimax理论和渐近分析（来自very_familiar中的“minimax bounds”和“high-dimensional asymptotics”）可用于理解和拓展其风险保证。短期可读全文，中期可将该收缩思想推广至因果推断中外部估计值的整合（如工具变量或proximal CI的敏感性分析）。由于核心工具（渐近风险分析、收缩估计）已在您的武器库中，本文可立即可做。

### 10. [10.5705/ss.202025.0194](https://doi.org/10.5705/ss.202025.0194) · [arXiv](https://arxiv.org/abs/2603.24875) — Post-Selection Inference in Generalized Linear Models via Parametric Programming
- **作者**: Qinyan Shen, Karl Gregory, Xianzheng Huang
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对Lasso变量选择后广义线性模型（GLM）中回归系数的推断问题，提出了一个基于参数规划的统一框架。该框架将线性模型（高斯响应）中的参数规划策略推广到非高斯GLM，通过构造伪响应和策略性线性化模型来模拟最大似然估计与最小二乘估计的平行关系。方法的核心在于利用原始数据生成伪响应和协变量，从而将后选择推断转化为线性化模型上的推断问题。模拟实验涵盖三种非高斯响应类型，表明所提方法能有效纠正忽略变量选择的朴素推断，且效率优于基于多面体的传统调整方法。该工作为高维GLM中的选择性推断提供了计算上可行的新途径，尤其适用于需同时处理变量选择和推断的实证场景。对您而言，该论文连接了高维统计中的后选择推断问题，您熟悉的high-dimensional asymptotics工具可帮助理解其渐近论证，且方法可能迁移至因果推断中的高维协变量选择后推断。
- **关键技术**: `Lasso-based variable selection`, `parametric programming`, `post-selection inference`, `generalized linear models`, `pseudo-response`, `polyhedral method`
- **为什么对您有用**: 该论文直接关联您的高维统计与假设检验兴趣，属于变量选择后推断这一经典子方向。您武器库中的high-dimensional asymptotics（非常熟悉）可支撑理解其线性化与渐近论证，且论文的方法经验证可迁移至因果推断情境（如高维协变量筛选后的处理效应推断）。基于现有武器，您可以立即复现其模拟并尝试将其参数规划框架扩展到您关注的因果估计量（如IPW或DR估计中的选择后推断）。

### 11. [10.5705/ss.202024.0334](https://doi.org/10.5705/ss.202024.0334) — Optimal Robust Sequential Tests of Circular Nonconforming Probability
- **作者**: Qunzhi Xu, Yajun Mei
- **期刊/来源**: Statistica Sinica
- **机构**: New York University
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在非参数序贯检验设定下，本文研究圆形非符合概率（CNP，即二维系统落入预设圆盘目标的概率）的 minimax 检验问题，目标是在不假设观测数据分布形状的前提下，用最少样本评估二维系统精度。核心方法是将落入/未落入圆盘的原始数据二值化，构造 Bernoulli 序贯概率比检验（SPRT）；理论证明该 Bernoulli SPRT 在所有满足相同或更小 Type I/II 错误概率的检验（含固定样本量检验）中，最小化了最大期望样本量，达到 minimax 最优。针对序贯分析渐近理论常假设极小错误概率而不实用的局限，本文进一步提出具体算法以设计与实现 Bernoulli SPRT，便于实际应用。对您可能有用：本文将 minimax 理论与序贯 SPRT 结合处理非参数假设检验，直接关联您在 hypothesis testing 与 minimax bounds 的核心兴趣。
- **关键技术**: `minimax sequential testing`, `Bernoulli SPRT`, `circular nonconforming probability`, `nonparametric hypothesis testing`, `expected sample size optimization`
- **为什么对您有用**: 直接关联您 primary interest 中的 hypothesis testing 与 minimax bounds 子方向：本文在非参数设定下严格证明了 Bernoulli SPRT 的 minimax 最优性，给出了具体的期望样本量下界与可达性。您武器库中 very_familiar 的 minimax bounds for estimation problems 可直接迁移至检验问题，审视其 minimax 证明策略是否可推广至更一般的非参数序贯检验设定。Follow-up 判断：立即可做——用 minimax bound 工具即可动手探索该框架在其他形状目标（如椭圆）或高维设定下的扩展。

### 12. [10.5705/ss.202025.0126](https://doi.org/10.5705/ss.202025.0126) — A Variation-Ratio Test for Volatility Jumps Using Noisy High Frequency Data
- **作者**: Guangying Liu, Kewen Shi, Zhiyuan Zhang
- **期刊/来源**: Statistica Sinica
- **机构**: Nanjing Audit University
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对高频金融数据中带微观结构噪声的波动率跳跃检验问题，提出一种新的 variation-ratio 检验统计量。原假设（无波动率跳跃）下该统计量渐近正态，备择假设（存在跳跃）下以 n^{1/4-}（任意小 ε>0）的发散速度趋于无穷，显著快于现有文献中最优的 n^{1/8} 速度。统计量基于经 pre-averaging 处理后的已实现波动率与已实现二次变差之比构造，以消除微观结构噪声影响。模拟实验证实了理论速率优势，实证分析显示 90 只美国股票中相当一部分表现出波动率跳跃特征。对您而言，本文在非标准渐近框架下设计检验统计量并推导更优发散速率的方法，可能为假设检验问题（尤其是 you 很熟悉的 minimax 检验界）提供新思路，但工具上需要高频时间序列渐近理论，并非您当前非常熟悉的领域。
- **关键技术**: `variation-ratio test`, `volatility jumps`, `high-frequency data`, `microstructure noise`, `pre-averaging`, `asymptotic normality`
- **为什么对您有用**: 本文属于假设检验领域，直接对应您 primary interest 中的 mathematical statistics & hypothesis testing。文中在备择假设下获得更快的发散率，展示了如何改进检验势，这与 minimax 检验界问题有潜在联系。但方法高度依赖高频时间序列的渐近理论（如 pre-averaging 技巧），并非您非常熟悉的工具（very_familiar 中无此项），因此短期难以直接迁移，但可作为中期可做方向——需先熟悉金融高频渐近工具。

### 13. [10.5705/ss.202025.0127](https://doi.org/10.5705/ss.202025.0127) — Classification Uncertainty Quantification: A Comparison Between Bootstrap and Conformal ROC Confidence Bands
- **作者**: Zheshi Zheng, Bo Yang, Peter Song
- **期刊/来源**: Statistica Sinica
- **机构**: Cancer Research And Biostatistics
- 相关性 4/10 · novelty: `application`
- **摘要**: 该文研究分类算法性能评估中 ROC 曲线的不确定性量化问题，对比了传统 Bootstrap 方法与现代共形预测（conformal prediction）方法在构建 ROC 置信带和 Youden 指数置信区间上的表现。通过一个简单的模型驱动分类示例，揭示了 Bootstrap 方法在这种设定下的局限——其置信带可能不具覆盖有效性。作者提出基于共形预测的方法，能够在有限样本下提供有有限样本覆盖保证的 ROC 置信带。理论分析证明该方法的有效性，数值实验进一步验证了共形预测相比 Bootstrap 在不确定性量化上的显著改进。对您而言，该文直接关联到假设检验中的置信区间构建方法，并且 ROC 曲线是流行病学诊断试验中的常用工具，可作为入门级对比阅读。
- **关键技术**: `conformal prediction`, `bootstrap confidence bands`, `ROC curve uncertainty`, `Youden index`
- **为什么对您有用**: （1）该文属于假设检验/不确定性量化方向，与您对置信区间及覆盖有效性的兴趣吻合；ROC 曲线在流行病学（secondary interest）中广泛用于诊断测试评估，可提供实际数据应用的入口。（2）您可以利用 very_familiar 中的软件开发和因果推断估计理论，在模拟或真实数据上复现并扩展该比较实验，检验共形预测在其他分类器（如深度学习）上的表现。（3）立即可做：使用熟悉的软件工具实现两种方法并在公开诊断数据上运行对比，无需额外学习新理论。

### 14. [10.5705/ss.202025.0139](https://doi.org/10.5705/ss.202025.0139) — Testing Conditional Tail Independence
- **作者**: Zhaowen Wang, Huixia Judy Wang, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文聚焦于双变量极端值的条件尾部依赖结构检验，现有尾部依赖指标未考虑协变量影响。首先定义了条件尾部依赖指数（conditional tail dependence index），用于区分条件尾部独立与依赖。提出条件尾部商相关系数（CTQCC）作为检验条件尾部独立性的统计量，并推导了其渐近分布。通过模拟研究评估了有限样本表现，并应用于美国日降水量与风速的条件尾部依赖分析，以日最高气温为条件变量。结果表明该方法能有效检测条件尾部依赖结构。对您而言，该工作属于假设检验在极值理论中的应用，与您的 hypothesis testing 兴趣直接相关。
- **关键技术**: `conditional tail dependence index`, `conditional tail quotient correlation coefficient (CTQCC)`, `extreme value theory`, `asymptotic distribution under null hypothesis`, `nonparametric kernel estimation`
- **为什么对您有用**: 本文直接连接到您的 primary interest 中的 hypothesis testing，特别是尾部依赖的假设检验问题。您可以用 very_familiar 中的 nonparametric statistics 工具（如核平滑）来估计条件分位数和尾部指数，从而复现或改进该检验方法。但这需要补充极值理论的渐近分布知识（如 tail index 估计的极限性质），该项不在当前武器库中，因此暂不可直接动手，建议作为中期可做方向——先学习极值理论中的条件尾部估计工具（moderately_familiar 可扩展至此），再尝试推广到高维或 U-statistic 形式的检验。

### 15. [10.5705/ss.202025.0075](https://doi.org/10.5705/ss.202025.0075) — D-Optimal Designs for Ordinal Response Experiments
- **作者**: Huiping Dang, Jun Yu, Fasheng Sun
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在有序响应实验设定下，本文研究 adjacent-categories 模型（含一般 link 函数及定量/定性因子）的 locally D-optimal design 问题。核心 estimand 为 Fisher 信息矩阵的行列式最大化，关键 regularity 假设为参数已知或给定初始值（locally 设定）。方法上，先推导出 D-optimal design 的支撑点数目特征与简单完全类（complete class）结构，再基于该结构提出高效搜索算法；最后讨论整数化分配的实际实现。理论结果给出了支撑点数的上界与完全类刻画，数值实验显示所提设计在统计效率与计算时间上优于现有方法。对您可能有用：若将有序响应模型嵌入因果推断或流行病学中的 treatment assignment 问题，D-optimal 结构可指导有限预算下的实验设计。
- **关键技术**: `locally D-optimal design`, `adjacent-categories logit model`, `complete class theorem`, `Fisher information matrix`, `integer-valued allocation`, `optimal design search algorithm`
- **为什么对您有用**: 本文连接到实验设计（hypothesis_testing / causal inference 的 treatment assignment 子方向），但核心是 classical optimal design 理论而非您关注的 semiparametric efficiency 或 high-dimensional inference。用您 very_familiar 中的 minimax bounds 视角审视，D-optimal 的完全类刻画本质上是在有限维参数空间做 minimax（D-criterion），但该框架与您当前武器库中的 higher-order U-statistics / tensor contraction 无直接交叉。**中期可做**：若想将有序响应的 D-optimal design 推广到 semiparametric / high-dim 设定（如 infinite-dimensional nuisance），需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体是 semiparametric information bound 与 design 的交互），当前 paper 本身是 classical 框架内的扎实工作，可作为入门读物了解有序响应模型结构，但不必深读证明细节。

### 16. [10.5705/ss.202025.0390](https://doi.org/10.5705/ss.202025.0390) · [arXiv](https://arxiv.org/abs/2509.15508) — Modelling Time Series of Counts with Hysteresis
- **作者**: Xintong Ma, Dong Li, Howell Tong
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对计数时间序列中的滞后效应提出一种新型非线性模型——滞后Poisson自回归(HPART)模型，通过引入阈值机制刻画状态转换的复杂动态。与已有的缓冲Poisson自回归(BPART)模型相比，HPART模型包含一个科学相关的控制因子以产生真正的滞后现象，从而更深入地揭示机制转换的内在规律。作者在统一框架下研究了两个模型参数的极大似然估计及其渐近性质（相合性、渐近正态性），并针对非嵌套模型（BPART vs HPART）建立了分离假设族检验。蒙特卡洛模拟验证了估计量和检验在有限样本下的有效性，两个实际数据案例展示了HPART在解释力和样本外预测上的优势。对您而言，尽管本文不涉及高维或因果框架，但其对非嵌套模型进行假设检验的思路可迁移至因果推断中的模型选择（如IV与proximal模型的检验），且您熟悉的M估计理论可直接用于理解其估计性质，属于立即可做的工具嫁接。
- **关键技术**: `Poisson autoregressive model`, `hysteretic threshold`, `maximum likelihood estimation`, `non-nested hypothesis testing`, `piecewise linear structure`
- **为什么对您有用**: 本文属于数学统计中的假设检验方向，直接连接您'primary_interests'中的hypothesis testing子方向。文中发展的非嵌套模型检验方法可与您熟悉的M-estimation理论结合，用于比较因果推断中不同识别策略（如IV与proximal模型）的适用性。技术上，您'very_familiar'中的nonparametric statistics和high-dimensional asymptotics足以支撑您快速阅读和理解全文的核心渐近结果，无需额外工具，因此立即可做。

### 17. [10.5705/ss.202025.0350](https://doi.org/10.5705/ss.202025.0350) — Models for Order-of-Addition Screening Experiments
- **作者**: Jing-Wen Huang, Hongquan Xu
- **期刊/来源**: Statistica Sinica
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 在序加筛选实验(order-of-addition screening)设定下，目标是在资源受限、仅能施加部分组件时，同时选择组件子集及其最优排列以最小化响应损失。作者提出一系列序加筛选模型，将位置效应与组件选择纳入统一框架，并给出相应最优设计的理论性质（如 D-optimal 条件与信息矩阵结构）。核心工具为排列线性模型与最优设计理论，模型在 job scheduling with rejection penalties 上做了实证演示。对您可能有用：该排列效应模型的结构与高阶 U-statistic 的对称群投影有形式相似性，其最优设计下的信息矩阵分析可借鉴到您对高阶 U-statistic minimax 界的推导。
- **关键技术**: `order-of-addition model`, `positional effect model`, `D-optimal design`, `permutation linear model`, `screening experiment`
- **为什么对您有用**: 本文连接到您 primary interest 中的高阶 U-statistic 与 minimax 理论：排列线性模型的位置效应参数化与您用 treewidth / einsum 分析高阶 U-statistic 对称群投影的结构同源，最优设计的信息矩阵界可类比到 estimator 的 semiparametric efficiency bound。用 very_familiar 的 minimax bounds for estimation problems 可直接分析该模型在部分排列观测下的估计效率下界，属于**立即可做**的延伸方向。

## 统计计算 / 算法  *(stat_computing, 7 篇)*

### 1. [10.5705/ss.202024.0308](https://doi.org/10.5705/ss.202024.0308) — Heterogeneous Autoregressive Modeling with Flexible Cascade Structures
- **作者**: Huiling Yuan, Guodong Li, Kexin Lu, Alan T.K. Wan, Yong Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对高频金融数据中已实现度量的预测问题，本文提出了多层低秩异质自回归（MLRHAR）模型。与传统HAR模型使用固定异质波动成分不同，MLRHAR采用数据驱动方法自动选择成分。利用四阶张量技术同时降维响应、预测变量、短期和日历时间方向，大幅减少参数空间。建立了高维HAR模型的非渐近性质，并提出投影梯度下降算法进行参数估计，同时给出了理论保证。模拟实验和标普500成分股数据的实证结果表明，该模型在预测精度上具有显著优势。这项工作将张量降维与高维时间序列建模相结合，其算法和理论分析为统计计算和高维统计提供了可借鉴的方法。
- **关键技术**: `low-rank tensor decomposition`, `projected gradient descent`, `Heterogeneous Autoregressive (HAR) model`, `non-asymptotic theory`, `high-dimensional time series`
- **为什么对您有用**: 连接点：高维统计中的非渐近理论与统计计算中的张量算法。您对高维渐近和逆问题非常熟悉，可直接分析该投影梯度算法的收敛速度与统计效率。中期可做：若进一步提升张量降维的模型可解释性，需先加强您在高阶U统计量工具箱中关于张量收缩复杂度的理解。

### 2. [10.5705/ss.202024.0346](https://doi.org/10.5705/ss.202024.0346) · [arXiv](https://arxiv.org/abs/2310.12485) — Gaussian Variational Approximation with Composite Likelihood for Crossed Random Effect Models
- **作者**: Libai Xu, Nancy Reid, Dehan Kong
- **期刊/来源**: Statistica Sinica
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对Poisson和Gamma回归中的交叉随机效应模型，提出了一种基于复合似然的Gaussian变分近似（GVA）方法。传统变分近似需要处理全似然函数，计算代价高；而复合似然通过忽略响应间的部分依赖来简化计算。作者推导了Gaussian变分近似的复合对数似然函数，并证明了由其导出的估计量具有相合性和渐近正态性。模拟研究验证了理论结果，并表明该方法在计算速度上显著优于基于全似然的Gaussian变分近似。该工作将变分推断与复合似然结合，在确保统计性质的前提下大幅提升计算效率，尤其适用于高维交叉随机效应模型。对于您的统计计算兴趣（数值方法与算法），本文展示了如何在实际模型中权衡近似精度与计算负担，并为变分近似的渐近理论提供了具体案例。
- **关键技术**: `Gaussian variational approximation`, `composite likelihood`, `crossed random effects`, `consistency and asymptotic normality`, `computational efficiency`
- **为什么对您有用**: 本文直接关联您的统计计算兴趣（数值方法与算法），特别是变分推断在复杂模型中的应用。您武器库中非常熟悉的“high-dimensional asymptotics”和“M-estimation theory”可用来审视其渐近结果的理论紧致性。同时，您可基于本文的GVA框架进一步探索更高效的计算策略（如小批量或自适应近似）——这属于立即可做的方向，因为您对渐近理论与估计理论已有充分储备。

### 3. [10.5705/ss.202024.0215](https://doi.org/10.5705/ss.202024.0215) — Distributed Sequential Federated Estimation
- **作者**: Zhanfeng Wang, Xinyu Zhang, Yuan-chin Chang
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `application`
- **摘要**: 该论文针对多站点分布式数据场景，提出了一种顺序联邦估计算法，以解决传统平均方法在数据非均匀性下可能产生的信息损失。方法结合序贯自适应设计，能够在每个站点逐步更新估计，同时保持通信高效性和隐私保护。通过序贯方法加速分析过程，并避免数据整合时的模型不匹配问题。理论部分建立了一类顺序融合估计量的渐近性质。数值实验和墨西哥32家医院COVID-19数据的回归分析验证了方法的有效性。对您而言，这是一篇聚焦分布式计算框架中统计推断的实证导向方法文章，链接到您对统计计算和软件方法的兴趣，但其方法论常规（加权序贯估计、无新理论突破），主要价值在于应用场景而非技术深度。
- **关键技术**: `sequential adaptive design`, `federated learning`, `distributed estimation`, `Oracle approximation`
- **为什么对您有用**: 本文属于统计计算方法在分布式数据场景下的应用，涉及您primary interest中的statistical computing方向。但方法本身未使用您武器库中的高阶U统计或半参效率工具，缺失核心前沿性。作为gateway阅读，本文可提供分布式序贯估计的入门案例，但方法论创新有限，不值得深读。

### 4. [10.5705/ss.202025.0109](https://doi.org/10.5705/ss.202025.0109) — Communication-Efficient Estimation of Regularized Smoothed Support Tensor Machine
- **作者**: Zihao Song, Lei Wang, Riquan Zhang, Weihua Zhao
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在分布式计算设定下，本文研究基于 tubal rank 的 regularized smoothed support tensor machine 的估计与通信效率问题，estimand 为具有低秩张量结构的分类边界，关键假设为张量数据具有 tubal 低秩结构且局部数据分片独立同分布。核心方法引入 tubal nuclear norm 替代传统 CP/Tucker 分解以保留张量内在结构，并提出一种 communication-efficient estimator：仅需第一台机器的局部数据与其余机器的梯度信息即可完成全局估计，避免了多轮数据传输。理论上证明了集中式估计量的收敛性质，并推导了分布式估计量的收敛率；利用 tubal nuclear norm 的性质给出了低秩结构恢复的理论保证。计算上采用交替方向算法求解。对您可能有用：分布式估计的通信效率框架与 tubal rank 的张量低秩恢复理论，直接连接到 statistical computing 与高维张量估计的 interest。
- **关键技术**: `tubal nuclear norm regularization`, `smoothed support tensor machine`, `communication-efficient distributed estimation`, `tubal rank recovery`, `alternating direction method`
- **为什么对您有用**: 本文连接到 statistical computing（分布式通信效率）与高维统计（张量低秩恢复）两个子方向。用您 very_familiar 的高维渐近理论与 minimax bound 工具，可以审视本文声称的分布式估计量收敛率是否紧致，以及 tubal nuclear norm regularizer 的低秩恢复条件是否可进一步削弱。follow-up 判断：**立即可做**——用 minimax rate 分析验证其收敛率的紧性，并对比传统矩阵 nuclear norm 与 tubal nuclear norm 在恢复阈值上的差异。

### 5. [10.5705/ss.202024.0379](https://doi.org/10.5705/ss.202024.0379) — Sliced Orthogonal Designs for Computer Experiments
- **作者**: Omar A. Alhelali, S.D. Georgiou, S. Stylianou
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验的设计问题，目标是构造 sliced orthogonal designs——一种 sliced Latin hypercube designs 的推广，使得每个 slice 构成正交子设计，同时整体设计对一阶与二阶模型均正交。构造方法利用零自相关序列（T-sequences、Golay sequences）与 disjoint amicable sequences，首次给出了此类设计的无穷族。生成的设计按文献中的多种准则（如最大投影距离等）进行评估并以表格呈现。对您可能有用：若您在统计计算方向关注实验设计的构造算法与数值实现，本文提供了基于序列组合的系统化构造流程。
- **关键技术**: `sliced orthogonal design`, `zero autocorrelation sequence (T-sequence / Golay sequence)`, `disjoint amicable sequence`, `Latin hypercube design`, `orthogonal array construction`
- **为什么对您有用**: 本文属于 stat_computing 中的实验设计构造，与您 primary interest 中的 statistical computing（numerical methods, algorithm）直接相关，但未触及高维推断或因果推断的核心理论。您武器库中的 software development 可直接用于实现文中基于 T-sequence / Golay sequence 的构造算法并验证其正交性，但理论深度较浅。follow-up 判断：立即可做——用 very_familiar 的 software development 实现构造程序并做数值评估，但若要推进理论（如最优性准则下的 minimax 界）需先在 moderately_familiar 的 M-estimation theory 上长肌肉。

### 6. [10.5705/ss.202025.0101](https://doi.org/10.5705/ss.202025.0101) · [arXiv](https://arxiv.org/abs/2312.06204) — Multilayer Network Regression with Eigenvector Centrality and Community Structure
- **作者**: Zhuoye Han, Tiandong Wang, Zhiliang Ying
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多层网络回归设定下，目标是利用跨层 eigenvector centrality 与 community structure 解释节点响应变量，模型假设层间/层内存在依赖结构且 centrality 带有测量误差。作者提出两阶段回归：第一阶段基于四阶 tensor-like 多层邻接矩阵提取 community-based centrality；第二阶段以这些 centrality 作为协变量做 least squares 回归。理论部分分别分析了 centrality 无测量误差和有测量误差两种情形，证明了 least squares 估计的一致性，但未给出收敛速率或 semiparametric efficiency bound。实证部分将方法应用于世界投入产出数据集，考察跨国/跨行业网络对行业总产出的影响。对您而言，本文的 tensor-like 多层邻接矩阵结构与 centrality 估计的测量误差校正，可作为高维统计与 tensor/einsum 计算交叉的入门案例。
- **关键技术**: `eigenvector centrality`, `community detection`, `multilayer network regression`, `measurement error correction`, `tensor-like adjacency representation`, `least squares consistency`
- **为什么对您有用**: 本文连接 stat_computing（tensor-like 多层邻接矩阵表示）与高维统计（eigenvector centrality 的测量误差），属于 gateway reading：tensor-like 结构与您 very_familiar 的 einsum/tensor contraction 计算直接相关，但理论深度较浅（仅一致性，无 rate 或 efficiency）。用您 very_familiar 的 higher-order U-statistics treewidth 视角可分析其 centrality 估计的计算代价；用 minimax bound 可验证其 consistency 结果是否可 sharpen 到 rate。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立 centrality 测量误差下的 n^{-1/2}-CAN 与 efficiency bound。

### 7. [10.5705/ss.202025.0279](https://doi.org/10.5705/ss.202025.0279) — Space-filling Designs with Kronecker Product Structures under Kernel-Based Criteria
- **作者**: Ruonan Zheng, Xinran Zhang, Jian-Feng Yang, Min-Qian Liu
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在计算机实验设计设定下，目标是系统建立各类 space-filling 准则之间的理论联系，并针对具有 Kronecker product 结构的设计给出显式表达与最优构造。核心机制是利用 kernel function 的代数性质，将常见的 space-filling 准则（如 discrepancy、distance-based）统一为 kernel 形式；在 Kronecker product 结构下，利用核函数的乘积分解性，推导出准则的显式分解公式与理论界。提出基于该结构的构造算法，生成的设计在多项准则下优于现有方法。对您有用：Kronecker product 与 tensor contraction / einsum 直接相关，本文的代数分解思路可借鉴到您 higher-order U-statistic 的 treewidth 计算复杂度分析中。
- **关键技术**: `Kronecker product structure`, `kernel-based space-filling criteria`, `discrepancy measure`, `design of computer experiments`, `tensor product decomposition`
- **为什么对您有用**: 本文连接到 stat_computing 与高维数值代数方向，其核心的 Kronecker product 分解正是您 very_familiar 中 tensor contraction / einsum 的直接应用场景。您可以用 einsum / treewidth 视角审视其构造算法的计算复杂度，甚至将 kernel 分解推广到更高阶 tensor 结构的设计准则。立即可做：用您已有的 tensor contraction 工具复现并优化其算法的数值实现。

## 经济理论 / 应用  *(econ_theory, 2 篇)*

### 1. [10.5705/ss.202024.0283](https://doi.org/10.5705/ss.202024.0283) — High-Dimensional-Responses-Assisted Heterogeneous Nodal Influence Analysis
- **作者**: Dongxue Zhang, Wei Lan, Danyang Huang, Huazhen Lin
- **期刊/来源**: Statistica Sinica
- **机构**: Southwestern University of Finance and Economics
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对 m×n 矩阵网络数据（m 个节点、每个节点对应 n 维响应），研究节点影响的异质性建模问题。假设节点影响参数通过链接函数与高维响应相关联，提出响应辅助网络影响模型。为避免传统最大似然估计失效，构建了“最优”广义矩方法（GMM）估计器，通过限制二次矩中权重矩阵的对角线来规避对未知误差方差的估计。证明了一致性和渐近正态性，并开发了同质性检验以检测影响异质性。通过基金和股票实证数据展示了模型的实际效用。作为经济应用方向的计量新方法，其 GMM 构造与高维网络数据整合思路对研究者处理复杂数据结构有启发，值得作为入门读物阅读。
- **关键技术**: `generalized method of moments`, `matrix network data`, `heterogeneous nodal influence`, `homogeneity test`, `high-dimensional responses`
- **为什么对您有用**: 本文属于经济理论方向（secondary interest）的计量方法论文，对于想了解网络数据分析的统计学者是较好的入门读物。研究者拥有高维渐近和估计理论的坚实基础（very_familiar），足以理解主要理论结果；但缺乏网络模型识别和 GMM 在异质性面板数据中的专门知识，需补充后（中期可做）才能在此方向进行原创工作。全文方法新颖且实证丰富，值得花时间阅读，尤其是 GMM 在矩阵响应网络下的构造思路对将来处理复杂数据结构有启发。

### 2. [10.5705/ss.202025.0450](https://doi.org/10.5705/ss.202025.0450) · [arXiv](https://arxiv.org/abs/2401.07038) — Bubble Modeling and Tagging: a Stochastic Nonlinear Autoregression Approach
- **作者**: Xuanling Yang, Dong Li, Ting Zhang
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文提出随机非线性自回归（SNAR）模型，用于刻画经济和金融时间序列中泡沫的局部爆炸动态行为。模型在特定参数范围外具有周期性爆炸特性，从而可模拟泡沫的形成与破灭。作者证明了该模型是严格平稳且几何遍历的，能捕捉宏观变量中的长摆动和持久性。采用拟极大似然估计（QMLE）进行参数推断，在极弱假设下建立了估计量的强一致性和渐近正态性。进一步构建了模型诊断检验统计量，用于评估拟合充分性。提出两种泡沫标记方法：基于残差和基于零状态视角，并通过蒙特卡洛模拟验证了有限样本性能。最后将模型应用于恒生指数月度数据，展示了实际可用性。对您可能有用：本文提供了泡沫建模与推断的完整框架，属于经济时间序列分析的应用，适合作为进入经济建模方向的入门阅读。
- **关键技术**: `Stochastic Nonlinear Autoregressive (SNAR) Model`, `Quasi-Maximum Likelihood Estimation (QMLE)`, `Model Diagnostic Checking Statistic`, `Bubble Tagging (Residual and Null-State Perspectives)`, `Geometric Ergodicity`
- **为什么对您有用**: （1）本文是经济时间序列泡沫分析的入门佳作：模型设定、估计、诊断、标记步骤清晰，无需深厚经济背景即可理解，适合作为研究者进入该领域的起点。（2）武器库方面：研究者熟悉非参统计、M估计、高维渐近理论，能够理解QMLE的渐近性质和诊断检验的构造；而深入强化非线性时间序列的混合性和鞅差CLT可能需要补充，但核心工具已足够支撑基本阅读和复现。（3）值得花时间读全文：泡沫检测是宏观经济学和金融领域的核心实证问题，本文提供了一套可操作的工具箱，结合研究者现有的时间序列与估计理论功底，可快速上手并尝试应用到因果推断中的结构断点检测或媒介分析等交叉问题。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.5705/ss.202025.0314](https://doi.org/10.5705/ss.202025.0314) — Transfer Learning for High-dimensional Regression with Compositional Covariates: Application to Microbiome Studies
- **作者**: Qinqin Hu, Xiaojing Luo, Chencheng Ma, Wang Zhou
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对微生物组研究中的高维成分回归问题，提出迁移学习方法以利用辅助源研究的信息，目标是在目标样本量有限时提高对含有成分协变量（如细菌相对丰度）和非成分协变量的回归模型的估计精度。采用中心对数比变换处理成分数据的线性约束，并通过约束的L1正则化估计（constrained Lasso）实现变量选择。提出了 Oracle-Trans-sub-Coda-Lasso（已知信息源）和 Trans-sub-Coda-Lasso（通过边际筛选统计量自动检测信息源）两种方法。在正则条件和源-目标相似性条件下，推导了 Oracle 估计量的 2-范数误差收敛速率，并证明了源检测过程的一致性。模拟和一项溃疡性结肠炎肠道微生物组数据上的 BMI 预测实验展示了方法相比传统成分回归的改进。该论文将高维统计方法应用于真实流行病学数据，对您的流行病学应用兴趣（尤其是微生物组数据建模）具有直接参考价值。
- **关键技术**: `Compositional regression via centered log-ratio transform`, `Constrained Lasso with subcomposition structure`, `Transfer learning with source detection by marginal screening`, `High-dimensional convergence rate of 2-norm error`
- **为什么对您有用**: 本文连接您的流行病学应用兴趣（微生物组数据预测）和高维统计兴趣（成分回归中的约束Lasso）。您武器库中的‘高维渐近’可直接用于验证其理论收敛速率，‘软件开发’可用于复现方法并应用到类似肠道菌群数据。因此，这是一项可立即可做的工作：在理解方法后即可尝试在其他流行病学队列中实施该迁移学习框架。

## 其他  *(other, 6 篇)*

### 1. [10.5705/ss.202025.0147](https://doi.org/10.5705/ss.202025.0147) — Effects-Nested Multi-Level Supervised Heterogeneity Analysis
- **作者**: Ruiyue Wang, Sanguo Zhang, Shuangge Ma
- **期刊/来源**: Statistica Sinica
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该文提出一种多层级监督异质性分析方法（Effects-Nested Multi-Level Supervised Heterogeneity Analysis），适用于样本存在多层级分组结构且回归系数随组别变化的情形。以两层结构为例：高层利用“粗”信息将样本分为较少组，低层利用“细”信息分为较多亚组，且高层重要变量嵌套于低层重要变量中。方法采用惩罚估计同时实现变量选择和分组识别，并建立了估计量的理论性质（如一致性、选择相合性）和计算收敛性。模拟显示该方法在分组准确性和回归系数估计上优于单层方法。在TCGA乳腺癌数据分析中，得到了合理的分组和变量识别结果。该方法拓展了监督异质性分析的范围，但对您而言，其核心是惩罚回归与嵌套结构，并不直接连接您的主要兴趣方向。可作为高维统计中变量选择方法的一个应用变体参考。
- **关键技术**: `penalized estimation`, `multi-level clustering`, `nested variable selection`, `group lasso`, `supervised heterogeneity analysis`
- **为什么对您有用**: 本文涉及高维惩罚估计和变量选择，与您主要兴趣中的‘高维统计’有微弱关联。您可以用熟悉的minimax界技术审视其变量选择相合性的理论证明是否紧，但方法本身不涉及causal inference、U-statistics或效率理论。武器库中‘高维渐近’工具可用于评估其收敛速率，但无直接突破点。建议作为应用统计方法参考，暂无需深入阅读。

### 2. [10.5705/ss.202025.0148](https://doi.org/10.5705/ss.202025.0148) — Identification and Estimation of General Nonlinear Structured Latent Factor Model for Functional Data
- **作者**: Xiaorui Wang, Yimang Zhang, Jian Qing Shi
- **期刊/来源**: Statistica Sinica
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对函数型数据，提出一类非线性结构潜变量模型，通过引入潜因子之间的相关性刻画数据的时间依赖性。利用高斯过程先验对未知非线性链接函数进行建模，并采用近邻高斯过程（NNGP）近似以提升计算效率。理论上，建立了潜因子和参数的一致性以及链接函数的后验一致性，同时讨论了结构化可识别性条件以确保潜因子的物理可解释性。仿真和步态数据应用展示了模型在灵活性和计算时间上的优势。本文方法学核心是贝叶斯非参数潜变量模型，与研究者主力方向（因果推断、U统计量、统计-计算权衡）距离较远，但非参数理论和计算加速技术仍有一定参考价值。
- **关键技术**: `Gaussian Process prior`, `Nearest Neighbor Gaussian Process (NNGP)`, `Structured latent factor model`, `Posterior consistency`, `Identifiability for latent factor models`
- **为什么对您有用**: 本文涉及非线性潜变量模型的可识别性和后验一致性，与研究者熟悉的非参数统计和M估计理论有交集。NNGP加速技术对大规模函数型数据计算有实际意义，但研究者擅长的树宽/张量收缩分析并未在本文中使用。作为非核心方向，可快速浏览了解非参数潜变量模型的理论工具，但暂不展开深入。

### 3. [10.5705/ss.202026.0029](https://doi.org/10.5705/ss.202026.0029) · [arXiv](https://arxiv.org/abs/2601.12031) — Estimations of Extreme Covar and Coes Under Asymptotic Independence
- **作者**: Qingzhao Zhong
- **期刊/来源**: Statistica Sinica
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文在两随机变量渐近独立但正相关的设定下，研究极端尾部系统性风险度量 CoVaR 与 CoES 的估计问题。提出两类外推方法：第一类基于中间水平的 VaR 并通过调整因子外推至极端 CoVaR/CoES；第二类直接将中间水平的 CoVaR/CoES 估计外推至极端尾部。所有中间与极端估计量均被证明具有渐近正态性，并通过 Monte Carlo 模拟与 S&P500 成分股数据验证了实证表现。对您可能有用：若关注经济金融中的尾部风险估计，本文提供了渐近独立假设下极值外推的具体渐近正态工具。
- **关键技术**: `extreme value extrapolation`, `asymptotic normality of tail estimators`, `CoVaR / CoES estimation`, `asymptotic independence assumption`, `intermediate quantile extrapolation`
- **为什么对您有用**: 本文属于经济理论（金融系统性风险度量）的应用极值统计工作，与您 primary interests 中的高维/半参数/效率理论无直接交集。技术层面，其渐近正态证明依赖经典极值理论工具，您武器库中的 minimax bounds 与 M-estimation theory 可用于审视其估计量是否达到半参数有效界，但本文并未涉及此讨论。follow-up 判断：**暂不可做**——极值统计与尾部外推的核心机器不在武器库中，需先补足渐近独立下的极值极限定理与 Hill-type 估计量理论。

### 4. [10.5705/ss.202025.0049](https://doi.org/10.5705/ss.202025.0049) — Mirror-Symmetric Orthogonal Latin Hypercubes with Attractive Space-Filling Properties
- **作者**: Chunyan Wang, Min-Qian Liu
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验设计中镜像对称正交拉丁超立方体的构造问题。目标是在满足正交性与一维最大分层的同时，利用镜像对称结构获得高阶正交性，以提升主效应与交互效应的辨识能力。作者利用基于Reed-Solomon码的正交数组，提出了一种显式构造方法，并从理论上证明所得设计具有优良的正交性和低维空间填充性质。部分设计在最大最小距离准则下达到最优。仿真比较表明，新设计优于现有方案。本文与您的核心研究兴趣（因果推断、非参数理论、U统计量等）直接关联较弱，但可作为统计设计中组合构造的一个参考案例。
- **关键技术**: `Orthogonal array`, `Reed-Solomon codes`, `Maximin distance criterion`, `Mirror symmetry`, `Latin hypercube design`
- **为什么对您有用**: 本文主题为计算机实验设计，与您的主要兴趣（因果推断、高维统计等）直接匹配较低。但其正交数组构造方法涉及组合设计与有限域，可在统计计算领域拓宽思路。您当前的武器库中缺少组合设计的专门工具，故目前暂不可做直接跟进，但若未来接触涉及实验设计的问题，本文可作为入门参考。

### 5. [10.5705/ss.202025.0187](https://doi.org/10.5705/ss.202025.0187) — Inference for A Two-Step Joint Model of Extreme Quantile and Expected Shortfall Regression
- **作者**: Qingzhao Zhong, Jingyu Ji, Liujun Chen, Yanxi Hou, Deyuan Li
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究极端分位数与期望损失（Expected Shortfall, ES）联合回归模型中的推断问题。ES作为一致性风险度量，与分位数回归结合可刻画协变量对响应变量尾部风险的条件效应，但极端水平下尾部观测稀疏导致现有方法估计困难。作者提出一个两步骤联合模型：先估计极端分位数（如使用极值理论中的POT方法或广义帕累托近似），再基于分位数回归系数构造ES回归估计量，并给出回归系数的置信区间。方法在理论上证明了估计量的渐近正态性，并通过模拟和实证研究验证了有限样本表现。本文的核心技术包括极值理论中的尾部建模、分位数回归的极端水平外推以及两步估计的方差校正。对您而言，本文属于经济金融风险度量的方法论，可作为经济理论应用中极值回归的入门参考。
- **关键技术**: `extreme quantile regression`, `expected shortfall regression`, `two-step estimation`, `tail semiparametric modeling`, `Peaks Over Threshold method`, `confidence intervals for ES coefficients`
- **为什么对您有用**: 本文属于经济金融风险度量的应用统计方法，对应您的secondary interest中的经济理论应用方向。但当前武器库中缺少极值理论工具（如广义帕累托分布、阈值选择），暂不可直接复现或扩展。作为gateway reading，可帮助您了解极端分位数回归与ES推断的基本框架。

### 6. [10.5705/ss.202025.0285](https://doi.org/10.5705/ss.202025.0285) — Bi-optimal Quantile-based Test Planning for Accelerated Degradation Test Based on Wiener Process
- **作者**: Ya-Shan Cheng, Chien-Yu Peng
- **期刊/来源**: Statistica Sinica
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文针对基于Wiener过程的加速退化试验，研究双最优分位数测试计划问题。传统方法通过最小化估计的q分位数近似方差来确定样本量、终止时间和测量次数，但通常只优化单一准则。本文理论推导了同时满足两个最优性准则的bi-optimal测试计划存在的充要条件及其唯一性。该方法可以在有限资源下实现100%效率的双目标优化。通过两个数值例子验证了实际适用性。本文的工作对可靠性工程的测试设计有参考价值，但与研究者当前的核心兴趣（因果推断、高维统计）关联较弱。
- **关键技术**: `Wiener process`, `bi-optimal test plan`, `quantile-based optimality`, `accelerated degradation test`, `approximate variance minimization`
- **为什么对您有用**: 本文属于实验设计和可靠性统计的优化问题，与研究者主要兴趣方向（因果推断、高维统计、非参理论等）无直接交集。不过，其推导存在性和唯一性的理论框架对于统计计算和优化方法有一定可借鉴性，但武器库中缺乏相关背景（如Wiener过程推断、加速寿命试验），因此暂不可做。如果研究者打算拓展到工程可靠性或时间序列退化建模，本文可作为入门文献。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

