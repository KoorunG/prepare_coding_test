# https://www.acmicpc.net/problem/1463

'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

num = int(input())


def div2(inp: int, count: int = 0) -> int:
    return div3(inp // 2, count + 1) if inp % 2 == 0 else count


def div3(inp: int, count: int = 0) -> int:
    return div3(inp // 3, count + 1) if inp % 3 == 0 else count


def sub1(inp: int) -> int:
    return inp - 1


# def cal(inp: int, count: int = 0) -> int:
#     while inp % 3 == 0:


# num = 3x + 2y + z + 1일 때 x+ y+ z의 최솟값을 구하면 된다.
print(div3(num))