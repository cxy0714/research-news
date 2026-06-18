# Synthetic Controls for Experimental Design

**讲者**: Alberto Abadie  
**讨论人**: Dmitry Arkhangelsky  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2025-03-18  
**主题**: 因果推断  
**视频**: <https://youtu.be/FeS9a_USwqA> · [幻灯片](https://economics.mit.edu/sites/default/files/2023-12/Synthetic%20Controls%20for%20Experimental%20Design.pdf)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

**方向：将合成控制（Synthetic Control, SC）方法从观察性研究拓展到实验设计。** 这条工作线直接回答一个实践中的核心矛盾：当干预必须在聚合层面（如城市、市场、地区）部署时，随机化实验（如个体层次的A/B测试）往往不可行或无效，而仅仅随机化少数几个聚合单元又会造成“垃圾设计”（treated unit 与 control units 在特征上严重不匹配）。

**标准 SC 的故事**（Abadie, Diamond & Hainmueller 2010, 2014; 以及大量后续工作）：给定一个受干预的单元（如加州、巴斯克地区）和一个不受干预的 donor pool，SC 通过求解权重使得 pre-treatment 结果与协变量的加权组合逼近 treated unit 的 pre-treatment 轨迹，然后用该加权组合作为反事实估计干预效果。这里 treated unit 是“给定的”——讲者不能选择谁被处理。

**这场报告在追问**：如果实验者可以自由选择哪些单元被处理、哪些作为 donor，那么我们应该如何选择？这变成了一个**设计问题**，而非估计问题。核心在于：(1) 选择一个 synthetic treated unit (由带权重 w 的 unit 构成) 使其特征代表总体；(2) 选择一个 synthetic control unit (由带权重 v 的单元构成) 使其特征匹配 synthetic treated unit 的反事实。wr 和 v 是非负、和为1、每个单元只能属于其中一个。目标是在预算约束（最多只能处理 n̄ 个单元）下最小化估计偏差。

**本研究的定位**：它不是在已有的 SC 估计方法上修修补补，而是提出了一个新的问题框架——**SC 式的设计选择**。该方法在工业界已有广泛应用（如 Uber、DoorDash 的聚合层实验），但学术文献还很少。报告提及的关键前序工作：(a) De & co-authors 的“Synthetic Controls for Experimental Design”类论文（讲者名字听不清，待核实）; (b) Chamberlain (2017, 2020?) 或类似 Uber 的内部方法（“Johann & Barrow from Uber”，名字不确定）。报告本身来自 Abadie 与 Jinglong Zhao（正在线嘉宾）合作的工作论文。

### 二、最小内核 / 一个最简例子

**数据设定**：一个面板，有 J 个单元 (j=1,…,J)，观测时段 t=1,…,T。实验者站在 T0 时刻（实验前），拥有 T0 个 pre-intervention 时段。实验将在之后 T1 个时段展开（整个 T1 期所有被选为 treated 的单元都受干预）。即：所有 pre-intervention 数据可用，实验是“全时段端到端”的（而非随时间推出）。

**模型与符号**：
- 潜在结果：Y_{jt}(0) = 如果没有干预的潜在结果；Y_{jt}(1) = 如果有干预。
- 观测结果：Y_{jt} = W_j·Y_{jt}(1) + (1-W_j)·Y_{jt}(0)，其中 W_j ∈ {0,1} 是实验阶段的处理分配（固定整个 T1 期）。
- 目标 estimand：平均处理效应 ATT（population average treatment effect），
    θ = 1/J Σ_j (1/T1) Σ_{t=T0+1}^{T0+T1} [Y_{jt}(1) - Y_{jt}(0)]，
  其中总体权重可以是均匀的（f_j=1/J）或与城市人口/市场规模成正比。

**合成控制设计中的核心结构**：实验者选择两组权重 w = (w_1,…,w_J) 和 v = (v_1,…,v_J)，均非负且和为1，且每个 j 只能使 w_j>0 或者 v_j>0（不能同时>0）。解释：
- w_j > 0 的单元被分到 treated 组，组成 synthetic treated unit；
- w_j = 0 的单元组成 donor pool，其中 v_j > 0 的单元贡献给 synthetic control unit。

估计量：在实验结束后，观测到
    Ŷ̄_treated = Σ_j w_j Y_{jt}   (含有干预);
    Ŷ̄_control = Σ_j v_j Y_{jt}   (无干预);
    估计的 ATE_{t} = Ŷ̄_treated - Ŷ̄_control;
    再对 T1 期取平均。

**最简例子（J=3, T0=2 个拟合时段, T1=1 个实验时段, n̄=1）**：
- 3 个城市：A、B、C。只有一个可以接受干预（n̄=1），其余两个是 donor。
- 两个 pre-intervention 时段（t=1,2）作为 fitting periods。
- 实验者要决定哪个城市被处理，以及如何从 donor pool 中构造 synthetic control。
- 例如，若选 A 为 treated（w_A=1, w_B=w_C=0），则 donor pool={B,C}，v 可以取 (v_B=0.6, v_C=0.4)。合成估计量 = Y_{A,post} - (0.6·Y_{B,post} + 0.4·Y_{C,post})。
- 目的是使得设计能代表总体（比如这三个城市的平均特征），并且 synthetic control 的 pre-treatment 轨迹与 A 的反事实接近。

讲了这段核心思想后，报告提出如何通过优化选择 (w,v)：最小化 synthetic treated 与 synthetic control 在 pre-treatment / fitting period 中预测变量的差异，同时保持 synthetic treated 能代表总体（即 Σ_j w_j·X_j ≈ 总体平均 X̄），以及约束预算 (∑ w_j ≤ n̄)。这是该框架的最简可理解版本。

### 三、报告主体：讲者讲了什么

**[0:01:05–0:05:18] 动机例子**：美国一家网约车公司想评估提高司机激励的效果。起初考虑在单个城市内随机分配司机到 treatment/control，但引发公平性（同城不同薪资）和干扰（treated 司机工作更久会抢走 control 司机订单）问题。然后考虑跨城市随机化，将所有城市的一半归为 treatment 一半归为 control，但发现昂贵、难回退、且若城市数量少则统计无效。最终决定只在一两个城市试点，核心问题是**选择哪个/哪些城市作为 treated**。

**[0:05:18–0:06:41]** 随机化在单元很少时可能产生“very defective designs”（treated 与 control 在特征上差异很大）。因此提出**非随机化实验**，用合成控制思想直接去选择 treated 单元与 control 单元以达到平衡。

**[0:08:54–0:12:45] 符号与概念**：
- J 个单元，T0 个 pre-experimental 时段，T1 个 experimental 时段。
- 潜在结果 Y_{jt}(1), Y_{jt}(0)；观测结果 Y_{jt}；处理效应定义为差值。
- 目标 estimand: 加权总体平均处理效应 θ = Σ_j f_j (1/T1) Σ_t [Y_{jt}(1)-Y_{jt}(0)]。权重 f_j 通常是 1/J，也可用人口权重。
- 设计选择 w 和 v（非负、和为1、互斥）。
- 估计量：Ŷ̄_treated(t) – Ŷ̄_control(t)。

**[0:12:45–0:14:35] 设计的理想目标**：
- 理想情况 1+2：synthetic treated 的平均结果=总体 treated 平均；synthetic control 的平均结果=总体 control 平均 → 则估计量直接等于 ATT。
- 备选目标 3（讲者提到的 De 等人论文所用）：synthetic control 匹配 synthetic treated 的未处理反事实 → 得到 ATT on the treated（即 ATET）。
- 实际中只能拟合 predictors（包括 pre-treatment 结果和其他协变量）。

**[0:14:57–0:19:48] 设计选择算法**：
- 定义 fitting periods（T_e 个时段），可以是全部 pre-intervention 时段，但如果保留一部分作为 blank periods 对后续推断有利。
- 构造 predictor 向量（包括 fitting periods 的结果及其他协变量），并计算总体平均 X̄。
- 基本优化问题：选择 (w,v) 使得 Σ_j w_j· X_j ≈ X̄ 且 Σ_j v_j· X_j ≈ X̄，约束 w_j, v_j ≥ 0, Σ w_j = Σ v_j = 1, 且 w_j 与 v_j 不能同时>0。此外，加预算约束 Σ w_j ≤ n̄（最多处理 n̄ 个单元）。
- 性质：问题在 w 与 v 上几乎对称，除预算约束外。因此对称结构会导致最优解中存在互换 W 和 V 的可能性，论文讨论了如何选择。
- 变体：对每个 treated unit 分别拟合 synthetic control（而非统一的一刀切），然后通过一个参数 ξ 调控对总体匹配（population representation）与对 treated unit 单独匹配（ATT vs ATET）之间的权衡。

**[0:19:48–0:20:50]** 聚类想法：在 predictor 空间中对单元聚类，再从每个簇中抽取一个 treated 单元（如三个簇各选一个 treated 代替三个都从同一个簇中选），这样设计更稳健。图示：数据点有清晰三个簇，选 red 点在中间（不合理） vs 每簇一个（合理）。

**[0:20:52–0:24:02] 估计性质（理论分析）**：
- 采用标准因子模型作为潜在结果 DGP（不使用干预时模型的自然延伸，但加上了干预时的表达式）：
    Y_{jt}(0) = δ_t + λ_t'·μ_j + θ_t'·C_j + ε_{jt}
    Y_{jt}(1) = Y_{jt}(0) + τ(D大项，具体未展开)
- 保号：若 synthetic treated 与 synthetic control 都能精确再现 X̄ 和内在因子部分（μ_j），则偏差上界为 O(σ_ε / √T_e)，其中 σ_ε 是噪声的方差代理，T_e 是 fitting periods 数。这一上界来自过拟合效应：如果拟合主要来自噪声而非真实因子 μ，则偏差大。
- 若不精确匹配（有残差），则偏差上界增加一个与拟合误差成正比的分量。

**[0:24:59–0:29:01] 推断方法**：
- 利用 blank periods 的安慰剂效应做检验。基本思路：假设在某些时段（blank periods）无处理效应，则在这些时段得到的估计量（安慰剂）应与实验期的估计量有相同分布（若交换性成立）。通过比较某种检验统计量（如 mean absolute error）来获得 p 值。
- 优点：(1) 即使 λ_t 不满足严格交换性，当 T_e 大时结果仍近似有效；(2) 允许 Y_{jt} 有趋势、季节性（通过 δ_t + θ_t·C_j 部分实现），而以往结果常要求 Y_{jt}(0) 是 i.i.d.。
- 另一种方法：若假设干预不影响个体暂态冲击 ε 的分布，则可用 blank periods 的安慰剂效应分布构造置信区间。

**[0:29:11–0:31:28] 实证示例：Walmart 数据（45个店铺, 143周, 100 fitting + 28 blank + 15 实验期）**：
- 目标是估计零效应（因为并无真实干预）。合成控制设计拟合得很好：synthetic treated 与 synthetic control 在 fitting/blank 期高度吻合，实验期也接近零，p 值大，区间含零。

**[0:31:32–0:35:23] 模拟（15 个单元, 20 fitting + 5 blank + 5 实验期）**：
- 展示一个代表性模拟：在拟合和空白期零效应，在实验期有处理效应，检验能拒绝零假设。
- 转写中提到对比“unconstrained case”（任意 w 与 v 单位数）与“constrained case”（限制只有1/2/3个 treated 单元）。未约束时偏差最小，但即使只有1~3个 treated 单元，表现也“quite well”。
- 零效应假设下的 p 值分布接近均匀。

**[0:35:23–0:37:20] 对比：合成控制设计 vs 随机化 vs 分层（stratification）**：
- 在单元少时，随机化可能导致很差的平衡，而合成控制设计有显著更低的 RMSE。
- 分层在仅有一个 treated unit 时退化为随机化（每个 stratum 至少需要1 treated unit），在多 treated 单元时改进也不明显。
- 事后调整（post-stratification adjustment, regression adjustment）在当前模拟（15 unit, 协变量多）中效果差。

**[0:37:48–0:41:12] 总结评论**：
- 实验≠随机化；实验是干预研究，可以非随机化。
- 当实验单元少、干预在聚合层部署时，随机化可能不是最佳方法。
- 本方法给出一个选择 treated/control 单元的优化框架，适合在 industry A/B tests 和学术情境中有类似约束的研究。

### 四、对应论文与开放问题

**(a) 报告对应的论文：**
- 转写中提到“this is a working paper with Jinglong Zhao”，标题即“Synthetic Controls for Experimental Design”。
- 可搜索：Abadie, Zhao, “Synthetic Controls for Experimental Design”, 2024 或 2025。尚无 arXiv 或正式发表记录（待核实）。
- 讲者及嘉宾还提及一篇相关论文：De & co-authors (名字听不清，可能为 “De Dacon” 或类似) 以及 Chamberlain 等 Uber 内部工作。

**(b) 开放问题（从转写中提取，每条都有时间点）**：
- **[0:35:23-0:37:20]** 当单元数很少（如15个）、协变量多时，事后回归调整的效果差。是否能设计更好的变体（如正则化或降维）以处理高维协变量？
- **[0:41:12-0:43:45] (讨论者提问)** 处理分配 w(·) 直接依赖于过去结果（即过去误差），这与标准 SC 假设（过去误差与 future 独立）冲突。这会导致何种偏差，如何量化？
- **[0:47:48-0:48:33] (讨论者建议)** 是否可以先对面板数据拟合一个参数模型（如线性因子模型），然后从拟合模型仿真大量的 assignment 结果，将得到的平均估计量视为一种“袋装合成控制”？这样可提供实验框架保证，并可能减少离散性带来的波动。
- **[0:48:48-0:49:27] (讲者回应)** 是否可以在合成控制之间结合基于模型的推断（如 parametric bootstrap）与纯设计推断（permutation）？讲者觉得这是一个方向，但尚不清楚收益。
- **[0:49:27-0:50:50] (讨论者建议)** 对不同的 panel 数据模型（如 AR、状态空间模型），对应的设计方法会不同。讲者也认可这一点（如 bar 模型可能更好）。
- **[0:50:52-0:51:12] (讲者结尾)** 推断方法能否在单一手法下适配不同模型，同时避免“researcher degrees of freedom”？

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

