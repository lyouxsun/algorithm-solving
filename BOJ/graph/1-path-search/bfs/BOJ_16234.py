# BFS - 16234번 - 인구 이동
## BFS 방문처리 시점 & 큐에 넣는 시점 주의하기!!!

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

n, l, r = list(map(int, input().split()))
land = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def grouping():
    visited = [[False for _ in range(n)] for _ in range(n)]
    groups = [[0 for _ in range(n)] for _ in range(n)]
    group_idx = 1
    group_dict = dict()

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_idx = bfs(group_dict, group_idx, groups, i, j, visited)
    return groups, group_dict, group_idx


def bfs(group_dict, group_idx, groups, i, j, visited):
    global n, l, r
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    # BFS 시작
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if ((0 <= ny < n) and (0 <= nx < n) and
                    not visited[ny][nx] and
                    (l <= abs(land[ny][nx] - land[y][x]) <= r)):
                if groups[y][x] != 0:
                    groups[ny][nx] = groups[y][x]
                    group_dict[groups[y][x]].add((ny, nx))
                elif groups[ny][nx] != 0:
                    groups[y][x] = groups[ny][nx]
                    group_dict[groups[ny][nx]].add((y, x))
                else:
                    groups[y][x] = group_idx
                    groups[ny][nx] = group_idx
                    group_dict[group_idx] = {(y, x), (ny, nx)}
                    group_idx += 1
                q.append((ny, nx))
                visited[ny][nx] = True
    return group_idx


while True:
    groups, group_dict, group_idx = grouping()
    # for i in range(n):
    #     print(groups[i])
    if not group_dict:
        print(cnt)
        break

    # 인구이동시키기
    for s in range(1, group_idx):
        size = len(group_dict[s])
        total = 0
        for (y, x) in group_dict[s]:
            total += land[y][x]
        end = total // size
        for (y, x) in group_dict[s]:
            land[y][x] = end
    # for i in range(n):
    #     print(land[i])
    # print()
    cnt += 1