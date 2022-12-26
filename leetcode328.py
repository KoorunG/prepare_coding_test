# https://leetcode.com/problems/odd-even-linked-list/

# 연결리스트를 홀수번째 노드 다음에 짝수번째 노드가 오도록 재구성하라.
# 공간복잡도 O(1), 시간복잡도 O(n)에 풀이해라.

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def to_linked_list(nums: List[int]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        for n in nums[::-1]:
            node = ListNode(n)
            node.next = prev
            prev = node
        return node

    # 홀수노드와 짝수노드를 동시에 진행시킨 뒤 루프를 모두 돌면 홀수노드와 짝수노드를 연결하는 방식...
    # 왜 이생각을 못했을까.............
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외처리
        if head is None:
            return None
        # 홀수노드를 head로, 짝수노드를 head.next로 초기화하고
        odd = head
        even = head.next
        # 짝수노드의 head를 head.next로 초기화하여 보관해둔다.
        even_head = head.next
        # 짝수노드와 next값이 존재하는 동안 루프를 돈다.
        while even and even.next:
            # 홀수노드와 짝수노드를 두칸씩 건너뛰도록 선언한다.
            odd.next, even.next = odd.next.next, even.next.next
            # (홀수노드와 짝수노드 진행)
            odd, even = odd.next, even.next

        # while 루프를 돌고 난 뒤 odd,next에 even_head를 연결한다.
        odd.next = even_head
        return head


head = [1, 2, 3, 4, 5]
# Output: [1,3,5,2,4]

head2 = [2, 1, 3, 5, 6, 4]
# Output: [2,3,6,7,1,5,4]

sol = Solution()
print(sol.oddEvenList(Solution.to_linked_list(head2)).next.next.next.val)
