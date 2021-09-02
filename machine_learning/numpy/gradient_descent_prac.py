import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler

boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['PRICE'] = boston.target

# Scaling
scaler = MinMaxScaler()
scaled_featured = scaler.fit_transform(boston_df[['RM', 'LSTAT']])


# ============================
# Mini-batch SGD , Loss = MSE
# ============================
# 파라미터 업데이트 함수
def get_update_weights(bias, w1, w2, rm, lstat, target, learning_rate):
    # 데이터 개수
    N = len(target)

    # Loss function
    pred = (w1 * rm) + (w2 * lstat) + bias
    error = target - pred
    bias_factors = np.ones((N,))

    # 파라미터 업데이트 양
    w1_update = -learning_rate * (2 / N) * np.dot(rm.T, error)
    w2_update = -learning_rate * (2 / N) * np.dot(lstat.T, error)
    bias_update = -learning_rate * (2 / N) * np.dot(bias_factors.T, error)

    return w1_update, w2_update, bias_update


# Mini-batch GD 메소드 생성
def mini_batch_sgd(features, target, n_epochs=1000, batch_size=32, verbose=True):
    # 파라미터 초기화
    w1 = np.ones((1,))
    w2 = np.ones((1,))
    bias = np.ones((1,))

    # Feature
    rm = features[:, 0]
    lstat = features[:, 1]
    learning_rate = 0.01

    # Epoch 설정
    for epoch in range(n_epochs):
        for step in range(0, len(target), batch_size):
            # batch의 Feature
            rm_batch = rm[step: step+batch_size]
            lstat_batch = lstat[step: step+batch_size]
            target_batch = target[step: step+batch_size]

            # batch로 파라미터 업데이트
            w1_update, w2_update, bias_update = get_update_weights(bias, w1, w2,
                                                                   rm_batch, lstat_batch, target_batch,
                                                                   learning_rate)
            w1 = w1 - w1_update
            w2 = w2 - w2_update
            bias = bias - bias_update

            # Loss, 파라미터 값 출력
            if verbose:
                pred = (w1*rm) + (w2*lstat) + bias
                error = target - pred
                mse = round(np.mean(np.square(error)), 2)

                print('Epoch:', epoch, '/', n_epochs)
                print('# Parameter\n',)
                print('w1:', w1, 'w2:', w2, 'bias:', bias, 'MSE:', mse)

    return w1, w2, bias, mse

# Tensorflow
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

model = Sequential([
    Dense(1, input_shape=(2, ), activation=None, kernel_initializer='zeros',
          bias_initializer='zeros')
])
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse', metrics=['mse'])
model.fit(x=scaled_featured, y=boston_df['PRICE'].values, epochs=1000, batch_size=32)
prediction = model.predict(x=scaled_featured)