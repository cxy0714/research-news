# Scand. J. Stat. — Vol 50  Issue 3  ·  2026-05-21

- 共 24 篇 · Scandinavian Journal of Statistics

## 高维统计 / 随机矩阵  *(high_dim_rmt, 3 篇)*

### 1. [10.1111/sjos.12632](https://doi.org/10.1111/sjos.12632) — Variable selection for high‐dimensional generalized linear model with block‐missing data
- **作者**: Yifan He, Yang Feng, Xinyuan Song
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1279-1297
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维广义线性模型（GLM）在多块缺失数据下的变量选择与估计问题，设定为多源数据融合中的块状缺失模式。方法分两步：首先利用块状缺失的协方差结构进行稀疏精度矩阵估计，随后基于观测块对缺失块进行条件均值回归插补。理论部分在 GLM 框架下证明了插补后估计量的变量选择与估计一致性。相比现有仅适用单块缺失或强依赖模型结构的插补法，该回归插补策略对多种缺失机制更具鲁棒性。ADNI 阿尔茨海默症数据的应用验证了其优越性。对您而言，该文的稀疏精度矩阵估计与块缺失插补理论，可为处理多源流行病学队列数据的高维推断提供方法学参考。
- **关键技术**: `sparse precision matrix estimation`, `conditional mean regression imputation`, `block-wise missing data`, `high-dimensional GLM`, `variable selection consistency`
- **为什么对您有用**: 涉及您的高维统计主方向（稀疏精度矩阵与变量选择一致性），且 ADNI 数据应用对您在流行病学队列数据的缺失值处理与高维推断有直接参考价值。

### 2. [10.1111/sjos.12628](https://doi.org/10.1111/sjos.12628) — Robust sure independence screening for nonpolynomial dimensional generalized linear models
- **作者**: Abhik Ghosh, Erica Ponzi, Torkjel Sandanger, Magne Thoresen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1232-1262
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在超高频（nonpolynomial 维度 p ≫ n）广义线性模型（GLM）设定下，经典 SIS 变量筛选方法对异常值和噪声极其不稳定。本文提出基于最小密度幂散度估计（MDPDE）的边际回归系数稳健筛选程序，以应对数据污染场景。核心机制是利用 MDPDE 的稳健性替代传统估计，从总体和样本层面证明了边际 MDPDE 的均匀一致性，进而推导出所提算法的 sure screening 性质。此外，文章将该方法扩展至稳健条件筛选并给出了相应的理论保证。对您有用：虽然本文侧重稳健筛选而非 RMT 或半参数效率，但其 nonpolynomial 维度下的均匀一致性与 sure screening 理论对高维变量筛选的假设条件研究有参考价值。
- **关键技术**: `sure independence screening`, `minimum density power divergence`, `ultra-high-dimensional GLM`, `uniform consistency`, `robust conditional screening`
- **为什么对您有用**: 涉及您 primary interest 中的高维统计（超高频变量筛选），其 nonpolynomial 维度下的 sure screening 理论和均匀一致性证明可为高维筛选的假设条件与理论边界提供参考。

### 3. [10.1111/sjos.12616](https://doi.org/10.1111/sjos.12616) — Inference for low‐ and high‐dimensional inhomogeneous Gibbs point processes
- **作者**: Ismaïla Ba, Jean‐François Coeurjolly
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 993-1021
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究非均匀 Gibbs 点过程（GPP）在低维和高维设定下的统计推断，目标是在协变量维度随观测区域发散时估计空间点过程的相互作用与回归参数。作者提出基于凸和非凸惩罚函数的正则化复合伪似然方法。在空间 GPP 依赖结构与惩罚函数的正则条件下，证明了估计量的 oracle 性质、一致性与渐近正态性。该理论结果同时涵盖了低维情形，填补了 GPP 低维渐近理论的文献空白。模拟实验与热带林业数据应用验证了方法的有效性。对您有用：高维惩罚伪似然与 oracle 性质的证明框架可迁移至您关注的**高维统计**中其他复杂依赖数据（如时空/网络）的 M-估计推断。
- **关键技术**: `regularized composite likelihood`, `pseudo-likelihood estimation`, `oracle property`, `diverging dimensionality`, `Gibbs point process`
- **为什么对您有用**: 与您的高维统计（发散维度下的 oracle 性质）和数学统计（渐近正态性）兴趣相关，其针对复杂空间依赖结构的高维 M-估计推断技术可借鉴至其他高维半参数模型。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.12622](https://doi.org/10.1111/sjos.12622) — Bayesian inverse problems with heterogeneous variance
- **作者**: Natalia Bochkina, Jenovah Rodrigues
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1116-1151
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究 Hilbert 空间中带相关高斯噪声（fractional noise）的 mildly ill-posed 逆问题的 Bayes 正则化估计，目标是在 Sobolev 类上获得 posterior contraction rate 并与 minimax rate 对比。核心方法是一种新的 wavelet-based vaguelette–vaguelette 变换，使得在算子与协方差算子不同时对角化的情形下仍可使用序列空间方法，推广了传统 vaguelette-wavelet 框架。理论结果包括：(1) 在更一般的基与协方差算子下证明 posterior contraction rate；(2) 将方差的一致估计量 plug-in 到序列空间后，证明 contraction rate 不受影响，并将此结果应用于 forward operator 有误差的情形；(3) 证明 empirical Bayes posterior（plug-in 最大边际似然估计先验尺度）以 minimax 意义下的最优 rate 自适应收缩。对您而言，该文在非参数 Bayes 自适应 minimax 理论与 plug-in 估计对 posterior contraction 影响的分析上，与 semiparametric/nonparametric theory 及 efficiency theory 的兴趣直接相关，vaguelette–vaguelette 技巧也可为高维/无穷维正则化问题提供计算与理论工具。
- **关键技术**: `vaguelette-vaguelette transform`, `posterior contraction rate`, `minimax adaptive estimation`, `empirical Bayes with plug-in MML`, `Sobolev class`, `fractional Gaussian noise`
- **为什么对您有用**: 与您 primary interest 中的 semiparametric/nonparametric theory 和 efficiency theory 直接相关：文章给出了 adaptive minimax posterior contraction rate 的完整理论，且 plug-in 估计对 Bayes posterior 影响的分析思路可迁移到 semiparametric efficiency 与 debiased ML 中 nuisance parameter 估计的类似问题。

### 2. [10.1111/sjos.12665](https://doi.org/10.1111/sjos.12665) — Outlier detection based on extreme value theory and applications
- **作者**: Shrijita Bhattacharya, Francois Kamper, Jan Beirlant
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1466-1502
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 本文研究基于极值理论（EVT）的异常值检测问题，设定为在未知分布所属的极大值吸引域（max-domain of attraction）下的非参数框架。作者将先前仅适用于重尾 Pareto 型分布的异常检测算法推广至所有极大值吸引域，提出了一种数据驱动的自动检测方法。核心技术工具包括极值理论的域吸引条件与尾部指数估计，并基于此构造了尾部调整的箱线图以及结合局部异常因子（LOF）的多变量异常检测程序。仿真与实例表明该算法在有限样本下能有效识别偏离中间与尾部特征的异常点。对您而言，虽然核心在极值统计而非因果或高维，但其将特定尾部假设放松至全域的非参数推广思路，对非参数理论中假设条件的弱化具有参考价值。
- **关键技术**: `extreme value theory`, `max-domains of attraction`, `tail index estimation`, `local outlier factors`, `tail-adjusted boxplot`
- **为什么对您有用**: 涉及非参数极值理论与假设条件（尾部特征）的弱化推广，虽非因果推断或高维效率理论，但其从特定 Pareto 尾部到全域的非参数拓展思路对您关注的非参数理论有一定参考价值。

### 3. [10.1111/sjos.12642](https://doi.org/10.1111/sjos.12642) — Asymptotic properties of the maximum smoothed partial likelihood estimator in the change‐plane Cox model
- **作者**: Shota Takeishi
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1503-1531
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在 change-plane Cox 模型（用于生存数据亚组分析）下，本文研究有限维参数估计量的渐近性质，重点解决多协变量分类下收敛率与渐近分布未知的理论空白。作者提出了最大平滑偏似然估计量，通过引入平滑技术与调谐参数克服了传统 change-plane 目标函数的非凸或不连续问题。在协变量分布与调谐参数的特定条件下，证明了分类参数的收敛率可任意接近 n^{-1/2}（至多差对数因子）。基于该收敛率结果，进一步推导出回归参数的渐近正态性。该研究填补了多变量 change-plane 模型的渐近理论空白，对您在半参数理论中处理非标准收敛率及渐近正态性推导有直接参考价值。
- **关键技术**: `change-plane model`, `smoothed partial likelihood`, `convergence rate`, `asymptotic normality`, `Cox proportional hazards`
- **为什么对您有用**: 直接关联您的 semiparametric theory 兴趣，提供了 change-plane 这类非规则参数模型下收敛率逼近 n^{-1/2} 的严格推导，对处理类似非标准半参数收敛率与渐近分布问题有借鉴意义。

### 4. [10.1111/sjos.12635](https://doi.org/10.1111/sjos.12635) — A new reproducing kernel‐based nonlinear dimension reduction method for survival data
- **作者**: Wenquan Cui, Jianjun Xu, Yuehua Wu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1365-1390
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 针对右删失生存数据的非线性降维问题，本文在切片逆回归(SIR)与再生核希尔伯特空间(RKHS)框架下提出了 RDSIR 方法。利用 RKHS 的等距同构性质，将非线性函数表示为同构特征空间中元素的内积；针对删失偏倚，采用双重切片(double slicing)估计权重函数进行校正。非线性充分降维(SDR)子空间通过广义特征分解问题求解，并基于矩阵扰动理论建立了估计量的渐近性质。数值实验表明 RDSIR 在提取非线性特征方面优于线性 SDR 且对删失稳健。对您有用之处：本文展示了 RKHS 与渐近扰动理论在非参数降维中的结合，属于您关注的 semiparametric/nonparametric theory 范畴，但未涉及半参数效率界或因果推断。
- **关键技术**: `sliced inverse regression (SIR)`, `reproducing kernel Hilbert space (RKHS)`, `double slicing`, `generalized eigen-decomposition`, `perturbation theory`
- **为什么对您有用**: 涉及非参数理论(RKHS)与渐近性质(扰动理论)，属于您 primary interest 中的 semiparametric/nonparametric theory 范畴，但其侧重降维而非效率界或因果推断，仅作方法扩展参考。

### 5. [10.1111/sjos.12606](https://doi.org/10.1111/sjos.12606) — Sparse concordance‐based ordinal classification
- **作者**: Yiwei Fan, Jiaqi Gu, Guosheng Yin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 934-961
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在有序分类设定下，目标是正确预测实例的相对顺序，本文引入 concordance 函数并采用带惩罚的平滑优化方法实现变量选择。在最大化 concordance 函数的分类规则集中，通过最小化损失函数寻找最优阈值，并推导类别条件概率的非参数估计。理论方面，建立了非参数估计量的渐近性质及变量选择相合性。仿真与实际数据表明该方法在分类精度上具有稳健性和优势。对您可能有用：其非参数估计的渐近理论及高维稀疏惩罚下的变量选择相合性证明，可为有序/离散数据下的半参数/非参数推断提供参考。
- **关键技术**: `concordance function`, `penalized smoothed optimization`, `variable selection consistency`, `nonparametric conditional probability estimation`, `ordinal classification`
- **为什么对您有用**: 涉及非参数估计的渐近性质与高维稀疏设定下的变量选择相合性，与您在非参数/半参数理论及高维统计方面的兴趣有一定交叉，可借鉴其有序数据下的理论分析技巧。

## 效率理论 / Debiased ML  *(efficiency_dml, 4 篇)*

### 1. [10.1111/sjos.12657](https://doi.org/10.1111/sjos.12657) — Errata for “A framework for covariate balance using Bregman distances”
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1552-1552
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是“A framework for covariate balance using Bregman distances”的勘误，涉及三处修正。第一处修正了在线附录中证明所瞄准的 semiparametric efficiency bound 的对齐问题；第二处删除了方程(26)右侧第二约束中多余的 qi；第三处澄清了 Section 5.2 中 hdCBPS 的描述，改为“CBPS 的增广版本，通过正则化回归技术获得 potential outcome means 的 debiased 估计”。勘误本身无方法学创新，但原文涉及 Bregman 距离下的协变量平衡框架与高维 debiased 估计，对您关注的高维因果推断中 debiased ML 与效率理论有背景关联。
- **关键技术**: `Bregman distance covariate balance`, `CBPS`, `debiased estimation of potential outcome means`, `regularized regression`, `semiparametric efficiency bound`
- **为什么对您有用**: 勘误本身价值有限，但原文框架连接了您 primary interest 中的效率理论（semiparametric efficiency bound）与高维 debiased 估计，若您此前追踪过该文则需注意修正。

### 2. [10.1111/sjos.12644](https://doi.org/10.1111/sjos.12644) — Targeted estimation of state occupation probabilities for the non‐Markov illness‐death model
- **作者**: Anders Munch, Marie Skov Breum, Torben Martinussen, Thomas A. Gerds
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1532-1551
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在连续时间非 Markov 疾病-死亡模型下，目标是在 coarsening at random 假设下估计状态占据概率，且不对转移强度函数施加参数形式限制。基于半参数效率理论推导出一类目标估计量，并证明在关于强度函数估计量的较弱条件下，该类估计量具有渐近线性性。这些条件弱到足以允许使用 data-adaptive 方法估计强度函数，从而在保证 n^{-1/2}-CAN 的同时缓解模型误设风险。具体实现上，提出基于惩罚 Poisson 回归的灵活方法来估计转移强度函数作为 nuisance 参数。模拟和真实流行病学数据应用验证了方法的有效性。对您有用：该文将半参数效率理论与多状态/纵向生存模型结合，展示了如何在允许 data-adaptive nuisance 估计的同时保持渐近有效性，直接契合您对 efficiency theory 与 longitudinal CI 的兴趣。
- **关键技术**: `semiparametric efficiency theory`, `illness-death model`, `asymptotically linear estimator`, `data-adaptive nuisance estimation`, `penalized Poisson regression`, `coarsening at random`
- **为什么对您有用**: 直接应用半参数效率理论推导多状态模型（纵向因果推断常见设定）的估计量，且允许 data-adaptive nuisance 估计以实现类似 debiased ML 式的稳健推断，完美契合您对 efficiency theory 与 longitudinal CI 的核心兴趣。

### 3. [10.1111/sjos.12634](https://doi.org/10.1111/sjos.12634) — Frequentist model averaging for envelope models
- **作者**: Ziwen Gao, Jiahui Zou, Xinyu Zhang, Yanyuan Ma
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1325-1364
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在多元线性回归的 envelope 模型设定下，本文旨在解决 envelope 维度选择不确定导致的估计效率损失问题，假设候选模型集合可能存在误设或正确设定。作者提出一种基于最小化 cross-validation 准则的 frequentist model averaging (FMA) 方法来组合多个候选 envelope 模型。理论上，当所有候选模型均误设时，证明了该 FMA 估计量具有渐近最优性（asymptotic optimality）；当存在正确候选模型时，证明了系数估计的一致性，且分配给正确模型的权重之和依概率收敛到1。Envelope 模型本身通过分离物质与非物质变异来达到更低的渐近方差，而 FMA 进一步在模型不确定性下保障了预测与估计的稳健性。对您有用：Envelope 估计本质上是追求参数效率的降维方法，与您 primary interest 中的 efficiency theory（渐近效率提升）紧密相连，其 FMA 渐近最优性证明也契合 mathematical statistics 的兴趣。
- **关键技术**: `frequentist model averaging`, `envelope model`, `cross-validation criterion`, `asymptotic optimality`, `multivariate linear regression`
- **为什么对您有用**: Envelope 模型通过剥离无关变异实现参数估计的渐近效率提升，直接关联您 primary interest 中的 efficiency theory；其 model averaging 的渐近最优性与权重一致性证明也契合 mathematical statistics 兴趣。

### 4. [10.1111/sjos.12626](https://doi.org/10.1111/sjos.12626) — Robust quasi‐randomization‐based estimation with ensemble learning for missing data
- **作者**: Danhyang Lee, Li‐Chun Zhang, Sixia Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1263-1278
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 在缺失数据设定下，现有 doubly robust (DR) 和 multiply robust (MR) 估计量仍依赖 outcome 模型或 response probability 模型的部分正确设定。本文提出基于 quasi-randomization 的鲁棒估计方法，允许对 outcome 变量使用任意多个半参数、非参数或机器学习工作模型（ensemble），在 cell-homogenous response 假设下，通过 subsampling Rao–Blackwell 方法消除 outcome 工作模型误设带来的偏差，实现无条件无偏性。同时给出了无需 jackknife/bootstrap 的无偏方差估计公式。模拟显示该方法在模型误设场景下优于现有 MR 估计量。对您有用：该工作将 DR/MR 鲁棒性框架推向更弱的假设条件，且 subsampling Rao-Blackwell 技巧与您关注的 semiparametric efficiency 及 debiased ML 中的 orthogonal score 思路有直接对话空间。
- **关键技术**: `doubly robust estimation`, `multiply robust estimation`, `Rao-Blackwell subsampling`, `quasi-randomization`, `ensemble working models`, `cell-homogenous response`
- **为什么对您有用**: 直接推进 DR/MR 鲁棒估计理论，与您 primary interest 中的 semiparametric efficiency bounds 和 debiased ML 的 orthogonal 思路高度相关；subsampling Rao-Blackwell 消偏机制可迁移至 causal inference 中 treatment effect 估计的模型误设保护。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1111/sjos.12648](https://doi.org/10.1111/sjos.12648) — Statistical evidence and surprise unified under possibility theory
- **作者**: David R. Bickel
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 923-928
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在假设检验框架下，将 Sander Greenland 提出的 surprisal（-log2(p)）推广至复合假设，提出基于可能性理论（possibility theory）的 surprise 概念，以量化拒绝假设所需的比特数。Surprisal 仅是假设空间中点的函数，而 surprise 扩展为假设空间子集的函数，满足条件极小-加概率（conditional min-plus probability）公理。通过这一公理体系，surprise 继承了可能性理论中的丰富工具，其等价的兼容性函数（compatibility function）可用于调整先验信息的 p 值及比较科学理论。该框架将点假设的 surprisal 与复合假设的 surprise 统一在非可加测度理论下，为重复性危机和证据量化提供了新视角。对您可能有用：如果您对假设检验中 p 值的信息论解释与可能性理论（非可加概率）的数学结构感兴趣，此文提供了一个简明的理论统一视角。
- **关键技术**: `surprisal (information-theoretic p-value)`, `possibility theory`, `conditional min-plus probability`, `compatibility function`, `composite hypothesis testing`
- **为什么对您有用**: 涉及您 primary interest 中的假设检验，特别是 p 值的信息论解释与可能性理论（非可加测度）的数学公理化，可为您在检验证据量化方面提供不同于经典 Neyman-Pearson 或 Bayes 的理论视角。

### 2. [10.1111/sjos.12629](https://doi.org/10.1111/sjos.12629) — Transform orders and stochastic monotonicity of statistical functionals
- **作者**: Tommaso Lando, Idir Arab, Paulo Eduardo Oliveira
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1183-1200
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究统计泛函在有限样本下的随机单调性，旨在为检验和置信区间等推断问题提供超越大样本渐近性质的随机行为刻画。作者引入了“变换序”（transform orders）这一广义随机序族，证明其能将经典随机序作为特例统一，从而为推导不同泛函的随机单调性提供灵活框架。该框架被应用于广义熵、基尼系数等不平等测度，证明了其关于样本量的随机单调性。在拟合优度检验中，利用该理论确定了最不利分布并分析了 Bootstrap 统计量的随机行为。对您可能有用：若您关注假设检验中泛函的有限样本行为或经济统计中的不平等指标推断，此框架提供了基于随机序的严格分析工具。
- **关键技术**: `stochastic orders`, `transform orders`, `statistical functionals`, `goodness-of-fit testing`, `least favorable distribution`, `bootstrap statistics`
- **为什么对您有用**: 与您在数学统计（假设检验）和经济理论（不平等测度）的兴趣相关；提供了分析统计泛函有限样本随机行为的随机序工具，对研究检验的最不利分布和 Bootstrap 行为有参考价值。

### 3. [10.1111/sjos.12617](https://doi.org/10.1111/sjos.12617) — Consistent Bayesian information criterion based on a mixture prior for possibly high‐dimensional multivariate linear regression models
- **作者**: Haruki Kono, Tatsuya Kubokawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1022-1047
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在可能高维的多变量线性回归模型中，本文研究变量选择问题，目标是在大样本与高维渐近框架下实现选择一致性。作者基于混合先验（光滑分布与 delta 分布的混合）推导了新的贝叶斯信息准则，该准则可视为 AIC 与 BIC 的融合。通过继承 AIC 和 BIC 的渐近性质，所提准则在 p 固定 n 趋向无穷及 p 趋向无穷的高维设定下均证明了变量选择的一致性。核心技术依赖于混合先验下的边际似然展开与渐近阶的精细分析。数值模拟表明，基于该信息准则的方法在多数情况下能以高概率选出真实变量集。对您有用：该文将高维变量选择的一致性理论扩展至多变量回归，其渐近分析手法对您在假设检验与高维统计中的模型选择研究有参考价值。
- **关键技术**: `mixture prior`, `Bayesian information criterion`, `variable selection consistency`, `high-dimensional asymptotics`, `marginal likelihood expansion`
- **为什么对您有用**: 论文处理高维多变量回归的变量选择一致性问题，属于高维统计与假设检验（模型选择）的交叉，其基于混合先验的边际似然渐近分析对您研究高维模型推断与假设检验有参考价值。

### 4. [10.1111/sjos.12607](https://doi.org/10.1111/sjos.12607) — Sequential monitoring of high‐dimensional time series
- **作者**: Rostyslav Bodnar, Taras Bodnar, Wolfgang Schmid
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 962-992
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究高维时间序列的序贯监控问题，在协方差矩阵逆矩阵难以估计或不存在的高维设定下，构建新的多元 EWMA 控制图。提出基于欧氏距离和方差加权距离（对角方差矩阵的逆）的 EWMA 控制统计量，避免了传统基于马氏距离的方法中计算高维逆协方差矩阵的难题。推导了这些控制统计量的精确分布性质，并据此确定了控制限。通过大量模拟研究，将新方法与基于马氏距离的多元 EWMA 控制图进行了比较。结果表明新方法在高维设定下不仅计算可行，且具有良好的监控表现。对您有用：该文处理高维协方差矩阵逆不可求的思路，以及序贯监控中的分布推导，对您在高维假设检验与统计计算方向的研究有直接参考价值。
- **关键技术**: `multivariate EWMA control chart`, `high-dimensional covariance matrix`, `Euclidean distance`, `sequential monitoring`, `distributional properties`
- **为什么对您有用**: 直接涉及高维设定下避免逆协方差矩阵的假设检验（序贯监控）问题，对您的高维统计与假设检验兴趣有参考价值，提供了绕过高维逆矩阵计算的具体方案与分布推导。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12637](https://doi.org/10.1111/sjos.12637) — Daisee: Adaptive importance sampling by balancing exploration and exploitation
- **作者**: Xiaoyu Lu, Tom Rainforth, Yee Whye Teh
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1298-1324
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文将自适应重要性抽样（AIS）建模为在线学习问题，强调探索-利用权衡在自适应过程中的关键作用。基于在线学习文献的思想，提出基于空间划分的 AIS 算法 Daisee，并引入 AIS 的 regret 概念，证明其累积伪 regret 上界为 O(√T)（T 为迭代次数）。进一步将 Daisee 扩展为自适应学习样本空间层次划分的版本，以提升抽样效率。实验验证了两种算法的数值表现。对您而言，该文将在线学习 regret 分析引入 Monte Carlo 计算的思路，可为统计计算中自适应算法设计提供理论分析工具参考。
- **关键技术**: `adaptive importance sampling`, `online learning regret`, `partition-based sampling`, `hierarchical partitioning`, `exploration-exploitation trade-off`
- **为什么对您有用**: 属于您 primary interest 中统计计算方向；将在线学习 regret 理论引入 Monte Carlo 抽样算法设计，提供了自适应数值方法的理论分析新范式，可迁移至因果推断中 likelihood/IPW 的自适应计算场景。

### 2. [10.1111/sjos.12636](https://doi.org/10.1111/sjos.12636) — Spatial bootstrapped microeconometrics: Forecasting for out‐of‐sample geo‐locations in big data
- **作者**: Katarzyna Kopczewska
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1391-1419
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在大样本空间计量模型中，由于空间权重矩阵 W 仅针对样本内观测定义且计算复杂度高，对样本外新地理位置的预测面临计算瓶颈与推断失效问题。本文提出基于 bootstrap 与空间镶嵌（tessellation/Voronoi 多边形）的联合校准方法：通过 bootstrap 抽样估计子模型，并利用 PAM（Partitioning Around Medoids）算法对回归系数进行联合非独立聚类以选择最优模型。随后基于最优模型中的地理点构建 Voronoi 多边形，将样本外新点映射至对应镶嵌区块并关联至 W 矩阵，从而实现样本外空间预测。该方法在预测精度与计算效率之间无需权衡，并在企业选址与盈利的微观实证数据中验证了有效性。对您而言，该文处理大样本空间权重矩阵计算瓶颈的算法思路（Voronoi 镶嵌与 PAM 聚类）可迁移至统计计算中大规模矩阵运算的优化，同时其微观经济学数据集对经济理论应用有参考价值。
- **关键技术**: `spatial weights matrix`, `bootstrap resampling`, `Voronoi tessellation`, `Partitioning Around Medoids (PAM)`, `out-of-sample spatial prediction`
- **为什么对您有用**: 连接到您的统计计算（大规模矩阵/算法优化）与经济理论（微观计量数据集）兴趣：其通过 Voronoi 镶嵌与 PAM 聚类解决空间权重矩阵 W 的计算与样本外推断瓶颈的算法设计，为处理大样本空间相关数据的计算问题提供了可迁移的思路。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1111/sjos.12615](https://doi.org/10.1111/sjos.12615) — Generalizing the information content for stepped wedge designs: A marginal modeling approach
- **作者**: Fan Li, Jessica Kasza, Elizabeth L. Turner, Paul J. Rathouz, Andrew B. Forbes, John S. Preisser
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1048-1067
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在阶梯楔形（stepped wedge）集群随机试验中，当资源限制导致不完全设计（省略某些 cell/sequence/period）时，如何量化信息损失是核心问题。本文将信息含量（information content）指标从连续结局推广到离散结局，在边际模型框架下采用一般 link 和 variance 函数推导了省略数据元素后的信息含量解析表达式。证明了在使用方差稳定化 link 函数时，离散结局的信息含量仍可保持中心对称（centrosymmetric）模式。数值研究表明，在 canonical link 下 cell 层面的信息含量近似中心对称，但 sequence 和 period 层面的模式对时间趋势（secular trend）更敏感，可能严重偏离中心对称。对您而言，信息含量分析思路可迁移至纵向因果推断中处理不完整随访的设计效率评估，但本文主要贡献在试验设计层面而非半参数效率界或估计理论。
- **关键技术**: `information content metric`, `marginal model with general link`, `stepped wedge incomplete design`, `centrosymmetric pattern`, `variance-stabilizing link function`
- **为什么对您有用**: 信息含量与效率理论有概念联系，阶梯楔形设计属于纵向流行病学试验；但本文聚焦设计优化而非半参数效率界或因果识别，对您 primary interest 的直接推进有限，更适合作为流行病学应用背景阅读。

## 其他  *(other, 5 篇)*

### 1. [10.1111/sjos.12640](https://doi.org/10.1111/sjos.12640) — Multivariate geometric anisotropic Cox processes
- **作者**: James S. Martin, David J. Murrell, Sofia C. Olhede
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1420-1465
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文提出了一种多元几何各向异性Cox过程的建模与推断框架，旨在刻画空间点过程中多变量及方向依赖的结构。基于多元空间统计的近期进展，作者构建了一类新的多元各向异性随机场，并由此导出各向异性点过程，同时给出了保证模型有效性的数学条件。针对Cox过程似然函数不可解的问题，提出了基于Palm似然的推断方法以绕过计算瓶颈。实证部分利用Barro Colorado Island的植物与树木空间生态数据展示了该框架的实用性。该文属于空间点过程领域，与您关注的高维/半参数/因果推断等核心方向交集较小，但Palm似然作为替代推断工具的思路对处理复杂似然问题有微弱参考价值。
- **关键技术**: `Cox process`, `anisotropic random fields`, `Palm likelihood`, `spatial point processes`
- **为什么对您有用**: 本文主要属于空间点过程与生态统计，与您的高维统计、因果推断及半参数理论等核心兴趣交集较小，仅Palm似然推断方法对处理不可解似然问题有微弱参考。

### 2. [10.1111/sjos.12630](https://doi.org/10.1111/sjos.12630) — Longitudinal network models and permutation‐uniform Markov chains
- **作者**: William K. Schwartz, Sonja Petrović, Hemanshu Kaul
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1201-1231
- 相关性 0/10
- **摘要**: {
  "topic": "stat_computing",
  "summary_zh": "在纵向网络设定下，假设边状态按具有指数族转移概率的离散时间马尔可夫链演化，目标是刻画其联合分布并简化推断。作者证明了在何种条件下该链的联合分布也是同参数的指数族，从而实现数据降维；并引入"置换均匀"（permutation-uniform）子类，使其可视为独立同分布序列。将此框架应用于时序指数随机图模型（TERGM），讨论了均值参数收敛与可交换性，并为部分模型导出了闭式极大似然估计（MLE）。该框架简化了现有自回归网络模型的渐近分析，对您在统计计算（闭式 MLE 简化数值算法）和数理统计（指数族马尔可夫链理论）方面的兴趣有参考价值。",
  "key_techniques": [
    "exponential family",
    "discrete-time Markov chain",
    "permutation-uniform",
    "temporal ERGM",
    "closed-form MLE",
    "data reduction"
  ],
  "why_relevant": "本文属于数理统计与统计计算范畴，其关于指数族马尔可夫链联合分布的刻画和闭式 MLE 的推导，对您在统计计算（数值求解简化）和数理统计（指数族渐近性）方面的兴趣有直接

### 3. [10.1111/sjos.12627](https://doi.org/10.1111/sjos.12627) — Posterior consistency for the spectral density of non‐Gaussian stationary time series
- **作者**: Yifu Tang, Claudia Kirch, Jeong Eun Lee, Renate Meyer
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1152-1182
- 相关性 0/10
- **摘要**: {
  "topic": "nonparam_semipara",
  "summary_zh": "本文研究非高斯平稳时间序列谱密度的贝叶斯非参数估计后验一致性问题，设定为依赖数据下误设模型的一般框架。先前文献基于 Whittle 似然近似与 Bernstein–Dirichlet 过程先验，仅在高斯序列下证明了后验一致性；本文通过引入依赖数据与误设模型下的一般一致性定理，将结论推广至非高斯情形，同时 Whittle 似然下的后验一致性也作为特例被推广。核心技术工具包括 Bernstein–Dirichlet 过程先验的支撑性质、Whittle 似然的非参数修正、以及依赖数据经验过程的相关收敛论证。模拟部分用若干非高斯时间序列示例展示了小样本性质。对您而言，这是非参数理论中"放松分布假设（高斯→非高斯）"的一个干净范例，误设模型下后验一致性的论证思路可迁移到您关注的半参数效率与弱假设推断问题中。",
  "key_techniques": [
    "Bernstein-Dirichlet process prior",
    "Whittle likelihood approximation",
    "posterior consistency under misspecification",
    "spectral density estimation",

### 4. [10.1111/sjos.12620](https://doi.org/10.1111/sjos.12620) — Distributed inference for two‐sample <i>U</i>‐statistics in massive data analysis
- **作者**: Bingyao Huang, Yanyan Liu, Liuhua Peng
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1090-1115
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究海量数据下两样本 U-统计量的分布式推断问题，设定为数据分块存储在不同节点上的分布式计算环境。为降低计算与通信开销，作者提出了分布式两样本 U-统计量与分块线性两样本 U-统计量，并建立了两者的渐近性质。针对非退化与退化两种情形，文章提出了基于分布式加权自助法的分布逼近算法，其中针对分布式两样本 U-统计量的加权自助法在现有文献中系首次提出。该自助法程序计算高效且具备严格的理论保证，数值实验验证了方法的有效性。对您有用：直接推进了您关注的 higher-order U-statistics 在分布式计算场景下的推断方法，其退化情形的处理与分布式自助法设计对研究复杂 U-统计量的假设检验具有迁移价值。
- **关键技术**: `distributed two-sample U-statistics`, `blockwise linear U-statistic`, `distributed weighted bootstrap`, `degenerate U-statistics`, `asymptotic properties`
- **为什么对您有用**: 直接对应您 primary interest 中的 higher-order U-statistics 与 statistical computing；退化情形的分布式自助法为海量数据下基于 U-统计量的假设检验提供了新工具。

### 5. [10.1111/sjos.12619](https://doi.org/10.1111/sjos.12619) — State estimation for aoristic models
- **作者**: Maria N. M. van Lieshout, Robin L. Markwitz
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1068-1089
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文研究 aoristic 数据的状态估计问题：时间标记点过程中事件点不可直接观测，仅知其落在可观测区间（标记）内。在标记由平衡交替更新过程建模、先验为 Markov 点过程的贝叶斯设定下，推导了潜在事件点的后验分布及其参数估计。数值示例展示了先验选择对后验推断的影响，实证应用于区间审查犯罪事件的发生时间估计。方法学 novelty 有限，属于特定点过程模型的贝叶斯后验推导，未涉及半参数效率或收敛率优化。区间审查概念虽在流行病学队列中常见，但本文的 Markov 点过程先验 + 交替更新过程框架与您关注的因果推断/半参数效率工具链重叠有限，阅读收益偏低。
- **关键技术**: `alternating renewal process`, `Markov point process prior`, `Bayesian state estimation`, `interval censoring`, `posterior parameter estimation`
- **为什么对您有用**: 区间审查（interval censoring）在流行病学队列研究中常见，但本文方法（Markov 点过程先验 + 交替更新过程）与您关注的因果推断/半参数效率/高维推断工具链重叠有限，阅读收益偏低。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

