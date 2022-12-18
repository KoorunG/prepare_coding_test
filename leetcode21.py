# https://leetcode.com/problems/merge-two-sorted-lists/
import collections
# 두 개의 "정렬된" 연결 리스트 list1, list2가 주어진다.
# 정렬되어 있는 두 연결 리스트를 합친 결과를 반환하여라

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    #1. 내 풀이
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []

        # 예외사항 필터링
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        # list1, list2의 값을 꺼내서 result에 담기
        while list1:
            result.append(list1.val)
            list1 = list1.next

        while list2:
            result.append(list2.val)
            list2 = list2.next

        # result 정렬
        result.sort()

        # tail 생성
        tail = ListNode(result.pop(), None)
        node_next = None

        # 리스트를 순회하면서 연결리스트(ListNode) 만들기
        while len(result) > 0:
            # node_next = None이면 node_next = tail로 지정
            if not node_next:
                node_next = tail
            # node를 만든 뒤 node_next 지정
            node = ListNode(result.pop(), node_next)
            node_next = node
            # 배열을 모두 순회했으면 노드 리턴
            if len(result) == 0:
                return node

    # 2. 재귀호출
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1, list2의 val을 비교하며 자리바꾸기
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        # 재귀호출
        if list1:
            list1.next = self.mergeTwoLists2(list1.next, list2)
        return list1

sol = Solution()

node_1_3 = ListNode(4)
node_1_2 = ListNode(2, node_1_3)
node_1_head = ListNode(1, node_1_2)

node_2_3 = ListNode(4)
node_2_2 = ListNode(3, node_2_3)
node_2_head = ListNode(1, node_2_2)

print(sol.mergeTwoLists(node_1_head, node_2_head).val)