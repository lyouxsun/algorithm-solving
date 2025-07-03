# 다이나믹 프로그래밍 - 2156번 - 포도주 시식
import sys
input = sys.stdin.readline
N = int(input())
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = int(input())
dp = [0 for _ in range(N)]
dp[0] = arr[0]
if N >= 2:
    dp[1] = dp[0] + arr[1]
if N >= 3:
    dp[2] = max(dp[0], arr[1])+arr[2]
if N >= 4:
    dp[3] = max(dp[1], dp[0]+arr[2])+arr[3]
if N>=5:
    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3]+arr[i-1], dp[i-4]+arr[i-1])+arr[i]
print(max(dp))