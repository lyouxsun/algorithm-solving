# DP - 2294번 - 동전 2
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_set = set()
for _ in range(n):
    num = int(input())
    if num > k:
        continue
    coin_set.add(num)
coins = list(coin_set)

dp = [float('inf')] * (k+1)
for i in coins:
    dp[i] = 1

for i in range(1, k+1):
    if dp[i] == 1:
        continue
    for j in coins:
        if i-j < 0:
            continue
        dp[i] = min(dp[i], dp[i-j] + dp[j])
# print(dp)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])