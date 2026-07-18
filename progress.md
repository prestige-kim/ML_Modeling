# Bootcamp Progress

이 파일은 부트캠프의 현재 실행 상태를 기록하는 단일 원본이다. 교육과정은 `PLAN.md`, 상세 복습 기록은 `notes/weekN.md`, 갱신 절차는 `.rules/tracking.md`를 따른다.

## Current State

| Field | Value |
|---|---|
| Start Date | 2026-07-09 |
| Last Updated | 2026-07-18 |
| Current Phase | Phase 3 - Feature Engineering |
| Current Week | 3 |
| Week Status | In Progress |
| Current Focus | `shift(1)`로 과거 값을 현재 행의 lag feature로 정렬하는 개념 확인 |
| Next Session Goal | 실제 데이터에서 `industrial_production_index_lag1`을 만들고, 첫 행의 결측과 날짜 정렬을 확인한다. |

## Completed Evidence

상세한 학습 내용과 함수 설명은 해당 주차의 `notes/weekN.md`에 기록한다.

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
- Exercise 2 - Feature/target month alignment
  - 한 학습 행이 feature month의 입력 정보와 target month의 정답을 함께 담는 구조임을 설명했다.
  - `shift(-1)`로 다음 달 `industrial_production_index`를 `target_next_month`로 만들고, `drop_duplicates()`를 `shift` 전에 적용해야 하는 이유를 확인했다.
  - 과제 문항이 일반적이었던 한계는 남겼고, 다음 세션부터 구체 날짜와 컬럼 기준으로 문항을 제시하기로 했다.
  - 답안: `answers/code/week2/week2_2.ipynb`, `answers/text/week2/week2_2.txt`
- Exercise 3 - Time-series train/test split
  - `target_next_month`가 없는 행을 제외하고, 2021-01-31부터 2023-12-31까지를 train, 2024-01-31부터 2024-11-30까지를 test로 나눴다.
  - 무작위 8:2 분할과 시간순 8:2 분할을 구분하고, 미래 데이터가 train에 섞이면 평가가 비현실적이 된다는 점을 확인했다.
  - 답안: `answers/code/week2/week2_3.ipynb`, `answers/text/week2/week2_3.txt`
- Exercise 4 - Baseline prediction definition
  - 다음 달도 이번 달과 같을 것이라는 기준 모델을 정의하고, `baseline_pred_next_month`를 feature month의 `industrial_production_index`에서 만들었다.
  - `target_next_month`를 예측값으로 복사하지 않아야 하는 이유와 예측값의 출처와 예측 대상 시점의 차이를 확인했다.
  - 답안: `answers/code/week2/week2_4.ipynb`, `answers/text/week2/week2_4.txt`
- Exercise 5 - Baseline evaluation with MAE/MSE/RMSE
  - test 구간 11행에서 기준 모델의 `baseline_pred_next_month`와 `target_next_month`의 오차를 계산했다.
  - MAE, MSE, RMSE의 계산 의미를 구분하고, RMSE가 원래 target 단위로 해석된다는 점을 확인했다.
  - 답안: `answers/code/week2/week2_5.ipynb`, `answers/text/week2/week2_5.txt`
- Week 2 Review Check - End-to-end baseline modeling review
  - 예측 문제 정의, feature/target 정렬, 시간순 train/test split, 기준 모델 예측과 MAE/MSE/RMSE 평가를 하나의 흐름으로 재현했다.
  - `target_next_month`는 실제 정답이고 `baseline_pred_next_month`는 feature month의 현재 산업생산지수에서 나온 예측값임을 구분했다.
  - 답안: `answers/code/week2/week2_review.ipynb`, `answers/text/week2/week2_review.txt`

### Week 3 - Feature Engineering

- Exercise 1 - Lag feature direction concept
  - `2024-02-29` 행을 기준으로 `target_next_month`는 2024년 3월 값, `industrial_production_index_lag1`은 2024년 1월 값이어야 함을 구분했다.
  - lag feature는 과거 값을 현재 행으로 가져오므로 `shift(1)`을 사용해야 하고, 반대 방향은 예측 시점에 알 수 없는 미래 정보를 feature에 넣는 Data Leakage가 될 수 있음을 설명했다.
  - 답안: `answers/text/week3/week3_1.txt`

## Diagnostic Scores

점수 범위는 0부터 10까지다. Exercise 리뷰에서 확인된 증거가 있을 때만 변경한다.

| Area | Score |
|---|---:|
| Pandas | 7/10 |
| EDA | 6/10 |
| Visualization | 3/10 |
| Missing Value Handling | 3/10 |
| Feature Engineering | 2/10 |
| Model Evaluation | 3/10 |
| Leakage Awareness | 8/10 |
| Time-Series Intuition | 8/10 |

## Active Weak Areas

- Pandas 메서드의 반환값, 원본 변경 여부와 재할당 필요성을 정확히 설명하기
- 코드 출력을 과장 없이 정확한 문장으로 옮기기
- 결측치 처리 결정을 컬럼 의미와 예측 목적에 따라 설명하기
- 그래프가 보여주는 사실과 추가 데이터 확인이 필요한 판단을 구분하기
- 약한 시각적 관계만으로 변수의 예측 가치를 단정하지 않기
- 새 pandas 메서드의 반환값, 원본 변경 여부, 재할당 필요 여부를 구현 전에 확인하기
- 과제 질문의 표현이 `month`인지 정확한 `date`인지에 따라 답변 기준을 일관되게 맞추기
- notebook에서 상대경로를 사용할 때 현재 작업 폴더(`os.getcwd()`)를 먼저 확인하기

## Strong Areas

- Economic Data Understanding
- Data Collection
- Data Source Validation

## Follow-up Queue

1. 각 설명 변수 후보가 Prediction Time에 실제로 발표되어 있는지 확인하는 습관을 만든다.
2. Week 3에서 실제 lag feature 생성 후 첫 행 결측과 날짜별 정렬 결과를 직접 확인한다.
3. notebook에서 절대경로 대신 현재 작업 폴더를 확인하고 저장소 상대경로를 사용하는 습관을 만든다.

## Week Advancement Evidence

- 현재 판단: 사용자 동의에 따라 Week 3 Feature Engineering으로 진입했다.
- 확보된 증거: Exercise 1에서 목표 변수, 예측 대상 시점, 1개월 Forecast Horizon과 Prediction Time의 핵심을 설명했다. Exercise 2에서 feature month와 target month 정렬, `target_next_month` 생성, 중복 행 정리 필요성을 확인했다. Exercise 3에서 시간순 train/test split 기준과 무작위 분할 위험을 확인했다. Exercise 4에서 기준 모델의 예측값을 feature month의 `industrial_production_index`에서 만들고, target을 복사하지 않아야 함을 확인했다. Exercise 5에서 MAE, MSE, RMSE를 계산하고 기준 모델의 test 성능을 해석했다. Week 2 Review Check에서 전체 흐름을 재현하고, test 11행의 기준 모델 평가 지표를 계산 및 설명했다.
- 추가로 필요한 증거: Week 3 Exercise 2에서 실제 데이터로 lag feature를 만들고, 첫 행 결측과 예측 시점 기준의 사용 가능성을 확인하는 코드와 설명.
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

### Supervised Learning Row Alignment

- 실수: 같은 학습 행에 현재 달 feature와 다음 달 target을 같이 두는 이유가 충분히 설명되지 않은 상태에서 pandas 문법으로 넘어갔다.
- 교정: 모델은 각 행을 하나의 연습문제로 본다. 한 행은 "현재 시점에 아는 입력값"과 "나중에 맞혀야 하는 정답"을 함께 담아야 한다.

### Exercise Prompt Specificity

- 실수: 과제 질문이 일반적인데 리뷰에서 더 구체적인 답안을 사후 요구했다.
- 교정: 다음 세션부터 문항에 사용할 컬럼명, 예시 날짜, 예측 시점, target 시점, 기대 답변 범위와 통과 기준을 명시한다.

### Month and Date Wording

- 실수: 질문에는 `month`라고 표현했지만 리뷰에서는 정확한 일자까지 요구해 평가 기준이 흔들렸다.
- 교정: `month`를 묻는 문항은 월 단위 이해를 기준으로 판단하고, 정확한 날짜가 필요하면 질문과 통과 기준에 `date`를 명시한다.

### Relative Path and Working Directory

- 실수: notebook에서 상대경로를 사용할 때 파일 위치 기준으로 해석된다고 생각할 수 있었다.
- 교정: 상대경로는 보통 현재 작업 폴더 기준으로 해석된다. `os.getcwd()`로 현재 작업 폴더를 확인한 뒤 경로를 정한다.
