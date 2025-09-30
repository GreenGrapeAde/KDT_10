## ----------------------------------------------------------------
## 내장함수 filter() : 사용법 map()과 동일
## - 형식 : filter(함수이름, iterable)
## - 기능 : 함수 결과가 True인 원소만 반환
## ----------------------------------------------------------------
## 데이터 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수만 추출해서 저장
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## [방법1] for ~ in 반복문 + 조건문
data2 = []
for d in data:
    if not d % 2:
        data2.append(d)

for d in data:
    if d % 2: continue
    data2.append(d)

for d in data[2::2]:
    data2.append(d)

## [방법2] List Comprehension
data1 = [d for d in data if d % 2 == 0]
print('data1=>', data1)

## [방법3] 내장함수 filter(함수이름, iterable)
def isvalid(d):
    return not d % 2

print('data3=>', list(filter(isvalid, data)))

print('data4=>', list(filter(lambda d: not d % 2, data)))