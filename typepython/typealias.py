# 타입스크립트와 비슷하게 타입별칭을 지정할 수 있다.

from typing import *

# 타입이 이런식으로 매우 복잡해질 수 있는데
value: Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]] = 17


def calculate(value: Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]):
    return value


# 1. 타입별칭 : 변수 선언처럼 그냥 선언하는 것으로 타입별칭을 지정할 수 있다.
Value = Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]


def calculate2(value: Value) -> Value:
    return value


# 2. 딕셔너리 별칭
# JSON은 파이썬의 딕셔너리로 매핑이 되는데, int나 bool처럼 str으로 넘어오지 않는 경우가 종종 있다.
# 이럴 때 딕셔너리 별칭을 사용하면 편하다.
custom_dict: Dict[str, Union[str, int, bool]] = {"hello": "world", "test": "test2", "age": 17, "isHuman": False}


# TypedDict를 상속받은 클래스를 정의하면 딕셔너리의 타입을 fit하게 맞출 수 있다.
class Point(TypedDict):
    x: int
    y: float
    z: str


point: Point = {"x": 8, "y": 8.4, "z": "12"}
