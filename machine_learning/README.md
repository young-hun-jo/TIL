# 💡 사전에 가장 먼저 수행해야 할 일
- 이메일로 보내드린 ``LINEAD_ML_조영훈.zip`` 파일을 담당자님의 로컬 컴퓨터 환경변수 중 반드시 ``$HOME``(홈 디렉토리)에 다운로드 받아 주세요! 
```shell
# 반드시 아래의 디렉토리로 이동한 후 하단의 명렁어들 수행
$HOME/LINEAD_ML_조영훈
```
- 반드시 위 경로로 이동해야 아래의 학습 및 예측 코드, Flask 웹 서버 코드가 동작합니다!
- 패키지 의존성 충돌 방지를 위해 새로운 가상환경에서 아래의 명령어를 수행해 최적의 패키지 버전을 설치하세요!
- Python은 ``python==3.7.11`` 버전을 사용합니다.
```shell
pip install -r src/requirements.txt
```

# 🔖 Problem 1
- ``train.sparse.tsv``, ``test.sparse.tsv`` 데이터를 활용한 다중 분류 예측
## 🔗 Sparse 모델 학습 실행 방법
```shell
# 현재 디렉토리 경로: $HOME/LINEAD_ML_조영훈
python src/train/train_sparse.py
```
- 위 명령어 수행 시 다음과 같은 동작들이 수행
  - ``train.sparse.tsv`` 데이터 로드 및 전처리
  - 모델이 학습 후 학습 데이터에 대한 정확도 계산 및 출력
  - ``$HOME/LINEAD_ML_조영훈/model/`` 디렉토리에 ``model.dense.dat`` 파일로 새롭게 학습한 모델 저장(덮어쓰기)

## 🔗 Sparse 모델 예측 실행 방법
```shell
# 현재 디렉토리 경로: $HOME/LINEAD_ML_조영훈
python src/test/test_sparse.py [--retrain] [yes/no]
```
- 위 명령어 수행 시 가능한 옵션

|명령어|축약 명령어|의미|인자|기본값|
|---|---|---|---|---|
|``--retrain``|``-rt``|``train.sparse.tsv`` 데이터를 다시 학습하고 예측할 것인지|``yes`` 또는 ``no``|``no``|

- 위 명령어 수행 시 다음과 같은 동작들이 수행
  - 테스트 데이터인 ``test.sparse.tsv`` 로드 및 전처리
  - 만약 옵션 ``yes``로 설정 시, 학습 데이터인 ``train.sparse.tsv``로 모델 재학습 후 정확도 계산 및 출력
  - ``$HOME/LINEAD_ML_조영훈/model`` 디렉토리에 새롭게 학습한 모델 저장(덮어쓰기)
  - ``$HOME/LINEAD_ML_조영훈/result``디렉토리에 테스트 데이터 예측결과인 ``result.sparse.txt`` 파일로 저장

## 📊 분석 보고서
### 1. 데이터 탐색 및 피쳐 추출
- 전체 데이터 결측치 존재하지 않음

(1) **종속변수**(``label``)
- 범주형 변수이기 때문에 클래스의 분포도 확인<br><br>
<img width="600" alt="스크린샷 2021-11-18 오후 5 31 13" src="https://user-images.githubusercontent.com/54783194/142379662-2d4b409c-3012-45b6-ba1f-5a48103e5a41.png"><br>
- 클래스 분포가 카이제곱 분포를 띔
- 클래스 불균형 발견
  - 모델 개발 단계에서 성능 검증 시 클래스 분포를 고려해 학습/검증 데이터 분할 수행해야 함
  - 오버샘플링을 통해 클래스 균형 상태로 만들어준 후 모델의 성능 검증 시도

(2) **날짜 변수**
- 여기서 날짜변수란, 아래와 같이 필드의 값에 ``a_date`` 또는 ``c_date`` 문자열이 들어간 필드 2개를 의미<br><br>
![스크린샷 2021-11-18 오후 4 52 31](https://user-images.githubusercontent.com/54783194/142374460-974680be-f083-476b-b639-dc35a96874e2.png)
- 광고 카테고리 유형별에 따라 시간적인 특성이 있을 것으로 예상하여 해당 필드의 값을 ``pandas.datetime`` 형태로 전처리 수행 후 종속변수와 통계적 검정 수행
  - 변환된 ``datetime`` 형태의 필드로부터 해당 시간의 ``연도(year)``, ``월(month)``, ``시간대(hour)`` 을 파생변수로 생성
- ``a_date`` 또는 ``c_date`` 필드로부터 생성한 파생변수들(``연도(year)``, ``월(month)``, ``시간대(hour)``) 과 종속변수(``label``)와의 관계 파악을 위해 통계적 검정 수행
  - 두 범주형 변수 간의 관계 파악을 해야하고 종속변수 유형 모두가 하나의 모집단에 속하기 때문에 **독립성 검정**을 위해 **카이제곱 통계적 검정** 수행
  - 카이제곱 통계적 검정에서 **``p-value < 0.05``** 라면 두 범주형 변수 간의 관계가 있음을 의미<br><br>
  <img width="650" alt="스크린샷 2021-11-18 오후 5 37 03" src="https://user-images.githubusercontent.com/54783194/142380484-feb2a531-7828-43be-9db0-8d8a24432499.png"><br>
  - 위와 같이 통계적 검정 결과, 생성한 시간 관련 파생변수들 모두 종속변수에 따라 빈도차이가 존재하므로 종속변수와 관계가 있음을 알 수 있음
  - 따라서, 예측 모델 개발 시, Feature Engineering 으로 사용하기로 결정

(3) **다른 주어진 익명의 범주형 변수들**
- 먼저, 주어진 다른 변수들 중 아래 그림에서 ``ftr2``, ``ftr3``, ``ftr6``, ``ftr7`` 변수들과 종속변수 간의 관계 파악을 위해 동일하게 독립성 검정 수행
  - 여기서 피어슨 상관분석을 하지 않은 이유는 '과제 설명' 부분에서 필드 모두 문자열 형태의 데이터라고 했기 때문. 모두 문자열 데이터라는 것은 모두 범주형 데이터임을 의미
- ``ftr2``, ``ftr3``, ``ftr6``, ``ftr7`` 변수들과 종속변수 간의 독립성 검정 수행 결과는 아래와 같음<br><br>
<img width="650" alt="스크린샷 2021-11-18 오후 5 46 18" src="https://user-images.githubusercontent.com/54783194/142381821-0751b55a-7eb3-492f-a179-acc6cd86bd87.png"><br>
- 통계적 검정 결과, 다른 익명의 변수들도 모두 종속변수와 관계가 있다고 판단
- 따라서, 예측 모델 개발 시, 해당 변수들 모두 변수로 활용하기로 결정

(4) **Sparse한 익명의 변수**
- 여기서 'Sparse한 익명의 변수'란, 아래 그림에서 ``ftr1``을 의미<br><br>
<img width="550" alt="스크린샷 2021-11-18 오후 5 50 12" src="https://user-images.githubusercontent.com/54783194/142382450-402af6c1-3084-4568-b180-c5c7d7d4b75b.png"><br>
- 해당 변수에 들어있는 숫자들이 무엇을 의미하는 것인지 파악이 불가
- 광고 내용 텍스트의 단어들을 사전에 정의한 Vocabulary 범위의 인덱스로 매핑한 변수라고 생각해 0을 모두 제거
- 0 이외의 값들에 대해 벡터화 후 코사인 유사도를 계산하려 했으나 약 ``10만 x 1만 5천개 변수`` 형상의 Sparse한 행렬이 계산됨
- 이러한 너무 Sparse한 행렬을 변수로 활용한다면 차원의 저주에 걸릴 뿐만 아니라 모델의 오버피팅을 발생시킬 가능성이 농후하기 때문에 **과감히 제거**
### 2. 모델 선정
- 모든 변수가 범주형 변수이기 때문에 변수 값들을 Normalization 해서는 안 됨
- 따라서, 변수 값들을 Normalization 하지 않고 예측을 해야 하므로 **Tree 기반 모델**을 선정<br><br>
  - ``Decision Tree``
  - Bagging
    - ``Random Forest``
  - Boosting
    - ``XGBoost``
    - ``Light GBM``

### 3. 모델 비교 평가
- 클래스 불균형 문제를 해소하기 위해 다음과 같은 방법을 사용해 후보 모델들의 성능 검증
  - 소수 클래스에 속하는 데이터의 거리 주변에 원본 데이터와 동일하지 않으면서 소수 클래스에 속하는 가상의 데이터를 생성
    - K-NN 알고리즘 사용해 샘플링하는 SMOTE 오버샘플링 
  - 클래스 유형 별 개수를 고려해 학습, 검증 데이터를 분할하는 ``Stratified K-fold`` 교차검증 방법 수행(2만개 데이터씩 총 5번 검증 수행)
- 사용된 평가 지표: ``정확도(Accuracy)``, ``정밀도(Precision)``, ``재현율(Recall)``, ``F1-score``, ``AUC``, ``Training time``
- 하단은 5번의 교차 검증 수행한 결과 

|Model|Train Accuracy|Valid Accuracy|Valid Precision|Valid Recall|Valid F1-score|Valid AUC|Training time|
|---|---|---|---|---|---|---|---|
|**Decision Tree**|99.9%|98.8%|0.98|0.98|0.98|0.99|**2.2초**|
|Random Forest|99.9%|99.5%|0.99|0.99|0.99|0.99|52.5초|
|XGBoost|99.9%|98.7%|0.98|0.98|0.98|0.99|383.3초|
|Light GBM|17.2%|17.2%|0.25|0.17|0.15|0.56|27.2초|
- 위 표의 ``Training time``인 학습 시간은 오버샘플링 한 후인 약 64만 개의 데이터 학습 시간을 의미

### 4. 평가 결과
- ``Light GBM``을 제외한 모든 모델들의 성능이 매우 좋음
- 5번의 교차검증에도 불구하고 학습, 검증 데이터 간의 성능 차이가 거의 없으므로 테스트 데이터에 대한 모델의 성능 안정성도 보장
- 하지만 모델 학습 시간에 있어서 매우 큰 차이가 발생
- 따라서, 가장 빠른 학습속도를 보이는 **``Decision Tree``** 로 **최종 모델 선정**

### 5. 사후 분석
- 모델을 사후 분석하며 모델의 예측 성능에 영향을 미치는 변수 별 중요도 파악
  - Tree 기반 모델의 ``Feature Importance`` 기법 활용
    - 하지만 이 기법은 중복도가 낮은(Cardinality가 높은) 변수 중에 중요하지 않은데 중요하다고 여길 수도 있는 위험도가 있음
  - 따라서, 다른 방법으로 변수 하나씩 shuffle 후 예측력을 측정함으로써 shuffle 전 예측력보다 얼마나 저하되었는지 기준으로 변수의 중요도 판단하는 ``Permutation Importance`` 기법 활용<br><br>
<img width="1000" alt="스크린샷 2021-11-19 오후 3 54 55" src="https://user-images.githubusercontent.com/54783194/142578574-ea2478a7-9cd7-4c87-9d91-30d19da9bc18.png"><br><br>
- 위 그래프 분석 결과, 두 기법 모두 ``ftr2`` 이라는 주어진 변수가 가장 중요도가 높았고 다음으로 시간 관련 파생변수인 ``a_day``, ``a_hour``, ``a_month``를 중요한 변수라고 판단
- 따라서, 익명의 변수여서 구체적인 의미를 파악할 수는 없은 ``ftr2``가 광고 카테고리 예측에 매우 큰 역햘을 담당하며 다음으로 시간 관련 변수들도 예측력에 기여한다는 분석 결과가 도출

# 🔖 Problem 2
- ``train.dense.tsv``, ``test.dense.tsv`` 데이터를 활용한 다중 분류 예측
## 🔗 Dense 모델 학습 실행 방법
```shell
# 현재 디렉토리 경로: $HOME/LINEAD_ML_조영훈
python src/train/train_dense.py [--epochs] [int] [--batch_size] [int]
```
- 위 명령어 수행 시 가능한 옵션

|명령어|축약 명령어|의미|인자|기본값|
|---|---|---|---|---|
|``--epochs``|``-e``|딥러닝 모델 학습 Epoch 횟수|정수(``int``) 형태로 지정|45|
|``--batch_size``|``-b``|딥러닝 모델 Mini-batch 학습시 배치 사이즈|정수(``int``) 형태로 지정|2000|

- 위 명령어 수행 시 다음과 같은 동작들이 수행
  - ``train.dense.tsv`` 데이터 로드 및 전처리
  - 순수 ``numpy``로 구현한 은닉층이 4개인 Fully Connected layer 신경망 모델 학습
  - ``$HOME/LINEAD_ML_조영훈/model/`` 디렉토리에 ``model.dense.dat`` 파일로 새롭게 학습한 모델 저장(덮어쓰기)

## 🔗 Dense 모델 예측 실행 방법
```shell
# 현재 디렉토리 경로: $HOME/LINEAD_ML_조영훈
python src/test/test_dense.py [--retrain] [yes/no]
```
- 위 명령어 수행 시 가능한 옵션

|명령어|축약 명령어|의미|인자|기본값|
|---|---|---|---|---|
|``--retrain``|``-rt``|``train.dense.tsv`` 데이터를 다시 학습하고 예측할 것인지|``yes`` 또는 ``no``|``no``|

- 위 명령어 수행 시 다음과 같은 동작들이 수행
  - 테스트 데이터인 ``test.dense.tsv`` 로드 및 전처리
  - 만약 옵션 ``yes``로 설정 시, 학습 데이터로 모델 재학습 후 정확도 계산 및 출력
  - ``$HOME/LINEAD_ML_조영훈/model`` 디렉토리에 새롭게 학습한 모델 저장(덮어쓰기)
  - ``$HOME/LINEAD_ML_조영훈/result`` 디렉토리에 테스트 데이터 예측결과인 ``result.dense.txt`` 파일로 저장

## 📊 분석 보고서
### 1. 데이터 탐색
- 전체 데이터 결측치 존재하지 않음

(1) 종속변수(``label``)
- ``Problem 1`` 문제와 동일한 종속변수이므로 클래스 불균형, 분포도 동일
- 따라서, 클래스 불균형 존재하므로 모델 개발 시 클래스 분포를 고려한 교차 검증 수행해야 함

(2) 독립변수
- 200개의 실수형으로 이루어진 수치형 변수
- 200개의 변수에 대하여 하나씩 분포를 시각화 했을 때, 모두 정규분포 형태를 띔. 또한 아래처럼 200개 변수들의 평균값의 평균이 0에 매우 근사하고 표준편차값의 평균도 0에 근사하므로 표준정규분포 형태임을 알 수 있음<br><br>
<img width="540" alt="스크린샷 2021-11-19 오후 2 29 46" src="https://user-images.githubusercontent.com/54783194/142570349-c904cbab-3e35-4fc9-9934-4d3ce3021dc4.png"><br>

### 2. 독립변수와 종속변수 간의 관계 및 피쳐 선정
- 수치형 독립변수가 200개로 매우 많기 때문에 Feature Selection 과정을 수행해야 하므로 종속변수와 관계가 유의미한 독립변수들 파악 수행

(1) 피어슨 상관관계 분석
- 피어슨 상관관계 분석은 수치형 변수들간의 관계를 검정하는 기법
- 하지만 현재 레이블 유형이 수치화되어 있고 아래와 같이 클래스 유형별 개수를 파악해보면 **값이 큰 레이블일수록 개수가 적음**을 알 수 있음<br><br>
<img width="200" alt="스크린샷 2021-11-19 오후 2 42 30" src="https://user-images.githubusercontent.com/54783194/142571356-200eee01-5630-49e6-bbea-66761c566bba.png"><br><br>
- 따라서, 종속변수인 ``label`` 값이 클수록 양의 상관관계를 보이는 독립변수가 있다면 해당 독립변수의 값이 클수록 ``label`` 값이 클 것임을 알 수 있음
- 종속변수와 상관계수 값이 ``0.1`` 이상인 것들은 아래처럼 총 42개의 변수들임을 알 수 있음. 이를 하단의 ANOVA 분석결과와 비교<br>
<img width="600" alt="스크린샷 2021-11-19 오후 2 57 50" src="https://user-images.githubusercontent.com/54783194/142572796-a0503ca3-74bf-462f-bb44-92c086a98fe1.png">
<br>

(2) 이원 분산분석(Two-way ANOVA)
- 독립변수가 3개 이상일 때 집단(여기서는 ``label``) 유형 간의 평균 차이가 유의미한지 통계적으로 검정
  - ``귀무가설``: ``특정 독립변수는 레이블 유형에 따라 평균 차이가 없다``
  - ``p-value <0.05`` 라면, 귀무가설을 기각. 즉, 해당 독립변수와 종속변수 간의 관계가 존재
  - 종속변수와 관계가 없는 독립변수들을 파악<br><br>
<img width="249" alt="스크린샷 2021-11-19 오후 2 53 58" src="https://user-images.githubusercontent.com/54783194/142572462-b5c8162c-765b-43a0-a3f2-36930ee34b25.png"><br>

- (1) 피어슨 상관관계로 도출된 변수들은 ANOVA로 분석한 결과로 얻은 종속변수와 관계가 없는 변수들에 하나도 속하지 않았음.
- 심지어, ``p-value >= 0.05``인 종속변수와 관계가 없는 변수들의 피어슨 상관계수는 오히려 음수로 나왔음<br><br>
<img width="350" alt="스크린샷 2021-11-20 오후 7 36 20" src="https://user-images.githubusercontent.com/54783194/142723216-1b27ebf1-af0b-4821-aa7f-f7c58b99295d.png"><br>
- 따라서, 피어슨 상관계수 값이 ``0.1`` 이상인 42개의 변수들만을 선정해 입력 데이터로 넣기로 결정

### 3. 모델 선정
- ``Problem 1``에서 Tree 기반 모델이 좋은 성능을 보였으므로 이 문제에서도 Tree 기반 모델 사용 시도
- 이번엔 모든 변수가 실수형 변수이므로 딥러닝 신경망 모델 사용 시도
  - 단, 딥러닝 신경망은 오직 ``Numpy``만을 활용해 구현한 모델 사용
- 따라서, 성능 비교할 모델의 종류들은 아래와 같음<br><br>
  - ``Decision Tree``
  - Bagging
    - ``Random Forest``
  - Boosting
    - ``Light GBM``
  - ``Deep Learning(Fully Connected Layer)``

### 4. 모델 비교 평가
- 클래스 불균형 문제를 해소하기 위해 클래스 유형 별 개수를 고려해 데이터를 분할하는 ``Stratified K-fold`` 교차검증 방법을 수행(2만개 데이터씩 총 5번 수행)
  - 변수 개수가 너무 많기 때문에 오랜 모델 학습 시간으로 인해 ``Problem 1``과 달리 오버샘플링은 진행하지 않음
- 사용된 평가지표: ``정확도(Accuracy)``, ``정밀도(Precision)``, ``재현율(Recall)``, ``F1-score``, ``Training time``
- 하단은 5번의 교차 검증을 수행한 결과 표
  - 단, ``Deep Learning``의 평가지표는 1번의 교차검증만을 수행한 결과이며 ``Training Time``은 1번의 Epoch 당 시간을 의미

|Model|Train Accuracy|Valid Accuracy|Valid Precision|Valid Recall|Valid F1-score|Training time|
|---|---|---|---|---|---|---|
|Decision Tree|99.9%|90.3%|0.90|0.90|0.90|8.1초|
|Random Forest|99.9%|96.3%|0.96|0.96|0.96|64초|
|Light GBM|84.3%|80.8%|0.80|0.80|0.80|11.3초|
|Deep Learning|88.2%|87.9%|0.87|0.87|0.87|1.8초|

### 5. 평가 결과
- ``Random Forest`` 모델의 성능이 가장 좋지만 학습 시간이 약 1분 소요
- ``Decision Tree`` 모델은 성능이 대체로 좋지만 하이퍼파라미터 튜닝을 수행하여 오버피팅을 극복해야 함
- ``Light GBM`` 모델은 ``Problem 1`` 때와는 달리 높은 성능을 보여줌
- ML 라이브러리를 사용하지 않고 순수한 ``numpy``로만 구현한 ``Deep Learning`` 모델은 최상위 성능은 아니지만 양호한 성능을 보임
- 저장 후 웹 서버에서 사용할 모델로는 ``Deep Learning`` 으로 결정
  - 선정 이유
    - ML 라이브러리 없이 구현한 모델을 저장하고 로드 및 운영하는 방식을 배워보기 위해 선정
    - Epoch 횟수를 늘릴수록 정확도가 증가

### 6. 사후 분석
- 사후분석은 성능 측면에서 가장 좋았던 ``Random Forest`` 모델 기반으로 수행 
- ``Problem 1``과 동일하게 Tree 기반 모델의 ``Feature Importance`` 기법과 ``Permutation Importance`` 기법 2가지를 수행해 모델 예측력에 중요한 변수 분석
  - 단, ``Problem 2``의 데이터가 ``10만 x 42개의 변수`` 로 많기 때문에 ``Permutation Importance`` 기법 사용 시 반복 횟수는 5회로 제한<br><br>
<img width="1000" alt="스크린샷 2021-11-19 오후 4 17 09" src="https://user-images.githubusercontent.com/54783194/142581142-6ce535e9-9e74-450d-a404-b1c8da46ac2e.png"><br>
- 위 그래프 분석 결과, 빨간색 네모칸처럼 중요도가 가장 높은 공통의 상위 변수로는 ``ftr113``으로 존재하긴 하지만 해당 변수의 절대적인 중요도 값이 높은 편은 아님
- 따라서 모델의 예측력에는 42개의 모든 변수가 골고루 기여하는 것으로 판단
- 단, ``ftr7`` 변수의 의미가 익명이기 때문에 구체적인 변수의 의미는 파악이 불가하지만 광고 카테고리 예측에 가장 크게 기여하는 변수임은 분명한 것으로 도출

# 🔖 Problem 3
## 🔗 Flask 웹 서버에서 새로운 입력 데이터에 대한 예측 방법
- 하단의 명령어로 Flask 웹 서버 시작
```shell
# 현재 디렉토리 경로: $HOME/LINEAD_ML_조영훈
python src/main.py
```
- 서버 시작과 동시에 ``http://localhost:8080/update/model`` URL로 이동하면서 ``model.sparse.dat`` 모델을 로드

<img width="792" alt="스크린샷 2021-11-20 오후 10 00 51" src="https://user-images.githubusercontent.com/54783194/142727253-2839b695-1d93-4877-8361-b27a4c7b9e85.png"><br>
- 위 코드 수행 후, 아래의 URL로 이동하면 ``test.sparse.tsv`` 와 동일한 형태의 데이터를 입력시킬 수 있는 폼이 출력
```shell
http://localhost:8080/html/class.html
```
<img width="792" alt="스크린샷 2021-11-20 오후 6 53 40" src="https://user-images.githubusercontent.com/54783194/142722048-58a3e40e-3d73-41a4-966e-4d40592aa0fe.png"><br>
- 데이터 입력시킨 후 ``데이터 전송`` 버튼 누르면 입력시킨 데이터에 대한 레이블 예측 값이 아래처럼 출력

<img width="792" alt="스크린샷 2021-11-20 오후 6 53 49" src="https://user-images.githubusercontent.com/54783194/142722073-f8fafc3c-1cda-46bf-8cbe-9c5eb07599db.png"><br>

# 🗃 디렉토리 구조

```
📦 LINEAD_ML_조영훈
 ┣ 📜 README.md                -> 소스코드 실행 방법, 과제 결과에 대한 분석 리포트
 ┣ 📂 model                    -> 예측 모델 저장한 디렉토리
 ┃ ┣ 📜 model.sparse.dat       -> train.sparse.tsv 사용해 빌드한 예측 모델
 ┃ ┗ 📜 model.dense.dat        -> train.dense.tsv 사용해 빌드한 예측 모델
 ┣ 📂 result                   -> 테스트 데이터에 대한 예측 결과 저장
 ┃ ┣ 📜 result.sparse.txt      -> test.sparse.tsv 데이터에 대한 예측 결과
 ┃ ┗ 📜 result.dense.txt       -> test.dense.tsv 데이터에 대한 예측 결과
 ┣ 📂 src                      -> 소스 코드 디렉토리
 ┃ ┣ 📂 dataset                -> 학습 및 테스트 데이터가 있는 디렉토리
 ┃ ┃ ┣ 📜 train.sparse.tsv     -> sparse 학습 데이터
 ┃ ┃ ┣ 📜 train.dense.tsv      -> dense 학습 데이터
 ┃ ┃ ┣ 📜 test.sparse.tsv      -> sparse 테스트 데이터
 ┃ ┃ ┗ 📜 test.dense.tsv       -> dense 테스트 데이터
 ┃ ┣ 📂 page_view           
 ┃ ┃ ┗ 📜 view.py              -> 클라이언트가 전송한 sparse 데이터에 대해 예측한 결과를 웹 브라우저에 표시하는 소스코드
 ┃ ┣ 📂 preprocess         
 ┃ ┃ ┗ 📜 input.py             -> 클라이언트가 전송한 sparse 데이터를 모델에 맞게 전처리하는 소스코드
 ┃ ┣ 📂 templates
 ┃ ┃ ┗ 📜 class.html           -> 클라이언트가 전송할 데이터를 입력하는 웹 브라우저를 구성하는 HTML
 ┃ ┣ 📂 test               
 ┃ ┃ ┣ 📜 test_sparse.py       -> test.sparse.tsv 데이터에 대해 예측 수행하는 소스코드
 ┃ ┃ ┗ 📜 test_dnese.py        -> test.dense.tsv 데이터에 대해 예측 수행하는 소스코드
 ┃ ┣ 📂 train                  -> sparse, dense 데이터를 모델이 학습하는 소스코드가 담겨 있는 디렉토리
 ┃ ┃ ┣ 📂 common               -> 순수 Numpy로 신경망을 구현하기 위해 필요한 함수들이 담긴 디렉토리
 ┃ ┃ ┃ ┣ 📜 functions.py       -> 다양한 활성함수, 손실함수가 담겨 있는 소스코드
 ┃ ┃ ┃ ┣ 📜 gradients.py       -> 수치 미분을 계산하는 함수
 ┃ ┃ ┃ ┣ 📜 layers.py          -> 활성화 함수가 적용된 행렬 곱 계층을 구현한 소스코드
 ┃ ┃ ┃ ┣ 📜 multi_fc_layer.py  -> 다층 신경망 빌드, 오차역전파 수행해 파라미터의 기울기를 구하는 소스코드
 ┃ ┃ ┃ ┗ 📜 optimizers.py      -> 기울기를 기반으로 파라미터를 갱신하는 최적화 기법을 구현하는 소스코드(SGD, Momentum, Adam 등)
 ┃ ┃ ┣ 📜 train_sparse.py      -> train.sparse.tsv 데이터를 학습하는 소스코드
 ┃ ┃ ┗ 📜 train_dnese.py       -> train.dense.tsv 데이터를 학습하는 소스코드
 ┃ ┣ 📂 update_models          
 ┃ ┃ ┗ 📜 update.py            -> Flask 웹 서버 시작 시, model.sparse.model을 로드하는 소스코드
 ┃ ┣ 📜 main.py                -> Flask 웹 서버 시작하는 메인 스크립트 소스코드
 ┃ ┣ 📜 observer.py            -> model.sparse.dat 파일이 변경된 경우, 감지한 후 모델 재로드 하는 소스코드
 ┗ ┗ 📜 requirements.txt       -> 해당 소스코들을 모두 안정적으로 수행하기 위해 필요한 패키지 버젼
```
# ⚙️ 패키지 설치 dependency

```
autopep8==1.6.0
certifi==2021.10.8
click==8.0.3
Flask==2.0.2
importlib-metadata==4.8.2
itsdangerous==2.0.1
Jinja2==3.0.3
joblib==1.1.0
MarkupSafe==2.0.1
numpy==1.21.4
pandas==1.3.4
pycodestyle==2.8.0
python-dateutil==2.8.2
pytz==2021.3
scikit-learn==1.0.1
scipy==1.7.2
six==1.16.0
threadpoolctl==3.0.0
toml==0.10.2
typing_extensions==4.0.0
watchdog==2.1.6
Werkzeug==2.0.2
zipp==3.6.0
```

