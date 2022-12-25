# https://leetcode.com/problems/swap-nodes-in-pairs/

# 연결리스트를 입력받아 페어 단위로 스왑하라.

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 리스트를 입력받아 연결리스트 만들기

class Solution:
    @staticmethod
    def to_linked_list(num_list: List[int]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        for n in num_list[::-1]:
            node = ListNode(n)
            node.next = prev
            prev = node
        return node
    #
    # @staticmethod
    # def to_list(head: Optional[ListNode]) -> List[int]:
    #     node = head
    #     result = []
    #     while node:
    #         result.append(node.val)
    #         node = node.next
    #     return result
    #
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     node = head
    #     num_list = self.to_list(node)
    #     if len(num_list) <= 1:
    #         return node
    #
    #     # 홀수일경우 홀수 직전까지만 반복 돌리기
    #     limit = len(num_list)
    #     if len(num_list) % 2 == 1:
    #         limit = len(num_list) - 1
    #
    #     # 리스트의 값만 교체
    #     for n in range(len(num_list[:limit])):
    #         if n % 2 == 0:
    #             num_list[n + 1], num_list[n] = num_list[n], num_list[n + 1]
    #
    #     return self.to_linked_list(num_list)

    # 2. 각 노드의 val만 교체하는 방법
    # 매우 간단하며 성능도 제일 잘나오나, 이렇게 val만 교체할 수 있는 경우는 의도에 벗어난다. (의도 = "노드" 자체를 스왑하는 것)
    # def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     node = head
    #     # node와 node.next가 있는 동안만 반복
    #     while node and node.next:
    #         node.val, node.next.val = node.next.val, node.val
    #         node = node.next.next
    #     # head 리턴
    #     return head

    # 3. 재귀를 이용한 방법
    def swapPairs3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            # 백트래킹으로 연결리스트 엮기
            p = head.next
            head.next = self.swapPairs3(p.next)
            # 노드 스왑
            p.next = head
            # return p로 재귀함수의 리턴값을 현재 포인터로 설정
            return p
        # 탐색과 스왑이 끝난 후 head 리턴
        return head


head = [1, 2, 3]
# Output: [2,1,4,3]

head2 = []
# Output: []

sol = Solution()
node1 = sol.to_linked_list(head)
print(sol.swapPairs2(node1).val)