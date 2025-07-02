# DFS&DP - 1520번 - 내리막 길
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1] * C for _ in range(R)]


# print(graph)

def dfs(y, x):
    # print('y=', y, ', x=', x, ' 방문')
    if y == R - 1 and x == C - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < R) and (0 <= nx < C) and graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]

dfs(0, 0)
# for i in range(R):
#     print(dp[i])

print(dp[0][0])
