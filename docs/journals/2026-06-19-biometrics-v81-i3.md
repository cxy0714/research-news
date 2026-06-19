# Biometrics — Vol 81  Issue 3  ·  2026-06-19

- 共 41 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 4 篇（对照 OpenAlex 46 篇）：10.1093/biomtc/ujaf031、10.1093/biomtc/ujaf070、10.1093/biomtc/ujaf079、10.1093/biomtc/ujaf078

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics Vol 81 Issue 3 的 35 篇论文围绕几条方法主线展开。因果推断方向聚焦于处理效应估计在缺失数据、无重叠、交互效应、未测量混杂等复杂场景下的识别与估计，涵盖异质性处理效应（CATE）、动态治疗切换、变量重要性、因果发现、敏感性分析、个性化治疗规则及空间混杂，对应去掉缺失结果数据的 CATE 估计、无重叠下切换治疗效应界、两阶段非参变量重要性、TANM 因果发现、case² 研究 attributable effect 敏感性分析、分布式 ITR 贝叶斯元分析、空间两阶段 DSR 等 7 篇。半参数/非参数方法与效率理论是另一条突出主线，涉及双稳健估计、有效影响函数（EIF）、debiasing、半监督效率提升、分位数分布式滞后、度量空间回归、动态借用历史对照、GEE 调整预测、Cox-Pólya-Gamma 算法等，代表论文包括生存数据预测价值的双稳健非参估计（基于 EIF）、高维半监督线性回归（debiasing 同时提升效率）、形状约束分位数分布式滞后、度量空间二元回归、非参贝叶斯动态借用、adjusted GEE predictor、Cox-Pólya-Gamma 多水平生存模型等。流行病学方法创新集中在纵向替代终点、罕见病外部数据借用、发病率回推、累积发生率函数、复杂抽样校准、累积暴露非线性效应、双变量空间疾病映射等领域，相关论文如半参数联合模型估计纵向替代效应、动态富集贝叶斯 snSMART、基于模拟的发病率重建、生物样本库累积发生率估计、model-assisted calibration 两阶段效率提升、广义 ACE-DLNM、双变量 Poisson 空间疾病映射等。此外，假设检验方向有聚类显著性检验（SigClust-DEV）、二值响应最优分配 I 类错误控制、竞争风险 RMTL 多重检验等 3 篇；高维随机矩阵方向仅一篇多研究多模态协变量增强广义因子模型；计算方法与设计方向涉及稀有事件子抽样容量确定和剂量-反应稳健设计。

因果推断方向的 7 篇论文（从 CATE 缺失数据到空间混杂）直接涉及因果识别、效应界、变量重要性、敏感性分析等核心问题，适合因果研究者优先关注。半参数效率方向的双稳健预测价值、高维半监督线性回归、GEE 调整预测、Cox-Pólya-Gamma 等论文与半参效率理论、debiasing 和有效估计紧密相关。高维方向的广义因子模型和半监督线性回归推进了高维推断与效率。空间因果与空间非参方面，空间混杂 DSR 和单调单指标空间模型对分析点参考数据中的空间混淆有直接参考价值。

## 因果推断  *(causal_inference, 7 篇)*

### 1. [10.1093/biomtc/ujaf098](https://doi.org/10.1093/biomtc/ujaf098) · [arXiv](https://arxiv.org/abs/2412.19711) — Causal machine learning for heterogeneous treatment effects in the presence of missing outcome data
- **作者**: Matthew Pryce, Karla Diaz-Ordaz, Ruth H Keogh, Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文关注缺失结果数据下的异质性处理效应估计问题。在缺失随机（MAR）假设下，标准CATE估计器可能因为某些子群代表性不足而产生偏差。作者将逆概率删失权重（IPCW）引入现有的DR-learner和EP-learner框架，提出mDR-learner和mEP-learner两种去偏机器学习估计器。在正则条件下，这些估计器是oracle有效的，即其渐近方差达到半参效率下界。模拟研究显示它们在偏差、覆盖率和均方误差上优于直接使用完整数据或简单插补的替代方法。本文还利用GBSG2乳腺癌临床试验数据比较激素与非激素疗法的CATE，并给出实践者的实施指导。本研究对您有用：它直接涉及因果推断中CATE估计与缺失数据的结合，方法基于去偏机器学习，您可利用半参理论和M估计知识深入分析其效率性质。
- **关键技术**: `Debiased machine learning`, `DR-learner`, `EP-learner`, `Inverse probability of censoring weighting`, `CATE estimation`, `Oracle efficiency`
- **为什么对您有用**: 本文属于因果推断中子方向'缺失结果数据下的CATE估计'，与您primary interest中的'estimation theory in causal inference'直接相关。具体来说，您可以用'very_familiar'中的非参统计和因果推断估计理论理解其去偏构造，但要严格验证其oracle效率证明需借助'moderately_familiar'中的半参理论（如influence function）。因此，这是一个'中期可做'的扩展点：先加深半参效率理论，即可将此框架推广到更复杂的缺失机制（如非随机缺失）或与其他去偏方法（如折刀）结合。

### 2. [10.1093/biomtc/ujaf085](https://doi.org/10.1093/biomtc/ujaf085) — A positivity robust strategy to study effects of switching treatment
- **作者**: Matias Janvin, Pål C Ryalen, Aaron L Sarvet, Mats J Stensrud
- **期刊/来源**: Biometrics
- **机构**: University of Oslo · University of Massachusetts Amherst · École Polytechnique Fédérale de Lausanne
- **分类**: vol 81 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在医疗观察性研究中，个体常经历复发事件后才会切换治疗，但实际数据中观察到的切换者极少甚至为零，导致传统因果方法失效。本文考虑一个动态治疗切换设定，利用基线复发事件的初始观测来提供治疗更新建议，目标是在几乎无直接对比数据的条件下估计切换治疗对后续事件的平均因果效应。核心贡献有两部分：一是推导了在无交叠（positivity）假设下可识别的效应界，并给出非参数界估计量；二是在部分识别框架下定义价值函数和遗憾函数，进而确立悲观（maximin）、乐观（maximax）和机会主义（minimax regret）三种最优动态治疗制度。其中悲观者制度保证期望预后至少不低于标准治疗。将方法应用于Systolic Blood Pressure Intervention Trial（SPRINT）数据，展示了实际可行性。该方法直接回应了因果推断中处理治疗切换的稳健性与识别问题，对纵向因果推断及部分识别研究具有参考价值。
- **关键技术**: `partial identification`, `nonparametric bounds`, `dynamic treatment regimes`, `value function`, `minimax regret`
- **为什么对您有用**: 该论文聚焦因果推断中动态治疗切换的部分识别问题，与您的纵向因果推断和识别理论方向高度吻合。您的武器库中非常熟悉非参数统计和因果推断估计理论，可快速复现其非参数界估计量，并检验最优制度选择机制；部分识别部分则需要进一步熟悉identification theory（中等熟悉项），属于中期可做的拓展方向。

### 3. [10.1093/biomtc/ujaf095](https://doi.org/10.1093/biomtc/ujaf095) — Valid and efficient inference for nonparametric variable importance in two-phase studies
- **作者**: Guorong Dai, Raymond J Carroll, Jinbo Chen
- **期刊/来源**: Biometrics
- **机构**: Fudan University · Texas A&M University · University of Pennsylvania
- **分类**: vol 81 · issue 3
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 考虑两阶段研究设定，其中响应变量 Y 和廉价协变量 X 可在大样本中观测，而昂贵协变量 Z 仅在一小子样本中测量。目标是推断 Z 在预测 Y 中的非参数变量重要性，定义为 Z 在多个预测模型中最大潜在贡献的聚合，由一般损失函数量化。本文提出一种新方法，通过用 (Y, X) 的函数替代每个个体对涉及 Z 的预测损失的贡献，来处理 Z 的缺失机制。该方法在 Z 对 Y 是否贡献零或正值时均能实现统一且有效的推断，这一属性因数据不完整而令人惊讶。理论部分建立了半监督推断和两阶段非参数估计的新结果，数值模拟和真实数据展示了方法的优越性能。对您而言，本文连接了因果推断中的变量重要性度量与您擅长的非参数估计、效率理论，尤其涉及两阶段抽样和缺失数据问题。
- **关键技术**: `two-phase sampling`, `nonparametric variable importance`, `semi-supervised inference`, `efficient estimation`, `imputation-based adjustment`
- **为什么对您有用**: 直接对应您在因果推断中 variable importance 的兴趣，且处理方法与您的非参数理论与效率理论 arsenal 高度相关。您可立即运用 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 分析其估计量的一致性与收敛速率，甚至尝试用 HOIF（moderately_familiar）扩展至更高阶影响函数。结论：立即可做。

### 4. [10.1093/biomtc/ujaf089](https://doi.org/10.1093/biomtc/ujaf089) — Tree-based additive noise directed acyclic graphical models for nonlinear causal discovery with interactions
- **作者**: Fangting Zhou, Kejun He, Yang Ni
- **期刊/来源**: Biometrics
- **机构**: Yale University · Renmin University of China · The University of Texas at Austin · Texas A&M University
- **分类**: vol 81 · issue 3
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在非线性因果发现设定下，传统 additive noise DAG 模型假设结构因果函数为纯加性，无法捕捉因果交互效应；本文提出 tree-based additive noise model（TANM），用树结构表示分段常数的因果函数以纳入交互项，目标为 DAG 的 identifiability 与拓扑排序估计。因树构造导致因果函数不连续/不平滑，现有基于连续光滑函数的 ANM identifiability 结果不再适用，作者给出新的 identifiability 条件（涉及条件分布的 piecewise 结构与交互项可分性）。算法层面，开发了递归 source node identification 与 score-based ordering search；模拟显示在强交互存在时优于 GP/neural-network ANM，且计算代价与可解释性更优。实证应用于乳腺癌蛋白质–蛋白质交互网络推断。对您有用：TANM 的 identifiability 新条件与 piecewise 结构为 semiparametric/nonparametric 因果识别理论提供了一个非光滑设定的新切入点。
- **关键技术**: `tree-based additive noise model`, `DAG identifiability with piecewise constant functions`, `score-based ordering search`, `recursive source node identification`, `nonlinear causal discovery with interactions`
- **为什么对您有用**: 直接连接 causal inference 的 identification theory 子方向，特别是非光滑/分段常数因果函数下的 identifiability 条件，突破了传统 ANM 对连续光滑函数的依赖。您 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 identification theory in causal inference 可以直接攻这篇 paper 的 identifiability 新条件是否可进一步弱化或推广至更一般的 piecewise/sieve 设定。**立即可做**：用现有的 nonparametric minimax 与 identification 理论工具审视其 identifiability 条件的紧性与可推广性。

### 5. [10.1093/biomtc/ujaf102](https://doi.org/10.1093/biomtc/ujaf102) — Sensitivity analysis for attributable effects in case2 studies
- **作者**: Kan Chen, Ting Ye, Dylan S Small
- **期刊/来源**: Biometrics
- **机构**: Cancer Research And Biostatistics · Seattle Pacific University · University of Washington · University of the Sciences · University of Pennsylvania
- **分类**: vol 81 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该文聚焦于 case² 研究设计（case-case study）中的 attributable effect，即第一类病例中因治疗而避免发生的病例数。传统推断依赖于两个关键假设：治疗不导致第二类病例，且治疗不改变个体的病例类型。然而这些假设在许多实际场景中不成立。本文提出了一个系统的敏感性分析框架，用于评估偏离这两个假设对 attributable effect 推断的影响。此外，还纳入了针对未测量混杂的敏感性分析，以处理潜在偏倚。方法通过 1993 年美国国家死亡率随访调查数据（验证暴力行为是否增加自杀风险）进行了实证演示。该框架为因果推断中假设偏离的稳健性检验提供了具体工具，尤其适用于病例-病例设计。这与您对因果推断中敏感性分析的兴趣直接相关，且所使用的流行病学数据集也为二次分析提供了参考。
- **关键技术**: `sensitivity analysis`, `attributable effect`, `case-case design`, `unmeasured confounding`, `observational study`
- **为什么对您有用**: 本文属于因果推断中敏感性分析的具体方法拓展，直接连接您 primary interest 中的 sensitivity analysis 子方向。您的 technical arsenal 中 'estimation theory in causal inference' 和 'nonparametric statistics' (very_familiar) 可直接用于理解其识别策略与推断流程，并可复现或扩展其敏感性分析框架到其他 case² 设计场景。立即可做：无需新工具即可阅读并评估其方法论贡献。

### 6. [10.1093/biomtc/ujaf082](https://doi.org/10.1093/biomtc/ujaf082) · [arXiv](https://arxiv.org/abs/2406.03056) — Sparse 2-stage Bayesian meta-analysis for individualized treatments
- **作者**: Junwei Shen, Erica E M Moodie, Shirin Golchi
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多站点数据无法共享个体水平信息的设定下，目标是估计优化期望患者结局的个性化治疗规则（ITR），关键假设为各站点模型参数的稀疏性与异质性。本文提出两阶段贝叶斯元分析方法：第一阶段各站点本地拟合贝叶斯线性模型并提取后验摘要统计量，第二阶段在中心聚合这些摘要，通过 spike-and-slab 先验同时实现跨站点参数异质性的部分共享与 ITR 稀疏结构的变量选择。模拟表明该方法能一致估计完全刻画最优 ITR 的参数（尤其是微弱的 treatment-covariate 交互项），并在国际华法林药物遗传学联盟数据上估计最优华法林剂量策略。对您可能有用：该文在分布式因果推断设定下处理了小交互效应与站点间稀疏异质性的联合问题，与您 primary interest 中的因果推断估计理论及 sensitivity 分析设定有直接对接。
- **关键技术**: `Bayesian meta-analysis`, `spike-and-slab prior`, `individualized treatment rule`, `distributed inference`, `treatment-covariate interaction`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的因果推断估计理论（个性化治疗规则/ITR 的估计），特别是多站点分布式因果推断设定下小交互效应的识别与稀疏变量选择。从您 technical_arsenal 的视角，可用 M-estimation theory（moderately_familiar）审视其两阶段贝叶斯估计的渐近性质（如一致性是否可转化为 semiparametric 效率界讨论），或用 minimax bounds（very_familiar）分析其声称的交互项估计收敛率是否紧。**中期可做**：若想从频率派视角建立该分布式稀疏 ITR 估计的效率理论，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以推导分布式设定下的 influence function 与效率界。

### 7. [10.1093/biomtc/ujaf093](https://doi.org/10.1093/biomtc/ujaf093) · [arXiv](https://arxiv.org/abs/2404.09358) — Two-stage estimators for spatial confounding with point-referenced data
- **作者**: Nate Wiecha, Jane A Hoppin, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在空间因果推断设定下，当暴露变量与空间相关未测量混杂（如环境污染物）关联时，标准空间回归会产生偏倚和推断失效，目标是估计暴露效应。本文将 geoadditive SEM（gSEM）与 double machine learning / 两阶段半参数回归联系起来，提出 double spatial regression（DSR）估计量：先用 Matérn 协方差 Gaussian process 分别拟合暴露与结局的空间趋势并移除，再对残差做 OLS。在适当 regularity 条件下，DSR 达到 root-n 一致渐近正态，并提供闭式方差估计；模拟中标准空间回归严重偏倚且覆盖率极差，DSR 有效消除偏倚并达到 nominal coverage。对您有用：DSR 的 orthogonal / two-stage 结构直接对接您 efficiency theory 与 semiparametric theory 的武器库，空间混杂设定为流行病学应用提供了新场景。
- **关键技术**: `double machine learning`, `two-stage semiparametric regression`, `Gaussian process with Matérn covariance`, `geoadditive structural equation modeling`, `root-n asymptotic normality`, `spatial confounding`
- **为什么对您有用**: 本文直接对接 causal inference 中的混杂调整与 efficiency theory：DSR 的 orthogonal score / two-stage 结构是您 very_familiar 的 DML 框架在空间数据上的具体实现，regularity 条件的推导可用您 moderately_familiar 的 semiparametric theory 审视其是否达到 semiparametric efficiency bound。Follow-up 判断：**立即可做**——用 very_familiar 的 minimax bounds 与 M-estimation theory 检验 DSR 在空间混杂下的效率性质，或将其推广至 longitudinal / mediation 设定。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujaf107](https://doi.org/10.1093/biomtc/ujaf107) · [arXiv](https://arxiv.org/abs/2507.09889) — High-dimensional multi-study multi-modality covariate-augmented generalized factor model
- **作者**: Wei Liu, Qingzhi Zhong
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对现有因子模型无法同时整合多研究多模态数据的问题，该文提出一个高维广义因子模型，并允许纳入额外协变量，以提升模型解释力。在识别性方面，作者系统讨论了模型参数的识别条件，确保参数意义明确。为处理四个大型潜在随机矩阵导致的高维非线性整合难题，采用变分下界近似观测对数似然，将推断转化为变分后验分布的优化问题。进一步基于M估计理论，通过对变分参数进行剖面处理，建立了模型参数估计量的渐近性质（如一致性和渐近正态性）。算法层面，设计了一个计算高效的变分期望最大化（EM）算法，并给出了确定研究共享因子与研究特有因子个数的方法。大量模拟和真实数据应用表明，该方法在估计精度和计算效率上显著优于现有竞争方法。该文将高维因子分析与变分推断、M估计相结合，对您在高维统计和统计计算方面的兴趣有直接参考价值。
- **关键技术**: `variational lower bound`, `M-estimation theory`, `variational EM algorithm`, `high-dimensional generalized factor model`, `identification conditions`, `large latent random matrices`
- **为什么对您有用**: 本文直接涉及高维统计（random matrix theory）和统计计算（算法实现），属于您的主要兴趣；您在very_familiar中的'高维渐近'和'M估计理论'可以快速用于评估其理论证明的严谨性（如渐近正态性条件是否紧），且变分EM算法的细节可作为您'软件发展'和'统计计算'方向的案例参考。follow-up粗判：立即可做——用您已有的M估计和高维渐近工具即可深入剖析该文理论部分，并考虑将其推广至更一般的广义线性模型设定。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1093/biomtc/ujaf123](https://doi.org/10.1093/biomtc/ujaf123) · [arXiv](https://arxiv.org/abs/2302.11746) — Binary regression and classification with covariates in metric spaces
- **作者**: Yinan Lin, Zhenhua Lin
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对协变量位于一般度量空间（无需向量结构）的二元响应问题，提出了一种受逻辑回归启发的回归模型和相应的分类器。通过将协变量作为度量空间中的元素，该模型允许处理函数型数据、流形数据等复杂对象。采用最大似然估计来估计度量空间中的回归系数，并基于度量熵条件给出了估计误差的上界。在常见的度量空间（如Riemannian流形）上推导了匹配的极小化下界，证明所提估计量在这些空间中的最优性。对于Riemannian流形，进一步得到了更精细的上界和匹配的下界，从而建立了分类器的最优性。数值实验和fMRI数据应用展示了方法的实用性。该工作首次在一般度量空间中为二元回归提供了极小化最优估计理论，对非欧几里得数据的统计建模具有基础性意义。与您对非参数统计和极小化界的兴趣高度契合，可直接将现有极小化工具扩展至度量空间协变量的因果推断问题。
- **关键技术**: `metric entropy`, `minimax lower bound`, `maximum likelihood estimation`, `Riemannian manifolds`, `binary classification`
- **为什么对您有用**: 本文直接对应您的primary interest中的『非参数统计』和『minimax bounds for estimation problems』，将经典回归理论推广到度量空间协变量，并给出了完整的最优性分析。您的技术武器库中『minimax bounds for estimation problems』可直接用于验证或改进本文的下界构造，而『nonparametric statistics』的框架可帮助您理解其理论贡献。目前可立即可做：将本文的极小化界技巧用于您熟悉的非参数设定下的因果推断问题，探索度量空间中的影响函数表示。

### 2. [10.1093/biomtc/ujaf101](https://doi.org/10.1093/biomtc/ujaf101) · [arXiv](https://arxiv.org/abs/2408.08450) — Smooth and shape-constrained quantile distributed lag models
- **作者**: Yisen Jin, Aaron J Molstad, Ander Wilson, Joseph Antonelli
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在环境流行病学中，妊娠期污染物暴露对出生体重等结局的影响往往存在“易感窗口”，传统条件均值型分布式滞后模型仅关注平均效应，无法刻画临床最关心的极端分位数。本文提出两种新的分位数分布式滞后模型（QDLM）估计量，通过在分位数回归框架中引入平滑性惩罚和形状约束（如单峰性、凹性）来提升估计效率与可解释性。方法上，估计量基于B样条基展开并施加不等式约束（如单调递减、先增后减等），通过凸优化求解。在科罗拉多出生队列数据中，新方法成功识别出孕期不同阶段的暴露关键窗口，且估计区间比传统QDLM更窄、生物学解释更清晰。该工作为极端分位数下的环境健康效应分析提供了可操作的工具。对您而言，本文连接secondary interest中的流行病学应用，以及primary interest中的semiparametric & nonparametric theory——具体是分位数回归和形状约束估计。
- **关键技术**: `Quantile regression`, `Distributed lag models`, `Shape-constrained regression`, `Unimodality constraints`, `Concavity constraints`, `B-spline basis expansion`
- **为什么对您有用**: 本文与您的 semiparametric & nonparametric theory 兴趣直接相关，具体是分位数回归和形状约束估计；同时连接 secondary 中的流行病学实际数据应用。利用您 very_familiar 中的 nonparametric statistics（B样条、约束优化）可直接复现并理解该方法的渐近性质。立即可做：方法本身不涉及您不熟悉的计算复杂性或高维工具，用现有的非参数样条知识即可评估其创新点并考虑推广到您的因果推断问题（如滞后暴露的因果效应估计）。

### 3. [10.1093/biomtc/ujaf118](https://doi.org/10.1093/biomtc/ujaf118) · [arXiv](https://arxiv.org/abs/2411.11675) — Nonparametric Bayesian approach for dynamic borrowing of historical control data
- **作者**: Tomohiro Ohigashi, Kazushi Maruo, Takashi Sozu, Masahiko Gosho
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在纳入历史对照数据以分析当前 RCT 时，若存在未测量因素导致异质性且仅调整观测协变量不足，目标是动态借阅同质历史对照并抑制异质对照的影响。本文提出基于非参数贝叶斯的方法处理试验间异质性，并引入依赖 Dirichlet 过程（DP）混合模型以强化历史与当前对照间的冲突解决机制。该方法对聚合研究级数据与个体参与者数据统一适用，并基于目标参数的后验分布构建了衡量历史与当前对照相似度的新指标。模拟与临床试验实例表明，依赖 DP 混合方法在异质历史对照场景下优于典型 DP 混合与元分析方法，能更准确地借阅同质数据并有效降权异质数据。对您可能有用：该框架为处理因果推断中未测量混杂导致的异质性提供了非参数贝叶斯视角的动态借阅思路。
- **关键技术**: `dependent Dirichlet process mixture`, `dynamic borrowing`, `nonparametric Bayesian`, `posterior similarity index`, `historical control data integration`
- **为什么对您有用**: 本文连接到因果推断中处理未测量混杂与外部数据整合的设定，特别是 RCT 历史对照的动态借阅问题。您武器库中的 nonparametric statistics 与 identification theory in causal inference 可以用来审视该非参数贝叶斯方法的 identification 假设与收敛性质，但当前方法核心依赖贝叶斯非参数（DP mixture）而非您熟悉的 semiparametric efficiency / influence function 路线。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，探索能否用 HOIF 或 debiased ML 构造出与该 DP mixture 动态借阅对应的频率派 semiparametric efficient estimator。

### 4. [10.1093/biomtc/ujaf090](https://doi.org/10.1093/biomtc/ujaf090) — Adjusted predictions for generalized estimating equations
- **作者**: Francis K C Hui, Samuel Muller, Alan H Welsh
- **期刊/来源**: Biometrics
- **机构**: Australian National University · Macquarie University
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在纵向数据的独立簇 GEE 设定下，目标是利用已观测时间点的信息提升对新时间点响应变量的预测精度，传统方法仅依赖边际均值模型。本文将 GEE 的迭代求解视为迭代工作线性模型，借用 universal kriging 思想，通过工作交叉相关矩阵构建 adjusted GEE predictor，将同一簇内当前与新观测的关联纳入预测。理论上给出了 adjusted predictor 在均方误差意义下优于 standard marginal predictor 的充分条件。模拟与 Sitka spruce 生长数据表明，即使工作相关结构误设，adjusted predictor 仍可优于标准 GEE 预测、使用全部时间点的 oracle GEE 预测，乃至 GLMM 的簇特定预测。对您可能有用：该工作将 kriging 与 GEE 结合的思路为纵向因果推断中处理时间依赖预测与敏感性分析提供了新视角。
- **关键技术**: `generalized estimating equations`, `universal kriging`, `working cross-correlation matrix`, `iterative working linear model`, `mean squared prediction error`
- **为什么对您有用**: 本文直接涉及纵向数据（longitudinal）的 GEE 预测改进，连接到您 primary interest 中的 causal inference (longitudinal) 子方向——纵向因果推断中常需对未来时间点做 counterfactual prediction，adjusted predictor 的交叉相关借用思路可迁移至 longitudinal IV / mediation 的预测环节。用您 very_familiar 的 M-estimation theory（moderately_familiar）可直接审视其迭代工作线性模型的收敛与 MSPE 理论条件是否可进一步放宽。**中期可做**：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以严格分析 adjusted predictor 在更复杂纵向因果 estimand 下的效率性质。

### 5. [10.1093/biomtc/ujaf105](https://doi.org/10.1093/biomtc/ujaf105) · [arXiv](https://arxiv.org/abs/2507.09057) — A monotone single index model for spatially referenced multistate current status data
- **作者**: Snigdha Das, Minwoo Chae, Debdeep Pati, Dipankar Bandyopadhyay
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在空间聚类多状态当前状态数据（current status data）设定下，目标是估计疾病状态转移时间与转移概率，核心假设为随机检查时间与事件时间的独立性及空间随机效应的可分性。作者提出贝叶斯半参数加速失效时间（AFT）模型：误差项采用 Dirichlet process mixture of Gaussians 建模，空间关联通过逆 Wishart 提案的随机效应刻画；系统成分使用单调单指标模型（monotone single index model），未知链接函数通过积分基展开并赋予约束 Gaussian process 先验来估计。理论上证明了参数可识别性；计算上结合 elliptical slice sampling 与 circulant embedding 实现可扩展的 MCMC，并给出状态占据与转移概率的估计。对您可能有用：本文的约束 Gaussian process 先验与 DPM 误差建模为半参数/非参数理论提供了贝叶斯视角的单指标模型识别与收敛参考，且流行病学数据结构可作为 secondary interest 的应用案例。
- **关键技术**: `monotone single index model`, `Dirichlet process mixture of Gaussians`, `constrained Gaussian process prior`, `accelerated failure time model`, `elliptical slice sampling`, `circulant embedding`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向（单调单指标模型的贝叶斯非参数估计与可识别性），以及 epidemiology secondary interest（牙周病多状态当前状态数据的空间聚类结构）。从 technical_arsenal 看，您 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 semiparametric theory 可直接攻入本文的单指标模型识别与先验收敛率分析口子（当前论文仅证可识别性，未给后验收缩率）。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体为贝叶斯非参数后验收缩率理论），才能将本文的可识别性结果推进到后验 minimax 收缩率。

### 6. [10.1093/biomtc/ujaf122](https://doi.org/10.1093/biomtc/ujaf122) — Exploring the heterogeneity in recurrent episode lengths based on quantile regression
- **作者**: Yi Liu, Guillermo E Umpierrez, Limin Peng
- **期刊/来源**: Biometrics
- **机构**: Emory University
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在慢性病反复发作事件数据设定下，目标是刻画个体内重复发作时长异质性的分位数参数（quantile coefficients），关键假设是放松传统方法中发作时长可交换性（exchangeability）的限制并允许依赖时变协变量。将重复发作视为聚类数据，作者提出分位数回归估计程序，通过逆概率加权（IPW）类手段同时处理依赖截断（dependent truncation）、依赖删失（dependent censoring）与信息性聚类规模（informative cluster size）三类复杂缺失机制。估计程序计算简便，所得估计量具备 n^{-1/2}-CAN 渐近正态性与标准分位数回归类似的推断性质。数值模拟显示该方法在偏差与覆盖率上优于忽略聚类依赖或强行施加可交换假设的朴素改编方法。对您可能有用：本文在聚类数据分位数回归框架下处理 informative cluster size 与依赖截断/删失的 semiparametric 推断，其 IPW 权重构造与渐近方差推导思路可迁移至 longitudinal causal inference 中带 informative dropout 的 semiparametric 估计问题。
- **关键技术**: `quantile regression`, `dependent censoring`, `dependent truncation`, `informative cluster size`, `inverse probability weighting`, `asymptotic normality`
- **为什么对您有用**: 本文连接到 longitudinal causal inference 与 semiparametric theory 子方向：其处理 informative cluster size 与 dependent truncation/censoring 的 IPW 构造，与纵向因果推断中 informative dropout / missing-at-random-but-dependent 的 semiparametric 估计问题结构同构。用 technical_arsenal 中 moderately_familiar 的 semiparametric theory 可以攻本文估计量的 influence function 与效率界缺口——本文未讨论 semiparametric efficiency bound，这是一个可切入的理论口子。follow-up 判断：中期可做——需先在 moderately_familiar 的 semiparametric theory 上长肌肉（具体是推导带 informative cluster size 约束下的 efficient influence function），才能将本文 IPW 估计提升至 one-step / DR 估计并刻画效率界。

### 7. [10.1093/biomtc/ujaf121](https://doi.org/10.1093/biomtc/ujaf121) — The Cox-Pólya-Gamma algorithm for flexible Bayesian inference of multilevel survival models
- **作者**: Benny Ren, Jeffrey S Morris, Ian Barnett
- **期刊/来源**: Biometrics
- **机构**: Regeneron (United States) · Stony Brook School · Stony Brook University · University of Pennsylvania
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在 Bayesian Cox 半参数回归设定下，目标是同时对非参数 baseline cumulative hazard（需满足单调性约束）与多水平回归（frailty / case weights / smoothing splines）进行推断。本文提出 Cox-Pólya-Gamma 算法，利用 Cox 模型的椭圆信息几何将生存模型与层次 Gaussian 模型桥接。核心计算策略有两步：首先通过 Poisson 过程将 Cox 模型近似为负二项过程，从而将 Bayesian 计算降维为迭代 Gaussian sampling；其次利用充分维度缩减与 beta 充分统计量，在 Gibbs sampler 中 collapse 处理非参数 baseline cumulative hazard 的 Markov transition，巧妙绕开单调性约束的直接采样困难。理论上给出了该算法 uniform ergodicity 的条件，并附带开源软件实现。对您可能有用：该算法将半参数 Cox 模型的计算转化为 Gaussian 后验采样与 beta collapse，为 semiparametric 推断中的 constrained M-estimation 提供了新颖的 computational shortcut。
- **关键技术**: `Pólya-Gamma data augmentation`, `negative binomial process approximation`, `sufficient dimension reduction`, `Gibbs sampler collapse`, `uniform ergodicity`, `elliptical information geometry`
- **为什么对您有用**: 直接连接 semiparametric theory 子方向：Cox 模型是半参数效率理论的经典对象，本文从计算角度用椭圆几何与 sufficient dimension reduction 统一处理 baseline hazard 的单调约束与多水平结构。用 very_familiar 中的 software development 与 M-estimation theory（moderately_familiar）可以审视其 Gibbs collapse 步骤的数值稳定性与收敛条件是否可推广至更一般的 semiparametric constrained M-estimator。中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以评估该 sufficient dimension reduction 策略在其他半参数模型（如 longitudinal Cox / mediation）中的迁移潜力。

### 8. [10.1093/biomtc/ujaf117](https://doi.org/10.1093/biomtc/ujaf117) — A group distributional ICA method for decomposing multi-subject diffusion tensor imaging
- **作者**: Guangming Yang, Ben Wu, Jian Kang, Ying Guo
- **期刊/来源**: Biometrics
- **机构**: Emory University · Renmin University of China · University of Michigan
- **分类**: vol 81 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在多受试者扩散张量成像（DTI）数据分析设定下，目标是针对 3D diffusion tensor 的特殊分布结构进行盲源分离与降维去噪，现有标准 ICA 因不兼容 tensor 参数空间而无法直接应用。本文提出 Group Distributional ICA (G-DICA)，将观测数据的分布函数参数分解为独立源信号的混合，从而在分布层面而非原始观测层面实现组水平 ICA。核心机制是将 DTI tensor 的分布参数映射至可分离的源信号空间，并利用组水平约束提取对应主要白质纤维束的结构网络。模拟与真实数据表明 G-DICA 在重现性与分离性能上优于现有方法，但摘要未给出具体的收敛率或效率界理论结果。对您可能有用：若将此分布参数混合模型视作 semiparametric 模型，可探讨其 identification 条件与 semiparametric efficiency bound。
- **关键技术**: `blind source separation`, `independent component analysis`, `distributional ICA`, `diffusion tensor imaging`, `multi-subject decomposition`, `tensor distribution parameters`
- **为什么对您有用**: 本文属于 DTI 神经影像数据的盲源分离方法，与您 primary interest 中的 semiparametric / nonparametric theory 有间接连接——G-DICA 本质是对分布参数空间的混合分解，其 identification 与 estimation 效率可纳入 semiparametric 框架审视。用您 very_familiar 的 minimax bounds for estimation problems 可评估其 estimator 在分布参数空间中的收敛率是否达到最优；但本文偏向生物统计应用，理论深度有限。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，才能为这类分布参数混合模型建立严格的 efficiency bound 与 identification 理论。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujaf084](https://doi.org/10.1093/biomtc/ujaf084) — Doubly robust nonparametric estimators of the predictive value of covariates for survival data
- **作者**: Torben Martinussen, Mark J van der Laan
- **期刊/来源**: Biometrics
- **机构**: University of Copenhagen · University of California, Berkeley
- **分类**: vol 81 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究生存数据中协变量的预测价值，以阳性预测值曲线（PPV）为目标 estimand，基于非参数评分规则。将 PPV 视为数据生成概率测度的一个光滑泛函，通过计算其有效影响函数（EIF）构造双稳健非参数估计量。该估计量具有双稳健性：当生存模型或评分规则中有一个正确指定时，估计量仍相合，且达到半参数效率界。论文推导了 EIF 的显式形式，给出了估计量的渐近正态性和收敛速率。通过数值模拟和两项癌症数据研究验证了有限样本性能。本文对您有用：直接连接您在半参数效率理论与 debiased ML 方向的核心兴趣，且提供了在生存数据中应用 EIF 和双稳健技术的具体案例。
- **关键技术**: `efficient influence function`, `doubly robust estimator`, `nonparametric scoring rule`, `survival data`, `positive predictive value`
- **为什么对您有用**: 本文属于您 primary interest 中的 efficiency theory（半参数效率界、双稳健估计）在生存数据中的应用，是 van der Laan 的经典技术路线。您可以用 very_familiar 的 nonparametric statistics 理解其非参数部分，并用 moderately_familiar 的 semiparametric theory 审视其 EIF 推导与 double robustness 论证，属于中期可做：需先加强对半参数效率理论在复杂数据（如生存数据）中具体形式的理解，之后即可独立将该方法迁移至其他因果推断或 U-statistics 设定。

### 2. [10.1093/biomtc/ujaf113](https://doi.org/10.1093/biomtc/ujaf113) · [arXiv](https://arxiv.org/abs/2311.17685) — Semi-supervised linear regression: enhancing efficiency and robustness in high dimensions
- **作者**: Kai Chen, Yuqian Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维半监督设定下，本文挑战了"无标签数据仅在模型误设时才有用"的传统认知，证明即使真实模型是线性，大量无标签数据也能降低估计偏差、提升效率与推断鲁棒性。针对dense场景（population slope无稀疏假设），作者提出基于debiasing的鲁棒半监督估计量，利用无标签数据修正高维偏差。在sparse场景下，进一步提出效率增强的半监督方法，结合稀疏结构与无标签信息获得更优收敛率。核心工具为debiasing / one-step correction与高维半监督推断框架，理论证明无标签样本可同时改善偏差与方差。对您有用：直接推进了高维debiasing与效率理论在半监督场景的边界，与您关注的semiparametric efficiency bounds及debiased ML高度对接。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `high-dimensional debiased estimator`, `semi-supervised inference`, `one-step correction`, `sparse linear regression`, `bias reduction via unlabeled data`
- **为什么对您有用**: 直接连接您primary interest中的efficiency theory (debiased ML)与高维统计：本文在dense无稀疏假设下用debiasing修正高维偏差，是您very_familiar的高维渐近与estimation theory可直接切入的口子。用您moderately_familiar的semiparametric theory（特别是one-step / influence function修正）可以审视其效率声称是否达到semiparametric efficiency bound。**立即可做**：用very_familiar的高维渐近工具验证其dense场景debiasing的收敛率；若想深挖sparse场景的效率增强，需先在moderately_familiar的semiparametric efficiency bound技术上稍作加强。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biomtc/ujaf120](https://doi.org/10.1093/biomtc/ujaf120) — Statistical significance of clustering for count data
- **作者**: Yifan Dai, Di Wu, Yufeng Liu
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · University of Michigan
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维计数数据（如基因组学 scRNA-seq）聚类设定下，目标是检验聚类结果的统计显著性，即判断所观测到的簇是否可能仅由自然抽样变异产生而非真实异质性。现有 SigClust 方法基于单 Gaussian 假设设计，对非 Gaussian 离散数据不仅模型失配且统计功效显著下降。本文提出 SigClust-DEV，通过引入离散分布（如 Poisson / Negative Binomial）的偏差度量来构造检验统计量与参考分布，从而在计数数据下实现聚类显著性的 Monte Carlo 检验。模拟显示 SigClust-DEV 在多种计数分布下功效优于原 SigClust 变体，并在 Hydra scRNA 数据与癌症 EHR 数据中识别出有意义的亚组。对您可能有用：本文将高维假设检验从 Gaussian 拓展到计数型，其功效分析与参考分布构造思路可迁移至您对高维假设检验的关注。
- **关键技术**: `SigClust`, `Monte Carlo hypothesis testing`, `Poisson / Negative Binomial deviation measure`, `high-dimensional count data`, `cluster significance assessment`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 hypothesis testing 子方向，处理高维计数数据下聚类显著性的检验问题。从 technical_arsenal 看，您 very_familiar 的 minimax bounds 与 high-dimensional asymptotics 可用于分析 SigClust-DEV 检验统计量在高维计数设定下的极限行为与功效界，这是攻入本文理论缺口的具体口子。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立离散偏差统计量在非 Gaussian 高维下的 M-estimator 渐近理论，从而将本文的纯模拟/算法驱动推进到有严格功效界与渐近保证的理论层面。

### 2. [10.1093/biomtc/ujaf114](https://doi.org/10.1093/biomtc/ujaf114) · [arXiv](https://arxiv.org/abs/2502.06381) — Revisiting optimal allocations for binary responses: insights from considering type-I error rate control
- **作者**: Lukas Pin, Sofía S Villar, William F Rosenberger
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文重新审视二值结局响应自适应设计中最优分配比例导致的I类错误率膨胀问题，发现该问题在文献中未被充分记录。作者比较了已有校正方法，发现均无法稳健控制I类错误。他们推导了两种基于score检验（代替Wald检验）且使用有限样本估计（代替未知真值）的新最优分配比例：一种优化统计检验效能，另一种在固定方差下最小化总失败数。通过早期与确证性试验的模拟，新设计在控制I类错误的同时显著改善患者结局。本文框架可自然推广至多臂试验和其他结局类型。对您的价值在于：直接涉及假设检验中检验统计量选择与error rate控制，您可利用熟悉的hypothesis testing渐近理论评估其有限样本表现。
- **关键技术**: `response-adaptive randomization`, `optimal allocation proportions`, `score test vs Wald test`, `type-I error rate inflation`, `finite-sample estimation`, `power optimization`
- **为什么对您有用**: 连接至您primary interests中的hypothesis testing子方向，特别是检验统计量选择对I类错误的影响。您very_familiar中的'estimation theory in causal inference'可直接用于分析finite-sample estimators在本文新比例下的偏差与方差权衡。follow-up判据：立即可做——您可运用经典渐近理论验证score test分配的渐近相对效率，或借助高维渐近工具扩展到多臂情形。

### 3. [10.1093/biomtc/ujaf086](https://doi.org/10.1093/biomtc/ujaf086) · [arXiv](https://arxiv.org/abs/2409.07917) — Multiple tests for restricted mean time lost with competing risks data
- **作者**: Merle Munko, Dennis Dobler, Marc Ditzhaus
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在竞争风险框架下，目标是检验受限平均损失时间（RMTL）在因子设计与任意事件类型数下的组间差异，RMTL定义为累积发生率函数至预指定时间点的积分。本文基于Wald-type检验统计量构造一般对比检验，并去除了事件时间分布的连续性假设以允许数据中存在结（ties）。为改善小样本表现，进一步提出基于permutation的检验方案；在多重检验阶段，利用局部检验统计量间的渐近精确依赖结构以提升检验功效。模拟与白血病骨髓移植真实数据验证了方法实用性。对您可能有用：本文在生存/竞争风险设定下放宽连续性假设并做依赖结构的多重检验，与您在hypothesis testing与semiparametric theory的兴趣相连。
- **关键技术**: `restricted mean time lost`, `Wald-type test statistic`, `permutation test`, `multiple testing with dependence structure`, `competing risks cumulative incidence`, `ties without continuity assumption`
- **为什么对您有用**: 直接连接您 primary interest 中的 hypothesis testing 子方向：在竞争风险模型下构造 Wald-type 多重对比检验并利用渐近依赖结构提升功效，属于半参数/非参数检验理论的具体推进。用您 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 M-estimation theory 可以分析其 Wald-type 统计量的渐近性质与结（ties）处理的影响。**中期可做**：若想深入其依赖结构的多重检验功效界，需先在 moderately_familiar 的 semiparametric theory 上长肌肉（特别是多参数 Wald 检验的协方差矩阵估计与投影理论）。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biomtc/ujaf110](https://doi.org/10.1093/biomtc/ujaf110) — Mastering rare event analysis: subsample-size determination in Cox and logistic regressions
- **作者**: Tal Agassi, Nir Keret, Malka Gorfine
- **期刊/来源**: Biometrics
- **机构**: Tel Aviv University
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在 Cox 回归（稀有生存事件）与 logistic 回归（平衡/不平衡数据）设定下，本文解决大规模数据子抽样分析中子样本容量确定（subsample-size determination）问题，目标是控制相对于全样本估计的效率损失。核心机制是提出基于相对效率/方差比的子样本容量选择准则，并为不平衡 logistic 回归提出新的最优子抽样程序（optimal subsampling procedure）。方法依赖 IPW-type subsampling weights 与 asymptotic variance expansion，收敛性质为 subsample estimator 的 n^{-1/2}-CAN 及相对全样本的效率界。实证部分在 UK Biobank（~3.5亿行，稀有 colorectal cancer 事件）与 linked birth-infant death（~2800万行）数据上验证。对您可能有用：若在流行病学/经济大数据中需做 subsample-based 因果估计，此工具可直接提供计算-效率权衡的量化依据。
- **关键技术**: `optimal subsampling`, `subsample-size determination`, `Cox regression rare events`, `logistic regression imbalanced data`, `IPW-type subsampling weights`, `asymptotic relative efficiency`
- **为什么对您有用**: 直接连接 stat_computing（大规模数据数值方法与算法）与 epidemiology（稀有事件队列数据的因果/回归分析）两个子方向。研究者 very_familiar 的 software development 与 high-dimensional asymptotics 可直接攻这篇 paper 的子样本容量公式实现与效率界验证。follow-up 粗判：立即可做——可用 very_familiar 的软件开发能力复现其 subsampling 算法，并在自己关心的 causal inference（如 ATE 的 subsample IPW/TMLE）设定下推广效率-计算权衡框架。

### 2. [10.1093/biomtc/ujaf112](https://doi.org/10.1093/biomtc/ujaf112) — Model robust designs for dose-response models
- **作者**: Belmiro P M Duarte, Anthony C Atkinson, Nuno M C Oliveira
- **期刊/来源**: Biometrics
- **机构**: Institute for Systems Engineering and Computers · University of Coimbra · London School of Economics and Political Science
- **分类**: vol 81 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在剂量-反应实验设计设定下，目标是在模型池（含非线性模型）不确定时寻找近似最优的 model robust design，以最小化模型误设导致的信息损失。本文将 Läuter 提出的三类 model robustness 准则（D₁、D₂、D₃）利用其半定可表示性（semidefinite representability），转化为半定规划（SDP）问题求解。为保证不同模型间信息矩阵的可比性，采用标准化设计（standardized designs）统一量纲。理论贡献是将 robustness 准则的优化问题严格映射到 SDP 框架，从而利用凸优化工具获得全局最优近似设计；实证部分在包含七个候选剂量-反应模型的真实案例上验证了所提 SDP 求解器的有效性。对您可能有用：本文展示了 SDP 在实验设计优化中的数值计算威力，与您 statistical computing 方向的数值方法与软件开发兴趣直接相关。
- **关键技术**: `semidefinite programming (SDP)`, `model robust design`, `Läuter robustness criteria`, `standardized designs`, `locally optimal design`, `dose-response modeling`
- **为什么对您有用**: 本文连接到您 statistical computing（数值方法与软件）的子方向，将实验设计优化问题严格转化为 SDP 并利用凸优化求解器实现，是数值计算在统计设计中应用的典型范例。您武器库中 very_familiar 的 software development 与 high-dimensional asymptotics 可以直接攻这篇 paper 的 SDP 求解实现与信息矩阵渐近分析口子。Follow-up 粗判：立即可做——用您熟悉的 Python/R SDP 库（如 CVXPY）复现并扩展其求解器，或探索高维协变量下 SDP 设计的计算瓶颈。

## 流行病学  *(epidemiology, 8 篇)*

### 1. [10.1093/biomtc/ujaf104](https://doi.org/10.1093/biomtc/ujaf104) · [arXiv](https://arxiv.org/abs/2412.14124) — Semiparametric joint modeling to estimate the treatment effect on a longitudinal surrogate with application to chronic kidney disease trials
- **作者**: Xuan Wang, Jie Zhou, Layla Parast, Tom Greene
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在慢性肾病（CKD）临床试验中，目标是估计处理对纵向替代结局（GFR slope）的效应，但 GFR 测量可能被死亡或肾衰竭等终端事件截断，因此需联合建模纵向轨迹与终端事件过程。本文提出半参数联合模型：纵向结局采用半参数模型（可扩展至非线性轨迹），纵向与终端事件的关联结构非参数化，终端事件用半参数 Cox 模型。基于估计方程方法估计处理对纵向替代的效应，推导了估计量的理论性质（一致性、渐近正态性），并通过模拟与 RENAAL 试验数据验证了方法。对您可能有用：本文提供了流行病学纵向替代结局中处理效应估计的半参数框架，可直接连接到您对 longitudinal causal inference 与 semiparametric theory 的兴趣。
- **关键技术**: `semiparametric joint model`, `Cox proportional hazards model`, `estimating equation method`, `nonparametric association structure`, `longitudinal surrogate endpoint`, `terminal event truncation`
- **为什么对您有用**: (1) 直接连接到 epidemiology 的纵向因果推断设定（terminal event 截断下的 treatment effect on surrogate），以及您 primary interest 中的 longitudinal causal inference 与 semiparametric theory。(2) 您 technical_arsenal 中 moderately_familiar 的 semiparametric theory 与 M-estimation theory 可以直接攻这篇 paper 的估计方程推导与渐近性质部分；若想进一步研究其效率理论，可用 very_familiar 的 estimation theory in causal inference 检查其是否达到 semiparametric efficiency bound。(3) **立即可做**：用 very_familiar 武器（estimation theory / semiparametric theory）即可复现其理论推导并审视效率性质。

### 2. [10.1093/biomtc/ujaf103](https://doi.org/10.1093/biomtc/ujaf103) — Evaluating longitudinal treatment effects for Duchenne muscular dystrophy using dynamically enriched Bayesian small sample, sequential, multiple assignment randomized trial (snSMART)
- **作者**: Sidi Wang, Satrajit Roychoudhury, Kelley M Kidwell
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · Pfizer (United States)
- **分类**: vol 81 · issue 3
- 相关性 7/10 · novelty: `application`
- **摘要**: 针对杜氏肌营养不良症这类渐进性罕见病，本文提出一种动态富集贝叶斯小样本顺序多分配随机试验（snSMART）的分析框架，以纵向评估治疗对疾病进展和功能结局的影响。采用两步稳健荟萃分析方法，利用外部对照数据来增强统计效能并解决参与者稀缺和伦理问题，同时调整基线混杂因素以及外部对照与试验数据的潜在冲突。引入分段模型处理阶段式治疗分配，并整合重要基线协变量以解释患者异质性。通过DMD案例研究展示了该方法在实际罕见病试验中的应用，论证了其提高治疗效果分析稳健性和可靠性的潜力。该工作虽未提出全新统计理论，但巧妙整合了现有贝叶斯方法和外部数据利用策略，为罕见病临床试验设计提供了实用范例，与您在流行病学应用领域的因果推断兴趣高度契合。
- **关键技术**: `Bayesian analysis`, `sequential multiple assignment randomized trial (SMART)`, `external control data`, `meta-analytic approach`, `piecewise model`, `small sample trial`
- **为什么对您有用**: 本文直接连接您的次级兴趣『流行病学』中的应用因果工作与真实数据集（DMD），展示了如何在小样本纵向试验中整合外部对照数据评估治疗效应。从武器库来看，您对『因果推断中的identification theory』为moderately_familiar，本文的piecewise model与dynamically enriched设计可作为一个纵向因果识别的案例来学习——建议先熟悉SMART设计和外部数据融合的识别假设，后续可考虑将更高效的半参数估计（如DR估计量）引入类似框架。属于中期可做：需先在identification theory上加强。

### 3. [10.1093/biomtc/ujaf088](https://doi.org/10.1093/biomtc/ujaf088) — Simple simulation based reconstruction of incidence rates from death data
- **作者**: Simon N Wood
- **期刊/来源**: Biometrics
- **机构**: University of Edinburgh
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 在已知感染至死亡时间间隔分布的设定下，本文研究如何从每日死亡数据回推每日发病率（incidence rate）的估计问题。作者提出一种基于模拟的重建方法，避免拟合简化非线性动力学模型带来的模型设定偏倚，也规避了传统 spline deconvolution 方法的技术晦涩性。核心机制是直接利用 infection-to-death 分布进行前向模拟，将假设的发病率轨迹映射为死亡序列，再与观测死亡数据比对，从而实现轨迹的检验与筛选。该方法仅需最小化分布假设，透明且易于公共卫生从业者快速部署。主要实证结果表明该方法在类 COVID 场景下可快速无争议地提供管理决策输入；对您可能有用的是，此问题本质上是一类离散卷积逆问题，与您熟悉的 inverse problems with random noise 存在直接结构对应。
- **关键技术**: `simulation-based inference`, `deconvolution of infection-to-death distribution`, `incidence reconstruction from death data`, `discrete convolution inverse problem`
- **为什么对您有用**: 本文属于流行病学应用，直接处理发病率回推这一经典 epi 数据分析问题，且方法透明、适合作为入门读物了解 epi 领域对 deconvolution 逆问题的实际需求。您武器库中 inverse problems with random noise 的经验可直接切入该问题的理论深化（如量化死亡数据噪声下的反卷积误差界）。立即可做：用 minimax bounds 工具为该模拟反卷积方法建立有限样本误差界，填补其目前缺乏统计理论保证的空白。

### 4. [10.1093/biomtc/ujaf049](https://doi.org/10.1093/biomtc/ujaf049) — Cumulative incidence function estimation using population-based biobank data
- **作者**: Malka Gorfine, David M Zucker, Shoval Shoham
- **期刊/来源**: Biometrics
- **机构**: Tel Aviv University · Hebrew University of Jerusalem
- **分类**: vol 81 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对人群生物样本库数据（biobank data）中的累积发生率函数（CIF）估计问题，提出了一种新颖的估计量。这类数据包含招募时报告发病年龄的普遍病例（prevalent data）以及初始健康后在随访中发病的个体，存在左截断和右删失。现有方法通常忽略普遍病例或仅将其作为补充，而新方法通过加权或似然框架有效整合了两类信息，从而提高了效率，并允许估计低于招募年龄下限c_L的CIF。方法可能涉及逆概率加权或非参数似然，但摘要未给出具体实现细节。模拟或实证研究表明，新估计量在有限样本下具有更小的均方误差。对您而言，该研究直接对应流行病学中的实际数据挑战（biobank data），您可用非参数统计和逆问题工具理解其估计策略，并思考是否可推广到因果推断中的截断处理。
- **关键技术**: `Cumulative incidence function`, `prevalent cohort`, `left truncation`, `right censoring`, `biobank data`, `efficient estimation`
- **为什么对您有用**: 该论文聚焦流行病学中biobank数据的CIF估计，属于您的次要兴趣流行病学应用。您熟悉的非参数统计和逆问题工具可直接用于分析其估计量的偏差-方差权衡，且可以思考该估计量是否达到半参效率界（需要您moderately_familiar的semiparametric理论）。目前可立即可做：您已有的非参数和逆问题技能足以理解其方法并评估其适用性。

### 5. [10.1093/biomtc/ujaf092](https://doi.org/10.1093/biomtc/ujaf092) · [arXiv](https://arxiv.org/abs/2312.08530) — Using model-assisted calibration methods to improve efficiency of regression analyses using two-phase samples or pooled samples under complex survey designs
- **作者**: Lingxiao Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在复杂抽样设计下的两阶段抽样与池化设计（pooled design）中，目标 estimand 为回归系数，关键假设为两阶段抽样设计的可测性与有限总体框架下的模型辅助校准一致性。本文提出利用第一阶段样本对第二阶段变量的预测值，基于回归模型 score function 将第二阶段样本权重校准至加权第一阶段样本，以提升第二阶段估计量的效率。核心机制为 model-assisted calibration estimator，作者证明了校准权重下估计的一致性，并给出了两阶段/池化设计嵌套于复杂抽样时回归系数的方差估计公式。实证与 NHANES 数据表明，相较于现有校准与插补方法，该方法在效率与鲁棒性上均有提升。对您可能有用：若在流行病学两阶段数据中做因果推断（如 IV / mediation），此校准法可改善第二阶段协量缺失下的估计效率。
- **关键技术**: `model-assisted calibration`, `two-phase sampling design`, `score function calibration`, `finite population inference`, `pooled survey design`, `variance estimation under complex survey`
- **为什么对您有用**: 本文直接连接流行病学因果推断应用（两阶段抽样下协量缺失的效率问题），属于 secondary interest 的 epidemiology 方向；技术上，其 score function 校准思路与您熟悉的 semiparametric efficiency / influence function 体系有自然接口——校准权重本质上是在构造一个近似 efficient influence function 的修正项。follow-up 判断：**中期可做**——若要将此校准框架推广到因果参数（ATE / mediation effect）的 semiparametric efficient estimation，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是有限总体框架下 influence function 的推导与校准辅助变量的选择理论。

### 6. [10.1093/biomtc/ujaf116](https://doi.org/10.1093/biomtc/ujaf116) · [arXiv](https://arxiv.org/abs/2505.15759) — Estimating associations between cumulative exposure and health via generalized distributed lag non-linear models using penalized splines
- **作者**: Tianyi Pan, Hwashin Hyun Shin, Glen McGee, Alex Stringer
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 4/10 · novelty: `minor`
- **摘要**: 在流行病学队列设定下，目标是估计短期空气污染累积暴露对健康的延迟非线性效应，模型为广义 ACE-DLNM（adaptive cumulative exposure distributed lag non-linear model）。现有 ACE-DLNM 仅适用于连续响应且计算不可扩展，本文将其推广至一般响应类型（如 Poisson 计数），并用 penalized splines 替代原有光滑工具以实现数据自适应的累积暴露构造。核心计算策略是 profile likelihood 配合 Laplace approximate marginal likelihood（LAML）与 Newton-type 优化，显著提升了大规模数据集上的计算效率。模拟与应用（加拿大 2001–2018 每日污染与呼吸系统住院计数）表明，该方法比固定暴露的 GAM 推断更稳定且保持解释性。对您而言，这篇论文提供了一个流行病学因果/关联分析的真实数据管道范例，其 penalized spline + LAML 的计算策略对统计计算兴趣有参考价值。
- **关键技术**: `distributed lag non-linear model`, `penalized splines`, `profile likelihood`, `Laplace approximate marginal likelihood`, `Newton-type optimization`, `generalized additive model`
- **为什么对您有用**: 本文属于流行病学应用方向，提供了空气污染-健康关联分析的真实数据集与建模管道，可作为该领域的入门阅读。武器库中的 software development 与 high-dimensional asymptotics 可支撑理解其 penalized spline + LAML 计算策略，但方法学 novelty 仅为 minor（对已有框架的工程推广）。作为 gateway reading 值得花时间浏览数据结构与建模逻辑，但无需深读理论细节。

### 7. [10.1093/biomtc/ujaf119](https://doi.org/10.1093/biomtc/ujaf119) — Joint disease mapping for bivariate count data with residual correlation due to unknown number of common cases
- **作者**: Edouard Chatignoux, Zoé Uhry, Laurent Remontet, Isabelle Albert
- **期刊/来源**: Biometrics
- **机构**: Santé Publique France · Hospices Civils de Lyon · Université Claude Bernard Lyon 1 · Centre National de la Recherche Scientifique · Lyon College · Laboratoire de Biométrie et Biologie Evolutive · AgroParisTech · Université Paris-Saclay 等
- **分类**: vol 81 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在空间流行病学双变量计数数据（如两种疾病区域计数）设定下，目标是估计共享与特异空间变异及未知共患病例数。经典 Poisson 共享成分模型（P-SCM）假设隐变量完全捕获相关性，但当两疾病存在未知数量的共患病例时，计数间产生正的残差相关性，P-SCM 将其误归因于隐变量协方差，导致推断偏倚与预测退化。本文提出基于双变量 Poisson 分布的 BP-SCM，将每个区域计数分解为共患与两种特异计数，对这三个计数分别用 Gaussian Markov Random Field 建模空间结构。模型在贝叶斯框架下通过 Hamiltonian Monte Carlo 进行推断，模拟与真实数据证实 BP-SCM 修正了 P-SCM 的偏倚并提升了预测性能。对您可能有用：该文在流行病学数据中展示了 latent variable misspecification 导致的 identification 偏倚，与因果推断中 unmeasured confounder 的敏感性分析逻辑相通。
- **关键技术**: `Poisson shared component model`, `Bivariate Poisson decomposition`, `Gaussian Markov Random Field`, `Hamiltonian Monte Carlo`, `Bayesian spatial disease mapping`, `residual correlation bias`
- **为什么对您有用**: (1) 连接到流行病学队列/区域计数数据中的因果/关联推断问题，具体是 latent variable misspecification 导致的偏倚，与 proximal CI / sensitivity analysis 中 unmeasured confounder 的识别问题有结构相似性。(2) 用您 very_familiar 的 M-estimation / identification theory 可以分析 P-SCM 的偏倚来源与 BP-SCM 的 identification 条件，这是一个可切入的理论口子。(3) **中期可做**：需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉，将空间隐变量模型的 identification 与因果图中的 latent confounder identification 统一表述，才能做理论推广。

### 8. [10.1093/biomtc/ujaf087](https://doi.org/10.1093/biomtc/ujaf087) — A flexible framework for <i>N</i>-mixture occupancy models: applications to breeding bird surveys
- **作者**: Huu-Dinh Huynh, J Andrew Royle, Wen-Han Hwang
- **期刊/来源**: Biometrics
- **机构**: Industrial University of Ho Chi Minh City · United States Geological Survey · National Tsing Hua University
- **分类**: vol 81 · issue 3
- 相关性 1/10
- **摘要**: 在生态监测的 N-mixture 模型设定下，目标是当封闭假设（closure assumption）被违反时仍能无偏估计物种丰度（abundance）与个体检测概率。本文提出基于 mixed Gamma-Poisson 模型的扩展框架，引入一个"社群参数"表示在整个调查期间始终存在的个体比例，从而将 zero-inflated occupancy 模型（参数=0）和标准 N-mixture 模型（参数=1）统一为特例。估计方法依赖该参数化混合分布的似然推断，模拟与北美及瑞士繁殖鸟类调查数据验证了放松封闭假设后估计的准确性与适应性。对您可能有用：该框架在流行病学重复调查队列中处理个体迁移/失访（类似非封闭）的丰度或患病率估计问题时有直接迁移价值。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `N-mixture model`, `mixed Gamma-Poisson distribution`, `zero-inflated occupancy model`, `closure assumption relaxation`, `community parameter`, `maximum likelihood estimation`
- **为什么对您有用**: (1) 连接到流行病学队列调查中个体失访/迁移导致封闭假设违反的患病率估计问题，与 secondary interest 的 epidemiology 直接相关。(2) 用 technical_arsenal 中 very_familiar 的 M-estimation theory 可以分析该 mixed Gamma-Poisson MLE 的渐近性质（如一致性、效率界），这是本文未深入的理论口子。(3) 中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以将此 parametric framework 推广到半参数 robust 估计并推导 semiparametric efficiency bound。

## 其他  *(other, 10 篇)*

### 1. [10.1093/biomtc/ujaf125](https://doi.org/10.1093/biomtc/ujaf125) · [arXiv](https://arxiv.org/abs/2508.14184) — A Bayesian semiparametric mixture model for clustering zero-inflated microbiome data
- **作者**: Suppapat Korsurat, Matthew D Koslovsky
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对微生物组数据中零膨胀多变量成分计数数据的聚类问题，现有方法通常需要预先指定簇数，且未能充分处理零膨胀带来的复杂性。本文提出一种新颖的贝叶斯半参数混合模型框架，通过狄利克雷过程先验自动学习数据中的簇数，同时进行聚类分配。模型利用半参数混合分布刻画零膨胀成分数据的分布特征，在模拟研究中展示了相比基于距离和模型的替代方法更优的聚类性能，并强调了处理零膨胀的重要性。最后将该模型应用于一项研究肠道微生物组成与腹泻疾病关系的数据集，识别出具有不同微生物组成的亚组。该方法融合了贝叶斯非参数和半参数建模技术，为微生物组聚类提供了灵活的工具。
- **关键技术**: `Bayesian semiparametric mixture model`, `Dirichlet process prior`, `zero-inflated compositional data`, `clustering with unknown number of clusters`, `microbiome data analysis`
- **为什么对您有用**: 本文属于微生物组数据的聚类方法，与您的次要兴趣流行病学中的应用（肠道微生物与疾病）有一定关联。技术层面，贝叶斯半参数混合模型与您熟悉的非参数统计有交集，但核心方法依赖狄利克雷过程而非您熟悉的U统计量或半参数效率理论。从武器库角度看，您可运用非参数统计知识理解其模型设定，但贝叶斯计算（MCMC）不在您的武器库中，因此属于**暂不可做**的领域，除非您有意拓展贝叶斯方向。若仅作为应用案例，阅读全文可了解微生物组数据结构和分析挑战，对流行病学应用有一定参考价值。

### 2. [10.1093/biomtc/ujaf097](https://doi.org/10.1093/biomtc/ujaf097) · [arXiv](https://arxiv.org/abs/2212.09866) — Covariance-on-covariance regression
- **作者**: Yi Zhao, Yize Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 4/10

### 3. [10.1093/biomtc/ujaf100](https://doi.org/10.1093/biomtc/ujaf100) — Regression analysis of interval-censored failure time data with change points and a cured subgroup
- **作者**: Yichen Lou, Mingyue Du, Xinyuan Song
- **期刊/来源**: Biometrics
- **机构**: Chinese University of Hong Kong · Jilin University
- **分类**: vol 81 · issue 3
- 相关性 4/10

### 4. [10.1093/biomtc/ujaf043](https://doi.org/10.1093/biomtc/ujaf043) — Precision generalized phase I-II designs
- **作者**: Saijun Zhao, Peter F Thall, Ying Yuan, Juhee Lee, Pavlos Msaouel, Yong Zang
- **期刊/来源**: Biometrics
- **机构**: Indiana University Health · Indiana University – Purdue University Indianapolis · The University of Texas MD Anderson Cancer Center · University of California, Santa Cruz
- **分类**: vol 81 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 在贝叶斯 I-II 期剂量优化设定下，目标是基于早期疗效、早期毒性及长期治疗失败时间，在患者异质性（亚组）条件下寻找最优剂量。方法采用分段指数分布刻画失败时间，引入亚组特异的剂量-结局效应；通过潜变量自适应聚类相似亚组，实现跨亚组的信息借用与模型简化。决策规则包括剔除不可接受剂量、在可接受剂量间随机化及基于长期随访确定最优剂量。模拟显示 PGen I-II 在正确处理异质性方面优于忽略亚组或独立试验的设计。对您而言，本文属于临床试验设计应用，方法学 novelty 有限，但潜变量自适应聚类借力的思路可泛化参考。
- **关键技术**: `Bayesian dose optimization`, `piecewise exponential failure time`, `latent variable adaptive clustering`, `subgroup-specific dose-outcome model`, `phase I-II trial design`
- **为什么对您有用**: 本文属于临床试验设计应用，与您 primary interests（因果推断、高维/效率理论、U-stat）无直接交集；其潜变量自适应聚类借力的思路与您 moderately_familiar 中的 identification theory 有微弱概念联系，但无技术深度。作为 gateway reading，本文不是好入门读物（大量临床试验专有术语与决策逻辑），武器库无需为此长肌肉，不值得花时间读全文。

### 5. [10.1093/biomtc/ujaf094](https://doi.org/10.1093/biomtc/ujaf094) — Improved prediction and flagging of extreme random effects for non-Gaussian outcomes using weighted methods
- **作者**: John Neuhaus, Charles McCulloch, Ross Boylan
- **期刊/来源**: Biometrics
- **机构**: University of California, San Francisco
- **分类**: vol 81 · issue 3
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对非高斯纵向/聚类数据（二元、计数结果）中极端随机效应的预测与标记问题，将加权预测方法从高斯结果扩展至广义线性混合模型。由于非高斯结果下预测随机效应和标记概率无闭式解，作者提出了自校准(self-calibrated)预测器的理论框架，通过简单标记规则自动控制错误标记率，并开发了数值算法高效计算加权预测器及其性能指标。模拟实验表明，相比现有方法，加权预测器在极端分位点处预测均方误差显著降低，正确标记率大幅提升，同时错误标记率受控。方法以儿童哮喘急诊再住院数据展示实际应用。数值优化与自校准流程与您在estimation theory和M-estimation theory中熟悉的框架有共通点，可作为纵向因果推断中极端效应估计的技术参考。
- **关键技术**: `weighted prediction`, `self-calibrated predictors`, `mixed effects models`, `extreme random effects`, `numerical optimization for non-Gaussian outcomes`
- **为什么对您有用**: 本文涉及非高斯纵向数据中极端随机效应的预测，直接关联您对纵向数据分析(causal inference)和流行病学应用的兴趣。其自校准预测器的数值优化逻辑可借助您非常熟悉的estimation theory in causal inference进行理解，而加权预测的M-估计视角可调用您的M-estimation theory加以深化。中期可做：需先熟悉广义线性混合模型下的M-估计性质，即可尝试将自校准思路迁移至因果推断中的极端效应预测问题。

### 6. [10.1093/biomtc/ujaf115](https://doi.org/10.1093/biomtc/ujaf115) — Bayesian inference for copy number intra-tumoral heterogeneity from single-cell RNA-sequencing data
- **作者**: PuXue Qiao, Chun Fung Kwok, Guoqi Qian, Davis J McCarthy
- **期刊/来源**: Biometrics
- **机构**: St Vincents Institute of Medical Research · The University of Melbourne
- **分类**: vol 81 · issue 3
- 相关性 2/10

### 7. [10.1093/biomtc/ujaf083](https://doi.org/10.1093/biomtc/ujaf083) · [arXiv](https://arxiv.org/abs/2301.03664) — Frequency band analysis of nonstationary multivariate time series
- **作者**: Raanju R Sundararajan, Scott A Bruce
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 3
- 相关性 2/10

### 8. [10.1093/biomtc/ujaf127](https://doi.org/10.1093/biomtc/ujaf127) — Spatially aware adjusted Rand index for evaluating spatial transcriptomics clustering
- **作者**: Yinqiao Yan, Xiangnan Feng, Xiangyu Luo
- **期刊/来源**: Biometrics
- **机构**: Beijing University of Technology · Fudan University · Renmin University of China
- **分类**: vol 81 · issue 3
- 相关性 2/10

### 9. [10.1093/biomtc/ujaf099](https://doi.org/10.1093/biomtc/ujaf099) — Negative binomial mixed effects location-scale models for intensive longitudinal count-type physical activity data provided by wearable devices
- **作者**: Qianheng Ma, Genevieve F Dunton, Donald Hedeker
- **期刊/来源**: Biometrics
- **机构**: Palo Alto University · Stanford University · University of Southern California · Chicago Department of Public Health · University of Chicago
- **分类**: vol 81 · issue 3
- 相关性 2/10

### 10. [10.1093/biomtc/ujaf081](https://doi.org/10.1093/biomtc/ujaf081) — Inference on age-specific fertility in ecology and evolution. Learning from other disciplines and improving the state of the art
- **作者**: Fernando Colchero
- **期刊/来源**: Biometrics
- **机构**: University of Southern Denmark · Max Planck Institute for Evolutionary Anthropology
- **分类**: vol 81 · issue 3
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文系统综述了自1940年代以来人口学、统计学和社会科学中提出的年龄别生育率模型，包括多项式模型和概率密度函数模型，并评估了各类模型在描述生育率不同阶段上的表现。作者指出，生态学和进化生物学领域长期局限于简单最小二乘推断，亟需更复杂的推断方法。为此，作者开发了R包“Bayesian Fertility Trajectory Analysis”，使用贝叶斯层次模型进行模型选择与推断。文章将所提方法应用于狮子和狒狒的聚合数据，并通过模拟实验验证其在个体追踪数据上的表现，表明即使跟踪的个体数较少也能实现合理的模型选择。本文的主要贡献在于方法综述与开源工具推广，而非新颖的理论或方法创新。
- **关键技术**: `Bayesian hierarchical model`, `age-specific fertility model`, `polynomial models`, `probability density function models`, `R package development`, `simulation study for model selection`
- **为什么对您有用**: 本文属于应用性综述，与您的主要研究兴趣（因果推断、高维统计等）直接关联不大，但其R包开发和多层次模型推断可以引起统计计算的兴趣。您的武器库中的“software development”项可用于评估该包的实现质量或扩展其功能；若未来您涉足生态或进化领域的复杂纵向数据建模，本文可作为入口文献，但当前阶段可能暂不可直接利用。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

