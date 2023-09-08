# 다이나믹 프로그래밍 - 1904번 - 01타일
import sys
input = sys.stdin.readline
N = int(input())
if N<3:
    dp = [0]*3
else:
    dp = [0]* (N+1)

dp[1] = 1
dp[2] = 2
if N>=3:
    for i in range(3, N+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
print(dp[N])
# dp[4] = 5 = 1+(N-1)+(N//2)
# dp[5] = 1+4+3 = 8 = dp[3]+dp[4]