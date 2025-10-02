## --------------------------------------------------------
## 개발자/사용자 정의 모듈 및 패키지 사용하기
##
## - 모  듈: 파이썬 파일(.py) 1개
## - 패키지: 모듈 여러개 묶은 것
## --------------------------------------------------------
## 모듈 로딩
## - D1002
##     |----- ex_custom.py *
##     |----- utils.py
##     |----- func
##             |----- my_func.py *
## -COMM
##   |----display.py
## --------------------------------------------------------
import utils                ## 같은 위치 즉, 폴더에 존재하는 모듈
import func.my_func as mf   ## 하위 폴더에 존재하는 모듈

import sys                  ## 상위 폴더에 존재하는 모듈
sys.path.append(r'C:\Users\choju\KDT_10\EX_PYTHON\COMM')
import display

## 모듈 사용 1
utils.print_msg("맛점하세요~^^")

## 모듈 사용 2
r1, r2, r3, r4 = mf.calc(3, 4)
print(f'+ => {r1}')
print(f'- => {r2}')
print(f'* => {r3}')
print(f'/ => {r4}')

display.show()