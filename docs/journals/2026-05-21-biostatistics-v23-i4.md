# Biostatistics — Vol 23  Issue 4  ·  2026-05-21

- 共 8 篇 · Biostatistics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1093/biostatistics/kxac027](https://doi.org/10.1093/biostatistics/kxac027) — Marginal structural models for multilevel clustered data
- **作者**: Yujie Wu, Benjamin Langworthy, Molin Wang
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1056-1073
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在纵向因果推断中，针对具有多层次聚类结构（如个体、时间与中心嵌套）的重复测量数据，本文研究如何拟合边际结构模型（MSM）以估计时变暴露的因果效应。提出两种方法处理多层次相关性：一是直接在加权广义估计方程（GEE）中对重复结局的协方差结构进行建模；二是两阶段法，先拟合聚类特异性的MSM，再利用混合效应元分析合并参数估计。有限样本模拟表明，考虑多层次相关性可减少偏差并提升估计效率；同时探讨了存在未测量聚类水平混杂时，固定效应与混合效应模型估计处理概率对MSM参数的影响。实证分析应用于CHEARS AAA数据集评估阿司匹林对听力损失的因果效应。对您有用：该文将纵向MSM扩展至多层次结构，其处理聚类内相关性的GEE与元分析策略对您在纵向因果推断及流行病学应用中的效率提升与稳健性考量有直接参考价值。
- **关键技术**: `marginal structural models`, `inverse probability weighting`, `weighted generalized estimating equations`, `mixed-effects meta-analysis`, `multilevel clustered data`
- **为什么对您有用**: 扩展了纵向因果推断中MSM的适用范围至多层次聚类数据，其利用协方差建模和两阶段元分析提升效率的策略，以及探讨未测量聚类混杂对IPW影响的视角，对您在纵向因果推断和流行病学应用中的研究有直接的方法迁移价值。

### 2. [10.1093/biostatistics/kxab020](https://doi.org/10.1093/biostatistics/kxab020) — Adaptive randomization in a two-stage sequential multiple assignment randomized trial
- **作者**: Junyao Wang, Liwen Wu, Abdus S Wahed
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1182-1199
- 相关性 0/10 · novelty: `minor`
- **摘要**: 在两阶段序贯多重分配随机试验（SMART）设定下，目标是优化动态治疗策略（DTR）的分配机制，克服等概率随机化导致的招募困难和依从性低等问题。本文提出响应自适应 SMART（RA-SMART）设计，根据前期累积的治疗效果信息动态调整后续阶段的分配概率，使其偏向更优治疗方案。文章通过大量模拟评估了 RA-SMART 相较于传统 SMART 的操作特性，包括 DTR 响应率估计的相合性与效率、识别最优 DTR 的检验功效，以及最优与最差 DTR 下的患者分配比例。模拟结果表明，RA-SMART 在提升伦理收益（更多患者接受最优治疗）的同时，对 DTR 估计的相合性无偏且效率损失有限。对您而言，该文涉及纵向因果推断中的 DTR 设定，但侧重于试验设计而非半参数效率或识别理论，可作为了解自适应随机化在 SMART 中应用的背景阅读。
- **关键技术**: `dynamic treatment regimes`, `response-adaptive randomization`, `sequential multiple assignment randomized trial`, `operating characteristics`
- **为什么对您有用**: 涉及纵向因果推断中的动态治疗策略（DTR）设计，但侧重于试验分配机制而非半参数效率或识别理论，可作为了解自适应随机化在 SMART 中应用的背景阅读。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxac017](https://doi.org/10.1093/biostatistics/kxac017) — Estimation of sparse functional quantile regression with measurement error: a SIMEX approach
- **作者**: Carmen D Tekwe, Mengli Zhang, Raymond J Carroll, Yuanyuan Luan, Lan Xue, Roger S Zoh et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1218-1241
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在函数型协变量存在异方差测量误差的设定下，本文研究线性分位数回归的一致估计问题，目标是修正测量误差导致的回归分位数偏差。提出两阶段策略：第一阶段利用工具变量估计测量误差的协方差结构；第二阶段采用 SIMEX（simulation extrapolation）对函数型协变量的测量误差进行修正，将传统标量 SIMEX 推广至函数型数据并允许异方差误差。逐点标准误通过非参数 bootstrap 估计。模拟表明修正后估计在偏差和覆盖率上显著优于朴素方法；NHANES 实证分析体力活动与 BMI 的关系。对您有用：IV 修正测量误差的思路可与 proximal CI 中 negative control 的 identification 策略对话，且函数型协变量的 SIMEX 框架对纵向因果推断中时变暴露的测量误差问题有迁移价值。
- **关键技术**: `SIMEX`, `instrumental variable for measurement error`, `functional quantile regression`, `nonparametric bootstrap`, `heteroscedastic measurement error`
- **为什么对您有用**: IV 修正测量误差的思路可与 proximal CI 中 negative control 的 identification 策略对话；函数型协变量的 SIMEX 框架对纵向因果推断中时变暴露的测量误差问题有迁移价值；NHANES 数据集对流行病学应用有参考价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biostatistics/kxac001](https://doi.org/10.1093/biostatistics/kxac001) — Estimation and false discovery control for the analysis of environmental mixtures
- **作者**: Srijata Samanta, Joseph Antonelli
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1039-1055
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在环境流行病学的混合暴露分析设定下，目标是识别与结局相关的暴露及交互作用，而现有灵活回归加变量选择的方法无法控制暴露选择的错误率。本文提出两种新方法，在利用灵活回归估计混合暴露总体效应并提供有效推断的同时，通过结合变量选择与 FDR 控制程序来识别重要暴露与交互作用。核心机制在于构建能够同时进行效应估计与选择后推断的框架，并在高维暴露设定下保证 FDR 的渐近控制。理论与模拟表明，该方法在检测弱效应暴露时显著提升了检验功效。对持久性有机污染物的实证分析显示，控制 FDR 会得出与传统方法截然不同的结论。对您有用：该文将多重假设检验（FDR 控制）引入混合暴露模型，为高维变量选择中的假设检验问题提供了新思路，且其环境流行病学数据集对您的流行病学应用兴趣有参考价值。
- **关键技术**: `false discovery rate control`, `environmental mixtures`, `variable selection`, `flexible regression`, `multiple hypothesis testing`
- **为什么对您有用**: 该文将 FDR 控制引入高维混合暴露的变量选择，直接契合您对假设检验的兴趣；同时其环境流行病学的应用场景和数据集对您的 secondary interest（流行病学应用）有实际参考价值。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1093/biostatistics/kxab035](https://doi.org/10.1093/biostatistics/kxab035) — A note on median regression for complex surveys
- **作者**: Raphael A Fraser, Stuart R Lipsitz, Debajyoti Sinha, Garrett M Fitzmaurice
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1074-1082
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文研究复杂抽样调查中偏斜响应变量的中位数回归，目标参数为条件中位数系数，关键假设为正确纳入抽样设计。针对传统分位数回归方差估计因忽略调查设计而失准的问题，作者提出将调查设计（分层、整群、权重）显式纳入方差估计过程。核心方法基于设计基推断（design-based inference），对中位数回归估计量的方差进行校正，模拟显示其相对偏差极小且覆盖概率达标。实证基于 NHANES 数据，展示调整协变量后性别对碘缺乏的影响。对您而言，本文提供了 NHANES 流行病学数据集的应用范例，但方法学属于标准调查抽样方差校正，对半参数效率或高维理论的借鉴价值较低。
- **关键技术**: `median regression`, `design-based variance estimation`, `complex survey sampling`, `sampling weights`
- **为什么对您有用**: 涉及流行病学（NHANES 数据集）的次级兴趣，但方法学属于标准调查抽样方差校正，对您关注的半参数效率或高维理论无直接推进，仅作数据集参考。

## 其他  *(other, 3 篇)*

### 1. [10.1093/biostatistics/kxac021](https://doi.org/10.1093/biostatistics/kxac021) — A probabilistic gene expression barcode for annotation of cell types from single-cell RNA-seq data
- **作者**: Isabella N Grabski, Rafael A Irizarry
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1150-1164
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对单细胞 RNA-seq 数据中的细胞类型注释问题，提出一种基于潜变量模型的概率条形码方法，目标 estimand 为细胞类型身份的后验概率。方法利用公共参考数据集跨数千个基因整合信息，通过 latent variable model 定义细胞类型特异的 barcode 并显式建模批次效应，再以概率方式将查询细胞注释到已知参考类型。该 barcode 框架同时提供了一种新的 marker gene 发现途径。在多组跨研究数据集（包括不完美参考数据）上，该方法显著优于现有 reference-based 方法，尤其在跨研究预测场景下。该方法学与您关注的 semiparametric efficiency、高维推断理论无直接关联，latent variable 模型设定也偏离您核心的因果/效率理论方向。
- **关键技术**: `latent variable model`, `batch effect correction`, `probabilistic annotation`, `reference-based cell typing`, `empirical Bayes`
- **为什么对您有用**: 与您的主要研究方向（因果推断、RMT、半参数效率界、U-统计量）基本无直接关联；latent variable 建模批次效应的思路可作泛化参考，但技术迁移价值有限。

### 2. [10.1093/biostatistics/kxab046](https://doi.org/10.1093/biostatistics/kxab046) — Separating and reintegrating latent variables to improve classification of genomic data
- **作者**: Nora Yujia Payne, Johann A Gagnon-Bartsch
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1133-1149
- 相关性 2/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "在高维基因组数据分类中，密集的潜在变量既可能包含与表型相关的预测信息，也可能掩盖稀疏的弱信号，本文旨在解决此分类问题。提出交叉残差分类器（CRC），首先估计并残差化去除潜在变异（类似 RUV/SVA），然后在残差上训练基分类器以提取稀疏信号，最后将潜在变异重新整合进集成分类器中。该过程通过交叉拟合避免过拟合，保留了潜在变量中的预测信息同时消除了其噪声干扰。模拟与多平台基因组真实数据表明，CRC 相较于现有分类器有稳健提升，尤其在潜在变异强且信号稀疏时增益显著。对您有用：CRC 的残差化步骤与 DML 的正交化及 Proximal CI 中基于 negative control 的 RUV 调整思想高度同源，其"分离-重整"策略可为因果推断中处理潜在混杂的效率提升提供算法借鉴。",
  "key_techniques": [
    "cross-residualization",
    "latent variable adjustment",
    "Remove Unwanted Variation (RUV)",
    "ensemble classification",
    "cross-fitting"
  ],
  "why_relevant": "CRC的残

### 3. [10.1093/biostatistics/kxac022](https://doi.org/10.1093/biostatistics/kxac022) — A hierarchical prior for generalized linear models based on predictions for the mean response
- **作者**: Ethan M Alt, Matthew A Psioda, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 4 · pp 1165-1181
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在广义线性模型（GLM）框架下，提出了一种基于均值响应预测的分层先验（hierarchical prediction prior, HPP），扩展了 Chen & Ibrahim (2003) 的共轭先验，将先验预测视为随机变量。在 i.i.d. 正态线性模型设定下，作者推导了超先验仍为共轭先验的条件；同时开发了利用历史研究汇总统计量的 HPP 扩展形式，允许根据个体预测质量进行折扣加权。与共轭先验和 power prior 的模拟对比表明，HPP 在先验与数据冲突时具有更低的 MSE；作者还设计了高效的 MCMC 算法。该工作属于参数贝叶斯先验构造，与您关注的半参数效率界、因果推断及高维理论方向重叠有限，但其中先验-数据冲突的鲁棒性思路和 MCMC 计算细节对统计计算子方向有轻微参考价值。
- **关键技术**: `hierarchical conjugate prior`, `power prior comparison`, `prior-data conflict robustness`, `MCMC sampling`, `GLM prior elicitation`
- **为什么对您有用**: 与您的主要兴趣方向（因果推断、半参数效率、高维/RMT、U-统计量）重叠很小；仅 MCMC 算法设计与统计计算子方向有轻微关联，先验-数据冲突鲁棒性概念可类比敏感性分析思路，但整体收益有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

