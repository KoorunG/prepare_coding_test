# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 한번의 거래로 낼 수 있는 최대 이익을 산출하여라
# 예를들어 [7, 1, 5, 3, 6, 4] 의 경우 1에 사서 6에 팔면 최대 이익 5가 남고
# [7, 6, 4, 3, 1]의 경우 가격이 항상 낮아지기 때문에 최대 이익은 0이다
import collections
import sys
from typing import *

prices = [7, 1, 5, 3, 6, 4]
# Output: 5

prices2 = [7, 6, 4, 3, 1]
# Output: 0

prices3 = [1, 2, 4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        distance = 0  # 최댓값과 최솟값의 차이 : 0으로 초기화
        min_price = sys.maxsize  # 최솟값 : 시스템의 가장 큰 값

        # 리스트를 순회하면서 distance를 갱신하는 것이 목적
        # 최솟값은 min_price에서 계속 갱신되며, distance는 현재 price와 min_price의 차이로 갱신되기 때문에
        # 최대 거리를 도출할 수 있다!
        for price in prices:
            min_price = min(min_price, price)  # 최솟값 갱신
            distance = max(distance, price - min_price)
        return distance


sol = Solution()
print(sol.maxProfit(prices))
print(sol.maxProfit(prices2))
print(sol.maxProfit(prices3))