# Machine Learning Modeling Bootcamp

경제·시계열 데이터를 사용해 데이터 이해, 전처리, 모델링, 평가와 해석을 독립적으로 수행하는 능력을 기르는 학습 저장소다.

목표는 튜토리얼을 빠르게 끝내는 것이 아니라 새로운 예측 문제를 만났을 때 다음 과정을 스스로 설계하는 것이다.

```text
데이터 확인 → 예측 문제 정의 → 전처리 → 기준 모델 → 평가 → 개선 → 해석
```

## Automated Coaching System

이 저장소의 부트캠프 운영은 다음 문서 계층으로 관리한다.

| File | Responsibility |
|---|---|
| `AGENTS.md` | 에이전트가 자동으로 참고하는 저장소 운영 진입점 |
| `PLAN.md` | 교육 목표, 교수 원칙과 전체 커리큘럼의 단일 원본 |
| `.rules/core.md` | 언어, 단계적 힌트, 모델링 안전 기준 등 공통 규칙 |
| `.rules/session.md` | 세션 시작 시 현재 상태를 읽고 과제를 제시하는 절차 |
| `.rules/review.md` | 코드와 글 답안을 검토하고 단계적으로 피드백하는 절차 |
| `.rules/tracking.md` | Exercise 통과, 진도 갱신과 Week 승급 절차 |
| `progress.md` | 현재 Phase, Week, 점수, 활성 약점과 다음 목표 |
| `review_notes.md` | 완료한 Exercise의 개념, 함수와 교정된 실수 기록 |

`.rules/`는 독립적으로 자동 탐색되는 설정에 의존하지 않는다. `AGENTS.md`가 요청 유형에 맞는 규칙 파일을 읽도록 연결한다.

## Workflow

### 세션 시작

`promptArchive/DailyStartPrompt.txt`의 짧은 요청을 사용하면 에이전트가 다음 순서로 진행한다.

```text
AGENTS.md
→ .rules/core.md와 .rules/session.md
→ PLAN.md와 progress.md
→ 현재 약점에 맞는 오늘의 단일 학습 목표
```

### 답안 리뷰

답안은 같은 Exercise 이름으로 코드와 글을 나눠 저장한다.

```text
answers/code/week2/week2_1.ipynb
answers/text/week2/week2_1.txt
```

리뷰에서는 Correctness, Modeling Logic, Data Leakage Risk, Evaluation Quality, Possible Improvements를 확인한다. 피드백은 `Hint → Guidance → Partial Solution → Full Solution` 순서이며 Full Solution은 명시적으로 요청한 경우에만 제공한다.

### Exercise 완료

핵심 개념 이해와 제출물 검토가 끝나면 한 작업 흐름에서 두 문서를 함께 갱신한다.

- `progress.md`: 현재 상태, 완료 증거, 점수와 다음 목표
- `review_notes.md`: 배운 개념, 함수 설명, 수정한 실수와 핵심 정리

단일 Exercise 완료만으로 Week를 자동 승급하지 않는다.

## Repository Structure

```text
.
├── AGENTS.md
├── PLAN.md
├── README.md
├── progress.md
├── review_notes.md
├── requirements.txt
├── .rules/
│   ├── core.md
│   ├── review.md
│   ├── session.md
│   └── tracking.md
├── answers/
│   ├── code/
│   │   ├── week1/
│   │   └── week2/
│   └── text/
│       ├── week1/
│       └── week2/
├── data/
├── promptArchive/
│   ├── DailyStartPrompt.txt
│   └── SessionReview.txt
└── scripts/
    └── validate_bootcamp.py
```

사용자 답안과 notebook 출력은 학습 증거다. 운영 문서를 정리한다는 이유로 수정하거나 삭제하지 않는다.

## Curriculum

1. Phase 1 - Data Analysis Foundations
2. Phase 2 - Machine Learning Foundations
3. Phase 3 - Feature Engineering
4. Phase 4 - Time-Series Foundations
5. Phase 5 - Forecasting Models
6. Phase 6 - Capstone Project

현재 학습 위치는 중복해서 기록하지 않고 `progress.md`를 기준으로 확인한다.

## Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
jupyter notebook
```

notebook에서는 가능하면 사용자 컴퓨터의 절대 경로 대신 저장소 기준 상대 경로를 사용한다.

## Validation

운영 문서를 변경하거나 Exercise 완료 기록을 갱신한 뒤 다음 명령으로 필수 파일, 현재 상태 필드, 진단 점수와 답안 경로를 확인한다.

```bash
python3 scripts/validate_bootcamp.py
```
