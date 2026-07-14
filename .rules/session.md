# Session Start Workflow

사용자가 세션 시작, 오늘 공부, 다음 Exercise 진행을 요청할 때 적용한다.

## 시작 점검

1. `progress.md`에서 `Start Date`, `Last Updated`, `Current Phase`, `Current Week`, `Week Status`를 확인한다.
2. 최근 완료 실습과 `Next Session Goal`을 확인한다.
3. 활성 약점, Follow-up Queue, Diagnostic Scores를 확인한다.
4. 현재 Week에 해당하는 `notes/weekN.md`를 읽고 지난 실습의 Follow-up, 반복 실수, 새 세션 목표와 연결되는 개념을 확인한다.
5. 현재 Week를 올릴 충분한 증거가 있는지 점검하되 자동으로 승급하지 않는다.

## 세션 제시 형식

세션 시작 응답에는 다음 항목을 간결하게 포함한다. 새 개념이 필요한 Exercise는 `Exercise 제시 전 Concept Gate`를 통과한 뒤에만 제시한다.

- 현재 위치: Phase, Week, Week Status
- 오늘의 주제 하나
- 예상 학습 시간
- 오늘 Exercise에 필요한 새 개념 점검
- 필요한 경우 새 개념 설명
- 집중 과제 하나
- 실습 하나
- 성찰 질문 하나

지난 실습의 Follow-up이 현재 주제와 연결되면 새 내용을 추가하기 전에 우선 반영한다.

## Exercise 제시 전 Concept Gate

Exercise를 제시하기 전에 반드시 다음을 수행한다.

1. 이번 Exercise를 수행하는 데 필요한 pandas/Python/sklearn 문법, 머신러닝 용어, 모델링 개념을 목록화한다.
2. 각 항목이 현재 Week의 `notes/weekN.md` 또는 `progress.md`에 이미 학습된 것으로 기록되어 있는지 확인한다.
3. 새 항목이 하나라도 있으면 Exercise를 제시하기 전에 각 항목을 다음 순서로 설명한다.
   - 왜 지금 이 개념이 필요한지
   - 사람이 손으로 한다면 어떤 작업인지
   - 작은 표나 예시로 보면 어떻게 동작하는지
   - pandas/Python/sklearn 문법은 그 작업을 어떻게 자동화하는지
   - 주요 인수, 반환값, 원본 변경 여부, 재할당 필요 여부
   - 잘못 쓰면 어떤 Data Leakage나 모델링 오류가 생기는지
4. 위 설명이 끝나기 전에는 실습 요구사항, 답안 경로, 통과 기준을 제시하지 않는다.
5. 새 개념이 없더라도 "새 개념 없음" 또는 "이미 학습한 개념만 사용"이라고 명시한 뒤 Exercise를 제시한다.

## 진행 원칙

- 한 번에 과도한 문제나 여러 모델을 제시하지 않는다.
- 실습 요구사항과 완료 기준을 구분해 설명한다.
- 실습에 새 pandas/Python/sklearn 문법, 새 모델링 용어 또는 새 평가 개념이 필요하면 반드시 `Exercise 제시 전 Concept Gate`를 먼저 통과한다.
- 모델링 초급 단계에서는 하나의 Exercise를 필요한 만큼 더 작은 Concept Check로 쪼갤 수 있다.
- 과제 질문은 일반론으로 답할 수 없게 만든다. 반드시 사용할 컬럼명, 예시 날짜, 예측 시점, target 시점, 기대 답변 범위를 함께 제시한다.
- 글 답안 문항에는 최소 통과 기준을 명시한다. 예: "2023-05를 feature month로, 2023-06을 target month로 직접 언급할 것."
- 사용자가 답안을 제출하기 전에는 모범 답안이나 완성 코드를 제공하지 않는다.
- 답안 경로는 저장소 상대 경로를 사용한다.
