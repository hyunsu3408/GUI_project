from tkinter import *

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

txt = Text(root,width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # 글자 미리삽입

e = Entry(root,width=30) # 한줄로 입력 받고싶을때 Entry 사용
e.pack()
e.insert(0,"한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END)) # 1.0 의미는 1: 첫번째라인 0 :  0번째 컬럼, END까지 가져오기
    print(e.get())

    # 텍스트 삭제
    txt.delete("1.0",END)
    e.delete(0,END)


btn = Button(root,text="클릭",command=btncmd)
btn.pack()



root.mainloop()





