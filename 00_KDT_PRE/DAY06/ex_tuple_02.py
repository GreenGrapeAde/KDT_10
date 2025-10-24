## --------------------------------------------------------
## 순서가 있는 (Sequence) 자료형 - tuple
## - 변경/삭제위한 list 형변환 진행 ==> tuple 다시 변환
## --------------------------------------------------------
## 튜플 생성 : (데이터1, .., 데이터n)
##            데이터1, ..., 데이터n
##            (데이터,)
##             데이터,
## --------------------------------------------------------
## phone => 010, 016, 017, 018, 019 
phone=('011', '016', '017', '018', '019')

print(f'phone: {type(phone)}, {len(phone)}개, {phone}')

## 전부다 010 변경 => list 형변환
phone = list(phone)
phone[:] = ['010']
print(f'phone: {type(phone)}, {len(phone)}개, {phone}')

## 다시 => tuple로 변환
phone = tuple(phone)
print(f'phone: {type(phone)}, {len(phone)}개, {phone}')