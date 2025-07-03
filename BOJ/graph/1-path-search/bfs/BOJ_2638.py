# BFS - 2638번 - 치즈
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

r, c = map(int, input().split())
graph = []
visited = [[0] * c for _ in range(r)]
for i in range(r):
    line = list(map(int, input().split()))
    graph.append(line)


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        air_cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < r) and (0 <= nx < c) and graph[ny][nx] == 0:
                air_cnt += 1
        if air_cnt >= 2:

for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            bfs(i, j)