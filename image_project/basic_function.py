"""
project) 여러 이미지를 합치는 프로그램 만들기

-사용자 시나리오-
1. 사용자는 합치려는 이미지를 1개 이상 선택
2. 합쳐진 이미지가 저장될 경로를 지정한다
3. 가로넓이, 간격, 포맷 옵션을 지정한다.
4. 시작 버튼을 통해 이미지를 합친다
5. 닫기 버튼을 통해 프로그램을 종료한다.

-기능 명세-
1. 파일추가: 리스트 박스에 파일 추가
2. 선택삭제: 리스트 박스에서 선택된 항목 삭제
3. 찾아보기: 저장 폴더를 선택하면 텍스트 위젯에 입력
4. 가로넓이: 이미지 넓이 지정(원본유지,1024, 800, 640)
5. 간격: 이미지 간의 간격 지정(없음, 좁게, 보통, 넓게)
6. 포맷 : 저장 이미지 포맷지정(png,jpg,bmp)
7. 시작: 이미지 합치기 작업 실행
8. 진행상황: 현재 진행중인 파일 순서에 맞게 반영
9. 닫기 : 프로그램 종료
"""
from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox

root = Tk()
root.title("Hyunsu GUI")
# root.geometry("640x480")

# 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일 선택하세요",\
        filetypes= (("PNG 파일","*.png"),("모든 파일","*.*")),
        initialdir=r"C:\Users\hyunsu\study\python2\quiz\images") 
        # 최초에 사용자가 지정한 경로를 보여줌
    
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END,file)

# 선택 삭제 함수
def del_file():
    # reversed로 리스트 거꾸로 반환
    # 앞에서부터 지우면 인덱스가 앞으로 당겨져서 이상한게 지워질수 있기 때문
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None: # 취소 했을 때
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)

# 시작 함수
def start():
    # 각 옵션들 값을 확인
    print("가로넓이:",cmb_width.get())
    print("간격:",cmb_space.get())
    print("포맷:",cmb_format.get())
    
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return
    
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고","저장 경로를 선택하세요")
        
    

# 파일 프레임(파일추가,선택삭제)
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5,pady=5) # 간격 띄우기


btn_add_file= Button(file_frame,padx=5,pady=5,width=12,text="파일추가",command=add_file)
btn_add_file.pack(side="left")

btn_del_file=Button(file_frame,padx=5,pady=5,width=12,text="선택삭제",command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame,selectmode="extended",height=15,
    yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True,padx=5,pady=5)

# 저장 경로 프레임
path_frame = LabelFrame(root,text="저장경로")
path_frame.pack(fill="x",padx=5,pady=5,ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",expand=True,ipady=4,padx=5,pady=5)

btn_dest_path = Button(path_frame,text="찾아보기",width=10,command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5,pady=5)

# 옵션 프레임
frame_option = LabelFrame(root,text="옵션")
frame_option.pack(padx=5,pady=5,ipady=5)

# 1.가로 넓이 옵션
# 가로넓이 레이블
lbl_width = Label(frame_option,text="가로넓이",width=8)
lbl_width.pack(side="left",padx=5,pady=5)

# 가로넓이 콤보
opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(frame_option,state="readonly",values=opt_width,width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5,pady=5)

# 2.간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option,text="간격",width=8)
lbl_space.pack(side="left",padx=5,pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option,state="readonly",values=opt_space,width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5,pady=5)

# 3.파일 포맷 옵션
# 파일 포맷 레이블
lbl_format = Label(frame_option,text="포맷",width=8)
lbl_format.pack(side="left",padx=5,pady=5)

# 파일 포맷 콤보
opt_format = ["png","jpg","bmp"]
cmb_format = ttk.Combobox(frame_option,state="readonly",values=opt_format,width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5,pady=5)

# 진행 상황 progressbar
frame_progress = LabelFrame(root,text="진행상황")
frame_progress.pack(fill="x",padx=5,pady=5,ipady=5)

p_var = DoubleVar()
progress_bar= ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x",padx=5,pady=5,ipady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

# 닫기 버튼
btn_close = Button(frame_run,padx=5,pady=5,text="닫기",width=12,command=root.quit())
btn_close.pack(side="right",padx=5,pady=5)

# 시작 버튼
btn_start = Button(frame_run,padx=5,pady=5,text="시작",width=12,command=start)
btn_start.pack(side="right",padx=5,pady=5)

scrollbar.config(command=list_file.yview)
root.mainloop()
