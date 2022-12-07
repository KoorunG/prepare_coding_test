# https://leetcode.com/problems/reorder-data-in-log-files/
import collections
# 로그의 가장 앞부분은 식별자다.
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다. -> 이걸 어떻게 하지?
# 숫자 로그는 입력 순서대로 한다.

from typing import *


def reorderLogFiles(logs: List[str]) -> List[str]:
    # letters와 digits 분리
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # letters를 2개의 키를 기준으로 정렬
    # 람다식을 쓰는 부분을 주의할 것
    # sort는 key 매개변수로 함수나 람다식을 받으며 튜플이 오면 튜플의 요소 순차적으로 정렬한다.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

logs2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
# ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


# print(reorderLogFiles(logs))
print(reorderLogFiles(logs2))
