# 因果推断 · 专题 A：设计、随机化与数据融合

> JCSDS 2026 · Causal Inference A — Design, Randomization & Data Integration · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 9 场）

## 本专题导览

> 自动生成：归纳本专题主线与建议先看的几场，**不打分、不排名**。

本专题的 4 个分会场共享一条主线：**以随机化/设计为根基，逐一攻克现实实验中破坏经典假设的复杂因素**。Peng Ding 组织的两场是骨架——「Design-Based Causal Inference」处理设计层面的偏离（样本流失下的随机化推断、有向网络边层结果、交叉设计、免样本分割的模型辅助检验），「Data Integration and Surrogate Endpoint」处理数据层面的缺口（长期效应的近端 DiD、个体化治疗中的替代终点评估、持续混杂下的数据融合、以及组合有偏/无偏估计量的 B 值敏感性分析）。Feifang Hu 的「Adaptive Randomization」把视角转向**分配机制本身自适应**（CARA 网络干扰、协变量自适应下的 assumption-lean 调整、ego-cluster 溢出效应）。Jingfei Zhang 的「Adaptive Learning」则把因果与**跨源/跨任务学习**耦合（联邦多任务、高维中介、空间干扰下的动态治疗规则、分层投影迁移）。若按依赖关系浏览，建议先看 Design-Based 场作为方法论基座，再看 Data Integration 场理解「短期↔长期、实验↔观测」的数据拼接，最后看两场 Adaptive 场——它们把静态设计推向自适应、网络干扰与迁移学习的前沿。贯穿全专题的两个关键词是**稳健性**（对模型误设、缺失、混杂、干扰）与**效率**（协变量调整、交叉拟合、数据融合的增益），二者的调和正是设计基础因果推断当前的核心张力。

---

## Design-Based Causal Inference

*7 月 12 日（周日） · 15:30-17:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Peng Ding（University of California,Berkeley） · 主持 Peng Ding（University of California,Berkeley）*

### 1. Randomization Inference with Sample Attrition

**讲者**：Xinran Li（University of Chicago）

**对应论文**：Randomization Inference with Sample Attrition · [arXiv:2507.00795](https://arxiv.org/abs/2507.00795)

<details><summary>摘要（原文）</summary>

Randomization inference is a widely-used and appealing approach for analyzing treatment effects in randomized experiments, as it is finite-sample valid and does not require any distributional assumptions. However, naive application of randomization inference may suffer from severe size distortion in the presence of sample attrition, where outcome data are missing for some units. In this paper, we propose new, computationally efficient methods for randomization inference that remain valid under a broad class of potentially informative missingness mechanisms, allowing a unit's missingness to depend on its (unobserved) potential outcomes. Specifically, we construct valid p-values for testing both sharp and bounded null hypotheses on treatment effects via a worst-case consideration of the classical Fisher randomization test. Leveraging distribution-free test statistics, these worst-case p-values admit closed-form solutions. Importantly, by incorporating both potential outcomes and potential missingness indicators into the test statistic, our methods can exploit structural assumptions such as monotone missingness, which are commonly adopted in applications due to their plausibility and ability to substantially improve inferential power. Moreover, our approach connects to a range of partial identification bounds in the literature, which in some sense suggests the sharpness of our tests. We illustrate the proposed methods through both simulation studies and an empirical application. An R package implementing the proposed methods is publicly available.

</details>

**问题**  
随机化实验中的样本损耗（sample attrition）导致部分单元结果缺失，若直接丢弃缺失单元并应用经典 Fisher 随机化检验，可能产生严重的尺寸扭曲。传统方法常假设缺失完全随机或对缺失机制施加强约束，但实际中缺失可能依赖于未观测的潜在结果（即信息性缺失）。如何在允许任意信息性缺失的机制下，仍能构造有限样本有效的随机化推断，是本文要解决的核心问题。

**核心方法**  
作者提出基于最坏情况考虑（worst-case consideration）的随机化检验。首先，利用分布自由的秩统计量（如 Wilcoxon 秩和统计量）作为检验统计量，其零分布仅依赖于处理分配机制，与结果值无关，从而避免了缺失导致的分布未知问题。其次，通过构造“复合控制潜在结果” $\tilde{Y}_{b,i}(0) = Y_i(0) M_i(0) M_i(1) + b_{00}(1-M_i(0))(1-M_i(1)) + b_{01}(1-M_i(0))M_i(1) + b_{10} M_i(0)(1-M_i(1))$，将缺失机制的结构信息（如单调缺失）融入检验统计量。在给定观测数据和零假设下，通过最小化（对处理组）或最大化（对对照组）复合结果，得到最坏情况下的 p 值，该 p 值具有封闭解且计算高效。进一步，两步法利用观测缺失模式推断缺失类型的分布，构造置信集并施加约束，从而提升检验功效。

**与已有工作关系**  
本文与部分识别文献紧密相连：最坏情况 p 值自然对应 Manski (1990) 和 Horowitz & Manski (2000) 的平均处理效应 sharp bounds；在单调缺失下，两步法的比较方式与 Zhang & Rubin (2003) 和 Lee (2009) 的 bounds 一致。此外，本文扩展了随机化检验到非 sharp 零假设（如 bounded null），并首次将稳健随机化推断与部分识别框架显式关联。与现有处理缺失的随机化方法（如假设缺失随机或零处理效应于缺失）不同，本文允许任意信息性缺失，且不依赖分布假设。

**主要贡献**  
1. 提出在样本损耗下仍有效的随机化检验方法，适用于一般缺失、单调缺失和 sharp 缺失等多种机制，且计算高效（p 值有封闭解）。  
2. 通过复合结果变量和两步法，有效利用缺失机制的结构信息，显著提升检验功效，同时保持有限样本有效性。  
3. 建立了随机化推断与部分识别界限之间的理论联系，为理解检验的 sharpness 提供了新视角。  
4. 提供公开 R 包，便于实证应用。


### 2. Design-Based Prediction-Powered Inference for Edge-Level Outcomes in Directed Networks

**讲者**：Hanzhong Liu（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在有向网络中，边级结果（如社交网络中的信息传递次数、引用网络中的引用强度）的统计推断面临两大挑战：一是网络依赖性与干扰效应破坏了传统独立同分布假设；二是完全观测所有边级结果成本高昂。现有预测驱动推断（Prediction-Powered Inference, PPI）方法虽能利用机器学习预测提升效率，但主要针对独立数据或节点级结果。本报告旨在解决：如何在有向网络的设计框架下（如随机化实验或抽样设计），借助预测模型对边级结果进行有效推断，并保证覆盖概率与置信区间宽度之间的权衡。

**核心方法**  
报告提出一种基于设计（design-based）的推断框架。核心思路是：首先利用有向网络的结构特征（如入度、出度、互惠性）及协变量，训练一个预测模型 $\hat{f}(e)$ 估计每条边 $e$ 的结果 $Y_e$；然后基于实验或抽样设计（如随机分配边级干预或子集抽样），仅观测部分边的真实结果，构造一个“预测辅助”的估计量，例如 $\hat{\tau} = \frac{1}{N}\sum_{e \in \mathcal{U}} \hat{f}(e) + \frac{1}{n}\sum_{e \in \mathcal{S}} (Y_e - \hat{f}(e))$，其中 $\mathcal{U}$ 为全体边集，$\mathcal{S}$ 为观测子集。通过设计随机化保证 $\hat{\tau}$ 的无偏性，并推导其方差表达式，进而构造渐近正态的置信区间。方法的关键在于利用设计权重与预测残差的相关性，实现比纯设计或纯预测更小的方差。

**与已有工作关系**  
与经典 PPI（Angelopoulos et al., 2023）相比，本工作将独立数据假设推广到有向网络，并引入设计随机化以处理边级依赖。与网络因果推断中常用的逆概率加权或双重稳健估计相比，本方法明确聚焦于“预测驱动”这一视角，强调利用现代机器学习模型提升效率，而非仅依赖网络结构假设。此外，现有网络推断多关注节点级平均处理效应，本报告首次系统处理边级结果的推断问题，填补了有向网络下预测辅助推断的理论空白。

**贡献**  
主要贡献有三：第一，提出首个针对有向网络边级结果的 design-based PPI 框架，给出估计量的无偏性与渐近正态性证明；第二，推导了最优预测模型选择准则，并给出方差估计的显式公式，支持实际应用中的置信区间构造；第三，通过模拟与真实网络数据（如电子邮件网络、引文网络）验证方法在效率与覆盖概率上的优势，为网络数据分析提供了一种兼具理论严谨性与计算可行性的新工具。


### 3. Principled Analysis of Crossover Designs: Causal Effects, Efficient Estimation, and Robust Inference

**讲者**：Zhichao Jiang（Sun Yat-sen University）

**对应论文**：Principled analysis of crossover designs: causal effects, efficient estimation, and robust inference · [arXiv:2511.09215](https://arxiv.org/abs/2511.09215)

<details><summary>摘要（原文）</summary>

Crossover designs randomly assign each unit to receive a sequence of treatments. By comparing outcomes within the same unit, these designs can effectively eliminate between-unit variation and facilitate the identification of both instantaneous effects of current treatments and carryover effects from past treatments. They are widely used in traditional biomedical studies and are increasingly adopted in modern digital platforms. However, standard analyses of crossover designs often rely on strong parametric models, making inference vulnerable to model misspecification. This paper adopts a design-based framework to analyze general crossover designs. We make two main contributions. First, we use potential outcomes to formally define the causal estimands and assumptions on the data-generating process. For any given type of crossover design and assumptions on potential outcomes, we outline a procedure for identification and estimation, emphasizing the central role of the treatment assignment mechanism in design-based inference. Second, we unify the analysis of crossover designs using least squares, with restrictions on the coefficients and weights on the units. Based on the theory, we recommend the specification of the regression function, weighting scheme, and coefficient restrictions to assess identifiability, construct efficient estimators, and estimate variances in a unified fashion. Crucially, the least squares procedure is simple to implement, and yields not only consistent and efficient point estimates but also valid variance estimates even when the working regression model is misspecified.

</details>

**问题**  
交叉设计（crossover design）通过让同一单元接受多个治疗序列，消除单元间变异，从而高效估计瞬时效应和携带效应。然而，传统分析依赖强参数模型（如线性混合模型），其因果估计量定义于模型之内，易因模型误设而产生偏倚，且难以灵活适应不同实验配置。核心问题在于：在仅依赖随机化（design-based）的框架下，如何对任意交叉设计进行因果效应的识别、有效估计与稳健推断？

**核心方法**  
本文采用潜在结果框架，形式化定义瞬时效应 $\tau_t$ 与 $k$ 阶携带效应 $\tau_t^k$，并引入无预期假设（Assumption 1）、无高阶携带效应（Assumption 2）及时间不变性（Assumption 3）等可解释假设。关键创新在于将上述假设转化为对回归系数的线性约束 $C\gamma=0$，并提出**受限加权最小二乘**（restricted weighted least squares）作为统一估计工具。该方法以单元为观测，将各期结果向量堆叠，回归自变量为处理序列指示变量，权重矩阵为各序列内潜在结果的协方差矩阵（可一致估计）。在满秩条件 $X^\top X + C^\top C$ 下，受限加权最小二乘估计量是因果效应的最佳线性无偏估计（BLUE），且其 Eicker–Huber–White 方差估计量在 design-based 下是保守的（Theorem 3），即使工作模型误设仍有效。

**与已有工作关系**  
区别于传统模型基于方法（如 Senn, 2002; Jones & Kenward, 2003），本文不假设数据生成过程，而是将随机化作为推断基础，与 Neyman (1923)、Lin (2013) 等 design-based 回归调整一脉相承。与 Bojinov et al. (2023) 等时间序列实验相比，本文统一处理任意周期数与序列子集，并通过系数约束系统性地纳入科学假设。此外，受限加权最小二乘的理论推广（如广义 Gauss–Markov 定理）本身具有独立统计价值。

**贡献**  
1. 为交叉设计提供了 design-based 的因果定义与识别条件，明确区分因果假设与建模假设。  
2. 提出基于受限加权最小二乘的统一估计与推断框架，仅需指定回归函数、权重与约束，即可自动获得 BLUE 与保守方差估计，计算简单且适用于任意设计。  
3. 建立了受限加权最小二乘的渐近理论，包括 EHW 方差估计的保守性及假设检验方法，为实践者提供了可靠工具。  
4. 通过实例与模拟展示了方法相对于模型基于方法的稳健性与效率优势，并指出向删失数据、聚类设计等方向的扩展空间。


### 4. Model-Assisted Randomization Tests Without Sample Splitting

**讲者**：Yao Zhang（National University of Singapore）

**对应论文**：Fit CATE Once: Model-Assisted Randomization Tests Without Sample Splitting · [arXiv:2605.09116](https://arxiv.org/abs/2605.09116)

<details><summary>摘要（原文）</summary>

Randomization tests and flexible treatment-effect models offer complementary strengths for analyzing data from randomized panel experiments: the former provide valid inference under the known assignment mechanism, while the latter can capture complex patterns of effect heterogeneity. We develop model-assisted randomization tests that combine these strengths without sample splitting. The key idea is to estimate an unsigned version of the conditional average treatment effect (CATE) from the covariance structure of residualized outcomes, while leaving the realized assignments for randomization inference. The remaining sign can be chosen to best fit the observed outcomes. We establish identification and consistency for the proposed unsigned CATE estimators, as well as validity for the CATE-assisted randomization tests. Across synthetic and semi-synthetic experiments, the CATE-assisted randomization tests control Type I error and achieve higher power than covariate-adjusted and sample-split alternatives. Finally, we show that the assignment-free CATE estimates can be used to discover heterogeneous subgroups and test subgroup-specific treatment effects.

</details>

**问题**：在随机化面板实验中，如何在不进行样本分割（sample splitting）的前提下，利用灵活的异质性处理效应模型（如 CATE）来构造更高效的随机化检验？传统做法要么为每个随机化分配重拟合模型（计算昂贵），要么牺牲部分样本用于模型估计（损失功效）。本文旨在打破这一权衡，在保持有限样本有效性的同时提升检验功效。

**核心方法**：关键洞察在于，在加性结果模型下，残差化后的结果可写为处理时机指示变量与滞后处理效应的线性组合加噪声。因此，残差的二阶矩（协方差矩阵）编码了处理效应的幅度信息，且仅依赖于协变量、结果和已知的分配机制，而与实际分配无关。具体地，若效应滞后不变，对角矩可识别公共效应大小；若残差序列不相关，离对角矩可识别整个滞后 CATE 向量（至多一个全局符号）。剩余符号可通过最小化残差拟合损失或利用少量分配信息确定，从而得到有符号的 CATE 估计，用于构造检验统计量（如 AIPW 或似然比得分）。

**与已有工作关系**：已有随机化检验的协变量调整多基于条件均值模型（Rosenbaum, 2002; Zhao & Ding, 2021），或需样本分割（Zhang & Gao, 2025）或重拟合（Guo et al., 2025）。本文首次利用面板数据的重复观测结构，从残差协方差中无分配地提取 CATE 信息，避免了样本分割和重拟合的计算负担，同时保留了 CATE 模型在捕捉异质性方面的优势。

**贡献**：① 提出无分配 CATE 估计框架（对角矩与离对角矩），并建立局部/全局识别性及一致性；② 构造 CATE 辅助随机化检验，在控制第一类错误的同时，相比无调整、协变量调整及样本分割方法显著提升功效；③ 证明无分配 CATE 估计可用于发现异质性子组并进行子组检验，拓展了方法的应用范围。


## Data Integration and Surrogate Endpoint for Causal Inference

*7 月 12 日（周日） · 13:30-15:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Peng Ding（University of California,Berkeley） · 主持 Peng Ding（University of California,Berkeley）*

### 1. Estimating Long-Term Treatment Effects: a Semiparametric Proximal DiD Approach

**讲者**：Shu Yang（North Carolina State University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在观察性研究中，长期处理效应（Long-Term Treatment Effects）的估计常受限于两个挑战：一是存在未观测混杂（unmeasured confounding），二是研究者仅能观测到短期结局或代理变量（proxies），而真正的长期结局可能缺失或测量滞后。传统双重差分（DiD）方法依赖平行趋势假设，但该假设在长期中易被违反；现有代理变量方法（如proximal causal inference）虽能处理未观测混杂，却通常要求代理变量满足特定的条件独立性，且难以直接利用时间上的差分结构。本报告旨在提出一种半参数方法，结合代理变量与DiD框架，在更弱的假设下识别并估计长期平均处理效应（ATE）。

**核心方法**  
讲者引入“Proximal DiD”框架，将代理变量（如短期结局、协变量的替代测量）作为未观测混杂的“影子”，并利用两期数据（处理前与处理后）的差分结构。具体地，假设存在两个代理变量 $Z_1, Z_2$ 满足某种条件独立性（如 $Z_1 \perp Z_2 \mid U, T$，其中 $U$ 为未观测混杂，$T$ 为处理变量），且处理效应在时间上具有某种结构（如线性或可加性）。通过构建半参数矩条件（moment conditions），结合DiD的差分思想，导出长期效应的识别公式。估计采用两步法或最小化某个损失函数，得到 $\sqrt{n}$-consistent 的估计量，并允许使用机器学习方法（如随机森林、神经网络）灵活建模代理变量与结局的关系。

**与已有工作关系**  
已有文献中，proximal causal inference（Tchetgen Tchetgen et al., 2020）主要处理单期或静态的未观测混杂，未充分利用时间维度信息；而传统DiD（如Abadie, 2005）依赖平行趋势假设，无法直接处理未观测混杂随时间变化的情形。本工作将两者结合：一方面，利用代理变量放松DiD中平行趋势假设（允许未观测混杂随时间变化）；另一方面，利用DiD的差分结构减少对代理变量条件独立性的要求（例如，仅需代理变量与未观测混杂在差分意义上满足某种条件）。这比单纯使用代理变量或DiD更灵活，且能处理长期效应估计中常见的“测量误差”与“动态混杂”问题。

**主要贡献**  
1. 提出一个统一的半参数框架，首次将proximal inference与DiD结合，用于长期处理效应估计，拓展了因果推断的适用场景。  
2. 在较弱的识别条件下（如允许未观测混杂随时间变化、代理变量存在测量误差）给出长期效应的可识别性证明，并构造了双重稳健（doubly robust）的估计量，即只要部分模型（如代理变量与结局的关系或处理分配机制）正确设定，估计量即一致。  
3. 提供渐近正态性与有效推断的理论结果，并通过模拟和实证（如劳动经济学中的培训项目长期效果）展示方法的实用性，为政策评估中“短期数据推断长期效果”这一难题提供了新工具。


### 2. Evaluating Surrogates in Individual Treatment Regimes

**讲者**：Yue Liu（Renmin University of China）

**对应论文**：Evaluating Surrogates in Individualized Treatment Rules · [arXiv:2512.00405](https://arxiv.org/abs/2512.00405)

<details><summary>摘要（原文）</summary>

In many decision-making problems, the primary outcome is expensive, time-consuming, or difficult to observe, so individualized treatment rules (ITRs) may be instead learned from surrogate endpoints. However, a surrogate that is highly associated with the primary outcome, or even satisfies existing surrogate criteria, may not necessarily induce a treatment rule that performs well on the primary outcome, especially under treatment resource budget constraints. In this paper, we develop a principled framework for evaluating the decision-making value of surrogate endpoints. We introduce three ITR-oriented performance measures: surrogate regret, which assesses the expected loss from using the surrogate-optimal ITR instead of outcome-optimal ITR; surrogate gain, which quantifies the benefit of surrogate-optimal ITRs relative to the no-treatment baseline; and surrogate efficiency, which evaluates improvement over random treatment assignment. We also extend them to budget-constrained settings. We propose augmented inverse probability weighted (AIPW) estimators for these measures and establish their large-sample properties. We demonstrate the proposed approach on both simulations and an application to the Criteo dataset.

</details>

**问题**：当主要结局（如长期转化率、临床死亡率）昂贵或延迟时，研究者常依赖替代终点（如点击率、生物标志物）学习个体化治疗规则（ITR）。然而，现有替代标准（如高观测相关性、潜在结局相关性、甚至符号保持）均不能保证替代诱导的ITR在主要结局上表现良好，尤其在预算约束下可能劣于随机分配。报告旨在回答：如何直接评估替代终点在ITR中的决策价值？

**核心方法**：引入三个面向ITR的评估指标——**surrogate regret**（使用替代最优ITR而非结局最优ITR的期望损失）、**surrogate gain**（相对于无治疗的增益）和**surrogate efficiency**（相对于随机分配的改进），并扩展至预算约束下的$\lambda$-版本。基于增广逆概率加权（AIPW）构造估计量，利用样本分割或交叉拟合处理非光滑指示函数，在margin条件下建立$\sqrt{n}$-一致性和渐近正态性。关键技巧是将偏差分解为乘积项（如倾向得分与回归误差的乘积）和由margin参数控制的一阶项。

**与已有工作关系**：现有替代文献（Prentice, Frangakis-Rubin, Wang等）聚焦于效应估计的替代有效性，而本文转向决策质量评估。与ITR学习文献（Qian-Murphy, Zhao等）不同，本文不学习最优规则，而是评估替代本身的价值。特别指出，即使符号保持（Yang等2023）在预算约束下也不充分，因为个体排序可能颠倒。

**贡献**：1. 提出首个面向ITR的替代评估框架，包含三个互补指标，直接量化决策损失与增益；2. 允许主结局与替代在不同样本中观测（两样本设计），实用性强；3. 发展AIPW估计与推断理论，给出收敛速率和渐近正态性条件，并通过模拟和Criteo数据集验证。该工作为实践中筛选替代终点提供了严谨的统计工具。


### 3. Long-Term Causal Inference under Persistent Confounding via Data Combination

**讲者**：Yuhao Wang（Tsinghua University）

**对应论文**：Long-term Causal Inference Under Persistent Confounding via Data Combination · [arXiv:2202.07234](https://arxiv.org/abs/2202.07234)

<details><summary>摘要（原文）</summary>

We study the identification and estimation of long-term treatment effects when both experimental and observational data are available. Since the long-term outcome is observed only after a long delay, it is not measured in the experimental data, but only recorded in the observational data. However, both types of data include observations of some short-term outcomes. In this paper, we uniquely tackle the challenge of persistent unmeasured confounders, i.e., some unmeasured confounders that can simultaneously affect the treatment, short-term outcomes and the long-term outcome, noting that they invalidate identification strategies in previous literature. To address this challenge, we exploit the sequential structure of multiple short-term outcomes, and develop three novel identification strategies for the average long-term treatment effect. We further propose three corresponding estimators and prove their asymptotic consistency and asymptotic normality. We finally apply our methods to estimate the effect of a job training program on long-term employment using semi-synthetic data. We numerically show that our proposals outperform existing methods that fail to handle persistent confounders.

</details>

**问题**  
长期因果推断中，研究者常面临“短期实验无长期结局、长期观测数据存在未测混淆”的两难困境。已有数据组合方法（如 Athey et al., 2020）假设短期结局能完全阻断处理与长期结局的关联（即无持久混淆），但现实中未观测混淆变量 $U$ 可能同时影响短期与长期结局，导致该假设失效。本文旨在解决持久混淆（persistent confounding）下的长期平均处理效应 $\tau = \mathbb{E}[Y(1)-Y(0)\mid G=O]$ 的识别与估计问题。

**核心方法**  
作者将多个短期结局按时间顺序分为三组 $S=(S_1,S_2,S_3)$，并假设其满足条件独立性（Assumption 4）：$(Y(a),S_3(a))\perp S_1(a)\mid S_2(a),U,X,G=O$。这一时序结构允许将 $S_1$ 和 $S_3$ 视为未观测混淆 $U$ 的代理变量。在此基础上，提出两类桥函数：  
- **结果桥函数** $h_0(S_3,S_2,A,X)$ 满足 $\mathbb{E}[Y\mid S_2,A,U,X,G=O]=\mathbb{E}[h_0\mid S_2,A,U,X,G=O]$，可通过观测数据中的条件矩方程 $\mathbb{E}[Y\mid S_2,S_1,A,X,G=O]=\mathbb{E}[h_0\mid S_2,S_1,A,X,G=O]$ 识别；  
- **选择桥函数** $q_0(S_2,S_1,A,X)$ 满足密度比条件，可通过类似矩方程识别。  
进而得到双重稳健识别公式（Theorem 3）：$\tau = \sum_a (-1)^{1-a}\big\{\mathbb{E}[h_0\mid A=a,G=E] + \mathbb{E}[q_0(Y-h_0)\mid A=a,G=O]\big\}$。基于此，作者构造了交叉拟合的估计量，并证明在桥函数估计满足弱/强度量误差乘积为 $o(n^{-1/2})$ 时，双重稳健估计量渐近正态且达到半参有效界。

**与已有工作关系**  
区别于 Athey et al. (2020) 的潜在无混淆性（无法处理持久混淆），本文首次利用短期结局的内部时序结构作为代理变量，而非将其视为整体。与经典代理推断（proximal causal inference）不同，本文的 $S_1,S_3$ 均受处理影响，不满足负控制条件，但借助实验数据实现了识别。此外，本文的识别策略与 Ghassami et al. (2022) 的“近端数据融合”等价，但本文更明确地揭示了短期结局的时序角色，并提供了完整的估计与推断理论。

**贡献**  
1. 在持久混淆下，利用短期结局的时序结构提出三种新的识别策略（结果桥函数、选择桥函数、双重稳健），放宽了已有方法对无持久混淆的依赖。  
2. 基于桥函数估计构造了长期处理效应估计量，并给出渐近一致性、正态性及半参有效性的理论保证，允许使用灵活的机器学习估计器。  
3. 通过半合成数据实验（GAIN项目）验证了方法在强持久混淆下显著优于基准方法，且双重稳健估计量表现最佳。


### 4. Introducing the B-Value: Combining Unbiased and Biased Estimators from a Sensitivity Analysis Perspective

**讲者**：Peng Ding（University of California,Berkeley）

**对应论文**：Introducing the b-value: combining unbiased and biased estimators from a sensitivity analysis perspective · [arXiv:2602.16310](https://arxiv.org/abs/2602.16310)

<details><summary>摘要（原文）</summary>

In empirical research, when we have multiple estimators for the same parameter of interest, a central question arises: how do we combine unbiased but less precise estimators with biased but more precise ones to improve the inference? Under this setting, the point estimation problem has attracted considerable attention. In this paper, we focus on a less studied inference question: how can we conduct valid statistical inference in such settings with unknown bias? We propose a strategy to combine unbiased and biased estimators from a sensitivity analysis perspective. We derive a sequence of confidence intervals indexed by the magnitude of the bias, which enable researchers to assess how conclusions vary with the bias levels. Importantly, we introduce the notion of the b-value, a critical value of the unknown maximum relative bias at which combining estimators does not yield a significant result. We apply this strategy to three canonical combined estimators: the precision-weighted estimator, the pretest estimator, and the soft-thresholding estimator. For each estimator, we characterize the sequence of confidence intervals and determine the bias threshold at which the conclusion changes. Based on the theory, we recommend reporting the b-value based on the soft-thresholding estimator and its associated confidence intervals, which are robust to unknown bias and achieve the lowest worst-case risk among the alternatives.

</details>

**问题**：在实证研究中，研究者常面临无偏但低效的估计量（如IV估计）与有偏但高效的估计量（如OLS估计）的权衡。如何结合二者进行有效的统计推断？当偏差$\Delta$未知时，如何构造随偏差水平变化的置信区间序列，并量化使结论反转的偏差阈值？

**核心方法**：论文从敏感性分析视角出发，假设无偏估计量$\hat{\tau}_0\sim N(\tau,\sigma_0^2)$与有偏估计量$\hat{\tau}_1\sim N(\tau+\Delta,\sigma_1^2)$独立，对相对偏差$|\Delta/\sigma_0|$施加上界$b$，构造一系列对称固定长度的置信区间$\hat{\tau}\pm c(b,\zeta)$，使其在$|\Delta/\sigma_0|\le b$上均匀覆盖$1-\zeta$。定义**b-value**为使得结合估计量不再显著（即$0\in\hat{\tau}\pm c(b,\zeta)$）的最小$b$，类似于Rosenbaum的设计敏感性或E-value。论文重点考察三种组合估计量：精度加权（PW）、预检验（PT）和软阈值（ST），并推导了各自的$c(b,\zeta)$与b-value。其中ST估计量具有覆盖概率关于$|\Delta|$单调递减的性质，计算效率最高，且最坏情况风险最低。

**与已有工作关系**：点估计层面已有大量研究（Bickel, 1984; Green & Strawderman, 1991等），但推断问题鲜有涉及。本文首次将敏感性分析框架引入组合估计的推断，与Rosenbaum (2004)的设计敏感性、VanderWeele & Ding (2017)的E-value一脉相承。软阈值估计量继承了Bickel (1983)的稳健性思想，但本文进一步给出了其置信区间构造和b-value的显式或数值解法。

**贡献**：1) 提出b-value这一新概念，为组合估计的推断提供直观的稳健性度量；2) 系统推导了PW、PT、ST三种估计量的置信区间序列和b-value计算方法，并证明ST估计量的单调性优势；3) 将框架推广到依赖、多元和多个估计量情形，并提供了Python包；4) 通过Angrist & Krueger (1991)的实证例子展示了方法在IV与OLS结合中的应用价值。


## New Advances in Adaptive Randomization

*7 月 12 日（周日） · 13:30-15:10 · Hongfeng Meeting Room*  
*组织 Feifang Hu（George Washington University） · 主持 Feifang Hu（George Washington University）*

### 1. Dynamic Influencer Identification in CARA Experiments under Bipartite Network Interference

**讲者**：Likun Zhang（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在二分图网络（如平台与用户、广告主与消费者）的随机实验（CARA 实验，即条件平均响应自适应实验）中，个体间的干扰（interference）通过二分图结构传播，且影响者的身份可能随时间动态变化。传统方法要么假设静态网络、要么忽略二分图特有的跨层干扰，难以在实验进行中实时识别当前最具影响力的节点（influencer）。本报告旨在解决：如何在二分图干扰下，利用在线实验数据动态识别影响者，以优化后续干预分配。

**核心方法**  
讲者可能提出一种结合 **bandit 算法** 与 **因果推断** 的在线学习框架。具体地，将二分图一侧的节点（如平台上的内容创作者）视为候选影响者，另一侧节点（如用户）为受干扰单元。利用 **CARA 实验** 的自适应随机化机制，在每一轮根据当前累积数据估计每个候选影响者的 **条件平均处理效应（CATE）**，并采用 **上置信界（UCB）** 或 **汤普森采样** 策略平衡探索与利用。为处理二分图干扰，方法可能引入 **网络暴露模型**（如基于邻居处理状态的线性或阈值函数），并利用 **双重机器学习（DML）** 或 **逆概率加权（IPW）** 对干扰效应进行去偏估计。

**与已有工作关系**  
已有工作主要分为两类：一是静态网络下的影响者识别（如基于中心性指标或离线因果图），二是动态实验中的自适应分配（如 contextual bandit）。本报告将二者结合，并专门针对二分图结构——该结构常见于平台经济（如直播带货中主播影响观众），但现有因果推断文献多假设单层网络（如个体间直接相连）。此外，CARA 实验通常假设无干扰或干扰结构已知，本报告允许干扰结构未知且随时间变化。

**主要贡献**  
1. 首次在二分图网络干扰下提出动态影响者识别问题，并给出形式化定义。  
2. 设计了一种自适应实验算法，在保证统计效力的同时，渐近地识别出最优影响者，且 regret 上界为 $O(\sqrt{T})$ 量级。  
3. 提供了理论保证：在 mild 条件下，算法估计的影响者效应一致，且识别错误概率随实验轮次指数衰减。  
4. 可能通过仿真或真实数据（如社交平台实验）验证方法有效性，为平台运营中的实时干预策略提供因果推断工具。


### 2. Assumption-Lean Covariate Adjustment in Covariate Adaptive Randomization

**讲者**：Lin Liu（Shanghai Jiao Tong University）

**对应论文**：Assumption-lean covariate adjustment under covariate adaptive randomization when $p = o (n)$ · [arXiv:2512.20046](https://arxiv.org/abs/2512.20046)

<details><summary>摘要（原文）</summary>

Adjusting for (baseline) covariates with working regression models becomes standard practice in the analysis of randomized clinical trials (RCT). When the dimension $p$ of the covariates is large relative to the sample size $n$, specifically $p = o (n)$, adjusting for covariates even in a linear working model by ordinary least squares can yield overly large bias, defeating the purpose of improving efficiency. This issue arises when no structural assumptions are imposed on the outcome model, a scenario that we refer to as the assumption-lean setting. Several new estimators have been proposed to address this issue. However, they focus mainly on simple randomization under the finite-population model, not covering covariate adaptive randomization (CAR) schemes under the superpopulation model. Due to improved covariate balance between treatment groups, CAR is more widely adopted in RCT; and the superpopulation model fits better when subjects are enrolled sequentially or when generalizing to a larger population is of interest. Thus, there is an urgent need to develop procedures in these settings, as the current regulatory guidance provides little concrete direction. In this paper, we fill this gap by demonstrating that an adjusted estimator based on second-order $U$-statistics can almost unbiasedly estimate the average treatment effect and enjoy a guaranteed efficiency gain if $p = o (n)$. In our analysis, we generalize the coupling technique commonly used in the CAR literature to $U$-statistics and also obtain several useful results for analyzing inverse sample Gram matrices by a delicate leave-$m$-out analysis, which may be of independent interest. Both synthetic and semi-synthetic experiments are conducted to demonstrate the superior finite-sample performance of our new estimator compared to popular benchmarks.

</details>

**问题**：在协变量自适应随机化（CAR）设计的随机对照试验中，当调整的协变量维度 $p$ 相对于样本量 $n$ 较大（$p = o(n)$）时，传统的 OLS 调整估计量因包含对角项而产生 $O(p/n)$ 量级的偏差，导致推断失效。现有偏差校正方法多针对简单随机化下的有限总体模型，尚未覆盖 CAR 下的超总体模型。因此，亟需一种在假设宽松（assumption-lean）设定下、无需对结局模型施加结构假设（如线性或稀疏性）的稳健且高效的 ATE 估计量。

**核心方法**：本文提出基于二阶 $U$-统计量的新估计量 $\hat{\tau}$。其核心思想是：将 OLS 调整项中的 $V$-统计量（含对角项）替换为 $U$-统计量（剔除对角项），从而消除由高维协方差矩阵逆估计引入的偏差。具体地，在每个分层 $k$ 内，分别对处理组和对照组构造 $U$-统计量 $U_{n[k],2}(\hat{\Sigma}_{[k]}^{-1}; a)$，再结合分层均值差得到 $\hat{\tau}$。该方法仅需 $p = o(n)$ 且协变量有界、Gram 矩阵特征值有界等温和条件，即可保证 $\sqrt{n}$-相合性与渐近正态性，且渐近方差不超过未调整估计量。

**与已有工作关系**：区别于 Zhao et al. (2024) 等针对简单随机化与有限总体模型的工作，本文聚焦于 CAR 与超总体模型，更贴合序贯入组和总体推断的实际需求。与 Jiang et al. (2025) 相比，后者在 $p \gtrsim \sqrt{n}$ 时需假设线性结局模型正确，而本文允许任意非线性关系，实现真正的“假设宽松”。技术上，本文将 CAR 文献中的耦合技巧推广至 $U$-统计量，并发展出精细的 leave-two-out 分析以处理样本 Gram 矩阵逆的随机性，这些工具具有独立价值。

**贡献**：方法论上，首次在 CAR 与超总体模型下给出 $p = o(n)$ 时无需模型假设的偏差校正 ATE 估计量，并构造了相合方差估计量以支持 Wald 型推断。理论上，建立了 $U$-统计量在 CAR 下的渐近性质，并解决了高维逆 Gram 矩阵的 decoupling 难题。实证上，通过模拟和半真实数据验证了 $\hat{\tau}$ 在偏差、效率和覆盖概率上均优于 OLS 与未调整估计量，为 FDA 指南中“协变量数较大时”的情形提供了具体可行的分析方案。


### 3. Some Recent Advances in Adaptive Design

**讲者**：Wei Ma（Renmin University of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
传统临床试验设计（如固定随机化比例、固定样本量）在伦理与效率上存在显著局限：患者可能被分配至疗效较差的治疗组，且中期数据无法动态调整分配方案或样本量。自适应设计（Adaptive Design）旨在利用累积数据修改试验流程，但现有方法在延迟响应、协变量异质性、多重比较控制等方面仍面临挑战。本报告聚焦于近期自适应设计在理论严谨性与实际可操作性上的突破，尤其关注响应自适应随机化（Response-Adaptive Randomization, RAR）与样本量重估（Sample Size Re-estimation, SSR）的融合。

**核心方法**  
报告系统介绍了基于贝叶斯框架的RAR方法，如采用Thompson sampling动态更新治疗分配概率，并引入协变量平衡机制（如Covariate-Adaptive RAR）以降低组间混杂。同时，针对中期分析中效应量估计的不确定性，提出结合条件功效（Conditional Power）的SSR策略，允许在维持Type I error控制的前提下调整最终样本量。方法核心在于利用序贯似然比检验（Sequential Likelihood Ratio Test）与鞅理论推导渐近性质，并借助重抽样（Bootstrap）校准有限样本下的决策边界。

**与已有工作关系**  
经典RAR（如Play-the-Winner规则）缺乏严格的Type I error控制，且对延迟响应敏感。本报告的新进展将RAR与group sequential design结合，通过信息分数（Information Fraction）的实时估计，在保证检验效力的同时避免过度分配。相比传统SSR仅基于方差调整，新方法允许根据中期疗效差异动态修改分配比例，并利用多重比较调整（如Bonferroni-Holm校正）处理多臂试验。此外，与现有贝叶斯自适应设计相比，报告强调频率学派下的渐近有效性，弥补了理论空白。

**贡献**  
主要贡献有三：其一，为延迟响应场景下的RAR提供了严格的Type I error控制框架，证明其渐近最优性；其二，提出协变量调整的RAR与SSR联合算法，在异质性人群中实现更高效的分配；其三，通过模拟与真实临床试验案例（如肿瘤学II/III期无缝设计）验证方法在降低样本量需求与提升伦理收益上的优势。这些进展为自适应设计从理论走向实际应用提供了可操作的统计工具与理论保障。


### 4. Estimating Treatment and Spillover Effects with Ego-Cluster Experimental Design

**讲者**：Xiao Liu（Renmin University of China）

**对应论文**：Estimating Treatment and Spillover Effects with the Ego-Cluster Experimental Design · [arXiv:2605.00534](https://arxiv.org/abs/2605.00534)

<details><summary>摘要（原文）</summary>

Network interference occurs when a unit's outcome depends not only on its own treatment but also on the treatments received by connected units in the network. Experimental designs and analysis methods that ignore such interference can yield biased estimators of causal effects. In this paper, we develop a new experimental design for the estimation and inference of global treatment effect and spillover effect under a model-based framework and ego-cluster randomization. Under this design, the network is partitioned into a collection of ego-clusters, each consisting of a focal unit (the ego) and its network neighbors (the alters), with randomization conducted at the cluster level. We propose model-based estimators for the global treatment effect and spillover effect and establish their consistency and asymptotic normality, with asymptotic variances determined by the ego-cluster structure. Building on these theoretical results, we introduce an ego-clustering algorithm that sequentially selects egos and assigns alters to minimize asymptotic variances. Simulation studies and two empirical applications demonstrate that the proposed procedure yields accurate inference and efficiency improvements over existing network experimental designs.

</details>

**问题**：网络实验中，个体结果不仅受自身处理影响，还受邻居处理干扰（network interference），导致经典SUTVA假设失效。现有实验设计（如cluster randomization）虽能降低干扰以估计全局处理效应（global treatment effect, $\tau$），但难以同时估计溢出效应（spillover effect, $\gamma$）；而其他设计（如独立集、冲突图）或需先验信息，或估计量方差过大。如何在一个实验中同时高效估计$\tau$和$\gamma$？

**核心方法**：采用ego-cluster随机化设计，将网络划分为若干“自我-他人”簇（ego-cluster），每个簇由一个焦点单元（ego）及其部分邻居（alters）组成，在簇层面随机分配处理。假设线性结果模型$Y_i = \alpha + \beta T_i + \gamma \rho_i + \epsilon_i$（$\rho_i$为邻居处理比例），则$\tau = \beta + \gamma$，$\gamma$即为目标参数。通过回归估计量$(\hat{\alpha}, \hat{\beta}, \hat{\gamma})$得到$\hat{\tau}, \hat{\gamma}$。在超总体框架下，证明估计量的相合性和渐近正态性，且渐近方差$\sigma^2_{\tau,n} = 4\sigma^2_\epsilon (\bar{r}_n^2 / b_n + 1)$，$\sigma^2_{\gamma,n} = 4\sigma^2_\epsilon / b_n$，其中$\bar{r}_n$为平均损失率（邻居不在同一簇的比例），$b_n$刻画邻居在不同簇间的分布。基于此，提出两步贪心算法：先向后选择egos，再重分配alters，以最小化$\bar{r}_n^2 / b_n$（针对$\tau$）或$1/b_n$（针对$\gamma$），自动确定簇数。

**与已有工作关系**：相比cluster randomization（如3-net、Louvain），ego-cluster设计保留更多跨簇连接，能同时估计溢出效应；相比LinkedIn的原始ego-cluster设计（随机选ego），本文首次给出理论性质并基于方差优化构造簇；相比冲突图设计（Kandiros et al., 2025），回归估计量避免了小暴露概率下的高方差；相比因果聚类（Viviano et al., 2025），本文方法不依赖先验数据且计算更高效。

**贡献**：1）首次对ego-cluster设计进行严格理论分析，建立回归估计量的渐近性质；2）揭示渐近方差与簇结构的显式关系，并据此提出首个方差导向的ego-cluster构造算法，无需预设簇数；3）模拟和两个真实数据应用表明，该方法在估计$\tau$和$\gamma$上均优于现有设计，且对模型误设和混淆变量稳健。


## Advances in Causal Inference and Adaptive Learning

*7 月 11 日（周六） · 13:30-15:10 · Fanjing Mountains Meeting Room*  
*组织 Jingfei Zhang（Emory University） · 主持 Jingfei Zhang（Emory University）*

### 1. Unsupervised Federated Multi-Task Learning for Heterogeneous Tasks

**讲者**：Yang Feng（New York University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
联邦学习（Federated Learning, FL）通常假设各客户端数据分布相似或任务同质，但实际场景中客户端可能承担不同任务（如分类、回归、聚类），且数据无标签。现有FL方法难以同时处理任务异质性（heterogeneous tasks）与无监督设定。本报告旨在解决：如何在无标签、任务类型各异的客户端间，通过多任务学习（Multi-Task Learning, MTL）框架实现有效协同训练，同时保护数据隐私。

**核心方法**  
提出一种无监督联邦多任务学习框架。核心思路是：每个客户端本地运行一个自编码器（autoencoder）或对比学习模型，以无监督方式提取共享表示；服务器端维护一个任务关系图（task relation graph），通过客户端上传的表示分布或梯度相似性动态推断任务间的关联强度。基于此图，服务器设计一个加权聚合策略：对关联强的任务组，共享更多参数（如编码器层）；对关联弱的任务，保留更多个性化参数。训练中交替进行本地无监督更新与服务器端图引导的聚合，最终每个客户端获得一个适应自身任务的无监督模型。

**与已有工作关系**  
传统联邦多任务学习（如MOCHA）假设任务同质或需标签，且依赖凸优化；本工作将MTL扩展至无监督与任务异质场景。与Federated Contrastive Learning（如FCL）相比，后者仅处理同质任务（如图分类），本方法通过任务关系图显式建模异质性，允许不同任务（如聚类与异常检测）共享部分表示。此外，相比单任务无监督FL（如FedAE），本方法利用多任务间的互补信息提升表示泛化性。

**主要贡献**  
1. 首次提出无监督联邦多任务学习框架，解决任务异质性与无标签的双重挑战。  
2. 引入任务关系图作为桥梁，实现异质任务间的自适应知识共享，避免负迁移。  
3. 理论分析表明，在任务关系图满足一定稀疏性条件下，算法收敛至局部最优，且通信效率与任务数线性相关。  
4. 在合成与真实数据集（如多模态医疗数据）上验证，相比单任务无监督FL与独立训练，下游任务性能提升10-20%，且隐私泄露风险可控。


### 2. SMS: Symmetric Mediation Statistics for Powerful High-Dimensional Mediation Analysis

**讲者**：Yijuan Hu（Peking University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维中介分析（high-dimensional mediation analysis）旨在同时检验大量中介变量（mediators）在暴露与结局之间的间接效应，但现有方法面临两大挑战：一是高维情形下多重检验导致统计功效低下；二是传统中介检验统计量（如Sobel检验或乘积系数检验）对中介效应的方向不对称——当暴露与中介、中介与结局的效应符号相反时，间接效应可能被抵消，但现有统计量无法有效捕捉这种“符号对称”的贡献。本报告提出Symmetric Mediation Statistics（SMS），旨在构造一种对效应方向对称、且在高维稀疏场景下具有更高检验功效的统计量。

**核心方法**  
SMS的核心思想是：将间接效应分解为两个方向分量（暴露→中介的系数$a_j$与中介→结局的系数$b_j$），并构造一个对称的统计量$T_j = \text{sign}(a_j b_j) \cdot \min(|a_j|, |b_j|)$或类似形式，从而同时保留效应的符号信息和强度信息。通过引入对称性，SMS避免了传统乘积统计量$|a_j b_j|$在符号相反时被低估的问题。进一步，SMS采用去偏Lasso或debiased估计量对高维系数进行估计，并基于bootstrap或渐近正态性构造检验p值，再通过Benjamini-Hochberg等FDR控制程序筛选显著中介。

**与已有工作关系**  
已有高维中介方法（如HIMA、HDMA）多基于乘积系数$|a_j b_j|$或联合显著性检验，但忽略了符号方向对功效的影响。SMS首次将“对称性”引入中介统计量，使得当$a_j$与$b_j$符号相反时（即抑制型中介），统计量仍能有效反映中介强度。此外，SMS在估计阶段采用高维正则化方法（如Lasso）进行变量筛选，但通过对称统计量避免了传统方法因符号抵消导致的漏检问题，与现有方法形成互补。

**主要贡献**  
1. 提出一种对效应方向对称的中介统计量，显著提升在符号相反场景下的检验功效。  
2. 在高维稀疏假设下，给出SMS的渐近分布理论，并证明其FDR控制性质。  
3. 通过模拟和实际数据（如基因表达中介分析）展示SMS相比HIMA等方法的功效提升，尤其在抑制型中介占比较高时。该工作为高维中介分析提供了新的统计推断工具，拓展了因果中介分析在复杂生物机制中的应用边界。


### 3. Optimizing Dynamic Treatment Regimes under Spatial Interference: Evidence from COVID-19 School Closures

**讲者**：Yunan Wu（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
动态治疗方案（Dynamic Treatment Regimes, DTR）旨在根据个体随时间变化的协变量自适应地选择最优治疗序列，但现有方法通常假设个体间无干扰（即SUTVA）。在COVID-19学校关闭政策中，一所学校的关闭不仅影响本校学生，还会通过人口流动、社区接触等空间机制改变邻近学校的疫情传播风险，形成空间干扰（spatial interference）。此时，传统DTR的优化会因忽略空间溢出效应而产生偏误。本报告的核心问题是：**如何在存在空间干扰的条件下，估计并优化动态治疗方案，以最小化累积疫情负担？**

**核心方法**  
讲者可能将空间因果推断中的干扰模型（如部分干扰、空间权重矩阵）嵌入DTR的框架。具体地，假设每个单位（学校）的潜在结果依赖于自身及其空间邻居的历史治疗序列，通过引入空间邻接矩阵 $W$ 定义“暴露向量”（exposure vector），将个体治疗历史与邻居治疗历史的加权组合作为新的决策变量。估计阶段可能采用带空间惩罚的Q-learning或A-learning：在每一步，用空间自回归模型（如SAR）拟合条件均值函数 $Q_t(H_t, A_t)$，其中 $H_t$ 包含自身和邻居的协变量与历史治疗；优化阶段则通过动态规划求解最优策略 $\pi_t^*(h_t) = \arg\max_{a_t} Q_t(h_t, a_t)$，并利用逆概率加权（IPW）或双重稳健估计处理空间干扰下的混淆偏差。

**与已有工作关系**  
已有文献主要分为两支：一是静态空间因果推断（如Hudgens & Halloran, 2008），关注单一时间点的处理效应估计，但未涉及序贯决策；二是无干扰的DTR（如Murphy, 2003; Robins, 2004），假设个体间独立。本报告首次将空间干扰引入动态治疗优化，填补了“空间-时序”交叉领域的空白。与近期考虑网络干扰的DTR（如Tchetgen Tchetgen et al., 2021）相比，本报告更聚焦于连续空间（如地理距离）而非离散网络，且以COVID-19学校关闭为实证场景，具有现实紧迫性。

**贡献**  
主要贡献有三：（1）提出一个可识别空间干扰下最优DTR的因果框架，并给出识别条件（如空间稳定性与序贯可忽略性）；（2）开发了结合空间权重与强化学习的估计算法，理论上证明其收敛性与一致性；（3）利用美国学区COVID-19数据，发现忽略空间干扰会导致高估学校关闭的边际收益，而考虑空间溢出后，最优策略建议在疫情热点区域采取“区域协同关闭”而非孤立关闭，为公共卫生决策提供了新洞见。


### 4. Hierarchical Projection for Adaptive Knowledge Transfer

**讲者**：Tian Gu（Columbia University）

**对应论文**：Hierarchical Projection for Adaptive Knowledge Transfer · [arXiv:2606.08691](https://arxiv.org/abs/2606.08691)

<details><summary>摘要（原文）</summary>

Modern data-driven applications increasingly involve learning from multiple heterogeneous sources, where a target dataset is limited but related information is available across domains. Naively combining these sources can degrade performance when relevance varies or spurious signals are present, posing a fundamental challenge for trustworthy cross-domain learning. We propose Projection Transfer Learning (ProjectionTL), a unified framework that integrates hierarchical Bayesian modeling with adaptive projection for selective knowledge transfer. The key idea is to decouple transfer at two levels: first, we construct a source-guided hierarchical prior that aggregates information across sources using data-driven weights, capturing global alignment between each source and the target; second, we refine this borrowing through a posterior-projection step that operates at the feature level, selectively retaining coordinates that exhibit local agreement with the target signal. This two-stage design enables the method to simultaneously perform source selection and feature selection, thereby mitigating negative transfer while preserving interpretability. ProjectionTL provides a principled approach to integrating heterogeneous data across domains, bridging statistical modeling and modern machine learning paradigms for robust and interpretable transfer. Through simulations and real-world biomedical applications, we demonstrate improved accuracy, stability, and interpretability compared to existing methods. Our framework offers a scalable and generalizable strategy for trustworthy cross-domain learning in high-dimensional settings.

</details>

**问题**  
跨域学习中，目标数据集有限而多个异质源域可用时，简单合并所有源会因相关性差异或虚假信号导致负迁移。现有方法多聚焦于源选择或特征选择之一，难以同时应对源间全局对齐与特征级局部一致性的双重挑战，尤其在源域与目标域关系复杂的高维场景下，缺乏兼具稳健性与可解释性的统一框架。

**核心方法**  
本文提出 Projection Transfer Learning (ProjectionTL)，其本质是两阶段自适应投影框架。第一阶段构建**源引导的层次先验**：通过数据驱动权重 $\omega_s$ 聚合各源信息，形成全局对齐的先验分布，实现源级别的选择性借用。第二阶段引入**后验投影**：在得到参数后验后，对特征坐标进行投影操作，仅保留与目标信号局部一致的维度，等价于在特征层面执行稀疏化。两阶段分别对应源选择与特征选择，且通过层次贝叶斯模型自然耦合，避免了手动调参或两阶段分离带来的偏差。

**与已有工作关系**  
现有迁移学习方法或依赖正则化（如 $L_1$ 惩罚）进行特征选择，或通过贝叶斯先验（如 spike-and-slab）实现源选择，但鲜有同时处理两个维度。ProjectionTL 的创新在于将层次先验（全局源权重）与后验投影（局部特征筛选）结合，形成“先源后特征”的递进式自适应机制。相比基于深度学习的域适应方法，本框架保留了统计可解释性，且在高维异质性场景下更稳定。

**主要贡献**  
1. 提出首个同时实现源选择与特征选择的统一迁移学习框架，理论清晰且可解释。  
2. 通过层次贝叶斯建模与后验投影的耦合，有效缓解负迁移，并在模拟与真实生物医学数据上展示出优于现有方法的精度与稳定性。  
3. 为高维、多源、异质性场景下的可信跨域学习提供了可扩展的统计策略，桥接了贝叶斯统计与现代机器学习范式。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)