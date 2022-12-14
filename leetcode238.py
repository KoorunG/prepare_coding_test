# https://leetcode.com/problems/product-of-array-except-self/
# 배열을 입력받아 ouput[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 나오도록 출력하여라
# "You must write an algorithm that runs in O(n) time and without using the division operation."    => O(n)에 풀어야함
import collections
from typing import *

nums = [1, 2, 3, 4]
# [24,12,8,6]

nums2 = [-1, 1, 0, -3, 3]


# [0, 0, 9, 0, 0]


class Solution:
    # 1. 첫 풀이 : 타임아웃 (요구사항이 O(n)에 푸는 것이었음)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_dict = collections.defaultdict(list)
        for i in range(len(nums)):
            num_dict[i] = [nums[j] for j in range(len(nums)) if i != j]

        result = []
        for num_list in num_dict.values():
            mul = 1
            for num in num_list:
                if num == 0:
                    mul = 0
                mul *= num
            result.append(mul)
        return result
    # 2. 투 포인터 활용 : 여전히 O(n^2)이므로 타임아웃
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        result = []
        # 이것만으로 O(n)
        for i in range(len(nums)):
            mul_left, mul_right = 1, 1
            left, right = i - 1, i + 1
            while left >= 0:
                mul_left *= nums[left]
                left -= 1
            while right <= len(nums) - 1:
                mul_right *= nums[right]
                right += 1

            result.append(mul_left * mul_right)
        return result
    # 3. 교재 풀이 : 초기 리턴용 리스트 result에 값을 누적시키는 방향으로 O(n)을 달성함
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        # 결과를 담기 위한 공간
        result = []
        # 왼쪽 곱셈
        # 초기값 1
        mul = 1
        # 왼쪽에서부터 끝까지 값을 곱해나간 값을 result에 append한다. (초기값 1)
        for i in range(0, len(nums)):
            result.append(mul)
            mul *= nums[i]
        # 오른쪽 곱셈
        # mul을 다시 초기화하고
        mul = 1
        # 리스트를 역순으로 순회한다.
        # 여기서 각 result[i]에 mul을 곱하면서
        # mul은 본래 nums[i]를 곱해나간다.
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= mul
            mul *= nums[i]
        return result


sol = Solution()
print(sol.productExceptSelf3(nums))
print(sol.productExceptSelf3(nums2))
