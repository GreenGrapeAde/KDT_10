# ------------------------------------------------
# 비교연산자와 논리연산자
# - 결과값 : bool 타입의 True/False
# ------------------------------------------------
# 두 개의 글자 데이터를 비교하기
# 글자 1개 1개의 각각 코드값을 비교함
word1 = 'abc'
word2 = 'abC'

print(f'{word1} < {word2}  => { word1 < word2 }') # False
print(f'{word1} > {word2}  => { word1 > word2 }\n')

print(f'{word1} <= {word2} => { word1 <= word2 }')
print(f'{word1} >= {word2} => { word1 >= word2 }\n')

print(f'{word1} == {word2} => { word1 == word2 }')
print(f'{word1} != {word2} => { word1 != word2 }\n')

# ------------------------------------------------
# 논리연산자
# - 결과값 : bool 타입의 True/False
# - 여러 개의 조건이나 값을 평가하는 연산자
# - 종류: and, or, not
# ------------------------------------------------
# 성별, 나이, 지역 입력 받아서 논리 연산 결과 출력
gender = input("성별(예] 남) : ")
age = int(input("나이 : "))
loc = input("지역 : ")

# 기준 1] 대구 지역이거나 나이가 20세 미만이거나 여자이거나
#         -> or 연산자 : 조건이 모두 False만 아니면 값이 True
print(f'OR 연산자 => { gender == "여" or age < 20 or loc == "대구"}\n')

# 기준 2] 대구 지역에 30대인 사람은 지원하세요.
print(f'AND 연산자 => { loc == "대구" and (age >= 30  and age < 40) }\n')

# 기준 3] 대구 지역이 아니신 분 지원하세요.
#         -> not 연산자 : toggle 결과의 반대 (토글링)
print(f'NOT 연산자 => { not loc == "대구"}\n')