# https://leetcode.com/problems/valid-palindrome/
# 주어진 문자열이 펠린드롬인지 확인하여라 (대소문자를 구분하지 않고 영문자, 숫자만을 대상으로 함)


from typing import *


# 1. 내가 푼 풀이
def palindrome(arg: str) -> bool:
    # original과 compare 문자열 초기화
    original = ""
    compare = ""
    for c in arg:
        # alpha & number 필터링
        if c.isalnum():
            # 문자열 구성
            original = c.lower() + original
            compare = compare + c.lower()
    # 리턴
    return original == compare


case1 = "A man, a plan, a canal: Panama"
case2 = "race a car"
case3 = " "

print(palindrome(case1), palindrome(case2), palindrome(case3))

import collections


# 2. 데크 자료형 이용
def palindrome2(arg: str) -> bool:
    strs: Deque = collections.deque()
    for c in arg:
        if c.isalnum():
            strs.append(c.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

-0
print(palindrome2(case1), palindrome2(case2), palindrome2(case3))


import re


# 3. 정규식과 슬라이싱 이용
def palindrome3(arg: str) -> bool:
    arg = arg.lower()
    s = re.sub('[^0-9a-z]', '', arg)    # re.sub(정규표현식, 치환문자, 대상문자열)
                                        # -> 알파벳이나 숫자가 아닌경우 문자 제거

    return s == s[::-1]                 # [::-1] : 리스트를 뒤집는 방법


print(palindrome3(case1), palindrome3(case2), palindrome3(case3))