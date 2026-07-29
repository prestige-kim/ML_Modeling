# Bike Sharing Demand Progress

## Current State

| Field | Value |
|---|---|
| Last Updated | 2026-07-29 |
| Competition | Bike Sharing Demand |
| Status | Ready |
| Current Lesson | Lesson 1 |
| Lesson Status | Ready |
| Current Focus | 한 행·feature·target·prediction time과 target leakage를 정의하고 첫 시간 feature ablation을 준비함 |
| Next Session Goal | 안전한 원본 feature와 시간 파생 feature를 expanding monthly backtest의 공통 validation 행에서 비교함 |

## Lesson Status

| Lesson | Title | Status | Required Evidence |
|---|---|---|---|
| 1 | 예측 문제와 시간 피처 | Ready | Feature Set A/B의 공통 OOF RMSLE·MAE 비교와 leakage 설명 |
| 2 | 범주형과 순환형 인코딩 | Locked | One-hot/cyclic 표현의 증분 가치와 train-only preprocessing |
| 3 | 도메인 피처와 상호작용 | Locked | 세 feature group의 순차 ablation과 최종 후보 set |
| 4 | Target 변환, 오류 분석, 제출 | Locked | target 전략 비교, OOF 오류 분석, 검증된 submission |

## Completed Evidence

아직 통과한 Lesson이 없다.

## Active Weak Areas

- 머신러닝 workflow를 처음부터 설명받는 수준에서 feature, target과 prediction time을 명확히 구분하기
- 새로운 feature가 계산 가능하다는 사실과 validation 성능 개선을 구분하기
- 전처리와 모델을 fold train에서만 fit하는 습관 만들기

## Follow-up Queue

1. Lesson 1에서 RMSLE, RandomForest와 expanding backtest의 toy workflow를 먼저 실행한다.
2. 모든 C/T 문항 통과 전에는 Lesson 2를 열지 않는다.

## Competition Completion Gate

- Lesson 1~4가 모두 Passed
- 공통 validation으로 최소 세 feature group 비교
- leakage-safe final pipeline
- 오류 분석과 feature 선택 설명
- 검증을 통과한 `output/bike_submission.csv`
- 실제 Kaggle 업로드는 필수 아님
