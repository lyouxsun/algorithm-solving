# 다이나믹 프로그래밍 - 1912번 - 연속합
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))