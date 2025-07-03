# bfs - 1261번 - 알고스팟
from collections import deque
import sys

input = sys.stdin.readline

garo, sero = map(int, input().split())
arr = []
for i in range(sero):
    arr.append(list(map(int, input().strip())))
visited = [[float('inf')] * garo for _ in range(sero)]
visited[0][0] = 0

# print(arr)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
q = deque()
q.append([0, 0])

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < sero and 0 <= nx < garo:
            new_value = visited[y][x] + arr[ny][nx]
            if visited[ny][nx] > new_value:
                visited[ny][nx] = new_value
                q.append([ny, nx])
# print(visited)

print(visited[sero - 1][garo - 1])
