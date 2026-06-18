# ocis-2021-02-02-interview-with-james-robins

**讲者**: Interview with James Robins  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2021-02-02  
**主题**: 因果推断  
**视频**: <https://youtu.be/j26nYFxRJr0>

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这不是一场标准的学术报告，而是2021年OCIS（Online Causal Inference Seminar）对James Robins的专题访谈。**它不是介绍某一篇新论文或一个特定结果，而是回顾Robins整个职业生涯的工作线——他如何从一位没有统计背景的临床医生成长为因果推断领域的奠基人，以及他对该领域现状与未来的看法。**

这场访谈可以被视为**因果推断方法发展史的一次口述**，站在当前（2021年）回望：
- **子方向**：Robins及其合作者（Andrea Rotnitzky, Sander Greenland, Thomas Richardson, Ilya Shpitser, Miguel Hernán等）开创的**基于反事实（counterfactual/potential outcomes）的因果推断体系**，核心包括：G-computation（G公式）、逆概率加权（IPW）、双稳健估计（doubly robust estimation）、半参数效率理论（专题：估计任意光滑功能的影响函数）、时间相依混杂的处理、以及SWIGs（单世界干预图）对因果图的统一。这与用户的“causal inference, semiparametric theory, efficiency theory”重叠度高。
- **方向追问的问题**：观测数据中，当我们有**随时间变化的暴露与混杂因素**（time-varying exposure and confounding），传统方法（如分层、标准回归）会因“健康工人幸存者偏倚”一类结构而失效，因为**一个时间点的混杂变量同时是先前暴露的结果**，从而阻塞了因果路径导致两难。Robins的核心贡献是：正式定义了因果效应（反事实）、提出了在**序贯条件可忽略性**下的识别与估计方案（G-formula, IPW, 结构嵌套模型），并将其拓展到了含有缺失数据的半参数理论。
- **当前frontier（Robins在访谈中提及）**：
  - 单位干扰（interference）
  - 未测量混杂（proximal causal inference, Eric Tchetgen Tchetgen的工作）
  - 深度学习在因果推断中的角色（如Caroline Uhler的工作）
  - 因果发现 / 搜索（嵌套马尔可夫模型、不变性推理）
  - **高阶影响函数（higher-order influence functions）**：用于在估计偏差小于标准误时提供更可靠的置信区间。这与用户“HOIF”和“high-order U-statistics”兴趣直接对齐。
  - **诊断测试情境下的巨大效率增益**（利用“诊断本身不影响生存”这一结构约束，使方差缩小50倍）。
- **用户兴趣关联**：这场访谈本质上是理论资源的蓝图。Robins指出高阶影响函数是尝试在最小假设下去评估双机器学习等方法的覆盖率的候选工具。这与用户对HOIF、效率边界、DM-L的研究兴趣有明确的重叠。但访谈不只是讲技术细节，而是讲述这些思想产生的**动机与演化**。

### 二、最小内核 / 一个最简例子

**核心问题**：在纵向观测数据中，要估计随时间变化的暴露A(t)对终点Y的因果效应，而存在随时间变化的混杂变量L(t)既受先前暴露影响也会影响后续暴露。这是典型的**健康工人幸存者偏倚（healthy worker survivor effect）** 或更一般的**时间相依混杂（time-varying confounding）**。

**符号与模型**（2个时间点 t=0,1 的最简版本）：
- **可观测数据**：对于第i个个体，我们观测到 \( (L_0, A_0, L_1, A_1, Y) \)，其中：
  - \(L_0\)：基线混杂变量（如年龄、基线健康）
  - \(A_0\)：初始暴露（二值：1=暴露，0=不暴露，如在化工厂工作）
  - \(L_1\)：时变混杂变量（如健康指标CD4或“是否离职”），它可能受A_0影响，也会影响A_1
  - \(A_1\)：后续暴露（二值）
  - \(Y\)：终点结局（如死亡/发病，二值或连续）
- **潜在不可观测量**：
  - 反事实结局：\( Y(a_0, a_1) \) 表示如果暴露序列被强制设为\((a_0, a_1)\) 时个体将经历的结果（极端假设）。
  - 要估计的目标量（estimand）通常是反事实结局的均值：
    \[ \psi = E[Y(a_0=1, a_1=1)] - E[Y(a_0=0, a_1=0)] \]（连续暴露下整个生涯都暴露 vs 都不暴露的效应）或更一般的“动态”干预参数（如“在某个阈值下继续/停止治疗”）。
- **识别假设**：我们需要在观测数据中用条件分布表达反事实均值。核心假设是**序贯条件可忽略性（sequential conditional exchangeability）**：
  - \( Y(a_0, a_1) \amalg A_0 \mid L_0 \)
  - \( Y(a_0, a_1) \amalg A_1 \mid (L_0, A_0, L_1) \)
  - 即给定已观测到的过去，暴露是“与未来的（反事实）结局无关”的，决定准随机化。
- **G-computation公式（G-formula）**：在上述假设下，期望可以被识别为：
  \[
  E[Y(a_0, a_1)] = \int_{l_0, l_1} E[Y \mid L_0=l_0, A_0=a_0, L_1=l_1, A_1=a_1] \times f(l_1 \mid L_0=l_0, A_0=a_0) \times f(l_0) \, dl_0 dl_1
  \]
  这其实是一个标准的反事实识别公式：需要**模型化结局的条件均值**（结局回归）与**时变混杂变量的条件分布**（中间变量的转移概率）。

**为什么传统方法会失败？**
- 若直接标准Cox回归只包含累积暴露与基线协变量：忽略了时变混杂L_1（如离职），因L_1是暴露导致的健康损伤路标没被考虑，从而低估了暴露效应。
- 反之，若将L_1也纳入为一般协变量：L_1是暴露的中间结果（暴露->疾病->离职->不暴露），调整它就把部分因果路径（暴露通过L_1对Y的效应）给“调掉了”，导致效应低估。
- 这就是Robins所说“damned if you adjust and damned if you don’t”的本质。

### 三、报告主体：讲者讲了什么

**[0:00-0:02] 开场与介绍**：主持人Andrea Rotnitzky介绍James Robins（简称Jamie），概述其贡献：定义“科学界对待时间相依暴露与治疗在观察与非完美随机研究中的因果推断的方式”，以及缺失数据和半参理论。

**[0:02-0:12] 动机起源**：Robins作为耶鲁实习医生（留着一头长发），在工会诊所工作，为工人群体作证 **"more probable than not that the person's exposure at work caused their illness"**[0:03:39-0:03:46]。这引发了他对因果关系量化与证据的理解。

**[0:04-0:09] 自学统计学的关键转折**：
- 曾学Ed Leamer的《Specification Searches》[0:06:11-0:06:18]：这本书用贝叶斯反向工程的方式拆解了当时流行的（无头绪的）变量选择流程，让他第一次觉得统计学有意义。[0:06:49-0:07:01] "All of a sudden there was somebody making sense in this crazy world."
- 后读Cox和Hinkley的《Theoretical Statistics》[0:07:55-0:07:58]——“这是一个全新的世界。这是数学，但它有统计学的特定东西（似然原理、条件性原理等）。”
- 核心计划：把流行病学家Olli Miettinen 的直觉规则翻译为**形式数学统计学的语言**。[0:09:18-0:09:22] 例如，Efron & Hinkley关于“观测信息 vs 期望信息”的论文[0:10:01-0:10:11]，发现在流行病学中人们早在15年前就已经做了“条件于观测关联”的方差估计。这是两个群体（统计学家、流行病学家）互不沟通却达到同一结论的典型案例。

**[0:12-0:24] 早期的变迁与出版困难**：
- 在“因果”一词在布斯或生物统计界是**禁忌**的年代（"You were not allowed to use the word causality" [0:13:03-0:13:05]），Robins的所有伟大想法都只能发表在工程学期刊上或被拒绝。
- 确定核心问题：**“健康工人幸存者偏倚”（healthy worker survivor effect）**。[0:14:25-0:16:38] 关键例子：Ethel Gilbert提出了这个困境。工厂工人患肺病时离职不再累积暴露，但调整“离职”会阻塞暴露->L1->Y的通路，分为弊病调出。传统方法不能同时解决这两个问题。
- 结果在世界第一梯队统计期刊遭遇激烈拒稿：在Biometrika（Sir David Cox任主编）被拒，与Cox面谈时，Cox道：“Your paper sounds interesting but it would take me three months to read it... I have to go by the referees.” [0:19:10-0:19:28] 多年后Cox在Cutter讲座上说这是他最遗憾的事之一。[0:20:22-0:20:28]
- 关键的伯乐：Sander Greenland（流行病学教研室）完全通晓并赞赏他的工作，帮助在流行病学渠道发表。[0:22:31-0:22:55] 1987年的长论文（关于时间相依因果理论与G公式）最终发表在工程学期刊上。

**[0:24-0:28] 缺失数据突破与双稳健估计**：
- 意识到“缺失数据即是因果推断”，反之亦然。因为在生物学上下文中，失访/审查（censoring）就是在时间点上的“是否观察到”，它相当于另一组离散——若否定规则（forced to be uncensored）相当于否定暴露（forcing treatment）。[0:25:00-0:25:12]
- 意识到**逆概率加权（IPW）与G公式的对偶关系**；通过研究缺失数据的半参数理论，自然得到了影响函数形式。自1992/1994年与Rotnitzky的合作，在影响函数中，出现了double robustness结构：只需在治疗模型（propensity score）或结局回归模型中有一方正确，估计仍是一致的。[0:28:10-0:28:44]
- 在1990年的JASA论文讨论中，他们将DR正式化，并在后续泛化到更复杂的“非随机缺失（MNAR）”模型——这也成为与Rotnitzky及Ezequiel Smucler最新Biometrika合作的基础。[0:32:10-0:32:16]

**[0:32-0:40] 因果图神话与SWIGs的独创**：
- 论争与两极化的画面：Pearl（图方法）与反事实观点之间的联系。Robins坚称“任何方法学家都应该能说两种语言”。[0:33:23-0:33:40]
- 核心武器：**SWIGs**（Single World Intervention Graphs）。[0:36:31-0:36:35] 用口语描述：
  - 先把治疗变量A分裂成两个：“随机A” (大写, 表示实际世界中观察到的A) 与“干预A” (小写, 如a=0, 固定了值)。
  - 只保留一个世界：干预后的世界。在该图中，只有随机A与反事实结局Y(a=0)是随机变量；它们之间的d-分离性完美编码了反事实的“无混杂”条件。
  - Robins认为 **"SWIG is the bridge"**——用统一的语言（d-separation + 反事实）就能匹敌所有已经被图形法建立的识别结果（back-door, front-door, 中介分析）。[0:39:27-0:39:35]
- 最新进展（2021年左右）：与Thomas Richardson和Ilya Shpitser的两篇arxiv论文，展示了SWIGs应用于一般因果图的巨大能力。

**[0:40] 观众提问：最大开放问题** （Eric Tchetgen Tchetgen 提问 [0:41:09]）
- 干扰（interference）网络效应。[0:42:18-0:42:22]
- 未测量混杂：“这是计算机科学家用深度学习、自编码器当黑箱来‘控制未测量混杂’的时代——这不可能没有假设。Eric的‘proximal causal inference’是我见过最严谨、最酷的版本。”[0:43:00-0:44:19]
- 对于这么多方法，**如何在实际工作中判断它们有效？** 这是一个元科学问题。
- 深度学习 / 基因因果网络重建（Caroline Uhler等人的工作）。[0:46:20-0:46:42]
- 因果结构发现：嵌套马尔可夫模型、不变性推理（invariant causal prediction，ETH）[0:47:00-0:47:18]

**[0:48-0:52] 成功案例：HIV用药效果**：
- 因为存在严重的“治疗指征混杂”（医生倾向于给最重的病人用药），在标准模型中用Cox回归得到的是 **刚好相反的结果**（用药“有害”或无效）。而当使用G公式 / IPW 调整时间变化混杂后，结果与随机对照试验完全一致。这使得整个HIV临床界最终接受了这些方法。[0:52:34-0:52:47]

**[0:53-0:58] 当前主要研究方向**：
- **诊断测试的黑色十字冲击（black box diagnostic test）**：刚理解的一个结构——诊断本身（如CT扫描）对生存无直接效应，只通过改变治疗方案起作用。利用这个零假设，2018年左右的工作（与Wen Wu和Sean Zhao）得到了一个**方差减少50倍的效率增益**。这是极其罕见的统计学效率跃升。[0:54:58-0:55:06]
- **有效推断在ML之后**：双机器学习（DML / cross-fitting）仍会出现偏差。Robins的思路转向“如何用假设检验或置信区间的覆盖正确性”——这需要用到**高阶影响函数（higher-order influence functions, HOIF）**。[0:55:54-0:56:18] 他试图回答：“在最小假设下，高阶影响函数能否改进有限样本性质？”[0:57:00-0:58:10] 并提到Tchetgen也有相关工作，但他（Robins）更想构建无附加强假设的最小底气方案。

**[0:58-1:00] 1986-87论文的摘要**：
- **关键词**（自读）：Causal questions in English become mathematical conjectures about the parameters of a causal **interventional structural tree graph** under certain **non-identifiable assumptions**。[0:59:10-0:59:40]
- 这是因果推断从口头变数学的一种哲思。

**[1:00-1:03] 训练建议**：不需要“垂直隔离”，因为聪明的年轻人应当同座于Riff, a good day就能让人弄懂多年前天书般的概念；而在全球化背景下生源素质空前提升，但要注意避免被孤立成小岛。

### 四、对应论文与开放问题

**（a）本报告可能提及的论文**：
- **开创性工作**：Robins 1986, 1987年关于时间相依因果效应与G公式的工程学期刊论文（具体刊名在转写中未明确，但可能是 *Statistics in Medicine* 或 *Computers & Mathematics with Applications* 等处，待查）。
- **双稳健的开端**：Robins, Rotnitzky 1992 (coarsening at random paper, Biometrika-like) 及Robins, Rotnitzky, van der Laan (1994 JASA) 关于缺失数据中DR结构。但转写中提及“讨论文章”是1999 JASA讨论的回应。[0:30:47]
- **SWIGs统一工作**：Richardson & Robins (2013); 和2020/2021的Richardson, Robins, Shpitser arxiv论文（关于SWIGs的完全泛化，转写仅提“recent two papers in arxiv”）。
- **最新Biometrika合作**：Rotnitzky, Smucler, Robins (2020/2021) 关于非随机缺失（MNAR）模型中的双稳健性质。[0:32:10-0:32:16]
- **诊断测试增益**：Wu, Zhao, Rotnitzky, Robins (近在发表中) 关于“无直接效应的诊断标记导致的巨量方差削减”。
- **高阶影响函数**：Robins及其合作者（可能包括Mark van der Laan）的连续工作——尚未明确单篇。
- **Tchetgen的proximal causal inference**：Tchetgen Tchetgen等 (2020/2021), 被Robins高度评价“最严谨”。

**（b）开放问题（根植于转写）：**
1. **如何在实际应用中严肃评估各个不同因果方法间的性能？**（[0:44:35-0:44:44]）——这是一个跨领域的元科学问题：提出了新方法的人没有动力检验它的实用性。
2. **高阶影响函数能否在最小假设下改善置信区间的覆盖？**（[0:57:29-0:58:10]）——Robins自己正在在这个前线上投注主要精力。
3. **当有大量未测量的混杂时，我们能否系统地评价哪类专业假设（近端因果推断 / 深度学习方法 / 不变性因果预测）是可行的？**（暗示需要在模型复杂性、可验证性和实际数据质量之间取舍）[0:43:00-0:45:25]。
4. **“利用跨测试/跨实验的不变性进行因果结构搜索”的整体前景如何？哪种只会躺赢基础规则？**（Robin 表达了对这些方向的不确定性预期）[0:47:00-0:48:17]。
5. **在诊断工具（无直接效应）情景下，巨大效率增益的推广条件是什么？**（Robins [0:55:10-0:55:28]刚发现“通常30-50倍”增益，但还在推导在何种模型结构该种增益才会出现）。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

