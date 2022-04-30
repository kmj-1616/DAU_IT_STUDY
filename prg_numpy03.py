##화씨를 섭씨로 바꾸고 plot을 그리는 프로그램
import numpy as np #numpy 모듈 호출
import matplotlib.pyplot as plt #matplotlib 패키지 호출
ftemp=[63,73,80,86,84,78,66,54,45,63] #화씨온도
f=np.array(ftemp) #array 배열로 변환
c=(f-32)*0.55 #화씨를 섭씨로 변환
#plot 작성
plt.plot(c)
plt.show()