from tkinter import *
from tkinter import messagebox
def call() :
    print("안녕하세요 파이썬 수업 중입니다")
    messagebox.showinfo("Hi~", "파이썬 수업을 재미있게 하자!")

w=Tk()
w.title("2016677 권미정")
#객체 클래스는 속성f과 메소드m로 구성
w.geometry("250x200")
btnok=Button(w,text="확인", command=call) #확인 버튼 누르면 call 호출
btnok.pack() #.pack, .grid : 배치
w.mainloop()