# J. Econometrics — Vol 253  ·  2026-07-06

- 共 2 篇 · Journal of Econometrics
- 目录核对 ⚠️ 疑似漏 36 篇（对照 OpenAlex 40 篇）：10.1016/j.jeconom.2026.106183、10.1016/j.jeconom.2025.106161、10.1016/j.jeconom.2025.106125、10.1016/j.jeconom.2025.106130、10.1016/j.jeconom.2025.106153 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Journal of Econometrics》第253卷仅收录两篇论文，分别聚焦于因果推断中的两阶段估计与推断问题，以及高频金融数据中的跳跃检测。两篇论文在方法上均涉及非标准推断框架（准贝叶斯与单边噪声模型），但主题差异较大，未形成明显主线。整体来看，本期内容偏向于特定应用场景下的方法论创新，而非通用技术突破。

在因果推断方向，**Quasi-Bayesian estimation and inference with control functions** 针对结构离散选择模型中控制函数法的两阶段推断困境，提出了一种混合推断策略：第一阶段使用频率学派估计控制函数，第二阶段采用贝叶斯方法处理结构方程。论文的核心发现是，直接使用准后验构造的置信集在大样本下覆盖概率不正确，但通过bootstrap校正第一阶段不确定性后，可恢复有效推断。理论贡献包括准后验的Bernstein-von Mises型性质及bootstrap后验的覆盖概率校正。这篇论文对因果推断研究者尤其有价值，因为它直接关联内生性处理与两阶段推断的统计性质。

在高频金融方向，**Jump detection in high-frequency order prices** 针对限价订单簿中最佳卖价受单边噪声（仅向上偏差）影响的特点，提出基于局部最小值的跳跃检测方法。论文构建了局部跳跃检验，并证明了跳跃大小与时间的一致性估计；全局跳跃检验则基于极值理论推导了无跳跃原假设下最大统计量的渐近分布，且在备择假设下具有一致性。局部备择假设的收敛速度远快于标准市场微观结构噪声模型，能识别更小的跳跃。此外，还建立了单边噪声下已实现波动率估计的一致性与均匀收敛性质。这篇论文适合高频计量与金融统计方向的研究者。

对于因果推断方向的研究者，**Quasi-Bayesian estimation and inference with control functions** 是本期最直接相关的论文，其关于两阶段推断中不确定性校正的讨论具有方法论意义。对于高频计量与极值理论方向的研究者，**Jump detection in high-frequency order prices** 提供了针对单边噪声的新检测框架。两篇论文均未涉及高维或半参数效率等主题。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1016/j.jeconom.2025.106126](https://doi.org/10.1016/j.jeconom.2025.106126) · [arXiv](https://arxiv.org/abs/2402.17374) — Quasi-Bayesian estimation and inference with control functions
- **作者**: Ruixuan Liu, Zhengfei Yu
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 253 · pp 106126
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文研究两阶段推断中第一阶段使用频率学派估计、第二阶段使用贝叶斯方法的准贝叶斯方法，其动机来自结构离散选择模型中用控制函数纠正内生性偏差的问题。第一阶段通过参数或非参数方法估计控制函数，第二阶段的结构方程因似然函数复杂而更适合贝叶斯处理。作者证明了第二阶段得到的准后验分布构造的置信集在大样本下不具有正确的覆盖概率，但准贝叶斯点估计量是一致的且渐近等价于频率学派的两阶段估计量。进一步，通过对准后验进行bootstrap（考虑第一阶段估计不确定性）可以获得有效的推断。理论结果包括准后验的Bernstein-von Mises型性质及bootstrap后验的覆盖概率校正。本文对您有用的点：直接关联因果推断中IV/控制函数的内生性处理，且其两阶段不确定性传播问题与您熟悉的semiparametric efficiency bound和debiased ML中的正交性思想有深层联系。
- **关键技术**: `control function`, `quasi-Bayesian`, `two-stage estimation`, `bootstrap inference`, `Bernstein-von Mises theorem`, `endogeneity correction`
- **为什么对您有用**: 直接关联您primary interest中的因果推断（IV/控制函数）和semiparametric theory（两阶段估计的不确定性传播）。您的武器库中'identification theory in causal inference'和'semiparametric theory'可用来分析其bootstrap后验校正是否达到semiparametric efficiency bound，而'higher-order U-statistics'的树宽视角可能用于刻画其bootstrap计算复杂度。中期可做：需先在moderately_familiar的HOIF上长肌肉，以严格分析其bootstrap后验的一阶与二阶渐近性质。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1016/j.jeconom.2025.106133](https://doi.org/10.1016/j.jeconom.2025.106133) · [arXiv](https://arxiv.org/abs/2403.00819) — Jump detection in high-frequency order prices
- **作者**: Markus Bibinger, Nikolaus Hautsch, Alexander Ristig
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 253 · pp 106133
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对限价订单簿中高频订单价格数据，提出了一类跳跃检测方法。与经典的双边市场微观结构噪声模型不同，本文考虑单边噪声（即最佳卖价仅受向上偏差影响），将价格过程建模为半鞅。方法核心是利用局部最小值（local minima of best ask quotes）来估计、定位和检验跳跃。作者构建了局部跳跃检验，并证明了跳跃大小和跳跃时间的一致性估计。主要贡献是全局跳跃检验：基于极值理论推导了无跳跃原假设下最大统计量的渐近分布，并证明了备择假设下的一致性。局部备择假设的收敛速度远快于标准市场微观结构噪声模型下的最优速率，从而能识别更小的跳跃。此外，还建立了单边噪声下已实现波动率估计的一致性和均匀收敛性。模拟和实证分析展示了方法的有限样本性能，并与经典方法进行了对比。该文对您在高频金融数据中应用假设检验和极值理论有直接参考价值，尤其其全局检验的渐近最优性分析可迁移至您在高维统计中的检验问题。
- **关键技术**: `extreme value theory`, `maximum statistic`, `local jump test`, `global jump test`, `spot volatility estimation`, `one-sided microstructure noise`
- **为什么对您有用**: 本文属于假设检验方向，直接对应您 primary interest 中的 'hypothesis testing' 和 'high-frequency data' 设定。其全局检验的极值理论推导和局部备择假设的收敛速率分析，可借助您 very_familiar 的 'minimax bounds for estimation problems' 工具来验证其最优性是否紧。中期可做：若想将此类检验推广到更一般的半鞅模型，需先在 moderately_familiar 的 'M-estimation theory' 上提升对渐近分布推导的熟练度。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

