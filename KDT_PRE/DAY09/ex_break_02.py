## --------------------------------------------------------
## break : for/while 반복을 중단시키는 키워드/명령어
##         - 즉시 반복을 중단함
##         - break 아래의 코드는 절대 실행 안됨!
##         - 중첩 반복문의 경우 가장 가까운 반복문을 탈출
## --------------------------------------------------------
## [요청] 중첩 반복문과 break문
isstop = False   ## flag 변수
for ch in "ABCDEFGHIJKLMN":
    print(ch)
    for num in range(4, 20):
        if num == 11:
            isstop = True
            break  ## 즉시 중단. 바깥 for문은 중단 x
        print(num)

    if isstop: break