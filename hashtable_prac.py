# 해시 테이블에서 해싱의 과정중 충돌은 생각보다 빈번하게 일어난다.
# 이는 비둘기집 원리에 의한 것으로, n개의 아이템을 m개의 공간에 넣을 때
# n > m이라면 아이템이 적어도 둘 이상이 존재하는 컨테이너는 반드시 존재한다.
# 즉 좋지 못한 해시함수를 사용한다면 충돌이 다수 발생하여 공간의 낭비가 발생하게 된다.


# 23명 이상이 모이면 생일이 같은 사람이 존재할 확률이 50% 이상이다.

import random


TRIALS = 100_000
same_birthdays = 0

for i in range(TRIALS):
    birthdays = []
    for j in range(57):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays / TRIALS * 100}%') # n = 23일때 50%, 57일때 99%를 넘게 됨..

