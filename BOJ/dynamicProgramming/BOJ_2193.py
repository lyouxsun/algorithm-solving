# 다이나믹 프로그래밍 - 2193번 - 이친수
import sys
input = sys.stdin.readline
N = int(input())
dp = [0 for _ in range(N)]
dp[0] = 1
if N >= 2:
    dp[1] = 1
if N >= 3:
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N-1])