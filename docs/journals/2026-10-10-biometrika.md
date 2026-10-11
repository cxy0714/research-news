# Biometrika  ·  2026-10-10

- 共 13 篇 · Biometrika

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期共13篇论文，主线大致可归为四类：因果识别与推断（4篇）、假设检验与推断理论（4篇）、半参数效率与两阶段设计（2篇）、以及计算与高维方法（3篇）。因果推断部分覆盖了工具变量、代理结局、非欧结果变量和生存分析中的因果 estimand；假设检验部分则从稳健置信区间、过参数化推断、水印生成到模型置信集，跨度较大。半参数效率主线聚焦两阶段抽样与自适应选择；计算与高维部分则涉及优化下界、谱估计和点过程正则化。

最突出的主线是因果推断与代理信息的结合。`Predictions as Surrogates` 将机器学习预测输出纳入代理结局框架，提出重校准预测驱动推断，通过灵活学习最优插补损失构造高效估计量，并在估计不一致时仍保证优于仅用真实数据；`The Multiplicative Instrumental Variable Model` 则以乘法可分性替代传统单调性条件，识别 ATT，估计量兼具多重稳健与半参数有效性。两篇均以“利用额外信息提升效率”为核心，但前者依赖预测模型，后者依赖工具变量结构，形成互补。`Geodesic difference-in-differences` 将 DID 推广到测地度量空间，处理分布、网络等非欧结果，识别 geodesic ATT，并扩展到交错设定，与前述两篇在“扩展经典因果框架”上呼应。

第二条主线是推断在非标准设定下的稳健性。`Confidence Intervals for Linear Models with Arbitrary Noise Contamination` 在 Huber 污染下构造一致覆盖的置信区间，无需污染比例先验，且长度达到最优阶；`Benign Overfitting Beyond Prediction` 则系统刻画过参数化 OLS 插值器的估计与推断性质，推广 Gauss-Markov 定理，两者分别从污染和过参数化角度挑战经典推断假设。`Post-reduction inference` 利用 Fisher 条件推断的充分性分离，解决高维筛选后模型置信集的校准问题，与前述两篇共同构成“推断在模型不确定或数据污染下如何保持有效性”的讨论。`Optimal Watermark Generation` 虽主题不同，但将水印生成形式化为假设检验，与推断主线在错误率控制上存在方法交叉。

半参数效率与两阶段设计方面，`An optimal two-step estimation approach` 提出两步估计量，利用廉价协变量与结局的工作模型更新初始估计，任意工作模型下渐近不劣于完全数据估计量，并达到最优效率；`Bias correction for Chatterjee’s graph-based correlation coefficient` 则修正最近邻图相关系数的偏差，在维度不超过三时消除慢速率项，实现 n^{1/2} 一致估计。两篇均涉及非参数或半参数估计的精细理论，前者侧重设计效率，后者侧重偏差修正。计算与高维部分，`Optimal and computationally tractable lower bounds` 构造分段二次下界加速 MM 算法，与广义 lasso 联系；`Regularised Spectral Estimation` 将 Whittle 伪似然与惩罚结合，处理高维点过程谱估计，两者均以计算可行性为目标。

若按主题优先阅读：因果推断方向可先看 `The Multiplicative Instrumental Variable Model` 与 `Geodesic difference-in-differences`，前者提供新的 IV 识别机制，后者扩展 DID 到非欧空间；半参数效率方向关注 `An optimal two-step estimation approach` 与 `Predictions as Surrogates`，前者处理两阶段设计，后者结合预测模型；高维推断方向则看 `Benign Overfitting Beyond Prediction` 与 `Post-reduction inference`，分别涉及过参数化推断和筛选后置信集。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1093/biomet/asag055](https://doi.org/10.1093/biomet/asag055) · [arXiv](https://arxiv.org/abs/2507.09302) — The Multiplicative Instrumental Variable Model
- **作者**: Jiewen Liu, Chan Park, Yonghoon Lee, Yunshu Zhang, Mengxin Yu, James M Robins et al.
- **期刊/来源**: Biometrika
- **机构**: University of Pennsylvania · University of Illinois Urbana-Champaign · Washington University in St. Louis · Harvard University
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文提出乘法工具变量模型（MIV），在工具变量（IV）设计中，通过假设工具与未测混杂因子对治疗倾向得分的影响是乘法可分的（即无乘法交互），替代传统的单调性或同质性条件，从而在非参数设定下识别治疗组平均处理效应（ATT）。识别估计量为经典 Wald 比率的单臂版本，作者证明了其非参数可识别性。估计方面，提出了一类多重稳健且半参数有效的估计器，并给出了影响函数与渐近性质。通过扩展模拟和一项职业培训项目对收入影响的实证研究验证了方法的有限样本表现。该工作为 IV 识别提供了新的机制性解释，即工具与混杂因子独立影响治疗选择，对因果推断中 IV 方法的理论发展有重要贡献。
- **关键技术**: `multiplicative IV model`, `nonparametric identification`, `ATT`, `Wald ratio`, `multiply robust estimation`, `semiparametric efficiency`
- **为什么对您有用**: 直接推进因果推断中 IV 识别的理论，提出新的可检验条件（乘法交互）替代单调性，与您的 identification theory 和 semiparametric efficiency 兴趣高度契合；可用您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 semiparametric theory 来审视其多重稳健估计的效率性质，并考虑扩展至纵向或代理变量设定。

### 2. [10.1093/biomet/asag053](https://doi.org/10.1093/biomet/asag053) · [arXiv](https://arxiv.org/abs/2501.09731) — Predictions as Surrogates: Revisiting Surrogate Outcomes in the Age of AI
- **作者**: Wenlong Ji, Lihua Lei, Tijana Zrnic
- **期刊/来源**: Biometrika
- **机构**: Stanford University
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在代理结局（surrogate outcome）的经典框架下，将预测模型输出视为真实结局的低成本代理，与预测驱动推断（prediction-powered inference, PPI）建立正式联系。作者提出重校准预测驱动推断（recalibrated PPI），通过机器学习灵活学习最优“插补损失”（imputed loss），从而构造更高效的估计量。该方法在最优插补损失估计不一致时仍能保证优于仅用真实结局数据的估计量，若估计一致则达到 PPI 类估计量的最小渐近方差。优化目标在损失函数凸时保持凸性，计算可行。理论分析和数值实验表明，在预测系统性偏离结局的常见场景下，有效样本量显著提升，并通过三个使用前沿 AI 模型的应用展示了实际收益。对您而言，该文将代理结局识别与半参数效率理论结合，为因果推断中的效率提升提供了新视角。
- **关键技术**: `prediction-powered inference`, `surrogate outcomes`, `recalibration`, `imputed loss`, `semiparametric efficiency`, `convex optimization`
- **为什么对您有用**: 该文直接连接您的 causal inference 子方向（代理结局与效率理论），且其重校准思想可迁移至您的 proximal CI 或 mediation 设定。您可用 very_familiar 的 semiparametric theory 和 M-estimation 工具分析其效率界，或探索将 recalibration 与 higher-order U-statistics 结合以处理复杂插补损失。中期可做：需在 moderately_familiar 的 HOIF 上长肌肉以处理高阶影响函数。

### 3. [10.1093/biomet/asag054](https://doi.org/10.1093/biomet/asag054) · [arXiv](https://arxiv.org/abs/2501.17436) — Geodesic difference-in-differences
- **作者**: Yidong Zhou, Daisuke Kurisu, Taisuke Otsu, Hans-Georg Müller
- **期刊/来源**: Biometrika
- **机构**: University of Minnesota · The University of Tokyo · London School of Economics and Political Science · University of California, Davis
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出 geodesic DID，将经典 DID 框架从欧氏或标量结果推广到一般测地度量空间中的结果变量（如分布、网络、流形值数据）。现有非欧结果变量的 DID 方法主要依赖分位数函数空间的线性运算，无法推广到一般度量空间；本文利用测地线作为差分的替代，定义 geodesic ATT 作为因果 estimand。作者在唯一测地度量空间且具备测地传输结构的设定下，建立了 geodesic ATT 的识别性，并利用度量几何与经验过程理论推导了样本版本的收敛速率。框架进一步扩展到交错 DID 设定，允许多期与异质处理时点。实证部分分析了苏联解体对年龄死亡分布的健康影响，以及美国电力市场自由化对发电结构的影响。对您而言，本文在非欧结果变量的因果识别与估计上提供了新视角，与您 causal inference 中 longitudinal 和 mediation 方向有潜在连接。
- **关键技术**: `geodesic transport`, `difference-in-differences`, `metric geometry`, `empirical process theory`, `staggered DID`
- **为什么对您有用**: (1) 直接连接 causal inference 中 DID 识别与估计的扩展方向，特别是非欧结果变量（分布、网络）的因果推断；(2) 可用您 very_familiar 的 nonparametric statistics 与 minimax bounds 工具审视其收敛速率是否最优，或用 higher-order U-statistics 的视角分析其估计量的高阶性质；(3) 中期可做：需先在 semiparametric theory 上长肌肉，以深入理解其识别假设与效率界。

### 4. [10.1093/biomet/asag056](https://doi.org/10.1093/biomet/asag056) · [arXiv](https://arxiv.org/abs/2501.15284) — Beyond Fixed Restriction Time: Adaptive Restricted Mean Survival Time Methods in Clinical Trials
- **作者**: Jinghao Sun, Douglas E Schaubel, Eric J Tchetgen Tchetgen
- **期刊/来源**: Biometrika
- **机构**: University of Pennsylvania
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对右删失生存数据，提出自适应受限平均生存时间（RMST）方法，以替代在比例风险假设不成立时失效的风险比。核心问题是限制时间的选择：过小会遗漏晚期效应，过大会增大方差、降低功效。作者提出数据驱动的准则，在连续范围内最大化兼顾效应大小与估计精度的目标函数，从而自适应选择最优限制时间。理论部分处理了自适应选择引入的额外变异性，并针对零假设下的非正则估计提出两种策略：基于凸包的估计量和惩罚化方法。当限制时间在离散网格上预指定时，所提过程与在惩罚总体最优值处评估的oracle估计量具有相同的一阶分布，选择不带来额外的一阶方差。模拟显示该方法在多种生存情景下优于传统RMST分析和log-rank检验，并在一个三期胰腺癌试验中发现了标准方法遗漏的临床获益。
- **关键技术**: `Adaptive restricted mean survival time`, `Nonregular estimation`, `Convex-hull-based estimator`, `Penalized selection`, `Oracle property`
- **为什么对您有用**: 本文属于因果推断中生存分析的应用方法，直接关联您对纵向数据和临床试验中因果效应的兴趣。其处理非正则估计的策略（凸包、惩罚）与您熟悉的M估计和半参数理论有接口，可用您very_familiar的软件开发和估计理论来复现或扩展。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1093/biomet/asag059](https://doi.org/10.1093/biomet/asag059) · [arXiv](https://arxiv.org/abs/2403.12908) — Regularised Spectral Estimation for High-Dimensional Point Processes
- **作者**: C J Pinkney, C Euán, A J Gibberd, A Shojaie
- **期刊/来源**: Biometrika
- **机构**: Lancaster University · Heriot-Watt University · University of Washington
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维多元点过程（如神经元峰电位序列）的谱密度矩阵估计问题，提出将 Whittle 伪似然与岭或 Lasso 惩罚相结合的正则化估计方法。在神经科学中，谱密度矩阵可用于推断神经元之间的脑网络连接，但高维峰电位数据使得传统谱估计统计量难以计算。作者建立了所提估计量的渐近和大样本性质，并在多元 Hawkes 过程模拟数据上评估了其性能。最后，将方法应用于真实的神经科学峰电位数据，展示了其推断脑连接的能力。该方法为高维点过程的频域分析提供了正则化工具，对您在高维统计和统计计算方面的兴趣有直接关联。
- **关键技术**: `Whittle pseudo-likelihood`, `ridge penalty`, `Lasso penalty`, `spectral density matrix estimation`, `multivariate Hawkes process`
- **为什么对您有用**: 本文属于高维统计推断，直接关联您的高维统计与随机矩阵理论兴趣，特别是高维协方差/谱矩阵的估计问题。您可以用 very_familiar 的高维渐近和 minimax 界工具来审视其估计量的收敛速率是否最优，或用 moderately_familiar 的 M-估计理论分析其惩罚估计的 oracle 性质。中期可做：需在 moderately_familiar 的 semiparametric 理论上稍加延伸以处理点过程的非参数谱估计。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biomet/asag051](https://doi.org/10.1093/biomet/asag051) · [arXiv](https://arxiv.org/abs/2508.09040) — Bias correction for Chatterjee’s graph-based correlation coefficient
- **作者**: Mona Azadkia, Leihao Chen, Fang Han
- **期刊/来源**: Biometrika
- **机构**: London School of Economics and Political Science · University of Amsterdam · University of Washington
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文针对 Azadkia & Chatterjee (2021) 提出的基于最近邻图的相关系数，研究其偏差项并给出修正。该系数能一致地检测独立性和函数依赖，但其最近邻估计量含有一个可能以慢于 n^{1/2} 速率消失的偏差项，阻碍了参数速率的一致性。作者首先细致分析该偏差项，证明在维度不超过三时偏差渐近可忽略；对更一般的维度，提出偏差修正程序。在两种情形下，均得到以 n^{1/2} 速率一致且渐近正态的估计量。该工作属于非参数独立性检验与图基统计量的理论分析，对您在高阶 U-统计量和非参数理论方面的兴趣有直接关联。
- **关键技术**: `nearest-neighbour graph`, `bias correction`, `asymptotic normality`, `parametric rate`, `dependence measure`
- **为什么对您有用**: 本文属于非参数独立性检验的理论分析，直接关联您的非参数与半参数理论兴趣；其偏差分析技术可能用到高阶 U-统计量的投影方法，您可用 very_familiar 的 U-统计量工具来验证或改进其偏差界。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1093/biomet/asag057](https://doi.org/10.1093/biomet/asag057) · [arXiv](https://arxiv.org/abs/2510.11587) — An optimal two-step estimation approach for two-phase studies
- **作者**: Q Zhou, K Y Wong
- **期刊/来源**: Biometrika
- **机构**: University of North Carolina at Charlotte · Hong Kong Polytechnic University
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究两阶段抽样（two-phase sampling）设计下的估计效率问题：第一阶段观测结局和廉价协变量，第二阶段仅对子集测量昂贵协变量，导致缺失数据问题。作者提出一类两步估计量：先用完整数据（第二阶段样本）得到初始估计量，再用基于廉价协变量与结局的工作模型构造的渐近均值为零的估计量进行更新，从而利用全部数据信息。该类估计量在任意工作模型设定下都渐近不劣于完全数据估计量，且对工作模型误设有稳健性。作者提出基于核的方法构造该类估计量，并在该类估计量中达到最优效率；当完全非参数核方法不可行时，提出基于多个工作模型的简单联合更新方法以近似最优估计量。模拟和癌症基因组学实际数据应用展示了所提方法相对现有方法的优势。对您而言，该文是半参数效率理论与实际缺失数据设计结合的典型例子，其两步更新框架与您熟悉的 one-step 估计和 influence function 思想直接相关。
- **关键技术**: `two-phase sampling`, `two-step estimation`, `kernel-based estimation`, `working model`, `semiparametric efficiency`, `robustness to misspecification`
- **为什么对您有用**: 该文直接关联您的效率理论（semiparametric efficiency bounds）与因果推断中的缺失数据问题，属于半参数估计的经典设定。您可用 very_familiar 的 nonparametric statistics 和 minimax 工具分析其核估计的收敛速率，或用 moderately_familiar 的 semiparametric theory 验证其最优性声明。中期可做：若想推广到高维协变量，需在 high-dimensional statistics 上加强（点名：高维核方法或稀疏估计）。

## 数理统计 / 假设检验  *(hypothesis_testing, 5 篇)*

### 1. [10.1093/biomet/asag058](https://doi.org/10.1093/biomet/asag058) · [arXiv](https://arxiv.org/abs/2511.07605) — Confidence Intervals for Linear Models with Arbitrary Noise Contamination
- **作者**: Dong Xie, Chao Gao, John Lafferty
- **期刊/来源**: Biometrika
- **机构**: University of Chicago · Yale University
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究 Huber 污染模型下线性回归的置信区间构造，其中噪声变量以未知比例被任意污染。虽然该设定下的稳健点估计已有充分研究，但统计推断仍具挑战性，尤其是污染比例不可识别。作者提出一种基于平滑估计函数的 Z-estimation 框架，无需污染水平的先验知识即可构造单个回归系数的置信区间。方法通过预处理步骤对与 nuisance 参数相关的协变量进行去相关，直接量化估计方程的不确定性。理论证明该置信区间对所有污染分布具有一致覆盖，且长度达到最优阶 O(1/n(1-ε)^2)，与已知污染比例时的速率匹配。这一结果与高斯位置模型中稳健区间估计的自适应代价形成鲜明对比，表明线性回归中可实现无自适应损失。
- **关键技术**: `Z-estimation`, `smooth estimating function`, `decorrelation`, `Huber contamination model`, `uniform coverage`
- **为什么对您有用**: 本文直接关联您的假设检验与稳健统计兴趣，其核心问题是污染比例不可识别下的有效推断，属于数学统计中的前沿问题。您可运用 very_familiar 的 minimax 界技术验证其最优长度率是否紧，或利用 moderately_familiar 的 M-estimation 理论分析其 Z-estimator 的渐近性质。立即可做：基于现有工具推导该估计量的 influence function 并比较不同去相关策略。

### 2. [10.1093/biomet/asag039](https://doi.org/10.1093/biomet/asag039) · [arXiv](https://arxiv.org/abs/2309.15769) — Benign Overfitting Beyond Prediction: The Ordinary Least Squares Interpolator
- **作者**: Dennis Shen, Dogyoon Song, Peng Ding, Jasjeet Sekhon
- **期刊/来源**: Biometrika
- **机构**: University of Southern California · University of California, Davis · University of California, Berkeley
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究过参数化线性模型中最小 ℓ2 范数 OLS 插值器的参数估计与推断性质，而非传统的预测风险。作者在 Gauss-Markov 模型下建立了 leave-k-out 公式、遗漏变量偏误公式和 Frisch-Waugh-Lovell 定理的过参数化类比，并推广了 Gauss-Markov 定理，分析了同方差下的方差估计。这些结果系统性地刻画了过参数化 OLS 的估计与推断行为，为良性过拟合提供了超越预测的新视角。对您而言，该工作将经典线性模型理论延伸到过参数化设定，与您在高维统计和因果推断中的估计与推断兴趣直接相关。
- **关键技术**: `minimum ℓ2-norm OLS interpolator`, `leave-k-out formulas`, `omitted-variable bias`, `Frisch-Waugh-Lovell theorem`, `Gauss-Markov theorem`
- **为什么对您有用**: 本文属于高维/过参数化线性模型的推断理论，直接连接您的高维统计与假设检验兴趣。您可以用 very_familiar 的 minimax 界工具来检验其估计量的最优性，或用 moderately_familiar 的 semiparametric 理论来审视其效率性质。立即可做：基于其 leave-k-out 公式推导过参数化下的置信区间构造；中期可做：结合 HOIF 分析其高阶偏差。

### 3. [10.1093/biomet/asag049](https://doi.org/10.1093/biomet/asag049) · [arXiv](https://arxiv.org/abs/2512.05333) — Optimal Watermark Generation under Type I and Type II Errors
- **作者**: Hengzhi He, Shirong Xu, Alexander Nemecek, Jiping Li, Erman Ayday, Guang Cheng
- **期刊/来源**: Biometrika
- **机构**: University of California, Los Angeles · Xiamen University · Case Western Reserve University
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文将水印生成问题形式化为一个统计假设检验问题，在零分布与其水印版本之间进行检验，目标是在控制第一类与第二类错误率的前提下最小化生成保真度损失。作者以一般 f-散度度量保真度损失，推导出可实现的最小损失的下界，并刻画达到该下界的最优水印分布。进一步，他们提出了一种对应的采样规则，作为插入水印的最优机制，在最小化保真度失真的同时满足错误率约束。该结果建立了假设检验、信息散度与水印生成之间的简洁而广泛适用的原则。
- **关键技术**: `f-divergence`, `Neyman-Pearson lemma`, `hypothesis testing`, `optimal transport`, `watermarking`
- **为什么对您有用**: 该论文将水印生成问题转化为假设检验框架，并给出最优性刻画，与您的假设检验与效率理论兴趣直接相关。您可以用非常熟悉的 minimax 界和 Neyman-Pearson 引理来验证其下界是否紧，并考虑将 f-散度推广到更一般的损失函数。中期可做：若想深入其采样规则的实现，可能需要熟悉最优传输或计算统计的特定工具。

### 4. [10.1093/biomet/asag045](https://doi.org/10.1093/biomet/asag045) · [arXiv](https://arxiv.org/abs/2507.10373) — Post-reduction inference for confidence sets of models
- **作者**: H S Battey, D G Rasines, Y Tang
- **期刊/来源**: Biometrika
- **机构**: Imperial College London · CUNEF Universidad
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对高维回归中模型本身作为推断对象的问题，提出在初步变量筛选（reduction）之后，对模型置信集进行有效推断的方法。其核心思想是利用 Fisher 条件推断中的充分性/余充分性和辅助性/余辅助性分离，使得模型充分性检验不依赖于偏离方向，从而避免因使用同一数据进行筛选和评估而导致的校准问题。在无 nuisance 参数理想情形下，该分离能无损失、无冗余提取信息；文章详细展示了正态线性模型中估计 nuisance 参数对理想化的影响，并推广到对数正态加速失效模型。作为分析的一部分，作者引入了 Fan et al. (2012) 的 refitted cross-validation 估计量的修正版本，其分布理论在适当条件意义下可处理。结论表明，在缩减样本上进行筛选无问题的情况下，样本分裂相对于条件分析具有高效率，呼应 Cox (1975)；否则会产生校准错误的置信集。
- **关键技术**: `sufficiency/co-sufficiency separation`, `ancillarity/co-ancillarity separation`, `conditional inference`, `refitted cross-validation`, `sample splitting`, `confidence sets for models`
- **为什么对您有用**: 该文直接关联您对假设检验和因果推断中模型不确定性的兴趣，特别是高维设定下模型选择后的推断问题。您非常熟悉的非参数统计和极小极大界工具可用于分析其条件推断的效率，而您对因果推断中估计量的理解有助于将这种分离思想推广到因果模型选择。中期可做：需在 moderately_familiar 的 semiparametric theory 上加强，以处理更复杂的 nuisance 参数结构。

### 5. [10.1093/biomet/asag052](https://doi.org/10.1093/biomet/asag052) · [arXiv](https://arxiv.org/abs/2608.26553) — Tight differencing in spectral density estimation with centrosymmetric kernels
- **作者**: Y Wang, K W Chan
- **期刊/来源**: Biometrika
- **机构**: Chinese University of Hong Kong
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究序列相关数据下谱密度与长期方差的均值稳健估计问题，目标是在存在易变趋势或突变时仍保持估计的可靠性。现有方法将差分与核平均结合时，紧差分（小滞后差分）会引入强相关，破坏核平均估计的高阶性质，导致最优性受损。作者提出一类新的中心对称核，专门设计为与紧差分兼容，从而解决这一不兼容性。文中证明，对于序列相关数据，最优紧差分序列与经典独立数据情形不同，且这些最优序列是数据无关的，可直接应用而无需预拟合。所提估计量在平稳性检验和白噪声检验等统计推断任务中表现出实用性。
- **关键技术**: `spectral density estimation`, `long-run variance estimation`, `centrosymmetric kernels`, `tight differencing`, `kernel averaging`
- **为什么对您有用**: 本文属于假设检验与时间序列推断方向，与您对 hypothesis testing 的兴趣直接相关；其核心是构造与差分兼容的核以恢复估计的最优性，您可以用 very_familiar 的非参数统计和核方法知识快速理解其机制，并考虑将中心对称核思想迁移到其他长期方差估计场景。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biomet/asag060](https://doi.org/10.1093/biomet/asag060) · [arXiv](https://arxiv.org/abs/2410.10309) — Optimal and computationally tractable lower bounds for logistic log-likelihoods
- **作者**: Niccoló Anceschi, Cristian Castiglione, Tommaso Rigon, Giacomo Zanella, Daniele Durante
- **期刊/来源**: Biometrika
- **机构**: Statistical and Applied Mathematical Sciences Institute · Duke University · Bocconi University · University of Milano-Bicocca
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究 logistic log-likelihood 的切线下界问题，目标是构造比二次 minorizer 更紧但仍可计算的下界，以加速 MM 算法和变分贝叶斯近似。作者提出一种分段二次下界，它一致优于任意切向二次 minorizer，并与广义 lasso 问题有直接联系。理论部分证明了该下界的优化性质，实证部分展示了其在点估计和 VB 近似中的加速与精度提升。该工作属于计算统计中的优化与近似方法，对您而言，其分段二次构造与广义 lasso 的联系可能为统计计算中的算法设计提供新视角。
- **关键技术**: `piecewise quadratic lower bound`, `minorize-maximize (MM) algorithm`, `variational Bayes approximation`, `generalized lasso`
- **为什么对您有用**: 本文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关。您可以用 very_familiar 的软件开发和数值方法经验，快速实现并验证该分段二次下界在您熟悉的模型（如 logistic 回归）上的效果，属于立即可做的 follow-up。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

