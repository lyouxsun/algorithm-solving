# 위상정렬 - 14567번 - 선수과목
## result 배열에다가 각 과목을 듣기 전에 몇개를 들어야 하는지를 저장하면 됨 (거기에 +1)
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0, []] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][1].append(b)
    graph[b][0] += 1

q = deque()
for i in range(1, n+1):
    if graph[i][0] == 0:
        q.append((1, i))

# print(q)
result = [1]*(n+1)
while q:
    order, now = q.popleft()
    result[now] = order
    for next in graph[now][1]:
        graph[next][0] -= 1
        if graph[next][0] == 0:
            q.append((order+1, next))

for i in range(1, n+1):
    print(result[i], end=' ')