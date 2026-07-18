# Week 3 Review Notes

이 파일은 Week 3에서 실제로 배운 내용과 수정된 실수를 보존하는 누적 학습 기록이다.

`progress.md`는 현재 진도, 점수, 약점, 완료 상태를 추적한다.
`notes/week3.md`는 Week 3 Exercise에서 실제로 배운 내용, 사용한 함수/메서드, 실수에서 정리된 이해를 복습용으로 기록한다.

기록 절차는 `.rules/tracking.md`를 따른다. 기존 기록은 명백한 사실 오류를 수정하는 경우를 제외하고 삭제하거나 다시 쓰지 않는다.

---

## Phase 3 - Feature Engineering

현재 상태: 시작됨

시작 목표:

- `lag feature`를 예측 시점 기준으로 안전하게 정의한다.
- `shift(-1)`로 만든 target과 `shift(1)`로 만든 과거 feature를 구분한다.
- feature month, target month, lag source month를 구체 날짜 기준으로 설명한다.
- 미래 정보를 feature에 넣는 Data Leakage 위험을 점검한다.

## Exercise 1 - Lag feature direction concept

완료 상태: 통과

사용 데이터셋: 코드 실습 없음. 기존 월별 산업생산지수 예측 문제의 날짜 정렬 개념 점검.

실습 목표:

- 한 행에서 feature month, target month, lag source month를 구분한다.
- `target_next_month`와 `industrial_production_index_lag1`의 역할을 구분한다.
- lag feature를 만들 때 `shift(1)`과 `shift(-1)` 중 어느 방향을 써야 하는지 설명한다.
- 반대 방향을 feature로 쓰면 왜 Data Leakage가 될 수 있는지 설명한다.

배운 개념:

- `target_next_month`는 현재 feature month에서 맞히려는 다음 달의 정답이다.
- `industrial_production_index_lag1`은 현재 feature month에 사용할 수 있는 한 달 전 산업생산지수다.
- `2024-02-29` 행에서 `target_next_month`는 2024년 3월 값이고, `industrial_production_index_lag1`은 2024년 1월 값이다.
- lag feature는 과거 값을 현재 행으로 가져와야 하므로 `shift(1)` 방향을 사용한다.
- `shift(-1)` 방향의 값을 feature로 쓰면 다음 달 값을 현재 행의 입력으로 넣게 되어 예측 시점에 알 수 없는 미래 정보를 사용할 수 있다.

사용한 함수/메서드:

- `shift()`
  - 필요한 이유: 시간순 데이터에서 과거 값 또는 미래 target을 현재 행에 맞춰 정렬하기 위해 사용한다.
  - 주요 인수: `periods`; 양수는 값을 아래 방향으로 이동시키고, 음수는 값을 위 방향으로 이동시킨다.
  - 반환값: 이동된 새 `Series` 또는 `DataFrame`.
  - 원본 변경 여부: 원본을 직접 변경하지 않는다.
  - 재할당 필요 여부: 새 컬럼으로 쓰려면 `df["new_column"] = ...`처럼 재할당해야 한다.
  - 주의점: target 생성과 lag feature 생성을 같은 방향으로 착각하면 미래 정보가 feature에 들어가는 Data Leakage가 생길 수 있다.

수정된 실수:

- 처음에는 `industrial_production_index_lag1`에 `shift(-1)`을 써야 한다고 답했지만, 리뷰 후 `shift(1)`이 맞다는 점을 수정했다.
- 날짜 기준으로는 lag source month를 올바르게 잡았으나, pandas 이동 방향 설명이 처음에 반대로 적혔다.

핵심 정리:

- 다음 달을 맞히는 target은 미래 값이므로 `shift(-1)`로 현재 행에 붙일 수 있다.
- 한 달 전 값을 feature로 쓰는 lag feature는 과거 값이므로 `shift(1)`로 현재 행에 붙인다.
- feature에는 예측 시점에 실제로 알 수 있는 정보만 들어가야 한다.
