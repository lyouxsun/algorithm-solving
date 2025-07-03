# 재귀 - 1629번 - 곱셈
## a**b를 c로 나눈 나머지가 d일 때, a**(2b)를 c로 나눈 나머지는 d*d 이다.
import sys
input = sys.stdin.readline


def func(a, b, c):
    if b == 1:
        return a % c
    value = func(a, b // 2, c)
    value *= value
    if b % 2 == 0:
        # (a ** b) % c  = {(a ** b/2) % c } ** 2
        return value % c
    else:
        return (a * value) % c

a, b, c = map(int, input().split())
a %= c
print(func(a, b, c))
