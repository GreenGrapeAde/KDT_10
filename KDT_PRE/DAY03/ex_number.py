# ------------------------------------------------
# 숫자 표기법 : 2진수, 8진수, 16진수 변환
# ------------------------------------------------
# 진수 변환 내장함수 => bin(), oct(), hex(), int()
# ------------------------------------------------
noDec = 2025
noBin = '0b111'  # 0b는 문자열로 사용해야 함 -> ', " 사용
noOct = '0o7'
noHex = '0x15'

## 10진수 => 다른 진수로 변환
print(f'{noDec} 2진수 변환 : {bin(noDec)}')
print(f'{noDec} 8진수 변환 : {oct(noDec)}')
print(f'{noDec} 16진수 변환 : {hex(noDec)}')

## 2진수/8진수/16진수 => 10진수로 변환
print( f'{noBin} 10진수 변환 : {int(noBin, base=0)}' ) # 0을 주면 문자열의 접두어를 보고 진법을 자동 인식
print( f'{noBin} 10진수 변환 : {int(noBin, base=2)}' )
print( f'{noOct} 10진수 변환 : {int(noOct, base=8)}' )
print( f'{noHex} 10진수 변환 : {int(noHex, base=16)}' )