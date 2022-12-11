# https://leetcode.com/problems/longest-palindromic-substring/

# 가장 긴 팰린드롬 부분 문자열을 출력하라.

from typing import *


# 첫 풀이 : 너무 어렵게 생각했다 -> 실패
def longestPalindrome(s: str) -> str:
    left, right = 0, len(s) - 1
    left2, right2 = 0, len(s) - 1
    left_save = list()
    right_save = list()
    left_save2 = list()
    right_save2 = list()

    while left <= right:
        if s[left] != s[right]:
            left_save.clear()
            right_save.clear()
            if right % 2 == 0 and left % 2 == 0:
                left = left + 1
            elif right % 2 == 0 and left % 2 == 1:
                right = right - 1
            elif right % 2 == 1 and left % 2 == 0:
                right = right - 1
            elif right % 2 == 1 and left % 2 == 1:
                left = left + 1
        elif s[left] == s[right]:
            left_save.append(left)
            right_save.append(right)
            left = left + 1
            right = right - 1

    while left2 <= right2:
        if s[left2] != s[right2]:
            left_save2.clear()
            right_save2.clear()
            if right2 % 2 == 0 and left2 % 2 == 0:
                right2 = right2 - 1
            elif right2 % 2 == 0 and left2 % 2 == 1:
                left2 = left2 + 1
            elif right2 % 2 == 1 and left2 % 2 == 0:
                left2 = left2 + 1
            elif right2 % 2 == 1 and left2 % 2 == 1:
                right2 = right2 - 1
        elif s[left2] == s[right2]:
            left_save2.append(left2)
            right_save2.append(right2)
            left2 = left2 + 1
            right2 = right2 - 1

    if max(right_save) - min(left_save) > max(right_save2) - min(left_save2):
        return s[min(left_save): max(right_save) + 1]
    else:
        return s[min(left_save2): max(right_save2) + 1]


s = "jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"
# "babab"

s2 = "cbbd"
# "bb"

s3 = "babcbabcbaccba"
s4 = "aacakacaa"
s5 = "ccd"
s6 = "eabcb"
s7 = "cmmrracelnclsbtdmuxtfiyahrvxuwreyorosyqapfpnsntommsujibzwhgugwtvxsdsltiiyymiofbslwbwevmjrsbbssicnxptvwmsmiifypoujftxylpyvirfueagprfyyydxeiftathaygmolkcwoaavmdmjsuwoibtuqoewaexihispsshwnsurjopdwttlzyqdbkypvjsbuidsdnpgklhwfnqdvlffcysnxeywvwvblatmxbflnuykhfhjptenhcxqinomlwalvlezefqybpuepbnymzlruuirpiatqgjgcnfmrlzshauoxuoqopcikogfwpssjdeplytcapmujyvgtfmmolnuadpwblgmcaututcrwsqrlpaaqobjfnhudmsulztbdkxpfejavastxejtpbqfftdtcdhvtpbzfuqcwkxtldtjycreimiujtxudtmokcoebhodbkgkgxjzrgyuqhozqtidltodlkziyofdeszwiobkwesdijxbbagguxvofvtphqxgvidqfkljufgubjmjllxoanbizwtedykwmneaosopynzlzvrlqcmyaahdcagfatlhwtgqxsyxwjhexfiplwtrtydjzrsysrcwszlntwrpgfedhgjzhztffqnjotlfudvczwfkhuwmdzcqgrmfttwaxocohtuscdxwfvhcymjpkqexusdaccw"


# print(longestPalindrome(s))
# print(longestPalindrome(s2))
# print(longestPalindrome(s3))
# print(longestPalindrome(s4))
# print(longestPalindrome(s5))
# print(longestPalindrome(s6))
# print(longestPalindrome(s7))

# 두 번째 풀이 : 길이가 1씩 줄어드는 고정막대를 만들어서 왼쪽에서부터 오른쪽으로 움직이며 스캔 -> 성공
# 통과하긴 했으나 Runtime이 하위 13%라는 결과가 나움 -> 좌측에서 우측으로 고정막대를 하나만 움직여서 그럴수도
def longestPalindrome2(s: str) -> str:
    slide = len(s)
    while slide > 0:
        for i in range(len(s) - slide + 1):
            n = s[i: i + slide]
            if n == n[::-1]:
                return n
            if i + slide == len(s):
                slide -= 1


# 세 번째 풀이 : 투 포인터 슬라이딩 윈도우를 이용한 풀이
# 펠린드롬의 길이가 짝수의 경우와 홀수의 경우 두 경우의 윈도우를 만들어 검사한다.
def longestPalindrome3(s: str) -> str:
    # 1. left와 right를 인수로 받아 확장하는 함수 expand 정의
    # 윈도우는 s[left]와 s[right]이 같을 경우 확장한다.
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    # 2. 문자열 슬라이싱을 이용한 필터링 (길이가 1인 경우 펠린드롬 | 뒤집었을 때 같은 경우 펠린드롬)
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    # 3. 슬라이딩 윈도우 이동
    for i in range(0, len(s) - 1):
        # key=len으로 길이를 기준으로 max값을 구한다.
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


# print(longestPalindrome2(s))
# print(longestPalindrome2(s2))
# print(longestPalindrome2(s3))
# print(longestPalindrome2(s4))
# print(longestPalindrome2(s5))
# print(longestPalindrome2(s6))
# print(longestPalindrome2(s7))

print(longestPalindrome3(s))
print(longestPalindrome3(s2))
print(longestPalindrome3(s3))
print(longestPalindrome3(s4))
print(longestPalindrome3(s5))
print(longestPalindrome3(s6))
print(longestPalindrome3(s7))
