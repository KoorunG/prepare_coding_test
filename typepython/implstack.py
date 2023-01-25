# Linked List와 typing을 이용한 스택 구현

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    __slots__ = ("item", "pointer")

    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        cur_node = self.head
        count: int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count


class Stack(Generic[T], LinkedList[T]):
    def push(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def pop(self) -> T:
        if self.head is None:
            raise ValueError("stack is empty")
        else:
            cur_node = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item
        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer
        result = cur_node.pointer
        cur_node.pointer = None
        return result.item


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.head.item)
