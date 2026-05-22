# Biometrics — Vol 82  Issue 1  ·  2026-05-21

- 共 42 篇 · Biometrics

## 因果推断  *(causal_inference, 13 篇)*

### 1. [10.1093/biomtc/ujag003](https://doi.org/10.1093/biomtc/ujag003) — Scalable and distributed individualized treatment rules for multicenter datasets
- **作者**: Nan Qiao, Wangcheng Li, Jingxiao Zhang, Canyi Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多中心数据与隐私约束设定下，目标是构建最优个体化治疗规则（ITR），克服经典元学习因局部估计偏差导致的次优性。提出卷积平滑加权支持向量机，其损失函数兼具凸性与平滑性。基于此设计多轮分布式学习程序，仅需在各中心间传递汇总统计量，在固定通信轮数内即可保证最优统计性能，避免汇聚个体级原始数据。开发高效坐标梯度下降算法，保证该优化问题至少具有线性收敛速率。仿真与多ICU脓毒症治疗数据验证了方法有效性。对您有用：该工作将分布式优化与因果推断ITR结合，其通信高效的坐标下降算法与凸平滑技巧可直接迁移至您在统计计算与因果推断交叉方向的算法设计中。
- **关键技术**: `individualized treatment rules`, `distributed learning`, `convolution-smoothed weighted SVM`, `coordinate gradient descent`, `communication-efficient inference`
- **为什么对您有用**: 结合了因果推断（ITR）与统计计算（分布式优化、坐标梯度下降、线性收敛），且包含多中心流行病学（脓毒症）应用；其通信高效的分布式算法设计对您在因果推断中的计算方法研究有直接参考价值。

### 2. [10.1093/biomtc/ujag017](https://doi.org/10.1093/biomtc/ujag017) — Semiparametric causal mediation analysis of cluster-randomized trials for indirect and spillover effects
- **作者**: Chao Cheng, Fan Li
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在整群随机试验（CRT）设定下，本文研究因果中介效应的半参数推断，目标估计量包括自然间接效应、个体中介效应及溢出中介效应（spillover mediation effect，即他人中介对自身结局的影响），现有方法多依赖强参数假设。作者为每种估计量推导了有效影响函数（EIF），并通过对 EIF 的精细参数化构建了双重稳健（doubly-robust）估计量。在干扰函数估计上，文章同时考虑了参数工作模型与数据自适应机器学习算法；当使用后者时，所得估计量达到半参数有效界。理论证明了估计量的双重稳健性与渐近正态性，模拟与真实 CRT 数据分析验证了其有限样本表现。对您有用：本文将半参数效率理论系统引入带干扰效应的中介分析，推导溢出效应 EIF 的思路及结合 ML 估计干扰函数的范式，可直接迁移至您关注的纵向/干扰设定下的中介或 IV 问题。
- **关键技术**: `efficient influence function`, `doubly-robust estimation`, `spillover mediation effect`, `data-adaptive machine learners`, `semiparametric efficiency bound`
- **为什么对您有用**: 直接命中您 primary interest 中的因果推断（中介分析）与效率理论（半参数有效界、debiased ML）；推导簇内溢出效应的 EIF 并结合 ML 估计干扰函数的范式，对处理纵向或干扰数据下的半参数推断具有直接参考价值。

### 3. [10.1093/biomtc/ujaf167](https://doi.org/10.1093/biomtc/ujaf167) — Learning optimal early decision treatment rules with multi-domain intermediate outcomes
- **作者**: Wenbo Fei, Yuan Chen, Zexi Cai, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向精准医疗设定下，目标是学习最优个体化治疗规则（ITR），但最终结局（如临床评估）往往滞后且难以获取，而多域中间结局（如患者自评）可作为早期代理。本文提出将多域中间观测推断的潜在状态加权组合为个性化复合结局，以此作为 ITR 学习的奖励信号，权重因人而异且保证与长期最终结局的一致性。方法核心是潜在状态推断（latent state inference）与个性化加权复合，替代传统仅依赖最终结局的 value-based ITR 学习。模拟表明该方法能更早识别无响应者并改善长期治疗结局；在重度抑郁症 RCT 数据上验证了有效性。对您而言，中间结局作为最终结局代理的思路与 proximal CI 中 negative-control proxy 的 identification 逻辑有概念呼应，且 ITR 估计的效率与半参数理论是您 efficiency theory 兴趣的潜在延伸方向。
- **关键技术**: `individualized treatment rules`, `latent state inference`, `personalized composite outcome`, `value-based ITR learning`, `intermediate outcome as proxy`
- **为什么对您有用**: 中间结局代理最终结局的思路与 proximal CI 的 proxy identification 逻辑相通，ITR 估计的效率问题可连接到 semiparametric efficiency bounds 兴趣；MDD RCT 数据集对流行病学应用有参考价值。

### 4. [10.1093/biomtc/ujaf168](https://doi.org/10.1093/biomtc/ujaf168) — An adaptive design for optimizing treatment assignment in randomized clinical trials
- **作者**: Wei Zhang, Zhiwei Zhang, Aiyi Liu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随机化临床试验中，本文研究如何在给定随机化机制类内优化处理分配以最大化处理效应估计的统计效率，关键假设涉及潜在结果在基线协变量下的条件方差函数。针对最优设计依赖未知条件方差函数的困境，提出一种多阶段自适应设计，允许在期中分析时基于累积信息动态修改处理分配概率。由于自适应机制改变了后续数据的分布，作者在估计阶段严格处理了这一影响，构建了一类一致且渐近正态（CAN）的处理效应估计量。在该估计量类中，作者识别出最有效估计量，并通过代入未知条件方差函数的估计来实现近似。模拟与中风试验真实数据表明，在先验信息匮乏时，该方法相比传统单阶段设计有显著的效率提升。对您有用：本文将自适应设计与效率理论深度结合，推导了自适应抽样下的最有效估计量，直接契合您在因果推断（RCT处理效应）与效率理论（CAN与有效界）方面的核心兴趣。
- **关键技术**: `adaptive randomization`, `potential outcomes`, `conditional variance estimation`, `semiparametric efficient estimator`, `asymptotic normality`
- **为什么对您有用**: 本文在自适应随机化下推导处理效应的最有效估计量，直接涉及您关注的因果推断（RCT处理效应）与效率理论（半参数有效界与CAN估计量），为自适应设计下的效率理论提供了严谨推导。

### 5. [10.1093/biomtc/ujag050](https://doi.org/10.1093/biomtc/ujag050) — A robust covariate-balancing method for estimating individualized treatment with censored data
- **作者**: Rujia Zheng, Wensheng Zhu, Xiaofan Guo
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在生存分析框架下，本文研究删失数据下最优个体化治疗方案（ITR）的估计问题，目标 estimand 为对比价值函数（contrast value function），关键正则假设涉及倾向得分模型与删失模型的一致性。提出两种稳健协变量平衡估计量，分别通过在权重中引入删失概率和删失时间的生存函数来实现协变量平衡；两种估计量均具有双重稳健性（doubly robust），即倾向得分模型或删失模型任一正确设定时估计量仍一致，且在标准正则条件下渐近正态（asymptotically normal）。大量模拟表明该方法优于仅依赖单一模型设定的现有方法；实证应用于中国农村高血压控制项目，识别最优用药方案以最大化预期生存时间，36 个月随访期内估计的最优方案提升了生存概率。对您而言，本文将协变量平衡从横截面扩展至删失生存数据并给出 DR 与 CAN 性质，可作为因果推断中处理删失/纵向数据的估计方法参考，同时高血压队列数据集对流行病学应用方向有数据集价值。
- **关键技术**: `covariate balancing`, `doubly robust estimation`, `contrast value function`, `censoring model`, `individualized treatment regime`, `survival analysis`
- **为什么对您有用**: 本文属于因果推断中个体化治疗方案的估计，双重稳健性与渐近正态性直接关联您的 efficiency theory 兴趣；高血压队列数据集对流行病学应用方向有数据集参考价值。

### 6. [10.1093/biomtc/ujaf174](https://doi.org/10.1093/biomtc/ujaf174) — Estimating optimal dynamic treatment regimes with Gaussian process emulation
- **作者**: Daniel Rodriguez Duque, David A Stephens, Erica E M Moodie
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断的动态治疗策略（DTR）设定下，目标是寻找最大化期望结果（value function）的最优策略，传统参数化方法（如边际结构模型）易受模型错设影响，而网格搜索计算代价高且估计不确定性大。本文提出利用高斯过程（GP）仿真优化方法来估计和搜索最优DTR，将带噪声的value function估计视作响应面进行非参数建模。GP优化通过获取函数在策略空间中自适应采样，相比网格搜索更高效地利用信息，并能有效处理多峰的value function。理论与模拟表明，考虑了估计噪声的GP方法比网格搜索产生更稳健的解，并在HIV治疗优化CD4细胞计数的流行病学数据中展示了应用。对您有用：该文将非参数GP引入纵向因果DTR的价值搜索，为处理复杂策略空间提供了计算与推断结合的新视角，直接契合您对因果推断（DTR/纵向）与统计计算交叉领域的兴趣。
- **关键技术**: `dynamic treatment regimes`, `Gaussian process emulation`, `value search estimation`, `marginal structural models`, `Bayesian optimization`
- **为什么对您有用**: 直接契合您对纵向因果推断（DTR）和统计计算的兴趣；GP仿真替代网格搜索为复杂策略空间的因果推断提供了计算高效的非参数方案，且包含流行病学应用数据集。

### 7. [10.1093/biomtc/ujag023](https://doi.org/10.1093/biomtc/ujag023) — Causal inference with misspecified network interference structure
- **作者**: Bar Weinstein, Daniel Nevo
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究网络干扰下因果效应估计中网络结构误设的后果与补救，目标 estimand 为干扰下的因果效应，关键假设是至少一个候选网络正确刻画了真实干扰结构。作者首先推导了网络误设导致的估计偏差上界，证明偏差与假定网络和真实网络诱导的暴露概率（exposure probabilities）之间的散度成正比。为解决此问题，提出了一种利用多个候选网络同时进行估计的新型鲁棒估计量。该估计量在至少一个候选网络正确时保持无偏，且无需事先知道哪个网络正确。模拟与社交网络实验数据验证了该方法降低误设偏差的有效性。对您有用：本文直接处理因果推断中干扰结构的误设问题，其“多候选网络鲁棒估计”的思路与您关注的 causal sensitivity analysis 及模型误设下的 identification 密切相关。
- **关键技术**: `network interference`, `exposure mapping`, `misspecification bias bound`, `robust estimation`, `multiple candidate networks`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断与敏感性分析，提供了网络干扰结构误设下的偏差界与鲁棒估计方法，思路可迁移至其他依赖图结构的因果模型。

### 8. [10.1093/biomtc/ujag034](https://doi.org/10.1093/biomtc/ujag034) — Distributed fusion <i>R</i> -learner of heterogeneous treatment effect using distributed medicaid data
- **作者**: Jinhong Li, Julie M Donohue, Lu Tang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多站点数据整合与隐私保护设定下，目标是估计条件平均处理效应（CATE），允许不同站点间的处理效应异质性且不共享个体数据。提出分布式融合 R-learner (DF R-learner)，通过数据驱动的融合惩罚（fusion penalty）聚合跨站点相似参数以提升估计精度。该方法利用置信分布（confidence distributions）在站点间传递信息，实现隐私保护下的高效通信。理论证明该分布式估计量相比基于集中式数据的 oracle 估计量无效率损失，达到半参数有效界。实证通过宾州多管理式医疗组织的 Medicaid 数据研究阿片类药物使用障碍的药物治疗。对您有用：该工作结合了因果推断CATE估计、半参数效率理论（无效率损失证明）与分布式计算，且提供了流行病学Medicaid真实数据集，直接契合您在因果推断、效率理论与流行病学应用上的多重兴趣。
- **关键技术**: `R-learner`, `confidence distribution`, `fusion penalty`, `distributed learning`, `CATE estimation`, `semiparametric efficiency`
- **为什么对您有用**: 结合了因果推断CATE估计与半参数效率理论（证明分布式下无效率损失），并涉及分布式统计计算；同时提供了流行病学Medicaid真实数据应用，直接契合您在因果推断、效率理论与流行病学应用上的兴趣。

### 9. [10.1093/biomtc/ujaf176](https://doi.org/10.1093/biomtc/ujaf176) — Long-term memory effects of an incremental blood pressure intervention in a mortal cohort
- **作者**: Maria Josefsson, Nina Karalija, Michael J Daniels
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究在存在死亡截断（truncation by death）的纵向队列中，降压干预对情景记忆的长期因果效应，目标参数包括病因效应（etiological effect，总体人群）与预后效应（prognostic effect，always-survivor 层）。方法上，作者基于扩展 G-formula 提出了针对 incremental threshold intervention 的贝叶斯半参数估计框架，并引入了一种利用纵向数据结构的稀疏诱导 Dirichlet 先验。模拟中与 Bayesian decision tree ensemble 方法进行了对比，展示了所提方法在有限样本下的性能。对 Betula 队列数据的分析发现，降压干预在所有年龄段均无显著的病因或预后效应。对您有用：该文将 incremental intervention 思路引入纵向死亡截断设定，扩展 G-formula 的识别策略与 always-survivor stratum 的分层效应估计可直接迁移到您关注的纵向因果推断与流行病学应用中。
- **关键技术**: `incremental threshold intervention`, `extended G-formula`, `truncation by death`, `Bayesian semi-parametric estimation`, `sparsity-inducing Dirichlet prior`, `always-survivor stratum`
- **为什么对您有用**: 直接连接您 primary interest 中的纵向因果推断（incremental intervention + G-formula 识别）与 secondary interest 中的流行病学应用（Betula 队列、死亡截断下的因果效应分层），贝叶斯半参数框架与稀疏 Dirichlet 先验对纵向因果的 computing 实现亦有参考价值。

### 10. [10.1093/biomtc/ujag030](https://doi.org/10.1093/biomtc/ujag030) — Handling incomplete outcomes and covariates in cluster-randomized trials: doubly robust estimation, efficiency considerations, and sensitivity analysis
- **作者**: Bingkai Wang, Fan Li, Rui Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在整群随机试验（CRT）设定下，目标是在结局、协变量及群组人口规模均可能缺失的情况下识别并估计平均因果效应（ATE）。本文提出一种双重稳健（doubly robust）估计量，同时处理结局的随机缺失（MAR）、协变量无约束缺失以及群组规模的均匀抽样缺失。为提升精度，作者通过指定最优权重、利用机器学习以及建模处理分配机制来逼近半参数有效界。此外，针对缺失数据假设可能违背的问题，提出了专门针对 CRT 的敏感性分析框架。理论上证明了估计量的双重稳健性与渐近正态性，模拟与实证数据验证了方法的有效性。对您有用：该文将双重稳健估计与效率优化结合，且其针对 CRT 缺失机制的敏感性分析框架可直接迁移至您关注的因果推断敏感性分析及流行病学应用中。
- **关键技术**: `doubly robust estimation`, `missing data sensitivity analysis`, `semiparametric efficiency`, `optimal weighting`, `cluster-randomized trials`
- **为什么对您有用**: 直接涉及因果推断中的双重稳健估计与效率理论（最优权重逼近半参数有效界），并提供了针对 CRT 缺失机制的敏感性分析框架，与您主攻的因果推断敏感性分析及流行病学应用高度契合。

### 11. [10.1093/biomtc/ujag022](https://doi.org/10.1093/biomtc/ujag022) — Bias mitigation in matched observational studies with continuous treatments: calipered non-bipartite matching and bias-corrected estimation and inference
- **作者**: Anthony Frazier, Siyu Heng, Wen Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在连续处理（continuous treatment）的匹配观察性研究中，非精确协变量匹配导致的残余协变量不平衡会引入严重因果推断偏差，本文针对此问题提出覆盖匹配、估计与推断三阶段的系统性偏差校正框架。匹配阶段提出融合协变量距离与处理剂量信息的 caliper，用于非二部图匹配（non-bipartite matching）以优化下游处理效应估计。估计与推断阶段引入偏差校正的 Neyman 估计量及相应的偏差校正方差估计量，校正因 inexact matching 产生的系统性偏移。数值模拟与 COVID-19 社交距离对病例数影响的再分析均表明，忽略 inexact matching 偏差的传统做法偏差显著，而所提框架有效消除该偏差。对您研究连续处理因果推断（dose-response）中的匹配设计与偏差校正有直接方法借鉴价值，偏差校正 Neyman 估计量的思路也可迁移至其他 semiparametric 场景。
- **关键技术**: `non-bipartite matching`, `caliper design with dose information`, `bias-corrected Neyman estimator`, `bias-corrected variance estimator`, `continuous treatment dose-response`
- **为什么对您有用**: 直接推进连续处理因果推断中的匹配与偏差校正方法，对您在 causal inference 中处理 continuous treatment / dose-response 的估计与推断有方法迁移价值，偏差校正 Neyman 估计量的构造思路也可借鉴至 semiparametric efficiency 场景。

### 12. [10.1093/biomtc/ujaf173](https://doi.org/10.1093/biomtc/ujaf173) — Estimating the causal effect of redlining on present-day air pollution
- **作者**: Xiaodan Zhou, Shu Yang, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在空间因果推断设定下，研究 1930 年代红线政策对当代空气污染（PM2.5 和 NO2）的长期因果效应，核心挑战在于缺乏处理前协变量导致的未测量混杂。作者提出一种空间与非空间潜因子框架，利用 1940 年人口普查中的失业率、房租和黑人比例作为代理变量，重构处理前的潜在社会经济地位。该方法在较宽泛的假设下实现了因果效应的识别，并采用贝叶斯 MCMC 进行不确定性量化。实证结果表明，红线社区面临显著更高的 NO2 浓度，而 PM2.5 差异相对较弱。对您而言，该文将代理变量处理未测量混杂的思路应用于空间流行病学数据，与您关注的 proximal CI 及流行病学因果应用直接相关，提供了潜因子模型替代经典 negative control 的实证案例。
- **关键技术**: `spatial causal inference`, `latent factor model`, `proxy variables for unmeasured confounding`, `Bayesian MCMC`, `causal identification`
- **为什么对您有用**: 该文使用代理变量和潜因子模型处理未测量混杂，与您关注的 proximal CI 思路相通，同时提供了流行病学/环境健康领域的真实空间因果推断数据集和分析范式。

### 13. [10.1093/biomtc/ujag009](https://doi.org/10.1093/biomtc/ujag009) — Repeated inclusion cluster randomized trials: a new class of designs for assessing group-level interventions
- **作者**: Jessica Kasza, Kelsey L Grantham, Rhys Bowden, Brennan C Kahan, Andrew B Forbes
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的整群随机试验设计——重复纳入整群随机试验，允许部分群组在同一试验中被连续多次随机分配，假设干预效应在重复纳入中恒定。通过方差分解分析了组内相关结构对处理效应估计量精度的影响，证明在总测量数相同时，增加组内比较次数能提升检验效能，且其效能不低于无重复随机化的传统设计。理论结果表明该设计在群组招募困难时能有效减少招募需求并维持或提升统计效能。对您可能有用：虽然本文侧重试验设计而非观察性因果推断，但其对群组水平重复测量下处理效应估计量方差与效能的解析推导，可为纵向因果推断或流行病学整群试验的样本量规划提供参考。
- **关键技术**: `cluster randomized trial`, `re-randomization design`, `treatment effect estimator`, `power analysis`, `within-cluster correlation`, `variance decomposition`
- **为什么对您有用**: 涉及整群随机试验中处理效应估计量的方差分解与检验效能分析，与因果推断中的纵向设计及假设检验有一定交叉，可为流行病学应用中的整群试验设计提供理论参考，但方法学深度偏向传统试验设计而非半参数/高维理论。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biomtc/ujag035](https://doi.org/10.1093/biomtc/ujag035) — Ultra-high-dimensional threshold selection for quantile feature screening with false discovery rate error rate control: a case study on high blood pressure analysis
- **作者**: Saidat Abidemi Sanni, Yan Yu, Zhigen Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在超高维特征筛选设定下，本研究针对分位数特征筛选中的阈值选择问题，目标是在控制错误发现率（FDR）的前提下识别重要遗传风险因子。提出了一种新的分位数镜像（QM）方法，利用对称 QM 统计量估计 FDR，实现数据自适应的阈值选择。方法结合多重数据分割以增强结果稳定性，允许不同分位数采用不同阈值，并进一步提出 QREDS 及 Hard Threshold with QREDS 筛选程序。理论上证明了在适当条件下所提程序能渐近控制 FDR。实证分析应用于 Framingham Heart Study 数据，验证了已知高血压遗传特征并发现新风险因子。该文将 FDR 控制思想引入超高维分位数筛选，对您在**高维统计**变量筛选与**假设检验**交叉方向有方法论参考，且 Framingham 数据集对**流行病学**应用有直接价值。
- **关键技术**: `quantile feature screening`, `false discovery rate control`, `mirror statistic`, `multiple data splitting`, `ultra-high-dimensional variable selection`
- **为什么对您有用**: 结合了您在**高维统计**（超高维筛选）和**假设检验**（FDR 控制）的兴趣，同时提供了 Framingham Heart Study 这一经典**流行病学**数据集的应用范例，方法与数据均有借鉴价值。

### 2. [10.1093/biomtc/ujag039](https://doi.org/10.1093/biomtc/ujag039) — Sparse robust discriminant analysis for high-dimensional and heavy-tailed data
- **作者**: Weijian Huang, Qing Mai, Jing Zeng
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 在高维重尾数据设定下，传统稀疏线性判别分析（LDA）常因轻尾假设失效，本文在椭圆等高判别分析（EDA）半参数模型下研究稳健分类，目标是最小化不平衡数据下的 balanced rate。作者识别出捕获预测信息以达到最低 balanced rate 的内在降维子空间，并据此提出稳健高维分类器：先通过子空间投影降维，再对降维数据进行预测。理论上，在预测变量仅满足有限四阶矩的弱正则条件下，该方法同时实现了子空间估计、变量选择与预测准确率的一致性。数值模拟与三个医学实际数据（肺癌与白血病基因表达）验证了其相对现有方法的优越性。对您有用：该文在 EDA 半参数框架下放松了矩条件，其高维子空间估计与变量选择的双重一致性理论，对您研究高维统计与半参数理论的交叉有直接参考价值。
- **关键技术**: `sparse linear discriminant analysis`, `elliptically contoured discriminant analysis`, `sufficient dimension reduction`, `balanced rate`, `finite fourth-moment condition`, `subspace estimation consistency`
- **为什么对您有用**: 涉及高维统计中的稀疏判别与半参数 EDA 模型，放松了传统的轻尾假设（仅需四阶矩），其子空间估计与变量选择的一致性理论对您的高维统计与半参数理论兴趣有直接参考价值；同时医学数据应用对流行病学方向有数据集参考意义。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1093/biomtc/ujaf175](https://doi.org/10.1093/biomtc/ujaf175) — Multiple-index interaction models to accommodate exposure grouping in environmental mixtures
- **作者**: Myeonggyun Lee, Mengling Liu, Shanshan Zhao
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在环境混合物（environmental mixtures）分析中，目标是在暴露变量按生物特征分组的设定下，估计各组整体效应及组间交互作用对健康结局的影响，关键假设是暴露可通过组内线性组合（index）降维且组间存在非线性交互。本文提出半参数多指标交互模型（MIIM），将高维暴露通过组级 index 汇总以克服维数灾难，同时允许组 index 间的非线性效应与交互，并支持连续、二值及生存结局。估计方面采用 profile/sieve 类方法处理多指标结构，模拟显示在高维相关暴露下 MIIM 在偏差和方差上优于忽略分组的方法，且能识别组内关键贡献变量。实证分析基于 NHANES 数据考察三类持久性有机污染物对白细胞端粒长度的影响。该文将分组先验融入半参数多指标模型，对您在半参数理论（多指标模型的 efficiency 与 estimation）及流行病学应用（NHANES 数据集与暴露混合物建模）两个方向均有参考价值。
- **关键技术**: `semiparametric multiple-index model`, `group-level index dimension reduction`, `nonlinear interaction via indices`, `sieve estimation`, `environmental mixtures analysis`
- **为什么对您有用**: 半参数多指标模型直接属于您 primary interest 中的 semiparametric theory；同时 NHANES 流行病学数据集和暴露混合物建模连接您 secondary interest 中的 epidemiology，可借鉴其分组降维思路迁移至因果推断中的多暴露 mediation / IV 设定。

### 2. [10.1093/biomtc/ujag044](https://doi.org/10.1093/biomtc/ujag044) — Variable selection in functional linear Cox model
- **作者**: Yuanzhen Yue, Stella Self, Yichao Wu, Jiajia Zhang, Rahul Ghosal
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 functional linear Cox 模型设定下，研究基线多函数及标量协变量的变量选择问题，目标是同时实现函数系数的光滑估计与稀疏选择。方法采用基于样条的半参数估计逼近函数系数，并引入 group minimax concave penalty (MCP) 将光滑性与稀疏性整合至目标函数中。优化求解使用高效的 group descent 算法，并提供了平滑与稀疏惩罚参数的自动选择程序。模拟研究表明该方法在变量选择和估计精度上表现良好；实证分析 NHANES 队列数据，识别出与全因死亡率相关的体力活动时间分布模式。对您而言，该文展示了样条半参数估计与高维 group penalty 在生存分析中的结合，其算法实现与流行病学数据集对 semiparametric theory 及 epi 应用有参考价值。
- **关键技术**: `functional linear Cox model`, `spline-based semiparametric estimation`, `group minimax concave penalty`, `group descent algorithm`, `time-to-event data`
- **为什么对您有用**: 该文将样条半参数估计与高维 group MCP 惩罚结合，对您在 semiparametric theory 和 high-dimensional variable selection 交叉方向有方法学借鉴；同时 NHANES 队列数据及生存分析框架对 epidemiology secondary interest 提供了真实数据应用范例。

### 3. [10.1093/biomtc/ujag040](https://doi.org/10.1093/biomtc/ujag040) — Reduced varying coefficient models for regional quantile regression with multiple responses
- **作者**: Woorim Jung, Seyoung Park, Hyokyoung G Hong, Eun Ryung Lee
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在高维设定下研究多响应变量的区域分位回归问题，目标是在变系数模型框架下估计随时间指数变化的分位系数矩阵。方法上，对多变量变系数矩阵施加低秩结构，通过主成分函数实现降维与可解释性；同时引入 KNN-fused LASSO 惩罚项，以捕捉共享的动态模式并识别主成分中的潜在聚类。该框架将多响应的维度灾难转化为低秩子空间的估计问题，结合图结构惩罚实现系数的局部平滑与聚类。模拟表明，该方法在高维场景下提供一致的估计与鲁棒性能，实证分析使用两个健康数据集揭示了预测变量与多相关结果间复杂的、分位数特异的关联。对您有用：该文将低秩近似与 fused LASSO 结合处理高维非参数变系数，对您关注的高维统计惩罚方法及流行病学健康数据应用有直接参考价值。
- **关键技术**: `varying coefficient model`, `regional quantile regression`, `low-rank approximation`, `KNN-fused LASSO`, `principal component functions`
- **为什么对您有用**: 结合了高维惩罚回归与变系数半参数模型，并在流行病学健康数据上实证，对您关注的高维统计计算及流行病学应用有参考价值。

### 4. [10.1093/biomtc/ujag051](https://doi.org/10.1093/biomtc/ujag051) — Simultaneous clustering and estimation of additive shape invariant models for recurrent event data
- **作者**: Zitong Zhang, Shizhe Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在神经科学随机化干预实验中，目标是在观测数据为多刺激响应叠加且各神经元响应延迟未知的设定下，识别具有异质刺激响应的神经元聚类并估计其响应曲线。本文提出additive shape invariant model，同时容纳多聚类、可加成分与未知time-shift，并建立模型参数的可识别性条件，为实验设计提供理论指导。方法通过simultaneous clustering与estimation联合求解，处理recurrent event data中的响应叠加与延迟对齐问题。模拟研究验证了算法性质，应用于小鼠视觉辨别任务的Neuropixels spike train数据，识别出三个具有异质响应模式（包括刺激特异性活动与响应时间变异性）的功能神经元群。对您而言，shape invariant model的identifiability理论与semiparametric theory直接相关，且随机化干预下的异质响应估计与causal inference中heterogeneous treatment effect的设定有方法迁移潜力。
- **关键技术**: `additive shape invariant model`, `simultaneous clustering and estimation`, `identifiability conditions`, `time-shift alignment`, `recurrent event data`
- **为什么对您有用**: shape invariant model的可识别性理论属于semiparametric theory范畴；随机化干预下多聚类响应估计与causal inference中heterogeneous treatment effect estimation的设定有方法迁移潜力，聚类结构也为longitudinal/mediation分析中的异质性建模提供思路。

### 5. [10.1093/biomtc/ujag045](https://doi.org/10.1093/biomtc/ujag045) — DNN-based semiparametric AFT model for integrating genomic and pathological imaging data in cancer prognosis
- **作者**: Jingmao Li, Qingzhao Zhang, Shuangge Ma
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在癌症预后设定下提出一种基于深度神经网络的半参数加速失效时间（AFT）模型，整合高维基因组（参数部分）与病理影像（非参数部分）数据。对高维基因组变量施加参数假定与稀疏惩罚以保证可解释性，对高维影像特征利用 DNN 估计非参数效应，并在 DNN 第一层权重施加 group penalization 以实现变量选择。理论上，文章严格建立了参数与非参数部分的渐近选择一致性、估计一致性及正态性。模拟与 TCGA 肺癌真实数据分析表明该方法具有竞争性的预测与选择表现。对您有用：该文将 DNN 嵌入半参数 AFT 框架并给出严苛的高维渐近理论，直接契合您对半参数理论与高维统计的兴趣，其 DNN 第一层 group penalization 的变量选择机制也可为高维非参数计算提供参考。
- **关键技术**: `semiparametric AFT model`, `deep neural networks`, `group penalization`, `high-dimensional variable selection`, `asymptotic normality`, `survival analysis`
- **为什么对您有用**: 直接契合您对半参数理论与高维统计的兴趣；文章在 DNN 非参数估计中结合 group penalization 并严格证明高维渐近性质（一致性、正态性），为高维半参数模型的推断提供了新理论支撑。

### 6. [10.1093/biomtc/ujaf177](https://doi.org/10.1093/biomtc/ujaf177) — Inhomogeneous mark correlation functions for general marked point processes
- **作者**: Mehdi Moradi, Matthias Eckardt
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在一般空间标记点过程设定下，本文研究如何在存在空间非齐次性时准确捕捉标记关联与变异。作者提出了一类非齐次标记相关函数，量化成对空间距离下标记的平均变异/关联程度，并发展了相应的非参数估计量。模拟研究表明，传统方法在空间非齐次性下表现不佳，而所提估计量能准确识别标记关联的正负性及有效空间范围。此外，空间强度估计方式的差异对非齐次标记相关函数的经验偏差和方差影响可忽略。实证分析两类森林生态系统数据进一步验证了该方法在揭示树木生长模式上的优势。对您而言，本文虽属空间统计，但其非参数估计量的构造与偏差/方差分析思路，可为非参数理论方向提供边缘参考，但与因果推断或效率理论等核心兴趣距离较远。
- **关键技术**: `inhomogeneous mark correlation function`, `nonparametric estimation`, `spatial point processes`, `intensity estimation`
- **为什么对您有用**: 本文核心是空间点过程的非参数估计，与您的主要兴趣（因果推断、高维/效率理论）直接关联较弱，仅在非参数估计构造与偏差分析层面有极微弱的参考价值。

### 7. [10.1093/biomtc/ujag002](https://doi.org/10.1093/biomtc/ujag002) — Quasi-likelihood estimation for semiparametric circular regression models
- **作者**: Anna Gottard, Andrea Meilán-Vila, Agnese Panzera
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对圆形响应变量（如方向角）的回归问题，本文提出一种半参数圆形回归模型，设定参数与非参数成分可同时包含线性与圆形协变量，且不假设误差项的具体参数分布。核心估计方法采用圆形准似然（quasi-likelihood）函数，避免了未知分布的完全参数化假设。计算上使用 backfitting 算法迭代拟合参数与非参数成分。理论上推导了所得估计量的渐近性质。模拟与柳莺鸟迁徙方向的基因组效应实证展示了方法的有限样本表现与实际应用价值。对您而言，本文的半参数 backfitting 渐近理论与准似然构造思路可作参考，但圆形数据的特定设定与您关注的高维/因果/效率界主线距离较远。
- **关键技术**: `semiparametric circular regression`, `quasi-likelihood`, `backfitting algorithm`, `circular data analysis`, `asymptotic properties`
- **为什么对您有用**: 涉及半参数理论与 backfitting 算法（属于您的 primary interest），但针对的是圆形数据这一特殊设定，与您核心关注的高维/因果/效率界距离较远，主要提供特定数据类型下半参数估计的参考视角。

### 8. [10.1093/biomtc/ujaf171](https://doi.org/10.1093/biomtc/ujaf171) — Semiparametric piecewise accelerated failure time model for the analysis of immune-oncology clinical trials
- **作者**: Hisato Sunami, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在免疫肿瘤临床试验的生存分析设定下，针对治疗存在滞后时间（lag-time）导致比例风险假设失效的问题，本文目标是识别不受益患者并估计分段处理效应。作者提出半参数分段加速失效时间（piecewise AFT）模型，并基于半参数极大似然方法构建推断程序。该模型将滞后期前后的生存机制解耦，在统一框架下同时提供总体处理效应总结与低受益患者的协变量特征识别。数值实验表明各参数估计具有极小偏差，真实数据分析展示了免疫治疗效应评估及患者异质性刻画。对您可能有用：该文是半参数极大似然理论在复杂生存模型中的典型应用，可为您在半参数效率理论或流行病学队列生存分析中的方法开发提供模型设定与推断思路。
- **关键技术**: `semiparametric maximum likelihood estimation`, `piecewise accelerated failure time model`, `lag-time identification`, `survival analysis`, `treatment heterogeneity`
- **为什么对您有用**: 涉及半参数极大似然推断，属于您关注的半参数理论范畴；其应用场景（免疫肿瘤临床生存分析）与流行病学应用高度相关，可提供生存数据下处理效应异质性识别的模型框架。

## 效率理论 / Debiased ML  *(efficiency_dml, 3 篇)*

### 1. [10.1093/biomtc/ujaf166](https://doi.org/10.1093/biomtc/ujaf166) — Jointly modeling multiple endpoints for efficient treatment effect estimation in randomized controlled trials
- **作者**: Jack M Wolf, Joseph S Koopmeiners, David M Vock
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随机对照试验（RCT）设定下，目标是利用次要终点信息提升主要终点处理效应（ATE）的估计效率，关键假设为主要与次要终点存在可联合建模的分布结构。提出一种基于多终点联合建模的 ATE 估计量：当联合模型正确设定时，该估计量相比标准估计量获得效率提升；通过引入模型平均（model averaging）机制，确保在模型误设时估计量仍具备一致性与鲁棒性。实证应用于烟草监管科学数据（极低尼古丁香烟对黑人戒烟率的影响），该方法使标准误降低约 27%。对您有用：该工作直接关联您对效率理论的兴趣，展示了在 RCT 中利用辅助变量（次要终点）逼近半参数效率边界的实用策略，且模型平均思路对处理 nuisance model 误设具有参考价值。
- **关键技术**: `joint modeling of multiple endpoints`, `model averaging`, `efficient treatment effect estimation`, `robustness to model misspecification`, `randomized controlled trials`
- **为什么对您有用**: 直接关联您在因果推断和效率理论方面的兴趣，展示了如何在 RCT 中利用次要终点辅助信息提升 ATE 估计效率，并通过模型平均保证误设下的鲁棒性，方法可迁移至其他多终点或辅助变量的因果推断场景。

### 2. [10.1093/biomtc/ujag047](https://doi.org/10.1093/biomtc/ujag047) — Nonparametric ANCOVA for longitudinal outcomes in a randomized clinical trial
- **作者**: Rex Shen, Xiaotong Jiang, Changyu Shen, Lu Tian
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随机对照试验的纵向数据设定下，本文研究平均处理效应（ATE）的估计，且不假设混合效应模型正确设定（非参数 ANCOVA）。传统纵向 ANCOVA 依赖参数模型设定，本文指出最优协变量调整依赖于纵向结局给定基线协变量的未知条件期望。为此，作者提出利用 cross-fitting 程序对该条件期望进行非参数估计，以指导 ANCOVA 的协变量调整构造。该方法避免了模型误设带来的效率损失，理论上可证明其达到最优精度（逼近半参数效率界）。数值实验与理论推导均显示其优于传统参数 ANCOVA。对您而言，该文将 cross-fitting 与半参数效率理论结合应用于纵向因果推断，对研究 debiased ML 在纵向数据中的理论性质有直接参考价值。
- **关键技术**: `nonparametric ANCOVA`, `cross-fitting`, `conditional expectation estimation`, `semiparametric efficiency bound`, `longitudinal RCT`
- **为什么对您有用**: 直接连接到您的 primary interest 中的因果推断（纵向 RCT 的 ATE 估计）与效率理论（最优协变量调整逼近半参数效率界）；cross-fitting 的使用对您关注 debiased ML 在纵向数据中的理论性质有借鉴意义。

### 3. [10.1093/biomtc/ujag041](https://doi.org/10.1093/biomtc/ujag041) — Generalized entropy calibration for analyzing voluntary survey data
- **作者**: Yonghyun Kwon, Jae Kwang Kim, Yumou Qiu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在可忽略抽样机制假设下，本文研究自愿调查数据的选择偏差校正问题，目标是构建统一的校准加权估计量。提出广义熵校准方法，并严格证明了广义校准加权与其对偶回归估计之间的等价关系。该对偶关系是识别隐含回归模型和开发校准加权模型选择准则的关键。进一步，在重要研究变量的线性回归模型可用时，提出两步校准法以平滑权重并提升估计效率。理论上证明了所提估计量具有双重稳健性与局部有效性。对您有用：双重稳健与局部有效性属于您关注的效率理论核心，且校准加权与因果推断中的 IPW/处理加权高度同构，其对偶视角与模型选择策略可直接迁移至缺失数据与因果推断的半参数估计中。
- **关键技术**: `generalized entropy calibration`, `calibration weighting`, `dual regression estimation`, `double robustness`, `local efficiency`, `two-step calibration`
- **为什么对您有用**: 本文的核心贡献在于校准加权的对偶理论与双重稳健/局部有效估计，这与您关注的效率理论直接相关，且校准加权与因果推断中的 IPW 方法高度同构，其模型选择策略对处理缺失数据与因果推断的半参数估计具有直接迁移价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biomtc/ujag042](https://doi.org/10.1093/biomtc/ujag042) — Inference for microbe–metabolite association networks using a latent graph model
- **作者**: Jing Ma
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在微生物-代谢物关联网络推断中，传统 FDR 控制方法（如 BH）假设 p 值弱相依，在存在密集关联模块（强相依结构）时检验功效低下。本文提出一种基于潜在图模型的推断程序，通过二分随机块模型刻画网络潜在模块结构以增强检验功效。作者采用变分 EM 算法估计模型参数，并将学习到的图结构融入多重检验过程以实现 FDR 控制。该方法同时提供微生物与代谢物的模块聚类结果，便于生物学解释。模拟与细菌性阴道病数据应用表明，该方法在严格控制 FDR 的同时显著提升了网络恢复功效。对您有用：该文将潜在图结构融入多重假设检验的思路，对您在假设检验方向处理强相依 p 值或高维网络推断有方法论借鉴，且其流行病学数据应用可作参考。
- **关键技术**: `false discovery rate control`, `bipartite stochastic block model`, `variational EM algorithm`, `multiple testing under dependence`, `latent graph model`
- **为什么对您有用**: 该文将潜在图结构融入多重假设检验以处理强相依 p 值，直接契合您在假设检验方向的兴趣；同时其流行病学（细菌性阴道病）数据应用对您在流行病学领域的关联/因果推断工作具有数据集与分析流程参考价值。

### 2. [10.1093/biomtc/ujag052](https://doi.org/10.1093/biomtc/ujag052) — Rank-adaptive covariance testing with applications to genomics and neuroimaging
- **作者**: David Veitch, Yinqiu He, Jun Young Park
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维两样本协方差矩阵检验中，当信号弱分散且源于低秩结构差异时，传统方法常面临功效不足的问题。本文引入 Ky-Fan(k) 范数（前 k 个奇异值之和）来捕捉此类低秩信号，并研究其检验性质。作者提出 rank-adaptive covariance testing (RACT) 方法，通过自适应选择秩 k 以最大化检验功效。推断环节采用置换检验，确保了精确的第一类错误控制，规避了高维下渐近分布的复杂推导。模拟与肺癌基因网络及 DTI 实证表明 RACT 在低秩信号下功效显著提升。对您有用：直接契合您对高维假设检验与随机矩阵/低秩结构的兴趣，且置换法思路对高维推断计算有参考价值。
- **关键技术**: `Ky-Fan(k) norm`, `two-sample covariance testing`, `low-rank structure`, `permutation test`, `rank adaptation`, `singular value`
- **为什么对您有用**: 直接契合您对高维假设检验与随机矩阵理论（奇异值/低秩结构）的交叉兴趣；Ky-Fan范数与置换检验的结合为高维推断提供了计算可行且有限样本精确的思路。

### 3. [10.1093/biomtc/ujag048](https://doi.org/10.1093/biomtc/ujag048) — Making all pairwise comparisons in multi-arm clinical trials without control treatment
- **作者**: T Burnett, T Jaki
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在无对照组的多臂临床试验设定下，本文研究如何对所有实验组进行两两比较的假设检验问题，关键假设为各组独立且需严格控制族错误率（FWER）。作者提出了基于闭包检验原理的精确多重检验方法，通过利用检验统计量间的相关性结构，避免了 Bonferroni 校正的保守性，使得 FWER 精确控制在目标水平 α。该方法在提升检验功效的同时，被证明可自然扩展至多阶段自适应试验设计（如组合检验框架）。理论与模拟结果表明，该程序在保持精确一类错误控制的前提下，相比传统保守方法具有显著的功率优势。对您可能有用：本文的闭包检验构造与精确误差控制思路，可直接迁移到您关注的假设检验子方向，特别是在多重比较或自适应推断中如何利用相关性结构放松保守性。
- **关键技术**: `closed testing procedure`, `familywise error rate (FWER) control`, `pairwise comparisons`, `adaptive trial design`, `exact test`
- **为什么对您有用**: 本文聚焦多重假设检验的精确误差控制与自适应设计，直接对应您在数学统计（假设检验）方向的兴趣；其利用相关性结构避免 Bonferroni 保守性的思路，对复杂结构下的多重推断具有方法学借鉴价值。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biomtc/ujag016](https://doi.org/10.1093/biomtc/ujag016) — Estimation of mixed-effects ordinary differential equation models linear in the parameters
- **作者**: Oleksandr Laskorunskyi, Snigdhansu Chatterjee, Itai Dattner
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在参数线性的混合效应常微分方程（ODE）设定下，本文目标是估计含嵌套与交叉结构的固定及随机效应。提出 Direct Integral Mixed-Effects (DIME) 方法，利用参数与状态的可分离性，通过直接积分将非线性ODE重构为线性混合效应模型（LMM）。该重构使得标准LMM推断工具（置信区间、模型选择）直接可用，并给出参数估计的一致性与渐近正态性理论保证。模拟表明 DIME 在小样本下方差分量估计的覆盖概率优于现有非线性方法，实证分析（人口与气象数据）验证了其灵活性。对您有用：该文将复杂非线性ODE转化为LMM的计算技巧，对统计计算（数值方法与算法）和非线性/半参数推断有方法论借鉴意义。
- **关键技术**: `mixed-effects ODE`, `direct integral method`, `linear mixed-effects model`, `parameter-state separability`, `asymptotic normality`
- **为什么对您有用**: 将非线性ODE转化为LMM的算法重构思路，对您在统计计算（数值方法与算法）和半参数推断方面的研究有直接的技巧借鉴价值。

### 2. [10.1093/biomtc/ujaf169](https://doi.org/10.1093/biomtc/ujaf169) — Optimal design of dynamic experiments for scalar-on-function linear models with application to a biopharmaceutical study
- **作者**: Damianos Michaelides, Maria Adamou, David C Woods, Antony M Overstall
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 scalar-on-function 线性模型设定下，本文针对变量取值为函数（profile variables）的动态实验，提出了一种贝叶斯最优实验设计（OED）框架。核心机制是通过基展开（basis expansion）将无限维的函数型变量有限维化，使得设计空间可被参数化搜索。在此基础上，结合贝叶斯设计准则和坐标交换算法寻找最优的函数组合设计。该方法能够显式控制函数型变量和模型的复杂度，避免过拟合。实证部分将该方法应用于 Ambr250 模块化生物反应器系统的动态投料策略优化。对您而言，虽然该文核心在实验设计而非因果或效率理论，但其基展开处理函数型协变量的技巧和优化算法对统计计算与半参数建模有一定参考价值。
- **关键技术**: `Bayesian optimal design`, `scalar-on-function regression`, `basis expansion`, `functional data analysis`, `coordinate exchange algorithm`
- **为什么对您有用**: 涉及函数型协变量的基展开表示与统计计算优化，与您在统计计算和半参数建模方面的兴趣有弱关联，但核心属于实验设计领域，与因果推断或效率理论距离较远。

### 3. [10.1093/biomtc/ujag013](https://doi.org/10.1093/biomtc/ujag013) — Non-boundary covariance matrix estimation in generalized linear mixed effects models using data augmentation priors
- **作者**: Tina Košuta, Erik Langerholc, Rok Blagus
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在广义线性混合效应模型 (GLMM) 中，ML 估计随机效应协方差矩阵常出现边界估计（奇异矩阵），导致数值不稳定与推断失效；本文在正则性假设下引入基于条件共轭先验的惩罚似然方法来规避此问题。核心机制：对协方差/精度矩阵施加条件共轭先验导出的惩罚项，并将惩罚表示为伪观测数据 (pseudo-observations)，使惩罚似然可在现有 ML 软件中通过数据增强直接实现。构造伪观测是关键技术难点——其似然贡献须与惩罚函数形式精确匹配且仅依赖随机效应协方差/精度矩阵。此外提出完全数据驱动的惩罚参数选择程序，无需先验指定。模拟与真实数据表明，所提方法在边界估计常见场景下优于现有方法，有效改善协方差矩阵估计。对您而言，伪观测数据增强技巧作为统计计算中利用已有软件实现惩罚估计的通用范式，可能在层级因果模型或纵向数据的数值实现中有迁移价值。
- **关键技术**: `data augmentation prior`, `conditionally conjugate prior`, `pseudo-observation construction`, `penalized maximum likelihood`, `GLMM boundary estimation`, `data-driven penalty selection`
- **为什么对您有用**: 连接到统计计算方向——伪观测数据增强技巧为在已有 ML 软件中实现惩罚估计提供了通用计算范式，可能在层级因果模型（如纵向因果推断中的 mixed effects 设定）的数值实现中有迁移价值；边界估计问题本身也是数学统计中参数空间边界推断的经典难题。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biomtc/ujag020](https://doi.org/10.1093/biomtc/ujag020) — Bayesian nowcasting for delay adjustments using time-varying parametric functions of cumulative reporting probability
- **作者**: Erick A Chacón-Montalván, Yang Xiao, Paula Moraga
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究流行病学监测中报告延迟导致的实时病例数估计（nowcasting）问题，目标是在报告概率时变的设定下估计真实病例数。提出贝叶斯分层模型，用灵活参数形式刻画累积报告比例，并通过随机游走或 Ornstein–Uhlenbeck 过程对报告行为的时间变异进行建模，前者保证平滑性、后者引入均值回复。模拟涵盖 6 种场景（含完全/非完全报告），所提模型优于传统 nowcasting 方法；真实数据应用显示在显著延迟下仍可给出可靠估计并揭示严重漏报。方法学 novelty 有限（标准贝叶斯分层 + 参数时变过程），但对您在流行病学应用方向有数据集与建模思路参考价值。
- **关键技术**: `Bayesian hierarchical model`, `time-varying reporting probability`, `Ornstein-Uhlenbeck process`, `random walk smoothing`, `cumulative reporting proportion`
- **为什么对您有用**: 属于您 secondary interest 中流行病学应用方向，提供真实监测数据集与延迟修正建模思路，但未涉及因果推断或半参数效率理论，方法学深度有限。

### 2. [10.1093/biomtc/ujag001](https://doi.org/10.1093/biomtc/ujag001) — Bayesian randomized basket trial design: a case study from the ultra-rare invasive mold infections
- **作者**: Yunhe Liu, Satrajit Roychoudhury, Wei Wei
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在超罕见侵袭性霉菌感染(IMI)的随机非劣效篮子试验设定下，目标是在多病原体亚型异质性下估计处理效应并减少对照样本量。提出一种贝叶斯借力策略，核心机制包括：(i) 跨霉菌类型借力处理效应并显式建模异质性；(ii) 利用外部历史数据增广对照组。该方法通过贝叶斯框架提升估计精度与统计功效，同时减少对照组所需的伦理负担。模拟与实例表明，其在控制族水平一类错误的前提下，显著优于简单合并不同亚型的传统做法。对您有用：虽然核心是贝叶斯借力而非半参数效率界，但其“外部数据增广+异质性借力”的框架对流行病学因果推断中处理罕见亚群与外部数据融合的效率问题有参考价值。
- **关键技术**: `Bayesian borrowing`, `basket trial design`, `external control augmentation`, `heterogeneity adjustment`, `noninferiority trial`
- **为什么对您有用**: 属于流行病学/临床试验的因果推断应用；其利用外部数据增广对照组以提升效率的思路，对您在罕见病或观察性因果推断中处理数据稀疏性与异质性的研究有借鉴意义。

### 3. [10.1093/biomtc/ujag019](https://doi.org/10.1093/biomtc/ujag019) — Improving transportability of regression calibration under the main/external validation study design
- **作者**: Zexiang Li, Donna Spiegelman, Molin Wang, Zuoheng Wang, Xin Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在流行病学主研究/外部验证研究（EVS）设计下，针对暴露变量测量误差（ME），目标是改善回归校准模型的跨场景可移植性，避免因 EVS 参数不可移植导致的估计偏差。传统方法直接将 EVS 估计的校准参数代入主研究（MS），本文提出新策略：利用 EVS 仅估计测量误差生成过程参数，而校准模型中的其余参数直接从 MS 获取，从而保证校准模型对 MS 的适用性。理论上推导了所提估计量的渐近性质，模拟表明该方法有效降低偏差并保持名义置信区间覆盖率。实证分析采用 Health Professionals Follow-up Study 与 Men’s Lifestyle Validation Study 数据评估饮食摄入对体重的影响。对您有用：该文处理了流行病学数据中的 ME 与可移植性问题，其拆分参数识别来源的思路对因果推断中 transportability 假设的放松有借鉴意义，同时提供了两个真实的流行病学队列数据集。
- **关键技术**: `regression calibration`, `measurement error correction`, `transportability`, `external validation study`, `asymptotic properties`
- **为什么对您有用**: 涉及流行病学（次级兴趣）中的测量误差与可移植性（transportability，因果推断核心概念），提供了真实数据集，且其拆分参数识别策略对处理外部验证数据的不可移植偏差有方法论启发。

## 其他  *(other, 7 篇)*

### 1. [10.1093/biomtc/ujag014](https://doi.org/10.1093/biomtc/ujag014) — A framework for causal estimand selection under positivity violations
- **作者**: Martha Barnard, Jared D Huling, Julian Wolfson
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10
- **摘要**: {
  "topic": "causal_inference",
  "summary_zh": "在观察性研究中，当处理组和对照组协变量分布重叠不足（positivity violations）时，传统 IPW 类估计量虽保持 ATE 等经典 estimand 但方差与偏差剧增，而 overlap weighting 等方法通过改变目标人群降低方差却引入 estimand mismatch。本文提出一种偏差分解框架，将总偏差拆分为估计量的统计偏差与因目标人群偏移导致的 estimand mismatch 偏差，并据此构建两个设计阶段指标和 estimand 选择程序，使分析者可在"保留原始研究人群"与"降低统计偏差"之间按领域偏好显式权衡。方法在右心导管数据集上进行了实证演示。对您有用：该框架将 positivity 问题形式化为 estimand 选择问题，与您关注的 causal inference 估计和敏感性分析直接相关，偏差分解思路可迁移至 proximal CI 等设定下讨论 identification 假设偏离的后果。",
  "key_techniques": [
    "positivity violations",
    "bias decomposition",
    "estimand mismatch",
    "overlap weighti

### 2. [10.1093/biomtc/ujag015](https://doi.org/10.1093/biomtc/ujag015) — A general framework for heterogeneous variable importance: Pointwise and uniform inference
- **作者**: Lingxuan Shao, Guorong Dai, Jinbo Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "nonparam_semipara",
  "summary_zh": "在非参数回归设定下，本文研究协变量对响应变量的"异质性变量重要性"，即该贡献如何随特征变量（如年龄）变化；目标参数定义为两个条件均方误差之比，无需显式参数结构假设。作者提出该比率参数的点估计量，分别建立逐点收敛速率与一致收敛速率。推断方面，发展了渐近置信区间与置信带的构造程序，并证明其达到名义覆盖率。模拟与实际数据（心理学/流行病学场景）展示了有限样本表现。对您有用：条件比率参数的逐点与一致推断涉及 semiparametric efficiency 与 uniform inference，与您关注的 semiparametric efficiency bounds 及 hypothesis testing 直接相关，且实际数据应用可作流行病学队列分析的参考 pipeline。",
  "key_techniques": [
    "conditional mean squared error ratio",
    "uniform convergence rate",
    "asymptotic confidence bands",
    "nonparametric regression",
    "influence function"
  ],

### 3. [10.1093/biomtc/ujag036](https://doi.org/10.1093/biomtc/ujag036) — OPERA: a new algorithm for patient stratification based on partially ordered risk factors
- **作者**: Yingzhou Liu, Menggang Yu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对医疗风险分层问题，提出基于偏序风险因子的患者分层算法 OPERA（Ordering Poset Elements by Recursive Amalgamation），设定中多个风险因子联合构成偏序集（poset）。相较于传统回归模型，OPERA 类似树方法能探索高阶交互，但通过显式利用偏序结构，允许更灵活的分期模式并实现更快的剪枝。算法核心在于递归合并偏序元素，将有序风险因子映射为分层结构。仿真与癌症分期数据表明 OPERA 在有序风险分层上表现良好；对您而言，若在流行病学队列研究中需处理具有天然偏序结构的多风险因子分层，该算法提供了一种计算友好的替代方案，但方法学上与因果推断或半参数效率理论关联较弱。
- **关键技术**: `partially ordered set (poset)`, `recursive amalgamation`, `tree pruning`, `high-order interaction`, `risk stratification`
- **为什么对您有用**: 属于流行病学/临床数据分析应用，但方法核心是偏序集的递归合并与剪枝，未涉及因果推断、半参数或高维推断，仅在处理有序风险因子的分层计算上有微弱参考价值。

### 4. [10.1093/biomtc/ujag046](https://doi.org/10.1093/biomtc/ujag046) — LLOT: application of Laplacian Linear Optimal Transport in spatial transcriptome reconstruction
- **作者**: Junhao Zhu, Kevin Zhang, Dehan Kong, Zhaolei Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究空间转录组重建问题，设定为整合 scRNA-seq 与空间转录数据以推断单细胞分辨率下的全基因组表达。核心方法 LLOT（Laplacian Linear Optimal Transport）通过迭代校正平台效应，并利用 Laplacian 最优传输将空间 spot 分解为单细胞的空间平滑概率混合。方法依赖于最优传输的数值优化与 Laplacian 正则化以保证空间平滑性。实证方面，在 ISH、Slide-seq、10x Visium 等多技术数据集上 benchmark，表明 LLOT 提供了可解释且通用的重建框架。对您而言，本文属生物信息应用，与因果推断/高维/半参数理论无直接关联，仅在最优传输的数值计算层面有极弱联系。
- **关键技术**: `Laplacian optimal transport`, `linear optimal transport`, `spatial transcriptomics integration`, `platform effect correction`
- **为什么对您有用**: 本文属空间转录组学的最优传输应用，与您主攻方向（因果推断、高维RMT、半参数效率界）无方法重叠；仅在最传输数值优化层面有极弱关联，阅读收益低。

### 5. [10.1093/biomtc/ujag043](https://doi.org/10.1093/biomtc/ujag043) — SIMBA–a Bayesian decision framework for the identification of optimal biomarker subgroups for cancer basket clinical trials
- **作者**: Shijie Yuan, Jiaxin Liu, Zhihua Gong, Xia Qin, Crystal Qin, Yuan Ji et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对多适应症篮子临床试验（basket trial），提出名为 SIMBA 的贝叶斯决策框架，目标是在生物标志物过表达与响应率正相关的假设下识别最优亚组并做出 go/no-go 决策。核心机制基于贝叶斯分层模型（Bayesian hierarchical model），通过跨适应症的信息共享（information sharing）来定义生物标志物阳性/阴性亚组。方法通过模拟评估操作特性（operating characteristics）并与现有方法对比，旨在提高受益亚群的识别率。对您而言，本文属于临床试验设计范畴，与您关注的因果推断、半参数效率界或高维统计等核心理论方向关联较弱，若需了解篮子试验的贝叶斯分层建模可作泛读。
- **关键技术**: `Bayesian hierarchical model`, `basket trial design`, `subgroup identification`, `information sharing`, `go/no-go decision`
- **为什么对您有用**: 本文属于临床试验设计领域，与您的主要兴趣（因果推断、高维/半参数理论）关联较弱；若您关注流行病学/临床应用中的贝叶斯分层建模或亚组分析，可作背景参考，但方法学创新点不在效率界或因果识别上。

### 6. [10.1093/biomtc/ujag018](https://doi.org/10.1093/biomtc/ujag018) — Quantifying uncertainty in RNA velocity
- **作者**: Huizi Zhang, Natalia Bochkina, Sara Wade
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在单细胞 RNA 测序快照的 RNA velocity 估计问题中，提出贝叶斯层次模型，采用时间依赖转录率与非平凡初始条件，目标 estimand 为基因共享潜时间与 velocity 向量。核心方法为贝叶斯层次建模，结合 MCMC 与 consensus approach 进行全贝叶斯推断，实现对潜时间与 velocity 的 well-calibrated 不确定性量化。作者讨论了模型参数的可识别性，特别是大潜时间值的 identifiability，这是此前工作未涉及的。模拟与小鼠胚胎干细胞数据实证表明，该方法的不确定性校准优于现有黑箱方法，估计结果与细胞周期阶段一致。该论文属于计算生物学应用，方法学 novelty 有限（贝叶斯层次模型 + MCMC/consensus），对您的主要兴趣方向（因果推断、半参数效率、高维理论）无直接迁移价值。
- **关键技术**: `Bayesian hierarchical model`, `MCMC with consensus Monte Carlo`, `parameter identifiability analysis`, `RNA velocity estimation`, `uncertainty quantification`
- **为什么对您有用**: 与您的研究兴趣关联较弱：identifiability 讨论与数学统计有微弱联系，MCMC/consensus 计算策略与统计计算方向有少量重叠，但整体为生物信息学应用，方法论通用性有限。

### 7. [10.1093/biomtc/ujag011](https://doi.org/10.1093/biomtc/ujag011) — Doubly balanced samples with dynamic sample sizes
- **作者**: Blair Robertson, Chris Price, Marco Reale, Philip Davies
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究空间抽样设计问题，目标是在给定研究区域内生成同时满足辅助变量平衡和空间平衡的双重平衡主样本或超样本。作者为动态分配抽样（DAS）提出了一种新的目标函数，仅需总体单元间的距离度量即可实现双重平衡。该方法通过优化该目标函数，在动态调整样本量的同时保证了样本在辅助变量和空间分布上的代表性。数值实验表明，该方法在生成双重平衡样本方面优于传统的固定样本量设计，并配套提供了基于设计的方差估计量。实证部分将其应用于巴西亚马逊地区地上生物量的估计。该文属于传统抽样设计领域，与您关注的因果推断、半参数效率界及高维理论等核心方向距离较远，仅在基于设计的推断框架上有极微弱的方法论旁支联系。
- **关键技术**: `dynamic assignment sampling`, `spatially balanced design`, `auxiliary variable balancing`, `design-based variance estimation`
- **为什么对您有用**: 本文属于空间抽样设计领域，与您的主要兴趣（因果推断、半参数效率、高维统计）基本无直接交集；仅在“基于设计的方差估计”这一推断思路上有极微弱的旁支联系，对您核心方向的直接收益极低。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

