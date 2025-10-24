# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##        제출 : 구글 드라이브에 work_0910_이름.py
# ## ----------------------------------------------------------------

# ## ----------------------------------------------------------------
# 1. words = ["I", "study", "python", "language", "!"] 데이터에 대한 
#    아래 코드 작성하세요.    
#    (1)  words의 모든 요소를 for반복문으로 출력
#    (2)  words에서 홀수번째 요소만 for반복문으로 출력
#    (3)  words에서 길이가 3이상인 요소만 for반복문으로 출력
#    (4)  words를 오름차순 정렬하여 모든 요소 출력
print('#1')

words = ["I", "study", "python", "language", "!"]

print("모든 요소:", end=" ")
for ch in words:
    print(ch, end=" ")
print()

print("홀수 요소:", end=" ")
for i in range(0, len(words), 2):
    print(words[i], end=" ")
print()

print("길이가 3이상인 요소:", end=" ")
for ch in words:
    if len(ch) > 3:
        print(ch, end=" ")
print()

print("오름차순 정렬된 요소:", end=" ")
words.sort()
for ch in words:
    print(ch, end=" ")
print()

# ## ----------------------------------------------------------------
# 2.  아래 데이터에 대한 구현 코드 작성하세요.
#     files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']
#     (1) 확장자 없이 파일명만 출력
#     (2) 확장자가 ‘h’이거나 ‘c’인 것만 출력
#     (3) 파일명에 ‘e’가 2개 이상 있고 ‘f’가 있는 파일명만 출력
print('#2')

files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']
result = ''

print("확장자 없이 파일명만 출력:", end = " ")
for data in files:
    result = data.split(".")
    print(result[0], end=" ")
print()

print("확장자가 h이거나 c인 것만 출력:", end = " ")
for data in files:
    result = data.split(".")
    if result[1] == 'h' or result[1] == 'c':
        print(f'{".".join(result)}', end=" ")
print()

print("파일명에 e가 2개 이상 있고 f가 있는 파일명만 출력:", end = " ")
for data in files:
    result = data.split(".")
    if result[0].count("e") >=2 and result[0].count("f"):
        print(result[0], end=" ")

print()
	

# ## ----------------------------------------------------------------
# 3. for 반복문을 사용하여 2단부터 9단까지 모두 출력하세요.
#    단 아래와 같이 출력하세요.

#     3               5     
# 3 * 1 = 03      5 * 1 = 05
# 3 * 2 = 06      5 * 2 = 10
# 3 * 3 = 09      5 * 3 = 15
# 3 * 4 = 12      5 * 4 = 20
# 3 * 5 = 15      5 * 5 = 25
# 3 * 6 = 18      5 * 6 = 30
# 3 * 7 = 21      5 * 7 = 35
# 3 * 8 = 24      5 * 8 = 40
# 3 * 9 = 27      5 * 9 = 45

#     7               9     
# 7 * 1 = 07      9 * 1 = 09
# 7 * 2 = 14      9 * 2 = 18
# 7 * 3 = 21      9 * 3 = 27
# 7 * 4 = 28      9 * 4 = 36
# 7 * 5 = 35      9 * 5 = 45
# 7 * 6 = 42      9 * 6 = 54
# 7 * 7 = 49      9 * 7 = 63
# 7 * 8 = 56      9 * 8 = 72
# 7 * 9 = 63      9 * 9 = 81

print("#3")

for i in range(3, 8, 4):
    print(f'{i:^10}      {i+2:^10}')
    for j in range(1, 10):
        if i==3 and j==9:
            print(f'{i} * {j} = {i * j:0>2}      {i+2} * {j} = {(i+2) * j:0>2}')
            print()
        else:
            print(f'{i} * {j} = {i * j:0>2}      {i+2} * {j} = {(i+2) * j:0>2}')

# ## ----------------------------------------------------------------
# 4. 2개의 정수와 덧셈, 뺄셈, 곱셈, 나눗셈 연산자 1개를 입력 받으세요.
#    연산 결과를 출력합니다. 단, 입력 함수는 1개 사용합니다.
print("#4")

expr = input("두 정수와 연산자를 입력하세요 (예: 10 + 3): ")

a, op, b = expr.split()
a, b = int(a), int(b)

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    # 0으로 나누기 방지
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("0으로 나눌 수 없습니다.")
else:
    print("지원하지 않는 연산자입니다.") 

# ## ----------------------------------------------------------------
# 5. “가나*마바사*자***파하”에서 첫 번째 *의 인덱스를 출력하세요.
#    세 번째 ‘*’의 인덱스를 출력하세요.
print("#5")

msg = "가나*마바사*자***파하"
print(f'첫 번째 *의 인덱스 {msg.find("*")}')

idx = 0
count = 0
while True:
    idx = msg.find("*", idx)
    count += 1
    if count == 3:
        break
    idx += 1
    
print(f'세 번째 *의 인덱스 {idx}')


# ## ----------------------------------------------------------------
# 6. 좋아하는 단어를 입력 받은 후 대문자로 변환하여 출력하세요.
#    그리고 각 알파벳이 단어안에 몇개 있는지 출력하세요.
#    [예시] Hello
#          H - 1개     e - 1개      l - 2개        o - 1개
print("#6")

word = input("좋아하는 단어를 입력하세요: ")
print(f'대문자 변환: {word.upper()}')

checked = []
for ch in word:
    if ch not in checked:
        print(f'{ch} - {word.count(ch)}개')
        checked.append(ch)

# ## ----------------------------------------------------------------
# 7. “1,234,567,890” 문자열에서 숫자들의 합계를 계산 후 출력하세요.
#    숫자들은 1자리 숫자입니다.
print("#7")

data = "1,234,567,890"
result = 0

for ch in data:
    if ch.isdecimal():
        result += int(ch)

print(f'{data} 전체 숫자에서 한자리씩 모두 더한 값: {result}')

# ## ----------------------------------------------------------------
# 8. “산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐” 문장을 
#     아래와 같이 출력하세요.
#     [출력] 끼토산 야끼토 를디어 냐느가 짝폴 짝폴 서면뛰 를디어 냐느가
print("#8")

msg = "산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐".split()

for i in range(len(msg)):
    msg[i] = msg[i][::-1]

print(" ".join(msg))

# ## ----------------------------------------------------------------
# 9. [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7] 에서 중복된 데이터 제외한 
#     데이터들 평균 출력하세요.
print("#9")

data1 = [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7]
data2 = []

for n in data1:
    if n not in data2:
        data2.append(n)

print(f'평균: {sum(data2) / len(data2)}')

# ## ----------------------------------------------------------------
# 10. [1,1,5,2,6,9,2]와 [5,9,1,3,4,2,8,7,1,2,5] 데이터 중복된 값을 제거한
#     하나의 리스트를 생성해 주세요.
print("#10")

data1 = [1, 1, 5, 2, 6, 9, 2]
data2 = [5, 9, 1, 3, 4, 2, 8, 7, 1, 2, 5]
result = []

for x in data1 + data2:
    if x not in result:
        result.append(x)

print(result)