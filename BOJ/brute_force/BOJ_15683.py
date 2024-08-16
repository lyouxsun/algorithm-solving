# 브루트 포스 - 15683번 - 감시
from copy import deepcopy

directions = {
    # 상하좌우
    1: [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    2: [[1, 1, 0, 0], [0, 0, 1, 1]],
    3: [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1]],
    4: [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]],
    5: [[1, 1, 1, 1]]
}

r, c = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
cctvs = []
for i in range(r):
    for j in range(c):
        if 0 < room[i][j] < 6:
            cctvs.append([i, j])
ans = 100


def change(y, x, arr, d):
    # print('[change] 호출됨. %d행 %d열'%(y, x))
    copy_arr = deepcopy(arr)
    if d[0]:
        ny = y
        while True:
            ny -= 1
            if not (0 <= ny < r) or copy_arr[ny][x] == 6:
                break
            if copy_arr[ny][x] == 0:
                copy_arr[ny][x] = -1
            # print('d[0] == 1, %d행 %d열 -1로 변경'%(ny, x))
    if d[1]:
        ny = y
        while True:
            ny += 1
            if not (0 <= ny < r) or copy_arr[ny][x] == 6:
                break
            if copy_arr[ny][x] == 0:
                copy_arr[ny][x] = -1
            # print('d[1] == 1, %d행 %d열 -1로 변경'%(ny, x))

    if d[2]:
        nx = x
        while True:
            nx -= 1
            if not (0 <= nx < c) or copy_arr[y][nx] == 6:
                break
            if copy_arr[y][nx] == 0:
                copy_arr[y][nx] = -1
            # print('d[2] == 1, %d행 %d열 -1로 변경'%(y, nx))

    if d[3]:
        nx = x
        while True:
            nx += 1
            if not (0 <= nx < c) or copy_arr[y][nx] == 6:
                break
            if copy_arr[y][nx] == 0:
                copy_arr[y][nx] = -1
            # print('d[3] == 1, %d행 %d열 -1로 변경'%(y, nx))
    return copy_arr


def dfs(arr, num):
    if num == len(cctvs):
        global ans
        result = 0
        for i in range(r):
            result += arr[i].count(0)
        ans = min(ans, result)
        return
    # copy_arr = deepcopy(arr)
    cctv = cctvs[num]
    for d in directions[arr[cctv[0]][cctv[1]]]:
        tmp = change(cctv[0], cctv[1], arr, d)
        dfs(tmp, num + 1)


if len(cctvs) == 0:
    ans = 0
    for i in range(r):
        ans += room[i].count(0)
    print(ans)
    exit(0)

dfs(room, 0)
print(ans)