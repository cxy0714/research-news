# Econometrica — Vol 93  Issue 5  ·  2026-06-21

- 共 12 篇 · Econometrica
- 目录核对 ✅ 12 篇全部抓到（对照 OpenAlex 15 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚成三条主线：半参数分布建模与估计效率、实验与政策评估中的推断框架（含贝叶斯与规格搜寻）、以及基于结构模型与准实验变异的宏观/空间反事实分析。半参数/非参方向仅有“Gaussian Transforms”一篇，但直接切入条件分布的参数率估计；推断框架方面，“Misaligned Preferences”处理规格搜寻下的minimax最优估计，“Bayesian Impact Evaluation”引入先验信息缓解小样本实验的推断瓶颈；实证与结构估计构成了本期最大板块，包含“Rural Pensions”“Surge Pricing”“Landmines”等多篇，普遍采用IV或事件研究识别reduced-form效应，再嵌入一般均衡或空间均衡模型做政策反事实。此外，纯经济理论（OLG债务可持续性、气候贸易俱乐部、非平稳搜索匹配）与实验结构估计（高阶风险偏好）各占零星篇幅。

在推断框架与估计效率这条主线中，两篇论文从不同角度应对有限信息下的估计稳健性。“Misaligned Preferences”在研究者可能做规格搜寻的设定下，证明无偏性约束可将研究者偏好与社会MSE目标对齐，并构造出固定偏差下的minimax最优样本分割估计器，为因果推断中的sensitivity analysis与规格稳健性提供了新视角；“Bayesian Impact Evaluation”则在小样本政策评估中正式引入由多方elicitation得到的贝叶斯先验，展示了先验与数据一致性如何缩窄后验区间，而噪声大的结果几乎不更新先验，直观呈现了贝叶斯框架在实验推断中的效率边界。半参数建模方面，“Gaussian Transforms”通过单调变换将条件CDF映射至Gaussian结构并以凹似然做MLE，在保证单调性与误设稳健性的同时，实现了条件密度、CDF与分位数函数的参数率（n^{-1/2}）一致估计，对现有分布回归（DR、QR）构成了方法上的简化与理论推进。

结构估计与准实验识别的结合是本期实证板块的突出特征，多篇论文共享“先用IV/事件研究拿reduced-form，再建结构模型做反事实”的范式。“Rural Pensions”利用农村养老金政策的准实验变异估计迁移成本与生产率差异，随后在一般均衡模型中量化劳动力再配置对GDP与福利的拉动；“Landmines”自建地理编码面板，通过事件研究验证排雷的因果效应，并构建market-access IV分离直接与间接效应，反事实显示经济红利主要源于市场接入的间接渠道；“Surge Pricing”则依托平台真实数据，在空间均衡结构模型中量化动态定价的福利分配，发现乘客受益而司机（尤其是长工时女性）受损。此外，“Privatizing Disability Insurance”利用德国改革外生变异结合差分法识别挤出效应，并通过揭示偏好估算保险支付意愿以完成福利分析；“Women in Science”与“Structural Estimation of Higher Order Risk Preferences”分别用事件研究与实验设计结构模型，处理长面板中的生育惩罚与高阶风险偏好估计。

对因果推断与半参数效率方向的研究者，优先建议看“Gaussian Transforms”（条件分布的半参数参数率估计与单调性保证）与“Misaligned Preferences”（规格搜寻下的minimax最优性与偏差约束框架）；关注高维与结构反事实评估的读者，可重点留意“Rural Pensions”与“Landmines”中IV与一般均衡/空间均衡模型的嵌套范式。

## 非参数 / 半参数  *(nonparam_semipara, 1 篇)*

### 1. [10.3982/ecta19153](https://doi.org/10.3982/ecta19153) · [arXiv](https://arxiv.org/abs/2011.06416) — Gaussian Transforms Modeling and the Estimation of Distributional Regression Functions
- **作者**: Richard H. Spady, Sami Stouli
- **期刊/来源**: Econometrica
- **分类**: vol 93 · issue 5 · pp 1885-1913
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于 Gaussian transforms 的条件累积分布函数（cCDF）的灵活半参数建模方法，目标 estimand 为条件分布函数（密度、CDF、分位数）。核心机制是通过单调变换将 cCDF 映射至 Gaussian 结构，并构建凹似然准则进行 MLE 估计；该估计在有限样本及一般模型误设下均保证 cCDF 的单调性。理论性质上，方法实现了条件密度、CDF 与分位数函数的 parametric rate（n^{-1/2}）一致估计，且相比现有分布回归（如 DR、QR）方法在有限样本表现上有显著简化与改善。实证部分以美国性别工资差距数据展示框架应用。对您可能有用：该框架为条件分布估计提供了保证单调性的 MLE 路径，可与您熟悉的 semiparametric efficiency 理论对比其是否达到效率界。
- **关键技术**: `Gaussian transform`, `concave likelihood estimation`, `distributional regression`, `conditional CDF monotonicity`, `parametric-rate MLE`, `quantile function estimation`
- **为什么对您有用**: 本文直接连接到 semiparametric & nonparametric theory 子方向，聚焦条件分布函数的灵活建模与估计。您可用 very_familiar 的 minimax bounds 与 M-estimation theory 工具，审视其声称的 parametric rate 在何种光滑度假设下成立、以及该 MLE 是否达到 semiparametric efficiency bound（moderately_familiar），从而判断其理论紧致性。中期可做：需先在 moderately_familiar 的 semiparametric theory 上长肌肉，以严格推导该估计的 influence function 并与效率界对比。

## 经济理论 / 应用  *(econ_theory, 11 篇)*

### 1. [10.3982/ecta18640](https://doi.org/10.3982/ecta18640) — Optimal Estimation When Researcher and Social Preferences Are Misaligned
- **作者**: Jann Spiess
- **期刊/来源**: Econometrica
- **机构**: Stanford University
- **分类**: vol 93 · issue 5 · pp 1779-1810
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在实验数据分析的机制设计设定下，本文研究研究者偏好与社会偏好（MSE最小化）不一致时的最优 ATE 估计问题，关键假设是研究者可基于数据选择协变量调整规格。核心结果表明：无偏性要求可将研究者的规格搜寻偏好与 MSE 最小化目标对齐；在固定偏差约束下，可推导出 minimax 意义上的最优估计限制。进一步，本文将固定偏差的处理效应估计器构造性地表征为样本分割程序，并讨论了允许有益规格搜寻的次优估计器的实现。对您可能有用：该文的 minimax 最优性与偏差约束框架，为因果推断中 sensitivity analysis 与 specification robustness 提供了新的理论视角。
- **关键技术**: `mechanism design for estimation`, `minimax optimality under bias constraint`, `covariate adjustment`, `sample-splitting characterization`, `specification search`, `average treatment effect`
- **为什么对您有用**: 本文直接连接因果推断的 estimation theory 与 sensitivity analysis 子方向——将研究者 specification search 视为内生偏好偏离，用 minimax 界刻画偏差约束下的最优估计。用您 very_familiar 的 minimax bounds 工具即可分析其 minimax 最优性声称是否紧，并可用 moderately_familiar 的 M-estimation theory 探究该机制设计框架在更一般 semiparametric 模型下的推广。**立即可做**：用 minimax 工具验证其偏差约束下的最优界。

### 2. [10.3982/ecta19699](https://doi.org/10.3982/ecta19699) — Rural Pensions, Labor Reallocation, and Aggregate Income: An Empirical and Quantitative Analysis of China
- **作者**: Qingen Gai, Naijia Guo, Bingjing Li, Qinghua Shi, Xiaodong Zhu
- **期刊/来源**: Econometrica
- **机构**: Shanghai Jiao Tong University · University of Hong Kong
- **分类**: vol 93 · issue 5 · pp 1663-1696
- 相关性 7/10 · novelty: `application`
- **摘要**: 本文研究中国农村养老金政策对劳动力再配置与总收入的影响，核心 estimand 为农村-城市迁移成本与部门生产率差异。基于大规模面板数据，利用政策实施的准实验变异进行 reduced-form 估计，发现迁移成本显著、部门生产率差异巨大，而异质性自选择对部门收入差距贡献微小。随后构建并结构估计了一个含内生劳动供给与迁移的一般均衡家庭模型，模型结果与 reduced-form 一致，揭示了养老金通过改善家庭内劳动配置提升 GDP 与福利的机制。反事实分析表明即使迁移成本大幅降低政策仍有正效应，扩大政策规模将带来更大改善。对您而言，本文展示了 IV/准实验方法与结构估计在经济学中的结合范式。
- **关键技术**: `quasi-experimental variation`, `structural general equilibrium estimation`, `reduced-form causal estimation`, `counterfactual policy analysis`, `Roy model sorting`
- **为什么对您有用**: 本文属于经济理论（应用因果与结构估计）方向，利用政策准实验变异做 reduced-form 因果识别，再嵌入一般均衡结构模型做反事实分析，是经典的 IV+结构估计范式。您的武器库中 identification theory in causal inference 与 estimation theory in causal inference 可直接审视其 reduced-form 识别策略与结构估计的效率/鲁棒性。**立即可做**：用 very_familiar 的因果识别理论审视其 IV/准实验假设的敏感性，或用 moderately_familiar 的 M-estimation 理论评估其结构估计的渐近性质。

### 3. [10.3982/ecta22260](https://doi.org/10.3982/ecta22260) — Structural Estimation of Higher Order Risk Preferences
- **作者**: Morten I. Lau, Hong Il Yoo
- **期刊/来源**: Econometrica
- **机构**: Copenhagen Business School · Durham University · Loughborough University
- **分类**: vol 93 · issue 5 · pp 1855-1883
- 相关性 6/10 · novelty: `application`
- **摘要**: 本文在期望效用理论（EUT）框架下，利用实验数据对高阶风险态度（风险厌恶、审慎、节制）进行结构性估计。作者设计了一个新颖的彩票选择实验，并构建了对应的计量模型，允许同时估计绝对风险厌恶、绝对审慎和绝对节制指数，而不施加相互独立的参数约束。估计结果显示，三种风险态度随收入水平呈现不同的变化模式，且EUT与等级依赖效用理论（RDU）预测的风险溢价随风险阶数升高而逐渐收敛。常规的CRRA等参数效用函数会因风险厌恶假设而掩盖这些模式，导致对审慎和节制的估计偏误。本文的结构性方法在中等样本下依然稳健，表明该方法可推广至更大规模的研究。对于关注经济理论中偏好估计的研究者，本文提供了实验设计与结构建模相结合的实证范例，但其统计方法以经典MLE/非线性最小二乘为主，未涉及因果推断或半参数效率理论。
- **关键技术**: `structural estimation`, `Expected Utility Theory`, `Rank-Dependent Utility Theory`, `experimental design for risk preferences`, `nonlinear least squares / MLE`
- **为什么对您有用**: 本文属于经济理论中偏好估计的实证研究，与次要兴趣中的经济理论（应用、模型）直接相关。研究者的武器库中 moderately_familiar 的 M-estimation 理论可用于理解其似然估计框架，但结构性估计中关于实验设计、效用函数非线性识别等细节并非研究者当前专长。总体而言，作为经济学应用论文，本文的统计方法相对传统，研究者读后可能获得对风险偏好度量领域的概念性了解，但难以直接迁移到自身主攻的因果推断或高维统计问题。建议作为入门读物快速浏览，不展开深度挖掘。

### 4. [10.3982/ecta19106](https://doi.org/10.3982/ecta19106) — Who Benefits From Surge Pricing?
- **作者**: Juan Camilo Castillo
- **期刊/来源**: Econometrica
- **机构**: University of Pennsylvania
- **分类**: vol 93 · issue 5 · pp 1811-1854
- 相关性 5/10 · novelty: `application`
- **摘要**: 本文研究网约车平台Uber动态定价（surge pricing）的福利效应。作者利用Uber真实数据，构建了一个包含需求、供给和匹配技术的空间均衡结构模型，以量化动态定价相对于统一定价的福利变化。实证发现：动态定价使总福利增加约2.15%的毛收入，但分配效应高度不对称——乘客剩余增加3.57%，而司机剩余减少0.98%，平台利润减少0.50%。异质性分析表明，所有收入水平的乘客均受益；司机中，工作时间较长者（尤其是女性司机）受损最大。该文采用结构估计（而非传统因果推断中的IV或DID）进行反事实政策评估，模型识别依赖于供需匹配的均衡条件。对您而言，此文的政策反事实框架和新颖的异质性分析值得借鉴，可拓展您在经济学应用中因果推断的实证思路。
- **关键技术**: `spatial equilibrium model`, `structural estimation`, `counterfactual policy evaluation`, `demand-supply-matching model`, `heterogeneity analysis`
- **为什么对您有用**: 本文直接对应您的次要兴趣“经济理论（数据集、应用因果工作）”。虽然方法论是结构性估计而非您主力研究的因果推断，但其反事实评估思路和空间均衡建模可以拓宽您对政策评估工具的理解，尤其适合作为入门读物了解经济学中结构模型与因果推断的交叉。您的武器库中“estimation theory in causal inference”可用于分析模型识别假设；中期可做：若想深入复现类似分析，需补充对空间均衡匹配计量经济学的基础（当前武器库未覆盖该子方向，学习成本中等）。

### 5. [10.3982/ecta21567](https://doi.org/10.3982/ecta21567) — Bayesian Impact Evaluation With Informative Priors: An Application to a Colombian Management and Export Improvement Program
- **作者**: Leonardo Iacovone, David McKenzie, Rachael Meager
- **期刊/来源**: Econometrica
- **机构**: World Bank · World Bank Group · UNSW Sydney
- **分类**: vol 93 · issue 5 · pp 1915-1935
- 相关性 4/10 · novelty: `application`
- **摘要**: 本文研究在小样本政策评估中如何正式引入贝叶斯先验信息以提高推断效率。以哥伦比亚针对200家企业的出口促进项目为案例，评估算法的因果效应（如是否增加出口、出口多样性、出口值等）。作者从学术界、政策制定者及企业自身 elicitation 获得先验分布，并将其与频率学派估计结果进行对比。对于二值结果（如是否出口），频率学派估计已经较为精确，贝叶斯后验区间与标准置信区间几乎重叠。对于先验与数据一致的连续结果（如出口多样性），贝叶斯后验区间明显更窄，体现了先验信息的价值。对于噪声大的结果（如出口值），后验区间几乎没有从先验更新，表明数据信息量有限。文章展示了贝叶斯方法在小样本实验中的实际效用，并建议未来政策实验可将这些后验作为新先验。对您而言，本文是经济理论方向应用因果推断的案例，可与您熟悉的估计理论（如ATE估计、频率学派推断）进行对比，理解先验elicitation在实践中的操作与局限。
- **关键技术**: `Bayesian prior elicitation`, `Bayesian inference for impact evaluation`, `frequentist versus Bayesian comparison`, `confidence intervals vs posterior intervals`, `informative priors in small samples`
- **为什么对您有用**: 本文直接对接您的 secondary interest —— economic theory 中的应用因果推断，具体是政策评估（impact evaluation）。您武器库中的 estimation theory in causal inference（very_familiar）可以用于分析其频率学派部分的估计性质；同时，identification theory（moderately_familiar）可用于审视其因果识别假设（如无混淆、测量误差等）是否被充分讨论。本文未引入新方法，但在实践中展示了先验 elicitation 的完整流程，对您来说可作为入门案例，立即可理解并迁移至其他实验评估场景（如流行病学或发展经济学项目）。追评：立即可做——概念和工具均在武器库内。

### 6. [10.3982/ecta17951](https://doi.org/10.3982/ecta17951) — Landmines and Spatial Development
- **作者**: Giorgio Chiovelli, Stelios Michalopoulos, Elias Papaioannou
- **期刊/来源**: Econometrica
- **机构**: Universidad de Montevideo · Center for Economic and Policy Research · John Brown University · London Business School · London School of Economics and Political Science
- **分类**: vol 93 · issue 5 · pp 1739-1778
- 相关性 3/10 · novelty: `application`
- **摘要**: 本文研究莫桑比克地雷清除对地方经济发展的因果效应，estimand 为 demining 对夜间灯光（luminosity）及市场接入（market access）的影响。作者自建了地理编码的疑似污染区域与排雷操作面板数据集。Event-study 分析显示排雷后经济活动显著上升，而排雷前无趋势且误标区域无效应，支持排雷的因果解释。识别策略上，利用远离早期全国调查的"先前被视为安全区域"的地雷清除所引发的市场接入变化，构建 market-access IV 以分离直接与间接效应。政策模拟表明排雷的经济红利主要来自市场接入的间接效应，远超直接生产力提升，且优先疏通交通路线的排雷策略具有显著宏观收益。对您有用：本文提供了地理空间因果推断与 market-access IV 的完整应用范例，数据集与识别设计可直接作为经济理论中空间因果推断的参考案例。
- ⚠️ *摘要不完整，待重跑（`python -m research_news.rerun`）*
- **关键技术**: `event-study design`, `market-access instrumental variable`, `nighttime luminosity as economic proxy`, `spatial difference-in-differences`, `policy counterfactual simulation`
- **为什么对您有用**: 本文直接连接到经济理论中的因果推断应用（空间地理设定下的 market-access IV 与 event-study 识别）。您武器库中的 identification theory in causal inference 可以直接用来审视其 IV 的 exclusion restriction 与 monotonicity 假设在空间设定下的合理性，semiparametric theory 也可评估其 market-access 指标的函数形式假设。Follow-up 判断：立即可做——用 very_familiar 的因果识别理论工具即可对本文的 IV 策略进行 critique 或拓展分析。

### 7. [10.3982/ecta22741](https://doi.org/10.3982/ecta22741) — Women in Science. Lessons From the Baby Boom
- **作者**: Scott Kim, Petra Moser
- **期刊/来源**: Econometrica
- **机构**: University of Pennsylvania · Center for Economic and Policy Research
- **分类**: vol 93 · issue 5 · pp 1521-1560
- 相关性 2/10 · novelty: `application`
- **摘要**: 本文利用《美国男性科学家》(MoS 1956)传记数据与出版记录，以事件研究(event study)方法估计子女出生对女性科学家生产力的因果效应。首先描述母亲的生命周期生产力模式：其他科学家在30多岁达到峰值，母亲在此年龄段生产力下降，峰值推迟至40岁早期。进而通过双差分框架对比母亲与父亲、其他已婚科学家在婚姻前后生产力轨迹的差异，发现母亲生产力持续下降至子女学龄，父亲无变化。最终仅有27%的母亲获得终身教职，远低于父亲的48%和其他女性的46%。该研究是经济理论中应用因果推断的经典实证，其事件研究设计及纵向数据处理对您关注的因果推断（尤其是mediation与longitudinal设定中的处理效应时变分析）有直接参考价值。
- **关键技术**: `event study`, `difference-in-differences`, `life-cycle productivity analysis`, `biographical data linked with publications`
- **为什么对您有用**: 本文属经济理论应用因果工作的典型范例，事件研究设计与纵向匹配策略可直接迁移至您关注的因果推断子方向（如处理效应随时间的动态识别）。您已有的estimation theory工具（very_familiar中的causal inference估计理论）能轻松复现其核心分析，属于立即可做的网关阅读材料。

### 8. [10.3982/ecta22749](https://doi.org/10.3982/ecta22749) — Running Primary Deficits Forever in a Dynamically Efficient Economy: Feasibility and Optimality
- **作者**: Andrew B. Abel, Stavros Panageas
- **期刊/来源**: Econometrica
- **机构**: National Bureau of Economic Research · University of Pennsylvania · University of California, Los Angeles
- **分类**: vol 93 · issue 5 · pp 1601-1633
- 相关性 2/10
- **摘要**: 本文在随机动态效率经济体中研究政府债务可持续性问题。采用交叠世代模型（OLG），假设劳动增强型技术进步以常数增长率g增长，资本耐久性受随机冲击。主要识别参数为风险自由利率r_f与增长率g的关系。理论表明，当r_f = g时，债券与资本比率达到最大可持续值，且该比率同时最大化平衡增长路径上的人均效用。证明经济在此最大债务比率下仍保持动态效率。该结果挑战了传统“动态无效率才允许庞氏游戏”的直觉。对您而言，这是一个纯经济理论模型，可帮助理解宏观公共财政与动态效率的基本概念，但方法论上不直接涉及统计推断。
- **关键技术**: `overlapping-generations model`, `balanced growth path`, `risk-free interest rate`, `dynamic efficiency`, `debt rollover`, `stochastic durability shocks`
- **为什么对您有用**: 本文属于经济理论中的公共财政与动态效率子方向，是研究者secondary interests中‘economic theory (models)’的典型文献。作为入门阅读，本文理论性强但表述清晰，以OLG为基础框架，无需预先掌握动态随机一般均衡的复杂工具。然而，研究者的技术武器库（非参数统计、高维、U-statistics等）与本文的核心论证（确定性等价、随机贴现因子、布兰查德条件等）无直接交集，暂时无法基于本文提出可操作的后续统计问题。因此建议通读全文以拓展经济直觉，但不作为短期研究驱动。

### 9. [10.3982/ecta22113](https://doi.org/10.3982/ecta22113) — Privatizing Disability Insurance
- **作者**: Arthur Seibold, Sebastian Seitz, Sebastian Siegloch
- **期刊/来源**: Econometrica
- **机构**: Center for Economic and Policy Research · Ludwig-Maximilians-Universität München · Centre for European Economic Research · University of Manchester · University of Cologne
- **分类**: vol 93 · issue 5 · pp 1697-1737
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究公共残疾保险（DI）削减后私人保险市场的福利效应。利用德国一项取消部分公共DI的改革，结合一家大型保险公司的独特个体数据，分析公共DI削减对私人保险参保的挤出效应。发现挤出效应适中，私人保险参保不完全，且不存在逆向选择，而是吸引高收入、高教育、低残疾风险人群。通过揭示偏好方法估计个体对私人保险的支付意愿（保险估值），并进行福利分析。结果表明，部分依靠自愿私人市场提供DI可以改善福利，但分配公平考量可能仍需完全的公共DI强制覆盖。这篇论文对关注应用因果推断和政策福利分析的经济学者具有参考价值，其识别策略（改革外生性、差分法）和福利估算框架可直接迁移到类似的公共政策评估问题。
- **关键技术**: `difference-in-differences`, `revealed preference estimation`, `insurance valuation`, `crowding-out effect decomposition`, `adverse selection testing`
- **为什么对您有用**: 直接连接 secondary interest 中的 econ_theory 子方向（应用因果推断与政策评估）。论文使用改革作为外生冲击进行因果识别，属于 identification theory in causal inference 的典型应用，这一模块在您的武器库中为 very_familiar，因此阅读和批判性吸收其识别策略与福利分析方法立即可做。此外，其数据清理与市场均衡建模思路也可用于流行病学中的保险选择问题。

### 10. [10.3982/ecta20153](https://doi.org/10.3982/ecta20153) — Can Trade Policy Mitigate Climate Change?
- **作者**: Farid Farrokhi, Ahmad Lashkaripour
- **期刊/来源**: Econometrica
- **机构**: Boston College · Indiana University – Purdue University Indianapolis
- **分类**: vol 93 · issue 5 · pp 1561-1599
- 相关性 1/10 · novelty: `application`
- **摘要**: 本文研究贸易政策能否有效缓解气候变化中的搭便车问题。作者将一个包含全球碳供应链和气候外部性的框架嵌入多国多行业一般均衡贸易模型，推导了最优碳税和最优碳边境税的理论公式。量化分析表明：在现有关税基础上添加最优碳边境税几乎无效，仅能实现全球最优碳定价效力的3.4%；而采用气候俱乐部框架（即把边境税作为惩罚搭便车者的条件性工具），根据初始联盟构成的不同，可达成33%–68%的减排效果，且能确保普遍遵守从而维护自由贸易。本文属于经济理论中贸易政策与气候变化的交叉应用，模型构建和量化分析较为系统，对于关注该领域模型结构与政策量化方法的经济理论兴趣者有参考价值。但论文未涉及因果推断或统计估计方法，与研究者主要兴趣的方法论联系有限。
- **关键技术**: `General equilibrium trade model`, `Optimal carbon border tax`, `Climate club`, `Global supply chains of carbon`
- **为什么对您有用**: 本文属于secondary interest中的经济理论应用（贸易与气候变化交叉），提供了一般均衡模型的构造和量化评估范式，可作为经济理论方向的入门读物。但研究者武器库中缺乏一般均衡模型、结构估计等工具（暂不可做），且无因果推断方法，因此仅适合泛读了解领域概况，不适合立即展开深度研究工作。

### 11. [10.3982/ecta22257](https://doi.org/10.3982/ecta22257) — Non‐Stationary Search and Assortative Matching
- **作者**: Nicolas Bonneton, Christopher Sandmann
- **期刊/来源**: Econometrica
- **机构**: Vanderbilt University · London School of Economics and Political Science
- **分类**: vol 93 · issue 5 · pp 1635-1662
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究非平稳搜索匹配环境中的正向匹配（assortative matching）问题，假设 payoff 不可转移。非平稳性意味着代理人数量及其特征随时间内生演化。现有文献证明了在稳态下正向匹配成立的某些充分条件，但在非平稳环境中正向匹配可能失败，原因在于匹配前景恶化的风险。本文的主要贡献是推导了正向匹配所需的最弱充分条件；除了稳态条件外，还需要更理想的个体在 Arrow-Pratt 意义下具有更低的风险厌恶。这一结果揭示了风险态度在动态匹配中的关键作用。对于当前以方法和工具为焦点的读者而言，本文属于经济理论方向的入门级阅读，展示了微观经济模型的推理风格，但短期内难以直接迁移到因果推断或高维统计的工作中。
- **关键技术**: `search-and-matching model`, `non-transferable payoffs`, `Arrow-Pratt measure of risk aversion`, `non-stationary dynamics`
- **为什么对您有用**: 本文属于经济理论（匹配模型）方向，是您的次要兴趣点。由于您的技术武器库中缺乏搜索理论、动态规划及风险厌恶建模等核心工具，并且本文纯理论、无数据或因果识别结果，因此评估为暂不可做——需要先补充搜索模型和比较静态分析的基础知识。不过，若未来您参与劳动市场或婚姻市场等匹配相关的因果分析，本文的框架可能提供理论背景。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

