# 파이썬에서도 제네릭 타입을 사용할 수 있다.

from typing import Union, Optional, TypeVar, Generic

# 일반적인 변수선언처럼 제네릭 변수를 선언할 수 있다.
# TypeVar을 사용하여 선언한다.

# T = TypeVar("T")
T = TypeVar("T", int, float, str)
# K = TypeVar("K")
K = TypeVar("K", int, float, str)


# 제네릭은 여러개를 등록하는 것이 가능하다.
class Robot(Generic[T, K]):
    # 각 부품은 암호화된 상태로 넘어옴
    def __init__(self, arm: T, head: K):
        self.arm = arm
        self.head = head

    # 암호를 해독하는 코드
    def decode(self) -> None:
        print(f"{type(self.arm)} ::: {self.arm}", f"{type(self.head)} ::: {self.head}")


robot1 = Robot[int, int](12321310, 5436456)
robot2 = Robot[str, int]("45735213", 1236456)
robot3 = Robot[float, str](24573.213, "3678456")

robot1.decode()
robot2.decode()
robot3.decode()


class Siri(Generic[T, K], Robot[T, K]):
    pass


siri1 = Siri[int, int](12321310, 5436456)
siri2 = Siri[str, int]("45735213", 1236456)
siri3 = Siri[float, str](24573.213, "3678456")

siri1.decode()
siri2.decode()
siri3.decode()


# 함수에서의 제네릭 사용
def test(x: T) -> T:
    return x


print(test(80))
print(type(test(80)))