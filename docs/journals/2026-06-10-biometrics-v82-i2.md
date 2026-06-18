# Biometrics — Vol 82  Issue 2  ·  2026-06-10

- 共 42 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 3 篇（对照 OpenAlex 50 篇）：10.1093/biomtc/ujag008、10.1093/biomtc/ujag007、10.1093/biomtc/ujag005

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biometrics》第82卷第2期共18篇论文，整体围绕**因果推断与效率提升**、**半参数/非参数方法**、**高维与异质性数据建模**、以及**临床试验与流行病学设计**四条主线展开。因果推断主线集中处理多时间点中介分析、个性化治疗设计与异质性因果效应，涉及目标最大似然估计、Q-learning与贝叶斯加性回归树等工具。半参数/非参数主线关注转移学习、交互效应分析与效率界收紧，涵盖加速失效时间模型、随机对照试验中的高效交互分析。高维与异质性主线包括分布式生存数据异质性学习、零膨胀层次变换模型与知识引导双聚类，处理大规模数据与噪声图谱。临床试验与流行病学主线覆盖两阶段设计、成本-效果分析与安全性监测，强调间歇观察与终止事件下的推断。

在因果推断与效率提升主线中，**Targeted maximum likelihood estimation for mediation analysis with multiple time-varying mediators** 将AUMCF作为多事件时间设定下的因果estimand，发展augmentation estimator以提升效率并处理终止性竞争风险。**Personalized treatment design in the context of functional confounding** 针对clustered adaptive intervention中的非正则性问题，提出clustered Q-learning配合M-out-of-N cluster bootstrap。**Heterogeneous causal mediation analysis using Bayesian additive regression trees** 在SMART框架下利用贝叶斯后验概率实现响应自适应随机化，优化病理完全缓解率。**Efficient interaction analysis in randomized controlled trials** 利用外部二值化数据收紧semiparametric efficiency bound，保证效率提升。**Heterogeneity learning in distributed networks with large-scale survival data** 通过Distributed Spanning-Tree-Based Fused Lasso识别跨节点异质性系数，但未涉及效率界推导。

在半参数/非参数与高维主线中，**Transfer learning estimation of the accelerated failure time model based on high-dimensional data** 在去中心化联邦学习下提出momentum network EM，实现异质数据下的渐近有效估计。**A zero-inflated hierarchical generalized transformation model** 通过层次变换处理空间转录组数据的零膨胀问题，但处于生物信息学语境。**Knowledge-guided Bayesian biclustering model for omics data with noisy graphs** 显式建模图谱假阳性与假阴性，避免传统方法因图谱误设导致的偏误。**Mixed membership latent variable model with unknown factors** 针对noncollapsible效应量提出基于nonparanormal模型的调整边际推断，理论证明调整预后变量可提高估计精度。

与因果推断方向最贴的论文包括：**Targeted maximum likelihood estimation for mediation analysis with multiple time-varying mediators**（多时间点中介分析）、**Personalized treatment design in the context of functional confounding**（个性化治疗设计）、**Heterogeneous causal mediation analysis using Bayesian additive regression trees**（异质性中介分析）、**Efficient interaction analysis in randomized controlled trials**（效率界收紧）。与半参数效率方向最贴的包括：**Transfer learning estimation of the accelerated failure time model**（联邦学习下的渐近效率）、**Efficient interaction analysis**（效率界收紧）。与高维方向最贴的包括：**Heterogeneity learning in distributed networks with large-scale survival data**（分布式异质性学习）、**Knowledge-guided Bayesian biclustering model**（噪声图谱整合）。


## 因果推断  *(causal_inference, 14 篇)*

### 1. [10.1093/biomtc/ujag102](https://doi.org/10.1093/biomtc/ujag102) — Targeted maximum likelihood estimation for mediation analysis with multiple time-varying mediators
- **作者**: Yan-Lin Chen, Yun-Hao Chang, Sheng-Hsuan Lin
- **期刊/来源**: Biometrics
- **机构**: National Yang Ming Chiao Tung University · National Dong Hwa University
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在 causally ordered multiple time-varying mediation 设定下，目标是将 total effect (TE) 分解为多个 path-specific effects (PSEs) 并保证 PSEs 之和等于 TE，以解决既有方法无法处理多时变中介互馈动态与效应不可加的问题。本文推导了各 PSE 的 efficient influence function (EIF)，并基于此构建了 targeted maximum likelihood estimation (TMLE) 估计量。该估计量具备 multiple robustness、$n^{-1/2}$-CAN 及局部渐近效率等优良性质。理论证明了在多重稳健条件下的渐近性质，并在 COPD 流行病学数据中展示了 dyspnea 与 physical inactivity 的互馈中介路径。对您有用：本文直接推进了 longitudinal mediation 的 semiparametric efficiency bound 推导与 TMLE 估计，是因果推断中介分析方向的典型工作。
- **关键技术**: `path-specific effects (PSEs)`, `efficient influence function (EIF)`, `targeted maximum likelihood estimation (TMLE)`, `multiple robustness`, `time-varying mediation decomposition`
- **为什么对您有用**: 直接对应 primary interest 中的 causal inference (mediation, longitudinal) 与 efficiency theory (semiparametric efficiency bounds)，并在 epidemiology 数据上做了应用。用您 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 即可审视其 EIF 推导与 multiple robustness 条件的完备性。**立即可做**：您现有的 semiparametric/CI estimation 武器库完全足够复现其 EIF 推导并验证 TMLE 的 robustness 条件，甚至可尝试用 HOIF 推进其高维 nuisance parameter 下的 debiased 估计。

### 2. [10.1093/biomtc/ujag057](https://doi.org/10.1093/biomtc/ujag057) · [arXiv](https://arxiv.org/abs/2406.00940) — Measurement error-robust causal inference via constructed instrumental variables
- **作者**: Caleb H Miles, Linda Valeri, Brent Coull
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在测量误差干扰下估计因果效应（含误差混杂的 ATE、含误差暴露/混杂的 NIE），传统方法依赖外部数据或已知误差分布，本文在 outcome regression 对误差变量线性的假设下，提出无需外部信息的 constructed IV 方法。构造的 IV 仅依赖观测数据函数，在满足特定条件时充当误差变量的有效 IV，从而恢复 ATE 和自然间接效应的一致估计。无需外部验证数据或误差分布先验知识是核心突破，但代价是 outcome model 必须对误差变量线性。理论上证明了估计的一致性，并在孟加拉国母婴队列（重金属暴露与神经发育）中实证分析了铅暴露与蛋白质摄入的因果/中介效应。对您有用：直接连接因果推断的 IV 与 mediation 子方向，且提供了流行病学真实数据的应用范例。
- **关键技术**: `constructed instrumental variables`, `measurement error correction`, `natural indirect effect`, `outcome regression linearity`, `internal validation-free estimation`
- **为什么对您有用**: 直接连接 causal inference 的 IV 与 mediation 子方向，以及 epidemiology 的真实队列数据应用。从 semiparametric theory 视角，可审视其 outcome 线性强假设是否可放松至半参模型，或用 HOIF 探究其效率界。Follow-up：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，尝试将 constructed IV 推广到非线性/半参 outcome regression，或推导其 semiparametric efficiency bound。

### 3. [10.1093/biomtc/ujag082](https://doi.org/10.1093/biomtc/ujag082) · [arXiv](https://arxiv.org/abs/2410.08849) — Causal inference targeting a concentration index for studies of health inequalities
- **作者**: Mohammad Ghasempour, Xavier de Luna, Per E Gustafsson
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在因果推断框架下，本文研究暴露（如教育）对收入相关健康不平等测度——集中指数（健康变量与收入秩的标准化协方差）的效应，定义了反事实集中指数作为目标 estimand。给出了该复杂 estimand 的 identification 条件，并推导了其有效影响函数（efficient influence function）。基于 EIF 提出了正则渐近线性（RAL）估计量，证明了其 √n-一致性、渐近正态性及局部有效性。估计量的实现依赖于多个 nuisance 函数的拟合，且具备 rate robustness（部分 nuisance 函数收敛速率可慢于 √n），体现了 orthogonal score 的性质。通过模拟验证了有限样本渐近性质，并在瑞典流行病学队列数据上进行了教育对健康不平等效应的实证分析。对您有用：本文将 semiparametric efficiency theory 与复杂因果 estimand 的 identification 结合，直接连接您 primary interest 中的因果推断 identification/estimation 与 efficiency theory，以及 secondary interest 中的流行病学应用。
- **关键技术**: `efficient influence function`, `counterfactual concentration index`, `regular asymptotic linear estimator`, `rate robustness`, `identification conditions`, `nuisance function estimation`
- **为什么对您有用**: 本文直接连接您 primary interest 中的因果推断 identification/estimation 与 efficiency theory（EIF/RAL），以及 secondary interest 中的流行病学队列实证因果分析。您可用 moderately_familiar 的 "semiparametric theory" 和 "identification theory in causal inference" 审视其 EIF 推导与 identification 条件的完备性，用 very_familiar 的 "estimation theory in causal inference" 评估其 rate robustness 的具体形式。Follow-up 粗判：**立即可做**——您现有武器库完全覆盖本文理论工具，可直接复现其 EIF 推导或将其 estimand 框架推广到 longitudinal/mediation 设定。

### 4. [10.1093/biomtc/ujag053](https://doi.org/10.1093/biomtc/ujag053) · [arXiv](https://arxiv.org/abs/2412.09304) — Nonparametric estimation of the total treatment effect with multiple outcomes in the presence of terminal events
- **作者**: Jessica Gronsbell, Zachary R McCaw, Isabelle-Emmanuella Nogues, Xiangshan Kong, Tianxi Cai, Lu Tian et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在存在终止性竞争风险（如死亡或提前停药）的多事件时间设定下，目标是估计总处理效应，以 AUMCF（area under the mean cumulative function）作为 estimand——它是 restricted mean survival time 在多事件设定的推广，可非参数识别且自然处理终止性竞争风险。作者发展了 augmentation estimator（类似 augmented IPW / one-step），通过协变量调整保证效率不低于未调整估计量且通常更优；推导了 influence function 与大样本性质，提供非参数推断程序。实证通过模拟与 BEST 心衰试验多终点数据验证，附 R 包 MCC。对您有用：augmentation estimator 的效率增益机制与您关注的 semiparametric efficiency theory 直接相关，且多终点+竞争风险设定是流行病学因果推断的典型应用场景。
- **关键技术**: `augmentation estimator`, `mean cumulative function`, `restricted mean survival time extension`, `nonparametric inference`, `competing risks`, `influence function`
- **为什么对您有用**: 本文连接到 causal inference 的 estimation theory（多终点+竞争风险下的 AUMCF 估计）与 semiparametric efficiency（augmentation estimator 的效率增益）。用 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 semiparametric theory 可以分析其 augmentation estimator 的 influence function 是否达到该模型的 semiparametric efficiency bound，以及是否可用 HOIF 进一步提升效率。中期可做：需先在 moderately_familiar 的 semiparametric theory 上确认 AUMCF 模型的 efficiency bound 是否已被精确刻画，再判断 augmentation 是否真正 efficient 或仅是 variance-reducing。

### 5. [10.1093/biomtc/ujag056](https://doi.org/10.1093/biomtc/ujag056) — Personalized treatment design in the context of functional confounding
- **作者**: Zhixian Yang, Peijun Sang, Yixin Han, Bei Jiang, Linglong Kong, Xingcai Zhou
- **期刊/来源**: Biometrics
- **机构**: University of Alberta · University of Waterloo · Nanjing Audit University
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在观察性研究中研究含功能性混淆变量的个体化治疗规则（ITR）估计问题，目标 estimand 是最优决策函数的风险最小化。作者将 outcome-weighted learning（OWL）与再生核希尔伯特空间（RKHS）结合，用距离加权判别（DWD）分类器替代传统 SVM 以解决数据堆积问题。理论上建立了决策函数估计量的一致性及风险收敛界，但未涉及 semiparametric efficiency bound 或 sharper minimax rate。模拟与 ADNI 数据集分析显示该方法优于传统 OWL，并揭示了阿尔茨海默病进展的关键因素。对您而言，ITR 的因果推断设定与 RKHS 非参数估计框架直接对接 causal inference 与 nonparametric theory 两个 primary interest，但理论深度偏中等。
- **关键技术**: `outcome-weighted learning`, `RKHS estimation`, `distance-weighted discrimination`, `risk bound`, `functional confounding`, `individualized treatment rule`
- **为什么对您有用**: 本文连接 causal inference 中 ITR 估计与 nonparametric theory 中 RKHS 方法，ADNI 数据集属于流行病学应用。用您 very_familiar 的 nonparametric statistics 与 minimax bounds 视角可审视其风险界是否紧致，但本文未触及 efficiency bound 或 higher-order 修正。Follow-up 判断：**中期可做**——若想深入 functional data ITR 的效率理论，需先在 moderately_familiar 的 semiparametric theory 上推导该设定下的 efficient influence function。

### 6. [10.1093/biomtc/ujag100](https://doi.org/10.1093/biomtc/ujag100) · [arXiv](https://arxiv.org/abs/2601.12478) — Assessing interactive causes of an occurred outcome due to two binary exposures
- **作者**: Shanshan Luo, Wei Li, Xueli Wang, Shaojie Wei, Zhi Geng
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在两个二元暴露和一个二元结局的设定下，研究已发生结局的回顾性因果归因问题，estimand 为后验概率（posterior probability），刻画交互作用导致结局的概率。利用一个在主结局之后出现的次级结局（secondary outcome）作为辅助变量，建立了后验概率的可识别性（identifiability），无需依赖随机化假设。核心机制是将反事实框架下的联合归因概率转化为可观测的次级结局条件概率，从而绕过传统 RCT 无法识别回顾性交互因果的障碍。实证应用于吸烟与石棉暴露致肺癌的经典数据，发现协同交互作用的归因概率占主导。对您可能有用：本文的 identification 策略（次级结局作为 proxy）与 proximal CI 中 negative-control 思路有结构相似性，可对比其可识别性条件与 proximal g-formula 的差异。
- **关键技术**: `posterior probability of causation`, `interactive causes identification`, `secondary outcome as proxy`, `counterfactual framework`, `retrospective causal attribution`
- **为什么对您有用**: 本文直接连接因果推断中的 identification theory 子方向，特别是回顾性归因（causal attribution）而非前瞻性效应估计。其用次级结局做 proxy 的 identification 策略与 proximal CI 的 negative-control 设定结构相似，可用您 very_familiar 的 identification theory 工具审视其可识别性条件是否可放宽或推广到连续暴露。follow-up 判断：立即可做——用 identification theory 分析其假设的必要性，并尝试与 proximal CI 框架统一表述。

### 7. [10.1093/biomtc/ujag076](https://doi.org/10.1093/biomtc/ujag076) · [arXiv](https://arxiv.org/abs/2410.02941) — Efficient collaborative learning of the average treatment effect
- **作者**: Sijia Li, Rui Duan
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多站点协作因果推断设定下，目标是在数据共享受限时估计目标人群的 ATE。ECO-ATE 采用联邦式架构：仅使用目标站点的个体数据与源站点的汇总统计量，无需迭代通信即可构造 ATE 估计量。该方法允许结局、处理和协变量分布跨站点偏移，并在适当条件下达到 semiparametric efficiency bound。核心机制基于 one-step efficient influence function 修正与 cross-fitting，避免了对源站点完整数据的访问。模拟显示在分布偏移与过度参数化下仍有稳健的效率增益。对您有用：该文将 federated learning 与 semiparametric efficiency 结合，直接触及您 primary interest 中的效率理论（semiparametric efficiency bound）与因果推断估计理论。
- **关键技术**: `semiparametric efficiency bound`, `one-step estimation`, `efficient influence function`, `federated learning`, `data integration`, `cross-fitting`
- **为什么对您有用**: 直接连接您 primary interest 中的因果推断估计理论与 semiparametric efficiency bound；您 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 可直接用来审视其 influence function 构造是否可推广至 longitudinal / mediation 设定。立即可做：用您熟悉的 semiparametric efficiency 工具验证其 bound 在更一般 transportability 模型下的可达性，或扩展至 proximal CI 设定。

### 8. [10.1093/biomtc/ujag081](https://doi.org/10.1093/biomtc/ujag081) · [arXiv](https://arxiv.org/abs/2411.02123) — Uncertainty quantification and multi-stage variable selection for personalized treatment regimes
- **作者**: Jiefeng Bi, Matteo Borrotti, Bernardo Nipoti
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向动态治疗策略（DTR）框架下，目标是识别多阶段最优治疗序列并量化每个治疗方案对特定患者为最优的概率，同时从高维协变量中筛选关键预后因子。方法上，作者提出贝叶斯模型：通过反事实变量增广处理最优决策序列的不确定性量化；引入一类新的多阶段 spike-and-slab 先验实现跨阶段信息共享的变量选择，以应对高维协变量挑战。收敛性质未给出频率学派意义上的 asymptotic guarantee（如 CAN 或 efficiency bound），而是以贝叶斯后验收敛为推断基础。模拟研究展示了方法在有限样本下的表现，实证分析使用了严重急性动脉高血压的临床试验数据。对您而言，本文的 DTR 多阶段决策设定直接连接 longitudinal causal inference 子方向，但其贝叶斯推断路径与您常用的 semiparametric efficiency / debiased ML 路线不同。
- **关键技术**: `dynamic treatment regime`, `counterfactual augmentation`, `spike-and-slab prior`, `multi-stage variable selection`, `Bayesian posterior inference`, `optimal treatment probability`
- **为什么对您有用**: 本文的多阶段 DTR 设定直接对应您 primary interest 中 causal inference 的 longitudinal 子方向，且高维变量选择问题与您的高维统计兴趣有交集。但核心方法论是贝叶斯 spike-and-slab，而非您武器库中的 semiparametric efficiency bound / HOIF / debiased ML 路线——若要从频率学派效率理论视角审视 DTR 的多阶段变量选择与不确定性量化，您需要先在 moderately_familiar 的 semiparametric theory 上长肌肉，特别是多阶段 sequential decision 的 efficient influence function 构造。中期可做：用 HOIF 或 orthogonal score 重构该问题的频率学派推断，与贝叶斯后验做效率对比。

### 9. [10.1093/biomtc/ujag078](https://doi.org/10.1093/biomtc/ujag078) · [arXiv](https://arxiv.org/abs/2505.00822) — <i>Q</i> -Learning with clustered-SMART (cSMART) data: examining moderators in the construction of clustered adaptive interventions
- **作者**: Yao Song, Kelly Speth, Amy Kilbourne, Andrew Quanbeck, Daniel Almirall, Lu Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 clustered adaptive intervention (cAI) 框架下，目标 estimand 是因果效应调节参数——即候选 tailoring 变量是否在多阶段决策规则中调节干预效应，从而定义最优 cAI。核心挑战是 Q-learning 估计这些参数时存在 non-regularity：当最优决策规则不依赖 tailoring 变量（调节效应为零），参数落在边界，标准 bootstrap 失效。本文提出 clustered Q-learning 配合 M-out-of-N cluster bootstrap：从 N 个 cluster 中抽取 m 个（m/N→0, m→∞），在 non-regular 条件下仍可构造近名义覆盖率的置信区间。模拟验证了不同 non-regularity 强度、cluster 数量与组内相关系数下的 CI 覆盖表现，并应用于 ADEPT 数据集（诊所级 cAI 改进情绪障碍循证治疗）。对您而言，non-regularity 下的推断问题与 longitudinal causal inference 及 semiparametric efficiency 边界处的估计理论直接相关。
- **关键技术**: `Q-learning for dynamic treatment regimes`, `M-out-of-N cluster bootstrap`, `non-regularity in boundary inference`, `causal effect moderation`, `clustered sequential multiple assignment randomized trial`, `intra-cluster correlation adjustment`
- **为什么对您有用**: 本文连接到您 causal inference 的 longitudinal 子方向（多阶段 adaptive intervention 的决策规则估计），以及 mathematical statistics 中 non-regularity / boundary inference 的理论问题。用您 moderately_familiar 的 semiparametric theory 与 M-estimation theory 可以审视 M-out-of-N bootstrap 在此设定下的效率损失——是否可以用 HOIF 或 one-step correction 在 non-regular 点获得更优的局部逼近。中期可做：需先在 DTR (dynamic treatment regime) 的 identification 与估计理论上长肌肉，目前该子方向不在核心武器库中。

### 10. [10.1093/biomtc/ujag079](https://doi.org/10.1093/biomtc/ujag079) — Heterogeneous causal mediation analysis using Bayesian additive regression trees
- **作者**: Chen Liu, Xu Qin, Victor B Talisa, Jiebiao Wang
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · Department of Health
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在因果中介分析框架下，本文目标是估计异质性（条件）自然直接与间接效应，设定允许非线性关系及处理-中介交互。核心方法采用 BART（Bayesian Additive Regression Trees）对中介与结果模型进行非参数建模，通过层级后验采样构建中介效应的 credible intervals，并利用树结构识别亚组、SHAP 值提取调节变量。理论层面缺乏 semiparametric efficiency bound 或 influence function 的刻画，收敛性质依赖 BART 的后验收敛率而非 n^{-1/2}-CAN。模拟显示区间覆盖达标，实证应用于阿尔茨海默病流行病学数据（APOE→病理→认知）。对您而言，本文提供了异质性中介的流行病学应用范式，但理论深度偏弱。
- **关键技术**: `causal mediation analysis`, `heterogeneous natural direct/indirect effects`, `Bayesian additive regression trees (BART)`, `SHAP values`, `hierarchical posterior sampling`, `subgroup identification`
- **为什么对您有用**: (1) 直接连接因果推断的中介分析子方向与流行病学应用；(2) 本文 BART 黑箱缺乏效率界与 influence function，您可用 moderately_familiar 的 HOIF / semiparametric theory 为异质性中介效应构建具有 CAN 性质与效率界的 debiased estimator，填补其理论空白；(3) 中期可做：需先在 moderately_familiar 的 HOIF 与 semiparametric efficiency 上长肌肉，以将 BART 替换为严谨的 DML 框架。

### 11. [10.1093/biomtc/ujag083](https://doi.org/10.1093/biomtc/ujag083) · [arXiv](https://arxiv.org/abs/2604.10712) — Integrative learning of individualized treatment rules from multiple studies with partially overlapping treatments
- **作者**: Yuan Bian, Donglin Zeng, Hyun-Joon Yang, Leanne M Williams, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在多源 RCT 设定下，本文目标是估计治疗方案部分重叠（共享对照组但不同实验组）时的个性化治疗规则（ITR）。核心方法提出正则化加权误分类风险函数，自适应分配各研究对其他研究 ITR 的信息贡献权重，从而实现跨研究证据整合。理论上严格分析了所得估计器的 excess risk（超额风险）收敛性质。模拟与实证表明，该方法在 value/benefit function 估计上优于单一学习与一刀切方法，并在抑郁症临床数据（EMBARC/iSPOT-D）中验证了效用。对您有用：多源因果推断的 ITR 估计与 excess risk 理论，直接关联因果推断估计理论与流行病学临床应用。
- **关键技术**: `individualized treatment rule (ITR)`, `regularized weighted misclassification risk`, `multi-source data integration`, `excess risk bound`, `value function estimation`
- **为什么对您有用**: (1) 本文直接关联因果推断的 ITR 估计理论与流行病学临床数据应用；(2) 可用 very_familiar 的 estimation theory in causal inference 检视其 excess risk bound 是否紧，或用 moderately_familiar 的 M-estimation theory 分析其正则化加权目标函数的渐近性质；(3) **中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以推导更紧的 excess risk bound 或将其扩展到 semiparametric efficiency 框架下。

### 12. [10.1093/biomtc/ujag054](https://doi.org/10.1093/biomtc/ujag054) · [arXiv](https://arxiv.org/abs/2501.08231) — Bayesian shrinkage priors for penalized synthetic control estimators in the presence of spillovers
- **作者**: Esteban Fernández-Morales, Arman Oganisian, Youjin Lee
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在合成控制（SC）框架下，目标是估计地理单元政策干预的因果效应，但邻近控制单元可能受溢出效应污染导致估计偏倚。本文提出贝叶斯 SC 方法，引入基于效用函数的 shrinkage prior（horseshoe / spike-and-slab），将协变量相似性与空间距离结合为度量，数据驱动地选择控制单元并降低溢出风险高的邻近单元权重。方法不直接排除邻近单元，而是通过 shrinkage 在偏倚与方差间折中，对潜在受污染控制赋予较小重要性。模拟在不同溢出水平下评估，实证应用于费城 2017 料税对含糖饮料销售的影响。对您可能有用：该文将空间溢出纳入 SC 的 identification 与 estimation，为地理单元因果推断中处理 interference 提供贝叶斯 shrinkage 思路。
- **关键技术**: `synthetic control method`, `Bayesian shrinkage priors`, `horseshoe prior`, `spike-and-slab prior`, `spatial spillover / interference`, `utility-based penalization`
- **为什么对您有用**: 本文连接因果推断中合成控制与 interference / spillover 设定，属于地理单元因果效应估计的具体子方向。武器库中 identification theory in causal inference 可用于审视其 spillover 下的 identification 假设是否完备，但贝叶斯 shrinkage prior 与空间模型不在当前武器库核心。中期可做：需先在 moderately_familiar 的 M-estimation theory 或贝叶斯半参数模型上长肌肉，才能深入其 prior 设计与后验收敛性质的理论分析。

### 13. [10.1093/biomtc/ujag012](https://doi.org/10.1093/biomtc/ujag012) · [arXiv](https://arxiv.org/abs/2305.18793) — A First Course in Causal Inference
- **作者**: Alessandra Mattei
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `survey`
- **摘要**: 本文是 UC Berkeley 因果推断课程讲义的教材公告，面向本科生，仅要求基础概率、统计推断与线性/逻辑回归知识。内容覆盖潜在结果框架、随机化实验下 ATE 的基本 identification 与估计（IPW、regression adjustment），但未涉及 proximal CI、semiparametric efficiency bound、IV、mediation、longitudinal 等进阶主题。理论深度停留在经典 IPW 与简单 adjustment 层面，不触及 influence function、cross-fitting、debiasing 等现代工具。作为入门教材定位明确，但对您在 proximal CI / HOIF / semiparametric efficiency 方向的研究需求无直接推进。该书更适合教学参考而非研究拓展。
- **关键技术**: `potential outcomes framework`, `IPW estimation`, `regression adjustment`, `randomized experiment identification`, `ATE estimation`
- **为什么对您有用**: 本文属于 causal inference 入门教材，与您在 proximal CI、semiparametric efficiency bound、HOIF 等进阶子方向的研究深度严重不匹配。武器库中 semiparametric theory / HOIF / identification theory 已远超此书覆盖范围，无需借助此书进入任何新方向。**暂不可做**：非因缺工具，而是此书对您的研究层级无实质推进价值，不值得花时间读全文。

### 14. [10.1093/biomtc/ujag063](https://doi.org/10.1093/biomtc/ujag063) · [arXiv](https://arxiv.org/abs/2505.16047) — Bayesian adaptive randomization in the I-SPY2 sequential multiple assignment randomized trial
- **作者**: Peter Norwood, Christina Yau, Denise Wolf, Philip Beineke, Andrew Chapple, Anastasios Tsiatis et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `minor`
- **摘要**: 在 I-SPY2 乳腺癌新辅助治疗平台试验被重构为 SMART（序贯多重随机试验）的设定下，目标是设计一种跨最多三阶段治疗更新随机化概率的响应自适应随机化（RAR）方案，以最大化病理完全缓解（pCR）率。核心方法是基于贝叶斯后验概率的 RAR：在每个阶段根据累积数据计算各治疗方案属于最优动态治疗策略（optimal regime）的后验概率，并据此更新分配权重，使患者更可能被分配到高疗效策略对应的方案。模拟研究表明，该方案相比均匀随机化能让更多患者接受与最优策略一致的治疗、提高试验内整体 pCR 率，且试验后识别最优策略的速率与均匀随机化相当或更优。对您可能有用：SMART 与动态治疗策略属于 longitudinal causal inference 的核心问题，但本文聚焦试验设计而非因果估计理论。
- **关键技术**: `response-adaptive randomization`, `SMART design`, `Bayesian posterior probability updating`, `dynamic treatment regimes`, `optimal regime identification`
- **为什么对您有用**: SMART 设计与动态治疗策略（DTR）估计属于 longitudinal causal inference 范畴，与您 causal inference 中 longitudinal 子方向直接相关；但本文核心贡献在试验随机化方案设计，而非因果效应的 identification/estimation 理论或 semiparametric efficiency——您武器库中的 semiparametric theory / M-estimation 工具不直接攻这篇 paper 的口子。若想从 SMART 数据做因果估计理论（如 DTR 的 efficient influence function / debiased estimation），需另找文献；本文仅提供设计视角。**中期可做**：需先在 moderately_familiar 的 identification theory 上长肌肉（具体是 DTR / longitudinal setting 下的 identification 条件与 semiparametric efficiency bound），才能从 SMART 估计理论角度切入后续工作。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1093/biomtc/ujag103](https://doi.org/10.1093/biomtc/ujag103) — Transfer learning estimation of the accelerated failure time model based on high-dimensional data
- **作者**: Yichen Lou, Mingyue Du, Hui Zhao, Jianguo Sun
- **期刊/来源**: Biometrics
- **机构**: Nanyang Technological University · Jilin University · Zhongnan University of Economics and Law · Southern University of Science and Technology
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维设定下研究加速失效时间（AFT）模型的迁移学习估计，目标参数为回归系数，解决目标样本信息受限时传统高维方法失效或表现不佳的问题。提出两种迁移学习程序：一是数据驱动的源检测方法，区分正迁移与负迁移源数据集并仅利用正迁移源进行估计；二是集成加权方法，根据源与目标数据集的相关性自适应分配权重。理论部分在高维假设下证明了所提估计量的收敛性质与一致性。模拟与真实数据（重症住院成人临终关怀队列）分析表明，该方法能识别传统单源方法无法发现的预后因子。对您有用：结合了高维半参数估计与流行病学队列应用，为研究多源数据下的 semiparametric efficiency bound 与迁移学习 minimax rate 提供了具体案例。
- **关键技术**: `transfer learning`, `high-dimensional AFT model`, `negative transfer detection`, `adaptive ensemble weighting`, `semiparametric survival analysis`, `convergence rate`
- **为什么对您有用**: (1) 直接连接到高维统计（高维 AFT 估计）与流行病学（临终关怀真实数据）两个子方向；(2) 您 very_familiar 的高维渐近理论可直接审视其迁移估计的收敛率是否紧，moderately_familiar 的半参数理论可用来推导该设定下的 efficiency bound；(3) **中期可做**：需先在多源数据/迁移学习的 semiparametric efficiency 理论上长肌肉，目前武器库缺多源迁移下的最优效率界推导工具。

### 2. [10.1093/biomtc/ujag099](https://doi.org/10.1093/biomtc/ujag099) · [arXiv](https://arxiv.org/abs/2406.13111) — Nonparametric motion control in functional connectivity studies in children with autism spectrum disorder
- **作者**: Jialu Ran, Sarah Shultz, Benjamin B Risk, David Benkeser
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在 ASD 儿童功能性连接研究中，目标是估计诊断对功能性连接的平均差异效应，同时将头动标准化到通过质控的低动分布上——这是一个涉及选择偏差的标准化 estimand。提出 MoCo 非参数估计量，利用全部参与者数据，通过 ensemble ML 灵活建模动度及其他特征的效应；建立了该估计量的大样本效率性和多重稳健性（multiple robustness），即只需多个 nuisance 模型中的部分子集正确即可保证一致性。实证应用于 132 名 ASD 与 245 名非 ASD 儿童（仅 34/126 通过质控），MoCo 相比标准剔除法更高效利用数据并缓解选择偏差，相比无剔除法显著减少动度伪影。对您有用之处在于其多重稳健性框架与标准化 estimand 定义可直接迁移到流行病学队列研究中涉及选择/缺失的因果 estimand 问题。
- **关键技术**: `multiple robustness`, `standardization estimand`, `ensemble machine learning`, `semiparametric efficiency`, `selection bias correction`, `cross-fitting`
- **为什么对您有用**: 本文连接到 semiparametric theory 的 multiple robustness 估计量设计与 epidemiology 中选择偏差下的因果 estimand 定义。用 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory 可以分析其 estimand 的 identification 条件是否可进一步放松或推广到 longitudinal 设定。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体是 multiply robust estimator 的 influence function 推导与效率界计算），然后可探索将 MoCo 的标准化+多重稳健框架推广到 mediation 或 longitudinal 因果设定下的缺失/选择问题。

### 3. [10.1093/biomtc/ujag092](https://doi.org/10.1093/biomtc/ujag092) · [arXiv](https://arxiv.org/abs/2411.05591) — Decentralized EM algorithm for Gaussian mixtures under data heterogeneity and partial labeling
- **作者**: Xuetong Li, Shuyuan Wu, Bin Du, Hansheng Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在去中心化联邦学习（DFL）框架下研究高斯混合模型（GMM）的 EM 算法，目标是各局部站点数据异质分布时仍能获得与全样本等价的渐近有效估计量。直接将经典 EM 扩展至 DFL 在数据异质性下会产生严重偏差；为此提出 momentum network EM（MNEM），融合当前与历史迭代估计量以消除偏差。进一步利用部分标注数据开发 semi-MNEM，加速收敛并缓解混合成分分离度不足的问题。理论证明在适当正则条件下 MNEM 估计量达到全样本估计量的渐近效率，semi-MNEM 显著提升收敛速度。实证通过模拟与胸部 X 光数据集验证有限样本表现。对您可能有用：MNEM 的渐近效率证明涉及 M-estimation 与 EM 收敛率分析，与您 semiparametric efficiency 及 M-estimation 理论武器库直接相关。
- **关键技术**: `decentralized federated learning`, `EM algorithm for Gaussian mixtures`, `momentum network EM (MNEM)`, `semi-supervised MNEM`, `asymptotic efficiency under data heterogeneity`, `M-estimation theory`
- **为什么对您有用**: 本文连接到您 semiparametric efficiency 与 M-estimation 理论的子方向：MNEM 在异质数据下达到全样本渐近效率的证明依赖 M-estimation 收敛性分析，您 very_familiar 的高维渐近与 moderately_familiar 的 M-estimation 理论可直接切入其效率界论证。用 minimax bound 或 HOIF 视角可检验其声称的效率是否紧、异质性条件是否可弱化。中期可做：需先在 moderately_familiar 的 M-estimation 理论上长肌肉（特别是 EM 局部收敛率与全局收敛的统一分析），再审视其效率证明的严密性。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujag074](https://doi.org/10.1093/biomtc/ujag074) — Efficient interaction analysis in randomized controlled trials
- **作者**: Likun Zhang, Wei Ma
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China
- **分类**: vol 82 · issue 2
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在随机对照试验(RCT)中，连续协变量的治疗-协变量交互作用定义常依赖强参数假设；本文在协变量适应性随机化（包括分层与最小化方法）下提出无模型交互分析框架，定义了明确的交互效应目标参数。指出传统方法因忽略处理分配诱导的依赖结构，方差估计会保守或反保守；作者修正了方差估计量，并推导出该交互效应的半参数有效界。进一步提出基于有效影响函数的半参数有效估计方法，利用非参数与机器学习技术调整基线协变量。理论证明该估计量达到半参数有效界，实证验证了其适用性。对您有用：直接连接到efficiency theory与causal inference的交叉点，展示了复杂随机化设计下有效界推导与估计量构造的完整流程。
- **关键技术**: `semiparametric efficiency bound`, `covariate-adaptive randomization`, `treatment-covariate interaction`, `model-free interaction parameter`, `efficient influence function`, `machine learning covariate adjustment`
- **为什么对您有用**: (1) 连接到 causal inference 中 RCT 的 treatment heterogeneity/interaction 估计，以及 efficiency theory 中半参数有效界推导；(2) 您的 "estimation theory in causal inference" (very_familiar) 和 "semiparametric theory" (moderately_familiar) 可以直接用来审视其有效界推导是否完备，或探讨该交互参数的 HOIF 扩展；(3) **立即可做** — 用 very_familiar 的因果推断估计理论即可复现或延伸其有效界计算到其他随机化方案。

### 2. [10.1093/biomtc/ujag062](https://doi.org/10.1093/biomtc/ujag062) · [arXiv](https://arxiv.org/abs/2501.06360) — Borrowing information from an unidentifiable model: Guaranteed efficiency gain with a dichotomized outcome in the external data
- **作者**: Lu Wang, Yanyuan Ma, Jiwei Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在数据整合设定下，主数据集包含连续结局，外部数据仅提供其二值化版本，目标是利用不可识别的外部模型提升主数据回归参数的估计效率。提出两种新估计量：第一种在误差分布误设下仍保持渐近一致；第二种保证比仅用主数据的加权最小二乘（WLS）估计有严格的效率提升。核心机制在于外部二值化数据提供了连续分布截断点的额外信息，即使外部模型参数不可识别，仍能收紧 semiparametric efficiency bound。理论严格证明了效率增益的保证，并在 NHANES 数据上验证实用性。对您有用：直接触及 semiparametric efficiency theory 中“不可识别辅助信息如何收紧效率下界”的问题，与您关注的 efficiency bounds 和 causal inference 中的 data integration 密切相关。
- **关键技术**: `semiparametric efficiency bound`, `data integration`, `misspecification-robust estimation`, `unidentifiable external model`, `influence function`, `weighted least squares`
- **为什么对您有用**: (1) 直接连接到 efficiency theory (semiparametric efficiency bounds) 和 causal inference 中的 data integration / transportability 设定。(2) 可以用 moderately_familiar 的 "semiparametric theory" 和 "M-estimation theory" 来审视其 influence function 构造，看其效率收紧机制是否可推广到 causal inference 中的 surrogate outcome 或 negative control 设定。(3) **中期可做**：需先在 moderately_familiar 的 "semiparametric theory" 上长肌肉，深入推导其 influence function 与不可识别辅助信息的交互，再探索在 proximal CI 中引入类似机制的可行性。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biomtc/ujag093](https://doi.org/10.1093/biomtc/ujag093) — A Bayesian decision-theoretic approach to multiple testing in basket trials
- **作者**: Amartya Kumar Maulik, Tianjian Zhou
- **期刊/来源**: Biometrics
- **机构**: Colorado State University
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在 basket trial 的多重检验设定下，目标是跨子人群同时检验治疗效应，同时控制 frequentist error rate。本文提出一族 Bayesian decision-theoretic loss function，根据真实 null/alternative 的数量自适应惩罚 false positive/negative，使得当其他 basket 显示疗效时，当前 basket 更易被判为 promising。各 basket 的效应估计保持独立，避免了 hierarchical model 的计算负担，并可推广至不同 endpoint 类型。通过 tuning parameter 控制 borrowing 程度与决策保守性，可校准至目标 frequentist error rate 水平。最优 Bayes decision rule 通过最小化 posterior expected loss 得到，计算高效。模拟显示与常用方法竞争力相当，并在 vemurafenib basket trial 上实证。对您可能有用：该框架将 Bayesian decision theory 与 frequentist error rate 校准结合，为多重假设检验提供了一个可调 borrowing 强度的替代路径。
- **关键技术**: `Bayesian decision theory`, `multiple testing`, `adaptive loss function`, `posterior expected loss minimization`, `frequentist error rate calibration`, `basket trial borrowing`
- **为什么对您有用**: 直接连接到 primary interest 中的 hypothesis testing 子方向，特别是多重检验的 decision-theoretic 视角。用您 very_familiar 的 minimax bounds 工具可以分析该 adaptive loss 下的 risk 性质，或用 moderately_familiar 的 M-estimation theory 探讨 tuning parameter 的最优选择理论。立即可做：用 minimax 框架验证其声称的 frequentist error rate 校准是否紧。

### 2. [10.1093/biomtc/ujag059](https://doi.org/10.1093/biomtc/ujag059) · [arXiv](https://arxiv.org/abs/2412.02945) — Detection of multiple influential observations on model selection
- **作者**: Dongliang Zhang, Masoud Asgharian, Martin A Lindquist
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 在高维设定（p>n）下，研究对随机子模型选择产生不当影响的异常观测的诊断问题，目标 estimand 是影响度量（influence measure）的分布及其阈值。作者基于 exchangeability 概念推导了该诊断度量的精确渐近分布，并据此提出参数与非参数两种分布逼近方法及异常识别阈值。框架进一步推广至 logistic 回归模型，通过模拟比较多种检测方法的表现。实证分析基于任务式 fMRI 热痛数据，在线性与 logistic 模型下识别出两个此前未被检测到的影响观测。对您可能有用：本文将 exchangeability 与高维模型选择的影响诊断结合，为高维假设检验与 M-estimation 理论提供了一个新的分布刻画视角。
- **关键技术**: `exchangeability-based asymptotic distribution`, `high-dimensional influence diagnostics`, `model selection perturbation`, `parametric and nonparametric threshold derivation`, `logistic regression extension`
- **为什么对您有用**: 本文连接到 hypothesis testing 与高维统计的交叉：在高维 p>n 设定下对模型选择影响度量的渐近分布做精确刻画，属于高维 M-estimation 的扰动分析。您武器库中 minimax bounds 与 M-estimation theory（moderately_familiar）可直接切入其 exchangeability 论证与阈值推导的紧性分析。中期可做：需先在 M-estimation theory 的扰动分析（如 leave-one-out stability）上长肌肉，再审视其渐近分布是否可进一步 sharpen。

### 3. [10.1093/biomtc/ujag061](https://doi.org/10.1093/biomtc/ujag061) — A novel exact confidence interval for the difference of proportions in paired data using a restricted most probable statistic
- **作者**: Xingyun Cao, Weizhen Wang, Tianfa Xie
- **期刊/来源**: Biometrics
- **机构**: Chongqing Technology and Business University · Beijing University of Technology · Beijing Information Science & Technology University · University of Science and Technology Beijing · Wright State University
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在配对二元数据（2×2 匹配表）设定下，目标是构造两个比例之差 p1−p2 的精确置信区间，避免渐近正态近似在小样本下的不可靠性。作者提出基于 restricted most probable (RMP) 统计量的精确区间，并进一步用 h-function 方法优化得到最优精确区间，同时保证覆盖概率不低于名义水平且区间长度尽量短。比较对象包括 score method、Tang 的两种方法、Wang 方法、adjusted Wald 及带连续性修正的 score method。以 infimum coverage probability 和 total interval length 为评价指标，所提区间在所有比较方法中表现一致最优。配对比例之差的精确推断是经典假设检验问题，本文的 RMP+h-function 组合给出了该具体参数的最优精确区间方案。
- **关键技术**: `restricted most probable statistic`, `h-function optimization`, `exact confidence interval`, `infimum coverage probability`, `paired binary data inference`, `discrete parameter exact inference`
- **为什么对您有用**: 本文落在您 primary interest 的 hypothesis testing 子方向，但具体问题是配对比例之差的离散精确推断，与您常用的 semiparametric efficiency / U-statistic / high-dimensional 工具链距离较远。RMP 统计量与 h-function 优化属于离散参数精确检验的专门技术，不在您当前 technical_arsenal 中。若要沿此方向做 follow-up（如将 RMP 思想推广到更复杂参数或高维离散设定），需先在 moderately_familiar 的 M-estimation theory 之外额外学习离散精确推断的 ordering 与 optimization 框架——判定为**中期可做**，需先在离散参数精确检验方法上长肌肉。

## 流行病学  *(epidemiology, 15 篇)*

### 1. [10.1093/biomtc/ujag101](https://doi.org/10.1093/biomtc/ujag101) · [arXiv](https://arxiv.org/abs/2504.03480) — Multivariate causal effects: a Bayesian causal regression factor model
- **作者**: Dafne Zorzetto, Jenna Landy, Corwin Zigler, Giovanni Parmigiani, Roberta De Vito
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在多变量潜在结果框架下，本文研究野火烟雾对PM2.5中27种化学成分的多变量因果效应，旨在解决因果推断中缺失数据与多变量复杂相关性挑战。提出贝叶斯因果回归因子模型，核心创新是对处理特异性的因子得分引入probit stick-breaking过程先验，实现潜因子结构的灵活数据驱动刻画。通过聚焦因子得分，方法绕过了多变量因果推断中缺失数据难题，并在贝叶斯框架下完成效应估计。模拟表明模型在多变量因果效应估计与潜结构刻画上具准确性。实证分析美国空气质量数据，揭示野火烟雾对PM2.5化学成分的因果影响及成分间依赖。对您而言，本文提供了流行病学多变量因果效应的应用案例与数据集，但其贝叶斯非参路径与您偏好的半参效率/去偏ML框架差异显著。
- **关键技术**: `multivariate potential outcomes`, `Bayesian factor model`, `probit stick-breaking process`, `causal regression`, `missing data imputation via factor scores`
- **为什么对您有用**: (1) 连接到流行病学（环境健康因果推断）的次级兴趣，提供了多变量潜在结果框架下的真实数据集（PM2.5化学成分）与应用范式。(2) 本文的贝叶斯非参因子模型路径与您的 `technical_arsenal`（半参效率/去偏ML）不匹配，无法用现有武器分析其理论性质；若要攻破多变量因果效应的效率理论，需用 `moderately_familiar` 的半参理论推导多变量影响函数。(3) **中期可做**：需先在多变量半参效率理论（多变量影响函数与效率界）上长肌肉，本文仅作为应用与数据集参考。

### 2. [10.1093/biomtc/ujag088](https://doi.org/10.1093/biomtc/ujag088) — Two-phase designs for biomarker studies when disease processes are under intermittent observation
- **作者**: Kecheng Li, Richard J Cook
- **期刊/来源**: Biometrics
- **机构**: University of Waterloo
- **分类**: vol 82 · issue 2
- 相关性 6/10
- **摘要**: 在多状态模型框架下研究慢性病进程与生物标志物的关联，目标参数为 biomarker 对状态转移强度的回归系数，关键假设是间歇观察与两阶段抽样设计下的条件独立性。本文提出基于伪残差的依赖性抽样策略（pseudo-score residual-dependent sampling），通过条件似然与估计函数进行推断，显著提升 biomarker 效应的 MLE 估计效率。理论部分比较了不同子抽样策略的 semiparametric efficiency，实证与 Psoriatic Arthritis 队列的 HLA-B27 数据验证了方法优势。对您可能有用：若关注流行病学队列中 intermittent observation 下的因果/关联推断，此文的 pseudo-score sampling 与效率比较提供了直接参考。
- **关键技术**: `multistate models`, `two-phase sampling design`, `pseudo-score residual-dependent sampling`, `conditional likelihood`, `estimating functions`, `semiparametric efficiency comparison`
- **为什么对您有用**: 本文连接到流行病学队列研究的因果/关联推断子方向，特别是 intermittent observation 下的 biomarker 效应估计。武器库中 semiparametric theory 与 M-estimation theory（moderately_familiar）可用来审视其 pseudo-score sampling 的效率界是否达到 semiparametric efficiency bound，以及估计函数的 robustness。中期可做：需先在 semiparametric efficiency bound 计算上长肌肉，才能严格验证其声称的效率优势是否紧。

### 3. [10.1093/biomtc/ujag058](https://doi.org/10.1093/biomtc/ujag058) — Two-phase designs for cost-effective evaluation of cancer screening tests
- **作者**: Fangya Mao, Richard J Cook, Thomas Lorey, Nicolas Wentzensen, Li C Cheung
- **期刊/来源**: Biometrics
- **机构**: National Cancer Institute · University of Waterloo · Kaiser Permanente
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在癌症筛查试验评估的 two-phase design 设定下，目标是估计阳性预测值（PPV）与阴性预测值（NPV）及风险分层效用，关键假设为 subsampling 选择机制可由 Phase-1 已知变量刻画且测量缺失为 MAR。本文提出新型 two-phase design，将传统用于 marker-outcome 关联估计的设计扩展至预测性指标估计，同时纳入初始筛查时的现患病例（prevalent cases）与随访中新发病例（incident cases），解决筛查队列中两类病例共存的结构。核心估计基于 inverse probability weighting 与效率优化 subsampling 策略（类 Neyman allocation），通过在 test-positive/test-negative 子群中差异化采样昂贵标志物来提升 PPV/NPV 估计效率。模拟显示所提设计在 PPV/NPV 估计方差上相比简单随机 subsampling 与传统关联导向 subsampling 有显著效率增益。实证使用 Kaiser Permanente Northern California 宫颈癌细胞库数据，评估 p16/ki-67 双染色试验对 HPV 阳性女性的管理价值。对您可能有用：two-phase design 下的效率优化直接关联 semiparametric efficiency bound 与 influence function，且流行病学筛查队列数据可作为因果/预测评估方法的真实数据测试平台。
- **关键技术**: `two-phase design`, `inverse probability weighting`, `predictive value estimation (PPV/NPV)`, `optimal subsampling allocation`, `risk stratification`, `prevalent-incident cohort`
- **为什么对您有用**: (1) 连接到流行病学（secondary interest）的真实队列筛查数据与评估场景，同时触及 efficiency theory（primary interest）中 two-phase missing data 下的 semiparametric efficiency 问题；(2) 用 moderately_familiar 中的 semiparametric theory 可推导 PPV/NPV 在 two-phase sampling 下的 efficient influence function，进而验证所提 subsampling 策略的效率是否紧贴该 bound——这是本文未显式展开的理论口子；(3) 中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，完成 two-phase design 下 predictive values 的 efficient influence function 推导与 efficiency bound 计算，再对比所提设计的实际效率。

### 4. [10.1093/biomtc/ujag072](https://doi.org/10.1093/biomtc/ujag072) · [arXiv](https://arxiv.org/abs/2504.17195) — Borrowing strength across exposures and outcomes via index models for multi-pollutant mixtures
- **作者**: Glen McGee, Joseph Antonelli
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在多污染物混合暴露的环境流行病学设定下，目标是估计多个高相关暴露对多个健康结局的非线性联合效应，核心挑战是暴露间强相关且效应弱导致低功效。提出多变量 index model 策略，通过共享 mixture component weights 与暴露-响应曲线的相似结构跨结局和跨暴露借力提升功效。在 distributed lag model 特例中，联合鼓励 lag profile 与暴露-响应曲线的 co-clustering，以更高效识别 critical windows of vulnerability。进一步扩展到 index 结构（index 数量与组成）未知的设定，引入 variable importance measures 量化各组分对混合效应的贡献。使用 NMMAPS 时间序列数据（3 个死亡结局、2 个累积空气污染指标、最大 lag 14 天）进行实证演示。对您可能有用：多 index model 属半参数框架但本文侧重 Bayesian 建模而非效率理论；NMMAPS 是流行病学经典数据源，可作因果/半参数方法的 benchmark。
- **关键技术**: `multiple index models`, `Bayesian kernel machine regression`, `distributed lag models`, `co-clustering of lag profiles`, `variable importance measures`, `exposure-response curve estimation`
- **为什么对您有用**: 连接到流行病学子方向（环境流行病学数据集 NMMAPS）与半参数理论子方向（多 index model 的估计问题）；当前论文未推导 semiparametric efficiency bound 或 influence function，用 moderately_familiar 中的 semiparametric theory 可分析该多 index model 的效率界与 one-step / debiased 估计，这是本文未触及的理论口子；中期可做：需先在 semiparametric theory（多 index model 的 efficiency bound 推导）上长肌肉，才能从理论角度推进此方向。

### 5. [10.1093/biomtc/ujag087](https://doi.org/10.1093/biomtc/ujag087) · [arXiv](https://arxiv.org/abs/2604.03970) — Learning association from multiple intermediate events for dynamic prediction of survival: an application to cardiovascular disease prognosis
- **作者**: Tonghui Yu, Liming Xiang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在心血管疾病多病共发、死亡导致 informative censoring 的生存分析设定下，目标是动态预测总体生存概率。作者提出 copula-based 框架，通过 pseudo-likelihood 估计多个中间事件发病时间之间的依赖结构；采用非参数边际分布，避免传统 copula 模型对边际的参数假设，并用 concordance estimating equation 估计中间事件与死亡的关联。在此基础上发展了 renewable risk assessment 方法，利用已观测疾病发病时间和最大随访时间进行动态预测。理论部分给出了估计量的渐近性质；模拟与心脏病队列数据实证表明，纳入多病关联与协同效应对生存预测有显著提升。对您可能有用：该文在流行病学队列中处理 informative censoring 与多中间事件的动态预测，与您在因果推断 longitudinal/mediation 设定下的 identification 与 semiparametric estimation 有结构相似性。
- **关键技术**: `copula pseudo-likelihood`, `nonparametric marginals`, `concordance estimating equation`, `informative censoring`, `dynamic survival prediction`, `renewable risk assessment`
- **为什么对您有用**: 本文属于流行病学应用，核心是多中间事件与死亡之间的关联建模及 informative censoring 下的动态预测，与您在因果推断 longitudinal/mediation 设定下处理中间事件与竞争风险的 identification/estimation 有直接结构对应。您武器库中的 semiparametric theory 与 M-estimation theory 可直接攻其 concordance estimating equation 的渐近性质与效率界分析。Follow-up 判断：中期可做——若想将此 copula-semiparametric 框架与 proximal/IV 因果识别结合，需先在 moderately_familiar 的 identification theory 上长肌肉，但纯方法学延伸（如 semiparametric efficiency bound 计算）立即可做。

### 6. [10.1093/biomtc/ujag075](https://doi.org/10.1093/biomtc/ujag075) · [arXiv](https://arxiv.org/abs/2508.16256) — A regularized multi-state model for covariate selection with interval-censored survival data
- **作者**: Ariane Bercu, Agathe Guilloux, Cécile Proust-Lima, Hélène Jacqmin-Gadda
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在流行病学队列的区间删失与半竞争风险（死亡截断诊断）设定下，本文研究 illness-death 多状态模型的高维协变量选择问题。提出基于 elastic-net 惩罚的 proximal gradient hybrid 算法最大化正则化似然，对三个转移强度分别估计回归参数并设定转移特异的惩罚参数（外层网格搜索）。算法在 R 包 HIDeM 中实现，模拟表明其在预测疾病概率与选择转移特异风险因子上优于忽略区间删失的模型，后者倾向于选择与死亡相关的无关协变量。实证应用于 Three-City 队列，从脑影像与临床标记中识别痴呆发病预测因子。对您有用：本文提供了半竞争风险区间删失数据的高维变量选择方法与真实数据集，连接了您在因果推断（多状态模型）与流行病学应用的兴趣。
- **关键技术**: `illness-death model`, `interval-censored survival`, `semi-competing risk`, `proximal gradient algorithm`, `elastic-net penalty`, `transition-specific variable selection`
- **为什么对您有用**: (1) 直接连接流行病学应用因果工作（半竞争风险/区间删失多状态模型）及高维变量选择；(2) 您武器库中的 estimation theory in causal inference 与 software development 可直接审视其 proximal gradient 算法实现与似然推断的稳定性；(3) 立即可做：用 very_familiar 的 software development 与 high-dimensional asymptotics 视角评估其 elastic-net 在多状态模型下的理论性质（如 oracle property），或直接将 Three-City 数据集作为区间删失因果推断的实验平台。

### 7. [10.1093/biomtc/ujag071](https://doi.org/10.1093/biomtc/ujag071) · [arXiv](https://arxiv.org/abs/2411.10858) — Scalable Gaussian process regression via median posterior inference for estimating the health effects of an environmental mixture
- **作者**: Aaron Sonabend-W, Jiangshan Zhang, Edgar Castro, Joel Schwartz, Brent A Coull, Junwei Lu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 4/10 · novelty: `application`
- **摘要**: 在环境混合物（environmental mixture）健康效应估计问题中，目标是在高维暴露变量存在复杂相关与非线性暴露-响应关系的设定下估计暴露对结局的效应，同时调整混杂。作者提出分治策略：将数据分块后在各子集上并行计算 Gaussian process 回归的后验分布，再通过 generalized median 组合子后验，避免全样本 MCMC 的计算瓶颈。该方法声称可推广至任何后验计算代价过高的 Bayesian 模型，但本文未给出 median posterior 收敛速率的严格 minimax 或效率界。实证应用于 Massachusetts 2001–2012 年 65 万出生记录与空气污染混合物，发现交通污染标记物（元素碳、有机碳、PM₂.₅）与出生体重负相关、臭氧与植被绿度正相关。对您而言，本文提供了一个大规模流行病学数据集作为潜在的应用因果推断素材，但其因果方法论仅停留在混杂调整，未涉及 IV / proximal CI / sensitivity 等您关心的工具。
- **关键技术**: `divide-and-conquer posterior`, `generalized median combination`, `Gaussian process regression`, `Bayesian feature selection`, `environmental mixture exposure-response`
- **为什么对您有用**: （1）连接到流行病学数据集方向——65 万出生记录+空气污染多暴露变量是真实大规模队列，可作为 IV 或 proximal CI 方法的应用测试床；（2）武器库中 software development 可审视其分治后验组合的工程实现，但 minimax bounds 工具难以直接攻入——本文未给出 median posterior 的收敛速率理论；（3）中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，才能将 GP exposure-response 模型嵌入 semiparametric efficiency 框架并给出 sharper rate，当前论文本身更值得作为数据集来源而非方法学参考。

### 8. [10.1093/biomtc/ujag080](https://doi.org/10.1093/biomtc/ujag080) · [arXiv](https://arxiv.org/abs/2503.24146) — Joint modeling of multiple longitudinal biomarkers and survival outcomes via threshold regression: variability as a predictor
- **作者**: Mingyan Yu, Zhenke Wu, Michelle M Hood, Carrie Karvonen-Gutierrez, Siobán D Harlow, Michael R Elliott
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文在多纵向生物标志物与生存结局的联合建模框架下，将纵向子模型的随机效应方差作为生存预测变量纳入 threshold regression，从而利用变异度信息而非仅依赖均值轨迹。纵向部分处理了多个可能受检测限 censoring 的生物标志物；生存部分采用 threshold regression（允许非比例风险），以随机效应均值与方差共同作为协变量。方法通过 Bayesian 框架实现联合估计，模拟展示了 operating characteristics，并应用于 SWAN 数据，研究 FSH 与 AMH 的均值及变异度对绝经年龄的预测作用。核心方法贡献在于将"变异度作为系统失调信号"形式化纳入生存模型，而非仅视其为 nuisance。对您而言，本文提供了流行病学纵向队列的真实数据集（SWAN）及一个将纵向变异度与生存结局关联的建模思路，但方法论层面为 Bayesian 联合模型，与您关注的 semiparametric efficiency / causal identification 路线不同。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `Bayesian joint model`, `threshold regression`, `random-effect variance as predictor`, `limit-of-detection censoring`, `nonproportional hazards`, `longitudinal biomarker variability`
- **为什么对您有用**: 本文连接到您 secondary interest 中的流行病学纵向队列数据集（SWAN），提供了一个将纵向变异度与生存结局关联的建模思路；但方法论为 Bayesian 联合模型，不涉及 causal identification 或 semiparametric efficiency，因此与您 primary interest 的纵向因果推断 / 效率理论无直接技术对接。用您 very_familiar 的高维渐近 / minimax 工具无法直接攻此 paper 的 Bayesian 推断口子；若想深入此类联合模型的理论性质，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，将 threshold regression 置于 semiparametric efficiency bound 框架下分析。Follow-up 判断：中期可做（需先在 semiparametric joint model 的效率理论方向积累）。

### 9. [10.1093/biomtc/ujag090](https://doi.org/10.1093/biomtc/ujag090) · [arXiv](https://arxiv.org/abs/2406.05262) — A three-groups non-local model for combining heterogeneous data sources to identify genes associated with Parkinson’s disease
- **作者**: Troy P Wixson, Benjamin A Shaby, Daisy L Philtron, Leandro A Lima, Stacia K Wyman, Julia A Kaye et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种三层混合（three-groups mixture）层次贝叶斯模型，整合异构基因组数据源（GWAS、RNA-seq）以识别帕金森病相关基因。每个基因被建模为属于 null（无关联）、deleterious（有害）或 beneficial（有益）三组之一，组分配先验采用 Dirichlet 分布，后验组概率自动控制大规模基因检验的 multiplicity。通过条件于组标签构建各模态实验结果的分布，任意数量数据模态可在单一概率框架下融合共享信息，实现 parsimonious inference。模拟表明该方法在 GWAS 与 RNA-seq 场景下与常用工具表现相当或更优，假阳性率低且信号检测功率更高。应用于公开 PD 数据集，发现若干潜在治疗靶点的新基因。对您而言，本文属流行病学/遗传学应用范畴，方法核心是标准 Dirichlet-mixture 层次模型，与您主要兴趣（因果推断、半参数效率、高维 RMT）关联较弱。
- **关键技术**: `three-groups mixture model`, `Dirichlet prior for multiplicity control`, `hierarchical Bayesian model`, `multi-modal data integration`, `posterior group probability`
- **为什么对您有用**: 本文属流行病学（遗传学方向）二次兴趣范畴，但方法核心是贝叶斯层次混合模型而非因果推断或半参数理论，与您 primary interests 连接较弱。您的 technical_arsenal 中无贝叶斯层次模型推断工具，无法直接攻入此方向；若要跟进需先在 moderately_familiar 的 M-estimation 理论之外补贝叶斯计算（MCMC / variational inference），属中期可做但收益不高。作为 gateway reading，本文对统计学家入门多模态基因组数据整合有一定参考价值，但方法学 novelty 有限（标准 Dirichlet-mixture 框架），不值得花时间读全文。

### 10. [10.1093/biomtc/ujag073](https://doi.org/10.1093/biomtc/ujag073) — Regression methods for cost-effectiveness analysis with different censoring times or terminating events for survival time and costs
- **作者**: Dingning Liu, Shuai Chen
- **期刊/来源**: Biometrics
- **机构**: University of California, Davis
- **分类**: vol 82 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在成本-效果分析（CEA）中，当成本与效果面临不同终止事件或不同删失时间时，目标是估计增量成本-效果比（ICER）与增量净效益（INB），现有方法均无法纳入协变量调整。本文提出回归框架下的估计方法，通过协变量调整处理诱导信息性删失并改善效率，同时支持亚组识别以应对不完美随机化。模拟研究显示有限样本表现良好，方法应用于MADIT-CRT与MADIT-II两个心血管临床试验数据集。对您而言，本文提供了流行病学心血管试验的真实数据集与applied causal场景，但方法学层面未涉及semiparametric efficiency bound或influence function推导，理论深度与您核心兴趣距离较远。
- **关键技术**: `incremental cost-effectiveness ratio`, `incremental net benefit`, `induced informative censoring`, `covariate adjustment under imperfect randomization`, `regression-based survival estimation`, `subgroup identification`
- **为什么对您有用**: （1）连接到流行病学secondary interest中的心血管试验数据集与applied causal work——MADIT-CRT/MADIT-II是真实CEA数据源；（2）武器库中'estimation theory in causal inference'可用来审视其协变量调整是否达到效率最优，但本文未推导该设定下的semiparametric efficiency bound，这正是您能切入的理论口子；（3）中期可做：若想在此CEA删失设定下推导efficiency bound并构造efficient one-step/TMLE estimator，需先在moderately_familiar的semiparametric theory上长肌肉（具体是influence function在informative censoring下的推导）。

### 11. [10.1093/biomtc/ujag077](https://doi.org/10.1093/biomtc/ujag077) — A mixed effect similarity matrix regression model (SMRmix) for integrating multiple microbiome datasets at the community level
- **作者**: Mengyu He, Ni Zhao
- **期刊/来源**: Biometrics
- **机构**: Emory University · Johns Hopkins University · Johns Hopkins Medicine
- **分类**: vol 82 · issue 2
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在多微生物组研究整合场景下，目标是在研究间异质性（人群与实验流程差异）条件下识别与结局变量关联的群落水平微生物整体偏移，关键假设为各研究共享固定效应但具有随机效应异质性。提出混合效应相似矩阵回归 SMRmix，将单研究微生物组核关联检验 MiRKAT 扩展至多研究 meta-analysis：以生态距离相似矩阵为响应，固定效应捕捉结局-群落关联，随机效应刻画研究间异质性。模拟中 SMRmix 的 Type I error 控制良好且 power 优于单独分析及简单合并方法。实证应用于 17 个 HIV 肠道菌群失调数据集和 11 个结直肠癌数据集，均得到一致的群落水平偏移结论。对关注非参数核检验与流行病学数据集的研究者，SMRmix 提供了 kernel-based association test 在 meta-analysis 场景的扩展思路，但方法 novelty 主要在领域特定设计而非一般非参数理论推进。
- **关键技术**: `similarity matrix regression`, `mixed effect model`, `microbiome kernel association test (MiRKAT)`, `meta-analysis of microbiome studies`, `ecological distance kernel`
- **为什么对您有用**: 连接到流行病学数据集方向——提供了 HIV 肠道菌群与结直肠癌的多研究整合数据集及分析流程，但方法核心是关联检验而非因果推断，与研究者关注的 epi causal inference 子方向重叠有限。武器库中 nonparametric statistics 可用于分析其 kernel regression 的理论性质（如相似矩阵回归的渐近分布与 minimax rate），但该 paper 的理论贡献仅限于模拟验证，未建立正式渐近理论。中期可做——若想将 SMRmix 框架推广至因果推断设定（如 proximal CI 的 negative control 矩阵回归），需先在 semiparametric theory 上长肌肉以建立混合效应相似矩阵回归的效率界与 influence function。

### 12. [10.1093/biomtc/ujag086](https://doi.org/10.1093/biomtc/ujag086) — Correcting random effect distributions to account for survivorship bias in individual heterogeneity Cormack–Jolly–Seber models
- **作者**: Blanca Sarzo, Ruth King, Rachel McCrea
- **期刊/来源**: Biometrics
- **机构**: Fundación para el Fomento de la Investigación Sanitaria y Biomédica de la Comunitat Valenciana · Maxwell Institute for Mathematical Sciences · Lancaster University
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究捕获-再捕获数据中因初次捕获前存活筛选导致的幸存者偏差问题，聚焦于带连续随机效应的 Cormack–Jolly–Seber (CJS) 模型，假设个体存活概率来自某共同分布。经典 CJS 模型条件化于首次观测时刻，忽略了进入样本前的存活筛选，导致随机效应分布被系统性低估。作者提出一种修正建模方法，在生态学合理的框架下显式纳入幸存者偏差，通过模拟与 guillemot 实际数据展示即使轻度选择偏差也会使个体异质性方差被严重低估。对您可能有用：该文是流行病学/生态学队列研究中选择偏差的经典实例，与因果推断中条件化于存活者的 selection bias 问题结构同构。
- **关键技术**: `Cormack–Jolly–Seber model`, `random effect distribution correction`, `survivorship bias`, `capture-recapture`, `conditional likelihood`
- **为什么对您有用**: 本文连接到流行病学队列研究中的幸存者偏差问题，与因果推断中条件化于存活者（如 mediation/longitudinal 中的 collider bias）结构同构。用您 very_familiar 的 identification theory in causal inference 可以分析该修正模型的 identification 条件是否完备，或用 moderately_familiar 的 semiparametric theory 探究修正后随机效应分布估计的效率界。属于 gateway reading：入门易懂，数据/模型清晰，值得花时间读全文以理解选择偏差在非标准观测框架下的修正思路。

### 13. [10.1093/biomtc/ujag097](https://doi.org/10.1093/biomtc/ujag097) — TITE-safety: a robust time-to-event safety monitoring approach for clinical trials
- **作者**: Michael J Martens, Qinghua Lian, Brent R Logan
- **期刊/来源**: Biometrics
- **机构**: Medical College of Wisconsin · Versiti Blood Center of Wisconsin · Bristol-Myers Squibb (Belgium)
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在临床试验安全性监控设定下，目标是构建能处理 time-to-event (TITE) 终点的 stopping rule，以在毒性事件过多时及时终止试验。现有方法通常将毒性事件视为二分类结局，而作者提出的 TITE-safety 方法将事件视为生存数据，同时处理重复分析、删失与竞争风险。具体构建了基于 score test、Bayesian beta-extended binomial 模型及序贯概率比检验 (SPRT) 的三种 stopping rule。模拟显示，相比二分类方法，TITE 方法在多种场景下预期毒性事件数减少 20% 以上，且 I 类错误率接近名义水平。该方法通过 R 包 stoppingrule 实现，并重新设计了 BMT CTN 0601 试验的安全性监控方案。对您可能有用：若关注流行病学/临床试验中的因果或安全性评估，本文提供了将生存分析工具嵌入序贯检验的完整范例。
- **关键技术**: `time-to-event endpoint`, `score test`, `Bayesian beta-extended binomial model`, `sequential probability ratio test (SPRT)`, `competing risks`, `group sequential monitoring`
- **为什么对您有用**: 本文属于流行病学/临床试验安全性监控的应用方法论文，将 TITE 信息嵌入序贯 stopping rule，对您在流行病学 secondary interest 中的临床试验数据分析有直接参考价值。从 technical_arsenal 角度，您 very_familiar 的高维渐近理论与 M-estimation 可用于审视其 score test 的渐近性质，但本文核心是序贯设计与 Bayesian 模型，不在您当前武器库的核心方向。follow-up 判断：中期可做——若想深入序贯检验的理论性质，需先在 moderately_familiar 的 M-estimation theory 上补充 group sequential / SPRT 的渐近理论。

### 14. [10.1093/biomtc/ujag085](https://doi.org/10.1093/biomtc/ujag085) · [arXiv](https://arxiv.org/abs/2504.12288) — The underlap coefficient as a measure of a biomarker’s discriminatory ability
- **作者**: Zhaoxi Zhang, Vanda Inácio, Miguel de Carvalho
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在三分类疾病诊断设定下，经典 VUS 与三分类 Youden index 通常要求各组 biomarker 分布满足随机序（stochastic ordering），违反时可能导致误导性结论，且不同 biomarker 的随机序方向可能不一致。本文提出 underlap coefficient（UNL）作为不受随机序假设与分类规则约束的汇总指标，量化 biomarker 区分三组（或更多组）的能力。为刻画患者异质性，进一步发展了 covariate-specific UNL，并对无条件与条件 UNL 分别构造了 Bayesian nonparametric 估计量（基于 Dirichlet process mixture 等）。模拟显示估计量表现良好；实证部分用 ADNI 数据库评估四种阿尔茨海默病 biomarker 区分正常认知、轻度障碍与痴呆的能力，并考察年龄与性别对判别力的影响。对您而言，ADNI 数据集与多分类诊断框架可作为流行病学 secondary interest 的真实数据入口，但方法层面（Bayesian nonparametric）与您常用的 frequentist semiparametric efficiency / debiased ML 路线差异较大。
- **关键技术**: `underlap coefficient`, `Bayesian nonparametric estimation`, `Dirichlet process mixture`, `covariate-specific discriminatory measure`, `volume under ROC surface`, `three-class Youden index`
- **为什么对您有用**: 本文属于流行病学 secondary interest 范畴：(1) 作为入门读物尚可——多分类诊断评价问题清晰，ADNI 数据集结构（三类认知状态、四种 biomarker、协变量）交代明确，但 Bayesian nonparametric 估计部分对不熟悉 Dirichlet process 的读者需额外补课；(2) 武器库中 nonparametric statistics 与 semiparametric theory 可支撑理解 UNL 的定义与性质，但 Bayesian nonparametric 估计量的构造不在常用武器内；(3) 若仅关注数据集与判别指标定义，值得花时间读实证部分；若想深入估计理论，需先在 moderately_familiar 的 semiparametric theory 上补充 Bayesian nonparametric 基础——中期可做。

### 15. [10.1093/biomtc/ujag089](https://doi.org/10.1093/biomtc/ujag089) — Mixed membership latent variable model with unknown factors, factor loadings and number of extreme profiles
- **作者**: Yuyang He, Xinyuan Song, Kai Kang
- **期刊/来源**: Biometrics
- **机构**: Chinese University of Hong Kong · Sun Yat-sen University
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文在混合成员模型（MMM）框架下，目标是在潜因子数量、因子载荷结构与极端剖面（类别）数量均未知时，实现联合的参数估计与模型选择。核心方法提出一种混合成员潜变量模型，内嵌探索性因子分析提取潜预测变量，并采用修改的随机搜索变量选择算法（SSIS）自动确定潜因子及其关联的观测变量。同时，引入贝叶斯惩罚方法选择极端剖面数量，避免了传统基于信息准则方法的低效性。模拟研究表明该方法在参数估计和模型选择上均表现良好。在帕金森病进展标志物倡议（PPMI）数据的应用中，模型识别出具有临床意义的潜特质与不同疾病剖面。对您而言，PPMI数据集是流行病学纵向队列的典型，但本文的贝叶斯潜变量范式与您主攻的半参数/因果推断差异较大，可作为了解疾病异质性建模的参考。
- **关键技术**: `mixed membership model`, `exploratory factor analysis`, `stochastic search variable selection (SSIS)`, `Bayesian penalized model selection`, `Parkinson's Progression Markers Initiative (PPMI)`
- **为什么对您有用**: 本文连接到您的secondary interest流行病学（PPMI纵向队列数据集），但分析范式是贝叶斯潜变量而非因果推断。您武器库中的semiparametric efficiency / HOIF无法直接攻破本文的Bayesian SSIS框架；若要在此数据上做因果推断，需用identification theory重新定义estimand。中期可做：若想利用PPMI数据做因果/半参数分析，需先在moderately_familiar的identification theory上构建潜变量混杂的因果图，本文仅提供数据集入口与异质性描述。

## 其他  *(other, 5 篇)*

### 1. [10.1093/biomtc/ujag065](https://doi.org/10.1093/biomtc/ujag065) · [arXiv](https://arxiv.org/abs/2503.01657) — Nonparanormal adjusted marginal inference
- **作者**: Susanne Dandl, Torsten Hothorn
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 2
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在临床试验协变量调整设定下，本文针对 noncollapsible 效应量（边际 odds ratio / hazard ratio / Cohen's d）提出基于 nonparanormal 模型的调整边际推断方法。核心模型对结局-协变量联合分布建模，直接嵌入边际定义的处理效应参数，同时给出整体决定系数与协变量特异性预后强度度量。对 Cohen's d 特例，理论证明调整预后变量可提高边际 noncollapsible 效应的估计精度；模拟与四项实证亦覆盖 odds / hazard ratio。该方法避免了条件模型中因协变量选择不同导致效应不可比的问题，R 包 tram 提供参考实现。
- **关键技术**: `nonparanormal model`, `marginal odds ratio`, `marginal hazard ratio`, `noncollapsible effect`, `covariate adjustment precision`, `semiparametric transformation model`
- **为什么对您有用**: 直接连接因果推断中 noncollapsible 效应（marginal OR/HR）的协变量调整与效率提升问题，属于 semiparametric 效率理论的边际推断分支。您武器库中 semiparametric theory 与 estimation theory in causal inference 可直接切入：用 semiparametric efficiency bound 验证其声称的精度增益是否达到最优，或用 HOIF 分析更高阶调整的潜力。立即可做：用 very_familiar 的 minimax / efficiency 工具审视其 Cohen's d 精度增益的理论紧性。

### 2. [10.1093/biomtc/ujag091](https://doi.org/10.1093/biomtc/ujag091) — Heterogeneity learning in distributed networks with large-scale survival data
- **作者**: Tingting Cai, Tao Hu, Jianguo Sun, Mengqi Xie
- **期刊/来源**: Biometrics
- **机构**: Capital Normal University · Southern University of Science and Technology · Duke University
- **分类**: vol 82 · issue 2
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究分布式网络中大规模生存数据的异质性学习问题，目标是在 Cox 回归设定下识别跨节点的异质性系数与聚类结构，关键假设是节点间存在地理/网络结构且系数满足稀疏融合约束。提出 Distributed Spanning-Tree-Based Fused Lasso (DSTFL) 方法，利用最小生成树融合框架减少计算与通信负担，并通过 ADMM 算法实现带隐私保护的分布式优化。理论方面建立了估计量的大样本性质与聚类一致性，但未给出 minimax rate 或 semiparametric efficiency bound。实证部分在 SEER 胃癌数据上识别了地理结构化的生存异质性。对您而言，本文的分布式 ADMM 与 fused lasso 聚类属于高维 M-estimation 范畴，但缺乏与您核心武器（higher-order U / efficiency theory / RMT）的直接接口。
- **关键技术**: `Cox regression`, `fused lasso`, `minimum spanning tree fusion`, `distributed ADMM`, `clustering consistency`
- **为什么对您有用**: 本文属于高维 M-estimation 与分布式计算交叉，与您 primary interest 中的 high-dimensional statistics 有边际重叠，但核心工具（fused lasso + ADMM）不在您的 technical arsenal 内。用您 moderately_familiar 的 M-estimation theory 可以审视其大样本性质证明的严谨度，但无法直接切入其分布式优化或聚类一致性率。**中期可做**：若想在分布式高维推断方向发力，需先在 ADMM / communication-efficient distributed inference 上长肌肉；目前缺乏与 efficiency theory / higher-order U 的直接连接点，不建议优先展开。

### 3. [10.1093/biomtc/ujag055](https://doi.org/10.1093/biomtc/ujag055) — A zero-inflated hierarchical generalized transformation model to address non-normality in spatially-informed cell-type deconvolution
- **作者**: Hunter J Melton, Jonathan R Bradley, Chong Wu
- **期刊/来源**: Biometrics
- **机构**: Florida State University · Dartmouth College · University of Missouri · The University of Texas MD Anderson Cancer Center
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对口腔鳞状细胞癌（OSCC）空间转录组数据中高零膨胀问题，提出零膨胀层次广义变换模型（ZI-HGT），并将其嵌入条件自回归去卷积（CARD）框架进行细胞类型比例推断。ZI-HGT 作为辅助贝叶斯变换技术，将高度零膨胀的计数数据与 CARD 的正态假设相衔接，核心机制是通过层次变换对响应变量做正态化校正后再接入 CAR 空间先验。模拟与 OSCC 实数据分析表明 ZI-HGT+CARD 在去卷积精度和不确定性量化上优于忽略零膨胀的方法，并能定位肿瘤微环境中不同成纤维细胞亚群的空间分布。变换模型思路触及半参数理论，但整体处于空间统计/生物信息学语境，与您关注的效率界、因果推断或高维 RMT 无直接交集。
- **关键技术**: `zero-inflated hierarchical transformation model`, `Conditional AutoRegressive (CAR) spatial prior`, `Bayesian cell-type deconvolution`, `generalized transformation for normality correction`, `spatial transcriptomics deconvolution`
- **为什么对您有用**: 本文与您核心兴趣（因果推断、效率理论、高维 RMT、U-statistics）基本无交集；变换模型校正非正态性虽触及半参数思想，但实现路径是贝叶斯层次模型而非 influence function / debiased ML 范式。您的 technical_arsenal 中无空间 CAR 模型与转录组数据结构经验，**暂不可做**：核心空间统计与零膨胀层次贝叶斯机器不在武器库中，需先补空间先验与生物计数数据建模基础才可进入此方向。

### 4. [10.1093/biomtc/ujag070](https://doi.org/10.1093/biomtc/ujag070) — Knowledge-guided Bayesian biclustering model for omics data with noisy graphs
- **作者**: Qiyiwen Zhang, Wenrui Li, Suprateek Kundu, Qi Long
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · University of Connecticut · The University of Texas MD Anderson Cancer Center · University of Pennsylvania
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在高维异质 omics 数据的疾病亚型分型（biclustering）设定下，目标是整合先验生物图谱（如基因调控网络）同时处理图谱中的假阳性（FP）与假阴性（FN）噪声。本文提出 Bayesian denoising knowledge-guided biclustering 方法，将输入图谱视为真实图谱的噪声变体，通过显式建模 FP/FN 错误实现图谱去噪与多图谱同时整合。估计采用 MCMC 算法，避免了传统 graph-guided 方法因忽略图谱 misspecification 导致的 bicluster 识别偏误。模拟与阿尔茨海默症基因表达及蛋白质组学数据分析表明，该方法在去噪与亚型识别上优于忽略图谱噪声的现有方法。对您可能有用：若关注流行病学中的高维图谱数据应用，本文提供了一个处理 misspecified graph prior 的贝叶斯去噪视角，但与 semiparametric efficiency 或 U-statistics 无直接方法学交集。
- **关键技术**: `Bayesian biclustering`, `graph denoising (FP/FN error modeling)`, `MCMC sampling`, `multi-graph integration`, `disease subtyping`
- **为什么对您有用**: 本文属于 secondary interest 中流行病学/生物医学数据集的应用（阿尔茨海默症 omics 数据），但核心方法是贝叶斯 biclustering，与 primary interests（CI, RMT, U-stats, semipara efficiency）无直接方法学重叠。研究者的 very_familiar 武器库（高维渐近理论、minimax bounds）难以直接攻击此贝叶斯 MCMC 方法的理论性质；moderately_familiar 的 M-estimation 理论也与此贝叶斯图模型框架不匹配。暂不可做：核心机器（贝叶斯图模型去噪的 MCMC 收敛理论）不在武器库里，且与研究者主攻方向偏离较大，不建议深入展开读全文。

### 5. [10.1093/biomtc/ujag098](https://doi.org/10.1093/biomtc/ujag098) — Minimum noninferiority dose for phase I clinical trials with immunotherapy
- **作者**: Ninghao Zhang, Guosheng Yin
- **期刊/来源**: Biometrics
- **机构**: University of Hong Kong
- **分类**: vol 82 · issue 2
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在免疫治疗I期临床试验中，本文提出最小非劣效剂量(MND)概念：从最优生物剂量(OBD)出发，寻找在保持疗效非劣于OBD的前提下尽可能低的剂量，无需人为设定疗效目标值。基于calibration-free odds(CFO)设计监控毒性，提出贝叶斯两阶段CFO-MND设计，通过剂量-疗效权衡与自适应随机化实现剂量选择，方法为model-free思路。进一步引入因果推断中的安慰剂等效剂量(placebo equivalent dose)概念，在MND处对药物平均处理效应(ATE)进行初步估计，为后续试验提供因果效应信息。主要贡献为MND定义与CFO-MND设计的操作特性；模拟显示设计在多种场景下稳健。对您可能有用：本文将ATE估计嵌入剂量寻找设计，因果推断部分较浅（仅涉及潜在结果框架下ATE初步估计），但'安慰剂等效剂量'概念为因果推断在临床试验设计中的整合提供了一个具体切入点。
- **关键技术**: `minimum noninferiority dose`, `calibration-free odds design`, `Bayesian two-stage design`, `adaptive randomization`, `placebo equivalent dose`, `average treatment effect estimation`
- **为什么对您有用**: (1) 本文将因果推断ATE估计嵌入I期剂量寻找设计，连接到因果推断在临床试验中的应用子方向，但因果推断理论深度有限——仅涉及潜在结果框架下ATE初步估计，未触及proximal/IV/mediation等研究者关注的核心理论工具；(2) 研究者technical_arsenal中'identification theory in causal inference'可用来审视本文placebo equivalent dose的识别条件是否充分（如unmeasured confounding如何处理），但核心设计方法（CFO、贝叶斯两阶段剂量寻找）不在武器库中；(3) **中期可做**：若想探索因果推断在临床试验中的更深层整合（如用IV处理非依从、用proximal方法处理unmeasured confounding），需先在moderately_familiar的'identification theory in causal inference'上结合临床试验设计文献长肌肉。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

