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


print(longestPalindrome2(s))
print(longestPalindrome2(s2))
print(longestPalindrome2(s3))
print(longestPalindrome2(s4))
print(longestPalindrome2(s5))
print(longestPalindrome2(s6))
print(longestPalindrome2(s7))
