## --------------------------------------------------------
## break : for/while 반복을 중단시키는 키워드/명령어
##         - 즉시 반복을 중단함
##         - break 아래의 코드는 절대 실행 안됨!
## --------------------------------------------------------
## [요청] data 리스트의 원소가 7의 배수면 반복 중단
data = [1, 3, 5, 7, 9, 11, 13]

for num in data:
    if not num % 7:
        break
    print(num)


idx = 0
size = len(data)
while idx < size:
    if not num % 7:
        break
    print(data[idx])
    idx += 1
