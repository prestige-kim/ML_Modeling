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
