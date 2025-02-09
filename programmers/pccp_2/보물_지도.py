from collections import deque
import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def solution(n, m, hole):
    # n행 m열 짜리 배열이 2층 있는 3차원 배열 = result[층][행][열]
    inf = sys.maxsize
    result = [[[inf] * n for _ in range(m)] for _ in range(2)]

    for (x, y) in hole:
        result[0][y - 1][x - 1] = -1

    result[0][0][0] = 0  # 시작점 초기화
    q = deque()
    q.append((0, 0, 0))

    while q:
        d, y, x = q.popleft()
        # print(f'd={d}, y={y}, x={x}')

        # 1칸 이동
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n:
                if result[0][ny][nx] != -1 and result[d][y][x] + 1 < result[d][ny][nx]:
                    result[d][ny][nx] = result[d][y][x] + 1
                    q.append((d, ny, nx))

        # 2칸 이동
        if d == 0:
            for i in range(4):
                ny = y + 2 * dy[i]
                nx = x + 2 * dx[i]
                if 0 <= ny < m and 0 <= nx < n:
                    if result[0][ny][nx] != -1 and result[d][y][x] + 1 < result[1][ny][nx]:
                        result[1][ny][nx] = result[d][y][x] + 1
                        q.append((1, ny, nx))

    # for i in range(2):
    #     for j in range(m):
    #         print(result[i][j])
    #     print()

    if result[1][m-1][n-1] > 1000000:
        return -1
    return min(result[0][m-1][n-1], result[1][m-1][n-1])
