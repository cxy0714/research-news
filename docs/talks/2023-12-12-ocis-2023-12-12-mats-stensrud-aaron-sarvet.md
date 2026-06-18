# Interpretational errors in causal inference and how to avoid them

**讲者**: Mats Stensrud, Aaron Sarvet  
**讨论人**: Kerollos Wanis and Vanessa Didelez . Q&A moderators: Lan Wen  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2023-12-12  
**主题**: 因果推断  
**视频**: <https://youtu.be/bEhAMREAEbo> · [幻灯片](https://drive.google.com/file/d/1NOkFQaB1bC5HCmpGV7gVC635TlhdJoQG/view?usp=drive_link)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告属于因果推断中一个正在快速发展的反思性子方向——**“估计量的实质解释性 vs. 统计便利性”之间的张力**。它追问的核心问题是：当我们定义了一个有良好统计性质（可识别、可有效估计、满足某种零假设准则）的因果参数后，这个参数是否真的对应了研究者心中想回答的那个实质性问题？如果不是，就把那个参数的结果“滑移”解释成理想问题的答案——这种“身份滑移”（identity slippage）[约 0:22:15] 是报告反复强调的解析错误。

这个子方向的奠基与主流路线可以追溯到两个传统：
- **问题驱动（理想）传统**：以 Robins (1986, 1987) 的“问题先于方法”哲学为代表，后来被目标试验框架 (Target Trial) 和因果路线图 (Causal Roadmap) 广泛推广。它要求先精确表述因果问题（用潜在结果语言），再找识别条件，最后估计。报告里引用了一句 “the primary question... should be what economic question does the analyst seek to answer?” [0:06:00]，来自 Heckman & Urzua (2010)。
- **“参数空间”探索（实用）传统**：在“识别-统计性质”驱动的驱动下，方法学家不断创造新的因果参数——例如中介分析中，在自然直接效应 (NDE) 被证实非参数不可识别的 (Avin, Spirtes & Pearl 2005) 之后，涌现了一大批可识别的替代参数（随机干预类似物 / RIA、分离效应 / separable effects、条件分离效应等，跨度约 2010–2023）。这些参数有吸引人的统计性质（可识别、可有效估计、甚至满足 sharp mediational null），但报告指出，它们只是“与 NDE 概念相邻”，实质是完全不同的因果实体 [约 0:21:30–0:22:00]。

当前 frontier：这个反思性子方向正处在从“发明新参数”到“严格检查参数与问题之间的对应关系”的转折点。几个关键里程碑：
- **Avin, Spirtes & Pearl (2005)**：证明在存在“反证见证”（recanting witness）的 DAG 下 NDE 不是非参数可识别的 —— 由此点燃了实用期。
- **VanderWeele 等 (2014)**、**Miles (2023)**、**Díaz (2023)**：定义了 sharp mediational null 准则，验证出部分实用参数不满足该准则 [0:19:00–0:19:40]。
- **Stensrud 等 (2020, 2021, 2023)** 与 **Robins-Richardson (2010)** 的干预主义中介分析路线提出另一个框架：与其在 NDE 附近找替代，不如直接修改问题描述（引入 intervening variable），生成一个完全不同但可识别的“问题-参数”对。

**这场报告站在这个 frontier 的哪一侧**：它不做新参数的技术改进，而是**负责元层面的诊断**——系统性地审视实用主义框架是否给身份滑移创造了“认知条件”（cognitive conditions），并用实证（一个系统综述和两个案例）来支撑这个论点。报告非常明确地说：“我们不认为实用主义总是坏的，但要有透明度并意识到其中的危险。” [0:42:39–0:43:01]

关键相关工作（听不准的名字标注不确定性）：
- Avin, Spirtes & Pearl (2005) — recanting witness 与 NDE 不可识别性。（字幕可能拼错 “Avin” 为 “Aveng”，已校正）
- Miles (2023), Díaz (2023) — 讨论 sharp mediational null criterion 的识别 / 检验。
- Robins & Richardson (2010), Robins, Richardson & Shpitser (2020) — interventionist mediation (separate effects)。
- Wen, Sarvet & Stensrud (2023), arXiv:2305.00349 — 在无测混杂下对 intervening variable 的因果推断。
- Sarvet, Laurendeau & Stensrud (要投 arXiv 的 工作中，标注“unpublished”) — 有限资源下的 optimal treatment allocation under constraint-induced interference。

### 二、最小内核 / 一个最简例子

#### 2.1 符号、模型、数据

记观测数据为 $(A, M, Y, L)$，其中：
- $A$ — 暴露（如性别、种族），取值 $\{0,1\}$。
- $M$ — 中介（如是否被安排面试）。
- $Y$ — 结局（如是否被录用）。
- $L$ — 基线的/非暴露引起的混杂。

潜在结果：
- $Y(a, m)$ — 把 $A$ 设为 $a$，$M$ 设为 $m$ 时的 $Y$。
- $M(a)$ — 把 $A$ 设为 $a$ 时的 $M$。
- **自然直接效应 (NDE)** 的参数：
  \[
  \text{NDE} = \mathbb{E}[Y(1, M(0)) - Y(0, M(0))].
  \]
  它把暴露从 0 变为 1，但中介固定在其“无暴露时的自然值” $M(0)$。这对应的是“纯粹改变 A 而保持其他路径不变”的直觉。

#### 2.2 一个最简特例（二值处理，单一中介，无基线混杂）

假设 $L$ 为空（或已严格调整），$A, M, Y$ 均为二值。根据 Avin et al. (2005)，NDE 非参数可识别当且仅当 $A$ 与 $M$、$M$ 与 $Y$ 之间没有未被 $A$ 影响的混杂。即不存在“recanting witness”——一个由 $A$ 引起的、同时影响 $M$ 和 $Y$ 的变量（例如 $L$ 是 $A$ 的后代）。

**问题**：在真实队列中，$A$ (性别) 可能影响 $L$ (教育水平)，而 $L$ 又影响 $M$ (是否面试) 和 $Y$ (是否录用)。这时 L 就是 recanting witness，NDE 不可识别。

**实用主义解决办法**：放弃 NDE，改为定义一个**随机干预中介类似物 (RIA-NDE)**：
\[
\text{RIA-NDE} = \mathbb{E}\Big[\sum_{m} Y(a', m) P(M(a^*) = m \mid L) \Big] \quad \text{(用某个固定的 } a^*\text{)}.
\]
这个参数是识别且可估计的（幻灯片显示它满足 front-door 公式 [0:39:49–0:40:07]；识别公式形式上有 $\sum_{m,l} f(m|a^\dagger,l) f(l) \sum_{a} \mathbb{E}[Y|l,a,m] f(a|l)$）。

**身份滑移的机制**：研究者最初问的是“换 $A$ 但不换 $M$，对 $Y$ 的影响”（即 NDE 的直觉）。在方法部分，他们正确地声称“我们估计了 RIA-NDE”。但在讨论部分，他们可能会写出“我们发现直接效应（NDE）解释了总效应的 $x\%$”或“即使控制了中介路径，暴露的直接影响仍然显著”，而 RIA-NDE 并不分解一个总效应为直接+间接 [0:22:15–0:22:27]。

报告将这个“说一套（估计的统计参数）做一套（解释成另一个理想参数）”现象定义为**身份滑移 (identity slippage)** [0:22:17]，并给出了正式定义（见幻灯片，涉及两个参数空间 $\mathcal{P}_{\mathcal{F}}$ 和 $\mathcal{P}$，对比两个模型的识别情况）。

### 三、报告主体：讲者讲了什么

以下按时间顺序复原报告的三大模块。

#### 模块 1：问题背景与有限资源案例 [0:01:38–0:09:44]

- **[0:01:38] Mats 开场**：先给出三个实际例子（器官移植、新冠 ICU 床位分配、手术量与死亡率的关系），它们有一个共同点——资源是有限的，一个患者的治疗选择会影响另一个患者的可用资源。
- **[0:03:58–0:04:08]**：讲者引 Robins (1987) 的著名论述：数据集只是字符串；我们得先把“通俗英文表达的问題”翻译成正式的数学参数，否则后面分析无从做对。
- **[0:06:13–0:06:48]**：提出限制资源的第一个特征：**雷姆斯限于一组患者的整个集群**。例如，ICU 分配不是一个患者一个患者独立决定的，而是根据所有候诊的患者的病情评分（如 SOFA score，含有疾病严重程度等特征）来排序。因此，感兴趣的理想稳态 $G_n$ 应是一个从 $\mathcal{L}_1, \dots, \mathcal{L}_n$（全部 n 名患者的协变量）到 $\{0,1\}^n$ 的映射，不是常规的单一患者级动态 rule。
- **[0:08:13–0:09:03]**：第二个特征：在观测数据中，医生可能已经在用这种人多决定方式，所以数据也不是 IID 的。因此，主流的动态治疗 regime 方法（它假设 IID 个体和简单约束 $\mathbb{E}[A_g] \le \tau$）不直接适用。Sarvet, Laurendeau & Stensrud (即将 arXiv) 的论文是在这个理想框架下工作的。
- **[0:09:07–0:09:43]**：小结：Mats 的框架要求同时面对“更复杂的 estimand（基于集群的 regime）”和“非 IID 观测数据”。他暂时不细讲识别细节，留作后续工作。

#### 模块 2：身份滑移与中介分析的系统综述 [0:09:46–0:34:22]

- **[0:09:46] Aaron 接手**：提出“空间”类比。有 **Q-空间**（研究者真正想问的因果问题）和 **P-空间**（数学上定义的因果参数）。因果革命把 P-空间中仅含关联参数扩展为包含多种因果参数，使 Q→P 映射更加丰富。
  - **[0:10:54–0:11:10]**：但问题出现了：P-空间可以被单独探索（methodologists 独立发明新参数，只关心它们的统计性质如可识别性、效率、零假设准则等），然后“后验”地尝试把新参数映射回 Q-空间。他质疑：这种映射是否够坚固/准确，还是重复了前因果时代“把关联当作因果”的不稳健映射？
- **[0:12:43–0:14:52] 通过中介分析的历史举例**：
  - 前形式期 (Pre-formal)：Wright (1920) 的路径系数、Baron & Kenny (1986) 的回归系数分解，后者已被批判混淆了关联与参数。
  - 形式期 (Formal)：Robins & Greenland (1992), Pearl (2001) 提出 NDE 和 NIE 的模型无关定义。但是 Avin et al. (2005) 证明了在常见的 recanting witness 结构（治疗引起的中介-结局混合）下，NDE 并非非参数可识别。
  - **[0:16:22–0:22:00] 实用期 (Pragmatic)**：大量替代参数被提出（RIA-NDE, separable effects, stochastic mediation estimands 等），它们被设计为“可识别”且具备良好统计性质。然后 Miles (2023) 和 Díaz (2023) 提出了 sharp mediational null criterion，发现许多实用参数不满足该准则（即使参数非零，也未必存在个体水平的间接效应）。
  - **[0:21:05–0:22:27]**：Aaron 提出核心假设：“当前的中介分析实用方法创造了身份滑移的认知条件”。
  - **[0:22:17–0:22:28]**：**正式定义 identity slippage**（见幻灯片：在模型 $\mathcal{M}_1$ 下识别参数 $\psi_1$ 的估计量 $\hat\psi_1$ 被用于声称属于另一模型 $\mathcal{M}_2$ 的不同参数 $\psi_2$ 的结论。即 I1–I4 条件）。
- **[0:23:16–0:25:14]**：引 van der Laan & Petersen (2008) 的推辞语（“若对 NDE 的识别假设不安，可把原文参数视为新目标参数”），说明这种“参数替换”是被鼓励的。
- **[0:25:16–0:27:05]**：**系统综述设计与结果**：
  - 目标人群：“Implementing the RIA-NDE（NDE 的随机干预类似物）”的应用文章。
  - 编码标准：如果文章在任何一节（方法/结果/讨论/摘要）至少有一个解释提到“我们估计的是一个随机干预中介参数，而不是 NDE”，该节标记为无错误；否则标记为存在身份滑移错误。
  - **结果严重性**：从 965 篇文书缩减至 16 篇完全审读的文章。**频率随文章节段递增**：在方法节错误率最低，在讨论节错误率最高（幻灯片展示了条形图，约占 80%+ 的应用文本在讨论节存在身份滑移）。而且方法学文化的文章（methods-authored）比非方法学文化的好一些，但仍显著。
  - **[0:26:48–0:27:05]**：回到有限资源案例——warns that 提出 I-DTR 再加一个简单边际约束 $\mathbb{E}[A_g] \le \tau$ 的这个套路，正在把有限资源问题“简化”成一个廉价的替代问题，存在与中介分析类似的身份滑移风险。

#### 模块 3：干预主义替代思路与最后反思 [0:27:22–0:43:27]

- **[0:27:22] Mats 再接手**：回到有限资源场景，以一个对比表格说明“标准框架”与“修改后框架”的差异：标准框架里超总体单位是个人（IID），修改后框架里超总体单位是“集群”（医院/病房），样本大小 n=1（实测只有一个集群），但 n 个患者个体之间因资源限制有因果联系。
  - 建议：虽然推断困难，至少这个陈述（把因果联系明确指出来、把 regime 定义在集群水平）已经是“理想路径”的第一步。对应论文 Sarvet, Laurendeau & Stensrud (unpublished)。
- **[0:31:00–0:32:16]**：转为对担心“中介分析是否对应于实际问题”的深入回应：
  - 反驳 Pearl (2001/2014) 以 NDE 作为歧视案件中标准参数的观点。核心例子：在雇佣歧视诉讼中问“若是不同的性别/种族，结果会如何？”——这个交叉式的 counterfactual（让一个人的 race 同时保持不变的 CV 且完全改变他的其他特征）难以操作化。
  - 替代：考虑一个更“动手”的问题：“如果把简历上的名字从‘平凡的黑人名字’改为‘平凡的西裔名字’（掩码判断，即 whiten the CV），被录用的概率会增加多少？” 这正是对 **intervening variable**（介子的体貌判断）的对照，而非对种族本身的对照。
- **[0:33:00–0:34:20]**：把这个想法通过向 DAG 添加一个结点（$A_M$）正式化：$A_M$ 是一个确定性等于 $A$ 但捕获了 $A$ 对 $M$ 影响的变量，实际可被改动（例如制度改变简历评审流程）。以此避开原 $A$ 的不可干预性问题。
- **[0:34:20–0:36:00] 延伸到识别公式**：
  - **[0:34:20–0:35:00]**：在 Wen, Sarvet & Stensrud (2023) 的假设（包括一致性、正性、无测混杂但在 $A\leftarrow Y$ 路径上允许混杂，即允许未处理混杂——这是重点不同！）下，识别公式即为 front-door formula。与其他参数（如 PIIE/Population Intervention Indirect Effect）在同一个 DAG 上公式相同，但识别逻辑（cross-world independence vs. 干预观点）不同。
  - **[0:36:35–0:41:40]**：举了一个反例：如果数据生成中 $A\rightarrow L$ （Pain \(A\) 影响 Depression \(L\)，然后 \(L\) 影响中介和结局），PIIE 不可识别，但 intervening variable 方法仍然给出同一个 front-door 公式（因为识别不依靠 recanting witness 禁止性）。用一篇真实的流行病学研究（Inoue, Ritz & Arah, 2022，关于慢性疼痛、阿片使用与死亡率——字幕可能有拼写错 Ihoue 等）作为例子：它想研究“慢性疼痛的 对死亡率的影响，通过阿片用药”。原本的诊断存在 Pain→Depression 或 Depression→Pain 的不确定性；但干预主义方法（研究“医生对病人疼痛的感知”如何影响处方行为）避开了这个问题，因为 $A_M$ 与 $L$ 之间无箭头。
- **[0:42:19–0:43:27] 总结**：
  - 不 “all pragmatism is bad”；但必须透明选择、并认识危险。
  - 理想路径（以问题为先，费神地形式化参数）不是布尔答案，而是一种优使（nudge）。
  - 结合具体例子见到，这种优使（a）强制想到切实可行的干预，(b) 引发新的识别结果，(c) 让估计值与可做的实验更接近。
  - 结束语：“要保守一些”，引用 FDA 层级决策锚定。

### 四、对应论文与开放问题

#### 4.1 这场报告对应的论文

- **核心诊段论文（系统综述部分）**：无最终标题/arXiv 号给出，但内容已被组织成一篇系统性综述（幻灯片标注“Population of applied articles implementing RIA–NDE”的结果）。作者系 Mats Stensrud 和 Aaron Sarvet（也可能合作者更多，待 arXiv 发布）。讲者至少一次提及 “paper that we will post on arXiv soon, not today but soon” [0:09:31]，但未提供任何链接或标题。注意：此稿至今可能未公开（“unpublished”）。必须从报告改为标注“即将公开”。
- **有限资源因果推断（集群 regime）**：Sarvet, Laurendeau, & Stensrud. “Optimal treatment allocation under constraint-induced interference.” 同上“on arXiv soon, manuscript available upon request”。
- **Intervening variable 方法**：Lan Wen, Aaron L Sarvet, & Mats J Stensrud. “Causal effects of intervening variables in settings with unmeasured confounding.” arXiv:2305.00349 (2023). 已经公开。
- **分离效应（Separable effects）**：Stensrud et al. “Separable effects for causal inference in the presence of competing events.” *Journal of the American Statistical Association*, 2020；Stensrud et al. “Conditional separable effects.” arXiv:2006.15681 (2020). 这些在幻灯片中列出，是讲者原团队对“干预主义中介分析”的贡献。

#### 4.2 开放问题（扎根于转写）

- **[0:04:55–0:05:02] 对中介分析中“精准实用参数”与“实际问题的对应关系”缺乏严格形式化**：报告提到“这些参数真的是同等的问题吗？它们之间的值可以相差很大”（[0:21:30–0:21:59]）。但是未给出量化的方法（例如敏感性分析工具，测度“如果参数的选择不同，结论稳不稳健”）。这是一个潜在的统计工具问题。
- **[0:08:28–0:09:10] 在有限资源框架中，观测数据非 IID**（因医生决策参考了其他患者的特征）。Mats 明确说“identifaction 在不 iid 数据上往往比常规设置更困难”。这个问题在现在已知的 interference literature（隐马尔可夫 / 网络模型）里不充分吻合（因为这里的一个“集群”绝大多数因果链接是通过排位产生的，而非社交网络连接）。这提供了一个建模 & 为识别设计新 estimator 的机会。
- **[0:14:52–0:15:00] 关于 sharp mediational null 的适用性**：报告指出很多实用参数不满足此标准，但未讨论：是否所有因果分解都必须满足该标准？在公共健康决策中是否存在可接受“较弱的”零假设？这仍是一个开放的哲学/方法论问题。
- **[0:26:48–0:27:05] I-DTR（有限资源）的身份滑移风险只被提出来，没有系统综述实证数据**。这部分（有限资源的类比）目前只有假设性论证，缺少类似中介分析的实证支持。Sarvet & Stensrud 的论文目前未公开，暂时只有 marco-level 的设计图样。如果研究者想跟进，可以做一个类似的文献回顾：“In practice, how often are I-DTR with simple marginal constraint interpreted as if they had addressed the full limited-resource problem?”
- **[0:42:39–0:43:27] “如何测量身份滑移的实际公共健康后果”**：讲者 Aaron 自己直说“我们不知道，这是极其艰巨的经验性问题”。这是一个很漂亮的“problem for future research”——把方法论元检验做成估算的**一体**。

以上每个开放问题都有对应的转写线索引，确保了“生于这场报告的问题发现”，不含讲者未言的推理。研究者可以根据自己的武器库选择切入——如对有限资源框架感兴趣，可以试探其统计识别（与集群水平 U-statistics / tensor-contraction 视角能否交叉？）；或用 half cancer 方法可做敏感性分析来量化身份滑移的后果。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

