# Biostatistics — Vol 23  Issue 1  ·  2026-07-04

- 共 20 篇 · Biostatistics
- 目录核对 ✅ 20 篇全部抓到（对照 OpenAlex 20 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》第23卷第1期的20篇论文，整体上围绕**因果推断与治疗效应评估**、**复杂数据结构的建模与推断**、以及**临床试验设计与假设检验**三条主线展开。因果推断方向集中了多篇针对特殊数据类型的因果估计方法，包括复发事件、半竞争风险、生存数据中的亚组分析，以及利用已有数据评估生物标志物的策略。复杂数据结构建模则涵盖纵向半连续数据、区间删失数据、多水平功能数据、传染病传播的空间模型、以及多块张量数据融合。临床试验设计方面，涉及篮子试验的信息借用、贝叶斯决策理论下的稳健性、以及非劣效性检验的新方法。此外，还有若干应用导向的论文，如肿瘤亚克隆识别、医疗提供者质量评估、睡眠血糖监测等。

在因果推断主线中，最突出的工作是**Causal inference for recurrent event data using pseudo-observations**，它将IPTW、回归调整和双重稳健估计系统性地推广到复发事件数据的边际比较，并提出了基于伪观测的调整后两样本伪得分检验，是因果工具在生存分析中的直接扩展。**A Bayesian nonparametric approach for evaluating the causal effect of treatment in randomized trials with semi-competing risks**则通过主分层框架定义新的因果estimand，并引入贝叶斯非参数和敏感性分析，为处理非终端事件被终端事件删失的复杂设定提供了灵活工具。**Depth importance in precision medicine (DIPM)** 针对右删失生存数据，用树集成方法识别治疗效应异质性亚组，其变量重要性构造思路（基于分裂深度）与CATE估计有直接关联。**Evaluating biomarkers for treatment selection from reproducibility studies**则提出一种高效策略，利用可重复性研究或已有数据中的重复测量来评估新标志物，无需重新进行完整临床试验，对流行病学中的治疗选择评估有实用价值。

在复杂数据建模与假设检验方面，**Assessing the accuracy of predictive models with interval-censored data** 将预测准确性评估（平均预测误差、AUC）扩展到区间删失数据，并提出了IPW和AIPW估计量，处理了评估过程与事件过程的相关性。**Efficient model-based bioequivalence testing** 和 **New approaches for testing non-inferiority for three-arm trials with Poisson distributed outcomes** 分别针对生物等效性和三臂非劣效性试验提出了更高效的检验方法，后者还比较了频率学派与贝叶斯范式的联系。**Multiway generalized canonical correlation analysis** 将正则化广义CCA扩展到张量数据块，其算法层面的贡献（低秩分解、交替最小二乘）与高阶U-统计量计算中的张量收缩有技术关联。

对于因果推断方向的研究者，优先关注**Causal inference for recurrent event data using pseudo-observations**（复发事件因果估计）、**A Bayesian nonparametric approach for evaluating the causal effect of treatment in randomized trials with semi-competing risks**（半竞争风险的主分层+敏感性分析）、**Depth importance in precision medicine**（生存数据中的CATE异质性识别）以及**Evaluating biomarkers for treatment selection from reproducibility studies**（标志物验证的高效策略）。对于半参数效率或高维方向，**Nonparametric targeted Bayesian estimation of class proportions in unlabeled data** 展示了targeted learning与贝叶斯方法的结合，其Bernstein–von Mises定理保证了后验的高效性，值得一看。

## 因果推断  *(causal_inference, 5 篇)*

### 1. [10.1093/biostatistics/kxaa020](https://doi.org/10.1093/biostatistics/kxaa020) — Causal inference for recurrent event data using pseudo-observations
- **作者**: Chien-Lin Su, Robert W Platt, Jean-François Plante
- **期刊/来源**: Biostatistics
- **机构**: Jewish General Hospital · McGill University · HEC Montréal
- **分类**: vol 23 · issue 1 · pp 189-206
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对观察性研究中常见的复发事件数据（如多次住院），目标是在存在混杂因素的情况下比较两组累积率函数（CRF）。作者基于伪观测（pseudo-observations）框架，提出了三类估计量：逆概率加权（IPTW）估计量、回归模型估计量以及双重稳健（doubly robust）估计量。这些估计量被证明具有一致性和渐近正态性，方差估计采用bootstrap方法。此外，还提出了基于伪观测的调整后两样本伪得分检验，用于比较两组CRF。模拟研究评估了有限样本性能，并通过医院再入院数据集展示了方法的应用。该工作将因果推断中的标准工具（IPTW、回归调整、双重稳健）系统性地推广到了复发事件数据的边际比较场景，填补了方法学空白。
- **关键技术**: `pseudo-observations`, `inverse probability of treatment weighting (IPTW)`, `doubly robust estimation`, `cumulative rate function (CRF)`, `bootstrap variance estimation`, `pseudo-score test`
- **为什么对您有用**: 直接连接 primary interest 中的因果推断（纵向数据/复发事件）和估计理论。技术武器库中 'estimation theory in causal inference' 和 'nonparametric statistics' 可直接用于理解其双重稳健估计量的构造和渐近性质。中期可做：将本文的伪观测框架与您 moderately_familiar 的 'HOIF' 结合，推导复发事件设定下的高效影响函数，可能得到更优的收敛速率。

### 2. [10.1093/biostatistics/kxaa018](https://doi.org/10.1093/biostatistics/kxaa018) — Evaluating biomarkers for treatment selection from reproducibility studies
- **作者**: Xiao Song, Kevin K Dobbin
- **期刊/来源**: Biostatistics
- **机构**: University of Georgia
- **分类**: vol 23 · issue 1 · pp 173-188
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究在已有临床试验（使用标准生物标志物）基础上，评估新或更精确的预测性生物标志物用于治疗选择的效果。作者提出一种更高效的策略，无需重新进行完整临床试验，只需进行一项可重复性研究（在新旧标志物上同时测量同一批患者样本），或利用原研究中标准标志物的重复测量数据。该方法基于一个工作模型来评估治疗选择，但所提出的受限平均生存时间估计量在工作模型误设时仍然有效。通过模拟研究和癌症数据应用验证了方法的可行性。该工作为利用已有数据资源进行标志物验证提供了实用工具，对流行病学中的治疗选择评估有直接参考价值。
- **关键技术**: `working model`, `robust estimation`, `restricted mean lifetime`, `reproducibility study`, `predictive biomarker evaluation`
- **为什么对您有用**: 本文属于流行病学应用，直接涉及因果推断中的治疗选择（treatment selection）问题，与您的 secondary interest 流行病学（应用数据集、因果推断）高度匹配。您武器库中 very_familiar 的 estimation theory in causal inference 可直接用于理解其估计量的稳健性论证；但本文方法学 novelty 有限（主要是应用层面的设计），属于中期可做——若想深入改进其估计效率，需先在 moderately_familiar 的 semiparametric theory 上加强。

### 3. [10.1093/biostatistics/kxaa008](https://doi.org/10.1093/biostatistics/kxaa008) · [arXiv](https://arxiv.org/abs/1903.08509) — A Bayesian nonparametric approach for evaluating the causal effect of treatment in randomized trials with semi-competing risks
- **作者**: Yanxun Xu, Daniel Scharfstein, Peter Müller, Michael Daniels
- **期刊/来源**: Biostatistics
- **机构**: Johns Hopkins University · The University of Texas at Austin · University of Florida
- **分类**: vol 23 · issue 1 · pp 34-49
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文在随机试验中处理半竞争风险（非终端事件可被终端事件删失，反之不成立）的因果效应评估问题。基于主分层（principal stratification）框架，定义了一个新的因果 estimand，即治疗对非终端事件的因果效应。引入一组识别假设，并通过一个敏感性参数来刻画假设的偏离程度。采用贝叶斯非参数（BNP）方法进行推断，利用 Dirichlet process 先验对潜在结果分布建模。通过模拟研究和脑癌试验数据验证方法性能，并提供 R 代码实现。对您而言，本文的主分层+敏感性分析思路可直接迁移到您 causal inference 方向中的 mediation 或 longitudinal 设定，且 BNP 框架与您 moderately_familiar 的 identification theory 有交叉。
- **关键技术**: `principal stratification`, `Bayesian nonparametrics`, `Dirichlet process prior`, `sensitivity analysis`, `semi-competing risks`
- **为什么对您有用**: 直接连接到 primary interest 中的 causal inference 子方向（主分层与敏感性分析）。武器库中 very_familiar 的 estimation theory in causal inference 可用来分析其识别假设的强度（如单调性假设是否可检验），而 moderately_familiar 的 identification theory 可用来评估其敏感性参数的可解释性。中期可做：若想将 BNP 替换为 semiparametric 方法（如 DML），需先在 moderately_familiar 的 semiparametric theory 上长肌肉。

### 4. [10.1093/biostatistics/kxaa022](https://doi.org/10.1093/biostatistics/kxaa022) — Nonparametric targeted Bayesian estimation of class proportions in unlabeled data
- **作者**: Iván Díaz, Oleksander Savenkov, Hooman Kamel
- **期刊/来源**: Biostatistics
- **机构**: Cornell University · Weill Cornell Medicine
- **分类**: vol 23 · issue 1 · pp 274-293
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文提出一种新的贝叶斯估计器，用于无标签数据中类别比例（如病例比例）的推断，基于 targeted learning 框架。该方法仅需对目标参数（而非全部模型）指定先验并输出后验，后验分布高度集中。作者证明了 Bernstein–von Mises 型定理，保证后验分布收敛到高效、渐近线性估计量的分布，即后验渐近正态、双重稳健且高效，仅需 nuisance 参数以慢于参数速率估计。数值实验验证了方法的频率性质，并应用于估计隐源性卒中中来自隐匿性心脏或大动脉粥样硬化病灶的比例。该方法具有一般性，可推广至非参数模型中任意路径可微参数。对您而言，本文是 targeted learning 与贝叶斯方法结合的范例，其双重稳健性和效率理论直接关联您的 semiparametric efficiency 和 causal inference 兴趣，且 Bernstein–von Mises 结果对您熟悉的非参数统计理论有参考价值。
- **关键技术**: `targeted learning`, `Bernstein–von Mises theorem`, `doubly robust estimation`, `efficient influence function`, `pathwise differentiability`
- **为什么对您有用**: 本文直接连接您的 primary interest 中的 causal inference（targeted learning 框架）和 efficiency theory（高效、渐近线性估计量）。您的 very_familiar 武器库中的非参数统计和 minimax 界可用于验证其 Bernstein–von Mises 结果的假设条件是否紧；moderately_familiar 的 semiparametric theory 可用于理解其 efficient influence function 的推导。中期可做：若想将贝叶斯 targeted 方法推广至您的 proximal CI 或 IV 设定，需先在 semiparametric theory 上加强（moderately_familiar 项）。

### 5. [10.1093/biostatistics/kxaa021](https://doi.org/10.1093/biostatistics/kxaa021) — Depth importance in precision medicine (DIPM): a tree- and forest-based method for right-censored survival outcomes
- **作者**: Victoria Chen, Heping Zhang
- **期刊/来源**: Biostatistics
- **机构**: Yale University
- **分类**: vol 23 · issue 1 · pp 157-172
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对右删失生存数据，在精准医学框架下提出深度重要性（DIPM）方法，用于识别治疗效应异质性亚组。核心思路是修改传统分类树的节点分裂准则，使其适应于比较两个（或多个）治疗组的生存结局差异。在每个节点处构建随机森林，利用变量在树中被选为分裂变量的深度（越靠近根节点越重要）计算深度变量重要性得分，选出最优分裂变量。该方法不依赖参数模型，可处理高维协变量，并通过模拟和两个真实数据集验证了其相对于现有方法的优势。对您而言，本文提供了一个在生存数据中做因果亚组分析的树集成工具，其变量重要性构造思路（基于分裂深度）可与您熟悉的非参数统计和因果推断中的异质性分析（如CATE估计）结合。
- **关键技术**: `random survival forest`, `variable importance by depth`, `subgroup identification`, `right-censored survival`, `precision medicine`
- **为什么对您有用**: 本文属于因果推断中异质性处理效应（HTE）的树方法，直接连接您的primary interest中的causal inference子方向。技术武器库中very_familiar的nonparametric statistics和estimation theory in causal inference可用来分析其变量重要性得分的统计性质（如一致性、收敛速率），而moderately_familiar的identification theory可评估其亚组识别的因果可解释性。中期可做：若想将分裂深度重要性推广到更一般的因果森林框架，需先在moderately_familiar的semiparametric theory上补强，以处理生存数据中的时变混杂。

## 数理统计 / 假设检验  *(hypothesis_testing, 2 篇)*

### 1. [10.1093/biostatistics/kxaa026](https://doi.org/10.1093/biostatistics/kxaa026) · [arXiv](https://arxiv.org/abs/2002.09316) — Efficient model-based bioequivalence testing
- **作者**: Kathrin Möllenhoff, Florence Loingeville, Julie Bertrand, Thu Thuy Nguyen, Satish Sharan, Liang Zhao et al.
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 1 · pp 314-327
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对生物等效性试验中的经典TOST方法提出了一种更高效的替代检验。在药代动力学数据中，传统做法是先通过非房室分析（NCA）估计AUC和Cmax，再对几何均值比进行双单侧检验（TOST），但NCA在稀疏设计下不可靠。作者采用非线性混合效应模型（NONMEM）进行模型化估计，并构造了一个新的检验统计量，其核心思想是利用模型化估计量的协方差结构构造更灵敏的检验。通过模拟研究，新方法在NCA和模型化两种估计路径下均比TOST有更高的检验功效；对于高变异药物，其I类错误更接近名义水平0.05，表明在传统生物等效性分析不适用的场景下具有潜在应用价值。对您而言，本文属于假设检验在生物医学应用中的具体案例，其检验构造思路（利用估计量的协方差信息替代简单置信区间比较）可迁移到您在高维或因果推断中遇到的类似检验问题。
- **关键技术**: `two one-sided tests (TOST)`, `nonlinear mixed effects models`, `model-based estimation of AUC/Cmax`, `bioequivalence testing`, `simulation-based power comparison`
- **为什么对您有用**: 本文属于假设检验在生物医学应用中的具体案例，连接您的primary interest中的hypothesis testing方向。技术武器库中very_familiar的nonparametric statistics和high-dimensional asymptotics可用于分析其检验统计量的渐近性质（如能否扩展到高维PK参数或非参数模型）。中期可做：若想将类似思路推广到因果推断中的敏感性分析检验，需先在moderately_familiar的semiparametric theory上长肌肉（理解估计量的影响函数协方差结构）。

### 2. [10.1093/biostatistics/kxaa014](https://doi.org/10.1093/biostatistics/kxaa014) — New approaches for testing non-inferiority for three-arm trials with Poisson distributed outcomes
- **作者**: Samiran Ghosh, Erina Paul, Shrabanti Chowdhury, Ram C. Tiwari
- **期刊/来源**: Biostatistics
- **机构**: Wayne State University · Center for Devices and Radiological Health
- **分类**: vol 23 · issue 1 · pp 136-156
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文针对三臂非劣效性试验（安慰剂、阳性对照、试验组）中计数结局（Poisson分布）的假设检验问题，提出了频率学派和贝叶斯学派的新方法。传统两臂非劣效性试验因缺少安慰剂组而依赖强不可验证假设；三臂设计可同时检验阳性对照优于安慰剂以及试验组非劣于阳性对照。频率学派方法基于改进的Wald型检验统计量，利用Poisson均值的渐近正态性构造检验；贝叶斯方法则通过Gamma先验构造后验概率，并利用历史数据（如安慰剂和阳性对照的既往信息）自然整合先验信息。文章还讨论了样本量计算，并揭示了两种范式在非劣效性界值设定上的有趣联系。模拟和实例表明，贝叶斯方法在历史信息充分时具有更高的检验效能。该工作对您可能有用：它属于假设检验在临床试验中的具体应用，与您对数学统计与假设检验的兴趣直接相关，且贝叶斯-频率学派对比的视角可迁移至您熟悉的因果推断中的敏感性分析设定。
- **关键技术**: `Wald-type test`, `Bayesian posterior probability`, `Gamma prior`, `non-inferiority margin`, `sample size calculation`, `three-arm trial design`
- **为什么对您有用**: 本文直接对应您 primary interest 中的 'hypothesis testing' 子方向，且三臂非劣效性试验的统计推断框架与您熟悉的因果推断中的 active-control 设定有结构相似性。您武器库中 'nonparametric statistics' 和 'high-dimensional asymptotics' 的功底可用于评估其检验统计量的有限样本性质（如能否用 Edgeworth 展开改进），但核心方法（Poisson 似然下的参数检验）对您而言是 moderately_familiar 的 M-estimation 范畴，无需额外工具即可理解。中期可做：若想将此类检验推广到更复杂的计数模型（如零膨胀 Poisson 或负二项），需先在 'semiparametric theory' 上长肌肉以处理 nuisance 参数。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1093/biostatistics/kxaa010](https://doi.org/10.1093/biostatistics/kxaa010) — Multiway generalized canonical correlation analysis
- **作者**: Arnaud Gloaguen, Cathy Philippe, Vincent Frouin, Giulia Gennari, Ghislaine Dehaene-Lambertz, Laurent Le Brusquet et al.
- **期刊/来源**: Biostatistics
- **机构**: Centre National de la Recherche Scientifique · Commissariat à l'Énergie Atomique et aux Énergies Alternatives · Université Paris-Saclay · Laboratoire des signaux et systèmes · CentraleSupélec · CEA Paris-Saclay · NeuroSpine Institute · Inserm 等
- **分类**: vol 23 · issue 1 · pp 240-256
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文提出多路广义典型相关分析（MGCCA），将正则化广义典型相关分析（RGCCA）扩展到至少一个数据块具有张量结构的情形。RGCCA 本身是一个通用的多块数据分析框架，涵盖 PCA、PLS 和多种广义 CCA 版本。MGCCA 的核心贡献在于算法层面：它通过将张量块分解为低秩成分，并利用交替最小二乘和正则化策略进行迭代估计，同时证明了算法的收敛性。文中还讨论了高阶成分的计算方法。通过模拟实验和一项婴儿认知脑电图（EEG）研究，展示了 MGCCA 在实际多模态数据分析中的有效性。对您而言，本文的张量分解与多块数据融合思路，与您在高阶 U-统计量计算中使用的张量收缩/einsum 复杂度有直接技术交集，可作为统计计算方向的一个应用案例参考。
- **关键技术**: `regularized generalized canonical correlation analysis (RGCCA)`, `tensor decomposition`, `alternating least squares`, `multi-block data analysis`, `higher-level components`
- **为什么对您有用**: 本文属于统计计算方向，直接连接到您 primary interest 中的 'statistical computing (numerical methods, algorithm)'。其张量块分解与交替最小二乘算法，与您 technical_arsenal 中 'very_familiar' 的 'computation of higher-order U-statistics (treewidth / tensor contraction / einsum)' 有共同的计算结构——都涉及张量收缩的优化与迭代。作为 gateway reading，本文算法清晰、收敛性证明完整，适合作为您进入多块张量数据分析领域的入门读物，值得花时间读全文。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biostatistics/kxaa025](https://doi.org/10.1093/biostatistics/kxaa025) — Joint modeling and multiple comparisons with the best of data from a SMART with survival outcomes
- **作者**: Yan-Cheng Chao, Qui Tran, Alex Tsodikov, Kelley M Kidwell
- **期刊/来源**: Biostatistics
- **机构**: Amgen (United States) · University of Michigan
- **分类**: vol 23 · issue 1 · pp 294-313
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对序贯多分配随机试验（SMART）中生存结局的动态治疗方案（DTR）评估问题，目标是识别出能带来最佳总体生存率的一线治疗、二线治疗（对响应者与非响应者）及其与协变量的交互作用。现有方法多采用逆概率加权进行非参数生存率估计，但无法提供协变量效应或推断信息；而优化DTR的方法又很少处理多重比较问题。作者提出联合建模（joint modeling）框架，同时建模生存过程与纵向协变量，以无偏估计基线/时变协变量效应、治疗效应及其交互。针对特定时间点的多重比较问题，采用“与最优者比较”（multiple comparisons with the best, MCB）方法进行控制。模拟和实际数据分析表明该方法能有效识别最优DTR并给出有效的多重比较推断。对您而言，本文是流行病学中因果推断与序贯治疗策略评估的典型应用，其联合建模+多重比较的框架可迁移至您关注的纵向因果推断与敏感性分析问题。
- **关键技术**: `joint modeling`, `multiple comparisons with the best (MCB)`, `sequential multiple assignment randomized trial (SMART)`, `dynamic treatment regimen (DTR)`, `survival analysis`
- **为什么对您有用**: 本文属于流行病学应用方向，直接对应您的secondary interest。它展示了在SMART设计中如何用联合建模处理生存结局的DTR评估，并系统处理多重比较问题——这一分析模式对您关注的纵向因果推断（如时序治疗策略的ATE估计）有直接参考价值。您的武器库中'identification theory in causal inference'和'nonparametric statistics'足以理解其核心框架，但若要深入改进其估计效率（如引入DML或正交得分），需先在'semiparametric theory'上加强。总体而言，这是一篇值得花时间阅读全文的扎实应用论文。

### 2. [10.1093/biostatistics/kxaa012](https://doi.org/10.1093/biostatistics/kxaa012) — Two-part joint model for a longitudinal semicontinuous marker and a terminal event with application to metastatic colorectal cancer data
- **作者**: Denis Rustand, Laurent Briollais, Christophe Tournigand, Virginie Rondeau
- **期刊/来源**: Biostatistics
- **机构**: Inserm · Bordeaux Population Health · Mount Sinai Hospital · University of Toronto · Lunenfeld-Tanenbaum Research Institute · Centre Hospitalier Universitaire Henri-Mondor
- **分类**: vol 23 · issue 1 · pp 50-68
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对肿瘤临床试验中常见的纵向半连续生物标志物（如肿瘤尺寸，具有零膨胀和右偏特征）与终点事件（死亡）的联合建模问题，提出了一种两部件联合模型。纵向部分采用两部件模型：第一部分用二项分布建模生物标志物是否为零，第二部分用连续分布建模正值部分。生存部分采用比例风险模型，并设计了三种关联结构（当前值、斜率、共享随机效应）连接纵向过程与生存风险。模拟研究表明，若忽略半连续特性而使用单部件联合模型，参数估计会出现偏倚。应用至转移性结直肠癌GERCOR研究数据，发现FOLFOX6/FOLFIRI方案（B组）与更高的肿瘤尺寸相关，且其正向关联导致死亡风险增加。本文方法学贡献在于将两部件模型与联合建模框架结合，为处理零膨胀纵向数据提供了更合理的工具。对您而言，该研究展示了因果推断中纵向数据与生存结局联合建模的实用案例，尤其适合流行病学队列中处理零膨胀生物标志物（如病毒载量、炎症指标）的场景。
- **关键技术**: `joint model`, `two-part model`, `proportional hazards model`, `shared random effects`, `semicontinuous biomarker`
- **为什么对您有用**: 本文属于流行病学应用方向，直接对应您的secondary interest。它展示了如何为纵向半连续数据（零膨胀+右偏）构建联合模型，这在流行病学队列中处理病毒载量、炎症标志物等常见数据时非常实用。您的武器库中'identification theory in causal inference'和'nonparametric statistics'可帮助评估其关联结构的因果解释力，但核心方法（两部件+联合建模）属于经典统计建模，不需要额外工具即可理解。作为入门读物，本文清晰阐述了数据结构和模型假设，适合快速了解该领域实践。

### 3. [10.1093/biostatistics/kxaa017](https://doi.org/10.1093/biostatistics/kxaa017) — Direct modeling of the crude probability of cancer death and the number of life years lost due to cancer without the need of cause of death: a pseudo-observation approach in the relative survival setting
- **作者**: Dimitra-Kleio Kipourou, Maja Pohar Perme, Bernard Rachet, Aurelien Belot
- **期刊/来源**: Biostatistics
- **机构**: London School of Hygiene & Tropical Medicine · University of Ljubljana
- **分类**: vol 23 · issue 1 · pp 101-119
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文在相对生存框架下，针对癌症登记数据中死因信息缺失或不可靠的常见问题，提出用伪观察（pseudo-observation）方法直接建模癌症死亡的粗概率（crude probability of death, CPr）和因癌损失的生命年数（life years lost, LYL），无需依赖死因编码。方法核心是将CPr和LYL视为时间-事件结局的变换，通过伪观察构造个体水平的响应变量，然后拟合广义线性模型（如cloglog、logit链接）进行回归参数估计。模拟研究评估了不同链接函数下的有限样本表现，表明伪观察方法在相对生存设定下对回归系数的估计偏差和覆盖概率均令人满意。应用部分使用英格兰癌症登记数据中的宫颈癌数据展示了方法的实际使用流程，并提供了R语言教程。对您而言，这是一篇应用导向的方法学论文，其伪观察+相对生存的建模思路可迁移至流行病学队列中死因不完整时的因果推断问题，属于secondary interest中流行病学应用的具体案例。
- **关键技术**: `pseudo-observation`, `relative survival`, `crude probability of death`, `life years lost`, `competing risks`, `generalized linear models`
- **为什么对您有用**: 本文属于流行病学应用方向，直接处理癌症登记数据中死因缺失这一实际痛点，方法学上使用伪观察（pseudo-observation）这一您moderately_familiar的M-estimation工具，可视为您从因果推断视角理解竞争风险建模的入门材料。武器库中'nonparametric statistics'和'estimation theory in causal inference'足以理解其估计框架，但若想深入伪观察的渐近理论（如影响函数推导），需先在'semiparametric theory'上长肌肉。本文值得通读全文，尤其是R教程部分可快速复现。

### 4. [10.1093/biostatistics/kxaa009](https://doi.org/10.1093/biostatistics/kxaa009) · [arXiv](https://arxiv.org/abs/1908.06822) — Geographically dependent individual-level models for infectious diseases transmission
- **作者**: M D Mahsin, Rob Deardon, Patrick Brown
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 1 · pp 1-17
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对传染病传播建模中个体级模型（ILM）假设传播概率仅依赖于空间距离而非空间位置本身的局限，提出了一类新的地理依赖个体级模型（GD-ILM）。该模型通过引入条件自回归（CAR）模型来捕捉未观测到的空间结构化协变量或测量误差的影响，从而允许评估空间变化的风险因素（如教育、社会剥夺、环境因素）对传染病传播的作用。模型在贝叶斯框架下使用MCMC方法进行拟合，并在模拟数据和2009年阿尔伯塔省季节性流感暴发数据上验证了可靠性。该方法为制定病因学假设和识别异常高风险地理区域提供了灵活工具。对您而言，这是一篇流行病学应用论文，展示了空间随机效应与个体级传播模型的结合，其CAR建模思路和贝叶斯推断框架可作为您处理空间结构数据时的参考，但方法学新颖性有限。
- **关键技术**: `individual-level models (ILMs)`, `conditional autoregressive (CAR) model`, `Bayesian MCMC`, `spatio-temporal modeling`, `geographically dependent risk factors`
- **为什么对您有用**: 本文属于流行病学应用方向，展示了空间随机效应在传染病传播模型中的整合方式。您的武器库中非参数统计和M估计理论可用于分析其CAR模型的平滑性假设是否合理，但核心机器（空间统计、MCMC诊断）不在非常熟悉或中等熟悉列表中，属于暂不可做方向——需先补充空间统计或贝叶斯计算工具。本文作为流行病学入门读物尚可，但方法学贡献一般，不值得花时间全文精读。

## 其他  *(other, 8 篇)*

### 1. [10.1093/biostatistics/kxaa019](https://doi.org/10.1093/biostatistics/kxaa019) · [arXiv](https://arxiv.org/abs/1908.05091) — Borrowing of information across patient subgroups in a basket trial based on distributional discrepancy
- **作者**: Haiyan Zheng, James M S Wason
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 1 · pp 120-135
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对篮子试验（basket trial）中跨患者亚组的信息借用问题，提出了一种稳健的贝叶斯方法。研究设定为随机、安慰剂对照的篮子试验，结局为连续型变量，目标是在协变量调整后，从治疗效应相似的亚组间借用信息。核心机制是通过分布差异（distributional discrepancy）刻画亚组间的可公度性，并在先验精度因子上放置 spike-and-slab 先验，实现选择性信息借用。当篮子试验包含至少三个亚组时，将逐对可公度性度量转化为权重，组合成边际预测先验，仅借用最匹配亚组的信息。该方法在慢性病真实篮子试验的模拟中表现出优于其他贝叶斯模型的性能，能更准确地识别最可公度的信息源并控制借用程度。数值结果表明，该方法可提高估计精度并潜在地提升假设检验的统计功效。
- **关键技术**: `spike-and-slab prior`, `commensurate prior`, `distributional discrepancy`, `Bayesian borrowing`, `marginal predictive prior`
- **为什么对您有用**: 本文属于应用贝叶斯方法，与您的主要兴趣（因果推断、高维统计等）无直接技术重叠，但可作为流行病学或临床试验中信息借用方法的入门读物。武器库中的非参数统计和 M-估计理论可用于分析其先验选择对后验收缩的影响，但核心的贝叶斯建模框架与您的技术栈距离较远，属于暂不可做方向。

### 2. [10.1093/biostatistics/kxaa016](https://doi.org/10.1093/biostatistics/kxaa016) — Matrix decomposition for modeling lesion development processes in multiple sclerosis
- **作者**: Menghan Hu, Ciprian Crainiceanu, Matthew K Schindler, Blake Dewey, Daniel S Reich, Russell T Shinohara et al.
- **期刊/来源**: Biostatistics
- **机构**: Brown University · Johns Hopkins University · National Institutes of Health · National Institute of Neurological Disorders and Stroke · University of Pennsylvania
- **分类**: vol 23 · issue 1 · pp 83-100
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究多发性硬化症（MS）病灶在纵向多序列结构磁共振成像（sMRI）中的演化过程。目标是通过功能数据模型捕捉每个体素在多序列上的强度轨迹的时空动态。为处理嵌套数据结构（观测嵌套于体素、体素嵌套于病灶、病灶嵌套于受试者），采用结构化功能主成分分析（SFPCA）进行建模。进一步提出假设检验方法，评估治疗干预对病灶演化的影响，并控制多水平结构。通过该检验策略，发现治疗组间病灶演化存在显著差异。本文方法学贡献在于将功能数据分析与多水平结构结合，用于医学影像中的纵向过程建模。对您而言，这是一篇应用导向的论文，涉及纵向数据与假设检验，但方法学新颖性有限，且与您的主要兴趣方向（因果推断、高维统计等）直接关联较弱。
- **关键技术**: `structured functional principal component analysis`, `multilevel functional data analysis`, `hypothesis testing for longitudinal data`
- **为什么对您有用**: 本文涉及纵向数据建模与假设检验，与您的primary interest中'因果推断（纵向）'和'假设检验'有表面关联，但方法学核心是功能数据分析而非因果识别或高维统计。您的武器库中'非参数统计'和'M估计理论'可理解其SFPCA框架，但本文未涉及您擅长的minimax界或U统计量。作为应用论文，它展示了医学影像中多水平结构的数据分析流程，但方法学深度不足以支撑直接迁移。暂不可做——核心机器（功能数据分析的特定工具）不在您的武器库中，且问题本身不直接对应您的主要兴趣。

### 3. [10.1093/biostatistics/kxaa011](https://doi.org/10.1093/biostatistics/kxaa011) — Assessing the accuracy of predictive models with interval-censored data
- **作者**: Ying Wu, Richard J Cook
- **期刊/来源**: Biostatistics
- **机构**: Nankai University · University of Waterloo
- **分类**: vol 23 · issue 1 · pp 18-33
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对区间删失验证数据下事件时间预测模型的准确性评估问题，开发了三种估计量：基于插补的估计量、逆概率加权（IPW）估计量以及增强型逆概率加权（AIPW）估计量。目标是在一个标志性时间点预测事件状态，评估指标包括平均预测误差和受试者工作特征曲线下面积。IPW和AIPW估计量的权重通过拟合一个多状态模型获得，该模型联合考虑了事件过程、重复评估过程和失访过程。通过模拟研究实证比较了所提方法的性能，并在银屑病关节炎的类风湿学研究中进行了应用，其中人类白细胞抗原标记用于预测疾病进展状态。本文主要贡献在于将预测准确性评估方法扩展到区间删失数据这一常见但复杂的设定，并提供了处理评估过程与事件过程相关性的加权策略。对您而言，本文属于应用导向的方法学工作，与您的主要兴趣（因果推断、半参理论）关联较弱，但其中处理缺失数据和删失数据的加权思路（IPW/AIPW）在纵向因果推断中可能有参考价值。
- **关键技术**: `inverse probability weighting`, `augmented inverse probability weighting`, `multiple imputation`, `multistate model`, `interval-censored data`, `predictive accuracy`
- **为什么对您有用**: 本文属于生物统计应用领域的方法学工作，与您的主要兴趣（因果推断、半参理论）关联较弱。加权估计（IPW/AIPW）的思路在纵向因果推断中处理缺失数据时可能有借鉴意义，但核心问题（预测准确性评估而非因果效应估计）和方法工具（多状态模型而非因果推断框架）与您的武器库重叠有限。作为流行病学应用方向的gateway阅读，本文方法学新颖性一般（novelty_flag: application），不值得花费大量时间深入阅读。

### 4. [10.1093/biostatistics/kxaa015](https://doi.org/10.1093/biostatistics/kxaa015) — Estimating diversity in networked ecological communities
- **作者**: Amy D Willis, Bryan D Martin
- **期刊/来源**: Biostatistics
- **机构**: University of Washington
- **分类**: vol 23 · issue 1 · pp 207-222
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对生态群落多样性指数估计中忽视物种共现网络（co-occurrence networks）的问题，提出利用成分数据模型（compositional data models）来显式建模物种间的正负共现关系，从而改进多样性指数的估计。传统方法基于多项分布假设，无法处理物种间的网络结构，导致估计偏差。作者将Shannon、Simpson、Bray-Curtis和Euclidean等常用多样性指数嵌入成分数据模型框架，并与多项分布、低秩及非参数方法进行模拟比较。模拟结果表明，在物种网络强关联且物种数多的群落中，所提方法增益最大。最后，文章分析了包含1425个分类单元和12个群落的深海玄武岩微生物组16S扩增子测序数据，展示了方法的实际应用。本文主要贡献在于将成分数据模型引入多样性估计，但方法学创新程度有限，属于应用导向的方法适配。
- **关键技术**: `compositional data models`, `co-occurrence networks`, `diversity indices estimation`, `multinomial model comparison`
- **为什么对您有用**: 本文属于流行病学/微生物组数据分析的应用工作，与您的secondary interest（流行病学数据集和因果推断应用）有间接关联。但方法学上未涉及因果推断、高维统计或效率理论等核心兴趣，且技术工具（成分数据模型）不在您的武器库中。作为入门读物，本文对微生物组数据中网络结构的建模思路有一定参考价值，但无需深入精读。

### 5. [10.1093/biostatistics/kxaa013](https://doi.org/10.1093/biostatistics/kxaa013) — A hidden Markov modeling approach for identifying tumor subclones in next-generation sequencing studies
- **作者**: Hyoyoung Choo-Wosoba, Paul S Albert, Bin Zhu
- **期刊/来源**: Biostatistics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 23 · issue 1 · pp 69-82
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对下一代测序数据中的肿瘤亚克隆识别问题，提出了一种基于隐马尔可夫模型（HMM）的方法 subHMM。研究目标是同时估计肿瘤样本中亚克隆的区域、区域特异性亚克隆基因型以及克隆比例。模型将克隆基因型和亚克隆状态合并为一个隐状态变量，采用两步估计算法：第一步用标准 HMM 拟合合并状态变量（通过 EM 算法和前向-后向算法），第二步通过最大化区域特异性伪似然来估计克隆比例。该方法突破了现有工具只能识别亚克隆区域、无法推断基因型的局限。模拟实验和 TCGA 肾癌数据集的应用展示了良好的性能。R 源代码已公开。本文属于生物信息学应用，方法学贡献在于将 HMM 框架扩展到亚克隆基因型推断，但未涉及因果推断、高维统计或效率理论等核心兴趣方向。
- **关键技术**: `Hidden Markov Model`, `Expectation-Maximization algorithm`, `Forward-backward algorithm`, `Pseudo-likelihood estimation`, `Allele-specific copy number alteration`
- **为什么对您有用**: 本文属于生物信息学/癌症基因组学应用，与主要兴趣（因果推断、高维统计、U-统计量等）无直接关联。作为流行病学方向的次级兴趣，本文展示了 HMM 在肿瘤异质性分析中的应用，但方法学新颖性有限（主要是现有 HMM 框架的扩展）。武器库中无直接可攻工具（缺 HMM 专门经验），暂不可做。

### 6. [10.1093/biostatistics/kxaa027](https://doi.org/10.1093/biostatistics/kxaa027) — A decision-theoretic approach to Bayesian clinical trial design and evaluation of robustness to prior-data conflict
- **作者**: Silvia Calderazzo, Manuel Wiesenfarth, Annette Kopp-Schneider
- **期刊/来源**: Biostatistics
- **机构**: German Cancer Research Center · Heidelberg University
- **分类**: vol 23 · issue 1 · pp 328-344
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文从贝叶斯决策理论的角度，系统探讨了在临床试验设计中如何平衡历史信息的有效利用与对先验-数据冲突的稳健性。核心设定是：在贝叶斯框架下，先验分布可引入外部信息，但若先验与当前数据不一致，会损害试验的频率学操作特性（如I类错误率）。作者定义了一个综合风险函数，整合了来自假设检验、参数估计和抽样的损失，并通过加权组合在检验与估计目标之间平滑过渡。方法上，区分了数据生成过程的先验与分析先验，并考察了基于后验概率或贝叶斯因子的不同检验决策规则。通过正态和二项结局的模拟以及一项单臂概念验证试验的应用，展示了先验-数据冲突对综合风险、操作特性和最优样本量的影响，并比较了逐步折扣冲突先验信息的稳健分析先验设定。本文为贝叶斯临床试验设计中的成本设定和稳健性评估提供了实用指导。
- **关键技术**: `Bayesian decision theory`, `integrated risk`, `prior-data conflict`, `operating characteristics`, `robust prior specification`, `Bayes factor`
- **为什么对您有用**: 本文属于临床试验设计的方法学工作，与您的主要兴趣（因果推断、高维统计等）无直接重叠。但作为一篇应用导向的贝叶斯方法论文，其决策理论框架（综合风险、先验折扣）对您理解贝叶斯稳健性有参考价值。武器库中'非参数统计'和'估计理论'可帮助理解其风险函数的构造，但核心贝叶斯决策机制不在您当前工具链中，属于暂不可做方向。

### 7. [10.1093/biostatistics/kxaa024](https://doi.org/10.1093/biostatistics/kxaa024) · [arXiv](https://arxiv.org/abs/1907.07809) — Accounting for total variation and robustness in profiling health care providers
- **作者**: Lu Xia, Kevin He, Yanming Li, John Kalbfleisch
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 1 · pp 257-273
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对医疗提供者（如透析机构）质量评估中的 profiling 问题，提出一种平滑经验零分布方法，以更公平地识别表现异常（优于或劣于预期）的机构。传统随机或固定效应模型未能充分纳入机构间因未观测患者特征差异导致的变异，可能造成不公平评估。该方法通过估计总变异并自适应不同机构规模，构造一个经验零分布作为基准，从而控制假阳性。在线性模型框架下推导了理论性质，并推广至生存或二元结局等非线性模型。模拟和实际透析设施生存数据表明，该方法在保持稳健性的同时改善了机构排名的准确性。对您而言，本文虽非因果推断或高维统计核心方向，但其 profiling 框架与医疗质量评估中的 provider profiling 问题直接相关，可作为流行病学应用案例参考。
- **关键技术**: `smoothed empirical null`, `random effects model`, `provider profiling`, `total variation accounting`, `robustness to unobserved heterogeneity`
- **为什么对您有用**: 本文属于流行病学应用（secondary interest），处理的是医疗质量评估中 provider profiling 的统计方法，与您对流行病学数据集的兴趣一致。但方法学上较为常规（经验零分布 + 随机效应），未涉及您武器库中的核心工具（如高维统计、U-statistics、semiparametric efficiency），且无 computational tradeoff 或新理论贡献。可作为入门级应用文献阅读，但无需深入跟进。

### 8. [10.1093/biostatistics/kxaa023](https://doi.org/10.1093/biostatistics/kxaa023) — Modeling continuous glucose monitoring (CGM) data during sleep
- **作者**: Irina Gaynanova, Naresh Punjabi, Ciprian Crainiceanu
- **期刊/来源**: Biostatistics
- **机构**: Texas A&M University · Johns Hopkins University · Johns Hopkins Medicine
- **分类**: vol 23 · issue 1 · pp 223-239
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对 2 型糖尿病患者睡眠期间的连续血糖监测（CGM）数据，提出了一种多水平函数 Beta 模型。该模型将血糖水平视为从活动记录仪估计的入睡时间起算的函数，通过 Beta 分布刻画血糖值的边界（0-1 标准化后）和异方差性。模型包含受试者内和受试者间的随机效应，能够估计受试者特定的边际分位数，并量化血糖动态的个体间变异。参数估计采用似然方法，并通过模拟验证了模型的有效性。实证部分展示了模型参数与糖化血红蛋白（HbA1c）的关联，说明该模型在糖尿病管理中的潜在应用价值。本文属于应用统计方法在生物医学领域的实证研究，方法学创新有限，但数据结构和建模思路（多水平函数数据）对处理纵向、高频率生理信号有参考意义。
- **关键技术**: `multilevel functional data analysis`, `Beta regression`, `quantile estimation`, `continuous glucose monitoring`
- **为什么对您有用**: 本文属于流行病学领域的应用研究，使用了多水平函数数据模型处理高频率纵向血糖数据。研究者若对纵向因果推断或高维函数数据建模感兴趣，可从中了解 CGM 数据结构和分析挑战，但方法学工具（如 Beta 回归、随机效应）不在当前技术武库的核心范围内，属于暂不可做的方向。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

