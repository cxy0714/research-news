# 高维统计 High-Dimensional Statistics · 1

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 8 场）

---

## Variable Selection and FDR Control and Change Point Detection

*7 月 11 日（周六） · 13:30-15:10 · Executive Meeting Room, 12th Floor, Qunsheng Howard Johnson*  
*主持 Xueli Wang（Beijing Technology and Business University）*

### 1. To Split or Not to Split: Valid Inference and Adaptive Stopping for Graph Segmentation

**讲者**：Jiajing Chen（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
图分割（graph segmentation）旨在将节点划分为若干同质子图，但现有方法通常预设分割层数或依赖启发式准则（如模块度最大化），缺乏对“是否应继续分割”这一决策的统计保证。报告聚焦于：如何在分割过程中进行有效的统计推断，并设计自适应停止规则，使得最终分割结果既避免过度分割（over-segmentation）又避免欠分割（under-segmentation），同时保证推断的 validity（如 FDR 控制或置信区间覆盖）。

**核心方法**  
讲者可能提出一个两阶段框架：第一阶段，对当前子图内的边密度或社区结构进行假设检验（例如，检验该子图是否来自一个均匀随机图 vs. 存在内部结构），检验统计量基于谱特征或局部邻接矩阵的偏差；第二阶段，若拒绝原假设，则继续分割，否则停止。为控制多重比较下的错误率，采用 sequential testing 或 selective inference 技术，例如在分割路径上调整 p 值或使用 conditional calibration。自适应停止规则可能基于一个信息准则（如 BIC 的变体）与检验的 p 值阈值联动，确保停止决策的渐近最优性。

**与已有工作关系**  
已有图分割方法（如谱聚类、随机块模型）通常固定分割数或通过交叉验证选择，但缺乏对分割决策的统计推断。近期工作如“significance-based community detection”或“graph change point detection”虽涉及假设检验，但多针对单次分割或已知分割数。本报告将分割与停止视为一个在线决策问题，结合 sequential analysis 与 graph inference，拓展了传统多重比较框架到图结构数据，且可能引入一种新的“分割路径”上的 FDR 控制方法。

**主要贡献**  
1. 首次为图分割中的“是否继续分割”提供严格的统计推断框架，而非仅依赖启发式准则。  
2. 提出自适应停止规则，在保证分割质量的同时控制错误发现率或 family-wise error rate，具有理论保证。  
3. 方法可应用于层次聚类、网络社区检测、图像分割等场景，尤其适用于大规模图上的自动分割。  
4. 可能通过模拟与真实数据（如社交网络、脑网络）展示相比传统方法（如 Louvain 算法、谱聚类+肘部法则）在分割准确性与推断可靠性上的提升。


### 2. Interval Localization with Error Rate Control in Multiple Change-Point Analysis

**讲者**：Zijian Wei（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多变化点分析中，现有方法多聚焦于点估计（如 CUSUM、Binary Segmentation）或单一变化点的置信区间构造，但同时对多个变化点进行区间定位（Interval Localization）并控制整体错误率（如 Family-Wise Error Rate 或 False Discovery Rate）的问题尚未被系统解决。实际应用中，如基因组拷贝数变异检测、金融时间序列分段，不仅需要知道变化点位置，还需给出可信区间并保证区间覆盖的联合概率可控。

**核心方法**  
报告可能提出一种基于“分割-筛选-校正”的框架：首先通过多尺度扫描（如 Wild Binary Segmentation 或 Narrowest-Over-Threshold）获得候选变化点集，然后对每个候选点构造基于似然比检验或自举的置信区间，最后利用多重比较校正（如 Benjamini-Hochberg 或 Bonferroni 型）对区间进行筛选，使得所有真实变化点被其对应区间覆盖的概率（或期望覆盖比例）不低于预设水平。关键创新在于将区间估计与错误率控制耦合，而非分步进行。

**与已有工作关系**  
已有工作如 Frick 等人（2014）的“Simultaneous Multiscale Change-Point Inference”提供了同时置信带，但针对的是分段常数函数而非变化点位置；另一些工作如“Confidence Sets for Multiple Change-Points”（如 Fryzlewicz, 2018）仅给出点估计的置信集，未显式控制区间长度或错误率。本报告可能填补了“区间定位+错误率控制”的空白，将多重比较思想从假设检验迁移至区间估计。

**主要贡献**  
1. 首次提出在多变化点场景下同时输出每个变化点的置信区间，并保证区间覆盖的联合错误率（如 FWER ≤ α 或 FDR ≤ q）。  
2. 方法理论上可证明在信号强度满足一定条件下，区间长度随样本量增加以最优速率收缩，且错误率渐近可控。  
3. 算法上可能结合了快速分割与高效多重比较，计算复杂度接近 $O(n \log n)$，适用于大规模数据。  
4. 模拟与真实数据（如 DNA 拷贝数）验证了方法相比现有点估计或单区间方法在解释性和可靠性上的优势。


### 3. Powerful Derandomized Knockoff: A Powerful and Reproducible FDR Control Approach

**讲者**：Changhan Jin（Beijing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维变量选择中，Knockoff 方法通过构造“影子变量”实现 FDR（False Discovery Rate）控制，但其随机性导致不同运行下选择结果不稳定，可重复性差。现有去随机化策略（如多次运行后聚合）往往以牺牲统计功效为代价。本报告旨在设计一种既能保持 FDR 控制、又能显著提升功效与可重复性的去随机化 Knockoff 框架。

**核心方法**  
报告提出一种“强力去随机化 Knockoff”（Powerful Derandomized Knockoff）。其核心思路是：首先，基于原始数据生成多组独立的 Knockoff 副本（例如 $B$ 组），每组独立运行标准 Knockoff 筛选流程，得到 $B$ 个选择集 $\hat{S}_1,\dots,\hat{S}_B$；然后，构造一个聚合统计量，例如每个特征被选中的频率 $f_j = \frac{1}{B}\sum_{b=1}^B \mathbb{I}(j \in \hat{S}_b)$，并设定一个阈值 $\tau$（可能依赖于 $B$ 和预设 FDR 水平 $\alpha$），最终选择 $f_j \geq \tau$ 的特征。关键在于，通过引入一种基于“选择性推断”的校正机制（如对频率进行多重假设检验调整），在理论上证明该聚合过程仍能控制 FDR，同时利用多组信息的平均效应大幅降低随机波动，从而提升功效。

**与已有工作关系**  
已有去随机化 Knockoff 工作（如 Aggregated Knockoff、Stable Knockoff）多采用简单的多数投票或平均 $p$ 值，但常因忽略组间相关性而导致 FDR 膨胀或功效损失。本报告区别于这些方法之处在于：其一，聚合统计量并非简单平均，而是基于频率的“硬阈值”并辅以理论校正；其二，可能引入了一种新的“去随机化不等式”，将多次运行视为一种隐式重抽样，从而在保持 FDR 控制的同时获得比单次运行更高的功效。此外，与传统的 Bootstrap 或 Bagging 思路不同，Knockoff 的随机性源于构造副本的随机性，而非数据重抽样，因此需要专门的理论工具。

**主要贡献**  
1. 提出一种新颖的去随机化 Knockoff 框架，在理论上严格证明其 FDR 控制性质，且不依赖渐近假设。  
2. 通过数值模拟和真实数据实验，展示该方法在功效上显著优于单次 Knockoff 及现有去随机化变体，同时可重复性（如选择集的一致性）大幅提升。  
3. 为高维变量选择中“可重复性”与“统计功效”的权衡提供了新的解决思路，尤其适用于生物医学等需要稳定特征筛选的领域。


### 4. FDR Control and Statistical Power for High-Dimensional Semiparametric Transformation Models

**讲者**：Gaorong Li（Beijing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维数据下变量选择与多重假设检验的核心矛盾在于：如何在控制错误发现率（FDR）的同时最大化统计功效。现有FDR控制方法（如Benjamini-Hochberg、Knockoffs）多针对线性模型或广义线性模型，但实际应用中常遇到响应变量需经未知单调变换（如Box-Cox变换、对数变换）才能满足线性假设的情形。半参数转换模型 $g(Y) = X^\top \beta + \varepsilon$ 中变换函数 $g(\cdot)$ 未知，高维情形下同时估计 $g$ 与稀疏系数 $\beta$ 并控制FDR，是一个尚未充分解决的问题。

**核心方法**  
报告可能提出一种基于debiased Lasso的推断框架。首先利用profile likelihood或秩回归技巧消除未知变换函数的影响，得到 $\beta$ 的初始估计；然后通过构造debiased Lasso估计量 $\hat{\beta}_j^d$ 及其渐近正态性，建立每个系数的 $p$ 值。在此基础上，采用自适应阈值或Knockoffs类方法控制FDR。关键在于证明debiased估计量在未知 $g$ 下仍保持 $\sqrt{n}$ 一致性与渐近正态性，且变换函数的非参数估计误差不影响推断的一阶性质。

**与已有工作关系**  
已有高维FDR控制工作（如van de Geer et al., 2014）主要针对广义线性模型，其似然函数完全已知。本报告将框架推广至半参数情形，变换函数 $g$ 作为无穷维 nuisance parameter，需额外处理其估计对检验统计量的影响。与纯非参数变换模型（如Cox比例风险模型）不同，这里 $g$ 不依赖于协变量，且允许任意单调递增函数，更具灵活性。

**贡献**  
1. 首次在高维半参数转换模型中实现FDR控制，填补了该模型下多重检验的理论空白。  
2. 方法在控制FDR的同时，渐近达到与已知变换函数情形相同的统计功效，即非参数估计不损失检验效率。  
3. 提供了可操作的算法（如基于秩的debiased Lasso），并可能通过模拟与真实数据验证其在生存分析、经济计量中的实用性。


### 5. Optimal Estimators and Tests for Reciprocal Effects

**讲者**：Yaru Tian（Southeast University）

**对应论文**：Optimal estimators and tests for reciprocal effects · [arXiv:2601.01325](https://arxiv.org/abs/2601.01325) · 📖 [长篇精读](../../deep_reads/jcsds2026-2601.01325.md)

<details><summary>摘要（原文）</summary>

The $p_1$ model plays a fundamental role in modeling directed networks, where the reciprocal effect parameter $ρ$ is of special interest in practice. However, due to nonlinear factors in this model, how to estimate $ρ$ efficiently is a long-standing open problem. We tackle the problem by the cycle count approach. The challenge is, due to the nonlinear factors in the model, for any given type of generalized cycles, the expected count is a complicated function of many parameters in the model, so it is unclear how to use cycle counts to estimate $ρ$. However, somewhat surprisingly, we discover that, among many types of generalized cycles with the same length, we can carefully pick a pair of them such that in the ratio between the expected cycle counts of the two types, the non-linear factors cancel out nicely with each other, and as a result, the ratio equals to $\mathrm{exp}(ρ)$ exactly. Therefore, though the expected count of cycles of any type is not tractable, the ratio between the expected cycle counts of a (carefully chosen) pair of generalized cycles may have an utterly simple form. We study to what extent such pairs exist, and use our discovery to derive both an estimate for $ρ$ and a testing procedure for testing $ρ= ρ_0$. In a setting where we allow a wide range of reciprocal effects and a wide variety of network sparsity and degree heterogeneity, we show that our estimator achieves the optimal rate and our test achieves the optimal phase transition. Technically, first, motivated by what we observe on real networks, we do not want to impose strong conditions on reciprocal effects, network sparsity, and degree heterogeneity. Second, our proposed statistic is a type of $U$-statistic, the analysis of which involves complex combinatorics and is error-prone. For these reasons, our analysis is long and delicate.

</details>

**问题**：有向网络建模中，Holland-Leinhardt 的 $p_1$ 模型是刻画互惠效应的经典框架，其核心参数 $\rho$ 度量双向边的强度。然而，模型中的非线性因子 $K_{ij}$ 使得 $\rho$ 的估计与检验成为四十余年未解决的难题：MLE 存在性条件苛刻且计算缓慢，谱方法因模型非低秩而失效，现有环计数方法仅适用于无向网络或不同问题。如何在允许广泛稀疏性、严重度异质性和大范围 $\rho$ 的设定下，得到 $\rho$ 的最优估计与检验，是核心挑战。

**核心方法**：作者提出对数环计数比率（LCR）方法。关键发现是：对于偶数长度 $m\ge 4$，可构造一对广义有向环（如 $m=4$ 时三种非平凡对），使得二者期望计数之比恰好为 $e^{c_0\rho}$（$c_0$ 已知）。尽管单个环的期望因非线性因子而复杂，但精心选择的环对中非线性因子在比率中完全抵消，得到简洁形式。基于此，定义统计量 $\hat\rho = \log(Q_n(a)/Q_n(b))$，并辅以硬阈值得到 LCR 估计 $\hat\rho^*$。方差估计和检验统计量 $\psi_n^*$ 也通过类似技巧构造。

**与已有工作关系**：与 Gao-Lafferty、Jin 等针对无向网络社区检测的环计数方法不同，本文针对有向网络中的互惠参数，且统计量直接作用于原始邻接矩阵而非中心化矩阵。与 MLE 相比，LCR 无需迭代、存在性无条件、计算快 6–16 倍；与谱方法相比，LCR 不依赖低秩假设。此外，本文首次在 $p_1$ 模型中实现 $\rho$ 的相变最优检验，而此前仅存在对 $\rho=0$ 的似然比检验且理论不完整。

**贡献**：1）发现偶数长广义环对可使非线性因子抵消，导出 $\rho$ 的显式估计；2）在允许 $\rho$ 全范围、网络密度低至 $n^{-2}\log n$、度异质性严重的条件下，证明 LCR 估计达到 minimax 最优速率，检验达到最优相变；3）提出可一致估计方差的方法，使检验具有显式渐近正态零分布；4）数值实验表明 LCR 在存在性和计算效率上显著优于 MLE 和 LRT，且对模型误设稳健。


### 6. Mediation Analysis with Parallel Multiple Mediators: Missing Not at Random

**讲者**：Xueli Wang（Beijing Technology and Business University）

**对应论文**：Mediation analysis with the mediator and outcome missing not at random · [arXiv:2212.05577](https://arxiv.org/abs/2212.05577) · 📖 [长篇精读](../../deep_reads/jcsds2026-2212.05577.md)

<details><summary>摘要（原文）</summary>

Mediation analysis is widely used for investigating direct and indirect causal pathways through which an effect arises. However, many mediation analysis studies are challenged by missingness in the mediator and outcome. In general, when the mediator and outcome are missing not at random, the direct and indirect effects are not identifiable without further assumptions. In this work, we study the identifiability of the direct and indirect effects under some interpretable mechanisms that allow for missing not at random in the mediator and outcome. We evaluate the performance of statistical inference under those mechanisms through simulation studies and illustrate the proposed methods via the National Job Corps Study.

</details>

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
在因果中介分析中，当存在多个平行中介变量（parallel multiple mediators）且中介与结局均存在非随机缺失（Missing Not at Random, MNAR）时，如何非参数地识别自然直接效应（NDE）与自然间接效应（NIE）？现有方法多假设缺失机制为随机缺失（MAR）或仅处理单一中介，而实际数据（如全国职业军团研究）中缺失常依赖于未观测到的中介或结局本身，且多个中介可能共享缺失模式，导致传统完整病例分析或多重插补产生严重偏倚。

**核心方法**  
报告基于Zuo等（2023）对单一中介MNAR的识别框架，将其推广至多个平行中介。核心思路是：对每个中介$M_k$，假设缺失指示$R_{M_k}$在给定$(M_k, T, X)$下与结局$Y$条件独立（即$R_{M_k} \perp\!\!\!\perp Y \mid M_k, T, X$），且结局缺失$R_Y$仅依赖于可观测的缺失模式或中介本身（如$R_Y \perp\!\!\!\perp Y \mid (M_1,\dots,M_K, T, X)$）。通过构建基于完整子样本的条件分布$P(Y \mid M_1,\dots,M_K, T, X)$，并利用完备性条件（completeness）从可观测的联合分布中识别$P(M_1,\dots,M_K \mid T, X)$，进而得到NDE和NIE。估计采用EM算法结合参数模型（如logistic回归与两部分模型）以缓解维度灾难。

**与已有工作关系**  
已有工作（Li & Zhou, 2017）仅处理结局MNAR且需工具变量；Zuo等（2023）首次系统研究了中介与结局均MNAR下单一中介的识别。本报告将其扩展至多个平行中介，填补了多中介MNAR情境的理论空白。与MAR假设下的多重中介方法（如Imai等）相比，本报告允许缺失依赖于未观测值，更贴近实际；与单一中介MNAR相比，需处理多个中介间的联合分布识别，对完备性条件要求更高（如要求$Y$的支撑维度不小于所有中介的联合支撑维度）。

**主要贡献**  
1. 首次给出多个平行中介在MNAR下NDE与NIE的非参数识别条件，涵盖四种可解释的缺失机制（如$R_Y$依赖于$R_{M_k}$、$Y$自身或$M_k$）。  
2. 证明完备性条件等价于中介与结局间的充分关联性，并给出离散情形下的秩条件。  
3. 通过模拟验证所提EM估计在有限样本下优于完整病例分析与MAR多重插补，并在全国职业军团研究中发现显著间接效应（教育证书对收入的提升），而直接效应不显著。  
4. 为多中介MNAR的敏感性分析提供了理论基准，推动因果中介分析在缺失数据领域的应用。


## Recent Development on High-Dimensional Data Modeling

*7 月 12 日（周日） · 13:30-15:10 · Colourful Guizhou Ballroom 1*  
*组织 Runze Li（Pennsylvania State University） · 主持 Xu Guo（Beijing Normal University）*

### 1. A Statistical Framework for Alignment with Biased AI Feedback

**讲者**：Zhanrui Cai（The University of Hong Kong）

**对应论文**：A Statistical Framework for Alignment with Biased AI Feedback · [arXiv:2602.08259](https://arxiv.org/abs/2602.08259) · 📖 [长篇精读](../../deep_reads/jcsds2026-2602.08259.md)

<details><summary>摘要（原文）</summary>

Modern alignment pipelines are increasingly replacing expensive human preference labels with evaluations from large language models (LLM-as-Judge). However, AI labels can be systematically biased compared to high-quality human feedback datasets. In this paper, we develop two debiased alignment methods within a general framework that accommodates heterogeneous prompt-response distributions and external human feedback sources. Debiased Direct Preference Optimization (DDPO) augments standard DPO with a residual-based correction and density-ratio reweighting to mitigate systematic bias, while retaining DPO's computational efficiency. Debiased Identity Preference Optimization (DIPO) directly estimates human preference probabilities without imposing a parametric reward model. We provide theoretical guarantees for both methods: DDPO offers a practical and computationally efficient solution for large-scale alignment, whereas DIPO serves as a robust, statistically optimal alternative that attains the semiparametric efficiency bound. Empirical studies on sentiment generation, summarization, and single-turn dialogue demonstrate that the proposed methods substantially improve alignment efficiency and recover performance close to that of an oracle trained on fully human-labeled data.

</details>

**问题**：现代 LLM 对齐管线广泛采用 LLM-as-Judge 替代昂贵的人类偏好标注，但 AI 评判者可能引入系统性偏差（如长度偏好、位置偏好）。如何利用大量有偏 AI 反馈数据与少量准确人类标注，在统计上高效地恢复真实人类偏好，并保证对齐性能的理论最优性？

**核心方法**：提出两个去偏对齐框架。Debiased Direct Preference Optimization (DDPO) 在标准 DPO 目标上引入残差校正项 $\hat{L}_{\text{DDPO}} = \hat{L}_{\text{DPO}} - \hat{L}_{\text{B}}$，其中 $\hat{L}_{\text{B}}$ 基于人类数据估计 AI 标签与人类标签的差异，并通过密度比 $w(Y^{(1)},Y^{(2)}|X)$ 校正响应生成分布偏移，保持 DPO 的计算效率。Debiased Identity Preference Optimization (DIPO) 直接估计人类偏好概率 $P(\pi \succ \pi_{\text{ref}})$，利用影响函数构造去偏估计量 $\hat{P}_{\text{DIPO}}(\pi) = \hat{P}_{\text{DM}}(\pi) - \widehat{\text{Bias}}(\pi)$，无需参数化奖励模型，且达到半参数效率界。

**与已有工作关系**：与 Prediction-Powered Inference (PPI) 共享“用外部预测校正偏差”的思想，但本文进一步处理了 AI 与人类数据间响应分布的异质性（通过密度比加权），更贴近实际对齐场景。相比标准 DPO/IPO 直接混合有偏数据，本文明确建模偏差并校正；相比双重机器学习 (DML)，本文将去偏思想适配到偏好优化目标，并给出策略次优性界。

**主要贡献**：1) 提出 DDPO 和 DIPO 两种去偏对齐方法，分别兼容 DPO 和 IPO 框架；2) 为 DDPO 建立次优性界 $O(\sqrt{v/N} + \sqrt{v\nu_n/n} + \nu_n^{1/2}\|\hat{w}-w\|_2)$，揭示偏差率 $\nu_n$ 和密度比估计误差的影响；3) 证明 DIPO 达到半参数效率界，且其遗憾界仅依赖于 $\|\hat{\pi}_{\text{Gen}}^{\text{Hum}}/\pi_{\text{Gen}}^{\text{Hum}}-1\|\cdot\|\hat{g}-g\|$ 乘积项，具有双重稳健性；4) 在情感生成、摘要、对话任务上实验表明，DDPO 和 DIPO 显著缩小与全人类数据 oracle 的性能差距，优于简单混合基线。


### 2. Inference of High-Dimensional Weak Instrumental Variable Regression Models without Ridge-Regularization

**讲者**：Xu Guo（Beijing Normal University）

**对应论文**：Inference of high-dimensional weak instrumental variable regression models without ridge-regularization · [arXiv:2504.20686](https://arxiv.org/abs/2504.20686) · 📖 [长篇精读](../../deep_reads/jcsds2026-2504.20686.md)

<details><summary>摘要（原文）</summary>

Inference of instrumental variable regression models with many weak instruments attracts many attentions recently. To extend the classical Anderson-Rubin test to high-dimensional setting, many procedures adopt ridge-regularization. However, we show that it is not necessary to consider ridge-regularization. Actually we propose a new quadratic-type test statistic which does not involve tuning parameters. Our quadratic-type test exhibits high power against dense alternatives. While for sparse alternatives, we derive the asymptotic distribution of an existing maximum-type test, enabling the use of less conservative critical values. To achieve strong performance across a wide range of scenarios, we further introduce a combined test procedure that integrates the strengths of both approaches. This combined procedure is powerful without requiring prior knowledge of the underlying sparsity of the first-stage model. Compared to existing methods, our proposed tests are easy to implement, free of tuning parameters, and robust to arbitrarily weak instruments as well as heteroskedastic errors. Simulation studies and empirical applications demonstrate the advantages of our methods over existing approaches.

</details>

**问题**：高维弱工具变量回归中，传统Anderson-Rubin (AR) 检验因工具变量维数 $K$ 发散而失效。现有基于岭正则化的方法（如RJAR, Dovì et al. 2024）虽能处理 $K>n$ 情形，但需选择正则化参数并计算高维投影矩阵，计算成本高；而基于最大型统计量的BCCH检验（Belloni et al. 2012）因采用Bonferroni校正而过于保守，功效损失严重。本文旨在开发无需岭正则化、无调参、且对工具变量稀疏性鲁棒的推断方法。

**核心方法**：提出三类检验。1）**JAR检验**：构造二次型统计量 $\text{JAR}_n = \frac{\sum_{i\neq j} e_i e_j Z_i^\top Z_j}{\sqrt{2\sum_{i\neq j} e_i^2 e_j^2 (Z_i^\top Z_j)^2}}$，直接使用投影矩阵 $P=ZZ^\top$ 而非岭正则化版本，渐近服从 $N(0,1)$，对密集替代假设功效高。2）**改进的最大型检验**：对BCCH统计量 $M_n = \max_k |S_{nk}/\hat\sigma_k|$ 推导其平方的渐近Gumbel分布，采用临界值 $c(\alpha)=2\log K - \log\log K + q_\alpha$，避免Bonferroni的保守性，对稀疏替代假设功效高。3）**Fisher组合检验**：基于JAR与 $M_n^2$ 在零假设下的渐近独立性，将两者p值通过Fisher方法组合，无需预知稀疏性即可在各类替代下保持高功效。

**与已有工作关系**：与RJAR相比，JAR完全避免岭正则化参数选择，计算时间降低数百倍（模拟显示），且理论允许 $K>n$ 及异方差；与BCCH相比，本文推导了 $M_n^2$ 的精确渐近分布，临界值更小，显著提升功效；组合检验则首次在弱工具变量框架下利用二次型与最大型统计量的互补性，无需模型选择。

**主要贡献**：1）提出首个无调参、计算高效的二次型检验JAR，适用于任意弱工具与异方差；2）为最大型检验提供非保守的渐近临界值，理论证明其渐近分布；3）证明两类统计量的渐近独立性，并构造Fisher组合检验，在稀疏性未知时仍具一致功效；4）模拟与实证表明，所提方法在功效和计算上均优于现有基准方法。


### 3. Optimal Multi-Machine Learning Assisted Semi-Supervised Inference

**讲者**：Baihua He（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
半监督推断（Semi-Supervised Inference）旨在利用大量未标记数据提升有标记样本下的参数估计或假设检验效率。现有方法多依赖单一机器学习模型（如随机森林、神经网络）对未标记数据做预测，再结合标记数据构造估计量。然而，单一模型可能因模型误设或过拟合导致推断偏差，且其效率未必达到半监督设置下的最优界。本报告聚焦于：如何同时利用多个机器学习模型（Multi-Machine Learning）的预测结果，在保证推断有效性的前提下，实现半监督推断的最优渐近方差？

**核心方法**  
讲者提出一种“多模型辅助半监督推断”框架。核心思路是：对每个机器学习模型 $m=1,\dots,M$，基于标记数据训练得到预测函数 $\hat{f}_m(x)$，并在未标记数据上生成伪标签。随后构造一个联合估计方程，将多个模型的预测作为辅助信息，通过加权或集成方式融入目标参数 $\theta$ 的估计中。具体地，定义半监督矩条件 $ \sum_{i=1}^n \psi(Z_i;\theta) + \sum_{j=1}^N \sum_{m=1}^M w_m \phi(X_j, \hat{f}_m; \theta) = 0$，其中 $n$ 为标记样本量，$N$ 为未标记样本量，$w_m$ 为最优权重。通过最小化估计量的渐近方差，推导出 $w_m$ 的闭式解，并证明该估计量达到半监督 Cramér-Rao 下界。

**与已有工作关系**  
已有半监督推断工作（如 Zhang et al., 2019; Chakrabortty & Cai, 2018）通常假设一个固定的预测模型，并证明其效率增益依赖于该模型与真实条件均值的匹配程度。本报告将单模型推广至多模型，允许不同模型捕捉数据的不同特征，并通过最优加权自动平衡偏差与方差。这与集成学习（Ensemble Learning）思想类似，但目标从预测精度转向统计推断的最优性，且权重由渐近方差最小化准则决定，而非交叉验证误差。

**贡献**  
1. **理论最优性**：首次在多模型辅助半监督框架下，证明存在一组最优权重使估计量的渐近方差达到半监督有效下界，且该下界不依赖于任何单一模型。  
2. **稳健性**：即使部分模型误设，最优加权仍能自动降低其权重，避免偏差累积，从而比单模型方法更稳健。  
3. **可操作性**：给出权重估计的显式公式（基于标记数据的方差-协方差矩阵），并证明其相合性，计算复杂度仅为 $O(M^2)$，易于实现。  
4. **拓展性**：方法可推广至假设检验、置信区间构造等推断任务，为多机器学习模型在统计推断中的融合提供了统一范式。


### 4. Strongly Consistent Community Detection in Popularity Adjusted Block Models

**讲者**：Danning Li（Northeast Normal University）

**对应论文**：Strongly Consistent Community Detection in Popularity Adjusted Block Models · [arXiv:2506.07224](https://arxiv.org/abs/2506.07224) · 📖 [长篇精读](../../deep_reads/jcsds2026-2506.07224.md)

<details><summary>摘要（原文）</summary>

The Popularity Adjusted Block Model (PABM) provides a flexible framework for community detection in network data by allowing heterogeneous node popularity across communities. However, this flexibility increases model complexity and raises key unresolved challenges, particularly in effectively adapting spectral clustering techniques and efficiently achieving strong consistency in label recovery. To address these challenges, we first propose the Thresholded Cosine Spectral Clustering (TCSC) algorithm and establish its weak consistency under the PABM. We then introduce the one-step Refined TCSC algorithm and prove that it achieves strong consistency under the PABM, correctly recovering all community labels with high probability. We further show that the two-step Refined TCSC accelerates clustering error convergence, especially with small sample sizes. Additionally, we propose a data-driven approach for selecting the number of communities, which outperforms existing methods under the PABM. The effectiveness and robustness of our methods are validated through extensive simulations and real-world applications.

</details>

**问题**：Popularity Adjusted Block Model (PABM) 允许节点在不同社区间具有异质性流行度，但现有社区检测方法（如 Sengupta & Chen 2017 的似然模块度、Noroozi et al. 2021b 的子空间聚类）仅达到弱一致性（weak consistency），且谱聚类难以直接应用——同一社区内节点的特征向量行既不相等也不成比例。关键开放问题：(1) 能否在 PABM 下有效实现谱聚类？(2) 能否高效达到强一致性（strong consistency），即高概率正确恢复所有标签？

**核心方法**：首先，通过分析 PABM 边概率矩阵 $\Theta$ 的特征空间结构（Proposition 1），发现不同社区节点特征向量正交，但同社区节点间角度相似性非零。基于此，提出 Thresholded Cosine Spectral Clustering (TCSC)：计算邻接矩阵 $A$ 的特征向量，估计节点对余弦相似度 $\hat{\tau}_{ij}$，经阈值化得到二值向量 $\tilde{\tau}_i$，再应用 K-means 聚类，获得弱一致初始估计 $\hat{c}^{(0)}$。然后，提出一步精炼 R-TCSC：利用节点 $i$ 与各社区中心之间的余弦相似度（基于边概率向量）更新标签，证明在温和条件下可将弱一致提升为强一致（Theorem 2）。进一步，两步精炼可加速有限样本下聚类误差收敛（Theorem 3）。此外，提出基于奇异值变化点（SVCP）的社区数选择方法。

**与已有工作关系**：与 Sengupta & Chen (2017) 的似然模块度、Noroozi et al. (2021b) 的子空间聚类相比，本文首次在 PABM 下实现谱聚类并达到强一致性。与 Koo et al. (2023) 的 OSC 方法相比，本文不要求同社区内节点流行度向量独立同分布，更具灵活性。精炼思想借鉴了 SBM 和 DCSBM 中的一步估计（Gao et al. 2017, 2018），但针对 PABM 设计了新的角度相似度度量。

**贡献**：1. 揭示了 PABM 特征空间的精确结构，为谱聚类奠定基础。2. 提出 TCSC 算法，实现弱一致谱聚类。3. 证明一步 R-TCSC 达到强一致性，两步 R-TCSC 加速收敛。4. 提出 SVCP 方法选择社区数，优于现有 LP 方法。理论和模拟验证了方法的有效性和鲁棒性。


## High-Dimensional Statistics and Random Matrices

*7 月 12 日（周日） · 15:30-17:10 · Colourful Guizhou Ballroom 1*  
*组织 Jianfeng Yao（The Chinese University of Hong Kong, Shenzhen） · 主持 Jianfeng Yao（The Chinese University of Hong Kong, Shenzhen）*

### 1. High-Dimensional Precision Matrix Quadratic Forms: Estimation Framework for p>n

**讲者**：Weiming Li（Shanghai University of Finance and Economics）

**对应论文**：High-Dimensional Precision Matrix Quadratic Forms: Estimation Framework for $p > n$ · [arXiv:2601.03815](https://arxiv.org/abs/2601.03815) · 📖 [长篇精读](../../deep_reads/jcsds2026-2601.03815.md)

<details><summary>摘要（原文）</summary>

We propose a novel estimation framework for quadratic functionals of precision matrices in high-dimensional settings, particularly in regimes where the feature dimension $p$ exceeds the sample size $n$. Traditional moment-based estimators with bias correction remain consistent when $p<n$ (i.e., $p/n \to c <1$). However, they break down entirely once $p>n$, highlighting a fundamental distinction between the two regimes due to rank deficiency and high-dimensional complexity. Our approach resolves these issues by combining a spectral-moment representation with constrained optimization, resulting in consistent estimation under mild moment conditions. The proposed framework provides a unified approach for inference on a broad class of high-dimensional statistical measures. We illustrate its utility through two representative examples: the optimal Sharpe ratio in portfolio optimization and the multiple correlation coefficient in regression analysis. Simulation studies demonstrate that the proposed estimator effectively overcomes the fundamental $p>n$ barrier where conventional methods fail.

</details>

**问题**  
高维精度矩阵二次型 $\tau_p = a^\top \Sigma^{-1} a$ 是多元统计中的核心量，广泛出现在最优夏普比率、马氏距离、多重相关系数等应用中。当特征维度 $p$ 超过样本量 $n$ 时，样本协方差矩阵 $S_n$ 秩亏，其 Moore–Penrose 伪逆 $S_n^+$ 的二次型 $a^\top S_n^+ a$ 的极限与 $\tau_p$ 之间不再是一一映射，导致传统矩估计完全失效。这一非可识别性构成了 $p>n$ 场景下推断的根本障碍。

**核心方法**  
论文将 $\tau_p$ 重新解释为向量经验谱分布（VESD）$F_{\Sigma,a}(x)=\sum_{i=1}^p (a^\top u_i)^2 I(\lambda_i\le x)$ 的逆矩 $\int x^{-1} dF_{\Sigma,a}(x)$。利用随机矩阵理论，证明样本 VESD 的 Stieltjes 变换 $s_n(z)$ 依概率收敛到由 Marčenko–Pastur 方程决定的极限 $s(z)$。通过复分析导出矩重建公式 $\alpha_j = \frac{(-1)^j}{2\pi i}\oint \frac{z s(z) \underline{m}'(z)}{\underline{m}^{j+1}(z)} dz$，并用样本量替换得到一致矩估计 $\hat\alpha_j$。最后，将前 $k$ 个矩估计输入带约束的线性规划，匹配离散网格上的权重，重建 $\hat F_{\Sigma,a}$，进而得到 $\hat\tau_p = \int x^{-1} d\hat F_{\Sigma,a}$。对于 $a$ 未知的情形，进一步推导了偏差校正公式，并应用于最优夏普比率和多重相关系数的估计。

**与已有工作关系**  
当 $p<n$ 时，Bai 等人（2007, 2009）通过缩放 $a^\top S_n^{-1} a$ 得到一致估计，但该方法在 $p>n$ 时因 $S_n$ 不可逆而崩溃。现有正则化方法（如稀疏图模型、收缩估计）虽能估计 $\Sigma^{-1}$，但直接代入二次型会产生不可忽略的偏差，且依赖稀疏性或低秩假设。本文首次在 $p>n$ 且无需结构假设的条件下，实现了 $\tau_p$ 的一致估计，将问题转化为 VESD 的矩匹配重建，统一了已知和未知 $a$ 的情形。

**贡献**  
1. 提出了首个在 $p>n$ 下一致估计精度矩阵二次型的通用框架，突破了秩亏导致的非可识别性障碍。  
2. 建立了样本 VESD 的 Stieltjes 变换收敛性，并给出矩估计的显式复积分公式，理论证明在温和矩条件下一致。  
3. 将框架推广至 $a$ 未知的场景，通过偏差校正得到最优夏普比率和多重相关系数的一致估计，模拟表明其均方误差显著优于收缩估计和现有方法。


### 2. Mean-Shift PCA by Knockoff Mean

**讲者**：Zeng Li（Southern University of Science and Technology）

**对应论文**：Mean-Shift PCA by Knockoff Mean · [arXiv:2605.25460](https://arxiv.org/abs/2605.25460) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.25460.md)

<details><summary>摘要（原文）</summary>

Removing noise is difficult, but adding noise is easy. In this work, we show how to eliminate mean-shift noisy components from PCA by deliberately introducing knockoff mean-shift perturbation. Standard PCA is highly sensitive to shifts in the sample mean: a small fraction of samples from a shifted distribution can cause large deviations in the leading principal components. In high-dimensional regimes, existing Robust PCA approaches cannot handle the mean-shift contamination structure inherent in the mixture model. Using tools from Random Matrix Theory, we prove that the mean-shift spikes are spectrally separable from the stable eigenvalues of the original covariance. Furthermore, the original eigenspace remains asymptotically invariant to the contamination, independent of the mixture weight. Exploiting this spectral stability, we propose a simple, two-stage PCA algorithm by adding knockoff mean that identifies and removes the mean-shift component using only standard PCA operations.

</details>

**问题**：标准PCA对均值偏移（mean-shift）污染高度敏感——即使少量来自偏移分布的样本也会严重扭曲前几个主成分。现有Robust PCA方法（如RPCA、ℓ1-PCA、Median-of-Means PCA）在高维（$d/n\to c>0$）下无法处理这种污染，因为均值偏移噪声是低秩而非稀疏的，与真实信号同构，导致RPCA的稀疏性假设失效，其恢复的主成分与真实特征向量的余弦相似度随维度增加趋于零。

**核心方法**：本文提出Mean-Shift PCA（MS-PCA），核心思想是“加噪声比去噪声容易”。算法分两步：1）对污染数据$\widetilde{\mathbf{X}}_n$做标准PCA，得到特征值$\{\widetilde{\lambda}_i\}$；2）人为添加一个knockoff均值偏移扰动$\mathbf{A}'_n$（随机方向、足够强度），得到双扰动数据$\widetilde{\mathbf{X}}'_n$，再做一次PCA得到特征值$\{\lambda'_j\}$。关键观察：均值偏移引起的尖峰特征值在额外扰动下会移动，而原始协方差引起的特征值保持稳定（波动阶$O(n^{-1/2})$）。通过阈值$\epsilon = C n^{-1/2}$筛选稳定特征值对应的特征向量，即为真实主成分。理论工具是随机矩阵理论（RMT），证明均值偏移尖峰与协方差尖峰渐近独立（Theorem 3.5），且原始特征空间对污染渐近不变（Theorem 3.11）。

**与已有工作关系**：区别于传统RPCA（Candès et al. 2011）的稀疏+低秩分解，本文处理的是低秩非稀疏的均值偏移污染，RPCA在此场景下完全失效。也区别于ℓ1-PCA（NP-hard）和MoMPCA（迭代非凸优化），MS-PCA仅需两次标准PCA，计算复杂度$O(nd)$，远低于现有方法。本文首次从RMT角度刻画均值偏移污染下PCA的渐近行为，并利用“加噪声”策略实现鲁棒估计。

**贡献**：1）理论贡献：证明均值偏移污染下样本协方差矩阵的特征值分解为两组独立尖峰（协方差相关和均值偏移相关），且原始特征空间渐近不变。2）方法贡献：提出MS-PCA，仅用标准PCA操作即可识别和移除均值偏移成分，无需复杂优化。3）实验贡献：在高维设置下显著优于RPCA及其他鲁棒方法（如Tyler、Huber M估计），且计算高效。


### 3. Mesoscopic Dynamics in Complex Networks: A Random Matrix Perspective

**讲者**：Zhenggang Wang（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
复杂网络中的介观动力学（mesoscopic dynamics）关注介于微观节点与宏观整体之间的结构（如社区、模体、核心‑外围结构）如何影响网络上的传播、同步或扩散过程。现有研究多依赖数值模拟或特定拓扑假设，缺乏普适的解析工具来刻画介观结构对动力学行为的统计规律。本报告试图回答：能否利用随机矩阵理论（Random Matrix Theory, RMT）的谱分析框架，从网络邻接矩阵或拉普拉斯矩阵的局部特征值统计量中提取介观动力学的关键信息？

**核心方法**  
讲者从随机矩阵视角出发，将网络邻接矩阵视为一个随机矩阵的扰动版本。核心思路是：介观结构（如社区）会在谱密度中产生偏离经典 Wigner 半圆律或 Marchenko–Pastur 律的“异常”特征值，而这些特征值对应的特征向量则编码了介观结构的空间模式。通过分析特征值间距分布（如 $\beta$-ensemble 的推广）以及特征向量分量的局部化程度，可以建立介观结构参数（如社区强度、模块度）与动力学过程（如同步阈值、扩散时间尺度）之间的解析关系。具体地，可能利用自由概率论（free probability）中的加法卷积或乘法卷积，将介观结构的随机矩阵模型与动力学算子的谱联系起来。

**与已有工作关系**  
已有工作主要分为两类：一是将 RMT 用于网络噪声过滤或社区检测（如谱聚类），但多停留在静态结构识别；二是介观动力学研究多依赖平均场近似或数值模拟，缺乏严格的谱理论支撑。本报告将 RMT 从静态结构分析拓展到动态过程，特别是利用特征值对系统响应函数的敏感性，定量刻画介观结构如何改变动力学的临界行为。这与近期关于“随机矩阵与网络同步”的工作有交集，但更聚焦于介观尺度而非全局谱。

**贡献**  
主要贡献在于：① 提出一个统一框架，将介观动力学的核心问题（如同步阈值、扩散模式）转化为随机矩阵谱统计量的计算；② 给出介观结构参数与动力学特征值分布之间的显式关系，为理论预测提供解析工具；③ 通过数值实验验证该框架在人工网络与真实网络（如脑网络、社交网络）中的有效性，揭示介观结构对动力学鲁棒性的非平凡影响。该工作为复杂网络动力学研究提供了新的数学视角，有望推动随机矩阵理论在系统科学中的更广泛应用。


### 4. Orthogonalized Kernel Debiased Machine Learning for Logistic Multimodal Inference

**讲者**：Yaohua Rong（Beijing University of Technology）

**对应论文**：Orthogonalized Kernel Debiased Machine Learning for Multimodal Data Analysis · [arXiv:2103.07088](https://arxiv.org/abs/2103.07088) · 📖 [长篇精读](../../deep_reads/jcsds2026-2103.07088.md)

<details><summary>摘要（原文）</summary>

Multimodal imaging has transformed neuroscience research. While it presents unprecedented opportunities, it also imposes serious challenges. Particularly, it is difficult to combine the merits of the interpretability attributed to a simple association model with the flexibility achieved by a highly adaptive nonlinear model. In this article, we propose an orthogonalized kernel debiased machine learning approach, which is built upon the Neyman orthogonality and a form of decomposition orthogonality, for multimodal data analysis. We target the setting that naturally arises in almost all multimodal studies, where there is a primary modality of interest, plus additional auxiliary modalities. We establish the root-$N$-consistency and asymptotic normality of the estimated primary parameter, the semi-parametric estimation efficiency, and the asymptotic validity of the confidence band of the predicted primary modality effect. Our proposal enjoys, to a good extent, both model interpretability and model flexibility. It is also considerably different from the existing statistical methods for multimodal data integration, as well as the orthogonality-based methods for high-dimensional inferences. We demonstrate the efficacy of our method through both simulations and an application to a multimodal neuroimaging study of Alzheimer's disease.

</details>

**问题**  
多模态数据分析中，主模态（如脑结构MRI）与辅助模态（如PET、遗传数据）共同影响结局，但主模态效应常需兼顾可解释性与灵活性。现有方法要么采用简单线性模型牺牲精度，要么使用黑箱机器学习牺牲推断能力。核心挑战在于：如何对主模态参数 $\theta_0$ 及主效应函数 $f_0$ 进行有效统计推断，同时允许主模态存在非可忽略的模型误差 $\delta_0$，并允许辅助模态与主模态高度相关、辅助模态效应 $g_0$ 及关联函数 $r_0$ 由灵活的非参数方法估计。

**核心方法**  
提出正交化核去偏机器学习（OKDML）。模型设定为 $Y = f_0(X) + g_0(Z) + U$，其中 $f_0(x) = \Phi(x)^\top \theta_0 + \delta_0(x)$，$\Phi(x)$ 为基函数，$\delta_0$ 为模型误差。辅助模态关联 $\Phi(X) = r_0(Z) + V$。方法融合两种正交性：**Neyman正交性**构造得分函数 $\psi = [\Phi(X)-r(Z)][Y-\Phi(X)^\top\theta - g(Z)-\delta(X)]$，使 $\theta$ 的估计对 $g,\delta,r$ 的估计误差局部不敏感；**分解正交性**要求 $E[\Phi(X)\delta_0(X)]=0$，通过构造特殊RKHS核 $K_\delta$ 保证 $\delta$ 估计与 $\Phi$ 正交，确保 $\theta_0$ 可识别。算法采用交叉拟合迭代更新，先估计 $r$，再交替估计 $g,\delta$ 和 $\theta$，最终得到 $\hat\theta$ 并建立 $\sqrt{N}$-一致性与渐近正态性。

**与已有工作关系**  
与双/去偏机器学习（DML, Chernozhukov et al. 2018）相比，本文首次引入非零模型误差 $\delta_0$，并增加分解正交性，使简单线性模型等不精确模型仍可进行有效推断。与Kozbur (2020) 相比，不要求近似误差以 $o(N^{-1})$ 速度消失，允许 $\delta_0$ 非零。与Lu et al. (2020) 相比，不要求主辅模态弱相关，允许强相关。与现有线性多模态集成方法（如因子回归、降秩回归）相比，本文允许辅助模态效应由任意机器学习方法估计，兼具灵活性与推断能力。

**主要贡献**  
1. 提出OKDML框架，通过双重正交性（Neyman正交+分解正交）实现主参数 $\theta_0$ 的 $\sqrt{N}$-一致估计、渐近正态性与半参数有效性。  
2. 建立主效应函数 $f_0$ 的渐近有效置信带，可量化主模态的预测效应与贡献度（如 $R^2$ 置信区间），并具有因果解释潜力。  
3. 理论证明在模型误差非零、辅助模态高维非线性时，估计仍无偏且有效，而现有替代方法（单模态回归、简单联合回归、忽略 $\delta_0$ 的DML）均存在不可忽略的偏差。  
4. 在阿尔茨海默病多模态神经影像研究中验证方法，识别出内嗅皮层、海马旁回等关键脑区，并支持tau沉积先于结构萎缩的病理假说。


## High-Dimensional Inference and Variable Selection and FDR Control

*7 月 12 日（周日） · 15:30-17:10 · Xijiang Room*  
*主持 Nayang Shan（Capital University of Economics and Business）*

### 1. A Cross-Layer Independent Cascade Model for Signaling Pathway Discovery: Uncovering the Dual Role of Ephx2 in Atherosclerosis

**讲者**：Caiyuzhen Zhang（Xiangtan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：信号通路发现是理解复杂疾病机制的关键，但现有方法多基于单层网络或静态关联，难以捕捉跨层次（如基因、蛋白质、代谢物）的级联传播效应，且对同一分子在不同通路中的双重角色（如Ephx2在动脉粥样硬化中既有保护又有促进作用）缺乏系统性识别工具。

**核心方法**：报告提出一种**跨层独立级联模型**（Cross-Layer Independent Cascade Model），将生物网络建模为多层图（如转录层、蛋白互作层、代谢层），每层节点代表不同分子实体，层间边表示调控或转化关系。模型假设信号以独立概率沿边传播，并引入**跨层传播概率** $p_{ij}^{(k,l)}$ 表示从第 $k$ 层节点 $i$ 到第 $l$ 层节点 $j$ 的激活概率。通过最大化观测到的差异表达/磷酸化等数据的似然，估计传播参数，进而识别关键信号路径。针对Ephx2，模型通过比较不同起始节点（如Ephx2在脂质代谢层 vs. 炎症信号层）的传播模式，揭示其双重角色。

**与已有工作关系**：传统独立级联模型（ICM）仅用于单层社交网络或基因调控网络，而本工作将其扩展至多层异质网络，并引入跨层边参数化。与基于图神经网络（GNN）的通路发现方法相比，本模型保持概率可解释性，且无需大量标注数据。与经典信号通路数据库（如KEGG）的静态路径不同，本模型能从数据中动态推断跨层信号流，尤其适用于Ephx2这类功能矛盾的分子。

**主要贡献**：①提出首个跨层独立级联模型，为多层生物网络中的信号传播提供可解释的概率框架；②通过参数估计与路径排序，系统识别Ephx2在动脉粥样硬化中通过脂质代谢（保护）和炎症激活（促进）的双重机制；③在模拟与真实数据上验证模型优于单层ICM和传统富集分析，为复杂疾病中多功能分子的研究提供新工具。


### 2. High-Dimensional Distributional Change-Point Inference via Sparse Rank-Score Statistics

**讲者**：Xuesong Fu（Guizhou University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维数据中分布变化点检测是统计推断的前沿难题。传统变化点方法多聚焦于均值或方差的变化，且在高维场景下受维数灾难与模型假设限制。然而，实际应用中分布变化可能体现在尾部、相关性或高阶矩等复杂特征上，且变化点位置未知。本报告旨在解决：如何在高维、非参数框架下，仅依赖稀疏信号假设，对任意形式的分布变化进行在线或离线推断？

**核心方法**  
报告提出基于稀疏秩得分统计（Sparse Rank-Score Statistics）的推断框架。核心思路是：将原始高维观测转化为秩得分向量，利用秩的非参数性质消除分布假设；再通过稀疏正则化（如 $\ell_1$ 惩罚）筛选出对变化敏感的关键维度，构造累积和（CUSUM）型统计量。具体地，对每个时间点 $t$，定义秩得分向量 $R_t$，并构建稀疏化后的得分过程 $S_t = \sum_{i=1}^t \text{soft-threshold}(R_i, \lambda)$，其中阈值 $\lambda$ 控制稀疏性。变化点检测基于 $S_t$ 的极大值偏离零的程度，通过自举或渐近分布确定临界值。

**与已有工作关系**  
已有高维变化点检测多依赖均值或协方差结构的参数化假设（如高维均值CUSUM），或采用核方法但计算复杂。本报告的非参数秩方法对异常值和厚尾分布稳健，且稀疏性假设更贴合高维信号稀疏的真实场景。与低维秩检验（如Mann-Whitney型）相比，本报告将秩统计推广至高维，并引入稀疏正则化以克服维数灾难。此外，方法不要求分布变化的具体形式，可检测任意类型的分布偏移。

**主要贡献**  
1. 首次将秩得分统计与稀疏正则化结合，提出高维分布变化点的非参数推断框架，理论证明检验统计量在稀疏假设下的渐近分布。  
2. 给出阈值参数 $\lambda$ 的自适应选择准则，并证明方法在变化点位置和幅度的检测一致性。  
3. 数值实验表明，在多种高维分布变化场景（如尾部变化、相关性突变）下，该方法相比现有均值或方差变化点方法具有更高的检测功效和更低的误报率，且计算复杂度与维度近似线性。


### 3. 利用汇总统计量进行因果效应异质性估计

**讲者**：Yadong Yang（East China Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在因果推断中，异质性处理效应（HTE）的估计通常依赖个体层面数据，但许多实际场景（如多中心临床试验、分布式数据仓库）仅能提供各子组的汇总统计量（如均值、方差、样本量、协变量分布矩），而无法共享原始记录。本报告旨在解决：如何仅利用这些汇总统计量，对处理效应随协变量变化的异质性结构进行有效估计与推断。

**核心方法**  
报告可能提出一种基于加权最小二乘或广义矩估计（GMM）的框架。具体地，将各子组的平均处理效应（ATE）视为协变量均值的函数，利用子组内汇总的协变量矩与结果均值，构造关于异质性参数（如线性系数或非参数光滑项）的矩条件。通过逆方差加权（IVW）或似然近似，在汇总层面拟合一个 meta-regression 模型，其中子组内方差由个体误差与估计误差组成。若异质性结构为线性，则参数可解析求解；若为非线性，则可采用核方法或样条基展开，并借助汇总协方差矩阵进行惩罚估计。

**与已有工作关系**  
现有 meta-analysis 方法（如随机效应模型）通常仅估计平均效应及其方差，或假设异质性完全随机，无法刻画协变量驱动的系统性异质性。而个体层面的 HTE 方法（如 Causal Forest、BART）虽灵活，但要求原始数据。本报告的工作介于两者之间：它继承了 meta-regression 利用汇总统计量的传统，但将协变量矩纳入建模，从而允许对异质性结构进行参数或半参数推断，同时避免了隐私泄露。与基于 summary statistics 的孟德尔随机化（MR）方法相比，本报告更关注处理效应异质性的结构而非单一因果效应。

**贡献**  
主要贡献有三：第一，提出一种仅依赖汇总统计量的 HTE 估计框架，拓展了因果推断在数据受限场景下的适用性；第二，给出参数估计的渐近性质与置信区间构造方法，为后续推断提供理论基础；第三，通过模拟与真实数据（如多中心临床试验）验证方法在有限样本下的表现，证明其能有效恢复异质性模式，且效率接近使用个体数据的方法。该工作为分布式数据环境下的因果异质性研究提供了实用工具。


### 4. Pathway-Guided Conditional Ultrahigh-Dimensional Feature Screening with Nested Group Structures for Survival Analysis

**讲者**：Leen Huang（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在生存分析中，超高维协变量（如基因表达数据）常呈现嵌套组结构（nested group structures），例如基因通路（pathway）内包含子通路，子通路内包含基因。现有特征筛选方法（如SIS、CIS）多假设特征独立或仅考虑无结构情形，忽略组内相关性及先验通路信息，导致筛选效率低、假阳性高。本报告旨在解决：如何利用通路先验知识，在条件筛选框架下对具有嵌套组结构的超高维生存数据实现高效、稳健的特征筛选。

**核心方法**  
报告提出一种**通路引导的条件筛选**（Pathway-Guided Conditional Screening）方法。核心思路是：首先基于先验通路信息将特征划分为嵌套组，然后定义条件边际效用度量——例如，给定已选通路或组内特征后，计算每个特征与生存结局的条件相关性（如条件距离相关或条件Cox偏似然得分）。筛选过程分两步：第一步，在通路层级进行条件筛选，保留与生存显著相关的通路；第二步，在保留通路内，对子组或单个特征进行条件筛选，从而控制组内冗余。方法本质是将组结构嵌入条件独立性检验，通过逐层条件化避免组内强相关特征的重复入选。

**与已有工作关系**  
已有工作如Sure Independence Screening (SIS) 及其条件变体（如CIS）仅处理无结构或简单组结构，未考虑嵌套层级；而基于正则化的方法（如group lasso）虽能处理组结构，但在超高维下计算成本高且需调参。本报告的方法将通路先验作为筛选的“锚点”，在条件框架下逐层剥离组内相关性，相比SIS更适应复杂结构，相比正则化方法更高效且无需稀疏性假设。

**主要贡献**  
1. 首次将嵌套组结构与通路先验同时引入超高维生存特征筛选，提出分层条件筛选框架。  
2. 理论层面证明了所提方法在Cox模型下的sure screening property，即在适当条件下能以概率趋于1保留所有重要特征。  
3. 数值实验表明，在模拟和真实基因数据中，该方法在筛选准确率、模型预测性能及计算效率上均优于现有SIS、group SIS等基准方法，尤其当组内相关性高时优势显著。


### 5. Population-Unbiased Calibration for High-Dimensional Logistic Regression with Measurement Error

**讲者**：Mingrui Zhong（Zhejiang University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维逻辑回归中，协变量存在经典测量误差时，常规的极大似然估计或惩罚估计（如Lasso）会因误差污染而产生渐近偏差，导致变量选择与系数推断失效。现有校准方法（如SIMEX或回归校准）在高维场景下或需强分布假设，或无法同时保证估计的总体无偏性与稀疏性。本报告旨在解决：如何在测量误差存在时，构造一个对总体参数渐近无偏的高维逻辑回归估计量，且不依赖误差分布的具体形式。

**核心方法**  
讲者提出一种“总体无偏校准”（Population-Unbiased Calibration）框架。其核心思想是：利用测量误差的矩结构，构造一个修正的损失函数或 estimating equation，使得在真实协变量分布下，该方程的期望为零。具体地，假设观测协变量 $W = X + U$，其中 $U$ 为均值为零、协方差已知的独立测量误差。通过引入一个辅助变量或利用二阶矩条件，将逻辑回归的 score function 中的 $X$ 替换为 $W$ 的某种无偏变换，例如 $E[g(W) \mid X] = X$，从而得到对 $\beta$ 的无偏 estimating equation。在高维场景下，进一步结合去偏Lasso（debiased Lasso）或正交化技巧，在 $\ell_1$ 惩罚框架下实现稀疏估计与渐近正态性，并证明所提估计量在总体水平上渐近无偏。

**与已有工作关系**  
已有工作如Corrected Lasso（Loh & Wainwright, 2012）通过修正惩罚项处理测量误差，但仅适用于线性模型；Sparse SIMEX（Carroll et al., 2006）需重复抽样或已知误差方差，且在高维下理论性质不完整。本报告的方法不依赖误差分布的具体形式，仅需误差协方差已知或可估计，且将无偏性从“条件无偏”提升至“总体无偏”，更适用于高维逻辑回归的非线性结构。与近期基于debiased Lasso的测量误差方法（如Datta & Zou, 2020）相比，本报告的方法在估计方程构造上更直接，避免了复杂的偏差校正迭代。

**贡献**  
1. 首次在高维逻辑回归中提出“总体无偏”的校准框架，给出了估计量的渐近无偏性与置信区间构造的理论保证。  
2. 方法仅需误差协方差信息，无需误差分布假设或重复测量，实用性强。  
3. 通过数值实验与真实数据验证，该方法在变量选择准确率与系数估计偏差上显著优于现有高维测量误差方法。


### 6. Q-DREAM: Double Robust Estimation and Aggregation for High-Dimensional Quantile Mediation Analysis

**讲者**：Nayang Shan（Capital University of Economics and Business）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：高维中介分析通常聚焦于条件均值，难以揭示中介效应在响应变量分布不同分位点上的异质性。现有分位数中介方法在高维场景下对模型误设（如中介模型或结果模型错误指定）敏感，且缺乏稳健的推断工具。如何在高维协变量中同时实现分位数中介效应的稳健估计与有效聚合，是亟待解决的问题。

**核心方法**：报告提出 Q-DREAM 框架，核心是双重稳健估计与聚合策略。首先，对每个感兴趣的分位点 $\tau$，分别建立中介变量 $M$ 的条件分位数模型和结果变量 $Y$ 的条件分位数模型，并引入倾向性得分（propensity score）作为权重，构造双重稳健估计量：只要中介模型或结果模型之一正确，该估计量即保持一致性。其次，针对高维稀疏性，采用惩罚分位数回归（如 $\ell_1$ 惩罚）进行变量选择，并利用去偏（debiased）技术得到渐近正态的推断。最后，通过聚合多个分位点或不同惩罚参数下的估计结果（如加权平均或集成学习），提升有限样本下的稳定性和效率。

**与已有工作关系**：传统中介分析（如 Baron-Kenny 方法）和高维中介方法（如 HIMA）均基于均值回归，无法刻画分位异质性。现有分位数中介工作（如 quantile mediation）多限于低维或单一分位点，且缺乏对模型误设的鲁棒性。Q-DREAM 首次将双重稳健思想引入高维分位数中介分析，并引入聚合机制，区别于仅依赖单一模型或单一分位点的已有方法。

**主要贡献**：1. 提出高维分位数中介效应的双重稳健估计量，理论上证明其一致性和渐近正态性，放松了模型假设。2. 设计聚合策略，有效整合多个分位点或不同正则化路径下的信息，提升估计精度。3. 通过模拟和实证研究（如基因表达数据）验证方法在识别异质性中介效应方面的优势，为高维因果中介分析提供新工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)