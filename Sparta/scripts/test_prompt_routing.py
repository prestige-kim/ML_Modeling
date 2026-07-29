#!/usr/bin/env python3
"""Deterministic smoke test for the documented bootcamp/Sparta prompt routing."""

from __future__ import annotations

import sys


BOOTCAMP_EXACT = {
    "오늘 수업 시작",
    "머신러닝 부트캠프 수업 시작",
    "경제 시계열 부트캠프 세션 시작",
    "과제 채점 시작",
    "머신러닝 부트캠프 과제 채점 시작",
}
AMBIGUOUS_EXACT = {
    "수업 시작해줘",
    "다음 수업 진행해줘",
    "과제 채점해줘",
    "검사해줘",
}
SPARTA_MARKERS = ("sparta", "kaggle", "자전거 수요예측", "bike sharing demand")


def route(prompt: str) -> str:
    normalized = " ".join(prompt.strip().split())
    lowered = normalized.lower()
    if any(marker in lowered for marker in SPARTA_MARKERS):
        return "sparta"
    if normalized in BOOTCAMP_EXACT:
        return "bootcamp"
    if normalized in AMBIGUOUS_EXACT:
        return "clarify"
    return "clarify"


CASES = [
    ("오늘 수업 시작", "bootcamp"),
    ("머신러닝 부트캠프 수업 시작", "bootcamp"),
    ("Sparta 수업 시작", "sparta"),
    ("Kaggle 수업 시작", "sparta"),
    ("자전거 수요예측 수업 시작", "sparta"),
    ("Sparta의 자전거 수요예측 Lesson 1 과제 채점 시작", "sparta"),
    ("수업 시작해줘", "clarify"),
    ("다음 수업 진행해줘", "clarify"),
]


def main() -> int:
    failed = False
    for prompt, expected in CASES:
        actual = route(prompt)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] {prompt!r} -> {actual} (expected={expected})")
        failed |= actual != expected
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
