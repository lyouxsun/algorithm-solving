# 백트래킹 - 2239번 - 스도쿠
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

LIST = [list(map(int, input().strip())) for _ in range(9)]
NUMBER = [i for i in range(1, 10)]
# ex. row_used[i][8] : i번째 행에 8이 있는지 없는지
row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]


def set_used(row, col, num, isUsed):
    row_used[row][num] = isUsed
    col_used[col][num] = isUsed
    box_row = row // 3
    box_col = col // 3
    # print('box_used_idx =', box_row * 3 + box_col)
    box_used[box_row * 3 + box_col][num] = isUsed



def is_box_used(row, col, num):
    box_row = row // 3
    box_col = col // 3
    # print('box_used_idx =', box_row * 3 + box_col)
    return box_used[box_row * 3 + box_col][num]


## 시간초과를 해결하기 위해 빈칸(0) 위치 미리 저장해두기
BLANK = list()
for r in range(9):
    for c in range(9):
        if LIST[r][c] == 0:
            BLANK.append((r, c))
        else:
            set_used(r, c, LIST[r][c], True)


def back_tracking(idx):
    # 1. base condition
    if idx == len(BLANK):
        return True

    # 2. 할일을 하자 : 내가 숫자를 채워야 하는 경우
    row, col = BLANK[idx]
    for num in NUMBER:
        # -> 없으면 그 숫자로 할당하고 다음 재귀 호출
        if not row_used[row][num] and not col_used[col][num] and not is_box_used(row, col, num):
            # print('row=', row, ', col=', col, ', num=', num)
            LIST[row][col] = num
            set_used(row, col, num, True)

            if back_tracking(idx + 1):  # 값을 성공적으로 채운 경우
                return True

            # 실패해서 돌아온 경우
            LIST[row][col] = 0
            set_used(row, col, num, False)
    # 3. 빠꾸 (들어올 수 있는 숫자가 없다)
    return False


back_tracking(0)
for r in LIST:
    print(''.join(str(num) for num in r))
