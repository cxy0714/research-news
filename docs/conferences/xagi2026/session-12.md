# Session 12 · 扩散语言模型

> XAGI 2026 交叉智能大会 · 10 月 18 日（周日）上午 10:00-12:00 · 7会（友谊宫二层7号会议室） · [返回会议总览](index.md)

- 3 场报告 · 已精读 3 场

**主持**：胡天阳（香港中文大学（深圳））

## 本场导览

> 自动生成：归纳本场主线，**不打分、不排名**。

这一场聚焦扩散语言模型（dLLM）的技术路径与系统实现，三条主线清晰：**规模化训练与推理**（刘华斌的LLaDA 2.x系列）、**建模范式对比与架构设计**（胡天阳从掩码到连续扩散的探索）、**生成收敛性与目标函数**（李根的ConvergeFlow）。三场报告均围绕“如何让扩散模型在语言任务上实用化”展开，但切入角度不同：刘华斌侧重工程落地，胡天阳侧重理论机制，李根则直接挑战现有连续扩散框架的收敛缺陷。

最突出的主线是**连续扩散语言模型的生成质量与训练目标**。刘华斌的LLaDA 2.0通过自回归到块扩散的渐进转换解决规模扩展，2.1引入并行生成与token编辑平衡速度与质量，2.2加入插入/删除/替换机制并配合块级专家路由与RL，面向多轮智能体任务——这条线是“系统级”推进，强调编辑操作与长上下文能力。胡天阳则从“解耦建模范式与网络架构”入手，比较掩码扩散与自回归，指出潜变量方法可缓解少步采样中的依赖建模不足，并转向连续扩散的Transformer适配与蒸馏研究，关注连续预测与离散token生成的关系——这是“机制级”分析，与刘华斌的工程路线互补。李根的ConvergeFlow直接针对连续框架依赖交叉熵解码器的痛点，将数据预测器约束在token嵌入的凸包内，仅用MSE训练，保证流轨迹收敛到有效嵌入——这是“目标函数级”修正，与胡天阳讨论的“连续空间预测不确定性”形成递进：胡天阳指出问题，李根给出约束解法。

若想快速建立全局图景，先看刘华斌的LLaDA 2.x（覆盖训练、推理、应用全链路，适合作为系统入口）；若关注理论机制与范式对比，胡天阳的报告提供掩码与连续扩散的对照框架；若对生成收敛性有具体疑问，李根的ConvergeFlow是针对性补充。三场按“系统-机制-目标”顺序阅读，可形成从实践到理论的完整链条。

---

### 1. Parallel Generation, Iterative Refinement: The Evolution of LLaDA 2.x in Practice

**讲者**：刘华斌（蚂蚁集团） · 10:00-10:40

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>扩散语言模型通过并行生成与迭代去噪，为大语言模型提供了不同于逐 token 自回归生成的技术路径。如何将这种潜力转化为可规模化训练、高效推理，并能胜任复杂任务的模型，是 LLaDA 团队持续探索的核心问题。本报告将以 LLaDA 2.x 系列的演进为主线，介绍团队在dLLM模型训练、推理机制与Agentic能力上的研究与实践：LLaDA 2.0 通过自回归模型到块扩散模型的渐进式转换，将扩散语言模型扩展至千亿参数规模；LLaDA 2.1 将并行生成与 token 编辑结合，改善解码速度与生成质量的权衡；LLaDA 2.2 进一步引入支持插入、删除与替换的编辑机制，结合长上下文、块级专家路由和面向交互反馈的强化学习，探索多轮、长程智能体任务。在此基础上，报告将讨论扩散语言模型在训练目标、并行解码与迭代修正中的关键问题，并展望其与自回归模型的协同，以及向原生多模态统一模型的发展方向。</p>

</details>

*（未检索到公开论文，以下依据报告摘要与讲者方向推断）*

**问题**  
扩散语言模型通过并行生成与迭代去噪，提供了一条不同于逐 token 自回归生成的技术路径，但其潜力尚未转化为可规模化训练、高效推理且能胜任复杂任务的模型。报告以 LLaDA 2.x 系列演进为主线，核心问题是：如何让扩散语言模型在参数规模、解码效率与任务能力上逼近甚至超越自回归模型。当前大模型主流仍为自回归架构，扩散路线需要证明自身在千亿参数级别上的可行性与实用性，因此该报告聚焦工程化实践而非理论推导。

**核心方法**  
LLaDA 2.0 采用自回归模型到块扩散模型的渐进式转换，将扩散语言模型扩展至千亿参数规模；2.1 将并行生成与 token 编辑结合，改善解码速度与生成质量的权衡；2.2 进一步引入支持插入、删除与替换的编辑机制，并配合长上下文、块级专家路由和面向交互反馈的强化学习，探索多轮、长程智能体任务。官网摘要未给出具体模型结构、训练损失函数、编辑操作实现方式或推理加速比等细节，仅能确认其技术路线是“渐进式转换 + 编辑机制 + 强化学习”。

**与已有工作的关系**  
该工作属于扩散语言模型（dLLM）路线，相对自回归逐 token 生成提出替代方案。其演进路径从纯扩散生成逐步加入 token 编辑，类似将并行解码与局部修正结合，但摘要未点名任何基线或同期工作，无法判断与哪些模型直接对比。摘要中“块级专家路由”暗示可能借鉴混合专家（MoE）思想，“面向交互反馈的强化学习”则与 RLHF/RLVR 等后训练范式相关，这些属于方向层面的推断，具体设计未知。

**贡献与边界**  
主要贡献是展示了扩散语言模型在千亿参数规模上的渐进式训练路径，以及通过编辑机制增强多轮、长程智能体任务的能力。边界：未检索到公开论文，摘要未提供评测基准、计算开销、与自回归模型的系统对比，也未说明渐进式转换的收敛代价或编辑机制在长上下文下的复杂度。适用场景可能偏向交互式任务，但能否推广到通用生成任务仍需更多证据。

<details><summary>讲者简介</summary>

<p>刘华斌，博士毕业于上海交通大学，现就职于蚂蚁技术研究院-LLaDA团队，专注于扩散语言模型的训练范式和架构研究。</p>

</details>


### 2. 扩散式语言建模探索：从掩码扩散到连续扩散

**讲者**：胡天阳（香港中文大学（深圳） · 数据科学学院） · 10:40-11:20

**对应论文**：未检索到公开论文（以下为依据报告摘要与讲者方向的推断）

<details><summary>摘要（会议官网）</summary>

<p>自回归建模是当前大语言模型的主流范式，而扩散模型为语言建模与生成提供了一条不同的研究路径。本报告介绍我们从掩码扩散到连续扩散的一系列探索，讨论这一路径的潜力、局限与关键设计问题。首先，通过解耦建模范式与网络架构，重新审视掩码扩散与自回归建模的比较，并探讨潜变量方法如何缓解少步并行采样中的依赖建模不足。随后，我们转向连续扩散语言模型，围绕预训练与生成两个环节，探索适配连续去噪过程的 Transformer 架构设计，并重点介绍面向单步与少步生成的蒸馏研究。这些工作关注连续空间预测与离散 token 生成之间的关系，以及如何在降低预测不确定性的同时保留样本多样性。报告将结合这些探索，讨论扩散式语言建模的设计思路与尚待解决的问题。</p>

</details>

*（未检索到公开论文，以下依据报告摘要与讲者方向推断）*

**问题**：当前大语言模型以自回归建模为主流，但自回归的逐 token 顺序生成在推理效率与并行性上存在瓶颈。扩散模型已在连续信号生成上取得成功，能否将其迁移到离散的语言建模与生成，成为一条值得探索的替代路径。报告从掩码扩散与连续扩散两个方向切入，试图回答：扩散式语言建模能否在少步并行采样下保持依赖建模能力，以及如何弥合连续空间预测与离散 token 生成之间的鸿沟。

**核心方法**：报告提出两条递进的技术路线。其一，在掩码扩散中，将建模范式与网络架构解耦，重新设计比较实验，并引入潜变量方法以缓解少步并行采样时依赖建模不足的问题。其二，转向连续扩散语言模型，围绕预训练与生成两个环节，改造 Transformer 架构以适配连续去噪过程；同时针对单步与少步生成开展蒸馏研究，核心关注如何在降低预测不确定性的同时保留样本多样性。官网摘要未给出具体模型名称、参数量或实验数值。

**与已有工作的关系**：该工作直接对标自回归建模这一主流范式，属于扩散模型在语言领域的系统化探索。掩码扩散部分与同期基于离散去噪的掩码语言模型路线相关，但强调通过解耦范式与架构来获得更公平的比较；连续扩散部分则承接连续信号扩散模型的思想，并针对语言离散性做架构与蒸馏层面的适配。讲者背景为统计机器学习与深度生成模型，报告整体偏向方法机制分析与设计原则提炼。

**贡献与边界**：主要贡献在于系统梳理了从掩码扩散到连续扩散的设计空间，指出潜变量建模、架构适配与蒸馏是提升少步生成质量的关键杠杆，并揭示了连续预测与离散生成之间的张力。边界方面，官网摘要未给出实验验证细节，无法判断方法在标准语言建模基准上的实际表现；且讨论集中于生成环节，对扩散模型在长文本、大规模预训练下的可扩展性未作说明。依赖的假设是少步并行采样值得以一定质量损失换取效率，这一权衡在不同任务上可能差异显著。

<details><summary>讲者简介</summary>

<p>胡天阳现为香港中文大学（深圳）数据科学学院的助理教授。他的主要研究方向为人工智能与统计的交叉领域，包括统计机器学习、可信 AI、特征表示学习、深度生成模型等，旨在通过揭示 AI 模型的深层机制，为设计更有效的新算法提供理论指导。</p>

</details>


### 3. ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings

**讲者**：李根（香港中文大学 · 统计与数据科学） · 11:20-12:00

**对应论文**：ConvergeFlow : Language Flow with Provable Convergence to Token Embeddings · [arXiv:2608.23551](https://arxiv.org/abs/2608.23551)

<details><summary>摘要（会议官网）</summary>

<p>Existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce ConvergeFlow, an embedding-space flow-based LM, which constrains the data predictor to the convex hull of token embeddings and trains it solely with the mean squared error objective induced by flow matching. Under suitable regularity conditions, we prove that the resulting flow converges to valid token embeddings despite errors in the data predictor, enabling direct token prediction without a CE-supervised decoder. We further develop three sampling mechanisms for controlling the trade-off between the generative perplexity and entropy. Experiments on OpenWebText demonstrate that ConvergeFlow achieves performance competitive with existing continuous and discrete diffusion LMs. These findings demonstrate the potential of the flow-based paradigm for language modeling.</p>

</details>

**问题**：现有连续扩散/流式语言模型（LM）虽在嵌入空间上定义生成过程，但采样轨迹并不保证终止于合法的 token embedding，因此仍需额外训练一个以交叉熵（CE）监督的解码器来把连续状态映射回离散 token。这使“纯连续”的流式范式并不完整。ConvergeFlow 要回答的问题是：能否让流式 LM 的轨迹直接收敛到合法 token embedding，从而去掉 CE 解码器？在连续流式 LM 已能与离散扩散 LM 性能竞争的背景下，这一理论保证的缺失成为当前值得补上的关键环节。

**核心方法**：ConvergeFlow 在嵌入空间上做流匹配，将数据预测器参数化为 token embedding 凸包上的加权平均：$\mu_\theta^{(i)}(x_t,t)=\sum_{j=1}^V w_\theta^{(i)}(j|x_t,t)e_j$，其中权重由可学习基函数与加噪过程诱导的精确高斯核相乘并归一化得到。训练只使用流匹配导出的均方误差（MSE）目标，完全不引入 CE 损失。作者证明，在基函数恒正且 log-权重沿采样轨迹 Lipschitz 连续等正则条件下，流会收敛到合法 token embedding。此外还提出三种采样机制，用于显式控制生成困惑度（Gen. PPL）与熵之间的权衡。在 OpenWebText 上，ConvergeFlow 在数据集熵 5.44 处取得 Gen. PPL 33.17，模型规模 130M。

**与已有工作的关系**：该工作直接针对连续流式 LM 的短板：LangFlow 和 FLM 在轨迹上施加 CE 目标，ELF 则在最终解码步使用 CE，三者都未摆脱离散监督。ConvergeFlow 沿用 LangFlow 的预训练 embedding 并固定不变，但把凸组合参数化仅作为架构约束，训练目标纯粹是 FM 的 MSE。与离散扩散 LM（如 MDLM、Duo、SEDD）相比，它保留了连续框架的全部工具（如 ODE 求解、自条件化），并在报告结果中达到与离散基线竞争的性能；在相同熵水平下，其 Gen. PPL 明显低于所列连续基线（约 60），也低于表中 AR Transformer 的 35.90。

**贡献与边界**：主要贡献是给出了首个（据作者所述）可证明收敛到 token embedding 的流式 LM，从而在理论上允许去掉 CE 解码器，并提供质量—多样性的显式控制。边界也很清楚：理论结论依赖基函数正性和 Lipschitz 连续性等正则假设；embedding 矩阵来自预训练 LangFlow 且固定，未与流模型联合学习；实验仅在 OpenWebText 上报告，官网摘要未给出采样机制的具体实现、计算成本及更大规模验证。因此，其“可证明收敛”目前是在特定构造与假设下的保证，尚不能直接外推到任意嵌入空间或训练设置。

<details><summary>讲者简介</summary>

<p>Gen Li is currently an assistant professor in the Department of Statistics and Data Science at the Chinese University of Hong Kong. His research interests include diffusion model, generative AI and reinforcement learning.</p>

</details>


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)
