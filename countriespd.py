import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/권미정/Desktop/프밍언어/advanced_python/week11/data/countries.csv")
#print(df.info())
#print(df.describe())
df['density']=df['population']/df['area']
#print(df)
#data1=df[df['density']>=300]
#print(data1)
gdp1=[32115,65717,41491,9979,11287]
df['gdp1']=gdp1
#print(df)
df.plot(kind='bar',x='country',y='gdp1',color='blue') #막대그래프
plt.show()