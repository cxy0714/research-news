# Automatic Debiased Machine Learning for Dynamic Treatment Effects and General Nested Functionals

**讲者**: Vasilis Syrgkanis  
**讨论人**: Eric Tchetgen Tchetgen  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2022-09-27  
**主题**: 因果推断  
**视频**: <https://youtu.be/RYN094Ql2Wg>

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

## 相关论文

- [2203.13887](https://arxiv.org/abs/2203.13887) *（尚未精读 — `talks read --id … --read-papers` 可补）*

---

### 一、这场报告在讲哪条工作线

这场报告属于 **自动去偏机器学习（Automatic Debiased Machine Learning, AutoDML）** 这一子方向。它的核心追问是：**如何在不手动推导去偏项（efficient influence function / Riesz representer）具体形式的前提下，自动构造出对任意半参数泛函的、可用于推断的正则估计量？**

- **方向背景与奠基**：半参数估计理论的核心结论是，几乎任何光滑的泛函都可以通过"去偏"或"正交化"来获得根号n-渐近正态、小偏倚的估计量，典型例子包括 DR-IPW (Robins, Rotnitzky & Zhao 1994)、双稳健估计 (Bang & Robins 2005) 和去偏机器学习 (DML, Chernozhukov et al. 2018)。但所有这些方法都要求研究者**手动**推导出具体泛函对应去偏项（或其构成部分，如倾向得分 / 条件密度）的解析形式。
- **当前前沿与 AutoDML 的定位**：在大量新因果泛函（动态治疗效应、自适应策略评估、替代结局下的长期效应等）涌现的背景下，手动推导变得越来越繁琐或不可行。AutoDML 的思路是**绕过解析推导，通过巧妙的损失函数直接估计去偏项（Riesz 表示子）**，使整个过程自动化。本报告及其对应论文（arXiv 2203.13887）正是在这种理念下，将 AutoDML 从静态处理效应沿着多重稳健性递归扩展到**动态治疗效应和一般嵌套泛函**，并提供了一种不影响效率的自动去偏框架。
- **关键相关工作**：直接估计 Riesz 表示子的思想可追溯到 Newey (1994, *Series estimation of semiparametric models*) 和 Chen & Reiss (2007, *Estimation of a semiparametric model with some semiparametric ...*)；通过 L1-惩罚线性基来估计该表示子的自动方法出现在 Chernozhukov, Newey & Singh (20??, ???)。AutoDML 则允许使用**任意 ML 模型**（神经网络、随机森林、梯度提升等）来估计该表示子，并给出有限样本理论保证。

### 二、最小内核 / 一个最简例子

**模型设定（静态 ATE）**：
- **可观测数据**：$(Y, T, X)$, 独立同分布，其中 $Y \in \mathbb{R}$ 是结果，$T \in \{0,1\}$ 是二值处理，$X \in \mathbb{R}^d$ 是协变量。
- **未观测**：潜在结果 $Y(1), Y(0)$。
- **识别假设**：无混杂 $Y(t) \perp\!\!\!\perp T \mid X$；重叠 $0 < \mathbb{P}(T=1|X) < 1$。
- **目标参数（estimand）**：平均处理效应（ATE）$\theta = \mathbb{E}[Y(1) - Y(0)]$。
- **等价写成线性矩泛函**：
  $\theta = \mathbb{E}[g_1(X) - g_0(X)]$，其中 $g_t(X) = \mathbb{E}[Y \mid T=t, X]$.

**核心思想（一个最简步骤）**：
1. **去除偏置**：直接插件估计 $\hat{\theta}_{\text{plugin}} = \frac{1}{n} \sum_i (\hat{g}_1(X_i) - \hat{g}_0(X_i))$ 会因为 $\hat{g}$ 的估计偏倚（来自正则化 ML）导致 $\sqrt{n}$-不一致。
2. **去偏修正**：修正后估计量 $\hat{\theta} = \frac{1}{n} \sum_i \left[ \hat{g}_1(X_i) - \hat{g}_0(X_i) + \hat{a}(X_i, 1) (Y_i - \hat{g}_1(X_i)) - \hat{a}(X_i, 0) (Y_i - \hat{g}_0(X_i)) \right]$, 这里的 $\hat{a}(X, t)$ 就是**Riesz 表示子**。
3. **Riesz 表示子**：对于 ATE，它的解析形式是 $\alpha_0(X, t) = \frac{t}{\pi_0(X)} - \frac{1-t}{1-\pi_0(X)}$, 其中 $\pi_0(X) = \mathbb{P}(T=1|X)$. 手动推导后需要估计倾向得分 $\pi$. 但 AutoDML 自动估计它的方式是从数据中直接学习：定义损失函数 $L(a) = \mathbb{E}[a(X,T)^2 - 2 a(X,T)(g_1(X) - g_0(X))]$, 其极小化等价于 $\mathbb{E}[(a(X,T) - a_0(X,T))^2]$, 因此只需观测 $\{Y_i, T_i, X_i\}$ 和**黑箱访问**线性矩泛函 $\psi(g) = \mathbb{E}[g_1 - g_0]$, 无需知道 $a_0$ 的解析形式.

**为什么这成立**：因为线性泛函 $\psi(g)$ 可以写成乘积形式 $\mathbb{E}[a_0(X,T) g_T(X)]$, 于是 $(Y - \hat{g})$ 乘以 $\hat{a}$ 的期望近似为 $\mathbb{E}[(a_0 - \hat{a})(g_0 - \hat{g})]$, 即两个误差的乘积。这就是双稳健性的来源。

### 三、报告主体：讲者讲了什么

**[0:00 - 0:05]** **开场与动机**
- 讲者（Vasilis Syrgkanis）介绍他们希望将因果推断变得像自动驾驶一样**自动化**：领域专家只需提供数据、设定目标参数，自动去偏方法即可给出置信区间。

**[0:05 - 0:12]** **自动去偏（AutoDML）的切入点**
- **线性矩泛函**类：$\theta = \mathbb{E}[m(Z; g)]$, 其中 $g$ 是某些回归函数（例如 $g_t(X) = \mathbb{E}[Y|T=t,X]$）。这覆盖了 ATE、政策效应、平均边际效应等。
- **去偏与 Riesz 表示子**：去偏修正项 $\hat{a}(X,T) (Y - \hat{g}(X,T))$, 其中 $\hat{a}$ 需要是线性泛函 $\theta(g) = \mathbb{E}[m(Z; g)]$ 的 Riesz 表示子。
- **核心理论：双稳健性**：如果 $a$ 和 $g$ 都估计到 $o_p(n^{-1/4})$（即 $n^{-1/4}$ 速度），则 ATE 估计量达到 $\sqrt{n}$-渐近正态（双稳健性）。若两者之一更快，则另一者可慢。
- **关键转变**：不推导 $a_0$ 的解析形式，而是直接通过损失函数估计。
    - 损失函数：$\ell(a) = a(X)^2 - 2 \cdot m(Z; a)$ —— 这是对 Riesz 表示子的自动估计（Newey 1994 隐含，但 AutoDML 推广到任意 ML 模型）。

**[0:15 - 0:18]** **估计理论**
- 若 $a$ 属于某个函数类 $\mathcal{F}$（如 VC 子图、神经网络、RKHS），则拿着该损失做 ERM 会得到 $\|\hat{a} - a_0\|^2 = O_p(\delta_n^2 + \text{bias}^2)$, 其中 $\delta_n$ 是 $\mathcal{F}$ 的临界半径。
- 对参数类 $d$-维，$\delta_n \asymp \sqrt{d/n}$, 得到 $n^{-1}$ 速率；对神经网络，可达到 $\approx n^{-1/2}$ 至 $n^{-1}$。

**[0:23 - 0:27]** **非线性泛函的推广**
- 若 $\theta$ 不是线性的（如平均边际效应），需要先对 $g$ 线性化（方向导数），然后对该线性化的方向导数应用 AutoDML。这是**自动微分**的延伸。

**[0:27 - 0:33]** **实现（神经网络 / 随机森林）**
- **神经网络**：基于 Rosenbaum-Rubin 充分性，讲者提出**多任务学习**：同一个表示层用于学习 $a$ 和 $g$, 降低学习难度。这参考了 David Blei 小组的工作（可能是“贝叶斯因果森林”？字幕可能有误），但 AutoDML 不需要手动指定 $a$ 的解析形式。实验结果显示，在 IHDP 数据集上，MAE 为 0.11 vs 插件法的 0.146。
- **随机森林**：通过将 $\ell(a)$ 转化为条件矩限制（条件期望等于 0），与广义随机森林 (Athey, Tibshirani & Wager 2019) 对接。实验表明具有良好的置信区间覆盖。

**[0:33 - 0:44]** **动态治疗效应与嵌套泛函**
- **数据结构**：两阶段 $S_1, T_1, S_2, T_2, Y$。
- **识别（G-公式递归）**：
  $\theta = \mathbb{E}[g_1(S_1, \tau_1)]$, 其中 $g_1(s_1, t_1) = \mathbb{E}[g_2(S_2, \tau_2) \mid T_1=t_1, S_1=s_1]$, 而 $g_2(s_2, t_2) = \mathbb{E}[Y \mid T_2=t_2, S_2=s_2]$。
- **自动去偏（递归 Riesz）**：
  - 对第一层矩 $\psi_1(g_1) = \mathbb{E}[g_1(S_1, \tau_1)]$, 去偏修正项为 $a_1 (g_2 - g_1)$。
  - 但 $g_2$ 也有估计误差，故需要第二层矩 $\psi_2(g_2) = \mathbb{E}[a_1 g_2(S_2, \tau_2)]$ 的去偏，修正项为 $a_2 (Y - g_2)$。
  - 最终估计量：$\hat{a}_1 (Y - \hat{g}_2) + \hat{a}_1 \hat{a}_2 (Y - \hat{g}_2)$（具体形式需核对论文）。
- **渐近性质**：双稳健性演化为“**多重稳健性**”——要求每层 Riesz 表示子误差与对应回归函数误差的乘积足够小。时间层数 $M$ 增加时，速率条件会**指数变差**（不利用时间共享结构时）。

**[0:44 - 0:53]** **扩展与结论**
- 该框架可延伸至**自适应政策评估**、**动态离散选择模型**、**非参数 IV**、**数据融合（如替代结局）**等领域。
- 核心信息：对于一大类因果估计量，AutoDML 无需手算 EIF，且可用任意 ML 模型。

**[0:53 - 1:10]** **讨论（Eric Tchetgen Tchetgen）**
- Tchetgen Tchetgen 将 AutoDML 定位为 **“小偏倚性质（small-bias property）的民主化”**，高效地避免了 EIF 的繁琐计算。
- 他提出几个开放讨论点：
  - 如何让 AutoDML 利用参数模型假设进一步提升效率（讲者回应：在限制 $g$ 的同一函数类中估计 $a$ 通常足以捕获效率）。
  - 误差在动态结构中的传播：若 $g_2$ 差，$g_1$ 会更差（讲者承认若不利用时间共享，误差会指数累积，这是开放问题）。
  - 高估值 / 参数共享：若知道某些 $a$ 或 $g$ 在时间点间相似，应如何融入？讲者建议可通过多任务学习或重新形成矩条件来纳入参数共享假设。
  - 超参数选择：讲者建议直接使用“Riesz 损失”的留出样本进行选择，这样会自然趋于最小化 $\theta$ 误差。

### 四、对应论文与开放问题

**对应论文（权威，来自摘要）**：

- 报告主体基于 **Chernozhukov, V., Newey, W., Singh, R., & Syrgkanis, V. (2022). Automatic Debiased Machine Learning for Dynamic Treatment Effects and General Nested Functionals. arXiv: 2203.13887**。
- 报告中演示的 AutoDML 静态部分与 **Chernozhukov, V., Newey, W., & Singh, R. (2022). Automatic Debiased Machine Learning for Linear Moment Functionals** (可能对应 arXiv: 2101.03953) 有重叠。讲者提及 “第一性反故去偏”和“Athey et al. 的广义随机森林动机相似” 代表已知工作，具体需核实。

**报告留下的开放问题**：

1. **时间维度 / 长 horizon 问题**：[1:01:10-1:02:00] 讲者承认，若不做参数共享或平稳性假设，AutoDML 在长 horizon 动态结构中的速率会**指数累积**（近似 $2^M / \epsilon^2$），目前无理论修复，是明显开放问题。
2. **参数共享 / 获取效率的代价**：[0:57:50-0:58:30] Tchetgen Tchetgen 提问如何将已知的结构假设（如某些 $a$ 或 $g$ 是相同函数）自动注入自动框架。讲者回应“也许需重新定义矩条件”而非自动法，这表明在模型保持识别性前提下，全自动化和高效率之间的张力并未完全解决。
3. **非光滑泛函（如分位处理效应）**：[0:53:50-0:54:10] Tchetgen Tchetgen 提及“结构参数是积分方程的解”（如生存分析中的自然直接效应、代理 IV），此时 Riesz 表示子甚至不存在或难以估计，AutoDML 框架是否可扩展到此境界尚不清楚。
4. **Riesz 表示子的唯一性**：[0:24:20-0:25:00] 有听众提问 Riesz 表示子是否唯一；讲者回答不唯一但损失函数 $\mathbb{E}[a^2]$ 会挑最小 $L^2$ 范数的那个，但这是否保证效率需进一步验证。

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

