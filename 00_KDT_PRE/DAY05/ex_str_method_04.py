## --------------------------------------------------------
## str 전용 메서드: 문자열 나누거나 연결하거나 하는 메서드
## --------------------------------------------------------
## split() : 1개 문자열 => 여러 개 문자열을 공백 기준으로 분리
##                        리스트 타입에 담아서 돌려줌
## --------------------------------------------------------
msg = "Happy New Year 2025"

# 공백으로 분리
result = msg.split()
print( type(result), result )

# 공백으로 분리, 분리 개수 지정
result = msg.split(maxsplit = 2)
print( type(result), result )

# 'e' 분리
result = msg.split('e')
print( type(result), result )

# 'A' 분리
result = msg.split('A')  # 없는 문자열을 입력하면 split이 되지 않은 상태로 list에 담아서 반환
print( type(result), result )

## --------------------------------------------------------
## join() : 여러 개 문자열 => 1개 문자열로 연결하는 메서드
##          연결한 str.join([여러개 문자열])
## --------------------------------------------------------
data = "2025/09/05"

# => 년, 월, 일 분리
ymd = data.split('/')
print(f'ymd => {ymd}')

# => 년-월-일
print('-'.join(ymd))

# => 년★월★일
print(''.join(ymd))