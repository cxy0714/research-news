# Biostatistics — Vol 24  Issue 1  ·  2026-05-21

- 共 12 篇 · Biostatistics

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1093/biostatistics/kxab026](https://doi.org/10.1093/biostatistics/kxab026) — A Bayesian nonparametric model for classification of longitudinal profiles
- **作者**: Jeremy T Gaskins, Claudio Fuentes, Rolando De La Cruz
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 209-225
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在纵向数据的疾病分类设定中，传统方法分别对健康与患病人群的纵向响应建模再利用贝叶斯定理分类，但在群体内存在异质性时表现不佳。本文提出一种贝叶斯非参数（BNP）模型，对疾病状态与纵向响应的联合分布进行建模，并通过 Dirichlet 过程（DP）混合模型诱导的聚类实现分类。该方法允许健康、患病及混合隶属度等多种潜在子群体，以非参数方式灵活处理异质性；同时设计了 MCMC 采样方案进行后验推断与预测。实证部分将该方法应用于智利辅助生殖治疗女性的 hCG 激素纵向数据以预测妊娠结局。对您而言，该文提供了一个流行病学纵向数据的 BNP 应用案例，其利用 DP 混合模型刻画潜在异质子群的结构思路，可为您在纵向因果推断或半参数理论中处理潜在混杂与子群异质性提供模型参考。
- **关键技术**: `Bayesian nonparametrics`, `Dirichlet process mixture model`, `longitudinal classification`, `MCMC sampling`, `mixed membership model`
- **为什么对您有用**: 作为流行病学纵向数据的应用案例，其利用 DP 混合模型刻画潜在异质子群的结构思路，可为您在纵向因果推断或半参数理论中处理潜在混杂与子群异质性提供模型参考。

### 2. [10.1093/biostatistics/kxab014](https://doi.org/10.1093/biostatistics/kxab014) — Semiparametric regression analysis of bivariate censored events in a family study of Alzheimer’s disease
- **作者**: Fei Gao, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 32-51
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在家族流行病学研究中，目标是对双变量删失事件（如AD与CVD共病）进行半参数回归，其中次发事件受区间删失、家族成员间存在共享环境与遗传相关的依赖结构。作者提出半参数回归模型，引入家族特异性随机效应与个体随机效应分别刻画共享环境暴露和未观测遗传关联，并联合建模主要疾病与区间删失的次发疾病。估计采用非参数极大似然（NPMLE），计算上发展了稳定的EM算法。理论上建立了NPMLE估计量的渐近性质（一致性、渐近正态性）。模拟验证了有限样本表现；应用于AD家族研究数据，发现AD与CVD共病主要归因于遗传因素而非环境因素。对您而言，NPMLE在随机效应区间删失下的渐近理论与您semiparametric theory兴趣直接相关，AD/CVD家族数据集及遗传vs环境的因果分解思路对epidemiology方向的applied causal work有借鉴价值。
- **关键技术**: `nonparametric maximum likelihood estimation`, `EM algorithm`, `interval censoring`, `shared random effects`, `bivariate survival model`, `semiparametric regression`
- **为什么对您有用**: NPMLE在随机效应区间删失设定下的渐近理论对您semiparametric & nonparametric theory兴趣有直接参考；AD/CVD家族数据集及遗传vs环境的因果分解框架对您epidemiology方向的applied causal work提供数据集和方法借鉴。

### 3. [10.1093/biostatistics/kxab015](https://doi.org/10.1093/biostatistics/kxab015) — Single-index models with functional connectivity network predictors
- **作者**: Caleb Weaver, Luo Xiao, Martin A Lindquist
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 52-67
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对功能连接网络预测变量提出单指标模型（SIM），目标是在高维稀疏网络设定下估计未知的联系函数与指标参数。方法利用网络拓扑结构施加稀疏约束，不仅能识别与响应相关的区域间交互，还能评估特定脑区功能连接的关联性。估计框架属于典型的半参数单指标模型设定，通常涉及指标参数的n^{-1/2}-CAN估计与联系函数的非参数收敛。模拟研究与Human Connectome Project的静息态fMRI数据（预测流体智力与性别）验证了方法的有效性。对您有用：该文将半参数单指标模型拓展至高维网络结构数据，其稀疏约束机制与半参数估计框架对您在半参数理论及高维统计方面的研究有直接参考价值。
- **关键技术**: `single-index model`, `sparse network constraints`, `semiparametric estimation`, `functional connectivity`, `high-dimensional predictors`
- **为什么对您有用**: 将半参数单指标模型与高维网络稀疏约束结合，对您在半参数理论及高维统计方面的研究有直接参考价值，特别是处理结构化高维预测变量的半参数估计问题。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxaa053](https://doi.org/10.1093/biostatistics/kxaa053) — Smaller<i>p</i>-values in genomics studies using distilled auxiliary information
- **作者**: Jordan G Bryan, Peter D Hoff
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 193-208
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在高维基因组学研究中，针对小样本特定实验下的假设检验问题，本文提出利用大规模多模态辅助数据提升检验功效的 FAB (Frequentist Assisted by Bayes) 框架。核心机制是通过一个多模态概率模型提取跨实验条件的细胞系与基因辅助信息，并将其编码为检验统计量的先验分布。FAB 检验构造了结合辅助信息与当前数据的检验统计量：当辅助信息与当前研究高度相关时，检验功效显著高于经典频率学派检验；当相关性低时，其发现数与经典检验一致。理论与模拟表明，该程序在严格控制第一类错误率（Type I error）和错误发现率（FDR）的前提下，有效增加了真实效应的发现数。对您有用：该工作直接推进了您关注的数学统计假设检验方向，展示了如何在保持频率学派有效性下融合外部信息提升功效，其高维多模态信息蒸馏思路亦可迁移至其他高维推断场景。
- **关键技术**: `FAB hypothesis testing`, `multimodal probability model`, `auxiliary information distillation`, `type I error and FDR control`, `power enhancement via prior specification`
- **为什么对您有用**: 直接关联您 primary interest 中的数学统计假设检验，展示了在严格频率学派误差控制下融合外部辅助信息提升功效的新框架；其多模态数据蒸馏与高维检验的结合对高维统计推断亦有参考价值。

### 2. [10.1093/biostatistics/kxab050](https://doi.org/10.1093/biostatistics/kxab050) — Bayesian multivariate probability of success using historical data with type I error rate control
- **作者**: Ethan M Alt, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 17-31
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在临床试验多重终点设定下，研究多重检验的 Bayesian 方法，目标是在渐近保证 type I error 控制的前提下提高功效并确定样本量。作者采用 seemingly unrelated regression (SUR) 模型显式刻画多个结局变量间的相关性，从而对处理效应的联合后验分布进行推断。在此基础上提出一种 Bayesian 多重检验程序，渐近地保证 family-wise type I error rate，避免了传统 frequentist 校正（如 Bonferroni 或 Holm）的过度保守性。进一步发展了 multivariate probability of success (mPoS) 以在多重结局下稳健地确定样本量。模拟结果表明该方法比 Holm 方法具有更高的检验功效。对您而言，虽然本文偏 Bayesian 临床试验，但其对多重检验 type I error 的渐近控制机制和 SUR 联合建模思路，可为您的 hypothesis testing 兴趣提供多重比较视角的参考。
- **关键技术**: `Bayesian multiple testing`, `seemingly unrelated regression`, `asymptotic type I error control`, `multivariate probability of success`, `family-wise error rate`
- **为什么对您有用**: 本文涉及多重检验与 type I error 控制，属于您 primary interest 中的 hypothesis testing 子方向；其利用 SUR 刻画变量相关性以放松传统保守校正的思路，对研究多变量假设检验有一定参考价值。

## 统计计算 / 算法  *(stat_computing, 3 篇)*

### 1. [10.1093/biostatistics/kxab025](https://doi.org/10.1093/biostatistics/kxab025) — A sparse negative binomial mixture model for clustering RNA-seq count data
- **作者**: Yujia Li, Tanbin Rahman, Tianzhou Ma, Lu Tang, George C Tseng
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 68-84
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 small-n-large-p 的 RNA-seq 计数数据设定下，目标是带变量选择的样本聚类。本文提出负二项混合模型，结合 lasso 或 fused lasso 对高维基因特征进行正则化，推断采用改进的 EM 算法与 BIC 准则。相比先将计数数据标准化再用稀疏高斯混合模型的传统做法，直接对计数数据建模避免了分布误设。模拟与真实转录组数据（大鼠脑、乳腺癌）表明其在聚类精度与特征选择上更优。对您而言，该文的高维正则化与 EM 计算细节可作参考，但缺乏半参数/效率理论，方法学新颖度相对有限。
- **关键技术**: `negative binomial mixture model`, `lasso / fused lasso regularization`, `modified EM algorithm`, `BIC tuning`, `small-n-large-p clustering`
- **为什么对您有用**: 涉及高维统计(small-n-large-p)的正则化与统计计算(EM算法)，对您在高维计数数据上的计算方法设计有参考价值，但无RMT或效率理论贡献。

### 2. [10.1093/biostatistics/kxab030](https://doi.org/10.1093/biostatistics/kxab030) — Capturing discrete latent structures: choose LDs over PCs
- **作者**: Theresa A Alexander, Rafael A Irizarry, Héctor Corrada Bravo
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 1-16
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在高维异质生物数据中，目标是识别分离离散潜在结构（如批次效应或细胞类型）的低维嵌入；传统 PCA 假设类别沿最大方差方向分离，若假设不成立则失效。t-SNE/UMAP 虽能缓解此问题，但计算昂贵、非线性导致特征权重难解释，且 t-SNE 仅限 2-3 维。本文提出迭代判别分析（iDA），一种线性降维技术，通过迭代优化生成携带判别信息的嵌入，以最优分离潜在聚类，同时保留线性变换以便事后分析确定定义潜在结构的特征。主要贡献是提供了一个兼顾线性可解释性与离散结构分离的迭代算法。对您在高维统计计算中的降维算法设计有参考价值，但缺乏您关注的渐近理论或效率界。
- **关键技术**: `iterative discriminant analysis (iDA)`, `linear dimensionality reduction`, `discrete latent structure`, `PCA`, `feature interpretability`
- **为什么对您有用**: 涉及高维数据的降维算法设计（统计计算），但缺乏您关注的高维渐近理论（如 RMT）或效率界，属于方法学层面的算法改进。

### 3. [10.1093/biostatistics/kxab021](https://doi.org/10.1093/biostatistics/kxab021) — Fast approximate inference for multivariate longitudinal data
- **作者**: David M Hughes, Marta García-Fiñana, Matt P Wand
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 177-192
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多变量纵向数据设定下，目标是在多变量广义线性混合模型（MGLMM）中对高斯、泊松或二元标记进行联合推断，克服大数据集下的计算瓶颈。本文提出一种平均场变分贝叶斯（MFVB）近似推断算法，通过因子化近似拆解联合后验分布以降低计算复杂度。相比传统MCMC方法，该算法在模拟研究与糖尿病视网膜病变、原发性胆汁性肝硬化等临床应用中实现了显著的计算加速，同时保持了参数估计的良好精度。对您在纵向数据的统计计算与算法设计有直接参考价值，其MFVB近似策略可为处理高维随机效应提供计算思路。
- **关键技术**: `mean field variational Bayes`, `multivariate generalized linear mixed model`, `approximate inference`, `longitudinal markers`, `MCMC comparison`
- **为什么对您有用**: 涉及您primary interest中的统计计算（数值方法与算法）与纵向数据设定，MFVB算法为大规模混合效应模型提供了计算加速方案，且包含流行病学真实数据集可供借鉴。

## 流行病学  *(epidemiology, 3 篇)*

### 1. [10.1093/biostatistics/kxab037](https://doi.org/10.1093/biostatistics/kxab037) — Joint frailty modeling of time-to-event data to elicit the evolution pathway of events: a generalized linear mixed model approach
- **作者**: Shu Kay Ng, Richard Tawiah, Geoffrey J Mclachlan, Vinod Gopalan
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 108-123
- 相关性 3/10 · novelty: `minor`
- **摘要**: 本文在纵向复发事件生存分析框架下，提出联合 frailty 模型以刻画多重共病（multimorbidity）的演化路径；目标参数为不同事件类型的复发风险及其在终止事件（informative censoring）下的联合分布。核心方法引入多元随机效应（multivariate random effects）同时捕获个体异质性风险与终末事件导致的 informative censoring，并基于广义线性混合模型（GLMM）实现参数的高效估计。模拟比较显示联合 frailty 模型在偏差与覆盖概率上优于标准 frailty 模型；实证分析使用黑色素瘤癌症登记数据展示共病路径识别能力。方法学 novelty 有限（GLMM 框架下的参数扩展），但对您在流行病学队列中处理复发事件与 informative censoring 的纵向因果推断有参考价值。
- **关键技术**: `joint frailty model`, `multivariate random effects`, `generalized linear mixed model`, `informative censoring`, `recurrent event analysis`
- **为什么对您有用**: 与您在 longitudinal causal inference 和流行病学应用方向的兴趣相关：复发事件 + informative censoring 的联合建模思路可迁移至纵向因果推断中处理竞争风险与依赖删失的场景，但本文方法层面对 semiparametric efficiency 或 debiased ML 无贡献，收益主要在数据结构与应用范式。

### 2. [10.1093/biostatistics/kxab023](https://doi.org/10.1093/biostatistics/kxab023) — Tailored Bayes: a risk modeling framework under unequal misclassification costs
- **作者**: Solon Karapanagiotis, Umberto Benedetto, Sach Mukherjee, Paul D W Kirk, Paul J Newcombe
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 85-107
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在医疗风险预测的二分类设定下，针对假阳性和假阴性错分成本不对称的问题，本文提出 Tailored Bayes (TB) 框架。TB 框架将不对称错分成本直接融入贝叶斯模型拟合过程（通过修改后验目标或加权损失），而非仅在决策阶段调整分类阈值。核心机制是在贝叶斯推断中引入反映非平衡成本的加权似然或先验调整，从而在逻辑回归等模型中获得面向特定成本结构的后验分布。模拟研究表明，在错分成本差异显著时，TB 相比标准贝叶斯逻辑回归在成本加权的预测指标上有明显提升。实证分析涵盖心脏手术和乳腺癌等三个真实临床数据集，验证了其实用性。对您而言，本文虽非因果推断或半参数效率理论，但其处理不对称损失的决策理论视角，对假设检验（主要兴趣）中的非对称错误控制及流行病学（次要兴趣）风险建模有参考价值。
- **关键技术**: `asymmetric misclassification costs`, `Bayesian decision theory`, `weighted loss function`, `risk prediction modeling`, `logistic regression`
- **为什么对您有用**: 涉及流行病学（次要兴趣）的真实临床数据集与风险预测应用；其处理不对称损失的决策理论框架，可为假设检验（主要兴趣）中非对称错误控制提供贝叶斯视角的参考。

### 3. [10.1093/biostatistics/kxab016](https://doi.org/10.1093/biostatistics/kxab016) — Bayesian integrative analysis and prediction with application to atherosclerosis cardiovascular disease
- **作者**: Thierry Chekouo, Sandra E Safo
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 124-139
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文在多组学数据整合框架下，目标是同时实现变量关联分析与10年动脉粥样硬化性心血管疾病（ASCVD）风险预测，设定中允许融入先验功能信息与临床协变量。作者提出贝叶斯分层整合分析模型，通过联合建模替代传统的“先关联筛选、后预测建模”两阶段方法。核心机制依赖贝叶斯分层先验与变量选择先验（如 spike-and-slab 类），利用 MCMC 进行后验推断以识别相关基因变异与通路。模拟与实证结果表明，联合模型在预测和变量选择上优于两阶段法，并在 ASCVD 数据中识别出若干已知的 CVD 风险基因通路。对您而言，该文提供了流行病学多组学真实数据集的整合分析案例，但方法学上属于纯贝叶斯预测，缺乏您关注的因果推断或半参数效率理论。
- **关键技术**: `Bayesian hierarchical model`, `integrative analysis`, `multi-omics data`, `spike-and-slab prior`, `joint association and prediction`
- **为什么对您有用**: 提供了流行病学（ASCVD）多组学真实数据集与贝叶斯整合分析的应用案例，但方法学上属于纯贝叶斯预测而非您主要关注的因果推断或半参数效率理论，参考价值有限。

## 其他  *(other, 1 篇)*

### 1. [10.1093/biostatistics/kxab011](https://doi.org/10.1093/biostatistics/kxab011) — Accounting for technical noise in Bayesian graphical models of single-cell RNA-sequencing data
- **作者**: Jihwan Oh, Changgee Chang, Qi Long
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 161-176
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对单细胞RNA测序(scRNAseq)数据中由dropout和扩增偏差引起的零膨胀问题，提出了一种贝叶斯层次图模型以估计基因间的条件依赖网络。现有多元高斯图模型无法充分处理过量零值，scLGM通过引入UMI和ERCC数据，在贝叶斯框架下显式地对零膨胀的两个技术噪声来源进行建模。核心机制在于构建包含潜在真实表达量与观测零膨胀的层次结构，利用控制变量修正观测偏差。模拟与实证分析表明，该方法在图结构恢复精度上优于现有基于高斯假设的方法。对您而言，本文方法学新颖性有限（纯参数贝叶斯框架），且与您关注的因果推断、半参数效率界及高维RMT等核心方向关联较弱，仅可作为高维图模型处理零膨胀数据的边缘参考。
- **关键技术**: `Bayesian hierarchical model`, `graphical model`, `zero-inflation modeling`, `UMI/ERCC correction`, `conditional dependency network`
- **为什么对您有用**: 本文属于生物信息学领域的贝叶斯图模型应用，与您关注的因果推断、半参数理论或高维RMT等核心方向关联较弱，仅可作为高维图模型处理零膨胀数据的背景阅读。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

