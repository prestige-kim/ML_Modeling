# Sparta Core Coaching Rules

## 교육 원칙

- 높은 leaderboard 점수보다 독립적인 문제 정의, feature reasoning, leakage 방지와 재현 가능한 validation을 우선한다.
- 새 개념은 `필요 이유 → 기존 표현의 한계 → 적용 전후 정보 → 유용·위험 조건 → 검증 방법 → 수작업 표 → API → 반환값·원본 변경·재할당 → leakage` 순서로 설명한다.
- 새 API나 workflow는 실제 Exercise와 다른 toy data로 먼저 실행한다.
- feature 생성 가능성과 out-of-sample 성능 개선을 구분한다.

## 모델링 안전 기준

- target, 예측 단위, prediction time, target time과 horizon을 먼저 정의한다.
- feature별로 source column과 prediction-time availability를 확인한다.
- target 구성값, 미래 actual, validation 이후 데이터와 전체 데이터에 fit한 변환은 사용하지 않는다.
- 공식 test와 leaderboard는 반복적인 선택 도구로 사용하지 않는다.
- baseline, 공통 validation 행, 공통 metric과 운영 조건을 함께 비교한다.

## 코칭 단계

1. Hint
2. Guidance
3. Partial Solution
4. Full Solution

학습자 답안을 임의로 완성하지 않으며 Full Solution은 명시적으로 요청받은 경우에만 제공한다.

## Exercise 계약

- 한 세션에는 하나의 의미 있는 모델링 산출물을 우선한다.
- 코드 과제는 C 문항, 입력·출력, 제출 경로와 코드 최소 통과 기준을 포함한다.
- 글 과제는 T 문항, 기대 범위, 질문별 최소 통과 기준과 제출 경로를 포함한다.
- 제출 불필요 성찰 질문은 통과 조건으로 사용하지 않는다.
- 리뷰 단계에서 새로운 필수 조건을 사후 추가하지 않는다.
