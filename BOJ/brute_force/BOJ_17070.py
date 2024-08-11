# 브루트 포스 - 17070번 - 파이프 옮기기 1
## 매 경우마다 DFS를 통해 이동 가능한 방법을 카운트하기

import sys

# sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
ans = 0

directions = {
    'h': [[0, 1]],  # horizontal
    'v': [[1, 0]],  # vertical
    'd': [[0, 1], [1, 0], [1, 1]]  # diagonal
}


# h면 -> h, d 가능 // v면 -> v, d 가능 // d면 -> h, v, d 가능

def dfs(r, c, st):
    # print('r=%d, c=%d, st=%s' % (r, c, st))
    if r == n - 1 and c == n - 1:
        global ans
        ans += 1
        return
    d_flag = True
    for i in directions['d']:
        if (not (0 <= r + i[0] < n) or not (0 <= c + i[1] < n)) or arr[r + i[0]][c + i[1]] != 0:
            d_flag = False
    if d_flag:
        dfs(r + 1, c + 1, 'd')
    if st == 'h' or st == 'd':
        if (0 <= r < n) and (0 <= c + 1 < n) and arr[r][c + 1] == 0:
            dfs(r, c + 1, 'h')
    if st == 'v' or st == 'd':
        if (0 <= r + 1 < n) and (0 <= c < n) and arr[r + 1][c] == 0:
            dfs(r + 1, c, 'v')


if arr[n-1][n-1] == 1:
    print(0)
else:
    dfs(0, 1, 'h')
    print(ans)
