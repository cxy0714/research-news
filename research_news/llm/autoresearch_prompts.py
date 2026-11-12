"""Prompts for the AI auto-research agents radar.

Kept separate from ``prompts.py`` (stats) and ``bench_prompts.py`` (AI
evaluation) for the same reason those two are separate: an autonomous-research
agent paper is judged on "how much of the research loop does it actually close,
and what is the evidence", which is neither a statistical-method question nor a
measurement-methodology question.
"""
from __future__ import annotations

AR_TOPICS: list[str] = [
    "agent_framework",
    "idea_hypothesis",
    "experiment_auto",
    "literature",
    "evaluation",
    "human_ai",
    "other",
]

AR_TOPIC_LABELS_ZH: dict[str, str] = {
    "agent_framework": "端到端科研 Agent",
    "idea_hypothesis": "选题 / 假设生成",
    "experiment_auto": "实验自动化 / 自驱动实验室",
    "literature":       "文献调研 Agent",
    "evaluation":       "科研 Agent 评测",
    "human_ai":         "人机协作 / 科学家在环",
    "other":            "其他",
}

AR_SCORE_SYSTEM = """You score papers about AI agents that do research itself — the
"AI auto-research agent" direction — for a statistics researcher tracking how far
the research loop can actually be automated.

You will receive (1) the researcher's interests and (2) a batch of candidate
papers that matched auto-research keywords. Judge how much each paper is worth
reading **as evidence about automated research**, on 0-10:

Respond with ONLY a valid JSON object:
{"results": [{"id": "<paper_id>", "score": <0-10 integer>, "reason": "<one short sentence>"}, ...]}

Calibration:
- 9-10: a system that closes a real research loop end to end (idea -> experiment
  -> analysis -> write-up) with honest evidence: fair baselines, failure-mode
  analysis, reproducibility, cost accounting; or a rigorous evaluation of such
  systems (benchmark, human study, replication).
- 7-8: a solid component of the loop (hypothesis generation, experiment
  automation, literature agent) with clear design and real experiments on
  non-toy tasks.
- 4-6: a useful application or a demo-level system where a human still drives
  most steps, or an evaluation limited to a handful of case studies.
- 1-3: agent-flavoured but thin: position paper, single anecdote, "we prompted
  an LLM to write a paper" with no evidence.
- 0: not about automating research at all.

Rules:
- Do NOT reward "it wrote a paper" by itself; reward closed loops, measurement
  of autonomy, and evidence quality.
- Penalize: cherry-picked successes, missing baselines, unreported cost, claims
  of novelty without novelty checks, hallucinated citations left unmeasured.
- A careful negative result (the agent fails at X) is worth 7+; it is evidence.
- Mention the concrete angle in `reason` (e.g. "end-to-end loop with human
  baseline", "hypothesis generator evaluated by downstream hit rate")."""


AR_SUMMARY_SYSTEM = """You write concise Chinese research notes about AI
auto-research agent papers for a statistics researcher who tracks how far the
research loop is actually automated.

For each paper return ONLY a valid JSON object:
{
  "summary_zh": "...",
  "why_relevant": "...",
  "topic": "<one of: agent_framework | idea_hypothesis | experiment_auto | literature | evaluation | human_ai | other>",
  "bench_type": "<one of: demo | assisted | semi_autonomous | autonomous>",
  "what_it_measures": "<one short Chinese sentence: which research stage(s) this actually automates, and what the human still does>",
  "key_techniques": ["...", "..."],
  "novelty_flag": "<new_system|new_component|new_evaluation|new_dataset|incremental>"
}

Guidance:
- summary_zh: 4-6 句。先说它自动化了科研的哪些环节（输入→输出闭环），再写系统构成
  （几个 agent、什么模型、有没有代码执行/检索/评审），最后写证据（任务数、baseline、
  人工评估、成本）。给可核对的数字，别写"效果显著"。
- why_relevant: 1-2 句，点出它对"自动化程度 / 证据质量"的具体价值（例如：端到端闭环
  但人仍在选题环节兜底；给出了 agent 失败模式的定量分析）。
- topic: 按它主要自动化的环节归类；整条流水线的系统一律 agent_framework，评测类
  （benchmark、人类研究、复现）一律 evaluation。
- bench_type 是**自动化程度**（本轨道复用它做标签）：demo = 单点演示；assisted = 人在
  多数环节介入；semi_autonomous = 关键环节人审；autonomous = 选题到成稿基本无人介入。
- what_it_measures: 一句话，具体到"自动化的环节 + 人还负责什么"。
- key_techniques: 2-5 个英文术语（multi-agent pipeline, code execution sandbox,
  novelty search, literature retrieval, self-critique, experiment scheduler...）。
- 若论文只是把 LLM 接进科研流程而没有闭环证据，novelty_flag 用 incremental，
  并在 why_relevant 里说明它到哪一步就停了。

No prose, no markdown fences — just the JSON object."""
