# Combining Experimental and Observational Data for Identification and Estimation of Long-Term Causal Effects

**讲者**: AmirEmad Ghassami  
**讨论人**: Guido Imbens  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2022-06-14  
**主题**: 因果推断  
**视频**: <https://youtu.be/uVfEo9UuC20> · [幻灯片](https://drive.google.com/file/d/1NW1ggfyFz7qhiIhod0AUwuDtKgyyD2Mg/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2201.10743](https://arxiv.org/abs/2201.10743) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

**子方向**：结合实验（RCT）与观察（observational）数据进行因果推断，以便在**实验未能记录长期结果**而**观察数据存在未观测混杂**时识别长期因果效应。这个子方向属于 **data fusion / evidence synthesis** 的因果识别分支，区别于“仅用于提升效率”的融合——在这里，单一数据源连识别都做不到。

**奠基与主流路线**：
- **Athey, Chetty, Imbens 等 (2020)**：对该子方向有开创性工作；他们假设“潜在无混淆性”——给定短期结果 M(a) 和观测混淆 X，处理 A 与长期结果 Y(a) 条件独立。这一假设实质排除了未观测混淆变量 U 对 Y 的直接影响。
- **代理推断 (Proximal Causal Inference)**：更一般地，用观测到的代理变量（proxy）代替未观测混淆，在识别上需要两个独立代理（或一个代理加一个负对照），“排除性”假设是关键。
- **Bespoke IV (Richardson & Tchetgen Tchetgen, 2022)**：将观测数据中的一个协变量“定制”为工具变量——不要求传统的排除性限制或未混淆性，只要求它满足一个偏加性等关联条件。

这场报告的讲者 **Ghassami 等** 站在上述两条路线的交会点上，提出三个框架——**等混杂偏差（Equi-Confounding Bias）、定制IV（Bespoke IV）和代理数据融合（Proximal Data Fusion）**。其共同叙事结构是：在传统的“纯观察”版本中，每个框架需要一个强的排除性假设（如平行趋势、IV排除性、第二代理独立性）；有了实验数据后，**可以用实验数据中的短期效应“锚定”调整，从而放松该排除性假设**。

**关键词**：data fusion, identification without external validity, unmeasured confounding, influence-function-based estimation, multiply robust.

---

### 二、最小内核 / 一个最简例子

**符号与模型**：

| 符号 | 含义 |
|---|---|
| \(A\in\{0,1\}\) | 二元处理 |
| \(M\) | 短期结果（实验中测得，观察域中也测得） |
| \(Y\) | 长期结果（实验中未观测，观察域中测得） |
| \(X\) | 观测混淆变量 |
| \(U\) | 未观测混淆（同时影响 A 与 M、Y） |
| \(G\in\{O,E\}\) | 域指示符：\(G=O\) = 观察域，\(G=E\) = 实验域 |

**已知从实验域得到**：
- 内部有效性：条件于 X，处理 A 在实验域随机化（\(A\perp\!\!\!\perp\{Y(a),M(a)\}\mid X, G=E\)）。
- 外部有效性假定（所有框架共用）：\(G\perp\!\!\!\perp\{Y(a),M(a)\}\mid X\)（实验与观察域的条件分布相同，即 \(P(X)\) 和条件关系可交换）。
- 实验只记录短期结果 M，不记录长期结果 Y。

**目标参数**：  
\( \theta_{ATE} = \mathbb{E}[Y(1)-Y(0)\mid G=O] \)，以及 ETT（条件于 \(A=1\) 的版本）。

**最简特例**（d=1）：令所有变量均为二元（或一维连续），且忽略 X 的作用（\(X\equiv\emptyset\)）：
- 观察域：有 A、M、Y，但存在 U 同时影响 A 与 Y（和 M），因此 \( \mathbb{E}[Y\mid A=1] - \mathbb{E}[Y\mid A=0] \) 不是因果效应。
- 实验域：有 A、M（但无 Y），实验随机分配 A，所以 \( \mathbb{E}[M\mid A=1,G=E] - \mathbb{E}[M\mid A=0,G=E] \) 是短期因果效应。

**核心思想（以 Equi-Confounding Bias 为例）**：

等混杂偏差假定：在观察域中，混杂误差（selection bias）对短期结果 M 和长期结果 Y 是**加性相等的**：
\[
\mathbb{E}[M(0)\mid A=1] - \mathbb{E}[M(0)\mid A=0] = \mathbb{E}[Y(0)\mid A=1] - \mathbb{E}[Y(0)\mid A=0].
\]
直观上，这意味着从 M 到 Y 的**平均趋势**在处理组和控制组间相同（类似平行趋势但将“时间点”换成了“M→Y 的跨度”）。

于是，ATE 可以写为：
\[
\theta_{ATE} = \left(\mathbb{E}[Y\mid A=1] - \mathbb{E}[Y\mid A=0]\right) - \left(\mathbb{E}[M\mid A=1] - \mathbb{E}[M\mid A=0]\right) + \underbrace{\mathbb{E}[M(1)-M(0)]}_{\text{短期ATE}}.
\]
其中，括号内的第一行是观察域中 Y 的关联差异，第二行是观察域中 M 的关联差异（可观测），第三行是**短期因果效应**（由实验域识别，因为实验域中 A 随机，且记录了 M）。整个公式的关键是：实验数据给出了短期因果效应，然后用等混杂偏差假设将 Y 的关联差异减去 M 的关联差异，就得到了 Y 的因果效应。

---

### 三、报告主体：讲者讲了什么

**[0:00–0:10] 问题设定**  
- 讲者介绍了 DAG（A→M→Y，X→A, X→M, X→Y，U→A, U→M, U→Y；观察域中所有箭头都存在；实验域中 A 与 U 断开，Y 被遮住）。  
- 明确目标参数：ATE 和 ETT 定义在 \(G=O\) 上。  
- 强调：仅观察数据因 U→A 导致不可识别；仅实验数据因 Y 缺失也不可识别。  

**[0:10–0:15] 现有方法回顾**  
- 参考文献 Athey et al. (2020)。给出他们的 latent unconfoundedness 假设：\(A\perp\!\!\!\perp Y(a)\mid X, M(a), G=O\)。  
- 指出该假设实质排除 U 对 Y 的直接影响（即 \(U\not\to Y\)）。这是这篇工作想放松的。

**[0:15–0:20] 三大框架概览**  
讲者列出三个提案的中心思想：

1. **Equi-Confounding Bias Data Fusion**：  
   假设观察域中 M 和 Y 的**选择偏差相等**（加性）。  
   这是 DiD 到数据融合的推广：这里 M 是治疗后变量（不是 DiD 中的前处理变量 Y0），因此不需要“无治疗预期效应”这一假设。

2. **Bespoke IV Data Fusion**：  
   基于 Richardson & Tchetgen Tchetgen (2022) 的BSIV。不需要假设 M 和 Y 有相同的选择偏差，而是寻找一个观测协变量 Z，使得 Z 对 M(a) 和 Y(a) 的**偏加性关联**相等（partial additive equi-association）。此时 Z 可视为“Y−M”这个新结果的一个 IV，尽管 Z 不满足标准的未混淆性或排除性。

3. **Proximal Data Fusion**：  
   基于 Tchetgen Tchetgen (2020) 的 Proximal Causal Inference。需要一个观测到的代理变量 Z（如家庭收入）满足 \(Z\perp\!\!\!\perp\{M(a),Y(a)\}\mid U,X,A,G=O\)。与标准 Proximal 不同：标准需要两个代理，这里因为有了实验数据，只需要一个代理。

**[0:23–0:30] Equi-Confounding Bias — 识别细节**  
- 讲者给出 ATE 的识别公式（幻灯片第 15 页）：  
  \[
  \theta_{ATE} = \sum_{a}(-1)^{1-a}\mathbb{E}[\mathbb{E}[Y\mid X,A=a,G=O] + \mathbb{E}[M\mid X,A=a,G=E] - \mathbb{E}[M\mid X,A=a,G=O]\mid G=O]。
  \]
- 证明思路：将 Y 的关联差异分解为（a）观测域中 M 的关联偏差，（b）实验域中 M 的因果效应，再由等混杂偏差将 Y 的关联差与 M 的关联差链接起来。
- 提到当 M 和 Y 不在同一量表时，用“Change-in-Changes”（Athey & Imbens, 2006）推广，以识别分布的累积分布函数。

**[0:30–0:37] Bespoke IV — 识别细节**  
- BSIV 假设（第 18 张幻灯片）：
  - (1) 相关性：\(\mathbb{E}[A\mid Z=0,X,G=O] \neq \mathbb{E}[A\mid Z=1,X,G=O]\)。
  - (2) 偏加性等关联：\(\mathbb{E}[M(a)\mid X,Z=1] - \mathbb{E}[M(a)\mid X,Z=0] = \mathbb{E}[Y(a)\mid X,Z=1] - \mathbb{E}[Y(a)\mid X,Z=0]\)。
- 通过 Robins 等 (2000) 的非参数重参数化，将 \(\mathbb{E}[Y-M\mid A=a, Z=z, X, G=O]\) 表达为含未知 \(\beta(z,X)\)、\(\gamma(z,X)\)、\(\mathbb{E}[Y(0)-M(0)\mid Z=z,X,G=O]\) 的方程。BSIV 使得第三项不依赖于 z，于是得到 4 个方程（A、Z 各两水平）、5 个未知参数→ 欠识别。
- 消除一个参数：两种可选假设：
  - (i) \( \beta(z,X)\) 不随 z 变（ETT of \(Y-M\) 无修饰）；
  - (ii) \(\gamma(z,X)\) 不随 z 变（选择偏差无修饰）。
  任一假设即完成识别。
- 讲者提到在模拟中 BSIV 表现良好，当 M 在观察域不可观测时也可以推广（需稍强假设）。

**[0:37–0:42] Proximal Data Fusion — 识别细节**  
- 需要一个代理 Z，满足 \(Z\perp\!\!\!\perp\{M(a),Y(a)\}\mid U,X,A,G=O\)。  
- 识别依赖一个桥函数 \(h(M,A,X)\) 满足：  
  \[
  \mathbb{E}[Y\mid Z,A,X,G=O] = \mathbb{E}[h(M,A,X)\mid Z,A,X,G=O].
  \]
  这是一个 Fredholm 第一类积分方程，需要完备性条件（类似 IV 中的治疗完备性）。  
- 讲者给出两种识别方式：基于 h 的“outcome regression”形式，和基于 q 的“IPW-like”形式。  
- 强调这是对标准 Proximal Inference 的放松：标准需要两个代理（如 Z 和另一个 W），这里用实验数据代替了一个代理。

**[0:42–0:47] 估计方法**  
- 讲者表明三种框架下的**影响函数（influence function）**已经导出。  
- 可以使用 DML（Chernozhukov et al., 2018）的交叉拟合（cross-fitting）方案：将样本分 K 份，轮流用 K-1 份估计 nuisance、1 份估计参数。  
- **多重稳健性**：若至少一个 nuisance 函数集合被正确设定，估计量一致。  
- 实现在模拟中：对 Proximal Data Fusion 的桥函数使用 **对抗性学习**（Adversarial learning, 参考 Kallus 等 2021 对 Proximal 的算法）。  
- 模拟中，基于 IF 的 Proximal 估计器（Prox4）表现最稳健，即使样本量 ~1000 也收敛良好。

**[0:47–1:04] 讨论环节（Guido Imbens & Eric Tchetgen Tchetgen）**  
- **Imbens 的主要建议**：用“LaLonde-type”的实证验证——拿一个既有短期也有长期结果的 RCT，遮住长期结果，用本方法估计，再与真实 RCT 结果比较。他质疑标准误可能会很大，但讲者回应模拟中 n=1000、四维 X 时收敛尚可。  
- **Eric Tchetgen Tchetgen 提问**：所有方法都依赖外部有效性假设（\(G\perp\!\!\!\perp\)），实际中可能最脆弱。Imbens 答道：不可直接区分外部偏离与混杂偏离，但目前无好办法；该假设虽强，但仍然是基准，建议通过更丰富的协变量和敏感度分析来加强对它的信念。

---

### 四、对应论文与开放问题

**(a) 对应论文**  
- **arXiv: 2201.10743** (v1, 2022-01-28)：  
  *Combining Experimental and Observational Data for Identification and Estimation of Long-Term Causal Effects*  
  Author list: AmirEmad Ghassami, Alan Yang, David Richardson, Ilya Shpitser, Eric Tchetgen Tchetgen.  
  幻灯片中列出的参考文献还包括 Athey et al. (2020)、Richardson & Tchetgen Tchetgen (2022)、Tchetgen Tchetgen & Vansteelandt (2013) 等。转写中多次提到的“Athey, Chetty, Imbens” 应是 Athey et al. (2020) 及其中的合作者。  
  **（注意：人名可能存在 ASR 拼写错误，建议直接查 arXiv 原文确认所有作者和序号。）**

**(b) 开放问题**  

1. **多重实验环境下的扩展**（Imbens 在讨论中提及）  
   转写 [1:00:03]：“it can be more than two you could well imagine multiple experiments.”  
   对应研究报告了两种数据域的组合；当有多个实验（每个实验记录不同部分）、或多个观察数据集时，如何扩展识别与估计框架？这属于结构未完全开放的组合问题。

2. **敏感度分析**（针对等混杂与 BSIV 假设）  
   转写 [0:16:50]：“if you don't have external validity it may be due to population differences.”  
   所有三个框架都共用外部有效性假设。转写 [0:59:55] 中 Imbens 承认无法直接区分外部有效性偏离与混杂偏离。一个自然开放问题是：能否构造一类**部分识别**或**敏感度分析**，将偏离该假设的幅度参数化并给出效应区间？

3. **代理变量的充分性与选择**  
   转写 [0:57:00]：“the difficult part is to be able to convince ourselves that the proxy we use captures variability in the latent confounder.”  
   在 Proximal Data Fusion 中，如何从观察数据**检验**或**部分验证**代理假设？这是 Proximal Causal Inference 领域未解决的问题。

4. **自适应实验设计**  
   Imbens 在讨论中提到实验数据可能昂贵而稀缺。开放问题：能否设计**贝叶斯自适应实验**，允许随着实验进行动态更新长期效应的估计，从而更高效地利用实验预算？

5. **高维协变量下的计算与理论**  
   转写仅演示了 d=4 的协变量。当 X、Z 的维度很高时，桥函数 h 的学习需要求解高维积分方程。能否利用稀疏性或核方法给出可行的估计量与收敛率？这与研究者的随机矩阵、高维统计背景直接相关。

6. **多重稳健性的确切定义与嵌套结构**  
   转写 [0:34:28]：“the moment function is multiply robust.”  
   但多重稳健性在三个框架中具体表现是不同的（例如 Equi-Confounding 需要哪些 nuisance 函数被正确设定）。给出精确的鲁棒性层级（类似 Robins 2000 对 IPW 和回归估计量的嵌套性），仍在工作中。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

