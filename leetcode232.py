# https://leetcode.com/problems/implement-queue-using-stacks/

# 스택을 이용하여 큐를 구현하라. 구현한 큐는 다음 함수를 지원해야 한다.
# push(x) : 요소 x를 큐의 마지막에 삽입
# pop() : 큐 처음 요소를 제거
# peek() : 큐 처음 요소를 조회
# empty() : 큐가 비어있는지 여부를 리턴

# 문제풀이용 스택 구현 (그냥 파이썬의 리스트를 사용해도 되긴 함)
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)

    def top(self) -> int:
        return self.stack[self.size() - 1]

    def empty(self) -> bool:
        return self.size() == 0


# 큐 구현
class MyQueue:
    def __init__(self):
        self.input = MyStack()
        self.output = MyStack()

    def push(self, x: int) -> None:
        self.input.push(x)

    def pop(self) -> int:
        # peek을 실행한 뒤
        self.peek()
        # output에서 pop한 값을 리턴
        return self.output.pop()

    def peek(self) -> int:
        # output 스택이 비어있다면
        if self.output.empty():
            # input 스택이 빌 동안
            while not self.input.empty():
                # output 스택에 input 스택에서 pop하여 집어넣는다.
                self.output.push(self.input.pop())
        # output의 top을 리턴
        return self.output.top()

    # 두 스택에 값이 모두 없을 때 True 리턴
    def empty(self) -> bool:
        return self.input.empty() and self.output.empty()


myqueue = MyQueue()
myqueue.push(1)
myqueue.push(2)
myqueue.push(3)
myqueue.push(4)
print(myqueue.peek())
myqueue.push(5)
print(myqueue.pop())
print(myqueue.pop())
print(myqueue.pop())
print(myqueue.pop())
