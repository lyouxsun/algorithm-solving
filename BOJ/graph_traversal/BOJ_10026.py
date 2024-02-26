# 그래프 탐색 - 10026번 - 적록색약 (DFS, 재귀)

# 1
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
dw = [-1, 1, 0, 0]
dh = [0, 0, -1, 1]
arr = []
visited = [[0 for _ in range(n)] for _ in range(n)]

# 2
for i in range(n):
    arr.append(list(input()))  # 문자 하나씩 배열에 저장하려면 split()을 사용하면 안된다! 이렇게 저장해야 됨!!!

# 3
def A_dfs(h, w):
    visited[h][w] = 1
    for i in range(4):
        nw = w + dw[i]
        nh = h + dh[i]
        if (0 <= nw < n) and (0 <= nh < n):
            if visited[nh][nw] == 0 and arr[nh][nw] == arr[h][w]:
                # visited[nh][nw] = 1
                A_dfs(nh, nw)
    return


def B_dfs(h, w):
    for i in range(4):
        nw = w + dw[i]
        nh = h + dh[i]
        if (0 <= nw < n) and (0 <= nh < n):
            if visited[nh][nw] == 0:
                if (arr[h][w] == 'B' and arr[nh][nw] == 'B') or (arr[h][w] != 'B' and arr[nh][nw] != 'B'):
                    visited[nh][nw] = 1
                    B_dfs(nh, nw)
    return

# 4
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            A_dfs(i, j)
            cnt += 1
print(cnt, end=' ')

cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            B_dfs(i, j)
            cnt += 1

print(cnt)