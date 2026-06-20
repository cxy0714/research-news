# Econometrica — Vol 92  Issue 5  ·  2026-06-21

- 共 12 篇 · Econometrica
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 16 篇）：10.3982/ecta925sum

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期Econometrica Vol 92 Issue 5的12篇论文大致可归纳为三条主线：**因果识别与推断**（约6篇，涉及RCT调整偏倚、自然实验、网络溢出、长期制度效应等）、**空间/时间序列方法**（1篇，聚焦空间单位根及其对回归推断的影响）、以及**经济理论与结构建模**（5篇，涵盖机制设计、生产网络、财政政策、契约链等）。各主线下的代表论文依次为：Exact Bias Correction for Linear Adjustment、Historical Self-Governance、Random Votes to Parties、Propagation and Amplification、Rise of Fiscal Capacity（因果主线）；Spatial Unit Roots and Spurious Regression（空间方法主线）；Lifestyle Behaviors、Endogenous Production Networks、Can Deficits Finance Themselves?、Robust Real Rate Rules、Contractual Chains、On the Structure of Informationally Robust Optimal Mechanisms（理论主线）。

**因果识别主线**最为突出，且方法多样。Exact Bias Correction for Linear Adjustment of Randomized Controlled Trials 在Freedman的随机化模型下推导了OLS调整估计量的精确闭式偏倚校正，并证明与交互项调整结合可彻底化解有限样本偏倚，直接关联RCT中的半参数推断。Historical Self-Governance and Norms of Cooperation 利用瑞士中世纪贵族绝嗣作为外生冲击，结合面板数据和安慰剂检验，识别自我治理对合作规范的长期因果效应，展示了自然实验与长期追踪数据的结合。Random Votes to Parties and Policies in Coalition Governments 借助选票上政党符号位置随机化的工具变量，估计投票冲击对联盟政府政策分配的因果效应，属于典型的随机化自然实验。Propagation and Amplification of Local Productivity Spillovers 通过工厂级微观数据识别企业网络内部知识共享带来的生产率溢出，并用结构化模型进行反事实模拟，体现了网络因果路径的识别与量化。Rise of Fiscal Capacity 使用帝国税征收的准随机冲击作为IV，估计财政中央化对领土整合的因果效应，机制通道涉及收入、军事与联姻。

**空间/时间序列方法** 的Spatial Unit Roots and Spurious Regression 将时间序列单位根理论推广至空间过程，揭示在空间单位根下即使使用聚类或HAC标准误仍会产生虚假回归，并开发了空间单位根检验与平稳性检验，对处理持久空间数据的推断有直接参考。**经济理论主线**中的论文多采用结构估计或最优化框架：Lifestyle Behaviors 用异质性代理人生命周期模型量化健康努力的贡献；Endogenous Production Networks 构建一般均衡模型分析供应链不确定性下的网络重组与宏观效应；Can Deficits Finance Themselves? 通过定量模型校准识别财政赤字自我融资的条件；Robust Real Rate Rules 在极弱假设下证明利率规则能保证均衡唯一性；Contractual Chains 用顺序合同设计实现帕累托有效均衡。这些工作虽偏理论，但提供了结构模型与识别策略结合的范本。

对于**因果推断**方向的研究者，优先看Exact Bias Correction for Linear Adjustment（RCT精确偏倚校正）、Historical Self-Governance（长期因果效应识别）、Random Votes to Parties（自然实验与工具变量）、以及Propagation and Amplification（网络因果识别）。**半参数效率**方向可重点关注Exact Bias Correction中的精确偏倚公式与交互项调整。**空间/时间序列**方向直接阅读Spatial Unit Roots。**高维/网络**方向可参考Propagation and Amplification（高维网络溢出）和Endogenous Production Networks（内生网络估计）。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.3982/ecta20289](https://doi.org/10.3982/ecta20289) — Exact Bias Correction for Linear Adjustment of Randomized Controlled Trials
- **作者**: Haoge Chang, Joel A. Middleton, P. M. Aronow
- **期刊/来源**: Econometrica
- **机构**: Columbia University · Yale University
- **分类**: vol 92 · issue 5 · pp 1503-1519
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在随机化实验的 randomization model 下，目标是估计平均处理效应（ATE），Freedman (2008) 指出线性回归调整估计量存在偏倚。本文在 Freedman 的原始假设下，推导了该 OLS 调整估计量的精确闭式偏倚校正项（exact closed-form bias correction）。理论证明校正后估计量的极限分布与未校正估计量完全相同；结合 Lin (2013) 的交互项调整结果，表明 Freedman 对回归调整的理论质疑可通过微小的实践修改（加交互项+偏倚校正）彻底化解。对您有用：此工作为 RCT 中回归调整的有限样本偏倚提供了精确的数学刻画，直接连接到因果推断估计理论中对 ATE 估计量偏倚-方差权衡的关注。
- **关键技术**: `randomization-based inference`, `exact bias correction`, `regression adjustment in RCT`, `Freedman bias`, `Lin estimator with interactions`, `asymptotic distribution of ATE estimator`
- **为什么对您有用**: 直接连接到因果推断中 RCT 估计理论（regression adjustment 的偏倚与效率）。您武器库中 very_familiar 的 M-estimation theory 与高维渐近理论可直接用来审视该偏倚校正项在更复杂设定（如高维协变量调整、semiparametric adjustment）下的表现，甚至推导类似的精确偏倚表达式。立即可做：用 very_familiar 的 M-estimation 与 minimax 工具，将此 exact bias correction 推广到高维 debiased-ML 调整或 semiparametric sieve 调整的 RCT 场景，验证偏倚校正是否仍可闭式表达。

## 经济理论 / 应用  *(econ_theory, 11 篇)*

### 1. [10.3982/ecta21654](https://doi.org/10.3982/ecta21654) — Spatial Unit Roots and Spurious Regression
- **作者**: Ulrich K. Müller, Mark W. Watson
- **期刊/来源**: Econometrica
- **机构**: Princeton University
- **分类**: vol 92 · issue 5 · pp 1661-1695
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究经济变量中强空间依赖（spatial unit root）的建模及其对回归推断的影响，设定为空间过程具有类似时间序列单位根的累积性冲击结构。核心发现是：在空间单位根过程下，即使使用聚类标准误或空间 HAC 修正，回归仍会产生虚假显著性（spurious regression），这与时间序列单位根文献的经典结论完全对应。作者基于空间过程的渐近理论，开发了适用于大样本的空间单位根检验与平稳性检验，并通过模拟研究了持久空间数据下的有效推断策略（如空间差分变换）。实证部分以 Chetty et al. (2014) 的跨区域回归为例展示了问题的严重性与方法有效性。对您有用：本文将时间序列单位根理论完整迁移到空间设定，为处理空间持久性数据的因果/回归推断提供了新视角。
- **关键技术**: `spatial unit root process`, `spurious regression`, `spatial HAC`, `spatial first-differencing`, `large-sample spatial unit root test`, `stationarity test`
- **为什么对您有用**: 本文直接连接到经济理论（secondary interest）中的空间因果推断与回归推断问题，空间单位根导致的虚假回归对跨区域因果估计（如 Chetty 的邻里效应 IV 研究）有根本性影响。您武器库中的高维渐近理论与 minimax bound 工具可以用来分析本文提出的空间单位根检验在更一般空间网络结构下的功效界与 sharper rate。Follow-up 判断：**中期可做**——需先在 moderately_familiar 的 M-estimation 理论上长肌肉，以将本文的空间渐近理论推广到半参数空间 IV/因果估计的 efficiency bound 分析。

### 2. [10.3982/ecta20603](https://doi.org/10.3982/ecta20603) — Lifestyle Behaviors and Wealth‐Health Gaps in Germany
- **作者**: Lukas Mahler, Minchul Yum
- **期刊/来源**: Econometrica
- **机构**: KU Leuven · Center for Economic and Policy Research · Virginia Commonwealth University
- **分类**: vol 92 · issue 5 · pp 1697-1733
- 相关性 5/10 · novelty: `application`
- **摘要**: 该文利用德国行政面板数据，系统刻画了健康状态与财富水平在整个生命周期中的显著差距——即便在全民医保且自付医疗支出极低的环境下依然存在。为了探明差距的成因，作者构建了一个异质性代理人生命周期模型，其中健康与财富互为内生演化，个体通过投入“健康生活方式”努力来维持未来健康，且努力行为受调整成本约束以匹配习惯形成特征。通过结构估计校准模型，发现模型能够再现绝大多数的实证财富-健康差距，并量化了健康影响财富的两个传导渠道：劳动收入（因病丧失工作能力）和储蓄动机（预防性储蓄）。进一步的反事实分解表明，个体健康努力程度的差异可以解释约四分之一的模型生成财富差距，从而揭示行为选择是放大财富-健康差距的重要机制。对您而言，这是一篇高质量的经济学应用论文，其模型设定（特别是健康努力作为内生变量且带有习惯调整成本）和分解方法可为您后续在流行病学或健康经济学中研究因果机制时提供分析框架与数据结构的参考。
- **关键技术**: `heterogeneous-agent life-cycle model`, `structural estimation`, `calibration`, `habit formation adjustment costs`, `counterfactual decomposition`, `panel data (German SOEP)`
- **为什么对您有用**: 本文属于 secondary interest 中的经济理论应用，属于 gateway reading 范畴。论文清晰展示了经济学家如何用结构模型将健康行为（努力）内生化并量化其对财富差距的贡献，数据侧（SOEP）与模型侧（生命周期最优化、调整成本）都阐述得较为充分，适合作为了解该领域分析范式的入门读物。您的技术库中，**非参数估计与因果推断**可以用于批判性地检查模型假设（如健康生产函数的函数形式、努力变量的外生性假定），而**M-估计理论**可帮助您理解其结构估计的识别条件是否稳健。总体而言，本文值得花时间通读全文，以获取建模灵感并评估数据结构的可迁移性。

### 3. [10.3982/ecta20579](https://doi.org/10.3982/ecta20579) — Historical Self‐Governance and Norms of Cooperation
- **作者**: Devesh Rustagi
- **期刊/来源**: Econometrica
- **机构**: University of Warwick
- **分类**: vol 92 · issue 5 · pp 1473-1502
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文利用瑞士中世纪贵族绝嗣导致部分市政自然实验性获得自我治理的历史事件，识别自我治理对合作规范的长期因果效应。研究设定以贵族绝嗣作为外生冲击，比较历史上自我治理与继续封建的市政在数百年后的合作行为差异。核心数据来源包括行为实验中的公共品博弈、世界价值观调查的主观规范指标以及瑞士家庭面板的客观行为记录，并通过150年以上的投票率数据追踪效果的时间动态。识别策略依赖历史边境和家庭登记数据进行安慰剂检验与排除迁移干扰，支持文化传播而非经济差异的解释。实证一致显示自我治理显著提升了合作规范，且该效应持续并映射到慈善捐赠和环境保护等社会偏好行为。对您有用的价值在于，本文展示了自然实验与长期面板数据结合识别文化制度因果效应的经典范例，适合作为了解经济史因果推断应用的高质量入门文献。
- **关键技术**: `Natural experiment`, `Historical difference-in-differences`, `Behavioral experiment`, `Cultural persistence`, `Panel data analysis`
- **为什么对您有用**: 本文属于经济理论与应用因果推断的交叉方向，直接关联您在secondary interests中对经济理论（数据集、模型、应用因果工作）的兴趣。您武器库中『estimation theory in causal inference』（very_familiar）足以理解其识别策略和估计方法，无需额外工具。作为一篇高质量的应用因果论文，它清晰展露了历史自然实验的构造、长期面板数据的利用以及不可观测混淆的排除论证，值得花时间全文阅读以获取实证设计灵感。

### 4. [10.3982/ecta20029](https://doi.org/10.3982/ecta20029) — Propagation and Amplification of Local Productivity Spillovers
- **作者**: Xavier Giroud, Simone Lenzu, Quinn Maingi, Holger Mueller
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · Columbia University · New York University · University of Southern California · California Southern University · European Corporate Governance Institute
- **分类**: vol 92 · issue 5 · pp 1589-1619
- 相关性 3/10 · novelty: `application`
- **摘要**: 在量化空间经济学框架下，研究大型工厂开业产生的局部生产率溢出如何通过多区域企业的内部知识共享网络向远距离传播与放大。核心 estimand 是非局部（全局）生产率溢出效应及其随距离/行业知识关联的衰减模式。方法上，先用 Census 工厂级微观数据做 reduced-form 回归，识别出跨数百英里、不随距离衰减且在知识共享行业间更强的溢出；随后估计一个结构化量化空间模型，将多区域企业各工厂通过共享知识链接，并进行反事实模拟。实证结果表明，欠发达地区局部效应更大，但发达地区因网络连通度更高而产生更大的总体增益。对您有用：本文展示了企业网络结构如何作为因果传播路径，为经济因果推断中的网络 mediation / interference 设定提供了真实数据与结构模型范例。
- **关键技术**: `plant-level microdata regression`, `quantitative spatial model`, `counterfactual simulation`, `network-mediated spillover`, `knowledge-sharing linkage`
- **为什么对您有用**: 本文直接连接经济理论中的因果推断应用：企业内部网络作为因果传播路径，实质上是 network interference / mediation 问题，与您 primary interest 中的 causal inference (mediation, longitudinal) 交叉。您可用 very_familiar 的 estimation theory in causal inference 分析其 reduced-form 回归的 identification 假设（如 no unobserved network confounding），或用 moderately_familiar 的 identification theory 探索结构模型中网络 mediation 的非参数 identification 条件。Follow-up 判断：中期可做——需先在 moderately_familiar 的 identification theory 上长肌肉，以将网络 interference 的 semiparametric identification 形式化。

### 5. [10.3982/ecta20629](https://doi.org/10.3982/ecta20629) — Endogenous Production Networks Under Supply Chain Uncertainty
- **作者**: Alexandr Kopytov, Bineet Mishra, Kristoffer Nimark, Mathieu Taschereau-Dumouchel
- **期刊/来源**: Econometrica
- **机构**: University of Rochester · Cornell University
- **分类**: vol 92 · issue 5 · pp 1621-1659
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文构建了一个内生生产网络形成的一般均衡模型，研究供应链不确定性如何影响企业供应商选择及宏观经济。模型假设企业在追求成本最小化的同时，需考量供应商的稳定性；当不确定性上升时，企业会转向更稳定的供应商（即使报价更高），这导致生产网络重组。均衡中，网络重组倾向于降低宏观经济的波动性，但以总产出下降为代价。模型还指出，生产率更高、更稳定的企业在网络均衡中拥有更大的Domar权重（即作为供应商的系统重要性）。作者利用美国数据对模型进行校准，量化了上述机制的重要性。对于统计学者而言，本文提供了一个将网络模型嵌入宏观经济框架的实例，展示了结构估计的思路。
- **关键技术**: `endogenous network formation`, `general equilibrium model`, `Domar weights`, `calibration`, `supply chain uncertainty`
- **为什么对您有用**: 本文属于经济理论（次要兴趣），是宏观经济学中生产网络结构模型的代表作品。对于入门阅读，本文模型设定清晰但需一定经济学背景（如一般均衡、Domar权重），非经济学统计学家可能需要补充宏观经济学基础才能完全吸收。技术武器库中熟悉网络分析和因果推断有助于理解部分机制，但缺乏对结构估计和DSGE范式的直接训练，因此暂不可直接迁移工具。若研究者希望了解经济学家如何用模型刻画供应链冲击的因果效应，本文值得读引言和建模部分，但全文深入需额外学习。

### 6. [10.3982/ecta20612](https://doi.org/10.3982/ecta20612) — The Rise of Fiscal Capacity: Administration and State Consolidation in the Holy Roman Empire
- **作者**: Davide Cantoni, Cathrin Mohr, Matthias Weigand
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · Ludwig-Maximilians-Universität München · Fafo Foundation · University of Bonn · Harvard University
- **分类**: vol 92 · issue 5 · pp 1439-1472
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究财政能力（fiscal capacity）对欧洲国家整合的作用，设定为神圣罗马帝国早期现代领土与城市的新面板数据集，关键识别策略利用帝国税（Imperial taxes）征收的准随机时间与规模作为冲击。核心方法为基于准随机外生冲击的 IV 设计，估计财政中央化改革对领土存活、规模扩张与形态紧凑的因果效应，并检验收入增加、军事投资与联姻成功三个机制通道。实证结果显示，实施早期财政改革的领土更可能存活且版图更紧凑；帝国税冲击提高了统治者建立高效税制的收益，驱动财政中央化，内部行政机构（Chamber）的崛起则使整合国家向专制倾斜。对您可能有用：该文提供了早期现代经济史中利用准随机制度冲击做 IV 识别的完整案例，数据集与因果设计可直接作为经济理论应用因果推断的参考。
- **关键技术**: `quasi-random institutional shock`, `instrumental variables`, `mechanism channel decomposition`, `historical panel data construction`, `survival / territorial expansion analysis`
- **为什么对您有用**: 直接连接经济理论（secondary interest）中的 applied causal work 与 IV 方法；文中 quasi-random Imperial tax shock 的 IV 设计与机制分解，可用您 very_familiar 的 causal inference estimation theory 检验其识别假设的敏感性与效率。follow-up 判断：立即可做——用 very_familiar 的 IV / sensitivity analysis 工具即可对该文的准随机冲击假设与 IV 估计做 sensitivity 或效率边界复查。

### 7. [10.3982/ecta21791](https://doi.org/10.3982/ecta21791) — Can Deficits Finance Themselves?
- **作者**: George-Marios Angeletos, Chen Lian, Christian K. Wolf
- **期刊/来源**: Econometrica
- **机构**: University of California, Berkeley
- **分类**: vol 92 · issue 5 · pp 1351-1390
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在名义刚性和李嘉图等价失效（有限寿命或流动性约束）的环境中，财政赤字如何实现自我融资。作者识别出两个渠道：实际经济繁荣扩大税基，以及通货膨胀侵蚀名义债务的实际价值。主要理论结果表明，如果货币当局不强烈紧缩以抵消财政刺激，且财政调整延迟到足够远，则赤字可以完全自我融资——债务最终收敛回初始水平，无需未来增税或减支。方法上采用定量宏观经济模型，结合宏观时间序列和微观估计（如边际消费倾向、价格粘性参数）进行校准与反事实模拟。实证结果显示，在合理的参数取值下，显著程度的自我融资是可行的。该论文对您（统计学家）而言，可作为理解宏观财政政策识别（如财政乘数的因果推断）的一个入口，其中校准方法与动态模型的反事实分析值得关注。
- **关键技术**: `nominal rigidity`, `Ricardian equivalence`, `fiscal theory of the price level`, `marginal propensity to consume`, `quantitative macroeconomic calibration`
- **为什么对您有用**: 本文属于经济理论中财政动态模型的应用，作为gateway reading： (1) 摘要清晰，非专家可理解核心机制和结论，但需一定宏观经济学背景，可作为入门读物； (2) 您的武器库（因果推断中的IV方法、非参数估计、高维统计）可部分迁移到宏观乘数识别问题，但缺乏动态宏观建模和校准经验，属于中期可做（需先学习定量宏观经济学方法）； (3) 值得花时间读全文，因为其识别策略（利用政策时间序列变化）和校准思路（结合微观证据约束宏观参数）对统计学家有启发，且问题本身重要。

### 8. [10.3982/ecta20240](https://doi.org/10.3982/ecta20240) — On the Structure of Informationally Robust Optimal Mechanisms
- **作者**: Benjamin Brooks, Songzi Du
- **期刊/来源**: Econometrica
- **机构**: University of Chicago · University of California San Diego
- **分类**: vol 92 · issue 5 · pp 1391-1438
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在机制设计设定下，研究设计者对代理人信息结构及均衡选择均不确定时的最优机制，estimand 为机制的最大保证值与信息结构的最小潜力值。核心方法是将问题转化为一对线性规划：一个给出所有机制最大保证值的下界，另一个给出所有信息结构最小潜力值的上界。通过求解这对 LP，在公共支出、双边贸易与最优拍卖三个经典经济模型中，刻画了保证值最大化机制与潜力值最小化信息结构，并证明 max-guarantee = min-potential 的等式成立。该结果为信息鲁棒机制设计提供了可计算的 LP 框架与极小极大对偶刻画。对您有用之处在于：它展示了如何在经济模型中用线性规划求解 worst-case 下的极小极大问题，与您在 minimax bounds 和 estimation theory 中的数学训练直接相通。
- **关键技术**: `informationally robust mechanism design`, `min-max duality via linear programming`, `worst-case equilibrium analysis`, `potential vs guarantee characterization`, `optimal auction under information uncertainty`
- **为什么对您有用**: 本文属于经济理论（机制设计）方向，核心是 worst-case 下的极小极大对偶与 LP 可计算性，与您 primary interest 中的 minimax bounds 数学工具直接对应。您武器库中 very_familiar 的 minimax bounds for estimation problems 可用来审视此文中 max-guarantee/min-potential 对偶界是否紧致，以及 LP 松弛与真实极小极大值的 gap 问题。Follow-up 判断：**中期可做**——若想将此 LP 框架迁移到因果推断或高维统计中的 worst-case identification / sensitivity 分析，需先在 moderately_familiar 的 identification theory in causal inference 上长肌肉，构建类似的信息结构不确定性建模。

### 9. [10.3982/ecta21069](https://doi.org/10.3982/ecta21069) — Robust Real Rate Rules
- **作者**: Tom D. Holden
- **期刊/来源**: Econometrica
- **机构**: Deutsche Bundesbank
- **分类**: vol 92 · issue 5 · pp 1521-1551
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究中央银行如何通过名义利率规则避免自生性波动（self-fulfilling fluctuations），目标 estimand 是能实现唯一均衡（determinacy）的利率反馈系数。核心提出“real rate rule”：名义利率对实际利率（由通胀保值债券推断）的响应系数为1，在此设定下证明该规则在关于家庭与企业行为的极弱假设下仍能保证均衡唯一性。鲁棒性涵盖家庭异质性、hand-to-mouth消费者、非理性预期、主动财政政策及任意跨期或名义-真实联动形式；引入时变短期通胀目标后，该规则可实施任意通胀路径（含最优政策），为将决策者合意通胀路径转化为名义利率路径提供显式映射。实证表明美联储行为与 real rate rule 推论高度吻合，机制核心在于 Fisher equation 在货币传导中的关键锚定作用。对您可能有用：若关注经济理论中的因果/结构模型识别，本文在极弱行为假设下给出均衡唯一性的充分条件，是宏观货币政策鲁棒识别的范例。
- **关键技术**: `real rate rule`, `equilibrium determinacy`, `Fisher equation anchoring`, `time-varying inflation target`, `TIPS-implied real rates`
- **为什么对您有用**: 本文属于经济理论（宏观货币政策）的 gateway reading：对您而言，(1) 它是了解宏观均衡唯一性（determinacy）与利率规则鲁棒识别的极佳入门，逻辑清晰且不依赖复杂动态随机一般均衡（DSGE）估计；(2) 武器库中的 identification theory in causal inference 可帮助审视其“极弱假设下仍保证唯一均衡”的识别逻辑是否可迁移至其他结构因果模型；(3) 值得花时间读全文——理论证明简洁，实证部分用 TIPS 数据推断实际利率的操作对统计计算有参考价值，但方法学 novelty 属于经济理论内部推进，非统计新方法。

### 10. [10.3982/ecta19797](https://doi.org/10.3982/ecta19797) — Contractual Chains
- **作者**: Joel Watson
- **期刊/来源**: Econometrica
- **机构**: University of California San Diego
- **分类**: vol 92 · issue 5 · pp 1735-1774
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在给定网络结构的私有双边签约环境下，分散签约能否通过顺序合同设计内部化外部性。模型假设生产行动全局可验证且转移可外部执行，但参与者只能与网络邻居签约。主要结论是存在一种“签约制度”——允许顺序签约和撤销——可以为任何连通网络和基础博弈支持帕累托有效均衡。关键机制是“保证合同”和“取消罚金”，使参与者在签约阶段能够可信地承诺未来的行动。该结果理论上证明了即使在高度分散的签约环境下，通过制度设计也能实现效率。对于统计学家，本文可作为经济理论入门阅读，尤其适合希望理解合同设计逻辑的研究者，但统计工具并不直接适用。与您次要兴趣“经济理论”一致，建议作为跨学科拓展阅读。
- **关键技术**: `bilateral contracting`, `contracting institution`, `assurance contracts`, `sequential contract formation`, `externality internalization`, `network games`
- **为什么对您有用**: 本文属于经济理论方向，与您次要兴趣中的“经济理论（模型）”直接对应。武器库中的非参数统计、因果推断等工具不直接适用于本文的博弈论模型，但本文可作为经济理论入门阅读，帮助理解合同设计与外部性内部化的结构，为将来研究涉及合同网络的因果推断问题提供背景。由于您的武器库缺乏博弈论和合同理论核心工具，目前暂不可做直接的follow-up，但值得花时间阅读全文以拓展跨学科视野。

### 11. [10.3982/ecta20942](https://doi.org/10.3982/ecta20942) — Random Votes to Parties and Policies in Coalition Governments
- **作者**: Matteo Cervellati, Giorgio Gulino, Paolo Roberti
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · International Zinc Association · Fafo Foundation · University of Bologna · University of Rome Tor Vergata · Free University of Bozen-Bolzano
- **分类**: vol 92 · issue 5 · pp 1553-1588
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文利用意大利所有地方选举中政党符号在选票上位置随机化的自然实验，估计增加对某个政党的投票如何影响联盟政府的政策分配。随机化带来非边际的投票冲击，使得预算支出向受冲击政党的竞选纲领倾斜，但仅限于该政党强调的议题。进一步机制分析表明，更高的选举支持转化为执政联盟内更大的谈判权，并影响内阁成员的任命及其人口特征。方法上，作者利用选举中的抽签作为工具变量，结合回归和固定效应模型识别因果关系。研究为投票如何通过联盟政治机制转化为政策提供了可靠的因果证据。该工作对您在因果推断和经济学应用方面的兴趣有直接参考价值，尤其是自然实验的设计和识别策略。
- **关键技术**: `natural experiment`, `randomization`, `causal inference`, `coalition bargaining`, `budgetary spending analysis`
- **为什么对您有用**: 本文属于经济理论（应用）方向，与您的因果推断兴趣高度契合。它展示了如何利用自然实验在复杂的政治联盟场景中识别因果效应——这正是您感兴趣的identification理论在经济学中的应用。您可以用熟悉的非参数估计和识别理论来批判性评估其识别假设（如排除限制、随机化有效性），属于立即可做的阅读。该数据集和分析框架也可以作为您未来在应用因果推断中设计类似自然实验的参考。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

