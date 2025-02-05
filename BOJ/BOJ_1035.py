# 백트래킹 - 1035번 - 조각 움직이기
import sys
from collections import deque
input = sys.stdin.readline

# 방향 벡터 (좌, 우, 상, 하)
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

piece = []
for i in range(5):
    line = list(input().strip())
    for j in range(5):
        if line[j] == '*':
            piece.append((i, j))

num = len(piece)


def is_connected(pieces):
    if not pieces:
        return False

    pieces_set = set(pieces)
    queue = deque([pieces[0]])
    visited = {pieces[0]}
    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]

            if (ny, nx) in pieces_set and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx))

    return len(visited) == len(pieces)


def quest(visited, p, cnt):
    global ans

    if is_connected(p):
        ans = min(ans, cnt)
        return

    for i in range(len(p)):
        y, x = p[i]

        for j in range(4):
            ny, nx = y + dy[j], x + dx[j]

            if 0 <= ny < 5 and 0 <= nx < 5 and (ny, nx) not in p:
                temp_p = p[:i] + [(ny, nx)] + p[i + 1:]
                state = frozenset(temp_p)

                if state not in visited:
                    visited.add(state)
                    quest(visited, temp_p, cnt + 1)


ans = float('inf')
visited = set()
visited.add(frozenset(piece))
quest(visited, piece, 0)

print(ans)
