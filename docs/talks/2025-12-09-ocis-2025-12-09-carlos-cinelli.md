# Long Story Short: Omitted Variable Bias in Causal Machine Learning

**讲者**: Carlos Cinelli  
**讨论人**: Dominik Rothenhäusler  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2025-12-09  
**主题**: 因果推断  
**视频**: <https://youtu.be/1RZz1gLse7s> · [幻灯片](https://drive.google.com/file/d/14FU1KukMS-DF1vzurj_EiUdT7sfrAsnP/view?usp=share_link)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告在讲一条经典但仍在活跃发展的因果推断工作线：**省略变量偏倚（Omitted Variable Bias, OVB）的敏感性分析**。这条线追问的核心是：“当因果识别依赖于‘无未观测混杂’这一不可验证假设时，结果对违反该假设有多敏感？” 传统上，这一追问在**线性回归**框架中就有标准答案（如 Theil 1957 的 OVB 公式、Angrist & Pischke 对其的推崇），并在 2000 年代由 **Rosenbaum (2002, 2010)** 等人在**观测研究设计**（如边际敏感模型）中系统化为敏感性分析学科。近十年，随着**双机器学习（Double/Debiased ML, DML）** 和**可解释机器学习**的兴起，工作线的一个自然延伸是：**当用 ML（随机森林、神经网络等）灵活估计因果参量（如 ATE、平均因果导数）时，是否还能写出一个像线性 OVB 公式那样简单、直观的偏倚界？**

- **主流路线**当前分为几支：
  - **边际敏感模型（Marginal Sensitivity Models, MSM）**：用单个参数 λ 约束未观测混杂改变治疗几率的上界（如 Tan 2006; Zhao, Small & Bhattacharya 2019; Dorn & Guo 2022 给出其双重锐界与双重稳健推断）。
  - **方差基线敏感界（Variance-based Sensitivity Bounds）**：用 R² 类参数表示未观测混杂对治疗与残差变化的解释能力（如 A. M. d’Haultfoeuille 等人 2019; 以及讲者此前的 OVB 的工作——Cinelli & Hazlett 2020, JRSS-B）。
  - **运用现代半参效率理论的敏感分析**：将偏倚分解为“outcome regression 残差”与“Riesz representer 残差”的内积（这实际上是本报告的核心贡献）。

- **本报告站在哪**：报告的工作同时属于“方差基线界”与“半参效率理论”两股力量的交汇处。它将 Cinelli & Hazlett (2020) 针对 OLS 的 OVB 公式（用偏 R² 与偏相关系数表达）**一般化到任意线性功能（linear functional of the CEF）** 在**完全非参数或部分线性模型**下的表达，并用 **Riesz 表示定理**与 DML 的**正交条件**做桥梁，使得同样的直觉（偏倚 ≈ 两个残差部分的 R² 乘积 × 相关性 × 尺度因子）**适用于 ATE、ATT、平均因果导数等广泛参量**，且无需假定条件期望函数为线性。这是业界首次在 DML 框架下给出与线性 OVB 形式几乎一致的、可直接分解为三个可解释成分的界。

- **关键引用**（基于幻灯片，转写 **可能听错人名**）：
  - **奠基**：Cinelli & Hazlett (2020) “Making Sense of Sensitivity: Extending Omitted Variable Bias” JRSS-B （线性 OVB 分解为核心 R²+ρ 形式）。
  - **EXTEND POST-DML**: 本报告对应论文：Chernozhukov, Cinelli, Newey, Sharma, Syrgkanis (2025) “Long Story Short: Omitted Variable Bias in Causal Machine Learning” forthcoming at Review of Economics and Statistics.
  - **相关最近的锐界工作**：Dorn & Guo (2022) (转写中提及为 “dor and b and jaza 2022” 可能是 Dorn, B. & Guo, J. “Sharp Bounds on the Average Treatment Effect under Marginal Sensitivity Models”)。

### 二、最小内核 / 一个最简例子

先理清符号：

- **可观测数据**：$W = (Y, D, X)$，其中 $Y$ = outcome (连续)，$D$ = treatment (二进制/连续)，$X$ = 可观测协变量向量。**不可观测的混杂**记为 $U$（可以是向量）。
- **目标**：$\theta = \mathbb{E}[m(W, g)]$，其中 $g(w) = \mathbb{E}[Y \mid D, X, U]$ 是“长回归（long regression）”的条件期望函数，$m$ 是一个**线性功能**（例如 ATE: $m(W,g) = g(1, X, U) - g(0, X, U)$）。
  但在实际数据中，我们仅观测到 $(Y, D, X)$，因此只好用“短回归” $g_s(w_s) = \mathbb{E}[Y \mid D, X]$ 去近似 $\theta$，得到 $\theta_s = \mathbb{E}[m(W_s, g_s)]$ ($W_s$ 包含 $D, X$ 而没有 $U$)。
- **核心对象**：**Riesz 表示器 (Riesz Representer)**。对于任何平方可积函数空间上的线性功能 $\ell(h)$，存在唯一函数 $\alpha \in L^2$ 使得 $\ell(h) = \mathbb{E}[h(W) \alpha(W)]$。
  — 长回归的 $\alpha$：对应 $g$ 的 Riesz 表示器（例如对 ATE，$\alpha(W) = D/e(W) - (1-D)/(1-e(W))$，其中 $e(W) = \mathbb{P}(D=1 \mid X,U)$ 是长倾向分）。
  — 短回归的 $\alpha_s$：相似的 Riesz 表示器用 $X$ 和 $D$ 算（例如 $\alpha_s(W_s) = D/e_s(X) - (1-D)/(1-e_s(X))$，其中 $e_s(X) = \mathbb{P}(D=1 \mid X)$）。

- **关键恒等式**：$\alpha_s = \mathbb{E}[\alpha \mid W_s]$。即短 Riesz 表示器是长 Riesz 表示器在短协变量空间的投影；同理，$g_s = \mathbb{E}[g \mid W_s]$。

**最简特例：d=1 的二进制治疗，无 X 协变量。** 此时：

- 长回归：$g(1, U) = \mathbb{E}[Y \mid D=1, U]$，$g(0,U) = \mathbb{E}[Y \mid D=0, U]$；$\theta = \mathbb{E}[g(1,U)-g(0,U)]$（真实 ATE）。
- 短回归：$g_s(1) = \mathbb{E}[Y \mid D=1]$，$g_s(0) = \mathbb{E}[Y \mid D=0]$；$\theta_s = \mathbb{E}[Y \mid D=1] - \mathbb{E}[Y \mid D=0]$（naive 比较均值）。
- 偏倚 $\theta - \theta_s$ 直接由 Simpson 悖论公式：$\text{bias} = \mathbb{E}_{U|D=1}[\mathbb{E}[Y|D=1,U]] - \mathbb{E}_{U|D=0}[\mathbb{E}[Y|D=0,U]] - (\text{naive diff})$。

但报告的通用公式则将偏倚重写为：

$$
\text{bias} = \rho \times \sqrt{R^2_{Y\sim U|D,X}} \times \sqrt{\frac{R^2_{\alpha \sim U | D,X}}{1 - R^2_{\alpha \sim U | D,X}}} \times \text{scaling factor},
$$

其中：
- $R^2_{Y\sim U|D,X}$：在控制了 $D,X$ 后，$U$ 还能解释 $Y$ 残差变异的多大比例。
- $R^2_{\alpha \sim U | D,X}$：$U$ 能解释 Riesz 表示器残差（即权重残差）的多大比例。
- $\rho$：这两个残差之间的相关系数（介于 -1 到 1，最 adversarial 情况为 ±1）。
- 尺度因子：$\frac{\text{sd}(Y \perp D, X)}{\text{sd}(D \perp X)}$（线性回归特例）或更一般地由 $\lVert Y - g_s(W_s) \rVert_2$ 与 $\lVert \alpha_s \rVert_2$ 给出。

这个公式的价值在于：**使用者不需要知道 $U$ 具体的作用方向或结构，只需要就两个 R² 型参数给出一个上限（比如“U 不能比 income 解释得更多”），便能立即得到偏倚的单一数值或边界。**

### 三、报告主体：讲者讲了什么

**[0:00-0:02]** 报告序曲：介绍讲者 Carlos Cinelli（华盛顿大学），以及讨论人 Dominik Rothenhäusler（Stanford）。

**[0:02-0:06]** 动机案例：401(k) 对净金融资产的影响。使用 401(k) 资格作为 treatment ($D$)，net financial assets 作为 outcome ($Y$)，调整标准协变量 $X$ (年龄、收入、家庭规模、教育等) 满足条件可忽略性（conditional ignorability）。用随机森林 + DML 估计 ATE ≈ $9,000（部分线性模型）≈ $8,000（全非参数模型）。

**[0:06-0:10]** 潜在混杂的故事：雇主可能提供最高达收入 5% 的匹配缴款 match amount，该变量 $M$ 同时关联 $D$（是否 eligible）与 $Y$（储蓄倾向），但不可观测。若 $M$ 是真正的混杂 $U$，则调整 $X$ 不足以识别。

**[0:10-0:12]** 核心声明：论文贡献为一种**省略变量偏倚的通用理论**，适用于 ATE、ATT、平均因果导数等广泛参数（线性功能），且仅需对 $U$ 在 outcome 与 treatment 上的解释能力做简单判断即可得到偏倚边界。可以推广到部分线性、完全非参数等设定，并且用 DML 估计。

**[0:12-0:15]** OLS 热身复习：$Y = \theta D + X'\beta + U'\gamma + \epsilon$ （长回归） vs $Y = \theta_s D + X'\beta_s + \epsilon_s$ （短回归），传统 OVB 公式 $\text{bias} = \theta - \theta_s = -\gamma' \delta$（$\delta$ 是 $U$ 在 $D$ 上的回归系数）。该公式难以直接用于敏感性分析。讲者提出重新参数化为：

$$
\text{bias} = \rho \times (R^2_{Y\sim U|D,X}) \times \left( \frac{R^2_{D\sim U|X}}{1 - R^2_{D\sim U|X}} \right)^{1/2} \times \frac{\text{sd}(Y \perp D,X)}{\text{sd}(D \perp X)}.
$$

**[0:15-0:20]** 一般理论部分：
- 引入长 CEF $g$ 和短 CEF $g_s$；定义目标 $\theta = \mathbb{E}[m(W,g)]$（线性功能）与短参量 $\theta_s = \mathbb{E}[m(W_s, g_s)]$。
- 由 Riesz 表示定理：$\theta = \mathbb{E}[g(W) \alpha(W)]$，$\theta_s = \mathbb{E}[g_s(W_s) \alpha_s(W_s)]$。
- 核心性质：$\alpha_s = \mathbb{E}[\alpha | W_s]$（短Riesz表示器是长Riesz表示器的条件投影）。对 ATE 举例，$\alpha$ 为 IPW 权重 $D/e(W)-(1-D)/(1-e(W))$。
- 利用正交条件推导出 OVB 在非参数情形下的通用分解，与线性情况形式完全相同，只是将 $R^2_{D\sim U|X}$ 换成 $R^2_{\alpha \sim U|D,X}$。

**[0:20-0:27]** 讨论不同 estimands 下的敏感参数：
- 部分线性模型 → 偏 R²（variance explained）。
- 完全非参数 ATE（二进制治疗） → 平均精度增益（gain in average precision）。
- ATT → 平均几率变化（gain in average odds）。讲者指出这些敏感参数虽名称不同，但取值均在 [0,1] 且可相互转换，因而便捷。

**[0:27-0:33]** 统计推断与估计：
- 给出边界 $\theta_{\text{low}} = \theta_s - \text{bias}$；bias 可从中公式分解的三成分（短参量、残差平方和、Riesz 表示器范数）估计。每成分有其正交得分，可用 DML+交叉拟合估计并构建置信区间。

**[0:33-0:45]** 与边际敏感模型的关系：
- 标准敏感模型（如 MSM Lambda）是从“对 U 施加一条约束”出发推导整个行列的边界；OVB 公式则反向：给定偏倚大小，如何构造 U 的最弱约束。OVB 公式表明，**只需对“偏倚的两个 R² 型参数”设定上限，不必对整个 U 的边际分布/条件分布做全局约束**。MSM 要求对 $\Lambda$ bound 最差情况下的 odd change，而 OVB 允许 bound 平均变化。后者假设更弱、可能产生更紧的界。
- 举例：若 MSM 认为 odds 改变最多 50% ($\Lambda = 1.5$)，可换算为一个 4% 残差 R² 上界用于 OVB 公式。
- 提问环节：与 Austin 2019, E-value (VanderWeele & Ding 2017) 等对比。讲者简要回应：OVB 用的是不同的敏感参数 (R², odds, precision)，且更灵活（可与各种生存/中介分析搭配）。

**[0:45-0:55]** 回到实证样例：
- **最小敏感报告**：提供 **robustness value (RV)** 作为一个描述性统计量（类似 p-value）。对于部分线性 ATE 的 RV 为 5.4%。含义：若某未观测混杂 $U$ 对 outcome 和 treatment 的残差 R² 均小于 5.4%，则不能推翻在 5% 显著性水平上的结论。
- **构造最大匹配场景**：假设 $U$ 如同雇主匹配缴款，解释 outcome 约 4% ($R^2_{Y|U}$)，treatment 约 3%，均低于 RV。故该特定场景不足彻底推翻结果。
- **等高线图**：x−y 平面分别为 $R^2_{\alpha \sim U|D,X}$ 与 $R^2_{Y \sim U|D,X}$；图片显示原估计 95% CI 下限如何随公共的强被衰减。最大匹配场景令下限从 \$6,000 降至约 \$2,500。
- **与 income 对标**：若 $U$ 的强度 = 收入（模型中最重要的可观测协变量），则能彻底将估计推至负值。讲者认为收入这种强度的混杂几乎不可想象，而“双收入者”等弱协变量则不能推翻。

**[0:55-1:00]** 讨论与开放问题：
- **ρ 的相位**：Dominik 提出 ρ 是否应常设为 1？讲者回应：线性单混杂下 ρ ≡ 1；多混杂在非线性模型中 ρ 往往 < 0.5，且实证见到 < 0.5。但使用者应主动检查 data 中 observed covariate 的 ρ 并以此为启发。
- **当边界宽且无信息时**：这是正面信息（知道自己知之不多），应回头设计新研究（新人群、RCT、辅助数据）；尚无形式化方法整合多种证据源。
- **二进制 outcome/治疗下的锐界**：边界目前仅基于整体 R² 约束，未利用尺度信息。解析式得锐界需逐类推导（Binary treatment 已有工作进展）。

### 四、对应论文与开放问题

- **(a)** 论文相关信息：
  - 全名（幻灯片确认）：**Chernozhukov, V., Cinelli, C., Newey, W., Sharma, A., & Syrgkanis, V. (2025). Long Story Short: Omitted Variable Bias in Causal Machine Learning.** 已被 *Review of Economics and Statistics* 接收（即将发表）。arXiv 编号暂未在材料中提供（转写提及“just recently been accepted”）。
  - R 包：`dml.sensemakr` ； Python 实现包含在 `doubleml` / `py` 中（两者均存有文档链接）。
- **(b)** 报告明确留下的开放问题（每条扎根转写特定句段，以 [H:MM] 标记）：
  - **扩展到非线性功能的 CEF** [0:44:18]: 如何将 OVB 公式推广至非线性目标参数（如 IV 的 ratio 估计；不是线性功能）。`“we can extend this to nonlinear functions of the CEF and we're working on that right now.”`
  - **锐化二进制/离散治疗与结果的界**[0:59:24]: 当前 OVB 界在边界参数不可达时可能非锐；二进制治疗时如何加入支撑约束得到锐界。`“the bound cannot be sharp... if you take the formula...there are going to be some parameter values not possible...started working on this now to see how we can characterize sharp bounds.”`
  - **形式化整合多元证据校准敏感参数**[0:56:53–0:58:53]: 当边界不具信息时如何结合不同来源（RCT、历史数据、其他研究的“U 解释力”的基准）给出可操作的下一步。`“we still don't have a very formal theory how to combine this in a very systematic way... we can already start doing these things.”`
  - **ρ 参数的先验/校准**[0:53:40]: 如何系统地引导用户设定 ρ，而非默认 1（最 adversarial）。`“we still don't have a good answer for that... but empirically it seems to be much less than one... we should do more.”`

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

