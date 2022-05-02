import numpy as np
data=np.array([[3,5,10],[8,10,12],[7,10,23]])
print(data.sum()) #전체의 합
#결과: 88
print(data.sum(axis=0)) #행의 합
#결과: [18 25 45]
print(data.sum(axis=1)) #열의 합
#결과: [18 30 40]
print(data.std(axis=0)) #행의 표준편차
#결과: [2.1602469  2.3570226  5.71547607]
