# https://leetcode.com/problems/array-partition/
# 숫자 배열에서 한 쌍의 min(a, b) 페어를 만들어 이 페어들의 합의 최댓값을 구하여라 (배열의 크기는 2n 이다)

from typing import *

nums = [1, 4, 3, 2]
# 4
nums2 = [6, 2, 6, 5, 1, 2]
# 9


class Solution:
    # 1. 첫 풀이
    def arrayPairSum(self, nums: List[int]) -> int:
        # 정렬
        nums.sort()
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 1:
                continue
            sum += min(nums[i], nums[i + 1])
        return sum

    # 2. 두 번째 풀이 (사실 첫번째 코드와 완전 동일함)
    def arrayPairSum2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


sol = Solution()
print(sol.arrayPairSum2(nums))
print(sol.arrayPairSum2(nums2))
