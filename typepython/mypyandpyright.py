from typing import *

# 파이썬에서 기본 지원하는 타입
int_var: int = 30
str_var: str = "koorung"
float_var: float = 30.1

# 여기서부터는 typing 모듈을 사용해야 한다.
list_var: List[int] = [1, 2, 3]
tuple_var: Tuple[int, int, int] = (1, 2, 3)
dic_var: Dict[str, int] = {"koorung": 30}


# typing 모듈에서 warning을 보내주긴 하지만 정상적으로 실행된다.
def cal_add(x: int, y: int) -> int:
    return x + y


print(cal_add(3, 4))
print(cal_add('3', '4'))            # TypeError: Type Error : <class 'int'>, but : <class 'str'>
print(cal_add([1, 2], [3, 4]))      # TypeError: Type Error : <class 'int'>, but : <class 'list'>
