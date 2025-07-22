# DP - 1106번 - 호텔
## ~~ dp[i] = 0~i번째 도시까지 고려했을 때 최소비용 ~~
## dp[i] = i을 모으는 데 필요한 최소비용
import sys
input = sys.stdin.readline

GOAL, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
MAX_CLIENT = max(client for _, client in arr)
SIZE = MAX_CLIENT
for i in range(2, ):
    if MAX_CLIENT * (i - 1) <= GOAL < MAX_CLIENT * i:
        SIZE *= i
        break

SIZE += 1
dp = [float('inf')] * SIZE

for cost, client in arr:
    multiple = 1
    while True:
        if client * multiple >= SIZE:
            break
        dp[client * multiple] = min(dp[client * multiple], cost * multiple)
        multiple += 1
for i in range(1, SIZE):
    if dp[i] != float('inf'):
        for j in range(i, 0, -1):
            dp[j] = min(dp[j], dp[i])

for i in range(SIZE):
    for j in range(1, i // 2 + 1):
        dp[i] = min(dp[i], dp[i - j] + dp[j])

# print('최종 dp =', dp)

print(min(dp[GOAL:]))

# 반례
# input:
# 1 15
# 13 47
# 12 33
# 80 93
# 20 38
# 16 40
# 54 51
# 18 13
# 31 49
# 29 35
# 3 13
# 69 70
# 55 28
# 79 25
# 33 67
# 22 18
#
# answer:
# 3
