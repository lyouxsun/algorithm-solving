# BFS - 9376번 - 탈옥
## 죄수가 한명인 경우,, BFS를 이용해서 문을 여는 최소 횟수를 구하는 문제
import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(h, w, arr, start_y, start_x):
    cnt = [[-1] * w for _ in range(h)]
    q = deque()
    q.append([start_y, start_x])
    cnt[start_y][start_x] = 0
    while len(q) > 0:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < h) or not (0 <= nx < w):
                continue
            if arr[ny][nx] == '*':
                continue
            if cnt[ny][nx] != -1:       # 이미 방문한 칸
                continue
            if arr[ny][nx] == '#':
                cnt[ny][nx] = cnt[y][x] + 1
                q.append([ny, nx])
            if arr[ny][nx] == '.' or arr[ny][nx] == '$':
                cnt[ny][nx] = cnt[y][x]
                q.appendleft([ny, nx])  # 문이 없는 경로는 우선적으로 처리하도록 deque의 왼쪽에 추가
    # for j in range(h):
    #     print(cnt[j])
    # print()
    return cnt


cycle = int(input())
for i in range(cycle):
    h, w = map(int, input().split())
    h += 2
    w += 2
    arr = [list('.' * w) for _ in range(h)]
    now = []
    for j in range(1, h-1):
        arr[j] = ['.'] + list(input().strip()) + ['.']
        for k in range(w):
            if arr[j][k] == '$':
                now.append([j, k])
    # for j in range(h):
    #     print(arr[j])

    p0 = bfs(h, w, arr,0, 0)     # 밖에서 들어오는 경우
    p1 = bfs(h, w, arr, now[0][0], now[0][1])     # 죄수1이 탈출하는 경우
    p2 = bfs(h, w, arr, now[1][0], now[1][1])     # 죄수2가 탈출하는 경우

    ans = float('inf')
    for j in range(h):
        for k in range(w):
            if arr[j][k] =='*':
                continue
            current = p0[j][k] + p1[j][k] + p2[j][k]
            if current < 0:     # . 으로 된 칸이어도, 사방이 벽이어서 접근할 수 없는 공간이면 처리하지 말자
                continue
            if arr[j][k] == '#':
                current -= 2
            ans = min(ans, current)
    print(ans)
