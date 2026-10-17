# Session 07 · 扩散模型的理论基础以及推理测算法

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 8会（友谊宫二层8号会议室） · [返回会议总览](index.md)

- 4 场报告 · 已精读 2 场

**主持**：陆一平（北京大学）、周默（北京大学）

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场的四场报告围绕“采样与推理”展开，但切入路径不同：前两场聚焦于概率分布的确定性/动态传输方法，后两场则从Bellman方程与强化学习的视角处理推理与误差校正。整体上，它们共享一个核心关切——如何在有限计算预算下，用可证明收敛或可扩展的算法逼近目标分布或最优策略。

最突出的主线是“动态最优传输与粒子流方法”。史作强提出的加权Laplacian流，将采样问题转化为确定性粒子流，通过演化对数密度比实现从初始分布到目标分布的传输，并给出收敛性保证，属于理论驱动的粒子方法。周沛劼的WFR-FM则针对非平衡动态最优传输，引入Wasserstein-Fisher-Rao度量，提出无模拟训练算法，直接学习速度场与质量变化项，实现一步推断，侧重可扩展性与计算效率。两者互补：史作强强调理论收敛性，周沛劼侧重算法实用性与非平衡场景，但都绕开了传统扩散模型的随机微分方程模拟。

另一条主线是“推理时扩展与Bellman误差校正”。陆一平借鉴科学计算中的缺陷校正思想，将代理模型误差表示为另一个抛物型方程的解，并用蒙特卡洛模拟修正，为推理时扩展提供统一框架，适用于高维半线性方程。焦雨领则从离线强化学习出发，将最优动作值估计转化为求解最优Bellman方程，通过解耦算子估计与扩散模型生成，应对奖励与转移核未知的挑战。这两场在方法上递进：陆一平用Bellman误差校正提升SciML推理，焦雨领则用扩散模型逼近Bellman算子，共同指向“用生成模型或校正机制替代精确求解”的推理范式。

若想快速建立本场脉络，建议先看史作强与周沛劼的两场，理解粒子流与动态OT的两种基础框架；随后进入陆一平或焦雨领，看Bellman思想如何迁移到推理与RL场景。若对理论收敛性感兴趣，优先史作强；若关注算法可扩展性，周沛劼更直接；若想了解推理时扩展的通用设计，陆一平提供了原则性框架。

---

### 1. Weighted Laplacian Flow: A Deterministic Particle Flow with Provable Convergence

**讲者**：史作强（清华大学 · 数学中心） · 14:00-14:30

**对应论文**：Weighted Laplacian Flow: A Deterministic Particle Flow with Exponential Convergence · [arXiv:2608.21831](https://arxiv.org/abs/2608.21831)

<details><summary>摘要（会议官网）</summary>

<p>Sampling from a target probability density is a fundamental task in statistics, machine learning, and scientific computing. We introduce weighted Laplacian flow, a deterministic particle-flow method that transports samples from a tractable initial density to a target density known up to normalization. The method evolves the logarithmic density ratio between the target and the transported distribution and constructs the particle velocity by solving a weighted Poisson equation associated with the target density. We establish the global well-posedness of the proposed PDE system and prove that the transported density converges to the target density. Under a sublinear forcing condition, the method achieves exact convergence in finite time. Numerical experiments on multimodal, heavy-tailed, and ten-dimensional targets demonstrate that weighted Laplacian flow can perform long-range mass transport, overcome energy barriers.</p>

</details>

**问题**  
从仅知未归一化密度的目标分布中采样，是统计与机器学习的基础任务。现有路线中，Langevin 动力学依赖局部 score 力，在多模态或重尾目标上易受能量势垒阻碍；SVGD 等确定性粒子法又高度依赖核函数的选择。报告提出 weighted Laplacian flow（WLF），旨在构造一种无需核、可证明收敛的确定性粒子流，以克服扩散型方法在长程质量输运上的低效。官网摘要强调，该方法在子线性强迫条件下还能实现有限时间精确收敛，这为采样理论提供了新的收敛保证。

**核心方法**  
WLF 不直接演化粒子密度，而是演化目标密度 $\rho$ 与当前输运密度 $q_t$ 的对数比 $\omega=\log(\rho/q_t)$。令粒子速度 $v=\nabla\phi$，通过目标加权 Poisson 方程  
$$L_\rho\phi:=\frac{1}{\rho}\nabla\cdot(\rho\nabla\phi)=-(\omega-\bar\omega)$$  
确定势函数 $\phi$，其中 $\bar\omega$ 由 Neumann 相容性条件决定。沿特征线，$\omega$ 满足中心化线性松弛 $\frac{d}{dt}\omega=-(\omega-\bar\omega)$，从而将采样问题转化为椭圆-输运耦合系统（论文中的式 (7)）。该构造的关键是：$\rho$ 乘任意正常数不改变 $\omega-\bar\omega$ 与速度场，因此天然免归一化；速度场由非局部椭圆算子给出，无需核函数。

**与已有工作的关系**  
论文明确将 WLF 与两条经典路线对比：一是 overdamped Langevin 动力学，其 Wasserstein 梯度流结构对应局部 score 力 $v_{\mathrm{Lan}}=\nabla\log(p/q)$；二是 SVGD，其均值场极限依赖核积分算子 $T_{k,q_t}$。WLF 则是在目标锚定度量下反向 KL 散度 $\mathrm{KL}(p\|q)$ 的梯度流，用目标加权 Poisson 逆算子替代核平滑，从而将输运几何从 Wasserstein 改为由固定目标 $p$ 决定的椭圆度量。这一构造与 He 等人关于正则化 Stein 流的联系不同，WLF 不引入正则化参数。

**贡献与边界**  
主要贡献包括：在 Lipschitz 初值下建立全局适定性（Schauder 不动点 + 对数椭圆估计）；证明对数密度比振荡精确按 $e^{-t}$ 收缩，进而得到 $L^\infty$ 收敛与 KL 散度指数衰减；给出精确熵耗散恒等式，耗散率恰为 Jeffreys 散度；并揭示其变分几何结构。边界方面：理论限于有界光滑域与齐次 Neumann 边界，要求 $\rho$ 严格正光滑；官网摘要仅报告十维数值实验，论文摘要称“高维”但未给出具体规模与运行时间；有限时间精确收敛依赖子线性强迫条件，一般情形仅为指数收敛。官网摘要未给出与其他方法的数值对比。

<details><summary>讲者简介</summary>

<p>史作强，清华大学丘成桐数学科学中心长聘教授，北京雁栖湖应用数学研究院双聘研究员，主要研究方向为偏微分方程数值方法，微分方程与机器学习，非线性非平稳信号时频分析等，在国际知名学术期刊和学术会议发表文章100余篇。</p>

</details>


### 2. Simulation-Free Dynamic Unbalanced Optimal Transport and One-step Inference

**讲者**：周沛劼（北京大学 · 前沿交叉学科研究院） · 14:30-15:00

**对应论文**：WFR-FM: Simulation-Free Dynamic Unbalanced Optimal Transport · [arXiv:2601.06810](https://arxiv.org/abs/2601.06810)

<details><summary>摘要（会议官网）</summary>

<p>The Wasserstein-Fisher-Rao (WFR) metric extends dynamic optimal transport (OT) by coupling displacement with change of mass, providing a principled geometry for modeling unbalanced snapshot dynamics. Existing WFR solvers, however, are often unstable, computationally expensive, and difficult to scale. Here we introduce WFR Flow Matching (WFR-FM), a simulation-free training algorithm that unifies flow matching with dynamic unbalanced OT. Unlike classical flow matching which regresses only a transport vector field, WFR-FM simultaneously regresses a vector field for displacement and a scalar growth rate function for birth-death dynamics, yielding continuous flows under the WFR geometry. Theoretically, we show that minimizing the WFR-FM loss exactly recovers WFR geodesics. Empirically, WFR-FM yields more accurate and robust trajectory inference in single-cell biology, reconstructing consistent dynamics with proliferation and apoptosis, estimating time-varying growth fields, and applying to generative dynamics under imbalanced data. It outperforms state-of-the-art baselines in efficiency, stability, and reconstruction accuracy. Overall, WFR-FM establishes a unified and efficient paradigm for learning dynamical systems from unbalanced snapshots, where not only states but also mass evolve over time.</p>

</details>

**问题**：单细胞转录组测序只能得到少量时间快照，且细胞增殖与凋亡使总质量不守恒，因此需要在不平衡最优传输（UOT）框架下重建连续动态。Wasserstein-Fisher-Rao（WFR）度量同时刻画位移与质量生灭，为不平衡动态建模提供原理性几何，但现有 WFR 求解器不稳定、计算昂贵、难以扩展。经典 flow matching 只回归传输速度场，无法处理质量变化。报告提出 WFR-FM，目标是在 simulation-free 框架下同时学习位移场与生长率，并精确恢复 WFR 测地线。

**核心方法**：WFR-FM 将 flow matching 推广到不平衡动态。核心构造是 traveling Gaussian 条件路径：利用 WFR 度量下两个 Dirac 测度间 traveling Dirac 测地线的解析形式（$m(t)=At^2-2Bt+m_0$，$u(t)m(t)=\omega_0$），定义条件向量场 $u_t(x|z)$ 与条件生长率 $g_t(x|z)$。训练时最小化条件不平衡 flow matching 损失 $L_{CUFM}=\mathbb{E}_{t,z,x\sim\tilde\rho_t(\cdot|z)}[(\|v_\theta-u_t\|^2+\kappa\|g_\phi-g_t\|^2)m_t(z)]$，并证明该损失与原始不平衡 flow matching 损失梯度一致，从而无需 ODE 模拟。对多时间点数据，先通过 mini-batch WFR-OET 求解半耦合，再共享网络参数训练。

**与已有工作的关系**：在不平衡 flow matching 方向上，已有工作如 Eyring et al.、Corso et al. 只回归速度场而忽略生长率；VGFM（Wang et al.）虽联合学习传输与生长，但将生灭与传输分离，且后处理仍需 ODE 模拟，并非完全 simulation-free。Action Matching 与 WLF 虽免模拟，但前者需要连续密度曲线，后者引入内外层优化开销。WFR-FM 与 OT-CFM（Tong et al.）的平衡情形相容：当 $m_t\equiv1$、$g_t\equiv0$ 时退化为标准 flow matching。论文在 Gene、Dyngen、1000 维高斯混合及真实胚胎体数据上对比了 TIGON、DeepRUOT、Var-RUOT 等基线，称 WFR-FM 在 $W_1$ 与相对质量误差（RME）上均最优（具体数值在节选中未完整给出）。

**贡献与边界**：主要贡献是给出一个理论上有保证、训练完全免模拟的不平衡动态 OT 求解器，同时恢复速度场与生长率，并支持多时间点轨迹推断。边界：方法依赖 WFR 度量与 traveling Dirac 测地线的解析形式，对非 Dirac 初值依赖高斯条件路径近似；mini-batch WFR-OET 是对全局耦合的近似，可能引入偏差；超参数 $\delta,\sigma,\kappa$ 需调节。报告题目中的 "one-step inference" 在摘要与节选中未展开，官网摘要未给出具体机制。整体上，该工作适合关注单细胞轨迹推断与生成模型理论交叉的研究者。

<details><summary>讲者简介</summary>

<p>周沛劼，北京大学前沿交叉学科研究院国际机器学习研究中心和定量生物学中心研究员、博士生导师，博雅青年学者，国家级青年人才。2014年和2019年在北京大学数学科学学院获得计算数学学士和博士学位，获北京大学优秀博士论文奖；2020-2023年任美国加州大学尔湾分校数学系访问助理教授。主要从事计算系统生物学、单细胞组学动力学、复杂生物系统建模与AI for Science研究。相关成果发表在Nature正刊, 大子刊(NM, NCC, NMI,NG), NC, SA, PRX, MSB, AS等重要交叉学科期刊以及ICLR(Oral), ICML, NeurIPS, AAAI(Oral)等人工智能会议，并担任Nature Methods, PNAS, Nature Communications, Cell Genomics, Cell Systems, SIAP等多个期刊审稿人。</p>

</details>


### 3. 基于Bellman缺陷校正的科学机器学习与生成式人工智能的推理算法

**讲者**：陆一平（北京大学 · 国际数学研究中心） · 15:00-15:30

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>传统大模型主要依赖“训练时扩展”（Training-time Scaling），但在处理复杂推理和前沿数学科学问题时，单纯堆参数已遭遇边际效应瓶颈。“推理时扩展”（Inference-time Scaling）打破了这一限制，它在推理阶段注入动态计算资源，实现“算力越多、效果越好”。然而，当前生成式 AI 缺乏普适的原则性设计框架，科学机器学习（SciML）领域也亟待类似的推理时扩展体系。为此，本报告借鉴科学计算中的缺陷校正（Defect Correction）思想，在推理时将数据驱动方法与底层机理有机融合，首次为推理时扩展提供了一个具备理论保障的统一Bellman Error Correction的原则性框架。具体包含两大核心应用： 面向科学机器学习（SciML）：针对高维半线性抛物型方程，我们将代理模型的误差严谨地表示为另一个抛物型方程的解，并利用基于蒙特卡洛的随机模拟算法对其高效修正。该方法在推理时模拟未来规划误差并动态校正当前解，实现了计算资源与精度的协同提升。我们进一步展现了离线数据驱动训练与在线机理修正的“两阶段结合”才能真正达到统计最优。 面向生成式人工智能：我们将规划过程与缺陷校正相结合，利用顺序蒙特卡洛（SMC）方法动态修正生成规划中的累积的Belmman误差。我们在理论上首次给出了该方法在大语言模型推理中的样本复杂度分析；针对扩散模型，我们构造了顺序蒙特卡洛方法失效的不收敛反例，并进一步设计了首个基于二点格式的扩散模型推理算法，有效确保了其方差不随离散步长缩小而恶化（或增大）。 本工作表明，通过深化数据与机理结合，将底层物理与数学规律转化为动态矫正算子来纠偏数据驱动模型在复杂推理中的累积漂移，能够让推理时算力的投入真正转化为兼具严格理论保障与高精度的智能决策。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>陆一平，北京大学北京国际数学研究中心助理教授。2019年本科毕业于北京大学应用数学专业，2023年于斯坦福大学获得应用数学博士学位；曾任纽约大学柯朗研究所柯朗讲师、美国西北大学工业工程与管理科学系助理教授。 他的研究主要聚焦于微分方程与深度学习的交叉领域，致力于将微分方程、随机过程和控制理论等经典领域与机器学习及随机实验进行深度融合。其代表性成果包括建立了微分方程与深度学习的联系，科学机器学习的最优样本复杂度，并于近期成功解决了困扰学术界长达35年的关于带符号BAR解（signed BAR solutions）唯一性的经典难题。 他曾获得 CPAL 新星奖、芝加哥大学数据科学新星奖、斯坦福跨学科研究生奖学金等多项荣誉，并长期担任 ICML、NeurIPS、ICLR 、 AISTATS 和AAAI等国际顶级机器学习会议的领域主席以及运筹学顶级期刊Mathematics of Operations Research的副编辑。</p>

</details>


### 4. Offline Deep Q* Estimation with Diffusion Models

**讲者**：焦雨领（武汉大学 · 人工智能学院） · 15:30-16:00

**对应论文**：Offline Deep Q * Estimation with Diffusion Models · [arXiv:2608.14401](https://arxiv.org/abs/2608.14401)

<details><summary>摘要（会议官网）</summary>

<p>In offline RL, estimating the optimal action-value function can be formulated as solving the optimal Bellman equation based solely on offline observations. A fundamental challenge is that the reward function and transition kernel are unknown, so the optimal Bellman operator is not directly observable from data. To address this issue, we propose a novel framework that decouples operator estimation from value function learning. In this approach, we first formulate conditional diffusion models to estimate the reward law and transition kernel, which induces a data-driven approximation of the optimal Bellman operator. We then plug these estimators into the Bellman equation and obtain a deep estimator of by minimizing the empirical Bellman residual over a neural network function class. We establish sharp nonasymptotic convergence rates for learning the optimal Bellman operator through an end-to-end analysis of conditional diffusion estimation in total variation distance.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>焦雨领，武汉大学人工智能学院，教授博导，副院长。入选教育部国家重大人才工程，主要研究机器学习、科学计算。近期关注深度学习数理基础，在计算数学、应用数学、统计学、电子工程、人工智能等领域的旗舰期刊和会议上发表论文四十多篇。主持国家重点研发计划课题、国家自然科学基金天元交叉重点项目、面上项目及一批同华为开展的校企合作项目。</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
