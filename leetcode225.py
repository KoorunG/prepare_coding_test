# https://leetcode.com/problems/implement-stack-using-queues/
import collections


# 두개의 큐를 이용하여 스택을 구현하여라.
# 구현한 스택은 (push, top, pop, empty) 함수를 지원해야 한다.
# void push(int x) : 스택의 최상단에 x를 넣는다.
# int pop() : 스택 최상단의 값을 빼낸 뒤 리턴한다.
# int top() : 스택 최상단의 값을 리턴한다.
# boolean empty() : 스택이 비어있는지 여부를 리턴한다.

# deque로 큐를 선언하고 큐 연산만을 이용하여 스택을 구현해보자!
class MyStack:

    def __init__(self):
        self.deque = collections.deque()

    def push(self, x: int) -> None:
        self.deque.append(x)
        for i in range(len(self.deque) - 1):
            self.deque.append(self.deque.popleft())

    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return len(self.deque) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())