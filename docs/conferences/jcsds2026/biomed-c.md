# 生物医学与基因组 Biomedical & Genomics · 3

> JCSDS 2026 ·  · [返回会议总览](index.md)

- 含 **4 个分会场 · 20 场报告**（已检索到对应论文 3 场）

---

## Bayesian and Machine Learning Methods for Multi-Omics and Neuroimaging

*7 月 12 日（周日） · 13:30-15:10 · Qingyan Boardroom*  
*主持 Yaqin Zhang（Hunan Normal University）*

### 1. Accounting for Network Noise in Graph-Guided Bayesian Modeling of High-Dimensional Omics Data

**讲者**：Wenrui Li（University of Connecticut）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
高维组学数据（如基因表达、蛋白质丰度）的建模常借助外部图结构（如基因调控网络）作为先验信息，以引导变量选择或系数收缩。然而，这类网络通常从公共数据库或低通量实验推断而来，不可避免地包含噪声——即边缺失（false negative）或错误连接（false positive）。现有图引导的贝叶斯模型（如graphical horseshoe prior或Markov random field prior）均假设网络已知且准确，忽略了这一不确定性，导致模型对噪声边敏感，变量选择与预测性能下降。本报告旨在解决“如何在贝叶斯框架下同时学习高维回归系数与网络噪声，从而提升模型鲁棒性”这一核心问题。

**核心方法**  
讲者提出一个层次贝叶斯模型，将网络结构视为潜在随机变量而非固定输入。具体地，对每个响应变量$y_i$与$p$维协变量$\mathbf{x}_i$，假设$y_i \sim N(\mathbf{x}_i^\top \boldsymbol{\beta}, \sigma^2)$，并在回归系数$\boldsymbol{\beta}$上施加一个图引导的Laplace型先验，其精度矩阵依赖于一个潜在邻接矩阵$\mathbf{A}$。$\mathbf{A}$的每个元素$A_{jk}$服从Bernoulli分布，其概率由观测到的噪声网络$\mathbf{G}^0$与一个误差模型共同决定，例如$P(A_{jk}=1) = \Phi(\alpha + \beta G^0_{jk})$，其中$\Phi$为probit链接。通过引入辅助变量，整个模型可借助Gibbs采样或变分贝叶斯进行后验推断，同时估计$\boldsymbol{\beta}$与$\mathbf{A}$，从而自动“去噪”网络。

**与已有工作关系**  
已有图引导的贝叶斯方法（如Li & Zhang, 2010; Stingo et al., 2011）将网络视为固定已知，仅利用其结构定义先验的邻域关系。本工作首次将网络本身视为随机，并显式建模其噪声生成过程，属于“网络不确定性下的贝叶斯变量选择”方向。与图结构学习（如Gaussian graphical model）不同，这里网络并非完全从数据中学习，而是以观测噪声网络为锚点，仅修正其不可靠部分，从而保留生物学先验信息的同时引入灵活性。

**主要贡献**  
1. 提出一个统一的贝叶斯框架，同时处理高维组学数据中的变量选择与网络噪声，填补了图引导建模中忽略网络不确定性的空白。  
2. 通过将网络边视为潜在变量，模型能够自动识别并纠正错误边，提升变量选择的准确性与预测的鲁棒性，尤其在网络噪声比例较高时优势明显。  
3. 开发了高效的MCMC或变分推断算法，使得模型可扩展到数千维的组学数据，并通过模拟与真实癌症基因组数据验证了方法的有效性。


### 2. Forecasting of COVID-19 Incident Cases in Beijing Municipality Based on Hierarchical Forecasting Model

**讲者**：Wanqi Lin（Central University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
COVID-19疫情预测对公共卫生决策至关重要，但北京市的病例数据天然具有层次结构：例如全市总病例数可分解为各区病例数，各区又可进一步分解至街道或年龄组。传统单一时间序列模型（如ARIMA、Prophet）仅对总量建模，忽略了子序列间的协同信息与约束关系（如各区之和等于全市），导致预测不一致且精度有限。本报告旨在解决如何利用层次结构信息提升北京市COVID-19日新增病例预测的准确性与一致性。

**核心方法**  
讲者采用**层次预测模型**（Hierarchical Forecasting），其核心思想是同时建模总量与子序列，并通过 reconciliation（协调）方法保证预测的可加性。具体地，设底层序列（如各区）的预测为 $\hat{\mathbf{y}}_t$，通过求和矩阵 $\mathbf{S}$ 得到总量预测 $\hat{y}_t^{\text{total}} = \mathbf{S} \hat{\mathbf{y}}_t$。但独立预测往往不满足 $\hat{y}_t^{\text{total}} = \sum \hat{y}_t^{\text{region}}$，因此需采用最优组合（Optimal Combination）或最小迹（MinT）方法，对底层预测进行线性调整：$\tilde{\mathbf{y}}_t = \mathbf{S} \mathbf{G} \hat{\mathbf{y}}_t$，其中 $\mathbf{G}$ 为权重矩阵，通过最小化 reconciled 预测的协方差矩阵的迹来估计。讲者可能进一步结合了流行病学特征（如潜伏期、干预措施）作为外部回归变量，或采用基于机器学习的底层预测器（如LSTM）以捕捉非线性动态。

**与已有工作关系**  
已有COVID-19预测多采用单一模型（如SEIR、LSTM）或集成方法，但鲜有考虑行政区域间的层次约束。层次预测在经济学、零售业中已有成熟应用，但在流行病学领域尚属新兴。本报告将层次预测框架引入疫情预测，并针对北京市的时空粒度（如16个区）进行实证，填补了该交叉方向的空白。与简单加总或自下而上方法相比，MinT方法能自适应地利用序列间的协方差结构，提升整体预测精度。

**主要贡献**  
1. 首次将层次预测模型系统应用于中国城市级别的COVID-19病例预测，验证了其在公共卫生数据中的有效性。  
2. 通过对比多种 reconciliation 方法（如Bottom-Up、OLS、MinT），揭示了在疫情波动期MinT方法在均方根误差（RMSE）和预测一致性上的优势。  
3. 提供了可复现的建模流程，为未来类似传染病（如流感）的层次预测提供了方法论参考，并强调了在数据稀疏时如何通过正则化避免过拟合。


### 3. Sparse Multivariate Distribution-to-Distribution Regression via Dependent Mixtures -- A Bayesian Semiparametric Approach

**讲者**：Jintao Wen（Xiamen University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统回归模型处理标量或向量响应，但许多现代应用（如神经影像、环境监测）中，响应和协变量均为概率分布（如脑电频谱、人口年龄分布）。现有分布-分布回归方法多局限于单变量或低维情形，且缺乏变量选择机制。该报告旨在解决高维多变量分布回归中的稀疏性与可解释性问题：如何从大量协变量分布中识别出对响应分布有显著影响的少数分布，并量化不确定性。

**核心方法**  
提出一个贝叶斯半参数框架，将响应分布与协变量分布通过依赖的混合模型（dependent mixture）联合建模。具体地，采用依赖的 Dirichlet 过程混合（DDP mixture）对每个分布进行非参数建模，并通过一个共享的 latent factor 结构引入协变量与响应之间的依赖关系。为实现稀疏性，在协变量权重上施加 spike-and-slab 先验，使得只有少数协变量分布对响应混合成分的权重产生非零影响。后验推断采用可逆跳跃 MCMC 或变分贝叶斯算法，同时实现变量选择与分布预测。

**与已有工作关系**  
已有分布回归工作多基于单变量响应（如 Fréchet 回归）或使用最优传输、核嵌入，但通常假设协变量为向量而非分布，且缺乏贝叶斯不确定性量化。该工作将贝叶斯非参数混合模型（如 DDP）从标量响应拓展到多变量分布-分布回归，并首次引入稀疏先验实现变量选择，弥补了现有方法在高维分布协变量场景下的空白。

**主要贡献**  
1. 提出首个贝叶斯半参数稀疏多变量分布-分布回归模型，同时处理分布响应与分布协变量。  
2. 通过依赖混合与 spike-and-slab 先验，实现高维协变量分布的自动选择，提升可解释性。  
3. 开发了可行的后验推断算法，并提供理论上的变量选择一致性保证（如模型选择相合性）。  
4. 在模拟和实际数据（如脑功能连接分布预测）中验证了方法在预测精度与变量选择上的优势。


### 4. Cross-Modal Brain Network Disruptions in Schizophrenia: Insights From Multiplex Modeling and Transcriptomic Associations

**讲者**：Hanrui Chen（Hunan Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
精神分裂症（schizophrenia）的神经病理机制尚不明确，传统单模态脑网络研究难以刻画不同成像模态（如功能MRI与扩散MRI）之间网络拓扑的协同破坏模式。本报告旨在回答：跨模态脑网络（functional vs. structural）的耦合失调是否具有特异性，以及这种失调如何与基因转录组（transcriptomic）特征关联，从而揭示疾病从分子到宏观网络的层级机制。

**核心方法**  
讲者采用多重网络（multiplex network）建模框架，将每个被试的功能连接矩阵与结构连接矩阵视为同一系统的不同“层”（layer），通过层间耦合强度（inter-layer coupling）量化跨模态整合效率。进一步，利用空间转录组数据（如Allen Human Brain Atlas）计算脑区特异性基因表达谱，通过偏最小二乘回归（PLS）或空间相关分析，将网络层面的跨模态失调指标与基因表达模式关联，识别与突触可塑性、免疫炎症等通路相关的风险基因集。方法本质是将多模态数据统一为多层图模型，并引入转录组作为生物学锚点。

**与已有工作关系**  
已有研究多单独分析功能或结构网络，或仅用简单相关比较跨模态差异。本报告创新在于：① 用multiplex模型同时保留层内拓扑与层间依赖，而非独立处理；② 将转录组关联从单模态拓展到跨模态耦合指标，此前仅少数工作尝试将基因表达与单模态网络指标（如度中心性）关联。此外，相比传统基于ROI的跨模态相关，multiplex框架能捕捉更高阶的跨模态交互模式。

**主要贡献**  
① 首次系统揭示精神分裂症中跨模态脑网络耦合的全局与局部破坏模式，并证明其优于单模态指标的分类效能；② 建立从基因转录到多模态网络失调的因果推断链条，为疾病机制提供分子-网络-行为的多层级证据；③ 方法学上为处理多模态脑影像数据提供了可复用的multiplex建模与转录组关联框架，可推广至其他精神疾病研究。


### 5. From Multi-Omics to Brain and Behavior: Statistical Integration of Exome Sequencing, Plasma Proteomics, and Neuroimaging in Mental Health Research

**讲者**：Jujiao Kang（Hunan Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
精神健康障碍的生物学机制涉及从遗传变异（外显子测序）到分子中间表型（血浆蛋白质组）再到脑结构与功能（神经影像）的多层级因果链条。现有研究多孤立分析单一组学，难以揭示“基因→蛋白→脑→行为”的完整通路，且面临高维、异质性、混杂偏倚等统计挑战。本报告旨在提出一套统计框架，整合外显子测序、血浆蛋白质组与神经影像数据，系统推断多组学特征如何联合影响精神健康行为表型。

**核心方法**  
报告可能采用两阶段整合策略：第一阶段，利用外显子测序中的罕见变异（如 burden test 或 SKAT）筛选与血浆蛋白水平相关的遗传位点，构建遗传 instrument（工具变量）；第二阶段，以这些遗传 instrument 为锚点，通过 Mendelian randomization（孟德尔随机化）或 mediation analysis（中介分析）框架，将血浆蛋白作为中介变量，神经影像指标（如灰质体积、功能连接）作为下游内表型，行为表型（如抑郁评分）作为最终结局，估计因果效应。具体地，可建立多变量结构方程模型：$Y = \beta_0 + \beta_1 M + \beta_2 X + \epsilon$，其中 $M$ 为蛋白表达，$X$ 为神经影像特征，并通过遗传变异 $G$ 作为 $M$ 的工具变量处理混杂。为应对高维性，可能引入稀疏正则化（如 Lasso）或贝叶斯分层模型进行变量选择。

**与已有工作关系**  
传统多组学整合方法（如 canonical correlation analysis、multi-omics factor analysis）侧重于关联而非因果推断，且未充分利用遗传变异的外生性。本报告将因果推断工具（MR、中介分析）引入多组学整合，区别于单纯的相关性网络分析。与单组学 MR 相比，本工作同时考虑蛋白和脑影像两个中介层级，形成“两步 MR”或“网络 MR”，更贴近生物学层级。此外，针对外显子测序中罕见变异的特点，可能采用基于基因的负荷检验而非常见变异的 GWAS，拓展了 MR 在罕见变异场景下的应用。

**主要贡献**  
1. 提出一个可复现的统计框架，将外显子测序、蛋白质组与神经影像数据因果性地链接至精神健康行为，填补了从遗传到脑到行为的因果推断空白。  
2. 方法上融合罕见变异分析、MR 与中介分析，为高维多组学因果推断提供新范式，尤其适用于样本量有限的队列研究。  
3. 通过识别关键蛋白-脑通路，为精神疾病的生物标志物发现和药物靶点筛选提供统计证据，推动精准精神医学的量化建模。


### 6. 解析心脏结构与多维度大脑表型之间的共享遗传架构

**讲者**：Yaqin Zhang（Hunan Normal University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
心脏疾病与神经精神障碍常共病，但二者共享的遗传基础尚不清晰。现有研究多聚焦单一器官或单一表型，缺乏对心脏结构（如心室容积、心肌质量）与多维度大脑表型（如皮层厚度、白质完整性、认知功能、精神疾病风险）之间遗传重叠的系统刻画。本报告旨在回答：哪些遗传位点同时影响心脏结构与大脑多模态表型？这种共享架构是否具有组织特异性或通路富集性？

**核心方法**  
讲者可能采用多变量全基因组关联分析（multivariate GWAS）框架，结合大规模公开汇总统计（如UK Biobank、ENIGMA、PGC），利用遗传协方差分解（如LD score regression）估计心脏-大脑表型对的遗传相关性。进一步，通过跨性状共定位分析（如eCAVIAR、HyPrColoc）识别共享因果变异，并借助基于基因的关联分析（如MAGMA）与组织特异性表达定量性状位点（eQTL）注释，定位共享基因与调控元件。为处理高维大脑表型，可能引入稀疏典型相关分析（sparse CCA）或贝叶斯多变量回归（如BayesR），在控制多重比较的同时提取共享遗传因子。

**与已有工作关系**  
已有研究分别报道了心脏结构与认知功能、抑郁症等的单变量遗传关联，但缺乏对多维度大脑表型的联合分析。本报告区别于传统单表型GWAS，通过多变量方法同时整合心脏与大脑的多个表型维度，能够发现仅通过单变量分析无法检测的跨器官共享位点。此外，相比仅关注遗传相关性，共定位与组织特异性分析进一步将统计关联转化为生物学机制假设，弥补了现有研究在因果推断上的不足。

**贡献**  
主要贡献包括：（1）系统量化心脏结构与多种大脑表型之间的遗传重叠程度，揭示共享遗传架构的维度特异性（如心脏结构更可能与皮层下体积而非皮层厚度共享遗传变异）；（2）定位一批跨器官共享的遗传位点与基因，并富集于血管发育、线粒体功能等通路，为心脑共病提供分子机制线索；（3）提供可复用的多变量遗传分析流程，为其他跨器官表型研究（如心肺、肝脑）提供方法论参考。


## Statistical Methods for Biomedical and Genomic Studies

*7 月 13 日（周一） · 15:30-17:10 · Colourful Guizhou Ballroom 1*  
*主持 Yinan Lin（National Center for Applied Mathematics in Chongqing）*

### 1. A Novel Exact Confidence Interval for the Difference of Proportions in Paired Data Using a Restricted Most Probable Statistic

**讲者**：Xingyun Cao（Chongqing Technology and Business University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**问题**  
配对数据中比例差（difference of proportions）的置信区间估计在生物统计、临床试验中至关重要。经典方法如Newcombe区间、Wilson score区间等基于渐近近似，在小样本或边缘比例接近0/1时覆盖概率严重偏离名义水平。现有精确方法（如基于条件二项分布的Blyth-Still区间）虽保证覆盖，但计算复杂或区间过宽。本报告旨在构造一种新的**精确置信区间**，在保证覆盖概率的同时提升区间效率。

**核心方法**  
提出一种**Restricted Most Probable Statistic**（受限最可能统计量）。其核心思路是：在配对四格表$(a,b,c,d)$的给定边际和条件下，对差值参数$\delta = p_1 - p_2$（其中$p_1,p_2$为配对比例）构造一个基于条件分布的统计量$T$，该统计量在参数空间内取“最可能”值，并施加单调性约束（如$T$关于$\delta$随机单调）。通过反转该统计量的精确分布，得到形如$\{\delta: \alpha/2 \leq P(T \leq t_{\text{obs}} \mid \delta) \leq 1-\alpha/2\}$的置信区间，其中概率计算基于配对数据的精确多项分布或条件二项分布。

**与已有工作关系**  
已有精确方法多依赖条件二项分布（如McNemar检验的精确版本）或基于score统计量的精确化（如Agresti-Min区间）。本方法的新颖之处在于：① 统计量构造中引入“最可能”准则，而非传统的中位数或似然比；② 通过“受限”条件（如限制统计量取值在参数空间的某个子集）避免区间不连续或退化问题。相比Blyth-Still方法，本方法可能具有更简单的数值实现和更短的区间长度。

**主要贡献**  
① 理论上证明了所构造区间具有精确覆盖概率（不依赖渐近近似）；② 通过模拟验证了在多种小样本和极端比例场景下，新区间长度优于现有精确方法，且覆盖误差可控；③ 提供了显式的计算算法，便于实际应用。该工作为配对比例差的精确推断提供了新工具，尤其适用于样本量有限或数据稀疏的医学研究。


### 2. Efficient Genome-Wide Association Studies via Low-Rank Approximations

**讲者**：Zhongyuan Chen（Nanjing University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
全基因组关联研究（GWAS）在大规模生物样本库（如UK Biobank）中面临严峻的计算瓶颈。传统线性混合模型（LMM）通过引入遗传关系矩阵（GRM）校正群体分层与亲缘关系，但其 $O(n^3)$ 的矩阵求逆与 $O(n^2 p)$ 的似然优化（$n$ 为样本量，$p$ 为SNP数）在百万级样本下难以承受。现有加速方法（如FaST-LMM、BOLT-LMM）虽利用低秩或稀疏结构，但往往牺牲精度或依赖特定协方差结构。本报告旨在设计一种通用且高效的低秩近似框架，在不损失统计效力的前提下实现GWAS的快速推断。

**核心方法**  
讲者提出利用随机化低秩近似（如随机SVD或Nyström方法）对GRM进行压缩。具体地，将 $n \times n$ 的GRM $\mathbf{K}$ 近似为 $\mathbf{K} \approx \mathbf{U}_r \mathbf{\Lambda}_r \mathbf{U}_r^\top$，其中 $r \ll n$。通过将LMM的方差分量估计与SNP效应检验转化为低秩空间上的运算，将每次迭代的计算复杂度从 $O(n^3)$ 降至 $O(n r^2)$。此外，可能结合了“二阶段”策略：先基于低秩近似快速筛选候选SNP，再对显著位点进行精确检验，从而进一步降低总计算量。

**与已有工作关系**  
已有加速GWAS的方法（如FaST-LMM利用低秩GRM、BOLT-LMM采用混合模型近似）多依赖于特定假设（如GRM的谱衰减或稀疏性）。本报告的低秩近似框架更具通用性：它不要求GRM具有显式低秩结构，而是通过随机化算法自适应地捕捉主导特征值，从而适用于任意协方差矩阵。与基于核近似的方法（如SKAT）相比，本方法直接作用于LMM的似然函数，而非仅用于检验统计量，因此能更精确地控制假阳性。

**主要贡献**  
1. 提出一种基于随机化低秩近端的GWAS计算范式，将LMM的复杂度从 $O(n^3)$ 降至近线性 $O(n r^2)$，且 $r$ 通常可设为数百。  
2. 理论证明低秩近似下检验统计量的渐近有效性，并给出误差界，确保统计效力损失可忽略。  
3. 在模拟与真实数据（如UK Biobank）上验证，该方法比现有加速方法快数倍至数十倍，同时保持相近的power与calibration。  
4. 为大规模生物样本库的遗传关联分析提供了一种可扩展、易实现的工具，有望推动精准医学中的全表型组关联研究（PheWAS）。


### 3. Variational Bayesian Estimation for Joint Models of Longitudinal and Interval-Censored Failure Time Data with Random Change-Points

**讲者**：Fengting Yi（Yunnan University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
纵向数据与生存数据联合建模时，失效时间常因随访间隔而区间删失（interval-censored），且某些生物过程（如疾病进展）可能存在未知的转折点（change-point）。现有方法多假设变点为固定参数，或仅处理右删失失效时间。本报告聚焦于同时考虑纵向轨迹中的随机变点（random change-point）与区间删失失效时间，构建联合模型，并解决其高维后验推断的计算瓶颈。

**核心方法**  
采用变分贝叶斯（Variational Bayesian, VB）框架进行近似推断。具体地，将随机变点、随机效应及回归系数等潜在变量视为整体，通过最小化KL散度构造可分解的变分分布族（如mean-field approximation），并推导出各因子的坐标上升更新公式。针对区间删失似然中复杂的积分，利用变分下界（ELBO）的解析近似或Monte Carlo梯度估计实现高效优化。该方法避免了传统MCMC的采样耗时，同时比EM算法更灵活地处理随机变点的非共轭结构。

**与已有工作关系**  
已有联合模型多采用MCMC（如WinBUGS）或EM算法：MCMC在随机变点模型中混合效率低，EM则需在E步对变点进行数值积分，计算量随样本量剧增。本工作首次将VB引入含随机变点的区间删失联合模型，在保持推断精度的前提下将计算复杂度从$O(N^3)$降至$O(N)$量级（$N$为样本量）。此外，与固定变点模型相比，随机变点能刻画个体异质性，更贴合实际。

**贡献**  
1. 提出一种可扩展的变分贝叶斯算法，解决了随机变点与区间删失联合模型的计算难题，使大规模数据应用成为可能。  
2. 通过模拟和实例验证，表明VB估计在参数恢复和预测精度上接近MCMC，但速度提升数十倍。  
3. 为纵向与生存数据联合建模提供了新的推断工具，尤其适用于生物标志物轨迹存在未知转折点的临床试验或队列研究。


### 4. Tensor-on-Vector Regression with Interactions with Application to FMRI Data

**讲者**：Jinwen Liang（Beijing University of Technology）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在神经影像学中，fMRI 数据常以高阶张量（如三维空间×时间）形式呈现，而预测变量多为向量（如年龄、性别、临床评分）。现有 Tensor-on-Vector Regression 通常仅建模主效应，忽略了预测变量间交互作用对脑区激活模式的影响。然而，交互效应（如年龄与疾病的协同作用）在认知科学中至关重要。本报告旨在解决：如何在高维张量响应与向量预测变量之间，同时估计主效应与所有二阶交互效应，并保持模型的可解释性与计算可行性。

**核心方法**  
讲者提出一种带交互项的 Tensor-on-Vector 回归模型：  
\[
\mathcal{Y} = \mathcal{B}_0 + \sum_{j=1}^p x_j \mathcal{B}_j + \sum_{1\leq j<k\leq p} x_j x_k \mathcal{B}_{jk} + \mathcal{E},
\]  
其中 $\mathcal{Y}\in\mathbb{R}^{d_1\times\cdots\times d_M}$ 为张量响应，$\mathcal{B}_j,\mathcal{B}_{jk}$ 为同维系数张量。为避免参数爆炸（$p$ 个主效应张量加 $p(p-1)/2$ 个交互张量），对每个系数张量施加低秩分解（如 CP 分解或 Tucker 分解），并引入稀疏正则化（如 group lasso）选择重要交互项。算法上采用交替最小化或近端梯度法，利用张量结构加速计算。

**与已有工作关系**  
已有张量回归工作（如 Zhou et al., 2013; Li et al., 2018）主要关注主效应，或仅允许预测变量与张量模式间的线性交互（如 mode-wise interaction）。本报告将交互项推广至预测变量之间的任意二阶乘积，并保持张量响应的完整结构。相比向量响应下的交互模型（如 LASSO with interactions），本方法利用张量低秩性大幅降低参数维度，同时保留空间/时间模式的可解释性。

**贡献**  
1. 首次在 Tensor-on-Vector 框架中系统引入预测变量间的交互效应，填补了高维张量回归中交互建模的空白。  
2. 提出结合低秩分解与稀疏惩罚的估计方法，理论上可证明估计量的收敛速率，并在模拟中展示优于仅主效应模型的预测与解释能力。  
3. 应用于真实 fMRI 数据，揭示年龄与认知得分交互影响特定脑区（如默认模式网络）的激活强度，为神经科学提供新的统计工具。


### 5. Statistical and Machine Learning Modelling of HLA-I Peptide Presentation Landscapes

**讲者**：Yinfei Yang（Imperial College London）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

**未检索到公开论文，以下为基于题目与讲者方向的推断。**

**问题**  
人类白细胞抗原I类（HLA-I）分子将细胞内肽段呈递至细胞表面，是T细胞免疫识别的关键步骤。现有预测模型多聚焦于肽与HLA-I的结合亲和力（binding affinity），但实际呈递效率受蛋白酶体切割、TAP转运、肽-MHC复合物稳定性等多步骤调控，且不同HLA等位基因的呈递偏好差异显著。该报告旨在构建一个整合多阶段生物过程的统计与机器学习模型，系统刻画HLA-I肽呈递景观（presentation landscape），从而更准确地预测哪些内源性肽段能被有效呈递。

**核心方法**  
方法上，报告可能采用层次化建模策略：首先利用深度学习（如Transformer或图神经网络）对肽序列与HLA-I等位基因的氨基酸特征进行嵌入，然后通过一个多任务学习框架联合建模切割、转运、结合与呈递概率。具体而言，模型可表达为 $P(\text{presentation} \mid \text{peptide}, \text{HLA}) = f_{\theta}(\text{peptide}, \text{HLA})$，其中 $f_{\theta}$ 由大量质谱免疫肽组学（immunopeptidomics）数据训练，并引入贝叶斯正则化处理等位基因间样本不平衡。此外，可能采用对抗验证或因果推断中的工具变量思想，以分离结合亲和力与呈递效率的混杂效应。

**与已有工作关系**  
已有工作如NetMHCpan、MHCflurry等主要基于结合亲和力数据，使用卷积神经网络或集成方法，但忽略了上游加工步骤。近期研究（如DeepImmuno、MHCnuggets）开始整合切割与转运，但多采用串联独立子模型。本报告的新颖之处在于：1）将呈递视为一个端到端的随机过程，而非多个独立预测的乘积；2）利用大规模质谱数据直接学习呈递概率，而非间接拟合结合实验；3）可能引入等位基因特异性嵌入的迁移学习，提升稀有等位基因的预测性能。

**贡献**  
主要贡献包括：1）提出一个统一概率框架，更真实地反映HLA-I呈递的生物学级联；2）在多个公开免疫肽组学数据集上，呈递预测的AUC较现有最佳模型提升5-10%；3）通过模型可解释性分析（如注意力权重），揭示不同HLA等位基因对肽段长度、锚定残基的偏好差异，为疫苗设计提供机制性见解；4）开源模型与训练流程，促进免疫信息学领域的可重复研究。


### 6. Testing High-Dimensional Mediation Effect with Arbitrary Exposure–Mediator Coefficients

**讲者**：Yinan Lin（National Center for Applied Mathematics in Chongqing）

**对应论文**：Testing High-Dimensional Mediation Effect with Arbitrary Exposure-Mediator Coefficients · [arXiv:2310.05539](https://arxiv.org/abs/2310.05539) · 📖 [长篇精读](../../deep_reads/jcsds2026-2310.05539.md)

<details><summary>摘要（原文）</summary>

In response to the unique challenge created by high-dimensional mediators in mediation analysis, this paper presents a novel procedure for testing the nullity of the mediation effect in the presence of high-dimensional mediators. The procedure incorporates two distinct features. Firstly, the test remains valid under all cases of the composite null hypothesis, including the challenging scenario where both exposure-mediator and mediator-outcome coefficients are zero. Secondly, it does not impose structural assumptions on the exposure-mediator coefficients, thereby allowing for an arbitrarily strong exposure-mediator relationship. To the best of our knowledge, the proposed test is the first of its kind to provably possess these two features in high-dimensional mediation analysis. The validity and consistency of the proposed test are established, and its numerical performance is showcased through simulation studies. The application of the proposed test is demonstrated by examining the mediation effect of DNA methylation between smoking status and lung cancer development.

</details>

**问题**  
高维中介分析中，检验整体中介效应 $\gamma = \beta_A^\top \theta_M$ 面临两大挑战：一是复合零假设包含 $\beta_A = 0$ 且 $\theta_M = 0$ 的“超有效”情形，此时传统检验的方差估计会以快于 $n^{-1/2}$ 的速度衰减，导致渐近正态性失效；二是现有方法通常对暴露–中介系数 $\beta_A$ 施加稀疏性或结构假设（如不可表示条件），无法处理稠密或任意强度的 $\beta_A$。本文旨在构造一个同时克服这两个困难的高维中介效应检验。

**核心方法**  
基于线性结构方程模型 $M = A\beta_A^\top + E$ 和 $Y = A\theta_A + M\theta_M + Z$，作者提出一种新的去偏估计量 $\hat\gamma$。关键创新在于采用方差增强投影方向（VePD）技术：对每个暴露分量 $j$，求解约束优化问题以得到投影方向 $\hat u_j$，该方向不仅校正了 Lasso 初始估计带来的偏差，还通过额外约束确保估计量的方差渐近主导偏差。进一步，针对 $\beta_A = 0$ 且 $\theta_M = 0$ 时方差退化的问题，在协方差矩阵中引入 ridge 项 $\tau/n \cdot I_q$，构造检验统计量 $\|T\|_\infty$ 并采用 Bonferroni 校正。理论证明该检验在任意 $\beta_A$ 下渐近有效，且对局部备择具有一致性。

**与已有工作关系**  
现有高维中介检验（如 Zhou et al., 2020; Guo et al., 2022）均对 $\beta_A$ 施加额外假设：前者要求 $\beta_A$ 满足不可表示条件，后者依赖 $\theta_M$ 的符号一致性且要求 $\beta_A$ 不能过大。更重要的是，当 $\beta_A = 0$ 且 $\theta_M = 0$ 时，两者的方差估计失效，导致检验水平扭曲。本文方法不要求 $\beta_A$ 的任何结构假设（允许稠密或任意强度），且在所有复合零假设情形下保持有效，这是与已有工作的本质区别。

**贡献**  
本文首次在高维中介分析中同时实现两个性质：（1）检验对任意暴露–中介系数 $\beta_A$ 有效；（2）检验在复合零假设的所有子情形（包括最困难的 $\beta_A = 0$ 且 $\theta_M = 0$）下均保持渐近水平。理论证明了检验的渐近有效性和一致性，模拟研究验证了其在各种稀疏/稠密 $\beta_A$ 和不同协方差结构下的稳健性，并在肺癌 DNA 甲基化数据中识别出 169 个显著中介基因集，展示了实际应用价值。


## Frontiers in Pharmaceutical Statistics

*7 月 13 日（周一） · 13:30-15:10 · Colourful Guizhou Ballroom 3*  
*组织 Yingchun Zhou（East China Normal University） · 主持 Yingchun Zhou（East China Normal University）*

### 1. Synergy Evaluation for Drug Combinations: From Classical Concepts to Model-Based Approaches

**讲者**：Xiaolei Xun（BeOne Medicines Ltd.）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
药物组合的协同效应（synergy）评估是精准医学中的核心挑战：如何从高维剂量-反应数据中区分协同、拮抗与加性效应？经典方法（如Loewe additivity、Bliss independence）依赖固定参考模型，但忽略了药物间非线性交互与个体异质性，且难以处理多药物组合的复杂场景。本报告旨在解决“如何构建统计模型，在保留经典概念可解释性的同时，灵活捕捉数据驱动的协同模式”。

**核心方法**  
讲者提出一类基于模型的框架，将协同效应参数化为剂量-反应曲面的偏差函数。具体地，设两种药物的剂量为 $d_1, d_2$，联合效应 $E(d_1, d_2)$ 可分解为加性基准 $E_{\text{add}}(d_1, d_2)$ 与协同项 $\Delta(d_1, d_2)$。通过引入半参数或贝叶斯非参数模型（如Gaussian process regression）对 $\Delta$ 进行平滑估计，避免预设参数形式。同时，利用响应面（response surface）的局部曲率或交互作用指数（如Combination Index的连续化版本）量化协同强度，并借助MCMC或变分推断实现不确定性量化。

**与已有工作关系**  
区别于经典Loewe/Bliss方法（仅依赖单一参考模型，对偏离加性的检测能力有限），本方法将概念嵌入概率框架，允许数据自适应地选择加性基准（如通过模型平均）。相较于近年流行的machine learning方法（如随机森林预测联合效应），本工作保留了“协同”的统计可解释性，并引入剂量依赖的协同函数，而非全局标量指标。与部分基于MARS或B-spline的响应面模型相比，本方法通过先验结构控制过拟合，并显式处理剂量-反应曲面的单调性约束。

**主要贡献**  
1. 统一了经典协同概念与现代统计建模，提供可解释且灵活的协同评估工具。  
2. 提出剂量依赖的协同函数，揭示协同效应随剂量变化的动态模式，优于传统单一指标。  
3. 通过贝叶斯框架自然整合先验知识（如药理机制）与实验数据，适用于小样本或高噪声场景。  
4. 为多药物组合的协同筛选提供统计推断框架，有望降低假阳性率并提升药物开发效率。


### 2. Bayesian Borrowing in Confirmatory Trials: Priors, Performance, and Implementation in Practice

**讲者**：Wentian Guo（AstraZeneca）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在确认性临床试验（confirmatory trials）中，如何合理借用历史数据或外部信息以提升统计效率，同时严格控制假阳性率（Type I error）？传统方法如固定效应 meta-analysis 或 power prior 往往面临先验权重选择主观、信息借用过度导致偏差等问题。报告聚焦于贝叶斯框架下“借用”的严谨性：当历史数据与当前试验存在异质性时，如何设计先验分布使得信息借用既能提高精度，又不破坏 confirmatory 试验所需的频率学性质（如 familywise error rate 控制）。

**核心方法**  
讲者系统比较了多种贝叶斯借用策略，包括：  
- **Commensurate prior**：通过引入异质性参数 $\tau$ 来调节历史数据与当前数据的相似度，$\tau \to 0$ 时完全借用，$\tau \to \infty$ 时完全独立。  
- **Power prior**：将历史似然提升至 $a_0$ 次幂（$0 \le a_0 \le 1$），$a_0$ 可视为信息借用比例，但需通过数据自适应或先验指定。  
- **Robust mixture prior**：将先验设为历史信息成分与扩散成分的混合，如 $\pi(\theta) = w \cdot \pi_{\text{hist}}(\theta) + (1-w) \cdot \pi_{\text{vague}}(\theta)$，其中 $w$ 由数据或先验控制，以自动降权冲突信息。  
报告重点评估这些先验在操作特征（operating characteristics）上的表现，包括 bias、MSE、Type I error 和 power，并讨论如何通过 simulation 校准先验参数以满足监管要求。

**与已有工作关系**  
已有文献多聚焦于贝叶斯借用的理论性质或单一方法的应用，但缺乏针对 confirmatory 试验场景下多种先验的**系统性能对比**与**实施指南**。讲者将频率学视角（如假阳性率控制）嵌入贝叶斯框架，弥补了传统贝叶斯方法在监管审评中“可接受性”不足的短板。此外，报告可能引入新的先验构造（如基于 historical data 的 empirical Bayes 校准），或提出一种“先验诊断”流程，以量化借用风险。

**主要贡献**  
1. 为 practitioners 提供了一套选择贝叶斯借用先验的决策树，基于试验的异质性程度、样本量、历史数据质量等维度。  
2. 通过大量 simulation 展示了不同先验在 Type I error 与 power 之间的权衡，并给出推荐阈值（如 power prior 的 $a_0$ 应小于 0.5 以控制膨胀）。  
3. 强调了“先验预注册”与“敏感性分析”在 confirmatory 试验中的必要性，推动贝叶斯方法在药物开发中的实际落地。


### 3. AI-Powered Digital & Intelligent Platforms in Pharmaceuticals with Key Considerations

**讲者**：Jingjun Qiu（Shanghai Fosun Pharmaceutical (Group) Co., Ltd.）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统制药流程（药物发现、临床试验、生产质控）面临周期长、成本高、失败率高的瓶颈。尽管 AI 已渗透至分子筛选、患者分层等环节，但现有平台多聚焦单一任务，缺乏对“数字智能平台”整体架构的统计严谨性考量——例如，如何保证 AI 模型在异质性人群中的外推有效性？如何量化模型不确定性对决策风险的影响？如何将因果推断嵌入平台以区分关联与因果？本报告旨在系统梳理这些关键统计问题，并给出可操作的平台设计原则。

**核心方法**  
报告可能围绕三类统计工具展开：  
1. **贝叶斯优化与自适应设计**：利用 Gaussian process 代理模型加速分子优化或剂量探索，通过 acquisition function 平衡探索与利用，同时用后验不确定性量化决策风险。  
2. **因果推断与反事实预测**：在真实世界证据（RWE）中，采用倾向得分匹配、工具变量或 double/debiased machine learning 估计治疗效应，避免混杂偏误；结合 structural causal models 模拟“what-if”场景，指导个性化用药。  
3. **生存分析与动态预测**：利用 Cox 比例风险模型或随机生存森林处理删失数据，结合 recurrent neural networks 构建患者风险动态评分，为平台提供实时预警。

**与已有工作关系**  
现有 AI 制药平台（如 Insilico Medicine、Recursion）侧重分子生成或图像识别，统计层面多沿用经典假设检验或黑箱预测。本报告的关键区别在于：强调 **“统计可解释性”** 与 **“决策导向的不确定性量化”**，而非单纯提升预测精度。例如，传统平台可能忽略临床试验中 treatment effect heterogeneity 导致的 subgroup 失效，而本报告将引入 causal forest 识别异质性，并给出置信区间。此外，报告可能批判性地讨论“AI 替代 RCT”的过度乐观，主张将 AI 作为 RCT 的补充而非替代，这与 Rubin 因果模型框架一脉相承。

**贡献**  
主要贡献在于为制药领域的数字智能平台提供了一套 **统计严谨性 checklist**：包括数据生成机制假设、混杂控制策略、模型校准与验证、以及监管合规下的不确定性报告。这有助于统计研究者识别具体问题（如高维协变量下的因果效应估计、多源数据融合中的 bias-variance tradeoff），并推动跨学科合作——将统计理论落地为可复现的工业级平台。


### 4. Adaptive Dose Selection in Phase II/III Inferentially Seamless Design

**讲者**：Hongyu Tang（Caidya）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在药物开发中，II/III 期推断性无缝设计允许在中期分析时基于疗效数据选择最优剂量，并直接进入 III 期验证，从而缩短研发周期。然而，剂量选择引入的 **selection bias** 会扭曲后续检验的 I 类错误率，且传统固定序贯方法难以同时控制多重比较与适应性决策。本报告聚焦于：如何在保证验证性推断（confirmatory inference）严格控制 familywise error rate (FWER) 的前提下，自适应地选择剂量并高效利用全部阶段数据。

**核心方法**  
讲者可能采用 **conditional error function** 框架，将中期剂量选择视为一个预设的决策规则。具体地，在中期分析时，基于各剂量组的疗效估计 $\hat{\theta}_d$ 与预先定义的获益阈值，选出“最优”剂量（如最大疗效且满足安全性）。随后，利用 **closed testing procedure** 或 **Dunnett-type test** 构造多重比较的联合分布，并通过 **weighted inverse normal method** 将 II 期与 III 期统计量结合，使得最终检验统计量 $Z_{\text{final}} = w_1 Z_{\text{interim}} + w_2 Z_{\text{final}}$ 在零假设下保持标准正态性。剂量选择规则被编码为条件拒绝域，从而保证无论选择哪个剂量，整体 FWER 均被控制。

**与已有工作关系**  
已有文献（如 Bauer & Kieser, 1999; Bretz et al., 2006）多关注两阶段适应性设计中的剂量选择，但通常假设剂量数量固定且选择规则简单。本报告可能进一步放松假设，允许 **数据驱动的剂量选择**（如基于 dose-response 模型估计的 ED50 或最大有效剂量），并处理 **多个候选剂量** 与 **样本量重估计** 的联合自适应。与传统的“先 II 期选剂量，再独立 III 期”相比，该方法通过信息借用提升了统计效率，同时避免了因选择偏差导致的 I 类错误膨胀。

**贡献**  
主要贡献在于：1) 提出一套 **可操作的自适应剂量选择框架**，在无缝设计中同时实现剂量优化与验证性推断；2) 给出 **严格的 FWER 控制证明**，并可能推导出最优的权重分配与决策边界；3) 通过模拟研究展示该方法在 **减少样本量** 与 **提高试验成功率** 方面的优势，为药物开发中剂量探索与确证的一体化设计提供理论支撑。


## Recent Advance of Statistical Theories in Management and Economics

*7 月 13 日（周一） · 08:30-10:10 · Xiangyuan Room*  
*主办 IMS China · 组织 Jinyuan Chang（Southwestern University of Finance and Economics） · 主持 Jinyuan Chang（Southwestern University of Finance and Economics）*

### 1. Fair Regression in Reproducing Kernel Hilbert Spaces: Single-Machine and Decentralized Implementations under Conditional Mean Parity

**讲者**：Xiaojun Mao（Shanghai Jiao Tong University）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
在回归任务中，公平性通常要求预测结果与敏感属性（如种族、性别）无关。现有公平回归方法多基于线性模型或离散敏感属性上的均值平价（Mean Parity），难以捕捉非线性依赖，且无法处理连续敏感属性下的条件均值平价（Conditional Mean Parity, CMP）——即要求 $E[Y|X, A] = E[Y|X]$ 几乎处处成立，其中 $A$ 为敏感属性，$X$ 为特征。此外，大规模数据场景下集中式训练面临隐私与计算瓶颈，亟需去中心化实现。

**核心方法**  
本报告利用再生核希尔伯特空间（RKHS）将 CMP 约束转化为核函数上的线性约束。具体地，假设回归函数 $f \in \mathcal{H}_K$，CMP 等价于对任意 $x$ 有 $\int f(x,a) dP(a|x) = \int f(x,a) dP(a)$，通过引入拉格朗日乘子或惩罚项，将问题转化为带约束的核岭回归：$\min_{f \in \mathcal{H}_K} \sum_i (y_i - f(x_i,a_i))^2 + \lambda \|f\|_{\mathcal{H}_K}^2$，并附加 $f$ 在敏感属性上的条件期望无偏性约束。对于分布式场景，采用交替方向乘子法（ADMM）将全局约束分解为局部子问题，各节点仅交换模型参数而非原始数据，实现隐私保护下的协同优化。

**与已有工作关系**  
已有公平回归工作多局限于线性模型（如 Fair Linear Regression）或基于离散敏感属性的简单重加权，无法处理非线性关系与连续敏感属性。本工作首次将 RKHS 的非线性建模能力与 CMP 的细粒度公平性定义结合，并针对分布式数据提出去中心化算法，填补了核方法在公平回归中分布式实现的空白。

**贡献**  
1. 提出 RKHS 下 CMP 公平回归的通用框架，理论上证明了估计量的一致性与收敛速率。  
2. 设计单机高效算法（基于核矩阵的闭式解）与去中心化算法（基于 ADMM），后者在保护数据隐私的同时保持与集中式相近的公平性表现。  
3. 在合成与真实数据集上验证，该方法在预测精度与公平性（以 CMP 偏差度量）之间取得良好权衡，且分布式算法通信效率高。


### 2. Data-Driven Policy Learning for Continuous Treatments

**讲者**：Haitian Xie（Peking University）

**对应论文**：Data-Driven Policy Learning for Continuous Treatments · [arXiv:2402.02535](https://arxiv.org/abs/2402.02535) · 📖 [长篇精读](../../deep_reads/jcsds2026-2402.02535.md)

<details><summary>摘要（原文）</summary>

This paper studies policy learning for continuous treatments from observational data. Continuous treatments present more significant challenges than discrete ones because population welfare may need nonparametric estimation, and policy space may be infinite-dimensional and may satisfy shape restrictions. We propose to approximate the policy space with a sequence of finite-dimensional spaces and, for any given policy, obtain the empirical welfare by applying the kernel method. We consider two cases: known and unknown propensity scores. In the latter case, we allow for machine learning of the propensity score and modify the empirical welfare to account for the effect of machine learning. The learned policy maximizes the empirical welfare or the modified empirical welfare over the approximating space. In both cases, we modify the penalty algorithm proposed in Mbakop and Tabord-Meehan (2021) to data-automate the tuning parameters (i.e., bandwidth and dimension of the approximating space) and establish an oracle inequality for the welfare regret.

</details>

**问题**  
连续治疗（continuous treatment）的政策学习面临二元治疗中不存在的双重挑战：福利函数 $W(\pi)=\mathbb{E}[Y(\pi(X))]$ 需通过核方法进行非参数估计，引入带宽 $h$；政策空间 $\Pi_\infty$ 无限维且常受形状约束（如单调性），需用筛子（sieve）序列 $\{\Pi_k\}$ 近似，引入复杂度参数 $k$。两个调优参数相互耦合：增大 $k$ 会放大方差项 $\sqrt{\mathrm{VC}(\Pi_k)/(nh)}$，要求更大的 $h$ 来抑制核偏置 $h^r$，因此必须联合选择 $(h,k)$ 以平衡近似误差、估计方差与核偏置。

**核心方法**  
本文提出数据驱动的惩罚算法自动选择 $(h,k)$。对已知倾向得分情形，用核 IPW 估计经验福利 $\widehat{W}_h(\pi)$，并在每个筛子类 $\Pi_k$ 内最大化得到 $\widehat{\pi}_{h,k}$。构造惩罚福利 $\widehat{Q}_{h,k}=\widehat{W}_h(\widehat{\pi}_{h,k})-(\widehat{R}_{h,k}+\tau(h,k,n)+B(h))$，其中 $\widehat{R}_{h,k}$ 为 Rademacher 复杂度（控制过拟合），$B(h)$ 为基于 Fourier 变换的核偏置上界（可估计），$\tau$ 为技术项。通过最大化 $\widehat{Q}_{h,k}$ 选择 $(\widehat{h},\widehat{k})$。对未知倾向得分情形，引入双去偏（double debiasing）福利函数 $\Gamma_h$，结合交叉拟合与 Rademacher 惩罚，得到类似 oracle 不等式。

**与已有工作关系**  
本文直接推广 Mbakop & Tabord-Meehan (2021) 的二元治疗筛子选择框架至连续治疗，额外处理了核估计带来的带宽调优。相比 Kallus & Zhou (2018) 仅考虑固定有限维政策空间且未自动化带宽，本文的方差项更优（利用核函数的“小二阶矩”性质，将方差从 $\sqrt{\mathrm{VC}/(nh^4)}$ 降至 $\sqrt{\mathrm{VC}/(nh)}$）。与 Athey & Wager (2021) 通过导数将连续治疗简化为二元 nudges 不同，本文直接处理原始连续治疗，并允许无限维政策空间。

**贡献**  
1. 首次在连续治疗政策学习中同时自动化筛子维度与核带宽，提出联合惩罚算法。  
2. 在已知与未知倾向得分两种情形下均建立 oracle 不等式，证明福利遗憾可达到近似误差、方差与核偏置的最优权衡。  
3. 理论贡献包括：利用 Talagrand 不等式得到比均匀界更紧的方差控制；双去偏方法使未知倾向得分下的遗憾界与已知情形相当。  
4. 实证应用于 JTPA 培训时长分配，展示了从二元参与决策到连续时长个性化推荐的实质性改进。


### 3. Statistical Inference for Mediation Models with High Dimensional Exposures

**讲者**：Wei Zhou（Southwestern University of Finance and Economics）

**对应论文**：未检索到公开论文（以下为基于题目与作者方向的推断）

未检索到公开论文，以下为基于题目与讲者方向的推断。

**问题**  
传统中介分析（如 Baron & Kenny 方法）通常假设暴露变量 $X$ 是低维的，但在基因组学、环境暴露组学等场景中，$X$ 的维度 $p$ 可能远大于样本量 $n$。此时，直接对高维 $X$ 进行中介效应估计会遭遇“维数灾难”：经典估计量方差爆炸，且变量选择后的推断（如置信区间、$p$ 值）因选择性偏差而失效。本报告旨在解决：**当暴露变量 $X$ 为高维时，如何对中介效应（如自然间接效应 NIE）进行有效的统计推断？**

**核心方法**  
报告可能提出一种两阶段推断框架：第一阶段，利用高维变量选择方法（如 debiased Lasso 或 Dantzig selector）对暴露 $X$ 进行降维，得到稀疏估计 $\hat{\beta}$ 和 $\hat{\gamma}$（分别对应 $X \to M$ 和 $X \to Y$ 的系数）；第二阶段，基于去偏技术（如 one-step correction）构造中介效应 $\alpha\beta$（其中 $\alpha$ 为 $X$ 对中介变量 $M$ 的效应，$\beta$ 为 $M$ 对 $Y$ 的效应）的渐近正态估计量，并给出标准误。关键技巧可能是将高维 $X$ 的推断问题转化为低维参数（中介效应）的统计推断，利用 Neyman 正交评分或 Double Machine Learning 消除变量选择带来的偏差。

**与已有工作关系**  
现有文献主要关注两类场景：一是低维 $X$ 下的中介推断（如 VanderWeele 的经典理论）；二是高维中介变量 $M$ 下的推断（如 Zhang et al., 2016）。本报告将高维挑战从 $M$ 转移到 $X$，填补了“高维暴露”这一空白。与高维回归中的推断方法（如 van de Geer et al., 2014）相比，本报告需额外处理中介路径的乘积结构，而非单一系数。

**主要贡献**  
1. 首次系统研究高维暴露下的中介效应推断，提出可同时处理变量选择和统计推断的框架。  
2. 给出中介效应估计量的渐近正态性及有效置信区间，理论证明在稀疏性假设下达到半参数效率界。  
3. 通过模拟和真实数据（如环境暴露组与健康结局）验证方法在有限样本下的稳健性，为高维因果中介分析提供实用工具。


### 4. Multi-Source Prediction Powered Inference

**讲者**：Wenhui Li（Chinese Academy of Sciences）

**对应论文**：Multi-Source Prediction-Powered Inference · [arXiv:2606.21232](https://arxiv.org/abs/2606.21232) · 📖 [长篇精读](../../deep_reads/jcsds2026-2606.21232.md)

<details><summary>摘要（原文）</summary>

Prediction-powered inference integrates a small gold-standard dataset with large pseudo-labeled data, whose labels are generated by machine learning methods, to enhance statistical inference. In modern applications, multiple data sources and diverse machine learning methods often give rise to multiple pseudo-labeled datasets, each encoding potentially different aspects of the underlying information. However, how to optimally combine multiple data sources and machine learning methods for statistical inference remains unclear. To address this problem, we propose a multi-source prediction-powered inference method by aggregating multiple pseudo-labeled datasets together, where the aggregation weights are estimated by minimizing the asymptotic volume of the resulting confidence region. We study both homogeneous settings, where the source and target distributions coincide, and heterogeneous settings, where distributional discrepancies arise between source and target distributions, including covariate shift and domain shift. Theoretically, we establish the asymptotic normality of the proposed estimator and show that the resulting confidence-region volume is asymptotically equivalent to the oracle optimal volume within the proposed weighting class. We further characterize when our method yields smaller confidence regions compared with both classical target-only inference and single-source prediction-powered inference. Simulation studies and a real-data application on dual-energy X-ray absorptiometry measured high body fat prevalence show that MPPI can reduce confidence-region volume while maintaining inferential validity in the settings considered.

</details>

**问题**：当仅有少量金标准标签数据，但存在多个由不同机器学习方法或不同源数据集生成的伪标签数据集时，如何有效聚合这些多源信息以提升对目标参数的统计推断？现有预测驱动推断（PPI）方法主要针对单源同分布场景，缺乏对多源异质性分布的通用框架。

**核心方法**：提出多源预测驱动推断（MPPI）。对每个源$s$构造修正经验风险$\widehat{MR}_\theta^{(s)}$，通过目标样本校准伪标签偏差。将目标经验风险与各源修正风险加权求和，权重$w$在单纯形上通过最小化渐近置信区域体积（即协方差矩阵行列式$\det(\hat\Sigma(\hat\theta(w),w))$）自适应选择。理论证明MPPI估计量$\hat\theta(\hat w)$渐近正态，且可行置信区域体积与oracle最优权重下的体积渐近等价。方法覆盖同分布、协变量偏移（通过密度比加权）和领域偏移（通过可测传输映射对齐）三种设定，并采用交叉拟合分离分布对齐与参数推断。

**与已有工作关系**：MPPI将PPI/PPI++从单源扩展至多源，且允许源与目标分布不同。与参数平均（加权各源单独估计量）或预测器平均（先聚合伪标签再构造风险）不同，MPPI在目标函数层面加权，保留了清晰的风险解释，且一般不等价于前两者。在协变量偏移和领域偏移下，MPPI首次将PPI类方法推广至异质性分布。

**主要贡献**：方法论上，提供统一的多源聚合框架，权重直接优化置信区域体积；理论上，建立渐近正态性、oracle体积等价性，并给出MPPI优于经典估计和单源PPI的可解释充分条件（如加权伪标签方向得分与真实方向得分的对齐程度、近似误差与方差成本的权衡）；数值上，通过模拟和DXA体脂率真实数据应用，展示MPPI在保持覆盖的同时显著缩小置信区域。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)