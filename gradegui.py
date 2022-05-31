from tkinter import *
from tkinter import messagebox
def grade():
    score=int(num1.get())
    if score >=60:
        messagebox.showinfo("당신은","합격")
    else:
        messagebox.showinfo("당신은","불합격")
w=Tk()
w.geometry("200x50")
label=Label(w, text="점수 입력")
label.grid(column=0,row=0)
num1=Entry(w,width=20)
num1.grid(column=1,row=0)
button=Button(w,text="계산",command=grade)
button.grid(column=0,row=1)
w.mainloop()