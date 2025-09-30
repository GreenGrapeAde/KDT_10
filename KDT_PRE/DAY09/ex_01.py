## --------------------------------------------------------
## List Comprehension
## --------------------------------------------------------
data = ['apple', 'Happy', 'Good', 'luck', 'LOVE']

## [1] 새로운 리스트에 모든 원소값을 대문자로 저장하기
data1 = [ d.upper() for d in data ]
print(f'대문자 원소: {data1}')

## [2] 새로운 리스트에 소문자 -> 대문자, 대문자 -> 소문자로 저장
# data1 = [ d.swapcase() for d in data ]
# print(f'대소문자 변경: {data1}')

data1 = [d.lower() if d.isupper() else d.upper() for d in data] ## apple과 luck은 if문 / Happy, Good은 else문에 걸림
print(f'대소문자 변경: {data1}')

data = ['3', '-1', '9', '0']
## [3] 새로운 리스트에 int로 저장하기
data1 = [ int(d) for d in data ]
print(f'정수로 변경: {data1}')

data = "Good 2025 Happy Day 2026"
## [4] data안에 요소들 중 숫자만 다른 리스트에 저장하기
data1 = [ ch for ch in data if ch.isdecimal()]
print(f'숫자만 저장: {data1}')