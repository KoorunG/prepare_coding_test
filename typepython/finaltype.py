# 파이널 타입
# 파이썬에서는 상수라는 개념이 없기 때문에 암묵적으로 대문자를 사용하는 것을 상수로 정해왔는데
# Final 타이핑을 하는 것으로 이를 정할 수 있다.

from typing import *

RATE: Final = 300
RATE = 200 # error: "RATE" is declared as Final and cannot be reassigned

print(RATE)