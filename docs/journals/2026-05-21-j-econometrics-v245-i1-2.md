# J. Econometrics — Vol 245  Issue 1-2  ·  2026-05-21

- 共 5 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105873](https://doi.org/10.1016/j.jeconom.2024.105873) — Inference in cluster randomized trials with matched pairs
- **作者**: Yuehao Bai, Jizhou Liu, Azeem M. Shaikh, Max Tabord-Meehan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105873
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究配对设计下整群随机化试验的因果推断与假设检验问题，目标是在基线协变量配对且群内随机分配处理的设定下对平均处理效应进行有效推断。作者研究了加权均值差估计量的大样本性质，区分了是否按群规模进行配对两种情形，并提出了一种在两种情形下均一致的单一方差估计量，从而保证了相关检验的渐近精确性。进一步证明基于线性回归构造的常用 t 检验在此框架下通常是保守的。同时，考察了群内对换处理状态的随机化检验，建立了其有限样本与渐近有效性。最后提出利用未用于配对的基线协变量进行调整的估计量，并在一定条件下证明了其能严格提升估计精度。对您有用：该文对实验设计下方差估计与检验保守性的精细分析，以及协变量调整实现严格精度提升的理论，直接关联您对因果推断中假设检验与效率理论的兴趣。
- **关键技术**: `matched pairs design`, `cluster randomized trials`, `weighted difference-in-means`, `randomization inference`, `covariate adjustment`, `asymptotic exactness`
- **为什么对您有用**: 本文对配对整群实验中方差估计与检验保守性的精细推导，以及对协变量调整实现严格精度（效率）提升的理论证明，直接关联您在因果推断（实验设计下的假设检验）和效率理论（协变量调整的效率增益）方面的核心兴趣。

### 2. [10.1016/j.jeconom.2024.105876](https://doi.org/10.1016/j.jeconom.2024.105876) — Testing for strong exogeneity in Proxy-VARs
- **作者**: Martin Bruns, Sascha A. Keweloh
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105876
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在 Proxy-VAR（代理变量向量自回归）框架下，研究目标是检验代理变量的强外生性假设，即代理变量不包含非目标冲击条件期望的任何信息，而不仅是传统的零相关。传统上代理变量（类似 IV）的外生性仅依赖经济逻辑论证，缺乏正式的统计检验。本文论证了在无需额外识别假设的条件下，这种强外生性概念是可检验的，并提出了相应的假设检验方法。核心机制在于将强外生性转化为 VAR 系统中关于预期信息的可测矩条件，从而允许使用标准统计推断。理论结果为宏观 Proxy-SVAR 模型的识别提供了统计验证途径。对您有用：直接连接因果推断中的 IV/Proxy 假设检验，为评估工具变量外生性提供了从定性论证走向定量检验的新方法。
- **关键技术**: `Proxy-VAR`, `strong exogeneity test`, `instrument validity`, `structural VAR identification`, `moment conditions`
- **为什么对您有用**: 直接回应您在因果推断中对 IV 识别假设的关注，提供了检验 Proxy/IV 外生性的统计检验方法，同时契合假设检验与经济理论中的因果推断应用。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105875](https://doi.org/10.1016/j.jeconom.2024.105875) — Inference in predictive quantile regressions
- **作者**: Alex Maynard, Katsumi Shimotsu, Nina Kuriyama
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105875
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究预测性分位数回归中，当预测变量具有近单位根时的推断问题，目标是在局部单位根假设下对分位数可预测性进行假设检验。作者推导了分位数回归估计量及其 HAC t 统计量的渐近分布，其极限分布由 Ornstein-Uhlenbeck 过程的泛函给出。提出了一种 switching-fully modified (FM) 预测检验：当预测变量为近单位根时，采用 FM 修正并结合 Bonferroni 界处理局部单位根参数；当预测变量最大根在平稳范围内时，切换为带有略微保守临界值的标准预测分位数回归检验。模拟表明该检验在小样本下具有可靠的水平和良好的功效，实证分析将其应用于股息价格比等持久内生滞后估值回归变量对股票收益分布的预测。对您而言，该文将单位根理论中的 FM 修正与分位数回归结合，其 switching 检验构造和 Bonferroni 界处理 nuisance parameter 的技巧，对研究假设检验与经济理论交叉方向具有参考价值。
- **关键技术**: `predictive quantile regression`, `local-to-unity asymptotics`, `fully modified (FM) correction`, `Bonferroni bound`, `Ornstein-Uhlenbeck process functional`, `HAC t-statistic`
- **为什么对您有用**: 本文核心是构造存在近单位根 nuisance parameter 时的假设检验，属于数学统计（假设检验）与经济理论的交叉；其处理 nuisance parameter 的 Bonferroni switching 策略和 FM 修正技巧，对您在计量经济设定下的检验问题有直接借鉴意义。

### 2. [10.1016/j.jeconom.2024.105868](https://doi.org/10.1016/j.jeconom.2024.105868) — Why are replication rates so low?
- **作者**: Patrick Vu
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105868
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究社会科学中复制成功率偏低的问题，在原始研究无偏的设定下，聚焦于复制研究样本量计算方法的理论缺陷。核心机制在于，常规方法将原始估计效应量视为固定真实值来设定名义检验效能，但忽略了其估计误差。由于复制效能函数关于原始效应量具有非线性，忽略估计误差会导致期望效能系统性低于名义目标（类似Jensen不等式效应）。理论上证明了即使原始研究无偏，这种样本量设定偏差也会导致实际复制率低于名义目标。实证表明，仅包含此偏差的简约模型即可完全解释实验经济学中的观测复制率，及心理学中三分之二的复制缺口。对您有用：该文从效能函数非线性视角揭示了假设检验的系统性偏差，对您在假设检验与经济理论交叉方向的理解有直接启发。
- **关键技术**: `replication power function`, `sample size calculation`, `publication bias model`, `Jensen's inequality effect`, `expected power`
- **为什么对您有用**: 论文从检验效能函数的非线性（Jensen不等式）角度解释了假设检验中复制率偏低的现象，属于假设检验与经济理论（实验经济学）的交叉，对理解实际应用中统计方法的系统性偏差有直接参考价值。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.1016/j.jeconom.2024.105872](https://doi.org/10.1016/j.jeconom.2024.105872) — On the spectral density of fractional Ornstein–Uhlenbeck processes
- **作者**: Shuping Shi, Jun Yu, Chen Zhang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 245 · issue 1-2 · pp 105872
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文研究离散采样分数Ornstein–Uhlenbeck (fOU) 过程的谱密度逼近问题，目标是在Hurst参数 H∈(0, 0.5) 的粗糙区域实现高精度逼近。作者提出一种新颖且易于实现的近似谱密度方法，显著降低了传统方法在粗糙区域的逼近误差。基于该近似谱密度，构建了近似Whittle极大似然 (AWML) 估计量，并严格证明了其在 H∈(0, 1) 全区间内的一致性与渐近正态性。大量模拟表明，AWML在有限样本下的估计精度优于现有方法。对40个金融资产交易量的实证应用显示Hurst参数估计值介于0.10至0.21，揭示了金融交易量的粗糙动态特征。该工作对您在经济理论（金融时间序列模型与实证数据）的兴趣有直接参考价值，其基于谱密度的推断框架也对数学统计中的假设检验与统计计算中的数值逼近方法有借鉴意义。
- **关键技术**: `spectral density approximation`, `fractional Ornstein-Uhlenbeck process`, `approximate Whittle maximum likelihood`, `asymptotic normality`, `rough dynamics`
- **为什么对您有用**: 契合您在经济理论（金融时间序列模型与实证数据集）的次要兴趣；同时，其基于谱密度的推断框架对您在数学统计（假设检验）与统计计算（数值逼近）方面的主要兴趣有方法论借鉴。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

