# DP - 9251번 - LCS
import sys
input = sys.stdin.readline

str1 = list(' ' + input().strip())
str2 = list(' ' + input().strip())
n1, n2 = len(str1), len(str2)

dp = [[0] * n2 for _ in range(n1)]

for i in range(1, n1):
    for j in range(1, n2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n1 - 1][n2 - 1])

# bcdefgha
# acdefghb
