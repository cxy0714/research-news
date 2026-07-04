# Biostatistics — Vol 24  Issue 1  ·  2026-07-04

- 共 12 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 1 篇（对照 OpenAlex 13 篇）：10.1093/biostatistics/kxac015

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》第24卷第1期的12篇论文，整体上呈现出两条清晰的主线：**假设检验与多重性控制**，以及**贝叶斯方法在复杂数据建模中的扩展**。此外，还有若干篇涉及**半参数回归**、**降维与聚类**、**计算加速**等主题。以下按主线归纳。

**主线一：假设检验与多重性控制**。这一主题集中出现在两篇论文中。Smaller *p*-values in genomics studies using distilled auxiliary information 提出FAB检验，利用大规模辅助数据构造偏移项提升小样本检验功效，并保证第一类错误率控制。Bayesian multivariate probability of success using historical data with type I error rate control 则针对多个临床结局的多重性检验，通过贝叶斯后验与渐近理论结合，在控制第一类错误的同时提升功效，并扩展至多元成功概率的样本量确定。两篇均聚焦于如何利用外部信息或结构（辅助数据、结局相关性）来优化检验性能，但前者更偏向基因组学应用，后者更贴近临床试验设计。

**主线二：贝叶斯方法在复杂数据建模中的扩展**。这一主线覆盖了多篇论文，但侧重点各异。Bayesian integrative analysis and prediction with application to atherosclerosis cardiovascular disease 提出贝叶斯分层整合模型，用于多组学数据关联与预测，但方法学新颖性有限。Tailored Bayes: a risk modeling framework under unequal misclassification costs 将误分类成本嵌入贝叶斯推断，优化预测性能，属于决策理论应用。A Bayesian nonparametric model for classification of longitudinal profiles 利用狄利克雷过程处理纵向分类中的异质性。Accounting for technical noise in Bayesian graphical models of single-cell RNA-sequencing data 则针对单细胞数据零膨胀问题，将噪声建模融入图模型。这些工作展示了贝叶斯框架在整合多源信息、处理异质性和噪声方面的灵活性，但均未涉及因果推断或半参数效率理论。

**其他值得关注的主题**：半参数回归方面，Semiparametric regression analysis of bivariate censored events in a family study of Alzheimer’s disease 处理双变量区间删失数据，引入随机效应并建立渐近性质，与流行病学因果推断相关。降维与聚类方面，Capturing discrete latent structures: choose LDs over PCs 提出iDA方法，强调线性判别分析在离散结构检测中的优势；A sparse negative binomial mixture model for clustering RNA-seq count data 则扩展了稀疏混合模型至计数数据。计算加速方面，Fast approximate inference for multivariate longitudinal data 通过变分贝叶斯将MGLMM的计算复杂度降至线性，适合大规模纵向数据。

**适合优先阅读的论文**：若您关注因果推断与半参数效率，可优先看Semiparametric regression analysis of bivariate censored events in a family study of Alzheimer’s disease（半参数随机效应模型与区间删失）和Joint frailty modeling of time-to-event data to elicit the evolution pathway of events（联合脆弱模型与信息删失处理）。若关注假设检验与多重性控制，Smaller *p*-values in genomics studies using distilled auxiliary information 和 Bayesian multivariate probability of success using historical data with type I error rate control 值得细读。若关注高维数据降维，Capturing discrete latent structures: choose LDs over PCs 提供了线性判别分析的替代视角。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxaa053](https://doi.org/10.1093/biostatistics/kxaa053) — Smaller<i>p</i>-values in genomics studies using distilled auxiliary information
- **作者**: Jordan G Bryan, Peter D Hoff
- **期刊/来源**: Biostatistics
- **机构**: Duke University
- **分类**: vol 24 · issue 1 · pp 193-208
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种“frequentist assisted by Bayes”（FAB）假设检验程序，旨在利用大规模基因组辅助数据集（如癌症细胞系分子谱）的信息来提升小规模专项研究（如定制实验条件下的遗传筛选）的检验功效。核心设定是：主研究有少量样本，辅助数据来自多个公共数据库，两者共享基因和细胞系等维度。方法通过一个多模态概率模型将辅助数据“蒸馏”为关于效应大小的先验信息，再构造FAB检验统计量，其形式为经典检验统计量加上一个由后验期望驱动的偏移项。关键机制是：若辅助信息与当前研究高度相关，FAB检验比经典t检验或z检验更敏感；若相关性低，则退化为经典检验，不损失功效。理论保证包括严格的type I error控制（在给定显著性水平下）和FDR控制（通过Benjamini-Hochberg程序）。模拟和实际数据分析（如CRISPR筛选）显示，在保持错误率的同时，发现效应数量显著增加。对您而言，该工作展示了如何将外部信息系统性地融入频率学派检验框架，与您对假设检验的兴趣直接相关，且其“蒸馏”思想可迁移至您熟悉的因果推断中利用辅助数据提升估计效率的场景。
- **关键技术**: `FAB (frequentist assisted by Bayes) testing`, `empirical Bayes prior distillation`, `multimodal probabilistic model`, `type I error control`, `false discovery rate control`
- **为什么对您有用**: 直接连接您primary interest中的“hypothesis testing”：本文提出一种新颖的融合外部信息的检验框架，与您熟悉的经典假设检验理论形成互补。从技术武器库看，您对“非参数统计”和“高维渐近”的熟悉度足以理解其核心机制（先验蒸馏与检验统计量构造），但若要深入分析其最优性（如能否达到渐近功效上界），可能需要调用您moderately_familiar的“semiparametric theory”来刻画信息利用的效率边界。中期可做：若您想将类似“蒸馏”思想用于因果推断中的敏感性分析或工具变量选择，需先在“identification theory in causal inference”上进一步积累。

### 2. [10.1093/biostatistics/kxab050](https://doi.org/10.1093/biostatistics/kxab050) — Bayesian multivariate probability of success using historical data with type I error rate control
- **作者**: Ethan M Alt, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **机构**: Brigham and Women's Hospital · Harvard University · University of North Carolina at Chapel Hill
- **分类**: vol 24 · issue 1 · pp 17-31
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对临床试验中多个临床结局（如共同主要终点或主要+多个次要终点）的多重性检验问题，提出一种贝叶斯方法。该方法基于看似无关回归模型显式建模结局间的相关性，从而得到处理效应联合后验分布。通过渐近控制第一类错误率，解决了贝叶斯多重比较中频率型错误率控制的难点。模拟表明，该方法比常用的Holm校正（Bonferroni的改进版）有更高检验功效。此外，作者发展了多元成功概率（multivariate probability of success）方法，用于在多个结局下稳健确定样本量。本文的核心技术工具是贝叶斯后验推断与渐近理论结合，属于假设检验与贝叶斯方法的交叉。对您而言，该文的多重性控制机制可迁移至因果推断中多个假设（如多个IV、多个中介路径）的联合检验问题，但核心机器（贝叶斯渐近）不在您的武器库中，属于暂不可做方向。
- **关键技术**: `Bayesian multiple testing`, `seemingly unrelated regression`, `type I error rate control`, `multivariate probability of success`, `asymptotic posterior validity`
- **为什么对您有用**: 连接至 hypothesis testing 子方向，但核心是贝叶斯渐近控制频率型错误率，与您熟悉的 minimax 和频率学派检验框架不同。武器库中 very_familiar 的非参/高维工具无法直接攻入其渐近论证；moderately_familiar 的 M-estimation 理论也不直接适用。暂不可做——缺贝叶斯渐近理论（如 Bernstein-von Mises 在多重比较下的推广）这一核心机器。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxab021](https://doi.org/10.1093/biostatistics/kxab021) · [arXiv](https://arxiv.org/abs/2203.06256) — Fast approximate inference for multivariate longitudinal data
- **作者**: David M Hughes, Marta García-Fiñana, Matt P Wand
- **期刊/来源**: Biostatistics
- **机构**: King Abdullah University of Science and Technology · Université de Bordeaux · Inserm · Bordeaux Population Health
- **分类**: vol 24 · issue 1 · pp 177-192
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对多变量纵向数据中多个高斯、泊松或二分类结局变量的联合建模问题，提出了一种基于平均场变分贝叶斯（MFVB）的快速近似推断算法。模型框架为多变量广义线性混合模型（MGLMM），通过引入潜在随机效应来刻画结局间的相关性和时间依赖性。核心机制是将变分分布分解为因子化形式，推导出坐标上升更新公式，从而将计算复杂度从MCMC的O(N^3)量级降至近似线性。在糖尿病视网膜病变和原发性胆汁性胆管炎两个临床数据集上，该方法在参数估计精度与MCMC相当的前提下，计算时间缩短了数个数量级。对您而言，本文展示了变分贝叶斯在大规模纵向数据中的实用化路径，其计算加速思路可迁移至您软件工具开发中的高维随机效应模型推断。
- **关键技术**: `mean field variational Bayes`, `multivariate generalized linear mixed model`, `coordinate ascent updates`, `computational scalability`
- **为什么对您有用**: 本文属于统计计算方向，直接对应您的primary interest中的'statistical computing (numerical methods, algorithm)'。您武器库中'very_familiar'的'软件工具开发'可直接用于复现或扩展其变分推断算法至更复杂的协方差结构。中期可做：若您想将MFVB推广至非共轭模型（如有序分类结局），需先在'moderately_familiar'的'M-estimation theory'上加强，以推导更一般的变分下界梯度。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biostatistics/kxab037](https://doi.org/10.1093/biostatistics/kxab037) — Joint frailty modeling of time-to-event data to elicit the evolution pathway of events: a generalized linear mixed model approach
- **作者**: Shu Kay Ng, Richard Tawiah, Geoffrey J Mclachlan, Vinod Gopalan
- **期刊/来源**: Biostatistics
- **机构**: Griffith University · The University of Melbourne · The University of Queensland
- **分类**: vol 24 · issue 1 · pp 108-123
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对多病共存（multimorbidity）的纵向时间-事件数据，提出一种联合脆弱模型（joint frailty model），以刻画事件间的演进路径。模型引入多元随机效应，同时处理异质性风险与由终止事件（如死亡）导致的信息删失。估计方法基于广义线性混合模型（GLMM）框架，通过似然函数实现参数的高效估计。作者利用黑色素瘤患者癌症登记数据展示模型的实际应用能力，并通过模拟研究比较所提模型与标准脆弱模型的相对表现。该工作为多病共存研究提供了纵向分析的新视角，有助于理解疾病进展路径。对您而言，本文是流行病学中因果推断方法的应用实例，其中联合建模与信息删失处理思路可迁移至您关注的纵向因果推断问题。
- **关键技术**: `joint frailty model`, `multivariate random effects`, `generalized linear mixed model`, `informative censoring`, `recurrent events`
- **为什么对您有用**: 本文属于流行病学应用，直接对应您的secondary interest。模型中的联合脆弱建模与信息删失处理，与您熟悉的纵向因果推断（如边际结构模型、g-formula）有方法学交叉。武器库中'identification theory in causal inference'可帮助您评估其因果假设的合理性，但核心估计方法（GLMM）不在您非常熟悉的工具中，属于'暂不可做'——需先补充混合效应模型与生存分析联合建模的文献。

### 2. [10.1093/biostatistics/kxab014](https://doi.org/10.1093/biostatistics/kxab014) — Semiparametric regression analysis of bivariate censored events in a family study of Alzheimer’s disease
- **作者**: Fei Gao, Donglin Zeng, Yuanjia Wang
- **期刊/来源**: Biostatistics
- **机构**: Fred Hutch Cancer Center · University of North Carolina at Chapel Hill · Columbia University
- **分类**: vol 24 · issue 1 · pp 32-51
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对家族研究中双变量区间删失事件（如阿尔茨海默病与心血管疾病共病）提出半参数回归模型。模型引入家族特异性随机效应和个体随机效应，分别刻画共享环境暴露和未观测遗传相关性的依赖结构。采用非参数最大似然估计（NPMLE）和稳定的EM算法进行参数估计，并建立了估计量的渐近性质。模拟研究验证了有限样本性能，实际数据分析表明AD与CVD共病的主要贡献来自遗传因素而非环境因素。该工作为家族共病模式分析提供了可处理区间删失数据的统计工具，对您而言，这是一篇流行病学应用论文，展示了半参数随机效应模型在真实队列数据中的分析流程，可作为您进入流行病学因果推断方向的入门读物。
- **关键技术**: `semiparametric regression`, `nonparametric maximum likelihood estimation`, `EM algorithm`, `interval-censored data`, `random effects model`
- **为什么对您有用**: 本文属于流行病学应用方向，直接对应您的secondary interest。它展示了半参数模型与随机效应在家族队列数据中的完整分析流程，包括区间删失处理、EM算法实现和渐近理论。作为入门读物，它清晰呈现了流行病学数据结构和模型假设，但核心方法（NPMLE+EM）已在您的武器库中（very_familiar的估计理论），因此可快速理解并评估其分析模式是否可迁移至您关注的因果推断问题（如家族研究中IV或mediation的识别）。

## 其他  *(other, 7 篇)*

### 1. [10.1093/biostatistics/kxab016](https://doi.org/10.1093/biostatistics/kxab016) · [arXiv](https://arxiv.org/abs/2005.11586) — Bayesian integrative analysis and prediction with application to atherosclerosis cardiovascular disease
- **作者**: Thierry Chekouo, Sandra E Safo
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 124-139
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出贝叶斯分层整合分析模型，用于同时关联多组学数据（如基因变异、基因表达）并预测临床结局（10年动脉粥样硬化性心血管疾病风险）。模型可整合先验功能信息（如基因通路）并纳入临床协变量，采用马尔可夫链蒙特卡洛进行后验推断。通过模拟和真实数据（健康成人的临床、人口学和基因组数据）验证，发现联合关联与预测模型优于两阶段方法（先关联后预测），并识别出若干与心血管疾病风险相关的遗传变异、基因和通路。方法学上属于贝叶斯变量选择与整合分析的结合，但未涉及因果推断或半参数效率理论。对您而言，本文是流行病学领域的应用工作，展示了多模态数据整合的贝叶斯框架，但方法学新颖性有限，与您的主要兴趣（因果推断、高维统计、U-统计量）直接关联较弱。
- **关键技术**: `Bayesian hierarchical model`, `Markov chain Monte Carlo`, `variable selection`, `multi-omics integration`, `pathway analysis`
- **为什么对您有用**: 本文属于流行病学应用（ASCVD风险预测），与您的secondary interest（流行病学数据集和因果推断应用）相关。但方法学上以贝叶斯变量选择为主，未涉及您武器库中的核心工具（如U-统计量、半参数效率界、DML）。作为入门读物，它清晰展示了多组学整合的贝叶斯建模流程，但缺乏您可立即攻克的统计问题。暂不可做——核心机器（贝叶斯分层模型与MCMC）不在您的武器库中，且方法学新颖性不足以驱动您投入时间。

### 2. [10.1093/biostatistics/kxab015](https://doi.org/10.1093/biostatistics/kxab015) — Single-index models with functional connectivity network predictors
- **作者**: Caleb Weaver, Luo Xiao, Martin A Lindquist
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 52-67
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出单指标模型（single-index model）用于处理功能连接网络预测变量，其中响应变量与稀疏功能连接网络通过未知光滑函数连接，以容纳潜在非线性关系。利用网络结构施加有意义的稀疏约束，不仅识别区域间交互与响应的关联，还评估脑区功能连接是否与响应相关。通过模拟研究和人类连接组项目静息态fMRI数据验证模型有效性，用于建模流体智力和性别。方法核心是单指标模型与网络稀疏约束的结合，但未涉及因果推断、高维统计或效率理论等核心兴趣领域。对您而言，本文属于应用统计方法，与您的主要兴趣方向（因果推断、高维统计等）直接关联较弱。
- **关键技术**: `single-index model`, `functional connectivity network`, `sparsity constraints`, `fMRI data analysis`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要兴趣方向（因果推断、高维随机矩阵理论、半参数效率理论等）直接关联较弱。武器库中的非参数统计和M估计理论可能部分相关，但核心方法（单指标模型+网络稀疏性）并非您熟悉或中度熟悉的工具。暂不可做：核心机器（功能连接网络建模、单指标模型估计）不在武器库中，且缺乏直接可迁移的问题口子。

### 3. [10.1093/biostatistics/kxab030](https://doi.org/10.1093/biostatistics/kxab030) — Capturing discrete latent structures: choose LDs over PCs
- **作者**: Theresa A Alexander, Rafael A Irizarry, Héctor Corrada Bravo
- **期刊/来源**: Biostatistics
- **机构**: University of Maryland, College Park · Dana-Farber Cancer Institute
- **分类**: vol 24 · issue 1 · pp 1-16
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对高维生物数据中离散潜在结构（如批次效应、未知细胞类型）的降维问题，提出迭代判别分析（iDA）方法。iDA 通过迭代地应用线性判别分析（LDA）来寻找最优分离潜在类别的线性变换，从而生成保留判别信息的低维嵌入。与主成分分析（PCA）仅关注总方差不同，iDA 直接优化类间分离度，克服了 PCA 在离散结构检测中的局限性。与 t-SNE 和 UMAP 等非线性方法相比，iDA 计算效率更高，且生成的线性变换具有可解释的特征权重，便于后续分析。模拟和实际数据实验表明，iDA 在保留离散结构信息方面优于 PCA，且计算成本远低于 t-SNE/UMAP。本文属于方法学应用，对您作为统计计算和因果推断研究者，其迭代判别框架可能启发您在高维混杂调整或潜在类别识别中的降维策略。
- **关键技术**: `iterative discriminant analysis (iDA)`, `linear discriminant analysis (LDA)`, `principal component analysis (PCA)`, `t-SNE`, `UMAP`, `dimensionality reduction`
- **为什么对您有用**: 本文属于统计计算方法应用，与您的统计计算兴趣相关。iDA 的迭代判别框架可迁移至因果推断中的高维混杂调整或潜在类别识别问题。武器库中的非参数统计和软件开发技能足以理解其核心逻辑，但本文方法学 novelty 有限，属于应用型工作，暂不可直接用于您的主要研究方向。

### 4. [10.1093/biostatistics/kxab025](https://doi.org/10.1093/biostatistics/kxab025) · [arXiv](https://arxiv.org/abs/1912.02399) — A sparse negative binomial mixture model for clustering RNA-seq count data
- **作者**: Yujia Li, Tanbin Rahman, Tianzhou Ma, Lu Tang, George C Tseng
- **期刊/来源**: Biostatistics
- **机构**: University of Pittsburgh
- **分类**: vol 24 · issue 1 · pp 68-84
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对RNA-seq计数数据的小n大p聚类问题，提出稀疏负二项混合模型（SNBMM），直接在原始计数上建模而非先归一化再假设高斯分布。模型引入lasso或fused lasso正则化实现基因层面的变量选择，通过改进的EM算法和BIC确定调参。模拟和两个真实转录组应用（大鼠脑、乳腺癌）表明，相比稀疏高斯混合模型和稀疏K-means，SNBMM在聚类准确率、特征选择和通路生物学解释上均更优。方法学上属于应用驱动的模型开发，核心贡献在于将计数数据分布假设与稀疏聚类框架结合。对您而言，本文是流行病学或生物统计中聚类分析的应用案例，但方法学新颖性有限（现有稀疏混合模型框架的分布扩展），且与您的主要兴趣方向（因果推断、高维统计、U统计量）无直接技术连接。
- **关键技术**: `negative binomial mixture model`, `lasso regularization`, `fused lasso`, `EM algorithm`, `BIC tuning`
- **为什么对您有用**: 本文属于流行病学/生物统计的应用工作，与您的secondary interest（流行病学数据集、应用因果工作）有弱连接，可作为了解RNA-seq数据聚类分析现状的入门读物。但方法学核心（稀疏混合模型+计数分布）不在您的技术武器库中，且无因果推断或高维统计理论的新贡献，不值得花时间精读全文。

### 5. [10.1093/biostatistics/kxab011](https://doi.org/10.1093/biostatistics/kxab011) — Accounting for technical noise in Bayesian graphical models of single-cell RNA-sequencing data
- **作者**: Jihwan Oh, Changgee Chang, Qi Long
- **期刊/来源**: Biostatistics
- **机构**: University of Pennsylvania
- **分类**: vol 24 · issue 1 · pp 161-176
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对单细胞RNA测序数据中因dropout和扩增偏差导致的零膨胀问题，提出scLGM（单细胞潜在图模型）——一个贝叶斯层次模型，用于估计基因间的条件依赖网络。模型利用UMI（唯一分子标识符）和ERCC（外源RNA控制联盟）分子数据，显式建模零膨胀的两个来源。采用贝叶斯推断框架，通过MCMC进行后验采样。模拟和真实数据分析表明scLGM在恢复基因网络方面优于现有方法。该工作属于生物信息学应用，方法学贡献在于将零膨胀噪声建模融入图模型，但未涉及因果推断、高维统计或半参效率理论等核心兴趣方向。
- **关键技术**: `Bayesian hierarchical model`, `graphical model`, `zero-inflation modeling`, `single-cell RNA-seq`, `MCMC`
- **为什么对您有用**: 本文属于生物统计应用，与主要兴趣（因果推断、高维统计、半参理论）无直接关联。武器库中的非参数统计或高维渐近理论可能用于分析其模型一致性，但方法本身不涉及因果识别或效率理论。作为流行病学数据集的入门阅读价值有限，因为scRNA-seq数据结构和分析目标与流行病学队列研究差异较大。暂不可做：核心机器（贝叶斯图模型、MCMC）不在武器库中，且问题设定与研究者方向距离较远。

### 6. [10.1093/biostatistics/kxab023](https://doi.org/10.1093/biostatistics/kxab023) · [arXiv](https://arxiv.org/abs/2104.01822) — Tailored Bayes: a risk modeling framework under unequal misclassification costs
- **作者**: Solon Karapanagiotis, Umberto Benedetto, Sach Mukherjee, Paul D W Kirk, Paul J Newcombe
- **期刊/来源**: Biostatistics
- **分类**: vol 24 · issue 1 · pp 85-107
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出 Tailored Bayes (TB) 框架，针对二分类风险预测模型中误分类成本不相等的问题，在贝叶斯推断中直接优化与成本相关的预测性能度量。TB 将误分类成本函数嵌入模型拟合过程，而非在事后调整阈值，从而在模型训练阶段就“定制”后验分布。通过模拟研究展示了在逻辑回归设定下 TB 相对于标准贝叶斯方法的优势。在三个真实医疗数据集（心脏手术、乳腺癌预后、乳腺癌肿瘤分类）上，TB 在成本加权预测误差上优于标准方法。该方法本质上是贝叶斯决策理论的应用，而非统计推断或因果推断的新理论。对您而言，本文属于应用统计方法，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接技术连接，但可作为医疗风险建模中成本敏感学习的参考案例。
- **关键技术**: `Bayesian decision theory`, `cost-sensitive learning`, `logistic regression`, `predictive performance optimization`
- **为什么对您有用**: 本文属于医疗领域的应用统计方法，与您的主要兴趣方向（因果推断、高维统计、U-统计量、半参效率理论等）无直接技术连接。武器库中无对应工具可攻该文的具体口子。暂不可做——核心机器（贝叶斯决策理论、成本敏感学习）不在武器库中。可作为了解医疗风险建模中成本敏感问题的入门读物，但不值得花时间全文精读。

### 7. [10.1093/biostatistics/kxab026](https://doi.org/10.1093/biostatistics/kxab026) — A Bayesian nonparametric model for classification of longitudinal profiles
- **作者**: Jeremy T Gaskins, Claudio Fuentes, Rolando De La Cruz
- **期刊/来源**: Biostatistics
- **机构**: University of Louisville · Oregon State University · Adolfo Ibáñez University
- **分类**: vol 24 · issue 1 · pp 209-225
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对纵向数据下的疾病分类问题，提出一种贝叶斯非参数模型。传统方法分别对健康与患病群体的纵向响应建模，再通过贝叶斯定理计算疾病概率，但当群体内存在显著异质性时效果不佳。作者将疾病状态与纵向响应视为联合结果，利用狄利克雷过程（Dirichlet process）诱导的聚类结构进行灵活分类，允许存在健康、患病及混合归属的多个子群体。模型通过马尔可夫链蒙特卡洛（MCMC）抽样实现推断与预测。在智利女性辅助生殖治疗的人绒毛膜促性腺激素β亚单位激素纵向数据上，该方法用于预测妊娠结局。本文方法学贡献在于贝叶斯非参数框架下的纵向分类，但未涉及因果推断、高维统计或效率理论等核心兴趣方向。
- **关键技术**: `Bayesian nonparametric model`, `Dirichlet process`, `Markov chain Monte Carlo`, `longitudinal data classification`
- **为什么对您有用**: 本文属于流行病学应用（妊娠结局预测），但方法学核心是贝叶斯非参数聚类，与您的主要兴趣（因果推断、高维统计、效率理论）无直接交集。武器库中无贝叶斯非参数工具，暂不可做。若您想了解纵向数据分类的流行病学应用，可作为入门阅读，但方法学迁移价值有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

