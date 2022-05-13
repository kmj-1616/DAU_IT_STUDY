#titanic 데이터 다루기, python console에서 진행
import pandas as pd
titanic=pd.read_csv("C:/Users/권미정/Desktop/프밍언어/titanic.csv")
#타이타닉 탑승객의 이름,나이,성별?
titanic[["Name","Age","Sex"]]
#20세 미만의 승객 중 10명만?
b=titanic[titanic["Age"]<20]
b.head(10)
#20세 미만의 승객의 이름만?
titanic.loc[titanic["Age"]<20,"Name"]
#20행에서 23행, 5열에서 7열만?
titanic.iloc[20:23,5:7]
#각 성별의 평균 연령?
titanic[["Sex","Age"]].groupby("Sex").mean()
#각 승객 등급의 수?
titanic["Pclass"].value_counts()
#나이 기준으로 데이터 정렬
titanic.sort_values(by="Age").head()
#1순위 탑승등급, 2순위 나이 기준으로 내림차순 데이터 정렬
titanic.sort_values(by=['Pclass','Age'],ascending=False).head()