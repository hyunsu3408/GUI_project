from tkinter import *

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

# 문장 드래그해서, ctl+c, ctl+v 후 바꿀 문장적고 바꾸면 한번에 바뀜

# 맨 윗줄
btn_f16 = Button(root, text="F16",width =5, height =2)
btn_f17 = Button(root, text="F17",width =5, height =2)
btn_f18 = Button(root, text="F18",width =5, height =2)
btn_f19 = Button(root, text="F19",width =5, height =2)

# sticky=N+E+W+S,padx=3, pady=3 : 동서남북으로 붙게 하는 것
btn_f16.grid(row=0,column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0,column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3,sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="Clear",width =5, height =2)
btn_equal = Button(root, text="=",width =5, height =2)
btn_div = Button(root, text="/",width =5, height =2)
btn_mul = Button(root, text="*",width =5, height =2)

btn_clear.grid(row=1,column=0,sticky=N+E+W+S,padx=3, pady=3)
btn_equal.grid(row=1,column=1,sticky=N+E+W+S,padx=3, pady=3)
btn_div.grid(row=1,column=2,sticky=N+E+W+S,padx=3, pady=3)
btn_mul.grid(row=1,column=3,sticky=N+E+W+S,padx=3, pady=3)

# 7 시작 줄
btn_7 = Button(root, text="7",width =5, height =2)
btn_8 = Button(root, text="8",width =5, height =2)
btn_9 = Button(root, text="9",width =5, height =2)
btn_sub = Button(root, text="-",width =5, height =2)

btn_7.grid(row=2,column=0,sticky=N+E+W+S,padx=3, pady=3)
btn_8.grid(row=2,column=1,sticky=N+E+W+S,padx=3, pady=3)
btn_9.grid(row=2,column=2,sticky=N+E+W+S,padx=3, pady=3)
btn_sub.grid(row=2,column=3,sticky=N+E+W+S,padx=3, pady=3)

# 4 시작줄

btn_4 = Button(root, text="4",width =5, height =2)
btn_5 = Button(root, text="5",width =5, height =2)
btn_6 = Button(root, text="6",width =5, height =2)
btn_add = Button(root, text="+",width =5, height =2)

btn_4.grid(row=3,column=0,sticky=N+E+W+S,padx=3, pady=3)
btn_5.grid(row=3,column=1,sticky=N+E+W+S,padx=3, pady=3)
btn_6.grid(row=3,column=2,sticky=N+E+W+S,padx=3, pady=3)
btn_add.grid(row=3,column=3,sticky=N+E+W+S,padx=3, pady=3)

# 1 시작줄

btn_1 = Button(root, text="1",width =5, height =2)
btn_2 = Button(root, text="2",width =5, height =2)
btn_3 = Button(root, text="3",width =5, height =2)
btn_enter = Button(root, text="enter",width =5, height =2) #세로로 합쳐짐

btn_1.grid(row=4,column=0,sticky=N+E+W+S,padx=3, pady=3)
btn_2.grid(row=4,column=1,sticky=N+E+W+S,padx=3, pady=3)
btn_3.grid(row=4,column=2,sticky=N+E+W+S,padx=3, pady=3)
btn_enter.grid(row=4,column=3,rowspan=2,sticky=N+E+W+S,padx=3, pady=3)

# 0 시작줄

btn_0 = Button(root, text="0",width =5, height =2)
btn_point = Button(root, text=".",width =5, height =2)

btn_0.grid(row=5,column=0,columnspan=2,sticky=N+E+W+S,padx=3, pady=3)
btn_point.grid(row=5,column=2,sticky=N+E+W+S,padx=3, pady=3)


root.mainloop()