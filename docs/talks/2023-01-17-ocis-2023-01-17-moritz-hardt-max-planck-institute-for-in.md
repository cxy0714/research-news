# From prediction to power

**讲者**: Moritz Hardt, Max Planck Institute for Intelligent Systems)  
**讨论人**: Michael P. Kim  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2023-01-17  
**主题**: 因果推断  
**视频**: <https://youtu.be/dShLLhc48yw> · [幻灯片](https://docs.google.com/presentation/d/1478yiG_0OWEa_9HxWpvJlhy1gvd7wCvm5UI3AMorVkM/edit?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告的核心不是提出一个新的因果识别方法，而是建立一套用于**测量和推理数字平台市场力量 (market power)** 的概念框架，名为 **"Performative Power"**。它根植于讲者之前提出的 **"Performative Prediction"** 理论，并试图将其与反垄断（antitrust）执法中的实际因果问题桥接。

**1. 背景子方向：预测的因果效应 vs. 传统的市场力量测量**

- **传统反垄断经济学的核心工具**：Lerner指数、HHI（Herfindahl-Hirschman Index）等。这些工具通常依赖于**市场定义**（Market Definition）、**均衡价格**、**竞争基准**（competitive equilibrium price）等概念。但数字平台（多边市场、免费服务、算法定价）使得市场定义极度困难，是当前执法中的公认痛点（[H:00:24] 引用了Stigler Committee和European Commission报告）。
- **当前统计/因果推断的前沿应用**：已有大量的经济学和营销科学工作估计特定行为的因果效应，例如位置排序对点击率（CTR）的影响（position bias）、评分对销量的影响（如Anderson & Magruder 2012的RDD）。但这些估计通常是孤立的、针对特定行为（treatment），缺乏一个统一的框架将它们与“企业是否拥有过度的市场力量”这一更大问题关联起来。
- **这场报告站在哪里**：讲者（Hardt及其合作者）提出了**Performative Power**，试图将上述孤立的因果效应估计统一进一个**有理论基础的测量框架**。它不依赖于市场定义，而是直接测量一个企业**潜在**能对目标群体特征造成的最大变化。其理论根脚是Performative Prediction（Perdomo, Zrnic, Mendler-Dünner, Hardt, 2020及其后续），后者本身是监督学习（supervised learning）的扩展，允许分布D随预测模型θ变化：D → D(θ)。

**2. 关键奠基与当前Frontier**

- **Performative Prediction** (Perdomo et al., 2020): 提出了这一概念框架，定义了Performative Risk, Performative Stability, Performative Optimality，并给出了重复风险最小化收敛到稳定点的条件（smooth, strongly convex loss, ε-sensitive distribution map）。
- **Strategic Classification** (Hardt, Megiddo, Papadimitriou, Wootters, 2016及后续): 试图通过标准经济学的微基础（rational utility-maximizing agent）来微观地导出D(θ)的形式。报告指出其存在**严重缺陷**（[H:00:48]及幻灯片），如聚合响应D(θ)存在不连续性、对非策略性行为非鲁棒、放大社会成本等（Jagadeesan, Mendler-Dünner, Hardt, 2021）。这使得直接从微观推导D(θ)的方法在实证中并不可靠。
- **因果效应的下界性质**：这是向Performative Power过渡的**关键技术桥梁**。报告证明了一个定理（[H:00:33]附近）：在无干扰假设下，**位置的因果效应（causal effect of position）β是Performative Power的一个下界**：P ≥ β。这意味着，即使我们不知道精确的D(θ)映射，我们也可以通过因果推断方法（如RDD, DID, A/B test）估计一个具体的因果效应，并判定这是Perf. Power至少有多大。这极大提升了框架的可操作性。

### 二、最小内核 / 一个最简例子

**核心思想**：一个企业（如YouTube）所做的**预测**（θ）本身会**因果地影响**它试图预测的**结果**（Y）。这个能力——即通过改变其预测来改变结果的能力——就是它的 **"Performative Power"**。

**符号与模型**：
- 令 **U** 为与一个数字平台（企业）交互的用户群体（例如，所有YouTube上传者或搜索结果的用户）。
- 令 **F** 为该企业可以采取的可能性**行动集** (a set of actions)。这些行动通常是算法或策略的改变（如，一个新的排序模型、关注时长的权重调整）。用 **f ∈ F** 表示一个具体行动。
- 令 **z(u)** 为用户 **u** 在当前状态下的**观察特征**（如，用户在该平台上的观看时长、创作者的订阅数）。
- 令 **z<sub>f</sub>(u)** 为一个**潜在结果** (potential outcome)，代表如果企业采取了行动 **f**，该用户将会有的特征。
- **Performative Power (P)** 定义为：  
  **P := sup<sub>f ∈ F</sub> E[ dist( z(u), z<sub>f</sub>(u) ) ]**  
  其中dist(·,·)是某种距离度量（如绝对差|·|或L2范式）。  
  这衡量的是：企业通过最“强力”的可行行动，所能**引起的目标群体的最大平均变化**。

**最简特例（d=1, 两个时间点, 一个二值行动）**:
- **行动**：平台的排序算法是一个二值变量。**f=0**：按照现有规则排序（给予新内容更多曝光）；**f=1**：改变排序规则，只按收益最大化（按广告收入）排序。
- **群体**：所有内容创作者 **U**。
- **特征(z)**：每个创作者 **u** 的**月收入**（设为1维）。
- **数据收集**：当前，平台在f=0下运行，我们观察到当前收入 **z = z <sub>f=0</sub>**。
- **潜在结果**：我们需要知道或估计 **z<sub>f=1</sub>**，即如果平台切换到f=1后的收入。
- **Performative Power 估计**：
    1. 进行一个A/B测试，将平台随机分为两组：一组继续f=0（对照），另一组切换到f=1（处理）。或者，如果有了自然实验，用DID等方法估计平均处理效应 (ATE) = E[ z<sub>f=1</sub> - z<sub>f=0</sub> ]。
    2. 这个ATE本身就是对该特定行动 **f=1** 的因果效应。根据定理，这个ATE是Performative Power的一个下界： **P ≥ |ATE|**。
    3. 如果我们能想到另一个更“夸张”的行动，比如“只展示我平台自己的广告，屏蔽所有第三方创作者的链接”，并估计出它的因果效应，我们就得到一个更大的下界，更接近真正的P。
- **解释**：如果ATE = 0，则企业改变到这个特定行动f=1不能改变创作者收入，该行动没有权力。如果ATE为正且很大（比如绝对值增加50%），则说明这个f行动很有权力。Performative Power就是寻找那个能使效果最大化的 **f**，它衡量的是企业的**最大潜在影响力**，而非某个具体行动的效果。若此最大影响力很小（P ≈ 0），则企业只能被动“学习”并适应市场，无法主动“引导”它——这正是竞争的代理指标（主讲者在最后强调的核心观点之一）。

### 三、报告主体：讲者讲了什么

**1. [0:00-0:05] 简介与动机**
- **问题**：监督学习隐含假设预测不能影响结果，但在数字平台（YouTube ranking, Google Search, algorithmic pricing）中，预测**因果地**影响结果（分布改变）。忽略此效应会引发自我实现的预言、Goodhart's law, Lucas critique等经典问题。
- **核心理念**：引入**Performative Prediction**，正式化“预测改变分布”的想法。

**2. [0:06-0:12] Performative Prediction 框架**
- **核心假设**：部署模型θ后，人口分布从D变为D(θ)。
- **代价函数**: Performative Risk = Risk(θ, D(θ))。
- **关键分解**: Risk(θ, D(θ)) = 标准风险 (在D上优化) + Performative Advantage (因引导至新分布带来的收益)。这揭示了两个竞争目标："学习" vs. "引导"。
- **解概念**:
  - **Performative Stable**: 模型在它自己诱导的数据上是最优的 (不动点)。重复风险最小化会在一定条件下收敛到它。
  - **Performative Optimal**: 在全局最优的分布上最优（更难达到）。

**3. [0:12-0:20] 从微观到宏观 / 转至 Power**
- **提出的核心问题**：D(θ)从哪里来？
- **路径一：Standard Microfoundations (Strategic Classification)**。假设理性agent最大化效用，但讲者指出它有三个严重缺陷：聚合响应不连续、非理性agent破坏稳定性、放大社会成本。
- **关键转折**: 觉察到Performative Strength的强度本质上就是**权力的体现**（power = ability to direct/influence behavior）。
- **新方向**: 主张直接研究权力本身，而不必拘泥于精确的D(θ)微观机制。

**4. [0:21-0:35] Performative Power: 理论定义与性质**
- **定义 (形式上)**：以Yelp和Walmart reviews为例，引入潜在结果编码，最终定义P = sup_{f∈F} E[dist(z(u), z_f(u))]。
- **关键性质1：低Power ⇒ 无“引导”收益**。证明了 Risk(θ_SL, D(θ_SL)) ≤ Risk(θ_PO, D(θ_PO)) + O(P)。其中θ_SL是监督学习最优，θ_PO是Performative最优。这意味着当P很小（竞争激烈）时，企业最好的策略就是优化现有数据（学习），无法靠引导获得额外收益。
- **关键性质2：垄断与竞争**。在Strategic Classification模型下证明：垄断企业最大化Power；个性化增强Power；外部选择削弱Power；**两个完美替代的竞争对手P=0**（类似Bertrand竞争）。

**5. [0:35-0:41] Performative Power 与反垄断 / 因果推断桥接**
- **因果效应作为下界**：提出关键定理：位置的因果效应（即使只针对一个具体行动）是Performative Power的一个下界。示例：Anderson & Magruder (2012) 的RDD估计（半颗星对餐厅客流的因果效应）可直接作为对Yelp的Power下界。
- **关键应用：Google Shopping反垄断案**。这是本次报告的**核心实证案例**。讲者总结了400页卷宗的要点 (由合作者G. Carovano整理): 欧洲委员会的核心主张是Google的搜索排名和购物框“引导”了流量，构成了滥用市场支配地位。他们拿出的“位置偏差研究”（position bias study）本质上就是想估计位置的因果效应 -> 即 **Performative Power**。Google反过来用DID等方法来反驳，试图证明自己没有Power。这里暴露出的一个核心法律/统计问题是：**F（行动集）怎么界定？** 企业认为合理的、温和的变动 vs. 监管者认为潜在的、极端的变化，会导致Power的估算天差地别。

**6. [0:41-1:00] 讨论与Q&A 核心观点**
- **Power ≠ Harm**: 在Q&A中反复强调，高Power未必有害（例如，凭借卓越产品“引导”用户是良性Power）。判断“harm”需要进一步的语境分析（如消费者福利是否受损）。Performative Power 主要解决“企业有多少权力”的实证问题，而不是“该权力是否违法”的规范问题。
- **如何确定F**: 讲者建议让F“尽量大”（larger set at the risk of being too large），以覆盖“潜在的、意想不到的、突然的转变行为”（如Twitter被收购后内部大变动）。因为这符合“potential for harm”的反垄断原则，也给了调查者更多灵活性。但F过大可能使Power成为空洞概念，其何时非空而变化是一个值得研究的问题。
- **Performative Power vs. 传统指标**: 不旨在完全取代，而是**澄清反垄断诉讼中的核心因果问题**。它与HHI等传统指标不同，没有天然的上界（或归一化方式），但可以通过表达为“baseline的百分比”来增强可解释性。

### 四、对应论文与开放问题

**(a) 对应的工作**

这场报告的核心技术内容来源于以下工作（基于幻灯片和转写提炼）：
- **Performative Prediction**: 主要概念与算法
  - [Perdomo, Zrnic, Mendler-Dünner, Hardt, 2020] *"Performative Prediction"*
  - [Mendler-Dünner, Perdomo, Zrnic, Hardt, 2020] *"Stochastic Optimization for Performative Prediction"*
  - [Jagadeesan, Mendler-Dünner, Hardt, 2021] *"Alternative Microfoundations for Strategic Classification"* (指出微观基础的三大缺陷)
- **Performative Power**: 自身定义与理论
  - [Hardt, Jagadeesan, Mendler-Dünner, 2020/2022] *"Performative Power"*，标题待确认（报告标题'From Prediction to Power'可能与之对应）。在转写中未给出arXiv号，但你在幻灯片中看到了 *"H, Jagadeesan, Mendler-Dünner, (2020)"* 的引用。
- **实证因果估计案例**:
  - Anderson & Magruder (2012): 半颗星对餐厅销售的RDD分析。
  - Narayanan & Kalyanam (2015): 关于Google定向广告对点击率影响的估计。

**(b) 开放问题 (扎根于转写与幻灯片)**

1.  **[关于行动集F的界定]** 如何系统地定义 **F**（可行行动集）？在讨论中讲者承认这是“我们经常挣扎的问题”。F太紧（只包括已实施过的行动）会低估Power；F太松（包括所有想象到的极端变化）可能使Power概念被滥用。这本质上是一个法律与统计交织的辨识问题。**(基于讨论 [H:00:48]， Michael Kim提问及讲者回答)**

2.  **[关于下界的闭合]** 报告证明了特定因果效应是Power的下界。但一个重要的统计问题是：**何时这些下界对真实的P（sup over all actions in F）是信息量足够的（sharp）？** 换句话说，我们能否找到条件，使得一个（或几个）战略选择的行动估计出的因果效应，能够作为整个P的精确上界或近似？**(这虽未明确提问，但从其构造「下界」的框架本质出发，自然会想到)**。

3.  **[关于博弈与动态]** Performative Power 目前定义为**静态**的（对所有可能行动能力的sup）。但反垄断中需要预测**竞争**和**进入**如何改变Power。在竞争下P迅速衰减到0是一个关键结果，但它是基于Strategic Classification的微观假设的。更一般地，**在非策略性、或更杂合的行为个体组成市场时，竞争如何改变Performative Power？**(转写中Q&A讨论了垄断与双寡头差异 [H:00:43])。

4.  **[关于 Power 与 Harm 的接口]** 如何将对Power的统计估计，转化为关于**危害程度**的正式判断？讲座中只区分了概念。但是，同一水平的Power（例如，使流量转向自己10%），在“引导至更优产品”与“引导至高价劣质产品”之间，对消费者福利的影响截然不同。这需要将Power执行时的**特征变化方向**（如，用户满意度、价格）纳入框架进行更有结构的分析。**(基于Q&A，Sacha提出“user’s value是关键中介”，讲者认同但强调需要额外建模)**

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

