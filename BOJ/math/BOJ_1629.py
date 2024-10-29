# 분할정복(재귀) - 1629번 - 곱셈
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def multiply(a, b, c):
    if b == 1:
        return a % c
    result = multiply(a, b // 2, c)
    if b % 2 == 1:
        return (result * result * a) % c
    return (result * result) % c


a, b, c = map(int, input().split())
print(multiply(a, b, c))
