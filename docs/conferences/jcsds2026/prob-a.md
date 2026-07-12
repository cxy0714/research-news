# 概率论与随机过程 Probability & Stochastic Processes · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 8 场）

---

## Interacting Particle System and Related Models

*7 月 11 日（周六） · 15:30-17:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Xinxin Chen（Beijing Normal University） · 主持 Xinxin Chen（Beijing Normal University）*

### 1. 分数ARIMA过程的阶选择

**讲者**：Chunhao Cai（Sun Yat-sen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
分数ARIMA（FARIMA）模型是刻画长记忆时间序列的经典工具，其阶选择涉及自回归阶 $p$、差分阶 $d$（允许非整数）和移动平均阶 $q$ 的联合确定。传统ARIMA的阶选择方法（如AIC、BIC）直接套用于FARIMA时面临两大困难：一是分数差分参数 $d$ 的连续性与整数阶 $p,q$ 的离散性混合，导致搜索空间非标准；二是长记忆特性使似然函数计算复杂，且有限样本下信息准则易过拟合或欠拟合。本报告旨在解决“如何同时且一致地选择 $(p,d,q)$”这一核心问题。

**核心方法**  
报告可能提出一种基于**修正Whittle似然**的两步法。第一步，利用周期图或小波方法获得 $d$ 的相合估计 $\hat d$（如GPH估计或局部Whittle估计），将其视为已知；第二步，对分数差分后的序列 $y_t = (1-B)^{\hat d} X_t$ 应用惩罚似然或信息准则（如BIC）选择 $p,q$，其中惩罚项针对长记忆残余进行调整。另一种可能是直接构造联合准则，例如将 $d$ 视为连续参数纳入AIC框架，并引入与 $d$ 相关的模型复杂度惩罚（如基于有效参数个数）。方法本质是将连续参数与离散阶的优化解耦或统一，并利用谱域近似降低计算负担。

**与已有工作关系**  
已有工作多聚焦于固定 $d$ 下的 $p,q$ 选择（如Hannan-Rissanen算法），或单独估计 $d$ 而不考虑阶选择。少数研究（如Beran et al., 1998）提出基于BIC的联合选择，但未充分处理长记忆导致的偏差。本报告可能改进之处在于：① 采用更稳健的 $d$ 估计初值，避免局部最优；② 针对有限样本下Whittle似然的偏差提出修正项，使准则在长记忆强度不同时仍保持一致性；③ 与近年基于机器学习（如LASSO）的阶选择方法对比，突出统计效率。

**贡献**  
主要贡献包括：① 提出一种计算可行且理论上一致的FARIMA阶选择准则，填补了该领域系统方法的空白；② 通过渐近理论证明所选阶数依概率收敛到真值，并给出有限样本下的模拟证据；③ 为长记忆时间序列建模提供了实用工具，可推广至季节分数ARIMA或多元情形。报告有望推动时间序列分析中模型选择理论从短记忆向长记忆的拓展。


### 2. On Phase Transition of a Multi Particle Pool Model

**讲者**：Yuan Zhang（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多粒子池模型（Multi Particle Pool Model）是一类描述大量粒子在多个“池”（pool）之间随机跳转的相互作用粒子系统。当系统参数（如粒子总数、池容量、跳转速率）变化时，系统可能呈现两种截然不同的宏观状态：粒子均匀分布在各池的“均匀相”与粒子聚集在少数池的“凝聚相”。该报告旨在严格刻画这一相变现象，回答“临界参数是什么？相变是否为一阶？临界指数如何？”等核心问题。

**核心方法**  
讲者可能采用概率论中的大偏差原理与耦合技术。首先将模型映射为某个可积随机过程（如零范围过程或广义排斥过程），利用其平稳分布的显式形式（如乘积形式）推导出粒子数分布的渐近行为。通过构造适当的序参量（如最大池粒子占比）并分析其大偏差速率函数，证明当粒子密度超过某一阈值时，速率函数从凸变为非凸，从而触发相变。此外，可能借助随机对偶或鞅方法刻画临界点附近的标度行为。

**与已有工作关系**  
经典池模型（如单粒子池模型或有限容量池模型）的相变已被广泛研究，但大多假设粒子间无相互作用或池容量固定。本工作将模型推广至多粒子、可变容量且允许粒子间排斥/吸引的设定，填补了非平凡相互作用下相变严格分析的空白。与零范围过程的凝聚相变相比，该模型允许粒子同时从多个池出发，导致更丰富的临界现象。

**贡献**  
主要贡献包括：(1) 给出多粒子池模型发生相变的精确临界条件（如粒子密度与池数之比），并证明相变的存在性与阶数；(2) 推导出临界指数（如凝聚相中最大池粒子数的增长阶数），揭示其与模型参数的普适类关系；(3) 提供一套可推广至其他相互作用粒子系统的分析框架，为统计物理中非平衡相变的理论研究提供新工具。


### 3. Shape of Large Feynman Cycles under BEC

**讲者**：Wen Sun（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
玻色-爱因斯坦凝聚（BEC）是量子统计力学中重要的相变现象，其微观机制可由 Feynman 路径积分中的环交换（cycle exchange）描述。在 BEC 相中，大量玻色子形成宏观占据的基态，对应的 Feynman 环（worldline cycles）呈现长程关联。然而，这些大环的几何形状（如回转半径、分形维数、环长分布）在临界点附近如何变化，以及是否存在普适的标度律，尚未被完全理解。本报告旨在刻画 BEC 相变下大 Feynman 环的统计形状。

**核心方法**  
讲者可能采用随机环模型（random loop model）或路径积分蒙特卡洛（PIMC）模拟，结合鞍点分析与重整化群思想。具体地，通过将玻色子系统的配分函数映射为环的集合，利用大偏差理论或极值统计研究环长 $L$ 与空间延伸 $R$ 的关系，例如 $R \sim L^\nu$ 中的指数 $\nu$。此外，可能引入环的曲率或缠绕数等几何量，并借助共形场论或 Schramm-Loewner Evolution（SLE）理论分析其临界行为。

**与已有工作关系**  
已有工作主要关注 BEC 中环长分布的幂律行为（如 $P(L) \sim L^{-\tau}$）以及环的连通性（如 percolation 转变）。本报告的新颖之处在于超越环长分布，深入探讨环的**形状**——例如环是否趋向于自回避行走（SAW）或布朗环，以及形状在临界点是否具有分形自相似性。这与统计物理中“环的几何”这一前沿方向（如环的 knotting、entanglement）紧密相关，但聚焦于 BEC 这一具体物理系统。

**主要贡献**  
1. 首次系统刻画 BEC 相变点附近大 Feynman 环的几何标度律，可能发现 $\nu$ 与已知临界指数（如 $\eta$、$\nu$）的关系。  
2. 揭示环形状从低温凝聚相到高温正常相的 crossover 行为，为理解 BEC 的拓扑激发提供新视角。  
3. 建立随机环模型与 SLE 的联系，为量子多体系统的几何性质研究提供可解析求解的范例。


### 4. Statistical Learning Problems in IPS: Learning Multi‑Type Heterogeneous Interacting Particle Systems

**讲者**：Xiong Wang（Sun Yat-sen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
相互作用粒子系统（Interacting Particle Systems, IPS）广泛用于物理、生物与社会科学，但现有统计学习工作多假设粒子类型单一且相互作用同质。实际场景中粒子常具有多种类型（如不同细胞亚群）且相互作用强度与形式随类型对而异。本报告聚焦于：如何从稀疏、含噪的轨迹观测中，同时学习多类型异质IPS的动力学方程（包括漂移项与扩散项）以及类型依赖的相互作用核函数？核心挑战在于类型标签未知、相互作用函数的高维非参数结构以及观测数据的时间离散性。

**核心方法**  
报告提出一种基于图神经网络（GNN）与变分推断的联合学习框架。首先，将每个时刻的粒子状态视为图节点，利用GNN编码器提取类型隐变量，并通过一个可微分的相互作用核参数化模块（如径向基函数网络）建模类型对之间的力场。其次，设计一个变分自编码器（VAE）结构，将粒子轨迹的似然函数近似为SDE的Euler-Maruyama离散化形式，并引入重参数化技巧同时优化类型分配与核函数参数。为处理异质性，采用Dirichlet过程先验自动确定类型数量，并通过一个对比正则项鼓励类型间核函数的可区分性。

**与已有工作关系**  
已有IPS学习工作主要分为两类：一是假设已知类型标签，仅估计同质或少量预定义类型的相互作用核（如经典的非参数核学习）；二是利用GNN学习同质粒子的动力学（如神经ODE）。本报告首次将类型发现与异质相互作用学习统一在概率框架下，突破了“类型已知”或“相互作用形式固定”的假设。与隐马尔可夫模型结合粒子滤波的方法相比，本方法无需显式模拟粒子轨迹，计算效率更高。

**贡献**  
主要贡献有三：1）提出一个端到端的统计学习框架，能同时推断粒子类型与多类型异质相互作用核，无需人工标注；2）在理论上证明了在适当正则化条件下，类型分配与核函数估计的相合性；3）在合成数据与真实生物迁移数据上验证了方法优于现有基准，尤其在类型数未知且观测稀疏时，恢复的相互作用网络具有更高的可解释性。该工作为复杂系统动力学推断提供了新工具。


## Probability and Asymptotic Theory

*7 月 11 日（周六） · 13:30-15:10 · Xijiang Room*  
*主办 Bernoulli Society for Mathematical Statistics and Probability · 组织 Xiao Fang（The Chinese University of Hong Kong） · 主持 Yuta Koike（The University of Tokyo）*

### 1. Sampling Error Bounds for the Denoising Diffusion Probabilistic Model via the Föllmer Process

**讲者**：Yuta Koike（The University of Tokyo）

**对应论文**：Wasserstein bounds for denoising diffusion probabilistic models via the Föllmer process · [arXiv:2605.18069](https://arxiv.org/abs/2605.18069)

<details><summary>摘要（原文）</summary>

This paper studies sampling error bounds for denoising diffusion probabilistic models (DDPMs) in the 2-Wasserstein distance. Our contributions are threefold. (i) Under general Lipschitz-type conditions on the score function and for a broad class of variance schedules, including the cosine schedule, we establish sharp upper bounds that are optimal in both the dimension and the number of steps, and recover several sharp error bounds previously obtained in the literature. (ii) We prove that the same Lipschitz-type conditions, which encompass those commonly imposed on the (learned) score, imply a logarithmic Sobolev inequality and hence a quadratic transportation cost inequality for the DDPM. As a consequence, in settings covered by existing work, an optimal Wasserstein bound, up to a logarithmic factor, follows from the recently obtained sharp error bound in the Kullback-Leibler divergence under geometric-type variance schedules. (iii) We show that for general log-concave target distributions, the optimal Wasserstein error bound remains attainable even without a quadratic transportation cost inequality for the target. Our analysis is based on viewing the DDPM sampler as a discretization of the Föllmer process rather than the conventional reverse Ornstein-Uhlenbeck process.

</details>

**问题**  
Denoising Diffusion Probabilistic Model (DDPM) 的采样误差分析以往多集中于 total variation 距离和 KL 散度，而 2-Wasserstein 距离因其统计相关性（如对几何结构的刻画）日益受到关注，但其分析难度更高。现有 Wasserstein 界要么依赖较强的目标分布假设（如强 log-concave），要么在步数或维度上非最优。该报告旨在为 DDPM 在 2-Wasserstein 距离下建立 sharp 的采样误差上界，并覆盖更广泛的方差调度（如 cosine schedule）和更一般的分布条件。

**核心方法**  
作者将 DDPM 采样器重新解释为 **Föllmer 过程**（而非传统的反向 Ornstein-Uhlenbeck 过程）的 Euler–Maruyama 离散化。Föllmer 过程的漂移项是一个鞅，这一结构带来三大优势：1）偏差项自动消失，简化了误差的 bias-variance 分解；2）有效步长 $h_i = t_{i+1} - t_i$ 比反向 OU 框架中的步长更小，允许分析更广泛的方差调度（包括 cosine schedule）；3）初始化误差的分析更精确，可显式刻画初始均值 $\hat{\mu}$ 对最终误差的影响。基于此，作者利用鞅表示和 $L^p$ 范数不等式（如 2-smoothness 性质）推导出离散化误差、分数近似误差和早停误差的累积上界。

**与已有工作关系**  
已有 Wasserstein 界（如 Arsenyan et al. 2025, Wang & Wang 2026, Stéphanovitch 2026）通常要求目标分布满足强 log-concave 或 sub-Gaussian 条件，且步长调度受限于几何型调度。本文在更弱的 Lipschitz 型条件下（如弱 log-concave 加半对数凸）恢复了这些最优阶 $\sqrt{d\eta}$ 的界，并首次将 cosine schedule 纳入理论分析。此外，作者证明 DDPM 样本分布满足对数 Sobolev 不等式，从而通过 Otto–Villani 定理将 Wasserstein 界与近期 sharp KL 界（Jiao et al. 2025）联系起来，揭示了已有结果的内在一致性。

**贡献**  
1. 在一般 Lipschitz 型条件下建立了 DDPM 在 2-Wasserstein 距离下的 sharp 上界，在维度和步数上达到最优，且对 cosine 等非几何调度同样适用。  
2. 证明了 DDPM 样本分布的对数 Sobolev 不等式，从而为从 KL 界导出 Wasserstein 界提供了通用路径。  
3. 对一般 log-concave 目标分布，即使目标本身不满足二次运输成本不等式，仍能获得最优 Wasserstein 误差界，显著放宽了现有理论对分布的要求。


### 2. Gaussian Fluctuations of Generalized U-Statistics and Subgraph Counting in the Binomial Random-Connection Model

**讲者**：Nicolas Privault（Nanyang Technological University）

**对应论文**：Gaussian fluctuations of generalized $U$-statistics and subgraph counting in the binomial random-connection model · [arXiv:2505.12338](https://arxiv.org/abs/2505.12338)

<details><summary>摘要（原文）</summary>

We derive normal approximation bounds for generalized $U$-statistics of the form \begin{equation*} S_{n,k}(f):=\sum_{ 1 \leq β(1),\dots,β(k) \leq n \atop β(i)\neβ(j), \ 1\leq i\ne j \leq k} f\big(X_{β(1)},\dots,X_{β(k)},Y_{β(1),β(2)},\dots,Y_{β(k-1),β(k)}\big), \end{equation*} where $\{X_i\}_{i=1}^n$ and $\{Y_{i,j}\}_{1\le i

</details>

**问题**  
该报告聚焦于广义 $U$-统计量  
\[
S_{n,k}(f)=\sum_{\beta\in[n]_{\neq}^k} f\big(X_{\beta(1)},\dots,X_{\beta(k)},Y_{\beta(1),\beta(2)},\dots,Y_{\beta(k-1),\beta(k)}\big)
\]  
的高斯波动问题，其中 $\{X_i\}$ 与 $\{Y_{i,j}\}$ 为独立 i.i.d. 序列。此类统计量可统一刻画二项随机连接模型（binomial random-connection model, RCM）中的子图计数。核心问题是：当连接概率 $p_n$ 可能趋于零时，子图计数 $N_G$ 的渐近正态性及其收敛速率如何？  

**核心方法**  
作者采用**划分图（partition diagram）论证**，首先推导广义 $U$-统计量的矩恒等式（Theorem 3.2），进而得到累积量上界（Theorem 4.1）。在此基础上，利用**累积量方法**（Statulevičius 条件）获得 Kolmogorov 距离下的正态逼近界（Corollary 4.3）及中偏差原理（Corollary 4.4）。针对子图计数，进一步结合**凸分析**（强平衡图的凸包边界）与依赖图技术，得到累积量增长率的精确刻画（Theorem 7.5），并由此导出 Kolmogorov 界（Corollary 7.9）与阈值现象（Corollary 7.11）。  

**与已有工作关系**  
已有工作如 [JN91] 研究了广义 $U$-统计量的渐近分布，但未给出收敛速率；[Zha22] 虽得到 Berry-Esseen 界，但要求连接概率 $p_n$ 不趋于零。在 Erdős–Rényi 模型中，[Kho08, FMN16] 给出了子图计数的累积量界，但无法直接推广至 RCM。本文首次在二项 RCM 中允许 $p_n=o(1)$，并建立了与 Erdős–Rényi 模型类似的**阈值现象**（当 $p_n\ll n^{-v(G)/e(G)}$ 时 $N_G\to 0$，反之 $N_G\to\infty$），同时将 Kolmogorov 界从常概率情形推广至稀疏情形。  

**主要贡献**  
1. 建立了广义 $U$-统计量的正态逼近界（Kolmogorov 距离 $\sim n^{-1/(2+4k)}$）及中偏差原理，方法基于划分图论证，具有一般性。  
2. 应用于二项 RCM 中的子图计数，对强平衡连通图 $G$ 给出了累积量增长率的完整刻画（分 $p_n\gg n^{-(v-1)/e}$ 与 $p_n\ll n^{-(v-1)/e}$ 两种情形），并得到相应的 Kolmogorov 界（分别为 $n^{-1/(2+4v)}$ 与 $(n^v p_n^{e})^{-1/(2+4v)}$）。  
3. 证明了子图包含的阈值现象，将 Erdős–Rényi 模型中的经典结论推广至更一般的随机连接模型。这些结果为高维统计与网络数据分析中的子图计数推断提供了理论支撑。


### 3. Decay of Correlations and Limit Theorems for Random Intermittent Dynamical Systems

**讲者**：Juho Leppanen（Tokai University）

**对应论文**：Decay of correlations and limit theorems for random intermittent maps · [arXiv:2511.02359](https://arxiv.org/abs/2511.02359)

<details><summary>摘要（原文）</summary>

In this paper, we revisit the problem of polynomial memory loss and the central limit theorem for time-dependent LSV maps. More precisely, we show that for random LSV maps corresponding to a random parameter beta() we obtain quenched memory loss, decay of correlations, central limit theorems with rates, moment bounds and almost sure invariance principles (ASIP) when the essential infimum of beta() is less than 1/5 and the driving process (i.e. random environment) is mixing sufficiently fast. In [59, Corollary 3.8] the ASIP was obtained for ergodic driving systems when the essential supremum of \b{eta} is less than 1/2. As will be elaborated in Section 1, restrictions on the essential infimum are more natural in our context. Our results have an abstract form which we believe could be useful in other circumstances, as will be elaborated in a future work

</details>

**问题**  
随机间歇动力系统（如随机 LSV 映射）因存在中性不动点而呈现多项式混合，其统计性质（CLT、ASIP 等）的证明长期受限于参数条件。已有结果（如 Su 2019, 2022）要求随机参数 $\beta(\omega)$ 的 essential supremum 小于 $1/2$，但物理上更自然的限制应作用于 essential infimum $\gamma = \operatorname{ess\,inf} \beta(\omega)$，因为小 $\beta$ 对应接近扩张映射的行为。本文旨在证明当 $\gamma < 1/5$ 且驱动过程混合足够快时，仍能获得 quenched 多项式记忆丧失、CLT 速率、矩界及 ASIP。

**核心方法**  
首先建立 quenched 多项式记忆丧失估计：对 Lipschitz 观测，控制转移算子迭代的 $L^s$ 范数，其中随机乘子 $K(\omega)$ 属于 $L^p$，衰减指数 $a$ 依赖于 $\gamma$。该估计通过将随机 LSV 映射的诱导（inducing）分析与大偏差技术结合，利用 $\beta(\omega) \le \gamma$ 的频繁出现来获得多项式上界。随后，基于记忆丧失估计，采用鞅逼近和 Skorokhod 嵌入定理（Su 的方法）证明 ASIP，并利用 Burkholder 不等式和反向鞅分解得到 CLT 速率与矩界。

**与已有工作关系**  
与 Su (2019, 2022) 相比，本文将 ASIP 的条件从 $\|\beta\|_{L^\infty} < 1/2$ 放松为 $\gamma < 1/5$，代价是要求驱动过程具有足够快的 $\alpha$-混合（而非仅遍历）。与 Nicol 等 (2021) 的矩界相比，本文获得了更精细的随机乘子 $K(\omega)$ 的 $L^p$ 可积性。此外，本文的抽象框架（Assumption 1）统一了多种非均匀双曲系统的记忆丧失估计，可推广至随机 Young 塔等情形。

**主要贡献**  
1. 首次在随机 LSV 映射中建立以 essential infimum 为条件的 ASIP、CLT 速率和矩界，参数范围更自然且更宽。  
2. 发展了适用于弱依赖驱动过程的 quenched 多项式记忆丧失估计，其随机乘子具有显式的大偏差控制。  
3. 提供了抽象条件（Assumption 1），使得后续研究可套用该框架获得其他随机间歇系统的极限定理。


### 4. Berry–Esseen Bounds for Distributed Studentized Statistics

**讲者**：Zhijun Cai（Southern University of Science and Technology）

**对应论文**：Nonuniform Berry-Esseen bounds for Studentized U-statistics · [arXiv:2303.08619](https://arxiv.org/abs/2303.08619)

<details><summary>摘要（原文）</summary>

We establish nonuniform Berry-Esseen (B-E) bounds for Studentized U-statistics of the rate $1/\sqrt{n}$ under a third-moment assumption, which covers the t-statistic that corresponds to a kernel of degree $1$ as a special case. While an interesting data example raised by Novak (2005) can show that the form of the nonuniform bound for standardized U-statistics is actually invalid for their Studentized counterparts, our main results suggest that, the validity of such a bound can be restored by minimally augmenting it with an additive correction term that decays exponentially in $n$. To our best knowledge, this is the first time that valid nonuniform B-E bounds for Studentized U-statistics have appeared in the literature.

</details>

**问题**  
Studentized U-statistics（如t统计量）在实际中需用数据驱动的Jackknife估计量替代未知方差，但其正态逼近的精度刻画长期缺失非均匀Berry-Esseen界。Novak (2005) 通过反例指出，通常形式的非均匀界（如 $|P(T_n \le x)-\Phi(x)|\le C(1+|x|)^{-3}n^{-1/2}$）对Studentized统计量不可能成立，因为当数据分布使 $T_n$ 以不可忽略概率取无穷值时，该界失效。因此，如何修正形式以恢复有效性是核心问题。

**核心方法**  
本文采用Stein方法，并引入**变量截断**（variable censoring）技术处理Studentizer $\hat\sigma$ 的复杂结构。关键创新在于：对分母余项 $D_2$ 施加精细截断后，利用**非负核U统计量的指数下尾界**（Lemma 4.3）得到 $P(\hat\sigma^2 \le c)$ 的指数衰减上界 $\exp(-c n \sigma^6/(E[|h|^3])^2)$。该界源于将 $\hat\sigma^2$ 重写为 $2m$ 阶非负核U统计量，并借助Hoeffding技巧与Rosenthal不等式导出。最终非均匀界形如  
$$|P(T_n\le x)-\Phi(x)|\le \exp\!\left(-\frac{c n\sigma^6}{(E[|h|^3])^2}\right)+\frac{C E[|h|^3]}{(1+|x|^3)\sqrt{n}\sigma^3},$$  
其中指数项为修正项，确保对Novak反例仍成立。

**与已有工作关系**  
已有工作仅建立Studentized U统计量的**均匀**Berry-Esseen界（Leung & Shao, 2023）或标准化U统计量的非均匀界（Chen & Shao, 2007）。本文首次证明非均匀界对Studentized版本有效，并揭示其必须附加指数衰减项，这与标准化情形本质不同。此外，对t统计量，借助Cramér型大偏差可进一步将非均匀因子改进为 $e^{-c x^2}$。

**贡献**  
1. 首次得到Studentized U统计量（任意阶核）的有效非均匀Berry-Esseen界，填补理论空白。  
2. 通过Novak反例证明修正项的必要性，并论证其指数阶 $n$ 的最优性。  
3. 发展了非负核U统计量的指数下尾界（Lemma 4.3），该工具独立于主结果，可应用于其他问题。  
4. 对t统计量给出更精细的指数型非均匀界，展示方法可推广性。


## Stochastic Partial Differential Equations

*7 月 13 日（周一） · 10:30-12:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Tusheng Zhang（University of Science and Technology of China） · 主持 Tusheng Zhang（University of Science and Technology of China）*

### 1. Dynamic Mean-Variance Problem with Frictions

**讲者**：Guiyuan Ma（Xi'an Jiaotong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典动态均值-方差（Mean-Variance）投资组合选择问题在无摩擦市场中已有成熟解，但现实市场存在交易成本、流动性限制、税收等摩擦因素，使得动态最优策略难以解析求解。本报告旨在解决：在存在多种摩擦（如比例交易成本、借贷约束、市场冲击）的连续时间框架下，如何刻画并求解动态均值-方差最优投资策略，并分析摩擦对有效前沿与策略结构的影响。

**核心方法**  
讲者可能采用随机控制与鞅方法相结合的路径。首先将动态均值-方差问题转化为一个等价的线性二次型（LQ）随机控制问题，利用Hamilton-Jacobi-Bellman（HJB）方程推导最优策略的解析形式。针对摩擦引入的非光滑性，可能借助粘性解（viscosity solution）理论或通过引入辅助状态变量（如“影子价格”）将约束松弛为无摩擦问题，再通过对偶方法或随机微分博弈（stochastic differential game）得到显式或半显式解。数值上，可能采用有限差分或深度学习算法处理高维状态空间。

**与已有工作关系**  
已有文献多聚焦于无摩擦动态均值-方差问题（如Zhou & Li, 2000）或静态摩擦情形。本报告将摩擦动态化，拓展了Li & Ng (2000) 的连续时间框架，并与存在交易成本的Merton问题（Davis & Norman, 1990）形成对比：后者以期望效用最大化为目标，而均值-方差目标导致时间不一致性，需引入预承诺（pre-commitment）或均衡策略概念。本报告可能首次在摩擦环境下给出预承诺策略的显式解，并比较其与无摩擦情形的偏差。

**主要贡献**  
1. 建立了包含多种摩擦的动态均值-方差问题的统一求解框架，填补了该领域理论空白。  
2. 揭示了摩擦如何扭曲有效前沿：例如交易成本导致有效前沿向内收缩，且最优策略呈现“惰性区域”（no-trade zone）。  
3. 提供了可操作的数值算法，为量化投资中考虑实际约束的资产配置提供理论依据。


### 2. Stochastic Reaction-Diffusion Equations with Super-Linear Drift

**讲者**：Shijie Shang（University of Science and Technology of China）

**对应论文**：Large deviation principle for stochastic reaction-diffusion equations with super-linear drift on $\mathbb{R}$ driven by space-time white noise · [arXiv:2307.14554](https://arxiv.org/abs/2307.14554)

<details><summary>摘要（原文）</summary>

In this paper, we consider stochastic reaction-diffusion equations with super-linear drift on the real line $\mathbb{R}$ driven by space-time white noise. A Freidlin-Wentzell large deviation principle is established by a modified weak convergence method on the space $C([0,T], C_{tem}(\mathbb{R}))$. Obtaining the main result in this paper is challenging due to the setting of unbounded domain, the space-time white noise, and the superlinear drift term without dissipation. To overcome these difficulties, the special designed norm on $C([0,T], C_{tem}(\mathbb{R}))$, one order moment estimates of the stochastic convolution and two nonlinear Gronwall-type inequalities play an important role.

</details>

**问题**  
该报告研究定义在实数线 $\mathbb{R}$ 上、由时空白噪声驱动的随机反应扩散方程  
\[
du^\epsilon(t,x)=\frac12\Delta u^\epsilon dt+b(u^\epsilon)dt+\sqrt{\epsilon}\sigma(u^\epsilon)W(dt,dx)
\]  
当噪声强度 $\epsilon\to0$ 时的 Freidlin–Wentzell 大偏差原理（LDP）。核心困难在于：空间域无界、噪声为时空白噪声（导致解的空间上确界几乎必然发散）、漂移项 $b$ 满足超线性增长（如 $b(u)=u\log|u|$）且不满足通常的耗散性条件。已有结果仅覆盖有界域或线性/耗散性漂移，无界域上超线性漂移的 LDP 是公开问题。

**核心方法**  
采用 Budhiraja–Dupuis 弱收敛方法，将 LDP 的验证转化为两个关键引理：骨架方程（确定性控制方程）的强连续性（Claim C1）以及随机受控方程与骨架方程之差依概率趋于零（Claim C2）。为克服无界域和超线性漂移，引入带时间依赖指数权的特殊范数  
\[
\sup_{t\le T,x\in\mathbb{R}}\bigl(|u(t,x)|e^{-\lambda|x|e^{\beta t}}\bigr),
\]  
其中 $\beta$ 与超线性系数 $c_1$ 相关，通过选取 $\lambda$ 足够小使 $T\le T^*(c_1,\lambda)$ 以保证关键不等式成立。利用一阶矩估计（而非高阶矩）处理对数非线性，并借助两个非线性 Gronwall 型引理控制增长。

**与已有工作关系**  
已有 LDP 结果（如 Cerrai–Röckner 2004, Salins 2021）均假设空间域为有界区间，且漂移项满足局部 Lipschitz 与多项式增长并具有耗散性（如 $b(u)=u-u^3$）。本文首次在无界域 $\mathbb{R}$ 上处理超线性漂移（如 $u\log|u|$）且无耗散性的情形，填补了该方向的空白。技术上的创新在于：用时间依赖的指数权范数替代传统停止时论证，并发展了一阶矩估计与非线性 Gronwall 不等式以应对对数奇异性。

**主要贡献**  
1. 建立了无界域上超线性漂移随机反应扩散方程的 Freidlin–Wentzell LDP，率函数由骨架方程给出。  
2. 提出了适用于无界域和超线性漂移的弱收敛方法变体，包括特殊范数设计、一阶矩估计和两个非线性 Gronwall 不等式。  
3. 为后续研究无界域上其他随机偏微分方程（如带耗散性漂移的情形）的 LDP 提供了可推广的分析框架。


### 3. Joint Law Limits for Non-Autonomous Multi-Scale Diffusions with Irregular Coefficients

**讲者**：Longjie Xie（Jiangsu Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多尺度扩散系统广泛用于物理、生物与金融建模，但现有极限理论大多假设系数光滑且系统自治（即系数不显含时间）。当系统具有非自治性（系数随时间变化）且系数不规则（如仅 Hölder 连续或可测）时，快慢变量的联合分布极限行为尚不清晰。本报告旨在建立此类非自治多尺度扩散的 joint law limits，即快过程与慢过程在适当时间尺度下的联合弱收敛定理。

**核心方法**  
讲者可能采用“随机平均原理”的推广，结合鞅问题与 tightness 论证。核心思路是将快过程视为一个“时间非齐次”的随机环境，利用其遍历性构造一个有效漂移与扩散系数，该系数依赖于慢过程的当前状态与时间。对于不规则系数，需借助截断、光滑化与局部时技术，并利用 Krylov 估计或 Malliavin 分析控制误差。最终通过证明 Skorokhod 空间上的联合弱收敛，得到极限过程由一组耦合的 SDE 描述，其中慢过程系数由快过程的 invariant measure 在时间上的平均给出。

**与已有工作关系**  
经典多尺度扩散极限（如 Papanicolaou–Varadhan 理论）要求系数 Lipschitz 连续且系统自治。近年虽有工作推广到不规则系数（如随机动力系统粗粒化），但大多仍假设自治或仅考虑慢过程的边缘极限。本报告将非自治性与不规则性同时纳入，并首次给出快慢过程的联合分布极限，填补了“时间依赖系数 + 低正则性”情形下的理论空白。

**主要贡献**  
1. 在系数仅 Hölder 连续或可测的条件下，证明了非自治多尺度扩散的联合弱收敛定理，推广了经典随机平均原理。  
2. 提供了极限过程的显式刻画：慢过程系数由快过程在时间依赖的 invariant measure 下的积分给出，快过程则收敛到一个与慢过程耦合的 Ornstein–Uhlenbeck 型过程。  
3. 为后续研究非自治多尺度系统的偏差估计、大偏差原理及数值粗粒化算法提供了理论基础。


### 4. Stochastic Wave Equation with Additive Fractional Noise: Solvability and Global Hölder Continuity

**讲者**：Xiong Wang（Sun Yat-sen University）

**对应论文**：Stochastic wave equation with additive fractional noise: solvability and global Hölder continuity · [arXiv:2305.02425](https://arxiv.org/abs/2305.02425)

<details><summary>摘要（原文）</summary>

We determine the range of Hurst parameters that provide the necessary and sufficient conditions for the solvability, in $L^2(Ω)$, of the stochastic wave equation: $ \frac{\partial^2 }{\partial t^2}u(t,x) =Δu(t,x)+\dot{W}(t,x)$, where $\{ W(t,x),\ t\geq 0, x\in \mathbb{R}^d\} $ is a fractional Brownian field with temporal Hurst parameter $H_0\in[\tfrac12,1]$ and spatial Hurst parameters $H_i\in(0,1)$ for $i=1,\cdots,d$. {In particular, the solvability condition exhibits a phase transition at $H_0 = 1$.} We also obtain the sharp growth rate and the sharp Hölder continuity of the solution on the real line in the case $H_0=1/2$.

</details>

**问题**：该报告研究带加性分数噪声的随机波动方程（SWE）的可解性与全局 Hölder 连续性。噪声为时间 Hurst 参数 $H_0\in[1/2,1]$、空间 Hurst 参数 $H_i\in(0,1)$ 的分数布朗场。核心问题是：在什么条件下方程在 $L^2(\Omega)$ 意义下有解？解在时空上的全局 Hölder 正则性如何？特别地，当空间参数 $H_i$ 可以小于 $1/2$（即粗糙噪声）时，已有结果不再适用，需要新的充要条件。

**核心方法**：可解性条件通过分析随机积分方差积分的收敛性得到。利用 Fourier 变换将问题转化为多重积分收敛性判别，关键在于处理波核 $\hat G_t(\xi)=\sin(t|\xi|)/|\xi|$ 的振荡性。对于 $H_0\in(1/2,1)$，通过变量替换和广义超几何函数 ${}_1F_2$ 的渐近分析，得到 $g_1(\rho)\asymp\rho$ 的精确阶，从而导出条件 $|H|+H_0>d-1/2$。对于 $H_0=1/2$ 和 $H_0=1$ 则直接积分。全局 Hölder 连续性部分，利用 Talagrand 的 majorizing measure 定理和 Sudakov 下界定理，关键在于建立解的正则度量 $d_1((t,x),(s,y))$ 的精确上下界，其形式为 $(s\wedge t)^{1/2}[|x-y|^H\wedge (s\wedge t)^H] + (s\vee t)^{1/2}|t-s|^H$，这比热方程情形更复杂。

**与已有工作关系**：已有工作（如 Balan-Tudor 2010）在 $H_0>1/2$ 且 $H_i>1/2$ 时给出了可解性条件 $|H|+H_0>d-1/2$，但未覆盖 $H_i<1/2$ 的情形。本文首次给出所有 $H_i\in(0,1)$ 的充要条件，并发现 $H_0=1$ 时条件发生相变（不连续性），这是新现象。对于 Hölder 连续性，已有结果多限于局部或仅上界，本文在一维时间白噪声情形下给出了匹配的上下界，并显式刻画了常数对区域直径的依赖（全局性），这比热方程情形（Hu-Wang 2022）的增长率形式不同。

**贡献**：1）完整刻画了 SWE 在加性分数噪声下的可解性充要条件，包括 $H_0=1$ 处的相变，填补了粗糙空间参数情形的空白。2）在一维时间白噪声情形下，得到了解的全局增长率和时空 Hölder 连续性的精确（sharp）上下界，证明 Hölder 指数 $H-\epsilon$ 是最优的，且常数随区域增长呈对数修正。3）方法上，处理波核振荡性的积分技巧和度量估计为更一般的非线性 SWE 研究提供了工具。


## Branching Processes and Related Models

*7 月 13 日（周一） · 13:30-15:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Xinxin Chen（Beijing Normal University） · 主持 Quan Shi（Chinese Academy of Sciences‌）*

### 1. Towards Central Limit Theorem of Critical Branching Random Walks

**讲者**：Tianyi Bai（Chinese Academy of Sciences）

**对应论文**：Central limit theorem for the range of critical branching random walk · [arXiv:2511.17101](https://arxiv.org/abs/2511.17101)

<details><summary>摘要（原文）</summary>

In this paper, we study second order fluctuations for the size of the range of a critical branching random walk (BRW) in $\mathbb Z^d$. We consider the BRW with geometric offspring indexed by the Kesten tree, and show that the size of its range has linear variance when $d>8$, and satisfies a central limit theorem (CLT) with Gaussian limiting distribution when $d>16$. The proof combines the stationarity of the model under depth-first exploration, the general CLT of Dedecker and Merlevède [7], a truncation scheme exploiting the local independence of the tree, and a recursive method for controlling moments.

</details>

**问题**  
临界分支随机游走（critical branching random walk, BRW）的 range（即所有访问位置的集合）大小 $#\mathcal{R}_n^{(c)}$ 的渐近行为已在低维（$d\le 4$）得到刻画，但其二阶波动——特别是中心极限定理（CLT）——在高维下仍是公开问题。经典随机游走的 range 满足 CLT（$d\ge 3$），但 BRW 的增量沿深度优先顺序不再独立，导致传统方法失效。本报告旨在证明：当维度足够高时，range 的波动服从高斯极限。

**核心方法**  
讲者采用 Kesten 树（临界 Galton–Watson 树条件为无穷）构造平稳的双边 BRW 序列 $(V(k))_{k\in\mathbb{Z}}$，并定义修正的 range 统计量 $Y_n = \#\{V(1),\dots,V(n)\}\setminus V(-\infty,0]$。利用深度优先探索的平移不变性，$Y_n$ 的求和项构成平稳序列。证明的关键在于：  
1. 通过截断技术将指示函数 $1_{\{V(i)\notin V(-\infty,i)\}}$ 替换为仅依赖局部图距离的 $\xi_i^k$，使得相距足够远的项独立；  
2. 应用 Dedecker–Merlevède 关于平稳序列的条件 CLT 准则，将问题转化为验证三个条件：条件期望收敛、条件方差收敛以及均匀可积性；  
3. 借助 Kesten 树的显式结构（几何后代分布）和随机游走的局部时估计，精细控制矩与协方差。

**与已有工作关系**  
已有工作（Jain–Pruitt, Le Gall–Rosen）对经典随机游走的 range 建立了 CLT，其核心依赖增量独立性。对于 BRW，Le Gall–Lin 与 Zhu 已得到 range 的 law of large numbers 及临界维度 $d=4$，但二阶波动长期未解。本文首次将 CLT 推广至 BRW 这一缺乏独立增量的模型，并揭示了维度门槛 $d>8$（方差线性增长）与 $d>16$（高斯极限）的机制。此外，方法上借鉴了 Asselah–Schapira–Sousi 对随机游走 capacity 的 CLT 证明中的截断与矩估计思想，但需处理树结构带来的复杂依赖。

**主要贡献**  
1. 证明了当 $d>8$ 时，$Y_n$ 的方差线性增长：$\lim_{n\to\infty} \operatorname{Var}(Y_n)/n = \kappa>0$；  
2. 当 $d>16$ 时，建立了条件 CLT：$(Y_n-\mathbb{E}[Y_n])/\sqrt{n} \xrightarrow{d} N(0,\kappa)$，且极限分布是高斯型；  
3. 给出了第四矩估计 $\mathbb{E}[\langle Y_n\rangle^4] \lesssim n^2$，从而保证均匀可积性；  
4. 揭示了维度门槛与 BRW 的 Hausdorff 维数（$4$）的关系：$d>4\times 4$ 时四矩可控，并猜想 $d>8$ 时 CLT 可能仍成立但需更精细方法。


### 2. 二维高斯自由场的臂概率

**讲者**：Yifan Gao（Westlake University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
二维高斯自由场（2D Gaussian Free Field, GFF）是随机分析与统计物理中的核心对象，其水平集（level set）的几何性质（如连通分量的数目、分形维数）长期受到关注。本报告聚焦于GFF的“臂概率”（arm probability）：在圆环区域中，从内边界到外边界存在 $k$ 条不相交的连通路径（臂）的概率。这一问题直接关联到GFF水平集的临界指数、渗流相变行为以及共形场论中的多臂指数，是理解GFF空间结构的关键未解难题。

**核心方法**  
讲者可能利用GFF的共形不变性与高斯过程的特殊结构，将臂概率转化为某种随机游走或布朗运动的首达问题。具体地，通过将GFF的零水平集与Schramm-Loewner Evolution（SLE）的边界行为建立联系，或借助离散高斯自由场的缩放极限，推导臂概率的指数衰减率。方法上可能结合了共形场论中的算子乘积展开（OPE）与概率论中的耦合技术，将多臂事件分解为独立臂的乘积形式，并利用GFF的Markov性质与局部化技巧得到精确渐近。

**与已有工作关系**  
已有工作主要集中于离散渗流模型（如Bernoulli渗流、随机簇模型）的臂指数，以及GFF水平集的单臂概率（如零水平集连通性）。本报告将臂概率推广至多臂情形，并利用GFF的连续性与共形不变性，可能得到与离散模型不同的指数（例如，由于GFF的长程相关性，多臂指数可能不满足简单的加和性）。此外，与SLE理论中多臂事件的指数计算形成对照，揭示GFF作为高斯场的独特几何特征。

**主要贡献**  
1. 首次系统研究二维GFF的多臂概率，给出其指数衰减的严格上界与下界，并推测精确指数。  
2. 建立GFF臂概率与共形场论中多点关联函数的联系，为统计物理中的临界指数提供新计算框架。  
3. 方法上发展了一套处理连续高斯场多连通事件的概率工具，可推广至其他高斯随机场（如高斯自由场在黎曼曲面上的推广）。


### 3. Branching Random Walks and Percolation on Hyperbolic Groups

**讲者**：Longmin Wang（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
双曲群（hyperbolic groups）是一类具有负曲率几何性质的无限群，其上的随机过程（如随机游走、渗流）是几何概率与群论交叉的前沿。本报告聚焦于双曲群上的分支随机游走（branching random walk）与渗流（percolation）模型，旨在回答：在非欧几何背景下，分支系统的空间分布与连通性相变如何受群的双曲性影响？具体而言，当粒子在 Cayley 图上按群作用随机移动并分裂时，其极限行为（如波前速度、极值位移）与渗流临界阈值是否可由群的几何参数（如等周不等式、Gromov 边界）刻画？

**核心方法**  
报告将双曲群的负曲率性质转化为概率工具：利用群的双曲性构造“测地线树”近似，将分支随机游走的路径嵌入到群的边界（boundary）上，从而将问题约化至树上的分支过程。对于渗流，则借助双曲群上的等周不等式与指数增长性质，通过比较渗流簇的边界体积与内部体积，建立相变的存在性。关键技巧包括：使用 Gromov 乘积定义“距离扭曲”，结合鞅方法与 large deviation 原理控制粒子数的空间分布；对渗流，引入“锚定”技术（anchoring）处理群作用的非交换性。

**与已有工作关系**  
经典分支随机游走与渗流理论主要建立在欧氏空间 $\mathbb{Z}^d$ 或正则树上，其几何是平坦或树状的。双曲群介于两者之间：它既非可交换（如 $\mathbb{Z}^d$），也非自由群（如树），而是具有负曲率但可能含环路的图。已有工作（如 Benjamini–Schramm 对双曲群上随机游走的调和测度研究）为渗流提供了基础，但分支过程与渗流的耦合分析尚属空白。本报告将树上的经典结果（如 Biggins 定理）推广到双曲群，并揭示群的双曲性如何导致与欧氏空间截然不同的相变行为（例如渗流临界概率可能为 0 或 1 的极端情形）。

**贡献**  
主要贡献有三：其一，建立了双曲群上分支随机游走的波前速度公式，证明其由群的指数增长率和随机游走的漂移共同决定；其二，证明了双曲群上 Bernoulli 渗流的相变存在性，并给出临界概率的上下界，与群的等周常数直接相关；其三，揭示了分支过程与渗流在双曲群上的深层联系——分支随机游走的极值位移可视为渗流簇的“边界距离”，从而统一了两类模型的渐近分析。这些结果为理解负曲率空间上的随机演化提供了新工具，也为群论中的几何性质提供了概率解释。


### 4. Cover Times for Random Walk on Subcritical Dynamical Percolation

**讲者**：Yushu Zheng（Chinese Academy of Sciences）

**对应论文**：Cover times for random walk on dynamical percolation · [arXiv:2312.06821](https://arxiv.org/abs/2312.06821)

<details><summary>摘要（原文）</summary>

We study the cover time of random walk on dynamical percolation on the torus $\mathbb{Z}_n^d$ in the subcritical regime. In this model, introduced by Peres, Stauffer and Steif, each edge updates at rate $μ$ to open with probability $p$ and closed with probability $1-p$. The random walk jumps along each open edge with rate $1/(2d)$. We prove matching (up to constants) lower and upper bounds for the cover time, which is the first time that the random walk has visited all vertices at least once. Along the way, we also obtain a lower bound on the hitting time of an arbitrary vertex starting from stationarity, improving on the maximum hitting time bounds by Peres, Stauffer and Steif.

</details>

**问题**  
亚临界动态渗流（dynamical percolation）模型下，随机游走在环面 $\mathbb{Z}_n^d$ 上的覆盖时间（首次访问所有顶点的时间）的渐近阶是什么？该模型由 Peres–Stauffer–Steif (2015) 引入，每条边以速率 $\mu$ 独立更新为开（概率 $p<p_c(d)$）或闭，游走沿开边以速率 $1/(2d)$ 跳跃。此前仅知混合时间与最大击中时间的紧界，覆盖时间尚无结果。

**核心方法**  
利用再生时间序列 $(\tilde{\tau}_k)$ 将动态渗流上的游走与对称随机游走耦合：在再生时刻，环境条件独立于游走历史且服从 $\pi_x^p$（顶点 $x$ 的邻边全闭），游走位置构成对称随机游走，再生间隔期望为 $O(1/\mu)$，其间访问顶点数有指数尾。  
- 对 $d\ge 3$：先证明从 $\pi_x^p$ 出发击中任意顶点 $y$ 的期望时间下界为 $\Omega(n^d/\mu)$（定理 1.4），利用局部中心极限定理和再生间隔内访问顶点数有界性；再通过 Matthews 方法，选取间距 $\sqrt{n}$ 的顶点子集，结合再生时刻的环境性质，将覆盖时间下界转化为击中时间下界之和。  
- 对 $d=2$：将再生时刻的游走强逼近为布朗运动（Einmahl 定理），利用二维布朗运动覆盖时间的已知结果（Dembo–Peres–Rosen–Zeitouni 2004）得到下界 $n^2(\log n)^2/\mu$。  
- 对 $d=1$：通过构造往返于 $0$ 与 $n/2$ 的再生区间，利用几何分布与 Wald 等式得到上界 $O(n^2/\mu)$，下界由击中时间下界直接给出。

**与已有工作关系**  
Peres–Stauffer–Steif (2015) 给出了亚临界区混合时间 $t_{\text{mix}}\le C n^2/\mu$ 及最大期望击中时间 $t_{\text{hit}}$ 的上下界（$d=1$: $\Theta(n^2/\mu)$; $d=2$: $\Theta(n^2\log n/\mu)$; $d\ge 3$: $\Theta(n^d/\mu)$）。本文首次研究覆盖时间，并发现其阶与击中时间相比在 $d\ge 3$ 时多一个 $\log n$ 因子（来自 Matthews 方法中调和级数），在 $d=2$ 时多一个 $\log n$ 因子（来自布朗运动覆盖时间）。此外，定理 1.4 改进了 $d\ge 3$ 时从 $\pi_x^p$ 出发的击中时间下界，此前仅知最大击中时间上界。

**主要贡献**  
1. 证明了亚临界动态渗流上覆盖时间的紧界（常数因子匹配）：  
   $d=1$: $\Theta(n^2/\mu)$; $d=2$: $\Theta(n^2(\log n)^2/\mu)$; $d\ge 3$: $\Theta(n^d\log n/\mu)$。  
2. 为 $d\ge 3$ 建立了从特殊环境 $\pi_x^p$ 出发的击中时间下界 $\Omega(n^d/\mu)$，该下界与最大击中时间同阶，是覆盖时间下界的关键。  
3. 方法上展示了如何将再生时间技术与 Matthews 方法、强逼近结合，处理非马尔可夫游走的覆盖时间问题，为动态随机环境中的极值时间分析提供了新工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)