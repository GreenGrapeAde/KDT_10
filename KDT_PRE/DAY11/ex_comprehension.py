## ----------------------------------------------------------------
## Comprehension => List/Dict/Set
## ----------------------------------------------------------------
## 형식 : for ~ in + if ~ else + List/Dict/Set => 합친 것!
## ----------------------------------------------------------------
## [List Comprehension]
## 문  제 : str 타입의 숫자를 int 타입의 숫자로 형변환 진행
## 데이터 : nums = ['9', '0', '4', '7', '2']
numstr = ['9', '0', '4', '7', '2']

numInt = []
## => 방식1 : 일반
for num in numstr:
    numInt.append(int(num))

## => 방식2 : LComprehension
numInt2 = [int(num) for num in numstr]

## [Dict Comprehension]
## 문  제 : 문자에 대한 코드값 저장된 chr2code => 코드값에 대한 문자값
## 데이터 : chr2code = {'A': 65, 'C': 67, 'b': 98}
## => 방법1 - 일반
chr2code = {'A': 65, 'C': 67, 'b': 98, '3': 3}
code2chr = {}
for k, v in chr2code.items():
    code2chr[v] = k

print(code2chr)

## => 방법2 - Dict Comprehension
code2chr2 = {v: k for k, v in chr2code.items()}

print(code2chr2)

## => 방법3 - Dict Comprehension : 필터링
##    대문자 문자만 코드값 저장
code2chr3 = {v: k for k, v in chr2code.items() if k.isupper()}

print(code2chr3)

## => 방법4 - Dict Comprehension : 원소마다 다른 저장법 적용
##    str 숫자는 k와 v 변경 없고 그대로 저장
##    문자는 코드값과 문자 변경해서 저장

# code2chr4 = {v: k if k.isalpha() else v for k, v in chr2code.items()}

# print(code2chr4)

## [Set Comprehension]
## 문  제 : "Good Luck" 데이터에서 중복된 문자는 1번만 저장하세요.
msg1 = list("Good Luck")
msg2 = set("Good Luck")          ## 자동으로 중복을 제거함
msg3 = {ch for ch in "Good Luck"}

print(f'msg1 => {msg1}\nmsg2 => {msg2}\nmsg3 => {msg3}')

## 중복 금지와 특정 데이터 필터링을 모두 하고 싶다면
msg4 = {ch for ch in "Good Luck" if ch.islower()}
print(f'msg4 => {msg4}')