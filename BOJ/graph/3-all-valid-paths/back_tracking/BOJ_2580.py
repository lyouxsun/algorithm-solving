# 백트래킹 - 2580번 - 스도쿠
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

ARR = [list(map(int, input().split())) for _ in range(9)]
ROW_USED = [[False] * 10 for _ in range(9)]
COL_USED = [[False] * 10 for _ in range(9)]
BOX_USED = [[False] * 10 for _ in range(9)]

blank = []
for r in range(9):
    for c in range(9):
        if ARR[r][c] == 0:
            blank.append((r, c))
        else:
            ROW_USED[r][ARR[r][c]] = True
            COL_USED[c][ARR[r][c]] = True
            BOX_USED[(r // 3) * 3 + (c // 3)][ARR[r][c]] = True


def back_tracking(idx):
    # 1. base condition
    if idx == len(blank):
        return True

    # 2. idx에 들어갈 숫자 찾기
    r, c = blank[idx]
    for num in range(1, 10):
        if not ROW_USED[r][num] and not COL_USED[c][num] and not BOX_USED[(r // 3) * 3 + (c // 3)][num]:
            ARR[r][c] = num
            ROW_USED[r][num] = True
            COL_USED[c][num] = True
            BOX_USED[(r // 3) * 3 + (c // 3)][num] = True
            if back_tracking(idx + 1):
                return True
            ROW_USED[r][num] = False
            COL_USED[c][num] = False
            BOX_USED[(r // 3) * 3 + (c // 3)][num] = False
            ARR[r][c] = 0
    return False


back_tracking(0)
for i in range(9):
    for j in range(9):
        print(ARR[i][j], end=' ')
    print()
