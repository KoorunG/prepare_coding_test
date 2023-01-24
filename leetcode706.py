# https://leetcode.com/problems/design-hashmap/
import collections


# 다음의 기능을 제공하는 해시맵을 디자인하라. (편의상 key, value는 모두 int로 한다)

# 1. put(key, value) : 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
# 2. get(key) : 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
# 3. remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제한다.


# 개별 체이닝 방식으로 구현!
class ListNode:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # key와 size의 모듈로 연산의 결과를 index로 선언
    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = hash(key)

        # 1. 해당 인덱스에 값이 존재하지 않는 경우 (defaultdict의 특성으로 인해 존재하지 않는 인덱스로 조회할 경우 디폴트 객체를 생성하므로 이렇게 처리)
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # hashTable의 ListNode 선언
        hash_node = self.table[index]

        # 2. 해당 인덱스에 값이 존재하는 경우
        while hash_node:
            # 2-1. 이미 키가 존재하는 경우 value를 업데이트
            if hash_node.key == key:
                hash_node.value = value
                return
            # 2-2. hash_node.next가 None일때 까지 반복을 돌려 개별 체이닝을 잇는다.
            if hash_node.next is None:
                break
            hash_node = hash_node.next

    def get(self, key: int) -> int:
        index = hash(key)

        if self.table[index].value is None:
            return -1

        hash_node = self.table[index]
        while hash_node:
            if hash_node.key == key:
                return hash_node.value
            hash_node = hash_node.next
        return -1

    def remove(self, key: int) -> None:
        index = hash(key)

        if self.table[index].value is None:
            return

        hash_node = self.table[index]
        # 인덱스의 첫번째 노드일때 삭제
        if hash_node.key == key:
            # 연결리스트의 다음값이 존재하지 않을 경우 ListNode()로 초기화, 아닐경우 연결리스트의 다음값으로 초기화 (삼항연산자)
            self.table[index] = ListNode() if hash_node.next is None else hash_node.next
            return

        # 연결리스트의 노드 삭제
        prev = hash_node
        while hash_node:
            if hash_node.key == key:
                prev.next = hash_node.next
                return
            prev, hash_node = hash_node, hash_node.next


mhm = MyHashMap()
mhm.put(1, 1)
mhm.put(2, 2)
print(mhm.get(1))
print(mhm.get(3))
mhm.put(2, 1)
print(mhm.get(2))
mhm.remove(2)
print(mhm.get(2))
