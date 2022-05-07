##MSE 오차 계산하기
import numpy as np

ypred=np.array([1,0,0,0,0])
y=np.array([0,1,0,0,0])
n=5
MSE=(1/n)*np.sum(np.square(ypred-y))
print(MSE)
#결과: 0.4