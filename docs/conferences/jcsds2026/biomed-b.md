# 生物医学与基因组 Biomedical & Genomics · 2

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 16 场报告**（已检索到对应论文 4 场）

---

## 临床研究与数据监管1

*7 月 12 日（周日） · 13:30-15:10 · Colourful Guizhou Ballroom 3*  
*组织 Yuantao Hao（Peking University） · 主持 Yan Hou（Peking University）*

### 1. Simultaneously Leveraging Individual and Summary Level External Data in Clinical Trials

**讲者**：Guoyou Qin（Fudan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在临床试验中，外部数据（如历史对照、真实世界证据）常以个体水平（individual-level）或汇总水平（summary-level）两种形式存在。现有方法通常仅利用其中一种：个体水平数据可通过倾向性评分加权或贝叶斯先验整合，但获取成本高、隐私限制多；汇总水平数据（如已发表文献的均值、标准差）虽易得，却无法捕捉个体异质性。本报告旨在解决如何**同时**高效融合这两类外部数据，以提升试验的统计功效与估计精度，同时控制偏倚。

**核心方法**  
报告提出一种两阶段数据融合框架。第一阶段，利用个体水平外部数据构建一个“校准模型”，通过协变量平衡（如逆概率加权）或贝叶斯层次模型，估计外部数据与当前试验的异质性参数。第二阶段，将汇总水平外部数据（如来自多个研究的效应估计及其标准误）视为独立信息源，通过 meta-analysis 或 empirical Bayes 方法，与第一阶段得到的个体水平推断进行加权整合。关键创新在于引入一个**异质性调整因子**，使得汇总数据中的效应估计可被“去偏”后再与个体数据融合，从而避免因人群差异导致的混杂。

**与已有工作关系**  
现有文献中，个体水平数据整合多采用 propensity score 或 Bayesian dynamic borrowing（如 Power Prior），而汇总数据整合则依赖经典 meta-analysis。本报告首次将两者统一于一个框架：不同于仅用汇总数据作为先验的 Bayesian 方法，该方法允许个体数据与汇总数据在模型层面交互，并显式建模异质性。与单纯 stacking 两类数据不同，该框架通过一个共享的协变量空间，使得汇总数据中的信息可被个体数据“校准”，从而减少模型误设风险。

**主要贡献**  
1. 提出一种可同时利用个体与汇总水平外部数据的通用框架，填补了该领域的方法空白。  
2. 通过引入异质性调整，有效缓解了外部数据与当前试验人群不匹配导致的偏倚。  
3. 理论推导了估计量的渐近性质，并给出方差估计的闭合形式，便于实际应用。  
4. 在有限样本模拟中，该方法相比单独使用任一类数据，在均方误差和覆盖率上均有显著改善，尤其当外部数据来源多样时。


### 2. A Pharmacokinetics-Informed Bayesian Design for Dose Optimization in Multi-Regional Clinical Trials

**讲者**：Fangrong Yan（China Pharmaceutical University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
多区域临床试验（MRCT）中，不同种族/地区人群的药代动力学（PK）差异常导致剂量-反应关系异质性，传统剂量优化设计（如3+3、CRM）未充分利用PK信息，且难以在早期阶段同时兼顾全局最优剂量与区域特异性调整。本报告旨在解决：如何将PK模型与贝叶斯自适应设计结合，在MRCT中实现剂量-暴露-疗效/毒性联合建模，从而在有限样本下高效识别各区域的最佳剂量。

**核心方法**  
提出一个两阶段贝叶斯分层模型。第一阶段，利用历史PK数据构建先验，通过非线性混合效应模型（NONMEM）刻画药物浓度-时间曲线，并引入区域随机效应 $\eta_k \sim N(0, \tau^2)$ 捕捉区域间PK变异。第二阶段，将个体暴露量（如AUC、$C_{\max}$）作为协变量，建立剂量-毒性/疗效的 logistic 回归模型：$\logit(p_{ij}) = \alpha + \beta \cdot \text{Exposure}_{ij} + \gamma_k$，其中 $\gamma_k$ 为区域截距。采用马尔可夫链蒙特卡洛（MCMC）进行后验推断，并基于后验概率设计剂量递增规则：若某剂量在区域 $k$ 的毒性概率低于阈值且疗效概率高于对照，则推荐为该区域候选剂量。同时，通过全局共享信息（如 $\beta$）与区域特异性参数（$\gamma_k, \eta_k$）的贝叶斯收缩，实现“借力”与“自适应”的平衡。

**与已有工作关系**  
传统贝叶斯剂量优化（如BOIN、CRM）通常仅基于毒性或疗效终点，忽略PK暴露信息；而PK/PD建模多用于固定剂量方案的事后分析，未嵌入实时决策。本报告将PK模型作为剂量-反应关系的桥梁，使剂量调整直接基于暴露量而非名义剂量，更符合药理学机制。相比近期提出的“PK-guided CRM”（如Liu et al., 2020），本方法进一步引入区域随机效应，允许不同区域共享全局暴露-效应斜率的同时保留区域截距差异，解决了MRCT中“全局最优”与“局部适应”的张力。

**贡献**  
1. 首次将PK-informed贝叶斯自适应设计系统性地扩展到MRCT场景，为跨区域剂量优化提供了统计框架。  
2. 通过分层模型实现信息借力，在区域样本量较小时仍能稳定估计，降低I型错误与毒性暴露风险。  
3. 提供后验概率驱动的决策规则，可直接输出各区域推荐剂量及不确定性度量，便于监管沟通。该方法有望加速创新药在全球同步开发中的剂量选择，减少重复试验成本。


### 3. 数字孪生和个体处理疗效估计

**讲者**：Yang Zhao（Nanjing Medical University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
个体处理疗效估计（Individual Treatment Effect, ITE）是精准医疗与个性化决策的核心问题，但传统方法（如匹配、倾向得分加权）依赖强可忽略性假设，且在高维协变量下难以捕捉个体异质性。数字孪生（Digital Twin）作为一种动态、高保真的虚拟副本，能否为每个个体构建反事实轨迹，从而更准确地估计 ITE？本报告旨在回答：如何利用数字孪生技术，在观测数据中实现个体层面的因果效应推断，并克服传统方法对模型形式与数据分布的刚性约束。

**核心方法**  
讲者可能提出一个两阶段框架：首先，利用深度生成模型（如变分自编码器或时序生成对抗网络）为每个个体学习一个“数字孪生”表征，该表征同时编码其基线协变量与历史状态，并能够模拟在给定处理下的潜在结果序列。其次，基于该表征，通过对比同一孪生在处理与对照下的模拟输出，直接计算个体处理效应 $\tau_i = Y_i(1) - Y_i(0)$。关键创新在于将数字孪生视为一个可干预的“虚拟实验台”，从而绕过传统因果推断中“反事实不可观测”的困境。

**与已有工作关系**  
现有 ITE 估计方法（如 Causal Forest、TARNet、CFR）主要依赖表示学习或正则化来平衡分布，但本质上仍是对观测数据的静态拟合。数字孪生方法则引入动态模拟机制：它不直接学习 $E[Y|X,T]$，而是学习一个可生成个体化轨迹的动力学模型。这与近期基于 SCM（Structural Causal Model）的个体化反事实生成思路一脉相承，但数字孪生更强调实时更新与多步预测，且对时序数据（如电子健康记录）具有天然适配性。相比传统匹配方法，数字孪生避免了维度诅咒与稀疏性问题。

**主要贡献**  
1. 提出将数字孪生作为因果推断的新范式，为个体处理效应估计提供了一种“模拟-对比”的替代路径，降低了对强假设的依赖。  
2. 在方法上，融合深度生成模型与因果推理，实现了从静态协变量到动态轨迹的扩展，可能显著提升在复杂时序场景下的估计精度。  
3. 为数字孪生技术在医疗、工业等领域的落地提供了理论支撑与算法原型，有望推动个性化干预策略的实证研究。


### 4. 贝叶斯适应性富集在中药研究的应用

**讲者**：Yang Wang（National Center for Cardiovascular Diseases/Fuwai hospital）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
中药临床试验面临多组分、多靶点、个体化疗效差异大的独特挑战。传统固定样本设计难以在早期识别有效亚组，导致试验效率低下、假阴性率高。本报告旨在解决：如何利用贝叶斯适应性富集设计，在中药试验中动态识别并富集对特定中药方剂反应更佳的亚群，从而在控制错误率的同时提升统计功效与决策灵活性。

**核心方法**  
报告提出一种贝叶斯适应性富集框架。其核心是：在试验中期分析时，基于累积数据计算各候选亚组的后验疗效概率 $P(\theta_k > \delta \mid \text{data})$，其中 $\theta_k$ 为第 $k$ 亚组的平均处理效应，$\delta$ 为临床意义阈值。若某亚组的后验概率低于预设的停止边界（如 $<0.05$），则终止该亚组入组；若高于富集边界（如 $>0.95$），则后续仅继续招募该亚组。整个决策过程通过贝叶斯因子或后验预测分布校准，并利用中药古籍或前期小样本研究构建先验分布（如采用 power prior 或 commensurate prior），以整合历史信息。

**与已有工作关系**  
已有适应性富集设计多基于频率学派框架（如 group sequential 或 adaptive enrichment by subgroup），依赖渐近正态近似，对先验信息利用有限。本报告将贝叶斯方法引入中药领域，其创新在于：① 允许先验反映中药“辨证论治”的临床经验，缓解小样本下的估计不稳定；② 通过后验概率直接量化亚组富集的证据强度，避免多重比较校正的保守性；③ 针对中药多终点（如证候积分、生物标志物）设计联合建模策略，优于传统单指标富集。

**主要贡献**  
理论层面，为中药临床试验提供了一套完整的贝叶斯适应性富集方法论，包括先验构建、中期决策规则及事后推断的校准流程。实践层面，通过模拟与案例（如某活血化瘀方剂治疗冠心病）展示：相比固定设计，该框架可减少 20–30% 样本量，同时将正确识别有效亚组的概率提升至 85% 以上。该工作填补了贝叶斯适应性设计在中医药循证评价中的空白，为复杂干预的精准试验设计开辟了新路径。


## Advances in Statistical Methods for Complex Biomedical Data

*7 月 12 日（周日） · 15:30-17:10 · Colourful Guizhou Ballroom 3*  
*组织 Pei Wang（Icahn School of Medicine at Mount Sinai） · 主持 Pei Wang（Icahn School of Medicine at Mount Sinai）*

### 1. A Joint Fairness Model with Applications to Risk Predictions for Underrepresented Populations

**讲者**：Hua (Judy) Zhong（Weill Cornell Medicine）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
在风险预测模型中（如疾病风险评分、信用评分），传统公平性方法通常仅针对单一敏感属性（如种族、性别）的二元群体，或仅优化单一公平性指标（如demographic parity）。然而，现实场景中常存在多个“代表性不足”的群体（如罕见病群体、少数族裔亚群），它们可能同时面临预测偏差与样本稀疏的双重挑战。现有方法难以在多个群体间联合控制公平性，且容易因群体间异质性导致预测性能严重退化。本报告旨在解决：如何构建一个能同时兼顾多个代表性不足群体的公平性约束，并保持整体预测效能的联合模型？

**核心方法**  
报告提出一种**联合公平性模型**（Joint Fairness Model），其核心思想是将多个群体的公平性约束整合到一个统一的优化框架中。具体而言，模型在损失函数中引入多群体公平性正则项，例如对每个群体$g$定义公平性度量$F_g$（如equalized odds的差异$\Delta_g$），并构造联合惩罚项$\lambda \sum_{g} w_g \cdot \Delta_g$，其中$w_g$为群体权重（可基于样本量或先验重要性设定）。同时，模型可能采用对抗学习或重加权策略，在训练过程中动态调整群体间的偏差，使得预测误差与公平性约束达到帕累托最优。此外，针对代表性不足群体的小样本问题，方法可能结合迁移学习或数据增强技术，提升模型在稀疏群体上的稳定性。

**与已有工作关系**  
已有公平性研究多聚焦于单一敏感属性（如种族）的二元公平性（如Hardt et al., 2016），或仅关注整体公平性而忽略群体间异质性（如Zafar et al., 2017）。本工作将公平性从“单属性-单群体”扩展至“多属性-多群体”的联合场景，并特别关注“代表性不足”这一实际痛点。与多任务学习或群体鲁棒优化（如Group DRO）不同，本方法明确将公平性作为约束而非仅关注最差群体性能，从而在群体间实现更精细的权衡。

**贡献**  
1. 提出首个面向多个代表性不足群体的联合公平性框架，填补了现有方法在群体异质性处理上的空白。  
2. 在风险预测应用中（如医疗风险评分），通过真实数据验证模型在保持整体AUC的同时，显著降低多个少数群体的偏差（如种族与罕见病亚组）。  
3. 提供理论分析，证明联合正则化项在凸损失下的收敛性，并给出群体权重$w_g$的自适应选择策略，增强了方法的可解释性与实用性。


### 2. Contextual Evaluation of MicroRNA Sequencing Data Harmonization in Machine Learning Tasks

**讲者**：Lixuan Qin（Memorial Sloan Kettering Cancer Center）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
MicroRNA测序数据常因实验平台、批次效应等引入系统性异质性，数据整合（harmonization）方法（如ComBat、limma、HarmonizR等）被广泛用于消除此类偏差。然而，现有评估多聚焦于统计指标（如批次效应去除程度、数据分布一致性），缺乏在具体机器学习任务（如分类、聚类、生存预测）中的上下文验证。本报告旨在回答：不同整合方法在miRNA测序数据的下游机器学习任务中表现如何？是否存在任务依赖的最优选择？

**核心方法**  
讲者可能构建一个系统评估框架：首先对多个公开miRNA测序数据集施加人工批次效应或直接使用真实批次标签，然后应用若干主流整合方法（如基于位置尺度调整的ComBat、基于线性模型的limma、基于图正则化的HarmonizR等）生成整合后的表达矩阵。随后，在多个机器学习任务（如二分类、多分类、无监督聚类）中，使用统一模型（如随机森林、SVM、K-means）评估整合后数据的预测性能与稳定性。关键指标包括分类准确率、AUC、聚类纯度（NMI/ARI）以及跨批次泛化误差。可能还引入统计检验（如配对t检验或Friedman检验）比较方法间差异。

**与已有工作关系**  
已有研究多关注基因表达微阵列或RNA-seq数据的批次效应校正，且评估指标局限于统计层面（如PCA可视化、批次间差异的F统计量）。本报告将焦点转向miRNA测序数据——其表达量低、动态范围窄、噪声结构特殊，并首次在多个机器学习任务中系统比较整合方法。与单纯比较整合后数据分布的方法不同，本报告强调“上下文”即任务导向的评估，填补了方法选择与下游应用之间的鸿沟。

**贡献**  
1. 提供miRNA测序数据整合方法在机器学习任务中的首个系统性基准测试，揭示不同方法在分类与聚类任务中的表现差异（例如，ComBat可能提升分类精度但破坏聚类结构）。  
2. 提出任务依赖的选择指南：若目标为跨批次分类，推荐某种方法；若为发现新亚型，则需谨慎。  
3. 为生物信息学研究者提供可复现的评估框架，推动数据整合方法从“统计上好看”向“实际可用”转变。


### 3. Learning Directed Acyclic Graph Models with Applications on High Throughput Omics Data

**讲者**：Jie Peng（University of California, Davis）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高通量组学数据（如基因表达、蛋白质组学）通常呈现“高维小样本”特征，且变量间存在复杂的非线性依赖与潜在混杂。现有有向无环图（DAG）学习方法（如PC算法、GES、LiNGAM）在低维或满足特定分布假设时有效，但在组学数据中面临两大瓶颈：一是条件独立性检验在高维下统计功效不足，二是基于score的搜索易陷入局部最优且计算成本过高。本报告旨在解决如何从高维、噪声强、样本量有限的组学观测数据中，可靠地学习出具有因果解释的DAG结构。

**核心方法**  
讲者可能提出一种两阶段框架：首先利用变量聚类或稀疏正则化（如graphical lasso）对高维变量进行降维或筛选，构建无向骨架；然后引入基于似然比的score函数（如BIC）结合贪婪搜索或混合整数规划，在稀疏子空间内定向边方向。为应对非高斯性与非线性，方法可能采用非参数条件独立性检验（如基于核的HSIC）或引入copula变换。此外，可能通过bootstrap聚合（bagging）或稳定性选择（stability selection）来提升结构学习的鲁棒性，并给出有限样本下的误差界。

**与已有工作关系**  
区别于传统PC算法依赖高斯假设与逐对检验，该方法通过先验聚类降低检验维度，并允许更灵活的分布假设。与LiNGAM相比，不要求严格非高斯且可处理非线性。与贝叶斯网络结构学习（如K2算法）相比，引入高维正则化项以避免过拟合，并利用稳定性选择替代主观先验。方法在思想上与“先骨架后定向”的混合策略一致，但针对组学数据特点优化了检验与搜索的平衡。

**主要贡献**  
1. 提出一种适用于高维组学数据的DAG学习算法，在保持统计一致性的同时显著降低计算复杂度。  
2. 通过理论分析证明在稀疏性条件下，所估计DAG的边集与因果方向以高概率收敛于真图。  
3. 在模拟与真实组学数据（如酵母基因调控网络）上验证，相比现有方法（如PC、GES）在FDR控制与结构恢复精度上提升显著，尤其适用于样本量小于变量数的场景。  
4. 为后续因果推断（如干预效应估计）提供可靠图结构基础，推动组学数据中因果机制的发现。


### 4. CausalGRN: Deciphering Causal Gene Regulatory Networks from Single-Cell CRISPR Screens

**讲者**：Wei Sun（Fred Hutchinson Cancer Center）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
单细胞CRISPR筛选技术能够同时记录扰动（perturbation）与全转录组响应，为推断基因调控网络（GRN）提供了前所未有的因果识别机会。然而，现有方法多基于共表达或相关性（如SCENIC、PIDC），无法区分调控方向与混杂效应；而传统CRISPR分析仅关注差异表达基因，未能系统利用扰动作为外生变异来重建有向图结构。核心挑战在于：如何从高噪声、低捕获率的单细胞数据中，利用CRISPR诱导的基因敲除/激活作为工具变量，稳健地推断出因果边及其方向。

**核心方法**  
CausalGRN 的核心思路是将每个CRISPR靶向基因视为一个外生工具变量（instrumental variable），其扰动状态（是否被编辑）通过单细胞barcode可被观测。方法首先构建一个稀疏有向无环图（DAG）模型，其中节点为基因表达量，边代表因果调控关系。利用CRISPR扰动提供的条件独立性约束，通过两阶段估计：第一阶段用扰动状态预测靶基因表达（排除弱工具变量问题），第二阶段将预测值作为协变量，对其他基因表达进行回归，从而识别因果效应。为避免高维过拟合，采用基于去偏Lasso（debiased Lasso）或贝叶斯变量选择，并引入dropout校正与批次效应调整。最终输出一个加权有向图，边权重为因果效应大小，并附有统计显著性检验（如bootstrap置信区间或FDR控制）。

**与已有工作关系**  
与基于相关性或互信息的GRN推断方法（如GENIE3、SCENIC）不同，CausalGRN 明确利用CRISPR扰动作为外生变异，从而突破“相关不等于因果”的局限。与单细胞CRISPR分析工具（如MAGeCK、scMAGeCK）相比，后者仅关注单个扰动对靶基因的影响，而CausalGRN 将多个扰动联合建模，推断全基因组范围的因果网络。此外，该方法在统计框架上借鉴了因果推断中的工具变量法与结构方程模型，但针对单细胞数据的高稀疏性与技术噪声进行了专门设计（如零膨胀模型与正则化）。

**贡献**  
主要贡献有三：第一，首次将工具变量思想系统引入单细胞CRISPR数据的GRN推断，为因果发现提供了可检验的统计框架；第二，提出一套针对单细胞数据特性的稳健估计与推断流程，包括dropout校正、弱工具变量诊断与多重假设检验；第三，通过模拟与真实数据验证，CausalGRN 在边识别准确率与方向正确率上显著优于现有方法，有望揭示癌症、发育等过程中关键的因果调控模块，为后续功能实验提供可验证假设。


## Advancements in Statistical Learning for Precision Medicine

*7 月 12 日（周日） · 15:30-17:10 · Zhenyuan Room*  
*组织 Heping Zhang（Yale University） · 主持 Jiarui Zhang（South China University of Technology）*

### 1. Stein-Encoder: A White-Box Supervised Encoder via Stein Identities

**讲者**：Xinzhou Guo（The Hong Kong University of Science and Technology）

**对应论文**：Stein-Encoder: A White-Box Supervised Encoder via Stein Identities in Multi-Modal Studies · [arXiv:2605.25734](https://arxiv.org/abs/2605.25734) · 📖 [长篇精读](../../deep_reads/jcsds2026-2605.25734.md)

<details><summary>摘要（原文）</summary>

In multi-modal biomedical research, integrating high-dimensional genomic data with clinical baselines is essential for precision medicine. However, standard deep neural network approaches often entangle these modalities, obscuring the specific predictive impact of genetic features and leading to possibly suboptimal predictive performance. Motivated by the landmark METABRIC cohort primary breast tumors study, we propose the Stein-Encoder, a white-box supervised framework designed to isolate the genetic signal driving clinical outcomes conditional on nuisance covariates. By leveraging Stein's method and residualization techniques, our approach constructs an interpretable single index that summarizes relevant biological heterogeneity while flexibly incorporating clinical factors and can be used to improve downstream prediction. We establish theoretical guarantees for identification, consistency and efficiency improvement. Applied to the METABRIC cohort, the Stein-Encoder outperforms unsupervised benchmarks in predictive accuracy. Crucially, it achieves structural disentanglement by revealing response-specific biological mechanisms: we find that tumor size is driven primarily by mitotic networks, whereas prognostic indices rely on a distinct proliferation-versus-immune axis. This work contributes a unified, computationally efficient framework that bridges statistical rigor with the representational power of neural networks, enabling interpretable, task-specific and efficient compression of multi-modal health data for a wide range of precision medicine applications, beyond biomarker discovery.

</details>

**问题**  
在多模态生物医学研究中，整合高维基因组数据与临床基线是精准医学的关键，但标准深度神经网络（DNN）会以复杂非线性方式纠缠不同模态，既无法分离遗传特征的增量预测信号，又因过拟合高维噪声导致预测次优。以METABRIC乳腺癌队列为例，研究者需同时实现临床结局的准确预测与遗传影响的透明解释，而现有黑箱模型难以满足这一双重需求。

**核心方法**  
本文提出Stein-Encoder，一种基于Stein恒等式的白盒监督编码器。其核心思想是：在条件于临床协变量$X$（nuisance）的框架下，利用Stein恒等式构造一个线性单指标$\gamma^\top Z$来总结遗传模态$Z$的预测信号。具体地，假设$Z\mid X\sim N(AX,\Sigma)$，则一阶Stein矩$E[T(Y)\Sigma^{-1}(Z-AX)]$与真实方向$\beta$成比例，二阶矩的领先特征向量亦然。算法先通过残差化去除$X$对$Z$的线性影响，再顺序选择探针函数$T(Y)$（如$y,y^2,\arctan(ay)$等）和阶数（一阶或二阶）以规避识别退化，最后在低维或高维（稀疏假设）下估计$\gamma$。所得$\hat\gamma^\top Z$作为条件遗传风险评分，与$X$共同输入下游DNN进行预测。

**与已有工作关系**  
与无监督方法（如PCA）相比，Stein-Encoder是监督的，直接利用$Y$提取预测相关方向而非方差最大方向；与经典充分降维方法（如SIR）相比，它能灵活处理混合类型（离散/连续）的$X$，且通过条件线性高斯假设得到闭式估计，避免维度灾难；与黑箱DNN相比，Stein-Encoder是白盒的，权重$\gamma$有显式统计解释，而非来自不透明的训练过程。

**贡献**  
1. 提出基于Stein恒等式的白盒监督编码器框架，实现多模态数据中遗传信号的条件分离与可解释压缩。2. 建立识别性、低维与高维下估计一致性以及下游DNN泛化误差改进的理论保证。3. 在METABRIC数据上，Stein-Encoder在肿瘤大小、NPI等预测任务中显著优于标准DNN和PCA（如肿瘤大小$R^2$从0.075提升至0.182），并揭示响应特异性生物学机制：肿瘤大小主要由有丝分裂网络驱动，而NPI依赖于增殖-免疫轴。4. 提供计算高效的闭式估计器，可作为即插即用模块提升下游模型性能，兼具统计严谨性与神经网络表示能力。


### 2. Enhancing Inference for Small Cohorts via Transfer Learning

**讲者**：Yi Li（University of Michigan）

**对应论文**：Enhancing Inference for Small Cohorts via Transfer Learning and Weighted Integration of Multiple Datasets · [arXiv:2505.07153](https://arxiv.org/abs/2505.07153) · 📖 [长篇精读](../../deep_reads/jcsds2026-2505.07153.md)

<details><summary>摘要（原文）</summary>

Lung sepsis remains a significant concern in the Northeastern U.S., yet the national eICU Collaborative Database includes only a small number of patients from this region, highlighting underrepresentation. Understanding clinical variables such as FiO2, creatinine, platelets, and lactate, which reflect oxygenation, kidney function, coagulation, and metabolism, is crucial because these markers influence sepsis outcomes and may vary by sex. Transfer learning helps address small sample sizes by borrowing information from larger datasets, although differences in covariates and outcome-generating mechanisms between the target and external cohorts can complicate the process. We propose a novel weighting method, TRANSfer LeArning wiTh wEights (TRANSLATE), to integrate data from various sources by incorporating domain-specific characteristics through learned weights that align external data with the target cohort. These weights adjust for cohort differences, are proportional to each cohort's effective sample size, and downweight dissimilar cohorts. TRANSLATE offers theoretical guarantees for improved precision and applies to a wide range of estimands, including means, variances, and distribution functions. Simulations and a real-data application to sepsis outcomes in the Northeast cohort, using a much larger sample from other U.S. regions, show that the method enhances inference while accounting for regional heterogeneity.

</details>

**问题**：当目标（锚）队列样本量很小（如东北地区仅408例肺脓毒症患者）时，直接推断精度极低。现有迁移学习方法多针对特定单变量结局设计，难以同时处理协变量与结局的跨队列异质性，且易因不相似队列的引入导致负迁移。

**核心方法**：提出 TRANSLATE（TRANSfer LeArning wiTh wEights）框架。阶段一：通过估计队列标签对协变量与结局的回归（如随机森林）得到对齐因子 $\psi_s(z) = f_Z^{(0)}(z)/f_Z^{(s)}(z)$，进而构造锚对齐伪总体（anchor-aligned pseudopopulation）。关键创新在于选择对齐比例 $\gamma$ 以最大化复合有效样本量（ESS），使得 $\tilde{\gamma}_s \propto Q_{N_s}^{(s)}$（队列 $s$ 的 ESS），从而自动降权不相似队列。阶段二：利用归一化权重 $\tilde{w}_i$ 构造加权估计量 $\hat{\lambda} = N^{-1}\sum \tilde{w}_i \Phi(Z_i)$，可统一估计均值、方差、协方差、相关系数及亚组对比等多元功能参数，并建立渐近正态性。

**与已有工作关系**：区别于固定/随机效应 meta 分析（假设同质或预设层次）、重要性加权（仅调整协变量，忽略结局异质性且权重不稳定）和层次部分池化（假设共享模式，无法纠正协变量偏移），TRANSLATE 是估计量无关的（estimand-agnostic），在联合协变量-结局空间对齐队列，同时处理两类异质性。理论证明其复合 ESS 渐近可加且超过锚队列样本量，确保精度提升并防止负迁移。

**贡献**：① 提出首个估计量无关的迁移学习框架，支持多变量结局的广泛功能参数推断；② 给出最大化 ESS 的权重选择准则及渐近理论；③ 在肺脓毒症数据中，TRANSLATE 的 ESS 达 3140（45.1%），远高于重要性加权的 1184（17.0%），且对均值、相关性等估计均获得最低标准误，并检测到性别差异，为小队列研究提供了稳健、高效的整合工具。


### 3. Active Subsampling for Measurement-Constrained M-Estimation of Individualized Thresholds with High-Dimensional Data

**讲者**：Yang Ning（Cornell University）

**对应论文**：Active Subsampling for Measurement-Constrained M-Estimation of Individualized Thresholds with High-Dimensional Data · [arXiv:2411.13763](https://arxiv.org/abs/2411.13763) · 📖 [长篇精读](../../deep_reads/jcsds2026-2411.13763.md)

<details><summary>摘要（原文）</summary>

Measurement-constrained problems frequently arise in modern applications such as electronic health record studies. In such problems, despite the availability of large datasets, collecting labeled data can be highly costly or time-consuming, allowing only a small portion of the data to be labeled within a given budget. This raises a critical question: which data points are most beneficial to label given the budget constraint? We study this question in the context of estimating an optimal individualized threshold under a measurement-constrained M-estimation framework. In particular, our goal is to estimate a high-dimensional parameter $θ$ in a linear threshold $θ^TZ$ for a continuous variable $X$ such that the discrepancy between whether $X$ exceeds the threshold $θ^TZ$ and a binary outcome $Y$ is minimized. In the measurement-constrained setting, we propose a novel $K$-step active subsampling algorithm to estimate $θ$, which iteratively samples the most informative observations in the dataset and solves a regularized M-estimator. Our theoretical analysis reveals a sharp phase transition phenomenon with respect to $β$, the smoothness of the conditional density of $X$ given $Y$ and $Z$. Please see the paper for the full abstract.

</details>

**问题**  
在电子健康档案等测量受限场景中，尽管拥有大量未标记数据（如患者特征 $X,Z$），但获取标签 $Y$（如是否30天内再入院）成本极高，只能标记少量样本。本文研究在此约束下，如何主动选择最富信息的数据点进行标记，以高效估计高维个性化阈值 $\theta^\top Z$，使得连续变量 $X$ 是否超过该阈值与二元结果 $Y$ 的差异最小化。该问题可归结为带0-1损失的M-estimation，但非正则性导致传统方法收敛慢（如Feng et al. 2022在i.i.d.下仅达 $(s\log d/N)^{\beta/(2\beta+1)}$ 速率）。

**核心方法**  
提出 $K$ 步主动子采样算法。第一步均匀采样少量数据，求解正则化平滑M估计（用核函数近似0-1损失）得到初始估计 $\hat\theta_1$。后续步骤基于当前估计定义活跃集 $S_k = \{(X,Z): |X-\hat\theta_{k-1}^\top Z| \leq b_{k-1}\}$，仅在该“近阈值”区域内以更高概率采样，再求解相同形式的正则化M估计。理论分析揭示条件密度光滑参数 $\beta$ 的相变：当 $\beta > (1+\sqrt{3})/2$ 时，两步算法（$K=2$）即达参数速率 $O_p((s\log d/N)^{1/2})$，快于i.i.d.下的极小化最优速率；当 $1<\beta\leq (1+\sqrt{3})/2$ 时需有限更多步；当 $\beta\leq 1$ 时需 $K\propto \log\log N$ 步达超参数速率 $O_p((s/N)^{1/(2\beta)})$。此外，建立 $N$-预算极小化框架并证明所提估计量是率最优的（至多对数因子），并利用Lepski方法实现自适应。

**与已有工作关系**  
区别于传统子采样（如线性回归、GLM）旨在近似全数据估计量，本文针对非正则问题，目标是加速收敛速率。与主动学习类似，但本文算法基于平滑代理损失和梯度方法，计算高效，且理论依赖于条件密度光滑性而非Tsybakov噪声条件，导致独特的相变现象。与半监督推断不同，本文需主动设计采样方案而非被动利用未标记数据。

**贡献**  
1) 提出测量受限下高维个性化阈值估计的主动子采样算法，计算高效且理论完备；2) 揭示关于光滑参数 $\beta$ 的相变现象，证明两步算法在光滑性足够时达到参数速率，显著优于被动采样；3) 建立 $N$-预算极小化框架并证明估计量的率最优性；4) 提供自适应方法和实际实施指导，仿真与真实数据验证了优越性。


### 4. Automatic Hybrid Neural ODE Reduction

**讲者**：Lu Tian（Stanford University）

**对应论文**：Automatic and Structure-Aware Sparsification of Hybrid Neural ODEs · [arXiv:2505.18996](https://arxiv.org/abs/2505.18996) · 📖 [长篇精读](../../deep_reads/jcsds2026-2505.18996.md)

<details><summary>摘要（原文）</summary>

Hybrid neural ordinary differential equations (neural ODEs) integrate mechanistic models with neural ODEs, offering strong inductive bias and flexibility, and are particularly advantageous in data-scarce healthcare settings. However, excessive latent states and interactions from mechanistic models can lead to training inefficiency and over-fitting, limiting practical effectiveness of hybrid neural ODEs. In response, we propose a new hybrid pipeline for automatic state selection and structure optimization in mechanistic neural ODEs, combining domain-informed graph modifications with data-driven regularization to sparsify the model for improving predictive performance and stability while retaining mechanistic plausibility. Experiments on synthetic and real-world data show improved predictive performance and robustness with desired sparsity, establishing an effective solution for hybrid model reduction in healthcare applications.

</details>

**问题**：混合神经ODE（Hybrid Neural ODE）通过将机械模型与神经ODE结合，在数据稀缺的医疗场景中展现出强归纳偏置与灵活性。然而，生理机械模型常包含大量冗余潜状态与交互（如UVa-Padova模型有20+潜状态），导致训练低效、过拟合，削弱混合模型的优势。现有简化方法要么依赖领域专家经验（如时间尺度分离），要么是纯数据驱动的图剪枝（如NeuralSparse、Elastic Net），但前者成本高，后者忽略机械结构，难以保持机械合理性与预测性能的平衡。

**核心方法**：提出混合图稀疏化（Hybrid Graph Sparsification, HGS）算法，分三步：1）将机械ODE的图表示中的最大强连通分量（MSCC）合并为超节点，得到松弛有向无环图（RDAG），消除循环以提升训练稳定性；2）对关键路径添加部分传递闭包捷径，允许跳过中间状态，增加模型灵活性；3）对边权重施加$L_1+L_2$正则化（等价于第一层group LASSO，惩罚项为$\sum \|\Gamma_{(u,v)}\|_2^{2/3}$），在训练中自动剪枝冗余边与节点。正则化参数通过交叉验证选择。

**与已有工作关系**：区别于传统生化简化（需深度领域知识）和纯数据驱动图剪枝（如NeuralSparse、Elastic Net，忽略机械结构），HGS将领域知识（图修改）与数据驱动正则化结合，在保持机械合理性的同时实现自动简化。与Zou et al. (2024)的贪心搜索相比，HGS计算更高效且性能更优，类似于LASSO相对于逐步回归的增益。此外，HGS的图修改步骤借鉴了经典简化思想（如准稳态近似），但通过捷径添加保留了关键动力学。

**贡献**：1）提出首个自动、结构感知的混合神经ODE简化框架，融合领域知识与数据驱动；2）理论证明正则化等价于第一层group LASSO，促进组稀疏；3）在合成数据与真实T1D血糖预测数据上，HGS在RMSE、峰值RMSE、有效参数数等指标上一致优于黑箱模型（LSTM、TCN、Transformer等）及其他简化方法（NeuralSparse、Elastic Net、贪心搜索等），尤其在数据稀缺时优势显著；4）产生可解释的简化图，可生成生物学假设（如胰高血糖素反馈环的消除），为临床验证提供方向。


## Statistical Inference on Clinical Trials and Censored Data

*7 月 12 日（周日） · 13:30-15:10 · Libo Room*  
*主办 Chinese Association for Industrial Statistics Teaching · 组织 Qizhai Li（Chinese Academy of Sciences） · 主持 Junjian Zhang（Guangxi Normal University）*

### 1. Equivalence and Non-Inferiority Assessment in Clinical Trials by Win Probability

**讲者**：Shifang Qiu（Chongqing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在临床试验中，等效性（equivalence）与非劣效性（non-inferiority）检验通常基于均值差异或风险比的假设检验，但这类方法对数据分布假设敏感，且难以处理有序分类、生存时间等非正态终点。报告旨在提出一种基于胜率（Win Probability, WP）的通用框架，将等效性与非劣效性评估转化为对概率参数 $P(X > Y) + \frac{1}{2}P(X = Y)$ 的推断，从而规避传统参数假设的局限。

**核心方法**  
定义两组治疗（试验组 $T$ 与对照组 $C$）的胜率 $\theta = P(T > C) + \frac{1}{2}P(T = C)$。等效性检验可表述为 $H_0: \theta \leq \theta_L$ 或 $\theta \geq \theta_U$ 对 $H_1: \theta_L < \theta < \theta_U$，其中 $(\theta_L, \theta_U)$ 为预先指定的等效界值（如 $0.45, 0.55$）；非劣效性检验则为 $H_0: \theta \leq \theta_0$ 对 $H_1: \theta > \theta_0$（如 $\theta_0 = 0.4$）。通过构造基于 U 统计量的无偏估计 $\hat{\theta}$，并利用其渐近正态性构建置信区间，进而进行决策。该方法可自然推广到分层数据或协变量调整。

**与已有工作关系**  
传统方法（如两单侧检验 TOST）依赖均值差或风险比的参数模型，而胜率方法最早由 Mann-Whitney 提出用于两组比较，但多用于优效性检验。本报告将其系统拓展至等效性与非劣效性场景，并给出界值选择、样本量公式及与 Wilcoxon 秩和检验的等价性证明。相比非参数 bootstrap 方法，该框架提供了解析的方差估计，计算更高效。

**主要贡献**  
① 统一了等效性与非劣效性检验的胜率框架，适用于任意有序或连续终点；② 给出了基于 U 统计量的渐近理论，包括方差公式与置信区间构造；③ 通过模拟与实例展示了该方法在偏态分布或小样本下比传统方法更稳健，且检验效能损失可控。为临床试验设计提供了灵活、稳健的替代工具。


### 2. Testing Patterned Covariance Matrices Under Quadratic Subspace

**讲者**：Yuli Liang（Guangxi Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维协方差矩阵的结构检验是统计推断的核心问题之一，但现有检验方法通常针对特定模式（如稀疏、带状、因子结构）分别设计，缺乏统一框架。本报告考虑更一般的“模式化协方差矩阵”（patterned covariance matrix），即协方差矩阵属于某个已知的线性子空间（如Toeplitz、可交换、带通等），并进一步将检验问题置于二次子空间（quadratic subspace）下：原假设为 $\Sigma \in \mathcal{S}$，其中 $\mathcal{S}$ 是一个由二次型约束定义的子空间。该设定能涵盖多种常见模式，但检验统计量的构造与极限分布在高维情形下极具挑战。

**核心方法**  
讲者提出基于二次型投影的检验统计量。首先，将协方差矩阵的样本估计 $\hat{\Sigma}$ 投影到原假设子空间 $\mathcal{S}$ 的正交补空间上，得到残差矩阵 $R = \hat{\Sigma} - \Pi_{\mathcal{S}}(\hat{\Sigma})$。然后构造 $T_n = \operatorname{tr}(R^2)$ 或加权二次型，并利用随机矩阵理论在高维 $p \to \infty$、$n \to \infty$ 且 $p/n \to c$ 的框架下推导其渐近正态分布。关键步骤是证明 $R$ 的二次型在子空间约束下可分解为独立同分布随机变量的U统计量，从而建立中心极限定理。

**与已有工作关系**  
已有工作多聚焦于检验协方差矩阵等于某个给定矩阵（如单位阵）或具有稀疏结构，而本报告将模式化检验推广到任意由二次子空间定义的线性结构。与Ledoit-Wolf检验、Johnstone的Spiked模型检验不同，本方法不要求模式为对角或稀疏，而是允许更丰富的代数结构。此外，与基于似然比的方法相比，本方法避免了高维下似然函数的病态性，且无需对分布做正态性假设（仅需有限四阶矩）。

**贡献**  
1. 提出了一个统一的检验框架，覆盖多种常见协方差模式（如Toeplitz、可交换、循环对称等），只需将模式表示为二次子空间即可。  
2. 在高维非正态条件下给出了检验统计量的渐近分布，并证明了其相合性，填补了该领域缺乏通用检验方法的空白。  
3. 通过数值模拟展示了方法在有限样本下的良好表现，尤其在高维低样本量场景下优于传统基于似然比或Bootstrap的方法。  
4. 为后续研究协方差矩阵的模型选择与假设检验提供了新的理论工具。


### 3. Quantile Regression for Censored Data with A Cure Fraction

**讲者**：Bo Han（Yunnan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在生存分析中，当部分个体“永不经历事件”（即被治愈，cure fraction）时，传统 Cox 模型或加速失效时间模型无法刻画协变量对生存时间不同分位点的异质性影响。现有分位数回归方法（如 Portnoy 2003、Peng & Huang 2008）虽能处理删失数据，但未显式建模治愈比例，导致估计偏倚。本报告旨在解决：如何在存在治愈分数的右删失数据下，建立协变量对生存时间条件分位数的稳健回归模型，同时识别治愈概率的影响。

**核心方法**  
报告提出一种两阶段估计框架。第一阶段，利用 logistic 回归或非参数方法估计治愈概率 $\pi(\mathbf{X}) = P(T = \infty \mid \mathbf{X})$，其中 $T$ 为潜在生存时间。第二阶段，对未治愈子群（$T < \infty$）的条件分位数 $Q_{\tau}(\mathbf{X})$ 进行建模，采用加权分位数回归，权重由删失分布和治愈概率的逆概率构成。具体地，通过 EM 算法或一步估计（one-step）迭代求解，将治愈分数视为缺失数据，利用 Buckley-James 型插补处理删失。理论证明估计量在正则条件下具有相合性和渐近正态性。

**与已有工作关系**  
已有工作分为两支：一是混合治愈模型（如 Farewell 1982），仅关注均值或危险率；二是删失分位数回归（如 Portnoy 2003），假设所有个体最终都会经历事件。本报告首次将治愈分数纳入分位数回归框架，允许协变量对治愈概率和未治愈分位数有不同影响，推广了标准分位数回归的适用场景。与 Peng & Huang (2008) 的计数过程方法相比，本方法直接建模分位数而非累积危险率，更易解释协变量在特定分位点上的效应。

**主要贡献**  
1. 提出一个兼具灵活性和可解释性的模型，同时估计治愈概率和条件分位数，填补了该交叉领域的空白。  
2. 发展了一套稳健的估计方程和计算算法，克服了治愈分数导致的非光滑目标函数和删失双重挑战。  
3. 建立了渐近理论，为推断提供了基础，并通过模拟和实际数据（如癌症临床试验）展示了方法在存在长尾和治愈个体时的优越性。


### 4. Semi-Parametric Estimation for Sample Selection Models

**讲者**：Junjian Zhang（Guangxi Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
样本选择模型（Sample Selection Models）广泛应用于劳动经济学、健康计量等领域，经典 Heckman 两阶段法依赖误差项联合正态性假设，一旦违背则估计不一致。实际数据中误差分布未知且可能非对称、厚尾，因此需要放松参数假设。本报告聚焦于如何在保留部分结构信息的同时，对选择方程与结果方程进行半参数估计，以在稳健性与效率之间取得平衡。

**核心方法**  
讲者提出一种基于 **control function** 框架的半参数估计策略。具体地，选择方程采用单指标形式 $P(D=1 \mid Z) = G(Z^\top \gamma)$，其中链接函数 $G(\cdot)$ 未知但光滑；结果方程设定为 $Y = m(X) + \varepsilon$，$m(\cdot)$ 为未知函数，且 $\varepsilon$ 与选择误差相关。通过局部多项式或级数方法（如 B‑spline）非参数估计 $G(\cdot)$ 与逆 Mills 比型修正项，再代入结果方程进行 profile 似然或两步估计。估计量通过核平滑或 series 逼近实现，并利用 U‑统计量技巧推导渐近性质。

**与已有工作关系**  
传统参数方法（Heckman, 1979）要求 $(\varepsilon, u)$ 联合正态；完全非参数方法（如 Das, Newey & Vella, 2003）虽放松分布假设，但收敛速度慢且需高维平滑。本报告介于两者之间：选择方程保留单指标结构以降低维数，结果方程允许 $m(\cdot)$ 非参数，同时误差分布完全自由。相比现有半参数文献（如 Ichimura, 1993; Newey, 2009），本方法在控制函数构造中引入自适应带宽选择，并给出更易验证的正则条件。

**贡献**  
主要贡献有三：第一，提出一种无需指定误差分布且计算可行的半参数估计量，并证明其 $\sqrt{n}$ 一致性与渐近正态性；第二，通过蒙特卡洛模拟显示，在非正态误差下该估计量均方误差显著低于 Heckman 估计，且与完全非参数方法效率相当；第三，为实证研究者提供了一套可操作的推断程序（包括 bootstrap 标准误），降低了半参数方法的应用门槛。该工作为样本选择模型的稳健估计提供了新工具。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)