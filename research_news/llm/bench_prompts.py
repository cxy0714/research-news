"""Prompts for the AI evaluation / benchmark track.

Kept separate from ``prompts.py`` (stats track) so the two rubrics can evolve
independently: a statistics paper and a benchmark paper are scored on very
different grounds, and mixing the vocabularies made the model grade benchmarks
by "does it look like ML" instead of "is the measurement any good".
"""
from __future__ import annotations

BENCH_TOPICS: list[str] = [
    "methodology",
    "llm_general",
    "agents_tools",
    "rag_longctx",
    "multimodal",
    "safety_factuality",
    "domain",
    "efficiency",
    "other",
]

BENCH_TOPIC_LABELS_ZH: dict[str, str] = {
    "methodology":       "评测方法学",
    "llm_general":       "通用能力评测",
    "agents_tools":      "Agent / 工具使用",
    "rag_longctx":       "RAG / 长上下文",
    "multimodal":        "多模态评测",
    "safety_factuality": "安全 / 事实性",
    "domain":            "领域基准",
    "efficiency":        "效率 / 成本",
    "other":             "其他",
}


BENCH_SCORE_SYSTEM = """You score AI evaluation / benchmark papers for a statistics
researcher who follows AI evaluation as a methodology topic (measurement design,
validity, reliability), not as a leaderboard spectator.

You will receive (1) the researcher's interests and (2) a batch of candidate
papers that already matched evaluation/benchmark keywords. Judge how much each
paper is worth reading **for its evaluation methodology**, on 0-10:

Respond with ONLY a valid JSON object:
{"results": [{"id": "<paper_id>", "score": <0-10 integer>, "reason": "<one short sentence>"}, ...]}

Calibration:
- 9-10: a genuinely new measurement idea or a rigorous meta-evaluation — e.g. a
  benchmark whose construction/validation is documented (contamination checks,
  human baselines, item difficulty calibration, inter-annotator agreement), a
  study of what benchmarks actually measure, judge/LLM-as-judge validation,
  leaderboard dynamics, statistical reliability of eval scores.
- 7-8: a solid, well-scoped benchmark or evaluation method with clear
  task definition, non-trivial construction, and enough detail to reuse.
- 4-6: a useful application/domain benchmark, or an evaluation study whose
  contribution is mostly "we ran model X on task Y"; limited methodological
  novelty.
- 1-3: benchmark-flavoured but thin (a small dataset, a single-model comparison,
  no validation), or an evaluation section inside a model paper.
- 0: not actually about evaluation/benchmarking.

Rules:
- Do NOT reward leaderboard/SOTA numbers by themselves.
- Reward: measurement validity, construct coverage, contamination control,
  difficulty calibration, human/statistical baselines, reproducibility, cost.
- Penalize: "yet another MMLU-style re-skin" with no new measurement insight.
- A benchmark for a genuinely new capability (agents, long-horizon tasks,
  multimodal) is worth 7+ even if small, when the task definition is careful.
- Mention the concrete measurement angle in `reason` (e.g. "contamination
  audit", "judge validation", "new agent task suite")."""


BENCH_SUMMARY_SYSTEM = """You write concise Chinese research notes about AI
evaluation / benchmark papers for a statistics researcher who cares about
measurement design and validity.

For each paper return ONLY a valid JSON object:
{
  "summary_zh": "...",
  "why_relevant": "...",
  "topic": "<one of: methodology | llm_general | agents_tools | rag_longctx | multimodal | safety_factuality | domain | efficiency | other>",
  "bench_type": "<one of: benchmark | evaluation_method | meta_evaluation | dataset | analysis>",
  "what_it_measures": "<one short Chinese sentence: which capability / failure mode / property it measures>",
  "key_techniques": ["...", "..."],
  "novelty_flag": "<new_benchmark|new_metric|new_analysis|new_dataset|incremental>"
}

Guidance:
- summary_zh: 4-6 句。先说它测什么、怎么构造（任务/数据来源/规模/标注方式），
  再说关键结果或方法学贡献（是否做了污染检查、人类基线、难度校准、judge 验证）。
  避免空泛形容词；给出可核对的数字（题目数、模型数、语言数、成本）。
- why_relevant: 1-2 句，点出它对"评测方法学"的具体价值（例如：提供了可复用的
  污染检测流程；把 LLM-as-judge 与人类评分做了 agreement 分析；揭示了某类
  benchmark 的天花板/饱和问题）。不要只说"与 AI 评测相关"。
- topic: 按主要评测对象归类；纯方法学论文（meta-evaluation、指标、统计可靠性、
  污染、judge 验证）一律 methodology。
- what_it_measures: 一句话，具体到能力或失败模式（如"多步工具调用的规划鲁棒性"），
  不要写"大模型能力"这种泛化表述。
- key_techniques: 2-5 个英文术语（benchmark construction, contamination audit,
  human baseline, item response theory, LLM-as-judge, inter-annotator agreement...）。
- 若论文只是"在某个任务上比较了几个模型"而没有评测方法学贡献，novelty_flag 用
  incremental，并在 why_relevant 里说明它的边界。

No prose, no markdown fences — just the JSON object."""


BENCH_DAILY_SYSTEM = """You pick and annotate the most useful AI evaluation /
benchmark papers from a day's arXiv submissions for a statistics researcher.

You will receive the researcher's interests and a JSON list of candidate papers
(title + abstract excerpt + arXiv category). Return ONLY:
{"results": [{"id": "<paper_id>", "score": <0-10>, "reason": "<short>"}, ...]}

Score by evaluation methodology value (see the same rubric as the benchmark
track): new measurement ideas, benchmark construction/validation, contamination
audits, judge validation, meta-evaluation, statistical reliability of eval.
Do not reward leaderboard claims. Papers that merely use a benchmark to train or
compare models score low."""
