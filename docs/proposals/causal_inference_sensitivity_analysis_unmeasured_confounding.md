# 选题提案 · 未测量混杂的敏感性分析

**战线范围**: 通过参数化偏离无混杂假设（如边际敏感性模型、校准敏感性分析、混淆函数），推导ATE或分位数效应的部分识别界（sharp bounds），并构建置信区间。  
**证据论文**: 30 篇（★ 收藏 11 篇）  
**提案条数**: 3  
**生成日期**: 2026-09-01  

> 每条提案的证据都点名来源论文 [k] 并引其原话。**不打分、不排名**——「证据 N 篇」是可数的事实，不是质量分。标了 ⚠️ 单点证据的条目只有一篇论文支撑，自己掂量。

---

### 提案 1：Higher-Order Influence Functions for Local Sensitivity Analysis: Sharpening First-Order Approximations Under Unmeasured Confounding

- **claim（一句话）**：证明在未测量混杂的局部敏感性分析中，一阶泰勒展开的余项可由高阶影响函数（HOIF）的二阶U-统计量显式控制，并给出该余项在Wasserstein扰动半径δ下的minimax上界，从而将现有局部敏感度从一阶导数提升至二阶可计算界。

- **最小内核**：先打单参数、单连续处理、无协变量的最简特例。设处理A连续，结局Y连续，无混杂假设下的目标参数为ATE = E[Y(1) - Y(0)]。在Wasserstein-2扰动下，偏差函数的一阶项为∇ψ·ν，二阶余项为∫∫h(x,y) dν(x)dν(y)（核h为二阶影响函数）。在此特例下，要证的命题退化为：当扰动半径δ→0时，二阶余项的上界为O(δ²)，且该界由核h的Hilbert-Schmidt范数决定，可通过U-统计量一致估计。

- **证据**：
  - [7] 开放问题3：“与高阶影响函数（HOIF）的结合：HOIF估计量涉及高阶U-统计量的渐近展开，其偏差项的控制需要乘子U-过程的bound。本文的乘子不等式能否直接用于HOIF的bootstrap推断？”（扎根：作者在intro中没有引用HOIF文献，但HOIF是U-统计量的自然应用场景。）
  - [19] 开放问题2：“高阶U-统计量 / HOIF 与局部敏感度的关系？本文用一阶∇ψ定价假设，但HOIF理论用二阶余项定价nuisance估计误差的偏差；二者在‘已知π₀的价值’上是否给出一致结论？”（扎根点：Intro提到“classical apparatus falls short in several respects”，但未引用HOIF文献；这是被回避的竞争路线。）

- **为什么现在**：[19] 已建立一阶局部敏感度的闭式解（Proposition 2），并明确将二阶余项列为开放问题（Eq. 7提到“when a functional Taylor expansion holds uniformly over the ball”，但未给出δ的上界条件）。同时，[7] 的乘子U-过程bound（Theorem 2.1）为控制二阶U-统计量的随机波动提供了现成工具，使得将HOIF的偏差分析从理论存在推进到可计算界成为可能。

- **武器匹配**：使用 **高阶U统计量的计算（treewidth / tensor contraction / einsum）** 来显式计算二阶影响函数核h的Hilbert-Schmidt范数。具体地，当处理A和结局Y的联合分布可表示为低树宽图模型时，核h的积分运算可转化为einsum收缩，从而在O(n·tw)时间内完成，避免全张量O(n²)计算。

- **风险与竞争**：
  - 已被做过？需查Robins et al. (2008) 关于HOIF在因果推断中的工作，以及Rothenhäusler & Bühlmann (2023) 关于局部敏感度的二阶展开。若已有类似结果，则选题失效。
  - 假设太强？二阶余项的控制要求核h的Hilbert-Schmidt范数有限，这等价于处理效应曲面的二阶光滑性。若处理效应不光滑（如阶梯函数），二阶项可能发散。
  - 反例存在？当扰动分布ν的支撑集中在核h的奇点附近时，二阶余项可能主导一阶项，导致minimax上界不紧。
  - 算不出来？若图模型树宽随变量数指数增长，einsum收缩不可行。需限制在低树宽结构（如链式、树状）。

- **交付形态**：`定理型`

- **第一周动作**：
  1. 读 [19] Section 2.2，确认一阶局部敏感度的闭式推导细节，特别是∇ψ的显式表达式。
  2. 读 [7] Theorem 2.1及其证明，提取乘子U-过程bound中关于核复杂度（熵积分）的假设，判断是否适用于二阶核h。
  3. 推导单参数、无协变量特例下二阶影响函数核h的解析形式（通过Gateaux导数二阶项）。
  4. 用einsum写出核h的Hilbert-Schmidt范数在n=100模拟数据下的计算代码，验证计算复杂度。
  5. 搜索Robins et al. (2008) 和Rothenhäusler & Bühlmann (2023) 的标题，确认是否已有二阶局部敏感度结果。

---

### 提案 2：Nested Sensitivity Envelopes for Longitudinal Causal Effects with Time-Varying Treatments

- **claim（一句话）**：将嵌套敏感性包络线（nested sensitivity envelopes）从截面分位数处理效应推广至纵向时变处理设定，推导在序贯可忽略性违反下，动态处理策略的累积处理效应（如均值或分位数）的部分识别sharp界，并给出方向可微推断的渐近理论。

- **最小内核**：先打两个时间点（t=1,2）、二值处理、无协变量的最简特例。设A₁, A₂ ∈ {0,1}，结局Y在t=2后观测。序贯可忽略性假设为Y(a₁,a₂) ⊥ A₁ | ∅ 和 Y(a₁,a₂) ⊥ A₂ | A₁, Y。违反由两个灵敏度参数Γ₁, Γ₂刻画（分别对应两个时间点的未测量混杂强度）。在此特例下，要证的命题退化为：累积ATE = E[Y(1,1) - Y(0,0)]的sharp界可由两个嵌套线性规划给出，且当Γ₁=Γ₂=0时退化为点识别。

- **证据**：
  - [13] 开放问题：“纵向/面板数据扩展：当前模型限于截面数据，如何将此嵌套包络线与方向可微推断拓展至纵向因果推断中的动态处理策略是重要方向。”（扎根：作者在Limitations段明确提及。）
  - [10] 开放问题2：“纵向设置下的推广：本文的框架能否推广至具有时变治疗的纵向设置？在纵向设置下，广义策略的识别需要更强的假设（如Young et al., 2014所述），部分识别结果是否还能保持？”（扎根点：Section 5的“extend these methods to handle longitudinal settings”。）

- **为什么现在**：[13] 已为截面QTE建立了嵌套包络线的sharp界和方向可微推断（Theorem 1-3），其技术核心（CDF过程的联合sharp界 + 广义逆映射）在纵向设定下可逐时间点递归应用。[10] 的随机干预框架提供了纵向推广的另一种路径（通过耦合和最优传输），但未解决非光滑分位数推断。两者结合使得纵向推广从“概念可行”变为“技术可操作”。

- **武器匹配**：使用 **非参数统计** 中的方向可微性（Hadamard导数）理论。具体地，将纵向CDF过程的嵌套包络线视为从灵敏度参数(Γ₁,Γ₂)到CDF泛函的映射，利用Hadamard导数链式法则推导累积ATE的渐近分布，避免对每个时间点单独做bootstrap。

- **风险与竞争**：
  - 已被做过？需查Robins et al. (2000) 的G-computation敏感性分析，以及Díaz & van der Laan (2013) 的纵向TMLE。若已有sharp界结果，则选题失效。
  - 假设太强？纵向设定下需要序贯可忽略性在每个时间点被相同结构的灵敏度参数刻画，且灵敏度参数不随时间变化（或变化已知）。若实际中混杂强度随时间变化，模型可能误设。
  - 反例存在？当处理路径数随时间指数增长（2^T），sharp界的线性规划规模爆炸。需限制T较小（如T≤5）或使用动态规划。
  - 算不出来？方向可微推断要求CDF泛函的Hadamard导数存在，但分位数映射在CDF平坦处不可微。需假设CDF严格递增。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [13] Section 2-3，理解嵌套包络线在截面下的构造（特别是CDF界的线性规划形式）。
  2. 读 [10] Section 5，确认作者对纵向推广的conjecture具体内容（哪些假设需要加强）。
  3. 写出两个时间点、二值处理下累积ATE的识别表达式，并推导在序贯可忽略性违反下的偏倚公式。
  4. 用R实现两个时间点的sharp界线性规划（使用lpSolve），在n=500模拟数据下验证界是否随Γ₁,Γ₂单调变化。
  5. 搜索Robins et al. (2000) 和Díaz & van der Laan (2013) 的纵向敏感性分析，确认是否已有sharp界结果。

---

### 提案 3：Confidence Intervals for Sensitivity Intervals: Inference on the Entire Identification Region Under Distributional Uncertainty

- **claim（一句话）**：为公式工具IV和全局敏感性分析中的敏感区间（sensitivity interval）构建具有渐近有效覆盖概率的置信集，该置信集同时覆盖分布不确定性（灵敏度参数）和抽样不确定性，并证明其半参数效率界。

- **最小内核**：先打单工具变量、二值处理、无协变量的最简特例。设Z为二元工具，D为二值处理，Y为连续结局。在公式工具IV设定下，敏感区间为{β: ∃G∈P_m(δ) s.t. β = E[Y·Z]/E[D·Z] under G}，其中P_m(δ)是冲击分布G的边际灵敏度集。在此特例下，要证的命题退化为：构建关于β的置信集C_n，使得liminf P(β_true ∈ C_n) ≥ 1-α，且C_n的直径以速率n^{-1/2}收敛到敏感区间的长度。

- **证据**：
  - [30] 开放问题1：“构建具有有效覆盖概率的统计推断区间：本文构建的只是识别区间，不是置信区间。一个开放问题是：如何对δ和ATE的识别区间进行统计推断？”（扎根：论文Discussion部分指出目前方法只提供点估计区间，而非统计推断。）
  - [4] 开放问题4：“置信区间与假设检验的更新：论文展示了点估计的敏感区间，但标准误是在敏感区间的端点处计算的。一个开放的方法论问题是：如何对整个‘敏感区间’本身进行推断（即构建关于β的置信集，这个集能同时覆盖分布不确定性p和抽样不确定性）？”（扎根：基于“6 结论”部分，只提到了标准误计算在端点，没有给置信区间。）

- **为什么现在**：[4] 已给出敏感区间的线性规划构造（Proposition 1），并指出端点处标准误的计算方法，但未解决整个区间的联合覆盖。[30] 已建立全局敏感性分析的识别区间，但同样缺乏统计推断。两者都停留在“点估计的敏感性”层面，而最近关于部分识别推断的进展（如Imbens & Manski 2004的置信区间、Stoye 2009的修正）为将识别区间转化为置信集提供了现成框架，但尚未应用于敏感区间。

- **武器匹配**：使用 **估计问题的minimax下界** 来刻画置信集的最优收敛速率。具体地，将敏感区间视为一个集合值参数Θ(δ)，其估计的minimax风险由识别区间的长度和抽样误差共同决定。通过推导Θ(δ)的Hausdorff距离下界，证明置信集直径的n^{-1/2}速率是minimax最优的。

- **风险与竞争**：
  - 已被做过？需查Imbens & Manski (2004) 和Stoye (2009) 的部分识别置信区间，以及Armstrong (2022) 关于集合值参数的推断。若已有直接应用于敏感区间的工作，则选题失效。
  - 假设太强？置信集的构造需要敏感区间端点处的估计量联合渐近正态，且协方差矩阵可一致估计。若端点处估计量非正则（如边界点），渐近正态性可能不成立。
  - 反例存在？当敏感区间退化为单点（δ=0）时，置信集退化为标准置信区间，此时方法应自动退化。需验证退化情形下的覆盖性质。
  - 算不出来？线性规划求解敏感区间在工具变量个数多时可能计算量大，但二元工具下是简单的。

- **交付形态**：`方法+模拟型`

- **第一周动作**：
  1. 读 [4] Section 3-4，理解敏感区间的线性规划构造，特别是端点处标准误的计算公式（Proposition 1的证明）。
  2. 读 [30] Section 3，理解全局敏感性分析中识别区间的构造，特别是偏差函数参数化方式。
  3. 推导二元工具、二值处理下敏感区间端点估计量的联合渐近分布（通过Delta方法）。
  4. 用R实现Imbens & Manski (2004) 的置信区间构造方法，在n=500模拟数据下测试覆盖概率（δ固定已知）。
  5. 搜索Armstrong (2022) 关于集合值参数推断的论文，确认其方法是否可直接套用。

---

### 本页的证据论文

- [1] ★ [Calibrated sensitivity models](/research-news/deep_reads/2026-05-26-10.1093_biomet_asag001/) — Biometrika · 2026-05-26
- [2] ★ [Adaptive Estimation of Aggregated Values of Conditional Linear Programs](/research-news/deep_reads/2026-06-09-2606.08359/) — 2026-06-09
- [3] ★ [A new design for observational studies applied to the study of the effects of high school football on cognition late in life](/research-news/deep_reads/2026-06-19-10.1214_24-aoas1949/) — Annals of Applied Statistics · 2026-06-19
- [4] ★ [What's the Magic Formula Instrument?](/research-news/deep_reads/2026-06-23-2606.21569/) — 2026-06-23
- [5] ★ [The risk of maternal complications after cesarean delivery: Near-far matching for instrumental variables study designs with large observational datasets](/research-news/deep_reads/2026-06-24-10.1214_22-aoas1691/) — Annals of Applied Statistics · 2026-06-24
- [6] ★ [Doubly robust estimation and sensitivity analysis for marginal structural quantile models](/research-news/deep_reads/2026-07-03-10.1093_biomtc_ujae045/) — Biometrics · 2026-07-03
- [7] ★ [Multiplier U-processes: Sharp bounds and applications](/research-news/deep_reads/2026-07-14-10.3150_21-bej1334/) — Bernoulli · 2026-07-14
- [8] ★ [Apportioning Causal Responsibility of Two Risk Factors for an Adverse Outcome via Counterfactual Attribution](/research-news/deep_reads/2026-06-19-2606.18459/) — 2026-06-19
- [9] ★ [Choosing A Headline Estimand from Matching, DID, and Hybrid Designs: A Minimax-Regret Approach](/research-news/deep_reads/2026-06-22-2606.20435/) — 2026-06-22
- [10] ★ [Stochastic interventions, sensitivity analysis, and optimal transport](/research-news/deep_reads/2026-08-31-2411.14285/) — 2026-08-31
- [11] ★ [The global demand and potential public health impact of oral antiviral treatment stockpile for influenza pandemics](/research-news/deep_reads/2026-07-31-10.1073_pnas.2524161123/) — Proceedings of the National Academy of Sciences · 2026-07-31
- [12] [Semiparametric Mediation Analysis with Separately Observed Mediator and Outcome under Unmeasured Confounding](/research-news/deep_reads/2026-06-17-2606.17232/) — 2026-06-17
- [13] [Nested Sensitivity Envelopes for Transported Quantile Treatment Effects](/research-news/deep_reads/2026-05-12-2605.09264/) — 2026-05-12
- [14] [Sensitivity analysis for causal mediation: bridge score, sharp sensitivity bounds, and calibration](/research-news/deep_reads/2026-05-19-2605.18724/) — 2026-05-19
- [15] [Confidence intervals for causal effects in sequential decision making](/research-news/deep_reads/2026-05-26-2605.25687/) — 2026-05-26
- [16] [Identification and multiply robust estimation in causal mediation analysis across principal strata](/research-news/deep_reads/2026-05-26-10.1093_jrsssb_qkaf037/) — Journal of the Royal Statistical Society Series B · 2026-05-26
- [17] [Beyond principal ignorability: Nonparametric sensitivity bounds for principal stratification](/research-news/deep_reads/2026-06-02-2606.01669/) — 2026-06-02
- [18] [Partial Identification under High-Dimensional Potential Outcomes and Confounders via Optimal Transport](/research-news/deep_reads/2026-06-02-2606.00847/) — 2026-06-02
- [19] [Local Sensitivity Under Transport Restrictions](/research-news/deep_reads/2026-06-04-2606.04276/) — 2026-06-04
- [20] [Stochastic Sensitivity Analysis for Matched Observational Studies](/research-news/deep_reads/2026-06-04-2606.05120/) — 2026-06-04
- [21] [Policy learning with new treatments](/research-news/deep_reads/2026-06-07-10.3982_qe2477/) — Quantitative Economics · 2026-06-07
- [22] [The informativeness of combined experimental and observational data under dynamic selection](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106219/) — Journal of Econometrics · 2026-06-07
- [23] [Treatment effects with targeting instruments](/research-news/deep_reads/2026-06-07-10.1016_j.jeconom.2026.106253/) — Journal of Econometrics · 2026-06-07
- [24] [Sharp Bounds and Inference in Sample Selection Models with Treatment Endogeneity](/research-news/deep_reads/2026-06-09-2606.09223/) — 2026-06-09
- [25] [Addressing the influence of unmeasured confounding in observational studies with time-to-event outcomes: a semiparametric sensitivity analysis approach](/research-news/deep_reads/2026-06-10-10.1093_biostatistics_kxag005/) — Biostatistics · 2026-06-10
- [26] [Multiply robust estimation for causal survival analysis with treatment noncompliance](/research-news/deep_reads/2026-06-10-10.1214_25-aoas2117/) — Annals of Applied Statistics · 2026-06-10
- [27] [Data fusion methods for the heterogeneity of treatment effect and confounding function](/research-news/deep_reads/2026-06-18-10.3150_24-bej1835/) — Bernoulli · 2026-06-18
- [28] [Mediation analysis with unmeasured confounding between parallel mediators and outcome](/research-news/deep_reads/2026-06-18-10.1214_26-ejs2517/) — Electronic Journal of Statistics · 2026-06-18
- [29] [Efficient Estimation of Average Treatment Effects with Unmeasured Confounding and Proxies](/research-news/deep_reads/2026-06-19-10.5705_ss.202025.0104/) — Statistica Sinica · 2026-06-19
- [30] [Global Sensitivity Analysis for Studies Extending Inferences From a Randomized Trial to a Target Population](/research-news/deep_reads/2026-06-19-10.1002_sim.70083/) — Statistics in Medicine · 2026-06-19

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

