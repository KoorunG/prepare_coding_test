# Linked List와 typing을 이용한 큐 구현

from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T, pointer: Optional["Node[T]"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if not self.head:
            return 0
        cur_node: Node[T] = self.head
        count: int = 1
        while cur_node.pointer:
            cur_node = cur_node.pointer
            count += 1
        return count

    def __str__(self) -> str:
        result: str = ""
        if not self.head:
            return result
        cur_node: Node[T] = self.head
        result += f"Node({cur_node.item})"
        while cur_node.pointer:
            cur_node = cur_node.pointer
            result += f" -> Node({cur_node.item})"
        return result


class Queue(Generic[T], LinkedList[T]):
    def enqueue(self, item: T) -> None:
        new_node: Node[T] = Node(item=item)
        if not self.head:
            self.head = new_node
            return
        cur_node: Node[T] = self.head
        while cur_node.pointer:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def dequeue(self) -> T:
        if not self.head:
            raise ValueError("queue is empty")
        cur_node: Node[T] = self.head
        if not cur_node.pointer:
            self.head = None
            return cur_node.item
        self.head = cur_node.pointer
        return cur_node.item


# Java의 pulbic static void main(String[] args) 와 비슷한 개념...?
if __name__ == "__main__":
    queue = Queue[int]()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue)

    print(queue.dequeue())
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(queue.dequeue())
    print(queue)
