# 跨篇综合 · 数理统计 / 假设检验

**子方向**: 数理统计 / 假设检验  
**期刊范围**: core  
**聚合期刊论文数**: 11  
**生成日期**: 2026-06-02  

> 本页由跨篇综合自动生成：从近期期刊精读里归纳反复出现的开放问题、张力与迁移空位。**不打分、不排名**，每条点名来源论文 [k]，供你自己判断。

---

### 一、这个子方向的全景
这批论文共同追问的核心是：**在复杂结构（高维、非稀疏、相依、误设定、对抗污染）下，如何突破传统独立/稀疏/正确模型假设，构造具有理论保证（渐近分布、minimax率、大偏差界）且计算可行的检验与决策规则**。主流路线有三条：一是基于**Neyman正交/高阶影响函数（HOIF）+交叉拟合**的半参数去偏推断（[3][6][11]）；二是基于**局部熵/大偏差/低次多项式**刻画信息与计算的极限相变（[1][2][4]）；三是利用**矩约束/秩条件/群代数结构**重构检验统计量的代数与几何形状（[5][9][10]）。整体停滞点在于：当结构复杂度超出传统假设时，正交框架的偏差控制失效、计算相变间隙缺乏可达算法、高阶矩/张量检验的计算复杂度爆炸，且三者之间尚未形成统一理论。

### 二、反复出现的开放问题
① **高阶矩/张量检验的计算复杂度爆炸与优化空位**：[5][6][9][11]均指出，当检验统计量涉及高阶U-统计量、子行列式或张量外积时，直接计算不可行。需证/估：如何通过incomplete U-统计量设计、treewidth优化或tensor contraction（einsum）寻找最优收缩顺序，以将计算复杂度从指数级降至多项式级甚至线性级。卡在：高阶矩检验的代数结构（如累积量张量秩）与计算图最优收缩顺序的映射关系尚未建立。
② **Neyman正交/双重稳健对nuisance估计误差容忍度的极限与高阶推广**：[3][6][11]均指出，一阶正交/双重稳健要求nuisance误差乘积或收敛速率达到$O(n^{-1/2})$，在复杂非参数/高维设定下过强。需证/估：引入HOIF（高阶影响函数）能否将容忍度从$n^{-1/2}$提升至$n^{-\alpha}(\alpha<1/2)$，以及高阶正交CI检验统计量的具体形式与偏差拆解。卡在：HOIF的K-th order正交性与条件分布乘积/拟似然交叉项的代数结合缺乏显式构造，且方差控制框架未推广至高阶。
③ **相依/非稀疏/误设定结构下检验的minimax最优性与相变刻画**：[1][2][4][7][11]均指出，传统检验在相关假设、非稀疏差分或方差误设定下失效。需估/算：在相关compound decision（[1]）、星形约束污染（[2]）、非稀疏变点（[7]）、超高维误设定GLM（[11]）下的minimax检测率下界，以及信息-计算间隙的精确位置。卡在：局部熵/大偏差率函数与minimax下界的Fano论证在相依/非稀疏/误设定下的统一隐式方程尚未解出。
④ **复合零假设/弱重叠性下的尺寸控制与偏差爆炸**：[3][5][10]均指出，当零假设复合（如MCAR兼容性、复合CI）或存在弱重叠性（倾向性得分趋0/1）时，nuisance估计的二阶偏差不可忽略，导致size偏离。需证/算：如何通过截断/正则化/样本分割在非渐近层面控制误差，且不损失过多功效。卡在：正交得分函数在边界/奇异点处的非渐近展开缺乏精确的Hoeffding/Edgeworth控制。

### 三、张力 / 矛盾
① **FDR框架下separable rule的最优性分歧**：[1]指出在真实FDR约束下separable rule（如BH）渐近严格次优，必须用compound rule；而已有文献（Storey 2002等）在mFDR框架下证明separable rule可达最优。两者对同一权衡问题的最优决策机制刻画矛盾，调和需证真实FDP的高概率控制与mFDR期望控制的渐近等价/退化条件。
② **样本分裂的必要性分歧**：[3]宣称通过更强光滑性假设与Neyman正交可完全避免sample splitting获得渐近分布；而[6][11]及DML框架依赖cross-fitting控制nuisance偏差。两者在处理nuisance偏差的技术路线上矛盾，调和需证正交构造在何种光滑度/误差条件下可免除样本分裂，以及交叉拟合在弱光滑下的不可替代性。
③ **置换检验群大小的势与有效性分歧**：[10]证明子群置换（如符号翻转）因保留信号方向一致性而势远优于全置换，且计算更省；传统信条及部分文献认为全置换提供最精确的null分布。调和需在极值理论与群代数结构下，量化“信号稀释”与“null分布精确度”之间的权衡。
④ **线性后悔与非线性后悔下随机化规则的完备性分歧**：[8]证明对严格凸后悔（如均方后悔），单点规则不再本质完备，推翻Manski (2004)在线性后悔下的经典结论。调和需证后悔函数的凸性如何改变决策类的拓扑与风险极值，并给出有限随机化类成为本质完备类的充要条件。

### 四、迁移空位（接研究者武器库）
① **高阶U-统计量/tensor contraction优化高阶矩检验计算**：空位在[5]的SDP对偶矩阵运算、[6]的GNN乘积误差U-统计量、[9]的子行列式U-统计量。武器：高阶U-统计量的einsum/tensor contraction/treewidth计算。第一步：将[9]的子行列式核函数表示为张量网络，计算其treewidth，寻找最优einsum收缩顺序以替代显式高阶矩遍历；对[5]的缺失模式超图，将SDP对偶最优性条件转化为矩阵乘法序列的contraction cost问题。
② **HOIF提升半参数检验的nuisance容忍度**：空位在[3]的CATE异质性检验（容忍度$n^{-1/4}$）与[6]的CI检验（容忍度乘积$o(n^{-1/2})$）。武器：高阶影响函数（HOIF）与minimax下界。第一步：为[3]的influence function得分检验构造二阶正交HOIF，将nuisance误差容忍度从$n^{-1/4}$放松至$n^{-1/6}$，并用einsum表示二阶HOIF核的方差控制；对[6]，推导K阶GNN误差乘积条件$\varepsilon_X \varepsilon_Y = O(n^{-\alpha})$下的HOIF-CI检验统计量，并用minimax下界证明$\alpha$的紧性。
③ **minimax下界刻画非稀疏/相依/误设定的检测极限**：空位在[1]的相依compound oracle间隙、[2]的星形约束污染率、[7]的非稀疏变点检测率、[11]的误设定GLM检验功效。武器：minimax下界与高维渐近。第一步：对[7]的LCS检测量，将信号强度参数化为$\|\Sigma^{1/2}\delta\|_2$，利用Fano引理+局部pack构造推导非稀疏差分下的minimax检测率下界，并与LCS的扫描率比较证匹配；对[1]，将相关结构引入大偏差率函数，推导从compound oracle到MLE-插件曲线的间隙渐近界。
④ **大偏差/局部熵统一计算-统计相变**：空位在[4]的low-degree检测间隙与[2]的局部熵隐式方程。武器：高维渐近与大偏差理论。第一步：将[2]的局部熵隐式方程$N\eta^2/\sigma^2 = \log M_K^{loc}(\eta,c)$推广至[4]的CSBM设定，计算相关子图计数统计量的局部pack数，试图用局部熵统一解释low-degree barrier与KS阈值的计算相变。

---

### 本页聚合的论文

- [1] Large-scale multiple testing: Fundamental limits of false discovery rate control and compound oracle — Annals of Statistics (2026-05-26)
- [2] Information theoretic limits of robust sub-Gaussian mean estimation under star-shaped constraints — Annals of Statistics (2026-05-26)
- [3] Nonparametric tests of treatment effect homogeneity for policy-makers — Journal of the American Statistical Association (2026-05-26)
- [4] A computational transition for detecting correlated stochastic block models by low-degree polynomials — Annals of Statistics (2026-05-26)
- [5] Tests of missing completely at random based on sample covariance matrices — Annals of Statistics (2026-05-26)
- [6] Doubly robust conditional independence testing with generative neural networks — Journal of the Royal Statistical Society Series B (2026-05-26)
- [7] Detection and inference of changes in high-dimensional linear regression with nonsparse structures — Journal of the Royal Statistical Society Series B (2026-05-26)
- [8] Treatment choice with nonlinear regret — Biometrika (2026-05-26)
- [9] Goodness-of-fit tests for linear non-Gaussian structural equation models — Biometrika (2026-05-26)
- [10] More power by using fewer permutations — Biometrika (2026-05-26)
- [11] Inference for possibly misspecified generalized linear models with nonpolynomial-dimensional nuisance parameters — Biometrika (2026-05-26)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

