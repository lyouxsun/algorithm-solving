# DP - 16194번 - 카드 구매하기 2
## 구매한 카드 개수의 합은 N과 일치해야 한다. = 크거나 작을 수 없다.
import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))

# 그리디? 아님 -> 이유 : 그리디는 a를 몇개 모아서 b가 될 수가 없는데, DP는 1개 짜리를 모아서 2개짜리를 살 수 있음
#           -> 그리디 불가 이유: 현재의 선택이 미래의 최적해를 보장하지 못함 (단순 합산으로 목표치 도달 불가)

# dp[i]= 카드를 i+1 개 샀을 때, 총액의 최솟값
#
# dp[0] = prices[0]
# dp[1] = min(
#     dp[0] + prices[1],
#     prices[0]
# )
# dp[2] = min(
#     dp[0] + prices[1],
#     dp[1] + prices[0],
#     prices[2]
# )

dp = [float("INF") for _ in range(N)]
dp[0] = prices[0]
for i in range(N):
    dp[i] = prices[i]
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + prices[i-1-j])
print(dp[-1])