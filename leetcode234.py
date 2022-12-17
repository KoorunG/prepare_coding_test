# https://leetcode.com/problems/palindrome-linked-list/

# 연결리스트가 펠린드롬 구조인지 판별하여라.

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)  # head


# Output: true

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = list()
        # head가 존재하지 않는 예외사항 -> True
        if not head:
            return True
        # head일 때 node = head로 시작
        node = head
        # node가 None일때까지 (tail일때까지) 반복
        while node is not None:
            q.append(node.val)
            # head가 아니므로 node = node.next
            node = node.next

        if not q == q[::-1]:
            return False
        return True


sol = Solution()
print(sol.isPalindrome(node1))
# sol.isPalindrome(head2)
