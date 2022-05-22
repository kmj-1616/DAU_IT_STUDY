import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({
    'name':['Kim','Lee','Park','Choi','Hong','Chung','Jang'],
    'age':[22,26,78,17,46,32,21],
    'city':['Seoul','Busan','Seoul','Busan','Seoul','Daejun','Daejun'],
    'children':[2,3,0,1,3,4,3],
    'pets':[0,1,0,2,2,0,3]
})

df.plot(kind='line',x='name',y='pets',color='red') #꺾은선그래프 그리기
plt.show()

ax=plt.gca() #중첩 차트 그리기
df.plot(kind='line',x='name',y='children',ax=ax)
df.plot(kind='line',x='name',y='pets',color='red',ax=ax)
plt.show()

df.plot(kind='bar',x='name',y='age') #막대그래프 그리기
plt.show()

df.plot(kind='scatter',x='children',y='pets',color='red') #산포도 그리기
plt.show()