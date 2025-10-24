## ----------------------------------------------------------------
##              PYTHON EXAM WORK
##       제출 파일명 : work_0319_이름.py
## ----------------------------------------------------------------
## 문제1) 비어 있는 리스트에 10, 40, “홍길동”, False, 40, False를 저장하는
#        코드를 작성하세요
list1 = list([])

list1.append(10)
list1.append(40)
list1.append("홍길동")
list1.append(False)
list1.append(40)
list1.append(False)

print(list1)
## 문제2) nums=[1,6,3,9,10]과 datas=[‘a’, ‘b’, ‘f’, ‘z’] 데이터의 
#        덧셈 결과를 출력하세요.
nums2=[1,6,3,9,10]
datas2=['a', 'b', 'f', 'z']
print(f'nums2 + datas2 = {nums2 + datas2}')

## 문제3) 아래 데이터에서 밑줄 _____부분에 코드를 작성하세요.
# nums=[ ]
# nums._____( 10 )   # 데이터 10 추가
# nums._____( 3 )    # 데이터 3 추가
# nums._____( 91 )   # 데이터 91 추가 
# print( nums )            # => 결과 :                           
# nums.remove( 3 )         # => 결과 :                           
# nums.remove( 100 )       # => 결과 :                           
# nums.______(1, 24 )      # => 결과 :   

nums=[ ]
nums.append( 10 )   # 데이터 10 추가
nums.append( 3 )    # 데이터 3 추가
nums.append( 91 )   # 데이터 91 추가 
print( nums )            # => 결과 :  [10, 3, 91]                   
#nums.remove( 3 )         # => 결과 : ValueError             
#nums.remove( 100 )       # => 결과 : ValueError                
nums.insert(1, 24 )      # => 결과 :  [10, 24, 3, 91]
print( nums )

## 문제4) 아래 데이터에서 요청을 처리하는 코드를 작성하세요.
# nums=[1,2,3,1,2,3,5,6,7,3]
# - nums 변수의 데이터 개수 출력 코드 
# - 요소 값 3의 개수 출력 코드
# - 요소 값 6의 인덱스 출력 코드
# - 마지막 요소를 삭제하는 코드
# - 3번째 요소를 삭제하는 코드
nums = [1, 2, 3, 1, 2, 3, 5, 6, 7, 3]

print("데이터 개수:", len(nums))
print("3의 개수:", nums.count(3))
print("6의 인덱스:", nums.index(6))

nums.pop()
print("마지막 삭제 후:", nums)

nums.pop(2)
print("3번째 요소 삭제 후:", nums)


## 문제5) 아래 데이터에서 해당 결과가 나오도록 코드를 작성하세요.
data=['a','c', True, 1, 9, 23, 'Happy', 21]
data.pop()                
print( data )     #=> 출력결과 :  ['a','c', True, 1, 9, 23, 'Happy']

data[1] = 'b'
data.remove(23)          
print( data )     #=> 출력결과 :  ['a', 'b', True, 1, 9, 'Happy']

data.insert(1, 2022)            
print( data )     #=> 출력결과 :  ['a', 2022, 'b', True, 1, 9, 'Happy']



## 문제6) datas=[9, 30, 1, 21, 5, 8, 0] 데이터를 정렬하는 코드 작성하세요.
##       오름차순 정렬과 내림차순 정렬 결과를 출력하세요.
datas=[9, 30, 1, 21, 5, 8, 0]

datas.sort()
print(f'오름차순 정렬: {datas}')

datas.sort(reverse=True)
print(f'내림차순 정렬: {datas}')


## 문제7) 10, 30, 89, 10, 23, 1, 2, 7, 11 데이터를 변경이 불가능한 
#         형태로 하나의 변수명에 저장해 출력해 주세요. 
nums = (10, 30, 89, 10, 23, 1, 2, 7, 11)
print(nums)


## 문제8) 주민번호를 입력 받아서 아래 내용대로 출력해주세요.
## 0000년 0월 0일 생  00세
## (예시: 2000년 8월 2일 생 24세 )   
#jumin=input("주민번호 입력(예:)")

jumin=input("주민번호 입력(예: 19971024 27)").split()
num = jumin[0]
age = jumin[1]

yy = num[:4]
mm = num[4:6]
dd = num[6:]
print(f'{yy}년 {mm}월 {dd}일 생 {age}세')

## 문제9)  nums = [13, 21, 12, 14, 30, 18] 데이터에 코드 작성하세요.
##     (1)  nums의 모든 요소를 for반복문으로 출력
##     (2)  nums에서 짝수값만 for반복문으로 출력
##     (3)  nums에서 모든 요소 값의 합계와 평균 출력
##     (4)  nums를 내림차순 정렬하여 모든 요소 출력
nums = [13, 21, 12, 14, 30, 18]
for n in nums:
    print(n)

for i in range(0, len(nums), 2):
    print(nums[i])

print(f'sum of nums is : {sum(nums)} and mean is : {sum(nums) / len(nums)}')

nums.sort(reverse=True)
print(f'Decreasing number of num is : {nums}')

## 문제10) 1부터 N번 숫자까지 모두 곱하는 팩토리얼(Factorial)을 구현하세요.
#    [ 입력 ] 팩토리얼 숫자 :  5
#    [ 출력 ] 5! 결과 :  5 * 4 * 3 * 2 * 1  = 120

n = int(input("Enter integer for factorial : "))
result = 1
while n >= 1:
    result *= n
    n -= 1

print(result)

## 문제11) 사용자에게 단어를 입력 받고 코드값을 16진수로 출력하세요.
#     [ 입력 ] 메시지 입력 : Hello
#     [ 호출 ] 16진수 코드값 변환 함수
#     [ 출력 ] Hello의 코드값 : 0x480x650x6c0x6c0x6f

word = input("Enter your word : ")
result = ''
for i in word:
    result += hex(ord(i))

print(result)


## 문제12) 아래와 같이 출력이 되도록 구구단을 2단부터 9단까지 출력하세요.
# 2 * 1 =  2      3 * 1 =  3      ---   8 * 1 =  8      9 * 1 =  9
# 2 * 2 =  4      3 * 2 =  6      ---   8 * 2 = 16      9 * 2 = 18
# 2 * 3 =  6      3 * 3 =  9      ---   8 * 3 = 24      9 * 3 = 27
# 2 * 4 =  8      3 * 4 = 12      ---   8 * 4 = 32      9 * 4 = 36
# 2 * 5 = 10      3 * 5 = 15      ---   8 * 5 = 40      9 * 5 = 45
# 2 * 6 = 12      3 * 6 = 18      ---   8 * 6 = 48      9 * 6 = 54
# 2 * 7 = 14      3 * 7 = 21      ---   8 * 7 = 56      9 * 7 = 63
# 2 * 8 = 16      3 * 8 = 24      ---   8 * 8 = 64      9 * 8 = 72
# 2 * 9 = 18      3 * 9 = 27      ---   8 * 9 = 72      9 * 9 = 81

for i in range(1, 10):
    for j in range(2, 10):
        if j != 9:
            print(f'{j} * {i} = {j * i:>2}', end="      ")
        else:
            print(f'{j} * {i} = {j * i:>2}')
