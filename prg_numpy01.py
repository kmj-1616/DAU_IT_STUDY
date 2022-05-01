import numpy as np
a=[10,25,30] #list
b=[5,10,10] #list
a1=np.array(a)
b1=np.array(b)
print(a1[0]) #array도 index로 원소를 구분한다
print('배열합=',a1+b1) #array의 합
print('배열곱=',a1*b1) #array의 곱
print(a+b) #리스트