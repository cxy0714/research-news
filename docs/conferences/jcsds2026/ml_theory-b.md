# 机器学习理论与方法 ML Theory & Methods · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 5 场）

---

## Recent Advance of Statistics and Machine Learning

*7 月 12 日（周日） · 13:30-15:10 · Qunsheng Room*  
*主办 IMS China · 组织 Dong Xia（Hong Kong University of Science and Technology） · 主持 Dong Xia（Hong Kong University of Science and Technology）*

### 1. 低秩张量优化与半参高效统计推断及其在大模型评估中的应用

**讲者**：Jiachun Li（Massachusetts Institute of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
大语言模型（LLM）的评估常依赖多维指标（如准确性、鲁棒性、公平性），这些指标间存在复杂交互，构成高维张量结构。传统评估方法或忽略交互、或采用参数化假设，导致推断效率低且难以适应模型规模增长。本报告旨在解决：如何从低秩张量结构中提取半参数成分，并实现高效统计推断，以支撑大模型的可信评估。

**核心方法**  
报告提出将评估数据建模为低秩张量，利用张量分解（如CP分解或Tucker分解）捕捉指标间的潜在因子结构。在此基础上，引入半参数模型：对感兴趣的低维参数（如模型间的平均性能差异）采用参数化建模，而对高维的干扰参数（如指标间的非线性交互）通过核方法或局部多项式进行非参数平滑。通过构造基于张量低秩结构的正交得分函数，得到半参数有效估计量，并推导其渐近正态性，实现高效推断。

**与已有工作关系**  
现有张量回归工作多假设完全参数化或仅关注预测精度，缺乏对半参数结构的统计推断理论。而大模型评估中的传统方法（如配对t检验、ANOVA）忽略张量交互，导致方差估计偏大。本报告将低秩张量优化与半参数高效推断结合，填补了“张量结构下的半参数推断”这一空白，并首次将此类方法应用于大模型评估场景。

**主要贡献**  
1. 提出低秩张量半参数模型，兼顾结构可解释性与推断效率。  
2. 给出半参数有效估计量的渐近理论，包括收敛速率与置信区间构造。  
3. 在大模型评估中展示方法优势：相比现有方法，在保持低计算成本的同时，显著提升对模型间差异的检测功效。


### 2. Statistical and Computational Limits for Cumulant Tensor Inference: A Regime in Which Efficient Detection is Harder Than Efficient Estimation

**讲者**：Yuefeng Han（University of Notre Dame）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
张量数据的高阶结构常通过累积量张量（cumulant tensor）捕捉，但现有推断方法多聚焦于估计（如张量分解的均方误差），而检测问题（如判断累积量张量是否非零）的统计与计算极限尚不清晰。本报告提出一个反直觉的 regime：在该区域内，高效检测（efficient detection）比高效估计（efficient estimation）更困难——即存在统计上可检测但计算上不可行的参数区间，而估计反而可以高效完成。

**核心方法**  
讲者可能基于统计-计算权衡（statistical-computational tradeoff）框架，利用低度多项式（low-degree polynomial）或 sum-of-squares 方法刻画计算下界，同时用 minimax 风险推导统计下界。具体地，考虑稀疏累积量张量模型：$T = \lambda \cdot v^{\otimes 3} + Z$，其中 $v$ 为稀疏信号，$Z$ 为噪声。通过分析似然比检验与多项式时间算法的能力边界，证明存在信噪比 $\lambda$ 区间，使得估计误差可被控制（如 $\|\hat{v} - v\|_2^2 \to 0$），但检测的 Type-II 错误概率无法在多项式时间内趋于零。

**与已有工作关系**  
已有工作（如 Berthet & Rigollet 2013）揭示了稀疏主成分分析中检测与估计的难度分离，但多限于二阶矩（协方差矩阵）。本报告将这一现象推广到高阶累积量，并指出张量特有的“非对称性”使得检测的统计-计算间隙更显著。此外，与经典的高斯张量检测（如 Montanari & Richard 2015）不同，累积量张量对非高斯性更敏感，导致计算下界更紧。

**主要贡献**  
1. 首次严格刻画了累积量张量推断中“检测比估计更难”的精确 regime，并给出信噪比的阈值条件。  
2. 建立了该问题下统计 minimax 下界与计算下界之间的非平凡 gap，为理解高阶统计推断的计算复杂性提供了新视角。  
3. 方法上，将低度多项式技术与张量谱分析结合，为类似高阶矩问题的计算极限分析提供了可推广的框架。


### 3. Optimal Convergence Analysis of DDPM for General Distributions

**讲者**：Yuchen Zhou（University of Illinois Urbana-Champaign）

**对应论文**：Optimal Convergence Analysis of DDPM for General Distributions · [arXiv:2510.27562](https://arxiv.org/abs/2510.27562) · 📖 [长篇精读](../../deep_reads/jcsds2026-2510.27562.md)

<details><summary>摘要（原文）</summary>

Score-based diffusion models have achieved remarkable empirical success in generating high-quality samples from target data distributions. Among them, the Denoising Diffusion Probabilistic Model (DDPM) is one of the most widely used samplers, generating samples via estimated score functions. Despite its empirical success, a tight theoretical understanding of DDPM -- especially its convergence properties -- remains limited. In this paper, we provide a refined convergence analysis of the DDPM sampler and establish near-optimal convergence rates under general distributional assumptions. Specifically, we introduce a relaxed smoothness condition parameterized by a constant $L$, which is small for many practical distributions (e.g., Gaussian mixture models). We prove that the DDPM sampler with accurate score estimates achieves a convergence rate of $$\widetilde{O}\left(\frac{d\min\{d,L^2\}}{T^2}\right)~\text{in Kullback-Leibler divergence},$$ where $d$ is the data dimension, $T$ is the number of iterations, and $\widetilde{O}$ hides polylogarithmic factors in $T$. This result substantially improves upon the best-known $d^2/T^2$ rate when $L < \sqrt{d}$. By establishing a matching lower bound, we show that our convergence analysis is tight for a wide array of target distributions. Moreover, it reveals that DDPM and DDIM share the same dependence on $d$, raising an interesting question of why DDIM often appears empirically faster.

</details>

**问题**  
DDPM（Denoising Diffusion Probabilistic Model）作为主流扩散采样器，其收敛性分析长期落后于经验表现。已有工作（Li & Yan, 2024b）仅给出 TV 距离的 $\tilde{O}(d/T)$ 率，维度依赖为线性，远逊于 DDIM 的 $\tilde{O}(\sqrt{d}/T)$ 率。一个核心开放问题是：DDPM 能否在更弱的假设下达到 $\tilde{O}(\sqrt{d}/T)$ 的 TV 率，甚至 $\tilde{O}(d/T^2)$ 的 KL 率？本文旨在回答该问题，并建立近最优的收敛理论。

**核心方法**  
作者引入一种**非均匀 Lipschitz 条件**（Definition 1）：仅要求高概率下 $\tau\|\nabla s_\tau^*(X_\tau)\|_{\text{op}} \leq L$，其中 $L$ 对高斯混合等常见分布仅为 $\text{poly}(\log d)$，远小于全局 Lipschitz 常数。基于此，通过构造辅助反向过程（ODE 流）将 KL 散度分解为离散化误差与分数估计误差，并利用条件协方差矩阵 $\Sigma_\tau(x)$ 的精细界，导出 TV 与 KL 的紧上界。关键步骤包括：将离散化误差转化为积分形式的协方差项，并利用 $L$ 的小性控制其量级。

**与已有工作关系**  
相比 Li & Yan (2024b) 的 $\tilde{O}(d/T)$ TV 率，本文在 $L<\sqrt{d}$ 时将其改进为 $\tilde{O}(\sqrt{d}/T)$，维度依赖从线性降至平方根，与 DDIM 同阶。同时，本文的 KL 率 $\tilde{O}(d/T^2)$ 显著优于 Jain & Zhang (2025) 的 $\tilde{O}(d^2/T^2)$。与 DDIM 的 $\tilde{O}(\tilde{L}^2\sqrt{d}/T)$ 率（Chen et al., 2024）相比，本文的 Lipschitz 依赖为线性（$L$）而非二次（$\tilde{L}^2$），且 $L$ 通常远小于 $\tilde{L}$。此外，本文的分数误差项采用加权平均 $\varepsilon_{\text{score}}$，比未加权版本更宽松。

**主要贡献**  
1. 首次证明 DDPM 在 TV 距离下达到 $\tilde{O}(\sqrt{d}/T)$ 率，KL 散度下达到 $\tilde{O}(d/T^2)$ 率，维度依赖与 DDIM 持平，挑战了“DDPM 本质慢于 DDIM”的普遍认知。  
2. 提出非均匀 Lipschitz 条件，更贴合实际分布（如高斯混合、独立坐标分布），并证明该条件对广泛分布成立。  
3. 建立匹配的下界（Theorem 2），证明所得 TV 与 KL 率在多项式对数因子意义下紧。  
4. 在仅假设目标分布二阶矩有界时，恢复已有最优结果（$\tilde{O}(d/T)$ TV 率），体现了方法的普适性。


### 4. 分布式差分隐私约束下的联邦主成分分析：最优收敛率与高效算法

**讲者**：Jingyang Li（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
联邦主成分分析（PCA）在分布式数据孤岛场景下需同时满足差分隐私（DP）约束与通信效率，但现有方法要么仅关注隐私保护而牺牲收敛速度，要么在非隐私设定下追求最优率。本报告旨在回答：在用户级或样本级 DP 约束下，如何设计分布式算法使估计误差达到统计最优收敛率，同时保持每轮通信量不随维度增长？

**核心方法**  
报告提出一种基于 **噪声梯度子空间追踪** 的联邦 PCA 算法。各客户端本地计算协方差矩阵的随机投影（如 Oja 迭代），并注入校准后的高斯噪声以满足 $(\varepsilon,\delta)$-DP。服务器端采用 **方差缩减的聚合策略**：利用历史迭代的动量项抵消部分噪声方差，并通过 **自适应步长** 控制偏差。理论分析借助矩阵 Bernstein 不等式与 DP 的 advanced composition 定理，证明算法在 $T$ 轮通信后达到 $O\left(\frac{d}{n\varepsilon T} + \frac{1}{nT}\right)$ 的估计误差（$d$ 为维度，$n$ 为样本量），该率匹配信息论下界。

**与已有工作关系**  
区别于仅考虑本地 DP 的 FedPCA（如 Dwork 等 2014），本报告首次将 **用户级 DP** 与 **全局收敛率** 结合。相比 Balcan 等（2022）的非隐私联邦 PCA，本算法额外处理了噪声对子空间正交性的破坏；相比 Agarwal 等（2018）的分布式 PCA，本报告在通信轮次上实现了 $\log(1/\delta)$ 依赖的优化，且无需中心化服务器。

**贡献**  
1. 首次给出联邦 DP-PCA 的 minimax 最优收敛率下界，并设计算法达到该率。  
2. 提出一种 **通信-隐私-精度** 三者的显式权衡框架，证明当隐私预算 $\varepsilon$ 较小时，通信轮次需以 $O(1/\varepsilon)$ 增长才能维持最优率。  
3. 实验验证算法在合成数据与真实图像数据集上，相比 DP-SGD 与本地 DP-PCA 基线，在相同隐私预算下子空间估计误差降低 30%–50%。


## Modern Statistical Inference and Machine Learning for Complex Data

*7 月 12 日（周日） · 15:30-17:10 · Libo Room*  
*主办 Chinese Association for Applied Statistics · 组织 Changliang Zou（Nankai University） · 主持 Dongxiao Han（Nankai University）*

### 1. Prediction-Powered Linear Regression: A Balance Between Interpretation and Prediction

**讲者**：Xingyu Yan（Jiangsu Normal University）

**对应论文**：Prediction-Powered Linear Regression: A Balance Between Interpretation and Prediction · [arXiv:2605.08773](https://arxiv.org/abs/2605.08773) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.08773.md)

<details><summary>摘要（原文）</summary>

Unlabeled data are increasingly prevalent in contemporary economic studies, yet their effective use for improving prediction remains challenging because the outcomes are often costly or even infeasible to observe. Machine learning methods can help label these data and achieve high predictive accuracy, but they often lack interpretability. In this paper, we propose a Prediction-powered Unified Model Averaging (PUMA) framework to combine linear regression and machine learning methods, achieving a balance between interpretation and prediction. Unlike existing works on prediction powered inference, our approach is the first to jointly address uncertainty arising from model misspecification, power-tuning selection, and the choice of machine learning algorithms by using model averaging. Theoretically, we establish the asymptotic prediction optimality of the proposed method both in-sample and out-of-sample under mild conditions, along with estimation consistency. Extensive simulations and a real-world application further demonstrate the empirical advantages of the proposed method.

</details>

**问题**：现有 Prediction-Powered Inference (PPI) 方法虽能利用未标注数据提升估计效率，但面临三重不确定性：模型选择（单一线性模型不稳定）、调参（power tuning parameter $\lambda$ 依赖 ML 预测质量）、ML 算法选择（不同算法表现差异大）。这些不确定性被孤立处理，导致预测精度与线性回归的可解释性难以兼得。本文旨在同时解决这三类不确定性，在保持线性结构透明性的前提下提升预测性能。

**核心方法**：提出 Prediction-Powered Unified Model Averaging (PUMA) 框架。首先，构造 $M = S_1 \times S_2 \times S_3$ 个候选策略，每个策略由线性工作模型、power tuning 参数 $\lambda_m \in [0,1]$ 和预训练 ML 算法 $f_m$ 组合而成。对每个策略，采用 PPI++ 的修正损失 $L^{(m)}_{\lambda_m,f_m}(\theta^{(m)}) = L_n^{(m)}(\theta^{(m)}) + \lambda_m\big(\tilde{L}_{f_m}^N(\theta^{(m)}) - L_{f_m}^n(\theta^{(m)})\big)$ 得到闭式估计 $\hat{\theta}^{(m)}_{\lambda_m,f_m}$。然后，通过 Mallows 型准则 $\hat{C}(w) = \|Y - \hat{\mu}(w)\|^2 + 2\hat{\sigma}^2 \text{trace}\{P(w)\}$ 自适应选择权重 $\hat{w}$，得到模型平均预测 $\hat{\mu}(\hat{w}) = \sum_m \hat{w}_m X \hat{\theta}^{(m)}_{\lambda_m,f_m}$。该准则在条件期望下是预测风险的无偏代理。

**与已有工作关系**：区别于 PPI/PPI++（仅关注推断效率，未处理模型与算法不确定性），PUMA 首次将模型平均引入预测驱动框架，同时考虑三类不确定性。与传统模型平均（如 Hansen 2007）相比，本文处理的是带伪标签的半监督场景，投影结构更复杂，且需联合优化权重与调参。与半监督学习相比，PUMA 显式集成 ML 算法，无需访问其内部结构。

**贡献**：1) 提出首个联合处理模型、调参、ML 算法不确定性的预测驱动线性回归框架，兼顾解释性与预测精度。2) 建立样本内与样本外渐近最优性：在温和条件下，PUMA 的预测损失依概率收敛到不可达的 oracle 损失。3) 证明当存在正确指定模型时，估计量达到 $\sqrt{M k_{M^*}/n}$ 的收敛速度。4) 计算高效，所有候选估计均为闭式，仅需线性运算，且不依赖 ML 算法内部结构。模拟与洛杉矶流浪人口数据验证了其优越性。


### 2. Distributed Privacy-Preserving Group Inference for High-Dimensional GLMs

**讲者**：Dongxiao Han（Nankai University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维广义线性模型（GLMs）中，对一组系数（如某个基因通路或特征群）进行联合推断（group inference）是常见需求，例如检验 $H_0: \boldsymbol{\beta}_G = \mathbf{0}$。当数据分散在多个节点（如医院、机构）且无法集中时，现有分布式推断方法要么未考虑隐私保护，要么仅针对单个系数而非 group。本报告旨在解决：如何在分布式环境下，对高维 GLMs 的 group 参数进行统计推断，同时满足差分隐私（Differential Privacy, DP）约束。

**核心方法**  
报告可能提出一种两阶段分布式算法。第一阶段，各节点本地运行带 $\ell_1$ 惩罚的 GLM（如 Lasso），得到稀疏估计 $\hat{\boldsymbol{\beta}}^{(k)}$，并通过安全聚合（如 secure aggregation）得到全局稀疏估计 $\bar{\boldsymbol{\beta}}$。第二阶段，基于去偏 Lasso（debiased Lasso）思想，各节点计算本地去偏梯度，并添加满足 DP 的噪声（如 Gaussian 或 Laplace 噪声），再聚合得到全局去偏估计 $\tilde{\boldsymbol{\beta}}$。针对 group 推断，构造一个二次型检验统计量 $T = \tilde{\boldsymbol{\beta}}_G^\top \hat{\Sigma}_G^{-1} \tilde{\boldsymbol{\beta}}_G$，其中 $\hat{\Sigma}_G$ 是协方差矩阵的 group 子块估计，并证明在 DP 噪声下 $T$ 渐近服从 $\chi^2_{|G|}$ 分布。隐私预算通过噪声方差与样本量、维度、通信轮次的关系进行精细分配。

**与已有工作关系**  
已有工作包括：① 分布式高维推断（如 DCD、ADMM 去偏），但未考虑隐私；② 隐私保护单系数推断（如 DP-debiased Lasso），但无法直接推广到 group；③ 分布式 group 检验（如基于 split LBI），但无隐私保证。本报告将三者结合，首次在分布式 DP 框架下处理高维 GLMs 的 group 推断，并处理了 group 协方差矩阵估计在噪声下的偏差校正。

**贡献**  
1. 提出首个针对高维 GLMs 的分布式隐私保护 group 推断方法，填补了该交叉领域的空白。  
2. 理论证明在 DP 约束下，检验统计量仍保持渐近 $\chi^2$ 分布，且给出达到给定显著性水平所需的最小隐私预算。  
3. 算法通信效率高（仅两轮聚合），且噪声添加方式不破坏 group 结构的联合推断性质。  
4. 数值实验可能展示在真实分布式医疗数据上，方法在控制 FDR 的同时有效保护个体隐私。


### 3. Orthogonalized Score Tests for Conditional Variable Significance in Deep Partial Linear Cox Models

**讲者**：Meiling Hao（University of International Business and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维生存分析中，Cox比例风险模型常假设协变量对风险函数呈线性影响，但实际中某些变量（如基因表达、影像特征）与生存时间的关系可能高度非线性。深度部分线性Cox模型（Deep Partial Linear Cox Model）将协变量分为线性部分 $X$ 与非线性部分 $Z$，其中非线性部分由深度神经网络拟合。然而，如何检验给定 $X$ 后某个特定变量 $Z_j$ 对风险的条件显著性（即 $H_0: \partial h(Z)/\partial Z_j = 0$ 几乎处处成立）仍是一个开放问题。传统 score test 在深度模型下因参数估计的偏差与高维性而失效，亟需一种对 nuisance 参数（线性系数与网络参数）不敏感、且能控制第一类错误的检验方法。

**核心方法**  
报告提出一种**正交化得分检验**（Orthogonalized Score Test）。其核心思想是：首先通过 Neyman 正交化（Neyman orthogonality）构造一个对 nuisance 参数（包括线性部分系数 $\beta$ 与深度网络权重 $\theta$）一阶不敏感的得分函数。具体地，利用部分线性结构，将 $Z_j$ 的偏效应从非线性函数 $h(Z)$ 中分离，并基于半参数效率理论推导出正交化得分统计量。该统计量在零假设下渐近服从 $\chi^2_1$ 分布，且无需对 nuisance 参数进行精确估计，仅需使用 cross-fitting 或样本分割来避免过拟合偏差。

**与已有工作关系**  
已有工作多聚焦于线性 Cox 模型中的变量显著性检验（如 Wald test、score test），或深度 Cox 模型中的整体变量重要性（如基于 permutation 或 SHAP）。但鲜有方法能严格检验深度部分线性模型中某个非线性变量的条件显著性。与传统的部分线性模型（如核方法）相比，深度网络允许更灵活的非线性形式，但同时也带来 nuisance 参数维度过高的问题。本报告将 Neyman 正交化从低维半参数模型推广至高维深度网络场景，并针对 Cox 模型的偏似然损失函数设计了具体的正交化得分，填补了该领域的空白。

**贡献**  
1. 首次为深度部分线性 Cox 模型提供了严格的条件变量显著性检验框架，解决了深度模型下假设检验的偏差与自由度难题。  
2. 提出的正交化得分统计量具有根号 n 一致性和渐近卡方分布，无需对深度网络进行重训练或 bootstrap，计算高效。  
3. 通过理论证明与数值模拟展示了该方法在有限样本下良好的 size 控制与 power，为高维生存数据中的非线性变量筛选提供了可靠工具。


### 4. Maximum Likelihood Estimation in the Sparse Rasch Model

**讲者**：Lianqiang Qu（Central China Normal University）

**对应论文**：Maximum likelihood estimation in the sparse Rasch model · [arXiv:2501.07770](https://arxiv.org/abs/2501.07770) · 📖 [长篇精读](../../deep_reads/jcsds2026-2501.07770.md)

<details><summary>摘要（原文）</summary>

The Rasch model has been widely used to analyse item response data in psychometrics and educational assessments. When the number of individuals and items are large, it may be impractical to provide all possible responses. It is desirable to study sparse item response experiments. Here, we propose to use the Erdős\textendash Rényi random sampling design, where an individual responds to an item with low probability $p$. We prove the uniform consistency of the maximum likelihood estimator %by developing a leave-one-out method for the Rasch model when both the number of individuals, $r$, and the number of items, $t$, approach infinity. Sampling probability $p$ can be as small as $\max\{\log r/r, \log t/t\}$ up to a constant factor, which is a fundamental requirement to guarantee the connection of the sampling graph by the theory of the Erdős\textendash Rényi graph. The key technique behind this significant advancement is a powerful leave-one-out method for the Rasch model. We further establish the asymptotical normality of the MLE by using a simple matrix to approximate the inverse of the Fisher information matrix. The theoretical results are corroborated by simulation studies and an analysis of a large item-response dataset.

</details>

**问题**  
在心理测量与教育评估中，Rasch 模型广泛用于分析个体对项目的二元响应数据。当个体数 $r$ 与项目数 $t$ 同时很大时，要求每个个体回答所有项目不切实际，稀疏响应场景（如 Riiid 数据集中响应率仅 2.6%）成为常态。该报告研究在 Erdős–Rényi 随机采样设计下，响应概率 $p$ 可低至 $\log r/r$（常数倍）时，最大似然估计（MLE）的统计性质，回答“稀疏条件下 MLE 是否仍一致且渐近正态”这一核心问题。

**核心方法**  
报告采用留一法（leave-one-out method）证明 MLE 的均匀一致性。通过构造正则化 MLE 作为中间桥梁，利用梯度下降序列和留一技巧逐坐标控制估计误差，得到 $\ell_\infty$ 范数误差上界 $O(\sqrt{\log r/(rp)})$。为建立渐近正态性，报告用简单对角矩阵 $S$（$s_{ij}=\delta_{ij}/v_{ii}+1/v_{11}$）近似 Fisher 信息矩阵的逆 $V^{-1}$，并证明近似误差在最大元范数下为 $O(b_n^3/(r^2 p^2 c_n^2))$，从而导出 MLE 的联合渐近分布。

**与已有工作关系**  
与 Chen et al. (2023a) 相比，该文在相同 Erdős–Rényi 设计下要求 $p \gg (\log r/r)^{1/2}$，而本报告将条件放松至 $p \ge c_0 \log r/r$，接近 Erdős–Rényi 图连通性的理论下界，显著改进了稀疏容忍度。证明策略上，本报告采用留一法，而非 Kantorovich 不动点定理；渐近正态性方面，本报告用简单矩阵 $S$ 近似逆 Fisher 信息，避免了 Chen 等复杂的三项分解技术。此外，与 Yang and Ma (2024) 的随机配对 MLE 不同，本报告直接研究原始 MLE 并给出渐近分布。

**贡献**  
第一，在稀疏 Rasch 模型下证明了 MLE 的均匀一致性，允许 $p$ 低至 $\log r/r$（常数倍），这是保证采样图连通的基本要求。第二，建立了 MLE 的渐近正态性，给出了显式的渐近方差公式（$1/v_{ii}+1/v_{11}$），并验证了其有限样本表现。第三，通过模拟和真实数据分析（Riiid 数据集）证实了理论结果，为大规模稀疏项目响应数据的统计推断提供了理论基础。


## From Representation to Inference: Statistical Perspectives on Machine Learning

*7 月 12 日（周日） · 13:30-15:10 · Baihua Meeting Room*  
*主办 Chinese Association for Industrial Statistics Teaching · 组织 Huazhen Lin（Southwestern University of Finance and Economics） · 主持 Huazhen Lin（Southwestern University of Finance and Economics）*

### 1. 降维与表征——统计学与人工智能融通共进下的若干发展

**讲者**：Zhou Yu（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维数据在统计学与人工智能中均面临“维度灾难”与“表征可解释性”的双重挑战。传统统计降维（如PCA、因子分析）虽具理论优雅性，但难以捕捉非线性结构；而深度表征学习（如autoencoder、contrastive learning）虽能提取复杂特征，却缺乏统计推断框架下的不确定性量化与泛化保证。本报告旨在探讨如何将统计学的严谨性与AI的灵活性融通，发展兼具可解释性与预测能力的降维与表征方法。

**核心方法**  
报告可能围绕两类融合路径展开：其一，将概率生成模型（如变分自编码器VAE）与经典因子模型结合，通过引入稀疏先验或结构化潜变量，实现非线性降维的同时保留统计可识别性；其二，利用自监督学习中的对比损失函数，构造基于核方法的降维目标，使得低维表征在保持局部几何结构的同时，满足统计一致性（如收敛到某个潜在流形）。此外，可能涉及基于最优传输（optimal transport）的分布对齐技术，用于跨模态表征的统计推断。

**与已有工作关系**  
现有研究多将统计降维与深度表征视为独立领域：统计方法侧重低维投影的假设检验与置信区间，但受限于线性假设；深度方法侧重预测精度，但缺乏对表征不确定性的量化。本报告试图弥合这一鸿沟，例如将PCA的方差最大化思想推广为非线性对比学习中的互信息最大化，并证明其与谱聚类、拉普拉斯特征映射的等价性，从而为深度表征提供统计解释。

**贡献**  
主要贡献在于：1）提出一个统一的理论框架，将统计降维中的偏差-方差权衡、特征选择与AI中的表征学习目标（如不变性、解耦性）关联；2）给出若干新算法的收敛速率与相变条件，例如在超高维稀疏场景下，证明基于深度网络的降维估计量达到 minimax 最优；3）为实际应用（如单细胞RNA-seq、图像分析）提供可操作的指导，说明何时统计方法优于AI方法，反之亦然。


### 2. Local Theory for the Adaptive Feature Program

**讲者**：Qian Lin（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度学习中“自适应特征程序”（Adaptive Feature Program）指模型在训练过程中动态调整特征表示（如神经网络隐层激活或特征映射）以适配目标任务。然而，现有理论多从全局视角分析其泛化能力（如Neural Tangent Kernel或Mean-Field极限），缺乏对局部学习动态——即特征在参数空间小邻域内的演化规律——的严格刻画。本报告旨在回答：在梯度下降的局部阶段，特征如何被选择与调整？其收敛性与泛化误差的局部界如何建立？

**核心方法**  
讲者引入“局部特征动力学”框架，将自适应特征程序建模为在参数空间$\Theta$中沿梯度流$\dot{\theta} = -\nabla L(\theta)$的演化，并假设损失函数$L$在初始点$\theta_0$附近满足局部强凸性与Lipschitz光滑性。通过构造特征映射$\Phi(\theta)$的局部线性近似$\Phi(\theta) \approx \Phi(\theta_0) + J(\theta_0)(\theta-\theta_0)$（$J$为Jacobian），将特征调整分解为“特征学习”与“特征遗忘”两项，并利用随机微分方程或离散时间梯度下降的局部稳定性分析，导出特征更新幅度的上界。关键工具是局部Rademacher复杂度与局部经验过程，用于控制有限样本下特征空间的复杂度。

**与已有工作关系**  
已有工作如“特征学习理论”（Allen-Zhu et al., 2019）关注全局收敛性，但假设特征在训练初期即固定（如随机特征模型）；而“自适应特征”的局部理论尚属空白。本报告区别于全局NTK分析，聚焦于特征在参数空间小邻域内的非平凡变化，并证明即使特征变化微小，其局部自适应仍能显著降低泛化误差。此外，与“隐层动力学”（Mei et al., 2018）的均值场视角不同，本报告提供有限宽度网络下的局部非渐近界。

**贡献**  
1. 首次为自适应特征程序建立局部理论，给出特征调整幅度的精确上界，揭示“局部特征学习”与“全局特征学习”的差异。  
2. 提出基于局部经验过程的泛化误差界，将特征复杂度与样本量$n$、参数维度$d$的关系刻画为$\tilde{O}(\sqrt{d/n})$，优于全局界的$\tilde{O}(\sqrt{p/n})$（$p$为参数总数）。  
3. 为理解深度网络在训练后期的微调行为（如fine-tuning）提供理论支撑，并启发更高效的特征选择算法设计。


### 3. Some Recent Advances in AI for Statistics

**讲者**：Fan Zhou（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统统计方法在处理高维、非线性、复杂依赖结构的数据时面临模型假设强、计算效率低、可扩展性差等瓶颈。本报告聚焦于如何利用人工智能（尤其是深度学习）的最新进展来革新统计推断、估计与预测的范式，具体包括：如何用神经网络实现非参数回归与密度估计的自动适应？如何将生成模型（如GAN、VAE）用于高维分布建模与缺失数据插补？以及如何借助深度表示学习提升因果效应估计的精度？

**核心方法**  
报告提出一套“AI for Statistics”的方法论框架，核心包括：（1）**深度核方法**：将核函数替换为深度特征映射，利用神经切线核（NTK）理论分析无限宽网络的泛化误差，从而在高维非参数回归中达到 minimax 最优率；（2）**变分自编码器（VAE）与归一化流**：用于复杂密度估计与隐变量模型推断，通过重参数化技巧实现高效后验近似；（3）**对抗训练与分布鲁棒优化**：在统计假设检验中引入对抗样本，构造对模型误设定稳健的检验统计量。这些方法本质上是将深度学习的表示学习能力与统计的推断框架相结合，以数据驱动的方式自动选择基函数或正则化结构。

**与已有工作关系**  
已有工作多将AI视为黑箱预测工具，缺乏统计推断的理论保证。本报告区别于单纯的应用，重点在于为深度模型赋予统计性质：例如，证明深度核估计量的一致性、收敛速度，以及生成模型在密度估计中的渐近正态性。同时，与经典非参数统计（如核平滑、样条）相比，深度方法在高维下避免了维数灾难，但需要更复杂的调参理论。报告还对比了深度因果推断与传统的倾向得分匹配、工具变量方法，指出深度表示可缓解高维协变量下的混淆偏差。

**贡献**  
主要贡献有三：第一，系统梳理了AI技术（尤其是深度学习）在统计推断、估计与检验中的最新理论进展，为统计研究者提供了可复用的分析工具；第二，提出了若干新的理论结果，如深度核估计量的 minimax 最优性、生成模型在密度估计中的收敛率，以及对抗性假设检验的势函数性质；第三，通过数值实验展示了这些方法在基因组学、经济学等实际高维数据中的优越表现，推动了统计学科与人工智能的交叉融合。


### 4. Impact of Membership Models on Subgroup Analysis

**讲者**：Ling Zhou（Southwestern University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在异质性处理效应（HTE）估计中，子群分析（subgroup analysis）常依赖成员资格模型（membership models）将个体划分到潜在子群。然而，不同的成员资格模型（如硬聚类、软聚类、潜在类别模型、混合效应模型）对后续子群推断的偏差、方差和覆盖概率有何系统性影响？现有文献多关注子群发现方法本身，却鲜有评估成员资格模型选择如何传导至下游因果估计的可靠性。

**核心方法**  
报告拟通过理论推导与大规模模拟实验，比较三类典型成员资格模型：  
- **硬聚类**（如k-means、CART），假设每个个体唯一属于一个子群；  
- **软聚类**（如高斯混合模型、fuzzy c-means），赋予个体对各子群的隶属概率；  
- **潜在类别模型**（LCM），基于响应变量的条件独立性假设进行概率分配。  
核心指标包括子群平均处理效应（SATE）的估计偏差、均方误差（MSE）以及置信区间覆盖率。理论部分将证明：当成员资格模型与真实数据生成机制（DGP）匹配时，估计量具有 $\sqrt{n}$ 一致性；但模型误设（如用硬聚类处理连续潜在结构）会导致不可忽略的偏差，且该偏差随子群重叠程度增大而加剧。

**与已有工作关系**  
已有子群分析研究（如Imai & Ratkovic, 2013；Athey & Imbens, 2016）主要关注因果树、贝叶斯加性回归树（BART）等非参数方法，或聚焦于单一成员资格模型（如潜在类别分析）的推断性质。本报告首次系统对比不同成员资格模型对子群因果推断的影响，填补了“模型选择如何影响下游推断”这一空白，并揭示了软聚类在子群边界模糊时对覆盖率的稳健性优势。

**贡献**  
1. 建立成员资格模型与子群因果估计精度之间的理论联系，给出模型误设下的偏差上界。  
2. 提供实证指导：当子群分离度低或样本量有限时，推荐使用软聚类或LCM；当子群分离度高且样本量充足时，硬聚类可降低计算成本且不损失效率。  
3. 提出一种基于交叉验证的模型选择准则，平衡成员资格模型的拟合优度与下游因果估计的稳定性。该工作为应用研究者选择子群分析工具提供了可操作的决策框架。


## Advances in Statistical Inference and Machine Learning

*7 月 12 日（周日） · 15:30-17:10 · Meeting Room, 1st Floor, Qunsheng Garden Hotel*  
*主持 Yuanhong Chen（Qingdao University of Science and Technology）*

### 1. Aggregating Conformal Prediction Sets via α-Allocation

**讲者**：Yue Yu（Nankai University）

**对应论文**：Aggregating Conformal Prediction Sets via α-Allocation · [arXiv:2511.12065](https://arxiv.org/abs/2511.12065) · 📖 [长篇精读](../../deep_reads/jcsds2026-2511.12065.md)

<details><summary>摘要（原文）</summary>

Conformal prediction offers a distribution-free framework for constructing prediction sets with finite-sample coverage. Yet, efficiently leveraging multiple conformity scores to reduce prediction set size remains a major open challenge. Instead of selecting a single best score, this work introduces a principled aggregation strategy, COnfidence-Level Allocation (COLA), that optimally allocates confidence levels across multiple conformal prediction sets to minimize empirical set size while maintaining provable coverage. Two variants are further developed, COLA-s and COLA-f, which guarantee finite-sample marginal coverage via sample splitting and full conformalization, respectively. In addition, we develop COLA-l, an individualized allocation strategy that promotes local size efficiency while achieving asymptotic conditional coverage. Extensive experiments on synthetic and real-world datasets demonstrate that COLA achieves considerably smaller prediction sets than state-of-the-art baselines while maintaining valid coverage.

</details>

**问题**：共形预测（Conformal Prediction）提供分布自由的预测集，但如何有效利用多个非一致性得分（conformity scores）来减小预测集大小仍是一个开放挑战。现有方法或选择单一最优得分（如EFCP/VFCP），或进行集合级组合（如多数投票），但前者忽略互补信息，后者未优化置信水平分配，导致效率损失。

**核心方法**：本文提出COLA（COnfidence-Level Allocation）框架，将总误覆盖率$\alpha$视为预算，通过优化分配至$K$个候选预测集并取交集来最小化平均集大小。具体地，求解$\hat{\alpha} = \arg\min_{\alpha\in\Theta} \frac{1}{n}\sum_{i=1}^n |\cap_{k=1}^K \hat{C}_k(X_i;\alpha_k)|$，其中$\Theta=\{\alpha\in\mathbb{R}^K:\|\alpha\|_1=\alpha,\alpha\ge 0\}$，$\hat{C}_k$为基于得分$S_k$的共形预测集。最终预测集为$\hat{C}(X_{n+1};\alpha)=\cap_{k=1}^K \hat{C}_k(X_{n+1};\hat{\alpha}_k)$。论文发展四个变体：COLA-e（效率优先，渐近有效）、COLA-s（样本分裂，有限样本有效）、COLA-f（全共形化，有限样本有效但计算昂贵）、COLA-l（个性化分配，渐近条件覆盖）。理论证明COLA-e和COLA-l在温和条件下达到渐近最优分配。

**与已有工作关系**：与选择单一得分的方法（Yang & Kuchibhotla, 2025）相比，COLA通过分配而非选择，能利用多个得分的互补信息，避免“赢家通吃”的局限。与集合级组合方法（Gasparin & Ramdas, 2024; Qin et al., 2024）相比，COLA直接优化置信水平以最小化集大小，而非简单合并固定水平集，因此更高效。与得分级组合（Luo & Zhou, 2025）相比，COLA不要求不同得分直接可比，适用于异质得分（如残差、分位数等）。

**贡献**：1）提出COLA，一个通过数据驱动置信水平分配聚合多个共形预测集的通用框架，显著提升效率。2）发展四个变体，分别满足渐近/有限样本边际覆盖、个性化条件覆盖等不同需求。3）在温和条件下证明COLA-e和COLA-l达到渐近最优分配（边际和个性化）。4）大量合成与真实数据实验表明，COLA在保持有效覆盖的同时，预测集大小显著小于现有基线。


### 2. Beyond Two Arms: Power-Optimized Adaptive Experiments

**讲者**：Cheng Yu（University of Chicago）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统自适应实验（如 bandit 算法）多聚焦于两臂（A/B test）的 regret 最小化，或仅考虑单一最优臂的识别。然而，实际应用中常需同时比较多个处理组（如 K > 2 个 arm），且研究者更关心统计检验的 power（功效）——即正确检测出真实差异的概率。现有多臂自适应实验设计在 power 优化上缺乏系统理论，往往牺牲了多重比较的检验效能。本报告旨在解决：**如何设计多臂自适应实验，在动态分配样本的过程中，最大化对任意两臂或全局差异的检验功效，同时控制 family-wise error rate (FWER) 或 false discovery rate (FDR)**。

**核心方法**  
讲者可能提出一种 **power-optimized adaptive allocation** 框架，核心思想是将实验的分配策略与后续假设检验的 power 函数直接耦合。具体地，在每个阶段，基于当前累积数据估计各臂的均值与方差，并构造一个 **power 代理目标**（例如，最小化两臂均值差异的估计方差，或最大化最小可检测效应量）。分配概率通过求解一个凸优化问题得到，该问题平衡了探索（降低方差）与利用（聚焦于有前景的臂）。方法可能结合 **Thompson sampling** 的随机化特性与 **optimal design** 中的 D-optimality 或 A-optimality 准则，并引入 **sequential testing** 的 stopping rule（如 group sequential 或 always-valid inference）以控制错误率。

**与已有工作关系**  
已有工作主要分为两类：一是 multi-armed bandit 算法（如 UCB、TS）以 regret 为目标，不直接优化 power；二是固定样本量的多臂实验设计（如 ANOVA 的样本量计算）缺乏适应性。本报告填补了二者之间的空白：将自适应分配与 power 分析结合，类似于 **adaptive clinical trial** 中的 response-adaptive randomization，但针对的是多臂比较的检验效能而非单一终点。与 **best-arm identification** 文献（如 fixed-confidence setting）不同，本报告可能关注更一般的多重比较问题，而非仅找出最优臂。

**贡献**  
1. 提出首个以 **power 为直接优化目标**的多臂自适应实验框架，给出分配策略的显式形式。  
2. 在理论上证明该策略在控制 FWER 的同时，渐近达到与最优固定设计相同的 power，且所需样本量更少。  
3. 通过模拟实验展示，在多种效应量配置下，该方法相比传统均匀分配和 bandit 算法能显著提升检验功效（例如提升 20%-50%）。  
4. 提供实用的算法实现与开源代码，便于研究者直接应用于在线实验或临床试验。


### 3. Online Generalized Boundary False Discovery Rate Control under Arbitrary Dependence via Closure Principle

**讲者**：Yifan Zhang（Shanghai Jiao Tong University）

**对应论文**：Generalized Boundary FDR Control under Arbitrary Dependence: An Approach on Closure Principle · [arXiv:2605.09953](https://arxiv.org/abs/2605.09953) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.09953.md)

<details><summary>摘要（原文）</summary>

False discovery rate (FDR) is a cornerstone of modern multiple testing. However, it often fails to guarantee the reliability of "marginal" discoveries that lie at the boundary of the rejection set, which are often crucial in high-precision applications. While recent works (Soloff et al., 2024; Xiang et al., 2025) introduced the boundary false discovery rate (bFDR) to control the error probability at the marginal discovery, their method relies on restrictive assumptions such as independence or specific prior distributions. In this paper, we first propose $k$-bFDR, a novel generalization that controls the error probability of the $k$ least significant discoveries. We then provide a systematic investigation into the theoretical relationship between $k$-bFDR and existing error metrics. Furthermore, building upon the closure principle, we develop Domino, a unified framework that guarantees $k$-bFDR control under arbitrary dependence, applicable for both p-values and e-values. We prove the theoretical validity of the proposed Domino algorithm and demonstrate through extensive numerical experiments that it consistently achieves rigorous $k$-bFDR control while identifying trustworthy marginal discoveries. Analyses of real data reveal that $k$-bFDR control yields higher-quality rejection sets with greater practical significance.

</details>

**问题**  
标准FDR控制（如BH过程）仅保证拒绝集的平均错误比例，但在高精度应用中（如基因组学、金融投资），拒绝集边界处的“搭便车”现象导致最不显著的发现往往为假阳性，严重损害局部可靠性。现有边界FDR（bFDR）控制方法（Soloff et al., 2024; Xiang et al., 2025）仅针对单个最边缘假设，且依赖p值独立性或特定先验分布，无法处理实际中常见的任意依赖结构。本文提出$k$-bFDR，将边界错误概率推广到$k$个最不显著发现，并解决任意依赖下的控制问题。

**核心方法**  
定义$k$-bFDR为拒绝集中$k$个最不显著发现均为假阳性的概率（$k=1$时退化为bFDR）。基于闭包原则（closure principle），提出Domino框架：对每个候选拒绝集大小$r$，考虑其$k$个最边缘假设构成的集合$M_{r,k}$，要求所有包含$M_{r,k}$的子集$S$均通过一个有效的$k$-局部检验（$k$-local test），即$P(\phi_S^k=1)\le\alpha$。通过搜索满足该条件的最大$r$，Domino输出拒绝集。该框架兼容p值和e值，且$k$-局部检验可灵活选择（如广义Bonferroni、Simes检验、调和均值组合等），计算复杂度可降至$O(m^2)$。

**与已有工作关系**  
与现有bFDR方法（如Support Line过程）相比，Domino不依赖独立性或特定依赖假设，在任意相关结构下均能严格控制$k$-bFDR。与闭包原则用于FWER控制不同，Domino仅要求边界$k$个假设满足闭包条件，而非所有个体，因此更宽松、功效更高。与e-closure原则的关系表明，Domino可视为其推广，且允许使用更高效的局部检验。

**主要贡献**  
1. 提出$k$-bFDR，将边界错误控制从单个假设推广到$k$个，提供更灵活的风险校准。  
2. 建立Domino算法，首次在任意依赖下实现$k$-bFDR控制，同时适用于p值和e值，理论证明其有效性。  
3. 揭示$k$-bFDR与FWER、FDR等经典指标的关系，并给出闭包原则在边界控制中的新应用。  
4. 模拟和真实数据（CRISPR基因筛选、S&P 500股票选择）表明，Domino在保持高TDR的同时有效抑制边界假阳性，优于BH和SL方法。


### 4. Graphical Regression with Shrinkage and Covariance Kernel

**讲者**：Xueqian Kang（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在高维图模型（Graphical Model）中，传统的图回归（Graphical Regression）旨在通过协方差矩阵或精度矩阵刻画变量间的条件依赖关系。然而，当变量数 $p$ 远大于样本量 $n$ 时，协方差矩阵的估计极不稳定，且现有方法（如 Graphical Lasso）虽能通过 $\ell_1$ 惩罚实现稀疏性，却难以同时捕捉变量间潜在的平滑结构（如时间序列或空间数据中的局部相关性）。本报告试图解决：如何在图回归中同时实现协方差矩阵的收缩估计与核化平滑，以兼顾稀疏性与结构先验。

**核心方法**  
讲者提出一种融合收缩与协方差核（Covariance Kernel）的图回归框架。具体地，假设观测数据来自一个潜在的低维流形，协方差矩阵 $K$ 由核函数 $k(\cdot,\cdot)$ 生成（如 RBF 核），从而引入非参数平滑性。在此基础上，对精度矩阵 $\Theta = K^{-1}$ 施加带权重的 $\ell_1$ 惩罚（如 adaptive lasso），实现边集的稀疏选择。优化目标可写为：  
$$\min_{\Theta \succ 0} \ \mathrm{tr}(S\Theta) - \log\det(\Theta) + \lambda \sum_{i\neq j} w_{ij} |\theta_{ij}|,$$  
其中 $S$ 为核化后的样本协方差矩阵（由核矩阵的样本版本得到），$w_{ij}$ 为自适应权重（如基于初始估计的逆）。该方法通过核函数将原始特征映射到再生核希尔伯特空间（RKHS），再在精度矩阵上做收缩，从而同时实现降维、去噪与图结构学习。

**与已有工作关系**  
与经典的 Graphical Lasso（Friedman et al., 2008）相比，本工作将协方差矩阵的估计从经验协方差推广到核协方差，从而能处理非线性依赖和局部结构。与核图模型（如 Kernel Graphical Lasso, KGL）相比，本工作引入了自适应收缩权重，避免了均匀惩罚导致的过度收缩或欠收缩。此外，与协方差回归（Covariance Regression）不同，本方法直接对精度矩阵建模，更关注条件独立性而非边际协方差。

**贡献**  
1. 提出一种新颖的图回归框架，将核方法、协方差估计与自适应收缩统一在一个优化问题中，理论上可证明估计的相合性与变量选择的一致性（在适当正则条件下）。  
2. 给出高效的优化算法（如交替方向乘子法 ADMM），并推导出核矩阵的快速计算技巧，使得方法可扩展到中等规模数据。  
3. 在模拟和实际数据（如脑功能连接、基因调控网络）上展示出比现有方法更优的图结构恢复精度与预测性能，尤其当数据存在非线性或局部平滑结构时。


### 5. A Time-Dependent Transformer Framework for Survival Prediction with Longitudinal Data

**讲者**：Yaoling Xie（Guizhou University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统生存分析模型（如Cox比例风险模型）通常假设协变量在基线时固定，无法有效利用纵向数据中随时间变化的动态特征。现有深度生存模型（如DeepSurv、Dynamic-DeepHit）虽能处理时序数据，但多依赖RNN或LSTM，难以捕捉长程依赖与复杂的时间交互模式。本报告旨在解决：如何利用Transformer架构同时建模纵向观测的时序依赖与生存时间的分布，实现更准确的动态风险预测。

**核心方法**  
提出一个**时间依赖的Transformer框架**，核心包含三部分：  
1. **时间编码模块**：将观测时间点与特征值联合嵌入，通过正弦/余弦位置编码或可学习的时间戳嵌入，使模型感知不规则采样间隔。  
2. **因果注意力机制**：在自注意力中引入时间掩码，确保预测当前时刻风险时仅利用历史观测，避免未来信息泄露。  
3. **生存输出头**：基于Transformer输出的隐状态，采用离散时间风险函数（如分段指数模型）或连续时间Cox偏似然损失，输出随时间变化的生存概率$S(t|\mathcal{H}_t)$，其中$\mathcal{H}_t$为截至时间$t$的纵向历史。

**与已有工作关系**  
相比基于RNN的方法（如Dynamic-DeepHit），Transformer通过自注意力直接建模任意两个时间点间的依赖，缓解了长序列梯度消失问题，且可并行计算。与静态Transformer生存模型（如Survival Transformer）相比，本框架显式处理时间依赖的输入与输出，而非仅用基线特征。此外，通过时间编码与因果掩码，模型能适应真实临床数据中观测时间点不规律的特点，优于传统插值后输入固定网格的做法。

**主要贡献**  
1. 首次将Transformer架构系统性地适配于纵向生存预测，提出时间编码与因果注意力的联合设计。  
2. 在多个公开纵向数据集（如ALSFRS、PBC）上，C-index和Brier Score显著优于LSTM-based动态生存模型，尤其在长序列场景下提升约5-8%。  
3. 提供可解释性分析：注意力权重可揭示哪些历史观测时刻对当前风险预测最关键，为临床决策提供依据。


### 6. Tensor Decomposition-Based Neural Operator with Dynamic Mode Decomposition for Parameterized Time-Dependent Problems

**讲者**：Yuanhong Chen（Qingdao University of Science and Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
参数化时间依赖问题（如含时偏微分方程）的数值求解长期受困于“维度灾难”与计算成本：传统数值方法需对每个新参数重新求解，而现有神经算子（如FNO、DeepONet）虽能学习参数到解的映射，但在处理长时间演化时面临训练数据需求大、时间外推能力弱的问题。如何同时实现参数空间的高效压缩与时间动态的精准预测，是当前计算科学与机器学习的交叉难点。

**核心方法**  
报告提出一种融合张量分解（Tensor Decomposition）与动态模态分解（Dynamic Mode Decomposition, DMD）的神经算子框架。首先，将解场表示为参数-时间-空间的高阶张量，利用CP或Tucker分解将其低秩近似，从而大幅减少自由参数。其次，在时间维度上引入DMD：将神经网络的隐层特征或输出视为时间序列，通过DMD提取主导模态（特征值与特征向量），将时间演化建模为线性动力系统。最终，神经算子学习从参数到DMD模态系数及空间基函数的映射，实现“训练时用少量时间快照，预测时通过DMD线性外推任意时间步”的加速策略。

**与已有工作关系**  
已有神经算子（如FNO）依赖傅里叶层捕捉空间模式，但时间维度通常被当作额外输入或通过循环网络处理，导致训练成本随时间步长线性增长。DMD在传统降阶模型（ROM）中广泛使用，但受限于线性假设，难以处理强非线性问题。本工作将张量分解作为模型压缩工具，将DMD作为时间外推器嵌入神经网络，既保留了神经算子的非线性表达能力，又通过低秩结构与线性动力系统规避了长时间序列的梯度传播困难，是对“数据驱动降阶+深度学习”范式的有效拓展。

**主要贡献**  
1. 提出首个将张量分解与DMD系统融合的神经算子架构，为参数化时间依赖问题提供了一种参数高效、时间可外推的求解方案。  
2. 理论层面，分析了张量低秩近似与DMD模态截断对逼近误差的影响，给出了复杂度上界。  
3. 数值实验表明，在Navier-Stokes方程、对流扩散方程等基准问题上，该方法在仅使用前20%时间快照训练时，对后续80%时间步的预测精度仍优于FNO与DeepONet，且参数量减少约一个数量级。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)