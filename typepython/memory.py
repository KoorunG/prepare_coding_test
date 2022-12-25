"""
    1. 일반적으로 객체 내에 있는 변수들은 __dict__를 통해 관리된다.
    2. 그러나 파이썬에서는 __slots__를 통해 변수를 관리할 수 있는 방법도 있다
    3.
"""


class WithoutSlot:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlot("withoutslot", 12)
print(wos.__dict__)  # {'name': 'withoutslot', 'age': 12}
wos.__dict__["hello"] = "world"  # .__dict__ 를 통해 클래스 딕셔너리에 속성을 추가할 수 있다.
print(wos.__dict__)  # {'name': 'withoutslot', 'age': 12, 'hello': 'world'}


class WithSlot:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlot("withslot", 30)
# print(ws.__dict__)                      # 'WithSlot' object has no attribute '__dict__'
print(ws.__slots__)  # ['name', 'age']

########### 메모리 사용량 비교 ###########

import timeit


def repeat(obj):
    def inner():
        obj.name = "test"
        obj.age = 222
        del obj.name
        del obj.age

    return inner


use_dict_time = timeit.repeat(repeat(wos), number=99999)
use_slots_time = timeit.repeat(repeat(ws), number=99999)

print("use_dict_time ::: ", use_dict_time)                  # use_dict_time :::  [0.021761, 0.016708083, 0.014855624999999997, 0.014047125000000008, 0.013506041999999996]
print("use_slots_time ::: ", use_slots_time)                # use_slots_time :::  [0.009784374999999998, 0.009799832999999994, 0.010108541999999998, 0.009829582999999975, 0.009749250000000015]

