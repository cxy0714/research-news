# Statistical Testing under Distributional Shifts

**讲者**: Niklas Pfister  
**讨论人**: Thomas Berrett  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2021-06-01  
**主题**: 因果推断  
**视频**: <https://youtu.be/ZrIivZDygmo> · [幻灯片](https://drive.google.com/file/d/17VKr_I2OqewBk2W6b1Gn4dHV_QcgPrOs/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2105.10821](https://arxiv.org/abs/2105.10821) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

这场报告位于一个新兴但连接多领域的子方向：**transductive testing under distribution shift**（「迁移假设检验」或「分布偏移下的假设检验」）。它追问的是：当我们对目标分布 P* 有一个 hypothesis (P* ∈ H₀)，但只能观测到来自另一分布 Q* 的 i.i.d. 数据，且已知 P* 与 Q* 通过一个**已知（或可估计）的似然比** r = dP*/dQ* 相联系时，我们能否（以及在什么条件下）利用观测数据对目标 hypothesis 做有 asymptotic level guarantee 的检验？

**这个方向的历史与主流路线**：
- **奠基工作**：重要性抽样（importance sampling）与 Rubin (1987, 1988) 的 sampling/importance resampling (SIR) 为用观测分布模拟目标分布的样本提供了工具。但在**假设检验**语境下使用这种重采样、并证明其 level 与 power 的统计性质，是近期的工作。
- **最直接的先驱与竞争路线**：
  - 对于报告中**条件独立性检验**（conditional independence testing, CIT），两个重要的方法是（尽管它们没有使用分布偏移框架，而是直接在观测分布下利用已知条件分布）：
    - **Candès et al. (2018)** 的 **Conditional Randomization Test (CRT)**（听写中 "Candès et al. 2018" 应指该文，但讲者口误说成 "Candice"）：假设已知 X|Z 的条件分布，通过随机化产生 X 的 null 拷贝来构造 p-value。CRT 是 exact finite-sample level，但需要模拟 null 分布。
    - **Berrett et al. (2020)** 的 **Conditional Permutation Test (CPT)**（本场讨论人 Thomas Berrett 的工作；报告提到 "Tom who's discussing here today" 可佐证）：通过加权排列（weighted permutations）处理已知条件分布下的 CIT。
    - **本报告方法 vs. CRT/CPT**：本方法不是通过随机化 X 或排列来构造 p-value，而是**将观测分布直接重采样（resample）为近似来自目标分布的样本**，再在目标域中应用现成的**无条件检验**。其 tradeoff：点态渐近 level vs. 有限样本 exact level；可以把任何黑箱无条件检验用在重抽样数据上；代价是 m = o(√n) 的重采样规模限制。

- **对于 contextual bandit & invariance learning 路线**：报告引用 Saengkyongam et al. (2021)（arXiv 尚未出号），该工作研究了在 multi-environment bandit 中，当存在 hidden confounding 时，为何只考虑 invariant policy（即环境变量 e ⊥ R | X_S）能有效保障 worst-case reward，**而不需要引入我们这里的 shift-testing 框架**。本报告填补的正是**如何实际检验一个目标 policy 是否为 invariant** 这一问题：其数据来自旧 policy，但 invariance 涉及的是目标 policy，必须做 distribution shift。

**当前 frontier & 本报告站的位置**：
- **本工作是开创性而非终结性的**：它定义了一个相当一般的 shift-testing 框架，但只给出了**点态渐近 level**（不是 uniform、不是 finite-sample）、重采样规模有较严格的约束（m = o(√n)）、且对于 **rq 依赖 q 的情形**（需估计权重）需要额外的一致估计 rate 条件和更小的 m。报告位于「框架 + 首次可行性证明」的 stage，而非「最优条件或更强保证」的 stage。
- **关键未解决 gap**：讨论人 Thomas Berrett 提出——m 能否取更大？对 closeness of P* and Q* 是否应显式建模？能否做 uniform 或 finite-sample 保证？能否做 estimation 而非 testing？这些都是当前 frontier。

**可查的引用提醒**（基于幻灯片结尾及转写）：
- Thams, N., Saengkyongam, S., Pfister, N., Peters, J. (2021). *Statistical Testing under Distributional Shifts*. arXiv:2105.10821.
- Saengkyongam, S., Thams, N., Peters, J., Pfister, N. (2021). *Invariant Policy Learning: A Causal Perspective*. arXiv:no-number-yet (讲者说 soon on arXiv).

---

### 二、最小内核 / 一个最简例子

**符号与设定**：

- **可观测数据**：X₁, …, Xₙ ~ Q* (i.i.d.)，每个 X ∈ 𝒳。
- **目标分布**：P* ∈ 𝒫（定义在 𝒵 上，可能 𝒵 ≠ 𝒳，但在所有例子中 𝒳 = 𝒵？实际在条件独立测试中 𝒳 = 𝒵 = (X, Y, Z)，所以可假设空间一致）。
- **已知映射**：τ: 𝒬 → 𝒫，其中 Q* 是观测的，P* = τ(Q*)。形式为：p(x) = r_q(x) · q(x)，其中 r_q(x) 是权重函数（可依赖于 q，也可不依赖；在「已知 r」情形中 r 不依赖 q 且已知）。
- **要检验的 hypothesis**：H₀ ⊆ 𝒫 是目标域上的原假设。等价地，通过拉回，Q ∈ τ⁻¹(H₀) 就是观测域上的原假设。
- **检验**：我们希望构造 ψₙ: 𝒳ⁿ → {0,1}，使得在观测 Q ∈ τ⁻¹(H₀) 下，limsup_{n→∞} P_Q(ψₙ=1) ≤ α（点态渐近 level）。

**最简特例：二值变量，d=1，一个** **known r** **情形**

- 设 𝒳 = {0,1}。
- 观测分布：Q*(0) = 0.9, Q*(1) = 0.1。
- 目标分布 P*：我们希望它满足 P*(0) = 0.5, P*(1) = 0.5（均匀分布）。所以权重 r(0) = 0.5/0.9 ≈ 0.556, r(1) = 0.5/0.1 = 5。
- H₀ 是「P* 是一个均匀分布」，即 P* ∈ {Uniform{0,1}}。
  - 换言之，观测域的原假设 Q ∈ τ⁻¹(H₀) 包含所有满足 τ(Q) = Uniform 的 Q。此时只要观测 Q 本身对应的权重 r(x)=0.5/Q(x)（即观测 Q 的分布可以与 0.5/0.5 的均匀目标相差任意大），原假设都视为成立。
- 从观测样本 X₁,…,Xₙ 出发，我们想检验 P* 是否是均匀分布。
  - **直接想法**：我们不能直接用 X₁,…,Xₙ 测频率，因为观测分布严重有偏于 0。
  - **方法**：
    1. 从观测样本中，**无需放回地重采样 m 个 distinct 样本**，权重正比于 ∏_{ℓ=1}^{m} r(X_{i_ℓ})（即若 X=1 的数据需被大幅上采样，X=0 的数据被大幅下采样）。这里 m 必须小（o(√n)）。
    2. 这么做之后，这个大小为 m 的重样本「看起来」近似来自 P*。
    3. 然后用一个现成的二项检验（例如 exact binomial test of proportion）来判断在目标域中是否 P*(1)=0.5。
  - **核心直觉**：重采样的权重纠正了观测分布的偏差，但代价是有效样本量大幅缩减（m≪n）。这个 tradeoff 对于 level 保障是充分的——只有当重采样规模足够小（远小于√n）时，权重中的极端方差才不会破坏渐近 level。

---

### 三、报告主体：讲者讲了什么

**[0:04]–[0:12] 引言 & 框架定义**
- 定义了统计测试在分布偏移下的抽象框架：观测域 Q、目标域 P、映射 τ (shift function)，原生假设 H₀ ⊆ 𝒫，通过 τ⁻¹(H₀) 转入观测域。
- 明确 tau 形式为 **p(x) = r_q(x) q(x)**，其中 r_q 是似然比 (dP/dQ)，可依赖于 q。
- 区分两种情形：r_q 不依赖 q (known) vs. 需要估计 r_q 的情况。

**[0:13]–[0:20] 应用之一：多环境上下文 Bandit (RL)**
- 图模型：U (hidden confounder) → X₁, X₂ (observed contexts)；action A 由 policy π 从 X₁,X₂ 生成；Reward R 取决于 A, U, X₂。E（环境）仅影响 X 的边缘分布。
- 核心结果（来自 Saengkyongam et al. 2021）：
  - 无 hidden confounder 时：pooling 所有环境后的最优 policy 就是 maximin optimal（不需要考虑环境结构）。
  - 有 hidden confounder + mean faithfulness + strong environments 时：在 observed environments 中只考虑 invariant policies（即 e ⊥ R | X_S）就能保障 worst-case 目标域 reward。
- 于是问题变为：能否检验一个**目标 policy** ¯π（并非被观测的 π）是否 invariant？即需 shift 观测数据至目标 policy 下的分布。

**[0:20]–[0:30] 应用之二、三：条件独立检验 & 休眠独立 (Verma constraint)**
- **条件独立检验**：观测数据 (X, Y, Z) 来自某 Q，想知道 X ⊥ Y | Z。
  - 已知条件密度 q*(z|x)（或 q*(x|z)）。
  - 通过 shift τ 将 q(z|x) 替换为 φ(z)（任意选择，如边际高斯），那么若原假设 H₀（X ⊥ Y|Z 且条件密度 = q*）成立，则在目标域中 X ⊥ Y（无条件独立）。
  - 从而将复杂的条件独立检验转化为简单的无条件独立检验（可用 HSIC 或线性相关检验）。

- **休眠独立（Verma 约束）**：图 H_G vs H_H（中继节点 X₃ 的系数不同）。当分布来自 H_G 时，满足 X₁ ⊥ X₄ in Q do(X₃ := N)——这是一种 dormant independence。通过 shift 将 q(x₃|x₂) 替换为某个 φ(x₃)（例如 N(0,1)），即在目标域中检验 X₁ ⊥ X₄。

**[0:30]–[0:40] 核心方法：基于重采样的检验**

**Case 1: r 已知 (不依赖 q)**
- 两步程序：
  1. 从 n 个观测中无序不放回地抽取 m 个 distinct 样本，权重 w(i₁,…,iₘ) ∝ ∏_{ℓ=1}^{m} r(X_{i_ℓ})（若序列不重复；重复序列权重置0）。
  2. 将现成的目标域检验 φₘ 应用于此重样本。
- **定理条件 (点态渐近 level)**：
  - A1: φₘ 有点态渐近 level。
  - A2: m = o(√n)。
  - A3: E_Q[r(X_i)²] < ∞。
- 证明 sketch：重样本的生成分布依概率收敛到目标域中大小为 m 的 i.i.d. 样本的分布（由于重采样权重抓住了似然比），收敛速度受限于 n 与 m 的比率；当 m = o(√n) 时，剩余变异不会导致 asymptotically level 膨胀。

**Case 2: r 依赖 q (需估计)**
- 三步程序：
  1. 数据随机二等分；一半用于估计 r̂（例如 q(z|x) 的密度比）。
  2. 在另一半上重采样 m 个 distinct 样本，权重 w ∝ ∏ r̂(X_{i_ℓ})。
  3. 应用现成检验。
- **定理条件**：
  - A0: r̂ 一致相合，满足 lim_n sup_x | (r̂ₙ(x)/r_q(x))^{n^a} - 1 | = 0 （其中 a 为相合幂次，可 very slow）。
  - A1: φₘ 有渐近 level。
  - A2': m = o(min(n^a, √n))。
  - A3': E_Q[r_q(X)²] < ∞。

**[0:40]–[0:46] 回到应用：实验结果**
- **Bandit**：仿真实验展示对不同 subset S 的 invariance 检验。只有 X₂ 是真正 invariant 的，检验在 n → ∞ 时保持 level（接受率接近 0.05），而对非 invariant 的 S 则 power 趋于 1。
- **条件独立检验（模拟）**：检验 X-Y 直接效应 θ（线性/二次）。使用重采样 + 边际检验（CorTest 或 HSIC）与全条件检验（KCI, GCM）对比。重采样方法在 m≈√n 时 power 略低但渐近收敛。
- **休眠独立**：检验 X₁-X₄ 之间的休眠独立性。

**[0:46]–[Q&A] 讨论 (Thomas Berrett) & 回应**
- 讨论人指出：① m 的上界问题；② 能否有 uniform 或 finite-sample 保证；③ 如何处理 P* 与 Q* 有不同 closeness；④ 能否在 shift 框架下使用更多先验信息（如同时知道 q(z|x) 与 q(y|x,z)）；⑤ 能否扩展到估计问题。
- 讲者回应：① m = o(√n) 确实是边界，但对于更简单（如线性）的检验可以取更大 m；② uniform 保证需要额外对权重施加 uniform bound；③ closeness 实际上隐藏在 E[r²] 的 bound 中；④ 同时使用两个条件密度的想法「nice idea, haven't thought about」；⑤ 估计问题可以使用类似 asymptotic convergence 的思路。

**[H:MM] 标注示例**：
- [1:00:14]–[1:00:36]：讨论人提到"m is kind of equivalent to power"。
- [1:00:42]–[1:01:07]：讨论人提问能否利用 P* 与 Q* 的 closeness（未在文中直接呈现，是 open point）。

---

### 四、对应论文与开放问题

#### 对应论文

- **主要论文**（报告对应）：
  - **Thams, N., Saengkyongam, S., Pfister, N., Peters, J. (2021).** *Statistical Testing under Distributional Shifts*. arXiv:2105.10821.
  - 讲者确认这篇已上 arXiv，且全文可查。
- **关联论文（报告中也引用了结果但没有 arXiv 号）**：
  - **Saengkyongam, S., Thams, N., Peters, J., Pfister, N. (2021).** *Invariant Policy Learning: A Causal Perspective*. 讲者说 soon available on arXiv（报告时 no number yet）。本场后半集中于 invariance 的理论结果即源自此工作（prop 与 theorem 关于 maximin optimality of invariant policies）。

#### 开放问题（每一条扎根于转写/讨论中的具体依据）

1. **重采样规模 m 的上界能否放宽？** [讨论人提问，1:00:09–1:00:11] 讲者回应称 m=o(√n) 是保守边界，对线性检验可更大——但**尚未发表显式有限样本条件**。这是一个直接可做的理论问题：针对特定检验（如 t-test、线性相关），可推导出 m 的最大容许增长率与权重矩的关系。
   
2. **从点态渐近 level 到 uniform asymptotic level 所需的额外假设**。 [讨论人提问，1:00:23–1:00:28] 讲者提到加入 uniform boundedness of weights 可实现 uniform control，但未展开。这需要严格化 uniform bound 如何依赖于 weight r 的尾部分布。

3. **如何整合关于两个或多个条件密度的先验知识？** [讨论人提问，1:01:23–1:01:37] 讲者认为这是个好想法但尚未探索。例如在 CIT 中同时知道 q(z|x) 与 q(y|x,z)（或只知其一）如何提高 shift 的准确性或放宽 m 约束？

4. **能否将重采样框架扩展到参数/半参数估计，而非仅限于假设检验？** [讨论人提问，1:01:38–1:02:01] 讲者承认在定理中只证明了 level，但指出类似收敛性可用于估计问题（如 CI construction、point estimation）。这需要发展估计量的渐近正态性与收敛率的理论，在 shift 框架下是全新的。

5. **当 r_q 需估计时，估计误差的精确率对 m 的影响。** [定理条件 A0: 讲者, 0:36:24–0:36:40] 条件 A0 要求 r̂ 一致相合且收敛率幂次 a 需显式满足 m=o(n^a)。对于现实中的非参数估计（如核密度比估计），a 可能很小 → m 极受限。能否通过改进密度比估计（例如使用深度学习方法）来放松这一条件？

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

