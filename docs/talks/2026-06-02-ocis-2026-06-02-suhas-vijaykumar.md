# Demonstration Experiments

**讲者**: Suhas Vijaykumar  
**讨论人**: Aurélien Bibaut  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2026-06-02  
**主题**: 因果推断  
**视频**: <https://youtu.be/iEd5f1jARBk> · [幻灯片](https://drive.google.com/file/d/1Nij0j0A_3hP_Sjs8gW2Da7lFr1qFyQl8/view?usp=sharing)

> **官方摘要**：Adaptive experiments are used extensively in online platforms, healthcare and biotechnology, and the social sciences. Often, the primary goal is not to precisely estimate a treatment effect but to demonstrate that at least one candidate intervention yields a positive effect, for some subpopulation and on some measured outcome. We formalize this objective as testing the global null in a threshold bandit framework, and develop two inference procedures that are valid under general adaptive sampling: one that pools information across promising arms, and one based on time-uniform multiple testing of individual arm means. To support the latter, we establish a moderate-deviations principle for the sequential t-statistic, justifying asymptotic confidence sequences in settings where the number of arms is large relative to the sample size. To illustrate how adaptive designs can target the proposed statistics, we recast experimental design as bandit optimization with an arm's reward given by its signal-to-noise ratio, and analyze an allocation rule for which we establish a logarithmic regret bound. We apply the methods in a simulation study of targeting unconditional cash transfer programs. Joint work with Guido Imbens, Lorenzo Masoero, Alexander Rakhlin and Thomas Richardson.

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2603.06941](https://arxiv.org/abs/2603.06941) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

**子方向**：自适应实验（adaptive experiment）中的**统计推断**问题。该领域的核心追问是：在数据由适应性算法（如 bandit）采集而非固定随机化设计产生时，如何对处理效应进行有效且保证频率性质的推断？

- **奠基与主流路线**：经典工作确立了自适应采样会引入选择性偏差，导致 naive 的样本均值或 t 统计量失效。两条主流解决路径是：
    1.  **限制采样规则**（“smooth” propensity，如 IPW），代表性工作如 Khamaru et al. (2025, AoS) 证明了在对抗性对比下，此为避开偏差的必要代价。
    2.  **时间均匀推断 / e 值** (game-theoretic statistics)，如 Howard et al. (2021), Waudby-Smith et al. (2024), Ramdas et al. (2023)。此路径提供非渐近的有效检验（e-process / process），代价通常是保守性或对分布/矩的额外假设。

- **当前 frontier**：近年来，研究更关注在**最小化采样规则限制**的同时获得精确（sharp）的推断，或者处理**高维**（臂数多）情形下的自适应采样压力。

**这场报告的位置**：

- **问题设定——阈值多臂老虎机（Threshold Bandit）**：报告将目标重定义为“检验是否存在至少一个臂的均值优于一个已知阈值”。这被命名为 **“Demonstration”（演示）** 问题，并与常见的“Best-Arm Identification”（最佳臂识别/BAI）问题明确区分。
- **核心论点是凸的对立面的易处理性**：报告指出，Demonstration null（所有均值≤0）的补集是一个**凸的**（convex orthant），而 BAI 的 null 是**非凸的**（union of half-spaces）。从经典的假设检验理论（Lehmann & Romano, Ch.4; Berger, 1982; Berger & Hsu, 1996）看，凸 null 的检验在几何上就是更容易的，即使在没有自适应干扰的 i.i.d. 环境下也是如此。这为“为什么可以实现几乎无限制的自适应采样下的精确推断”提供了底层论证。
- **提供的方案**：报告提出了两种推断程序——**Pooled 检验**（聚合证据，sharp）和 **Max 检验**（逐臂检验，可识别具体臂，适度保守）。针对 Max 检验，报告采用 **KMT 耦合 + 中偏差原理 (MDP)** 来处理臂数增长带来的技术挑战，这是一项对经典理论（Borovkov, 1960s-70s）的现代应用。
- **与“计算约束统计”的关联**：用户兴趣点之一。报告不研究计算复杂度（不知道哪个问题是多时间不可解），其核心是**统计效率**而非计算约束。报告中设计实验者的策略时提出的 SN-UCB 算法可以被看作一个经典的多臂老虎机（Bandit）问题，其目标是最大化信号-噪声比（SNR）的累积（伪遗憾 bound），而不是经典的均值。这一点与用户常规的“计算-信息鸿沟”问题有本质不同，subfield 上仍有距离。

### 二、最小内核 / 一个最简例子

**符号与模型**：

1.  **可观测数据**：在时刻 \( t = 1, \dots, T \)，实验者选择臂 \( A_t \in \{1, \dots, K\} \)，观测到收益 \( Y_t \)。
2.  **潜在变量/结构**：假设存在每个臂的潜在结果序列 \( (Y_t(1), \dots, Y_t(K)) \)，其中 \( Y_t \) 是 \( Y_t(A_t) \) 的观测值。向量 \( (Y_t(1), \dots, Y_t(K)) \) 在时间上是 i.i.d. 的。
3.  **参数 vs. 随机变量**：
    -   \( \mu_k = \mathbb{E}[Y_t(k)] \)：臂 \( k \) 的期望（**待估/检验参数**）。
    -   \( \sigma_k^2 = \text{Var}(Y_t(k)) \)：臂 \( k \) 的方差（**非参数干扰参数**）。
    -   \( N_k(T) \)：到时刻 \( T \) 为止臂 \( k \) 被选中的次数（**随机变量**，取决于自适应的选择策略）。
    -   \( \theta_k = \mu_k / \sigma_k \)：臂 \( k \) 的**信号-噪声比 (SNR)**，是驱动统计量漂移的核心量。
4.  **目标：检验全局零假设（Demonstration Null）**：
    \[
    H_0: \mu_k \le 0 \quad \forall k \in \{1, \dots, K\}
    \]
    备择是至少存在一个臂 \( \mu_k > 0 \)。

**最简特例（d=1, K=2 臂）**：

-   **设定**：有两个臂（\( K=2 \)），两臂独立且有未知的均值 \( \mu_1, \mu_2 \) 和已知方差 \( \sigma_1^2 = \sigma_2^2 = 1 \)（为简化）。
-   **数据**：在第 \( t \) 轮，实验者根据某个规则挑选臂 \( A_t \)，观测回报 \( Y_t \)。
-   **Pooled Statistic（简化版）**：
    报告的核心思想是构造一个标准化累积和：
    \[
    S_T = \sum_{t=1}^{T} \frac{Y_t}{\hat{\sigma}_{A_t}(t)}
    \]
    其中 \( \hat{\sigma}_{A_t}(t) \) 是某个基于历史的方差估计。在最简情况下（方差已知为1），这就是简单的 \( S_T = \sum_{t=1}^{T} Y_t \)。
    -   **思想**：由于 \( H_0 \) 要求 \( \mu_1, \mu_2 \le 0 \)，\( S_T \) 在零假设下每一步的期望都是非正的。它形成了一个上鞅（supermartingale），并且在参数化零假设 \( \mu_1 = 0, \mu_2 = 0 \)（sharp null）下，它是鞅（martingale）。因此，利用 Martingale CLT，在 \( T \to \infty \) 时 \( S_T \) 依分布收敛于标准正态分布。检验很简单：做单边检验，当 \( S_T > z_{1-\alpha} \) 时拒绝 \( H_0 \)。
-   **为何能绕过自适应**：任意自适应选择 \( A_t \) 只会影响在 \( S_T \) 中累加哪个 \( Y_t \)，但每一步的“条件方差”始终为1（因为我们已知方差），而**每一步的“条件均值”始终为 \( \mu_{A_t} \le 0 \)**。这保证了鞅结构。自适应带来的潜在偏差不会破坏零假设下鞅的正确定位。
-   **Pooled vs. Max**：如果我们怀疑“只有臂2是好的”，即希望识别出好臂，我们需要对**每个**臂做检验。最直接的是 arm-wise t 统计量：
    \[
    \bar{Y}_k(N_k) / \hat{\sigma}_k  \quad \text{(基于该臂 N_k 个样本)}
    \]
    但 \( N_k(T) \) 是随机且依赖自适应选择历史的，要得到一个在任意停止时间都有效的 p 值需要付出“时间均匀性”的代价（Max 检验的核心逻辑）。

### 三、报告主体：讲者讲了什么

**[0:46-0:57]** **开场与动机**：介绍问题背景——众多网页变体测试，大多无效果，实验昂贵。**核心问题**：如何用有限的实验资源高效判断*是否存在*一个有效的变体（Demonstration），而不是精确估计其效果（estimation）或找出最优（Best-Arm）。

**[1:30-2:04]** **核心想法 1：Game-Theoretic Statistics**：实验者（试图收集证据）与分析者（控制假阳性）的博弈。报告提供的是：
> 对分析者（统计学家）的策略：**Robust Test Statistic**（在自适应下仍有 type-I error 控制）。
> 对实验者的策略：**Optimal Experimental Design**（最大化统计量的功效）。

**[2:08-2:38]** **核心想法 2：Demonstration vs. Exhibition (Best-Arm)**：
- **凸 vs. 非凸 null**：这里讲者展示了两个三臂均值的对比：Demonstration null 是“negative orthant”（凸集），BAI null 是“union of half-spaces”（非凸）。这是几何上的核心差异。
- **证书数量**：Demonstration 只需要**一个**证书（某个臂/组合），BAI 需要 **(K-1)** 个证书（证明臂1优于所有其他）。这解释了为何演示可以更高效。
- **结果**：可以构建一个全局联合检验（pooled test），其在几乎任意自适应下都**sharp**（size exactly α），以及一个针对每个臂的时间均匀多重检验（max test），以鉴定好臂。
- **[2:38-3:16]** **与 BAI 的关键对比**：在 BAI 中，文献表明对任意自适应采样，要么限制采样规则，要么承受一个不可避免的渐近方差膨胀（citing Khamaru et al. AoS 2025）。报告论证：在 Demonstration null 下这个膨胀消失了。
- **[3:16-4:02]** **原因**：再次强调几何特性（凸性与单一方向）。

**[4:02-5:37]** **Pooled Statistic**：
- **定义（infeasible）**：\( Z_T = \sum_{t=1}^T \frac{Y_t}{\sigma_{A_t}} \)。备注：这是一步滞后于标准化的“运行和”。
- **性质**：在 \( H_0 \)（尤其是 sharp null）下，\( Z_T \) 是一个具有单位二次变差（quadratic variation pinned at T）的上鞅，因此 \( Z_T / \sqrt{T} \) 渐近标准正态。在备择下，其漂移项是 \( \sum_{k} \frac{N_k(t)}{T} \cdot \frac{\mu_k}{\sigma_k} \)，即**加权平均 SNR**。
- **Feasible 版本**：用可估的 \( \hat{\sigma}_k \) 替代 \( \sigma_k \)。为了防止低样本的臂因方差估计过小而导致 inflate 统计量，引入一个**padding（填充）正则化**，即在 \( \hat{\sigma}_k \) 上加一个量 \( \sqrt{ \frac{\log(KT)}{N_k(t)} } \)，使其从下方被控制。
- **Main Result**（Berry–Esséen bound）：中心化的可行统计量以 \( O\big( \frac{K \cdot \log^{1/2}(KT)}{\sqrt{T}} \big) + o(1) \) 的速度收敛到标准正态。这意味着只要 \( K \) 的增长速度慢于 \( \sqrt{T} \)，检验就 valid。
- **Proof Sketch**：将求和拆成“well-sampled”（\( N_k \) 大，\( \hat{\sigma}_k \) 好估计）和“under-sampled”（\( N_k \) 小）两类臂。对于后者，padding 保证了其标准差被 bound 在一个量级上，而权重（\( \frac{N_k}{T} \)）也小，所以合并后的贡献可控。关键：不需要精确估计每一个臂。

**[5:37-8:08]** **Max Test**：
- **动机**：Pooled 检验的弱点：1) 不能进行早期停止（不能任意思考何时停止）；2) 只能回答“是否有好臂”，但不能指出**是哪个**。而且如果只有一个好臂，Pooled 会稀释它（将它与噪声臂平均），而 Max 只关注那个最强的臂，因此在强信号下可能更高效。
- **方法**：对每个臂维护一个**Arm-wise Sequential t-statistic**，使用臂自己的“时钟”（第 q 次被抽中的样本，而不是总时间的 wall-clock）。
- **关键技巧：时间均匀性**：因为自适应选择只影响我们从臂的完全路径中“看到”的点（\( N_k(T) \)），而不是路径本身。如果我们将抽样过程视为在**整个完全的潜在路径**（包含未被抽中的后缀/反事实）上做推断，则自适应问题消失。做法是用一个**边界（boundary）** 同时覆盖所有时刻（包括未观测到的），进行时间均匀假设检验。
- **边界**：使用了经典的 Robbins–Siegmund (1970) 边界（线性和对数/弯曲两类）。Burden式边界将所有路径一起检验，从而消去了随机 \( N_k(T) \) 带来的依赖。
- **技术挑战：臂数 K 增长**：常用的逐点 Kolmogorov 逼近（\( O(1/\sqrt{N}) \) 的加法误差）在多重检验中（Bonferroni 校正至 \( \alpha/K \)）会被 K 放大。需要**乘法（multiplicative）精度**，即要求误差是 \( 1/\sqrt{N} \) 的相对误差，而不是加法误差。
- **解决方案**：利用 KMT 耦合（Komlós–Major–Tusnády 逼近，给出 \( O(\log N / \sqrt{N}) \) 的逼近速度）并发展了一个**Sequential t-statistic 的中偏差原理（MDP）**，从而获得对尾部概率的乘性控制。这是论文的一个核心技术贡献。
- **Result**：这样的 Max 检验，在 Bonferroni 校正（将 \( \alpha \) 分配到每个臂和每笔时间上）下，可以控制 type-I error。代价是略微保守，且“无法避免”地要为一个几乎无法避免的多重比较支付 cost。
- **[8:08-8:38]** **与 e-process 方法的联系（讨论者 Bibaut 的评论）**：
    -   Bibaut 将报告的工作置于三种方法的对比中：**a) 鞅/池化方法**（报告的核心，sharp 但限时）；**b) 时间均匀 e-process**（Sandoval, Waudby-Smith & Jordan 2026, 非渐近，exact）；**c) 牛顿/QLIS**（报告没细讲，有提及 Bibaut-Kallus-Lindon）。
    -   **Simplification**：在方差已知情况下，池化的 e-process 就是报告 Pooled stat 的逆过来取 exp，通过 Ville's inequality 得到界。这会在固定视界时 lossy，而用 report 的 CLT 是目前更 tight。
    -   **Bibaut 提出的关键问题**：对于`Exhibition`（发现具体好臂），是否有比 Bonferroni 更好的方法？（类似“needle-in-a-haystack”问题）。这联系到如 Arias-Castro / Candès 等人的 `detection vs. localization` 文献。讨论者提到 Jamieson（等人）关于 `Lil' UCB` 等工作，启发可能通过自适应地跨臂分配阿尔法预算（adaptive α-budget allocation）来支付更少的多重性成本。

**[8:38-9:15]** **实验者策略——SN-UCB 与结论**：
- **核心洞察**：报告的两种统计量的漂移（drift）都是关于**信噪比（SNR = μ/σ）** 的函数，而不是原始的均值。因此，最大化功效等价于**在 SNR 上最小化累积遗憾（Regret）**。
- **算法**：提出 SN-UCB，即用 UCB 算法在**学生化的信噪比估计**上操作，而不是原始回报。它的探索奖励项也用 studentized 尾界的 bound 来校准。
- **理论结果**（Regret Bound）：建立了对数级别的伪遗憾界（\( O(\log T) \)），这等价于“power guarantee”——在替代假设下，检验的功效会与一个了解所有 SNR 值的“上帝”所能达到的极限只差一个对数因子。对于局部（local）备择（SNR 趋近0），bound 仍然成立，但描述其意义时“vacuous”。

**[9:15-10:00]** **模拟证据**：
- **单峰备择（Single-spike）**：只有一个臂有信号。因为在驱动检验的 SN-UCB 中 SNR = μ (σ=1)，它与标准 UCB 等价，但自适应性仍然提升了所有方法的功效。
- **多尺度备择（Multi-scale）**：报告构建了一个例子，最高 SNR 的臂具有极小的方差，而高均值的臂有大方差。SN-UCB 明确优于 UCB 或 UCB-V（针对方差），因为它追踪的是 SNR。这证明**即使已知方差，SN-UCB 也比 UCB 优越**。

**[10:00-End]** **讨论与开放问题**：
- **Multi-dimensional arms / Non-Gaussian 极限**：观众提问。报告者回答：“Pooled test 在多维情况下不确定如何操作”；“布朗极限适用广泛”。
- **Exhibition 层面自适应 α 预算**：讨论者 Bibaut 再次强调这是开放方向。
- **时间的作用**：时间越多证据越多，但 Max test 中 α 需要同时在时间和臂之间分配，值得玩味。

### 四、对应论文与开放问题

**对应论文**：
- **主论文**：
    - **标题**：*Demonstration Experiments*
    - **arXiv 或预印本**：**arXiv 2603.06941**（已在用户提供材料中确认，信息来源权威，此为准确 arXiv ID）
    - **作者**：Guido Imbens, Lorenzo Masoero, Alexander Rakhlin, Thomas S. Richardson, **Suhas Vijaykumar**（讲者本人）。
    - **状态**：疑似提交/待发表（报告时间为 2026 年），具体出版信息未在材料中提及。
- **紧密相关文献**：
    - **Sandoval, Waudby-Smith & Jordan (2026)**：[**SPRUCE**] 研究非渐近 e-process 版 Demonstration null 检验，与报告工作互补。
    - **Khamaru et al. (2025, AoS)**：在 Bandit 问题中证明了自适应推断逼不可避免的成本。

**报告留下的开放问题（每条扎根于转写/幻灯片）**：

1.  **Exhibition 的索引难题（对 Max 检验的关键扩展）**：
    - **出处**：讨论者 Bibaut 的大量评论及讲者的回应（[9:50-10:10] 讨论环节）。
    - **问题**：如何**避免为多重性（K 个臂）支付固定代价**（如 Bonferroni），实现**自适应 α 预算分配**在**Exhibition**任务中。报告承认 Pooled 自动做到了这一点（在计算统计量时 weight 跟着证据走），但 Max 检验目前还是静态分配盘（equal α/arm）。
    - **扎根证据**：讲者最后在讨论中说“...我只有和您谈过才意识到这问题有多有趣... Sandoval 的论文中提到了自适应 α 预算... 如何映射回这个高斯实验...”。

2.  **早期停止与最优停止规则**：
    - **出处**：讲者在介绍 Max 检验优势时提到（[5:37-6:20]）。
    - **问题**：Max 检验允许“peek and stop”（任何时间停止并拒绝），但其代价（time-uniformity tax）导致了保守性。是否存在**最优的、能最小化该税的训练停止规则**，或者是否存在一种**适应性更强的规则**，在高信号臂上花费更多 α，弱信号臂上花费更少？这个问题更偏向于“adaptive spending”的微观结构。

3.  **针对“局部备择”的功率保证**：
    - **出处**：讲者在 SN-UCB Regret bound 后明确说（[8:38-9:15]）“The log(KT) in the bound makes it vacuous when SNR ~ O(1/sqrt(T)) — characterizing power against local alternatives is open.”
    - **问题**：在局部备择（local alternatives，即 μ_k ~ 1/sqrt(T)）情境下，SN-UCB 的 regret 对数界失效，从而导致检验功效无保障。需要发展新的分析或算法来处理这种局部参数化。

4.  **含异质性方差的池化检验**：
    - **出处**：观众提问（[10:00-10:15]）：“could the arms have different dimensions?” 讲者回答：“In the pool testing approach, I'm not entirely sure how I would implement it...”。
    - **问题**：对于**异质性臂维度**（即 arms may be vectors or have different structures），如何扩展 Pooled 检验？讲者不确定，这可能是一个方法论空白。

5.  **时间分配优化的探究**：
    - **出处**：结尾 Q&A（[10:15-10:25]）：“What's the role of time... does longer time complicate anything?” 讲者提到：“...有趣的是... 在 Max 检验中，你既要跨臂又要跨时分配 α... 不同边界（线性的 vs 对数的）有不同的分配模式...”。
    - **问题**：如何**联合优化跨时间和跨臂的 α 分配**，得到对特定替代假设（如早期交替 vs. 晚期交替）最优的检验边界？这是一个自适应实验设计的更优优化问题。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

