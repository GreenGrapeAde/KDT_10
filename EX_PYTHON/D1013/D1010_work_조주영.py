# --------------------------------------------------------
## 35.5 연습문제: 날짜 클래스 만들기
# --------------------------------------------------------
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

# --------------------------------------------------------
# 프로그램 실행부
# --------------------------------------------------------

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

# --------------------------------------------------------
## 35.6 심사문제: 시간 클래스 만들기
# --------------------------------------------------------
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(":"))
        return cls(hour, minute, second)

    @staticmethod
    def is_time_valid(time_string):
        try:
            hour, minute, second = map(int, time_string.split(":"))
            return (0 <= hour < 24) and (0 <= minute < 60) and (0 <= second < 60)
        except:
            return False


# --------------------------------------------------------
# 프로그램 실행부
# --------------------------------------------------------
time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)  # 클래스를 직접 호출 => class method 사용
    print(t.hour, t.minute, t.second)
else:
    print("잘못된 시간 형식입니다.")

# --------------------------------------------------------
## 36.8 연습문제: 리스트에 기능 추가하기
# --------------------------------------------------------
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

# --------------------------------------------------------
# 프로그램 실행부
# --------------------------------------------------------
x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

# --------------------------------------------------------
## 36.9 심사문제: 다중 상속 사용하기
# --------------------------------------------------------
class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다')

# --------------------------------------------------------
# 프로그램 실행부
# --------------------------------------------------------

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

# --------------------------------------------------------
## 37.2 연습문제: 사각형의 넓이 구하기
# --------------------------------------------------------
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# --------------------------------------------------------
# 프로그램 실행부
# --------------------------------------------------------

rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height
print(area)

# --------------------------------------------------------
## 37.3 심사문제: 두 점 사이의 거리 구하기
# --------------------------------------------------------
import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y



# --------------------------------------------------------
# 프로그램 실행부
# --------------------------------------------------------
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

length = math.sqrt(abs(p[3].x - p[0].x) ** 2 + abs(p[3].y - p[0].y) ** 2)
print(length)