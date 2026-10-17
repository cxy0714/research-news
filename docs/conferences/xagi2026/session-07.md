# Session 07 · 扩散模型的理论基础以及推理测算法

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 8会（友谊宫二层8号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 0 场

**主持**：陆一平（北京大学）、周默（北京大学）

---

### 1. Weighted Laplacian Flow: A Deterministic Particle Flow with Provable Convergence

**讲者**：史作强（清华大学 · 数学中心） · 14:00-14:30

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

Sampling from a target probability density is a fundamental task in statistics, machine learning, and scientific computing. We introduce weighted Laplacian flow, a deterministic particle-flow method that transports samples from a tractable initial density to a target density known up to normalization. The method evolves the logarithmic density ratio between the target and the transported distribution and constructs the particle velocity by solving a weighted Poisson equation associated with the target density. We establish the global well-posedness of the proposed PDE system and prove that the transported density converges to the target density. Under a sublinear forcing condition, the method achieves exact convergence in finite time. Numerical experiments on multimodal, heavy-tailed, and ten-dimensional targets demonstrate that weighted Laplacian flow can perform long-range mass transport, overcome energy barriers.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

史作强，清华大学丘成桐数学科学中心长聘教授，北京雁栖湖应用数学研究院双聘研究员，主要研究方向为偏微分方程数值方法，微分方程与机器学习，非线性非平稳信号时频分析等，在国际知名学术期刊和学术会议发表文章100余篇。

</details>


### 2. Simulation-Free Dynamic Unbalanced Optimal Transport and One-step Inference

**讲者**：周沛劼（北京大学 · 前沿交叉学科研究院） · 14:30-15:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

The Wasserstein-Fisher-Rao (WFR) metric extends dynamic optimal transport (OT) by coupling displacement with change of mass, providing a principled geometry for modeling unbalanced snapshot dynamics. Existing WFR solvers, however, are often unstable, computationally expensive, and difficult to scale. Here we introduce WFR Flow Matching (WFR-FM), a simulation-free training algorithm that unifies flow matching with dynamic unbalanced OT. Unlike classical flow matching which regresses only a transport vector field, WFR-FM simultaneously regresses a vector field for displacement and a scalar growth rate function for birth-death dynamics, yielding continuous flows under the WFR geometry. Theoretically, we show that minimizing the WFR-FM loss exactly recovers WFR geodesics. Empirically, WFR-FM yields more accurate and robust trajectory inference in single-cell biology, reconstructing consistent dynamics with proliferation and apoptosis, estimating time-varying growth fields, and applying to generative dynamics under imbalanced data. It outperforms state-of-the-art baselines in efficiency, stability, and reconstruction accuracy. Overall, WFR-FM establishes a unified and efficient paradigm for learning dynamical systems from unbalanced snapshots, where not only states but also mass evolve over time.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

周沛劼，北京大学前沿交叉学科研究院国际机器学习研究中心和定量生物学中心研究员、博士生导师，博雅青年学者，国家级青年人才。2014年和2019年在北京大学数学科学学院获得计算数学学士和博士学位，获北京大学优秀博士论文奖；2020-2023年任美国加州大学尔湾分校数学系访问助理教授。主要从事计算系统生物学、单细胞组学动力学、复杂生物系统建模与AI for Science研究。相关成果发表在Nature正刊, 大子刊(NM, NCC, NMI,NG), NC, SA, PRX, MSB, AS等重要交叉学科期刊以及ICLR(Oral), ICML, NeurIPS, AAAI(Oral)等人工智能会议，并担任Nature Methods, PNAS, Nature Communications, Cell Genomics, Cell Systems, SIAP等多个期刊审稿人。

</details>


### 3. 基于Bellman缺陷校正的科学机器学习与生成式人工智能的推理算法

**讲者**：陆一平（北京大学 · 国际数学研究中心） · 15:00-15:30

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

传统大模型主要依赖“训练时扩展”（Training-time Scaling），但在处理复杂推理和前沿数学科学问题时，单纯堆参数已遭遇边际效应瓶颈。“推理时扩展”（Inference-time Scaling）打破了这一限制，它在推理阶段注入动态计算资源，实现“算力越多、效果越好”。然而，当前生成式 AI 缺乏普适的原则性设计框架，科学机器学习（SciML）领域也亟待类似的推理时扩展体系。为此，本报告借鉴科学计算中的缺陷校正（Defect Correction）思想，在推理时将数据驱动方法与底层机理有机融合，首次为推理时扩展提供了一个具备理论保障的统一Bellman Error Correction的原则性框架。具体包含两大核心应用： 面向科学机器学习（SciML）：针对高维半线性抛物型方程，我们将代理模型的误差严谨地表示为另一个抛物型方程的解，并利用基于蒙特卡洛的随机模拟算法对其高效修正。该方法在推理时模拟未来规划误差并动态校正当前解，实现了计算资源与精度的协同提升。我们进一步展现了离线数据驱动训练与在线机理修正的“两阶段结合”才能真正达到统计最优。 面向生成式人工智能：我们将规划过程与缺陷校正相结合，利用顺序蒙特卡洛（SMC）方法动态修正生成规划中的累积的Belmman误差。我们在理论上首次给出了该方法在大语言模型推理中的样本复杂度分析；针对扩散模型，我们构造了顺序蒙特卡洛方法失效的不收敛反例，并进一步设计了首个基于二点格式的扩散模型推理算法，有效确保了其方差不随离散步长缩小而恶化（或增大）。 本工作表明，通过深化数据与机理结合，将底层物理与数学规律转化为动态矫正算子来纠偏数据驱动模型在复杂推理中的累积漂移，能够让推理时算力的投入真正转化为兼具严格理论保障与高精度的智能决策。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

陆一平，北京大学北京国际数学研究中心助理教授。2019年本科毕业于北京大学应用数学专业，2023年于斯坦福大学获得应用数学博士学位；曾任纽约大学柯朗研究所柯朗讲师、美国西北大学工业工程与管理科学系助理教授。 他的研究主要聚焦于微分方程与深度学习的交叉领域，致力于将微分方程、随机过程和控制理论等经典领域与机器学习及随机实验进行深度融合。其代表性成果包括建立了微分方程与深度学习的联系，科学机器学习的最优样本复杂度，并于近期成功解决了困扰学术界长达35年的关于带符号BAR解（signed BAR solutions）唯一性的经典难题。 他曾获得 CPAL 新星奖、芝加哥大学数据科学新星奖、斯坦福跨学科研究生奖学金等多项荣誉，并长期担任 ICML、NeurIPS、ICLR 、 AISTATS 和AAAI等国际顶级机器学习会议的领域主席以及运筹学顶级期刊Mathematics of Operations Research的副编辑。

</details>


### 4. Offline Deep Q* Estimation with Diffusion Models

**讲者**：焦雨领（武汉大学 · 人工智能学院） · 15:30-16:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

In offline RL, estimating the optimal action-value function can be formulated as solving the optimal Bellman equation based solely on offline observations. A fundamental challenge is that the reward function and transition kernel are unknown, so the optimal Bellman operator is not directly observable from data. To address this issue, we propose a novel framework that decouples operator estimation from value function learning. In this approach, we first formulate conditional diffusion models to estimate the reward law and transition kernel, which induces a data-driven approximation of the optimal Bellman operator. We then plug these estimators into the Bellman equation and obtain a deep estimator of by minimizing the empirical Bellman residual over a neural network function class. We establish sharp nonasymptotic convergence rates for learning the optimal Bellman operator through an end-to-end analysis of conditional diffusion estimation in total variation distance.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

焦雨领，武汉大学人工智能学院，教授博导，副院长。入选教育部国家重大人才工程，主要研究机器学习、科学计算。近期关注深度学习数理基础，在计算数学、应用数学、统计学、电子工程、人工智能等领域的旗舰期刊和会议上发表论文四十多篇。主持国家重点研发计划课题、国家自然科学基金天元交叉重点项目、面上项目及一批同华为开展的校企合作项目。

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
