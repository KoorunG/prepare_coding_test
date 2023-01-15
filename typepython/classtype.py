from typing import *


class Hello:
    def world(self) -> str:
        return "world"


class World:
    pass


hello: Hello = Hello()
world: World = World()


def foo(ins: Hello) -> str:
    # 클래스 타이핑은 따옴표를 사용하여 하는것이 가능하다.
    # def foo(ins: "Hello") -> str:
    return ins.world()


print(foo(hello))  # 이상없음


print(foo(world))
'''
error: Argument of type "World" cannot be assigned 
to parameter "ins" of type "Hello" in function "foo" 
'''


# 클래스 타입 보충
class ListNode:
    # 클래스 안에서 자기 자신을 타이핑 할 때 따옴표로 묶어주면 수월하다!
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# 12 - 24인 연결 리스트
node2 = ListNode(24)
node = ListNode(12, node2)
print(node.next.val)
