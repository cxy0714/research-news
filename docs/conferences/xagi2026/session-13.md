# Session 13 · AI的数理和计算基础

> XAGI 2026 交叉智能大会 · 10 月 18 日（周日）下午 14:00-16:00 · 4会（友谊宫二层4号会议室） · [返回会议总览](index.md)

- 3 场报告 · 已精读 2 场

**主持**：周峰（中国人民大学）

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场三场报告表面上分属随机矩阵理论、几何深度学习与大模型系统优化，但共同指向一个核心问题：如何在结构约束下逼近最优计算效率。马俊杰从统计物理视角处理带旋转不变噪声的尖峰矩阵模型，提出同时作用于观测矩阵特征值与AMP迭代轨迹的双重去噪器，并给出状态演化方程与最优性刻画；许洪腾将SE(3)-Transformer的注意力机制重新解释为哈密顿流上的参数化动力学，通过引入可学习的辛结构约束来改进等变表示的传播方式；周峰则直接面向工程瓶颈，分别从注意力核的谱频率学习与多草稿序列验证两个层面压缩长序列建模和自回归解码的冗余计算。

最突出的主线是“结构先验的算法化利用”。马俊杰的工作属于理论端：他证明在旋转不变噪声下，传统AMP的标量去噪不再最优，必须引入矩阵级特征值处理，这为高维统计估计提供了新的可达界；许洪腾则把物理守恒量（哈密顿量）作为归纳偏置注入Transformer，使等变性从群作用层面延伸到动力学层面，与马俊杰的谱方法形成对照——前者利用噪声的旋转对称性，后者利用目标函数的辛对称性。周峰的工作虽无显式对称性，但Flexformer通过随机傅里叶特征的谱频率学习，本质上是在逼近注意力核的低秩结构，与马俊杰的特征值去噪共享“谱域操作”的思路；MDSeq则从解码端优化接受概率，属于对自回归顺序结构的概率性利用。三者在“结构—算法”映射上构成递进：马俊杰给出理论最优基准，许洪腾提供几何约束下的新架构，周峰落地为可部署的系统方案。

若想快速建立本场脉络，建议先看马俊杰的报告，它提供了分析这类问题的标准框架（状态演化与最优性条件），是理解后两场的理论底色；随后看周峰，因其两个工作分别对应注意力与解码两个最实际的效率瓶颈，且与马俊杰的谱方法有直接呼应；许洪腾的报告适合对几何深度学习或分子建模感兴趣的读者，其哈密顿流视角可作为独立入口，但与前两场的关联较弱。按主题分组：理论方法入口（马俊杰）、系统效率入口（周峰）、几何架构入口（许洪腾）。

---

### 1. Spiked Matrix Models with Rotationally Invariant Noise: AMP Algorithms and Optimality

**讲者**：马俊杰（中国科学院数学与系统科学研究院 · 计算数学与科学工程计算研究所） · 14:00-14:40

**对应论文**：Optimality of Approximate Message Passing Algorithms for Spiked Matrix Models with Rotationally Invariant Noise · [arXiv:2405.18081](https://arxiv.org/abs/2405.18081) · 📖 [长篇精读](../../deep_reads/xagi2026-2405.18081.md)

<details><summary>摘要（会议官网）</summary>

<p>In this talk, I will present our recent work on the optimality of Approximate Message Passing (AMP) algorithms for spiked matrix models with rotationally invariant noise. We introduce a new AMP algorithm that employs a matrix denoiser - acting on the eigenvalues of the observed matrix - and an iterate denoiser - applied to the AMP iterates. The resulting dynamics admit a simple state-evolution characterization, which allows us to identify the optimal pair of denoisers achieving the minimum possible asymptotic estimation error among a broad class of iterative algorithms.</p>

</details>

*（对应论文为自动检索推断，可能有偏差）*

**问题**：报告讨论从观测矩阵估计秩一信号矩阵的问题，模型为 $Y=\frac{\theta}{N}x_*x_*^\top+W$，其中噪声 $W$ 是旋转不变噪声：特征向量服从 Haar 分布，特征值可任意给定。相比经典 Wigner 噪声，这类噪声能刻画特征值非平凡、分量强相关的实际扰动，但现有 AMP 类算法的动态与最优性在此模型下远未清楚。报告的核心动机正是为这类更一般的噪声模型建立可分析的 AMP 算法，并回答其能否达到最小渐近估计误差。

**核心方法**：作者提出一类正交近似消息传递（OAMP）算法，每步同时使用两个去噪器：矩阵去噪器 $\Psi_t$ 作用于观测矩阵的特征值，迭代去噪器 $f_t$ 作用于前次迭代。在高维极限下，算法动态由简单的状态演化递归刻画；通过优化状态演化，可以选出最优的矩阵去噪器与迭代去噪器，使渐近估计误差最小。论文给出状态演化定理和最优性定理，并指出最优矩阵去噪器与特征值收缩估计有密切联系。

**与已有工作的关系**：该工作将 AMP 从 i.i.d. 高斯噪声推广到旋转不变噪声，直接回应 Barbier 等人在 trace ensemble 假设下的工作，但不再要求噪声来自特定势函数 $V$，只要求谱测度满足绝对连续、密度 Hölder 连续等温和条件。最优性证明借鉴了 Celentano 等人以及 Montanari-Wu 在 Wigner 模型下证明 AMP 最优性的技术路线；算法结构上可视为 OAMP/vector AMP 在矩阵估计问题中的自然类比。

**贡献与边界**：主要贡献是给出旋转不变噪声下 AMP 的状态演化、最优去噪器构造，以及在固定迭代次数下的一类算法最优性。边界在于：结果在高维极限下成立，依赖谱测度的正则性假设；最优性限于“固定迭代预算”内的某类迭代算法，不覆盖所有多项式时间算法；信息论极限部分以猜想形式给出，材料未给出数值实验的具体规模与误差数值。

<details><summary>讲者简介</summary>

<p>马俊杰，中国科学院数学与系统科学研究院长聘副研究员，2015年在香港城市大学取得博士学位。曾于哥伦比亚大学、哈佛大学从事博士后研究。研究兴趣为复杂信号处理的数学理论与算法，在AOS、IEEE TIT、NeurIPS、ICML等国际期刊和会议发表多篇学术论文。曾入选中科院百人计划，主持3项国家自然基金委项目（青年项目、面上项目、青年科学基金B类项目），并参与中科院先导科技专项、科技部重点专项等科研项目。担任中国运筹学会青年工作委员会副秘书长（2022-2024）、中国现场统计研究会随机矩阵理论与应用分会理事。</p>

</details>


### 2. An Improved SE(3)-Transformer Driven by Hamiltonian Flow

**讲者**：许洪腾（中国人民大学 · 高瓴人工智能学院） · 14:40-15:20

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>The Transformer architecture plays a central role in modern deep learning, and its SE(3)-equivariant variants have been widely applied to molecular conformation modeling and optimization. In this study, we propose an improved SE(3)-Transformer architecture, called HamFormer, which revisits the design of SE(3)-Transformer through the lens of Hamiltonian flow. In particular, we define a parametrized Hamiltonian flow in the phase space of position and velocity, corresponding to optimizing an energy functional that combines an optimal transport-based potential with a damped momentum. The Lie-Trotter splitting framework of the Hamiltonian flow leads to the proposed HamFormer architecture, whose feedforward computation achieves the optimization step of the proposed energy functional. Furthermore, we combine HamFormer with Equivariant Graph Neural Network (EGNN), build a new model for molecular conformation optimization.</p>

</details>

*（未检索到公开论文，以下依据报告摘要与讲者方向推断）*

**问题**：SE(3)-Transformer 是分子构象建模与优化中的常用等变架构，但其层设计多从注意力机制出发，缺乏对物理动力学过程的显式刻画。报告提出从 Hamiltonian 流视角重新审视 SE(3)-Transformer，试图回答：能否将网络的前向计算解释为对某个能量泛函的优化步骤，从而让等变架构同时具备物理可解释性与能量下降保证。该问题在分子构象优化中尤为关键，因为构象变化天然服从动力学规律，而最优传输理论又为衡量分布间迁移提供了自然框架。

**核心方法**：提出 HamFormer 架构。具体地，在位置与速度构成的相空间 $(x,v)$ 中定义参数化 Hamiltonian 流，其对应的能量泛函由基于最优传输的势能项与阻尼动量项组成。利用 Lie-Trotter 分裂将连续流离散化，得到交替更新的网络层，使前向计算等价于对该能量泛函的优化步骤。进一步将 HamFormer 与 Equivariant Graph Neural Network（EGNN）结合，构建分子构象优化模型。官网摘要未给出网络层数、参数规模、实验数据集及数值结果。

**与已有工作的关系**：该工作直接以 SE(3)-Transformer 为改进对象，用 Hamiltonian 流重新设计其前向传播，属于“数值算法驱动架构设计”路线；与 EGNN 的结合表明它不是替代等变图网络，而是作为可解释的动力学模块嵌入其中。讲者此前有最优传输驱动的图神经网络工作，可推测该研究延续了将最优传输与等变架构结合的方向，但官网摘要未点名具体基线或同期对比方法。

**贡献与边界**：主要贡献是为 SE(3)-Transformer 提供一种基于 Hamiltonian 流的可解释重构，将网络层与能量优化步骤对应，并给出与 EGNN 融合的分子构象优化方案。边界在于：能量泛函的具体形式与可优化性依赖 Hamiltonian 流和 Lie-Trotter 分裂的离散化假设；官网摘要未提供实验验证，因此无法判断实际性能；未检索到公开论文，架构细节、理论保证和适用任务范围均需进一步核实。

<details><summary>讲者简介</summary>

<p>许洪腾，中国人民大学高瓴人工智能学院长聘副教授，博导，国家高层次青年人才。其研究方向为通用人工智能技术及其应用，特别是（1）最优传输驱动的机器学习理论与方法；（2）生成式大模型架构设计、模型压缩、模型融合；（3）AI4Math以及AI4Science等前沿应用。近年来的代表性工作包括基于最优传输距离的图神经网络设计与学习方法、数值算法驱动的大模型架构设计与高效适配、基于生成式人工智能的柔性大分子建模技术等。研究工作曾获得ICML2025 AI for Math研讨会杰出论文提名奖，入选《Environmental Science &amp; Technology》副封面文章等荣誉。主持国家自然科学基金重大研究计划培育项目、中央引导地方人工智能专项等项目。</p>

</details>


### 3. 高效大模型

**讲者**：周峰（中国人民大学 · 统计学院） · 15:20-16:00

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>面向大模型在长序列建模与自回归生成中的效率瓶颈，相关研究从注意力计算和推理解码两个层面展开。在注意力计算方面，Flexformer通过学习随机傅里叶特征的谱频率，实现灵活且高效的注意力核建模，提升了线性注意力的表达能力。在推理解码方面，MDSeq采用多草稿序列级验证机制，通过优化接受概率与残差分布，提高推测解码的期望接受长度。理论分析与实验结果表明，该系列工作能够在保持模型性能与采样正确性的同时，有效提升长序列建模和大模型推理效率，为高效大模型的研究与应用提供了新的技术路径。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>周峰，中国人民大学统计学院副教授，主要研究领域包括统计机器学习、贝叶斯方法、随机过程、大模型推理加速等，主持国家自然科学基金青年项目、面上项目，在JMLR、STCO、ICML、NeurIPS、ICLR、AAAI、KDD等国际期刊和会议上发表论文40余篇，担任NeurIPS、ICLR、IJCAI、AISTATS等国际会议领域主席，国际期刊《Statistics and Computing》副主编，《Transactions on Machine Learning Research》执行编辑，《Journal of Machine Learning Research》编委。</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
