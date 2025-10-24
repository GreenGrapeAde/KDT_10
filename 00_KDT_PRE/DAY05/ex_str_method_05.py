## --------------------------------------------------------
## str 전용 메서드: 문자열 검사해주는 메서드 => 결과 True/False
##                 is___()
## --------------------------------------------------------
## 대소문자 검사해주는 메서드 : isupper(), islower()
## --------------------------------------------------------
print(f'GOOD.isupper()    : {"GOOD".isupper()}')
print(f'GOOD.islower()    : {"GOOD".islower()}')
print(f'GOOD.isspace()    : {"GOOD".isspace()}')

## --------------------------------------------------------
## 문자 구성요소 종류 검사해주는 메서드 : isalpha(), isdigit(),,
## --------------------------------------------------------
print(f'GOOD.isalpha()    : {"GOOD".isalpha()}')
print(f'GOOD7.isalpha()   : {"GOOD7".isalpha()}')
print(f'123.8.isdigit()   : {"123.8".isdigit()}')  # "."은 digit이 아니므로 False
print(f'오늘.isalpha()    : {"오늘".isalpha()}')    # 한글도 true 


## 숫자/문자 검사 메서드 3개 범위 isdecimal() < isdigit() < isnumeric()
## -, + 기호, 실수는 X
print(f'123.isdigit()     : {"123".isdigit()}')
print(f'123.decimal()     : {"123".isdecimal()}')
print(f'123.isnumeric()   : {"123".isnumeric()}')

print(f'-123.isdigit()    : {"-123".isdigit()}')
print(f'-123.decimal()    : {"-123".isdecimal()}')
print(f'-123.isnumeric()  : {"-123".isnumeric()}')

print(f'123.5.isdigit()   : {"123.5".isdigit()}')
print(f'123.5.decimal()   : {"123.5".isdecimal()}')
print(f'123.5.isnumeric() : {"123.5".isnumeric()}')