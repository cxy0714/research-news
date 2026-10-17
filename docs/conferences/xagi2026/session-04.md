# Session 04 · 预训练算法的新进展

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 5会（友谊宫二层5号会议室） · [返回会议总览](index.md)

- 3 场报告 · 已精读 1 场

**主持**：谢天（Qwen）

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场聚焦预训练阶段优化算法与评估范式的底层问题，三场报告共享一条主线：**在给定数据与算力约束下，如何通过优化器设计或超参数选择，让模型在相同训练成本下获得更强的下游能力**。张华清从工程视角讨论超参数缩放律的推导与外推；胡译文从理论视角修正优化器与参数化框架的错配；陈焕然则直接质疑“预训练损失”作为能力指标的充分性，提出以极小值点几何结构为目标的优化器。

最突出的主线是**优化器层面的能力边界突破**。胡译文的 Spectral Sphere Optimizer（SSO）针对 μP 与 Muon 的冲突——Muon 只约束更新方向、不约束权重谱半径，导致激活尺度漂移——在谱球切平面内构造满足最速下降与严格 μP 约束的更新，从优化器内部根治不稳定，而非依赖 SandwichNorm 等架构补丁。陈焕然的 Nexus 则从另一角度切入：标准 AdamW 收敛到各任务极小值点彼此疏远的区域，Nexus 通过最大化梯度相似度显式拉近这些极小值点，在相同预训练损失下显著提升 OOD 与推理性能。两者互补：SSO 解决“如何稳定地快速收敛”，Nexus 解决“收敛到何处更有泛化价值”。张华清的工作为这两者提供了超参数选择的量化基础——若优化器改变，原有缩放律是否仍成立，是其报告隐含的衔接点。

若时间有限，建议先看陈焕然（130M-3B 规模、多配比实验，直接挑战主流评估范式，结果可复现性强），再看胡译文（理论框架完整，适合理解优化器与参数化约束的深层关系），最后补张华清（为前两者提供超参数外推的工程工具）。三场按“现象-机制-工具”的顺序阅读，可形成完整闭环。

---

### 1. On Optimal Hyperparameter Scaling for LLM Pretraining

**讲者**：张华清（清华大学 · 交叉信息研究院） · 14:00-14:40

**对应论文**：Configuration-to-Performance Scaling Law with Neural Ansatz · [arXiv:2602.10300](https://arxiv.org/abs/2602.10300)

<details><summary>摘要（会议官网）</summary>

<p>Setting appropriate training hyperparameters is critical for efficient and stable large language model pretraining. Since sweeping hyperparameters at the target training scale is prohibitively expensive, a common approach is to use smaller training runs to fit a hyperparameter scaling law for extrapolation. In this talk, we discuss our approach to deriving hyperparameter scaling laws for the next generation of Qwen models (Qwen3.8-flash-next), which enables accurate extrapolation. Notably, the current hyperparameter scaling law predicts larger learning rates and batch sizes than our previous scaling law and several published results suggest. Through controlled ablation studies, we examine how other training factors (data, architecture, optimizer) influence hyperparameter scaling. We will also discuss several practical guidelines for fitting a hyperparameter scaling law as accurately as possible within a limited compute budget.</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>Huaqing Zhang is a first-year PhD at IIIS, Tsinghua University, advised by Prof. Andrew Yao. His research interests lie in the theory and training of large language models. He has been fortunate to work closely with Prof. Jingzhao Zhang and Prof. Kaifeng Lyu. He is currently interning with the Qwen pretraining team, where he works on scaling laws and optimizers.</p>

</details>


### 2. Controlled LLM Training on Spectral Sphere

**讲者**：胡译文（中国人民大学 · 高瓴人工智能学院） · 14:40-15:20

**对应论文**：Controlled LLM Training on Spectral Sphere · [arXiv:2601.08393](https://arxiv.org/abs/2601.08393) · 📖 [长篇精读](../../deep_reads/xagi2026-2601.08393.md)

<details><summary>摘要（会议官网）</summary>

<p>Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization (μP) provides a theoretical safeguard for width-invariant Θ(1) activation control, whereas emerging optimizers like Muon are only half-aligned with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the Spectral Sphere Optimizer (SSO), which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully μP-aligned optimization process. To enable large-scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.</p>

</details>

**问题**：（对应论文为自动检索推断，可能有偏差）大模型预训练需要稳定前提下的快速收敛。μP 理论上保证激活尺度 $\Theta(1)$，但 Muon 只约束更新、不约束权重，导致权重漂移与激活异常；现有做法靠 SandwichNorm、QK-Norm 等架构补丁强行稳定，牺牲表达力且调参成本高。报告要解决的问题是：能否构造一个同时满足最速下降与严格 μP 约束的优化器，从优化器层面根治不稳定？

**核心方法**：提出 Spectral Sphere Optimizer (SSO)。对权重 $W\in\mathbb{R}^{d_{\text{out}}\times d_{\text{in}}}$，令谱半径 $R=\Theta(\sqrt{d_{\text{out}}/d_{\text{in}}})$，更新 $\Delta W=\eta R\Phi$，其中 $\Phi$ 在谱球切平面内最大化 $\langle G,\Phi\rangle$ 且满足 $\langle\Theta,\Phi\rangle=0$（$\Theta=u_1v_1^\top$）。通过 Lagrange 乘子 $\lambda$ 搜索，$\Phi^*(\lambda)=\operatorname{msign}(G+\lambda\Theta)$，用 bracketing+bisection 求 $h(\lambda)=\langle\Theta,\operatorname{msign}(G+\lambda\Theta)\rangle$ 的根，并加 retraction 投影回谱球。在 Megatron 中实现原子模块分片、ping-pong 负载均衡、自适应 kernel 与多流并行。实验覆盖 Dense 1.7B、MoE 8B-A1B、200 层 DeepNet，均优于 AdamW 和 Muon，且改善 MoE 路由均衡、抑制 outlier、激活严格有界。

**与已有工作的关系**：SSO 直接推进 μP（Yang et al., 2024）的谱条件，补上 Muon（Jordan et al., 2024）缺失的权重约束。与 Scion（Pethick et al., 2025）及 MuonSphere（$\lambda=0$ 变体）相比，SSO 通过 $\lambda$ 搜索实现真正的切空间最速下降，而非简单归一化。实验还显示 SSO 在 μP 宽度扩展下学习率迁移更稳，且可去掉隐藏层权重衰减，减少一个超参数。

**贡献与边界**：主要贡献是给出一个完全 μP 对齐的优化器，兼具理论推导、分布式实现和跨架构验证。边界：论文为自动检索匹配，细节可能有偏差；SSO 每步比 Muon 慢 11.45%（表 2），CPU 端二分求解器带来同步开销；谱半径常数 $c$ 需人工调节（$c=2.0$ 最佳）；方法只作用于 2D 权重，embedding 仍用权重衰减。官网摘要未给出完整实验设置，泛化性仍需更多任务验证。

<details><summary>讲者简介</summary>

<p>中国人民大学博士研究生，导师为赵鑫老师。主要研究方向为大模型预训练和模型结构。曾获ICML Spotlight、ACL Oral等。</p>

</details>


### 3. Pretraining Loss相同，模型能力则相同么？

**讲者**：陈焕然（清华大学/字节跳动 · 人工智能学院） · 15:20-16:00

**对应论文**：Nexus : Same Pretraining Loss , Better Downstream Generalization via Common Minima · [arXiv:2604.09258](https://arxiv.org/abs/2604.09258)

<details><summary>摘要（会议官网）</summary>

<p>大语言模型的能力主要源于互联网级别数据上的预训练。在本工作中，我们提出了一个非常有趣的问题：“相同的预训练损失，一定意味着相同的模型能力吗？” 我们猜想，特定任务极小值点之间的几何“接近性”（Closeness）与下游泛化能力有着内在的必然联系。然而，标准的优化器（如 AdamW）往往会收敛到各任务特定极小值点彼此疏远的区域。为了打破这一局限，我们提出了 Nexus 优化器，通过在优化过程中最大化梯度相似度，显式促进这些极小值点的几何接近。在 130M 到 3B 参数规模的模型、多种数据配比和超参数下的广泛实验表明：尽管预训练损失完全相同，Nexus 却大幅度提升了下游任务的性能。 例如，Nexus 将分布外（OOD）损失降低了 0.012，并在复杂推理任务（如 GSM8k）上实现了高达 15.0% 的准确率提升。这一发现挑战了“将预训练损失作为评估模型能力唯一指标”的传统范式，有力证明了隐式偏置（Implicit Biases）在解锁下游泛化能力中的重要性。</p>

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

<p>I’m a PhD student at Tsinghua SAIL, advised by Prof. Jun Zhu and closely collaborating with Prof. Yinpeng Dong. I also work with Prof. Jingzhao Zhang’s group. I study the physics of deep learning: the optimization dynamics, geometry, and statistical mechanisms that could make neural-network training more explainable, predictable, and controllable.</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
