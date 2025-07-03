# 동적 프로그래밍 - 17069번 - 파이프 옮기기 2
## dp -> 3차원 배열의 dp 테이블 이용
# dp[i][j][a] = b : arr[i][j] 까지 a방향 (0/1/2 : 수평/수직/대각선) 으로 이동할 수 있는 경우의 수

import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
ans = 0

dp_h = [[0] * n for _ in range(n)]
dp_v = [[0] * n for _ in range(n)]
dp_d = [[0] * n for _ in range(n)]

for i in range(1, n):
    if arr[0][i] == 1:
        break
    dp_h[0][i] = 1  # horizontal

# print('dp_h=', dp_h)
# print('dp_v=', dp_v)
# print('dp_d=', dp_d)

# h면 -> h, d 가능 // v면 -> v, d 가능 // d면 -> h, v, d 가능
for i in range(1, n):  # 헹
    for j in range(1, n):  # 열
        if (i == 0 and j == 0) or (arr[i][j] == 1):
            continue
        # 수평 (horizontal) : 0
        if arr[i][j] == 0:
            dp_h[i][j] = dp_h[i][j - 1] + dp_d[i][j - 1]

        # 수직 (vertical) : 1
        if arr[i][j] == 0:
            dp_v[i][j] = dp_v[i - 1][j] + dp_d[i - 1][j]

        # 대각선 (diagonal) : 2
        if arr[i - 1][j - 1] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            dp_d[i][j] = dp_h[i - 1][j - 1] + dp_v[i - 1][j - 1] + dp_d[i - 1][j - 1]

if arr[n - 1][n - 1] == 1:
    print(0)
else:
    print(dp_h[n - 1][n - 1] + dp_v[n - 1][n - 1] + dp_d[n - 1][n - 1])
