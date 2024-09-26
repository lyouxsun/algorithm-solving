# bfs - 4485번 - 녹색 옷을 입은 애가 젤다지?
# [0, 0] -> [n-1, n-1] 로 이동할 때, 배열의 합의 최솟값 구하기
import sys
from collections import deque
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(n, arr):
    q = deque()
    ans = [[float('inf')]*n for _ in range(n)]
    ans[0][0] = arr[0][0]
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<= ny < n and 0<=nx<n:
                new_cost = ans[y][x] + arr[ny][nx]
                if ans[ny][nx] > new_cost:
                    ans[ny][nx] = new_cost
                    q.append((ny, nx))
    return ans[n-1][n-1]


cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    ans = bfs(n, arr)
    print("Problem %d: %d"%(cnt, ans))