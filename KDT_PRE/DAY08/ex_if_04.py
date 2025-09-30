## --------------------------------------------------------
## 다중 if문
## - if / elif / else / 이때 else는 선택
## --------------------------------------------------------
## 점수에 대한 학점 출력하기----------------------------------
## ->  A : 90점이상
## ->  B : 80점이상
## ->  C : 70점이상
## ->  D : 60점이상
## ->  F : 나머지
score = int(input("Please enter a score: "))

# 다중조건문
if score >= 90:
    print(f" your socre is {score}, grade A.")
elif score >= 80:                                  # elif는 자동으로 break를 수행하므로 'and score < 90'을 굳이 쓸 필요없음
    print(f" your socre is {score}, grade B.")
elif score >= 70:
    print(f" your socre is {score}, grade C.")
elif score >= 60:
    print(f" your socre is {score}, grade D.")
else:
    print(f" your socre is {score}, grade F.")

## 조건문 여러개
## 주의 ★★★★) 자동으로 90점 입력시 A, B, C, D를 모두 출력하게 된다.
if score >= 90:
    print(f" your socre is {score}, grade A.")
if score >= 80:
    print(f" your socre is {score}, grade B.")
if score >= 70:
    print(f" your socre is {score}, grade C.")
if score >= 60:
    print(f" your socre is {score}, grade D.")
if score < 60:
    print(f" your socre is {score}, grade F.")