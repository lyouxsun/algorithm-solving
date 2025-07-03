# BFS - 4991번 - 로봇 청소기
## sol 1) 탈옥 문제처럼 여러 방향에서 최단거리 구한 후, 만나는 지점을 구해서 더한다.
## sol 2) 더러운 곳 최대 10개 -> 모든 방문 순서를 고려 -> 그 중 최단 경로를 찾기
import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
arr = []
vy, vx = 0, 0
r, c = 0, 0

# now -> next로 가는 최단 경로만 구해서 dict에 저장
def bfs(now):
    global arr, r, c
    visited = [[float('inf')] * c for _ in range(r)]
    visited[now[0]][now[1]] = 0
    q = deque([now])
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] != 'x':
                if visited[ny][nx] > visited[y][x] + 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
    return visited


while True:
    c, r = map(int, input().split())
    if c == 0 and r == 0:
        break
    num = 0

    # 1. 방 구조 입력받기 : 청소기와 더러운 칸 위치 배열에 추가하기
    arr = []
    dirty = []
    for i in range(r):
        arr.append(list(input().strip()))
        for j in range(c):
            if arr[i][j] == '*':
                dirty.append([i, j])
                num += 1
            elif arr[i][j] == 'o':
                vy, vx = i, j
                num += 1

    distance = [[0]*num for _ in range(num)]
    # 2. 모든 칸에서의 최단경로 미리 구해놓기
    dirty.insert(0, [vy, vx])
    # print(dirty)
    for i in range(num):
        v = bfs(dirty[i])
        for j in range(i + 1, num):
            distance[i][j] = v[dirty[j][0]][dirty[j][1]]
            distance[j][i] = v[dirty[j][0]][dirty[j][1]]

    # 3. 2번에서 구해놓은 값을 사용해서 모든 순서에 대한 거리 구하기
    ans = float('inf')
    orders = permutations(range(num))

    for order in orders:
        if order[0]!= 0:
            continue
        cnt = 0
        for i in range(num-1):
            # print('order[i]=',order[i], ' / order[i+1]=', order[i+1])
            cnt += distance[order[i]][order[i+1]]
        ans = min(ans, cnt)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)