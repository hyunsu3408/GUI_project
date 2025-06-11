from tkinter import *

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

listbox = Listbox(frame,selectmode="extended",height=10,yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 매핑해줘야 함

root.mainloop()





