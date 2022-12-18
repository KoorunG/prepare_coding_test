# https://leetcode.com/problems/reverse-linked-list/

# 연결 리스트를 뒤집어라

from typing import *


# 연결리스트 선언
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 리스트를 받아서 연결리스트의 헤드를 리턴하는 함수
def make_node(num_list: List[int]) -> Optional[ListNode]:
    node_next = None
    while num_list:
        node_val = num_list.pop()
        node = ListNode(node_val, node_next)
        node_next = node
        if len(num_list) == 0:
            return node


class Solution:
    # 1. 내 풀이 : 위에서 리스트를 받아 연결리스트의 헤드를 리턴하는 함수를 재활용함
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = []
        node = head
        while node:
            q.append(node.val)
            node = node.next
        # 배열을 뒤집은 뒤 make_node 함수에 전달
        r = q[::-1]
        return make_node(r)

    # 재귀를 이용한 풀이
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 다음 노드 next, 현재 노드 node를 파라미터로 받는 함수를 계속해서 재귀호출
        #
        def reverse(node: Optional[ListNode], prev: Optional[ListNode] = None):
            # node == None일 경우 리턴 (뒤집힌 연결리스트의 첫번째 노드)
            if not node:
                return prev
            # 재귀호출
            # node.next에는 이전 prev 리스트를 게속 연결해주면서 node == None이 될 때 까지 재귀호출한다.
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    # 반복을 이용한 풀이
    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            # prev : 역순 연결리스트
            # node : 현재 연결리스트
            # next : 현재 연결리스트의 next값
            next, node.next = node.next, prev
            prev, node = node, next
        # 역순인 prev의 첫번째값 -> 뒤집은 연결리스트의 헤드
        return prev


num_list = [1, 2, 3, 4, 5]
node_head = make_node(num_list)

sol = Solution()
print(sol.reverseList(node_head).val)
print(sol.reverseList2(node_head).val)
print(sol.reverseList3(node_head).val)
# sol.reverseList(sol.reverseList(node_head))
# print(node_head.val)
