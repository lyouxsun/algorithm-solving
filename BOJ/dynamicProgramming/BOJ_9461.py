# 다이나믹 프로그래밍 - 9461번 - 파도반 수열
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
dp = [0 for _ in range(max(arr))]
for i in range(max(arr)):
    if i<3:
        dp[i] = 1
    else:
        dp[i] = dp[i-3] + dp[i-2]
for i in range(N):
    print(dp[arr[i]-1])