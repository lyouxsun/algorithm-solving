import sys
input = sys.stdin.readline
n = int(input())
mod = 1_000_000_000

dp = [[0 for _ in range(1 << 10)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1 << i] = 1

for i in range(1, n):
    dp_next = [[0 for _ in range(1024)] for _ in range(10)]
    for j in range(10):
        for k in range(1024):
            if j < 9:
                dp_next[j][k | (1 << j)] = (dp_next[j][k | (1 << j)] + dp[j + 1][k]) % mod
            if j > 0:
                dp_next[j][k | (1 << j)] = (dp_next[j][k | (1 << j)] + dp[j - 1][k]) % mod

    dp = dp_next

print(sum(dp[i][1023] for i in range(10)) % mod)