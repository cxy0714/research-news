# 跨篇综合 · 非参数 / 半参数

**子方向**: 非参数 / 半参数  
**期刊范围**: core  
**聚合期刊论文数**: 7  
**生成日期**: 2026-06-02  

> 本页由跨篇综合自动生成：从近期期刊精读里归纳反复出现的开放问题、张力与迁移空位。**不打分、不排名**，每条点名来源论文 [k]，供你自己判断。

---

### 一、这个子方向的全景
这批论文共同追问：在高维、逆问题或流式等复杂设定下，非参数/半参数泛函（如导数、条件期望特征、分布函数值、逆密度加权期望）能否实现根号n速率的可靠推断（置信区间/带）？主流路线有三条：①去偏/投影校正（[1]乘性权重去偏、[5]先验+投影逆映射、[6]Voronoi分段多项式无调参拟合）；②极小极大下界与风险刻画（[2]凸对偶统一下界、[4]特征值衰减揭示SIR困境、[6]Fano下界定光滑性门槛）；③强近似与在线/bootstrap推断（[3]RKHS-SGD的sup-norm高斯逼近、[7]近似鞅的三阶Gaussian mixture耦合）。整体停在：泛函推断的“根号n-CAN”上界已有多种构造，但下界紧性、半参效率界可达性、以及高阶偏差校正（HOIF）对有限样本推断的实质性改进，均处于刚被提出但未闭环的阶段。

### 二、反复出现的开放问题
① **半参效率界是否可达？** 需证/估：现有根号n一致估计量（如DLL、Voronoi匹配）的渐近方差是否达到半参效率下界。点名：[1]（明确future work要推导DLL效率界并据此改进）、[6]（明确future work要推导逆密度加权期望的效率界并比较Voronoi估计量方差）。卡在：去偏/无调参构造虽消除了高维nuisance偏差，但方差结构是否最优缺乏理论闭环。
② **高阶偏差校正（HOIF）能否实质性改善弱信号/有限样本推断？** 需证/算：用k阶U-统计量或三阶矩匹配替代一阶/二阶近似，能否在弱特征值(λ_d极小)或非参数局部多项式推断中收紧置信区间/降低风险对弱信号的依赖。点名：[4]（提出用k阶U-统计量估计Cov[E(X|Y)]以降低对λ_d依赖）、[7]（提出三阶耦合与HOIF结合改进debiased ML分布近似）、[1]（迁移线索指出二阶导数推断需双核加权去偏接高阶U-统计量理论）。卡在：高阶项的degeneracy处理与计算复杂度（O(m^2)协方差）缺乏系统工具。
③ **多点/高维/同时推断的可行性及协方差结构计算。** 需估/算：从单点x_0边际推断扩展到多点联合置信带或高维可加泛函时，如何控制FWER/FDR及计算估计量协方差。点名：[1]（开放问题：多重推断控制FWER/FDR；future work：平均导数泛函需算多网格点协方差）、[5]（future work：多点联合推断推导协方差结构）、[3]（开放问题：高维下sup-norm bootstrap是否一致）。卡在：多点泛函的协方差计算面临高阶U-统计量或非独立经验过程的组合爆炸。
④ **minimax下界的紧性（匹配上界）缺失。** 需证：现有下界构造（SIR风险、逆密度加权期望光滑性门槛、Wicksell逆问题速率）是否存在匹配的可达估计量。点名：[4]（承认仅证下界未提供上界）、[6]（下界假设类与上界一致但未证完全无光滑性密度下的紧性）、[5]（future work要补全minimax速率下界证明）。卡在：下界构造依赖特定先验/假设类（如GP先验、紧支集），上界估计量难以在同等约束下达到同等速率。

### 三、张力 / 矛盾
① **对协变量/ nuisance分布光滑性要求的根本分歧。** [6]宣称对协变量密度“无需任何光滑性”（仅需inf f>0）即可达根号n，而[1]要求nuisance协变量能被稀疏非线性函数逼近（强非线性依赖致权重不稳定），[4]与[5]则依赖GP先验或Hölder指数(γ>1/2)控制偏差。这反映了“免光滑性调参”与“用光滑性控制高维偏差”两条路线在假设上的直接冲突，调和点可能在：密度无光滑性时，nuisance函数的光滑性或稀疏性是否足以保根号n。
② **SIR失效原因的模型设定冲突。** [4]将链接函数f视为GP先验导出特征值指数衰减(λ_d~e^{-θd})，解释SIR失效；而经典SIR理论（Li 1991）依赖线性条件均值(LCE)无特征值衰减分析。GP先验与LCE在本质上是冲突的假设，这意味着SIR困境的数学解释目前绑定在贝叶斯先验上，频率学派LCE设定下是否必然存在同等衰减尚未定论。
③ **分布近似阶数的收益与条件矛盾。** [7]宣称三阶Gaussian mixture耦合比二阶获得更紧近似（误差降至n^{-3/2}量级），但承认这依赖特定三阶矩结构匹配，且DML的cross-fitting破坏鞅结构致三阶无法直接应用；而[3]的SGD推断仅用二阶展开。三阶改进的“必要条件”与“实际可用设定（如DML）”之间存在错配，构成方法推广的张力。

### 四、迁移空位（接研究者武器库）
① **空位：多点泛函/平均导数推断的协方差计算爆炸。** [1]要算多网格点DLL估计量的协方差以构造平均导数置信区间，[5]要算多点IIP联合后验协方差。武器：高阶U-统计量计算（einsum/tensor contraction优化Hoeffding分解）。第一步：将[1]中多网格点DLL估计量写成二阶U-统计量形式，用einsum推导其treewidth，将协方差计算从O(m^2)降至线性。
② **空位：SIR及半参数估计中弱信号特征值(λ_d)依赖的高阶校正。** [4]提出用k阶U-统计量替代切片平均估计Cov[E(X|Y)]以校正高阶bias并降低对λ_d依赖，但未实施。武器：高阶U-统计量渐近理论（degeneracy处理）与半参数HOIF。第一步：在[4]的SIR设定中，将条件协方差估计量构造为三阶U-统计量，计算其degeneracy阶数与渐近方差对λ_d的依赖幂次，对比切片平均的一阶依赖。
③ **空位：非参数局部多项式/逆问题泛函的minimax下界刻画。** [5]需补Wicksell问题minimax速率下界，[6]需验证光滑性门槛下界在更广假设类的紧性。武器：minimax下界（Le Cam两点法/凸对偶/Fano）。第一步：用[2]的凸对偶框架（将两点下界对偶化为估计器风险上界），对[5]中Wicksell逆问题的分布函数泛函构造modulus of continuity，去掉Hölder假设直接证下界紧性。
④ **空位：DML/cross-fitting破坏鞅结构下的高阶分布近似。** [7]指出三阶耦合无法直接用于DML估计量（非鞅），[1]的去偏估计量也面临nuisance估计误差的非鞅残差。武器：高阶U-统计量理论（退化U-统计量的正交分解）与近似鞅耦合。第一步：将[1]的DLL估计量或典型DML估计量分解为精确鞅+高阶退化U-统计量残差，套用[7]的近似鞅三阶耦合框架，推导Gaussian mixture近似的误差界。

---

### 本页聚合的论文

- [1] Decorrelated Local Linear Estimator: Inference for Non-linear Effects in High-dimensional Additive Models — JMLR (2026-05-26)
- [2] Dualizing Le Cam’s method for functional estimation I: General theory — Annals of Statistics (2026-05-26)
- [3] Scalable inference for nonparametric stochastic approximation in reproducing kernel Hilbert spaces — Annals of Statistics (2026-05-26)
- [4] On the structural dimension of sliced inverse regression — Annals of Statistics (2026-05-26)
- [5] Semiparametric Bernstein–von Mises phenomenon via Isotonized Posterior in Wicksell’s problem — Annals of Statistics (2026-05-26)
- [6] Multivariate root-n-consistent smoothing parameter-free matching estimators and estimators of inverse density weighted expectations — Annals of Statistics (2026-05-26)
- [7] Yurinskii’s coupling for martingales — Annals of Statistics (2026-05-26)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

