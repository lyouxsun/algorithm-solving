# 재귀 - 25501번 - 재귀의 귀재
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
N = int(input())


def recursion(str, cnt, start, end):
    if start >= end:
        print(1, cnt)
        return
    elif str[start] != str[end]:
        print(0, cnt)
        return
    recursion(str, cnt +1, start + 1, end - 1)


for _ in range(N):
    input_str = list(input().strip())
    recursion(input_str, 1, 0, len(input_str) - 1)
