# https://leetcode.com/problems/reverse-linked-list-ii/

# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.


from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. 내 풀이 : 연결리스트와 노드를 뒤집는 함수를 정의하고 절차지향적으로 풀었다.
# 의외로 성능은 잘나오나 코드량이 매우 많음... 시간도 오래 걸림
class Solution:
    @staticmethod
    def to_linked_list(nums: List[int]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        for n in nums[::-1]:
            node = ListNode(n)
            node.next = prev
            prev = node
        return node

    def reverse_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        node = head
        while node:
            result.append(node.val)
            node = node.next
        result.reverse()
        return self.to_linked_list(result)


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 두 수가 같으면 Head 리턴
        if left == right:
            return head

        # node_left, node_right 선언
        node_left = node_right = head
        # prev_node_left : node_left의 prev노드
        # next_node_right : node_right의 next노드
        prev_node_left: Optional[ListNode] = None
        next_node_right: Optional[ListNode] = None

        # 반복을 돌며 위에서 선언한 값 매핑
        for i in range(1, left):
            prev_node_left = node_left
            node_left = node_left.next
        for i in range(1, right):
            node_right = node_right.next
            next_node_right = node_right.next

        # 노드 끊기
        node_right.next = None
        # 노드 뒤집기
        reverse_node = self.reverse_node(node_left)

        # 1. prev_node_left 이 None일 경우
        if prev_node_left is None:
            head = prev_node_left = reverse_node
        # 2. 아닐경우 노드 잇기
        else:
            prev_node_left.next = reverse_node

        while prev_node_left and prev_node_left.next:
            prev_node_left = prev_node_left.next
        prev_node_left.next = next_node_right
        return head


head = [1, 2, 3, 4, 5]
left = 2
right = 4
# Output: [1,4,3,2,5]


head2 = [5]
left2 = 1
right2 = 1
# Output: [5]

head3 = [1, 2, 3]
left3 = 1
right3 = 2

sol = Solution()
node1 = Solution.to_linked_list(head3)
print(sol.reverseBetween(node1, left3, right3).next.next.val)