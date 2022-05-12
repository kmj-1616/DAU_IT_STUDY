#서울/부산의 기온 그래프
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
x=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
y1=[15.6,14.2,16.3,18.2,17.1,20.2,22.4]
y2=[20.1,23.1,23.8,25.9,23.4,25.1,26.3]
font_path="C:\\Windows\Fonts\malgun.ttf"
font=fm.FontProperties(fname=font_path,size=18)
f1=fm.FontProperties(fname=font_path).get_name()
plt.rc('font',family=f1) #모든 폰트 맑은고딕으로 설정
plt.plot(x,y1,label="서울")
plt.plot(x,y2,label="부산")
plt.title("서울/부산의 기온",fontproperties=font)
plt.ylabel("temperature")
plt.xlabel("day")
plt.legend() #범례 출력하기
plt.show()