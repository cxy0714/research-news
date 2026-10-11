# Scand. J. Stat. — Vol 53  Issue 3  ·  2026-10-10

- 共 18 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 未见遗漏（对照 OpenAlex 17 篇，权威目录可能尚未完全收录本期）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期《Scand. J. Stat.》18 篇论文可大致归为四条主线：**因果推断与删失数据**（3 篇）、**高维变量选择与分组回归**（3 篇）、**半参数与非参数推断**（4 篇，含测量误差、单调密度、经验似然）、**统计计算与随机过程**（其余 7 篇，涵盖子抽样、数值积分、动态网络、SDE 等）。其中因果与删失、高维选择两条主线最为突出，且与半参数效率、假设检验有交叉。

因果推断主线中，三篇论文分别从不同角度处理**无真实标签或删失结局下的估计与推断**。`A Semiparametric Approach for Robust Modeling of Electronic Health Record Linked Biobank Data` 针对 EHR 关联数据中疾病结局有误分类的设定，提出两步法——先做复合非参数回归，再通过参数投影降方差，在无真实结局标签下达到根号 n 收敛，属于测量误差框架下的稳健风险建模。`A Doubly Robust Learner for Regression and Inference With Right‐Censored Outcomes` 将 DR-learner 推广至右删失结局，通过构造删失无偏变换生成伪结局，并给出条件偏差的新表示，从而建立率双稳健性与 oracle 效率，与因果推断中的交叉拟合技术直接衔接。`Bayesian Estimation of Transition Rates in Two‐State Nonhomogeneous Markov Jump Processes With Intermittent Observations` 则从纵向状态转移角度，用“诚实时间”数据增广处理间歇观测下的非齐次马尔可夫跳变过程，为删失或缺失数据下的动态系统推断提供了贝叶斯计算工具。

高维变量选择主线中，`Sparse Generalized Factor Models With Weaker Loadings` 在弱载荷条件下用组惩罚实现稀疏载荷估计，并开发投影交替最大化算法与稀疏信息准则，同时给出载荷矩阵和因子得分的收敛速率；`Group Regression With Tailored Penalties for High‐Dimensional Data With or Without Predefined Groups` 则允许不同组使用不同惩罚类型，并推导了组惩罚估计量的精确分布以支持统计推断，与高维假设检验直接相关；`Sparse Minimum Redundancy Maximum Relevance for Feature Selection` 结合非凸正则与 knockoff filter 实现 FDR 控制下的特征筛选，属于高维变量选择与多重检验的交叉。此外，`Automatic Variable Selection for Longitudinal Quantile Regression` 虽归入因果类，但其 QIF 与平滑阈值估计方程的结合也涉及高维纵向数据的选择一致性，可视为该主线的延伸。

半参数与非参数主线中，`Generalized Empirical Likelihood for Partially Linear Errors‐in‐Variables Regression Model With Longitudinal Data` 在纵向测量误差下构造经验似然比统计量并证明卡方极限，与半参数效率理论紧密相关；`Bayesian Inference for Multivariate Monotone Densities` 通过 L2 投影将无约束后验映射到单调密度空间，证明最优收缩速率并构造贝叶斯检验，属于非参数贝叶斯与检验的交叉。其余如 `Maximum Spacing Estimation for Multivariate Observations` 的模型误设检测工具、`A Modified Random Survival Forest` 对 case-cohort 设计的重抽样改进，也分别与假设检验和删失数据预测相关。

若按主题优先阅读：因果推断与删失数据方向可先看 `A Doubly Robust Learner` 和 `A Semiparametric Approach`；半参数效率与测量误差方向可看 `Generalized Empirical Likelihood` 和 `Bayesian Inference for Multivariate Monotone Densities`；高维选择与推断方向可看 `Group Regression With Tailored Penalties` 和 `Sparse Minimum Redundancy Maximum Relevance`。

## 因果推断  *(causal_inference, 4 篇)*

### 1. [10.1111/sjos.70082](https://doi.org/10.1111/sjos.70082) — A Semiparametric Approach for Robust Modeling of Electronic Health Record Linked Biobank Data
- **作者**: Molei Liu, Xinyi Wang, Chuan Hong
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Peking University · University of California, Berkeley · Duke University
- **分类**: vol 53 · issue 3 · pp 1279-1298
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对电子健康记录（EHR）关联生物样本库数据中的表型分类与疾病风险建模问题，提出一种无监督半参数方法。在真实疾病结局不可观测、仅有多个有误分类的EHR替代结局以及少量可能也有误的图表审核标签的设定下，目标是对基线生物标志物进行风险建模（估计疾病风险函数），同时构建EHR表型预测模型并评估其性能。方法分为两步：先进行复合非参数回归（无需参数模型假设），再通过参数投影步骤降低估计量方差。理论证明该方法对参数假设的违背具有稳健性，同时风险建模估计量达到根号n收敛速度。模拟研究显示优于现有方法，并在2型糖尿病的表型与遗传风险建模实际应用中验证了有效性。对您而言，该方法属于无真实结局标签下的测量误差校正与半参数效率问题，与您的因果推断（测量误差、替代结局）及半参数理论兴趣直接相关。
- **关键技术**: `semiparametric estimation`, `composite nonparametric regression`, `parametric projection`, `measurement error correction`, `surrogate outcomes`, `EHR phenotyping`
- **为什么对您有用**: 该论文涉及因果推断中的测量误差与替代结局问题（无真实结局标签），并采用半参数方法实现根号n收敛，与您的半参数理论及因果推断兴趣直接相关。可用您非常熟悉的非参数统计和M估计理论来审视其投影步骤的效率损失，中期可尝试将方法推广到纵向或代理因果推断设定。

### 2. [10.1111/sjos.70076](https://doi.org/10.1111/sjos.70076) · [arXiv](https://arxiv.org/abs/2411.04909) — A Doubly Robust Learner for Regression and Inference With Right‐Censored Outcomes
- **作者**: O. L. Sandqvist
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Copenhagen · PFA Pension (Denmark)
- **分类**: vol 53 · issue 3 · pp 1176-1188
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在右删失结局下提出一个通用的双稳健非参数回归框架，将异质性处理效应中的 DR-learner 策略推广到删失数据设定。方法将删失无偏变换推广为生成伪结局，再作为第二阶段非参数回归的输入，并采用样本分割或交叉拟合。作者推导了这些伪结局条件偏差的新表示，该表示是建立估计量渐近性质的核心，包括率双稳健性和当第二阶段回归为线性光滑器时的 oracle 效率。模拟研究展示了良好的有限样本表现，并应用于右删失结局的断点回归设计以估计因果效应。对您而言，该方法与您熟悉的因果推断中的双稳健估计和交叉拟合技术直接相关，且其偏差表示可能为删失数据下的效率分析提供新视角。
- **关键技术**: `DR-learner`, `censoring unbiased transformation`, `pseudo-outcomes`, `cross-fitting`, `rate double robustness`, `oracle efficiency`, `regression discontinuity design`
- **为什么对您有用**: 本文属于因果推断中删失数据下的双稳健估计，直接连接您的 primary interest 中的 causal inference 和 efficiency theory。您可以用 very_familiar 的非参数统计和 minimax 理论来审视其率双稳健性是否最优，或探索其偏差表示在更复杂设定（如纵向数据）中的推广。中期可做：需在 moderately_familiar 的 semiparametric theory 上进一步巩固以深入理解 oracle 效率的证明。

### 3. [10.1111/sjos.70077](https://doi.org/10.1111/sjos.70077) — Automatic Variable Selection for Longitudinal Quantile Regression With Application to Alzheimer's Disease Progression
- **作者**: Indrabati Bhattacharya, Mohammad Alfrad Nobel Bhuiyan, Suneel Babu Chatla
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Florida State University · Louisiana State University Health Sciences Center Shreveport · The University of Texas at El Paso
- **分类**: vol 53 · issue 3 · pp 1189-1205
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对纵向数据中的分位数回归，提出了一种自动变量选择的新框架，目标是在存在组内相关性和协变量维数发散的情况下，同时实现估计和选择的一致性。方法结合了二次推断函数（QIF）与平滑阈值估计方程（SEEs），利用QIF处理纵向相关性，通过SEE实现自动变量选择，避免了传统惩罚方法的调参复杂性。作者建立了变量选择一致性，并证明可用BIC准则选择调参参数，理论结果覆盖了协变量维数随样本量增长的情形。模拟研究显示该方法在估计精度和选择可靠性上表现良好。最后，将该方法应用于阿尔茨海默病神经影像学倡议（ADNI）数据，识别出与极端认知衰退相关的生物标志物和风险因素。对您而言，本文的纵向分位数回归与变量选择结合思路，以及QIF处理相关性的技术，可能对您关注的纵向因果推断和流行病学应用有参考价值。
- **关键技术**: `quadratic inference function`, `smooth-threshold estimating equations`, `variable selection consistency`, `BIC tuning parameter selection`, `longitudinal quantile regression`
- **为什么对您有用**: 本文属于纵向数据中的分位数回归和变量选择，与您的因果推断（纵向）和流行病学应用兴趣相关。您可以用非常熟悉的非参数统计和估计理论来审视其估计方程的一致性证明，中期可尝试将QIF与您的HOIF或U统计量工具结合，以处理更复杂的相关性结构。

### 4. [10.1111/sjos.70087](https://doi.org/10.1111/sjos.70087) — Bayesian Estimation of Transition Rates in Two‐State Nonhomogeneous Markov Jump Processes With Intermittent Observations: An Honest‐Time Data‐Augmentation Approach
- **作者**: Dario Gasbarra, Sangita Kulathinal, Etienne Sebag
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Vaasa · University of Helsinki
- **分类**: vol 53 · issue 3 · pp 1343-1357
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究两状态非齐次马尔可夫跳变过程（MP）在间歇观测下的转移强度估计问题。由于非齐次过程的转移概率矩阵（TPM）通常无法用生成元的矩阵指数简单表示，直接构建似然函数存在困难。作者提出一种贝叶斯数据增广方法，通过引入两个独立的驱动泊松点过程产生的“诚实时间”来增广间歇观测，从而避免采样完整路径。该方法使得模型参数的采样变得可行，并给出了具体的MCMC算法。通过模拟研究和真实临床就诊数据（间歇时间网格）验证了方法的有效性。对您而言，该方法为纵向数据中状态转移过程的贝叶斯推断提供了一种计算技巧，与您因果推断中纵向设定下的估计问题相关。
- **关键技术**: `Bayesian data augmentation`, `Markov jump process`, `nonhomogeneous transition intensity`, `Poisson point process`, `MCMC`
- **为什么对您有用**: 本文属于纵向因果推断中状态过程建模的计算方法，连接您的causal inference（纵向）兴趣。您可用very_familiar的软件开发和M-estimation理论来复现或扩展该算法，例如将其嵌入因果推断的g-formula或mediation分析中。中期可做：需在moderately_familiar的identification theory上进一步理解非齐次过程的识别条件。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.70079](https://doi.org/10.1111/sjos.70079) — Sparse Generalized Factor Models With Weaker Loadings
- **作者**: Zhijing Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Beijing Normal University
- **分类**: vol 53 · issue 3 · pp 1230-1248
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究广义因子模型（generalized factor models）在弱载荷（weaker loadings）条件下的稀疏估计问题。目标是在高维数据降维的同时实现变量选择，并提升模型可解释性。作者提出一种组惩罚估计方法，得到稀疏载荷矩阵，并开发了投影交替最大化算法（projected alternating maximization）以同时进行参数估计和变量选择。针对因子数确定问题，提出了稀疏信息准则（sparsity information criterion）。在弱载荷假设及其他温和条件下，建立了参数估计的上下界误差，推导了载荷矩阵和因子得分的收敛速率，并证明了变量选择和因子数的一致性。模型还扩展至缺失数据情形，并给出了相应的理论保证。模拟和两个真实数据集验证了方法的有效性。
- **关键技术**: `group-wise penalized estimation`, `projected alternating maximization`, `sparsity information criterion`, `weak loadings assumption`, `upper and lower error bounds`
- **为什么对您有用**: 本文属于高维统计与因子模型交叉领域，与您的高维统计和随机矩阵理论兴趣相关，特别是弱载荷假设下的估计理论。您可以用 very_familiar 的 minimax bounds 技术来审视其上下界是否紧，或考虑将稀疏因子模型与您熟悉的 U-statistics 结合，探索新的估计方法。中期可做：需先熟悉广义因子模型的渐近理论。

### 2. [10.1111/sjos.70072](https://doi.org/10.1111/sjos.70072) — Group Regression With Tailored Penalties for High‐Dimensional Data With or Without Predefined Groups
- **作者**: Reza Drikvandi
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Durham University
- **分类**: vol 53 · issue 3 · pp 1081-1100
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对高维回归中协变量具有自然分组结构的情形，提出一个灵活的组回归框架，允许不同组使用不同类型的惩罚（如组lasso、组SCAD等），突破了传统方法“一刀切”的惩罚类型限制。同时，在未预先指定分组时，提出一种新的组相关学习方法来自动识别协变量分组。理论上，作者给出了估计误差和预测误差的上界及渐近速率，并推导了组惩罚估计量的精确分布以支持统计推断。方法通过R包HDGR实现。对于您而言，其精确分布结果与您在高维统计和假设检验方面的兴趣相关，但分组相关学习方法可能涉及较复杂的计算，需评估其可迁移性。
- **关键技术**: `group lasso`, `group SCAD`, `group correlation learning`, `oracle inequalities`, `exact distribution of penalized estimators`
- **为什么对您有用**: 本文属于高维回归与分组惩罚方法，与您的高维统计兴趣直接相关，但更偏向于惩罚回归而非随机矩阵理论。其精确分布结果可用于构造检验，但方法核心（分组相关学习）可能涉及非凸优化，与您的武器库（如U统计量、经验过程）有一定距离。初步判断：中期可做，需在优化或高维推断方面补充知识。

## 非参数 / 半参数  *(nonparam_semipara, 2 篇)*

### 1. [10.1111/sjos.70078](https://doi.org/10.1111/sjos.70078) · [arXiv](https://arxiv.org/abs/2306.05202) — Bayesian Inference for Multivariate Monotone Densities
- **作者**: Kang Wang, Subhashis Ghosal
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: The University of Texas MD Anderson Cancer Center · North Carolina State University
- **分类**: vol 53 · issue 3 · pp 1206-1229
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文考虑多元单调密度的非参数贝叶斯估计与检验问题。与传统直接对满足单调性约束的密度施加先验不同，作者通过分箱和 Dirichlet 分布对阶梯高度施加先验，得到共轭后验，但该后验不满足单调性。他们利用 L2 投影将任意分段常数密度映射到多元单调函数空间，并归一化，从而由无约束后验诱导出单调密度上的“投影后验”。作者证明该投影后验以最优速率收缩，并基于到单调函数类的 L2 距离构造了贝叶斯检验，其检验水平趋于零且对充分分离的备择具有高功效。此外，为获得内点密度值的贝叶斯可信区间，他们考虑函数值在特定块上优化后的诱导映射的后验分位数区间，并显式计算了极限覆盖概率，发现其超过构造时使用的可信水平；通过分析覆盖与可信的渐近关系，可精确实现期望的渐近覆盖。数值实验比较了与单调化传统密度估计器的精度，并分析了基因表达联合 p 值的真实数据集。对您而言，该文的投影后验与最优收缩率分析，可连接到您熟悉的非参数统计与 minimax 界工具，且其贝叶斯检验构造思路或可迁移至因果推断中的敏感性分析设定。
- **关键技术**: `Dirichlet prior`, `L2 projection`, `projection posterior`, `optimal contraction rate`, `Bayesian testing`, `credible interval coverage`
- **为什么对您有用**: 该文属于非参数贝叶斯与单调性约束估计，直接连接您的 primary interest 中的非参数与半参数理论；其投影后验收缩率分析可用您 very_familiar 的 minimax 界工具来验证或扩展；贝叶斯检验与可信区间覆盖的渐近分析也可能启发因果推断中敏感性分析的不确定性量化。

### 2. [10.1111/sjos.70075](https://doi.org/10.1111/sjos.70075) — Generalized Empirical Likelihood for Partially Linear Errors‐in‐Variables Regression Model With Longitudinal Data
- **作者**: Miaomiao Wang, Shunping Zheng, Xiaoqian Zheng, Xuejun Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Anhui University · Zhejiang Gongshang University
- **分类**: vol 53 · issue 3 · pp 1152-1175
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究纵向数据下部分线性测量误差模型（parametric 与 nonparametric 部分的协变量均含测量误差）的广义经验似然（GEL）推断。目标是对回归系数进行估计与置信区间构造，同时利用组内相关性提高效率，且无需直接估计相关矩阵中的 nuisance 参数。方法上，通过构造包含相关结构的估计方程，得到经验似然比统计量，并在正则条件下证明其渐近服从卡方分布，从而构建置信区间。进一步给出参数的 profile 经验似然比，并验证其卡方极限；同时证明非参数函数估计的强相合性与收敛速度，以及参数估计的根号 n 相合性。数值模拟与真实数据分析验证了所提方法的有限样本表现。对您而言，该文将经验似然与测量误差、纵向数据结合，其 profile 技巧与 nuisance 参数处理思路可迁移至您熟悉的 semiparametric 理论框架下的因果推断问题。
- **关键技术**: `generalized empirical likelihood`, `profile empirical likelihood`, `measurement error model`, `longitudinal data`, `within-group correlation`, `chi-square calibration`
- **为什么对您有用**: 该文属于 semiparametric 与非参数理论方向，具体涉及经验似然在测量误差和纵向数据下的推断，与您 primary interest 中的 semiparametric theory 和 hypothesis testing 直接相关。您可运用 very_familiar 的 nonparametric statistics 与 minimax bounds 工具，审视其非参数函数估计的收敛速度是否最优，或利用 moderately_familiar 的 semiparametric theory 分析其 profile 经验似然的效率损失。中期可做：若想将经验似然推广至更复杂的因果推断设定（如 proximal CI），需在 semiparametric efficiency 上进一步积累。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.70089](https://doi.org/10.1111/sjos.70089) — Maximum Spacing Estimation for Multivariate Observations Under a General Class of Information‐Type Measures for Misspecified Models
- **作者**: Han Bao, Kristi Kuljus, Bo Ranneby
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Tartu · Swedish University of Agricultural Sciences
- **分类**: vol 53 · issue 3 · pp 1358-1377
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究多元观测下最大间距（MSP）估计在模型误设下的行为，考虑一类由不同信息型散度（如 Kullback-Leibler 信息）导出的 MSP 估计量。作者证明在误设下 MSP 估计量收敛到依赖于所选散度的明确定义极限，从而建立相合性。通过模拟研究比较不同散度下 MSP 估计量的表现，并利用 MSP 估计量和间距函数的渐近性质提出在大样本中检测模型误设的工具。该工作将经典的一元 MSP 方法推广到多元且误设的情形，并统一了不同散度对应的估计框架。对您而言，其模型误设检测工具与您对假设检验和半参数理论的兴趣相关，且其渐近分析思路可借鉴到您熟悉的 M-估计框架中。
- **关键技术**: `maximum spacing estimation`, `divergence measures`, `model misspecification`, `consistency`, `asymptotic normality`, `goodness-of-fit testing`
- **为什么对您有用**: 本文属于假设检验与估计理论交叉方向，直接关联您对 hypothesis testing 和 semiparametric/nonparametric theory 的兴趣。其误设检测工具可视为一种 goodness-of-fit 检验，您可用 very_familiar 的 M-估计理论（如 influence function、渐近方差）来剖析其检验功效，或将其与您熟悉的 U-统计量方法结合，构造更高阶的检测统计量。中期可做：需在 moderately_familiar 的 semiparametric theory 上稍加巩固以处理其渐近效率分析。

### 2. [10.1111/sjos.70074](https://doi.org/10.1111/sjos.70074) · [arXiv](https://arxiv.org/abs/2508.18901) — Sparse Minimum Redundancy Maximum Relevance for Feature Selection
- **作者**: Peter Naylor, Benjamin Poignard, Héctor Climente‐González, Makoto Yamada
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 3 · pp 1134-1151
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出一种特征筛选方法，同时考虑特征间冗余与特征-目标相关性，通过带非凸正则的连续化 mRMR 过程识别不活跃特征，并建立零系数正确识别的条件以保证不活跃特征恢复的准确性。方法引入基于 knockoff filter 的多阶段流程，在控制 FDR 的同时丢弃不活跃特征，仅需设定 FDR 阈值而非指定保留特征数。模拟与真实数据实验表明，其性能与 HSIC-LASSO 相当，但所选特征更保守。该方法属于高维变量选择与假设检验的交叉领域，其 FDR 控制机制与您在高维统计和假设检验方面的兴趣直接相关。
- **关键技术**: `mRMR`, `non-convex regularization`, `knockoff filter`, `FDR control`, `feature screening`
- **为什么对您有用**: 本文属于高维特征选择与 FDR 控制，直接关联您的高维统计与假设检验兴趣。您可运用 very_familiar 中的 minimax bounds 分析其筛选过程的统计效率，或利用 moderately_familiar 的 M-estimation 理论验证其非凸正则估计的相合性。中期可做：若需深入 knockoff 构造的幂性质，需先加强 moderately_familiar 中的假设检验理论。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.70080](https://doi.org/10.1111/sjos.70080) — Optimal Poisson Subsampling for Multiplicative Regressions With Massive Data
- **作者**: Jiahui Zou, Jie he, Xiaomeng Yan, Xinyu Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Capital University of Economics and Business · Chinese Academy of Sciences · Academy of Mathematics and Systems Science
- **分类**: vol 53 · issue 3 · pp 1249-1278
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对大规模乘法回归（如股票价格、寿命等正响应数据）的参数估计计算负担问题，本文提出一种高效的 Poisson 子抽样方法。与有放回的最优子抽样不同，Poisson 子抽样避免了重复观测，从而提高了估计效率。作者基于 A- 和 L- 最优性准则推导了两种 oracle 最优子抽样概率，并给出了实用的实现算法及适应分布式计算的版本。理论上，他们证明了子抽样参数估计量的一致性、渐近正态性，并给出了集中不等式。模拟和真实数据实验验证了所提方法的有效性。对您而言，该文展示了在大数据场景下如何通过子抽样设计在计算效率与统计效率之间取得平衡，其理论分析框架（渐近性质与集中不等式）与您在高维统计和假设检验方面的兴趣有潜在联系。
- **关键技术**: `Poisson subsampling`, `A-optimality`, `L-optimality`, `multiplicative regression`, `concentration inequalities`, `distributed computing`
- **为什么对您有用**: 本文属于统计计算与大规模数据方法，与您的统计计算兴趣直接相关。其子抽样概率设计可视为一种计算-统计权衡的实例，您可以用 very_familiar 的 minimax 估计理论来审视其最优性是否在更广的模型类中成立，或探索将其推广到高维乘法回归的可行性。该文作为 gateway reading，能帮助您了解子抽样方法在计算受限场景下的理论保证，但核心机器（子抽样最优性）不在您的武器库中，因此属于中期可做方向，需先熟悉子抽样理论。

### 2. [10.1111/sjos.70073](https://doi.org/10.1111/sjos.70073) · [arXiv](https://arxiv.org/abs/2308.04825) — Repelled Point Processes With Application to Numerical Integration
- **作者**: Diala Hawat, Gabriel Mastrilli, Rémi Bardenet, Raphaël Lachièze‐Rey
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Centre National de la Recherche Scientifique · Université Paris Cité · Université de Lille · Centre de Recherche en Informatique, Signal et Automatique de Lille · Mathématiques Appliquées à Paris 5 · Centrale Lille Institut · Centre de Recherche en Économie et Statistique · Université de Rennes 等
- **分类**: vol 53 · issue 3 · pp 1101-1133
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文从随机几何视角研究蒙特卡洛数值积分，将粗蒙特卡洛估计视为齐次泊松点过程（PPP）的线性统计量，而更规则的点过程可产生方差衰减更快的无偏估计。作者引入一个 Coulomb 排斥算子，通过轻微推开配置中的点来减少聚类，经验上对 PPP 及更规则点过程均保持无偏性并降低方差，且对 PPP 情形给出了方差缩减的理论证明。计算上，该算子复杂度为二次，且算法可无通信并行化。对您而言，该工作将随机几何与数值积分结合，其方差缩减机制和并行实现思路可能对您在高维统计计算中的算法设计有启发。
- **关键技术**: `Coulomb repulsion operator`, `Monte Carlo integration`, `point process`, `variance reduction`, `parallel algorithm`
- **为什么对您有用**: 该论文属于统计计算方向，与您的 primary interest 中的 statistical computing 直接相关。其核心是设计一种计算上可行的算子来改善蒙特卡洛估计的方差，这涉及算法复杂度和并行化，您可以用 very_familiar 的软件开发和数值方法知识快速评估其实现细节。中期可做：若想深入理论，需在 moderately_familiar 的随机几何或点过程理论上加强。

## 其他  *(other, 6 篇)*

### 1. [10.1111/sjos.70083](https://doi.org/10.1111/sjos.70083) — A Modified Random Survival Forest for Improving Prediction Accuracy in Case‐Cohort and Generalized Case‐Cohort Studies
- **作者**: Haolin Li, Haibo Zhou, David Couper, Jianwen Cai
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Boston University · University of North Carolina at Chapel Hill
- **分类**: vol 53 · issue 3 · pp 1299-1307
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对 case-cohort 和 generalized case-cohort 研究设计，提出一种改进的随机生存森林（random survival forest）方法，以提高非参数预测精度。现有方法要么忽略抽样设计导致估计有偏，要么在自助抽样中纳入逆概率权重但未充分利用设计效率。作者提出新的重抽样方案以保留 case-cohort 结构，并采用针对该设计定制的树分裂和节点内估计方法。理论上证明了所提方法的一致收敛性，模拟研究显示有限样本性能良好。最后将该方法应用于 ARIC 研究中 generalized case-cohort 设计的糖尿病发病预测。
- **关键技术**: `random survival forest`, `case-cohort design`, `inverse probability weighting`, `resampling scheme`, `uniform consistency`
- **为什么对您有用**: 本文属于流行病学应用中的生存预测方法，与您的 secondary interest 流行病学（应用、数据集、因果推断）相关，但方法学上主要是对随机森林的修改，而非因果推断或效率理论。作为流行病学应用，其分析模式（处理复杂抽样设计）对您可能有一定参考价值，但核心机器（随机森林、重抽样）不在您的技术武器库中，且方法学新颖性有限。

### 2. [10.1111/sjos.70067](https://doi.org/10.1111/sjos.70067) — Time‐Varying Degree‐Corrected Stochastic Block Models
- **作者**: Mengxue Li, Rainer von Sachs, Eugen Pircalabelu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: UCLouvain
- **分类**: vol 53 · issue 3 · pp 1029-1060
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种时变度修正随机块模型（t-v DCSBM），用于拟合沿时间轨迹观测的动态网络，允许社区内节点度异质性随时间演化。方法上采用滑动窗口与基于平滑的 profile-likelihood 估计，同时恢复时变连接概率、社区成员和节点度参数。理论贡献在于为这三个目标提供渐近理论：给出度参数和社区估计的相合速率，以及每个时间点社区成员估计的强相合性。模拟研究和两个真实数据应用验证了方法。对您而言，该文属于网络数据分析领域，与您的主要兴趣（因果推断、高维统计等）关联较弱，但可作为了解动态网络社区检测方法的入门读物。
- **关键技术**: `time-varying degree-corrected stochastic block model`, `sliding window smoothing`, `profile likelihood`, `strong consistency`
- **为什么对您有用**: 本文属于网络数据分析，与您的主要兴趣（因果推断、高维统计、U统计量等）关联较弱。但作为统计方法学论文，其滑动窗口平滑和 profile likelihood 技术可能对纵向数据建模有启发。作为入门读物，它清晰展示了动态网络建模的设定和渐近理论，但方法学新颖性一般。武器库足以理解，但无需深入。

### 3. [10.1111/sjos.70068](https://doi.org/10.1111/sjos.70068) · [arXiv](https://arxiv.org/abs/2408.17257) — Likelihood Estimation for Stochastic Differential Equations with Mixed Effects
- **作者**: Fernando Baltazar‐Larios, Mogens Bladt, Michael Sørensen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Universidad Nacional Autónoma de México · University of Copenhagen
- **分类**: vol 53 · issue 3 · pp 1061-1080
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究带混合效应的随机微分方程（SDE）的似然推断，其中部分参数在不同实验单元间随机变化。由于离散观测下似然函数通常无显式形式，作者提出基于增广数据的 Gibbs 采样器和随机 EM 算法，利用 Bladt 和 Sørensen (2014) 的扩散桥模拟方法生成潜在路径。该方法实现简单、无调参参数，且计算时间随观测间隔线性增长，在低采样频率下高效。对于指数族扩散过程（涵盖许多实际模型），算法可大幅简化。模拟研究验证了方法在 Ornstein–Uhlenbeck 过程和 t-扩散混合效应模型中的良好表现，并应用于神经元数据，同时讨论了扩展到测量误差模型的途径。对您而言，本文属于统计计算与纵向数据建模的交叉，但并非您主要兴趣中的因果推断或高维理论，可作为统计计算方法的参考。
- **关键技术**: `Gibbs sampler`, `stochastic EM algorithm`, `diffusion bridge simulation`, `mixed-effects SDE`, `exponential family of diffusions`
- **为什么对您有用**: 本文属于统计计算与纵向数据建模的交叉，但并非您主要兴趣中的因果推断或高维理论。作为统计计算方法的参考，其扩散桥模拟和 EM 算法可能对您处理纵向数据中的潜在变量问题有启发，但整体相关性较低。

### 4. [10.1111/sjos.70086](https://doi.org/10.1111/sjos.70086) — Extremal Alignments in LCS‐Inference
- **作者**: Jüri Lember, Joonas Sova
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Tartu
- **分类**: vol 53 · issue 3 · pp 1327-1342
- 相关性 2/10 · novelty: `minor`
- **摘要**: 本文研究有限字母串相似性度量——最长公共子序列（LCS）的最优比对集合的多样性。在成对马尔可夫模型下，证明了强相关序列的极值比对之间的距离仍呈对数增长，且相关性越强增长越慢。基于此对数增长，得到了 LCS 平均长度的收敛速率，该速率快于 iid 独立情形下目前已知的最佳速率。此外，极值比对被证明是研究 LCS 性质的有用技术工具，并由此推导出未知的 Chvátal–Sankoff 常数的一个界。该工作属于组合概率与随机序列分析的范畴，方法上涉及马尔可夫链、大偏差或集中不等式等工具。对您而言，该主题与您的主要兴趣（因果推断、高维统计等）无直接交集，但其中关于随机序列极值结构的分析思路，或可类比于您在高阶 U-统计量中处理相关结构的某些技术。
- **关键技术**: `longest common subsequence`, `pairwise Markov model`, `extremal alignments`, `logarithmic growth rate`, `Chvátal–Sankoff constant`
- **为什么对您有用**: 该论文属于随机序列与组合概率方向，与您的主要兴趣（因果推断、高维统计、半参数理论等）无直接关联，也不属于 gateway-reading 范畴（非天文、经济、流行病学或计算复杂度入门）。因此相关性较低，仅作为跨领域参考，不建议优先阅读。

### 5. [10.1111/sjos.70084](https://doi.org/10.1111/sjos.70084) · [arXiv](https://arxiv.org/abs/2503.21768) — Results on Branching Random Walks and Rumor Processes via Germ Order
- **作者**: Daniela Bertacchi, Fabio Zucca
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Milano-Bicocca · Politecnico di Milano
- **分类**: vol 53 · issue 3 · pp 1308-1326
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究分支随机游走与谣言过程的随机序（germ order）性质。该序最初针对具有常数繁殖律和独立后代扩散的分支随机游走定义，通过一维生成函数比较；本文将其推广到由多维生成函数刻画的过程，如一般分支随机游走和谣言过程。作者利用 germ order 刻画了具有非齐次繁殖/传播律的这类过程的渐近行为。主要贡献在于建立了多维情形下 germ order 的性质，并应用于具体过程的行为分类。对您而言，该文属于随机过程理论，与您的主攻方向（因果推断、高维统计、U-统计量等）无直接交集，但其中生成函数与渐近分析的技术或可为某些统计计算问题提供参考。
- **关键技术**: `germ order`, `generating functions`, `branching random walks`, `rumor processes`, `stochastic ordering`
- **为什么对您有用**: 本文属于随机过程理论，与您的主攻方向（因果推断、高维统计、U-统计量等）无直接交集，但其中生成函数与渐近分析的技术或可为某些统计计算问题提供参考。作为 gateway reading，本文对统计学家而言并非入门级读物，需要随机过程背景；武器库中的工具（如高维渐近、U-统计量）不足以直接支撑进入该方向，因此暂不可做。

### 6. [10.1111/sjos.70058](https://doi.org/10.1111/sjos.70058) — Issue Information
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 53 · issue 3
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是《Scandinavian Journal of Statistics》第53卷第3期的期刊信息页，包含期刊宗旨、编辑团队、投稿指南等常规内容，无具体研究论文。期刊主要发表理论和应用统计的研究论文，也欢迎与概率及其他领域相关的统计动机论文，以及统计方法创新应用的论文。对研究者而言，此信息页无实质学术内容，仅作为期刊动态的参考。
- **为什么对您有用**: 本文为期刊信息页，无具体研究内容，与您的主要或次要兴趣均无直接关联。不建议花费时间阅读全文。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

