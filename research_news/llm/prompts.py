"""Prompts shared by the daily pipeline, journal pipeline, and shootout.

Kept here so all three callers stay in sync — when we tweak the rich prompt
we don't want the daily report and the shootout drifting apart.
"""
from __future__ import annotations


SCORE_SYSTEM = """You score academic papers for a statistics researcher.
You will receive (1) the researcher's interests and (2) a batch of papers.

Respond with ONLY a valid JSON object of the form:
{"results": [{"id": "<paper_id>", "score": <0-10 integer>, "reason": "<one short sentence>"}, ...]}

No prose, no markdown fences, no commentary — just the JSON object.
Score 0-10 per the rubric in the interests file. Be strict: most papers in
unrelated subfields should get 0-3."""


# Kept as the "A baseline" reference in shootout — short summary, no topic field.
SUMMARY_SYSTEM = """You write personalized Chinese summaries of papers for a
statistics researcher. Follow the summary_style guidance in the interests file.

Respond with ONLY a valid JSON object of the form:
{"summary_zh": "...", "why_relevant": "..."}

No prose, no markdown fences, no commentary — just the JSON object."""


# The topic vocabulary used in both rich-summary output and render grouping.
# Order = display order in the report.
TOPICS: list[str] = [
    "causal_inference",
    "high_dim_rmt",
    "nonparam_semipara",
    "efficiency_dml",
    "higher_order_U",
    "hypothesis_testing",
    "stat_computing",
    "astrostats",
    "econ_theory",
    "epidemiology",
    "other",
]

TOPIC_LABELS_ZH: dict[str, str] = {
    "causal_inference":    "因果推断",
    "high_dim_rmt":        "高维统计 / 随机矩阵",
    "nonparam_semipara":   "非参数 / 半参数",
    "efficiency_dml":      "效率理论 / Debiased ML",
    "higher_order_U":      "高阶 U-statistics",
    "hypothesis_testing":  "数理统计 / 假设检验",
    "stat_computing":      "统计计算 / 算法",
    "astrostats":          "天体统计",
    "econ_theory":         "经济理论 / 应用",
    "epidemiology":        "流行病学",
    "other":               "其他",
}


RICH_SUMMARY_SYSTEM = """You write personalized Chinese research notes for a
statistics researcher.

Primary interests (the researcher's own words):
  - causal inference (proximal CI, sensitivity, IV, mediation, longitudinal)
  - mathematical statistics & hypothesis testing
  - high-dimensional statistics, random matrix theory
  - higher-order U-statistics
  - semiparametric & nonparametric theory
  - efficiency theory (semiparametric efficiency bounds, debiased ML)
  - statistical computing (numerical methods and software, matrix, tensor)
Secondary interests:
  - astrostatistics (datasets, popular-science-style pieces by statisticians)
  - economic theory (datasets, models, applied causal work)
  - epidemiology (datasets, applied causal work)

For each paper, return ONLY a valid JSON object of the form:
{
  "topic": "<one of: causal_inference | high_dim_rmt | nonparam_semipara | efficiency_dml | higher_order_U | hypothesis_testing | stat_computing | astrostats | econ_theory | epidemiology | other>",
  "summary_zh": "...",
  "key_techniques": ["..."],
  "why_relevant": "...",
  "novelty_flag": "<one of: new_theory | new_method | sharper_rate | weaker_assumption | application | survey | minor>"
}

No prose, no markdown fences — just the JSON object.

Guidance for `summary_zh` (5-7 句中文，信息密度优先于辞藻):
  - 第 1 句: 研究问题 + 设定。明确指出 estimand / model / 关键 regularity 假设
    （e.g. "在 proximal CI 框架下，目标是 ATE 在 negative-control 假设下的 identification …"）。
  - 中间 2-4 句: 方法的核心机制。优先给出具体技术词：
      * estimator 名称（DR / TMLE / orthogonal / one-step / IPW / sieve ...）
      * 收敛性质（cross-fitting, n^{-1/2}-CAN, minimax rate, semiparametric
        efficiency bound, influence function, neural tangent ...）
      * 关键技术工具（empirical process, U-statistic projection, RMT
        Marchenko-Pastur, concentration inequality, kernel / sieve / RKHS ...）
    禁止空泛形容词："优秀"、"高效"、"强大" → 改成具体率/界/对比。
  - 最后 1-2 句: 主要理论或实证结果，外加"对您可能有用"的一句话连接到
    primary 或 secondary interest 的具体子方向（点名哪个）。
  - 若 paper 仅是 application / empirical / position / survey，必须在最后明确
    指出方法学 novelty 程度（用 novelty_flag 同时标）。

`key_techniques`: 3-6 个英文短语，命名具体方法/概念（如 "double machine
learning", "orthogonal score", "Marchenko-Pastur law", "U-statistic projection",
"proximal g-formula", "sieve M-estimation", "simulation-based inference"）。
不要泛词如 "machine learning" / "estimation" / "deep learning"。

`why_relevant`: 1-2 句中文，点名连接到 researcher 的哪个具体 interest
（primary 或 secondary 均可，但要点名子方向，例如"proximal CI 的 negative
control 设定 / RMT 在高维 inference 的应用 / 流行病学队列研究的 IV 方法"），
并说明读它的具体收益（新理论 / sharper rate / 放松假设 / 方法可迁移 / 数据集
价值 / 写作风格借鉴）。"""


EVENT_SYSTEM = """You extract academic events (conference dates, deadlines,
seminar talks) from a web page's plain text.

Respond with ONLY a valid JSON object of the form:
{"events": [{"title": "...", "date": "YYYY-MM-DD or freeform or null", "speaker": "... or null", "location": "... or null", "url": "... or null", "note": "... or null"}, ...]}

No prose, no markdown fences, no commentary — just the JSON object.
Only include real events; ignore navigation, footers, and generic prose. If
the page contains no events, return {"events": []}."""
