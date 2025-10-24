import datetime as dt

a = 10
b = 20
c = a + b
# print( f'{a} + {b} = {c}' )
print('%d + %d = %d' %(a, b, c))

# name = input('Enter your name: ')

#print(f'your name is {name}')

Msg="Good-Luck"
print(len(Msg))

total = 0
for i in range(1, 11):
    total += i

print(total)

for n in range(1, 101):
    if (n % 3 == 0) and (n % 5 == 0):
        print(n)

#msg = input("Enter your string: ")
#print(msg[::-1])

scores = [85, 90, 78, 92, 88]
# 전체평균, 최고점수, 최저점수
mean  = sum(scores) / len(scores)
print(mean, max(scores), min(scores))

print(dt.datetime.now())

data = {'A': 10, 'Z': 7, 'D': 20, 'B': 100}

asc = sorted(data.items(), key=lambda item: item[1])
desc = sorted(data.items(), key=lambda item: item[1], reverse=True)

print('asc => ', asc, '\ndesc => ', desc)

## map() + lambda + 조건부 표현식 -----------------------------------
## 3의 배수는 str타입 변환하고 나머지 숫자는 float 변환해서 저장
a = range(15)

print(f'map 사용: {list(map(lambda x: float(x) if x % 3 else str(x), a))}')
print(f'filter 사용: {list(filter(lambda x: float(x) if x % 3 else str(x), a))}')

# 6. 조건부 딕셔너리
#    정수 리스트 range(1, 11)이 있을 때,
#    짝수만 key로 사용하고, value는 제곱 값을 가지는 딕셔너리를 
#    dict comprehension으로 작성하세요.
int_list = range(1, 11)

result = {n: n**2 for n in int_list if not n % 2}

print(result)