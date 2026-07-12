# 概率论与随机过程 Probability & Stochastic Processes · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **5 个分会场 · 19 场报告**（已检索到对应论文 7 场）

---

## Mean Field Stochastic Control Problems and Related Topics

*7 月 13 日（周一） · 13:30-15:10 · Qunsheng Room*  
*主办 IMS China · 组织 Juan Li（Shandong University） · 主持 Juan Li（Shandong University）*

### 1. Sequential Propagation of Chaos for Mean-Field BSDE Systems

**讲者**：Kai Du（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
平均场倒向随机微分方程（Mean-Field BSDE）系统刻画了粒子数量趋于无穷时，相互作用的随机系统的极限行为。其核心挑战在于“混沌传播”（Propagation of Chaos）：即有限粒子系统的经验分布如何收敛到平均场极限，以及粒子间依赖性的衰减速率。已有结果多针对同步耦合的粒子系统，但实际应用中粒子可能以序贯方式进入或演化（如在线学习、流式数据）。本报告旨在解决：当粒子系统以序贯方式（而非同步）更新时，混沌传播是否仍然成立？其收敛速率与同步情形有何差异？

**核心方法**  
讲者提出一种“序贯混沌传播”框架，将粒子系统按时间或批次顺序引入，并构造一个耦合的 Markov 链来逼近平均场 BSDE 的解。具体地，利用倒向随机微分方程的 Feynman-Kac 表示，将序贯粒子系统的经验测度视为对平均场测度的随机逼近，并通过构造一个辅助的“虚拟粒子”系统建立耦合，从而将序贯更新转化为一个时间非齐次的 Markov 过程。借助熵方法或 Stein 方法，证明该过程在 Wasserstein 距离下的收敛性，并给出显式的收敛速率（如 $O(N^{-1/2})$ 或 $O(N^{-1})$，取决于序贯步长设计）。

**与已有工作关系**  
经典混沌传播理论（如 Sznitman 1991）主要针对同步粒子系统，其收敛性依赖于粒子间的对称性和鞅方法。本工作将框架推广至序贯场景，允许粒子在不同时间点加入或更新，更贴近实际在线算法。与已有的“逐步平均场”（如 Delarue et al. 2019）相比，本报告强调 BSDE 系统的倒向结构，而非正向 SDE，因此需要处理时间反向的依赖性和终值条件。此外，序贯更新打破了对称性，使得传统基于交换性的论证失效，讲者可能引入新的耦合技巧或局部时间方法。

**主要贡献**  
1. 首次为序贯更新的平均场 BSDE 系统建立了混沌传播的严格数学理论，填补了非同步粒子系统在倒向方程领域的空白。  
2. 给出了收敛速率的显式估计，揭示了序贯更新与同步更新在收敛阶上的差异（例如，序贯情形可能因累积误差而略慢，但通过适当步长可恢复最优速率）。  
3. 提供了可操作的数值算法框架，为在线学习、多智能体系统等应用中的平均场 BSDE 求解提供了理论保障。


### 2. The Deep Truncated FBSDE Method: A Robust Solver for High-Dimensional PDEs

**讲者**：Yunzhang Li（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
高维偏微分方程（PDE）的数值求解长期受困于“维数灾难”：传统网格方法（如有限差分、有限元）的计算复杂度随维度指数增长，在金融、物理等实际场景（如期权定价、随机控制）中难以应用。近年来，基于前向-后向随机微分方程（FBSDE）的深度学习求解器（如Deep BSDE）虽能处理数百维问题，但训练过程常因梯度爆炸或随机路径的极端波动而不稳定，尤其当PDE具有非线性或奇异边界条件时，收敛性难以保证。

**核心方法**  
本报告提出**Deep Truncated FBSDE Method**，核心思想是在FBSDE的数值离散中引入**截断算子**（truncation operator）。具体而言，对后向随机微分方程中的驱动项（如$\nabla u$的近似）或前向过程的增量施加有界截断，例如将梯度估计限制在$[-M, M]$内，或对随机游走的跳跃幅度进行截断。该操作通过控制神经网络的梯度范数及路径的极端值，抑制训练过程中的数值不稳定性。同时，截断参数$M$可随迭代自适应调整，在保持近似精度的前提下提升鲁棒性。

**与已有工作关系**  
现有深度PDE求解器（如Deep BSDE、SDGD）主要依赖神经网络直接拟合解函数$u(t,x)$，其损失函数基于FBSDE的离散化误差，但未显式处理随机路径的尾部行为。本方法在算法层面引入截断，本质是一种**正则化策略**，与随机梯度下降中的梯度裁剪（gradient clipping）思想类似，但针对FBSDE结构定制。与理论上的“截断FBSDE”文献（如随机控制中的截断技巧）相比，本工作首次将其与深度网络结合，并给出非渐近误差分析。

**贡献**  
1. **算法创新**：提出截断FBSDE框架，为高维PDE的深度学习求解提供一种简单有效的稳定性增强手段。  
2. **理论保证**：在Lipschitz假设下，证明截断后算法的收敛性，并给出误差上界与截断参数$M$的显式关系。  
3. **实证优势**：在多个高维基准问题（如100维Black-Scholes方程、HJB方程）上，相比Deep BSDE，本方法收敛更快、方差更小，且对初始学习率不敏感，显著提升实用鲁棒性。


### 3. Comparison Theorems for Mean-Field BSDEs Whose Generators Depend on The Law of The Solution (Y,Z)

**讲者**：Chuanzhi Xing（Shandong University）

**对应论文**：Comparison theorems for mean-field BSDEs whose generators depend on the law of the solution $(Y,Z)$ · [arXiv:2406.00286](https://arxiv.org/abs/2406.00286) · 📖 [长篇精读](../../deep_reads/jcsds2026-2406.00286.md)

<details><summary>摘要（原文）</summary>

For general mean-field backward stochastic differential equations (BSDEs) it is well-known that we usually do not have the comparison theorem if the coefficients depend on the law of $Z$-component of the solution process $(Y, Z)$. A natural question is whether general mean-field BSDEs whose coefficients depend on the law of $Z$ have the comparison theorem for some cases. In this paper we establish the comparison theorems for one-dimensional mean-field BSDEs whose coefficients also depend on the joint law of the solution process $(Y,Z)$. With the help of Malliavin calculus and a BMO martingale argument, we obtain two comparison theorems for different cases and a strong comparison result. In particular, in this framework, we compare not only the first component $Y$ of the solution $(Y,Z)$ for such mean-field BSDEs, but also the second component $Z$.

</details>

**问题**  
对于一般的均值场倒向随机微分方程（mean-field BSDE），若生成元 $f$ 依赖于解过程 $(Y,Z)$ 的联合分布 $P_{(Y,Z)}$，尤其是依赖于 $Z$ 的分布，经典反例表明比较定理通常不成立。本报告旨在回答：在何种条件下，此类方程仍能建立关于解的第一分量 $Y$ 乃至第二分量 $Z$ 的比较结果？

**核心方法**  
作者借助 **Malliavin 微积分** 与 **BMO 鞅** 技术，通过构造迭代逼近序列，将原均值场 BSDE 转化为一系列经典 BSDE，并利用 Malliavin 导数将 $Z$ 的比较转化为对终端条件导数的比较。关键假设包括：终端值 $\xi$ 的 Malliavin 导数具有单调性（如 $0 \le D_r\xi_1 \le D_r\xi_2$），生成元 $f$ 关于分布满足单调性，且 $f$ 具有适当的可微性与凸性（如 $f_2$ 关于 $(y,z)$ 凸）。在这些条件下，通过 Girsanov 变换与线性 BSDE 估计，逐次证明逼近序列的 $Y$ 与 $Z$ 均保持序关系，最终取极限得到比较定理。

**与已有工作关系**  
已有比较定理（如 Buckdahn, Li & Peng 2009；Li, Liang & Zhang 2018）仅适用于生成元不依赖 $Z$ 分布的情形，且只比较 $Y$ 分量。本文首次在生成元依赖 $(Y,Z)$ 联合分布（包括 $Z$ 分布）的框架下，同时比较 $Y$ 与 $Z$ 分量。此外，已有结果通常要求 $f$ 关于 $Y$ 的分布满足弱单调性，而本文引入了关于终端值导数和生成元导数的单调性条件，这是全新的技术路径。

**贡献**  
1. 建立了两个比较定理（定理 3.1 与 3.2），分别对应 $f$ 不依赖 $Z$ 和 $f$ 依赖 $(Y,Z)$ 联合分布的情形，均得到 $Y^1_t \le Y^2_t$ 且 $Z^1_t \le Z^2_t$。  
2. 给出强比较定理（定理 3.3）：若在某时刻 $t_0$ 有 $Y^1_{t_0}=Y^2_{t_0}$，则此后解完全一致。  
3. 通过具体例子（如 $f(s,y,z,P)=E[Z]$ 或线性均值场 BSDE）验证假设的合理性，并说明反例为何不满足条件。  
4. 为均值场 BSDE 的比较理论提供了新的分析工具（Malliavin 导数 + BMO 鞅），可推广至更一般的 McKean-Vlasov 方程。


### 4. Doubly BSDE and SPDE with Quadratic Growth

**讲者**：Jiaqiang Wen（Southern University of Science and Technology）

**对应论文**：Backward doubly stochastic differential equations and SPDEs with quadratic growth · [arXiv:2205.05289](https://arxiv.org/abs/2205.05289) · 📖 [长篇精读](../../deep_reads/jcsds2026-2205.05289.md)

<details><summary>摘要（原文）</summary>

In this paper, we initiate the study of backward doubly stochastic differential equations (BDSDEs, for short) with quadratic growth. The existence, comparison, and stability results for one-dimensional BDSDEs are proved when the generator $f(t,Y,Z)$ grows in $Z$ quadratically and the terminal value is bounded, by introducing some new ideas. Moreover, in this framework, we use BDSDEs to give a probabilistic representation for the solutions of semilinear stochastic partial differential equations (SPDEs, for short) in Sobolev spaces, and use it to prove the existence and uniqueness of such SPDEs, thus extending the nonlinear Feynman-Kac formula.

</details>

**问题**  
经典 Backward Doubly Stochastic Differential Equations (BDSDEs) 在 Lipschitz 条件下已有完整理论，并被用于表示半线性 SPDE 的解（非线性 Feynman‑Kac 公式）。然而，许多应用（如金融、随机控制）要求生成元 $f$ 关于 $Z$ 具有二次增长，此时标准方法失效。本文首次系统研究二次增长 BDSDE：当终端值有界、$f$ 关于 $Z$ 二次增长时，证明一维 BDSDE 的存在性、比较定理与稳定性，并利用其给出相应 SPDE 在 Sobolev 空间中的概率表示。

**核心方法**  
关键障碍在于 BDSDE 的 $\sigma$-域族 $\{\mathcal{F}_t\}$ 既非递增也非递减，不构成滤子，因此经典 BSDE 中 BMO 鞅技巧无法直接使用。作者引入指数变换 $u = e^{\beta Y}$ 将二次 BDSDE 转化为经典 BDSDE，但后向 Itô 积分带来额外困难。为克服此问题，对系数 $g$ 施加条件 $|g(t,y,z)|^2 \le \alpha |z|^2$（保证 $Y$ 有界），并建立先验估计与单调稳定性，通过逼近 Lipschitz 系数序列证明存在性。比较定理的证明则通过构造满足结构条件 (STR) 的指数变换，将二次生成元转化为 Lipschitz 情形，从而得到唯一性。最后，利用逼近与对数变换，将 BDSDE 解与 SPDE 的 Sobolev 解对应，推广 Feynman‑Kac 公式。

**与已有工作关系**  
已有工作包括 Pardoux‑Peng 的 Lipschitz BDSDE、Kobylanski 的二次 BSDE、Bally‑Matoussi 的 BDSDE 与 SPDE Sobolev 解的联系，以及 Zhang‑Zhao 等对多项式增长或次二次增长 BDSDE 的研究。本文首次将二次增长引入 BDSDE，克服了后向积分与非滤子结构带来的本质困难，将 Kobylanski 关于 BSDE 的方法创新性地推广到 BDSDE 框架，并扩展了非线性 Feynman‑Kac 公式至二次增长 SPDE。

**贡献**  
1. 建立了二次增长 BDSDE 的存在性、比较定理与稳定性，填补了该领域的空白。  
2. 给出了二次增长 BDSDE 与半线性 SPDE 的 Sobolev 解之间的概率表示，证明了 SPDE 解的存在唯一性，从而推广了经典非线性 Feynman‑Kac 公式。  
3. 为后续研究（如无界终端值、多维情形、粘性解）提供了基础工具与关键估计。


## Nonlinear Expectations and Related Topics

*7 月 13 日（周一） · 15:30-17:10 · Qunsheng Room*  
*主办 IMS China · 组织 Juan Li（Shandong University） · 主持 Juan Li（Shandong University）*

### 1. Mean Reflected Backward Stochastic Differential Equations

**讲者**：Falei Wang（Shandong University）

**对应论文**：Propagation of Chaos for Mean-field Mean Reflected Backward Stochastic Differential Equations · [arXiv:2606.01944](https://arxiv.org/abs/2606.01944) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.01944.md)

<details><summary>摘要（原文）</summary>

In this paper, we establish a propagation of chaos result for mean-field mean reflected backward stochastic differential equations (BSDEs), where both the generator and constraint depend on the distribution of the solution. When the generator does not rely on $z$, under mild Lipschitz and integrability conditions, we prove existence and uniqueness of the solution to the interacting particle system for general reflections. We are able to consider the case where the generator depends on $z$ when the reflection is linear. In both cases, we obtain the convergence rate of solution to the interacting particle system towards the solution to the mean-field mean reflected BSDEs.

</details>

**问题**  
该报告聚焦于**平均场平均反射倒向随机微分方程（mean-field mean reflected BSDEs）**的数值逼近问题。这类方程同时具有平均场（生成元依赖解的分布）和平均反射（约束为 $E[h(t,Y_t)]\ge 0$）特征，其解已在理论层面被构造，但缺乏可行的数值方案。核心困难在于：约束与分布耦合，使得经典蒙特卡洛方法无法直接应用。报告旨在通过**交互粒子系统**逼近原方程的解，并建立**混沌传播（propagation of chaos）**的收敛速率。

**核心方法**  
构造一个 $N$ 维交互粒子系统，每个粒子满足一个带平均反射的多维 BSDE，其中经验分布替代真实分布。  
- **非线性反射**（生成元 $f$ 不依赖 $z$）：利用 Snell 包络方法处理常数生成元情形，再通过**压缩映射**在短时间区间上证明解的存在唯一性，并延拓至整个区间。  
- **线性反射**（$h(t,x)=ax+b$，生成元可依赖 $z$）：借助凸集反射理论（Gégout-Petit & Pardoux 1996）直接得到粒子系统的适定性。  
收敛速率的证明依赖于对 Wasserstein 距离的精细控制：在非线性反射下，利用 $h$ 的 $C^{1,2}_b$ 光滑性得到 $O(N^{-1/2})$ 或 $O(N^{-1/4})$ 的速率；在线性反射下，通过鞅表示和方差估计得到 $O(N^{-1/2})$ 的速率。

**与已有工作关系**  
已有工作包括 Briand et al. (2018) 的平均反射 BSDE、Djehiche et al. (2023) 的平均场反射 BSDE（约束为 $Y_t\ge l(t,Y_t,\mathcal{P}_{Y_t})$），以及 Briand & Hibon (2021) 对平均反射 BSDE 的混沌传播。本文的新颖之处在于：  
- 生成元同时依赖 $Y$ 和 $Z$ 的分布（平均场型），而 Djehiche et al. (2023) 的生成元不能依赖 $Z$ 的分布，且其约束为路径wise 形式，不能退化到本文的期望约束。  
- 本文的约束 $E[h(t,Y_t)]\ge 0$ 不要求 Lipschitz 常数的小性假设，而 Djehiche et al. (2023) 需要 $\gamma_1,\gamma_2$ 足够小。  
- 与 Briand & Hibon (2021) 相比，本文处理了平均场生成元，且在线性反射下允许 $f$ 依赖 $z$。

**主要贡献**  
1. 首次建立了**平均场平均反射 BSDE** 的混沌传播结果，为这类方程的数值计算提供了严格的理论基础。  
2. 在非线性反射下，证明了交互粒子系统的存在唯一性，并给出了显式的收敛速率（$O(N^{-1/2})$ 或 $O(N^{-1/4})$）。  
3. 在线性反射下，允许生成元依赖 $z$ 及其分布，同样得到了 $O(N^{-1/2})$ 的收敛速率，推广了已有结果。  
4. 方法上，结合 Snell 包络、压缩映射和 Wasserstein 距离估计，为更一般的分布依赖型反射 BSDE 的逼近提供了分析框架。


### 2. 超前信息的随机控制

**讲者**：Huilin Zhang（Shandong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
传统随机最优控制假设决策者仅能基于当前及历史信息（即自然滤子 $\mathcal{F}_t$）做出决策。然而，许多实际场景（如金融高频交易、在线广告投放、流行病干预）中，决策者可能提前获知部分未来随机扰动或状态信息，即“超前信息”（anticipative information）。这类信息打破了标准信息流的适应性条件，导致经典动态规划原理失效。本报告旨在解决：当决策者拥有关于未来随机性的部分超前知识时，如何系统性地定义并求解最优随机控制问题？

**核心方法**  
报告提出一种基于“信息分解”与“鞅表示”的框架。首先，将超前信息建模为一个与自然滤子正交的辅助滤子 $\mathcal{G}_t \supset \mathcal{F}_t$，并利用 Girsanov 变换或条件期望的迭代性质，将原超前信息控制问题转化为一个等价的标准控制问题，其中新噪声项被“吸收”为状态过程的一部分。具体地，通过引入一个“信息调整项” $\Delta_t$，将控制器的 admissible 策略空间重新参数化，使得最优控制律可通过求解一个修正的 Hamilton-Jacobi-Bellman (HJB) 方程得到，该方程中额外包含一个由超前信息引起的漂移修正项。

**与已有工作关系**  
已有文献主要关注“部分可观测”或“延迟信息”下的随机控制，而“超前信息”的研究相对零散，多局限于线性二次型（LQ）框架或特定噪声结构。本报告将问题推广至一般非线性扩散过程，并利用信息论中的“互信息率”概念刻画超前信息的价值。与经典的“anticipative stochastic control”相比，本工作不要求超前信息具有完全确定性，而是允许其以随机过程形式出现，从而更贴近实际。

**主要贡献**  
1. 建立了超前信息随机控制的一般数学框架，给出了信息流相容的 admissible 策略定义。  
2. 提出了基于信息分解的降维方法，将原问题转化为标准控制问题，并推导了修正 HJB 方程，为数值求解提供了理论基础。  
3. 通过若干经济与工程实例（如带前瞻性预测的库存管理、基于新闻情绪的资产配置），展示了超前信息对最优策略的显著影响，并量化了信息价值的上界。  
4. 为因果推断中“干预超前于观测”的设定提供了新的分析工具，拓展了随机控制与因果推理的交叉研究。


### 3. Quadratic Forward Backward Stochastic Differential Equations Driven by G-Brownian Motion

**讲者**：Peng Luo（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典正倒向随机微分方程（FBSDEs）在二次增长情形下已有成熟理论，但驱动噪声为G-布朗运动时，非线性期望带来的模型不确定性使得系数二次增长的处理极为困难。本报告旨在解决：在G-框架下，当漂移和扩散项关于对偶变量呈二次增长时，FBSDEs解的存在唯一性、正则性及其与非线性偏微分方程（PDE）的联系。

**核心方法**  
报告可能采用G-期望下的随机分析工具，包括G-Itô公式、G-鞅表示定理以及BMO（有界平均振荡）鞅理论。针对二次增长，关键技巧是引入指数变换将方程线性化，或利用连续性方法结合压缩映射原理，在适当的加权Sobolev空间中构造迭代序列。同时，通过G-框架下的非线性Feynman-Kac公式，将FBSDEs的解与全非线性抛物型PDE的粘性解对应，从而借助PDE的正则性理论反推随机解的性质。

**与已有工作关系**  
已有工作主要集中于G-布朗运动驱动的Lipschitz或线性增长FBSDEs（如Hu、Ji、Peng等人的成果），以及经典布朗运动下二次增长FBSDEs（如Kobylanski、Tehranchi等）。本报告将二者结合，首次在G-框架下处理二次增长，克服了G-期望非线性和二次增长双重困难，填补了该交叉领域的空白。

**主要贡献**  
1. 建立G-布朗运动驱动下二次增长FBSDEs解的存在唯一性定理，推广了经典结果到模型不确定环境。  
2. 揭示解与全非线性PDE粘性解之间的对应关系，为数值计算提供理论依据。  
3. 为金融中具有模型不确定性的衍生品定价（如波动率不确定下的二次风险度量）提供严格的数学基础。


## Dynamic Game and Particle Approximation

*7 月 13 日（周一） · 08:30-10:10 · Xijiang Room*  
*主办 IMS China · 组织 Lijun Bo（Xidian University） · 主持 Panpan Ren（City University of Hong Kong）*

### 1. Two-Time-Scale McKean-Vlasov Systems

**讲者**：Fuke Wu（Huazhong University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
McKean-Vlasov 系统描述大量弱相互作用粒子的平均场极限，其漂移和扩散系数依赖于自身分布。当系统内部存在快慢两种时间尺度（如部分粒子演化极快、部分极慢）时，经典的单时间尺度分析失效。本报告旨在建立 **Two-Time-Scale McKean-Vlasov 系统** 的严格数学框架，回答：快慢变量耦合下，慢变量的极限动力学是否仍由某个有效 McKean-Vlasov 方程刻画？快变量的遍历性如何影响慢变量的分布依赖？

**核心方法**  
讲者可能采用 **奇异摄动与平均化** 的路径：将系统写为快变量 $Y_t^\varepsilon$（时间尺度 $\varepsilon^{-1}$）与慢变量 $X_t^\varepsilon$ 的耦合 McKean-Vlasov SDE，其中 $\varepsilon \to 0$。关键步骤是：  
1. 证明对固定的慢变量路径，快变量在条件分布下具有唯一不变测度 $\mu^{X}$；  
2. 利用 **Kurtz 型平均化原理**，将慢变量的漂移和扩散系数关于 $\mu^{X}$ 取平均，得到极限方程：  
   $$ d\bar{X}_t = \bar{b}(\bar{X}_t, \mathcal{L}(\bar{X}_t)) dt + \bar{\sigma}(\bar{X}_t, \mathcal{L}(\bar{X}_t)) dW_t, $$  
   其中 $\bar{b}, \bar{\sigma}$ 为平均后的系数，$\mathcal{L}(\bar{X}_t)$ 表示分布。  
3. 借助 **McKean-Vlasov 的弱解唯一性** 与 **概率紧性** 论证收敛性。

**与已有工作关系**  
已有文献多关注单时间尺度 McKean-Vlasov 系统（如 Sznitman 1991）或经典多尺度扩散（如 Papanicolaou 1977）。本报告将多尺度思想引入分布依赖系统，需处理快变量不变测度对慢变量分布的依赖，以及平均化后系数仍保持分布依赖的闭环结构。这与传统多尺度随机微分方程（无分布依赖）有本质区别，也不同于有限维平均场博弈中的多尺度（如 Bardi 2012），后者通常假设快变量为独立同分布噪声。

**贡献**  
1. 首次严格建立 **Two-Time-Scale McKean-Vlasov 系统** 的平均化极限定理，给出收敛速率。  
2. 揭示快变量的遍历性如何“平滑”慢变量的分布依赖，为多尺度粒子系统（如神经集群、社会动力学）提供理论工具。  
3. 方法上，将 **耦合的 Fokker-Planck 方程** 与 **随机平均化** 结合，可能推广至非 Lipschitz 系数情形。


### 2. Mean Field Control with Poissonian Common Noise: A Pathwise Compactification Approach

**讲者**：Xiaoli Wei（Harbin Institute of Technology）

**对应论文**：Mean Field Control with Poissonian Common Noise: A Pathwise Compactification Approach · [arXiv:2505.23441](https://arxiv.org/abs/2505.23441) · 📖 [长篇精读](../../deep_reads/jcsds2026-2505.23441.md)

<details><summary>摘要（原文）</summary>

This paper contributes to the compactification approach to study mean-field control problems with Poissonian common noise. To overcome the lack of compactness and continuity issues caused by common noise, we exploit the point process representation of the Poisson random measure with finite intensity and propose a pathwise formulation in a two-step procedure by freezing a sample path of the common noise. In the first step, we establish the existence of optimal relaxed controls in the pathwise formulation as if common noise is absent, but with finite deterministic jumping times. The second step plays the key role in our approach, which is to aggregate the optimal solutions in the pathwise formulation over all sample paths of common noise and show that it yields an optimal solution in the original model. To this end, with the help of concatenation techniques, we first develop a pathwise superposition principle in the model with deterministic jumping times, drawing a relationship between the pathwise relaxed control problem and the pathwise measure-valued control problem. We then further bridge the equivalence among different problem formulations and verify that the constructed solution under aggregation is indeed optimal in the original problem.

</details>

**问题**  
带有公共噪声的均值场控制（MFC）问题中，公共噪声（通常为布朗运动）导致条件分布空间的非紧性与连续性缺失，使得经典紧化方法失效。现有处理布朗公共噪声的紧化方法需对噪声路径进行时空离散化，所得解仅为弱适应（weak MFE），无法保持对公共噪声滤子的适应性。本文聚焦于**泊松型公共噪声**（有限强度），其路径具有有限跳跃点，为发展无需离散化的紧化方法提供了新可能。

**核心方法**  
作者提出**路径紧化方法**，分两步构造最优松弛控制。第一步：固定一条公共噪声样本路径 $\omega_1$，将原问题转化为无公共噪声但带有确定跳跃时间的辅助模型，利用Skorokhod拓扑下的紧化论证（Proposition 3.9）证明存在最优路径松弛控制 $P^{\omega_1}_*$，并验证其对 $\omega_1$ 的可测性。第二步：通过**路径叠加原理**（Theorem 4.1-(ii)）建立路径松弛控制与路径测度值控制之间的等价关系，进而证明聚合 $P^{\omega_1}_*$ 得到的 $\bar{P}_*(d\omega,d\omega_1)=P^{\omega_1}_*(d\omega)P_1(d\omega_1)$ 是原问题的最优松弛控制（Theorem 4.1-(iii)）。关键工具包括Fokker-Planck方程、拼接技术（concatenation）以及有限强度泊松测度的点过程表示。

**与已有工作关系**  
已有MFC/MFG紧化方法（如Lacker [29]、Carmona et al. [13]）主要针对布朗公共噪声，需离散化噪声路径，所得解为弱适应。本文首次将紧化方法推广至泊松公共噪声，利用其有限跳跃特性，**无需离散化**，直接通过路径冻结与聚合保持对公共噪声滤子的适应性。与Bo et al. [6] 的随机最大值原理方法相比，本文提供了一种更通用的存在性框架。

**主要贡献**  
1. 提出针对泊松公共噪声的路径紧化方法，克服了紧性与连续性障碍，证明了最优松弛控制的存在性（Theorem 2.5）。  
2. 建立了路径叠加原理（Theorem 4.1-(ii)），首次在确定跳跃时间模型中连接了路径松弛控制与测度值控制，该结果独立于布朗噪声情形。  
3. 证明了原问题与路径公式的价值函数等价性（Theorem 4.1-(iii)），并得到严格控制的存在性（Corollary 2.6）。该方法为处理更复杂跳跃型公共噪声的均值场问题提供了新工具。


### 3. Controlled Particle Systems and Their Applications in Deep Learning

**讲者**：Huafu Liao（Dalian University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
深度学习中广泛使用的随机优化（如SGD）与采样方法（如Langevin dynamics）可视为粒子系统的演化，但传统方法缺乏对粒子间交互与外部控制的系统建模。当面临高维非凸目标、多模态分布或动态环境时，粒子系统容易陷入局部最优或收敛缓慢。本报告旨在回答：如何通过引入控制理论，设计受控粒子系统（Controlled Particle Systems），使其演化过程既能保持粒子多样性，又能高效逼近目标分布或损失景观，从而提升深度学习训练与推理的鲁棒性与效率。

**核心方法**  
讲者将粒子系统建模为随机微分方程（SDE）的集合，每个粒子的漂移项包含一个可学习的控制函数。该控制函数通过最小化一个与任务相关的代价泛函（如KL散度、泛化误差上界）来优化，形成“控制-粒子”耦合的变分问题。方法本质是将粒子系统的演化视为一个最优控制问题：控制输入调节粒子间的相互作用力（如排斥项保持多样性）与外部驱动力（如梯度下降方向），使得粒子分布沿指定路径逼近目标。求解时可能借助Pontryagin最大值原理或强化学习中的actor-critic框架，将控制函数参数化为神经网络，并通过伴随方法（adjoint method）计算梯度。

**与已有工作关系**  
已有工作包括：① 交互粒子系统（如mean-field Langevin dynamics）仅依赖固定交互核，缺乏自适应控制；② 神经ODE与扩散模型将粒子演化视为确定性或随机流，但未显式引入控制代价；③ 强化学习中的策略梯度方法可视为单粒子控制，但未利用粒子间信息。本报告将控制理论与粒子系统结合，统一了优化、采样与表示学习：相比传统粒子方法，控制函数可动态调整粒子行为；相比单智能体控制，粒子间的耦合提供了更丰富的探索信号。

**主要贡献**  
① 提出受控粒子系统的一般框架，将深度学习中的多种算法（SGD、Langevin采样、粒子滤波）纳入统一的最优控制视角；② 给出控制函数的存在性与最优性条件，并设计可扩展的数值求解方案（如基于score matching的近似）；③ 在深度生成模型（如扩散模型加速采样）与贝叶斯深度学习（如后验近似）中展示性能提升，为理论分析（如收敛速率、泛化界）提供新工具。该工作为统计与机器学习交叉领域开辟了“控制+粒子”的新研究方向。


### 4. Bi-Coupling Approach and its Applications

**讲者**：Panpan Ren（City University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在许多统计与机器学习任务中，耦合（coupling）是连接两个概率分布、构造随机变量对以最小化某种距离或控制误差的核心工具。然而，单一耦合往往在特定目标（如Wasserstein距离、总变差距离或收敛速度）上存在权衡：例如，optimal transport coupling能精确刻画Wasserstein距离但计算昂贵，而maximal coupling虽易采样却可能给出松弛的界。本报告提出的“Bi-Coupling Approach”旨在解决如何同时利用两种不同耦合的优势，在保持计算可行性的同时获得更紧的理论保证或更高效的算法。

**核心方法**  
Bi-Coupling Approach的核心思想是同时构造两个耦合：一个“粗耦合”（coarse coupling）用于快速近似或提供初始对齐，另一个“细耦合”（fine coupling）用于修正误差或实现精确控制。通过设计两个耦合之间的交互机制（如交替迭代、加权组合或条件采样），该方法能够在不显著增加计算负担的前提下，将两个耦合的优点融合。例如，在马尔可夫链蒙特卡洛（MCMC）的收敛诊断中，可先用maximal coupling快速生成候选对，再通过optimal transport coupling对局部区域进行精细调整，从而得到总变差距离的上下界。

**与已有工作关系**  
现有文献中，单耦合方法（如Wasserstein耦合、Doeblin耦合、反射耦合）已被广泛研究，但鲜有工作系统性地探讨如何组合多个耦合。Bi-Coupling Approach与“耦合不等式”（coupling inequality）和“多步耦合”（multi-step coupling）有联系，但后者通常只使用一个耦合的多次应用，而非同时维护两个不同性质的耦合。该方法也区别于“混合耦合”（mixture coupling），后者是将多个耦合随机混合，而本报告强调两个耦合的协同而非随机选择。

**贡献**  
本报告的主要贡献在于：（1）提出一个通用的双耦合框架，为分布比较、算法收敛分析和因果推断中的敏感性分析提供了新工具；（2）在若干典型应用（如高维正态分布的Wasserstein距离估计、贝叶斯后验的近似误差界）中展示了该框架如何获得比单耦合更紧的界或更快的收敛速度；（3）给出了双耦合构造的充分条件与理论性质，为后续研究奠定了分析基础。这一工作有望推动耦合方法在统计计算与因果推断中的进一步应用。


## Stein Method with Recent Advances

*7 月 13 日（周一） · 13:30-15:10 · Xijiang Room*  
*主办 IMS China · 组织 Zhonggen Su（Zhejiang University） · 主持 Zhonggen Su（Zhejiang University）*

### 1. Rank Deficiency of Bernoulli Random Matrices for Large k

**讲者**：Hanchao Wang（Shandong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
考虑一个 $n \times k$ 的 Bernoulli 随机矩阵 $\mathbf{M}$，其元素独立同分布于 $\text{Bernoulli}(p)$（$p \in (0,1)$ 固定）。当列数 $k$ 远大于行数 $n$ 时，矩阵以高概率满秩（秩为 $n$），但秩亏缺（$\text{rank}(\mathbf{M}) < n$）事件仍以指数小概率发生。本报告旨在刻画这一小概率事件的精确渐近行为：对于固定的 $n$ 和 $p$，当 $k \to \infty$ 时，秩亏缺概率 $\mathbb{P}(\text{rank}(\mathbf{M}) < n)$ 的衰减速率与主导项。

**核心方法**  
秩亏缺等价于存在一个非零向量 $\mathbf{v} \in \mathbb{R}^n$ 使得 $\mathbf{v}^\top \mathbf{M} = \mathbf{0}$，即所有 $k$ 列均落在 $\mathbf{v}$ 的正交补中。利用组合概率与线性代数，可将该事件分解为若干“小秩子矩阵”的并。核心工具是 **union bound** 与 **二阶矩方法**：先对每个可能的非零 $\mathbf{v}$（共 $2^n-1$ 个）计算其对应列向量全正交的概率 $[ \mathbb{P}(\mathbf{v}^\top \mathbf{X} = 0) ]^k$，其中 $\mathbf{X}$ 为单列 Bernoulli 向量；再通过精细的计数与概率估计，得到主导项来自 $\mathbf{v}$ 为稀疏向量（如仅含一个非零分量）的情形。最终导出 $\mathbb{P}(\text{rank}(\mathbf{M}) < n) \sim C \cdot \rho^k$，其中 $\rho = \max_{\mathbf{v} \neq \mathbf{0}} \mathbb{P}(\mathbf{v}^\top \mathbf{X} = 0) = \max\{p, 1-p\}^n$（当 $p \neq 1/2$ 时）或更复杂的表达式（当 $p=1/2$ 时需考虑对称性）。

**与已有工作关系**  
经典随机矩阵理论（如高斯、亚高斯情形）已证明满秩概率趋于 1 且指数衰减率可由小奇异值下界刻画，但 Bernoulli 矩阵的离散性导致秩亏缺事件具有组合本质。已有工作（如 Kahn–Komlós–Szemerédi 关于随机图邻接矩阵的秩）给出了 $n$ 固定时满秩概率的下界，但未给出精确指数。本报告填补了该空白：将问题转化为 **随机二分图** 的连通性（秩亏缺等价于存在孤立行或列结构），并利用大偏差技术得到精确指数，与随机图相变理论中的“次临界”行为相呼应。

**贡献**  
1. 首次给出固定 $n$、$k \to \infty$ 时 Bernoulli 随机矩阵秩亏缺概率的精确渐近公式，指数由 $p$ 和 $n$ 的简单函数决定。  
2. 揭示了秩亏缺的主导机制：当 $p \neq 1/2$ 时，主要来自全零列或全一列（对应 $\mathbf{v}$ 为单位向量）；当 $p=1/2$ 时，来自更复杂的线性约束，指数出现对数修正。  
3. 方法可推广至其他离散随机矩阵（如 Rademacher 矩阵），并为高维统计中“设计矩阵病态”的小概率事件分析提供新工具。


### 2. Rates of Convergence in the Distances of Kolmogorov and Wasserstein for Standardized Martingales

**讲者**：Xiequan Fan（Northeastern University at Qinhuangdao）

**对应论文**：Rates of convergence in the distances of Kolmogorov and Wasserstein for standardized martingales · [arXiv:2309.08189](https://arxiv.org/abs/2309.08189) · 📖 [长篇精读](../../deep_reads/jcsds2026-2309.08189.md)

<details><summary>摘要（原文）</summary>

We give some rates of convergence in the distances of Kolmogorov and Wasserstein for standardized martingales with differences having finite variances. For the Kolmogorov distances, we present some exact Berry-Esseen bounds for martingales, which generalizes some Berry-Esseen bounds due to Bolthausen. For the Wasserstein distance, with Stein's method and Lindeberg's telescoping sum argument, the rates of convergence in martingale central limit theorems recover the classical rates for sums of i.i.d.\ random variables, and therefore they are believed to be optimal.

</details>

**问题**  
该报告研究标准化鞅 $S_n/s_n$ 在 Kolmogorov 距离 $K(S_n/s_n)$ 与 Wasserstein 距离 $W(S_n/s_n)$ 下的收敛速率。已有结果多针对特定条件（如条件方差几乎必然等于无条件方差），且 Wasserstein 距离的收敛速率研究较少。报告旨在给出更一般的、可恢复最优速率的 Berry-Esseen 型界。

**核心方法**  
对于 Kolmogorov 距离，采用 Bolthausen 的引理将问题转化为对条件期望的泰勒展开估计，通过截断技巧处理鞅差分的尾部行为，并利用条件矩的界控制余项。对于 Wasserstein 距离，结合 Stein 方法与 Lindeberg 的 telescoping sum，构造辅助正态变量，将 Lipschitz 函数的期望差分解为可逐项估计的鞅差分和，最终得到显式常数界。

**与已有工作关系**  
报告推广了 Bolthausen (1982) 关于 Kolmogorov 距离的精确 Berry-Esseen 界（如 $n^{-1/4}$ 与 $n^{-1}\ln n$），去除了条件方差几乎必然相等的假设，并允许条件方差具有随机性。在 Wasserstein 距离方面，将 Röllin (2014) 的结果从三阶矩条件推广到 $2+\delta$ 阶矩，且改进了 Dedecker 等 (2022) 的界，使其在 i.i.d. 情形下达到最优速率（除对数因子外）。

**主要贡献**  
1. 建立了标准化鞅在 Kolmogorov 距离下的统一 Berry-Esseen 界，其形式依赖于条件方差与无条件方差的偏差以及矩条件，并证明该界在多种设定下是最优的（如 $n^{-\delta/(2+2\delta)}$ 与 $n^{-1/2}\ln n$）。  
2. 在 Wasserstein 距离下得到了与 i.i.d. 情形相同的最优收敛速率（$n^{-\delta/2}$ 与 $n^{-1/2}\ln n$），且常数显式。  
3. 将结果应用于随机环境中的分支过程，给出了 Lotka-Nagaev 估计量的 Berry-Esseen 界，展示了方法的实用性。


### 3. Refined Berry-Esseen Bounds under Local Dependence

**讲者**：Zhuosong Zhang（Southern University of Science and Technology）

**对应论文**：Refined Berry-Esseen bounds under local dependence · [arXiv:2602.02217](https://arxiv.org/abs/2602.02217) · 📖 [长篇精读](../../deep_reads/jcsds2026-2602.02217.md)

<details><summary>摘要（原文）</summary>

In this paper, we establish Berry--Esseen bounds for both self-normalized and non-self-normalized sums of locally dependent random variables. The proofs are based on Stein's method together with a concentration inequality approach. We develop a new class of concentration inequalities that extend classical results and achieve optimal convergence rates under more general dependence structures. As applications, we apply our main results to derive sharper Berry--Esseen bounds for graph dependency, distributed $U$-statistics, constrained $U$-statistics, and decorated injective homomorphism sums.

</details>

**问题**  
局部依赖随机变量的正态逼近是概率统计中的经典问题。已有工作（Chen & Shao, 2004）在条件 (LD1) 与 (LD2′) 下建立了 Berry–Esseen 界，但 (LD2′) 中邻域集 $B_i$ 过大，导致图依赖等场景下 Kolmogorov 距离的界无法匹配 Wasserstein 距离的最优阶。本文旨在更灵活的依赖结构 (LD1) 与 (LD2) 下，为和与自标准化和同时建立精细的 Berry–Esseen 界，并推广到多个重要统计量。

**核心方法**  
证明基于 Stein 方法与集中不等式途径。作者发展了一类新的随机化集中不等式（Proposition 4.5 与 4.6），通过递归构造处理局部依赖下的概率估计。关键技巧在于利用 (LD2) 中较小的 $A_{ij}$ 集，结合 Hölder 不等式与 Young 不等式，对 $\xi_A S_A^2$ 等矩进行精细控制（Lemma 4.4），从而在 Stein 方程中同时处理非自标准化与自标准化情形。自标准化部分还引入了截断函数 $\psi$ 以保证方差估计的稳定性。

**与已有工作关系**  
相比 Chen & Shao (2004) 与 Zhang (2024) 在 (LD2′) 下的结果，本文在 $\kappa$ 的指数上取得改进（例如图依赖中 $d$ 的幂次从 $5$ 降至 $2$）；相比 Eichelsbacher & Rednoß (2023) 的 Kolmogorov 界，本文的矩条件更弱（仅需四阶矩而非有界性）。对于分布式 $U$ 统计量，本文通过整体处理局部依赖结构，避免了 Chen & Peng (2021) 中分块误差累积问题，去除了 $k=O(N^a)$ 的限制。

**贡献**  
1. 在 (LD1) 与 (LD2) 下建立了非自标准化与自标准化和的 Berry–Esseen 界，收敛率在 $\kappa$ 与 $\tau$ 意义上达到最优。  
2. 发展了适用于局部依赖的随机化集中不等式，可作为独立工具用于其他逼近问题。  
3. 应用于图依赖、分布式 $U$ 统计量、约束 $U$ 统计量及装饰单射同态和，获得了比现有结果更优的收敛阶或更弱的矩条件，其中自标准化情形下的 Berry–Esseen 界为首次给出。


### 4. High-Dimensional Normal Approximations for Sums of Langevin Markov Chains

**讲者**：Xiaolin Wang（The Chinese University of Hong Kong）

**对应论文**：High-dimensional normal approximations for sums of Langevin Markov chains · [arXiv:2512.19496](https://arxiv.org/abs/2512.19496) · 📖 [长篇精读](../../deep_reads/jcsds2026-2512.19496.md)

<details><summary>摘要（原文）</summary>

Consider the well-known Langevin diffusion on $\mathbb{R}^d$ $$\mathrm{d} X_t = -\nabla U(X_t)\,\mathrm{d} t + \sqrt{2}\mathrm{d} B_t, $$ and its Euler-Maruyama discretization given by $$X_{k+1}=X_k-η\nabla U(X_k)+\sqrt{2η}ξ_{k+1},$$ where $η$ is the step size. Under mild conditions, the Langevin diffusion admits $π(\mathrm{d} x)\propto \exp(-U(x))\mathrm{d} x$ as its unique stationary distribution. In this paper, we mainly study the normal approximation of the normalized partial sum $$ W_n = η^{1/2} n^{-1/2} \left( \sum_{i=0}^{n-1} X_i- \int_{\mathbb{R}^d} x\,π(\mathrm{d} x) \right).$$ To the best of our knowledge, this work provides the first dimension-explicit convergence rates in high-dimensional settings. Our main tool is a novel upper bound for the 1-Wasserstein distance $W_1(W,γ)$ via the exchange pair approach, where $W$ is any random vector of interest and $γ$ is a $d$-dimensional standard normal random vector.

</details>

**问题**  
该报告聚焦于高维Langevin Markov链（即Langevin Monte Carlo算法）的归一化部分和  
\[
W_n = \eta^{1/2} n^{-1/2} \sum_{i=0}^{n-1} \bigl( X_i - \int x \pi(dx) \bigr)
\]  
的渐近正态性。在高维统计与采样问题中，理解LMC迭代的联合分布行为至关重要，但现有结果多限于一维或低维情形，缺乏显式的维度依赖收敛速率。本文旨在填补这一空白，给出$W_n$在1-Wasserstein距离下逼近标准正态的显式上界。

**核心方法**  
方法本质是**交换对（exchangeable pair）技术与Stein方法的结合**。首先将$W_n$分解为鞅部分$H_n$和余项$R_n$。对于鞅部分，构造一个特殊的交换对$(W_n, W_n')$及辅助变量$D$，使得$E[D \mid X] = \lambda W_n$，从而利用Stein方程得到$W_1(H_n, \gamma)$的上界。关键创新在于用$D$替换传统交换对中的$\delta$，简化了条件期望结构并降低了高阶项的量级。余项$R_n$则通过直接随机计算（利用梯度Lipschitz、强凸性及矩估计）进行控制。最终合并两部分得到$W_1(\Sigma^{-1/2}W_n, \gamma)$的界。

**与已有工作关系**  
已有工作如Lu et al. (2022)仅证明了LMC部分和的中心极限定理，未给出收敛速率；Fan et al. (2024)针对自归一化版本建立了Berry–Esseen界，但维度依赖不明确。本文首次在高维设定下提供**显式的维度依赖收敛速率**，且步长$\eta$与迭代次数$n$满足$n = \lfloor \eta^{-p} \rfloor$（$1<p<3$），覆盖了实际中常用的衰减步长情形。此外，在线性势函数（$\nabla U(x)=Ax$）的特例中，利用$W_n$可表示为独立高斯向量的加权和，得到了更优的2-Wasserstein速率，凸显了非线性带来的本质困难。

**主要贡献**  
1. 建立了一个通用的高维正态逼近定理（Theorem 3.2），通过交换对方法给出$W_1$距离的上界，其形式适用于一般依赖结构。  
2. 针对LMC算法，在势函数强凸、光滑且高阶导数有界的条件下，证明了  
\[
W_1(\Sigma^{-1/2}W_n, \gamma) \le C \bigl[ d^{5/2}((n\eta)^{-1/2} + n^{-1/2}d^{1/2}\log(nd) + \eta^{1/2}d^{1/2} + \eta^{3/2}n^{1/2}) \bigr],
\]  
其中$\Sigma$为渐近协方差矩阵。该界首次显式刻画了维度$d$的影响（$d^{5/2}$量级）。  
3. 在线性势函数情形下，进一步得到2-Wasserstein距离的$O(n^{1/p-1}d^{3/2})$速率，验证了方法的有效性并揭示了非线性带来的速率退化。  
这些结果为高维MCMC的统计推断（如置信区间构造、假设检验）提供了理论基础。


## Functional Inequalities and Related Topics

*7 月 13 日（周一） · 15:30-17:10 · Libo Room*  
*主办 IMS China · 组织 Lian Wu（Central South University） · 主持 Wangjun Yuan（Southern University of Science and Technology）*

### 1. Volume Asymptotics of Intersection and Difference of Schatten Balls

**讲者**：Qiang Zeng（Chinese Academy of Sciences）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维矩阵空间中，Schatten balls（即由 Schatten $p$-范数 $\|X\|_{S_p} = (\sum \sigma_i^p)^{1/p}$ 定义的球）是随机矩阵理论与高维统计中的基本对象。当维度 $n \to \infty$ 时，两个 Schatten balls 的交集与差集的体积如何渐近？这一问题直接关系到高维置信区域的构造、信号检测的几何解释以及非交换凸几何的极限行为。

**核心方法**  
报告可能借助 **large deviation principle (LDP)** 与 **convex geometry 的渐近体积公式**。具体而言，将 Schatten balls 视为 $\mathbb{R}^{n \times n}$ 中的凸体，利用其支撑函数与极体的对偶关系，将体积渐近转化为关于奇异值分布的变分问题。通过 **random matrix theory** 中 Marchenko–Pastur 律或 Wishart 矩阵的谱分布，推导出交集与差集体积的指数率（即 Minkowski 泛函的极限）。关键工具包括 **Gaussian isoperimetric inequality** 与 **Sanov 定理** 在矩阵空间中的推广。

**与已有工作关系**  
已有工作主要集中于欧氏球（$\ell_2$ 球）或 $\ell_p$ 球的体积渐近（如 Ball 1993, Schechtman & Schmuckenschläger 1997），以及 Schatten balls 的单个体积公式（如 Vershynin 2014）。但两个 Schatten balls 的交集与差集（尤其当中心不同或半径不同时）的渐近行为尚未被系统研究。本报告将经典凸几何结果推广到非交换的矩阵空间，并处理因奇异值非负性带来的技术困难。

**主要贡献**  
1. 给出两个 Schatten balls 交集与差集体积的精确指数率，揭示其与 Schatten 范数指数 $p$ 及维度 $n$ 的依赖关系。  
2. 建立 **Minkowski 泛函** 在矩阵凸体上的极限定理，为高维统计中基于 Schatten 范数的假设检验提供几何直观。  
3. 提供一种将随机矩阵谱分布与凸体渐近体积相结合的通用分析框架，可推广至其他 unitary invariant 范数球。


### 2. Noncommutative Functional Inequalities and Their Applications

**讲者**：Sijie Luo（Central South University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典泛函不等式（如Poincaré不等式、对数Sobolev不等式、传输不等式）在概率论与统计物理中刻画了测度的集中性与混合速率。然而，在非交换概率论（如算子代数、自由概率）中，随机变量替换为算子，测度替换为迹态，经典不等式无法直接移植。本报告旨在建立非交换框架下的泛函不等式，并探索其在量子信息、随机矩阵理论及高维统计中的应用，例如量子信道的 mixing time 估计、纠缠 witness 的构造等。

**核心方法**  
讲者可能采用非交换的 Dirichlet 形式与 Bakry-Émery 曲率条件，将经典分析中的梯度算子替换为非交换导数（如自由差分或量子导数）。通过引入非交换的 carré du champ 算子 $\Gamma(f,g) = \frac12(\Delta(fg) - f\Delta g - (\Delta f)g)$，并证明在特定非交换 Markov 半群下满足曲率下界 $\Gamma_2 \ge \kappa \Gamma$，从而导出非交换对数Sobolev不等式 $\tau(f^2 \log f^2) - \tau(f^2)\log\tau(f^2) \le \frac{2}{\kappa} \tau(|\nabla f|^2)$。此外，可能利用非交换的 Orlicz 空间与超压缩性技巧，将经典传输不等式推广为量子 Wasserstein 距离下的形式。

**与已有工作关系**  
经典泛函不等式在交换情形已臻成熟（如 Gross 的对数Sobolev不等式、Talagrand 的传输不等式）。非交换方向已有部分先驱工作：Voiculescu 的自由熵、Biane 的自由对数Sobolev不等式、Junge 等人的非交换 Poincaré 不等式。本报告的可能新意在于：1）将曲率条件系统引入非交换半群，统一已有零散结果；2）建立非交换的 HWI 不等式（熵- Wasserstein- 信息量），填补非交换最优传输理论中的空白；3）将不等式应用于非交换统计模型（如量子态估计的 minimax 风险界），此前多限于交换情形。

**贡献**  
主要贡献包括：1）提出一套非交换泛函不等式的统一框架，给出曲率与熵耗散的定量关系；2）证明若干新的非交换不等式（如非交换的 Talagrand 不等式），并给出显式常数；3）在量子信息中，利用这些不等式导出量子 Markov 半群的指数混合速率，并构造基于熵的纠缠判据；4）为高维随机矩阵的谱分布收敛速度提供非交换分析工具，可能推动自由概率与统计学的交叉。


### 3. 非交换索伯列夫不等式

**讲者**：Bang Xu（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典 Sobolev 不等式刻画了函数在 $L^p$ 范数与导数 $L^q$ 范数之间的嵌入关系，是 PDE 与几何分析的基础工具。在非交换框架下（如 von Neumann 代数、非交换 $L^p$ 空间），如何建立类似的 Sobolev 型不等式？具体而言，给定一个非交换微分结构（如非交换流形上的导数或量子 Markov 半群的生成元），能否对非交换函数（算子）的“梯度”范数给出其自身范数的上界估计？该报告旨在解决非交换背景下 Sobolev 不等式的存在性、形式与最优常数问题。

**核心方法**  
讲者可能利用非交换 $L^p$ 空间的插值理论与非交换微分学（如非交换 Riesz 变换、非交换 Hardy 空间）。核心思路是将经典 Sobolev 不等式中的导数替换为某个非交换微分算子 $d$（例如非交换流形上的 Dirac 算子或量子导数），并借助非交换测度（迹）定义 Sobolev 范数 $\|f\|_{W^{k,p}} = \|f\|_p + \|d^k f\|_p$。通过非交换 Calderón–Zygmund 理论或非交换 Littlewood–Paley 分解，建立 $L^p$ 范数与 $d$ 的 $L^p$ 范数之间的控制关系，从而得到形如 $\|f\|_{L^q} \leq C \|f\|_{W^{1,p}}$ 的嵌入不等式，其中 $1/p - 1/q = 1/n$ 的维度关系由非交换空间的“维度”参数替代。

**与已有工作关系**  
经典 Sobolev 不等式在欧氏空间与 Riemann 流形上已十分成熟。非交换情形的工作可追溯至非交换环面（noncommutative torus）上的 Sobolev 空间（如 Connes 的非交换几何框架），以及量子群上的类似结果。已有结果多针对特定非交换结构（如 $L^p$ 空间上的 Markov 半群生成元）。本报告可能推广至更一般的非交换微分流形或非交换测度空间，或给出更优的常数（如与经典情形一致的临界指数），并可能建立与 noncommutative Riesz transform 有界性的等价关系。

**贡献**  
1. 提出或证明了在某种非交换微分结构下的 Sobolev 不等式，填补了该框架下嵌入定理的空白。  
2. 给出了非交换 Sobolev 空间 $W^{k,p}$ 到 $L^q$ 的紧嵌入条件，为后续非交换 PDE 与几何分析提供工具。  
3. 可能揭示了非交换 Sobolev 不等式与经典情形在维度参数、临界指数上的异同，深化了对非交换空间几何性质的理解。  
4. 方法上可能发展了非交换 Littlewood–Paley 理论或非交换插值技巧，对非交换调和分析有独立价值。


### 4. 循环群上的对数索伯列夫不等式

**讲者**：Gan Yao（Harbin Institute of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
对数索伯列夫不等式（Logarithmic Sobolev inequality）是刻画函数熵与 Dirichlet 型之间关系的关键工具，在马尔可夫链混合时间、高维集中不等式及统计计算中具有核心地位。经典结果主要针对连续空间（如 $\mathbb{R}^n$）或紧黎曼流形，而离散情形（尤其是有限群）的研究相对零散。本报告聚焦于**循环群** $\mathbb{Z}_n$（或更一般的有限循环群），旨在建立该群上函数空间的对数索伯列夫不等式，并揭示其常数与群阶 $n$ 的显式依赖关系。

**核心方法**  
报告可能借助循环群的**傅里叶分析**结构：利用群上的特征标将函数分解为傅里叶系数，将熵与 Dirichlet 型转化为频域上的加权和。通过精细的调和分析技巧（如超压缩估计、热核的 Gaussian 型上界）或与**谱隙**（spectral gap）的耦合，推导出最优的 Sobolev 常数。另一可能路径是构造循环群上的**离散热半群**，并利用其与连续环面 $S^1$ 的逼近关系，通过离散化连续不等式得到离散版本。

**与已有工作关系**  
已有离散对数索列夫不等式主要针对一般图（如超立方体、乘积图）或 Cayley 图，其常数通常依赖于图的度数与直径。循环群作为最简单的 Cayley 图（度为 2 的环图），其特殊结构允许更精确的刻画。与连续环面 $S^1$ 上的经典 Gross 不等式相比，离散版本需处理高频截断与有限群带来的边界效应。报告可能填补循环群上**显式最优常数**的空白，并揭示其与 $n$ 的 $\log n$ 量级关系（类似连续情形中常数与维数的对数依赖）。

**贡献**  
1. 给出循环群上对数索伯列夫不等式的**最优常数**（或紧的上下界），明确其随 $n$ 增长的渐近行为。  
2. 提供一种可推广至一般交换群的傅里叶分析框架，为离散群上的泛函不等式研究提供新工具。  
3. 所得不等式可直接用于估计循环群上随机游走的**混合时间**（mixing time），并可能在高维统计中（如循环对称数据的集中不等式）产生应用。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)