# 14502번 - 그래프 탐색 - 연구소
## 1. 벽 3개를 세우는 모든 경우의 수 고려 (dfs)
## 2. 바이러스 확산 -> 그 때 남는 빈칸의 수 cnt (둘 다 bfs)
## 3. cnt의 최댓값 출력


from collections import deque
import copy
import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6) ## 이 코드 하나 추가했다고 Pypy3에서 메모리초과 발생..

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]


def bfs():
    test_lab = copy.deepcopy(arr)
    q = deque()
    for i in range(h):
        for j in range(w):
            if test_lab[i][j] == 2:
                q.append((i, j))
    while len(q) > 0:
        xh, xw = q.popleft()
        for i in range(4):
            nh = xh + dh[i]
            nw = xw + dw[i]
            if (0 <= nh < h) and (0 <= nw < w):
                if test_lab[nh][nw] == 0:
                    test_lab[nh][nw] = 2
                    q.append((nh, nw))


    global ans  # ans를 전역 변수로 사용하겠다고 명시
    cnt_0 = 0
    for row in test_lab:
        cnt_0 += row.count(0)
    ans = max(ans, cnt_0)


def create_wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 0:
                arr[i][j] = 1
                create_wall(wall_cnt + 1)
                arr[i][j] = 0


# 그래프 리스트로 입력 받기
h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

ans = 0
create_wall(0)
print(ans)
