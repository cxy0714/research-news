# Biometrics — Vol 81  Issue 1  ·  2026-06-24

- 共 18 篇 · Biometrics
- 目录核对 ⚠️ 疑似漏 20 篇（对照 OpenAlex 38 篇）：10.1093/biomtc/ujaf010、10.1093/biomtc/ujaf013、10.1093/biomtc/ujaf020、10.1093/biomtc/ujae164、10.1093/biomtc/ujae163 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期以因果推断为主线，共有7篇论文，主分层、数据融合、动态治疗机制与连续暴露处理效应是其中反复出现的主题。此外，非参数/半参数方法（4篇）、高维筛选与计算（4篇）以及假设检验（1篇）构成了另一条线索。流行病学与可解释回归各有2篇和1篇，整体上关注方法上的识别、估计效率与计算可行性。

因果推断中最突出的子线是主分层与数据融合。两篇主分层论文分别提出无亚型平均因果效应（SF-ACE）和贝叶斯非参数树（BCF），前者在异质性病因下定义因果效应并提供双稳健估计与敏感性分析，后者用BART建模连续主分层成员关系与条件结局，两者都强调识别假设的放松与灵活性。数据融合方面，power likelihood方法通过对观察性数据似然施加自适应幂参数，平衡偏差与方差，并给出基于ELPD的λ选择；而连续暴露的DiD多重稳健估计量则组合干预、暴露、结局三个模型，在任意一个正确指定下保持一致性，并推导了影响函数与渐近分布。动态治疗机制方面，针对协变量不可忽略缺失的加权Q-learning构建了非响应工具变量与敏感性分析两条路径，弥补了传统Q-learning在伪结局缺失下的偏差。大规模中介分析中，复合零假设检验通过区域计数控制I类错误，是非渐近框架的直接应用，无需方差估计。临床试验估计一文比较了多种因果推断估计量在hypothetical estimand下的表现，虽未提出新方法，但提供了识别假设与R包实现细节。

非参数/半参数板块中，Fréchet-SIS将特征筛选推广至度量空间值响应，利用边际广义残差平方和实现超高维筛选（胜出性质），适用于分布与矩阵数据。RBF-net with shared neurons针对多处理条件效应曲线，通过共享隐藏层参数提高效率，在贝叶斯框架下量化不确定性。二元生存数据伪观测方法推广了经典pseudo-observations至删失二元结局，基于两个非参数联合生存估计量，给出回归系数的渐近理论。贝叶斯标量对网络回归则保留SPD矩阵的黎曼几何结构，在切空间上做稀疏贝叶斯降维。高维计算方面，分布式高斯过程通过递归积分整合局部模型，证明相合性与渐近正态性；矩阵回归中提出的多层次子图提取方法在控制假阳性下识别结构特征对功能连接网络的影响。

假设检验部分，相依检验组合框架通过估计依赖结构校正合并分布，将Cauchy组合法视为特例，解决微生物组关联研究中忽视依赖导致的尺寸失真。其他论文包括负-无标签混合模型用于长COVID亚型识别、正则化Dirichlet-multinomial整合单细胞与临床数据、鲁棒贝叶斯图形回归处理异质性蛋白质组网络、以及基于Mallows's Cp的可解释函数构建。

对于因果推断方向的研究者，power likelihood（数据融合）、SF-ACE与BCF（主分层）、multiply robust DiD（连续暴露）以及weighted Q-learning（缺失协变量）值得优先关注；半参数/非参数效率方向可关注Fréchet-SIS与RBF-net；高维渐近方向可参阅分布式空间模型与矩阵回归。

## 因果推断  *(causal_inference, 7 篇)*

### 1. [10.1093/biomtc/ujaf008](https://doi.org/10.1093/biomtc/ujaf008) · [arXiv](https://arxiv.org/abs/2304.02339) — Combining experimental and observational data through a power likelihood
- **作者**: Xi Lin, Jens Magelund Tarp, Robin J Evans
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 针对随机对照试验（RCT）样本量不足、观察性数据易受隐藏混杂偏倚的问题，本文提出一种 power likelihood 方法，用于融合两种数据源以提高处理效应（ATE）估计的效率。核心思路是对观察性数据的似然部分施加一个幂参数 λ（学习率），在联合似然中调控其信息贡献量；λ 通过最大化期望对数预测密度（ELPD）实现数据自适应选择，从而在偏差与方差间取得平衡。模拟实验显示，该方法在扩大功效的同时近似维持了名义覆盖率，且对不同程度的混杂具有稳健性。在真实数据应用中，该方法成功将 PIONEER 6 临床试验与美国健康索赔数据融合，并给出了详细的实际操作指南。该工作为因果推断中的数据融合提供了可操作框架，可直接利用您擅长的“估计理论”分析其识别假设和渐近性质，并有望通过“高阶影响函数（HOIF）”进一步提升效率。
- **关键技术**: `power likelihood`, `expected log predictive density`, `data adaptive learning rate`, `RCT-observational data fusion`
- **为什么对您有用**: 本文直接对应您因果推断兴趣中子方向“数据融合（RCT + observational）”。您非常熟悉的“estimation theory in causal inference”可严格分析该方法的识别条件与渐近效率，而您较熟悉的“HOIF”有潜力推导其半参数有效界或构建更稳健的高阶估计。立即可做：检验 power likelihood 选择程序能否通过影响函数实现稳健推断；中期可做：将正交机器学习（DML）框架融入该方法以减轻对初始估计的依赖。

### 2. [10.1093/biomtc/ujaf016](https://doi.org/10.1093/biomtc/ujaf016) · [arXiv](https://arxiv.org/abs/2206.00209) — The subtype-free average causal effect for heterogeneous disease etiology
- **作者**: A Sasson, M Wang, S Ogino, D Nevo
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文针对结直肠癌的MSI亚型异质性，提出了一种新的因果效应估计量——无亚型平均因果效应（SF-ACE），基于主分层框架定义暴露（吸烟）对那些在任何暴露水平下都不会患其他亚型疾病的人群的因果效应。作者研究了SF-ACE的非参数可识别性，并讨论了多种单调性假设，这些假设比标准主分层设置更精细。由于识别依赖不可检验假设，作者进一步开发了敏感性分析方法以放松这些假设。估计方面，论文给出了三种估计量，包括一个双稳健估计器，利用倾向性得分和结局回归模型。该方法被应用于两个大型队列研究，分析吸烟对结直肠癌MSI亚型的异质效应。该工作对您在流行病学中应用因果推断方法、特别是主分层和敏感性分析的实践有直接参考价值。
- **关键技术**: `principal stratification`, `doubly robust estimation`, `sensitivity analysis`, `monotonicity assumptions`, `Subtype-Free Average Causal Effect (SF-ACE)`, `non-parametric identification`
- **为什么对您有用**: 本文直接涉及因果推断中的主分层估计和敏感性分析，属于您的primary interest中的因果推断子方向。您对因果推断识别理论和估计理论（very_familiar）的掌握可直接用于评估该estimand的识别条件是否合理、双稳健估计器的有限样本性态如何。该方法的敏感性分析思路可迁移至您关注的其他纵向或IV设定中的不可检验假设评估。基于您的武器库，对此类方法的理解和潜在扩展应是立即可做的。

### 3. [10.1093/biomtc/ujae161](https://doi.org/10.1093/biomtc/ujae161) · [arXiv](https://arxiv.org/abs/2312.01735) — Weighted Q-learning for optimal dynamic treatment regimes with nonignorable missing covariates
- **作者**: Jian Sun, Bo Fu, Li Su
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 论文研究在动态治疗机制（DTRs）中，当协变量存在不可忽略缺失时如何估计最优治疗规则。Q-learning是常用的向后归纳算法，但后一阶段非可忽略缺失的协变量会导致前一阶段伪结局也出现非可忽略缺失，即使纵向结局完全观测，也会得到次优规则。作者提出两种加权Q-learning方法，通过估计方程结合非响应工具变量或敏感性分析来获得伪结局缺失的逆概率权重，从而校正偏差。作者推导了加权Q-learning估计量的渐近性质，并通过模拟和MIMIC-III数据库中脓毒症患者液体策略研究验证了方法效果。对于您的因果推断研究方向，特别是纵向处理机制和缺失数据的工具变量识别问题，本文提供了可直接借鉴的加权估计框架。
- **关键技术**: `Weighted Q-learning`, `Inverse probability weighting`, `Nonresponse instrumental variables`, `Estimating equations`, `Sensitivity analysis`, `Backward induction`
- **为什么对您有用**: 本文直接对应您因果推断兴趣中的纵向DTR和缺失数据问题，并使用工具变量处理非可忽略缺失，这与您熟悉的因果推断估计理论（estimation theory in causal inference）高度契合。技术武器库中“identification theory in causal inference”和“estimation theory in causal inference”均为非常熟悉，因此可立即理解并评估该方法是否可推广到其他纵向因果设定（如IV在缺失数据中的应用）。立即可做——无需补充新工具。

### 4. [10.1093/biomtc/ujaf011](https://doi.org/10.1093/biomtc/ujaf011) — A simple and powerful method for large-scale composite null hypothesis testing with applications in mediation analysis
- **作者**: Yaowu Liu
- **期刊/来源**: Biometrics
- **机构**: Southwestern University of Finance and Economics · Statistical Research (United States)
- **分类**: vol 81 · issue 1
- 相关性 8/10 · novelty: `new_theory`
- **摘要**: 在大规模中介分析（如全基因组表观遗传研究）中，需检验的复合零假设为“间接效应为零或直接效应为零”，经典 Sobel 检验和联合显著性检验因将两类间接效应同时视为零导致保守，功效低。本文提出一种仅需统计某一预设区域内观测检验统计量数目的简单方法，无需估计方差或使用 Bootstrap，通过区域计数直接控制 I 类错误。非渐近理论在弱假设下建立，证明该方法能有限样本控制族系误差并保持较高功效，理论边界与模拟吻合。模拟覆盖多种效应分布和维度，显示该方法在全部设定下控制 I 类错误且功效优于 Sobel 检验。真实数据应用于 DNA 甲基化中介效应筛选。该方法直接关联因果推断中的中介分析，其非渐近结果可用高维渐近工具验证最适性，且计数策略易于与现有多重比较程序结合。
- **关键技术**: `composite null hypothesis`, `region-based counting procedure`, `non-asymptotic error control`, `large-scale mediation analysis`, `multiple testing`
- **为什么对您有用**: 本文直接针对因果推断中的中介分析大规模检验难题，属于 primary interest 中 causal inference 的 mediation 子方向；您非常熟悉的 `high-dimensional asymptotics` 和 `estimation theory in causal inference` 可直接用于评估其非渐近边界是否紧致，并扩展至更一般的效应模型上；**立即可做**——该方法理论清晰、假设弱，您已有工具即可检验其最小最大最优性或设计更高效的计数区域。

### 5. [10.1093/biomtc/ujae167](https://doi.org/10.1093/biomtc/ujae167) · [arXiv](https://arxiv.org/abs/2308.13085) — Estimating hypothetical estimands with causal inference and missing data estimators in a diabetes trial case study
- **作者**: Camila Olarte Parra, Rhian M Daniel, David Wright, Jonathan W Bartlett
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文以2型糖尿病临床试验为案例，针对ICH E9附录中定义的hypothetical estimand，旨在估计随机化治疗在假设无抢救治疗和停药情况下的因果效应。作者使用了五种估计方法：混合模型重复测量（MMRM）、多重插补（MI）、逆概率治疗加权（IPTW）、G-formula和G-estimation，并详细说明了各自的识别假设和R包实现细节。所有方法得到相似的估计值和标准误，说明在满足各自假设时结果稳健。文章还讨论了实际选择估计方法时的考量，如计算时间、缺失数据处理、是否纳入事件后数据以及是否调整时依混杂。作为应用导向的比较研究，该文并未提出新方法学，但为因果推断在临床试验中的应用提供了实用的方法论指南。对研究者而言，本文能帮助理解因果推断方法在真实缺失数据和intercurrent event下的实施细节，尤其连接了因果推断中的identification假设与实际估计的差距。
- **关键技术**: `MMRM`, `multiple imputation`, `inverse probability of treatment weighting`, `G-formula`, `G-estimation`
- **为什么对您有用**: 该文直接连接您首要兴趣中的因果推断应用方向，特别是缺失数据与intercurrent events的处理。您武器库中'very_familiar'的'estimation theory in causal inference'可帮助您评估这些估计量在假设偏离时的效率损失；同时，该文可作为'流行病学'次级兴趣的入门阅读，清晰展示了统计方法在真实临床试验中的全流程。c此文章为应用导向，无新理论贡献，但提供了可复现的R代码和实际数据案例，适合作为中期可做的教学材料——您若想在此方向上结合自己的理论工作，需先熟悉这些标准方法的具体实现细节（moderately_familiar中的identification theory可帮助理解假设）。

### 6. [10.1093/biomtc/ujaf024](https://doi.org/10.1093/biomtc/ujaf024) · [arXiv](https://arxiv.org/abs/2403.13256) — Bayesian nonparametric trees for principal causal effects
- **作者**: Chanmin Kim, Corwin Zigler
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 主分层分析旨在评估处理对结局的因果效应如何随中间变量上的处理效应而变。当中间变量连续时，存在无限多基本主分层，识别和估计变得困难。本文提出贝叶斯非参数方法，采用贝叶斯因果森林（BCF）同时指定两个BART模型：一个用于主分层成员关系，另一个用于条件于主分层的结局。BCF捕捉处理效应异质性的能力特别适用于连续主分层场景，并且能缓解目标选择和正则化诱发混淆问题。通过模拟和真实数据（发电厂排放控制对PM的影响）验证方法性能。该方法将中介因果推断与非参数贝叶斯树模型相结合，为主分层分析提供了灵活的建模工具。对您而言，这与您关于中介分析和因果效应异质性的兴趣直接相关，同时非参数建模技巧可迁移到其他因果推断设定。
- **关键技术**: `Bayesian Causal Forests (BCF)`, `Bayesian Additive Regression Trees (BART)`, `Principal Stratification`, `Treatment effect heterogeneity`, `Posterior inference via MCMC`
- **为什么对您有用**: （1）直接关联因果推断中的主分层与中介分析子方向，是您感兴趣的mediation框架的一个具体实施。（2）武器库中的“非参数统计”和“因果推断的识别理论”可以用于评估该方法的识别假设和模型灵活性，尤其是BART作为非参数回归工具与您的非参数背景契合。（3）中期可做：您当前对贝叶斯非参数树方法（BART）不熟悉，需先在该工具上投入阅读（如Chipman等BART原始论文）后才能动手改进或扩展该方法。

### 7. [10.1093/biomtc/ujaf015](https://doi.org/10.1093/biomtc/ujaf015) · [arXiv](https://arxiv.org/abs/2401.14355) — Multiply robust difference-in-differences estimation of causal effect curves for continuous exposures
- **作者**: Gary Hettinger, Youjin Lee, Nandita Mitra
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 difference-in-differences (DiD) 框架下，目标是估计连续型暴露处理的 causal effect curve，允许 confounding 同时影响干预状态、暴露水平和结果趋势。作者提出 multiply robust estimator，通过组合 intervention model、exposure model 和 outcome model 构建估计量，在三个模型中任一子集正确指定时仍保持一致性，且对 effect curve 不施加参数假设。理论证明估计量具有 n^{-1/2}-consistency 和渐近正态性，并推导了 influence function 以支持方差估计。模拟研究验证了有限样本表现，实证分析应用于营养消费税在跨境购物便利性异质性下的政策效果。对您在因果推断中处理连续处理变量和 robust estimation 的兴趣有直接参考价值。
- **关键技术**: `difference-in-differences`, `multiply robust estimation`, `continuous treatment exposure`, `causal effect curve`, `influence function`, `semiparametric efficiency`
- **为什么对您有用**: 直接连接因果推断中的 DiD 设计与连续处理变量估计，属于您 primary interest 中 identification 和 estimation 的范畴。multiply robust 结构与 semiparametric efficiency theory 紧密相关，可用您 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 semiparametric theory 来审视其 influence function 构造和 efficiency bound 是否可达最优。立即可做：用您熟悉的 semiparametric efficiency 理论验证其 robustness 条件是否 sharp，或探索更高阶的 influence function 改进。

## 非参数 / 半参数  *(nonparam_semipara, 4 篇)*

### 1. [10.1093/biomtc/ujaf007](https://doi.org/10.1093/biomtc/ujaf007) — Feature screening for metric space-valued responses based on Fréchet regression with its applications
- **作者**: Bing Tian, Jian Kang, Wei Zhong
- **期刊/来源**: Biometrics
- **机构**: Xiamen University · University of Michigan
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对度量空间值响应（如分布数据、矩阵数据）的超高维特征筛选问题，提出了一种基于全局Fréchet回归的Fréchet-SIS程序。该方法利用边际广义残差平方和作为筛选效用，仅需响应变量之间的距离，无需具体空间结构。理论证明在温和正则条件下，Fréchet-SIS具有sure screening性质，即能以概率趋于1保留所有重要预测变量。模拟研究验证了其在有限样本下的良好表现；在阿尔茨海默病神经影像研究中，从582,591个SNP中筛选出与脑区域活跃性相关的关键基因。此外还包含一个经济案例。该工作将经典SIS框架拓展至非线性、非欧几里得型响应，为非参数回归和高维统计提供了新工具。
- **关键技术**: `Fréchet regression`, `sure independence screening`, `metric space-valued responses`, `marginal generalized residual sum of squares`, `sure screening property`
- **为什么对您有用**: 本文直接连接到您的非参数统计（very_familiar）兴趣：Fréchet回归是非参数方法处理复杂响应数据的典型例子，其理论分析依赖高维渐近技巧。由于您已熟练掌握非参数统计学和高维渐近理论，可立即深入考察该方法在因果推断中高维协变量筛选的适用性，或将其与您熟悉的U-统计量/高阶影响函数结合。follow-up判断：立即可做——非参数工具足以理解与扩展，无需补充新器材。

### 2. [10.1093/biomtc/ujaf019](https://doi.org/10.1093/biomtc/ujaf019) · [arXiv](https://arxiv.org/abs/2401.16571) — Individualized multi-treatment response curves estimation using RBF-net with shared neurons
- **作者**: Peter Chang, Arkaprava Roy
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在多处理（multi-treatment）因果推断设定下，目标是估计条件处理效应曲线（individualized treatment response curves），假设无混淆性并允许处理间存在共享结构。作者提出 RBF-net with shared neurons 的非参数方法，通过共享隐藏层神经元建模不同处理响应曲线之间的共性，从而提高估计效率。估计与推断在贝叶斯框架下进行，使用 thresholded best linear projections 和 MCMC 算法，同时量化不确定性。模拟展示了有限样本表现，应用于 MIMIC 脓毒症数据分析了不同治疗策略对 ICU 住院时长和 SOFA 评分的影响。对您而言，这是非参数估计与因果推断交叉的应用型工作，方法学 novelty 相对有限。
- **关键技术**: `RBF neural network`, `shared hidden neurons`, `Bayesian nonparametric estimation`, `MCMC inference`, `heterogeneous treatment effect`, `multi-treatment causal inference`
- **为什么对您有用**: 连接到因果推断中的 heterogeneous treatment effect (HTE) 估计，属于您 primary interest 中因果推断的应用延伸。从技术武器库看，本文的贝叶斯非参数方法与您熟悉的 nonparametric statistics 和 minimax theory 有一定距离，核心是神经网络 + MCMC 而非效率理论或 influence function。follow-up 判断：**暂不可做**——若想深入需要先补贝叶斯非参数和神经网络优化方面的肌肉，不在当前武器库内；但作为应用案例了解 MIMIC 数据和 HTE 实践可一读。

### 3. [10.1093/biomtc/ujaf006](https://doi.org/10.1093/biomtc/ujaf006) · [arXiv](https://arxiv.org/abs/2412.04109) — Pseudo-observations for bivariate survival data
- **作者**: Yael Travis-Lumer, Micha Mandel, Rebecca A Betensky
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在双变量生存时间受右删失的设定下，本文提出将 pseudo-observations 方法推广至二元情形，目标是估计协变量对联合生存概率、条件生存概率等量的效应。核心机制是先估计联合生存函数（考虑 Lin-Ying 1993 和 Dabrowska 1988 两个非参数估计量），再基于此构造 pseudo-observations 作为广义线性模型的响应变量。理论证明：在两个估计量下，回归系数估计均具有一致性与渐近正态性，关键工具是多元 Kaplan-Meier 估计量的渐近理论与 influence function 分解。方法通过模拟与两个真实数据集验证，可同时估计多个时间点的协变量效应。对您而言，这是 pseudo-observations 从一元到二元的一个非平凡推广，涉及 influence function 与半参数渐近理论。
- **关键技术**: `pseudo-observations`, `bivariate survival analysis`, `Dabrowska estimator`, `influence function`, `asymptotic normality`, `right censoring`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric theory 与 efficiency theory——pseudo-observations 本质上是 influence function 的一个实现形式，二元推广涉及非参数估计量的渐近性质分析。您武器库中 very_familiar 的 nonparametric statistics 与 moderately_familiar 的 semiparametric theory 足以攻这篇 paper 的理论部分。**立即可做**：用 influence function 视角审视其 pseudo-observations 构造是否达到 semiparametric efficiency bound，或考虑是否可用 HOIF 改进高维协变量情形下的估计效率。

### 4. [10.1093/biomtc/ujaf023](https://doi.org/10.1093/biomtc/ujaf023) · [arXiv](https://arxiv.org/abs/2401.16749) — Bayesian scalar-on-network regression with applications to brain functional connectivity
- **作者**: Xiaomeng Ju, Hyung G Park, Thaddeus Tarpey
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文研究标量响应变量与脑功能连接（对称正定矩阵，SPD）之间的回归问题，目标是在保持 SPD 矩阵 Riemannian 几何结构的前提下实现降维与预测。方法在 SPD 矩阵的切空间（tangent space）中进行建模，通过 Stiefel 流形上的稀疏先验对降维矩阵进行监督学习，避免了直接向量化忽略几何结构的问题。估计采用全贝叶斯框架，可对所有参数进行不确定性量化并识别关键脑区。理论部分未给出频率学派意义下的收敛率或效率界，主要贡献在于将 Riemannian 几何与稀疏贝叶斯降维结合。对您而言，本文提供了一个将流形几何约束与回归结合的案例，但方法学深度有限。
- **关键技术**: `SPD matrix Riemannian geometry`, `tangent space projection`, `Stiefel manifold optimization`, `sparse Bayesian prior`, `supervised dimension reduction`
- **为什么对您有用**: 本文涉及 semiparametric theory 中的流形约束建模，但核心是贝叶斯方法而非效率理论或 influence function，与您熟悉的 minimax bound / HOIF / semiparametric efficiency 武器库距离较远。技术层面，切空间投影是标准的 SPD 几何处理，稀疏 Stiefel 流形先验属于计算贝叶斯技巧，不涉及您 primary interest 中的 identification / sensitivity / debiased ML 等核心问题。follow-up 判断：**暂不可做**——若想进入流形约束统计方向，需先补充 Riemannian 几何与流形优化基础（武器库中缺），且本文本身更偏向应用而非理论推进。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1093/biomtc/ujaf001](https://doi.org/10.1093/biomtc/ujaf001) · [arXiv](https://arxiv.org/abs/2404.09353) — A unified combination framework for dependent tests with applications to microbiome association studies
- **作者**: Xiufan Yu, Linjun Zhang, Arun Srinivasan, Min-ge Xie, Lingzhou Xue
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对微生物组关联研究中多种检验的合并问题，提出一个统一的元分析框架，能够在检验相互依赖时正确合并P值或置信分布。该框架推广了经典的P值组合方法和置信分布方法，通过引入依赖结构估计（如相关矩阵或协方差）来校正合并统计量的分布，从而控制检验的尺寸。此框架将广泛使用的Cauchy组合法视为特例，并能在Cauchy组合法的分布假设不满足时提供替代方案。理论分析证明了所提方法能准确控制第一类错误率，并在相依条件下保持渐近有效性。数值模拟和微生物组数据应用表明，忽略检验之间的依赖会导致严重的尺寸失真，而所提框架能灵活适应依赖结构，提高检验功效。该方法整合了多种微生物组关联检验的优势，在不同备择空间下实现更高效的微生物组关联发现。对您（研究者）而言，该工作为处理依赖检验的组合问题提供了通用且可理论验证的框架，可直接应用于您假设检验兴趣方向中的多重检验校正或敏感性分析场景，且与微生物组流行病学应用相关。
- **关键技术**: `P-value combination`, `Cauchy combination method`, `confidence distribution`, `dependent test adjustment`, `microbiome association studies`
- **为什么对您有用**: 该论文直接针对您primary interest中的假设检验（hypothesis testing）子方向，特别是依赖检验的组合方法，这是您关注的统计推断问题之一。武器库中very_familiar的“high-dimensional asymptotics”可帮助理解其依赖结构估计的渐近性质，而框架本身可作为工具应用于您因果推断或流行病学分析中的多重假设检验校正。您可立即可做——因为您对假设检验理论非常熟悉，只需将现有代码或模拟框架适配即可检验该方法在自身应用中的表现。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1093/biomtc/ujaf027](https://doi.org/10.1093/biomtc/ujaf027) · [arXiv](https://arxiv.org/abs/2310.18533) — Evaluating the effects of high-throughput structural neuroimaging predictors on whole-brain functional connectome outcomes via network-based matrix-on-vector regression
- **作者**: Tong Lu, Yuan Zhang, Vince Lyzinski, Chuan Bi, Peter Kochunov, Elliot Hong et al.
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究多模态神经影像数据中结构特征（如白质微结构完整性、皮层厚度）对全脑功能连接网络的影响，estimand 是矩阵型响应（功能连接矩阵）对向量型预测变量的回归系数。作者提出 multi-level sub-graph extraction 方法，在 matrix-on-vector regression 框架下通过 dense bipartite with nested unipartite graph 结构识别空间特异性的 SI 子集对 FC 子网络的系统性影响。方法核心是控制大规模高维数据中的 false positive，采用 network-based 的多重检验校正策略。理论贡献主要是方法学框架与算法设计，未给出显式的渐近理论或 minimax 率。应用于 UK Biobank 4242 名受试者数据，发现皮质脊髓束和小脑下脚的 WMMI 显著影响感觉运动、突显和执行子网络的功能连接（平均相关 0.81，p < 0.001）。对您而言，这是高维矩阵回归与 network data 的应用案例，涉及您感兴趣的 high-dimensional statistics 与 statistical computing 交叉。
- **关键技术**: `matrix-on-vector regression`, `sub-graph extraction`, `bipartite graph modeling`, `false discovery control`, `high-dimensional neuroimaging data`, `network-based inference`
- **为什么对您有用**: (1) 连接到 high-dimensional statistics 与 statistical computing 的交叉——matrix-on-vector regression 是高维矩阵数据推断的具体设定，涉及多重检验与 false discovery control。(2) 您的 very_familiar 武器库中 minimax bounds for estimation 与 high-dimensional asymptotics 可用于分析该方法的 rate optimality，但目前论文缺乏显式理论框架，需先厘清其 matrix regression 的概率模型设定。(3) follow-up 判断：**中期可做**——若想深入，需在 moderately_familiar 的 semiparametric theory 上补充 matrix-valued response 的 efficiency theory，或用您的 high-dimensional asymptotics 工具分析其 sub-graph extraction 的理论性质。

### 2. [10.1093/biomtc/ujae159](https://doi.org/10.1093/biomtc/ujae159) · [arXiv](https://arxiv.org/abs/2305.15951) — Distributed model building and recursive integration for big spatial data modeling
- **作者**: Emily C Hector, Brian J Reich, Ani Eloyan
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 在超高维空间数据设定下，本文研究高斯过程模型参数的估计与推断问题，目标是克服全数据似然计算不可行的瓶颈。核心方法是分布式模型构建与递归积分：将空间域递归划分，在各分区独立构建局部模型，再通过递归积分同时整合分区内部与分区之间的空间依赖。理论贡献包括证明估计量的相合性与渐近正态性，并给出计算复杂度的降低量级。实证部分应用于自闭症谱系障碍的脑影像数据。对您在统计计算与高维渐近方面的兴趣有直接参考价值。
- **关键技术**: `distributed estimation`, `Gaussian process`, `recursive integration`, `spatial partitioning`, `computational complexity`, `asymptotic normality`
- **为什么对您有用**: 本文属于 stat_computing 与高维渐近的交叉，核心贡献是分布式递归积分框架，与您 very_familiar 的「high-dimensional asymptotics」和「software development」直接相关。技术层面，递归积分的方差-协方差整合涉及高维矩阵分块运算，可用您熟悉的矩阵计算与高维渐近工具审视其效率与理论紧性。follow-up 判定：立即可做——用 very_familiar 的高维渐近工具验证其声称的渐近效率是否达到 semiparametric efficiency bound，或用软件工程经验评估其分布式实现的可扩展性。

## 流行病学  *(epidemiology, 2 篇)*

### 1. [10.1093/biomtc/ujaf021](https://doi.org/10.1093/biomtc/ujaf021) — Sparse Bernoulli mixture modeling with negative-unlabeled data: an approach to identify and characterize long COVID
- **作者**: Tingyi Cao, Harrison T Reeder, Andrea S Foulkes
- **期刊/来源**: Biometrics
- **机构**: Harvard University · Massachusetts General Hospital
- **分类**: vol 81 · issue 1
- 相关性 6/10
- **摘要**: 本文聚焦于长COVID（PASC）的识别与亚表型分型问题。数据来源为RECOVER-Adult前瞻性队列，具有负-无标签（negative-unlabeled）结构：未感染者确定阴性，感染者PASC状态未知。作者提出稀疏伯努利混合模型，通过引入贝叶斯先验实现特征自动选择，并设计新参数化形式以适配负-无标签观测机制。采用EM算法进行参数估计，网格搜索确定聚簇数目与稀疏水平。模拟验证了方法在有限样本下的良好表现，真实数据分析展示了疾病亚型的症状特征与异质性。本文为流行病学中无序症状数据的无监督分型提供了可行框架，其负-无标签建模思路对公共卫生领域的因果推断问题亦有借鉴。
- **关键技术**: `Bernoulli mixture models`, `negative-unlabeled data`, `sparse Bayesian priors`, `EM algorithm`, `feature selection`, `grid search`
- **为什么对您有用**: (1) 本文直接对应您 secondary interest 中的流行病学方向，处理的是真实队列数据中的疾病亚型识别问题，负-无标签设定在疾病登记研究中十分普遍，方法学可迁移至其他类似场景； (2) 您的 very_familiar 武器库中的 nonparametric statistics 和 software development 可用于复现或扩展其 EM 算法（例如用您熟悉的 einsum 语法加速似然计算），而 moderately_familiar 中的 M-estimation theory 可用于分析该混合模型估计的渐近性质； (3) 立即可做：您已有的非参数统计与软件开发经验足以理解并动手改进该方法（如引入更高阶的稀疏结构或非参数混合核）。

### 2. [10.1093/biomtc/ujaf005](https://doi.org/10.1093/biomtc/ujaf005) — A regularized Bayesian Dirichlet-multinomial regression model for integrating single-cell-level omics and patient-level clinical study data
- **作者**: Yanghong Guo, Lei Yu, Lei Guo, Lin Xu, Qiwei Li
- **期刊/来源**: Biometrics
- **机构**: The University of Texas at Dallas · The University of Texas Southwestern Medical Center
- **分类**: vol 81 · issue 1
- 相关性 4/10 · novelty: `application`
- **摘要**: 研究问题：整合单细胞RNA测序数据与患者水平临床变量（如年龄、性别、表型），以揭示细胞类型丰度与临床结局的关联。该方法基于Dirichlet-multinomial回归，并引入正则化（regularized Bayesian框架）处理高维细胞类型比例。模型通过层次树结构（hierarchical tree）在不同细胞类型分辨率水平上识别关联，避免了传统的两阶段分析。在三个疾病数据集（肺纤维化、COVID-19、非小细胞肺癌）上，模型成功发现了有生物学意义的关联。方法上采用贝叶斯推断，利用MCMC进行后验抽样，但未讨论识别性、偏差或效率理论。对您的主要兴趣（因果推断、高维统计、效率理论）而言，此文作为流行病学应用案例，展示了单细胞数据与临床变量整合的实证思路，但其方法学新颖性有限（主要是应用现有贝叶斯框架）。
- **关键技术**: `Dirichlet-multinomial regression`, `Bayesian regularization`, `hierarchical tree structure`, `single-cell RNA-seq integration`, `MCMC`
- **为什么对您有用**: 连接次要兴趣中的流行病学应用，提供了单细胞组学与临床数据关联的实证案例。虽然方法论与您的primary interest交集较少（非因果推断、非高维渐近效率），但可作为流行病学研究的数据结构和分析流程参考。武器库：用软件开发和M-estimation知识容易复现拟合，但方法对您的主要理论工具（如U统计量、半参数效率）暂无直接结合点；**暂不可做**——核心高级统计工具（如因果识别、半参数推断）在此文中不凸显。

## 其他  *(other, 2 篇)*

### 1. [10.1093/biomtc/ujae160](https://doi.org/10.1093/biomtc/ujae160) · [arXiv](https://arxiv.org/abs/2310.18474) — Robust Bayesian graphical regression models for assessing tumor heterogeneity in proteomic networks
- **作者**: Tsung-Hung Yao, Yang Ni, Anindya Bhadra, Jian Kang, Veerabhadran Baladandayuthapani
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在蛋白质组网络异质性研究中，现有图形模型常假设同质图或正态性，本文提出鲁棒贝叶斯图形回归（rBGR）以同时处理非正态数据和异质性图。方法通过随机边际变换将非正态数据映射到正态，并利用图形回归技术构建协变量依赖图。提出条件符号独立性（conditional sign independence with covariates）的表征边依赖性，并设计高效后验采样算法。模拟表明rBGR在边缘和协变量选择上优于现有图形回归模型，尤其当数据非正态性增强时。应用于肺癌和卵巢癌蛋白质组网络，揭示与免疫细胞丰度差异相关的蛋白质-蛋白质相互作用，部分验证已知知识并发现新互作。对您的流行病学数据应用兴趣可能有用，尤其是蛋白质组网络与免疫微环境的关联分析。
- **关键技术**: `Bayesian graphical regression`, `random marginal transformations`, `conditional sign independence`, `graphical regression`, `posterior sampling`, `proteomic networks`
- **为什么对您有用**: 1) 连接到次要兴趣“流行病学”中的癌症蛋白质组数据集及免疫微环境分析。2) 技术储备中的“非参数统计”可用于理解随机边际变换的理论性质，但当前工作偏向应用。3) 暂不可做，核心机器不在武器库里（贝叶斯图形模型和MCMC采样算法）。

### 2. [10.1093/biomtc/ujaf014](https://doi.org/10.1093/biomtc/ujaf014) · [arXiv](https://arxiv.org/abs/2501.15526) — A general, flexible, and harmonious framework to construct interpretable functions in regression analysis
- **作者**: Tianyu Zhan, Jian Kang
- **期刊/来源**: Biometrics
- **分类**: vol 81 · issue 1
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对连续结果回归分析中的可解释函数构建，提出一个通用且灵活的框架，将用户对可解释性的期望形式化为函数骨架。使用 Mallows's Cp 统计量构建新的模型选择准则，以平衡近似精度、泛化能力和可解释性。方法应用于适应性临床试验设计的样本量公式推导、贝叶斯 Go/No-Go 范式的操作特征解释，以及 Fisher 精确检验的假设检验示例。在 NHANES 实际数据分析中展示了重要实验室测量之间的关系。还讨论了扩展到分类结果以及更广泛的可解释性定义。该框架为回归建模中的可解释性提供了系统性方案，但其方法论主要基于经典的 Mallows's Cp 和模型选择，并未引入与统计学前沿（如半参数效率、高维推断或因果识别）直接相关的技术。
- **关键技术**: `interpretable regression`, `Mallows's Cp statistic`, `model selection criterion`, `functional skeleton`, `adaptive clinical trial design`
- **为什么对您有用**: 本文与您的 primary interests 中 'semiparametric & nonparametric theory' 以及 'statistical computing' 有间接关联——可解释函数骨架可视为一种半参数建模思路，Mallows's Cp 选择准则属于经典统计计算。但该论文更偏向于应用统计学而非理论前沿，且未涉及因果推断或高维统计。从武器库角度看：您非常熟悉的非参数统计和软件工程技能可用于复现该框架，但核心问题（可解释性定义与模型选择）并非您当前的研究重点，属于可读可不读的邻域拓展材料。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

