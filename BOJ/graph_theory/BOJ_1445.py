# 다익스트라 - 1445번 - 일요일 아침의 데이터
import sys
from heapq import *

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

n, m = map(int, input().split())
start, end = [0, 0], [0, 0]
garden = []
for i in range(n):
    line = list(input().strip())
    garden.append(line)
    for j in range(m):
        if line[j] == 'S':
            start = [i, j]
        elif line[j] == 'F':
            end = [i, j]

# 쓰레기 옆 칸을 미리 계산한 값 저장
near_g_values = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if garden[y][x] == '.':
            for j in range(4):
                ny = y + dy[j]
                nx = x + dx[j]
                if 0 <= ny < n and 0 <= nx < m and garden[ny][nx] == 'g':
                    near_g_values[y][x] = 1
                    break

q = []
visited = [[0] * m for _ in range(n)]
heappush(q, (0, 0, start))
visited[start[0]][start[1]] = 1

while q:
    access_cost, near_cost, (y, x) = heappop(q)
    visited[y][x] = 1
    # print('y=', y, ', x=',x)
    if garden[y][x] == 'F':
        print(access_cost, near_cost)
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < n) and (0 <= nx < m) and not visited[ny][nx]:
            visited[ny][nx] = 1
            if garden[ny][nx] == 'g':
                heappush(q, (access_cost + 1, near_cost, (ny, nx)))

            elif garden[ny][nx] == '.':
                heappush(q, (access_cost, near_cost + near_g_values[ny][nx], (ny, nx)))

            else:  # S, F인 경우
                heappush(q, (access_cost, near_cost, (ny, nx)))


# 쓰레기를 통과해서 가는 최소 비용 경로 중에서!!!!! 쓰레기와 인접한 칸을 적게 지나는 경우를 따져야 한다.


