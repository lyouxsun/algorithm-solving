# 7569번 - 그래프 탐색 - 토마토
## 가로 : width / 세로 : length / 높이 : height (arr[h][l][w])
## 가까운 곳부터 차례대로 탐색하면 날짜를 카운트해야 함 -> bfs
## 최단경로 구하는 방법 : arr[i] = arr[이전순서] + 1 == 도달하기까지 걸린 횟수를 리스트에 저장
from collections import deque

dh = [-1, 1, 0, 0, 0, 0]
dl = [0, 0, -1, 1, 0, 0]
dw = [0, 0, 0, 0, -1, 1]

w, l, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(l)] for _ in range(h)]
q = deque([])


def bfs():
    while len(q) > 0:
        xh, xl, xw = q.popleft()
        day = arr[xh][xl][xw]
        for i in range(6):
            nh = xh + dh[i]
            nl = xl + dl[i]
            nw = xw + dw[i]
            if (0 <= nh < h) and (0 <= nl < l) and (0 <= nw < w):
                if arr[nh][nl][nw] == 0:
                    arr[nh][nl][nw] = day + 1
                    q.append((nh, nl, nw))
    ans = -1
    for i in range(h):
        for j in range(l):
            ans = max(ans, max(arr[i][j]))
            if 0 in arr[i][j]:
                print(-1)
                return
    print(ans - 1)


for i in range(h):
    for j in range(l):
        for k in range(w):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

bfs()
