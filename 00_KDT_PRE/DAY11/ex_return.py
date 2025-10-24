## ----------------------------------------------------------------
## return 키워드
## - for/while 반복문 중단 기능
## - 함수 종료 기능
## - 즉시 종료!!!
## ----------------------------------------------------------------
## 반복문과 return
## ----------------------------------------------------------------
for ch in "Good Luck 2025!!":
    if ch.isspace(): break
    print("ch => ", ch)

print("END")
## ----------------------------------------------------------------
## 함수와 return
## ----------------------------------------------------------------
def add(a, b):
    if b < 0:
        return              ## 조건 만족 시 여기서 즉시 중단 되어버림
    elif a < 0:
        return
    total = a + b
    return total

print("1", add(3, 2))
print("2", add(3, -2))
print("3", add(-3, 2))

## ----------------------------------------------------------------
## 함수와 반복문과 return
## ----------------------------------------------------------------
## 기능: 전달 받은 문자열을 한개씩 한 행에 출력
def print_row1(msg):
    for ch in msg:
        if ch.isspace():
            break            ## 가장 가까운 반복문을 탈출
        print(ch)
    print('---^^---')
    return                   ## None 반환

def print_row2(msg):
    for ch in msg:
        if ch.isspace():
            return           ## 가장 가까운 반복문을 탈출
        print(ch)
    print('---^^---')        ## 이 줄 출력하지 않고 종료
    return                   ## None 반환

## => 호출하기
print("print_row1", print_row1("Good Luck"))
print("print_row2", print_row2("Good Luck"))