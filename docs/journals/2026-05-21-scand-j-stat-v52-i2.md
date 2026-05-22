# Scand. J. Stat. — Vol 52  Issue 2  ·  2026-05-21

- 共 21 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12770](https://doi.org/10.1111/sjos.12770) — Post‐selection inference for high‐dimensional mediation analysis with survival outcomes
- **作者**: Tzu‐Jung Huang, Zhonghua Liu, Ian W. McKeague
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 756-776
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维中介变量与生存结局的因果中介分析设定下，目标是推断暴露对生存结局的最大边际自然间接效应（NIE），关键假设包括顺序可忽略性与半参数模型条件。针对高维筛选后的 post-selection inference 挑战，本文基于半参数有效影响函数构造了 stabilized one-step estimator。该估计器通过影响函数修正了中介变量选择带来的偏差，并在考虑选择事件（maximally selected）的条件下证明了其渐近正态性。理论上给出了筛选后 NIE 的有效置信区间；实证上应用于肺癌基因组流行病学数据，识别出介导吸烟与肺癌生存关联的 CpG 位点。对您有用：本文将半参数有效影响函数与 post-selection inference 结合，直接推进了高维中介分析的理论，对您在因果中介与效率理论交叉方向的研究有重要参考价值。
- **关键技术**: `post-selection inference`, `semiparametric efficient influence function`, `stabilized one-step estimator`, `natural indirect effect`, `high-dimensional mediation analysis`
- **为什么对您有用**: 直接结合了您关注的因果中介分析与半参数效率理论，展示了如何用影响函数解决高维筛选后的有效推断问题，且附带流行病学真实数据集。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.12776](https://doi.org/10.1111/sjos.12776) — On high‐dimensional variance estimation in survey sampling
- **作者**: Esther Eustache, Mehdi Dagdoug, David Haziza
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 924-959
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在调查抽样（survey sampling）框架下，假设线性回归模型用于预测辅助变量，目标是在 p/n 不趋于零的高维设定下对总体估计量的方差进行有效估计。作者指出，基于一阶 Taylor 展开或 jackknife 的传统方差估计量在高维情形下会产生显著偏差，并通过理论与模拟揭示了偏差来源——本质上是高维回归系数估计的 shrinkage bias 渗入方差公式。提出了 bias-adjusted variance estimators，通过显式修正项消除高维偏差，理论上证明了修正后方差估计量的偏差在 p/n 较大时仍可控。实证结果验证了修正估计量在偏差和覆盖率上的优势。对您有用：该工作将高维偏差修正思路引入抽样调查方差估计，与您在 high-dimensional statistics 和 debiased ML 方向的兴趣直接相关，bias-adjustment 的技术路线可迁移至其他高维推断场景。
- **关键技术**: `high-dimensional linear regression`, `bias-adjusted variance estimation`, `Taylor expansion bias correction`, `jackknife variance estimation`, `survey sampling prediction`
- **为什么对您有用**: 直接关联您的高维统计与 efficiency theory 兴趣：揭示了高维下方差估计的偏差机制并提出修正，bias-adjustment 思路与 debiased ML 的去偏逻辑同源，技术路线可迁移至高维因果推断中的方差估计问题。

### 2. [10.1111/sjos.12772](https://doi.org/10.1111/sjos.12772) — Support estimation and sign recovery in high‐dimensional heteroscedastic mean regression
- **作者**: Philipp Hermann, Hajo Holzmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 805-839
- 相关性 0/10 · novelty: `weaker_assumption`
- **摘要**: 在随机设计线性均值回归模型下，目标是在误差可能异方差且重尾的设定下进行支持集估计与符号恢复，关键正则假设为损失函数的严格凸性与调参依赖于问题参数。方法采用严格凸且光滑的 Huber 损失变体配合 adaptive LASSO 惩罚，兼顾计算效率与鲁棒性。证明了所得估计量具有符号一致性（sign-consistency），并在 ℓ∞ 范数下达到与同方差轻尾设定相同的最优收敛速率，即重尾异方差并未导致速率损失。模拟部分将方法与 thresholded LASSO、knockoffs（FDR 控制）对比，并指出 Donoho–Tanner 相变曲线对变量选择的指导意义。主要理论贡献在于将高维 LASSO 的 sign-consistency 与最优速率结果从轻尾假设推广到重尾异方差情形。对您有用：该工作直接推进了高维统计中放松分布假设的研究，其 sign-consistency 证明技术与 optimal rate 结果可迁移到您关注的高维推断与 debiased ML 框架中对重尾误差的鲁棒性分析。
- **关键技术**: `adaptive LASSO`, `smooth Huber loss`, `sign-consistency`, `Donoho-Tanner transition`, `knockoff FDR control`, `thresholded LASSO`
- **为什么对您有用**: 直接关联您的高维统计 primary interest：在重尾异方差下保持最优速率与 sign-consistency，为 debiased ML / 高维推断在弱假设下的理论提供了基础；Donoho–Tanner 相变与 knockoffs 的讨论也对高维假设检验有参考价值。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1111/sjos.12767](https://doi.org/10.1111/sjos.12767) — A novel semiparametric approach to nonignorable missing data by catching covariate marginal information
- **作者**: Manli Cheng, Yukun Liu, Jing Qin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 691-709
- 相关性 9/10 · novelty: `new_theory`
- **摘要**: 在非随机缺失数据设定下，针对参数可识别性难题，本文提出结合 logistic 倾向得分模型与半参数比例似然比模型（SPLRM）的新框架，无需工具变量或影子变量即可在多数场景下实现可识别性。在可识别情形下，该方法利用基于密度比模型的经验似然捕捉协变量边际分布信息，所得估计量被证明具有渐近正态性且达到半参数有效界。在不可识别的例外情形下，通过充分利用边际协变量信息进行敏感性分析，提升了对模型误设的稳健性。数值结果表明该估计量较现有方法更可靠且对误设更稳健。该工作在缺失数据下实现了半参数有效估计与敏感性分析的统一，对您在因果推断中处理选择偏差的半参数效率界及敏感性分析有直接的方法论借鉴意义。
- **关键技术**: `semiparametric proportional likelihood ratio model`, `empirical likelihood`, `semiparametric efficiency bound`, `nonignorable missing data`, `sensitivity analysis`
- **为什么对您有用**: 直击您 primary interest 中的半参数效率理论与敏感性分析；无需 IV 即可处理非随机缺失（选择偏差）的思路，对因果推断中的 identification 与 sensitivity analysis 有直接迁移价值。

### 2. [10.1111/sjos.12777](https://doi.org/10.1111/sjos.12777) — Statistical inference in the presence of imputed survey data through regression trees and random forests
- **作者**: Mehdi Dagdoug, Camelia Goga, David Haziza
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 960-998
- 相关性 6/10 · novelty: `new_theory`
- **摘要**: 在调查抽样存在项目无回答（item nonresponse）的设定下，目标是有限总体均值的 imputed estimator 的一致性与方差估计，允许预测变量维度随样本量发散。作者以回归树和随机森林作为非参数插补工具，在高维框架下建立了树/森林插补估计量的均方一致性（mean square consistency）条件。提出了一种基于 K-fold 交叉验证的新型方差估计量，用于量化插补带来的额外变异性。模拟从偏差、效率和正态置信区间覆盖率三方面评估了点估计与方差估计的表现，并从理论与经验两个角度讨论了随机森林超参数选择的影响。该工作为非参数 ML 插补提供了有限总体框架下的严格理论保证，对您在非参数理论（随机森林一致性条件）和统计计算（交叉验证方差估计、超参数调优）方向有参考价值。
- **关键技术**: `random forest imputation`, `regression tree consistency`, `cross-validation variance estimation`, `high-dimensional survey sampling`, `mean square consistency`, `finite population inference`
- **为什么对您有用**: 论文在非参数理论方向给出了随机森林插补估计量的均方一致性条件与交叉验证方差估计，对您关注的高维非参数理论（diverging predictors 下的 consistency）和统计计算（方差估计算法设计、超参数理论分析）有直接参考意义。

### 3. [10.1111/sjos.12778](https://doi.org/10.1111/sjos.12778) — Adaptively robust small area estimation: Balancing robustness and efficiency of empirical bayes confidence intervals
- **作者**: Daisuke Kurisu, Takuya Ishihara, Shonosuke Sugasawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 999-1017
- 相关性 5/10 · novelty: `weaker_assumption`
- **摘要**: 在 Fay-Herriot 模型的小区域估计设定下，标准 Empirical Bayes (EB) 方法对异常值敏感，而现有稳健方法在模型正确时效率受损，本文旨在解决此 robustness-efficiency 权衡问题。核心方法是用 β-divergence 替代边际对数似然构造目标函数，并通过优化调谐参数来追求 EB 置信区间的渐近效率。理论贡献在于建立了分布正确设定与存在异常区域两种情形下的渐近理论，证明该方法在正确设定下可恢复标准 EB 的效率，在异常值下保持稳健。模拟与犯罪数据应用表明，该方法在区间估计的覆盖率和长度上实现了较好的平衡。对您有用：本文在 EB 框架下通过 divergence 调节稳健性与效率的渐近理论，对您在 efficiency theory 中思考 robust estimation 与 efficiency bound 的权衡有参考价值。
- **关键技术**: `Empirical Bayes`, `beta-divergence`, `Fay-Herriot model`, `asymptotic efficiency`, `robust confidence interval`
- **为什么对您有用**: 本文聚焦于稳健性与渐近效率的权衡，属于 efficiency theory 的范畴；虽然应用场景是小区域估计，但其利用 divergence 放松假设并追求区间估计效率的思路，对您在 efficiency theory 和 semiparametric theory 中处理模型误设下的效率问题有方法论启发。

### 4. [10.1111/sjos.12779](https://doi.org/10.1111/sjos.12779) — Kernel density estimation in metric spaces
- **作者**: Chenfei Gu, Mian Huang, Xinyu Song, Xueqin Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 1018-1057
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在一般度量空间设定下，本文目标是基于 metric distribution function 进行概率密度估计，解决非欧数据缺乏基础非参数工具的问题。作者将经典核密度估计推广至度量空间，提出局部与全局两种 metric kernel density estimator（MKDE），并在正则条件下建立大样本性质（逐点一致性、MISE 收敛率）。带宽选择方面，发展了基于 MISE 准则的带宽选取方法，给出了最优带宽的渐近表达式。模拟与海马体形状数据分析展示了有限样本表现，后者关联阿尔茨海默病严重程度与海马体表面变化。对您而言，本文提供了非参数密度估计从欧氏空间到一般度量空间的直接推广路径，属于非参数理论方向的方法扩展，但未涉及效率界或更高阶渐近理论。
- **关键技术**: `metric distribution function`, `kernel density estimation in metric spaces`, `MISE bandwidth selection`, `large sample asymptotics`, `non-Euclidean data analysis`
- **为什么对您有用**: 直接关联您 primary interest 中的非参数理论，提供了度量空间上 KDE 的完整框架（估计+渐近+带宽），可迁移至其他非欧数据场景；应用部分涉及流行病学数据结构，但方法学 novelty 限于标准渐近，未触及效率界或高阶理论。

### 5. [10.1111/sjos.12774](https://doi.org/10.1111/sjos.12774) — Conditional Aalen–Johansen estimation
- **作者**: Martin Bladt, Christian Furrer
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 873-902
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在有限状态跳跃过程设定下，提出了条件 Aalen–Johansen 估计量，用于非参数估计条件状态占据概率，支持外部与内部协变量条件化。该估计量在生存模型下退化为条件 Kaplan–Meier 估计量，在离散协变量下包含近期 landmark 估计量。理论方面，作者在宽松的多变量计数过程矩条件下证明了强一致相合性与渐近正态性，特别允许转移次数无界。这一结果为多状态生存分析提供了灵活的非参数推断工具。对您有用：该非参数估计与渐近理论直接契合您的非参数/半参数理论兴趣，且条件状态占据概率是纵向因果推断中多状态处理效应的核心 estimand，为后续构建半参数效率界或 debiased 方法提供了非参数基础。
- **关键技术**: `conditional Aalen-Johansen estimator`, `finite-state jump process`, `strong uniform consistency`, `asymptotic normality`, `multivariate counting process`, `landmark estimation`
- **为什么对您有用**: 该文在多状态过程下建立了条件非参数估计的渐近理论，直接契合您的非参数理论兴趣；同时条件状态占据概率是纵向因果推断中随时间变化的处理效应的核心 estimand，对您在纵向因果推断方向的研究有基础性支撑作用。

### 6. [10.1111/sjos.12775](https://doi.org/10.1111/sjos.12775) — A joint estimation approach for monotonic regression functions in general dimensions
- **作者**: Christian Rohrbeck, Deborah A. Costain
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 903-923
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在一般维度的单调非参数回归设定下，本文研究多个单调回归函数的联合估计问题，目标是通过信息借用提升估计效率。核心方法是对函数估计值的成对差异施加惩罚，惩罚权重由函数在某点等价的统计检验决定。估计量通过迭代优化算法逐个更新直至收敛，适用于固定/随机设计及任意协变量维度。理论与模拟表明，当函数存在相似性时估计效率显著提升，且在函数不同时不会过度平滑。实证部分分析了巴西新生儿死亡率与英格兰中风患者的流行病学数据。对您有用：该文展示了非参数设定下通过惩罚与等价检验实现信息借用与效率提升的机制，其迭代优化思路可迁移至其他半参数/非参数效率理论问题。
- **关键技术**: `monotonic regression`, `joint estimation`, `penalized pairwise differences`, `equivalence test`, `iterative optimization`, `information borrowing`
- **为什么对您有用**: 涉及非参数理论中的效率提升（信息借用）与统计计算（迭代优化），并在流行病学数据上应用，对您在非参数估计效率与计算实现方面的兴趣有参考价值。

### 7. [10.1111/sjos.12773](https://doi.org/10.1111/sjos.12773) — Likelihood analysis of latent functional response regression models for sequences of correlated binary data
- **作者**: Fatemeh Asgari, Mohammad H. Alamatsaz, Saeed Hayati, Valeria Vitelli
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 840-872
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究潜在功能响应回归模型：响应曲线本身不可观测，仅能在一系列相关二值数据点处观测到其离散化版本，estimand 为功能回归系数与潜在过程的主成分。方法基于参数扩展（PX-EM）技术构建完全数据似然，可处理不等间距与缺失观测；在 Function-on-Scalar 回归设定下，假设潜在响应为取值于可分 Hilbert 空间的高斯随机元素。提出自适应 EM 算法获得功能回归系数与主成分的光滑估计，收敛性质依赖 EM 的单调上升与正则化平滑惩罚。模拟与实例验证了方法表现，R 包 dfrr 已发布。对您而言，该文在统计计算（自适应 EM 算法设计）与 Hilbert 空间上的功能数据建模方面有参考价值，但未涉及半参数效率界或 debiased 推断。
- **关键技术**: `parameter expansion EM (PX-EM)`, `functional principal component analysis`, `function-on-scalar regression`, `complete data likelihood`, `separable Hilbert space Gaussian process`
- **为什么对您有用**: 与您 primary interest 中的统计计算（自适应 EM 算法、R 包实现）和半参数/非参数理论（Hilbert 空间功能数据）有弱到中等关联；但方法偏参数化，未触及效率界或高维推断，收益主要在计算框架与功能数据建模思路的可迁移性。

### 8. [10.1111/sjos.12768](https://doi.org/10.1111/sjos.12768) — Post‐selection inference for the Cox model with interval‐censored data
- **作者**: Jianrui Zhang, Chenxi Li, Haolei Weng
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 710-735
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究区间删失数据下 Cox 比例风险模型经 lasso 变量选择后的 post-selection 推断问题，目标是在给定所选模型的条件下给出渐近有效的 p 值与置信区间。核心方法构造了一个 pivotal quantity，在局部参数下证明其收敛到均匀分布，从而实现选择性推断的校准。方法涉及高效信息矩阵（efficient information matrix）的估计，文中提出多种估计策略并证明其一致性。模拟显示中小样本下表现良好，并以阿尔茨海默病研究数据做实证展示。对您有用之处在于：高效信息矩阵的估计技术与 semiparametric efficiency theory 直接相关，且 post-selection inference 的 pivotal quantity 构造思路可迁移到其他高维半参数推断场景。
- **关键技术**: `post-selection inference`, `pivotal quantity`, `efficient information matrix`, `lasso variable selection`, `interval-censored Cox model`, `local asymptotic framework`
- **为什么对您有用**: 高效信息矩阵估计直接关联您的 semiparametric efficiency theory 兴趣；post-selection inference 的 pivotal 构造与 hypothesis testing 和高维推断交叉，方法框架可迁移至其他半参数模型的选择后推断问题。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12771](https://doi.org/10.1111/sjos.12771) — On the properties of distance covariance for categorical data: Robustness, sure screening, and approximate null distributions
- **作者**: Qingyang Zhang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 777-804
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在大型稀疏列联表中，传统 Pearson Chi-squared 检验功效显著下降，本文研究分类变量的 distance covariance 泛函的统计性质。首先证明 distance covariance 泛函在类别数固定或发散时均具有 B-robustness，而 Chi-squared 不具备此性质。其次，在温和条件下建立 distance covariance screening 的强一致性（sure screening），模拟显示其在稀疏表中优于 Chi-squared screening，并以 General Social Survey 数据做实证。最后，对 bias-corrected distance correlation 估计量推导近似零分布，避免置换检验的计算负担。对您有用：该文将 distance covariance 与 U-statistic 估计结合用于假设检验与 sure screening，直接连接您的高阶 U-statistics 与假设检验方向，B-robustness 与近似零分布的理论工具也可迁移至其他非参数检验问题。
- **关键技术**: `distance covariance for categorical data`, `B-robustness`, `sure screening consistency`, `U-statistic permutation test`, `bias-corrected distance correlation`, `approximate null distribution`
- **为什么对您有用**: 直接连接您的高阶 U-statistics 与假设检验方向；distance covariance 的 U-statistic 估计与近似零分布推导为非参数独立性检验提供了可迁移的理论工具，sure screening 部分也与高维变量筛选相关。

### 2. [10.1111/sjos.12766](https://doi.org/10.1111/sjos.12766) — A comprehensive framework for evaluating time to event predictions using the restricted mean survival time
- **作者**: Ariane Cwiling, Vittorio Perduca, Olivier Bouaziz
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 658-690
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在右删失生存数据设定下，本文研究基于限制平均生存时间（RMST）的预测评估问题，关键假设为RMST估计量渐近收敛且允许模型误设。核心方法包含三个部分：首先，利用逆概率删失加权（IPCW）构建了估计RMST均方误差的准则。其次，引入适用于右删失数据的模型不可知保形算法，以计算预测区间并评估局部变量重要性。最后，发展了一种检验全局变量重要性的模型不可知统计检验方法。理论上证明了该框架在模型误设下的有效性，无需依赖特定参数模型假定。对您可能有用：其全局变量重要性的假设检验构建直接对应您在数学统计（假设检验）方向的兴趣，且IPCW与半参数理论紧密相连，生存分析背景亦契合流行病学应用。
- **关键技术**: `restricted mean survival time (RMST)`, `inverse probability censoring weighting (IPCW)`, `conformal prediction`, `model-agnostic hypothesis testing`, `variable importance`
- **为什么对您有用**: 论文提出的全局变量重要性检验方法直接对应您在数学统计（假设检验）方向的兴趣；同时，IPCW框架和模型误设下的渐近性质探讨与半参数理论相关，生存分析背景也契合流行病学应用。

### 3. [10.1111/sjos.12757](https://doi.org/10.1111/sjos.12757) — Optimal designs for testing pairwise differences: A graph‐based game theoretic approach
- **作者**: Arpan Singh, Satya Prakash Singh, Ori Davidov
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 533-571
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究多处理实验中成对处理差异的假设检验最优设计问题，关注两类科学问题：所选处理对中是否存在至少一对有差异（union 型），以及是否所有选定对均有差异（intersection 型）。作者将处理对结构建模为图，把最优设计问题转化为图上的 max-min 博弈：自然选择最不利的参数配置，实验者选择最优分配比例以最大化最坏情形下的检验功效。部分所得 max-min 设计与经典设计重合但首次被证明最优性，另一部分则是新设计，相比朴素等分配设计有显著功效提升。对您而言，该文将博弈论与图结构引入假设检验最优设计的思路，可为因果推断中多处理比较的实验设计（如 IV 或纵向设定下的多臂干预）提供理论参考。
- **关键技术**: `max-min optimal design`, `graph-based game theoretic formulation`, `pairwise comparison hypothesis testing`, `union and intersection hypotheses`, `optimal allocation proportions`
- **为什么对您有用**: 与您 hypothesis testing 的 primary interest 直接相关，max-min 博弈框架对多处理因果推断实验设计有迁移价值；但属于经典 DOE 范式，非高维/半参数设定。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12780](https://doi.org/10.1111/sjos.12780) — Road traffic estimation and algorithmic routing in a spatially dependent network
- **作者**: Rens Kamphuis, Michel Mandjes, Paulo Serra
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 1058-1091
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究在具有空间依赖性的道路交通网络中，基于独立探测车辆的实现行程时间估计各边行程时间的联合分布。所提估计量被证明具有相合性且达到最优收敛速率（rate-optimal）。在路由策略中，方法利用空间依赖性在行驶途中迭代更新剩余行程时间的预测分布，并支持包含估计不确定性与风险规避的广义目标函数。数值实验系统评估了估计量与路由策略的组合表现。对您而言，本文在空间依赖结构下的联合分布估计与最优速率证明，以及算法路由的迭代更新机制，可为统计计算（算法设计）和数学统计（收敛速率）方向提供跨领域的方法参考。
- **关键技术**: `joint distribution estimation`, `rate-optimal estimator`, `spatial dependence`, `predictive distribution updating`, `algorithmic routing`
- **为什么对您有用**: 本文涉及联合分布估计的相合性与最优速率证明，以及基于预测分布更新的算法路由，与您在统计计算（算法设计）和数学统计（收敛速率）方面的兴趣有方法学交叉，可提供网络结构数据下的估计与计算思路。

### 2. [10.1111/sjos.12769](https://doi.org/10.1111/sjos.12769) — Robust Composite Quantile Regression with Large‐scale Streaming Data Sets
- **作者**: Kangning Wang, Di Zhang, Xiaofei Sun
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 736-755
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在流数据设定下，针对累积数据量无界、内存受限且复合分位数回归(CQR)目标函数非光滑的挑战，研究如何实现在线CQR估计。方法上，首先构造了光滑化的CQR目标函数，随后提出一种在线可更新CQR算法。理论上，证明了该可更新估计量具有oracle性质，即其渐近表现等价于基于全量数据的离线估计量。数值实验验证了方法的有效性。对您在统计计算（流数据在线算法）方向有直接参考价值，其光滑化与在线更新的结合思路可迁移至其他非光滑目标函数的在线半参数估计。
- **关键技术**: `composite quantile regression`, `streaming data`, `online renewable estimation`, `smooth approximation`, `oracle property`
- **为什么对您有用**: 涉及统计计算（流数据在线算法）与半参数理论（CQR的oracle性质），其处理非光滑目标函数的在线更新思路对您在统计计算与半参数估计交叉领域的工作有参考价值。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.1111/sjos.12764](https://doi.org/10.1111/sjos.12764) — Weighted reduced rank estimators under cointegration rank uncertainty
- **作者**: Christian Holberg, Susanne Ditlevsen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 595-630
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多维协整过程的 reduced rank regression 设定下，传统两步法先估秩再估参数，但渐近理论通常假设真实秩已知。本文首先量化了秩误设（偏大或偏小）下协整估计量的渐近偏差，并推导了误设秩下的渐近分布。进而提出一类新的加权 reduced rank 估计量，通过对不同秩对应的估计赋权来灵活应对秩选择困难的情况。理论部分给出了误设秩下估计量的渐近性质，实证表明适当选取权重可在秩不确定时提升预测表现，最后用心理学视觉处理实验的 EEG 数据做了演示。对您而言，协整是计量经济学的核心模型，本文在秩误设下推导渐近分布的思路与您对 mathematical statistics 中假设检验/模型误设的兴趣相通，加权估计策略也可作为高维秩不确定场景的方法参考。
- **关键技术**: `reduced rank regression`, `cointegration analysis`, `asymptotic distribution under misspecification`, `weighted rank estimation`, `rank uncertainty`
- **为什么对您有用**: 协整是经济理论中核心的时间序列模型，本文在秩误设下推导渐近分布的工作与您 mathematical statistics / hypothesis testing 的兴趣直接相关；加权 reduced rank 估计策略对高维秩不确定场景有方法迁移价值。

## 其他  *(other, 4 篇)*

### 1. [10.1111/sjos.12781](https://doi.org/10.1111/sjos.12781) — Ratio‐consistency of some invariant <i>U</i>‐statistic‐based estimators with an application to high‐dimensional data ranking
- **作者**: Jia Guo, Bu Zhou
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 1092-1110
- 相关性 9/10
- **摘要**: {
  "topic": "higher_order_U",
  "summary_zh": "本文在高维设定下研究协方差矩阵函数的估计问题，目标是构造无偏且旋转-平移不变的 U-统计量线性组合估计器，并在较弱矩假设下建立其比率一致性（ratio-consistency）。作者提出了一般性推导程序，利用 U-统计量方差公式（Hoeffding 分解）给出了判定比率一致性的关键理论引理。在此基础上，推导了所提无偏估计器满足比率一致性的充分条件，避免了直接处理高维协方差矩阵特征结构的复杂依赖。作为应用，提出了一种基于此类不变估计器的高维数据排序新程序。对您有用：该文将 U-统计量方差分解技巧严格应用于高维协方差估计，直接连接了您的"higher-order U-statistics"与"high-dimensional statistics"两个核心兴趣，其不变估计器构造与比率一致性证明框架可迁移至其他高维 U-统计量推断问题。",
  "key_techniques": [
    "ratio-consistency",
    "U-statistics variance formula",
    "rotation-translation-invariant estimators",
    "high-dimensional covariance matrix",

### 2. [10.1111/sjos.12765](https://doi.org/10.1111/sjos.12765) — Enriched Pitman–Yor processes
- **作者**: Tommaso Rigon, Sonia Petrone, Bruno Scarpa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 631-657
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 本文提出了一种新的贝叶斯非参数先验——enriched Pitman–Yor 过程，旨在解决传统先验（如 Dirichlet 过程）无法刻画嵌套聚类结构的问题。作者证明了该先验与 enriched Dirichlet 过程及标准化随机测度的形式化联系，并给出了 square-breaking 表示、后验分布的闭式解及相应的 Pólya urn 方案。多个已有模型（如 spike-and-slab 基测度的 Dirichlet 过程、mixture of mixtures 模型）被证明是该先验的特例，从而提供了一个统一的贝叶斯非参数先验框架。最后通过生态学物种采样问题展示了其实用性。该文属于贝叶斯非参数先验构造，与您关注的半参数效率理论或因果推断距离较远，方法学新颖性主要在贝叶斯先验设计而非频率渐近理论。
- **关键技术**: `enriched Pitman-Yor process`, `nested clustering`, `square-breaking representation`, `Polya urn scheme`, `normalized random measures`
- **为什么对您有用**: 本文属于贝叶斯非参数先验构造，与您关注的半参数效率界、因果推断或高维推断等核心方向距离较远，仅在非参数模型这一宽泛类别下有微弱交集。

### 3. [10.1111/sjos.12763](https://doi.org/10.1111/sjos.12763) — Graph neural networks for the localization of faults in a partially observed regional transmission system
- **作者**: Mantautas Rimkus, Piotr Kokoszka, Dongliang Duan, Xuao Wang, Haonan Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2 · pp 572-594
- 相关性 1/10
- **摘要**: {
  "topic": "stat_computing",
  "summary_zh": "本文研究部分观测的区域电力传输系统中故障定位问题，目标是在仅部分节点有测量设备的条件下，识别短路故障的拓扑位置。作者构造了回归型图神经网络（regression GNN），结合统计方法，实现无需故障标签训练数据即可定位故障。核心创新在于"零样本"定位：网络训练时不使用故障位置信息，而是利用图结构传播的物理特性与GNN的消息传递机制之间的对应。理论部分较弱，主要依赖数值实验验证方法在部分观测场景下的有效性。对您而言，该文在统计计算（GNN架构设计+统计方法协同）方面有一定参考，但理论深度有限，novelty 偏应用层面。",
  "key_techniques": [
    "regression graph neural network",
    "partially observed network topology",
    "zero-shot fault localization",
    "message passing on graphs",
    "physics-informed deep learning"
  ],
  "why_relevant": "与您 primary interest 中 statistical computing 的算法设计有弱关联

### 4. [10.1111/sjos.12726](https://doi.org/10.1111/sjos.12726) — Issue Information
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 2
- 相关性 0/10 · novelty: `minor`
- **摘要**: 这是 Scandinavian Journal of Statistics 第 52 卷第 2 期的期刊信息页，非研究论文，摘要仅为出版社（Wiley）的 ESG 声明。无任何统计方法、理论或实证结果。对研究者的任何兴趣方向均无参考价值。
- **为什么对您有用**: 无研究内容，与所有 primary/secondary interests 均无关。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

