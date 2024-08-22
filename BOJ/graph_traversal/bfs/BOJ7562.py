# 7562번 - 그래프 탐색 - 나이트의 이동 (BFS)
from collections import deque
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
def bfs():
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n):
                if nx == end_x and ny == end_y:
                    arr[nx][ny] = arr[x][y] + 1
                    return
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))


cycle = int(input())
for _ in range(cycle):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = list(map(int, input().split()))
    q = deque()
    q.append((start_x, start_y))
    if (start_x == end_x) and (start_y == end_y):
        print(0)
        continue
    bfs()
    # print(arr)
    print(arr[end_x][end_y])