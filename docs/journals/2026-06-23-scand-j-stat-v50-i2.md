# Scand. J. Stat. — Vol 50  Issue 2  ·  2026-06-23

- 共 16 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 16 篇全部抓到（对照 OpenAlex 16 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期整体围绕非参数/半参数方法展开，16篇中有7篇归属该领域，覆盖扩散过程漂移估计（Nadaraya-Watson）、高维Cox比例风险模型（debiased lasso不依赖逆稀疏假设）、极值分位数（非参数渐近置信区间）、函数型数据（稳健M型位置估计与协方差变点检测）、贝叶斯稳健回归（Student‑t过程的正则变化鲁棒性分析）、小区域估计（benchmarked线性收缩预测）以及平稳determinantal点过程（似然渐近近似）。假设检验与模型选择有2篇，分别处理大规模依赖结构下的post hoc真发现数下界（基于closed testing和广义均值阈值化）和聚类数据线性混合效应模型的选择（条件广义信息准则CGIC）。因果推断与实验设计方向有2篇，一是概率样本与非概率样本整合的多重稳健估计量（融合多个propensity和outcome模型），二是多臂临床试验个性化治疗规则的最优分配设计（D‑optimal框架，最优分配率对协变量的依赖性随臂数变化）。高维/正则化方向1篇，研究动态随机截距模型的同时变量选择（联合建模初始响应以避免条件似然偏倚）。其余3篇分属图模型几何（高斯双马尔可夫分布）、贝叶斯无知先验（离散凸递增失败率）和连续时间阈值自回归（跳跃过程与粒子滤波估计）。

在非参数/半参数主线中，高维Cox模型的推断改进值得注意——通过二次规划直接近似逆信息矩阵，突破了传统debiased lasso对逆稀疏性的依赖，为生存分析中的发散维数协变量推断提供了实用解法。函数型数据分析有两篇推进：一是M型平滑样条在离散采样且存在测量误差下达到minimax最优率，二是协方差算子的CUSUM变点检测，系统分析了参数截断对检验的影响。极值分位数的非参数置信区间基于均匀次序统计量的分布性质，在二阶正则变化下证明覆盖收敛。贝叶斯方向用正则变化理论严格证明了Student‑t过程后验自动拒绝离群值的能力。小区域估计中的BELS预测器在无正态性假设下给出了二阶无偏MSE估计。

因果推断与实验设计的两篇直接涉及因果参数估计与优化。多重稳健数据整合将double robustness扩展至多个working models同时成立时的consistency，并给出渐近正态性与方差估计；这适用于非概率抽样下的总体参数推断，与因果推断中的倾向性和结果模型稳健结合一致。个性化治疗规则的最优设计理论揭示：两臂时最优分配不依赖协变量，三臂及以上则依赖协变量与真实系数——直接关联因果推断中个体化处理效应的实验设计。假设检验中，基于closed testing的大规模同时推断方法通过广义均值阈值化处理依赖结构，计算为线性时间，对多重比较中的相关性调整有参考价值。

若关注因果推断与半参数效率，本期最贴的包括：多重稳健数据整合（多重稳健性、渐近理论）、Cox模型debiased lasso（高维半参数推断）、个性化治疗规则最优设计（实验设计与因果优化）、函数型数据M型稳健估计（minimax效率）、小区域BELS预测量（二阶MSE估计，无正态假设）。此外，函数型协方差变点检测与扩散过程NW估计也属非参数/半参数理论推进。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1111/sjos.12605](https://doi.org/10.1111/sjos.12605) — General purpose multiply robust data integration procedures for handling nonprobability samples
- **作者**: Sixia Chen, David Haziza
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Oklahoma Health Sciences Center · University of Ottawa · Ottawa University
- **分类**: vol 50 · issue 2 · pp 697-724
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在概率样本与非概率样本数据整合框架下，目标是估计总体总量、均值、分布函数等参数，关键假设是参与概率的模型正确设定或结果回归模型的正确设定。作者提出一类 multiply robust estimator，同时融合多个 outcome regression 模型和多个 propensity score 模型，当所有模型中除一个外均被错误设定时，估计量仍保持一致性。理论贡献包括建立估计量的渐近正态性、推导方差估计量、证明在多个 working models 下的多重稳健性。模拟研究显示在模型误设情形下 bias 和 efficiency 的改善；实证分析使用韩国国家健康营养调查数据。对您在因果推断中处理 selection bias 和 missing data 问题有直接参考价值。
- **关键技术**: `multiply robust estimation`, `propensity score weighting`, `outcome regression`, `data integration`, `nonprobability sample`
- **为什么对您有用**: 本文直接连接到您 primary interest 中因果推断的 identification 与 estimation 理论，特别是 selection bias 调整和 semiparametric efficiency。multiply robust 估计量的构造与您熟悉的 semiparametric theory 和 influence function 方法高度相关，可用 very_familiar 的 semiparametric efficiency 理论分析其效率性质。**立即可做**：用您 very_familiar 的 semiparametric theory 工具，可以验证其声称的 multiply robustness 是否达到 semiparametric efficiency bound，或探索在 high-dimensional setting 下用 debiased ML 替代 parametric working models。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 1 篇)*

### 1. [10.1111/sjos.12592](https://doi.org/10.1111/sjos.12592) — Regularization in dynamic random‐intercepts models for analysis of longitudinal data
- **作者**: Amir‐Abbas Mofidian Naieni, Reyhaneh Rikhtehgaran
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Isfahan University of Technology
- **分类**: vol 50 · issue 2 · pp 513-549
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究纵向数据中动态随机截距模型（包含一阶滞后响应和随机效应）的同时变量选择与估计问题。该模型是处理重复测量数据的常用工具，随机效应刻画个体内相关，滞后响应处理时序相关。作者证明，若忽略随机效应与初始响应的相关性而直接使用条件似然进行正则化估计，会带来有偏性。相比之下，对初始响应与后续观测进行联合建模，所得的正则化估计量（如LASSO、自适应LASSO等）在低维和高维设定下均具备参数估计的一致性和变量选择的Oracle性质。理论分析涵盖了正则化一致性的条件估计量以及高维情形下稀疏性恢复的渐近性质。模拟研究和真实数据分析验证了所提方法的有限样本表现。对于您在高维统计和纵向数据分析方面的兴趣，本文提供了一种在高维框架内处理复杂相关结构的正则化思路，并且其证明技术可迁移至其他涉及动态结构的估计问题。
- **关键技术**: `regularized estimation (LASSO, Adaptive LASSO)`, `dynamic random-intercepts model`, `Oracle property`, `joint modeling of initial conditions`, `high-dimensional asymptotic theory`
- **为什么对您有用**: 本文直接涉及您 primary interest 中的“高维统计”（高维正则化估计与Oracle性质证明），您可用非常熟悉的“高维渐近”工具审视其定理假设与证明严谨性，这是立即可做的。同时，该动态随机截尾模型在流行病学纵向研究中具有应用潜力，可作为您进入流行病学应用的敲门砖。整体而言，这是一篇方法学扎实、与您高维统计方向高度契合的论文。

## 非参数 / 半参数  *(nonparam_semipara, 8 篇)*

### 1. [10.1111/sjos.12593](https://doi.org/10.1111/sjos.12593) · [arXiv](https://arxiv.org/abs/2105.06884) — Nadaraya–Watson estimator for I.I.D. paths of diffusion processes
- **作者**: Nicolas Marie, Amélie Rosier
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 589-637
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 本文研究扩散过程的漂移函数非参数Nadaraya-Watson估计。设定为独立同分布的连续扩散路径观测，目标是估计漂移函数。作者建立了估计器及其离散时间近似的风险界（均方误差上界），覆盖了L^2和L^∞范数。方法上，沿用标准NW核估计器，但针对扩散过程的再生核Hilbert空间结构推导了新的浓度不等式。同时，将PCO和留一交叉验证带宽选择方法扩展到该设定。数值实验验证了理论结果。对您而言，该工作将经典非参数回归估计推广到连续时间随机过程，与您的非参数统计兴趣直接相关。
- **关键技术**: `Nadaraya–Watson estimator`, `nonparametric drift estimation`, `diffusion processes`, `risk bounds`, `cross-validation bandwidth selection`
- **为什么对您有用**: 本文连接您的非参数统计子方向，特别是核估计在连续时间过程上的推广。技术武器库中“非参数统计”非常适合评估该方法风险界的最优性（如minimax下界对比）。Follow-up：中期可做——需先在“扩散过程随机分析”上长肌肉才能深入该理论，但作为入门阅读已足够。

### 2. [10.1111/sjos.12595](https://doi.org/10.1111/sjos.12595) · [arXiv](https://arxiv.org/abs/2106.03244) — Statistical inference for Cox proportional hazards models with a diverging number of covariates
- **作者**: Lu Xia, Bin Nan, Yi Li
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 550-571
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对协变量维数发散（p 随 n 增长）的 Cox 比例风险模型，提出一种改进的 debiased lasso 推断方法。现有 debiased lasso 通常要求 Fisher 信息矩阵的逆稀疏，该假设在 Cox 模型下常被违反，导致置信区间覆盖不足。新方法通过求解一系列二次规划问题直接近似逆信息矩阵，无需稀疏性假设。在 p 发散条件下，建立了回归系数估计的渐近正态性与一致性。模拟实验表明估计量偏差小，置信区间覆盖接近名义水平。最后将方法应用于波士顿肺癌生存队列数据，评估遗传标记对总生存期的影响。本文与您在高维半参数推断（Cox 模型）和 debiased lasso 理论方面的兴趣直接相关，尤其连接了半参数效率和稳健推断的需求。
- **关键技术**: `debiased lasso`, `Cox proportional hazards model`, `diverging number of covariates`, `quadratic programming inverse approximation`, `high-dimensional inference`
- **为什么对您有用**: 本文关注高维 Cox 模型下逆信息矩阵近似问题，属于半参数理论和高维统计的交汇点。您的技术武器库中 'high-dimensional asymptotics' 和 'semiparametric theory'（moderately_familiar）可直接用于评估其渐近论证的严谨性和效率最优性。基于您对高维渐近的熟悉程度，可立即着手理解方法细节，并对比现有 debiased lasso 理论。

### 3. [10.1111/sjos.12610](https://doi.org/10.1111/sjos.12610) — Nonparametric asymptotic confidence intervals for extreme quantiles
- **作者**: Laurent Gardes, Samuel Maistre
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Centre National de la Recherche Scientifique · Université de Strasbourg
- **分类**: vol 50 · issue 2 · pp 825-841
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究重尾分布下极值分位数（超出数据范围的分位数）的非参数渐近置信区间构造问题，目标 estimand 是位于数据支撑之外的 quantile，关键假设是分布满足二阶正则变化条件。核心方法不采用传统的 pivotal quantity 路线，而是基于均匀分布次序统计量的分布性质，通过构造与均匀次序统计量相关的统计量来建立置信区间。理论贡献是在二阶条件下证明了覆盖概率收敛到名义水平，给出了渐近有效性保证。实证部分通过模拟和真实数据集验证了有限样本表现。对您在非参数理论和极值统计方向的兴趣有直接参考价值。
- **关键技术**: `order statistics distribution`, `second-order regular variation`, `heavy-tailed distribution`, `extreme quantile estimation`, `nonparametric confidence interval`, `coverage probability convergence`
- **为什么对您有用**: 本文属于非参数理论范畴，涉及次序统计量的精确分布和二阶正则条件下的渐近理论，与您 very_familiar 的非参数统计和 minimax bounds 直接相关。技术切入点：可以用您熟悉的 minimax 理论审视其置信区间的 rate-optimality，或用 higher-order U-statistics 视角分析次序统计量相关估计量的高阶渐近性质。follow-up 判定：立即可做——武器库中的非参数理论和 minimax 方法足以展开对极值分位数估计效率边界的理论分析。

### 4. [10.1111/sjos.12586](https://doi.org/10.1111/sjos.12586) · [arXiv](https://arxiv.org/abs/2008.00782) — Robust optimal estimation of location from discretely sampled functional data
- **作者**: Ioannis Kalogridis, Stefan Van Aelst
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 411-451
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究函数型数据中位置参数的稳健估计问题，目标是在离散采样且存在测量误差的设定下估计均值函数。现有方法大多假设完全观测轨迹且缺乏对异常值的鲁棒性，该文首次提出一类基于M型平滑样条的位置估计器，适用于常见观测和独立观测两种轨迹结构。该方法结合了重复测量数据和稳健损失函数，能够在测量误差存在时保持一致性。理论部分证明，在适当的正则性条件下，所提估计量族在minimax意义下达到最优收敛速率。数值模拟和基于COVID-19数据的实证分析展示了其在有限样本下的稳健性和实用性。本文对非参数估计的minimax理论和稳健M估计的结合进行了系统研究，对您在semiparametric & nonparametric theory方向下的函数型数据分析子领域具有参考价值。
- **关键技术**: `M-type smoothing spline`, `minimax rate optimality`, `robust estimation`, `functional data analysis`, `discrete sampling`, `measurement error`
- **为什么对您有用**: 本文连接您primary interests中的'semiparametric and nonparametric theory'子方向——函数型数据的位置估计问题。技术层面上，您武器库中'very_familiar'的'minimax bounds for estimation problems'可直接用于验证本文minimax率是否紧，'nonparametric statistics'和'high-dimensional asymptotics'可帮助理解其渐近论证。follow-up粗判为立即可做：基于您对非参数统计和minimax bound的熟悉程度，可以立即评估该方法能否推广到其他损失函数或相关设定。

### 5. [10.1111/sjos.12611](https://doi.org/10.1111/sjos.12611) — On the robustness to outliers of the Student‐t process
- **作者**: J. Ailton A. Andrade
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Universidade Federal do Ceará
- **分类**: vol 50 · issue 2 · pp 725-749
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文在贝叶斯非线性回归框架下，以Student-t过程替代高斯过程，利用正则变化理论（regular variation）系统分析模型对输入异常值、输出异常值及两者同时存在时的鲁棒性。作者证明在特定条件下，当异常值趋于无穷时，后验分布收敛到不依赖于异常信息的极限分布，从而从数学上确认了Student-t过程自动拒绝离群值的能力。除了后验分布，论文还推导了预测后验分布的极限行为，并通过模拟加以验证。这项理论工作为贝叶斯鲁棒回归提供了严格的渐近基础，不同于以往侧重计算的研究。对您而言，本文展示了正则变化在非参数回归鲁棒性分析中的威力，可能为半参数推断中的稳健性处理提供新的视角，但需深入理解贝叶斯框架和正则变化工具。
- **关键技术**: `Regular variation theory`, `Student-t process`, `Posterior robustness`, `Nonlinear regression`, `Bayesian nonparametrics`
- **为什么对您有用**: 本文与您的非参数统计兴趣（nonparametric statistics）直接相关，聚焦于鲁棒回归的理论性质。但论文采用贝叶斯框架和正则变化工具，而您武器库中的频率学派工具（如minimax界、U-统计量）并未直接适用；若要在此方向深入，需先掌握正则变化理论（目前不在武器库中），因此暂不可做直接的问题发现。不过，文中关于后验鲁棒性的结论可作为扩展知识，帮助理解鲁棒性的另一种数学表述。

### 6. [10.1111/sjos.12589](https://doi.org/10.1111/sjos.12589) · [arXiv](https://arxiv.org/abs/2006.13887) — Break point detection for functional covariance
- **作者**: Shuhao Jiao, Ron D. Frostig, Hernando Ombao
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 477-512
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在函数型数据分析框架下，研究零均值函数型数据的协方差算子变点检测问题，目标是识别协方差结构发生突变的时间点。方法基于 CUSUM 统计量构造检测程序，核心挑战在于零分布依赖于无穷多未知参数，实际检验只能纳入有限参数，文章系统分析了参数截断数目对检验功效与 size 的影响。理论贡献包括：建立了变点估计量的一致性收敛速率，推导了检验统计量的渐近分布，并刻画了参数数目选择对 finite-sample performance 的影响。模拟与大鼠脑信号（中风实验）数据验证了方法的有效性。对您在 longitudinal / brain signal 等函数型数据的假设检验与变点检测有直接参考价值。
- **关键技术**: `CUSUM statistics`, `functional principal component analysis`, `covariance operator change point`, `asymptotic distribution theory`, `parameter truncation analysis`
- **为什么对您有用**: 连接到 nonparametric theory 与 hypothesis testing 的交叉领域，具体是函数型数据的协方差算子推断。您 very_familiar 的 minimax bounds 与 nonparametric statistics 可用于分析该 CUSUM 检验的最优性（如 detection boundary 是否 sharp）；moderately_familiar 的 M-estimation theory 可用于审视其变点估计的收敛速率是否可达 semiparametric efficiency bound。**立即可做**：用熟悉的 minimax / nonparametric 工具检验其声称的收敛速率是否紧、参数截断的 tradeoff 是否有更精细的理论刻画。

### 7. [10.1111/sjos.12596](https://doi.org/10.1111/sjos.12596) — Benchmarked linear shrinkage prediction in the Fay–Herriot small area model
- **作者**: Kentaro Chikamatsu, Tatsuya Kubokawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Japan University of Economics · The University of Tokyo
- **分类**: vol 50 · issue 2 · pp 572-588
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在 Fay–Herriot 小区域估计模型下，目标是构造满足整体区域约束（benchmarking constraint）的小区域均值预测量，且不依赖随机效应和抽样误差的正态性假设。作者提出 benchmarked empirical linear shrinkage (BELS) predictor，通过数据驱动的系数调整实现 EBLUP 的 benchmarking，使各小区域预测值之和等于大区域的直接估计。核心贡献包括：在无正态假设下推导 BELS 的二阶无偏 MSE 估计量，采用解析修正消除偏差。理论结果给出了 MSE 估计的渐近性质，Monte Carlo 模拟验证了有限样本表现。对您有用：涉及 shrinkage estimation 的二阶矩理论，与 semiparametric efficiency 和 M-estimation 理论有方法学连接。
- **关键技术**: `Fay–Herriot model`, `empirical best linear unbiased predictor`, `linear shrinkage estimation`, `benchmarking constraint`, `second-order unbiased MSE estimation`, `analytical bias correction`
- **为什么对您有用**: 本文属于小区域估计中的 shrinkage estimation 与二阶推断问题，连接到您 primary interest 中的 semiparametric theory（二阶无偏 MSE 估计）和 efficiency theory。您武器库中 very_familiar 的 minimax bounds for estimation 和 moderately_familiar 的 M-estimation theory 可直接用于分析 BELS 的渐近效率与二阶性质。**立即可做**：用 M-estimation 理论框架审视其 MSE 估计量的二阶无偏性证明，或探索在更弱矩假设下的效率界。

### 8. [10.1111/sjos.12613](https://doi.org/10.1111/sjos.12613) · [arXiv](https://arxiv.org/abs/2103.02310) — Asymptotic approximation of the likelihood of stationary determinantal point processes
- **作者**: Arnaud Poinas, Frédéric Lavancier
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 842-874
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 在连续 determinantal point processes (DPPs) 的平稳设定下，目标是基于观测窗口 $W$ 上的点模式对模型参数进行极大似然估计，但精确似然的计算涉及高维行列式求逆，计算代价过高。本文提出一种基于渐近展开的似然近似方法：当观测窗口 $W \uparrow \mathbb{R}^d$ 时，利用 DPP 的谱表示和 Fourier 变换性质，将似然函数近似为仅依赖谱密度的积分形式，避免了矩阵求逆。该方法不限于矩形窗口、无需调参、计算速度优于现有 Fourier 级数近似，并给出了估计量的渐近方差显式公式。理论部分证明了近似似然估计的相合性和渐近正态性，模拟显示在标准参数模型上优于对比方法。对您而言，这是空间点过程参数推断中计算与理论结合的范例，涉及谱方法和渐近展开，与您在 semiparametric theory 和 statistical computing 方面的兴趣有方法学交叉。
- **关键技术**: `determinantal point processes`, `spectral representation`, `asymptotic likelihood approximation`, `Fourier transform methods`, `Whittle likelihood`, `stationary point processes`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric theory（渐近方差显式公式、influence function 类似结构）和 statistical computing（数值方法替代高维矩阵运算）。从 technical_arsenal 角度，您 very_familiar 的 minimax bounds 和 high-dimensional asymptotics 可用于分析该近似估计量的效率损失；moderately_familiar 的 semiparametric theory 可帮助理解其 influence function 结构。**中期可做**：若想进入空间点过程领域，需先在 moderately_familiar 的 semiparametric theory 上补充点过程特定的谱分析方法；若仅关注计算-统计 tradeoff 思路，则可直接迁移到您熟悉的 causal inference 或高维推断问题中。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1111/sjos.12614](https://doi.org/10.1111/sjos.12614) · [arXiv](https://arxiv.org/abs/2102.11253) — Large‐scale simultaneous inference under dependence
- **作者**: Jinjin Tian, Xu Chen, Eugene Katsevich, Jelle Goeman, Aaditya Ramdas
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 750-796
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究在假设依赖结构下的大规模同时推断问题，目标是构造 post hoc 真发现数（true discoveries）的有效置信下界。核心框架基于 closed testing，作者聚焦于一类特殊形式的 local test——对个体假设检验分数之和的函数进行阈值化，并据此提出新的统计量来量化多重性调整的代价。在计算方面，针对这类 local test 设计了快速算法（多为线性时间），解决了 closed testing 通常面临的组合爆炸问题。结合近期基于广义均值的 global null 检验进展，本文方法可处理多种依赖结构和信号构成。理论部分分析了不同 local test 的保守性和敏感性，模拟研究验证了 local test 与完整 closed testing 的类似表现。对您有用：这是 multiple testing 领域的系统方法论文，与您 primary interest 中的 hypothesis testing 直接相关。
- **关键技术**: `closed testing`, `post hoc inference`, `true discovery proportion`, `generalized mean tests`, `linear-time algorithms`, `simultaneous inference`
- **为什么对您有用**: 直接对应您 primary interest 中的 hypothesis testing 子方向，涉及 multiple testing 的 admissibility 理论（closed testing 的必要性）和计算效率问题。您武器库中的 minimax bounds 和 high-dimensional asymptotics 可用于分析所提方法在稀疏信号设定下的 power 性质——这是立即可做的方向。若要深入 closed testing 的 admissibility 理论，需在 moderately_familiar 的 semiparametric theory 上补充一些 testing 方向的文献。

### 2. [10.1111/sjos.12623](https://doi.org/10.1111/sjos.12623) — Selection of linear mixed‐effects models for clustered data
- **作者**: Chih‐Hao Chang, Hsin‐Cheng Huang, Ching‐Kang Ing
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: National University of Kaohsiung · National Kaohsiung University of Applied Sciences · Institute of Statistical Science, Academia Sinica · National Tsing Hua University
- **分类**: vol 50 · issue 2 · pp 875-897
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文研究线性混合效应模型（LME）在聚类结构下的模型选择问题，目标是在条件 Kullback-Leibler（CKL）损失下实现渐近有效性。作者提出条件广义信息准则（CGIC），通过将经验最佳线性无偏预测（EBLUP）代入随机效应并配合最大似然估计来估计 CKL 损失。核心难点在于随机效应方差的选择——当聚类数 g 固定不随样本量增长时，方差参数不可一致估计，传统方法失效。通过 CKL 风险的新型分解，证明 CGIC 在 g 固定或 g→∞ 两种情形下均能同时达到选择一致性和渐近损失有效性。模拟实验验证了理论结果。对您在 semiparametric efficiency 和 M-estimation 理论方面的兴趣有直接参考价值。
- **关键技术**: `conditional Kullback-Leibler loss`, `empirical BLUP`, `generalized information criterion`, `asymptotic loss efficiency`, `random effects selection`, `risk decomposition`
- **为什么对您有用**: 本文的核心贡献是在参数不可一致估计的困难情形下（g 固定），通过风险分解技术证明信息准则仍能达到渐近有效性，这与您在 semiparametric efficiency bounds 和 M-estimation theory 方面的兴趣直接相关。您武器库中的 M-estimation theory（moderately_familiar）可以用来审视其 CGIC 的渐近性质证明是否可推广到更一般的损失函数或更复杂的随机效应结构。**中期可做**：需先在 semiparametric theory 上加深（特别是 efficiency theory 在参数边界情形的处理），然后可考虑将类似的信息准则框架推广到 semiparametric 模型的变量选择问题。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.1111/sjos.12597](https://doi.org/10.1111/sjos.12597) — Continuous‐time threshold autoregressions with jumps: Properties, estimation, and application to electricity markets
- **作者**: Daniel Lingohr, Gernot Müller
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Augsburg
- **分类**: vol 50 · issue 2 · pp 638-664
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 该文在连续时间阈值自回归(CTAR)模型框架中引入跳跃成分，旨在处理金融与电力市场中频繁出现的价格跳跃现象。证明了带跳跃的CTAR过程存在唯一弱解，并给出Euler近似方案在弱意义下的相合性。由于似然函数无显式形式，采用基于核的粒子滤波进行参数估计，通过模拟实验验证了估计量的有限样本表现。将模型拟合至德国物理电力指数(PHELIX)的实证分析显示，较之传统高斯CTAR，该模型能更准确地捕捉数据的尖峰与跳跃特征。对您而言，本文是统计计算(粒子滤波)在非线性时间序列中的应用实例，可作为统计计算工具箱的参考；同时作为能源经济学的模型应用，与您对经济理论方向的关注相符。
- **关键技术**: `Continuous-time threshold autoregression`, `Jump processes`, `Euler approximation`, `Kernel-based particle filtering`, `Regime switching model`
- **为什么对您有用**: 本文涉及非线性时间序列模型的估计方法，其中核粒子滤波属于统计计算范畴，可连接您对该方向的兴趣。但该模型非因果推断或高维问题，您的技术武库中‘M-estimation’和‘非参数统计’可为分析其渐近性质提供思路，但粒子滤波具体实现需补充‘序列蒙特卡洛’知识，属‘暂不可做’范围——核心机器不在武器库里。整体而言，作为经济时间序列的应用阅读，可帮助您了解电力市场数据的结构，但非方法学突破。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.12621](https://doi.org/10.1111/sjos.12621) · [arXiv](https://arxiv.org/abs/2102.07093) — Optimal designs for the development of personalized treatment rules
- **作者**: David Azriel, Yosef Rinott, Martin Posch
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 797-824
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文研究多臂平行组临床试验的最优设计，目标是估计个性化治疗规则（PTR），即在给定协变量下为患者选择最佳治疗。设定为各处理臂响应服从同方差线性模型（臂间方差可不同），受试者来自非选择性总体的随机样本；作者优化（可能随机化的）处理分配，允许分配率依赖于协变量。核心方法是 D-optimal 设计框架下的分配率优化，推导了使估计方差最小化的分配规则，并给出理论最优解的显式形式。主要理论发现：两处理臂情形下，近似最优分配规则不依赖协变量取值，仅依赖各臂响应方差；三处理臂及以上情形，最优分配依赖协变量值及真实回归系数。文中用一项饮食临床试验数据展示方法。对您而言，这是最优实验设计在因果推断个性化决策场景的应用，方法学 novelty 属于经典最优设计框架的扩展。
- **关键技术**: `D-optimal design`, `treatment allocation optimization`, `personalized treatment rules`, `homoscedastic linear model`, `multi-armed clinical trial`
- **为什么对您有用**: 连接到因果推断中个性化治疗规则的估计问题，但核心是最优实验设计而非 identification/estimation 理论。武器库中 minimax bounds 和 estimation theory 可用于验证其声称的 optimality 是否紧，但本文不涉及 semiparametric efficiency 或 debiased ML 等您熟悉的效率理论工具。**中期可做**：若想进入最优设计领域，需先在 moderately_familiar 的 M-estimation 理论基础上补充 experimental design 的经典文献（如 Fedorov、Kiefer 的最优设计理论）。

### 2. [10.1111/sjos.12604](https://doi.org/10.1111/sjos.12604) · [arXiv](https://arxiv.org/abs/2107.00134) — The geometry of Gaussian double Markovian distributions
- **作者**: Tobias Boege, Thomas Kahle, Andreas Kretschmer, Frank Röttger
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 2 · pp 665-696
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文研究高斯双马尔可夫分布族，该分布族由一对图同时约束协方差矩阵及其逆矩阵中的零元素。作者系统刻画了这些模型的半代数几何性质，包括维数公式、光滑性判别条件、以及连通性结构。利用代数组合工具，证明了所有合法图对对应的模型都是连通的，并在一般位置下是光滑的。文章还给出了模型的隐维数与图结构之间的显式关系，以及一些不可约分解的结果。本质上这是一篇代数统计与图模型理论的交叉工作，与您的因果推断或高维统计等主要方向直接关联较弱。如果您关注图模型的基础理论，可作为了解双马尔可夫模型性质的参考。
- **关键技术**: `semi-algebraic geometry`, `graphical models`, `Gaussian double Markovian models`, `dimension formula`, `connectedness`, `algebraic statistics`
- **为什么对您有用**: 本文主题为图模型的代数几何理论，不属于您的任何主要或次要兴趣方向。技术武器库中的非参数统计、高维渐近、U统计等工具均不直接适用于本文内容，因此无法形成现成的follow-up问题。如果您不从事图模型或代数统计的研究，此文的阅读价值有限。

### 3. [10.1111/sjos.12588](https://doi.org/10.1111/sjos.12588) — Prior distributions expressing ignorance about convex increasing failure rates
- **作者**: Jørund Gåsemyr, Aliaksandr Hubin
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: OsloMet – Oslo Metropolitan University · University of Oslo
- **分类**: vol 50 · issue 2 · pp 452-476
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文在贝叶斯框架下研究如何为离散化（如年度）失败率或死亡率设定表示无知（noninformative）的先验分布，假设这些率已知为递增且凸。作者指出早期工作中使用的均匀先验不令人满意，尤其因为它对时间尺度选择敏感，导致后验不具尺度不变性。他们提出基于Dirichlet分布在相关凸集极点上分配权重的替代先验，并探讨了尺度中性（scale neutrality）对Dirichlet参数选择的约束。通过理论推导和数值示例，展示了所提先验在表达“完全无知”方面的合理性。该方法融合了凸几何、序约束先验和贝叶斯非参数思想。结果对可靠性工程和流行病学中的死亡率建模有一定参考价值，但与您以频率学派和因果推断为主的研究方向关联较弱。
- **关键技术**: `Dirichlet distribution`, `noninformative priors`, `convex increasing functions`, `extreme points of convex sets`, `scale invariance`
- **为什么对您有用**: 本文涉及非参数贝叶斯先验构造，与您'非参数统计'兴趣方向（凸函数上的先验设定）有边际交集，但您的技术武器库中缺乏贝叶斯非参数核心工具（如Dirichlet过程后验采样），因此暂无法直接应用其结果。如果未来您需要处理序约束下的贝叶斯推断（如流行病学中的单调死亡率曲线），可作为入门读物，但当前阶段不具紧迫性。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

