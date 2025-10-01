## ------------------------------------------------------------
## 파일 입출력하기
## ------------------------------------------------------------
## - 내장함수: open()
## * filepath + filename: 존재하면 내용을 지우고 쓰기, 없으면 생성
## * mode               : 파일 작업 모드 설정
##                        'w' - 기존 내용 삭제, 새롭게 쓰기
##                        'a' - 기존 내용에 추가
## * encoding           : 기계어 변환(코드화)위한 기준 테이블
## * 반환값              : 파일 접근 가능한 객체/주소
## ------------------------------------------------------------
## 전역변수 정의
## ------------------------------------------------------------
FILE_NAME = './test.txt'

## ------------------------------------------------------------
## 파일에 쓰기 기능
## ------------------------------------------------------------
## [1] 파일 열기 - mode='w': 기존 내용 삭제 후 쓰기
## - 영어 외의 언어 입력 시 encoding 지정
with open(FILE_NAME, mode='w', encoding='utf-8') as f:

    ## [2] 파일에 쓰기 => 데이터 미리 존재, 줄바꿈이 되지 않음에 주의
    data = ['Good Luck', 'Happy New Year', '2025!!', '오늘은 좋은날']
    data = [d + '\n' for d in data]

    cnt = f.writelines(data)



## [1] 파일 열기 - mode='a': 기존 내용 아래에 내용 추가하기 (append)
## - 영어 외의 언어 입력 시 encoding 지정
with open(FILE_NAME, mode='a', encoding='utf-8') as f:

    ## [2] 파일에 쓰기 => 데이터 미리 존재, 줄바꿈이 되지 않음에 주의
    data = ['Good Luck', 'Happy New Year', '2025!!', '오늘은 좋은날']
    data = [d + '\n' for d in data]

    cnt = f.writelines(data)

## x는 배타적(exclusive). 파일 이름이 기존에 존재한다면 에러를 발생시킨다.
FILE_NAME = './exclusive.txt'
with open(FILE_NAME, mode='x', encoding='utf-8') as f:

    ## [2] 파일에 쓰기 => 데이터 미리 존재, 줄바꿈이 되지 않음에 주의
    data = ['Good Luck', 'Happy New Year', '2025!!', '오늘은 좋은날']
    data = [d + '\n' for d in data]

    cnt = f.writelines(data)