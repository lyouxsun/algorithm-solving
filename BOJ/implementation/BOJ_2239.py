# 백트래킹 - 2239번 - 스도쿠
## 🚨🚨3*3 박스 검사를 빼먹음!!!!🚨🚨
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

LIST = [list(map(int, input().strip())) for _ in range(9)]

# print(LIST)

def back_tracking(row, col):
    print()
    print('row=', row, ', col=', col)
    for i in range(9):
        print(LIST[i])
    # 1. base condition
    if row == 9:
        for r in LIST:
            print(''.join(str(num) for num in r))
        sys.exit()

    # 2. 할일을 하자
    if LIST[row][col] != 0:
        if col == 8:
            back_tracking(row + 1, 0)
        else:
            back_tracking(row, col + 1)
    else:
        invalid = set()
        for i in range(9):
            invalid.add(LIST[row][i])
            invalid.add(LIST[i][col])
        print('invalid =', invalid)
        for num in range(1, 10):
            # 행, 열에 num 숫자가 있는지 확인
            if num in invalid:
                continue
            # -> 없으면 그 숫자로 할당하고 다음 재귀 호출
            invalid.add(num)
            LIST[row][col] = num
            if col == 8:
                back_tracking(row + 1, 0)
            else:
                back_tracking(row, col + 1)
        # 3. 빠꾸 (들어올 수 있는 숫자가 없다)
        return


back_tracking(0, 0)
