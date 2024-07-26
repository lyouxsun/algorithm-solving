# 동적 프로그래밍 - 10942번 - 팰린드롬?

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * n for _ in range(n)]  # 각 자리를 중심으로 하는 팰린드롬의 반지름 길이 저장

for i in range(n):  # i < j
    dp[i][i] = 1  # 길이 1
    if i < n - 1:  # 길이 2
        if arr[i + 1] == arr[i]:
            dp[i][i + 1] = 1
        else:
            dp[i][i + 1] = 0

for i in range(2, n):  # i : 부분수열의 길이, j : 부분수열의 시작점
    for j in range(n):
        if i+j < n:
            if arr[j] == arr[j+i]:
                dp[j][j+i] = dp[j+1][j+i-1]
            else:
                dp[j][j+i] = 0

# print(dp)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])