# Econometrica — Vol 93  Issue 4  ·  2026-05-21

- 共 9 篇 · Econometrica

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.3982/ecta19739](https://doi.org/10.3982/ecta19739) — Selecting the Most Effective Nudge: Evidence From a Large‐Scale Experiment on Immunization
- **作者**: Abhijit Banerjee, Arun G. Chandrasekhar, Suresh Dalpath, Esther Duflo, John Floretta, Matthew O. Jackson et al.
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1183-1223
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在大规模因子设计实验设定下，本文研究如何从众多干预组合中筛选最优政策并修正选择偏差。提出treatment variant aggregation (TVA)方法，将效果无显著差异的政策变体合并，并剪枝无效变体，从而压缩干预空间。对合并后的变体进行一致估计，并针对“赢家诅咒”（winner's curse）进行修正以保证post-selection inference的有效性。将TVA应用于印度哈里亚纳邦的免疫接种促进RCT（75种提醒、激励与社区大使的组合），发现结合激励、信息枢纽大使和提醒的政策使接种率提升44%。最具成本效益的政策（无激励）每美元接种量提升9.1%。对您有用：TVA的合并剪枝机制及winner's curse修正，为高维因子实验的因果推断与多重假设检验提供了可迁移的思路，且该免疫接种数据集对流行病学应用有参考价值。
- **关键技术**: `factorial design`, `treatment variant aggregation`, `winner's curse adjustment`, `post-selection inference`, `multiple hypothesis testing`
- **为什么对您有用**: TVA方法涉及高维因子设计下的选择后推断与多重检验修正，直接关联因果推断与假设检验的primary interest；同时作为大规模RCT应用，其数据集与分析范式对流行病学与经济学的secondary interest极具参考价值。

### 2. [10.3982/ecta19303](https://doi.org/10.3982/ecta19303) — Fisher–Schultz Lecture: Generic Machine Learning Inference on Heterogeneous Treatment Effects in Randomized Experiments, With an Application to Immunization in India
- **作者**: Victor Chernozhukov, Mert Demirer, Esther Duflo, Iván Fernández-Val
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1121-1164
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在随机化实验设定下，本文研究如何利用机器学习（ML）代理变量对异质性处理效应（HTE）的关键特征（如最佳线性预测 BLP、分组平均效应 GATES、极端影响单元特征 CLAN）进行估计与推断，允许高维协变量且不要求第一阶段 ML 估计一致收敛。方法核心是对 ML 代理变量进行后处理，通过 repeated data splitting 避免过拟合并保证推断有效性，同时采用 quantile aggregation（如 p 值中位数、置信区间分位数）聚合多次划分结果以降低估计风险。理论证明了分位数聚合策略的推断性质，并指出可利用因果学习目标函数构建更优的 ML 代理变量。实证部分将该方法应用于评估印度免疫接种助推政策的随机实验。该文对您有用之处在于：其 quantile aggregation 与 repeated splitting 机制为高维 debiased ML 推断提供了稳健的计算方案，且 BLP/GATES 框架可直接迁移至您关注的因果推断异质性分析及假设检验中。
- **关键技术**: `generic machine learning`, `quantile aggregation`, `repeated data splitting`, `heterogeneous treatment effects`, `best linear predictor (BLP)`, `causal learning proxies`
- **为什么对您有用**: 直接关联您 primary interest 中的 causal inference (HTE) 与 efficiency theory (debiased ML / post-processing ML proxies)；其 repeated splitting + quantile aggregation 的推断机制为高维假设检验与统计计算提供了可迁移的稳健算法框架，同时印度免疫数据集对 epidemiology 应用有参考价值。

## 经济理论 / 应用  *(econ_theory, 5 篇)*

### 1. [10.3982/ecta19576](https://doi.org/10.3982/ecta19576) — You Can Lead a Horse to Water: Spatial Learning and Path Dependence in Consumer Search
- **作者**: Charles Hodgson, Gregory Lewis
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1299-1332
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文在消费者搜索模型中引入空间学习机制，设定消费者基于已搜索产品在属性空间中的位置推断未搜索产品，从而产生搜索路径依赖。作者构建并估计了该结构模型，利用在线搜索路径数据验证了模型预测：搜索轨迹向最终选择产品收敛，且在冷门产品附近搜索步长更大。反事实分析表明，消除空间学习会使消费者福利下降12%，因为跨产品推断加速了优质产品的发现。研究进一步指出不具代表性的推荐会降低福利，最优推荐取决于学习机制与平台竞争。对您而言，此文属于经济理论的结构计量应用，其路径依赖设定与在线搜索微观数据对序列决策的因果推断建模有参考价值。
- **关键技术**: `structural econometric model`, `spatial learning`, `consumer search model`, `counterfactual welfare analysis`, `path dependence`
- **为什么对您有用**: 属于secondary interest中的economic theory (application, data sets, model)，提供了结合结构模型与在线搜索微观数据的实证范例，其路径依赖的设定对序列决策的因果推断建模有启发。

### 2. [10.3982/ecta20046](https://doi.org/10.3982/ecta20046) — Contract Labor and Establishment Growth in India
- **作者**: Marianne Bertrand, Chang-Tai Hsieh, Nick Tsivanidis
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1411-1448
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究印度《劳资争议法》(IDA)对大型工厂施加的解雇成本如何驱动合同工替代正式工，并影响企业动态与全要素生产率 (TFP)。在因果识别上，利用IDA仅适用于100人以上企业的制度门槛作为准自然实验，对比大（>100）小（<50）企业在2000-2015年间合同工份额的差异变化（大企业从21%增至40%，小企业仅14%至17%）。方法上结合了简约式（reduced-form）的因果估计与包含解雇成本的企业增长结构模型。结构模型的反事实模拟表明，合同工获取便利化使印度制造业TFP一次性提升7.3%，主要机制是缓解了大小企业间的资源错配，而非改变长期增长率。对您而言，该文是经济理论中应用因果推断的典型代表，展示了如何从制度细节提取识别策略，并桥接简约式与结构模型进行反事实量化。
- **关键技术**: `quasi-natural experiment`, `structural model of establishment growth`, `difference-in-differences`, `misallocation measurement`, `counterfactual simulation`
- **为什么对您有用**: 属于经济理论中的 applied causal work，展示了如何结合制度门槛（准自然实验）与结构模型进行反事实量化，对您在因果推断的应用场景和经济学数据集有参考价值。

### 3. [10.3982/ecta18492](https://doi.org/10.3982/ecta18492) — Fiduciary Duty and the Market for Financial Advice
- **作者**: Vivek Bhattacharya, Gastón Illanes, Manisha Padi
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1449-1480
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究金融顾问信义义务对委托代理问题的因果效应，利用递延年金交易级数据与州级普通法差异作为准实验变异。实证结果表明，信义义务使风险调整回报提高25个基点，并导致受影响企业进入率下降16%。通过构建企业进入与建议提供结构模型，将上述效应分解为固定成本增加与提供低质量建议成本增加两个机制。文中提出了识别与分离这两个渠道的方法，发现两者在实证上均显著。反事实模拟显示，进一步提高信义义务严格程度会单调改善建议质量。对您而言，该文是经济理论中结合准实验变异与结构模型进行机制分解和反事实推断的典型应用，对政策评估中的因果与结构联合推断有参考价值。
- **关键技术**: `quasi-experimental variation`, `structural model of entry`, `channel decomposition`, `counterfactual simulation`, `principal-agent model`
- **为什么对您有用**: 属于您的 secondary interest（经济理论中的 applied causal work 与模型），展示了如何利用州级政策变异做因果识别并结合结构模型做渠道分解与反事实分析，对处理类似政策评估与机制拆解的研究有方法迁移价值。

### 4. [10.3982/ecta22072](https://doi.org/10.3982/ecta22072) — Competitive Capture of Public Opinion
- **作者**: Ricardo Alonso, Gerard Padró i Miquel
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1265-1297
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文构建了一个 Bayesian 博弈模型：两个对立的利益方（interested parties）竞争捕获新闻条目的报道倾向，以影响具有异质先验的公民。模型刻画了均衡捕获水平与信息传递水平，核心发现是对立捕获努力并不相互抵消，而是因理性公民对信息性消息打折而削弱社会学习。公民的怀疑态度使捕获努力成为策略替代品，进而使竞争与媒体水平分化兼容；均衡中公民明知偏差仍选择消费立场一致的来源。该文是纯信息经济学/博弈论理论，无统计估计或因果推断方法贡献；对您而言仅在经济理论模型层面有弱关联，缺乏数据集、IV 或半参数方法等可迁移要素。
- **关键技术**: `Bayesian game equilibrium`, `strategic substitutes`, `information transmission`, `Bayesian persuasion`
- **为什么对您有用**: 属于经济理论二级兴趣范畴，但纯博弈论建模，无数据集、因果推断方法或统计估计组件可迁移，阅读收益有限。

### 5. [10.3982/ecta21016](https://doi.org/10.3982/ecta21016) — Producing Health: Measuring Value Added of Nursing Homes
- **作者**: Liran Einav, Amy Finkelstein, Neale Mahoney
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1225-1264
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在存在患者自选择（进入与离开护理机构）的设定下，构建风格化模型以识别和估计护理机构（SNF）的增值（value-added）estimand。核心方法通过显式建模患者的健康动态与选择过程来校正选择偏差，从而剥离出机构对健康产出与住院时长的因果效应。基于2011-2016年约600万Medicare患者的详细物理与精神健康数据，研究对约14,000家SNF进行了增值估计。实证结果表明SNF增值存在显著异质性：90分位与10分位机构相比，能在相同健康水平下提前近一周出院（相当于中位住院时长的1/4）。市场内部的增值异质性几乎与全国水平相当，暗示通过市场内患者重新配置可带来巨大潜在福利增益。对您有用：这是经济理论中处理选择偏差与因果推断的经典应用，其大规模Medicare数据集和针对选择偏差的建模思路对您在因果推断（选择偏差/敏感性分析）和流行病学应用方向有直接参考价值。
- **关键技术**: `value-added estimation`, `selection bias correction`, `health production model`, `heterogeneous treatment effects`, `Medicare claims data`
- **为什么对您有用**: 属于经济理论与因果推断的交叉应用，使用了大规模Medicare真实数据集；其处理患者自选择（进入与离开）的建模思路对您在因果推断（选择偏差/敏感性分析）及流行病学应用方向具有方法与数据层面的参考价值。

## 其他  *(other, 2 篇)*

### 1. [10.3982/ecta18063](https://doi.org/10.3982/ecta18063) — Private Information and Price Regulation in the US Credit Card Market
- **作者**: Scott T. Nelson
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1371-1410
- 相关性 2/10
- **摘要**: {
  "topic": "econ_theory",
  "summary_zh": "本文研究2009年美国CARD法案对信用卡市场定价的影响，该法案限制了贷款人基于新信息（私人/公共风险信号）调整利率，使定价向池化定价转移。作者构建了包含私人信息和借款人异质性的结构模型，以估计此定价规则变化的效率和分配效应。方法上结合了结构参数估计与反事实政策模拟，量化了价格离散下降对消费者剩余和贷款人利润的异质性影响。结果显示，高风险和价格无弹性消费者的价格下降，但最安全的次级借款人中超过30%面临价格超过支付意愿；总体消费者剩余上升，部分源于贷款人利润下降，部分源于法案为借款人提供的"保险价值"（避免不利风险变化后定价上升）。对您而言，这篇 Econometrica 文章展示了如何在存在私人信息和内生定价的经济学模型中进行反事实因果推断与政策评估，其结构模型设定和异质性效应的分析思路可迁移至经济因果推断应用中。",
  "key_techniques": [
    "structural model estimation",
    "counterfactual policy simulation",
    "private information pricing model",
    "heterogeneous surplus analysis",
    "price di

### 2. [10.3982/ecta22139](https://doi.org/10.3982/ecta22139) — Dynamic Concern for Misspecification
- **作者**: Giacomo Lanzani
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 4 · pp 1333-1370
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "econ_theory",
  "summary_zh": "本文研究决策者在面临模型遗漏风险时的动态行为：决策者对一组概率模型赋予先验，但担心真实模型不在该集合中，从而进行对冲。misspecification concern 被建模为内生的——若某模型对历史观测解释良好，则该关注衰减；衰减速度的不同导致长期偏好收敛到 SEU、maxmin 或 robust control 等不同静态形式。内生 misspecification concern 自然产生行为周期（behavioral cycles），作者刻画了极限行动频率。应用包括货币政策周期与复杂税表下的选择问题。对您而言，该文虽属 axiomatic decision theory 而非统计推断方法，但"模型遗漏下的动态对冲"框架与 causal inference 中 sensitivity analysis / model misspecification 的思路有概念对应，且属于经济理论中 robust decision-making 的前沿工作。",
  "key_techniques": [
    "maxmin expected utility",
    "robust control",
    "Bayesian model updating",
    "en


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

