# J. Econometrics — Vol 256  ·  2026-06-21

- 共 2 篇 · Journal of Econometrics
- 目录核对 ⚠️ 疑似漏 9 篇（对照 OpenAlex 11 篇）：10.1016/j.jeconom.2026.106253、10.1016/j.jeconom.2026.106267、10.1016/j.jeconom.2026.106254、10.1016/j.jeconom.2026.106242、10.1016/j.jeconom.2026.106264 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

J. Econometrics Vol 256 的两篇论文均聚焦于因果识别中的结构性挑战——内生性与测量误差，但分别在不同数据设定下展开。一篇关注面板数据中时变内生随机系数（Identification and estimation in a time-varying endogenous random coefficient panel data model），另一篇处理代际流动性分析中 outcome 和 treatment 同时存在测量误差的双边情形（Distributional effects with two-sided measurement error: An application to intergenerational income mobility）。两篇的共同主线是：在非标准干扰下恢复关键因果参数（平均部分效应、局部平均响应函数、转移矩阵等）的识别条件与估计方法。

“时变内生随机系数面板数据模型”通过引入充分统计量控制固定效应、控制变量控制个体特异随机冲击，将回归变量剩余变异仅由外生工具变量驱动，从而实现平均部分效应（APE）与局部平均响应函数（LARF）的识别，并构建三步级数估计量，给出渐近理论。该文以中国企业生产函数为例展示应用，对面板数据中异质性与内生性并存的问题提供了可操作框架。

“双边测量误差的代际分布效应”则从分位数回归测量误差框架入手，对 outcome 和 treatment 分别建立线性 QR 模型，结合对称性假设即可恢复联合分布，进而识别转移矩阵、rank-rank 相关性等分布效应参数。该方法无需工具变量或重复测量，也未对测量误差分布做参数假设，为处理两端都有测量误差的因果分析提供了替代路径。

两篇均与因果推断紧密相关：第一篇适合关注面板数据 IV、随机系数与非参级数估计的读者，第二篇适合关注测量误差下分布因果参数识别（特别是代际流动性）的研究者。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106272](https://doi.org/10.1016/j.jeconom.2026.106272) · [arXiv](https://arxiv.org/abs/2110.00982) — Identification and estimation in a time-varying endogenous random coefficient panel data model
- **作者**: Ming Li
- **期刊/来源**: Journal of Econometrics
- **机构**: National University of Singapore
- **分类**: vol 256 · pp 106272
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一个时变内生随机系数线性面板数据模型，允许回归变量通过固定效应和时变随机冲击与个体特异随机系数相关。目标是识别平均部分效应（APE）和局部平均响应函数（LARF）。识别策略采用一个充分统计量控制固定效应，一个控制变量控制随机冲击，使得条件于这两个控制后，回归变量的剩余变异仅由外生工具变量驱动。利用此识别条件，构建了三步级数估计量，并证明了收敛速度和渐近正态性。该方法通过估计中国制造业企业的异质性Cobb-Douglas生产函数进行说明，发现产出弹性在企业间存在显著差异。这对您的主要兴趣——因果推断中的面板数据、IV和纵向数据识别——直接相关，且级数估计量的理论分析可借用您熟悉的非参数统计和因果推断工具。
- **关键技术**: `control function`, `sufficient statistic`, `series estimator`, `panel data`, `random coefficient model`
- **为什么对您有用**: 该论文直接连接到您的主要兴趣：因果推断中的面板数据、IV和纵向数据识别。您熟悉的非参数统计和因果推断理论（如级数估计、控制函数）可以直接用于理解和评估该方法的性质。它提供了一个在时变随机系数设定下识别平均效应的新框架，您可以基于此探索更高效的估计量或进行敏感性分析——目前属于立即可做的方向，无需额外工具。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106268](https://doi.org/10.1016/j.jeconom.2026.106268) · [arXiv](https://arxiv.org/abs/2107.09235) — Distributional effects with two-sided measurement error: An application to intergenerational income mobility
- **作者**: Brantly Callaway, Tong Li, Irina Murtazashvili, Emmanuel S. Tsyawo
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 106268
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在双变量均存在测量误差（two-sided measurement error）的设定下，本文研究代际收入流动性中分布效应参数（如转移矩阵、rank-rank 相关性、条件贫困率）的 identification 与估计。核心机制基于 Hausman et al. (2021) 的分位数回归测量误差框架，对 outcome 和 treatment 分别建立线性 QR 模型，结合对两变量测量误差的特定假设（如对称性），即可恢复 outcome 与 treatment 的联合分布。该方法无需工具变量、重复测量或测量误差的分布假设，直接从 QR 系数与误差矩条件出发完成 identification。实证应用 NLSY97 数据表明，校正测量误差后多项代际流动性参数估计值显著下降。对您可能有用：该文展示了在缺乏 IV/repeated measurements 时如何用 QR 框架处理双侧测量误差下的分布效应 identification，为因果推断中测量误差敏感性分析提供了新视角。
- **关键技术**: `quantile regression with measurement error`, `two-sided measurement error identification`, `joint distribution recovery`, `transition matrix estimation`, `rank-rank correlation`
- **为什么对您有用**: (1) 直接连接 econ_theory 子方向中的代际流动性数据集与模型，且其 identification 策略（无 IV 下处理双侧测量误差）对 causal inference 的 measurement error sensitivity 分析有明确参考价值。(2) 您 technical_arsenal 中的 identification theory in causal inference（moderately_familiar）可直接切入：该文完全绕开 IV，仅靠 QR 系数与误差矩条件完成 identification，您可审视其假设的强度与可替代性，或用 semiparametric theory 探讨其估计效率。(3) **中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以评估该 QR-based identification 在非参数/半参数扩展下的 robustness 及可能的效率改进。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

