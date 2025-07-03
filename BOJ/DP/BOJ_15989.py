# 동적 프로그래밍 - 15989번 - 1, 2, 3 더하기 4
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0] * (max(arr)+1)
dp[0] = 1
dp[1] = 1

for j in range(1, 4):       # 1로만 만들기 -> 2로만 만들기 -> 3으로만 만들기
    for i in range(2, max(arr)+1):
        if i-j >= 0:
            dp[i] += dp[i-j]
    # print(j)
    # print(dp)

for i in arr:
    print(dp[i])