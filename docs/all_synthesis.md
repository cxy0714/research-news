# 选题提案

从你的精读语料 + 收藏里提炼**可上手的选题**。每条提案给：可投的标题、点名数学对象的 claim、先打哪个最简特例、哪几篇论文独立点名了这个 gap（附原话）、接你武器库的哪一件、什么会杀死它、以及第一周的具体动作。

> **怎么读**：战线按**你收藏了几篇**排（同数再看证据论文数）——都是**可数的事实**，不是质量分。系统不打分、不排名、不替你判断值不值得做，每条证据都点到论文原话，你自己核验。战线本身是先按「主兴趣 → 覆盖了你武器库的几个领域 → 收藏数」筛出来的，所以 `低度多项式` 这种收藏少但正中主兴趣的战线也在。

**本次生成**: 2026-09-01 · 16 条战线 · 37 条提案 · 候选池 1441 篇（score ≥ 8 或已收藏的精读）

---

## 战线一览

| 战线 | 证据论文 | ★ 收藏 | 提案 |
|---|---:|---:|---:|
| [U统计量与重抽样推断](proposals/hypothesis_testing_u_statistic_bootstrap_inference.md) | 140 | 23 | 2 |
| [非参数回归的极小极大率刻画](proposals/nonparam_semipara_minimax_rate_nonparametric_regression.md) | 98 | 22 | 2 |
| [双稳健估计与半参效率理论](proposals/causal_inference_doubly_robust_efficiency.md) | 124 | 18 | 2 |
| [去偏机器学习与正交分数理论](proposals/efficiency_dml_debiased_machine_learning_orthogonal.md) | 140 | 15 | 3 |
| [近端因果推断/负对照变量](proposals/causal_inference_proximal_causal_inference.md) | 107 | 15 | 3 |
| [高阶影响函数与高阶去偏估计](proposals/efficiency_dml_higher_order_influence_functions.md) | 59 | 15 | 2 |
| [共享奇异子空间与公共子空间的最优估计与推断](proposals/high_dim_rmt_subspace_estimation_inference.md) | 98 | 13 | 2 |
| [未测量混杂的敏感性分析](proposals/causal_inference_sensitivity_analysis_unmeasured_confounding.md) | 133 | 11 | 3 |
| [结构无关模型下的半参数效率与去偏](proposals/efficiency_dml_structure_agnostic_semiparametric.md) | 53 | 11 | 3 |
| [半参数效率与影响函数](proposals/nonparam_semipara_semiparametric_efficiency_influence_function.md) | 66 | 10 | 2 |
| [高维稀疏信号检测与相变](proposals/hypothesis_testing_high_dimensional_sparse_detection.md) | 45 | 9 | 2 |
| [非参数图模型与扩散模型选择](proposals/nonparam_semipara_nonparametric_graphical_model_diffusion.md) | 43 | 8 | 2 |
| [条件独立性检验与因果推断](proposals/hypothesis_testing_conditional_independence_testing.md) | 42 | 6 | 2 |
| [张量分解与黎曼优化](proposals/stat_computing_tensor_decomposition_optimization.md) | 39 | 6 | 2 |
| [低度多项式与计算-统计阈值](proposals/hypothesis_testing_low_degree_computational_threshold.md) | 15 | 2 | 3 |
| [高阶累积量张量估计与U统计量](proposals/other_higher_order_cumulant_tensor.md) | 8 | 2 | 2 |

---

## 跨战线反复出现的主题

每条战线生成提案时**看不到其他战线**，所以同一个想法从多条战线独立冒出来时，这个「反复」本身就是证据——跟提案内部要求「≥2 篇独立论文点名」是同一个标准。这里只报事实，不替你合并：想法相近但 estimand 常常不同，值得你自己对一遍。

**低度多项式 / 计算-统计 gap** — 6 条提案，横跨 4 条战线

- [非参数回归的极小极大率刻画](proposals/nonparam_semipara_minimax_rate_nonparametric_regression.md) · Statistical-Computational Tradeoffs in Low-Rank Matrix/Tensor Estimation: A Low-Degree Polynomial Approach
- [高维稀疏信号检测与相变](proposals/hypothesis_testing_high_dimensional_sparse_detection.md) · Low-Degree Polynomial Barriers for Sparse Signal Detection in the Curie-Weiss Ising Model
- [张量分解与黎曼优化](proposals/stat_computing_tensor_decomposition_optimization.md) · Phase Transitions in Tensor Estimation: How the Order \(K\) Shapes the Statistical–Computational Gap
- [低度多项式与计算-统计阈值](proposals/hypothesis_testing_low_degree_computational_threshold.md) · Low-Degree Hardness Under Non-Gaussian Designs: The Case of Shuffled Linear Regression
- [低度多项式与计算-统计阈值](proposals/hypothesis_testing_low_degree_computational_threshold.md) · Beyond Low-Degree Polynomials: Can Sum-of-Squares Break the \(\sqrt{L}\) Barrier in Multi-Layer SBM?
- [低度多项式与计算-统计阈值](proposals/hypothesis_testing_low_degree_computational_threshold.md) · Computational Barriers for Graphon Estimation in the Ultra-Sparse Regime: A Low-Degree Polynomial Approach

**近端因果的桥函数估计** — 5 条提案，横跨 4 条战线

- [双稳健估计与半参效率理论](proposals/causal_inference_doubly_robust_efficiency.md) · Computational-Statistical Tradeoffs in Bridge Function Estimation for Proximal Causal Inference
- [去偏机器学习与正交分数理论](proposals/efficiency_dml_debiased_machine_learning_orthogonal.md) · High-Dimensional Bridge Function Estimation for Proximal Causal Inference via Regularized Spectral Methods
- [近端因果推断/负对照变量](proposals/causal_inference_proximal_causal_inference.md) · Higher-Order Influence Functions for Proximal Causal Inference: Relaxing the \(n^{-1/4}\) Rate Condition
- [近端因果推断/负对照变量](proposals/causal_inference_proximal_causal_inference.md) · Diagnosing Bridge Function Misspecification in Proximal Causal Inference: A Specification Test
- [条件独立性检验与因果推断](proposals/hypothesis_testing_conditional_independence_testing.md) · Higher-Order Debiased Estimation of Bridge Functions in Proximal Causal Inference

**HOIF 放松 n^{-1/4} 速率条件** — 5 条提案，横跨 4 条战线

- [去偏机器学习与正交分数理论](proposals/efficiency_dml_debiased_machine_learning_orthogonal.md) · Higher-Order Influence Functions for Robust Debiased Machine Learning under Slow Nuisance Convergence
- [近端因果推断/负对照变量](proposals/causal_inference_proximal_causal_inference.md) · Higher-Order Influence Functions for Proximal Causal Inference: Relaxing the \(n^{-1/4}\) Rate Condition
- [半参数效率与影响函数](proposals/nonparam_semipara_semiparametric_efficiency_influence_function.md) · Higher-Order Influence Functions for Doubly Robust Estimation under Slow Nuisance Convergence
- [条件独立性检验与因果推断](proposals/hypothesis_testing_conditional_independence_testing.md) · Higher-Order Influence Function Correction for Riesz Representer Estimation Under Slow Nuisance Convergence
- [条件独立性检验与因果推断](proposals/hypothesis_testing_conditional_independence_testing.md) · Higher-Order Debiased Estimation of Bridge Functions in Proximal Causal Inference

**退化核 U 统计量的极限分布** — 2 条提案，横跨 2 条战线

- [U统计量与重抽样推断](proposals/hypothesis_testing_u_statistic_bootstrap_inference.md) · Degenerate U-Statistic Bootstrap: A Unified Algorithm and Higher-Order Theory
- [高阶影响函数与高阶去偏估计](proposals/efficiency_dml_higher_order_influence_functions.md) · Treewidth-Accelerated Computation and Inference for Degenerate Higher-Order U-Statistics


---

## [U统计量与重抽样推断](proposals/hypothesis_testing_u_statistic_bootstrap_inference.md)

基于U统计量（含V统计量、退化核）的高维假设检验，结合bootstrap、Edgeworth展开、高斯逼近实现渐近有效推断。

*证据 140 篇 · 含收藏 23 篇 · 提案 2 条*

- Degenerate U-Statistic Bootstrap: A Unified Algorithm and Higher-Order Theory
- Higher-Order Coverage Accuracy for U-Statistics via Studentized Cheap Bootstrap

## [非参数回归的极小极大率刻画](proposals/nonparam_semipara_minimax_rate_nonparametric_regression.md)

在随机设计、流形、星形约束等不同函数类下，刻画非参数回归/估计的极小极大收敛率，使用度量熵、Fano不等式、Le Cam方法等工具。

*证据 98 篇 · 含收藏 22 篇 · 提案 2 条*

- High-Dimensional Minimax Rates for Nonparametric Causal Functionals under Smoothness Constraints
- Statistical-Computational Tradeoffs in Low-Rank Matrix/Tensor Estimation: A Low-Degree Polynomial Approach

## [双稳健估计与半参效率理论](proposals/causal_inference_doubly_robust_efficiency.md)

发展双稳健（doubly robust）估计量及其影响函数（influence function），推导半参数效率界（semiparametric efficiency bound），并应用于ATE、CATE、分位数效应、剂量反应函数等因果参数的推断。

*证据 124 篇 · 含收藏 18 篇 · 提案 2 条*

- High-Dimensional Doubly Robust Variance Estimation: When Nuisance Functions Are Estimated via Machine Learning
- Computational-Statistical Tradeoffs in Bridge Function Estimation for Proximal Causal Inference

## [去偏机器学习与正交分数理论](proposals/efficiency_dml_debiased_machine_learning_orthogonal.md)

基于 Neyman 正交分数和 Riesz 表示子的去偏机器学习框架，包括交叉拟合、有限样本推断、自动去偏（AutoDML）以及在高维/非参数设定下的效率理论。

*证据 140 篇 · 含收藏 15 篇 · 提案 3 条*

- Semiparametric Efficiency Bounds for Proximal Dose-Response Functions and Distal Causal Excursion Effects
- Higher-Order Influence Functions for Robust Debiased Machine Learning under Slow Nuisance Convergence
- High-Dimensional Bridge Function Estimation for Proximal Causal Inference via Regularized Spectral Methods

## [近端因果推断/负对照变量](proposals/causal_inference_proximal_causal_inference.md)

利用负对照暴露和负对照结果（negative control variables）作为代理变量，在存在未测量混杂时识别和估计因果效应（如直接效应、路径效应、剂量反应函数），核心数学对象为桥函数（bridge function）和影响函数。

*证据 107 篇 · 含收藏 15 篇 · 提案 3 条*

- Longitudinal Proximal Mediation with Time-Varying Treatments and Mediators: Identification and Efficient Estimation
- Higher-Order Influence Functions for Proximal Causal Inference: Relaxing the \(n^{-1/4}\) Rate Condition
- Diagnosing Bridge Function Misspecification in Proximal Causal Inference: A Specification Test

## [高阶影响函数与高阶去偏估计](proposals/efficiency_dml_higher_order_influence_functions.md)

研究高阶影响函数（二阶及以上）在非参数/半参数模型中的构造、稳定化估计及其对 minimax 效率的改进，涉及 U-过程、Gram 矩阵逆、谱分析等工具。

*证据 59 篇 · 含收藏 15 篇 · 提案 2 条*

- Treewidth-Accelerated Computation and Inference for Degenerate Higher-Order U-Statistics
- Stabilized Higher-Order Influence Functions via Regularized Gram Matrix Inversion: A Spectral Analysis

## [共享奇异子空间与公共子空间的最优估计与推断](proposals/high_dim_rmt_subspace_estimation_inference.md)

针对多矩阵共享奇异子空间或公共子空间，研究minimax最优估计（如Stack-SVD、投影梯度下降）、sinΘ距离收敛率、自适应置信区间及渐近正态性，涉及计算-统计最优性权衡。

*证据 98 篇 · 含收藏 13 篇 · 提案 2 条 · ⚠️ 单点证据 1 条*

- Optimal Estimation of Shared Singular Subspaces under Heteroskedastic and Correlated Noise
- Shared Subspace Estimation without Spectral Gap: Minimax Rates under Continuous Singular Value Decay

## [未测量混杂的敏感性分析](proposals/causal_inference_sensitivity_analysis_unmeasured_confounding.md)

通过参数化偏离无混杂假设（如边际敏感性模型、校准敏感性分析、混淆函数），推导ATE或分位数效应的部分识别界（sharp bounds），并构建置信区间。

*证据 133 篇 · 含收藏 11 篇 · 提案 3 条*

- Higher-Order Influence Functions for Local Sensitivity Analysis: Sharpening First-Order Approximations Under Unmeasured Confounding
- Nested Sensitivity Envelopes for Longitudinal Causal Effects with Time-Varying Treatments
- Confidence Intervals for Sensitivity Intervals: Inference on the Entire Identification Region Under Distributional Uncertainty

## [结构无关模型下的半参数效率与去偏](proposals/efficiency_dml_structure_agnostic_semiparametric.md)

在不对 nuisance 函数施加具体结构（如光滑性、稀疏性）的设定下，推导半参数泛函的 minimax 下界、构造自适应去偏估计量并研究其渐近性质。

*证据 53 篇 · 含收藏 11 篇 · 提案 3 条*

- Structure-Agnostic Minimax Rates Under Asymmetric Nuisance Errors: Closing the Gap Between Upper and Lower Bounds
- Debiased Estimation of Nonlinear Semiparametric Functionals Under Structure-Agnostic Models: Beyond Monotone Bias Class
- Adaptive Hyperparameter Selection for Debiased Estimators in Structure-Agnostic Models: From Oracle to Data-Driven

## [半参数效率与影响函数](proposals/nonparam_semipara_semiparametric_efficiency_influence_function.md)

推导半参数模型的效率界、有效影响函数、有效得分函数，并构造渐近正态/半参数BvM的估计量，涉及部分线性模型、分位数回归、逆问题等。

*证据 66 篇 · 含收藏 10 篇 · 提案 2 条*

- Higher-Order Influence Functions for Doubly Robust Estimation under Slow Nuisance Convergence
- Interventional Mediation Effects under Treatment-Induced Confounding: Identification and Semiparametric Estimation

## [高维稀疏信号检测与相变](proposals/hypothesis_testing_high_dimensional_sparse_detection.md)

研究高维稀疏信号（如子矩阵、图模型、Ising模型）的极小极大检测边界与计算-统计相变，常用Higher Criticism、似然比、二阶矩方法。

*证据 45 篇 · 含收藏 9 篇 · 提案 2 条*

- Low-Degree Polynomial Barriers for Sparse Signal Detection in the Curie-Weiss Ising Model
- Adaptive Sparse Signal Detection Under Unknown Dependence in the Ising Model on a Cycle Graph

## [非参数图模型与扩散模型选择](proposals/nonparam_semipara_nonparametric_graphical_model_diffusion.md)

利用扩散模型、得分匹配等工具进行非参数无向图模型选择，研究模型选择相合性、高维非参数估计。

*证据 43 篇 · 含收藏 8 篇 · 提案 2 条*

- Sparse-Graph-Adaptive Nonparametric Graphical Model Selection via Diffusion Models
- High-Dimensional Nonparametric Graph Recovery Using k-NN Azadkia-Chatterjee Correlations and Diffusion-Based Hessian Estimation

## [条件独立性检验与因果推断](proposals/hypothesis_testing_conditional_independence_testing.md)

检验条件独立性或处理效应异质性，利用条件随机化检验、双稳健得分、影响函数、交叉拟合等方法。

*证据 42 篇 · 含收藏 6 篇 · 提案 2 条*

- Higher-Order Influence Function Correction for Riesz Representer Estimation Under Slow Nuisance Convergence
- Higher-Order Debiased Estimation of Bridge Functions in Proximal Causal Inference

## [张量分解与黎曼优化](proposals/stat_computing_tensor_decomposition_optimization.md)

研究张量分解（CP/Tucker）中黎曼梯度下降、双投影迭代等优化方法的计算与统计性质，包括统计-计算权衡、过参数化、相位转变。

*证据 39 篇 · 含收藏 6 篇 · 提案 2 条*

- Phase Transitions in Tensor Estimation: How the Order \(K\) Shapes the Statistical–Computational Gap
- Global Convergence of Riemannian Gradient Descent for Tensor Decomposition: The Role of Spectral Initialization

## [低度多项式与计算-统计阈值](proposals/hypothesis_testing_low_degree_computational_threshold.md)

利用低度多项式方法刻画假设检验的计算-统计相变，适用于尖峰Wigner模型、混洗回归等，建立通用下界。

*证据 15 篇 · 含收藏 2 篇 · 提案 3 条*

- Low-Degree Hardness Under Non-Gaussian Designs: The Case of Shuffled Linear Regression
- Beyond Low-Degree Polynomials: Can Sum-of-Squares Break the \(\sqrt{L}\) Barrier in Multi-Layer SBM?
- Computational Barriers for Graphon Estimation in the Ultra-Sparse Regime: A Low-Degree Polynomial Approach

## [高阶累积量张量估计与U统计量](proposals/other_higher_order_cumulant_tensor.md)

带状累积量张量的最优估计、高阶U统计量的Bochner积分收缩估计、核退化与RKHS均值元，以及非高斯数据建模中的张量收缩复杂度

*证据 8 篇 · 含收藏 2 篇 · 提案 2 条*

- Minimax Optimal Estimation of High-Dimensional Cumulant Tensors Under Higher-Order Fluctuation Terms
- Adaptive Directional Shrinkage for High-Order U-Statistics with Bandable Cumulant Structure

---

## 旧版跨篇综合（存档）

本页此前是按 10 个粗 topic 做的跨篇综合，产物停在「反复出现的开放问题 / 张力 / 迁移空位」，没有到可上手的提案。14 个旧页面全部保留：[跨篇综合存档](synthesis/index.md)。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

