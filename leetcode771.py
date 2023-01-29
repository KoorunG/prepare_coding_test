# https://leetcode.com/problems/jewels-and-stones/
import collections

# J는 보석이며 S는 가지고 있는 돌이다. S에는 보석이 몇개나 있을까? (대소문자는 구분한다.)

jewels = "aA"
stones = "aAAbbbb"
# Output: 3

jewels2 = "z"
stones2 = "ZZ"
# Output: 0



class Solution:
    # 1. set을 이용한 풀이
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     count = 0
    #     keys = set()
    #     for jewel in jewels:
    #         keys.add(jewel)
    #     for stone in stones:
    #         if stone in keys:
    #             count += 1
    #     return count

    # 2. sum()과 Counter를 이용한 파이써닉한 풀이
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     return sum(collections.Counter([stone for stone in stones if stone in jewels[:]]).values())

    # 3. 해시테이블을 이용한 풀이
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        int_dict = collections.defaultdict(int)
        count = 0
        for stone in stones:
            int_dict[stone] += 1

        for jewel in jewels:
            count += int_dict[jewel]
        return count


sol = Solution()
print(sol.numJewelsInStones(jewels, stones))