# 위상정렬 - 1516번 - 게임개발
import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
cost = [0] * (v + 1)
indegree = [0] * (v+1)
graph = [[] for _ in range(v + 1)]
for i in range(v):
    line = list(map(int, input().split()))
    cost[i + 1] = line.pop(0)
    # print(line)
    for j in line:
        if j == -1:
            break
        indegree[i + 1] += 1
        graph[j].append(i + 1)

result = [0] * (v + 1)
q = deque()
for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result[now] += cost[now]
    for next in graph[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now])
        if indegree[next] == 0:
            q.append(next)
for i in range(1, v+1):
    print(result[i])

# 5
# 10 -1
# 20 1 -1
# 30 2 -1
# 40 3 5 -1
# 100 -1