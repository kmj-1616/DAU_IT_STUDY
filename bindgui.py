from tkinter import *
from tkinter import messagebox
def fun1() :
    ans=messagebox.askyesno("확인","프로그램을 종료하시겠습니까?")
    if ans :
        w.destroy()
    else :
        w.title("취소하였습니다")
def funCheck() :
    if chk.get()==1:
        lbl.configure(text="재미있어요")
    else:
        lbl.configure(text="어려워요")
def funRadio() :
    if var.get()==1 :
        lbl.configure(text="파이썬을 선택하셨습니다")
    elif var.get()==2 :
        lbl.configure(text="웹프로그래밍을 선택하셨습니다")
    else:
        lbl.configure(text="데이터베이스를 선택하셨습니다")
def mouse(event):
    lbl.configure(text=str(event)+"눌렀습니다.")
def keyEvent(event) :
    lbl.configure(text="눌린 키==>"+chr(event.keycode))
w=Tk()
w.title("20 권미정 (이벤트)")
w.geometry("400x250")
chk=IntVar()
cb=Checkbutton(w,text="파이썬은 재미있다",variable=chk,command=funCheck)
var=IntVar()
rb1=Radiobutton(w,text="프로그래밍 언어",variable=var,value=1,command=funRadio)
rb2=Radiobutton(w,text="웹프로그래밍",variable=var,value=2,command=funRadio)
rb3=Radiobutton(w,text="데이터베이스",variable=var,value=3,command=funRadio)
lbl=Label(w,text="",fg='red')
btn=Button(w,text="확인",command=fun1)
cb.pack()
rb1.pack()
rb2.pack()
rb3.pack()
btn.pack()
lbl.pack(side=BOTTOM)
w.bind("<Button-1>", mouse) #마우스 왼쪽 클릭 시
w.bind("<Button-3>", mouse) #마우스 오른쪽 클릭 시
w.bind("<B1-Motion>", mouse) #마우스 왼쪽으로 드래그할 때
w.bind("<Key>",keyEvent) #키보드가 눌릴 때
w.mainloop()