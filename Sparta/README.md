# Sparta Kaggle Modeling Academy

`Sparta/`는 여러 Kaggle 대회를 차례로 학습하는 독립 실습 시스템이다. 각 대회는 별도의 예측 문제, 데이터, Lesson, 답안, 평가 설계와 진도 기록을 가진다.

## 현재 과정

- Active competition: `bike-sharing-demand`
- 과정 경로: `competitions/bike-sharing-demand/`
- 현재 상태와 다음 목표: `progress.md`

## 공통 구조

```text
Sparta/
├── AGENTS.md
├── README.md
├── progress.md
├── .rules/
├── promptArchive/
├── scripts/
└── competitions/
    └── <competition-slug>/
        ├── PLAN.md
        ├── progress.md
        ├── notes.md
        ├── data/
        ├── lessons/
        ├── answers/
        └── output/
```

루트 파일의 역할:

- `AGENTS.md`: Sparta 요청의 자동 진입점과 명령 라우팅
- `.rules/`: 모든 Kaggle 과정에 공통인 세션·리뷰·추적 규칙
- `progress.md`: 현재 활성 대회와 전체 대회 목록의 단일 원본
- `scripts/validate_sparta.py`: 구조와 상태 일관성 검사

대회 폴더의 역할:

- `PLAN.md`: 해당 대회의 교육 목표, 데이터 계약, 평가 설계와 완료 기준
- `progress.md`: 현재 Lesson, 상태, 통과 증거, 활성 약점과 다음 목표
- `notes.md`: 통과한 실습에서 배운 내용과 교정된 실수
- `lessons/`: Concept Gate를 통과한 수업 notebook
- `answers/`: 학습자가 작성하는 코드·글 답안
- `output/`: validation으로 선택을 끝낸 뒤 만드는 최종 산출물

## 기준 명령

- `Sparta 수업 시작`: 활성 대회의 현재 Lesson을 시작한다.
- `Sparta 과제 채점 시작`: 활성 대회의 현재 Lesson 답안을 리뷰한다.
- 대회명을 함께 말하면 해당 대회를 우선한다. 예: `자전거 수요예측 수업 시작`.

현재 저장소 루트에서 그대로 명령하면 되며 `Sparta/`로 폴더를 이동할 필요가 없다.

권장 프롬프트:

```text
Sparta 수업 시작
Sparta에서 자전거 수요예측 수업 시작
Sparta 과제 채점 시작
Sparta의 자전거 수요예측 Lesson 1 과제 채점 시작
```

본 부트캠프를 시작할 때는 다음처럼 구분한다.

```text
머신러닝 부트캠프 수업 시작
오늘 수업 시작
```

`수업 시작해줘`, `다음 수업 진행해줘`처럼 시스템 이름도 기준 명령도 없는 표현은 자동 라우팅하지 않고 어느 수업인지 확인한다.

## 실행

저장소 루트에서 다음과 같이 Jupyter를 실행한다.

```bash
source .venv/bin/activate
jupyter notebook
```

상대경로는 현재 작업 폴더에 따라 해석되므로 notebook 첫 단계에서 `Path.cwd()`를 확인한다.

## 새 대회 추가 원칙

새 대회는 `competitions/<competition-slug>/` 아래에 독립적으로 추가한다. 기존 대회의 데이터, 답안, validation 결과를 새 대회와 섞지 않는다. 새 과정은 데이터 계약, prediction time, target, 공식 평가 지표, leakage 위험, validation 설계와 완료 기준을 `PLAN.md`에 먼저 확정한 뒤 시작한다.
