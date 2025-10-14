from tkinter import *

# ------------------------------------------
# 윈도우 창 생성
# ------------------------------------------
mainWin = Tk()
mainWin.title("미니 계산기")
mainWin.geometry("250x150")

# ------------------------------------------
# 입력 필드 & 결과 레이블
# ------------------------------------------
Label(mainWin, text="첫 번째 숫자").pack()
entry1 = Entry(mainWin)
entry1.pack()

Label(mainWin, text="두 번째 숫자").pack()
entry2 = Entry(mainWin)
entry2.pack()

result_label = Label(mainWin, text="결과: ")
result_label.pack(pady=5)

# ------------------------------------------
# 버튼 클릭 시 실행될 함수
# ------------------------------------------
def calc_sum():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        result = n1 + n2
        result_label.config(text=f"결과: {result}")
    except ValueError:
        result_label.config(text="숫자를 입력하세요!")

# ------------------------------------------
# 버튼
# ------------------------------------------
Button(mainWin, text="더하기", command=calc_sum).pack()

# ------------------------------------------
# 윈도우 실행
# ------------------------------------------
mainWin.mainloop()
