## ---------------------------------------------------------------
## 상속(Inheritance)
## - 클래스 재사용 및 확장 용도
## - 구성: 부모/Super 클래스 <-- 자식/Sub 클래스
## - 최상위 부모클래스: Object. 자동 상속이 되어서 명시하지 않음!!
## ---------------------------------------------------------------
## 클래스 기능: Point 데이터 표현 클래스
## 클래스 이름: Point
## 속성 / 특징: x, y, color
##            클래스  속성 => 없음
##            인스턴스 속성 => 모든 속성
##            비공개   속성 => 없음
## 기능 / 역할: 그리기, 정보 출력기능
## ---------------------------------------------------------------
class Point:
    ##- 메모리 스캔 및 할당
    def __new__(cls, *args, **kwargs):
        print("Frome new")
        # 메모리 스캔 및 인스턴스를 생성하고 반환
        obj = super().__new__(cls)
        return obj
    
    def __init__(self, x=0, y=0, color='black'):
        print("From init")
        self.x = x
        self.y = y
        self.color = color

    def drawing(self):
        print(f'({self.x}, {self.y}) 위치에 {self.color}점 그리기')

    def print_info(self):
        print(f'색상: {self.color}')
        print(f'위치: {self.x}, {self.y}')

## ---------------------------------------------------------------
## 클래스 기능: Point 3D 데이터 표현 클래스
## 클래스 이름: Point
## 부모 클래스 Point
## 속성 / 특징: x, y, z, color
##            클래스  속성 => 없음
##            인스턴스 속성 => 모든 속성
##            비공개   속성 => 없음
## 기능 / 역할: 그리기, 정보 출력기능
## ---------------------------------------------------------------
class Point3D(Point):
    def __init__(self, x=0, y=0, z=0, color='black'):
        super().__init__(x, y, color)
        print("From init Point3D")
        self.z = z

    ## Overriding(재정의)
    def drawing(self):
        print(f'({self.x}, {self.y}, {self.z}) 위치에 {self.color}점 그리기')

    # def print_info(self):
    #     print(f'색상: {self.color}')
    #     print(f'위치: {self.x}, {self.y}')

## ---------------------------------------------------------------
## 인스턴스/ 객체 생성 및 활용
## ---------------------------------------------------------------
p1 = Point3D(x=10, y=25, color='red')
print(p1.color, p1.z)