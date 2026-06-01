# 跨篇综合 · 其他

**子方向**: 其他  
**期刊范围**: core  
**聚合期刊论文数**: 7  
**生成日期**: 2026-06-02  

> 本页由跨篇综合自动生成：从近期期刊精读里归纳反复出现的开放问题、张力与迁移空位。**不打分、不排名**，每条点名来源论文 [k]，供你自己判断。

---

### 一、这个子方向的全景
这批论文共同追问：在模型结构存在病态、高维、干扰或未知对称性等“非标准”阻碍时，如何保证因果参数或统计泛函的**识别与有效推断**。主流路线有三条：一是通过引入辅助变量（近端proxy [1]）或结构不变性（对称群 [7]）来降维或补全未观测信息；二是通过算法化/计算化手段（自动微分 [2]、repro samples [4]、平均场变分 [6]）绕过手工理论推导或渐近正态依赖；三是直面算子退化或弱识别的底层不可能性，刻画推断的理论边界（积分方程反问题 [3]、SPDE变点 [5]）。整体停留在：**识别与计算方案已提出，但有限样本/弱信号/算子退化下的推断有效性边界与效率最优化尚未闭环**。

### 二、反复出现的开放问题
1. **半参数估计量的效率界与minimax最优性缺失**
   - ① 要证/估：当前构造的CAN/√n-一致估计量是否达到半参数效率界？其收敛速度是否匹配minimax下界？
   - ② 提及：[1]（需推导ATE的半参数效率界并与当前渐近方差对比）、[4]（需证明repro samples置信区间长度渐近等价于半参数效率下界）、[5]（需推导扩散系数的半参效率下界并与δ^{3/2}速率比较）、[6]（需推导网络干扰下ATE的半参数效率界）。
   - ③ 卡在：估计量已具备一致性，但二阶偏差与方差展开的精细分析未完成，无法判断是否最优。

2. **高阶影响函数（HOIF）在弱识别/高维/干扰下的推断校正潜力未探明**
   - ① 要证/估：HOIF能否在算子近不可逆（弱识别）、高维混淆或网络干扰下，构造偏差校正或均匀有效的置信区间？
   - ② 提及：[2]（将Dimple扩展至HOIF的自动计算）、[3]（研究HOIF在算子退化下能否构造半参数置信区间，或证明其宽度发散下界）、[4]（用HOIF构造二阶校正的ATE置信区间）、[6]（用HOIF构造网络干扰下方差的多重稳健估计）。
   - ③ 卡在：HOIF的理论潜力被反复提及，但其计算复杂度与在病态条件下的理论有效性（是校正还是发散）均未落地。

3. **弱信号/算子退化下有限样本推断的失效与补救**
   - ① 要证/估：当初始模型遗漏变量、积分算子近不可逆或跳跃高度过小时，现有推断的覆盖保证是否崩溃？能否构造均匀有效或部分识别的置信集？
   - ② 提及：[3]（算子退化下均匀置信集的不可能下界与部分识别补救）、[4]（弱信号导致初始模型不一致，覆盖率失效且区间取并集扩大）。
   - ③ 卡在：点识别与渐近正态的理论前提在弱信号下不成立，转向部分识别或有限样本保证的路径尚未打通。

4. **复杂模型（非参数/网络/SPDE）中计算复杂度的精确刻画与优化**
   - ① 要算：算法（如二元变量置信集、mean-field迭代、对称化算子）的复杂度是否指数级？能否利用张量代数降至多项式级？
   - ② 提及：[3]（二元变量构造复杂度指数增长，需设计多项式时间算法）、[6]（mean-field迭代需用tensor contraction表述并分析treewidth代价）、[7]（对称化算子需用einsum高效实现并刻画复杂度）。
   - ③ 卡在：理论框架已搭好，但计算实现停留在概念或低维演示，未与高阶U-统计量的计算图优化结合。

5. **模型/结构误设的敏感性缺乏量化工具**
   - ① 要估：当completeness假设、高温条件或Lipschitz action不成立时，估计量偏差有多大？
   - ② 提及：[1]（缺乏对completeness假设与proxy误设的敏感性分析）、[6]（低温相变导致平均场失效，缺乏推断）。
   - ③ 卡在：核心识别条件多为不可检验的定性假设，一旦偏离缺乏定量的稳健性或部分识别兜底。

### 三、张力 / 矛盾
1. **点识别+渐近正态 vs. 弱识别+不可能性**：[1][4][6] 均在强假设（completeness、模型选择一致性、高温条件）下宣称了√n-一致与渐近正态推断的有效性；但 [3] 严格证明一旦算子接近不可逆（即这些强假设的边界处），Wald区间与score反转均匀失效，直径下界为常数。调和此张力需回答：在何种定量谱系下，强假设方法从“有效”平滑过渡到“不可能”？
2. **局部干扰 vs. 长程干扰的模型设定分歧**：[6] 明确采用chain graph允许长程干扰，与部分干扰假设（干扰局部性）和线性无干扰模型根本矛盾。这不仅是设定选择，更直接影响方差估计与置信区间的构造逻辑（局部化推断 vs. 全局平均场）。
3. **对称性降维的适用边界 vs. 稀疏性特例**：[7] 声称协变量稀疏性仅是平移对称性的退化特例，其对称化框架可统一处理；但该框架要求群族紧且满足Lipschitz action，这在稀疏性设定中自动成立，在一般非线性轨道中是极强限制。张力在于：[7] 的“统一”宣称实际上排除了大量非紧/非光滑的实用对称结构。

### 四、迁移空位（接研究者武器库）
1. **空位：HOIF在算子退化下的推断边界（[3]）**
   - 武器：minimax下界、高阶U-统计量计算
   - 动作：针对 [3] 的积分方程 $E[h|Z]=E[Y|Z]$，设定算子奇异值衰减速率，利用Le Cam变体构造两个接近不可逆的分布，推导HOIF校正后置信区间宽度的minimax下界，证明其是否仍发散。
2. **空位：近端因果中bridge function求解的逆问题与计算加速（[1]）**
   - 武器：nonparametric inverse problems、einsum/tensor contraction
   - 动作：将 [1] 的series estimator OLS求解桥函数改写为高阶张量收缩形式，利用treewidth优化交叉拟合中的重复计算；当W缺失时，将积分方程形式化为随机噪声下的非参数逆问题，推导正则化解的收敛率。
3. **空位：网络干扰下因果估计量的HOIF与方差解扰（[6]）**
   - 武器：高阶U-统计量计算、半参数效率界
   - 动作：为 [6] 的chain graph模型写出ATE的EIF，若 nuisance 估计导致二阶偏差，构造二阶U-统计量形式的HOIF；利用AMP状态进化方程加速该U-统计量期望的计算，并用tensor contraction实现解扰机动方差估计。
4. **空位：对称化算子的计算图优化与轨道维度的数据驱动选择（[7]）**
   - 武器：高阶U-统计量计算（einsum/tensor contraction/treewidth）
   - 动作：将 [7] 的置换对称化算子（轨道上求平均）实现为U-统计量计算图，用einsum批量缩并，分析treewidth以规避指数爆炸；设计基于交叉拟合残差方差最小化的数据驱动算法选择轨道维度k。
5. **空位：高维repro samples置信区间的半参数效率证明（[4]）**
   - 武器：高维渐近、minimax下界
   - 动作：在 [4] 的设定中，假设 nuisance 参数满足restricted eigenvalue条件，利用高维渐近理论控制Lasso初始选择的正则化偏差，推导repro samples区间长度的渐近展开，并与半参数效率下界比对以证minimax最优性。

---

### 本页聚合的论文

- [1] Proximal indirect comparison — Biometrika (2026-05-26)
- [2] Simplifying debiased inference via automatic differentiation and probabilistic programming — Journal of the Royal Statistical Society Series B (2026-05-26)
- [3] On the asymptotic validity of confidence sets for linear functionals of solutions to integral equations — Biometrika (2026-05-26)
- [4] Finite- and large sample inference for model and coefficients in high-dimensional linear regression with repro samples — Annals of Statistics (2026-05-26)
- [5] Change point estimation for a stochastic heat equation — Annals of Statistics (2026-05-26)
- [6] Causal effect estimation under network interference with mean-field methods — Annals of Statistics (2026-05-26)
- [7] Symmetry: A general structure in nonparametric regression — Annals of Statistics (2026-05-26)


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source](https://github.com/cxy0714/research-news)

