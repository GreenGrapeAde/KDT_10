## ----------------------------------------------------------------
##                      PYTHON EXAM-02
##                  제출 파일명 : work_0905_이름.py
## ----------------------------------------------------------------

## [1] 문자열을 입력 받은 후 문자열 구성요소 검사 결과를 출력하세요.
##     예) 문자만 있는지, 숫자만 있는지
print('[1]')
str1 = input("Enter string: ")
print(f'only alphabet: {str1.isalpha()}')
print(f'only digit: {str1.isdigit()}')
print('')

## [2] 'Merry Christmas'에 대해서 아래 조건에 맞는 코드 작성하세요.
##      - 대문자는 소문자로 소문자는 대문자로 변환 저장 및 추력
##      - 모두 대문자로 변환 후 저장 및 출력
##      - 모두 소문자로 변환 후 저장 및 출력
print('[2]')
str2 = 'Merry Christmas'
print(f'swapcase: {str2.swapcase()}')
print(f'upper: {str2.upper()}')
print(f'lower: {str2.lower()}')
print('')


## [3] [2]의 문자열을 구성하는 문자의 갯수와 인덱스 범위를 출력하세요
## - 예: Merry Christmas  문  자 개수 : OO개 
##       Merry Christmas  인덱스 범위 : O ~ O 
print('[3]')
print(f'Merry Christmas  문  자 개수 : {len(str2)}개')
print(f'Merry Christmas  인덱스 범위 : {0} ~ {len(str2) - 1}')
print('')


## [4] 문자열에서 조건에 맞는 문자열 출력
## - HappyAppleanimal : a의 인덱스 모두 출력
print('[4]')
str4 = "HappyAppleanimal"
start = 0
while True:
    idx = str4.find("a", start)
    if idx == -1:
        break
    print(idx)
    start = idx + 1
print('')


## [5] 사용자로부터 아래 정보를 1개 input()함수로 입력 받은 후
##     분리해서 출력 바랍니다.
##     - [예시] 이름, 고향, 나이, 성별 입력 : 
##     - [입력] "홍길동, 대구, 29, 남"
##     - [출력] ['홍길동', '대구', '29', '남']
print('[5]')
list5 = input("이름, 고향, 나이, 성별 입력 : ").split(",")
print(list5[:])
print('')

## [6] 알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요.
##     문자열 포맷과 이스케이프문자를 사용해서 출력하세요.
##     - [입력] 구구단 : 5
##     - [출력] 5 * 1 = 05	 5 * 2 = 10	    5 * 3 = 15	
##             5 * 4 = 20   5 * 5 = 25     5 * 6 = 20
##             5 * 7 = 35	5 * 8 = 40     5 * 9 = 45   
print('[6]')
num6 = int(input("구구단 : "))
for i in range(1, 10):
    if i % 3 != 0:
        print(f"{num6} * {i} = {num6 * i :0>2}", end="\t")
    else:
        print(f"{num6} * {i} = {num6 * i :0>2}")

print('')

## [7] 아래 조건을 만족하는 코드를 작성하세요.
print('[7]')

##     7-1. 주민등록번호 881120-1068234
##          연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력하세요.
str7_1 = "881120-1068234"
print(str7_1.split("-"))
##     7-2. 문자열 a:b:c:d
##          해당 문자열에서 a, b, c, d 만 출력해 주세요.
str7_2 = "a:b:c:d"
print(str7_2.split(":"))
##     7-3. “에이컨 월 48,584원에 무이자 36개월의 조건으로 판매" 
##          에서 총 금액을 출력해 주세요.
##          [출력] 에어컨 금액 : OOOOOOO원  
price7_3 = 48584
month7_3 = 36
print(f"에어컨 금액 : {price7_3 * month7_3}원")
##     7-4. “가로 10cm, 세로 11cm인 직사각형 넓이 계산” 
##          넓이 계산 후 출력하세요.
##          [출력] 직사각형 넓이 : 가로 10 x  세로 11 = 110
width7_4 = 10
lengh7_4 = 11
print(f"직사각형 넓이 : 가로 {width7_4} x 세로 {lengh7_4} = {width7_4 * lengh7_4}")

print('')

## [8] 아래 조건을 만족하는 코드를 작성해 주세요.
print('[8]')
##     8-1. 아래 데이터를 jumsu라는 변수명으로 저장해 주세요.  
##          점수 98 71 90  82  88
jumsu = list([98, 71, 90, 82, 88])

##     8-2. 정수 1개를 입력받은 후 그 숫자만큼 리스트 원소를 출력해 주세요.
##          - data = [10, 8, 3, "A"]
##          - [입력] 정수 입력: 2
##          - [출력] [10, 8, 3, "A", 10, 8, 3, "A"]
data = [10, 8, 3, "A"]
num8_2 = int(input("Enter num8_2: "))
print(data * num8_2)

##     8-3. [1,3,5,7,9,11]를 [1,15]가 되도록 코드를 구현해 주세요.
##          단, 2가지 방법으로 구현해주세요.
list8_3 = [1, 3, 5, 7, 9, 11]

#1)
del list8_3[1:]
list8_3_1 = list8_3 + list([15])
print(list8_3_1)


list8_3 = [1, 3, 5, 7, 9, 11]

#2)
list8_3 = [list8_3[0], 15]
print(list8_3)

##     8-4. [11, 22, ['Good', 'Luck'], 33, 44, 55] 데이터를 저장하세요.
##          'Luck' 데이터를 출력하세요.
##          'Luck' 데이터를 'lUCK'로 출력해주세요.
list8_4 = [11, 22, ['Good', 'Luck'], 33, 44, 55]
print(list8_4[2][1])
print(list8_4[2][1].upper())