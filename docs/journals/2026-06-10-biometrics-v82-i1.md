# Biometrics — Vol 82  Issue 1  ·  2026-06-10

- 共 8 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 42 篇（对照 OpenAlex 59 篇）：10.1093/biomtc/ujaf132、10.1093/biomtc/ujaf169、10.1093/biomtc/ujaf177、10.1093/biomtc/ujag052、10.1093/biomtc/ujaf109 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》的六篇论文大致可归为三条主线：**因果推断中的识别与估计权衡**（两篇）、**半参数/非参数推断**（两篇）、以及**流行病学中的建模与监测**（两篇）。因果主线聚焦于处理协变量重叠不足时的 estimand 选择与分布式 ITR 学习；半参数主线关注异质性变量重要性的推断与混合效应 ODE 模型的估计；流行病学主线则涉及环境混合物暴露分组建模与报告延迟的 nowcasting。

因果推断主线中，**“A framework for causal estimand selection under positivity violations”** 将总偏差分解为统计偏差与 estimand mismatch 偏差，并引入 design-based metrics 指导 estimand 选择，直接回应了重叠不足下 ATE 与 overlap weighting 之间的经典两难。**“Scalable and distributed individualized treatment rules for multicenter datasets”** 则通过卷积平滑加权 SVM 实现分布式 ITR 学习，在固定通信轮数下达到最优价值函数收敛率，其凸平滑技术为统计-计算权衡提供了新工具。两篇分别从 estimand 层面和算法层面推进了因果推断的实用性。

半参数/非参数主线中，**“A general framework for heterogeneous variable importance: Pointwise and uniform inference”** 将变量重要性定义为条件均方误差之比，并建立逐点与均匀收敛率及置信带，本质是条件期望之比的半参数推断问题，涉及 empirical process 工具。**“Estimation of mixed-effects ordinary differential equation models linear in the parameters”** 虽标题为 ODE 模型，但摘要实际聚焦于微生物-代谢物关联网络中的多重检验，引入二分随机块模型刻画图结构以提升 FDR 控制功效，将随机块模型与假设检验结合。流行病学主线中，**“Multiple-index interaction models to accommodate exposure grouping in environmental mixtures”** 提出半参数多指标交互模型，将高维暴露按生物学特征分组为组级指标，允许组内非线性与组间交互，适用于连续、二元及生存结局。**“Bayesian nowcasting for delay adjustments using time-varying parametric functions of cumulative reporting probability”** 则用 Bayesian 层次模型处理报告延迟，以时变参数捕捉报告行为变化，在非完全报告环境下优于传统方法。

与因果推断方向最贴的是前两篇（estimand 选择与分布式 ITR）；半参数效率方向可关注变量重要性论文中的均匀推断与 empirical process 应用；高维/假设检验方向可看 ODE 模型论文中的随机块模型与 FDR 控制结合。


## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biomtc/ujag017](https://doi.org/10.1093/biomtc/ujag017) · [arXiv](https://arxiv.org/abs/2404.18256) — Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects
- **作者**: Chao Cheng, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在 cluster-randomized trials (CRTs) 设定下，本文研究 cluster-level treatment 通过 intermediate outcome 影响个体结局的因果中介机制，目标 estimands 包括 natural indirect effect、individual mediation effect 与 spillover mediation effect（他人中介对自身结局的影响）。现有 CRT 中介方法均依赖参数假设；本文建立 semiparametric efficiency theory，推导每个 estimand 的 efficient influence function (EIF)，并据此构造 doubly-robust (DR) estimator。nuisance function 的估计既可用 parametric working models 也可用 data-adaptive machine learners（配合 cross-fitting），后者达到 semiparametric efficiency bound。模拟与真实 CRT 数据验证了有限样本表现。对您有用：本文将 semiparametric efficiency + DR + DML 框架系统性地扩展到 CRT 的 spillover mediation，直接连接 causal inference (mediation, spillover) 与 efficiency theory (EIF, debiased ML) 两个 primary interests。
- **关键技术**: `efficient influence function`, `doubly-robust estimation`, `semiparametric efficiency bound`, `spillover mediation effect`, `cross-fitting with machine learners`, `cluster-randomized trials`
- **为什么对您有用**: 直接连接 causal inference 的 mediation 与 spillover 子方向，以及 efficiency theory 的 EIF / debiased ML 子方向。可用 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory / HOIF 直接审视其 EIF 推导与 DR 构造，判断 spillover mediation estimand 的 identification 条件是否可进一步弱化或扩展到更高阶 influence function 以加速收敛。立即可做：用现有武器复现 EIF 推导并检查其 nuisance parameter 的 orthogonal score 结构。

### 2. [10.1093/biomtc/ujag014](https://doi.org/10.1093/biomtc/ujag014) — A framework for causal estimand selection under positivity violations
- **作者**: Martha Barnard, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biometrics
- **机构**: University of Minnesota
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在观察性研究中处理协变量分布重叠不足（positivity violation）时，研究者常面临两难：使用 IPW 等方法估计传统 estimand（如 ATE）会引入巨大偏差与方差，而使用 overlap weighting 等方法虽能降低方差却改变了目标人群、造成 estimand mismatch。本文提出一个在方差、统计偏差与 estimand mismatch 之间权衡的框架，将总偏差分解为（1）估计器的统计偏差与（2）因目标人群偏离而产生的 estimand mismatch 偏差。作者引入两个 design-based metrics 及 estimand 选择程序，允许分析者根据领域偏好（保留原始研究人群 vs. 降低统计偏差）进行决策，并在右心导管化数据集上展示了应用。对您可能有用：本文的偏差分解与 estimand 选择框架直接关联 causal inference 中 positivity / overlap 问题，为 sensitivity analysis 与 estimand 选择提供了新视角。
- **关键技术**: `bias decomposition`, `estimand mismatch`, `overlap weighting`, `inverse probability weighting`, `design-based metrics`, `positivity violations`
- **为什么对您有用**: 本文直接针对 causal inference 中 positivity violation 下的 estimand 选择问题，属于您 primary interest 中因果推断的 identification 与 estimation 子方向。偏差分解框架将 estimand mismatch 与统计偏差分离，可用您 very_familiar 的 estimation theory in causal inference 工具审视其分解的严密性与选择程序的理论性质。立即可做：用您熟悉的 minimax / efficiency 视角评估该框架下不同 estimand 的 semiparametric efficiency bound，或将其与 sensitivity analysis 结合。

### 3. [10.1093/biomtc/ujag003](https://doi.org/10.1093/biomtc/ujag003) — Scalable and distributed individualized treatment rules for multicenter datasets
- **作者**: Nan Qiao, Wangcheng Li, Jingxiao Zhang, Canyi Chen
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · Beijing Normal University · University of Michigan
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多中心隐私数据设定下，目标是学习最优个体化治疗规则（ITR），避免汇集原始数据。作者提出卷积平滑加权支持向量机（convolution-smoothed weighted SVM），其损失函数经平滑后为凸且光滑，从而支持多轮分布式学习。分布式算法在固定通信轮数下达到最优统计性能（价值函数收敛率），避免了经典 meta-learning 平均局部有偏估计的缺陷。优化层面开发了坐标梯度下降算法，保证至少线性收敛。模拟与多 ICU 脓毒症治疗数据验证了方法有效性。对您可能有用：分布式 ITR 估计中的统计-计算权衡与凸平滑技术，可连接到因果推断的 ITR 估计与统计计算方向。
- **关键技术**: `individualized treatment rule`, `convolution-smoothed weighted SVM`, `distributed learning`, `coordinate gradient descent`, `value function estimation`, `multi-center data integration`
- **为什么对您有用**: 本文直接连接因果推断中的个体化治疗规则（ITR）估计，并涉及统计计算（分布式优化、坐标梯度下降、通信轮数与统计收敛率的权衡）。用 very_familiar 中的软件开发与高维渐近理论可以审视其收敛率声称是否紧；moderately_familiar 的 M-estimation 理论可用于分析平滑 SVM 估计量的渐近性质。立即可做：用 M-estimation 理论验证其凸平滑估计量的影响函数与效率性质。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1093/biomtc/ujag015](https://doi.org/10.1093/biomtc/ujag015) — A general framework for heterogeneous variable importance: Pointwise and uniform inference
- **作者**: Lingxuan Shao, Guorong Dai, Jinbo Chen
- **期刊/来源**: Biometrics
- **机构**: Fudan University · University of Pennsylvania
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在非参数预测框架下，本文研究“异质性变量重要性”——某协变量对响应变量的解释贡献如何随特征变量（如年龄）变化，目标参数定义为两个条件均方误差之比（条件非参数光滑参数）。提出该比率参数的点估计量，分别建立逐点收敛率与均匀收敛率；基于收敛理论构造逐点置信区间与均匀置信带，保证达到名义覆盖率。模拟研究与实证数据验证了有限样本表现。对您有用：该比率参数本质是条件期望之比的半参数推断问题，均匀置信带涉及 empirical process 工具，直接连接您的半参数理论与假设检验兴趣。
- **关键技术**: `ratio of conditional MSEs`, `pointwise convergence rate`, `uniform convergence rate`, `asymptotic confidence bands`, `conditional nonparametric estimation`, `empirical process`
- **为什么对您有用**: 本文目标参数（条件MSE之比）是典型的半参数光滑参数，其逐点与均匀推断直接触及您的 semiparametric theory 和 hypothesis testing 两个 primary interest 子方向。用您 moderately_familiar 的 M-estimation theory 和 semiparametric theory 可以审视其 influence function 构造与收敛率是否达到 semiparametric efficiency bound。follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上确认其估计量是否可嵌入 HOIF 框架以刻画更高阶余项，进而判断均匀推断的 rate 是否可 sharpen。

### 2. [10.1093/biomtc/ujag016](https://doi.org/10.1093/biomtc/ujag016) — Estimation of mixed-effects ordinary differential equation models linear in the parameters
- **作者**: Oleksandr Laskorunskyi, Snigdhansu Chatterjee, Itai Dattner
- **期刊/来源**: Biometrics
- **机构**: University of Haifa · University of Maryland, Baltimore County
- **分类**: vol 82 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究参数线性但状态非线性的混合效应 ODE 模型的固定效应与随机效应估计，支持单层、嵌套与交叉随机效应结构。核心方法 Direct Integral Mixed-Effects (DIME) 利用参数与状态的分离性，通过积分变换将非线性 ODE 问题重构为线性混合效应模型框架，从而可直接调用标准 LMM 推断工具（置信区间、模型选择）。理论方面给出了估计量的一致性与渐近正态性保证；模拟中 DIME 在小样本方差分量估计的 coverage 上优于 nlme/nlmixr2 的非线性混合效应方法，且在后者无法适用的交叉结构下仍可运行。对您可能有用：DIME 的积分重构思路与 semiparametric theory 中 profiling / sieve 的降维策略有结构相似性，可作为 ODE 约束下 semiparametric 推断的入门案例。
- **关键技术**: `linear mixed-effects model`, `ODE parameter-state separability`, `integral transformation`, `consistency and asymptotic normality`, `crossed random effects`, `profile likelihood`
- **为什么对您有用**: 本文连接到 semiparametric theory 子方向：ODE 模型中参数线性但状态非线性，本质上是一个 semiparametric 约束问题，DIME 的积分重构相当于把 nuisance（状态轨迹）投影到有限维空间。用 technical_arsenal 中 very_familiar 的 M-estimation theory 可以直接验证其渐近正态性条件是否满足常规 regularity；moderately_familiar 的 semiparametric theory 可用来审视 DIME 是否达到 semiparametric efficiency bound（当前论文未讨论效率）。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric efficiency bound 上长肌肉，计算该模型的 efficient influence function 并与 DIME 的线性重构对比，看是否存在效率损失。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biomtc/ujag042](https://doi.org/10.1093/biomtc/ujag042) · [arXiv](https://arxiv.org/abs/2506.12275) — Inference for microbe–metabolite association networks using a latent graph model
- **作者**: Jing Ma
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究在微生物-代谢物关联网络推断中，当p值因潜在图拓扑结构（如密集关联模块）而产生强依赖时，传统BH程序控制FDR的功效不足问题。目标是在保持FDR控制的同时提高检测显著关联的功效。方法核心是引入二分随机块模型刻画潜在图结构，通过变分EM算法估计模型参数，并将学习到的图结构融入多重检验过程以提升功效。该方法同时提供微生物与代谢物的模块聚类，便于生物学解释。实证分析在模拟和细菌性阴道病数据集上验证了方法优势。对您可能有用：本文将随机块模型与多重检验结合，直接连接到您的 hypothesis testing 兴趣，同时提供了流行病学微生物组数据集。
- **关键技术**: `bipartite stochastic block model`, `variational EM algorithm`, `FDR control under dependence`, `multiple testing`, `latent graph model`
- **为什么对您有用**: (1) 连接到 hypothesis testing 中的 FDR 控制与依赖结构，以及 epidemiology 中的微生物组数据集；(2) 您 moderately_familiar 的 M-estimation theory 可用于分析变分EM估计量的收敛性，或用 minimax bounds 评估该检验的最优功效界；(3) 中期可做：需先在 moderately_familiar 的 M-estimation 上长肌肉以分析变分推断的理论性质，或学习随机块模型的谱方法理论。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biomtc/ujaf175](https://doi.org/10.1093/biomtc/ujaf175) — Multiple-index interaction models to accommodate exposure grouping in environmental mixtures
- **作者**: Myeonggyun Lee, Mengling Liu, Shanshan Zhao
- **期刊/来源**: Biometrics
- **机构**: National Institute of Environmental Health Sciences · New York University
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在环境混合物的流行病学研究中，目标是评估按生物学特征分组的暴露对健康结局的影响，设定为半参数多指标交互模型（MIIM）。MIIM 通过将高维暴露汇总为组级指标来应对维度挑战，同时允许组内非线性效应与组间交互。该框架支持连续、二元及生存结局，提供组级整体效应与组间交互的可解释洞察，并允许识别组内关键暴露。Monte Carlo 模拟评估了高维相关暴露下的性能，NHANES 数据实证分析了三类持久性有机污染物对白细胞端粒长度的影响。对您可能有用：作为流行病学环境混合物分析的半参数方法参考，NHANES 数据集为 epi 方向的因果/关联推断提供了具体案例。
- **关键技术**: `semiparametric multiple-index model`, `environmental mixtures`, `group-level index dimension reduction`, `between-group interaction`, `NHANES dataset`
- **为什么对您有用**: 本文连接到 epidemiology secondary interest 的环境混合物数据集与模型设定，提供了 NHANES 实际数据与 MIIM 框架。您 technical_arsenal 中 moderately_familiar 的 semiparametric theory 可以用来审视 MIIM 的多指标模型部分是否达到半参数效率界或存在更优的 debiased 估计路径。Follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体考察多指标模型的效率界与估计理论。

### 2. [10.1093/biomtc/ujag020](https://doi.org/10.1093/biomtc/ujag020) — Bayesian nowcasting for delay adjustments using time-varying parametric functions of cumulative reporting probability
- **作者**: Erick A Chacón-Montalván, Yang Xiao, Paula Moraga
- **期刊/来源**: Biometrics
- **机构**: National University of Engineering · King Abdullah University of Science and Technology
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对流行病学实时监测中报告延迟导致真实病例数被遮蔽的问题，提出了一种 Bayesian 层次模型进行 nowcasting。模型用灵活参数形式刻画累积报告比例，并引入时变参数（random walk 或 Ornstein–Uhlenbeck 过程）以捕捉报告行为的变化。6 个模拟场景及真实数据应用表明，该方法在非完全报告和动态报告环境下优于传统 nowcasting 方法。核心估计策略是 Bayesian posterior inference，而非 semiparametric efficiency 或 debiased ML 路线。对您而言，本文提供了流行病学延迟报告的数据结构与问题设定，但方法论层面（Bayesian hierarchical）与您关注的 causal inference / semiparametric 工具链不直接对接。
- **关键技术**: `Bayesian hierarchical nowcasting`, `time-varying parametric reporting curve`, `Ornstein-Uhlenbeck process`, `random walk smoothness prior`, `cumulative reporting probability`
- **为什么对您有用**: 本文属于流行病学（secondary interest）的应用论文，提供了报告延迟数据的问题设定与真实数据集，但方法论是 Bayesian hierarchical 而非您关注的 causal inference / IV / semiparametric 路线。若想从 identification 视角重新审视延迟报告的 nowcasting 问题（将未观测完整报告视为 missing data / selection 问题），可用您 very_familiar 的 inverse problems with random noise 框架切入，但本文本身未走此路线。**中期可做**：需先在 moderately_familiar 的 identification theory in causal inference 上构建延迟报告的 identification 方案，再与 semiparametric efficiency 结合，方可提出替代性非 Bayesian 方法。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

