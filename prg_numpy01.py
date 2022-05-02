#정규분포의 난수 발생하여 데이터 생성
import numpy as np
import matplotlib.pyplot as plt
y=np.random.normal(5,2,10000)
plt.hist(y)
plt.show()