# Week 4 Review Notes

이 파일은 Week 4에서 실제로 배운 내용과 수정된 실수를 보존하는 누적 학습 기록이다.

## Phase 3 - Feature Engineering

현재 상태: 진행 중 (`Feature Experiment 1`, `Transfer Experiment` 통과)

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

## Transfer Experiment - Korea Composite Leading Indicator

완료 상태: 통과

사용 데이터셋: `data/week4_korea_cli.csv`

답안:

- `answers/code/week4/week4_transfer.ipynb`
- `answers/text/week4/week4_transfer.txt`

실습 목표:

- 익숙하지 않은 한국 OECD Composite Leading Indicator 데이터의 구조, 날짜 범위, 중복 날짜, 값의 결측과 누락 월을 새로 점검한다.
- 다음 달 `KORLOLITOAASTSAM`을 예측하는 1개월 horizon 문제를 정의한다.
- 원래 월별 행에서 lag1, rolling3와 target을 만든 뒤 공통 유효 행을 선택한다.
- 2000-01부터 2019-12까지를 train, 2020-01부터 2024-11까지를 test feature date로 사용해 persistence baseline과 `LinearRegression`을 비교한다.
- reference date, release date와 revision 가능성이 실제 예측 시점의 feature 가용성에 미치는 한계를 확인한다.

배운 개념:

- `is_monotonic_increasing=True`는 날짜가 감소하지 않고 정렬됐다는 뜻일 뿐, 중간 월이 빠지지 않았다는 뜻은 아니다.
- 날짜 정렬, 중복 날짜, 값의 결측과 누락 월은 서로 다른 데이터 품질 문제이므로 각각 확인해야 한다.
- 매월 1일로 표시된 월별 데이터에서는 전체 예상 월을 `freq='MS'`로 만든 뒤 실제 날짜와 비교할 수 있다.
- 이번 원본 데이터는 1990-01부터 2026-06까지 438개 월이 연속적으로 존재했고, 중복 날짜와 값의 결측도 없었다.
- feature 생성 전에 누락 월의 행을 삭제하면 떨어진 두 달이 이웃 행처럼 연결되어 행 기반 `shift()`와 `rolling()`의 달력상 의미가 달라질 수 있다.
- `observation_date`는 지표가 나타내는 reference period의 표기이며 실제 release date라고 단정할 수 없다.
- Publication lag가 있으면 기준월 값이 prediction time에 아직 발표되지 않았을 수 있다. Revision이 있으면 현재 내려받은 최신 값이 과거에 처음 알려졌던 값과 다를 수 있으므로, 실시간 예측 성능을 엄밀히 재현하려면 당시 vintage가 필요하다.
- 공통 test 기간에서 persistence baseline의 MAE/RMSE는 약 0.1942/0.2245, lag1+rolling3 `LinearRegression`은 약 0.3632/0.4465였다. 이번 기간에서는 baseline의 오차가 더 낮았다.

새로 사용한 함수/속성:

- `Series.is_monotonic_increasing`
  - 필요한 이유: feature를 만들기 전에 날짜가 오름차순으로 정렬됐는지 확인한다.
  - 반환값: 값이 감소하지 않으면 `True`, 감소하는 지점이 있으면 `False`인 단일 `bool`을 반환한다.
  - 원본 변경 여부: 원본 `Series`를 변경하지 않는 읽기 전용 속성이다.
  - 재할당 필요 여부: 즉시 점검만 할 때는 필요 없고, 결과를 나중에 사용하려면 변수에 저장한다.
  - 주의점: `True`여도 중간 날짜가 빠질 수 있으므로 월별 연속성 검사를 대신하지 않는다.
- `pd.date_range(start=..., end=..., freq='MS')`
  - 필요한 이유: 실제 데이터의 최소 날짜부터 최대 날짜까지 존재해야 할 모든 월초 날짜를 만든다.
  - 주요 인수: `start`와 `end`는 예상 기간의 경계이고, `freq='MS'`는 Month Start, 즉 매월 첫날 빈도다.
  - 반환값: 새 `DatetimeIndex`를 반환한다.
  - 원본 변경 여부: 원본 `DataFrame`이나 날짜 컬럼을 변경하지 않는다.
  - 재할당 필요 여부: 실제 날짜와 비교하려면 `expected_dates` 같은 변수에 저장한다.
  - 주의점: 원본 날짜가 월말이라면 `MS`가 아니라 데이터의 날짜 규칙에 맞는 빈도를 선택해야 한다.
- `pd.DatetimeIndex(...)`
  - 필요한 이유: 실제 날짜 `Series`를 예상 날짜와 같은 index 형태로 만들어 집합 차이 비교를 명확하게 수행한다.
  - 주요 인수: datetime으로 변환된 1차원 날짜 값이다.
  - 반환값: 새 `DatetimeIndex`를 반환한다.
  - 원본 변경 여부: 원본 날짜 `Series`를 변경하지 않는다.
  - 재할당 필요 여부: 비교에 다시 사용할 때는 `actual_dates` 같은 변수에 저장한다.
- `Index.difference(other)`
  - 필요한 이유: 예상 날짜에는 있지만 실제 날짜에는 없는 월을 찾는다.
  - 주요 인수: 비교 대상인 실제 날짜 index다.
  - 반환값: 호출한 index에만 존재하는 값으로 구성된 새 `Index` 또는 `DatetimeIndex`를 반환한다.
  - 원본 변경 여부: 예상 날짜와 실제 날짜 index를 변경하지 않는다.
  - 재할당 필요 여부: 누락 월을 출력하거나 개수를 확인하려면 `missing_dates` 같은 변수에 저장한다.
  - 주의점: 중복 날짜 검사는 별도 문제이므로 `duplicated()` 확인을 대신하지 않는다.

재사용한 함수/메서드:

- `pd.to_datetime()`, `sort_values()`, `duplicated()`, `isna()`, `shift()`, `rolling().mean()`, `dropna(subset=[...])`를 새 데이터의 날짜 점검과 leakage-safe feature 구성에 재사용했다.
- `LinearRegression`, `fit()`, `predict()`와 MAE/RMSE 계산을 공통 test 행의 baseline 비교에 재사용했다.

수정된 실수:

- 처음에는 `is_monotonic_increasing=True`를 월별 날짜가 끊기지 않았다는 의미로 해석했으나, 이는 정렬 여부만 확인한다는 점을 교정했다.
- 초기 코드에서는 train 종료일을 2019-01로 두고 `cli_rolling3` 대신 현재 값인 `baseline`을 모델 feature로 넣었으나, train 종료일을 2019-12로 수정하고 `cli_lag1`과 `cli_rolling3`을 사용했다.
- 글 답안 질문과 통과 기준이 충분히 분리되지 않은 상태에서 리뷰가 더 구체적인 설명을 사후 요구했다. 이번 답안은 원래 제시된 질문 범위로 평가했으며, 이후 과제는 글 답안 질문과 최소 통과 기준을 Exercise 제시 시점에 명시해야 한다.

핵심 정리:

- 날짜가 정렬됐다는 것과 모든 월이 존재한다는 것은 다르다. 월별 feature를 만들기 전에 예상 날짜와 실제 날짜를 비교해야 한다.
- 새 데이터로 workflow를 옮길 때 target, horizon, split과 baseline을 다시 정의하고, 모든 모델을 공통 test 행에서 비교해야 한다.
- 최신 CSV만으로는 과거 release date와 당시 vintage를 완전히 복원할 수 없으므로, 계산된 backtest 성능을 그대로 실시간 성능이라고 단정할 수 없다.
- 이번 새 데이터에서도 단순 persistence baseline이 lag1+rolling3 선형회귀보다 낮은 test 오차를 보였다.
