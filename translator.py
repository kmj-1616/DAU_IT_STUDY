from googletrans import Translator
from tkinter import *
translator = Translator()

def myFunc():
    d_src = translator.detect(TranslatorEntry.get())
    if var.get() == 1 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='ko')
    elif var.get() == 2 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='en')
    elif var.get() == 3 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='zh-cn')
    elif var.get() == 4 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='zh-tw')
    elif var.get() == 5 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='ja')
    elif var.get() == 6 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='fr')
    elif var.get() == 7 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='de')
    elif var.get() == 8 :
        result = translator.translate(TranslatorEntry.get(), src=d_src.lang, dest='ru')

    DetectLabel = Label(w, text=result.text, width=30, fg='blue')
    DetectLabel.grid(column=1, row=6, columnspan=2)

w=Tk()
w.title("번역기")
w.geometry("500x250")
w.resizable(False, False)

TranslatorEntryLabel = Label(w, text="번역할 문장: ", width=10)
TranslatorEntryLabel.grid(column=0, row=0)
TranslatorEntry=Entry(w, width=50, relief="sunken")
TranslatorEntry.grid(column=1, row=0, columnspan=2)

var=IntVar()
rb1=Radiobutton(w,text="한국어",variable=var,value=1)
rb2=Radiobutton(w,text="영어",variable=var,value=2)
rb3=Radiobutton(w,text="중국어(간체)",variable=var,value=3)
rb4=Radiobutton(w,text="중국어(번체)",variable=var,value=4)
rb5=Radiobutton(w,text="일본어",variable=var,value=5)
rb6=Radiobutton(w,text="프랑스어",variable=var,value=6)
rb7=Radiobutton(w,text="독일어",variable=var,value=7)
rb8=Radiobutton(w,text="러시아어",variable=var,value=8)

rb1.grid(column=1, row=1)
rb2.grid(column=1, row=2)
rb3.grid(column=1, row=3)
rb4.grid(column=1, row=4)
rb5.grid(column=2, row=1)
rb6.grid(column=2, row=2)
rb7.grid(column=2, row=3)
rb8.grid(column=2, row=4)

ConvertButton = Button(w, text="번역하기", overrelief="solid", command=myFunc)
ConvertButton.grid(column=1, row=5, columnspan=2)

w.mainloop()