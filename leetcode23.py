import heapq
import queue
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # int 리스트를 연결리스트로 리턴하는 편의함수
    @staticmethod
    def to_linked_list(list: List[int]) -> Optional[ListNode]:
        node: Optional[ListNode] = None
        prev: Optional[ListNode] = None
        for n in list[::-1]:
            node = ListNode(n)
            node.next = prev
            prev = node
        return node

    @staticmethod
    def to_list(head: Optional[ListNode]) -> List[int]:
        list = []
        node = head
        while node:
            list.append(node.val)
            node = node.next
        return list

    # K개의 연결리스트를 병합하는 함수
    # 내 풀이 : to_list, to_linked_list 함수를 만들어 입력받은 연결리스트를 재조합하여 조건에 맞는 연결리스트 리턴
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     result = []
    #     # 1. 입력받기
    #     for linked in lists:
    #         # 2. 리스트로 만들기
    #         list = self.to_list(linked)
    #         for n in list:
    #             result.append(n)
    #     # 3. 병합 후 정렬된 값을 다시 연결리스트로 만들어 리턴하기
    #     return self.to_linked_list(sorted(result))

    # 우선순위큐를 이용한 풀이
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # 각 연결리스트의 루트를 힙에 저장
        for i, linked in enumerate(lists):
            if linked:
                heapq.heappush(heap, (linked.val, i, linked))

        # 힙 추출 이후 다음 노드 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

sol = Solution()
linkeds = []
for list in lists:
    linkeds.append(sol.to_linked_list(list))

print(sol.to_list(sol.mergeKLists(linkeds)))