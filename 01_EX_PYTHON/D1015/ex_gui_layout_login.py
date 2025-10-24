## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## LogIn 화면 구성
## - 사용 Widget
##   * Label     : LOGIN 제목, ID, PW 표시
##   * Entry     : ID, PW 입력창
##   * Button    : OK, Cancel 버튼
##   * Frame     : 위젯을 구역별로 묶어서 레이아웃 정리
##   * padx     - 왼쪽, 오른쪽 바깥여백 설정
##   * pady     - 위쪽, 아래쪽 바깥여백 설정
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
from tkinter import *

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
window = Tk()
window.title("LOGIN")
window.geometry("300x200+500+300")
window.resizable(False, False)

## --------------------------------------------------------------------
##- Frame 구역 나누기
##   top_frame  : LOGIN 제목
##   form_frame : ID / PW 입력 라인
##   btn_frame  : OK / Cancel 버튼
## --------------------------------------------------------------------
top_frame = Frame(window)
top_frame.pack(pady=10)

form_frame = Frame(window)
form_frame.pack(pady=10)

btn_frame = Frame(window)
btn_frame.pack(pady=10)

## --------------------------------------------------------------------
##- LOGIN 제목
## --------------------------------------------------------------------
msgLB1 = Label(top_frame, text="LOGIN", foreground='black', font=('Arial', 16, 'bold'))
msgLB1.pack()

## --------------------------------------------------------------------
##- ID / PW 입력 필드
## --------------------------------------------------------------------
# Label (왼쪽) + Entry (오른쪽)
msg_id = Label(form_frame, text="ID", width=8, anchor="w")
input_id = Entry(form_frame, width=20)

msg_pw = Label(form_frame, text="PW", width=8, anchor="w")
input_pw = Entry(form_frame, width=20, show="*")  # 비밀번호는 *로 표시

# grid로 정렬
msg_id.grid(row=0, column=0, padx=5, pady=5)
input_id.grid(row=0, column=1, padx=5, pady=5)
msg_pw.grid(row=1, column=0, padx=5, pady=5)
input_pw.grid(row=1, column=1, padx=5, pady=5)

## --------------------------------------------------------------------
##- 버튼 (OK / Cancel)
## --------------------------------------------------------------------
btn_ok = Button(btn_frame, text="OK", width=10, bg="lightblue")
btn_cancel = Button(btn_frame, text="Cancel", width=10, bg="lightgray")

btn_ok.pack(side="left", padx=15)
btn_cancel.pack(side="left", padx=15)

## --------------------------------------------------------------------
##- 윈도우 실행
## --------------------------------------------------------------------
window.mainloop()
