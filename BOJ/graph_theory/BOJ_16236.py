# 그래프 이론 - 16236번 - 아기 상어
## 처음 상어의 크기 = 2 / 자신의 크기와 같은 수의 물고기를 먹어야 크기가 +1 커짐
## 물고기 크기 작아야만 먹을 수 있음 / 물고기 크기 같으면 지나갈 수 있음. 먹을 수는 없음 / 물고기 크키가 더 크면 지나갈 수 없음
## 더이상 먹을 수 있는 물고기가 없을 때 종료됨

# bfs (q) , size 변수, cnt 변수, 남아있는 물고기의수,
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
fish_num, size, sizeup_cnt, p = 0, 2, 0, []
shark_y, shark_x = 0, 0
fish = [0]*7
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(n):
        if 1 <= line[j] <= 6:
            fish[line[j]] += 1
        if arr[i][j] == 9:
            shark_y = i
            shark_x = j
            arr[i][j] = 0
# fish_num = fish[1]

ans = 0

def bfs(y, x, size):
    can_eat = []
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]  # 여기에 존재하는 먹이를 먹었는지 확인

    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n) and (0 <= nx < n) and (visited[ny][nx] == 0):
                if arr[ny][nx] <= size:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[y][x] + 1
                    if 0 < arr[ny][nx] < size:
                        can_eat.append((ny, nx, distance[ny][nx]))

    return sorted(can_eat, key=lambda x: (-x[2], -x[0], -x[1]))

cnt, ans = 0, 0
while True:
    fish = bfs(shark_y, shark_x, size)
    # print(fish)
    if len(fish) == 0:
        break
    ny, nx, dist = fish.pop()
    ans += dist
    arr[shark_y][shark_x], arr[ny][nx] = 0, 0
    shark_y, shark_x = ny, nx
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
    # print(arr)
    # print('ans=', ans)
    # print()

print(ans)

