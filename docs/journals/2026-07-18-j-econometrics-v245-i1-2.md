# J. Econometrics — Vol 245  Issue 1-2  ·  2026-07-18

- 共 5 篇 · Journal of Econometrics

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Journal of Econometrics》第245卷1-2期共5篇论文，主题分布较为分散，但可归纳为三条主线：**因果推断与实验设计**（2篇）、**时间序列与持久性预测**（2篇）、以及**复制危机与统计推断**（1篇）。此外，还有一篇关于分数阶过程的谱密度方法（other类），属于计算方法方向。

在**因果推断与实验设计**主线上，两篇论文分别处理了不同场景下的识别与检验问题。Inference in cluster randomized trials with matched pairs 聚焦于配对匹配整群随机试验，推导了加权均值差估计量的渐近分布，并提出了统一的方差估计量，同时考察了线性回归t检验的保守性及随机化检验的有效性，最后引入协变量调整以提升效率。Testing for strong exogeneity in Proxy-VARs 则在Proxy-VAR框架下检验强外生性假设，利用代理变量与滞后VAR残差的样本协方差构造统计量，无需额外识别假设即可检验该假设，并以货币政策冲击为例验证。两篇都涉及假设检验的渐近精确性，但前者侧重实验设计中的配对结构，后者侧重时间序列中的外生性检验。

**时间序列与持久性预测**主线包含两篇论文。Inference in predictive quantile regressions 处理预测变量近单位根时的分位数回归推断，推导了估计量与HAC t统计量的渐近分布，并提出一种切换式完全修正（FM）预测检验，在近单位根情形使用Bonferroni界修正，平稳时切换为标准检验，实证应用于股票收益分位数预测。On the spectral density of fractional Ornstein–Uhlenbeck processes 则提出一种谱密度解析近似方法，用于离散采样fOU过程，显著降低粗糙区域（H∈(0,0.5)）的近似误差，并基于此构造近似Whittle最大似然估计量，证明其相合性与渐近正态性。两篇都涉及持久性或长记忆过程，但前者关注分位数回归的推断，后者关注谱密度近似与参数估计。

此外，Why are replication rates so low? 从统计推断角度解释复制率低的原因，指出常用复制样本量设定方法忽略效应量估计误差，导致复制功效非线性偏低，并通过简约模型拟合实验经济学与心理学的复制数据。这篇论文虽属经济理论，但其核心机制（估计不确定性对复制率的影响）与因果推断中的敏感性分析有潜在关联。

与因果推断方向最贴的论文是 Inference in cluster randomized trials with matched pairs 和 Testing for strong exogeneity in Proxy-VARs；与半参数效率方向相关的是前者中的协变量调整部分；与高维/随机矩阵方向无直接关联；与时间序列推断方向相关的是 Inference in predictive quantile regressions 和 On the spectral density of fractional Ornstein–Uhlenbeck processes。

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105873](https://doi.org/10.1016/j.jeconom.2024.105873) · [arXiv](https://arxiv.org/abs/2211.14903) — Inference in cluster randomized trials with matched pairs
- **作者**: Yuehao Bai, Jizhou Liu, Azeem M. Shaikh, Max Tabord-Meehan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105873
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究配对匹配设计下整群随机试验的推断问题。目标估计量为加权均值差，关键设定是匹配是否基于集群规模。作者推导了两种情形下估计量的渐近分布，并提出一个统一的方差估计量，保证检验的渐近精确性。进一步分析了基于线性回归的t检验的保守性，并研究了配对内置换处理状态的随机化检验的有限样本与渐近有效性。最后提出协变量调整估计量，在额外基线协变量下可严格提升精度。模拟验证了理论结果的实际相关性。对您而言，本文在整群随机试验的配对设计下提供了严谨的推断工具，与您的因果推断（尤其是实验设计和敏感性分析）兴趣直接相关。
- **关键技术**: `weighted difference-in-means estimator`, `variance estimation`, `randomization test`, `covariate-adjusted estimator`, `asymptotic exactness`
- **为什么对您有用**: 本文直接关联您的因果推断兴趣中的实验设计（配对整群随机试验），提供了方差估计和检验的渐近理论。您的武器库中'非参数统计'和'因果推断中的估计理论'可立即用于理解其估计量的性质，而'半参数理论'可用于分析协变量调整估计量的效率增益。中期可做：将本文的配对设计思想与您的proximal causal inference框架结合，探索在未观测混杂下的识别策略。

### 2. [10.1016/j.jeconom.2024.105876](https://doi.org/10.1016/j.jeconom.2024.105876) — Testing for strong exogeneity in Proxy-VARs
- **作者**: Martin Bruns, Sascha A. Keweloh
- **期刊/来源**: Journal of Econometrics
- **机构**: University of East Anglia · Norwich Research Park · TU Dortmund University
- **分类**: vol 245 · issue 1-2 · pp 105876
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在 Proxy-VAR 框架下研究强外生性（strong exogeneity）的可检验性问题。Proxy-VAR 利用代理变量（proxy）识别结构 VAR 模型，其核心假设是代理变量与所有非目标冲击不相关（外生性）。作者指出，实践中常用的代理变量（如基于叙事法构造的变量）通常满足更强的外生性条件：代理变量不包含任何关于非目标冲击条件期望的信息。在一定的条件下，这种强外生性假设是可检验的，无需额外的识别假设。检验方法基于代理变量与滞后 VAR 残差的样本协方差构造统计量，并推导其渐近分布。模拟和实证研究（以货币政策冲击为例）验证了检验的有效性。对您而言，本文提供了一个在时间序列因果推断中检验工具变量外生性的新视角，与您 causal inference 方向中 IV 和 longitudinal 设定直接相关。
- **关键技术**: `Proxy-VAR`, `strong exogeneity`, `structural VAR`, `instrumental variables`, `specification test`
- **为什么对您有用**: 本文直接关联您 primary interest 中的 causal inference（IV 和 longitudinal 设定），特别是工具变量外生性假设的统计检验问题。您 moderately_familiar 中的 identification theory 可用于理解其识别条件，而 very_familiar 中的 high-dimensional asymptotics 可用于分析其检验统计量的渐近性质。中期可做：若将本文的检验思想推广到高维代理变量或非线性设定，需先在 moderately_familiar 的 semiparametric theory 上加强。

## 经济理论 / 应用  *(econ_theory, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105875](https://doi.org/10.1016/j.jeconom.2024.105875) · [arXiv](https://arxiv.org/abs/2306.00296) — Inference in predictive quantile regressions
- **作者**: Alex Maynard, Katsumi Shimotsu, Nina Kuriyama
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105875
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文研究预测分位数回归中的推断问题，当预测变量具有近单位根时。推导了分位数回归估计量及其HAC t统计量的渐近分布，表示为Ornstein-Uhlenbeck过程的泛函。提出了一种切换式完全修正（FM）预测检验，对近单位根情形采用Bonferroni界进行FM风格修正，当最大根处于平稳范围时切换为标准预测分位数回归检验（使用略保守的临界值）。模拟表明该检验在小样本下具有可靠的尺寸和良好的功效。实证部分用股息价格比、盈利价格比和账面市值比三个高持久性滞后估值变量预测股票收益分布的中位数、肩部和尾部。对您而言，本文是经济理论（金融计量）中处理持久性预测变量的分位数推断方法，其切换式FM修正思路可迁移至因果推断中弱工具变量或持久性暴露的敏感性分析。
- **关键技术**: `predictive quantile regression`, `near-unit root`, `Ornstein-Uhlenbeck process`, `fully modified (FM) correction`, `Bonferroni bound`, `HAC t-statistic`
- **为什么对您有用**: 本文属于经济理论（金融计量）方向，处理持久性预测变量下的分位数推断，是您secondary interest中经济理论的应用型工作。武器库中'非参数统计'和'高维渐近'可帮助理解其渐近分布推导，但核心工具（近单位根渐近、OU过程泛函）不在very_familiar或moderately_familiar中，属于暂不可做——需要先补充时间序列近单位根理论。不过作为gateway reading，本文实证部分的数据结构（高持久性估值变量预测收益分布尾部）对您进入金融计量领域有入门价值。

### 2. [10.1016/j.jeconom.2024.105868](https://doi.org/10.1016/j.jeconom.2024.105868) — Why are replication rates so low?
- **作者**: Patrick Vu
- **期刊/来源**: Journal of Econometrics
- **机构**: UNSW Sydney
- **分类**: vol 245 · issue 1-2 · pp 105868
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究社会科学中复制率低的原因，重点关注复制研究样本量设定方法的问题。作者构建了一个简单的发表过程模型，证明即使原始研究无偏，复制率也会低于名义目标。核心机制是：常用的复制样本量设定方法假设原始效应量是固定真实值，但复制功效函数存在非线性，忽略效应量估计误差会导致复制率系统性偏低。实证上，一个仅考虑此问题的简约模型能完全解释实验经济学和社会科学的复制率，以及心理学三分之二的复制差距。最后给出实用建议。对您而言，本文是经济理论方向的应用因果推断入门读物，展示了估计不确定性在复制研究中的关键作用。
- **关键技术**: `power analysis`, `sample size planning`, `replication rate`, `publication bias`, `effect size estimation`
- **为什么对您有用**: 本文属于经济理论方向的应用因果推断，是gateway-reading范畴。武器库中的'估计理论在因果推断中的应用'足以理解其核心论证，但本文是实证导向，不涉及新方法学。作为入门读物，它清晰阐述了复制率问题的统计根源，值得花时间读全文以了解经济学的复制危机讨论。

## 其他  *(other, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105872](https://doi.org/10.1016/j.jeconom.2024.105872) — On the spectral density of fractional Ornstein–Uhlenbeck processes
- **作者**: Shuping Shi, Jun Yu, Chen Zhang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105872
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对离散采样分数阶 Ornstein–Uhlenbeck (fOU) 过程，提出一种新颖且易于实现的谱密度近似方法，显著降低了近似误差，尤其在粗糙区域（Hurst 参数 H∈(0,0.5)）表现突出。该方法基于谱密度的解析近似，避免了传统数值积分的高计算成本。作者进一步引入近似 Whittle 最大似然 (AWML) 估计量，利用该近似谱密度进行参数估计，并证明了当 H∈(0,1) 时 AWML 估计量具有相合性和渐近正态性，与经典 Whittle 最大似然方法类似。通过大量模拟，AWML 在有限样本下优于现有方法。实证部分应用于 40 个金融资产的交易量数据，估计的 Hurst 参数在 0.10 至 0.21 之间，表明粗糙动态。该工作为时间序列谱分析提供了计算高效的实用工具，但其方法学核心（谱密度近似与 Whittle 估计）与您的主要兴趣（因果推断、高维统计、U-统计量）无直接交集。
- **关键技术**: `Whittle maximum likelihood`, `spectral density approximation`, `fractional Ornstein–Uhlenbeck process`, `Hurst parameter estimation`, `rough volatility`
- **为什么对您有用**: 本文属于时间序列谱分析领域，与您的 primary interests（因果推断、高维统计、U-统计量）无直接关联。虽然 AWML 方法在计算效率上有优势，但缺乏与您武器库中具体工具（如高阶 U-统计量的树宽分析、极小极大界）的连接点。作为 gateway reading 价值有限，因为其统计模型（fOU 过程）和问题设定（谱密度估计）偏离您的核心方向。暂不可做：核心机器（谱分析、Whittle 似然）不在武器库中。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

