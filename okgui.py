##Ok Cancel 창 Tkinter 처리하기
from tkinter import *
def processOK():
    print("OK 버튼을 클릭했습니다.")
def processCancel():
    print("Cancel 버튼을 클릭했습니다.")

window=Tk() #창을 생성
btnOk=Button(window, text="Ok", fg="red", command=processOK())
btnCancel=Button(window, text="Cancel", fg="#ffff00", command=processCancel())

btnOk.pack()
btnCancel.pack()
window.mainloop() #이벤트 루프 생성하기