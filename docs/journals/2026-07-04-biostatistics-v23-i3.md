# Biostatistics — Vol 23  Issue 3  ·  2026-07-04

- 共 20 篇 · Biostatistics
- 目录核对 ✅ 20 篇全部抓到（对照 OpenAlex 20 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Biostatistics》第23卷第3期的20篇论文，整体上围绕**因果推断与效应运输**、**假设检验与多重比较**、**高维/图结构数据建模**以及**临床试验设计与校准**四条主线展开。因果推断方向聚焦于效应运输的扩展，假设检验方向关注图结构先验与校准诊断，高维建模方向涉及图模型、矩阵数据和聚类，临床试验方向则涵盖剂量探索、自适应设计和等价性检验。

在因果推断主线中，**Efficiently transporting causal direct and indirect effects** 一文突破了现有运输中介方法仅处理单个二元中介变量的限制，提出基于有效影响函数的非参数估计量，具有多重稳健性和半参数有效性，并允许中间混杂和多个高维中介变量，是本期因果推断方向的核心方法贡献。**Semiparametric regression on cumulative incidence function** 针对区间删失竞争风险数据中事件类型缺失问题，提出增广逆概率加权筛极大似然估计，双重稳健地估计累积发生率函数，并给出了影响函数形式，适用于缺失比例高的实际场景。**Treed distributed lag nonlinear models** 则从纵向因果推断的应用角度，用贝叶斯加性回归树替代传统样条，自适应捕捉暴露-时间-响应曲面的非光滑结构，在识别关键时间窗口上具有优势。

假设检验主线中，**Dimension constraints improve hypothesis testing** 提出图拉普拉斯正则化的经验贝叶斯混合模型（GraphMM）来估计局部错误发现率，在控制FDR的同时提升检测功效，尤其适用于脑影像等图结构数据。**Testing for similarity of binary efficacy–toxicity responses** 将等价性检验扩展到协变量依赖的二元结局，并首次处理相关二元联合终点，采用参数自助法逼近零分布。**Testing calibration of phenotyping models** 针对EHR数据中表型模型校准检验，仅需阳性样本和未标记数据，构造了基于风险子组病例数差异的卡方统计量，并给出了校准斜率和区分度指标的一致估计。此外，**An optimal kernel-based multivariate U-statistic** 提出基于核的多元U统计量（KMU），用于多表型关联检验，具有数据驱动的核选择和渐近理论，直接连接U统计量的理论兴趣。

其他主线中，高维图模型方向有**Information enhanced model selection** 将先验结构信息融入BIC，提出sBIC并证明模型选择一致性；**Simultaneous differential network analysis** 在Kronecker积协方差框架下同时进行差异网络分析与分类。临床试验方向包括**A benchmark for dose-finding studies** 推广非参数基准到剂量-毒性顺序未知场景，**Bayesian adaptive design** 提出基于相关混合先验的平行试验信息借用设计。流行病学应用方向有**A spatiotemporal recommendation engine** 结合层次贝叶斯时空模型与策略搜索优化疟疾资源分配，**Assessing risk model calibration** 用调查校准方法处理缺失协变量下的校准评估，**Estimation of the generation interval** 用EM算法从监测数据推断代际间隔。

对于因果推断方向的研究者，优先看 **Efficiently transporting causal direct and indirect effects**（效应运输与中介分析）、**Semiparametric regression on cumulative incidence function**（竞争风险与缺失数据）、**Treed distributed lag nonlinear models**（纵向暴露-响应识别）。对于半参数效率方向，**Efficiently transporting causal direct and indirect effects** 的有效影响函数构造和多重稳健性值得关注。对于高维假设检验方向，**Dimension constraints improve hypothesis testing** 的图正则化经验贝叶斯框架和 **An optimal kernel-based multivariate U-statistic** 的U统计量渐近理论是重点。

## 因果推断  *(causal_inference, 3 篇)*

### 1. [10.1093/biostatistics/kxaa057](https://doi.org/10.1093/biostatistics/kxaa057) — Efficiently transporting causal direct and indirect effects to new populations under intermediate confounding and with multiple mediators
- **作者**: Kara E Rudolph, Iván Díaz
- **期刊/来源**: Biostatistics
- **机构**: Cornell University · Weill Cornell Medicine · Columbia University
- **分类**: vol 23 · issue 3 · pp 789-806
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在因果中介分析框架下，研究如何将源人群中的直接和间接效应（interventional (in)direct effects）运输（transport）到新目标人群，允许存在中间混杂（intermediate confounding）和多个高维中介变量。现有运输中介方法仅能处理单个二元中介变量，本文突破了这一限制。作者提出非参数估计量，基于 efficient influence function 构造，具有 multiply robust 性质（即只要部分模型正确即可一致估计），且是渐近正态和半参数有效的。估计量可结合数据自适应（data-adaptive）的 nuisance 参数估计（如机器学习），并通过 cross-fitting 控制过拟合偏差。理论部分给出了影响函数、渐近方差和收敛速率。模拟和实证研究（如 HIV 治疗效应在不同人群间的差异分解）验证了方法的有限样本表现。对您而言，本文直接连接 causal inference 中的 mediation 和 transportability 子方向，且其 multiply robust 和 efficient 估计框架可迁移至您熟悉的 proximal CI 或 longitudinal 设定。
- **关键技术**: `efficient influence function`, `multiply robust estimation`, `cross-fitting`, `interventional (in)direct effects`, `transportability`, `data-adaptive nuisance estimation`
- **为什么对您有用**: 本文直接对应 primary interest 中的 causal inference（mediation, transportability）和 efficiency theory（semiparametric efficiency bound）。您武器库中 very_familiar 的 nonparametric statistics 和 estimation theory in causal inference 可直接用于理解其影响函数推导和 multiply robust 性质；moderately_familiar 的 semiparametric theory 和 identification theory 可进一步评估其假设（如 positivity, no unmeasured confounding）在您关注的 proximal CI 设定下的可放松性。**中期可做**：若想将本文的 transport 框架与 proximal CI 的 negative control 假设结合，需先在 moderately_familiar 的 identification theory 上深入（特别是 proximal g-formula 的识别条件）。

### 2. [10.1093/biostatistics/kxaa052](https://doi.org/10.1093/biostatistics/kxaa052) — Semiparametric regression on cumulative incidence function with interval-censored competing risks data and missing event types
- **作者**: Jun Park, Giorgos Bakoyannis, Ying Zhang, Constantin T Yiannoutsos
- **期刊/来源**: Biostatistics
- **机构**: Merck & Co., Inc., Rahway, NJ, USA (United States) · Indiana University – Purdue University Indianapolis · University of Nebraska Medical Center
- **分类**: vol 23 · issue 3 · pp 738-753
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对区间删失竞争风险数据中事件类型缺失的问题，提出了一种增广逆概率加权筛极大似然估计（AIPW sieve MLE）。目标估计量为累积发生率函数（CIF），在竞争风险框架下，事件时间仅知落在两次检查之间，且部分个体的事件类型（如死因）缺失。方法核心是构造一个双重稳健的估计方程：通过逆概率加权处理缺失机制，同时利用辅助变量放宽缺失随机（MAR）假设；筛基函数（如B样条）用于非参数建模基线风险。理论部分证明了估计量的相合性和渐近正态性，并给出了影响函数形式。模拟表明，即使缺失比例高达50%，方法仍保持低偏倚和良好覆盖。应用实例来自撒哈拉以南非洲的HIV队列研究，其中大量死亡原因缺失。对您而言，本文的双重稳健框架和缺失数据处理思路可直接迁移至您关注的纵向因果推断和流行病学应用场景。
- **关键技术**: `augmented inverse probability weighting`, `sieve maximum likelihood`, `doubly robust estimation`, `interval-censored competing risks`, `missing event types`
- **为什么对您有用**: 本文直接关联您的流行病学应用兴趣和因果推断中的缺失数据处理。技术层面，您非常熟悉的非参数统计和M估计理论可用于分析其筛估计的收敛速度，而您中等熟悉的半参数理论可帮助评估其双重稳健性的效率损失。中期可做：将AIPW框架与您关注的proximal causal inference结合，处理更复杂的未测量混杂下的缺失数据问题，这需要先在identification theory上进一步积累。

### 3. [10.1093/biostatistics/kxaa051](https://doi.org/10.1093/biostatistics/kxaa051) · [arXiv](https://arxiv.org/abs/2010.06147) — Treed distributed lag nonlinear models
- **作者**: Daniel Mork, Ander Wilson
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 754-771
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文针对空气污染暴露与儿童健康结局的纵向研究，提出基于贝叶斯加性回归树（BART）的分布式滞后非线性模型（DLNM）。传统DLNM使用双变量基展开（如样条）参数化暴露-时间-响应曲面，假设整个曲面光滑，这在暴露仅在特定时间窗口与结局相关时可能不现实。新方法用一组回归树在暴露-时间空间上假设分段常数关系，从而自适应地捕捉非光滑结构。模拟表明，当真实曲面不光滑时，树模型优于样条模型；在光滑设定下两者表现相近。关键优势是方差更低，能更精确地识别暴露与健康结局相关的关键时间窗口。该方法在科罗拉多出生队列中估计了PM2.5暴露与出生体重的关联。对您而言，该工作属于流行病学纵向因果推断的应用，其识别关键窗口的思路可迁移到您感兴趣的mediation或longitudinal causal inference中的时间效应估计问题。
- **关键技术**: `Bayesian additive regression trees (BART)`, `distributed lag nonlinear model (DLNM)`, `exposure-time-response surface`, `piecewise constant approximation`, `critical window identification`
- **为什么对您有用**: (1) 直接连接到您的secondary interest——流行病学队列研究的因果推断应用，具体是纵向暴露-结局关联中的时间窗口识别问题。(2) 您的very_familiar武器库中的非参数统计和因果推断估计理论可用于分析该方法的估计性质（如分段常数近似的minimax rate），而moderately_familiar的identification theory可用于形式化“关键窗口”的因果定义。(3) 中期可做：若想将该方法推广到proximal causal inference或mediation设定，需先在moderately_familiar的identification theory上长肌肉（如时间-varying confounding下的identification条件）。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1093/biostatistics/kxaa058](https://doi.org/10.1093/biostatistics/kxaa058) — Testing for similarity of binary efficacy–toxicity responses
- **作者**: Kathrin Möllenhoff, Holger Dette, Frank Bretz
- **期刊/来源**: Biostatistics
- **机构**: Eindhoven University of Technology · Ruhr University Bochum · Novartis (Switzerland)
- **分类**: vol 23 · issue 3 · pp 949-966
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文针对临床试验中两组患者（如不同地理区域或年龄层）在协变量（如剂量）范围内的疗效与毒性二元结局的相似性检验问题。目标是在整个协变量范围内，两组平均结局差异始终低于预设界值（即等价性检验）。方法上，首先针对单一二元终点，基于两组响应曲线最大偏差的估计量构造检验统计量，并采用参数自助法（parametric bootstrap）逼近其零分布。进一步，利用二维Gumbel-type copula模型处理相关二元疗效-毒性结局的联合相似性检验。模拟研究评估了有限样本下的检验水平与功效，并通过案例研究展示实际应用。该工作将经典的等价性检验框架扩展到协变量依赖的二元结局，并首次处理了相关二元联合终点。对您而言，其参数自助法与最大偏差估计的结合是假设检验中处理复杂零分布的有用技术，且与您在高维统计和假设检验方面的兴趣直接相关。
- **关键技术**: `equivalence testing`, `parametric bootstrap`, `maximum deviation`, `Gumbel copula`, `binary endpoints`
- **为什么对您有用**: 直接连接到您对假设检验的兴趣，特别是协变量依赖的等价性检验这一具体子方向。武器库中'非参数统计'和'高维渐近理论'可用于分析其最大偏差估计量的渐近分布，而'M估计理论'可为其参数自助法的有效性提供理论支撑。中期可做：若想将方法推广到高维协变量或更复杂的结局类型，需先在'半参数理论'上加强，以处理更灵活的模型设定。

### 2. [10.1093/biostatistics/kxab003](https://doi.org/10.1093/biostatistics/kxab003) — Testing calibration of phenotyping models using positive-only electronic health record data
- **作者**: Lingjiao Zhang, Yanyuan Ma, Daniel Herman, Jinbo Chen
- **期刊/来源**: Biostatistics
- **机构**: University of Pennsylvania · Pennsylvania State University
- **分类**: vol 23 · issue 3 · pp 844-859
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 本文针对电子健康记录（EHR）数据中表型模型的校准检验问题，提出了一种仅需阳性（gold-standard cases）和未标记样本、无需阴性对照的方法。核心设定是：标记病例代表所有病例（代表性假设），未标记人群包含病例和对照。对于校准检验，作者构造了一个聚合各风险子组中模型自由估计与模型基估计的病例数差异的统计量，该统计量渐近服从卡方分布。此外，还提出了校准斜率的估计方法以及区分度指标的一致估计，并推导了其大样本性质。方法通过大量模拟验证，并应用于宾夕法尼亚大学医学中心的EHR数据，验证了两个原发性醛固酮增多症风险预测模型的校准性能。该工作属于假设检验与模型诊断的交叉，其统计量构造思路（基于分组聚合差异）与您熟悉的非参数统计和M估计理论有直接关联。
- **关键技术**: `Chi-squared goodness-of-fit test`, `calibration slope estimation`, `positive-unlabeled learning`, `model-free vs model-based estimation`, `large sample theory`
- **为什么对您有用**: 本文直接关联您的primary interest中的假设检验与因果推断（模型校准是预测模型验证的核心，也是因果推断中倾向性评分校准的常见步骤）。技术层面，其统计量构造（分组聚合差异）可用您非常熟悉的非参数统计和M估计理论来理解与扩展；中期可做：若想将方法推广至更复杂的缺失机制或因果框架，需先在moderately_familiar的identification theory上加强。总体而言，这是一篇方法学扎实的应用导向论文，值得一读。

### 3. [10.1093/biostatistics/kxab001](https://doi.org/10.1093/biostatistics/kxab001) · [arXiv](https://arxiv.org/abs/1908.07176) — Dimension constraints improve hypothesis testing for large-scale, graph-associated, brain-image data
- **作者**: Tien Vo, Akshay Mishra, Vamsi Ithapu, Vikas Singh, Michael A Newton
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 860-874
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文针对图结构关联的大规模假设检验问题，提出了一种经验贝叶斯混合模型（GraphMM）来估计局部错误发现率（local FDR）。核心设定是每个测试单元（如脑区体素）对应图的一个节点，非零效应倾向于形成连通子图。方法通过引入图拉普拉斯正则化来收缩相邻单元的参数差异，从而在保持FDR控制的前提下提升检测功效。模拟表明GraphMM在多种图结构下控制FDR，但过度正则化可能导致失控。在阿尔茨海默病脑影像数据上，GraphMM比传统大规模检验方法（如BH过程）发现了更多有意义的激活区域。该工作将图结构先验融入经验贝叶斯框架，对您的高维假设检验兴趣有直接参考价值，尤其是图正则化与多重比较的结合思路。
- **关键技术**: `empirical Bayes mixture model`, `local false discovery rate`, `graph Laplacian regularization`, `large-scale hypothesis testing`, `FDR control`
- **为什么对您有用**: 直接连接到您的高维假设检验兴趣，特别是图结构数据下的多重比较问题。您的武器库中'非参数统计'和'高维渐近理论'可用于分析GraphMM的FDR控制边界和正则化参数选择，属于'立即可做'的follow-up。

## 流行病学  *(epidemiology, 4 篇)*

### 1. [10.1093/biostatistics/kxab010](https://doi.org/10.1093/biostatistics/kxab010) · [arXiv](https://arxiv.org/abs/2003.05084) — A spatiotemporal recommendation engine for malaria control
- **作者**: Qian Guan, Brian J Reich, Eric B Laber
- **期刊/来源**: Biostatistics
- **机构**: North Carolina State University
- **分类**: vol 23 · issue 3 · pp 1023-1038
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对疟疾控制中的资源分配问题，提出一个时空推荐引擎框架。目标是在连续资源分配域上，将分配策略形式化为从当前疾病信息到资源量的映射序列，并寻找最优策略以最大化长期累积效果。方法结合了层次贝叶斯时空模型（用于建模疾病传播动态）与策略搜索算法（policy-search），在预设的可解释策略类内估计最优分配策略。策略类设计兼顾可解释性与公平性约束，适合实际政策制定场景。模拟实验和刚果民主共和国的真实疟疾干预数据均显示，该框架优于朴素基线方法。对您而言，这是一篇流行病学领域的应用论文，其策略搜索与时空建模的结合思路，以及真实数据驱动的政策优化框架，可作为您了解流行病学中因果推断与决策优化应用的入门读物。
- **关键技术**: `hierarchical Bayesian spatiotemporal model`, `policy-search algorithm`, `resource allocation policy`, `interpretable policy class`
- **为什么对您有用**: 本文属于流行病学应用，可作为 gateway reading：它清晰展示了如何将统计模型（时空贝叶斯模型）与决策优化（策略搜索）结合，用于真实公共卫生问题。您的武器库中非参数统计和因果推断的估计理论可帮助理解其策略估计的统计性质，但核心的贝叶斯时空建模和策略搜索算法并非您熟悉的方向，因此属于暂不可做——需要补充贝叶斯时空模型和强化学习中的策略梯度方法。不过，作为入门读物，它值得花时间读全文，以了解流行病学中资源分配问题的数据结构和分析框架。

### 2. [10.1093/biostatistics/kxaa060](https://doi.org/10.1093/biostatistics/kxaa060) — Assessing risk model calibration with missing covariates
- **作者**: Yei Eun Shin, Mitchell H Gail, Ruth M Pfeiffer
- **期刊/来源**: Biostatistics
- **机构**: National Cancer Institute · Division of Cancer Epidemiology and Genetics
- **分类**: vol 23 · issue 3 · pp 875-890
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究在独立验证队列中评估风险模型校准度（即模型预测偏差）时，部分协变量缺失的问题。校准度由观察事件数 O 与模型期望事件数 E 的比值 O/E 量化。作者提出通过整合全队列可得的辅助信息来调整逆概率权重，以提高加权估计的效率。具体采用调查校准方法，要求完整数据子集中辅助统计量的加权和等于全队列中的总和。理论贡献包括推导了调整权重后 O/E 的解析方差公式。模拟表明，使用伪风险（仅利用全队列可用变量近似实际风险）作为辅助统计量进行权重调整，比逆概率加权效率高得多，且即使伪风险近似较差也能得到一致估计；多重插补在模型设定正确时有效，但误设时产生偏倚。该方法在独立队列中评估了第二原发甲状腺癌绝对风险模型的校准度。对您而言，本文展示了流行病学中处理缺失协变量的实用加权方法，与您对流行病学应用数据集的兴趣直接相关。
- **关键技术**: `inverse probability weighting`, `survey calibration`, `pseudo-risk estimate`, `multiple imputation`, `calibration assessment`
- **为什么对您有用**: 本文属于流行病学领域的应用方法论文，直接对应您的 secondary interest 中的流行病学应用数据集。方法上，调查校准与伪风险估计是处理缺失数据的实用技术，您武器库中的非参数统计和因果推断估计理论可帮助理解其效率增益机制。作为流行病学入门级方法论文，值得花时间读全文以了解该领域的数据分析模式。

### 3. [10.1093/biostatistics/kxaa059](https://doi.org/10.1093/biostatistics/kxaa059) — Estimation of the generation interval using pairwise relative transmission probabilities
- **作者**: Sarah V Leavitt, Helen E Jenkins, Paola Sebastiani, Robyn S Lee, C Robert Horsburgh, Andrew M Tibbs et al.
- **期刊/来源**: Biostatistics
- **机构**: Boston University · Massachusetts Department of Public Health
- **分类**: vol 23 · issue 3 · pp 807-824
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文提出一种利用常规监测数据估计传染病代际间隔（generation interval）的新方法，无需接触追踪或全基因组测序数据。核心思路是结合期望最大化算法与相对传播概率，并引入噪声降低步骤，从仅含发病时间的成对数据中推断感染关系。通过模拟实验验证了方法在不同再生数、代际间隔和突变率下的准确性。随后应用于2010-2016年马萨诸塞州结核病监测数据，估计了该地区的序列间隔（serial interval）。方法学上属于应用型贡献，未涉及新的统计推断理论或效率界。对您而言，本文是流行病学中因果推断（感染关系识别）的实用案例，但方法学新颖性有限，可作为应用场景参考。
- **关键技术**: `expectation maximization algorithm`, `relative transmission probability`, `noise reduction`, `surveillance data analysis`
- **为什么对您有用**: 本文属于流行病学应用，使用EM算法处理缺失的感染关系，与您secondary interest中的流行病学数据集和因果推断应用相关。但方法学深度一般，未涉及您primary interest中的高效推断或半参理论。武器库中'identification theory in causal inference'可帮助理解其识别假设，但本文不涉及新理论突破，属于暂不可做的应用阅读。

### 4. [10.1093/biostatistics/kxaa056](https://doi.org/10.1093/biostatistics/kxaa056) · [arXiv](https://arxiv.org/abs/2101.00484) — Marginal modeling of cluster-period means and intraclass correlations in stepped wedge designs with binary outcomes
- **作者**: Fan Li, Hengshi Yu, Paul J Rathouz, Elizabeth L Turner, John S Preisser
- **期刊/来源**: Biostatistics
- **机构**: Yale University · University of Michigan · The University of Texas at Austin · Duke University · University of North Carolina at Chapel Hill
- **分类**: vol 23 · issue 3 · pp 772-788
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对阶梯楔形集群随机试验（SW-CRT）中二元结局的边际建模问题，提出了一种基于集群-周期均值的估计方程方法。传统方法直接对个体水平观测定义估计方程，当集群-周期规模较大时计算负担沉重。作者证明，个体水平边际均值的拟得分可以等价地重写为集群-周期均值的拟得分，并通过将个体水平ICC映射为集群-周期均值间的相关性，为这一简化提供了严格的理论依据。该方法显著降低了计算成本，并支持干预效应和相关系数的快速点估计与区间估计。进一步，作者提出了矩阵调整的估计方程以改进ICC的有限样本推断。本文在广义线性模型框架下为相关二元结局提供了有效的ICC估计方法，从而落实了CONSORT扩展声明中关于报告ICC的关键建议。对您而言，本文展示了在复杂试验设计中通过聚合统计量简化计算并保持推断有效性的策略，其估计方程构造思路可迁移至您熟悉的因果推断纵向数据设定。
- **关键技术**: `estimating equations`, `cluster-period means`, `intraclass correlation coefficients (ICC)`, `generalized linear models for correlated binary outcomes`, `matrix-adjusted estimating equations`
- **为什么对您有用**: 本文属于流行病学领域的应用方法学工作，直接关联您的secondary interest中的流行病学方向。其核心贡献在于通过集群-周期均值聚合简化计算，这一思路与您非常熟悉的非参数统计和估计理论中的聚合技巧相通，可视为一个具体案例。本文是流行病学试验设计方法学的好入门读物，清晰阐述了数据结构和模型假设，值得花时间阅读全文以了解SW-CRT的边际建模框架。

## 其他  *(other, 10 篇)*

### 1. [10.1093/biostatistics/kxaa049](https://doi.org/10.1093/biostatistics/kxaa049) — An optimal kernel-based multivariate U-statistic to test for associations with multiple phenotypes
- **作者**: Y Wen, Qing Lu
- **期刊/来源**: Biostatistics
- **机构**: University of Auckland · University of Florida
- **分类**: vol 23 · issue 3 · pp 705-720
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于核的多元U统计量（KMU），用于检验一组预测因子与多个表型之间的关联。该方法采用秩基核函数处理多表型数据，对表型分布具有鲁棒性；并通过数据驱动的方式从多个候选核中选择最优核，以捕捉预测因子与表型间的复杂关系。KMU的渐近性质（包括零分布和一致性）被严格推导。模拟研究表明，KMU在控制第一类错误的同时，比现有方法（如多表型SKAT）具有更高的统计功效。在阿尔茨海默病神经影像学倡议的全基因组测序数据中，KMU检测到与影像表型相关的新基因。对您而言，本文直接连接您对高阶U统计量的理论兴趣，并展示了U统计量在遗传关联检验中的实际应用，其核选择策略和渐近理论可迁移至您熟悉的因果推断或高维设定。
- **关键技术**: `kernel-based multivariate U-statistic`, `rank-based kernel function`, `data-driven kernel selection`, `asymptotic null distribution`, `genetic association testing`
- **为什么对您有用**: 本文直接连接您对高阶U统计量的理论兴趣，其核选择策略和渐近理论可迁移至您熟悉的因果推断或高维设定。您可以用very_familiar的U统计量计算（treewidth/tensor contraction）分析其计算成本，或用moderately_familiar的HOIF理论检验其是否达到半参效率界。中期可做：需先熟悉遗传学中的核方法（如SKAT框架），但核心U统计量工具已在武器库中。

### 2. [10.1093/biostatistics/kxab006](https://doi.org/10.1093/biostatistics/kxab006) — Information enhanced model selection for Gaussian graphical model with application to metabolomic data
- **作者**: Jie Zhou, Anne G Hoen, Susan Mcritchie, Wimal Pathmasiri, Weston D Viles, Quang P Nguyen et al.
- **期刊/来源**: Biostatistics
- **机构**: Dartmouth College · University of North Carolina at Chapel Hill · University of Southern Maine
- **分类**: vol 23 · issue 3 · pp 926-948
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文针对高维生物数据信噪比低的特点，提出了一种结合先验知识的高斯图模型结构学习方法。首先，提出了结构贝叶斯信息准则（sBIC），将先验结构信息融入BIC中，并证明流行的扩展BIC（eBIC）是其特例。其次，设计了一个两步算法来构建候选模型池，该算法是数据驱动的，并自动嵌入先验结构。理论分析表明，在温和条件下，sBIC对高维高斯图模型具有模型选择一致性。模拟研究验证了所提算法优于现有方法，并对模型误设具有鲁棒性。应用于婴儿粪便代谢物相对浓度数据，验证了代谢通路参与是代谢物间条件依赖的显著因素，并发现了传统通路分析方法无法识别的新代谢物关系。本文属于应用导向的方法学工作，对您而言，其将先验信息整合入模型选择的思路在因果推断的敏感性分析中可能有借鉴价值，但核心方法（图模型选择）与您的主要兴趣方向（因果推断、高维统计、U统计量）关联较弱。
- **关键技术**: `structural Bayesian information criterion`, `Gaussian graphical model`, `model selection consistency`, `prior structure embedding`, `two-step candidate model pool algorithm`
- **为什么对您有用**: 本文属于应用统计方法学，与您的主要兴趣（因果推断、高维统计、U统计量）关联较弱。其将先验信息融入模型选择的思路在因果推断的敏感性分析中可能有启发，但核心工具（图模型选择）不在您的技术武器库中。作为流行病学应用，本文展示了代谢组学数据的分析流程，但方法学新颖性有限，不值得深入阅读。

### 3. [10.1093/biostatistics/kxab007](https://doi.org/10.1093/biostatistics/kxab007) · [arXiv](https://arxiv.org/abs/2005.08457) — Simultaneous differential network analysis and classification for matrix-variate data with application to brain connectivity
- **作者**: Hao Chen, Ying Guo, Yong He, Jiadong Ji, Lei Liu, Yufeng Shi et al.
- **期刊/来源**: Biostatistics
- **机构**: Alzheimer’s Disease Neuroimaging Initiative
- **分类**: vol 23 · issue 3 · pp 967-989
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对矩阵型数据（如fMRI脑功能连接）提出一种同时进行差异网络分析与分类的方法。采用Kronecker积协方差矩阵框架，分别捕捉空间（脑区）和时间（扫描序列）相关性，并将时间协方差视为冗余参数。核心创新在于通过集成学习识别病例组与对照组之间的差异交互模式（即差异网络），同时利用这些模式进行疾病诊断分类。方法不依赖向量化，保留了矩阵数据的结构信息。模拟实验验证了方法的有效性，并在阿尔茨海默病fMRI研究中应用，识别的枢纽节点和差异模式与已有实验一致，且样本外分类性能良好。对您而言，本文属于应用型工作，方法学新颖性有限（集成学习+Kronecker积框架在矩阵协方差估计中已有较多研究），但fMRI数据的矩阵结构处理思路可能对您的高维统计或统计计算兴趣有间接启发。
- **关键技术**: `Kronecker product covariance`, `differential network analysis`, `ensemble learning`, `matrix-variate data`, `functional connectivity`
- **为什么对您有用**: 本文属于流行病学/神经影像应用，连接您的secondary interest（流行病学应用）。方法学上，Kronecker积协方差框架与您very_familiar的高维协方差估计有交集，但核心方法（集成学习+差异网络）并非您武器库中的强项，且无新理论贡献。作为gateway reading，本文清晰展示了fMRI数据的矩阵结构及分析流程，适合了解流行病学应用场景，但无需深入阅读方法细节。

### 4. [10.1093/biostatistics/kxab005](https://doi.org/10.1093/biostatistics/kxab005) — Structure-preserving integrated analysis for risk stratification with application to cancer staging
- **作者**: Tianjie Wang, Rui Chen, Wenshuo Liu, Menggang Yu
- **期刊/来源**: Biostatistics
- **机构**: University of Wisconsin–Madison
- **分类**: vol 23 · issue 3 · pp 990-1006
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对多源个体患者数据，提出一种保持结构的分层分析方法，用于癌症分期等风险分层任务。目标是在多个研究间共享共同的分组结构以借力信息，同时允许数据异质性（如不平衡的数据结构）。方法基于“lasso-tree”框架，该框架比传统的分类回归树（CART）更灵活，能生成更多可能的分组模式，且其参数化自然融入风险因素的序信息。本文还首次建立了lasso-tree方法的理论性质（一致性、变量选择等），弥补了原文献的理论空白。通过模拟和多个乳腺癌数据集分析验证了方法的有效性。对您而言，本文属于应用统计方法开发，与您的主要兴趣（因果推断、高维统计）无直接交集，但若您关注多源数据整合或风险分层问题，可作为方法学参考。
- **关键技术**: `lasso-tree`, `classification and regression tree (CART)`, `grouping structure`, `data heterogeneity`, `variable selection`
- **为什么对您有用**: 本文与您的主要兴趣方向（因果推断、高维统计、半参理论）无直接关联，属于生物统计应用领域的方法开发。您的技术武器库（非参统计、高维渐近、M估计）可部分用于理解其理论证明，但核心问题（多源数据分层）并非您的活跃方向。暂不可做——核心机器（多源数据整合的特定惩罚方法）不在武器库中，且缺乏与您当前研究问题的直接连接。

### 5. [10.1093/biostatistics/kxab002](https://doi.org/10.1093/biostatistics/kxab002) · [arXiv](https://arxiv.org/abs/2005.08361) — Bayesian biclustering for microbial metagenomic sequencing data via multinomial matrix factorization
- **作者**: Fangting Zhou, Kejun He, Qiwei Li, Robert S Chapkin, Yang Ni
- **期刊/来源**: Biostatistics
- **机构**: Renmin University of China · Texas A&M University · The University of Texas at Dallas · University of North Texas at Dallas
- **分类**: vol 23 · issue 3 · pp 891-909
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对微生物组测序数据的组成性、稀疏性、噪声和异质性，提出一个可识别的贝叶斯多项矩阵分解模型，用于同时推断微生物和宿主上的重叠聚类。模型将观测到的过度离散零膨胀计数矩阵表示为Dirichlet-多项混合，并在其上分层构建潜在聚类结构。在贝叶斯框架下，聚类数自动确定，并自然整合了微生物分类等级树的信息，提升了结果的可解释性。通过模拟研究比较了替代方法，展示了方法的有效性。应用于炎症性肠病（IBD）患者的人体肠道微生物组数据，发现了与IBD及其亚型相关的已知菌科聚类。该工作主要贡献在贝叶斯建模和微生物组应用，而非您核心关注的因果推断、高维统计或半参效率理论。
- **关键技术**: `Bayesian multinomial matrix factorization`, `Dirichlet-multinomial mixture`, `overlapping biclustering`, `taxonomic rank tree`, `zero-inflated count model`
- **为什么对您有用**: 本文属于应用统计方法在流行病学（微生物组与疾病关联）中的工作，与您的secondary interest流行病学相关。但方法学上以贝叶斯非参数聚类为主，与您primary interests中的因果推断、高维RMT、U-统计等核心方向无直接技术交集。作为流行病学应用，本文的数据结构（组成性、零膨胀计数）和分析流程（聚类发现）可作为入门参考，但武器库中的工具（如minimax bound、U-统计）难以直接攻入。暂不可做——核心机器（贝叶斯非参数混合模型、MCMC计算）不在您的武器库中。

### 6. [10.1093/biostatistics/kxab004](https://doi.org/10.1093/biostatistics/kxab004) — A greedy approach for mutual exclusivity analysis in cancer study
- **作者**: Hongyan Fang, Zeyu Zhang, Yinsheng Zhou, Lishuai Jin, Yaning Yang
- **期刊/来源**: Biostatistics
- **机构**: Anhui University · University of Science and Technology of China
- **分类**: vol 23 · issue 3 · pp 910-925
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对癌症基因组学中驱动基因与乘客基因的区分问题，提出了一种基于概率生成模型的互斥性（ME）基因集选择方法。核心设定是假设突变在功能通路中呈现互斥模式，目标是从高维突变数据中识别出具有统计显著互斥性的基因集合。方法上采用贪心算法，包含预筛选和逐步前向选择两步，大幅降低了计算复杂度。通过功效分析验证了该方法在单ME集和含重叠基因的多ME集场景下的有效性。最后在TCGA全外显子测序数据上进行了实证分析。本文属于生物信息学应用，方法学贡献在于计算效率的改进，而非统计推断或因果识别的新理论。对您而言，该文与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接技术关联，但可作为生物医学应用领域的背景阅读。
- **关键技术**: `greedy algorithm`, `mutual exclusivity model`, `pre-selection procedure`, `stepwise forward selection`, `power analysis`
- **为什么对您有用**: 本文属于生物信息学应用，与您的主要兴趣方向（因果推断、高维统计、U统计量、半参效率理论等）无直接技术关联。武器库中的工具（如非参统计、高维渐近、U统计量计算）在此问题中未体现核心作用。暂不可做——核心机器（生物信息学中的突变互斥性模型和贪心算法）不在武器库中。作为gateway reading，本文对统计学家入门生物信息学有一定参考价值，但方法学新颖性有限。

### 7. [10.1093/biostatistics/kxaa054](https://doi.org/10.1093/biostatistics/kxaa054) — A benchmark for dose-finding studies with unknown ordering
- **作者**: Pavel Mozgunov, Xavier Paoletti, Thomas Jaki
- **期刊/来源**: Biostatistics
- **机构**: Lancaster University · Inserm · Institut Curie · University of Cambridge · MRC Biostatistics Unit
- **分类**: vol 23 · issue 3 · pp 721-737
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对剂量探索试验（dose-finding）中剂量-毒性顺序未知的问题，提出了一种非参数最优基准（benchmark）的推广。传统基准假设剂量可按毒性单调递增排序，但在联合用药试验中，部分剂量组合的毒性顺序无法确定。新基准通过计算在已知每位患者完整信息条件下每种可能排序的发生概率，给出了更紧的性能上界。该方法适用于任意数量的离散或连续终点。作者通过I期联合试验（二元毒性终点）和I/II期联合试验（二元毒性+连续疗效）的实例展示了其实用性。该基准为评估剂量探索设计提供了更严格的比较标准，但方法学上属于应用导向的扩展，而非理论创新。
- **关键技术**: `nonparametric optimal benchmark`, `dose-finding design`, `unknown ordering`, `Phase I/II combination trials`
- **为什么对您有用**: 本文属于临床试验设计的方法学应用，与您的主要兴趣（因果推断、高维统计等）无直接交集。武器库中无对应工具可攻该问题，且该方向（剂量探索基准）并非您的核心或次要兴趣领域。暂不可做。

### 8. [10.1093/biostatistics/kxaa061](https://doi.org/10.1093/biostatistics/kxaa061) · [arXiv](https://arxiv.org/abs/2010.06408) — Penalized model-based clustering of fMRI data
- **作者**: Andrew Dilernia, Karina Quevedo, Jazmin Camchong, Kelvin Lim, Wei Pan, Lin Zhang
- **期刊/来源**: Biostatistics
- **机构**: University of Minnesota System · University of Minnesota
- **分类**: vol 23 · issue 3 · pp 825-843
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出随机协方差聚类模型（RCCM），用于对fMRI数据中的功能连接（FC）网络进行无监督聚类。模型假设每个受试者的FC矩阵来自一个混合分布，其中每个组分对应一个聚类，组内共享一个公共的FC结构但允许个体间随机变异。估计采用惩罚似然框架，通过L1或自适应Lasso惩罚实现稀疏性和可解释性。模拟实验表明RCCM在聚类准确性和FC网络估计精度上优于K-means、谱聚类等现有方法。应用于精神分裂症患者与健康对照的静息态fMRI数据，RCCM识别出有临床意义的亚组。本文主要贡献在于同时进行受试者聚类和组/个体水平FC推断，但方法学上属于应用型拓展，未涉及因果推断或高维统计的新理论。
- **关键技术**: `random covariance clustering model`, `penalized likelihood`, `functional connectivity`, `mixture model`, `adaptive Lasso`
- **为什么对您有用**: 本文属于流行病学应用（精神分裂症fMRI数据），但方法学核心是聚类而非因果推断或高维统计，与您的主要兴趣（因果推断、高维RMT、U统计量）无直接技术交集。武器库中'非参数统计'或'高维渐近'可勉强用于分析其估计量的收敛性，但问题本身不涉及您擅长的识别策略或效率理论。作为流行病学gateway阅读，本文数据描述清晰（43+61样本，静息态fMRI），但方法学新颖性有限，不值得投入全文时间。

### 9. [10.1093/biostatistics/kxab008](https://doi.org/10.1093/biostatistics/kxab008) — Bayesian adaptive design for concurrent trials involving biologically related diseases
- **作者**: Matthew A Psioda, H Amy Xia, Xun Jiang, Jiawei Xu, Joseph G Ibrahim
- **期刊/来源**: Biostatistics
- **机构**: University of North Carolina at Chapel Hill · Amgen (United States)
- **分类**: vol 23 · issue 3 · pp 1007-1022
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文提出一种贝叶斯自适应设计方法，用于在多个生物学相关疾病的平行临床试验中同时研究同一试验药物，目标是在每个疾病中均证明优于对照。该方法通过构建相关混合先验来借用不同疾病间的疗效信息，该先验基于对每个疾病数据的悲观和乐观预测的共轭先验，并针对所有可能的先验配置（悲观/乐观）设定混合权重，分析过程与贝叶斯模型平均密切相关。该方法为不同疾病可能使用不同数据类型（如连续、二分类）的终点提供了稳健的信息借用框架。模拟研究表明，与使用贝叶斯层次模型的信息借用设计相比，所提设计框架在操作特征（如检验效能、I类错误控制）上表现更优，而贝叶斯层次模型在终点数据类型不同时信息借用效果不佳。本文主要贡献在于临床试验设计方法学，而非统计理论或因果推断。对您而言，该论文属于应用统计领域，与您的主要研究兴趣（因果推断、高维统计等）无直接关联，但如果您对临床试验设计或贝叶斯自适应方法感兴趣，可作为背景阅读。
- **关键技术**: `Bayesian adaptive design`, `correlated mixture priors`, `Bayesian model averaging`, `information borrowing`, `conjugate priors`
- **为什么对您有用**: 本文属于临床试验设计方法学，与您的主要研究兴趣（因果推断、高维统计、半参理论等）无直接关联。作为gateway-reading，本文对统计学家友好，清晰阐述了贝叶斯信息借用框架，但问题本身并非您武器库中工具（如U统计量、高效影响函数等）可直接攻克的。暂不可做，因为核心机器（贝叶斯自适应设计、混合先验elicitation）不在您的武器库中。

### 10. [10.1093/biostatistics/kxaa039](https://doi.org/10.1093/biostatistics/kxaa039) · [arXiv](https://arxiv.org/abs/1910.13293) — Sine-skewed toroidal distributions and their application in protein bioinformatics
- **作者**: Jose Ameijeiras-Alonso, Christophe Ley
- **期刊/来源**: Biostatistics
- **分类**: vol 23 · issue 3 · pp 685-704
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文针对生物信息学中氨基酸二面角数据（环面数据）的建模问题，提出了一类正弦偏斜环面分布。现有环面分布大多为（逐点）对称分布，而实际数据常呈现非对称模式。作者从对称环面分布出发，通过正弦偏斜变换构造非对称分布，其关键优势在于无需计算新的归一化常数，从而在增加灵活性的同时不增加模型复杂度。文章推导了新分布的一般性质，包括形状和依赖测度的显式表达式，给出了简单的随机数生成算法，并建立了极大似然估计的渐近理论。在蛋白质数据上的应用表明，新模型通常优于其对称基础模型。该工作主要贡献于统计分布建模与生物信息学应用，与您的主要研究方向（因果推断、高维统计等）无直接技术交集。
- **关键技术**: `sine-skewing`, `toroidal distributions`, `maximum likelihood estimation`, `circular statistics`
- **为什么对您有用**: 本文属于生物统计应用，与您的主要研究兴趣（因果推断、高维统计、半参理论等）无直接技术关联。作为流行病学或生物信息学的应用论文，其数据结构和分析模式对您的武器库（非参统计、M估计）有一定参考价值，但核心方法（环面分布建模）不在您的技术栈内，属于暂不可做的方向。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

