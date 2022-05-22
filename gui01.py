##윈도우 창 만들기
from tkinter import *
w=Tk()
w.title("20 권미정") #창의 제목 표시
w.geometry("400x100") #창의 크기
label=Label(w,text="안녕하세요") #레이블 위젯 생성
label.pack() #레이블을 창에 배치
w.mainloop() #사용자 이벤트를 대기