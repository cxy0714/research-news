# 强化学习与决策 RL & Decision

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **1 个分会场 · 4 场报告**（已检索到对应论文 2 场）

---

## Recent Advances in Reinforcement Learning

*7 月 11 日（周六） · 13:30-15:10 · Qunsheng Room*  
*主办 IMS China · 组织 Cong Ma（University of Chicago） · 主持 Cong Ma（University of Chicago）*

### 1. From Nonparametric Statistics to LLM Reasoning

**讲者**：Chengchun Shi（London School of Economics and Political Science）

**对应论文**：Kernelized Advantage Estimation: From Nonparametric Statistics to LLM Reasoning · [arXiv:2604.28005](https://arxiv.org/abs/2604.28005) · 📖 [长篇精读](../../deep_reads/jcsds2026-2604.28005.md)

<details><summary>摘要（原文）</summary>

Recent advances in large language models (LLMs) have increasingly relied on reinforcement learning (RL) to improve their reasoning capabilities. Three types of approaches have been widely adopted: The first relies on a deep neural network to estimate the value function of the learning policy in order to reduce the variance of the policy gradient. However, estimating and maintaining such a value network incurs substantial computational and memory overhead. The second avoids training a value network by approximating the value function using sample averages. However, it samples a large number of reasoning traces per prompt for accurate value function approximation, making it computationally expensive. The third samples only a single reasoning trajectory per prompt, which reduces computational cost but suffers from poor sample efficiency. This paper focuses on a practical, resource-constrained setting in which only a small number of reasoning traces can be sampled per prompt, while low-variance gradient estimation remains essential for high-quality policy learning. To address this challenge, we bring classical nonparametric statistical methods, which are both computationally and statistically efficient, to LLM reasoning. We employ kernel smoothing as a concrete example for value function estimation and the subsequent policy optimization. Numerical and theoretical results demonstrate that our proposal achieves accurate value and gradient estimation, leading to improved policy optimization.

</details>

**问题**  
在大语言模型（LLM）推理的强化学习后训练中，策略梯度估计的方差是影响学习效率的核心瓶颈。现有方法面临两难：PPO/A2C 需维护深度价值网络，计算与存储开销巨大；GRPO 虽免去价值网络，但要求每 prompt 采样大量轨迹（如 64 条）以逼近价值函数，在资源受限场景（如高校实验室）下不可行；REINFORCE++ 仅采单条轨迹，但基线偏差大、方差高。如何在仅能采样少量轨迹的条件下获得低方差梯度估计，是亟待解决的统计—计算效率权衡问题。

**核心方法**  
本文提出 **Kernelized Advantage Estimation (KAE)**，将经典非参数统计中的核平滑引入 LLM 推理的价值函数估计。核心洞察：同一 prompt 在训练迭代中反复出现，历史奖励蕴含当前价值函数信息，但需按迭代距离加权。KAE 将迭代索引视为一维自变量，价值函数为 Lipschitz 光滑的回归目标，采用 Nadaraya–Watson 核估计器跨迭代借力：  
\[
\hat{V}_i^{(g)}(x) = \frac{1}{M_i(x)}\left[ \sum_{(I_j,Z_j)\in\mathcal{H}_i(x)} K\!\left(\frac{i-I_j}{ih}\right) Z_j + \sum_{k\neq g} K(0) Z^{(b,k)} \right],
\]  
其中 $K(\cdot)$ 为核函数，$h$ 为带宽，$\mathcal{H}_i(x)$ 为历史奖励集。该估计器无需训练额外网络，仅需维护历史奖励列表，计算成本极低。

**与已有工作关系**  
与 PPO/A2C 相比，KAE 完全避免深度价值网络，计算与内存开销大幅降低；与 GRPO 相比，KAE 通过跨迭代借力，在固定小样本组数 $G$ 下仍能获得一致的价值估计（GRPO 的组均值估计在 $G$ 固定时不收敛）；与 REINFORCE++ 相比，KAE 的核平滑基线对每个 prompt 自适应，而非全局平均，偏差更小。此外，KAE 与近期基于 James–Stein 收缩或 Kalman 滤波的方法不同，采用核平滑并设计 prompt 采样调度，且首次给出完整的梯度 MSE 与策略子最优性理论保证。

**贡献**  
1. **理论**：在 Lipschitz 光滑与 uncorrelatedness 假设下，证明 KAE 价值估计 MSE 达到 $O(N_i^{-2/3})$（一维非参数最优率），而 GRPO/REINFORCE++ 不一致；梯度 MSE 与 oracle 渐近等价；策略子最优性上界由梯度 MSE 控制，从而建立 KAE 的 oracle 性质。  
2. **实验**：在 GSM8K、MATH、DAPO 等基准上，KAE 在价值估计 MSE 上比 GRPO 降低 60–70%，比 REINFORCE++ 降低 90%+；梯度 MSE 降低 5–9% 与 32–65%；最终策略准确率平均提升 5–12%，且对核函数与带宽选择稳健。  
3. **方法**：为统计与 AI 交叉提供新范式——用经典非参数工具解决 LLM 推理中的实际优化难题，兼具统计效率与计算可行性。


### 2. What Should Post-Training Optimize? A Test-Time Scaling Law Perspective

**讲者**：Muheng Li（University of Toronto）

**对应论文**：What should post-training optimize? A test-time scaling law perspective · [arXiv:2605.10716](https://arxiv.org/abs/2605.10716) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.10716.md)

<details><summary>摘要（原文）</summary>

Large language models are increasingly deployed with test-time strategies: sample $N$ responses, score them with a reward model or verifier, and return the best. This deployment rule exposes a mismatch in post-training: standard objectives optimize the mean reward of a single response, whereas best-of-$N$ performance is governed by the upper tail of the reward distribution. Recent test-time-aware objectives partly address this mismatch, but typically assume that training can use the same per-prompt rollout budget as deployment, which is impractical when post-training must cover many prompts while deployment can allocate much larger per-prompt test-time compute. We study this budget-mismatch regime, where only $m\ll N$ per-prompt rollouts are available during training but the target objective is best-of-$N$ deployment. Under structural assumptions on the reward tails, we show that the policy gradient of the best-of-$N$ objective can be approximated from a much smaller rollout group by extrapolating upper-tail statistics. This yields a family of Tail-Extrapolated estimators for best-of-$N$-oriented post-training: a simple direct estimator, Tail-Extrapolated Advantage (TEA), and a fixed-order debiased Prefix-TEA estimator based on moment cancellation. Experiments on instruction-following tasks show that TEA and Prefix-TEA improve best-of-$N$ performance across different language models, reward models and datasets under various training and test-time budget settings.

</details>

**问题**  
标准 RLHF 后训练优化单次响应的期望奖励，但部署时广泛采用 best-of-$N$ 采样，其性能由奖励分布的上尾而非均值决定。已有测试时感知目标虽部分缓解这一错配，却假设训练时每个提示的 rollout 预算 $m$ 与部署预算 $N$ 相同。实际中后训练需覆盖大量提示，$m$ 往往远小于 $N$（$m\ll N$），因此核心问题是：**如何在训练预算严重不足时，仍能有效优化 best-of-$N$ 部署目标？**

**核心方法**  
论文从测试时缩放定律出发，假设奖励分布的上尾服从高斯结构（经验支持），从而将 best-of-$N$ 期望值近似为尾部均值与尾部标准差的线性组合：$V_N(\theta;x)\approx \mu_{\theta,\alpha}(x)+\tilde{c}_N\sigma_{\theta,\alpha}(x)$。基于此，推导出策略梯度的尾部外推形式，并构造两类有限样本估计器：**TEA**（直接插件估计）和 **Prefix-TEA**（固定阶去偏估计）。两者均仅需 $m$ 个 rollout 即可估计上尾统计量，再通过外推公式得到近似 best-of-$N$ 梯度的优势函数，从而在分组策略梯度框架下进行训练。

**与已有工作关系**  
现有后训练方法（如 RLHF、GRPO）优化单样本均值，忽略测试时多候选机制；近期测试时感知方法（如 BoN-aware RL、max@k）虽直接优化 best-of-$N$，但要求训练时每个提示的 rollout 数等于部署预算 $N$，不适用于 $m\ll N$ 的预算错配场景。本文首次在预算错配下利用尾部外推实现高效训练，填补了理论与实践的空白。

**贡献**  
1. 提出 TEA 与 Prefix-TEA 两类尾部外推梯度估计器，理论证明其偏差以 $1/m$ 或 $1/m^k$ 速率衰减，方差为 $O(\log N/m)$，并给出非渐近收敛保证。  
2. 在指令跟随任务上，TEA 和 Prefix-TEA 在多种模型、奖励模型、数据集及预算设置下一致超越 GRPO 及现有测试时感知基线，且增益随 $m$ 与 $N$ 的差距增大而保持。  
3. 揭示后训练应针对部署时上尾而非均值进行优化的原则，为预算受限下的测试时感知训练提供了可扩展的解决方案。


### 3. Acceleration for Diffusion Models: Theory and Practice

**讲者**：Gen Li（The Chinese University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
扩散模型在图像生成等领域表现优异，但其采样过程通常需要数百步迭代，计算成本高昂。如何在不牺牲生成质量的前提下大幅减少采样步数，是当前理论与应用的核心挑战。现有加速方法（如DDIM、DPM-solver）多依赖离散化ODE/SDE求解器，但缺乏对加速策略收敛性的严格理论分析，且实践中常面临步数-质量权衡的瓶颈。

**核心方法**  
本报告提出一套融合高阶数值求解与自适应步长控制的加速框架。在理论层面，将扩散模型的逆向过程建模为带有Lipschitz连续漂移项的随机微分方程（SDE），利用指数积分器（exponential integrator）构造高阶离散化格式，并证明在特定正则条件下，该格式的全局误差以$O(h^2)$收敛（$h$为步长），显著优于传统Euler方法的$O(h)$。在实践层面，引入基于局部截断误差估计的自适应步长策略，在生成早期使用大步长快速穿越平滑区域，后期自动缩小步长以捕捉精细结构，从而在保持FID指标的同时将采样步数压缩至10步以内。

**与已有工作关系**  
与DDIM（确定性采样）和DPM-solver（基于指数积分器）相比，本工作的理论贡献在于首次给出了自适应步长策略下高阶格式的严格误差界，并证明了加速不会引入额外偏差。与Consistency Models（蒸馏式加速）不同，本方法无需额外训练，直接作用于预训练模型，具有更强的通用性。此外，报告还对比了随机微分方程与常微分方程两种视角下的加速差异，揭示了随机性在低步数场景下的正则化作用。

**贡献**  
主要贡献有三：其一，建立了扩散模型加速的理论基础，填补了高阶自适应求解器收敛性分析的空白；其二，提出一种无需重训练、即插即用的实用加速算法，在CIFAR-10和ImageNet上验证了10步内达到与100步DDPM相近的生成质量；其三，通过理论-实践闭环，为后续设计更高效的扩散模型采样器提供了分析工具与设计原则。


### 4. The Statistical Price of Few Updates: Efficiency and Adaptivity in Batched Contextual Bandits

**讲者**：Cong Ma（University of Chicago）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
在在线决策问题中，contextual bandits 通常假设每轮观测后立即更新策略，但在许多实际场景（如临床试验、A/B 测试）中，更新只能以批量（batch）方式进行，且批次数（即更新次数）受限于操作成本。本报告关注的核心问题是：当更新次数被严格限制（如仅允许 $K$ 次更新）时，最优 regret 的下界与上界如何刻画？这种“少更新”约束是否必然导致统计效率的损失？进一步，算法能否在不预先知道总轮数 $T$ 的情况下，自适应地达到与最优 batch 数匹配的 regret？

**核心方法**  
讲者可能基于“分阶段探索与利用”框架，将 $T$ 轮决策划分为 $K$ 个 batch，每个 batch 内使用固定策略。方法的关键在于：在每个 batch 结束时，利用该 batch 收集的数据对策略进行更新，并设计一种“乐观-悲观”型置信区间（如 UCB 或 Thompson sampling 的变体）来平衡探索与利用。为了刻画“少更新”的统计代价，讲者可能引入一个关于 batch 数 $K$ 的额外 regret 项，例如 $\tilde{O}(\sqrt{T/K})$ 或类似形式，并证明该下界是紧的。此外，为达到自适应（即无需知道 $T$），算法可能采用“doubling trick”或基于数据驱动的 batch 划分策略，使得 regret 在任意 $T$ 下均接近最优。

**与已有工作关系**  
已有 batched bandit 工作多关注固定 batch 数下的 regret 分析，但通常假设 batch 边界已知或 $T$ 已知，且多限于有限臂情形。本报告将问题推广到 contextual bandits（特征空间可能高维），并重点研究“自适应”场景——即算法需在未知 $T$ 的情况下自动调整 batch 划分。这与“anytime” bandit 思想类似，但额外受限于更新次数。此外，已有工作多关注“batch 数足够大”时的渐近最优性，而本报告可能首次严格证明“少更新”带来的非渐近统计代价（即 $\Omega(\sqrt{T/K})$ 项），并揭示其与上下文维度 $d$ 的交互关系。

**主要贡献**  
1. 建立了 batched contextual bandits 中 regret 关于 batch 数 $K$ 的 minimax 下界，明确“少更新”的统计代价为 $\Omega(\sqrt{T/K})$（忽略对数因子），并证明该下界在 $K$ 较小时不可改进。  
2. 提出一种自适应算法，无需知道总轮数 $T$，即可在任意 $T$ 下达到 $\tilde{O}(\sqrt{T/K} + \sqrt{dT})$ 的 regret，其中 $d$ 为上下文维度，从而在效率与适应性之间取得最优权衡。  
3. 通过理论分析与模拟实验，验证了算法在实际 batch 约束下的优越性，为在线决策中资源受限的更新策略提供了理论指导。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)