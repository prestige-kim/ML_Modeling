# Week 2 Review Notes

이 파일은 Week 2에서 실제로 배운 내용과 수정된 실수를 보존하는 누적 학습 기록이다.

`progress.md`는 현재 진도, 점수, 약점, 완료 상태를 추적한다.
`notes/week2.md`는 Week 2 Exercise에서 실제로 배운 내용, 사용한 함수/메서드, 실수에서 정리된 이해를 복습용으로 기록한다.

기록 절차는 `.rules/tracking.md`를 따른다. 기존 기록은 명백한 사실 오류를 수정하는 경우를 제외하고 삭제하거나 다시 쓰지 않는다.

---

## Phase 2 - Machine Learning Foundations
### Week 2 Exercise 1 - Modeling Problem Definition

완료 상태: 완료

사용한 데이터셋:

- `data/week1_macro_practice.csv`

실습 목표:

- 모델을 만들기 전에 예측 문제를 먼저 정의한다.
- 목표 변수와 예측 대상 시점을 구분한다.
- 예측 기간(Forecast Horizon)을 명확히 말한다.
- 설명 변수 후보는 데이터가 깔끔한지보다 예측 시점에 알 수 있는지로 판단해야 함을 이해한다.
- 데이터 누수(Data Leakage)가 왜 실제 예측 성능을 왜곡하는지 설명한다.

배운 내용:

- 목표 변수(Target Variable)는 모델이 예측하려는 컬럼이다.
  - 이번 문제에서는 `industrial_production_index`가 목표 변수다.
- 예측 대상 시점은 그 목표 변수의 어느 시점 값을 예측하는지이다.
  - 이번 문제에서는 다음 달의 `industrial_production_index`를 예측하려고 한다.
- 예측 기간(Forecast Horizon)은 현재 예측 시점에서 얼마나 미래를 예측하는지이다.
  - 이번 문제에서는 1개월 후를 예측한다.
- 예측 시점(Prediction Time)은 모델이 실제로 예측을 수행한다고 가정하는 순간이다.
- 설명 변수(Explanatory Variable)는 예측 대상과 관련이 있을 가능성이 있고, 예측 시점에 실제로 알 수 있는 정보여야 한다.
- 결측치가 있는 컬럼 자체가 곧바로 위험한 것은 아니다.
  - 위험한 것은 미래 정보를 사용해 결측치를 채우거나, 예측 대상 월의 정보를 설명 변수로 쓰는 것이다.
- 데이터 누수(Data Leakage)는 예측 시점에는 알 수 없는 정보를 모델이 사용해 평가 성능이 실제보다 좋아 보이는 문제다.

사용한 기존 함수/메서드:

- `pd.read_csv()`: Week 1에서 설명한 CSV 로딩 함수다. 이번에는 모델링 문제 정의 전에 실제 컬럼과 관측치를 확인하기 위해 다시 사용했다.
- `pd.to_datetime()`: Week 1에서 설명한 날짜 변환 함수다. 이번에는 예측 시점과 시간 순서를 다루기 위해 다시 사용했다.
- `.sort_values()`: Week 1에서 설명한 정렬 메서드다. 이번에는 시계열 예측 문제 정의 전에 날짜순으로 데이터를 맞추기 위해 다시 사용했다.

수정된 실수:

- 처음에는 목표 변수를 "다음 달 산업생산지수"라고 표현했지만, 이후 목표 변수는 `industrial_production_index`이고 예측 대상 시점이 다음 달이라는 점을 구분했다.
- 처음에는 설명 변수 후보를 결측치 유무 중심으로 생각했지만, 이후 예측 시점에 알 수 있는지와 경제적으로 관련 가능성이 있는지가 더 중요한 기준임을 정리했다.
- 처음에는 예측 시점에 알 수 있는 정보를 예측값과 혼동했지만, 이후 예측 시점까지 관측 또는 발표된 과거 및 현재 정보라고 정리했다.
- 데이터 누수를 단순히 과적합으로만 설명하기보다, 실제로 사용할 수 없는 미래 정보를 사용해 평가 성능이 왜곡되는 문제로 이해했다.

핵심 정리:

- 모델링은 모델을 고르는 것보다 예측 문제를 정의하는 것에서 시작한다.
- 목표 변수, 예측 대상 시점, 예측 기간, 예측 시점의 사용 가능 정보를 구분해야 한다.
- 다음 단계에서는 이 정의를 바탕으로 기준 모델(Baseline Model)을 만들기 전에 feature month와 target month를 명확히 맞춰야 한다.

---

### Week 2 Exercise 2 - Feature/Target Month Alignment

완료 상태: 완료

사용한 데이터셋:

- `data/week1_macro_practice.csv`

답안:

- `answers/code/week2/week2_2.ipynb`
- `answers/text/week2/week2_2.txt`

실습 목표:

- 1개월 Forecast Horizon에서 feature month와 target month를 구분한다.
- 한 학습 행이 "현재 시점에 아는 입력 정보"와 "다음 달의 정답"을 함께 담는 구조임을 이해한다.
- `industrial_production_index`의 다음 달 값을 `target_next_month`로 정렬한다.
- `shift(-1)`은 다음 달을 직접 찾는 함수가 아니라 다음 행의 값을 가져오는 함수임을 이해한다.
- 중복 행이 있으면 `shift(-1)` 결과가 왜 왜곡될 수 있는지 확인한다.
- 예측 시점에 알 수 없는 미래 설명 변수를 feature로 넣으면 Data Leakage가 된다는 점을 설명한다.

배운 내용:

- 모델은 각 행을 하나의 학습 문제로 본다.
  - feature는 문제를 풀 때 볼 수 있는 입력값이다.
  - target은 모델이 맞혀야 하는 정답이다.
- 1개월 Forecast Horizon에서는 feature month가 `t`이면 target month는 `t + 1`이다.
- 예를 들어 2023-05의 정보로 2023-06의 `industrial_production_index`를 예측한다면, 2023-06의 `industrial_production_index`는 target으로 붙일 수 있다.
- 반대로 2023-06의 `pmi`, `exports_usd_billion`, `cpi_yoy` 같은 설명 변수를 2023-05 행의 feature로 넣으면 예측 시점에 알 수 없는 미래 정보를 사용하는 것이므로 Data Leakage 위험이 있다.
- `shift(-1)`은 날짜를 이해해서 "다음 달"을 찾아주는 것이 아니라, 현재 정렬 상태에서 바로 다음 행의 값을 가져온다.
- 따라서 `shift(-1)` 전에 날짜순 정렬과 중복 행 확인이 필요하다.
- 이번 데이터에는 `2022-06-30` 중복 행이 있었고, 중복 제거를 하지 않으면 같은 달 중복 행이 다음 target처럼 붙을 수 있었다.
- 과제 질문이 일반적이면 답안도 일반적일 수 있으므로, 다음 세션부터는 구체 날짜, 컬럼명, 예측 시점과 통과 기준을 문항에 명시해야 한다.

사용한 기존 함수/메서드:

- `pd.read_csv()`: 원본 경제 데이터를 다시 불러오는 데 사용했다.
- `pd.to_datetime()`: 날짜 컬럼을 시간 정보로 다루기 위해 다시 사용했다.
- `.sort_values()`: `shift(-1)`이 다음 행을 가져오기 때문에, 날짜순 정렬을 보장하기 위해 다시 사용했다.

새로 배운 함수/메서드:

#### `.drop_duplicates()`

- 역할: 중복된 행을 제거한 새 DataFrame을 반환한다.
- 왜 필요한가: 월별 시계열에서는 한 달이 한 행이어야 하며, 중복 행이 있으면 `shift(-1)`이 다음 달이 아니라 같은 달의 중복 행을 target처럼 가져올 수 있다.
- 주요 인수:
  - 인수 없이 쓰면 모든 컬럼 값이 같은 행을 중복으로 본다.
  - `subset`: 특정 컬럼만 기준으로 중복 여부를 판단한다. 예: `subset="date"`.
  - `keep`: 중복 중 어느 행을 남길지 정한다. 예: `keep="first"`.
- 반환값: 중복이 제거된 새 DataFrame.
- 원본을 바꾸는가: 기본적으로 원본을 직접 바꾸지 않는다.
- 다시 저장해야 하는가: 중복 제거 결과를 계속 쓰려면 `ds = ds.drop_duplicates(...)`처럼 다시 저장해야 한다.

#### `.shift()`

- 역할: Series나 DataFrame의 값을 위아래로 이동시킨다.
- 왜 필요한가: 현재 행의 feature와 다음 행의 target을 같은 학습 행에 나란히 두기 위해 필요하다.
- 주요 인수:
  - `periods`: 몇 칸 이동할지 정한다.
  - `shift(-1)`: 다음 행의 값을 현재 행으로 가져온다.
  - `shift(1)`: 이전 행의 값을 현재 행으로 가져온다.
- 반환값: 값이 이동된 새 Series 또는 DataFrame.
- 원본을 바꾸는가: 원본 Series나 DataFrame을 직접 바꾸지 않는다.
- 다시 저장해야 하는가: 결과를 새 컬럼으로 쓰려면 `ds["target_next_month"] = ...`처럼 저장해야 한다.
- 이번 실습에서의 의미:
  - `ds["industrial_production_index"].shift(-1)`은 다음 행의 산업생산지수를 현재 행의 `target_next_month`로 가져왔다.

수정된 실수:

- 처음에는 feature month, target month, prediction time의 구분이 충분히 구체적이지 않았다.
- 이후 feature month는 입력 정보가 속한 월, target month는 맞혀야 하는 미래 월이라고 정리했다.
- 처음에는 Data Leakage를 과적합 쪽으로 설명했지만, 이후 예측 시점에 알 수 없는 미래 설명 변수를 feature로 넣는 문제라고 정리했다.
- 리뷰 과정에서 과제 질문이 일반적이었는데 구체 답변을 사후 요구하는 문제가 있었다.
- 이후 다음 세션부터 과제 문항에 구체 날짜, 컬럼명, 예측 시점, target 시점, 기대 답변 범위를 명시하기로 했다.

핵심 정리:

- 한 학습 행은 "이 시점에 아는 정보로 저 시점의 값을 예측하는 사례 하나"다.
- 미래 target을 정답으로 붙이는 것은 정상적인 지도학습 구조다.
- 미래 설명 변수를 feature로 넣는 것은 Data Leakage가 될 수 있다.
- `shift(-1)`을 쓰기 전에는 날짜순 정렬과 중복 행 확인이 필요하다.
- 다음 단계에서는 이 정렬된 학습 데이터 구조를 바탕으로 시간순 train/test split을 배운다.

---

### Week 2 Exercise 3 - Time-Series Train/Test Split

완료 상태: 완료

사용한 데이터셋:

- `data/week1_macro_practice.csv`

답안:

- `answers/code/week2/week2_3.ipynb`
- `answers/text/week2/week2_3.txt`

실습 목표:

- `target_next_month`가 있는 행만 학습 및 평가 후보로 사용한다.
- 시계열 데이터에서는 train과 test를 날짜순으로 나눠야 함을 이해한다.
- 2021-01-31부터 2023-12-31까지를 train, 2024-01-31부터 2024-11-30까지를 test로 나눈다.
- 무작위 8:2 분할과 시간순 8:2 분할을 구분한다.
- `2024-12-31` 행은 다음 달 정답이 없기 때문에 test에서 제외해야 함을 설명한다.

배운 내용:

- 시간순 train/test split은 과거 데이터로 학습하고 미래 데이터로 평가하기 위한 분할 방식이다.
- 이번 실습의 train 구간은 feature month 기준 `2021-01-31`부터 `2023-12-31`까지다.
- 이번 실습의 test 구간은 feature month 기준 `2024-01-31`부터 `2024-11-30`까지다.
- `2024-01` feature month의 target month는 `2024-02`이고, `2024-11` feature month의 target month는 `2024-12`다.
- `2024-12-31`은 데이터 안에 다음 달 `industrial_production_index`가 없으므로 `target_next_month`가 비고 평가에 사용할 수 없다.
- 날짜순으로 정렬한 뒤 앞 80%를 train, 뒤 20%를 test로 나누는 방식은 시간순 분할이므로 가능하다.
- 위험한 것은 월별 데이터를 무작위로 섞어 8:2로 나누는 방식이다. 이 경우 2024년 같은 미래 데이터가 train에 들어가 실제 예측 상황과 다른 평가가 될 수 있다.

사용한 기존 함수/메서드:

- `pd.read_csv()`: 원본 경제 데이터를 불러오는 데 사용했다.
- `pd.to_datetime()`: `date` 컬럼을 날짜 비교가 가능한 값으로 변환하는 데 사용했다.
- `.sort_values()`: `shift(-1)`과 시간순 분할 전에 날짜순 정렬을 보장하는 데 사용했다.
- `.drop_duplicates()`: 중복 월이 다음 target처럼 붙는 문제를 막기 위해 `shift(-1)` 전에 사용했다.
- `.shift(-1)`: 다음 행의 `industrial_production_index`를 현재 행의 `target_next_month`로 가져오는 데 사용했다.

새로 배운 함수/메서드 및 문법:

#### Boolean Filtering

- 역할: 조건을 만족하는 행만 선택한다.
- 왜 필요한가: 날짜 기준으로 train과 test를 나누기 위해 필요했다.
- 주요 형태: `ds["date"] <= target_date`
- 반환값: 조건을 만족하는 행만 남은 새 DataFrame.
- 원본을 바꾸는가: 원본을 직접 바꾸지 않는다.
- 다시 저장해야 하는가: 결과를 계속 쓰려면 `train = ...` 또는 `test = ...`처럼 저장해야 한다.
- 모델링 주의점: 날짜 조건을 잘못 잡으면 미래 데이터가 train에 들어가거나 정답이 없는 행이 test에 들어갈 수 있다.

#### `&`

- 역할: 여러 조건을 동시에 만족하는 행을 고른다.
- 왜 필요한가: test 구간을 `2024-01-31` 이후이면서 `2024-12-31`은 제외하는 방식으로 제한하기 위해 사용했다.
- 주요 형태: `(조건1) & (조건2)`
- 반환값: 각 행별 `True` 또는 `False` 조건 결과.
- 원본을 바꾸는가: 원본을 직접 바꾸지 않는다.
- 다시 저장해야 하는가: 필터링 결과를 쓰려면 변수에 저장해야 한다.
- 모델링 주의점: 괄호를 빼거나 조건을 잘못 쓰면 의도하지 않은 날짜가 train/test에 들어갈 수 있다.

#### `.dropna(subset=...)`

- 역할: 특정 컬럼에 결측치가 있는 행을 제거한 새 DataFrame을 반환한다.
- 왜 필요한가: `target_next_month`가 없는 행은 정답이 없으므로 학습이나 평가에 사용할 수 없기 때문이다.
- 주요 인수:
  - `subset`: 결측치 제거 기준으로 삼을 컬럼을 지정한다. 이번에는 `subset=["target_next_month"]`를 사용했다.
- 반환값: 지정한 컬럼의 결측 행이 제거된 새 DataFrame.
- 원본을 바꾸는가: 기본적으로 원본을 직접 바꾸지 않는다.
- 다시 저장해야 하는가: 계속 쓰려면 `ds = ds.dropna(...)`처럼 재할당해야 한다.
- 모델링 주의점: `subset` 없이 모든 결측치를 제거하면 target과 무관한 설명 변수 결측 때문에 의도보다 많은 행이 사라질 수 있다.

#### `.copy()`

- 역할: 필터링한 DataFrame의 독립적인 복사본을 만든다.
- 왜 필요한가: train과 test를 이후 별도 데이터셋으로 명확히 다루기 위해 사용했다.
- 반환값: 새 DataFrame.
- 원본을 바꾸는가: 원본을 직접 바꾸지 않는다.
- 다시 저장해야 하는가: 복사본을 쓰려면 `train = ...copy()`처럼 변수에 저장해야 한다.
- 모델링 주의점: `.copy()` 자체가 Data Leakage를 막지는 않는다. 누수를 막는 핵심은 시간순 날짜 조건이다.

수정된 실수:

- 처음에는 `dropna(subset=["target_next_month"])`를 실행만 하고 재할당하지 않아 target이 비어 있는 행이 남았다.
- 이후 `ds = ds.dropna(subset=["target_next_month"])`로 수정해 train과 test 모두 target 결측이 없도록 했다.
- 처음에는 test에 `2024-12-31`이 포함되었지만, 이후 제외 조건을 추가해 test가 `2024-01-31`부터 `2024-11-30`까지만 포함되도록 했다.
- 리뷰 과정에서 `month`를 묻는 질문에 정확한 `date`를 요구해 기준이 흔들렸다. 앞으로 정확한 날짜가 필요하면 문항과 통과 기준에 `date`라고 명시한다.

핵심 정리:

- 시계열 예측에서는 train이 test보다 과거여야 한다.
- `target_next_month`가 없는 행은 정답이 없으므로 학습과 평가에서 제외한다.
- 무작위 8:2 분할이 위험한 이유는 미래 시점의 데이터가 train에 섞일 수 있기 때문이다.
- 시간순으로 정렬한 뒤 앞 구간을 train, 뒤 구간을 test로 나누는 8:2 방식은 시계열 평가 원칙에 맞을 수 있다.
- 다음 단계에서는 이 train/test 구조 위에서 기준 모델(Baseline Model)을 만든다.

---

### Week 2 Exercise 4 - Baseline Prediction Definition

완료 상태: 완료

사용한 데이터셋:

- `data/week1_macro_practice.csv`

답안:

- `answers/code/week2/week2_4.ipynb`
- `answers/text/week2/week2_4.txt`

실습 목표:

- 복잡한 ML 모델 전에 비교 기준으로 사용할 기준 모델(Baseline Model)을 정의한다.
- 다음 달도 이번 달과 같을 것이라는 단순 기준 예측을 만든다.
- `baseline_pred_next_month`의 값 출처와 예측 대상 시점을 구분한다.
- 예측값을 `target_next_month`에서 가져오지 않고 feature month의 `industrial_production_index`에서 가져와야 함을 이해한다.
- `drop_duplicates()` 결과를 재할당한 뒤 `shift(-1)`을 실행해야 함을 다시 확인한다.

배운 내용:

- 기준 모델(Baseline Model)은 복잡한 모델이 최소한 이겨야 하는 비교 기준이다.
- 이번 기준 모델의 규칙은 "다음 달 `industrial_production_index`도 이번 달 `industrial_production_index`와 같을 것이다"이다.
- `baseline_pred_next_month`는 다음 달을 예측한 값이지만, 그 값의 출처는 같은 행의 feature month `industrial_production_index`다.
- 예를 들어 `2024-01-31` 행에서는:
  - prediction time: `2024-01-31`
  - target time: `2024-02-29`
  - feature로 사용할 수 있는 값: `2024-01-31`의 `industrial_production_index` = `108.4`
  - 실제 정답: `2024-02-29`의 `industrial_production_index`, 즉 `target_next_month` = `108.9`
  - 기준 모델 예측값: `baseline_pred_next_month` = `108.4`
- 같은 숫자라도 행에 따라 역할이 달라질 수 있다.
  - `2024-02-29`의 실제 산업생산지수는 `2024-01-31` 행에서는 target이고, `2024-02-29` 행에서는 feature month의 현재값이다.
- `target_next_month`를 예측값으로 복사하면 실제 정답을 미리 본 것이므로 Data Leakage가 된다.
- 상대경로는 notebook 파일 위치가 아니라 현재 작업 폴더(current working directory) 기준으로 해석될 수 있다.
  - 프로젝트 루트가 현재 작업 폴더이면 `data/week1_macro_practice.csv`가 맞다.
  - 현재 작업 폴더가 `answers/code/week2`이면 같은 파일을 가리키려면 `../../../data/week1_macro_practice.csv`처럼 상위 폴더 이동이 필요하다.
  - `os.getcwd()`로 현재 작업 폴더를 확인할 수 있다.

사용한 기존 함수/메서드:

- `pd.read_csv()`: 원본 경제 데이터를 불러오는 데 사용했다.
- `pd.to_datetime()`: `date` 컬럼과 날짜 기준값을 비교 가능한 날짜형으로 변환하는 데 사용했다.
- `.sort_values()`: `shift(-1)` 전에 날짜순 정렬을 보장하는 데 사용했다.
- `.drop_duplicates()`: `2022-06-30` 중복 행을 제거해 `shift(-1)`이 같은 달 중복 행을 다음 target처럼 가져오지 않도록 했다.
- `.shift(-1)`: 다음 행의 `industrial_production_index`를 현재 행의 `target_next_month`로 가져오는 데 사용했다.
- `.dropna(subset=["target_next_month"])`: 다음 달 정답이 없는 마지막 행을 학습 및 평가 후보에서 제외하는 데 사용했다.
- Boolean Filtering과 `&`: feature month 기준으로 train과 test 구간을 나누는 데 사용했다.
- `.copy()`: train과 test를 독립적인 DataFrame으로 다루는 데 사용했다.

새로 배운 개념:

#### Baseline Model

- 역할: 복잡한 모델과 비교할 최소 기준을 만든다.
- 왜 필요한가: ML 모델이 단순 기준보다 못하면, 복잡한 모델이 실제로 의미 있는 패턴을 배웠다고 보기 어렵기 때문이다.
- 이번 실습의 기준 규칙: 다음 달 값은 이번 달 값과 같다고 예측한다.
- 반환값: 특정 함수의 반환값이 아니라, 규칙에 따라 만든 예측 컬럼 `baseline_pred_next_month`.
- 원본을 바꾸는가: `test["baseline_pred_next_month"] = ...`처럼 새 컬럼을 만들면 `test` DataFrame에 컬럼이 추가된다.
- 다시 저장해야 하는가: 새 컬럼 대입은 별도 재할당이 필요 없지만, 이후 계속 쓸 DataFrame이 `test`인지 확인해야 한다.
- 모델링 주의점: `target_next_month`를 baseline 예측값으로 쓰면 정답을 복사하는 것이므로 Data Leakage다.

#### Current Working Directory

- 역할: 상대경로를 해석할 기준 폴더다.
- 왜 필요한가: 같은 `data/week1_macro_practice.csv`라도 notebook 커널이 어느 폴더에서 실행되는지에 따라 성공하거나 실패할 수 있기 때문이다.
- 확인 방법: `os.getcwd()`를 실행한다.
- 반환값: 현재 작업 폴더 경로 문자열.
- 원본을 바꾸는가: `os.getcwd()`는 현재 작업 폴더를 조회만 하며 바꾸지 않는다.
- 다시 저장해야 하는가: 확인 결과를 계속 쓰려면 변수에 저장할 수 있지만, 단순 확인만 할 때는 재할당이 필요 없다.
- 모델링 주의점: 경로가 깨져 다른 파일을 읽거나 파일을 읽지 못하면, 이후 모델링 결과를 신뢰할 수 없다.

수정된 실수:

- 처음에는 `drop_duplicates()`를 실행만 하고 재할당하지 않아 중복 행이 남은 상태로 `shift(-1)`이 실행되었다.
- 이후 `ds = ds.drop_duplicates()`로 수정하고 notebook을 다시 실행해 `2022-06-30` 중복 행이 한 행만 남는 것을 확인했다.
- 처음에는 수정 후 저장된 출력이 오래된 실행 결과와 섞여 있었지만, 이후 전체 셀을 다시 실행해 코드와 출력이 일치하도록 정리했다.
- 상대경로가 실패한 이유를 코드 문법 문제가 아니라 notebook의 현재 작업 폴더 문제로 구분했다.

핵심 정리:

- 기준 모델은 최종 모델이 아니라 복잡한 모델이 이겨야 하는 최소 비교 기준이다.
- 이번 기준 모델의 예측값은 feature month의 현재 산업생산지수에서 가져오고, 예측 대상은 target month의 산업생산지수다.
- `baseline_pred_next_month`와 `target_next_month`가 같은 뜻은 아니다.
- `target_next_month`는 실제 정답이고, `baseline_pred_next_month`는 예측 시점에 알 수 있는 현재값으로 만든 예측값이다.
- pandas 메서드가 새 DataFrame을 반환하는지 원본을 바꾸는지 확인하고, 필요한 경우 반드시 재할당해야 한다.
- notebook의 상대경로 문제는 `os.getcwd()`로 현재 작업 폴더를 확인한 뒤 판단한다.
