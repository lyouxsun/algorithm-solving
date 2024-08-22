# 그래프 탐색 - 4963번 - 섬의 개수 (DFS, 재귀)
# import sys
# input = sys.stdin.readline()
import sys
sys.setrecursionlimit(10**6)

di = [0, 0, -1, -1, -1, 1, 1, 1]
dj = [1, -1, 0, -1, 1, 0, -1, 1]

def dfs(i, j, w, h):
    arr[i][j] = 0   # 방문 처리
    for a in range(8):
        ni = i + di[a]
        nj = j + dj[a]
        if (0 <= ni < h) and (0 <= nj < w):
            if arr[ni][nj] == 1:
                arr[ni][nj] = 0
                dfs(ni, nj, w, h)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    # print(arr)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i, j, w, h)
    print(cnt)