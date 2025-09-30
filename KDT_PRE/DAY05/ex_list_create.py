## --------------------------------------------------------
## 컨테이너 자료형 : 여러 개의 데이터를 저장할 수 있는 자료형
## -> 그 중에 순서 있는 자료형 : 시퀀스(Sequence) 자료형
## --------------------------------------------------------
## [1]-> list
## - 형식: [ 데이터1, 데이터2, ..., 데이터n ]
##        [] (empty list)
## --------------------------------------------------------
data = []                            ## empty string, 인터프리터가 알아서 list([])로 해석
print(type(data), len(data))

data = list([])                      ## empty string, 정석 방식
print(type(data), len(data))         ## 생성자(constructor)

data = [1,3,9]                       ## list([1, 3, 9]) <- 인터프리터가 변환 
print(type(data), len(data))

data = [False, "Good", 4.9, 7]       ## list([1, 3, 9]) <- 인터프리터가 변환 
print(type(data), len(data))

data = [False, "Good", 4.9, 7, []]   ## list도 자료형이므로 list안에 list 원소 추가 가능 
print(type(data), len(data))