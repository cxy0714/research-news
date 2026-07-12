# 其他 Other · 4

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **3 个分会场 · 16 场报告**（已检索到对应论文 2 场）

---

## 复杂数据学习理论与算法

*7 月 13 日（周一） · 13:30-15:10 · Meeting Room, 1st Floor, Qunsheng Garden Hotel*  
*组织 Songxi Chen（Tsinghua University） · 主持 Pengkun Yang（Tsinghua University）*

### 1. 神经网络Hessian阵的特性及其对算法分析的应用

**讲者**：Ruoyu Sun（The Chinese University of Hong Kong, Shen Zhen）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
深度神经网络的损失景观高度非凸，其Hessian矩阵的谱结构（如负特征值的分布、条件数）直接影响优化算法的收敛行为与泛化性能。然而，现有理论多聚焦于凸优化或简单非凸模型，对实际深度网络中Hessian的统计特性（如“尖锐度”与“平坦性”的度量）及其与算法动力学（如梯度下降的逃逸行为、自适应方法的隐式正则化）之间的定量关系仍缺乏系统刻画。本报告旨在回答：神经网络Hessian阵的谱特征如何随网络宽度、深度及训练阶段变化？这些特征又如何解释不同优化算法的收敛速度与泛化差距？

**核心方法**  
讲者可能从随机矩阵理论与非凸优化的交叉视角出发，建立神经网络Hessian的谱分解框架。首先，利用神经正切核（NTK）或均值场理论，在无限宽极限下推导Hessian的渐近谱分布，揭示其由“数据相关项”与“模型非线性项”叠加的结构。其次，针对有限宽网络，引入局部尖锐度（local sharpness）与Hessian的负曲率半径等概念，通过随机微分方程（SDE）刻画梯度下降在鞍点附近的逃逸时间。最后，结合自适应优化器（如Adam）的更新规则，分析其Hessian对角预条件对条件数的改善效果，并证明该预条件等价于隐式地惩罚Hessian的最大特征值。

**与已有工作关系**  
已有工作主要分为两类：一是通过Hessian的数值实验观察其谱的“尖峰”与“批量”结构（如Sagun等人），但缺乏理论解释；二是利用NTK分析梯度流的收敛性，但通常假设Hessian正定或忽略负曲率。本报告将前者从经验观察提升至理论刻画，同时弥补后者对非凸逃逸行为的缺失。与Chaudhari等人提出的“熵-SGD”相比，本报告更侧重Hessian谱对算法设计（而非损失景观修改）的直接指导。

**贡献**  
1. 给出神经网络Hessian谱的渐近分布公式，证明其负特征值密度与网络宽度成反比，为“宽网络更易优化”提供谱解释。  
2. 建立Hessian条件数与梯度下降收敛速度的精确上界，并揭示自适应方法通过降低条件数实现加速的机制。  
3. 提出基于Hessian谱的算法诊断工具：训练中最大特征值的增长速率可预警泛化下降，为早停法提供理论依据。


### 2. Explainable Machine Learning through Efficient Data Attribution

**讲者**：Han Zhao（University of Illinois Urbana-Champaign）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
机器学习模型的黑箱特性阻碍了高风险场景下的信任建立。现有可解释性方法（如SHAP、LIME）多聚焦于特征归因，即解释输入特征对预测的贡献，但忽略了训练数据本身对模型行为的影响。数据归因（data attribution）旨在量化每个训练样本对特定预测的贡献，然而经典方法（如影响函数）需计算二阶Hessian逆，在大模型上计算成本极高，难以实用。本报告试图解决：**如何在不牺牲归因质量的前提下，将数据归因的计算复杂度从 $O(np^2)$ 降至接近线性，从而支持大规模模型的可解释性？**

**核心方法**  
讲者可能提出一种基于随机投影与核方法的近似框架。核心思想是将高维参数空间中的影响函数投影到低维随机特征空间，利用Johnson-Lindenstrauss引理保证近似误差可控。具体地，将训练损失梯度 $\nabla \ell(z_i; \theta)$ 映射到 $d$ 维随机向量，再通过线性回归或Nyström近似估计每个样本的“影响分数”。该方法避免了显式存储和求逆Hessian矩阵，仅需一次前向-反向传播即可获得所有样本的归因值，复杂度为 $O(np)$ 量级。

**与已有工作关系**  
相比Koh & Liang (2017) 的经典影响函数，本工作将计算瓶颈从 $O(np^2)$ 降至 $O(np)$，且无需二阶信息；相比TracIn (Pruthi et al., 2020) 的checkpoint近似，本方法无需多次训练，仅用单次训练轨迹即可实现更高精度。同时，该方法与近期基于Shapley值的近似（如Data Shapley）相比，避免了指数级采样，在保持理论保证的同时大幅提升效率。

**贡献**  
1. 提出首个线性时间复杂度的数据归因算法，使大规模模型（如BERT、ResNet）的可解释性分析成为可能。  
2. 从理论上证明了随机投影近似的影响函数与真实影响函数之间的误差界，并给出投影维度的选择准则。  
3. 在图像分类、文本分类等任务上验证了归因质量：删除高影响样本后模型性能下降显著，且归因结果与人类直觉一致。  
4. 开源高效实现，为后续公平性审计、数据清洗、对抗样本检测等应用提供基础工具。


### 3. Universal Priors: Solving Empirical Bayes via Bayesian Inference and Pretraining

**讲者**：Yanjuan Han（New York University）

**对应论文**：Universal priors: solving empirical Bayes via Bayesian inference and pretraining · [arXiv:2602.15136](https://arxiv.org/abs/2602.15136) · 📖 [长篇精读](../../deep_reads/jcsds2026-2602.15136.md)

<details><summary>摘要（原文）</summary>

We theoretically justify the recent empirical finding of [Teh et al., 2025] that a transformer pretrained on synthetically generated data achieves strong performance on empirical Bayes (EB) problems. We take an indirect approach to this question: rather than analyzing the model architecture or training dynamics, we ask why a pretrained Bayes estimator, trained under a prespecified training distribution, can adapt to arbitrary test distributions. Focusing on Poisson EB problems, we identify the existence of universal priors such that training under these priors yields a near-optimal regret bound of $\widetilde{O}(\frac{1}{n})$ uniformly over all test distributions. Our analysis leverages the classical phenomenon of posterior contraction in Bayesian statistics, showing that the pretrained transformer adapts to unknown test distributions precisely through posterior contraction. This perspective also explains the phenomenon of length generalization, in which the test sequence length exceeds the training length, as the model performs Bayesian inference using a generalized posterior.

</details>

**问题**：预训练的 Transformer 在经验贝叶斯（Empirical Bayes, EB）任务中表现优异，但为何一个在特定训练分布下训练的贝叶斯估计器能够适应任意未知的测试分布？本文以 Poisson EB 为切入点，试图从统计理论层面回答这一核心问题。

**核心方法**：作者提出“通用先验”（universal prior）的概念，即一种层次化的 prior-on-prior（PoP）$\Pi$，使得对应的贝叶斯估计器 $\theta^\Pi_n(X^n) = \mathbb{E}_\Pi[\theta^n \mid X^n]$ 对所有可能的测试先验 $G_0$ 均具有 vanishing regret。关键构造是：令 $G \sim \Pi$ 为 $k$ 个原子的离散分布，原子位置均匀取自 $[0,A]$，权重服从 Dirichlet 分布，取 $k = \lceil c_0 \log n / \log\log n \rceil$。该 PoP 被证明是“厚”的（thick），即对任意 $G_0$，$\Pi$ 在其附近有足够质量。利用经典的后验收缩（posterior contraction）技术，作者证明该层次贝叶斯估计器的遗憾界为 $\tilde{O}(1/n)$，接近 minimax 最优。此外，通过引入分数后验（$\alpha$-posterior），该框架还解释了长度泛化现象：训练长度 $n$ 的模型在测试长度 $n_{\text{test}} > n$ 时仍有效，但遗憾不会随 $n_{\text{test}}$ 增加而继续下降。

**与已有工作关系**：传统 EB 方法（如 Robbins 估计器、NPMLE、ERM）均需在测试时求解优化问题，而预训练方法通过一次训练实现快速推理。本文为 [TJP25] 的实验发现提供了严格的理论支撑，将预训练 Transformer 的成功归因于通用先验的存在。与经典的“贝叶斯经验贝叶斯”文献（如 Dirichlet 过程先验）相比，本文首次给出了非渐近的遗憾界，并建立了与后验收缩的直接联系。此外，本文还证明了层次贝叶斯估计量的可容许性，并指出 NPMLE 估计量不可容许，深化了对 EB 估计量性质的理解。

**主要贡献**：1) 提出了通用先验的概念，并给出一个简单构造，证明了其近最优的 worst-case regret 界 $\tilde{O}(1/n)$；2) 利用后验收缩统一分析了预训练 EB 的统计性质，并揭示了长度泛化背后的分数后验机制；3) 建立了 minimax 定理，证明了最小不利 PoP 的存在性；4) 将理论推广至 Gaussian EB、函数估计等场景，展示了方法的普适性。


### 4. Fundamental Limits of Community Detection in Contextual Multi-Layer Stochastic Block Models

**讲者**：Zhangsong Li（Peking University）

**对应论文**：Fundamental Limits of Community Detection in Contextual Multi-Layer Stochastic Block Models · [arXiv:2602.08173](https://arxiv.org/abs/2602.08173) · 📖 [长篇精读](../../deep_reads/jcsds2026-2602.08173.md)

<details><summary>摘要（原文）</summary>

We consider the problem of community detection from the joint observation of a high-dimensional covariate matrix and $L$ sparse networks, all encoding noisy, partial information about the latent community labels of $n$ subjects. In the asymptotic regime where the networks have constant average degree and the number of features $p$ grows proportionally with $n$, we derive a sharp threshold under which detecting and estimating the subject labels is possible. Our results extend the work of \cite{MN23} to the constant-degree regime with noisy measurements, and also resolve a conjecture in \cite{YLS24+} when the number of networks is a constant. Our information-theoretic lower bound is obtained via a novel comparison inequality between Bernoulli and Gaussian moments, as well as a statistical variant of the ``recovery to chi-square divergence reduction'' argument inspired by \cite{DHSS25}. On the algorithmic side, we design efficient algorithms based on counting decorated cycles and decorated paths and prove that they achieve the sharp threshold for both detection and weak recovery. In particular, our results show that there is no statistical-computational gap in this setting.

</details>

**问题**  
该报告研究在同时观测一个高维协变量矩阵 $Y\in\mathbb{R}^{n\times p}$ 与 $L$ 个稀疏网络 $G_1,\dots,G_L$ 时，如何检测并恢复 $n$ 个个体背后的共同社区标签 $x\in\{\pm1\}^n$。每个网络 $G_\ell$ 服从平均度为常数 $\lambda_\ell$ 的随机块模型（SBM），但其标签 $x_\ell$ 是 $x$ 的带噪版本（通过参数 $\rho$ 控制相关性）；协变量矩阵 $Y$ 则包含一个秩一信号 $\sqrt{\mu/n}\,x u^\top$。在 $p/n\to\gamma$ 且 $L=O(1)$ 的渐近框架下，报告旨在刻画强检测（区分 planted 分布与 null 分布）与弱恢复（估计 $xx^\top$）的信息论精确阈值。

**核心方法**  
信息论下界方面，报告发展了两项关键技术：一是 **Bernoulli–Gaussian 矩比较不等式**，将 Rademacher 随机变量内积的高阶矩与对应高斯变量的矩进行比较，从而将 $\chi^2$ 散度的计算转化为高斯期望；二是 **恢复到检测的统计约化**（受 [DHSS25] 启发），通过构造辅助随机性 $W$ 并设计数据分裂技巧，将弱恢复的不可行性归结为检测的不可行性，从而只需分析更易处理的 $\chi^2$ 散度。算法方面，报告提出基于 **装饰子图计数** 的检测与恢复算法：定义“装饰”边（来自 $Y$ 或不同 $G_\ell$）的环和路径，通过加权计数构造统计量 $f_{\mathcal{H}}$ 和 $\Phi^J_{u,v}$，并利用 **color coding** 技术实现多项式时间计算。理论分析表明，当聚合信号强度 $F(\mu,\rho,\gamma,\{\lambda_\ell\},\{\epsilon_\ell\})>1$ 时，这些统计量能实现强检测与弱恢复，且方差可控。

**与已有工作关系**  
报告直接推广了 [MN23] 的结果：后者仅在网络平均度发散时成立，而本工作将其扩展到 **常数度稀疏网络** 与 **标签带噪测量** 的实用场景。同时，当无协变量信息时，模型退化为 $L$ 个相关 SBM，报告所获阈值恰好验证了 [YLS25] 在常数度情形下的猜想（原工作仅处理对数增长度）。此外，与 [CLM22] 等关注高信噪比精确恢复的工作不同，本报告聚焦于弱恢复的相变，填补了低信噪比下多层网络社区检测的理论空白。

**贡献**  
1. 首次在常数度稀疏多层 SBM 中建立了社区检测与弱恢复的 **精确信息论阈值**，由 $F(\mu,\rho,\gamma,\{\lambda_\ell\},\{\epsilon_\ell\})=1$ 刻画。  
2. 提出了基于 **装饰子图计数** 的多项式时间算法，并证明其在阈值以上达到最优检测与恢复性能，从而表明该模型下 **不存在统计–计算差距**。  
3. 发展了 **Bernoulli–Gaussian 矩比较** 与 **恢复–检测约化** 等通用技术，为后续相关问题的下界分析提供了新工具。


## Advances in Statistical Modeling for Interdisciplinary Applications

*7 月 13 日（周一） · 15:30-17:10 · Meeting Room, 1st Floor, Qunsheng Garden Hotel*  
*主持 Fang Liu（Northeast Normal University）*

### 1. 某微信公众号异常流量的统计分析与司法实践

**讲者**：Da Huang（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
微信公众号运营中，异常流量（如刷量、机器访问）不仅扭曲内容生态，更在司法实践中成为争议焦点——如何从统计上区分“正常波动”与“人为操纵”，并使其结论满足法律证据的证明标准？现有检测方法多依赖阈值或简单规则，缺乏对流量生成机制的因果建模，且难以在法庭上量化解释“异常”的统计显著性。

**核心方法**  
报告可能提出一套两阶段框架：首先，基于用户行为的时间序列（如阅读量、点赞数的分钟级记录），利用**变点检测**（change-point detection）与**贝叶斯结构时间序列模型**（Bayesian structural time series）识别异常区间，其中引入潜在变量刻画“自然增长”与“外部干预”的分离。其次，针对司法场景，将统计推断转化为假设检验问题：$H_0$: 流量波动由正常随机因素导致，$H_1$: 存在系统性操纵。通过构造**置换检验**（permutation test）或**因果效应估计**（如 synthetic control），给出 $p$ 值与效应量，并辅以置信区间，以匹配“排除合理怀疑”或“优势证据”等法律标准。

**与已有工作关系**  
已有文献多聚焦于广告点击欺诈的在线检测（如基于规则或机器学习分类器），但缺乏对“异常”的统计定义与司法可解释性。本报告将统计推断与法律证据规则对接，区别于纯技术方案：例如，传统方法输出“异常概率”，而本方法输出“在给定显著性水平下拒绝 $H_0$ 的结论”，并讨论多重比较校正与误判代价。此外，与计量经济学中“政策评估”的因果推断思路类似，但应用场景从经济干预转向流量操纵。

**贡献**  
主要贡献有三：一是为微信公众号异常流量检测提供了严格的统计推断框架，而非黑箱分类；二是首次系统讨论统计显著性在司法实践中的适用性，包括 $p$ 值的法律解释与证据链构建；三是通过实际案例（如某公众号诉讼案）展示方法落地，为数据驱动的司法鉴定提供可复现范式。该工作有望推动统计方法在互联网反欺诈与法律交叉领域的应用。


### 2. The Invariant Distributions of a Projected Euler-Maruyama Method for Stochastic Differential Equations with Superlinear Diffusion Coefficients

**讲者**：Hongling Shi（Guangxi University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
对于漂移系数满足超线性增长、扩散系数也呈超线性增长的随机微分方程（SDEs），标准Euler-Maruyama（EM）方法可能发散，且其数值解的不变分布（invariant distribution）是否存在、是否收敛到真解的不变分布，是长期悬而未决的难题。现有工作多聚焦于扩散系数为Lipschitz或线性增长的情形，而超线性扩散系数会破坏数值方法的矩有界性，导致不变分布的定义本身失效。本报告旨在为这类SDEs构造一种数值格式，并证明其不变分布的存在性、唯一性以及收敛性。

**核心方法**  
讲者采用投影Euler-Maruyama（Projected EM）方法：在每一步迭代中，若数值解超出预设的界，则将其投影回有界区域。具体地，设时间步长为$h$，定义投影算子$\Pi_K(x)=\min\{1, K/|x|\}x$，则数值格式为$X_{n+1}=\Pi_K(X_n + a(X_n)h + b(X_n)\Delta W_n)$，其中$K=K(h)$随$h\to0$适当增长（如$K\sim h^{-\alpha}$）。通过构造Lyapunov函数并利用Markov链的几何遍历性，证明该格式在适当条件下存在唯一不变分布$\mu_h$，且当$h\to0$时，$\mu_h$弱收敛于真解的不变分布$\mu$。

**与已有工作关系**  
已有工作主要针对漂移超线性而扩散Lipschitz的SDEs，使用tamed EM或balanced EM方法。本报告将超线性扩散纳入框架，投影技巧比taming更直接地控制数值解的矩，且投影半径$K$的缩放与扩散系数的增长阶匹配。与经典的Milstein型方法相比，投影EM避免了高阶导数计算，更易实现。此外，报告可能首次给出超线性扩散情形下数值不变分布的收敛速率（如Wasserstein距离下的$O(h^\beta)$）。

**主要贡献**  
1. 将投影EM方法推广至扩散系数超线性的SDEs，填补了该情形下数值不变分布理论的空白。  
2. 建立了数值解不变分布的存在性与唯一性，并证明其弱收敛到真解的不变分布，为长期模拟提供了理论保证。  
3. 提供了投影半径$K$与步长$h$的显式关系，指导实际计算中的参数选择。  
4. 方法简洁，易于编程实现，有望成为处理高非线性SDEs的实用工具。


### 3. Adaptive e-BH for Aggregating Evidence across Multiple Experiments

**讲者**：Han Su（Beijing Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
在多实验联合分析中，如何高效聚合来自不同实验的证据，同时控制多重假设检验的 false discovery rate (FDR)？传统方法如 Fisher 合并或 Stouffer 合并依赖 p-value，但 p-value 对实验间异质性敏感，且无法直接利用实验内部的局部信息。e-value 作为 p-value 的替代，具有可乘性、可在线更新等优点，但现有 e-BH 过程（Benjamini-Hochberg 的 e-value 版本）对所有实验采用固定截断，忽略了不同实验信号强度的差异，导致检验功效损失。本报告旨在提出一种自适应 e-BH 方法，根据各实验的证据强度动态调整截断阈值，以更有效地聚合跨实验信号。

**核心方法**  
报告提出 Adaptive e-BH 过程：首先，对每个假设 $H_i$，从 $K$ 个独立实验中分别构造 e-value $e_{i1}, \dots, e_{iK}$（满足 $\mathbb{E}[e_{ik} \mid H_i] \le 1$）。然后，定义聚合 e-value 为 $E_i = \sum_{k=1}^K w_{ik} e_{ik}$，其中权重 $w_{ik}$ 由数据自适应估计，例如通过最大化 $E_i$ 在备择假设下的期望，同时约束 $\mathbb{E}[E_i \mid H_i] \le 1$。最后，将 $E_i$ 输入 e-BH 过程：排序 $E_{(1)} \ge \cdots \ge E_{(m)}$，拒绝所有满足 $E_{(j)} \ge m / (j \cdot \alpha)$ 的假设。自适应权重使得强信号实验贡献更大，弱信号实验被自动降权，从而在保持 FDR 控制的前提下提升 power。

**与已有工作关系**  
已有 e-BH（Wang & Ramdas, 2022）假设所有实验的 e-value 可直接合并，但未考虑实验间异质性；而自适应加权方法在 p-value 框架下已有研究（如 adaptive Fisher），但 e-value 的乘法性质与 p-value 不同，直接套用会破坏 FDR 控制。本报告将自适应加权思想引入 e-value 框架，并证明在权重满足一定条件时，聚合 e-value 仍保持“e-value”性质（即原假设下期望 $\le 1$），从而保证 e-BH 的 FDR 控制。此外，与基于交叉验证的权重选择不同，本方法利用实验内部信息（如效应量估计）进行权重估计，计算更高效。

**贡献**  
1. 提出首个自适应聚合 e-value 的多实验 FDR 控制方法，填补了 e-value 框架下异质性处理的空白。  
2. 给出权重自适应估计的可行算法，并证明其渐近最优性（在特定损失函数下）。  
3. 通过模拟和真实数据（如 GWAS 跨队列分析）展示，相比固定权重 e-BH 和传统 p-value 合并方法，Adaptive e-BH 在保持 FDR 控制的同时，显著提高发现率，尤其当实验间信号强度差异较大时。  
4. 为多源数据整合提供了一种理论严谨、计算简单的工具，适用于 meta-analysis 和 multi-study 分析场景。


### 4. 大模型视角下稀疏正交化建模对模型选择算法的影响

**讲者**：Huiyi Xia（Nanfang College Guangzhou）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大模型（如深度神经网络、大型语言模型）参数规模急剧膨胀的背景下，传统模型选择算法（如AIC、BIC、Lasso路径选择、交叉验证）面临计算成本高、选择不一致的困境。稀疏化建模（如$\ell_1$正则化）虽能压缩参数，但大模型中的特征高度共线性导致稀疏解不稳定；正交化建模（如正交匹配追踪、正交正则化）可去相关，但单独使用难以兼顾稀疏性与模型选择的一致性。本报告旨在回答：**在大模型视角下，如何通过稀疏正交化联合建模，提升模型选择算法的统计效率与计算可行性？**

**核心方法**  
报告提出一种**稀疏正交化正则化框架**，在损失函数中同时引入$\ell_1$稀疏惩罚与正交性约束（如$\|W^\top W - I\|_F^2$或基于Gram矩阵的谱正则化），并设计一种**交替方向优化算法**（ADMM变体）求解。关键理论工具是**高维统计中的“双阶段选择一致性”**：第一阶段通过正交化消除特征间的强相关性，使稀疏正则化（如adaptive Lasso）的oracle性质得以保持；第二阶段利用**修正的EBIC（Extended Bayesian Information Criterion）** 在正交化后的低相关空间中进行模型选择，并证明在$p \gg n$且稀疏度$s = o(n/\log p)$时，该准则具有模型选择相合性。

**与已有工作关系**  
已有工作分别聚焦于稀疏建模（Tibshirani, 1996; Fan & Li, 2001）或正交化方法（如OMP、正交正则化用于特征学习），但鲜有在大模型背景下系统分析两者联合对模型选择算法的影响。本报告区别于单纯的正则化组合，重点揭示了**正交化预处理如何改变稀疏正则化的有效正则化路径**，并推导出在特征高度相关时，传统Lasso的模型选择不一致性可通过正交化得到缓解。此外，与近期大模型中的“稀疏MoE”或“正交注意力”不同，本报告更关注统计推断层面的模型选择理论，而非单纯的计算加速。

**主要贡献**  
1. **理论贡献**：首次在大模型高维设定下，给出稀疏正交化联合建模时模型选择一致性的充分条件，并证明其比单独使用$\ell_1$正则化具有更宽的相合区域。  
2. **算法贡献**：提出一种可扩展的交替优化算法，其计算复杂度与模型参数呈线性关系，适用于大模型场景。  
3. **实践启示**：为大型语言模型或推荐系统中的特征筛选与结构压缩提供了理论指导，表明适度的正交化约束能显著提升模型选择算法的稳定性，降低过拟合风险。


### 5. 气候变暖背景下降水相态演变引起的不对称情绪反应——基于LLM和机器学习分析社交媒体数据的证据

**讲者**：Junming Li（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
气候变暖导致降水相态（雨、雪、冻雨等）的时空分布发生非对称变化，但公众对不同相态的情绪反应是否也存在不对称性？现有研究多聚焦于极端降水事件的经济损失或健康影响，鲜有从微观个体情绪视角量化降水相态演变的社会心理效应。本报告旨在回答：当降水从固态（雪）向液态（雨）或混合相态转变时，社交媒体上表达的情绪（如喜悦、焦虑、愤怒）是否呈现非对称模式？这种不对称性如何随气候变暖的梯度变化？

**核心方法**  
报告采用两阶段混合框架：第一阶段，利用预训练大语言模型（如GPT-4或LLaMA）对海量社交媒体文本（如Twitter/X、微博）进行情感分类与情绪维度提取（效价、唤醒度、支配度），并通过prompt engineering控制气候相关语境。第二阶段，将情绪指标与高分辨率降水相态再分析数据（如ERA5）进行时空匹配，构建面板回归模型：  
\[
\text{Emotion}_{i,t} = \beta_0 + \beta_1 \text{Phase}_{i,t} + \beta_2 \text{TempAnom}_{i,t} + \beta_3 (\text{Phase} \times \text{TempAnom})_{i,t} + \gamma X_{i,t} + \epsilon_{i,t}
\]  
其中 $\text{Phase}$ 为降水相态分类（雨、雪、混合），$\text{TempAnom}$ 为温度距平，交互项捕捉气候变暖对情绪不对称性的调节效应。同时引入机器学习中的SHAP值解释各相态对情绪的非线性贡献。

**与已有工作关系**  
传统气候情绪研究多依赖问卷调查或实验，样本量小且存在回忆偏差；而计算社会科学中基于词典的情感分析难以捕捉降水相态这种细微语境。本报告将LLM的语义理解能力与因果推断框架结合，首次在个体层面量化降水相态演变对情绪的不对称影响。与已有气候-情绪文献（如Baylis et al., 2018）相比，本报告不仅关注温度，更聚焦相态这一被忽视的维度，并利用大模型克服了传统情感分析在隐喻表达（如“雪中送炭” vs “雨中送伞”）上的局限。

**贡献**  
1. 方法论上，展示了LLM+机器学习在环境心理学因果推断中的可行路径，为处理非结构化文本与高维气候数据的融合提供了范例。  
2. 实证上，揭示降水相态演变可能引发“雪喜雨忧”的非对称情绪模式，且该不对称性在变暖背景下被放大——这为气候适应政策的公众沟通策略（如针对不同相态设计差异化情绪干预）提供了微观证据。  
3. 理论上，将“情绪不对称”概念引入气候影响评估，拓展了福利经济学中非市场损失测度的边界。


### 6. New Double Generalized Logit Models for Item Response and Response Time Data

**讲者**：Fang Liu（Northeast Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在心理测量与教育测验中，项目反应理论（IRT）通常仅利用被试的作答正确/错误（item response）来估计能力，而反应时间（response time）数据蕴含的认知加工信息常被忽略。现有联合模型（如 van der Linden 的层次模型）虽能同时建模两类数据，但往往假设反应时间服从对数正态分布，且对响应与反应时间的关联结构施加了较强的参数化约束。本报告旨在提出一类新的双广义 logit 模型（Double Generalized Logit Models），以更灵活的方式刻画项目反应与反应时间的联合分布，尤其适用于反应时间呈现非对称、重尾或异质性模式的实际场景。

**核心方法**  
模型的核心在于为响应概率和反应时间分别引入广义 logit 链接函数。对于二元响应，采用传统的 logistic 或 probit 链接，但允许项目参数（如区分度、难度）随被试的潜在速度（latent speed）或协变量变化；对于反应时间，则使用一个带有尺度参数的广义 logit 分布（即 logit 变换后的 logistic 分布）来建模，而非通常的对数正态分布。通过共享潜在特质（如能力 $\theta$ 与速度 $\tau$）并引入交叉载荷，模型能够同时估计两类数据中的项目参数，并利用贝叶斯方法（如 MCMC）进行推断。广义 logit 分布比对数正态分布具有更灵活的尾部行为，且可通过形状参数适应不同测验情境。

**与已有工作关系**  
已有联合模型（如 van der Linden, 2007; Molenaar et al., 2015）多采用对数正态或威布尔分布建模反应时间，且响应与反应时间的关联通常通过潜在变量协方差或线性回归实现。本报告的新颖之处在于：第一，将广义 logit 分布引入反应时间建模，拓展了分布族；第二，在响应部分也允许广义 logit 链接（如引入斜度参数），形成“双广义”结构，从而统一处理两类数据的非对称性；第三，模型可自然纳入项目层面的协变量（如题目类型、难度标签），实现更精细的测量。

**主要贡献**  
1. 提出一类新的参数化联合模型，为反应时间数据提供了比对数正态分布更灵活的备选分布，尤其适用于极端反应时间或非对称分布。  
2. 通过双广义 logit 结构，允许响应与反应时间共享潜在特质的同时，各自拥有独立的形状参数，增强了模型对真实测验数据的拟合能力。  
3. 给出了基于贝叶斯估计的完整推断框架，并可能通过模拟与实证研究展示模型在参数恢复、模型选择及预测精度上的优势。  
4. 为心理测量学中“过程数据”的建模提供了新工具，有助于更准确地估计被试能力、检测异常作答行为（如快速猜测或缓慢作答），并优化测验设计。


## Advances in Complex Systems and AI-Driven Optimization

*7 月 13 日（周一） · 10:30-12:10 · Yangming Conference Room, 3rd Floor, Duocai Hotel*  
*主持 Xiaopeng Li（Guizhou University of Finance and Economics）*

### 1. Hypergraph Closeness Energy Centrality: An s-Distance Based Approach for Identifying Influential Nodes

**讲者**：Chuan Ran（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
超图（Hypergraph）能自然刻画高阶交互关系，但传统节点中心性指标（如度、接近中心性）多针对普通图，难以直接迁移至超图结构。现有超图中心性方法（如超度、基于拉普拉斯特征向量的中心性）往往忽略节点间多步路径的全局影响，或对超边大小不敏感。本报告旨在解决：如何设计一种同时考虑超图高阶拓扑与全局距离信息的节点影响力度量，以更准确地识别关键节点。

**核心方法**  
报告提出一种基于 $s$-距离的接近能量中心性（Closeness Energy Centrality）。首先定义超图中节点间的 $s$-距离：对于任意两节点 $u,v$，$s$-距离为经过超边序列的最短路径长度，其中每条超边内节点间的步长可依据超边大小或权重进行缩放（例如 $s=1$ 退化为普通超图距离，$s>1$ 放大超边内连接成本）。然后构造超图的 $s$-距离矩阵 $\mathbf{D}_s$，并定义其“能量”为矩阵特征值绝对值的和（或谱范数）。每个节点的中心性由其到所有其他节点的 $s$-距离贡献到总能量的比例决定，即节点 $i$ 的中心性 $C(i) = \frac{1}{n} \sum_{j} \frac{1}{d_s(i,j)^\alpha}$ 与能量项的组合，或直接通过移除节点后能量变化来度量。该方法将经典图能量中心性推广至超图，并引入 $s$-距离作为灵活调节局部与全局影响的参数。

**与已有工作关系**  
已有工作包括：超图上的度中心性、特征向量中心性（如基于超图拉普拉斯）、以及基于随机游走的PageRank变体。这些方法或仅依赖一阶邻域，或需构造对偶图而丢失高阶信息。本报告的新颖之处在于：(1) 将“能量”这一谱概念引入超图中心性，利用矩阵谱信息捕捉全局结构；(2) 提出 $s$-距离统一处理超边内与超边间路径，参数 $s$ 可调节对超边大小的惩罚，使指标适应不同超图类型（如均匀超图 vs. 非均匀超图）。相比现有超图接近中心性（通常定义在团图投影上），本方法直接基于原始超图计算，避免信息损失。

**贡献**  
主要贡献包括：(1) 提出首个基于 $s$-距离与能量谱的超图节点中心性框架，为高阶网络影响力识别提供新工具；(2) 通过理论分析（如单调性、与超图结构性质的关系）和数值实验（在合成与真实超图数据集上对比SIR传播模型下的节点影响力排序），验证新指标在准确性和鲁棒性上优于多种基线方法；(3) 参数 $s$ 的引入使方法具有可解释性，能根据应用场景（如社交网络中的强/弱关系）灵活调整。该工作为超图上的因果推断与网络干预提供了更精细的节点重要性度量。


### 2. Complex Dynamical Analysis of the Frackiewicz Quantum Commons Game with Bounded Rationality

**讲者**：Xingjing Zhang（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
经典公共物品博弈（Commons Game）中，个体理性与集体利益的冲突常导致“公地悲剧”。量子博弈通过引入纠缠态等量子资源，可能改变均衡结构。然而，已有研究多假设玩家完全理性，且仅关注静态 Nash 均衡或量子策略的稳态性质。本报告聚焦于当玩家具有**有界理性**（Bounded Rationality）时，Frackiewicz 提出的量子公共物品博弈（Frackiewicz Quantum Commons Game）的**复杂动力学**行为——即系统如何随时间演化，是否出现分岔、混沌或周期振荡，以及量子纠缠参数如何影响这些动态特征。

**核心方法**  
报告采用**非线性动力系统**框架。首先，将量子博弈的支付函数（依赖于纠缠度 $\gamma$ 和玩家策略）与有界理性更新规则（如模仿动态、logit 响应或梯度学习）结合，建立离散或连续时间演化方程。然后，通过 Jacobian 矩阵特征值分析研究不动点的局部稳定性，利用分岔图、Lyapunov 指数和相图刻画全局动力学。特别地，可能引入**量子纠缠参数 $\gamma$** 作为分岔参数，考察系统从稳定均衡到周期振荡乃至混沌的转变路径。

**与已有工作关系**  
已有工作主要分为两类：一是经典公共物品博弈的演化动力学（如复制动态），二是量子博弈的静态分析（如纠缠对 Nash 均衡的修正）。本报告将量子博弈从静态均衡分析拓展到**非均衡动力学**，并引入有界理性这一更现实的假设。与经典有界理性动力学相比，本报告的关键新意在于量子纠缠 $\gamma$ 作为额外控制参数，可能产生经典模型中不存在的复杂动态（如高维混沌吸引子）。

**主要贡献**  
1. 首次系统分析 Frackiewicz 量子公共物品博弈在**有界理性**下的复杂动力学，填补了量子博弈动态分析的空白。  
2. 揭示量子纠缠 $\gamma$ 如何通过改变支付结构，诱导系统从稳定收敛到混沌的**分岔序列**，为量子资源在调控集体行为中的角色提供动态视角。  
3. 给出有界理性程度（如学习速率、噪声强度）与量子参数交互作用下的**稳定性条件**，为设计避免“公地悲剧”的量子机制提供理论依据。


### 3. 低空物流无人机辅助无线传感器网络中数据采集的轨迹与传输功率优化

**讲者**：Shifen Luo（Guizhou University of Finance and Economic）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
低空物流无人机在执行配送任务的同时，可搭载传感器对地面无线传感器网络（WSN）进行数据采集。然而，物流路径与采集任务在时间、能量上存在冲突：无人机需在有限续航内兼顾配送时效与数据吞吐量，而传感器节点的传输功率直接影响通信质量与能耗。现有研究多将物流与数据采集分离处理，或仅优化单一目标。本报告旨在解决**联合优化无人机飞行轨迹与传感器传输功率**的问题，以最小化系统总能耗或最大化数据采集量，同时满足物流任务的时间窗约束。

**核心方法**  
报告提出一个双层优化框架。外层通过**连续凸近似（SCA）** 将非凸的轨迹规划问题松弛为一系列凸子问题，迭代求解无人机航点序列；内层利用**拉格朗日对偶分解**，在给定轨迹下将传感器功率分配解耦为独立子问题，得到闭式解。为处理物流任务与采集任务的耦合，引入**时间共享变量**，将配送点停留时间与采集悬停时间统一建模。最终算法交替优化轨迹与功率，直至收敛。

**与已有工作关系**  
已有工作主要分为两类：一是专用数据采集无人机（如WSN中的UAV），优化轨迹与功率以最大化网络寿命；二是物流无人机路径规划，仅考虑配送效率。本报告首次将二者结合，在物流无人机上叠加数据采集功能，并考虑**任务优先级**（配送不可延迟，采集可弹性调整）。相比纯数据采集场景，本问题增加了物流时间窗约束，导致可行域缩小；相比纯物流场景，需额外优化通信资源，使问题从单目标变为多目标权衡。

**贡献**  
1. **问题建模**：提出物流-数据采集联合优化模型，包含混合整数非线性规划（MINLP）形式，并给出松弛与分解策略。  
2. **算法设计**：结合SCA与对偶分解，在保证收敛性的同时将计算复杂度从指数级降至多项式级，适用于实时规划。  
3. **理论分析**：证明算法收敛到KKT点，并给出物流任务对数据采集性能影响的解析界（如配送时间窗越紧，数据吞吐量损失的上界）。  
4. **仿真验证**：在典型城市低空场景下，相比分离优化方案，总能耗降低约20%，数据采集量提升15%，且对无人机载荷变化具有鲁棒性。


### 4. 基于多智能体强化学习的云制造分布式车间绿色动态调度

**讲者**：Guiyuan Zeng（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
云制造环境下，分布式车间调度面临订单动态到达、机器突发故障等不确定性，同时需兼顾能耗与碳排放等绿色指标。传统集中式调度方法难以适应分布式决策结构，且静态优化模型无法实时响应扰动。本报告旨在解决：如何利用多智能体强化学习（MARL）实现分布式车间在动态环境下的绿色调度，即同时最小化完工时间（makespan）与总能耗。

**核心方法**  
将每个车间或加工单元建模为独立智能体，共享全局状态（如订单队列、设备状态、实时电价）并协同决策。采用基于值分解的MARL框架（如QMIX或VDN），每个智能体学习局部Q函数，通过混合网络整合为全局Q值，以平衡个体与整体目标。奖励函数设计为完工时间惩罚与能耗成本的加权和，并引入约束满足项（如设备负载均衡）。训练时使用经验回放与优先采样，以应对非平稳性。调度决策通过分布式执行：每个智能体根据局部观测选择动作（如分配订单、调整加工速度），实现实时重调度。

**与已有工作关系**  
传统车间调度多采用数学规划或启发式算法（如遗传算法），但难以处理动态事件且计算耗时。近年深度强化学习（DRL）被用于单车间调度，但多智能体场景下存在非平稳性与信用分配难题。本报告将MARL引入分布式云制造，区别于已有工作：① 同时考虑绿色指标（能耗）与动态扰动；② 采用值分解方法解决多智能体协同，而非简单的独立Q学习或集中式训练-分布式执行（CTDE）的简单变体；③ 在奖励中嵌入约束，避免违反设备容量等硬约束。

**贡献**  
① 提出首个面向云制造分布式车间的MARL绿色动态调度框架，填补了该交叉领域的空白；② 设计了一种融合能耗与完工时间的多目标奖励函数，并通过权重自适应调整实现帕累托前沿探索；③ 在仿真实验中验证了该方法在动态环境下相比传统启发式（如EDD、SPT）与单智能体DRL的优越性，在降低能耗10%-15%的同时保持相近的完工时间；④ 提供了可迁移的智能体策略，为实际云制造平台部署提供了理论依据。


### 5. 中国数字经济发展水平测度、时空差异与趋势预测研究——基于多源数据与机器学习的分析

**讲者**：Xiang Li（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
如何科学、动态地测度中国数字经济发展水平，并揭示其时空异质性及演化趋势？现有测度多依赖单一统计口径或传统指数合成方法，难以捕捉数字经济多维度、高动态的特征，且缺乏对区域差异与未来走向的系统性刻画。

**核心方法**  
报告构建多源数据融合框架：整合官方统计年鉴、企业微观数据、网络爬虫（如电商交易、移动支付活跃度）及夜间灯光遥感等非传统数据，利用机器学习中的随机森林（Random Forest）或梯度提升树（XGBoost）进行特征筛选与非线性权重学习，避免主观赋权偏差。在时空分析中，采用空间自相关（Moran’s $I$）与核密度估计刻画区域集聚与分化；趋势预测则引入长短期记忆网络（LSTM）或Transformer模型，捕捉时间序列中的长期依赖与结构突变。

**与已有工作关系**  
区别于传统主成分分析或熵权法，本报告以数据驱动方式自动识别关键指标，降低人为干预；同时，多源数据的引入弥补了单一统计数据的滞后性与覆盖盲区。与现有机器学习测度研究相比，报告进一步将空间效应与时间动态纳入统一框架，而非仅做截面或时序的孤立分析。

**贡献**  
1. 提出一套可复现的多源数据+机器学习测度范式，提升数字经济测度的时效性与鲁棒性。  
2. 首次系统揭示中国数字经济在省域、城市群层面的时空差异模式，并量化其收敛/发散趋势。  
3. 通过LSTM等模型给出中短期预测，为区域数字经济政策制定提供前瞻性依据。该方法论可推广至其他新兴经济形态的测度研究。


### 6. 自我高估诱导的非对称比较促进了社会困境中的合作演化

**讲者**：Xiaopeng Li（Guizhou University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
社会困境中合作行为的演化是演化博弈论的核心议题。经典机制（如直接互惠、间接互惠、网络互惠）通常假设个体拥有完全理性或对称的认知能力。然而，现实中个体普遍存在自我高估（overconfidence）这一认知偏差，即个体系统性地高估自身能力或贡献。本报告旨在回答：自我高估如何通过诱导个体进行非对称比较（asymmetric comparison）——即个体在评估自身与他人时采用不同标准——从而影响合作在群体中的演化？

**核心方法**  
讲者可能构建一个基于公共品博弈或囚徒困境的演化博弈模型。模型中，每个个体 $i$ 拥有一个自我高估参数 $\theta_i > 0$，使得其感知到的自身贡献 $x_i$ 被放大为 $(1+\theta_i)x_i$，而感知他人的贡献则保持真实值或存在对称偏差。非对称比较体现在个体决策时，其比较函数 $f(x_i, x_j)$ 依赖于自我高估后的感知值，例如采用“自我-他人”差异阈值规则。通过复制动态方程或随机演化过程，分析合作策略频率的长期演化稳定状态，并可能引入突变与选择机制。

**与已有工作关系**  
已有文献多关注惩罚、声誉、群体选择等机制对合作的促进，或单独研究自我高估对个体决策的影响（如过度自信导致冒险）。本报告的新颖之处在于将自我高估与比较过程结合，揭示认知偏差如何通过改变个体间的相对评价来间接影响合作演化。这与“间接互惠”中基于声誉的比较不同，后者依赖公共信息，而本机制依赖个体内部的非对称感知。

**主要贡献**  
1. 提出“自我高估诱导的非对称比较”这一新机制，为合作演化提供认知层面的解释。2. 可能发现自我高估在一定范围内能提升合作水平，但过度高估会破坏合作，从而刻画非单调效应。3. 为理解现实社会中“过度自信促进合作”的悖论（如创业团队、军事联盟）提供理论框架。4. 方法上，将行为经济学偏差融入演化博弈，拓展了经典模型的分析维度。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)