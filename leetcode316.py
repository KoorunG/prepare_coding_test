# https://leetcode.com/problems/remove-duplicate-letters/
# 중복된 문자를 제외하고 사전식 순서로 나열하여라
# (sorting 하는 것이 아니라 중복을 제거하면서 사전적으로 가장 먼저 오도록)
import collections

s = "bcabc"
# Output: "abc"

s2 = "cbacdcbc"

s3 = "beadbeb"
# Output: "acdb"

s4 = "bbbbbbeeeeeeeeaddbeeebaaa"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        reverse = []
        for i in s:
            # 스택에 문자열이 있는 경우 "평가"
            if i in stack:
                old = "".join(stack)
                copy = stack.copy()
                copy.remove(i)
                copy.append(i)
                new = "".join(copy)
                if old > new:
                    stack = copy
            else:
                stack.append(i)
        for j in s[::-1]:
            if j in reverse:
                old = "".join(reverse)
                copy = reverse.copy()
                copy.remove(j)
                copy.append(j)
                new = "".join(copy)
                if old < new:
                    reverse = copy
            else:
                reverse.append(j)

        print("".join(reverse[::-1]), "".join(stack))
        return min("".join(reverse[::-1]), "".join(stack))

    # 1. 재귀를 이용한 풀이
    def removeDuplicateLetters(self, s: str) -> str:
        # set으로 중복을 제거한 집합을 정렬하여 반복을 돌린다.
        # 집합을 정렬하여 리스트로 만들었기 때문에 중복제거 && 사전식 순서의 사전조건을 만족한 셈
        for char in sorted(set(s)):
            # suffix : 해당 문자열이 가장 먼저 나온 인덱스부터 리스트를 자른 값 == 사전적 배열 실현
            suffix = s[s.index(char):]
            # 문자열의 set과 suffix의 set이 같을 경우에 값을 반환한다.
            # == 적어도 모든 문자가 하나씩은 들어가야 하기 때문에 두 집합의 크기가 같을 경우 리턴한다.
            if set(s) == set(suffix):
                # 현재 문자열에 재귀한 값을 누적시킨다.
                # 재귀값은 현재 문자열을 제외한 suffix를 파라미터로 받는다.
                # 따라서 suffix가 더이상 존재하지 않을 경우 백트래킹 되면서 결과가 리턴된다!
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        # (재귀함수의 초기 리턴값)
        return ''

    # 2. 스택을 이용한 풀이
    def removeDuplicateLetters2(self, s: str) -> str:
        # 적어도 하나의 문자가 있는지 여부를 받기위한 카운터와, 문자 체크여부를 받는 집합 seen, 스택 stack을 선언한다.
        counter, seen, stack = collections.Counter(s), set(), list()
        # 문자열을 반복을 돌면서
        for char in s:
            counter[char] -= 1
            # 해당 문자가 검사를 받은 경우는 반복을 건너뛴다.
            if char in seen:
                continue
            # 현재 문자(char)이 스택의 최상단의 문자보다 작은경우 (사전적으로 앞서있는 경우) && 최상단의 문자가 스택에 존재하는 경우
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                # 스택에서 최상단의 문자를 뺀다. (사전적으로 앞서는 문자로 교체한다.)
                seen.remove(stack.pop())
            # 아니라면 스택에 현재 문자열을 적층한다.
            stack.append(char)
            # 문자가 검사를 받은 경우는 seen 집합에 "이력을 남긴다".
            seen.add(char)
        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicateLetters2(s4))
# sol.removeDuplicateLetters(s)