# DP - 1309번 - 동물원
## 점화식 : dp[n] = 2 * dp[n-1] + dp[n-2]
n = int(input())
dp = [0] * (n + 1)
if n == 1:
    print(3)
    exit()
dp[1] = 3
dp[2] = 7
if n == 2:
    print(dp[n])
    exit()

for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901
print(dp[n])
