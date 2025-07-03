# dfs - 16956번 - 늑대와 양
r, c = map(int, input().split())
pasture = [0] * r
wolves = []
ans = 1
for i in range(r):
    pasture[i] = list(input())
    for j in range(c):
        if pasture[i][j] == 'W':
            wolves.append([i, j])
        if pasture[i][j] == '.':
            pasture[i][j] = 'D'


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if pasture[ny][nx] == 'S':
                global ans
                ans = 0
                return


for cood in wolves:
    bfs(cood[0], cood[1])


print(ans)
if ans == 1:
    for i in range(r):
        arr = ''.join(pasture[i])
        print(arr)
