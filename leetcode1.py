from typing import *


# 배열에서 덧셈하여 타겟을 얻을 수 있는 두 수의 인덱스를 리턴하라.

# 1. 첫 번째 풀이 : 브루트포스를 이용하여 모든 경우를 탐색
# 시간복잡도는 전체 탐색을 이중으로 하기 때문에 O(n^2)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9

nums2 = [3, 3]
target2 = 6

nums3 = [3, 2, 4]
target3 = 6


# 2. enumerate를 이용
# in 역시 시간복잡도가 O(n)이기 때문에 전체 시간복잡도 : O(n^2)
# 그러나 상수항이 브루트포스에 비해 훨씬 작다 (가볍다)
def twoSum2(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        if target - num in nums[i:]:
            sub_index = nums.index(target - num)
            if i != sub_index:
                return [i, sub_index]


# 3. dict를 이용하여 enumerate의 key, value를 뒤집은 경우를 만들어 비교
# in 탐색을 하고 O(1)인 딕셔너리를 이용하기 때문에 전체 시간복잡도는 O(n)이 된다!
def twoSum3(nums: List[int], target: int) -> List[int]:
    nums_dict = dict()
    # key : 값, value : 인덱스
    for i, num in enumerate(nums):
        nums_dict[num] = i

    # 딕셔너리에서 타겟 - num을 키값으로 가지고 있는 경우 필터링!
    for i, num in enumerate(nums):
        if target - num in nums_dict and i != nums_dict[target - num]:
            return [i, nums_dict[target - num]]


# 3_1. 리팩토링으로 for문을 하나로 합침
# for문에서 key, value를 뒤집은 딕셔너리를 탐색하면서 만약 target - num이 딕셔너리 안에 있으면 리턴하고
# 없으면 딕셔너리에 값을 추가한다.
def twoSum3_1(nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    # key : 값, value : 인덱스
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return [i, nums_dict[target - num]]
        nums_dict[num] = i



# 4. 투 포인터 이용 (단, 리스트가 정렬된 경우에만 사용가능)
def twoSum4(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


# print(twoSum(nums, target))
# print(twoSum(nums2, target2))

# print(twoSum2(nums, target))
# print(twoSum2(nums2, target2))
# print(twoSum2(nums3, target3))

# print(twoSum3(nums, target))
# print(twoSum3(nums2, target2))
# print(twoSum3(nums3, target3))

print(twoSum3_1(nums, target))
print(twoSum3_1(nums2, target2))
print(twoSum3_1(nums3, target3))

# print(twoSum4(nums, target))
# print(twoSum4(nums2, target2))
# print(twoSum4(nums3, target3))
# 리트코드의 Python3 -> 타입스크립트와 비슷하게 타입을 지정하는 부분이 존재...
