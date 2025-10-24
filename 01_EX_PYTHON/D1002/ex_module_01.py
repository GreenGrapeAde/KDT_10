## --------------------------------------------------------
## 패키지 사용하기
## - 패키지: 유사한 기능/목적의 모듈들을 하나로 묶어서 관리하는 것
## - 사용: import 패키지명.모듈명
##        import 패키지명.모듈명 as 약칭
##        from 패키지명.모듈명 import 변수, 함수, 클래스
##        from 패키지명.모듈명 import *  
## --------------------------------------------------------
## 모듈 로딩
## --------------------------------------------------------
import urllib.request as req

## --------------------------------------------------------
## 모듈의 변수, 함수, 클래스 사용 => 모듈명, 변수명 / 모듈명.함수명()
## --------------------------------------------------------
data = req.urlopen("https://docs.python.org/3.11/library/datetime.html")
print(f'data => {type(data)}')  ## <class 'http.client.HTTPResponse'>
print(f'data.url => {data.url}')
print(f'data.status => {data.status}')
print(f'data.read => {data.read}')
# print(f'math.pi => {math.pi}')

## req.urlretrieve(URL, filename): 해당 URL을 파일로 저장
IMG_URL = "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg?h=430&w=710&hash=7FEB820D235A44B76B271060E03572C7"
req.urlretrieve(IMG_URL, "dog.jpg")