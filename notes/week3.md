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

## Exercise 2 - Lag feature creation on real data

완료 상태: 통과

사용 데이터셋: `data/week1_macro_practice.csv`

실습 목표:

- 실제 월별 데이터에서 `industrial_production_index_lag1`을 생성한다.
- `target_next_month`와 lag feature가 서로 다른 시점을 의미함을 코드 출력으로 확인한다.
- `2024-02-29` 행을 기준으로 feature month, lag source date, target date를 구분한다.
- 첫 행의 lag feature 결측 이유와 `shift(-1)`을 feature에 사용할 때의 Data Leakage 위험을 설명한다.

배운 개념:

- `2024-02-29` 행의 `industrial_production_index_lag1`은 `2024-01-31`의 `industrial_production_index`에서 온 값이다.
- `2024-02-29` 행의 `target_next_month`는 `2024-03-31`의 `industrial_production_index`를 의미한다.
- 첫 번째 행인 `2021-01-31`에는 이전 달인 `2020-12-31` 행이 없으므로 `industrial_production_index_lag1`이 결측이 된다.
- lag feature를 `shift(-1)`로 만들면 `2024-02-29` 행에 `2024-03-31`의 산업생산지수가 들어가므로, 예측 시점에 알 수 없는 미래 값을 feature로 사용하는 Data Leakage가 된다.

사용한 함수/메서드:

- `pd.read_csv()`: CSV 파일을 `DataFrame`으로 불러오는 역할로 사용했다.
- `pd.to_datetime()`: `date` 컬럼을 날짜형으로 변환하는 역할로 사용했다.
- `sort_values()`: `date` 기준 오름차순 정렬에 사용했다. 시계열에서 `shift()`를 적용하기 전 정렬 순서가 중요하다.
- `drop_duplicates()`: 중복 행을 제거한 뒤 시간 정렬 기반 feature를 만들기 위해 사용했다.
- `shift()`: `industrial_production_index_lag1`에는 `shift(1)`, `target_next_month`에는 `shift(-1)`을 사용했다.
- `isin()`: 지정한 세 날짜(`2024-01-31`, `2024-02-29`, `2024-03-31`)만 필터링해 정렬 결과를 확인하는 데 사용했다.

수정된 실수:

- 처음에는 `shift(-1)` 누수를 baseline 예측값과 같아져 오차가 0이 되는 문제로 설명했지만, 실제 핵심은 target 시점의 미래 실제값이 feature에 들어가는 문제임을 수정했다.
- 답안에서 `24년 1월`, `24년 3월`처럼 월 단위로 적었으나, 이번 실습 기준에서는 `2024-01-31`, `2024-03-31`처럼 정확한 날짜로 쓰는 편이 더 명확하다.
- notebook에서 절대경로를 사용했다. 실행은 가능했지만 저장소 기준 상대경로를 쓰는 습관이 필요하다.

핵심 정리:

- `shift(1)`은 과거 값을 현재 행으로 가져와 lag feature를 만든다.
- `shift(-1)`은 미래 값을 현재 행으로 가져오므로 target 생성에는 사용할 수 있지만, feature 생성에 쓰면 Data Leakage 위험이 크다.
- 한 행에는 "예측 시점에 아는 정보"와 "나중에 맞힐 정답"이 함께 있어야 하며, 둘의 시점을 코드 출력으로 직접 확인해야 한다.

## Exercise 3 - Lag/target missing row handling

완료 상태: 통과

사용 데이터셋: `data/week1_macro_practice.csv`

실습 목표:

- `industrial_production_index_lag1`과 `target_next_month`를 만든 뒤 생기는 결측 행의 원인을 구분한다.
- 첫 행의 lag 결측과 마지막 행의 target 결측이 모델링에서 서로 다른 의미를 갖는다는 점을 설명한다.
- 모델 입력 feature와 정답 target이 모두 있는 행만 `model_df`로 남긴다.
- `2024-02-29` 행에서 feature date, lag source date, target date를 정확한 날짜로 설명한다.

배운 개념:

- 첫 번째 날짜 행의 `industrial_production_index_lag1`은 이전 달 행이 없어서 결측이 된다.
- 마지막 날짜 행의 `target_next_month`는 다음 달 정답이 데이터셋에 없어서 결측이 된다.
- `target_next_month`가 결측인 행은 supervised learning에서 학습 정답이 없으므로 학습용 행으로 사용할 수 없다.
- 결측 자체가 Data Leakage인 것은 아니며, 예측 시점에 알 수 없는 미래 값이나 전체 데이터 통계로 결측을 채우려 할 때 Data Leakage 위험이 생긴다.
- `2024-02-29` 행의 feature date는 `2024-02-29`, lag source date는 `2024-01-31`, target date는 `2024-03-31`이다.

사용한 함수/메서드:

- `isna()`: `industrial_production_index_lag1`과 `target_next_month`의 결측 여부를 확인하는 데 사용했다.
- `sum()`: `isna()` 결과에서 `True` 개수를 세어 결측 행 수를 확인하는 데 사용했다.
- `dropna(subset=[...])`
  - 필요한 이유: 모델링에 필요한 feature와 target 컬럼에 결측이 있는 행을 제외하기 위해 사용한다.
  - 주요 인수: `subset`; 결측 여부를 검사할 컬럼명 목록을 받는다.
  - 반환값: 지정한 컬럼의 결측 행이 제거된 새 `DataFrame`.
  - 원본 변경 여부: 기본적으로 원본 `DataFrame`을 직접 바꾸지 않는다.
  - 재할당 필요 여부: 결과를 계속 쓰려면 `model_df = ...`처럼 새 변수에 저장해야 한다.
  - 주의점: `subset=['target_next_month' and 'industrial_production_index_lag1']`처럼 쓰면 Python의 `and` 연산 때문에 두 컬럼이 아니라 마지막 문자열 하나만 검사하게 된다. 컬럼명은 `subset=['target_next_month', 'industrial_production_index_lag1']`처럼 각각 별도 원소로 넣어야 한다.

수정된 실수:

- 처음에는 `2024-02-29` 행의 feature month, lag source date, target date를 월 단위로만 쓰거나 서로 바꿔 적었지만, 최종 답안에서 정확한 날짜 기준으로 수정했다.
- 처음에는 `isna()`의 행별 `True/False` 출력만 확인했지만, 이후 `isna().sum()`으로 결측 행 수를 숫자로 확인했다.
- 처음에는 `dropna(subset=...)`에서 두 컬럼을 `and`로 연결해 한 컬럼만 검사했지만, 이후 두 컬럼명을 리스트의 별도 원소로 넣는 방식으로 수정했다.
- `target_next_month` 결측 자체를 Data Leakage라고 표현하는 경향이 남아 있었고, 정확히는 결측을 미래 정보로 채울 때 누수 위험이 생긴다는 점을 교정했다.

핵심 정리:

- lag feature의 첫 행 결측은 과거 입력값이 없기 때문에 생긴다.
- target의 마지막 행 결측은 맞혀야 할 다음 달 정답이 없기 때문에 생긴다.
- 모델링 후보 데이터는 feature와 target이 모두 있는 행으로 구성해야 한다.
- 결측 행을 제거하는 것은 미래 값을 임의로 채우지 않기 때문에 현재 단계에서 안전한 처리다.

## Exercise 4 - First LinearRegression with lag1 feature

완료 상태: 통과

사용 데이터셋: `data/week1_macro_practice.csv`

실습 목표:

- `industrial_production_index_lag1` 하나를 입력 feature `X`로 사용해 첫 `LinearRegression` 모델을 학습한다.
- `target_next_month`를 정답 `y`로 두고, 시간순 train/test split을 유지한다.
- Week 2 baseline과 `LinearRegression`을 같은 test 11행에서 MAE/RMSE로 비교한다.
- `X`, `y`, `fit`, `predict`의 역할과 target 또는 미래 이동 컬럼을 `X`에 넣으면 안 되는 이유를 설명한다.

배운 개념:

- `X`는 모델이 예측 시점에 사용할 수 있는 입력 feature 표다. 이번 실습에서는 `industrial_production_index_lag1`만 사용했다.
- `y`는 모델이 맞혀야 하는 정답이다. 이번 실습에서는 다음 달 산업생산지수인 `target_next_month`를 사용했다.
- `fit`은 train 구간의 `X_train`과 `y_train`을 사용해 선형회귀의 계수와 절편을 학습하는 단계다.
- `predict`는 학습된 모델이 `X_test`만 보고 test 구간의 예측값을 만드는 단계다.
- baseline은 feature date의 현재 `industrial_production_index`를 다음 달 예측값으로 사용하는 persistence model이다.
- 같은 test 11행에서 baseline은 MAE 약 0.4455, RMSE 약 0.4602였고, `LinearRegression`은 MAE 약 1.3536, RMSE 약 1.4119였다.
- 이번 test 구간에서는 `industrial_production_index_lag1` 하나만 사용한 선형회귀가 baseline보다 좋은 성능을 보이지 못했다.

사용한 함수/메서드:

- `LinearRegression`
  - 필요한 이유: lag feature와 다음 달 target 사이의 선형 관계를 학습하기 위해 사용한다.
  - 주요 인수: 이번 실습에서는 기본값으로 생성했다.
  - 반환값: `LinearRegression()` 객체.
  - 원본 변경 여부: `DataFrame`을 직접 변경하지 않는다.
  - 재할당 필요 여부: 학습과 예측에 계속 쓰려면 `model = LinearRegression()`처럼 변수에 저장해야 한다.
- `fit(X_train, y_train)`
  - 필요한 이유: train 데이터에서 입력 feature와 target의 관계를 학습하기 위해 사용한다.
  - 주요 인수: `X_train`은 2차원 feature table, `y_train`은 target 값이다.
  - 반환값: 학습된 모델 객체 자신.
  - 원본 변경 여부: 입력 `DataFrame`을 직접 변경하지 않지만, 모델 객체 내부에는 학습된 계수와 절편이 저장된다.
  - 재할당 필요 여부: 보통 `model.fit(...)`처럼 호출해도 모델 객체가 학습 상태를 갖는다.
- `predict(X_test)`
  - 필요한 이유: 학습된 모델로 test 구간의 예측값을 만들기 위해 사용한다.
  - 주요 인수: `X_test`; train 때 사용한 feature와 같은 컬럼 구조여야 한다.
  - 반환값: 예측값 배열.
  - 원본 변경 여부: 입력 `DataFrame`을 직접 변경하지 않는다.
  - 재할당 필요 여부: 예측값을 평가하거나 표에 붙이려면 `pred = model.predict(X_test)`처럼 저장해야 한다.
- `mean_absolute_error(y_true, y_pred)`: 실제 정답과 예측값의 절대오차 평균을 계산하는 데 사용했다.
- `mean_squared_error(y_true, y_pred)`: MSE를 계산한 뒤 `** 0.5`를 적용해 RMSE를 만들었다.
- 이전 실습에서 배운 `pd.read_csv()`, `pd.to_datetime()`, `sort_values()`, `drop_duplicates()`, `shift()`, `dropna(subset=[...])`는 모델링 workflow 준비 단계로 재사용했다.

수정된 실수:

- 처음에는 baseline 예측값과 `LinearRegression` 예측값끼리 비교해 오차를 계산했지만, 모델 평가는 실제 정답인 `target_next_month`와 각 예측값을 비교해야 한다는 점을 수정했다.
- 처음에는 RMSE 대신 MSE 값을 RMSE로 해석했지만, MSE에 제곱근을 씌운 값이 RMSE라는 점을 교정했다.
- `y_train`을 DataFrame 형태로 만들었다가, 이후 target 벡터의 의미가 더 명확한 Series 형태로 수정했다.
- 글 답안에서 성능 해석을 어려워했지만, 수정 후 MAE/RMSE가 더 큰 모델이 실제 정답과 더 멀리 벗어났다는 방식으로 비교했다.

핵심 정리:

- 안전한 lag feature라고 해서 반드시 baseline보다 예측력이 좋은 것은 아니다.
- feature의 가치는 feature를 만든 사실이 아니라, 같은 test 행에서 실제 정답과 비교한 out-of-sample 성능으로 판단해야 한다.
- MAE/RMSE는 두 예측값끼리 비교하는 지표가 아니라, 실제 정답과 예측값의 차이를 측정하는 지표다.
