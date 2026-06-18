# The (Causal) Discovery Ladder: Unravelling Governing Equations and Beyond using Machine Learning

**讲者**: Mihaela van der Schaar  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2024-04-16  
**主题**: 因果推断  
**视频**: <https://youtu.be/P-GxxhhcLUo> · [幻灯片](https://drive.google.com/file/d/1Y3s5gzw-I-K7F1g75i_i3oYAOkaKSbVV/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2002.04083](https://arxiv.org/abs/2002.04083) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

这场报告的核心论点是：**因果推断的下一个前沿（"Discovery Ladder"）是从观测数据中发现闭式控制方程（ODE/PDE）**，而不仅仅是估计静态或动态的因果效应。讲者Mihaela van der Schaar（剑桥大学）将因果发现从 Pearl 的因果之梯（关联→干预→反事实）再向上推一层，提出「控制方程（Governing equations）」作为更高阶的结构知识。这条工作线在**因果发现与科学发现的交叉点**上，尤其聚焦于**面向动力学系统的符号回归**──从纵向数据中恢复出简洁、可解释的微分方程，从而使科学模型（如药代动力学/药效学 PKPD 模型）既能被人类理解，又能用于临床决策。

**主流路线与奠基工作：**
- **经典符号回归**（Symbolic regression, SR）如 Koza (1992) 遗传编程，但直接用于导数不可观测的 ODE 数据时效果很差。
- **两步法**（先数值微分再 SR）如 Schmidt & Lipson (2009) 的 SINDy（Brunton, Proctor & Kutz, 2016），但对噪声和稀疏采样敏感。
- **Neural ODE**（Chen et al., 2018）用神经网络近似右端函数，不产生闭式方程，缺乏可解释性。
- **本报告的直接前序工作**是实验室自己开发的 D-CODE（Qian, Kacprzyk, van der Schaar, ICLR 2022）——首次利用**变分公式化**（variational formulation）绕过导数估计，直接发现闭式 ODE；以及 D-CIPHER（Kacprzyk, Qian, van der Schaar, NeurIPS 2023）——将变分技巧扩展到 PDE 发现，得到目前最广的可发现 PDE 类（Variational-Ready PDEs）。
- **动态因果推断**的平行线：从 Marginal Structural Models（Robins, Hernán & Brumback, 2000）到本实验室的 CRN（Bica, Alaa, Jordon, van der Schaar, ICLR 2020）和 TE-CDE（Seedat, Imrie, Bellot, van der Schaar, ICML 2022），再到 INSITE（Kacprzyk et al., ICLR 2024）——首次将 ODE 发现与面板数据因果推断统一。

**当前 frontier：** 如何将发现出的闭式方程（ODE/PDE）与高维、混杂、非规则采样的真实临床数据结合，形成可解释的个性化预测与干预推荐。报告还提出了「Causal Deep Learning」框架（Berrevoets, Qian, Kacprzyk & van der Schaar, 2023），试图弱化 Pearl 因果之梯的“全有或全无”要求，通过可检验的部分结构假设和函数形式梯度来桥接理论与落地。

---

### 二、最小内核 / 一个最简例子

**符号设定（针对 ODE 发现）：**
- 观测数据：系统在时间点 \(t_1, t_2, \dots, t_T\) 的状态向量 \(\mathbf{y}(t) \in \mathbb{R}^J\)。可能带有噪声、不规则采样。
- 潜在真实轨迹：\(\mathbf{x}(t): [0,T] \to \mathbb{R}^J\)，但不可直接观测。
- 目标：发现一个闭式 ODE 系统  
  \[
  \frac{d x_j}{dt} = f_j(\mathbf{x}(t)), \quad j=1,\dots,J,
  \]
  其中 \(f_j: \mathbb{R}^J \to \mathbb{R}\) 是已知形式的符号函数（如多项式、三角函数、指数等）。
- **estimation target（estimand）**：函数 \(f\) 的结构（而非参数值）。它是无限维的，但被限制在一个预先指定的候选字典中（例如 \(1, x_1, x_2, x_1^2, x_1x_2, \sin(x_1), \dots\)）。注意：这里不涉及因果效应 estimand，而是方程发现。
- **关键挑战**：导数是不可观测的，直接对 \(x\) 进行数值微分会放大噪声。

**最简特例（d=1, 单个状态变量）：**  
考虑一维 Gompertz 生长模型（肿瘤生长）：  
\[
\frac{dx}{dt} = \alpha x \left(1 - \frac{x}{\beta}\right),
\]
其中 \(x(t)\) 是肿瘤体积，\(\alpha\) 是生长率，\(\beta\) 是最大容量。观测数据是时间序列 \(\{y_i = x(t_i) + \varepsilon_i\}\)，噪声 \(\varepsilon_i \sim N(0,\sigma^2)\)，采样时间可能不均匀。

**D-CODE 的核心思想（用变分公式化绕过导数）：**  
引入一组已知的、光滑的测试函数 \(\{g_s(t)\}_{s=1}^S\)（例如傅里叶正弦基 \(g_s(t) = \sqrt{2/T} \sin(s\pi t/T)\)）。  
积分恒等式（分部积分）：
\[
\int_0^T x(t) \, g_s'(t) \, dt = -\int_0^T f(x(t)) \, g_s(t) \, dt,
\]
左边只涉及 \(x(t)\) 和已知导数 \(g_s'(t)\)（可解析计算），右边涉及未知的 \(f\)。因此可以将左侧从数据估计出来（如通过插值后的数值积分），右侧则是一个关于 \(f\) 参数的线性函数（若 \(f\) 是参数的线性组合，比如 \(f(x) = a x + b x^2\)）。于是问题转化为一个线性系统，再用符号回归或稀疏优化求解参数。  
在这个一维例子中，候选字典取 \(\{x, x^2\}\)，那么左侧向量（对每个 \(s\)）等于右侧 \(a \int x(t) g_s(t) dt + b \int x^2(t) g_s(t) dt\)，可通过最小二乘或 LASSO 解出 \((a,b)\)。

**为什么这个例子能说明全貌：** 它演示了 (1) 无需显式计算导数，(2) 利用分部积分将微分方程转化为线性积分方程，(3) 通过预设测试函数族实现 low-variance 估计。更复杂的系统（多维、PDE）原理相同，只是增加维度或引入偏导的变分公式化。

---

### 三、报告主体：讲者讲了什么

以下按时间戳整理，融合幻灯片权威内容与转写口语解释。

#### [0:00-0:05] 开场与实验室介绍  
讲者介绍自己的实验室（Cambridge Centre for AI in Medicine），列出参与因果课题的学生（Zhaozhi Qian, Krzysztof Kacprzyk, Alicia Curth 等）。强调实验室约一半成员从事因果研究，涵盖极广面。

#### [0:05-0:15] 「发现之梯」（Discovery Ladder）的提出  
- **核心命题**：在 Pearl 的三层之梯（关联 → 干预 → 反事实）之上，还有更高一层——**控制方程（Governing equations）**，即闭式微分方程。它们比结构化因果模型更紧凑、可泛化、可分析（如平衡态、灵敏性），且对人类专家透明。
- 展示各种方程形式（显函数、隐函数、ODE、PDE），举例爱因斯坦质能方程、伯努利方程、牛顿定律、热方程。强调发现此类方程是“下一个前沿”。

#### [0:15-0:22] ODE 发现的挑战与 D-CODE  
- 问题设定：给定离散噪声观测 \(\{y(t_i)\}\)，希望发现闭式 ODE 系统 \(dx_j/dt = f_j(x)\)。  
- 三大困难：(a) 导数不可观测；(b) 噪声下导数估计困难；(c) 初值未知，直接数值积分 ODE 稳定性和计算代价高。  
- **D-CODE 解决方案（Qian, Kacprzyk & vdS, ICLR 2022）**：使用**变分公式化**（Hackbusch 2017）——选取光滑测试函数 \(g_s(t)\) 在 \([0,T]\) 上满足 \(g(0)=g(T)=0\)，利用分部积分得到  
  \[
  \int_0^T x(t) g_s'(t) dt = -\int_0^T f(x(t)) g_s(t) dt.
  \]  
  这样左边只依赖 \(x(t)\) 和已知的 \(g_s'(t)\)，右边是 \(f\) 的线性泛函（若 \(f\) 参数化后线性）。  
- 算法步骤：  
  1. 预处理：估计轨迹 \(\hat{x}(t)\)（如通过样条或傅里叶基）。  
  2. 选择测试函数（如正弦基），计算左侧数值积分。  
  3. 对候选字典（如 \(\{x, x^2, \sin x\}\) ）用符号回归（如稀疏优化）求解系数。  
- 实验：在 Gompertz、广义 logistic、糖酵解振荡器、Lorenz 系统上，D-CODE 显著优于两步法（SR-T, SR-S, SR-G），且即使在高噪声和大采样间隔下仍能高概率恢复真方程。**注意**：报告提到“neural ODE 也失败”，但幻灯片未显示对应具体数字，可能为讲者口头补充。

#### [0:22-0:27] 真实数据应用：化疗肿瘤生长  
- 使用 8 个临床试验数据集（癌症患者），D-CODE 发现肿瘤体积对化疗的 ODE 模型。结果未声称“正确”，但比符号回归更简洁，且能捕捉复发趋势。

#### [0:27-0:34] 从实验室到临床：Latent Hybridization Model (LHM)  
- **动机**：药理学中的 PKPD 模型（ODE）由专家在实验室构建，使用“专家变量”（如免疫激活水平）可在实验室测量，但临床上只能观测到高分子生物标志物（如 C-反应蛋白 CRP）。  
- **LHM（Qian, Zame, Fleuren, Elbers & vdS, NeurIPS 2021）**：将专家 ODE 作为潜变量动力学，嵌入一个**神经 ODE 系统**来建模观测变量的演化。具体：  
  - 潜状态（专家变量）用已知 PKPD ODE 演化（有合理参数）。  
  - 观测变量（CRP 等）由另一个神经 ODE 从潜状态映射。  
- **COVID-19 案例**：为 ICU 患者个性化地塞米松剂量。专家 PKPD 模型描述免疫-药物相互作用，但不可观测；LHM 从 CRP、FiO2 等临床指标推断潜变量，从而“解卷” PKPD 模型，提供可解释剂量建议。讲者特别强调：只需 100-200 患者样本即可学到有效模型（纯 ML 需要成千上万），且输出对临床医生透明。

#### [0:34-0:39] 扩展到 PDE：D-CIPHER  
- **挑战**：变分技巧对高阶 ODE 和 PDE 不能直接推广。  
- **D-CIPHER（Kacprzyk, Qian, vdS, NeurIPS 2023）**：  
  - 将任何 PDE 分解为**含导数项**（derivative-bound, \(f(\cdot)\)）和**无导数项**（derivative-free, \(g(\cdot)\)）。  
  - 无导数项可直接从数据评估（无需约束），含导数项需要**变分就绪**（Variational-Ready）条件——目前最广的可变分 PDE 类。  
  - 算法：字典搜索（如 \(\partial_t u, \partial_x^2 u, u\partial_x u\) 等）+ 符号回归优化，使用提出的 CoLLie 优化器。  
- 适用场景：时空物理系统、群体模型、年龄结构流行病模型。  

#### [0:39-0:51] 连接 ODE 发现与因果推断：INSITE  
- **桥接动机**：因果推断长期针对离散治疗方案和混杂数据；ODE 发现偏向连续动力学、单一群体方程。两者有三个主要差异：  
  1. **识别假设不同**：因果推断假设无未观测混杂（序贯可忽略性），ODE 发现假设方程对所有个体相同且无干预分配选择。  
  2. **治疗方案类型**：因果推断处理离散/连续/多个方案；ODE 发现输出连续函数。  
  3. **个体间异质性**：因果推断关注 CATE（条件平均处理效应）；ODE 发现默认一个方程用于所有个体。  
- **INSITE（Kacprzyk, Holt, Berrevoets, Qian & vdS, ICLR 2024）** 提出三步调和：  
  - 新的识别假设，接受 ODE 发现固有的（如函数形式先验）。  
  - 将治疗方案表示为 ODE 输入（如药物浓度作为时变参数）。  
  - 通过个性化 ODE（每个患者一个方程）引入个体异质性。  
- 讲者称此为“第一个可用的将 ODE 发现转化为处理效应方法的一般框架”，并声称优于标准表示学习（如 CRN）和两步法。  
- **注意**：转写 [0:39-0:45] 部分略为含糊，但幻灯片结构清晰。

#### [0:51-1:00] 回顾历史工作  
- 静态 CATE：从 Counterfactual Regression (Shalit et al., 2016) 到 GANITE (Yoon et al., 2018) 到 Meta-Learners (Curth & vdS, 2021)，实验室贡献了多个方法。  
- 动态 CATE：  
  - 从 Marginal Structural Models + RNN (RMSN, Lim et al., 2018) 到 CRN (Bica et al., ICLR 2020)（用对抗训练平衡表示）。  
  - 处理不规则采样：TE-CDE (Seedat et al., ICML 2022)，用神经控制微分方程（Neural CDE）学习连续隐含状态。  
  - 处理信息性缺失（informative sampling）：Vanderschueren et al. (ICML 2023) 使用强度-重要性权重。

#### [1:00-1:10] 因果深度学习（Causal Deep Learning）  
- **问题**：现有因果方法要么是“全有或全无”的游戏（要么假设精确结构，要么什么都不假设），导致实际应用受限。  
- **提案**：Berrevoets, Qian, Kacprzyk & vdS (2023) 引入**因果深度学习地图**，在两条轴上划分：  
  - **结构轴** (Level 1-3)：从无结构 (任何图) → 可检验的部分结构 → 已知因果图（但不可检验）。  
  - **函数轴** (Level 1-4)：从非参数 → 噪声模型 → 参数化（+,-,×,÷,指数等）→ 完全已知函数。  
  - **时间轴** (隐含在动态设置中)。  
- 目标：为从业者提供“选择正确假设水平”的方法论，避免不必要的强假设。

#### [1:10-1:12] 结束与邀请  
- 提醒明天（转写日期次日）的“Inspiration Exchange”环节，Kacprzyk 将介绍更多 AI for Science 的新进展。

---

### 四、对应论文与开放问题

**(a) 这场报告对应的论文（需要对照报告实际内容而非仅限于摘要）**  

| 论文（讲者提及） | 出处 | 备注 |
|------------------|------|------|
| D-CODE: Discovering Closed-form ODEs | Qian, Kacprzyk, van der Schaar, ICLR 2022 | 转写和幻灯片均确认。 |
| D-CIPHER: Discovering Closed-form PDEs | Kacprzyk, Qian, van der Schaar, NeurIPS 2023 | 同。 |
| Latent Hybridization Model (LHM) | Qian, Zame, Fleuren, Elbers, van der Schaar, NeurIPS 2021 | 转写和幻灯片确认；用于 COVID-19 案例。 |
| INSITE: ODE Discovery for Longitudinal Heterogeneous Treatment Effect Inference | Kacprzyk, Holt, Berrevoets, Qian & van der Schaar, ICLR 2024 | 转写和幻灯片确认。 |
| Counterfactual Recurrent Network (CRN) | Bica, Alaa, Jordon, van der Schaar, ICLR 2020 | 幻灯片列在动态推断中。对应摘要 arXiv 2002.04083。 |
| TE-CDE: Continuous-Time Modeling of Counterfactual Outcomes Using Neural CDEs | Seedat, Imrie, Bellot, van der Schaar, ICML 2022 | 幻灯片确认。 |
| Accounting For Informative Sampling (Vanderschueren et al.) | Vanderschueren, Curth, Verbeke & van der Schaar, ICML 2023 | 幻灯片确认。 |
| Causal Deep Learning | Berrevoets, Qian, Kacprzyk, van der Schaar, 2023 | 幻灯片引用 vanderschaar-lab.com 上的论文。具体出版处未知（可能是 arXiv 或期刊）。 |
| Reality-Centric Manifesto 和 PLOS Digital Health 2024 | 口头提及，非因果论文本身 | 讲者倡导“现实中心”的研究文化。 |

**注意**：转写中提到的“2002.04083”是 CRN 论文，但报告的主体是 Discovery Ladder，CRN 只是其中一部分回顾。报告中没有给出一一对应每篇论文的标题，以上根据幻灯片文字抽取确认。人名拼写（如“Kacprzyk”“Berrevoets”）已纠正；转写有听错风险，但幻灯片提供权威拼写。

**(b) 开放问题（扎根转写时间点）**  

1. **[0:12-0:14] 变分公式化对高阶 ODE / PDE 的推广**：D-CIPHER 只覆盖了“变分就绪 PDE 类”，但还有大量 PDE（如含混合偏导的方程）不能直接处理。如何扩大可发现类？  
2. **[0:47-0:50] 信息性采样（informative sampling）的更好处理方法**：讲者承认现有强度-重要性权重只是初步方案，还需要更鲁棒的框架来处理“患者何时就诊”与治疗结果之间的因果偏差。  
3. **[1:04-1:06] 因果深度学习架构中的假设验证**：如何检验部分结构假设（如马尔可夫等价类中的边缺失）？目前只能靠先验知识，缺乏数据驱动的检验方法。  
4. **[0:36-0:38] 从发现方程到个性化干预的落地**：INSITE 虽然建立了框架，但讲者未讨论当真实动力学并非 ODE（如随机微分方程或滞后方程）时的扩展。  
5. **[全报告脉络] 发现出的方程如何被科学家接受并验证**：D-CODE 和 D-CIPHER 提供的是统计最优的候选方程，但因果关系确认需要实验；报告没有讨论后续验证设计。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

