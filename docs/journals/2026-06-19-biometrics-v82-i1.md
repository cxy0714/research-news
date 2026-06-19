# Biometrics — Vol 82  Issue 1  ·  2026-06-19

- 共 35 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 13 篇（对照 OpenAlex 60 篇）：10.1093/biomtc/ujaf132、10.1093/biomtc/ujaf109、10.1093/biomtc/ujaf136、10.1093/biomtc/ujaf135、10.1093/biomtc/ujaf175 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Biometrics Vol 82 Issue 1 的 35 篇论文主要围绕三条主线展开：**因果推断中的鲁棒识别与效率提升**（约 11 篇）、**假设检验与多重比较的精确控制**（约 4 篇），以及**半参数/非参方法与高维建模**（约 10 篇），其余论文分散在流行病学应用、空间转录组重建、抽样设计、统计计算等领域。

**因果推断**主线最为集中，覆盖网络干扰、最优治疗规则（ITR/DTR）、整群随机试验、观察性研究匹配、空间因果、自适应试验等子问题。在网络干扰方向，“Causal inference with misspecified network interference structure” 推导了误设网络下偏差界并提出多候选网络鲁棒估计量；“Learning optimal early decision treatment rules with multi-domain intermediate outcomes” 利用多域中间结局构建个性化复合代理奖励，改善早期决策效率；“A robust covariate-balancing method for estimating individualized treatment with censored data” 在删失数据下给出双重稳健的 ITR 值函数估计量；“Estimating optimal dynamic treatment regimes with Gaussian process emulation” 用 GP 响应面替代网格搜索，提高多模态值函数优化效率；“Distributed fusion R-learner of heterogeneous treatment effect using distributed medicaid data” 在分布式隐私约束下实现无效率损失的 CATE 融合估计；“Handling incomplete outcomes and covariates in cluster-randomized trials” 提出针对三类缺失的双重稳健估计量并讨论半参效率界逼近；“Long-term memory effects of an incremental blood pressure intervention in a mortal cohort” 用贝叶斯半参数 G-formula 处理死亡竞争风险；“Bias mitigation in matched observational studies with continuous treatments” 在连续处理匹配中引入卡钳与偏差校正 Neyman 估计；“Estimating the causal effect of redlining on present-day air pollution” 用潜变量因子模型代理预处理期混杂，识别历史政策的长期空间因果效应；“An adaptive design for optimizing treatment assignment in randomized clinical trials” 多阶段自适应更新分配机制以提高条件方差未知时的效率；“Generalized entropy calibration for analyzing voluntary survey data” 建立校准权重与回归估计的对偶关系，给出双重稳健性与局部效率。这些工作反复强调对网络误设、模型误设、缺失机制、分布偏移的鲁棒性，并大量采用双重稳健、半参效率界、交叉拟合、贝叶斯或分布融合等工具。

**假设检验**主线聚焦多重比较与高维检验的精确 error rate 控制。“Making all pairwise comparisons in multi-arm clinical trials without control treatment” 基于封闭检验原则实现精确 FWER 控制，并推广到自适应设计；“Ultra-high-dimensional threshold selection for quantile feature screening with false discovery rate error rate control” 构造对称镜像统计量，在超高维分位数筛选下渐近控制 FDR；“Rank-adaptive covariance testing with applications to genomics and neuroimaging” 基于 Ky-Fan 范数自适应选择秩，在低秩异质结构下提升检验功效；“Repeated inclusion cluster randomized trials” 提出允许集群重复随机化的新设计，在固定总样本下提升检验效能。共同特点是面向实用约束（无对照、超高维、低秩信号、集群间相关性）设计精确而非保守的推断过程。

**半参数/非参与高维建模**主线包括：“Nonparametric ANCOVA for longitudinal outcomes in a randomized clinical trial” 用交叉拟合估计条件期望以逼近半参效率界，实现稳健方差缩减；“DNN-based semiparametric AFT model for integrating genomic and pathological imaging data” 用 DNN sieve 处理影像非参数项，并给出参数部分的选择一致性与渐近正态性；“Variable selection in functional linear Cox model” 用组 MCP 实现功能协变量选择；“Reduced varying coefficient models for regional quantile regression with multiple responses” 用低秩约束加 KNN-fused LASSO 降维分位数系数；“Quasi-likelihood estimation for semiparametric circular regression models” 结合 backfitting 与核光滑处理圆形响应；“Bayesian inference for Cox regression models using catalytic prior distributions” 将催化先验推广到高维 Cox 模型，给出正则化偏似然估计量的一致性；“Sparse robust discriminant analysis for high-dimensional and heavy-tailed data” 在椭圆等高判别下放松轻尾假设，仅需四阶矩即达子空间估计相合性；“Inhomogeneous mark correlation functions for general marked point processes” 非参数估计空间标记关联，校正非平稳性偏差。这些工作展示了非参数/半参数工具在高维、函数型、圆形、空间数据下的适应性，且多数伴随渐近理论。

与因果推断、半参数效率方向最贴近的优先阅读论文包括：网络干扰与多重候选估计（Causal inference with misspecified network interference structure）、删失数据双重稳健 ITR（A robust covariate-balancing method for estimating individualized treatment with censored data）、整群随机试验缺失处理（Handling incomplete outcomes and covariates in cluster-randomized trials）、连续处理匹配偏差校正（Bias mitigation in matched observational studies with continuous treatments）、非参数 ANCOVA（Nonparametric ANCOVA for longitudinal outcomes in a randomized clinical trial）、DNN 半参数 AFT（DNN-based semiparametric AFT model）。高维检验方向可关注秩自适应协方差检验（Rank-adaptive covariance testing）与 FDR 控制的分位数筛选（Ultra-high-dimensional threshold selection for quantile feature screening）。

## 因果推断  *(causal_inference, 11 篇)*

### 1. [10.1093/biomtc/ujag023](https://doi.org/10.1093/biomtc/ujag023) · [arXiv](https://arxiv.org/abs/2302.11322) — Causal inference with misspecified network interference structure
- **作者**: Bar Weinstein, Daniel Nevo
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在网络干扰设定下，目标是估计单元的因果效应，传统方法假设干扰网络已知且准确，本文研究网络误设下的后果。作者推导了基于误设网络估计因果效应的偏差界，证明偏差随假设网络与真实网络诱导暴露概率（exposure probability）的散度增大而增长。为解决此问题，提出一种同时利用多个候选网络的新估计量，该估计量在至少一个候选网络正确时保持无偏，且无需预先知晓哪个网络正确。模拟与社交网络田野实验验证了该估计量的鲁棒性。对您可能有用：该工作直接推进了因果推断中网络干扰设定下的 identification 与 estimation 理论，其多网络鲁棒估计思路可启发 longitudinal / mediation 中复杂依赖结构的误设敏感性分析。
- **关键技术**: `network interference`, `exposure mapping`, `misspecification bias bound`, `multiple-network robust estimator`, `divergence of induced exposure probabilities`
- **为什么对您有用**: 本文直接连接因果推断中网络干扰与 identification 理论子方向，处理了依赖结构误设这一核心痛点。研究者可用 technical_arsenal 中的 identification theory in causal inference 分析其暴露概率散度界是否可进一步收紧，或用 moderately_familiar 的 M-estimation theory 推导该多网络鲁棒估计量的渐近分布与 semiparametric efficiency bound。**立即可做**：用 very_familiar 的 estimation theory in causal inference 检查其无偏性条件与偏差界，并尝试构造更高效的 one-step / DR 版本。

### 2. [10.1093/biomtc/ujaf167](https://doi.org/10.1093/biomtc/ujaf167) — Learning optimal early decision treatment rules with multi-domain intermediate outcomes
- **作者**: Wenbo Fei, Yuan Chen, Zexi Cai, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biometrics
- **机构**: New York University · Columbia University · Memorial Sloan Kettering Cancer Center · University of Michigan
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向/多阶段干预设定下，目标是学习最优早期决策的个体化治疗规则（ITR），核心 estimand 为最大化长期临床结局的期望奖励。现有方法通常仅以最终结局为奖励，本文提出利用多域中间结局（如患者自评等早期信号）构建个性化复合结局作为代理奖励。复合结局由观测指标推断的潜在状态的加权求和构成，权重针对个体个性化且保证与长期最终响应的一致性。理论层面，该方法通过潜在状态模型与个性化加权机制实现早期非响应者的识别，并改善长期治疗结局的估计效率。模拟与重度抑郁症（MDD）随机临床试验数据验证了方法的有效性。对您可能有用：本文在 longitudinal causal inference 的多阶段决策设定中引入中间代理结局，其潜在状态推断与个性化加权机制可连接到您熟悉的 semiparametric efficiency 与 identification theory。
- **关键技术**: `individualized treatment rules`, `personalized composite outcome`, `latent state inference`, `proximal/intermediate outcome weighting`, `longitudinal dynamic treatment regime`
- **为什么对您有用**: 本文直接连接到 longitudinal causal inference 中多阶段最优治疗规则的学习，其利用中间结局作为代理奖励的思路与 proximal CI 中 negative-control / proxy variable 的 identification 逻辑有结构相似性。您可以用 technical_arsenal 中 moderately_familiar 的 identification theory 与 semiparametric theory 分析其个性化加权机制的 identification 条件与效率性质。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以推导该复合结局 estimator 的 influence function 与 semiparametric efficiency bound。

### 3. [10.1093/biomtc/ujag050](https://doi.org/10.1093/biomtc/ujag050) — A robust covariate-balancing method for estimating individualized treatment with censored data
- **作者**: Rujia Zheng, Wensheng Zhu, Xiaofan Guo
- **期刊/来源**: Biometrics
- **机构**: Northeast Normal University · First Hospital of China Medical University · China Medical University
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据下，目标是估计最优个体化治疗方案（optimal ITR）的 contrast value function，以最大化期望生存时间。现有方法依赖倾向得分模型或删失模型的正确设定，任一模型误设将导致估计不可靠。本文提出两种 robust covariate-balancing 估计量，分别通过在权重中引入删失概率和删失时间的生存函数来实现协变量平衡。理论证明所提估计量具有双重稳健性（doubly robust），且在标准正则条件下达到 n^{-1/2}-CAN（渐近正态）。模拟显示其优于现有方法；实证应用于中国农村高血压控制项目，识别最优用药方案以提升 36 个月生存概率。对您可能有用：本文将 covariate-balancing 从横截面 ITR 推广到删失生存数据，其 DR 与 CAN 的推导路径可直接对照您熟悉的因果推断估计理论。
- **关键技术**: `individualized treatment regime`, `contrast value function`, `covariate-balancing`, `doubly robust estimation`, `censored survival data`, `asymptotic normality`
- **为什么对您有用**: 本文连接到因果推断的个体化治疗规则（ITR）与删失数据设定，属于 longitudinal/precision medicine 子方向。您 very_familiar 的因果推断估计理论可直接审视其 DR 与协变量平衡的 influence function 构造；若想深入，可用 moderately_familiar 的 semiparametric theory 检验其声称的 efficiency 是否达到 semiparametric efficiency bound。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以验证其 DR 估计量是否为最优或可进一步用 HOIF 提升效率。

### 4. [10.1093/biomtc/ujaf174](https://doi.org/10.1093/biomtc/ujaf174) — Estimating optimal dynamic treatment regimes with Gaussian process emulation
- **作者**: Daniel Rodriguez Duque, David A Stephens, Erica E M Moodie
- **期刊/来源**: Biometrics
- **机构**: McGill University
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断设定下，本文研究最优动态治疗策略（DTR）的估计问题，目标 estimand 为值函数（value function），即遵循特定策略下的期望因果结局。针对贝叶斯动态边际结构模型等参数化值搜索方法可能因模型误设导致错误结论，以及网格搜索计算代价高且估计不确定性大的缺陷，作者提出用高斯过程（GP）回归对策略空间到值函数的响应面进行非参数建模与优化。核心机制是将值函数的估计视为带噪声的响应面，利用 GP 的后验均值与方差实现主动搜索（acquisition function 优化），在多模态值函数场景下仍能高效定位全局最优策略，避免了网格搜索的信息低效利用与鲁棒性不足。理论层面未给出严格的收敛率或半参数效率界，但通过模拟与 HIV 病例数据（优化 CD4 细胞计数的治疗调整）实证展示了 GP 方法在计算效率与估计精度上的优势。对您可能有用：本文将 GP emulation 引入 DTR 的值搜索，为纵向因果推断中的策略优化提供了一种非参数计算替代方案。
- **关键技术**: `dynamic treatment regimes`, `value search estimation`, `Gaussian process emulation`, `Bayesian marginal structural models`, `acquisition function optimization`, `inverse probability weighting`
- **为什么对您有用**: 本文直接连接到纵向因果推断中的动态治疗策略（DTR）估计这一子方向。您武器库中的 semiparametric theory 与 minimax bounds 可以用来攻这篇 paper 的理论缺口——它目前缺乏值函数估计的收敛率与半参数效率界分析，用 HOIF 或 minimax 理论可以刻画 GP emulation 在策略空间上的最优收敛阶。Follow-up 粗判：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上长肌肉，结合 GP 回归的 nonparametric convergence rate 来推导值函数估计的效率界；若要严格处理 GP acquisition 的计算-统计权衡，还需补充 computationally constrained statistics 的低阶多项式视角。

### 5. [10.1093/biomtc/ujag034](https://doi.org/10.1093/biomtc/ujag034) — Distributed fusion <i>R</i> -learner of heterogeneous treatment effect using distributed medicaid data
- **作者**: Jinhong Li, Julie M Donohue, Lu Tang
- **期刊/来源**: Biometrics
- **机构**: University of Pittsburgh · Department of Health
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对多站点分布式数据下的条件平均处理效应（CATE）估计问题，提出了一种分布融合 R-learner（DF R-learner）方法。该方法允许各站点 CATE 函数存在差异，并通过数据驱动的融合惩罚将相似参数进行合并，从而在保护隐私（不共享个体层面数据）的前提下提升估计效率。估计器利用置信分布（confidence distribution）实现高效信息交换，论文在理论上证明了该方法与集中式数据方法相比无效率损失。模拟和实证研究使用了宾夕法尼亚州多个医疗管理组织的医疗补助数据，以评估药物使用障碍的药物治疗效果。该方法结合了 R-learner 的残差化建模思想与分布式优化框架，适用于大规模多源异质性效应估计。对您而言，该工作直接连接因果推断中的异质性处理效应（HTE）方向，并在统计计算层面展示了分布式隐私保护算法如何与现有 CATE 估计器结合。
- **关键技术**: `R-learner`, `distributed learning`, `fusion penalty`, `confidence distribution`, `heterogeneous treatment effect`, `privacy-preserving data integration`
- **为什么对您有用**: 该论文直接涉及因果推断中的异质性处理效应（CATE）估计，属于您的首要兴趣方向。您非常熟悉的'估计理论 in causal inference' 可以轻松理解其理论性质（无效率损失），并且您擅长软件实现，可尝试复现或扩展其分布融合框架。从 follow-up 角度看，这是立即可做的：基于 R-learner 和分布式优化的思想，可以进一步引入高维变量选择或半参数效率理论改进。

### 6. [10.1093/biomtc/ujag030](https://doi.org/10.1093/biomtc/ujag030) · [arXiv](https://arxiv.org/abs/2401.11278) — Handling incomplete outcomes and covariates in cluster-randomized trials: doubly robust estimation, efficiency considerations, and sensitivity analysis
- **作者**: Bingkai Wang, Fan Li, Rui Wang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在整群随机化试验（CRT）设定下，目标是估计多种效应尺度上的平均处理效应（ATE），同时应对结局变量 MAR 缺失、协变量无约束缺失及群组人口规模缺失三类数据缺失问题。本文提出一个 doubly robust estimator，在缺失机制与 outcome/treatment 模型之一正确时仍保持一致估计，且不要求对协变量缺失机制建模。为提升精度，作者详细讨论了通过指定最优权重、利用 machine learning（cross-fitting）以及建模处理分配机制来逼近 semiparametric efficiency bound 的策略。此外，针对 MAR 假设可能失效的情形，提出了专门适配 CRT 结构的 sensitivity analysis 框架，用于评估偏离缺失假设对估计的影响。对您可能有用：本文的 DR + efficiency 优化 + sensitivity 框架组合，直接连接到 causal inference 中的 DR estimation 与 sensitivity analysis 子方向。
- **关键技术**: `doubly robust estimation`, `semiparametric efficiency bound`, `cross-fitting`, `missing at random (MAR)`, `sensitivity analysis`, `cluster-randomized trials`
- **为什么对您有用**: 本文直接连接到 causal inference 中的 DR estimation 与 sensitivity analysis 子方向，且在 CRT 结构下统一处理多种缺失模式，这在流行病学应用中极为常见。您可以用 technical_arsenal 中 very_familiar 的 estimation theory in causal inference 分析其 DR estimator 的 influence function 构造，并用 moderately_familiar 的 identification theory 检视其协变量无约束缺失下的 identification 逻辑。Follow-up 判断：**立即可做**——用 very_familiar 武器即可展开对其 efficiency bound 与 DR 性质的理论审视，并可尝试将 sensitivity analysis 框架推广至 longitudinal CRT 设定。

### 7. [10.1093/biomtc/ujaf176](https://doi.org/10.1093/biomtc/ujaf176) · [arXiv](https://arxiv.org/abs/2311.00357) — Long-term memory effects of an incremental blood pressure intervention in a mortal cohort
- **作者**: Maria Josefsson, Nina Karalija, Michael J Daniels
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本研究在纵向队列数据中，评估长期降血压干预对情景记忆的因果效应，并区分病因效应（干预对总体的影响）和预后效应（在始终存活者中的影响）。为处理死亡竞争风险，作者采用贝叶斯半参数方法估计增量阈值干预的扩展G-formula，并引入一种新的稀疏诱导Dirichlet先验，利用纵向数据的时间结构实现变量选择。通过仿真研究，与贝叶斯决策树集成方法比较，展示了所提方法的有限样本性能。应用于Betula队列数据后，未发现显著病因或预后效应，提示降血压干预可能不强烈影响记忆。该方法为纵向因果推断中处理死亡偏移提供了新思路，直接对应您对纵向因果识别与贝叶斯半参数估计的兴趣。
- **关键技术**: `Bayesian semiparametric estimation`, `Extended G-formula`, `Incremental threshold intervention`, `Sparsity-inducing Dirichlet prior`, `Longitudinal causal inference`, `Etiological vs prognostic effects`
- **为什么对您有用**: 本文属于纵向因果推断中增量干预效应的识别与估计，直接对应您primary interest中的causal inference（纵向方向）。您熟悉的因果推断估计理论（technical arsenal中very_familiar）可支撑对贝叶斯估计量的频率性质进行交叉验证，但贝叶斯后验收缩理论需要先在moderately_familiar的semiparametric theory上提升，因此建议作为中期可做课题。

### 8. [10.1093/biomtc/ujag022](https://doi.org/10.1093/biomtc/ujag022) · [arXiv](https://arxiv.org/abs/2409.11701) — Bias mitigation in matched observational studies with continuous treatments: calipered non-bipartite matching and bias-corrected estimation and inference
- **作者**: Anthony Frazier, Siyu Heng, Wen Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该文针对连续处理变量（continuous treatment）的匹配观察性研究中因不精确匹配（inexact matching）导致的协变量失衡引发的偏差问题。作者通过重新分析社交距离对COVID-19病例数影响的匹配研究，指出现有常规做法仅凭事后协变量平衡指标（如标准化差异）可能掩盖严重偏差。在匹配阶段，提出一种同时纳入协变量和处理剂量信息的卡钳设计（caliper），用以提高下游估计和推断的质量。在估计和推断阶段，引入偏差校正的Neyman估计量及其对应的偏差校正方差估计量，实现匹配后偏差的系统性缓解。数值实验和实际数据分析表明，该方法能有效降低估计偏差并改善置信区间覆盖。该论文提供了一个开源R包实现整个框架。对您而言，该研究直接对应primary interest中的因果推断（特别是连续处理变量的匹配设计），其中的caliper设计与偏差校正估计思路可迁移至您熟悉的非参数估计与因果推断方法论中。
- **关键技术**: `caliper matching`, `bias-corrected Neyman estimator`, `continuous treatment`, `matched observational study`, `R package`
- **为什么对您有用**: 本文直接针对因果推断中连续处理变量的匹配问题，属于您primary interest中的因果推断子方向。您技术武器库中'very_familiar'的'estimation theory in causal inference'可以直接复现其偏差校正估计量并检验其在其他设定下的表现（如sharpness of variance estimator）。立即可做：基于论文R包和现有匹配流程，可立即对其方法进行敏感性分析或调整卡钳设计来扩展适用场景。

### 9. [10.1093/biomtc/ujaf173](https://doi.org/10.1093/biomtc/ujaf173) · [arXiv](https://arxiv.org/abs/2501.16958) — Estimating the causal effect of redlining on present-day air pollution
- **作者**: Xiaodan Zhou, Shu Yang, Brian J Reich
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在空间因果推断框架下，估计1930年代美国红线政策对2010年PM2.5和NO2污染浓度的长期因果效应。由于政策年代久远，预处理协变量极少，传统方法难以充分控制未测量混杂。作者提出一个空间和非空间的潜变量因子模型，利用1940年人口普查中的失业率、房租和黑人人口比例作为代理变量，重构预处理期的潜在社会经济地位。在较宽泛的假设下建立因果效应的可识别性，并采用贝叶斯MCMC进行不确定性量化。因果分析发现，历史上被红线标注的街区现今NO2浓度显著更高，但PM2.5差异不显著；洛杉矶和亚特兰大的效应最为突出。本文为环境流行病学中历史政策的长期间接效应提供了可操作的分析范式，对您使用因果推断方法处理观测研究中未测量混杂的应用场景（如流行病学队列数据）有直接参考价值。
- **关键技术**: `Bayesian MCMC`, `latent factor model`, `spatial causal inference`, `proxy variables for unmeasured confounding`, `identification via latent variable`
- **为什么对您有用**: 本文属于您次级兴趣中的重要应用领域（流行病学/环境健康），其核心问题——利用代理变量处理未测量混杂——与您的因果推断identification和估计理论直接相关。您擅长的因果推断估计理论（very_familiar）可直接用于分析该潜变量模型的单向度和识别强度；同时，该文的空间建模思路（空间潜因子）可启发您将贝叶斯MCMC与debiased ML相结合来获得更精确的长期效应估计。总体而言，这是一篇扎实的应用论文，可作为您进入环境因果推断领域的入门参考，值得花时间阅读全文以了解数据结构和分析流程。

### 10. [10.1093/biomtc/ujaf168](https://doi.org/10.1093/biomtc/ujaf168) · [arXiv](https://arxiv.org/abs/2509.00429) — An adaptive design for optimizing treatment assignment in randomized clinical trials
- **作者**: Wei Zhang, Zhiwei Zhang, Aiyi Liu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 该论文针对随机临床试验中处理分配机制的统计效率优化问题，在给定随机化机制类别内，最优分配可由基线协变量下潜在结果的条件方差函数刻画。然而，设计阶段常缺乏或不可靠关于条件方差函数的信息，故提出一种多阶段自适应设计，在期中分析时基于累积信息更新处理分配机制。此种自适应调整会影响试验数据的联合分布，需在效应估计中予以考虑。论文考虑一类一致且渐近正态的处理效应估计量，识别该类中最有效的估计量，并通过代入条件方差函数的估计量加以近似。模拟表明，当先验信息有限时，该设计相比基于相同先验信息的传统单阶段设计可带来可观的效率增益，并以实际卒中试验数据加以说明。对您而言，该工作涉及因果推断中随机化试验设计的效率和估计理论，与您熟练的因果推断估计理论直接相关，可作为临床试验设计优化的参考。
- **关键技术**: `adaptive design`, `conditional variance function`, `multi-stage randomization`, `asymptotically normal estimator`, `optimal treatment assignment`
- **为什么对您有用**: 该论文属于因果推断中的随机试验设计与处理效应估计优化，与您primary interest中的causal inference（尤其是估计效率）紧密相关。您very_familiar中的“estimation theory in causal inference”可直接用于评价该自适应设计下估计量的渐近性质，或扩展至更复杂的协变量调整框架。立即可做：用您熟悉的因果推断估计理论（如DR估计、半参效率界）分析该设计在更一般设定下的效率增益或与交叉拟合的结合。

### 11. [10.1093/biomtc/ujag041](https://doi.org/10.1093/biomtc/ujag041) · [arXiv](https://arxiv.org/abs/2412.12405) — Generalized entropy calibration for analyzing voluntary survey data
- **作者**: Yonghyun Kwon, Jae Kwang Kim, Yumou Qiu
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对自愿调查数据中的选择偏差问题，提出广义熵校准（generalized entropy calibration）作为统一的校准加权工具，其假设采样机制可忽略。方法核心是建立校准权重与回归估计的对偶关系，从而识别隐含的回归模型，并可用于模型选择。基于广义熵（如指数、对数、线性形式）构造权重，作者还发展了两步校准法：在已知重要研究变量的线性模型时，先校准倾向性再平滑权重，以提高效率。理论上，该估计量具有双鲁棒性（倾向性或结果模型之一正确即一致）和局部效率（两者都正确时达到半参效率界）。模拟研究验证了有限样本性能。该工作对因果推断中控制选择偏差的加权方法（如 IPW、AIPW）有直接参考价值，尤其是双鲁棒性和效率分析可为观察性研究提供新思路。
- **关键技术**: `Calibration weighting`, `Generalized entropy balancing`, `Double robustness`, `Local efficiency`, `Two-step calibration`
- **为什么对您有用**: 本文聚焦的校准加权方法直接对应因果推断中控制选择偏差的估计问题（如倾向得分加权、AIPW），属于您 primary interest 中的 causal inference（identification, estimation）。您的武器库中“estimation theory in causal inference”可用来分析其双鲁棒性和局部效率性质，并与传统 DR 估计比较。立即可做：方法原理与您熟悉的 IPW 和 DR 估计一脉相承，可直接迁移到观察性研究的 ATE 估计场景，无需额外工具。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomtc/ujag039](https://doi.org/10.1093/biomtc/ujag039) — Sparse robust discriminant analysis for high-dimensional and heavy-tailed data
- **作者**: Weijian Huang, Qing Mai, Jing Zeng
- **期刊/来源**: Biometrics
- **机构**: University of Science and Technology of China · Hefei University of Technology · Florida State University
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维重尾数据的分类问题，在椭圆等高判别分析（EDA）模型下提出鲁棒稀疏线性判别方法。传统稀疏LDA假设预测变量轻尾，而实际医学数据（如基因表达数据）常具有重尾特征。该文采用平衡率（balanced rate）作为不平衡数据下的分类性能指标，并识别出达到最低平衡率所需的内在维数约简子空间。方法先通过子空间投影大幅降维，再在降维后的低维数据上进行分类预测。理论方面，仅在预测变量四阶矩有限条件下，即可同时保证子空间估计、变量选择和预测精度的相合性。模拟和两个肺癌数据集、一个白血病数据集的实证结果表明该方法优于多种现有方法。本文的高维鲁棒分类思想与您的高维统计（特别是轻尾假设放宽）兴趣直接相关，其理论分析技巧（如仅用四阶矩条件）可以为更一般的重尾高维推断提供参考。
- **关键技术**: `elliptically contoured discriminant analysis`, `balanced rate`, `dimension-reduction subspace`, `sparse linear discriminant analysis`, `consistency under fourth-moment condition`
- **为什么对您有用**: 该论文直接对应您的高维统计子方向，特别是高维分类中重尾数据的处理。您熟悉的 very_familiar 工具 high-dimensional asymptotics 可立即用来审视其变量选择和子空间估计的收敛速率是否最优，例如检验其四阶矩条件是否紧。立即可做：您现有的高维渐近理论知识和数值经验足以复现其模拟并尝试改进变量选择的一致性界。

## 非参数 / 半参数  *(nonparam_semipara, 7 篇)*

### 1. [10.1093/biomtc/ujag047](https://doi.org/10.1093/biomtc/ujag047) — Nonparametric ANCOVA for longitudinal outcomes in a randomized clinical trial
- **作者**: Rex Shen, Xiaotong Jiang, Changyu Shen, Lu Tian
- **期刊/来源**: Biometrics
- **机构**: Stanford University · Biogen (United States)
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在随机化临床试验的纵向数据设定下，目标是估计 ATE，传统混合效应模型 ANCOVA 依赖模型正确设定。本文提出非参数 ANCOVA，不假设混合效应模型正确，通过调整基线协变量提升 ATE 估计精度。最优 ANCOVA 调整依赖于纵向结局对基线协变量的条件期望，该函数通常未知；作者采用 cross-fitting 结合非参数/机器学习方法估计该条件期望，进而指导 ANCOVA 协变量调整。理论推导表明该方法达到 semiparametric efficiency bound，实现 n^{-1/2}-CAN 且在协变量与结局相关时方差显著低于传统 ANCOVA。数值实验验证了其稳健性与精度优势。对您有用：本文将 cross-fitting 与非参数条件期望估计结合以逼近纵向 ATE 的效率界，直接连接您在 efficiency theory 与 semiparametric theory 上的核心兴趣。
- **关键技术**: `nonparametric ANCOVA`, `cross-fitting`, `semiparametric efficiency bound`, `conditional expectation estimation`, `longitudinal mixed effects model`, `covariate adjustment`
- **为什么对您有用**: 本文直接连接您 primary interest 中的 efficiency theory 与 semiparametric theory 子方向，展示了在纵向 RCT 设定下如何通过 cross-fitting 逼近 ATE 的 semiparametric efficiency bound。您 technical_arsenal 中 very_familiar 的 minimax bounds 与 estimation theory in causal inference 可直接用于审视其声称的效率优势是否紧；moderately_familiar 的 semiparametric theory 与 M-estimation theory 则可切入其条件期望估计的收敛率与 influence function 推导细节。Follow-up 判断：**立即可做**——用您熟悉的 semiparametric efficiency 与 minimax 工具即可复现其理论推导并探索更一般（如非随机化/观测性纵向数据）设定下的效率界。

### 2. [10.1093/biomtc/ujag045](https://doi.org/10.1093/biomtc/ujag045) — DNN-based semiparametric AFT model for integrating genomic and pathological imaging data in cancer prognosis
- **作者**: Jingmao Li, Qingzhao Zhang, Shuangge Ma
- **期刊/来源**: Biometrics
- **机构**: Yale University · Xiamen University · Xiamen University of Technology
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在癌症预后设定下，本文针对高维基因组与病理影像的融合数据，提出一个半参数加速失效时间（AFT）模型，目标参数为基因组变量的参数系数与影像变量的非参数函数。基因组效应采用参数建模并施加稀疏惩罚，影像效应采用深度神经网络（DNN）建模并对第一层权重施加 group 惩罚以实现变量选择。理论部分在适当正则条件下证明了参数部分的选择一致性、估计一致性及渐近正态性，为 DNN 非参数组件的惩罚估计提供了较严格的大样本保证。计算方面给出了优化算法细节，模拟与 TCGA 肺癌真实数据分析显示了相较于替代方法的竞争力。对您而言，本文展示了 DNN-sieve 在半参数 AFT 模型中的惩罚估计与渐近理论，可作为半参数效率与 debiased ML 方向的对比参考案例。
- **关键技术**: `semiparametric AFT model`, `deep neural network sieve estimation`, `group penalization on first-layer weights`, `selection and estimation consistency`, `asymptotic normality`, `high-dimensional variable selection`
- **为什么对您有用**: 本文直接连接到半参数理论（primary interest），具体展示了 DNN 作为 sieve 估计器在部分线性 AFT 模型中的惩罚收敛与渐近正态性证明。用您 very_familiar 的 minimax bounds 与 M-estimation theory（moderately_familiar）可以审视其 DNN-sieve 的收敛率是否达到最优，以及其渐近正态性证明是否可沿 HOIF / one-step 路线改进至半参数有效估计。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，具体是将 DNN-sieve 的收敛率嵌入到 debiased ML / orthogonal score 框架中，以判断当前一步估计是否达到 semiparametric efficiency bound。

### 3. [10.1093/biomtc/ujag044](https://doi.org/10.1093/biomtc/ujag044) · [arXiv](https://arxiv.org/abs/2506.02524) — Variable selection in functional linear Cox model
- **作者**: Yuanzhen Yue, Stella Self, Yichao Wu, Jiajia Zhang, Rahul Ghosal
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 在功能线性Cox模型框架下，本文研究多个功能协变量和标量协变量的变量选择问题，目标是在高维功能数据下识别与时间-事件结局（全因死亡率）相关的关键预测因子。方法采用B样条基展开近似功能系数，并使用组MCP（minimax concave penalty）惩罚实现组级稀疏性，同时引入二阶差分惩罚确保功能系数的平滑性。通过组下降算法优化正则化路径，并自动选择平滑参数和稀疏参数（如BIC或交叉验证）。模拟研究展示了该方法在变量选择和系数估计方面的准确性。应用在NHANES 2003-2006队列数据上，识别出身体活动的日分布模式（如活动时间、强度分布）与年龄、性别等协变量是重要预测因子。对研究者的意义：该方法结合了半参数建模和高维变量选择，可迁移至其他纵向或功能数据场景；特别是其自动化参数选择流程对软件包开发有参考价值。
- **关键技术**: `spline-based semiparametric estimation`, `group MCP penalty`, `functional linear Cox model`, `group descent algorithm`, `functional coefficient sparsity`
- **为什么对您有用**: 本文连接了流行病学应用（NHANES队列数据）和半参数变量选择方法，属于您的次要兴趣中流行病学应用数据分析方向。武器库中非参数统计（样条估计）可直接用于理解该方法的核心估计步骤，但功能数据和Cox模型的结合需要额外背景，属于暂不可做的范畴，因为功能数据分析和生存分析交叉的工具目前不在武器库中。不过该文的自动化调参思想和组下降算法对统计计算有借鉴意义。

### 4. [10.1093/biomtc/ujag040](https://doi.org/10.1093/biomtc/ujag040) — Reduced varying coefficient models for regional quantile regression with multiple responses
- **作者**: Woorim Jung, Seyoung Park, Hyokyoung G Hong, Eun Ryung Lee
- **期刊/来源**: Biometrics
- **机构**: Sungkyunkwan University · Yonsei University · National Institutes of Health · Center for Cancer Research
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在高维多响应变量设定下，本文研究 regional quantile regression 的估计问题，目标 estimand 为随时间/索引变量变化的分位数系数矩阵，并假设系数矩阵具有低秩结构。核心方法是将多变量分位数变系数模型投影到主成分函数上，对系数矩阵施加低秩约束以实现降维与可解释性，并叠加 KNN-fused LASSO 惩罚以捕捉共享动态模式与潜在聚类。理论方面，文章通过仿真展示了方法在高维场景下估计的准确性与鲁棒性，但摘要未给出显式的收敛率或 minimax 界。实证部分用两个健康数据集揭示了预测变量与多相关结局之间跨分位数的复杂关联。对您可能有用：该文的变系数低秩结构与 KNN-fused LASSO 惩罚机制，可作为 semiparametric 理论中研究 penalized M-estimator 收敛性质的切入点。
- **关键技术**: `regional quantile regression`, `varying coefficient model`, `low-rank coefficient matrix`, `principal component functions`, `KNN-fused LASSO`, `multivariate quantile regression`
- **为什么对您有用**: 本文连接到 semiparametric & nonparametric theory 子方向（变系数模型与 penalized M-estimation）。您武器库中 M-estimation theory（moderately_familiar）可直接用来分析此 penalized low-rank estimator 的 oracle 性质与收敛率，填补该文目前缺失的理论部分。中期可做：需先在 moderately_familiar 的 M-estimation theory 上长肌肉，特别是 fused LASSO 与 low-rank 矩阵惩罚的 oracle inequality 推导，然后可攻其理论收敛率。

### 5. [10.1093/biomtc/ujag002](https://doi.org/10.1093/biomtc/ujag002) — Quasi-likelihood estimation for semiparametric circular regression models
- **作者**: Anna Gottard, Andrea Meilán-Vila, Agnese Panzera
- **期刊/来源**: Biometrics
- **机构**: University of Florence · Universidad Carlos III de Madrid
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在半参数圆形回归模型设定下，目标是对含线性与圆形协变量的圆形响应变量进行估计，不假设误差项的具体参数分布而采用圆形 quasi-likelihood。作者提出 backfitting 算法交替估计参数与非参数分量，并讨论了所得估计量的渐近性质（一致性、收敛率）。核心工具为 circular quasi-likelihood 与局部似然/核光滑等非参数回归技术，规避了 von Mises 等强分布假设。模拟与候鸟迁徙方向的基因组效应实证展示了方法的实用性。对您可能有用：本文的半参数 backfitting 与 quasi-likelihood 思路可作为 semiparametric theory 的一个非标准（圆形数据）案例参考。
- **关键技术**: `semiparametric circular regression`, `circular quasi-likelihood`, `backfitting algorithm`, `local likelihood smoothing`, `asymptotic consistency`
- **为什么对您有用**: 本文连接到 semiparametric theory 子方向，但处理的是圆形数据而非通常的 Euclidean 响应，其 quasi-likelihood 与 backfitting 机制对您熟悉的 M-estimation theory 是一个特殊变体。用 very_familiar 的 M-estimation theory 可以审视其渐近证明是否可推广到更一般的 manifold 响应设定，但本文未涉及 efficiency bound 或 influence function，理论深度有限。判断为**中期可做**：若想在此方向深挖，需先在 moderately_familiar 的 semiparametric theory 上补充 manifold 上的 efficiency bound 文献，当前武器库暂缺圆形/流形空间的 semiparametric efficiency 工具。

### 6. [10.1093/biomtc/ujag004](https://doi.org/10.1093/biomtc/ujag004) · [arXiv](https://arxiv.org/abs/2312.01411) — Bayesian inference for Cox regression models using catalytic prior distributions
- **作者**: Weihao Li, Dongming Huang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对高维小样本下Cox比例风险模型最大偏似然推断不稳定的问题，提出Cox催化先验分布进行贝叶斯推断。该先验构造为基于合成数据与替代基线危险常数的加权似然，合成数据从拟合的简单模型预测分布生成，而替代危险可由用户指定或从数据估计。点估计时推导了边际后验众数的近似，转化为正则化对数偏似然估计量，便于计算。理论上证明该先验是适当的，且所得估计量在温和条件下具有一致性。模拟结果表明，该方法在MSE等指标上优于标准最大偏似然推断，与现有收缩方法（如LASSO）表现相当。该工作将原用于稳定复杂参数模型的催化先验推广至半参数Cox框架，为高维生存数据分析提供了正则化贝叶斯途径。对您而言，可运用高维渐近和极小极大界工具评估其估计量的率最优性，同时该方法可作为流行病学或生存分析应用中处理高维协变量的候选工具。
- **关键技术**: `catalytic prior`, `Cox proportional hazards model`, `regularized partial likelihood`, `synthetic data generation`, `Bayesian inference for survival data`
- **为什么对您有用**: 连接高维统计中半参数模型的正则化推断子方向，您非常熟悉的“高维渐近”可直接检验其一致性证明的严谨性，“极小极大界”经验可用于思考该估计量是否达到最优收敛速度。中期可做：本文涉及M估计框架中正则化似然的近似后验，需先熟悉“M估计理论”（moderately_familiar）才能深入理解其正则化路径与Oracle性质，该论文是一块很好的跳板。

### 7. [10.1093/biomtc/ujaf177](https://doi.org/10.1093/biomtc/ujaf177) · [arXiv](https://arxiv.org/abs/2505.24501) — Inhomogeneous mark correlation functions for general marked point processes
- **作者**: Mehdi Moradi, Matthias Eckardt
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对空间环境中事件分布不均匀且带有标记属性（如树木胸径、高度）的点过程，提出了一类不均匀标记相关函数（inhomogeneous mark correlation functions），用以在显式控制空间非平稳性的同时量化标记间的关联或变异随距离的变化。该方法通过核平滑估计空间强度，并基于标记与强度的关系构造非参数估计量，可区分正/负关联并识别有效空间作用范围。模拟研究表明，在点模式存在聚类或稀疏区域时，传统标记相关函数存在严重偏差，而新方法准确恢复了真实标记结构，且强度估计方式对偏差/方差影响有限。将方法应用于美国佐治亚州长叶松和瑞士Pfynwald苏格兰松的森林数据，发现不均匀标记相关函数揭示了传统方法忽略的生长模式差异。对您可能有用：本文连接了非参数空间统计与您熟悉的minimax评价框架，可运用您的非常规武器库中非参数统计与U-statistics计算经验，进一步分析该估计量的收敛速率或拓展至时空因果推断中的空间敏感性分析。
- **关键技术**: `inhomogeneous mark correlation functions`, `nonparametric estimation`, `spatial point processes`, `kernel smoothing intensity estimation`, `simulation-based performance evaluation`
- **为什么对您有用**: 本文直接关联您的primary interest中的非参数统计理论，您可运用very_familiar的非参数统计知识（minimax bounds、经验过程）来严格分析该估计量的收敛速率和最优性；同时，标记相关函数本身可视为二阶U-statistic形式，您可将higher-order U-statistics的树宽/张量缩并复杂性视角引入，分析其计算成本并设计更高效的算法。follow-up判断：立即可做——您对非参数估计和U-statistics计算已非常熟练，可立即着手推导该估计量的最小最大界或提出更快的张量实现。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujaf166](https://doi.org/10.1093/biomtc/ujaf166) · [arXiv](https://arxiv.org/abs/2506.03393) — Jointly modeling multiple endpoints for efficient treatment effect estimation in randomized controlled trials
- **作者**: Jack M Wolf, Joseph S Koopmeiners, David M Vock
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在随机对照试验设定下，目标是估计主要终点（如戒烟率）的平均处理效应（ATE），当次要终点（如每日吸烟量）与主要终点具有相似处理效应时，利用次要终点信息提升估计效率。本文提出基于主要与次要终点联合模型的处理效应估计量，在模型正确设定时该估计量相较于标准估计量获得效率提升，并通过 model averaging 机制保证在模型误设时仍具有稳健性（即不劣于标准估计量）。核心机制是利用联合建模捕捉终点间的相关性以缩小标准误，同时用 model averaging 防止误设带来的效率损失。实证分析显示，在低尼古丁香烟对黑人吸烟者戒烟比例的效应估计中，该方法将标准误降低了 27%。对您可能有用：该文在 RCT 多终点设定下探索了效率提升与稳健性的折衷，与效率理论（semiparametric efficiency bounds）及因果推断估计理论直接相关。
- **关键技术**: `joint modeling of multiple endpoints`, `model averaging for robustness`, `efficiency gain under correct specification`, `RCT treatment effect estimation`, `subgroup analysis power`
- **为什么对您有用**: 本文连接到效率理论（semiparametric efficiency bounds）与因果推断估计理论，具体是在 RCT 多终点设定下利用辅助信息提升 ATE 估计效率。用您 very_familiar 的 estimation theory in causal inference 可以直接审视其 model averaging 稳健性机制是否达到局部最小方差界，或用 moderately_familiar 的 semiparametric theory 推导该多终点联合模型下的 efficient influence function 以验证其效率增益是否已达到 bound。Follow-up 粗判：**立即可做**——用 very_familiar 的估计理论武器即可动手推导其 semiparametric efficiency bound 并检验 model averaging 是否为最优折衷。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1093/biomtc/ujag048](https://doi.org/10.1093/biomtc/ujag048) · [arXiv](https://arxiv.org/abs/2410.20908) — Making all pairwise comparisons in multi-arm clinical trials without control treatment
- **作者**: T Burnett, T Jaki
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对多臂临床试验中没有对照组的场景，提出了进行所有两两比较的假设检验方法。现有方法如Bonferroni校正过于保守，而本文的方法能精确控制族系错误率（FWER）至期望水平，无保守性，因此提高了统计功效。该方法基于封闭检验原则，通过构造满足特定性质的检验统计量来实现错误率控制。进一步，该方法可灵活扩展到多阶段适应性试验设计，覆盖了大多数自适应试验场景。此外，该方法也可推广至临床试验之外的一般多重比较问题。对于您而言，此工作直接关联您对假设检验的兴趣，且其中精确控制错误率的思路可应用于您在高维或因果推断中涉及的多重比较问题。
- **关键技术**: `closed testing procedure`, `familywise error rate control`, `multistage adaptive design`, `Bonferroni adjustment improvement`
- **为什么对您有用**: 本文直接命中您primary interest中的hypothesis testing，尤其是多重比较错误率控制。您对nonparametric statistics和estimation theory的熟悉使您能快速理解并可能推广该方法至更一般设定（如高维或因果推断中的多重比较）。立即可做：利用您已有的软件开发和假设检验工具，可复现或扩展该方法至您自己的研究场景（如无对照的因果效应比较）。

### 2. [10.1093/biomtc/ujag035](https://doi.org/10.1093/biomtc/ujag035) — Ultra-high-dimensional threshold selection for quantile feature screening with false discovery rate error rate control: a case study on high blood pressure analysis
- **作者**: Saidat Abidemi Sanni, Yan Yu, Zhigen Zhao
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at San Antonio · University of Cincinnati · Temple University
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对超高维分位数特征筛选中的阈值选择问题，提出一种能在控制错误发现率（FDR）的前提下数据自适应选取阈值的方法，重点分析高血压的遗传风险因素。方法构建了对称的quantile mirror（QM）统计量以估计FDR，并采用多次数据拆分提升稳定性，进一步提出Quantile REflection via Data Splitting (QREDS) 及硬阈值特征筛选过程。理论上证明了在正则条件下渐近控制FDR。在Framingham Heart Study数据上的应用验证了多个已知高血压相关遗传位点，同时发现了若干新风险因子。数值模拟表明方法在不同分位数、不同信噪比下均具有良好的FDR控制效果及筛选能力。本文的方法对您的高维渐近理论熟悉领域直接相关，同时流行病学应用可作为secondary interest的实证参考。
- **关键技术**: `quantile mirror statistics`, `multiple data splitting`, `false discovery rate control`, `quantile feature screening`, `high-dimensional variable selection`
- **为什么对您有用**: 本文核心属于高维统计中的特征选择与假设检验（FDR控制），与您非常熟悉的高维渐近理论直接对接；论文中利用数据拆分稳定FDR估计的策略与因果推断中cross‑fitting的思想相似，可启发您在高维因果敏感性分析中引入类似设计。作为流行病学应用，本文展示了真实遗传因子筛选的完整流程，适合作为gateway reading进入该领域。**中期可做**：若想将FDR机制融入您的因果推断工作，需先提升多重假设检验（中熟悉项）的掌握程度。

### 3. [10.1093/biomtc/ujag052](https://doi.org/10.1093/biomtc/ujag052) · [arXiv](https://arxiv.org/abs/2309.10284) — Rank-adaptive covariance testing with applications to genomics and neuroimaging
- **作者**: David Veitch, Yinqiu He, Jun Young Park
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文关注两样本协方差检验问题，尤其当协方差差异由低秩结构驱动而弱分散在高维中时，现有方法功效不足。作者提出秩自适应协方差检验（RACT），基于Ky-Fan(k)范数（前k个奇异值之和）构造检验统计量，并通过置换检验实现精确的I型错误控制。RACT的核心是自适应选择秩k以最大化检验功效，无需对信号结构做先验假设。模拟研究表明，RACT在低秩信号场景下显著优于传统检验方法。实际应用中，RACT成功检测出两种肺癌（肺腺癌与鳞状细胞癌）的基因表达网络差异，以及不同扫描仪类型下扩散张量成像（DTI）数据的协方差异质性。对您而言，该工作直接关联 primary interest 中的 hypothesis testing 方向，并将高维协方差检验与低秩结构洞察相结合，具有实际应用价值。
- **关键技术**: `Ky-Fan(k) norm`, `permutation test`, `rank-adaptive testing`, `two-sample covariance testing`, `low-rank structure`
- **为什么对您有用**: 本文直接针对您 primary interest 中的假设检验问题，特别是高维协方差结构的检验。您熟悉的 high-dimensional asymptotics 和 nonparametric statistics 可以用于分析 RACT 的渐近性质及其置换检验的有限样本行为。从 follow-up 角度看，该问题属于立即可做方向：您可以利用自己熟悉的工具（如极小极大下界、U-statistic）对该方法的检验功效进行理论刻画，或将其扩展到更复杂的因果推断中的协方差平衡检验（如匹配后协变量协方差检验）。

### 4. [10.1093/biomtc/ujag009](https://doi.org/10.1093/biomtc/ujag009) — Repeated inclusion cluster randomized trials: a new class of designs for assessing group-level interventions
- **作者**: Jessica Kasza, Kelsey L Grantham, Rhys Bowden, Brennan C Kahan, Andrew B Forbes
- **期刊/来源**: Biometrics
- **机构**: Monash University · MRC Clinical Trials Unit at UCL · University College London
- **分类**: vol 82 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出一类新的集群随机试验设计——重复纳入集群随机试验（repeated inclusion cluster randomized trials），允许同一集群在同一试验中被多次独立随机化分配干预。核心设定是在 constant treatment effect 与 equal allocation 假设下，比较重复纳入设计与传统不重复设计的检验效能。方法机制依赖集群内纵向相关结构（within-cluster correlation）与跨期比较的方差分解；估计量保持无偏，且通过增加集群内比较次数降低方差。理论结果表明，在总观测数相同的前提下，重复纳入设计的检验效能不低于传统设计，具体增益取决于试验设计类型（如 crossover vs parallel）与集群内相关结构。对您有用之处：本文将重复随机化框架从个体层面推广到集群层面，其方差分解与效能分析思路可迁移至 longitudinal causal inference 中处理 cluster-level repeated exposure 的效率界问题。
- **关键技术**: `cluster randomized trial design`, `re-randomization`, `within-cluster correlation structure`, `variance decomposition for power analysis`, `longitudinal cluster crossover`
- **为什么对您有用**: 本文直接连接 longitudinal causal inference 中 cluster-level repeated exposure 的设计效率问题，其方差分解框架与您熟悉的 minimax bounds / estimation theory 可对接——可用 semiparametric efficiency bound 视角审视其 constant treatment effect 假设下的效能声称是否紧。**中期可做**：需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉，以将本文的 repeated inclusion 设定嵌入更一般的 longitudinal identification 框架并推导无参数效率界。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujag013](https://doi.org/10.1093/biomtc/ujag013) — Non-boundary covariance matrix estimation in generalized linear mixed effects models using data augmentation priors
- **作者**: Tina Košuta, Erik Langerholc, Rok Blagus
- **期刊/来源**: Biometrics
- **机构**: Institute for Medical Informatics and Biostatistics · University of Primorska
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在广义线性混合效应模型(GLMEM)中，最大似然估计常导致随机效应协方差矩阵的边界估计（零方差或奇异），影响数值稳定性与推断。本文通过引入条件共轭先验（对协方差或精度矩阵）构造惩罚似然，该惩罚可等价表示为伪观测(pseudo-observations)形式，从而允许在现有ML软件中通过数据增广实现惩罚估计。核心贡献是设计了一种构造伪观测的算法，使其似然贡献与惩罚的函数形式匹配且仅依赖随机效应的协方差/精度矩阵。方法包含可调的惩罚参数，当无先验信息时作者还提出了完全数据驱动的参数选择程序。模拟研究表明，在若干现实场景下该方法比已有竞争方法估计更准确。真实数据应用进一步验证了实用性。该论文的统计计算思路（数据增广实现惩罚估计）可直接迁移到研究者关注的因果推断中的纵向数据随机效应模型或高维混合模型实现。
- **关键技术**: `data augmentation`, `conditionally conjugate priors`, `penalized likelihood`, `pseudo-observations`, `generalized linear mixed effects models`
- **为什么对您有用**: 本文属于统计计算中的数值方法与算法实现，与您的主要兴趣'statistical computing (numerical methods, algorithm)'直接对应。您的技术武库中'software development'可以直接用来复现或扩展该数据增广框架到因果推断中的纵向数据模型（如中介分析中的随机效应）。目前属于'中期可做'：需要先补齐对混合效应模型识别条件的知识（武器库中当前未列该项），但数据增广的软件实现思路本身可直接动手尝试。

## 流行病学  *(epidemiology, 5 篇)*

### 1. [10.1093/biomtc/ujag019](https://doi.org/10.1093/biomtc/ujag019) · [arXiv](https://arxiv.org/abs/2503.22933) — Improving transportability of regression calibration under the main/external validation study design
- **作者**: Zexiang Li, Donna Spiegelman, Molin Wang, Zuoheng Wang, Xin Zhou
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在流行病学队列研究中，暴露变量常受测量误差影响，传统回归校准法依赖外部验证研究 (EVS) 估计校准模型参数，但若 EVS 参数不可迁移至主研究 (MS) 则导致估计偏倚。本文针对线性回归模型，提出一种改进的回归校准方法：利用 EVS 估计测量误差生成过程的参数，而校准模型中剩余参数直接从 MS 数据中估计，从而确保校准模型对 MS 适用。理论层面推导了估计量的相合性与渐近正态性，模拟结果表明该方法能有效降低偏倚并维持名义覆盖概率。应用部分利用 Health Professionals Follow-Up Study 和 Men's Lifestyle Validation Study 数据，评估膳食摄入对体重的影响，验证了实用性。对您而言，本文是流行病学测量误差校正方法的具体应用，其可迁移性改进思路可与您熟悉的 M-estimation 理论或因果推断中的测量误差处理建立联系。
- **关键技术**: `regression calibration`, `external validation study`, `measurement error model`, `transportability`, `linear regression`, `two-stage estimation`
- **为什么对您有用**: 本文属于流行病学测量误差方法应用，与您的 secondary interest 中流行病学数据与分析直接相关。方法核心是两阶段估计与参数可迁移性诊断，可用您技术库中 very_familiar 的 estimation theory in causal inference（测量误差可视为一种非随机缺失机制）和 moderately_familiar 的 M-estimation theory 来分析估计方程与渐近方差，属于立即可做或只需轻度背景补充即可深入探讨的范围。此外，其应用数据集结构清晰，可作为流行病学因果推断中测量误差校正的案例参考。

### 2. [10.1093/biomtc/ujag001](https://doi.org/10.1093/biomtc/ujag001) — Bayesian randomized basket trial design: a case study from the ultra-rare invasive mold infections
- **作者**: Yunhe Liu, Satrajit Roychoudhury, Wei Wei
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Austin · Pfizer (United States) · Yale Cancer Center
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在罕见侵袭性霉菌感染（IMI）的非劣效性随机篮式试验设定下，目标是估计不同霉菌亚型的处理效应，同时解决罕见病招募困难与亚型异质性问题。本文提出一种贝叶斯借力策略，核心机制包含两部分：(i) 跨霉菌亚型借力处理效应，通过稳健先验（如 power prior / commensurate prior 类机制）在异质性存在时自适应控制借力强度；(ii) 利用外部历史数据扩增对照组，进一步缩减对照组所需样本量。模拟与真实数据表明，该方法在维持 family-wise type I error 的前提下显著提升了统计功效与估计精度，优于将不同亚型简单合并的传统做法。对您可能有用：该文展示了罕见病流行病学试验中贝叶斯借力与外部对照扩增的具体设计，可作为了解流行病学因果推断（处理效应估计）中外部数据整合与异质性建模的入门案例。
- **关键技术**: `Bayesian basket trial design`, `robust borrowing across subtypes`, `external control augmentation`, `noninferiority trial`, `family-wise type I error control`, `power prior / commensurate prior`
- **为什么对您有用**: (1) 本文属于流行病学（epidemiology）应用方向，聚焦罕见病随机试验中的处理效应估计与外部数据借力，直接对应您 secondary interest 中流行病学因果推断的应用场景；(2) 您武器库中 very_familiar 的因果推断估计理论与 moderately_familiar 的识别理论可以用来审视其贝叶斯借力在异质性下的识别假设（如外部对照的可交换性 / transportability），但本文核心是贝叶斯试验设计而非半参数效率理论，技术口径并不直接对口；(3) 判定为**中期可做**：若想在此类罕见病试验中引入 semiparametric efficiency bound 或 debiased ML 做更精确的处理效应估计，需先在 moderately_familiar 的半参数理论上长肌肉以替代其贝叶斯先验框架。

### 3. [10.1093/biomtc/ujag043](https://doi.org/10.1093/biomtc/ujag043) · [arXiv](https://arxiv.org/abs/2505.13202) — SIMBA–a Bayesian decision framework for the identification of optimal biomarker subgroups for cancer basket clinical trials
- **作者**: Shijie Yuan, Jiaxin Liu, Zhihua Gong, Xia Qin, Crystal Qin, Yuan Ji et al.
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对多适应症篮子试验（basket trial）中，目标生物标志物治疗在不同癌种中的疗效评估，提出一个贝叶斯决策框架SIMBA。研究目标是确定最佳biomarker亚组，并制定go/no-go决策规则。方法采用贝叶斯层次模型，在正负biomarker亚组之间共享信息，估计各亚组疗效。通过模拟比较，SIMBA在亚组识别和决策准确性上优于现有方法。该框架直接应用于胃癌、胰腺癌等癌症试验，可提高患者亚群识别效率。对您而言，虽然未直接使用因果推断工具，但其亚组识别和决策框架可与您关注的流行病学应用（临床试验设计）以及可能的异质性因果效应评估相联系。
- **关键技术**: `Bayesian hierarchical model`, `biomarker subgroup identification`, `go/no-go decision`, `multi-indication basket trial`, `simulation-based operating characteristics`
- **为什么对您有用**: 本文属于流行病学和临床试验设计的应用，与您的次要兴趣（流行病学应用）直接相关。它处理的是生物标志物亚组的识别和决策问题，虽然方法上未使用因果推断或高维统计，但亚组分析是异质性治疗效果评估的基础，可启发您使用半参数或因果推断方法改进亚组识别。目前您的武器库缺乏贝叶斯层次建模的熟练度（moderately_familiar以外），但可以从中提炼出亚组定义和决策规则的一般思路，作为中期可做的入口：您可以在因果推断框架下利用biomarker进行亚组识别，并用您熟悉的高维推断工具进行理论分析。论文本身可读性良好，适合作为流行病学应用的入门参考。

### 4. [10.1093/biomtc/ujag036](https://doi.org/10.1093/biomtc/ujag036) — OPERA: a new algorithm for patient stratification based on partially ordered risk factors
- **作者**: Yingzhou Liu, Menggang Yu
- **期刊/来源**: Biometrics
- **机构**: University of Wisconsin–Madison · University of Michigan
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 OPERA（Ordering Poset Elements by Recursive Amalgamation）算法，用于基于具有自然序关系的多个风险因子对患者进行分层，核心设定为风险因子联合构成偏序集（poset）。方法机制上，OPERA 利用偏序集的代数结构进行递归合并，类似决策树可探索高阶交互，但通过 poset 结构约束实现了更灵活的分层模式与更快的剪枝。理论层面，文章未给出收敛率或 minimax 界，主要依赖模拟与癌症分期真实数据验证分层效果。对您而言，本文展示了偏序结构在流行病学分层中的建模价值，但方法学 novelty 偏应用层面。
- **关键技术**: `partially ordered set (poset)`, `recursive amalgamation`, `tree-based pruning`, `risk stratification`, `high-order interaction`
- **为什么对您有用**: 本文属于流行病学应用方向，展示了偏序集（poset）结构在癌症分期等多风险因子分层中的建模与剪枝优势。从武器库看，very_familiar 的 minimax bounds 与 nonparametric statistics 可用来为这类偏序约束下的分层算法建立理论保证（如收敛率、误分层概率界），这是当前文章完全缺失的。follow-up 判断：**中期可做**——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，将偏序约束下的递归合并形式化为 M-estimator，再推导其 asymptotic properties。

### 5. [10.1093/biomtc/ujaf171](https://doi.org/10.1093/biomtc/ujaf171) · [arXiv](https://arxiv.org/abs/2407.17658) — Semiparametric piecewise accelerated failure time model for the analysis of immune-oncology clinical trials
- **作者**: Hisato Sunami, Satoshi Hattori
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 针对免疫肿瘤临床试验中生存函数存在滞后期、比例风险假设不适用的问题，提出半参数分段加速失效时间（Piecewise AFT）模型。该模型通过半参数极大似然方法同时估计滞后期和长期治疗效应参数，并建立识别获益较少患者的框架。与比例风险模型不同，该模型假设治疗组与对照组生存时间在滞后期后成比例加速。估计采用数值优化（如EM算法），数值实验显示各参数估计偏差小。通过实际临床试验数据分析，展示了免疫治疗效果的评估及协变量对患者获益的预测。本文为流行病学中的生存分析应用提供了实用且解释性强的工具。
- **关键技术**: `semiparametric maximum likelihood`, `piecewise accelerated failure time`, `lag-time modeling`, `survival analysis in clinical trials`
- **为什么对您有用**: (1) 直接对应于流行病学（临床试验）中的生存数据分析应用，属于您的次要兴趣。(2) 您可以用半参数M估计理论检查该估计量的渐近性质（如是否达到半参效率界），工具库中的semiparametric theory可胜任。(3) 立即可做——您已有的非参数与半参数知识足以理解和评估该方法，无需额外学习。

## 其他  *(other, 5 篇)*

### 1. [10.1093/biomtc/ujag046](https://doi.org/10.1093/biomtc/ujag046) · [arXiv](https://arxiv.org/abs/2408.15149) — LLOT: application of Laplacian Linear Optimal Transport in spatial transcriptome reconstruction
- **作者**: Junhao Zhu, Kevin Zhang, Dehan Kong, Zhaolei Zhang
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 单细胞RNA测序（scRNA-seq）能提供细胞转录组图谱，但样本制备通常破坏空间位置；空间转录组技术（如Slide-seq）可测量局部基因表达，但无法达到单细胞分辨率。本文提出Laplacian Linear Optimal Transport（LLOT），一种可解释的数据整合方法，用于将scRNA-seq与空间转录组数据结合，在全基因组单细胞分辨率下重建缺失的空间表达信息。LLOT的核心是迭代校正平台效应（platform effect），并利用Laplacian最优传输将空间转录组中的每个spot分解为空间平滑的单细胞概率混合。方法层面，最优传输通过图拉普拉斯正则化增强空间连续性，从而在保持生物学可解释性的同时实现细胞类型定位。作者在多种技术平台（如原位杂交、Slide-seq、10x Visium、Visium HD）的数据集上与多个现有方法进行基准测试，结果表明LLOT在重建空间基因表达和推断细胞位置方面具有竞争性表现。该方法适用于生物信息学中的空间组学数据整合问题，与统计计算中的最优传输及高维数据分析有间接关联。
- **关键技术**: `Laplacian Linear Optimal Transport`, `spatial transcriptomics`, `single-cell RNA-seq integration`, `platform effect correction`, `probabilistic mixture decomposition`, `graph regularization`
- **为什么对您有用**: 本文聚焦空间转录组数据整合，属于生物信息学应用，与您的主要兴趣（因果推断、高维统计等）不直接重叠。但其核心工具——拉普拉斯正则化最优传输——是一种非参数分布对齐方法，在因果推断中的协变量匹配、反事实分布估计等场景有潜在应用价值。您武器库中的「高维渐近」与「非参数统计」可帮助理解其统计性质，但LLOT本身依赖最优传输的线性规划算法，不在您熟悉或中等的技术栈内（如树宽/张量收缩不直接适用）。因此，本文可作为了解最优传输在数据整合中应用的入门材料，但暂不可直接转化为您的研究问题——需要先补充最优传输理论的基础知识。

### 2. [10.1093/biomtc/ujag051](https://doi.org/10.1093/biomtc/ujag051) · [arXiv](https://arxiv.org/abs/2404.03160) — Simultaneous clustering and estimation of additive shape invariant models for recurrent event data
- **作者**: Zitong Zhang, Shizhe Chen
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对神经科学中重复事件数据（neuron spike trains）提出一种新的加性形状不变模型（additive shape invariant model），能够同时实现神经元聚类、估计加性刺激响应成分以及未知的时间平移。在随机刺激实验设定下，模型允许不同簇的神经元对多重刺激有不同的响应形状和延迟。作者建立了模型参数的可识别性条件，为实验设计提供了理论指导。算法方面采用迭代优化策略，通过模拟实验验证了估计的准确性。真实数据分析中，应用Neuropixels探针记录的小鼠视觉辨别任务数据，识别出三个功能不同的神经元群，对两个独立随机刺激表现出异质性响应模式。该方法对您在半参数/非参数理论方面的兴趣有一定参考价值，尤其是其形状不变加性结构可视为一种半参数模型。
- **关键技术**: `additive shape invariant model`, `simultaneous clustering and estimation`, `time-shift estimation`, `identifiability conditions`, `neural spike train analysis`
- **为什么对您有用**: 本文构建的加性形状不变模型属于半参数框架，与您在半参数/非参数理论方面的兴趣有直接交集；其可识别性条件的推导方法与您在因果推断identification理论（moderately_familiar）中的工具可以相互启发。但由于该模型高度依赖神经科学实验的特定结构（刺激随机化、尖峰计数），且未使用您武器库中的高端工具（如U-statistics或高效因子分析），因此仅作为中期可做的参考方向：若未来您希望将半参数方法推广至更一般的重复事件数据，可借鉴其shape-invariant加性分解思路。

### 3. [10.1093/biomtc/ujaf169](https://doi.org/10.1093/biomtc/ujaf169) · [arXiv](https://arxiv.org/abs/2110.09115) — Optimal design of dynamic experiments for scalar-on-function linear models with application to a biopharmaceutical study
- **作者**: Damianos Michaelides, Maria Adamou, David C Woods, Antony M Overstall
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 该文针对标量-函数线性模型（scalar-on-function linear model）下的动态实验，提出了一种贝叶斯最优实验设计框架。实验中某些变量（称为剖面变量）可以随时间变化，设计即每个实验运行中这些函数变量的组合。通过基函数展开将剖面变量表示为有限维参数，从而将无限维设计问题转化为有限维最优设计问题。该方法允许控制变量复杂度和模型复杂度，并基于贝叶斯准则（如期望效用）搜索最优设计。作者在一个实际生物制药案例（Ambr250 系统中的动态喂养策略）上展示了方法的应用。该文的贡献在于将贝叶斯最优设计方法拓展到函数型输入变量，并提供了可实现的算法。对于主要兴趣在因果推断和高维统计的研究者，该文的间接关联在于实验设计思想可能应用于处理时变处理或测量中的函数型协变量，但核心方法学距离较远。
- **关键技术**: `Bayesian optimal experimental design`, `scalar-on-function linear model`, `basis expansions`, `dynamic feeding strategies`, `Ambr250 bioreactor system`
- **为什么对您有用**: 本文属于生物统计领域的应用方法研究，与您的主要兴趣（因果推断、高维统计等）无直接重叠，但函数型线性模型在因果推断中的时变处理或剂量-反应关系中有潜在应用。您的武器库中非参数统计和逆问题经验可帮助理解函数型数据建模的某些理论方面，但核心的贝叶斯最优设计框架（效用函数构造、搜索算法）并非您的熟悉领域。**暂不可做**：该方向需要补充贝叶斯实验设计、函数型数据基展开和优化算法等工具，这些核心机器目前不在您的武器库中。

### 4. [10.1093/biomtc/ujag018](https://doi.org/10.1093/biomtc/ujag018) — Quantifying uncertainty in RNA velocity
- **作者**: Huizi Zhang, Natalia Bochkina, Sara Wade
- **期刊/来源**: Biometrics
- **机构**: Maxwell Institute for Mathematical Sciences
- **分类**: vol 82 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 该论文聚焦单细胞RNA测序中RNA velocity估计的不确定性量化问题。现有方法多缺乏不确定性度量，且常采用不切实际的假设或难以解释的黑箱模型。作者提出一个贝叶斯层次模型，引入时间依赖的转录速率和非平凡初始条件，更贴合生物学过程。模型参数的可识别性被严格讨论，尤其是潜在时间的大值区域，这在既往工作中未被充分处理。为进行完整的贝叶斯推断，设计了一种结合马尔可夫链蒙特卡洛（MCMC）与共识算法的新型采样策略，从而得到校准良好的后验不确定性。仿真实验覆盖多种场景验证了方法的有效性，并在小鼠胚胎干细胞数据上与多种流行方法比较，其估计的基因共享潜在时间和速度向量与细胞周期阶段一致。对您而言，该工作展示了贝叶斯层次模型在复杂动态系统中的应用，其MCMC-共识混合算法思路可以作为统计计算中不确定性量化工具的一个案例。
- **关键技术**: `Bayesian hierarchical model`, `Markov chain Monte Carlo`, `consensus approach`, `identifiability analysis`, `uncertainty quantification`
- **为什么对您有用**: 本文与您的主要兴趣（因果推断、高维统计等）无直接重叠，但属于统计计算中的贝叶斯推断与不确定性量化应用。您可以用非常熟悉的 software development 技能去复现或改进其MCMC-共识算法，但需要先补充贝叶斯层次模型中先验选择与收敛诊断的基础知识（属于 moderately_familiar 以外的领域），因此为中期可做：在您投入少量时间掌握贝叶斯建模后，便可利用现有工具优化其计算效率或扩展至其他时序高维数据。

### 5. [10.1093/biomtc/ujag011](https://doi.org/10.1093/biomtc/ujag011) — Doubly balanced samples with dynamic sample sizes
- **作者**: Blair Robertson, Chris Price, Marco Reale, Philip Davies
- **期刊/来源**: Biometrics
- **机构**: University of Canterbury
- **分类**: vol 82 · issue 1
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文研究空间抽样设计，目标是在给定研究区域内放置样本点以精确估计总体参数，关键假设是环境变量具有正空间关联性且仅需单元间距离度量。作者在近期提出的动态分配抽样（DAS）框架上提出新目标函数，使 master/over-sample 同时满足双重平衡：在辅助变量上近似平衡与空间平衡。方法仅需单元间距离度量，数值实验表明其生成的双重平衡样本在精度上优于传统固定样本量设计。实证部分使用巴西东亚马逊地上生物总量数据验证了方法，并提供了基于设计的方差估计量。对您而言，本文属于抽样设计领域，与因果推断或高维效率理论无直接技术交叉，但其在空间辅助变量上的平衡思路可类比于因果中的协变量平衡抽样。
- **关键技术**: `dynamic assignment sampling`, `doubly balanced sampling`, `spatially balanced design`, `auxiliary variable balancing`, `design-based variance estimation`
- **为什么对您有用**: 本文属于空间抽样设计，与您 primary interests 中的因果推断、高维或效率理论无直接技术重叠。若从因果推断的 covariate balancing / IPW 视角看，空间平衡与辅助变量平衡的联合目标函数构造可类比于因果中同时追求 treatment balance 与 prognostic balance 的设计，但此处无 identification 或 semiparametric efficiency 的深度。您的 very_familiar 武器（minimax bounds / U-stat computation）无法直接攻入此领域，核心缺口是空间抽样与 survey sampling 的 finite-population design-based 理论。**暂不可做**：需先补 survey sampling 的 design-based variance 理论才可评估其效率界是否可被 semiparametric 视角重新刻画。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

