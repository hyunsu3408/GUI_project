from tkinter import *

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

label1= Label(root, text="하이")
label1.pack()

photo = PhotoImage(file="gui_project\\image.png")
label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="또 만나")

    global photo2 # 전역변수로 해야 GC가 메모리에서 삭제 안함
    photo2=PhotoImage(file="gui_project\\image2.png")
    label2.config(image=photo2)
    
btn = Button(root,text="클릭",command=change)
btn.pack()


root.mainloop()





