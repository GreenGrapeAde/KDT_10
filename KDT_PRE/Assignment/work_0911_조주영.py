# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##        제출 : work_0911_이름.py
# ## ----------------------------------------------------------------

# ## ----------------------------------------------------------------
# 1. 아래 리스트 원소들을 정수형으로 변환 후 저장하세요.
##   List Comprehension 문법으로 작성하세요.
#    data = ['9', '3', '7', '-1']

print("#1")

data = ['9', '3', '7', '-1']
data1 = [int(d) for d in data]
print(data1)


# ## ----------------------------------------------------------------
# 2. 아래 예시처럼 입력 데이터를 체크해 주세요.
#    5번 반복 질문해 주세요.
# 출력예시 #1
# [입력] 메시지 입력: 하늘 바다
# [출력] 글자입니다.
# 
# 출력예시 #2
# [입력] 메시지 입력:
# [출력] 공백입니다.
# 
# 출력예시 #3
# [입력] 메시지 입력: Good 2025 Happy
# [출력] 글자와 숫자 입니다.
# 
# 출력예시 #4
# [입력] 메시지 입력: GOOD
# [출력] 대문자 입니다.
# 
# 출력예시 #5
# [입력] 메시지 입력: abc good
# [출력] 소문자 입니다.
# 
# 출력예시 #6
# [입력] 메시지 입력: '3²' '½'
# [출력] 숫자 입니다.
print("#2")

for _ in range(5):
    msg = input("메시지 입력: ").split()

    if msg == []:
        print("공백입니다.")

    elif all(word.isupper() and word.isalpha() for word in msg):
        print("대문자입니다.")

    elif all(word.islower() and word.isalpha() for word in msg):
        print("소문자입니다.")

    elif all(word.isnumeric() for word in msg):
        print("숫자입니다.")

    elif any(word.isalpha() for word in msg) and any(word.isnumeric() for word in msg):
        print("글자와 숫자입니다.")

    else:
        print("글자입니다.")




# ## ----------------------------------------------------------------
# 3. 알파벳/한글 입력 받은 후 해당 문자의 코드값을 출력하세요.
#    알파벳/한글 외의 문자는 ‘정확한 데이터가 아닙니다’를 출력하세요.
# 
# 출력예시 #1
# [입력] 알파벳/한글 입력: 오늘
# [출력] 50724 45720 
# 
# 출력예시 #2
# [입력] 알파벳/한글 입력: today
# [출력] 116 111 100 97 121 
# 
# 출력예시 #3
# [입력] 알파벳/한글 입력: today12
# [출력] 정확한 데이터가 아닙니다
print("#3")

msg = input("알파벳/한글 입력: ")

if all(ch.isalpha() for ch in msg):
    codes = [str(ord(ch)) for ch in msg]
    print(" ".join(codes))
else:
    print("정확한 데이터가 아닙니다.")





# ## ----------------------------------------------------------------
# 4. 1 ~ 100 범위에 숫자를 누적 합계를 계산해 주세요.
##   단, 합계가 33이상이면 계산 중단함.
print("#4")

##  for문 방식"
sum4_1 = 0
for i in range(1, 101):
    if sum4_1 < 33:
        sum4_1 += i
    else: break

print(f'for문을 사용한 합계: {sum4_1}')


##  while문 방식
sum4_2 = 0
num = 1
while True:
    if sum4_2 < 33:
        sum4_2 += num
    else: break

    num += 1

print(f'while문을 사용한 합계: {sum4_2}')


# ## ----------------------------------------------------------------
# 5. List Comprehension 문법으로 코드 작성하세요.
#    values=['9', '0', '3', '5', '2']
#
# 출력예시 #1
# [입력] 변환 타입 : 정수형
# [출력] [9, 0, 3, 5, 2]   
#
# 출력예시 #2
# [입력] 변환 타입 : 논리형
# [출력] [True, True, True, True, True]
#
# 출력예시 #3
# [입력] 변환 타입 : 실수형
# [출력] [9.0, 0.0, 3.0, 5.0, 2.0]
print("#5")

values = ['9', '0', '3', '5', '2']
dtype = input("변환 타입 : ")

if dtype == "정수형":
    result = [int(v) for v in values]
elif dtype == "실수형":
    result = [float(v) for v in values]
elif dtype == "논리형":
    result = [bool(int(v)) for v in values]
else:
    result = values

print(result)

# ## ----------------------------------------------------------------
# 6. 1 ~ 100 범위에 숫자를 누적 합계를 계산해 주세요.
##   단, 합계가 33이상이면 계산 중단함.
print("#6")

sum6 = 0
for i in range(1, 101):
    if sum6 < 33:
        sum6 += i
    else: break

print(f'for문을 사용한 합계: {sum6}')

# ## ----------------------------------------------------------------
# 7. “!@Happy a Good Day~^^” 문자열을 시작과 끝을 검사해 주세요.
#      - 시작 :“!@”			- 끝 : “^^”
print("#7")

msg = "!@Happy a Good Day~^^"

if msg.startswith("!@"):
    print("시작: '!@'")
if msg.endswith("^^"):
    print("끝: '^^'")
## ----------------------------------------------------------------
## 8. 알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요.
## -  문자열 포맷과 이스케이프문자를 사용해서 출력하세요.
## - [입력] 구구단 : 5
## - [출력] 5 * 1 = 05	 5 * 2 = 10	    5 * 3 = 15	
##         5 * 4 = 20   5 * 5 = 25     5 * 6 = 20
##         5 * 7 = 35	5 * 8 = 40     5 * 9 = 45   
print("#8")

dan = int(input("구구단 : "))

for i in range(1, 10):
    print(f"{dan} * {i} = {dan * i:02}", end="\t")
    
    if i % 3 == 0:
        print()


# ## ----------------------------------------------------------------
# 9. 계절명을 입력받고 해당하는 달을 출력해주세요.
## - [입력] 좋아하는 계절 : 여름
## - [출력] 여름은 6월~8월 입니다.
print("#9")

season = input("좋아하는 계절 : ")

if season == "봄":
    print("봄은 3월~5월 입니다.")
elif season == "여름":
    print("여름은 6월~8월 입니다.")
elif season == "가을":
    print("가을은 9월~11월 입니다.")
elif season == "겨울":
    print("겨울은 12월~2월 입니다.")
else:
    print("정확한 계절명을 입력해주세요. (봄/여름/가을/겨울)")

# ## ----------------------------------------------------------------
## 10. 5과목 점수를 입력 받아서 저장해 주세요.
## - 아래 조건에 맞도록 메시지 출력하세요.
## - 입력 데이터 여부 체크           => 입력된 데이터가 없습니다. 
## - 입력 데이터가 숫자가 맞는지 체크  => 정확한 데이터가 아닙니다. 
## - 5과목 점수에서 최고 점수, 최저 점수, 총합, 평균 출력
print("#10")

scores = input("5과목 점수를 입력하세요 (공백으로 구분): ").split()

if not scores or all(s.strip() == "" for s in scores):
    print("입력된 데이터가 없습니다.")
else:
    is_valid = True
    for s in scores:
        if not s.isdigit():
            is_valid = False
            break

    if not is_valid:
        print("정확한 데이터가 아닙니다.")
    else:
        total = []
        for s in scores:
            total.append(int(s))

        print(f"최고 점수: {max(total)}")
        print(f"최저 점수: {min(total)}")
        print(f"총합: {sum(total)}")
        print(f"평균: {sum(total) / len(total)}")

# ## ----------------------------------------------------------------
# 11. 월을 숫자로 입력 받고 영어로 월을 출력해 주세요.
## - [입력] 좋아하는 월 : 3
## - [출력] 3월은 March
print("#11")

months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

month = input("좋아하는 월 : ")

if not month.isdigit():
    print("정확한 숫자를 입력해주세요.")
else:
    month = int(month)
    if 1 <= month <= 12:
        print(f"{month}월은 {months[month]}")
    else:
        print("1~12 사이의 숫자를 입력해주세요.")

# ## ----------------------------------------------------------------
# 12. 로그인 기능을 구현합니다. 
#     아이디(10자리 숫자, 영어, 기호)와 패스워드(8자리 숫자, 영어) 입력 받습니다.
#     [예] 임의의 아이디 : kkk12!,  비밀번호: 123aa
#     미리 지정한 아이디와 비밀번호가 맞다면 "kkk12!님! 반갑습니다."
#                                틀리면 "아이디 또는 비밀번호 확인하세요."
print("#12")

saved_id = "kkk12!"
saved_pw = "123aa"

user_id = input("아이디 입력: ")
user_pw = input("비밀번호 입력: ")

if user_id == saved_id and user_pw == saved_pw:
    print(f"{user_id}님! 반갑습니다.")
else:
    print("아이디 또는 비밀번호 확인하세요.")

# ## ----------------------------------------------------------------
# 13. 조건에 맞게 구현하세요.
# [13-1] 아래와 같은 크기로 출력
#       *
#       ***
#       *****
#       ***
#       *
print("#13-1")

for i in range(1, 6, 2):
    print("*" * i)

for i in range(3, 0, -2):
    print("*" * i)

# [13-2] 입력 받은 크기로 출력
#        크기 입력: 3
#        *
#        ***
#        *
print("#13-2")

val = int(input("홀수 크기 입력: "))

for i in range(1, val + 1, 2):
    print("*" * i)

for i in range(val-2, 0, -2):
    print("*" * i)
