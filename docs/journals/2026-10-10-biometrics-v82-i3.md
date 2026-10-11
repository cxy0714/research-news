# Biometrics — Vol 82  Issue 3  ·  2026-10-10

- 共 44 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 5 篇（对照 OpenAlex 50 篇）：10.1093/biomtc/ujag106、10.1093/biomtc/ujag031、10.1093/biomtc/ujag032、10.1093/biomtc/ujag049、10.1093/biomtc/ujag064

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期共 44 篇论文，主线大致可归为四类：因果推断与处理效应估计（约 10 篇）、半参数与非参数方法（约 5 篇）、假设检验与高维推断（约 4 篇）、以及贝叶斯建模与临床试验设计（约 15 篇，后者多为应用导向）。因果推断是本期最集中的主题，且内部呈现明显的方法论分层：从经典协变量调整到未观测混杂、再到时空干扰下的识别，覆盖了不同数据生成机制下的识别与估计问题。半参数方向则聚焦于区间删失数据与效率界，假设检验部分关注高维聚类显著性与变量选择。

因果推断主线中，最值得注意的推进在于对未观测混杂与选择偏差同时存在的处理。`Doubly robust proximal causal inference under confounded outcome-dependent sampling` 将 proximal 方法从 test-negative design 推广到一般 ODS 设计，用一对代理变量同时校正混杂与选择偏差，给出可识别条件并构造双重稳健估计量。`A latent factor panel approach to spatiotemporal causal inference` 则从因子模型出发，在未测量混杂不平滑且存在单元间干扰时，利用有限干扰假设实现点识别，与前者形成互补——一个依赖代理变量，一个依赖因子结构。`Multiply robust inference of average treatment effects by high-dimensional empirical likelihood` 走的是另一条路，用高维经验似然结合多个工作模型构造 Neyman 正交得分，在倾向得分和结果回归均可能错误时保持覆盖。这三篇分别对应未观测混杂、时空干扰、模型误设三种场景，适合对照阅读。此外，`Bias reduction in g-computation` 和 `Density and treatment effect estimation under covariate-adaptive randomization` 分别处理小样本偏差和重尾结果，属于经典框架下的有限样本修正。

半参数与非参数方向，`Efficient estimation for deep generalized accelerated hazards models with interval-censored data` 将深度神经网络与单调样条结合，在区间删失下达到半参数效率界，是本期少数同时涉及深度学习和效率理论的工作。`Statistical analysis of disease onset during lifespan with left truncation` 则处理老龄队列中常见的左截断问题，用核加权乘积限估计量分解发病时间分布，方法上更接近传统生存分析。假设检验部分，`One-at-a-time knockoffs` 简化了经典 knockoff 的构造条件，每次只替换单个变量列，在温和相关性假设下渐近控制 FDR，计算成本显著降低；`A general framework for testing clustering significance` 则在高维聚类检验中同时改进零协方差估计并扩展至变量层面推断，与前者同属高维推断但目标不同。

若按主题优先阅读：因果推断方向建议先看 `Doubly robust proximal causal inference`、`A latent factor panel approach` 和 `Multiply robust inference` 三篇，覆盖未观测混杂、时空干扰和模型误设三种核心场景；半参数效率方向看 `Efficient estimation for deep generalized accelerated hazards models`；高维推断看 `One-at-a-time knockoffs`。其余贝叶斯与临床试验设计类论文多为应用扩展，方法论创新有限，可按需查阅。

## 因果推断  *(causal_inference, 13 篇)*

### 1. [10.1093/biomtc/ujag157](https://doi.org/10.1093/biomtc/ujag157) · [arXiv](https://arxiv.org/abs/2208.01237) — Doubly robust proximal causal inference under confounded outcome-dependent sampling
- **作者**: Kendrick Li, Xu Shi, Wang Miao, Eric Tchetgen Tchetgen
- **期刊/来源**: Biometrics
- **机构**: St. Jude Children's Research Hospital · University of Michigan · Peking University · University of Pennsylvania
- **分类**: vol 82 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在 outcome-dependent sampling（ODS）设计下研究因果推断，目标是在未观测混杂与选择偏差同时存在时识别并估计因果优势比（causal odds ratio）。作者将 proximal causal inference 方法从 test-negative design 推广到一般 ODS 设计，利用一对代理变量（proxies）同时校正由隐藏共同原因导致的未观测混杂和选择偏差。主要贡献包括：给出在混杂与选择偏差共存时因果优势比可识别的新条件；提出新的 proximal doubly robust 估计量，并刻画其双重稳健性质。通过大量模拟和密歇根大学健康系统的实际数据验证了估计量的有限样本性能。本文对您有用之处在于，它直接扩展了 proximal CI 在流行病学 ODS 设计中的应用，且其双重稳健估计框架与您的 semiparametric 理论兴趣高度相关。
- **关键技术**: `proximal causal inference`, `doubly robust estimation`, `outcome-dependent sampling`, `causal odds ratio`, `negative control variables`
- **为什么对您有用**: 本文属于 causal inference 子方向中的 proximal CI 与 ODS 设计结合，直接对应您的 primary interest。您可以用 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory 来审视其识别条件与估计量的效率性质，例如检查其双重稳健估计量是否达到半参数效率界。中期可做：若想深入推导其影响函数，需在 semiparametric theory 上进一步巩固。

### 2. [10.1093/biomtc/ujag149](https://doi.org/10.1093/biomtc/ujag149) · [arXiv](https://arxiv.org/abs/2509.00312) — Multiply robust inference of average treatment effects by high-dimensional empirical likelihood
- **作者**: Xintao Xia, Yumou Qiu
- **期刊/来源**: Biometrics
- **机构**: Zhejiang University · Peking University
- **分类**: vol 82 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对高维协变量下平均处理效应（ATE）的推断问题，提出了一种多重稳健（multiply robust）的推断方法。在倾向得分（PS）难以用单一参数模型正确指定时，作者提出一种高维经验似然加权方法，通过软协变量平衡约束结合多个工作PS模型。同时，利用扩展的校准函数集和正则化的增广结果回归（OR）来校正非精确协变量平衡带来的偏差，从而构造ATE的Neyman正交得分。理论结果表明，在任一PS模型、其线性组合或OR模型正确指定时，所提置信区间在高维协变量下具有渐近有效的名义覆盖。方法还扩展到结果变量服从广义线性模型以及数据存在未知聚类的情形，并基于估计的聚类拟合多个工作PS模型。模拟研究展示了该方法相对于现有高维协变量下双重稳健推断方法的优势，并分析了右心导管数据集以验证其有效性。
- **关键技术**: `high-dimensional empirical likelihood`, `multiply robust estimation`, `Neyman orthogonal score`, `soft covariate balancing`, `regularized outcome regression`
- **为什么对您有用**: 本文直接关联因果推断中的稳健推断与高维协变量处理，属于您的主要兴趣方向。其构造Neyman正交得分和多重稳健估计的思路，可结合您熟悉的高维统计和半参数理论进行深入分析。您可考虑用您擅长的minimax界或U-统计量工具来评估其估计量的效率损失或推广到其他因果参数。

### 3. [10.1093/biomtc/ujag153](https://doi.org/10.1093/biomtc/ujag153) · [arXiv](https://arxiv.org/abs/2509.10974) — A latent factor panel approach to spatiotemporal causal inference
- **作者**: Jiaxi Wu, Alexander Franks
- **期刊/来源**: Biometrics
- **机构**: University of California, Santa Barbara
- **分类**: vol 82 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一种针对时空观测数据的因果推断方法，目标是在存在未测量混杂且混杂在时空上不平滑时估计处理效应。方法基于因子混杂假设，即未测量混杂对处理和结果的影响可由共享的潜在因子模型刻画，该假设足以在存在单元间干扰时部分识别因果效应。进一步假设时空干扰程度有限（在多数应用中合理），则可实现点识别。估计采用面板数据文献中的因子模型技术，结合多元因果推断方法。模拟研究表明，相比空间平滑和面板数据基线，该方法能大幅减少遗漏变量偏误。案例研究估计了加州产前PM2.5暴露对出生体重的影响。对您而言，该方法将因子模型与因果推断结合，为时空数据中的未测量混杂问题提供了新视角，与您的proximal CI和纵向因果推断兴趣相关。
- **关键技术**: `factor confounding assumption`, `latent factor model`, `panel data methods`, `partial identification`, `spatiotemporal interference`
- **为什么对您有用**: (1) 直接关联您的causal inference兴趣中的未测量混杂与identification问题，特别是时空设定下的proximal CI思想有可比性；(2) 可用您very_familiar的estimation theory in causal inference来审视其因子模型的识别条件是否可放松或推广到proximal框架；(3) 中期可做：需在moderately_familiar的identification theory上加深对因子模型识别条件的理解，然后可尝试将方法扩展到更复杂的干扰结构。

### 4. [10.1093/biomtc/ujag129](https://doi.org/10.1093/biomtc/ujag129) · [arXiv](https://arxiv.org/abs/2509.07369) — Bias reduction in g-computation for covariate adjustment in randomized clinical trials
- **作者**: Xin Zhang, Lin Liu, Haitao Chu
- **期刊/来源**: Biometrics
- **机构**: Pfizer (United States) · Shanghai Jiao Tong University · University of Minnesota
- **分类**: vol 82 · issue 3
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究随机临床试验中协变量调整的 g-computation 方法，目标是在小样本或事件数较少时改进估计与推断。标准 g-computation 依赖典型广义线性模型，但小样本下可能出现方差低估和 MLE 不存在等问题。作者分析了 g-computation 估计量的渐近偏差，并提出一种基于广义 Oaxaca–Blinder 估计的偏差校正方法，保证估计量有界。该方法使用轻微修改的 MLE 或 Firth 校正估计作为 nuisance 参数，并引入小样本方差调整以改善有限样本推断。模拟显示该方法在偏差-效率权衡上优于现有方法，并在一个实际临床试验的亚组分析中提升了精度。
- **关键技术**: `g-computation`, `Oaxaca-Blinder decomposition`, `Firth correction`, `bias reduction`, `small-sample variance adjustment`
- **为什么对您有用**: 本文直接关联因果推断中的纵向/协变量调整方法，且其偏差校正思路可迁移到您的 proximal CI 或 mediation 分析中的 nuisance 估计。您可用 very_familiar 的估计理论（如 influence function 视角）审视其偏差校正的渐近性质，或考虑将 Oaxaca-Blinder 技巧推广到更复杂的因果 estimand。中期可做：需在 semiparametric theory 上进一步打磨以处理非参数 nuisance 模型。

### 5. [10.1093/biomtc/ujag159](https://doi.org/10.1093/biomtc/ujag159) — Density and treatment effect estimation under covariate-adaptive randomization with heavy-tailed outcomes
- **作者**: Hongzi Li, Wei Ma, Yingying Ma, Hanzhong Liu
- **期刊/来源**: Biometrics
- **机构**: Tsinghua University · Renmin University of China · Beihang University
- **分类**: vol 82 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在协变量自适应随机化（CAR）设计下研究重尾结果变量的处理效应估计问题，目标估计量为密度处理效应和总体分位数处理效应。作者首先分析了非参数核密度估计在 CAR 下的理论性质，为基于密度估计的处理效应估计量提供一致性保证。随后，他们利用该密度估计框架推导了密度处理效应和总体分位数处理效应的估计量，并证明了其相合性和渐近正态性。针对总体分位数处理效应，他们发现现有的基于影响函数的 M-估计量的方差估计量在更平衡的设计下会高估渐近方差，且不适用于所有随机化方法。为此，他们提出了一种新的分层变换均值差估计量以提高效率，并给出一个普遍适用的方差估计量以支持有效推断。数值实验验证了所提方法在有限样本下的有效性。对您而言，该文将重尾结果与 CAR 设计结合，为您的因果推断（特别是纵向或分层随机化）研究提供了新的估计和推断工具。
- **关键技术**: `covariate-adaptive randomization`, `kernel density estimation`, `influence function-based M-estimator`, `stratified transformed difference-in-means estimator`, `variance estimation`
- **为什么对您有用**: 该文直接关联您的因果推断兴趣，特别是 CAR 设计下的处理效应估计，且涉及重尾结果这一实际挑战。您可运用 very_familiar 的非参数统计和估计理论工具，评估其密度估计的收敛速率，或结合 moderately_familiar 的 semiparametric theory 检验其方差估计量的最优性。中期可做：若想深入 CAR 下的效率界，需在 semiparametric theory 上加强。

### 6. [10.1093/biomtc/ujag160](https://doi.org/10.1093/biomtc/ujag160) — Estimating effects on cumulative incidence probabilities by direct polytomous regression and polytomous log-odds product
- **作者**: Shiro Tanaka, Thomas H Scheike
- **期刊/来源**: Biometrics
- **机构**: Kyushu University Hospital · University of Copenhagen
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在竞争风险分析中，分别对每个原因建模可能导致累积发生率函数不满足自然的总和为1约束，从而缺乏联合一致性。本文提出直接多项式回归方法，通过基于多项式对数优势积的重参数化同时建模所有原因，强制实现一致性。该方法适用于具有随时间共同乘性效应的半参数模型以及关注特定时间点的模型。在右删失下，作者开发了分层逆概率删失加权（IPCW）估计量来估计效应参数。在指定的增广IPCW估计量类别中，所提估计量在给定正则条件下达到最小渐近方差，且无需为每个原因推导增广项的计算负担。模拟研究和两个实际数据应用（2型糖尿病队列研究和前列腺癌随机试验）展示了该一致建模方法的实用性。
- **关键技术**: `polytomous regression`, `inverse probability of censoring weighting (IPCW)`, `augmented IPCW estimators`, `semiparametric models`, `competing risks`
- **为什么对您有用**: 本文属于因果推断中竞争风险设定下的估计方法，直接关联您对纵向数据和因果推断的兴趣。您可以用非常熟悉的非参数统计和M估计理论来审视其半参数效率声明，并考虑其增广IPCW估计量是否可推广到更复杂的因果结构（如时变处理）。中期可做：若想深入其效率界推导，需在semiparametric theory上加强。

### 7. [10.1093/biomtc/ujag131](https://doi.org/10.1093/biomtc/ujag131) · [arXiv](https://arxiv.org/abs/2501.08270) — Individual causal effect estimation accounting for latent disease state modification among bipolar participants in mobile health studies
- **作者**: Charlotte R Fowler, Xiaoxuan Cai, Habiballah Rahimi-Eichi, Lisa Dixon, Justin T Baker, Jukka-Pekka Onnela et al.
- **期刊/来源**: Biometrics
- **机构**: Worcester Polytechnic Institute · The Ohio State University · McLean Hospital · New York State Psychiatric Institute · Columbia University · Harvard University
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对双相情感障碍患者的移动健康纵向数据，提出一种N-of-1个体因果效应估计方法。研究假设潜在疾病状态（如抑郁、躁狂）是干预（如社交活动）对健康结局（如睡眠时长）的效应修饰因子，目标是在存在缺失数据下估计状态特异性的个体因果效应。方法采用自回归隐马尔可夫模型（AR-HMM）识别潜在疾病状态，并基于反事实框架推导g-formula估计量来恢复该效应。通过大量模拟和一项多年智能手机研究的数据应用，与朴素方法比较，展示了所提方法的性能。该方法为纵向移动健康数据中的个体化因果推断提供了新工具，尤其适用于疾病状态异质性明显的人群。
- **关键技术**: `auto-regressive hidden Markov model`, `g-formula estimator`, `N-of-1 causal inference`, `counterfactual framework`, `missing data handling`
- **为什么对您有用**: 本文属于纵向因果推断与潜在状态建模的应用，直接关联您的主要兴趣（causal inference 的 longitudinal 子方向）。您可以用 very_familiar 的 estimation theory in causal inference 来审视其 g-formula 估计的有限样本性质，或用 moderately_familiar 的 identification theory 来检查潜在状态可识别性假设。中期可做：若想深入理论，需在 semiparametric theory 上加强（moderately_familiar），以推导该估计量的效率界。

### 8. [10.1093/biomtc/ujag120](https://doi.org/10.1093/biomtc/ujag120) · [arXiv](https://arxiv.org/abs/2504.03143) — Interim analysis in sequential multiple assignment randomized trials for survival outcomes
- **作者**: Zi Wang, Yu Cheng, Abdus S Wahed
- **期刊/来源**: Biometrics
- **机构**: University of Electronic Science and Technology of China · University of Pittsburgh · University of Rochester
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对序贯多臂随机试验（SMART）中的生存结局，提出统计上有效的全局中期监测（IM）方法，允许因疗效提前终止试验。研究目标是动态治疗方案的比较有效性，在患者经历多阶段治疗且分配随时间调整的设定下，需要处理重叠治疗路径带来的相关性。作者提出加权 log-rank 卡方统计量，以考虑重叠路径，并量化不同分析时间点 log-rank 统计量之间的相关性。基于该统计量，利用 Pocock、O'Brien-Fleming 和 Lan-DeMets 边界建立多次中期分析的疗效边界。通过大量模拟比较所提统计量与现有替代统计量的操作特性（I 类错误和功效），并在神经母细胞瘤数据集上进行了演示。对您而言，该工作将因果推断中的动态治疗方案与生存分析中的序贯检验相结合，其处理重叠路径的相关性结构方法可能对您的中介分析或纵向因果推断中的敏感性分析有借鉴意义。
- **关键技术**: `weighted log-rank statistic`, `group sequential design`, `Pocock/O'Brien-Fleming/Lan-DeMets boundaries`, `SMART design`, `survival analysis`
- **为什么对您有用**: 本文属于因果推断中的动态治疗方案（SMART）领域，直接关联您的主要兴趣中的纵向因果推断。您可以用 very_familiar 的估计理论（如 IPW 或 g-formula）来审视其加权统计量的构造，中期可做的是将其与您 moderately_familiar 的 semiparametric theory 结合，推导更高效的边界。立即可做的是用您的软件技能复现其模拟，中期可做的是在 moderately_familiar 的 identification theory 上长肌肉，以处理更复杂的治疗路径。

### 9. [10.1093/biomtc/ujag126](https://doi.org/10.1093/biomtc/ujag126) · [arXiv](https://arxiv.org/abs/2506.22805) — FLAME: a model for duration-dependent risk accumulation in episodic temporal exposures
- **作者**: Xinkai Zhou, Lee Goeddel, Nauder Faraday, Ciprian M Crainiceanu
- **期刊/来源**: Biometrics
- **机构**: Beijing Normal-Hong Kong Baptist University · Hong Kong Baptist University · Johns Hopkins University
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出 FLAME（FLexible Accumulation ModEl），一个针对 episodic temporal exposures 的半参数风险累积模型，目标是估计暴露 episode 的持续时间对结局风险的累积效应。模型将风险累积函数视为 episode 持续时间的未知函数，通过半参数结构（如可加或可乘的累积形式）识别，并允许 subject-specific 的 episode 数量和时长。估计方法基于 sieve 或样条逼近，结合广义估计方程或似然框架，得到风险累积函数的估计及其不确定性。应用数据来自心脏手术中的术中低血压监测，结果显示单次持续 60 分钟的低血压 episode 比 60 次 1 分钟的 episode 导致 AKI 风险增加 38%（0.33 vs 0.24），强调了 episode 时长模式的重要性。该方法可推广到其他高分辨率时间暴露场景，并提供了 R 包 flameRisk。对您而言，该模型涉及纵向暴露的因果效应估计，与您的 causal inference 和 longitudinal 兴趣相关，但其识别假设和估计效率值得进一步审视。
- **关键技术**: `semiparametric model`, `sieve estimation`, `risk accumulation function`, `episodic exposure`, `generalized estimating equations`
- **为什么对您有用**: 该论文属于因果推断中纵向暴露的建模，直接关联您的 primary interest 中的 causal inference 和 longitudinal 方向。您可以用 very_familiar 的 estimation theory in causal inference 来审视其识别假设和估计量的有限样本性质，或用 moderately_familiar 的 semiparametric theory 来推导其半参数效率界，判断其估计是否达到最优。中期可做：若想深入其 sieve 估计的收敛速度，需在非参数理论（moderately_familiar）上加强。

### 10. [10.1093/biomtc/ujag138](https://doi.org/10.1093/biomtc/ujag138) — Shift-adjusted Neyman–Pearson classifiers via single index modeling (SACSIM)
- **作者**: Jiaming Qiu, Ying-Qi Zhao, Yingye Zheng
- **期刊/来源**: Biometrics
- **机构**: Fred Hutch Cancer Center
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文提出 SACSIM，一种基于单指标模型的 Neyman–Pearson 分类器迁移方法，用于解决源域与目标域分布偏移下分类规则的适配问题。目标是在目标域上最大化临床收益（如灵敏度）同时控制误分类风险（如假阳性率），尤其关注对欠代表群体的公平性。方法利用目标域的小规模无标签样本、少量辅助信息以及源域的带标签数据，通过半参数模型估计移位参数，实现决策规则的调整。理论部分给出了所提估计量的渐近性质，并通过模拟和前列腺癌研究实例验证了方法的有效性。该方法将分布偏移下的分类问题转化为半参数估计问题，与因果推断中的外部效度（transportability）问题紧密相关，对您研究中的迁移学习和公平性分析有直接参考价值。
- **关键技术**: `Neyman-Pearson classification`, `single index model`, `semi-parametric estimation`, `distribution shift`, `transportability`
- **为什么对您有用**: 本文属于因果推断中外部效度（transportability）的应用，与您的 causal inference 兴趣直接相关；其半参数模型和移位调整策略可视为一种处理分布偏移的识别与估计方法，您可以用 very_familiar 的非参数统计和估计理论工具来审视其估计量的效率性质，例如推导其半参数效率界或检验其移位参数估计的渐近最优性；立即可做：基于现有武器库可尝试将其与您的 proximal causal inference 框架结合，处理未观测混杂下的迁移问题。

### 11. [10.1093/biomtc/ujag163](https://doi.org/10.1093/biomtc/ujag163) — Optimal subsampling methods for large clustered imbalanced data based on generalized estimating equations
- **作者**: Tingting Yu, Sehwan Kim, Rui Wang
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Harvard Pilgrim Health Care
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对大规模聚类数据中罕见事件（如心脏病发作）的 GEE 建模，提出基于最优子抽样的加权 GEE（SaWGEE）估计量。在独立或可交换工作相关结构下，推导出最小化渐近均方误差或其上界的最优个体级抽样概率，并证明当簇数或簇大小增长时估计量的渐近性质。与简单随机抽样和 1:1 病例对照抽样相比，SaWGEE 在保持相关结构的同时校正了不等抽样概率，显著提高了罕见事件信息的利用效率和有限样本稳定性。模拟研究验证了其性能，并应用于 2022 年 CDC 调查数据构建心脏病发作风险调整模型。该方法为大规模聚类纵向数据的因果推断和流行病学应用提供了计算可行的工具。
- **关键技术**: `generalized estimating equations`, `optimal subsampling`, `weighted estimating equations`, `asymptotic mean-square-error minimization`, `working correlation structure`, `case-control sampling`
- **为什么对您有用**: 本文属于流行病学应用（CDC 数据）和因果推断中的纵向/聚类数据建模，与您的 secondary interest 流行病学直接相关；其最优子抽样策略可视为一种计算约束下的估计方法，与您对统计计算和算法效率的兴趣有交集。您可以用 very_familiar 的软件开发和估计理论工具复现其最优抽样概率推导，或将其扩展到更复杂的相关结构，属于立即可做的方向。

### 12. [10.1093/biomtc/ujag166](https://doi.org/10.1093/biomtc/ujag166) — Flexible copula-based variable selection for interval-censored semi-competing risks data: application to aging research
- **作者**: Yuyao Zhang, Naijia Fan, Huiping Zheng, Ying Ding, Tao Sun
- **期刊/来源**: Biometrics
- **机构**: Chinese University of Hong Kong · Renmin University of China · University of Pittsburgh
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对老化研究中常见的半竞争风险数据（如残疾为非终点事件、死亡为终点事件），在非终点事件为区间删失且协变量维度较高时，提出一种基于 copula 的变量选择框架。边际分布采用半参数变换模型（涵盖比例风险与比例优势），联合分布用双参数 copula 灵活刻画上下尾依赖。估计采用 sieve 方法与新的坐标轮换优化算法，将高维问题分解为低维子问题，并基于近似信息准则实现免调参的变量选择。作者建立了估计量的渐近性质，模拟显示其变量选择准确且计算效率高。应用于中国老年健康影响因素跟踪调查（CLHLS），识别出与残疾和死亡相关的关键共病及生活方式因素。该方法为区间删失半竞争风险数据提供了一种可解释、可扩展的工具，对纵向因果推断和流行病学研究有直接参考价值。
- **关键技术**: `copula-based joint modeling`, `semiparametric transformation models`, `sieve estimation`, `coordinate-wise optimization`, `information criterion-based variable selection`
- **为什么对您有用**: 该文属于纵向因果推断与流行病学应用的交叉方向，直接对应您对 longitudinal causal inference 和流行病学队列研究的兴趣。其半竞争风险设定与区间删失处理是老化研究中的常见挑战，方法上的 sieve + 坐标轮换优化可借鉴到您熟悉的 M-estimation 框架中。您可用 very_familiar 的非参数统计和 M-estimation 理论快速评估其渐近论证，中期可尝试将变量选择思想推广到更复杂的因果 estimand（如动态处理效应）。

### 13. [10.1093/biomtc/ujag135](https://doi.org/10.1093/biomtc/ujag135) — Group sequential clinical trial designs for composite endpoints incorporating recurrent and terminal events
- **作者**: Qinghua Lian, Kwang Woo Ahn, Soyoung Kim, Brent R Logan, Melhem Solh, Michael J Martens
- **期刊/来源**: Biometrics
- **机构**: Bristol-Myers Squibb (United States) · Medical College of Wisconsin · Northside Hospital
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对复合终点（包含复发事件和终止事件）的临床试验，提出单样本和两样本的组序贯设计。目标估计量是平均频率函数，即随时间累积的所有复发和终止事件的计数。由于同一受试者的事件数据相关，检验统计量序列不满足独立增量结构，作者利用统计量的渐近协方差结构构造组序贯边界以控制 I 类错误。通过大量模拟验证了设计的 I 类错误控制和功效，并重新分析了 BMT CTN 1703 三期随机对照试验。该方法为纵向事件数据下的序贯检验提供了新工具，与您的纵向因果推断和假设检验兴趣相关。
- **关键技术**: `group sequential design`, `composite endpoints`, `mean frequency function`, `asymptotic covariance structure`, `recurrent and terminal events`
- **为什么对您有用**: 本文属于纵向事件数据下的假设检验方法，直接关联您的因果推断（纵向）和假设检验兴趣。您可以用 very_familiar 的估计理论（如 U-statistics 的渐近理论）来分析其检验统计量的渐近性质，或探索其与因果推断中复合终点估计的联系。中期可做：需在 moderately_familiar 的 semiparametric theory 上进一步熟悉以处理更复杂的协变量调整。

## 非参数 / 半参数  *(nonparam_semipara, 3 篇)*

### 1. [10.1093/biomtc/ujag118](https://doi.org/10.1093/biomtc/ujag118) — Statistical analysis of disease onset during lifespan with left truncation
- **作者**: Yue Wang, Bin Nan, Daniel L Gillen, Maria M Corrada
- **期刊/来源**: Biometrics
- **机构**: University of California, Irvine
- **分类**: vol 82 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对慢性病（如痴呆）发病时间分析提出一种新的非参数方法，在死亡频繁发生的老年队列中，研究以死亡时间为条件的发病时间分布，该分布由两个分量组成，分别对应生前发病与死亡前未发病的生存过程，解释直观且无需模型假设。方法采用核加权乘积限估计量，并正确处理了老龄研究中常见的左截断问题。估计量渐近正态，方差可由 Greenwood 型估计量估计，带宽选择基于积分 Brier 分数。通过模拟研究、The 90+ Study 和 UC Health Data Warehouse 数据验证了方法的有限样本性能。该方法为纵向老龄队列中疾病发病与死亡的联合分布提供了非参数推断工具，与您的纵向因果推断和半参数理论兴趣相关。
- **关键技术**: `kernel-weighted product-limit estimator`, `left truncation`, `Greenwood-type variance estimator`, `integrated Brier score`, `conditional distribution estimation`
- **为什么对您有用**: 本文属于非参数生存分析，直接关联您的非参数/半参数理论兴趣，特别是左截断处理与核加权估计的渐近理论。您可用 very_familiar 的非参数统计和 minimax 工具评估其估计量的最优性，或将其与纵向因果推断中的竞争风险设定联系，中期可探索将方法扩展到条件因果效应估计。

### 2. [10.1093/biomtc/ujag140](https://doi.org/10.1093/biomtc/ujag140) — Efficient estimation for deep generalized accelerated hazards models with interval-censored data
- **作者**: Qiang Wu, Mingyue Du, Shuangge Ma, Xingqiu Zhao
- **期刊/来源**: Biometrics
- **机构**: Hong Kong Polytechnic University · Jilin University · Yale University
- **分类**: vol 82 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对区间删失数据提出深度广义加速风险模型，旨在灵活刻画风险因素与失效时间风险的关系。估计采用结合深度神经网络与单调样条的筛极大似然方法，以捕捉非参数效应。在正则条件下，作者推导了估计量的非渐近误差界，并证明有限维参数估计渐近正态且达到半参数效率界。模拟研究评估了有限样本表现，并将方法应用于社区动脉粥样硬化风险研究。该方法将深度学习引入区间删失的半参数效率框架，对您在半参数效率理论与非参数估计方面的兴趣有直接关联。
- **关键技术**: `sieve maximum likelihood`, `deep neural networks`, `monotonic splines`, `semiparametric efficiency`, `nonasymptotic error bound`
- **为什么对您有用**: 本文属于半参数与非参数理论方向，直接关联您的 primary interest 中的 semiparametric theory 和 efficiency theory。您可以用 very_familiar 的 minimax bounds 工具来审视其非渐近误差界是否最优，或用 moderately_familiar 的 semiparametric theory 验证其效率论证的严密性。该文是立即可读并可能引发中期跟进工作的论文。

### 3. [10.1093/biomtc/ujag121](https://doi.org/10.1093/biomtc/ujag121) · [arXiv](https://arxiv.org/abs/2405.13353) — Adaptive Bayesian multivariate spline knot inference with prior specifications on model complexity
- **作者**: Junhui He, Ying Yang, Jian Kang
- **期刊/来源**: Biometrics
- **机构**: Tsinghua University · University of Michigan
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯框架用于多元样条回归中的节点推断，目标是在参数空间维度可变且似然函数不可微的设定下，同时估计节点的数量和位置。通过引入对模型复杂度有先验设定的先验分布，该方法能够处理不连续多元函数拟合、单变量变点检测以及多元回归中峰值定位等任务。方法的核心机制是基于可逆跳跃马尔可夫链蒙特卡洛（RJMCMC）或类似的可变维度采样技术，在节点数量和位置之间进行联合采样，并利用先验来控制模型复杂度。通过大量模拟研究评估了方法的性能，并在三头肌皮褶厚度测量和人类连接组计划的功能磁共振成像数据上展示了实际应用价值。结果表明，与现有方法相比，该方法在节点推断的准确性和模型拟合方面表现更优。对您而言，本文涉及的非参数回归中的模型选择与计算问题，与您对非参数统计和统计计算的兴趣相关，但其方法核心（贝叶斯可变维度推断）与您的主要研究领域（因果推断、高维统计）关联较弱。
- **关键技术**: `Bayesian spline regression`, `knot inference`, `reversible jump MCMC`, `model complexity prior`, `multivariate splines`
- **为什么对您有用**: 本文属于非参数统计中的模型选择与计算问题，与您对非参数统计和统计计算的兴趣相关，但并非您的主要研究方向。作为应用导向的论文，其方法学新颖性有限，主要贡献在于贝叶斯框架下的节点推断。从问题发现角度看，本文的核心机器（RJMCMC）不在您的武器库中，且与您熟悉的高阶U统计量或因果推断方法无直接接口，因此暂不可做。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1093/biomtc/ujag145](https://doi.org/10.1093/biomtc/ujag145) — A general framework for testing clustering significance and variable-level inference in high-dimensional data
- **作者**: Hui Shen, Dongmei Li, Yufeng Liu
- **期刊/来源**: Biometrics
- **机构**: McGill University · University of Rochester Medicine · University of Rochester · University of Michigan
- **分类**: vol 82 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 SigClust-DE，一个在高维数据中同时检验聚类显著性和识别驱动聚类分离变量的联合框架。针对 SigClust 方法在高维下零协方差估计不准确的问题，SigClust-DE 改进了零模型下协方差的估计，并将框架扩展至变量层面的推断，以识别与聚类分离相关的特征。在聚类显著性检验中，该方法通过控制第一类错误率来评估观察到的聚类是否反映真实结构而非抽样变异；在变量层面推断中，则通过控制错误发现率（FDR）来识别差异表达特征。通过大量模拟和 RNA-seq 数据应用，作者展示了 SigClust-DE 在聚类显著性检验中控制第一类错误、在变量推断中控制 FDR，并具有检测差异表达特征的强功效。该方法为聚类显著性检验和差异表达分析提供了统一的框架，对高维生物数据尤其有用。
- **关键技术**: `SigClust`, `Gaussian null model`, `covariance estimation`, `false discovery rate control`, `differential expression analysis`
- **为什么对您有用**: 本文属于假设检验方向，直接关联您对高维数据中假设检验的兴趣。其核心问题——在高维下检验聚类显著性并控制错误率——与您熟悉的高维渐近和 minimax 理论有交集。您可以用 very_familiar 的高维渐近工具来审视其零协方差估计的收敛性质，或评估其检验功效的 optimality。作为 Biometrics 上的方法学论文，它也是连接统计方法与实际应用（如 RNA-seq）的好例子。

### 2. [10.1093/biomtc/ujag119](https://doi.org/10.1093/biomtc/ujag119) · [arXiv](https://arxiv.org/abs/2502.18750) — One-at-a-time knockoffs
- **作者**: Charlie K Guan, Zhimei Ren, Daniel W Apley
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 3
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 one-at-a-time knockoffs (OATK)，一种在线性回归（含 ridge 和 lasso）中检测重要变量并控制 FDR 的新方法。与经典 knockoff filter 同时生成整个设计矩阵的 knockoff 列不同，OATK 每次只替换单个变量的列，从而大幅简化约束条件，仅需保持 Gram 矩阵的对应元素。检验统计量通过比较原始系数与 knockoff 系数构建，在原始设计矩阵满足温和的相关性假设下，作者证明 OATK 能渐近控制 FDR 于任意目标水平。模拟实验和真实遗传数据集表明，OATK 在保持良好 FDR 控制的同时，通常比现有方法具有更高功效，尤其在 HIV 治疗病毒学应答的全基因组关联研究中发现了更多经临床验证的独特突变。OATK 还带来显著的计算优势，并支持条件校准或去随机化等增强，以提升功效和 FDR 控制的稳定性。该方法与您在高维统计和假设检验方面的兴趣直接相关，其单列替换的构造思路也可能与您对 U-统计量计算复杂度的关注有潜在联系。
- **关键技术**: `knockoffs`, `false discovery rate control`, `linear regression`, `Gram matrix preservation`, `conditional calibration`, `derandomization`
- **为什么对您有用**: 本文属于高维变量选择与 FDR 控制的前沿方法，直接对应您 primary interests 中的 hypothesis testing 和高维统计。您可以用 very_familiar 的 minimax 界工具分析其渐近 FDR 控制的紧性，或从统计计算角度评估其单列替换策略的计算复杂度优势。

### 3. [10.1093/biomtc/ujag132](https://doi.org/10.1093/biomtc/ujag132) — Generalized Local Kendall’s τ: a novel framework for uncovering nonlinear local dependence
- **作者**: Zaixin Huang, Zhengjun Zhang
- **期刊/来源**: Biometrics
- **机构**: Shanghai University of Finance and Economics · University of Wisconsin–Madison · Beijing University of Chinese Medicine · University of Chinese Academy of Sciences
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出 Generalized Local Kendall's τ 框架，用于刻画非线性局部依赖，目标是在个性化医疗中识别患者亚组。该框架允许局部区域具有多样形状（如矩形、正方形、极值邻域），统一了全局、局部和尾部依赖。估计量包括基于 U-统计量和基于 copula 模型的两种，并引入四种新的分位数依赖测度和新的尾部依赖系数。作者开发了两种可视化工具（Type I 和 Type II 局部 Kendall's τ 曲面），应用于 Archimedean copulas 以辅助解释。模拟表明，在模型正确设定下，copula 估计量性能显著更优。通过帕金森病和 COVID-19 数据集展示了检测亚组特异性依赖模式的实际效用。对您而言，该框架的 U-统计量基础与您对高阶 U-统计量的兴趣直接相关，且其局部依赖分析思路可迁移至因果推断中的异质性处理效应探索。
- **关键技术**: `U-statistics`, `copula models`, `local dependence measures`, `tail dependence coefficients`, `quantile dependence`
- **为什么对您有用**: 该论文直接涉及 U-统计量（您 very_familiar 的武器）在依赖测度中的应用，且其局部依赖框架可用于因果推断中的异质性分析（如条件平均处理效应的探索）。立即可做：您可以用高阶 U-统计量的树宽/张量收缩视角分析其估计量的计算成本，或探索其 copula 估计量的渐近性质。

### 4. [10.1093/biomtc/ujag147](https://doi.org/10.1093/biomtc/ujag147) · [arXiv](https://arxiv.org/abs/2508.18815) — Blinded sample size recalculation in randomized controlled trials with analysis of covariance
- **作者**: Takumi Kanata, Yasuhiro Hagiwara, Koji Oba
- **期刊/来源**: Biometrics
- **机构**: National Center of Neurology and Psychiatry · The University of Tokyo
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对随机对照试验中基于协方差分析（ANCOVA）的样本量再计算问题，提出了一种盲态样本量再计算方法。现有方法假设结局与基线协变量的联合分布为多元正态，这在实践中常不成立；本文在极小的分布假设下，基于ANCOVA估计量的渐近相对效率（ARE）进行样本量再计算，允许任意模型误设。该方法在最终分析中能达到名义功效并控制I类错误率，同时减少所需样本量。通过模拟研究评估了多种场景下的表现，并应用于一项HIV临床试验，结果显示相比未调整分析，所需样本量最多可减少三分之一，尽管偶尔略有增加。
- **关键技术**: `blinded sample size recalculation`, `analysis of covariance (ANCOVA)`, `asymptotic relative efficiency`, `model misspecification`, `simulation study`
- **为什么对您有用**: 本文属于临床试验设计中的假设检验与功效分析，与您的主要兴趣（数学统计与假设检验）直接相关。您可以用非常熟悉的非参数统计和渐近理论工具来审视其ARE方法的严谨性，例如检查其效率损失是否最优。中期可做：若想深入，可在半参数理论（moderately_familiar）上加强，以推导更一般的效率界。

### 5. [10.1093/biomtc/ujag148](https://doi.org/10.1093/biomtc/ujag148) · [arXiv](https://arxiv.org/abs/2508.08758) — Random-effects meta-analysis via generalized linear mixed models: A Bartlett-corrected approach for few studies
- **作者**: Keisuke Hanada, Tomoyuki Sugimoto
- **期刊/来源**: Biometrics
- **机构**: Wakayama Medical University · The University of Osaka
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在随机效应元分析中，当研究数量较少时，传统的正态-正态模型下的小样本校正方法（如 Bartlett 校正）无法直接推广到广义线性混合模型（GLMM）。本文提出一个统一的 GLMM 框架，仅依赖汇总数据，可处理指数族分布（二项、泊松、伽马）的结果。核心方法是带简化 Bartlett 校正的剖面似然法（PLSBC），它改进了剖面似然比统计量的卡方近似，且无需计算高阶导数。理论上证明了所提估计量保持极大似然估计的一致性和渐近正态性。模拟显示 PLSBC 在多种结果类型下几乎无偏且覆盖率达到名义水平。三个真实元分析（二项、泊松、伽马）的应用表明该方法在小样本下稳健且可解释。对您而言，该文将 Bartlett 校正从正态模型扩展到 GLMM，是假设检验中有限样本校正的一个新进展，与您对假设检验的兴趣相关。
- **关键技术**: `Bartlett correction`, `profile likelihood`, `generalized linear mixed models`, `small-sample inference`, `coverage probability`
- **为什么对您有用**: 该文属于假设检验方向，具体是有限样本下似然比检验的校正，与您对 hypothesis testing 的兴趣直接相关。您可以用 very_familiar 的 M-estimation 理论来审视其 Bartlett 校正的渐近展开是否严密，或考虑将类似校正思想用于您熟悉的因果推断中的检验问题。立即可做：用 M-estimation 理论验证其理论证明；中期可做：若想推广到更复杂的模型，需在 semiparametric theory 上进一步熟悉；暂不可做：无需额外工具。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biomtc/ujag141](https://doi.org/10.1093/biomtc/ujag141) · [arXiv](https://arxiv.org/abs/2512.07739) — Symmetric vaccine efficacy
- **作者**: Lucy D’Agostino McGowan, Sarah C Lotspeich, Michael G Hudgens
- **期刊/来源**: Biometrics
- **机构**: University of North Carolina at Chapel Hill
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出对称疫苗效力（SVE）作为传统疫苗效力（VE）的替代指标，解决VE估计不对称、下界无界导致解释困难的问题。SVE定义为感染风险的一个对称变换，取值在[-1,1]内，对有益和有害效应提供统一尺度。作者推导了SVE与VE的关系，并基于二项分布或泊松近似给出点估计和置信区间（如Wald、score、bootstrap）。通过随机化HIV疫苗试验数据重新分析，展示SVE在避免极端负值、改善可解释性方面的优势。R包sve提供开源实现。对您而言，这是流行病学应用中一个简洁的效应度量重参数化案例，其推断方法（如置信区间构造）可迁移到因果推断中的效应尺度选择问题。
- **关键技术**: `symmetric transformation`, `confidence interval construction`, `bootstrap`, `randomized trial`, `R package`
- **为什么对您有用**: 本文属于流行病学应用，涉及效应度量的统计推断，与您的流行病学应用兴趣相关。武器库中的非参数统计和M估计理论足以理解其推断方法，但该文方法学新颖性有限，主要是应用导向。作为入门读物，它展示了如何将统计推断原则应用于公共卫生问题，但可能不值得深入阅读，除非您关注效应尺度选择。

### 2. [10.1093/biomtc/ujag155](https://doi.org/10.1093/biomtc/ujag155) — Inferring leakage in imports of frozen seafood allowing for censoring, testing accuracy and a minimum positive prevalence
- **作者**: Sumonkanti Das, Robert G Clark, Mahdi Parsa, Belinda Barnes
- **期刊/来源**: Biometrics
- **机构**: Australian National University · Australian Bureau of Agricultural and Resource Economics and Sciences
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究进口冷冻海产品中受污染批次（leakage）的推断问题，基于澳大利亚的筛查数据，目标是估计被接受批次中受污染的比例及污染单位数。作者扩展了已有的截断 beta-binomial 模型，允许测试灵敏度和特异度未知，并证明了在此设定下特异度可识别而灵敏度不可识别。他们还提出了一类新模型，假设批次的污染倾向要么为零要么高于某个最小阳性流行率阈值，这由案例驱动但具有更广泛的适用性。使用分层贝叶斯和极大似然方法对历史测试数据建模，揭示了泄漏风险的新见解。对您而言，本文是流行病学中应用因果/统计推断的实例，其可识别性分析（特异度可识别、灵敏度不可识别）与您对识别理论的兴趣相关，且截断数据建模方法可迁移至其他筛查场景。
- **关键技术**: `censored beta-binomial model`, `identifiability analysis`, `hierarchical Bayes`, `maximum likelihood`, `pooled testing`
- **为什么对您有用**: 本文属于流行病学应用，涉及筛查数据中的识别问题，与您的识别理论兴趣（causal inference 中的 identification）有直接联系。您可以用 very_familiar 的估计理论（如 M-estimation）来审视其可识别性证明，或考虑将截断 beta-binomial 模型推广到更复杂的相关结构。作为 gateway reading，本文数据描述清晰，模型设定明确，适合作为进入流行病学筛查建模的入门读物，武器库足以支撑理解。

## 其他  *(other, 21 篇)*

### 1. [10.1093/biomtc/ujag142](https://doi.org/10.1093/biomtc/ujag142) · [arXiv](https://arxiv.org/abs/2505.12181) — Reliable fairness auditing with semi-supervised inference
- **作者**: Jianhui Gao, Jessica Gronsbell
- **期刊/来源**: Biometrics
- **机构**: University of Toronto
- **分类**: vol 82 · issue 3
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文提出 Infairness，一个在半监督推断框架下审计机器学习模型公平性的统一方法。目标是在仅有少量标注数据和大量未标注数据时，估计模型在不同子群体上的公平性指标（如均方误差差异等）。方法通过回归模型插补缺失结局，并精心选择非线性基函数，结合小标注集和大未标注集进行推断。理论上证明该估计量对插补模型或 ML 模型的设定具有鲁棒性，且比仅用标注数据的监督估计更有效。在电子健康记录和医学影像两个真实公平性审计中，方差降低了 40-60%。对您而言，该方法涉及半监督推断和鲁棒估计，与您的因果推断和效率理论兴趣有潜在联系，但主题更偏向公平性审计而非核心统计理论。
- **关键技术**: `semi-supervised inference`, `imputation with nonlinear basis functions`, `robust estimation`, `variance reduction`
- **为什么对您有用**: 本文属于应用统计方法，涉及半监督推断和鲁棒性，与您的效率理论（semiparametric efficiency）和因果推断（估计子群体差异）有间接联系。但主题是公平性审计，非您核心兴趣。作为 Biometrics 的应用论文，可作入门阅读，但方法学新颖性一般。

### 2. [10.1093/biomtc/ujag123](https://doi.org/10.1093/biomtc/ujag123) · [arXiv](https://arxiv.org/abs/2502.12729) — Unsupervised optimal deep transfer learning for classification under general conditional shift
- **作者**: Junjun Lang, Yukun Liu
- **期刊/来源**: Biometrics
- **机构**: East China Normal University
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究无监督最优深度迁移学习在一般条件偏移下的分类问题。作者提出一种新的“一般条件偏移”假设，将标签偏移作为特例，并在无需强分离条件的情况下保证目标分布和偏移函数的可识别性。分类器结合深度神经网络与伪极大似然方法，并建立了分类器及条件概率估计量的渐近误差界，其界依赖于源数据条件概率的内在维度。所提分类器的超额风险达到最优极小极大速率（至多差对数因子），且无需估计偏移函数，在条件概率具有低维结构时可缓解维数灾难。数值模拟和阿尔茨海默病数据集分析验证了方法的优越性。
- **关键技术**: `deep neural networks`, `pseudo-maximum likelihood`, `general conditional shift`, `minimax optimal rate`, `intrinsic dimension`
- **为什么对您有用**: 本文属于迁移学习与半参数/非参数理论的交叉，其识别性假设和极小极大速率结果与您的非参数与半参数理论兴趣相关；但核心是分类与迁移学习，而非因果推断或高维统计。您可用非常熟悉的非参数极小极大界工具来审视其速率是否紧，但方法本身与您的技术武库交集有限，属于中期可做的方向。

### 3. [10.1093/biomtc/ujag122](https://doi.org/10.1093/biomtc/ujag122) — Subgroup identification and membership prediction
- **作者**: Lu Chen, Xuerong Chen, Xinzhou Guo, Yi Li
- **期刊/来源**: Biometrics
- **机构**: Southwestern University of Finance and Economics · Hong Kong University of Science and Technology · University of Michigan
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对临床试验中治疗异质性导致的亚组识别问题，提出一个无分布假设的最小二乘回归框架。该框架允许亚组成员关系依赖于协变量，且系数分组数目和组织结构可随协变量变化，突破了传统有限混合模型和阈值模型对分布假设和预设结构的依赖。方法上，先基于正则化技术高效检测线性回归系数的亚组结构，再用支持向量机恢复对应的划分，从而对新个体进行亚组成员预测。与成对融合正则化相比，该方法大幅降低了计算复杂度。作者建立了组特定参数估计和划分恢复的理论保证，并通过模拟和真实数据验证了实用性。对您而言，该文的亚组识别与预测问题与您的因果推断兴趣中异质性处理效应估计相关，但其核心贡献在于聚类与分类的统计计算，而非因果识别或效率理论。
- **关键技术**: `least-squares regression`, `regularization`, `support vector machine`, `subgroup identification`, `membership prediction`
- **为什么对您有用**: 该文涉及异质性处理效应下的亚组识别，与您的因果推断兴趣（如个体化处理效应）有概念上的连接，但方法学上属于聚类与分类的统计计算，而非因果推断的核心方法。从技术武器库看，您熟悉的非参数统计和M估计理论可用于理解其理论保证，但该文并未涉及您擅长的U统计量或半参数效率理论，因此作为方法学参考价值有限。若作为亚组分析的应用案例，可关注其真实数据应用，但整体上属于边缘相关。

### 4. [10.1093/biomtc/ujag151](https://doi.org/10.1093/biomtc/ujag151) · [arXiv](https://arxiv.org/abs/2508.11213) — Estimating covariate effects on functional connectivity using voxel-level fMRI data
- **作者**: Wei Zhao, Brian J Reich, Emily C Hector
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 3
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对静息态 fMRI 功能连接分析中，因高维 voxel 数据而常采用 ROI 内平均信号的做法，提出一种保留 voxel 级信息的新方法。作者以 ROI 间经验 voxel 相关作为汇总统计量，并为其构建一个新的正定协方差函数，以刻画这些相关之间的复杂空间依赖结构。在此基础上，开发了一个计算高效的两步估计程序，用于对区域级连接上的协变量效应进行可扩展的统计推断。模拟研究表明，与标准平均方法相比，该方法在推断有效性上有显著提升，且不确定性量化校准良好。在 Autism Brain Imaging Data Exchange 数据上，作者发现自闭症谱系障碍与注意力相关 ROI 间的功能连接改变有关。该方法为大规模神经影像研究提供了可解释且统计严谨的协变量效应估计框架。
- **关键技术**: `positive definite covariance function`, `two-step estimation`, `voxel-wise correlations`, `functional connectivity`, `spatial dependence modeling`
- **为什么对您有用**: 本文属于应用统计工作，涉及高维数据下的协方差建模和两步估计，与您的高维统计和统计计算兴趣有间接联系，但并非核心方法学创新。作为神经影像应用，可视为流行病学或应用因果推断的潜在数据集来源，但方法学迁移性有限。

### 5. [10.1093/biomtc/ujag144](https://doi.org/10.1093/biomtc/ujag144) — Bayesian network meta-regression models for multivariate aggregate responses with partially observed or completely missing within-treatment sample covariance matrices
- **作者**: Simiao Gao, Sungduk Kim, Ming-Hui Chen, Arvind K Shah, Jianxin Lin, Joseph G Ibrahim
- **期刊/来源**: Biometrics
- **机构**: University of Connecticut · National Cancer Institute · Division of Cancer Epidemiology and Genetics · Merck & Co., Inc., Rahway, NJ, USA (United States) · University of North Carolina at Chapel Hill
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一个贝叶斯多元网络 meta-regression 模型，用于比较治疗心血管和糖尿病的多种疗法，其中多元汇总结局包括低密度脂蛋白胆固醇、高密度脂蛋白胆固醇和甘油三酯。为处理某些治疗仅出现在单一研究中的困难，作者对治疗随机效应的标准差假设了一个对数线性回归模型。由于研究内样本协方差矩阵 S 部分观测或完全缺失，且研究内样本相关系数完全未观测，作者对未知的研究内协方差矩阵设定了一个层次结构。他们进一步开发了 MCMC 采样算法从后验分布中抽样，以及一个 Monte Carlo 程序来对多元结局的治疗效果进行排序。模型比较使用 DIC，并开发了两种 DIC 变体来量化多元模型相对于单变量模型的整体拟合改进以及每个结局的拟合增益。通过对真实随机对照试验的汇总数据进行详细分析，进一步证明了所提方法的有效性。
- **关键技术**: `Bayesian network meta-regression`, `hierarchical modeling of covariance matrices`, `MCMC sampling`, `DIC model comparison`, `Monte Carlo ranking`
- **为什么对您有用**: 本文属于贝叶斯 meta-analysis 应用，涉及缺失协方差矩阵的建模，与您的因果推断（尤其是纵向和中介分析中的协方差结构）有一定方法学联系，但并非核心兴趣。作为流行病学领域的应用工作，它展示了处理复杂数据结构的实用方法，但方法学新颖性有限。

### 6. [10.1093/biomtc/ujag150](https://doi.org/10.1093/biomtc/ujag150) — DAG trend filtering for genomic denoising via higher-order Bayesian networks and DAG shrinkage processes
- **作者**: Weixuan Zhu, Fan Liao, Yang Ni
- **期刊/来源**: Biometrics
- **机构**: Xiamen University · The University of Texas at Austin
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出有向无环图趋势滤波（GTF）框架，用于基因组数据的去噪，其核心是引入高阶贝叶斯网络和图形收缩过程，以增强沿图有向边的信号平滑的局部自适应性。与基于无向图的传统 GTF 不同，该方法显式利用图的定向结构，提高可解释性和依赖捕获的准确性。推断采用哈密顿蒙特卡洛算法。模拟和基因组应用表明，该方法在均方误差降低和信噪比提升方面优于现有 GTF 算法。对您而言，本文属于统计计算与图模型的应用，与您的主要兴趣（如高阶 U 统计、计算复杂度）关联较弱，但可作为图结构去噪方法的入门参考。
- **关键技术**: `directed acyclic graph trend filtering`, `higher-order Bayesian networks`, `graphical shrinkage processes`, `Hamiltonian Monte Carlo`
- **为什么对您有用**: 本文属于统计计算与图模型的应用，与您的主要兴趣（如高阶 U 统计、计算复杂度）关联较弱，但可作为图结构去噪方法的入门参考。

### 7. [10.1093/biomtc/ujag146](https://doi.org/10.1093/biomtc/ujag146) · [arXiv](https://arxiv.org/abs/2511.15882) — Bayesian semiparametric modeling of biomarker variability in joint models
- **作者**: Sida Chen, Jessica K Barrett, Marco Palma, Jianxin Pan, Brian D M Tom
- **期刊/来源**: Biometrics
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究纵向生物标志物轨迹的个体内变异性（WIV）与临床结局的关联，采用基于曲率的轨迹粗糙度定义（TB-WIV），并需借助联合模型（JM）进行动态风险预测。作者在贝叶斯半参数框架下比较了三种纵向建模方法：两种新提出的（贝叶斯惩罚样条 P-splines 和函数主成分分析 FPCA）以及一种改编的现有半参数方法。通过模拟研究评估了参数估计、TB-WIV 关联检测、效应量估计和生存预测性能，并警示解释原始 TB-WIV 关联幅度需谨慎。方法应用于英国囊性纤维化登记数据，发现肺功能 TB-WIV 与死亡风险显著正相关，且独立于基础肺功能水平，并证明 TB-WIV 能提升生存预测信息。
- **关键技术**: `Bayesian penalized splines`, `functional principal component analysis`, `joint models for longitudinal and time-to-event data`, `trajectory-based within-individual variability`, `dynamic risk prediction`
- **为什么对您有用**: 本文属于纵向因果推断与半参数建模的应用，与您的 primary interest 中 causal inference 的 longitudinal 子方向及 semiparametric theory 相关。虽然方法学新颖性有限（主要是比较现有方法），但 UK 囊性纤维化登记数据及 TB-WIV 的估计流程对流行病学应用有参考价值。从武器库看，您对 semiparametric theory 和 M-estimation 熟悉，可中期尝试将 TB-WIV 的估计与因果推断中的 mediation 或 sensitivity analysis 结合，但需先补充贝叶斯计算技能。

### 8. [10.1093/biomtc/ujag130](https://doi.org/10.1093/biomtc/ujag130) — A Bayesian transfer learning model for mixed-effects longitudinal data analysis
- **作者**: Jialing Liu, Souradipto Ghosh Dastidar, Steffen Ventz
- **期刊/来源**: Biometrics
- **机构**: University of Minnesota
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种用于纵向数据的贝叶斯迁移学习模型（BTLL），目标是在目标数据集样本量小、估计不稳定时，从多个源数据集借力以提升目标总体的推断精度。模型对目标与源研究结局模型的关键参数差异采用混合先验建模，实现数据自适应的信息借用，并旨在最小化源研究带来的负迁移偏差。通过模拟和真实数据（轻度认知障碍进展为痴呆的纵向队列）验证，BTLL 相比替代方法显著提高目标研究参数估计精度，并在异质性设置下降低估计偏差。该方法属于贝叶斯分层建模与迁移学习的结合，与您的主要兴趣（因果推断、半参数理论、高维统计）关联较弱，但纵向数据设定与流行病学应用有一定交集。
- **关键技术**: `Bayesian transfer learning`, `mixture priors`, `longitudinal mixed-effects models`, `data-adaptive information borrowing`
- **为什么对您有用**: 本文属于纵向数据建模的应用型方法论文，与您的 primary interests（因果推断、半参数效率、高维统计）无直接交集，但纵向设定与流行病学队列研究（secondary interest）相关。作为流行病学应用，其数据结构和预测目标（痴呆风险）可能提供数据集参考，但方法学上无直接可迁移的因果推断或效率理论工具。武器库中的非参数统计和 M-估计理论不足以支撑深入方法学跟进，且本文未涉及因果识别或半参数效率，故暂不可做。

### 9. [10.1093/biomtc/ujag143](https://doi.org/10.1093/biomtc/ujag143) · [arXiv](https://arxiv.org/abs/2505.07232) — Spatial confounding in multivariate areal data analysis
- **作者**: Kyle Lin Wu, Sudipto Banerjee
- **期刊/来源**: Biometrics
- **机构**: University of California, Los Angeles
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究多元区域数据中的空间混杂问题，在贝叶斯核心区域化（coregionalized）回归模型下，从分析和数据生成两个视角考察空间混杂对固定效应估计的影响。作者推导出新结果：在空间混杂存在时，多元区域模型的后验方差膨胀有限，空间点估计相比非空间对应物保持更高精度。模拟实验表明，即使空间结构被错误设定，空间分析仍优于非空间模型，支持分层空间模型的偏好。实证部分使用美国县级肥胖/糖尿病患病率和糖尿病相关癌症死亡率数据，比较有无空间随机效应的结果。对您而言，本文属于贝叶斯空间统计的应用型工作，与您的主要兴趣（因果推断、高维统计等）关联较弱，但可作为流行病学数据应用的入门参考。
- **关键技术**: `Bayesian coregionalized areal regression`, `spatial confounding`, `posterior variance inflation`, `multivariate disease mapping`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），但方法学上以贝叶斯空间模型为主，与您的主要统计兴趣（因果推断、高维、半参数）无直接交集。作为流行病学数据应用的入门读物，其数据结构和建模思路可参考，但武器库（如非参数、U-统计）难以直接迁移。建议仅作浏览，不值得深读。

### 10. [10.1093/biomtc/ujag124](https://doi.org/10.1093/biomtc/ujag124) · [arXiv](https://arxiv.org/abs/2603.11916) — Distributionally balanced sampling designs
- **作者**: Anton Grafström, Wilmer Prentius
- **期刊/来源**: Biometrics
- **机构**: Swedish University of Agricultural Sciences
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一类新的概率抽样设计——分布平衡设计（DBD），目标是在完整辅助变量分布层面而非仅若干矩上实现样本对总体的代表性。在生态、林业和环境科学等领域，野外数据采集成本高昂，最大化有限样本的信息量至关重要。DBD 可视为最小差异设计，最小化样本与总体辅助分布之间的期望差异。作者给出等包含概率情形下的首个实现，基于优化后的总体循环排序并随机选取连续区块。排序准则为最小化设计期望能量距离，该差异度量能捕捉低阶矩之外的分布差异，促进强空间扩散，并降低随辅助变量平滑变化的总量的 Horvitz-Thompson 估计量方差。模拟表明，近似 DBD 在分布拟合上优于局部枢轴和局部立方等现有方法，可提高昂贵野外数据估计的可靠性。
- **关键技术**: `probability sampling design`, `energy distance`, `minimum discrepancy design`, `Horvitz-Thompson estimator`, `circular ordering`
- **为什么对您有用**: 本文属于抽样设计领域，与您的主要兴趣（因果推断、高维统计等）无直接重叠，但其中能量距离作为分布差异度量，可能对您在高阶 U 统计量或非参数检验中的分布比较问题有启发。作为方法论论文，其设计思想（最小化分布差异）可迁移至平衡性诊断或敏感性分析。不过，本文并非入门读物，且与您的技术武器库（如高阶 U 统计、半参数理论）关联较弱，暂不建议深入阅读。

### 11. [10.1093/biomtc/ujag154](https://doi.org/10.1093/biomtc/ujag154) · [arXiv](https://arxiv.org/abs/2509.15480) — A tree-based kernel for densities and its applications in clustering DNase-seq profiles
- **作者**: Yuliang Xu, Kaixuan Luo, Li Ma
- **期刊/来源**: Biometrics
- **机构**: Johns Hopkins University · University of Chicago
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种基于二叉树的密度核（tree-based kernel），用于在分层贝叶斯框架下对多个采样密度进行建模，并作为潜在变量模型（如混合模型）中的核函数以实现样本聚类。该核通过多元 logit-normal 模型和稀疏精度矩阵刻画树分裂概率，从而诱导灵活的（函数）协方差结构，能够捕捉染色质可及性数据中转录因子足迹的空间长程依赖。贝叶斯推断采用 Pólya–Gamma 增广的 Gibbs 采样。模拟研究表明该核显著提升聚类精度；在 ENCODE 的 DNase-seq 数据上，聚类结果对应两种常见转录因子的结合事件，具有生物学意义。
- **关键技术**: `tree-based kernel`, `multivariate logit-normal model`, `sparse precision matrix`, `Pólya–Gamma augmentation`, `Gibbs sampling`, `Bayesian nonparametrics`
- **为什么对您有用**: 本文属于应用统计（生物信息学）方向，与您的主要兴趣（因果推断、高维统计、U-统计量等）无直接交集，但可作为统计方法在基因组学中应用的入门读物。其树结构建模和稀疏精度矩阵思想与您熟悉的图模型/稀疏高维方法有潜在联系，但核心方法（贝叶斯非参数混合）不在您的武器库中，且无直接可迁移的方法学问题。

### 12. [10.1093/biomtc/ujag152](https://doi.org/10.1093/biomtc/ujag152) · [arXiv](https://arxiv.org/abs/2404.11323) — Bayesian optimization for identification of optimal biological dose combinations in personalized dose-finding trials
- **作者**: James Willard, Shirin Golchi, Erica E M Moodie
- **期刊/来源**: Biometrics
- **机构**: University of Cambridge · MRC Biostatistics Unit · McGill University
- **分类**: vol 82 · issue 3
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究早期个性化剂量-反应试验中，针对联合疗法识别患者特异的最优生物剂量组合（OBD）的问题，目标是在安全约束下最大化治疗收益。鉴于试验样本量小且存在多个剂量因子和协变量模式，传统参数方法难以应对，作者提出基于贝叶斯优化的序贯搜索策略。方法上，用独立高斯过程分别建模疗效和毒性曲面，通过采集函数（acquisition function）定义剂量探索策略，并利用OBD位置的后验熵设计自适应停止规则。模拟研究考察了疗效和毒性响应异质性程度的影响，并针对阻塞性睡眠呼吸暂停（OSA）双药试验比较了多种最终设计，结果显示所提方法在设定场景下表现良好。对您而言，本文属于应用导向的贝叶斯优化与试验设计交叉工作，与您的主要兴趣（因果推断、半参数理论）关联较弱，但可作为统计计算与序贯决策方法的入门读物。
- **关键技术**: `Bayesian optimization`, `Gaussian process`, `acquisition function`, `posterior entropy stopping rule`, `personalized dose-finding`
- **为什么对您有用**: 本文属于统计计算与试验设计的应用工作，与您的主要兴趣（因果推断、高维统计、半参数理论）无直接重叠，但其中高斯过程建模和序贯决策策略可作为统计计算方向的入门阅读；您的武器库（非参数统计、软件工程）足以理解方法，但缺乏贝叶斯优化背景，需先补充相关知识；作为gateway reading，本文可读性较好，但方法学新颖性有限，不值得优先投入时间。

### 13. [10.1093/biomtc/ujag128](https://doi.org/10.1093/biomtc/ujag128) — Bayesian tele-connected spatial clustering of multivariate spatial data with applications to disease-mapping
- **作者**: Srijato Bhattacharyya, Huiyan Sang, Bani Mallick
- **期刊/来源**: Biometrics
- **机构**: Texas A&M University
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种新的贝叶斯空间聚类方法，用于多元空间疾病数据，目标是识别具有不同疾病模式的地理子区域，同时考虑空间邻近性和多个疾病测量之间的依赖性。方法核心是开发一种随机远程连通图划分先验，允许未知数量的簇，既能鼓励局部连续簇，又能将远程子区域聚在一起。该先验被嵌入贝叶斯层次模型，用于检测空间簇并估计簇特异的疾病模式和多元变量间的依赖结构。为进行后验推断，作者设计了定制的MCMC算法，利用高效的二分裂-合并采样器并借助图算法。通过模拟研究验证方法性能，并将其应用于1985-2014年美国南部六州县级前列腺癌死亡率下降的聚类模式分析。
- **关键技术**: `Bayesian hierarchical model`, `random tele-connected graph partition prior`, `MCMC`, `split-merge sampler`, `spatial clustering`
- **为什么对您有用**: 本文属于应用统计方法论文，与您的主要兴趣（因果推断、高维统计等）无直接交集，但作为流行病学应用（疾病制图）的gateway阅读，可了解空间聚类方法在健康数据中的应用。您的武器库（如非参数统计、MCMC）足以理解其方法，但该方向并非您的研究重点，因此作为入门读物价值有限，不值得优先投入时间。

### 14. [10.1093/biomtc/ujag125](https://doi.org/10.1093/biomtc/ujag125) · [arXiv](https://arxiv.org/abs/2506.22313) — Manifold-constrained Gaussian processes for inference of mixed-effects ordinary differential equations with application to pharmacokinetics
- **作者**: Yuxuan Zhao, Samuel W K Wong
- **期刊/来源**: Biometrics
- **机构**: University of Waterloo
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对混合效应常微分方程（mixed-effects ODE）模型，在贝叶斯框架下提出一种流形约束高斯过程（manifold-constrained Gaussian process）推断方法，用于处理群体动力学中个体间参数异质性、部分观测和轨迹对参数敏感等问题。方法的核心是将ODE解约束在流形上，通过高斯过程先验对个体轨迹进行建模，并利用嵌套优化实现参数和轨迹的快速准确推断。模拟实验验证了方法的准确性和计算效率，并应用于HIV联合治疗研究的药代动力学真实数据分析。该方法为非线性混合效应ODE模型提供了一种计算上可行的贝叶斯推断方案，但方法论上属于应用导向的扩展，理论创新有限。
- **关键技术**: `manifold-constrained Gaussian processes`, `mixed-effects ODE models`, `Bayesian inference`, `nested optimization`, `pharmacokinetic modeling`
- **为什么对您有用**: 本文属于统计计算与贝叶斯方法的交叉应用，与您的统计计算兴趣相关，但并非核心方向。作为流行病学应用（HIV药代动力学）可作入门阅读，但方法学上无直接可迁移的武器。武器库足以理解，但无需深入。

### 15. [10.1093/biomtc/ujag021](https://doi.org/10.1093/biomtc/ujag021) · [arXiv](https://arxiv.org/abs/2406.00778) — Bayesian joint additive factor models for multiview learning
- **作者**: Niccolo Anceschi, Federico Ferrari, David B Dunson, Himel Mallick
- **期刊/来源**: Biometrics
- **机构**: Duke University · Merck & Co., Inc., Rahway, NJ, USA (United States) · Cornell University · Weill Cornell Medicine
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出两种贝叶斯联合因子回归模型用于多视图学习，目标是在多组学数据中同时推断视图内与视图间的依赖关系，并改善对临床结局的预测。基线模型 JFR 用单一因子集捕捉跨视图的联合变异，而更精细的 JAFAR 将变异分解为共享成分与视图特有成分，以应对不同视图信噪比差异大的问题。为保证分解的可识别性，作者为 JAFAR 设计了依赖的累积收缩过程（D-CUSP）先验，JFR 则使用独立版本（I-CUSP）。模型通过 Gibbs 采样实现，能灵活处理特征与结局的分布，并具备特征选择与不确定性量化能力。在免疫组、代谢组和蛋白质组数据上预测分娩时间，展示了相对现有方法的性能提升。对您而言，本文属于贝叶斯多视图建模的应用型工作，与您的主要兴趣（因果推断、半参数理论）关联较弱，但其中的因子分解与可识别性处理思路对纵向或中介分析中的潜在变量建模或有参考价值。
- **关键技术**: `Bayesian factor regression`, `cumulative shrinkage process`, `joint additive factor model`, `Gibbs sampling`, `multi-view learning`
- **为什么对您有用**: 本文属于应用统计建模，与您的主要兴趣（因果推断、高维统计、半参数理论）无直接交集，但多视图数据中的共享/特有成分分解与可识别性设计，对您关注的纵向因果推断中的潜在混杂建模可能有一定启发。作为 Biometrics 上的应用型论文，可作为了解多组学数据建模的入门读物，但方法学新颖性一般，不值得深入精读。

### 16. [10.1093/biomtc/ujag134](https://doi.org/10.1093/biomtc/ujag134) — A Bayesian contamination model for serial dilution assays
- **作者**: Siquan Wang, Qixuan Chen, Matthew S Perzanowski, Adnan Divjan, Andrew Gelman
- **期刊/来源**: Biometrics
- **机构**: Columbia University
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对连续稀释测定（serial dilution assays）中浓度估计的边界效应与样本污染问题，提出一个贝叶斯污染模型。该模型同时识别受污染的样本并估计未知样本的浓度，同时量化估计不确定性。在多种污染场景的模拟研究中，所提方法一致优于常用方法。作者还以纽约市哮喘与过敏研究的免疫测定原始数据为例，展示了贝叶斯工作流的逐步应用。该工作为免疫测定中检测污染样本和估计浓度提供了实用方法，并提出了将未知污染过程纳入贝叶斯建模工作流的通用框架。对您而言，本文的贝叶斯建模与不确定性量化思路，以及处理测量误差和污染的实际应用，可作为统计计算与流行病学应用方向的参考。
- **关键技术**: `Bayesian contamination model`, `serial dilution assay`, `calibration curve`, `uncertainty quantification`, `Bayesian workflow`
- **为什么对您有用**: 本文属于流行病学应用（免疫测定数据），与您的 secondary interest 中流行病学应用方向相关；其贝叶斯建模和不确定性量化方法可作为统计计算方向的参考。武器库中非参数统计和估计理论可帮助理解其模型假设，但核心是贝叶斯方法，非您的主要兴趣，因此作为入门或应用参考。

### 17. [10.1093/biomtc/ujag165](https://doi.org/10.1093/biomtc/ujag165) — A Bayesian adaptive digital twin design for avatar-driven cancer clinical trials
- **作者**: Peng Yang, Yeonhee Park, Suyu Liu
- **期刊/来源**: Biometrics
- **机构**: The University of Texas MD Anderson Cancer Center · Rice University · Sungkyunkwan University
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯自适应临床试验设计，利用小鼠或实验室动物移植瘤（avatar）作为患者的数字孪生，以指导个性化治疗选择。研究问题是在存在患者异质性和avatar与患者之间转化差异（translational discrepancy）的背景下，如何联合建模avatar肿瘤生长和患者临床结局（毒性、无进展生存期）来优化治疗分配。方法上，作者构建了一个联合模型，将avatar治疗反应与患者数据相结合，预测每个患者的治疗效用，并通过潜在类别模型处理avatar仅在部分患者中作为有效替代终点的情况。通过模拟研究，该设计相比不含avatar信息的传统试验，显著提高了患者接受个性化最优治疗的概率并改善了治疗结局。对您而言，本文属于应用统计方法在临床试验设计中的案例，其贝叶斯自适应框架和潜在类别建模思路虽与您的主要兴趣（因果推断、高维统计等）无直接交集，但可作为流行病学或个性化医疗应用方向的入门阅读。
- **关键技术**: `Bayesian adaptive design`, `joint modeling`, `latent class model`, `digital twin`, `personalized medicine`
- **为什么对您有用**: 本文属于流行病学/个性化医疗的应用型工作，可作为secondary interest中流行病学方向的入门读物；其贝叶斯自适应设计和潜在类别建模方法虽不直接对应您的技术武器库，但可帮助您了解临床试验设计中的统计建模思路，武器库足以支撑理解，但无需深入方法学细节，适合快速浏览。

### 18. [10.1093/biomtc/ujag136](https://doi.org/10.1093/biomtc/ujag136) · [arXiv](https://arxiv.org/abs/2412.11267) — P3LS: Point Process Partial Least Squares
- **作者**: Jamshid Namdari, Robert T Krafty, Amita Manatunga
- **期刊/来源**: Biometrics
- **机构**: Emory University
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出点过程偏最小二乘（P3LS），用于处理预测变量为点过程（如患者肾图）的回归/分类问题。在 log-Gaussian Cox 过程框架下，将点过程预测器的潜在时变强度函数作为 PLS 的输入，通过估计强度函数实现降维和预测。估计过程利用 log-Gaussian Cox 过程的性质，并建立了预测一致性。模拟研究评估了有限样本表现，并应用于肾放射性核素成像数据以预测肾梗阻。该方法为点过程预测器提供了首个 PLS 扩展，但理论深度有限，主要贡献在于应用和算法。
- **关键技术**: `partial least squares`, `log-Gaussian Cox process`, `point process predictors`, `predictive consistency`
- **为什么对您有用**: 本文属于统计方法在生物医学应用中的工作，与您的主要兴趣（因果推断、高维统计等）无直接交集，但可作为流行病学/临床数据中点过程预测的入门读物。武器库中的非参数统计和估计理论足以理解其方法，但无直接可攻的问题。

### 19. [10.1093/biomtc/ujag127](https://doi.org/10.1093/biomtc/ujag127) · [arXiv](https://arxiv.org/abs/2509.07267) — Monitoring adverse events through Bayesian nonparametric clustering across studies
- **作者**: Shijie Yuan, Kevin Roberts, Noirrit Kiran Chandra, Yuan Ji, Peter Müller
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Austin · Pfizer (United States) · The University of Texas at Dallas · University of Chicago
- **分类**: vol 82 · issue 3
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯非参数方法，用于跨研究汇总的不良事件（AE）监测。模型基于协变量依赖的产品划分模型（PPMx），通过定义成对相似度度量对具有相似协变量特征的实验单元进行随机划分，以提高 AE 发生率估计的精度。该方法能整合历史试验的外部数据以定义背景发生率，并适应从患者级到研究级的不同协变量粒度。框架支持盲态下的实时安全监测，并可无缝过渡到揭盲分析。通过案例研究和模拟研究展示了模型在多种试验场景下检测安全信号和评估风险的能力。
- **关键技术**: `Bayesian nonparametrics`, `product partition model with covariates (PPMx)`, `random partition`, `pairwise similarity measure`, `real-time safety monitoring`
- **为什么对您有用**: 本文属于贝叶斯非参数聚类在临床试验安全监测中的应用，与您的主要兴趣（因果推断、高维统计等）无直接交集，但作为流行病学/临床试验领域的应用工作，其数据整合和实时监测框架可能对您了解真实世界数据的安全信号检测有参考价值。武器库中的非参数统计和估计理论可帮助理解其模型设定，但核心的贝叶斯计算并非您的专长，因此仅作为入门级阅读，不值得深入跟进。

### 20. [10.1093/biomtc/ujag156](https://doi.org/10.1093/biomtc/ujag156) — A Bayesian model averaging method for dose ranging studies in oncology
- **作者**: Adetayo Kasim, Nathan W Bean, Elena Parkhomenko, Amelia Cottle, Andre Acusta, Helen Zhou et al.
- **期刊/来源**: Biometrics
- **机构**: GlaxoSmithKline (United States) · GlaxoSmithKline (Japan)
- **分类**: vol 82 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对肿瘤学剂量优化研究提出一种贝叶斯模型平均方法 BAMADOS，用于二元结局的剂量-反应建模。在 Project Optimus 背景下，随机剂量优化试验样本量小、剂量水平少，传统 MCP-Mod 等方法不再适用。BAMADOS 假设反应与剂量单调，不预设候选模型，而是在约束模型空间中评估所有可能模型。为缓解 Occam 剃刀效应，采用广义正态先验族中的非共轭中等信息先验。模拟研究表明，BAMADOS 能正确识别最优生物剂量，且在先验与数据不一致时仍能低偏估计反应率；与 MCP-Mod 相比，在小样本（每剂量≤30人）下功效更高，大样本下功效相当。该方法对您可能有用：其模型平均与先验设计思路可迁移至因果推断中的敏感性分析或纵向数据建模，但方法学新颖性有限，属于应用型方法论文。
- **关键技术**: `Bayesian model averaging`, `generalized normal priors`, `constrained model space`, `dose-response modeling`, `binary endpoints`
- **为什么对您有用**: 本文属于应用统计方法，与您的 primary interests（因果推断、半参数理论）无直接交集，但可作为流行病学或临床试验数据分析的入门读物；其贝叶斯模型平均与先验稳健性设计对您的中期可做方向（如敏感性分析中的先验扰动）有一定启发，但核心机器（贝叶斯计算）不在您的武器库中，暂不可直接跟进。

### 21. [10.1093/biomtc/ujag161](https://doi.org/10.1093/biomtc/ujag161) — Seamless dose optimization design accounting for unknown patient heterogeneity in cancer clinical trials
- **作者**: Rebecca B Silva, Bin Cheng, Shing M Lee
- **期刊/来源**: Biometrics
- **机构**: Columbia University
- **分类**: vol 82 · issue 3
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对肿瘤临床试验中的剂量优化问题，提出了一种两阶段自适应设计，以应对患者异质性未知的情况。第一阶段基于毒性数据估计安全剂量集；第二阶段利用疗效和患者特征数据，通过贝叶斯稀疏组选择（Bayesian Sparse Group Selection）识别影响反应的异质性亚群，并整合药代动力学数据以刻画暴露-毒性关系。设计在阶段间进行无效性评估，以确定目标人群，并为每个识别出的亚群推荐最优剂量。模拟研究表明，该模型驱动的方法能有效识别与异质性相关的患者特征，并为不同亚群给出差异化剂量建议。该设计区别于大多数预设亚群的试验设计，强调在早期阶段通过数据学习亚群结构。
- **关键技术**: `Bayesian Sparse Group Selection`, `two-stage adaptive design`, `pharmacokinetic modeling`, `futility assessment`, `dose optimization`
- **为什么对您有用**: 本文属于临床试验设计领域，与您的主要兴趣（因果推断、高维统计等）无直接交集，但其中贝叶斯稀疏组选择用于异质性识别的方法，可能对您在因果推断中处理未观测异质性（如 proximal causal inference 中的 latent confounder）有启发。作为应用型论文，其方法学新颖性有限，但若您对临床试验设计或贝叶斯变量选择感兴趣，可作为入门读物。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

