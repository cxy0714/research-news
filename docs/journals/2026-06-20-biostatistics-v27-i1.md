# Biostatistics — Vol 27  Issue 1  ·  2026-06-20

- 共 2 篇 · Biostatistics
- 目录核对 ⚠️ 疑似漏 18 篇（对照 OpenAlex 20 篇）：10.1093/biostatistics/kxaf052、10.1093/biostatistics/kxag011、10.1093/biostatistics/kxag001、10.1093/biostatistics/kxag004、10.1093/biostatistics/kxag006 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期仅收录两篇论文，分属因果推断与半参数/非参两个主题，但每篇都在各自方向上给出了有深度的方法论扩展。整体来看，一条主线是**因果识别与政策学习在干扰网络下的推广**，另一条是**功能数据分析的分位数拓展与层级分解**。

**因果识别与最优政策学习**：第一篇论文将个体层面的Q-Learning与A-Learning扩展至二分网络干扰（BNI）场景，允许干扰结构任意而不限于局部或对称设定。其核心贡献在于直接学习最小化期望损失的最优干预规则而非仅估计平均因果效应，并在理论层面推导了所提估计量的渐近性质。实证上的应用（电厂scrubber对社区健康的影响）展示了该框架在实际成本约束下的政策优化能力，适合关注因果推断中干扰与政策学习的读者。

**功能数据分析的分位数拓展**：第二篇论文针对多层功能数据（如受试者内部的重复测量），提出了分位数主成分分析（MFQPCA），将传统的均值主成分分解推广到各分位数水平，从而揭示变异随条件分布位置不同的变化。算法采用交替最小化，并提供了R包FunQ。这对于需要解析层级功能数据中分布尾部变异的研究，如生物医学中的加速度计或神经影像数据，具有直接实用价值。

因果推断方向的读者可优先关注第一篇；若研究涉及功能数据的分位数建模或多层结构，第二篇值得细读。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.1093/biostatistics/kxaf041](https://doi.org/10.1093/biostatistics/kxaf041) · [arXiv](https://arxiv.org/abs/2410.08362) — Towards optimal environmental policies: policy learning under arbitrary bipartite network interference
- **作者**: Raphael C Kim, Falco J Bargagli-Stoffi, Kevin L Chen, Rachel C Nethery
- **期刊/来源**: Biostatistics
- **分类**: vol 27 · issue 1
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在 bipartite network interference (BNI) 设定下，目标是学习最优干预政策以最小化受干扰单元的期望损失，其中干预施加于一侧（电厂），结果观测于另一侧（社区），且干扰结构任意。本文将 Q-Learning 与 A-Learning 从经典个体干预扩展至 BNI 场景，通过估计干扰下的价值函数与反事实结果来学习最优政策规则。理论上推导了所提估计量的渐近性质，仿真验证了有限样本表现。实证应用 Medicare 数据与污染传输网络，在多种成本约束下寻找安装电厂 scrubber 的最优策略，可使缺血性心脏病住院率降低 23.37–55.30/万人年。对您有用：本文将政策学习拓展至网络干扰设定，直接连接因果推断中的 longitudinal/IV 与 semiparametric efficiency 理论。
- **关键技术**: `Q-Learning under interference`, `A-Learning under interference`, `bipartite network interference`, `policy learning with cost constraints`, `asymptotic properties of policy estimators`
- **为什么对您有用**: (1) 直接连接 causal inference 的 policy learning 与 network interference 设定，属于因果推断中 interference / spillover 的前沿子方向。(2) 本文的 Q/A-Learning 渐近理论可尝试用您 very_familiar 的 M-estimation theory 与 moderately_familiar 的 semiparametric theory 来审视其效率界是否达到，或用 HOIF 视角探索更高阶修正。(3) **中期可做**：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以推导 BNI 下最优政策的 semiparametric efficiency bound 并验证本文估计量是否 efficient。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.1093/biostatistics/kxag017](https://doi.org/10.1093/biostatistics/kxag017) — Multilevel functional quantile principal component analysis
- **作者**: Álvaro Méndez-Civieta, Ying Wei, Jeff Goldsmith
- **期刊/来源**: Biostatistics
- **机构**: Universidad Carlos III de Madrid · Columbia University
- **分类**: vol 27 · issue 1
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 在多层（层级）功能数据设定下，本文目标是分解功能数据在不同分位数水平下的变异来源，而非仅聚焦均值曲线。作者提出 Multilevel Functional Quantile PCA (MFQPCA)，将 Functional Quantile PCA 扩展至层级结构，把分位数特异的变异分解为 between-participant 与 within-participant 两层，并估计各层与各分位数下的共享模式与得分。核心算法采用 alternating minimization 实现高效求解，开源 R 包 FunQ 提供了完整实现。实证分析使用充血性心力衰竭患者 4-9 月的加速度计数据，揭示久坐期变异主要来自日内波动，而剧烈活动期变异主要来自个体间差异。对您而言，本文在层级功能数据的分位数分解与 alternating minimization 计算框架上提供了具体参考，可连接到您对 semiparametric/nonparametric 变异分解与统计计算的兴趣。
- **关键技术**: `functional quantile PCA`, `multilevel variance decomposition`, `alternating minimization algorithm`, `hierarchical functional data`, `quantile-specific principal components`
- **为什么对您有用**: 本文连接到您 primary interest 中的 semiparametric/nonparametric theory（功能数据的分位数而非均值建模）与 statistical computing（alternating minimization 算法与 R 包实现）。您武器库中 very_familiar 的 software development 与 moderately_familiar 的 M-estimation theory 可直接攻入其 alternating minimization 的收敛性与计算效率分析，或将其分位数变异分解框架推广至更一般的 semiparametric 层级模型。Follow-up 判断：立即可做——可用 M-estimation 理论审视其算法的收敛保证，并用软件开发能力复现或扩展 FunQ 包。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

