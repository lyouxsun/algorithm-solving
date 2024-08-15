# 브루트포스 - 14939번 - 불 끄기
## 모든 지점에서 불을 바꾸는 경우 -> 1024 (백트래킹, 재귀로ㄱㄱ)
## 추가) 위의 행에서 아래로만 가기 때문에, 한번 내려가면 다시 올라가지 않는다.
## 따라서 윗칸이 꺼져있다면 불을 그대로 두고, 윗칸이 켜져 있을 때에만 불을 바꾼다.
# 핵심!! : 첫번째 줄에서 전구를 바꿀 수 있는 모든 경우의 수 (2**10가지) 고려하기!!
from copy import deepcopy

arr = [list(input()) for _ in range(10)]

dy = [0, 0, 0, -1, 1]
dx = [0, -1, 1, 0, 0]
ans = float('INF')


def turn(y, x, copy_arr):
    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 10 and 0 <= nx < 10:
            if copy_arr[ny][nx] == 'O':
                copy_arr[ny][nx] = '#'
            else:
                copy_arr[ny][nx] = 'O'


for k in range(1 << 10):        # 2**10
    copy_arr = deepcopy(arr)
    result = 0

    for i in range(10):         # 첫째줄 전구 모든 경우의 수 구하기
        # (1024가지 - 1024를 2의 제곱들의 합으로 표현했을 때, 그 수에 따라 각 전구를 바꿀지가 결정됨)
        # ex) k = 7 = 2**2 + 2**1 + 2**0 -> 2, 1, 0번째 전구만 바꾸는 경우
        if k & (1 << i):
            turn(0, i, copy_arr)
            result += 1
    for i in range(1, 10):
        for j in range(10):
            if copy_arr[i - 1][j] == 'O':
                turn(i, j, copy_arr)
                result += 1
    if all('O' not in copy_arr[a] for a in range(10)):
        ans = min(ans, result)
        # for i in copy_arr:
        #     print(i)
        # print()

if ans == float('INF'):
    print(-1)
    exit(0)
print(ans)
