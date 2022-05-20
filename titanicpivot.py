#타이타닉 데이터로 피벗테이블 만들기
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("./data/titanic.csv")
df.drop(['PassengerId','Ticket','Name'],axis=1,inplace=True) #열 삭제
table=df.pivot_table(df,['Sex','Pclass'], aggfunc={'Age':np.mean, 'Survived':np.sum}) #집계 함수 적용
print(table)
table.plot(kind='bar',color='red') #막대그래프 그리기
plt.show()