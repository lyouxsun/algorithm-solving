# DFS - 3109번 - 빵집
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dy = [-1, 0, 1]      # ↗ → ↘ 방향 우선

R, C = map(int, input().split())
roads = [list(input().strip()) for _ in range(R)]

def dfs(y, x):
    if x == C - 1:
        visited[y][x] = True
        return True
    for d in dy:
        ny, nx = y + d, x + 1
        if 0 <= ny < R and 0 <= nx < C:
            if roads[ny][nx] == '.' and not visited[ny][nx]:
                # 교차 파이프 판별 불가능
                # 만약에, 이미 탐색해서 실패한 곳을 방문 처리 하면 교차가 생길 일이 없다.
                visited[ny][nx] = True
                # return dfs(ny, nx)        # 여기서 리턴하면 다음 방향을 탐색하지 못함
                if dfs(ny, nx):         # 🌟파이프 구축에 성공했을 때에만 바로 리턴하기!!!
                    return True
    return False

visited = [[False] * C for _ in range(R)]
ans = 0

for start in range(R):
    if roads[start][0] == '.':
        visited[start][0] = True
        if dfs(start, 0):
            ans += 1
print(ans)
