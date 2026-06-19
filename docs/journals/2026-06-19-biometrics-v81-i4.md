# Biometrics — Vol 81  Issue 4  ·  2026-06-19

- 共 34 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 4 篇（对照 OpenAlex 42 篇）：10.1093/biomtc/ujaf075、10.1093/biomtc/ujaf096、10.1093/biomtc/ujaf106、10.1093/biomtc/ujaf108

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期共 34 篇论文，主要汇聚在三条方法主线上。最密集的是**因果推断**（约 9 篇），围绕因果效应的定义、异质性和效率展开，覆盖微随机试验、生存数据、观测研究和两阶段设计等场景。其次是**半参数/非参数方法**（约 6 篇），通过深度网络、贝叶斯非参和空间混合等工具扩展传统模型的灵活性。此外，**高维推断与假设检验**（约 5 篇）在高维图模型、因子分析和生存回归中提供了新的推断和选择工具。流行病学应用（14 篇）虽数量最大，但多为上述方法的具体落地或设计改进，如生存外推、漏诊校正、多状态预测和剂量优化。

因果推断主线有多个推进方向。**远端因果游走效应**（DCEE）将微随机试验的因果度量从近端延伸到远端，提出 marginalization 策略和双鲁棒估计器。**异质性处理效应**（HTE）出现了三条并行路径：（1）生存数据下的 HTE 估计通过 penalized sieve 结合 RCT 与 RWD，用 omnibus bias function 统一刻画偏差来源；（2）非参数处理效应变量重要性（TE-VIMs）基于有效影响函数给出 CATE 预测误差的增量度量，可与任意 CATE 估计器配合；（3）DINA 参数将 HTE 扩展到指数族和 Cox 模型的自然参数差，并借助 Neyman 正交性实现对 nuisance 误设的鲁棒性。测量误差方面，控制变量法在两阶段设计中达到双鲁棒性。元学习方法 DR-WCLS 将双鲁棒思想引入 MRT 的因果游走效应估计，允许随机化概率未知且处理缺失。剂量匹配的敏感性分析和自适应分层设计（AdaStrat）分别补充了匹配研究和两阶段抽样中的推断与效率工具。IIW-GEE 则从访视率模型的变量选择角度澄清了协变量对效率的影响。

半参数/非参方面，**深度偏线性变换模型**在生存数据下结合 DNN 和 profile MLE，给出了参数部分的 n^{-1/2}-CAN 和非参数部分的 minimax 速率。**广义非参数时间模型**同时建模复发性事件的多时间尺度，通过双核局部似然统一乘法和加法强度。**贝叶斯分位数回归**针对计数数据引入生成式潜在变量和 BNP 核混合，避免了离散分位数的不连续问题。**贝叶斯单调单指标分位数回归**处理有界响应和错位功能性协变量，同时保证估计在边界内。**半参数空间混合模型**在空间聚类中允许混合概率非参数依赖位置，并建立参数分量的渐近正态性。此外，**贝叶斯 ODE 系统识别**通过 collocation 和 group-sparse prior 实现稀疏结构选择和不确定性量化。

高维方法主线集中在三类设置。**协变量依赖的高维图回归**用多任务学习估计精度矩阵，并通过去偏投影得到渐近正态的节点推断，计算复杂度控制在样本量级别。**广义因子模型**中 entrywise splitting CV 解决了传统样本拆分低估因子数的问题，在混合数据类型和随机缺失下证明了选择一致性。**高维 additive hazards 回归**在协变量含测量误差时利用最近 PSD 投影将非凸目标凸化，提出 SPLasso 并建立模型选择一致性和 oracle inequality。假设检验方面，**双重稳健条件独立性检验**在右删失生存数据下通过重采样逼近似然比分布，只要因果或暴露模型之一正确即可控制 I 类错误；**序贯检验回归**将 MaxSPRT 扩展以纳入混杂协变量，适用于疫苗不良反应监测。

若重点关注因果推断，可优先看 DCEE（远端效应与微随机试验）、TE-VIMs（异质性变量重要性）、控制变量测量误差框架、DR-WCLS（元学习双鲁棒）以及 DINA（统一自然参数差异）。半参数效率方向值得留意联邦 DML、半参数空间混合和深度偏线性模型的渐近理论。高维推断方向最相关的三篇是高维图回归的去偏估计、entrywise splitting CV 和 SPLasso。

## 因果推断  *(causal_inference, 9 篇)*

### 1. [10.1093/biomtc/ujaf134](https://doi.org/10.1093/biomtc/ujaf134) · [arXiv](https://arxiv.org/abs/2502.13500) — Distal causal excursion effects: modeling long-term effects of time-varying treatments in micro-randomized trials
- **作者**: Tianchen Qian
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向微随机试验（MRT）设定下，目标是量化时变干预对远端结果的长期因果效应，克服现有因果游走效应（CEE）仅适用于近端结果的局限。本文提出新 estimand——远端因果游走效应（DCEE），通过对比两种游走策略下的远端结果并对大部分干预分配进行边际化，在决策点众多时仍保持模型的简约与可解释性。作者构造了两个估计器（含 cross-fitting 与不含），均对结果模型误设具有鲁棒性，并建立了其渐近性质（n^{-1/2}-CAN）。模拟验证了估计器的表现；HeartSteps MRT 实证表明早期推送的长期习惯养成效应显著强于晚期，凸显干预时机的重要性。对您有用：本文直接推进了 longitudinal causal inference 的 estimand 与估计理论，其 cross-fitting + robust-to-outcome-misspecification 的估计策略与您熟悉的 semiparametric efficiency / DML 框架高度同构。
- **关键技术**: `distal causal excursion effect`, `micro-randomized trials`, `cross-fitting`, `robustness to outcome model misspecification`, `longitudinal time-varying treatment`, `marginalization over treatment assignments`
- **为什么对您有用**: 本文直接连接到 primary interest 中的 longitudinal causal inference 与 estimation theory，提出了针对时变干预长期效应的新 estimand 及具备部分鲁棒性的估计器。您武器库中 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 可直接攻入其估计器的效率界分析——当前估计器仅声称对 outcome model 棒，但未讨论是否达到 semiparametric efficiency bound，这是一个立即可做的 follow-up 方向。

### 2. [10.1093/biomtc/ujaf131](https://doi.org/10.1093/biomtc/ujaf131) · [arXiv](https://arxiv.org/abs/2503.15745) — Statistical inference for heterogeneous treatment effect with right-censored data from synthesizing randomized clinical trials and real-world data
- **作者**: Guangcai Mao, Shu Yang, Xiaofei Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据下，目标是估计由协变量条件下的处理特异性受限平均生存时间差定义的异质性处理效应（HTE），通过综合随机临床试验（RCT）与可能存在偏差的真实世界数据（RWD）。作者定义了一个 omnibus bias function 以统一刻画未测量混杂、删失与结局异质性导致的偏差，并通过结合 RCT 与 RWD 数据实现该偏差函数的 identification。估计方面，提出 penalized sieve 方法同时估计 HTE 与偏差函数，理论分析基于 RKHS 与经验过程理论，证明 integrative estimator 的收敛性质。模拟与早期非小细胞肺癌 RCT+registry 数据的整合分析显示，该方法优于仅用 RCT 数据的估计。对您可能有用：本文将 semiparametric sieve 估计与因果 identification 结合处理 RWD 偏差，直接连接 causal inference 的 identification/estimation 与 semiparametric/nonparametric theory 两个子方向。
- **关键技术**: `omnibus bias function identification`, `penalized sieve estimation`, `reproducing kernel Hilbert space (RKHS)`, `empirical process theory`, `restricted mean survival time (RMST)`, `data fusion / integrative analysis`
- **为什么对您有用**: 本文直接连接 causal inference 的 identification/estimation 子方向（RWD 偏差的 identification 与 HTE 估计）以及 semiparametric/nonparametric theory 子方向（RKHS penalized sieve）。您武器库中 moderately_familiar 的 semiparametric theory 与 M-estimation theory 可直接攻本文 sieve estimator 的收敛率与 semiparametric efficiency bound 缺口——本文未讨论 efficiency bound，这是一个可切入的理论口子。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，推导该 penalized sieve estimator 的 influence function 与 efficiency bound。

### 3. [10.1093/biomtc/ujaf140](https://doi.org/10.1093/biomtc/ujaf140) · [arXiv](https://arxiv.org/abs/2204.06030) — Variable importance measures for heterogeneous treatment effects
- **作者**: Oliver J Hines, Karla Diaz-Ordaz, Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究个性化医疗中异质性处理效应的变量重要性度量。在条件平均处理效应（CATE）的框架下，提出了非参数处理效应变量重要性测量（TE-VIMs），定义为当变量从CATE条件集中移除时，个体处理效应预测均方误差的增加量。推导了高效的TE-VIM估计量，该估计量基于有效影响函数，可与任何CATE估计策略（包括机器学习方法）结合使用。提出了多种VIM计算策略（如留一法、保留一法），并利用元学习器进行CATE估计。通过模拟研究评估了有限样本性能，并应用临床试验数据进行了实证分析。该工作为理解处理效应异质性的驱动因素提供了正式的非参数工具，与您在因果推断和非参数估计方面的研究直接相关。
- **关键技术**: `heterogeneous treatment effects`, `conditional average treatment effect (CATE)`, `variable importance measures (VIMs)`, `efficient influence function`, `meta-learners`, `nonparametric estimation`
- **为什么对您有用**: 本文直接连接您在因果推断中的非参数异质性处理效应和变量选择子方向。您对非参数统计学和因果推断估计理论非常熟悉，因此可以立即理解其估计方法和理论性质。这是一个立即可做的方向：您可以基于本文的TE-VIM框架，进一步研究其在敏感性分析或工具变量设定下的推广，或者结合您的高阶U-统计量知识开发更高效的计算算法。

### 4. [10.1093/biomtc/ujaf151](https://doi.org/10.1093/biomtc/ujaf151) · [arXiv](https://arxiv.org/abs/2410.12590) — Flexible and efficient estimation of causal effects with error-prone exposures: a control variates approach for measurement error
- **作者**: Keith Barnatchez, Rachel Nethery, Bryan E Shepherd, Giovanni Parmigiani, Kevin P Josey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文针对观察性研究中暴露变量测量误差导致的因果推断偏倚问题，提出了一种基于控制变量法的灵活估计框架。方法适用于两相抽样设计，其中验证子样本包含金标准暴露测量，而全体样本仅有含误差的暴露数据。估计量由验证子样本的初始一致估计量加上基于全体数据构建的方差缩减项构成，本质上是控制变量技巧的推广。理论表明，在标准因果假设下该估计量具有双稳健性（double robustness），即只要暴露模型或结果模型中有一个正确指定，估计量仍保持一致。模拟研究显示，在多种两相抽样方案下该方法相比回归校准、多重插补等主流方法有更小的均方误差和更好的覆盖概率。实证部分以HIV电子健康记录数据为例展示了实际可行性。对您而言，该工作直接对应因果推断中测量误差这一核心挑战，其控制变量框架可借由您熟悉的因果推断估计理论（very_familiar）进一步分析效率最优性，例如推导影响函数或半参效率界。
- **关键技术**: `control variates`, `two-phase sampling`, `measurement error`, `double robustness`, `variance reduction`
- **为什么对您有用**: 本文直接处理 causal inference 中的暴露测量误差问题，属于您 primary interest 的子方向。您 very_familiar 的 estimation theory in causal inference 可用来分析该控制变量估计量的一致性和渐近方差；moderately_familiar 的 semiparametric theory 可用于检验其是否达到半参效率界。立即可做：用因果推断估计理论分析其方差缩减项与影响函数的联系，并与现有半参有效估计量（如 TMLE）做对比。

### 5. [10.1093/biomtc/ujaf129](https://doi.org/10.1093/biomtc/ujaf129) · [arXiv](https://arxiv.org/abs/2306.16297) — A meta-learning method for estimation of causal excursion effects to assess time-varying moderation
- **作者**: Jieru Shi, Walter Dempsey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对微随机试验（MRT）中因果瞬时效应（causal excursion effects）的估计问题，提出了一种基于元学习视角的双稳健推断过程DR-WCLS。现有方法假设随机化概率已知、观测完整且高维历史特征的线性模型正确设定，在移动健康数据的复杂环境下这些假设常被违反。DR-WCLS采用双稳健加权中心最小二乘估计，不要求随机化概率已知或线性模型正确，且能处理缺失观测。作者建立了估计量的双向渐近性质（bidirectional asymptotic properties），并在理论上和模拟中与现有方法比较，证明其一致且更高效。最后通过分析美国医学生队列数据展示了方法的实用性。本文对您有用：直接关联您主要兴趣中的纵向因果推断与效率理论，特别是双稳健估计在复杂纵向数据下的理论分析。
- **关键技术**: `Micro-randomized trials (MRTs)`, `Causal excursion effects`, `Doubly robust estimation`, `Weighted-centered least squares (WCLS)`, `Meta-learner`, `Bidirectional asymptotics`
- **为什么对您有用**: 连接到您的主要研究方向：纵向因果推断中的因果瞬时效应估计，以及效率理论（双稳健推断的渐近效率）。武器库中的‘因果推断估计理论’（very_familiar）和‘半参理论’（moderately_familiar）可直接用于审阅其双稳健机制与渐近论证。mid-term可做：在moderately_familiar的高阶影响函数（HOIF）上进一步训练后，可尝试构造高阶影响函数提升该估计量在复杂缺失机制下的效率。

### 6. [10.1093/biomtc/ujaf156](https://doi.org/10.1093/biomtc/ujaf156) · [arXiv](https://arxiv.org/abs/2409.12848) — Bridging the gap between design and analysis: randomization inference and sensitivity analysis for matched observational studies with treatment doses
- **作者**: Jeffrey Zhang, Siyu Heng
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 针对剂量匹配观察性研究（连续或有序处理）中缺乏有效随机化推断和敏感性分析方法的问题，本文提出了新方法。在无未测混杂假设下，该方法适用于一般匹配设计，同时覆盖 Fisher 精确零假设（对非二元结局）和 Neyman 型弱零假设（样本平均处理效应类似物），且可用于二元、有序或连续结局变量。方法核心是利用匹配后的随机化分布构造检验统计量，并通过置换推断实现，同时引入基于 Rosenbaum 框架的敏感性分析。通过模拟和实际数据验证，表明方法具有良好的有限样本性质。所有方法已集成到 R 包 doseSens 中。该工作直接服务于因果推断中的敏感性分析，与您对匹配设计和处理剂量估计的关注高度相关。
- **关键技术**: `randomization inference`, `sensitivity analysis`, `matched observational studies`, `treatment doses`, `Fisher's sharp null`, `Neyman-type weak null`, `R package doseSens`
- **为什么对您有用**: 本文直接针对因果推断中敏感性分析子方向，处理剂量匹配设计这一尚未被充分覆盖的场景。您非常熟悉的 estimation theory in causal inference 可立即用于评估该方法的假设合理性及扩展方向（如引入高效影响函数以提升效率）。立即可做：方法本身已提供 R 包，您可基于现有工具快速复现并测试其性能。

### 7. [10.1093/biomtc/ujaf162](https://doi.org/10.1093/biomtc/ujaf162) · [arXiv](https://arxiv.org/abs/2103.04277) — Estimating heterogeneous treatment effects for general responses
- **作者**: Zijun Gao, Trevor Hastie
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对异质性处理效应（HTE）估计问题，提出了一种新的目标参数——DINA（DIfference in NAtural parameters），用于量化处理组与对照组在指数族分布与Cox模型下的自然参数差异。与传统的条件均值差（CATE）相比，DINA对响应类型（连续、二值、计数、生存）具有统一的表达形式，且更便于建模协变量对处理效应的影响。文章给出了DINA的半参数识别条件与基于Neyman正交性的元算法，允许研究者直接使用现成的机器学习工具（如随机森林、boosting等）估计 nuisance 函数，并证明该算法对nuisance估计误差具有鲁棒性。通过理论推导和数值实验，作者展示了DINA在不同基学习器组合下均能保持有效的推断性能。该工作为因果推断中异质性效应的度量提供了新视角，尤其在响应类型多样（如流行病学中的二值/计数结局）时更具实用性。
- **关键技术**: `exponential family`, `natural parameters`, `meta-algorithm`, `Neyman orthogonality`, `off-the-shelf ML`
- **为什么对您有用**: 该论文直接关联你的主要兴趣『因果推断』中的异质性处理效应估计（HTE），尤其提出了一种对多种响应类型统一的自然参数差异度量（DINA），且元算法对nuisance误差的鲁棒性暗示了某种双稳健性或正交估计结构。这一思路与你武器库中『estimation theory in causal inference』紧密对应，可用你熟悉的半参数效率理论（moderately_familiar中的『semiparametric theory』）深入分析DINA的正交得分及影响函数形式，从而评估其效率损失或改进空间。立即可做：利用现成ML工具实现此元算法并应用于你手头的流行病学或经济数据集（如二值/生存结局的ATE估计），与现有CATE方法作对比。

### 8. [10.1093/biomtc/ujaf143](https://doi.org/10.1093/biomtc/ujaf143) — Adaptive stratified sampling design in two-phase studies for average causal effect estimation
- **作者**: Min Zeng, Qiyu Wang, Zijian Sui, Hong Zhang, Jinfeng Xu
- **期刊/来源**: Biometrics
- **机构**: City University of Hong Kong · Anhui University of Finance and Economics · Artificial Intelligence in Medicine (Canada)
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在两阶段观测研究设定下，目标是估计平均因果效应（ACE），其中昂贵混杂变量仅在第二阶段子样本中测量。本文提出自适应分层抽样设计（AdaStrat），先随机抽取 pilot 数据测量昂贵混杂，据此构建分层策略与各层抽样概率，再对第一阶段全体实施该策略以确定第二阶段样本。作者严格证明，在给定第二阶段样本量下，AdaStrat 产生的 ACE 估计量方差小于固定分层抽样（FixStrat），本质上是一种针对 semiparametric efficiency 的最优设计。模拟与 UK Biobank 实证显示 AdaStrat 相对 FixStrat 的相对效率提升约 20%-30%。对您可能有用：此设计视角可直接连接到您 primary interest 中因果推断的 estimation theory 与 semiparametric efficiency bound，为两阶段缺失数据下的最优抽样提供理论基准。
- **关键技术**: `two-phase sampling design`, `adaptive stratification`, `average causal effect estimation`, `semiparametric efficiency`, `pilot-based sampling probability`, `relative efficiency comparison`
- **为什么对您有用**: 直接连接到您 primary interest 中因果推断的 estimation theory 与 semiparametric efficiency bound——本文本质上是在两阶段缺失混杂设定下，用 pilot 数据逼近使 ACE 估计量达到最小方差（即逼近 semiparametric efficiency bound）的分层抽样概率。您武器库中 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 可以直接攻入：验证其声称的效率提升是否真正逼近了该设定下的 semiparametric efficiency bound，或用 HOIF 视角审视更高阶修正是否能在 AdaStrat 框架中进一步压低方差。**立即可做**：用 very_familiar 的 estimation theory 与 minimax bound 工具分析其效率声称的紧性。

### 9. [10.1093/biomtc/ujaf128](https://doi.org/10.1093/biomtc/ujaf128) — Inverse-intensity weighted generalized estimating equations for longitudinal data subject to irregular observation: which variables should be included in the visit rate model?
- **作者**: Eleanor M Pullenayegum, Di Shan
- **期刊/来源**: Biometrics
- **机构**: University of Toronto · Hospital for Sick Children · Public Health Ontario
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 针对纵向数据中不规则的且可能带有信息性的访视时间，本文探讨了在逆概率加权广义估计方程（IIW-GEE）框架下，访视率模型应包含哪些协变量的问题。当结果变量与访视时间在给定模型协变量后条件独立时，IIW-GEE给出渐近无偏估计。加入其他协变量不会改变渐近无偏性，但对方差的影响未知。本文证明了：加入与结果和访视过程均无关的变量不改变方差；加入仅与结果相关的变量会降低方差；而加入仅与访视过程相关的变量则可能增大或减小方差，具体取决于协变量与结果的相关结构。通过一项抑郁症研究的数据应用，发现仅预测访视但不预测结果的变量可能导致方差增大至两倍。本文建议访视过程模型应包含与结果相关的变量，而对与结果无关的变量需谨慎使用。该结果对处理纵向数据中信息性访视时间的因果推断研究有直接指导意义。
- **关键技术**: `inverse probability weighting`, `generalized estimating equations`, `longitudinal data`, `informative visit times`, `variance analysis`, `asymptotic theory`
- **为什么对您有用**: 本文属于因果推断中纵向数据处理的逆概率加权方法，直接对接您对纵向因果推断（longitudinal causal inference）的兴趣。其核心理论（方差随协变量选择的变化）可以进一步利用您的非参数统计和最小化界工具来推导更一般的方差界，或在高维协变量场景下验证结果。中期可做：将当前结果推广到时间依赖性的处理效应或时依混杂情形，这需要巩固您中等熟悉的识别理论（identification theory）。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 3 篇)*

### 1. [10.1093/biomtc/ujaf165](https://doi.org/10.1093/biomtc/ujaf165) — Statistical inference on high-dimensional covariate-dependent Gaussian graphical regressions
- **作者**: Xuran Meng, Jingfei Zhang, Yi Li
- **期刊/来源**: Biometrics
- **机构**: University of Michigan · Emory University
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究协变量依赖的高维高斯图回归，即精度矩阵随高维协变量变化。传统高斯图模型忽略协变量，无法刻画异质性。作者采用多任务学习（multi-task learning）框架估计模型，相比逐节点回归误差更低。为进行统计推断，提出一类基于多任务学习器的去偏估计量，并引入新的投影技术估计逆协方差矩阵，将计算复杂度降至样本规模级别。理论上，所提估计量达到快速收敛和渐近正态性，支持有效推断。模拟和脑癌基因表达数据应用验证了方法实用性。与您的高维统计和推断兴趣直接相关，去偏思路类似去偏机器学习，可联系效率理论中影响函数框架。
- **关键技术**: `multi-task learning`, `debiased estimator`, `projection method for inverse covariance`, `asymptotic normality`, `high-dimensional graphical model`
- **为什么对您有用**: 直接连接到您的高维统计兴趣中的图模型推断问题。本文使用的去偏估计技术类似因果推断中的去偏机器学习，可用您非常熟悉的高维渐近理论和 moderately_familiar 的半参数理论中影响函数视角检验其最优性。属于立即可做的范畴——已有的高维渐近工具可直接用于分析此类估计量的收敛性质和推断有效性。

### 2. [10.1093/biomtc/ujaf153](https://doi.org/10.1093/biomtc/ujaf153) — Entrywise splitting cross-validation in generalized factor models: from sample splitting to entrywise splitting
- **作者**: Zhijing Wang
- **期刊/来源**: Biometrics
- **机构**: Shanghai Jiao Tong University
- **分类**: vol 81 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在广义因子模型（涵盖连续、二元、计数等混合数据类型）设定下，目标是确定因子数 K 的选择问题，核心难点在于传统样本拆分 CV 在高维因子模型中易低估因子数。本文提出基于 entrywise splitting（ES）的交叉验证方法，将矩阵的元素级而非样本级拆分作为训练/验证集，避免了样本拆分破坏因子结构导致的低估倾向。进一步引入惩罚项融合信息论准则，提出 penalized ES-CV，在高维设定（n, p → ∞）及温和条件下证明了选择一致性。方法还扩展至不同缺失概率场景的随机缺失数据，并通过模拟与单细胞 RNA 测序数据验证了表现。对您可能有用：ES-CV 的元素级拆分思想为高维因子模型的模型选择提供了新视角，其一致性证明涉及的高维渐近分析可衔接您的高维渐近与 RMT 工具。
- **关键技术**: `generalized factor model`, `entrywise splitting cross-validation`, `penalized information criterion`, `factor number selection consistency`, `high-dimensional asymptotics`, `random missing data imputation`
- **为什么对您有用**: 直接连接您的高维统计与 RMT 方向——广义因子模型的因子数选择是高维渐近中的经典开放问题，本文的 entrywise splitting 思想绕过了传统 sample splitting 的结构破坏问题，惩罚项的一致性证明在高维渐近框架下进行。您可以用 very_familiar 的高维渐近工具直接审视其一致性条件是否可进一步放松，或用 moderately_familiar 的 M-estimation theory 分析 penalized ES-CV 的极值点性质。**立即可做**：用高维渐近与 minimax 视角评估其 rate 是否紧，并探索 entrywise splitting 在其他矩阵估计问题中的可移植性。

### 3. [10.1093/biomtc/ujaf130](https://doi.org/10.1093/biomtc/ujaf130) — SPLasso for high-dimensional additive hazards regression with covariate measurement error
- **作者**: Jiarui Zhang, Hongsheng Liu, Xin Chen, Jinfeng Xu
- **期刊/来源**: Biometrics
- **机构**: Hong Kong University of Science and Technology · University of Hong Kong · University of North Carolina at Chapel Hill · Southern University of Science and Technology · City University of Hong Kong
- **分类**: vol 81 · issue 4
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维带测量误差的生存数据设定下，目标是 additive hazards 模型中回归参数的估计与变量选择，关键假设为协变量测量误差矩阵已知或可估计且噪声导致目标函数非凸。作者提出 error-in-variables additive hazards 模型，利用最近正半定矩阵投影（nearest PSD projection）将非凸修正目标凸化，构造 SPLasso 及软阈值变体 SPLasso-T。理论方面，在温和条件下证明了模型选择一致性、oracle inequality 及极限分布；核心工具为 PSD 投影恢复凸性及高维 Lasso 的稀疏恢复理论。仿真与两个真实数据（含缺失值场景）显示方法在效率与鲁棒性上优于现有做法。对您可能有用：该文将矩阵 PSD 投影作为高维非凸纠偏的计算桥梁，与您熟悉的高维渐近理论及矩阵数值计算工具直接对接。
- **关键技术**: `nearest positive semi-definite matrix projection`, `error-in-variables additive hazards model`, `high-dimensional Lasso variable selection`, `oracle inequality`, `model selection consistency`, `non-convex optimization correction`
- **为什么对您有用**: 本文连接到您 primary interest 中的高维统计与统计计算：PSD 投影修正测量误差导致的非凸性，本质上是一个矩阵数值方法（最近 PSD 投影）与高维 Lasso 理论的交叉，您在 very_familiar 的高维渐近理论与软件/矩阵计算上可直接审视其 oracle inequality 与极限分布的紧性。follow-up 判断：**立即可做**——用您熟悉的高维 minimax 理论与矩阵计算工具，可验证其 PSD 投影步骤在更一般误差结构下的理论性质或计算加速。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1093/biomtc/ujaf149](https://doi.org/10.1093/biomtc/ujaf149) · [arXiv](https://arxiv.org/abs/2510.16421) — A semiparametric Gaussian Mixture Model with spatial dependence and its application to whole-slide image clustering analysis
- **作者**: Baichen Yu, Jin Liu, Hansheng Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在无监督聚类设定下提出半参数空间混合模型（SGMM），目标 estimand 为空间依赖的混合概率与条件 GMM 参数，关键假设是实例位置随机且同类实例空间聚集。核心机制在于令混合概率非参数地依赖空间位置，从而突破经典 GMM 的参数混合限制；估计采用专门设计的 EM 算法，理论部分建立了参数分量的 n^{-1/2}-CAN 性与渐近正态性。仿真与 CAMELYON16 乳腺癌全切片图像数据实证表明该方法在空间聚类任务上优于经典 GMM。对您而言，该文的非参数混合概率设定与 EM 下的 M-estimation 渐近理论可连接到半参数效率与 M-estimation 理论方向。
- **关键技术**: `semiparametric Gaussian mixture model`, `nonparametric mixing probability`, `EM algorithm for spatial clustering`, `M-estimation asymptotic theory`, `whole-slide image analysis`
- **为什么对您有用**: 本文连接到 primary interest 中的半参数理论与 M-estimation 理论子方向；您可用 technical_arsenal 中 moderately_familiar 的 M-estimation 理论与 semiparametric theory 来审视其 EM 估计量的渐近效率是否达到半参数效率界，或探讨非参数混合概率部分的 sieve 估计收敛率。Follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以补足对非参数混合概率下 EM 渐近效率分析的工具。

### 2. [10.1093/biomtc/ujaf146](https://doi.org/10.1093/biomtc/ujaf146) — Generalized nonparametric temporal modeling of recurrent events with application to a malaria vaccine trial
- **作者**: Fei Heng, Yanqing Sun, Jing Xu, Peter B Gilbert
- **期刊/来源**: Biometrics
- **机构**: University of North Florida · University of North Carolina at Charlotte · Cape Town HVTN Immunology Laboratory / Hutchinson Centre Research Institute of South Africa · Infectious Disease Research Institute · Fred Hutch Cancer Center · University of Washington · Cancer Research And Biostatistics
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 该论文针对复发性事件提出广义非参数时间强度模型，允许同时建模多个时间尺度对事件强度的影响。通过链接函数的选择，模型统一了乘法强度模型和加法强度模型。估计采用局部线性平滑结合双核的极大似然方法，并开发了自适应算法处理协变量重叠问题以及交叉验证带宽选择。论文建立了估计量的渐近性质，包括一致性和渐近正态性。模拟研究验证了有限样本下乘法和加法模型的表现。实际数据应用来自疟疾疫苗效力试验，分析了新感染风险随时间的变化以及先前感染或接种对后续感染风险的影响。该方法为疫苗保护效应的动态刻画提供了新视角。
- **关键技术**: `local linear smoothing`, `double kernels`, `maximum likelihood estimation`, `cross-validation bandwidth selection`, `multiplicative/additive temporal intensity model`
- **为什么对您有用**: 本文属于非参数统计方法在纵向复发性事件中的应用，连接您的“非参数与半参数理论”和“流行病学应用”兴趣。非参数局部平滑与双核估计器是您非常熟悉的工具（very_familiar: nonparametric statistics），您可以直接理解其理论框架并可能基于它扩展至因果推断场景（例如考虑时变混淆）。立即可做：阅读全文以评估该方法能否用于您自己的纵向因果推断项目中的描述性分析。

### 3. [10.1093/biomtc/ujaf126](https://doi.org/10.1093/biomtc/ujaf126) · [arXiv](https://arxiv.org/abs/2412.07611) — Deep partially linear transformation model for right-censored survival data
- **作者**: Junkai Yin, Yue Zhang, Zhangsheng Yu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在右截断生存数据下，本文提出 deep partially linear transformation model，目标是在 semiparametric transformation 模型框架中对线性参数部分与 DNN 非参数部分进行联合估计，以规避维度灾难并保留部分协变量的可解释性。核心机制基于 profile maximum likelihood estimation：先通过 DNN 逼近非参数成分，再对参数部分做 M-estimation。理论方面，作者证明了 DNN 非参数估计的 minimax lower bound 与整体 MLE 的收敛速率，并关键地建立了参数估计的 n^{-1/2}-CAN 与 semiparametric efficiency。仿真与真实数据验证了估计精度与预测表现。对您可能有用：本文将 DNN sieve 嵌入经典 semiparametric transformation 模型并给出完整的 efficiency 理论，直接连接您关注的 semiparametric efficiency bounds 与 nonparametric theory。
- **关键技术**: `semiparametric transformation model`, `deep neural network sieve estimation`, `profile maximum likelihood`, `minimax lower bound`, `semiparametric efficiency`, `right-censored survival data`
- **为什么对您有用**: 本文直接触及您 primary interest 中的 semiparametric efficiency bounds 与 nonparametric theory 子方向，给出了 DNN sieve 在生存分析 transformation model 下的完整 minimax rate 与 efficiency 结果。您武器库中 very_familiar 的 minimax bounds 与 moderately_familiar 的 semiparametric theory / M-estimation theory 完全足以攻入本文的 profile MLE 与 efficiency bound 推导细节。**立即可做**：用您熟悉的 minimax 理论审视其 DNN 非参数部分的 lower bound 是否紧，并用 semiparametric theory 验证其声称的 efficient influence function 推导是否完备。

### 4. [10.1093/biomtc/ujaf152](https://doi.org/10.1093/biomtc/ujaf152) — Flexible Bayesian quantile regression for counts via generative modeling
- **作者**: Yuta Yamauchi, Genya Kobayashi, Shonosuke Sugasawa
- **期刊/来源**: Biometrics
- **机构**: Nagoya University · Meiji University · Keio University
- **分类**: vol 81 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在计数数据的分位数回归设定下，目标是估计条件分位数上的回归参数，解决离散响应导致分位数非连续且难以直接建模的问题。本文提出一种生成式贝叶斯框架：引入与观测计数关联的潜在连续变量，通过最小化该潜在变量条件分位数分布下的期望损失来定义目标参数。对计数响应与协变量的联合分布采用贝叶斯非参数核混合（BNP kernel mixture）建模，从而将回归参数的后验推断转化为简单的优化问题。数值实验表明，相比现有粗略方法，该框架在偏差与估计精度上有明显改善；在急性心肌梗死住院时长数据的应用中展示了更灵活、可解释的结果。对您可能有用：该文将 BNP 混合与生成式潜在变量结合用于离散数据的半参数推断，其建模思路可启发您在因果推断中处理离散型中介或结果变量时的半参数识别与估计策略。
- **关键技术**: `Bayesian nonparametric kernel mixture`, `latent continuous variable generative model`, `quantile regression for discrete outcomes`, `posterior via optimization`, `conditional quantile loss minimization`
- **为什么对您有用**: 本文连接到半参数理论（BNP kernel mixture 作为联合分布的灵活建模）与流行病学应用（急性心肌梗死住院时长数据集）。您武器库中的 nonparametric statistics 与 M-estimation theory 可直接审视其潜在变量分位数损失的定义与优化推断的收敛性质。**中期可做**：若想深入其 BNP 混合的后验收敛率与半参数效率，需先在 moderately_familiar 的 M-estimation theory 上补充贝叶斯非参数收敛率（如 Dirichlet process 后验收敛）的相关知识。

### 5. [10.1093/biomtc/ujaf141](https://doi.org/10.1093/biomtc/ujaf141) — A Bayesian collocation integral method for system identification of ordinary differential equations
- **作者**: Mingwei Xu, Samuel W K Wong, Peijun Sang
- **期刊/来源**: Biometrics
- **机构**: University of Waterloo
- **分类**: vol 81 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 additive ODE 模型设定下，本文目标是从 noisy time-course data 中识别高维稀疏 ODE 结构并对参数估计做 uncertainty quantification。核心方法是 Bayesian hierarchical collocation：将 likelihood、ODE 约束的积分形式与 group-wise sparse penalty 统一在一个框架内，同时完成系统识别与轨迹估计。技术路径依赖 collocation 方法将微分约束转化为代数约束，配合 Bayesian sparse prior 实现结构选择，避免了传统 frequentist 方法在 UQ 上的困难。模拟与基因调控网络实证表明轨迹恢复与成分估计优于近期方法。对您而言，该文的 collocation + integral 策略为 ODE 约束下的 semiparametric estimation 提供了一个 Bayesian 视角，可作为 ODE inverse problems 方向的参考。
- **关键技术**: `Bayesian hierarchical model`, `collocation method`, `ODE integral constraint`, `group-wise sparse penalty`, `additive ODE model`, `uncertainty quantification`
- **为什么对您有用**: 本文连接到 primary interest 中的 inverse problems with random noise 与 semiparametric theory：ODE system identification 本质上是带微分约束的 inverse problem，而 additive 结构引入了 semiparametric 成分。您武器库中 inverse problems with random noise (very_familiar) 可直接切入其 likelihood + integral constraint 的建模方式，但 Bayesian sparse prior 与 collocation 数值细节需在 moderately_familiar 的 M-estimation theory 上补充。Follow-up 判断：**中期可做**——若想将 semiparametric efficiency / HOIF 视角引入此类 ODE identification，需先在 M-estimation theory 下补齐 Bayesian collocation 的数值收敛性质。

### 6. [10.1093/biomtc/ujaf145](https://doi.org/10.1093/biomtc/ujaf145) — Bayesian monotone single-index quantile regression model with bounded response and misaligned functional covariates
- **作者**: Shengxian Ding, Debajyoti Sinha, Greg Hajcak, Roman Kotov, Chao Huang
- **期刊/来源**: Biometrics
- **机构**: Yale University · Florida State University · Santa Clara University · Stony Brook University · University of Georgia
- **分类**: vol 81 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在青少年抑郁队列研究中，目标是估计标量协变量（父母抑郁史等）与错位功能性协变量（神经奖励响应）对未来有界抑郁评分的条件分位数效应。本文提出 Bayesian monotone single-index quantile regression，将标量与功能性协变量投影为 single-index，并通过单调链接函数灵活捕捉未知非线性关系与交互，同时保证估计分位数落在响应变量的自然边界内。方法在分位数回归框架下联合处理功能性协变量的 registration（对齐）问题，避免了传统线性回归与无约束 single-index 模型的局限。模拟显示在含标量与预对齐功能性协变量时，该方法优于无约束 single-index 方法。实证结果提供了一个具有临床可解释性的神经奖励处理综合指标。对您可能有用：本文的单调链接+single-index 结构属于 semiparametric 模型范畴，其 Bayesian 实现可对比您熟悉的 semiparametric efficiency 视角下的 frequentist 估计效率。
- **关键技术**: `single-index model`, `monotone link function`, `Bayesian quantile regression`, `functional covariate registration`, `bounded response constraint`
- **为什么对您有用**: 本文连接到 semiparametric theory 子方向（single-index + monotone link 属于半参数模型），但核心是 Bayesian 分位数回归在流行病学队列数据的应用，方法学 novelty 偏应用驱动。用您 very_familiar 的 minimax bounds for estimation problems 可以审视该 single-index 估计量在单调约束下的收敛率是否达到最优；但本文未涉及 influence function 或效率界推导，且 Bayesian 计算非您武器库核心。**中期可做**：若想从效率理论角度切入，需先在 moderately_familiar 的 semiparametric theory 上长肌肉，推导该 monotone single-index 分位数模型的 efficient influence function 与 semiparametric efficiency bound，再与文中 Bayesian 后验收敛率做理论对比。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomtc/ujaf150](https://doi.org/10.1093/biomtc/ujaf150) — Federated double machine learning for high-dimensional semiparametric models
- **作者**: Kai Kang, Zhihao Wu, Xinjie Qian, Xinyuan Song, Hongtu Zhu
- **期刊/来源**: Biometrics
- **机构**: Sun Yat-sen University · Chinese University of Hong Kong · University of North Carolina at Chapel Hill
- **分类**: vol 81 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在多中心联邦学习设定下，目标是高维半参数模型中低维目标参数的估计，关键假设为各中心数据独立且满足 Neyman 正交性。核心机制为：各中心本地用 DML 估计中心特异参数，通过 surrogate efficient score 方法在 Neyman-orthogonal 框架下构造正交得分，再利用 density ratio tilting 将本地个体数据与来自其他中心的汇总统计量融合，形成联邦估计量。该方法有效缓解了高维 nuisance 参数估计中的正则化偏差与过拟合问题。理论上在极小假设下证明了估计量的极限分布，实现 n^{-1/2}-CAN 与半参数有效界收敛。对您可能有用：本文将 DML 的 orthogonal score 与 density ratio tilting 结合以实现跨中心信息聚合，直接连接到您 primary interest 中的 debiased ML 与半参数效率理论。
- **关键技术**: `double machine learning`, `Neyman-orthogonal score`, `surrogate efficient score`, `density ratio tilting`, `federated learning`, `high-dimensional nuisance parameters`
- **为什么对您有用**: 本文直接连接到您 primary interest 中的 debiased ML 与 semiparametric efficiency bounds 子方向，其核心是将 Chernozhukov DML 的 orthogonal score 推广到多中心联邦设定。您武器库中 very_familiar 的 minimax bounds 与 estimation theory in causal inference 可直接审视其声称的极小假设与效率界是否紧。**立即可做**：用您熟悉的 semiparametric theory 与 DML 框架验证其 density ratio tilting 融合步骤的 influence function 构造是否达到局部效率，并可探索将此联邦 DML 框架迁移至 proximal CI 的多中心设定。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biomtc/ujaf133](https://doi.org/10.1093/biomtc/ujaf133) — Double robust conditional independence test for novel biomarkers given established risk factors with survival data
- **作者**: Baoying Yang, Jing Qin, Jing Ning, Yukun Liu
- **期刊/来源**: Biometrics
- **机构**: Southwest Jiaotong University · National Institutes of Health · National Institute of Allergy and Infectious Diseases · The University of Texas MD Anderson Cancer Center · East China Normal University
- **分类**: vol 81 · issue 4
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在生存数据可能受右删失的设定下，本文研究条件独立性检验 $T \perp X | Z$（$Z$ 为已知风险因子，$X$ 为潜在新生物标志物），目标是识别对风险预测有增量贡献的新 biomarker。核心方法是基于偏/参数似然比统计量检验 $X$ 的系数是否为零，但传统直接参照卡方分布的做法在模型误设下 I 类错误失控；作者提出 resampling 方法逼近似然比分布，使检验具有双重稳健性——只要结局模型 $T|(X,Z)$ 或工作模型 $\Pr(X|Z)$ 之一正确指定，即可保证近似正确的 I 类错误率。方法还允许嵌入机器学习估计以提升表现，模拟与 ADNI 数据验证了有限样本性质。对您有用：该文将 DR 思想引入带删失生存数据的条件独立性检验，直接连接您 primary interest 中的 hypothesis testing 与 causal identification（条件独立性是因果图判定 d-separation 的核心）。
- **关键技术**: `conditional independence test`, `double robustness`, `likelihood ratio statistic`, `resampling-based inference`, `right-censored survival data`, `machine learning nuisance estimation`
- **为什么对您有用**: 本文直接触及您 primary interest 中的 hypothesis testing 与 causal identification（条件独立性检验是因果发现与 d-separation 判定的基石），且 DR 逻辑与您熟悉的 semiparametric efficiency / debiased ML 视角一致。您武器库中 very_familiar 的 estimation theory in causal inference 与 moderately_familiar 的 semiparametric theory 完全可以攻这篇 paper 的 DR 证明与 influence function 推导口子。Follow-up 判断：**立即可做**——用您熟悉的 semiparametric DR 框架审视其 resampling 方案的 asymptotic validity，或尝试用 cross-fitting + DML 替换其 ML nuisance 估计以收紧有限样本 I 类错误。

### 2. [10.1093/biomtc/ujaf142](https://doi.org/10.1093/biomtc/ujaf142) · [arXiv](https://arxiv.org/abs/2408.12541) — Clarifying the role of the Mantel–Haenszel risk difference estimator in randomized clinical trials
- **作者**: Xiaoyu Qiu, Yuhan Qian, Jaehwan Yi, Jinqiu Wang, Yu Du, Yanyao Yi et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究随机化临床试验中二元结局的 Mantel–Haenszel (MH) 风险差估计量，目标 estimand 为超总体框架下的平均处理效应 (ATE) 及跨层风险差的加权平均，放松了传统的 common risk difference 同质性假设，仅要求风险差变异的合理约束。核心机制是将 MH 估计量重新定位为协变量调整工具，并在大层 (large-stratum)、稀疏层 (sparse-stratum) 及混合渐近框架下严格推导其一致性与渐近分布；同时提出统一的稳健方差估计量，在无需同质性假设下于所有渐近框架中均具可证一致性，改进了 Greenland–Robins 与 Sato 等人的经典方差估计。理论延伸还为 MH 检验、事后分层估计量及多处理设置提供了新见解。对您有用：本文为 RCT 中协变量调整估计量的渐近理论提供了严格刻画，其 large-/sparse-stratum 双框架分析及 robust variance 构造思路可直接迁移至您在因果推断估计理论中的研究。
- **关键技术**: `Mantel-Haenszel risk difference estimator`, `covariate adjustment in randomized trials`, `large-stratum asymptotics`, `sparse-stratum asymptotics`, `robust variance estimation`, `super-population ATE`
- **为什么对您有用**: 直接连接因果推断的估计理论子方向：在 RCT 协变量调整设定下，对 MH 估计量在 large-/sparse-stratum 渐近框架下的一致性及 robust variance 给出严格证明。您武器库中 very_familiar 的 M-estimation theory 与 estimation theory in causal inference 可直接攻入本文的渐近分析口子，验证其 robust variance 在混合框架下的收敛性质。立即可做：用 very_familiar 的 M-estimation 与高维渐近工具即可展开对本文方差估计量效率性质的进一步探讨。

### 3. [10.1093/biomtc/ujaf170](https://doi.org/10.1093/biomtc/ujaf170) — Maximized sequential probability ratio test regression
- **作者**: Ivair R Silva, Joselito Montalban, Fernando L P de Oliveira
- **期刊/来源**: Biometrics
- **机构**: Universidade Federal de Ouro Preto · Harvard Pilgrim Health Care · Manitoba Health
- **分类**: vol 81 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在药物/疫苗上市后不良反应的序贯监测设定下，将 MaxSPRT 及其条件版本 CMaxSPRT 扩展以纳入可观测混杂协变量的回归结构，目标是在序贯假设检验中控制混杂偏倚。针对二项与 Poisson 数据，作者提出 straightforward 的序贯回归检验方法，使得在历史数据与监测数据比较（CMaxSPRT 设定）中可同时处理未知异质性基线率、季节性及其他混杂。核心机制是在 MaxSPRT 的似然比构造中嵌入回归参数，保持序贯检验的停止边界与 alpha 消耗性质，并利用 R Sequential 包实现数值计算。理论贡献主要为方法层面的扩展而非渐近效率或 minimax 界的新结果。对您可能有用：若关注序贯监测中的假设检验设计，本文提供了一个将回归调整嵌入经典序贯似然比检验的具体实例。
- **关键技术**: `MaxSPRT`, `CMaxSPRT`, `sequential likelihood ratio test`, `Poisson regression adjustment`, `alpha spending function`, `post-market surveillance`
- **为什么对您有用**: 本文连接到 primary interest 中的 hypothesis testing 子方向，具体是序贯监测设定下的似然比检验设计；同时涉及 epidemiology secondary interest 中的疫苗不良反应监测数据与混杂调整。从 technical_arsenal 看，本文的似然比构造与 alpha 消耗机制属于 very_familiar 的 nonparametric statistics / minimax bounds 范畴之外的经典参数序贯检验，但回归调整部分可用 moderately_familiar 的 M-estimation theory 视角审视其参数估计一致性。Follow-up 粗判：**中期可做**——若想在此方向深入，需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以分析序贯回归估计的渐近性质与效率界，当前武器库对纯参数序贯检验的 alpha 消耗设计并非核心专长。

## 流行病学  *(epidemiology, 11 篇)*

### 1. [10.1093/biomtc/ujaf155](https://doi.org/10.1093/biomtc/ujaf155) — Super learner for survival prediction in case-cohort and generalized case-cohort studies
- **作者**: Haolin Li, Haibo Zhou, David Couper, Jianwen Cai
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在流行病学罕见疾病的 case-cohort 及广义 case-cohort 设计下，目标是解决生存预测问题而非传统参数估计，关键假设为 subcohort 的随机抽样与 censoring 机制。本文提出基于 super learner 的预测算法，核心机制是利用 case-cohort 加权将全队列损失函数适配到子样本，通过 cross-validation 在候选库中筛选最优组合。理论方面证明了该 super learner 的 asymptotic model selection consistency 与 uniform consistency，模拟显示同等样本量下其预测精度优于简单随机抽样设计。实证分析基于 ARIC 研究的广义 case-cohort 数据。对您而言，本文提供了流行病学复杂抽样设计下 ensemble 预测的完整案例，但理论部分未涉及 efficiency bound 或 influence function。
- **关键技术**: `case-cohort sampling weight`, `super learner / stacked ensemble`, `asymptotic model selection consistency`, `uniform consistency`, `survival prediction`, `generalized case-cohort design`
- **为什么对您有用**: 本文属于流行病学应用方向，提供了 case-cohort 设计下生存预测的完整数据流程与加权 super learner 框架，可作为了解该抽样设计及其加权机制的入门读物。武器库中 estimation theory in causal inference 与 semiparametric theory 足以支撑阅读，但本文未触及 semiparametric efficiency bound 或 influence function，理论深度有限。是否值得花时间读全文：若需快速了解 case-cohort 加权预测流程可读，若寻求效率理论或高阶推断的新视角则不必深入。

### 2. [10.1093/biomtc/ujaf157](https://doi.org/10.1093/biomtc/ujaf157) — A semiparametric method for addressing underdiagnosis using electronic health record data
- **作者**: Weidong Ma, Jordana B Cohen, Jinbo Chen
- **期刊/来源**: Biometrics
- **机构**: University of Pennsylvania
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在电子健康记录（EHR）数据中，许多疾病存在漏诊（underdiagnosis）现象，导致数据呈现正-无标签（positive-unlabeled, PU）结构：确诊患者为阳性，其余未标注患者中混杂了漏诊者与真正无病者，缺乏明确无病的金标准数据。本文提出通过主动验证（ascertainment）获取少量未标注患者的真实疾病状态，从而补充 PU 数据，构建估计个体患病概率的模型。核心方法是半参数估计框架，结合验证子集的信息与全样本 EHR 特征，推导出估计量的影响函数并证明其 n^{-1/2}-CAN 性质及半参数有效性。模拟研究验证了有限样本表现，并在 Penn Medicine EHR 数据上应用于识别潜在漏诊的非酒精性脂肪性肝炎（NASH）患者。对您可能有用：本文将 PU 学习与半参数有效估计结合，为流行病学 EHR 数据的因果/患病率估计提供了新框架。
- **关键技术**: `positive-unlabeled learning`, `semiparametric efficiency bound`, `influence function`, `n^{-1/2}-CAN estimator`, `active ascertainment / verification sampling`, `EHR underdiagnosis`
- **为什么对您有用**: 本文直接连接到流行病学因果推断与半参数有效估计两个子方向：(1) PU 数据结构在流行病学 EHR 研究中极常见，本文的半参数有效估计框架为处理此类选择偏差/测量误差提供了严谨的 identification 与 estimation 工具；(2) 您武器库中 semiparametric theory 与 influence function 的 very_familiar/moderately_familiar 知识可直接攻入本文的理论部分，验证其有效界是否紧、或拓展至 longitudinal EHR 场景。Follow-up 判断：**立即可做**——用您熟悉的半参数效率理论审视其影响函数推导，或将验证采样设计与 proximal CI 的 negative control 思路做对比。

### 3. [10.1093/biomtc/ujaf161](https://doi.org/10.1093/biomtc/ujaf161) — Censoring-robust estimation in fixed sample time-to-event clinical trials with adaptive randomization
- **作者**: Navneet R Hakhu, Daniel L Gillen
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Cancer Research And Biostatistics · University of California, Irvine · Irvine University
- **分类**: vol 81 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对固定样本时间-事件临床试验中自适应随机化带来的删失模式改变问题，以边际风险比为科学估量，证明Cox比例风险估计量会产生偏倚。作为补救，提出一个删失鲁棒估计量，通过治疗特异性删失分布对部分似然得分进行逆概率加权，以消除自适应随机化引入的删失偏倚。推导了该估计量的渐近正态性，并通过蒙特卡洛模拟评估了其有限样本操作特性。最后，将方法应用于社区艾滋病临床研究002试验数据。本文方法虽针对时间-事件终点，但其加权部分似然框架与您熟悉的因果推断估计理论相通，对流行病学中随机试验的效应估计有直接参考价值。
- **关键技术**: `Cox proportional hazards model`, `censoring-robust reweighting`, `partial likelihood score`, `adaptive randomization`, `marginal hazard ratio`
- **为什么对您有用**: 本文聚焦自适应随机化下时间-事件试验中治疗效应的无偏估计，属于流行病学应用中的因果推断问题。您very_familiar中的'estimation theory in causal inference'可直接用于分析该加权估计量的识别假设和渐近性质，且加权思路与双稳健估计中的逆概率加权有共鸣。该工作立即可做，无需额外工具即可理解其识别策略和渐近推导。

### 4. [10.1093/biomtc/ujaf144](https://doi.org/10.1093/biomtc/ujaf144) — Bayesian scalar-on-image regression with spatial interactions for modeling Alzheimer’s disease
- **作者**: Nilanjana Chakraborty, Qi Long, Suprateek Kundu
- **期刊/来源**: Biometrics
- **机构**: Indian Institute of Management Udaipur · University of Pennsylvania · The University of Texas MD Anderson Cancer Center
- **分类**: vol 81 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究阿尔茨海默病（AD）中认知障碍的预测建模问题，基于神经影像生物标志物和人口学、临床、遗传等补充风险因素，建立标量-图像回归模型。作者提出贝叶斯方法，通过功能回归系数的层次表示来捕捉脑影像与风险因子之间的空间变化交互作用。该方法采用多分辨率小波分解处理图像的高维性，并引入 spike-and-slab 混合先验（slab 分量为潜类别分布）实现同时稀疏性和聚类，以应对维度灾难。后验计算通过高效的马尔可夫链蒙特卡洛算法完成。模拟和应用于 Alzheimer's Disease Neuroimaging Initiative 纵向数据表明，所提模型在多个访视点的认知障碍预测上显著优于对比方法，并能识别出与认知能力直接相关或通过风险因子交互作用的关键脑区。对您而言，该文属于流行病学领域的真实数据应用，展示了如何在高维成像数据中整合交互效应，其分析框架（稀疏正则化、空间结构建模）可作为处理大规模观测数据的参考，尤其适用于您感兴趣的因果推断中 mediation 或 longitudinal 设定下的高维协变量处理。
- **关键技术**: `scalar-on-image regression`, `multi-resolution wavelet decomposition`, `spike-and-slab prior`, `latent class distribution`, `Markov chain Monte Carlo`
- **为什么对您有用**: 作为流行病学领域的入门级读物，本文清晰展示了高维影像数据与风险因子交互建模的完整流程（小波分解、spike-and-slab 先验、MCMC），适合了解该方向的数据结构和方法流程。您的武器库中 'high-dimensional asymptotics' 和 'estimation theory in causal inference' 可支撑评价其正则化策略，但贝叶斯计算（MCMC）和潜类别模型不属于核心装备。总体上值得读全文以获取处理复杂交互效应的思路，但短期内难以直接嫁接您的因果推断工具。

### 5. [10.1093/biomtc/ujaf164](https://doi.org/10.1093/biomtc/ujaf164) — Prediction of transition probabilities in multi-state models with nested case-control data
- **作者**: Yen Chang, Anastasia Ivanova, Demetrius Albanes, Jason P Fine, Yei Eun Shin
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill · National Cancer Institute · University of Pittsburgh · Seoul National University · New Generation University College · National University College
- **分类**: vol 81 · issue 4
- 相关性 5/10 · novelty: `application`
- **摘要**: 该论文针对多状态模型中转移概率的预测问题，处理嵌套病例对照（NCC）抽样数据。NCC设计通过条件似然分析通常只关注单一事件，无法复用数据研究其他终点。作者扩展了基于逆概率加权（IPW）的伪似然方法，使其适用于一般多状态模型下转移概率的预测。并提出两种新方法提升效率：一是利用队列层面信息校准设计权重，二是联合建模源自同一状态的多个转移。同时推导了显式方差估计量。模拟显示两种方法均显著改善效率，联合使用效果更佳。PLCO队列实际数据示例展示了方法的应用价值。本文对关注流行病学队列研究中复杂事件过程的统计学方法有直接参考意义。
- **关键技术**: `nested case-control sampling`, `inverse probability weighting`, `pseudo-likelihood`, `calibration`, `multi-state models`, `variance estimation`
- **为什么对您有用**: (1) 直接连接流行病学应用（研究者secondary interest），NCC采样是大型队列研究常用设计，处理从发病到死亡的多状态路径；(2) 武器库中的M-estimation理论（moderately_familiar）和IPW估计框架可用于理解和改进此类伪似然方法，但NCC采样和加权校准的具体技术属于流行病学领域特殊工具，需进一步熟悉；(3) 中期可做：本文提供了一个具体入口，研究者可在职业人口学等方向结合自己的因果推断工具（如IPW与semiparametric效率理论）拓展至监测数据或纵向事件分析。

### 6. [10.1093/biomtc/ujaf159](https://doi.org/10.1093/biomtc/ujaf159) — Stable survival extrapolation using mortality projections
- **作者**: Anastasios Apsemidis, Nikolaos Demiris
- **期刊/来源**: Biometrics
- **机构**: Athens University of Economics and Business
- **分类**: vol 81 · issue 4
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文聚焦于生存外推（survival extrapolation）问题，目标是在健康经济评价中从有限随访数据外推完整生存曲线以估计平均生存时间。方法层面，作者采用贝叶斯死亡率模型，利用登记和人口统计数据的长期信息构建基线人群，以此锚定生存模型。随后提出基于灵活参数化多风险（poly-hazard）模型的 extrapolation 方法，可自然处理非比例风险、交叉生存曲线等复杂形状，同时保持数据生成机制的可解释性。在乳腺癌、晚期黑色素瘤和心律失常三个真实数据集上进行估计，包括三阴性乳腺癌的生存劣势、黑色素瘤免疫治疗联合 mRNA 疗法的疗效、以及心脏复律除颤器的适宜性（在竞争风险框架下）。结果表明，该方法在需要生存外推的场景下提供了一种灵活、可解释且稳健的方案。此文属于流行病学领域的应用工作，数据集和分析流程对研究者有参考价值。
- **关键技术**: `Bayesian mortality model`, `poly-hazard model`, `survival extrapolation`, `competing risks`, `flexible parametric survival models`
- **为什么对您有用**: (1) 作为流行病学入门读物，本文清晰展示了生存外推在健康经济评价中的实际需求、数据结构和建模流程（贝叶斯死亡率模型 + poly-hazard 模型），对不熟悉该领域的统计学家友好。 (2) 研究者武器库中 very_familiar 工具（非参数统计、高维渐近）可部分用于理解 poly-hazard 模型的灵活性，但核心依赖于贝叶斯推断（MCMC、先验设定），不属于当前 weapon set，因此进入该方向需要补充贝叶斯计算方法（moderately_familiar 中未列此项）。 (3) 值得花时间读全文，因为三组真实数据（癌症、心律失常）的生存外推案例可为研究者将来的应用导向工作（如流行病学中的因果推断）提供参考，但方法论上的直接迁移有限。

### 7. [10.1093/biomtc/ujaf138](https://doi.org/10.1093/biomtc/ujaf138) — A regularized continuous-time hidden Markov model for identifying latent state transition patterns of poly-tobacco use
- **作者**: Xinyu Yan, Ji-Hyun Lee, Xiang-Yang Lou
- **期刊/来源**: Biometrics
- **机构**: University of Florida · University of Florida Health
- **分类**: vol 81 · issue 4
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对流行病学队列研究中多烟草使用状态的潜在转移模式识别问题，提出了一种带弹性网正则化的连续时间隐马尔可夫模型（CT-HMM）。在 PATH 纵向队列数据设定下，目标 estimand 为高维协变量下的状态转移概率矩阵与隐状态数；关键假设包括连续时间马尔可夫性及弹性网对转移参数的稀疏性约束。核心机制在于：对转移强度参数引入 elastic-net 正则化以实现高维协变量筛选与估计精度的双重提升，并通过纳入关键协变量辅助 BIC 等准则确定隐状态数；同时整合了调查权重、分层与聚类信息以修正复杂抽样设计偏差。模拟验证了该方法在状态数确定、协变量筛选及参数估计上的有效性；PATH 实际数据分析揭示了青年群体烟草使用状态转移的若干人口学、行为与心理社会风险因子。对您而言，本文提供了一个将高维变量筛选与连续时间纵向隐状态模型结合的流行病学应用案例。
- **关键技术**: `continuous-time hidden Markov model`, `elastic-net regularization`, `survey-weighted likelihood`, `latent state number determination`, `transition intensity estimation`
- **为什么对您有用**: 本文属于流行病学纵向队列的因果/机制性应用，连接到您 secondary interest 中 epidemiology 的 longitudinal data 与 causal inference 子方向。您武器库中 very_familiar 的 high-dimensional asymptotics 与 estimation theory 可直接审视其 elastic-net 正则化下转移参数估计的收敛性质（当前论文仅以模拟验证，缺乏理论收敛率或 minimax 分析）。**立即可做**：用您熟悉的高维 M-estimation 理论为该 elastic-net CT-HMM 补上 n^{-1/2}-CAN 或 oracle 性质的理论缺口。

### 8. [10.1093/biomtc/ujaf163](https://doi.org/10.1093/biomtc/ujaf163) · [arXiv](https://arxiv.org/abs/2407.08278) — Structuring, sequencing, staging, selecting: the 4S method for the longitudinal analysis of multidimensional questionnaires in chronic diseases
- **作者**: Tiphaine Saulnier, Wassilios G Meissner, Margherita Fabbri, Alexandra Foubert-Samier, Cécile Proust-Lima
- **期刊/来源**: Biometrics
- **机构**: Université de Bordeaux · Inserm · Bordeaux Population Health · Institut des Maladies Neurodégénératives · New Zealand Brain Research Institute · Centre Hospitalier Universitaire de Toulouse
- **分类**: vol 81 · issue 4
- 相关性 3/10 · novelty: `application`
- **摘要**: 在慢性病纵向队列研究中，目标是利用重复采集的多维有序问卷数据识别疾病进展过程中的关键表现，核心假设是问卷维度满足单维性、条件独立与单调递增的校准假设。方法提出四步 4S 策略：(1) 通过校准假设识别问卷的维度结构；(2) 对每个维度使用联合潜在过程模型（内含连续时间 IRT 模型）刻画纵向轨迹并处理截断事件；(3) 通过投影方法将各维度轨迹与疾病分期对齐；(4) 利用 Fisher 信息量在不同疾病分期筛选最具信息量的条目。实证分析应用于多系统萎缩症（MSA）的日常活动与运动障碍数据，展示了从原始条目到疾病分期映射的完整分析管线。对您可能有用：本文展示了流行病学队列中纵向多维有序数据的结构化建模策略，其中连续时间 IRT 与联合潜在过程模型为处理纵向因果推断中的测量误差与截断提供了参考框架。
- **关键技术**: `continuous-time item response theory model`, `joint latent process model`, `Fisher information criterion`, `conditional independence calibration`, `disease stage projection`
- **为什么对您有用**: 本文属于流行病学应用与纵向建模，连接到 epidemiology 的纵向队列因果推断子方向；其联合潜在过程模型与连续时间 IRT 为处理纵向因果推断中 latent variable measurement error 提供了可借鉴的模型框架，但核心是 IRT 与疾病分期投影，而非因果识别或效率理论。作为 gateway reading，本文对多维有序纵向数据的建模思路阐述清晰，数据结构（重复有序条目+截断）暴露了真实统计挑战，武器库中的 M-estimation theory 与 semiparametric theory 足以支撑进入此方向，值得花时间读全文以了解流行病学纵向数据的典型痛点。

### 9. [10.1093/biomtc/ujaf158](https://doi.org/10.1093/biomtc/ujaf158) — Joint Bayesian additive regression trees for multiple nonlinear dependency networks
- **作者**: Licai Huang, Christine B Peterson, Min Jin Ha
- **期刊/来源**: Biometrics
- **机构**: The University of Texas MD Anderson Cancer Center · AbbVie (United States) · Department of Health · Yonsei University Health System
- **分类**: vol 81 · issue 4
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究多子组（如癌症亚型）下非线性依赖网络的推断问题，目标是在多个子组之间共享常见依赖关系的同时，允许各子组保留特异性连接。方法上，提出了一种层次贝叶斯模型，结合贝叶斯加性回归树（BART）和马尔可夫随机场（MRF）先验：BART用于灵活捕获节点间的非线性效应和交互效应，适合处理基因组数据中的复杂关系；MRF先验则作用于BART分裂规则中特征的使用概率，从而在子组间借用信息以实现共享边选择。后验推断采用MCMC算法，通过模拟数据和结直肠癌（CRC）亚型的蛋白质-蛋白质相互作用网络真实数据验证了模型在识别共享与特异性边上的优势。对您可能有用：本文是流行病学/生物信息学中应用非参数模型进行网络推断的典型案例，可启发您在高维因果推断或应用数据分析时采用类似的层次贝叶斯思路。
- **关键技术**: `Bayesian Additive Regression Trees (BART)`, `Markov random field prior`, `hierarchical Bayesian model`, `dependency network inference`, `MCMC sampling`
- **为什么对您有用**: 本文属流行病学应用论文，使用BART建模非线性依赖网络，对非流行病学背景的统计学者友好，适合作为入门读物。武器库中'非参数统计'知识足以理解BART的建模框架，无需额外背景。本文的数据分析和模型设计流程清晰，值得花时间全文阅读，以借鉴其跨子组信息共享的网络推断策略，或许可迁移到您关注的因果推断或高维问题中类似的层次结构。

### 10. [10.1093/biomtc/ujaf154](https://doi.org/10.1093/biomtc/ujaf154) — Analysis of cross-platform health communication with a network approach
- **作者**: Xinyan Fan, Mengque Liu, Shuangge Ma
- **期刊/来源**: Biometrics
- **机构**: Renmin University of China · Xi'an Jiaotong University · Yale University
- **分类**: vol 81 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究在线健康社区（Breastcancer.org）与Twitter之间的跨平台健康通信问题，目标是分析Twitter上的乳腺癌话题如何影响社区内的内容结构和交流量。作者提出一种新的跨平台通信模型，联合建模词共现网络（反映内容结构）与词频向量（反映交流量），并允许参数随时间平滑变化。模型通过融合网络拓扑与计数信息，比单一视角更全面地刻画跨平台影响；作者证明了估计量的理论性质（如相合性）并进行了数值模拟验证。使用2010-2020年超过139万条推文和51.7万条帖子的真实数据，分析发现Twitter内容对社区话题具有显著驱动作用，并在2012–2013和2015–2018出现明显峰值。对您而言，这是一篇流行病学领域的应用型论文，展示了大规模文本网络数据与模型驱动的分析流程，可作为了解健康传播实证研究的入门材料。
- **关键技术**: `word co-occurrence network`, `cross-platform communication model`, `time-varying graphical model`, `text mining`, `joint modeling of network and count data`
- **为什么对您有用**: 本文属于流行病学领域（健康通信）的应用研究，与您的次要兴趣流行病学（数据集、应用）直接对应。方法上虽未涉及因果推断，但网络分析工具（词共现网络、时变模型）属于您非常熟悉的非参数统计范畴，可快速评估其分析模式。若未来希望从“影响”描述转向因果识别（如Twitter对社区参与度的因果效应），则需补充面板数据或工具变量等识别策略，这属于中期可做方向，需在因果推断的识别理论项上提升。

### 11. [10.1093/biomtc/ujaf124](https://doi.org/10.1093/biomtc/ujaf124) · [arXiv](https://arxiv.org/abs/2505.03898) — Randomized optimal selection design for dose optimization
- **作者**: Shuqi Wang, Ying Yuan, Suyu Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 针对FDA Project Optimus推动剂量选择从最大耐受剂量转向最佳生物剂量(OBD)的背景，本文提出了一种随机化最优选择(ROSE)设计。该设计在保证正确选择概率达到预设精度的前提下最小化样本量，方法简单——只需比较两个剂量组的反应率差异是否超过预设决策边界。进一步发展的两阶段ROSE设计允许在中期数据充足时提前选择OBD，进一步减少样本量。模拟显示，每剂量组15-40名患者可达到60%-70%的正确选择概率。本文作为流行病学领域中剂量优化的应用，提供了一种简单有效的随机试验设计框架，与您的次要兴趣(流行病学应用)相关。
- **关键技术**: `Randomized optimal selection`, `selection design framework`, `two-stage design`, `sample size optimization`, `correct selection probability`
- **为什么对您有用**: (1) 本文属于临床试验设计，直接连接您的次要兴趣——流行病学中的药物有效性评估与剂量优化应用。(2) 您可以使用非常熟悉的software development技能实现该ROSE设计并进行模拟扩展，或利用nonparametric statistics知识增强决策边界的灵活性。(3) follow-up粗判：立即可做——该设计方法简单，您可立即理解并复现结果，无需额外工具学习。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biomtc/ujaf160](https://doi.org/10.1093/biomtc/ujaf160) · [arXiv](https://arxiv.org/abs/2407.06173) — Large row-constrained supersaturated designs for high-throughput screening
- **作者**: Byran J Smucker, Stephen E Wright, Isaac Williams, Richard C Page, Andor J Kiss, Surendra Bikram Silwal et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文针对高通量筛选（high-throughput screening）中化合物池大小受限的实际问题，提出一类新的行约束超饱和设计（row-constrained supersaturated designs），并整合为CRowS（Constrained Row Screening）流程。作者发展了一个高效的计算程序来构造CRowS设计，给出了主效应信息矩阵的平均非对角元平方的下界，并研究了约束对设计质量的影响。通过模拟比较，CRowS在统计性能上优于传统的单化合物单孔方法和已有的池化方法。最后在Verona整合子编码的金属-β-内酰胺酶-2检测数据上展示了该方法的实际效用。本文主要贡献在于将实验设计中的超饱和设计思想推广到具有行约束的实际场景，为大规模生物筛选提供了新的统计工具。对您而言，该方法中涉及的下界分析和计算构造可能对您在高维统计或统计计算中的设计问题有所启发，但核心方向与您的因果推断、高阶U统计等兴趣点无直接重叠。
- **关键技术**: `supersaturated designs`, `row-constrained designs`, `CRowS procedure`, `lower bounds on information matrix`, `simulation comparison`, `high-throughput screening`
- **为什么对您有用**: 本文与您的primary interests没有直接连接；但其对设计矩阵的下界分析属于高维统计中矩阵性质的一点联系，而您的武器库中"high-dimensional asymptotics"可能勉强相关。然而，论文主题（实验设计）是您较少涉足的领域，缺乏实验设计相关的理论工具，目前暂不可做直接跟进。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

