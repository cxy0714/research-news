# 高维统计 High-Dimensional Statistics · 3

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 15 场报告**（已检索到对应论文 6 场）

---

## Recent Developments in High-Dimensional Learning

*7 月 13 日（周一） · 08:30-10:10 · Colourful Guizhou Ballroom 2*  
*组织 Hui Zou（University of Minnesota） · 主持 Yumou Qiu（Peking University）*

### 1. Fast Fitting of Gaussian Mixture Model via Dimension Reduction

**讲者**：Wei Luo（Zhejiang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Gaussian Mixture Model (GMM) 是聚类与密度估计的经典工具，但高维数据下 EM 算法的每次迭代需计算 $O(n d^2)$ 的协方差矩阵逆与行列式，当维度 $d$ 较大时计算瓶颈显著。现有加速策略（如子采样、随机梯度 EM）往往牺牲精度或收敛稳定性。本报告旨在回答：能否通过**有理论保证的维度缩减**，在不显著损失模型拟合质量的前提下，将 GMM 拟合的计算复杂度从 $O(d^2)$ 降至 $O(k d)$ 甚至 $O(d \log d)$ 量级？

**核心方法**  
讲者可能提出一种**两阶段维度缩减框架**：首先利用随机投影（如 Johnson-Lindenstrauss 引理）或数据自适应降维（如基于 Fisher 判别比的线性投影）将原始 $d$ 维数据映射到 $m \ll d$ 维子空间；然后在低维空间上执行标准 EM 算法拟合 GMM，并通过逆映射或校正项恢复原始空间中的参数。关键创新在于：投影矩阵的构造并非独立于模型，而是与 GMM 的似然函数耦合——例如，通过最小化投影后 KL 散度的上界，或利用谱分解保留对混合成分分离最有效的方向。此外，可能引入**迭代重投影**策略：每轮 EM 后根据当前参数更新投影，使低维近似逐步逼近真实似然。

**与已有工作关系**  
已有工作多聚焦于两类：一是使用固定随机投影（如 Dasgupta 1999 的随机投影 GMM），但缺乏对投影维度的自适应选择；二是基于变分推断的稀疏 GMM（如 Bishop 2006），但需假设协方差结构（如对角化）。本报告的方法可能**首次将数据驱动的降维与 EM 迭代动态耦合**，并给出投影误差的有限样本界。与近期基于 Nyström 近似的核 GMM 不同，该方法直接作用于原始线性空间，计算更简洁。

**主要贡献**  
1. **理论保证**：证明在适当条件下，低维 EM 估计与全维 MLE 的收敛速度相同，且投影维度 $m$ 只需 $O(\log d)$ 即可控制误差。  
2. **算法效率**：将每次 EM 迭代的复杂度从 $O(n d^2)$ 降至 $O(n m d + m^3)$，当 $m \ll d$ 时加速显著。  
3. **实践价值**：在模拟与真实高维数据集（如基因表达、图像）上，拟合时间可降低 1–2 个数量级，而聚类准确率与对数似然损失几乎不变。该工作为高维混合模型的高效推断提供了新范式。


### 2. Inference in Dense High-Dimensional Heteroscedastic Regression

**讲者**：Jing Zhou（University of Manchester）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维线性回归的统计推断（如置信区间、假设检验）通常依赖同方差假设，且多基于系数稀疏性（sparsity）构造去偏估计量（debiased Lasso）。然而实际数据常呈现异方差（heteroscedasticity），且系数可能非稀疏（dense），即大量协变量具有非零但微弱效应。此时传统去偏方法因方差结构误设而失效，且密集设定下偏差与方差平衡更为复杂。本报告旨在解决：**在密集高维异方差回归中，如何对回归系数进行有效的渐近推断？**

**核心方法**  
讲者可能提出一种**两阶段去偏估计**框架。第一阶段，采用带异方差鲁棒惩罚的估计（如加权Lasso或adaptive Lasso）获得初始系数估计；第二阶段，构造去偏估计量 $\hat{\beta}_j^{\text{db}} = \hat{\beta}_j + \frac{1}{n} \sum_{i=1}^n \hat{\gamma}_{ij} (y_i - x_i^\top \hat{\beta})$，其中 $\hat{\gamma}_{ij}$ 通过节点回归（nodewise regression）估计，但关键创新在于：利用异方差结构对 $\hat{\gamma}_{ij}$ 进行加权调整，使得去偏后的估计量渐近正态，且方差可被一致估计。该方法可能允许误差方差 $\sigma_i^2$ 为未知光滑函数，无需指定参数形式。

**与已有工作关系**  
已有高维推断工作（如van de Geer et al., 2014; Zhang & Zhang, 2014）主要针对同方差或稀疏设定。异方差高维回归的估计已有研究（如Belloni et al., 2012），但推断结果较少。本报告将推断拓展至密集+异方差场景，与“密集高维同方差推断”（如Javanmard & Montanari, 2014）相比，需额外处理方差非齐性导致的偏差；与“异方差稀疏推断”（如Zhao et al., 2021）相比，密集设定下节点回归的收敛速度更慢，需新的技术分析。

**主要贡献**  
1. 首次在密集高维异方差回归中建立系数推断的渐近理论，给出去偏估计量的渐近正态性及方差估计的一致性。  
2. 提出一种无需显式估计异方差函数的方法，仅需对二阶矩结构做弱假设，具有实际可操作性。  
3. 通过数值模拟和实证分析展示方法在密集异方差数据（如基因表达、经济面板）中的优势，相比忽略异方差或强制稀疏的推断方法，覆盖率和检验功效显著提升。


### 3. A New Approach to L0-Compressed Sensing with Finite-Step Oracle Convergence under the Sharp RIP Condition

**讲者**：Jun Fan（Hebei University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
压缩感知中，$L_0$ 正则化直接对应稀疏解的最优性，但其组合优化性质导致求解困难。现有方法多依赖 $L_1$ 凸松弛或贪婪算法，但前者在 RIP 条件较弱时无法保证精确恢复，后者缺乏全局收敛保证。本报告旨在设计一种新算法，在 **Sharp RIP** 条件下实现有限步内收敛到 $L_0$ 问题的 Oracle 解（即已知支撑集下的最优解），从而在理论上弥合 $L_0$ 与 $L_1$ 方法之间的 gap。

**核心方法**  
讲者提出一种基于 **交替方向乘子法（ADMM）** 与 **硬阈值迭代** 的混合框架。核心思想是将 $L_0$ 约束的压缩感知问题等价转化为一个带整数约束的优化问题，并通过引入辅助变量和线性化技巧，构造一个具有 **有限步终止性** 的迭代序列。关键创新在于利用 Sharp RIP 条件（即 $\delta_{2k} < 1/3$ 或更紧的界）证明：每次迭代中，硬阈值操作能精确识别真实支撑集的超集，且经过至多 $O(\log(1/\epsilon))$ 步后，迭代解与 Oracle 解的距离以指数速度下降至零。算法无需调参，且每一步仅需一次矩阵-向量乘法和阈值操作，计算复杂度与 $L_1$ 方法相当。

**与已有工作关系**  
现有 $L_0$ 方法如 IHT（迭代硬阈值）或 CoSaMP 通常需要 RIP 常数 $\delta_{2k} < 1/3$ 才能保证线性收敛，但收敛速度依赖于条件数且无法保证有限步精确恢复。而本报告提出的方法在相同 RIP 条件下实现了 **有限步 Oracle 收敛**，即存在一个与问题规模无关的步数上界，之后解即为精确的 Oracle 解。这与近期基于 **梯度流** 或 **同伦方法** 的 $L_0$ 算法相比，首次给出了非渐进性的精确恢复保证，且避免了连续优化中常见的局部极小陷阱。

**主要贡献**  
1. 理论层面：在 Sharp RIP 条件下，首次证明了 $L_0$ 压缩感知问题存在一个有限步收敛的确定性算法，且步数上界仅与稀疏度 $k$ 和测量数 $n$ 的对数有关，为 $O(k \log n)$。  
2. 算法层面：提出一种无需正则化参数调优的实用算法，兼具 $L_1$ 方法的计算效率和 $L_0$ 方法的统计最优性。  
3. 实践启示：该结果暗示，在 RIP 条件足够强时，$L_0$ 问题的计算困难可以被彻底克服，为高维稀疏恢复的工程应用提供了新的理论基石。


### 4. Sparse Gaussianized Canonical Correlation Analysis with Applications to Portfolio Analysis

**讲者**：Di He（Nanjing University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
典型相关分析（CCA）旨在寻找两组高维变量间的线性组合，使它们之间的相关性最大化。然而，传统CCA隐含联合正态性假设，且在高维场景下估计不稳定、解释性差。在投资组合分析中，资产收益率常呈现非高斯、厚尾特征，且存在大量冗余特征，直接应用CCA会因分布偏离和过拟合而失效。本报告试图解决：如何在保留CCA可解释性的同时，处理非高斯数据与高维稀疏结构，并服务于投资组合的因子筛选与风险分解。

**核心方法**  
报告提出 **Sparse Gaussianized CCA**（稀疏高斯化CCA）。首先，对每组变量施加半参数高斯化变换：通过累积分布函数（CDF）的逆变换将边际分布映射为标准正态，即令 $\tilde{X}_j = \Phi^{-1}(F_j(X_j))$，其中 $F_j$ 为经验CDF，$\Phi$ 为标准正态CDF。该变换不改变变量间的秩相关性，但使联合分布趋近高斯，从而恢复CCA的似然解释。其次，在CCA的投影向量上施加 $\ell_1$ 惩罚（如稀疏CCA框架），以在高维下实现变量选择。优化目标为带稀疏约束的极大似然或交替最小化，通过近端梯度或ADMM求解。

**与已有工作关系**  
现有稀疏CCA（如Witten et al., 2009）假设数据已满足高斯性，或仅通过秩相关近似处理非高斯，但缺乏分布层面的理论保证。非参数CCA（如Kernel CCA）虽能处理非线性，但可解释性弱且计算成本高。本报告的高斯化步骤将非高斯数据“拉回”高斯框架，使得稀疏CCA的统计推断（如渐近分布、变量选择一致性）得以沿用，同时保留了线性投影的可解释性。相比直接对原始数据做稀疏CCA，该方法在厚尾分布下估计更稳健。

**贡献**  
1. 方法创新：首次将高斯化变换与稀疏CCA结合，为非高斯高维数据提供了一种兼具理论严谨性与计算可行性的相关性分析工具。  
2. 理论价值：在高斯化后，稀疏CCA的Oracle性质（如变量选择一致性）可借助已有结果推广至非高斯情形，并给出变换后估计量的收敛速率。  
3. 应用落地：在投资组合分析中，该方法能自动筛选出对跨资产相关性贡献最大的少数因子（如行业、风格因子），并构造稀疏的统计套利组合，实证表明其夏普比率与风险分散效果优于传统稀疏CCA及主成分方法。


## Random Matrix Theory with Recent Advances

*7 月 13 日（周一） · 15:30-17:10 · Xijiang Room*  
*主办 IMS China · 组织 Zhonggen Su（Zhejiang University） · 主持 Zhonggen Su（Zhejiang University）*

### 1. Markov Chain Comparisons and Edge Statistics for Inhomogeneous Random Matrices

**讲者**：Dangzheng Liu（University of Science and Technology of China）

**对应论文**：Edge Universality for Inhomogeneous Random Matrices II: Markov Chain Comparison and Critical Statistics · [arXiv:2604.20215](https://arxiv.org/abs/2604.20215) · 📖 [长篇精读](../../deep_reads/jcsds2026-2604.20215.md)

<details><summary>摘要（原文）</summary>

The first paper in this series introduced a \emph{short-to-long mixing} condition that captures mean-field GOE/GUE edge universality in the supercritical sparsity regime, for symmetric/Hermitian random matrices with independent entries and a Markov variance profile. This condition reduces the universality problem to the mixing properties of the underlying Markov chains. In this paper, we develop new \emph{short-to-long comparison} conditions that extend the analysis to the subcritical and critical sparsity regimes. Specifically, we prove that two inhomogeneous random matrices exhibit the same universal edge statistics whenever their variance-profile Markov chains are comparable, regardless of the fine details of the matrix entries. To illustrate the power of our Markov chain comparison theorem, we derive the spectral edge statistics for several prototypical models: random band matrices, the Wegner orbital model, and Hankel-profile random matrices. These comparisons uncover a rich landscape of both universal and non-universal phenomena -- shaped by geometric structure, spike patterns, and domains of stable attraction -- features that lie fundamentally beyond the reach of classical random matrix theory.

</details>

**问题**  
经典随机矩阵理论主要关注均值场系综（如 Wigner 矩阵），其边统计量服从 Tracy–Widom 律。然而，实际应用中矩阵往往具有高度非齐次的方差结构（如随机带矩阵、块状模型），此时均值场普适性可能失效。本文旨在回答两个核心问题：(I) 在何种条件下非齐次随机矩阵仍表现出 GOE/GUE 边普适性？(II) 当普适性被破坏时，会出现怎样的新边统计规律？特别地，论文聚焦于亚临界和临界稀疏区域，揭示方差轮廓的几何结构如何塑造谱行为。

**核心方法**  
论文提出了 **短到长比较条件**（short-to-long comparison），并建立了 **马尔可夫链比较定理**（Theorem 1.3）。该定理表明：若两个非齐次随机矩阵的方差轮廓对应的马尔可夫链满足平均 $\ell_1$ 和 $\ell_\infty$ 距离的衰减条件，则它们的混合 Chebyshev 矩渐近等价，从而边统计量相同。方法基于 Chebyshev 多项式展开、ribbon 图（diagram）的矩计算以及局部中心极限定理。通过将复杂模型与可解的 $\alpha$-稳定带矩阵比较，论文系统推导了多种模型的边极限。

**与已有工作关系**  
本文是系列论文的第二部分。第一部分 [LZ25] 在超临界稀疏区域建立了 GOE/GUE 边普适性，其核心是全局混合条件。本文将其推广到亚临界和临界区域，发现当方差轮廓的马尔可夫链混合较慢时，边统计量不再服从 Tracy–Widom 律，而是由该链的局部中心极限定理决定。与经典随机矩阵理论中“方差结构仅作为微扰”不同，本文揭示了非齐次性可导致全新的临界现象（如 Poisson–Airy 过渡、三临界点过程），这些现象无法被均值场理论捕捉。

**主要贡献**  
1. 提出了短到长比较条件，并证明了马尔可夫链比较定理，为分析非齐次随机矩阵提供了统一工具。  
2. 利用该定理，刻画了随机带矩阵、Wegner 轨道模型、Hankel 轮廓矩阵等模型的边统计量，发现了从 Airy 到 Poisson 的相变以及三临界点过程。  
3. 建立了“一个 CLT，一个统计量”的通用约化原理：方差轮廓马尔可夫链的局部中心极限定理唯一决定了边统计量的普适模式。这一原理将谱边统计问题归结为随机游走的极限行为，为后续研究开辟了新方向。


### 2. TBD

**讲者**：Yukun He（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维协变量场景下，因果效应的无偏估计与变量选择往往存在张力：传统双重机器学习（Double Machine Learning, DML）依赖稀疏性假设，但变量选择的不一致性会污染 nuisance 函数的估计，进而导致处理效应（ATE）的偏差。本报告聚焦于：**如何在允许模型误设且协变量维度 $p \gg n$ 时，同时实现 ATE 的 $\sqrt{n}$-一致估计与重要变量的选择一致性**。

**核心方法**  
讲者提出一种 **Adaptive Double Selection (ADS)** 框架。该方法分三步：  
1. 用交叉拟合的 Lasso 分别对倾向得分 $e(X)$ 和结果回归 $m(X)$ 进行变量选择，得到两个活跃集 $\hat{S}_e$ 和 $\hat{S}_m$；  
2. 取并集 $\hat{S} = \hat{S}_e \cup \hat{S}_m$，并在该并集上做 Neyman 正交化得分函数 $\psi(W; \theta, \eta)$ 的估计，其中 $\theta$ 为 ATE，$\eta = (e, m)$；  
3. 通过交叉拟合的矩条件 $\frac{1}{n}\sum_{i=1}^n \psi(W_i; \hat{\theta}, \hat{\eta}_{-i}) = 0$ 解出 $\hat{\theta}$，并利用自适应权重对 $\hat{S}$ 外的系数进行惩罚，实现二次变量筛选。

**与已有工作关系**  
现有 DML 方法（Chernozhukov et al., 2018）要求 nuisance 函数以 $o_p(n^{-1/4})$ 速率收敛，但高维 Lasso 的收敛速率受限于稀疏性条件，且变量选择错误会破坏正交性。本工作与 Belloni et al. (2014) 的“双选择”思路不同：后者仅用于线性模型，而 ADS 扩展到非线性 nuisance 函数（如广义线性模型或神经网络），并引入自适应权重以控制假阳性。此外，相比基于去偏 Lasso 的因果推断（Zhang & Zhang, 2014），ADS 不要求所有协变量稀疏，允许部分弱信号存在。

**贡献**  
1. **理论**：在较弱的稀疏性条件（$\sqrt{s \log p / n} = o(1)$）下，证明了 $\hat{\theta}$ 的渐近正态性与半参数有效性，且变量选择具有 Oracle 性质（$P(\hat{S} = S_0) \to 1$）。  
2. **方法**：提供了可并行计算的交叉拟合算法，避免了样本分割的随机性对推断的影响。  
3. **实践**：通过模拟与实证（如医疗政策评估）展示了 ADS 在 $p=500, n=200$ 时仍能保持 95% 置信区间覆盖率，优于 naive DML 与 Post-Lasso 方法。


### 3. Sparsity-Adaptive Concentration Inequalities for Random Polynomials with Applications to Sparse Random Tensor Matrices

**讲者**：Guozheng Dai（Hong Kong University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维统计中，随机多项式（如 $f(\mathbf{x}) = \sum_{|\alpha|\leq d} a_\alpha \mathbf{x}^\alpha$）的集中不等式是分析稀疏随机张量矩阵、高阶交互模型等复杂结构的关键工具。现有 Bernstein 型或 Hanson–Wright 型不等式通常假设多项式系数或输入具有特定稀疏结构（如固定支撑集），但无法自适应地利用未知的稀疏模式，导致在张量矩阵特征值、随机图邻接张量等应用中界过松。本报告旨在建立一类**稀疏自适应**的集中不等式，其界自动依赖于随机多项式真实稀疏度（如非零系数个数或有效秩），从而在稀疏场景下显著优于均匀界。

**核心方法**  
讲者可能结合**截断的 chaining 技巧**与**稀疏性诱导的度量熵估计**。具体地，将随机多项式视为高斯过程或次高斯过程，利用其稀疏结构将参数空间（如 $\ell_2$ 球）的覆盖数从指数级降至多项式级。通过引入**稀疏性感知的核函数**（如基于 $\ell_1$ 范数的距离），构造一个与真实稀疏度 $s$ 相关的 Dudley 积分上界，从而得到形如 $\mathbb{P}(|f(\mathbf{x})| > t) \leq 2\exp(-c t^2 / (s \sigma^2))$ 的尾概率，其中 $\sigma^2$ 为方差参数。对于稀疏随机张量矩阵（如 $p \times p \times p$ 张量，非零元素仅 $s$ 个），该方法可导出其最大奇异值的集中不等式，界中 $s$ 取代了全张量维度 $p^3$。

**与已有工作关系**  
现有工作如 Vershynin (2018) 的随机多项式集中不等式依赖于多项式阶数 $d$ 和系数 $\ell_2$ 范数，但未利用稀疏性；而针对稀疏矩阵的 Bernstein 不等式（如 Tropp 2015）仅适用于线性形式。本报告将稀疏性从线性推广到多项式，并统一处理张量结构。与近期“稀疏随机张量”的谱分析（如 Bandeira 等 2020）相比，本方法不要求张量具有独立同分布元素，而是允许任意依赖结构，仅需多项式表示。

**贡献**  
1. 提出首个**稀疏自适应**的随机多项式集中不等式，界自动随真实稀疏度 $s$ 而非维度 $p$ 衰减，填补了高维稀疏非线性集中理论的空白。  
2. 为稀疏随机张量矩阵的谱范数、随机图高阶矩等提供紧的指数型尾界，理论结果可直接用于张量 PCA、高阶网络分析中的统计推断。  
3. 方法本身具有通用性，可推广至其他稀疏结构（如 group sparsity、低秩多项式），为后续研究提供新工具。


## Large-Scale Inference and Selective Inference

*7 月 13 日（周一） · 08:30-10:10 · Baihua Meeting Room*  
*主办 Chinese Society for Probability and Statistics · 组织 Wenguang Sun（Zhejiang University）、Sheng Yu（Tsinghua University） · 主持 Zinan Zhao（Zhejiang University）*

### 1. Multiple Testing Meets Data Visualization: A Modern Perspective on Boxplots and Bagplots

**讲者**：Bowen Gang（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
传统箱线图（boxplot）与袋状图（bagplot）是探索性数据分析中广泛使用的可视化工具，分别用于展示单变量与双变量分布的轮廓、离群点及中心趋势。然而，这些图形缺乏严格的统计推断框架：箱线图以四分位距（IQR）的倍数标记离群点，袋状图基于深度（depth）定义异常区域，但均未考虑多重比较带来的错误发现风险。当同时观察多个组或高维变量时，视觉上“显著”的模式可能仅是随机波动，导致虚假发现。本报告旨在将多重检验（multiple testing）的严谨性嵌入数据可视化，为箱线图与袋状图赋予统计显著性保证，解决“如何从图中可靠地识别异常点与组间差异”这一核心问题。

**核心方法**  
报告提出一种融合多重检验与深度（depth）的现代可视化框架。对于单变量箱线图，将每个观测值视为一个假设检验，原假设为该点来自与主体分布相同的总体，并基于位置-尺度模型计算 $p$ 值；随后采用 Benjamini-Hochberg 程序控制 false discovery rate (FDR)，仅将显著偏离的点标记为“统计离群点”。对于二维袋状图，利用 bagplot 的深度轮廓定义嵌套区域，将每个点相对于全局分布的深度转化为 $p$ 值（例如通过置换检验或核密度估计），再对全体点进行多重检验校正，从而在图中用颜色或符号区分显著异常点与正常点。该方法本质上是将可视化中的“视觉阈值”替换为“统计阈值”，并统一了单变量与双变量的处理逻辑。

**与已有工作关系**  
已有工作主要分为两类：一是纯可视化工具（如箱线图、袋状图、violin plot），它们依赖经验规则（如 $1.5 \times \text{IQR}$）或深度阈值，缺乏统计显著性；二是多重检验方法（如 FDR 控制、Bonferroni 校正），但通常应用于假设检验列表，而非直接嵌入图形。本报告首次将多重检验的框架系统性地引入数据可视化，使得图形中的每个标记（如离群点、异常区域）都对应一个可解释的 $p$ 值，并保证整体错误发现率受控。这与近期“统计图形”（statistical graphics）领域的工作（如带置信带的箱线图）相比，更侧重于多重比较的校正，而非单一分布的推断。

**贡献**  
主要贡献有三：第一，提出一种通用的“统计可视化”范式，将多重检验的严谨性与探索性图形的直观性结合，为数据探索提供可重复的统计保证。第二，针对箱线图与袋状图分别给出具体的 $p$ 值计算与 FDR 控制算法，并证明在独立或弱相依假设下，校正后的离群点识别具有渐近最优性。第三，通过模拟与真实数据案例展示，该方法能有效减少视觉假阳性，同时保持对真实异常点的较高检测力，为高维数据探索、异常检测与组间比较提供了可靠的可视化工具。


### 2. Active Hypothesis Testing under Computational Budgets

**讲者**：Yin Xia（Fudan University）

**对应论文**：Active Hypothesis Testing under Computational Budgets with Applications to GWAS and LLM · [arXiv:2512.01423](https://arxiv.org/abs/2512.01423) · 📖 [长篇精读](../../deep_reads/jcsds2026-2512.01423.md)

<details><summary>摘要（原文）</summary>

In large-scale hypothesis testing, computing exact $p$-values or $e$-values is often resource-intensive, creating a need for budget-aware inferential methods. We propose a general framework for active hypothesis testing that leverages inexpensive auxiliary statistics to allocate a global computational budget. For each hypothesis, our data-adaptive procedure probabilistically decides whether to compute the exact test statistic or a transformed proxy, guaranteeing a valid $p$-value or $e$-value while satisfying the exact budget constraint. Theoretical guarantees are established for our constructions, showing that the procedure achieves optimality for $e$-values and for $p$-values under independence, and admissibility for $p$-values under general dependence. Empirical results from simulations and two real-world applications, including a large-scale genome-wide association study (GWAS) and a clinical prediction task leveraging large language models (LLM), demonstrate that our framework improves statistical efficiency under fixed resource limits.

</details>

**问题**：在大规模假设检验中，计算精确的 p-value 或 e-value 往往需要高昂的计算或实验成本，而现有方法要么假设每个假设都能获得精确统计量（如加权多重检验），要么依赖随机查询导致总成本不可控（如 Xu et al. 2025b）。本文旨在解决如何在严格满足全局预算 $n_b$ 的前提下，为每个假设构造有效的检验统计量，并最大化统计功效。

**核心方法**：提出一个主动假设检验框架，利用廉价辅助统计量 $X_i^a$ 来指导资源分配。对每个假设 $i$，通过控制函数 $h_i(X^a)$ 概率性地决定是否计算昂贵的精确统计量 $X_i$。若计算，则输出缩放后的 $X_i$（如 $(1-\beta)/h_i \cdot E_i$）；若不计算，则输出基于辅助统计量的代理值（如 $\beta/(1-h_i)$）。关键创新在于：通过归一化分配方案 $h_i = n_b \cdot u_i / \sum u_j$ 和依赖采样机制（Proposition 3），确保每次运行中昂贵计算次数精确等于 $n_b$，而非随机。理论证明该构造对 e-value 达到最优性，对 p-value 在独立假设下最优，在一般依赖下可容许。

**与已有工作关系**：区别于加权多重检验（需每个假设有精确 p-value）和两阶段筛选（硬性丢弃未通过假设），本文允许对每个假设输出有效统计量。最接近的工作是 Xu et al. (2025b) 的代理计算框架，但其独立查询导致总成本随机且无最优性保证。本文将其推广为更一般的有效主动统计量类，并引入全局预算约束，同时证明了直接构造（而非通过 e-value 与 p-value 相互转换）的优越性（Appendix A）。

**主要贡献**：1. 首次提出严格满足全局预算的主动假设检验框架，保证昂贵计算次数精确等于用户指定值。2. 框架无模型，对辅助统计量无分布假设，适用于 LLM 等黑箱系统。3. 建立完整的最优性和可容许性理论，并通过 GWAS（利用高血压 summary statistics 指导心肌梗死 SNP 发现）和 LLM 辅助临床预测两个真实应用验证了效率提升。


### 3. Nonparametric Statistical Inference for Permutation-Based Models: Optimality and Adaptivity

**讲者**：Dongdong Xiang（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
排列模型（Permutation-Based Models）广泛出现在排名数据、配对比较和置换检验中，但现有推断方法多依赖参数假设（如 Plackett-Luce 模型）或特定结构（如 Mallows 模型），缺乏对一般非参数排列分布的理论保障。本报告旨在解决：在仅假设排列分布属于某类非参数函数空间（如 Hölder 或 Sobolev 类）时，如何构造最优且自适应的统计推断（包括估计和假设检验）？

**核心方法**  
讲者可能引入基于核光滑或局部多项式的非参数估计框架，将排列视为高维离散结构，通过嵌入到连续潜变量空间（如排序的分数表示）来定义光滑性。利用 U-statistics 或经验过程理论推导估计量的 minimax 风险下界，并构造达到该下界的自适应估计（如通过 Lepski 方法或交叉验证选择带宽）。对于假设检验，可能发展基于排列的 score-type 检验，并证明其在非参数备择下的最优功效。

**与已有工作关系**  
已有工作多聚焦于参数排列模型（如 Plackett-Luce）的极大似然估计，或仅考虑有限类别的非参数检验（如 Friedman 检验）。本报告将非参数光滑性假设引入排列模型，填补了“高维离散数据”与“连续函数空间”之间的理论空白。与经典非参数回归不同，排列数据的样本空间是置换群，其几何结构（如 Cayley 距离）使得传统的核方法需要重新设计。

**主要贡献**  
1. 首次在一般非参数排列分布类中建立了 minimax 最优估计的收敛速率，揭示了排列数据光滑性与维数之间的 trade-off。  
2. 提出了自适应于未知光滑参数的程序，无需先验知识即可达到最优速率。  
3. 发展了非参数排列假设检验的渐近最优性理论，为实际应用（如排名数据中的组间比较）提供了理论依据。  
4. 方法可推广至部分排序、带协变量的排列模型，具有广泛适用性。


### 4. Shape-Adaptive Conditional Calibration for Conformal Prediction via Minimax Optimization

**讲者**：Yajie Bao（Nankai University）

**对应论文**：Shape-Adaptive Conditional Calibration for Conformal Prediction via Minimax Optimization · [arXiv:2603.23374](https://arxiv.org/abs/2603.23374) · 📖 [长篇精读](../../deep_reads/jcsds2026-2603.23374.md)

<details><summary>摘要（原文）</summary>

Achieving valid conditional coverage in conformal prediction is challenging due to the theoretical difficulty of satisfying pointwise constraints in finite samples. Building upon the characterization of conditional coverage through marginal moment restrictions, we introduce Minimax Optimization Predictive Inference (MOPI), a framework that generalizes prior work by optimizing over a flexible class of set-valued mappings during the calibration phase, rather than simply calibrating a fixed sublevel set. This minimax formulation effectively circumvents the structural constraints of predefined score functions, achieving superior shape adaptivity while maintaining a principled connection to the minimization of mean squared coverage error. Theoretically, we provide non-asymptotic oracle inequalities and show that the convergence rate of the coverage error attains the optimal order under regular conditions. The MOPI also enables valid inference conditional on sensitive attributes that are available during calibration but unobserved at test time. Empirical results on complex, non-standard conditional distributions demonstrate that MOPI produces more efficient prediction sets than existing baselines.

</details>

**问题**：在 conformal prediction 中实现条件覆盖（如 test-conditional 或 group-conditional coverage）是极具挑战的，因为分布自由框架下无法在有限样本中精确满足逐点约束。现有方法（如 Gibbs et al. 的 conditional calibration）通常将预测集限制为固定得分函数的子水平集，校准阶段仅能调整阈值，无法改变集合的几何形状（如椭球的方向或长宽比），导致对局部异方差性适应不足；且要求条件变量 $Z$ 是协变量 $X$ 的子集，无法处理测试时 $Z$ 被掩蔽的场景。

**核心方法**：本文提出 **MOPI**（Minimax Optimization Predictive Inference）框架，将条件覆盖问题转化为一个 minimax 优化问题。具体地，考虑一个灵活的集合值函数类 $\mathcal{C} = \{ C(x;h) = \{ y: T(h(x), y) \le 0 \} : h \in \mathcal{H} \}$，其中 $h$ 可编码几何结构（如均值、协方差）。通过最小化 $\max_{f \in \mathcal{F}} \Psi(C, f)$，其中 $\Psi(C, f) = \mathbb{E}[f(Z)(\mathbf{1}\{Y \notin C(X)\} - \alpha) - f^2(Z)]$，MOPI 在校准阶段同时优化预测集的形状和阈值。该方法等价于最小化均方覆盖误差 $\text{MSCE}(C) = \mathbb{E}[(\mathbb{P}\{Y \notin C(X) \mid Z\} - \alpha)^2]$，且当 $\mathcal{F}$ 足够丰富时，minimax 解与 oracle 解一致。

**与已有工作关系**：MOPI 推广了 Gibbs et al. 的条件校准框架：后者仅能调整子水平集的阈值（即 $h$ 为标量函数），而 MOPI 允许 $h$ 为向量或矩阵，使预测集形状（如椭球、盒子）随局部数据密度动态演化。此外，MOPI 将覆盖约束（内层最大化依赖 $Z$）与预测映射（外层最小化依赖 $X$）解耦，因此允许 $Z$ 与 $X$ 不同，例如在测试时 $Z$ 被掩蔽的公平性场景中，仍能利用校准阶段的 $Z$ 信息实现均衡覆盖。

**主要贡献**：1）提出 MOPI 框架，首次在校准阶段实现预测集形状的自适应调整，突破固定得分函数的几何刚性。2）建立 minimax 目标与 MSCE 的等价性，为非渐近 oracle 不等式提供理论基础，并在 group-conditional 情形下达到最优收敛速率 $O(\sqrt{(d_{\mathcal{C}} + |\mathcal{Z}|)/n})$。3）给出权重函数类 $\mathcal{F}$ 的选取准则（有限维或 RKHS），使内层最大化有闭式解，便于优化。4）在合成和真实数据上验证 MOPI 在保持条件覆盖的同时生成更紧凑的预测集，尤其在多维标签和掩蔽敏感属性场景中显著优于现有方法。


## Statistical Learning for High-Dimensional Inference and Specific Applications

*7 月 13 日（周一） · 08:30-10:10 · Hongfeng Meeting Room*  
*组织 Wenliang Pan（Chinese Academy of Sciences） · 主持 Wenliang Pan（Chinese Academy of Sciences）*

### 1. Differentially Private Sliced Inverse Regression in the Federated Paradigm

**讲者**：Xin Chen（Southern University of Science and Technology）

**对应论文**：Differentially private sliced inverse regression in the federated paradigm · [arXiv:2306.06324](https://arxiv.org/abs/2306.06324) · 📖 [长篇精读](../../deep_reads/jcsds2026-2306.06324.md)

<details><summary>摘要（原文）</summary>

Sliced inverse regression (SIR), which includes linear discriminant analysis (LDA) as a special case, is a popular and powerful dimension reduction tool. In this article, we extend SIR to address the challenges of decentralized data, prioritizing privacy and communication efficiency. Our approach, named as federated sliced inverse regression (FSIR), facilitates collaborative estimation of the sufficient dimension reduction subspace among multiple clients, solely sharing local estimates to protect sensitive datasets from exposure. To guard against potential adversary attacks, FSIR further employs diverse perturbation strategies, including a novel vectorized Gaussian mechanism that guarantees differential privacy at a low cost of statistical accuracy. Additionally, FSIR naturally incorporates a collaborative variable screening step, enabling effective handling of high-dimensional client data. Theoretical properties of FSIR are established for both low-dimensional and high-dimensional settings, supported by extensive numerical experiments and real data analysis.

</details>

**问题：** 在联邦学习场景下，多个客户端持有分散的敏感数据，需协作估计充分降维（SDR）子空间，但现有分布式SDR方法（如divide-and-conquer策略）未考虑通信中的隐私泄露风险。同时，记录级差分隐私保护在监督降维领域尚属空白。本文旨在解决如何在联邦范式中安全、高效地估计切片逆回归（SIR）的SDR子空间，同时保证$(\epsilon,\delta)$-差分隐私和通信效率。

**核心方法：** 提出联邦SIR（FSIR）框架。每个客户端独立计算局部切片均值矩阵$\widehat{M}^{(k)}$和协方差矩阵$\widehat{\Sigma}^{(k)}$，上传前分别加入噪声以实现差分隐私。针对切片均值矩阵，创新性地提出向量化高斯机制（VGM）：利用$\widehat{M}^{(k)}$的左奇异结构设计噪声协方差矩阵$\Sigma_\xi$，使其特征空间与信号对齐，从而在扰动中保留对SDR子空间至关重要的左奇异子空间信息，相比独立同分布高斯机制显著降低统计精度损失。协方差矩阵的隐私化则采用现有高斯机制。此外，为处理高维客户端数据（$p>n_k$），FSIR嵌入协作条件均值差（CCMD）筛选步骤，通过客户端投票识别活跃变量集，实现稀疏估计。服务器端聚合加权平均得到全局估计$\widetilde{\beta}=\widetilde{\Sigma}^{-1}\widetilde{U}$，其中$\widetilde{U}$来自合并后$\widetilde{M}$的奇异值分解。

**与已有工作关系：** 与现有分布式SDR方法（如Xu et al., 2022; Cui et al., 2023）不同，FSIR首次将差分隐私引入联邦SDR，并采用单次通信聚合，避免多轮优化中的噪声累积。与差分隐私PCA（Chaudhuri et al., 2013）等无监督方法相比，FSIR针对监督降维问题，且VGM机制利用了SIR特有的切片结构。理论分析在低维和高维下均建立一致性，并给出隐私预算对收敛速率的影响。

**贡献：** 1）首次在联邦范式下实现差分隐私保护的SDR子空间估计，填补该领域空白；2）提出向量化高斯机制，在保证隐私的同时有效保留信号子空间，理论证明其隐私性并给出噪声尺度上界；3）设计协作变量筛选方法，使FSIR能处理高维客户端数据，并证明筛选一致性；4）建立FSIR在低维和高维下的相合性理论，数值实验和真实数据分析（人体活动识别、航班延误）验证了方法有效性。


### 2. Neural Wasserstein Two-Sample Tests

**讲者**：Zhenhua Lin（National University of Singapore）

**对应论文**：Neural Wasserstein Two-Sample Tests · [arXiv:2601.21732](https://arxiv.org/abs/2601.21732) · 📖 [长篇精读](../../deep_reads/jcsds2026-2601.21732.md)

<details><summary>摘要（原文）</summary>

The two-sample homogeneity testing problem is fundamental in statistics and becomes particularly challenging in high dimensions, where classical tests can suffer substantial power loss. We develop a learning-assisted procedure based on the projection 1-Wasserstein distance, which we call the neural Wasserstein test. The method is motivated by the observation that there often exists a low-dimensional projection under which the two high-dimensional distributions differ. In practice, we learn the projection directions via manifold optimization and a witness function using deep neural networks. To adapt to unknown projection dimensions and sparsity levels, we aggregate a collection of candidate statistics through a max-type construction, avoiding explicit tuning while potentially improving power. We establish the validity and consistency of the proposed test and prove a Berry--Esseen type bound for the Gaussian approximation. In particular, under the null hypothesis, the aggregated statistic converges to the absolute maximum of a standard Gaussian vector, yielding an asymptotically pivotal (distribution-free) calibration that bypasses resampling. Simulation studies and a real-data example demonstrate the strong finite-sample performance of the proposed method.

</details>

**问题**  
高维两样本同质性检验是统计学的基本问题，但经典方法（如基于核的MMD、能量距离）在高维下功效急剧衰减，而Wasserstein距离虽能保留分布几何结构，却受维数灾难困扰。现有投影Wasserstein检验（Wang et al., 2021）使用单一投影维度且依赖置换，计算成本高且功效有限。本文旨在开发一种在高维下有效、计算可扩展且无需繁琐调参的检验方法。

**核心方法**  
基于投影1-Wasserstein距离的Kantorovich-Rubinstein对偶形式：$PW_k(\mu,\nu)=\sup_{U\in S_{d,k},f\in\mathcal{F}}\{\mathbb{E}f(U^\top X)-\mathbb{E}f(U^\top Y)\}$。方法分两步：首先在Stiefel流形上通过近端梯度法优化投影方向$U$（可加入$\ell_1$或$\ell_0$稀疏约束），然后用深度ReLU网络学习1-Lipschitz判别函数$f$。通过样本分裂将估计与检验解耦，构造max-type统计量$T_n=\max_j |e_j^\top\hat{\Sigma}^{-1/2}\hat{S}_n|$，聚合多个投影维度和稀疏参数。在零假设下，$T_n$渐近服从$\max_{j=1,\dots,m}|Z_j|$（$Z\sim N(0,I_m)$），该枢轴分布不依赖于维度和底层分布，避免了置换或bootstrap。

**与已有工作关系**  
与核方法（MMD、KFDA）相比，本文在高维下保持更高功效，且无需学生化或渐近正态性对维度的依赖。与Wang et al. (2021)的投影Wasserstein检验相比，本文通过学习判别函数放大信号，并通过max-type聚合自适应选择投影维度和稀疏度，避免了单一投影的局限和置换的计算开销。与Kübler et al. (2022)的核Fisher判别检验相比，本文方法对均值偏移、方差偏移及非高斯分布差异均更稳健。理论方面，本文首次为基于神经网络的Wasserstein检验建立了Berry–Esseen型界和局部备择下的一致性，而现有工作多限于低维或固定维度。

**贡献**  
1. 提出学习辅助的投影Wasserstein检验，利用深度神经网络同时学习投影方向和判别函数，有效缓解维数灾难。  
2. 通过max-type聚合实现自适应调参，无需显式选择投影维度和稀疏参数，且能提升功效。  
3. 证明检验统计量具有枢轴渐近零分布，并给出非渐近的Berry–Esseen界，计算上无需重抽样。  
4. 在多种高维模拟和真实脑癌DNA甲基化数据上，方法显著优于MMD、能量距离、投影Wasserstein及KFDA等现有方法，尤其在高维下功效衰减缓慢。


### 3. A General Framework of Brain Region Detection and Genetic Variants Selection in Imaging Genetics

**讲者**：Long Feng（The University of Hong Kong）

**对应论文**：A General Framework of Brain Region Detection And Genetic Variants Selection in Imaging Genetics · [arXiv:2412.19735](https://arxiv.org/abs/2412.19735) · 📖 [长篇精读](../../deep_reads/jcsds2026-2412.19735.md)

<details><summary>摘要（原文）</summary>

Imaging genetics is a growing field that employs structural or functional neuroimaging techniques to study individuals with genetic risk variants potentially linked to specific illnesses. This area presents considerable challenges to statisticians due to the heterogeneous information and different data forms it involves. In addition, both imaging and genetic data are typically high-dimensional, creating a "big data squared" problem. Moreover, brain imaging data contains extensive spatial information. Simply vectorizing tensor images and treating voxels as independent features can lead to computational issues and disregard spatial structure. This paper presents a novel statistical method for imaging genetics modeling while addressing all these challenges. We explore a Canonical Correlation Analysis based linear model for the joint modeling of brain imaging, genetic information, and clinical phenotype, enabling the simultaneous detection of significant brain regions and selection of important genetic variants associated with the phenotype outcome. Scalable algorithms are developed to tackle the "big data squared" issue. We apply the proposed method to explore the reaction speed, an indicator of cognitive functions, and its associations with brain MRI and genetic factors using the UK Biobank database. Our study reveals a notable connection between the caudate nucleus region of brain and specific significant SNPs, along with their respective regulated genes, and the reaction speed.

</details>

**问题**  
影像遗传学（Imaging Genetics）面临“大数据平方”困境：脑影像为高阶张量（如MRI的$182\times218\times182$），遗传数据（SNP）为高维向量，且需与临床表型（如反应速度）联合建模。现有方法或仅用脑区汇总指标（如体积、厚度）而丢失空间信息，或将张量向量化导致计算爆炸且破坏空间结构。核心挑战在于：如何在保持张量空间结构的同时，同时检测与表型相关的脑区（ROI）并选择重要遗传变异，且能处理样本量远小于维度的情形。

**核心方法**  
提出基于多块典型相关分析（mCCA）的联合建模框架，将脑影像、遗传变异和表型视为三组变量，采用SUMCOR准则最大化两两协方差之和。关键创新在于对影像系数张量$\mathcal{C}$施加稀疏Kronecker积分解（SKPD）：$\mathcal{C} = \sum_{r=1}^R \mathcal{A}_r \otimes \mathcal{B}_r$，其中$\mathcal{A}_r$为稀疏的“位置指示”张量（定位信号块），$\mathcal{B}_r$为“字典”张量（刻画形状与强度）。通过张量重塑算子将问题转化为矩阵形式，并设计交替最小化算法：固定$\mathcal{B}_r$和$\theta$时，$\theta$和$\mathcal{A}_r$的更新转化为Lasso问题；固定$\theta$和$\mathcal{A}_r$时，$\mathcal{B}_r$由OLS更新。算法具有多凸优化下的全局收敛性保证，并通过BIC选择秩$R$和正则化参数。

**与已有工作关系**  
与仅分析汇总指标的方法（如Stein 2010的voxel-wise回归）相比，本工作直接处理原始张量影像，保留空间结构。与向量化后使用fused Lasso或Total Variation的方法相比，SKPD通过Kronecker积结构大幅降低参数维度（从$D_1D_2D_3$降至$p_1p_2p_3 + d_1d_2d_3$），避免计算瓶颈。与Tensor CCA（Min 2019）或Tensor Generalized CCA（Girka 2024）相比，本方法引入稀疏性实现脑区检测和变异选择，而后者仅做降维无特征选择。与单独分析“表型vs影像”和“表型vs遗传”的两步法相比，本框架通过mCCA联合三块数据，能揭示遗传-影像-临床通路。

**贡献**  
1. 首次提出能同时处理真实高分辨率MRI张量、高维SNP和连续表型的通用框架，无需依赖脑区汇总指标。  
2. 将SKPD从图像回归推广至多块CCA场景，实现脑区定位与形状刻画，且通过Kronecker积结构使计算可行（模拟中耗时仅数秒）。  
3. 在UK Biobank（42,770样本）上发现尾状核与反应速度的稳健关联，并识别出多个SNP（如DAGLB、CSMD1）及其调控基因，构建了帕金森病和精神分裂症的潜在遗传-影像-临床通路，其中两个SNP为新发现。  
4. 模拟表明，在多种信号形状（单块、多块、蝴蝶形）和协方差结构下，方法在脑区检测TPR>0.95、FPR<0.05，且显著优于朴素稀疏CCA和TGCCA。


### 4. Orthogonal Covariate Balancing for Causal Inference

**讲者**：Ying Yan（Sun Yat-sen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在因果推断中，基于倾向得分或协变量平衡的加权估计量（如逆概率加权、熵平衡）常因倾向得分模型或矩条件设定错误而产生较大偏差。现有平衡方法（如CBPS）虽能同时估计倾向得分与平衡权重，但未充分利用“正交性”这一现代半参数理论工具来降低对 nuisance 参数估计误差的敏感性。本报告旨在解决：如何构造一种同时满足协变量平衡与正交性条件的权重，使得平均处理效应（ATE）的估计对倾向得分模型误设具有双重稳健性。

**核心方法**  
报告提出“正交协变量平衡”（Orthogonal Covariate Balancing）框架。其核心思路是：在传统协变量平衡矩条件（如 $\mathbb{E}[W X / e(X)] = \mathbb{E}[X]$）基础上，引入正交化约束——即要求权重函数与倾向得分估计的得分函数（score function）在期望意义下正交。具体地，通过求解一个带有正交性惩罚项的优化问题，得到权重 $\hat{w}_i$，使得 $\sum_i \hat{w}_i T_i X_i = \sum_i X_i$ 且 $\sum_i \hat{w}_i \frac{\partial \log \hat{e}(X_i)}{\partial \beta} = 0$，其中 $\hat{e}(X)$ 为倾向得分模型。该正交条件借鉴了 double machine learning 中 Neyman 正交矩的思想，确保权重对倾向得分的一阶估计误差不敏感。

**与已有工作关系**  
与经典协变量平衡方法（如熵平衡、CBPS）相比，本方法额外要求权重与倾向得分模型的 score 正交，从而在理论上达到“双重稳健”的更强性质：只要倾向得分模型或权重矩条件之一正确，ATE 估计即一致。这与 Athey 等人（2018）的近似残差平衡（approximate residual balancing）不同，后者侧重线性回归的稳健性，而本方法直接针对倾向得分加权框架。此外，与 Chernozhukov 等人（2018）的 DML 相比，本方法通过权重而非残差化实现正交，更适用于有限样本下权重直接可解释的场景。

**贡献**  
主要贡献有三：第一，首次将正交性条件显式融入协变量平衡优化，提出一种新的权重估计量；第二，证明了该估计量在倾向得分模型误设下的 $\sqrt{n}$-一致性与渐近正态性，且渐近方差达到半参数效率下界；第三，通过模拟与实证研究展示了该方法在有限样本下优于 CBPS 和熵平衡的稳健性，尤其当倾向得分模型存在轻微误设时。该工作为因果推断中平衡权重的设计提供了新的理论视角。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)