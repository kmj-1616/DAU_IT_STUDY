##BMI 계산 윈도우창 설계
from tkinter import *
from tkinter import messagebox
def calBmi() :
    bmi = float(eWeight.get()) / float(eHeight.get())**2 #BMI 계산
    #label1['text'] = bmi
    messagebox.showinfo("당신의 bmi지수", bmi)

w=Tk()
w.title("20 권미정 (BMI 프로그램)") #창의 제목 표시
w.geometry("250x300") #창의 크기
label1=Label(w,text="몸무게(kg)", fg="blue") #레이블 위젯 생성, 글자색 설정
eWeight=Entry(w, text="") #한줄 텍스트 입력
label2=Label(w, text="신장(m)", fg="blue")
eHeight=Entry(w, text="")
btnOk=Button(w, text="확인", command=calBmi)
label1.grid(row=0, column=0) #레이블을 창에 배치
eWeight.grid(row=0, column=1)
label2.grid(row=1, column=0)
eHeight.grid(row=1, column=1)
btnOk.grid(row=2, column=0, columnspan=2)
w.mainloop() #사용자 이벤트를 대기