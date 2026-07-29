# Week 5 Review Notes

## Phase 4/5 - Time-Series Foundations and Forecasting Models

현재 상태: 진행 중

운영 메모:

- 2026-07-29부터 `Sparta/` 자전거 수요예측 피처 엔지니어링 4회 특별수업을 먼저 진행한다.
- 기존 ARIMA/SARIMA 학습 목표는 완료 처리하지 않고 잠시 보류한다.
- 특별수업 결과는 피처 엔지니어링 보강 증거로 기록하며 Week 5 forecasting 완료 증거와 구분한다.
- `Sparta/`를 여러 Kaggle 대회를 수용하는 독립 Academy로 분리하고, 자전거 과정은 `Sparta/competitions/bike-sharing-demand/`에서 관리한다.
- 대회별 PLAN·progress·notes, Sparta 전용 session/review/tracking 규칙, 검증 스크립트와 네 개 Lesson notebook을 준비했다. 이는 수업 준비 기록이며 Exercise 통과 증거는 아니다.

선정 데이터:

- `data/week5_us_retail_sales_nsa.csv`
- FRED series: `MRTSSM44X72USN`
- 미국 Retail Trade and Food Services 판매액
- 월별, 비계절조정, 백만 달러 단위
- 1992-01부터 2026-05까지

첫 학습 목표:

- Trend, seasonality와 stationarity 진단을 첫 ARIMA 후보의 차수 선택과 연결한다.
- Persistence baseline과 ARIMA를 동일한 validation 기간에서 비교한다.

완료한 Exercise: 없음
