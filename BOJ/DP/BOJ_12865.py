# 동적 프로그래밍 - 12865번 - 평범한 배낭
## dp[i][j] = i번째 물품까지 고려한 상황에서, 무게가 j 일 때 가치의 최대합
##            1. i번째 물품이 포함된 경우       dp[i][j] = dp[i-1][j-w[i]] + v[i]
##            2. i번째 물품이 포함되지 않은 경우  dp[i][j] = dp[i-1][j]
import sys
input = sys.stdin.readline

n, weight = map(int, input().split())
w = [0] * n
v = [0] * n
dp = [[0] * (weight+1) for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    w[i] = a
    v[i] = b

if w[0] <= weight:
    dp[0][w[0]] = v[0]
# print(dp)

for i in range(1, n):
    for j in range(weight+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

# print(dp)
print(max(dp[n-1]))


# 4 7
# 1 7
# 2 2
# 3 3
# 4 4
## 정답: 13

# 1 1
# 1 3
## 정답: 3

# 6 304
# 98 98
# 4 4
# 6 6
# 100 100
# 101 101
# 103 103
## 정답: 304

