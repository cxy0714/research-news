# Biometrics — Vol 81  Issue 4  ·  2026-05-21

- 共 34 篇 · Biometrics

## 因果推断  *(causal_inference, 10 篇)*

### 1. [10.1093/biomtc/ujaf156](https://doi.org/10.1093/biomtc/ujaf156) — Bridging the gap between design and analysis: randomization inference and sensitivity analysis for matched observational studies with treatment doses
- **作者**: Jeffrey Zhang, Siyu Heng
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在匹配观察性研究中，针对连续或有序处理剂量，现有方法缺乏对 Neyman 弱零假设的随机化推断，且在非二元结果下缺乏对 Fisher 严零假设的有效敏感性分析。本文提出新的随机化推断与敏感性分析方法，适用于一般匹配设计下的处理剂量，兼容连续、有序及二元结果。核心机制在于构建适用于处理剂量的一般匹配设计的推断框架，同时覆盖 Fisher 严零假设与 Neyman 弱零假设两种检验视角。该方法填补了非二元结果下严零假设敏感性分析及弱零假设推断的空白，并通过模拟与实证数据验证了有效性。所有方法已整合至 R 包 doseSens。对您有用：该工作直接推进了因果推断中敏感性分析的工具箱，且其针对 Fisher/Neyman 零假设的随机化推断框架与您在假设检验和因果推断方向的兴趣高度契合。
- **关键技术**: `randomization inference`, `sensitivity analysis`, `Fisher's sharp null`, `Neyman's weak null`, `matched observational studies`, `treatment doses`
- **为什么对您有用**: 直接推进因果推断中敏感性分析的方法论，且其针对 Fisher 严零假设与 Neyman 弱零假设的随机化推断框架，与您在因果推断（sensitivity analysis）和假设检验方向的兴趣高度契合，R 包也便于计算实现。

### 2. [10.1093/biomtc/ujaf129](https://doi.org/10.1093/biomtc/ujaf129) — A meta-learning method for estimation of causal excursion effects to assess time-varying moderation
- **作者**: Jieru Shi, Walter Dempsey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在微观随机化试验(MRT)的纵向因果推断设定下，目标是估计随时间变化的因果偏移效应，但现有方法依赖已知随机化概率、完全观测及线性 nuisance 模型。本文提出 DR-WCLS 方法，从 meta-learner 视角构建 doubly robust 估计量，放宽了上述假设，允许使用灵活的机器学习模型拟合高维历史数据的 nuisance 函数。理论上证明了估计量的双向渐近性质与双重稳健性，在 nuisance 估计正确时可达半参数有效界，且在随机化概率不确定或存在缺失数据时仍保持一致性与更高效率。模拟与医学住院医生队列数据分析验证了该方法的实用优势。对您有用：该文将 meta-learning 思想引入纵向因果推断的 excursion effect，其 DR 构造与双向渐近理论对您在 longitudinal causal inference 与 efficiency theory 方面的研究有直接参考价值。
- **关键技术**: `causal excursion effects`, `doubly robust estimation`, `meta-learner`, `Micro-randomized trials`, `bidirectional asymptotics`
- **为什么对您有用**: 直接涉及 longitudinal causal inference 的估计量构建，采用 meta-learner 视角实现 doubly robust 估计，与您关注的 efficiency theory (DML) 和 semiparametric theory 高度契合，且提供了 mHealth 领域的流行病学应用范式。

### 3. [10.1093/biomtc/ujaf143](https://doi.org/10.1093/biomtc/ujaf143) — Adaptive stratified sampling design in two-phase studies for average causal effect estimation
- **作者**: Min Zeng, Qiyu Wang, Zijian Sui, Hong Zhang, Jinfeng Xu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在两阶段研究设定下，目标是当昂贵混杂因子仅对部分子集观测时估计平均因果效应(ACE)，关键假设是第一阶段变量(治疗、结果、廉价混杂)可全样本观测。本文提出自适应分层抽样设计(AdaStrat)，通过先导数据构建分层策略并确定各层抽样概率，以在给定第二阶段样本量下最小化 ACE 估计量的方差。理论证明了 AdaStrat 相较于固定分层抽样设计(FixStrat)具有更高的渐近效率，其核心在于利用第一阶段信息优化第二阶段的抽样权重。模拟与 UK Biobank 实证显示 AdaStrat 相对 FixStrat 效率提升 20%-30%。该工作将效率理论应用于两阶段因果推断的抽样设计，其自适应优化方差的思想可迁移至您关注的昂贵协变量或缺失数据下的半参数效率界讨论。
- **关键技术**: `two-phase study design`, `adaptive stratified sampling`, `average causal effect`, `variance minimization`, `pilot data stratification`
- **为什么对您有用**: 直接关联您 primary interest 中的因果推断与效率理论，展示了在两阶段昂贵混杂因子设定下如何通过优化抽样设计最小化 ACE 估计量方差；其 UK Biobank 实证对您 secondary interest 的流行病学应用也有数据集参考价值。

### 4. [10.1093/biomtc/ujaf134](https://doi.org/10.1093/biomtc/ujaf134) — Distal causal excursion effects: modeling long-term effects of time-varying treatments in micro-randomized trials
- **作者**: Tianchen Qian
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在微随机试验（MRT）的纵向因果推断设定下，目标是量化时变干预对远端结果的长期效应，突破现有因果游走效应仅限近端结果的局限。提出远端因果游走效应（DCEE）作为新 estimand，通过在大部分干预分配上边际化来对比游走策略下的远端结果，使高维决策点下的因果模型保持简约与可解释。构造了两种估计器（含 cross-fitting 与不含），均对结果模型误设具有鲁棒性（基于稳健得分/影响函数构造）。理论上建立了估计量的渐近性质（$n^{-1/2}$-CAN 及渐近正态性），模拟验证了有限样本表现。HeartSteps 实证表明早期干预的长期效应更强。对您有用：该工作直接推进了纵向时变干预的因果推断，其 cross-fitting 与鲁棒性构造对您关注的效率理论与半参数推断具有方法学迁移价值。
- **关键技术**: `distal causal excursion effect`, `micro-randomized trials`, `cross-fitting`, `robust estimation`, `longitudinal causal inference`, `time-varying treatments`
- **为什么对您有用**: 直接契合您 primary interest 中的纵向因果推断与时变干预；其 cross-fitting 估计器与对结果模型误设的鲁棒性（通常基于 influence function / 正交性）对您关注的效率理论与半参数推断有直接参考价值。

### 5. [10.1093/biomtc/ujaf161](https://doi.org/10.1093/biomtc/ujaf161) — Censoring-robust estimation in fixed sample time-to-event clinical trials with adaptive randomization
- **作者**: Navneet R Hakhu, Daniel L Gillen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在自适应随机化的固定样本生存分析试验中，目标是边际风险比在间歇性删失下的稳健估计。文章解析了自适应随机化如何改变删失模式，导致标准 Cox 比例风险估计量产生偏差。作为修正，作者提出了一种删失稳健估计量，通过利用处理特异性删失分布对偏似然得分进行重新加权来校正偏差。该估计量的渐近性质（一致性与渐近正态性）得到了严格推导，模拟显示其有效校正了有限样本偏差。实证分析应用于 AIDS 临床试验数据。对您有用：该文在复杂设计下通过修改得分方程实现稳健估计的思路，对您在 longitudinal 因果推断（时变混杂/删失）与半参数理论方面的研究具有直接的方法迁移价值。
- **关键技术**: `adaptive randomization`, `censoring-robust estimation`, `weighted partial likelihood`, `marginal hazard ratio`, `asymptotic normality`, `time-to-event analysis`
- **为什么对您有用**: 该文处理自适应随机化导致的依赖删失问题，属于半参数估计与因果推断的交叉；其修改得分方程实现稳健性的思路，对您在 longitudinal 因果推断和半参数效率理论方面的研究有方法迁移价值。

### 6. [10.1093/biomtc/ujaf162](https://doi.org/10.1093/biomtc/ujaf162) — Estimating heterogeneous treatment effects for general responses
- **作者**: Zijun Gao, Trevor Hastie
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在异质性处理效应（HTE）估计中，针对连续、二值、计数及生存等一般响应变量，传统 estimand 关注条件均值差，本文提出基于指数族与 Cox 模型的自然参数差（DINA）作为新 estimand。为估计 DINA，作者构建了一个 meta-algorithm，允许嵌入任意现成机器学习基学习器来估计干扰函数。该算法利用正交化思想，对干扰函数的估计误差具有鲁棒性，从而实现 n^{-1/2}-CAN 的渐近性质。理论分析与模拟实验表明，DINA 在不同响应类型下比传统均值差更实用且更易建模协变量对处理效应的影响。对您有用：本文将指数族自然参数引入 HTE estimand，并结合 orthogonal meta-learner，直接契合您在因果推断估计和 efficiency theory/debiased ML 方向的兴趣，展示了在非连续响应下构造 nuisance-robust 估计量的具体路径。
- **关键技术**: `heterogeneous treatment effects`, `exponential family`, `natural parameter`, `orthogonal meta-algorithm`, `nuisance robustness`, `debiased machine learning`
- **为什么对您有用**: 提出了基于指数族的新 HTE estimand (DINA) 及其 orthogonal meta-algorithm，直接契合您在因果推断估计和 efficiency theory/debiased ML 方向的兴趣，展示了如何在非连续响应下构造 nuisance-robust 的半参数有效估计量。

### 7. [10.1093/biomtc/ujaf131](https://doi.org/10.1093/biomtc/ujaf131) — Statistical inference for heterogeneous treatment effect with right-censored data from synthesizing randomized clinical trials and real-world data
- **作者**: Guangcai Mao, Shu Yang, Xiaofei Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在右删失生存数据下，通过融合随机临床试验（RCT）与存在偏差的真实世界数据（RWD），研究异质性处理效应（HTE）的估计，目标参数为给定协变量下处理特异的条件限制平均生存时间（cRMST）之差。为刻画RWD中由未测量混杂、删失和结局异质性引起的偏差，作者定义了全能偏差函数并利用RCT与RWD的联合信息实现其非参数识别。基于此，提出惩罚筛法同时估计HTE与偏差函数，并结合再生核希尔伯特空间（RKHS）与经验过程理论推导了积分估计量的理论性质，表明融合RWD可提升估计效率。模拟与早期非小细胞肺癌的实际数据分析验证了该方法优于仅用RCT的估计。对您有用：本文将RKHS与筛法应用于因果推断的数据融合与未测量混杂校正，其偏差函数识别策略和半/非参理论工具可直接迁移至您关注的因果推断（混杂敏感性/数据融合）与半参数理论研究中。
- **关键技术**: `penalized sieve estimation`, `reproducing kernel Hilbert space (RKHS)`, `data fusion (RCT and real-world data)`, `omnibus bias function`, `conditional restricted mean survival time`, `empirical process theory`
- **为什么对您有用**: 本文处理因果推断中RCT与观察性数据融合及未测量混杂偏差校正问题，使用RKHS与惩罚筛法推导理论性质，直接契合您在因果推断（混杂/数据融合）和半/非参数理论方面的核心兴趣，且提供了流行病学真实数据集的分析范式。

### 8. [10.1093/biomtc/ujaf128](https://doi.org/10.1093/biomtc/ujaf128) — Inverse-intensity weighted generalized estimating equations for longitudinal data subject to irregular observation: which variables should be included in the visit rate model?
- **作者**: Eleanor M Pullenayegum, Di Shan
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在纵向数据受不规则且信息性访问时间影响的设定下，目标是研究逆强度加权广义估计方程（IIW-GEE）中访问率模型应纳入哪些协变量，关键识别假设为结果与访问时间在访问模型协变量下条件独立。本文通过渐近方差分析证明：加入与结果和访问过程均无关的变量不改变回归系数估计方差；加入与结果相关但与访问无关的变量降低方差；加入与访问相关但与结果无关的变量则可能增减方差，取决于协变量-结果相关结构。方法核心是IPW类加权GEE的方差分解，无需新的正则性条件即可刻画不同协变量类型对估计效率的异质性影响。重度抑郁症数据应用显示，仅加入访问预测变量可使方差增大至2倍。对您有用：该工作直接关联纵向因果推断中IPW估计量的效率理论，为加权模型协变量选择以优化效率提供了明确的理论指导，与您关注的longitudinal causal inference和efficiency theory交叉。
- **关键技术**: `inverse-intensity weighted GEE`, `informative visit process`, `asymptotic variance decomposition`, `conditional independence assumption`, `longitudinal marginal models`, `IPW efficiency analysis`
- **为什么对您有用**: 直接连接纵向因果推断与效率理论：在IPW类加权估计中，访问模型协变量选择对效率的影响此前缺乏理论刻画，本文给出了明确的方差变化规则，对您关注的longitudinal causal inference中如何优化加权估计量效率有直接参考价值。

### 9. [10.1093/biomtc/ujaf140](https://doi.org/10.1093/biomtc/ujaf140) — Variable importance measures for heterogeneous treatment effects
- **作者**: Oliver J Hines, Karla Diaz-Ordaz, Stijn Vansteelandt
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在异质性处理效应（CATE）框架下，目标是量化协变量对个体处理效应预测的重要性，定义了基于均方误差（MSE）增加量的非参数处理效应变量重要性测度（TE-VIM）。作者推导了 TE-VIM 的半参数有效估计量，该估计量基于有效影响函数构建，支持与任意 CATE 估计策略结合，并兼容机器学习的非参数拟合。通过样本拆分与交叉拟合，估计量达到 n^{-1/2}-CAN 且达到半参数有效界。文中提出了 leave-one-out 和 keep-one-in 两种 VIM 计算策略，以适配不同的 CATE 元学习器（如 DR-learner）。理论上给出了估计量的渐近正态性与效率性质，模拟与临床试验数据验证了其有限样本表现。对您有用：该工作将半参数效率理论应用于 CATE 的 VIM 推断，其影响函数推导与 debiased ML 策略可直接迁移至您在因果推断与效率理论交叉方向的研究。
- **关键技术**: `efficient influence function`, `CATE meta-learners`, `semiparametric efficiency bound`, `variable importance measures`, `cross-fitting`
- **为什么对您有用**: 直接涉及因果推断（CATE异质性）与效率理论（半参数有效估计量），其有效影响函数推导与 ML 兼容的推断框架对您研究 debiased ML 和因果推断的交叉点具有直接参考价值；同时临床试验应用契合流行病学方向。

### 10. [10.1093/biomtc/ujaf151](https://doi.org/10.1093/biomtc/ujaf151) — Flexible and efficient estimation of causal effects with error-prone exposures: a control variates approach for measurement error
- **作者**: Keith Barnatchez, Rachel Nethery, Bryan E Shepherd, Giovanni Parmigiani, Kevin P Josey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在暴露变量存在测量误差的因果推断设定下，目标是在两阶段抽样设计（仅小子集拥有金标准暴露测量）下灵活且高效地估计因果效应。本文将控制变量法（control variates）引入因果推断，利用验证数据构建初始一致估计量，并通过全样本信息构造方差缩减项进行增强。该方法继承了双重稳健性，且在标准因果假设下实现了半参数效率界的逼近。相比现有依赖强参数假设或仅针对特定统计量的数据自适应方法，该框架在假设更弱的同时保持了灵活性。模拟显示其在多种两阶段抽样下优于现有方法；实证分析基于HIV电子病历数据。对您有用：该文将控制变量法与半参数效率理论结合处理测量误差，直接推进了您关注的因果推断估计与效率理论，且其EHR应用对流行病学因果推断有迁移价值。
- **关键技术**: `control variates method`, `double-robustness`, `two-phase sampling`, `exposure measurement error`, `variance reduction`, `semiparametric efficiency`
- **为什么对您有用**: 直接连接因果推断（测量误差下的估计）与效率理论（控制变量法实现方差缩减与双重稳健），并在流行病学EHR数据上应用，对您关注的半参数效率界与因果推断结合方向有重要参考价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1093/biomtc/ujaf153](https://doi.org/10.1093/biomtc/ujaf153) — Entrywise splitting cross-validation in generalized factor models: from sample splitting to entrywise splitting
- **作者**: Zhijing Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维广义因子模型（涵盖二值、计数与连续数据）下，本文研究因子数量 r 的确定问题，设定为 n, p → ∞ 的高维渐近框架。提出基于逐元素拆分的交叉验证（ES-CV）方法替代传统样本拆分，以避免因子数低估。进一步引入融合信息论准则的惩罚项，构建 penalized ES-CV 准则。在温和正则条件下证明了该准则选择因子数的一致性，并将方法扩展至不同缺失概率的随机缺失数据场景。模拟与小鼠大脑单细胞 RNA 测序数据验证了方法的有效性。对您有用：该文将高维因子模型的 CV 从样本拆分推进到逐元素拆分，其一致性证明与算法设计对您的高维统计与统计计算兴趣有直接参考价值。
- **关键技术**: `generalized factor model`, `entrywise splitting cross-validation`, `penalized information criterion`, `high-dimensional consistency`, `missing data imputation`
- **为什么对您有用**: 直击您的高维统计兴趣：在高维因子模型中提出 entrywise splitting 替代 sample splitting，提供了新的 CV 算法思路与高维一致性理论，对研究高维推断与计算方法有直接启发。

### 2. [10.1093/biomtc/ujaf130](https://doi.org/10.1093/biomtc/ujaf130) — SPLasso for high-dimensional additive hazards regression with covariate measurement error
- **作者**: Jiarui Zhang, Hongsheng Liu, Xin Chen, Jinfeng Xu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维带协变量测量误差的生存数据设定下，本文研究 additive hazards 模型的参数估计与变量选择，假设误差结构已知或可估计以构造修正矩条件。针对测量误差导致的非凸优化挑战，作者利用最近正半定（PSD）矩阵投影技术，将修正后的经验协方差矩阵投影至 PSD 锥，从而提出 SPLasso 及其软阈值变体 SPLasso-T，将非凸问题转化为可快速求解的凸优化。理论上，在较温和的稀疏与相容性条件下，证明了方法的模型选择一致性、oracle inequality 以及极限分布。模拟与真实数据（特别是含缺失值场景）表明该方法在高维噪声环境下具有优越的效率与鲁棒性。对您有用：PSD 矩阵投影技巧是处理高维误差协方差矩阵的有效计算手段，且高维 additive hazards 的 oracle inequality 与极限分布推导对您的高维统计与统计计算兴趣有直接参考价值。
- **关键技术**: `additive hazards model`, `covariate measurement error`, `nearest positive semi-definite matrix projection`, `oracle inequality`, `model selection consistency`, `high-dimensional survival analysis`
- **为什么对您有用**: PSD 矩阵投影技巧直接关联您的统计计算与矩阵理论兴趣；高维带测量误差的 oracle inequality 与极限分布结果对您的高维统计与半参数理论兴趣有参考价值；真实数据集对流行病学应用有借鉴。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1093/biomtc/ujaf126](https://doi.org/10.1093/biomtc/ujaf126) — Deep partially linear transformation model for right-censored survival data
- **作者**: Junkai Yin, Yue Zhang, Zhangsheng Yu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 本文在右删失生存数据下提出深度部分线性转换模型，目标是在放宽 Cox 比例风险假设的半参数转换模型框架下估计参数与非参数成分。方法采用最大似然估计（MLE），利用深度神经网络（DNN）逼近非参数函数以规避维数灾难并保留部分协变量的可解释性。理论上推导了 MLE 的整体收敛速率，并证明了非参数 DNN 估计量达到极小极大下界（minimax lower bound）。同时，建立了参数估计量的渐近正态性与半参数有效性（semiparametric efficiency）。模拟与实际数据验证了该估计程序在估计精度与预测上的表现。对您有用：该文对部分线性模型中 DNN 估计的极小极大收敛率及参数部分的半参数有效界推导，直接契合您在 semiparametric efficiency bounds 与 nonparametric theory 方向的核心兴趣。
- **关键技术**: `deep neural network`, `semiparametric transformation model`, `maximum likelihood estimation`, `minimax lower bound`, `semiparametric efficiency`, `partially linear model`
- **为什么对您有用**: 论文严格推导了部分线性模型中参数分量的半参数有效界与非参数 DNN 估计的极小极大下界，直接契合您在 semiparametric efficiency bounds 与 nonparametric theory 方向的核心兴趣，提供了 DNN 在生存分析中理论收敛率的参考。

### 2. [10.1093/biomtc/ujaf146](https://doi.org/10.1093/biomtc/ujaf146) — Generalized nonparametric temporal modeling of recurrent events with application to a malaria vaccine trial
- **作者**: Fei Heng, Yanqing Sun, Jing Xu, Peter B Gilbert
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文在复发事件（recurrent events）框架下，提出广义非参数时间强度模型，允许通过 link function 灵活涵盖乘性与加性时间强度模型，关键正则假设为强度过程的局部光滑性及双时间尺度的可分离结构。估计方面，基于双核（double kernel）局部线性光滑的最大似然估计程序被提出，并发展了自适应算法处理协变量重叠问题；带宽选择采用基于对数似然的交叉验证准则。渐近性质方面，证明了估计量的逐点相合性与渐近正态性。模拟显示有限样本表现良好，应用于 MAL-094/MAL-095 疟疾疫苗效力试验数据，揭示了疫苗保护效力如何随既往感染史动态变化。对您而言，双核局部线性光滑与多时间尺度强度模型的渐近理论可直接迁移至纵向因果推断中时变处理效应的非参数估计问题，同时疟疾疫苗试验数据集对流行病学应用有参考价值。
- **关键技术**: `local linear smoothing with double kernels`, `generalized temporal intensity model`, `maximum likelihood for counting processes`, `cross-validation bandwidth selection`, `recurrent event intensity process`, `adaptive algorithm for overlapping covariates`
- **为什么对您有用**: 核心方法（双核局部线性光滑、多时间尺度非参数强度模型的渐近理论）直接关联您 primary interest 中的非参数/半参数理论与纵向因果推断；疟疾疫苗试验的复发事件数据集对您 secondary interest 中的流行病学应用有数据集价值。

### 3. [10.1093/biomtc/ujaf152](https://doi.org/10.1093/biomtc/ujaf152) — Flexible Bayesian quantile regression for counts via generative modeling
- **作者**: Yuta Yamauchi, Genya Kobayashi, Shonosuke Sugasawa
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文针对计数数据的条件分位数回归问题，提出一种基于生成模型的贝叶斯非参数框架；核心 estimand 是与潜在连续变量相关的条件分位数上的回归参数，假设计数响应可由某连续潜变量经取整/截断生成。方法上，对计数响应与协变量的联合分布采用 Bayesian nonparametric kernel mixture 建模，再通过最小化关于潜变量条件分位数分布的期望损失，将后验推断转化为简单优化问题，避免了直接对离散分位数求逆的困难。数值实验显示相比现有 crude approaches（如 jittering 或直接分位数定义），偏差与估计精度均有改善；在急性心肌梗死住院时长数据上展示了更可解释的灵活结果。对您而言，该文的 BNPM kernel mixture 建模思路和潜变量生成机制可启发 semiparametric 框架下离散结局的因果/分位数推断，但整体偏贝叶斯路线，与您关注的 frequentist efficiency theory 距离较远。
- **关键技术**: `Bayesian nonparametric kernel mixture`, `latent continuous variable generative model`, `quantile regression for counts`, `expected loss minimization for posterior`, `Bayesian posterior via optimization`
- **为什么对您有用**: 与您 semiparametric/nonparametric theory 兴趣有方法重叠（BNP kernel mixture），且流行病学应用（住院时长）属 secondary interest；但贝叶斯路线与您关注的 frequentist efficiency bound / influence function 体系不直接对接，收益主要在建模思路借鉴而非理论工具迁移。

### 4. [10.1093/biomtc/ujaf149](https://doi.org/10.1093/biomtc/ujaf149) — A semiparametric Gaussian Mixture Model with spatial dependence and its application to whole-slide image clustering analysis
- **作者**: Baichen Yu, Jin Liu, Hansheng Wang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在无监督聚类设定下提出半参数高斯混合模型（SGMM），假设特征向量在给定空间位置下服从标准GMM，而混合概率与空间位置非参数相关。该模型允许同类样本空间聚集，非参数混合概率设定相比经典GMM更灵活。估计方面，作者设计了新型EM算法以处理非参数混合概率带来的计算挑战。理论上，建立了参数估计量的严格渐近性质（如相合性与渐近正态性）。实证分析在CAMELYON16全切片图像数据集上验证了聚类效果。对您而言，该文在混合模型中引入非参数成分并推导渐近理论的框架，可为半参数理论及复杂EM算法设计提供参考。
- **关键技术**: `semiparametric Gaussian mixture model`, `nonparametric mixing probability`, `EM algorithm`, `spatial dependence`, `asymptotic properties`
- **为什么对您有用**: 涉及半参数模型设定与非参数混合概率的渐近理论推导，契合您对半参数理论的兴趣；同时其针对复杂依赖结构的EM算法设计对统计计算方向有参考价值。

### 5. [10.1093/biomtc/ujaf158](https://doi.org/10.1093/biomtc/ujaf158) — Joint Bayesian additive regression trees for multiple nonlinear dependency networks
- **作者**: Licai Huang, Christine B Peterson, Min Jin Ha
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在异质性亚组（如结直肠癌分子亚型）下推断依赖网络，目标是同时识别跨组共享与亚组特异的边，假设变量间存在非线性依赖关系。方法采用 BART 刻画各亚组的非线性条件期望，并在特征被选为分裂规则的概率上放置 Markov 随机场（MRF）先验，以实现跨亚组的信息借用与共同变量选择的收缩。BART 的非参数灵活性使其比线性假设模型更适合基因组数据，MRF 先验则通过连接亚组间的选择概率来增强共享边的检测功效。模拟与结直肠癌蛋白质-蛋白质交互网络数据展示了方法在边恢复与亚组差异识别上的表现。对您而言，该文展示了 BART 在多组非参数回归中的层次化扩展思路，MRF 先验跨组收缩机制可迁移至因果推断中多处理/多人群设定的变量选择问题，但理论性质（收敛率、后验收缩率）未深入讨论。
- **关键技术**: `Bayesian Additive Regression Trees`, `Markov random field prior`, `hierarchical Bayesian model`, `dependency network estimation`, `multi-group shrinkage`
- **为什么对您有用**: BART 作为非参数工具与您 semiparametric/nonparametric theory 兴趣相关，MRF 跨组收缩机制可启发因果推断中多人群/多处理设定下的变量选择策略，但本文偏应用 Bayesian 方法，理论深度有限。

### 6. [10.1093/biomtc/ujaf157](https://doi.org/10.1093/biomtc/ujaf157) — A semiparametric method for addressing underdiagnosis using electronic health record data
- **作者**: Weidong Ma, Jordana B Cohen, Jinbo Chen
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在电子健康记录（EHR）的 positive-unlabeled (PU) 设定下，目标是估计患者患有特定漏诊疾病的概率，核心挑战在于缺乏明确的健康对照样本。作者提出对一小部分未标记样本进行确诊验证，将其转化为 two-phase sampling 问题，并构建半参数估计量。方法通过结合验证样本的逆概率加权（IPW）与半参数效率理论，推导出渐近有效的 influence function 以纠正选择偏倚。理论证明了估计量的 n^{-1/2}-CAN 性质与渐近正态性，模拟与 Penn Medicine 的 NASH 漏诊数据应用验证了其实用性。对您有用：该文将 PU 学习与 two-phase sampling 结合的半参数效率框架，可直接迁移至您关注的缺失数据/选择偏倚下的半参数效率界推导，同时提供了流行病学 EHR 数据的应用范式。
- **关键技术**: `positive-unlabeled learning`, `semiparametric efficiency`, `two-phase sampling`, `influence function`, `inverse probability weighting`
- **为什么对您有用**: 该文在流行病学 EHR 数据（secondary interest）上发展了处理 PU 结构的半参数方法（primary interest: semiparametric theory），其基于 two-phase sampling 的效率理论推导对您研究缺失数据/选择偏倚下的 influence function 与效率界具有直接参考价值。

## 效率理论 / Debiased ML  *(efficiency_dml, 3 篇)*

### 1. [10.1093/biomtc/ujaf150](https://doi.org/10.1093/biomtc/ujaf150) — Federated double machine learning for high-dimensional semiparametric models
- **作者**: Kai Kang, Zhihao Wu, Xinjie Qian, Xinyuan Song, Hongtu Zhu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 10/10 · novelty: `new_method`
- **摘要**: 在多中心联邦学习设定下，针对包含高维干扰参数的半参数模型，目标是构建全局参数的有效估计量。方法基于 double machine learning (DML) 框架，在 Neyman 正交条件下扩展了 surrogate efficient score，并引入 density ratio tilting 技术将本地个体数据与其他中心的汇总统计量结合。该机制有效缓解了高维干扰参数估计中的正则化偏差与过拟合问题。理论上在极小假设下建立了估计量的渐近正态分布，保证了联邦环境下的半参数效率。对您有用：直接推进了您关注的 debiased ML 与半参数效率理论在分布式计算场景的边界，且 density ratio tilting 技巧可迁移至其他因果推断/两阶段采样设定。
- **关键技术**: `double machine learning`, `Neyman orthogonality`, `surrogate efficient score`, `density ratio tilting`, `semiparametric efficiency`, `federated learning`
- **为什么对您有用**: 直接推进了您关注的 debiased ML 与半参数效率理论在分布式计算场景的边界，且 density ratio tilting 技巧可迁移至其他因果推断/两阶段采样设定。

### 2. [10.1093/biomtc/ujaf164](https://doi.org/10.1093/biomtc/ujaf164) — Prediction of transition probabilities in multi-state models with nested case-control data
- **作者**: Yen Chang, Anastasia Ivanova, Demetrius Albanes, Jason P Fine, Yei Eun Shin
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在嵌套病例对照（NCC）抽样下，研究多状态模型中转移概率的预测问题；NCC 的条件似然限制了数据复用，故采用 IPW 伪似然进行推断，但标准 IPW 估计转移概率时效率较低。本文提出两种提升效率的方法：一是利用队列层面信息校准设计权重（calibration），二是对同一起始状态的多条转移联合建模。两种方法均导出了显式方差估计，模拟显示单独使用即有显著效率提升，联合使用增益更大。实证分析基于 PLCO 癌症筛查试验数据。对您而言，IPW 权重校准提升效率的思路与 semiparametric efficiency theory 中 augmented/orthogonal 改进 IPW 的逻辑相通，且 NCC 设计在流行病学队列中常见，方法可直接迁移。
- **关键技术**: `inverse probability weighting`, `nested case-control sampling`, `weight calibration`, `pseudolikelihood`, `multi-state transition probabilities`, `joint transition modeling`
- **为什么对您有用**: IPW 权重校准提升效率的机制与您关注的 semiparametric efficiency / debiased ML 中 orthogonal score 改进 IPW 的思路同源；NCC 设计与 PLCO 数据集对您 secondary interest 流行病学应用有直接价值。

### 3. [10.1093/biomtc/ujaf165](https://doi.org/10.1093/biomtc/ujaf165) — Statistical inference on high-dimensional covariate-dependent Gaussian graphical regressions
- **作者**: Xuran Meng, Jingfei Zhang, Yi Li
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维协变量依赖的高斯图回归模型中，目标是推断精度矩阵随高维个体协变量变化的条件依赖结构，传统 GGM 忽略了此类异质性。作者采用多任务学习进行初始估计，并据此构造 debiased estimator 以实现逐元素统计推断。核心技术创新是引入一种新的投影技巧估计逆协方差矩阵，将优化成本降至与样本量 n 同阶，避免了高维矩阵求逆的巨大开销。理论上证明了去偏估计量具备快速收敛性与渐近正态性，从而支持有效的置信区间构建与假设检验。对您有用：该文的高维去偏推断框架与投影降计算技巧直接契合您在 efficiency theory (debiased ML) 与 high-dimensional statistics 上的兴趣，投影法降低逆矩阵计算复杂度的思路可迁移至其他高维推断场景。
- **关键技术**: `debiased estimator`, `multi-task learning`, `Gaussian graphical regression`, `projection technique for inverse covariance`, `asymptotic normality`, `high-dimensional inference`
- **为什么对您有用**: 直接契合您在 efficiency theory (debiased ML) 与 high-dimensional statistics 的核心兴趣；其用于估计逆协方差矩阵的投影技巧将计算复杂度降至 O(n)，对高维图模型推断的计算方法有直接借鉴价值。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biomtc/ujaf133](https://doi.org/10.1093/biomtc/ujaf133) — Double robust conditional independence test for novel biomarkers given established risk factors with survival data
- **作者**: Baoying Yang, Jing Qin, Jing Ning, Yukun Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据设定下，本文研究条件独立性检验 T⊥X∣Z，其中 T 为生存时间，Z 为已知风险因子，X 为潜在新生物标志物，目标是检验 X 在条件模型中的系数是否为零。传统基于似然比与卡方分布的检验在模型误设下第一类错误率失控。本文提出基于重抽样的方法来近似似然比统计量的零分布，核心优势在于双重稳健性：只要结局模型 T∣(X,Z) 或工作模型 P(X∣Z) 之一正确指定，即可保证正确的第一类错误率。此外，该方法允许融入机器学习技术估计 nuisance functions 以提升表现。模拟与 ADNI 阿尔茨海默病数据应用验证了有限样本性质。对您有用：该文将双重稳健思想与条件独立性检验结合，直接推进您在假设检验方向的兴趣，其处理删失数据与 nuisance function 估计的策略也可迁移至因果发现与流行病学应用中的条件独立性检验。
- **关键技术**: `conditional independence test`, `double robustness`, `likelihood ratio statistic`, `resampling-based inference`, `survival analysis with right censoring`, `nuisance function estimation`
- **为什么对您有用**: 直接推进您在假设检验方向的兴趣，将双重稳健性引入条件独立性检验，且其处理右删失数据与 nuisance function 估计的策略可迁移至因果发现与流行病学应用中的条件独立性检验。

### 2. [10.1093/biomtc/ujaf170](https://doi.org/10.1093/biomtc/ujaf170) — Maximized sequential probability ratio test regression
- **作者**: Ivair R Silva, Joselito Montalban, Fernando L P de Oliveira
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在 MaxSPRT 及其条件版本 CMaxSPRT 的序贯检验框架下，引入回归结构以调整可观测混杂变量（如年龄、性别），目标是在二项和 Poisson 数据的序贯监测中对 adverse event 信号进行带协变量调整的假设检验。核心方法是将广义线性模型的回归参数嵌入序贯似然比统计量，使得在历史对照与监测期 Poisson 数据比较中可同时处理基线率异质性、季节性及可观测混杂；检验统计量的临界值通过数值计算（R Sequential 包）获得。理论贡献主要是将原有齐性样本假设下的 MaxSPRT 推广到回归设定，但未给出渐近效率界或 influence function 层面的深入分析。实证部分以加拿大 Manitoba 疫苗安全监测为例展示了应用。对您而言，该文在序贯假设检验（primary: hypothesis testing）与流行病学监测（secondary: epidemiology）的交叉处提供了一个可迁移的分析模式，但理论深度有限。
- **关键技术**: `sequential probability ratio test`, `MaxSPRT`, `CMaxSPRT`, `regression-adjusted sequential test`, `Poisson/binomial GLM in surveillance`, `vaccine safety sequential monitoring`
- **为什么对您有用**: 连接 primary interest 中的 hypothesis testing（序贯检验的回归扩展）与 secondary interest 中的 epidemiology（疫苗安全监测数据及分析流程），但理论新颖性偏 incremental，主要价值在于应用模式和数据集可迁移性。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomtc/ujaf141](https://doi.org/10.1093/biomtc/ujaf141) — A Bayesian collocation integral method for system identification of ordinary differential equations
- **作者**: Mingwei Xu, Samuel W K Wong, Peijun Sang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在高维稀疏常微分方程（ODE）系统辨识设定下，本文针对含噪时间序列数据，提出一种贝叶斯层次配点积分方法以量化参数估计的不确定性。方法基于加性ODE模型假设，将似然函数、积分形式的ODE约束与组稀疏惩罚统一在贝叶斯框架下，实现系统结构与轨迹的联合估计。配点积分法将ODE转化为代数约束，避免了传统ODE求解器的反复调用，显著提升了计算效率；同时引入组稀疏先验处理高维结构，后验推断采用MCMC。模拟与基因调控网络真实数据表明，该方法在轨迹恢复与成分估计上优于现有频率学派方法，并提供可靠的不确定性量化。对您有用：该文提出的配点积分法属于统计计算中的数值方法创新，若您关注ODE参数推断的计算效率与不确定性量化，此算法框架可提供直接借鉴。
- **关键技术**: `Bayesian hierarchical model`, `collocation integral method`, `group-wise sparse penalty`, `ODE system identification`, `uncertainty quantification`
- **为什么对您有用**: 直接对应您 primary interest 中的 statistical computing (numerical methods)，提供了一种避免反复调用 ODE solver 的配点积分算法，对处理高维稀疏 ODE 的计算与不确定性量化有方法迁移价值。

## 流行病学  *(epidemiology, 6 篇)*

### 1. [10.1093/biomtc/ujaf144](https://doi.org/10.1093/biomtc/ujaf144) — Bayesian scalar-on-image regression with spatial interactions for modeling Alzheimer’s disease
- **作者**: Nilanjana Chakraborty, Qi Long, Suprateek Kundu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在 scalar-on-image 回归框架下，目标是建模阿尔茨海默病(AD)认知损伤与脑影像生物标记物的关联，关键假设是影像特征与补充风险因子（人口学、临床、遗传）之间存在空间交互效应，忽略该异质性将导致预测偏差与估计偏倚。方法通过功能回归系数依赖于补充风险因子的层次表示来刻画空间交互，嵌入多分辨率小波分解的 scalar-on-function 框架。为应对高维诅咒，采用 spike-and-slab 混合先验实现同时稀疏与聚类，其中 slab 分量由潜类分布刻画。开发了高效的 MCMC 算法进行后验计算。模拟与 ADNI 纵向研究应用显示，该模型在多次访问的认知损伤预测上显著优于替代方法，并识别出与认知能力直接或通过交互显著关联的关键脑区。对您而言，ADNI 纵向数据集及其分析流程在流行病学因果推断方向具有数据集价值，小波分解+spike-and-slab 的 MCMC 计算策略也可为高维贝叶斯功能回归的统计计算提供参考。
- **关键技术**: `scalar-on-image regression`, `multi-resolution wavelet decomposition`, `spike-and-slab mixture prior`, `spatially varying interactions`, `latent class slab component`, `MCMC posterior computation`
- **为什么对您有用**: ADNI 纵向数据集对流行病学因果推断应用有直接数据集价值；小波+spike-and-slab 的 MCMC 计算策略对统计计算方向的高维贝叶斯推断有方法参考意义，但本文不涉及经典半参数效率理论或因果 identification，方法论新颖性限于贝叶斯功能回归的扩展。

### 2. [10.1093/biomtc/ujaf155](https://doi.org/10.1093/biomtc/ujaf155) — Super learner for survival prediction in case-cohort and generalized case-cohort studies
- **作者**: Haolin Li, Haibo Zhou, David Couper, Jianwen Cai
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在病例队列及广义病例队列设计下，针对罕见疾病生存预测问题，目标是构建适应偏倚抽样机制的预测算法。本文提出基于 Super Learner 的集成学习算法，通过加权损失函数校正子队列抽样的选择偏倚。理论上证明了该算法具有渐近模型选择一致性与均匀一致性。模拟表明同等样本量下其预测精度优于简单随机抽样设计，实证分析基于 ARIC 动脉粥硬化风险社区研究数据。对您有用：为流行病学罕见结局的生存预测提供了半参数集成方法，且 ARIC 数据集对您做流行病学应用因果推断有参考价值。
- **关键技术**: `super learner`, `case-cohort design`, `asymptotic model selection consistency`, `uniform consistency`, `weighted loss function`, `survival prediction`
- **为什么对您有用**: 直接对应您在流行病学（epidemiology）的应用兴趣，提供了罕见疾病队列设计的半参数集成预测方法；ARIC 数据集及分析流程对您做流行病学因果推断应用有数据集价值。

### 3. [10.1093/biomtc/ujaf159](https://doi.org/10.1093/biomtc/ujaf159) — Stable survival extrapolation using mortality projections
- **作者**: Anastasios Apsemidis, Nikolaos Demiris
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在健康经济评估与生存分析设定下，目标是估计完全生存曲线下的面积（平均生存时间），需对右删失观测数据进行外推。方法结合贝叶斯死亡率模型，将人口统计数据的长期预测作为基线锚点；提出基于灵活参数化多危险（poly-hazard）模型的外推框架，可自然容纳非比例风险与交叉生存曲线，并在竞争风险框架下利用原因别危险函数减少外推不稳定性。实证分析了三阴性乳腺癌、黑色素瘤免疫疗法及心律失常数据，展示了方法在长程外推中的鲁棒性。对您可能有用：该文提供了流行病学/健康经济中生存外推的贝叶斯参数化策略，若您关注竞争风险下的因果推断或生存估计，其锚定人口数据的思想可作参考。
- **关键技术**: `poly-hazard models`, `Bayesian mortality projection`, `competing risks`, `cause-specific hazard`, `survival extrapolation`
- **为什么对您有用**: 涉及流行病学和健康经济的真实数据应用，若您关注生存分析中的竞争风险或因果推断应用，其利用人口数据锚定基线风险的外推策略具有参考价值。

### 4. [10.1093/biomtc/ujaf163](https://doi.org/10.1093/biomtc/ujaf163) — Structuring, sequencing, staging, selecting: the 4S method for the longitudinal analysis of multidimensional questionnaires in chronic diseases
- **作者**: Tiphaine Saulnier, Wassilios G Meissner, Margherita Fabbri, Alexandra Foubert-Samier, Cécile Proust-Lima
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对慢性病纵向多维问卷数据，提出 4S 方法（structuring, sequencing, staging, selecting），目标是在有序重复测量且可能被事件截断的设定下，恢复疾病维度的动态演进。方法依次：(1) 通过单维性、条件独立性、单调性三个校准假设识别问卷维度结构；(2) 对每个维度拟合 joint latent process model，其中纵向子模型采用连续时间 IRT（item response theory）模型刻画有序 item 与潜在过程的关系，同时处理事件截断；(3) 通过投影将各维度轨迹与疾病阶段对齐；(4) 利用 Fisher 信息量筛选各阶段最具信息量的 item。应用于多系统萎缩症（MSA）的日常活动与运动障碍数据，展示了维度轨迹随疾病进展的分化及关键 item 的筛选。对您而言，该文在流行病学纵向数据建模中处理截断与潜在过程的思路，可迁移至 longitudinal causal inference 中 time-to-event 与重复测量的联合建模场景。
- **关键技术**: `continuous-time item response theory`, `joint latent process model`, `Fisher information for item selection`, `multidimensional questionnaire calibration`, `projection approach for disease staging`, `truncation by events handling`
- **为什么对您有用**: 连接您 secondary interest 中的流行病学应用与 longitudinal causal inference：joint latent process model 处理事件截断的框架可迁移至纵向因果推断中 time-to-event confounding / truncation 的建模，且 MSA 数据集本身可作为稀有神经退行性疾病纵向分析的实例参考。

### 5. [10.1093/biomtc/ujaf138](https://doi.org/10.1093/biomtc/ujaf138) — A regularized continuous-time hidden Markov model for identifying latent state transition patterns of poly-tobacco use
- **作者**: Xinyu Yan, Ji-Hyun Lee, Xiang-Yang Lou
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在纵向队列设定下，本文目标是识别多烟草使用模式的潜在状态转移，解决高维风险因素与观测时间间隔不一致的挑战。提出连续时间隐马尔可夫模型（CT-HMM），在转移参数上引入 elastic-net 正则化以选择信息协变量并提高估计精度，同时利用关键协变量辅助确定隐状态数。方法整合了复杂抽样设计的调查权重、分层和聚类信息。模拟验证了状态数确定、变量选择和参数估计的有效性，PATH 数据应用揭示了青年烟草状态转移的风险因素。对您可能有用：提供了流行病学纵向队列（PATH 数据）的潜变量转移建模范例，正则化 CT-HMM 的计算框架可迁移至其他带有不规则观测时间的纵向数据分析。
- **关键技术**: `continuous-time hidden Markov model`, `elastic-net regularization`, `survey weight integration`, `latent state determination`, `variable selection for transition parameters`
- **为什么对您有用**: 属于流行病学纵向队列应用，PATH 数据集和正则化 CT-HMM 计算框架对处理不规则观测时间的潜变量模型有参考价值，但方法学理论深度（如半参数效率/因果推断）有限。

### 6. [10.1093/biomtc/ujaf145](https://doi.org/10.1093/biomtc/ujaf145) — Bayesian monotone single-index quantile regression model with bounded response and misaligned functional covariates
- **作者**: Shengxian Ding, Debajyoti Sinha, Greg Hajcak, Roman Kotov, Chao Huang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在响应变量有界（如抑郁评分）且包含标量与错位函数协变量（如神经反应信号）的设定下，目标是估计条件分位数并确保预测不越界。本文提出贝叶斯单指标分位数回归框架，通过单调链接函数灵活捕捉未知非线性关系，同时保证估计分位数在响应界限内。该方法在分位数回归中联合整合了函数协变量的配准，克服了传统线性回归的局限，并提供了类似线性模型的临床可解释指标。模拟表明其在处理标量与预配准函数协变量时优于无约束单指标方法。在青少年抑郁大规模数据中验证了实用性。对您有用：该文展示了半参数单指标模型在流行病学有界数据中的应用，其联合配准与回归的思路对处理纵向因果推断中的函数型暴露/混杂有参考价值。
- **关键技术**: `Bayesian quantile regression`, `single-index model`, `monotone link function`, `functional covariate registration`, `bounded response`
- **为什么对您有用**: 属于流行病学应用，使用半参数单指标模型处理有界响应与函数协变量；其联合配准与回归的建模思路对处理纵向因果推断中的函数型暴露/混杂具有参考价值。

## 其他  *(other, 4 篇)*

### 1. [10.1093/biomtc/ujaf154](https://doi.org/10.1093/biomtc/ujaf154) — Analysis of cross-platform health communication with a network approach
- **作者**: Xinyan Fan, Mengque Liu, Shuangge Ma
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `application`
- **摘要**: 本文研究跨平台健康传播问题，基于 Breastcancer.org 和 Twitter 的文本数据，构建词共现网络与词频向量的联合模型。方法上，利用词共现网络刻画传播的结构内容，词频向量刻画传播量级，提出可容纳时间变异的跨平台传播模型，并讨论了其理论与数值性质。实证分析了 2010-2020 年超 139 万条推文和 51.7 万条帖子，发现 Twitter 主题显著影响在线健康社区的内容与量级，并识别出 2012-2013 和 2015-2018 两个活跃期。该研究属于文本挖掘与网络分析的应用，缺乏因果识别或半参数效率等核心统计方法创新，对您在因果推断或效率理论方面的研究直接参考价值有限。
- **关键技术**: `word co-occurrence network`, `cross-platform communication model`, `text mining`, `temporal variation analysis`
- **为什么对您有用**: 本文属于健康传播领域的文本挖掘应用，未涉及因果推断、半参数理论或高维统计等您的主要兴趣方向，方法论参考价值极低。

### 2. [10.1093/biomtc/ujaf160](https://doi.org/10.1093/biomtc/ujaf160) — Large row-constrained supersaturated designs for high-throughput screening
- **作者**: Byran J Smucker, Stephen E Wright, Isaac Williams, Richard C Page, Andor J Kiss, Surendra Bikram Silwal et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对高通量筛选（high-throughput screening）中大量化合物逐一测试效率低下的问题，提出一类行约束超饱和设计（row-constrained supersaturated designs），用于指导多化合物池（pool）的构造，整体方法命名为 CRowS。模型设定为主效应线性模型，关键约束为每池化合物数上限（row constraint）；设计质量通过主效应信息矩阵的非对角元平均平方值衡量，文中给出了该量的初始下界。计算方面，作者开发了高效的组合优化程序构造 CRowS 设计，并分析了行约束对设计质量的影响。模拟表明 CRowS 在统计性能上优于传统一化合物一孔方法及现有池化方法，并在 VIM-2 酶 assay 数据上做了实证演示。本文核心贡献在实验设计领域，与您的高维统计（RMT）或效率理论方向交集有限，但超饱和设计中信息矩阵性质的分析思路可作参考。
- **关键技术**: `supersaturated design`, `row-constrained pooling`, `information matrix lower bound`, `combinatorial optimization for design construction`, `E(s²) optimality criterion`
- **为什么对您有用**: 与您的高维统计（RMT）和效率理论方向交集较弱；超饱和设计本质是 p>>n 设定下的实验设计问题，信息矩阵非对角元下界的分析思路或可迁移，但工具和语言差异较大。

### 3. [10.1093/biomtc/ujaf142](https://doi.org/10.1093/biomtc/ujaf142) — Clarifying the role of the Mantel–Haenszel risk difference estimator in randomized clinical trials
- **作者**: Xiaoyu Qiu, Yuhan Qian, Jaehwan Yi, Jinqiu Wang, Yu Du, Yanyao Yi et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10
- **摘要**: {
  "topic": "causal_inference",
  "summary_zh": "本文研究随机化临床试验中 Mantel–Haenszel (MH) 风险差估计量的性质，目标 estimand 为超总体 ATE 及分层风险差的加权平均，关键假设从传统的"跨层风险差齐性"放松为对风险差异变异性施加合理限制。作者将 MH 估计量重新定位为协变量调整方法，证明在 large-stratum、sparse-stratum 及混合渐近体制下均能一致估计超总体 ATE。核心贡献是提出统一稳健方差估计量，改进了 Greenland–Robins 和 Sato 等人的经典方差估计，且在上述三种渐近体制下均有可证明的一致性，无需齐性假设。扩展结果还给出了 MH 检验、post-stratification 估计量及多处理设置的新见解。对您有用：该工作为 RCT 协变量调整提供了更弱的识别假设与更优的方差估计，直接关联您在因果推断中 ATE 估计与效率理论的兴趣，且 sparse-stratum 渐近分析对高维分层场景有方法论迁移价值。",
  "key_techniques": [
    "Mantel-Haenszel risk difference estimator",
    "covariate adjustment in RCTs",
    "large-strat

### 4. [10.1093/biomtc/ujaf124](https://doi.org/10.1093/biomtc/ujaf124) — Randomized optimal selection design for dose optimization
- **作者**: Shuqi Wang, Ying Yuan, Suyu Liu
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 4
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在 FDA Project Optimus 背景下，针对最优生物学剂量（OBD）的选择问题，提出随机最优选择设计（ROSE），目标是在预设正确选择概率下最小化样本量。核心机制是将两剂量组响应率之差与预设决策边界比较，属于 selection design 框架下的序贯检验；进一步扩展为两阶段设计，允许在期中分析时提前选择 OBD 以进一步减少样本量。模拟显示每剂量组 15–40 人时正确选择率约 60%–70%。该文属于临床试验剂量优化设计，方法学 novelty 有限（决策边界为预设常数，无效率理论或半参数框架），对您的主要理论兴趣（因果推断、效率界、高维推断）直接关联较弱，仅在序贯假设检验/决策边界构造上有边际参考价值。
- **关键技术**: `selection design`, `optimal biological dose`, `two-stage sequential testing`, `decision boundary`, `sample size minimization`
- **为什么对您有用**: 与您 primary interest 中的 hypothesis testing 有微弱关联（序贯决策边界构造），但整体为应用型临床试验设计，理论深度不足，对您核心方向（效率界、半参数、高维）无直接收益。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

