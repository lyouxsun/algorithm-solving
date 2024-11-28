# 그래프 이론 - 30464번 - 시간낭비
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [-1] * n
dp[0], now = 0, 0
cnt = 0
while now + arr[now] < n:
    cnt += 1
    dp[now + arr[now]] = cnt
    now += arr[now]
print(dp)
