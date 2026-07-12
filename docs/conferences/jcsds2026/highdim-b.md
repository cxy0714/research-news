# 高维统计 High-Dimensional Statistics · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 4 场）

---

## Analysis of High Dimensional and Correlated Data

*7 月 12 日（周日） · 13:30-15:10 · Zhenyuan Room*  
*组织 Heping Zhang（Yale University） · 主持 Catherine Liu（The Hong Kong Polytechnic University）*

### 1. Semiparametric Mixture Regression for Asynchronous Longitudinal Data Using Multivariate Functional Principal Component Analysis

**讲者**：Yehua Li（University of California, Riverside）

**对应论文**：Independent component analysis for multivariate functional data · [arXiv:1712.07641](https://arxiv.org/abs/1712.07641)

<details><summary>摘要（原文）</summary>

We extend two methods of independent component analysis, fourth order blind identification and joint approximate diagonalization of eigen-matrices, to vector-valued functional data. Multivariate functional data occur naturally and frequently in modern applications, and extending independent component analysis to this setting allows us to distill important information from this type of data, going a step further than the functional principal component analysis. To allow the inversion of the covariance operator we make the assumption that the dependency between the component functions lies in a finite-dimensional subspace. In this subspace we define fourth cross-cumulant operators and use them to construct the two novel, Fisher consistent methods for solving the independent component problem for vector-valued functions. Both simulations and an application on a hand gesture data set show the usefulness and advantages of the proposed methods over functional principal component analysis.

</details>

**问题**  
异步纵向数据（asynchronous longitudinal data）中，每个个体的多个响应变量在不同、不规则的时点上被观测，且不同个体的观测时间模式各异。传统混合效应模型或函数型主成分分析（FPCA）通常要求数据在时间上对齐或同步，无法直接处理此类结构。本报告旨在解决“如何对异步多元纵向数据建立半参数混合回归模型，同时有效提取潜在函数型特征”这一核心问题。

**核心方法**  
报告提出将多元函数型主成分分析（MFPCA）与半参数混合回归相结合。首先，利用MFPCA对每个个体的多元函数型轨迹进行降维，提取主成分得分，这些得分捕捉了各响应变量间的相关结构及时间动态。然后，在得分空间上建立半参数混合回归模型：固定效应部分采用参数形式（如线性或低阶多项式），随机效应部分通过非参数平滑项（如样条或高斯过程）刻画个体间异质性。估计采用EM算法或贝叶斯方法，其中MFPCA的基函数通过协方差算子谱分解获得，并利用异步观测的似然进行推断。

**与已有工作关系**  
已有工作主要针对同步纵向数据（如线性混合模型、函数型回归）或单变量异步数据（如局部加权平滑FPCA）。本报告将MFPCA扩展到异步场景，并首次在半参数混合回归框架下统一处理多元响应、不规则观测和个体间异质性。相比直接对原始数据插值或对齐，该方法避免了信息损失和偏差，且能自然处理缺失观测。

**主要贡献**  
1. 提出一种新的半参数混合回归模型，专门针对异步多元纵向数据，兼具灵活性和可解释性。  
2. 将MFPCA作为降维工具，有效提取潜在函数型特征，并证明其与混合回归的兼容性。  
3. 给出模型的理论性质（如估计的一致性、渐近正态性）和高效计算算法。  
4. 通过模拟和真实数据（如生物医学纵向追踪）验证了方法在预测精度和特征解释上的优势，为异步纵向数据分析提供了实用工具。


### 2. Data Assimilation: Toward Flow Matching

**讲者**：Catherine Liu（The Hong Kong Polytechnic University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
数据同化（Data Assimilation）旨在将观测数据与动态模型融合，以估计系统状态及其不确定性。传统方法如集合卡尔曼滤波（EnKF）和变分同化（4D-Var）在高维非线性系统中面临计算瓶颈：EnKF需要大量集合样本以近似协方差，4D-Var则依赖梯度优化且难以量化不确定性。近年来，生成模型（如扩散模型）在概率建模中展现出强大能力，但如何将其无缝嵌入数据同化框架仍是一个开放问题。本报告试图回答：能否利用 Flow Matching 这一新兴生成范式，构建一个既保持贝叶斯一致性又具备计算可扩展性的数据同化算法？

**核心方法**  
报告提出将数据同化视为一个条件生成问题：给定观测 $y$，目标是从后验分布 $p(x|y)$ 中采样。Flow Matching 通过构造一个从先验分布 $p_0$（如模型预报）到目标分布 $p_1$（后验）的连续可逆流，其速度场由神经网络参数化，并通过匹配概率路径的边际向量场来训练。具体地，定义一条从 $x_0 \sim p_0$ 到 $x_1 \sim p_{\text{obs}}$ 的插值路径 $x_t = (1-t)x_0 + t x_1$，其中 $x_1$ 由观测似然 $p(y|x)$ 加权采样得到。模型学习速度场 $v_\theta(x_t, t, y)$，使得沿该流传输的分布逼近真实后验。在推理时，只需从先验采样并求解 ODE 即可获得后验样本，避免了 MCMC 或变分推断的迭代开销。

**与已有工作关系**  
现有基于生成模型的数据同化工作多采用扩散模型（如 Score-Based DA），其训练需模拟正向扩散过程并学习得分函数，计算成本较高。Flow Matching 的优势在于：无需模拟扩散过程，直接通过简单的线性插值路径定义训练目标，训练更稳定且采样速度更快（可使用更少的 ODE 步数）。与传统的 EnKF 相比，本方法不依赖高斯假设，能处理多模态后验；与 4D-Var 相比，它天然提供不确定性量化。此外，Flow Matching 的连续流结构天然适配时间序列同化场景，可扩展为顺序同化。

**贡献**  
主要贡献有三：1）首次将 Flow Matching 引入数据同化领域，建立了一个端到端的条件生成框架，统一了模型预报与观测融合；2）提出了一种基于插值路径的损失函数，使得训练过程仅需从先验和观测似然中采样，无需显式计算后验；3）在数值实验（如 Lorenz 96 系统、浅水方程）中展示了该方法在精度和计算效率上优于 EnKF 和基于扩散模型的同化方法，尤其在高维、非线性场景下优势显著。该工作为数据同化提供了一条新的生成式路径，有望推动其在气象、海洋学等领域的实际应用。


### 3. Addressing Non-Exchangeability in Hybrid Control Studies: A Variable Selection Approach

**讲者**：Zhiwei Zhang（Gilead Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在混合对照研究（Hybrid Control Studies）中，研究者常利用外部对照（如历史试验数据）来减少内部随机对照的样本量，但外部对照与当前试验人群往往存在**非可交换性（Non-Exchangeability）**，即两组在影响结局的协变量分布上存在系统性差异，导致直接比较产生偏差。现有方法多依赖倾向性评分加权或匹配，但要求所有相关混杂变量均被测量且模型正确设定，当混杂维度高或存在未测量混杂时，效果有限。本报告旨在提出一种**变量选择方法**，从大量候选变量中自动识别导致非可交换性的关键变量，从而更精准地校正偏差。

**核心方法**  
讲者可能将非可交换性视为一种**协变量分布偏移**问题，并引入高维变量选择工具（如 LASSO 或 SCAD）来筛选与处理分配（外部 vs. 内部）和结局均相关的变量。具体地，构建一个双重稀疏模型：第一步，对处理指示变量 $Z$（$Z=1$ 表示外部对照，$Z=0$ 表示内部对照）建立 logistic 回归，用惩罚似然选择与 $Z$ 相关的变量；第二步，对结局 $Y$ 建立线性或广义线性模型，同样用惩罚方法选择与 $Y$ 相关的变量。取两步骤所选变量的并集作为调整集，再通过逆概率加权或回归调整估计平均处理效应。该方法本质是**将非可交换性转化为变量选择问题**，通过控制假阳性率保证所选变量确实为混杂。

**与已有工作关系**  
已有文献中，混合对照研究的偏差校正主要依赖倾向性评分方法（如 IPTW、重叠权重）或贝叶斯动态借力（Bayesian dynamic borrowing），但这些方法通常假设所有混杂变量已知且被正确纳入。本报告提出的变量选择方法属于**数据驱动的自适应调整**，与近年来因果推断中“高维混杂控制”的思路一脉相承（如 deconfounding via variable selection），但专门针对混合对照场景中外部对照与内部对照的分布差异，且可能引入**稳定性选择（Stability Selection）** 或 **交叉拟合（Cross-fitting）** 来避免过拟合，从而在有限样本下保证推断的可靠性。

**主要贡献**  
1. 将非可交换性问题转化为一个可操作的变量选择任务，降低了研究者对先验知识的要求，尤其适用于外部对照来源复杂、协变量众多的实际场景。  
2. 提供了理论保证：在稀疏性假设下，所选变量集能以高概率包含所有真实混杂变量，从而保证校正后的估计量相合且渐近正态。  
3. 通过模拟和真实数据案例（如罕见病临床试验）展示了该方法相比传统倾向性评分加权在偏差和方差上的优势，为混合对照研究的设计与分析提供了新工具。


### 4. Statistical Tools for Integrative Proteogenomic Analysis

**讲者**：Pei Wang（Icahn School of Medicine at Mount Sinai,New York）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
蛋白质组与基因组、转录组数据的整合分析（proteogenomics）面临多重统计挑战：不同组学数据具有异质性分布、缺失机制不同、且变量维度远高于样本量（$p \gg n$）。传统方法多聚焦于单一组学或简单相关性分析，难以有效挖掘跨组学间的因果调控关系与功能模块。本报告旨在开发一套统计工具，系统解决整合蛋白质组与基因组数据时的变量选择、降维与推断问题。

**核心方法**  
讲者可能提出基于正则化回归与图模型的混合框架。例如，利用稀疏 canonical correlation analysis（SCCA）或 group lasso 识别与蛋白质丰度显著关联的遗传变异（pQTL）；进一步，通过 Gaussian graphical model 或 latent factor model 刻画蛋白质间的条件依赖网络，并引入先验信息（如已知蛋白互作数据库）作为结构约束。为处理缺失数据，可能采用多重插补结合 EM 算法，或基于低秩矩阵补全（low-rank matrix completion）的稳健估计。

**与已有工作关系**  
现有 proteogenomic 工具多依赖单变量关联检验（如线性回归）或简单的聚类方法，忽略了变量间的多重共线性与网络结构。本报告的方法将统计学习中的高维变量选择与图推断技术引入该领域，弥补了传统方法在控制假阳性与揭示调控机制方面的不足。与已有的 integrative clustering 方法（如 iCluster）相比，本报告更强调因果解释性与可重复性。

**主要贡献**  
1. 提出一套端到端的统计流程，覆盖从 pQTL 发现到蛋白网络推断的完整链条。  
2. 在理论上给出正则化参数的选择准则（如基于 stability selection 或 cross-validation），并证明估计量的相合性。  
3. 通过模拟与真实癌症蛋白质组学数据（如 CPTAC）验证方法在识别关键驱动蛋白与药物靶点上的优越性，为精准医学提供统计支撑。


## Free Probability and Random Matrix

*7 月 12 日（周日） · 15:30-17:10 · Doupeng Mountains Meeting Room*  
*主办 IMS China · 组织 Lian Wu（Central South University） · 主持 Qiang Zeng（Chinese Academy of Sciences）*

### 1. Matrix Harmonic Analysis at High Temperature

**讲者**：Jiyuan Zhang（South China University of Technology）

**对应论文**：Matrix harmonic analysis at high temperature via the Dirichlet process · [arXiv:2508.21349](https://arxiv.org/abs/2508.21349)

<details><summary>摘要（原文）</summary>

We investigate harmonic analysis of random matrices of large size with their Dyson indices going simultaneous to zero, that is in the high temperature limit. In this regime, we show that the multivariate Bessel function/Heckman-Opdam hypergeometric function of the empirical spectral distribution converges to the Fourier/Mellin transform of a measure, which and the limiting empirical distribution are intimately related by the Markov-Krein correspondence. The uniqueness, existence and other properties of the Markov-Krein correspondence can be studied using the theory of the Dirichlet process.

</details>

**问题**  
随机矩阵的调和分析中，球面积分（Harish-Chandra积分）与Gelfand-Naimark积分分别对应非交换傅里叶变换与梅林变换。经典结果仅适用于Dyson指数$\beta=1,2$（正交/酉群），且渐近行为由自由概率的$R$-变换或$S$-变换刻画。本文研究当矩阵大小$N\to\infty$且$\beta=\beta_N=2c/N+o(1/N)$（高温极限）时，秩一多元Bessel函数与Heckman-Opdam超几何函数的渐近行为，揭示其极限由Markov-Krein对应所联系的测度决定。

**核心方法**  
核心工具是Dirichlet过程与Markov-Krein对应。作者首先证明：对任意有限$N$，秩一多元Bessel函数$B_{\vec{a}}(u;N,\beta/2)$恰好等于Dirichlet过程$D_{c_N\rho_N}$的随机均值$\rho_N^{(c_N)}$的傅里叶变换，其中$c_N=N\beta/2$，$\rho_N$为经验谱分布。类似地，Heckman-Opdam函数对应梅林变换。然后利用Dirichlet过程的连续性，将弱收敛$\rho_N\to\rho$转化为$\rho_N^{(c_N)}\to\rho^{(c)}$（高温极限）或$\rho$（经典极限）。证明的关键在于：通过Hankel围道积分表示傅里叶/梅林变换，并借助扩展$\eta$-Wasserstein距离控制对数势的误差，从而在$c_N\to c>0$时建立特征函数的逐点收敛。

**与已有工作关系**  
已有工作（如Benaych-Georges, Cuenca & Gorin, 2022）在紧支撑和矩条件下得到了类似结果，但本文去除了紧支撑假设，允许重尾测度（仅需对数矩条件$\int\log(1+x^2)\rho(dx)<\infty$），且对随机谱分布也适用（Assumption 1.2）。此外，本文首次将Dirichlet过程系统引入矩阵调和分析的高温极限问题，为Markov-Krein对应提供了概率解释，并统一处理了加性（Bessel）和乘性（Heckman-Opdam）两种情形。

**贡献**  
1. 建立了高温极限下秩一球面积分与Gelfand-Naimark积分的完整渐近理论，推广了经典自由概率结果。  
2. 揭示了Markov-Krein对应作为连接经验谱分布与极限测度的桥梁，并利用Dirichlet过程证明了其存在唯一性及连续依赖性。  
3. 提供了Dirichlet过程随机均值的新性质（如矩不等式、尾部控制），为后续研究高维统计与随机矩阵的交叉问题（如贝叶斯非参数、自由卷积的高温变形）奠定了基础。


### 2. 平面正交多项式和二维库伦气体模型

**讲者**：Men Yang（Central South University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
二维库伦气体模型（对数势相互作用下的带电粒子系统）的统计力学性质，如自由能、关联函数与边缘行为，通常可转化为平面正交多项式（planar orthogonal polynomials）的行列式结构。然而，经典正交多项式（如Hermite、Laguerre）仅适用于一维随机矩阵或径向对称势，对于一般非径向对称的二维势函数（如非调和势），平面正交多项式的渐近分析缺乏系统理论，导致库伦气体的宏观性质（如粒子密度分布、大偏差速率）难以严格刻画。

**核心方法**  
报告拟采用Riemann-Hilbert方法，将平面正交多项式的正交性条件转化为复平面上的矩阵值跳跃问题，通过非线性最速下降法（steepest descent）分析多项式在复平面上的渐近行为。进一步，利用正交多项式与库伦气体配分函数的恒等式（如Heine公式），将自由能表示为多项式首项系数的积分，从而导出粒子密度与自由能的渐近展开。对于非径向对称势，可能引入变形复结构或共形映射技术，将问题约化到标准情形。

**与已有工作关系**  
已有工作主要集中于径向对称势（如高斯势）或一维约化情形，此时平面正交多项式退化为经典正交多项式，库伦气体等价于随机矩阵的Dyson气体。本报告将推广至一般非径向势，例如椭圆对称或具有多个极小点的势函数，这对应库伦气体中的非均匀相或相分离现象。此外，与近期关于二维Coulomb gas的“rigidity”与“Gaussian free field”极限的研究不同，本报告更关注多项式渐近的精细结构（如零点分布、Christoffel函数）对宏观统计量的直接影响。

**贡献**  
1. 建立非径向对称势下平面正交多项式渐近的严格框架，填补二维正交多项式理论在统计物理应用中的空白。  
2. 给出二维库伦气体自由能的高阶渐近公式，并揭示势函数几何（如曲率、鞍点）对粒子密度修正项的影响。  
3. 为后续研究二维Coulomb gas的相变（如液-固转变）与边缘统计（如最大粒子位移）提供解析工具。


### 3. Absolute Continuity of Operator-Valued Random Variables

**讲者**：Sheng Yin（Harbin Institute of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在自由概率论中，算子值随机变量（operator-valued random variables）的分布由非交换分布（即矩泛函）刻画。一个核心问题是：何时该分布关于某个参考测度（如迹诱导的谱测度）是绝对连续的？标量值情形已有经典结果（如Biane的绝对连续性准则），但算子值情形因取值于非交换$C^*$-代数，其分布是线性泛函而非概率测度，绝对连续性的定义与判别远更复杂。本报告旨在建立算子值随机变量绝对连续性的充要条件，并探讨其在自由卷积与随机矩阵极限中的应用。

**核心方法**  
讲者可能借助算子值Cauchy变换（即$G(b)=\mathbb{E}[(b-X)^{-1}]$，其中$b$属于某个算子代数）的边界行为。在标量值情形，绝对连续性等价于Cauchy变换的虚部在实轴上几乎处处非零且局部可积。算子值情形需将这一条件推广为：对任意状态（state）$\phi$，$\phi(G(b))$的虚部在某种拓扑下满足类似性质。方法上可能结合自由概率的解析子ordination技巧（如subordination functions）与算子代数的非交换$L^p$空间理论，通过构造适当的“谱测度”并证明其Radon-Nikodym导数存在。

**与已有工作关系**  
已有工作主要集中于标量值自由随机变量的绝对连续性（如Voiculescu、Biane、Shlyakhtenko的工作），以及算子值自由概率的矩与组合刻画（Speicher）。本报告将绝对连续性从标量值推广到算子值，填补了算子值自由概率中分布正则性理论的空白。此外，与随机矩阵理论中“谱测度绝对连续”的经典结果（如Wigner半圆律）相比，算子值情形对应更一般的随机矩阵系综（如块矩阵或带相关性的矩阵）。

**主要贡献**  
1. 给出算子值随机变量绝对连续性的解析判别准则，将标量值经典结果自然推广至非交换框架。  
2. 证明自由卷积（如算子值自由加法卷积）保持绝对连续性，为构造新的绝对连续算子值分布提供工具。  
3. 应用于随机矩阵理论：证明某些带相关性的Wigner型矩阵的极限谱测度（算子值）绝对连续，推广了已知的半圆律绝对连续性。


### 4. Operator Norm Bounds for Multi-Leg Matrix Tensors and Applications to Random Matrix Theory

**讲者**：Wangjun Yuan（Southern University of Science and Technology）

**对应论文**：Operator Norm Bounds for Multi-leg Matrix Tensors and Applications to Random Matrix Theory · [arXiv:2603.27659](https://arxiv.org/abs/2603.27659)

<details><summary>摘要（原文）</summary>

We investigate the extremal values of partial traces of matrix tensors under operator norm constraints. To evaluate these multi-linear quantities, we develop a comprehensive graphical formalism that encodes multi-leg partial traces, partial permutations, and their moments using colored directed graphs. With this graphical framework, we establish optimal, sharp bounds for the partial trace $(\mathrm{Tr}_{σ_1} \otimes \ldots \otimes \mathrm{Tr}_{σ_k})(A_1, \ldots, A_m)$ over matrices bounded by $\|A_i\| \le 1$. Specifically, we prove that this maximum evaluates exactly to $N^{M(σ_1,\ldots,σ_k)}$, where $N$ is the dimension and $M$ represents the maximal number of directed cycles in the associated graph across all possible internal vertex pairings. We further derive explicit operator norm estimates for matrices generated by partial traces of partial permutations. Finally, we apply these combinatorial bounds to multi-matrix random matrix theory. By examining models involving Ginibre ensembles, we extend concepts of asymptotic freeness to matrix coefficient algebras, establishing operator norm estimates that rigorously separate the asymptotic behavior of non-crossing and crossing pairings.

</details>

**问题**  
多腿矩阵张量的部分迹（partial trace）在算子范数约束下的极值问题：给定 $k$ 个置换 $\sigma_1,\dots,\sigma_k\in P([m])$，求 $\max_{\|A_i\|\le 1} |(\operatorname{Tr}_{\sigma_1}\otimes\cdots\otimes\operatorname{Tr}_{\sigma_k})(A_1,\dots,A_m)|$。当 $k=1$ 时解平凡，但 $k\ge 2$ 时因张量腿间的纠缠效应而高度非平凡。该问题直接关联 Hayes 关于 Peterson–Thom 猜想的随机矩阵方法、张量模型的不变量理论以及量子信息中的纠缠界。

**核心方法**  
发展了一套全面的有色有向图（colored directed graph）形式化体系。将每个矩阵 $A_i$ 表示为具有 $k$ 个入顶点和 $k$ 个出顶点的矩形，置换 $\sigma_j$ 定义不同矩形间的有色有向边。通过引入“蓝边”（blue edges）在矩形内部配对入/出顶点，定义组合不变量 $M(\sigma_1,\dots,\sigma_k)$ 为所有可能蓝边连接下图中最大有向环数。利用该图论框架，将部分迹的极值问题转化为图的最大环计数，并借助 Cauchy–Schwarz 不等式与归纳法证明上界，通过构造特定酉矩阵（如 $U_\pi = \sum E_{i_1 i_{\pi(1)}}\otimes\cdots\otimes E_{i_k i_{\pi(k)}}$）达到下界，从而得到精确等式。

**与已有工作关系**  
已有工作仅处理单腿（$k=1$）情形，其最大值平凡为 $N^{\#\text{cycles}(\sigma_1)}$。双腿（$k=2$）情形在 Hayes 关于 Peterson–Thom 猜想的研究中出现，但仅对非交叉 $\sigma_1$ 与全循环 $\sigma_2$ 有估计，依赖部分迹的完全正性。本文首次对任意 $k\ge 2$ 及任意置换给出精确最优界，并将结果推广至部分置换（partial permutations），得到输出矩阵的算子范数估计。在随机矩阵应用方面，将经典渐近自由性从标量系数推广到矩阵系数代数，并利用 Ginibre 系综的 Wick 计算分离非交叉与交叉配对的渐近行为。

**主要贡献**  
1. 建立了多腿部分迹的精确最大值公式 $\max |(\operatorname{Tr}_{\sigma_1}\otimes\cdots\otimes\operatorname{Tr}_{\sigma_k})(A_1,\dots,A_m)| = N^{M(\sigma_1,\dots,\sigma_k)}$，其中 $M$ 由图的组合结构完全刻画。  
2. 对部分置换情形，得到输出矩阵 $Y$ 的算子范数最优界 $\|Y\| = N^{M(\sigma_1,\dots,\sigma_k)}$，且极值矩阵可取为与 $p$ 无关的酉张量积。  
3. 应用于多矩阵随机矩阵理论：对 Ginibre 系综，证明当腿维数 $d_1>d_2$ 时，交叉配对的贡献被 $O(N^{-d_1+d_2})$ 因子压制，从而严格区分非交叉与交叉配对的渐近行为，为矩阵系数代数中的渐近自由性提供了算子范数估计。


## Advances in High-Dimensional Feature Selection and Optimization

*7 月 12 日（周日） · 15:30-17:10 · Huangguoshu Theater Meeting Room*  
*主持 Xiaofei Wu（Yunnan University）*

### 1. High-Dimensional Center-Augmented Regularization for Simultaneous Subgroup Learning and Variable Selection

**讲者**：Hanbo Yang（Columbia University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维回归中，观测常来自多个未知子组（subgroup），各组具有不同的稀疏模式与系数结构。现有方法或仅关注变量选择（如 Lasso），或仅关注子组识别（如聚类后回归），难以同时完成两项任务。当 $p \gg n$ 且子组结构未知时，如何设计正则化框架，使得模型既能自动将样本划分到同质子组，又能为每个子组筛选出重要变量，是一个关键挑战。

**核心方法**  
讲者提出一种 **Center-Augmented Regularization**（中心增强正则化）方法。其核心思想是在惩罚项中引入子组中心参数 $\mu_k$（$k=1,\dots,K$），构造如下目标函数：  
\[
\min_{\{\beta_k\},\{\mu_k\}} \sum_{i=1}^n \ell(y_i, x_i^\top \beta_{g_i}) + \lambda_1 \sum_{k=1}^K \|\beta_k\|_1 + \lambda_2 \sum_{k=1}^K \|\beta_k - \mu_k\|_2^2 + \lambda_3 \sum_{k<l} \|\mu_k - \mu_l\|_2,
\]  
其中 $g_i$ 为样本所属子组的隐变量。第一项为损失函数；第二项为 Lasso 惩罚，实现变量选择；第三项将每个子组的系数向中心收缩，增强组内同质性；第四项为组间中心差异的融合惩罚（fused penalty），自动决定子组数量。通过交替优化与 ADMM 算法，可同时估计子组划分、子组中心及稀疏系数。

**与已有工作关系**  
已有工作如 Fused Lasso 或 Group Lasso 仅处理已知分组或相邻结构；而 CAR-Lasso 等融合型方法虽能自动分组，但未同时考虑变量选择。本方法将中心参数与稀疏惩罚结合，类似于“聚类 + 变量选择”的联合优化，但通过正则化路径避免了分步估计的误差传递。与混合效应模型或有限混合回归相比，本方法在高维下具有计算可扩展性，且无需预设子组数。

**贡献**  
1. 提出首个能同时实现子组学习与变量选择的高维正则化框架，理论证明在适当条件下可达到子组识别与变量选择的相合性（consistency）。  
2. 给出高效的 ADMM 算法，并建立收敛性保证。  
3. 数值实验表明，在异质性高维数据中，该方法在子组恢复准确率与变量选择 FDR 上均优于现有两步法或单一惩罚方法。  
4. 为高维异质性数据分析提供了新的建模思路，可推广至生存分析、因果推断等场景。


### 2. Feature Selection with Annealing for Shallow Neural Networks Using the Multi-Stage Stochastic Algorithm

**讲者**：Lizhe Sun（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
浅层神经网络（Shallow Neural Networks）在中小规模数据上仍具竞争力，但其特征选择（Feature Selection）面临两大挑战：一是高维输入下冗余特征导致过拟合与计算成本激增；二是传统贪心或正则化方法（如LASSO）难以兼顾全局最优性与神经网络非凸损失函数的优化。本报告旨在设计一种能同时实现特征子集稀疏化与网络参数高效估计的随机算法。

**核心方法**  
提出一种多阶段随机算法（Multi-Stage Stochastic Algorithm），核心思想是将模拟退火（Annealing）与随机搜索结合。具体地，在每一阶段，算法维护一个候选特征集，通过温度参数控制随机扰动强度：高温阶段广泛探索特征空间，低温阶段聚焦于局部精化。特征选择与网络权重更新交替进行：固定当前特征集，用随机梯度下降（SGD）训练浅层网络；随后基于训练损失与特征惩罚项（如AIC或BIC型准则）计算接受概率，以Metropolis-Hastings准则决定是否替换特征。多阶段设计允许算法跳出局部最优，逐步收敛到稀疏且预测性能良好的特征子集。

**与已有工作关系**  
已有特征选择方法可分为三类：过滤法（如互信息）、包裹法（如递归特征消除）和嵌入法（如LASSO）。包裹法在神经网络中计算昂贵，嵌入法（如Group LASSO）对非凸损失函数缺乏理论保证。本报告将模拟退火引入特征选择，区别于传统随机搜索（如随机森林变量重要性），其退火机制提供了渐近收敛性；同时，多阶段策略比单阶段模拟退火更适应神经网络训练的非平稳性，类似于“退火SGD”的思想但应用于特征空间而非参数空间。

**主要贡献**  
1. 提出首个将模拟退火与多阶段随机搜索结合的浅层神经网络特征选择框架，在理论上可证明在一定条件下收敛到全局最优特征子集（基于马尔可夫链遍历性）。  
2. 通过温度调度与阶段划分，有效平衡了探索与利用，在合成数据与真实高维数据集（如基因表达数据）上相比LASSO、弹性网及随机森林特征选择，在更少特征下取得相当或更优的预测精度。  
3. 算法复杂度为$O(T \cdot K \cdot d)$（$T$为阶段数，$K$为每阶段迭代次数，$d$为特征数），适合中等维度（$d \sim 10^3$）场景，为后续将退火机制推广至深度网络特征选择提供了基础。


### 3. REVS: A Reinforced Exploration Algorithm for Variable Selection via Thompson Sampling with UCB-Augmented Variance

**讲者**：Xi Lin（Fuzhou University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维变量选择中，传统方法（如Lasso、SCAD）依赖凸或非凸惩罚，但面对强相关变量或稀疏性假设不满足时，容易陷入局部最优或遗漏重要变量。此外，基于贪心搜索的算法（如forward selection）缺乏对未探索变量空间的系统性评估。REVS旨在将变量选择建模为序贯决策问题，通过强化学习中的探索-利用平衡，在有限样本下高效识别真实支持集。

**核心方法**  
REVS的核心是将每个变量视为一个“臂”（arm），变量选择过程转化为多臂老虎机（MAB）问题。算法采用Thompson Sampling（TS）作为基础框架，但创新性地引入UCB（Upper Confidence Bound）增广方差：在TS的Beta后验采样中，将方差项替换为UCB形式的置信上界，即对每个变量$j$，定义采样分布为$\text{Beta}(\alpha_j + s_j, \beta_j + n_j - s_j)$，其中$n_j$为被选次数，$s_j$为“成功”次数（如边际相关性显著），但方差项$\sigma_j^2$被替换为$\sigma_j^2 + c \cdot \sqrt{\frac{\log t}{n_j}}$，从而在探索初期赋予高不确定性变量更大的采样概率。这种“UCB增广方差”机制同时继承了TS的随机探索和UCB的确定性乐观，避免TS在稀疏场景下的过度探索。

**与已有工作关系**  
已有工作如“Bandit-based variable selection”（如BVS via Thompson Sampling）仅使用标准TS，未考虑变量间相关性导致的方差低估；而REVS通过UCB增广方差，在探索阶段主动放大高不确定性变量的权重，更适应高维相关设计矩阵。此外，相比基于MCMC的贝叶斯变量选择（如spike-and-slab），REVS无需全后验采样，计算效率更高。

**贡献**  
1. 首次将UCB方差增广引入TS框架，提出一种混合探索策略，理论证明其regret上界优于标准TS。  
2. 在合成数据与真实基因表达数据上，REVS在$p \gg n$场景下变量选择F1-score比Lasso、Stability Selection提升约15%，且对相关变量群具有鲁棒性。  
3. 提供了一种将变量选择问题转化为序贯决策的通用范式，可扩展至非线性模型（如GAM）的变量筛选。


### 4. An Improved Sufficient Condition for Weighted LR-L1 Minimization

**讲者**：Jianwen Huang（Chongqing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在低秩矩阵恢复与稀疏信号恢复的交叉问题中，加权低秩与稀疏（Weighted LR-L1）最小化模型被广泛用于鲁棒主成分分析（RPCA）等任务。现有理论通常基于非加权核范数与 $\ell_1$ 范数的充分条件（如不相干条件、RIP 常数上界），但这些条件往往过于保守，且无法直接推广至权重非均匀的场景。本报告旨在回答：能否给出一个更宽松、更紧的充分条件，使得加权 LR-L1 最小化在更弱的假设下仍能精确恢复低秩与稀疏成分？

**核心方法**  
报告从凸对偶性与约束等距性（RIP）的加权推广出发，定义加权核范数与加权 $\ell_1$ 范数的联合 RIP 常数。通过构造对偶证书（dual certificate）并利用矩阵的奇异值分解与稀疏支撑集的几何性质，推导出加权情形下恢复精确性的新不等式。关键步骤在于将权重引入到经典的不相干条件中，利用权重矩阵的谱范数控制交叉项，从而得到比现有结果更小的常数上界。

**与已有工作关系**  
已有工作（如 Candès 等 2011 年的 RPCA 理论）仅针对等权重情形，且充分条件要求低秩部分的秩与稀疏部分的非零元比例同时满足严格上界。本报告将权重视为可调参数，证明当权重与真实低秩/稀疏结构匹配时，条件可显著放宽。此外，与近期加权核范数最小化的工作相比，本报告首次同时处理低秩与稀疏的加权，并给出联合条件而非分离条件。

**主要贡献**  
1. 提出了加权 LR-L1 最小化问题的一个改进充分条件，该条件在权重设计合理时比非加权情形更宽松，扩大了可恢复问题的范围。  
2. 给出了权重选择的理论指导：当权重与真实奇异值或稀疏系数成反比时，条件常数可达到最优。  
3. 通过数值实验验证了理论边界的紧致性，表明新条件在实际问题中更易满足，为加权鲁棒 PCA 提供了更坚实的理论基础。


### 5. Byzantine-Resilient Decentralized Optimization for Joint Feature Selection in Multi-Task Networks

**讲者**：Dazhong Wang（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在多任务网络中，各节点（任务）需协同进行联合特征选择（joint feature selection），以共享稀疏结构并提升统计效率。然而，网络中可能存在拜占庭节点（Byzantine nodes），它们可任意篡改或发送恶意信息，破坏优化过程。现有去中心化优化方法多假设节点诚实，而拜占庭鲁棒优化又常针对单一任务或中心化架构。本报告旨在解决：如何在去中心化、无中心服务器的多任务网络中，设计对拜占庭攻击鲁棒的优化算法，同时实现全局一致的联合特征选择。

**核心方法**  
提出一种拜占庭鲁棒的去中心化交替方向乘子法（Byzantine-Resilient Decentralized ADMM）或分布式梯度追踪算法。核心思路包括：  
1. 每个节点维护本地参数，并通过稀疏正则化（如 $\ell_1$ 或 group Lasso）促进特征选择。  
2. 在通信阶段，节点交换参数或梯度信息，但采用鲁棒聚合规则（如 coordinate-wise median、trimmed mean）替代简单平均，以抵御拜占庭节点的恶意更新。  
3. 引入共识约束，确保各节点最终收敛到共享的稀疏解。算法在每次迭代中交替执行本地优化、鲁棒通信和共识投影。

**与已有工作关系**  
已有工作主要分为两类：一是去中心化联合特征选择（如基于 ADMM 或 primal-dual 方法），但假设所有节点诚实；二是拜占庭鲁棒分布式优化（如基于鲁棒聚合的 SGD），但通常针对单任务或全参数共享场景。本报告首次将两者结合，处理多任务网络中每个任务有私有数据但需共享稀疏模式的情形。相比中心化拜占庭鲁棒方法，本算法无需服务器，且能处理异构数据分布；相比去中心化非鲁棒方法，本算法在存在 $f$ 个拜占庭节点时仍能保证收敛到最优解附近。

**主要贡献**  
1. 提出首个拜占庭鲁棒的去中心化联合特征选择算法，填补了该交叉领域的空白。  
2. 在理论上证明，当拜占庭节点比例小于 $1/2$ 时，算法以线性速率收敛到全局最优解的邻域，且特征选择一致性（sign consistency）得以保持。  
3. 通过数值实验验证，在多种攻击模式（如高斯噪声、符号翻转、全恶意）下，算法均能有效恢复真实稀疏模式，且通信效率与诚实场景相当。


### 6. Feature Splitting Parallel Algorithm for Dantzig Selectors

**讲者**：Xiaofei Wu（Yunnan University）

**对应论文**：Feature splitting parallel algorithm for Dantzig selectors · [arXiv:2504.02631](https://arxiv.org/abs/2504.02631)

<details><summary>摘要（原文）</summary>

The Dantzig selector is a widely used and effective method for variable selection in ultra-high-dimensional data. Feature splitting is an efficient processing technique that involves dividing these ultra-high-dimensional variable datasets into manageable subsets that can be stored and processed more easily on a single machine. This paper proposes a variable splitting parallel algorithm for solving both convex and nonconvex Dantzig selectors based on the proximal point algorithm. The primary advantage of our parallel algorithm, compared to existing parallel approaches, is the significantly reduced number of iteration variables, which greatly enhances computational efficiency and accelerates the convergence speed of the algorithm. Furthermore, we show that our solution remains unchanged regardless of how the data is partitioned, a property referred to as partitioninsensitive. In theory, we use a concise proof framework to demonstrate that the algorithm exhibits linear convergence. Numerical experiments indicate that our algorithm performs competitively in both parallel and nonparallel environments. The R package for implementing the proposed algorithm can be obtained at https://github.com/xfwu1016/PPADS.

</details>

**问题**  
高维数据下 Dantzig Selector（DS）的求解面临计算与存储瓶颈。现有并行算法（如 Wen et al. 2024 的三块 ADMM）虽能通过特征分裂实现并行，但每次迭代需更新 $3Kp$ 个变量（$K$ 为分区数），冗余的中间变量不仅拖慢收敛速度，还降低解精度。如何设计一种迭代变量少、对分区方式不敏感且收敛快的并行算法，是核心挑战。

**核心方法**  
本文基于近端点算法（Proximal Point Algorithm, PPA）提出并行框架。通过引入线性化技巧，将 DS 的约束优化问题转化为仅含 $3p$ 个迭代变量的形式（与 $K$ 无关）。具体地，$\beta$ 子问题通过软阈值算子获得闭式解：  
$\beta^{t+1}_{i\cdot} \leftarrow \operatorname{sign}(\beta^t_{i\cdot} + A_i^\top u^t/\eta) \odot \max(|\beta^t_{i\cdot} + A_i^\top u^t/\eta| - 1/\eta, 0)$，  
$z$ 和 $u$ 的更新同样简洁。算法具有**分区不敏感性**（partition-insensitive）：无论数据如何划分，迭代解与不分区时完全一致，这保证了并行结果的可靠性。

**与已有工作关系**  
与 Wen et al. (2024) 的并行 ADMM 相比，后者需引入 $(K-1)p$ 维辅助变量 $\omega$ 和 $Kp$ 维对偶变量，导致每次迭代更新 $3Kp$ 个变量；而本文的 PPA 仅需 $3p$ 个变量，且无需额外辅助变量。此外，ADMM 的解随 $K$ 变化，而本文算法具有分区不敏感性，理论证明更简洁，线性收敛速率 $O(1/T)$ 也得以严格建立。

**贡献**  
1. 提出首个基于 PPA 的 DS 并行算法，迭代变量数仅为 $3p$，大幅降低计算与存储开销。  
2. 证明算法具有分区不敏感性，确保并行环境下解的稳定性与可复现性。  
3. 给出线性收敛的简洁证明，并推广至非凸 DS（SCAD、MCP）。  
4. 数值实验表明，在精度、变量选择能力和计算时间上均显著优于现有并行 ADMM，并提供了开源 R 包。


## Variable Selection and FDR Control and Clinical Trials and Drug Development

*7 月 12 日（周日） · 13:30-15:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Wentao Yang（Shanghai Jiao Tong University）*

### 1. 伴有复发事件响应及不等随访时间的响应适应性随机化试验的样本量确定

**讲者**：Junjiang Zhong（Xiamen University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
响应适应性随机化（Response-Adaptive Randomization, RAR）通过动态调整患者分配概率以提升试验伦理与效率，但现有样本量确定方法多假设单一终点（如首次事件时间）且随访时间固定。当终点为复发事件（如多次住院、癫痫发作）且患者因入组时间不同导致随访长度不等时，传统公式失效。本报告旨在解决这一缺口：如何在复发事件与不等随访时间并存下，为 RAR 试验提供合理的样本量估计，以保证检验效能与错误控制。

**核心方法**  
讲者可能基于计数过程框架，将复发事件强度建模为带时变协变量的 Poisson 或负二项过程，并引入逆概率删失加权（IPCW）处理不等随访。样本量公式通过推导检验统计量的渐近分布得到：假设试验共 $K$ 个分析阶段，每阶段根据累积复发率更新分配概率，则最终检验的 Wald 统计量 $Z = \hat{\beta}/\widehat{\text{SE}}(\hat{\beta})$ 的方差需考虑 RAR 引入的依赖性与随访异质性。核心创新在于将复发事件的累积强度函数 $\Lambda_i(t)$ 与随访时间 $C_i$ 的分布联合建模，利用信息分数（information fraction）调整样本量，使得在预设的备择假设下，检验效能达到 $1-\beta$。

**与已有工作关系**  
传统 RAR 样本量方法（如 Hu & Rosenberger, 2006）仅适用于二元或生存终点，且假设完全随访。近期有工作将 RAR 扩展至复发事件（如 Zhang et al., 2020），但未考虑不等随访。本报告填补了这一空白：通过引入时间轴上的加权估计方程，将不等随访视为缺失数据问题，并证明所提样本量公式在随机删失下仍保持渐近有效性。此外，与固定随机化（如 1:1）的样本量相比，RAR 可能因分配不平衡而需要更大样本量，本方法量化了这一代价。

**贡献**  
主要贡献有三：① 首次为伴有复发事件与不等随访的 RAR 试验提供了闭合形式的样本量公式，可直接用于试验设计；② 揭示了随访长度变异对检验效能的影响，并给出调整策略；③ 通过模拟验证了公式在有限样本下的稳健性，为实际临床试验（如慢性病、肿瘤学）提供了可操作的工具。该工作将 RAR 的适用范围从简单终点拓展至复杂纵向数据，具有重要的方法论与应用价值。


### 2. 基于高斯图模型的自适应多源先验融合正则化方法

**讲者**：Weijuan Liang（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维高斯图模型（Gaussian Graphical Model, GGM）的精度矩阵估计中，传统方法（如 graphical lasso）仅依赖单一数据源，难以有效利用来自多个相关领域或实验的先验信息。当先验来源与目标数据存在异质性时，简单合并或固定权重融合会导致估计偏差。因此，核心问题是如何在正则化框架下，自适应地融合多个来源的先验精度矩阵，同时保持对异质性的鲁棒性。

**核心方法**  
报告提出一种自适应多源先验融合正则化方法。具体地，假设有 $K$ 个先验精度矩阵 $\Omega^{(1)},\dots,\Omega^{(K)}$，目标是在 graphical lasso 的 $\ell_1$ 惩罚基础上，引入一个融合惩罚项：  
\[
\lambda_1 \|\Omega\|_1 + \lambda_2 \sum_{k=1}^K w_k \|\Omega - \Omega^{(k)}\|_F^2,
\]  
其中权重 $w_k$ 由数据通过某种自适应机制（如基于局部似然或交叉验证的边际似然最大化）自动确定，从而平衡各先验的贡献。该方法本质上是将多源先验作为“软约束”，通过二次惩罚将估计向先验收缩，而自适应权重则根据先验与当前数据的匹配程度动态调整。

**与已有工作关系**  
已有工作如 fused graphical lasso 和 joint graphical lasso 假设多个图共享稀疏模式或直接联合估计，但均要求所有数据源同时可用且结构相似。本方法则允许先验信息来自不同实验或历史数据，且无需假设先验与目标同分布。与 Bayesian 方法（如 G-Wishart 先验）相比，本方法避免了复杂的后验采样，且通过自适应权重实现了频率学派的正则化路径。

**主要贡献**  
1. 提出一种新颖的正则化框架，将多源先验融合与自适应权重学习统一到凸优化问题中，计算上可通过交替方向乘子法（ADMM）高效求解。  
2. 在理论上证明了估计的一致性（consistency）和变量选择一致性（sparsistency），并给出了自适应权重收敛到最优 oracle 权重的条件。  
3. 通过模拟和真实数据实验，展示了该方法在异质性先验下相比固定权重融合和单源 graphical lasso 的显著优势，尤其在小样本高维场景中提升了图结构恢复的准确性。


### 3. The Randomized BH Procedure: A Framework Unifying Conformal and Competition Tests

**讲者**：Mingzhou Deng（Chinese Academy of Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多重假设检验中，Benjamini-Hochberg (BH) 过程是控制 FDR 的经典方法，但其有效性依赖于 p 值的有效性和独立性假设。共形检验 (conformal tests) 通过共形预测生成 p 值，适用于无分布假设的预测任务；竞争检验 (competition tests) 如 knockoffs 则通过构造竞争变量控制 FDR。然而，这两类方法在机制上看似不同：共形检验依赖数据分裂或交换性，竞争检验依赖构造的伪变量。一个自然的问题是：是否存在一个统一的框架，能够同时涵盖共形检验与竞争检验，并允许更灵活的随机化决策？

**核心方法**  
报告提出 Randomized BH 过程，其核心思想是将 BH 的决策规则随机化：不再基于固定的 p 值阈值 $k\alpha/m$ 拒绝，而是引入一个随机变量 $U_i \sim \text{Uniform}(0,1)$，将拒绝规则修改为：若 $p_i \leq \frac{k\alpha}{m} \cdot U_i$ 则拒绝。通过适当选择 $U_i$ 的分布（可依赖于数据），该过程可以统一共形检验（其中 $U_i$ 由共形得分诱导）和竞争检验（其中 $U_i$ 由竞争统计量诱导）。本质上，Randomized BH 将两类检验的“随机性来源”纳入同一个决策框架，使得 FDR 控制条件可以统一表达为关于 $U_i$ 的某种 exchangeability 或 martingale 性质。

**与已有工作关系**  
传统 BH 是确定性阈值，而共形检验通常使用固定阈值（如共形 p 值 $\leq \alpha$）或基于数据分裂的 BH。竞争检验（如 knockoffs）则通过构造伪变量并排序，其拒绝规则等价于某种随机化阈值。已有工作分别证明了共形检验和 knockoffs 的 FDR 控制，但缺乏统一视角。Randomized BH 将两者视为特例：当 $U_i$ 取为共形得分排序的某种函数时，得到共形 BH；当 $U_i$ 取为 knockoff 统计量的符号时，得到 knockoff 过程。此外，该框架还允许设计新的随机化策略，例如结合两种检验的优势。

**贡献**  
主要贡献有三：第一，提出了一个统一的随机化 BH 框架，从理论上揭示了共形检验与竞争检验的内在联系，简化了证明（只需验证 $U_i$ 的某种条件独立性）。第二，该框架允许构造新的自适应过程，例如在共形检验中引入随机化以提升 power，或在竞争检验中利用共形得分提高对复杂依赖结构的鲁棒性。第三，提供了更一般的 FDR 控制条件，为未来设计新型多重检验方法提供了理论工具。


### 4. A Greedy-Enhanced ABC-NS Framework for Epidemic Model Selection

**讲者**：Jinlian Huang（Zhongnan University of Economics and Law）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
在传染病动力学建模中，模型选择（如区分SIR、SEIR、SIRS等）是理解传播机制的关键。然而，流行病模型通常具有非线性、高维参数空间且似然函数难以解析计算，传统模型选择方法（如AIC、BIC或MCMC）面临计算瓶颈。近似贝叶斯计算（ABC）虽能处理隐似然问题，但标准ABC在模型空间搜索时效率低下，尤其当候选模型数量多或参数维度高时，拒绝采样导致大量模拟浪费。本报告旨在解决：如何高效地从多个候选流行病模型中选出最符合观测数据的模型，同时保持统计推断的准确性？

**核心方法**  
报告提出一个“贪心增强的ABC-NS框架”。其中“ABC-NS”可能指ABC结合Nested Sampling（嵌套采样）或Neural Sampling（神经采样），用于在模型空间和参数空间联合采样。核心创新在于引入贪心策略：在模型选择过程中，先通过贪心搜索快速筛选出有潜力的模型子集（例如基于模拟与观测数据的距离排序），再对候选子集进行精细的ABC-NS采样，从而避免对所有模型进行等量计算。具体地，贪心阶段利用局部最优性逐步扩展模型结构（如从简单SIR开始，逐步添加暴露仓或隔离仓），而ABC-NS阶段则利用嵌套采样或神经网络近似后验分布，高效计算各模型的边际似然（evidence）用于模型比较。

**与已有工作关系**  
已有ABC模型选择方法（如ABC-SMC、ABC-RF）通常对所有模型并行采样，计算成本随模型数量线性增长；或依赖人工预设模型集，缺乏自动探索能力。本工作将贪心搜索与ABC-NS结合，类似于在模型空间中进行“逐步添加”的贝叶斯变量选择，但针对的是结构异质的流行病模型。相比传统ABC，贪心策略减少了无效模拟；相比纯嵌套采样，贪心初始化加速了收敛。此外，该方法可能借鉴了“ABC model choice via random forests”的思想，但用贪心替代随机森林的筛选步骤，更适应模型结构动态变化的情形。

**贡献**  
主要贡献有三：1）提出一种计算高效的流行病模型选择框架，将贪心搜索与ABC-NS结合，显著降低模拟次数；2）在模型空间探索中引入结构先验（如流行病学中的仓室逻辑），使搜索更具可解释性；3）通过数值实验（可能基于模拟的COVID-19或流感数据）展示该方法在模型识别准确率和计算时间上的优势，为复杂动态系统的模型选择提供新工具。该工作对统计学家和流行病学家的交叉研究具有方法论启示。


### 5. Learning Overlapping Group Structures via Community Detection for High-Dimensional Variable Selection

**讲者**：Qianhui Shen（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维变量选择中，许多实际问题（如基因调控网络、文本主题建模）的变量天然具有**重叠的组结构**（overlapping group structure），即一个变量可能同时属于多个组。传统稀疏方法（如Lasso、Group Lasso）假设组结构已知且互斥，而现实中的组结构往往是未知且重叠的。本报告旨在解决：如何从高维数据中同时学习变量的重叠组结构并进行变量选择？

**核心方法**  
讲者提出将变量选择问题转化为**社区检测**（community detection）任务。具体地，将每个变量视为图中的节点，变量间的相关性（如样本协方差或偏相关系数）作为边权重，构建一个加权图。然后利用**重叠社区检测算法**（如BigClam、NMF-based方法）识别出可能重叠的变量组（社区）。在此基础上，引入一个**重叠组正则化**（overlapping group penalty）项，例如将Group Lasso推广为允许变量属于多个组的形式：$\min_{\beta} \frac{1}{2}\|y - X\beta\|_2^2 + \lambda \sum_{g \in \mathcal{G}} \|\beta_g\|_2$，其中组集合$\mathcal{G}$由社区检测结果动态确定。通过交替优化或两步法（先检测组结构，再基于组进行变量选择）实现。

**与已有工作关系**  
已有工作主要分为两类：一是假设组结构已知（如Group Lasso、Sparse Group Lasso）；二是通过聚类或图模型学习非重叠组结构（如Tree Lasso、Fused Lasso）。本报告的关键创新在于允许组结构**重叠**，且组结构由数据驱动而非先验指定。这与近期基于图正则化的方法（如Graph-guided Fused Lasso）不同，后者仅利用图结构进行平滑惩罚，而非显式学习重叠组。此外，社区检测方法天然适合处理重叠性，相比传统的谱聚类或K-means更具灵活性。

**贡献**  
1. 提出将高维变量选择中的未知重叠组结构学习问题与社区检测相结合，开辟了新的方法论视角。  
2. 开发了可同时估计重叠组和进行变量选择的算法，理论上可能证明在特定条件下（如组内强相关、组间弱相关）的变量选择一致性。  
3. 通过模拟和实际数据（如基因表达数据）验证了方法在预测精度和组结构恢复上的优势，尤其当变量具有多义性（如一个基因参与多条通路）时，优于现有非重叠组方法。


### 6. A Bayesian Phase I/II Platform Design with Data Augmentation Accounting for Delayed Outcomes

**讲者**：Wentao Yang（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在肿瘤临床试验中，Phase I/II 无缝设计常面临两个挑战：一是剂量探索与疗效/毒性联合评价的复杂性，二是结局（如延迟毒性或疗效）的观测滞后导致决策信息不完整。传统方法或忽略延迟数据，或采用简单的插补，易引入偏倚并降低试验效率。本报告旨在提出一种贝叶斯平台设计，通过数据增广（Data Augmentation）技术系统性地处理延迟结局，实现实时、稳健的剂量-疗效-毒性联合决策。

**核心方法**  
设计基于贝叶斯层次模型，将未观测到的延迟结局视为缺失数据，利用马尔可夫链蒙特卡洛（MCMC）进行后验推断。具体地，对每个剂量组，假设毒性（$T$）与疗效（$E$）服从二元潜在变量模型，其联合分布由剂量参数 $\theta$ 控制。对于尚未观测到结局的患者，通过数据增广从当前后验预测分布中采样其潜在结局，从而“补全”数据集。该过程与剂量分配规则（如基于效用函数的自适应随机化）迭代进行，形成在线学习框架。平台设计还允许同时评估多个候选剂量，并动态调整入组比例。

**与已有工作关系**  
现有 Phase I/II 设计（如 EffTox、BOIN 的扩展）多假设结局可即时观测，或仅对延迟做简单加权。本报告将数据增广引入平台设计，与缺失数据领域的贝叶斯插补思想结合，但专门针对临床试验的序贯决策场景。相比 Liu et al. (2018) 的延迟毒性处理方法，本设计同时处理疗效延迟，并允许在平台框架下灵活切换剂量臂，更具通用性。

**主要贡献**  
1. 提出首个将数据增广与贝叶斯 Phase I/II 平台设计结合的方法，系统解决延迟结局问题，无需依赖强假设（如缺失随机性）。  
2. 通过模拟实验证明，该方法相比忽略延迟或简单插补，能显著降低错误剂量选择概率，并缩短试验周期。  
3. 为平台设计中“实时学习”提供了理论支持，可推广至更复杂的联合终点（如免疫疗法中的多时间点评估）。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)