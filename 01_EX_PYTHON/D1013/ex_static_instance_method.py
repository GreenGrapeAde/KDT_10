## ---------------------------------------------------------------
## 사칙연산 계산기
## ---------------------------------------------------------------
## 클래스 기능: 사칙연산 수행 관련 클래스
## 클래스 이름: Calc4
## 부모 클래스: X
## 속      성: X
## 메  서  드: plus, minus, mult, div
## ---------------------------------------------------------------
class Calc4:
    ## 인스턴스 속성 초기화 메서드
    ## => 초기화 속성 X

    ## ---------------------------------------------------------------
    ## 인스턴스 메서드
    ## ---------------------------------------------------------------
    def plus(self, a, b): return a + b
    def minus(self, a, b): return a - b
    def mult(self, a, b): return a * b
    def div(self, a, b): return a / b if b else "0으로 나눌 수 없음!"

class SCalc4:
    ## 굳이 인스턴스가 필요없음 => 정적 메서드
    @staticmethod
    def plus(a, b): return a + b

    @staticmethod
    def minus(a, b): return a - b
    
    @staticmethod
    def mult(a, b): return a * b
    
    @staticmethod
    def div(a, b): return a / b if b else "0으로 나눌 수 없음!"

## ---------------------------------------------------------------
## 계산 진행
## ---------------------------------------------------------------
##=> 인스턴스/객체 생성
myCalc = Calc4()
print(myCalc.plus(4, 5), myCalc.div(5, 2))

## => 정적메서드에서는 인스턴스 생성 X
print(SCalc4.plus(1, 2), SCalc4.mult(4, 5))