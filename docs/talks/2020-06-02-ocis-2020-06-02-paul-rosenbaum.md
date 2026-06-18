# Replication and Evidence Factors in Observational Studies

**讲者**: Paul Rosenbaum  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-06-02  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=xQRfPcd3XqA> · [幻灯片](https://drive.google.com/file/d/12OPu8lgCYoRaV_hghzyz9wnKMt1RQcZt/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告位于**观察性研究中「证据的综合与复制」**这一核心方向。

- **该方向在追问什么**：在随机化缺失的情况下，观察性研究中的任何单一比较（如处理组 vs 对照组）都可能被未观测混杂（bias）完全解释。那么，**如何通过多种、受不同潜在偏差影响的分析，使得联合证据在对抗偏差时比单一分析更强？** 核心是：非重复的复制（non-repetitious replication）——不是重做同一项研究，而是用同一数据产生**多个证据因子（evidence factors）**，每个因子受到不同的偏差威胁，但都指向同一因果效应。
- **奠基与主流路线**：传统上，流行病学和统计学依赖**Hill 准则（一致性、剂量反应等）**以及**敏感性分析**（如 Rosenbaum [15] 的放大敏感性分析）。Rosenbaum 自 2010 年左右系统发展了一套**基于随机化推理（randomization inference）的证据因子框架**，将“非重复复制”形式化为：若研究设计具有对称性（群结构），则可分解出多个条件独立的检验，每个检验对不同的偏差模式敏感。
- **当前 frontier**：本报告是 Rosenbaum 对自己已有工作的梳理与推广。Rosenbaum 2017 *Statist. Sci.* [20] 给出了证据因子的一般群结构；Karmakar et al. [3, 4, 5] 在此基础上研究了效应合并、多项工具变量、以及近似算法构建设计。当前开放方向包括：更多因子的构造、与连续处理/工具变量的对接、以及如何用近似算法（如 bipartite matching）自动化生成证据因子设计（[6]）。
- **这场报告站在哪**：报告整合了 [20, 23] 和即将出版的著作 [22, Chapter 20]，通过一个具体例子（吸烟与牙周病）展示如何将“处理 vs 对照”和“剂量反应”两张分析嵌入同一群结构，形成两个证据因子，且其敏感性分析可按“独立研究”的 meta 分析方法合并。**关键创新**在于**knit product** 构造：在不假设两个因子独立的条件下，仅用每个因子各自的敏感性分析信度区间，即可证明联合 p 值的随机占优性（stochastic domination）。

---

### 二、最小内核 / 一个最简例子

**符号与设定**（用本报告最简版本，2 对患者，4 人）：
- **人员**：4 人，分 2 对（pair 1: 两 50 多岁男性；pair 2: 两 60 多岁女性），每种协变量分层内匹配。
- **处理**：吸烟（1=smoker, 0=control），每个 pair 内一个 smoker 一个 control。
- **剂量**：smoker 的吸烟量（cig/day），pair 1 剂量=40，pair 2 剂量=8。
- **观测**：每人的牙周病指标（% of diseased sites）。
- **目标（estimand）**：吸烟对牙周病的因果效应（如平均处理效应）。但报告聚焦于**检验 Fisher 精确零假说**（H0：处理对所有人无效应，即任何人的结果都是固定值，不受分配影响）。

**最简特例：2 对患者，每个 pair 内 2 种分配×pair 间 2 种剂量分配 → 8 种可能处理分配。**

1. **群结构 G**：8 个排列矩阵，将 4 人分配到 4 个处理位置（两个 smoker 位、两个 control 位，每个 smoker 位有固定剂量 {40, 8}）。G 保持 pair 内 match 完整。
2. **子群 H（剂量置换）**：固定每个 pair 内谁 smoker 谁 control，只 permute 两个 smoker 的剂量（40↔8）。|H|=2! = 2。
3. **陪集代表集 K（smoker/control 分配）**：固定剂量分配，只 permute 每个 pair 内部谁 smoker 谁 control。|K|=2² = 4。
4. **唯一表示 g = h·k**：每个分配可唯一写为：先决定谁 smoker 谁 control（K），再决定哪个 smoker 抽 40 哪个抽 8（H）。反之亦然。

**核心思想**（一个直觉到可懂的例子）：
- **因子 1（Wilcoxon 符号秩检验）**：只关心 smoker 与 control 比较，忽略剂量。这个检验的分布只受 **smoker/control 分配过程**（K 上的分布）影响，**完全不受 H 的影响**（因为统计量对 H 不变）。
- **因子 2（cross-cut 检验）**：在给定谁 smoker 谁 control 后，检验剂量（40 vs 8）与 outcome 差之间的关联。这个检验的分布只受 **剂量分配过程**（给定 K 后 H 上的条件分布）影响。
- 两个因子**联合起来**，若我们分别用 Rosenbaum 的敏感性分析建模 K 上的偏差（Γ 控制）和 H 上的偏差（Γ′ 控制），并且**不假定 K 与 H 独立**（即不假定“是否吸烟”与“吸多少”无关），则联合上界 p 值 **(P̄, P̄′)** 在单位正方形上随机占优于均匀分布。因此可以用 Fisher 方法（或截断乘积法，[25]）将两者视为独立研究的 p 值合并，得到更不敏感于偏差的证据。

关键：knit product（编织积）允许条件分布依赖 K，从而不附加独立性假设。

---

### 三、报告主体：讲者讲了什么

**[0:01:45–0:02:25] 引言：复制不是重复**
- 讲者引用 Cochran (1965) 和 Susser，强调“一致性”必须是**多样性**下的一致性，而非同一种偏差在多个数据集中重复出现。
- 提出核心问题：一个观察性研究能否自我复制——即在同一数据上做两个受不同偏差威胁的比较，联合起来比单独任何一个更强。

**[0:02:25–0:05:00] 例子：药物成瘾治疗效果研究（DATOS, TOPS）**
- 三组研究都发现“治疗时长≥3个月”与更好结局相关。但 NAS 1999 报告（Manski 等）指出：最可能的偏差（自选择完成/退出）完全能解释该关联。**同一偏差在三个研究中同样存在 → 重复不等于复制**。

**[0:05:00–0:11:20] 哲学类比：Polya (1941) 的贝叶斯启发、Haack (1995) 的填字谜**
- Polya：置信度增加取决于新证据与已有证据的**不相似性**。
- Haack 的填字谜类比：每个 clue 不能唯一确定 entry（类似观测关联不识别因果），但多个 clue 交叉（如 16 对 SCOUT 与 SOB 与 DOG 与 BRIGHT SIDE 的一致性）使 entry 变得高度可信，且**这种 coherence 不是 viciously circular**——因为可以剥离开单个 clue 的独立证据。
- 讲者关键词：**demarcation**（划定界限）——可问“如果没有 scud 与 sob 一致，我们还确信 scud 吗？” 答案：是的，因为有 clue、与 dog 交叉、与 bright side 交叉等。

**[0:11:20–0:17:00] 实际例子：吸烟与牙周病（Rosenbaum 2017 数据）**
- 数据：NHANES 2011–2012，441 对（daily smoker vs never smoker），匹配年龄/性别/教育/收入/种族。
- 结果（pcteither）：28 颗牙×6 位置，计算%患病位置。
- 箱线图（smoker – control 差）：明显右偏，**Wilcoxon 符号秩检验 p < 10⁻⁴（机器精度）**。
- 敏感性分析：Γ=2.75 时最大 p 值接近 0.05（Γ=1 为随机化情形）。
- 剂量反应图：x 轴=smoker 的 cigs/day，y 轴= pair 内 smoker–control 差。LOESS 平滑显示正向趋势。cross-cut 检验（四分位砍刀四角 OR≈3.65）随机化 p=0.02。

**[0:17:00–0:31:40] 核心结构：两个因子如何从同一数据产生**
- 第一因子（smoker vs control）：Wilcoxon，invariant to dose permutation（H）。
- 第二因子（dose response）：cross-cut，conditional on smoker/control assignment（K）。
- 讲者阐明：这两张图完全依赖（投影 scatter→boxplot），但它们的敏感性分析却可以按“独立研究”合并。
- **关键声明**：若 H0 成立，若 smoker/control 分配偏差≤Γ，若剂量分配偏差≤Γ′，则上界 p 值对 (P̄, P̄′) 在 [0,1]² 上随机占优于 Uniform。故可用 meta-analytic 方法（截断乘积，门限 0.2）合并。
- 实例结果：Wilcoxon Γ=2.75 敏感，cross-cut Γ′=1.6 敏感。合并后联合p=0.05 出现在 Γ=2.75, Γ′=1.6 时，即联合分析对偏差更不敏感。甚至可让一个因子承受无穷大偏差（infinite bias），另一个因子仍可维持证据。

**[0:31:40–0:45:55] 群论结构：一般构造**
- 讲者用 2 对患者的例子展开：8 种分配→群 G（4×4 排列矩阵）。
- H（剂量置换子群）|H|=2；K（smoker/control 分配，陪集代表集）|K|=4。
- 积分解 G = {h·k | h∈H, k∈K}，唯一表示。
- 一般化：任意有限群 G、子群 H，可取陪集代表集 K，则每个 g∈G 有唯一 h·k。
- 联合分布构造：**knit product（编织积）**——从 分布 p∈P（K 上的 marginal）和 分布族 p′(·|k)∈P′θ（给定 k 后 H 上的条件）构建 G 上的分布。不假定 marginal 与 conditional 独立 → 不同于逐点乘（那会隐含独立性）。

**[0:45:55–0:53:00] 命题与证明草图**
- **Lemma 1**：Wilcoxon 在 knit product 下的敏感性分析等价于原 marginal-only 分析（因统计量对 H 不变）。
- **Lemma 2**：cross-cut 在 knit product 下的敏感性分析等价于原 conditional-only 分析。
- 从而联合 p 值的随机占优性证明变为：在 knit product 下，两个检验的 p 值分别 control 各自的 level，故联合（P̄, P̄′）随机占优 Uniform。
- 描述简洁，核心是 marginal 检验 + conditional检验 → 联合随机占优。

**[0:53:00–0:55:00] 推广到更多因子与分层**
- 按 age 和 gender 分层（4 层）得到另一子群，与 dose 置换结合可产生更多因子。
- 实际结果：stratified cross-cut 比 unstratified 更不敏感（Γ′=2.25 vs 1.6）。联合 Wilcoxon（Γ=3）→ 联合 p=0.04（还在 0.05 以下）。
- 结论：只要设计中有分层/对称性，就可构造更多证据因子。讲者提到最长可达 3 个因子（处理 vs 对照、剂量、预防措施）。

**[0:55:00–0:59:00] 总结**
- 复制不是重复；观察性研究可自我复制。
- 证据因子来自群的对称性与子群。
- 联合敏感性分析可比单一因子允许更大的偏差。
- 可用于工具变量、控制组多重比较、各式设计。

---

### 四、对应论文与开放问题

**对应论文**（转写中提及，结合幻灯片）：
- 本场报告主要依据 **Rosenbaum (2017) "The general structure of evidence factors in observational studies"**, *Statist. Sci.*, 32:514-530 [20]。
- 其中的牙周病数据和 cross-cut 统计来自 **Rosenbaum (2016) "The cross-cut statistic and its sensitivity to bias in observational studies with ordered doses of treatment"**, *Biometrics*, 72:175-183 [19]。
- 即将出版的专著 **Rosenbaum, "Replication and Evidence Factors in Observational Studies"**, Chapman and Hall/CRC [23]，标注 “in preparation”。
- R 包 **DOS2** 提供了 periodontal 数据与 senWilcox、crosscut 函数。
- Karmakar, Small, Rosenbaum ([3], [5], [6]) 扩展了证据因子在工具变量、近似算法、多项暴露 biomarkers 上的应用。

**开放问题**（从转写中提取，非讲者简单提及即算，但经核实属于当前未解决）：
1. **超出两个因子的构造** [0:57:01–0:58:17]：讲者肯定理论上可推广到任意个因子，但多大程度上能实际找到“有意义”的分解（即每个因子受不同可辨识的偏差威胁）？当前例子（处理 vs 对照 + 剂量 + 预防措施）只是特例。**如何系统性地为给定研究构造多个证据因子？**
2. **knit product 的推广** [0:46:50–0:49:50]：讲者指出 knit product 的构造本身简单（他之前未见 explicit 描述），但当前仅用于二元处理+有序剂量情形。**knit product 能否与其他半参数/工具变量模型结合，形成一种通用的“多因子敏感性分析框架”？** 尤其对于连续处理/工具的 nonparametric sensitivity model。
3. **合并方法与 power 的权衡** [0:32:20–0:32:50]：截断乘积法（Zaykin et al., 2002 [25]）优于 Fisher 法，但讲者未讨论合并方法对 power 和 sensitivity range 的 impact。**对于给定的证据因子结构，是否存在最优合并统计量，使联合检验在偏差下保持 level 且最小化 type II error？**
4. **与现有工具变量 / 中介分析的衔接**（幻灯片提及 Karmakar et al. [5] 已涉及 IV，但本报告未深入）：**如何在统一群结构下将工具变量作为第三个因子融合？** 例如，IV 弱时偏差模式与处理分配的偏差不同，但需保证因子间条件独立。

**特别提示**：所有专有名词（Wilcoxon → 转写中多次出现 "Wilcoxan" 应是同一声；cross-cut → 转写中有 "cross-cut" 和 "crosscut" 两处 OCR 变体，均指 [19] 的 "cross-cut statistic"；knit product → 转写为 "nit product"，从幻灯片可知是 "knit product"）均以幻灯片和论文为 ground truth。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

