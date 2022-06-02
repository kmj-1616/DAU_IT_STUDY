from tkinter import *
def grade():
    score1=int(num1.get())
    score2=int(num2.get())
    avg=(score1+score2)/2
    if avg >=60:
        lblResult.configure(text=str(avg)+"합격입니다")
    else:
        lblResult.configure(text=str(avg)+"불합격입니다")
w=Tk()
w.geometry("200x100")
label1=Label(w, text="프로그래밍언어",fg="red")
label1.grid(column=0,row=0)
label2=Label(w, text="서비스기획",fg="red")
label2.grid(column=0,row=1)
num1=Entry(w,width=20)
num1.grid(column=1,row=0)
num2=Entry(w,width=20)
num2.grid(column=1,row=1)
button=Button(w,text="계산",command=grade)
button.grid(column=0,row=2,columnspan=2)
lblResult=Label(w,text=" ",fg="red")
lblResult.grid(column=0,row=3,columnspan=2)
w.mainloop()