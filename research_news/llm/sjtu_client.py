"""Thin wrapper around the SJTU OpenAI-compatible endpoint.

Handles rate limiting (10 req/min by default) via a token bucket.
"""
from __future__ import annotations

import logging
import os
import threading
import time
from collections import deque

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential, before_sleep_log

import logging as _logging

log = logging.getLogger(__name__)

# Per-request timeout and retry budget for the LLM endpoint. The SJTU/GLM
# endpoint occasionally hangs on long deep-read calls; a real call finishes in
# ~2-3 min, so default to a 5-min timeout to abandon a stuck request fast
# instead of waiting out the SDK's 10-min default. Retries are owned here
# (tenacity), so the OpenAI SDK's own retry layer is disabled (max_retries=0) to
# keep the attempt count predictable: worst case = MAX_ATTEMPTS × REQUEST_TIMEOUT
# (≈15 min/paper) instead of the old tenacity×SDK explosion (≈90 min/paper).
# Both are env-overridable — lower them to fail faster on flaky days, raise them
# if legitimate long reads get cut off.
REQUEST_TIMEOUT = float(os.environ.get("SJTU_TIMEOUT", "300"))
MAX_ATTEMPTS = int(os.environ.get("SJTU_MAX_ATTEMPTS", "3"))


class RateLimiter:
    def __init__(self, max_per_minute: int = 10):
        self.max = max_per_minute
        self.times: deque[float] = deque()
        self.lock = threading.Lock()

    def wait(self) -> None:
        with self.lock:
            now = time.monotonic()
            while self.times and now - self.times[0] > 60:
                self.times.popleft()
            if len(self.times) >= self.max:
                sleep_for = 60 - (now - self.times[0]) + 0.1
                if sleep_for > 0:
                    time.sleep(sleep_for)
                now = time.monotonic()
                while self.times and now - self.times[0] > 60:
                    self.times.popleft()
            self.times.append(time.monotonic())


class SJTUClient:
    def __init__(self):
        base = os.environ.get("SJTU_API_BASE", "https://models.sjtu.edu.cn/api/v1")
        key = os.environ.get("SJTU_API_KEY")
        if not key:
            raise RuntimeError("SJTU_API_KEY is not set (check your .env)")
        self.client = OpenAI(
            base_url=base, api_key=key, timeout=REQUEST_TIMEOUT, max_retries=0
        )
        self.model_fast = os.environ.get("SJTU_MODEL_FAST", "deepseek-chat")
        self.model_deep = os.environ.get("SJTU_MODEL_DEEP", "deepseek-reasoner")
        self.limiter = RateLimiter(max_per_minute=9)
        # Per-run accounting; keys are model names.
        self.usage: dict[str, dict[str, int]] = {}
        self.calls: int = 0

    def _record(self, model: str, usage_obj) -> None:
        if usage_obj is None:
            return
        slot = self.usage.setdefault(
            model, {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        )
        slot["prompt_tokens"] += int(getattr(usage_obj, "prompt_tokens", 0) or 0)
        slot["completion_tokens"] += int(getattr(usage_obj, "completion_tokens", 0) or 0)
        slot["total_tokens"] += int(getattr(usage_obj, "total_tokens", 0) or 0)
        self.calls += 1

    @retry(
        stop=stop_after_attempt(MAX_ATTEMPTS),
        wait=wait_exponential(multiplier=2, min=2, max=20),
        before_sleep=before_sleep_log(log, _logging.WARNING),
        reraise=True,
    )
    def chat(
        self,
        messages: list[dict],
        *,
        deep: bool = False,
        model: str | None = None,
        temperature: float = 0.2,
        max_tokens: int = 2048,
    ) -> str:
        if not any(m.get("role") == "user" for m in messages):
            raise ValueError("SJTU API requires at least one user-role message")
        self.limiter.wait()
        if model is None:
            model = self.model_deep if deep else self.model_fast
        resp = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        self._record(model, getattr(resp, "usage", None))
        choice = resp.choices[0]
        finish_reason = getattr(choice, "finish_reason", None)
        if finish_reason and finish_reason not in ("stop", "end_turn", None):
            # `length` = hit max_tokens; `content_filter` = safety; anything
            # other than `stop` means the output is partial. Surface it so we
            # don't silently lose the tail of long deep-read responses.
            log.warning(
                "LLM response truncated: finish_reason=%s, model=%s, "
                "max_tokens=%d (output may be missing the final sections)",
                finish_reason, model, max_tokens,
            )
        return choice.message.content or ""
