# Session Start Workflow

사용자가 세션 시작, 오늘 공부, 다음 Exercise 진행을 요청할 때 적용한다.

## 시작 점검

1. `progress.md`에서 `Start Date`, `Last Updated`, `Current Phase`, `Current Week`, `Week Status`를 확인한다.
2. 최근 완료 실습과 `Next Session Goal`을 확인한다.
3. 활성 약점, Follow-up Queue, Diagnostic Scores를 확인한다.
4. 현재 Week에 해당하는 `notes/weekN.md`를 읽고 지난 실습의 Follow-up, 반복 실수, 새 세션 목표와 연결되는 개념을 확인한다.
5. 현재 Week를 올릴 충분한 증거가 있는지 점검하되 자동으로 승급하지 않는다.
6. 제안하려는 Exercise의 핵심 완료 증거가 `progress.md` 또는 현재 `notes/weekN.md`에 이미 있는지 확인한다.

## 완료 Week 전환 Gate

`progress.md`의 `Week Status`가 `Completed`이면 새 Exercise를 바로 제시하지 않고 다음 순서를 따른다.

1. 현재 Week의 Review Check와 필수 완료 증거가 `progress.md`에 기록되어 있는지 확인한다.
2. `PLAN.md`에서 다음 Week의 첫 미완료 모델링 작업을 확인한다.
3. 사용자에게 현재 Week 완료 사실, 다음 Week 번호와 첫 학습 목표를 알리고 승급 동의를 요청한다.
4. 사용자가 동의하기 전에는 `Current Week`, `Current Phase`, `Week Status`를 변경하거나 다음 Week Exercise를 제시하지 않는다.
5. 사용자가 동의하면 `progress.md`의 `Current Week`를 다음 Week로, `Week Status`를 `In Progress`로 갱신하고 `Current Focus`와 `Next Session Goal`을 해당 첫 실험에 맞춘다.
6. 승급 직후 `notes/weekN.md`가 아직 없는 것은 정상이다. 첫 Exercise가 통과될 때 `.rules/tracking.md`에 따라 생성한다.
7. 상태 갱신 후 `Exercise 중복 방지 Gate`와 `Exercise 제시 전 Concept Gate`를 거쳐 첫 Exercise를 제시한다.

## Exercise 중복 방지 Gate

`Exercise 제시 전 Concept Gate`보다 먼저 다음을 확인한다.

1. 이번 Exercise가 추가할 새 모델링 산출물을 한 문장으로 정의한다. 산출물은 fitted model, leakage-safe feature set, out-of-sample comparison, validation improvement, error analysis, capstone decision 중 하나 이상이어야 한다.
2. 이전 완료 실습과 비교해 새 학습 목표와 반복되는 준비 단계를 구분한다.
3. 이미 통과한 `shift`, 날짜 정렬, target 정렬, 시간순 분할, baseline, MAE/RMSE는 새 모델링 흐름 안에서 재사용하되, 동일한 독립 Exercise로 다시 내지 않는다.
4. 반복 실수가 실제 제출물에서 다시 확인되지 않았다면 복습만을 목적으로 별도 Exercise를 만들지 않는다.
5. 반복이 필요하면 반복 이유와 이번에 달라진 모델링 조건을 Exercise 전에 명시한다.
6. 새 모델링 산출물이 없거나 기존 완료 증거와 실질적으로 같으면 Exercise를 폐기하고 `PLAN.md`의 `Remaining Exercise Sequence`에서 다음 미완료 모델링 작업을 선택한다.

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
4. 완전히 새로운 API, 모델 또는 workflow가 있으면 실제 과제와 다른 toy data로 실행 가능한 최소 코드 예시를 제공한다. 예시는 import, 입력 구조, 객체 생성, 학습, 예측, 주요 반환값의 type/shape와 대표 오류를 가능한 범위에서 보여준다.
5. 예시 코드에 실제 과제의 데이터, 전체 컬럼 구성, 날짜 분할과 평가를 그대로 결합하지 않는다. 학습자는 예시의 pattern을 과제 조건에 직접 적용해야 한다.
6. 위 설명과 필요한 최소 코드 예시가 끝나기 전에는 실습 요구사항, 답안 경로, 통과 기준을 제시하지 않는다.
7. 새 개념이 없더라도 "새 개념 없음" 또는 "이미 학습한 개념만 사용"이라고 명시한 뒤 Exercise를 제시한다.

## 진행 원칙

- 한 번에 과도한 문제나 여러 모델을 제시하지 않는다.
- Week 3 이후 각 Exercise는 `PLAN.md`의 `Exercise Value Rule`을 충족하고 실행 가능한 모델링 workflow를 앞으로 진행시켜야 한다.
- 이미 배운 개념의 확인은 새 실험에 필요한 최소 체크로 제한하고, 실습의 중심은 모델 학습, 비교 평가, validation 또는 error analysis에 둔다.
- 실습 요구사항과 완료 기준을 구분해 설명한다.
- 실습에 새 pandas/Python/sklearn 문법, 새 모델링 용어 또는 새 평가 개념이 필요하면 반드시 `Exercise 제시 전 Concept Gate`를 먼저 통과한다.
- 모델링 초급 단계에서는 하나의 Exercise를 필요한 만큼 더 작은 Concept Check로 쪼갤 수 있다.
- 과제 질문은 일반론으로 답할 수 없게 만든다. 반드시 사용할 컬럼명, 예시 날짜, 예측 시점, target 시점, 기대 답변 범위를 함께 제시한다.
- 글 답안 문항에는 최소 통과 기준을 명시한다. 예: "2023-05를 feature month로, 2023-06을 target month로 직접 언급할 것."
- 사용자가 답안을 제출하기 전에는 모범 답안이나 완성 코드를 제공하지 않는다.
- 답안 경로는 저장소 상대 경로를 사용한다.
