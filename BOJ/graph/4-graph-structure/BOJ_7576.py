# 그래프 이론 - 7576번 - 토마토 : 최단경로
import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < X) and (0 <= ny < Y) and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

q = deque()
graph = []
X, Y = map(int, input().split())
for _ in range(Y):
    graph.append(list(map(int, input().split())))
for x in range(X):
    for y in range(Y):
        if graph[y][x] == 1:
            q.append((y, x))
bfs()
ans = 0
for row in graph:
    for a in row:
        if a == 0:
            print(-1)
            exit(0)
        ans = max(max(row), ans)
print(ans-1)