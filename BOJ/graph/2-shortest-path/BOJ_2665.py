# bfs - 2665번 - 미로만들기
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))
# print(maze)

visited = [[float('inf')] * n for _ in range(n)]

q = deque()
visited[0][0] = 0
q.append([0, 0])

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < n) and (0 <= nx < n):
            new_cost = 0
            if maze[ny][nx] == 1:           # 백
                new_cost = visited[y][x]
            else:           # 흑
                new_cost = visited[y][x] + 1
            if visited[ny][nx] > new_cost:
                visited[ny][nx] = new_cost
                q.append((ny, nx))

# for i in range(n):
#     print(visited[i])
print(visited[n-1][n-1])