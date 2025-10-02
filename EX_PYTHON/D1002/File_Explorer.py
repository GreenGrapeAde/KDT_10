## ----------------------------------------------
## [실습]
## ----------------------------------------------
## 프로그램 : File_Explorer
## 주요기능 : Windows의 탐색기 기능
##   - 특정 폴더 아래  : 파일, 폴더 목록 출력
##   - 특정 폴더 선택  : 파일, 폴더 목록 출력
#          파일 선택  : 크기, 생성일자 (datetime)
##   - 상위 폴더 이동 : 상위 폴더의 목록 출력
## 시작 디렉토리: C drive 또는 현재 작업 디렉토리
## 실행 화면: 바탕화면의 목록들
## ----------------------------------------------
import os
import datetime

## 출력할 지정
working_dir = os.path.abspath("C:/Users/choju/Desktop")
files = []
#print(working_dir)

def printMenu():
    print("-" * 26)
    print("탐색기 메뉴")
    print("1. 현재 폴더 아래 보기")
    print("2. 하위 파일 / 폴더 선택")
    print("3. 상위 폴더 이동")
    print("4. 기본 디렉토리로 이동(바탕화면)")
    print("X. 종료")
    print("-" * 26)


def print_all():
    global working_dir
    ## 하위의 파일, 폴더목록 출력
    print(f'선택된 디렉토리: {working_dir}')

    global files
    files = os.listdir(working_dir)
    print(f'파일 목록: {files}')

def print_certain():
    global working_dir, files
    if not files:
        print("먼저 현재 폴더를 출력하세요(메뉴 1번).")
        return

    print(f'파일 목록: {files}')
    msg = input("작업할 파일 또는 폴더를 선택하세요: ")
    target_dir = os.path.join(working_dir, msg)

    if not os.path.exists(target_dir):
        print("올바른 이름이 아닙니다.")
        return
    
    if os.path.isdir(target_dir):
        files = os.listdir(target_dir)
        print(f'파일 목록: {files}')
    
    elif os.path.isfile(target_dir):
        size = os.path.getsize(target_dir)
        created = datetime.datetime.fromtimestamp(os.path.getctime(target_dir)) ## ★★★★★★★★★

        print("파일 정보")
        print(f"- 이름: {msg}")
        print(f"- 크기: {size} bytes")
        print(f"- 생성일자: {created}")

def change_dir():
    global working_dir
    parent_dir = os.path.dirname(working_dir)

    if parent_dir == working_dir:
        print("상위 폴더입니다. 더이상 올라갈 수 없습니다.")
    else:
        working_dir = parent_dir
        print(f"[상위 폴더로 이동] => {working_dir}")

def default_dir():
    global working_dir
    working_dir = os.path.abspath("C:/Users/choju/Desktop")
    print(f"[기본 폴더로 이동] => {working_dir}")


print(f'{"=" * 10} 탐색기 프로그램 시작 {"=" * 10}')

while True:
    print(f'\n=> 현재 선택된 디렉토리: {working_dir}')
    printMenu()
    cmd = input("선택: ").strip().lower()

    if cmd == "1":
        print_all()
    elif cmd == "2":
        print_certain()
    elif cmd == "3":
        change_dir()
    elif cmd == "4":
        default_dir()
    elif cmd in ["x", "X"]:
        print("프로그램 종료")
        break