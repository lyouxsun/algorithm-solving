# 브루트 포스 - 16924번 - 십자가 찾기
##  n행 m열 격자판 -> 주어진 격자판을 여러 개의 십자가로 만들 수 있는가
## 입력받을 때 십자가 부분을 1, 아닌 부분을 0으로 입력받음 -> 만들 수 있는 부분은 -1로 바꾸기
# -> 만약 마지막에도 1이 남아있으면 -1 출력 // 1이 없으면 십자가 개수랑 위치 출력

## 힌트 : 모든 *을 십자가의 중앙이라고 가정하고, 최대한 크게 그려보자!

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans_list = []

for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '.':
            arr[i][j] = 0
        else:
            arr[i][j] = 1
# print(arr)


## min(n, m) 크기의 십자가부터 1인 십자가까지 격자판 안에 있는지 for문을 돌며 확인
def change_arr(y, x, size):
    ans_list.append(f"{y + 1} {x + 1} {size}")
    # print("================================")
    # print(f"{y + 1} {x + 1} {size}")
    # print(arr)

    arr[y][x] = -1
    for i in range(1, size+1):
        for j in range(4):
            arr[y + dy[j] * i][x + dx[j] * i] = -1
    # print(arr)
    # print("================================")

def is_cross(y, x):
    size = 0
    # 십자가의 최대 크기 구하기
    while (0 <= x - (size+1)) and (x + (size+1) < m) and (0 <= y - (size+1)) and (y + (size+1) < n):
        for i in range(4):
            if arr[y + (size+1) * dy[i]][x + (size+1) * dx[i]] == 0:
                return size
        size += 1
    return size


# 최종 십자가를 1 -> -1 로 바꿔주기

# x, y : 십자가 중심의 좌표
# i : 십자가의 크기
ans = 0
for y in range(1, n):
    for x in range(1, m):
        if arr[y][x] != 0:
            size = is_cross(y, x)
            if size > 0:
                ans += 1
                change_arr(y, x, size)

# print(arr)
for i in arr:
    if 1 in i:
        print(-1)
        exit()
else:
    print(ans)
    # print(arr)
    for i in ans_list:
        print(i)

# 5 7
# ..*.*..
# .*****.
# ***.***
# .*****.
# ..*.*..
# 답 : 6
# 2 3 1
# 2 5 1
# 3 2 1
# 3 6 1
# 4 3 1
# 4 5 1