# BOJ - 17142번 - 연구소3
## deepcopy 말고 원상복구하는 방법 사용해서 시간 줄이기!
## 핵심 : 비활성 바이러스는 지나갈 수는 있지만 퍼뜨려야 하는 대상은 아니다
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')

n, v = map(int, input().split())
lab = []
virus = []
empty_cnt = 0
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == 2:
            virus.append([i, j])
        elif lab[i][j] == 0:  # 0, 빈칸인 경우
            empty_cnt += 1
# print(lab)
if empty_cnt == 0:
    print(0)
    exit()

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(comb):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    for (vy, vx) in comb:
        visited[vy][vx] = 0
        q.append([vy, vx])
    max_time, fill = 0, 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if lab[ny][nx] == 2 and visited[ny][nx] == -1:        # 비활성
                    visited[ny][nx] = visited[y][x] +1
                    q.append([ny, nx])
                    continue
                if lab[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
                    if lab[ny][nx] == 0:
                        fill+=1
                        max_time = max(max_time, visited[ny][nx])
            if fill == empty_cnt:
                return max_time
    return INF

combs = list(combinations(virus, v))
ans = INF
for comb in combs:
    tmp = bfs(comb)
    # print(tmp)
    ans = min(ans, tmp)
if ans == INF:
    print(-1)
else:
    print(ans)
