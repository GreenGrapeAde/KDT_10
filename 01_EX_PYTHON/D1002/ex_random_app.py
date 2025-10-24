## --------------------------------------------------------
##                    내장 모듈 random 활용
## - random -> 난수 생성하거나 무작위 선택할 때 사용
## --------------------------------------------------------
## [실습1] 로또 프로그램을 구현하세요.
##         - 숫자 범위: 1 ~ 45
##         - 추출 숫자: 6개 중복 X
##         - 조    건: randint 사용
## --------------------------------------------------------
## [방법 1]
import random    # 모듈 로딩

cnt = 0
result = []
while cnt < 6:
    n = random.randint(1, 45)
    if n not in result:
        result.append(n)
        cnt += 1


print(result)

## [방법2]
from random import randint

lotto = set()
while True:
    if len(lotto) == 6: break
    lotto.add(randint(1, 45))
print(f'이번주 로또 번호: {lotto}')

## [방법3]
from random import sample

print(f'이번주 로또 번호: {sample(range(1, 46), 6)}')