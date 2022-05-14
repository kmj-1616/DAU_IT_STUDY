#통계청 계절별 산불발생 현황 데이터 plot
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
x=["2019","2020","2021"]
y1=[392,381,158]
y2=[34,39,16]
y3=[30,83,25]
y4=[197,117,150]
font_path="C:\\Windows\Fonts\malgun.ttf"
font=fm.FontProperties(fname=font_path,size=18)
f1=fm.FontProperties(fname=font_path).get_name()
plt.rc('font',family=f1)
plt.plot(x,y1,label="봄(3~5월)")
plt.plot(x,y2,label="여름(6~8월)")
plt.plot(x,y3,label="가을(9~11월)")
plt.plot(x,y4,label="겨울(12,1~2월)")
plt.title("계절별 산불발생 현황",fontproperties=font)
plt.xlabel("기간")
plt.ylabel("계절")
plt.legend()
plt.show()