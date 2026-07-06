# Econometrica — Vol 92  Issue 1  ·  2026-07-06

- 共 8 篇 · Econometrica
- 目录核对 ⚠️ 疑似漏 7 篇（对照 OpenAlex 18 篇）：10.3982/ecta921mono、10.3982/ecta921eds、10.3982/ecta921sum、10.3982/ecta921forth、10.3982/ecta921sec 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期 Econometrica 第 92 卷第 1 期的 8 篇论文大致可归为三条主线：**因果识别与政策评估**（涉及 RCT 与准实验设计）、**经济理论与福利分析的充分统计量方法**（涵盖最优政策设计、财富不平等、合同设计）、以及**纯经济理论**（递归效用、比较静态、福利公理）。因果识别主线包括两篇实证论文（Make-it-Right 项目与油气钻井截止日期），充分统计量主线有三篇（DI 改革、低利率与财富不平等、钻井合同），纯理论主线有三篇（网络学习、递归效用、比较静态与福利公理）。

在因果识别与政策评估方面，**Can Restorative Justice Conferencing Reduce Recidivism?** 利用 RCT 评估恢复性司法会议对青少年再犯率的影响，采用 ITT 分析与生存模型，发现四年内效应持续存在，是典型的实验因果推断案例。**Drilling Deadlines and Oil and Gas Development** 则利用准实验变异性（钻井截止日期前的行为聚集），通过结构估计模型识别合同时间约束对总剩余的影响，展示了因果推断在合同设计中的应用。两篇均关注政策干预的因果效应，但方法上 RCT 与结构估计形成对比。

充分统计量主线是本期方法亮点。**Designing Disability Insurance Reforms** 推导了最优 eligibility rules 与 benefit levels 的充分统计量条件，利用 labor supply elasticity 等可观测参数进行 welfare 比较，无需完整结构模型。**Wealth Inequality in a Low Rate Environment** 同样基于充分统计量，将利率对财富分布帕累托指数的影响归结为顶层个体终生股权与债务发行率的函数，并利用美国数据估计，解释了约 40% 的不平等上升。**Drilling Deadlines** 虽属实证，但其结构模型中的充分统计量思路（如钻井投入对总剩余的边际效应）也与该主线呼应。这三篇共同展示了充分统计量在连接理论模型与实证估计中的工具价值。

纯理论部分中，**Learning in Repeated Interactions on Networks** 给出了网络学习中学习速度的上界仅由私人信号分布决定、不随网络结构变化的结论，对社会学习理论有基础性意义。**Do not Blame Bellman** 澄清了递归效用中值函数唯一性失效的根源在于聚合器而非 Bellman 算子，并给出唯一性条件。**Comparative Statics With Linear Objectives** 提出平行四边形序，推广了多先验模型中的一阶随机占优概念。**“Near” Weighted Utilitarian Characterizations** 弱化连续性公理，给出 Pareto 最优的加权功利主义刻画。这四篇均为纯理论贡献，不涉及数据。

对于因果推断方向的研究者，优先看 **Can Restorative Justice Conferencing Reduce Recidivism?**（RCT 应用）和 **Drilling Deadlines**（准实验+结构估计）；对于半参数效率与充分统计量方向，**Designing Disability Insurance Reforms** 和 **Wealth Inequality in a Low Rate Environment** 是直接参考；对于高维或网络学习方向，**Learning in Repeated Interactions on Networks** 提供了理论界限。

## 经济理论 / 应用  *(econ_theory, 8 篇)*

### 1. [10.3982/ecta20996](https://doi.org/10.3982/ecta20996) — Can Restorative Justice Conferencing Reduce Recidivism? Evidence From the Make‐it‐Right Program
- **作者**: Yotam Shem-Tov, Steven Raphael, Alissa Skog
- **期刊/来源**: Econometrica
- **机构**: University of California, Los Angeles · University of California, Berkeley
- **分类**: vol 92 · issue 1 · pp 61-78
- 相关性 8/10 · novelty: `application`
- **摘要**: 本文利用随机对照试验（RCT）评估了针对13-17岁面临中等严重重罪指控青少年的恢复性司法会议（Make-it-Right, MIR）项目对再犯率的影响。研究将143名符合条件的青少年随机分配到MIR项目或标准刑事起诉的对照组，并追踪了随机化后四年的再逮捕数据。核心估计显示，MIR项目在六个月内将再逮捕概率降低了19个百分点（相对降低44%），且该效应在四年后仍持续存在。方法上，本文采用了标准的意向治疗（ITT）分析，并可能通过线性概率模型或生存分析进行估计，同时检验了随机化平衡和样本损耗问题。结论表明，恢复性司法会议可作为传统刑事司法的有效替代方案，尤其对相对严重犯罪的青少年。对您而言，这是一篇高质量的应用因果推断论文，展示了在司法政策评估中如何利用随机化设计进行严谨的因果效应估计，其分析框架（RCT设计、ITT估计、长期效应追踪）对您在流行病学或经济理论方向的应用因果工作具有直接参考价值。
- **关键技术**: `randomized controlled trial`, `intention-to-treat analysis`, `linear probability model`, `survival analysis`
- **为什么对您有用**: 本文属于经济理论/应用因果推断方向，直接对应您的secondary interest中的'econ_theory (application, data sets, causal inference)'。论文展示了在司法政策评估中如何利用随机化设计进行严谨的因果效应估计，其分析框架（RCT设计、ITT估计、长期效应追踪）对您在流行病学或经济理论方向的应用因果工作具有直接参考价值。从武器库角度看，您'very_familiar'中的'estimation theory in causal inference'足以理解并批判本文的估计策略（如检查随机化平衡、处理样本损耗），属于**立即可做**的阅读范畴。

### 2. [10.3982/ecta19021](https://doi.org/10.3982/ecta19021) — Designing Disability Insurance Reforms: Tightening Eligibility Rules or Reducing Benefits?
- **作者**: Andreas Haller, Stefan Staubli, Josef Zweimüller
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · University of Calgary · University of Zurich · Norwegian School of Economics · International Zinc Association · Fafo Foundation
- **分类**: vol 92 · issue 1 · pp 79-110
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在 disability insurance (DI) 的 welfare analysis 中发展了一个 sufficient statistics 框架，目标是刻画两个核心政策参数——eligibility rules 和 benefit levels——的社会最优条件。作者推导出基于可观测充分统计量（如 labor supply elasticity、fiscal externality、insurance value）的最优条件公式，使得 welfare 比较不依赖于完整结构模型。将该框架应用于奥地利两次限制性 DI 改革（1996 和 2000 年），利用 administrative data 估计关键弹性，发现收紧 eligibility rules 比降低 benefit levels 带来更高的 fiscal cost savings 和更低的 insurance losses。核心方法工具是 sufficient statistics 与 revealed preference 的结合，属于公共经济学中 welfare analysis 的标准范式。对您而言，本文是经济理论中 applied causal work 的典型范例，展示了如何用 reduced-form 估计（如 IV、bunching）为 structural welfare 比较提供输入，适合作为进入经济政策评估领域的入门读物。
- **关键技术**: `sufficient statistics`, `revealed preference`, `fiscal externality`, `bunching estimation`, `labor supply elasticity`
- **为什么对您有用**: 本文属于经济理论（secondary interest）中的 applied causal work，使用 administrative data 和 reduced-form 估计（如 bunching）来校准 welfare 模型。武器库中的 estimation theory in causal inference 和 identification theory 可直接用于理解其估计策略（如如何用 IV 识别 labor supply elasticity）。本文是 gateway reading：它清晰展示了从估计到 welfare 结论的完整链条，适合作为进入经济政策评估方向的入门读物，值得花时间读全文。

### 3. [10.3982/ecta20806](https://doi.org/10.3982/ecta20806) · [arXiv](https://arxiv.org/abs/2112.14265) — Learning in Repeated Interactions on Networks
- **作者**: Wanying Huang, Philipp Strack, Omer Tamuz
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 1 · pp 1-27
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究理性代理人在社会网络中重复互动时的学习速度。在每期，代理人观察邻居的过往行动后收到私人信号，并选择仅依赖于状态的行动。由于均衡行动依赖于高阶信念，行为刻画通常困难。然而，作者证明无论网络大小、形状、效用函数或代理人耐心程度如何，任何均衡中的学习速度上界仅由私人信号分布决定。该上界是常数，不随网络结构变化。这一结果为网络学习理论提供了基础性界限，对经济理论中社会学习与信息传播的研究有重要参考价值。
- **关键技术**: `social learning`, `Bayesian equilibrium`, `higher-order beliefs`, `learning rate bounds`
- **为什么对您有用**: 本文属于经济理论中社会学习的核心问题，与您的 secondary interest 经济理论直接相关。虽然方法上不直接涉及您的技术武器库，但作为 gateway reading，它清晰阐述了网络学习的基本设定和关键结论，适合作为进入该领域的入门读物。武器库中的非参数统计和因果推断工具虽不直接适用，但理解此类理论界限有助于您评估经济应用中的统计模型。值得花时间读全文以把握经济理论中学习问题的框架。

### 4. [10.3982/ecta19092](https://doi.org/10.3982/ecta19092) — Wealth Inequality in a Low Rate Environment
- **作者**: Matthieu Gomez, Émilien Gouin-Bonenfant
- **期刊/来源**: Econometrica
- **机构**: Columbia University
- **分类**: vol 92 · issue 1 · pp 201-246
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究利率对财富不平等的影响机制。在低利率环境下，食利者的财富增长率下降，但企业家因融资成本降低而获得更高的增长率。作者推导出一个充分统计量，将利率对财富分布帕累托指数的影响归结为顶层个体终生股权与债务发行率的函数。利用美国顶级财富轨迹的新数据估计该充分统计量，发现利率（或更一般地，要求回报率）的长期下降可以解释约40%的帕累托不平等上升幅度。方法上，该文结合了理论模型推导与实证估计，属于应用因果推断的典型范例。对于您关注的经济学应用方向，本文展示了如何用简洁的充分统计量连接宏观参数与微观数据，其识别策略和估计思路对您从事的因果推断应用研究有直接参考价值。
- **关键技术**: `sufficient statistic`, `Pareto exponent estimation`, `wealth distribution dynamics`, `entrepreneurial vs rentier channel`
- **为什么对您有用**: 本文属于经济理论应用方向，直接对应您的secondary interest。它展示了如何将宏观参数（利率）对不平等的影响分解为可估计的充分统计量，其识别策略和估计方法对您从事的因果推断应用研究有参考价值。武器库中'identification theory in causal inference'和'minimax bounds for estimation problems'可用于评估其充分统计量的识别假设是否可放松或检验估计的精度边界。本文是值得花时间读全文的入门级应用经济学论文。

### 5. [10.3982/ecta18436](https://doi.org/10.3982/ecta18436) — Drilling Deadlines and Oil and Gas Development
- **作者**: Evan Herrnstadt, Ryan Kellogg, Eric Lewis
- **期刊/来源**: Econometrica
- **机构**: Congressional Budget Office · National Bureau of Economic Research · University of Chicago · Texas A&M University – San Antonio
- **分类**: vol 92 · issue 1 · pp 29-60
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究油气租赁合同中'primary term'（钻井截止日期）对钻井决策和总剩余的影响。利用路易斯安那页岩繁荣期的数据，作者首先发现钻井活动在截止日期前显著聚集。通过估计企业的钻井和投入选择模型，他们证明primary term可以通过抵消矿区使用费（royalties）对收入的税收效应和延迟钻井的抑制作用来提高总剩余。然而，当生产结果对钻井投入敏感，且钻一口井无限延长可钻更多井的期限时，这种收益会减少。进一步将模型扩展到考虑矿权所有者的租赁报价后，发现primary term对所有者收入的影响较小。该研究为合同设计中的时间约束如何影响实际经济结果提供了因果证据。
- **关键技术**: `bunching estimation`, `structural model of firm behavior`, `dynamic discrete choice`, `royalty taxation`
- **为什么对您有用**: 本文属于经济理论的应用实证工作，与您的secondary interest 'economic theory (application, data sets, causal inference)'直接相关。它展示了如何利用bunching设计和结构模型来识别合同条款的因果效应，其分析模式（结合准实验变异与模型估计）对您从事应用因果推断研究有参考价值。武器库中'identification theory in causal inference'和'estimation theory in causal inference'足以理解其核心识别策略，属于'立即可做'的gateway阅读。

### 6. [10.3982/ecta20386](https://doi.org/10.3982/ecta20386) — Do not Blame Bellman: It Is Koopmans' Fault
- **作者**: Gaetano Bloise, Cuong Le Van, Yiannis Vailakis
- **期刊/来源**: Econometrica
- **机构**: IPAG Business School · Paris School of Economics · Adam Smith Institute · University of Glasgow
- **分类**: vol 92 · issue 1 · pp 111-140
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文在递归效用（recursive utility）的随机动态规划框架下，提出基于 Tarski 不动点定理的统一方法。核心问题是：给定一个聚合器（aggregator），递归程序可能对应多个值函数（multiple values），而传统 Bellman 算子压缩性假设（如 Blackwell 条件）常被归咎为唯一性失效的原因。作者证明，唯一性失效的根源在于存在多个与聚合器一致的递归效用函数，而非 Bellman 算子的性质。他们给出了保证唯一性的充分条件（如单调性、凹性、有界性等），并论证在非唯一情形下，Bellman 算子的最大不动点应具有优先地位。理论结果通过构造性例子和反例加以说明。对您而言，本文是经济理论中动态规划与递归效用的经典问题，可作为理解该领域模型设定（如 Epstein-Zin 偏好）的入门读物，武器库中的非参数统计和逆问题工具可用于分析此类递归结构下的识别问题。
- **关键技术**: `Tarski fixed point theorem`, `recursive utility`, `Bellman operator`, `aggregator`, `stochastic dynamic programming`
- **为什么对您有用**: 本文属于经济理论（secondary interest）的 gateway reading，清晰阐述了递归效用模型中的多重值函数问题，适合作为进入该领域的入门读物。武器库中的非参数统计和逆问题工具（very_familiar）可用于分析此类递归结构下的识别问题，但核心机器（动态规划、不动点理论）不在武器库中，属于暂不可做方向。值得花时间读全文以理解模型设定和问题背景。

### 7. [10.3982/ecta19738](https://doi.org/10.3982/ecta19738) — Comparative Statics With Linear Objectives: Normality, Complementarity, and Ranking Multi‐Prior Beliefs
- **作者**: Pawel Dziewulski, John K.-H. Quah
- **期刊/来源**: Econometrica
- **机构**: University of Sussex · National University of Singapore
- **分类**: vol 92 · issue 1 · pp 167-200
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文在经济学比较静态分析中提出了一种新的集合序——平行四边形序（parallelogram order），该序保证对于任意线性目标函数 p·x，当约束集 A 在该序下增大时，argmin 在乘积序下单调递增。利用这一结果，作者刻画了导致正常需求（normal demand）的效用/生产函数类，以及边际成本随要素价格上升的生产函数类。通过推广超模性（supermodularity），文章还刻画了要素互补的生产函数类。在不确定性决策的背景下，该集合序自然推广了多先验模型中的一阶随机占优概念。本文是纯经济理论贡献，不涉及统计推断或数据。
- **关键技术**: `parallelogram order`, `supermodularity`, `comparative statics`, `first-order stochastic dominance`, `multi-prior models`
- **为什么对您有用**: 本文属于经济理论方向，是研究者的次要兴趣。文章不涉及统计方法或数据，但作为经济理论中比较静态分析的基础性工作，对于理解经济模型中的单调性结构有参考价值。研究者若想进入经济理论领域，本文可作为入门读物，但武器库中的统计工具无法直接应用于本文问题。

### 8. [10.3982/ecta18930](https://doi.org/10.3982/ecta18930) · [arXiv](https://arxiv.org/abs/2008.10819) — “Near” Weighted Utilitarian Characterizations of Pareto Optima
- **作者**: Yeon-Koo Che, Jinwoo Kim, Fuhito Kojima, Christopher Thomas Ryan
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 1 · pp 141-165
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文在经济学福利经济学框架下，研究Pareto最优与加权功利主义社会福利函数之间的关系。核心问题是：是否每个Pareto最优配置都可以表示为某个加权功利主义社会福利函数的最大化？经典结论需要连续性公理，而本文通过弱化连续性公理，给出了两种“近乎”加权功利主义的刻画。第一种刻画使用有限序列的非负且最终为正的福利权重，依次最大化功利主义社会福利函数；第二种使用一类具有正超实数权重的功利主义社会福利函数。这两种刻画对应的社会福利排序由标准加权功利主义公理在适当弱化连续性条件下唯一刻画。本文是纯经济理论工作，不涉及统计推断或数据。
- **关键技术**: `Pareto optimality`, `weighted utilitarian welfare`, `social welfare ordering`, `continuity axiom`, `hyperreal weights`
- **为什么对您有用**: 本文属于经济理论（secondary interest），但纯理论性质，不涉及数据集或统计方法。对于研究者而言，可作为了解福利经济学中Pareto最优与功利主义公理化基础的入门读物，但武器库中无直接可攻工具，暂不可做。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

