"""Quick sanity check for the SJTU API.

Usage:
    python -m research_news.smoke_test
"""
from __future__ import annotations

import sys

from dotenv import load_dotenv

from .llm.sjtu_client import SJTUClient


def main() -> int:
    load_dotenv()
    try:
        client = SJTUClient()
    except Exception as e:
        print(f"FAIL: client init: {e}")
        return 1

    print(f"base = {client.client.base_url}")
    print(f"fast model = {client.model_fast}")
    print(f"deep model = {client.model_deep}")

    try:
        resp = client.chat(
            [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'pong' and nothing else."},
            ],
            max_tokens=20,
        )
        print(f"chat reply = {resp!r}")
    except Exception as e:
        print(f"FAIL: chat: {e}")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
