# Selective Machine Learning of Doubly Robust Functionals

**讲者**: Eric Tchetgen Tchetgen  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2020-05-05  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=K-Uo5XbIE9I>

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [1911.02029](https://arxiv.org/abs/1911.02029) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

本报告属于 **「双重稳健功能估计中的机器学习模型选择」** 这条工作线。核心追问是：当目标参数（如平均处理效应）由双重稳健估计量估计时，需要先估计两个厌恶参数（倾向得分与结局回归），而这两个厌恶参数通常由机器学习算法得到。现有的 DML 框架（Chernozhukov et al. 2018, *Econometrica*）要求厌恶参数以足够快的速率收敛（至少快于 \(n^{-1/4}\)），但并未回答「当有一堆候选机器学习算法（随机森林、Lasso、Boosting 等）时，应如何选择最有利于减小目标参数偏差的那个算法」。本报告正是针对这一空缺提出选择准则。

- **奠基工作**：半参数效率理论（Bickel et al. 1993, *Efficient and Adaptive Estimation for Semiparametric Models*）提供了影响函数与 Neyman 正交性，是双重稳健估计的理论基础。DML 框架（Chernozhukov et al. 2018）将 cross-fitting 与 Neyman 正交矩方程结合，使厌恶参数可在较低收敛率下仍得到 \(\sqrt{n}\)- 一致的目标估计。
- **当前前沿**：在此之后，工作开始关注如何**专门针对目标参数**来调整厌恶参数估计，而非单纯优化预测损失。例如 Vansteelandt & Dukes (2020) 的 penalized 估计方程；又如「针对偏差的模型选择」思路——本报告是其中之一。
- **本报告的位置**：它提出的选择标准并非基于预测误差（如均方误差），而是基于目标估计量对厌恶参数扰动的**局部稳健性**。报告给出了两种Oracle选择准则（minimax 与 mixed minimax）的偏差阶数，并证明经验选择器与Oracle选择器之间的误差以 \(O(1/n)\) 速率衰减。后续讨论及讲者回应指出，这一选择准则可扩展到大量候选模型（包括模型的凸组合），但关于选择后如何做有效推断仍开放。

**注意**：报告提到一篇 arXiv 文章（1911.02029，见第四节），建议对照视频确认具体标题和合作者。另外讲者名字 (Eric Tchetgen Tchetgen) 及讨论者 (Stein van still on 可能为 Stijn Vansteelandt, 或 Stiven van still on? 待核实)。

### 二、最小内核 / 一个最简例子

以 **平均处理效应 (ATE)** 为贯穿例子。

#### 可观测数据与符号
- 观测数据：\((Y_i, A_i, X_i), i=1,\dots,n\)，其中  
  \(Y\) — 结局（连续或二值），  
  \(A\) — 处理（二值 0/1），  
  \(X\) — 协变量向量（高维）。
- 目标参数（estinand）：\(\psi = \mathbb{E}[Y(1) - Y(0)]\)，即平均处理效应。
- 识别假设：无混淆性（\(Y(a) \perp A \mid X\)）、正值性（\(0<\pi(x)<1\)）、一致性（\(Y = Y(A)\)）。在此假设下，  
  \(\psi = \mathbb{E}\big[ \mu_1(X) - \mu_0(X) \big]\)，其中 \(\mu_a(x) = \mathbb{E}[Y \mid A=a, X=x]\)。

#### 厌恶参数
- 倾向得分：\(\pi(x) = \mathbb{P}(A=1 \mid X=x)\)
- 结局回归：\(\mu_a(x), a=0,1\)。为简洁，通常只写 \(\mu_1(x), \mu_0(x)\)。注意他们是关于 \(x\) 的函数，可能是高维、非线性的。

#### 双重稳健估计量（Augmented Inverse Probability Weighting, AIPW）
影响函数（也是 Neyman 正交矩方程）为：
\[
IF(\psi) = \frac{A}{\pi(X)} (Y - \mu_1(X)) + \mu_1(X) - \frac{1-A}{1-\pi(X)} (Y - \mu_0(X)) - \mu_0(X) - \psi.
\]
其期望在真实 \(\pi, \mu\) 下为零。双重稳健性：只要 \(\pi\) 或 \(\mu\) 之一正确，则基于此矩方程的解仍一致估计 \(\psi\)。

#### 讲者提出的选择问题
设有 K1 种候选估计 \(\hat\pi_k\) （k=1..K1）和 K2 种候选估计 \(\hat\mu_{l}\) （l=1..K2）。目标是选出 \((k^*, l^*)\) 使得在后续用 AIPW 时，\(\hat\psi\) 的**偏差**最小。

讲者将目标转化为：选出一对 \((\hat\pi_k, \hat\mu_l)\) 使得 AIPW 估计量对该对中任一厌恶参数的**局部扰动**最不敏感。具体地，在某一锚定点 \((k,l)\) 处，考虑将结局回归从 \(\hat\mu_l\) 换成另一个候选 \(\hat\mu_{l'}\) 的扰动，定义扰动大小；同样考虑将倾向得分从 \(\hat\pi_k\) 换成 \(\hat\pi_{k'}\)。然后定义两种选择准则：

1. **minimax 准则**：取这两个方向扰动的 **最大值**，然后选使这个最大值最小的 \((\hat\pi_k, \hat\mu_l)\)。
2. **mixed minimax（mxmn）准则**：取两个方向扰动的 **最大值（但先对每个方向求平均？转写 [0:24:01-0:24:10] 讲得不清晰）**——实际上似乎是将对结局回归的扰动（对候选集合取所有可能换到其他候选的绝对值平均或最大）与对倾向得分的扰动分别计算，然后取其最大；但之后性质说 mixed minimax 偏差是两厌恶参数最佳收敛率的乘积，而 minimax 是较差的那个。因此推测 mixed minimax 可能采用每个方向分别取最大然后求和或取最大（转写提到“the first one will hold the purposes for asking one learner and we put turn the outcome regression where we look at all pairwise perturbation ... and we do the same thing holding the akka regression at King until now where we've been aiming at risk”）；准确形式需查论文。

**最简情况**：假设 \(K1=K2=2\)，即成对比较四种组合。选择器只需要在验证集上计算每个组合的扰动大小，选最小的即可。

### 三、报告主体：讲者讲了什么

**[0:00:00-0:01:50]** 开场与介绍。Dominique（可能是Dominik Rothenhäusler？）主持，介绍讲者 Eric Tchetgen Tchetgen（Wharton）。报告后由 Stein van still on（推测为 Stijn Vansteelandt）讨论。  
**[0:01:51-0:04:10]** 讲者引入问题：现代半参数方法常用机器学习来估计厌恶参数；以ATE为例，给出三种估计量——plug-in（使用回归）、IPW、以及双重稳健估计量。强调双重稳健估计量对厌恶参数的一致性要求更低。  
**[0:04:11-0:06:25]** 回顾 DML 框架的两个步骤：(1) 找到 Neyman 正交的矩方程（局部稳健）；(2) 用 cross-fitting 求解。要求厌恶参数收敛快于 \(n^{-1/4}\)。讲者指出，现有方法允许使用通用 ML 工具，但未说明如何选择具体 learner。  
**[0:06:26-0:09:00]** 提出两大挑战：(A) 如何从多个候选 learner 中选择最利于减小目标参数偏差的那个；(B) 选择后如何做有效推断（account for selection）。  
**[0:09:01-0:13:38]** 理论工具：半参数理论、影响函数。重点介绍一类**双重稳健影响函数**，其形式为 \(IF(\psi) = \text{linear term} + H\)，其中 \(H\) 是 \(B\)（与结局回归相关）和 \(P\)（与倾向得分相关）的乘积+线性项。此类影响函数满足双重稳健性：若 \(B\) 真或 \(P\) 真，则影响函数期望为零。许多功能（ATE、att、缺失数据下的均值、工具变量、负对照等）都属于此类。  
**[0:13:39-0:15:05]** 以 ATE 为例给出具体影响函数（AIPW 形式），并指出它自然满足 Neyman 正交性。  
**[0:15:05-0:17:10]** Q&A 环节：提问“是否关注选择后的推断还是仅选择？”讲者回答——先是选择，后做推断。  
**[0:17:11-0:22:00]** 提出选择框架：对每一对候选 \((k_1,k_2)\)（分别对应倾向得分和结局回归的 learner），定义两种方向扰动：(i) 固定倾向得分，扰动结局回归到另一候选；(ii) 固定结局回归，扰动倾向得分。基于此定义两种准则：  
- **minimax 准则**：取两种方向扰动的最大值的最大值（转写：maximal perturbation，可能是指 max over perturbations），选 min 组合。  
- **mixed minimax (mxmn) 准则**：另一种形式，转写 [0:23:50-0:24:10] 说“the second pseudo risk ... we take the maximum of those two perturbations again”但具体不同；讲者说“the minimax criteria does not have double robustness property, the mixed minimax does”。  
**[0:24:11-0:27:10]** 经验实施：多折交叉验证。在每折的训练集上训练所有候选 learner，在验证集上计算每个组合的扰动值（平均或最大），然后跨折取平均，选出最小组合。输出两个选定组合（对应两种准则）。  
**[0:27:11-0:32:00]** 理论结果（Oracle 分析）：  
- 假设所有倾向得分候选的收敛率为 \(\nu_1,...,\nu_{K1}\)，结局回归收敛率为 \(\omega_1,...,\omega_{K2}\)。  
- 对于 minimax Oracle 选择器，偏差阶为 \(\max\{\nu_{\min}, \omega_{\min}\}\)？转写 [0:29:12-0:30:00] 说到 minimax Oracle 偏差为最大速率（即较差的收敛率）。  
- 对于 mixed minimax Oracle 选择器，偏差阶为 \(\nu_{\min} \times \omega_{\min}\)（乘积），具有双重稳健性质。  
- 经验选择器与 Oracle 选择器之间的偏差差距以 \(O(1/n)\) 速率衰减。  
- 证明基于 van der Vaart 和同事关于 degenerate U-statistics 的指数不等式。  
**[0:32:00-0:35:00]** Q&A：关于“如果某个 learner 很烂，取 max 是否稳健？”讲者回答：mixed minimax 仍能获得乘积率（即使有一个差 learner，乘积仍可能趋于 0），但 minimax 会被差 learner 拖累。建议使用 mixed minimax。  
**[0:35:00-0:37:30]** 模拟：线性数据生成，比较 DML 使用单一 learner（GBoost, Lasso, RF）与本文选择器。结果显示选择器（minimax, mxmn）在偏差上有所改进。  
**[0:37:31-0:39:30]** 选择后的推断思路：通过光滑近似（smooth approximation）将离散选择变为模型平均，参数 \(\tau\) 控制近似程度（\(\tau\to\infty\) 退化为离散选择）。这样可以使用标准推断（但未给出具体渐近分布定理，仅陈述思路）。  
**[0:39:31-0:42:30]** 数据应用：ICU 患者用红细胞生成素（EPO）的 30 天存活率。候选模型包括逻辑回归、lasso、随机森林、梯度提升树。结果：点估计相似但置信区间略宽（反映模型选择的不确定性）。  
**[0:42:31-0:43:20]** 结尾与感谢。  
**[0:43:20-0:51:00]** 讨论部分（Stijn Vansteelandt 等）：称赞工作，提出两个关键问题：(1) 什么条件下能实现有效推断？(2) 如果两个厌恶参数都有 Learner 收敛到真值且速率够快，那么选择策略的额外好处是什么？讲者回应：若两者都很快，mixed minimax 的偏差乘积仍较小，但 minimax 的偏差可能更大；推断需使用光滑近似，条件需进一步探索。  
**[0:51:41-0:56:00]** 听众提问（Ilya）：能否刻画数据生成类使所选准则等价于最小化真实平方偏差？讲者回答尚无结果。最后结束。

### 四、对应论文与开放问题

#### 对应论文
讲者提到「paper can be found on the archive」（[0:42:15]）。候选论文为 arXiv:1911.02029。根据原 curator 标注，该论文题为「Selective Machine Learning of Doubly Robust Functionals」。建议对照视频确认标题与作者（Eric Tchetgen Tchetgen, 张元？等）。

#### 开放问题（基于转写与讨论）
1. **选择后推断的条件**：讲者仅给出光滑近似思路，但未给出严谨的渐近分布定理。需回答在何种条件下（如至少一个厌恶参数收敛快于 \(n^{-1/4}\)，且选择几乎总是收敛的好模型）才能得到 \(\sqrt{n}\)- 正态性及一致方差估计（见 [0:37:31] 及讨论者提问 [0:49:30-0:50:02]）。
2. **准则与真实偏差的关系**：讲者承认所提出的扰动准则只是真实平方偏差的替代；问题在于：是否存在一类数据生成过程，使得该准则与真实偏差范数等价？即最大化扰动对应最小化偏差？（Ilya 提问，[0:54:42]）
3. **扩展到高阶或多重稳健功能**：讲者提到「可以扩展到多重稳健影响函数」，但未展开（[0:41:00]）。具体如何定义扰动与选择准则？
4. **连续选择 vs 离散选择**：当候选数很大（如模型加权平均的凸组合）时，离散选择可能不稳定。讲者提到正在探索凸组合的权重选择（[0:41:30]），但尚未给出理论。
5. **不同范数下的误差界**：讨论中提出可以使用其他范数（如 \(L_1\)），但讲者说无法导出可证明的误差界（[0:40:40-0:40:56]）。是否可能存在其他度量可获得更好的性质？
6. **有限样本与渐近增益**：当有多个 Learner 均以 fast rate（好于 \(n^{-1/4}\)）收敛时，选择策略有何实际益处？讨论者指出这一情景下渐近无差别，但有限样本可能有改善（[0:50:30-0:51:00]）。清楚刻画这种有限样本改善的条件是开放问题。

以上开放问题均扎根于转写中的特定语句，研究者可根据自身兴趣选择深入。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

