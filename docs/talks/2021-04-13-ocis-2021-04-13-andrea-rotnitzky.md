# Optimal adjustment sets in non-parametric graphical models

**讲者**: Andrea Rotnitzky  
**讨论人**: Ema Perkovi c  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2021-04-13  
**主题**: 因果推断  
**视频**: <https://youtu.be/VBfMhMaIE-8> · [幻灯片](https://drive.google.com/file/d/1WDfsU2dyaVrodyYi91nljBiwQogd1uAZ/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告属于**因果推断中的混淆控制（confounding control）与调整集选择**这一子方向。这个方向追问的核心问题是：**在一项观测研究中，当我们有一个因果图模型（DAG）作为背景知识时，存在多个能够有效控制混淆的协变量调整集，究竟选择哪一个，能使后续的非参数估计量具有最小的渐近方差？**

**奠基与主流路线：**

- **经典后门准则 (Pearl, 1995)**：给出了调整集充分的图条件，但不完备（只提供充分条件，非必要条件）。
- **广义调整准则 (Shpitser et al., 2010; Perkovic et al., 2015, 2018)**：给出了调整集**充分且必要**的图条件，是当前判断一个集合是否为有效调整集的完备工具。
- **枚举所有有效调整集的图算法 (van der Zander, Liskiewicz & Textor, 2019)**：使得在给定DAG下找到所有候选调整集成为可能，为后续的最优选择问题铺平了道路。
- **方差比较以选择最优调整集 (Henckel, Perkovic & Maathuis, 2019)**：这是本报告最直接的先驱工作。该论文在**线性结构方程模型 (Linear SEM)** 的假设下，用 **OLS（普通最小二乘法）** 作为估计方法，给出了在DAG及部分有向无环图（CPDAG, MAG）上比较调整集方差的图规则，并定义了"全局最优静态调整集"O-set。

**当前Frontier与本报告的站位：**

本报告（及其源自的两篇论文，Rotnitzky & Smucler, 2020 JMLR; Smucler, Sapienza & Rotnitzky, 2021 Biometrika）**将Henckel et al. (2019)的线性/OLS框架推广到了非参数（non-parametric）或半参数（semiparametric）的估计环境**。也就是说，假设我们要用**非参数方法**（如核回归、随机森林等机器学习方法）来估计倾向得分和/或结果回归（即正交/双重稳健估计量），问题依然是：哪个调整集能使这个非参数估计量的渐近方差最小？报告证明了，在这种更一般、更接近现代因果推断实践的设置下，**Henckel et al. (2019) 发现的"全局最优调整集" O-set 依然是全局最优的**（对于静态处理），并进一步分析了：
1.  **动态（个性化）处理**下的最优Z-调整集（O-set ∪ Z）。
2.  **最小调整集**（最小、最少变量数量）中的最优者。
3.  **存在隐变量**时，全局最优可能不存在，并提出可操作解。
4.  **何时该非参数调整估计量能达到半参数效率界**。

该工作线不回答"如何构造最优估计量"（这是高维/半参数效率理论的方向），而是回答"给定一种非参数估计策略，选择哪个协变量测量集能最大化其统计效率"。

### 二、最小内核 / 一个最简例子

**符号与模型设定：**
- **可观测数据**：$(Y_i, A_i, Z_i, G_i), i=1,...,n$，其中：
  - $A$：二值处理变量（如服药与否）。
  - $Y$：连续结果变量（如血压）。
  - $Z, G$：两个协变量（如年龄、既往史）。
- **目标估计量 (estimand)**：平均处理效应 (ATE) $\psi = E[Y(1) - Y(0)]$，其中 $Y(a)$ 是反事实结果。
- **因果图**：一个DAG（有向无环图），已知 $A \rightarrow Y$，且 $A$ 和 $Y$ 之间有两条后门路径（back-door path）：
    1.  $A \leftarrow Z \rightarrow Y$
    2.  $A \leftarrow G \rightarrow Y$
   此外，图中 $Z$ 和 $G$ 之间没有边。
- **核心概念：调整集 (Adjustment Set)**：一个变量集合 $L$ 是有效的静态调整集，当且仅当用 $L$ 进行**G-公式**（或IPW, AIPW）调整后，可以无偏地识别ATE：$\psi = E[ E(Y|A=1, L) - E(Y|A=0, L) ]$。在此例中，$L_1 = \{Z\}$, $L_2 = \{G\}$, $L_3 = \{Z,G\}$ 都是有效调整集。

**核心问题：**
我们应该选择调整 $L_1$, $L_2$ 还是 $L_3$？如果使用非参数估计量的“L-调整估计量”（如用核回归估计 $E(Y|A=a,L=l)$ 然后做G-公式），哪一个调整集会使得该估计量的**渐近方差**最小？

**最小内核思想：**
在此特例中，由报告的结果可知：
1.  **只调整一个协变量**（$L = \{Z\}$ 或 $L = \{G\}$）可以识别ATE。
2.  **调整两个协变量**（$L = \{Z,G\}$）也能识别ATE。因为 $G$ 和 $Z$ 之间无关联，且都直接预测结果 $Y$，所以它们可以互相作为对方的“精度变量（precision variable）”。根据报告的**补充（supplementation）** 结果，添加一个不进一步预测处理的变量（如向 $\{Z\}$ 中添加与 $A$ 独立、但与 $Y$ 相关的 $G$）能降低方差，**永远不会伤害**。因此，$\{Z,G\}$ 的渐近方差会比 $\{Z\}$ 或 $\{G\}$ 都小。但问题是，$\{Z,G\}$ 是否已经是全局最优？
3.  报告的**全局最优调整集 O-set**：它是所有非后代（non-descendants）的、且是 $Y$ 的父节点（parent）或因果路径上中介变量的父节点的集合。在此例中，若图中没有中介，则 $O = \{Z, G\}$（如果两者都是 $Y$ 的父节点）。因此，最优解正是 $L_3 = \{Z,G\}$。这个结论与调整集的具体预测能力无关，是**图结构层面的结论**。

### 三、报告主体：讲者讲了什么

**[0:00 - 0:12]** 引言与动机
*   **问题定义**：在计划一项观测研究时，需要测量哪些协变量以控制混淆。当存在多个有效调整集时，选择哪一个能使**非参数调整估计量**（如IPW、AIPW等，其中倾向得分、结果回归用非参数方法估计）的渐近方差最小。这个问题是为了指导**研究设计**（design stage）。
*   **分类**：考虑了静态（static, 统一处理）和个性化（personalized / dynamic, 处理取决于Z）的处理。将调整集分为全局（所有有效集）、最小（minimal, 移去其中任一个变量便失效）、最小尺寸（minimum, 最小基数）以及这些类别的“可观测”版本（当部分变量不可测时）。

**[0:12 - 0:15]** 示例热身
*   **简单DAG例子**（幻灯片第4-7页）：
    *   图1：$A \rightarrow Y$, $A \leftarrow Z \rightarrow Y$, $A \leftarrow G \rightarrow Y$。$Z$ or $G$ or $\{Z,G\}$ 都是有效调整集。问：哪个方差最小？
    *   图2：同上，但处理是动态的（如 $A=1$ if $Z>z$）。有效调整集必须包含 $Z$，因此是 $\{Z\}$ 或 $\{Z,G\}$。
*   **复杂DAG例子**（幻灯片第8页）：
    *   展示了存在最小调整集（如$\{H1, H2\}$, $\{T\}$等）和最小尺寸调整集（如$\{T\}$, $\{R\}$）。调整集的类别不是唯一的，它们无法直接比较。

**[0:15 - 0:29]** 背景：因果图模型与调整集形式化
*   **因果DAG模型**：非参数因果（agnostic）模型，假设事实世界的分布根据图分解，干预世界的分布由截断公式（truncation formula）给出。本报告专注于**单点暴露（univariate A）**。
*   **Z-调整集的定义**：$L$ 是 $Z$-调整集，需满足 (i) $Z \subseteq L$; (ii) 对于任何依赖于 $Z$ 的处理 regime $\pi(a|z)$，干预均值可由G-formula用 $L$ 识别（即对于任何函数 $h(Y)$）。
*   **非参数 L-调整估计量**：用非参数方法估计 $E(Y|A,L)$ 和/或 $P(A|L)$ 的G-formula估计量。
*   **调整集的图特征**：
    *   **后门准则** (Pearl, 1995): 充分但不完备。
    *   **广义调整准则** (Shpitser, Perkovic等人): **充分且完备**。
    *   **关键结论**：所有 $Z$-调整集 = 所有包含 $Z$ 的静态调整集。这为通过枚举静态调整集（van der Zander et al., 2019算法）来找到 $Z$-调整集提供了理论依据。
*   **异步方差与影响函数**：
    *   **关键点**（本报告理论基石）：在适当复杂度条件（如Donsker类）下，所有正则、渐近线性的 L-NPA 估计量收敛到相同的**正态分布**，其渐近方差 $\sigma^2_{\pi,L}(p)$ 等于该G-functional在**非参数模型下**的唯一影响函数的方差。
    *   这提供了一个**统一的比较标准**：比较不同调整集 $L$ 的渐近方差，等价于比较它们对应影响函数的方差。

**[0:29 - 0:50]** 主要结果
*   **结果1: 精度变量的添加（Supplementation）** [0:29]
    *   若 $B$ 是 $Z$-调整集，且 $G$ 在给定 $B$ 下与 $A$ $d$-分离，则 $\{B,G\}$ 也是 $Z$-调整集，且对于所有 $P$ 和所有 $\pi$，有 $\sigma^2_{\pi, B \cup G}(p) \le \sigma^2_{\pi, B}(p)$。添加一个**不预测处理**的变量**永远不会伤害**（can never hurt）。
    *   **静态ATR公式**：方差减少量 $\propto E \left[ \frac{Var(Y|A=a,B)}{P(A=a|B)} - \frac{Var(Y|A=a,B,G)}{P(A=a|B)} \right]$。直觉上，当 $G$ 是**$Y$ 的强预测变量**，且 $B$ 中 $P(A=a|B)$ 小的层（即处理稀少层）时，减少最显著。这复现了Hahn (1998) 的经典结论。
*   **结果2: 过调整变量的去除（Deletion）** [0:33]
    *   若 $\{B,G\}$ 是 $Z$-调整集，且 $B$ 在给定 $\{G,A\}$ 下与 $Y$ $d$-分离（即$B$不进一步预测$Y$），则 $G$ 也是 $Z$-调整集，且 $\sigma^2_{\pi, G}(p) \le \sigma^2_{\pi, B \cup G}(p)$。去除一个**不预测结果**的变量**可以降低**方差。
*   **结果3: 排序引理（Corollary）** [0:35]
    *   若两个调整集 $G$ 和 $B$ 满足：(i) $G \backslash B$ 不预测 $A$ (clear sign); (ii) $B \backslash G$ 不预测 $Y$ ( weak arrow), 则 $G$ 总是优于或等于 $B$。证明通过添加删减序列实现。这提供了一个**图上的可检验条件**来比较调整集。
*   **结果4: 全局最优调整集（O-set）** [0:38]
    *   **静态处理**：设 $O$ 为所有**非后代（non-descendants）** 的、且是 $Y$ 或其**中介变量**的**父节点（parents）** 的集合。Henckel et al. (2019) 在线性OLS框架下证明 $O$ 是全局最优的。**本报告的核心贡献**：**证明了这个结论在非参数调整估计中同样成立**。因为 $O$ 满足上面排序引理中的条件(i)(ii)（$O$ 中的变量是precision variables，不预测$A$；$O$ 外的变量预测$A$但不预测$Y$，可以安全删除），所以 $O$ 是全局最优静态调整集。
    *   **$Z$-动态处理**：全局最优 $Z$-调整集为 $O \cup Z$。
    *   **示例**：在运动热身图上，最优集是{年龄，性别，以前受伤情况？}（具体变量依赖于图结构）。讲者当时口述了一个例子被ASR听错，但幻灯片第4-5页显示了正确的结构。
*   **结果5: 最优最小调整集** [0:43]
    *   如果用户希望使用最小调整集（即无法再删除任何变量而不破坏有效性），那么**$O$ 集合本身包含一个唯一的最小调整集**。该最小集可以借由从 $O$ 中递归删除与 $A$ 条件独立的变量得到。讲者称这个最小调整集为 $O_{\text{min}}$，它是最优最小调整集。
*   **存在隐变量的情形** [0:44]（快节奏，语速快，难抓全）
    *   **负面结果**：存在隐变量时，在所有可观测调整集中，**全局最优调整集可能不存在**。因为两个候选集（如空集 vs. $\{L1,L2\}$）的优越性依赖于无法被图固定的参数值（如隐变量 $U$ 与 $A$ 和 $Y$之间的关联强度）。
    *   **正面结果**：但**最优最小调整集**和**最优最小尺寸调整集**在可观测集中总是存在的（只要至少有一个可观测调整集）。论文提供了多项式时间算法（基于latent projected undirected moralized graph）来找到它们。
*   **[0:47]** 讲者简短提到半参数效率（Semiparametric Efficiency）结果：在某些图结构下，仅使用最优调整集进行非参数调整就能达到半参数效率界（即即使你测量了所有图上的变量，也无法做得更好）。这对应2020年JMLR论文的核心结果之一（第4-5节）。
*   **[0:48]** 开放问题：讲者快速提到时间依赖混淆（Time-dependent confounding）和多重处理（multiple treatment）情形下，**即使无隐变量，全局最优调整集也可能不存在**，这是一个更复杂的情景。同时，强调了**成本约束**下的调整集选择问题（cost of measurement），作为未来方向。

**[0:50 - 1:06]** 讨论环节（由Ema Perkovic 主持）
*   Perkovic 的讨论提及了这些结果与线性SEM框架下结果的一致性，以及对**CPDAG（部分有向无环图，代表等价类）** 的推广展望。她提了一个开放问题：如何将本报告关于时间依赖调整的结果推广到CPDAG。
*   讲者Rotnitzky在回应中强调了其工作与Henckel et al. (2019)在假设上的区别（线性vs.非参），并认为CPDAG视角更适用“事后数据分析”，而非“研究设计”（因为设计阶段图是通过专家先验给定的，不是从数据学习的）。她也预告了与Perkovic合作的新工作（关于半参数效率中哪些变量不可忽略）。

### 四、对应论文与开放问题

**(a) 对应论文**

*   **核心论文1**：Rotnitzky, A., & Smucler, E. (2020). Optimal adjustment sets in non-parametric graphical causal models. *Journal of Machine Learning Research, 21*(188), 1-86.
    *   对应报告中大部分理论结果（补充、删除、O-set最优性、半参数效率）。
*   **核心论文2**：Smucler, E., Sapienza, F., & Rotnitzky, A. (2021). Efficient adjustment sets in non-parametric graphical causal models with hidden variables. *Biometrika, 109*(1), 149-166. https://doi.org/10.1093/biomet/asab018
    *   对应报告中关于隐藏变量的结果（可观测O-set可能不存在，但最优最小/最小尺寸调整集存在及其算法）。
*   **直接先驱工作**：Henckel, L., Perkovic, E., & Maathuis, M. H. (2019). Graphical criteria for efficient total effect estimation via adjustment in causal linear models. *Journal of the Royal Statistical Society: Series B (Statistical Methodology), 81*(5), 1069-1092.
*   **枚举算法工作**：van der Zander, B., Liśkiewicz, M., & Textor, J. (2019). A complete and efficient algorithm for enumerating all valid back-door adjustment sets. *Journal of Artificial Intelligence Research, 65*, 789-810.

**(b) 开放问题**

*   **成本约束下的最优调整集** (时间线: 0:48)：
    > "assume the cost of an adjustment set is cl... we want to find the adjustment set that minimizes... over all... cost constraint... we don't think this problem is solvable..."
    这是一个尚无通用解的问题：当每个变量的测量成本不同时，如何在预算约束下找到方差最小的调整集（对所有分布而言）。
*   **半参数效率的完备特征** (时间线: 0:47, 讨论中提及)：
    > "...we have a complete and sound algorithm to determine when you don't really need to measure all the other variables... attains the semiparametric efficiency bound..."
    虽然论文给出了达到效率界的充分条件（某些图下O-set就够），但在更一般图中，如何系统性地判断哪些变量是高效估计所必须测量的，是开放问题（讲者提到有相关工作在进展）。
*   **多重处理与时间依赖混淆** (时间线: 0:48)：
    > "...multiple treatment and time dependent confounding... not so exciting because there are graphs which not even a globally optimal adjustment set exists..."
    当存在多个顺序处理变量时，定义和寻找单一最优调整集本身就有困难，甚至可能不存在。如何为一个时间序列的因果关系设计高效的调整策略是开放领域。
*   **等价类（如CPDAG）上的推广** (讨论环节, 时间线: 0:55)：
    > (Perkovic) "when can you extend these results to these equivalence classes... an interesting open question here is how you would identify what is this time dependent variable adjustment set..."
    当一个因果图是从数据中学习的（因此是不确定的等价类，如CPDAG）时，本报告的结论（如O-set的定义、算法）如何推广到这类图上？特别是对于时间依赖的调整。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

