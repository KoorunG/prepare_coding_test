# https://leetcode.com/problems/valid-parentheses/
# 괄호로 된 입력값이 올바른지 판별하여라.
import collections
from typing import *

s = "()"
# Output: true

s2 = "()[]{}"
# Output: true

s3 = "(]"
# Output : false

s4 = "{[]}"
# Output : true

s5 = "(([]){})"
# Output : true

s6 = "){"


class Solution:
    # 1. 망한 풀이... 너무 무식하게 했다
    # def isValid(self, s: str) -> bool:
    #     if len(s) % 2 != 0:
    #         return False
    #     case1 = False
    #     case2 = False
    #     result1 = []
    #     result2 = collections.deque()
    #     for i in s:
    #         result1.append(i)
    #         result2.append(i)
    #     # case1
    #     for j in range(len(result1) // 2):
    #         p = result1.pop()
    #         q = result1.pop()
    #         if p == "{" or p == "(" or p == "[":
    #             case1 = False
    #             break
    #         if (p == "}" and q == "{") or (p == "]" and q == "[") or (p == ")" and q == "("):
    #             case1 = True
    #         else:
    #             case1 = False
    #             break
    #
    #     for k in range(len(result2) // 2):
    #         r = result2.pop()
    #         z = result2.popleft()
    #         if r == "{" or r == "[" or r == "(":
    #             case2 = False
    #             break
    #         if (r == "}" and z == "{") or (r == "]" and z == "[") or (r == ")" and z == "("):
    #             case2 = True
    #         else:
    #             case2 = False
    #             break
    #     return case1 | case2

    # 2. 반복문을 돌면서 리스트에 넣은 뒤 "닫는 괄호" 일 때 pop으로 꺼내면서 케이스를 비교함
    def isValid2(self, s: str) -> bool:
        # 예외처리
        if len(s) % 2 == 1:
            return False
        tmp = []
        for i in s:
            # 반복문을 돌면서 요소를 스택에 넣는다.
            tmp.append(i)
            # 닫는괄호일 경우
            if i == ")" or i == "}" or i == "]":
                # pop으로 꺼낸다
                p = tmp.pop()
                # pop으로 꺼냈을 때 리스트의 길이가 0이라면 (닫는괄호로 시작한 경우라면) False 리턴
                if len(tmp) == 0:
                    return False
                # 리스트에서 pop으로 꺼냈을 때 여는괄호와 닫는괄호가 매칭되지 않을 경우 False 리턴
                last = tmp.pop()
                if (last == "[" and p != "]") or (last == "{" and p != "}") or (last == "(" and p != ")"):
                    return False
        # 위의 과정을 거쳤을 때 리스트에 요소가 남아있다면 False 리턴
        return len(tmp) == 0

    def isValid3(self, s: str) -> bool:
        stack = []
        # 딕셔너리로 매핑테이블을 만든다.
        table = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        # 반복문을 돌면서
        for c in s:
            # 닫는괄호가 아닐경우 append
            if c not in table:
                stack.append(c)
            # 스택이 비어있거나, 닫는괄호일 경우 매핑테이블과 매칭되지 않을 경우 False 리턴
            elif not stack or table[c] != stack.pop():
                return False
        # 결과로 리스트에 요소가 남아있으면 False를 리턴하는 것을 한번에 처리
        return len(stack) == 0


sol = Solution()
print(sol.isValid3(s))
print(sol.isValid3(s2))
print(sol.isValid3(s3))
print(sol.isValid3(s4))
print(sol.isValid3(s5))
print(sol.isValid3(s6))
