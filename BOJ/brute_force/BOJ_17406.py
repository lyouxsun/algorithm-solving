# 브루트 포스 - 17406번 - 배열 돌리기 4
from itertools import permutations
import sys, copy

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] * n
spin = [0] * k
ans = float('INF')
for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(k):
    spin[i] = list(map(int, input().split()))

orders = list(permutations(spin))


def spin(copy_arr, r, c, s):
    # print('=====spin 이전=====')
    # for i in range(n):
    #     print(copy_arr[i])

    for i in range(1, s + 1):

        tmp = copy_arr[r - i][c + i]

        for w in range(c + i, c - i, -1):  # 위쪽 행 : 오른쪽으로 이동
            copy_arr[r - i][w] = copy_arr[r - i][w - 1]

        for z in range(r - i, r + i):  # 왼쪽 열 : 위로 이동
            copy_arr[z][c - i] = copy_arr[z + 1][c - i]
        for y in range(c - i, c + i):  # 아랫쪽 행 : 왼쪽으로 이동
            copy_arr[r + i][y] = copy_arr[r + i][y + 1]

        for x in range(r + i, r - i, -1):  # 오른쪽 열 : 아래로 이동
            copy_arr[x][c + i] = copy_arr[x - 1][c + i]

        copy_arr[r - i + 1][c + i] = tmp

    # print('=====spin 이후=====')
    # for i in range(n):
    #     print(copy_arr[i])


for order in orders:
    copy_arr = copy.deepcopy(arr)
    # print('회전 순서 =', order)
    for i in order:
        # print('회전 =', i)
        spin(copy_arr, i[0] - 1, i[1] - 1, i[2])
    for j in copy_arr:
        ans = min(ans, sum(j))

    # print('+++++ 회전 결과 +++++')
    # for i in range(n):
    #     print(copy_arr[i])
    # print('ans =', ans)
    # print()

print(ans)
