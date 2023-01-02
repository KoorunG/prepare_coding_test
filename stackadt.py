# ADT(Abstract Data Type) : 스택 추상 자료형을 연결리스트로 구현해보자

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)   # 연결리스트에 요소를 추가하면서 self.last를 next로 지정한다.
                                            # 포인터 last를 가장 마지막으로 이동시킨다.

    def pop(self):
        item = self.last.item       # last의 item을 꺼낸다.
        self.last = self.last.next  # 다음 Node가 last가 된다. (last 포인터를 한칸 앞으로 전진시킨다.);
        return item                 # item을 리턴한다.


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.last.item)  # 5
print(stack.pop())      # 5
print(stack.pop())      # 4
print(stack.pop())      # 3
print(stack.pop())      # 2
print(stack.pop())      # 1
# print(stack.pop())      # AttributeError
