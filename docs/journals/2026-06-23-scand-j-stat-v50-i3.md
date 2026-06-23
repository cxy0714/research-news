# Scand. J. Stat. — Vol 50  Issue 3  ·  2026-06-23

- 共 24 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 24 篇全部抓到（对照 OpenAlex 29 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Scandinavian Journal of Statistics第50卷第3期共24篇论文，整体可以聚合为五条主线：**半参数效率与因果推断**（包括状态占用概率的targeted估计、缺失数据的准随机化估计、协变量平衡的Bregman距离框架勘误、change-plane Cox模型中的平滑部分似然）、**高维与变量选择**（高维广义线性模型块缺失变量选择、稳健Sure Independence Screening、高维Gibbs点过程推断、高维时间序列监控、基于混合先验的BIC变体）、**贝叶斯非参数与逆问题**（Hilbert空间中heterogeneous方差逆问题、非高斯平稳时间序列谱密度的后验一致性、aoristic数据的贝叶斯状态估计）、**假设检验与统计证据**（基于可能性理论的surprise度量、极值理论异常值检测、变换序与统计泛函单调性）、以及**统计计算与网络模型**（自适应重要性采样Daisee、空间bootstrap预测、纵向网络Markov链、多元各向异性Cox过程）。此外还有一篇分布式两样本U统计量、一篇envelope模型平均、一篇生存数据非线性降维（RDSIR）、一篇序数分类、一篇stepped wedge设计信息量推广，各自独立成题。

**半参数效率与因果推断**是本期最密集的方法论主线。Targeted estimation for non-Markov illness-death model在半参数效率理论框架下构造了一个估计量类——只要转移强度估计量弱正则，所有该类估计量均渐近线性，允许使用惩罚似然等自适应方法拟合转移强度，最终通过Aalen-Johansen或逆概率加权得到状态占用概率。Robust quasi-randomization-based estimation for missing data在cell-homogeneous response假设下提出子抽样Rao-Blackwell估计量，允许对outcome使用任意多个机器学习模型而无须正确指定工作模型，实现无偏估计——这与效率理论中的双稳健思路形成对比，更强调随机化假设而非模型正交性。Errata for Bregman distance covariate balance框架修正了原文效率界证明和hdCBPS描述中的疏漏。Change-plane Cox model采用最大平滑部分似然，证明了分类参数接近n^{-1/2}的收敛速度和回归参数渐近正态性，为子组分析中的非光滑参数推断提供了严格渐近理论。

**高维与变量选择**方面，Variable selection for high-dimensional GLM with block-missing data利用块缺失结构估计稀疏精度矩阵后进行条件均值插补，再执行变量选择，大样本下证明一致性，且对MAR/MCAR稳健。Robust sure independence screening for nonpolynomial dimensional GLM基于最小密度幂散度估计(MDPDE)替代边际似然，在异常值污染下仍满足确定筛选性质，且推广到条件筛选。Inference for low- and high-dimensional inhomogeneous Gibbs point processes是首个将LASSO/SCAD/MCP正则化系统引入空间点过程伪似然的工作，同时覆盖低维和高维渐近理论。Sequential monitoring of high-dimensional time series提出基于欧几里得距离的EWMA控制图，避免逆协方差矩阵计算，适用于p>>n场景。Consistent Bayesian information criterion via mixture prior通过先验混合结构同时继承AIC的渐近效率与BIC的一致性，在高维线性回归中证明了变量选择一致性。

对因果推断方向最相关的是Targeted estimation for non-Markov illness-death model（半参数有效估计与效率界）、Robust quasi-randomization-based estimation with ensemble learning for missing data（缺失数据下的无偏估计策略）以及Errata for Bregman distance covariate balance framework（协变量平衡的理论修正）。半参数效率方向还可关注Change-plane Cox model（非光滑参数收敛速度）和Frequentist model averaging for envelope models（交叉验证模型平均的渐近最优性）。高维方向优先看Variable selection for high-dimensional GLM with block-missing data和Robust sure independence screening for nonpolynomial dimensional GLM，它们分别处理缺失和异常值下的变量选择一致性问题。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.12626](https://doi.org/10.1111/sjos.12626) — Robust quasi‐randomization‐based estimation with ensemble learning for missing data
- **作者**: Danhyang Lee, Li‐Chun Zhang, Sixia Chen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Alabama · Statistics Norway · University of Southampton · University of Oklahoma Health Sciences Center
- **分类**: vol 50 · issue 3 · pp 1263-1278
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在缺失数据框架下，目标是估计总体均值，关键假设是 cell-homogeneous response（即同一协变量单元内的响应机制同质）。本文提出 robust quasi-randomization-based estimator，允许对 outcome 使用任意多个 semiparametric / nonparametric / machine learning 模型，通过 subsampling Rao–Blackwell 方法实现无偏性——只要 cell-homogeneous response 成立，无论 outcome working models 是否正确指定，估计量均无偏。理论贡献包括：证明估计量的无偏性、提出无需 jackknife/bootstrap 的无偏方差估计公式。模拟研究显示该方法在模型误设场景下优于现有 multiply robust 估计量。对您在因果推断中处理 missing data / selection bias 问题有直接参考价值。
- **关键技术**: `multiply robust estimation`, `Rao-Blackwellization`, `quasi-randomization`, `cell-homogeneous response assumption`, `semiparametric efficiency`, `ensemble learning`
- **为什么对您有用**: 直接连接因果推断中的缺失数据与 selection bias 问题，属于 DR/MR 估计量的扩展工作。您熟悉的 semiparametric theory 和 minimax bounds 可用于分析该估计量的 efficiency 性质——文中未讨论 efficiency bound，这是一个可切入的理论口子。**中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，验证该估计量是否达到 semiparametric efficiency bound，或构造 sharper rate 的替代方案。

### 2. [10.1111/sjos.12657](https://doi.org/10.1111/sjos.12657) — Errata for “A framework for covariate balance using Bregman distances”
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1552-1552
- 相关性 0/10 · novelty: `minor`
- **摘要**: 本文是对原文《A framework for covariate balance using Bregman distances》（Scandinavian Journal of Statistics, 2023）的勘误。原文提出基于Bregman距离的协变量平衡框架，并发展了CBPS（协变量平衡倾向得分）的高维版本hdCBPS。勘误修正了三处错误：第一，在线补充材料中关于效率界（efficiency bound）的证明存在疏漏，已更正；第二，第（26）式第二个约束条件的右侧错误地包含了一个多余的qi项，应删除；第三，第5.2节对hdCBPS方法的描述不够准确，应改为“使用正则化回归技术以得到潜在结果均值的去偏估计”。修正后的hdCBPS描述更好地反映了其通过正则化回归实现去偏估计的核心思想。这篇勘误对使用CBPS方法进行因果推断的研究者具有参考价值，确保方法论的准确性。
- **关键技术**: `covariate balancing propensity score (CBPS)`, `Bregman distance`, `efficiency bound`, `high-dimensional CBPS`, `regularized regression`
- **为什么对您有用**: 本文直接关联到因果推断中的协变量平衡方法（CBPS），属于您的主要兴趣方向。虽为勘误，但修正了效率界证明和hdCBPS描述，对确保方法正确性有实际意义。武器库中的'causal inference estimation theory'足以理解修正后的证明；这是一篇简单的勘误，立即可读，无需额外准备。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 4 篇)*

### 1. [10.1111/sjos.12632](https://doi.org/10.1111/sjos.12632) — Variable selection for high‐dimensional generalized linear model with block‐missing data
- **作者**: Yifan He, Yang Feng, Xinyuan Song
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Chinese University of Hong Kong · New York University
- **分类**: vol 50 · issue 3 · pp 1279-1297
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对多块缺失数据下的高维广义线性模型变量选择问题，提出一种基于单一回归的插补算法。该方法首先利用块缺失结构估计稀疏精度矩阵，然后基于观测块对缺失块进行条件均值插补。在广义线性模型框架下，建立了变量选择和参数估计的一致性理论。模拟研究显示，该插补方法对多种缺失机制（如MAR、MCAR）具有稳健性，优于现有仅适用于单块缺失或依赖模型结构的方法。最后，在阿尔茨海默病神经影像学倡议（ADNI）数据上验证了其实用性。本文对高维统计中缺失数据与变量选择的交叉研究有参考价值。
- **关键技术**: `regression imputation`, `sparse precision matrix estimation`, `block-wise missing data`, `high-dimensional generalized linear model`, `variable selection consistency`
- **为什么对您有用**: 本文涉及高维广义线性模型变量选择与块缺失数据处理，直接连接您对高维统计的兴趣。您的武器库中“高维渐近”工具可用于分析该插补方法的渐近性质（如一致性证明的验证与扩展），“软件开发”能力可复现并改进算法。从熟悉度看，块缺失的精度矩阵估计（graphical lasso）属于高维统计范畴，您已具备理解该方法的理论基础，可立即可做：读通全文后即可用已熟悉的非参与高维工具进行模拟复现或理论对比。

### 2. [10.1111/sjos.12628](https://doi.org/10.1111/sjos.12628) — Robust sure independence screening for nonpolynomial dimensional generalized linear models
- **作者**: Abhik Ghosh, Erica Ponzi, Torkjel Sandanger, Magne Thoresen
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Indian Statistical Institute · University of Oslo · UiT The Arctic University of Norway
- **分类**: vol 50 · issue 3 · pp 1232-1262
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对超高维广义线性模型（GLM）中的变量筛选问题，提出了一种基于最小密度幂散度估计（MDPDE）的稳健独立筛选方法（Robust SIS）。传统SIS方法对数据污染和噪声极其敏感，而MDPDE通过最小化数据分布与模型分布的α阶Rényi散度，获取对异常值具有鲁棒性的边际回归系数估计。作者从总体和样本两个层面证明了边际MDPDE的相合性，并证明了所提筛选算法满足确定筛选性质（sure screening property），即在超高维且模型阶数非多项式的设定下，以概率趋于1选出所有重要变量。进一步，他们还将方法拓展为稳健的条件筛选（conditional screening），同样证明了确定筛选性质。数值模拟和关于乳腺癌的流行病学真实数据分析表明，该方法在纯净数据和污染数据下均优于传统SIS及分位数SIS等稳健变体。对您而言，高维统计是主要研究兴趣之一，该稳健筛选方法可直接用于因果推断或流行病学研究中高维协变量的预筛选，特别是当数据可能存在测量误差或异常值时。
- **关键技术**: `Minimum density power divergence estimator (MDPDE)`, `Sure independence screening (SIS)`, `Marginal regression coefficients`, `Robust variable screening`, `Conditional screening`, `Ultra-high-dimensional GLM`
- **为什么对您有用**: 直接关联您对高维统计（主兴趣）的兴趣，特别是变量筛选在超高维设定下的稳健性问题。您熟悉的非参数统计与高维渐近理论可用于分析MDPDE的相合性和筛选性质（例如使用经验过程工具验证uniform consistency）。此外，实数据来自流行病学乳腺癌队列（流行病学为次要兴趣），且稳健筛选方法可用于因果推断中的预处理步骤（如倾向得分模型中的协变量选择）。从武器库角度看，这是可立即应用的方法（very_familiar中的高维渐近和估计论足以理解），且可与您熟悉的软件开发和因果推断估计论结合，在流行病学数据中复现或扩展。

### 3. [10.1111/sjos.12616](https://doi.org/10.1111/sjos.12616) — Inference for low‐ and high‐dimensional inhomogeneous Gibbs point processes
- **作者**: Ismaïla Ba, Jean‐François Coeurjolly
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Université du Québec à Montréal · Laboratoire Jean Kuntzmann · Université Grenoble Alpes
- **分类**: vol 50 · issue 3 · pp 993-1021
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文研究低维及高维非均匀Gibbs点过程的统计推断问题，目标是在协变量维数随观测区域增长时进行参数估计与变量选择。方法上，采用复合似然（特别是伪似然）结合凸和非凸惩罚函数（如LASSO、SCAD、MCP）的正则化估计。在空间点过程与惩罚函数的正则性条件下，证明了估计量的oracle性质、相合性与渐近正态性，结果同时覆盖低维情形，填补了文献空白。模拟实验验证了理论性质，并以热带森林数据集进行实例分析。该工作将高维正则化方法系统扩展到Gibbs点过程框架，连接了空间统计与高维推断。
- **关键技术**: `composite likelihood`, `pseudo-likelihood`, `nonconvex penalty (SCAD/MCP)`, `oracle property`, `high-dimensional spatial statistics`
- **为什么对您有用**: 本文属于高维统计方法在空间点过程模型中的推广，与研究者的primary interest（高维统计）直接相关，且其证明采用了M估计框架，对应你technical_arsenal中moderately_familiar的M估计理论，可借此加深对复合似然正则化方法在高维空间统计中渐近性质的理解。中期可做：将其中非凸惩罚的渐近理论与你熟悉的minimax界结合，检验Oracle性质是否在实际有限样本下最优；暂不可做，因为缺少与随机矩阵理论或U统计量的直接接口。

### 4. [10.1111/sjos.12607](https://doi.org/10.1111/sjos.12607) — Sequential monitoring of high‐dimensional time series
- **作者**: Rostyslav Bodnar, Taras Bodnar, Wolfgang Schmid
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: European University Viadrina · Stockholm University
- **分类**: vol 50 · issue 3 · pp 962-992
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对高维时间序列提出新型多元EWMA控制图。控制图基于欧几里得距离或仅用方差对角矩阵逆定义的距离，完全避免计算逆协方差矩阵，从而适用于p远大于n的高维场景。作者推导了控制统计量的分布性质（如均值、协方差、平稳分布），并利用这些性质设计控制限设定程序。通过大规模模拟研究，将新方法与基于马氏距离的经典EWMA控制图比较，展示其在检测均值偏移方面的表现。方法本质上是将传统多元质量监控推广至高维，但理论深度有限。
- **关键技术**: `EWMA control chart`, `Euclidean distance`, `diagonal variance matrix`, `high-dimensional time series`, `control limits design`, `simulation study`
- **为什么对您有用**: 本文属于高维统计在序贯监测中的应用，与您对高维统计的兴趣有部分交叉；您熟悉的high-dimensional asymptotics工具可直接评价其控制统计量的渐近性质，无需额外训练。但论文更偏向统计质量控制应用，缺乏随机矩阵理论或因果推断等您核心关注的深度，故建议作为背景浏览而非主攻对象。

## 非参数 / 半参数  *(nonparam_semipara, 5 篇)*

### 1. [10.1111/sjos.12622](https://doi.org/10.1111/sjos.12622) · [arXiv](https://arxiv.org/abs/1910.06914) — Bayesian inverse problems with heterogeneous variance
- **作者**: Natalia Bochkina, Jenovah Rodrigues
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Maxwell Institute for Mathematical Sciences
- **分类**: vol 50 · issue 3 · pp 1116-1151
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 本文研究 Hilbert 空间中带相关 Gauss 噪声的线性逆问题，目标是在 Sobolev 空间上推导后验收缩速率并与 minimax 速率比较。核心方法是 novel wavelet-based vaguelette–vaguelette approach，允许在不要求所有算子同时对角化的情形下应用序列空间方法，从而处理 fractional noise 与一般基/协方差算子。主要理论结果包括：(1) 在 mildly ill-posed 设定下证明后验收缩速率达到 minimax 最优；(2) 将方差的一致估计量 plug-in 后，后验收缩速率保持最优；(3) empirical Bayes 方法用 marginal likelihood 估计先验 scale，后验收缩速率自适应达到 minimax 最优。对您有用：这是 inverse problems 与 Bayesian nonparametrics 的经典工作，后验收缩速率与 minimax rate 的比较分析可直接迁移到您熟悉的 inverse problems with random noise 研究中。
- **关键技术**: `posterior contraction rate`, `minimax rate`, `wavelet-based vaguelette–vaguelette approach`, `empirical Bayes`, `marginal likelihood estimation`, `Sobolev space`
- **为什么对您有用**: (1) 直接连接到您 primary interest 中的 inverse problems with random noise，以及 semiparametric/nonparametric theory 中的 minimax bound 分析。(2) 您武器库中 very_familiar 的 minimax bounds for estimation problems 和 inverse problems with random noise 可以直接用来审视本文的速率紧性和证明技巧；moderately_familiar 的 semiparametric theory 可帮助理解 empirical Bayes plug-in 的理论机制。(3) **立即可做**：用 very_familiar 的 minimax bound 工具验证本文声称的 minimax optimality 是否紧，或尝试将 vaguelette–vaguelette 方法推广到您关心的其他噪声结构。

### 2. [10.1111/sjos.12635](https://doi.org/10.1111/sjos.12635) · [arXiv](https://arxiv.org/abs/1909.02243) — A new reproducing kernel‐based nonlinear dimension reduction method for survival data
- **作者**: Wenquan Cui, Jianjun Xu, Yuehua Wu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1365-1390
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 针对生存数据中的非线性降维问题，基于切片逆回归（SIR）和再生核希尔伯特空间（RKHS）理论，提出新方法RDSIR（RKHS-based Double SIR）。利用RKHS的等距同构性质，将RKHS中的非线性函数表示为特征空间中两个元素的内积，从而将非线性降维转化为线性问题。为处理生存数据中的删失偏差，采用双切片技术估计权重函数，通过广义特征分解估计非线性充分降维子空间。方法的渐近性质借助摄动理论建立，证明了估计量的相合性。数值实验表明，RDSIR与线性SDR方法性能相当，且能有效提取删失数据中的非线性结构。该方法为半参数降维增添了新工具，对您在半参数理论方向的方法论积累有参考价值。
- **关键技术**: `reproducing kernel Hilbert space`, `sliced inverse regression`, `nonlinear sufficient dimension reduction`, `double slicing`, `perturbation theory`, `generalized eigenvalue decomposition`
- **为什么对您有用**: 本文属于半参数与非参数理论中的充分降维方向，与您的 primary interest 中 semiparametric and nonparametric theory 高度吻合。您武器库中非常熟悉的 nonparametric statistics 和 high-dimensional asymptotics 可用于评估该方法的理论紧性（例如检验所给收敛速率是否最优）。由于您对生存数据的删失机制尚不熟悉，但核方法（RKHS）是 moderately_familiar 的工具，建议将本文列为中期可做——先补充生存分析中的逆概率删失加权（IPCW）知识，再考虑将 RDSIR 与您熟悉的因果推断降维任务结合。

### 3. [10.1111/sjos.12642](https://doi.org/10.1111/sjos.12642) · [arXiv](https://arxiv.org/abs/2109.14474) — Asymptotic properties of the maximum smoothed partial likelihood estimator in the change‐plane Cox model
- **作者**: Shota Takeishi
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1503-1531
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 该文研究change-plane Cox模型，用于生存数据的子组分析，其中分类基于多个协变量。目标是对分类参数（划分平面的方向）和回归参数进行估计，并建立渐近性质。作者提出最大平滑部分似然估计量，通过核平滑技术处理变化平面导致的非光滑似然问题。主要理论结果包括：分类参数的收敛速度可达到接近n^{-1/2}（除去对数因子），并给出了显式的上界；在此基础上，证明了回归参数的渐近正态性。证明依赖于经验过程理论和部分似然的局部展开。这些结果为半参数模型中的非光滑参数推断提供了严格的渐近理论。对您而言，该文直接联系到您对半参数与非参数理论的兴趣，分类参数的收敛速度可与您熟悉的minimax界和效率理论相连接，且平滑技巧可推广至因果推断中的子组效应分析。
- **关键技术**: `smoothed partial likelihood`, `change-point convergence rate`, `kernel smoothing`, `empirical process theory`, `asymptotic normality`, `semiparametric Cox model`
- **为什么对您有用**: 该文核心问题是半参数模型（Cox模型）中非光滑参数（变化平面）的推断，属于您的primary interest 'semiparametric and nonparametric theory'。文中分类参数的收敛速度上界可直接用您非常熟悉的'minimax bounds'工具验证最优性，且平滑部分似然思想可迁移至因果推断中的异质性处理效应估计（如subgroup analysis）。立即可做：利用非参数统计和最小化最优界来分析该收敛速率是否达到minimax最优。

### 4. [10.1111/sjos.12606](https://doi.org/10.1111/sjos.12606) — Sparse concordance‐based ordinal classification
- **作者**: Yiwei Fan, Jiaqi Gu, Guosheng Yin
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Beijing Institute of Technology · University of Hong Kong
- **分类**: vol 50 · issue 3 · pp 934-961
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在序数分类问题中，标签具有自然顺序，目标是正确预测实例的相对顺序。本文提出基于 concordance 函数的新方法，通过 penalized smoothed optimization 实现变量选择与稀疏性。在最大化 concordance 的分类规则集合内，通过最小化损失函数确定最优阈值进行标签预测。建立了估计量的渐近性质，证明了变量选择的一致性（selection consistency），并给出非参数类条件概率估计。模拟与实际数据分析显示该方法在分类准确率上具有稳健性和优势。对您而言，本文的 nonparametric estimation 与 M-estimation 渐近理论分析可作为 semiparametric theory 的应用实例参考。
- **关键技术**: `penalized smoothed optimization`, `concordance function`, `variable selection consistency`, `nonparametric conditional probability estimation`, `ordinal classification thresholds`
- **为什么对您有用**: 本文属于 nonparametric 与 M-estimation 理论范畴，涉及 selection consistency 证明与渐近性质推导。您可以用 very_familiar 的 nonparametric statistics 和 moderately_familiar 的 M-estimation theory 来审视其正则化条件与收敛率是否紧。**中期可做**：若想深入，需在 moderately_familiar 的 M-estimation theory 上加强，特别是 nonconvex penalized estimation 的渐近分析技巧。

### 5. [10.1111/sjos.12627](https://doi.org/10.1111/sjos.12627) · [arXiv](https://arxiv.org/abs/2103.01357) — Posterior consistency for the spectral density of non‐Gaussian stationary time series
- **作者**: Yifu Tang, Claudia Kirch, Jeong Eun Lee, Renate Meyer
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1152-1182
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文研究非高斯平稳时间序列谱密度的贝叶斯非参数估计的后验一致性问题。目标参数是谱密度 f(ω)，设定为 Bernstein–Dirichlet process 先验配合修正的 Whittle 似然，关键正则性假设包括谱密度的光滑性条件和时间序列的强混合性质。核心机制是将 J. K. Ghosal 等人关于相依数据与模型误设的一般后验一致性定理应用于非高斯情形，证明在 L₁ 距离下后验收缩到真实谱密度；作为特例，经典 Whittle 似然下的后验一致性也被推广到非高斯场景。技术工具包括 Whittle 似然近似、Bernstein 多项式先验的支撑性质、以及相依数据的经验过程理论。主要理论贡献是将此前仅适用于高斯时间序列的后验一致性结果扩展到更一般的非高斯平稳过程，填补了文献空白。对您而言，这是非参数贝叶斯理论与时间序列谱推断的交叉，可作为 semiparametric theory 中先验支撑与后验收缩的案例阅读。
- **关键技术**: `Bernstein–Dirichlet process prior`, `Whittle likelihood approximation`, `posterior consistency under misspecification`, `strong mixing conditions`, `spectral density estimation`, `Bayesian nonparametrics`
- **为什么对您有用**: 本文连接到 semiparametric and nonparametric theory 这一 primary interest，具体涉及贝叶斯非参数估计的后验一致性理论。您武器库中的 nonparametric statistics 和 minimax bounds for estimation problems 可用于审视本文的收敛率是否可达最优、后验收缩率是否与 frequentist minimax rate 匹配。follow-up 判定：**中期可做**——需先在 moderately_familiar 的 semiparametric theory 上加深对后验收缩率（posterior contraction rate）与先验支撑条件的理解，才能评估是否可将该框架推广到其他相依数据场景或改进收敛率。

## 效率理论 / Debiased ML  *(efficiency_dml, 1 篇)*

### 1. [10.1111/sjos.12644](https://doi.org/10.1111/sjos.12644) — Targeted estimation of state occupation probabilities for the non‐Markov illness‐death model
- **作者**: Anders Munch, Marie Skov Breum, Torben Martinussen, Thomas A. Gerds
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Copenhagen
- **分类**: vol 50 · issue 3 · pp 1532-1551
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 针对连续时间不可逆疾病‐死亡模型，研究状态占用概率（state occupation probabilities）的半参数有效估计。设定为非马尔可夫模型，允许转移强度函数完全非参数化，且考虑有／无基线协变量的两种场景。基于半参数效率理论推导出一个估计量类，其中任意估计量在转移强度函数估计量满足弱正则性条件下均为渐近线性——这一宽松条件使得数据自适应方法（如惩罚似然）可用于估计转移强度。为实现该类估计量，提出基于惩罚泊松回归的灵活方法估计各转移强度函数（0→1, 0→2, 1→2），再通过 Aalen‐Johansen 型或逆概率加权型估计得到状态占用概率。模拟和实际数据分析显示该估计量相较传统马尔可夫假设下的估计有更小的偏差，且方差接近半参数效率下界。本文对您的价值：它展示了半参数效率理论在流行病学多状态模型中的完整应用流程，您可将其视为将去偏机器学习思想拓展至竞争风险和慢性病病程估计的入口。
- **关键技术**: `semiparametric efficiency theory`, `asymptotically linear estimator`, `penalized Poisson regression`, `illness-death model`, `non-Markov model`, `Aalen-Johansen estimator`
- **为什么对您有用**: 直接连接您的半参数效率理论与流行病学应用子方向，文中推导的估计量类为理解您武器库中的『estimation theory in causal inference』如何迁移至非因果但结构相似的多状态模型提供了实例。您对『nonparametric statistics』和『M-estimation theory』的熟悉程度足以立即复现其实验框架（如模拟数据生成、用 penalized Poisson 估计强度），可快速验证方法的有限样本性质或尝试替换为其他数据自适应工具（如随机森林）。属于立即可做的阅读与实验入口。

## 数理统计 / 假设检验  *(hypothesis_testing, 4 篇)*

### 1. [10.1111/sjos.12648](https://doi.org/10.1111/sjos.12648) — Statistical evidence and surprise unified under possibility theory
- **作者**: David R. Bickel
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: The Graduate Center, CUNY · University of North Carolina at Greensboro
- **分类**: vol 50 · issue 3 · pp 923-928
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在经典假设检验框架下，本文针对复合假设的统计证据度量问题，将 p 值的 surprisal（以比特为单位的信息量）推广为 surprise（惊奇度），并统一到可能性理论中。Surprise 定义为条件 min-plus 概率，满足可能性理论公理体系，可量化数据对假设的否定程度。作者证明了 surprise 与 compatibility function 的等价性，并展示了其在复制危机、p 值先验调整等场景的应用。该工作为假设检验提供了新的理论工具，与您的数学统计与假设检验兴趣直接契合，可能启发设计具有直观解释的检验统计量。
- **关键技术**: `surprisal`, `surprise`, `possibility theory`, `conditional min-plus probability`, `compatibility function`, `p-value`
- **为什么对您有用**: 本文直接关联到您的主要兴趣——数学统计与假设检验，给出了基于可能性理论的统一证据度量框架。您可运用非参数统计知识分析 surprise 在非参数假设下的行为，或结合高维渐近理论探讨其在复杂模型中的性质。该框架有望用于因果推断中的敏感性检验，建议立即阅读。

### 2. [10.1111/sjos.12617](https://doi.org/10.1111/sjos.12617) · [arXiv](https://arxiv.org/abs/2208.09157) — Consistent Bayesian information criterion based on a mixture prior for possibly high‐dimensional multivariate linear regression models
- **作者**: Haruki Kono, Tatsuya Kubokawa
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1022-1047
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多元线性回归变量选择问题中，作者基于混合先验（平滑分布与delta分布的混合）推导了一类新的贝叶斯信息准则（BIC变体），该准则可视为AIC与BIC的融合。通过先验的混合结构，该准则同时继承了AIC的渐近效率（预测最优）和BIC的一致性（正确模型选择概率趋近1）。在大样本和高维（维度p随样本量n增长）渐近框架下均证明了变量选择的一致性。关键技术在于利用后验模型概率的Laplace近似导出可解析计算的准则形式。数值模拟展示了其在有限样本下优于传统AIC、BIC和EBIC的表现。该准则为高维线性回归提供了一种计算上简单且理论一致的变量选择工具，可直接应用于因果推断中的高维协变量筛选或假设检验中的多重比较场景。
- **关键技术**: `mixture prior`, `posterior model probability approximation`, `high-dimensional consistency`, `AIC-BIC fusion`, `variable selection consistency`
- **为什么对您有用**: 该论文直接针对高维线性回归的变量选择问题，属于高维统计和假设检验（模型选择）的核心方向，与研究者的primary interest匹配。研究者武器库中的“high-dimensional asymptotics”可用来评估该准则在更一般设定下的一致性速率，而“minimax bounds for estimation problems”可用于比较其变量选择的风险下界。立即可做：鉴于研究者熟悉高维渐近和模型选择，可以直接将该准则扩展到其他模型（如广义线性模型或因果推断中的倾向性得分回归）进行理论分析或仿真。

### 3. [10.1111/sjos.12629](https://doi.org/10.1111/sjos.12629) · [arXiv](https://arxiv.org/abs/2112.02383) — Transform orders and stochastic monotonicity of statistical functionals
- **作者**: Tommaso Lando, Idir Arab, Paulo Eduardo Oliveira
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1183-1200
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究统计泛函在随机序（stochastic order）下的单调性行为，聚焦于有限样本而非大样本性质。作者提出一类广义随机序族，称为变换序（transform orders），其定义基于分布函数的变换，并将经典的似然比序、失效率序、凸序等作为特例纳入统一框架。利用该框架，可以系统推导统计泛函（如广义熵、基尼系数及其推广）的随机单调性条件，例如泛函关于分布参数的单调性。方法的关键在于将泛函的变换与序关系的相容性转化为变换函数的单调性条件，从而避免逐例推导。应用方面，文章展示了如何利用变换序确定拟合优度检验中的最不利分布（least favorable distribution），并刻画bootstrap统计量的随机行为。对您而言，该工作直接关联假设检验的数学理论，尤其是最不利分布与检验规模的有限样本控制，可借助您熟悉的非参数统计工具（如经验过程）进一步推广至更复杂的检验情景。
- **关键技术**: `stochastic order`, `transform orders`, `least favorable distribution`, `bootstrap`, `Gini index`, `generalized entropy`
- **为什么对您有用**: 本文直接服务于数学统计中的假设检验方向，特别是有限样本下检验统计量的随机单调性和最不利分布问题，这是您 primary interests 中 'mathematical statistics (hypothesis testing)' 的具体子方向。您的武器库中 '非参数统计' 与 '估计的 minimax bound' 可用于系统评估变换序框架下泛函的识别性和检验的势函数，但核心工具——随机序的偏序理论与变换序的构造——目前不在您的武器库中。因此，阅读本文可作为进入该方向的 'gateway reading'，但短期内难以直接复现或改进其结果，属暂不可做。

### 4. [10.1111/sjos.12665](https://doi.org/10.1111/sjos.12665) — Outlier detection based on extreme value theory and applications
- **作者**: Shrijita Bhattacharya, Francois Kamper, Jan Beirlant
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Michigan State University · Stellenbosch University · ETH Zurich · Swiss Data Science Center · École Polytechnique Fédérale de Lausanne · University of the Free State · KU Leuven
- **分类**: vol 50 · issue 3 · pp 1466-1502
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文基于极值理论提出一种自动、数据驱动的异常值检测方法，将原有仅适用于重尾Pareto型分布的算法推广到所有最大吸引域（max-domains of attraction）。方法核心是利用极值理论的数学框架，通过识别偏离中间和中心特征的极端观测值来标记异常点。作者引入尾部调整箱线图（tail-adjusted boxplot），比传统箱线图更准确地反映可能的异常值，并扩展至多变量场景，结合局部异常因子（local outlier factor）分析。多个模拟和实际数据例子展示了算法在有限样本下的好表现。该方法对假设检验中异常值识别问题提供了一个基于严格极值理论的新工具。
- **关键技术**: `extreme value theory`, `tail-adjusted boxplot`, `max-domains of attraction`, `local outlier factor`, `multivariate outlier detection`
- **为什么对您有用**: 连接研究者interest中的hypothesis testing方向（异常值检测是假设检验的经典问题）。研究者熟悉的非参数统计和高维渐近理论可用于理解极值框架下的样本尾部分布行为，但核心的极值理论工具（如极值指数估计、吸引域判别）不在当前武器库中，属于暂不可做领域，需要补充极值理论基础知识。但本文清晰的数学推导和模拟验证可作为入门阅读，帮助评估该方向是否值得投入。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.12637](https://doi.org/10.1111/sjos.12637) — Daisee: Adaptive importance sampling by balancing exploration and exploitation
- **作者**: Xiaoyu Lu, Tom Rainforth, Yee Whye Teh
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Amazon (United States) · University of Oxford · Amazon (United Kingdom) · Science Oxford
- **分类**: vol 50 · issue 3 · pp 1298-1324
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出 Daisee，一种将自适应重要性采样（AIS）视为在线学习问题的新算法，强调在采样器的迭代更新中平衡探索与利用。借鉴在线学习中的遗憾最小化框架，Daisee 采用基于分区的采样空间划分，并通过策略性分配样本来平衡各区间的探索（获取新信息）与利用（加权当前最优）。作者为 AIS 引入了累积伪遗憾（pseudo-regret）概念，并证明 Daisee 的累积伪遗憾以 O(√T) 增长，T 为迭代次数，与经典在线学习遗憾率一致。算法进一步扩展为分层自适应分区版本，自动学习高维空间中的树形分区结构以提升效率。数值实验验证了 Daisee 在多模态和后验采样任务上优于现有 AIS 方法。该算法将采样与在线决策结合，为统计计算中蒙特卡洛方法的自动化提供了一个新框架。
- **关键技术**: `adaptive importance sampling`, `exploration-exploitation trade-off`, `regret analysis`, `partition-based sampling`, `hierarchical tree structure`, `online learning`
- **为什么对您有用**: 本文直接对应您对统计计算（numerical methods, algorithm）的 primary interest，提供了一个结合在线学习的最小化伪遗憾的 AIS 算法，理论分析清晰（√T 界）。您现有的软件开发能力（very_familiar）可快速实现该算法并复现结果，或将其嵌入您的因果推断/高维计算管线中；若需改进分区策略或扩展到高维，可进一步应用您熟悉的 high-dimensional asymptotics 知识。结论：立即可做——算法框架清晰，代码可独立实现，无需额外工具。

### 2. [10.1111/sjos.12636](https://doi.org/10.1111/sjos.12636) — Spatial bootstrapped microeconometrics: Forecasting for out‐of‐sample geo‐locations in big data
- **作者**: Katarzyna Kopczewska
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Warsaw
- **分类**: vol 50 · issue 3 · pp 1391-1419
- 相关性 4/10 · novelty: `minor`
- **摘要**: 本文研究大数据空间点数据的空间计量模型估计与预测问题，核心难点在于空间权重矩阵W仅定义在样本内观测点上，导致新位置（out-of-sample geo-locations）无法直接预测，且大样本下计算复杂度高。作者提出一种基于bootstrap与Voronoi tessellation（泰森多边形）的新方法：首先对数据进行bootstrap重抽样并估计空间模型，然后利用PAM（Partitioning Around Medoids）算法对回归系数进行非独立分类，选出代表性bootstrap模型；再利用该模型对应的地理点生成Voronoi多边形划分空间。当需要预测新位置时，将其分配到对应的tessellation tile中，并用该tile内原样点的空间权重矩阵替代，从而使得原校准模型可对新位置进行预测。实验表明该方法在预测质量与计算效率之间不存在trade-off。通过一个企业选址与盈利能力的实证案例展示了方法可用性。对于希望了解空间计量在大数据环境下计算挑战的经济应用研究者，本文可作为入门导读。
- **关键技术**: `spatial bootstrapping`, `Voronoi tessellation`, `PAM clustering`, `spatial weights matrix`, `out-of-sample forecasting`
- **为什么对您有用**: 本文连接了您的secondary interest中的econ_theory（空间计量经济应用）与stat_computing（大数据下bootstrap+分区算法）。您武器库中very_familiar项下的“软件发展”可直接用于复现或改进该方法的计算实现。作为gateway reading，空间权重矩阵与tessellation是您目前不熟悉的工具，因此属于中期可做的方向——需先在空间计量计算和Voronoi分区上建立基本理解，然后才能评估该方法是否值得深入或迁移到您自己的因果推断问题中。

## 流行病学  *(epidemiology, 1 篇)*

### 1. [10.1111/sjos.12615](https://doi.org/10.1111/sjos.12615) — Generalizing the information content for stepped wedge designs: A marginal modeling approach
- **作者**: Fan Li, Jessica Kasza, Elizabeth L. Turner, Paul J. Rathouz, Andrew B. Forbes, John S. Preisser
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Yale University · Monash University · Duke University · The University of Texas at Austin · University of North Carolina at Chapel Hill
- **分类**: vol 50 · issue 3 · pp 1048-1067
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究 stepped wedge 试验设计在不完整数据收集情形下的信息量度量，目标是在边际模型框架下量化当某些 cell/sequence/period 缺失时对 treatment effect estimator 精度的影响。设定为边际模型，允许一般的 link function 和 variance function，涵盖 binary/count 等离散结局。核心方法是扩展信息内容这一设计指标到离散结局，推导了在数据元素缺失情形下的解析表达式，并证明在 variance-stabilizing link 下信息量呈现中心对称模式。数值模拟在 canonical link 下进行，发现 cell-level 信息量近似中心对称，但 sequence/period 层面的信息量对 secular trend 敏感、可能严重偏离对称性。这是方法论导向的试验设计工作，对理解不完整 stepped wedge 设计的效率损失有直接参考价值。
- **关键技术**: `stepped wedge cluster randomized design`, `marginal modeling with generalized estimating equations`, `information content for design`, `variance-stabilizing link function`, `incomplete design efficiency analysis`
- **为什么对您有用**: 本文属于流行病学试验设计的方法论工作，与您的 causal inference 和 efficiency theory 兴趣有边际连接——stepped wedge design 本质上是 longitudinal cluster randomized design，涉及 treatment effect 的 identification 和 efficiency。技术层面，本文的信息量分析基于边际模型的方差计算，与您熟悉的 semiparametric efficiency theory 有概念上的呼应，但未涉及 influence function 或效率界等您常用的工具。follow-up 判断：**暂不可做**——本文的核心是试验设计优化而非估计理论，且技术工具（design-based information calculation）不在您的武器库中；若要进入这个方向，需先补充 longitudinal cluster design 的文献背景。

## 其他  *(other, 5 篇)*

### 1. [10.1111/sjos.12620](https://doi.org/10.1111/sjos.12620) — Distributed inference for two‐sample <i>U</i>‐statistics in massive data analysis
- **作者**: Bingyao Huang, Yanyan Liu, Liuhua Peng
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Wuhan University · The University of Melbourne
- **分类**: vol 50 · issue 3 · pp 1090-1115
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在大数据场景下，针对两样本U统计量（如Mann-Whitney统计量）的分布式推断问题，本文提出了两类估计量：直接分布式两样本U统计量（各数据块计算局部U统计量后平均）和分块线性两样本U统计量（基于U统计量的线性近似以降低通信开销）。建立了两种估计量的渐近正态性，并给出方差估计。为支持假设检验，提出了bootstrap算法，包括非简并与简并情形，其中分布式加权bootstrap为方法学新贡献。理论证明依赖Hájek投影和分块独立渐近性。数值实验验证了方法的有效性。对您可能有用：本文直接与您熟悉的高阶U统计量理论对接，可用treewidth/einsum视角分析分块线性U统计量的计算-通信权衡，并为更高阶U统计量（order>2）的分布式推断提供基准。
- **关键技术**: `two-sample U-statistics`, `distributed inference`, `blockwise linear U-statistics`, `weighted bootstrap`, `communication-efficient estimation`, `Hájek projection`
- **为什么对您有用**: 本文直接关联到您primary interest中的higher-order U-statistics，特别关注两样本U统计量在分布式场景下的推断。您对U统计量的计算（treewidth/einsum）非常熟悉，可以立即用该视角分析分块线性U统计量的计算-通信权衡（立即可做）。文中bootstrap方法的理论分析（简并与非简并）拓展了U统计量的推断工具，中期可扩展至更高阶U统计量的分布式推断（需熟悉高阶U统计量渐近理论，属于moderately_familiar）。

### 2. [10.1111/sjos.12634](https://doi.org/10.1111/sjos.12634) — Frequentist model averaging for envelope models
- **作者**: Ziwen Gao, Jiahui Zou, Xinyu Zhang, Yanyuan Ma
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Chinese Academy of Sciences · Academy of Mathematics and Systems Science · University of Chinese Academy of Sciences · Capital University of Economics and Business · Beijing Academy of Artificial Intelligence · Pennsylvania State University
- **分类**: vol 50 · issue 3 · pp 1325-1364
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究多元线性回归中envelope模型的频率学派模型平均方法。Envelope模型通过降维提高估计效率，但单一模型可能预测不稳定。作者提出基于交叉验证准则的模型平均估计量，以加权组合多个候选envelope模型。理论证明：当所有候选模型均错误设定时，该估计量具有渐近最优性，即预测损失渐近地达到不可达的oracle最优。当存在正确设定的模型时，系数估计量一致，且正确模型的权重依概率收敛到1。模拟与实证分析显示方法在预测性能上优于单个envelope模型，且计算上仅需交叉验证，较为简便。对您可能有用：本文与效率理论（envelope提升效率）和统计计算（交叉验证的数值实现）有交集，但属于参数线性模型设定，与半参效率界方向有距离。
- **关键技术**: `model averaging`, `cross-validation`, `envelope method`, `multivariate linear regression`, `asymptotic optimality`, `consistency`
- **为什么对您有用**: 本文涉及效率提升（envelope方法）和模型平均的渐近理论，与您的效率理论兴趣有交集，但未触及半参效率界。武器库中“nonparametric statistics”和“minimax bounds”可用来审视其渐近最优性证明的紧性，但论文的线性模型设定和交叉验证框架并非您当前熟悉的核心范例，属于中期可做：需先学习envelope模型与经典模型平均的文献，再考虑是否将类似思想推广至半参或高维设定。

### 3. [10.1111/sjos.12619](https://doi.org/10.1111/sjos.12619) · [arXiv](https://arxiv.org/abs/2108.10584) — State estimation for aoristic models
- **作者**: Maria N. M. van Lieshout, Robin L. Markwitz
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1068-1089
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对 aoristic 数据（事件精确时间未知，仅知落在观测区间）提出贝叶斯状态估计方法。模型假设潜在事件构成一个标记点过程，观测区间由处于平衡状态的交替更新过程生成，先验取为马尔可夫点过程。推导了后验分布的形式，并用 MCMC 估计模型参数。通过模拟例子展示了不同先验对推断的影响，并将该方法应用于犯罪发生时间的区间删失数据。方法上结合了交替更新过程与马尔可夫点过程，属于一种新的贝叶斯建模思路。对研究者而言，本文提供了一个从区间观测恢复点位置的统计反问题实例，与您非常熟悉的逆问题随机噪声设定有形式上的对应，但采用贝叶斯推断框架，可能拓展工具族。
- **关键技术**: `Markov point process`, `alternating renewal process`, `Bayesian state estimation`, `MCMC`, `interval-censored data`
- **为什么对您有用**: 本文处理的 aoristic 数据本质上是一个统计反问题：从区间观测恢复潜在点位置，这与您熟悉的「逆问题随机噪声」设定直接对应。但这一工作主要依赖贝叶斯 MCMC，而非频率学派估计，因此属于 moderately_familiar 中「M-estimation」以外的工具。若想将此框架推广至您更擅长的半参数效率理论，需要先对贝叶斯点过程的后验收缩率有一定掌握——目前武器库中尚无明确项，属于「暂不可做」；但可作为逆问题 case study 积累感性认识。

### 4. [10.1111/sjos.12630](https://doi.org/10.1111/sjos.12630) · [arXiv](https://arxiv.org/abs/2108.05555) — Longitudinal network models and permutation‐uniform Markov chains
- **作者**: William K. Schwartz, Sonja Petrović, Hemanshu Kaul
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Illinois Institute of Technology
- **分类**: vol 50 · issue 3 · pp 1201-1231
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究纵向网络（longitudinal networks）的边动态演化，设定为离散时间 Markov 链，其转移概率服从指数族形式。核心问题是刻画何时该过程的联合分布也构成同一参数的指数族，从而实现数据降维；同时引入 permutation-uniform 子类，证明其可解释为状态空间上的 i.i.d. 序列。技术工具包括指数族充分性理论、Markov 链的置换不变性分析、以及 temporal ERGM 的似然函数简化。主要理论结果包括：给出了联合分布为指数族的充要条件、对某些模型得到了 MLE 的闭式解、以及 mean-parameter 收敛性分析。本文属于网络模型的方法论工作，与您 primary interests 中的高维统计、半参数理论无直接交集，但涉及 Markov 链的渐近理论。
- **关键技术**: `exponential family transition probabilities`, `permutation-uniform Markov chains`, `temporal exponential random graph models`, `sufficient statistics for Markov chains`, `closed-form MLE`
- **为什么对您有用**: 本文主题（纵向网络模型 / temporal ERGM）不在您的 primary interests 范畴内，与因果推断、高维统计、半参数效率理论均无直接关联。技术层面未涉及您熟悉的 minimax bounds、influence functions、U-statistics 或高维渐近工具。判断为**暂不可做**：核心机器（网络模型的指数族结构 / ERGM 似然几何）不在武器库中，且与您当前研究议程无明显交叉点。建议跳过。

### 5. [10.1111/sjos.12640](https://doi.org/10.1111/sjos.12640) · [arXiv](https://arxiv.org/abs/1808.04348) — Multivariate geometric anisotropic Cox processes
- **作者**: James S. Martin, David J. Murrell, Sofia C. Olhede
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 50 · issue 3 · pp 1420-1465
- 相关性 1/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的多元各向异性Cox过程模型，用于分析和推断具有各向异性结构的多元空间点过程。作者基于多元各向异性随机场的构建，给出了模型的合法性条件，并开发了基于Palm似然的推断方法以避免完整的似然计算。理论部分包括模型的有效性验证和Palm似然估计量的渐近性质。通过Barro Colorado Island的植物树木数据集展示模型在生态学空间分析中的应用价值。研究贡献在于将各向异性引入多元点过程，扩展了传统空间点过程的建模能力，但方法学本质属于空间统计扩展而非高维或因果推断核心方向。对您而言，点过程建模中的计算技巧（如Palm似然近似）可作为统计计算方法的参考，但整体与您的研究兴趣交集有限。
- **关键技术**: `Palm likelihood`, `multivariate Cox process`, `anisotropic random fields`, `spatial point process`, `Markov chain Monte Carlo`
- **为什么对您有用**: 该论文属于空间统计与计算方法的交叉，您可关注其Palm似然推断的实现（与您'统计计算'的次级兴趣相关），但核心模型与您的因果推断、高维统计、U统计无交集。该方向（点过程）不在您当前技术武器库中，属于'暂不可做'范围，仅作入门了解。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

