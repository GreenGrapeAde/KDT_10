## --------------------------------------------------------
## for ~ in 반복문 : 원소 읽기용
## --------------------------------------------------------
## [1] List와 tuple, str, range
persons = [('홍길동', '대구'), ('마징가', '부산'), 'Good', range(5)]

for p in persons:
    print(p, type(p))

## [2] List와 언패킹(Unpacking)
persons = [ ('홍길동', '대구') ]

for name, loc in persons:
    print(name, loc, type(name), type(loc))  ## str 타입으로 바뀜

## --------------------------------------------------------
## for ~ in range 반복문 : 카운팅/인덱싱용
## --------------------------------------------------------
datas = ['1', '5', '0']

## str숫자 ==> int 숫자로 타입변경
for i in range(len(datas)):
    datas[i] = int( datas[i] )

print(datas)

