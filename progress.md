# Bootcamp Progress

이 파일은 부트캠프의 현재 실행 상태를 기록하는 단일 원본이다. 교육과정은 `PLAN.md`, 상세 복습 기록은 `review_notes.md`, 갱신 절차는 `.rules/tracking.md`를 따른다.

## Current State

| Field | Value |
|---|---|
| Start Date | 2026-07-09 |
| Last Updated | 2026-07-13 |
| Current Phase | Phase 2 - Machine Learning Foundations |
| Current Week | 2 |
| Week Status | In Progress |
| Current Focus | Baseline modeling concepts and time-series train/test split |
| Next Session Goal | Feature month와 target month를 정렬하고 1개월 Forecast Horizon에 맞는 학습 데이터를 설계한다. |

## Completed Evidence

상세한 학습 내용과 함수 설명은 `review_notes.md`에 기록한다.

### Week 1 - Data Analysis Foundations

- Exercise 1 - Basic dataset inspection
  - 데이터 구조, 자료형, 결측치, 중복 행과 행의 의미를 점검했다.
  - 답안: `answers/code/week1/week1_1.ipynb`, `answers/text/week1/week1_1.txt`
- Exercise 2 - Date conversion and chronological sorting
  - 날짜 변환과 시간순 정렬을 구분하고 오름차순 여부를 확인했다.
  - 답안: `answers/code/week1/week1_2.ipynb`, `answers/text/week1/week1_2.txt`
- Exercise 3 - Missing value analysis
  - 결측 컬럼과 날짜를 찾고, 의미를 확인하기 전 기계적으로 처리하지 않아야 하는 이유를 설명했다.
  - 답안: `answers/code/week1/week1_3.ipynb`, `answers/text/week1/week1_3.txt`
- Exercise 4 - Summary statistics interpretation
  - `count`, `mean`, `min`, `max`, `std`와 `NaN`의 영향을 해석했다.
  - 답안: `answers/code/week1/week1_4.ipynb`, `answers/text/week1/week1_4.txt`
- Exercise 5 - Basic time-series visualization
  - 선 그래프로 시간 흐름과 결측으로 인한 시각적 공백을 확인했다.
  - 답안: `answers/code/week1/week1_5.ipynb`, `answers/text/week1/week1_5.txt`
- Exercise 6 - Scatter plot relationship check
  - 산점도에서 뚜렷한 관계가 없다는 관찰과 예측에 쓸모없다는 단정을 구분했다.
  - 답안: `answers/code/week1/week1_6.ipynb`, `answers/text/week1/week1_6.txt`
- Week 1 Review Check - End-to-end EDA review
  - 데이터 로드부터 시각화와 모델링 전 판단까지 전체 EDA 흐름을 다시 수행했다.
  - 답안: `answers/code/week1/week1_review.ipynb`, `answers/text/week1/week1_review.txt`

### Week 2 - Machine Learning Foundations

- Exercise 1 - Modeling problem definition
  - 목표 변수 `industrial_production_index`와 다음 달이라는 예측 대상 시점을 구분했다.
  - Forecast Horizon을 1개월로 정의하고, 설명 변수의 예측 시점 가용성과 Data Leakage 위험을 설명했다.
  - 답안: `answers/code/week2/week2_1.ipynb`, `answers/text/week2/week2_1.txt`

## Diagnostic Scores

점수 범위는 0부터 10까지다. Exercise 리뷰에서 확인된 증거가 있을 때만 변경한다.

| Area | Score |
|---|---:|
| Pandas | 7/10 |
| EDA | 6/10 |
| Visualization | 3/10 |
| Missing Value Handling | 3/10 |
| Feature Engineering | 0/10 |
| Model Evaluation | 0/10 |
| Leakage Awareness | 4/10 |
| Time-Series Intuition | 5/10 |

## Active Weak Areas

- Pandas 메서드의 반환값, 원본 변경 여부와 재할당 필요성을 정확히 설명하기
- 코드 출력을 과장 없이 정확한 문장으로 옮기기
- 결측치 처리 결정을 컬럼 의미와 예측 목적에 따라 설명하기
- 그래프가 보여주는 사실과 추가 데이터 확인이 필요한 판단을 구분하기
- 약한 시각적 관계만으로 변수의 예측 가치를 단정하지 않기
- 설명 변수를 데이터의 깔끔함이 아니라 예측 시점의 정보 가용성으로 선택하기
- Data Leakage를 단순한 과적합이 아니라 실제로 사용할 수 없는 정보로 인한 평가 왜곡으로 설명하기

## Strong Areas

- Economic Data Understanding
- Data Collection
- Data Source Validation

## Follow-up Queue

1. Feature month와 target month를 예시 날짜로 명확히 구분한다.
2. 각 설명 변수 후보가 Prediction Time에 실제로 발표되어 있는지 확인하는 습관을 만든다.
3. 시계열 데이터에서 무작위 분할이 위험한 이유를 설명한다.
4. 복잡한 모델 전에 사용할 Baseline Model의 역할을 이해한다.

## Week Advancement Evidence

- 현재 판단: Week 2 유지, `In Progress`.
- 확보된 증거: Exercise 1에서 목표 변수, 예측 대상 시점, 1개월 Forecast Horizon과 Prediction Time의 핵심을 설명했다.
- 추가로 필요한 증거: feature/target 정렬, 시계열 train/test split, Baseline Model, MAE/RMSE의 기본 이해와 Week 2 Review Check.
- 승급 규칙: 충분한 증거가 모이면 다음 Week로의 이동을 추천하며, 자동으로 변경하지 않는다.

## Recurring Mistakes

### Duplicate Row Concept

- 실수: 반복되는 값이나 컬럼을 중복 행과 혼동했다.
- 교정: 한 행의 모든 컬럼 값이 다른 행과 동일할 때 중복 행이다.

### Pandas Output Interpretation

- 실수: 메서드를 실행한 뒤 출력의 의미를 정확한 문장으로 옮기지 못했다.
- 교정: 각 점검 결과가 데이터에 관해 무엇을 말하는지 함께 기록한다.

### Date Range Interpretation

- 실수: 가장 이른 날짜와 늦은 날짜를 뒤집고 2021-01부터 2024-12까지를 약 3년으로 표현했다.
- 교정: 해당 범위는 약 4년의 월별 데이터다.

### Missing Value Treatment Reasoning

- 실수: 결측치 처리를 한 번에 수행하는 기계적인 정리 단계로 생각했다.
- 교정: 컬럼의 역할과 분석 목적을 먼저 확인하고 미래 정보가 섞이지 않는 방법을 선택한다.

### Summary and Plot Interpretation Scope

- 실수: 요약 통계나 그래프만으로 경제적 원인, 정확한 날짜 또는 예측력을 과도하게 해석했다.
- 교정: 관찰된 사실과 추가 검증이 필요한 해석을 분리한다.

### Target and Explanatory Variable Selection

- 실수: 결측치가 없고 안정적으로 보인다는 이유를 목표 변수 선택의 주요 근거로 사용했다.
- 교정: 목표 변수는 미래에 알고 싶은 값으로, 설명 변수는 예측 시점에 사용할 수 있고 관련 가능성이 있는 정보로 정한다.

### Prediction Time and Data Leakage

- 실수: 예측 대상, 모델의 예측값과 예측 시점에 사용할 수 있는 정보를 혼동했다.
- 교정: 예측 시점에는 그 순간까지 실제로 관측 또는 발표된 정보만 사용할 수 있다.
