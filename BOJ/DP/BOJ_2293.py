# DP - 2293번 - 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
coins = []
for i in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)
coins.sort()

for coin in coins:
    dp[coin] += 1
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]
    # print(dp)

print(dp[-1])
