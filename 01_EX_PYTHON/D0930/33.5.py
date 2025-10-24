def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count


c = counter()   ## 자신만의 i 값을 기억하는 함수 객체, return된 count함수를 덩어리째 저장
for i in range(10):
    print(c(), end=' ')