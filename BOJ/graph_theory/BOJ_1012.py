# 그래프 이론 - 1012번 - 유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

# x : 몇번째 열에 있는가
# y : 몇번째 행에 있는가
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0

def bfs(b, a):
    q = deque()
    arr[b][a] = 0
    q.append((b, a))

    while q:
        y, x = q.popleft()
        arr[y][x] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < M) and (0 <= ny < N):
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    q.append((ny, nx))

cycle = int(input())
# 그래프 만들기
for _ in range(cycle):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # 그래프 탐색하기
    for x in range(M):
        for y in range(N):
            if arr[y][x] == 1:
                bfs(y, x)
                cnt += 1
    print(cnt)