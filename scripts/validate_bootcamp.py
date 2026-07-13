#!/usr/bin/env python3
"""Validate the bootcamp document system without external dependencies."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRESS_PATH = ROOT / "progress.md"

REQUIRED_FILES = (
    "AGENTS.md",
    "PLAN.md",
    "README.md",
    "progress.md",
    "notes/week1.md",
    "notes/week2.md",
    "requirements.txt",
    ".rules/core.md",
    ".rules/session.md",
    ".rules/review.md",
    ".rules/tracking.md",
    "scripts/validate_bootcamp.py",
)

REQUIRED_STATE_FIELDS = (
    "Start Date",
    "Last Updated",
    "Current Phase",
    "Current Week",
    "Week Status",
    "Current Focus",
    "Next Session Goal",
)

EXPECTED_DIAGNOSTICS = (
    "Pandas",
    "EDA",
    "Visualization",
    "Missing Value Handling",
    "Feature Engineering",
    "Model Evaluation",
    "Leakage Awareness",
    "Time-Series Intuition",
)


def table_value(markdown: str, field: str) -> str | None:
    pattern = rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|$"
    match = re.search(pattern, markdown, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def validate_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"필수 파일이 없습니다: {relative_path}")


def validate_state(progress: str, errors: list[str]) -> None:
    values = {field: table_value(progress, field) for field in REQUIRED_STATE_FIELDS}

    for field, value in values.items():
        if not value:
            errors.append(f"Current State 필드가 없거나 비어 있습니다: {field}")

    for field in ("Start Date", "Last Updated"):
        value = values.get(field)
        if value:
            try:
                date.fromisoformat(value)
            except ValueError:
                errors.append(f"{field}는 YYYY-MM-DD 형식이어야 합니다: {value}")

    current_week = values.get("Current Week")
    if current_week:
        if not current_week.isdigit() or not 1 <= int(current_week) <= 6:
            errors.append(f"Current Week는 1부터 6 사이의 정수여야 합니다: {current_week}")

    week_status = values.get("Week Status")
    if week_status and week_status not in {"Not Started", "In Progress", "Completed"}:
        errors.append(f"지원하지 않는 Week Status입니다: {week_status}")


def validate_diagnostics(progress: str, errors: list[str]) -> None:
    for area in EXPECTED_DIAGNOSTICS:
        value = table_value(progress, area)
        if value is None:
            errors.append(f"Diagnostic Score 항목이 없습니다: {area}")
            continue

        match = re.fullmatch(r"(10|[0-9])/10", value)
        if not match:
            errors.append(f"Diagnostic Score 형식이 잘못되었습니다: {area}={value}")


def validate_answer_references(progress: str, errors: list[str]) -> None:
    references = set(re.findall(r"`(answers/(?:code|text)/[^`]+)`", progress))
    for relative_path in sorted(references):
        if not (ROOT / relative_path).is_file():
            errors.append(f"완료 증거로 기록된 답안 파일이 없습니다: {relative_path}")


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)

    if PROGRESS_PATH.is_file():
        progress = PROGRESS_PATH.read_text(encoding="utf-8")
        validate_state(progress, errors)
        validate_diagnostics(progress, errors)
        validate_answer_references(progress, errors)

    if errors:
        print("Bootcamp 문서 검증 실패:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Bootcamp 문서 검증 통과")
    print(f"- 필수 운영 파일: {len(REQUIRED_FILES)}개")
    print(f"- 진단 점수 항목: {len(EXPECTED_DIAGNOSTICS)}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
