# Scand. J. Stat. — Vol 52  Issue 4  ·  2026-05-21

- 共 27 篇 · Scandinavian Journal of Statistics

## 因果推断  *(causal_inference, 2 篇)*

### 1. [10.1111/sjos.70002](https://doi.org/10.1111/sjos.70002) — Nonparametric estimation of path‐specific effects in the presence of nonignorable missing covariates
- **作者**: Jiawei Shan, Ting Wang, Wei Li, Chunrong Ai
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1556-1593
- 相关性 9/10 · novelty: `new_method`
- **摘要**: 在多中介变量的因果中介分析中，目标是估计路径特异性效应(PSE)以分离通过特定中介的因果路径；关键假设包括非忽略缺失机制与shadow variable的可及性。作者首先将PSE表达为观测数据函数以建立identification，再利用shadow variable证明相关nuisance functions可通过序列优化问题唯一确定，从而绕过参数化缺失模型假设。估计方面提出sieve-based regression imputation，建立所提估计量的大样本理论（一致性、渐近正态性），并提供PSE的推断方法。实证应用于NHANES数据集，研究血脂异常与肥胖在2型糖尿病至心血管疾病路径中的中介角色。对您有用：该工作将shadow variable识别策略引入中介分析的nonignorable missing设定，结合sieve M-estimation的大样本理论，直接关联您在causal inference (mediation)与semiparametric theory方面的兴趣，且sieve回归插补的渐近理论细节可迁移至其他半参数缺失数据问题。
- **关键技术**: `path-specific effect`, `shadow variable identification`, `sieve-based regression imputation`, `nonignorable missing data`, `sequential optimization for nuisance functions`, `mediation analysis`
- **为什么对您有用**: 直接推进causal inference中mediation的nonparametric估计理论，且shadow variable + sieve estimation的组合对您在semiparametric theory和efficiency方面的研究有方法迁移价值；NHANES数据集对epidemiology应用也有参考意义。

### 2. [10.1111/sjos.70001](https://doi.org/10.1111/sjos.70001) — Variable importance measures for heterogeneous treatment effects with survival outcome
- **作者**: Simon Christoffer Ziersen, Torben Martinussen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1505-1555
- 相关性 8/10 · novelty: `new_method`
- **摘要**: 在生存分析设定下（右删失时间-事件结局），本文将 Hines et al. (2022) 的处理效应变量重要性度量（TE-VIM）扩展至两种 CATE 定义：基于生存函数的 CATE 和基于 RMST 的 CATE，目标参数为各协变量对 CATE 方差的边际贡献。核心估计量基于半参数效率理论构造，利用 efficient influence function 导出 one-step 估计量，并在交叉拟合下给出估计量渐近线性的正则条件。此外，本文新提出基于 CATE 的最佳偏线性投影（best partially linear projection）的处理效应异质性度量，并给出相应的半参数有效估计量。模拟与两个真实数据示例（流行病学队列场景）验证了有限样本表现。对您有用：该文将半参数效率理论（您的核心兴趣）与因果推断中的 CATE 异质性度量结合，且生存结局设定在流行病学应用中极为常见，方法可直接迁移。
- **关键技术**: `semiparametric efficiency theory`, `efficient influence function`, `one-step estimation`, `cross-fitting`, `CATE variable importance`, `partially linear projection`, `RMST`
- **为什么对您有用**: 直接结合您的两个核心兴趣——因果推断（CATE 异质性）与半参数效率理论（influence function / 渐近线性），且生存结局设定对流行病学应用（secondary interest）有直接迁移价值。

## 高维统计 / 随机矩阵  *(high_dim_rmt, 2 篇)*

### 1. [10.1111/sjos.70028](https://doi.org/10.1111/sjos.70028) — A non‐asymptotic analysis of the single component PLS regression
- **作者**: Luca Castelli, Irène Gannaz, Clément Marteau
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2314-2351
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文在高维回归设定下研究偏最小二乘（PLS）单成分情形的预测理论性质，目标是在正则化条件下给出预测二次损失的非渐近上界。作者首先对首个 PLS 成分施加初步正则化，推导出以高概率成立的预测误差非渐近上界。随后将分析扩展至稀疏 PLS（sparse PLS），在设计矩阵满足限制特征值（RE）条件的额外约束下，证明了其预测误差上界与 Lasso 算法达到的速率同阶。核心结论是正则化单成分 PLS 及稀疏 PLS 在高维下具有与 Lasso 相当的预测性能，但稀疏 PLS 需要更强的 RE 条件。对您有用：此文提供了高维线性回归中 PLS 的非渐近分析，其有限样本界与 RE 条件的处理方式可直接迁移至您对高维统计理论（尤其是高维估计量收敛率与正则条件）的理解中。
- **关键技术**: `Partial Least Squares`, `non-asymptotic bound`, `restricted eigenvalue condition`, `sparse PLS`, `high-dimensional prediction`
- **为什么对您有用**: 本文属于高维统计理论范畴，给出了 PLS 的非渐近界与 RE 条件分析，对您关注的高维统计（收敛率与假设条件）有直接参考价值，尽管不涉及 RMT。

### 2. [10.1111/sjos.70026](https://doi.org/10.1111/sjos.70026) — Estimation of the number of principal components in high‐dimensional multivariate extremes
- **作者**: Lucas Butsch, Vicky Fasen‐Hartmann
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2270-2313
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 在高维多元极值（regularly varying random vectors）设定下，目标是估计角测度（angular measure）经验协方差矩阵在 spiked covariance 结构下的显著主成分个数。作者提出 AIC 和 BIC 信息准则来定位 spiked eigenvalue，以确定主成分数。在固定维度下，证明 AIC 不一致而 BIC 弱一致；在高维场景（p→∞）下，利用随机矩阵理论（RMT）方法，推导出保证 AIC 和 BIC 一致性的充分条件。模拟与降水数据验证了理论结果。对您有用：直接关联您的高维统计与 RMT 兴趣，展示了 RMT 在极值统计 spiked model 模型选择一致性判定中的具体应用与理论推导。
- **关键技术**: `spiked covariance model`, `random matrix theory`, `model selection consistency`, `angular measure`, `multivariate extremes`, `information criteria (AIC/BIC)`
- **为什么对您有用**: 直接关联您的高维统计与 RMT 兴趣，展示了 RMT 工具在极值统计 spiked model 模型选择一致性判定中的具体应用与理论推导。

## 非参数 / 半参数  *(nonparam_semipara, 6 篇)*

### 1. [10.1111/sjos.70009](https://doi.org/10.1111/sjos.70009) — Inference on data with both multiplicative and additive measurement errors
- **作者**: Yuxiang Zong, Yinfu Liu, Yanyuan Ma, Ingrid Van Keilegom
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1763-1785
- 相关性 7/10 · novelty: `new_theory`
- **摘要**: 在同时包含乘性与加性测量误差的设定下，本文研究误差方差的识别、估计与假设检验问题。作者首先建立模型可识别性，提出基于矩的误差方差估计量并推导其一致性与渐近正态性；进而构造检验统计量以判断两类误差是否存在，并发展基于似然的密度逼近方法。在线性回归中，结合 Regression Calibration 与 SIMEX 修正参数估计，模拟与实证验证了方法有效性。该文对您在数学统计（假设检验）与半参数理论方面的兴趣有直接参考价值，且测量误差修正方法可迁移至因果推断中处理混杂或处理变量的测量误差问题。
- **关键技术**: `moment-based estimator`, `measurement error model`, `asymptotic normality`, `hypothesis testing`, `Regression Calibration`, `SIMEX`
- **为什么对您有用**: 涉及数学统计中的假设检验与渐近分布推导，且测量误差修正是因果推断中处理变量/混杂测量误差的基础工具，方法可迁移至流行病学等应用场景。

### 2. [10.1111/sjos.70004](https://doi.org/10.1111/sjos.70004) — Smooth backfitting for additive hazard rates
- **作者**: Stephan M. Bischofberger, Munir Hiabu, Enno Mammen, Jens Perch Nielsen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1625-1669
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文将原始回归设定下的 smooth backfitting 推广至生存分析中加性 hazard 模型，estimand 为各加性分量 hazard 函数，允许右删失与截断（常见于医学队列与精算准备金）。核心机制是将数据投影到具有光滑加性分量的多元 hazard 函数空间，所得估计量即为该投影下的最近非参数加性拟合；即使真实 hazard 非加性，估计量仍有明确含义——这是与经典加性结构估计器（如 Buja-Hastie-Tibshirani backfitting）的关键区别。全文给出估计量的完整渐近理论（逐分量收敛速率与联合渐近分布），并提出可实际计算的实现方案。模拟显示有限样本表现良好。对您有用：投影视角下的 smooth backfitting 为非参数加性模型提供了 misspecification-robust 的估计框架，与您关注的 semiparametric theory 及 efficiency（投影即最近拟合）直接相关，且 hazard + 删失/截断设定可迁移至流行病学队列的因果推断场景。
- **关键技术**: `smooth backfitting`, `additive hazard model`, `projection estimation`, `nonparametric smoothing`, `censoring and truncation`
- **为什么对您有用**: 投影式 smooth backfitting 在 misspecification 下仍有明确估计目标，与您 primary interest 中 semiparametric/nonparametric theory 及 efficiency 的投影思想直接呼应；hazard + 删失/截断设定可迁移至流行病学队列的因果推断应用。

### 3. [10.1111/sjos.70007](https://doi.org/10.1111/sjos.70007) — A Donsker and Glivenko‐Cantelli theorem for random measures linked to extreme value theory
- **作者**: B. Bobbia, C. Dombry, D. Varron
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1708-1734
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究一类在给定外生随机现象条件下、与经验测度具有相似性质的随机点测度，探讨其 Glivenko-Cantelli 和 Donsker 定理的适用性。作者证明了在常规的一致熵条件（uniform entropy numbers）下，足以推导出这两类极限定理，并进一步证明了 Bootstrap Donsker 定理。核心技术工具涉及经验过程理论、函数类的熵界控制以及条件经验过程的弱收敛。主要理论结果为极端值理论和最近邻规则中的应用提供了严格的渐近保证。对您有用：该文对条件经验过程 Donsker 定理的严格推导，直接为半参数/非参数理论中条件影响函数的渐近正态性证明提供了关键的数学工具。
- **关键技术**: `empirical process theory`, `Donsker theorem`, `uniform entropy numbers`, `bootstrap consistency`, `conditional point measures`
- **为什么对您有用**: 本文属于数学统计与经验过程理论的核心工作，直接关联您 primary interest 中的 semiparametric and nonparametric theory；其关于条件经验测度的 Donsker 定理和 Bootstrap 结果，是推导半参数有效影响函数渐近性质的基础工具。

### 4. [10.1111/sjos.70011](https://doi.org/10.1111/sjos.70011) — Nonparametric inference for Poisson‐Laguerre tessellations
- **作者**: Thomas van der Jagt, Geurt Jongbloed, Martina Vittorietti
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1816-1851
- 相关性 3/10 · novelty: `new_theory`
- **摘要**: 本文研究 R^d 中 Poisson-Laguerre 镶嵌的非参数推断问题，目标量是生成点到达时间的分布函数 F，该函数唯一确定底层 Poisson 过程的强度测度。作者提出两个仅依赖非空细胞生成点及对应细胞的非参数估计量，在观测窗口无界扩张至全空间条件下证明了强一致性。此外考虑了体视学（stereology）设定：仅观测低维截面镶嵌时，估计高维 Poisson-Laguerre 镶嵌对应的分布函数。该工作属于随机几何 / 空间统计的非参数估计，与您关注的半参数效率理论、influence function 框架无直接交集，但体视学从低维截面推断高维参数的 identification 思路可类比因果推断中 latent variable 的 identification 问题。
- **关键技术**: `Poisson-Laguerre tessellation`, `nonparametric distribution estimation`, `strong consistency under increasing domain`, `stereological inference`, `Poisson point process intensity measure`
- **为什么对您有用**: 与您 primary interest 的非参数/半参数理论交集有限——本文无效率界、influence function 或收敛率结果；体视学从截面推断高维参数的 identification 结构可作类比参考，但整体偏随机几何方向，直接迁移价值不高。

### 5. [10.1111/sjos.70010](https://doi.org/10.1111/sjos.70010) — Distorted distributions and ROC curves
- **作者**: Marco Capaldo, Jorge M. Arevalillo, Jorge Navarro
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1786-1815
- 相关性 2/10 · novelty: `new_theory`
- **摘要**: 本文在 ROC 曲线与 ordinal dominance (OD) 曲线基础上构造新的 distortion functions，将其解释为相对随机变量的累积分布函数，从而刻画多种随机序与老化性质。通过 distortion 视角建立 ROC/OD 与 Lorenz 曲线、Gini 指数的联系，并基于 partial AUC 定义进一步 distortion，揭示其与偏态模型及均衡分布的对应关系。实证部分采用 ROC 曲线的 semiparametric 估计（sieve/binomial likelihood 类方法）在多个数据集上展示 distortion 方法的应用。核心贡献在于概率/分布论层面的新刻画，semiparametric 估计仅为工具性使用，未涉及效率界或 debiased 理论。对您而言，Lorenz/Gini 联系可作为经济理论中不平等测度的概率结构参考，但整体与您关注的 semiparametric efficiency / causal inference 距离较远。
- **关键技术**: `distortion functions`, `ROC curve semiparametric estimation`, `stochastic orders`, `Lorenz curve and Gini index`, `partial AUC`, `equilibrium distribution`
- **为什么对您有用**: Lorenz 曲线与 Gini 指数的 distortion 刻画可为经济理论中不平等测度提供概率结构视角，但论文核心是分布论/随机序，与您关注的 semiparametric efficiency bounds、causal inference 等方向重叠有限。

### 6. [10.1111/sjos.70020](https://doi.org/10.1111/sjos.70020) — Combining probability and non‐probability samples using semi‐parametric quantile regression and a nonparametric estimator of the participation probability
- **作者**: Emily Berg, Sixia Chen, Cindy Yu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2128-2151
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在概率样本与非概率样本数据整合的设定下，目标是在选择偏差存在时对总体参数进行有效估计，传统方法依赖参数模型假设。本文提出基于半参数分位数回归的 Mass-imputation 估计量，放松了对结果模型的参数假设，增强了对异常值的鲁棒性。进一步，作者提出结合非参数参与概率估计的 doubly-robust (DR) 估计量，仅需参与概率模型或结果模型之一正确指定即可保证一致性。理论部分建立了所提估计量的渐近正态性并推导了方差估计量。模拟与实证表明，在模型误设下所提方法显著优于现有参数方法。对您有用：该文将半参数/非参数理论应用于选择偏差纠正，其 DR 框架与非参数倾向得分估计的结合，可直接迁移至因果推断中处理不可忽略缺失数据或混杂校正的场景。
- **关键技术**: `semi-parametric quantile regression`, `doubly robust estimation`, `mass imputation`, `nonparametric propensity score`, `data integration`, `selection bias correction`
- **为什么对您有用**: 直接关联您 primary interest 中的 semiparametric & nonparametric theory 和 efficiency theory (doubly robust)；其处理非概率样本选择偏差的框架与因果推断中不可忽略缺失数据/混杂校正高度同构，方法可迁移。

## 效率理论 / Debiased ML  *(efficiency_dml, 2 篇)*

### 1. [10.1111/sjos.70003](https://doi.org/10.1111/sjos.70003) — Stein's method of moments
- **作者**: Bruno Ebner, Adrian Fischer, Robert E. Gaunt, Babette Picker, Yvik Swan
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1594-1624
- 相关性 6/10 · novelty: `new_method`
- **摘要**: 本文在严平稳遍历过程设定下，基于 Stein 算子对概率分布的微分刻画，提出边际参数点估计新框架——Stein 矩估计（SMOM）。SMOM 估计量具有相合性与渐近正态性；得益于算子的简单形式，在伪 MLE 需数值优化的场景下，SMOM 可直接给出显式估计量。该方法允许使用大类别检验函数以改进传统矩估计；在 i.i.d. 设定下，通过选取数据依赖的检验函数，可构造出达到 Cramer-Rao 下界的渐近有效估计量，且存在一列显式 SMOM 估计量收敛至 MLE。模拟表明 SMOM 在偏差和 MSE 上与 MLE 具有竞争力。该工作将 Stein 方法与渐近效率理论结合，为您在效率理论（渐近有效估计构造）和统计计算（显式计算避免数值优化）方向提供了新视角。
- **关键技术**: `Stein operator characterization`, `asymptotically efficient estimation`, `method of moments`, `data-dependent test functions`, `explicit estimation`
- **为什么对您有用**: 直接关联您在效率理论（通过数据依赖的检验函数构造渐近有效估计、逼近 MLE）和统计计算（显式估计避免数值优化）方向的兴趣，其构造渐近有效估计的思路具有方法论迁移价值。

### 2. [10.1111/sjos.70022](https://doi.org/10.1111/sjos.70022) — Subsampled One‐Step Estimation for Fast Statistical Inference
- **作者**: Miaomiao Su, Ruoyu Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2187-2208
- 相关性 0/10 · novelty: `sharper_rate`
- **摘要**: 在大规模数据下，传统子抽样估计器的收敛速率为 n^{-1/2}（n 为子样本量）而非 N^{-1/2}（N 为全样本量），导致估计效率严重损失。本文提出 subsampled one-step (SOS) 估计器，利用子抽样估计器与全数据估计器的渐近展开进行一步 Newton-type 更新，将收敛速率从 n^{-1/2} 提升至 N^{-1/2}。作者建立了 SOS 估计器的渐近分布理论——一般情形下可非正态，并据此构造置信区间；当 n 以适当速率趋于无穷时，SOS 估计器渐近正态且与全数据估计器等价。该方法将经典 one-step estimation 思想从半参数效率理论迁移至计算受限场景，计算开销接近均匀子抽样而估计效率接近全数据估计。对您在效率理论（one-step estimation / influence function）与统计计算交叉方向的研究有直接参考价值，尤其是如何在计算约束下恢复 N^{-1/2}-CAN 性质的技术路线。
- **关键技术**: `one-step estimation`, `asymptotic expansion`, `subsampling`, `efficient influence function`, `N^{-1/2}-CAN`, `non-normal asymptotic distribution`
- **为什么对您有用**: 直接连接您 primary interest 中的效率理论（one-step estimation / semiparametric efficiency）与统计计算：展示了如何在计算受限场景下通过一步更新恢复 N^{-1/2} 收敛速率，思路可迁移至 debiased ML / cross-fitting 等高维半参数推断中的计算加速问题。

## 数理统计 / 假设检验  *(hypothesis_testing, 3 篇)*

### 1. [10.1111/sjos.70013](https://doi.org/10.1111/sjos.70013) — Improved small‐sample inference for functions of parameters in the k$$ k $$‐sample multinomial problem
- **作者**: Michael C. Sachs, Erin E. Gabriel, Michael P. Fay
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1881-1898
- 相关性 7/10 · novelty: `new_method`
- **摘要**: 在 k-样本多项分布设定下，目标是多项概率的实值连续函数（如 ATE 的离散化版本）的推断；当函数在真实参数处不可微或样本量小时，非参数 bootstrap 与 delta method 方差估计表现不佳。作者提出一种精确推断方法，证明其精确 p 值严格控制 I 类错误率，对应置信区间至少达到名义覆盖概率。由于精确计算的组合爆炸问题，进一步提出 Monte Carlo 实现来近似精确 p 值与置信区间，并证明近似在迭代次数上的一致性。方法适用于任意样本数与类别数下多项概率的任意实值连续函数，不要求可微性。对您有用：直接关联 hypothesis testing 与 mathematical statistics 兴趣，为小样本/非可微参数函数提供比 delta method 更严格的有限样本保证，可迁移至因果推断中离散处理/结果的敏感度分析场景。
- **关键技术**: `exact test`, `multinomial parameters`, `nondifferentiable functions`, `Monte Carlo p-value`, `small-sample inference`, `type I error control`
- **为什么对您有用**: 直接关联 hypothesis testing 与 mathematical statistics 兴趣；为小样本/非可微参数函数提供有限样本精确推断，可迁移至因果推断中离散处理/结果的敏感度分析或 mediation 场景。

### 2. [10.1111/sjos.70019](https://doi.org/10.1111/sjos.70019) — Asymptotic distribution‐free tests related to maximum mean discrepancy
- **作者**: Kai Xu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2110-2127
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在多变量两样本拟合优度检验设定下，针对最大均值差异（MMD）零分布依赖底层分布且需昂贵置换检验的问题，本文提出基于特征核均值相等性的组合概率检验。所提检验被证明是渐近分布无关的，从而具有已知临界值，避免了计算密集的重抽样过程。在特征核二阶矩存在的正则条件下，该检验对所有固定备择假设具有相合性。局部功效分析进一步表明，在 n^{-1/2} 邻域内该检验具有非平凡功效。该方法在仿真和基因表达数据中展现了计算与功效优势；对您有用之处在于，MMD 本质为退化 U 统计量，本文绕过置换法实现渐近分布无关的思路，为您研究非参数假设检验与高阶 U 统计量渐近理论提供了可迁移的计算与理论视角。
- **关键技术**: `maximum mean discrepancy`, `combined probability test`, `characteristic kernel`, `asymptotically distribution-free test`, `local power analysis`
- **为什么对您有用**: 直接关联您在假设检验与非参数理论方面的兴趣：MMD 本质上是退化 U 统计量，本文通过组合概率检验绕过置换法实现渐近分布无关，为高维/非参数检验的计算与理论提供了一个可迁移的新思路。

### 3. [10.1111/sjos.70017](https://doi.org/10.1111/sjos.70017) — False selection rate control in mixture models
- **作者**: Ariane Marandon, Tabea Rebafka, Etienne Roquain, Nataliya Sokolovska
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2014-2060
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在无监督混合模型框架下，本文研究带弃权选项（abstention）的聚类问题，目标是在仅对部分样本做分类时控制错误选择率（FSR）不超过预设水平 α。作者提出一种 plug-in 程序以选择分类阈值，并给出 FSR 偏离目标水平的理论分析，量化了显式的余项。为改善有限样本表现，进一步发展了 Bootstrap 版本的程序，数值实验验证了其校准 FSR 的有效性。理论结果提供了 FSR 控制的非渐近保证，Bootstrap 方法增强了实用性。对您有用：该工作将多重检验中的 FSR 控制思想引入无监督聚类，属于您 primary interest 中的“假设检验”子方向，其理论余项推导和 Bootstrap 校准技术可为您在检验与选择问题上的研究提供参考。
- **关键技术**: `False selection rate`, `mixture model clustering`, `abstention option`, `plug-in procedure`, `bootstrap calibration`, `non-asymptotic deviation bounds`
- **为什么对您有用**: 本文将多重检验中的错误率控制（FSR）引入无监督聚类，属于您 primary interest 中的“假设检验”子方向；其非渐近理论余项推导和 Bootstrap 校准方法对研究选择与检验问题有直接参考价值。

## 统计计算 / 算法  *(stat_computing, 2 篇)*

### 1. [10.1111/sjos.70021](https://doi.org/10.1111/sjos.70021) — Projection‐based estimators for matrix/tensor‐valued data
- **作者**: Joni Virta, Stanislav Nagy, Klaus Nordhausen
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2152-2186
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文提出一种基于随机投影的通用框架，将多元估计量推广至矩阵与张量数据。核心机制为：对张量进行随机投影以消除部分维度，在每个投影上计算传统多元估计量，最终取所有投影估计量的均值作为联合估计。在基础情形下该估计量具有闭式解，且部分特例与现有方法等价。理论方面，在弱正则条件下证明了估计量的一致性，并指出只要投影数量以超线性于样本量 n 的速率增长，即可保留渐近正态性。实证表明该方法在分类成分提取与充分降维中表现优异，并在降维中实现了有效估计。这对您有用：直接呼应您对统计计算（矩阵/张量算法）的兴趣，提供了一种计算友好且理论完备的张量估计通用范式，其渐近正态性结论也可迁移至高维推断中的张量协变量处理。
- **关键技术**: `random projection`, `tensor-valued data`, `limiting normality`, `sufficient dimension reduction`, `averaging projected estimates`
- **为什么对您有用**: 直接契合您在统计计算中对矩阵/张量数值方法的兴趣；该框架通过随机投影实现张量估计，计算友好且具备渐近正态性，可为高维统计或因果推断中处理张量协变量提供可迁移的算法范式与理论工具。

### 2. [10.1111/sjos.70018](https://doi.org/10.1111/sjos.70018) — Spectral analysis for the inference of noisy Hawkes processes
- **作者**: Anna Bonnet, Felix Cheysson, Miguel Martinez Herrera, Maxime Sangnier
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2061-2109
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 在带噪声的 Hawkes 过程设定下，观测数据是真实 Hawkes 过程与独立 Poisson 过程的不可区分叠加，目标是同时估计两过程的参数。传统似然方法在此情形下不可行或计算代价高昂，本文基于过程的二阶性质的谱分析提出新的估计程序。理论贡献包括证明模型可识别性的充分条件（主要针对指数核，也探讨了其他核类型）。提出最大化谱对数似然估计量，无需知道每个观测时间的来源，且在估计两个过程时表现准确。对您而言，这种处理“不可区分噪声/混淆源”的谱推断思路，可为因果推断中 latent source / measurement error 问题或统计计算中的数值优化提供借鉴。
- **关键技术**: `spectral log-likelihood`, `Hawkes process`, `second-order properties`, `model identifiability`, `exponential kernel`
- **为什么对您有用**: 处理不可区分噪声（latent source）的谱推断思路，对因果推断中 measurement error / latent confounding 设定及统计计算中的数值方法有参考价值。

## 经济理论 / 应用  *(econ_theory, 1 篇)*

### 1. [10.1111/sjos.70005](https://doi.org/10.1111/sjos.70005) — Parameters estimation of a threshold Chan–Karolyi–Longstaff–Sanders process from continuous and discrete observations
- **作者**: Sara Mazzonetto, Benoît Nieto
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1670-1707
- 相关性 6/10 · novelty: `minor`
- **摘要**: 本文研究带多重阈值的连续时间自激励遍历过程（threshold CKLS）的参数估计，该模型推广了 Vasicek、CIR 等经典金融计量模型，允许动态机制在不同阈值区间内发生切换。作者分别在连续观测和离散观测下推导了漂移项参数的极大似然估计（MLE）与拟极大似然估计（QMLE），并证明在无限时间跨度与高频观测的离散设定下，估计量具有与连续观测相同的渐近正态性。文中还讨论了扩散系数的估计，并通过模拟与真实数据验证了引入多重阈值的必要性。对您而言，该文提供了阈值扩散过程参数估计的渐近理论，可作为经济理论（利率模型）与数理统计（MLE/QMLE 渐近性）交叉的参考，但缺乏半参数/高维/因果的视角。
- **关键技术**: `threshold diffusion process`, `maximum likelihood estimation`, `quasi-maximum likelihood estimation`, `asymptotic normality`, `high-frequency asymptotics`
- **为什么对您有用**: 涉及经济理论中的经典利率模型（CKLS）与数理统计中的 MLE/QMLE 渐近理论，可作为离散与连续时间扩散过程参数估计的参考，但方法学上偏纯参数化，与您主攻的半参数/高维/因果推断距离较远。

## 其他  *(other, 9 篇)*

### 1. [10.1111/sjos.70008](https://doi.org/10.1111/sjos.70008) — Collapsibility of the Conditional Models of CG‐Graphical Models
- **作者**: Xiangdong Xie, Jianhua Guo, Shiyuan He
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1735-1762
- 相关性 5/10 · novelty: `new_theory`
- **摘要**: 本文研究 CG-图模型（chain graph，混合离散-连续变量）条件模型的 collapsibility 性质，目标是给出模型可折叠性的等价条件且不依赖额外假设。此前 Didelez & Edwards (2004) 的结果需要特定假设，Liu & Guo (2013) 仅处理纯离散或纯连续情形；本文通过考察边际化后模型交互项的保持性，绕开了不可处理的条件密度计算，在混合变量的一般设定下完全解决了该问题。核心贡献是给出了最一般设定下模型可折叠性的一组等价条件，并证明了模型可折叠性与估计可折叠性的等价性。技术路线依赖交互结构在边际化下的保持分析，而非直接处理条件分布。该结果对理解图模型中边际化与条件独立性的关系有理论意义，对您在因果推断中思考 collapsibility 与混杂（Simpson's paradox）的联系有参考价值，但本文偏纯图模型理论，与估计效率或高维推断的直接关联较弱。
- **关键技术**: `CG-graphical models`, `collapsibility equivalence conditions`, `interaction preservation under marginalization`, `model-collapsibility vs estimate-collapsibility`, `mixed discrete-continuous variables`
- **为什么对您有用**: Collapsibility 是因果推断中混杂与 Simpson's paradox 的核心概念，本文在混合变量图模型下给出最一般的等价条件，对您在因果推断中理解边际化与条件效应的关系有理论参考；但本文是纯图模型结构理论，不涉及估计效率或半参数理论。

### 2. [10.1111/sjos.70012](https://doi.org/10.1111/sjos.70012) — Learning under commission and omission event outliers
- **作者**: Yuecheng Zhang, Guanhua Fang, Wen Yu
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1852-1880
- 相关性 4/10 · novelty: `new_method`
- **摘要**: 在 temporal point process 框架下，事件流可能被 commission outliers（意外出现的事件）和 omission outliers（意外缺失的事件）污染，目标是提出对两类异常同时鲁棒的估计方法。作者引入 novel weight function 动态调整每个观测事件的重要性，使最终估计器在无异常时保持无偏、有异常时具备鲁棒性。该方法可嵌入分类与变点检测等下游任务，理论与数值实验均验证了其有效性。据作者所知，这是首个可证明同时处理 commission 与 omission outliers 的方法。变点检测部分与您的假设检验兴趣有交集；鲁棒加权思路可迁移至其他 semiparametric 模型中的异常值处理，但论文核心在 point process 建模而非效率理论或高维推断。
- **关键技术**: `temporal point process`, `robust weight function`, `commission and omission outliers`, `change point detection`, `unbiasedness under null contamination`
- **为什么对您有用**: 变点检测下游任务与您的假设检验兴趣有交集；鲁棒加权估计的构造思路可迁移至 semiparametric 模型中的异常值处理，但论文核心在 point process 建模而非效率理论或高维推断，属于方法相邻而非直接推进。

### 3. [10.1111/sjos.70000](https://doi.org/10.1111/sjos.70000) — A proper concordance index for models with crossing hazards
- **作者**: A. Gandy, T. J. Matcham
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1479-1504
- 相关性 3/10 · novelty: `new_method`
- **摘要**: 在生存分析模型评估中，concordance index (C-index) 是广泛使用的指标，但在 crossing hazards（如分层 Cox 或机器学习模型）下，现有 C-index 不满足 proper scoring rule 性质（即真实模型未必最大化该指标）。本文刻画了基于个体对首次事件时间预测风险率排序时，C-index 成为 proper 指标的精确数学条件，并提出了一种新的 proper concordance index。理论证明该指标在 crossing hazards 下仍保持 proper 性质，而传统指标可能偏好错误模型。实验验证了新指标在模型选择中的正确性，并探讨了其作为深度学习辅助损失项的应用。对您而言，该文将 proper scoring rule 的数学性质引入生存模型评估，对研究模型选择与假设检验的数学统计基础有一定参考价值，但与核心因果推断或高维效率理论关联较弱。
- **关键技术**: `proper scoring rule`, `concordance index`, `crossing hazards`, `survival model evaluation`, `stratified proportional hazards`
- **为什么对您有用**: 本文属于数学统计中模型选择与评估的范畴（proper scoring rule），虽非您核心的因果推断或效率理论，但对理解生存分析中指标的理论缺陷与修正有方法论参考价值。

### 4. [10.1111/sjos.70014](https://doi.org/10.1111/sjos.70014) — Construction of maximum projection Latin hypercube designs using number‐theoretic methods
- **作者**: Yuxing Ye, Ru Yuan, Yaping Wang
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1899-1931
- 相关性 2/10 · novelty: `new_method`
- **摘要**: 本文研究计算机实验中最大投影拉丁超立方体设计的构造问题，目标是在仅部分因子活跃的设定下优化所有可能因子子集的投影性质。现有 MaxPro LHD 的构造较为困难且文献有限，作者提出两种基于好格点设计与数论的代数构造方法。理论上，所得设计在 log-distance 意义下渐近最优，且在逼近 MaxPro 下界方面近乎最优。此外，这些设计在列正交性、maximin 距离和均匀投影准则等多指标下均表现优异。该工作属于实验设计领域，与您关注的因果推断或高维推断理论无直接交集，但其中基于数论的代数构造算法对统计计算方向有微弱的方法论参考价值。
- **关键技术**: `maximum projection Latin hypercube designs`, `good lattice point designs`, `number-theoretic construction`, `log-distance optimality`, `multi-criteria optimization`
- **为什么对您有用**: 本文属于计算机实验设计，与您的主要研究兴趣（因果推断、高维统计、效率理论）无直接关联，仅数论构造算法与统计计算有微弱联系，整体相关性较低。

### 5. [10.1111/sjos.12728](https://doi.org/10.1111/sjos.12728) — Issue Information
- **作者**: 
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4
- 相关性 0/10 · novelty: `minor`
- **摘要**: 这是 Scandinavian Journal of Statistics 第 52 卷第 4 期的期刊信息页，非研究论文，仅包含 Wiley 出版社的 ESG（环境、社会、治理）声明与公司使命介绍。没有任何研究问题、方法或理论结果。对您的研究无任何参考价值。
- **为什么对您有用**: 非研究内容，与所有 primary/secondary interests 均无关。

### 6. [10.1111/sjos.70023](https://doi.org/10.1111/sjos.70023) — A general framework on conditions for constraint‐based causal learning
- **作者**: Kai Z. Teh, Kayvan Sadeghi, Terry Soo
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2209-2241
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "causal_inference",
  "summary_zh": "本文研究约束型因果发现算法的正确性条件（如 faithfulness），通过引入"性质"（property）这一抽象表示，构建了统一框架来推导和比较各类算法的正确性条件。在该框架下，作者给出了 PC 算法的精确正确性条件，并将其与其它因果发现算法的条件建立联系；进一步证明，对于输出满足任意极小性定义的祖先图或有向无环图的算法，最稀疏 Markov 表示（SMR）条件是最弱的可能正确性条件。文章还论证 Pearl-极小性对有意义的因果学习是必要的，但不足以放松 faithfulness 假设，必须结合背景知识等加以强化。该框架还提出了一种先控制正确性条件再设计算法的范式。对您而言，虽然本文聚焦因果发现而非效应估计，但其对 faithfulness 假设的系统性弱化分析与您在 causal inference 中 sensitivity analysis 的兴趣有思路上的共通性，且约束型方法底层依赖的条件独立性检验与 hypothesis testing 方向直接相关。",
  "key_techniques": [
    "constraint-based causal discovery",
    "faithfulness assumption",
    "s

### 7. [10.1111/sjos.70024](https://doi.org/10.1111/sjos.70024) — On optimal blocked definitive screening designs: Theoretical insights and computational simplifications
- **作者**: Bo Hu, Yaping Wang, Fasheng Sun
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 2242-2269
- 相关性 0/10 · novelty: `new_theory`
- **摘要**: 本文研究在线性加二次效应模型下，最优区组化确定性筛选设计（DSD）的理论性质与计算简化问题。作者推导了最优正交区组化 DSD 的理论条件，证明了部分现有设计的最优性，并据此大幅降低了搜索最优设计的计算复杂度。核心贡献在于将原本依赖复杂组合搜索的设计问题转化为有理论指导的简化计算。由于该文属于实验设计领域，与您关注的因果推断或高维推断等核心方向关联较弱，仅其计算简化的思路对统计计算子方向有极微弱的参考价值。
- **关键技术**: `definitive screening designs`, `optimal blocking`, `linear-plus-quadratic effects model`, `orthogonal blocking`, `combinatorial search simplification`
- **为什么对您有用**: 本文属于实验设计（DOE）领域，与您的主要研究方向（因果推断、高维统计、半参数效率等）直接关联较弱，仅计算简化的思路对统计计算子方向有极微弱的参考价值。

### 8. [10.1111/sjos.70015](https://doi.org/10.1111/sjos.70015) — Debiasing piecewise deterministic Markov process samplers using couplings
- **作者**: Adrien Corenflos, Matthew Sutton, Nicolas Chopin
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1932-1974
- 相关性 0/10
- **摘要**: ```json
{
  "topic": "stat_computing",
  "summary_zh": "本文研究连续时间 PDMP（piecewise deterministic Markov process）采样器的去偏问题，目标是在有限 Markov 迭代下构造无偏 Monte Carlo 估计量，而非依赖渐近无偏性。核心方法是将 coupled MCMC 估计器（Jacob et al. 思路）推广到连续时间框架，通过构造两个 PDMP 过程的耦合使得它们在随机时间 T 会合，从而利用 Glynn–Rhee 型无偏估计器消除 burn-in 偏差。作者具体推导了 bouncy sampler、boomerang sampler 和 coordinate sampler 三种 PDMP 的耦合方案，并给出初步数值实验验证维度可扩展性。理论贡献在于给出了连续时间 PDMP 耦合的显式构造，使估计器可在无限处理器极限下精确而非无限迭代极限下精确，从而实现 embarrassingly parallel 化。对您而言，虽然此处的"去偏"不同于 semiparametric debiased ML 的语境，但 PDMP 采样器的耦合构造与并行化思路对统计计算方向有直接参考价值。",
  "key_techniques": ["PDMP samplers", "coupled M

### 9. [10.1111/sjos.70016](https://doi.org/10.1111/sjos.70016) — The deep latent position topic model for clustering and representation of networks with textual edges
- **作者**: Rémi Boutin, Pierre Latouche, Charles Bouveyron
- **期刊/来源**: Scandinavian Journal of Statistics
- **分类**: vol 52 · issue 4 · pp 1975-2013
- 相关性 0/10 · novelty: `new_method`
- **摘要**: 本文针对边带文本的网络（如用户转发文本的社交网络），目标是同时实现节点聚类与低维可视化表示。提出 Deep-LPTM，将变分图自编码器（variational graph auto-encoder）与概率主题模型结合，在两个嵌入空间中联合表示节点与边，参数通过变分推断（variational inference）算法估计。同时引入 IC2L 模型选择准则，专门挑选兼具良好聚类与可视化性质的模型。合成数据实验表明 Deep-LPTM 在节点分区恢复上优于 ETSBM 和 STBM；Enron 邮件数据集分析展示了图结构的可解释可视化。该文与您核心兴趣关联较弱，变分推断算法属于统计计算范畴但非您关注的高维/效率/因果方向，仅当您对网络数据的变分推断实现细节感兴趣时可略读。
- **关键技术**: `variational graph auto-encoder`, `probabilistic topic model`, `variational inference`, `model selection criterion IC2L`, `network embedding`
- **为什么对您有用**: 与您 primary interests 关联弱；变分推断算法属于统计计算但非核心（非高维/效率/因果），Enron 数据集属经济领域应用但方法学迁移价值有限。


---

Maintained by 陈星宇 · [Homepage](https://cxy0714.github.io/) · [Source on GitHub](https://github.com/cxy0714/research-news)

