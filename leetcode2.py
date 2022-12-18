# https://leetcode.com/problems/add-two-numbers/

# 두 개의 비어있지 않은 연결리스트가 주어진다. 각 연결리스트에는 숫자가 하니씩 들어있으며 연결리스트의 역순으로 숫자를 구성할 수 있다.
# 두 숫자의 합을 계산한 뒤 역시 역순으로된 연결리스트의 head를 반환하여라

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def make_node(self, num_list: List[int]) -> Optional[ListNode]:
        node_next = None
        while num_list:
            node_val = num_list.pop()
            node = ListNode(node_val, node_next)
            node_next = node
            if len(num_list) == 0:
                return node

    # 1. 내 풀이
    # 각 노드를 받아 리스트에 저장한 뒤 형변환을 통해 문제에 주어진 대로 계산을 하고
    # 다시 연결리스트를 만들어 make_node() 함수를 이용한 값을 리턴
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q1 = []
        q2 = []
        while l1:
            q1.append(l1.val)
            l1 = l1.next
        while l2:
            q2.append(l2.val)
            l2 = l2.next
        new_q1 = [str(n) for n in q1[::-1]]
        new_q2 = [str(n) for n in q2[::-1]]
        result = []
        for d in str(int("".join(new_q1)) + int("".join(new_q2))):
            result.append(int(d))
        return self.make_node(result[::-1])


sol = Solution()
node1 = sol.make_node([2, 4, 3])
node2 = sol.make_node([5, 6, 4])
print(sol.addTwoNumbers(node1, node2).val)
