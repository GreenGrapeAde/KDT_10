## 다른 파일에 import 될 때 간단하게 작성하기 위해서 사용됨
## [1]
## . -> 현재위치
# from . import operation
# from . import geometry

# print('__init__.py')
## [2]
## 패키지 내 모듈들의 모든 것을 import 
# from .operation import *
# from .geometry import *



## [3]
## 패키지 내 모듈들의 일부만 공개하도록 설정
##     __all__ -> 매직변수코드에 설정
__all__ = ['add', 'mul', 'triangle_area']

from .operation import *
from .geometry import *


print('__init__.py')