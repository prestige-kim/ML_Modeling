# 자전거 수요예측 피처 엔지니어링 특별수업

## 목적

이 과정은 머신러닝을 처음 배우는 학습자가 자전거 수요예측 문제를 통해 다음 질문에 스스로 답하도록 돕는 4회 특별수업이다.

1. 한 행에서 무엇을 예측하고, 예측 시점에 어떤 정보를 사용할 수 있는가?
2. 원본 데이터를 모델이 이해하기 좋은 feature로 어떻게 표현하는가?
3. 만든 feature가 실제로 도움이 됐는지 어떻게 공정하게 비교하는가?
4. 선택한 workflow로 재현 가능한 예측과 제출 파일을 어떻게 만드는가?

기존 Week 5 ARIMA 과정은 완료 처리하지 않고 보류한다. 이 특별수업의 결과는 Week 5 승급 증거와 구분한다. `bike.ipynb`와 `temp.ipynb`는 이 과정의 수업 자료나 답안으로 사용하지 않는다.

## 설명 원칙

새 개념은 현실 문제에서 필요한 이유, 기존 표현의 한계, 수작업 과정, 작은 표, API 사용법, 반환값과 원본 변경 여부, 예측 시점 가용성, Data Leakage 위험, validation 검증 방법 순서로 설명한다. 새 API는 실제 과제와 다른 toy data로 먼저 실행한다.

정답은 `Hint → Guidance → Partial Solution → Full Solution` 순서로 제공하며, Full Solution은 학습자가 명시적으로 요청할 때만 제공한다.

## 데이터

- `data/train.csv`: 10,886개 시간별 관측치와 `count`
- `data/test.csv`: 6,493개 시간별 입력, `count` 없음
- 목표 변수: `count`
- 사용 가능한 원본 입력: `datetime`, `season`, `holiday`, `workingday`, `weather`, `temp`, `atemp`, `humidity`, `windspeed`
- 사용 금지: `casual`, `registered` (`casual + registered = count`)
- 외부 데이터와 공식 test의 정답은 사용하지 않는다.

## 공통 평가 설계

대회의 월별 train/test 구조를 흉내 내는 expanding monthly backtest를 사용한다.

Prediction time에는 각 validation 시작 시점보다 앞서 관측된 train target과 대회가 해당 예측 행에 제공한 달력·날씨 입력만 사용할 수 있다. Target 구성값, validation 이후 actual, 전체 데이터에 미리 fit한 전처리를 사용하는 경우는 Data Leakage로 처리한다.

| Fold | Train | Validation |
|---|---|---|
| 1 | `2012-10-16 00:00` 이전 | 2012-10-16~2012-10-19 |
| 2 | `2012-11-16 00:00` 이전 | 2012-11-16~2012-11-19 |
| 3 | `2012-12-16 00:00` 이전 | 2012-12-16~2012-12-19 |

- 모든 feature set은 동일한 validation 행에서 비교한다.
- 전처리 객체와 모델은 fold별 train에서만 `fit`한다.
- 공식 test는 최종 feature와 target 전략을 선택한 뒤에만 예측한다.
- 주 지표는 RMSLE, 보조 지표는 MAE다.
- RMSLE 계산 전 예측값을 0 이상으로 제한한다.
- fold별 점수와 전체 out-of-fold 점수를 함께 기록한다.

## 수업 순서

### Lesson 1 — 예측 문제와 시간 피처

한 행, feature, target, prediction time, target leakage, RMSLE와 시간 기반 validation을 배운다. 평균만 예측하는 `DummyRegressor`를 최소 기준으로 두고, 안전한 원본 feature와 `year`, `month`, `day`, `hour`, `weekday`를 추가한 feature set을 고정된 `RandomForestRegressor`로 비교한다.

### Lesson 2 — 범주형과 순환형 인코딩

범주형 숫자, one-hot encoding, `hour_sin`, `hour_cos`, `month_sin`, `month_cos`, `ColumnTransformer`, `Pipeline`을 배운다. 날짜 분해 feature와 범주형·순환형 feature set을 같은 조건에서 비교한다.

### Lesson 3 — 도메인 피처와 상호작용

시간대, 근무일 상호작용, 날씨·체감 feature group을 하나씩 추가하는 ablation을 수행한다. validation이 개선되지 않은 그룹은 최종 feature set에서 제외한다. target-derived lag와 rolling feature는 이번 과정에서 사용하지 않는다.

### Lesson 4 — Target 변환, 오류 분석, 제출

`log1p`, `expm1`, RMSLE를 배우고 원래 target 학습과 log target 학습을 비교한다. 최종 pipeline을 전체 train에 재학습하고 시간대·근무일·날씨·수요 수준별 오류를 분석한 뒤 `output/bike_submission.csv`를 만든다.

## 완료 기준

- target leakage와 시간 분할 누수가 없다.
- train/test에 동일한 feature 생성 과정이 적용된다.
- preprocessing과 모델은 각 fold train에서만 학습된다.
- 최소 세 개 feature group을 공통 backtest로 비교한다.
- feature의 채택과 제외가 validation 결과로 설명된다.
- 최종 notebook이 처음부터 끝까지 실행된다.
- 제출 파일은 `datetime,count` 두 컬럼과 6,493행을 가지며 sample submission과 datetime 순서가 같다.
- `count`에 결측치, 무한대, 음수가 없다.
- Kaggle 업로드는 수행하지 않는다.
