# 타입을 여러개 가질 수 있는 객체는 유니언 타입으로 타이핑 해야한다.

from typing import *

x: Union[int, str] = 3
print(x, type(x))

x = '17'
print(x, type(x))