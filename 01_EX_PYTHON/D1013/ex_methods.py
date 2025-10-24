## ---------------------------------------------------------------
## 메서드 바인딩 (Binding)
## 목적: 인터프리터의 불필요한 매개변수 전달을 피하기 위함
## -> 인스턴스 메서드: self          데코레이터 X
## -> 클래스 메서드: cls             @classmethod
## => 일반/순수 메서드: x            @staticmethod
## => 데코레이터를 사용해야함
## ---------------------------------------------------------------
## 개념 이해용 클래스
## ---------------------------------------------------------------
class C:
    def inst(self):                 # 일반 인스턴스 메서드 : self 전달
        return "self OK"
    
    @staticmethod
    def sm(x):                      # 정적 메서드: 바인딩 없음, 함수처럼 사용
        return f"x={x}"
    
    @classmethod
    def cm(cls):                    # 클래스 메서드 : cls 전달
        return f"cls={cls.__name__}"
    

c1 = C()                # OK, self 자동 바인딩
print(c1.inst())
# print(C.inst())       # self 없으므로 Error / 반드시 인스턴스를 생성해야 함

print(C.sm(10))         # x = 10
print(c1.sm(10))        # x = 10 (여전히 self 안 넘어옴!)

print(C.cm())           # cls = C
print(c1.cm())          # cls = C (인스턴스로 불러도 cls 전달)