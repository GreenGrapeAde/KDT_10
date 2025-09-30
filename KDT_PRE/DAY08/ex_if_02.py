## --------------------------------------------------------
## 조건문 if
## - 조건에 따라 실행 코드 결정이 되는 문법
## --------------------------------------------------------
## 형식 : if 조건코드 :  <= 조건코드 결과 True/False
##       <---->실행코드
jumsu = input("Enter a message: ")  ## 입력 데이터의 앞과 끝 부분의 공백 제거
print(f'jumsu : {len(jumsu)}개, {jumsu}')
## 입력 데이터 존재 여부 체크
jumsu2 = jumsu.strip()
if len(jumsu2) > 0:
    print(f'jumsu : {len(jumsu2)}개, {jumsu2}')
    print("Data exists")
else:
    print("Data doesn't exist")

print('--- END ---')