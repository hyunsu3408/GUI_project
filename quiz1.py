"""
메모장 프로그램 작성

조건1. title : 제목없음 - window 메모장
조건2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
조건3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2 저장 : mynote.txt. 파일에 현재 내용 저장하기
3-3 끝내기 : 프로그램 종료
조건4. 프로그램 시작 시 본문은 비어 있는 상태
조건5. 하단 status 바는 필요 없음
조건6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야함
조건7. 본문 우측에 상하 스크롤바 넣기
"""
from tkinter import *
import os

root = Tk()
root.title("제목없음-Windows 메모장")
root.geometry("640x480")


# 열기
def openfile():
    if os.path.isfile("mynote.txt"):
        with open("mynote.txt",'r',encoding="utf-8") as mynote :
            txt.delete("1.0",END)
            txt.insert(END,mynote.read())
    else:
        print("파일이 없습니다.")

# 저장
def savefile():
    if os.path.isfile("mynote.txt"):
        os.remove("mynote.txt")
        with open("mynote.txt",'w',encoding="utf-8") as mynote:
            mynote.write(txt.get("1.0",END))
    else:
        with open("mynote.txt",'w',encoding="utf-8") as mynote:
            mynote.write(txt.get("1.0",END))

# 끝내기
def quitfile():
    root.quit()

menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command=openfile)
menu_file.add_command(label="저장",command=savefile)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=quitfile)
menu.add_cascade(label="파일",menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
sb = Scrollbar(root)
sb.pack(side="right",fill="y")

# text 영역
txt = Text(root,yscrollcommand=sb.set)
txt.pack(side="left",fill="both",expand=True)


sb.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()