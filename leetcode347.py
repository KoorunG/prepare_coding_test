# https://leetcode.com/problems/top-k-frequent-elements/
import collections
import heapq
from typing import List

class Solution:

    # 1. 파이썬의 Counter를 이용한 풀이
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     return [s[0] for s in collections.Counter(nums).most_common(k)]

    # 2. 우선순위 큐를 이용한 풀이
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        # 힙에 삽입
        for s in counter:
            heapq.heappush(heap, (-counter[s], s))
        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(heap)[1])
        return topk

nums = [1, 1, 1, 2, 2, 3]
k = 2

nums2 = [1]
k2 = 1

nums3 = [1, 2]
k3 = 2

sol = Solution()
print(sol.topKFrequent(nums, k))