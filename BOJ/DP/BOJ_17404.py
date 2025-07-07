# dp - 17404번 - RGB거리 2
import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
result = INF

for first_color in range(3):  # 0: R, 1: G, 2: B
    dp = [[INF] * 3 for _ in range(N)]

    # 첫 번째 집은 첫 색으로 고정, 나머지는 불가능한 값으로 초기화
    dp[0][first_color] = costs[0][first_color]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

    # 마지막 집이 첫 집과 다른 색일 때만 고려
    for last_color in range(3):
        if last_color != first_color:
            result = min(result, dp[N - 1][last_color])

print(result)