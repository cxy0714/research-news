# 金融与计量经济 Finance & Econometrics · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 4 场）

---

## Advances in Economic and Social Data Science

*7 月 13 日（周一） · 15:30-17:10 · Colourful Guizhou Ballroom 3*  
*主持 Lingling Tian（Beijing University of Technology）*

### 1. 宏观审慎管理、房地产市场发展与系统性金融风险

**讲者**：Hui Wei（Xinjiang University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
宏观审慎管理旨在防范系统性金融风险，而房地产市场作为信贷周期的重要载体，其波动常被视为风险积聚的关键来源。然而，现有研究多聚焦于单一政策工具（如贷款价值比LTV）或单一风险指标（如房价增速），缺乏对“宏观审慎政策—房地产市场—系统性风险”这一完整传导链条的因果识别。本报告试图回答：不同宏观审慎工具（如债务收入比DTI、逆周期资本缓冲）如何通过影响房地产信贷扩张与资产价格，进而改变银行体系的尾部关联性与系统性风险水平？

**核心方法**  
讲者可能采用**双重差分**（DID）或**工具变量**（IV）策略，利用中国城市层面或银行层面的面板数据，识别宏观审慎政策冲击的外生性。例如，以政策实施的时间与地区差异构造处理组与对照组，估计政策对房价、信贷增速的局部平均处理效应（LATE）。进一步，通过**高维网络模型**（如LASSO估计的银行间风险敞口矩阵）或**CoVaR**、**SRISK**等系统性风险测度，将政策效果映射至尾部依赖结构，量化风险溢出强度的变化。若数据维度较高，可能引入**双重机器学习**（DML）或**因果森林**以处理高维协变量下的选择偏误。

**与已有工作关系**  
已有文献多从宏观视角检验宏观审慎政策对信贷周期或房价的抑制效果（如Claessens et al., 2013），或单独分析房地产市场与银行危机的关系（如Mian & Sufi, 2018）。本报告的可能创新在于：将政策评估与系统性风险建模结合，不仅估计平均处理效应，更关注政策对风险分布尾部的影响；同时，区别于仅使用时间序列的跨国研究，利用中国城市间政策差异提供更干净的识别。

**贡献**  
第一，为宏观审慎政策的有效性提供因果证据，尤其是区分不同工具（如数量型与价格型）的异质性效果。第二，揭示房地产市场波动向金融系统传导的机制路径，例如通过抵押品价值渠道或银行信贷渠道。第三，为监管者设计“逆周期”政策提供量化参考：在房价高涨期，何种工具组合能最有效地降低系统性风险，同时避免过度抑制合理住房需求。


### 2. 社会核算矩阵稳态均衡模型研究

**讲者**：Ke Liang（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
社会核算矩阵（Social Accounting Matrix, SAM）是刻画国民经济各部门间资金流与收入分配关系的方阵，其行和与列和分别对应各账户的总收入与总支出。传统SAM研究多聚焦于数据平衡调整（如RAS方法）或作为可计算一般均衡（CGE）模型的基期数据，但缺乏对SAM自身动态演化至稳态均衡的严格理论分析。本报告旨在回答：给定一个初始不平衡的SAM，是否存在一个稳态均衡状态（即行和等于列和且满足某种经济一致性条件）？若存在，其唯一性与收敛性如何刻画？

**核心方法**  
讲者可能将SAM视为一个线性系统，引入稳态均衡定义为存在一个正向量 $\mathbf{x}$ 使得 $A\mathbf{x} = \lambda \mathbf{x}$，其中 $A$ 为SAM的系数矩阵（或经过标准化后的转移概率矩阵），$\lambda$ 为最大特征值（Perron-Frobenius根）。通过Perron-Frobenius定理，非负不可约矩阵存在唯一正特征向量，该向量可解释为稳态下的账户规模。进一步，讲者可能构造一个迭代映射（如幂法或RAS型迭代）来逼近该稳态，并证明其收敛性依赖于矩阵的谱半径条件。此外，可能引入熵正则化或最小信息损失准则，将稳态求解转化为一个凸优化问题。

**与已有工作关系**  
已有SAM平衡方法（如RAS、交叉熵法）本质上是在给定行和与列和约束下调整矩阵元素，属于静态校准。而本报告将SAM视为一个动态系统，研究其内在的稳态性质，类似于投入产出模型中Leontief逆矩阵的收敛性分析，但扩展到更一般的非对称SAM结构。与CGE模型相比，本报告不依赖具体生产函数与效用函数，而是直接从矩阵代数角度给出均衡存在的充分条件，更接近图论与马尔可夫链的视角。

**主要贡献**  
1. 首次将Perron-Frobenius理论系统引入SAM稳态均衡分析，为SAM的“内在一致性”提供严格数学定义。  
2. 提出一种基于特征向量迭代的数值算法，可同时实现数据平衡与稳态识别，避免传统两步法（先平衡再模拟）的信息损失。  
3. 给出稳态均衡存在性与唯一性的可检验条件（如矩阵不可约性与非奇异性），为实际SAM构建提供理论指导。  
4. 通过经济解释（如稳态对应长期均衡的账户规模比例），架起了SAM与一般均衡理论之间的桥梁。


### 3. 基于SEEA-EA海洋生态系统核算的国际标准、国外实践及启示

**讲者**：Yue Gu（Shanxi University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
海洋生态系统为人类社会提供渔业、碳汇、旅游等关键服务，但其价值长期游离于国民经济核算体系之外，导致资源过度开发与生态退化。SEEA-EA（System of Environmental-Economic Accounting—Ecosystem Accounting）作为联合国统计委员会推荐的国际标准，已为陆地生态系统核算提供框架，但海洋生态系统的空间异质性、流动性及跨域特征使得直接套用面临挑战。本报告旨在回答：如何将SEEA-EA标准适配于海洋场景？国际先行国家（如澳大利亚、荷兰）的实践提供了哪些可迁移的经验？对中国构建海洋生态核算体系有何具体启示？

**核心方法**  
报告以SEEA-EA的“生态系统资产—服务—受益者”三层逻辑为骨架，重点解决海洋核算中的两个统计难题：一是**空间单元划分**，采用海洋生态区划（如EEZ、大陆架）替代行政边界，并引入$k$-means聚类或网格化方法对生境类型（珊瑚礁、海草床等）进行同质化分区；二是**价值量核算**，综合使用替代成本法、旅行成本法及生产函数法，将海洋服务（如渔业供给、海岸防护）转化为货币单位，并嵌入扩展的投入产出表（$EIO$）中，以追踪服务流对GDP、就业等指标的贡献。此外，报告可能涉及**不确定性量化**，通过Bootstrap或蒙特卡洛模拟评估参数估计的稳健性。

**与已有工作关系**  
现有SEEA-EA技术指南（2012/2021版）主要基于陆地生态系统（森林、湿地）开发，对海洋的潮汐能、海洋碳汇（蓝碳）等独特服务缺乏核算规则。国际实践方面，澳大利亚已率先编制海洋生态系统账户，但其方法依赖高分辨率遥感数据，对数据稀缺的发展中国家适用性有限。本报告在对比多国案例时，特别关注了**数据可得性约束下的简化策略**（如用代理变量替代直接测量），并指出中国现有海洋统计调查（如渔业统计、海洋经济公报）与SEEA-EA账户的衔接缺口，这比单纯介绍标准更贴近实际应用。

**主要贡献**  
1. **方法论适配**：系统梳理了海洋核算中空间尺度选择、服务分类调整及价值化技术的关键差异，为统计研究者提供了从陆地到海洋的迁移路径。  
2. **国际经验本土化**：提炼出“先试点后推广”的渐进策略，建议优先核算渔业与滨海旅游两类数据基础较好的服务，并利用中国已有的海洋生态红线数据作为资产边界。  
3. **政策启示**：指出海洋核算结果可服务于蓝色GDP测算、生态补偿标准制定及海洋空间规划，为统计部门与海洋管理机构的协作提供了可操作框架。


### 4. Precision Matrix Estimation for Multiple Compositional Vectors

**讲者**：Shen Zhang（Qufu Normal University）

**对应论文**：CARE: Large Precision Matrix Estimation for Compositional Data · [arXiv:2309.06985](https://arxiv.org/abs/2309.06985)

<details><summary>摘要（原文）</summary>

High-dimensional compositional data are prevalent in many applications. The simplex constraint poses intrinsic challenges to inferring the conditional dependence relationships among the components forming a composition, as encoded by a large precision matrix. We introduce a precise specification of the compositional precision matrix and relate it to its basis counterpart, which is shown to be asymptotically identifiable under suitable sparsity assumptions. By exploiting this connection, we propose a composition adaptive regularized estimation (CARE) method for estimating the sparse basis precision matrix. We derive rates of convergence for the estimator and provide theoretical guarantees on support recovery and data-driven parameter tuning. Our theory reveals an intriguing trade-off between identification and estimation, thereby highlighting the blessing of dimensionality in compositional data analysis. In particular, in sufficiently high dimensions, the CARE estimator achieves minimax optimality and performs as well as if the basis were observed. We further discuss how our framework can be extended to handle data containing zeros, including sampling zeros and structural zeros. The advantages of CARE over existing methods are illustrated by simulation studies and an application to inferring microbial ecological networks in the human gut.

</details>

**问题**：高维成分数据（compositional data）受单纯形约束，其精度矩阵（precision matrix）的估计面临根本性挑战：传统对数比变换导致协方差矩阵奇异或不可逆，且无法直接定义稀疏且可解释的成分精度矩阵。核心困难在于，生成成分的潜在基变量（basis）的精度矩阵 $\Omega_0$ 虽具有稀疏性和图模型解释，但由成分数据无法唯一识别。

**核心方法**：本文提出CARE（Composition Adaptive Regularized Estimation）方法。首先，通过中心化对数比协方差矩阵 $\Sigma_c$ 的Moore–Penrose逆，规范定义成分精度矩阵 $\Omega_c$，并建立其与 $\Omega_0$ 的显式关系：$\Omega_c = \Omega_0 - \frac{\Omega_0 \mathbf{1}_p \mathbf{1}_p^\top \Omega_0}{\mathbf{1}_p^\top \Omega_0 \mathbf{1}_p}$。该分解表明 $\Omega_c$ 是 $\Omega_0$ 加上一个秩一修正项。基于此，CARE采用约束 $\ell_1$ 最小化（类似CLIME）直接估计 $\Omega_0$：$\min \|\Omega\|_1$ subject to $\|\hat{\Sigma}_c \Omega - G\|_{\max} \leq \lambda$，其中 $G = I_p - p^{-1}\mathbf{1}_p\mathbf{1}_p^\top$。理论证明，当维度 $p$ 满足 $M_p = o(\sqrt{p})$ 时，识别误差 $O(M_p^2/\sqrt{p})$ 随 $p$ 增大而衰减；若进一步 $M_p = o(\sqrt{p \log p / n})$，则估计误差主导，CARE达到与观测到基变量时相同的minimax最优速率，体现了“维度祝福”。

**与已有工作关系**：现有方法如SPIEC-EASI、gCoda、CD-trace等或缺乏严格理论（如直接对变换后数据应用图模型），或依赖不可检验的交换性条件。本文首次严格建立了成分精度矩阵与基精度矩阵的联系，并证明了近似可识别性，填补了Cao, Lin, Li (2019)在协方差估计工作后的精度矩阵空白。与一般低秩加稀疏恢复问题不同，本文秩已知且无需估计，且不满足尖峰特征值假设。

**主要贡献**：1) 提出了成分精度矩阵的规范定义并建立了与基精度矩阵的显式低秩加稀疏关系；2) 证明了高维下基精度矩阵的近似可识别性，揭示了识别与估计之间的权衡及维度祝福；3) 提出了CARE方法，给出了在谱范数、$\ell_1$范数和Frobenius范数下的收敛速率，以及支持恢复和自适应调参的理论保证；4) 模拟和微生物组数据应用表明CARE显著优于现有方法，且在高维下性能接近Oracle。


### 5. 退市制度改革能够提高企业投资效率吗？ ——来自壳资源企业的证据

**讲者**：Dejin Tao（Xinjiang University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
中国退市制度改革旨在清理“壳资源”乱象，但其对壳资源企业投资效率的因果效应尚不明确。传统研究多关注退市制度对市场定价或壳价值的影响，而企业投资效率（如过度投资或投资不足）作为资源配置的关键指标，是否因制度冲击而改善，缺乏严谨的因果识别。本报告聚焦于：退市制度改革是否通过压缩壳价值、降低保壳动机，从而提升壳资源企业的投资效率？

**核心方法**  
采用双重差分（Difference-in-Differences, DID）框架，以退市制度改革（如2012年、2018年等关键政策节点）作为外生冲击，将壳资源企业（如连续亏损、市值低、有保壳压力的公司）设为处理组，非壳资源企业（或匹配后的对照组）设为对照组。投资效率通过 Richardson（2006）模型残差度量，即实际投资与预期投资的偏离绝对值。为缓解选择偏误，使用倾向得分匹配（Propensity Score Matching, PSM）或逆概率加权（IPW）构造可比样本，并控制企业固定效应与年份固定效应。识别假设为：在无政策干预下，处理组与对照组的投资效率趋势平行（parallel trends），且政策冲击仅通过壳价值渠道影响投资效率（排除其他同期政策干扰）。

**与已有工作关系**  
已有文献多从壳价值估值（如IPO抑价、借壳上市溢价）或市场反应（如股价崩盘风险）角度评估退市制度改革，较少直接检验其对微观企业投资行为的因果效应。部分研究关注退市制度对盈余管理或分红行为的影响，但投资效率作为长期资源配置的代理变量，其因果链条尚未被严格识别。本报告将DID与PSM结合，弥补了现有研究在因果推断上的不足，并回应了“制度变革如何影响企业真实投资决策”这一更广义的公司金融问题。

**贡献**  
1. **因果识别创新**：利用政策外生冲击，通过平行趋势检验和安慰剂检验（如随机分配处理组）增强因果推断可信度，为退市制度的经济后果提供干净证据。  
2. **机制揭示**：区分过度投资与投资不足，检验壳价值下降是否通过降低管理层保壳的短视行为（如削减研发、变卖资产）来优化投资效率，揭示“制度→壳价值→投资效率”的传导路径。  
3. **政策启示**：为监管层优化退市标准（如财务指标与交易指标结合）提供微观基础，同时提醒投资者关注壳资源企业投资效率在制度变革中的动态变化。


### 6. Estimation for Partially Time-Varying Spatial Autoregressive Panel Data Model under Linear Constraints

**讲者**：Lingling Tian（Beijing University of Technology）

**对应论文**：Statistical inference of partially linear time-varying coefficients spatial autoregressive panel data model · [arXiv:2410.10647](https://arxiv.org/abs/2410.10647)

<details><summary>摘要（原文）</summary>

This paper investigates a partially linear spatial autoregressive panel data model that incorporates fixed effects, constant and time-varying regression coefficients, and a time-varying spatial lag coefficient. A two-stage least squares estimation method based on profile local linear dummy variables (2SLS-PLLDV) is proposed to estimate both constant and time-varying coefficients without the need for first differencing. The asymptotic properties of the estimator are derived under certain conditions. Furthermore, a residual-based goodness-of-fit test is constructed for the model, and a residual-based bootstrap method is used to obtain p-values. Simulation studies show the good performance of the proposed method in various scenarios. The Chinese provincial carbon emission data set is analyzed for illustration.

</details>

**问题**  
现有空间面板数据模型多假设空间滞后系数或回归系数为常数，或允许全部系数时变（如 Chang et al. 2024），但后者在高维协变量下遭遇“维数诅咒”。实际应用中，部分解释变量的影响可能随时间稳定，而另一些则动态变化。本文针对**部分线性时变系数空间自回归面板数据模型**，在存在固定效应和部分系数为常数的线性约束下，解决如何同时估计时变系数、常数系数以及时变空间滞后系数的问题，并检验哪些系数应视为常数。

**核心方法**  
提出**基于 profile 局部线性虚拟变量的两阶段最小二乘估计（2SLS-PLLDV）**。第一阶段：选取工具变量 $H = (X, WX, W^2X)$，对空间滞后项 $WY$ 进行局部线性虚拟变量回归（LLDV），得到其估计 $\hat{Y}_w$，从而消除内生性。第二阶段：将 $\hat{Y}_w$ 代入原模型，对时变系数部分 $\gamma_v(\tau_t) = (\rho(\tau_t), \beta_v^\top(\tau_t))^\top$ 再次使用 LLDV 得到 profile 估计，对常数系数 $\beta_c$ 则通过 profile 最小二乘得到。该方法无需一阶差分，直接利用虚拟变量吸收固定效应，并借助核光滑处理时变系数。

**与已有工作关系**  
相比 Chang et al. (2024) 的全时变模型，本文引入部分线性结构，在保持灵活性的同时缓解维数灾难。与 Sun & Malikov (2018) 的功能系数模型不同，本文系数随时间而非协变量变化。与 Liang et al. (2022) 的局部线性 QML 方法相比，本文采用 2SLS 框架，避免对误差分布作强假设，且能处理固定效应。此外，本文还构建了基于残差平方和的检验统计量，用于判断部分系数是否应设为常数，并借助 bootstrap 获取 p 值。

**主要贡献**  
1. 提出一类更灵活且可估计的部分线性时变系数 SAR 面板数据模型，平衡了模型复杂度和可解释性。  
2. 发展 2SLS-PLLDV 估计方法，在温和条件下证明了常数系数估计的 $\sqrt{NT}$ 渐近正态性和时变系数估计的 $\sqrt{NTh}$ 渐近正态性。  
3. 构造了基于残差平方和的拟合优度检验，用于识别时变与常数系数，并给出 bootstrap 实现。  
4. 通过模拟验证了方法在有限样本下的优良表现，并应用于中国省级碳排放数据，揭示了空间自回归系数和部分回归系数的时变特征，为政策分析提供了统计工具。


## Theoretical Econometrics

*7 月 13 日（周一） · 08:30-10:10 · Qunsheng Room*  
*主办 IMS China · 组织 Fang Han（University of Washington, Seattle） · 主持 Fang Han（University of Washington, Seattle）*

### 1. The Optimal Selection of a Subset and the Roles of Testing

**讲者**：Lilun Du（City University of Hong Kong）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在统计推断中，从候选变量或特征中挑选一个最优子集是模型选择与高维推断的核心任务。传统方法（如AIC、BIC、Lasso）侧重预测误差或稀疏性，但往往忽略子集选择过程中的**不确定性量化**与**错误控制**。本报告聚焦于：在给定某种最优性准则（如最小化某种风险或最大化某种效用）下，如何同时利用假设检验来保证所选子集的统计可靠性？即，检验在子集选择中究竟扮演什么角色——是作为选择后的验证，还是作为选择过程中的内置机制？

**核心方法**  
讲者可能提出一个**两阶段或联合框架**：第一阶段基于某种损失函数（如平方损失或0-1损失）求解最优子集，第二阶段利用多重检验（如FDR控制或FWER控制）对所选子集中的每个变量进行显著性检验，并调整选择阈值以平衡“最优性”与“检验功效”。方法本质是将子集选择视为一个**带约束的优化问题**，其中约束条件来自检验的显著性水平或错误发现率。例如，可能构造一个目标函数 $L(S) + \lambda \cdot \text{FP}(S)$，其中 $L(S)$ 是子集 $S$ 的预测损失，$\text{FP}(S)$ 是假阳性数，通过调整 $\lambda$ 实现最优性与检验角色的权衡。

**与已有工作关系**  
已有工作如“最优子集选择”（best subset selection）通常只关注预测或估计的准确性，而“多重检验”则独立处理变量显著性。本报告试图弥合这两条路线：不同于Lasso等正则化方法隐式地通过惩罚项控制假阳性，这里显式地将检验的统计量或p值纳入选择准则，从而在理论上保证所选子集在某种最优意义下同时具有**可解释的误差控制**。与“选择性推断”（selective inference）不同，后者关注选择后条件推断，而本报告可能更关注选择过程的**事前最优性**。

**贡献**  
主要贡献在于：1）为子集选择问题提供了一个**统一的最优性框架**，将检验的角色从事后验证提升为选择准则的组成部分；2）可能推导出在给定检验水平下最优子集选择的**有限样本理论保证**（如oracle性质或minimax最优性）；3）为高维统计中“预测”与“推断”的融合提供了新视角，启发后续研究如何设计同时兼顾预测精度与错误控制的自适应选择算法。


### 2. Second-Order Sparse Sufficient Dimension Reduction with Applications to Quadratic Discriminant Analysis

**讲者**：Jing Zeng（University of Science and Technology of China）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
在高维分类问题中，二次判别分析（QDA）需要估计类内协方差矩阵的逆，当维度 $p$ 远大于样本量 $n$ 时，传统估计失效。充分降维（Sufficient Dimension Reduction, SDR）通过寻找低维子空间保留分类信息，但现有稀疏SDR方法（如Sparse SIR、Sparse SAVE）主要捕捉一阶矩（均值差异），无法有效处理QDA所需的二阶矩（协方差差异）结构。因此，如何在高维稀疏假设下同时实现二阶矩的充分降维，并直接服务于QDA，是核心挑战。

**核心方法**  
提出一种二阶稀疏充分降维方法（Second-Order Sparse SDR）。该方法基于逆回归框架，将中心子空间（central subspace）的估计转化为对条件协方差矩阵 $ \text{Cov}(X \mid Y) $ 的稀疏分解。具体地，对每个类别 $k$，假设类内协方差矩阵 $\Sigma_k$ 在某个低维子空间上具有稀疏特征向量结构，通过惩罚似然（如 $\ell_1$ 或SCAD）同时估计公共的降维方向与稀疏载荷。降维后的低维变量 $Z = B^\top X$ 满足 $X \perp Y \mid Z$，且 $B$ 的列向量仅有少量非零元素。随后在 $Z$ 空间上执行QDA，避免高维协方差矩阵的直接求逆。

**与已有工作关系**  
已有稀疏SDR（如Li, 2007; Bondell & Li, 2009）主要针对一阶矩（如SIR）或线性判别，而本工作首次将稀疏性引入二阶矩降维，专门适配QDA的非线性（二次）决策边界。相比传统的全协方差QDA（如Friedman, 1989），本方法通过降维和稀疏性实现高维可操作；相比基于核的SDR（如Kernel SIR），本方法保持线性可解释性并显式利用二阶结构。

**贡献**  
1. 提出首个针对二阶矩的稀疏充分降维框架，填补了稀疏SDR在二阶结构上的空白。  
2. 在正则条件下证明估计量的相合性及稀疏恢复性（如 $ \| \hat{B} - B \|_F = O_p(\sqrt{s \log p / n}) $，$s$ 为真实非零系数个数）。  
3. 将降维与QDA无缝衔接，理论推导降维后QDA的Bayes风险收敛速率，并给出变量选择一致性。  
4. 数值实验表明，在超高维模拟和实际数据（如基因表达、图像分类）中，该方法在分类精度和变量可解释性上显著优于Sparse SIR、Sparse SAVE及正则化QDA。


### 3. Score Test for Order of Finite Normal Mixtures

**讲者**：Junfan Tao（Kyoto University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
有限正态混合模型（Finite Normal Mixture）的阶数（即成分个数）是模型选择的核心难题。传统似然比检验（LRT）因参数在零假设下处于边界（如混合比例为零）而违反正则条件，导致检验统计量渐近分布非标准，且计算复杂。本报告旨在提出一种基于得分检验（Score Test）的解决方案，用于检验零假设 $H_0: \text{阶数为 } k$ 对备择 $H_1: \text{阶数大于 } k$，从而避免直接估计高阶模型下的 MLE。

**核心方法**  
得分检验仅需在零假设下计算对数似然关于“额外成分”参数的一阶导数（得分函数），并构造二次型统计量。具体地，将 $k+1$ 阶混合模型视为 $k$ 阶模型嵌入一个“冗余成分”，其混合比例 $\pi_{k+1}=0$ 且均值方差与某现有成分重合。此时得分函数在零假设下退化为零，但通过引入适当的惩罚或正则化（如对参数空间施加约束），可得到非退化的检验统计量。报告可能推导该统计量的渐近分布（如 $\chi^2$ 或混合 $\chi^2$），并给出基于 bootstrap 的有限样本校正。

**与已有工作关系**  
已有工作多聚焦于 LRT 的修正（如调整临界值或使用 EM 算法下的 bootstrap），或基于信息准则（AIC/BIC）的模型选择。得分检验的优势在于计算量小——无需拟合高阶模型，且可避免 LRT 中因参数边界导致的分布复杂化。与 Chen & Li (2009) 的修正 LRT 相比，得分检验可能对局部备择假设更敏感；与基于 EM 的 score test（如 Liang & Rathouz, 1999）相比，本报告可能专门处理正态混合的阶数问题，并给出显式的渐近理论。

**贡献**  
1. 提出一种计算高效的阶数检验方法，仅需 $k$ 阶模型的 MLE，适用于大规模数据。  
2. 严格证明检验统计量在零假设下的渐近分布，并处理参数不可识别（identifiability）带来的技术困难。  
3. 通过模拟和实际数据展示该方法在控制第一类错误和检验功效上优于现有 LRT 变体，尤其当成分分离度较小时。  
4. 为混合模型阶数选择提供了一种新的推断工具，可推广至其他指数族混合。


## Microeconometrics

*7 月 13 日（周一） · 13:30-15:10 · Doupeng Mountains Meeting Room*  
*组织 Ying Fang（Xiamen University） · 主持 Ming Lin（Xiamen University）*

### 1. Estimating Intergenerational Mobility via a Time-Varying Mixed Copula Method

**讲者**：Zongwu Cai（University of Kansas）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
代际流动性（intergenerational mobility）衡量父代与子代经济地位（如收入、教育）的关联强度，传统方法多假设该关联在时间上恒定，或仅通过线性回归系数（如弹性系数）刻画。然而，实际中流动性可能随经济周期、政策变迁而动态演化，且父代与子代分布常呈现非对称尾部依赖（如“贫困陷阱”与“富裕固化”并存）。现有模型难以同时捕捉时变性与非线性依赖结构。

**核心方法**  
报告提出一种**时变混合Copula方法**（Time-Varying Mixed Copula Method）。首先，用混合Copula族（如Clayton与Gumbel的凸组合）刻画父代与子代收入/教育等级的联合分布，其中不同Copula分量分别捕捉下尾依赖（低流动性）和上尾依赖（高流动性）。其次，允许混合权重及Copula参数随时间平滑变化，通过局部似然（local likelihood）或核加权估计实现非参数时变推断。最终，代际流动性指标（如秩-秩斜率、持久性弹性）可由Copula的时变参数导出。

**与已有工作关系**  
已有文献多采用固定参数Copula（如Dardanoni et al., 2012）或分位数回归（Chetty et al., 2014）分析代际流动性，但前者忽略时变性，后者难以直接建模尾部依赖。本报告将时变Copula引入代际流动性领域，并利用混合结构区分不同依赖模式，是对传统线性回归与静态Copula的实质性拓展。

**贡献**  
1. 方法论上，首次将时变混合Copula用于代际流动性估计，允许依赖结构随经济环境动态调整，且无需预先指定参数变化形式。  
2. 实证上，可揭示流动性在时间维度上的非单调变化（如金融危机后下尾依赖增强），并识别不同分位点流动性的异质性趋势。  
3. 为政策评估提供更精细的工具：例如，若发现上尾依赖增强，则表明顶层收入固化加剧，需针对性干预。


### 2. Estimating Counterfactual Distributions under Staggered Adoption in Short Panels

**讲者**：Ming Lin（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在交错采用（staggered adoption）的短面板（short panels）中，处理组单位在不同时间点接受处理，且时间维度 $T$ 较小。现有方法多聚焦于平均处理效应（ATT）的估计，但政策评估常需了解整个反事实分布（如分位数效应、不平等指标）。该报告旨在解决：如何在短面板、交错处理的设定下，识别并估计反事实分布 $F_{Y(0)}$ 与 $F_{Y(1)}$，从而得到分布处理效应（distributional treatment effects）。

**核心方法**  
报告可能提出一种基于双重稳健（doubly robust）思想的分布回归方法。具体地，利用面板数据的个体固定效应，假设处理前的结果分布满足某种“分布平行趋势”（distributional parallel trends）——即处理组与对照组在无处理时，其分位数函数或累积分布函数的差异随时间恒定。通过引入倾向得分（propensity score）与结果回归模型，构造逆概率加权（IPW）与回归调整的复合估计量，对每个时间点上的反事实分布进行插补。对于短面板，可能采用参数化或半参数化的分位数回归模型（如 quantile regression with fixed effects），并利用交错处理带来的多个处理前时间点进行校准。

**与已有工作关系**  
已有文献主要分为两类：一是处理效应分布估计（如 Callaway & Sant’Anna 2021 的 group-time average treatment effect），但多限于均值或特定分位数；二是交错处理下的 DID 方法（如 Goodman-Bacon, Sun & Abraham），但未扩展到分布层面。该报告将“分布平行趋势”假设引入交错设定，并借鉴双重稳健估计框架（如 Sant’Anna & Zhao 2020）处理高维协变量与短面板的有限样本偏差，弥补了现有方法在分布推断上的空白。

**贡献**  
1. 首次在交错采用短面板中系统提出反事实分布估计框架，允许处理时间异质性。  
2. 给出估计量的渐近性质（一致性、渐近正态性），并讨论短面板下偏差校正策略。  
3. 提供实证应用（如最低工资政策对工资分布的影响），展示方法在政策评估中的实用性。


### 3. 提升面板数据模型中PCA估计量的稳健性

**讲者**：Liangjun Su（Tsinghua University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在大规模面板数据中，因子模型常通过主成分分析（PCA）估计潜因子与载荷。然而，经典PCA估计量对异常值、厚尾分布或截面相依的异质性扰动极为敏感，导致因子恢复与后续推断（如共同相关效应估计）出现严重偏差。本报告旨在解决“如何在存在污染数据或非高斯误差时，仍能获得一致且渐近正态的因子与载荷估计”这一核心问题。

**核心方法**  
讲者提出一种**稳健化PCA**框架，核心思路是将传统最小二乘型损失函数替换为Huber损失或分位数损失，并引入自适应权重以抑制极端观测的影响。具体地，通过迭代重加权最小二乘（IRLS）或凸优化算法，同时估计因子、载荷与稳健尺度参数。该方法在理论上证明：当误差分布仅需有限二阶矩（甚至一阶矩）时，估计量仍保持$\sqrt{NT}$收敛速度与渐近正态性，且无需事先知道污染比例。

**与已有工作关系**  
现有文献中，Bai (2009) 的经典PCA要求误差矩条件严格；Bai & Ng (2002) 的因子数选择亦依赖正态近似。近年虽有基于分位数回归的因子模型（如Ando & Bai, 2020），但多聚焦于条件分位数而非均值结构。本报告将稳健估计从截面回归推广至因子模型的双向结构，并首次在统一框架下处理因子与载荷同时受污染的情形，弥补了“稳健主成分”在面板因子模型中理论分析的空白。

**主要贡献**  
1. 提出一类计算可行、理论完备的稳健PCA估计量，放宽了经典PCA对误差分布的苛刻要求。  
2. 建立该估计量在因子与载荷非稀疏、误差可能重尾下的渐近理论，包括一致性、收敛速率与极限分布。  
3. 提供数据驱动的调参准则（如稳健BIC选择截断常数），使方法可直接用于实证研究。该工作为面板数据中异常值普遍存在的场景（如金融收益率、宏观经济指标）提供了可靠的推断工具。


### 4. Marginal Treatment Effect in High Dimension Setting

**讲者**：Yahong Zhou（Shanghai University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
Marginal Treatment Effect (MTE) 是刻画处理效应随未观测异质性（如选择方程中的误差项）连续变化的经典工具，广泛应用于劳动经济学与政策评估。然而，当协变量维度 $p$ 远大于样本量 $n$ 时，传统 MTE 估计依赖低维参数模型或非参数平滑，面临维数灾难与模型误设风险。本报告旨在解决高维设定下 MTE 的识别与估计问题，即如何在 $p \gg n$ 时仍能一致地估计 MTE 曲线，并对其不确定性进行有效推断。

**核心方法**  
报告可能基于 Heckman-Vytlacil 框架，将 MTE 表示为条件期望的导数：$\text{MTE}(x, u) = \mathbb{E}[Y_1 - Y_0 \mid X=x, U=u]$，其中 $U$ 为选择方程中的潜变量。在高维场景下，采用稀疏性假设，利用 Lasso 或 Double/Debiased Lasso 分别估计倾向得分 $\Pr(D=1 \mid X)$ 与条件均值 $\mathbb{E}[Y \mid X, P]$（$P$ 为倾向得分），再通过局部线性回归或级数展开对 $u$ 维度进行平滑。关键步骤是引入正交化（Neyman orthogonality）或交叉拟合（cross-fitting）以消除正则化偏差，从而得到 $\sqrt{n}$ 一致的 MTE 估计量。

**与已有工作关系**  
现有 MTE 文献（如 Heckman & Vytlacil, 2005; Carneiro et al., 2011）主要假设协变量维数固定或采用低维参数化。近年来高维处理效应研究多集中于 Average Treatment Effect (ATE) 或 Quantile Treatment Effect (QTE)，鲜有涉及 MTE 这类连续异质性度量。本报告将高维统计推断技术（如 debiased Lasso）与结构计量模型结合，填补了高维异质性处理效应分析的空白。

**主要贡献**  
1. 提出高维设定下 MTE 的识别条件与稀疏性假设，拓展了 MTE 框架的适用范围。  
2. 给出基于正则化方法的估计量及其渐近性质（如一致性与渐近正态性），并构造点wise 置信区间。  
3. 通过模拟或实证案例展示方法在变量选择与异质性发现中的优势，为高维数据下的政策评估提供新工具。


## Econometrics

*7 月 13 日（周一） · 15:30-17:10 · Doupeng Mountains Meeting Room*  
*组织 Qiwei Yao（London School of Economics and Political Science） · 主持 Baojun Dou（City University of Hong Kong）*

### 1. CP-Factorization for High Dimensional Tensor Time Series and Double Projection Iterations

**讲者**：Guanglin Huang（Southwestern University of Finance and Economics）

**对应论文**：CP-factorization for high dimensional tensor time series and double projection iterations · [arXiv:2606.08560](https://arxiv.org/abs/2606.08560)

<details><summary>摘要（原文）</summary>

We adopt the canonical polyadic (CP) decomposition to model high-dimensional tensor time series. Our primary goal is to identify and estimate the factor loadings in the CP decomposition. We propose a one-pass estimation procedure through standard eigen-analysis for a matrix constructed based on the serial dependence structure of the data. The asymptotic properties of the proposed estimator are established under a general setting as long as the factor loading vectors are linearly independent, allowing the factors to be correlated and the factor loading vectors to be not nearly orthogonal. The procedure adapts to the sparsity of the factor loading vectors, accommodates weak factors, and demonstrates strong performance across a wide range of scenarios. To further reduce estimation errors, we also introduce an iterative algorithm based on a novel double projection approach. We theoretically justify the improved convergence rate of the iterative estimator, and derive the associated limiting distribution. A consistent estimator of the asymptotic variance is also provided, which plays a key role in the related inference problems. All results are validated through extensive simulations and two real data applications.

</details>

**问题**  
高维张量时间序列的建模中，如何从观测数据中识别并估计CP分解（canonical polyadic decomposition）下的因子载荷向量是核心挑战。现有方法（如Han et al., 2024b的HOPE）要求因子载荷近似正交且因子几乎不相关，这在实践中难以保证；而Chang et al. (2023)的矩阵CP因子模型仅适用于矩阵情形，且两步估计引入交叉plug-in误差，难以推广至高阶张量并支持统计推断。

**核心方法**  
本文提出两类估计方法。其一为**一步估计**：基于数据的序列依赖结构构造一个$d_j \times d_j$矩阵$K_{1,2,j}$，其非零特征值对应的特征向量即为因子载荷$a_{i,j}$，仅需标准特征分解，无需迭代。其二为**双投影迭代算法**：利用初始估计将张量数据投影至低维，构造与目标因子相关、与其余因子近似不相关的线性组合$\tilde{\xi}_{t,i}$，再通过阈值化更新载荷估计。该算法在每次迭代中仅需对$d_j$维向量进行阈值化，而非$d_j \times d_{-j}$矩阵，显著降低误差累积，且不依赖因子不相关或载荷近似正交假设。

**与已有工作关系**  
相比Han et al. (2024b)的HOPE方法，本文方法将“因子载荷近似正交”放松为“线性独立”，并允许因子任意相关；相比Chang et al. (2023)的矩阵CP因子模型，本文一步估计直接利用张量结构，避免交叉步骤的plug-in误差，且自然推广至$m \geq 2$阶张量。此外，本文首次为CP因子模型提供完整的推断框架（渐近分布及方差估计），而现有工作（如Chang et al., 2023）仅给出点估计。

**贡献**  
1. 提出无需迭代的一步估计，仅需标准特征分解，理论证明在载荷线性独立、因子可相关下一致。  
2. 提出双投影迭代算法，收敛速度快于HOPE和CC-ISO，尤其在因子高度相关时仍保持高效，并给出收敛速率。  
3. 推导迭代估计量的渐近正态性，并提供两种渐近方差估计（核估计与plug-in估计），使统计推断可行。  
4. 方法适应载荷稀疏性、弱因子，且通过北京空气污染数据验证了其可解释性（识别出臭氧相关因子与一般污染因子）。


### 2. Large-Scale Curve Time Series with Common Stochastic Trends

**讲者**：Degui Li（University of Macau）

**对应论文**：Large-Scale Curve Time Series with Common Stochastic Trends · [arXiv:2509.11060](https://arxiv.org/abs/2509.11060)

<details><summary>摘要（原文）</summary>

This paper studies high-dimensional curve time series with common stochastic trends. A dual functional factor model structure is adopted with a high-dimensional factor model for the observed curve time series and a low-dimensional factor model for the latent curves with common trends. A functional PCA technique is applied to estimate the common stochastic trends and functional factor loadings. Under some regularity conditions we derive the mean square convergence and limit distribution theory for the developed estimates, allowing the dimension and sample size to jointly diverge to infinity. We propose an easy-to-implement criterion to consistently select the number of common stochastic trends and further discuss model estimation when the nonstationary factors are cointegrated. Extensive Monte-Carlo simulations and two empirical applications to large-scale temperature curves in Australia and log-price curves of S&P 500 stocks are conducted, showing finite-sample performance and providing practical implementations of the new methodology.

</details>

**问题**：大规模曲线时间序列（curve time series）中，如何建模并估计潜在的共同随机趋势（common stochastic trends）？现有文献多假设曲线时间序列平稳，或仅处理单条曲线的非平稳性，缺乏适用于高维非平稳曲线数据的因子模型框架。实际中，如数千支股票收益率曲线或数百个气象站温度曲线，常由少数潜在非平稳因子驱动，亟需一种能同时容纳高维性、函数型数据和非平稳性的方法。

**核心方法**：本文提出一种**双功能因子模型**（dual functional factor model）。观测曲线 $Z_{it}$ 分解为公共成分 $\chi_{it}$ 和 idiosyncratic 成分 $\varepsilon_{it}$，其中 $\chi_{it}$ 通过积分算子定义，允许因子和载荷均为函数。进一步对潜在因子曲线 $F_t$ 施加低维因子结构：$F_{jt}(u)=\Phi_j(u)^\top G_t+\eta_{jt}(u)$，将问题转化为高维非平稳因子模型 $Z_{it}=\Lambda_i^\top G_t+\chi_{it}^\eta+\varepsilon_{it}$，其中 $G_t$ 为 $q$ 维 I(1) 共同趋势。采用**功能PCA**（functional PCA）估计 $G_t$ 和载荷 $\Lambda_i$，推导均方收敛率（依赖于 $N,T,q$）和极限分布（混合正态）。对于协整情形，提出**功能PANIC**方法，先差分再估计，并给出信息准则一致选择共同趋势个数和协整秩。

**与已有工作关系**：本文是Bai (2004) 非平稳因子模型向函数型数据的自然推广，但允许因子和载荷均为函数且 $q$ 发散。相比Guo, Qiao and Wang (2021) 和 Tavakoli, Nisol and Hallin (2023a,b) 的固定因子数或仅一方为函数，本文结构更灵活。与Leng et al. (2024) 的平稳双功能因子模型相比，本文首次处理非平稳情形，并建立更快的收敛率（$T^{-2}+N^{-1}$ 而非 $T^{-1}+N^{-1}$）。

**贡献**：1) 首次为高维非平稳曲线时间序列建立因子模型框架；2) 给出功能PCA估计的完整渐近理论，包括均方收敛和极限分布，允许 $N,T,q$ 联合发散；3) 提出易实现的信息准则一致估计共同趋势个数；4) 发展功能PANIC处理协整和非平稳 idiosyncratic 成分；5) 实证应用于澳大利亚温度曲线和S&P 500股票价格曲线，验证方法有效性。


### 3. Structural Identification for Spatial-Temporal Dynamic Models

**讲者**：Rongmao Zhang（Zhejiang Gongshang University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
空间-时间动态模型（如 $Y_{it} = \rho W Y_{it} + \phi Y_{i,t-1} + \beta X_{it} + \varepsilon_{it}$）广泛用于经济、环境等领域，但结构参数（如空间自回归系数 $\rho$、时间滞后系数 $\phi$）的识别面临双重挑战：空间溢出与时间滞后相互纠缠，且不可观测的个体异质性或测量误差易导致内生性。现有识别策略多依赖强工具变量或严格外生性假设，在面板数据中难以同时处理空间依赖与动态反馈。本报告旨在回答：在弱外生性条件下，如何仅利用时空数据的矩条件唯一识别结构参数？

**核心方法**  
讲者可能提出一种基于 **广义矩估计（GMM）** 的识别框架，核心思路是构造一组与误差项正交的 **空间-时间滞后工具变量**。例如，利用高阶空间滞后项 $W^2 Y_{it}$ 或 $W Y_{i,t-1}$ 作为工具，结合时间上的差分变换消除个体固定效应。关键在于证明这些工具在动态空间模型中满足 **秩条件**（即工具与内生变量相关）且 **排除性约束**（与误差项不相关）成立。方法可能进一步引入 **非线性矩条件**（如 $E[Y_{i,t-2} \cdot \varepsilon_{it}] = 0$）以应对弱工具问题，并通过 **连续更新估计（CUE）** 提升有限样本效率。

**与已有工作关系**  
已有文献（如 Kelejian & Prucha, 1998; Lee & Yu, 2014）多假设空间权重矩阵 $W$ 已知且误差项独立同分布，或依赖强外生工具。本报告可能突破两点：一是允许 $W$ 部分未知或存在测量误差，二是放松时间序列上的严格外生性，允许 $X_{it}$ 与过去冲击相关。相比纯时间序列的 **结构向量自回归（SVAR）** 识别，本方法将空间结构纳入识别条件，形成 **时空联合矩约束**，更贴合实际数据生成过程。

**主要贡献**  
1. 理论上给出时空动态模型参数 **可识别性的充分条件**，并证明在弱工具下估计量的 **一致性** 与 **渐近正态性**。  
2. 提出一种 **数据驱动的工具变量选择准则**（如基于 Lasso 的矩筛选），避免主观设定工具集。  
3. 通过蒙特卡洛模拟验证方法在有限样本下的稳健性，并可能应用于空气质量监测数据，揭示污染的空间扩散与时间累积效应。该工作为因果推断中 **时空混杂** 的识别提供了新工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)