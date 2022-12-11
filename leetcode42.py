# https://leetcode.com/problems/trapping-rain-water/

# 높이를 입력받아 비가 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

from typing import *


# 1. 내 풀이 : left, right, max를 설정
def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_height = max(height)
    result = 0

    # left -> max
    left_max = 0
    while left <= height.index(max_height):
        # 좌상한보다 현재 포인터가 가리키는 높이가 높을 경우 좌상한 재설정
        if left_max < height[left]:
            left_max = height[left]
        # 좌상한이 더 높을 경우 sum에 값 누적
        else:
            result += left_max - height[left]
        # 포인터 이동
        left += 1
    # max <- right의 경우 위와 동일
    right_max = 0
    while height.index(max_height) <= right:
        if right_max < height[right]:
            right_max = height[right]
        else:
            result += right_max - height[right]
        right -= 1
    return result


# 2. 스택을 이용한 풀이 : 현재 높이가 이전의 높이보다 높을 경우, 변곡점을 기준으로 격차만큼 물 높이를 채우는 방식
def trap2(height: List[int]) -> int:
    # stack과 volume 선언
    stack = []
    volume = 0

    # 배열을 돌면서 스택에 인덱스를 쌓음
    # 현재 포인터의 높이가 스택의 가장 윗부분의 경우보다 크다면 스택에서 그 값을 뽑아서 top으로 정함
    # 스택에 값이 비어있는 경우 반복문을 빠져나온다.
    # 그렇지 않은 경우는 distance와 waters를 곱한 값을 volume에 누적시킨다.
    # (정말 난해하기 때문에 다시 한번 찾아볼 필요...)
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
        stack.append(i)
    return volume


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
print(trap2(height))
# expected : 6

height2 = [4, 2, 0, 3, 2, 5]
print(trap(height2))
print(trap2(height2))
# expected : 9
