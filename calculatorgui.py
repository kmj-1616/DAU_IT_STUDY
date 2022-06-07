from tkinter import *
w = Tk()
w.title("My Calculator")
display=Entry(w, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5) #컬럼 5개를 1개로 병합
button_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', ' ',
]
def click(key):
    if key=="=" :
        r=eval(display.get())
        s=str(r)
        display.insert(END, "=" + s) # =을 누르면 계산
    elif key=="C" :
        display.delete(0, END) # C를 누르면 처음부터 끝까지 삭제
    else :
        display.insert(END, key)
row_index=1
col_index=0
for btn_text in button_list :
    Button(w, text=btn_text, width=5, command=lambda key=btn_text : click(key)).grid(row=row_index, column=col_index) #버튼 클릭하면 삽입됨
    col_index+=1
    if col_index >=5:
        col_index=0
        row_index+=1
w.mainloop()