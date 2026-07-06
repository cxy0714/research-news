# Econometrica — Vol 91  Issue 5  ·  2026-07-06

- 共 10 篇 · Econometrica
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 13 篇）：10.3982/ecta915forth

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Econometrica 第 91 卷第 5 期整体围绕两条主线展开：一是**因果识别与结构估计的桥接**，二是**市场设计与信息结构的经济理论**。前者集中在应用微观与宏观论文中，强调如何将准实验或随机化设计的因果证据嵌入结构模型，以量化反事实或政策效应；后者则覆盖重复博弈、机制设计、平台经济学和信用评分等理论议题，关注激励、信息与均衡的交互。此外，气候适应与债务展期等宏观动态模型构成第三条较弱的线索。

在因果识别与结构估计这条主线上，本期有多篇论文展示了不同层次的桥接策略。**Selection Into Credit Markets** 利用两阶段随机化识别信贷市场自选择导致的回报异质性，直接估计了借款者与非借款者的因果回报差异，并诊断配给失灵。**What Can Time‐Series Regressions Tell Us** 则从时间序列角度出发，证明在宏观线性模型中，只要识别了现行政策下的冲击效应，即可构造反事实政策动态，从而桥接局部投影/SVAR 与结构政策评估。**The Investment Effects of Market Integration** 结合准实验变化与结构进入模型，分离市场整合对可再生能源投资的因果效应，强调忽略投资效应会低估整合收益。**The Macro Impact of Short‐Termism** 则用微观断点回归思路识别短期主义对 R&D 的因果影响，再嵌入内生增长模型量化宏观福利损失。这几篇的共同特点是：先用因果推断方法（随机实验、准实验、断点）得到局部或微观参数，再通过结构模型外推至反事实或宏观场景。

市场设计与信息结构这条理论主线同样密集。**Platform Design When Sellers Use Pricing Algorithms** 研究平台如何通过需求引导规则破坏算法合谋，核心机制是奖励降价的卖家以额外曝光，模拟中使用了 Q-learning 算法。**Monitoring versus Discounting in Repeated Games** 推导了贴现与监测精度之间的替代关系，用信息论不等式刻画合作可行性边界。**Regret‐Minimizing Project Choice** 在委托-代理框架下比较单项目与多项目环境，发现多项目环境通过提供备选方案降低委托人遗憾。**A Quantitative Theory of the Credit Score** 将信用评分解释为贝叶斯更新，证明其能实现完全信息配置，并用结构估计量化信息限制的分配效应。这些论文虽不直接涉及因果推断，但其对信息结构、激励兼容性和均衡选择的分析，为因果识别中的工具变量强度、未观测混杂等理论问题提供了可迁移的框架。

与因果推断方向最贴合的论文是 **Selection Into Credit Markets**（两阶段随机化与异质性回报）、**What Can Time‐Series Regressions Tell Us**（因果估计与反事实桥接）和 **The Investment Effects of Market Integration**（准实验+结构模型）。半参数效率方向可关注 **What Can Time‐Series Regressions Tell Us** 中关于冲击可加性与线性结构的假设。高维或随机矩阵方向本期无直接相关论文。

## 经济理论 / 应用  *(econ_theory, 10 篇)*

### 1. [10.3982/ecta18916](https://doi.org/10.3982/ecta18916) — Selection Into Credit Markets: Evidence From Agriculture in Mali
- **作者**: Lori Beaman, Dean Karlan, Bram Thuysbaert, Christopher Udry
- **期刊/来源**: Econometrica
- **机构**: Kellogg's (Canada) · Abdul Latif Jameel Poverty Action Lab
- **分类**: vol 91 · issue 5 · pp 1595-1627
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文利用马里的农业贷款两阶段随机实验，检验信贷市场中的自选择是否预示资本回报率的异质性。第一阶段随机将村庄分为贷款提供组和对照组；第二阶段在无贷款村庄对所有农户、在有贷款村庄对未借款农户随机发放现金赠款。通过比较不同子组的资本回报率，识别出借款者的季节性回报率高达130%，而非借款者的回报率接近零。研究还发现部分基线贫困农户具有高回报却未获得贷款，表明信贷市场存在配给失灵。该文为发展经济学中信贷市场模型和政策设计提供了关键实证证据。对您而言，这是一篇高质量的应用因果推断论文，其两阶段随机化设计和异质性回报分析思路可迁移至流行病学或发展干预中的因果效应异质性研究。
- **关键技术**: `two-stage randomized experiment`, `heterogeneous treatment effects`, `selection into credit`, `returns to capital`, `cash grant experiment`
- **为什么对您有用**: 本文属于经济理论（发展经济学）的应用因果推断工作，直接对应您的 secondary interest 中的经济理论方向。其两阶段随机化设计是识别自选择偏误的经典策略，您可以用 very_familiar 的因果推断估计理论（如 IV 或断点回归）来理解其识别假设，并思考如何将类似设计应用于流行病学队列研究中的选择偏误校正。本文是值得全文阅读的实证范本，但属于应用型工作，方法学 novelty 有限。

### 2. [10.3982/ecta21045](https://doi.org/10.3982/ecta21045) — What Can Time‐Series Regressions Tell Us About Policy Counterfactuals?
- **作者**: Alisdair McKay, Christian K. Wolf
- **期刊/来源**: Econometrica
- **机构**: Federal Reserve Bank of Minneapolis · Moscow Institute of Thermal Technology
- **分类**: vol 91 · issue 5 · pp 1695-1725
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究在一般线性化结构宏观经济模型中，如何利用时间序列回归估计的政策冲击因果效应来构造反事实政策结果。作者证明，只要能够识别现行政策规则下的同期冲击和新闻冲击的因果效应，就足以推导出替代政策规则下的反事实动态。若研究者愿意指定损失函数，该方法还能恢复最优政策规则。关键假设是模型结构线性且冲击可加，在此条件下反事实和最优政策对卢卡斯批判具有稳健性。文章还讨论了当实证因果证据有限时的应用策略。核心贡献在于桥接了实证因果估计（如局部投影、SVAR）与结构政策评估之间的鸿沟，为宏观经济学中的政策反事实分析提供了半参数识别框架。对您而言，本文展示了因果推断方法在宏观政策评估中的直接应用，尤其适合作为经济理论方向的门槛读物。
- **关键技术**: `local projections`, `structural VAR`, `impulse response functions`, `policy counterfactuals`, `Lucas critique`, `loss function optimization`
- **为什么对您有用**: 本文直接连接您的 secondary interest 'economic theory (application, data sets, causal inference)'，展示了如何将时间序列因果估计（局部投影、SVAR）用于政策反事实分析。您的武器库中 'estimation theory in causal inference' 和 'identification theory in causal inference' 足以理解其识别策略，但需要补充宏观时间序列工具（如局部投影、脉冲响应）才能动手复现或扩展。属于中期可做：需先在 moderately_familiar 的 'identification theory in causal inference' 上长肌肉，具体是理解宏观识别中的滞后阶数选择和冲击正交化。

### 3. [10.3982/ecta20769](https://doi.org/10.3982/ecta20769) — The Investment Effects of Market Integration: Evidence From Renewable Energy Expansion in Chile
- **作者**: Luis E. Gonzales, Koichiro Ito, Mar Reguant
- **期刊/来源**: Econometrica
- **机构**: Pontificia Universidad Católica de Chile · University of Chicago · Center for Economic and Policy Research
- **分类**: vol 91 · issue 5 · pp 1659-1693
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究市场整合对可再生能源投资的影响。理论部分指出，市场整合不仅通过贸易收益改善配置效率，还能激励新建可再生能源电厂的投资。以智利电力市场近年电网扩张为实证背景，利用准实验变化分析市场整合对电力生产、批发价格、发电成本和可再生能源投资的影响。构建电厂进入的结构模型，量化有无投资效应下市场整合的因果效应。发现智利市场整合使太阳能发电量增加约180%，发电成本降低8%，碳排放减少5%；大量可再生能源进入在无市场整合时不会发生。结论表明忽略投资效应会严重低估市场整合的收益及其在扩大可再生能源中的关键作用。对您而言，这是一篇经济理论+应用因果推断的实证论文，展示了如何用结构模型和准实验设计识别市场制度变化的因果效应，与您的secondary interest（经济理论的应用因果工作）直接相关。
- **关键技术**: `structural model of entry`, `quasi-experimental variation`, `difference-in-differences`, `reduced-form estimation`, `counterfactual simulation`
- **为什么对您有用**: 本文属于经济理论的应用因果工作，与您的secondary interest直接匹配。它展示了如何将市场整合的理论预测与准实验设计结合，用结构模型量化投资效应，分析模式可迁移到您关注的因果推断应用场景。作为gateway reading，本文方法学清晰，适合作为进入经济实证因果推断的入门读物；您的武器库（非参数统计、因果推断估计理论）足以理解其核心识别策略，但结构模型的具体构建（如均衡假设、反事实模拟）属于moderately_familiar领域，需花时间熟悉。值得花时间读全文以获取实证分析框架。

### 4. [10.3982/ecta18771](https://doi.org/10.3982/ecta18771) — A Quantitative Theory of the Credit Score
- **作者**: Satyajit Chatterjee, Dean Corbae, Kyle Dempsey, José-Víctor Ríos-Rull
- **期刊/来源**: Econometrica
- **机构**: Federal Reserve Bank of Philadelphia · University of Wisconsin–Madison · The Ohio State University · Center for Economic and Policy Research · University College Lahore · University of Pennsylvania
- **分类**: vol 91 · issue 5 · pp 1803-1840
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文构建了一个定量理论模型，将信用评分解释为市场对借款人不可观测类型（耐心程度）的贝叶斯更新。模型设定为持久隐藏类型，其中可观测的还款行为通过贝叶斯规则动态更新公众对类型的信念，从而形成动态声誉机制，激励借款人还款。作者证明，信用评分经济能够实现与完全信息均衡相同的配置，即信用评分是声誉机制的充分统计量。利用信用市场数据和个体信用评分演化数据，对模型进行了结构估计。反事实分析表明，若禁止追踪个体信用行为（即减少评分信息量），低类型年轻贫困借款人将因高类型借款人的补贴而受益，尽管动态还款激励下降导致利率上升。本文对您可能有用：作为经济理论中结构估计与因果推断结合的范例，其贝叶斯更新框架与您关注的identification theory和IV方法有潜在联系，且数据集（信用市场微观数据）可用于检验因果推断方法在面板设定下的表现。
- **关键技术**: `Bayesian updating`, `dynamic reputation model`, `structural estimation`, `counterfactual analysis`, `hidden type model`
- **为什么对您有用**: 本文属于经济理论（secondary interest）中的应用因果工作，其核心是识别信用评分对还款行为的因果效应，但通过结构模型而非传统IV/DML实现。武器库中'identification theory in causal inference'可用来审视其识别假设（如隐藏类型与可观测行为的独立性）是否可被放松或检验。中期可做：若想将本文的贝叶斯更新框架与您熟悉的proximal CI结合（例如将信用评分视为负对照），需先在moderately_familiar的identification theory上深入理解动态设定下的非参数识别条件。

### 5. [10.3982/ecta15420](https://doi.org/10.3982/ecta15420) — The Macro Impact of Short‐Termism
- **作者**: Stephen J. Terry
- **期刊/来源**: Econometrica
- **机构**: University of Michigan
- **分类**: vol 91 · issue 5 · pp 1881-1912
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究短期主义（short-termism）对宏观经济的影响。作者利用企业R&D投资数据，发现刚好达到华尔街盈利预测的企业R&D增长和后续创新较低，而刚好未达标的经理人薪酬较低。为量化短期主义的宏观效应，作者构建并估计了一个内生增长模型，其中短期主义自然产生于对利益冲突经理人的约束，使企业价值提升约1%。但由于R&D的社会回报（知识溢出、不完全竞争等）高于私人回报，短期主义扭曲R&D，导致年增长率降低5个基点，社会福利下降约1%。该研究结合微观实证与宏观定量模型，为理解短期主义的经济后果提供了结构估计框架。对您而言，本文展示了如何将微观因果识别（如断点回归思路）与宏观结构模型结合，是经济理论方向的应用型参考，可作为了解该领域实证策略的入门读物。
- **关键技术**: `endogenous growth model`, `structural estimation`, `R&D distortion`, `short-termism`, `firm-level regression discontinuity`
- **为什么对您有用**: 本文属于经济理论（secondary interest）的应用型论文，展示了如何将微观层面的因果推断（R&D对盈利压力的响应）嵌入宏观结构模型。武器库中的'identification theory in causal inference'可帮助理解其识别策略（如利用盈利预测阈值），但核心是宏观模型估计，与您的主要统计兴趣（因果推断、半参理论）直接交集有限。作为gateway reading，本文清晰阐述了数据、模型和假设，适合作为进入经济理论应用方向的入门读物，值得花时间读全文以了解其分析框架。

### 6. [10.3982/ecta19978](https://doi.org/10.3982/ecta19978) — Platform Design When Sellers Use Pricing Algorithms
- **作者**: Justin P. Johnson, Andrew Rhodes, Matthijs Wildenbeest
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · University of Arizona · Cornell University · Toulouse School of Economics
- **分类**: vol 91 · issue 5 · pp 1841-1879
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究平台如何通过需求引导规则（demand-steering rules）设计市场，以促进卖家竞争、提高消费者剩余和平台自身收益。理论部分证明，即使卖家具有无限耐心并试图合谋，这些仅需少量信息的政策也能产生显著的促进竞争效果。模拟部分采用人工智能定价算法（Q-learning），发现更复杂的、基于历史行为且非中性对待卖家的政策能有效破坏算法轮换需求、分割行业利润的能力，从而压低价格。核心机制是平台通过奖励降价的卖家以额外曝光，打破算法共谋的均衡。对您而言，这是一篇将因果推断中的政策干预思想应用于平台经济学的理论+模拟论文，其模拟设计（Q-learning 算法与市场设计的交互）可作为您进入经济理论应用方向的入门读物。
- **关键技术**: `Q-learning algorithms`, `demand-steering rules`, `simulation-based policy evaluation`, `algorithmic collusion`, `platform design`
- **为什么对您有用**: 本文属于经济理论（secondary interest）的应用论文，适合作为 gateway reading：它清晰阐述了平台设计这一经济学问题，并展示了如何用模拟方法（Q-learning）评估政策效果，对不熟悉经济学的统计学者友好。武器库中 'estimation theory in causal inference' 和 'software development' 可用于理解其模拟框架，但核心机器（算法博弈论、Q-learning 的收敛性）不在武器库内，因此暂不可做——需先补充算法博弈论或强化学习基础。

### 7. [10.3982/ecta20442](https://doi.org/10.3982/ecta20442) — Mitigating Disaster Risks in the Age of Climate Change
- **作者**: Harrison Hong, Neng Wang, Jinqiang Yang
- **期刊/来源**: Econometrica
- **机构**: Columbia University · Cheung Kong Graduate School of Business · Shanghai University of Finance and Economics · Shanghai University of International Business and Economics
- **分类**: vol 91 · issue 5 · pp 1763-1802
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文在气候变化的背景下，构建了一个动态均衡模型来研究社会如何通过适应性投资（企业层面的努力和公共支出）来管理自然灾害对资本存量的风险。模型假设灾害到达率受全球变暖影响，且社会通过贝叶斯学习不断更新对气候后果的认知。最优适应性政策随学习过程动态调整，并需要同时征收资本税和碳税才能实现一阶最优。作者将模型应用于热带气旋引发的国家层面洪水控制，发现学习机制能合理化托宾q、股权风险溢价和无风险利率对灾害事件的实证反应模式。与无学习的反比情景相比，适应性投资在学习环境下更具价值，且学习会通过不确定性解决与内生适应性响应的交互作用改变社会碳成本的预测。本文属于经济理论的应用建模，方法学创新程度有限，但为气候适应政策提供了结构化的定量分析框架。
- **关键技术**: `dynamic equilibrium model`, `Bayesian learning`, `optimal adaptation policy`, `social cost of carbon`
- **为什么对您有用**: 本文属于经济理论方向的应用建模，与您的secondary interest（经济理论中的模型与因果推断）直接相关。虽然模型本身不涉及您武器库中的高阶U统计量或半参效率理论，但文中关于学习与适应性响应的交互机制、以及资本税与碳税联合优化的结构，可作为您未来在气候经济学中应用因果推断（如IV或DML）的实证设定参考。本文作为经济理论入门读物清晰易懂，但核心机器（动态随机一般均衡与贝叶斯学习）不在您当前武器库中，属于暂不可做方向，仅建议作为背景阅读。

### 8. [10.3982/ecta20206](https://doi.org/10.3982/ecta20206) — Monitoring versus Discounting in Repeated Games
- **作者**: Takuo Sugaya, Alexander Wolitzky
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 5 · pp 1727-1761
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究重复博弈中贴现与监测精度如何共同决定合作可行性。在非完美监测（公开或私人）设定下，作者推导出一个关于玩家激励强度的简单上界，该上界是贴现因子、监测精度和路径上支付方差的函数。在低贴现与低监测精度的双重极限下，该界是紧的，并由此建立了一个公开监测的民间定理，允许贴现因子与监测结构同时变化。主要技术工具包括动态规划、信息论不等式和鞅收敛定理。理论结果揭示了贴现与监测之间的替代关系：当监测精度足够高时，即使贴现因子接近1，合作仍可维持；反之亦然。对您而言，本文是经济理论中关于激励与信息结构的基础性工作，其分析框架（如用信息论界刻画激励可行性）可能为因果推断中关于未观测混杂与工具变量强度的理论提供类比思路。
- **关键技术**: `dynamic programming`, `information-theoretic bounds`, `martingale convergence`, `folk theorem`, `imperfect monitoring`
- **为什么对您有用**: 本文属于经济理论方向，是您的次要兴趣之一。它提供了一个清晰的激励可行性边界，其分析思路（用信息论不等式刻画监测精度与贴现的权衡）与因果推断中工具变量强度与识别边界的研究有方法论上的类比性。作为入门读物，本文对非博弈论背景的统计学者较为友好，但需要一定的动态规划基础。您的武器库中的非参数统计和最小最大界工具可用于理解其紧性论证，但核心博弈论设定（如完美公共监测、民间定理）不在您的技术栈中，因此属于暂不可做方向，但值得花时间阅读全文以获取跨领域灵感。

### 9. [10.3982/ecta21090](https://doi.org/10.3982/ecta21090) — Infinite Debt Rollover in Stochastic Economies
- **作者**: Narayana R. Kocherlakota
- **期刊/来源**: Econometrica
- **机构**: University of Rochester
- **分类**: vol 91 · issue 5 · pp 1629-1658
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究随机经济环境中无限债务展期（庞氏骗局）的可持续性条件。核心问题是：当利率/增长率随机时，经典的“r vs. g”比较准则应如何修正？作者证明，相关比较应使用无限期零息债券的长期收益率 r_long，而非短期利率的期望。关键理论结果是：r_long 低于短期利率的风险中性期望（当短期利率可变时），且当短期利率高度持久时，r_long 接近其最小实现值。方法上，论文构建了异质性代理人动态随机一般均衡（DSGE）模型，并推导出公共债务泡沫存在的更弱充分条件。实证部分通过数值例子展示了这些理论结果如何放宽传统财政可持续性条件。对您而言，这是一篇经济理论论文，属于您的次要兴趣领域，其核心是理论建模而非统计方法创新，但其中关于随机过程长期收益率与短期利率关系的分析，可能对理解时间序列中的持久性与极值行为有启发。
- **关键技术**: `stochastic discount factor`, `infinite-maturity bond yield`, `r vs. g comparison`, `heterogeneous agent DSGE`, `public debt bubble`
- **为什么对您有用**: 本文属于经济理论（secondary interest），核心是理论建模而非统计方法。作为入门读物，它清晰地阐述了随机环境中债务可持续性的经济直觉和理论结果，但未涉及您武器库中的具体统计工具（如高维、U-统计、因果推断）。武器库中的 minimax bounds 或高维渐近理论在此无直接应用口子。因此，本文暂不可做——核心机器（随机增长模型、资产定价理论）不在您的武器库中，但可作为了解经济理论中一个经典问题的背景阅读。

### 10. [10.3982/ecta20157](https://doi.org/10.3982/ecta20157) · [arXiv](https://arxiv.org/abs/2309.00214) — Regret‐Minimizing Project Choice
- **作者**: Yingni Guo, Eran Shmaya
- **期刊/来源**: Econometrica
- **分类**: vol 91 · issue 5 · pp 1567-1593
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究一个委托-代理问题：代理人观察到一组可行项目，并向委托人提议其中一部分（不必全部），委托人从提议集中选择至多一个项目。目标是设计一个机制，最小化委托人在最坏情况下的遗憾（regret）。文章比较了两种环境：单项目环境（代理人只能提议一个项目）和多项目环境（代理人可提议多个项目）。在两种环境中，若代理人提议一个项目，当委托人的收益足够高时该项目被确定选中；否则，选中概率随代理人收益增加而降低。在多项目环境中，代理人提议多个项目的收益等于他单独提议每个项目的最大收益。多项目环境通过提供比拒绝更好的备选方案，并更有效地向代理人传递这一收益，从而优于单项目环境。本文是经济理论中的机制设计研究，对您作为统计学研究者而言，可作为了解经济学中worst-case regret和机制设计思路的入门读物。
- **关键技术**: `worst-case regret minimization`, `mechanism design`, `single-project vs. multiproject environment`, `fallback options`
- **为什么对您有用**: 本文属于经济理论（secondary interest），可作为gateway reading了解经济学中worst-case regret的机制设计框架。武器库中'identification theory in causal inference'和'minimax bounds for estimation problems'的思维可类比本文的minimax regret思路，但核心机器（机制设计、博弈论）不在武器库中，属于暂不可做方向。本文适合作为拓宽视野的阅读，不值得投入全文时间。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

