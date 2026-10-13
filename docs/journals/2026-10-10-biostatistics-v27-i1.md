# Biostatistics — Vol 27  Issue 1  ·  2026-10-10

- 共 22 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 20 篇（对照 OpenAlex 42 篇）：10.1093/biostatistics/kxag011、10.1093/biostatistics/kxaf052、10.1093/biostatistics/kxag001、10.1093/biostatistics/kxag007、10.1093/biostatistics/kxag006 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》共 22 篇论文，整体上可归纳为三条主线：**因果推断与异质性处理效应**（约 7 篇）、**纵向 / 生存数据的联合建模与动态预测**（约 5 篇）、**高维 / 函数型数据的统计方法与计算**（约 6 篇）。此外，还有少量涉及荟萃分析检验、贝叶斯变量选择、空间点过程等主题的独立工作。因果推断主线在数量和方法多样性上最为突出，覆盖了从分解框架、敏感性分析到贝叶斯非参数和半监督校准等多个角度；纵向与生存主线则集中在多状态模型、治愈率模型和遗传力估计上；高维主线以脑连接、微生物组和转录因子活性估计等应用驱动的方法开发为主。

因果推断主线是本期最值得展开的部分。**分解与异质性**方面，A novel decomposition 将研究间效应差异分解为协变量分布、中介和结局机制，并给出半参数估计量，与中介分析直接相关；Data-adaptive identification 通过随机移位干预和交叉验证 TMLE 识别连续暴露下的效应修饰因子，方法上允许机器学习且保持有效置信区间。**干扰与网络**方面，Sensitivity analysis for contamination 针对 egocentric-network 随机试验中的网络污染，证明 Horvitz–Thompson 估计量有偏并给出偏差校正和敏感性分析框架，是干扰下因果推断的少见工作。**时间序列与个性化**方面，Causal estimands 处理 N-of-1 移动健康数据中的非平稳时间序列，提出时变效应 estimand 并基于 g-formula 和状态空间模型估计；Bayesian nonparametric mixtures 用 Dirichlet Process 混合 categorical DAG 实现个性化因果效应，允许处理效应随潜在聚类变化。**效率与缺失数据**方面，A data integration framework 通过整合多个外部研究提高 Cox 回归效率，对工作模型误设稳健；Semi-supervised calibration 针对结局未金标准验证的情况，建立与增强 IPW 的联系并达到局部半参数有效性；Robust estimation 处理协变量非随机缺失下的最优动态治疗策略，用直接搜索和协变量平衡权重避免 Q 函数误设的累积偏差。这七篇从不同切面推进了因果推断的识别、估计和稳健性，其中分解框架、干扰下的敏感性分析、非平稳时间序列的 estimand 定义，以及半监督校准的半参数效率结果，对因果方向研究者有直接参考价值。

纵向与生存主线中，Data-augmented multistate modeling 利用横断面数据估计慢性病转移强度，采用两步估计法结合外部信息；Risk estimation 提出离散时间联合模型处理多变量纵向与多状态数据，应对区间删失和状态删失；Cure rate joint model 针对 NSCLC 数据建模肿瘤负荷与生存时间，引入变化点刻画疾病进展；Estimating the heritability 在 PLCO 数据上估计 PSA 水平及变化速率的遗传力，提出划分-元分析 AI-REML 和快速 REHE 回归两种高效算法。这四篇共同关注复杂纵向结构下的参数估计与预测，其中多状态模型和治愈率模型在生物医学应用上较为成熟，遗传力估计的计算策略对大规模遗传数据有参考意义。高维主线中，Multivariate functional linear discriminant analysis 结合特征选择处理多元函数型数据，应用于 IBD 分类；SLACC 用稀疏潜在因子分解校正脑连接数据的站点效应；Modeling complex measurement error 针对微生物组实验的测量误差结构提出一致估计量；transfactor 通过概率基因表达去卷积估计转录因子活性；tREX-cap 用分治策略重建全基因组 3D 结构。这些工作以应用驱动的方法开发为主，与因果推断和半参数效率的关联较弱，但高维函数型判别和测量误差建模的思路可迁移至其他领域。

对因果推断 / 半参数效率方向，优先看 A novel decomposition（分解框架与半参数估计）、Semi-supervised calibration（局部半参数有效性）、Data-adaptive identification（TMLE 与数据自适应目标参数）、Sensitivity analysis for contamination（干扰下偏差校正）。对高维统计方向，Multivariate functional linear discriminant analysis 和 SLACC 提供了稀疏正则化与因子分解的实例；对纵向 / 生存方向，Cure rate joint model 和 Risk estimation 的联合建模框架值得关注。

## 因果推断  *(causal_inference, 9 篇)*

### 1. [10.1093/biostatistics/kxag030](https://doi.org/10.1093/biostatistics/kxag030) · [arXiv](https://arxiv.org/abs/2208.05543) — A novel decomposition to explain heterogeneity in observational and randomized studies of causality
- **作者**: Brian Gilbert, Iván Díaz, Kara Rudolph, Nicholas Williams, Tat-Thang Vo
- **期刊/来源**: Biostatistics
- **机构**: New York University · Columbia University · Université Paris-Est Créteil · Paris-Est Sup
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一种新颖的分解框架，用于解释观察性和随机化研究中因果效应的异质性。作者将研究间效应差异正式分解为预处理协变量分布、中介变量和结局机制等来源，并给出各成分的识别条件。在假设下，他们构建了稳健的估计量，可能采用半参数或去偏方法，并给出渐近性质。通过模拟研究验证了方法的有限样本表现，并应用于 Moving to Opportunity (MTO) 数据，展示了实际效用。该工作为多研究环境下的证据合成和政策评估提供了工具。对您而言，其分解思路与中介分析和异质性因果推断直接相关，可借鉴其识别策略到您的纵向或中介研究中。
- **关键技术**: `causal decomposition`, `between-study heterogeneity`, `mediation analysis`, `robust estimation`, `semiparametric efficiency`
- **为什么对您有用**: 直接关联您的因果推断兴趣，特别是中介分析和异质性研究。该分解框架可视为中介分析的一种扩展，您可运用 very_familiar 的估计理论（如 influence function）来审视其估计量的效率性质。中期可做：若想深入其半参数效率界，需在 moderately_familiar 的半参数理论上加强。

### 2. [10.1093/biostatistics/kxag031](https://doi.org/10.1093/biostatistics/kxag031) · [arXiv](https://arxiv.org/abs/2602.05553) — Sensitivity analysis for contamination in egocentric-network randomized trials with interference
- **作者**: Bar Weinstein, Daniel Nevo
- **期刊/来源**: Biostatistics
- **机构**: Tel Aviv University
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究 egocentric-network 随机试验（ENRTs）中因网络污染导致的因果估计偏差问题。在存在干扰（interference）且无法观测完整社会中心网络时，ENRTs 通过抽样 ego 及其 alters 来估计直接和间接效应，但设计上 disjoint 的观测网络可能掩盖潜在网络中的跨 ego 边，造成污染。作者在基于设计的框架下证明，存在污染时 Horvitz–Thompson 估计量对直接和间接效应均有偏。为纠正偏差，他们推导了偏差校正估计量，并提出基于敏感性参数（缺失边的概率或期望数）的敏感性分析框架，涵盖网格敏感性分析和概率偏差分析两种实现方式。方法应用于 HIV Prevention Trials Network 037 研究，发现忽略污染会低估间接效应并高估直接效应。
- **关键技术**: `Horvitz–Thompson estimator`, `bias correction`, `sensitivity analysis`, `probabilistic bias analysis`, `design-based inference`
- **为什么对您有用**: 本文属于因果推断中干扰（interference）与敏感性分析的交汇点，直接对应您 primary interest 中的 causal inference 子方向。您可以用 very_familiar 的 estimation theory in causal inference 来审视其偏差校正估计量的有限样本性质，或考虑用 moderately_familiar 的 identification theory 来扩展其敏感性参数的解释。中期可做：结合您对 higher-order U-statistics 的熟悉，分析其估计量的高阶偏差项，但需先熟悉网络抽样设计的具体细节。

### 3. [10.1093/biostatistics/kxag014](https://doi.org/10.1093/biostatistics/kxag014) — Causal estimands and identification of time-varying effects in nonstationary time series from N-of-1 mobile device data
- **作者**: Xiaoxuan Cai, Li Zeng, Charlotte Fowler, Lisa Dixon, Dost Ongur, Justin T Baker et al.
- **期刊/来源**: Biostatistics
- **机构**: The Ohio State University · Yale University · Worcester Polytechnic Institute · Columbia University · Harvard University · McLean Hospital
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对 N-of-1 移动健康研究中的非平稳多元时间序列，提出新的因果 estimand 来刻画时变暴露对结局的短期和长期动态效应，突破了现有方法仅关注同期、时间平均或人群平均效应且假设平稳性的局限。作者在潜在结果框架下给出识别假设，并基于 g-formula 提出估计量，该估计量通过状态空间模型框架灵活处理暴露-结局和结局-协变量之间的反馈，从而适应非平稳性。方法应用于一项双相情感障碍患者多年智能手机观察性研究，估计手机沟通对情绪的个体化动态效应，发现效应随时间及个体间存在显著异质性。此外，作者提出基于模拟的策略用于生成短期、动态、个性化的治疗推荐，并开发了新的 positivity 诊断图以验证时间序列因果推断的有效性。对您而言，该文将纵向因果推断与个性化医疗结合，其状态空间 g-formula 和 positivity 诊断思路可能对您的 longitudinal causal inference 和 sensitivity analysis 子方向有直接参考价值。
- **关键技术**: `g-formula`, `state space model`, `N-of-1 causal estimands`, `positivity diagnostics`, `simulation-based treatment recommendation`
- **为什么对您有用**: 该文直接关联您的 primary interest 中 longitudinal causal inference 和 identification theory 子方向，尤其针对非平稳时间序列的时变效应识别与估计。您可用 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory 来审视其识别假设的严谨性，并考虑将状态空间 g-formula 与您的 HOIF 工具结合以提升估计效率。中期可做：需在 semiparametric theory 上进一步巩固以推导其估计量的渐近性质。

### 4. [10.1093/biostatistics/kxag020](https://doi.org/10.1093/biostatistics/kxag020) · [arXiv](https://arxiv.org/abs/2406.10792) — Data-adaptive identification of effect modifiers through stochastic shift interventions and cross-validated targeted learning
- **作者**: David McCoy, Wenxin Zhang, Alan Hubbard, Mark van der Laan, Alejandro Schuler
- **期刊/来源**: Biostatistics
- **机构**: University of California, Berkeley
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对流行病学中连续暴露下的异质性处理效应估计问题，提出一种数据自适应的效应修饰因子识别方法。传统方法多限于二元暴露且缺乏可解释性，本文通过随机移位干预（stochastic shift intervention）定义目标参数，并采用交叉验证的TMLE（cross-validated TMLE）进行估计，同时结合数据自适应的目标参数选择策略，以识别暴露减少干预下影响最大的亚群。该方法假设宽松，允许整合机器学习，同时仍能提供有效的置信区间。模拟研究和NHANES数据应用（持久性有机污染物与白细胞端粒长度）验证了方法的稳健性，发现年龄是显著的效应修饰因子，且年轻人群对PCB暴露减少的反应更敏感。作者提供了开源R包EffectXshift，便于实际应用。该方法与您的因果推断（尤其纵向和异质性处理效应）及效率理论（TMLE、交叉验证）兴趣高度相关。
- **关键技术**: `stochastic shift interventions`, `cross-validated TMLE`, `data-adaptive target parameter`, `effect modification`, `continuous exposure`, `open-source software`
- **为什么对您有用**: 本文直接关联您的因果推断子方向（异质性处理效应、连续暴露的干预效应），且使用您熟悉的TMLE和交叉验证框架。您可以用very_familiar的软件开发和估计理论来复现或扩展其方法，例如将数据自适应目标参数策略与您的高阶U统计量计算结合，分析其计算复杂度。中期可做：若想深入理论性质，需在semiparametric theory（moderately_familiar）上加强，以推导其影响函数和效率界。总体而言，这是一篇方法学与实证结合紧密的论文，值得展开读。

### 5. [10.1093/biostatistics/kxag026](https://doi.org/10.1093/biostatistics/kxag026) — Bayesian nonparametric mixtures of categorical directed graphs for personalized causal inference
- **作者**: Federico Castelletti, Laura Ferrini
- **期刊/来源**: Biostatistics
- **机构**: Università Cattolica del Sacro Cuore · University of Milano-Bicocca
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在贝叶斯非参数框架下，针对分类变量构成的观测数据，提出用 Dirichlet Process 混合的 categorical DAG 模型进行个性化因果推断。传统 DAG 方法假设总体同质，对所有个体赋予单一因果效应，这在临床中常不现实；本文通过潜在聚类结构允许处理效应随个体变化。方法上，对每个聚类赋予一个 categorical DAG，并利用 Dirichlet Process 先验实现无限混合，开发了相应的 MCMC 算法进行后验推断。模拟研究评估了方法的性能，并应用于 HER2+ 乳腺癌患者接受可能引起心脏毒副作用的治疗数据。结果表明，忽略总体异质性的方法可能产生偏倚，过高或过低估计患者的心脏毒性风险。对您而言，该文将贝叶斯非参数聚类与因果 DAG 结合，为纵向或异质性人群中的因果效应估计提供了新视角，与您的 causal inference 和 Bayesian 方法兴趣相关。
- **关键技术**: `Dirichlet Process mixture`, `categorical DAG`, `Bayesian nonparametrics`, `MCMC`, `personalized causal inference`
- **为什么对您有用**: 该文直接关联您的因果推断兴趣，特别是异质性处理效应的建模，且使用贝叶斯非参数方法，与您熟悉的估计理论形成互补。从技术武器库看，您可用 very_familiar 的软件开发和 M-estimation 理论来复现或扩展其 MCMC 算法，或评估其聚类结构的识别性；中期可做的是在 moderately_familiar 的 semiparametric theory 上加强，以比较其贝叶斯方法与半参数方法的效率。总体而言，这是一篇值得展开读的应用方法论文，但 novelty 主要在于应用场景而非全新理论。

### 6. [10.1093/biostatistics/kxag035](https://doi.org/10.1093/biostatistics/kxag035) — A data integration framework to improve the efficiency of survival analysis by leveraging multiple external studies with multifaceted heterogeneity
- **作者**: Daxuan Deng, Chixiang Chen, Lijun Zhang, Vernon M Chinchilli, Ming Wang
- **期刊/来源**: Biostatistics
- **机构**: Penn State Milton S. Hershey Medical Center · University of Maryland, Baltimore · Case Western Reserve University
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出一个数据整合框架，旨在通过利用多个外部研究来提高内部Cox回归系数估计的效率，同时应对外部数据在数据形式、分布和协变量可用性上的多方面异质性。方法通过变换、工作模型、惩罚方法和自适应加权来选择同质成分，实现稳健整合。所得估计量具有相合性和渐近正态性，且比仅用内部数据的估计更有效，并对工作模型误设和数据异质性稳健。模拟研究验证了框架的良好性质。应用于宗教秩序研究和拉什记忆与衰老项目中黑人个体的痴呆风险研究，整合了ADNI和NACC等外部队列，识别出关键风险因素并提高了效率。该方法对生存分析中的因果推断和效率提升有直接贡献。
- **关键技术**: `data integration`, `Cox regression`, `working models`, `penalized estimation`, `adaptive weighting`
- **为什么对您有用**: 该论文直接关联因果推断中的效率提升和纵向生存分析，且其整合外部数据的框架与您的proximal CI和semiparametric效率理论兴趣相关。您可以用very_familiar的估计理论来评估其效率增益的紧性，或用moderately_familiar的semiparametric理论来检验其影响函数。中期可做：需在semiparametric theory上进一步熟悉以深入分析。

### 7. [10.1093/biostatistics/kxag023](https://doi.org/10.1093/biostatistics/kxag023) — Semi-supervised calibration of inferred outcomes for estimating average treatment effects with validated outcomes
- **作者**: Daniel A Xu, Katherine P Liao, Tianxi Cai, David Cheng
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Brigham and Women's Hospital · Massachusetts General Hospital
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对电子健康记录数据中结局变量未经金标准验证的问题，提出一种半监督校准方法，以在仅部分样本具有验证结局时一致估计平均处理效应。作者将问题类比为纵向研究中单调缺失下的均值估计，并建立与增强逆概率加权估计量的联系。所提估计量具有多重稳健性和局部半参数有效性，且在极端倾向得分下通过隐式增广项的归一化实现有限样本效率提升。模拟研究验证了有限样本性能，并应用于类风湿关节炎患者两种抗TNF疗法的比较效果分析。该方法为利用未验证结局进行因果推断提供了新思路，与您的因果推断和半参数效率理论兴趣高度相关。
- **关键技术**: `semi-supervised calibration`, `augmented inverse probability weighting`, `multiple robustness`, `local semiparametric efficiency`, `monotone missingness analogy`
- **为什么对您有用**: 本文直接关联您的因果推断（特别是利用代理或推断结局的估计）和半参数效率理论（多重稳健性、局部有效性）兴趣。您可以用非常熟悉的估计理论（如DR估计、IF推导）来审视其校准机制，并可能用您的中阶U统计量工具分析其有限样本性质。中期可做：若想深入其与纵向缺失的联系，需在识别理论上稍加扩展。

### 8. [10.1093/biostatistics/kxag041](https://doi.org/10.1093/biostatistics/kxag041) · [arXiv](https://arxiv.org/abs/2506.22892) — Robust estimation of optimal dynamic treatment regimes with nonignorable missing covariates
- **作者**: Jian Sun, Bo Fu, Li Su
- **期刊/来源**: Biostatistics
- **机构**: Fudan University · MRC Biostatistics Unit
- **分类**: vol 27 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究观测数据中协变量非随机缺失（nonignorable missing）情形下最优动态治疗策略（DTRs）的稳健估计问题。现有加权Q-learning方法依赖参数化Q函数模型，在多阶段设定中，Q函数误设会通过伪结局向后传播并累积偏差，同时缺失倾向得分估计的偏差也会间接影响结果。作者提出基于直接搜索（direct-search）的稳健估计器：单阶段规则下，利用协变量平衡权重（covariate balancing weights）并辅以非参数估计的Q函数，在future-independent缺失假设下构造治疗规则价值的稳健估计；多阶段DTR则通过逆缺失倾向加权整合伪结局，其中缺失倾向用非反应工具变量（nonresponse instrumental variables）进行半参数建模。模拟研究表明，所提估计器对模型误设和无效工具变量污染比加权Q-learning更稳健。电子病历数据应用显示，利用非随机缺失的血流动力学变量可改进脓毒症患者早期液体复苏策略的估计。对您而言，本文结合了proximal causal inference中的工具变量思想与DTR的纵向设定，且其稳健估计框架与您的semiparametric theory和causal inference兴趣直接相关。
- **关键技术**: `direct-search estimation`, `covariate balancing weights`, `nonparametric Q-function estimation`, `inverse missingness propensity weighting`, `nonresponse instrumental variables`, `semiparametric propensity modeling`
- **为什么对您有用**: 本文直接关联您的causal inference子方向（DTR、非随机缺失、工具变量），且其半参数稳健估计与您的semiparametric theory和efficiency theory兴趣点契合。您可用very_familiar的nonparametric statistics和minimax bounds工具来评估其估计器的理论性质（如收敛速率和效率界），或探索其与proximal CI框架的联系。中期可做：若想深入其半参数效率分析，需在semiparametric theory（moderately_familiar）上加强。

### 9. [10.1093/biostatistics/kxag025](https://doi.org/10.1093/biostatistics/kxag025) · [arXiv](https://arxiv.org/abs/2507.18773) — Cure rate joint model for time-to-event data and longitudinal tumor burden with potential change points
- **作者**: Yixiang Qu, Ethan M Alt, Weibin Zhong, Jeen Liu, Chenguang Wang, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill · Regeneron (United States)
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对非小细胞肺癌（NSCLC）临床试验中的纵向肿瘤负荷（TB）与生存时间数据，提出了一种治愈率联合模型（cure-rate joint model），旨在刻画治疗对TB轨迹和事件时间的联合影响。模型将患者分为存在变化点（change-point）和不存在变化点的轨迹组，其中变化点代表疾病进展的开始，且必须发生在事件时间之前，这构成了一个可解释的生物学约束。对于变化点组，方法利用事件时间信息灵活估计个体化的变化点，从而将纵向过程与生存结局联系起来。参数估计采用蒙特卡洛期望最大化（MCEM）算法，能够处理复杂的删失机制。模拟研究表明模型能恢复多样的疾病进展模式，并给出稳健的边缘TB结局估计。应用于一项III期NSCLC试验（cemiplimab对比标准治疗）时，结果显示治疗组肿瘤再生长延迟且TB持续较低，展示了临床实用性。
- **关键技术**: `cure-rate joint model`, `change-point estimation`, `Monte Carlo Expectation-Maximization (MCEM)`, `longitudinal-survival joint modeling`, `time-to-event data`
- **为什么对您有用**: 该论文属于纵向因果推断与生存分析的交叉领域，直接关联您的主要兴趣中的'causal inference (longitudinal)'和'epidemiology (applied causal work)'。其联合建模框架和变化点识别方法可迁移至其他纵向生物标志物与事件结局的研究。从武器库看，您对'identification theory in causal inference'和'nonparametric statistics'的熟悉程度足以理解其模型设定，但MCEM算法和变化点推断并非您当前最熟悉的工具，属于'中期可做'——需在'statistical computing'或'M-estimation'上稍作拓展。作为应用型论文，其方法学新颖性中等，但真实数据集和分析流程具有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxag040](https://doi.org/10.1093/biostatistics/kxag040) · [arXiv](https://arxiv.org/abs/2505.02153) — A monotone single-index modal regression powered by deep neural networks for non-Gaussian periodontal data
- **作者**: Qingyang Liu, Shijie Wang, Ray Bai, Dipankar Bandyopadhyay
- **期刊/来源**: Biostatistics
- **机构**: Wake Forest University · George Mason University · Virginia Commonwealth University
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对牙周病研究中常见的偏态、重尾且非线性的临床数据（如牙周袋深度 PD），提出一种稳健的单指标众数回归框架。模型采用灵活的 2-piece scale Student-t 误差分布，推广了正态和 2-piece scale 正态分布，并利用带单调性约束的神经网络估计未知的单指标函数，同时保留参数化指标系数的临床可解释性。理论方面建立了模型可识别性和通用逼近定理。估计采用基于众数的稳健方法，对异常值具有抵抗力。通过模拟研究和明尼苏达 HealthPartners 电子健康记录数据的应用验证了方法的性能，并提供了 R 包 DNNSIM。对您而言，该工作将半参数单指标模型与深度网络结合，并处理非高斯误差，可作为非参数/半参数理论中形状约束估计的一个具体案例，但其方法学新颖性主要在于应用与实现，而非全新的理论突破。
- **关键技术**: `single-index model`, `modal regression`, `monotone neural network`, `2-piece scale Student-t distribution`, `universal approximation`
- **为什么对您有用**: 本文属于非参数/半参数理论方向，具体涉及单指标模型与形状约束估计，与您的 primary interest 中 semiparametric & nonparametric theory 直接相关。您可以用 very_familiar 的 minimax bounds 工具来审视其单调神经网络估计量的收敛速率是否最优，或探讨其与经典单指标估计的效率差异。该文为应用导向，方法学 novelty 有限，但作为流行病学（牙周病）数据中的半参数建模案例，值得作为入门阅读。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxag033](https://doi.org/10.1093/biostatistics/kxag033) — Flexible nonparametric assessment of time-lag bias in meta-analysis
- **作者**: Xing Xing, Zhiyuan Yu, Mengli Xiao, Jiayi Tong, Lifeng Lin
- **期刊/来源**: Biostatistics
- **机构**: University of Arizona · Johns Hopkins University · Citigroup · University of Colorado Anschutz
- **分类**: vol 27 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对荟萃分析中的时间滞后偏倚（time-lag bias）提出一类灵活的非参数检验统计量。该偏倚源于效应显著或较大的研究更早发表，导致早期汇总估计被高估。现有诊断方法（累积荟萃分析、效应量对发表时间的元回归）易受重复检验膨胀影响，且对非线性时间趋势功效不足。作者构造标准化成对差异的统计量族，每个统计量强调不同时间对比幅度，并通过置换检验自适应组合这些证据。该混合检验在发表顺序可交换的零假设下控制第一类错误，并对线性趋势、早期异常值、振荡等多样时间模式敏感。模拟（9种场景，含异质性）显示混合检验在非线性趋势下维持名义错误率并优于线性元回归；两个临床荟萃分析实例中，该方法检测到标准回归遗漏的显著时间滞后模式。对您而言，该文将非参数检验与置换方法用于生物统计应用，其自适应组合思路可迁移至您假设检验方向的检验统计量构造问题。
- **关键技术**: `permutation test`, `adaptive combination`, `nonparametric statistics`, `meta-analysis`, `time-lag bias`
- **为什么对您有用**: 该文属于假设检验方向的应用型工作，与您的主要兴趣（数学统计与假设检验）直接相关。其核心是构造对多种时间模式敏感的非参数检验统计量族并通过置换检验控制错误率，您可用非常熟悉的非参数统计与置换检验工具快速理解并评估其方法。中期可考虑将自适应组合思想与您 moderately_familiar 的 HOIF 或 U-统计量理论结合，发展更高效的检验。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biostatistics/kxag022](https://doi.org/10.1093/biostatistics/kxag022) — Data-augmented multistate modeling for chronic disease processes using cross-sectional studies: application to HPV and cervical precancer
- **作者**: Fangya Mao, Nicole G Campos, Li C Cheung
- **期刊/来源**: Biostatistics
- **机构**: Division of Cancer Epidemiology and Genetics · Harvard University
- **分类**: vol 27 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对慢性疾病过程（以HPV感染和宫颈癌前病变为例）提出一种数据增强的多状态模型，目标是在仅有横断面数据时估计人群层面的疾病自然史转移强度。作者采用半马尔可夫多状态模型刻画HPV感染与未感染状态间的反复转换以及癌前病变进展。为利用横断面数据，提出两步估计法：先从外部数据在可转移性假设下估计生物学驱动的转移强度，再将这些估计值纳入近似似然，以推断受当地流行病学和行为因素影响的人群特异转移强度。模拟研究和两个人群的应用验证了方法的性能和实用性。该方法为资源有限环境下利用横断面数据估计疾病自然史提供了可行途径，对您而言，其两步估计框架与因果推断中利用外部信息进行校准的思路有相通之处，可作为流行病学应用中的方法参考。
- **关键技术**: `semi-Markov multistate model`, `approximate likelihood`, `two-step estimation`, `cross-sectional data`, `transferability assumption`
- **为什么对您有用**: 本文属于流行病学应用，使用多状态模型和两步估计法，与您的流行病学应用兴趣相关；其利用外部信息校准转移强度的思路可联系到因果推断中的传输性假设，但方法学新颖性一般，属于应用型工作。武器库中的估计理论可支撑理解其似然构造，但无需深入方法学跟进，可作为入门读物了解横断面数据建模的实践。

### 2. [10.1093/biostatistics/kxag018](https://doi.org/10.1093/biostatistics/kxag018) — Risk estimation and dynamic prediction using discrete-time joint models for longitudinal and multistate data with interval and state censoring
- **作者**: Lu You, Falastin Salami, Carina Törn, Åke Lernmark, Kendra Vehik, Xiang Liu et al.
- **期刊/来源**: Biostatistics
- **机构**: University of South Florida · Lund University · University of Florida
- **分类**: vol 27 · issue 1
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出一个离散时间联合模型，用于多变量纵向数据与多状态数据的联合建模，并以 TEDDY 研究中自身抗体的发展为应用背景。模型基于时变与非时变风险因素量化状态转移风险，并采用动态预测方法基于历史数据预测未来状态占用概率。方法能够处理纵向数据的测量误差以及多状态数据中的区间删失和缺失信息。文中讨论了预测性能指标及其估计，并通过模拟研究评估所提方法。最后详细展示了该方法在 TEDDY 数据上的应用，包括缺失信息处理和动态预测算法。对您而言，该文是流行病学队列研究中纵向与多状态数据联合建模的典型应用，其动态预测框架和缺失数据处理思路可能对您的因果推断（如纵向设定）有参考价值。
- **关键技术**: `joint modeling`, `discrete-time multistate model`, `dynamic prediction`, `interval censoring`, `measurement error`
- **为什么对您有用**: 本文属于流行病学应用，涉及纵向数据与多状态数据，与您的流行病学应用兴趣直接相关。作为入门读物，它清晰展示了实际队列研究中数据复杂性（区间删失、缺失）的处理流程，但方法学创新有限。您的武器库（如纵向因果推断、M估计）足以理解并评估其方法，但若要深入改进动态预测或处理更复杂的删失机制，可能需要补充生存分析或状态空间模型的专门知识。总体而言，值得花时间读全文以了解应用场景，但不必期待方法论上的重大突破。

### 3. [10.1093/biostatistics/kxag015](https://doi.org/10.1093/biostatistics/kxag015) · [arXiv](https://arxiv.org/abs/2505.04773) — Estimating the heritability of longitudinal rate-of-change: genetic insights into PSA velocity in prostate cancer-free individuals
- **作者**: Pei Zhang, Xiaoyu Wang, Jianxin Shi, Paul S Albert
- **期刊/来源**: Biostatistics
- **机构**: Division of Cancer Epidemiology and Genetics · University of Maryland, College Park
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文在 PLCO 癌症筛查试验的纵向 PSA 数据（15,260 名无癌男性，平均每人 5.34 次测量）与全基因组基因型数据下，估计 PSA 水平（年龄 54 岁）及其变化速率（PSA velocity）的遗传力。作者构建了一个混合模型，将基线水平与速率的遗传效应联合建模，目标估计量为两个遗传力参数。为应对大数据规模，提出了两种高效计算方法：基于平均信息 REML（AI-REML）的划分-元分析策略，以及快速限制性 Haseman–Elston（REHE）回归方法。模拟显示两种方法均无偏，且 AI-REML 在速率遗传力估计上变异性更小。应用于 PLCO 数据，基线 PSA 遗传力估计为 0.32（s.e.=0.07），PSA 速率遗传力为 0.45（s.e.=0.18）。该结果提示 PSA 动态变化具有显著遗传成分，为后续全基因组关联研究提供依据。对您而言，本文是流行病学纵向数据中遗传力估计的应用实例，其混合模型与计算策略（AI-REML、REHE）可视为统计方法在真实队列中的应用参考。
- **关键技术**: `linear mixed model`, `average information REML`, `Haseman-Elston regression`, `partitioning and meta-analysis`, `heritability estimation`
- **为什么对您有用**: 本文属于流行病学应用，涉及纵向数据的因果/关联推断，与您的 secondary interest 流行病学应用方向相关。作为 gateway reading，它展示了大型队列中遗传力估计的统计建模与计算权衡，但方法学 novelty 有限，主要是现有方法的组合与扩展。您的武器库（混合模型、M-估计）足以理解其方法，但若想深入遗传力估计的统计理论，可能需要补充数量遗传学背景。值得花时间读全文以了解 PLCO 数据结构和分析流程，但不必期待新方法突破。

## 其他  *(other, 8 篇)*

### 1. [10.1093/biostatistics/kxag027](https://doi.org/10.1093/biostatistics/kxag027) — Multivariate functional linear discriminant analysis with feature selection: an application to inflammatory bowel disease classification
- **作者**: Limeng Liu, Guannan Wang, Sandra E Safo
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota · William & Mary
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种针对多元函数型数据的线性判别分析方法，用于区分克罗恩病、溃疡性结肠炎和非IBD三类人群，并识别随时间变化的判别性微生物特征。方法通过最大化类间分离度来构造判别函数，并施加稀疏惩罚以实现特征选择，可同时处理高维预测变量、稀疏时间点和多分类结局。在Integrative Human Microbiome Project的IBD数据上，方法识别出与黏蛋白降解、氨基酸代谢和肽聚糖识别相关的微生物通路，并强调了多种维生素B缺乏在IBD中的作用。该方法属于函数型数据分析和判别分析的结合，与您的主要兴趣（因果推断、高维统计、半参数理论等）关联较弱，但作为生物统计应用，其处理高维函数型数据的思路可能对您在高维统计或统计计算方面的兴趣有一定参考价值。
- **关键技术**: `functional data analysis`, `linear discriminant analysis`, `sparse penalty`, `multivariate functional data`, `feature selection`
- **为什么对您有用**: 本文属于函数型数据判别分析的应用型工作，与您的主要兴趣（因果推断、高维统计、半参数理论等）关联较弱。但作为生物统计应用，其处理高维函数型数据的思路可能对您在高维统计或统计计算方面的兴趣有一定参考价值。

### 2. [10.1093/biostatistics/kxag039](https://doi.org/10.1093/biostatistics/kxag039) · [arXiv](https://arxiv.org/abs/2601.07446) — Penalized likelihood optimization for adaptive neighborhood clustering in time-to-event data with group-level heterogeneity
- **作者**: Alessandra Ragni, Lara Cavinato, Francesca Ieva
- **期刊/来源**: Biostatistics
- **机构**: Politecnico di Milano · Human Technopole
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种联合患者聚类与共享脆弱项生存建模的惩罚似然框架，用于在存在组级异质性（如医院）的生存数据中识别具有相似事件风险动态的潜在患者亚组。方法通过修改的谱聚类自适应学习患者间相似性矩阵，使聚类直接基于估计的风险剖面，同时考虑组隶属关系。模拟研究显示该方法能恢复潜在聚类并正确估计风险参数。应用于2020-2021年意大利伦巴第地区COVID-19住院心衰患者队列，识别出具有不同风险特征的临床相关亚组，并强调呼吸合并症和医院水平变异对死亡结局的作用。该方法为分层数据中的风险分层提供了灵活且可解释的工具，并附有软件实现。
- **关键技术**: `penalized likelihood`, `shared frailty survival model`, `spectral clustering`, `adaptive similarity matrix`, `hierarchical data`
- **为什么对您有用**: 本文属于应用统计方法学，涉及生存分析、聚类和组级异质性，与您的主要兴趣（如因果推断、半参数理论）关联较弱，但可作为流行病学应用（COVID-19队列）的入门读物，展示如何在分层数据中结合聚类与生存模型。您的武器库（如M估计、非参数方法）足以理解其方法，但核心创新在于算法实现而非理论深度，因此作为gateway reading价值中等，值得快速浏览以了解应用场景。

### 3. [10.1093/biostatistics/kxag024](https://doi.org/10.1093/biostatistics/kxag024) · [arXiv](https://arxiv.org/abs/2509.06779) — A nutritionally informed model for Bayesian variable selection with metabolite response variables
- **作者**: Dylan Clark-Boucher, Brent A Coull, Harrison T Reeder, Fenglei Wang, Qi Sun, Jacqueline R Starr et al.
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Vertex Pharmaceuticals (United States) · Massachusetts General Hospital · Brigham and Women's Hospital
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯变量选择方法，用于在营养流行病学中识别与血液代谢物相关的食物摄入变量。数据来自两个医疗专业人员队列，包含244个代谢物，具有偏态、左截断和结构缺失等复杂特征。方法基于偏态正态截断混合模型，并利用马尔可夫随机场先验整合食物项之间的先验营养关系，以在高维下进行推断。与现有低维方法相比，该方法能同时处理数据复杂性和变量间结构，并在队列数据中发现了若干已知及潜在的新的代谢物-饮食关联。方法已实现为R包multimetab。对您而言，本文展示了在高维贝叶斯变量选择中整合先验结构信息的一种实用方案，但其方法论核心与您的主要兴趣（如因果推断、半参数效率理论）关联较弱。
- **关键技术**: `Bayesian variable selection`, `skew-normal censored mixture model`, `Markov random field prior`, `high-dimensional inference`, `R package multimetab`
- **为什么对您有用**: 本文属于应用型方法论文，主题为高维贝叶斯变量选择，与您的主要兴趣（因果推断、半参数理论、U统计量）无直接交集。但可作为流行病学应用（次级兴趣）的参考，展示如何处理复杂数据结构和先验信息。武器库中的非参数统计和软件工程能力足以理解其方法，但无需深入。

### 4. [10.1093/biostatistics/kxag034](https://doi.org/10.1093/biostatistics/kxag034) · [arXiv](https://arxiv.org/abs/2601.09525) — Sparse covariate-driven factorization of high-dimensional brain connectivity with application to site effect correction
- **作者**: Rongqian Zhang, Elena Tuzhilina, Jun Young Park
- **期刊/来源**: Biostatistics
- **机构**: University of California, San Francisco · University of Toronto
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出 SLACC（Sparse LAtent Covariate-driven Connectome）分解方法，用于高维脑连接数据中的站点效应校正。模型将协变量效应显式参数化到潜在主题得分中，对应稀疏秩-1潜在模式，从而识别网络内外的局部站点驱动变异。估计采用带惩罚的 EM 算法，并用 BIC 指导优化。模拟实验验证了参数恢复和连接模式识别的稳健性；在 ABIDE 数据集上展示了降低站点效应的效果。该方法属于多变量统计与矩阵分解在神经影像中的应用，与您的主要兴趣（如高维统计、因果推断）关联较弱，但可作为统计计算与应用的参考。
- **关键技术**: `penalized EM algorithm`, `sparse matrix factorization`, `latent variable model`, `BIC model selection`
- **为什么对您有用**: 本文属于统计计算与高维数据应用，与您的统计计算兴趣有一定关联，但并非核心方向。作为入门读物，其方法（稀疏分解+EM）在您的武器库中已有基础，可快速理解；但若追求方法学深度，价值有限。

### 5. [10.1093/biostatistics/kxag036](https://doi.org/10.1093/biostatistics/kxag036) · [arXiv](https://arxiv.org/abs/2204.12733) — Modeling complex measurement error in microbiome experiments to estimate relative abundances and detection effects
- **作者**: David S Clausen, Amy D Willis
- **期刊/来源**: Biostatistics
- **机构**: University of Washington · Cancer Research And Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对微生物组实验中测量误差的复杂结构，提出一种估计物种相对丰度、检测效应和跨样本污染的方法。作者首先指出直觉式的相对丰度估计量存在偏倚，然后通过特定的实验设计（如添加已知组成的对照样本）实现模型参数的可识别性。方法上，他们构造了一致估计量，并基于稳健的推断程序（对工作似然的误设具有鲁棒性）提供渐近有效的置信区间。值得注意的是，该过程能够估计单纯形边界上的相对丰度，这在微生物组数据中很常见（如物种缺失）。作者通过模拟和真实数据展示了方法在比较实验方案、去除污染和估计物种可检测性方面的实用性。
- **关键技术**: `robust inference`, `misspecified likelihood`, `boundary estimation`, `identifiability via experimental design`, `consistent estimation`
- **为什么对您有用**: 本文属于应用统计方法，涉及测量误差建模和稳健推断，与您的主要兴趣（如半参数理论、假设检验）有间接联系，但并非直接推进您的研究方向。作为流行病学或应用因果推断的潜在工具，它可能对处理测量误差问题有启发，但方法本身并非您武器库中的核心。因此，本文作为入门读物或方法参考有一定价值，但不太可能成为您深入研究的对象。

### 6. [10.1093/biostatistics/kxag021](https://doi.org/10.1093/biostatistics/kxag021) — A divide and conquer strategy for recapitulating whole genome 3D structure using Hi-C data
- **作者**: Jincheol Park, Meng Wang, Emerson Webb, Victor Jin, Shili Lin
- **期刊/来源**: Biostatistics
- **机构**: Keimyung University · Nationwide Children's Hospital · The Ohio State University · Medical College of Wisconsin
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 tREX-cap 方法，用于从 Hi-C 数据重建全基因组三维结构。现有优化类方法虽能处理全基因组尺度，但忽略空间依赖与细胞异质性；而基于采样的概率模型（如 tREX）虽能刻画过度离散、稀疏性等特征，却因计算代价过高而难以直接用于全基因组。tREX-cap 采用分治策略，将 tREX 模型应用于染色体片段，同时通过截断随机效应表达-剪切-粘贴（truncated Random effect EXpression-cut and paste）机制整合染色体间接触信息，兼顾了模型对数据特征的适应性与计算可行性。作者通过大规模模拟和两个真实 Hi-C 数据集（淋巴母细胞系和 IMR90）验证了方法的性能。该方法属于生物信息学/统计基因组学应用，方法学核心是分治计算策略与分层贝叶斯模型的结合，而非新的统计理论。
- **关键技术**: `divide and conquer`, `truncated random effect model`, `Hi-C data analysis`, `3D genome structure inference`, `Bayesian sampling`
- **为什么对您有用**: 本文属于统计计算与高维数据结构推断的应用，与您的统计计算兴趣（数值方法、算法）有弱连接；分治策略与模型复杂度权衡对您处理大规模计算问题有参考价值。但方法学新颖性有限，且不涉及因果推断、高维理论或效率理论，作为入门读物价值一般。

### 7. [10.1093/biostatistics/kxag028](https://doi.org/10.1093/biostatistics/kxag028) · [arXiv](https://arxiv.org/abs/2502.10513) — A Bayesian multivariate spatial point pattern model: application to oral microbiome FISH image data
- **作者**: Kyu Ha Lee, Brent A Coull, Suman Majumder, Patrick J La Riviere, Jessica L Mark Welch, Jacqueline R Starr
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Indian Statistical Institute · University of Chicago · American Dental Association · The Forsyth Institute · Brigham and Women's Hospital
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一个灵活的贝叶斯多元点过程模型，用于刻画和估计多种细胞类型之间的复杂空间相互作用，目标是对口腔微生物 FISH 图像中的空间组织进行量化。模型通过潜在高斯过程引入点模式间的依赖，并对相关系数采用收缩先验以保证估计的稳定性和可解释性。估计过程在贝叶斯框架下统一进行，能直接量化关键估计量（如类型间相关性和由类型间关系解释的方差比例）的不确定性。模型选择采用针对含潜变量模型设计的偏差信息准则（DIC），并通过贝叶斯分层池化模型综合图像特异的后验汇总，实现全局和个体水平的推断。计算上，R 包 mspatPPM 基于 Hamiltonian Monte Carlo 和自适应 Metropolis-Hastings 算法实现高效采样。应用于人类舌背微生物生物膜图像数据，发现特定菌对（如 S. mitis-S. salivarius）呈强正空间相关，而其他菌对（如 Actinomyces-Rothia）呈轻微负相关，且大部分菌群的空间方差可归因于菌间关系。
- **关键技术**: `Bayesian multivariate point process`, `latent Gaussian processes`, `shrinkage priors`, `deviance information criterion`, `hierarchical pooling model`, `Hamiltonian Monte Carlo`
- **为什么对您有用**: 本文属于应用统计工作，涉及空间点过程建模和贝叶斯推断，与您的主要兴趣（因果推断、高维统计等）无直接交集，但可作为流行病学或微生物组数据中空间相关结构分析的入门读物。其贝叶斯分层建模和不确定性量化思路对您处理纵向或空间数据可能有一定启发，但方法学新颖性有限，不值得深入阅读。

### 8. [10.1093/biostatistics/kxag029](https://doi.org/10.1093/biostatistics/kxag029) — <tt>transfactor</tt> : transcription factor activity estimation via probabilistic gene expression deconvolution
- **作者**: Koen Van den Berge, Peter Bickel, Sandrine Dudoit
- **期刊/来源**: Biostatistics
- **机构**: Ghent University · University of California, Berkeley
- **分类**: vol 27 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 transfactor，一种基于概率基因表达去卷积的转录因子（TF）活性估计方法。在单细胞 RNA 测序背景下，目标是估计每个 TF 的活性，即其调控的 mRNA 分子数，而非传统的差异表达分析。模型利用基因调控网络（GRN）先验信息，将每个 mRNA 分子概率性地分配给调控它的 TF，从而将表达差异转化为调控差异。方法能处理激活和抑制两种调控关系，并允许整合 TF-靶基因的调控潜力先验。通过两个模拟实验和两个案例研究，与现有 TF 活性估计方法（如基于富集分数的方法）对比，结果显示 transfactor 在 TF 优先级排序上更直观且可解释。
- **关键技术**: `probabilistic deconvolution`, `gene regulatory networks`, `single-cell RNA-sequencing`, `Bayesian inference`, `transcription factor activity estimation`
- **为什么对您有用**: 本文属于生物信息学应用，与您的主要兴趣（因果推断、高维统计等）无直接方法学连接，但作为统计计算和建模的应用案例，可能对您了解单细胞数据中的统计建模有参考价值。作为 gateway reading，本文对统计学家友好，模型设定清晰，但方法学新颖性有限，属于应用型工作。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

