# Econometrica — Vol 91  Issue 1  ·  2026-07-18

- 共 9 篇 · Econometrica
- 目录核对 ⚠️ 疑似漏 2 篇（对照 OpenAlex 18 篇）：10.3982/ecta911sum、10.3982/ecta911ref

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Econometrica Vol 91 Issue 1 的九篇论文可归纳为三条主线：**结构模型与反事实推断**（涵盖非参数识别、敏感性分析与均衡检验）、**网络与大规模系统的方法论**（图博弈、线性系统检验）、以及**应用微观经济学的因果识别**（资本错配、电商税法、劳动份额）。此外，有一篇纯秘书报告不涉及方法贡献。

**结构模型与反事实推断**是本期最密集的线索。Nonparametric Estimates of Demand 在离散选择中结合部分识别与形状约束（单调性、凹性），用IV界定需求弹性与福利参数，并直接与参数混合Logit对比，揭示参数模型低估价格弹性但高估或低估消费者剩余的差异。Counterfactual Sensitivity and Robustness 则聚焦反事实预测对潜变量分布假设的敏感性，将无穷维优化转化为有限维凸规划，并给出plug-in估计与两种推断方法，覆盖可转移效用匹配和动态离散选择两类模型。Inference for Large‐Scale Linear Systems 为结构模型检验提供计算可操作的工具，将非负解假设转化为线性规划问题，适用于随机系数、处理效应等模型。这三篇共同推进了结构估计中识别、检验与稳健性的方法论边界。

**网络与大规模系统**方面，Graphon Games 提出图博弈框架，将大规模网络博弈的均衡与干预设计简化为低维优化问题，其图近似思想可直接迁移至因果推断中的网络干扰。Invidious Comparisons 则在复合决策框架下，用经验贝叶斯与NPMLE处理排序与选择问题，与多重检验文献紧密关联，为经济学中的排名应用提供决策理论视角。

**应用微观因果识别**中，Misallocation and Capital Market Integration 利用印度资本自由化的交错实施，通过双重差分分离政策对资本错配的因果效应，并提出一种利用自然实验界定错配上界的简约方法。Nexus Tax Laws 结合静态需求与动态投资模型，量化nexus税法对亚马逊配送网络密集化的扭曲。The Race Between Preferences and Technology 则通过非位似偏好与要素替代弹性，统一解释劳动份额的长期变化。

对于因果推断方向的研究者，优先看 Counterfactual Sensitivity and Robustness（敏感性分析框架）与 Nonparametric Estimates of Demand（部分识别与IV下的非参数界）；对于半参数/非参效率方向，Inference for Large‐Scale Linear Systems（线性系统检验）与 Graphon Games（图近似下的干预设计）值得关注；高维方向可留意 Invidious Comparisons（NPMLE在高维排序中的应用）。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.3982/ecta17232](https://doi.org/10.3982/ecta17232) · [arXiv](https://arxiv.org/abs/1904.00989) — Counterfactual Sensitivity and Robustness
- **作者**: Timothy Christensen, Benjamin Connault
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 1 · pp 263-298
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一个框架，用于分析结构模型中反事实预测对潜变量分布参数假设的敏感性。具体而言，在保持模型其他“结构”特征不变的前提下，让潜变量分布在一个给定参数规格的非参数邻域内变化，推导反事实量的边界。该方法将关于潜变量分布的无穷维优化问题（受模型约束）转化为有限维凸规划，并针对内生参数（如值函数）由均衡条件定义的模型开发了MPEC版本以简化计算。作者提出了边界的plug-in估计量以及两种推断方法，并证明当邻域尺寸趋于无穷时，该边界收敛到反事实量的sharp非参数边界。通过可转移效用匹配模型和动态离散选择模型两个实证应用展示了方法的广泛适用性。对您而言，该工作直接连接您对因果推断中敏感性分析的兴趣，其将无穷维优化转化为有限维凸规划的技术思路，可能为proximal causal inference中的敏感性分析提供新的计算工具。
- **关键技术**: `convex programming`, `MPEC`, `plug-in estimation`, `nonparametric neighborhood`, `sharp bounds`
- **为什么对您有用**: 本文直接针对您primary interest中的敏感性分析（sensitivity analysis）子方向，提出了一个将无穷维优化转化为有限维凸规划的一般性框架，这在结构模型的反事实推断中具有方法论创新。从您的技术武器库看，您对非参数统计和因果推断中的估计理论非常熟悉，可以立即尝试将该框架中的凸规划转化技巧应用于proximal causal inference的敏感性分析问题（例如，在negative control假设下，将关于潜变量分布的优化转化为可计算的凸问题）。这是**立即可做**的：您已有的非参数统计和因果推断估计理论足以支撑对该方法核心机制的理解和初步迁移。

## 经济理论 / 应用  *(econ_theory, 8 篇)*

### 1. [10.3982/ecta17215](https://doi.org/10.3982/ecta17215) — Nonparametric Estimates of Demand in the California Health Insurance Exchange
- **作者**: Pietro Tebaldi, Alexander Torgovitsky, Hanbin Yang
- **期刊/来源**: Econometrica
- **机构**: Columbia University · University of Chicago
- **分类**: vol 91 · issue 1 · pp 107-146
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对加州健康保险交易所的需求估计，提出了一种新的非参数离散选择方法。模型允许内生价格和工具变量，同时避免对效用中未观测成分施加参数函数形式假设。核心方法基于部分识别（partial identification）框架，利用IV和形状约束（如单调性、凹性）来界定需求弹性、消费者剩余和补贴支出等政策参数。估计结果显示，每月保费补贴减少10美元会导致受补贴成人参保比例下降1.8%至6.7%，年度消费者剩余减少6200万至7400万美元，补贴支出节省2.07亿至6.02亿美元。与混合Logit模型对比发现，参数模型的价格弹性估计往往落在非参数界的低端，而消费者剩余影响则可能高于或低于非参数界，取决于随机系数设定。本文为应用因果推断和实证产业组织研究提供了非参数识别与估计的范例，对您从事的因果推断（IV、部分识别）和半参数/非参数理论有直接参考价值。
- **关键技术**: `partial identification`, `instrumental variables`, `shape restrictions`, `nonparametric discrete choice`, `bound estimation`, `mixed logit comparison`
- **为什么对您有用**: 本文连接您的经济理论（应用因果工作）兴趣子方向，具体是IV在离散选择需求估计中的非参数识别。您的武器库中'identification theory in causal inference'（moderately_familiar）可直接用于理解其部分识别策略，而'nonparametric statistics'（very_familiar）可评估其形状约束的合理性。中期可做：若想将类似非参数界方法迁移到您的proximal CI或mediation问题，需先在'semiparametric theory'（moderately_familiar）上加强，以处理更复杂的识别函数。

### 2. [10.3982/ecta19304](https://doi.org/10.3982/ecta19304) · [arXiv](https://arxiv.org/abs/2012.12550) — Invidious Comparisons: Ranking and Selection as Compound Decisions
- **作者**: Jiaying Gu, Roger Koenker
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 1 · pp 1-41
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在Robbins (1956)的复合决策框架下，系统研究了基于带噪声标量测量值的排序与选择问题。目标是从n个对象中选出“最优”的一组，每个对象的测量精度可能异质。作者将问题形式化为一个经验贝叶斯问题，并利用Kiefer-Wolfowitz非参数最大似然估计（NPMLE）来估计先验混合分布，从而构造最优排序与选择规则。该方法与多重检验文献有密切联系，提供了一种从决策理论角度统一排序与选择问题的新视角。通过模拟和一项关于美国肾透析中心排名的实际应用，展示了所提规则的良好性能。对您而言，本文展示了经验贝叶斯和NPMLE在经济学应用中的强大潜力，其方法论（复合决策、排序规则）与您对因果推断和经济学应用的兴趣直接相关，可作为入门读物了解该领域。
- **关键技术**: `compound decision framework`, `empirical Bayes`, `nonparametric maximum likelihood estimator (NPMLE)`, `ranking and selection`, `multiple testing`
- **为什么对您有用**: 本文属于经济理论（应用）方向，是您secondary interest中的gateway reading。它清晰阐述了经验贝叶斯和复合决策框架在排序问题中的应用，方法论（NPMLE、排序规则）与您的因果推断兴趣有潜在联系（例如，处理效应排序）。作为入门读物，它不假设读者熟悉该领域，适合快速了解。武器库中'非参数统计'和'估计理论'足以支撑理解核心方法，但若要深入其理论性质（如NPMLE的收敛速度），可能需要补充'高维统计'知识。值得花时间读全文。

### 3. [10.3982/ecta18979](https://doi.org/10.3982/ecta18979) · [arXiv](https://arxiv.org/abs/2009.08568) — Inference for Large‐Scale Linear Systems With Known Coefficients
- **作者**: Zheng Fang, Andres Santos, Azeem M. Shaikh, Alexander Torgovitsky
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 1 · pp 299-327
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究大规模线性系统是否存在非负解这一假设检验问题，其中系数矩阵已知且可能欠定。该问题自然出现在随机系数模型、处理效应模型、离散选择模型以及一类线性规划问题中。作者首先给出了原假设的一个新颖几何刻画，将其转化为关于识别参数满足无穷多个不等式约束的条件。基于这一刻画，他们设计了一个仅需求解线性规划即可实现的检验方法，因此在高维应用中保持计算可行性。理论结果表明，所提检验的渐近尺寸在允许方程个数随样本量增长的一大类分布上均匀地不超过名义水平。该工作为经济学中结构模型的检验提供了计算上可操作的工具，尤其适用于高维设定下的模型验证。
- **关键技术**: `linear programming test`, `geometric characterization of null hypothesis`, `uniform asymptotic size control`, `inequality restrictions`, `high-dimensional inference`
- **为什么对您有用**: 本文直接连接您的 secondary interest 中的经济理论方向，特别是处理效应和离散选择模型的检验问题。您的武器库中 'high-dimensional asymptotics' 和 'estimation theory in causal inference' 可直接用于理解其均匀渐近尺寸控制的理论框架，而 'software development' 技能可用于实现其线性规划检验。中期可做：若想将此类检验推广到更复杂的因果模型（如工具变量或中介分析），需先在 'identification theory in causal inference' 上加强，以处理识别条件与检验统计量的耦合。

### 4. [10.3982/ecta17564](https://doi.org/10.3982/ecta17564) · [arXiv](https://arxiv.org/abs/1802.00080) — Graphon Games: A Statistical Framework for Network Games and Interventions
- **作者**: Francesca Parise, Asuman Ozdaglar
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 1 · pp 191-225
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出图博弈（graphon game）框架，用于分析从随机网络形成过程（graphon）中采样的大规模网络博弈的均衡与干预设计。作者引入一类新的无限总体博弈，其中连续异质主体根据图交互，并证明图博弈的均衡可近似采样网络博弈的均衡。基于此，提出一种渐近最优干预设计方法，通过求解一个维度远低于全网络结构的优化问题来实现。在合成数据上验证了该方法的计算效率，且仅需聚合关系数据。对您而言，本文连接了经济理论中的网络博弈与统计网络模型，其图近似思想可迁移至因果推断中的网络干扰问题。
- **关键技术**: `graphon`, `network games`, `Nash equilibrium approximation`, `asymptotically optimal intervention`, `aggregated relational data`
- **为什么对您有用**: 本文属于经济理论方向，是您 secondary interest 中的 gateway reading。它清晰阐述了网络博弈的统计模型（graphon）与干预设计问题，适合作为入门读物。您的武器库中 nonparametric statistics 和 estimation theory in causal inference 足以支撑理解其核心近似论证，但网络博弈的均衡分析工具（如变分不等式）不在您当前 arsenal 中，属于暂不可做方向。不过，若您对网络因果推断感兴趣，本文的图近似思路值得花时间读全文。

### 5. [10.3982/ecta15265](https://doi.org/10.3982/ecta15265) — Nexus Tax Laws and Economies of Density in E‐Commerce: A Study of Amazon's Fulfillment Center Network
- **作者**: Jean-François Houde, Peter Newberry, Katja Seim
- **期刊/来源**: Econometrica
- **机构**: University of Wisconsin–Madison · University of Georgia · Yale University
- **分类**: vol 91 · issue 1 · pp 147-190
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文量化了美国 nexus 税法（即电商企业仅在有实体设施的州才需代收销售税）对亚马逊配送网络投资决策的扭曲效应，时间跨度为 1999-2018 年。作者聚焦网络的两个特征：设施密集化（densification）和纵向整合至包裹分拣环节。密集化降低了每单运输成本，但提高了高租金地区的运营成本并降低了设施层面的规模经济；而 nexus 税法在网络扩张时产生额外的销售税负债。研究结合家庭跨线上/线下零售商的消费数据与亚马逊配送网络的详细数据，通过一个静态需求模型和一个动态投资模型来量化这些权衡。结果表明，亚马逊的扩张带来了显著的运输成本节约并实现了总体规模经济；若废除 nexus 税法而代之以非歧视性税收政策，公司将分散其网络、降低运输成本，但税后价格上升导致收入下降，利润整体减少。利润与消费者福利的下降总和小于税收收入与竞争对手利润的增加，因此废除 nexus 法可能提高总福利。该文为经济理论与应用因果推断的交叉研究，其结构模型与政策反事实分析对您从事的 IV 和因果推断应用有参考价值。
- **关键技术**: `static demand model`, `dynamic investment model`, `counterfactual policy simulation`, `network densification`, `vertical integration`
- **为什么对您有用**: 本文属于经济理论（secondary interest）中的应用因果推断工作，使用结构模型进行政策反事实分析，与您关注的 IV 和因果推断应用方向直接相关。武器库中 'estimation theory in causal inference' 和 'identification theory in causal inference' 可用于理解其识别策略和估计方法。本文是经济领域实证研究的优秀范例，值得花时间阅读全文以学习其建模思路和数据整合方式。

### 6. [10.3982/ecta19039](https://doi.org/10.3982/ecta19039) — Misallocation and Capital Market Integration: Evidence From India
- **作者**: Natalie Bau, Adrien Matray
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · Princeton University
- **分类**: vol 91 · issue 1 · pp 67-106
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用印度1990年代外国资本自由化政策的分行业交错实施，识别资本错配的变化及其对全要素生产率的影响。核心挑战在于如何从企业层面的投入楔子（input wedges）中分离出政策冲击的因果效应。作者采用双重差分框架，比较受自由化影响行业与未受影响行业中高、低边际资本产出（MRPK）企业的动态差异。关键识别假设是自由化外生于企业层面的MRPK分布，且通过行业-年份固定效应控制共同趋势。方法上，本文提出一种利用自然实验来界定错配变化对行业加总生产率影响上界的新方法，无需依赖结构模型的强参数假设。实证发现：自由化使高MRPK国内企业的收入增长23%、资本增长53%、工资支出增长28%，同时MRPK下降33%；效应在本地银行体系欠发达地区更大。最后，受处理行业的索洛残差提升3-16%。对您而言，本文是经济理论（应用因果推断）方向的高质量实证范例，展示了如何将交错DID与异质性处理效应结合来回答资源配置效率问题。
- **关键技术**: `staggered difference-in-differences`, `input wedges`, `marginal revenue product of capital (MRPK)`, `Solow residual`, `natural experiment bounding`
- **为什么对您有用**: 本文属于经济理论（应用因果推断）方向，直接对应您的secondary interest。其核心方法——交错DID与异质性处理效应分析——是您武器库中'因果推断中的估计理论'的典型应用场景。本文提出的'利用自然实验界定错配效应上界'的方法，可与您熟悉的minimax bound思路形成互补：您可以用非参数下界工具检验该上界是否紧。中期可做：若想将此类实证框架迁移到流行病学或发展经济学中的资源配置问题，需先在'moderately_familiar'的识别理论（如工具变量与错配的联合识别）上补强。

### 7. [10.3982/ecta18580](https://doi.org/10.3982/ecta18580) — The Race Between Preferences and Technology
- **作者**: Joachim Hubmer
- **期刊/来源**: Econometrica
- **机构**: University of Pennsylvania
- **分类**: vol 91 · issue 1 · pp 227-261
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究美国劳动份额长期变化的原因，认为必须统一分析消费与生产两方面。首先，利用全美消费者支出数据，发现高收入家庭在劳动密集型商品和服务上的消费占比更高；这一非位似偏好意味着经济增长通过收入效应提高总劳动份额。其次，利用要素份额和资本密集度的细分数据，发现设备密集型行业的劳动份额下降更大；据此估计资本与劳动为总替代关系，且投资专有技术进步降低劳动份额。在估计的弹性下，一个简约的新古典模型能定量匹配1950年代以来劳动份额的低频变动——1980年前相对稳定、之后持续下降。对您而言，本文是经济理论方向的应用型论文，展示了如何将非位似偏好和要素替代弹性等概念与宏观数据结合，为因果推断中的结构估计提供了可借鉴的实证策略。
- **关键技术**: `nonhomothetic preferences`, `factor substitution elasticity`, `investment-specific technical change`, `neoclassical growth model`, `household expenditure data`
- **为什么对您有用**: 本文属于经济理论方向的应用论文，直接对应您的secondary interest中的经济理论。它展示了如何利用消费与生产的微观数据识别偏好和技术参数，其结构估计思路（非位似偏好+要素替代弹性）对您理解宏观因果推断中的identification策略有参考价值。武器库中'identification theory in causal inference'可帮助您拆解其识别假设是否可信，但本文核心是宏观模型而非统计方法，属于中期可读——需先熟悉宏观劳动份额文献的基本设定。

### 8. [10.3982/ecta911sec](https://doi.org/10.3982/ecta911sec) — The Econometric Society Annual Reports Report of the Secretary
- **作者**: 
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 1 · pp 331-347
- 相关性 0/10 · novelty: `survey`
- **摘要**: 本文是计量经济学会的年度秘书报告，主要汇报学会的会员与机构订阅数据。报告通过六张表格展示了个人会员与机构订阅者的数量变化趋势，包括从印刷版向纯在线订阅的持续转移、机构订阅在许可证模式下的回升、以及不同国家和地区的会员分布变化。数据显示，学会总会员数较2015年增长近四分之一，非洲和亚洲（尤其是中国）会员增长显著，而英国和德国有所下降。欧洲地区的机构订阅在多年下滑后出现显著复苏。本文不涉及任何统计方法或理论贡献，纯粹是学会运营数据的汇总。对于您而言，这是一篇了解计量经济学会规模和地理分布现状的参考材料，但无方法学价值。
- **为什么对您有用**: 本文属于经济学会的行政报告，不涉及任何统计方法或因果推断内容，与您的主要兴趣（因果推断、高维统计、半参数理论等）和次要兴趣（经济理论应用）均无直接关联。武器库中没有任何工具可以用于分析此类纯描述性数据汇总。不值得花时间阅读全文。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

