# DFS - 2573번 - 빙산
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

R, C = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(R)]
if all(0 not in line for line in iceberg) or all(all(cell == 0 for cell in line) for line in iceberg):
    print(0)
    sys.exit(0)

# print(sea)


def dfs(v, y, x):
    v[y][x] = True
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ((0 <= ny < R) and (0 <= nx < C) and
                iceberg[ny][nx] > 0 and not v[ny][nx]):
            dfs(v, ny, nx)


ans = 0
while True:
    if all(all(cell == 0 for cell in line) for line in iceberg):
        print(0)
        sys.exit(0)
    # 1️⃣ 그룹 개수 확인하기 (2개 이상이면 종료) : dfs
    group_num = 0
    visited = [[False] * C for _ in range(R)]

    for y in range(R):
        if group_num >= 2:
            break
        for x in range(C):
            if group_num >= 2:
                break
            if iceberg[y][x] > 0 and not visited[y][x]:
                dfs(visited, y, x)
                group_num += 1
    # print(group_num)
    if group_num >= 2:
        break

    # 2️⃣ 인접한 바다 수 저장, 만약 빙하가 바다가 되면 여기에 즉시 반영하기!!!
    sea = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if (0 <= ny < R) and (0 <= nx < C) and iceberg[ny][nx] == 0:
                    sea[y][x] += 1

    # 3️⃣ 빙산 녹이기 : iceberg - sea
    for y in range(R):
        for x in range(C):
            if iceberg[y][x] > 0:
                iceberg[y][x] -= sea[y][x]
                if iceberg[y][x] <= 0:
                    iceberg[y][x] = 0
    ans += 1

print(ans)
