from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

# progressbar = ttk.Progressbar(root,maximum=100, mode= "indeterminate")
progressbar = ttk.Progressbar(root,maximum=100, mode= "determinate")
progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()


def btncmd():
    progressbar.stop() #작동중지

btn = Button(root,text="중지",command=btncmd)
btn.pack()



root.mainloop()





