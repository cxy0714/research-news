# 因果推断 · 专题 C：因果发现、高维与生物医学/时序

> JCSDS 2026 · Causal Inference C — Discovery, High-Dim & Biomedical/Time Series · [返回会议总览](index.md)

- 含 **4 个分会场 · 21 场报告**（已检索到对应论文 6 场）

---

## Frontiers in Causal Inference and High-Dimensional Data Analysis

*7 月 13 日（周一） · 13:30-15:10 · Baihua Meeting Room*  
*组织 Jianqiao Wang（Tsinghua University） · 主持 Zijun Gao（University of Southern California）*

### 1. Causal Partial Identification via Optimal Transport

**讲者**：Zijun Gao（University of Southern California）

**对应论文**：Causal Partial Identification via Conditional Optimal Transport · [arXiv:2506.00257](https://arxiv.org/abs/2506.00257) · 📖 [长篇精读](../../deep_reads/jcsds2026-2506.00257.md)

<details><summary>摘要（原文）</summary>

We study the estimation of causal estimand involving the joint distribution of treatment and control outcomes for a single unit. In typical causal inference settings, it is impossible to observe both outcomes simultaneously, which places our estimation within the domain of partial identification (PI). Pre-treatment covariates can substantially reduce estimation uncertainty by shrinking the partially identified set. Recent work has shown that covariate-assisted PI sets can be characterized through conditional optimal transport (COT) problems. However, finite-sample estimation of COT poses significant challenges, primarily because the COT functional is discontinuous under the weak topology, rendering the direct plug-in estimator inconsistent. To address this issue, existing literature relies on relaxations or indirect methods involving the estimation of non-parametric nuisance statistics. In this work, we demonstrate the continuity of the COT functional under a stronger topology induced by the adapted Wasserstein distance. Leveraging this result, we propose a direct, consistent, non-parametric estimator for COT value that avoids nuisance parameter estimation. We derive the convergence rate for our estimator and validate its effectiveness through comprehensive simulations, demonstrating its improved performance compared to existing approaches.

</details>

**问题**：因果推断中许多估计量（如个体处理效应的分布、分位数处理效应、两潜在结果 $Y(1),Y(0)$ 的联合分布泛函）依赖于处理组与对照组结果的联合分布，但同一单元不可能同时观测到两种潜在结果，导致联合分布不可点识别，只能进行**部分识别**（partial identification, PI），得到一个识别区间。

**核心方法**：作者利用前处理协变量收缩识别集。已有工作表明，协变量辅助的 PI 集可通过**条件最优传输**（conditional optimal transport, COT）问题刻画——在给定协变量下对两条件边际做最优耦合，取极值给出上下界。难点在于 COT 泛函在弱拓扑下**不连续**，故直接 plug-in 估计不相合。本文的关键突破是证明：在由**适配 Wasserstein 距离**（adapted Wasserstein distance）诱导的更强拓扑下，COT 泛函是连续的。基于此，作者构造了一个**直接、相合、非参数**的 COT 值估计量，绕开了对非参数扰动参数（nuisance）的估计，并推导了收敛速率。

**与已有工作关系**：相较于 Manski 型经典 PI 边界，本文纳入协变量以收窄区间；相较于依赖松弛（relaxation）或需估计 nuisance 的间接方法（如 Ji、Lei 等的 COT 路线），本文用适配拓扑给出更简洁一致的直接估计。合作者 Blanchet、Glynn 是最优传输与随机模拟领域专家。

**贡献**：(1) 建立 COT 泛函在适配 Wasserstein 拓扑下的连续性；(2) 提出免 nuisance 的直接非参数估计量并给出收敛速率；(3) 模拟验证优于现有方法，为高维协变量下的因果部分识别提供了可计算框架。


### 2. Root Cause Discovery

**讲者**：Jinzhou Li（National University of Singapore）

**对应论文**：Root cause discovery via permutations and Cholesky decomposition · [arXiv:2410.12151](https://arxiv.org/abs/2410.12151) · 📖 [长篇精读](../../deep_reads/jcsds2026-2410.12151.md)

<details><summary>摘要（原文）</summary>

This work is motivated by the following problem: Can we identify the disease-causing gene in a patient affected by a monogenic disorder? This problem is an instance of root cause discovery. In particular, we aim to identify the intervened variable in one interventional sample using a set of observational samples as reference. We consider a linear structural equation model where the causal ordering is unknown. We begin by examining a simple method that uses squared z-scores and characterize the conditions under which this method succeeds and fails, showing that it generally cannot identify the root cause. We then prove, without additional assumptions, that the root cause is identifiable even if the causal ordering is not. Two key ingredients of this identifiability result are the use of permutations and the Cholesky decomposition, which allow us to exploit an invariant property across different permutations to discover the root cause. Furthermore, we characterize permutations that yield the correct root cause and, based on this, propose a valid method for root cause discovery. We also adapt this approach to high-dimensional settings. Finally, we evaluate the performance of our methods through simulations and apply the high-dimensional method to discover disease-causing genes in the gene expression dataset that motivates this work.

</details>

**问题**：本文由一个医学遗传学问题驱动——能否在单基因遗传病患者中定位致病基因？这被抽象为**根因发现**（root cause discovery）：以一组观测样本为参照，在**单个**干预样本中识别出被干预的变量。作者考虑因果序未知的**线性结构方程模型**（linear SEM）。

**核心方法**：首先分析一个基于平方 z-score 的朴素方法，刻画其成功与失败的条件，证明它一般**无法**识别根因（因为异常的边际偏差可能源于上游变量的传播而非该变量本身被干预）。随后，作者在**无额外假设**下证明：即便因果序不可识别，根因仍是可识别的。识别性结果的两个关键要素是**变量置换**（permutations）与**Cholesky 分解**：对协方差矩阵在不同置换下做 Cholesky 分解，利用跨置换的一个不变性质来锁定根因。作者进一步刻画了能产出正确根因的置换集合，据此提出一个有效的根因发现方法，并将其推广到**高维**情形。

**与已有工作关系**：不同于传统因果发现（如 PC、GES 需先估计整个 DAG），本文绕开完整因果序的估计，直接聚焦单一干预样本的根因定位；相较依赖异常 z-score 的启发式（在微服务故障定位、异常检测中常见），本文给出了严格的可识别性理论。合作者含 Maathuis（因果推断权威）与 Gagneur（计算基因组学），体现方法—应用结合。

**贡献**：(1) 证明因果序未知下根因的可识别性；(2) 提出基于置换+Cholesky 的可证明有效方法及高维版本；(3) 在真实基因表达数据上成功发现致病基因。


### 3. Nonparametric Estimation and Inference with Elliptic PDE Priors

**讲者**：Wenlu Xu（UCLA）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到与该题目直接对应的公开论文（arXiv/Google Scholar/作者主页均未见同名成果，可能为在研工作）**，以下基于讲者背景与题目方向合理推断。讲者 Wenlu Xu 为 UCLA 统计与数据科学系博士生，导师 Xiaowu Dai，主攻非参数推断、核方法、双重机器学习与因果推断，早期亦有随机微分方程背景。

**问题（推断）**：报告应研究以**椭圆型偏微分方程（elliptic PDE）诱导的先验**做非参数估计与统计推断。核心思路是：将未知函数 $f$ 建模为某椭圆算子（如 $(-\Delta+\kappa^2)^{\alpha}$，即 Whittle–Matérn/Laplace 型算子）驱动的随机场，等价于以 $\|Lf\|^2$（$L$ 为微分算子）为惩罚的正则化。这类先验与高斯过程/Matérn 核、薄板样条及 SPDE 表示（Lindgren–Rue–Lindqvist）密切相关，能借稀疏精度矩阵实现大规模空间数据的高效计算。

**核心方法（推断）**：可能在贝叶斯或惩罚样条框架下，以椭圆 PDE 定义 $f$ 的粗糙度惩罚/先验协方差，导出估计量并建立**后验收缩速率**或**渐近正态性**与置信区间的频率主义有效性，兼顾计算（有限元/谱基离散）与理论最优速率（minimax）。

**与已有工作关系（推断）**：区别于纯高斯过程回归，PDE 先验显式编码空间平滑与物理结构，接近 Nickl、Giordano 等关于 PDE 反问题贝叶斯推断的收敛率理论，并可能结合导师 Dai 的核方法/梯度信息推断思路，拓展到因果或高维场景。

**贡献（推断）**：给出基于椭圆 PDE 先验的可扩展非参数估计框架，及配套的不确定性量化理论保证。（以上为推断，具体以现场报告为准。）


## Advances in Statistical Learning and Causal Discovery

*7 月 13 日（周一） · 13:30-15:10 · Fanjing Mountains Meeting Room*  
*主持 Xuemei Hu（Chongqing Technology and Business University）*

### 1. A General Framework of Kalman Smoother for High-Dimensional Nonlinear Dynamic Systems

**讲者**：Haoxiang Zhan（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与该题目及讲者（Haoxiang Zhan, 北京大学）确切对应的公开论文，以下基于题目与领域方向合理推断。

**问题**：状态空间模型中，卡尔曼平滑器用于在给定全部观测 $y_{1:T}$ 下重构潜在状态轨迹 $x_{1:T}$，即估计后验 $p(x_t\mid y_{1:T})$。经典 Rauch–Tung–Striebel 平滑器仅适用于线性高斯系统；当系统同时具有**高维**状态和**非线性**演化/观测算子时，扩展卡尔曼(EKF/EKS)线性化误差大、集合卡尔曼(EnKS)受样本量与协方差秩亏限制、无迹变换在高维下退化。

**核心方法（推断）**：报告很可能提出一个统一框架，把非线性平滑写成对轨迹的正则化优化/变分问题，或在高维下引入低秩、稀疏、局部化(localization)的协方差结构以控制维数灾难。可能结合前向滤波—后向平滑的两遍策略，并对非线性算子采用统计线性化或矩匹配，配合可扩展的数值线性代数（低秩摄动、$O(d)$ 更新）。

**与已有工作关系**：衔接 RTS 平滑、EKS、EnKS、以及把卡尔曼平滑视为二次规划的优化视角（如 Aravkin 等的鲁棒/稀疏平滑）。相较集合方法，框架化处理可给出更一般的收敛与误差分析。

**贡献（推断）**：提供覆盖多类高维非线性动态系统的通用平滑框架、可扩展算法与理论保证，适用于时空数据同化、神经动力学、金融等场景。


### 2. Bayesian Network Based Inference for Multivariable Mendelian Randomization

**讲者**：Jiangyan Wang（Nanjing Audit University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与讲者（Jiangyan Wang, 南京审计大学）确切对应的公开论文，以下基于题目与方向推断（检索到主题相近的贝叶斯多变量 MR 工作如 arXiv:2510.09991，但作者不符）。

**问题**：多变量孟德尔随机化(MVMR)用遗传变异作为工具变量，同时估计多个暴露 $X_1,\dots,X_p$ 对结局 $Y$ 的因果效应，以剥离相关暴露间的混杂与中介。经典 MVMR（如 MVMR-IVW）依赖工具有效性假设，面对**水平多效性(pleiotropy)**、暴露间因果关联及弱工具时易产生偏倚。

**核心方法（推断）**：将暴露—结局关系嵌入**贝叶斯网络(有向无环图)**，用遗传变异作为锚点(genetic anchors)辨识网络结构与边的因果方向，再在网络约束下做因果效应的后验推断。相较把各暴露视为并列回归项，贝叶斯网络能显式建模暴露间的条件独立结构，区分直接效应与经由其他暴露的间接效应，并通过先验对多效性与稀疏结构进行正则。

**与已有工作关系**：融合 MVMR（IVW、Egger、中介 MR）与贝叶斯网络/结构学习（如 Howey 等 genetic-anchor 方法），以概率图模型统一处理效应估计与结构辨识。

**贡献（推断）**：提出基于贝叶斯网络的 MVMR 推断框架，可同时输出因果结构与效应后验、量化不确定性，并对多效性更稳健，适用于多组学/复杂表型的因果解析。


### 3. Improving Dynamic Treatment Regimes Using External Evidence

**讲者**：Zhenyu Wang（University of Michigan）

**对应论文**：Information Borrowing from Partially Compatible Trajectories for Estimation of Dynamic Treatment Regimes · [arXiv:2512.10069](https://arxiv.org/abs/2512.10069) · 📖 [长篇精读](../../deep_reads/jcsds2026-2512.10069.md)

经检索，讲者 Zhenyu (Zach) Wang（密歇根大学，导师 Lu Wang）最可能对应的论文为 arXiv:2512.10069《Information Borrowing from Partially Compatible Trajectories for Estimation of Dynamic Treatment Regimes》。（注：本环境无法抓取 arXiv 摘要页，abstract 暂缺，以下深读基于题目、作者主页及领域方向。）

**问题**：动态治疗方案(DTR)是根据患者随时间累积的历史，为多阶段决策给出个体化治疗规则。单一研究(如某个 SMART 试验)样本有限，估计的最优 DTR 方差大；而外部数据(历史试验、观察性队列)往往阶段设置、变量或治疗选项与目标研究**仅部分兼容**，直接合并会引入偏倚。

**核心方法**：提出从**部分兼容轨迹**借力的信息借用框架——识别外部轨迹中与目标决策问题在相关阶段/协变量上兼容的片段，加以对齐并纳入 Q-learning 或值搜索类估计，同时对不兼容部分做偏倚防护(如自适应加权/收缩)，在提升效率的同时控制外部证据带来的偏差。

**与已有工作关系**：延续 Q-learning、A-learning、值搜索等 DTR 估计路线，并与整合随机化与观察性数据估计最优 DTR 的近期工作相衔接，区别在于强调轨迹层面的“部分兼容”而非要求外部数据结构完全一致。

**贡献**：给出可利用异构外部证据、兼顾效率与稳健性的 DTR 估计方法及理论/数值验证，扩展了在数据稀缺场景下的精准医疗决策能力。


### 4. Semiparametric Estimation with Reduced Dimension for the Treatment Effect in Causal Inference under Missing Data

**讲者**：Tao Tan（Xinjiang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与讲者（Tao Tan, 新疆大学）确切对应的公开论文，以下基于题目与方向推断。

**问题**：在因果推断中估计平均处理效应(ATE)时，若协变量维度较高且部分数据缺失(缺失结局或缺失协变量)，同时估计倾向得分 $\pi(X)=P(T=1\mid X)$ 与结局回归 $m(X)=E[Y\mid X,T]$ 会面临维数灾难与模型误设。经典逆概率加权(IPW)、增广 IPW(AIPW/双稳健)在高维非参数成分下收敛慢、有效性受限。

**核心方法（推断）**：引入**降维**思想——通过充分降维(如充分降维方向、单/多指标结构 $g(\beta^\top X)$)把倾向得分与结局回归建立在低维投影 $\beta^\top X$ 上，再在半参数框架内构造估计方程。缺失数据部分很可能采用 MAR 假设下的加权/插补，并结合有效影响函数得到具双稳健性与半参数有效性的 ATE 估计。

**与已有工作关系**：衔接半参数因果推断的有效影响函数理论(Robins/Tsiatis 一脉)、双稳健估计与充分降维(SDR)方法，并针对缺失数据做加权校正，缓解高维非参数估计的“维数诅咒”。

**贡献（推断）**：提出在缺失数据下兼具降维、双稳健与半参数有效性的处理效应估计方法，改善高维协变量情形的估计精度与稳健性，并给出渐近正态性等理论保证。


### 5. High Dimensional Maximum Likelihood Theory for Poisson Regression with Increasing Dimensions

**讲者**：Xuemei Hu（Chongqing Technology and Business University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与讲者（Xuemei Hu, 重庆工商大学）确切对应的公开论文（检索到主题相近的 arXiv:2410.20671 高维泊松回归推断，但作者不符），以下基于题目与方向推断。

**问题**：当泊松回归 $Y_i\sim\text{Poisson}(\exp(x_i^\top\beta))$ 的参数维度 $p$ 随样本量 $n$ 增长(增维渐近，通常 $p/n\to\kappa\in[0,1)$)时，经典的固定维极大似然理论失效：MLE 会出现系统性偏倚，Wald/似然比统计量的标准 $\chi^2$ 近似不再成立。

**核心方法（推断）**：在增维框架下重新推导泊松回归 MLE 的高维渐近理论。可能沿用 Sur–Candès 关于高维逻辑回归的近似消息传递(AMP)/凸高斯极大极小(CGMT)技术路线，刻画 MLE 各分量的偏倚放大因子、方差修正与极限分布，并据此给出校正后的假设检验与置信区间。也可能在 $p=o(n)$ 的中等增维下建立一致性与渐近正态性，量化维度对 Fisher 信息与似然比的影响。

**与已有工作关系**：把 Sur & Candès (2019) 高维逻辑回归、以及高维 Cox/GLM 的“现代极大似然理论”推广到计数响应的泊松模型，填补指数族中泊松情形的高维精确渐近空白。

**贡献（推断）**：给出增维泊松回归 MLE 的精确高维分布与偏倚/方差修正，纠正传统推断的过度乐观，为高维计数数据(如基因组、网络计数、流行病学)的可靠推断提供理论基础。


### 6. Evaluating Treatment Effects Using Group Testing with Retesting of Positive Groups

**讲者**：Qi Zheng（University of Louisville）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与讲者（Qi Zheng, 路易斯维尔大学）确切对应的公开论文，以下基于题目与方向推断。

**问题**：群检测(group/pooled testing)将多个个体样本混合后一次检验，以在低患病率下节省检测成本。常见的**阳性组复检(retesting of positive groups)**方案(如 Dorfman 两阶段)对判为阳性的混合组再逐一或分层复检以定位阳性个体。本报告关注在这种带复检的群检测数据结构下，如何评估**处理/协变量对结局(如感染状态)的效应**，即在只观测到组级(及部分复检个体级)结果、个体真实状态部分缺失的情形下做回归型推断。

**核心方法（推断）**：为带复检的群检测建立似然，正确刻画组级检测结果与个体潜在状态的关系，并纳入检测灵敏度/特异度(误分类)。在此基础上构造回归模型(如 logistic)估计处理效应，采用 EM 算法或贝叶斯方法处理潜在个体状态，得到处理效应的一致估计与有效方差。

**与已有工作关系**：衔接群检测回归文献(如 Vansteelandt、McMahan、Tebbs、Bilder 等关于 pooled/hierarchical testing regression 的工作)，将其从患病率/协变量效应估计扩展到**处理效应评估**，并显式利用阳性组复检带来的额外个体级信息以提升效率。

**贡献（推断）**：提供在成本高效的群检测(含阳性复检)设计下评估处理效应的统计框架，兼顾误分类校正与效率，适用于传染病筛查、公共卫生干预评估等场景。


## Advances in Causal Inference for Biomedical and Social Sciences

*7 月 13 日（周一） · 08:30-10:10 · Qingyan Boardroom*  
*主持 Haoxiang Wang（Peking University）*

### 1. A Novel Secondary-Outcome Approach to Estimating Primary Causal Effects with Unmeasured Confounders

**讲者**：Desu Kong（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（arXiv/期刊均无精确匹配，仅见相关的 Springer《Causal Inference with Secondary Outcomes》一文，非本报告），以下基于题目与作者方向推断。**问题**：在观测研究中，主结局 $Y$ 与处理 $A$ 之间常受未测量混杂 $U$ 干扰，使 $E[Y(a)]$ 不可识别。**核心方法**：报告提出一种“借力次要结局（secondary outcome）”的新思路——引入一个与处理、混杂共享结构但本身不受关注的次要结局 $S$，作为工具/代理变量。通过对 $(Y,S)$ 联合建模，利用两结局对同一 $U$ 的暴露关系（类似 proximal/negative-control 或双结局矩条件），构造可识别的估计方程，从而在不额外测量 $U$ 的情况下剥离混杂偏倚，得到主因果效应的一致估计并给出渐近方差。**与已有工作关系**：区别于 E-value 敏感性分析与单纯的负对照（negative control outcome）框架，此法把次要结局从“证伪工具”升级为“主效应识别的信息源”，与 proximal causal inference、confounding bridge 思路相承但更强调主/次结局的层级结构。**贡献**：给出新的识别条件、双稳健或半参数有效估计量，并可能在生物医学/社会科学数据上验证其相较传统调整法在混杂稳健性上的优势。


### 2. When Screening Misleads: A Robust Mendelian Randomization Test for Reliable Causal Discovery

**讲者**：Bo Chen（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与题目精确对应的公开论文（arXiv/Scholar 仅返回大量相关 MR 方法学文献，如自动选择有效工具、cML、Winner's-curse-free MR 等，非本报告本身），以下基于题目与作者方向推断。**问题**：Mendelian Randomization (MR) 用遗传变异作工具变量 (IV) 推断暴露对结局的因果作用，但多数变异存在水平多效性 (horizontal pleiotropy) 或弱工具，属无效 IV。实践中常先做“筛选 (screening)”挑出显著变异，标题指出这种基于同一数据的筛选会引入选择偏倚（如 winner's curse），导致因果发现被“误导”。**核心方法**：报告应提出一种对筛选偏倚稳健的 MR 检验——可能通过样本分裂/交叉拟合、去偏 (debiasing) 或后选择推断 (post-selection inference) 校正筛选带来的过度乐观，并在允许部分工具无效（如多数有效或 InSIDE 假设放松）下构造对因果零假设 $H_0:\beta=0$ 的有效检验，保证 I 类错误控制与检验功效。**与已有工作关系**：延续 MR-Egger、加权中位数、MR-PRESSO、cML 等对多效性的稳健化路线，但重点针对“先筛选后检验”这一被忽视的偏倚来源，与近年 winner's-curse-aware MR 相呼应。**贡献**：揭示筛选误导机制并给出可靠因果发现的稳健检验及其理论保证与组学/GWAS 应用。


### 3. Partially Functional Dynamic Backdoor Diffusion-Based Causal Model

**讲者**：Xinwen Liu（Yunnan University(Southwest United Graduate School)）

**对应论文**：Partially Functional Dynamic Backdoor Diffusion-based Causal Model · [arXiv:2509.00472](https://arxiv.org/abs/2509.00472) · 📖 [长篇精读](../../deep_reads/jcsds2026-2509.00472.md)

检索到对应 arXiv 论文 2509.00472（因环境限制未能抓取摘要原文，deep_read 基于标题、多个索引页题录及作者方向）。**问题**：在含时间维度与未测量混杂的观测数据中做因果效应估计与反事实/干预生成，尤其当协变量部分为函数型（随时间连续变化的曲线，partially functional）、处理与结局动态演化时，传统结构因果模型难以刻画高维分布。**核心方法**：将扩散模型 (diffusion-based generative model) 嵌入因果框架，构建“后门 (backdoor) 扩散因果模型”——利用后门准则识别可调整的混杂集，以扩散过程建模条件分布 $p(Y\mid \text{do}(A), C)$，其中 $C$ 含标量与函数型分量（partially functional），并引入动态 (dynamic) 结构处理时间演化。通过 backdoor 调整在生成过程中实现干预下的采样，从而估计动态处理效应与反事实轨迹。**与已有工作关系**：延续将扩散/生成模型用于因果推断的路线（如 Diffusion Model in Causal Inference with Unmeasured Confounders、DCM 等），创新在于把函数型数据分析 (FDA) 与动态后门调整结合进扩散框架，处理连续时间协变量。**贡献**：提出 PFD-BDCM 模型、给出识别与估计策略，并在含函数型协变量的时序因果场景验证其对复杂分布与动态效应的建模能力。


### 4. Causal Bayesian Network Learning: Application to the Causal Analysis of Masticatory Function and Coronary Heart Disease in Older Adults

**讲者**：Chunzi Wang（Shanghai Normal University Tianhua College）

**对应论文**：Causal Bayesian network learning: application to the causal analysis of masticatory function and coronary heart disease in older adults · [论文/主页](https://link.springer.com/article/10.1186/s12911-026-03549-3)

检索到对应论文，发表于 BMC Medical Informatics and Decision Making（DOI 10.1186/s12911-026-03549-3，题目完全一致；因环境限制未能抓取摘要原文，deep_read 基于题录与领域方向）。**问题**：老年人群中咀嚼功能 (masticatory function) 下降与冠心病 (coronary heart disease, CHD) 是否存在因果关联，及其经由哪些中间变量（营养、口腔健康、代谢因素等）传导，仅靠回归相关分析难以揭示方向与机制。**核心方法**：采用因果贝叶斯网络 (Causal Bayesian Network, CBN) 学习——从观测队列数据出发，用基于评分 (score-based，如 BIC/BDeu) 或基于约束 (constraint-based，如 PC 算法) 的结构学习自动构建变量间的有向无环图 (DAG)，估计条件概率并据 $do$-演算推断干预效应，从而刻画咀嚼功能 $\to$ CHD 的直接/间接路径。**与已有工作关系**：属于将 CBN/结构学习应用于观测医学研究的路线（近年 causal discovery in observational medical research 综述所归纳），相较传统流行病学回归能同时做变量选择、路径发现与因果排序。**贡献**：在真实老年人群数据上用 CBN 学习揭示咀嚼功能与冠心病的因果网络结构及潜在中介，为口腔-心血管健康关联提供数据驱动的因果证据与可解释模型。


### 5. Clike: Colocalization by LD-Informed Cosine Kernel Embedding

**讲者**：Wenxin Jiang（City University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（arXiv/bioRxiv/Scholar 无 Clike 精确匹配，仅见 coloc、SharePro、eCAVIAR 等既有共定位方法），以下基于题目与方法名推断。**问题**：基因组共定位 (colocalization) 判断 GWAS 性状信号与分子性状（如 eQTL）是否由同一因果变异驱动，以推断致病基因。经典方法（coloc 的 PP.H4）对多因果信号、连锁不平衡 (LD) 结构敏感，且假设单因果变异时易失效。**核心方法**：Clike 提出“LD 信息的余弦核嵌入 (LD-informed cosine kernel embedding)”——将两性状在同一区域的关联信号（如 z-score 向量或效应量谱）嵌入到由 LD 矩阵加权/白化的空间，用余弦相似度 (cosine kernel) 度量两信号向量方向的一致性；因 LD 会使相邻变异统计量相关，先以 LD 结构对嵌入做校正/加权，再计算核相似度作为共定位证据。方向一致（余弦接近 1）提示共享因果变异。**与已有工作关系**：区别于贝叶斯后验概率框架 (coloc/SharePro) 与精细定位式方法 (eCAVIAR)，改用核方法/几何相似度，计算高效且天然适应多信号与 LD；与将 embedding/kernel 用于遗传关联的思路相通。**贡献**：给出 Clike 方法、LD 感知的核构造与显著性判定，兼顾多因果信号下的准确性与可扩展性，用于 GWAS-eQTL 靶基因发现。


### 6. Tight Causal Bounds on Rare Outcomes under Multiple Biases in Test-Negative Design

**讲者**：Haoxiang Wang（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到与题目精确对应的公开论文（同名 Haoxiang Wang 另有 LSE 学者，应以北京大学单位区分；Scholar 仅返回 TND 与偏倚综述类文献），以下基于题目与作者方向推断。**问题**：检验阴性设计 (Test-Negative Design, TND) 广泛用于疫苗有效性评估，但同时受多重偏倚 (multiple biases)——选择偏倚、未测量混杂、错分等——影响；当结局罕见 (rare outcome) 时，点识别几乎不可能，需要部分识别 (partial identification)。**核心方法**：报告应在 TND 框架下推导因果参数（如疫苗有效性/风险比）的紧界 (tight/sharp bounds)。利用罕见结局的近似（发病率趋零使风险比≈优势比，简化非线性约束），对多重偏倚各设可解释的敏感性参数，构造联合约束下的优化问题，求解可达的上下确界，证明其为在给定假设内不可再收紧的 sharp bounds。**与已有工作关系**：延续 Manski 式部分识别与 TND 因果偏倚分析、E-value/敏感性分析路线，创新在于同时处理多种偏倚并针对罕见结局给出闭式或可计算的紧界，而非单一偏倚的点估计校正。**贡献**：给出 TND 下多重偏倚、罕见结局的锐界理论与敏感性分析工具，使疫苗有效性推断在不做过强假设时仍能给出可信区间，增强观测性疫苗研究的稳健性。


## Advances in Time Series and Causal Machine Learning

*7 月 12 日（周日） · 15:30-17:10 · ASEAN Roundtable Forum Meeting Room*  
*主持 Junni Zhang（Peking University）*

### 1. Z-Valued Smooth Transition GARCH Models: Specification and Testing

**讲者**：Fukang Zhu（Jilin University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（arXiv/期刊均无对应预印本），以下基于题目与 Fukang Zhu 长期研究方向（整数值/计数时间序列、INGARCH 族）合理推断。**问题**：经典 GARCH 处理实值收益率，而计数或整数值数据（如交易次数、事故数、可正可负的整数增量）需要专门的条件异方差模型。这里“Z-Valued”指取值于整数集 $\mathbb{Z}$（含负整数）的时间序列，通常借助 Skellam 或差分泊松等分布刻画。作者拟在 INGARCH 框架上引入**平滑转移（Smooth Transition, STAR 型）**机制，使条件均值/条件强度参数随某转移变量 $s_{t-d}$ 通过 logistic 或指数转移函数 $G(s_{t-d};\gamma,c)$ 在两个（或多个）状态间连续切换，从而刻画整数值波动的非线性与状态依赖（如高/低活跃期的持续性差异）。**核心方法**：给出模型的平稳性与遍历性条件、基于条件极大似然或泊松拟似然的参数估计及其渐近正态性；重点构造**线性性检验**（即是否需要平滑转移项，$H_0:\gamma=0$ 存在参数在零假设下不可识别的 Davies 问题），通常用 Taylor 展开近似转移函数得到辅助 LM/得分检验统计量。**与已有工作关系**：将实值 STAR-GARCH 与整数值 INGARCH（Ferland、Fokianos、Weiß 等）结合，并延伸到 $\mathbb{Z}$ 值情形，弥补现有计数模型多限于非负整数的不足。**贡献**：提出 Z 值平滑转移 GARCH 的设定、估计与非线性检验一整套推断工具，并预期以模拟与实际计数金融/流行病数据验证。


### 2. A Unified Statistical Framework for Testing Stochastic Dominance

**讲者**：Weiqi Yang（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（未在 arXiv 或作者主页定位到该题目预印本），以下基于题目与随机占优检验文献合理推断。**问题**：随机占优（Stochastic Dominance, SD）用于在不设定具体效用函数的前提下比较两个分布的优劣，是金融资产比较、福利与不平等分析的核心工具。一阶（FSD）、二阶（SSD）乃至更高阶占优可统一写成对分布函数反复积分 $D_s^F(x)=\int_{-\infty}^x D_{s-1}^F(t)\,dt$ 后的逐点比较 $D_s^F(x)\le D_s^G(x)$。现有检验（如 McFadden、Barrett–Donald、Linton–Maasoumi–Whang、Davidson–Duclos）在零假设设定、上/下确界型与积分型统计量、以及重抽样方法上各不相同，缺乏统一处理。**核心方法**：作者拟建立一个**统一框架**，将不同阶数、不同方向（占优/被占优）以及“最不利/least favorable”与“接触集（contact set）”等零假设纳入同一检验结构，构造以经验过程 $\sqrt{n}(\hat D_s^F-\hat D_s^G)$ 为基础的统计量，并用重抽样/乘子 bootstrap 或子抽样逼近其（依赖接触集的）极限分布，以获得渐近精确的水平控制与相合性。**与已有工作关系**：整合并推广 Barrett–Donald、Linton 等分散的检验，在同一理论下比较其功效与稳健性，可能进一步处理弱占优、几乎随机占优或多样本联合占优。**贡献**：提供统一的理论、可实现的统计量与重抽样推断，以及功效更优、适用面更广的随机占优检验工具，辅以模拟与金融/福利实证。


### 3. Testing and Estimation of Change Point in ARMA Model with Heavy-Tailed G-GARCH Noises

**讲者**：Qiang Bai（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（arXiv 与期刊数据库均未定位到该题目），以下基于题目与变点/重尾时间序列文献合理推断。**问题**：金融与经济时间序列常呈 ARMA 型条件均值动态，其新息又具有条件异方差与**重尾**特征（有限方差可能不成立）。若数据生成过程在某未知时点发生结构突变（ARMA 系数变化），需要在**重尾 GARCH（这里记 G-GARCH，广义/一般化 GARCH）**噪声下同时**检验**是否存在变点并**估计**其位置。重尾使经典基于二阶矩的 CUSUM 型统计量失效或收敛缓慢。**核心方法**：推断很可能采用对重尾稳健的手段——如基于分位数/最小绝对偏差（LAD）残差、自加权（self-weighted）估计或秩/符号型 CUSUM 统计量——构造对变点的检验量，其零假设极限分布通常为布朗桥泛函；变点位置由 argmax/argmin 型估计给出并建立收敛速率（重尾下常快于轻尾的 $n$ 速率）。G-GARCH 结构需引入平稳性与矩条件（可能只要求分数阶矩存在）以保证渐近理论。**与已有工作关系**：延续 Bai(1994)、Kokoszka–Leipus 关于 ARMA/GARCH 变点的框架，并针对重尾情形改用稳健统计量，弥补现有方法在无限方差下失效的不足。**贡献**：给出重尾 G-GARCH 新息下 ARMA 模型变点的检验统计量、位置估计及其渐近性质，配合模拟功效评估与金融重尾数据（如收益率、汇率）实证，提供对厚尾稳健的结构突变诊断工具。


### 4. Impact Mechanism of Digital Economy Policies on the Synergistic Effects of Pollution-Carbon Reduction in Cities: A Causal Inference Approach Based on Double Machine Learning

**讲者**：Yuhuan Sun（Dongbei University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（该研究属应用经济学/环境经济学实证，多发表于中文或环境类期刊，未在 arXiv 定位到对应预印本），以下基于题目与双重机器学习（DML）政策评估文献合理推断。**问题**：数字经济政策（如国家大数据综合试验区、宽带中国、智慧城市等试点）是否以及通过何种机制促进城市**污染减排与碳减排的协同（pollution–carbon reduction synergy）**效应？传统固定效应/双重差分（DID）在高维协变量与非线性混杂下易有设定偏误。**核心方法**：采用 Chernozhukov 等（2018）的**双重/去偏机器学习（Double/Debiased Machine Learning）**，在部分线性模型 $Y=\theta D+g(X)+\varepsilon$ 中用随机森林、梯度提升、Lasso 等灵活拟合处理变量方程 $D=m(X)+v$ 与结果方程 $g(X)$，通过 Neyman 正交得分与交叉拟合（cross-fitting）获得政策效应 $\theta$ 的 $\sqrt{n}$ 一致且渐近正态的估计，消除正则化偏差与过拟合偏差。以城市面板（可能为中国地级市）为样本，被解释变量为污染物与 $CO_2$ 排放的协同指标，处理为数字经济政策实施。**与已有工作关系**：相较传统 DID/中介分析，DML 更稳健地处理高维混杂并允许非线性；文章还应做机制分析（如产业结构升级、绿色技术创新、能源效率等中介渠道）与异质性分析。**贡献**：为数字经济政策的减污降碳协同效应提供基于 DML 的因果证据与机制识别，兼具方法学（DML 在环境政策评估的应用）与政策含义（数字化推动绿色低碳协同治理）价值。


### 5. Generalized Spectral Testing with Sample Splitting

**讲者**：Yuxin Tao（Southern University of Science and Technology）

**对应论文**：Generalized Spectral Testing with Sample Splitting · [arXiv:2605.29315](https://arxiv.org/abs/2605.29315) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.29315.md)

<details><summary>摘要（原文）</summary>

Residual-based goodness-of-fit tests for parametric time-series models are often complicated by parameter-estimation effects, which can alter the limiting behavior of diagnostic statistics. We propose a sample-splitting generalized spectral test (in the spirit of Escanciano(2006)) for assessing conditional mean specification in linear and nonlinear time-series models. The procedure estimates the model parameter on a fitting subsample and constructs a generalized spectral Cramer-von Mises statistic from residuals computed on a checking/testing subsample. The statistic aggregates pairwise conditional mean restrictions over all lags and is therefore bandwidth-free and free of truncation-lag selection. Under mild regularity conditions and a score-alignment condition, the residual-based process has the same limiting null distribution as the infeasible oracle process based on the true errors. Although the resulting limiting law is still non-pivotal, it can be consistently approximated by a simple multiplier bootstrap that does not require generating bootstrap time series or re-estimating parameters. Such an oracle-equivalence property is in sharp contrast to the original full-sample test, for which parameter estimation contributes an additional first-order term to the limiting process, and requires re-estimating parameters in each bootstrapped sample. We further establish consistency of the proposed test against fixed alternatives and nontrivial power against local alternatives. Extensive simulations and real data analyses show that the proposed test controls size well, has comparable power, and delivers substantial computational savings in models where repeated estimation is costly.

</details>

**问题**：时间序列参数模型的残差型拟合优度检验普遍受“参数估计效应”困扰——用估计参数构造的残差诊断统计量，其极限分布往往不同于用真实误差构造的理想（oracle）版本，导致临界值失真且 bootstrap 代价高昂。**核心方法**：作者在 Escanciano(2006) 广义谱框架下提出**样本分裂**思路：在拟合子样本上估计参数 $\hat\theta$，在独立的检验子样本上计算残差并构造广义谱 Cramér–von Mises 统计量。该统计量在所有滞后阶上聚合成对的条件均值约束 $E[\varepsilon_t\mid\varepsilon_{t-j}]=0$，因而**无需带宽、无需截断滞后选择**。关键理论是：在温和正则性与一个“score-alignment（得分对齐）”条件下，残差过程与基于真实误差的 oracle 过程具有**相同的零假设极限分布**（oracle 等价性）。虽然极限律仍非枢轴量，但可用简单的**乘子 bootstrap** 一致逼近，且无需重新生成时间序列或重估参数。**与已有工作关系**：相比原始全样本检验（参数估计会贡献一阶附加项、每次 bootstrap 都需重估参数），本法通过样本分裂消除一阶估计效应，大幅降低计算成本。**贡献**：建立 oracle 等价性、给出对固定备择的相合性与对局部备择的非平凡功效，并通过模拟与实证展示良好的水平控制、可比的功效及显著的计算节省，尤其适用于重复估计昂贵的模型。


### 6. Stable Causal Targeting with Machine Learning: Application to a Consumer Finance Field Experiment

**讲者**：Junni Zhang（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（arXiv 上 Junni Zhang 近作集中于随机实验因果推断，但未定位到此题目的预印本），以下基于题目与政策学习/异质处理效应文献合理推断。**问题**：企业（如消费金融机构）常希望用机器学习估计的**条件平均处理效应（CATE）** $\tau(x)=E[Y(1)-Y(0)\mid X=x]$ 来做个性化**目标干预（targeting）**，即只对预测收益为正的客户施加处理（如提额、优惠、催收策略）。然而 CATE 的机器学习估计噪声大、跨样本/跨环境不稳定，直接“择优而治”的目标策略可能过拟合、可复现性差。**核心方法**：作者拟提出**稳定（stable）**的因果目标策略——可能通过对处理规则加正则化或稳定性约束、控制策略在数据扰动/子样本间的方差、或采用分布稳健/保守的策略学习目标，在“效应估计”与“规则稳定性”间权衡，从而在保证可复现的前提下最大化目标干预的期望收益（policy value）。方法很可能结合双重稳健/正交得分与交叉拟合来无偏评估策略价值。**应用**：将方法用于一项**消费金融领域的现场实验（field experiment）**，用真实随机化数据评估目标策略相对全体处理或随机处理的增益与稳定性。**与已有工作关系**：延续 Athey–Wager 的政策学习、Künzel 等 meta-learner 与 Kitagawa–Tetenov 的经验福利最大化，强调**稳定性/可复现性**这一实践痛点。**贡献**：提出兼顾统计稳定与因果最优的目标干预框架，并以消费金融现场实验验证其商业与统计价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)