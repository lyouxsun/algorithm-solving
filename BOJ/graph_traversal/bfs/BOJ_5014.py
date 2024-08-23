# BFS - 5014번 - 스타트링크
## s에서 g로 가야됨
from collections import deque

f, s, g, u, d = map(int, input().split())
building = [-1] * (f + 1)
building[s] = 0
q = deque()
q.append(s)


def bfs():
    while q:
        current = q.popleft()
        if building[g] != -1:
            # print(building)
            print(building[g])
            exit()
        if current + u <= f and building[current + u] == -1:
            building[current + u] = building[current] + 1
            q.append(current + u)
        if current - d > 0 and building[current - d] == -1:
            building[current - d] = building[current] + 1
            q.append(current - d)


bfs()
print('use the stairs')
