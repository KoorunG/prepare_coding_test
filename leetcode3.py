# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 중복문자가 없는 가장 긴 '부분문자열'의 길이를 리턴하라
import collections


class Solution:
    # 1. 슬라이딩 윈도우를 이용한 풀이
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     result = []
    #     for i in range(len(s)):
    #         tmp = []
    #         for z in s[i:]:
    #             if z in tmp:
    #                 break
    #             tmp.append(z)
    #         result.append(len(tmp))
    #     if not result:
    #         return 0
    #     return max(result)

    # # 2. 해시테이블 사용
    # 2. 해시테이블과 슬라이딩 윈도우를 이용한 풀이
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 사용한 문자열의 인덱스를 저장하는 used 딕셔너리 선언
        used = {}
        # 시작점(start)와 최대길이(max_len)을 0으로 초기화
        max_len = start = 0
        # s를 반복을 돌면서 (c : 문자열 내의 문자, i : c의 인덱스)
        for i, c in enumerate(s):
            # 문자열 c가 used 딕셔너리 안에 있고, start가 used안에 있는 인덱스 이하라면
            if c in used and start <= used[c]:
                # start를 그 인덱스 + 1로 초기화
                start = used[c] + 1
            # 아니라면 max_len을 초기화 (기존의 max_len과 새로 선언된 문자열의 길이 중 큰 값으로)
            else:
                max_len = max(max_len, i - start + 1)
            # c의 인덱스를 딕셔너리에 저장
            used[c] = i
        # max_len 리턴
        return max_len


sol = Solution()

s = "pwwkew"
# 3
# Explanation: The answer is "wke", with the length of 3.

s2 = "bbbbb"
# 1

s3 = "abcabcbb"
# 3

# sol.lengthOfLongestSubstring(s)
# sol.lengthOfLongestSubstring(s3)
print(sol.lengthOfLongestSubstring(s))
print(sol.lengthOfLongestSubstring(s2))
print(sol.lengthOfLongestSubstring(s3))
