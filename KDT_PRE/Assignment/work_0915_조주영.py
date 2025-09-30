# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##                   제출 : work_0915_이름.py
# ## ----------------------------------------------------------------

# ## ----------------------------------------------------------------
# 1. 제곱 사전 만들기 문제 입니다. 
#    정수 리스트 [1, 2, 3, 4, 5]가 주어졌을 때,
#    key는 원래 숫자, value는 제곱 값으로 하는 딕셔너리를 
#    dict comprehension으로 작성하세요.
nums1 = [1, 2, 3, 4, 5]

squares1 = {n: n**2 for n in nums1}

print(squares1)


# ## ----------------------------------------------------------------
# 2. 홀수만 추출한 집합 만들기
#    정수 리스트 [1, 2, 3, 4, 5, 6, 7]에서 홀수만 모은 set을 
#    set comprehension으로 작성하세요.
nums2 = [1, 2, 3, 4, 5, 6, 7]

odds2 = {n for n in nums2 if n % 2 == 1}

print(odds2)

print(f' 2번 결과: {list(filter(lambda n: n % 2, nums2))}')


# ## ----------------------------------------------------------------
# 3. 문자열 길이 매핑 
#    문자열 리스트 ["apple", "banana", "cherry"]가 있을 때,
#    key는 문자열, value는 문자열의 길이가 되도록 딕셔너리를 
#    dict comprehension으로 작성하세요.
words3 = ["apple", "banana", "cherry"]

lengths3 = {w: len(w) for w in words3}

print(lengths3)
# ## ----------------------------------------------------------------
# 4. 구구단 dict
#    2단(2×1 ~ 2×9)의 결과를 딕셔너리로 만들되,
#    key는 곱하는 수(1~9), value는 곱셈 결과가 되도록 
#    dict comprehension으로 작성하세요.
dan4 = { i: 2 * i for i in range(1, 10)}

print(dan4)


# ## ----------------------------------------------------------------
# 5. 중복 없는 알파벳 집합 
#    문자열 "hello world"에서 공백을 제외한 알파벳 집합을 
#    set comprehension으로 작성하세요.
msg5 = "hello world"

alphabets5 = {ch for ch in msg5 if ch != " "}

print(alphabets5)

# ## ----------------------------------------------------------------
# 6. 조건부 딕셔너리
#    정수 리스트 range(1, 11)이 있을 때,
#    짝수만 key로 사용하고, value는 제곱 값을 가지는 딕셔너리를 
#    dict comprehension으로 작성하세요.
nums6 = [i for i in range(1, 11)]

squares6 = {num: num**2 for num in nums6 if num % 2 == 0}

print(squares6)
# ## ----------------------------------------------------------------
# 7. 정수 리스트를 입력받아 최댓값을 반환하는 함수 find_max(nums)를 작성하세요.
#    (내장 함수 max()는 사용하지 말 것)
def find_max(nums):
    result7 = 0
    for num in nums:
        if num > result7:
            result7 = num

    return result7

nums7 = [int(n) for n in input("리스트에 넣을 정수 입력: ").split()]
print(find_max(nums7))

# ## ----------------------------------------------------------------
# 8. 정수 n을 입력받아 n! (팩토리얼)을 반환하는 함수 factorial(n)을 작성하세요.
#    (반복문 사용 가능)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

num8 = int(input("팩토리얼 정수 입력: "))
print(factorial(num8))

# ## ----------------------------------------------------------------
# 9.  문자열을 입력받아 거꾸로 뒤집은 문자열을 반환하는 함수 reverse_string(s)를 
#     작성하세요.
def reverse_string(s):
    return s[::-1]

text9 = input("거꾸로 뒤집을 문자열 입력: ")
print(reverse_string(text9))
# ## ----------------------------------------------------------------
# 10. 정수 n을 입력받아 n단을 문자열 리스트 형태로 반환하는 함수 
#     multiplication_table(n)을 작성하세요.
#     예시 (n=3)
#     ["3 x 1 = 3", "3 x 2 = 6", ..., "3 x 9 = 27"]
def multiplication_table(n):
    return [f'{n} x {i} = {n * i}' for i in range(1, 10)]

dan10 = int(input("출력할 단을 입력하세요: "))
print(multiplication_table(dan10))
# ## ----------------------------------------------------------------
# 11. 문자열이 회문(palindrome: 앞뒤가 같은 문자열)인지 판별하는 함수 
#     is_palindrome(s)를 작성하세요.
def is_palindrome(s):
    return s == s[::-1]

text11 = input("회문을 검사할 문자열 입력: ")
print(is_palindrome(text11))

# ## ----------------------------------------------------------------
# 12. 문자열 문장을 입력받아 단어별 등장 횟수를 딕셔너리로 반환하는 함수 
#     word_count(sentence)를 작성하세요.
#     예시 : "apple banana apple"  → {"apple": 2, "banana": 1}
def word_count(sentence):
    words = sentence.split()
    return {w: words.count(w) for w in set(words)}

text12 = input("문자열 문장 입력: ")
print(word_count(text12))

# ## ----------------------------------------------------------------
# 13. 정수 n을 입력받아, n번째 항까지의 피보나치 수열을 리스트로 반환하는 함수 
#     fibonacci(n)을 작성하세요.
# 예시 : fibonacci(5) → [0, 1, 1, 2, 3]
def fibonacci(n):
    result13 = []
    a, b = 0, 1
    for i in range(n):
        result13.append(a)
        a, b = b, a + b
    return result13

num13 = int(input("피보나치 수열을 위한 정수 입력: "))
print(fibonacci(num13))
# ## ----------------------------------------------------------------
# 14. 정수 리스트를 입력받아 평균과 표준편차를 튜플 (mean, std)로 반환하는 함수 
#     stats(nums)를 작성하세요.
#     ( 공식을 직접 구현하세요)
def stats(nums):
    mean = sum(nums) / len(nums)
    var = sum((x - mean) ** 2 for x in nums) / len(nums)
    std = var ** 0.5
    return mean, std

nums14 = [int(n) for n in input("평균과 표준편차를 구할 정수 리스트 입력: ").split()]
print(stats(nums14))