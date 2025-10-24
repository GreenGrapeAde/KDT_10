## --------------------------------------------------------
## if ~else 조건문과 조건부표현식
## --------------------------------------------------------
## 조건부표현식 : 1줄 조건문
## - 형식 :   True 실행코드 if 조건식 else False 실행
## [예시1] 짝수 홀수 출력하기
num = 9

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")


if not num % 2:
    print("짝수")
else:
    print("홀수")

## ==> 조건부 표현식
print("짝수") if num % 2 == 0 else print("홀수")
print("홀수") if num % 2      else print("짝수")
print("짝수") if not num % 2  else print("홀수")

result = "짝수" if num % 2 == 0 else "홀수" # ★★★★ 변수에 무엇을 저장할 지 선택