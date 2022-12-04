# https://leetcode.com/problems/most-common-word/
import collections
import re
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하여라. 대소문자를 구분하지 않고 마침표나 쉼표 등은 무시한다.

from typing import *

paragraph = "Bob! hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


# 1. 내 풀이_1
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    for char in paragraph:
        paragraph = paragraph.lower()
        if not char.isalpha():
            paragraph = paragraph.replace(char, " ")

    words = paragraph.split()

    words_count = collections.Counter(words)
    for ban in banned:
        if words_count[ban]:
            words_count.pop(ban)

    return words_count.most_common()[0][0]


# 2. 내 풀이_2 : 정규식 이용
def mostCommonWord2(paragraph: str, banned: List[str]) -> str:
    test = re.sub("[^a-zA-Z]", " ", paragraph).lower().split()
    count = collections.Counter(test)
    for ban in banned:
        if ban in count:
            count.pop(ban)
    return count.most_common(1)[0][0]


# print(mostCommonWord(paragraph, banned))
print(mostCommonWord2(paragraph, banned))


# 3. 리스트 컴프리헨션 이용
def mostCommonWord3(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub("[^\w]", " ", paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(mostCommonWord3(paragraph, banned))
