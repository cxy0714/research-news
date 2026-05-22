# Econometrica — Vol 92  Issue 3  ·  2026-05-21

- 共 9 篇 · Econometrica

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.3982/ecta19466](https://doi.org/10.3982/ecta19466) — Bias‐Aware Inference in Fuzzy Regression Discontinuity Designs
- **作者**: Claudia Noack, Christoph Rothe
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 687-711
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 本文研究模糊断点回归（Fuzzy RD）中的因果参数推断问题，目标是在局部线性回归下构建置信集，关键正则条件为条件期望函数的二阶导数有界。作者提出 bias-aware 置信集，显式处理非参数平滑偏差；其构造借鉴了精确识别 IV 模型中的 Anderson-Rubin (AR) 统计量，避免了传统 delta method 在弱识别或离散驱动变量下的失效问题。在强识别与连续驱动变量的经典设定下，该方法与现有程序渐近等价；但在弱识别、离散驱动变量或 donut 设计等经验场景下仍保持有效性。该工作为存在非参数偏差的 IV 式因果参数提供了稳健的假设检验框架。对您有用：直接推进了您关注的 IV 因果推断与假设检验方向，其处理弱工具变量与离散协变量的 AR-type 推断思路可迁移至其他半参数 IV 模型。
- **关键技术**: `fuzzy regression discontinuity`, `Anderson-Rubin confidence set`, `bias-aware inference`, `local linear regression`, `weak identification`, `instrumental variable`
- **为什么对您有用**: 直接推进了您关注的 IV 因果推断与假设检验方向；其借鉴 AR 统计量处理弱识别与离散驱动变量的 bias-aware 推断思路，对半参数 IV 模型的稳健检验具有高度迁移价值。

### 2. [10.3982/ecta19636](https://doi.org/10.3982/ecta19636) — Identification and Estimation in Many‐to‐One Two‐Sided Matching Without Transfers
- **作者**: YingHua He, Shruti Sinha, Xiaoting Sun
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 749-774
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在无转移支付的多对一双向匹配（如大学录取）设定下，研究在单一市场数据中双方偏好的非参数识别问题，核心假设为观测匹配是稳定的且满足排除限制。利用排除限制（类似工具变量）构造偏好参数的识别条件，证明了在集中或分散市场下双方偏好的非参数可识别性。估计方面，比较了基于识别的直接估计量与参数贝叶斯方法，后者通过 Gibbs sampler 在现实规模问题中表现更优。智利公立与私立学校录取的实证分析展示了反事实政策评估。对您有用：该文将排除限制用于匹配市场的非参数识别，与您关注的因果识别及 IV 方法直接相关，且其贝叶斯计算方案对统计计算有参考价值。
- **关键技术**: `nonparametric identification`, `stable matching`, `exclusion restrictions`, `parametric Bayesian estimation`, `Gibbs sampler`, `counterfactual policy analysis`
- **为什么对您有用**: 论文核心是匹配市场中的非参数识别与排除限制（类似IV），直接对应您 primary interest 中的因果识别与 IV 方法；同时智利学校录取数据与反事实分析契合您 secondary interest 中的经济理论应用与因果推断。

## 经济理论 / 应用  *(econ_theory, 7 篇)*

### 1. [10.3982/ecta20417](https://doi.org/10.3982/ecta20417) — A Demand Curve for Disaster Recovery Loans
- **作者**: Benjamin Collier, Cameron Ellis
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 713-748
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文在自然灾害后家庭恢复贷款的情境下，估计并描绘了信贷需求曲线，目标参数为广延边际需求（extensive-margin demand）。识别策略利用了24个自然实验，基于联邦项目利率的时变外生冲击（类IV设计）来实现因果识别。基于超过一百万个申请者的行政数据，发现利率每上升1个百分点，贷款接受率平均下降26%。进一步分析揭示了申请人信用质量对需求的异质性影响以及月供目标行为。结合估计的需求曲线与项目成本，计算出该计划平均为每个借款人产生2900美元的社会剩余。对您而言，该文提供了一个利用自然实验进行因果识别的经济学实证范例，其大规模行政数据与异质性需求分析对经济理论中的应用因果推断有参考价值。
- **关键技术**: `natural experiment`, `extensive-margin demand estimation`, `exogenous time-based variation`, `heterogeneous demand elasticity`, `welfare analysis`
- **为什么对您有用**: 本文属于经济理论（应用因果）方向的实证研究，展示了如何利用自然实验（时变外生冲击）进行因果识别与需求曲线估计，其大规模行政数据结构和异质性分析思路对您关注的应用因果推断有直接参考价值。

### 2. [10.3982/ecta17876](https://doi.org/10.3982/ecta17876) — Equilibrium Grading Policies With Implications for Female Interest in STEM Courses
- **作者**: Tom Ahn, Peter Arcidiacono, Amy Hopson, James Thomas
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 849-880
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究STEM课程严格评分政策对学生选课与努力决策的影响，特别关注性别差异；设定上构建了学生课程需求与最优努力的结构模型，并将评分政策视为依赖学生需求的均衡对象。方法上，通过估计包含学生需求与教授评分策略的均衡模型，识别评分政策对选课组合的因果效应，并利用反事实分析模拟均等化评分政策的干预效果。实证结果表明，STEM与非STEM课程的需求差异解释了前者分数更低的现象，而均等化评分政策的反事实干预能显著缩小STEM性别差距并提高整体STEM选课率。对您而言，该文展示了结构均衡模型在经济学因果政策评估中的应用范式，属于您关注的economic theory与applied causal work的交叉。
- **关键技术**: `structural equilibrium model`, `counterfactual policy evaluation`, `discrete choice demand estimation`, `optimal effort model`
- **为什么对您有用**: 属于secondary interest中的economic theory与applied causal work；展示了结构计量模型如何处理均衡反馈下的政策评估，对理解经济学中的因果推断应用范式有参考价值。

### 3. [10.3982/ecta21157](https://doi.org/10.3982/ecta21157) — Walras–Bowley Lecture: Market Power and Wage Inequality
- **作者**: Shubhdeep Deb, Jan Eeckhout, Aseem Patel, Lawrence Warren
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 603-636
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文在一般均衡框架下研究商品与劳动力市场势力如何共同决定工资水平、技能溢价与工资不平等，利用美国普查局1997-2016年的微观面板数据进行结构估计。核心机制是构建包含异质性工人（高/低技能）与企业市场势力的结构模型，通过微观数据联合估计劳动力供给弹性、生产技术与市场结构参数。实证结果表明，市场竞争度下降使高/低技能工人平均工资分别下降11.3%和12.2%，对技能溢价上升贡献了8.1%，并解释了机构间工资方差增加的54.8%。该研究展示了如何将经济理论机制与大规模微观普查数据结合，进行反事实政策模拟。对您可能有用：该文提供了经济理论中结构估计与反事实分析的典型范式，其使用的US Census微观面板数据及建模思路对经济因果推断的应用有参考价值。
- **关键技术**: `structural estimation`, `general equilibrium model`, `microdata analysis`, `counterfactual simulation`, `market power measurement`
- **为什么对您有用**: 契合您在经济理论（应用、数据集、模型）方面的次要兴趣；展示了如何利用大规模微观普查数据（US Census）进行结构模型估计与反事实推断，对经济因果推断的应用场景有直接参考价值。

### 4. [10.3982/ecta19149](https://doi.org/10.3982/ecta19149) — Implementation via Information Design in Binary‐Action Supermodular Games
- **作者**: Stephen Morris, Daisuke Oyama, Satoru Takahashi
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 775-813
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 在二元行动超模博弈设定下，研究信息设计者通过选择信息结构所能实现的结果，核心约束为服从性（obedience）。文章刻画了最小均衡可实施性（smallest equilibrium implementability）的条件，要求满足更强的序贯服从（sequential obedience）：存在参与者的随机排序，使得即使个体认为只有排在前面的参与者会转向高行动，他也愿意转向。进一步刻画了偏好高行动但预期最差（最小）均衡被实现的设计者的最优信息结构。在势博弈中，若势函数和设计者目标函数满足凸性假设，最优结果是行动完美协调（所有人选同一行动），且高行动在最大化平均势的事件上发生。该文属于纯博弈论与机制设计理论，无实证数据或统计推断成分，对您的因果推断或半参数理论直接参考价值较低，但可作为经济理论中信息设计方向的背景了解。
- **关键技术**: `information design`, `supermodular games`, `Bayesian persuasion`, `sequential obedience`, `potential games`
- **为什么对您有用**: 属于经济理论中的纯信息设计/博弈论，缺乏数据集与因果推断方法，与您关注的计量经济学因果应用距离较远，仅作纯理论扩展参考。

### 5. [10.3982/ecta21548](https://doi.org/10.3982/ecta21548) — Setbacks, Shutdowns, and Overruns
- **作者**: Felix Zhiyu Feng, Curtis R. Taylor, Mark M. Westerfield, Feifan Zhang
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 815-847
- 相关性 1/10 · novelty: `new_theory`
- **摘要**: 本文研究动态委托-代理框架下的最优项目管理，设定中承包商可通过谎报挫折或延迟报告来掩盖偷懒（道德风险与信息不对称）。委托人的最优合同包含软截止期（soft deadline）与提前完工奖励，以同时激励努力与诚实报告。在项目后期，真实挫折会触发委托人在最小延期与无效率取消之间的随机化策略。由于延期可被反复批准，理论上项目进度与预算超支可任意大且最终仍可能被取消。该研究属于纯经济理论（机制设计/合同理论），未涉及实证数据或统计推断。对您而言，若需了解动态道德风险下的随机化机制与最优合同结构可作参考，但与您关注的因果推断或高维统计方法无直接交集。
- **关键技术**: `dynamic moral hazard`, `principal-agent model`, `mechanism design`, `optimal stopping`, `randomized strategy`
- **为什么对您有用**: 属于您 secondary interest 中的 econ_theory，但本文是纯机制设计/合同理论，无实证数据集或因果推断方法，仅适合作为动态委托代理模型的经济学背景阅读。

### 6. [10.3982/ecta21653](https://doi.org/10.3982/ecta21653) — Certification Design With Common Values
- **作者**: Andreas Asseyer, Ran Weksler
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 651-686
- 相关性 1/10 · novelty: `minor`
- **摘要**: 本文研究认证设计对信息披露的影响，设定为利润最大化认证方与质量未知卖方的博弈，且卖方机会成本依赖于商品质量（共同价值设定）。文章比较了认证方最优与透明度最大化两种认证设计。认证方最优设计实现了 Dye (1985) 的证据结构，即部分卖方获取信息而其余保持无知，导致市场仅出现部分披露。相反，透明度最大化的监管者偏好较不精确的信号，该信号通过更高的认证率和披露阶段的 unraveling（Grossman 1981, Milgrom 1981）向市场传递更多信息。本文属于纯微观信息经济学与机制设计理论，不涉及实证数据或高级统计推断方法。对您而言，除非研究兴趣延伸至信息不对称下的认证博弈模型，否则该文与因果推断、高维统计或效率理论等核心方向无直接关联。
- **关键技术**: `mechanism design`, `information disclosure`, `unraveling`, `common values`, `Bayesian persuasion`
- **为什么对您有用**: 本文属于纯微观经济理论（机制设计与信息经济学），缺乏实证数据与因果推断/半参数推断等统计方法，与您的 primary interests（因果推断、高维统计、效率理论）及 secondary interests 中的应用因果和数据集需求基本无关。

### 7. [10.3982/ecta18555](https://doi.org/10.3982/ecta18555) — Endogenous Information and Simplifying Insurance Choice
- **作者**: Zach Y. Brown, Jihye Jeon
- **期刊/来源**: Econometrica
- **分类**: vol 92 · issue 3 · pp 881-911
- 相关性 0/10 · novelty: `application`
- **摘要**: 在复杂保险产品市场中，个体内生地选择投入多少精力获取信息以比较替代方案，本文研究此内生信息获取对需求与福利的影响。基于理性疏忽（rational inattention）框架，构建并估计了一个简约的结构需求模型，其中个体决定对难以观测的特征进行多少研究。利用模型估计量评估简化选择的政策（如减少计划数量、限制自付费用上限）。实证发现减少计划数量可通过改善选择和节省信息成本提高福利，且限制自付费用上限比标准模型产生更大的福利收益；对您而言，这提供了一个经济理论中结构模型与反事实政策评估的应用案例，展示了内生信息处理如何改变传统因果或福利分析。
- **关键技术**: `rational inattention`, `structural demand estimation`, `counterfactual welfare analysis`, `endogenous information acquisition`
- **为什么对您有用**: 属于经济理论（secondary interest）中的结构模型与政策评估应用；展示了内生信息获取如何影响反事实福利分析，对在经济学应用中构建包含信息摩擦的因果或结构模型有参考价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

