# 다음 연산을 제공하는 원형 데크를 디자인하라.

# class ListNode:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# class MyCircularDeque:
#     def __init__(self, k: int):
#         # 이중 연결리스트 선언
#         self.head, self.tail = ListNode(None), ListNode(None)
#         # 입력값 k와 길이 len 초기화
#         self.k, self.len = k, 0
#         # head.right = tail, tail.left = head 이므로 원형으로 연결된 것을 확인
#         self.head.right, self.tail.left = self.tail, self.head
#
#     # 노드를 잇는 private 함수 (이중 연결리스트에서는 이미 있는 노드를 끊고 새 노드를 잇는 방식으로 구현된다.)
#     def _add(self, node: ListNode, new: ListNode):
#         # node.right를 n에 저장
#         n = node.right
#         # 새 노드를 node.right에 매핑
#         node.right = new
#         # 새 노드의 왼쪽 오른쪽을 연결
#         new.left, new.right = node, n
#         # 기존 n에 새 노드 연결
#         n.left = new
#
#     def _del(self, target: ListNode):
#         # front, rear = target.left, target.right
#         # # 기존 노드 찢기
#         # target.left, target.right = ListNode(None), ListNode(None)
#         # # 남아있는 노드 연결
#         # front.right = rear.left
#         n = target.right.right
#         target.right = n
#         n.left = target
#
#     # 앞에 아이템 추가, 추가여부를 bool로 반환
#     def insertFront(self, value: int) -> bool:
#         # len과 k가 같다면 (원형 데크가 꽉차있다면) False 리턴
#         if self.len == self.k:
#             return False
#         # len 길이 1 증가
#         self.len += 1
#         self._add(self.head, ListNode(value))
#         return True
#
#     # 끝에 아이템 추가, 추가여부를 bool로 반환
#     def insertLast(self, value: int) -> bool:
#         # len과 k가 같다면 (원형 데크가 꽉차있다면) False 리턴
#         if self.len == self.k:
#             return False
#         # len 길이 1 증가
#         self.len += 1
#         self._add(self.tail, ListNode(value))
#         return True
#
#     # 앞에 아이템 삭제, 삭제여부를 bool로 반환
#     def deleteFront(self) -> bool:
#         if self.len == 0:
#             return False
#         self.len -= 1
#         self._del(self.head)
#         return True
#
#     # 끝에 아이템 삭제, 삭제여부를 bool로 반환
#     def deleteLast(self) -> bool:
#         if self.len == 0:
#             return False
#         self.len -= 1
#         self._del(self.tail.left.left)
#         return True
#
#     # 앞에서 아이템 탐색, 데크가 비어있으면 -1 리턴
#     def getFront(self) -> int:
#         return self.head.right.value if self.len else -1
#
#     # 뒤에서 아이템 탐색, 데크가 비어있으면 -1 리턴
#     def getRear(self) -> int:
#         return self.tail.left.value if self.len else -1
#
#     # 비어있는지 여부 리턴
#     def isEmpty(self) -> bool:
#         return self.len == 0
#
#     # 꽉 차있는지 여부 리턴
#     def isFull(self) -> bool:
#         return self.len == self.k

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._head = None
        self._tail = None
        self._size = 0
        self._capacity = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self._head = self._tail = ListNode(value)
        elif self.isFull():
            return False
        else:
            new_head = ListNode(value)
            new_head.next = self._head
            self._head.prev = new_head
            self._head = new_head
        self._size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self._head = self._tail = ListNode(value)
        elif self.isFull():
            return False
        else:
            new_tail = ListNode(value)
            self._tail.next = new_tail
            new_tail.prev = self._tail
            self._tail = self._tail.next
        self._size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self._size == 1:
            self._head = None
            self._tail = None
        else:
            temp = self._head.next
            self._head.next = None
            temp.prev = None
            self._head = temp
        self._size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self._size == 1:
            self._head = None
            self._tail = None
        else:
            temp = self._tail.prev
            self._tail.prev = None
            temp.next = None
            self._tail = temp
        self._size -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self._head.val

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self._tail.val

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self._size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._size == self._capacity


mcdq = MyCircularDeque(5)
print(mcdq.insertLast(1))  # return True
print(mcdq.insertLast(2))  # return True
print(mcdq.insertFront(3))  # return True
print(mcdq.insertFront(4))  # return False, the queue is full.
print(mcdq.getRear())  # return 2
print(mcdq.isFull())  # return True
print(mcdq.deleteLast())  # return True
print(mcdq.insertFront(4))  # return True
print(mcdq.getFront())  # return 4
