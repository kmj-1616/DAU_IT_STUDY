#부산시 구/군별 경제지수 그래프 그리기
import pandas as pd
from matplotlib import font_manager
import matplotlib
import matplotlib.pyplot as plt
font_path = "C:/Windows/Fonts/H2GTRM.TTF"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font',family=font_name)
busan=pd.read_csv("./data/busanindex.csv")
busan.plot(kind='bar',x='SIG_KOR_NM',y='economic')
plt.title("부산 구/군별 경제지수")
plt.xlabel("구 이름")
plt.ylabel("경제지수")
plt.show()