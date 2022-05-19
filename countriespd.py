import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/권미정/Desktop/프밍언어/advanced_python/week11/data/countries.csv")
print(df.info()) #파일 정보 확인
print(df.describe()) #열 확인
df['density']=df['population']/df['area'] #인구밀도(density)=인구(population)%면적(area) 컬럼 생성하기
print(df)
data1=df[df['density']>=300] #인구밀도가 300 이상인 국가만 추출해 data1 데이터프레임 만들기
print(data1)
gdp1=[32115,65717,41491,9979,11287] #2019년 국민소득 시리즈(gdp1)를 열로 추가하기
df['gdp1']=gdp1
print(df)
df.plot(kind='bar',x='country',y='gdp1',color='blue') #막대그래프 그리기
plt.show()
