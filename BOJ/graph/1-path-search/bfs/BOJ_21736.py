# bfs - 21736번 - 헌내기는 친구가 필요해
import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
n, m = map(int, input().split())
arr = []
y, x = 0, 0
for i in range(n):
    line = list(input().strip())
    arr.append(line)
    for j in range(m):
        if line[j] == 'I':
            y = i
            x = j

visited = [[0] * m for _ in range(n)]
q = deque()
q.append((y, x))
visited[y][x] = 1
ans = 0
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<=ny<n) and (0<=nx<m):
            if visited[ny][nx] == 0 and arr[ny][nx] != 'X':
                if arr[ny][nx] == 'P':
                    ans += 1
                q.append((ny, nx))
                visited[ny][nx] = 1

if ans == 0:
    print('TT')
else:
    print(ans)