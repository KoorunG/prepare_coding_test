# Linked List와 typing을 이용한 스택 구현

from typing import Optional, Generic, TypeVar

T = TypeVar("T")


# 노드 정의
class Node(Generic[T]):
    def __init__(self, item: T, pointer: Optional["Node[T]"] = None):
        self.item = item
        self.pointer = pointer


# 연결리스트 정의
class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        # head가 존재하지 않는다면 길이는 0
        if self.head is None:
            return 0
        cur_node: Node[T] = self.head
        count: int = 1
        while cur_node.pointer:
            cur_node = cur_node.pointer
            count += 1
        return count

    # 연결리스트의 __str__ 선언
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


# 스택 정의
class Stack(Generic[T], LinkedList[T]):

    def push(self, item: T):
        new_node: Node[T] = Node(item=item)

        # head가 존재하지 않는다면 new_node를 self.head로 지정
        if self.head is None:
            self.head = new_node
            return

        cur_node: Node[T] = self.head

        # 노드 이동
        while cur_node.pointer:
            cur_node = cur_node.pointer
        # 마지막까지 왔다면 new_node를 cur_node.pointer으로 지정
        cur_node.pointer = new_node

    def pop(self) -> T:
        # self.head가 존재하지 않으면 (노드가 없으면) raise ValueError
        if not self.head:
            raise ValueError("stack is empty")
        # 아니라면 cur_node를 self.head로 초기화한다
        else:
            cur_node: Node[T] = self.head
        # 다음노드가 존재하지 않으면 self.head를 None으로 초기화하고 cur_node.item을 리턴한다. - 1
        if not cur_node.pointer:
            self.head = None
            return cur_node.item
        # 다음노드가 존재하고, 다음노드의 다음노드가 존재하면
        while cur_node.pointer.pointer:
            # 노드를 진행시킨다.
            cur_node = cur_node.pointer
        # cur_node.pointer를 result에 저장하고
        result = cur_node.pointer
        # cur_node.pointer를 None으로 만든 뒤
        cur_node.pointer = None
        # result.item을 리턴하면 pop을 구현하는 것이 된다.
        return result.item


# 유닛테스트 시 사용
if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(12)

    print(stack.head.item)
    print(stack.length)
    stack.push(13)

    print(stack.head.pointer.item)
    print(stack.length)
    stack.push(13)
    stack.push(14)
    stack.push(15)

    print(stack)

    stack.pop()

    print(stack)
