# 위상정렬 - 2252번 - 줄 세우기
# a b : a가 b의 앞에 서야함
import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    in_degree[b] += 1
    graph[a].append(b)

h = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(h, i)

while h:
    now = heapq.heappop(h)
    print(now, end=' ')
    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(h, i)
