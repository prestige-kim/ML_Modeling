#!/usr/bin/env python3
"""Validate the independent Sparta Kaggle academy structure and progress state."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SPARTA_ROOT = REPO_ROOT / "Sparta"
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def read_text(path: Path) -> str:
    if not path.is_file():
        ERRORS.append(f"필수 파일 없음: {path.relative_to(REPO_ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def table_value(text: str, field: str) -> str | None:
    pattern = rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip().strip("`") if match else None


def lesson_rows(text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    for match in re.finditer(
        r"^\|\s*(\d+)\s*\|.*?\|\s*(Ready|Locked|In Progress|Needs Revision|Passed)\s*\|",
        text,
        flags=re.MULTILINE,
    ):
        rows.append((int(match.group(1)), match.group(2)))
    return rows


def validate_notebook(path: Path, lesson_number: int, competition_root: Path) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"notebook JSON 오류: {path.relative_to(REPO_ROOT)}: {exc}")
        return

    require(notebook.get("nbformat") == 4, f"nbformat 4가 아님: {path.relative_to(REPO_ROOT)}")
    cells = notebook.get("cells", [])
    require(bool(cells), f"빈 notebook: {path.relative_to(REPO_ROOT)}")
    text = "\n".join("".join(cell.get("source", [])) for cell in cells)

    required_sections = [
        "## 1. 오늘의 질문",
        "## 2. 선수 지식 확인",
        "## 3. 개념 설명",
        "## 4. 손으로 만드는 작은 표",
        "## 5. 실행 가능한 toy example",
        "## 6. Data Leakage 점검",
        "## 7. 실제 데이터 Exercise",
        "## 8. 코드 과제",
        "## 9. 글 과제",
        "## 10. 성찰 질문",
        "## 11. 제출 전 자체 점검",
    ]
    for section in required_sections:
        require(section in text, f"{path.name} 섹션 누락: {section}")

    require(bool(re.search(r"\*\*C\d+", text)), f"{path.name}: C 문항 없음")
    require(bool(re.search(r"\*\*T\d+", text)), f"{path.name}: T 문항 없음")
    require("코드 최소 통과 기준" in text, f"{path.name}: 코드 최소 통과 기준 없음")
    require("통과 기준:" in text, f"{path.name}: T 질문별 통과 기준 없음")
    require("제출 불필요" in text, f"{path.name}: 성찰 질문 제출 여부 없음")
    require(any(cell.get("cell_type") == "code" for cell in cells), f"{path.name}: toy code cell 없음")

    expected_code = competition_root / "answers" / "code" / f"lesson{lesson_number}.ipynb"
    expected_text = competition_root / "answers" / "text" / f"lesson{lesson_number}.txt"
    require(
        str(expected_code.relative_to(REPO_ROOT)) in text,
        f"{path.name}: 코드 제출 경로 불일치",
    )
    require(
        str(expected_text.relative_to(REPO_ROOT)) in text,
        f"{path.name}: 글 제출 경로 불일치",
    )


def validate_git_ignore() -> None:
    for relative in ("Sparta/bike.ipynb", "Sparta/temp.ipynb"):
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", relative],
            cwd=REPO_ROOT,
            check=False,
        ).returncode == 0
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", relative],
            cwd=REPO_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode == 0
        require(ignored, f".gitignore 적용 안 됨: {relative}")
        require(not tracked, f"Git index에서 연결 해제되지 않음: {relative}")


def main() -> int:
    for relative in [
        "AGENTS.md",
        "README.md",
        "progress.md",
        ".rules/core.md",
        ".rules/session.md",
        ".rules/review.md",
        ".rules/tracking.md",
        "promptArchive/DailyStartPrompt.txt",
        "promptArchive/SessionReview.txt",
        "scripts/test_prompt_routing.py",
    ]:
        require((SPARTA_ROOT / relative).is_file(), f"Sparta 필수 파일 없음: {relative}")

    root_agents = read_text(REPO_ROOT / "AGENTS.md")
    for phrase in [
        "### 수업 시스템 구분",
        "Sparta 수업 시작",
        "머신러닝 부트캠프 수업 시작",
        "어느 수업인지 짧게 확인",
    ]:
        require(phrase in root_agents, f"루트 AGENTS 라우팅 계약 누락: {phrase}")

    academy_progress = read_text(SPARTA_ROOT / "progress.md")
    active_slug = table_value(academy_progress, "Active Competition")
    active_path_value = table_value(academy_progress, "Active Competition Path")
    require(bool(active_slug), "Sparta progress에 Active Competition 없음")
    require(bool(active_path_value), "Sparta progress에 Active Competition Path 없음")

    if not active_path_value:
        active_path_value = "competitions/__missing__"
    competition_root = (SPARTA_ROOT / active_path_value).resolve()
    competitions_root = (SPARTA_ROOT / "competitions").resolve()
    require(
        competition_root.is_relative_to(competitions_root),
        "Active Competition Path가 Sparta/competitions 밖을 가리킴",
    )
    require(competition_root.name == active_slug, "Active Competition과 경로 slug 불일치")

    for relative in [
        "PLAN.md",
        "progress.md",
        "notes.md",
        "data",
        "lessons",
        "answers/code",
        "answers/text",
        "output",
    ]:
        require((competition_root / relative).exists(), f"대회 필수 경로 없음: {relative}")

    plan = read_text(competition_root / "PLAN.md")
    for phrase in ["목표 변수", "prediction time", "validation", "Data Leakage", "완료 기준"]:
        require(phrase.lower() in plan.lower(), f"대회 PLAN 필수 계약 누락: {phrase}")

    competition_progress = read_text(competition_root / "progress.md")
    current_lesson_value = table_value(competition_progress, "Current Lesson") or ""
    lesson_status_value = table_value(competition_progress, "Lesson Status") or ""
    current_match = re.fullmatch(r"Lesson\s+(\d+)", current_lesson_value)
    require(bool(current_match), "대회 progress의 Current Lesson 형식 오류")
    require(
        lesson_status_value in {"Ready", "In Progress", "Needs Revision", "Passed"},
        "대회 progress의 Lesson Status 값 오류",
    )

    rows = lesson_rows(competition_progress)
    require(bool(rows), "대회 progress에 Lesson Status 표가 없음")
    if current_match:
        current_number = int(current_match.group(1))
        row_map = dict(rows)
        require(current_number in row_map, "Current Lesson이 Lesson Status 표에 없음")
        require(
            row_map.get(current_number) == lesson_status_value,
            "Current Lesson의 상단 상태와 Lesson 표 상태 불일치",
        )
        for number in range(1, current_number):
            require(row_map.get(number) == "Passed", f"이전 Lesson {number}이 Passed가 아님")

    lesson_files = sorted((competition_root / "lessons").glob("lesson*.ipynb"))
    require(bool(lesson_files), "Lesson notebook이 없음")
    for path in lesson_files:
        match = re.match(r"lesson(\d+)_", path.name)
        require(bool(match), f"Lesson 파일명 형식 오류: {path.name}")
        if match:
            validate_notebook(path, int(match.group(1)), competition_root)

    row_map = dict(rows)
    for number, status in row_map.items():
        if status == "Passed":
            require(
                (competition_root / "answers" / "code" / f"lesson{number}.ipynb").is_file(),
                f"Passed Lesson {number} 코드 답안 없음",
            )
            require(
                (competition_root / "answers" / "text" / f"lesson{number}.txt").is_file(),
                f"Passed Lesson {number} 글 답안 없음",
            )

    validate_git_ignore()

    if ERRORS:
        print("Sparta validation: FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print(
        f"Sparta validation: PASSED "
        f"(active={active_slug}, lessons={len(lesson_files)}, status={lesson_status_value})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
