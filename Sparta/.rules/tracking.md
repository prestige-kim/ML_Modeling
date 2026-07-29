# Sparta Progress Tracking Workflow

## 통과 기록 조건

- 코드와 글이 모두 요구된 경우 두 답안을 모두 검토했다.
- 현재 Lesson의 핵심 C/T 문항이 충족됐다.
- 실행 오류, target leakage와 잘못된 validation이 해결됐다.
- 남은 약점이 다음 세션에서 확인 가능한 문장으로 정리됐다.

## 대회별 기록

해당 대회의 `progress.md`에 다음만 기록한다.

- Last Updated
- Current Lesson과 Lesson Status
- 통과한 Lesson과 답안 경로
- 핵심 모델링 증거
- Active Weak Areas
- Follow-up Queue
- Next Session Goal

상세 개념, 새 API의 역할과 교정된 실수는 해당 대회의 `notes.md`에 누적한다.

## Sparta 상위 기록

`Sparta/progress.md`에는 Active Competition, Current Lesson, 상위 상태와 다음 행동만 동기화한다. Lesson 세부 점수나 함수 설명은 복사하지 않는다.

저장소 루트 `progress.md`와 현재 Week notes에는 본 부트캠프와 연결되는 한 줄 요약만 기록한다. Sparta의 상세 상태를 중복 기록하지 않는다.

## 승급

- 현재 Lesson이 `Passed`가 아니면 다음 Lesson으로 이동하지 않는다.
- 통과 후 다음 Lesson을 `Ready`로 바꾸고 사용자의 진행 의사를 확인한다.
- 마지막 Lesson 통과 후 대회 `PLAN.md`의 전체 완료 기준과 최종 산출물을 검증한다.
- 대회 완료는 사용자에게 추천하고 동의를 받은 뒤 `Completed`로 변경한다.

## 검증

기록 갱신 후 저장소 루트에서 다음을 실행한다.

```bash
.venv/bin/python Sparta/scripts/validate_sparta.py
python3 scripts/validate_bootcamp.py
```

실패하면 학습 기록을 삭제하지 않고 상태·경로 불일치를 수정한 뒤 다시 실행한다.
