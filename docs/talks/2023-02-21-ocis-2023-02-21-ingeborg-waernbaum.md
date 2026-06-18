# Selection bias and multiple inclusion criteria in observational studies

**讲者**: Ingeborg Waernbaum  
**讨论人**: Maya Mathur , Q&A moderator: Stina Zetterström  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2023-02-21  
**主题**: 因果推断  
**视频**: <https://youtu.be/u_TmBqJjEiA> · [幻灯片](https://drive.google.com/file/d/1bzK4X5GOsZpFmDHSw6F1NvQQxjud6FUi/view?usp=share_link)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告定位于**观察性研究中选择偏倚（selection bias）的敏感性分析**，尤其是当研究人群（subpopulation / selected units）通过**多重纳排标准（multiple inclusion/exclusion criteria）** 定义时的操作化问题。

**该子方向的追问**：在估计因果效应时，如果因选择性进入研究（conditioning on colliders / selection）而产生了偏倚，且没有足够观测变量来校正（或无法完全校正），如何通过敏感性分析量化这种偏倚的上界？

**奠基与主流路线**：传统的敏感性分析多集中于未测量混杂（unmeasured confounding），例如 E-value（VanderWeele & Ding, 2017）。对选择偏倚的敏感性分析则相对滞后。两条重要线索：
- **结构图（DAG）方法**：Bareinboim & Pearl（2012, 2016）等使用“选择图”（selection diagrams）和“选择后门准则”（selection back-door criterion）直接识别或校正偏倚——但要求足够的结构知识。
- **基于潜在结果的界限法**：Smith & VanderWeele（2019）在 *Epidemiology* 提出一种不指定图、只靠两个条件独立性假设的 SV 界限，通过未测量变量 U 将选择偏倚化为类似未测量混杂的形式，进而用 4 个风险比 RR 作为敏感参数构造上界。（用户幻灯片准确给出该界限的数学形式，B(β_R) = BF1·BF0，其中每个 BF 由 RR_UY|T 和 RR_SU|T 构成。）

**当前 frontier**：SV 界限虽然通用，但：
- 只有单一选择变量 S 的操作指南；
- 敏感参数（RR_UY|T、RR_SU|T 等）在实际应用中对研究者极难指定；
- 界是否 sharp（即能否达到）及敏感参数是否“变动独立”（variation independence）没有被系统讨论。
- 多个纳排（例如“出生与否”+“公立医院分娩”）在流程上常见，但 SV 原始论文未明示如何处理乘积结构的 IS = ∏ Sk。

**这场报告站在哪**：讲者（与 Zetterström 合作）将 SV 界限**延伸到多重选择情形**，给出了多重选择时偏导性的定性分析（结论：有多重选择时界可能变宽或变窄，取决于偏倚的方向是否叠加或抵消）。更重要的理论贡献是：
1. **证明了敏感参数（四个 RR）在总人口层面的变动独立性**（Theorem），使研究者可以独立地赋予每个 RR 值（≥1）而不受数据或其他参数的限制。
2. **给出了子总体 SV 界限 sharp 的充分条件**（Theorem），形式为 BF_U ≤ 1 / P(Y=1 | T=0, IS=1)，可直接用观测数据检验。
3. 同时提出了一个**无假设界限（assumption-free bound，AF bound）**，仅利用观测数据和 P(IS=1) 已知这一信息，完全不依赖 U 或条件独立性假设。

这些理论结果以外，配套一个 R 包 `SelectionBias`（arXiv 2302.06518）和一个模拟数据集 zika learner，极大降低了多重选择 SV 界限的使用门槛。

### 二、最小内核 / 一个最简例子

**符号与模型骨架**：
- 治疗 T ∈ {0,1}，二进制。
- 结局 Y ∈ {0,1}，二进制（报告全部假设二进制，非必需但简化）。
- 未测量变量 U（可以是一个向量；SV 界限的故事中还有一个 V，用于 M 结构的图形，但分析中可归入 U）。
- 选择变量 Sk ∈ {0,1}, k=1,…,K，复合选择指示子 IS = ∏ Sk = 1 当且仅当所有纳入标准同时满足（例如“活产”且“在公立医院分娩”）。
- 忽略抽样变异性、忽略已测混杂 X（或者将分析看作在 X 的一个确定层内）；无未测量混杂假设。
- 因果 estimand：
  - 总人口 causal risk ratio: β_R = P(Y(1)=1) / P(Y(0)=1)
  - 总人口 causal risk difference: β_D = P(Y(1)=1) - P(Y(0)=1)
  - 子总体（IS=1）对应 estimand：β_RS, β_DS。

**最简特例（K=1，一个选择 S）**：
假设研究者只排除了“自然流产”这一情形（S=1 if 活产）。观测数据仅包含 S=1 的个体，可计算的量是 
β_obs_R = P(Y=1|T=1, S=1) / P(Y=1|T=0, S=1) 
和 β_obs_D = P(Y=1|T=1, S=1) - P(Y=1|T=0, S=1)。

总人口 bias(β_R) = β_obs_R / β_R；bias(β_D) = β_obs_D - β_D。SV 界限称：存在 4 个敏感参数（都是 ≥1 的 RR），使得
B(β_R) = (RR_UY|T=1 · RR_SU|T=1) / (RR_UY|T=1 + RR_SU|T=1 - 1) × 同理 × T=0 的项 ≥ bias(β_R)。
给定研究者赋的 RR 值，就能反推出 β_R ≥ β_obs_R / B(β_R)。界限的保守性取决于对敏感参数的猜测。

**扩展到多重选择（K=2）**：
额外纳入“是否在公立医院分娩”作为第二个 S2。此时 IS = S1×S2，观测数据变得更小。SV 界限的敏感参数变为涉及乘积结构的 RR（如 RR_SU|T=1 需对应复合选择 S）。报告的理论分析表明：让研究者直接赋 4 个 RR 已很困难，再多重选择将更不可行——这正是 R 包 `SVboundparametersM()` 存在的理由：包内让用户指定三个 logistic 模型（U→T, U→S1, U→S2），自动计算所需的 RR。

### 三、报告主体：讲者讲了什么

[0:01:39]–[0:02:46] **开场与背景**：选择偏倚是与未测量混杂并行的因果推断威胁。引用 Lu et al. (2022, *Epidemiology*) 的话：“selection bias remains a subject of controversy; existing definitions are ambiguous.” 近期有大量新结果（但与未测量混杂相比晚了）。
- 讲者提问：“为什么会晚？” 留待讨论。

[0:02:55]–[0:04:58] **结构图线索**：Bareinboim & Pearl 的选择图与选择后门准则；Degtiar & Rose (2022) 关于可推广性（generalizability）和可迁移性（transportability）的综述。本报告采用 Smith & VanderWeele 的术语（total population / subpopulation of selected units），以区分目标人群与研究人群。

[0:07:19]–[0:08:03] **对 SV 界限的动机与推进**：讲者承认 SV 界限非常通用（仅用潜在结果+一个未测量变量 U），但“specifying the sensitivity parameters is very difficult, especially in the multi-selection case。” 这直接推动了 R 包的开发。

[0:08:30]–[0:10:17] **广义 M 结构与 SV 的条件独立性假设**：幻灯片精准绘制了图（V→S, U→Y, T→S）。两个核心假设：
1. 对总人口 estimand：Y ⟂ S | T,U。
2. 对子总体 estimand：Y(t) ⟂ T | S=1,U。
- 讲者强调它们也覆盖更小的结构，如 Sjölander (2023) 的结局-依赖抽样。

[0:14:59]–[0:17:59] **zika learner 模拟数据**：数据中的结构——Zika 感染（treatment）→ 小头症（outcome）；两个选择变量：birth（受 Zika 感染和居住地影响）和 public hospital（受居住地影响）；U = 居住地（unmeasured）、V = 社会经济地位（用两个 U 变量来更完整刻画 M 结构）。**尤其注意**：[0:17:30] 强调“所有分析在 X 层内；忽略抽样变异性；假设无未测量混杂”。

[0:18:39]–[0:21:49] **定义偏倚**：bias(β_R) = β_obs_R / β_R, 对于 risk difference 则 bias = β_obs_D - β_D。同理定义子总体 bias。

[0:22:01]–[0:24:10] **SV 界限的构造**：
- 敏感参数：RR_UY|T=t（当 U 从 0→1 时 Y 的风险比，在 T=t 组内）、RR_SU|T=t（当 U 从 0→1 时 S 的风险比，在 T=t 组内）。
- 界限 B(β_R) = BF1 × BF0，其中
  BF1 = (RR_UY|T=1 × RR_SU|T=1) / (RR_UY|T=1 + RR_SU|T=1 - 1)，类似定义 BF0。
- 讲者特别指出：这些 RR 是因果的（在给定 T 时 U 对 Y 或 S 的影响），而非观测风险比。实际赋值的困难在于研究者对 U 的认知有限。

[0:24:13]–[0:27:30] **多重选择下的扩展**：
- 讲者分析了偏导 ∂B / ∂IS，结论：二次选择可放大或抵消首个偏倚，方向取决于两个选择的偏倚是否朝向一致。
- 多重选择的核心挑战：一旦 K > 1，乘积结构的 IS 使得赋 RR 更不直观。R 包通过自动模型计算 RR，绕开手动赋值的困难。
- [0:26:33] 强调：界只针对偏倚方向已知（假定为正偏）的情形，否则需重编码治疗。

[0:28:38]–[0:33:38] **无假设界限（AF bound）**：
- 想法：利用概率论的基本约束（Y 和 IS 的联合概率不能超过 1）构造最小的可能 β_R 或 β_D，从而得到一个“不可能再差”的下界。
- AF 界限不需要 U，也不需要两个条件独立性假设——但要求已知 P(IS=1)（[0:43:15] 讨论中 Maya Mathur 确认这一点）。
- 具体公式（源自幻灯片）：β_min_R 通过将 P(Y=1) 和 P(Y=0) 各自分解为可观测部分和极值的组合得到；β_min_R 带入得到 B̃(β_R) ≥ β_obs_R / β_min_R。
- [0:33:00] 讲者指出 SV 界限有时会产出超出逻辑范围的结果（如 risk difference > 2），AF 界限提供一个“基准”：若 SV 界限 < AF 界限，则前者不可达到（即不 sharp），过于保守。

[0:34:50]–[0:38:11] **变动独立性与 sharpness**：
- Theorem（总人口）：四个敏感参数 {RR_UY|T=1, RR_UY|T=0, RR_SU|T=1, RR_SU|T=0} 都 ≥ 1，且它们在给定观测分布 P(Y,T,IS) 下互相不约束——即可以**独立**地赋任何 ≥1 的值。
- Theorem（子总体）：若 BF_U ≤ 1 / P(Y=1 | T=0, IS=1)，则子总体的 SV 界限是 sharp 的（即偏倚可达到该界值）。必要条件可用观测数据检验。
- [0:38:11] 讲者坦白：**总人口没有类似的简单 sharp 条件**，原因与为何不存在留作开放问题。

[0:42:20]–[0:52:00] **讨论人 Maya Mathur 的分析**：高屋建瓴地对比了 SV 界限与 ZW 界限的差异，尤其指出：
- SV 界限将选择偏倚“等效”为未测量混杂问题，依靠两个条件独立假设；ZW 界限则仅依赖于 P(S=1) 已知和概率约束，结构性假设更少。
- 以“结局直接导致选择”的 DAG 为例，展示 ZW 界限在此类 SV 假设不成立情况下仍可提供界值（尽管可能很宽）。
- **Mathur 提出的三个开放问题**（[0:52:57]–[0:53:33]）：
  1. ZW 界何时能越过 null（即形式上拒绝无效应）？
  2. 若 P(S=1) 未知，ZW 界限如何处理？
  3. 小样本下界值的不确定性多大？

[0:54:00]–[0:56:34] **讲者回应**：
- 承认当结局概率很小时（如 T1DM 应用）AF 界限会非常宽，提供不了多少信息。
- 呼应 Mathur 提到的“用 confounders 来减弱选择偏倚”的最新工作（可能指自己的同主题论文，待核实）。
- [0:55:00] 指出 U 定义为“最接近结局的 confounder set”时，SV 界限可能效率较好（但 U 不可观测时是假设）。

[0:57:54]–[1:01:10] **Q&A：sharpness 是否足够实用？** 
- 提问者质疑：即使 bound 是 sharp，达到 sharpness 的分布可能极不现实。
- 讲者持有建设性态度：敏感性分析应该被更多使用，即使 bounds 宽泛也有参考价值；“我们可以用数据来帮助验证假设。” Mathur 补充：可以考虑提升两个 bound 各自最 informative 的条件。

### 四、对应论文与开放问题

**对应论文**（经幻灯片与 arXiv 核对）：
1. **Zetterström, S. and Waernbaum, I. (2022)**. Selection bias and multiple inclusion criteria in observational studies. *Epidemiologic Methods*, 11(1). → 核心方法论文，包含变动独立性和 sharpness 的理论证明。
2. **Zetterström, S. and Waernbaum, I. (2023)**. Selection bias: an R package for bounding selection bias. arXiv: 2302.06518. → 方法+软件论文，介绍 `SelectionBias` 包及 zika learner。
3. 原始奠基工作：Smith, L.H. and VanderWeele, T.J. (2019). Bounding bias due to selection. *Epidemiology*, 30(4), 509–516.
4. 讲者引用 Sjölander (2020, 2023) 在 E-value 与 outcome-dependent sampling 的对应工作。

**开放问题**（每条扎根于转写/讨论）：
1. **总人口 SV 界限的 sharpness 条件**：讲者 [0:38:11] 明确“没有相应的简单结果”，此处是一个已知空缺（理论难题？）。
2. **多重选择下偏倚方向的确定**：当 K>1 时，各校正准则的偏倚方向可能相反，如何确保界是 upper bound？（[0:26:33] 提到需要重编码治疗，但未给出系统方向判别法）。
3. **无假设界限（AF bound）的最大信息性**：Mathur 提出 [0:51:00] 问题：当 P(S=1) 已知时，ZW 界限能否在某种结构下越过 null？讲者回应 [0:54:24] 当结局稀有时界极宽——那么，是否存在条件（如 outcome prevalence 较高时）使 AF bound 有意义？
4. **小样本推断**：Mathur [0:53:22] 问采样变异性对 bound 的影响——当前方法基于渐近无偏的点估计来构造界，缺乏置信区间或不确定带。
5. **与更一般的选择结构的兼容性**：SV 界限覆盖广义 M 结构，但 [0:46:00] Mathur 的 DAG 例子展示 SV 假设可能完全失败（如 outcome → selection）。**如何融入“结局直接导致选择”这种结构？** ZW 界限在该结构下虽可用但界极宽；是否存在介于 SV（强假设）与 ZW（弱假设但界宽）之间的、局部可验证的界限？
6. **与高维/弱识别场景的联系**：报告中没有提及，但研究者可思考：当 U 是高维且选择变量是复杂派生时，R 包中的 logistic 模型假设是否太强？有没有用更灵活的机器学习模型 + 敏感性分析的方法？

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

