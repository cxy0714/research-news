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
from tenacity import retry, stop_after_attempt, wait_exponential

log = logging.getLogger(__name__)


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
        self.client = OpenAI(base_url=base, api_key=key)
        self.model_fast = os.environ.get("SJTU_MODEL_FAST", "deepseek-chat")
        self.model_deep = os.environ.get("SJTU_MODEL_DEEP", "deepseek-reasoner")
        self.limiter = RateLimiter(max_per_minute=9)   # leave headroom under 10

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=20))
    def chat(
        self,
        messages: list[dict],
        *,
        deep: bool = False,
        temperature: float = 0.2,
        max_tokens: int = 2048,
    ) -> str:
        # SJTU V3.2 requires a real user message.
        if not any(m.get("role") == "user" for m in messages):
            raise ValueError("SJTU API requires at least one user-role message")
        self.limiter.wait()
        model = self.model_deep if deep else self.model_fast
        resp = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return resp.choices[0].message.content or ""
