#부산사회안전지수 파일 데이터 처리하기
import pandas as pd
import matplotlib.pyplot as plt
busan=pd.read_csv("./data/busanindex.csv")
print(busan['index']) #index만 추출하기
print(busan[['economic','heath','index']].corr()) #경제, 안전, index 상관계수 구하기
plt.scatter(busan['economic'],busan['index'],color="blue") #경제와 index의 산점도 그래프 그리기
plt.show() #거의 일직선 형태로, 상관관계가 크다는 걸 알 수 있다.