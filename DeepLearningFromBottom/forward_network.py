# 3층으로 구성된 신경망 순전파 Numpy로 구현
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def init_network():
    # 파라미터 직접 정의
    network = {}
    network['W1'] = np.array([[1,2,3], [4,5,6]])    # shape(2,3) -> 입력 shape가 (2,)임
    network['b1'] = np.array([1, 1, 1])             # shape(3,)
    network['W2'] = np.array([[3,2], [4,5], [6,7]]) # shape(3,2) -> 1번 layer에서 나온 출력 shape가 (3,)임
    network['b2'] = np.array([1, 1])                # shape(2,)
    network['W3'] = np.array([[10, 11], [12, 13]])  # shape(2,2) -> 2번 layer에서 나온 출력 shape가 (2,)임
    network['b3'] = np.array([1, 1])                # shape(2,) 최종 출력 shape가 (2,)이기 때문
    
    return network
    
def forward(network, x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    # layer 1
    a1 = np.matmul(x, w1) + b1
    # layer 2
    a2 = np.matmul(a1, w2) + b2
    # layer 3
    a3 = np.matmul(a2, w3) + b3
    # activation
    y = sigmoid(a3)
    
    return y  # shape(2,)이어야 함

network = init_network()
x = np.array([158, 170])
y = forward(network, x)
print(y, y.shape)
