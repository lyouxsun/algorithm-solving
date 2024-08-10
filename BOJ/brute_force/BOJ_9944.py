# 브루트 포스 - 9944번 - N*M 보드
## 모든 빈칸을 시작점으로 삼아서 그래프탐색
import sys
sys.setrecursionlimit(10 ** 6)

cycle = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def boundary(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False


def dfs(y, x, arr, cnt):  # cnt = 방문하지 않은 빈칸 수, 리턴값 = 이동해야 하는 칸
    result = -1
    if cnt == 0:
        return 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        while boundary(ny, nx) and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            cnt -= 1
            ny += dy[i]
            nx += dx[i]
        ny -= dy[i]
        nx -= dx[i]
        if not (ny == y and nx == x):  # 한칸도 이동하지 않은 경우
            tmp = dfs(ny, nx, arr, cnt)
            if tmp != -1:
                if result == -1 or result > tmp + 1:
                    result = tmp + 1
        while not (y == ny and x == nx):  # arr 원상복구
            arr[ny][nx] = 0
            cnt += 1
            ny -= dy[i]
            nx -= dx[i]
    return result


while True:
    try:
        n, m = map(int, input().split())
    except (ValueError, EOFError):  # ValueError, EOFError 가 발생하면 종료
        break
    cnt = 0
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        line = list(input())
        for j in range(m):
            if line[j] == '*':
                arr[i][j] = 1
            else:
                arr[i][j] = 0
                cnt += 1
    ans = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                tmp = dfs(i, j, arr, cnt - 1)
                if tmp != -1 and (ans == -1 or ans > tmp):
                    ans = tmp
                arr[i][j] = 0
    print("Case %d: %d" % (cycle, ans))
    cycle += 1
