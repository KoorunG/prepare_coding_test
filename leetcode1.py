from typing import *


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# nums = [2, 7, 11, 15]
# target = 9
nums = [3, 3]
target = 6
print(twoSum(nums, target))

# 리트코드의 Python3 -> 타입스크립트와 비슷하게 타입을 지정하는 부분이 존재...