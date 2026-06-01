# 跨篇综合 · 因果推断

**子方向**: 因果推断  
**期刊范围**: core  
**聚合期刊论文数**: 33  
**生成日期**: 2026-06-02  

> 本页由跨篇综合自动生成：从近期期刊精读里归纳反复出现的开放问题、张力与迁移空位。**不打分、不排名**，每条点名来源论文 [k]，供你自己判断。

---

### 一、这个子方向的全景
这批论文共同追问的核心是：**当因果推断的理想识别假设（如无未测量混杂、严格随机化、无干扰）被现实打破时，如何通过结构约束、辅助变量或设计技巧实现因果效应的（部分）识别与有效估计**。主流路线有三条：一是**半参数正交化与效率界**路线（[8,9,10,11,12,13,15,16,19,21,25,29]），通过EIF/DML/多重稳健容忍讨厌参数误设；二是**部分识别与敏感性分析**路线（[11,13,22,27,28,30,31,32]），放弃点识别转求非参数sharp界或校准未测量混杂强度；三是**复杂结构/高维设定下的识别与计算**路线（[1,2,4,5,9,17,20,24]），处理层级、潜变量、连续主分层或上下文特定因果图。整体停滞点在于：半参数路线的$n^{-1/4}$讨厌参数收敛条件在实践中极难满足，部分识别路线的界宽常随维度发散而退化为无信息，而复杂结构路线则普遍卡在计算可行性与非参数识别的矛盾上。

### 二、反复出现的开放问题

1. **讨厌参数慢速收敛（$<n^{-1/4}$）下的高阶偏差校正与效率恢复**
   - ①要证/估什么：当非参数/ML讨厌参数收敛慢于$n^{-1/4}$时，如何通过高阶影响函数（HOIF）或高阶U-统计量校正偏差，恢复$\sqrt{n}$-CAN或逼近半参数效率界。
   - ②点名：[1, 8, 9, 10, 12, 13, 15, 18, 23, 25, 29, 33]（共12篇独立点名）。
   - ③卡在哪：半参数一步估计/DR估计的余项为讨厌参数误差的乘积阶，慢收敛下该余项主导偏差；HOIF虽能降阶，但高阶U-统计量的计算复杂度与Donsker类约束成为瓶颈。

2. **非光滑泛函（界限、分位数、TV类）的半参数有效估计与局部可微性**
   - ①要证/估什么：对非光滑目标（如IV界限、主分层概率、CATE的TV类、绝对值函数），如何构造margin condition或光滑近似以恢复局部可微性，并推导其半参数有效界与minimax最优率。
   - ②点名：[6, 11, 13, 18, 23, 25, 32]（共7篇独立点名）。
   - ③卡在哪：非光滑泛函在边界点不可微导致EIF不存在或退化；现有光滑近似（如softmin/log-sum-exp）的偏差-方差权衡依赖难以验证的margin condition或光滑阶$r$的先验指定。

3. **连续/高维处理、多因子与纵向设定下的识别与计算瓶颈**
   - ①要证/估什么：将二元/单时间点因果推断扩展到连续处理、多因子($2^K$)非依从、纵向时变处理或连续主分层时，如何避免识别条件与计算复杂度的指数级发散。
   - ②点名：[3, 6, 7, 9, 10, 27, 31]（共7篇独立点名）。
   - ③卡在哪：连续/多值处理使潜在结果空间指数膨胀，部分识别界退化为平凡区间[0,1]（[27,31]）；连续主分层需双重积分与反卷积，计算呈NP-hard或需无限维LP（[9,31]）。

4. **未测量混杂的校准、代理变量与部分识别的统一框架**
   - ①要证/估什么：如何将敏感性分析的抽象参数（如$\Gamma$）校准为已测量混杂的倍数以提升可解释性，或通过负控制/Proximal变量实现未测量混杂的非参数识别，并构造对应的多重稳健估计量。
   - ②点名：[2, 12, 13, 19, 29]（共5篇独立点名）。
   - ③卡在哪：校准参数$\Gamma$的选择仍需主观判断且界宽正比于$\Gamma$易失效（[13]）；Proximal/负控制的桥函数求解存在多解性与非参数收敛率慢的困难（[12,29]）；非高斯LiNGAM与Proximal在识别条件上存在范式张力（[2]）。

5. **因果发现与因果识别的桥接及后选择推断**
   - ①要证/估什么：在因果图未知或部分已知时，如何从数据自适应选择调整集（如IGE）或因果发现（如PC算法），并对其选择不确定性进行后选择推断以保证对真实因果参数的覆盖。
   - ②点名：[14, 20]（共2篇独立点名）。
   - ③卡在哪：确定性选择规则导致选后泛函与真实参数脱节（[14]）；交互式图扩展（IGE）依赖用户每步正确提供初级调整集的强认知假设，且未处理潜变量（[20]）。

### 三、张力 / 矛盾

1. **匹配估计量的半参数效率之争**：[15]证明发散匹配数$M$下的倾向得分匹配（PSM）渐近方差可达到Hahn(1998)半参数效率界；而[26]与经典文献Abadie & Imbens(2008)认为固定$M$下PSM因不可忽略偏置不仅达不到效率界且naive bootstrap不一致。调和这一张力需严格证明$M$发散速率在何种光滑性条件下能完全消除偏置并恢复bootstrap一致性，填补$M$从固定到发散的相变空白。

2. **非高斯性 vs 代理变量的未测量混杂识别范式分歧**：[2]依赖非高斯性（ICA）在非线性潜变量混淆下实现参数generic识别，明确指出当误差为高斯时图判据完全失效；而[12,29]的Proximal/负控制框架依赖代理变量的条件独立性而非分布的非高斯性。两者在“打破未测量混杂不可识别”的核心杠杆上存在根本分歧，桥接需研究非高斯Proximal框架能否同时利用两种杠杆放宽识别条件。

3. **分布泛化中强不变性与因果图可识别性的矛盾**：[19]证明在隐藏混杂下，只要偏移仅改变$P(Z,H)$，Boosted Control Function即可满足强不变性并实现worst-case最优泛化，不要求因果图完全可识别；而[20,24]的因果发现路线要求图结构可识别（或等价类可学习）才能保证调整集的soundness。两者在“是否需要图可识别性才能做因果推断/泛化”上存在假设强度的张力。

4. **缺失数据下协变量调整的等价性崩溃**：[33]发现在结果与协变量均有缺失时，回归调整与倾向得分加权的渐近等价性崩溃——回归调整仅在模型线性或MCAR下提升效率，否则可能增方差；而完全观测下两者等价（Lin 2013）。这一矛盾揭示了缺失机制如何破坏正交投影的对称性，需在MAR下重新定义半参数效率界。

### 四、迁移空位（接研究者武器库）

1. **HOIF高阶偏差校正的einsum/tensor contraction计算落地**
   - ①空位：[1,9,10,12,25,31]均提出需用HOIF突破$n^{-1/4}$讨厌参数收敛瓶颈，但均未给出高阶U-统计量的可计算实现，[31]甚至指出连续暴露+连续结局的精确推断是NP-hard。
   - ②武器：高阶U-统计量的einsum/tensor contraction计算与treewidth复杂度分析。
   - ③第一步：将[9]中连续主分层DR估计量的双重积分核函数展开为张量收缩模式，计算其treewidth；若treewidth有界，则用einsum实现二阶HOIF的$O(n^2)$计算；若treewidth发散，则证明其与[31]的NP-hard壁垒等价。

2. **非光滑因果界限的minimax下界与局部可微性验证**
   - ①空位：[11,13,18,25]对IV界限、校准敏感性ATE界、TV类CATE给出了半参数效率上界，但均未证明该速率的minimax最优性，且[11]承认margin condition不可检验。
   - ②武器：Minimax下界构造与高维渐近。
   - ③第一步：对[11]的协变量辅助IV界限，在margin condition下构造两个难以区分的潜在结果分布（使界限点分别在边界内侧与外侧），用Le Cam方法计算Hellinger距离缩放，推导$n^{-1/2}$下界；若margin condition轻微违反，用Assouad方法计算下界退化至$n^{-2/3}$，与[11]的理论预测对齐。

3. **层级/潜变量因果图的代数识别与矩阵补全**
   - ①空位：[1,2,17]分别处理层级图、非线性潜变量混淆与高斯预边缘化图的参数识别，[1]未证层级do-calculus完备性，[2]未给出端到端参数提取算法。
   - ②武器：高阶U-统计量/张量收缩中的代数约束与treewidth。
   - ③第一步：将[1]的层级图压缩引理（inner plate边际化）转化为张量网络中的迹收缩操作，利用图分离条件写出识别方程的秩条件；用treewidth刻画[2]中非线性混淆等价线性化后的DAG子图拓扑复杂度，将图判据验证算法映射为矩阵补全的凸规划，给出多项式时间端到端提取步骤。

4. **匹配与置换检验的U-统计量渐近与计算可行性**
   - ①空位：[3,7,22,26,30,31]在多处理水平、干扰或连续暴露下推导有限样本/渐近界，但[31]证明一般匹配下精确推断NP-hard，[22]的SDP计算$O(N^3)$不可扩展。
   - ②武器：高阶U-统计量计算与minimax理论。
   - ③第一步：将[3]的二次置换统计量与[7]的ITE分布尾部概率求和重写为高阶U-统计量，用einsum评估其contraction树宽；对[31]的连续暴露NP-hard问题，构造基于二阶U-统计量的渐近近似检验，用minimax下界证明该近似在弱依赖匹配下的局部最优性，绕开MIP精确求解。

---

### 本页聚合的论文

- [1] Hierarchical Causal Models — JMLR (2026-05-26)
- [2] Parameter identification in linear non-Gaussian causal models under general confounding — Annals of Statistics (2026-05-26)
- [3] Berry–Esseen bounds for design-based causal inference with possibly diverging treatment levels and varying group sizes — Annals of Statistics (2026-05-26)
- [4] Counterfactual inference in sequential experiments — Annals of Statistics (2026-05-26)
- [5] Individualized Dynamic Mediation Analysis Using Latent Factor Models — Journal of the American Statistical Association (2026-05-26)
- [6] Doubly Robust Pointwise Confidence Intervals for a Monotonic Continuous Treatment Effect Curve — Journal of the American Statistical Association (2026-05-26)
- [7] Enhanced Inference for Distributions and Quantiles of Individual Treatment Effects in Various Experiments — Journal of the American Statistical Association (2026-05-26)
- [8] An Online Meta-Level Adaptive Design Framework with Targeted Learning Inference: Applications to Evaluating and Utilizing Surrogate Outcomes in Adaptive Designs — Journal of the American Statistical Association (2026-05-26)
- [9] Principal stratification with continuous post-treatment variables: nonparametric identification and semiparametric estimation — Journal of the Royal Statistical Society Series B (2026-05-26)
- [10] Identification and multiply robust estimation in causal mediation analysis across principal strata — Journal of the Royal Statistical Society Series B (2026-05-26)
- [11] Covariate-assisted bounds on causal effects with instrumental variables — Journal of the Royal Statistical Society Series B (2026-05-26)
- [12] Assumption-lean post-integrated inference with surrogate-control outcomes — Biometrika (2026-05-26)
- [13] Calibrated sensitivity models — Biometrika (2026-05-26)
- [14] Post-selection inference for causal effects after causal discovery — Biometrika (2026-05-26)
- [15] On propensity score matching with a diverging number of matches — Biometrika (2026-05-26)
- [16] Flexible Functional Treatment Effect Estimation — JMLR (2026-05-26)
- [17] Neural Network Parameter-optimization of Gaussian Pre-marginalized Directed Acyclic Graphs — JMLR (2026-05-26)
- [18] A causal fused lasso for interpretable heterogeneous treatment effects estimation — JMLR (2026-05-26)
- [19] Boosted Control Functions: Distribution Generalization and Invariance in Confounded Models — JMLR (2026-05-26)
- [20] Confounder selection via iterative graph expansion — Annals of Statistics (2026-05-26)
- [21] Facilitating Heterogeneous Effect Estimation via Statistically Efficient Categorical Modifiers — Journal of the American Statistical Association (2026-05-26)
- [22] Optimized Variance Estimation under Interference and Complex Experimental Designs — Journal of the American Statistical Association (2026-05-26)
- [23] Successive classification learning for estimating quantile optimal treatment regimes — Journal of the American Statistical Association (2026-05-26)
- [24] Representation of context-specific causal models with observational and interventional data — Journal of the Royal Statistical Society Series B (2026-05-26)
- [25] Semiparametric localized principal stratification analysis with continuous strata — Journal of the Royal Statistical Society Series B (2026-05-26)
- [26] On the consistency of bootstrap for matching estimators — Biometrika (2026-05-26)
- [27] Bounds on causal effects in $ 2^{K} $ factorial experiments with noncompliance — Biometrika (2026-05-26)
- [28] Planning for gold: Hypothesis screening with split samples for valid powerful testing in matched observational studies — Biometrika (2026-05-26)
- [29] A semiparametric instrumented difference-in-differences approach to policy learning — Biometrika (2026-05-26)
- [30] Sensitivity analysis for observational studies with flexible matched designs — Biometrika (2026-05-26)
- [31] Sensitivity analysis for matched observational studies with continuous exposures and binary outcomes — Biometrika (2026-05-26)
- [32] Sharp symbolic nonparametric bounds for measures of benefit in observational and imperfect randomized studies with ordinal outcomes — Biometrika (2026-05-26)
- [33] Covariate adjustment in randomized experiments with missing outcomes and covariates — Biometrika (2026-05-26)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

