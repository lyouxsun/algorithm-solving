# BFS - 2234번 - 성곽
## 그래프로 따지면 부분 그래프의 개수, 각 그래프의 크기 구하기 -> 요소 개수, 크기는 BFS로!
from collections import deque

def walls(num):
    dir = [0, 0, 0, 0]      # 순서대로 상, 하, 좌, 우
    if num>>3 & 1:      # 왼쪽에서 1번째 비트가 1인지 확인 (+8)
        # 남쪽(아래쪽)에 벽이 있음
        dir[1] = 1
    if num>>2 & 1:      # 왼쪽에서 2번째 비트가 1인지 확인 (+4)
        # 동쪽(오른쪽)에 벽이 있음
        dir[3] = 1
    if num>>1 & 1:      # 왼쪽에서 3번째 비트가 1인지 확인 (+2)
        # 북쪽(위쪽)에 벽이 있음
        dir[0] = 1
    if num>>0 & 1:      # 왼쪽에서 4번째 비트가 1인지 확인 (+1)
        # 서쪽(왼쪽)에 벽이 있음
        dir[2] = 1
    return dir

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

c, r = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(r)]
# print(castle)
visited = [[-1]*c for _ in range(r)]        # 여기에 group 인덱스 저장하기
group_idx = 0
group_size = [0]*2500


def bfs(q, visited, group_idx):
    global r, c, group_size
    # print('[bfs] group_idx =', group_idx,', q =', q)
    while q:
        y, x = q.popleft()
        up, down, left, right = walls(castle[y][x])
        # print('y=', y, 'x=', x,'일 때의 ', up, down, right, left)
        if up == 0 and y>0:
            # print('up has wall')
            if visited[y-1][x] == -1:
                visited[y-1][x] = group_idx
                group_size[group_idx] += 1
                q.append([y-1, x])
                # print([y-1, x])
        if down == 0 and y<r-1:
            # print('down has wall')
            if visited[y + 1][x] == -1:
                visited[y+1][x] = group_idx
                group_size[group_idx] += 1
                q.append([y+1, x])
                # print([y+1, x])

        if right == 0 and x<c-1:
            # print('right has wall')
            if visited[y][x+1] == -1:
                visited[y][x+1] = group_idx
                group_size[group_idx] += 1
                q.append([y, x+1])
                # print([y, x+1])

        if left == 0 and x>0:
            # print('left has wall')

            if visited[y][x-1] == -1:
                visited[y][x-1] = group_idx
                group_size[group_idx] += 1
                q.append([y, x-1])
                # print([y, x-1])


for i in range(r):
    for j in range(c):
        if visited[i][j] == -1:
            visited[i][j] = group_idx
            q = deque()
            # print(group_idx)
            # print([i, j])
            q.append([i, j])
            group_size[group_idx] += 1
            bfs(q, visited, group_idx)
            group_idx += 1
            # print()

# for i in visited:
#     print(i)

ans3 = set()
for y in range(r):
    for x in range(c):
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<r and 0<=nx<c:
                if visited[y][x] != visited[ny][nx]:
                    ans3.add(group_size[visited[y][x]]+group_size[visited[ny][nx]])

ans3 = list(ans3)
print(group_idx)
print(max(group_size))
print(max(ans3))

# 7 3
# 11 10 10 10 10 10 6
# 15 15 15 15 15 15 13
# 11 10 10 10 10 10 14