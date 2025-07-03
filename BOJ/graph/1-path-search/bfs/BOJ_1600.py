# BFS - 1600번 - 말이 되고픈 원숭이
import sys
from collections import deque

input = sys.stdin.readline
limit = int(input())

c, r = map(int, input().split())
arr = [0] * r
for i in range(r):
    arr[i] = list(map(int, input().split()))

hx = [-1, -1, -2, -2, 1, 1, 2, 2]
hy = [-2, 2, -1, 1, -2, 2, -1, 1]
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

visited = [[[float('inf')] * (limit + 1) for _ in range(c)] for _ in range(r)]
visited[0][0][limit] = 0
q = deque()
q.append([0, 0, limit])
while q:
    y, x, l = q.popleft()
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if arr[ny][nx] != 1:
                if visited[ny][nx][l] > visited[y][x][l] + 1:
                    visited[ny][nx][l] = visited[y][x][l] + 1
                    q.append([ny, nx, l])
    if l > 0:
        for i in range(8):
            ny = y + hy[i]
            nx = x + hx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if arr[ny][nx] != 1:
                    if visited[ny][nx][l - 1] > visited[y][x][l] + 1:
                        visited[ny][nx][l - 1] = visited[y][x][l] + 1
                        q.append([ny, nx, l - 1])

ans = min(visited[r - 1][c - 1])
# for i in visited:
#     print(i)
# print()

if ans == float('inf'):
    print(-1)
else:
    print(ans)

# 반례
# 1
# 7 8
# 0 0 0 0 0 0 0
# 1 1 1 1 1 1 0
# 1 1 1 1 1 1 0
# 0 0 0 1 1 1 0
# 0 1 1 1 0 0 0
# 0 1 1 1 1 1 1
# 0 1 1 1 1 1 1
# 0 0 0 0 0 0 0
# 답 : 25
