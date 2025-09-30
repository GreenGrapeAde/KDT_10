## --------------------------------------------------------
## List Comprehension : [] + for ~ in + if ~ else
## --------------------------------------------------------
## [요청] data1 리스트의 요소에 3을 곱한 값을 새로운 리스트에 저장
## --------------------------------------------------------
data1 = [1, 2, 3]

# [방법1]
data2 = []              ## empty list

for d in data1:
    data2.append(d * 3)

print(f'data2 => {data2}')

# [방법2]
result = [ d*3 for d in data1]
print(f'The result using list comprehension is: {result}')