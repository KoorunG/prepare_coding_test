from typing import *

# 파이썬에서 기본 지원하는 타입
int_var: int = 30
str_var: str = "koorung"
float_var: float = 30.1

# 여기서부터는 typing 모듈을 사용해야 한다.
list_var: List[int] = [1, 2, 3]
tuple_var: Tuple[int] = (1, 2, 3)
dic_var: Dict[str, int] = {"koorung", 30}


# isinstance(obj, class) 를 이용하여 타입 강제 validation 기능을 추가할 수 있다.
def type_check(obj, typer: Type) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}, but : {type(obj)}")


# typing 모듈에서 warning을 보내주긴 하지만 정상적으로 실행된다.
def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y


print(cal_add(3, 4))
# print(cal_add('3', '4'))            # TypeError: Type Error : <class 'int'>, but : <class 'str'>
# print(cal_add([1, 2], [3, 4]))      # TypeError: Type Error : <class 'int'>, but : <class 'list'>