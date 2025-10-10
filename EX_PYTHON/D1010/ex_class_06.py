## --------------------------------------------------------
## 객체지향언어(OOP) 특성 - 정보은닉/캡슐화
##
## - 파이썬은 모든 속성/메서드를 공개하는 것이 원칙
## - ★★그러나 비공개 속성 설정을 제공함: __속성명
## - 비공개 속성 사용 관련 간접 접근 메서드
##   * 비공개 속성값 읽기 메서드 => get속성명()
##   * 비공개 속성 값 변경 메서드 => set속성명(새로운 값)
## --------------------------------------------------------
## 클래스 정의: 한국 사람 데이터 타입 정의
## 클래스 이름: KoreanPeople
## 속      성: 나이, 이름, 성별, 주민번호, 국적
##            인스턴스 속성         => 나이, 이름, 성별, __주민번호
##            클래스 속성          => 국적
## 메  서  드: 정보 출력하기        => 인스턴스 메서드
##            비공개 나이계산 가능  => __인스턴스 메서드
##            비공개 속성 간접 접근 => 읽기 메서드 get_jumin()
## --------------------------------------------------------
class KoreanPeople:
    ## 클래스 속성/변수
    NATL = 'KO'

    ## 인스턴스 생성 및 속성 초기화 메서드
    def __init__(self, name_, age_, gender_, jumin_):
        self.name = name_
        self.age = age_
        self.gender = gender_
        self.__jumin = jumin_    ## ★★ 외부 접근 불가

    ## 인스턴스 메서드 => 공개, 개인정보 출력
    def print_info(self):
        print('*' * 20)
        print(f'이   름: {self.name}')
        print(f'나   이: {self.age}')
        print(f'성   별: {self.gender}')
        print(f'주민번호: {self.__jumin}')
        print('*' * 20)

    ## 연산자 메서드 오버로딩 => 매개변수 타입, 개수 다른 메서드
    ## 각 객체/인스턴스 나이를 덧셈 후 반환
    def __add__(a, b):    ## 연산자 괄호 안에 (self, other) 해도 됨
        print("__add__()")
        return a.age + b.age

    ## 비공개 속성 간접접근 메서드 => 읽기 메서드
    def get_jumin(self):
        return self.__jumin
    
    def set_jumin(self, new_value):
        self.__jumin = new_value
## --------------------------------------------------------
## 속성과 메서드 활용
## --------------------------------------------------------
## 객체/인스턴스 생성
hong = KoreanPeople("홍길동", 20, '남자', '051020-3000000')

## 객체/인스턴스 속성 읽기
print(hong.age)
# print(hong.__jumin)     ## private attribute라서 읽을 수 없음
print(hong.get_jumin())   ## <== 간접 접근 메서드

## 객체/인스턴스 속성 변경
hong.age = 100
hong.__jumin = ''        ## private attribute이므로 인스턴스에서 새로운 attribute를 만들어 버림

## 051020 -> 051120
jumin = hong.get_jumin()
jumin = jumin.replace('051020', '051120')
hong.set_jumin(jumin)
print(hong.get_jumin())
