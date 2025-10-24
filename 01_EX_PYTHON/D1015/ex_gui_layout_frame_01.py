## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## 컨테이너 위젯: 여러 개의 Widget을 담을 수 있는 widget
## - 대표 위젯  : Frame, TopLevel
## - Frame 위젯: 포함된 Widget들의 부모가 됨!
##   * 사용: Frame 인스턴스 생성
##           UI Widget 인스턴스 생성 시 Frame 인스턴스를 master로 설정
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성
window = tkinter.Tk()
window.title("** Container Widget - Frame **")
window.geometry("900x400")

## --------------------------------------------------------------------
##- Widget 인스턴스 생성 및 설정
## --------------------------------------------------------------------
##- ID 라벨과 입력 필드
idLB = tkinter.Label(window, text="ID")
idENT = tkinter.Entry(window)
idLB.pack(anchor='w', padx=10)                      # anchor를 하지 않으면 기본 값이 center임
idENT.pack(anchor='w', fill='x', padx=10)           # label과 entry는 해당 클래스에 하나씩 수동으로 pad값 입력해야함

##- PW 라벨과 입력 필드
pwFR = tkinter.Frame(window, bg='lightyellow', bd=2, relief='solid')
pwLB = tkinter.Label(pwFR, text="PW")
pwENT = tkinter.Entry(pwFR)

# Frame 자식 Widget 배치
pwFR.pack(anchor='e', padx=10, pady=10)            # window 대신에 FR을 할당하고 부모로 사용함, pack의 기본값은 중간
# pwLB.pack(side='left')                           # pack or grid 모두 가능함
# pwENT.pack(side='left')                          # frame은 부모에게 pad 적용해도 됨
pwLB.grid(row=0, column=0)
pwENT.grid(row=1, column=2)
## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()