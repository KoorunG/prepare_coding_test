# https://leetcode.com/problems/reverse-string/
import collections
# 문자열을 뒤집는 함수를 작성하라 입력값은 문자배열이며 리턴없이 리스트 내부를 직접 조작해야한다.

from typing import *


# 1. 내 풀이
def reverseString(s: List[str]) -> None:
    # deque 선언
    deque = collections.deque()
    # s에서 pop()으로 값을 추출하여 deque에 넣음
    for i in range(len(s)):
        deque.append(s.pop())
    # deque에서 popleft()로 값을 추출하여 s에 다시 넣음
    for i in range(len(deque)):
        s.append(deque.popleft())


s: List[str] = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)


# 2. 그냥 reverse() 함수 이용 (pythonic)
def reverseString2(s: List[str]) -> None:
    s.reverse()


reverseString2(s)
print(s)


# 3. 투 포인터 이용
def reverseString3(s: List[str]) -> None:
    (left, right) = (0, len(s) - 1)
    # right = len(s) - 1
    while left <= right:
        (s[left], s[right]) = (s[right], s[left])
        left += 1
        right -= 1


reverseString3(s)
print(s)
