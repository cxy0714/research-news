# J. Econometrics — Vol 256  ·  2026-07-06

- 共 7 篇 · Journal of Econometrics
- 目录核对 ⚠️ 疑似漏 27 篇（对照 OpenAlex 36 篇）：10.1016/j.jeconom.2025.105978、10.1016/j.jeconom.2026.106253、10.1016/j.jeconom.2025.106075、10.1016/j.jeconom.2026.106239、10.1016/j.jeconom.2026.106267 等

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

这一期《Journal of Econometrics》第256卷的7篇论文，整体上围绕两条主线展开：一是高维与复杂数据结构下的变量选择与推断（文本词项选择、矩阵型时间序列、高频网络连通性检验），二是贝叶斯方法在结构模型与状态空间模型中的创新应用（随机波动率、离散数据联立方程、银行效率非参数建模）。此外，部分识别与因果推断在宏观计量中的应用也构成一条次要线索。

最突出的主线是**高维与复杂数据结构的变量选择与推断**，涉及三篇论文。Text-term selection and analysis 提出了信息自适应Lasso与Spike-and-Slab Lasso，在超高维文本词项选择中建立了比现有Lasso更快的收敛速率，并提供了频率与贝叶斯双视角。Testing for differences in high-frequency network connectedness 则针对高频方差分解网络连通性，提出了贝叶斯Wald型检验，在局部时间点下建立了渐近正态性，实证中识别了FOMC公告后的货币政策意外效应。Large Bayesian matrix autoregressions 处理高维矩阵型时间序列，通过Minnesota型收缩先验应对参数爆炸，虽方法学新颖性有限，但为跨区域面板或动态网络数据提供了可扩展的建模工具。

第二条主线是**贝叶斯方法在结构模型与状态空间模型中的创新**，涉及三篇论文。Stochastic volatility in mean 通过将非中心卡方分布近似为30个正态混合，扩展了经典混合抽样器，实现了SVM模型的高效联合抽样，并扩展到含杠杆效应情形。Partial identification of structural vector autoregressions 提出非中心参数化的随机波动率模型，其强收缩重尾先验能更精确评估部分识别程度，在财政SVAR应用中验证了有效性。Likelihood specification in simultaneous equation models for discrete data 则从马尔可夫过程不变分布出发，为离散数据联立方程模型推导出唯一且完备的似然函数，无需递归性假设，解决了早期悖论，但方法学偏向综述性。

此外，Bayesian nonparametric inference in bank business models 将贝叶斯非参数混合模型（LSBP）应用于银行商业模式动态演化，区分持久性与暂时性成本无效率，虽方法学创新有限，但为面板数据聚类与动态转移提供了实用工具。

与因果推断方向最贴近的论文是 Likelihood specification in simultaneous equation models for discrete data（条件分布建模与IV/mediation相关）和 Partial identification of structural vector autoregressions（部分识别与贝叶斯推断）。半参数效率方向可关注 Text-term selection and analysis（变量选择一致性速率）和 Testing for differences in high-frequency network connectedness（渐近正态性与检验）。高维方向则优先看 Text-term selection and analysis 与 Large Bayesian matrix autoregressions。

## 数理统计 / 假设检验  *(hypothesis_testing, 1 篇)*

### 1. [10.1016/j.jeconom.2026.106238](https://doi.org/10.1016/j.jeconom.2026.106238) — Testing for differences in high-frequency network connectedness from variance decompositions
- **作者**: Mattia Bevilacqua, Michael Ellington, Rodrigo Hizmeri
- **期刊/来源**: Journal of Econometrics
- **机构**: University of Liverpool
- **分类**: vol 256 · pp 106238
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对高频金融时间序列中方差分解网络连通性的时序差异提出贝叶斯Wald型检验。在固定局部时间点下，建立了脉冲响应函数和方差分解矩阵的渐近正态性，检验统计量在原假设下渐近服从χ²分布。蒙特卡洛模拟显示检验具有良好的有限样本性质。实证部分使用2013年1月至2023年6月行业ETF高频期权数据，识别并量化FOMC公告后的货币政策意外效应。结果表明，FOMC公告后行业ETF隐含波动率的总体连通性显著上升，在存在货币政策意外的交易日，这种高连通性持续约一小时。超过五分之一的FOMC公告对金融市场构成意外。该检验方法为高频网络连通性的统计推断提供了新工具，对您在高维时间序列假设检验方向有参考价值。
- **关键技术**: `Bayesian Wald test`, `variance decomposition`, `impulse response function`, `high-frequency data`, `network connectedness`
- **为什么对您有用**: 本文属于假设检验在高频网络连通性中的应用，连接到您的primary interest中的hypothesis testing方向。技术武器库中'high-dimensional asymptotics'和'nonparametric statistics'可用于分析其检验统计量的渐近性质及有限样本表现。中期可做：若想将类似检验推广到更一般的网络结构，需先在moderately_familiar的'M-estimation theory'上加强。

## 经济理论 / 应用  *(econ_theory, 5 篇)*

### 1. [10.1016/j.jeconom.2025.106163](https://doi.org/10.1016/j.jeconom.2025.106163) — Text-term selection and analysis: Frequentist and Bayesian strategies and interpretations
- **作者**: Cathy Yi-Hsuan Chen, George Kapetanios, Wei-Biao Wu
- **期刊/来源**: Journal of Econometrics
- **机构**: Adam Smith Institute · University of Glasgow · King's College London · University of Chicago
- **分类**: vol 256 · pp 106163
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对文本数据中超高维词项的选择与估计问题，提出了两种新方法：信息自适应Lasso（Information-Adaptive Lasso）和信息自适应Spike-and-Slab Lasso（Bayesian方法）。核心理论贡献在于建立了词项选择一致性的收敛速率，并证明该速率快于现有Lasso文献中的结果。方法通过自适应地调整惩罚权重，利用了文本数据的稀疏结构。在美联储FOMC声明数据集上的应用，识别并估计了驱动货币政策不确定性波动的高影响词项。该工作为经济文本分析提供了兼具频率学派和贝叶斯视角的实用工具。对您而言，这是一篇经济理论应用方向的实证论文，展示了高维变量选择方法在文本数据中的具体落地，可作为入门读物了解该领域的数据结构与分析流程。
- **关键技术**: `Information-Adaptive Lasso`, `Spike-and-Slab Lasso`, `term-selection consistency rate`, `ultra-high dimensionality`, `text data analysis`
- **为什么对您有用**: 本文属于经济理论应用方向，聚焦文本数据中的高维变量选择问题，是经济因果推断中常见的数据预处理步骤。您的武器库中'高维渐近理论'和'非参数统计'可以直接用于理解其收敛速率证明，但核心方法（自适应Lasso）并非您的主攻方向。作为gateway reading，本文清晰展示了经济文本数据的结构（超高维、稀疏性）和模型假设，适合作为进入经济文本分析领域的入门读物，值得花时间读全文以了解其数据侧和模型侧设定。

### 2. [10.1016/j.jeconom.2025.105955](https://doi.org/10.1016/j.jeconom.2025.105955) — Large Bayesian matrix autoregressions
- **作者**: Joshua C.C. Chan, Yaling Qi
- **期刊/来源**: Journal of Econometrics
- **机构**: Purdue University West Lafayette
- **分类**: vol 256 · pp 105955
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文针对高维矩阵型时间序列数据（如跨区域面板、动态经济网络），提出了一类大规模贝叶斯矩阵自回归模型（MAR）。传统方法将矩阵向量化后使用向量自回归（VAR），在矩阵维度增长时计算不可行。作者通过引入Minnesota型收缩先验来应对参数爆炸问题，并允许模型包含时变波动性、非高斯误差和COVID-19异常值。估计方法统一且可扩展到高维场景。实证部分使用美国50州6个宏观经济指标共300个时间序列的数据集，展示了模型的实际应用价值。对您而言，本文是经济时间序列建模的实用工具，其先验设计和计算策略可为您的因果推断（如纵向数据）提供参考，但方法学新颖性有限。
- **关键技术**: `Bayesian matrix autoregression`, `Minnesota shrinkage prior`, `time-varying volatility`, `high-dimensional time series`
- **为什么对您有用**: 本文属于经济理论（应用）方向，是您secondary interest中的经济数据集和模型应用。您的技术武器库中'高维渐近理论'和'软件工程'可用于评估其先验收缩的渐近性质或复现其计算流程。作为gateway阅读，本文清晰展示了高维矩阵时间序列的建模挑战和贝叶斯解决方案，适合入门；但核心方法（Minnesota先验）较为经典，您无需额外学习即可理解。值得花时间读全文以了解经济数据结构和建模思路。

### 3. [10.1016/j.jeconom.2025.105949](https://doi.org/10.1016/j.jeconom.2025.105949) · [arXiv](https://arxiv.org/abs/2404.13986) — Stochastic volatility in mean: Efficient analysis by a generalized mixture sampler
- **作者**: Daichi Hiraki, Siddhartha Chib, Yasuhiro Omori
- **期刊/来源**: Journal of Econometrics
- **分类**: vol 256 · pp 105949
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文针对随机波动率均值（SVM）模型，提出了一种高效的贝叶斯模拟方法。核心贡献是将非中心卡方分布精确近似为30个正态分布的混合，从而扩展了Kim等人（1998）和Omori等人（2007）针对SV模型的混合抽样器。在此混合表示下，参数和潜在波动率可在一个块内联合抽样，并通过额外的Metropolis-Hastings步骤校正近似误差。该方法进一步扩展到含杠杆效应的SVM模型。实证部分应用于超额持有收益率和S&P500收益率，基于边际似然比较表明SVM模型优于其他波动率模型。对您而言，本文是经济理论（金融计量）中贝叶斯MCMC方法的典型应用，展示了混合抽样器在复杂状态空间模型中的设计思路，可作为进入该领域的入门读物。
- **关键技术**: `Markov chain Monte Carlo`, `mixture sampler`, `non-central chi-squared approximation`, `Metropolis-Hastings correction`, `stochastic volatility in mean`
- **为什么对您有用**: 本文属于经济理论（金融计量）方向，是贝叶斯MCMC在波动率模型中的经典应用。武器库中'软件发展'和'非参数统计'可支撑理解其混合近似与MCMC实现，但核心的贝叶斯模拟技术（如块抽样、校正步骤）不在当前武器库中，属于'暂不可做'——需先补充贝叶斯计算基础。不过，作为gateway reading，本文清晰展示了状态空间模型的模拟推断流程，值得花时间读全文以了解金融计量中的典型分析模式。

### 4. [10.1016/j.jeconom.2025.106107](https://doi.org/10.1016/j.jeconom.2025.106107) · [arXiv](https://arxiv.org/abs/2404.11057) — Partial identification of structural vector autoregressions with non-centred stochastic volatility
- **作者**: Helmut Lütkepohl, Fei Shang, Luis Uzeda, Tomasz Woźniak
- **期刊/来源**: Journal of Econometrics
- **机构**: German Institute for Economic Research · Freie Universität Berlin · Technology Holding (United States) · Bank of Canada · The University of Melbourne
- **分类**: vol 256 · pp 106107
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究结构向量自回归（SVAR）模型在随机波动率假设下的部分识别问题。作者提出一种非中心参数化（non-centred parameterization）的随机波动率模型，其边际先验分布以同方差为中心，具有强收缩和重尾特性，这与常见的中心参数化形成对比。这种先验设定特别适合评估任何感兴趣冲击的部分识别程度。通过蒙特卡洛实验，作者证明非中心设定在小规模和大规模系统中都能更精确地估计结构参数，并有效归一化条件方差。最后，作者重新审视了著名的财政SVAR应用，展示了非中心方法如何识别出与文献中估计一致的税收冲击。对您而言，本文是经济理论（宏观计量经济学）中关于部分识别和贝叶斯推断的扎实应用，其非中心参数化策略可能为您的因果推断（尤其是纵向/时间序列设定）提供新的先验设计思路。
- **关键技术**: `non-centred parameterization`, `stochastic volatility`, `structural vector autoregression`, `Bayesian estimation`, `partial identification`, `shrinkage prior`
- **为什么对您有用**: 本文属于经济理论（宏观计量经济学）的应用工作，直接关联您的secondary interest。其非中心参数化随机波动率模型为时间序列因果推断（如IV或纵向设定）中的部分识别问题提供了一种新颖的贝叶斯先验策略，您可以用moderately_familiar的identification theory来评估该策略在更一般因果模型中的适用性。作为gateway reading，本文对宏观计量方法有清晰阐述，值得花时间读全文以了解其识别策略。

### 5. [10.1016/j.jeconom.2026.106190](https://doi.org/10.1016/j.jeconom.2026.106190) — Likelihood specification in simultaneous equation models for discrete data
- **作者**: Ivan Jeliazkov, Angela Vossmeyer
- **期刊/来源**: Journal of Econometrics
- **机构**: University of California, Irvine · Claremont McKenna College
- **分类**: vol 256 · pp 106190
- 相关性 3/10 · novelty: `survey`
- **摘要**: 本文针对离散数据联立方程模型（SEM）的似然函数规范问题，提出了一种基于马尔可夫过程不变分布的理论框架。传统方法依赖递归性假设或临时性规则，导致似然函数不唯一或存在悖论。作者通过将模型视为条件分布建模问题，推导出唯一、恰当且完备的似然函数，并给出了明确的简化型。该框架无需递归性假设，解决了早期文献中突出的悖论。文中还讨论了计算问题，并在三个实证应用（女性劳动参与、健康与财富互动、大萧条时期银行借贷行为）中展示了方法。对您而言，本文是经济理论中因果推断方法的基础性工作，其条件分布建模思路与您的因果推断（尤其是IV和mediation）兴趣相关，但方法学新颖性有限，属于应用导向的综述性工作。
- **关键技术**: `Markov process invariant distribution`, `conditional distribution modeling`, `simultaneous equation models`, `discrete data likelihood`, `reduced form`
- **为什么对您有用**: 本文直接关联您的secondary interest中的经济理论（econ_theory），特别是离散数据联立方程模型中的因果识别问题。您的武器库中'identification theory in causal inference'（moderately_familiar）可用于理解其条件分布建模框架与IV/mediation的联系。本文作为入门读物较好，但方法学深度有限，属于中期可读——需先熟悉经济学的联立方程传统，但无需额外技术工具。

## 其他  *(other, 1 篇)*

### 1. [10.1016/j.jeconom.2025.106109](https://doi.org/10.1016/j.jeconom.2025.106109) — Bayesian nonparametric inference in bank business models with transient and persistent cost inefficiency
- **作者**: Dimitris Korobilis, Emmanuel C. Mamatzakis, Vasileios Pappas
- **期刊/来源**: Journal of Econometrics
- **机构**: BI Norwegian Business School · Adam Smith Institute · University of Glasgow · Birkbeck, University of London · University of Surrey
- **分类**: vol 256 · pp 106109
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文提出一个贝叶斯非参数框架，用于识别和建模银行商业模式（BBM）的动态演化。在随机前沿分析框架下，将成本无效率分解为持久性和暂时性两个分量，以区分长期结构性问题与短期冲击。方法核心是基于Logit Stick-Breaking Process（LSBP）的无限混合模型，允许聚类数量随数据自适应，并通过协变量依赖的聚类实现银行在不同商业模式间的动态转移。相比传统参数或核方法，该方法兼具非参数灵活性与可扩展计算效率。实证部分使用欧洲银行面板数据，识别出四个商业模式簇，揭示了银行绩效与效率演化的新见解。对您而言，本文属于应用计量经济学论文，方法学创新有限（贝叶斯非参数混合模型在银行效率领域的应用），与您的主要兴趣方向（因果推断、高维统计、U统计量等）无直接技术连接。
- **关键技术**: `Bayesian nonparametrics`, `Logit Stick-Breaking Process`, `stochastic frontier analysis`, `infinite mixture model`, `predictor-dependent clustering`
- **为什么对您有用**: 本文属于应用经济学论文，与您的主要兴趣方向（因果推断、高维统计、U统计量、半参效率理论等）无直接技术连接。武器库中无对应工具可攻该文方法学口子。暂不可做——核心机器（贝叶斯非参数混合模型、随机前沿分析）不在武器库中，且该文方法学贡献不足以作为进入经济理论方向的入门读物。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

