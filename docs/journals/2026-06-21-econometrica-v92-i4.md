# Econometrica — Vol 92  Issue 4  ·  2026-06-21

- 共 11 篇 · Econometrica
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 16 篇）：10.3982/ecta924forth

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文呈现出三条清晰的方法与主题主线：一是因果识别与政策评估，聚焦于随机实验与结构模型的结合以破除内生性或评估均衡效应，包含“Micro Data”、“DRC”、“Pollution”、“Congestion Pricing”、“Searching for Approval”与“Labor Law”六篇；二是经济理论与均衡稳健性，探讨非参数刻画、博弈解概念及社会学习条件，包含“Monotone Statistics”、“Sequentially Stable”、“Beyond Unbounded Beliefs”与“Public Debt”四篇；三是测量与识别框架，主张以更丰富的测量指标放松强识别假设，由“Presidential Address”独立支撑。

在因果识别与政策评估主线中，本期明显在推进“实验+结构”的混合范式以处理复杂政策与市场均衡问题。“Congestion Pricing”与“Searching for Approval”均先通过随机化或微观数据识别关键行为参数，再代入均衡模型做反事实模拟，前者揭示拥堵外部性线性特征限制了福利增益，后者证明审批筛选导致内生逆向选择与搜索成本估计偏误。同时，针对不可观测混淆的处理呈现两种切法：“Labor Law”与“DRC”依靠多维度随机化（干预、执法信件、官员分配）直接剥离执法能力与税率的交互效应；“Micro Data”与“Pollution”则利用数据微观结构破除混淆——前者借消费者异质性面板结构替代传统BLP工具变量需求，后者用日度面板固定效应吸收 locality 内时间变异。此外，“DRC”与“Labor Law”共同印证了外部执法/税率与内部管理/遵从能力的互补性。

经济理论主线中，本期集中推进了非期望效用与均衡稳健性的公理化刻画。“Monotone Statistics”在随机占优与可加性公理下，将统计量刻画为某函数期望的单调变换，把确定性时间偏好拓展至时间彩票；“Beyond Unbounded Beliefs”提出“excludability”概念，以偏好与信息的联合性质替代传统的无界信念假设，给出社会学习收敛的充分条件；“Sequentially Stable”则在扩展式博弈中定义微小行为扰动下的稳健结果，统一了正向归纳与Kohlberg-Mertens稳定集等经典性质。这三篇均致力于在更弱的公理假设下，为风险、学习与博弈行为提供更具一般性的解概念与识别条件。

对于关注因果推断与半参数效率的研究者，“Micro Data”利用微观面板结构放松工具变量需求的非参数识别策略，以及“Pollution”基于日度面板固定效应的异质性因果响应估计，最贴合因果与半参数方向，适合优先看；对于关注高维混淆控制与实验设计者，“DRC”多维随机化剥离执法能力与税率交互的设计，以及“Labor Law”对外部干预与内部管理互补性的识别，提供了直接的参考范式。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.3982/ecta19408](https://doi.org/10.3982/ecta19408) — Multinational Enforcement of Labor Law: Experimental Evidence on Strengthening Occupational Safety and Health Committees
- **作者**: Laura Boudreau
- **期刊/来源**: Econometrica
- **机构**: National Bureau of Economic Research · Centre for Economic Policy Research · Columbia University
- **分类**: vol 92 · issue 4 · pp 1269-1308
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文通过一个大型田间实验，估计职业安全与健康委员会（OSH 委员会）对工作场所安全与工人福利的因果效应。研究者与 29 家跨国服装买家合作，在孟加拉国 84 家供应商工厂中随机强制执行当地 OSH 委员会法律。实验干预提高了法律合规率，且对安全客观指标产生微弱正向影响，并未损害工人工资、就业或工厂劳动生产力。异质性分析显示，管理实践较好的工厂改善更显著，而管理较差的工厂不仅未改进，工人满意度反而下降，提示外部执法与内部能力之间存在互补性。该研究为劳动法规执行的因果效应提供了宝贵的实验证据，其随机化设计与合规测量策略对应用因果推断研究者具有直接参考价值。
- **关键技术**: `randomized field experiment`, `intention-to-treat (ITT) estimation`, `compliance analysis`, `heterogeneous treatment effects`, `occupational safety and health (OSH) committees`
- **为什么对您有用**: 本文是因果推断在劳动经济学领域的高质量应用，特别适合作为入门读物，了解如何在真实政策环境中设计、实施和分析大规模随机实验。您武器库中的非参数统计、因果推断估计理论以及软件开发能力足以理解甚至复现其分析流程，并为后续在流行病学或经济学中的类似实验设计提供模板。值得花时间全文阅读，以汲取实际田野实验的设计细节（如随机化层级、合规测量、异质性分析）和研究写作范式。

## 经济理论 / 应用  *(econ_theory, 10 篇)*

### 1. [10.3982/ecta20731](https://doi.org/10.3982/ecta20731) · [arXiv](https://arxiv.org/abs/2204.06637) — Nonparametric Identification of Differentiated Products Demand Using Micro Data
- **作者**: Steven T. Berry, Philip A. Haile
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 4 · pp 1135-1162
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究差异化产品需求函数的非参数识别问题，在消费者层面微观数据（消费者特征与选择）可用时，处理产品/市场层面不可观测变量导致的经济内生性。模型嵌套了丰富的消费者异质性和市场层面的不可观测因素，标准方法需要大量工具变量（价格和数量的IV）。作者发现微观数据提供的面板结构可以放松对工具变量的需求：即使在非价格产品特征内生且未被工具化的情形下，仍可识别需求弹性等关键参数。核心方法基于非参数识别策略，利用消费者选择的异质性来打破常见的多维不可观测变量混淆。与经典BLP方法相比，本文减少了对外部IV数量和质量的依赖，且不要求对替代模式施加参数假设。主要理论结果给出了识别条件的充分性和部分必要条件，并对实证应用中如何选择微观数据变量、检验识别假设提供了指导。本文所讨论的识别策略在经济学因果推断（IV设计、内生性处理）中有直接应用，您的identification theory知识可帮助理解其假设结构并评估其在其他领域的可迁移性。
- **关键技术**: `nonparametric identification`, `differentiated products demand`, `micro data panel structure`, `endogeneity without instruments`, `BLP-type models`, `consumer heterogeneity`
- **为什么对您有用**: 本文属于经济理论中的应用因果推断（IV非参数识别），与您的二级兴趣“经济理论（应用、模型、因果工作）”高度匹配，且直接涉及您初级兴趣中的IV和identification问题。您的反应：您对identification theory in causal inference moderately_familiar，可以深入理解本文在经济学框架下的识别策略，并对比其与外生性假设的关系；但完整评价其估计可行性需要熟悉BLP模型和消费者选择数据的具体结构，这不在您当前技术武器库中——因此暂不可做，但作为交叉领域阅读可极大拓展您对IV设计的理解，并可能在未来的因果推断研究（例如利用面板结构放松IV假设）中受到启发。

### 2. [10.3982/ecta19959](https://doi.org/10.3982/ecta19959) — The State Capacity Ceiling on Tax Rates: Evidence From Randomized Tax Abatements in the DRC
- **作者**: Augustin Bergeron, Gabriel Tourek, Jonathan L. Weigel
- **期刊/来源**: Econometrica
- **机构**: University of Southern California · University of Pittsburgh · University of California, Berkeley
- **分类**: vol 92 · issue 4 · pp 1163-1193
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究税率与税收执法如何共同影响发展中国家的财政能力。作者在刚果民主共和国开展了一项大规模随机实验，将38028名房产所有者随机分配到现行税率或约三分之一的减税组。实验发现，现行税率已高于政府收入最大化的税率（RMTR），降低税率反而可以通过提高纳税遵从度来增加政府财政收入。进一步利用随机执法信件和税务官员随机分配两种执法变异，作者发现执法力度的增强会提高RMTR：在催缴信中增加执法表述或替换执法能力最差的四分之一税务官员，可使RMTR提高约40%。因此，税率与执法是互补的杠杆，联合优化比独立优化可多带来10%的财政收入增长。本文提供了实验证据，证明在低收入国家，政府执法能力的不足构成了对RMTR的硬性上限。对您而言，这是一篇出色的应用因果推断论文，展示了如何通过田野随机实验识别政策参数，并检验了经济理论中的互补性假设。
- **关键技术**: `randomized controlled trial`, `tax enforcement experiment`, `revenue-maximizing tax rate`, `complementarity of tax rate and enforcement`, `causal inference in development economics`
- **为什么对您有用**: 本文属于您的次级兴趣——经济理论中的应用因果推断工作，直接涉及发展经济学中的税务政策实验。您熟练的causal inference estimation理论可以立即用于审视其识别策略和估计方法（例如,ATE估计的假设、随机化推断的合理性）。同时，该文的实验设计（随机税率减免、执法强度的随机变异）可作为您学习经济领域田野实验因果推断的优质案例，具备**立即可做**的阅读与批判评估价值。

### 3. [10.3982/ecta20484](https://doi.org/10.3982/ecta20484) — The Unequal Effects of Pollution on Labor Supply
- **作者**: Bridget Hoffmann, Juan Pablo Rud
- **期刊/来源**: Econometrica
- **机构**: Inter-American Development Bank · Institute for Fiscal Studies · Royal Holloway University of London · IZA - Institute of Labor Economics
- **分类**: vol 92 · issue 4 · pp 1063-1096
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文利用墨西哥城各 locality 层面每日 PM2.5 高频数据，研究空气污染对同日劳动供给的因果效应，并考察低收入与高收入工人的异质性回应。识别策略依靠日度面板固定效应，利用 locality 内污染的时间变异，估计污染浓度与劳动小时的非线性关系。主要发现：在极端高污染日（PM2.5 极高），平均工人减少约 7.5% 的工作时长，且存在部分补偿行为——高污染后一天工作小时增加。低收入工人减少的劳动供给显著低于高收入工人，体现了污染的健康-经济不平等效应，且这一差异不能完全由工作灵活性或性别等维度解释。论文为污染导致的规避行为提供了间接证据。该文是经济学应用因果推断的扎实范例，其数据集（高频污染与劳动供给面板）和分析模式（非线性异质性、动态补偿）对有类似数据的研究者极具参考价值。
- **关键技术**: `panel fixed effects`, `high-frequency locality-level PM2.5 data`, `nonlinear dose-response estimation`, `heterogeneous treatment effects by income`, `compensatory labor supply dynamics`
- **为什么对您有用**: 该文直接对应 secondary interest 中的 'economic theory (applied causal work)'，是环境污染与劳动市场交叉的实证因果研究，可作为理解经济学应用因果识别框架的入门读物。武器库中的非参数统计可以用于灵活估计非线性的污染-劳动供给曲线，而因果推断理论中的敏感性分析可进一步检验未观测混杂的稳健性。结论：本文值得花时间阅读全文，以获取实证分析的设计思路和数据处理模式。

### 4. [10.3982/ecta19967](https://doi.org/10.3982/ecta19967) — Monotone Additive Statistics
- **作者**: Xiaosheng Mu, Luciano Pomatto, Philipp Strack, Omer Tamuz
- **期刊/来源**: Econometrica
- **机构**: Princeton University · California Institute of Technology · Yale University
- **分类**: vol 92 · issue 4 · pp 995-1031
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文在随机占优单调性（monotone with respect to stochastic dominance）和关于独立随机变量之和的可加性（additive for sums of independent random variables）这两个公理下，完整刻画了所有满足条件的统计量，证明它们必然是某个函数期望的单调变换。这一刻画将期望视为特例，并推广到一大类非线性的统计量。作者将结果应用于时间偏好：把Fishburn和Rubinstein (1982)的确定性时间偏好拓展到时间彩票（time lotteries），为时间维度上的风险态度提供了新视角。同时，文中提出了一类非期望效用偏好（non-expected utility preferences），满足背景风险不变性（background risk invariance）和betweenness性质，且能灵活刻画混合风险态度（同时包含风险寻求与风险规避）。论文的方法是纯粹的公理化（axiomatic）和数学推导，没有引入统计估计或计算。对您而言，这是经济理论中关于统计量基本性质的纯理论工作，与您兴趣中的经济理论子方向直接对应，且可加性结构与您熟悉的高阶U统计量存在潜在概念联系，适合作为进入决策理论的gateway阅读。
- **关键技术**: `Monotonicity with respect to stochastic dominance`, `Additivity for sums of independent random variables`, `Axiomatic characterization`, `Time lotteries`, `Betweenness`, `Background risk invariance`
- **为什么对您有用**: 直接连接您兴趣中的经济理论（决策模型）子方向，论文核心概念“可加统计量”与您非常熟悉的高阶U统计量（treewidth/tensor contraction）在结构上有潜在可比性——可加性天然适合用张量网络表示，可能启发您分析此类统计量的计算复杂度。但因为本文是纯公理化工作，您武器库中的核心工具（如minimax bounds、U统计量理论）目前不能直接攻克其问题，属于暂不可做范畴，需要先补充经济决策理论背景，但作为跨领域gateway阅读极有价值。

### 5. [10.3982/ecta18422](https://doi.org/10.3982/ecta18422) — Peak‐Hour Road Congestion Pricing: Experimental Evidence and Equilibrium Implications
- **作者**: Gabriel Kreindler
- **期刊/来源**: Econometrica
- **机构**: Harvard University
- **分类**: vol 92 · issue 4 · pp 1233-1268
- 相关性 6/10 · novelty: `application`
- **摘要**: 在班加罗尔高峰时段交通拥堵均衡设定下，研究目标是通过内生拥堵机制评估最优拥堵收费的通勤者福利增益与出行时间缩减。作者基于出发时间选择模型设计随机化拥堵定价实地实验，利用 GPS 数据估计出行偏好参数，发现通勤者具有中等日程刚性但较高的时间价值。核心机制在于将实验估计的结构参数代入均衡模型，结合交通密度对延误的线性且中等影响进行政策模拟，揭示最优收费仅带来小幅福利改善。主要结论表明拥堵外部性的形状（线性而非急剧非线性）是福利增益有限的关键驱动因素，这对城市交通政策设计有直接启示。对您可能有用：本文展示了如何将结构模型与实地实验结合做政策模拟，是经济理论中因果推断与均衡分析交叉的典型应用。
- **关键技术**: `departure time choice model`, `field experiment with congestion pricing`, `GPS-based travel measurement`, `equilibrium policy simulation`, `congestion externality estimation`
- **为什么对您有用**: 本文属于经济理论（应用因果工作）方向，展示了如何用随机化实地实验估计结构参数并做内生拥堵均衡的政策模拟，对您关注的经济理论中因果推断与模型结合有参考价值。您的武器库中 identification theory in causal inference 与 M-estimation theory 可直接用于审视其结构模型识别与参数估计逻辑。**立即可做**：用 very_familiar 的因果推断估计理论审视其实验设计识别策略与估计效率，判断其政策模拟中参数不确定性是否被合理传播。

### 6. [10.3982/ecta21528](https://doi.org/10.3982/ecta21528) — Presidential Address: Economics and Measurement: New Measures to Model Decision Making
- **作者**: Ingvild Almås, Orazio Attanasio, Pamela Jervis
- **期刊/来源**: Econometrica
- **机构**: Peterson Institute for International Economics · Stockholm University · Norwegian School of Economics · Yale University · Institute for Fiscal Studies · University of Chile
- **分类**: vol 92 · issue 4 · pp 947-978
- 相关性 5/10 · novelty: `survey`
- **摘要**: 这篇 Presidential Address 指出，经济学实证工作通常只依赖狭窄的测量指标，迫使研究者使用很强的识别假设。文章主张测量应与经济模型设计互动，采用更灵活、更广泛的测量工具以放松假设。作者用一个父母行为模型（parental investment model）的 pilot 数据作为例证，展示了如何结合新型测量指标与行为模型来估计更丰富的参数。本文没有提出新的 estimator 或具体方法，而是提供一个方法论框架，强调测量不是理论的替代而是补充。对您而言，这是一篇理解经济学中测量与识别关系的好入门读物，属于经济理论（secondary interest）范畴。
- **关键技术**: `measurement design`, `identification under weak assumptions`, `parental investment model`, `pilot data collection`
- **为什么对您有用**: 本文属于经济理论子方向（经济实证中的测量与识别），是 Presidential Address，入门友好。您的武器库中的 'identification theory in causal inference' 可直接理解本文讨论的识别假设放松。作为立场文章，值得全文阅读，但无需立即动手跟进，可归为暂不可做。

### 7. [10.3982/ecta18554](https://doi.org/10.3982/ecta18554) — Searching for Approval
- **作者**: Sumit Agarwal, John Grigsby, Ali Hortaçsu, Gregor Matvos, Amit Seru, Vincent Yao
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 4 · pp 1195-1231
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究信贷市场中借款人搜索行为与贷款审批之间的互动机制。风险借款人会内化申请被拒的概率，从而表现出类似高搜索成本的行为，使得传统上以“多付”衡量消费者不成熟的做法产生偏差。作者构建了一个包含搜索与审批的均衡模型，推导出三个反直觉的预测：搜索过程导致内生逆向选择、搜索与利率/违约/批准率之间可能出现非单调关系、仅基于交易价格估计的搜索成本有偏。利用美国抵押贷款借款人的微观搜索行为数据，作者通过结构估计支持了模型预测，发现贷款机构的筛选具有信息量且借款人的搜索成本显著。反事实分析表明，收紧贷款标准或基于歧视性审批都会显著提高均衡利率。本文是经济理论与实证应用的结合，对关注市场均衡与政策评估的经济学或因果推断研究者有参考价值。
- **关键技术**: `search-and-matching model`, `structural estimation`, `adverse selection in credit markets`, `counterfactual policy simulation`, `endogenous rejection probability`
- **为什么对您有用**: 本文连接 secondary interest 中的经济理论应用，特别是信贷市场中搜索与审批的互动如何产生内生选择偏差，可与因果推断中的选择偏倚问题类比。武器库中 very_familiar 的 estimation theory in causal inference 可用于理解其识别策略（如利用拒绝信息构造控制组），但核心的结构估计需要补充动态离散选择模型的知识，目前属于中期可做；本文作为高质量应用经济学论文，提供了真实数据集和清晰的模型—数据对照，值得作为跨领域入门阅读。

### 8. [10.3982/ecta21470](https://doi.org/10.3982/ecta21470) · [arXiv](https://arxiv.org/abs/2103.02754) — Beyond Unbounded Beliefs: How Preferences and Information Interplay in Social Learning
- **作者**: Navin Kartik, SangMok Lee, Tianhao Liu, Daniel Rappoport
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 4 · pp 1033-1062
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 在序贯社会学习（observational learning）模型中，研究社会最终能否通过观察他人行为学到真实状态或采取正确行动的 identification 问题。核心 estimand 是社会学习收敛到真值的条件，关键假设是提出的新概念“excludability”——偏好与信息的联合性质，要求单个 agent 能排除任何错误行动，而非必须识别正确行动。文章证明 excludability 是正确学习的充分条件，并构建两类满足该条件的偏好-信息组合：(i) 一维状态下的 single-crossing preferences 加 directionally unbounded beliefs；(ii) 多维状态下的 intermediate preferences 加 subexponential location-shift information。理论结果揭示多维状态下经典 unbounded beliefs 假设与常见信息结构（如正态信息）不兼容，而 excludability 提供了更弱且更合理的替代。对您可能有用：本文的 identification 分析为经济理论中的社会学习模型提供了新的弱假设框架。
- **关键技术**: `sequential observational learning`, `excludability condition`, `single-crossing preferences`, `directionally unbounded beliefs`, `intermediate preferences`, `subexponential location-shift information`
- **为什么对您有用**: 本文直接连接经济理论中的社会学习模型，其 identification 条件（excludability）的分析思路与因果推断中的 identification theory 有结构相似性——都在寻找 estimand 可识别的最弱假设组合。您可以用 very_familiar 的 identification theory 视角审视 excludability 是否可转化为因果推断中某种弱可识别性条件。follow-up 判断：**中期可做**——需先在 moderately_familiar 的 identification theory 上长肌肉，将经济模型中的偏好-信息结构映射到因果模型的 treatment-response 结构，才能判断该弱假设框架能否迁移到因果推断的 sensitivity analysis 或 partial identification 场景。

### 9. [10.3982/ecta20497](https://doi.org/10.3982/ecta20497) — The U.S. Public Debt Valuation Puzzle
- **作者**: Zhengyang Jiang, Hanno Lustig, Stijn Van Nieuwerburgh, Mindy Z. Xiaolan
- **期刊/来源**: Econometrica
- **机构**: Kellogg's (Canada) · Center for Economic and Policy Research · Columbia University · The University of Texas at Austin
- **分类**: vol 92 · issue 4 · pp 1309-1347
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究美国国债的定价问题，核心问题是政府债务的市场价值是否等于预期财政盈余的现值（政府预算约束）。作者利用美国长期财政数据，发现税收收入和政府支出的周期性与长期动态使得盈余要求权具有显著风险，而国债投资者似乎未能施加无套利限制。在现实资产定价模型中，这种风险导致债务市场价值与基本面价值（盈余现值）之间存在巨大差距，表明美国国债可能被高估。该研究使用了现值预算约束模型和资产定价框架，对财政盈余风险进行了量化。这是一篇经济理论与实证相结合的工作，展示了如何将财政政策与资产定价联系起来。对于研究者而言，这是经济理论应用的一个良好入门案例，可以帮助理解经济学中资产定价与财政风险的分析范式。
- **关键技术**: `asset pricing model`, `present-value budget constraint`, `no-arbitrage restriction`, `fiscal surplus risk`, `discount rate estimation`
- **为什么对您有用**: 本文属于次要兴趣（经济理论）的实证应用，展示了如何使用资产定价模型检验政府债务定价的合理性。研究者无需额外掌握复杂工具即可阅读该文，但武器库（因果推断、高维统计等）与此方向并不直接匹配。作为跨领域阅读可以拓宽视野，但无法直接迁移自身方法学技能。全文值得一读以了解经济学中的财政风险定价思路，但非核心兴趣。

### 10. [10.3982/ecta21402](https://doi.org/10.3982/ecta21402) — Sequentially Stable Outcomes
- **作者**: Francesc Dilmé
- **期刊/来源**: Econometrica
- **机构**: University of Bonn
- **分类**: vol 92 · issue 4 · pp 1097-1134
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在扩展式博弈框架下提出了“顺序稳定结果”（sequentially stable outcomes）的概念，用于刻画在微小行为扰动下仍能保持接近的均衡结果。定义要求：对于任意ε>0和任意足够小的行为扰动，存在相应的支付扰动和均衡，使得均衡结果与目标结果距离小于ε。该概念保证了所有有限博弈都存在顺序稳定结果，且此类结果一定是顺序均衡的结果。文章建立了与Kohlberg-Mertens稳定集、正向归纳、迭代严格优势以及同时行动不变性等经典性质的关系。在信号博弈中，当支付为一般位置时，顺序稳定结果通过所有标准选择准则，并与稳定集结果重合。本文为扩展式博弈的均衡稳健性提供了统一的理论框架，属于纯博弈论理论贡献。对您可能有用：可作为经济理论（博弈论）的背景阅读，帮助理解因果推断中策略互动均衡的稳定性基础，但无直接统计方法连接。
- **关键技术**: `Extensive-form games`, `Sequential equilibrium`, `Stable sets of equilibria`, `Forward induction`, `Iterated strict dominance`, `Invariance to simultaneous moves`
- **为什么对您有用**: 本文属于经济理论中的博弈论子方向，是均衡稳健性理论的重要进展，与研究者的二级兴趣“economic theory”直接匹配。但武器库中无直接可用的博弈论分析工具（如扩展式博弈的均衡计算、稳定集构造），目前属于暂不可做——缺少博弈论定制工具。研究者可将其作为经济理论背景储备，待未来需要引入策略稳健性概念时再深入。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

