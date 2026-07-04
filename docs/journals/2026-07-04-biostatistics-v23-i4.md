# Biostatistics — Vol 23  Issue 4  ·  2026-07-04

- 共 8 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 4 篇（对照 OpenAlex 12 篇）：10.1093/biostatistics/kxab048、10.1093/biostatistics/kxac005、10.1093/biostatistics/kxab049、10.1093/biostatistics/kxab045

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》第23卷第4期的8篇论文，整体上围绕**因果推断中的复杂数据结构处理**与**高维/非标准数据的统计方法**两条主线展开。因果推断主线集中于多水平聚类数据、环境混合物分析、自适应试验设计及复杂抽样下的中位数回归；另一主线则涵盖函数型数据、贝叶斯先验、单细胞注释及基因组分类中的潜在变量问题。其中，因果推断方向占据近半数篇幅，且方法工具涉及逆概率加权、FDR控制、响应自适应随机化及调查设计方差校正。

在因果推断主线中，最突出的主题是**对传统因果估计方法在复杂数据场景下的扩展与效率改进**。例如，“Marginal structural models for multilevel clustered data”一文针对多水平聚类数据中的时变暴露，提出了两种处理聚类相关性的MSM扩展（加权GEE与两阶段meta分析），并探讨了未测量混杂对治疗概率模型的影响。“Estimation and false discovery control for the analysis of environmental mixtures”则聚焦环境混合物分析，将变量选择与FDR控制结合，通过数据分割与debiased lasso实现整体效应推断与错误发现率控制，理论证明渐近有效性。“Adaptive randomization in a two-stage sequential multiple assignment randomized trial”将响应自适应随机化引入SMART设计，旨在提高患者福利与试验效率，但未涉及识别假设或半参数效率。“A note on median regression for complex surveys”则从方差估计角度，将调查设计（分层、聚类、权重）纳入中位数回归的推断框架，直接服务于偏态分布响应数据的因果推断。

另一条主线是**非标准数据结构的统计建模**，包括函数型数据、贝叶斯先验与高维分类。“Estimation of sparse functional quantile regression with measurement error”将SIMEX方法从标量协变量扩展到函数型协变量，处理异方差测量误差，但技术路线与因果推断关联较弱。“A hierarchical prior for generalized linear models”提出层次预测先验，允许数据自适应调整先验强度，在先验-数据冲突时提升效率。“A probabilistic gene expression barcode for annotation of cell types”与“Separating and reintegrating latent variables to improve classification of genomic data”分别处理单细胞注释与基因组分类中的潜在变量问题，前者利用潜变量模型校正批次效应，后者通过残差化与再集成处理潜在变异对分类的影响。

对于因果推断方向的研究者，优先关注“Marginal structural models for multilevel clustered data”（多水平聚类数据下的因果参数估计与效率）、“Estimation and false discovery control for the analysis of environmental mixtures”（环境混合物因果效应推断与FDR控制）以及“Adaptive randomization in a two-stage sequential multiple assignment randomized trial”（自适应试验设计在DTR比较中的应用）。对于半参数效率或高维统计方向，“A note on median regression for complex surveys”提供了复杂抽样下中位数回归的方差校正思路，而“Estimation of sparse functional quantile regression with measurement error”展示了函数型数据中测量误差校正的SIMEX扩展。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biostatistics/kxac027](https://doi.org/10.1093/biostatistics/kxac027) — Marginal structural models for multilevel clustered data
- **作者**: Yujie Wu, Benjamin Langworthy, Molin Wang
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Brigham and Women's Hospital
- **分类**: vol 23 · issue 4 · pp 1056-1073
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文针对多水平聚类数据（如重复测量嵌套于参与者、时间、测试站点）中的时变暴露因果效应估计，扩展了边际结构模型（MSM）的应用。目标估计量是MSM中的因果参数，在逆概率治疗加权（IPTW）框架下处理时依混杂。方法一：在加权广义估计方程（WGEE）中直接对重复结局的协方差结构建模，以纳入多水平相关性；方法二：两阶段分析，先拟合聚类特异性MSM，再通过混合效应meta分析合并参数估计。模拟表明，两种方法相比忽略聚类相关性的标准MSM，能获得更小偏倚和更高效率的参数估计。此外，文章探讨了在存在未测量聚类水平混杂时，用固定效应或混合效应模型估计治疗概率对MSM参数估计的影响。最后应用于CHEARS AAA数据集，估计阿司匹林使用对听力损失的因果效应。对您而言，本文是纵向因果推断中处理复杂聚类结构的实用方法学案例，与您primary interest中的纵向因果推断和identification theory直接相关。
- **关键技术**: `marginal structural models`, `inverse probability treatment weighting`, `weighted generalized estimating equations`, `mixed-effects meta-analysis`, `multilevel clustered data`
- **为什么对您有用**: 本文直接连接您的primary interest中的纵向因果推断，特别是时变暴露下处理多水平聚类数据的identification和estimation问题。您的technical arsenal中'very_familiar'的estimation theory in causal inference可直接用于理解其WGEE和meta-analysis方法，而'moderately_familiar'的identification theory可帮助评估其未测量聚类混杂的敏感性。**中期可做**：若想进一步改进其效率或处理更复杂的聚类结构，需先在'moderately_familiar'的semiparametric theory上提升，以推导更高效的估计方程。

### 2. [10.1093/biostatistics/kxac001](https://doi.org/10.1093/biostatistics/kxac001) · [arXiv](https://arxiv.org/abs/2103.10563) — Estimation and false discovery control for the analysis of environmental mixtures
- **作者**: Srijata Samanta, Joseph Antonelli
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1039-1055
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对环境混合物分析中的两个核心目标——估计整体混合物效应与识别重要暴露及交互作用——提出了两种新方法。在环境流行病学中，现有方法虽能进行变量选择，但无法控制任何形式的错误发现率。方法一基于变量筛选后的回归模型，通过数据分割与多重检验校正实现FDR控制；方法二则利用debiased lasso构造检验统计量，在控制FDR的同时对整体混合物效应进行有效推断。理论证明两种方法均能渐近控制FDR，且相比传统方法在检测弱效应时具有显著功效提升。应用于持久性有机污染物研究时，控制FDR导致与未控制时截然不同的结论。对您而言，本文展示了在因果推断框架下如何将变量选择与FDR控制结合，其debiased lasso思路可迁移至您熟悉的high-dimensional asymptotics与causal inference中的sensitivity analysis设定。
- **关键技术**: `debiased lasso`, `false discovery rate control`, `data splitting`, `multiple testing correction`, `variable selection`, `environmental mixtures`
- **为什么对您有用**: 本文直接连接您的primary interest中的causal inference（环境混合物效应识别）与high-dimensional statistics（debiased lasso用于FDR控制）。您武器库中very_familiar的high-dimensional asymptotics可直接用于验证其debiased lasso的渐近性质是否在更一般的因果结构（如proximal CI）下成立。中期可做：需先在moderately_familiar的identification theory in causal inference上长肌肉，以将FDR控制方法推广至存在未测量混杂的设定。

### 3. [10.1093/biostatistics/kxab020](https://doi.org/10.1093/biostatistics/kxab020) — Adaptive randomization in a two-stage sequential multiple assignment randomized trial
- **作者**: Junyao Wang, Liwen Wu, Abdus S Wahed
- **期刊/来源**: Biostatistics
- **机构**: University of Pittsburgh
- **分类**: vol 23 · issue 4 · pp 1182-1199
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对序贯多阶段随机试验（SMART）提出响应自适应随机化（RA-SMART）设计，目标是在多阶段动态治疗策略（DTR）比较中提高患者福利和试验效率。传统SMART在各阶段对各治疗臂等概率随机化，可能导致低招募率、低保留率和低依从性。RA-SMART根据累积的疗效信息（来自先前患者和阶段）调整分配概率，使更多患者被分到更有希望的治疗臂。通过模拟研究评估了RA-SMART相对于传统SMART在DTR下响应率估计的一致性、识别最优DTR的检验功效以及分配到最优/最差DTR的患者数等操作特性。该方法本质上是因果推断中自适应试验设计的一个变体，但未涉及识别假设或半参数效率理论。对您而言，该文可作为纵向因果推断中试验设计的一个应用案例，但方法学新颖性有限。
- **关键技术**: `response-adaptive randomization`, `sequential multiple assignment randomized trial`, `dynamic treatment regimes`, `simulation-based evaluation`
- **为什么对您有用**: 该文涉及纵向因果推断中的试验设计（SMART），与您的primary interest 'causal inference (longitudinal)' 有直接连接。但方法学贡献主要是模拟驱动的应用型工作，未涉及identification或efficiency theory。武器库中'very_familiar'的'causal inference estimation theory'可理解其设计逻辑，但无新理论问题可攻。暂不可做：核心机器不在武器库里，缺adaptive randomization的formal theory（如bandit、regret bound）。

### 4. [10.1093/biostatistics/kxab035](https://doi.org/10.1093/biostatistics/kxab035) — A note on median regression for complex surveys
- **作者**: Raphael A Fraser, Stuart R Lipsitz, Debajyoti Sinha, Garrett M Fitzmaurice
- **期刊/来源**: Biostatistics
- **机构**: Medical College of Wisconsin · Harvard University · Florida State University
- **分类**: vol 23 · issue 4 · pp 1074-1082
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对复杂抽样调查中响应变量偏态分布的问题，提出在分位数回归（尤其是中位数回归）中正确估计方差的方法。核心贡献在于将调查设计（如分层、聚类、抽样权重）纳入方差估计过程，而非仅使用独立同分布假设下的标准误差。通过模拟研究，展示了所提方差估计量的相对偏倚很小且覆盖概率适当。方法动机来自美国国家健康与营养调查（NHANES），并应用于碘缺乏与性别关系的实证分析。对您而言，该文展示了在复杂抽样设计下如何正确进行推断，这与您因果推断中处理纵向或调查数据时的方差估计问题直接相关。
- **关键技术**: `quantile regression`, `median regression`, `survey design variance estimation`, `complex survey sampling`, `coverage probability`
- **为什么对您有用**: 本文直接关联您 primary interest 中的因果推断（纵向/调查数据）和假设检验（方差估计的正确性）。技术武器库中“非参数统计”和“因果推断中的估计理论”可用于理解其方差估计的稳健性，但核心方法（分位数回归的 survey 方差）属于 moderately_familiar 的 M-估计理论范畴。中期可做：若您想在复杂抽样下拓展因果推断方法（如 IV 或 mediation），需先熟悉 survey 加权和设计效应。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biostatistics/kxac017](https://doi.org/10.1093/biostatistics/kxac017) — Estimation of sparse functional quantile regression with measurement error: a SIMEX approach
- **作者**: Carmen D Tekwe, Mengli Zhang, Raymond J Carroll, Yuanyuan Luan, Lan Xue, Roger S Zoh et al.
- **期刊/来源**: Biostatistics
- **机构**: Indiana University Bloomington · Oregon State University · Texas A&M University · University of South Carolina · Sapienza University of Rome
- **分类**: vol 23 · issue 4 · pp 1218-1241
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究函数型协变量存在异方差测量误差时的稀疏分位数回归估计问题。目标是在函数型线性分位数回归模型中，对带误差的函数型协变量进行一致性估计。方法采用两阶段策略：第一阶段利用工具变量估计测量误差的协方差矩阵；第二阶段使用SIMEX（模拟外推）方法校正函数型协变量中的测量误差。标准误通过非参数bootstrap估计。模拟研究评估了校正方法的稳健性，并应用于NHANES数据，分析体力活动与BMI的关系。该方法主要贡献在于将SIMEX从标量协变量扩展到函数型协变量，并处理异方差误差。对您而言，本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计等）直接关联较弱，但测量误差校正思路在流行病学数据分析中可能有参考价值。
- **关键技术**: `SIMEX (simulation extrapolation)`, `functional quantile regression`, `instrumental variable for measurement error`, `nonparametric bootstrap`
- **为什么对您有用**: 本文属于流行病学应用论文，与您的secondary interest（epidemiology）相关，但方法学创新有限（主要是将SIMEX从标量扩展到函数型协变量）。您的武器库中'非参数统计'和'因果推断中的估计理论'可帮助理解其方法框架，但核心问题（函数型数据分位数回归+测量误差）与您的主要兴趣方向交集不大。暂不可做——缺乏函数型数据分析的专门工具。

### 2. [10.1093/biostatistics/kxac022](https://doi.org/10.1093/biostatistics/kxac022) · [arXiv](https://arxiv.org/abs/2107.11195) — A hierarchical prior for generalized linear models based on predictions for the mean response
- **作者**: Ethan M Alt, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1165-1181
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对广义线性模型（GLM）提出了一种层次预测先验（HPP），扩展了Chen & Ibrahim (2003)的共轭先验框架。核心创新在于将均值响应的先验预测视为随机变量而非固定值，从而允许数据对先验进行自适应调整。在独立同分布设定和正态线性模型下，作者推导了超先验为共轭先验的条件，并给出了基于历史研究汇总统计量的扩展版本。HPP通过个体层面预测的质量进行折扣，模拟表明在先验与数据冲突时，HPP相比共轭先验和power prior在均方误差上有效率提升。开发了高效的MCMC算法。应用示例显示HPP对先验-数据冲突的鲁棒性优于选定的非层次先验。该工作属于贝叶斯先验构建的方法论，与您的主要兴趣（因果推断、高维统计等）无直接技术交集，但若您未来涉及贝叶斯因果推断或罕见病临床试验中的先验设定，可作参考。
- **关键技术**: `hierarchical prediction prior`, `conjugate prior`, `power prior`, `MCMC algorithm`, `generalized linear models`
- **为什么对您有用**: 本文属于贝叶斯统计方法，与您的主要兴趣方向（因果推断、高维统计、半参理论等）无直接技术连接。您的武器库中缺乏贝叶斯先验构建的核心工具（如共轭先验理论、MCMC采样），因此暂不可做。若未来您涉足贝叶斯因果推断或罕见病临床试验中的先验设定，可作为入门阅读。

### 3. [10.1093/biostatistics/kxac021](https://doi.org/10.1093/biostatistics/kxac021) — A probabilistic gene expression barcode for annotation of cell types from single-cell RNA-seq data
- **作者**: Isabella N Grabski, Rafael A Irizarry
- **期刊/来源**: Biostatistics
- **机构**: Harvard University · Dana-Farber Cancer Institute
- **分类**: vol 23 · issue 4 · pp 1150-1164
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对单细胞RNA测序（scRNA-seq）数据中的细胞类型注释问题，提出了一种基于概率基因表达条形码的统计方法。现有方法依赖已知标记基因或易受批次效应影响导致过拟合。作者利用公共数据集整合数千个基因的信息，通过潜变量模型定义细胞类型特异性条形码，并同时建模批次效应，从而实现对细胞类型的概率性注释。该方法还提供了一种新的标记基因发现途径。在多个数据集（包括模拟真实世界参考数据不完美的场景）上的实验表明，该方法在跨研究预测时显著优于现有基于参考的方法。对您而言，本文属于生物信息学应用，与您的主要研究兴趣（因果推断、高维统计等）无直接技术关联，但展示了潜变量模型在批次效应校正中的实际应用。
- **关键技术**: `latent variable model`, `batch effect correction`, `probabilistic annotation`, `marker gene discovery`
- **为什么对您有用**: 本文属于生物信息学应用，与您的主要研究兴趣（因果推断、高维统计、半参理论等）无直接技术关联。它展示了潜变量模型在批次效应校正中的实际应用，但方法学新颖性有限，且不涉及您武器库中的核心工具（如U统计量、极小极大界、高效影响函数等）。作为流行病学或应用统计的入门阅读尚可，但鉴于您的时间优先级，不建议深入阅读。

### 4. [10.1093/biostatistics/kxab046](https://doi.org/10.1093/biostatistics/kxab046) · [arXiv](https://arxiv.org/abs/2012.11757) — Separating and reintegrating latent variables to improve classification of genomic data
- **作者**: Nora Yujia Payne, Johann A Gagnon-Bartsch
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1133-1149
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对基因组数据中未观测到的潜在变量（latent variables）对分类任务的影响，提出了一种新的分类方法——交叉残差化分类器（CRC）。这些潜在变量可能部分与表型相关（有帮助）或完全无关（仅增加噪声），同时可能掩盖仅影响少数特征的微弱信号。CRC通过两步调整与集成过程：首先估计并残差化潜在变量，在残差上训练分类器，然后将潜在变量重新集成到最终的集成分类器中，从而在不丢弃任何预测信息的前提下处理潜在变异。方法在模拟数据和多种基因组平台的实际数据上进行了验证，相比现有分类器表现良好，有时有显著提升。该方法本质上是针对高维、低信噪比数据的预测方法，与因果推断或效率理论无直接关联。
- **关键技术**: `cross-residualization`, `latent variable adjustment`, `ensemble classifier`, `genomic data classification`
- **为什么对您有用**: 本文属于基因组数据分类的应用方法，与您的主要兴趣（因果推断、高维统计、效率理论等）无直接交集。虽然涉及潜在变量处理，但方法核心是预测而非因果识别，且未提供理论保证（如收敛率或效率界）。作为流行病学或基因组学应用，其数据结构和分析流程对您当前武器库的迁移价值有限。暂不可做：核心机器不在武器库里（缺乏对潜在变量估计与集成分类器理论的分析工具）。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

