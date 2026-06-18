# Causal effects in maximally oriented partially directed acyclic graphs (MPDAGs): Identification and efficient estimation

**讲者**: Emilija Perkovic  
**讨论人**: Thomas Richardson  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-09-29  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=jY0nH3oVu4w> · [幻灯片](https://drive.google.com/file/d/14H0o9Dy5BwvorxPuYI_TH6bYDXmvdvgQ/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2008.03481](https://arxiv.org/abs/2008.03481) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

**方向**：因果效应在部分有向图（MPDAG）中的识别与有效估计。  
**核心追问**：当因果结构只能被部分地（从一个马尔可夫等价类中）获知时——即我们只能学到CPDAG或加入背景知识后的MPDAG，而非确切的DAG——如何从观测数据中识别并高效估计总因果效应？  
**奠基与主流路线**：
- 在已知因果DAG下，G-formula（Robins, 1986）给出识别总因果效应的充要条件，但需要完整DAG。
- 在实际中，从数据无法唯一识别DAG，只能学到代表等价类的CPDAG（Spirtes et al., 1993; Chickering, 2002）。此时如何判断效应是否可识别？Perković et al.（2015, 2017, 2018）给出了基于广义调整（generalized adjustment）的充分条件，但其对识别不是必要的，且对联合干预不完整。
- 对只有一个处理和一个结果的情形，广义调整几乎完备；但对多个处理/结果，它可能找不到有效的调整集，而效应仍可通过G-formula的一种推广来识别。
- 在线性SEM假设下，为估计效应，有基于路径追迹的plug-in MLE（Hoshi & Hirano ?, 可能指的是Hayashi & Horike? 转写中提到“Hayashi and Hiraki”，但未找到确切引用，暂照转写；需核实）和基于调整的OLS（如最优调整集选择，Henckel et al., 2019? 转写中“Hankel at all”应为Henckel et al.）。这些方法在已知DAG时有效率优劣；在CPDAG/MPDAG下，调整集不一定存在，且即使存在，其估计效率低于基于G-formula推广的plug-in。

**当前前沿与这场报告的站位**：  
这篇报告（对应论文Guo & Perković, 2020, arXiv:2008.03481）有两个贡献：
1. **因果识别公式**（Perković, 2020）：将G-formula推广到MPDAG，提供**充要**的图准则（所有可能的因果路径必须以有向边从处理出发），且识别公式通过将节点按“桶”（最大无向连通分量）分组，仅对桶间结构做乘积分解。这统一了DAG、CPDAG、MPDAG三种情形。
2. **有效线性估计的G-回归**：在线性SEM且无隐藏变量假设下，将该识别公式转化为一个递归最小二乘plug-in估计量，并证明它在所有基于样本协方差的规则估计量中（含调整估计、joint-IDA的递归回归与修正Cholesky分解）是渐近最有效的。关键技巧是块递归重参数化（block recursive reparameterization），利用MPDAG的“限制性”（restrictive property）：同桶内所有节点有相同的桶外父集。这避免了估计桶内方向的不确定性，从而得到有效估计。

**与你（研究者）的连接**：该工作直接落在你的核心兴趣——因果推断（识别与有效估计）与半参数理论（效率界）。报告第二部分在非高斯误差下仍成立（仅依赖二阶矩），这与你的高效率理论兴趣高度吻合。你熟悉的工具（如M-estimation、识别理论）足以阅读该论文，而其中的线性重参数化技巧与你的半参数经验可能有交叉。

### 二、最小内核 / 一个最简例子

**符号设定**：  
- 可观测数据: \( V = (X_1, X_2, \dots, X_p) \)，每个变量是实值。  
- 因果图是一个MPDAG \( G \)，节点集为 \( V \)。边可以是定向（→）或未定（—）。G代表一个DAG等价类。  
- 我们关心总因果效应 \(\tau_{X \to Y}\)，即 \( \frac{\partial}{\partial x} \mathbb{E}[Y \mid do(X=x)] \)（线性情形下），或更一般地，\( \mathbb{E}[Y \mid do(X=x+1)] - \mathbb{E}[Y \mid do(X=x)] \)。  
- 观测分布 \( f(v) \) 已知；干预分布 \( f(v \mid do(x)) \) 由因果结构决定。  
- **无隐藏变量**假设，误差独立（或线性SEM中误差独立且均值为零）。  
- **集合定义**：\( S = an(Y, G_{V \setminus X}) \setminus Y \)，即去掉X后，Y的所有祖先（不包含Y）。  
- **“桶”**：\( S \cup Y \) 在G的诱导无向子图中的最大连通分量（maximal undirected connected components），记为 \( S_1, \dots, S_k \)。这些桶按G的部分拓扑序排列（定向边定义了桶间的偏序）。

**最简特例**：只有三个变量 \( X, Y, Z \)，MPDAG \( G \) 为 \( X \rightarrow Z \rightarrow Y \) 且 \( X \) 与 \( Z \) 之间无未定向边（即定向全知）。这是一个DAG，识别平凡。为了演示MPDAG的挑战，我们考虑稍微复杂但仍是二维的例子：  

设 \( V = \{X, Y, A\} \)，G为：\( X — A \rightarrow Y \)（即X和A之间有未定向边，A到Y有定向边）。此时：
- **条件**：从X到Y的“可能的因果路径”是 \( X — A \rightarrow Y \)，它以未定向边开始，因此条件不满足，效应不可识别。直观原因：在等价类中，真实DAG可能是 \( X \rightarrow A \rightarrow Y \)（A是中介）或 \( X \leftarrow A \rightarrow Y \)（A是混杂）。两种情形下总效应不同，无法从观测数据唯一确定。

现在考虑可识别的例子：设 \( V = \{X, Y, A, B\} \)，G为：\( X \rightarrow A — B \rightarrow Y \)（X到A定向，A和B未定向，B到Y定向）。  
- **检查条件**：所有可能因果路径是 \( X \rightarrow A — B \rightarrow Y \)，以定向边开始，满足条件，效应可识别。  
- 计算 \( S = an(Y, G_{V \setminus \{X\}}) \setminus \{Y\} \)。去掉X后，Y的祖先为 \( A, B \)（因为 \( B \rightarrow Y \)，\( A — B \) 意味着在等价类中A可能是B的祖先或后代，但在去掉X后的图中，A仍可能在某个DAG中作为B的祖先；定义中 \( an(Y, G_{V\setminus X}) \) 包含通过任何可能定向路径可达的节点）。所以 \( S = \{A, B\} \)。  
- \( S \cup \{Y\} = \{A, B, Y\} \)。在G的诱导无向子图中，这些节点都连通（A—B，B—Y），所以只有一个桶 \( S_1 = \{A, B, Y\} \)。  
- 因果识别公式给出：  
  \[
  f(y \mid do(x)) = \int f(y \mid pa(Y, G)) \, f(a,b \mid pa(\{A,B\}, G)) \, da\,db ?
  \]  
  但需注意：桶内无定向关系未知，公式要求按桶分组。实际上，对于单个桶，公式退化为：  
  \[
  f(y \mid do(x)) = \int f(y, s \mid do(x)) ds = \int f(y, a, b \mid do(x)) da db.
  \]  
  然后利用链式法则和干预操作：由于X是桶外变量且是A的父节点，桶内用联合分布。在线性情形下，这导致 \( \tau = \beta_{Y \sim A, B} \times \beta_{A \sim X} + \beta_{Y \sim B} \times \beta_{B \sim X?} \) 实际上需要具体计算。在此仅说明原理：通过桶分解，只估计桶间的系数（从X到桶的定向边系数、从桶到Y的定向边系数），避免估计桶内方向。

**核心思想**：当因果图中有未定向边时，识别需要判断所有可能因果路径是否都以定向边从处理出发；若是，则通过将图中节点按无向连通分量（桶）分组，将干预分布表示为桶间因子的乘积（类似于G-formula但因子是桶的条件分布），从而识别。在线性模型中，这转化为递归最小二乘：只回归桶外父集即可，无需估计桶内结构。

### 三、报告主体：讲者讲了什么

**[0:00:06–0:01:45]**  
开场与目标介绍。Emilija Perković（UW）介绍讲座分为两部分：第一部分是因果效应在MPDAG中的识别（基于个人工作Perković, 2020），第二部分是有效估计（与F. Richard Guo合作，对应arXiv:2008.03481）。

**[0:01:46–0:03:35]**  
回顾总因果效应的定义与do-操作。演示一个简单DAG例子：节点B是混杂，干预通过切断指向X的边实现。强调干预分布与条件分布的区别。

**[0:03:36–0:05:20]**  
因果DAG的定义：观测分布与所有干预分布都按DAG因式分解。以三变量图 \( X \rightarrow Y, B \rightarrow X, B \rightarrow Y \) 为例，展示G-formula：\( f(y \mid do(x)) = \int f(y \mid b, x) f(b) db \)。导出总效应可识别。

**[0:05:21–0:06:20]**  
正式定义总因果效应为某个函数（期望差、导数等）。当可观测数据计算出的 \( f(y \mid do(x)) \) 唯一确定时，称效应可识别。给定因果DAG，所有总效应都可识别（通过G-formula）。

**[0:06:21–0:08:55]**  
问题：真实DAG未知，只能从数据学得CPDAG（如右侧图）。展示从DAG \( X \rightarrow A \rightarrow Y \) 等可能等价类推导出的CPDAG含未定边。之后引入背景知识可得到MPDAG（附加定向边后仍保留部分未定边）。框架：从观测数据+背景知识学习因果图，然后识别并估计效应。报告聚焦第二步。

**[0:08:56–0:14:00]**  
现有识别准则总结表（见图）：  
- G-formula（Robins, 1986）：对DAG充要。  
- 广义调整（Shpitser et al., 2010; Perković et al., 2015, 2017, 2018）：在CPDAG、MPDAG中充分但不必要（尤其多重处理/结果时）。  
- 因果识别公式（Perković, 2020）：对MPDAG充要，统一概括前两者。

**[0:14:01–0:19:30]**  
**因果识别公式定理**（幻灯片第15页）：若且仅若从X到Y的所有可能因果路径都以定向边从X出发，则  
\[
f(y \mid do(x)) = \int \prod_{i=1}^k f(s_i \mid pa(s_i, G)) \, ds,
\]  
其中S = an(Y, G_{V\setminus X}) \setminus Y，(S_1,…,S_k)为S ∪ Y在G的诱导无向子图中的最大连通分量（桶）。直觉解释：若存在路径 \( X — A \rightarrow Y \)，则效应不可识别（因不知该路径是因果还是混杂）。公式需要先找到桶，再按部分拓扑序因式分解。

**[0:19:31–0:21:50]**  
例子：将前图E改为X2，考虑联合干预 \((X1, X2) \rightarrow Y\)。发现无调整集可用（因为A既是X1的后代/中介，又是X2的混杂），但G-formula仍适用（因DAG可识别）。然后展示对应的MPDAG版本（X1与A之间未定向？具体见图）。演示如何应用因果识别公式：  
- 检查条件：X1、X2邻接边均为定向，通过。  
- 计算S = an(Y, G_{V\setminus\{X1,X2\}}) \setminus \{Y\} = \{A,B,C,D\}。  
- 桶分解：在移除X1、X2后的无向子图中，{B,C,D}连通，{A}孤立，{Y}孤立，故桶为({B,C,D}, {A}, {Y})。  
- 得公式：\( f(y \mid do(x1,x2)) = \int f(y \mid pa(Y,G)) f(A \mid pa(A,G)) f(B,C,D) \, dA\,dB\,dC\,dD \)。其中 \( pa(Y,G) = \{A, X2\} \)，\( pa(A,G) = \{B, D, X1? 或 B? \}\) 因A桶内无其他点，其父集仅为桶外父集（B、D、X1？需核对）。随后证明sktech：先写联合干预密度，链式分解，利用桶内条件独立去掉非父节点，最后将do(x)转为观测。

**[0:21:51–0:23:55]**  
证明sktech：从干预密度出发，按部分拓扑序（桶序）逐项写链式法则；利用桶内节点有相同外部父集的性质，简化；最后仅保留观测分布中的条件项。

**[0:23:56–0:28:00]**  
转入第二部分：线性SEM下的有效估计。假设线性、无隐藏变量、误差独立。重新定义符号（X为随机向量，节点用下标）。介绍线性结构方程模型：\( X_j = \sum_{i \in pa(j)} \gamma_{ij} X_i + \epsilon_j \)。总效应可表示为路径边缘权重的和（权重乘积沿因果路径）。自然估计方法：回归每个节点于其父集得到 \(\hat\gamma\)，然后plug-in（路径追踪估计量）。另一方法是调整：通过回归Y于处理X和选定的调整集Z得到系数。

**[0:28:01–0:30:30]**  
现有文献：对DAG，路径追踪MLE比任何调整集更有效（Hayashi & Hiraki?）；对CPDAG/MPDAG，Henckel et al. 给出了最优调整集选择方法（最优，但仍是调整估计量）。问题：我们的推广的因果识别公式对应的plug-in估计量（G-回归）是否比最优调整更有效？答案：是的。

**[0:30:31–0:34:20]**  
问答环节（Dominique提问）：计算复杂度？讲者答：只需一次桶分解（DFS）和一次祖先集计算，复杂度低。另问：线性假设是否改变调整集？答：因果识别公式本身就是非参数结果，但在线性模型下证明同样充要，不增加新调整集。

**[0:34:21–0:41:00]**  
回到MPDAG下的线性SEM例子。展示MPDAG与原DAG的gamma矩阵不可识别（因桶内方向未知）。利用因果识别公式的桶分解，发现桶间方向可识别，且每个桶内所有节点共享相同的桶外父集（限制性性质）。由此得到块递归重参数化：每一桶视为一个“块”，其依赖于桶外父集和一个桶内误差向量（可能相关）。从而新参数矩阵λ是块上三角的，且只涉及桶间系数。此λ可通过最小二乘一一估计（回归每个桶的所有变量于其桶外父集，给出系数矩阵的MLE——高斯假设下等价于OLS）。从而G-回归估计量将因果识别公式中的参数替换为这些OLS系数。

**[0:41:01–0:46:30]**  
**主要理论结果**（幻灯片第37页附近）：对于任何基于样本协方差的规则估计量（包括协变量调整、joint-IDA的递归回归与修正Cholesky分解），G-回归估计量的渐近方差小于等于该估计量。证明不假设高斯误差（仅依赖二阶矩）。解释：G-回归利用了完整图结构，而调整等方法只能利用部分信息。

**[0:46:31–0:50:00]**  
模拟结果：在DAG设定下，G-回归 vs 最优调整、joint-IDA两种方法。显示在单处理时收益不大，多处理时收益明显；在CPDAG设定下（图结构不能完全确定），收益变小但仍为正。讨论：调整与G-回归在单处理时几乎等价，因为广义调整在单处理时已接近完备。但在联合干预时调整可能不可用，而G-回归始终可用（只要可识别）。

**[0:50:01–0:53:30]**  
总结与R包（GitHub）。提及非参数效率工作（如Ernest & Smucler?）可能扩展方向。

**[0:53:31–结束]**  
讨论者Thomas Richardson评论：  
- 连接IDA与joint-IDA工作：IDA在CPDAG下通过所有可能父集做调整；joint-IDA给出两种基于父集的方法（递归回归和修正Cholesky）。当前G-回归提供一个统一且有效的方法。  
- “限制性”不是额外假设，而是CPDAG/MPDAG的固有性质：同一桶内节点有相同的桶外父集。这保证了重参数化的块结构。  
- G-回归无需估计桶内参数，因此若桶内结构不同但桶间结构相同，估计量不变（例如去掉某些定向边）。  
- 进一步问题：若只加入最少的背景知识（如只定向处理节点出发的边），是否足以识别？讲者回应：他们正在做相关工作，最小背景知识可能保证识别且G-回归结果相同（因Cochran公式，数值上相同，但大样本下可能因有限样本不同）。  
- 线性假设很关键，非参数推广需谨慎。

### 四、对应论文与开放问题

**对应论文**：  
- 第一部分识别理论：Perković (2020). "Causal effects in maximally oriented partially directed acyclic graphs: Identification." 未提供arXiv号，但在转写中被称为自己的独立工作。  
- 第二部分有效估计：Guo & Perković (2020). "Efficient least squares for estimating total effects under linearity and causal sufficiency." arXiv:2008.03481. （对应摘要已提供）  
- R包：可能为 `causalEffect` 或 ` gRegression`，GitHub链接需从讲者处查找（未在转写中明确给出）。

**开放问题**（每条扎根于转写）：  

1. **非参数/半参数效率**：线性模型下的效率结论能否推广至非/半参数？讲者提到“Ernest Can Smucler”的工作可能相关（[0:47:40–0:47:50]：“there is work on adjustment and on efficiency beyond the linear sem setting, that by Ernest Can Smucler and that is perhaps also worth considering applying to our own estimator”）。因此探索在非参数模型下，基于因果识别公式的半参数有效估计是一个自然延伸。

2. **最小背景知识**：Thomas提出一个开放的实用问题（[0:55:30–0:56:30]）：在MPDAG中，哪些额外定向边是识别/估计所必需的？是否只需要定向从处理节点出发的可能因果路径上的边？讲者确认正在做相关项目（[1:00:10–1:00:30]）。这引出的问题是：对于给定的处理-结果对，确定最小定向边集使得效应可识别，并探讨G-回归的估计是否保持不变（理论相等但有限样本可能差异）。

3. **隐藏变量**：Thomas指出当前假设无隐藏变量是强的（[0:59:00–0:59:15]：“assuming that there's a dag with no hidden variables is maybe appropriate in some settings but that seems to be quite a strong assumption”）。扩展至存在未观测混杂的情形，即从CPDAG/MAG（最大祖先图）出发，如何识别和有效估计总效应。

4. **桶内误差相关性**：Thomas提到在线性假设下允许桶内误差相关（[0:54:55–0:55:05]：“we could allow the errors to be correlated within buckets, so all of those would all give the same estimate”）。这引出对广义线性模型或非线性可加模型下桶分解的适用性。

5. **有限样本与数值稳定性**：模拟显示，在CPDAG下G-回归相对于最优调整的改进不如DAG下明显（[0:46:30–0:47:20]）。是否存在极端图结构使G-回归的方差反而更大？也需探究G-回归在估计桶内参数时的数值稳定性（特别是桶内变量数多时）。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

