# Higher order Targeted Maximum Likelihood Estimation

**讲者**: Mark van der Laan  
**讨论人**: Alex Luedtke  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2021-01-19  
**主题**: 因果推断  
**视频**: <https://www.youtube.com/watch?v=2jumfnRQpxs> · [幻灯片](https://drive.google.com/file/d/1DfsoZUjgf3L8ly_wO3ye_U45-LNWMwfX/view?usp=sharing)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告是 **Targeted Learning (TL)** 纲领下的最新进展，核心问题是：

**在高度非参数（无限维）模型中，如何为因果 / 统计 estimand 构造一个既灵活（可使用 ML）又具备根号 n 渐近正态性和半参有效性的 plug-in 估计量？**

- **奠基与主流路线**：第一代方法是 **TMLE** (van der Laan & Rubin, 2006) 和 **debiased / one-step ML**（如 Chernozhukov et al. 2018 的 DML）。两者都利用 **影响函数 (influence function / canonical gradient)** 的线性项来校正初始 ML 估计的偏差，核心条件是 **二阶余项** \(R^{(1)}(P, P_0)\) 是 \(o_P(n^{-1/2})\)。
- **这个假设在实践中很紧**：\(R^{(1)}\) 通常是两个 nuisance 函数（如倾向得分和结局回归）偏差的乘积。如果每个偏差都是 \(O_P(n^{-1/4})\)，余项就是 \(O_P(n^{-1/2})\)，但还需要对数维度的惩罚。van der Laan 团队开发的 **Highly Adaptive Lasso (HAL)** (Benkeser & van der Laan 2016, Bibaut & van der Laan 2019) 是一个关键的奠基工作：它以 \(n^{-1/3}\) 的速率估计任何有界变差 (cadlag) 的 NUISANCE 函数，恰好让 TMLE 的 \(R^{(1)}\) 成为 \(o_P(n^{-1/2})\)，从而在只用“有界变差”一个光滑性假设下实现渐近有效性。
- **报告站在哪里**：报告指出 **即使有 HAL，有限样本中 \(R^{(1)}\) 仍可能很大**（尤其高维）。van der Laan 提出一个系统化的 **高阶 (Higher Order, HO-) TMLE** 框架，通过**递归地对初始估计量本身进行 TMLE（即对“TMLE的参数化版本”再做 TMLE）**，把余项的阶数从 2 提高到 3、4、... \(k+1\)，从而在有限样本中大幅削差，并为“有效影响函数退化”的 estimand 提供新的推断路径。

**关键文献**（来自幻灯片，ASR 无法准确给出）：
- van der Laan, Wang, & van der Laan (2021). "Higher Order Targeted Maximum Likelihood Estimation." arXiv:2101.06290.
- Bibaut & van der Laan (2019). "Fast rates for empirical risk minimization over càdlàg functions."  (HAL 收敛速率)
- Benkeser & van der Laan (2016). "The Highly Adaptive Lasso estimator."  (HAL 估计器)

### 二、最小内核 / 一个最简例子

**设定**：观测数据 \(O = (W, A, Y)\) i.i.d.，非参数模型。目标参数是治疗特异性均值
\[\psi_0 = \Psi(P_0) = \mathbb{E}_{P_0}[\mathbb{E}_{P_0}(Y|A=1, W)].\]

**可观测 / 不可观测**：
- **估计量**：\(\psi\) 的取值。
- **参数**：\(Q_0(W) = \mathbb{E}_0(Y|A=1, W)\)（结局回归），\(G_0(W) = P_0(A=1|W)\)（倾向得分）。\(P_0\) 是完整数据分布，但 \(\Psi\) 只依赖 \((Q_0, G_0, W\) 的边际分布)。
- **样本**：\(n\) 个 i.i.d. 副本 \((W_i, A_i, Y_i)\)。

**一阶 TMLE 的问题**：
有效影响函数为
\[D^{(1)}_{P}(O) = \frac{A}{G(W)}(Y - Q(W)) + Q(W) - \Psi(P).\]
TMLE 的 key equation 为
\[\psi^*_n - \psi_0 = (P_n - P_0) D^{(1)}_{P^*_n} + R^{(1)}(P^*_n, P_0).\]
二阶余项为
\[R^{(1)}(P, P_0) = \mathbb{E}_{P_0}\left[ \frac{(\bar{Q} - \bar{Q}_0)(\bar{G} - \bar{G}_0)}{\bar{G}} \right].\]
这是一个**乘积结构**：如果 \(\bar{Q}_n\) 和 \(\bar{G}_n\) 各有 \(n^{-1/4}\) 的 \(L_2\) 速率，则 \(R^{(1)} = O_P(n^{-1/2})\)，但这往往不够——如果有一个是错的，余项是主导项。

**二阶 TMLE 的核心创意（最简特例）**：
1. 把一阶 TMLE 映射视为一个**新参数**：\(\Psi^{(1)}_n(P) \equiv \Psi(\tilde{P}^{(1)}(P, \epsilon^{(1)}_n(P)))\)，其中 \(\tilde{P}^{(1)}\) 是沿第一阶 LFM 的起伏，\(\epsilon^{(1)}_n(P)\) 是 MLE。这是“对初始估计 \(P\) 施加一个数据驱动的非线性映射”。
2. 想让初始 \(P\) 很好地估计 \(\Psi^{(1)}_n(P_0)\)。因此，对 \(P\) 再做一次 TMLE（针对此新参数 \(\Psi^{(1)}_n\)），得到二阶 TMLE。
3. **关键技术技巧**：直接用经验测度 \(P_n\) 做 MLE 会破坏可微性。替代方案：用 HAL-MLE 估计一个平滑的 \(\tilde{P}_n\) 代替 \(P_n\)（即把 \(P_n\) 替换为一个正则化的 MLE），从而使 \(\Psi^{(1)}_n\) 可微。这被称为“**用 HAL 正则化**”。
4. **结果**：最终的二阶 TMLE 的精确展开为
\[\psi^{2,*}_n - \psi_0 = (P_n-P_0) D^{(1)}_{P^{(1)}_n(P_0)} + (P_n-P_0) D^{(2)}_{n, P^{(2)}_n(P_0)} + \text{(negligible)} + R^{(3)}_n,\]
其中 \(R^{(3)}_n\) 是**三阶余项**（比如两个 nuisance 的偏差乘积再乘以第三个东西）。这大大削去了偏差。

### 三、报告主体：讲者讲了什么

**[0:00–0:06] 开场与纲目**
- 讲者 Mark van der Laan 介绍这是关于“高阶 TMLE”的演讲。大纲：[0:02:00] 先回顾一阶 TMLE，再介绍 Highly Adaptive Lasso (HAL)，然后定义二阶 TMLE，演示它优化了一阶 TMLE 的精确总余项，给出精确展开和推断，推广到 k 阶，最后展示 ATE 和积分平方密度的模拟。

**[0:06–0:12] 一阶 TMLE 回顾**
- [0:06:00] 参数 \(\Psi\) 的路径导数、典范梯度。 [0:06:45] 典范梯度定义了“最不利参数子模型”(least favorable submodel, LFM)，其 score 就是典范梯度。 [0:07:09] TMLE：初始估计 \(P^0_n\) \(\rightarrow\) 沿 LFM 做 MLE 得 \(\epsilon_n\) \(\rightarrow\) 更新为 \(P^{1,*}_n\) \(\rightarrow\) 得到 plug-in 估计 \(\Psi(P^{1,*}_n)\)。 [0:09:03] 该估计量满足得分方程 \(P_n D^{(1)}_{P^{1,*}_n}=0\)。 [0:09:20] 关键等式：
\[\Psi(P^{1,*}_n) - \Psi(P_0) = (P_n - P_0) D^{(1)}_{P^{1,*}_n} + R^{(1)}(P^{1,*}_n, P_0).\]
- [0:09:50] 如果 \(R^{(1)} = o_P(n^{-1/2})\) 且 Donsker 条件成立（可选交叉验证避免），则 \(\Psi(P^{1,*}_n) - \Psi(P_0) \approx (P_n-P_0)D^{(1)}_{P_0} + o_P(n^{-1/2})\) -> 渐近有效。 [0:11:56] 强调**所有问题都归结到二阶余项是否小**。

**[0:12–0:15] ATE 示例**
- [0:12:45] \(O=(W,A,Y)\)，\(\Psi(P)=\mathbb{E}_P[\mathbb{E}_P(Y|A=1,W)]\)。 [0:13:30] 典范梯度：
\[D^{(1)}_P = \frac{A}{G(W)}(Y-Q(W)) + Q(W) - \Psi(P).\]
- [0:14:16] 二阶余项：\(R^{(1)}(P,P_0) = \mathbb{E}_{P_0}[(\bar{Q}-\bar{Q}_0)(\bar{G}-\bar{G}_0)/\bar{G}]\)。这是“双稳健”结构。 [0:14:44] TMLE 更新：在初始结局回归的 logit 上加一个共变量 \(A/\bar{G}_n\)，跑一个逻辑回归得 \(\epsilon_n\)。

**[0:15–0:18] 积分平方密度示例**
- [0:15:57] 参数 \(\Psi(P)=\int p^2 d\mu\)。一阶余项 \(R^{(1)} = -\int(p-p_0)^2 d\mu\)，这是个平方项（非“针对”），没有双稳健中的抵消，有限样本偏差严重。
- [0:16:33] 演示图片：沿着 LFM 移动 epsilon，TMLE 更新从不偏的初始出发朝真值移动，在似然拐点停住。

**[0:18–0:23] Highly Adaptive Lasso (HAL)**
- [0:18:04] 任意 cadlag 函数 \(f:[0,1]^d \rightarrow \mathbb{R}\) 可表示为：
\[f(x) = \int_{[0,1]^d} 1\{x \ge u\} df(u).\]
变差范数 \(\|f\|_v = \int |df(u)|\)。所以 f 可看作“零阶样条（指示函数）”的无穷线性组合，L1 系数范数即变差范数。
- [0:20:16] HAL-MLE：给定损失函数，最小化
\[\min_{f: \|f\|_v < C} P_n L(f).\]
离散化为 L1-正则回归（lasso），基函数数约 \(n \cdot 2^{d-1}\)，\(C\) 由交叉验证选择。
- [0:22:04] 收敛速率：损失差异（如 \(L_2^2\)）为 \(n^{-1/3}(\log n)^{d/2}\)（Bibaut & vdL 2019）。
- [0:23:00] **关键结论**：对于 ATE，以 HAL-MLE 为初始的 TMLE 仅在以下假设下即渐近有效：(a) 阳性假设；(b) 真值 NUISANCE 函数为 cadlag，有限变差。

**[0:24–0:27] 二阶 TMLE 的动机与定义**
- [0:24:20] 即使有 HAL，有限样本中 \(R^{(1)}\) 仍可能大（大常数因子受维度影响）。想把它从二阶提升到三阶。
- [0:24:40] 把一阶 TMLE 映射视为新参数：
\[\Psi^{(1)}_n(P) \equiv \Psi(\tilde{P}^{(1)}(P, \epsilon^{(1)}_n(P))).\]
目标是让初始 \(P\) 估计 \(\Psi^{(1)}_n(P_0)\) 更好。于是用 TMLE 再估计它。
- [0:26:05] 问题：\(\epsilon^{(1)}_n(P) = \arg\min_\epsilon P_n L(\tilde{P}^{(1)}(P,\epsilon))\) 不路径可微，因为用到了经验测度 \(P_n\)。解决方案：**用 HAL-MLE \(\tilde{P}_n\) 代替 \(P_n\)** 做这个 MLE \(\rightarrow \tilde{\epsilon}^{(1)}_n(P)\)。这使得 \(\Psi^{(1)}_n\) 路径可微。
- [0:27:50] 二阶 TMLE：\(P^{2,*}_n = \tilde{P}^{(1)}_n(\tilde{P}^{(2)}_n(P^0_n))\)，plug in 得 \(\Psi(P^{2,*}_n)\)。

**[0:28–0:35] 关键理论：二阶 TMLE 优化了精确总余项**
- [0:28:03] 一阶 TMLE 的“精确总余项”：
\[\bar{R}^{(1)}(\tilde{P}^{(1)}_n(P), P_0) = \Psi^{(1)}_n(P) - \Psi^{(1)}_n(P_0) + R^{(1)}(\tilde{P}^{(1)}_n(P_0), P_0).\]
所以优化初始 \(P\) 就是 \(\Psi^{(1)}_n(P)\) 尽可能接近 \(\Psi^{(1)}_n(P_0)\)。这正是对参数 \(\Psi^{(1)}_n\) 做 TMLE 所要做的。
- [0:35:00] 精确展开 (Exact Expansion for 2nd order TMLE)：
\[\psi^{2,*}_n - \psi_0 = (\tilde{P}_n - P_0) D^{(1)}_{\tilde{P}^{(1)}_n(P_0)} + R^{(1)}(\tilde{P}^{(1)}_n(P_0), P_0) + (\tilde{P}_n-P_0) D^{(2)}_{n, \tilde{P}^{(2)}_n(P_0)} + R^{(2)}_n(\tilde{P}^{(2)}_n(P_0),P_0) + \tilde{R}^{(3)}_n.\]
- [0:40:00] \(\tilde{R}^{(3)}_n = R^{(2)}_n(\tilde{P}^{(2)}_n(P^0_n), \tilde{P}_n) - R^{(2)}_n(\tilde{P}^{(2)}_n(P_0), \tilde{P}_n)\) 是三阶差。所以二阶级数正保三阶余项。
- [0:41:13] 通过**欠平滑** HAL-MLE（选更大 L1 范数），可以使 \((\tilde{P}_n - P_n) D^{(j)}\) 项可忽略，于是近似公式变为：
\[\psi^{2,*}_n - \psi_0 \approx (P_n - P_0) [ D^{(1)}_{\tilde{P}^{(1)}_n(P_0)} + D^{(2)}_{n,\tilde{P}^{(2)}_n(P_0)} ] + \tilde{R}^{(3)}_n.\]
推断可用估计的“和影响曲线” \(\bar{D}_n = D^{(1)}_n + D^{(2)}_n\)。

**[0:42–0:46] 推广与模拟**
- [0:42:02] 推广到 k 阶 TMLE：精确展开包含 k 个线性项和 (k+1) 阶余项。
- [0:43:04] ATE 模拟：GN 是 \(n^{-1/4}\) 一致，QN 不一致时，一阶 TMLE 的偏差随 n 增大 \( \sqrt{n} \)-scale 增加，二阶 TMLE 偏差稳定。
- [0:44:18] 积分平方密度的模拟：二阶 TMLE 对“非宽恕”(non-forgiving) 平方余项也有巨大增益，将偏差从 \(10^{-3}\) 降至 \(10^{-5}\)。

**[0:57–1:03] 讨论回应（与 Alex Luedtke）**
- [0:57:36] Alex 指出：若用 HAL-MLE \(\tilde{P}_n\) 本身作为初始估计，高阶 TMLE 会退化回 \(\Psi(\tilde{P}_n)\)（因为 KL 投影在模型 \(M(\tilde{P}_n)\) 上会返回 \(\tilde{P}_n\)）。关键在于，高阶展开本身为分析 \(\Psi(\tilde{P}_n)\)（欠平滑的 HAL plug-in）提供了新工具。
- [1:00:00] van der Laan 回应：同意，但这不否定高阶 TMLE 的优势——它允许用超级学习器等更灵活的初始估计（优于 HAL），通过多步 MLE 推动最终估计量靠近 HAL 但仍保留初始的适应性。欠平滑 HAL 效果的 plug-in 估计量也是一个合法竞争者，但 TMLE 框架更灵活。

### 四、对应论文与开放问题

**对应论文**：
- **arXiv**: van der Laan, Wang, & van der Laan (2021). "Higher Order Targeted Maximum Likelihood Estimation." arXiv:2101.06290 (幻灯片已确认，ASR 无法完整给出数字)。
- **参考 HAL**: Bibaut & van der Laan (2019). "Fast rates for empirical risk minimization over càdlàg functions." 以及 Benkeser & van der Laan (2016). "The Highly Adaptive Lasso estimator."

**开放问题**（只罗列，不判断可行性）：
1. **计算实现与大规模数据**：[0:32:00] van der Laan 提到可以“用数值回归 / Cholesky 分解”计算典范梯度，但报告没有展示具体算法复杂度。对于大 \(n\)、高 \(d\)，计算 \(n2^{d-1}\) 个基函数并做 L1-正则化是否可行？
2. **欠平滑的实操准则**：[0:40:00–0:41:13] 提议“选择比CV更大的L1范数”使 \((\tilde{P}_n - P_n)D^{(j)}\) 可忽略。如何具体选择这个放大倍数？是否存在无模型、可计算的准则（例如基于 bootstrap 的检验）？
3. **交叉验证的整合**：[0:11:25] 提到“cross-validated TMLE 可以避免 Donsker 条件”。高阶情况下，交叉验证 TMLE 的结构是什么？它如何与递归的 HAL-正则化 MLE 步骤兼容？
4. **对“有效影响函数为零”的 estimand**：[0:46:05] 提到“高阶 TMLE 为有效影响函数消失的问题打开了推断的大门”。具体例子是什么（例如某些 Neyman 意义下的正交参数）？在这种退化情形下，线性展开的首项消失，二阶级数项如何决定收敛速率和推断？

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

