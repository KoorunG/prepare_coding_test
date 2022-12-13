# https://leetcode.com/problems/3sum/
import collections
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
# (세 수의 순서는 상관없음)

from typing import *

nums = [-1, 0, 1, 2, -1, -4]
# [[-1,-1,2],[-1,0,1]]

nums2 = [0, 1, 1]
# []

nums3 = [0, 0, 0]

nums4 = [-2, 0, 1, 1, 2]

nums5 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]

nums6 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]


# 1. 세 수는 인덱스가 같으면 안된다.
# 2. 세 수의 합은 0이어야 한다.
class Solution:
    # a. 초기 내 풀이 -> 실패
    # 투 포인터를 양 끝단에 설정하고 for문을 가운데에서 돌게끔 했는데 필터링하지 못한 일부 경우가 발생한듯
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     # 예외사항 필터링
    #     if len(nums) == 3 and sum(nums) == 0:
    #         return [nums]
    #     if len(nums) == 3 and sum(nums) != 0:
    #         return []
    #
    #     # 정렬
    #     nums.sort()
    #     print(nums)  # [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    #     # left, right 설정
    #     left, right = 0, len(nums) - 1
    #     left2, right2 = 0, len(nums) - 1
    #     arr = []
    #     # case1. 양 끝단의 합이 0보다 클 경우 right를 왼쪽으로 한칸 옮김
    #     while left <= right:
    #         for num in nums[left + 1: right]:  # num은 left + 1과 right를 순회한다.
    #             if nums[left] + num + nums[right] == 0:  # 세 수의 합이 0이면 append
    #                 arr.append([nums[left], num, nums[right]])
    #         if nums[left] + nums[right] < 0:  # 양 끝단의 합이 0보다 작을 경우 left를 오른쪽으로 한칸 옮김
    #             left += 1
    #         elif nums[left] + nums[right] >= 0:
    #             right -= 1
    #
    #     # case2. 양 끝단의 합이 0보다 클 경우 left를 오른쪽으로 한칸 옮김
    #     while left2 <= right2:
    #         for num in nums[left2 + 1: right2]:  # num은 left2 + 1과 right2를 순회한다.
    #             if nums[left2] + num + nums[right2] == 0:  # 세 수의 합이 0이면 append
    #                 arr.append([nums[left2], num, nums[right2]])
    #         if nums[left2] + nums[right2] <= 0:  # 양 끝단의 합이 0보다 작을 경우 left2를 오른쪽으로 한칸 옮김
    #             left2 += 1
    #         elif nums[left2] + nums[right2] > 0:
    #             right2 -= 1
    #
    #     # 두 경우를 모두 더한 뒤 중복제거
    #     result = []
    #     for r in arr:
    #         if r not in result:
    #             result.append(r)
    #     return result

    # b. 교재 풀이 (지만 나중에나도 이렇게 풀긴 함)
    # 배열을 돌면서 i의 앞에서 left를 선언하고 배열의 끝을 right로 선언하는 투 포인터 적용, 최소 3개의 수를 뽑을 수 있도록 n-2 까지 순회
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 예외사항 필터링 (딱히 드라마틱한 효과는 없다)
        # if len(nums) == 3 and sum(nums) == 0:
        #     return [nums]
        # if len(nums) == 3 and sum(nums) != 0:
        #     return []
        arr = []
        # 배열 정렬 (팀소트)
        nums.sort()
        # for문 돌기
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:  # O(n^2)
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    arr.append([nums[i], nums[left], nums[right]])
                    # 숫자가 같은경우가 나열된다면 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1
        result = []
        # 중복제거 (O(n))
        for r in arr:
            if r not in result:
                result.append(r)
        return result


sol = Solution()
print(sol.threeSum(nums))
print(sol.threeSum(nums2))
print(sol.threeSum(nums3))
print(sol.threeSum(nums4))
print(sol.threeSum(nums5))
print(sol.threeSum(nums6))
