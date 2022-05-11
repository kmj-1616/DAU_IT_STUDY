#평균 175,표준편차 10인 정규분포를 따르는 도수가 1000인 히스토그램 그리기
import numpy as np
import matplotlib.pyplot as plt
h=np.random.normal(175,10,1000)
#h=175+10*np.random.randn(1000)
print(h.mean()) #평균 구하기
print(h.std()) #표준편차 구하기
plt.hist(h)
plt.show()