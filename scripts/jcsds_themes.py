# -*- coding: utf-8 -*-
"""Theme taxonomy + keyword classifier for JCSDS 2026 sessions."""
import re

# Ordered: first matching theme wins. Each theme = (key, label_zh, [regex keywords]).
THEMES = [
    ("plenary",   "大会报告 Plenary", [r"^plenary talk$", r"opening ceremony"]),
    ("causal",    "因果推断 Causal Inference", [r"causal", r"因果", r"treatment effect", r"policy optim", r"design-based", r"surrogate endpoint", r"mediation", r"confound", r"randomiz"]),
    ("network",   "网络与图数据 Networks & Graphs", [r"network", r"graph", r"matrix method", r"tensor"]),
    ("llm_dl",    "深度学习与大模型 Deep Learning & LLM", [r"deep learning", r"large language", r"\bllm\b", r"generative", r"embodied", r"foundation model", r"transformer", r"neural"]),
    ("highdim",   "高维统计 High-Dimensional Statistics", [r"high-dimensional", r"high dimensional", r"变量选择", r"variable selection", r"fdr", r"selective inference", r"dimension reduction", r"factor analysis", r"feature selection", r"random matri", r"半监督"]),
    ("biomed",    "生物医学与基因组 Biomedical & Genomics", [r"biomedical", r"genomic", r"clinical", r"临床", r"medicine", r"disease", r"omics", r"single-cell", r"neuroimag", r"brain", r"bci", r"survival", r"pharmaceutical", r"precision", r"health", r"psychiatric", r"cohort"]),
    ("finecon",   "金融与计量经济 Finance & Econometrics", [r"financ", r"econometric", r"economic", r"asset pricing", r"business", r"urban econ", r"management", r"risk spillover", r"energy"]),
    ("rl",        "强化学习与决策 RL & Decision", [r"reinforcement", r"decision science", r"adaptive random", r"bandit"]),
    ("privacy",   "隐私·联邦·分布式 Privacy·Federated·Distributed", [r"privacy", r"private", r"federated", r"differential privacy", r"distributed", r"communication-efficient", r"decentralized"]),
    ("prob",      "概率论与随机过程 Probability & Stochastic Processes", [r"probability", r"stochastic", r"particle", r"branching", r"random matrix", r"free probability", r"mean field", r"nonlinear expectation", r"stein method", r"asymptotic theory", r"functional inequalit", r"partial differential", r"dynamic game"]),
    ("trustworthy","可信·公平·稳健 Trustworthy·Fair·Robust", [r"trustworthy", r"\bfair", r"robust", r"reliability", r"cyber", r"uncertainty quantif", r"conformal"]),
    ("timeseries","时间序列与时空 Time Series & Spatio-Temporal", [r"time series", r"change point", r"changepoint", r"spatio", r"spatial", r"longitudinal", r"state-space", r"dynamic"]),
    ("bayes",     "贝叶斯方法 Bayesian Methods", [r"bayesian"]),
    ("environ",   "环境·气候·地球 Environmental·Climate·Earth", [r"environment", r"climate", r"earth science", r"nature"]),
    ("ml_theory", "机器学习理论与方法 ML Theory & Methods", [r"machine learning", r"statistical learning", r"model averaging", r"sampling", r"model free", r"model-free", r"transfer learning", r"clustering", r"subsampling", r"kalman", r"feature learning"]),
    ("edu_psy",   "实验设计·测量·心理 Design·Measurement·Psychometrics", [r"experimental design", r"educational measurement", r"psychometric"]),
    ("hist",      "统计学史与文化 History & Culture", [r"统计学历史", r"history", r"textbook", r"forum", r"memorial", r"101 program"]),
]

def classify(title):
    t = title.lower()
    for key, label, kws in THEMES:
        for kw in kws:
            if re.search(kw, t):
                return key, label
    return "other", "其他 Other"

THEME_ORDER = [k for k, _, _ in THEMES] + ["other"]
THEME_LABEL = {k: l for k, l, _ in THEMES}
THEME_LABEL["other"] = "其他 Other"
