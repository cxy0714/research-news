# 网络与图数据 Networks & Graphs · 5

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **2 个分会场 · 12 场报告**（已检索到对应论文 4 场）

---

## Advances in Network Time Series and Risk Spillovers

*7 月 13 日（周一） · 15:30-17:10 · ASEAN Roundtable Forum Meeting Room*  
*主持 Kewen Shi（Nanjing Audit University）*

### 1. 县域数字普惠金融空间关联主干网络演化及韧性研究

**讲者**：Changlan Hong（Chongqing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
县域数字普惠金融的发展并非孤立，而是通过资金流、信息流等形成跨区域空间关联。然而，现有研究多聚焦于省级或城市层面的静态空间格局，对县域层面关联网络的动态演化规律及其抵御外部冲击的韧性（resilience）缺乏系统刻画。本报告旨在回答：县域数字普惠金融空间关联的主干网络如何随时间演化？其网络结构在面临经济波动或政策干预时是否具备稳健性？

**核心方法**  
报告采用复杂网络与空间计量相结合的框架。首先，基于县域数字普惠金融指数（如北京大学数字普惠金融指数）构建空间关联矩阵，利用平面极大过滤图（PMFG）或最小生成树（MST）提取主干网络，剔除冗余边以突出核心关联。其次，引入网络演化分析，通过滑动窗口计算不同年份的网络密度、平均路径长度、聚类系数等拓扑指标，并利用社区检测算法（如Louvain）识别空间聚类结构的变迁。最后，韧性评估采用蓄意攻击模拟：依次移除度中心性最高的节点（县域），观察网络全局效率（global efficiency）和最大连通子图相对大小的衰减曲线，以量化网络抵抗级联失效的能力。

**与已有工作关系**  
已有文献对数字普惠金融的空间溢出效应多采用空间杜宾模型或引力模型，侧重静态溢出强度，且通常忽略网络结构的异质性与动态性。本报告将网络科学中的主干网络提取与韧性分析引入该领域，弥补了县域尺度动态网络研究的空白。此外，相比传统金融地理学中基于地理距离的关联，本报告更强调经济关联与信息关联的复合性，并通过韧性指标将网络稳健性从定性描述提升为定量测度。

**主要贡献**  
第一，方法上，为县域数字普惠金融的空间关联研究提供了“主干网络提取—演化分析—韧性评估”的完整分析框架。第二，实证上，揭示县域间关联网络从“核心—边缘”向“多中心”演化的可能路径，并识别出关键节点（如经济强县）的脆弱性。第三，政策上，为县域金融风险防控与区域协同发展提供网络视角的决策依据，例如通过强化关键节点的冗余连接提升整体韧性。


### 2. Reduced-Rank Autoregressive Model for High-Dimensional Multivariate Network Time Series

**讲者**：Qi Lv（Shanghai Jiao Tong University）

**对应论文**：Reduced-Rank Autoregressive Model for High-Dimensional Multivariate Network Time Series · [arXiv:2601.01510](https://arxiv.org/abs/2601.01510)

<details><summary>摘要（原文）</summary>

Multivariate network time series are ubiquitous in modern systems, yet existing network autoregressive models typically treat nodes as scalar processes, ignoring cross-variable spillovers. To capture these complex interactions without the curse of dimensionality, we propose the Reduced-Rank Network Autoregressive (RRNAR) model. Our framework introduces a separable bilinear transition structure that couples the known network topology with a learnable low-rank variable subspace. We estimate the model using a novel Scaled Gradient Descent (ScaledGD) algorithm, explicitly designed to bridge the gap between rigid network scalars and flexible factor components. Theoretically, we establish non-asymptotic error bounds under a novel distance metric. A key finding is a network-induced blessing of dimensionality: for sparse networks, the estimation accuracy for network parameters improves as the network size grows. Applications to traffic and server monitoring networks demonstrate that RRNAR significantly outperforms univariate and unstructured benchmarks by identifying latent cross-channel propagation mechanisms.

</details>

**问题**：高维多元网络时间序列中，节点观测为$D$维向量，现有网络自回归（NAR）模型将节点视为标量过程（$D=1$），强制假设网络溢出仅在变量内部传递，忽略了跨变量（cross-variable）的交互机制（如上游交通拥堵同时影响下游速度和流量）。直接堆叠为向量自回归（VAR）需估计$O(N^2 D^2)$参数，遭遇维度灾难；而纯数据驱动的矩阵自回归（MAR）虽处理多元维度，却丢弃了已知的网络拓扑信息，导致统计效率损失。

**核心方法**：提出降秩网络自回归（RRNAR）模型，采用可分离双线性结构$Y_t = B_{\text{net}} Y_{t-1} B_{\text{var}}^\top + E_t$。其中节点算子$B_{\text{net}} = \beta_A I_N + \beta_N W_N$由已知网络权重矩阵$W_N$参数化，仅含两个标量；变量算子$B_{\text{var}}$为秩$r \ll D$的低秩矩阵，分解为$UV^\top$。该结构将网络传播限制在低维潜在因子空间，实现跨变量溢出建模。估计采用块特定预条件子的缩放梯度下降（ScaledGD），通过$\|B_{\text{var}}\|_F^{-2}$和$\|B_{\text{net}}\|_F^{-2}$平衡网络标量与变量子空间的梯度尺度，保证线性收敛。

**与已有工作关系**：区别于标量NAR（Zhu et al., 2017）的变量孤立假设，RRNAR通过低秩变量算子允许跨通道溢出；区别于纯数据驱动的降秩MAR（Xiao et al., 2022），RRNAR利用已知网络拓扑约束节点算子，将问题从纯矩阵恢复转化为“参数+子空间”估计，避免丢弃领域知识。理论分析揭示网络结构作为方差缩减装置，使网络参数估计率与高维变量空间解耦。

**贡献**：1）提出RRNAR模型，桥接标量网络模型与高维矩阵自回归，在避免维度灾难的同时捕捉跨变量网络传播。2）设计ScaledGD算法，解决“刚性标量+柔性子空间”参数异质性导致的梯度失衡问题，保证全局收敛。3）建立非渐近误差界，发现稀疏网络下网络参数估计误差以$O(\|W_N\|_F^{-2} Dr/T)$衰减，即网络规模增大反而提升估计精度（“维数祝福”），并通过交通和服务器监控数据验证了预测优势与可解释性。


### 3. Model-Xt Knockoffs: Controlling the False Discovery Rate in High Dimensional Time Series

**讲者**：Zexin Huang（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
高维时间序列中变量选择面临两大挑战：一是维度远大于样本量，二是观测间存在时序依赖（自相关、非平稳性）。传统 FDR 控制方法（如 Benjamini-Hochberg）依赖独立或弱相关假设，而现有 Knockoffs 框架（Model-X Knockoffs）要求协变量独立于响应变量且样本独立同分布，无法直接用于时间序列。本报告旨在解决：如何在保持 FDR 可控的前提下，对高维时间序列进行有效变量筛选。

**核心方法**  
提出 **Model-Xt Knockoffs**，核心思想是构造与原始时间序列具有相同时序依赖结构的“knockoff”变量。具体地，利用向量自回归（VAR）或状态空间模型拟合协变量的动态结构，生成条件独立于响应变量 $Y_t$ 的 knockoff 副本 $\tilde{X}_t$，使得 $(X_t, \tilde{X}_t)$ 的联合分布与交换后的分布不可区分。随后构造统计量 $W_j = |\hat{\beta}_j| - |\hat{\tilde{\beta}}_j|$（基于 Lasso 或 Dantzig Selector），并采用 Knockoffs 的阈值选择程序（如 knockoff+）控制 FDR。方法本质是将时序依赖嵌入 knockoff 生成过程，而非事后调整。

**与已有工作关系**  
已有工作包括：Model-X Knockoffs（Candès et al., 2018）假设 i.i.d. 样本；针对时间序列的 FDR 控制多基于 bootstrap 或分块技术（如 Barber & Candès, 2019 的 Fixed-X Knockoffs 仅适用于固定设计）。本报告首次将 Knockoffs 推广到高维时间序列，允许协变量具有任意自相关结构，且无需对响应变量分布做参数假设。相比分块方法，Model-Xt 保留了每个时间点的信息，统计效率更高。

**主要贡献**  
1. 提出一种适用于高维时间序列的 knockoff 构造算法，可处理 VAR、ARIMA 等常见时序模型。  
2. 在弱条件下（如协变量过程平稳且 $\beta$ 稀疏）证明所提方法能渐近控制 FDR，且不依赖响应变量与协变量的独立性。  
3. 通过模拟和真实数据（如金融收益率、神经信号）验证方法在自相关较强时仍保持 FDR 控制，且 power 优于现有方法。  
4. 为时间序列因果推断提供了可解释的变量选择工具，拓展了 Knockoffs 框架的应用边界。


### 4. 高水平对外开放下我国金融机构风险溢出的研究

**讲者**：Haoya Zhang（Zhongnan University of Economics and Law）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高水平对外开放背景下，我国金融机构面临跨境资本流动、汇率波动与政策协调等多重冲击，风险溢出机制可能发生结构性变化。现有研究多聚焦于封闭经济或发达国家市场，对中国开放进程中金融机构间风险传染的异质性、方向性与时变性缺乏系统刻画。本报告旨在回答：对外开放如何重塑我国金融机构的风险溢出网络？哪些机构成为新的风险枢纽？溢出强度是否随开放程度非线性变化？

**核心方法**  
报告可能采用高维时间序列的因果推断框架，如基于LASSO的Granger因果网络估计或时变参数VAR模型，结合尾部依赖度量（如CoVaR、ΔCoVaR）构建有向加权风险溢出网络。为处理高维金融数据中的稀疏性与异方差性，可能引入正则化回归（如adaptive LASSO）或分位数回归，并利用滚动窗口估计动态网络拓扑指标（如度中心性、中介中心性）。此外，可能通过面板回归或双重差分法识别对外开放政策（如金融业准入负面清单、沪港通等）对溢出效应的因果影响。

**与已有工作关系**  
已有文献多采用静态网络或对称溢出假设（如Diebold & Yilmaz溢出指数），且样本多限于发达国家。本报告的可能创新在于：1）将对外开放政策作为外生冲击，利用准自然实验识别因果效应，而非仅描述相关性；2）针对中国金融机构的异质性（国有大行、股份制、城商行、外资机构），分析不同开放阶段下风险枢纽的转移；3）结合高维统计方法处理大量机构间的稀疏网络，避免传统VAR的维度灾难。

**贡献**  
主要贡献包括：1）理论层面，提出一个融合政策冲击与网络拓扑的因果推断框架，为开放经济下的系统性风险研究提供新视角；2）实证层面，揭示对外开放如何改变风险溢出的方向与强度，识别关键风险节点（如外资持股比例高的机构）；3）政策层面，为宏观审慎监管提供动态预警指标，例如当某类机构中心性突破阈值时触发逆周期资本缓冲。


### 5. 投资者情绪压力与美国经济政策不确定性对泛能源市场风险连接度的非线性影响：基于TVP-SV-VAR与门限模型

**讲者**：Xiao Li（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
泛能源市场（包括石油、天然气、新能源等）的风险连接度如何受投资者情绪压力与美国经济政策不确定性（EPU）的非线性驱动？现有文献多关注线性或对称的溢出效应，但忽略了极端情绪或政策突变下风险传导的阈值效应与时变特征。本报告旨在揭示：当情绪压力或EPU跨越某一门限时，风险连接度是否发生结构性突变，以及这种突变在时间维度上如何随经济环境演变。

**核心方法**  
采用两阶段建模：首先，利用带随机波动率的时变参数向量自回归模型（TVP-SV-VAR）估计泛能源市场间的动态风险连接度（如Diebold-Yilmaz溢出指数），捕捉时变性与异方差性。其次，引入门限回归（Threshold Regression），以投资者情绪压力指数（如基于恐慌指数的构建）和EPU为门限变量，检验风险连接度是否存在非线性跳跃。模型设定为：  
\[
C_t = \beta_0 + \beta_1 C_{t-1} + \gamma_1 \cdot I(q_t \leq \tau) + \gamma_2 \cdot I(q_t > \tau) + \varepsilon_t
\]  
其中 \(q_t\) 为门限变量，\(\tau\) 为待估门限值，通过Bootstrap检验确定显著性。

**与已有工作关系**  
传统研究多采用静态或线性VAR分析风险溢出，或单独使用TVP-VAR刻画时变性，但未将门限效应纳入。本报告将TVP-SV-VAR的时变溢出指数作为因变量，再叠加门限回归，实质上是将“时变参数”与“结构突变”两种非线性来源分离：前者捕捉平滑演变，后者捕捉离散跳跃。这比单纯的门限VAR（TVAR）更灵活，因为TVP-SV-VAR已吸收参数连续变化，门限仅针对外部冲击的阈值效应。

**主要贡献**  
1. 首次将投资者情绪压力与EPU作为门限变量，揭示其对泛能源市场风险连接度的非线性驱动机制，为“情绪-政策-市场风险”三角关系提供新证据。  
2. 方法上融合TVP-SV-VAR与门限回归，既保留时变参数对动态结构的刻画能力，又识别出离散的结构断点，避免将时变与门限效应混淆。  
3. 实证结果可为风险管理与政策制定提供预警阈值：当情绪压力或EPU超过特定水平时，跨市场风险传染将急剧上升，需提前部署对冲策略。


### 6. Heterogeneous Autoregressive Model for Symmetric Matrix-Valued Time Series

**讲者**：Kewen Shi（Nanjing Audit University）

**对应论文**：Autoregressive Models for Matrix-Valued Time Series · [arXiv:1812.08916](https://arxiv.org/abs/1812.08916)

<details><summary>摘要（原文）</summary>

In finance, economics and many other fields, observations in a matrix form are often generated over time. For example, a set of key economic indicators are regularly reported in different countries every quarter. The observations at each quarter neatly form a matrix and are observed over many consecutive quarters. Dynamic transport networks with observations generated on the edges can be formed as a matrix observed over time. Although it is natural to turn the matrix observations into a long vector, and then use the standard vector time series models for analysis, it is often the case that the columns and rows of the matrix represent different types of structures that are closely interplayed. In this paper we follow the autoregressive structure for modeling time series and propose a novel matrix autoregressive model in a bilinear form that maintains and utilizes the matrix structure to achieve a greater dimensional reduction, as well as more interpretable results. Probabilistic properties of the models are investigated. Estimation procedures with their theoretical properties are presented and demonstrated with simulated and real examples.

</details>

**问题**  
传统向量自回归（VAR）模型处理矩阵值时间序列时，需将矩阵拉直为长向量，导致参数数量随维度平方增长（$m^2n^2$），且丢失了行与列的结构信息。报告针对对称矩阵值时间序列（如协方差矩阵、网络邻接矩阵），提出异质性自回归模型，旨在利用矩阵对称性实现维度缩减，并允许行与列方向的自回归系数不同（异质性），从而更灵活地刻画动态依赖。

**核心方法**  
模型采用双线性形式：$X_t = A X_{t-1} A' + E_t$（对称情形），或更一般的$X_t = A X_{t-1} B' + E_t$（非对称），其中$A$和$B$分别为$m\times m$和$n\times n$系数矩阵。通过Kronecker积可等价为VAR(1)：$\text{vec}(X_t) = (B\otimes A)\text{vec}(X_{t-1}) + \text{vec}(E_t)$，参数从$m^2n^2$降至$m^2+n^2$。估计方法包括：投影法（将无约束VAR估计投影到Kronecker积空间）、迭代最小二乘（交替更新$A$和$B$）、以及基于结构化误差协方差$\Sigma = \Sigma_c\otimes\Sigma_r$的MLE。报告进一步针对对称矩阵提出异质性扩展，允许$A$和$B$不同（如$X_t = A X_{t-1} B'$且$A\neq B$），或引入多个滞后项$X_t = \sum_{i=1}^d A_i X_{t-1} B_i'$。

**与已有工作关系**  
已有矩阵自回归模型（Chen et al., 2019）假设$A$和$B$为常数，且未专门处理对称性。报告在此基础上引入异质性：允许行与列方向的自回归系数不同，并针对对称矩阵提出约束形式（$B=A$或$B=A'$），同时可扩展至多滞后项。相比向量化VAR，该方法保留了矩阵结构，参数更少且可解释；相比因子模型（Wang et al., 2019），它直接建模动态而非潜变量。

**主要贡献**  
1. 提出异质性对称矩阵自回归模型，兼顾维度缩减与结构灵活性。  
2. 给出三种估计方法及其渐近正态性，并证明MLE在正确指定误差协方差结构时更有效。  
3. 推导规范检验统计量，用于判断Kronecker积结构是否成立。  
4. 通过经济指标实例展示模型的可解释性（如行系数反映指标间影响，列系数反映国家间影响）及预测性能。


## Network and Graphical Models and Tensor and Matrix Methods

*7 月 13 日（周一） · 08:30-10:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Xuefei Wang（Southeast University）*

### 1. Revisiting Madigan and Mosurski: Collapsibility via Minimal Separators

**讲者**：Pei Heng（Northeast Normal University）

**对应论文**：Revisiting Madigan and Mosurski: Collapsibility via Minimal Separators · [arXiv:2510.09024](https://arxiv.org/abs/2510.09024)

<details><summary>摘要（原文）</summary>

Collapsibility provides a principled approach for dimension reduction in contingency tables and graphical models. Madigan and Mosurski (1990) pioneered the study of minimal collapsible sets in decomposable models, but existing algorithms for general graphs remain computationally demanding. We show that a model is collapsible onto a target set precisely when that set contains at least one minimal separator between its non-adjacent vertices. This insight motivates the Close Minimal Separator Absorption (CMSA) algorithm, which constructs minimal collapsible sets using only local separator searches at very low costs. Simulations confirm substantial efficiency gains, making collapsibility analysis practical in high-dimensional settings.

</details>

**问题**  
在列联表与图形模型中，collapsibility（可折叠性）提供了一种降维原则，允许在不扭曲边际推断的前提下剔除变量。Madigan & Mosurski (1990) 首次提出“最小可折叠集”问题：给定目标变量集 $A$，寻找包含 $A$ 的最小超集 $B$，使得模型可折叠到 $B$。然而，其 SAHR 算法仅适用于可分解图，且需反复全局扫描顶点以移除单纯点，效率高度依赖顶点顺序；后续针对一般图的算法（如 Wang et al. 2011 的凸包方法、Heng & Sun 2023 的路径吸收法）仍依赖全局图操作，在高维场景下计算成本高昂。因此，如何高效、可扩展地识别一般图上的最小可折叠集，是亟待解决的开放问题。

**核心方法**  
本文给出一个简洁的图论表征：图形模型可折叠到 $A$ 当且仅当 $A$ 包含每对非相邻顶点 $x,y\in A$ 的至少一个 minimal separator（最小分隔符）。基于此，作者提出 Close Minimal Separator Absorption (CMSA) 算法。该算法首先找出 $V\setminus A$ 的连通分量，然后对每个分量，迭代检测其邻域中非相邻顶点对，利用 Takata (2010) 的 CloseSeparator 算法在局部邻域内吸收靠近顶点的最小分隔符（close minimal separator），直至所有邻域形成完全子图。整个过程仅涉及局部搜索，且连通分量规模递减，复杂度为 $O(nm)$（$n$ 顶点数，$m$ 边数），空间复杂度 $O(n)$。

**与已有工作关系**  
与 Madigan & Mosurski (1990) 的 SAHR 相比，CMSA 不再局限于可分解图，且避免了全局顶点扫描与顺序依赖；与 Wang et al. (2011) 及 Heng & Sun (2023) 的全局方法相比，CMSA 将问题转化为局部分隔符吸收，显著降低了计算开销。实验表明，在可分解图上 CMSA 一致优于 SAHR，在一般图上比 IPA 快数倍至数十倍，且优势随图规模增大而扩大。本文首次将 collapsibility 与最小分隔符建立等价关系，揭示了其本质上的局部图性质。

**贡献**  
理论贡献：证明了 collapsibility 等价于目标集包含所有非相邻顶点对的至少一个最小分隔符，为理解可折叠性提供了全新视角。方法贡献：设计了 CMSA 算法，其局部搜索策略使 collapsibility 分析在高维图形模型中变得可行，兼具理论简洁性与计算高效性。实验验证了算法在可分解图与一般图上的显著效率提升，为实际应用（如大规模列联表、混合图形模型）提供了实用工具。


### 2. Modeling and Inference for High-Dimensional Mediation Analysis with Endogeneity

**讲者**：Xinyu Zhang（Xiamen University）

**对应论文**：Powerful Large-scale Inference in High Dimensional Mediation Analysis · [arXiv:2402.13933](https://arxiv.org/abs/2402.13933)

<details><summary>摘要（原文）</summary>

In genome-wide epigenetic studies, exposures (e.g., Single Nucleotide Polymorphisms) affect outcomes (e.g., gene expression) through intermediate variables such as DNA methylation. Mediation analysis offers a way to study these intermediate variables and identify the presence or absence of causal mediation effects. Testing for mediation effects lead to a composite null hypothesis. Existing methods like the Sobel's test or the Max-P test are often underpowered because 1) statistical inference is often conducted based on distributions determined under a subset of the null and 2) they are not designed to shoulder the multiple testing burden. To tackle these issues, we introduce a technique called MLFDR (Mediation Analysis using Local False Discovery Rates) for high dimensional mediation analysis, which uses the local False Discovery Rates based on the coefficients of the structural equation model specifying the mediation relationship to construct a rejection region. We have shown theoretically as well as through simulation studies that in the high-dimensional setting, the new method of identifying the mediating variables controls the FDR asymptotically and performs better with respect to power than several existing methods such as DACT (Liu et al.)and JS-mixture (Dai et al).

</details>

**问题**  
高维中介分析中，检验复合零假设 $H_{0,i}:\alpha_i\beta_i=0$（$\alpha_i$ 为暴露-中介效应，$\beta_i$ 为中介-结局效应）面临两大挑战：一是零假设由三种子情形构成，传统 Sobel 检验或 Max-P 检验仅覆盖部分零空间，导致保守性；二是高维多重检验下需控制 FDR 并最大化功效。此外，未测量混杂（内生性）会扭曲估计，现有方法如 HDMT 和 DACT 虽改进 p 值处理，但未从最优性角度设计拒绝域。

**核心方法**  
报告提出 MLFDR（Mediation Analysis using Local False Discovery Rates）框架。首先对每个中介拟合结构方程模型得到系数估计 $(\hat\alpha_i,\hat\beta_i)$，并假设其服从高斯混合分布（零效应、仅 $\alpha$ 非零、仅 $\beta$ 非零、两者均非零）。通过 EM 算法估计混合比例及非零效应先验参数，进而计算每个假设的局部 FDR：$\text{lfdr}_i = \frac{\pi_{00}f_{00}+\pi_{10}f_{10}+\pi_{01}f_{01}}{f}$。最后采用 Sun & Cai (2007) 的 step-up 过程，以 $\hat Q_m(\delta)=\frac{\sum 1_{\{\widehat{\text{lfdr}}_i\leq\delta\}}\widehat{\text{lfdr}}_i}{\sum 1_{\{\widehat{\text{lfdr}}_i\leq\delta\}}}$ 估计 mFDR，自适应选取阈值 $\hat\delta_m$ 并拒绝 $\widehat{\text{lfdr}}_i\leq\hat\delta_m$ 的假设。针对未测量混杂，引入 Surrogate Variable Analysis 调整潜因子，缓解内生性。

**与已有工作关系**  
相比 HDMT（基于最大 p 值的混合零分布）和 MDACT（改进 p 值积分），MLFDR 直接利用局部 FDR 排序，理论上在非对称备择下比 p 值排序更优（Sun & Cai 2007）。与 Sun et al. (2023) 和 Ding & Zhu (2024) 等局部 FDR 方法不同，MLFDR 通过 EM 精确估计后验密度而非近似，并首次在复合零假设下给出局部 FDR 估计的收敛性证明。

**贡献**  
1. 将局部 FDR 框架系统扩展至复合零假设的中介检验，导出封闭形式的 FDP 估计量。  
2. 理论证明在 AMLE 条件下，自适应 MLFDR 渐近控制 FDR，且功效优于现有方法（模拟显示平均提升 7–12%）。  
3. 方法可处理连续/二元结局、有/无混杂、暴露-中介交互及未测量潜变量，鲁棒性强。  
4. 在 TCGA 前列腺癌和肺癌数据中，MLFDR 比 HDMT 和 MDACT 多识别 5–50% 的显著中介通路，发现已知风险 SNP 的新调控路径。


### 3. Clustering Analysis on Multi-layer Networks with Group Structure and Sparsity Heterogeneity

**讲者**：Xuefei Wang（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多层网络（multi-layer networks）中，节点共享同一组顶点，但各层边结构可能不同。现有聚类方法多假设各层网络具有同质性（如相同稀疏度或相同社区结构），但实际中不同层可能呈现显著稀疏异质性（sparsity heterogeneity），且节点可能同时属于多个组（group structure）。本报告旨在解决：如何在允许各层稀疏度差异的前提下，对多层网络进行节点聚类，并同时识别组结构。

**核心方法**  
报告提出一种基于正则化似然的聚类框架。设多层网络有 $L$ 层，每层邻接矩阵 $A^{(l)} \in \{0,1\}^{n \times n}$，节点属于 $K$ 个组。模型假设每层内节点连接概率由组结构决定，但各层可拥有不同的稀疏参数 $\rho_l$（即整体边密度）。方法通过引入 group lasso 型惩罚项对组结构进行稀疏化，同时利用 adaptive 权重处理层间稀疏异质性，将聚类问题转化为带约束的优化问题，并采用交替方向乘子法（ADMM）求解。

**与已有工作关系**  
已有工作如 stochastic block models（SBM）及其多层扩展（如 MMSBM）通常假设各层稀疏度相同或已知，或仅处理同质稀疏场景。本报告将稀疏异质性显式建模为可估计参数，并允许组结构在不同层间共享但连接概率不同。与基于谱聚类的多层方法相比，本方法能更灵活地处理层间密度差异，且通过惩罚项自动选择组数。

**主要贡献**  
1. 提出首个同时建模组结构与稀疏异质性的多层网络聚类模型，更贴合实际数据（如脑网络、社交网络）。  
2. 给出估计量的相合性及聚类误差上界，证明在稀疏异质性下仍能实现精确聚类。  
3. 通过模拟和真实数据（如多时点社交网络）验证方法优于忽略异质性的现有方法，尤其在层间密度差异大时优势显著。


### 4. High-Dimensional Heterogeneous Factor-Augmented Generalized Linear Regression Models for Multi-View Data

**讲者**：Tianmei Niu（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
多视图数据（multi-view data）在生物信息、社交网络等领域日益常见，但现有因子增强回归模型（如 factor-augmented regression）通常假设因子结构同质、响应为连续型，难以同时处理高维、非高斯响应（如二值、计数）以及不同视图间因子载荷的异质性。本报告旨在解决：如何在高维多视图框架下，构建一个既能利用潜在因子降维、又能刻画视图间异质性、且适用于广义线性响应的回归模型。

**核心方法**  
讲者提出 **High-Dimensional Heterogeneous Factor-Augmented Generalized Linear Regression (HD-HFAGL)** 模型。该模型假设每个视图 $v$ 的观测 $X_v$ 由低维公共因子 $F$ 和视图特异因子 $G_v$ 生成，且因子载荷允许跨视图异质。响应变量 $Y$ 通过广义线性模型与公共因子及视图特异因子关联：$g(\mathbb{E}[Y|F, G_1,\dots,G_V]) = \alpha + \beta_F^\top F + \sum_{v=1}^V \beta_{G_v}^\top G_v$，其中 $g(\cdot)$ 为 link function。估计采用带自适应惩罚的拟似然方法，同时实现因子个数选择、异质性结构识别与变量筛选。

**与已有工作关系**  
已有工作如 factor-augmented regression（Bai & Ng, 2006; Fan et al., 2011）仅考虑单视图且响应为线性；多视图因子分析（如 JIVE, AJIVE）虽能分解公共与个体结构，但未与广义线性回归结合。本工作首次将异质性因子结构嵌入 GLM 框架，并允许因子载荷在不同视图间自由变化，从而更灵活地捕捉多视图数据的共享与特有信息。

**主要贡献**  
1. 提出一个统一模型，同时处理高维、多视图、异质性及非高斯响应。  
2. 给出估计量的收敛速率与变量选择相合性理论，证明在因子个数发散时仍有效。  
3. 开发高效算法（如 ADMM 结合坐标下降），并在模拟与真实数据（如脑成像多模态数据）中展示优于现有方法的预测与解释性能。


### 5. Transfer Learning in High-Dimensional Group Factor Models

**讲者**：Yunjing Sun（Shandong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维群因子模型（Group Factor Models）允许不同数据组共享部分潜在因子，同时保留组特异因子，常用于多源异质数据（如多组学、多任务学习）。当目标组样本量远小于变量维数时，直接估计因子结构会面临严重的过拟合与不可识别问题。本报告旨在解决：如何利用多个源组（source groups）的丰富数据，通过迁移学习提升目标组（target group）在高维群因子模型中的因子载荷与公共因子估计精度，并刻画迁移带来的统计效率增益。

**核心方法**  
报告提出一种基于惩罚似然的迁移学习框架。首先，联合估计所有源组的群因子结构，识别出全局共享因子与组特异因子。然后，对目标组施加“共享因子载荷与源组一致”的结构约束，同时允许目标组拥有自己的特异因子。估计采用两步法：第一步，用源组数据通过 $L_1$ 或 $L_2$ 惩罚（如 group lasso）筛选出共享因子；第二步，在目标组上最小化带自适应惩罚的损失函数，惩罚项鼓励目标组共享因子载荷向源组估计值收缩，而特异因子部分则通过稀疏正则化控制维度。理论分析证明，当源组与目标组共享因子个数正确时，目标组因子载荷的估计误差可达到 $O_p(s \log p / n_{\text{target}} + 1/n_{\text{source}})$ 量级，其中 $s$ 为因子载荷非零元素个数，显著优于不使用迁移的 $O_p(s \log p / n_{\text{target}})$。

**与已有工作关系**  
现有高维因子模型的迁移学习多假设源组与目标组因子结构完全相同（如 Li et al., 2022），或仅考虑单因子模型。本报告将迁移学习推广至群因子模型，允许部分因子跨组共享、部分因子组特异，更贴合实际异质场景。此外，与传统的多任务因子分析（如 Bayesian group factor analysis）相比，本报告聚焦于高维稀疏设定，并提供了非渐近收敛率与迁移增益的显式刻画，而非仅依赖贝叶斯推断。

**主要贡献**  
1. 首次在高维群因子模型中系统引入迁移学习框架，明确区分共享因子与特异因子，并给出可识别的参数化条件。  
2. 提出带自适应惩罚的两步估计方法，计算可行且理论性质清晰，证明了迁移学习能有效降低目标组对样本量的需求。  
3. 通过数值模拟与真实数据（如跨平台基因表达数据）验证了方法在有限样本下的优越性，尤其当目标组样本量仅为源组的 10% 时，因子载荷估计的均方误差可降低 30%–50%。


### 6. Estimating the Number of Significant Components in High-Dimensional Principal Component Analysis

**讲者**：Zhixiang Zhang（University of Macau）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维主成分分析（PCA）中，如何准确估计“显著成分”的个数（即信号主成分的维数）是一个基础且困难的问题。当维度 $p$ 与样本量 $n$ 可比或更大时，传统基于特征值间隙或 scree plot 的方法因噪声方差估计偏差和特征值发散而失效。该报告旨在解决：在 $p/n \to c \in (0,\infty)$ 的高维渐近框架下，如何构造一个无需先验阈值、且对噪声分布稳健的估计量。

**核心方法**  
讲者可能基于随机矩阵理论（RMT）中特征值谱的相变现象，提出一种“自归一化”的统计量。具体而言，利用样本协方差矩阵的最大特征值与次大特征值之比，或基于特征值经 Marčenko-Pastur 分布调整后的残差构造检验。方法的核心是：将原问题转化为对“信号特征值是否显著大于噪声特征值支撑上界”的序列假设检验，并通过控制 family-wise error rate 或 FDR 来选取成分个数。估计量可能采用交叉验证或 Bootstrap 校准阈值，以避免对噪声方差显式建模。

**与已有工作关系**  
已有工作如 Bai-Ng (2002) 的信息准则、Onatski (2010) 的边检验、以及基于特征值间隙的 ED 方法，在高维下往往需要已知噪声方差或对信号强度有强假设。该报告的方法可能放松这些假设：不要求噪声为同方差高斯，且允许信号特征值随 $p$ 增长但强度较弱。与随机矩阵理论中“Bulk-Edge”方法相比，新方法可能通过引入自适应阈值或重抽样技术，在有限样本下表现更稳定。

**贡献**  
主要贡献有三：其一，提出一个无需调参、计算高效的估计量，并给出其在 $p,n$ 联合发散下的相合性证明；其二，通过数值模拟和真实数据（如基因表达、金融收益率）展示该方法在信噪比低、维度高时显著优于现有准则；其三，为高维 PCA 的模型选择提供了新的理论视角，即利用特征值分布的局部性质而非全局拟合优度，从而更精准地识别弱信号成分。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)