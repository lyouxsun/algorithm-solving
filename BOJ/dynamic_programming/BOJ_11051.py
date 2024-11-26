# DP - 11051번 - 이항 계수2
## dp[n][k] = nCk 를 10007로 나눈 값
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

if k == 0 or n == k:
    print(1)
    exit()

if k == 1:
    print(n)
    exit()

dp = [[1] * (k+1) for i in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = 1
    dp[i][1] = i

for r in range(2, n+1):
    for c in range(2, k+1):
        if r <= c:
            continue
        dp[r][c] = (dp[r-1][c-1] + dp[r-1][c])%10007

# for i in range(n+1):
#     print(dp[i])

print(dp[n][k])

# index error 발생 - 이유 : n, k가 1 또는 2일 때 발생하는 거 같음
