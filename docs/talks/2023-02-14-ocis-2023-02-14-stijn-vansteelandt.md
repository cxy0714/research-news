# Assumption-lean Causal Modeling

**讲者**: Stijn Vansteelandt  
**讨论人**: Elizabeth Ogburn  
**来源**: OCIS (Online Causal Inference Seminar)  
**日期**: 2023-02-14  
**主题**: 因果推断  
**视频**: <https://youtu.be/DkyNCJLWqUg> · [幻灯片](https://drive.google.com/file/d/1ZUmcWx0dNDGtNsEA7bvEuxjZLHKzYz9e/view?usp=share_link)

> 本页据讲座录音的自动转写（ASR）生成。**人名 / 术语 / 公式 / 具体的率与界可能被听错**，关键处请对照视频或讲者论文核对。

---

### 一、这场报告在讲哪条工作线

这场报告位于因果推断中“规定性（prescriptive）因果推断”与“描述性（descriptive）因果推断”的张力之间。

- **规定性因果推断**（van der Laan & Rubin, 2006; Robins et al., 2008; Chernozhukov et al., 2018）的核心是先定义模型无关的因果estimand（如 \(E(Y^1)\)），再在非参模型下用数据自适应方法估计，以实现“卫生的（hygienic）”因果推断——避免模型假设干扰、可做有效后选择/后模型推断。
- **描述性因果推断**则利用统计模型（如边际结构模型、Cox比例风险模型）来概括因果关系，但饱受批评：模型错误时估计量的概率极限复杂且不可解释（Breiman, 2001; Freedman, 2001; Robins & Rotnitzky, 2001）。

这场报告的工作（Vansteelandt & Dukes, *JRSS-B* 2022; Vansteelandt et al., *JASA* 2022）提出**“假设精简（assumption-lean）”因果建模**：保留回归模型的简洁性与沟通便利，但将目标参数关联到一个**模型无关、可解释的估计量**（如加权平均的层特异性效果），使得即使模型错误，也能明确知道在被估计什么；在此基础上利用非参推断（debiased ML）获得有效推断。

当前这一方向的frontier包括：
- 部分线性模型中的率双稳健性（Tchetgen Tchetgen, Robins & Rotnitzky, 2010; Tan, 2019），但需要模型正确；
- 投影估计（Neugebauer & van der Laan, 2007; Buja et al., 2019），但投影本身可能缺乏直接解释；
- 这场报告则尝试在**不要求模型正确**的前提下，保留模型作为沟通工具，同时给出明确可解释的估计量。

---

### 二、最小内核 / 一个最简例子

**符号**（以广义线性模型为例）：
- 可观测数据：\((Y_i, A_i, L_i)\)，i.i.d.，\(i=1,\dots,n\)。
- \(Y\)：二值或连续结局；\(A\)：暴露/处理（可为连续）；\(L\)：可观测混杂（向量）。
- 因果假设：\(L\) 足以调整混杂（条件无混淆性）。
- 感兴趣的因果参数 \(\psi\)：在部分线性模型
  \[
  g\{E(Y|A,L)\} = \psi A + \omega(L)
  \]
  中的系数（例如 \(g=\) logit link 时，\(\psi\) 为 log-OR）。但**我们不假设此模型正确**——它只作为沟通的模板。

**最简例子**（二值 \(A \in \{0,1\}\)，\(g=\) 恒等链接或 log 链接）：

- 若可观测每个层 \(L=l\) 的充足数据，则层内 OLS（或简单对比）给出：
  \[
  \psi(l) = \frac{\mathrm{Cov}(A, g\{E(Y|A,L)\} | L=l)}{\mathrm{Var}(A|L=l)}.
  \]
  当 \(A\) 为二值时：
  \[
  \psi(l) = \log\frac{P(Y=1|A=1, L=l)}{P(Y=1|A=0, L=l)} \quad (\text{log risk ratio}).
  \]

- 为克服稀疏性，取加权平均：
  \[
  \psi = \frac{E[\,w(L)\,\psi(L)\,]}{E[\,w(L)\,]}, \quad w(L) = \mathrm{Var}(A|L).
  \]
  当 \(A\) 二值时，\(w(L)=P(A=1|L)P(A=0|L)\)，即加权重于那些既有治疗又有未治疗者的层。

- 此 \(\psi\) 在模型（部分线性模型）成立时等于原 \(\psi\)；模型错误时，它是层特异 log-RR 的加权平均（权重为条件方差），仍具明确可解释性。

**估计**（非参推断）：利用 efficient influence function 在非参模型下构造的估计量（转写 [0:31:35]–[0:32:12]）：
\[
\frac{\sum_i \{A_i - \hat{E}(A_i|L_i)\} \, \mu(Y_i, A_i, L_i)}{\sum_i \{A_i - \hat{E}(A_i|L_i)\}^2},
\]
其中 \(\mu(Y,A,L)=g'\{E(Y|A,L)\}\{Y-E(Y|A,L)\} + g\{E(Y|A,L)\} - E[g\{E(Y|A,L)\}|L]\)。用样本分裂和机器学习估计 nuisance 函数，可获 \(\sqrt{n}\) 一致渐近正态推断。

---

### 三、报告主体：讲者讲了什么

**[0:01:29–0:03:41] 动机：规定性因果推断的成就与局限**
- 规定性因果方法（目标预定的模型无关估计量）使推断更“卫生”（hygienic），解决了后模型推断困难，但牺牲了模型带来的简洁性与沟通便利。
- 为适应现有方法论，研究者常被迫将问题简化（如二值化连续暴露、提出不现实的“若所有人都吸烟”等问题），或退回模型传统（如边际结构模型、工具变量回归）而导致估计量含义模糊。

**[0:03:43–0:07:49] 第一个动机：让因果推断更易用**
- 许多流行病学研究尚无明确干预目标，规定性方法在此情境下显得做作（如“该做何种位移干预？”）。
- 需要一种在无特定干预时仍能提供因果描述的方法，且不给非统计专家设置过高的专业门槛。

**[0:07:49–0:10:04] 第二个动机：避免模型传统的批评**
- Breiman 的“奥卡姆两难”：简洁可解释 vs 正确建模的冲突；模型错误时偏倚且低估不确定性；后选择推断失效；多重合理模型等。
- 这些批评同样适用于因果模型（边际结构模型、部分线性模型等）。

**[0:10:04–0:13:33] 模型错误时 OLS 极限表达式（警戒性例子）**
- 对二值 \(A\)，OLS 在 \(E(Y|A,L)=\psi A + \beta'L\) 下的极限包含一个非处理效应的偏差项，即使 \(A\perp\!\!\!\perp Y|L\) 时也非零。
- 更一般模型（如 Cox）下，概率极限通常复杂且无法解释为任何“平均”效应。

**[0:14:03–0:18:19] “估计量优先”原则与投影方法的不足**
- 参照 Robins & Greenland (1992) 对于 mediation 的“先定义估计量再识别”的教诲，强调在建模传统中常被遗忘。
- “投影估计”（如将 \(E(Y^a|V)\) 投影到线性模型）虽可提供非参推断，但投影本身缺乏直接因果解释（如最大化期望对数似然），且约束于模型成立时才得到有效推断。

**[0:18:19–0:20:55] Assumption-lean 回归的三步框架**
1. **用模型指定希望达到的简洁程度**（如部分线性模型 \(\log P(Y=1|A,L)=\psi A+\omega(L)\)）——仅作为沟通模板，不假设正确。
2. **指定一个模型无关、当模型正确时降为 \(\psi\) 的估计量**：加权平均的层特异性 log-RR。
3. **对估计量做非参推断**（debiased ML），从而在模型错误时仍有效推断该加权平均。

**[0:20:55–0:25:24] 估计量的具体构造（以 GLM 为例）**
- 层内 OLS 系数 \(\psi(L)=\mathrm{Cov}(A,g\{E(Y|A,L)\}|L)/\mathrm{Var}(A|L)\)，二值 \(A\) 即 log-RR。
- 取加权平均 \(\psi=E[w(L)\psi(L)]/E[w(L)]\)，权重 \(w(L)=\mathrm{Var}(A|L)\)。
- 对连续 \(A\)，若条件方差恒定，则 \(\psi=E[\psi(L)]\)。
- 报告加权后的人群特征（如年龄、性别分布）以明确推断目标人群。

**[0:25:24–0:29:37] Cox 回归的扩展（简略）**
- 从连续分层的 Cox 模型 \(\log \lambda(t|A,L)=\psi A+\omega(t,L)\) 出发，层特异性 log 累积风险比 \(\psi(t,l)\)，取时间均匀加权、层间按 \(\mathrm{Var}(A|L)\) 加权。
- 当前也在研究如何刻画 \(\psi(L)\) 的变异度以捕获异质性。

**[0:29:50–0:35:15] 估计与推断：EIF + 样本分裂**
- 直接 plug-in 有偏，利用 efficient influence function (EIF) 构造 estimating equation。
- 对于 GLM，EIF 导致闭合形式估计量（无需数值优化）。
- 对于 Cox 模型，EIF 涉及累计风险、生存函数、计数过程鞅等 nuisance，但不涉及暴露密度的逆加权。
- 使用样本分裂（cross-fitting）+ nuisance 估计收敛快于 \(n^{1/4}\) 时，方差可由 EIF 的样本方差估计。

**[0:35:20–0:38:58] 仿真结果**
- **仿真 1**：连续暴露，L 为 10 维，暴露模型用 Super Learner，测量变量选择下的偏倚与覆盖。Plug-in 严重有偏，CML/CML-CF（Causal Machine Learning with/without cross-fitting）显著降低偏倚，覆盖接近名义水平。
- **仿真 2**：更复杂的非线性数据生成（转用 Survival Random Forests），样本 \(n=500\)。Plug-in 偏倚极大，CML 覆盖约 94.7%（无交叉拟合），CML-CF 偏倚稍大但覆盖 84%（提示大样本可能更好）。

**[0:39:00–0:43:32] 讨论与特征总结**
- 本方法兼具回归的灵活性（连续暴露）、克服奥卡姆两难（模型仅用于概括，nuisance 用 ML）、避免模型误设偏倚、可做变量选择/ML 后有效推断、可近乎预注册分析、有闭合形式。
- **与部分线性模型的联系**：本方法使部分线性模型估计变得简单（无需解高维估计方程）；但缺失了率双稳健性（rate double robustness）。率双稳健性下的估计器（如 G-estimator）在模型错误时不仅失效，且概率极限不明确。
- 为实现简洁性（least squares projection）牺牲了部分效率；目前正在探求更具效率的 estimand（如对非线性模型有较大效率提升）。

**[0:43:36–1:00:02] 讨论（Betsy Ogburn）与讲者回应**
- Betsy 提出经典的六步规定性因果分析工作流，与报告提出的两步简化工作流对比，指出缺失了对识别假设的透明沟通、对定性异质性的诊断、以及敏感性分析。
- 她建议在估计前检查非单调 A-Y 关系与定性 A-L 交互，若存在则谨慎解释加权平均。
- 她补充了两条评估 estimand 合理性的准则：（1）零假设下估值为 0；（2）方向一致时符号正确；（3）存在定性交互时可解释性存疑。
- 讲者回应：正在探索异质性统计（如 \(\psi(L)\) 的变异度），并同意需整合更多诊断；对临床合作者，通常按模型成立解释，但保障若模型错误仍得“合理”（未必最优）值；理想世界应遵循完整工作流，但实际中希望给出更易用的工具。

---

### 四、对应论文与开放问题

**对应论文（基于幻灯片和转写）**

- Vansteelandt, S., & Dukes, O. (2022). Assumption-lean inference for generalised linear model parameters (with discussion). *Journal of the Royal Statistical Society: Series B*, 84, 657–685.  
  （JRSS-B 讨论论文，对应 GLM 部分）
- Vansteelandt, S., Van Lancker, K., Dukes, O., & Martinussen, T. (2022). Assumption-lean Cox regression. *Journal of the American Statistical Association*.  
  （JASA，对应 Cox 扩展部分）
- Hines, O., Dukes, O., Diaz-Ordaz, K., & Vansteelandt, S. (2021). Demystifying statistical learning based on efficient influence functions. *The American Statistician*, 1–48.  
  （参考文献中提及，科普 EIF 的文章）

**开放问题（每条对应转写中的具体时刻）**

1. **效率改进**：[0:42:12–0:43:05] 报告基于最小二乘投影牺牲了效率；如何构造兼具可解释性、连续暴露灵活性、以及更优效率界的 estimand？尤其是非线性模型中均数靠近 0 时效率提升空间大。

2. **定性异质性的处理**：[0:54:32–0:54:57]（Betsy 讨论）当前 estimand 在存在定性 A-L 交互（效应方向可变）时难以解释。需要发展正规的统计诊断（如 Buja et al. 提出的检验）并整合到工作流中。

3. **异质性刻画**：[0:39:45–0:39:48] 讲者提及仅用均值只是描述的一个方面，如何估计 \(\psi(L)\) 的变异度（方差、分位数等）并提供有效推断？

4. **条件平均处理效果 (CATE) 的 assumption-lean 版本**：[0:28:31–0:29:37]（观众 Shunbo Shi 提问）如何将框架推广到估计 CATE（而非其加权平均）？尤其是连续暴露情形。

5. **敏感性分析扩展**：[0:52:09–0:52:54]（Betsy 建议）对 assumption-lean 估计量发展针对未测混杂的敏感性分析，以及针对 nuisance 收敛速度不足（\(n^{1/4}\) 可能不满足）的诊断（如 Mukherjee & Robins 提出的检验）。

6. **其他因果模型扩展**：[0:38:38–0:38:58] 幻灯片列举了边际结构模型（多个 regime）、中介分析（连续中介）、目标试验、纵向临床试验（不规则测量时间）、工具变量（连续暴露）等场景的 ongoing work。这些具体如何实现？

---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

