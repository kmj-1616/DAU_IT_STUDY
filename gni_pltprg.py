#1인당 국민총소득 그래프 그리기

#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
x=["2000","2005","2010","2015","2019"]
ko=[11030,18520,22290,28720,33720]
jp=[36230,40560,43440,38840,41690]
ch=[940,1760,4340,7940,10410]
plt.plot(x,ko)
plt.show() #한국의 1인당 국민총소득 그래프가 그려진다.

#옵션을 넣어보자.
plt.plot(x,ko,color="red",marker='o',linestyle='solid') #plt.plot(x,ko,'ro-')
plt.title("한국 1인당 국민소득")
plt.ylabel("dollars")
plt.xlabel("년도")
plt.savefig("한국 1인당 국민소득",dpi=600)
plt.show()

#한글로 처리하자.
import matplotlib.font_manager as fm
font_path="C:\\Windows\Fonts\malgun.ttf" #맑은 고딕 폰트를 font_path로 대입하기
font=fm.FontProperties(fname=font_path,size=18)
plt.plot(x,ko,color="red",marker='o',linestyle='solid') #=plt.plot(x,ko,'ro-')
plt.title("한국 1인당 국민소득",fontproperties=font)
plt.ylabel("dollars")
plt.xlabel("년도",fontproperties=font)
plt.savefig("한국 1인당 국민소득.png",dpi=600)
plt.show()

#아시아 1인당 국민소득 그래프를 만들어보자.
plt.plot(x,ko,'ro-')
plt.plot(x,jp,'b*--')
plt.plot(x,ch,'g+-.')
plt.title("아시아 1인당 국민소득",fontproperties=font)
plt.ylabel("dollars")
plt.xlabel("년도",fontproperties=font)
plt.savefig("아시아 1인당 국민소득.png",dpi=600)
plt.show()