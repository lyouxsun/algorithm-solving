# BFS - 17086번 - 아기 상어2
import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, -1, -1, 1, 1, 1]
dx = [-1, 1, -1, 0, 1, -1, 0, 1]

r, c = map(int, input().split())
arr = [0] * r
shark = []
for i in range(r):
    arr[i] = list(map(int, input().split()))
    for j in range(c):
        if arr[i][j] == 1:
            shark.append([i, j])

visited = [[float('inf')] * c for _ in range(r)]

for s in shark:
    q = deque()
    visited[s[0]][s[1]] = 0
    q.append(s)
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if visited[y][x] + 1 < visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])


ans = 0
for i in visited:
    ans = max(ans, max(i))
print(ans)