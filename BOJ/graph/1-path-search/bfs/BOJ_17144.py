# bfs - 17144번 - 미세먼지 안녕!
import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c, t = map(int, input().split())
air_up, air_down = -1, -1
arr = []
q = deque()

for i in range(r):
    line = list(map(int, input().split()))
    arr.append(line)
    # print(line)
    for j in range(c):
        if line[j] > 0:
            q.append((i, j, line[j]))
        if line[j] == -1:
            if air_up == -1:
                air_up = i
            else:
                air_down = i


def diffusion(q):
    new_q = deque()
    while q:
        y, x, value = q.pop()
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            newValue = value // 5
            if (0 <= ny < r) and (0 <= nx < c):
                if arr[ny][nx] != -1:
                    cnt += 1
                    new_q.append((ny, nx, newValue))
        arr[y][x] -= (newValue * cnt)
    return new_q


def air_purifier_up(y):
    global r, c
    # 1. ⬇
    if y == 0:
        arr[y][1] = 0
    elif y == 1:
        arr[y-1][0] = 0
    else:
        arr[y - 1][0] = 0
        for i in range(y - 1, 0, -1):
            arr[i][0] = arr[i - 1][0]

    # 2. ⬅
    for i in range(0, c - 1):
        arr[0][i] = arr[0][i + 1]

    # 3. ⬆
    for i in range(0, y):
        arr[i][c - 1] = arr[i + 1][c - 1]

    # 4. ➡
    for i in range(c-1, 0, -1):
        arr[y][i] = arr[y][i - 1]
    arr[y][1] = 0


def air_purifier_down(y):
    global r, c
    # 1. ⬆
    if y == r-1:
        arr[y][1] = 0
    elif y == r-2:
        arr[y][r-1] = 0
    else:
        arr[y + 1][0] = 0
        for i in range(y + 1, r - 1):
            arr[i][0] = arr[i + 1][0]

    # 2. ⬅
    for i in range(0, c - 1):
        arr[r - 1][i] = arr[r - 1][i + 1]

    # 3. ⬇
    for i in range(r - 1, y - 1, -1):
        arr[i][c - 1] = arr[i - 1][c - 1]

    # 4. ➡
    for i in range(c - 1, 0, -1):
        arr[y][i] = arr[y][i - 1]
    arr[y][1] = 0


for _ in range(t):
    # 1. 미세먼지 확산
    result = diffusion(q)
    q.clear()
    while result:
        y, x, v = result.popleft()
        arr[y][x] += v

    # for i in range(i):
    #     print(arr[i])
    # print()
    # 2. 공기청정기 작동
    air_purifier_up(air_up)
    air_purifier_down(air_down)

    # 3. q에 먼지 값 넣기
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                q.append((i, j, arr[i][j]))

ans = 0
for i in range(r):
    ans += sum(arr[i])
print(ans + 2)


# 7 8 2
# -1 0 0 0 0 0 0 9
# -1 0 0 0 3 0 0 8
# 0 0 5 0 0 0 22 0
# 0 8 0 0 0 0 0 0
# 0 0 9 0 0 10 43 0
# 8 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0

# 7 8 2
# 64 0 0 0 0 0 0 9
# 9 0 0 0 3 0 0 8
# 0 0 5 0 0 0 22 0
# 0 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# -1 0 5 0 15 0 0 0
# -1 0 40 0 0 0 20 0