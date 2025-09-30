## 31.4
def is_palindrome(word):
    print(word[:])
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))

## 31.5
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))

## 33.5
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

## 33.6
def countdown(n):
    n += 1
    def count():
        nonlocal n
        n -= 1
        if n >= 1:
            return n
    return count

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')