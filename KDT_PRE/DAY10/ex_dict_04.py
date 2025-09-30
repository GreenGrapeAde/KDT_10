## ----------------------------------------------------------------
## Dict 자료형 - 전용 메서드(Method)
## ★ 필수 메서드 : keys(), values(), items()
## ----------------------------------------------------------------
## [실습] 5과목의 점수를 저장합니다.
##       합계, 평균 출력
## ----------------------------------------------------------------
## [list]
jumList = [98, 99, 100, 78, 88]
print(f'합계 : {sum(jumList)}, 평균 : {sum(jumList) / len(jumList)}')

## [dict-2]
jumDict = {'과목1': 98, '과목2': 99, '과목3': 100, '과목4': 78, '과목5': 88}

values = jumDict.values()
print(f'합계 : {sum(values)}, 평균 : {sum(values) / len(jumDict)}')
print(f'최대 : {max(jumDict)}, 최소 : {min(jumDict)}')  ## ★★★ key들의 아스키 코드 값으로 비교함

## [dict-3] => 내장함수는 dict의 Key만 사용
jumDict = {1: 98, 2: 99, 3: 100, 4: 78, 5: 88}

print(f'합계 : {sum(jumDict)}, 평균 : {sum(jumDict) / len(jumDict)}')  ## ★★★ jumDict의 key가 모두 int이므로
print(f'최대 : {max(jumDict)}, 최소 : {min(jumDict)}')