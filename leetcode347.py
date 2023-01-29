# https://leetcode.com/problems/top-k-frequent-elements/
import collections
from typing import List

class Solution:

    # 1. 파이썬의 Counter를 이용한 풀이
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [s[0] for s in counter.most_common(k)]


nums = [1, 1, 1, 2, 2, 3]
k = 2

nums2 = [1]
k2 = 1

nums3 = [1, 2]
k3 = 2

sol = Solution()
print(sol.topKFrequent(nums, k))