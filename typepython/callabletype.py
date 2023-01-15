from typing import *


def add(a: int, b: int):
    # 리턴이 없는 경우
    print(a + b)


print(add(1, 3))


# print(add(1, "33"))


# Callable의 첫번째 인자 : Callable 객체가 인자 타입 정보
# Callable의 두번째 인자 : Callable 객체가 리턴하는 타입
def test(func: Callable[[int, int], None]) -> None:
    return func(2, 3)


test(add)
