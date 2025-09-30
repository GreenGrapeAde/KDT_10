## ----------------------------------------------------------------
## 함수 관련
## ----------------------------------------------------------------
## [실1] 데이터의 타입에 따른 덧셈 결과를 반환하는 함수
##       함수 이름은 back_result
##       매개변수는 3개의 데이터. 타입은 int, float, str 가능
##       단, 타입이 다르면 형변환 후 결과 반환
## ----------------------------------------------------------------
def back_result(d1, d2, d3):
    check = [True if isinstance(d, str) else False for d in [d1, d2, d3]]

    # check = [True if type(d) == str else False for d in [d1, d2, d3]]  이것도 가능함
    # 3개 데이터 중 str 타입이 하나라도 있으면 str로 형변환 후 처리
    if sum(check):
        return str(d1) + str(d2) + str(d3)
    else:
        return d1 + d2 + d3

## [테스트]
a, b, c = input("덧셈을 수행할 세개의 피연산자를 입력하세요: ").split()

print(back_result(a, b, c))
## ----------------------------------------------------------------
## [실2] 변환을 원하는 조건에 맞는 결과를 반환하는 함수
##       함수 이름은 convert_number
##       매개변수는 정수만 가능 (10진수, 8진수, 2진수, 16진수, 그 외 처리)
##       
## ----------------------------------------------------------------
def convert_number(num, to):
    if to == 2:
        return bin(num)
    elif to == 8:
        return oct(num)
    elif to == 10:
        return int(num)
    elif to == 16:
        return hex(num)
    else:
        print("올바른 진수를 입력하세요.")

num2 = int(input("변환할 정수를 입력하세요: "))
num2_1 = int(input("변환할 진수를 입력하세요: "))
print(convert_number(num2, num2_1))

## ----------------------------------------------------------------
## [실3] 사칙 연산 결과를 출력하는 함수
##       함수 이름은 print_calc
##       매개변수는 list 타입의 숫자 데이터만 가능
##       
## ----------------------------------------------------------------
def print_calc(dataList):
    for data in dataList:
        if type(data) not in [int, float]:
            return "유효한 데이터가 아닙니다."
    
    result = [dataList[0], dataList[0], dataList[0], dataList[0]]
    for data in dataList[1: ]:
        result[0] += data
        result[1] -= data
        result[2] *= data
        result[3] /= data if data != 0 else -1
    return result

print('[1, 2, 3, 4]', print_calc([1, 2, 3, 4]))