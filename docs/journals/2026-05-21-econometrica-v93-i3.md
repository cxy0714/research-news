# Econometrica — Vol 93  Issue 3  ·  2026-05-21

- 共 10 篇 · Econometrica

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.3982/ecta21075](https://doi.org/10.3982/ecta21075) — Risk and Optimal Policies in Bandit Experiments
- **作者**: Karun Adusumilli
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 1003-1029
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在局部渐近框架下对 bandit 实验进行决策理论分析，目标是在参数和非参数奖励分布下刻画渐近 Bayes 和 minimax 风险。利用扩散过程和 limit of experiments 方法，证明正态奖励下的最小 Bayes 风险可由二阶偏微分方程（PDE）刻画，且该 PDE 刻画在非参数设定下渐近成立。该方法识别出渐近充分的统计量，实现了状态空间的降维。PDE 的数值求解通过稀疏矩阵算法或 Monte Carlo 方法高效完成。数值解导出的最优 Bayes/minimax 策略显著优于 Thompson sampling（后者风险常为前者的两倍）。对您有用：该文将 limit of experiments 与非参数理论结合推导 minimax 风险界的方法，对您在效率理论（minimax 风险/半参数界）和统计计算（PDE 数值解法）方面的兴趣有直接借鉴意义。
- **关键技术**: `limit of experiments`, `diffusion approximation`, `minimax risk`, `partial differential equation (PDE)`, `sparse matrix computation`, `nonparametric rewards`
- **为什么对您有用**: 论文将 Le Cam 局部渐近与扩散近似结合推导非参数下的 minimax 风险界，并利用稀疏矩阵求解 PDE，直接契合您在效率理论（minimax/半参数界）和统计计算方面的核心兴趣，且其决策理论视角对序贯因果推断（如纵向/自适应实验）有迁移价值。

## 经济理论 / 应用  *(econ_theory, 9 篇)*

### 1. [10.3982/ecta21319](https://doi.org/10.3982/ecta21319) — Making Subsidies Work: Rules versus Discretion
- **作者**: Federico Cingano, Filippo Palomba, Paolo Pinotti, Enrico Rettore
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 747-778
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文研究公共投资补贴的就业效应，设定为基于客观评分与地方政客自由裁量权混合排序的补贴分配机制，利用资金配给作为回归断点设计（RDD）进行因果识别。核心方法为利用 RDD 估计处理效应的异质性，刻画边际内企业在客观规则偏好与政治偏好下的成本效益差异，并进行反事实分配下的补贴效率估计。技术层面，文章将标准 RDD 扩展至多维排序规则下的异质性处理效应分解与反事实政策模拟。实证结果显示，政客偏好的企业虽带来更高就业增长，但单岗成本也更高；若仅依赖客观规则，单岗成本可降低 11%，而仅依赖自由裁量则增加 42%。对您有用之处在于，这是一个在经济学顶级期刊上应用 RDD 进行异质性因果推断与反事实政策模拟的范例，展示了如何将标准因果识别设计扩展至政策优化评估，契合您对经济理论中应用因果推断的关注。
- **关键技术**: `Regression Discontinuity Design`, `heterogeneous treatment effects`, `counterfactual policy evaluation`, `cost-effectiveness analysis`
- **为什么对您有用**: 属于您 secondary interest 中的经济理论应用因果推断；展示了如何利用 RDD 从局部平均处理效应扩展到异质性效应与反事实政策比较，对从事应用因果推断（特别是政策评估与异质性分析）的方法论迁移有参考价值。

### 2. [10.3982/ecta21394](https://doi.org/10.3982/ecta21394) — Location Sorting and Endogenous Amenities: Evidence From Amsterdam
- **作者**: Milena Almagro, Tomás Domínguez-Iino
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 1031-1071
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文在城市一般均衡框架下研究内生便利设施对居民福利分配的影响，构建了包含异质性家庭的动态居住选择模型，其中便利设施是非贸易品市场的均衡结果。估计策略利用阿姆斯特丹游客空间分布的变异作为需求冲击（类工具变量），以解决便利设施供给的内生性问题。实证发现居民对便利设施的偏好和便利设施供给对需求变化的反应均存在显著异质性。这种双向异质性决定了社区横向差异化、居住分选和不平等程度。反事实分析表明，大众旅游的分配效应取决于该异质性：年轻居民因偏好与游客相近而获得便利设施补偿，年长居民则因租金上涨和便利设施错配而遭受更大损失。对您而言，该文展示了在经济学应用中如何利用外生需求冲击（IV策略）处理一般均衡模型中的内生性，其结构估计框架和微观数据处理对经济因果推断应用有参考价值。
- **关键技术**: `dynamic discrete choice model`, `structural estimation`, `instrumental variable (demand shifter)`, `spatial general equilibrium`, `residential sorting`
- **为什么对您有用**: 契合您在经济理论（应用、数据集、因果推断）上的次级兴趣；文中利用游客分布作为需求冲击（类IV策略）解决便利设施内生性的识别思路，以及丰富的荷兰微观面板数据，对做应用因果推断和结构模型的研究有直接借鉴意义。

### 3. [10.3982/ecta22303](https://doi.org/10.3982/ecta22303) — The Cost of Consumer Collateral: Evidence From Bunching
- **作者**: Benjamin L. Collier, Cameron M. Ellis, Benjamin J. Keys
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 779-819
- 相关性 3/10 · novelty: `application`
- **摘要**: 在美国联邦灾难贷款项目的行政数据中，研究抵押要求对消费者借贷行为的因果影响，核心设定是贷款额超过阈值则必须抵押房产。采用 bunching 估计方法（类似 kink/notch 设计的半参数识别），发现中位借款人愿意放弃40%的贷款额度以避免抵押。利用阈值的时间变异作为因果识别策略，估计出抵押要求因果地降低了36%的违约率。进一步通过结构模型估计家庭对住房的依恋价值（中位数$11,000），量化了借贷双方对抵押物估值的15%楔子。结果解释了抵押贷款市场的高违约成本，并证实了抵押在减少消费信贷道德风险中的作用。对您有用：作为顶刊 applied causal work，它展示了 bunching 识别与结构估计的规范结合，直接契合您在 economic theory 与因果推断应用上的兴趣，其行政数据与模型设定也具借鉴价值。
- **关键技术**: `bunching estimation`, `quasi-experimental design`, `structural estimation`, `causal identification via time variation`, `moral hazard model`
- **为什么对您有用**: 直接契合您在 economic theory (applied causal work) 方向的次级兴趣；展示了 bunching 这一准实验识别策略与结构模型的结合，对理解抵押与道德风险的因果机制有参考价值，且其联邦灾难贷款的行政数据结构具有借鉴意义。

### 4. [10.3982/ecta22351](https://doi.org/10.3982/ecta22351) — Adaptive Maximization of Social Welfare
- **作者**: Nicolò Cesa-Bianchi, Roberto Colomboni, Maximilian Kasy
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 1073-1104
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究在重复政策选择中最大化社会福利的问题，目标estimand为私人效用与公共收入的加权和，其中私人效用不可直接观测而需间接推断。在对抗性设定下，作者推导了遗憾下界，并为 Exp3 算法变体证明了匹配的上界，其累积遗憾率为 T^{2/3}，表明该问题比有限策略集的标准多臂老虎机（T^{1/2}）更难且算法达到最优率。在随机设定且社会福利为凹函数的条件下，通过二分搜索（dyadic search）算法在连续策略集上实现了 T^{1/2} 的遗憾率。理论结果应用于非线性所得税设计，并对比了垄断定价与双边贸易定价的难度。对您而言，虽然核心是bandit理论，但其对不可观测效用的间接推断设定及政策优化算法，可为经济理论中的因果与决策问题提供在线学习的视角。
- **关键技术**: `multi-armed bandits`, `Exp3 algorithm`, `regret lower bounds`, `dyadic search`, `adversarial bandits`
- **为什么对您有用**: 属于您的 secondary interest（经济理论），展示了在线学习与bandit算法在税收与福利政策设计中的理论应用，其不可观测效用的推断设定对经济因果推断有一定启发。

### 5. [10.3982/ecta20404](https://doi.org/10.3982/ecta20404) — Insurance and Inequality With Persistent Private Information
- **作者**: Alexander W. Bloedel, R. Vijay Krishna, Oksana Leukhina
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 821-857
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究具有持续私人信息（类型服从遍历有限状态马尔可夫链）的经济体中，最优保险契约对长期福利和不平等的影响。证明最优契约必然导致“贫困化”（immiseration），即代理人的消费和效用无界递减。在类型存在正自相关时，契约还会后置高能激励，使得代理人效用对其报告的敏感度无界递增。分析采用了针对持续类型的递归契约方法，并允许全局激励约束起作用。数值结果表明，持续性导致更快的贫困化、更高的不平等以及新的短期扭曲。该文属于纯微观机制设计理论，对因果推断或半参数效率的方法论借鉴有限，但可作为结构计量经济学中动态委托代理模型的极端理论案例参考。
- **关键技术**: `recursive contract`, `dynamic mechanism design`, `Markov private information`, `global incentive constraints`, `numerical dynamic programming`
- **为什么对您有用**: 属于您的 secondary interest（经济理论），但偏向纯微观机制设计而非应用因果或数据集；若您关注结构计量中的动态委托代理模型或马尔可夫类型下的递归数值方法，可作理论背景阅读，否则方法论相关性较弱。

### 6. [10.3982/ecta21343](https://doi.org/10.3982/ecta21343) — Auctioning Control and Cash‐Flow Rights Separately
- **作者**: Tingjun Liu, Dan Bernhardt
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 859-889
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 在经典拍卖设定下，买方拥有关于项目预期收益的私有信号，且项目收益对控制者的信号比非控制者更敏感。本文证明卖方可通过分离控制权与现金流权（如最高出价者获现金流、次高者获控制权）来提升收入。分离机制的核心在于降低竞标者的信息租金，因为租金取决于私有信息对所获现金流价值的重要性。由于项目收益对控制者信号最敏感，将现金流分配给他人可削弱竞标者的信息优势。当竞标者信号接近时，分割权利能有效增加卖方收入。本文主要贡献是分离权利的最优拍卖机制设计理论；对您而言，若关注经济理论中的机制设计与信息不对称模型，本文提供了分离权利以降低信息租金的理论视角，但缺乏实证数据与统计推断方法。
- **关键技术**: `mechanism design`, `auction theory`, `information rent`, `optimal auction`, `private signals`
- **为什么对您有用**: 属于经济理论（机制设计）范畴，但纯理论推导无数据及因果推断方法，对您核心的统计推断与实证因果兴趣直接收益较低。

### 7. [10.3982/ecta20411](https://doi.org/10.3982/ecta20411) — Soaking up the Sun: Battery Investment, Renewable Energy, and Market Equilibrium
- **作者**: R. Andrew Butters, Jackson Dorsey, Gautam Gowrisankaran
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 891-927
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在加州电力市场设定下，构建并估计了一个评估大规模电池储能投资与可再生能源互补效应的市场均衡模型。核心方法为结构计量模型，通过求解动态投资均衡来量化电池储能对批发电力价格及各类发电商收入的反事实影响。研究发现储能对电价的降低存在边际递减效应（前5000 MWh降5.6%，25000-50000 MWh仅降2.6%），且大规模储能会削减传统与可再生能源的收益。在无补贴情况下，电池采用率至2030年几乎为零；而美国《通胀削减法案》中30%的资本成本补贴效果与加州储能强制令相当。对您而言，该文展示了结构均衡模型在评估政策干预反事实效果中的应用范式，属于经济学中因果与均衡分析结合的典型实例，但缺乏底层统计方法学创新。
- **关键技术**: `structural equilibrium model`, `counterfactual policy evaluation`, `dynamic investment model`, `market equilibrium estimation`
- **为什么对您有用**: 属于经济学次级兴趣中的经济理论与应用因果工作，展示了如何用结构模型评估政策干预（补贴/强制令）的反事实均衡效应，对理解电力市场中的因果与均衡分析范式有参考价值，但方法学创新有限。

### 8. [10.3982/ecta18838](https://doi.org/10.3982/ecta18838) — Personalized Pricing and the Value of Time: Evidence From Auctioned Cab Rides
- **作者**: Nicholas Buchholz, Laura Doval, Jakub Kastl, Filip Matejka, Tobias Salz
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 929-958
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在网约车拍卖平台设定下，利用消费者在价格与等待时间之间的离散选择面板数据，识别并估计消费者时间价值（value of time）的异质性。方法上构建了包含价格与等待时间的离散选择需求模型，通过反事实模拟评估个性化定价的福利效应。核心发现为：考虑司机最优反应后，个性化定价使消费者剩余降低2.5%、总剩余增加5.2%，且司机与平台均获益；若仅基于司机等待时间而非消费者数据定价，平台仍可攫取大部分利润并惠及消费者。该研究展示了结构计量模型在评估平台定价策略与福利分配中的应用。对您而言，此文提供了网约车拍卖机制下的丰富数据结构与反事实分析范式，可作为经济理论中应用因果与结构模型结合的案例参考，但方法论上未涉及前沿半参数或高维推断。
- **关键技术**: `discrete choice demand estimation`, `structural econometric model`, `counterfactual welfare analysis`, `personalized pricing`, `value of time recovery`
- **为什么对您有用**: 属于 secondary interest 中的经济理论与应用因果工作，提供了平台经济中离散选择与反事实福利分析的真实数据结构范例，但方法学上偏传统结构计量，对前沿半参数/效率理论的启发有限。

### 9. [10.3982/ecta21182](https://doi.org/10.3982/ecta21182) — Quality Disclosure and Regulation: Scoring Design in Medicare Advantage
- **作者**: Benjamin Vatter
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 3 · pp 959-1001
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究信息不对称下质量评分的均衡效应与最优设计，以 Medicare Advantage 市场为设定。作者构建结构模型发现消费者信息有限且质量供给低效，简单的评分设计可通过设定阈值规制寡头质量供给，而非仅提供信息。均衡效应打破了“信息越多越好”的直觉，福利增益过半来自质量规制而非信息揭示；二元认证即可实现最优评分 98% 的福利。主要结果表明粗粒度评分因锚定企业生产阈值而有效。对您而言，该文是经济理论中机制设计与结构估计的应用范例，展示了如何量化政策干预的均衡与福利效应。
- **关键技术**: `structural equilibrium model`, `welfare analysis`, `mechanism design`, `asymmetric information`, `counterfactual simulation`
- **为什么对您有用**: 契合您对经济理论（模型与应用因果）的次级兴趣；该文展示了如何通过结构模型量化信息干预的均衡与福利效应，其机制设计思路对理解政策干预的因果作用有参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

