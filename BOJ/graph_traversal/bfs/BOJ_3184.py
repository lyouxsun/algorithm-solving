# bfs - 3184번 - 양
from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, input().split())
arr = []
visited = [[0] * c for _ in range(r)]
for i in range(r):
    line = list(input().strip())
    arr.append(line)
    for j in range(c):
        if arr[i][j] == '#':
            visited[i][j] = 1


def bfs(y, x):
    cnt_o, cnt_v = 0, 0
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        if arr[y][x] == 'o':
            cnt_o += 1
        elif arr[y][x] == 'v':
            cnt_v += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ((0 <= ny < r) and (0 <= nx < c)) and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
    return cnt_o, cnt_v


ans_o, ans_v = 0, 0
for i in range(r):
    q = deque()
    for j in range(c):
        if visited[i][j] != 1:
            visited[i][j] = 1
            cnt_o, cnt_v = bfs(i, j)
            if cnt_o <= cnt_v:
                ans_v += cnt_v
            else:
                ans_o += cnt_o

print(ans_o, ans_v)

# '.' : 빈 필드
# '#' : 울타리
# 'o' : 양
# 'v' : 늑대
