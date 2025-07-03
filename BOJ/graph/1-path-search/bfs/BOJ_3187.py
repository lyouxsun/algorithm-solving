# bfs - 3187번 - 양치기 꿍

from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, input().split())
graph = []
visited = [[0]* c for _ in range(r)]
ans_v, ans_k = 0, 0

def bfs(y, x):
    global ans_v, ans_k, r, c
    q = deque()
    q.append((y, x))
    visited[y][x] =1
    wolf, sheep = 0, 0
    if graph[y][x] == 'v':
        wolf += 1
    elif graph[y][x] == 'k':
        sheep += 1

    while q:
        (y, x) = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < r) and (0 <= nx < c) and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx))
                if graph[ny][nx] == 'v':
                    wolf += 1
                elif graph[ny][nx] == 'k':
                    sheep += 1
    if wolf >= sheep:
        ans_v += wolf
    else:
        ans_k += sheep

for i in range(r):
    line = list(input().strip())
    graph.append(line)
    for j in range(c):
        if line[j] == '#':
            visited[i][j] = 1

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            bfs(i, j)

print(ans_k, ans_v)