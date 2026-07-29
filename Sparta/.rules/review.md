# Sparta Submission Review Workflow

## 리뷰 대상 확정

1. Active Competition과 Current Lesson을 확인한다.
2. 사용자가 경로를 지정하지 않았다면 현재 Lesson의 코드·글 답안만 선택한다.
3. Lesson notebook의 C/T 문항과 사전 공개된 최소 통과 기준을 체크리스트로 만든다.
4. notebook 코드 셀, 실행 순서, 출력, 오류, 경로와 재현성을 확인한다.
5. 글 답안이 코드 출력과 일치하는지 확인한다.

## 채점 형식

### 코드 과제

각 C 문항을 `충족`, `보완 필요`, `해당 없음`으로 판정한다.

### 글 과제

각 T 문항을 `충족`, `보완 필요`, `해당 없음`으로 판정한다.

### 필수 모델링 점검

- Correctness
- Prediction and modeling logic
- Data Leakage
- Validation quality
- Reproducibility

사전에 요구하지 않은 개선은 `추가 개선 제안`으로 분리하고 통과를 막지 않는다.

## 판정

- 모든 핵심 C/T 문항이 충족되고 실행·누수·평가 오류가 없으면 `Passed`
- 핵심 문항이 미충족이면 `Needs Revision`
- 사소한 표현·오탈자만으로 통과를 지연하지 않는다.
- `Needs Revision`이면 정확한 미충족 문항과 Hint만 제시하고 다음 Lesson으로 이동하지 않는다.
- 재제출에서는 기존 충족 문항을 반복 채점하지 않고 변경된 항목과 연관된 출력만 확인한다.
- 리뷰 요청만으로 학습자 파일을 수정하지 않는다.

통과 시 `.rules/tracking.md`를 적용한다.
