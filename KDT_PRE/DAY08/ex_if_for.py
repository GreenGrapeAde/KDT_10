## --------------------------------------------------------
## if & for
## --------------------------------------------------------
## [문제] 아래 문자열에서 숫자는 숫자끼리, 문자는 문자끼리 나누기
data = "에어컨 가격은 300만원 24개월 할부"

# dec = []
# alp = []
# for ch in data:
#     if(ch.isdecimal()):
#         #print(f'숫자: {ch}')
#         dec.append(ch)
#     elif(ch.isalpha()):
#         alp.append(ch)
#         #print(f'문자: {ch}')

# print(dec, alp)

## 교수님 풀이
data1, data2 = "", ""

for ch in data:
    if(ch.isdecimal()):
        data1 += ch
    elif(ch.isalpha()):
        data2 += ch

print(f'숫자 : {data1}\t문자 : {data2}')