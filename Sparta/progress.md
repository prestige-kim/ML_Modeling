# Sparta Academy Progress

이 파일은 Sparta 전체의 활성 대회와 대회별 상위 상태를 기록하는 단일 원본이다. Lesson별 상세 상태는 각 대회의 `progress.md`에서 관리한다.

## Current State

| Field | Value |
|---|---|
| Last Updated | 2026-07-29 |
| Active Competition | bike-sharing-demand |
| Active Competition Path | `competitions/bike-sharing-demand` |
| Academy Status | In Progress |
| Current Lesson | Lesson 1 |
| Current Focus | 예측 단위·prediction time·target leakage를 정의하고 안전한 원본 feature와 시간 파생 feature를 공통 backtest로 비교함 |
| Next Action | `Sparta 수업 시작`으로 Bike Sharing Demand Lesson 1을 진행함 |

## Competition Registry

| Competition | Status | Current Lesson | Path |
|---|---|---|---|
| Bike Sharing Demand | Ready | Lesson 1 | `competitions/bike-sharing-demand` |

## Academy Rules

- 한 번에 하나의 Active Competition만 둔다.
- 대회 전환은 사용자의 명시적 요청 또는 동의 후 수행한다.
- 새 대회는 등록 Gate와 검증 스크립트를 통과한 뒤 시작한다.
- 완료된 대회의 데이터와 답안은 보존하며 다른 대회의 학습 증거로 자동 전용하지 않는다.
