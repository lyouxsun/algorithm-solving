# BFS - 17141번 - 연구소2
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

n, v = map(int, input().split())
lab = []
candidate = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == 0:
            lab[i][j] = float('inf')
        if lab[i][j] == 1:
            lab[i][j] = -1
        if lab[i][j] == 2:
            candidate.append([i, j])
            lab[i][j] = float('inf')
# print(lab)
# print(candidate)
ans = float('inf')
combs = list(combinations(candidate, v))
for comb in combs:
    arr = deepcopy(lab)
    q = deque()
    for (y, x) in comb:
        arr[y][x] = 0
        q.append([y, x])
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < n) and (0 <= nx < n):
                if arr[ny][nx] != -1:
                    if arr[ny][nx] > arr[cy][cx]+1:
                        arr[ny][nx] = arr[cy][cx]+1
                        q.append([ny, nx])
    # for i in range(n):
    #     print(arr[i])
    cnt = 0
    for i in range(n):
        cnt = max(cnt, max(arr[i]))
    if cnt != float('inf'):
        # print(cnt)
        # print()
        ans = min(ans, cnt)
    # print('='*30)
if ans == float('inf'):
    print(-1)
else:
    print(ans)