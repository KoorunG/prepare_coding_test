# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
import sys

# 주식의 가격이 명시된 배열이 주어졌을 때 최대 수익금을 리턴하여라
# 주식은 언제든 사고 파는 것이 가능하다
# 예를들어 prices = [7,1,5,3,6,4] 가 주어지면,
# 2일차에 1원에 사고 3일차에 5원에 팔아 4원을 이득보고
# 4일차에 3원에 사고 5일차에 6원에 팔아 3원을 이득봐서 총 7원이 최대 수익금이 된다.


prices = [7, 1, 5, 3, 6, 4]  # 7
prices2 = [1, 2, 3, 4, 5]  # 4
prices3 = [7, 6, 4, 3, 1]  # 0
prices4 = [2, 4, 1]
from typing import *

# 엄청 파이써닉한 방법..
def maxProfit(prices: List[int]) -> int:
    # 리스트를 순회하면서 선택한 값보다 바로 앞의 값이 큰 경우에만 두 차이의 sum을 구한다.
    # 굳이 변곡점만 따질 이유가 없음...!
    return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] > prices[i])


print(maxProfit(prices))
print(maxProfit(prices2))
print(maxProfit(prices3))
print(maxProfit(prices4))
