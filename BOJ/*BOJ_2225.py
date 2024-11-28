# DP - 2225번 - 합분해
## dp[i] = i개의 숫자로 N을 만들 수 있는 경우의 수
n, k = map(int, input().split())

# dp[i][j] = i를 j개 수의 합으로 나타낼 수 있는 경우의 수
# dp[i][j] = dp[i-(j-1)][1] + dp[i-(j-2)][2] + ... + dp[i-1][j]
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# for i in range(n + 1):
#     print(dp[i])
print(dp[n][k] % 1000000000)