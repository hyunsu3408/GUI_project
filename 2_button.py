from tkinter import *

root = Tk()
root.title("hyunsu GUI")

btn1 = Button(root,text="버튼1")
btn1.pack()

# padx,pady는 여백 크기
btn2 = Button(root,padx=5, pady=10,text="버튼2")
btn2.pack()

btn3 = Button(root,padx=10, pady=5,text="버튼3")
btn3.pack()

# width,height 고정된 크기기
btn4= Button(root,width=10,height=3,text="버튼4")
btn4.pack()

btn5 = Button(root,fg="red", bg="yellow",text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_project\\image.png")
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print("버튼 클릭")

btn7 = Button(root,text="동작하는 버튼",command = btncmd)
btn7.pack()

root.mainloop()





