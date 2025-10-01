## [1] homework.txt, message.txt 파일 읽어서 출력
FILE_1 = './homework.txt'
FILE_2 = './message.txt'
FILE_3 = './data.txt'
FILE_4 = './data_copy.txt'

def print_file(originF, encode='utf-8'):
    with open(originF, mode='r', encoding=encode) as f:
        print(f.read())

print_file(FILE_1)
print_file(FILE_2, 'cp949')

## [2] data.txt를 복사해서 data_copy.txt 생성
def copy_file(originF, copyF, encode='utf-8'):
    with open(originF, mode='r', encoding=encode) as rf:
        with open(copyF, mode='w', encoding=encode) as wf:
            wf.write(rf.read())

copy_file(FILE_3, FILE_4)