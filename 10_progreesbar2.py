from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root,maximum=100, length=150,variable=p_var2)
progressbar2.pack()


def btncmd():
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기
        
        p_var2.set(i) # progressbar 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root,text="시작",command=btncmd)
btn.pack()



root.mainloop()





