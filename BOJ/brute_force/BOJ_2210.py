# 브루트 포스 - 2210번 - 숫자판 점프
arr = []
s = set()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(5):
    arr.append(list(map(int, input().split())))


def dfs(num, y, x):
    global s
    if len(num) == 6:
        num_str = ''.join(map(str, num))
        s.add(int(num_str))
        # print('num is end = ', num)
        return
    num.append(arr[y][x])
    # print('dfs 호출 : y=%d, x=%d'%(y, x), num)

    for k in range(4):
        if (0 <= y + dy[k] < 5) and (0 <= x + dx[k] < 5):
            # print('num is growing = ', num)
            dfs(num[:], y + dy[k], x + dx[k])


for i in range(5):
    for j in range(5):
        dfs([], i, j)
print(len(s))
