# Total causal effect estimation by combining causal structure learning and covariate adjustment

**讲者**: Marloes Maathuis  
**讨论人**: Daniel Malinsky  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-06-30  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=fpildpVeRTk> · [幻灯片](https://drive.google.com/file/d/1IQBi6bZFpVc5jKFIoqneCzQcYFZmbJfD/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2002.06825](https://arxiv.org/abs/2002.06825) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

报告将两条通常被分开处理的工作线——**因果结构学习**（从观测数据学习因果图）与**协变量调整**（利用已知图估计因果效应）——整合为一条端到端的流程，用于估计**总因果效应**（total causal effect）。核心追问是：*当因果图未知时，如何从观测数据可靠且有效地估计总因果效应，并尽可能减小估计方差？*

**奠基与主流路线**  
- 当因果有向无环图（DAG）已知时，协变量调整（back-door adjustment）是识别总因果效应的标准工具。Pearl (1993) 的 back-door 准则、Shpitser et al. (2010) 和 Perković et al. (2018) 的 adjustment criterion 给出了 DAG 上所有有效调整集的图论刻画。针对线性结构方程模型，调整后的 OLS 回归给出相合估计。  
- 但当 DAG 未知时，只能从观测数据中学习其 Markov 等价类（用 CPDAG 表示）。经典的 IDA 算法（Maathuis, Kalisch & Bühlmann, 2009; Maathuis et al., 2010）首先估计 CPDAG，然后枚举每个可能 DAG 中处理变量 X 的父集（parent set）作为调整集，得到一个多重集（multi-set）的因果效应估计，再通过最小绝对值等汇总得到下界。IDA 在高维稀疏设定下具有一致性（Maathuis et al., 2009, 2010），并扩展到联合干预（Nandy et al., 2017）和带背景知识的 CPDAG（Perković et al., 2017）。  
- 存在隐变量时，结构学习扩展到 MAG/PAG（FCI 算法系列，Spirtes et al., 2000; Colombo et al., 2012），LV-IDA（Malinsky & Spirtes, 2017）在 MAG 级别做调整；另一路线假设隐变量少且影响多个观测变量（低秩+稀疏结构），如 LRpS-GES（Frot et al., 2019），输出 CPDAG 从而可用标准 IDA。

**当前 Frontier 与本报告的站位**  
- 报告聚焦于 **效率**：在所有有效调整集中，哪一个能最小化估计的渐近方差？Henckel, Perković & Maathuis (2019) 在**线性模型**下给出了 O-set（最优调整集）的图论刻画和构造方法。  
- Witte, Henckel, Maathuis & Didelez (2020, arXiv:2002.06825) 进一步给出 O-set 的新直观特征——**禁忌投影（forbidden projection）**：将 DAG 中对调整无信息的节点（禁点）边缘化后，O-set 就是结果变量 Y 在该投影图中的父集。这一投影保持了所有有效调整集的信息，提供了一种更易理解且可直接计算的视角。该论文还将 O-set 引入 IDA 流程（称为“最优 IDA”），并证明其在非参数调整估计中仍保持最优性（基于 Rotnitzky & Smucler, 2019 的工作）。  
- 此外，报告将调整准则完整推广到了 **CPDAG、MAG、PAG**（Perković et al., 2015, 2018），使得调整不再局限于已知 DAG，而能直接在图类的代表性图上进行判断。  
- 这条工作线的核心在于：**不追求全图的精确恢复，而是直接服务于估计，同时兼顾计算可扩展性与统计效率**。报告以拟南芥基因表达数据（n=188, p=33）为实际案例，展示了不同隐变量假设下效果。

### 二、最小内核 / 一个最简例子

为理解报告核心思想，考虑一个仅含**两个混淆变量**的简单线性 DAG（取自幻灯片示例的简化版）：

**符号与模型**  
- 可观测随机变量：\(X\)（处理）、\(Y\)（结果）、\(Z_1, Z_2, Z_3, Z_4\)（协变量）。  
- 结构方程（系数已给定）：  
  \[
  X = Z_1 + Z_2 + \varepsilon_X, \quad Z_5 = 0.8X + Z_4 + \varepsilon_{Z_5}, \quad Y = Z_2 + 2Z_5 + Z_7 + \varepsilon_Y,
  \]
  其中 \(\varepsilon\) 是独立标准正态噪声，\(Z_1, Z_2, Z_4, Z_7\) 是外生标准正态。  
- 总因果效应定义为 \(\frac{\partial}{\partial x} \mathbb{E}[Y \mid do(X=x)]\)，在线性模型中等于从 \(X\) 到 \(Y\) 所有有向路径的边权乘积之和：此处唯一路径 \(X \to Z_5 \to Y\)，乘积为 \(0.8 \times 2 = 1.6\)。

**一个最简特例**：假设图中只有 \(X, Y\) 和一个混淆变量 \(Z_2\)（\(Z_2\) 同时指向 \(X\) 和 \(Y\)），且 \(X\) 与 \(Y\) 之间无中间变量（即 \(Z_5\) 不存在）。则总效应就是回归 \(Y\) on \(X\) and \(Z_2\) 时 \(X\) 的系数。此时：
- **有效调整集**必须包含 \(Z_2\)（block 从 \(X\) 到 \(Y\) 的非因果路径 \(X \leftarrow Z_2 \to Y\)），且不能包含任何位于因果路径上的变量（此时无中继节点，因此不包含 \(Y\) 的子孙或 \(X\) 的后代）。  
- 若只用空集（回归 \(Y\) on \(X\) 忽略 \(Z_2\)），得到有偏估计（例如 1.94 而非 1.6）。  
- 若加入 \(X\) 的后代如 \(Z_5\)（假设存在），则部分阻断因果路径，导致有偏。

**更一般的例子（含中间变量）**  
回到完整图（幻灯片 R code 示例），总效应 1.6。有效调整集必须：
1. 不含任何位于因果路径上的节点或其子孙（\(Z_5, Z_6, Y, Z_8\) 为禁点）；  
2. 包含 \(Z_2\) 来阻断唯一的非因果路径 \(X \leftarrow Z_2 \to Y\)。  
所以任意含 \(Z_2\) 且不含禁点的子集均有效，如 \(\{Z_1, Z_2\}\), \(\{Z_2, Z_3\}\), \(\{Z_2, Z_4, Z_7\}\) 等。但不同调整集给出不同方差。最优调整集 O-set = \(\{Z_2, Z_4, Z_7\}\)（来自 Henckel et al.）：它包含 \(Z_4\) 解释 \(Y\) 更多方差，而不包含与 \(X\) 强相关的 \(Z_1\) 或 \(Z_3\)，从而最小化 OLS 估计的渐近方差。

### 三、报告主体：讲者讲了什么

按时间顺序与幻灯片结构，结合转写整理如下（时间戳 [H:MM:SS] 来自视频，可能有秒级偏差）：

**[0:00–0:06] 引言与动机**  
- 背景：拟南芥基因表达数据（n=188, p=33），目标是从观测数据估计基因对之间的总因果效应（干预性解释）。  
- 定义：使用 do-算子，总因果效应为 \(\frac{\partial}{\partial x} \mathbb{E}[Y \mid do(X=x)]\)。 [0:02:45–0:04:07]  
- 关键假设：数据由某个未知的因果 DAG 生成，且观测分布满足 Markov 性和 faithfulness。通过 truncated factorization 将干预分布表示为观测条件密度的乘积。 [0:05:07–0:06:33]

**[0:06:48–0:15:53] 第一部分：协变量调整（DAG 已知）**  
- 有效调整集 S 的定义：\(f(y \mid do(x)) = \int f(y \mid x,s) f(s) ds\) 对所有与 DAG 兼容的分布成立。 [0:07:08–0:07:34]  
- 线性模型下，总效应等于回归 \(Y \sim X + S\) 中 \(X\) 的系数。父集 pa(X) 总是有效的（若 \(Y \notin \text{pa}(X)\)）。 [0:08:27–0:09:01]  
- 幻灯片示例（线性 STRUCTURAL EQUATION MODEL）演示不同调整集的后果：pa(X)={Z1,Z2} 给出 1.611；空集 1.940 (有偏)；{Z2,Z6} 0.542 (有偏)；{Z2,Z4,Z7} 1.604 (有效且更优)。 [0:09:16–0:13:10]  
- DAG 上有效调整集的充要条件（Shpitser et al. 2010; Perković et al. 2018）：
  1. Z 不得包含任何位于从 X 到 Y 的 proper causal path 上的节点 W (∉X) 的后代；
  2. Z 必须阻断所有 proper non-causal path 从 X 到 Y。  
  以此为例，有效集为 {Z2} ∪ S，其中 S ⊆ {Z1,Z3,Z4,Z7}。 [0:13:16–0:15:53]

**[0:15:57–0:23:11] 因果结构学习与 IDA 方法**  
- 多个 DAG 可编码相同 d-separation 关系，形成 Markov 等价类，由 CPDAG 唯一描述。CPDAG 可从观测数据中识别（假设 Markov + faithfulness）。 [0:16:26–0:18:00]  
- 三类结构学习方法：  
  - 基于约束的 PC 算法（Spirtes et al. 2000）；高维一致性（Kalisch & Bühlmann 2007）；顺序无关版本（Colombo & Maathuis 2014）。  
  - 基于分数的 GES（Chickering 2002）；高维一致性（Nandy et al. 2018）。  
  - 混合方法（如 MMHC, ARGES）。  
- IDA 框架：估计 CPDAG → 枚举所有可能 DAG → 对每个 DAG 用 pa(X) 做调整回归 → 得到多重集。优点：pa(X) 可由 CPDAG 局部读出，无需完整枚举。 [0:19:08–0:22:38]  
- 多重集可汇总为 bounds（如最小绝对值作为效应大小下界）。 [0:22:41–0:23:11]

**[0:23:12–0:26:19] 存在隐变量的扩展**  
- 允许任意多隐变量：FCI 算法（Spirtes et al. 2000; Colombo et al. 2012）输出 PAG（MAG 的等价类）；LV-IDA（Malinsky & Spirtes 2017）在 MAG 级别做调整。 [0:24:00–0:24:37]  
- 折中假设：少量隐变量影响多数观测变量（低秩+稀疏分解），如 LRpS-GES（Frot et al. 2019），输出 CPDAG 后可用标准 IDA。 [0:24:59–0:26:14]

**[0:26:27–0:29:13] 实际数据分析：拟南芥基因数据**  
- 结果对比：GES-IDA 发现大量可能因果效应；LV-IDA 仅找到 3 个非零下界（非常保守）；LRpS-GES-IDA 居中，且显示线粒体基因与其他通路基因间效应很弱（白色块），符合生物直觉。 [0:26:29–0:29:13]

**[0:29:58–0:33:03] 问答环节（第一部分结束前）**  
- 问题：调整集的计算效率。回答：R 包 pcalg 和 dagitty 可快速判断有效集、列出所有有效集。关于最小调整集：虽节省测量成本，但未必效率最优。 [0:30:00–0:31:51]  
- 问题：可处理的变量规模。回答：几千个变量可行，取决于图稀疏度和调参。 [0:31:58–0:32:56]

**[0:33:09–0:36:41] 第二部分：在 CPDAG/PAG 上直接做调整**  
- 示例：有些 CPDAG 中不存在对所有 DAG 都有效的调整集（如三条链的 CPDAG），有些存在（如 {A,Z} 对相应图有效）。 [0:33:09–0:34:18]  
- 广义调整准则（Perković et al. 2015, 2018）：适用于 DAG、CPDAG、MAG、PAG，三条条件（等价的推广），用“possible descendants”“possibly causal paths”“definite-status non-causal paths”等概念。增加了“amenability”条件（所有 proper possibly directed path 从 X 到 Y 必须以 visible edge 起始）。 [0:34:28–0:36:08]  
- 该准则已实现，可检查是否存在有效集、验证给定集是否有效、列举所有有效集。 [0:35:38–0:36:01]  
- 幻灯片总结表：各图类下充分/充要条件的进展。 [0:36:08–0:36:41]

**[0:36:46–0:44:23] 第三部分：效率考虑（O-set 与禁忌投影）**  
- 问题：在所有有效调整集中，哪一个渐近方差最小？聚焦线性模型、DAG 及 CPDAG（含背景知识）。 [0:37:07–0:37:33]  
- Henckel et al. (2019) 的贡献：  
  - 图形化两两比较准则（部分序）；  
  - 方差缩减的剪枝程序；  
  - 最优调整集 O(X,Y,G) = pa(cn(X,Y,G)) \ forb(X,Y,G)（若存在则唯一，且若不存在则无任何有效集）。 [0:37:37–0:38:38]  
- 直觉：OLS 回归中，好的 S 应解释 Y 大量方差（减小 σ²）且与 X 弱相关（减小方差膨胀因子）。父集 pa(X) 通常低效（易与 X 强相关），而 pa(Y) 通常不是有效调整集（会包含中介或后代）。 [0:38:42–0:40:20]  
- Witte et al. (2020) 的新特征：**禁忌投影（forbidden projection）**。  
  - 定义：将 DAG 中 forbidden nodes（即 forb(X,Y,D)，指所有在 proper causal path 上的节点及其后代，除去 X,Y）边缘化，得到混合图 \(D^{XY}\)（含可能双向边）。  
  - 然后 O-set = pa(Y in \(D^{XY}\)) \ (X ∪ Y)。 [0:40:20–0:42:27]  
  - 重要性质：禁忌投影保留了所有有效调整集的信息，且使“用 Y 的父集”这一直观想法变为可行。 [0:42:10–0:42:27]  
- 模拟：将 O-set 用于 IDA（最优 IDA） vs 局部 IDA（用 pa(X)）。当 CPDAG 估计准确时，最优 IDA 的 MSE 显著更低；但当 n=100 时优势减弱（因为图估计误差影响 O-set 选择）。 [0:42:31–0:44:23]

**[0:44:25–0:46:25] 总结与开放问题**  
- 三部分回顾：IDA 流程、直接在图类上调整、效率优化。强调方法可扩展且有统计保证，但不替代随机实验；可作为后续验证实验的输入。 [0:44:25–0:45:13]  
- 开放问题：  
  1. 利用不同有效调整集的估计做模型检查（若估计值差异大，提示模型误设）。  
  2. 因果结构学习中调参的选择（Eigenmann, Mukherjee & Maathuis, 2020）。  
  3. 因果效应的后选择推断（post-selection inference）——如何在图选择后给出有效标准误。 [0:45:34–0:46:10]  
- 相关软件：R 包 pcalg, dagitty。 [0:46:14–0:46:25]

**[0:46:25–1:10:02] 讨论（Daniel Malinsky）**  
Malinsky 的讨论扩展了若干未来方向（非参数/半参数扩展、隐变量、ID 算法整合等），其中提到两点直接关联报告：  
- Rotnitzky & Smucler (2019) 证明 O-set 在非参数调整估计中仍最优（使用 AIPW 类估计）。  
- Henckel & 合作者正在做条件工具变量的有效组合工作。  
讨论未在笔记主体中展开，但作为开放背景被报告提及。

### 四、对应论文与开放问题

**(a) 这场报告对应论文（验证自转写、幻灯片与摘要）**  

| 论文（按报告出现顺序） | 备注 |
|------------------------|------|
| **Witte, Henckel, Maathuis & Didelez (2020).** *On efficient adjustment in causal graphs.* arXiv:2002.06825. | 对应报告的核心新结果（O-set 的禁忌投影特征，最优 IDA）。转写中多次提到“Witte et al. '20”。 |
| **Henckel, Perković & Maathuis (2019).** *Graphical criteria for efficient total effect estimation via adjustment in causal linear models.* arXiv:1907.02435. | O-set 的定义与线性模型效率理论。 |
| **Maathuis, Kalisch & Bühlmann (2009).** *Estimating high-dimensional intervention effects from observational data.* Ann. Statist. | IDA 方法的奠基。 |
| **Perković, Textor, Kalisch & Maathuis (2018).** *Complete graphical characterization and construction of adjustment sets in Markov equivalence classes of ancestral graphs.* JMLR. | 广义调整准则（CPDAG/MAG/PAG）。 |
| **Rotnitzky & Smucler (2019).** *Efficient adjustment sets for population average treatment effect estimation in non-parametric causal graphical models.* arXiv:1912.00306. | O-set 在非参数模型中的最优性。 |
| **Frot, Nandy & Maathuis (2019).** *Robust causal structure learning with some hidden variables.* JRSS-B. | LRpS-GES。 |
| **Malinsky & Spirtes (2017).** *Estimating bounds on causal effects in high-dimensional and possibly confounded systems.* Int. J. Approx. Reason. | LV-IDA。 |

**(b) 开放问题（时间点与转写依据）**  

1. **模型检查工具**：使用不同有效调整集估计效应，若差异大则提示模型误解。 [转写 0:45:40–0:45:58]  
2. **结构学习调参**：如何选择 PC/GES 的显著性水平或惩罚参数，使得后续因果效应估计更优？Eigenmann, Mukherjee & Maathuis (2020) 有初步工作。 [转写 0:45:58–0:46:05]  
3. **后选择推断**：在估计 CPDAG 后，如何给出因果效应的有效标准误（而非忽略图选择的不确定性）？ [转写 0:46:05–0:46:10]  
4. （讨论中提及）**非参数化 IDA**：用非参数独立性检验和半参数效率估计替代线性假设，各组件存在但尚未完整实现和验证。  
5. （讨论中提及）**ADMG 等价类的直接学习和 ID 算法集成**：目前缺乏类似 CPDAG 的简洁表示 FCI 虽然输出 PAG，但将其转化为 ADMG 等价类仍繁琐且难以扩展。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

