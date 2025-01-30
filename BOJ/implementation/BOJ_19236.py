# 구현 - 19236번 - 청소년 상어
import sys
import copy
input = sys.stdin.readline

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [1, 0, -1, -1, -1, 0, 1, 1]

coord = dict()      # 물고기 번호 : (y, x, d) 물고기 위치와 방향
result = 0
sy, sx, sd = 0, 0, 0
arr = [[0] * 4 for _ in range(4)]
arr[0][0] = -1

# 1. 초기설정 + 상어 들어옴
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        if i == 0 and j == 0:
            result = line[j * 2]
            sd = line[j * 2 + 1] % 8
            continue
        arr[i][j] = line[j * 2]
        coord[line[j * 2]] = (i, j, line[j * 2 + 1] % 8)        # (y, x, d) 물고기 위치와 방향

# for i in range(1, 17):
#     print(f'물고기 번호 = {i}, 좌표 =[{coord[i][0]}][{coord[i][1]}], 방향 = {coord[i][2]}')

def back_tracking(ans, sy, sx, sd, old_arr, old_coord):
    global result
    arr = copy.deepcopy(old_arr)
    coord = copy.deepcopy(old_coord)

    # 2 - 물고기 이동
    fist_move(arr, coord)

    # 1 - base condition
    can_move = False
    for i in range(1, 4):
        nsy, nsx = sy + dy[sd] * i, sx + dx[sd] * i
        if (0 <= nsy < 4 and 0 <= nsx < 4) and arr[nsy][nsx] > 0:
            can_move = True
            break
    if not can_move:
        result = max(result, ans)
        return


    # 3 - 상어의 이동 가능한 모든 경우 다 고려해서 재귀 호출
    for i in range(1, 4):

        nsy, nsx = sy + dy[sd] * i, sx + dx[sd] * i
        if (0 <= nsy < 4 and 0 <= nsx < 4) and arr[nsy][nsx] > 0:

            fish_num = arr[nsy][nsx]
            y, x, d = coord[fish_num]

            # 상어 이동
            del coord[fish_num]      # 물고기 삭제
            arr[nsy][nsx] = -1      # 상어가 이동 할 위치
            arr[sy][sx] = 0         # 상어의 이동 전 위치

            back_tracking(ans + fish_num, nsy, nsx, d, arr, coord)

            coord[fish_num] = [y, x, d]
            arr[nsy][nsx] = fish_num
            arr[sy][sx] = -1

    return


def fist_move(arr, coord):

    for i in range(1, 17):

        ## Q. 이렇게 coord에서 아예 제거하는 방식이 아니라 [-1, -1, -1] 로 초기화하는 방식을 썼더니 틀렸다... 왜그럴까??
        if i not in coord or coord[i][0] == -1:  # 이미 잡아먹힌 물고기
            continue

        fy, fx, fd = coord[i]
        if fy == -1 and fx == -1:
            continue
        for _ in range(8):
            nfy, nfx = fy + dy[fd], fx + dx[fd]
            if (0 <= nfy < 4 and 0 <= nfx < 4) and arr[nfy][nfx] >= 0:  # 이동 가능한 경우
                if arr[nfy][nfx] > 0:  # 이동할 자리에 물고기가 있는 경우 -> 스왑
                    tmp = arr[nfy][nfx]
                    arr[fy][fx], arr[nfy][nfx] = arr[nfy][nfx], arr[fy][fx]
                    coord[tmp] = [fy, fx, coord[tmp][2]]
                    coord[i] = [nfy, nfx, fd]
                else:  # 이동할 자리에 물고기가 없는 경우
                    arr[fy][fx] = 0
                    arr[nfy][nfx] = i
                    coord[i] = [nfy, nfx, fd]
                break
            fd = (fd + 1) % 8

back_tracking(result, sy, sx, sd, arr, coord)
print(result)

