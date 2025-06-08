from tkinter import *

root = Tk()
root.title("hyunsu GUI")
root.geometry("640x480+350+200")

menu = Menu(root)


def create_new_file():
    print("새 파일을 만듭니다")

# File 메뉴
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New file",command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()
menu_file.add_command(label="Open File..")
menu_file.add_separator()
menu_file.add_command(label="Save all",state="disable")# 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File",menu=menu_file)

# Edit 메뉴
menu.add_cascade(label="Edit")

# language 메뉴 추가 (radio 버튼 통해서 택1)
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

# View 메뉴

menu_view= Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menu.add_cascade(label="View",menu=menu_view)


root.config(menu= menu)

root.mainloop()





