## --------------------------------------------------------
## break / continue / pass
## --------------------------------------------------------
## [1] "Happy!Good" 데이터에서 원소를 옆으로 출력하세요
##     단 문자가 아니면 중단해 주세요.
msg = "Happy!Good"
for ch in msg:
    if not ch.isalpha():
        break
    print(ch, end = "")

print()
## [2] "Happy!Good" 데이터에서 원소를 옆으로 출력하세요
##     단 문자만 출력하세요.
msg = "Happy!Good"
idx = -1            ## 원소 읽기 위한 인덱스
stop = len(msg)     ## 인덱스 범위 지정을 위한 변수, 10

while idx < (stop - 1):  ## 8까지만 통과 허용 8 < 9
    idx += 1    
    if not msg[idx].isalpha():
        continue
    print(msg[idx], end = ' ')

# for ch in msg:
#     if not ch.isalpha():
#         continue
#     print(ch, end = " ")

# for ch in msg:
#     if not ch.isalpha():
#         pass
#     print(ch, end = " ")