# bfs - 1926번 - 그림
from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, input().split())
pic = []
visited = [[0] * c for _ in range(r)]
for i in range(r):
    pic.append(list(map(int, input().split())))
    for j in range(c):
        if pic[i][j] == 0:
            visited[i][j] = 1


ans, cnt = 0, 0
# for i in range(r):
#     print(visited[i])

def bfs(y, x):
    q = deque()
    q.append((y, x))
    size = 1
    while q:
        y, x = q.popleft()
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0<=ny<r) and (0<=nx<c):
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    size += 1
    # print('size =', size)
    return size


for y in range(r):
    for x in range(c):
        if visited[y][x] == 0:
            cnt += 1
            ans = max(ans, bfs(y, x))

print(cnt)
print(ans)