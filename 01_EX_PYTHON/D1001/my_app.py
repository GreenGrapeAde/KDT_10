## ----------------------------------------------------
## 계산기 프로그램
## - 사칙연산
## - 연산 결과 / 이력 저장
## - 터미널을 통한 메뉴 출력 & 사용자 선택
## - 사용자의 종료 입력 전까지 반복

## ----------------------------------------------------
## 전역변수 선언
## ----------------------------------------------------
FILE_NAME = './calc_history.txt'


## ----------------------------------------------------
## 사용자 정의 함수들
## ----------------------------------------------------
## 함수 기능: 메인메뉴 출력기능
## 함수 이름: printMenu
## 매개변수: 없음
## 결과반환: 없음
## ----------------------------------------------------
def printMenu():
    print(f'{"선택":-^17}')
    print(f'{"1. 입  력":<12}')
    print(f'{"2. 덧  셈":<12}')
    print(f'{"3. 뺄  셈":<12}')
    print(f'{"4. 곱  셈":<12}')
    print(f'{"5. 나눗셈":<12}')
    print(f'{"6. 기  록":<12}')
    print(f'{"7. 기록 변경":<12}')
    print(f'{"8. 기록 초기화":<12}')
    print(f'{"9. 마지막 결과값 사용":<12}')
    print(f'{"X. 종  료":<12}')
    print(f'{"":-^19}')

## ----------------------------------------------------
## 함수 기능: 연산에 사용될 데이터 2개 입력받기 기능
## 함수 이름: inputData
## 매개변수: 없음
## 결과반환: 입력 받은 2개 데이터
## ----------------------------------------------------
def inputData():
    return map(int, input("2개 정수 입력(예시: 30 2): ").split())

## ----------------------------------------------------
## 함수 기능: 사칙연산 결과 출력하는 함수
## 함수 이름: plus, minus, multiply, divide
## 매개변수: 없음
## 결과반환: 없음
## ----------------------------------------------------
def plus():
    # 전역변수 수정 선언
    global n1, n2, n3
    n3 = n1 + n2
    # 결과 화면 출력
    print(f'{n1} + {n2} = {n1 + n2}')
    # 결과 파일 저장
    saveHistory(f'{n1} + {n2} = {n1 + n2}') ## 파일이름, 저장
    # 전역변수 초기화
    n1, n2 = None, None

def minus():
    # 전역변수 수정 선언
    global n1, n2, n3
    n3 = n1 - n2
    # 결과 화면 출력
    print(f'{n1} - {n2} = {n1 - n2}')
    # 결과 파일 저장
    saveHistory(f'{n1} - {n2} = {n1 - n2}') ## 파일이름, 저장
    # 전역변수 초기화
    n1, n2 = None, None

def multiply():
    # 전역변수 수정 선언
    global n1, n2, n3
    n3 = n1 * n2
    # 결과 화면 출력
    print(f'{n1} * {n2} = {n1 * n2}')
    # 결과 파일 저장
    saveHistory(f'{n1} * {n2} = {n1 * n2}') ## 파일이름, 저장
    # 전역변수 초기화
    n1, n2 = None, None

def divide():
    # 전역변수 수정 선언
    global n1, n2, n3
    n3 = n1 / n2
    # 결과 화면 출력
    print(f'{n1} / {n2} = {n1 / n2}')
    # 결과 파일 저장
    saveHistory(f'{n1} / {n2} = {n1 / n2:.2f}') ## 파일이름, 저장
    # 전역변수 초기화
    n1, n2 = None, None

## ----------------------------------------------------
## 함수 기능: 연산 결과 저장 함수
## 함수 이름: saveHistory
## 매개변수: filename - 경로 포함한 파일명 [기본값] ./calc_history.txt
##          data     - 파일에 저장할 데이터
## 결과반환: 파일에 쓴 문자 개수 반환
## ----------------------------------------------------
def saveHistory(data, filename=FILE_NAME):
    with open(filename, mode='a', encoding='utf-8') as F:
        F.write(data + '\n')

## ----------------------------------------------------
## 함수 기능: 연산 결과 저장 함수
## 함수 이름: printHistory
## 매개변수: filename - 경로 포함한 파일명 [기본값] ./calc_history.txt
## 결과반환: 화면 출력으로 반환 없음
## ----------------------------------------------------
def printHistory(filename=FILE_NAME):
    with open(filename, mode='r', encoding='utf-8') as F:
        lines = F.readlines()
    
    ## 최근 연산 결과를 맨위에 출력하기 위함
    lines.reverse()
    for line in lines:
        print(line.strip('\n'))

## ----------------------------------------------------
## 함수 기능: 기록 변경 함수
## 함수 이름: changeHistory
## 매개변수: filename - 경로 포함한 파일명 [기본값] ./calc_history.txt
## 결과반환: 화면 출력으로 반환 없음
## ----------------------------------------------------
def changeHistory(filename=FILE_NAME):
    with open(filename, mode='r', encoding='utf-8') as F:
        lines = F.readlines()
    ## 최근 연산 결과를 맨위에 출력하기 위함
    lines.reverse()
    for line in lines:
        print(line.strip('\n'))
    
    num_line = int(input("변경하실 줄을 선택하세요: "))

## ----------------------------------------------------
## 함수 기능: 기록 초기화 함수
## 함수 이름: clearHistory
## 매개변수: filename - 경로 포함한 파일명 [기본값] ./calc_history.txt
## 결과반환: 화면 출력으로 반환 없음
## ----------------------------------------------------
def clearHistory(filename=FILE_NAME):
    with open(filename, mode='w', encoding='utf-8') as F:
        F.write("")

    print("기록이 모두 초기화 되었습니다.")
## ----------------------------------------------------
## 함수 기능: 마지막 결과값 사용 함수
## 함수 이름: lastValue
## 매개변수: filename - 경로 포함한 파일명 [기본값] ./calc_history.txt
## 결과반환: 화면 출력으로 반환 없음
## ----------------------------------------------------
def lastValue():
    global n2, n3
    n2 = int(input(f"이전값 {n3}을 첫번째 값으로 불러왔습니다. 두번째 값을 입력하세요: "))

## ----------------------------------------------------
## 프로그램 구동 부분
## ----------------------------------------------------
print("계산기 프로그램 시작")

n1, n2 = None, None

while True:
    # 메뉴 출력
    printMenu()
    cmd = input("선택: ")

    # 종료 체크 및 처리
    if cmd in ['x', 'X']: break
    elif cmd == '1':
        n1, n2 = inputData()
        print(n1, n2)
    elif cmd == '2':
        if (n1 != None) and (n2 != None): plus()
    elif cmd == '3':
        if (n1 != None) and (n2 != None): minus()
    elif cmd == '4':
        if (n1 != None) and (n2 != None): multiply()
    elif cmd == '5':
        if (n1 != None) and (n2 != None) and (n2 != 0): divide()
        else: print("올바른 두번째 값을 입력하세요!!")
    elif cmd == '6':
        printHistory()
    elif cmd == '7':
        changeHistory()
    elif cmd == '8':
        clearHistory()
    elif cmd == '9':
        lastValue()
    else:
        print("존재하지 않는 항목입니다.")

print("계산기 프로그램 종료")