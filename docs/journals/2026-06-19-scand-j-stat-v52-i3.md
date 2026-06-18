# Scand. J. Stat. — Vol 52  Issue 3  ·  2026-06-19

- 共 11 篇 · Scandinavian Journal of Statistics
- 目录核对 ✅ 11 篇全部抓到（对照 OpenAlex 12 篇）

## 本期导览

> 自动生成：归纳本期主要主题与脉络，**不打分、不排名**。

本期论文大致聚成四条主线：半参数与非参数估计及降维（四篇）、假设检验与效应度量（三篇）、高维与重尾建模（两篇）、约束下的统计计算与实验设计（两篇）。半参数/非参数主线涉及局部散度回归、空间点过程带宽、条件尾指数降维及Fréchet稀疏降维；假设检验主线覆盖非参数效应联合推断、离散p值组合与函数型方差相关检验；高维主线聚焦众数因子模型与整值时间序列；计算与设计主线处理等式约束下的蒙特卡洛插补及分支拉丁超立方构造。

半参数与非参数降维主线在本期推进了估计目标的灵活性与高维协变量的可操作性。局部化Bregman散度回归将局部M-估计从似然/最小二乘推广至Bregman散度框架，推导了渐近正态性与一致性；空间点过程带宽选择则针对强度函数核估计，改编了plug-in与交叉验证技术以稳定偏差-方差权衡并校正边界效应。在降维侧，条件尾指数估计与Fréchet回归均直面高维协变量挑战：前者寻找使条件尾指数仅依赖其投影的低维子空间并证明一致性；后者对度量空间响应变量融合预测变量图结构，以凸优化与ADMM算法实现稀疏充分降维，给出变量选择相合性与收敛速率。

假设检验主线在检验的敏感度、适用分布与度量全面性上做了拓展。非参数效应度量将Mann-Whitney functional与distribution overlap index联合，基于联合渐近正态与Delta方法构建置信区域，其检验一致性区域远大于传统Wilcoxon检验；离散p值组合检验引入最小Wasserstein距离将离散分布映射至连续零分布，以最优gamma分布替代Fisher组合中的χ²，克服离散性导致的保守问题；函数型方差检验则用样条回扣核平滑与自归一化检验“无相关偏离”而非精确相等，具备oracle效率以避免过度敏感。

对因果推断与半参数效率方向，Semiparametric regression with localized Bregman divergence的局部M-估计与渐近分析框架可直接迁移至非参数nuisance函数估计；对高维与非参数降维方向，Sparse Fréchet sufficient dimension reduction与Dimension reduction for the conditional tail index分别从Fréchet回归与极值理论切入高维子空间提取，适合优先阅读。

## 非参数 / 半参数  *(nonparam_semipara, 4 篇)*

### 1. [10.1111/sjos.12789](https://doi.org/10.1111/sjos.12789) — Semiparametric regression with localized Bregman divergence
- **作者**: Hiroki Kosugi, Kanta Naito, Spiridon Penev
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Chiba University · Tohoku University · UNSW Sydney
- **分类**: vol 52 · issue 3 · pp 1330-1375
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文在半参数回归框架下引入局部化 Bregman 散度作为目标函数，替代传统的局部似然或最小二乘。模型基于广义线性模型的局部参数化，协变量和线性预测器结构允许在每一个拟合点使用核权重进行局部估计。作者推导了局部参数估计量和回归估计量的渐近正态性和一致性，并利用散度风险度量对不同估计量进行理论比较。进一步推广至多元多项式预测器，其中借助 Faa di Bruno 定理处理复合函数的导数展开。模拟和实际数据表明，该方法在灵活性和效率上优于标准局部似然估计。与您的半参数理论兴趣直接相关，尤其是局部 M-估计和渐近分析框架可迁移至您的 causal inference 中非参数 nuisance 函数的估计问题。文中对风险度量的比较方法也可能为您的效率理论工作提供新视角。
- **关键技术**: `local parametric model`, `Bregman divergence`, `semiparametric regression`, `generalized linear model`, `Faa di Bruno's theorem`, `divergence risk measure`
- **为什么对您有用**: 本文直接落点于您的 primary interest 中的半参数/非参数理论子方向，特别是局部估计的渐近行为分析。您的 very_familiar 武器库中的 nonparametric statistics 和 minimax bounds 可用来评估该估计量的收敛速率是否最优；moderately_familiar 中的 semiparametric theory 可以帮助您将 Bregman 散度思想推广至因果推断中的半参数效率界。立即可做：用您熟悉的非参数回归技术检验该方法的有限样本表现；中期可做：若能将局部 Bregman 散度与 cross-fitting / DML 结合，需先在 moderately_familiar 的 semiparametric theory 上提升对影响函数构造的熟练度。

### 2. [10.1111/sjos.12782](https://doi.org/10.1111/sjos.12782) — Bandwidth selection for kernel intensity estimators for spatial point processes
- **作者**: Bethany J. Macdonald, Tilman M. Davies, Martin L. Hazelton
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Otago
- **分类**: vol 52 · issue 3 · pp 1111-1137
- 相关性 7/10 · novelty: `minor`
- **摘要**: 该文研究空间点过程强度函数核估计的带宽选择问题。在常规非参数密度估计框架下，强度估计的精度高度依赖于核光滑参数（带宽），现有方法（如常用软件默认选项）在不同点格局下表现不稳定，易导致伪影或过度光滑。作者将经典多元密度估计中的plug-in方法和交叉验证技术进行改编，提出了两类新的带宽选择器（基于MISE渐近展开的plug-in规则和基于似然交叉验证的修正形式）。通过理论分析（AMISE渐近阶）和模拟实验，比较了多种情形的强度模式（Poisson过程、聚集过程、非齐次过程），新方法在偏差-方差权衡上表现更一致，且对边界效应具有更好的鲁棒性。文章还讨论了有限观测窗口下边界校正对带宽选择的影响。对您有用的点：该工作可直接类比于您熟悉的非参数统计中核密度带宽选择，但需针对空间点过程的结构（如强度函数与密度函数的差异、边缘效应）进行适配；若您关注统计计算方法，其plug-in和CV的数值实现可作为算法性能评估的对比基线。
- **关键技术**: `kernel intensity estimation`, `plug-in bandwidth selection`, `cross-validation bandwidth selection`, `spatial point process`, `boundary correction`
- **为什么对您有用**: 连接到您的非参数统计兴趣（核密度/强度估计的带宽选择），您熟悉非参数统计与minimax界，可从收敛速率角度验证其AMISE最优性是否达到渐近效率底线。由于空间点过程强度估计的非参数minimax速率已被刻画（取决于强度函数的Hölder光滑性与空间维度），本文的plug-in方法是否达到最优收敛阶是可用您的技术武器直接检验的问题（立即可做）。此外，该文涉及统计计算中的数值优化（带宽最小化），可视为算法比较的素材。

### 3. [10.1111/sjos.12792](https://doi.org/10.1111/sjos.12792) — Dimension reduction for the estimation of the conditional tail index
- **作者**: Laurent Gardes, Alexandre Podgorny
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Centre National de la Recherche Scientifique · Université de Strasbourg
- **分类**: vol 52 · issue 3 · pp 1444-1476
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文考虑重尾条件分布下，响应变量与多维协变量之间大值关系。在协变量维度较高时，直接估计条件尾指数变得困难。作者假设存在一个低维线性子空间，使得条件尾指数仅依赖于协变量在该子空间上的投影。提出了一种估计该降维子空间的方法，并证明了估计的一致性。进一步，利用该降维结果构建了条件尾指数的估计量，并证明了其一致性。通过模拟和实际数据验证了降维方法在条件尾指数估计中的优势。该方法对高维协变量下的极端分位数或尾指数估计提供了新的非参数工具。
- **关键技术**: `conditional tail index`, `sufficient dimension reduction (SDR)`, `linear subspace assumption`, `consistency proofs`, `heavy-tailed conditional distribution`
- **为什么对您有用**: 本文属于非参数降维与极值统计交叉，直接连接到研究者对非参数与半参数理论、高维统计的兴趣。研究者武器库中的非参数估计一致性技术（如核方法、M估计）可用于验证或扩展该文的降维估计理论。中期可做：若将降维思想推广到条件分位数处理效应估计，需先熟悉极值统计的渐近理论（如极值指数估计的收敛率），目前不在非常熟悉的武器中，但可通过学习极值统计文献补齐。

### 4. [10.1111/sjos.12791](https://doi.org/10.1111/sjos.12791) · [arXiv](https://arxiv.org/abs/2310.19114) — Sparse Fréchet sufficient dimension reduction with graphical structure among predictors
- **作者**: Jiaying Weng, Kai Tan, Cheng Wang, Zhou Yu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1422-1443
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 本文研究高维欧几里得预测变量下，响应变量为度量空间值（如概率分布、球面向量）的Fréchet回归的充分降维问题。现有Fréchet回归文献多假设预测变量维数固定，难以处理高维情形。作者提出一种融合预测变量图结构信息的稀疏充分降维方法，通过凸优化避免直接估计高维协方差矩阵的逆。算法上采用交替方向乘子法（ADMM）求解优化问题，适应大数据情景。理论上，在适当条件下证明了子空间估计的一致性以及变量选择的相合性，给出了收敛速率。模拟和真实数据表明方法在有限样本下表现良好。本文连接了非参数回归（Fréchet）与高维稀疏降维，其理论分析中使用的非参技巧与您非常熟悉的非参数极小化极大理论可以对比，验证所得速率是否最优。同时ADMM算法为统计计算提供了一个可实现的框架，与您的软件开发经验直接相关。
- **关键技术**: `Fréchet regression`, `Sufficient dimension reduction`, `Graphical structure`, `ADMM`, `Subspace estimation consistency`
- **为什么对您有用**: 本文涉及高维稀疏降维与非欧响应建模，直接对应您的非参数统计和高维渐近兴趣。您工具箱中“非参数极小化极大界”可用来检查论文子空间估计一致性的速率是否紧；ADMM算法部分可与您的“软件开发”经验结合，评估实际计算效率。这是一篇方法学论文，但需要先熟悉充分降维的基本框架，属于中期可做——需在“半参理论”或“M估计理论”上补充SDR领域的背景后再展开深度阅读。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.12783](https://doi.org/10.1111/sjos.12783) · [arXiv](https://arxiv.org/abs/2311.17564) — Combining stochastic tendency and distribution overlap towards improved nonparametric effect measures and inference
- **作者**: Jonas Beck, Patrick B. Langthaler, Arne C. Bathke
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1138-1175
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 本文提出将经典的Mann-Whitney functional（θ，衡量随机趋势）与新近提出的distribution overlap index（η，非参数离散度度量）结合，构建更全面的非参数效应度量框架。θ是常见U统计量，η可表达为分位数过程的泛函。作者推导了θ̂和η̂的联合渐近正态分布，并基于Delta方法构建置信区域。进一步，以该联合框架为基础提出一种新的假设检验，其一致性区域远大于Wilcoxon-Mann-Whitney检验，且在仅存在位置效应时保持竞争功效。相比于传统的综合检验（如Kolmogorov-Smirnov），所提检验在各种尺度与位置差异情景下功效显著提升。该效应度量具有直接的直观解释，便于应用解读。对您而言，本文直接连接数学统计中的假设检验与非参数理论，且所处理的U统计量是您非常熟悉的领域中的核心对象。
- **关键技术**: `Mann-Whitney functional`, `distribution overlap index`, `joint asymptotic distribution`, `quantile process`, `Delta method`, `confidence region`
- **为什么对您有用**: 本文专注于非参数效应度量与假设检验，直接对应您主兴趣中的“hypothesis testing”和“nonparametric theory”。其中Mann-Whitney U统计量是您武器库中非常熟悉的U统计量特例，而其联合渐近推断技术可被“非参数统计”与“更高阶U统计量的计算（树宽/张量收缩/einsum）”工具直接审视。Follow-up粗判：立即可做——您可用U统计量的einsum计算框架高效实现该方法的估计与检验，并可与经典WMW检验进行数值比较；中期可做——可探索将此联合效应度量扩展到因果推断中的分布处理效应（需适应混杂调整），但核心机制已在武器库内。

### 2. [10.1111/sjos.12787](https://doi.org/10.1111/sjos.12787) · [arXiv](https://arxiv.org/abs/2309.07692) — A minimum Wasserstein distance approach to Fisher's combination of independent, discrete <i>p</i>‐values
- **作者**: Gonzalo Contador, Zheyang Wu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1281-1300
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在离散分布下组合独立p值进行假设检验的设定中，传统连续近似（如χ²）因离散性导致保守。本文提出基于最小Wasserstein距离的离散检验统计量调整框架，将离散分布映射到最接近的连续零分布，从而统一解释了Lancaster的mid-p与mean-value χ²统计量作为特例。为克服Lancaster方法的保守性，作者进一步在给定分布族内对调整后统计量最小化Wasserstein距离，提出以最优gamma分布替代Fisher组合中传统的χ²分布作为零近似。新方法所得检验具有渐近一致性，在控制Type I误差的同时显著提升统计功效。对您有用：本文将Wasserstein距离引入离散p值组合的假设检验，为离散数据下的检验校准提供了新视角，直接关联您对hypothesis testing的兴趣。
- **关键技术**: `Wasserstein distance minimization`, `Fisher's combination of p-values`, `Lancaster's mid-p and mean-value chi-squared`, `discrete test statistic adjustment`, `optimal gamma null approximation`, `asymptotic consistency`
- **为什么对您有用**: 直接关联您 primary interest 中的 hypothesis testing 子方向，特别是离散数据下p值组合与检验校准问题。您武器库中的 minimax bounds for estimation problems 虽不直接针对此检验问题，但非参数统计与 M-estimation theory 可用于分析该 Wasserstein 最小化调整的渐近性质与功效界。follow-up 判断：中期可做——需先在 moderately_familiar 的 M-estimation theory 上长肌肉，以建立该 Wasserstein 调整估计量的渐近最优性与功效界理论。

### 3. [10.1111/sjos.12788](https://doi.org/10.1111/sjos.12788) — Testing relevant hypotheses in functional variance function via self‐normalization
- **作者**: Qirui Hu
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Shanghai University of Finance and Economics · Tsinghua University
- **分类**: vol 52 · issue 3 · pp 1301-1329
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文针对污染函数型数据中的方差函数，提出一种基于样条回扣核平滑（spline-backfitted kernel smoothing）与自归一化（self-normalization）的假设检验方法。传统检验关注精确相等，而该方法检验“无相关偏离”的原假设（例如两独立测量误差的方差函数是否几乎相等）。统计量适用于单样本、两样本以及单个或多个变点问题，且具有oracle效率，即基于观测数据的过程与基于真实轨迹的过程渐近不可区分。模拟研究和EEG数据分析展示了有限样本性能。文章的核心贡献在于将相关假设检验框架引入函数型方差分析，避免了过度敏感于微小偏差的经典检验。对您而言，该工作直接连接数学统计中的假设检验与非参数函数型数据领域，自归一化技术与oracle效率的理论分析可用您熟悉的非参数统计和高维渐近工具深入理解。
- **关键技术**: `spline-backfitted kernel smoothing`, `self-normalization`, `oracle efficiency`, `relevant hypothesis testing`, `functional variance function`
- **为什么对您有用**: 本文直接涉及数学统计中的假设检验（您的主要兴趣），且聚焦于函数型数据的非参数检验，属于非参数/半参数理论的具体应用。您非常熟悉的非参数统计和minimax理论可直接用于分析其oracle效率及自归一化方法的渐近性质。**立即可做**：利用您对非参数渐近和核方法的熟练掌握，可以评估该检验方法的幂函数和最优性，甚至尝试将其相关假设思路推广到其他函数型参数的检验问题。

## 统计计算 / 算法  *(stat_computing, 1 篇)*

### 1. [10.1111/sjos.12790](https://doi.org/10.1111/sjos.12790) · [arXiv](https://arxiv.org/abs/2504.18377) — Statistical disaggregation—A Monte Carlo approach for imputation under constraints
- **作者**: Shenggang Hu, Hongsheng Dai, Fanlin Meng, Louis Aslett, Murray Pollock, Gareth O. Roberts
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 3 · pp 1376-1421
- 相关性 6/10
- **摘要**: 该论文研究了等式约束模型下的统计分解问题，目标是根据低分辨率数据（如日用电量）恢复高分辨率（如每小时）的读数，约束条件要求各子单位之和等于总量。由于约束导致联合分布不可解析处理，传统拒绝采样在约束概率质量为零时失效。作者提出了一种基于Langevin扩散和拒绝采样的混合蒙特卡洛算法，能够在任意约束（包括非线性）下从目标分布精确采样，对线性约束可实现exact sampling，且天然适用于多模态分布。算法通过将约束嵌入扩散过程的漂移项中，再结合接受-拒绝步骤校正离散化误差，保证了遍历性。在真实电力消耗数据集上展示了相比直接插值/无条件采样方法更优的插值精度和不确定性量化。该工作对统计计算中约束采样问题提供了新工具，特别适用于需要精确边际分布的高维分解（disaggregation）任务。
- **关键技术**: `Langevin diffusion`, `rejection sampling`, `equality-constrained sampling`, `constrained Monte Carlo`, `exact sampling under linear constraints`, `statistical disaggregation`
- **为什么对您有用**: 本文属于统计计算（约束采样）方向，与您对数值方法和算法的兴趣直接吻合。您非常熟悉的重采样/扩散技巧和软件实现能力可用来复现或扩展该算法（例如将其与高阶U统计量的张量收缩框架结合，处理更复杂的约束图结构）。**立即可做**：您可以用常用的MCMC诊断工具评估该算法在您的因果推断（如IV纵向数据中的确定性约束）中的实际表现，无需额外学习新武器。

## 其他  *(other, 3 篇)*

### 1. [10.1111/sjos.12786](https://doi.org/10.1111/sjos.12786) — Enhanced branching Latin hypercube design and its application in automatic algorithm configuration
- **作者**: Bing Wen, Sumin Wang, Fasheng Sun
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Northeast Normal University · Hebei University of Technology
- **分类**: vol 52 · issue 3 · pp 1239-1280
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 针对包含分支和嵌套因子的实验设计问题，本文定义了增强型分支拉丁超立方设计（EBLHD），并提出了基于正交数组和切片拉丁超立方设计的多种构造方法。这些方法能够同时保证嵌套因子和共享因子的低维分层性质，并控制因子之间的列相关性。设计的大小可根据实验预算与估计精度的权衡灵活选择。仿真结果表明，所提设计在多种度量指标和估计精度上显著优于现有方法。此外，本文将该设计应用于自动算法配置的初始化阶段，展示了其实用价值。该论文的主要贡献在于实验设计领域的新构造方法，与您的核心兴趣（因果推断、高维统计等）直接关联较弱。
- **关键技术**: `orthogonal arrays`, `sliced Latin hypercube designs`, `branching Latin hypercube`, `space-filling design`, `column correlation`
- **为什么对您有用**: 该论文专注于实验设计的新构造，而非因果推断或高维统计。您的技术武器库中无直接可攻击的实验设计工具（如最优设计理论），目前暂不可做。若未来涉及嵌套因子实验的统计推断问题，此文的设计可能作为预实验采样方案被参考。

### 2. [10.1111/sjos.12785](https://doi.org/10.1111/sjos.12785) — Mode‐adaptive factor models
- **作者**: Tao Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: University of Victoria
- **分类**: vol 52 · issue 3 · pp 1206-1238
- 相关性 5/10 · novelty: `new_method`
- **摘要**: 该论文提出自适应众数因子模型（MAFM），用于高维面板数据的稳健因子分析。传统因子模型基于最小二乘与PCA等价性以均值估计为中心，在重尾、偏态分布下性能退化。MAFM 以众数替代均值捕捉中心趋势，构建迭代众数回归算法（融入EM过程）实现参数估计，并证明无矩条件下估计量的收敛性。理论贡献包括提出模式信息准则一致选择因子数、给出数据依赖带宽选择方法。模拟显示MAFM在多种非正态分布下优于传统方法，宏观经济预测应用进一步验证其实用性。对您而言，该工作在高维统计框架下提供了一种避开矩条件的新工具，武器库中的 high-dimensional asymptotics 可直接用于理解其渐近理论，且立即可读。
- **关键技术**: `mode regression`, `iterative mode regression algorithm`, `EM algorithm`, `mode information criterion`, `bandwidth selection`, `factor model PCA equivalence`
- **为什么对您有用**: 直接对应您的高维统计兴趣中的因子分析方法，尤其适用于金融宏观经济数据常见的重尾分布。武器库中的 high-dimensional asymptotics 可用来验证其收敛速度与已有的RMT结果是否可比。立即可读，重点理解其迭代算法设计，后续可考虑将众数估计思想迁移至因果推断中的稳健IV估计或高维敏感性分析。

### 3. [10.1111/sjos.12784](https://doi.org/10.1111/sjos.12784) — A unifying class of compound Poisson integer‐valued ARMA and GARCH models
- **作者**: Johannes Bracher, Barbora Němcová
- **期刊/来源**: Scandinavian Journal of Statistics
- **机构**: Karlsruhe Institute of Technology · Heidelberg Institute for Theoretical Studies
- **分类**: vol 52 · issue 3 · pp 1176-1205
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 本文提出了一类新的广义整数值 ARMA（GINARMA）模型，将以往分离研究的 compound Poisson INAR 与 INGARCH 计数时间序列模型统一在同一框架下。核心设定是依赖 compound Poisson thinning 操作的离散值随机过程，并重点研究了平行于 INGARCH(p,q) 扩展的广义 INAR(p) 模型。理论部分证明了该类过程的平稳性与几何遍历性；推断方面给出了 MLE、Gaussian quasi-likelihood 与矩估计，以及区分特定子类的 likelihood ratio test。模型可自然解释为随机流行病过程，并在 Bavaria 地区麻疹与腮腺炎周度数据上做了实证对比。对您而言，本文提供了流行病学计数数据的建模与推断范式，但方法学 novelty 限于现有离散值时间序列工具的统一与扩展。
- **关键技术**: `compound Poisson thinning`, `integer-valued ARMA (INARMA)`, `integer-valued GARCH (INGARCH)`, `geometric ergodicity`, `Gaussian quasi-likelihood`, `likelihood ratio test`
- **为什么对您有用**: 本文属于流行病学方向的实证应用与现有模型统一，连接到 epidemiology 的计数数据集与因果/推断前端的建模环节，但未涉及您 primary interest 中的 semiparametric efficiency 或 causal identification。武器库中 very_familiar 的 M-estimation theory 可直接审视其 quasi-likelihood 与矩估计的渐近性质，但核心的离散值时间序列 thinning 机制不在您当前关注的高维/半参/因果体系内。follow-up 判断：**暂不可做**——若要从效率理论或高维视角切入计数时间序列，需先补离散值随机过程的遍历性与 thinning 机制（武器库缺此核心机器），且本文本身更偏统一与实证而非新理论。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

