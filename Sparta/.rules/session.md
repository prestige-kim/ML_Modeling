# Sparta Session Workflow

## 시작 점검

1. `Sparta/progress.md`에서 Active Competition과 Current Lesson을 확인한다.
2. 해당 대회의 `PLAN.md`, `progress.md`, `notes.md`를 확인한다.
3. 현재 Lesson 상태가 `Ready`, `In Progress`, `Needs Revision`, `Passed` 중 무엇인지 확인한다.
4. 이전 Lesson이 있다면 `Passed`인지 확인한다.
5. 현재 Lesson notebook의 Concept Gate와 C/T 계약을 확인한다.
6. 같은 학습 증거가 이미 통과 기록에 있는지 확인한다.

## Lesson Advancement Gate

- `Not Started` 또는 `Ready`: 현재 Lesson을 시작할 수 있다.
- `In Progress`: 같은 Lesson을 이어서 진행한다.
- `Needs Revision`: 미충족 C/T 문항만 보완하며 다음 Lesson을 제시하지 않는다.
- `Passed`: 다음 Lesson이 있으면 목표를 알리고 사용자의 진행 의사를 확인한 뒤 상태를 변경한다.
- 단일 코드 실행이나 글 일부만으로 통과 처리하지 않는다.
- 마지막 Lesson이 통과되면 과정 완료 조건을 별도로 검증한 뒤 Competition 완료를 추천한다.

## 세션 제시 형식

- 현재 대회, Lesson, 상태
- 오늘의 주제 하나와 예상 시간
- 이전 통과 증거 또는 현재 보완 항목
- 새 개념 목록과 Concept Gate 설명
- toy example
- 코드 과제 C 문항과 최소 통과 기준
- 글 과제 T 문항과 질문별 최소 통과 기준
- 제출 불필요 여부가 표시된 성찰 질문
- 제출 경로와 다음 리뷰 명령

Lesson notebook이 이미 위 내용을 충족하면 해당 notebook을 기준으로 수업하되, 학습자에게 모든 내용을 한 번에 던지지 않고 현재 개념부터 순차적으로 진행한다.

## Concept Gate

새 개념마다 다음 질문에 별도 질문 없이 답할 수 있어야 Exercise를 제시한다.

1. 왜 사용하는가?
2. 적용하면 모델이 받는 정보가 무엇이 달라지는가?
3. 현재 데이터에서 도움이 되었는지 어떻게 판단하는가?

하나라도 설명되지 않았거나 새 API의 toy workflow가 실행되지 않으면 Exercise를 제시하지 않고 개념 자료부터 보완한다.
