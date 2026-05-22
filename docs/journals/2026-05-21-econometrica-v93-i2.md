# Econometrica — Vol 93  Issue 2  ·  2026-05-21

- 共 11 篇 · Econometrica

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.3982/ecta20203](https://doi.org/10.3982/ecta20203) — Choices and Outcomes in Assignment Mechanisms: The Allocation of Deceased Donor Kidneys
- **作者**: Nikhil Agarwal, Charles Hodgson, Paulo Somaini
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 395-438
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在肾脏分配机制设定下，研究基于选择的分配如何影响患者移植后生存年限（LYFT），核心挑战是选择偏差下潜在结果的识别。作者构建了结合选择与结果的联合模型，利用分配机制本身产生的工具变量（IV，如排队优先级的随机变动）实现非参数识别。估计上，采用结构模型量化选择效应，并将现实分配与无选择基准（随机分配）及最优基准进行反事实比较。实证表明现行机制筛选了移植后生存前景更好的患者，平均LYFT为9.29年，比随机分配多1.75年，但远低于最优聚合LYFT（14.08年）。这揭示了治疗最重症患者与最大化生命延长之间的政策权衡。对您有用之处在于，它展示了如何从机制设计中自然推导出 IV 以解决选择偏差，此思路可迁移至流行病学队列研究或经济理论中的分配问题因果评估。
- **关键技术**: `mechanism-derived instruments`, `nonparametric identification`, `selection on outcomes`, `counterfactual policy analysis`, `structural estimation`
- **为什么对您有用**: 直接契合您在因果推断（IV）与经济理论/流行病学（应用因果）的兴趣；展示了如何从分配机制中构造 IV 解决选择偏差，其识别策略与反事实分析框架可直接迁移至其他带选择偏差的观察性研究。

### 2. [10.3982/ecta21442](https://doi.org/10.3982/ecta21442) — Double Robust Bayesian Inference on Average Treatment Effects
- **作者**: Christoph Breunig, Ruixuan Liu, Zhengfei Yu
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 539-568
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在无混淆假设下，本文提出了一种针对平均处理效应（ATE）的双重稳健贝叶斯推断程序。方法核心在于利用半参数影响函数驱动的先导估计量，对条件均值函数的先验分布以及所得 ATE 的后验分布分别进行修正。理论上，本文在双重稳健性条件下建立了一个新的半参数 Bernstein–von Mises (BvM) 定理，证明了该贝叶斯过程与有效的频率学派 ATE 估计量渐近等价。具体而言，结果模型平滑性的不足可由倾向得分的高正则性补偿（反之亦然），且所得贝叶斯可信区间具有渐近精确的覆盖概率。模拟与 LaLonde 数据的实证表明，该方法在点估计精度和区间长度上优于现有方法。对您有用：该文将影响函数与贝叶斯修正结合，为您的 causal inference 和 efficiency theory 交叉兴趣提供了 DR 设定下 BvM 定理的新理论视角，且 LaLonde 应用契合 econ_theory 兴趣。
- **关键技术**: `double robustness`, `semiparametric Bernstein-von Mises theorem`, `efficient influence function`, `prior and posterior correction`, `unconfoundedness`
- **为什么对您有用**: 直接推进了您在 causal inference (ATE 的 DR 估计) 和 efficiency theory (半参数 BvM 定理与影响函数) 交叉方向的兴趣；双重稳健下的 BvM 理论是新的 semiparametric theory 贡献，且 LaLonde 数据应用契合您的 econ_theory 次要兴趣。

## 经济理论 / 应用  *(econ_theory, 6 篇)*

### 1. [10.3982/ecta20496](https://doi.org/10.3982/ecta20496) — Estimating Candidate Valence
- **作者**: Kei Kawai, Takeaki Sunada
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 463-501
- 相关性 4/10 · novelty: `application`
- **摘要**: 在美国众议院选举的结构模型下，本文旨在从选票份额数据中识别和估计不可观测的候选人“效价”（valence），关键挑战在于竞选支出的内生性以及候选人内生进入导致的样本选择偏差。识别策略借鉴了生产函数估计中的代理变量方法（类似 Olley-Pakes），利用竞选支出作为不可观测效价的代理变量以控制内生性，同时引入选择修正项处理样本选择。估计采用半参数两步法，先非参数估计进入概率与选择修正项，再估计结构参数。实证发现现任议员的效价显著高于挑战者，消除该差异会使挑战者获胜概率从6.5%升至12.1%。对您有用之处在于，该文将生产函数中的半参数代理变量方法应用于政治经济学，其处理不可观测混淆的思路与您关注的 proximal CI / negative control 框架有异曲同工之妙，提供了结构计量视角的半参数识别与估计实例。
- **关键技术**: `proxy variable approach`, `semiparametric two-step estimation`, `sample selection correction`, `structural production function estimation`, `control function`
- **为什么对您有用**: 属于经济理论的应用因果工作；其利用代理变量处理不可观测内生性的半参数识别策略，与您关注的 proximal causal inference 思路相通，提供了结构计量经济学中半参数估计与样本选择修正的实战案例。

### 2. [10.3982/ecta21871](https://doi.org/10.3982/ecta21871) — Feedback Design in Dynamic Moral Hazard
- **作者**: Jeffrey C. Ely, George Georgiadis, Luis Rayo
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 597-621
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文在动态道德风险框架下，研究粗粒度（全有或全无）绩效测度下的动态激励与绩效反馈联合设计问题。作者提出一种新的激励相容分析方法，推导出两阶段最优解：初始的“静默期”不提供反馈并要求代理人持续工作，随后的“全透明期”则在达到绩效阈值时停工。隐藏信息虽能激发更多努力，但激励无知的代理人成本更高；由于“向后复合效应”使得随时间推移隐藏信息的成本递增，最优策略将无知状态完全前置。主要理论贡献是刻画了该两阶段最优反馈机制的解析解。对您而言，本文属于经济理论中的纯机制设计模型，虽无数据与因果推断估计，但其动态信息设计的解析思路对理解契约理论有参考价值。
- **关键技术**: `dynamic moral hazard`, `incentive compatibility`, `information design`, `optimal control`, `mechanism design`
- **为什么对您有用**: 属于经济理论中的机制设计/契约理论模型，虽无数据与因果推断估计方法，但其动态信息设计与激励相容的解析解对理解经济模型中的信息不对称有参考价值。

### 3. [10.3982/ecta22841](https://doi.org/10.3982/ecta22841) — Comparative Statics With Adjustment Costs and the Le Chatelier Principle
- **作者**: Eddie Dekel, John K.-H. Quah, Ludvig Sinander
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 661-694
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文在带调整成本的优化模型中发展了单调比较静态理论，设定目标函数满足序数互补性假设且调整成本仅满足温和单调性条件。核心机制基于格论与超模性，证明了广义的 Le Chatelier 原理：在序数互补性假设下，若短期调整受制于单调成本，则长期对冲击的反应大于短期反应。进一步将结果扩展到完全动态调整模型，在稍强假设下证明了最优调整路径的单调性。理论应用于储蓄、生产、定价和投资等经典经济学模型。对您而言，本文属于纯微观经济理论，缺乏数据与统计推断，但其中的单调比较静态与格论工具对经济模型的结构分析有理论参考价值。
- **关键技术**: `monotone comparative statics`, `supermodularity`, `Le Chatelier principle`, `lattice theory`, `ordinal complementarity`
- **为什么对您有用**: 属于您的 secondary interest（economic theory），但本文是纯微观理论（格论与超模性），无数据集与统计因果推断，对统计方法论的直接迁移价值较低。

### 4. [10.3982/ecta22923](https://doi.org/10.3982/ecta22923) — Cap‐and‐Trade and Carbon Tax Meet Arrow–Debreu
- **作者**: Robert M. Anderson, Haosui Duanmu
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 357-393
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 在 Arrow-Debreu 一般均衡框架下，本文构建了配额均衡与排放税均衡两种模型，研究政府设定排放配额或税率后的均衡存在性与福利分配。证明了配额均衡始终存在，且在唯一外部性为总净排放时满足帕累托最优；而排放税均衡在某些税率下可能不存在。虽然每种配额均衡可实现为某种排放税均衡（反之亦然），但单一配额可能对应多个均衡价格，单一税率也可能对应多个排放水平。这种多重均衡的存在导致两种政策机制在均衡层面不等价。核心结论是配额机制在存在性和最优性上比税收机制更稳健，且排放权分配直接影响福利分布。对您而言，这篇纯经济理论文章展示了机制设计在一般均衡中的数学严谨性，但缺乏实证数据与统计推断，方法学借鉴价值有限。
- **关键技术**: `Arrow-Debreu general equilibrium`, `Pareto optimality`, `existence of equilibrium`, `multiple equilibria`, `mechanism inequivalence`
- **为什么对您有用**: 属于您的 secondary interest（经济理论），但属于纯数学一般均衡模型，无数据集与因果推断，主要提供碳税与碳配额不等价性的理论视角，对统计方法学的直接迁移价值较低。

### 5. [10.3982/ecta22028](https://doi.org/10.3982/ecta22028) — The Impact of Incarceration on Employment, Earnings, and Tax Filing
- **作者**: Andrew Garin, Dmitri Koustas, Carl McPherson, Samuel Norris, Matthew Pecenco, Evan K. Rose et al.
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 503-538
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究监禁对北卡罗来纳州和俄亥俄州个体工资、自雇及税收的因果效应，核心 estimand 为监禁对短期与长期劳动力市场结果的累积影响。识别策略采用两种准实验设计：量刑指南断点回归（RDD）与法官随机分配工具变量（Judge IV / Leniency IV）。利用大规模行政数据，研究估计出1年刑期导致5年累积收入下降13%，但5年以上无显著负向影响。结果表明先前被监禁者的低收入更可能源于上游因素（如先前司法接触或劳动力市场脱节），而非监禁本身的长期疤痕效应。对您有用：这是顶级经济学期刊中应用 IV 和 RDD 进行因果识别的标杆案例，展示了如何处理法官工具变量的局部平均处理效应（LATE）及合规性问题，对您在因果推断（IV）的应用理解与经济学实证设计有直接参考价值。
- **关键技术**: `Judge IV (leniency design)`, `Regression Discontinuity Design`, `Local Average Treatment Effect (LATE)`, `Administrative data linkage`, `Event-study estimates`
- **为什么对您有用**: 匹配您的经济学次级兴趣（应用因果推断与数据集），展示了 Judge IV 和 RDD 在大规模行政数据上的实际应用与 LATE 解读，对理解 IV 假设的实证落地极具参考价值。

### 6. [10.3982/ecta20574](https://doi.org/10.3982/ecta20574) — People Are More Moral in Uncertain Environments
- **作者**: Yiting Chen, Songfa Zhong
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 439-462
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文通过控制实验研究环境不确定性对个体道德决策的影响，核心发现是个体在不确定环境下的道德行为显著高于确定性环境。当道德含义降低或不确定性指向他人时，该效应减弱，且此现象违背标准占优（dominance）模型。作者提出基于焦虑的机制解释：个体在不确定中仿佛将道德行为视为改善结果的手段，并进一步分析了不确定性的复杂性维度。主要实证结果为不确定性引发的焦虑会显著提升道德表现。对您而言，此文属于纯行为经济学实验，未涉及因果推断的识别策略或半参数/高维统计方法，方法学 novelty 极低，仅可作为不确定性下决策模型的背景阅读。
- **关键技术**: `behavioral experiments`, `dominance violation`, `anxiety mechanism`, `moral decision-making`
- **为什么对您有用**: 属于经济理论中的行为经济学方向，但未涉及您关注的因果推断方法、真实观测数据集或计量模型，仅提供不确定性下决策行为的直觉参考，方法学收益极低。

## 其他  *(other, 3 篇)*

### 1. [10.3982/ecta22762](https://doi.org/10.3982/ecta22762) — On (Constrained) Efficiency of Strategy‐Proof Random Assignment
- **作者**: Christian Basteck, Lars Ehlers
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 569-595
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究不可分物品在具有严格偏好的代理人之间的随机分配机制。回答了机制设计领域的一个长期开放问题：证明了随机序列独裁（RSD）不能被同等待遇、事后Pareto效率和防策略性这三个性质刻画，存在满足这三者但不与RSD福利等价的机制。另一方面，本文证明RSD不会被任何满足防策略性和有界不变性的机制Pareto占优。进一步地，所有满足事后效率、防策略性和有界不变性的机制，都不会被其他满足防策略性和有界不变性的机制占优。这是纯微观经济学的机制设计理论，其“效率”指Pareto效率而非统计效率，与因果推断或高维统计无关，对您的统计方法论研究参考价值极低。
- **关键技术**: `Random Serial Dictatorship`, `strategy-proofness`, `Pareto efficiency`, `mechanism design`, `bounded invariance`
- **为什么对您有用**: 属于纯微观机制设计理论，虽在Econometrica发表，但不涉及您关注的因果推断、数据集或统计效率理论，对您的统计研究基本无直接参考价值。

### 2. [10.3982/ecta21101](https://doi.org/10.3982/ecta21101) — Uniform Priors for Impulse Responses
- **作者**: Jonas E. Arias, Juan F. Rubio-Ramírez, Daniel F. Waggoner
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 695-718
- 相关性 0/10
- **摘要**: {
  "topic": "econ_theory",
  "summary_zh": "在 set-identified 结构向量自回归（SVAR）模型中，针对正交矩阵集合上的均匀先验是否导致单个脉冲响应先验非均匀的争议，本文给出形式化回答。作者证明：当关注联合推断时，正交矩阵集合上的均匀先验不仅是充分的，而且是获得脉冲响应向量 identified set 上均匀联合先验的必要条件。这一结果直接反驳了此前对该标准程序"需谨慎使用"的呼吁。此外，文章给出了基于脉冲响应向量均匀联合先验进行推断的具体实施方案。核心工具是正交矩阵 Haar 测度与 identified set 上联合分布之间的精确对应关系。对您而言，SVAR 脉冲响应本质上是时间序列中的因果效应估计，set-identification 的先验规范性讨论与您在 causal inference 中 identification 及 sensitivity analysis 的兴趣直接相关，且文中 necessity & sufficiency 的证明风格可作数学统计视角的参考。",
  "key_techniques": [
    "structural vector autoregression",
    "set-identification",
    "uniform prior over orthogo

### 3. [10.3982/ecta22144](https://doi.org/10.3982/ecta22144) — A Quest for Knowledge
- **作者**: Christoph Carnehl, Johannes Schneider
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 2 · pp 623-659
- 相关性 0/10
- **摘要**: {
  "topic": "econ_theory",
  "summary_zh": "本文在动态经济理论框架下，研究科研问题的新颖度如何内生地影响发现的价值与难度，核心设定为知识沿时间步进式扩展且收益呈非单调性。研究者同时选择问题的新颖度与研究强度，短视最优往往倾向于较保守的问题。理论证明，由于知识积累的动态外部性，"登月式"研究（选择比短视最优更新颖的问题）能够改善长期知识演化。此类登月项目会诱发后续研究周期，将前沿发现与既有知识库相连接。该文为纯经济理论模型，未涉及数据集或统计推断方法；对您而言，若关注科研政策评估或科学知识生产的因果机制，可提供机制设计视角的参考，但无直接统计方法收益。",
  "key_techniques": [
    "dynamic externality",
    "endogenous growth model",
    "mechanism design",
    "nonmonotone returns",
    "optimal research intensity"
  ],
  "why_relevant": "属于纯经济理论（科研经济学），无数据集或统计方法；仅当您对科研政策的因果评估或机制设计感兴趣时有参考价值，与您的统计方法论主兴趣无直接关联。",
  "novelty_flag": "new_theory"
}


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

