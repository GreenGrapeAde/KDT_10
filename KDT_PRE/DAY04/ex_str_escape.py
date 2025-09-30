## ------------------------------------------------------
## str 타입과 escape 문자
## ------------------------------------------------------
## escape => '\문자 1개' 형식으로 특별한 의미를 가지는 문자
## 대표적인 escape 문자
## - '\n' : new line 약자. 줄바꿈 의미
## - '\t' : tab 약자. 키보드 탭 간격 의미
## - '\\' : 기호 \ 의미
## - '\'' : 단일 인용부호
## - '\"' : 이중 인용부호
## - '\u' : 유니코드 u222

print('\\n=>', "Good\nLuck!")
print('\\t=>', "Good\tLuck!")
print("\"=>", "Good Luck \"2020\"")
print('\'=>', 'Good \'Luck\' 2020')
print('\\u=>', 'Good \uAC00 Luck 2020')

## 경로 문자열
print('파일경로=>', 'C:\\Users\\sante\\Documents\\cat.jpg')

## str 내의 모든 escape 문자를 무시하도록 설정
print('파일경로=>', r'C:\Users\sante\Documents\cat.jpg') # ** 'r' 또는 'R': raw string literal (원시 문자열)
