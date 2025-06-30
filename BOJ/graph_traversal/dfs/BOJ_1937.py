# DFS&DP - 1937번 - 욕샘쟁이 판다
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

def dfs(y, x):
    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < N) and (0 <= nx < N):
            if forest[y][x] < forest[ny][nx]:
                if dp[ny][nx] == 0:
                    dfs(ny, nx)
                dp[y][x] = max(dp[y][x], 1 + dp[ny][nx])


for y in range(N):
    for x in range(N):
        if dp[y][x] == 0:
            dfs(y, x)
# print(dp)

ans = max(max(row) for row in dp)
print(ans)