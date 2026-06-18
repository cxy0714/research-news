# Causal reasoning in survival and time-to-event analyses

**讲者**: Vanessa Didelez  
**讨论人**: Els Goetghebeur  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-12-01  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=5dMdNGZGVR8&feature=youtu.be> · [幻灯片](https://drive.google.com/file/d/1uLGzs2I_MYJbpRTBZfkGchkRoTMnhgMv/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告把 **生存/时间-事件分析（survival / time-to-event analysis）** 放到 **因果推理** 的框架里，核心追问是：**当“因”到“果”之间可能有大量事件发生（中介、竞争事件、治疗改变、删失）时，如何定义、识别和估计有意义的因果 estimand？**

**背景与已有路线**：
- 经典生存分析关注 hazard ratio、Kaplan–Meier 曲线，但这些量的因果解释在 2010 年后受到系统性质疑（Hernán 2010; Aalen et al. 2015; Martinussen et al. 2020）。问题在于 hazard 条件于存活者集合，即使是在随机试验中，hazard ratio 也可能产生选择偏倚（“survivor selection bias”）。
- 针对“因与果之间发生的事情”，流行病学与因果推理文献有两条主流路线：
  1. **因果中介分析**（Robins & Greenland 1992; Pearl 2001）：基于嵌套反事实的自然直接/间接效应。但对生存结局和连续时间中介过程，自然效应定义本身有问题（Didelez 2019; Fulcher et al. 2021）。
  2. **竞争事件** 的处理：常见做法是把竞争事件当作删失（即“cause-specific hazard”或“subdistribution hazard”），但这隐含着对竞争事件进行不可置信的“消除”式干预（Young et al. 2020）。

**这场报告的位置**：
- 讲者 Didelez 与她合作者（Aalen, Røysland, Stensrud, Hernán, Robins 等）提出 **可分离效应（separable effects）** 作为第三条路线。它的思想是：**将处理分解为两个（或多个）可分离的组分**（比如 placebo trial 中“药丸外观” vs “活性成分”），分别对应激活不同因果路径的机制。这允许定义一种新的 estimand——**在保持某一组分不变时改变另一组分的反事实分布**——它避开了自然效应的跨世界假设（cross-world counterfactual），且在可分离假设下从观测数据可识别。
- 可分离效应最初由 Robins & Richardson (2011) 在因果图框架下提出，Didelez 将其扩展到 **标记点过程（marked point processes）** 和 **连续时间/生存结局** 的情境，形成了系统的识别理论（Didelez 2019; Stensrud et al. 2020a,b）。
- 报告还介绍了 **折叠图（folded graphs）** 或 **局部独立图（local independence graphs）**，这是 Didelez 及其合作者发展的一套处理连续时间过程的图形工具（Didelez 2008; Eichler 2012; Mogensen et al. 2018），用于形式化“哪个过程的过去影响哪个过程的现在”的依赖性。

**关键参考文献**（来自幻灯片末尾，转写确认）：
- Hernán, M. A. (2010). The Hazards of Hazard Ratios. *Epidemiology*.
- Aalen et al. (2015). Does Cox analysis yield a causal treatment effect? *Lifetime Data Analysis*.
- Martinussen et al. (2020). Subtleties in the interpretation of hazard contrasts. *Lifetime Data Analysis*.
- Didelez (2019). Defining causal mediation with a longitudinal mediator and a survival outcome. *Lifetime Data Analysis*.
- Stensrud, Young, Didelez, Robins, Hernán (2020a). Separable Effects for Causal Inference in the Presence of Competing Events. *JASA* (to appear at time of talk).
- Stensrud, Tchetgen Tchetgen, Didelez, Robins, Hernán, Young (2020b). Generalized interpretation and identification of separable effects. *arXiv*.
- Young, Stensrud, Tchetgen Tchetgen, Hernán (2020). A causal framework for classical statistical estimands in failure-time settings. *Statistics in Medicine*.

### 二、最小内核 / 一个最简例子

**符号与模型**（以报告中最干净的特例——二元基线处理、单个离散时间中介、事件结局为例）：

- **可观测数据**：对每个个体，观测到 \( (A, M_1, Y_2) \)。
  - \( A \in \{0,1\} \)：基线处理（如随机化），观测中 \( A = A_M = A_Y \)（处理是不可分的整体）。
  - \( M_1 \in \{0,1\} \)：在第一个时间点的中介状态（如副作用是否发生；只有在个体还活着时才定义）。
  - \( Y_2 \in \{0,1\} \)：第二个时间点的结局（如是否死亡；\( Y_2 = 1 \) 表示死亡）。
- **潜在不可观测量**（在因果推理中）：每个个体有多个潜在结局，取决于处理值。
- **Estimand**：报告关注的是 **可分离效应**。假设处理可分解为两个组分 \( A = (A_M, A_Y) \)：
  - \( A_M \)：激活/抑制中介过程的组分（如 placebo trial 中的“是否相信自己是治疗组”）；
  - \( A_Y \)：影响结局的组分（如“是否实际接受活性成分”）。
  观测上 \( A_M = A_Y = A \)，但反事实定义允许将它们设为不同值。
  **目标的 estimand**：
  \[
  P(Y_2 = 1; \text{do}(A_Y = a, A_M = a^*))
  \]
  即固定 \( A_Y = a \)、\( A_M = a^* \) 时的反事实死亡概率。
  - **可分离直接效应**：固定 \( a^* \)（如 \( a^* = 0 \)），让 \( a \) 在 0 和 1 之间变。
  - **可分离间接效应**：固定 \( a \)（如 \( a = 1 \)），让 \( a^* \) 在 0 和 1 之间变。

**最简识别例子**（幻灯片第 27 页“meditational g-formula”）：
- **两个关键假设**（条件于基线协变量 \(C\)；为简化暂时忽略 \(C\)）：
  1. \( M_1 \perp\!\!\!\perp A_Y \mid A_M = a^* \)：中介过程只取决于 \( A_M \)，与 \( A_Y \) 在给定 \( A_M \) 下独立。
  2. \( Y_2 \perp\!\!\!\perp A_M \mid A_Y = a, M_1 \)：结局只取决于 \( A_Y \)（和中介 \( M_1 \)），与 \( A_M \) 在给定 \( A_Y, M_1 \) 下独立。
- **识别公式（survival mediational g-formula）**：
  \[
  P(Y_2 = 1; \text{do}(A_Y = a, A_M = a^*)) =
  \sum_{m_1} P(Y_2 = 1 \mid Y_1 =0, M_1 = m_1; \text{do}(A = a)) \cdot
  P(M_1 = m_1 \mid Y_1 =0; \text{do}(A = a^*))
  \]
  这里 \( Y_1 = 0 \) 指第一时刻存活；观测到的处理 \( A \) 等于反事实中对应的组分。因此这个 estimand 由观测数据（只看到 \( A=0 \) 或 \( A=1 \) 的试验臂）就可识别：**分母项来自 `do(A=a*)` 下的中介分布，分子项来自 `do(A=a)` 下的结局（给定中介和存活）**。

**为什么这个例子是最小内核**：它避免了连续时间、多时间点的复杂性，直接展示了可分离效应的核心思想——通过“将处理分解为两个机制的操控”，把“反事实分布从两个不同的世界（一个设定 \(A\)，另一个设定 \(A^*\)）拼接起来”。这与自然中介效应完全不同（后者需要一个“保持中介与处理干预不一致”的跨世界反事实）。

### 三、报告主体：讲者讲了什么

**[0:00–0:14] 引言与动机**
- 讲者从“因先于果，但中间可能有其他事发生”出发，列举了三种场景（非依从性、竞争事件、副作用），并引出 ICH E9 附录中的“intercurrent events”术语。
- 指出 **删失**（censoring）是生存分析特有却又复杂的挑战：即使只有管理性删失（administrative censoring），它也不一定独立于结局（因为日历时间的变化可能改变入组人群特征）。

**[0:14–0:26] 第一部分：基础设置、折叠图、独立删失**
- **Estimand**：报告主张以 **干预生存曲线** \( P(Y > t; \text{do}(A = a)) \) 或 **干预累积发病率** 作为总因果效应的目标，而非 hazard ratio。
- **识别**：在随机试验中，若（a）时间-事件定义不依赖于中间事件，（b）删失独立，则可通过 arm-specific Kaplan–Meier 估计。在观测研究中，需额外控制混淆（定义好 time-zero，并推荐 **target trial emulation** 原则，引用 Garcia-Albeniz et al. 2017）。
- **折叠图**（[0:18–0:26]）：讲者引入 **folded graphs** 表示时间序列过程之间的依赖。节点代表过程（如 \( X_t, Y_t, Z_t \)），边代表“该过程的过去是否影响另一个过程的现在”。优势：紧凑表达。关联概念是 **δ-separation**（非对称门的图分离标准）。这一节给出了 Didelez (2008) 和 Eichler & Didelez (2010) 等奠基工作。转写中 ASR 将“folded”误作“folded”，已校正。
- **独立删失**（[0:26–0:30]）：通过折叠图展示：独立删失对应于“删失过程 C 的过去不直接或通过混杂影响结局过程 Y”。删失过程的“因果效应”通常更强于**未观测的混淆**（如 U 同时影响 C 和 Y）。这是条件独立删失的动机：若能观测 U，可调整。

**[0:30–0:45] 第二部分：可分离效应（核心贡献）**
- **中介过程与生存结局的冲突**（[0:30–0:38]）：经典的“自然”直接/间接效应嵌套反事实在生存分析中定义有问题——因为中介过程（如侧效应）的存在依赖于存活状态（Didelez 2019）。在多时间点情境下，从处理到中介再到结局的路径与直接路径共享“先验存活”节点，导致自然效应不可识别。
- **可分离效应思想**（[0:38–0:45]）：
  - 假设处理具有两个物理或概念上可分离的组分 \( A_M \)（激活中介机制）和 \( A_Y \)（激活结局机制），观测上二者相同。
  - **目标 estimand**：\( P(Y > t; \text{do}(A_Y = a, A_M = a^*)) \)。
  - 例子：双盲 RTC 中，\( A_M \) 是“服药行为”（placebo 效应），\( A_Y \) 是“活性成分”。绿色效应既是实际可分离的（因为双盲试验设计）也是直觉上合理的。
  - **重要性质**：这不是跨世界假设（cross-world）。讲者在 [0:42–0:45] 的 Q&A 中明确回应了观众的问题，指出假设 1 和 2 仅在 **同一个反事实世界** 中定义处理组分，即可通过实际的可分离试验（如双盲加安慰剂）检验。
- **识别假设与 mediational g-formula**（[0:45–0:53]）：
  - 假设 1（中介只取决于 \( A_M \)）：\( M_t \perp\!\!\!\perp A_Y \mid \bar{M}_{t-}, N_{t-}=0, A_M=a^* \)
  - 假设 2（结局只取决于 \( A_Y \)）：\( N_t \perp\!\!\!\perp A_M \mid \bar{M}_{t-}, N_{t-}=0, A_Y=a \)
  - 识别公式：生存 mediational g-formula（幻灯片第 27 页，转写仅提到“拼接”）：
    \[
    P(Y>t; \text{do}(A_Y=a, A_M=a^*)) =
    \sum_{\bar{m}_t} \prod_{s=1}^t P(N_s=0 | \ldots; \text{do}(A=a)) P(M_s=m_s | \ldots; \text{do}(A=a^*))
    \]
    第一项来自处理 = \( a \) 的观测臂（控制 \( A_Y \)），第二项来自处理 = \( a^* \) 的观测臂（控制 \( A_M \)）。
  - **违反假设的情况**（[0:53–0:58]）：处理不可分离、中介测量不充分、存在中介-结局混淆的未观测因素（即“recanting district”——Shpitser 2013）。若后者被观测到，可恢复识别。
- **示例：加性风险模型 + 线性中介模型**（[0:58–1:08]）：
  - 假设条件风险 \(\lambda_t = \mu_t + \alpha_t A + \beta_t \bar{M}_t + \rho'_t C\)
  - 中介模型 \( E[M_t | \ldots] = \gamma_t A + \delta'_t C + \sum_{s<t} b_{ts} M_s \)
  - 得到可分离直接/间接效应为 **相对生存（relative survival）** 的简洁公式：
    \[
    SDE: \exp\left\{ (a^* - a) \int_0^t \alpha_s ds \right\}, \quad
    SIE: \exp\left\{ (a^* - a) \int_0^t \beta_s \tilde{\gamma}_s ds \right\}
    \]
    其中 \(\tilde{\gamma}_t\) 是边际中介模型中的处理系数（边缘化中介过程）。
  - 应用：SPRINT 数据（抗高血压药 → 肾脏衰竭时间；中介：舒张压）。可分离假设较牵强（因为是“通过舒张压 vs 其他机制”），但计算简单。结果：直接效应主导。
- **可分离效应在竞争事件中的应用**（[1:08–1:16]）：
  - 两个事件 \( e_1 \)（癌症死亡）和 \( e_2 \)（其他原因死亡）。经典 estimand 是事件特异性累积发病率 \( F^k(t;a) \)。
  - 常见做法（将 \( e_2 \) 作为删失）对应“消除 \( e_2 \)”的干预，即控制直接效应——但假设往往不现实（人无法消除死亡）。
  - 可分离效应：将处理分解为 \( A_Y \)（影响 \( e_1 \) 路径）和 \( A_M \)（影响 \( e_2 \) 路径）。目标 estimand：\( F^1(t;a,a^*) = P(T \le t, E=e_1; \text{do}(A_Y=a, A_M=a^*)) \)。
  - 示例：前列腺癌治疗数据（治疗对肿瘤相关死亡有益但对其他原因死亡有害）。可分离假设：治疗成分分别对应“睾酮抑制剂”（\( A_Y \)）和“雌激素诱导的其他效应”（\( A_M \)）。结果：可分离间接效应小，直接效应大（Stensrud et al. 2020a）。
- **扩展**（[1:16–1:18]）：时间依赖/治疗后混淆（Stensrud et al. 2020b）、连续时间（Martinussen & Stensrud 2020）、与主分层 estimand 的替代关系（Stensrud et al. 2020c）。

**[1:18–1:26] 第三部分：展望——基于标记点过程的统一框架**
- **标记点过程形式化**：过程用计数过程 \( N_t^k \)（事件类型 \( k \)），其可分解为可预测补偿子（compensator）和鞅。
- **局部独立图（folded graphs）**：给出一套形式化工具定义“过程 j 的过去是否影响过程 k 的现在”（j ↛ k 当且仅当补偿子在省略含 j 的滤子下不变）。这是非对称独立性定义。
- **因果有效性（causal validity）**：若对处理过程 \( N^A \) 的强度进行随机干预（stochastic intervention），其余所有过程的强度保持不变，则图谱有效。
- **识别**：基于因果有效性、独立删失假设，得到识别公式：通过 **重加权**（reweighting）由观测数据计算干预分布（移除删失、改变处理强度）。权重是观测强度与干预强度之比的似然乘积（幻灯片第 48 页）。
- **数据示例**（[1:24–1:26]）：宫颈癌筛查中，HPV 检测本身对 CIN2+ 发病率无因果效应，但不同供应商的检测频率不同。通过将频率定义为处理过程，施加“使频率相等”的干预后，期望看到发病率一致（否则表明供检测准确性差）。

### 四、对应论文与开放问题

**(a) 对应论文（来自幻灯片关键参考文献，转写基本确认）**：
1. **Didelez, V. (2019)**. Defining causal mediation with a longitudinal mediator and a survival outcome. *Lifetime Data Analysis*, 25, 593–610. —— 奠基可分离效应在生存中介中的应用，定义识别条件与 mediational g-formula。
2. **Aalen, O.O., Stensrud, M.J., Didelez, V., Daniel, R., Røysland, K., Strohmaier, S. (2020)**. Time-dependent mediators in survival analysis: Modeling direct and indirect effects with the additive hazards model. *Biometrical Journal*, 62, 532–549. —— 加性风险+线性中介模型的闭合形式表达。
3. **Stensrud, M.J., Young, J.G., Didelez, V., Robins, J.M., Hernán, M.A. (2020a)**. Separable Effects for Causal Inference in the Presence of Competing Events. *JASA* (to appear). —— 竞争事件下的可分离效应。
4. **Stensrud, M.J., Tchetgen Tchetgen, E.J., Didelez, V., Robins, J.M., Hernán, M.A., Young, J.G. (2020b)**. Generalized interpretation and identification of separable effects in competing event settings. *arXiv*. —— 允许时间依赖/治疗后混淆的广义可分离效应。
5. **Røysland, K., Ryalen, P., Nygard, M., Didelez, V.** (in preparation). Graphical criteria for identification in continuous-time marginal structural survival models. —— 基于标记点过程与折叠图的识别准则。
6. **Didelez, V. (2008)**. Graphical models for marked point processes based on local independence. *JRSS(B)*, 70(1), 245–264. —— 折叠图 / 局部独立图的形式化。

**(b) 开放问题（来自报告的线索与转写中的模糊点）**：

1. **可分离组分的实际构造**（[0:40–0:45] 多个例子，[0:53] 讨论中薛定谔的“separability”）：讲者提到许多例子（双盲、大麻、减肥项目、乳腺癌筛查），但如何 **在给定实际处理时，先验地论证“可分离假设 1 & 2 是否合理”**，似乎没有一般性指导。转写中 Els 的讨论强调了“治疗通常与大量其他成分交互”的困难（[1:26–1:33]）。这对应一个核心开放问题：**是否存在数据驱动的可分离性检验？** 或 **仅有部分分离时，敏感度分析（sensitivity analysis）如何构造？**

2. **中介-结局混杂（“recanting district”）的完整处理**（[0:53–0:55]  Eric 的提问与简短回应）：转写中讲者承认“若 U 是治疗后且被处理影响，则需要第三组分...有论文正在处理”。这意味着 **即使在可分离框架下，面对时间依赖/治疗后混杂，也未完全解决**。当前的扩展（Stensrud et al. 2020b）提出了广义解释，但 line 上是否总能构造足够多的处理组分或者需要其他假设（如“主分层”或“一致性假设的类型升级”）？

3. **连续时间下的完整识别理论**（[1:18–1:26] 第三节，幻灯片的“lots of filtrations, martingales and measure theory”）：讲者的参考资料 “Røysland et al. (in prep.)” 是进行中的工作。基于标记点过程的识别准则（图形化）以及重加权估计量的渐近性质（如一致性、收敛速率、渐近方差）尚未公开。研究者陈星宇若对高维统计/半参数效率感兴趣，可关注 **这一框架下 debiased ML / 效率界问题**：当处理过程是高维时，是否需要降维或稀疏假设？

4. **实际应用的障碍**（Els 的讨论，转写 [1:26–1:33]）：生存分析实践者常忽略竞争事件和删失的独立性假设，且高层期刊也频现错误。报告的答案是“可分离效应促使思考更深入”，但 **如何将其转化为易懂的实践指南**（除了“separability 概念上的帮助”），尤其在观测数据中需要验证假设的系统性方法上，仍然是开放问题。

5. **可分离 vs 主分层 estimand**（[1:16–1:18] 提及 Stensrud et al. 2020c）：讲者提到可分离效应也可作为主分层 estimand 的替代。在竞争事件中，两者关系具体如何（哪个假设更弱？哪个估计更稳健？）——这是一个值得进一步比较的 open problem。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

