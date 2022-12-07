# https://leetcode.com/problems/group-anagrams/
import collections
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

from typing import *


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # 디폴트 키값이 존재하는 dict를 만든 뒤
    anagrams = collections.defaultdict(list)
    for str in strs:
        # 1. str 쪼갠뒤 정렬하여 배열만들기
        char_list: List[str] = [sorted_word for sorted_word in sorted(str)]
        # 2. key 만들기 -> 빈 문자열에 iterable한 값을 join하면 리스트 내의 문자열을 연결할 수 있다.
        key = "".join(char_list)
        # 3. defaultdict에 값 추가하기
        anagrams[key].append(str)
    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]

strs2 = [""]
# [[""]]

print(groupAnagrams(strs))
print(groupAnagrams(strs2))
