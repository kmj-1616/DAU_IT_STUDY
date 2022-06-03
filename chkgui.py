from tkinter import *
from tkinter import messagebox
def fun1() :
    ans=messagebox.askyesno("확인","프로그램을 종료하시겠습니까?")
    if ans :
        w.destroy() #창을 닫고,메모리에서 지워줌
    else :
        w.title("취소하였습니다")
def funCheck() :
    if chk.get()==1:
        lbl.configure(text="재미있어요")
    else:
        lbl.configure(text="어려워요")
w=Tk()
w.title("20 권미정 (이벤트)")
w.geometry("400x250")
chk=IntVar()
cb=Checkbutton(w,text="파이썬은 재미있다",variable=chk,command=funCheck)
lbl=Label(w,text="",fg='red')
btn=Button(w,text="확인",command=fun1)
cb.pack()
btn.pack()
lbl.pack()
w.mainloop()