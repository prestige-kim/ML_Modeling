# Week 4 Review Notes

이 파일은 Week 4에서 실제로 배운 내용과 수정된 실수를 보존하는 누적 학습 기록이다.

## Phase 3 - Feature Engineering

현재 상태: 진행 중 (`Feature Experiment 1` 통과)

## Feature Experiment 1 - Leakage-safe rolling feature comparison

완료 상태: 통과

사용 데이터셋: `data/week1_macro_practice.csv`

실습 목표:

- 현재 행을 포함한 최근 3개 행의 평균으로 rolling feature를 만든다.
- 중간 결측 월을 보존한 상태에서 feature를 생성해 시점 정렬을 유지한다.
- persistence baseline, lag1 선형회귀, lag1+rolling3 선형회귀를 공통 test 행에서 비교한다.
- publication lag가 실제 feature 가용성에 미치는 영향을 설명한다.

배운 개념:

- `rolling(window=3)`은 날짜 자체가 아니라 현재 행과 이전 두 행을 묶으므로, 날짜 정렬과 월별 연속성을 먼저 확인해야 한다.
- `2024-03-31`의 rolling3 source date는 `2024-01-31`, `2024-02-29`, `2024-03-31`이고 target date는 `2024-04-30`이다.
- 중간 결측 월의 행을 먼저 삭제하면 `shift()`와 행 기반 rolling이 떨어진 월을 이웃 행처럼 연결할 수 있다. 원래 월별 행에서 feature를 모두 만든 뒤 공통 유효 행을 선택해야 한다.
- 계산상 과거 방향인 feature도 해당 지표가 prediction time 이후 발표된다면 현실에서는 사용할 수 없다. Reference period와 release date 사이의 publication lag를 확인해야 한다.
- 동일한 test 11행에서 baseline의 MAE/RMSE는 약 0.4455/0.4602, lag1 모델은 약 1.3519/1.4088, lag1+rolling3 모델은 약 1.2373/1.2798이었다.
- Rolling feature 추가는 이번 test에서 lag1 모델의 오차를 줄였지만 persistence baseline보다 좋은 성능을 만들지는 못했다. 이 결과를 다른 데이터와 window 설정에 일반화할 수 없다.

사용한 함수/메서드:

- `rolling(window=3)`
  - 필요한 이유: 각 feature date에서 현재와 최근 과거 값의 평균 수준을 하나의 feature로 요약하기 위해 사용한다.
  - 주요 인수: `window=3`은 현재 행을 포함한 최근 3개 행을 뜻한다. 기본 `center=False`에서는 현재 행이 window의 오른쪽 끝이다.
  - 반환값: 집계 전에는 `Rolling` 객체를 반환하며, 이어서 `.mean()`을 호출하면 원래 index에 맞는 새 `Series`를 반환한다.
  - 원본 변경 여부: 원본 `Series`나 `DataFrame`을 직접 변경하지 않는다.
  - 재할당 필요 여부: 모델 feature로 사용하려면 새 컬럼에 저장해야 한다.
  - 주의점: 날짜 정렬 전에 계산하거나 `center=True`로 미래 행을 포함하면 Data Leakage가 생길 수 있다. 중간 결측값이 window에 포함되면 기본 설정에서는 rolling 결과도 결측이 된다.
- `dropna(subset=[...])`는 lag1, rolling3, target과 baseline에 필요한 현재 값이 모두 존재하는 공통 모델링 행을 선택하는 데 재사용했다.
- `LinearRegression`, `fit()`, `predict()`, MAE/RMSE 계산은 두 feature set을 같은 조건에서 비교하는 데 재사용했다.

수정된 실수:

- 처음에는 target과 lag1 결측 행을 제거한 뒤 rolling을 계산했으나, 중간 행 삭제가 rolling window의 달력상 의미를 바꿀 수 있음을 확인하고 모든 feature 생성 후 공통 결측 행을 제거하도록 수정했다.
- 처음에는 lag1+rolling3 모델과 baseline만 비교했으나, rolling feature의 증분 가치를 측정하기 위해 lag1 단독 모델을 같은 공통 행에서 다시 학습해 비교했다.
- 빈 `DataFrame`에 scalar metric을 대입해 컬럼만 보이고 행이 없었으나, 한 행의 index를 만든 뒤 결과를 저장하도록 수정했다.
- 절대오차 평균을 `MSE`로 표기했던 이름을 `MAE`로 수정했다.

핵심 정리:

- Feature engineering에서는 컬럼 생성 자체보다 source 시점, 결측 처리 순서와 공통 out-of-sample 비교가 중요하다.
- Rolling feature가 안전하려면 window가 과거 방향이어야 할 뿐 아니라 각 source value가 실제 prediction time에 발표되어 있어야 한다.
- 이번 rolling feature는 lag1 모델을 개선했지만 baseline을 넘지 못했으므로 다음 데이터와 실험에서도 통제 비교가 필요하다.
