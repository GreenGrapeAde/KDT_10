## ----------------------------------------------------------------
## 내장함수 sorted()
## - 형식: sorted(iterable, reverse=False, key=None)
## - 기능: 오름차순 정렬 후 결과를 ★★★★ 리스트로 반환
## ----------------------------------------------------------------
## 데이터 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수만 추출해서 저장
## list 타입의 iterable 데이터 --------------------------------------
data = [3, 7, 6, 4, 5, 1, 2, 3]

asc = sorted(data)
desc = sorted(data, reverse=True)

print('asc => ', asc, '\ndesc => ', desc)

## tuple 타입의 iterable 데이터 --------------------------------------
data = (3, 7, 6, 4, 5, 1, 2, 3)

asc = sorted(data)
desc = sorted(data, reverse=True)

print('asc => ', asc, '\ndesc => ', desc)

## set 타입의 iterable 데이터 --------------------------------------
data = {3, 7, 6, 4, 5, 1, 2, 3}

asc = sorted(data)
desc = sorted(data, reverse=True)

print('asc => ', asc, '\ndesc => ', desc)

## dict 타입의 iterable 데이터 --------------------------------------
data = {'A': 10, 'Z': 7, 'D': 20, 'B': 100}

## => key위주: key정렬
asc = sorted(data)
desc = sorted(data, reverse=True)

print('asc => ', asc, '\ndesc => ', desc)

## => value 정렬을 위해서 정렬 기준 설정. key 매개변수에
## => (k,v) : items() [0] => key, [1] => value
asc = sorted(data.items(), key=lambda item: item[1]) ## ★★★★ 람다함수 사용, 리스트 타입으로 반환
desc = sorted(data.items(), reverse=True, key=lambda item: item[1])

print('asc => ', asc, '\ndesc => ', desc)

## => sorted() 내장함수의 정렬 기준 설정 => key 매개변수 ----------------
data = ['Good', 'apple', 'Zoo', 'banana']
asc = sorted(data)
desc = sorted(data, reverse=True)

print('asc => ', asc, '\ndesc => ', desc)

asc = sorted(data, key=lambda d: d.lower())   ## ★★ 람다함수 사용, 소문자 기준으로 정렬, 데이터 값은 바뀌지 않는다
desc = sorted(data, reverse=True, key=lambda d: d.lower())

print('asc => ', asc, '\ndesc => ', desc)