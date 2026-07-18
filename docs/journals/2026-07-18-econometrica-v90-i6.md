# Econometrica — Vol 90  Issue 6  ·  2026-07-18

- 共 13 篇 · Econometrica
- 目录核对 ✅ 13 篇全部抓到（对照 OpenAlex 14 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

Econometrica 第 90 卷第 6 期围绕因果推断、经济理论与实证方法三条主线展开。因果推断主线集中了 Angrist 的总统演讲（LATE 框架与排他性约束的实践逻辑）、Imbens 的综述（因果推断的统计与计量传统融合）以及 Kenya 现金转移 RCT（一般均衡效应与溢出识别）和 United Fruit Company 的 RDD 案例（私营跨国公司的长期发展效应）。经济理论主线涵盖机制设计（Converse Envelope Theorem）、信息学习（Reviews 选择效应与学习速度）、政治经济学（Market Competition and Political Influence）以及自动化与不平等（Uneven Growth）。实证方法主线包括 Spatial Correlation Robust Inference（空间稳健推断）和 Robust Empirical Bayes Confidence Intervals（经验贝叶斯区间覆盖保证）。此外，Productivity Dispersion 与 Achieving Scale Collectively 分别从劳动力市场不完全竞争和小企业租赁市场角度补充了实证框架。

最突出的主线是因果推断的实践与理论深化。Angrist 的演讲以 LATE 框架为核心，强调排他性约束是 IV 识别中“最富争议”但“形式化承诺”的关键，并通过芝加哥考试学校案例展示其诊断价值。Imbens 的综述则从随机实验与选择模型两条脉络出发，指出 LATE 框架通过 complier 子群体和单调性假设实现了融合，并延伸至异质性处理效应与机制分析。Kenya 现金转移 RCT 通过村庄层面随机化捕捉一般均衡效应（溢出与价格），估计局部乘数约 2.5，为发展经济学中的宏观因果效应提供了罕见实验证据。United Fruit Company 的 RDD 利用土地特许权与结果变量的正交性，识别私营公司投资公共品的动机（工人流动性驱动），展示了历史案例中的因果识别策略。

另一条突出主线是经济理论中的信息与动态设计。Converse Envelope Theorem 将包络公式等价于一阶条件，推广了经典机制设计中递增分配的可实施性，并应用于信息销售。Learning From Reviews 模型刻画了选择效应下学习动态的复杂性，发现完整历史并不总是加速学习，但更细粒度的评分系统确实更快。Market Competition and Political Influence 则内生化市场力量与政治影响力的正反馈循环，揭示当市场力量过大时政策制定者与主导企业利益分歧导致无效率。这些工作均依赖精确的博弈论与贝叶斯更新建模，不涉及数据推断。

与因果推断方向最贴的优先看：Angrist（LATE 实践逻辑）、Imbens（因果推断融合综述）、Kenya 现金转移 RCT（一般均衡因果效应）、United Fruit Company RDD（历史案例因果识别）。与半参数效率/高维方向相关的：Spatial Correlation Robust Inference（worst-case 主成分 + 基准模型校准的稳健推断）、Robust Empirical Bayes Confidence Intervals（收缩效应临界值的平均覆盖保证）。

## 因果推断  *(causal_inference, 1 篇)*

### 1. [10.3982/ecta21204](https://doi.org/10.3982/ecta21204) — Causality in Econometrics: Choice vs Chance
- **作者**: Guido W. Imbens
- **期刊/来源**: Econometrica
- **分类**: vol 90 · issue 6 · pp 2541-2566
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文是 Guido Imbens 在 Econometrica 上发表的综述性论文，回顾了统计学与计量经济学中因果推断方法的两条发展脉络及其近年来的融合。统计学传统始于随机实验的设计与分析，强调通过随机化实现可忽略性；计量经济学传统则聚焦于经济主体最优选择下的非实验设定，如工具变量与选择模型。作者论证了局部平均处理效应（LATE）框架是促成融合的关键：它通过明确界定 complier 子群体和单调性假设，使工具变量假设对多领域学者透明且可检验。文章还讨论了近期因果推断的前沿发展，包括异质性处理效应、机制分析、以及结合实验与观测数据的方法，强调在保持透明性的同时提升相关性。作为一篇 survey，本文不提出新方法或新理论，但系统梳理了从 Fisher 到 Rubin、从 Heckman 到 Angrist-Imbens 的学术脉络，对理解因果推断在经济学中的识别策略演进具有重要参考价值。对您而言，本文可作为连接计量经济学因果推断传统与您熟悉的 proximal CI、IV 等工具的桥梁文献，尤其适合快速建立 LATE 框架与您武器库中非参数识别理论的对话语境。
- **关键技术**: `Local Average Treatment Effect (LATE)`, `Instrumental Variables`, `Randomized Experiments`, `Selection Models`, `Identification Assumptions`
- **为什么对您有用**: 本文直接对应您的 primary interest 中 causal inference 的 IV 和 identification 子方向，是理解计量经济学因果推断方法论演进的必读综述。您的武器库中 very_familiar 的 estimation theory in causal inference 和 moderately_familiar 的 identification theory 足以完全消化本文内容，属于**立即可做**的 gateway reading——读完后可立即将 LATE 框架与您熟悉的 nonparametric IV 或 proximal CI 设定进行对比，思考识别假设的透明性如何影响实际应用中的敏感性分析。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.3982/ecta18597](https://doi.org/10.3982/ecta18597) · [arXiv](https://arxiv.org/abs/2004.03448) — Robust Empirical Bayes Confidence Intervals
- **作者**: Timothy B. Armstrong, Michal Kolesár, Mikkel Plagborg-Møller
- **期刊/来源**: Econometrica
- **分类**: vol 90 · issue 6 · pp 2567-2602
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在正态均值估计问题中构造了稳健的经验贝叶斯置信区间（EBCI）。区间以通常的线性经验贝叶斯估计量为中心，但使用考虑了收缩效应的临界值。参数化EBCI假设均值服从正态分布（Morris, 1983b），当该假设不成立时可能严重欠覆盖。相比之下，本文的EBCI无论均值分布如何都能控制覆盖概率，同时在均值确实服从高斯分布时长度接近参数化EBCI。若将均值视为固定参数，本文的EBCI具有平均覆盖保证：每个均值的n个EBCI的平均覆盖概率至少为1-α。实证应用考虑了美国社区对代际流动性的影响。
- **关键技术**: `Empirical Bayes`, `confidence intervals`, `coverage guarantee`, `shrinkage estimation`, `normal means problem`
- **为什么对您有用**: 本文直接关联到假设检验和因果推断中的稳健推断问题。您熟悉的非参数统计和极小极大界工具可用于分析其覆盖保证的紧性。中期可做：需先在中等熟悉的半参数理论上提升，以将类似稳健EBCI方法推广到因果推断中的异质性处理效应估计。

## 经济理论 / 应用  *(econ_theory, 11 篇)*

### 1. [10.3982/ecta20640](https://doi.org/10.3982/ecta20640) — Empirical Strategies in Economics: Illuminating the Path From Cause to Effect
- **作者**: Joshua D. Angrist
- **期刊/来源**: Econometrica
- **分类**: vol 90 · issue 6 · pp 2509-2539
- 相关性 8/10 · novelty: `survey`
- **摘要**: 本文是 Angrist 在 Econometrica 上的总统演讲，系统阐述了 LATE 框架在应用经济学因果推断中的核心价值。LATE 框架将工具变量估计的识别条件拆解为随机分配的独立性假设和更富争议的排他性约束，后者形式化了研究者对简约式因果效应给出清晰一致解释的承诺。通过芝加哥考试学校入学对学业成绩影响的实证案例，作者展示了一个令人惊讶的排他性约束如何解释入学反而降低成绩的现象。文章还指出，应用计量经济学中的可信性革命至少同样归功于令人信服的实证分析，而非单纯的方法论创新。本文是 LATE 框架的权威综述和实证示范，对您作为因果推断研究者理解 IV 识别策略的实践逻辑和排他性约束的论证方式有直接参考价值。
- **关键技术**: `LATE framework`, `instrumental variables`, `exclusion restriction`, `random assignment`, `reduced-form causal effects`
- **为什么对您有用**: 本文直接连接您的 primary interest 中因果推断的 IV 子方向，是 LATE 框架的经典文献。您的武器库中 estimation theory in causal inference 和 identification theory in causal inference 足以完全理解本文的技术细节。作为经济理论方向的 gateway reading，本文是理解应用经济学中 IV 识别策略的必读之作，值得花时间全文阅读。

### 2. [10.3982/ecta19465](https://doi.org/10.3982/ecta19465) · [arXiv](https://arxiv.org/abs/2102.09353) — Spatial Correlation Robust Inference
- **作者**: Ulrich K. Müller, Mark W. Watson
- **期刊/来源**: Econometrica
- **分类**: vol 90 · issue 6 · pp 2901-2935
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文提出一种对多种空间相关形式稳健的置信区间构造方法。区间形式为常见的“估计量±标准误×临界值”，但标准误和临界值均采用新方法：标准误基于给定“最坏情况”空间相关模型的总体主成分构造，临界值则通过基准参数化空间相关模型校准以保证覆盖。该方法在有限样本高斯设定下，对一类受限但非参数的空间相关模型能控制覆盖概率；在大样本下，只要空间相关是弱的（即平均成对相关随样本量增大而消失），覆盖概率也成立。文章还给出了方法效率的理论结果。对您而言，这是一篇经济理论方向的应用论文，其稳健推断思路（worst-case 主成分 + 基准模型校准）可能对因果推断中的空间敏感性分析有启发，但方法学新颖性有限，属于应用层面的贡献。
- **关键技术**: `spatial correlation robust inference`, `population principal components`, `worst-case covariance model`, `benchmark parametric model`, `finite-sample coverage control`
- **为什么对您有用**: 本文属于经济理论方向的应用论文，连接您的 secondary interest 中的经济理论（空间数据推断）。武器库中 'estimation theory in causal inference' 和 'nonparametric statistics' 可用来评估其 worst-case 主成分方法在因果推断空间敏感性分析中的可迁移性——但核心机器（空间相关建模、主成分校准）不在您的主要武器库中，属于暂不可做方向。不过作为经济理论应用论文，本文是好的入门读物，值得花时间读全文以了解空间稳健推断的常见设定和工具。

### 3. [10.3982/ecta17945](https://doi.org/10.3982/ecta17945) — General Equilibrium Effects of Cash Transfers: Experimental Evidence From Kenya
- **作者**: Dennis Egger, Johannes Haushofer, Edward Miguel, Paul Niehaus, Michael Walker
- **期刊/来源**: Econometrica
- **机构**: University of California San Diego · Center for Effective Global Action · Max Planck Institute for Behavioral Economics · University of California, Berkeley · Stockholm University
- **分类**: vol 90 · issue 6 · pp 2603-2643
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文通过一项大规模随机对照试验（覆盖肯尼亚农村653个村庄、超过10,500户贫困家庭），研究一次性现金转移（约1000美元，相当于当地GDP的15%以上）对个体和总体经济的因果效应。实验设计采用村庄层面随机化，以捕捉一般均衡效应（包括溢出效应和价格效应）。核心发现是：受助家庭的消费和资产显著增加，同时非受助家庭和企业也出现显著的正向溢出效应，且通货膨胀极小。作者估计局部转移乘数约为2.5，即每1美元转移支付带来2.5美元的总收入增长。福利分析基于一个简单的家庭优化框架，将一般均衡效应纳入考量。该研究为发展经济学中现金转移的宏观效应提供了罕见的实验证据，对您作为关注因果推断和实证应用的研究者具有参考价值，尤其是其识别策略（村庄级随机化）和溢出效应的估计方法。
- **关键技术**: `cluster randomized trial`, `general equilibrium effects`, `spillover effects`, `local transfer multiplier`, `household optimization framework`
- **为什么对您有用**: 本文属于经济理论/应用方向，是您次要兴趣中的实证因果推断工作。其村庄级随机化设计和对一般均衡效应的识别，与您熟悉的因果推断识别理论（如IV、溢出效应）直接相关。武器库中的'identification theory in causal inference'和'estimation theory in causal inference'足以理解其核心识别策略，但若要深入分析其乘数估计的统计性质（如方差、置信区间），可能需要补充'nonparametric statistics'中的bootstrap或分位数方法。本文是值得花时间读全文的入门级实证研究，展示了如何用实验设计处理宏观因果问题。

### 4. [10.3982/ecta19514](https://doi.org/10.3982/ecta19514) — Multinationals, Monopsony, and Local Development: Evidence From the United Fruit Company
- **作者**: Esteban Méndez, Diana Van Patten
- **期刊/来源**: Econometrica
- **机构**: Yale University
- **分类**: vol 90 · issue 6 · pp 2685-2721
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究私营跨国公司在当地公共品发展中的作用，以20世纪最大的跨国公司之一——联合果品公司（UFCo）在哥斯达黎加的历史案例为对象。利用1899年至1984年的大规模土地特许权，结合1973年至2011年的行政普查数据（含街区级地理参照），采用地理断点回归设计（RDD），利用土地分配与结果变量正交的特性进行因果识别。研究发现，该公司对当地生活水平产生了积极且持久的影响。公司档案揭示，其核心动机是吸引和维持大规模劳动力，这促使公司大力投资于教育和健康等本地公共品。通过实证分析和理论模型，进一步证明公司的投资努力随工人流动性增加而增强。该文为经济史和区域发展中的因果推断提供了扎实的实证案例，其RDD设计和机制检验思路对应用因果工作有参考价值。
- **关键技术**: `regression discontinuity design`, `geographic RDD`, `causal identification`, `mechanism analysis`, `administrative census data`
- **为什么对您有用**: 本文属于经济理论（经济史/发展经济学）的应用因果工作，直接对应您的secondary interest中的经济理论方向。其核心方法——地理断点回归设计——是您武器库中'causal inference'中identification理论的具体应用，您可以用'minimax bounds for estimation problems'的视角来评估其RDD估计量的最优性。本文作为应用论文，数据和分析流程清晰，适合作为进入经济史因果推断领域的入门读物，值得花时间阅读全文。

### 5. [10.3982/ecta18119](https://doi.org/10.3982/ecta18119) · [arXiv](https://arxiv.org/abs/1909.11219) — The Converse Envelope Theorem
- **作者**: Ludvig Sinander
- **期刊/来源**: Econometrica
- **分类**: vol 90 · issue 6 · pp 2795-2819
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文在机制设计理论中证明了一个带逆命题的包络定理：包络公式等价于一个一阶条件。与 Milgrom 和 Segal (2002) 的包络定理类似，该结果对选择集不施加任何结构。利用该逆包络定理，作者将经典机制设计中“任何递增分配都是可实施的”这一结论推广到一般结果和偏好，并将其应用于信息销售问题。该工作属于纯经济理论，不涉及统计推断或数据。
- **关键技术**: `envelope theorem`, `mechanism design`, `first-order condition`, `implementation`
- **为什么对您有用**: 本文属于经济理论（secondary interest），但纯理论推导，无数据或统计方法，对您当前武器库的直接帮助有限。作为 gateway reading，它展示了经济理论中机制设计的核心逻辑，但缺乏与您统计兴趣（因果推断、高维、U-统计）的明显连接。暂不可做：核心机器不在武器库里（缺机制设计理论背景）。

### 6. [10.3982/ecta15847](https://doi.org/10.3982/ecta15847) — Learning From Reviews: The Selection Effect and the Speed of Learning
- **作者**: Daron Acemoglu, Ali Makhdoumi, Azarakhsh Malekian, Asuman Ozdaglar
- **期刊/来源**: Econometrica
- **机构**: Duke University · University of Toronto · Massachusetts Institute of Technology
- **分类**: vol 90 · issue 6 · pp 2857-2899
- 相关性 4/10 · novelty: `new_theory`
- **摘要**: 本文构建了一个贝叶斯学习模型，研究消费者如何从在线评论中推断产品质量，并分析不同评分系统（完整历史 vs. 汇总统计）下学习是否收敛以及收敛速度。核心设定是：消费者根据当前可获得的评分信息决定是否购买并留下评论，由此产生选择效应——购买者的类型（进而其满意度与评论）依赖于购买时可得的信息，这使学习动态复杂化。模型刻画了在两种评分系统下完全学习的条件，并比较了学习速度。关键发现是：提供更多信息（完整历史）并不总是加速学习，但严格更细的评分系统（即更细粒度的信息划分）确实会加快学习。理论结果依赖于对信息结构、消费者决策和贝叶斯更新过程的精确建模。对您而言，本文是经济理论中关于信息设计与学习动态的经典问题，其选择效应的建模思路与因果推断中的选择偏差问题有深层联系，可作为理解经济学中信息反馈机制的入门读物。
- **关键技术**: `Bayesian learning`, `selection effect`, `rating systems`, `information design`, `learning dynamics`
- **为什么对您有用**: 本文属于经济理论（secondary interest），是信息设计与在线平台学习动态的经典模型。武器库中'identification theory in causal inference'中的选择偏差概念可直接类比本文的选择效应，但本文是纯理论模型，不涉及统计推断或数据，因此暂不可做——核心机器（动态博弈与信息设计）不在武器库中。作为入门读物，它清晰展示了经济学如何形式化'评论偏差'问题，值得花时间读全文以理解建模框架。

### 7. [10.3982/ecta19775](https://doi.org/10.3982/ecta19775) — Market Competition and Political Influence: An Integrated Approach
- **作者**: Steven Callander, Dana Foarta, Takuo Sugaya
- **期刊/来源**: Econometrica
- **机构**: Stanford University
- **分类**: vol 90 · issue 6 · pp 2723-2753
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 本文构建了一个整合模型，将市场运作与政治决策之间的双向反馈内生化。模型设定中，政策制定者（政治家）选择市场规则（如监管强度），而市场中的企业通过政治影响（如游说）来改变政策。核心机制是市场力量与政治力量之间的正反馈循环：市场力量带来政治影响力，政治影响力又进一步巩固市场力量。然而，这种循环存在边界——当市场力量过大时，政策制定者与主导企业的利益出现分歧，反而会加剧静态和动态无效率。模型揭示了在战略性政策制定者介入下，关于市场竞争的传统直觉可能被颠覆。本文属于经济理论中的博弈论与政治经济学交叉领域，为理解市场与政治的相互塑造提供了形式化框架。
- **关键技术**: `political economy model`, `feedback loop`, `strategic policymaker`, `market power`, `dynamic inefficiency`
- **为什么对您有用**: 本文属于经济理论（secondary interest），提供了一个理解市场力量与政治影响力相互作用的模型框架。对于研究者而言，该模型中的'反馈循环'概念可能启发因果推断中处理'政策内生性'或'双向因果'的新识别策略。不过，本文是纯理论模型，不涉及数据或统计方法，因此作为入门读物价值有限——武器库中的'identification theory in causal inference'可用来思考如何将这类理论模型转化为可检验的因果假设，但当前阶段暂不可做，因为缺乏现成的数据结构和估计框架。

### 8. [10.3982/ecta18612](https://doi.org/10.3982/ecta18612) — Productivity Dispersion, Between‐Firm Competition, and the Labor Share
- **作者**: Émilien Gouin-Bonenfant
- **期刊/来源**: Econometrica
- **机构**: Columbia University
- **分类**: vol 90 · issue 6 · pp 2755-2793
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究劳动力市场不完全竞争对劳动收入份额的影响，构建了一个强调生产率离散度与企业在劳动力市场竞争之间相互作用的可处理模型。模型假设企业具有异质性生产率，并在劳动力市场进行工资竞争，劳动份额由企业生产率分布和竞争强度共同决定。作者利用2000-2015年加拿大全量企业行政数据校准模型，发现大多数企业劳动份额较高，但少数大型高生产率企业的非比例效应导致总体劳动份额偏低。核心机制是生产率离散度使高生产率企业免受工资竞争压力，从而降低总体劳动份额。跨国和跨行业的回归证据支持模型预测和机制。对您而言，本文提供了一个将生产率分布与市场结构联系起来的实证框架，其识别策略和校准方法可作为经济理论方向应用因果推断的参考案例。
- **关键技术**: `firm heterogeneity model`, `wage competition`, `productivity dispersion`, `administrative data calibration`, `cross-country regression`
- **为什么对您有用**: 本文属于经济理论方向的应用研究，连接了您的secondary interest中的经济理论（模型、数据集、应用因果工作）。本文的校准方法和回归证据展示了如何利用行政数据检验结构性模型，您武器库中的非参数统计和因果推断估计理论可用于分析其识别假设的稳健性。作为gateway reading，本文模型清晰、数据详实，适合作为进入经济理论实证研究的入门读物，值得花时间读全文以了解其分析模式。

### 9. [10.3982/ecta19417](https://doi.org/10.3982/ecta19417) — Uneven Growth: Automation's Impact on Income and Wealth Inequality
- **作者**: Benjamin Moll, Lukasz Rachel, Pascual Restrepo
- **期刊/来源**: Econometrica
- **机构**: London School of Economics and Political Science · University College London · Boston University
- **分类**: vol 90 · issue 6 · pp 2645-2683
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文构建了一个可处理的理论框架，将自动化技术冲击与收入及财富分配（而非仅工资分布）联系起来。核心机制是：自动化通过提高资本回报率来加剧不平等，同时可能导致低端工资停滞，从而压低底层收入。作者使用多资产模型扩展来区分生产性资产与安全资产的回报率差异，并利用美国数据校准模型，发现自动化可以解释部分观察到的收入与财富不平等趋势。该理论将技术变迁、要素回报与分配动态统一在一个均衡框架内，为理解自动化对宏观不平等的影响提供了新的机制视角。对您而言，这是一篇经济理论领域的应用性论文，其模型设定和校准思路可作为您从事应用因果推断或流行病学队列研究时处理技术冲击与分配效应的参考。
- **关键技术**: `multi-asset model`, `capital-return channel`, `automation-inequality link`, `model calibration with US data`
- **为什么对您有用**: 本文属于经济理论（secondary interest）的应用性论文，模型清晰、数据校准规范，适合作为入门读物了解自动化与不平等关系的理论机制。您的武器库中'identification theory in causal inference'和'high-dimensional asymptotics'虽不直接适用，但模型中的要素回报动态与分配效应分析思路可迁移至流行病学队列研究中的技术冲击评估。暂不可做：核心机器（一般均衡模型校准）不在武器库中，需先补充宏观经济学模型方法。

### 10. [10.3982/ecta18773](https://doi.org/10.3982/ecta18773) — Achieving Scale Collectively
- **作者**: Vittorio Bassi, Raffaela Muoio, Tommaso Porzio, Ritwika Sen, Esau Tugume
- **期刊/来源**: Econometrica
- **机构**: University of Southern California · Center for Economic and Policy Research · Columbia University · Kellogg's (Canada)
- **分类**: vol 90 · issue 6 · pp 2937-2978
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文研究发展中国家小企业通过租赁市场实现机械化的问题。作者在乌干达对制造业企业进行实地调查，发现非正式集群内存在活跃的大型机器租赁市场。基于此，构建了一个企业行为的均衡模型，并用调查数据估计模型参数。结果表明，租赁市场在促进机械化和提高生产率方面具有定量重要性，因为它能绕开其他导致企业规模偏小的市场不完善因素。租赁市场还会影响发展政策（如购买机器补贴）促进机械化的有效性。总体而言，本文强调在理解低收入国家技术采纳时，必须考虑非正式集群内的企业间互动，仅关注企业规模本身可能产生误导。
- **关键技术**: `equilibrium model`, `structural estimation`, `survey data`
- **为什么对您有用**: 本文属于经济理论的应用实证工作，与您的 secondary interest 经济理论（应用、数据集、因果推断）直接相关。它展示了如何利用调查数据构建和估计结构模型，其分析模式（均衡建模+数据估计）对您理解经济学中的因果推断和实证策略有参考价值。武器库中的 estimation theory in causal inference 可用于理解其估计策略的识别假设。本文是值得花时间阅读全文的入门级经济学实证论文。

### 11. [10.3982/ecta18310](https://doi.org/10.3982/ecta18310) — A Negishi Approach to Recursive Contracts
- **作者**: Gaetano Bloise, Paolo Siconolfi
- **期刊/来源**: Econometrica
- **机构**: Columbia University
- **分类**: vol 90 · issue 6 · pp 2821-2855
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文提出了一种基于Negishi方法研究递归合约的新框架。在递归合约问题中，一个计划者负责指定当前行动以及所有代理人未来效用值的分布，以最大化其加权效用和。在凸性条件下，该方法能够精确刻画有效前沿；否则，合约需要依赖于与基本面无关的公开可观测随机信号。文章还提供了有效合约的可操作一阶条件，并与文献中已有的对偶方法进行了全面比较。该工作为动态合约理论提供了新的分析工具，尤其适用于宏观经济学和金融学中的长期契约设计问题。对您而言，本文属于经济理论领域的应用型工作，可作为了解递归合约建模的入门读物，但方法学创新有限。
- **关键技术**: `Negishi method`, `recursive contracts`, `efficient frontier`, `first-order conditions`, `dual method`
- **为什么对您有用**: 本文属于经济理论（递归合约）的应用型工作，与您的次要兴趣经济理论直接相关。作为入门读物，它清晰地阐述了递归合约的建模框架和Negishi方法，但武器库中的非参数统计、高维渐近等工具无法直接用于攻破其核心问题。本文值得花时间阅读全文以了解经济理论中的合约设计范式，但暂不可做后续方法学拓展。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

