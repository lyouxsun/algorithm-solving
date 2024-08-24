# BFS - 16932번 - 모양 만들기
## 2차원 배열 탐색이니까 bfs!!
## 1그룹의 위치&크기를 미리 기록해 놓음(bfs) -> 0을 1로 바꾼 후 인접해 있는 그룹의 크기만 더하자!(bfs)
from collections import deque

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

## 그룹을 어떻게 저장하는게 좋을까...
group_num = 0  # 그룹의 개수
group = [[0] * c for _ in range(r)]         # 각 좌표에는 자기 자신의 그룹 인덱스를 넣어준다.
group_size = [0]
ans = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def make_group():
    global group_num, group, group_size
    q = deque()
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1 and group[i][j] == 0:
                group_num += 1
                group[i][j] = group_num
                q.append([i, j])
                size = 1
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0<= ny < r and 0<= nx < c:
                            if arr[ny][nx] == 1 and group[ny][nx] == 0:
                                group[ny][nx] = group_num
                                size += 1
                                q.append([ny, nx])
                group_size.append(size)


def search(y, x):
    global group, group_size
    result = 0
    group_idx = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if group[ny][nx] != 0 and  group[ny][nx] not in group_idx:
                result += group_size[group[ny][nx]]
                group_idx.append(group[ny][nx])
    return result


make_group()

# for a in group:
#     print(a)
# print(group_size)

for i in range(r):
    for j in range(c):
        if arr[i][j] == 0:
            arr[i][j] = 1
            ans = max(ans, search(i, j)+1)
            arr[i][j] = 0

print(ans)
