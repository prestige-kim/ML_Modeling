# Machine Learning Modeling Practice

경제 및 시계열 데이터를 활용해 데이터 확인, 전처리, 예측 문제 정의, 기준 모델 평가를 연습하는 저장소다.

이 저장소는 공개용 학습 자료와 재현 가능한 실행 환경만 포함한다. 개인 학습 진행 기록, 제출 답안, 에이전트 운영 규칙, 세션 프롬프트는 로컬 전용 파일로 관리한다.

## Repository Structure

```text
.
├── README.md
├── requirements.txt
└── data/
    └── week1_macro_practice.csv
```

## Dataset

`data/week1_macro_practice.csv`는 월별 거시경제 연습 데이터다.

주요 컬럼:

- `date`
- `industrial_production_index`
- `pmi`
- `policy_rate`
- `exports_usd_billion`
- `imports_usd_billion`
- `cpi_yoy`
- `unemployment_rate`

## Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
jupyter notebook
```

notebook에서는 가능하면 사용자 컴퓨터의 절대 경로 대신 저장소 기준 상대 경로를 사용한다.

## Scope

이 공개 저장소는 실습 데이터와 환경 정의를 공유하기 위한 용도다. 개인별 답안, 피드백, 진도 기록은 포함하지 않는다.
