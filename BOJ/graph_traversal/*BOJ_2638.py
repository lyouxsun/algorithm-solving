# DFS - 2638번 - 치즈
import sys
sys.setrecursionlimit(10**9)
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(map(int, input().split())))

def is_air(y, x):
    flag = False
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < r) and (0 <= nx < c):
            if arr[ny][nx] == -1:
                flag = True
    if flag:
        arr[y][x] = -1
        air.add((y, x))
    else:
        arr[y][x] = 0


def find_air(y, x):
    # 종료 조건
    if visited[y][x] == 1:
        return
    visited[y][x] = 1
    arr[y][x] = -1
    air.add((y, x))
    # 실행문
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < r) and (0 <= nx < c):
            if arr[ny][nx] == 0 and visited[ny][nx] == 0:
                find_air(ny, nx)


ans = 0

air = set()
visited = [[0] * c for _ in range(r)]
find_air(0, 0)  # 외부 공기만 air라는 집합에 넣기

while True:
    # BFS 하기 전 준비작업 : cheese, air
    cheese = deque()
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                cheese.append((i, j))
            if arr[i][j] == 0:
                is_air(i, j)

    if len(cheese) == 0:
        break

    g = set()
    while cheese:
        y, x = cheese.popleft()
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < r) and (0 <= nx < c):
                if arr[ny][nx] <= 0 and (ny, nx) in air:
                    cnt += 1
        if cnt >= 2:
            g.add((y, x))

    for y, x in list(g):
        arr[y][x] = 0
    ans += 1

print(ans)

# 7 9
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0
# 답 = 3

