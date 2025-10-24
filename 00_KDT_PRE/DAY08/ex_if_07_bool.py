
## --------------------------------------------------------
## 조건문과 bool 객체
## --------------------------------------------------------
## if 조건식 : <= 조건식의 결과가 True or False 체크
##               조건식의 결과가 True/False 아니면
##               해당 값을 bool 형변환 시켜서 해석
## --------------------------------------------------------
## int/float 타입과 bool        => 0만 False, 나머지 True
print(f'int타입의 경우 False인 숫자 : 0 {bool(0)}')
print(f'int타입의 경우 True인 숫자 : 나머지 {bool(-3)}')
print(f'float타입의 경우 False인 숫자 : 0 {bool(0.0)}')
print(f'float타입의 경우 True인 숫자 : 나머지 {bool(0.000009)}')

## str/list/tuple 타입과 bool => 원소가 0개면 False, 나머지 True
print(f'str/list/tuple 타입의 경우 False인 경우 : 원소 0개, {bool("")}')
print(f'str/list/tuple 타입의 경우 True인 경우 : 나머지 (공백 포함), {bool(" ")}')

print(f'[[]] => {len([[]])}개, {bool([[]])}')  # 원소 1개 있음 => True 