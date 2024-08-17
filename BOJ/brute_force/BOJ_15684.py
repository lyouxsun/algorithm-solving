# 브루트 포스 - 15684번 - 사다리 조작
## 문제 조건에 따르면 최대 3개까지만 추가 가능 -> 3개의 다리 놓는 모든 경우의 수만 고려하면 됨  (270**3)
# c=세로선 수, b=다리 수, r=가로선 수

c, b, r = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(b)]
ans = 5
if b == 0:
    print(0)
    exit()

ladder = [[0] * (c + 1) for _ in range(r + 1)]
for b in bridges:
    ladder[b[0]][b[1]] = 1
    ladder[b[0]][b[1] + 1] = -1


def go():  # 세로줄
    for column in range(1, c + 1):
        place = column
        for k in range(1, r + 1):
            place += ladder[k][place]
        if place != column:
            return False
    return True


all_pairs = [[a, b] for a in range(1, r + 1) for b in range(1, c)]


def dfs(depth, idx):
    global ans
    if go():
        ans = min(ans, depth)
        return
    if depth >= 3 or ans <= depth:
        return
    for i in range(idx, len(all_pairs)):
        y, x = all_pairs[i]
        if ladder[y][x] == 0 and ladder[y][x + 1] == 0:
            ladder[y][x] = 1
            ladder[y][x + 1] = -1
            dfs(depth + 1, i + 1)
            ladder[y][x] = 0
            ladder[y][x + 1] = 0


if go():
    print(0)
else:
    dfs(0, 0)
    print(ans if 0 <= ans <= 3 else -1)
