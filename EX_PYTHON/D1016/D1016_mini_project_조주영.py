## =====================================================================
##              Tkinter GUI - App Subscription Manager
## =====================================================================
## 기능 요약
## - 상단 버튼: 홈 / 추가 / 삭제 / 변경
## - 왼쪽: 정기결제 리스트 (앱 이름만 표시)
## - 오른쪽: 선택한 앱의 상세 정보 (앱명, 결제일, 기간, 가격)
## - 데이터는 임시 리스트로 관리
## =====================================================================

"""Todo List
"""

from tkinter import *
from tkinter import messagebox     # 알림창을 띄우기 위해 추가로 import

from datetime import *             # 시간을 띄우기 위한 패키지
from calendar import monthrange    

import os                          # 파일 입출력을 위한 패키지
## ---------------------------------------------------------------------
## 전역 변수
## ---------------------------------------------------------------------
subscriptions = []   # [{'name': str, 'date': str, 'price': str}, ...]
DATA_FILE = "subscriptions.txt"

## ---------------------------------------------------------------------
## 파일 입출력 함수
## ---------------------------------------------------------------------
def load_data():
    """저장된 정기결제 데이터를 파일에서 읽어오기"""
    if not os.path.exists(DATA_FILE):
        return  # 파일이 없으면 그냥 종료
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            name, date, price = line.strip().split(",")
            subscriptions.append({'name': name, 'date': date, 'price': price})

def save_data():
    """현재 정기결제 데이터를 파일에 저장"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for sub in subscriptions:
            f.write(f"{sub['name']},{sub['date']},{sub['price']}\n")

## ---------------------------------------------------------------------
## UI 관련 함수 정의
## ---------------------------------------------------------------------
def update_listbox():
    """리스트박스에 앱 이름 목록을 갱신"""
    listbox.delete(0, END)                        # 다 지우고
    for sub in subscriptions:
        listbox.insert(END, sub['name'])          # 새로 추가

def show_info(event):
    """리스트를 선택하였을 때,
       선택된 앱의 상세 정보를 오른쪽 라벨에 표시"""
    if not listbox.curselection():                # 리스트 선택이 없을 경우 아래 코드를 실행하지 않음
        return
    idx = listbox.curselection()[0]               # 튜플의 [0]값이 리스트의 index가 됨 ex) 3번째 리스트: (2,)
    sub = subscriptions[idx]                      # 해당 인덱스의 리스트 원소인 dict 선택

    # 현재 년, 월 기준
    today = datetime.now()
    year, month = today.year, today.month

    # 입력된 결제일
    pay_day = int(sub['date'])

    # 이번달 결제 시작일
    last_day_of_month = monthrange(year, month)[1] # (해당 1일의 요일 값 int, 이번 달이 몇일까지 있는지)
    if pay_day > last_day_of_month:
        pay_day = last_day_of_month                # 존재하지 않는 날짜면 마지막 날로 조정
    start_date = datetime(year, month, pay_day)

    # 다음달 계산
    if month == 12:
        next_year, next_month = year + 1, 1        # 현재 12월일 경우
    else:
        next_year, next_month = year, month + 1

    # 다음달의 마지막 날짜 구하기
    next_last_day = monthrange(next_year, next_month)[1]
    next_pay_day = min(int(sub['date']), next_last_day) # 결제일이 31일인 경우 다음달은 마지막 날인 30일로 조정
    end_date = datetime(next_year, next_month, next_pay_day)

    info_text.set(
        f"앱 이름: {sub['name']}\n"
        f"이번달 결제(예정)일: {start_date.strftime('%Y/%m/%d')}\n"
        f"다음달 결제(예정)일: {end_date.strftime('%Y/%m/%d')}\n"
        f"가격: {sub['price']}원"
    )

def add_subscription():
    """새 정기결제 추가"""
    def confirm_add():
        name = entry_name.get().strip()
        date = entry_date.get().strip()
        price = entry_price.get().strip()
        if not (name and date and price):
            messagebox.showwarning("입력 오류", "모든 항목을 입력해주세요.")
            return
        subscriptions.append({'name': name, 'date': date, 'price': price})
        subscriptions.sort(key=lambda sub: int(sub['date'])) ## 날짜 순으로 정렬, sub 말고 x처럼 임의의 값 주면 됨
        update_listbox()
        update_total()
        save_data()
        add_win.destroy()          # 서브 윈도우 내림


    add_win = Toplevel(window)     # 서브 윈도우 띄움
    add_win.title("정기결제 추가")
    add_win.geometry("250x180")

    # 서브 윈도우의 라벨과 엔트리들
    Label(add_win, text="앱 이름").pack(pady=3)  
    entry_name = Entry(add_win)
    entry_name.pack()

    Label(add_win, text="이번달 결제(예정)일").pack(pady=3)
    entry_date = Entry(add_win)
    entry_date.pack()

    Label(add_win, text="가격").pack(pady=3)
    entry_price = Entry(add_win)
    entry_price.pack()

    Button(add_win, text="확인", command=confirm_add).pack(pady=10)  # 버튼 클릭시 confrim_add 수행

def delete_subscription():
    """정기결제 삭제"""
    def confirm_delete():
        name = entry_del.get().strip()
        for sub in subscriptions:
            if sub['name'] == name:
                subscriptions.remove(sub)
                update_listbox()
                update_total()
                save_data()
                info_text.set("삭제 완료")
                del_win.destroy()
                return                                      # 정상적이라면 여기서 종료
        messagebox.showerror("오류", "해당하는 앱이 없습니다.") # 아니면 오류 출력

    # 서브 윈도우의 라벨과 엔트리들
    del_win = Toplevel(window)
    del_win.title("정기결제 삭제")
    del_win.geometry("250x120")

    Label(del_win, text="삭제할 앱 이름").pack(pady=5)
    entry_del = Entry(del_win)
    entry_del.pack()

    Button(del_win, text="삭제", command=confirm_delete).pack(pady=10)

def edit_subscription():
    """정기결제 정보 변경"""
    def confirm_edit():
        name = entry_name.get().strip()
        for sub in subscriptions:
            if sub['name'] == name:
                sub['date'] = entry_date.get().strip()
                sub['price'] = entry_price.get().strip()
                subscriptions.sort(key=lambda sub: int(sub['date']))  ## 날짜와 가격이 바뀌었으므로 날짜 오름차순으로 정렬
                update_listbox()
                update_total()
                save_data() 
                info_text.set("정보가 수정되었습니다.")
                edit_win.destroy()
                return
        messagebox.showerror("오류", "해당하는 앱이 없습니다.")

    # 서브 윈도우
    edit_win = Toplevel(window)
    edit_win.title("정기결제 변경")
    edit_win.geometry("250x180")
    # 서브윈도우의 라벨과 엔트리들
    Label(edit_win, text="변경할 앱 이름").pack(pady=3)
    entry_name = Entry(edit_win)
    entry_name.pack()

    Label(edit_win, text="새 결제(예정)일").pack(pady=3)
    entry_date = Entry(edit_win)
    entry_date.pack()

    Label(edit_win, text="새 가격").pack(pady=3)
    entry_price = Entry(edit_win)
    entry_price.pack()

    Button(edit_win, text="확인", command=confirm_edit).pack(pady=10)

def go_home():
    """홈 버튼 클릭 시 초기 화면 상태로 복귀"""
    listbox.selection_clear(0, END)            # 리스트 선택 해제
    info_text.set("")                          # 오른쪽 정보 초기화

def update_total():
    total = sum(int(sub['price']) for sub in subscriptions if sub['price'].isdigit())
    total_label.config(text=f"이번달 총 결제 금액: {total}원")
## ---------------------------------------------------------------------
## 메인 윈도우 설정
## ---------------------------------------------------------------------
window = Tk()
window.title("앱 정기결제 관리 프로그램")
window.geometry("700x400+400+200")
window.resizable(True, True)

## ---------------------------------------------------------------------
## 상단 버튼 영역
## ---------------------------------------------------------------------
top_frame = Frame(window)
top_frame.pack(pady=10)

btn_home = Button(top_frame, text="홈", width=10, command=go_home)
btn_add = Button(top_frame, text="추가", width=10, command=add_subscription)
btn_delete = Button(top_frame, text="삭제", width=10, command=delete_subscription)
btn_edit = Button(top_frame, text="변경", width=10, command=edit_subscription)

btn_home.pack(side="left", padx=5)
btn_add.pack(side="left", padx=5)
btn_delete.pack(side="left", padx=5)
btn_edit.pack(side="left", padx=5)


## ---------------------------------------------------------------------
## 하단 영역 (리스트 + 정보)
## ---------------------------------------------------------------------
bottom_frame = Frame(window)
bottom_frame.pack(fill='both', expand=True, padx=20, pady=10)

# 왼쪽: 리스트박스
list_frame = Frame(bottom_frame)
list_frame.pack(side='left', fill='y')

# 왼쪽 상단은 라벨, 하단은 리스트박스
Label(list_frame, text="정기결제 목록").pack()
listbox = Listbox(list_frame, width=30, height=15)
listbox.pack(side='left', fill='y')
listbox.bind("<<ListboxSelect>>", show_info)

# 오른쪽: 정보 표시 라벨
info_frame = Frame(bottom_frame)
info_frame.pack(side='top', fill='both', expand=True, padx=20, pady=(20, 100))

Label(info_frame, text="결제 정보", font=('Arial', 14, 'bold')).pack(anchor='w')

info_text = StringVar()  # 함수에서의 info_text의 실시간 변경을 바인딩
infoLB = Label(info_frame, textvariable=info_text, justify='left', font=('Arial', 12)) # textvariable 옵션
infoLB.pack(anchor='w', pady=10)

total_frame = Frame(bottom_frame)
total_frame.pack(side='bottom', fill='both', expand=True, padx=20, pady=(100, 0))
total_label = Label(total_frame, text=f"이번달 총 결제 금액: 0원", font=('Arial', 12, 'bold'))
total_label.pack(anchor='w')

## ---------------------------------------------------------------------
## 실행 전: 파일에서 데이터 불러오기
## ---------------------------------------------------------------------
load_data()
update_listbox()
update_total()

## ---------------------------------------------------------------------
## 이벤트 루프
## ---------------------------------------------------------------------
window.mainloop()