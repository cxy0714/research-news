# Session 12 · 扩散语言模型

> XAGI 2026 交叉智能大会 · 10 月 18 日（周日）上午 10:00-12:00 · 7会（友谊宫二层7号会议室） · [返回会议总览](index.md)

- 3 场报告 · 已精读 0 场

**主持**：胡天阳（香港中文大学（深圳））

---

### 1. Parallel Generation, Iterative Refinement: The Evolution of LLaDA 2.x in Practice

**讲者**：刘华斌（蚂蚁集团） · 10:00-10:40

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

扩散语言模型通过并行生成与迭代去噪，为大语言模型提供了不同于逐 token 自回归生成的技术路径。如何将这种潜力转化为可规模化训练、高效推理，并能胜任复杂任务的模型，是 LLaDA 团队持续探索的核心问题。本报告将以 LLaDA 2.x 系列的演进为主线，介绍团队在dLLM模型训练、推理机制与Agentic能力上的研究与实践：LLaDA 2.0 通过自回归模型到块扩散模型的渐进式转换，将扩散语言模型扩展至千亿参数规模；LLaDA 2.1 将并行生成与 token 编辑结合，改善解码速度与生成质量的权衡；LLaDA 2.2 进一步引入支持插入、删除与替换的编辑机制，结合长上下文、块级专家路由和面向交互反馈的强化学习，探索多轮、长程智能体任务。在此基础上，报告将讨论扩散语言模型在训练目标、并行解码与迭代修正中的关键问题，并展望其与自回归模型的协同，以及向原生多模态统一模型的发展方向。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

刘华斌，博士毕业于上海交通大学，现就职于蚂蚁技术研究院-LLaDA团队，专注于扩散语言模型的训练范式和架构研究。

</details>


### 2. 扩散式语言建模探索：从掩码扩散到连续扩散

**讲者**：胡天阳（香港中文大学（深圳） · 数据科学学院） · 10:40-11:20

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

自回归建模是当前大语言模型的主流范式，而扩散模型为语言建模与生成提供了一条不同的研究路径。本报告介绍我们从掩码扩散到连续扩散的一系列探索，讨论这一路径的潜力、局限与关键设计问题。首先，通过解耦建模范式与网络架构，重新审视掩码扩散与自回归建模的比较，并探讨潜变量方法如何缓解少步并行采样中的依赖建模不足。随后，我们转向连续扩散语言模型，围绕预训练与生成两个环节，探索适配连续去噪过程的 Transformer 架构设计，并重点介绍面向单步与少步生成的蒸馏研究。这些工作关注连续空间预测与离散 token 生成之间的关系，以及如何在降低预测不确定性的同时保留样本多样性。报告将结合这些探索，讨论扩散式语言建模的设计思路与尚待解决的问题。

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

胡天阳现为香港中文大学（深圳）数据科学学院的助理教授。他的主要研究方向为人工智能与统计的交叉领域，包括统计机器学习、可信 AI、特征表示学习、深度生成模型等，旨在通过揭示 AI 模型的深层机制，为设计更有效的新算法提供理论指导。

</details>


### 3. ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings

**讲者**：李根（香港中文大学 · 统计与数据科学） · 11:20-12:00

**对应论文**：待匹配（精读该场时自动检索 arXiv / OpenAlex）

<details><summary>摘要（会议官网）</summary>

Existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce ConvergeFlow, an embedding-space flow-based LM, which constrains the data predictor to the convex hull of token embeddings and trains it solely with the mean squared error objective induced by flow matching. Under suitable regularity conditions, we prove that the resulting flow converges to valid token embeddings despite errors in the data predictor, enabling direct token prediction without a CE-supervised decoder. We further develop three sampling mechanisms for controlling the trade-off between the generative perplexity and entropy. Experiments on OpenWebText demonstrate that ConvergeFlow achieves performance competitive with existing continuous and discrete diffusion LMs. These findings demonstrate the potential of the flow-based paradigm for language modeling.

</details>

*（待精读 — 本场在精读队列中）*

<details><summary>讲者简介</summary>

Gen Li is currently an assistant professor in the Department of Statistics and Data Science at the Chinese University of Hong Kong. His research interests include diffusion model, generative AI and reinforcement learning.

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
