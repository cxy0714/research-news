# Session 04 · 预训练算法的新进展

> XAGI 2026 交叉智能大会 · 10 月 17 日（周六）下午 14:00-16:00 · 5会（友谊宫二层5号会议室） · [返回会议总览](index.md)

- 3 场报告 · 已精读 0 场

**主持**：谢天（Qwen）

---

### 1. On Optimal Hyperparameter Scaling for LLM Pretraining

**讲者**：张华清（清华大学 · 交叉信息研究院） · 14:00-14:40

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

Setting appropriate training hyperparameters is critical for efficient and stable large language model pretraining. Since sweeping hyperparameters at the target training scale is prohibitively expensive, a common approach is to use smaller training runs to fit a hyperparameter scaling law for extrapolation. In this talk, we discuss our approach to deriving hyperparameter scaling laws for the next generation of Qwen models (Qwen3.8-flash-next), which enables accurate extrapolation. Notably, the current hyperparameter scaling law predicts larger learning rates and batch sizes than our previous scaling law and several published results suggest. Through controlled ablation studies, we examine how other training factors (data, architecture, optimizer) influence hyperparameter scaling. We will also discuss several practical guidelines for fitting a hyperparameter scaling law as accurately as possible within a limited compute budget.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

Huaqing Zhang is a first-year PhD at IIIS, Tsinghua University, advised by Prof. Andrew Yao. His research interests lie in the theory and training of large language models. He has been fortunate to work closely with Prof. Jingzhao Zhang and Prof. Kaifeng Lyu. He is currently interning with the Qwen pretraining team, where he works on scaling laws and optimizers.

</details>


### 2. Controlled LLM Training on Spectral Sphere

**讲者**：胡译文（中国人民大学 · 高瓴人工智能学院） · 14:40-15:20

**对应论文**：Controlled LLM Training on Spectral Sphere · [arXiv:2601.08393](https://arxiv.org/abs/2601.08393)

<details><summary>摘要（会议官网）</summary>

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization (μP) provides a theoretical safeguard for width-invariant Θ(1) activation control, whereas emerging optimizers like Muon are only half-aligned with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the Spectral Sphere Optimizer (SSO), which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully μP-aligned optimization process. To enable large-scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

中国人民大学博士研究生，导师为赵鑫老师。主要研究方向为大模型预训练和模型结构。曾获ICML Spotlight、ACL Oral等。

</details>


### 3. Pretraining Loss相同，模型能力则相同么？

**讲者**：陈焕然（清华大学/字节跳动 · 人工智能学院） · 15:20-16:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

大语言模型的能力主要源于互联网级别数据上的预训练。在本工作中，我们提出了一个非常有趣的问题：“相同的预训练损失，一定意味着相同的模型能力吗？” 我们猜想，特定任务极小值点之间的几何“接近性”（Closeness）与下游泛化能力有着内在的必然联系。然而，标准的优化器（如 AdamW）往往会收敛到各任务特定极小值点彼此疏远的区域。为了打破这一局限，我们提出了 Nexus 优化器，通过在优化过程中最大化梯度相似度，显式促进这些极小值点的几何接近。在 130M 到 3B 参数规模的模型、多种数据配比和超参数下的广泛实验表明：尽管预训练损失完全相同，Nexus 却大幅度提升了下游任务的性能。 例如，Nexus 将分布外（OOD）损失降低了 0.012，并在复杂推理任务（如 GSM8k）上实现了高达 15.0% 的准确率提升。这一发现挑战了“将预训练损失作为评估模型能力唯一指标”的传统范式，有力证明了隐式偏置（Implicit Biases）在解锁下游泛化能力中的重要性。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

I’m a PhD student at Tsinghua SAIL, advised by Prof. Jun Zhu and closely collaborating with Prof. Yinpeng Dong. I also work with Prof. Jingzhao Zhang’s group. I study the physics of deep learning: the optimization dynamics, geometry, and statistical mechanisms that could make neural-network training more explainable, predictable, and controllable.

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
