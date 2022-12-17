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

    # 런너를 이용한 풀이 (익혀두자)
    # 빠른 런너와 느린 런너 두가지를 만든다 (빠른런너의 이동속도가 두배 빠르게 설정)
    # 빠른런너가 끝 지점에 도달하는 순간 느린 런너는 정확히 중간 지점에 도달하고
    # 느린 런너가 여태 이동했던 자취를 역순으로 만든 뒤 끝지점까지 도달하면서 펠린드롬인지 검사한다.
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        if not head:
            return True

        # fast와 fast.next의 값이 존재하는 동안 반복
        while fast and fast.next:
            fast = fast.next.next
            # rev : 역순으로 이어붙일 연결리스트
            # 따라서 rev.next = rev로 초기화한다
            rev, rev.next, slow = slow, rev, slow.next
        # fast가 아직 존재하는 경우 (연결리스트가 홀수여서 위에서 마무리가 되지 않은 경우)
        # slow를 한칸 더 옮겨준다.
        if fast:
            slow = slow.next

        # rev.val == slow.val인동안 반복실행
        while rev and rev.val == slow.val:
            # rev를 풀어가면서 비교
            slow, rev = slow.next, rev.next
        # 펠린드롬이라면 slow와 rev가 None이 될때까지 이동한다.
        return not rev



sol = Solution()
print(sol.isPalindrome(node1))
print(sol.isPalindrome2(node1))
