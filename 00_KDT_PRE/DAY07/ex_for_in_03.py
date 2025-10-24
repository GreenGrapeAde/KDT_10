## --------------------------------------------------------
## for ~ in 반복문 : 중첩 반복문
## --------------------------------------------------------
## [1] 정수를 10개 입력 받아 최대값, 최소값, 평균 출력하기
'''
numList = []
for i in range (1, 11):
    num = int(input(f"Enter your {i}th integers: "))
    numList.append(num)

print(f'최대값: {max(numList)}, 최소값: {min(numList)}, 평균 {sum(numList) / len(numList)}')
'''
## [2] Happy 단어의 코드값을 출력하기
## 예) AB 6566  2진수로
msg = "Happy"
dec_code = ''
bin_code = ''

for ch in msg:
    code = ord(ch)
    dec_code += str(code)

    b_code = bin(code)
    bin_code += b_code[2:]

print(f'{msg}  {dec_code}  {bin_code}')
