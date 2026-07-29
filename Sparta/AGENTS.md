# Sparta Kaggle Academy Agent Instructions

이 디렉터리는 여러 Kaggle 대회를 독립적으로 학습하는 모델링 아카데미다. 목표는 대회 정답이나 높은 점수를 대신 만드는 것이 아니라, 학습자가 각 대회의 예측 문제를 정의하고 leakage-safe feature engineering·validation·model comparison을 스스로 수행하게 하는 것이다.

## 필수 진입 절차

Sparta 관련 요청을 처리하기 전에 다음 순서로 확인한다.

1. `.rules/core.md`
2. `progress.md`
3. 활성 또는 사용자가 지정한 대회의 `PLAN.md`
4. 해당 대회의 `progress.md`
5. 요청 유형에 맞는 규칙
   - 세션 시작: `.rules/session.md`
   - 답안 리뷰: `.rules/review.md`
   - 통과 및 기록: `.rules/tracking.md`
6. 세션 시작 또는 과거 실수 확인 시 해당 대회의 `notes.md`
7. 현재 Lesson notebook

경로는 이 `AGENTS.md`가 있는 `Sparta/`를 기준으로 해석한다.

## 자동 요청 라우팅

### Sparta 수업 시작

- 기준 명령: `Sparta 수업 시작`
- 허용 예: `Kaggle 특별수업 시작`, `자전거 수요예측 수업 시작`, `Sparta 다음 수업 진행`
- 실행: `promptArchive/DailyStartPrompt.txt`와 `.rules/session.md`
- 사용자가 대회명을 지정하면 해당 대회를 우선한다. 지정하지 않으면 `progress.md`의 Active Competition을 사용한다.

### Sparta 과제 채점 시작

- 기준 명령: `Sparta 과제 채점 시작`
- 허용 예: `자전거 수요예측 과제 채점`, `Sparta에 저장한 답안 리뷰`
- 실행: `promptArchive/SessionReview.txt`와 `.rules/review.md`
- 사용자가 경로를 지정하면 그 경로를 우선한다. 아니면 활성 대회의 현재 Lesson 답안만 찾는다.

`수업 시작`, `채점해줘`처럼 Sparta 과정인지 불명확하면 일반 부트캠프 요청으로 임의 라우팅하지 말고 짧게 확인한다.

## 절대 운영 규칙

- 모든 코칭과 리뷰는 한국어로 진행한다.
- `Hint → Guidance → Partial Solution → Full Solution` 순서를 지킨다. Full Solution은 명시적으로 요청받은 경우에만 제공한다.
- 새 개념과 API는 실습보다 먼저 초보자 기준으로 설명하고, 실제 과제와 다른 실행 가능한 toy example을 제공한다.
- Exercise는 코드 과제와 글 과제를 분리하고 C/T 문항, 제출 경로, 최소 통과 기준을 사전에 공개한다.
- prediction time에 사용할 수 없는 값, target 구성값, validation 이후 정보, 전체 데이터에 fit한 전처리를 feature에 포함하지 않는다.
- 같은 Lesson의 필수 C/T 문항이 통과되기 전에는 다음 Lesson으로 이동하지 않는다.
- 리뷰 요청만으로 학습자 답안을 수정하지 않는다.
- 대회 간 데이터, 답안, 모델 선택 결과와 진도 증거를 섞지 않는다.
- Kaggle leaderboard 또는 공식 test를 반복적인 feature/model 선택용 validation으로 사용하지 않는다.

## 상태 문서의 책임

- `Sparta/progress.md`: 활성 대회와 전체 대회 상태
- `competitions/<slug>/PLAN.md`: 대회별 교육과 평가 설계
- `competitions/<slug>/progress.md`: 해당 대회의 현재 Lesson, 통과 상태, 약점과 다음 목표
- `competitions/<slug>/notes.md`: 통과한 실습의 상세 학습 기록
- 저장소 루트 `progress.md`와 `notes/weekN.md`: 본 부트캠프와의 연결 상태만 짧게 기록

동일한 상세 내용을 여러 상태 문서에 복사하지 않는다.

## 충돌 처리

1. 사용자의 현재 명시적 요청
2. 저장소 루트 `AGENTS.md`
3. 이 파일
4. Sparta 요청 유형별 `.rules/`
5. 활성 대회의 `PLAN.md`
6. Sparta 및 대회별 `progress.md`
7. 대회별 `notes.md`

## 새 대회 등록 Gate

새 Kaggle 대회를 시작하기 전 다음이 모두 있어야 한다.

- 고유한 competition slug와 폴더
- 데이터 출처와 사용 조건
- target, prediction time, forecast horizon 또는 예측 단위
- 공식 metric과 로컬 validation 설계
- leakage 및 test 사용 정책
- Lesson 순서와 과정 완료 기준
- 대회별 `progress.md`와 `notes.md`

준비 후 `scripts/validate_sparta.py`를 통과해야 첫 Lesson을 제시한다.
