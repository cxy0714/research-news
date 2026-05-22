# J. Econometrics — Vol 241  Issue 1  ·  2026-05-21

- 共 7 篇 · Journal of Econometrics

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1016/j.jeconom.2024.105735](https://doi.org/10.1016/j.jeconom.2024.105735) — A vector monotonicity assumption for multiple instruments
- **作者**: Leonard Goff
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105735
- 相关性 9/10 · novelty: `weaker_assumption`
- **摘要**: 在多工具变量（IV）对单一二元处理的设定下，传统 LATE 单调性假设要求所有个体对不同 IV 有共同方向的响应，这在 IV 作用方向相反时过于严格。本文提出“向量单调性”（vector monotonicity）假设，仅要求处理状态对每个 IV 分别单调（即每个 IV 下“无违抗者”）。在此假设下，作者证明了一类因果参数（对特定 IV 子集有响应的子群体的 ATE）是点识别的。估计方面，提出了一个类 2SLS 的简单估计量。实证部分将其应用于大学教育的劳动力市场回报。对您有用：直接推进您 primary interest 中 IV 识别与估计的理论，放松了多 IV 场景的单调性假设，且提供了经济学的实证应用范式。
- **关键技术**: `vector monotonicity`, `multiple instrumental variables`, `LATE monotonicity`, `point identification`, `2SLS-like estimator`, `complier average treatment effect`
- **为什么对您有用**: 直接推进您 primary interest 中的 IV 识别与估计理论，放松了多 IV 设定下的单调性假设；同时作为经济学因果推断应用，契合您 secondary interest 中对经济模型与实证因果分析的关注。

### 2. [10.1016/j.jeconom.2024.105738](https://doi.org/10.1016/j.jeconom.2024.105738) — Testing identification conditions of LATE in fuzzy regression discontinuity designs
- **作者**: Yu-Chin Hsu, Ji-Liang Shiu, Yuanyuan Wan
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105738
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文在模糊断点回归设计框架下，研究局部平均处理效应（LATE）识别条件的可检验含义，目标是在标准正则性假设下验证 IV 识别假设的成立性。作者证明这些识别条件（如单调性或排他性约束）的可检验含义可转化为对可观测数据分布的有限个不等式约束。基于此，提出了一种针对该不等式约束的设定检验，并证明该检验能够严格控制第一类错误且具有渐近一致性。实证部分将该方法应用于文献中的多个模糊 RD 实例以验证其实用性。对您有用：该文将因果推断中 IV 的识别假设检验转化为不等式约束检验，直接契合您对因果识别与假设检验的双重兴趣，并为模糊 RD 的应用提供了严谨的规范性检验工具。
- **关键技术**: `fuzzy regression discontinuity`, `local average treatment effect`, `testable implications of identification`, `inequality restrictions testing`, `specification test`
- **为什么对您有用**: 直接契合您在因果推断（IV/识别）与数理统计（假设检验）的交叉兴趣：将模糊 RD 中 LATE 的识别条件转化为不等式约束并进行 size-controlled 的规范检验，为 IV 识别假设提供了可操作的检验工具。

### 3. [10.1016/j.jeconom.2024.105724](https://doi.org/10.1016/j.jeconom.2024.105724) — No star is good news: A unified look at rerandomization based on <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si4.svg" display="inline" id="d1e636"><mml:mi>p</mml:mi></mml:math>-values from covariate balance tests
- **作者**: Anqi Zhao, Peng Ding
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105724
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在随机实验中基于协变量平衡检验 $p$ 值的重随机化（ReP）方案对后续 ATE 推断的影响，设定为经典潜在结果模型。作者聚焦于未调整、加性和完全交互线性回归下的三种 ATE 估计量，推导了它们在 ReP 下的渐近抽样性质。核心发现有二：一是完全交互回归估计量在所有 ReP 方案下渐近最有效，且其回归辅助推断与完全随机化下完全一致；二是 ReP 不仅改善协变量平衡，也渐近提升了未调整和加性估计量的效率。因此，标准回归分析在 ReP 下仍有效但趋于保守。该文将假设检验（$p$ 值阈值筛选）与因果推断中的效率理论（渐近方差比较）紧密结合，对您理解重随机化设计下的有效推断与方差缩减机制具有直接参考价值。
- **关键技术**: `rerandomization`, `covariate balance test`, `asymptotic efficiency`, `average treatment effect`, `regression-assisted inference`
- **为什么对您有用**: 直接连接您在因果推断（ATE估计与实验设计）和假设检验（基于p值的重随机化）的兴趣，并涉及效率理论（比较不同回归调整估计量的渐近方差），为重随机化下的有效推断提供理论依据。

### 4. [10.1016/j.jeconom.2024.105727](https://doi.org/10.1016/j.jeconom.2024.105727) — Wild bootstrap inference for instrumental variables regressions with weak and few clusters
- **作者**: Wenjie Wang, Yichong Zhang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105727
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在少数大聚类（few large clusters）设定下，工具变量（IV）回归的 wild bootstrap 推断问题，关注弱工具变量与聚类结构交织时的 size control 与 power。首先证明，只要内生变量参数在至少一个聚类中被强识别，wild bootstrap Wald 检验即可渐近控制 size（误差极小）。进一步提出 wild bootstrap Anderson-Rubin (AR) 检验，证明即使在所有聚类均存在弱识别时，该全向量推断检验仍能渐近控制 size。此外，建立了 bootstrap 检验对局部替代假设的 power 条件。仿真与对美国本地劳动力市场数据的应用验证了方法的有效性。对您有用：直接推进了因果推断中 IV 的假设检验理论（弱识别/少聚类下的 size/power），且实证部分为经济因果应用提供了可迁移的分析流程。
- **关键技术**: `wild bootstrap`, `instrumental variable regression`, `weak identification`, `Anderson-Rubin test`, `few clusters inference`
- **为什么对您有用**: 直接推进了因果推断中 IV 的假设检验理论（弱识别下的 size/power），且实证部分涉及经济因果应用，方法与数据集对您的 IV 与假设检验兴趣均有直接价值。

### 5. [10.1016/j.jeconom.2024.105740](https://doi.org/10.1016/j.jeconom.2024.105740) — Covariate adjustment in experiments with matched pairs
- **作者**: Yuehao Bai, Liang Jiang, Joseph P. Romano, Azeem M. Shaikh, Yichong Zhang
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105740
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在配对实验（matched pairs）设定下，如何利用未参与配对的基线协变量调整以提高平均处理效应（ATE）的估计精度。基于双重稳健（doubly robust）矩条件，文章统一研究了有限维和高维形式的协变量调整估计器。理论证明，有限维线性调整（即使包含处理交互项）相对于未调整的均值差估计器无法提升精度，而加入配对固定效应（pair fixed effects）则是最优的有限维线性调整。对于基于 LASSO 的高维调整，文章证明其必定能提升精度，且在特定条件下可达到最优非参数协变量调整的半参数效率界。模拟与实证分析（宏观保险对微型企业的影响）验证了上述理论。该文对配对设计下协变量调整的效率界刻画及高维调整的最优性分析，直接连接到您关注的因果推断估计理论与半参数效率界方向。
- **关键技术**: `doubly robust moment condition`, `matched pairs design`, `pair fixed effects`, `high-dimensional LASSO adjustment`, `semiparametric efficiency bound`, `optimal covariate adjustment`
- **为什么对您有用**: 直接连接到因果推断的估计理论和效率理论（半参数效率界）。文章对配对设计下有限维/高维调整的效率分析，为实验设计中的协变量调整提供了精确的理论指导，对您研究 debiased ML 或高维因果推断中的效率提升有直接参考价值。

## 经济理论 / 应用  *(econ_theory, 2 篇)*

### 1. [10.1016/j.jeconom.2024.105742](https://doi.org/10.1016/j.jeconom.2024.105742) — The law of large numbers for large stable matchings
- **作者**: Jacob Schwartz, Kyungchul Song
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105742
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 在大规模双边稳定匹配市场（如大学招生）设定下，研究者观察到全部或部分匹配结果，目标是建立经验匹配概率的渐近理论。作者在允许学生偏好完全异质、但大学偏好存在强相关的假设下，推导了经验匹配概率的集中不等式。该方法不依赖独立同分布假设，而是处理了稳定匹配机制带来的复杂依赖结构，由此导出了经验匹配概率及其他常用统计量的大数定律。作为理论应用，文章证明了条件匹配概率估计量与正向分类匹配度量的估计量的一致性。对您有用：该文将集中不等式应用于具有内生依赖结构的计量模型，其处理非 i.i.d 依赖数据的概率界技术，对您在因果推断或经济理论中分析复杂依赖数据（如网络/匹配）的渐近性质有方法论借鉴意义。
- **关键技术**: `stable matching`, `concentration inequality`, `law of large numbers`, `dependent data`, `assortative matching`
- **为什么对您有用**: 属于经济理论中的计量经济基础工作；其在不依赖 i.i.d 假设下推导集中不等式与 LLN 的技术，对您在因果推断中处理复杂依赖结构（如网络或匹配数据）的渐近理论有直接参考价值。

### 2. [10.1016/j.jeconom.2024.105709](https://doi.org/10.1016/j.jeconom.2024.105709) — Spectral clustering with variance information for group structure estimation in panel data
- **作者**: Lu Yu, Jiaying Gu, Stanislav Volgushev
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 241 · issue 1 · pp 105709
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在面板数据设定下，假设个体存在共享相似效应的未知潜在分组，目标是利用方差信息进行分组结构估计。局部分析表明个体系数估计量的方差包含分组的有用信息；据此提出一种显式利用方差信息的谱聚类方法，适用于一般面板数据模型。该方法在大N和大T下保持计算可行性，且仅需参数估计及其不确定性度量（无需原始个体数据）即可实施。模拟显示其优于现有方法，并应用于两个实证案例。对您有用：该文将方差/不确定性信息融入谱聚类进行分组估计，思路可迁移至高维统计或因果推断中处理异质性与分组结构的问题，且符合您对经济模型与数据集的次级兴趣。
- **关键技术**: `spectral clustering`, `panel data group structure`, `variance information`, `uncertainty quantification`, `large N and T asymptotics`
- **为什么对您有用**: 直接契合您在经济理论（面板数据模型、实证应用）方面的次级兴趣；同时，利用估计量的方差信息（不确定性）改进谱聚类的思路，对高维统计或因果推断中处理异质性与分组结构具有方法迁移价值。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

