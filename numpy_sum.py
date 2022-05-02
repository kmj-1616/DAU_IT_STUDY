import numpy as np
data=np.array([[3,5,10],[8,10,12],[7,10,23]])
print(data.sum()) #전체의 합
print(data.sum(axis=0)) #행의 합
print(data.sum(axis=1)) #열의 합
print(data.std(axis=0)) #행의 표준편차