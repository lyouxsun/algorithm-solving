# DFS - 16724번 - 피리 부는 사나이
## 그래프 그룹 단위를 카운트하면 됨
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

d = dict()
d['U'] = (-1, 0)
d['D'] = (1, 0)
d['L'] = (0, -1)
d['R'] = (0, 1)

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

def dfs(y, x, v):
    # 1. base condition
    if v[y][x]:
        return
    # # 2. 방문 처리
    v[y][x] = True
    dir_y, dir_x = d[graph[y][x]]
    # print('(', y, '행 ', x, '열 ) 의 방향 : dy=', dy, ', dx=', dx)

    ny, nx = y + dir_y, x + dir_x
    # 3. 조건 확인 후 다음 재귀 호출
    if (0 <= ny < R) and (0 <= nx < C) and not v[ny][nx]:
        # print('dfs 안 탐색 시작 = (', r, '행 ', c, '열) 방문 처리')
        # v[ny][nx] = True
        dfs(ny, nx, v)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < R) and (0 <= nx < C) and not v[ny][nx]:
            # 오른쪽 탐색했는데 L일 때,
            # 왼쪽 탐색했는데 R일 때,
            # 위쪽 탐색했을 때 D일 때
            # 아래쪽 탐색했을 때 U일 때,
            dir_y, dir_x = d[graph[ny][nx]]
            if dy[i] + dir_y == 0 and dx[i] + dir_x == 0:
                dfs(ny, nx, v)

group_num = 0
visited = [[False] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if not visited[r][c]:
            dfs(r, c, visited)
            # print('탐색 시작 = (', r, '행 ', c, '열)')
            group_num += 1
print(group_num)