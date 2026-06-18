# A theory of causality with multiple interventions

**讲者**: Kayvan Sadeghi  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2026-02-24  
**主题**: 因果推断  
**视频**: <https://youtu.be/EkpY1l1sjPQ> · [幻灯片](https://drive.google.com/file/d/1FpXibixrorvPuURys08rx9nzAmTMmT-0/view?usp=share_link)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

【方向定位】这场报告的工作属于**因果推断的数学基础**，具体来说，是**干预主义因果（interventionist causality）的纯概率论公理化**。这个子方向的根本追问是：“因果”概念能否仅从概率分布的干预操作中定义，而不借助结构因果模型（SCM）中的方程、函数形式、噪声独立性假设，甚至不预设任何潜在因果图？

**奠基与主流路线**：当前关于干预的主流框架是 Pearl 的 SCM/Do-calculus（Pearl, 2000）。SCM 强假设包括：每一变量是父节点与新息（独立噪声）的确定性函数；图结构事先给定或由因果发现算法推断。Robins 和 Richardson 等人的“单一世界干预图”（Single World Intervention Graphs, SWIGs）以及前述研究者的“因果空间”（causal space）是较近的替代框架，但它们仍保留图的指向或 SCM 的结构性假定。

**当前 frontier**：近五年来，有少量工作尝试在更弱、更自然的假设下重述这些内容。Mogensen（2021, *On the Markov Property for Causal Graphs with Interventions*）从干预分布族到马尔可夫性质做了类似的构建，但假设每个干预分布是“硬干预”（atomic）。Dawid 的工作长期主张 SCM 是过载信息，可以用概率图模型（Bayesian networks）取代。Sadeghi & Soo（Biometrika, 2025）给出了**单一干预**的同类公理化，本报告将之推广到**多重任意子集干预**，并且声称使理论更简洁。

**本报告站在**：它站在“无 SCM、无真正因果图、仅靠干预分布族”的极端简约派一端。其核心主张是：（i）因果图是定义出来的副产品，不需要预设；（ii）三个“自然”假设可以将干预分布族与干预后因果图连接起来，使所有干预分布对该图服从全局马尔可夫性；（iii）SCM 的大部分信息在此框架中是冗余的，且 SCM 的任意函数形式可能违反这三个“合理”假设。

### 二、最小内核 / 一个最简例子

**基础符号与设定**：

- 固定变量集合 \(V = \{1, 2, ..., p\}\)。每个变量 \(X_i\) 取值空间 \(\mathcal{X}_i\)，全联合空间 \(\mathcal{X} = \prod_{i \in V} \mathcal{X}_i\)。
- **干预分布族**：\(\mathcal{P}^{\mathrm{do}} = \{\,P^{\mathrm{do}(A)}\,\}_{A \subseteq V}\)。对每一子集 \(A \subseteq V\)，\(P^{\mathrm{do}(A)}\) 是 \(\mathcal{X}\) 上的一个联合分布，解释为“对变量集合 \(A\) 进行硬、随机干预后的全系统分布”。特别地，\(P^{\mathrm{do}(\varnothing)}\) 是观测分布。
- **原因（cause）**：对任意 \(i \neq k\)，
   \[
   i \in \mathrm{cause}(k) \quad \Leftrightarrow \quad X_i \not\perp\!\!\!\perp_{P^{\mathrm{do}(i)}} X_k.
   \]
   即在**只干预 i** 的分布中，i 与 k 不独立。
- **直接原因（direct cause）**：
   \[
   i \in \mathrm{dcause}(k) \quad \Leftrightarrow \quad X_i \not\perp\!\!\!\perp_{P^{\mathrm{do}(V \setminus \{k\})}} X_k \;\big|\; X_{V\setminus\{i,k\}}.
   \]
   即在**干预除 k 以外所有变量**的分布中，i 与 k 仍依赖（给定其余全部变量）。
- **因果图** \(G(\mathcal{P})\)：有向图，节点集为 \(V\)，当且仅当 \(i \in \mathrm{dcause}(k)\) 时画一箭头 \(i \to k\)。
- **干预因果图** \(G^{\mathrm{do}(A)}\)：在原图 \(G\) 中**删除所有指向 \(A\) 中节点的入边**（出边保留）。

**最简例子**（取三个变量，所有分布是二值的）：

设 \(V = \{X, Y, Z\}\)。干预族 \(\mathcal{P}^{\mathrm{do}}\) 有 8 个分布（每个子集 A）。假设它们是“良性”的（满足下面 3 个假设），然后定义出的因果图可能如下：

```
X → Y → Z
```

这意味着：
- 在 \(P^{\mathrm{do}(X)}\) 里，X 与 Y 不独立（因为箭头）。
- 在 \(P^{\mathrm{do}(V \setminus \{Y\})}\) = \(P^{\mathrm{do}(\{X,Z\})}\) 中，给定 Z，X 与 Y 仍不独立 → X 是 Y 的直接原因。
- 在 \(P^{\mathrm{do}(V \setminus \{Z\})}\) = \(P^{\mathrm{do}(\{X,Y\})}\) 中，给定 X，Y 与 Z 仍不独立 → Y 是 Z 的直接原因。
- 同时，在 \(P^{\mathrm{do}(V \setminus \{Z\})}\) 中，给定 Y，X 与 Z 独立 → X 不是 Z 的直接原因。
- 但 X 仍是 Z 的原因（在 \(P^{\mathrm{do}(X)}\) 里，通过 Y 传递依赖）。

干预图 \(G^{\mathrm{do}(\{Y\})}\)：删除指向 Y 的入边（即 \(X \to Y\)），得到
```
X     Y → Z
```
（Y 现在无入边，等于外部随机化）

**核心思想**：只要给定一个**同时满足一致性与交性质**的干预分布族，原因和直接原因就可以直接读出来，因果图由直接原因定义，然后自动满足马尔可夫性质，从而回到传统因果推理的起点，**而不需要首先写出 SCM 方程**。

---

### 三、报告主体：讲者讲了什么

**[H:MM] 标注来自转写稿的 ASR 时间戳，可能有 ±30 秒偏差。**

---

**[0:01:37]** 开场：讲者 Kayvan Sadeghi（UCL）介绍这是与 Philip Dawid 和 Terry Soo 的 joint work，尚未投稿，主要理论部分已完工。强调替代输入：**不从图或 SCM 出发，而从干预分布族出发**。

**[0:02:49–0:03:29]** 核心架构：
- 干预是硬（摧毁原因）、随机（用独立随机变量替代分布）的——但也适用于原子干预（conditioning）。
- **输入**：族 \(\mathcal{P}^{\mathrm{do}}\)，输出：因果概念（cause、direct cause） + 因果图 \(G(\mathcal{P})\)。
- 然后提出几个“自然”性质，使干预分布对该图满足马尔可夫性；一旦有马尔可夫性，大量因果推理理论直接可用。

**[0:03:43–0:04:39]** 适用范围：理论核心是 DAG，但自然推广到**有向循环图**（部分证明进行中）和**带潜变量**（用双向边表示）的情况。

**[0:04:48–0:05:11]** 与前作关系：单一干预的版本发表在 Biometrika 2025（Sadeghi & Soo）。多重干预使理论**更简洁**。

**[0:05:13–0:06:57]** 图形模型速览：d-separation / m-separation / σ-separation；全局马尔可夫性质的定义；指出“SCM 的联合分布对因果图满足马尔可夫性质”是 SCM 能做因果推断的核心定理（Pearl, 1988; Sadeghi & Soo, 2022 for ancestral graphs; Bongers et al., 2021 for directed graphs）。

**[0:09:14–0:11:30]** **定义干预分布族**（Slide 6）：
- 对于每个 \(A \subseteq V\)，给定一个联合分布 \(P^{\mathrm{do}(A)}\)。
- **原因定义**：\(i \in \mathrm{cause}(k)\) iff \(X_i \not\perp\!\!\!\perp_{P^{\mathrm{do}(i)}} X_k\)。（仅使用单变量干预分布）
- **直接原因定义**（Slide 7）：\(i \in \mathrm{dcause}(k)\) iff \(X_i \not\perp\!\!\!\perp_{P^{\mathrm{do}(V\setminus\{k\})}} X_k \mid X_{V\setminus\{i,k\}}\)。（使用“除 k 外全干预”的分布）

**[0:13:09–0:14:40]** 因果图生成（Slide 8）：
- \(G(\mathcal{P})\)：箭头 \(i \to k\) 当且仅当 \(i \in \mathrm{dcause}(k)\)。
- 讲者明确：**因果图是构造的，不是假定的**。
- 干预图 \(G^{\mathrm{do}(A)}\)：删除所有指向 A 的入边。

**[0:19:46–0:21:30]** **三个假设**（Slide 9）——核心部分：

1. **一致性**（Assumption 1）：若在 \(P^{\mathrm{do}(A)}\) 中 \(D \perp\!\!\!\perp E \mid A\setminus(D\cup E)\)，则对任意 \(B \supseteq A\)，在 \(P^{\mathrm{do}(B)}\) 中该独立性成立。  
   → 直觉：干预越多，独立性只增不减。

2. **交性质**（Assumption 2）：每个 \(P^{\mathrm{do}(A)}\) 满足交性质（sufficient condition：有正密度/全支撑）。

3. **模块性**（Assumption 3——Slide 9 最下一行）：对任意 \(A \subseteq V\)，任意 \(k \notin A\)，
   \[
   P^{\mathrm{do}(A)}(x_k \mid x_{\mathrm{nd}_{G^{\mathrm{do}(A)}}(k)}) = P(x_k \mid x_{\mathrm{nd}_G(k)}).
   \]
   （“nd” = 非后代）。  
   这条直接连接干预分布与观测分布的条件分布，**是三条中最不平凡的一条**。  
   → 讲者澄清（[0:22:09]）：因为图是生成的，非后代实际是一串直接原因的链条，公式不依赖图的先验知识。

**[0:24:45–0:25:07]** 第一个推论（假设 1 的直接结果）：若 \(i \in \mathrm{dcause}(k)\) 则 \(i \in \mathrm{cause}(k)\)。

**[0:25:49–0:27:00]** **主要定理**（Slide 10）：
- 若 \(i \in \mathrm{cause}(k)\) 则 \(i\) 是 \(G\) 中 \(k\) 的祖先。
- 在干预分布 \(P^{\mathrm{do}(A)}\) 下，所有被干预节点 \(A\) 相互独立。
- **核心定理**：对任意 \(A \subseteq V\)，\(P^{\mathrm{do}(A)}\) 对图 \(G^{\mathrm{do}(A)}\) 满足全局马尔可夫性质。

**[0:30:44–0:31:50]** 推论（Slide 10 下半部分）：
- 观测分布 \(P\) 对 \(G\) 马尔可夫。
- 对任意 \(A, B\) 和任意 \(k \notin A\cup B\)，若条件集合 \(C_A\) 包含父母、是 \(G^{\mathrm{do}(A)}\) 中 \(k\) 的非后代，则
  \[
  P^{\mathrm{do}(A)}(x_k \mid x_{C_A}) = P^{\mathrm{do}(B)}(x_k \mid x_{C_B}) = P(x_k \mid x_{\mathrm{par}(k)}).
  \]
- 若 \(k\) 的祖先集与 \(A\cup B\) 不交，则 \(P^{\mathrm{do}(A)}(x_K) = P^{\mathrm{do}(B)}(x_K)\) 边际相等（[0:31:51]：“干预在下面，边际不变”）。

**[0:33:33–0:35:05]** **反向构建**（Slide 11）：给定 \(P\)（观测）和 \(G\)，可以构造整个干预族 \(\mathcal{P}^{\mathrm{do}}\)。方法：用上面推论先定义条件分布 \(P^{\mathrm{do}(A)}(x_k \mid x_{\mathrm{par}(k)})\)（对 \(k\notin A\)）；对 \(k\in A\)，自由指定干预分布；然后按干预图因式分解得全联合。这一构造自动使所得分布对 \(G^{\mathrm{do}(A)}\) 满足马尔可夫性。

**[0:38:02–0:39:20]** **推广到有向循环图**（Slide 12，work in progress）：
- 因果图 \(G\) 可以由直接原因定义出循环边。
- Assumption 3 需要修改：不再是单一节点 \(k\) 的条件分布，而是整条**环（强联通分量）**的条件分布。
- 主要定理：\(P^{\mathrm{do}(A)}\) 对 \(G^{\mathrm{do}(A)}\) 按 σ-separation 满足马尔可夫性。
- 附加结果：若观测分布 \(P\) 以 d-separation 对 \(G\) 马尔可夫，则对环上非 A 祖先的部分，干预分布也满足 d-separation。

**[0:40:24–0:42:50]** **推广到潜变量**（Slide 13）：
- 因果图增加双向边（bidirected edges）：对缺失有向边的节点 \(i, j\)，若在 \(P^{\mathrm{do}(V\setminus\{i,j\})}\) 中 \(X_i\) 与 \(X_j\) 不独立，则添加 \(i \leftrightarrow j\)。
- 修正 Assumption 3：用“bidirected chain component of \(k\)”的非后代代替 \(k\) 的非后代。
- 定理：\(P^{\mathrm{do}(A)}\) 对 \(G^{\mathrm{do}(A)}\) 按 **m-separation** 满足马尔可夫性。

**[0:44:54–0:48:50]** **与 SCM 的关系**（Slide 15–18）：
- SCM 给出：真实因果图 \(G_C\)、观测分布 \(P_C\)、以及所有标准干预分布。
- 但若先有 \(\mathcal{P}^{\mathrm{do}}\)，可恢复 \(G\) 和 \(P\)；反之亦然。因此 SCM 带冗余信息——**干预分布与 (P, G) 实际上是一回事**，不是 SCM 额外提供的。
- **Edge-cause condition**：是不是 SCM 图中的箭头 \(i \to j\) 就能推出 \(i \in \mathrm{dcause}(j)\)？不一定。给出二进制加法反例（[0:52:07]）：
  \[
  Y = X + \epsilon_Y \pmod{2},\quad \epsilon_Y \sim \mathrm{Ber}(1/2).
  \]
  此处 X 不是 Y 的直接原因（因为无论在 \(P^{\mathrm{do}(V\setminus\{Y\})}\) 还是 \(P^{\mathrm{do}(X)}\)，X、Y 仍独立）。
- **结论**（[0:53:02]）：多数“自然”SCM 满足三个假设；但**任意函数形式的 SCM 可能违反它们**，并带来不必要的复杂性（例如循环 SCM 的强可解性要求）。

**[0:58:34–0:59:20] Q&A：实际数据分析中如何用这个框架？**
- 讲者表示他们正在研究**只有部分干预集（subset of A）可观测时的部分识别与结构学习**，作为纯理论与结构学习之间的桥梁。
- 干预分布可以用非参数方法从数据估计，然后直接在其上操作，不需要假设函数形式。

---

### 四、对应论文与开放问题

**对应论文**：
- 直接对应的手稿**尚未提交**（讲者 [0:01:47] 明确：“it's still in progress, we haven't submitted it”），标题大概同报告标题“A theory of causality with multiple interventions”。
- 前序已发表工作：**Sadeghi & Soo (Biometrika, 2025)** ——单一干预的类似理论。
- 图中马尔可夫性质的已有证明参考：Pearl (1988, DAGs), Sadeghi & Soo (2022, ancestral graphs), Bongers et al. (2021, directed graphs)。
- 讲者未提及 arXiv 号或完整参考文献列表。

**开放问题**（每条扎根于转写）：

1. **部分可观测干预集**（[0:59:10–0:59:28]）：若观测到的不全是“每个 A 对应一个分布”，而是只有一半干预集，能否部分识别因果图？讲者正在探索，但尚未有成熟结果。  
   → 这对实证因果推断是一个天然缺口：现实实验很少能做 2^n 种干预。

2. **与“causal space”框架的比较**（[1:01:00]）：有听众问是否关联到“causal space”（近年由学者如 Evans, Didelez 等发展的另一种无 SCM 因果框架）。讲者坦承尚未比较。  
   → 这是一个显式的空白，蕴含可能的 unifying 或 critique 工作。

3. **如何将“干预分布族”具体化为统计模型与估计方法**（[0:58:36–0:59:06]）：观众提问实际数据分析中如何“生成一个有意思的 intervention 分布族”。这揭示本理论目前是抽象存在性层面，未下沉到可操作的**参数化空间**。  
   → 可能需要 受约束的概率模型（如带有“模块性”假设的 GAN / normalizing flow），或 与半参数因果估计的桥接。

4. **循环图下的完整证明 / 观测分布的存在性**（[0:54:15–0:55:30]）：关于循环情况下观测分布 \(P\) 是否一定存在。讲者承认有“一致性”（consistency）问题（而非 SCM 的可解性问题），但认为比 SCM 循环情形容易。  
   → 需澄清在纯公理框架下何时 \(P\) 可被干预分布族“拼出来”。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

