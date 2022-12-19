# https://leetcode.com/problems/add-two-numbers/
import functools
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
        # new_q1 = [str(n) for n in q1[::-1]]
        # new_q2 = [str(n) for n in q2[::-1]]
        # new_q1 = map(str, q1[::-1])
        # new_q2 = map(str, q2[::-1])
        # result = []
        # for d in str(int("".join(new_q1)) + int("".join(new_q2))):

        # functools.reduce() 를 이용하여 간단하게 자릿수를 이은 int값으로 변환
        result = []
        num1 = functools.reduce(lambda x, y: 10 * x + y, q1[::-1], 0)
        num2 = functools.reduce(lambda x, y: 10 * x + y, q2[::-1], 0)

        for d in str(num1 + num2):
            result.append(int(d))
        return self.make_node(result[::-1])

    # 2. 전가산기 구현을 이용 (교재 풀이)
    # 전가산기, 논리회로에 관한 지식이 부족하기 때문에 추가적인 공부 필요...
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # root = head의 복사본
        root = head = ListNode(0)

        # carry = 자리올림수
        carry = 0
        # 입력값이나 자리올림수가 존재하는 동안 반복
        while l1 or l2 or carry:
            sum = 0
            # sum에 노드의 값을 합산한 후 다음으로 진행
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            # sum + carry를 10으로 나눠 다음 (자리올림수, 값) 튜플 리턴
            carry, val = divmod(sum + carry, 10)
            # 문제에서 원하는 값은 Linked List의 역순의 head이므로 다음과 같이 설정
            head.next = ListNode(val)
            head = head.next
        # head의 복사본 root의 next 리턴
        return root.next


sol = Solution()
node1 = sol.make_node([2, 4, 3])
node2 = sol.make_node([5, 6, 4])
print(sol.addTwoNumbers(node1, node2).val)
print(sol.addTwoNumbers2(node1, node2).val)
