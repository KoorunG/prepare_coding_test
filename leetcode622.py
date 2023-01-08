# https://leetcode.com/problems/design-circular-queue/
# 원형큐를 디자인하라
import collections


# 원형 큐이긴 하나 isFull일때 rear과 front의 연결 여부를 나타내는 operation 구현 여부가 명시되어있지 않기 때문에 쉽게 풀이함
class MyCircularQueue:

    def __init__(self, k: int):
        self.deque = collections.deque()
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[len(self.deque) - 1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) >= self.size


mcq = MyCircularQueue(3)
print(mcq.enQueue(1))
print(mcq.enQueue(2))
print(mcq.enQueue(3))
print(mcq.enQueue(4))
print(mcq.Rear())
print(mcq.isFull())
print(mcq.deQueue())
print(mcq.enQueue(4))
print(mcq.Rear())
