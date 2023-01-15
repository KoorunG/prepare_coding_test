# 옵셔널타입 : 있을수도 있고 없을수도 있는 경우
# 유니언타입으로 대체가 가능하다

from typing import *

x: Union[str, None]

x = "test"
x = None

print(x)

y: Optional[str]
y = "test2"
y = None

print(y)