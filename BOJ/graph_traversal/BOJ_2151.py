# BFS - 2151번 - 거울 설치
import sys
from collections import deque

input = sys.stdin.readline
n: int = int(input())
arr = []
doors = []
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
for i in range(n):
    arr.append(list(input().strip()))
    for j in range(n):
        if arr[i][j] == '#':
            doors.append([i, j])

visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
q = deque()
for i in range(4):
    visited[doors[0][0]][doors[0][1]][i] = 0
    ny = doors[0][0] + dy[i]
    nx = doors[0][1] + dx[i]
    if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != '*':
        q.append([[ny, nx], i, 0])
        visited[ny][nx][i] = 0
        if arr[ny][nx] == '!':
            for nd in [(i + 1) % 4, (i + 3) % 4]:  # 좌회전과 우회전
                visited[ny][nx][nd] = 1
                q.append([[ny, nx], nd, 1])

ans = float('inf')
while q:
    [y, x], d, cnt = q.popleft()
    if [y, x] == doors[1]:
        ans = min(ans, cnt)
        continue

    ny = y + dy[d]
    nx = x + dx[d]

    if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != '*':
        if visited[ny][nx][d] > cnt:
            visited[ny][nx][d] = cnt
            q.append([[ny, nx], d, cnt])
            # print('y =', y, ', x =', x, ', d =', d, ', cnt =', cnt)

        if arr[ny][nx] == '!':
            for nd in [(d + 1) % 4, (d + 3) % 4]:  # 좌회전과 우회전
                if visited[ny][nx][nd] > visited[ny][nx][d] + 1:
                    visited[ny][nx][nd] = visited[y][x][d] + 1
                    q.append([[ny, nx], nd, cnt + 1])

# print(min(visited[doors[1][0]][doors[1][1]]))
print(min(visited[doors[1][0]][doors[1][1]]))
