# Biometrics — Vol 82  Issue 1  ·  2026-05-18

- 共 34 篇 · Biometrics

## 因果推断  *(causal_inference, 14 篇)*

### 1. [10.1093/biomtc/ujag017](https://doi.org/10.1093/biomtc/ujag017) — Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects
- **作者**: Chao Cheng, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 10/10 · novelty: `new_theory`
- **摘要**: 在整群随机试验(CRT)设定下，本文研究集群干预通过中介变量影响结局的因果机制，目标估计量为自然间接效应、个体中介效应和溢出中介效应（他人中介对自身结局的影响）。针对现有方法依赖参数假设的局限，作者发展了半参数效率理论，推导出各估计量的有效影响函数(EIF)，并基于EIF参数化构造了双重稳健(DR)估计量。在干扰函数估计上，既考虑了参数工作模型，也采用了数据自适应机器学习方法，后者结合交叉拟合可得到半参数有效估计量。模拟与实证分析表明该DR估计量在有限样本下具有稳健性和效率优势。对您有用：本文将半参数效率界与EIF推导扩展至带溢出效应的复杂中介设定，直接契合您在因果推断(中介与溢出)及效率理论(半参数有效估计与debiased ML)方面的核心兴趣。
- **关键技术**: `efficient influence function`, `doubly robust estimation`, `spillover mediation effect`, `data-adaptive machine learners`, `semiparametric efficiency theory`
- **为什么对您有用**: 直接契合您在因果推断（中介与溢出效应）及效率理论（半参数有效界、debiased ML）的核心兴趣；展示了如何在复杂依赖结构（CRT与溢出）下推导EIF并实现DR/debiased ML估计，方法可迁移至其他带干扰的因果图。

### 2. [10.1093/biomtc/ujaf174](https://doi.org/10.1093/biomtc/ujaf174) — Estimating optimal dynamic treatment regimes with Gaussian process emulation
- **作者**: Daniel Rodriguez Duque, David A Stephens, Erica E M Moodie
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断的动态治疗策略（DTR）设定下，目标是寻找使期望结局最大化的最优策略，传统 value search 方法依赖参数模型或面临网格搜索的计算瓶颈与高不确定性。本文提出利用高斯过程（GP）仿真优化方法来估计对特定 DTR 依从的因果效应，将带噪声的估计响应面建模为 GP 以替代网格搜索。GP 优化不仅避免了参数模型误设问题，还能在价值函数多模态时更高效地利用信息并降低不确定性。理论与模拟表明，相较于网格搜索，GP 方法在多模态设定下能稳健地收敛至最优 DTR，并在 HIV 疗法优化的流行病学数据中验证了其有效性。对您有用：该文将 GP 仿真引入纵向因果推断的 DTR 估计，为处理复杂响应面优化提供了新的计算思路，且 HIV 数据集对流行病学应用有参考价值。
- **关键技术**: `dynamic treatment regimes`, `Gaussian process emulation`, `value search estimation`, `marginal structural models`, `Bayesian optimization`
- **为什么对您有用**: 直接连接到您 primary interest 中的纵向因果推断（DTR）与统计计算（GP 优化算法），同时涉及 secondary interest 中流行病学（HIV 数据）的因果应用，提供了替代网格搜索的高效计算方案。

### 3. [10.1093/biomtc/ujag030](https://doi.org/10.1093/biomtc/ujag030) — Handling incomplete outcomes and covariates in cluster-randomized trials: doubly robust estimation, efficiency considerations, and sensitivity analysis
- **作者**: Bingkai Wang, Fan Li, Rui Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在整群随机试验（CRT）设定下，针对结局、协变量及群组人口规模同时缺失的问题，目标是估计多种效应尺度下的平均因果效应（ATE）。提出一种双重稳健（DR）估计量，同时处理随机缺失（MAR）的结局、无缺失机制约束的协变量，以及均匀抽样机制下的群组规模缺失。为提升精度，文章详细讨论了通过指定最优权重、利用机器学习及建模处理分配机制来逼近半参数效率界的方法。针对违背缺失数据假设的情况，提出了专门针对 CRT 的敏感性分析框架。理论证明了 DR 性质与效率提升，模拟与实例验证了方法有效性。对您有用：该文将 DR 估计与效率理论拓展至 CRT 复杂缺失场景，其敏感性分析框架可直接迁移至流行病学因果推断应用中。
- **关键技术**: `doubly robust estimation`, `semiparametric efficiency bound`, `optimal weights`, `sensitivity analysis`, `missing at random (MAR)`, `cluster-randomized trials`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断（DR 估计、敏感性分析）与效率理论（最优权重、精度提升），同时其 CRT 设定与敏感性分析框架对您 secondary interest 中的流行病学因果应用具有直接迁移价值。

### 4. [10.1093/biomtc/ujag050](https://doi.org/10.1093/biomtc/ujag050) — A robust covariate-balancing method for estimating individualized treatment with censored data
- **作者**: Rujia Zheng, Wensheng Zhu, Xiaofan Guo
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在删失数据的因果推断框架下，目标是估计最优个体化治疗方案（ITR）以最大化期望生存时间，关键假设包括处理与删失机制的无混杂性。针对传统基于倾向得分或结局模型误设导致估计失效的问题，本文定义了生存分析的对比值函数，并提出两种稳健协变量平衡估计量。核心机制是在权重中分别引入删失概率和删失时间的生存函数来实现协变量平衡，从而避免直接指定结局回归模型。理论证明所提估计量具有双重稳健性，并在标准正则条件下满足 n^{-1/2}-CAN（收敛至渐近正态）。模拟表明其在模型误设下优于现有方法；实证应用于中国农村高血压控制项目，估计的ITR显著提升了36个月随访生存率。对您有用：该文将协变量平衡与双重稳健性拓展至删失数据，对您关注的因果推断估计理论（DR/CAN）及流行病学队列数据应用均有直接参考价值。
- **关键技术**: `covariate balancing`, `double robustness`, `contrast value function`, `censored data survival analysis`, `asymptotic normality`
- **为什么对您有用**: 直接涉及因果推断的半参数估计理论（双重稳健与渐近正态），且应用了流行病学队列数据集，契合您在因果推断（估计/生存数据）和流行病学应用上的双重兴趣。

### 5. [10.1093/biomtc/ujag023](https://doi.org/10.1093/biomtc/ujag023) — Causal inference with misspecified network interference structure
- **作者**: Bar Weinstein, Daniel Nevo
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在网络干扰设定下，目标是估计处理效应，但现有方法通常假设网络结构已知且正确，本文则研究网络结构误设的后果及鲁棒估计。作者推导了使用误设网络估计因果效应时的偏差界，证明偏差随假定网络与真实网络诱导的暴露概率（exposure probabilities）之间的散度增大而增加。为解决此问题，提出了一种利用多个候选网络同时进行估计的新估计量。该估计量在至少一个候选网络正确时保持无偏，且无需预先知道哪个网络正确，从而提供了对网络设定的鲁棒性。模拟与社交网络实验数据验证了该估计量的有限样本表现。对您有用：该工作为网络干扰下的因果推断提供了对结构假设的敏感性分析视角，与您关注的因果推断敏感性分析及识别假设放松直接相关。
- **关键技术**: `network interference`, `exposure mapping`, `bias bounds`, `multiple network estimator`, `robustness to misspecification`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断敏感性分析，提供了网络干扰设定下对结构误设的鲁棒估计方法，可迁移至流行病学或经济学的社交网络应用中。

### 6. [10.1093/biomtc/ujag034](https://doi.org/10.1093/biomtc/ujag034) — Distributed fusion <i>R</i> -learner of heterogeneous treatment effect using distributed medicaid data
- **作者**: Jinhong Li, Julie M Donohue, Lu Tang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在多站点数据整合与隐私保护设定下，本文研究条件平均处理效应（CATE）的分布式估计，允许不同站点间的处理效应异质性。提出分布式融合 R-learner（DF R-learner），采用数据驱动的融合惩罚（fusion penalty）合并跨站点相似参数以提升估计精度。该方法利用置信分布（confidence distributions）在站点间传递汇总统计量，实现无需共享个体数据的隐私保护计算。理论上证明了基于置信分布的分布式估计量可达到与集中式数据相同的渐近效率（无效率损失）。实证部分通过宾州 Medicaid 多个管理医疗组织的阿片类药物使用障碍治疗数据验证了方法有效性。对您有用：该文结合了因果推断（CATE异质性）、效率理论（分布式下无效率损失的证明）与统计计算（分布式融合算法），并提供了流行病学 Medicaid 数据集的应用参考。
- **关键技术**: `R-learner`, `distributed fusion learning`, `confidence distribution`, `fusion penalty`, `conditional average treatment effect`
- **为什么对您有用**: 直击您在因果推断（CATE异质性）、效率理论（分布式下达到集中式半参数效率界）和统计计算（隐私保护分布式算法）三个 primary interest 的交叉点，同时提供流行病学 Medicaid 数据的 secondary interest 参考。

### 7. [10.1093/biomtc/ujag047](https://doi.org/10.1093/biomtc/ujag047) — Nonparametric ANCOVA for longitudinal outcomes in a randomized clinical trial
- **作者**: Rex Shen, Xiaotong Jiang, Changyu Shen, Lu Tian
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在随机对照试验（RCT）的纵向结局设定下，目标是估计平均处理效应（ATE），传统混合效应模型严重依赖正确的参数模型设定。本文提出一种非参数 ANCOVA 方法，无需假设混合效应模型正确设定。作者刻画了纵向结局下的最优 ANCOVA 调整形式，证明适当的协变量调整可大幅提升 ATE 估计精度。由于最优调整依赖于纵向结局给定基线协变量的未知条件期望，该方法采用 cross-fitting 程序对该条件期望进行非参数估计，从而指导 ANCOVA 的构建。理论与数值实验表明，该非参数 ANCOVA 相较传统方法更稳健且精度更高。该文将 cross-fitting 与非参数条件期望结合以实现纵向 RCT 的最优协变量调整，直接契合您在纵向因果推断、半参数效率理论及 cross-fitting/DML 方面的核心兴趣。
- **关键技术**: `nonparametric ANCOVA`, `cross-fitting`, `optimal covariate adjustment`, `conditional expectation estimation`, `longitudinal outcomes`
- **为什么对您有用**: 直接连接您在纵向因果推断和效率理论的兴趣；展示了如何通过 cross-fitting 估计条件期望来实现非参数下的最优协变量调整（逼近有效界），对 RCT 下的 robust 估计有方法迁移价值。

### 8. [10.1093/biomtc/ujaf167](https://doi.org/10.1093/biomtc/ujaf167) — Learning optimal early decision treatment rules with multi-domain intermediate outcomes
- **作者**: Wenbo Fei, Yuan Chen, Zexi Cai, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在长期最终结局难以获取的纵向精准医疗设定下，目标是利用多域中间结局（如患者自评等代理变量）学习最优个体化治疗规则（ITR）。方法将多域中间观测推断的潜在状态进行个性化加权，构建复合结局作为 ITR 的奖励函数，并保证该复合结局与长期最终结局的一致性。该框架克服了传统 ITR 仅依赖最终结局而忽略早期信号的局限，实现了对无响应者的早期检测。模拟研究与重度抑郁症（MDD）随机临床试验数据表明，该方法在提升长期治疗结局方面优于传统方法。对您有用：该工作利用中间结局作为最终结局的代理变量，与您关注的 proximal CI 及纵向因果推断设定高度契合，其复合代理结局的构建思路可为 surrogate/proxy 的 identification 与估计提供方法借鉴，同时 MDD 数据集对流行病学应用有参考价值。
- **关键技术**: `individualized treatment rules`, `intermediate outcomes as proxies`, `latent state inference`, `personalized composite outcome`, `long-term outcome consistency`
- **为什么对您有用**: 利用中间结局作为代理变量学习 ITR 的思路与您关注的 proximal CI 及纵向因果推断直接相关，方法可迁移至 surrogate/proxy 设定；同时包含 MDD 临床试验数据，对流行病学应用有数据集价值。

### 9. [10.1093/biomtc/ujag022](https://doi.org/10.1093/biomtc/ujag022) — Bias mitigation in matched observational studies with continuous treatments: calipered non-bipartite matching and bias-corrected estimation and inference
- **作者**: Anthony Frazier, Siyu Heng, Wen Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在连续处理（continuous treatments）的匹配观察性研究中，目标是对处理剂量效应进行因果推断，关键假设是匹配后协变量平衡。本文指出，即使匹配后协变量平衡满足常规标准，不精确匹配（inexact matching）仍可引入严重偏差，并通过社交距离对COVID-19病例数影响的数据重新分析加以验证。匹配阶段，提出结合协变量距离与处理剂量信息的 caliper，用于改进非二部图匹配（non-bipartite matching）。估计与推断阶段，引入偏差校正的 Neyman 估计量及对应的偏差校正方差估计量。数值模拟和实证分析表明该框架有效减轻了不精确匹配导致的偏差。对您有用：该工作为连续处理因果推断中的匹配偏差校正提供了完整框架，与您在因果推断估计方法及流行病学应用方面的兴趣直接相关，偏差校正 Neyman 估计量的构造思路可迁移至其他匹配设计。
- **关键技术**: `non-bipartite matching`, `caliper design with dose information`, `bias-corrected Neyman estimator`, `continuous treatment dose-response`, `covariate imbalance correction`
- **为什么对您有用**: 连续处理因果推断的匹配与偏差校正方法，与您 primary interest 中的因果推断估计方法及 secondary interest 中的流行病学应用直接相关；偏差校正 Neyman 估计量的思路可迁移至其他匹配/分层设计中的推断问题。

### 10. [10.1093/biomtc/ujaf168](https://doi.org/10.1093/biomtc/ujaf168) — An adaptive design for optimizing treatment assignment in randomized clinical trials
- **作者**: Wei Zhang, Zhiwei Zhang, Aiyi Liu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在随机对照试验设定下，研究如何在给定随机化机制类内优化处理分配以最大化统计效率，关键正则条件依赖于潜在结果给定基线协变量的条件方差函数。针对条件方差函数在设计阶段通常未知的问题，提出一种多阶段自适应设计，允许在期中分析时利用累积数据更新条件方差估计并修改分配机制。由于自适应分配改变了后续数据的分布，作者构建了一类一致且渐近正态（CAN）的处理效应估计量，并在该类中识别出最有效估计量。通过代入未知量的估计来近似该最有效估计量，仿真表明在先验信息缺乏时，该方法相比传统单阶段设计具有显著的效率提升。对您有用：该文将半参数效率理论拓展至自适应随机化下的因果效应估计，对您研究RCT设计下的效率界与最优估计量具有直接参考价值。
- **关键技术**: `adaptive randomization`, `conditional variance functions`, `semiparametric efficiency`, `asymptotically normal estimator`, `influence function`, `multi-stage design`
- **为什么对您有用**: 将半参数效率理论应用于自适应随机化下的因果效应估计，直接契合您在efficiency theory和causal inference上的核心兴趣，展示了如何在复杂设计下推导并实现最优估计量。

### 11. [10.1093/biomtc/ujaf173](https://doi.org/10.1093/biomtc/ujaf173) — Estimating the causal effect of redlining on present-day air pollution
- **作者**: Xiaodan Zhou, Shu Yang, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在空间因果推断设定下，本文研究1930年代红线政策对当代空气污染（PM2.5和NO2）的长期因果效应，核心挑战是缺乏预处理协变量导致的未测量混杂。为此，提出一种空间与非空间潜在因子框架，利用1940年人口普查变量（失业率、房租、黑人比例）作为代理变量重构预处理潜在社会经济地位。该方法在较宽泛的假设下实现了因果效应的识别，并采用贝叶斯MCMC进行不确定性量化。实证结果表明，红线社区暴露于显著更高的NO2浓度，而PM2.5的差异相对较弱。该文将代理变量思想与潜在因子模型结合以处理未测量混杂，对您研究proximal CI框架下的negative control设定及流行病学因果应用具有方法迁移与数据集参考价值。
- **关键技术**: `spatial causal inference`, `latent factor model`, `proxy variable`, `unmeasured confounding`, `Bayesian MCMC`
- **为什么对您有用**: 该文利用代理变量与潜在因子模型处理未测量混杂的思路与您关注的proximal CI紧密相关，同时提供了流行病学/环境健康领域的因果推断应用与数据集参考。

### 12. [10.1093/biomtc/ujaf176](https://doi.org/10.1093/biomtc/ujaf176) — Long-term memory effects of an incremental blood pressure intervention in a mortal cohort
- **作者**: Maria Josefsson, Nina Karalija, Michael J Daniels
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在存在死亡截断的纵向队列中，本文研究增量血压干预对情景记忆的长期因果效应，区分了病因学效应与预后效应。为解决死亡截断导致的识别问题，采用扩展 G-formula 进行 identification，并提出贝叶斯半参数估计方法来估计增量阈值干预效应。方法上引入了利用纵向数据结构的稀疏诱导 Dirichlet 先验，并在模拟中与贝叶斯决策树集成方法对比。对 Betula 队列的应用显示血压干预在总体人群或始终存活层中均无显著记忆效应。该文将增量干预与扩展 G-formula 结合处理死亡截断，对您在纵向因果推断和流行病学应用中的研究有直接方法学借鉴价值。
- **关键技术**: `incremental threshold intervention`, `extended G-formula`, `truncation by death`, `Bayesian semi-parametric estimation`, `sparsity-inducing Dirichlet prior`, `etiological and prognostic effects`
- **为什么对您有用**: 直接涉及纵向因果推断中的死亡截断问题与增量干预策略，扩展 G-formula 的半参数贝叶斯实现及流行病学队列数据（Betula）对您的纵向因果推断和流行病学应用兴趣有直接参考价值。

### 13. [10.1093/biomtc/ujag003](https://doi.org/10.1093/biomtc/ujag003) — Scalable and distributed individualized treatment rules for multicenter datasets
- **作者**: Nan Qiao, Wangcheng Li, Jingxiao Zhang, Canyi Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多中心数据与隐私约束设定下，目标是学习最优个体化处理规则（ITR）而避免汇聚原始数据。传统元学习方法因局部估计偏差常导致次优结果，本文提出卷积平滑加权支持向量机，其损失函数兼具凸性与光滑性，从而支持多轮分布式学习。该分布式算法仅需传递汇总统计量，在固定通信轮数内即可达到最优统计性能，显著降低多中心协调成本。同时开发了坐标梯度下降算法，保证优化问题至少具有线性收敛速率。该方法在模拟与脓毒症多ICU应用中验证了有效性；对您有用：为多中心因果推断（ITR）提供了兼顾隐私与通信效率的分布式计算方案，契合您对因果推断与统计计算交叉方向的兴趣。
- **关键技术**: `individualized treatment rules`, `distributed learning`, `convolution-smoothed weighted SVM`, `coordinate gradient descent`, `multi-center privacy-preserving inference`
- **为什么对您有用**: 结合了因果推断中的ITR估计与统计计算中的分布式优化算法，契合您对因果推断与统计计算交叉方向的兴趣，提供了多中心隐私约束下的高效算法与收敛性保证。

### 14. [10.1093/biomtc/ujag014](https://doi.org/10.1093/biomtc/ujag014) — A framework for causal estimand selection under positivity violations
- **作者**: Martha Barnard, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在观察性研究中，当协变量分布缺乏重叠（positivity violations）时，研究者常面临传统估计量（如 IPW 估计 ATE）的高方差/高偏差与修改目标人群（如 overlap weighting）导致的 estimand 不匹配之间的权衡。本文提出一种 estimand 选择框架，将总偏差分解为统计偏差（statistical bias of the estimator）与 estimand 偏差（estimand mismatch）。基于此分解，作者引入两个基于设计的度量指标和 estimand 选择程序，显式量化偏差与方差之间的权衡。该程序允许分析者引入领域偏好，在保留原始研究人群与降低统计偏差之间进行灵活调整，并在右心导管（right heart catheterization）流行病学数据上进行了实证演示。对您有用：直接关联您 primary interest 中的因果推断估计与假设违背处理，为 positivity 假设不成立时的 estimand 选择与偏差-方差权衡提供了形式化框架。
- **关键技术**: `positivity violations`, `overlap weighting`, `bias decomposition`, `estimand mismatch`, `inverse probability weighting`, `design-based metrics`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断估计与假设违背处理，为 positivity 假设不成立时的 estimand 选择与偏差-方差权衡提供了形式化框架；同时应用了流行病学经典数据集，契合您 secondary interest。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biomtc/ujag039](https://doi.org/10.1093/biomtc/ujag039) — Sparse robust discriminant analysis for high-dimensional and heavy-tailed data
- **作者**: Weijian Huang, Qing Mai, Jing Zeng
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `weaker_assumption`
- **摘要**: 在高维重尾设定下，本文研究椭圆等高判别分析（EDA）模型的稀疏鲁棒分类，目标是在有限四阶矩条件下实现降维子空间估计与分类。提出基于内在降维子空间投影的鲁棒高维分类器，先通过子空间投影降维，再对降维数据执行预测；同时引入平衡率（balanced rate）以更合适地度量不平衡数据的预测精度。理论上，在仅要求预测变量具有有限四阶矩的弱正则条件下，同时保证了子空间估计、变量选择与预测精度的一致性。数值实验在合成数据及肺癌、白血病等真实医学数据上验证了其相对现有方法的优越性。对您而言，该文在高维统计中放松了传统的轻尾假设至有限四阶矩，其弱假设下的估计一致性理论对高维推断有借鉴意义，且医学数据集可服务于流行病学因果推断探索。
- **关键技术**: `sparse linear discriminant analysis`, `elliptically contoured discriminant analysis`, `dimension-reduction subspace`, `finite fourth-moment condition`, `balanced rate`, `robust high-dimensional classification`
- **为什么对您有用**: 涉及您 primary interest 中的高维统计（放松轻尾假设至有限四阶矩的稀疏判别一致性理论），同时其肺癌与白血病医学数据集契合您 secondary interest 中的流行病学应用。

### 2. [10.1093/biomtc/ujag035](https://doi.org/10.1093/biomtc/ujag035) — Ultra-high-dimensional threshold selection for quantile feature screening with false discovery rate error rate control: a case study on high blood pressure analysis
- **作者**: Saidat Abidemi Sanni, Yan Yu, Zhigen Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在超高维遗传数据的分位特征筛选设定下，研究目标是实现数据自适应的阈值选择并控制错误发现率（FDR）。提出分位镜像（QM）方法，利用对称 QM 统计量构造零分布估计以实现 FDR 估计。引入 QREDS（Quantile REflection via Data Splitting）及硬阈值筛选程序，通过多次数据分割提升结果稳定性，并允许不同分位数设定不同阈值。理论上证明了在适当正则条件下所提程序渐近控制 FDR。实证分析应用于 Framingham Heart Study 数据，验证了已知高血压风险基因并发现新因子。对您有用：该文将 FDR 控制引入超高维分位筛选，对您的高维统计（特征筛选/多重检验）及流行病学（Framingham 数据集）兴趣有直接参考价值。
- **关键技术**: `quantile feature screening`, `false discovery rate control`, `mirror statistic`, `multiple data splitting`, `ultra-high-dimensional threshold selection`
- **为什么对您有用**: 连接高维统计（超高维特征筛选与 FDR 多重检验控制）与流行病学（Framingham Heart Study 数据集应用），为高维假设检验提供新阈值选择程序及实际数据参考。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1093/biomtc/ujaf175](https://doi.org/10.1093/biomtc/ujaf175) — Multiple-index interaction models to accommodate exposure grouping in environmental mixtures
- **作者**: Myeonggyun Lee, Mengling Liu, Shanshan Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在环境混合物暴露分组的设定下，目标是估计多组暴露对健康结局的非线性效应及组间交互作用，假设暴露可按生物学特征分组且通过组级指数影响结局。提出半参数多指标交互模型（MIIM），将高维暴露降维为组级指数（multiple-index），允许非线性效应和组间交互，适用于连续、二元及生存结局。该模型通过多指标结构在保持可解释性的同时缓解高维挑战，并能识别各组内关键贡献变量。模拟显示 MIIM 在高维相关暴露下表现良好，NHANES 数据实证了三组持久性有机污染物对白细胞端粒长度的影响。对您有用：该文将半参数多指标模型应用于流行病学高维混合物，其降维与交互作用建模思路可迁移至因果推断中的高维中介/混杂调整，且 NHANES 数据集对流行病学应用有参考价值。
- **关键技术**: `semiparametric multiple-index model`, `exposure grouping`, `nonlinear interaction`, `high-dimensional dimension reduction`, `survival outcome regression`
- **为什么对您有用**: 半参数多指标模型（multiple-index model）是您关注的非参数/半参数理论的重要结构，其高维降维与组间交互机制可启发因果推断中高维混杂/中介的建模；同时提供了 NHANES 流行病学数据集的应用案例。

### 2. [10.1093/biomtc/ujag044](https://doi.org/10.1093/biomtc/ujag044) — Variable selection in functional linear Cox model
- **作者**: Yuanzhen Yue, Stella Self, Yichao Wu, Jiajia Zhang, Rahul Ghosal
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在含多函数型与标量协变量的函数线性 Cox 模型下，目标是同时对函数系数进行半参数估计与变量选择，假设基线协变量与生存结局满足比例风险假设。方法采用基于样条的半参数估计逼近函数系数，并引入 group minimax concave penalty (MCP) 将平滑性与稀疏性整合到系数估计中。优化求解使用高效的 group descent 算法，并提供了平滑参数与稀疏惩罚参数的自动选择程序。模拟显示该方法在变量选择与估计上具有良好有限样本性质；实证分析 NHANES 队列数据识别了与全因死亡率相关的体力活动时间分布模式。该文将 group MCP 惩罚与样条半参数估计结合的框架及算法实现，可迁移至您关注的半参数理论与统计计算方向，同时 NHANES 穿戴设备数据对流行病学应用有参考价值。
- **关键技术**: `functional linear Cox model`, `spline-based semiparametric estimation`, `group minimax concave penalty`, `group descent algorithm`, `sparsity and smoothness regularization`
- **为什么对您有用**: 该文结合样条半参数估计与 group MCP 惩罚的高维变量选择框架及 group descent 算法实现，直接关联您的半参数理论与统计计算方向；同时 NHANES 队列的穿戴设备数据应用对流行病学因果推断研究具有数据集参考价值。

### 3. [10.1093/biomtc/ujag040](https://doi.org/10.1093/biomtc/ujag040) — Reduced varying coefficient models for regional quantile regression with multiple responses
- **作者**: Woorim Jung, Seyoung Park, Hyokyoung G Hong, Eun Ryung Lee
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在高维多响应设定下，本文研究区域分位数回归的变系数模型，目标是对随时间指数变化的系数矩阵进行降维估计与聚类。方法上，通过主成分函数对多元分位数变系数施加低秩结构约束，实现降维与可解释性；同时引入 KNN-fused LASSO 惩罚项，以捕捉主成分间的共享动态模式并识别潜在聚类。模拟研究表明该方法在高维场景下估计一致且稳健，并在两个真实健康数据集中揭示了预测变量与多响应间随时间变化的分位数特异性关联。对您有用：该文将低秩结构与 fused LASSO 结合处理高维多响应变系数，其计算策略与降维思路可迁移至您关注的半参数/高维统计及流行病学应用中。
- **关键技术**: `varying coefficient model`, `regional quantile regression`, `low-rank matrix approximation`, `KNN-fused LASSO`, `principal component functions`
- **为什么对您有用**: 结合了高维降维（低秩结构）与半参数（变系数分位数回归）方法，并在流行病学健康数据上应用，对您在半参数理论及流行病学应用方向有参考价值。

### 4. [10.1093/biomtc/ujag051](https://doi.org/10.1093/biomtc/ujag051) — Simultaneous clustering and estimation of additive shape invariant models for recurrent event data
- **作者**: Zitong Zhang, Shizhe Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在神经科学重复刺激实验的复发事件数据设定下，目标是识别具有独特刺激响应的神经元聚类并估计其叠加响应函数，面临未知时间偏移的挑战。提出一种新的加性形状不变模型，同时处理多聚类、加性成分和未知时间平移。理论上建立了模型参数的可识别性条件，为实验设计提供指导。算法上实现了聚类与估计的同步进行，并在小鼠视觉辨别任务的双随机刺激神经尖峰序列数据中识别出三个具有异质响应模式的功能群。对您可能有用：其半参数形状不变模型的可识别性证明及同步估计算法，对您在半参数理论中的可识别性分析及统计计算中的算法设计有参考价值。
- **关键技术**: `additive shape invariant model`, `identifiability conditions`, `simultaneous clustering and estimation`, `time-shift alignment`, `recurrent event data`
- **为什么对您有用**: 涉及半参数模型（形状不变模型）的可识别性条件与估计算法，与您在半参数理论及统计计算方面的兴趣相关，可借鉴其处理未知平移与加性结构的理论技巧。

### 5. [10.1093/biomtc/ujag015](https://doi.org/10.1093/biomtc/ujag015) — A general framework for heterogeneous variable importance: Pointwise and uniform inference
- **作者**: Lingxuan Shao, Guorong Dai, Jinbo Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在缺乏显式参数结构的复杂模型中，本文研究协变量对响应变量的“异质性变量重要性”，即该贡献如何随特征变量（如年龄）变化，目标参数定义为两个条件均方误差的比值。作者提出了该比值参数的点估计量，并基于非参数理论建立了其逐点和一致收敛速率。进一步开发了渐近置信区间与置信带的构造方法，并证明其能达到名义覆盖率。核心技术依赖于条件期望的非参数估计与经验过程的均匀推断工具。模拟与真实数据验证了有限样本表现。对您而言，该文在非参数比率参数的逐点与一致推断上提供了新理论，对研究半参数/非参数理论及假设检验（均匀置信带）有直接参考价值。
- **关键技术**: `heterogeneous variable importance`, `conditional MSE ratio`, `uniform convergence rate`, `asymptotic confidence bands`, `nonparametric smoothing`
- **为什么对您有用**: 直接关联您的半参数/非参数理论及假设检验（均匀置信带）兴趣，提供了非参数比率参数一致推断的新理论；同时Biometrics的实证应用对流行病学方向有数据集参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1093/biomtc/ujaf166](https://doi.org/10.1093/biomtc/ujaf166) — Jointly modeling multiple endpoints for efficient treatment effect estimation in randomized controlled trials
- **作者**: Jack M Wolf, Joseph S Koopmeiners, David M Vock
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在随机对照试验（RCT）中，主要终点的处理效应估计常面临功效不足的问题，而次要终点虽功效较高但科学相关性较弱。本文提出一种基于主要与次要终点联合模型的处理效应估计量，在模型正确设定时相比标准估计量能提升渐近效率。为应对模型误设风险，该方法通过模型平均（model averaging）机制保证了估计的稳健性。在烟草监管科学的应用中（评估极低尼古丁香烟对黑人戒烟比例的影响），该方法将标准误降低了 27%。对您有用：该工作在 RCT 因果估计中利用多终点实现效率提升且保持误设稳健性，直接契合您对 efficiency theory 与 causal inference 交叉方向的兴趣，其 model averaging 策略也可为半参数效率界逼近提供新思路。
- **关键技术**: `joint modeling of multiple endpoints`, `model averaging`, `efficient treatment effect estimation`, `robustness to misspecification`, `randomized controlled trials`
- **为什么对您有用**: 直接契合您在 efficiency theory 和 causal inference 上的核心兴趣，展示了如何在 RCT 中通过联合建模与模型平均实现效率提升且保持稳健性，同时涉及流行病学（烟草监管）的实际应用数据集。

### 2. [10.1093/biomtc/ujag041](https://doi.org/10.1093/biomtc/ujag041) — Generalized entropy calibration for analyzing voluntary survey data
- **作者**: Yonghyun Kwon, Jae Kwang Kim, Yumou Qiu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在可忽略抽样机制假设下，研究自愿调查数据的选择偏差问题，目标是构建统一的校准加权估计量。引入广义熵校准作为控制选择偏差的统一工具，并建立了校准加权与其对偶回归估计之间的理论联系。该对偶关系对识别隐含回归模型及发展校准加权的模型选择至关重要。在重要研究变量的线性回归模型可用时，两步校准法可平滑最终权重并实现统计效率。理论上证明了所提估计量具有双重鲁棒性与局部有效性。对您有用：该文对偶视角下的校准加权与效率理论直接相关，为处理因果推断/缺失数据中的选择偏差及构建双重鲁棒估计提供了可迁移的半参数方法思路。
- **关键技术**: `generalized entropy calibration`, `calibration weighting`, `dual regression estimation`, `double robustness`, `local efficiency`, `two-step calibration`
- **为什么对您有用**: 直接涉及半参数效率理论中的双重鲁棒性与局部有效性，其校准加权与对偶回归的框架可迁移至因果推断中处理选择偏差与缺失数据的估计问题。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujag052](https://doi.org/10.1093/biomtc/ujag052) — Rank-adaptive covariance testing with applications to genomics and neuroimaging
- **作者**: David Veitch, Yinqiu He, Jun Young Park
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维两样本设定下，当协方差差异源于低秩结构且信号弱分散时，传统协方差检验方法常面临功效损失。本文基于 Ky-Fan(k) 范数（前 k 个奇异值之和）提出 rank-adaptive covariance testing (RACT) 方法，以捕捉矩阵间低秩结构差异。方法采用置换检验进行统计推断，保证精确的第一类错误控制。模拟与肺癌基因网络及 DTI 脑成像数据的实证表明，RACT 在低秩信号下功效显著优于现有方法。该工作将 Ky-Fan 范数与高维假设检验结合，直接契合您对高维统计（奇异值/低秩结构）与假设检验的兴趣，且提供了神经影像/基因组学数据集参考。
- **关键技术**: `Ky-Fan(k) norm`, `two-sample covariance testing`, `permutation test`, `low-rank structure`, `singular value decomposition`
- **为什么对您有用**: 直接契合您对高维统计（奇异值/低秩结构）与假设检验的 primary interest，同时提供了神经影像/基因组学的 secondary interest 数据集参考。

### 2. [10.1093/biomtc/ujag042](https://doi.org/10.1093/biomtc/ujag042) — Inference for microbe–metabolite association networks using a latent graph model
- **作者**: Jing Ma
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在微生物-代谢物关联网络的多重检验设定下，传统 BH 等方法因假设 p 值弱依赖而在存在密集模块时检验功效不足，本文旨在提出一种在强依赖结构下仍能控制 FDR 且提升功效的推断方法。核心方法通过二分随机块模型刻画网络潜在的模块化结构，并利用变分 EM 算法估计模型参数；将学习到的图结构融入假设检验过程，利用潜在社区信息调整检验程序，从而在保证 FDR 控制的同时显著提升发现真实关联的功效。模拟与细菌性阴道病真实数据分析表明，该方法在保留 FDR 控制的前提下，相比 BH 等传统方法在模块化网络中具有更高的检验功效，并附带提供微生物与代谢物的聚类结果。对您有用之处在于：该文将图模型与多重检验结合的思路，为处理高维依赖结构下的假设检验提供了新视角，同时其流行病学数据集对您的应用方向有参考价值。
- **关键技术**: `false discovery rate control`, `bipartite stochastic block model`, `variational EM algorithm`, `multiple testing under dependence`, `latent graph model`
- **为什么对您有用**: 涉及您 primary interest 中的假设检验（多重检验在依赖结构下的 FDR 控制）与统计计算（变分 EM 算法），同时其微生物组应用属于您 secondary interest 中的流行病学数据集。

## 统计计算 / 算法  *(stat_computing, 4 篇)*

### 1. [10.1093/biomtc/ujag013](https://doi.org/10.1093/biomtc/ujag013) — Non-boundary covariance matrix estimation in generalized linear mixed effects models using data augmentation priors
- **作者**: Tina Košuta, Erik Langerholc, Rok Blagus
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在广义线性混合效应模型 (GLMM) 中，最大似然估计常导致随机效应协方差矩阵的边界估计（奇异估计），引发数值不稳定并影响后续推断。本文通过引入基于条件共轭先验的惩罚项来修正似然函数，该惩罚项可表示为伪观测值，从而将惩罚估计转化为数据增广问题，使其能直接在现有 ML 软件中实现。作者推导了构造伪观测值的程序，确保其似然贡献与惩罚函数形式匹配且仅依赖于协方差或精度矩阵。针对惩罚参数，提出了一种无需先验设定的全数据驱动选择程序，避免了主观先验指定。模拟与实际数据表明该方法在避免边界估计和提升协方差估计精度上优于现有方法。对您而言，其伪观测数据增广技巧为统计计算（数值方法与算法）提供了巧妙的实现思路，且在流行病学纵向数据的 GLMM 应用中具有实用价值。
- **关键技术**: `penalized maximum likelihood`, `data augmentation priors`, `pseudo-observations`, `generalized linear mixed models`, `covariance matrix estimation`
- **为什么对您有用**: 伪观测数据增广技巧巧妙解决了 GLMM 协方差矩阵边界估计的数值计算问题，对您在统计计算（数值方法与算法）方向的兴趣有直接启发，同时方法适用于流行病学纵向数据分析。

### 2. [10.1093/biomtc/ujaf169](https://doi.org/10.1093/biomtc/ujaf169) — Optimal design of dynamic experiments for scalar-on-function linear models with application to a biopharmaceutical study
- **作者**: Damianos Michaelides, Maria Adamou, David C Woods, Antony M Overstall
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在函数型协变量实验设定下，本文针对 scalar-on-function 线性模型提出贝叶斯最优实验设计框架。通过对函数型变量进行基展开，将无限维函数设计转化为有限维组合优化问题，从而在控制模型与变量复杂度的同时求解最优设计。方法采用贝叶斯准则（如期望后验方差）与坐标交换等数值算法寻找最优函数组合，并在 Ambr250 生物反应器动态喂养实验中进行了验证。对您而言，其基展开处理函数型数据的思路与半参数理论有微弱交叉，但整体偏应用实验设计，方法学新颖度相对有限。
- **关键技术**: `Bayesian optimal design`, `scalar-on-function regression`, `basis expansion`, `functional data analysis`, `coordinate exchange algorithm`
- **为什么对您有用**: 涉及函数型数据的基展开表示（与半参数/非参数理论有交叉）和实验设计的数值求解（统计计算），但核心偏向生物制药应用，对您主要关注的理论/因果推断直接收益较小。

### 3. [10.1093/biomtc/ujag046](https://doi.org/10.1093/biomtc/ujag046) — LLOT: application of Laplacian Linear Optimal Transport in spatial transcriptome reconstruction
- **作者**: Junhao Zhu, Kevin Zhang, Dehan Kong, Zhaolei Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 1/10 · novelty: `application`
- **摘要**: 在空间转录组重建设定下，目标是整合scRNA-seq与空间表达数据，以单细胞分辨率推断缺失的全基因组空间表达谱。本文提出Laplacian Linear Optimal Transport (LLOT) 方法，通过迭代校正平台效应，并利用Laplacian Optimal Transport将空间转录组中的每个spot分解为单细胞的空间平滑概率混合。该方法结合了线性最优传输的计算效率与拉普拉斯正则化的空间平滑性。在多种空间转录组技术（ISH, Slide-seq, Visium等）数据集上的实验表明LLOT具有良好的重建精度与可解释性。对您而言，其Laplacian Optimal Transport的迭代算法设计在统计计算（数值方法与算法）方面有一定参考价值，但方法学理论创新有限。
- **关键技术**: `Laplacian Optimal Transport`, `Linear Optimal Transport`, `platform effect correction`, `spatial smoothing regularization`, `probabilistic mixture decomposition`
- **为什么对您有用**: 涉及最优传输的数值算法设计与迭代求解，对应您在统计计算（数值方法与算法）方向的兴趣，但核心为生物数据应用，理论创新较弱。

### 4. [10.1093/biomtc/ujag016](https://doi.org/10.1093/biomtc/ujag016) — Estimation of mixed-effects ordinary differential equation models linear in the parameters
- **作者**: Oleksandr Laskorunskyi, Snigdhansu Chatterjee, Itai Dattner
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在参数线性的常微分方程 (ODE) 混合效应模型设定下，本文目标是估计固定与随机效应（含嵌套、交叉结构）。提出 Direct Integral Mixed-Effects (DIME) 方法，利用参数与状态的分离性，将非线性 ODE 估计转化为线性混合效应模型 (LMM) 框架，从而可直接调用标准 LMM 推断工具（如置信区间与模型选择）。理论上证明了估计量的一致性与渐近正态性。模拟表明 DIME 在偏差和 RMSE 上具竞争力，且在有限样本下方差分量的覆盖概率优于 nlme 等传统方法；实证涵盖人口增长与大气压/风速动态。对您有用：ODE 的推断与计算属于统计计算与半参数理论交叉，其参数分离技巧对纵向/动态数据的推断有借鉴意义，大气动态应用也契合您对天文/环境统计的次级兴趣。
- **关键技术**: `ordinary differential equation models`, `linear mixed-effects model`, `direct integral method`, `asymptotic normality`, `parameter-state separability`
- **为什么对您有用**: ODE 模型的推断与计算涉及统计计算与半参数理论，其参数分离技巧对纵向/动态数据的推断有借鉴意义；大气动态的实证应用契合您对天文/环境统计的次级兴趣。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biomtc/ujag020](https://doi.org/10.1093/biomtc/ujag020) — Bayesian nowcasting for delay adjustments using time-varying parametric functions of cumulative reporting probability
- **作者**: Erick A Chacón-Montalván, Yang Xiao, Paula Moraga
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在流行病学实时监测设定下，针对报告延迟导致真实病例数难以即时估计的问题，提出了一种贝叶斯分层 nowcasting 模型。该模型采用灵活的参数形式刻画累积报告概率，并引入时变参数以捕捉报告行为的动态变化。时变参数被建模为随机过程，如随机游走以保证平滑性，或 Ornstein–Uhlenbeck (OU) 过程以引入均值回复特性。在 6 种模拟场景及真实数据中，该方法优于传统 nowcasting 方法，能显著改善动态报告环境下的预测精度并揭示实际病例的严重漏报。对您有用之处：该文提供了流行病学监测中的时序数据集与贝叶斯动态建模思路，可为您在流行病学应用方向提供数据集参考及潜在的结合因果推断的切入点。
- **关键技术**: `Bayesian hierarchical model`, `nowcasting`, `time-varying parameters`, `Ornstein-Uhlenbeck process`, `cumulative reporting probability`
- **为什么对您有用**: 匹配您的 secondary interest 流行病学应用，提供真实监测数据集与动态参数建模方法，可作为将因果推断或半参数理论引入流行病学 nowcasting 的应用切入点。

### 2. [10.1093/biomtc/ujag036](https://doi.org/10.1093/biomtc/ujag036) — OPERA: a new algorithm for patient stratification based on partially ordered risk factors
- **作者**: Yingzhou Liu, Menggang Yu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究医疗风险分层问题，设定为多个具有自然偏序结构的风险因子联合形成偏序集（poset），目标是基于此结构对患者进行分期分层。提出 OPERA（Ordering Poset Elements by Recursive Amalgamation）算法，通过递归合并偏序集元素构建分层方案，类似树方法可捕获高阶交互，但显式利用偏序结构实现更灵活的分期模式与更快的剪枝策略。方法不依赖回归模型参数假设，属于非参数分层框架，但未给出收敛率或渐近理论保证。在模拟研究与癌症分期数据（AJCC staging）上评估，显示偏序结构约束可提升分层效果与可解释性。该方法学新颖性主要体现在算法设计层面，理论深度有限。对您而言，癌症分期数据集对流行病学应用有参考价值，但偏序集递归合并与因果推断/效率理论/高维统计的核心兴趣关联较弱。
- **关键技术**: `partially ordered set (poset)`, `recursive amalgamation`, `tree-based pruning`, `risk stratification`, `high-order interaction detection`
- **为什么对您有用**: 流行病学方向的癌症分期数据集有一定参考价值，但算法本身（偏序集递归合并）与您 primary interest 中的因果推断、效率理论、高维统计等核心方向关联较弱，方法学迁移收益有限。

### 3. [10.1093/biomtc/ujag001](https://doi.org/10.1093/biomtc/ujag001) — Bayesian randomized basket trial design: a case study from the ultra-rare invasive mold infections
- **作者**: Yunhe Liu, Satrajit Roychoudhury, Wei Wei
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 针对超罕见侵袭性霉菌感染（IMIs）的随机非劣效篮式试验，提出一种贝叶斯稳健借力策略，以解决招募困难与病原体异质性导致的推断难题。方法核心包含两点：一是跨霉菌类型借力处理效应并惩罚异质性，二是利用外部数据增广对照组。该贝叶斯框架提升了处理效应估计精度，减少了对照组样本需求，并在模拟与真实数据中证明能在控制 family-wise type I error 的前提下显著提高功效。对您而言，虽然本文侧重贝叶斯试验设计，但其外部对照增广机制与因果推断中的数据融合及可移植性高度相关，且提供了流行病学罕见感染病的数据集参考。
- **关键技术**: `Bayesian borrowing`, `basket trial design`, `external control augmentation`, `family-wise type I error control`, `robust borrowing strategy`
- **为什么对您有用**: 利用外部数据增广对照组的机制与因果推断中的数据融合/可移植性方法论交叉，同时提供了流行病学罕见感染病的数据集与应用场景参考。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujag018](https://doi.org/10.1093/biomtc/ujag018) — Quantifying uncertainty in RNA velocity
- **作者**: Huizi Zhang, Natalia Bochkina, Sara Wade
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `minor`
- **摘要**: 在单细胞 RNA 测序的 RNA velocity 估计问题中，针对现有方法缺乏不确定性量化且假设不现实的问题，本文提出一个贝叶斯分层模型，设定时变转录率与非平凡初始条件。文章重点讨论了模型参数（尤其是较大潜在时间）的可识别性，弥补了以往研究的空白。推断方面，提出一种结合 MCMC 与 consensus 方法的算法以实现完全贝叶斯推断，提供校准良好的不确定性量化。模拟与小鼠胚胎干细胞数据验证了方法的有效性，估计结果与细胞周期一致。对您而言，其关于动态系统可识别性的讨论及 MCMC-consensus 计算算法在潜在变量建模与统计计算中有一定参考价值，但整体偏向生物应用，理论深度有限。
- **关键技术**: `Bayesian hierarchical model`, `parameter identifiability`, `MCMC`, `consensus Monte Carlo`, `latent time estimation`
- **为什么对您有用**: 本文探讨了动态系统参数的可识别性（与因果推断 identification 相关）并提出了结合 MCMC 与 consensus 的计算算法（与统计计算相关），但整体偏向生物统计应用，理论创新为 minor 级别。

### 2. [10.1093/biomtc/ujag043](https://doi.org/10.1093/biomtc/ujag043) — SIMBA–a Bayesian decision framework for the identification of optimal biomarker subgroups for cancer basket clinical trials
- **作者**: Shijie Yuan, Jiaxin Liu, Zhihua Gong, Xia Qin, Crystal Qin, Yuan Ji et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 在多适应症篮子临床试验（如胃癌、胰腺癌等）设定下，目标是识别对生物标志物靶向治疗响应率更高的最优患者亚群。提出的SIMBA方法基于贝叶斯分层模型，通过跨适应症的信息共享来定义正/负生物标志物亚组，并构建最优的go/no-go决策框架。核心技术依赖于贝叶斯层次先验以实现借用强度，以及基于后验概率的决策规则。模拟结果表明，SIMBA在识别获益亚群方面的操作特性优于现有方法。对您而言，该文属于贝叶斯临床试验设计，与您主攻的半参数/因果推断理论距离较远，方法学新颖度偏应用层面。
- **关键技术**: `Bayesian hierarchical model`, `basket trial design`, `subgroup identification`, `go/no-go decision rule`, `borrowing strength across indications`
- **为什么对您有用**: 该文属于贝叶斯临床试验设计，与您主攻的因果推断、半参数效率及高维理论距离较远；仅在流行病学应用中处理亚群异质性（类似条件平均处理效应 CATE 的识别思路）的思路上有极微弱的参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

