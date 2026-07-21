# Progress Tracking Workflow

Exercise 또는 Review Check가 통과되었을 때 적용한다.

## 완료 조건

다음 조건을 모두 확인한 뒤 완료로 기록한다.

- Exercise의 핵심 학습 목표가 확인되었다.
- 제출된 코드와 글 답안을 모두 요구한 경우 둘 다 검토했다.
- 중요한 오개념이나 실행 오류가 해결되었다.
- 남은 약점이 있다면 다음에 확인할 수 있는 형태로 기록할 수 있다.

## `progress.md` 갱신

현재 상태만 짧고 명확하게 유지한다.

- `Last Updated`
- `Current Phase`, `Current Week`, `Week Status`
- 완료한 Exercise와 답안 경로
- `Current Focus`, `Next Session Goal`
- Diagnostic Scores
- Active Weak Areas와 Follow-up Queue
- Week Advancement Evidence

완료 기록에는 핵심 증거와 답안 경로만 남긴다. 함수별 상세 설명은 해당 주차의 `notes/weekN.md`에 기록한다.

## `notes/weekN.md` 갱신

완료한 Exercise마다 현재 Week에 해당하는 파일에 다음을 누적한다.

- Phase, Week, Exercise 번호와 제목
- 완료 상태와 사용 데이터셋
- 실습 목표와 배운 개념
- 사용한 함수/메서드
- 새로 등장한 함수/메서드의 필요 이유, 주요 인수, 반환값, 원본 변경 여부, 재할당 필요 여부
- 이미 이전 노트에서 상세 설명한 함수/메서드는 반복 설명하지 않고, 이번 Exercise에서 어떤 역할로 다시 사용했는지만 짧게 기록
- 수정된 실수
- 초보자도 이해할 수 있는 핵심 정리

기존 기록은 삭제하거나 과거 관점으로 다시 쓰지 않는다. 명백한 사실 오류를 고칠 때만 최소 수정한다.

아직 해당 주차 파일이 없으면 `notes/weekN.md`를 새로 만든다. 예를 들어 Week 3 Exercise를 처음 완료하면 `notes/week3.md`를 만든다.

## Week 승급

- 단일 Exercise 완료만으로 Week를 자동 승급하지 않는다.
- 현재 Week의 필수 개념과 Review Check 완료 증거를 확인한다.
- 증거가 충분하면 승급을 `추천`하고, 사용자가 동의하거나 세션 맥락상 명시적으로 진행을 승인한 뒤 `Current Week`를 변경한다.
- 승급하지 않은 이유와 필요한 다음 증거를 `Week Advancement Evidence`에 남긴다.

## 일관성 확인

갱신 후 `python3 scripts/validate_bootcamp.py`를 실행한다. 검증 실패 시 사용자 학습 기록을 삭제하지 말고 원인을 수정한 뒤 다시 확인한다.
