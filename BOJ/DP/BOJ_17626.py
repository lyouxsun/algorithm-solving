# DP - 17626번 - Four Square
## dp 점화식..
## 모든 수를 제곱수의 합으로 표현하기..
n = int(input())

dp = [4 for _ in range(n + 1)]
i = 1
while True:
    if i ** 2 > n:
        break
    dp[i ** 2] = 1
    i += 1
# print(dp)

for i in range(2, n + 1):
    min_ = 4
    j = 1
    while j ** 2 < i:
        dp[i] = min(dp[i], dp[i - j ** 2]+1)
        j += 1

# print(dp)
print(dp[n])

