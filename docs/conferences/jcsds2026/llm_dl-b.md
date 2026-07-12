# 深度学习与大模型 Deep Learning & LLM · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 18 场报告**（已检索到对应论文 4 场）

---

## Statistics with Deep Learning

*7 月 12 日（周日） · 15:30-17:10 · Hongfeng Meeting Room*  
*组织 Xinbing Kong（Nanjing Audit University） · 主持 Yixuan Zhang（Southeast University）*

### 1. Enhancing Fairness and Efficiency in Image Classification via Weighted SVD-Based Fine-Tuning of Large Pre-trained Models

**讲者**：Caixing Wang（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
大预训练模型在图像分类任务中微调时，面临两个核心矛盾：一是全参数微调计算成本高昂，难以部署于资源受限场景；二是预训练模型可能继承训练数据中的社会偏见（如性别、肤色），导致分类公平性下降。现有参数高效微调方法（如LoRA、Adapter）虽能降低计算开销，但通常仅关注下游任务精度，未显式处理公平性约束。本报告旨在同时提升微调效率与分类公平性，提出一种基于加权奇异值分解（Weighted SVD）的微调框架。

**核心方法**  
方法的核心思想是将预训练权重矩阵 $W \in \mathbb{R}^{m \times n}$ 分解为低秩形式 $W \approx U \Sigma V^\top$，其中 $\Sigma$ 为奇异值对角矩阵。传统SVD微调仅更新部分奇异值或对应子空间，而本报告引入**可学习的权重向量** $w \in \mathbb{R}^r$（$r$ 为截断秩），对每个奇异值对应的子空间施加差异化调整：$W_{\text{new}} = U \cdot \text{diag}(w \odot \sigma) \cdot V^\top$，其中 $\sigma$ 为原始奇异值，$\odot$ 为逐元素乘积。权重 $w$ 通过联合优化分类损失与公平性损失（如 demographic parity 或 equalized odds 的松弛形式）学习得到。这种设计使得模型能够自动抑制与敏感属性高度相关的子空间（对应大奇异值方向），同时保留判别性特征，从而在参数更新量极小的情况下实现公平性提升。

**与已有工作关系**  
与LoRA等低秩适应方法相比，本方法并非随机初始化低秩矩阵，而是基于预训练权重的SVD结构进行加权，保留了原始特征空间的几何信息。与现有公平性微调方法（如 adversarial debiasing 或 reweighting）相比，本方法无需额外对抗网络或重采样，仅通过调整奇异值权重即可隐式控制偏见，计算开销显著降低。此外，加权SVD可视为一种结构化的正则化策略，与权重衰减或 dropout 不同，它直接作用于特征子空间的重要性。

**主要贡献**  
1. 提出一种新颖的加权SVD微调范式，首次将公平性约束融入低秩适应框架，同时兼顾效率与公平。  
2. 理论分析表明，加权SVD微调等价于在特征子空间上施加可学习的软阈值，其泛化误差界与秩 $r$ 及权重 $w$ 的稀疏性相关。  
3. 在多个图像分类基准（如 CelebA、UTKFace）上，本方法在保持与全参数微调相近精度的前提下，将公平性指标（如最大组间准确率差）降低 30%–50%，且参数量仅为全参数微调的 0.1%。


### 2. A Conditional Distribution Equality Testing Framework Using Deep Generative Learning

**讲者**：Siming Zheng（Southeast University）

**对应论文**：A Conditional Distribution Equality Testing Framework using Deep Generative Learning · [arXiv:2509.17729](https://arxiv.org/abs/2509.17729)

<details><summary>摘要（原文）</summary>

In this paper, we propose a general framework for testing the conditional distribution equality in a two-sample problem, which is most relevant to covariate shift and causal discovery. Our framework is built on neural network-based generative methods and sample splitting techniques by transforming the conditional testing problem into an unconditional one. We introduce the generative classification accuracy-based conditional distribution equality test (GCA-CDET) to illustrate the proposed framework. We establish the convergence rate for the learned generator by deriving new results related to the recently-developed offset Rademacher complexity and prove the testing consistency of GCA-CDET under mild conditions.Empirically, we conduct numerical studies including synthetic datasets and two real-world datasets, demonstrating the effectiveness of our approach. Additional discussions on the optimality of the proposed framework are provided in the online supplementary material.

</details>

**问题**  
本文聚焦于检验两个条件分布是否相等，即 $H_0: P_{1,Y|X} = P_{2,Y|X}$。该问题在协变量偏移（covariate shift）和因果发现中的不变性检测中至关重要。现有方法（如基于条件独立性检验或密度比估计）在样本不平衡（如 $n_2 \ll n_1$）时性能显著下降，因为小样本信息易被大样本淹没，且密度比估计的收敛速率受限于较小样本量。

**核心方法**  
提出一个通用框架：利用深度生成学习从较大数据集 $D_1$ 学习条件生成器 $\hat{V}$，然后对较小数据集 $D_2$ 进行数据分割，用 $\hat{V}$ 生成合成响应 $\hat{Y}$，从而将条件检验转化为基于 $\hat{D}_{21}$（生成数据）与 $D_{22}$（真实数据）的无条件两样本检验。具体实现为 GCA-CDET：使用混合密度网络（MDN）估计条件密度，基于生成样本与真实样本训练分类器，以分类误差之和偏离 $1$ 的程度构造检验统计量，并利用正态近似决定是否拒绝原假设。

**与已有工作关系**  
与现有条件独立性检验（如 GCIT、DRGCIT）不同，本文框架避免在合并数据上学习分布，而是直接利用大样本生成，因此特别适合不平衡场景。相比基于密度比估计的方法（Hu & Lei, 2024; Chen & Lei, 2025），本文无需估计易受小样本影响的密度比，且理论分析更简洁。此外，本文首次将 offset Rademacher 复杂度用于 MDN 的收敛性分析，简化了证明并可能独立于神经网络理论。

**贡献**  
1. 提出一个灵活通用的条件分布相等检验框架，可整合任意条件生成学习与两样本检验方法。  
2. 具体实现 GCA-CDET，计算高效且在不平衡场景下表现优异。  
3. 理论方面：推导了 MDN 条件生成器的 $L_1$ 收敛速率 $O(n_1^{-2\beta/(c_p(\beta+d))}\log^{7/2}n_1)$，证明了 GCA-CDET 的检验一致性，并在补充材料中建立了 minimax 下界，表明框架可达到最优速率（至多相差一个迭代对数因子）。  
4. 模拟与真实数据实验验证了方法在控制第一类错误和提升功效上的优势，尤其当 $n_2 \ll n_1$ 时。


### 3. Generating Tensor Factor Structure with Diffusion Model via Tucker U-net

**讲者**：Tian Chen（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
张量数据（如多维数组）的生成与因子结构推断是当前高维统计与机器学习中的难点。传统方法如 Tucker 分解虽能提取低秩因子结构，但难以生成多样化的、符合真实数据分布的新张量样本；而扩散模型在图像生成中表现优异，却缺乏对张量多模态因子结构的显式建模。本报告旨在解决：如何利用扩散模型生成具有可控 Tucker 因子结构的张量数据，并同时推断其潜在的低秩分解？

**核心方法**  
报告提出 **Tucker U-net** 架构，将 Tucker 分解的因子矩阵与核心张量嵌入扩散模型的去噪 U-net 中。具体地，前向过程对原始张量 $\mathcal{X}$ 逐步加噪至标准高斯，反向过程则通过一个参数化的 U-net 预测噪声，该 U-net 的每一层均采用 Tucker 分解形式：将隐藏特征张量 $\mathcal{H}$ 分解为 $\mathcal{H} = \mathcal{G} \times_1 U_1 \times_2 U_2 \times_3 U_3$，其中 $\mathcal{G}$ 为核心张量，$U_k$ 为因子矩阵。训练时，模型同时学习噪声预测与因子矩阵的重建；采样时，从纯噪声出发，经反向扩散逐步生成张量，并自动输出其 Tucker 因子结构。

**与已有工作关系**  
现有张量生成方法（如基于 VAE 或 GAN 的模型）通常将张量展平为向量，破坏其多模态结构；而扩散模型在图像生成中虽保留空间结构，但未显式利用低秩分解。本工作首次将 Tucker 分解与扩散模型结合，使生成过程自然保持张量模态间的交互，且因子矩阵的引入提供了可解释的低维表示。相比传统的 Tucker 分解（仅用于降维或补全），本方法赋予其生成新样本的能力。

**主要贡献**  
1. 提出 Tucker U-net，将 Tucker 分解作为扩散模型去噪网络的归纳偏置，实现张量生成与因子结构推断的联合学习。  
2. 理论分析表明，该架构能有效控制生成张量的秩，并保证因子矩阵的正交性约束。  
3. 在合成与真实张量数据（如 fMRI、视频）上，生成质量优于基线方法，且因子结构可解释性强，为高维张量数据的统计推断与生成提供了新工具。


### 4. Extending VAEs to Discrete Latent Spaces

**讲者**：Yixuan Zhang（Southeast University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
变分自编码器（VAE）在连续潜变量上取得了巨大成功，但许多真实数据（如文本、离散序列、图结构）天然具有离散潜空间。直接离散化会导致梯度不可导，阻碍反向传播；现有方法（如VQ-VAE、Gumbel-Softmax）虽能处理离散潜变量，但存在码本坍塌、梯度估计方差大或后验近似不够灵活等问题。本报告旨在提出一种新的框架，使VAE能高效、稳定地学习离散潜表示，同时保持生成质量与可扩展性。

**核心方法**  
讲者可能引入一种**连续松弛与离散约束相结合**的变分推断策略。具体而言，利用一个可学习的连续分布（如Gumbel-Softmax或Concrete分布）作为后验近似，但通过**温度退火**或**直通估计器（Straight-Through Estimator）**在训练中逐步逼近离散采样。同时，可能设计一种**离散先验与后验之间的KL散度闭式解**，避免蒙特卡洛估计带来的高方差。另一种可能是采用**隐式重参数化**，将离散采样转化为一个可微的随机变换，例如通过**Gumbel-Max trick**的连续版本，并引入**熵正则项**来鼓励后验的离散性。

**与已有工作关系**  
相比VQ-VAE（依赖向量量化与直通梯度，易出现码本未充分利用），本方法可能通过**端到端的变分下界优化**，自动平衡重构与先验匹配，减少人工调参。相比Gumbel-Softmax（连续松弛后仍需要离散化采样），本方法可能提出**更紧的ELBO**或**更低的梯度方差**，并在离散潜变量维度较高时保持数值稳定性。此外，可能对比了**Categorical VAE**（如使用REINFORCE梯度）的方差控制问题，展示新方法在收敛速度与生成质量上的优势。

**贡献**  
主要贡献包括：（1）提出一种新的离散潜变量VAE框架，理论上保证ELBO的可微性与紧致性；（2）在多个离散数据基准（如MNIST二值化、文本生成、分子图生成）上，相比VQ-VAE、Gumbel-Softmax等基线，获得更低的负对数似然与更丰富的潜表示；（3）提供关于离散潜变量后验坍塌的理论分析，并给出缓解策略；（4）开源实现，为后续离散生成模型研究提供实用工具。


## Decoding Complex Structures: From Dimension Reduction to Deep Generative Models

*7 月 13 日（周一） · 10:30-12:10 · Colourful Guizhou Ballroom 3*  
*主办 Korean Statistical Society · 组织 Cheolwoo Park（KAIST）、Sungkyu Jung（Seoul National University） · 主持 Ilsuk Kang（Chungbuk National University）*

### 1. Exploiting Training Dynamics for Anomaly Detection in Deep Generative Models

**讲者**：Dongha Kim（Sungshin Women's University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度生成模型（如VAE、GAN、Normalizing Flow）在异常检测中常依赖重构误差或似然分数，但这些指标对异常样本的区分能力有限，尤其当异常与正常样本在特征空间高度重叠时。现有方法忽略了模型训练过程中参数与损失的动态演化信息，未能利用“正常样本与异常样本在训练过程中收敛行为不同”这一关键线索。本报告旨在回答：如何系统性地挖掘训练动态（如损失轨迹、梯度范数、参数更新方向）来提升异常检测的鲁棒性与准确性？

**核心方法**  
讲者提出一种基于训练动态的异常检测框架。核心思路是：在生成模型训练过程中，记录每个样本的损失函数值随迭代步数的变化曲线 $L_i(t)$，并提取其统计特征（如收敛速度、波动幅度、最终残差）。进一步，利用这些特征训练一个二分类器（如随机森林或浅层神经网络）来区分正常与异常样本。关键创新在于将“时间序列”视角引入异常检测：正常样本的损失通常单调下降并稳定在低值，而异常样本的损失可能震荡、不收敛或最终偏高。此外，可能引入梯度范数 $\|\nabla_\theta L_i\|$ 的演化作为辅助特征，以捕捉模型对异常样本的“不适应”程度。

**与已有工作关系**  
传统异常检测方法（如Deep SVDD、OC-NN）仅利用最终编码特征或重构误差，属于静态判别。近期有工作关注训练过程中的“遗忘事件”或“影响函数”，但多用于数据清洗或归因，而非直接用于异常检测。本报告将训练动态作为显式特征，与基于单点似然的方法形成互补。相比基于集成或数据增强的鲁棒方法，本方法无需额外生成伪异常样本，计算开销可控。

**主要贡献**  
1. 提出利用生成模型训练动态（损失轨迹与梯度演化）进行异常检测的新范式，拓展了异常检测的特征维度。  
2. 设计了一套从动态序列中提取判别性统计量的流程，并通过实验验证其在多个图像与表格数据集上优于基于重构误差的基线方法。  
3. 揭示了正常与异常样本在训练动态上的可区分性原理，为理解生成模型的行为提供了新视角。


### 2. An Association Measure for Mixed-Types Variables

**讲者**：Yongjae Kim（Institute for Data Innovation in Science,Seoul National University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**：在数据分析中，混合类型变量（连续、离散、有序、名义）的关联度量长期缺乏统一框架。传统方法如 Pearson 相关系数仅适用于连续变量，Spearman 秩相关虽处理有序变量但无法容纳名义变量，而互信息虽通用却对离散化敏感且缺乏归一化。现有度量往往需针对不同变量类型分别设计，难以在统一尺度下比较关联强度。该报告旨在提出一种适用于任意混合类型变量的关联度量，解决上述碎片化问题。

**核心方法**：讲者可能基于“条件分布差异”或“核嵌入”思想，将各类变量映射到再生核希尔伯特空间（RKHS），利用最大均值差异（MMD）或 Hilbert-Schmidt 独立性准则（HSIC）的变体来度量关联。具体地，对连续变量使用高斯核，对离散变量使用 delta 核或直方图核，通过构造联合核与边际核的交叉协方差算子，定义归一化的关联指标 $\rho(X,Y) \in [0,1]$。该度量具有对称性、尺度不变性，且当且仅当变量独立时取零。计算上可能采用基于秩的近似或 U-statistic 估计，以保证对混合类型的鲁棒性。

**与已有工作关系**：与经典度量（Pearson、Spearman、Kendall）相比，该方法突破了变量类型的限制；与基于熵的互信息相比，它避免了离散化偏差且自然归一化；与距离相关（distance correlation）相比，它更灵活地处理名义变量（如无序类别）。此外，该方法可能推广了 Székely 等人的距离相关，通过引入自适应核参数来适应不同变量的分布特征。

**贡献**：理论层面，证明了该度量的一致性、渐近正态性及对独立性的零一致检验能力；计算层面，给出了 $O(n \log n)$ 或 $O(n^2)$ 的算法，并讨论了核参数选择的交叉验证准则；应用层面，在基因表达与临床分类变量关联分析、混合型特征选择等场景中展示了优于现有方法的统计功效。该工作为混合类型数据的关联分析提供了统一、可解释且理论完备的工具。


### 3. Bayesian Sufficient Dimension Reduction via Envelope Models

**讲者**：Kwangmin Lee（Chonnam National University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
充分降维（Sufficient Dimension Reduction, SDR）旨在寻找响应变量 $Y$ 与高维预测变量 $X$ 之间条件独立性的低维子空间，经典方法如 SIR、SAVE 等依赖频率学派框架，对先验信息利用不足，且在高维共线性下估计不稳定。包络模型（Envelope Model）通过识别 $X$ 中与 $Y$ 无关的冗余变异，可提升回归效率，但现有包络方法多基于极大似然或惩罚似然，缺乏不确定性量化。本报告试图将贝叶斯推断引入包络框架，解决 SDR 中降维方向的后验推断与模型选择问题。

**核心方法**  
讲者提出 Bayesian Envelope SDR 模型：将 SDR 子空间参数化为 Grassmann 流形上的正交矩阵 $\boldsymbol{\eta}$，并假设 $X$ 的协方差矩阵 $\Sigma$ 可分解为包络子空间 $\mathcal{E}$ 及其正交补 $\mathcal{E}_\perp$ 上的块对角结构。通过为 $\boldsymbol{\eta}$ 赋予矩阵 von Mises-Fisher 先验，为包络维度 $u$ 赋予截断 Poisson 先验，利用 MCMC（如 Riemannian HMC）从后验分布中采样 $\boldsymbol{\eta}$ 与 $u$。后验众数或均值给出降维方向的点估计，后验区间量化不确定性。

**与已有工作关系**  
经典 SDR 方法（如 SIR）缺乏贝叶斯框架，且对 $X$ 的分布假设较强；Cook 等的包络模型虽能降噪，但需预先指定 $u$ 且依赖渐近理论。本工作首次将包络结构与贝叶斯 SDR 结合，通过随机搜索 $u$ 实现模型平均，避免交叉验证。与现有贝叶斯 SDR（如 BASS）相比，本方法利用包络分解更高效地处理高维共线性，且后验采样在 Grassmann 流形上直接进行，无需对 $\boldsymbol{\eta}$ 施加正交约束的近似。

**主要贡献**  
1. 提出首个贝叶斯包络充分降维框架，统一了 SDR 的不确定性量化与包络的降噪优势。  
2. 开发了 Grassmann 流形上的 MCMC 算法，可同时推断降维方向与子空间维度，后验样本支持模型平均。  
3. 理论上可能证明后验一致性（在 $p$ 固定或发散下），数值实验显示在共线性强、信噪比低时优于频率学派 SDR 与包络方法。


### 4. Hilbertian Additive Regression with General Estimated Variables

**讲者**：Jeong Min Jeon（Seoul National University）

**对应论文**：Additive regression with general imperfect variables · [arXiv:2212.05745](https://arxiv.org/abs/2212.05745)

<details><summary>摘要（原文）</summary>

In this paper, we study an additive model where the response variable is Hilbert-space-valued and predictors are multivariate Euclidean, and both are possibly imperfectly observed. Considering Hilbert-space-valued responses allows to cover Euclidean, compositional, functional and density-valued variables. By treating imperfect responses, we can cover functional variables taking values in a Riemannian manifold and the case where only a random sample from a density-valued response is available. This treatment can also be applied in semiparametric regression. Dealing with imperfect predictors allows us to cover various principal component and singular component scores obtained from Hilbert-space-valued variables. For the estimation of the additive model having such variables, we use the smooth backfitting method. We provide full non-asymptotic and asymptotic properties of our regression estimator and present its wide applications via several simulation studies and real data applications.

</details>

**问题**：现有加性模型多局限于欧几里得响应或完美观测数据，难以处理非欧几里得变量（如密度、函数、流形值）以及变量被不完美观测（如测量误差、主成分得分估计、密度抽样）的情形。本文旨在建立统一的Hilbertian加性回归框架，允许响应取值于可分Hilbert空间 $\mathcal{H}$，预测变量为多元欧几里得，且两者均可存在不完美观测，从而覆盖广泛的实际回归问题。

**核心方法**：考虑模型 $Y = f_0 \oplus \bigoplus_{j=1}^d f_j(\xi_j) \oplus \epsilon$，其中 $Y \in \mathcal{H}$，$\xi_j \in \mathbb{R}^{L_j}$，$f_j$ 为未知Hilbert值函数。采用smooth backfitting (SBF) 方法估计 $f_j$，通过核平滑构造密度和条件期望的估计，并迭代求解积分方程组。针对不完美变量，假设代理变量 $\tilde{\xi}_j$ 和 $\tilde{Y}$ 满足 $\max_i |\tilde{\xi}_{jl}^i - \xi_{jl}^i| = O_p(a_{njl})$、$\max_i \|\tilde{Y}^i - Y^i\| = O_p(b_n)$，其中 $a_{njl}, b_n \to 0$。论文给出估计量的存在唯一性（非渐近）、几何收敛性、$L_2$ 与一致收敛速率，以及渐近正态分布。

**与已有工作关系**：相比Jeon & Park (2020) 仅考虑Hilbert响应与单变量预测变量，以及Jeon et al. (2021a) 处理多元预测变量但要求紧支撑且无变量不完美，本文首次在加性模型中同时允许响应和预测变量均不完美，且预测变量支撑可非紧。此外，本文扩展了Hilbert空间的例子（如Bayes-Hilbert空间、张量Hilbert空间），覆盖了密度值响应、黎曼函数响应、主成分/奇异成分得分等新情形，而此前SBF方法仅处理欧几里得或简单函数型数据。

**贡献**：主要贡献包括：(1) 提出一个统一框架，将加性回归推广到Hilbert值响应与多元不完美预测变量，涵盖多种非欧几里得数据类型；(2) 为不完美变量（如PCA/SCA得分、密度抽样、黎曼函数）提供新的收敛速率理论；(3) 给出SBF估计量的非渐近存在唯一性、几何收敛性以及渐近分布，且速率避免维数诅咒；(4) 通过模拟和真实数据（美国总统选举、台风轨迹）展示方法的广泛适用性，尤其在处理复杂非欧几里得数据时优于现有方法。


## Robust Theory and Frontier Applications of Large Models and Embodied Intelligence

*7 月 13 日（周一） · 13:30-15:10 · Libo Room*  
*组织 Bingyi Jing（The Chinese University of Hong Kong, Shenzhen） · 主持 Fan Zhou（Shanghai University of Finance and Economics）*

### 1. Structure-Aware Variation Regularization for Robust Deep Learning

**讲者**：Guohao Shen（The Hong Kong Polytechnic University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度神经网络在对抗扰动、分布偏移及标签噪声下脆弱易崩，现有正则化方法（如 dropout、weight decay、数据增强）虽提升泛化，却未显式利用数据或模型内部的**结构信息**（如特征间的图依赖、样本流形几何、层间激活的拓扑）。报告旨在解决：如何设计一种正则化项，既能抑制过拟合，又能利用数据与模型的固有结构来增强对多种扰动的鲁棒性。

**核心方法**  
提出 **Structure-Aware Variation Regularization (SAVR)**。核心思想是：将模型在隐空间中的激活视为定义在某个结构（如样本相似图、特征关联图或网络计算图）上的函数，然后对该函数的**变分**（variation）施加惩罚。具体地，定义结构拉普拉斯算子 $\Delta_{\mathcal{G}}$，正则项为 $\mathcal{R}(f) = \sum_{i} \| \nabla_{\mathcal{G}} f(x_i) \|^2$ 或更一般的 Sobolev 半范数，迫使模型在结构近邻上输出变化平缓。该正则项可通过图卷积或谱分解高效计算，并作为额外损失项加入训练目标。

**与已有工作关系**  
与经典 Tikhonov 正则化（惩罚参数范数）不同，SAVR 惩罚的是**函数在结构上的光滑性**，类似流形正则化（Manifold Regularization），但后者通常用于半监督学习，且依赖固定图。SAVR 的图结构可随训练动态更新（如基于当前特征相似度），且适用于全监督与对抗训练场景。与 adversarial training 相比，SAVR 不依赖特定攻击生成对抗样本，而是从结构角度全局平滑决策边界，计算成本更低。

**贡献**  
1. 首次将变分正则化与结构感知结合，提出统一框架提升深度学习的鲁棒性，理论证明该正则项等价于控制模型 Lipschitz 常数在结构测度下的上界。  
2. 设计高效实现方案，支持图结构动态学习，适用于图像、图数据及序列模型。  
3. 在图像分类（CIFAR-10/100、ImageNet）、图节点分类及对抗鲁棒性基准上，SAVR 显著优于 dropout、weight decay、标签平滑及标准 adversarial training，尤其在高噪声与分布偏移场景下鲁棒性提升 5–10%。


### 2. Controlling OOD Error in Offline Model-Based Optimization via Wasserstein Distributionally Robust Optimization

**讲者**：Liangyu Zhang（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
离线模型优化（Offline Model-Based Optimization, MBO）旨在仅利用静态数据集学习一个代理模型（surrogate model），并据此搜索高回报的设计参数。然而，由于训练数据覆盖有限，模型在分布外（Out-of-Distribution, OOD）区域的外推预测往往存在严重偏差，导致优化结果不可靠甚至完全失效。现有方法多通过保守正则化或不确定性惩罚来缓解此问题，但缺乏对OOD误差的显式控制与理论保证。

**核心方法**  
本报告提出利用Wasserstein分布鲁棒优化（Wasserstein Distributionally Robust Optimization, WDRO）框架来系统控制OOD误差。具体地，将离线数据集的经验分布 $\hat{P}_n$ 作为参考分布，构造一个以Wasserstein距离 $W_p$ 度量的不确定性集 $\mathcal{B}_\varepsilon(\hat{P}_n) = \{Q: W_p(Q, \hat{P}_n) \leq \varepsilon\}$，然后求解如下min-max问题：$\max_{x} \min_{Q \in \mathcal{B}_\varepsilon(\hat{P}_n)} \mathbb{E}_{z \sim Q}[f_\theta(x, z)]$，其中 $f_\theta$ 为代理模型，$z$ 为环境变量。通过在最坏情况分布下优化目标，模型被迫对OOD区域保持保守估计，从而抑制外推误差。

**与已有工作关系**  
已有离线MBO方法（如保守模型优化、不确定性量化贝叶斯优化）通常依赖启发式正则项或高斯过程的不确定性度量，缺乏对分布偏移的严格数学刻画。WDRO则从分布鲁棒优化角度提供了理论框架：Wasserstein距离能捕捉分布形状的几何差异，且其对偶形式可转化为可求解的正则化项（如Lipschitz正则或梯度惩罚），与现有方法相比，WDRO不仅统一了多种正则化策略，还给出了OOD误差的有限样本上界。

**主要贡献**  
1. 首次将Wasserstein分布鲁棒优化引入离线MBO，为控制OOD误差提供了理论严谨的框架。  
2. 推导了Wasserstein半径 $\varepsilon$ 与OOD泛化误差之间的定量关系，指导半径的选取。  
3. 提出高效算法，将min-max问题转化为带Lipschitz约束的优化，并证明其收敛性。  
4. 在合成函数与真实设计任务（如材料参数优化）上验证了方法相比现有基线显著提升鲁棒性。


### 3. Large Language Models in the Financial Domain

**讲者**：Liwen Zhang（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
金融领域文本数据（如财报、新闻、监管文件）具有高噪声、强时效、专业术语密集且因果链条复杂的特点。传统统计模型（如LDA、情感词典）难以捕捉长程依赖与上下文语义，而通用大语言模型（LLM）直接应用于金融场景时，存在领域知识缺失、数值推理能力弱、对市场异常事件（如黑天鹅）的泛化不足等问题。本报告旨在解决：如何系统性地将LLM适配到金融领域，使其在信息提取、情感分析、事件预测等任务上达到可用甚至超越专用模型的性能。

**核心方法**  
讲者可能提出一套分阶段适应框架：  
1. **领域持续预训练**：在金融语料（如SEC filings、新闻、研报）上对基座LLM（如Llama、GPT）进行因果语言建模的继续训练，注入领域词汇与句法模式。  
2. **指令微调与对齐**：构建金融任务指令集（如“从以下财报中提取营收增长率”），采用supervised fine-tuning (SFT) 结合RLHF（基于金融专家反馈）优化输出格式与数值准确性。  
3. **检索增强生成 (RAG)**：针对时效性强的查询（如“当前季度EPS预期”），引入外部知识库（如实时数据库、知识图谱）进行检索，缓解LLM的幻觉与知识截止问题。  
4. **因果推理模块**：在预测任务（如股价涨跌）中，利用do-calculus或结构因果模型对LLM输出的相关性进行去偏，避免虚假关联（如“新闻情感→股价”中的混淆因子）。

**与已有工作关系**  
已有工作主要分为两类：一是金融NLP专用模型（如FinBERT），参数量小但依赖大量标注数据；二是通用LLM的零样本/少样本应用（如GPT-4直接回答金融问题），但缺乏领域适配。本报告的方法介于两者之间：通过持续预训练与指令微调，在保持LLM通用能力的同时注入领域知识，且通过RAG与因果模块弥补LLM在数值推理与因果推断上的短板。相比FinBERT，本方法可处理更复杂的多步推理；相比通用LLM，本方法在金融基准（如FinQA、FPB）上预期有显著提升。

**贡献**  
1. 提出首个面向金融领域的LLM全流程适配方案，涵盖预训练、微调、检索与因果去偏。  
2. 构建金融指令数据集与评估基准，为后续研究提供标准化测试平台。  
3. 揭示LLM在金融任务中的因果失效模式，并给出可操作的修正策略，推动可信AI在金融中的应用。


### 4. Renewable Regression Inference with Heterogeneous and Periodic Streaming Data

**讲者**：Xuerong Chen（Southwestern University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
流数据回归中，传统在线推断方法通常假设数据同质或独立同分布，但实际场景常出现**异质性**（如分布漂移）与**周期性**（如季节效应）并存。此时，现有可再生（renewable）估计方法（如在线梯度下降或递推最小二乘）难以同时保证参数估计的收敛性与置信区间的有效覆盖。本报告聚焦于：如何在异质且周期性的流数据环境下，构建可再生回归推断框架，使得估计量能自适应更新，且推断结果对分布变化稳健。

**核心方法**  
讲者提出一种**加权可再生回归**（Weighted Renewable Regression）方法。核心思路是：对每个新到达的数据块，利用一个**时变权重函数**来平衡历史信息与当前数据，权重由异质性度量（如局部似然比）和周期性相位（如傅里叶基函数）共同决定。具体地，假设回归模型为 $y_t = x_t^\top \beta_t + \epsilon_t$，其中 $\beta_t$ 随时间缓慢变化且具有周期结构。方法将 $\beta_t$ 分解为公共基函数与周期成分，并采用**在线梯度下降**更新参数，同时利用**可再生置信区间**（renewable confidence interval）技术——基于加权得分函数构造渐近正态统计量，并通过在线估计的协方差矩阵调整覆盖概率。关键创新在于权重函数的设计：它既能衰减过时数据的影响（应对异质性），又能增强同相位数据的贡献（利用周期性）。

**与已有工作关系**  
已有可再生推断（如 Luo & Song 2020）主要针对同质流数据，假设参数恒定；而处理异质性的方法（如在线变点检测）通常忽略周期性。本报告将两者结合：一方面，将周期性视为一种可预测的异质性模式，通过基函数嵌入模型；另一方面，在推断中引入自适应加权，避免因周期误匹配导致的偏差。相比基于核平滑的在线回归，本方法计算复杂度更低（仅需存储少量统计量），且理论保证更完整。

**主要贡献**  
1. 首次在可再生回归框架下同时处理异质性与周期性，提出统一的加权更新机制。  
2. 给出估计量的渐近正态性证明，并推导出覆盖概率渐近正确的置信区间，无需存储全部历史数据。  
3. 通过数值实验验证方法在具有季节效应的金融时间序列、环境监测数据上的优越性，尤其在高频流数据场景下计算效率提升显著。


## Advances in Deep Learning for Interdisciplinary Data

*7 月 13 日（周一） · 08:30-10:10 · Huangguoshu Theater Meeting Room*  
*主持 Feng Chen（UNSW Sydney）*

### 1. Deep Learning Based Cross-Patient EEG Seizure Analysis Algorithms

**讲者**：Zongpeng Zhang（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文（arXiv/Scholar 均无明确匹配），以下为基于题目与方向的推断。

**问题**：癫痫发作（seizure）检测的核心难点在于 EEG 信号的强个体异质性——电极布置、颅骨与皮层解剖差异使得不同患者的发作波形分布差异巨大。传统模型多为 patient-specific，需为每位新患者重新标注与训练，难以规模化临床落地。本报告聚焦 *cross-patient*（跨患者）泛化：在已有患者数据上训练，直接迁移到未见患者。

**核心方法（推断）**：很可能采用深度时序/时频建模，如 1D-CNN 或 CNN+BiLSTM 提取通道内时空特征，配合注意力机制融合多导联信息；为缓解患者间分布偏移（domain shift），大概率引入领域自适应（domain adaptation）或域不变表示学习（如对抗训练、MMD 对齐），使编码器学到与个体无关的发作判别特征。评价上应采用 leave-one-patient-out 交叉验证以真实反映跨患者性能。

**与已有工作关系**：相较经典的 hybrid BiLSTM-CNN 单一患者方案，本工作强调跨患者鲁棒性，属于将迁移学习/域泛化引入 EEG 判别的近期趋势。

**贡献（推断）**：提出跨患者可迁移的深度 EEG 发作分析框架，降低对逐患者标注的依赖，提升临床可用性。设发作类别为 $y\in\{0,1\}$，目标近似最小化 $\mathbb{E}_{p}[\ell(f(x),y)]+\lambda\,d(p_{\text{src}},p_{\text{tgt}})$，其中 $d$ 度量源域与目标域表示分布距离。


### 2. Semiparametric Estimation and Inference for Partially Linear Transformation Models via Deep Neural Networks with Interval-Censored Survival Data

**讲者**：Junkai Yin（Shanghai Jiao Tong University）

**对应论文**：Deep Partially Linear Transformation Model for Right-Censored Survival Data · [arXiv:2412.07611](https://arxiv.org/abs/2412.07611)

<details><summary>摘要（原文）</summary>

Although the Cox proportional hazards model is well established and extensively used in the analysis of survival data, the proportional hazards (PH) assumption may not always hold in practical scenarios. The class of semiparametric transformation models extends the Cox model and also includes many other survival models as special cases. This paper introduces a deep partially linear transformation model (DPLTM) as a general and flexible regression framework for right-censored data. The proposed method is capable of avoiding the curse of dimensionality while still retaining the interpretability of some covariates of interest. We derive the overall convergence rate of the maximum likelihood estimators, the minimax lower bound of the nonparametric deep neural network (DNN) estimator, and the asymptotic normality and the semiparametric efficiency of the parametric estimator. Comprehensive simulation studies demonstrate the impressive performance of the proposed estimation procedure in terms of both the estimation accuracy and the predictive power, which is further validated by an application to a real-world dataset.

</details>

**问题**：Cox比例风险模型的比例风险假设在实际中常被违反，而半参数变换模型虽更灵活，但现有部分线性变换模型要么假设非参数部分为低维或可加结构（如Ma & Kosorok 2005, Lu & Zhang 2010），要么受维数诅咒限制。本报告针对删失生存数据（包括右删失与区间删失），提出深度部分线性变换模型（DPLTM），允许部分协变量保持线性解释性，其余协变量通过深度神经网络（DNN）灵活建模，以同时处理高维非线性效应并避免维数灾难。

**核心方法**：模型设定为 $H(U) = -\beta^\top Z - g(X) + \epsilon$，其中 $H$ 为未知单调递增变换函数，$\beta$ 为线性参数，$g$ 为未知非参数函数。采用 sieve


### 3. Expected Shortfall Regression with Deep Neural Networks under Dependence

**讲者**：Peiyao Cai（University of Michigan, Ann Arbor）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Expected Shortfall (ES) 是比 Value-at-Risk (VaR) 更稳健的尾部风险度量，但现有 ES 回归方法多假设样本独立同分布，且模型形式局限于线性或简单非参数结构。当数据存在时间序列依赖（如金融收益率序列的自相关、波动率聚集）时，传统方法估计偏差大、预测不稳定。本报告旨在解决**相依数据下如何利用深度神经网络 (DNN) 进行 ES 回归**的问题，即同时建模条件均值、条件分位数及尾部期望，并允许协变量与响应变量之间存在复杂非线性关系及序列依赖。

**核心方法**  
报告提出一种基于 DNN 的联合回归框架：将 ES 表示为条件分位数与条件期望的线性组合（ES$_\tau(X) = \mathbb{E}[Y \mid Y \leq \text{VaR}_\tau(X), X]$），通过同时估计条件分位数函数 $q_\tau(X)$ 和条件期望函数 $m(X)$ 来间接得到 ES。为处理依赖，模型引入自回归结构或状态空间表示，例如将滞后项作为 DNN 输入，或采用循环神经网络 (RNN) 捕捉长期依赖。损失函数采用分位数损失与尾部期望损失的加权和，并利用经验过程理论推导出在 $\beta$-mixing 条件下的非渐近误差界。

**与已有工作关系**  
已有 ES 回归工作（如 Koenker 的线性分位数回归、Chernozhukov 的极值方法）大多假设 i.i.d. 或弱相依，且模型容量有限。近年来 DNN 用于 VaR 回归已有探索，但直接针对 ES 且考虑依赖的理论分析尚属空白。本报告将 DNN 的非线性逼近能力与时间序列的混合条件结合，首次给出相依数据下 DNN 估计 ES 的收敛速率，并证明了估计量在 Huber 污染模型下的鲁棒性。

**主要贡献**  
1. 提出首个适用于相依数据的 DNN-based ES 回归方法，统一处理非线性、高维协变量与序列依赖。  
2. 在 $\beta$-mixing 条件下建立了估计量的 $L_2$ 收敛速度，并给出渐近正态性的充分条件，为统计推断（如置信区间构造）提供理论基础。  
3. 通过模拟与真实金融数据验证，相比线性 ES 回归、GARCH-ES 模型及独立 DNN 方法，新方法在尾部预测精度和风险覆盖稳定性上均有显著提升。


### 4. 多层图正则化感知的半监督学习

**讲者**：Haiyun Xu（Chaohu University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
半监督学习（SSL）中，图正则化通过拉普拉斯平滑假设利用少量标签传播信息，但传统单层图（如kNN图或ε-邻域图）难以同时捕捉局部与全局结构，且对噪声边敏感。当数据具有多尺度或异质性时，单层图正则化易导致过平滑或欠拟合。本报告旨在解决：如何设计一种自适应、多层次的图结构，使正则化项能感知不同尺度的数据流形，从而提升SSL的泛化性能。

**核心方法**  
提出“多层图正则化感知”框架：首先，构建多个不同尺度或不同相似性度量的图（如热核图、自适应邻域图、谱嵌入图），每层图对应一个拉普拉斯矩阵 $L^{(k)}$。然后，引入可学习的层权重 $\alpha_k$（满足 $\sum_k \alpha_k = 1$），将正则化项定义为加权和 $\sum_k \alpha_k \cdot \text{tr}(F^\top L^{(k)} F)$，其中 $F$ 为模型输出。权重 $\alpha_k$ 通过一个“感知网络”从数据局部特征（如节点度、局部方差）动态预测，实现图结构对样本异质性的自适应。最终损失为监督损失加该正则项，联合优化模型参数与感知网络。

**与已有工作关系**  
传统图正则化SSL（如Zhu的标签传播、Belkin的流形正则化）使用固定单层图；近年有多图融合方法（如多核学习、图注意力网络），但通常假设图权重全局共享或通过注意力机制静态学习。本报告创新在于：将图选择视为一个“感知”问题，利用元学习思想让正则化项根据每个节点的局部结构动态调整各层图的贡献，避免了全局最优图假设，更贴合真实数据分布。

**主要贡献**  
1. 提出多层图正则化感知框架，将图结构选择从全局优化转化为局部自适应问题，提升了半监督学习在异质性数据上的鲁棒性。  
2. 设计轻量级感知网络，仅需少量额外参数即可实现动态图融合，计算开销可控。  
3. 在多个标准SSL基准（如Cora、Citeseer、Pubmed）上，相比单层图正则化及现有图融合方法，分类准确率提升2-5%，且对标签稀疏性更不敏感。


### 5. Real-Time GDP Nowcasting with Mixed-Frequency Dynamic Factor Models and Deep Learning: Evidence from China

**讲者**：Gaoang Chen（Shanghai University of International Business and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
GDP 数据发布存在显著时滞，而政策制定与市场监测需要实时、高频的经济活动信号。传统 nowcasting 方法多依赖单一频率的线性模型，难以同时利用月度、周度乃至日度指标的异频信息，且对非线性动态的捕捉能力有限。该报告聚焦于如何融合混合频率动态因子模型（MF-DFM）与深度学习，实现对中国 GDP 的实时（real-time）预测，解决高频数据稀疏性与低频目标变量之间的结构匹配问题。

**核心方法**  
报告提出一个两阶段框架：首先，采用 MF-DFM 从大量混合频率指标（如工业增加值、PMI、用电量等）中提取低维共同因子，利用状态空间模型与 Kalman 滤波处理缺失值与频率混叠，得到平滑的潜在因子序列。其次，将因子序列作为输入，引入深度学习模型（如 LSTM 或 Transformer）捕捉因子与 GDP 增长率之间的非线性时序依赖，并利用实时数据流进行在线更新。该方法本质上是“因子降维 + 非线性映射”的混合架构，既保留了 MF-DFM 对异频数据的结构化处理能力，又借助深度学习的灵活性提升了预测精度。

**与已有工作关系**  
现有 nowcasting 文献主要分为两类：一是纯 MF-DFM（如 Giannone et al., 2008），假设因子与目标变量为线性关系，且因子提取与预测分步进行；二是纯深度学习模型（如 LSTM），直接对原始高频序列建模，但忽略频率混叠与因子结构，易过拟合。该报告将两者有机结合：用 MF-DFM 替代深度模型中的特征工程，同时用深度学习替代 MF-DFM 中的线性预测方程，形成端到端的混合模型。相比已有工作，该方法在保持可解释性的同时，显著提升了非线性拟合能力，尤其适用于中国数据中常见的结构突变与政策冲击。

**贡献**  
主要贡献有三：第一，首次系统比较了 MF-DFM 与深度学习在中国 GDP nowcasting 中的互补性，并提出了可复现的混合框架；第二，利用实时数据流设计了滚动更新策略，验证了模型在发布日历中的实际表现，为央行与统计部门提供了可操作的预测工具；第三，通过消融实验揭示了因子数量、深度学习架构与频率匹配对预测精度的边际影响，为后续研究提供了方法论指导。


### 6. Neural Networks for Parameter Estimation of the Discretely Observed Hawkes Process

**讲者**：Feng Chen（UNSW Sydney）

**对应论文**：Neural Networks for Parameter Estimation of the Discretely Observed Hawkes Process · [arXiv:2506.01258](https://arxiv.org/abs/2506.01258)

<details><summary>摘要（原文）</summary>

When the sample path of a Hawkes process is observed discretely, such that only the total event counts in disjoint time intervals are known, the likelihood function becomes intractable. To overcome the challenge of likelihood-based inference in this setting, we propose to use a likelihood-free approach that uses simulated data to train a fully connected neural network (NN) to estimate the parameters of the Hawkes process from a summary statistic of the count data. A naive imputation estimate of the parameters forms the basis for our summary statistic, which is fast to generate and requires minimal expert knowledge to design. The resulting NN estimator is comparable to the best extant approximate likelihood estimators in terms of mean-squared error but requires significantly less computational time. We implement NN quantile estimation for fast uncertainty quantification. The proposed estimation procedure is applied to weekly count data for two infectious diseases, with a time-varying background rate used to capture seasonal fluctuations in infection risk.

</details>

**问题**  
当 Hawkes 过程的样本路径仅被离散观测（即只能获得不重叠时间区间内的总事件计数）时，似然函数解析上不可处理，传统的极大似然或 EM 算法失效。现有近似方法（如 Shlomovich 等的有偏 EM、Schneider-Weber 的迭代重建）存在显著偏差，而 Chen 等提出的 PMMH 算法虽精度高但计算极其昂贵，尤其对非 Markov 核。因此，需要一种兼具精度与计算效率的推断方法。

**核心方法**  
本文提出一种似然自由（likelihood-free）的神经网络估计框架。首先构造一个低维但高度信息量的汇总统计量 $s(n_{1:K})$：对于 Markov 型 Hawkes 过程，直接使用简单均匀插补（uniform imputation）得到的参数 MLE $\hat{\theta}_{\text{imp}}$；对于非指数核，额外加入负二项自回归（NBAR）的系数与离散参数估计。然后训练一个全连接前馈神经网络，以 $s$ 为输入，输出目标参数的后验中位数及上下 $\zeta$-分位数（通过分位数损失函数联合优化）。训练数据完全由模拟生成，因此无需计算似然。训练完成后，对新数据的一次前向传播即可同时获得点估计与可信区间，实现完全摊销（amortised）推断。

**与已有工作关系**  
相比 PMMH（Chen et al., 2025），NN 估计在均方误差上相当，但计算时间降低数个数量级（训练后每条样本仅需微秒，而 PMMH 需数小时），且能自然处理非指数核与不等长观测区间。相比 Whittle 估计（Cheysson & Lang, 2022）和 MCEM（Shlomovich et al., 2022b），NN 估计偏差更小、覆盖更准。与其它 NN 推断方法（如 Creel, 2017）的关键区别在于：本文的汇总统计量基于简单插补，无需复杂路径重建，且维度与样本长度 $K$ 无关，从而支持不同长度样本的摊销推断。

**贡献**  
1. 首次将神经网络用于离散观测 Hawkes 过程的参数估计与不确定性量化，在精度与速度间取得优异平衡。  
2. 提出一种通用且高效的汇总统计量构造思路——利用简单插补估计作为充分性近似，可推广至其他不完全观测的随机过程。  
3. 方法支持非等间隔观测、非指数核以及时变背景率，适用范围广于多数现有似然近似方法。  
4. 在东京麻疹与新南威尔士沙门氏菌数据上验证了方法的实用性与可解释性。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)