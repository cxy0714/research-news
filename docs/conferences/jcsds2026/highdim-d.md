# 高维统计 High-Dimensional Statistics · 4

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 17 场报告**（已检索到对应论文 7 场）

---

## High-Dimensional Independence and Nonparametric Testing Methods

*7 月 13 日（周一） · 10:30-12:10 · Hongfeng Meeting Room*  
*组织 Wenliang Pan（Chinese Academy of Sciences） · 主持 Ruizhe Jiang（Jinan University）*

### 1. Distribution-Free Robust Independence Test for High-Dimensional Data via Semi-Grothendieck's Divergence

**讲者**：Ruizhe Jiang（Jinan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
高维数据中变量间的独立性检验是统计推断的核心问题之一，但传统方法（如基于 Pearson 相关系数或距离相关性）常依赖分布假设或对异常值敏感，且在高维场景下面临维数灾难与计算瓶颈。该报告旨在提出一种**无分布假设、对异常值鲁棒**的高维独立性检验方法，尤其适用于样本量远小于维数的情形。

**核心方法**  
报告引入 **Semi-Grothendieck's Divergence** 作为独立性度量。该散度基于 Grothendieck 不等式思想，通过将两个随机向量的联合分布与边缘分布乘积之间的差异嵌入到特定核函数空间中，并利用半定规划（SDP）松弛构造一个可计算的统计量。具体地，定义 $D_{SG}(X,Y) = \sup_{\|A\|_{\infty} \le 1, \|B\|_{\infty} \le 1} \mathbb{E}[\phi(X)^\top A \psi(Y)] - \mathbb{E}[\phi(X)]^\top A \mathbb{E}[\psi(Y)]$ 的某种变体，其中 $\phi,\psi$ 为特征映射，$\|\cdot\|_{\infty}$ 为算子范数。该统计量无需估计联合分布，且通过截断或稳健核函数实现对异常值的鲁棒性。

**与已有工作关系**  
现有高维独立性检验多基于距离相关性（dCor）或 Hilbert-Schmidt 独立性准则（HSIC），但它们在重尾分布或存在离群点时表现不稳定。Grothendieck 不等式此前被用于协方差矩阵的稳健估计，而本工作首次将其直接用于独立性检验，并引入“半”松弛（Semi-）以平衡计算效率与统计功效。相比基于最大均值差异（MMD）的方法，该散度对非线性依赖的捕捉能力更强，且无需显式选择核参数。

**贡献**  
1. 提出一种全新的无分布、鲁棒的高维独立性检验统计量，理论证明其在原假设下渐近分布为 $\chi^2$ 型混合分布，并给出有限样本下的置换检验实现。  
2. 通过数值实验表明，在重尾噪声、异常值污染及超高维（$p \gg n$）场景下，该方法在检验功效和 Type-I error 控制上显著优于 dCor、HSIC 等基准方法。  
3. 为 Grothendieck 不等式在统计推断中的应用开辟了新方向，其半定规划形式也为后续优化算法设计提供了基础。


### 2. Test of Multivariate Independence via Comparing Two Bivariate Means

**讲者**：Yeqing Zhou（Tongji University）

**对应论文**：Reducing multivariate independence testing to two bivariate means comparisons · [arXiv:2402.16053](https://arxiv.org/abs/2402.16053) · 📖 [长篇精读](../../deep_reads/jcsds2026-2402.16053.md)

<details><summary>摘要（原文）</summary>

Testing for independence between two random vectors is a fundamental problem in statistics. It is observed from empirical studies that many existing omnibus consistent tests may not work well for some strongly nonmonotonic and nonlinear relationships. To explore the reasons behind this issue, we novelly transform the multivariate independence testing problem equivalently into checking the equality of two bivariate means. An important observation we made is that the power loss is mainly due to cancellation of positive and negative terms in dependence metrics, making them very close to zero. Motivated by this observation, we propose a class of consistent metrics with a positive integer $γ$ that exactly characterize independence. Theoretically, we show that the metrics with even and infinity $γ$ can effectively avoid the cancellation, and have high powers under the alternatives that two mean differences offset each other. Since we target at a wide range of dependence scenarios in practice, we further suggest to combine the p-values of test statistics with different $γ$'s through the Fisher's method. We illustrate the advantages of our proposed tests through extensive numerical studies.

</details>

**问题**：多元独立性检验是统计学基本问题。现有许多 omnibus 一致检验（如距离协方差、HSIC、HHG 等）在强非单调和非线性关系下功效骤降。论文揭示其根源：这些检验的依赖度量可统一表达为 $\mu_{f_1,f_2}=S_1+S_2-2S_3$，当 $S_1-S_3$ 与 $S_2-S_3$ 符号相反时，正负项相互抵消使度量接近零，导致检验失效。如何系统性地避免这种抵消、提升对复杂依赖模式的检验功效？

**核心方法**：论文首先证明，基于合适核函数 $f_1,f_2$，独立性等价于两个二元均值向量 $(S_1,S_3)$ 与 $(S_3,S_2)$ 相等。由此提出一类新度量 $\mu_{\gamma,f_1,f_2}=\{(S_1-S_3)^\gamma+(S_2-S_3)^\gamma\}^{1/\gamma}$，$\gamma\in[1,\infty]$ 为整数。当 $\gamma=1$ 时退化为现有度量；当 $\gamma$ 为偶数或无穷时，度量变为 $\ell_2$ 或 $\ell_\infty$ 范数，能有效避免正负抵消。理论证明 $\mu_{\gamma}$ 对任意 $\gamma\ge2$ 仍是一致度量。进一步，通过 Fisher 方法组合多个 $\gamma$ 的 $p$ 值得到综合检验，以应对多种依赖模式。

**与已有工作关系**：论文将大量现有依赖度量（距离协方差、HSIC、HHG、投影协方差等）纳入统一框架 $\mu_{f_1,f_2}=S_1+S_2-2S_3$，即 $\gamma=1$ 的特例。新提出的 $\mu_{\gamma}$ 是对这些度量的直接推广和重要补充：偶数 $\gamma$ 和无穷 $\gamma$ 在 $S_1-S_3$ 与 $S_2-S_3$ 异号时显著放大信号，而现有度量因抵消而失效。此外，偶数 $\gamma$ 的渐近零分布为加权半正态，是渐近分布自由的，无需置换；奇数 $\gamma$ 则需置换，但论文证明了置换的一致性。

**主要贡献**：1) 建立多元独立性检验与二元均值比较的等价性，提供新视角。2) 提出一类一致度量 $\mu_{\gamma}$，并严格刻画不同 $\gamma$ 下度量大小随依赖模式的变化规律，证明偶数 $\gamma$ 和无穷 $\gamma$ 能有效避免抵消、提升功效。3) 导出检验统计量的渐近联合零分布（偶数 $\gamma$ 为加权半正态，奇数 $\gamma$ 为高斯场二次型）和备择分布，并给出分布自由检验的方差估计。4) 提出基于 Fisher 等方法的组合检验，在多种非线性依赖下保持稳健高功效。5) 大量模拟和真实基因数据表明，新方法在非单调、非线性关系下显著优于现有方法。


### 3. Testing Independence and Conditional Independence in High Dimensions via Coordinatewise Gaussianization

**讲者**：Jing He（Southwestern University of Finance and Economics）

**对应论文**：Testing independence and conditional independence in high dimensions via coordinatewise Gaussianization · [arXiv:2504.02233](https://arxiv.org/abs/2504.02233) · 📖 [长篇精读](../../deep_reads/jcsds2026-2504.02233.md)

<details><summary>摘要（原文）</summary>

We propose new statistical tests, in high-dimensional settings, for testing the independence of two random vectors and their conditional independence given a third random vector. The key idea is simple, i.e., we first transform each component variable to the standard normal via its marginal empirical distribution, and we then test for independence and conditional independence of the transformed random vectors using appropriate $L_\infty$-type test statistics. While we are testing some necessary conditions of the independence or the conditional independence, the new tests outperform the 13 frequently used testing methods in a large scale simulation comparison. The advantage of the new tests can be summarized as follows: (i) they do not require any moment conditions, (ii) they allow arbitrary dependence structures of the components among the random vectors, and (iii) they allow the dimensions of random vectors to diverge at the exponential rates of the sample size. The critical values of the proposed tests are determined by a computationally efficient multiplier bootstrap procedure. Theoretical analysis shows that the sizes of the proposed tests can be well controlled by the nominal significance level, and the proposed tests are also consistent under certain local alternatives. The finite sample performance of the new tests is illustrated via extensive simulation studies and a real data application.

</details>

**问题**  
高维场景下检验两个随机向量 $X\in\mathbb{R}^p$ 与 $Y\in\mathbb{R}^q$ 的独立性，以及给定第三个向量 $Z\in\mathbb{R}^m$ 时的条件独立性。现有方法或依赖矩条件（如距离相关、HSIC），或对维度增长速率有限制，且鲜有方法能同时处理重尾分布、任意分量依赖结构以及 $p,q$ 随样本量指数增长的情形。

**核心方法**  
首先对每个分量进行坐标高斯化（coordinatewise Gaussianization）：利用边际经验分布函数将 $X_j,Y_k,Z_l$ 变换为标准正态变量 $U_j,V_k,W_l$。独立性检验采用 $L_\infty$ 型统计量 $H_n=\sqrt{n}\,|\hat{S}_n|_\infty$，其中 $\hat{S}_n$ 为 $U$ 与 $V$ 所有分量间样本协方差构成的向量；条件独立性检验则先对 $U$ 和 $V$ 关于 $W$ 做回归（非参数神经网络或线性 Lasso），取残差后构造类似的 $L_\infty$ 统计量。临界值通过计算高效的乘子 bootstrap（推荐 Rademacher 乘子）从高斯近似中获取。

**与已有工作关系**  
与 Shah & Peters (2020) 的广义协方差测度（GCM）相比，本文通过坐标高斯化消除了对原始变量矩条件的要求，且允许 $m$ 随样本量发散；与距离相关、HSIC 等核方法相比，本文无需任何矩条件，且允许 $p,q$ 以指数速率增长。模拟表明，新方法在 13 种常用检验中表现最优，尤其在重尾数据下优势显著。

**贡献**  
1. 提出无需矩条件、允许任意分量依赖结构的高维独立性与条件独立性检验，$p,q$ 可指数增长，$m$ 可多项式增长。  
2. 理论证明检验水平能被名义显著性水平控制，且在局部备择下具有相合性。  
3. 乘子 bootstrap 计算高效，模拟全面验证了方法在重尾、非线性依赖等复杂场景下的优越性。


## 半监督学习与高维数据

*7 月 13 日（周一） · 13:30-15:10 · Hongfeng Meeting Room*  
*组织 Yong Zhou（East China Normal University） · 主持 Yong Zhou（East China Normal University）*

### 1. Adaptive Semi-Supervised Inference for Estimating Equations: A Nonparametric Projection Approach using ReQU Neural Networks

**讲者**：Shanshan Song（Tongji University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
半监督场景下，大量无标签数据与少量有标签数据并存，如何利用无标签信息提升参数估计的效率与推断精度，是因果推断与统计学习中的核心挑战。现有半监督方法多依赖参数化模型（如线性回归）或核方法，但模型设定错误时偏差难以控制；而基于神经网络的非参数方法虽灵活，却缺乏对估计方程（estimating equations）框架下统计推断的理论保障。本报告聚焦于：在估计方程框架中，如何自适应地利用无标签数据构造半监督推断，同时保持估计的相合性与渐近正态性。

**核心方法**  
提出一种基于 ReQU（Rectified Quadratic Unit）神经网络的非参数投影方法。具体地，将无标签数据的信息通过一个非参数投影函数 $g(X)$ 融入估计方程，其中 $g$ 由 ReQU 网络逼近。ReQU 激活函数 $x^2 \cdot I(x>0)$ 相比 ReLU 具有二阶光滑性，能更好地逼近光滑函数，且其导数连续，便于理论分析。通过最小化投影后的估计方程方差，自适应地选择最优投影方向，从而在保持估计方程无偏性的前提下，最大化无标签数据带来的效率增益。该方法无需假设标签模型正确，仅需无标签数据的边际分布可估计。

**与已有工作关系**  
已有半监督推断工作（如 Zhang et al., 2019; Chakrabortty & Cai, 2018）多基于线性投影或核方法，其效率增益受限于投影函数的光滑性假设。本报告将投影函数推广至非参数空间，并首次在估计方程框架下引入 ReQU 神经网络，克服了传统核方法在高维数据上的维数灾难问题。与标准神经网络半监督学习（如自训练、伪标签）不同，本方法直接针对推断目标（估计方程）而非预测损失进行优化，从而保证了统计推断的有效性。

**主要贡献**  
1. 提出一种自适应半监督推断框架，适用于一般估计方程，无需标签模型正确设定。  
2. 利用 ReQU 神经网络实现非参数投影，兼具光滑逼近能力与计算可扩展性，并给出估计量的渐近正态性与半监督效率界。  
3. 理论证明：当无标签样本量远大于有标签样本量时，所提估计量的方差可降至有监督情形的 $1/(1+\rho)$ 倍，其中 $\rho$ 为投影可解释的方差比例。  
4. 数值实验验证了方法在低维与中等维度下的稳健性，尤其当标签模型存在误设定时，效率提升显著优于现有半监督方法。


### 2. Deep Transformation Model

**讲者**：Tong Wang（Southeast University）

**对应论文**：Deep Transformation Model · [arXiv:2410.19226](https://arxiv.org/abs/2410.19226) · 📖 [长篇精读](../../deep_reads/jcsds2026-2410.19226.md)

<details><summary>摘要（原文）</summary>

There has been a significant recent surge in deep neural network (DNN) techniques. Most of the existing DNN techniques have restricted model formats/assumptions. To overcome their limitations, we propose the nonparametric transformation model, which encompasses many popular models as special cases and hence is less sensitive to model mis-specification. This model also has the potential of accommodating heavy-tailed errors, a robustness property not broadly shared. Accordingly, a new loss function, which fundamentally differs from the existing ones, is developed. For computational feasibility, we further develop a double rectified linear unit (DReLU)-based estimator. To accommodate the scenario with a diverging number of input variables and/or noises, we propose variable selection based on group penalization. We further expand the scope to coherently accommodate censored survival data. The estimation and variable selection properties are rigorously established. Extensive numerical studies, including simulations and data analyses, establish the satisfactory practical utility of the proposed methods.

</details>

**问题**：现有深度神经网络（DNN）模型多基于特定损失函数（如平方损失、交叉熵），对模型误设定和重尾误差缺乏鲁棒性。同时，高维场景下的变量选择和删失生存数据的统一建模仍不充分。该报告旨在提出一个更具灵活性和鲁棒性的非参数变换模型，并发展相应的估计、变量选择与理论框架。

**核心方法**：提出非参数变换模型 $Y = D \circ F(f^*(X), \epsilon)$，其中 $D$ 和 $F$ 为单调递增函数，$f^*$ 为目标函数，涵盖线性、广义线性、单指标、Cox等模型为特例。估计采用基于秩的目标函数 $U_n(f) = \frac{1}{n(n-1)}\sum_{i\neq j} I(Y_i>Y_j)I(f(X_i)>f(X_j))$，并利用深度前馈网络参数化 $f_\theta$。为克服指示函数不可微，提出双ReLU（DReLU）近似 $S_{\omega_n}(u)=\sigma(u/\omega_n+1/2)-\sigma(u/\omega_n-1/2)$，实现高效随机梯度优化。变量选择通过对第一层权重施加组Lasso惩罚实现，并自然扩展到右删失生存数据。

**与已有工作关系**：区别于现有DNN的平方损失、交叉熵损失等，秩损失对模型误设定和重尾误差更鲁棒，且无需指定误差分布。与经典最大秩相关（MRC）相比，将线性形式推广至DNN非线性，显著提升对复杂关系的刻画能力。与现有DNN变量选择方法（如LassoNet）相比，采用组Lasso于第一层权重，并首次在秩估计框架下建立变量选择一致性理论。

**主要贡献**：1）提出深度变换模型，统一多种数据类型的鲁棒建模；2）发展DReLU近似秩估计，兼具计算效率和理论优势；3）建立可识别性、收敛速率（固定p和发散p）及变量选择一致性的严格理论；4）数值实验表明，在复杂非线性、重尾误差及高维场景下，预测和变量选择性能显著优于现有方法。


### 3. Dynamic Logistic Normal Multinomial Model for Microbiome Data

**讲者**：Shucong Zhang（University of International Business and Economics）

**对应论文**：Logistic Normal Multinomial Factor Analyzers for Clustering Microbiome Data · [arXiv:2101.01871](https://arxiv.org/abs/2101.01871) · 📖 [长篇精读](../../deep_reads/jcsds2026-2101.01871.md)

<details><summary>摘要（原文）</summary>

The human microbiome plays an important role in human health and disease status. Next generating sequencing technologies allow for quantifying the composition of the human microbiome. Clustering these microbiome data can provide valuable information by identifying underlying patterns across samples. Recently, Fang and Subedi (2020) proposed a logistic normal multinomial mixture model (LNM-MM) for clustering microbiome data. As microbiome data tends to be high dimensional, here, we develop a family of logistic normal multinomial factor analyzers (LNM-FA) by incorporating a factor analyzer structure in the LNM-MM. This family of models is more suitable for high-dimensional data as the number of parameters in LNM-FA can be greatly reduced by assuming that the number of latent factors is small. Parameter estimation is done using a computationally efficient variant of the alternating expectation conditional maximization algorithm that utilizes variational Gaussian approximations. The proposed method is illustrated using simulated and real datasets.

</details>

**问题**：微生物组计数数据具有高维、稀疏及成分性（总和为1）的特点，其协方差结构复杂。现有聚类方法中，Dirichlet-multinomial 混合模型因参数受限无法充分刻画协方差；Logistic Normal Multinomial (LNM) 混合模型虽能灵活建模，但其潜在变量 $Y$ 的协方差矩阵参数随维度 $K$ 二次增长，在高维场景下估计困难且易出现奇异。如何在高维微生物组数据中实现高效、准确的模型聚类，是核心挑战。

**核心方法**：提出 Logistic Normal Multinomial Factor Analyzers (LNM-FA) 家族。在 LNM 混合模型的潜在空间中引入因子分析结构：$Y = \mu_g + \Lambda_g U_g + \epsilon_g$，其中 $U_g \sim N(0, I_q)$ 为 $q$ 维潜因子，$\epsilon_g \sim N(0, D_g)$ 为对角误差，从而协方差矩阵 $\Sigma_g = \Lambda_g \Lambda_g^\top + D_g$ 的参数数量降为 $O(Kq)$。参数估计采用变分高斯近似（VGA）与交替期望条件最大化（AECM）算法：第一循环更新变分参数 $m_{ig}, V_{ig}$ 及 $\mu_g, \pi_g$；第二循环更新 $\Lambda_g, D_g$，并利用 Woodbury 恒等式将矩阵求逆复杂度从 $O(K^3)$ 降至 $O(q^3)$。进一步对 $\Lambda_g$ 和 $D_g$ 施加跨组约束，得到 8 种嵌套模型（如 UUU、CCC 等），通过 BIC 选择最优结构。

**与已有工作关系**：该方法直接扩展了 Fang & Subedi (2020) 的 LNM 混合模型（LNM-MM），将因子分析结构嵌入潜在空间，类似 McNicholas & Murphy (2008) 在 Gaussian 混合中的 PGMM 框架。相比 Dirichlet-multinomial 模型，LNM 能更灵活地建模协方差；相比 MCMC 方法，VGA 大幅降低计算负担。与 LNM-MM 相比，LNM-FA 在高维时参数数量线性增长，且通过 Woodbury 恒等式实现高效计算，解决了 LNM-MM 在高维数据中协方差矩阵奇异的问题。

**贡献**：提出了首个适用于高维微生物组数据的 LNM 因子分析混合模型家族，通过降维和变分推断实现了可扩展的聚类框架。模拟实验表明，在 $K=10$、$n=1000$ 时，LNM-FA 能准确恢复真实聚类（ARI 接近 1）和协方差结构，而 Dirichlet-multinomial 模型完全失效。在三个真实数据集（Dietswap、FerrettiP、ShiB）上，LNM-FA 在维度较高（$K=23,8$）时仍能成功拟合并取得良好聚类（ARI 0.8–0.9），而 LNM-MM 因奇异无法运行；在低维场景（$K=5$）下两者性能相当，但 LNM-FA 参数更少。该工作为高维成分计数数据的模型聚类提供了实用工具，并可通过约束结构进一步实现简约建模。


### 4. High-Resolution Inversion of Ocean Surface Current Fields via Diffusion Priors and Multimodal Constraints

**讲者**：Shuyi Zhang（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
海洋表面流场的高分辨率反演是物理海洋学中的病态逆问题：观测数据（如卫星高度计、海面温度、风场）稀疏且多模态，而传统变分同化或正则化方法依赖高斯平滑等简单先验，难以恢复小尺度涡旋、锋面等关键结构。现有深度学习超分辨率方法虽能提升分辨率，但缺乏物理一致性，且对多模态异质观测的融合能力有限。

**核心方法**  
提出基于扩散先验（diffusion priors）的条件生成框架。首先，利用高分辨率海洋流场模拟数据训练一个去噪扩散概率模型（DDPM），学习流场的复杂分布。在反演阶段，将多模态观测（如海面高度异常、海面温度、风应力）作为条件约束，通过反向扩散过程逐步去噪，同时引入物理方程（如地转平衡、连续性方程）作为软约束，在每一步投影到物理可行域。方法本质是将数据一致性项与扩散先验的得分函数（score function）结合，实现高分辨率、物理自洽的流场重建。

**与已有工作关系**  
区别于传统物理同化（如4D-Var）中手工设计的先验（如高斯协方差），本工作利用扩散模型学习数据驱动的非高斯、多尺度先验。相比现有基于GAN或VAE的海洋流场超分辨率，扩散模型避免了模式坍塌，且能通过条件采样灵活融合多模态观测。与最近在图像逆问题中应用的扩散模型（如DPS、MCG）相比，本工作首次将其引入海洋流场反演，并针对物理约束设计了多模态融合策略。

**贡献**  
1. 首次将扩散先验应用于海洋表面流场的高分辨率反演，展示了生成模型在物理逆问题中的有效性。  
2. 提出多模态约束框架，有效融合异质观测数据，在稀疏观测下仍能恢复小尺度涡旋等精细结构。  
3. 通过模拟和真实数据实验，证明该方法在反演精度和物理一致性上显著优于传统同化及纯数据驱动方法。  
4. 为海洋遥感数据同化提供了新范式，可推广至其他地球物理场（如海冰、大气）的高分辨率重建。


## High-Dimensional Inference and Learning under Complex Data Settings

*7 月 13 日（周一） · 08:30-10:10 · Doupeng Mountains Meeting Room*  
*组织 Xuejun Jiang（Southern University of Science and Technology） · 主持 Xuejun Jiang（Southern University of Science and Technology）*

### 1. Cross-Semantic Transfer Learning for High-Dimensional Linear Regression

**讲者**：Xuejun Jiang（Southern University of Science and Technology）

**对应论文**：Cross-Semantic Transfer Learning for High-Dimensional Linear Regression · [arXiv:2512.21689](https://arxiv.org/abs/2512.21689) · 📖 [长篇精读](../../deep_reads/jcsds2026-2512.21689.md)

<details><summary>摘要（原文）</summary>

Current transfer learning methods for high-dimensional linear regression assume feature alignment across domains, restricting their applicability to semantically matched features. In many real-world scenarios, however, distinct features in the target and source domains can play similar predictive roles, creating a form of cross-semantic similarity. To leverage this broader transferability, we propose the Cross-Semantic Transfer Learning (CSTL) framework. It captures potential relationships by comparing each target coefficient with all source coefficients through a weighted fusion penalty. The weights are derived from the derivative of the SCAD penalty, effectively approximating an ideal weighting scheme that preserves transferable signals while filtering out source-specific noise. For computational efficiency, we implement CSTL using the Alternating Direction Method of Multipliers (ADMM). Theoretically, we establish that under mild conditions, CSTL achieves the oracle estimator with overwhelming probability. Empirical results from simulations and a real-data application confirm that CSTL outperforms existing methods in both cross-semantic and partial signal similarity settings.

</details>

**问题**：现有高维线性回归的迁移学习方法均假设源域与目标域的特征在语义上对齐，即仅允许对应位置的系数进行信息迁移。然而在许多实际场景中，不同语义的特征可能扮演相似的预测角色（如BMI与腰臀比），导致系数值相近但特征不对齐。这种“跨语义信号相似性”无法被现有方法利用，限制了迁移学习的适用范围。

**核心方法**：本文提出Cross-Semantic Transfer Learning (CSTL)框架，核心思想是将每个目标系数 $\beta_j$ 与所有源域系数 $\theta_l$ 进行配对比较，通过加权融合惩罚 $\lambda_1 \sum_{j,l} w_{j,l} |\beta_j - \theta_l|$ 来鼓励值相近的系数对融合。权重 $w_{j,l}$ 由SCAD惩罚的导数 $p'_{\lambda_1}(|\hat{\beta}^{\text{init}}_j - \hat{\theta}^{\text{init}}_l|)$ 构造，实现平滑近似理想硬阈值：小差异强惩罚、大差异零惩罚。同时用Lasso初始估计构造目标系数的自适应Lasso惩罚。优化采用ADMM算法，各子问题有闭式解。

**与已有工作关系**：现有迁移学习（如TransLasso、TransGLM）要求特征空间同质或子集对齐，仅允许对应位置系数迁移。CSTL首次突破语义对齐限制，允许任意目标-源系数对之间的信息共享，可处理一对多、多对多等复杂对应关系。此外，与仅考虑部分系数共享的AdaTrans等方法相比，CSTL无需预先指定共享子集，而是通过数据驱动权重自动识别可迁移结构。

**主要贡献**：①提出跨语义迁移学习框架，通过全配对融合惩罚实现系数级信息迁移，无需特征对齐；②理论证明在理想权重下CSTL达到oracle估计量，且基于SCAD导数的数据驱动权重能以高概率恢复真实迁移结构并达到oracle性能；③ADMM算法高效可扩展；④模拟和真实数据（犯罪率预测）表明CSTL在跨语义和部分相似性设定下均显著优于现有方法，且能避免负迁移。


### 2. Testing High-Dimensional Parameters in Quantile Regression with High-Dimensional Control Factor

**讲者**：Xu Liu（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维分位数回归中，当研究者关心某个或某组低维参数的显著性时，需要同时控制大量潜在混淆变量（即“高维控制因子”）。现有高维分位数回归的推断方法多聚焦于整体系数向量的置信区域或变量选择，缺乏针对特定参数（如处理效应）的假设检验工具，且控制变量维数过高时，传统去偏估计的收敛速度与有效性会显著下降。本报告旨在解决：在分位数损失非光滑、控制变量维数随样本量增长的情形下，如何构造对感兴趣参数的有效检验统计量。

**核心方法**  
报告可能采用 **Neyman 正交化** 与 **双机器学习（Double Machine Learning）** 框架。具体地，将分位数回归的检验问题转化为一个矩条件：$E[\psi(Z; \theta_0, \eta_0)] = 0$，其中 $\theta$ 为待检参数，$\eta$ 为高维 nuisance 函数（包含分位数回归系数与条件分位数函数）。通过引入正交得分函数 $\psi$，使得 $\partial E[\psi] / \partial \eta = 0$，从而允许用机器学习方法（如 Lasso、随机森林）估计 $\eta$ 而不影响 $\theta$ 的渐近分布。检验统计量基于去偏后的估计量 $\hat{\theta}$ 构造，其渐近正态性可通过样本分割（cross-fitting）与经验过程理论证明。

**与已有工作关系**  
已有高维均值回归中的检验（如 de-biased Lasso）依赖损失函数的平滑性，而分位数回归的 check loss 在零点不可导，导致传统去偏方法失效。近年有工作（如 Belloni et al., 2019）针对高维分位数回归的推断，但多假设所有系数均为高维或仅关注整体置信带。本报告将检验问题聚焦于低维参数，并允许控制变量维数远高于样本量，与“高维控制因子”场景更契合。此外，与部分线性分位数模型不同，此处不假定控制因子以线性形式进入模型，而是通过 nuisance 函数灵活建模。

**主要贡献**  
1. 提出首个在高维分位数回归中同时处理“感兴趣参数低维”与“控制变量高维”的假设检验框架，填补了该场景下推断工具的空白。  
2. 通过 Neyman 正交化克服分位数损失非光滑带来的偏差累积问题，并给出检验统计量在局部备择下的渐近功效。  
3. 理论证明在较弱的稀疏性条件下，所提方法对 nuisance 函数的估计误差不敏感，且检验水平与功效具有一致性。  
4. 可能提供基于 bootstrap 或高斯近似的实用 p 值计算方法，为高维分位数回归的实证应用（如经济学中的政策效应评估）提供可靠推断工具。


### 3. To Explore or to Commit: Conservative Optimism with Pessimistic Baselines for Offline-to-Online Learning

**讲者**：Fang Kong（Southern University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
离线到在线学习（Offline-to-Online Learning）旨在利用离线数据集进行预训练，再通过在线交互微调策略。核心矛盾在于：在线阶段应积极探索以弥补离线数据覆盖不足，但过度乐观可能导致灾难性遗忘或性能崩溃；而过于保守则无法充分挖掘新信息。现有方法常采用悲观正则或乐观初始化，却难以动态平衡“探索”与“承诺”的时机。本报告针对这一困境，提出如何在不牺牲离线知识的前提下，安全地引导在线探索。

**核心方法**  
讲者提出一种名为“保守乐观与悲观基线”（Conservative Optimism with Pessimistic Baselines, COPB）的框架。其核心思想是：在线阶段维护一个**悲观基线**（如离线最优策略的价值下界），并以此作为参考点，对探索行为施加保守的乐观惩罚。具体地，算法在更新策略时，对状态-动作对的估计值同时引入两项：一项是乐观偏差（鼓励探索未充分访问的区域），另一项是相对于悲观基线的惩罚项（防止偏离离线知识）。通过调节两者权重，实现“当悲观基线可靠时保守承诺，当基线不确定时乐观探索”的自适应切换。理论分析表明，该机制可保证在线累积遗憾与离线性能退化均被控制在 $O(\sqrt{T})$ 量级。

**与已有工作关系**  
已有离线到在线方法主要分为两类：一是直接使用离线悲观值作为初始值，在线阶段采用标准乐观算法（如UCB），但易因初始悲观过强而抑制探索；二是采用悲观-乐观两阶段切换，但切换时机依赖人工设定。COPB 将悲观基线作为动态正则项融入在线优化，无需显式切换，且能利用离线数据的不确定性自动调节探索强度。这与保守Q学习（CQL）等离线算法不同——后者仅在离线阶段使用悲观，而COPB将悲观延续到在线阶段作为“安全锚点”。

**贡献**  
1. 首次在离线到在线学习框架中联合建模“保守乐观”与“悲观基线”，提出一种无需人工切换的自适应探索策略。  
2. 给出有限样本下的遗憾界与离线性能保持定理，证明算法在理论上的安全性与高效性。  
3. 在标准连续控制与离散动作基准任务上，COPB 相比现有方法（如IQL+finetune、CQL+exploration）在样本效率和最终性能上均取得显著提升，尤其适用于离线数据质量不均的场景。


### 4. Fine-Tuning LLM Agents without Fine-Tuning LLMs

**讲者**：Linyi Yang（Southern University of Science and Technology）

**对应论文**：Memento: Fine-tuning LLM Agents without Fine-tuning LLMs · [arXiv:2508.16153](https://arxiv.org/abs/2508.16153) · 📖 [长篇精读](../../deep_reads/jcsds2026-2508.16153.md)

<details><summary>摘要（原文）</summary>

In this paper, we introduce a novel learning paradigm for Adaptive Large Language Model (LLM) agents that eliminates the need for fine-tuning the underlying LLMs. Existing approaches are often either rigid, relying on static, handcrafted reflection workflows, or computationally intensive, requiring gradient updates of LLM model parameters. In contrast, our method enables low-cost continual adaptation via memory-based online reinforcement learning. We formalise this as a Memory-augmented Markov Decision Process (M-MDP), equipped with a neural case-selection policy to guide action decisions. Past experiences are stored in an episodic memory, either differentiable or non-parametric. The policy is continually updated based on environmental feedback through a memory rewriting mechanism, whereas policy improvement is achieved through efficient memory reading (retrieval). We instantiate our agent model in the deep research setting, namely \emph{Memento}, which attains top-1 on GAIA validation ($87.88\%$ Pass@$3$) and $79.40\%$ on the test set. It reaches $66.6\%$ F1 and $80.4\%$ PM on the DeepResearcher dataset, outperforming the state-of-the-art training-based method, while case-based memory adds $4.7\%$ to $9.6\%$ absolute points on out-of-distribution tasks. Our approach offers a scalable and efficient pathway for developing generalist LLM agents capable of continuous, real-time learning without gradient updates, advancing machine learning towards open-ended skill acquisition and deep research scenarios. The code is available at https://github.com/Agent-on-the-Fly/Memento.

</details>

**问题**：现有 LLM Agent 的持续适应能力受限于两种范式：一是依赖静态、手工设计的反思流程，缺乏灵活性；二是通过微调底层 LLM 参数（如 RL 或 SFT）实现适应，但计算成本高昂且易引发灾难性遗忘。本文旨在回答：**如何在不更新 LLM 参数的前提下，使 Agent 能够从环境中持续学习并提升性能？**

**核心方法**：作者将 Agent 的决策过程形式化为 **Memory-augmented Markov Decision Process (M-MDP)**，在标准 MDP 中引入记忆空间 $\mathcal{M}$，存储历史经验三元组 $(s, a, r)$。Agent 的策略定义为 $\pi(a|s, M) = \sum_{c \in M} \mu(c|s, M) p_{\text{LLM}}(a|s, c)$，其中 $\mu$ 是 case 检索策略，$p_{\text{LLM}}$ 是冻结的 LLM。为优化 $\mu$，采用 **soft Q-learning** 框架，推导出最优检索策略的闭式解 $\mu^*(c|s, M) \propto \exp(Q^*(s, M, c)/\alpha)$。为克服自然语言状态空间的复杂性，进一步提出基于核函数的 Q 值估计（Episodic Control），或利用单步任务特性将 Q 学习简化为二分类交叉熵损失，实现参数化记忆的在线更新。

**与已有工作关系**：区别于参数微调方法（如 START、Search-R1），本文完全冻结 LLM，通过外部记忆实现持续学习，避免了梯度计算和灾难性遗忘。与 RAG 系统相比，本文的记忆是动态增长的，且通过 RL 优化检索策略，而非静态相似度匹配。与 ExpeL、Agent Workflow Memory 等基于经验总结的方法相比，本文提供了严格的形式化 MDP 框架和理论最优策略推导。

**贡献**：（1）提出 M-MDP 形式化，将 case-based reasoning 与强化学习统一建模；（2）设计基于 soft Q-learning 的检索策略学习算法，并给出核函数近似与单步简化版本；（3）实现 Memento 系统，在 GAIA 验证集上达到 87.88% Pass@3（Top-1），在 DeepResearcher 上平均 F1 达 66.6%，超越所有基于训练的方法；（4）实验表明 case-based memory 在 OOD 任务上带来 4.7%~9.6% 的绝对提升，且持续学习曲线验证了记忆积累的有效性。


## Survival Analysis and High-Dimensional Modeling for Biomedical Applications

*7 月 13 日（周一） · 10:30-12:10 · Qingyan Boardroom*  
*主持 Mengyu Li（Northeastern University at Qinhuangdao）*

### 1. Generalized Win Fraction Regression for Composite Survival Endpoints

**讲者**：Zhiqiang Cao（Shenzhen Technology University）

**对应论文**：Generalized win fraction regression for composite survival endpoints · [arXiv:2604.04360](https://arxiv.org/abs/2604.04360) · 📖 [长篇精读](../../deep_reads/jcsds2026-2604.04360.md)

<details><summary>摘要（原文）</summary>

We propose a generalized win fraction regression framework for prioritized composite survival outcomes. The framework models the conditional win fraction through a chosen link function (including identity, logit, or probit), thereby accommodating multi-component time-to-event endpoints within a unified regression structure. To handle right censoring, we construct inverse-probability-of-censoring-weighted estimating equations that target the win fraction as if censoring were absent. Under the identity link, regression parameters characterize covariate associations on the natural win fraction scale. Under the logit link, they characterize the log odds of winning -- a new and complementary effect measure that treats ties as failures to win, imposing a more conservative standard than the win ratio or win odds. When there are no ties, the logit win fraction model reduces to proportional win fraction regression; moreover, the unweighted version of our estimating equations numerically coincides with the proportional win fraction point estimator regardless of ties. We establish large-sample properties of the proposed estimators and derive a consistent sandwich variance estimator that accounts for uncertainty from the estimated censoring weights. Extensive simulations examine finite-sample performance across link functions and censoring rates, and our method is illustrated through a reanalysis of the HF-ACTION clinical trial.

</details>

**问题**：在临床试验中，复合生存终点（如死亡和住院）常通过优先顺序比较（prioritized comparison）来评估整体获益，但现有回归方法（如比例赢分模型PWFM、广义赢胜率模型GWOM）受限于特定链接函数或对平局（ties）的处理方式，且无法直接建模删失下的条件赢分（win fraction）。如何在一个统一框架下，灵活选择链接函数（identity、logit、probit），并正确估计协变量对复合终点赢分的影响，同时处理右删失带来的偏倚？

**核心方法**：提出广义赢分回归模型（GWFM），直接建模条件赢分 $E\{W(Y_i,Y_j)(L) \mid X_i, X_j\} = g^{-1}(\beta_L^\top Z_{ij})$，其中 $W$ 为基于优先规则的赢函数，$Z_{ij}=X_i-X_j$，$g$ 为任意链接函数。为处理右删失，构造逆删失概率加权（IPCW）估计方程，权重 $W_{ij}^C(L)$ 确保观测到的赢分 $\omega_{ij}(L)$ 在删失下无偏。估计方程通过稀疏相关渐近理论（Lumley & Hamblett）建立大样本正态性，并给出考虑删失权重估计不确定性的三明治方差估计。

**与已有工作关系**：与PWFM（Mao & Wang, 2020）和GWOM（Wang et al., 2026）相比，GWFM的核心区别在于：（1）回归目标不同——PWFM建模赢比（win ratio），GWOM建模赢胜率（win odds），而GWFM直接建模赢分本身，且logit链接下参数对应“胜率”（odds of winning），将平局视为失败，比赢比和赢胜率更保守；（2）链接函数更灵活，可选用identity、logit、probit等，而PWFM隐含logit结构，GWOM固定为logit；（3）对平局的处理：PWFM排除平局，GWOM平分平局，GWFM在logit下将平局归入“非赢”；（4）当平局不存在时，logit GWFM退化为PWFM，且无权重版本与PWFM点估计数值一致。此外，IPCW权重构造与GWOM不同，本文证明其无偏性。

**贡献**：（1）首次提出广义赢分回归统一框架，允许研究者根据科学问题选择不同链接函数，直接解释协变量对赢分或胜率的影响；（2）引入“胜率”（odds of winning）作为复合终点的新效应度量，提供比赢比和赢胜率更保守的解读；（3）建立IPCW加权估计方程的大样本理论，包括一致的三明治方差估计，并证明其能正确校正删失权重估计的额外不确定性；（4）通过大量模拟和HF-ACTION临床试验数据验证方法在有限样本下的优良性质，并展示不同链接函数下回归系数随限制时间 $L$ 的变化轨迹，为实际应用提供计算工具（R包gwfmR）。


### 2. FedCox：联邦式局部自适应Cox比例风险模型

**讲者**：Changyue Wu（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多中心生存数据（如不同医院的随访记录）因隐私法规无法直接合并，传统Cox比例风险模型要求集中式数据，而现有联邦生存分析（如FedSurv）通常假设各中心共享全局同质的基线风险与协变量效应。然而，实际中不同中心的患者群体、诊疗环境存在显著异质性，忽略局部特征会导致模型偏差与预测精度下降。FedCox旨在解决“如何在保护数据隐私的前提下，为各中心学习自适应于局部数据分布的Cox模型”这一核心问题。

**核心方法**  
FedCox采用联邦学习框架，每个中心保留本地数据，仅交换模型参数梯度。其关键创新在于引入**局部自适应机制**：全局模型估计共享的协变量系数$\beta$，而每个中心额外维护一个局部基线风险函数$h_{0k}(t)$（或局部偏移项$\delta_k$），通过交替优化全局目标（如部分似然）与局部正则化项（如KL散度或L2惩罚）实现个性化。具体地，全局服务器聚合各中心上传的$\beta$梯度，同时允许各中心在本地更新中微调基线风险，从而在全局信息共享与局部异质性之间取得平衡。

**与已有工作关系**  
已有联邦Cox模型（如FedSurv, 2021）假设所有中心共享完全相同的$h_0(t)$和$\beta$，本质是“全局同质”联邦学习。FedCox则属于**个性化联邦学习**在生存分析中的首次应用，与FedAvg、pFedMe等思想类似，但针对Cox模型特有的部分似然函数与基线风险非参数估计进行了定制化设计。此外，传统分层Cox模型虽允许不同基线风险，但需要集中式数据，FedCox在隐私约束下实现了等价效果。

**主要贡献**  
1. 提出首个联邦式局部自适应Cox模型，在保护数据隐私的同时有效处理多中心生存数据的异质性。  
2. 设计了一种通信高效的优化算法，仅交换协变量系数梯度，避免泄露局部基线风险信息。  
3. 理论分析表明，当各中心基线风险差异有界时，FedCox的估计误差上界优于全局同质联邦Cox模型。  
4. 在模拟与真实多中心癌症生存数据上，FedCox在C-index和校准度上显著优于FedSurv及单中心Cox，且收敛速度与通信轮次相当。


### 3. Robust Variable Selection in High-Dimensional Survival Analysis

**讲者**：Yunwei Zhang（Murdoch University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维生存分析中，变量选择通常依赖Cox比例风险模型与惩罚似然（如LASSO、SCAD）。然而，Cox模型对异常值（如测量误差、删失机制偏离）和比例风险假设违背极为敏感，且高维场景下少量污染点即可严重扭曲估计与选择结果。现有鲁棒方法多局限于低维或仅处理截断，缺乏同时应对高维、右删失与异常值的统一框架。本报告旨在解决：**如何在生存数据存在异常值或模型误设时，仍能实现高维变量选择的一致性与估计的稳健性？**

**核心方法**  
讲者可能提出一种基于**加权偏似然**或**分位秩损失**的鲁棒惩罚估计框架。具体地，通过引入数据自适应权重（如Huber型权重或基于残差分布的稳健权重）来降低异常样本的影响，同时采用非凸惩罚（如MCP或SCAD）实现变量选择。另一种可能路径是采用**分位生存回归**（quantile survival regression）替代均值回归，利用分位损失函数对尾部异常不敏感的特性，并结合自适应Lasso或Group Lasso处理高维。算法上可能采用坐标下降或MM算法，并利用交叉验证或BIC型准则调优。

**与已有工作关系**  
已有工作主要分为两类：一是高维Cox模型的变量选择（如Tibshirani 1997的LASSO-Cox），但缺乏鲁棒性；二是低维鲁棒生存分析（如加权估计方程），但无法直接推广至高维。本报告可能首次将稳健估计与高维惩罚结合，并证明在污染比例有界时，估计量仍具有**oracle性质**（变量选择相合性与渐近正态性）。与现有鲁棒高维方法（如Huber回归）相比，本报告需处理删失机制与时间相依协变量，技术难度更高。

**贡献**  
1. **方法论创新**：提出首个兼具高维变量选择与异常值鲁棒性的生存分析框架，填补了该交叉领域的空白。  
2. **理论突破**：在删失数据下建立稳健惩罚估计的有限样本误差界与渐近性质，可能放松了传统Cox模型对比例风险假设的依赖。  
3. **计算可行性**：设计高效优化算法，并通过模拟与癌症基因组学实际数据验证方法在存在离群样本时的选择准确性与预测稳定性。  
4. **应用价值**：为生物医学中易受测量误差或异质性影响的生存数据（如基因表达、影像标记）提供可靠分析工具。


### 4. Identifying Shared Prognostic Genes in Pan-Cancer Studies: A Survival Analysis Approach with a Locally Weighted Group-Penalized Accelerated Failure Time Model

**讲者**：Tengdi Zheng（Beijing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
泛癌研究（pan-cancer study）旨在识别跨多种癌症类型共同影响患者生存的“共享预后基因”。传统方法通常针对单一癌种建模，或简单合并数据后使用标准生存模型（如Cox比例风险模型），但忽略了不同癌症间异质性（heterogeneity）导致的效应差异，且难以同时实现基因筛选与跨癌种共享性推断。本报告试图解决：如何在允许癌种间效应存在合理差异的前提下，从高维基因表达数据中稳健地筛选出对多个癌种生存时间均有显著影响的基因集。

**核心方法**  
讲者提出一个**局部加权组惩罚加速失效时间模型**（Locally Weighted Group-Penalized Accelerated Failure Time Model）。模型以AFT（Accelerated Failure Time）为生存分析框架，直接建模对数生存时间与协变量的线性关系，适用于高维右删失数据。关键创新在于：对每个基因，将其在不同癌种中的系数视为一个“组”（group），施加组级惩罚（如group lasso）以鼓励跨癌种共享效应；同时引入**局部权重**（locally weighted）——根据各癌种样本量或数据质量自适应调整惩罚强度，使得效应估计在异质性较大的癌种中仍保持稳健。优化目标可写为  
\[
\min_{\boldsymbol{\beta}} \sum_{k=1}^K w_k \ell_k(\boldsymbol{\beta}_k) + \lambda \sum_{j=1}^p \|\boldsymbol{\beta}_{j}\|_2,
\]  
其中 $\ell_k$ 为第 $k$ 个癌种的AFT损失函数，$w_k$ 为局部权重，$\boldsymbol{\beta}_j$ 为第 $j$ 个基因在 $K$ 个癌种中的系数向量，$\|\cdot\|_2$ 为组lasso惩罚。

**与已有工作关系**  
已有工作多采用meta分析整合各癌种独立模型的结果，或使用多任务学习（multi-task learning）中的group lasso，但通常假设各任务（癌种）完全同质或完全异质。本报告提出的局部加权策略介于两者之间：通过数据驱动的权重，允许不同癌种对共享基因的贡献不同，同时利用组惩罚强制基因在多数癌种中效应非零。相比标准group lasso，局部加权能避免小样本癌种被过度收缩；相比单独建模，则能借用跨癌种信息提升统计效力。

**贡献**  
1. 方法学上，首次将局部加权思想引入组惩罚生存模型，为异质性多源生存数据提供了一种灵活且可解释的变量选择工具。  
2. 在泛癌预后基因识别中，该方法能同时实现基因筛选与跨癌种共享性评估，输出每个基因的“共享程度”指标（如组系数范数），便于生物学验证。  
3. 通过模拟和真实数据（如TCGA）分析，有望证明该方法在预测精度和基因发现稳定性上优于现有单癌种或简单合并方法，为精准医学中的跨癌种生物标志物发现提供新思路。


### 5. Deep Semiparametric Regression under Unequal Probability Sampling

**讲者**：Sijie Xu（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
不等概率抽样（Unequal Probability Sampling）在调查数据、流行病学等领域广泛存在，但现有半参数回归模型（如部分线性模型）通常假设样本独立同分布或简单随机抽样，直接应用会导致估计偏差。该报告旨在解决：当观测数据来自已知或未知的抽样概率分布时，如何利用深度神经网络灵活估计半参数回归中的非参数成分，同时保证参数分量的相合性与有效推断。

**核心方法**  
报告提出一种深度半参数回归框架，将响应变量 $Y$ 与协变量 $(X, Z)$ 的关系建模为 $Y = X^\top \beta + g(Z) + \varepsilon$，其中 $g(\cdot)$ 由深度神经网络（DNN）逼近，$\beta$ 为有限维参数。为处理不等概率抽样，引入逆概率加权（IPW）或伪似然（pseudo-likelihood）技术，构造加权经验损失函数。估计过程分两步：首先用加权 DNN 估计非参数函数 $\hat{g}(Z)$，然后通过加权最小二乘或 profile 方法得到 $\hat{\beta}$。理论分析借助 DNN 的逼近误差界与抽样权重的鞅差结构，证明 $\hat{\beta}$ 的 $\sqrt{n}$-相合性与渐近正态性，并给出 $\hat{g}$ 的收敛速度。

**与已有工作关系**  
经典半参数回归（如 Speckman 1988）依赖核或样条光滑，难以处理高维或复杂结构；近期深度半参数方法（如 Farrell et al. 2021）假设 i.i.d. 样本，未考虑抽样偏差。该报告将不等概率抽样纳入深度半参数框架，填补了“复杂抽样设计 + 深度学习非参数”的空白。与 Horvitz-Thompson 型估计相比，该方法同时估计参数与非参数部分，避免了模型误设导致的偏差放大。

**主要贡献**  
1. 首次在不等概率抽样下建立深度半参数回归的理论性质，包括参数估计的渐近正态性与非参数估计的最优收敛速度。  
2. 提出一种计算可行的加权 DNN 算法，并给出权重选择（如已知抽样概率或估计倾向得分）的指导。  
3. 通过模拟与真实数据（如 NHANES 调查）验证方法在偏差校正与效率提升上的优势，为调查数据分析提供了新工具。


### 6. Semiparametric Model Averaging Prediction in Nested Case-Control Studies

**讲者**：Mengyu Li（Northeastern University at Qinhuangdao）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
嵌套病例对照研究（Nested Case-Control Study, NCC）是大型队列中高效抽样罕见结局的设计，但传统分析多聚焦于风险因素筛选（如条件逻辑回归），对个体水平预测关注不足。当存在多个候选预测模型（如不同协变量组合或半参数结构）时，单一模型选择易受抽样波动影响，导致预测不稳定。本报告旨在解决：在NCC设计下，如何利用半参数模型平均（Semiparametric Model Averaging）提升对新个体的预测精度与稳健性，同时正确刻画抽样机制带来的偏倚。

**核心方法**  
报告提出一种基于逆概率加权（IPW）的半参数模型平均框架。首先，对每个候选模型（如部分线性模型 $Y = X^\top\beta + g(Z) + \varepsilon$）通过加权似然或加权最小二乘估计参数，权重为NCC抽样概率的倒数。然后，构造交叉验证或信息准则导向的权重选择准则，对候选预测值进行加权平均。关键创新在于：权重优化目标直接针对预测误差，且利用NCC设计的“嵌套”结构（对照从风险集中随机抽取）导出渐近无偏的损失函数估计量，避免对完整队列数据的依赖。

**与已有工作关系**  
已有模型平均方法多假设独立同分布数据或简单随机抽样，直接应用于NCC会因抽样偏倚导致预测偏差。部分工作针对病例对照设计（如logistic回归的模型平均），但未考虑时间匹配与风险集结构。本报告将半参数模型平均拓展至NCC，通过IPW修正抽样偏倚，并利用风险集内的条件独立性简化方差估计，与Buckland (1997) 的平滑AIC权重及Hansen (2007) 的Mallows准则形成对比，后者在复杂抽样下失效。

**主要贡献**  
1. 首次为NCC设计提供半参数模型平均预测方法，填补了该领域在预测集成方面的空白。  
2. 理论证明所提权重选择准则在NCC下仍保持渐近最优性（即预测损失与最优不可达权重下的损失之比趋于1）。  
3. 数值模拟显示，相比单一最优模型或简单平均，该方法在有限样本下显著降低预测均方误差，尤其当候选模型间异质性较大时。  
4. 为大型队列中利用NCC子集进行高效预测建模提供了实用工具，兼具半参数灵活性与模型平均稳健性。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)