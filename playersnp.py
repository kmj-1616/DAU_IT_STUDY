import numpy as np
players=np.zeros((100,3)) #100행 3열에 0을 채움
players[:, 0]=np.random.normal(175,10,100) #첫 번째 열에 난수 발생(키)
players[:, 1]=np.random.normal(70,10,100) #두 번째 열에 난수 발생(몸무게)
players[:, 2]=np.int64(np.random.normal(24,10,100)) #세 번째 열에 정수형으로 난수 발생(나이)
print(players)
print(np.mean(players)) #전체 평균
print(np.mean(players, axis=0)) #행별 평균
print(np.median(players, axis=0)) #행별 중앙값
print(np.std(players, axis=0)) #행별 표준편차
print("상관계수=",np.corrcoef(players[:,0],players[:,1])) #키와 몸무게의 상관계수