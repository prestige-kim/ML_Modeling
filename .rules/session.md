# Session Start Workflow

사용자가 세션 시작, 오늘 공부, 다음 Exercise 진행을 요청할 때 적용한다.

## 시작 점검

1. `progress.md`에서 `Start Date`, `Last Updated`, `Current Phase`, `Current Week`, `Week Status`를 확인한다.
2. 최근 완료 실습과 `Next Session Goal`을 확인한다.
3. 활성 약점, Follow-up Queue, Diagnostic Scores를 확인한다.
4. 필요할 때만 `review_notes.md`에서 관련 실수와 개념을 확인한다.
5. 현재 Week를 올릴 충분한 증거가 있는지 점검하되 자동으로 승급하지 않는다.

## 세션 제시 형식

세션 시작 응답에는 다음 항목을 간결하게 포함한다.

- 현재 위치: Phase, Week, Week Status
- 오늘의 주제 하나
- 예상 학습 시간
- 집중 과제 하나
- 실습 하나
- 성찰 질문 하나

지난 실습의 Follow-up이 현재 주제와 연결되면 새 내용을 추가하기 전에 우선 반영한다.

## 진행 원칙

- 한 번에 과도한 문제나 여러 모델을 제시하지 않는다.
- 실습 요구사항과 완료 기준을 구분해 설명한다.
- 실습에 새 pandas 문법, 새 모델링 용어 또는 새 평가 개념이 필요하면 실습 전에 `개념 → 손작업 직관 → 작은 표 예시 → pandas 구현 의미` 순서로 먼저 설명한다.
- 모델링 초급 단계에서는 하나의 Exercise를 필요한 만큼 더 작은 Concept Check로 쪼갤 수 있다.
- 과제 질문은 일반론으로 답할 수 없게 만든다. 반드시 사용할 컬럼명, 예시 날짜, 예측 시점, target 시점, 기대 답변 범위를 함께 제시한다.
- 글 답안 문항에는 최소 통과 기준을 명시한다. 예: "2023-05를 feature month로, 2023-06을 target month로 직접 언급할 것."
- 사용자가 답안을 제출하기 전에는 모범 답안이나 완성 코드를 제공하지 않는다.
- 답안 경로는 저장소 상대 경로를 사용한다.
