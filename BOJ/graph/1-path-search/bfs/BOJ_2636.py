# BFS - 2636번 - BFS
## 발상의 전환! 치즈가 아닌 것들에 집중하자~
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs():
    cheese = []
    visited = [[0] * m for i in range(n)]
    q = deque()
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n) and (0 <= nx < m) and not visited[ny][nx]:
                visited[ny][nx] = 1
                if arr[ny][nx] == 0:        # 공기인 경우
                    q.append((ny, nx))
                else:                        # 치즈인 경우
                    cheese.append((ny, nx))
    cnt = len(cheese)
    # print('cnt =', cnt)
    for (y, x) in cheese:
        arr[y][x] = 0
    return cnt


n, m = map(int, input().split())
arr = []
cheese_size = 0
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    cheese_size += sum(line)

cnt = 1
while True:
    melt = bfs()
    cheese_size -= melt
    # print('남은 치즈 개수 =', melt)
    if cheese_size == 0:
        print(cnt)
        print(melt)
        break
    cnt += 1
